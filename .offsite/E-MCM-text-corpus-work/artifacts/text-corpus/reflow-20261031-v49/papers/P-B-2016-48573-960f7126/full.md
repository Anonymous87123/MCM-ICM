# P-B-2016-48573-960f7126

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
For oﬃce use only T1 T2 T3 T4 Team Control Number 48573 Problem Chosen B For oﬃce use only F1 F2 F3 F4 2016 Mathematical Contest in Modeling (MCM/ICM) Summary Sheet

<!-- b000002 | title | pages [1] -->
Will We Survive in the Space Junk?

<!-- b000003 | heading | pages [1] -->
summary

<!-- b000004 | prose | pages [1] -->
We aim to devise a model evaluating the performance of an ODR (Orbital Debris Removal) system and propose the best alternative. Conclusion is drawn about whether there exist proﬁtable business chances illustrated in a time-dependent mode. Further analysis is conducted by AHP to assess the overall performance of ODR. We are also required to come up with a new method implementing collision avoidance activities.

<!-- b000005 | prose | pages [1] -->
The ﬁrst model simulating the debris removal process is built on ordinary diﬀerential equations. This model serves as a basis for the proﬁts model which generates the net gains as the diﬀerence of the ODR cost and total revenue. We conclude that it takes a private ﬁrm more than 50 years to beneﬁt economically from this industry. Currently there is no proﬁts to be made.

<!-- b000006 | prose | pages [1] -->
We extend the proﬁts model to include the recycling activities of debris. Results show that it has smaller beneﬁts than the non-recycled mode due to high recycling cost. Further extensions take varying sizes of debris and diﬀerent types of cleaners into account. We conclude that using one type of cleaner makes more proﬁts than using diﬀerent types.

<!-- b000007 | prose | pages [1] -->
The third model utilizes AHP to choose the best alternatives in terms of overall performance based on ﬁve factors. The SpaDE ODR system is evaluated to be the most favorable one.Our sensitivity analysis demonstrates that our ﬁrst debris removal model is robust to parameters changes. The AHP model is sensitive to the relative weights value of the ﬁve factors.

<!-- b000008 | prose | pages [1] -->
We additionally contrive a new method of collision avoidance. The advantages of traditional ”box” method and the ”collisional probability” method are incorporated in our new method.

<!-- b000009 | furniture | pages [2] -->
Team # 48573 Page 1 of 28

<!-- b000010 | heading | pages [2] -->
Contents

<!-- b000011 | source_object | pages [2] -->
1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 1.2 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . 3 1.3 Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 1.4 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 2 Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 2.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 2.2 Symbols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 2.3 Establishment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 2.4 Model II . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 3 Model Extension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 3.1 What if launching different cleaners? . . . . . . . . . . . . . . . . . 11 3.2 Is there a commercial opportunity? . . . . . . . . . . . . . . . . . . 14 3.2.1 The Proﬁt Motive . . . . . . . . . . . . . . . . . . . . . . . . 14 3.2.2 The Results . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 3.3 What if recycling the debris? . . . . . . . . . . . . . . . . . . . . . . 15 4 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 5 Evaluation Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 5.1 Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 5.2 Target Cleaner Selection . . . . . . . . . . . . . . . . . . . . . . . . 19

<!-- b000012 | furniture | pages [3] -->
Team # 48573 Page 2 of 28

<!-- b000013 | source_object | pages [3] -->
5.3 Analytic Hierarchy Process ( AHP ) . . . . . . . . . . . . . . . . . . 19 5.4 A proper approach to avoid collision . . . . . . . . . . . . . . . . . 22 6 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . 24 6.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 6.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 7 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 Executive Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

<!-- b000014 | furniture | pages [4] -->
Team # 48573

<!-- b000015 | furniture | pages [4] -->
Page 3 of 28

<!-- b000016 | heading | pages [4] -->
1 Introduction

<!-- b000017 | heading | pages [4] -->
1.1 Background

<!-- b000018 | prose | pages [4] -->
Ever since the ﬁrst spacecraft Sputnik 1 was sent into space by human in 1957, there have been about 7100 spacecraft launched into space until now [1]. The problem arising with this augmenting number is the leftover debris in s- pace resulting from explosions of defunct artiﬁcial satellites, collisions between spacecraft and so on. Currently the earth is surrounded by approximately 21,000 bits of debris larger than 10 cm and much more of it in smaller sizes [2]. Figure 1 shows the debris distribution in view of LEO (low earth orbit).

<!-- b000019 | caption | pages [4] -->
Figure 1: LEO view

<!-- b000020 | prose | pages [4] -->
Large amount of debris poses an unneglectable threat on operating space- craft since collisions with even a small piece of such debris will involve consid- erable energy and destroy the satellites [3]. Figure 2 illustrates the number of different types of debris from year 1956 to 2012. With the space debris issue be- coming more and more alarming as people keep sending multipurpose satellites into space, a potential proﬁtable opportunity exists for private ﬁrms to commer- cialize the space debris removal. Different ODR (Orbital Debris Removal) sys- tems under developing which can be adopted by companies along with other factors such as risks, cost etc. should all be considered in this business mode [9].

<!-- b000021 | furniture | pages [5] -->
Team # 48573

<!-- b000022 | furniture | pages [5] -->
Page 4 of 28

<!-- b000023 | caption | pages [5] -->
Figure 2: Satellites around earth

<!-- b000024 | heading | pages [5] -->
1.2 Restatement of the Problem

<!-- b000025 | prose | pages [5] -->
We are required to build a mathematical model to judge whether a private ﬁrm can beneﬁt from removing space debris via a certain method or combina- tions of different alternatives. The problem is analyzed into three parts:

<!-- b000026 | prose | pages [5] -->
• Build a model to simulate the debris elimination process and predict the effect of the orbital debris removal system.

<!-- b000027 | prose | pages [5] -->
• Propose the best method using a mathematical criterion.

<!-- b000028 | prose | pages [5] -->
• Provide innovative schemes for collision avoidance if no viable commer- cial opportunity exists.

<!-- b000029 | prose | pages [5] -->
Notions to notice:

<!-- b000030 | prose | pages [5] -->
• The debris in this paper only includes the ones larger than 10 cm that can be traced and processed by the ”cleaner”. By ”debris” we refer to the man- made objects in orbit around the earth which no longer serve a useful pur- pose [3]. The meteorite pieces are not contained in the problem domain.

<!-- b000031 | prose | pages [5] -->
• In the commercial mode, the private ﬁrms only involve in business of debris removal but not in other ﬁled-related industries such as satellites launching. In our problem domain, companies can only beneﬁt from ODR systems.

<!-- b000032 | furniture | pages [6] -->
Team # 48573

<!-- b000033 | furniture | pages [6] -->
Page 5 of 28

<!-- b000034 | heading | pages [6] -->
1.3 Literature Review

<!-- b000035 | prose | pages [6] -->
Donald Kessler advanced a mathematical model in 1978 to predict the rate at which the debris belt might form. It was concluded that the debris ﬂux would in- crease exponentially with time even though zero net input rate were maintained [4], which is referred to as the ”Kessler Syndrome” [5].This could be traced back as the ﬁrst notion to address the space debris problem.

<!-- b000036 | prose | pages [6] -->
Ever since the concept has been put forward, numerous solutions have been proposed to deal with this issue. These technologies are mainly categorized as follows: the ground-based approaches to active debris removal and the passive de-orbit systems which are deployed at the end of life. For the ground based ap- proaches, high powered laser systems can remove debris in the low earth orbit. In the passive de-orbit systems, inﬂatable balloons, inﬂatable tube membranes, suspendable tethers etc. are all simple and easily deployable drag systems that can hasten the speed of debris de-orbiting process [6].

<!-- b000037 | heading | pages [6] -->
1.4 Results

<!-- b000038 | prose | pages [6] -->
We use a system of ordinary differential equations to simulate the environ- ment of the space from qualitative and quantitative perspectives, with ODR present or not. The results of modeling generate approximate amounts of debris and remaining spacecraft based on their initial numbers. We concluded that O- DR can help eliminate the debris while protecting the spacecraft effectively. The proﬁts of different methods are calculated by subtracting the ODR systems’ cost from the total value of protected satellites. Next we use AHP (Analytic Hierar- chy Process) to evaluate the performance of different ODR systems in regards to our pre-set essential factors. The result indicates the SpaDE ODR system to be the most favorable one. Our results show that given the best model, the de- bris removal industry will not make money in the current situation, but will be proﬁtable in more than 50 years from now on.

<!-- b000039 | heading | pages [6] -->
2 Models

<!-- b000040 | heading | pages [6] -->
2.1 Overview

<!-- b000041 | prose | pages [6] -->
The space debris removal problem encompasses a multitude of factors. To simplify the description, we concentrate on the numerical perspective and study dynamics of the number of satellites and space debris orbiting the earth.

<!-- b000042 | furniture | pages [7] -->
Team # 48573

<!-- b000043 | furniture | pages [7] -->
Page 6 of 28

<!-- b000044 | heading | pages [7] -->
Assumptions and Justiﬁcations

<!-- b000045 | prose | pages [7] -->
• There are only two types of satellites: in high orbit or low orbit.

<!-- b000046 | prose | pages [7] -->
• All the destructive space debris is the same and evenly distributed around the earth.

<!-- b000047 | prose | pages [7] -->
• The collision between a satellite and a debris is assumed to be a catastroph- ic one in which the satellite is destroyed into pieces. The number of debris generated in one collision is constant, regardless of the sizes of different spacecraft. The debris is of the same size.

<!-- b000048 | heading | pages [7] -->
2.2 Symbols

<!-- b000049 | prose | pages [7] -->
• t: time (measured in years)

<!-- b000050 | prose | pages [7] -->
• Sh: satellite population in high orbit

<!-- b000051 | prose | pages [7] -->
• Sl: satellite population in low orbit

<!-- b000052 | prose | pages [7] -->
• D: debris population

<!-- b000053 | prose | pages [7] -->
• β: collision coefﬁcient between satellite and debris

<!-- b000054 | prose | pages [7] -->
• α: number of satellites launched per year

<!-- b000055 | prose | pages [7] -->
• γ : number of satellites expired per year

<!-- b000056 | prose | pages [7] -->
• ρ: proportion of retired satellites that turn into space debris

<!-- b000057 | prose | pages [7] -->
• N: number of fragments when a satellite crashes

<!-- b000058 | prose | pages [7] -->
• λ: natural growth rate of space debris

<!-- b000059 | heading | pages [7] -->
2.3 Establishment

<!-- b000060 | heading | pages [7] -->
Assumptions and Justiﬁcaitons

<!-- b000061 | prose | pages [7] -->
• The earth is a close system. There is no space junk from outer space that enters into this system.

<!-- b000062 | prose | pages [7] -->
• The debris will not decompose nor spontaneously fall into the earth’s at- mosphere. It will always orbit the earth unless external impact exists.

<!-- b000063 | furniture | pages [8] -->
Team # 48573

<!-- b000064 | furniture | pages [8] -->
Page 7 of 28

<!-- b000065 | prose | pages [8] -->
• Among all types of space debris, we only concentrate on the relatively large objects, since there are hundreds of millions of debris in the space and not all of them are deadly to the satellites.

<!-- b000066 | prose | pages [8] -->
(1) The satellite part

<!-- b000067 | prose | pages [8] -->
The change of satellite population can occur in three ways: new satellites that launched into space, retired satellites and satellites destroyed in the colli- sion. The statistics show that in the past several decades since the launching technology became mature, the numbers of satellites launched each year are not remarkably different. So we treat the number launched α as constant and so is the number of retired satellites γ. Therefore, by introducing a collision co- efﬁcient β, the dynamics of satellite population in high and low orbit can be depicted as

<!-- b000068 | prose | pages [8] -->
dSh dt = −βhDSh + αh −γh (2.1)

<!-- b000069 | prose | pages [8] -->
dSl dt = −βlDSl + αl −γl (2.2)

<!-- b000070 | prose | pages [8] -->
(2) The debris part

<!-- b000071 | prose | pages [8] -->
Similar to the analysis above, we assume that space debris is created in three ways: the collision between satellite and debris, defunct satellites and natural growth rate of debris (caused by the collision among debris itself or boosters and dead spacecrafts). For simplicity, we also assume the number of fragment produced in collision to be the same, denoted by N, and a ﬁxed percentage of satellites transformed into space junk in the process of dying, denoted by γ. We also hold the annual growth rate of space debris λ to be constant. So the dynamics of the debris population can be described as

<!-- b000072 | prose | pages [8] -->
dD dt = (βhSh + βlSl)DN + (γh + γl)ρN + λD (2.3)

<!-- b000073 | prose | pages [8, 9] -->
By now we have constructed a system of ordinary differential equations with initial values dSh  dt = −βhDSh + αh −γh         dSl   dt = −βlDSl + αl −γl        dD dt = (βhSh + βlSl)DN1 + (γh + γl)ρN2 + λD         Sh(0) = Sh0, Sl(0) = Sl0         D(0) = D0 

<!-- b000074 | furniture | pages [9] -->
Team # 48573

<!-- b000075 | furniture | pages [9] -->
Page 8 of 28

<!-- b000077 | heading | pages [9] -->
(3) Test the Model

<!-- b000078 | prose | pages [9] -->
We use the data found on websites to test the validity of our model. Based on the initial values and the value of parameters, we can predict the number of satellites and debris in the future and see the consequence of increasing space debris.

<!-- b000079 | prose | pages [9] -->
• Sh: 0.482 (measured in thousand, according to Satellite Database[1])

<!-- b000080 | prose | pages [9] -->
• Sl: 0.589

<!-- b000081 | prose | pages [9] -->
• D: 21 (the relatively large objects, from Wikipedia)

<!-- b000082 | prose | pages [9] -->
• βh: 0.0000247 (calculated from the collisions occurred in recent years)

<!-- b000083 | prose | pages [9] -->
• βl: 0.0001213

<!-- b000084 | prose | pages [9] -->
• αh: 0.034 (according to Satellite Database[1])

<!-- b000085 | prose | pages [9] -->
• αl: 0.112

<!-- b000086 | prose | pages [9] -->
• γh: 0.027 (according to Satellite Database[1])

<!-- b000087 | prose | pages [9] -->
• γl: 0.086

<!-- b000088 | prose | pages [9] -->
• ρ: 0.1 (calculated from Spacecraft Encyclopedia[10])

<!-- b000089 | prose | pages [9] -->
• N1: 1 (in consideration of small and big collision)

<!-- b000090 | prose | pages [9] -->
• N1: 0.5

<!-- b000091 | prose | pages [9] -->
• λ: 0.05 (from Wikipedia)

<!-- b000092 | furniture | pages [10] -->
Team # 48573

<!-- b000093 | furniture | pages [10] -->
Page 9 of 28

<!-- b000094 | caption | pages [10] -->
Figure 3: The satellite and debris population with ODR

<!-- b000095 | heading | pages [10] -->
(4) Analysis and Conclusions

<!-- b000096 | prose | pages [10] -->
From the graph we can see the satellite population reaches its peak around 50th years in the future. Satellite population in low orbit grows faster in the next 40 years and gradually decreases with few satellites left in the orbit. Similarly, the satellite population in high orbit gradually drops to zero at a relatively small rate while the debris grows exponentially.

<!-- b000097 | prose | pages [10] -->
The result of our model is consistent with the Kessler syndrome [Kessler 1978], which means that the density of the objects around the earth will become so high in the future that the resulting debris cascade could make prospects for long-term viability of satellites in low earth orbit extremely low[Wikipedia]. The result also suggests that mitigating measures should be taken to restrict the in- crease of debris.

<!-- b000098 | heading | pages [10] -->
2.4 Model II

<!-- b000099 | prose | pages [10] -->
The model in the last section shows that when there is no removal measures, ”wandering” debris will continue to propagate through collisions, launches, ex- plosions and the expiration of active satellites. With each passing day the risk of damage to active satellites increases. Therefore, to make sure satellites can survive in the next few decades, mitigating measures are indispensable.

<!-- b000100 | furniture | pages [11] -->
Team # 48573

<!-- b000101 | furniture | pages [11] -->
Page 10 of 28

<!-- b000102 | prose | pages [11] -->
First we aim at analyzing the effects the cleaning system has on the earth’s orbit. We assume that the system is composed of several cleaning machines operating in the space to de-orbit or recycle the objects surrounding the earth. Additionally, we’re not going to focus on different types of ”cleaners” in this section. All the cleaners launched into space are treated as identical. In this way, we can introduce the variable W and θ to denote the cleaner population and its cleaning efﬁciency. Similarly to satellite, the cleaner also face the risk of collision with space debris, or undergo machinery damage in the process of working. Let δ denote the machinery damage rate.

<!-- b000103 | heading | pages [11] -->
(1)Additional assumptions

<!-- b000104 | prose | pages [11] -->
Without loss of generality, we have to make additional assumptions as fol- lows:

<!-- b000105 | prose | pages [11] -->
• The machines are not fully occupied so that the number of debris removed per unit time is positively correlated with the debris population in the s- pace.

<!-- b000106 | prose | pages [11] -->
• The more debris the machine has removed, the larger the possibility of machinery damage, which means that the damage frequency is relevant to the debris population.

<!-- b000107 | prose | pages [11] -->
• We neglect the debris produced by the cleaners themselves since the num- ber of cleaners is very small compared to the satellite population, and the collision with debris can be ascribed to machinery damage.

<!-- b000108 | prose | pages [11] -->
(2)Establishment & Test

<!-- b000109 | prose | pages [11] -->
By introducing ODR, the dynamics of satellite and debris population are un- doubtedly different from that in the last section. Based on Model I, the effect of launching cleaners can also be represented in differential equations. We need to notice that ODR has no direct impact on the satellite population. It affects the satellite population by removing the debris in the space, thus the differen- tial equations on the satellite part remain unchanged. The debris removed per unit time can be calculated as θWD, so on the debris part, equation (2.3) can be modiﬁed as

<!-- b000110 | prose | pages [11] -->
dD dt = (βhSh + βlSl)DN + (γh + γl)ρN + λD −θWD (2.4)

<!-- b000111 | prose | pages [11, 12] -->
Considering the machinery damage of the cleaners, the cleaner population can be depicted as dW dt = −δWD (2.5)

<!-- b000112 | furniture | pages [12] -->
Team # 48573

<!-- b000113 | furniture | pages [12] -->
Page 11 of 28

<!-- b000115 | prose | pages [12] -->
So the system of ordinary differential equations of introducing ODR is

<!-- b000116 | prose | pages [12] -->
 dSh dt = −βhDSh + αh −γh         dSl    dt = −βlDSl + αl −γl         dD    dt = (βhSh + βlSl)DN1 + (γh + γl)ρN2 + λD −θWD 

<!-- b000117 | prose | pages [12] -->
  dW    dt = −δWD          Sh(0) = Sh0, Sl(0) = Sl0         D(0) = D0 

<!-- b000118 | prose | pages [12] -->
A diagram can be drawn to illustrate the structure of the system.

<!-- b000119 | caption | pages [12] -->
Figure 4: The structure of the system

<!-- b000120 | prose | pages [12] -->
Based on the value of parameters, we can also simulate the satellite and de- bris population in the future and see the effect of ODR. The parameters related to cleaners are:

<!-- b000121 | prose | pages [12] -->
• θ : 4 (calculated from the research on laser base[11])

<!-- b000122 | prose | pages [12] -->
• W :0.02 (set according to research on laser base[11])

<!-- b000123 | prose | pages [12, 13] -->
• δ : 0.0011905 (calculated from the research on laser base[11]) Running the model by MATLAB, the development of this system is shown in the following ﬁgure.

<!-- b000124 | furniture | pages [13] -->
Team # 48573

<!-- b000125 | furniture | pages [13] -->
Page 12 of 28

<!-- b000127 | caption | pages [13] -->
Figure 5: The satellite and debris population without ODR

<!-- b000128 | heading | pages [13] -->
(3)Analysis and Conclusions

<!-- b000129 | prose | pages [13] -->
With the existence of ODR, we can see that the satellite population and debris population remain at the high level for more than 100 years. Compared to the ”do nothing” system, ODR has controlled the amount of debris to some extent and assured that more satellite can survive in the next few decades. From the ﬁgure we can also see that in the long run, the debris population still grows exponentially,. This may due to the fact that the cleaner will all eventually be damaged and the growth of debris is thereafter unrestricted.

<!-- b000130 | prose | pages [13] -->
The result of this model also shows that it is wise for us to launch cleaners continuously in order to keep the debris at a low level. Here we don’t take the speciﬁc number of cleaners into account; nevertheless, there exists the problem of how many cleaners should be launched, and we’ll show it in the later part.

<!-- b000131 | heading | pages [13] -->
3 Model Extension

<!-- b000132 | prose | pages [13] -->
3.1 What if launching different cleaners?

<!-- b000133 | prose | pages [13, 14] -->
(1)Analysis of the Problem In the last section we assume that all the debris is the same and there is only one type of cleaner that has the same cleaning efﬁciency. While in fact, ”no two snowﬂakes are the same”. The sizes of space debris are unlikely to be identical. We assume that there are two kinds of debris: large and small, denoted by D1 and D2, and each has the same probability to hit the satellite. However, because of the difference in size, the efforts needed to de-orbit them are not the same.

<!-- b000134 | furniture | pages [14] -->
Team # 48573

<!-- b000135 | furniture | pages [14] -->
Page 13 of 28

<!-- b000137 | prose | pages [14] -->
Let p1 and p2 denote the removal coefﬁcient ( i.e.efforts needed) for each type. Based on the second model, the number of debris removed per unit time is −pθWD. Note that in the last section we do not take this parameter into ac- count since we normalize average value p = 1. Thus we have 0 < p1 < 1 and p2 > 1.

<!-- b000138 | prose | pages [14] -->
Now we consider the specialization in cleaners. The heavy cleaners have the higher power and light cleaners have lower power. Our goal is to see whether this strategy is more effective in the removing system since both types are de- signed to have different functions. So the cleaning efﬁciency θ of these two types are different, θ1 > θ2 ( 1 for heavy and 2 for light). Again we assume the each size of debris has the same distribution in the space. Then with the same damage rate, the system of ordinary differential equations with specialization in cleaners is

<!-- b000139 | prose | pages [14] -->
dSh  dt = −βh(D1 + D2)Sh + αh −γh         dSl   dt = −βl(D1 + D2)Sl + αl −γl          dD1   = (βhSh + βlSl)(D1 + D2)N1 + (γh + γl)ρ1N2 + λD1 −(θ1W1 + θ2W2)p1D1   dt   dD2   = (βhSh + βlSl)(D1 + D2)N1 + (γh + γl)ρ2N2 + λD2 −(θ1W1 + θ2W2)p2D2   dt       dW1    = −δW1(Dl + D2)   dt       dW2   = −δW2(Dl + D2)   dt

<!-- b000140 | prose | pages [14] -->
Also, we can use a diagram to illustrate the structure.

<!-- b000141 | heading | pages [14] -->
(2)Test and Conclusions

<!-- b000142 | prose | pages [14, 15] -->
• W1: 0.005 • W2: 0.015

<!-- b000143 | furniture | pages [15] -->
Team # 48573

<!-- b000144 | furniture | pages [15] -->
Page 14 of 28

<!-- b000145 | caption | pages [15] -->
Figure 6: The structure of the system with different cleaners

<!-- b000147 | prose | pages [15] -->
• D1: 5000 ( consistent with the current distribution )

<!-- b000148 | prose | pages [15] -->
• D2: 15000

<!-- b000149 | prose | pages [15] -->
• p1: 0.7 ( larger debris are difﬁcult to remove )

<!-- b000150 | prose | pages [15] -->
• p2: 1.2

<!-- b000151 | prose | pages [15] -->
• θ1: 10 ( heavy cleaner has higher cleaning efﬁciency )

<!-- b000152 | prose | pages [15] -->
• θ2: 3

<!-- b000153 | prose | pages [15] -->
• ρ1: 0.25 ( consistent with the current distribution )

<!-- b000154 | prose | pages [15] -->
• ρ2: 0.75

<!-- b000155 | prose | pages [15] -->
The result is shown in the following ﬁgure.

<!-- b000156 | prose | pages [15] -->
We can see from the ﬁgure that the specialization in cleaner indeed has some- what positive effect on restricting the debris. The peak of the satellite population occurs in more than 100 years in the future, which is later than that in Model II, and the maximum is also larger. However, this result is not surprising since the specialization in cleaner may indeed increase the efﬁciency so that the overall debris population grows slower than that with identical cleaners.

<!-- b000157 | prose | pages [15] -->
Practically speaking, it is better for us to design machines for special use or aimed at different types of debris. A combination of different removing methods may also be the best choice in cleaning space debris.

<!-- b000158 | furniture | pages [16] -->
Team # 48573

<!-- b000159 | furniture | pages [16] -->
Page 15 of 28

<!-- b000160 | caption | pages [16] -->
Figure 7: The satellite and debris population with specialization

<!-- b000161 | prose | pages [16] -->
3.2 Is there a commercial opportunity?

<!-- b000162 | heading | pages [16] -->
3.2.1 The Proﬁt Motive

<!-- b000163 | prose | pages [16] -->
When it comes to whether a commercial opportunity exists in the world, proﬁt is undoubtedly the most important factor that a ﬁrm will care about. No agency of a space-faring nation will want to commit huge amounts of funding for the removal of space objects. Here for private companies, there is a question: How can anyone make money with space debris? Space trash has little value compared to the tens or hundreds of millions of dollars needed to retrieve it. However, practical proposals state that an insurance premium can be imposed to ﬁnance the debris removal measures. To ﬁnd the proﬁt of the company, we need to make several assumptions in this industry:

<!-- b000164 | prose | pages [16] -->
• All the countries invest in the removal system and they share the same protection, since the governments of space-faring nations would beneﬁt by allowing a private-sector company to remove debris.

<!-- b000165 | prose | pages [16] -->
• We believe that in the long run, the income from cleaning the debris must equal to the value the ﬁrm has produced, and the value is measured in the number of satellite the ﬁrm has protected.

<!-- b000166 | prose | pages [16] -->
• All the ﬁrms in this industry are identical. We can determine whether a commercial opportunity exists according to whether this industry is at- tractive enough.

<!-- b000167 | furniture | pages [17] -->
Team # 48573

<!-- b000168 | furniture | pages [17] -->
Page 16 of 28

<!-- b000169 | prose | pages [17] -->
Based on these assumptions, we can measure the proﬁt by subtracting the cost from its income. Note that the cost is composed of three parts: research and development, production, maintenance cost. So we can compare the cost and revenue of the total industry to see if this industry is proﬁtable now or in the future.

<!-- b000170 | heading | pages [17] -->
3.2.2 The Results

<!-- b000171 | prose | pages [17] -->
The proﬁt of ODR can be calculated as

<!-- b000172 | prose | pages [17] -->
π = (N2(t) −N1(t)) ∗V

<!-- b000173 | prose | pages [17] -->
where N2/N1 is the satellite population with/without ODR and V denotes the average value of a satellite. C(t) is the cost function related to time.

<!-- b000174 | prose | pages [17] -->
Here we set number the cleaners W at the same level with that in Model II. Additionally, about $100 - 200 million per year is required for maintenance [9]. We assume an additional cost of $20 billion is required during the research and $2 billion is required to produce and launch the cleaner. The replacement cost for the approximately 1071 active satellites in orbit today is estimated to be around $109 million [ESA/ESOC, 2013]. We thus set V = 0.101.

<!-- b000175 | prose | pages [17] -->
It’s not hard to ﬁnd that in the near future the research cost is so high that it’s impossible for the ﬁrms to make proﬁts. When t = 50, from the result of Model 1 and Model 2 , N1 = 1935, N2 = 2679, π(50) is calculated to be $75.14 billion. C(50) = $80 billion. C(50) > π(50). So in the 50th year, the company will only suffer a little deﬁcit.

<!-- b000176 | prose | pages [17] -->
When t = 60, the calculation shows that N1 = 1771, N2 = 2877. In the 60th years, π(60) is calculated to be $111.7 billion, C(60) = 84 billion. So C(60) < π(60) , the ﬁrms can make a proﬁt after 50 - 60 years.

<!-- b000177 | prose | pages [17] -->
Therefore, our calculation shows that the debris-cleaning industry will be proﬁtable in future. So there indeed exist opportunities for private ﬁrms several decades after. But in the near future, it may be very risky for ﬁrm to enter the industry because the costs are too high.

<!-- b000178 | prose | pages [17] -->
3.3 What if recycling the debris?

<!-- b000179 | prose | pages [17, 18] -->
We now consider the fact that not all the debris is useless. We use machine to recycle the debris and extract proportional value from the debris. Again we assume that debris is identical. Because of the effort to recycle the debris, the efﬁciency of the cleaner is obviously lower in terms of the number removed. Assume that in order to directly collect debris, the efﬁciency becomes half of its original value. Then the satellite and debris population are shown in the ﬁgure.

<!-- b000180 | furniture | pages [18] -->
Team # 48573

<!-- b000181 | furniture | pages [18] -->
Page 17 of 28

<!-- b000183 | caption | pages [18] -->
Figure 8: The satellite and debris population with recycling

<!-- b000184 | prose | pages [18] -->
Similarly, in the 60th year, the numbers of satellites No and Nr are 2,877 with ODR and 2,046 with recycle system. The debris population is 28.95 thousand without recycle and 168 thousand with recycle system. If we can ﬁnd one object useful among a thousand, the relative value of recycle in the next 60 years is calculated as (No −Nr) ∗V −0.001V (Do −Dr) < 0.

<!-- b000185 | prose | pages [18] -->
This means that the proﬁt made from recycle is less than just removing them from space. More speciﬁcally, the debris are so useless that it’s not wise for us to recycle them in the near future.

<!-- b000186 | heading | pages [18] -->
4 Sensitivity Analysis

<!-- b000187 | prose | pages [18] -->
(1) Collision rate: β

<!-- b000188 | prose | pages [18] -->
The collision rate between the debris and spacecraft is calculated according to the data available from the space agency. In the current situation, collision takes place nearly once per year, which is a comparatively small probability event. To make reasonable changes, we vary this data by a multiplication of 2 and 0.5 to test the inﬂuence of collision rate on the result.The ﬁrst ﬁgure shows the result when β is decreased to 0.5 times. The second shows the result when β doubles.

<!-- b000189 | prose | pages [18, 19] -->
We can see from the ﬁgures that when β is smaller, satellites reach a higher peak at a postponed time and a lower peak appears at an advanced time with bigger β. These observations are in accordance with our hypothesis. Further- more, the values of peaks do not change much with different β.

<!-- b000190 | furniture | pages [19] -->
Team # 48573

<!-- b000191 | furniture | pages [19] -->
Page 18 of 28

<!-- b000192 | caption | pages [19] -->
Figure 9: β is half of its original value

<!-- b000194 | caption | pages [19] -->
Figure 10: β doubles its original value

<!-- b000195 | prose | pages [19] -->
(2)Numbers of Fragments Produced : N

<!-- b000196 | prose | pages [19, 20] -->
The amount of debris produced in a collision is estimated according to the current data reported by detectors in space. This data is inevitably inaccurate since many pieces are lost because of the inability of tracing technique. We vary the amount of generated debris in one collision from the original 1000 to 1500, even 500,000 pieces. Results show that this factor exerts little inﬂuence on the ﬁnal predicted number of spacecrafts.

<!-- b000197 | furniture | pages [20] -->
Team # 48573

<!-- b000198 | furniture | pages [20] -->
Page 19 of 28

<!-- b000200 | prose | pages [20] -->
In Model 2, the change of collision rate and the amount of debris produced in one collision has no speciﬁc effect on the cleaner factor. Results show that these two elements exert the same inﬂuence on the predicted number of spacecraft as they do in model 1.

<!-- b000201 | heading | pages [20] -->
5 Evaluation Model

<!-- b000202 | heading | pages [20] -->
5.1 Metrics

<!-- b000203 | prose | pages [20] -->
Generally, a space debris cleaner can be evaluated from 5 aspects, including cost, cleaning efﬁciency, production cycle, disturbance and life expectancy.

<!-- b000204 | prose | pages [20] -->
(1)Cost

<!-- b000205 | prose | pages [20] -->
Undoubtedly, the total cost of a cleaner accounts for the majority percentage in the cleaner assessment. The cost consists of researching expense, produc- ing cost and launching price. The researching expense is directly related to the number of qualiﬁed published paper pi in a speciﬁc time period, since the more papers published, the larger amounts of money have been invested into the re- searching process. And in the aspect of producing, the total cost cpi approxi- mately equal to the cost of the main components. As to the launching expense, it is positively correlated to the weight z of the object.

<!-- b000206 | prose | pages [20] -->
Ci = pi + cpi + ε ∗zi

<!-- b000207 | prose | pages [20] -->
(2)Cleaning Efﬁciency

<!-- b000208 | prose | pages [20] -->
Cleaning efﬁciency refers to the number of debris it can deal with in a speciﬁc time period. Ei = n t

<!-- b000209 | prose | pages [20] -->
(3)Production Cycle

<!-- b000210 | prose | pages [20, 21] -->
We divide the production cycle into two parts. One is the time it takes to building the main part of the cleaner, another part is the time to build the left part. According to the critical path theory, the producing time of the main part contribute the majority proportion of the whole production cycle.

<!-- b000211 | furniture | pages [21] -->
Team # 48573

<!-- b000212 | furniture | pages [21] -->
Page 20 of 28

<!-- b000214 | prose | pages [21] -->
Ti = tmaini

<!-- b000215 | prose | pages [21] -->
(4)Disturbance

<!-- b000216 | prose | pages [21] -->
Different cleaners may cause various environment disturbance. There is a degree for different cleaners that disturb the normal functional spacecraft while coping with the space debris.

<!-- b000217 | prose | pages [21] -->
(5)Life Expectancy

<!-- b000218 | prose | pages [21] -->
Life expectancy deﬁnes the life span of the cleaner under normal condition.

<!-- b000219 | heading | pages [21] -->
5.2 Target Cleaner Selection

<!-- b000220 | prose | pages [21] -->
Here we collect data and determine the rank of four cleaners, they are space- based laser radiation, SpaDE (Space Debris Elimination) program from NASA, space-based water jets, tethered space tug. These four approaches are frequently discussed in papers or websites.

<!-- b000221 | prose | pages [21] -->
Laser radiation is aimed at ablating the objects and provides an impulse to the debris causing it to de-orbit. SpaDE is a method that will push satellites into a lower orbit by using air bursts within the atmosphere. Space-based water jets uses water to make the debris deviate from its orbit. The tethered system is also a promising technology to de-orbit the space debris. From these alternatives, we can build a model to choose the most preferable approach.

<!-- b000222 | heading | pages [21] -->
5.3 Analytic Hierarchy Process ( AHP )

<!-- b000223 | prose | pages [21] -->
While evaluating different aspects of those cleaners, all the criteria need to be considered and we must avoid subjective judgment. So we prefer to use AHP to make the decision.

<!-- b000224 | prose | pages [21] -->
(1)Obtain the Criteria Weight Vector

<!-- b000225 | prose | pages [21] -->
Determine the pairwise-comparison criteria judging matrix. In AHP, 1-9 method are used to represent the relatively importance between criteria. Con- structing the judging matrix A = (aij)n∗n, each element must satisfy following constraints:

<!-- b000226 | prose | pages [21, 22] -->
aij > 0 Goal Criteria Alternatives

<!-- b000227 | furniture | pages [22] -->
Team # 48573

<!-- b000228 | furniture | pages [22] -->
Page 21 of 28

<!-- b000230 | prose | pages [22] -->
Rank of the Cleaners Cost Laser Efﬁciency SpaDE Production Cycle Water Jet Disturbance Tethered Tug Life Expectancy

<!-- b000231 | caption | pages [22] -->
Table 1: Two-Layer Hierarchy Structure

<!-- b000232 | prose | pages [22] -->
aii = 1 aij = 1 aji

<!-- b000233 | prose | pages [22] -->
Calculate the eigenvalues and the corresponding eigenvectors. and Select the eigenvector u = (u1, u2, , un)T with the maximum eigenvalue λmax as the criteria weight vector and normalizing it as ui u′ i = Pn j=1 uj

<!-- b000234 | prose | pages [22] -->
(2)Applying consistency checking

<!-- b000235 | prose | pages [22] -->
• CI = λmax −n n −1

<!-- b000236 | prose | pages [22] -->
• Coincidence indicator table:

<!-- b000237 | prose | pages [22] -->
n 1 2 3 4 5 6 7 8 9

<!-- b000238 | prose | pages [22] -->
RI 0 0 0.58 0.90 1.12 1.24 1.32 1.41 1.45

<!-- b000239 | prose | pages [22] -->
We calculate the consistency ratio by CR = CI RI , if the calculating ratio is less than 0.1. Then we think the judging matrix is qualiﬁed and the eigenvector with the largest eigenvalue can be used as the weight vector; If not, the judging matrix need to be modiﬁed until the less-than condition is satisﬁed.

<!-- b000240 | prose | pages [22] -->
Determine the pairwise-comparison judging matrix between four cleaners in the respect of the ﬁve criteria. Repeating the above procedure and get ﬁve weight vectors which can be treated as relative grade vectors.

<!-- b000241 | heading | pages [22] -->
(3)Analysis and result

<!-- b000242 | prose | pages [22, 23] -->
Criteria Judging matrix   1 1 5 7 2 1 1 7 5 1   1/5 1/7 1 1/5 1/9 A = 1/7 1/5 5 1 1/3 1/2 1 9 3 1

<!-- b000243 | furniture | pages [23] -->
Team # 48573

<!-- b000244 | furniture | pages [23] -->
Page 22 of 28

<!-- b000246 | prose | pages [23] -->
The corresponding criteria weight vector is u = (0.3522, 0.2895, 0.0356, 0.0841, 0.2386). The grade vectors of four alternatives in the respect of ﬁve criteria is shown in the following ﬁgure.

<!-- b000247 | prose | pages [23] -->
The ﬁnal score of four alternatives are

<!-- b000248 | prose | pages [23] -->
Rank Method Score

<!-- b000249 | prose | pages [23] -->
1 SpaDE 0.3812 2 Water Jet 0.2778 3 Laser 0.2279 4 Tethered Tug 0.1131

<!-- b000250 | prose | pages [23] -->
The result of AHP shows that cost plays a signiﬁcant role in evaluating the candidate space debris cleaner followed by cleaning efﬁciency and SpaDE get the highest score in the evaluation process and have less variation with all crite- ria.

<!-- b000251 | heading | pages [23] -->
(4)Sensitivity Analysis

<!-- b000252 | furniture | pages [24] -->
Team # 48573

<!-- b000253 | furniture | pages [24] -->
Page 23 of 28

<!-- b000254 | prose | pages [24] -->
We analyze how the pairwise-comparison matrix will inﬂuence the ranking of candidate space debris cleaners. According to our model currentlyit is very hard for the de-debris service company to make a money. So when developing a space debris cleaner, the most signiﬁcant factor must be taken into consideration is the cost. Suppose in the future when de-debris business is far more proﬁtable, the cost of the cleaner plays a less signiﬁcant role in assessing one cleaner. So we modify the pairwise-comparison criteria matrix as:

<!-- b000255 | prose | pages [24] -->
  1 1/3 3 1/5 1/2 3 1 5 1/3 1   1/3 1/5 1 1/9 1/5 A = 5 3 9 1 3 2 1 5 1/3 1

<!-- b000256 | prose | pages [24] -->
And the corresponding weight vector is U = (0.0920, 0.2012, 0.0396, 0.4841, 0.1831)

<!-- b000257 | prose | pages [24] -->
The result becomes:

<!-- b000258 | prose | pages [24] -->
Rank Method Score

<!-- b000259 | prose | pages [24] -->
1 SpaDE 0.4834 2 Laser 0.2639 3 Tethered Tug 0.1280 4 Water Jet 0.1248

<!-- b000260 | prose | pages [24] -->
The result is quite different from the original one, so the selection of the cri- teria matrix has considerable inﬂuence on the ﬁnal result.

<!-- b000261 | heading | pages [24] -->
5.4 A proper approach to avoid collision

<!-- b000262 | heading | pages [24] -->
(1)Assumptions

<!-- b000263 | prose | pages [24] -->
• The collision avoidance strategy can only be applied on trackable debris and for the minor debris we make the assumption that they will not cause catastrophic damage and we can adopt special protecting-shield to limit the damage.

<!-- b000264 | prose | pages [24] -->
• Suppose the method we proposed can be achieved regardless of the tech- nical difﬁculties.

<!-- b000265 | prose | pages [24, 25] -->
(2)Model Due to the complicated environmental situation of the space, signiﬁcant un- certainties exist in the rotating orbit of trackable debris. Before we can build a collision avoidance system, position measurement of the space objects is needed. We need to obtain the rotating orbit information of both debris and functional spacecraft so that we can make the conjunction analysis. Here is our method, combining the Box method and the collision probability method:

<!-- b000266 | furniture | pages [25] -->
Team # 48573

<!-- b000267 | furniture | pages [25] -->
Page 24 of 28

<!-- b000269 | prose | pages [25] -->
Deﬁne a box area Vo of each functional spacecraft. The length, width and height for this box area are lo, wo, ho respectively. This box is deﬁned as ”outer box”. Based on the space object position measurement, predictions can be made about whether any debris will pass through this box. If debris exists, the control center will activate the level-one plan, keeping on surveilling the debris and offering detailed information.

<!-- b000270 | prose | pages [25] -->
Then calculate the position of both target spacecraft and debris based on the tracking data. Here r is the orbit vector of this spacecraft or debris while e is the error vector of the position of spacecraft or debris caused by environmental disturbance.

<!-- b000271 | prose | pages [25] -->
• The position vector of spacecraft: Rs = rs + es.

<!-- b000272 | prose | pages [25] -->
• The position vector of debris: Rd = rd + ed.

<!-- b000273 | prose | pages [25] -->
• Calculating the predicted minimum distance between spacecraft and de- bris.

<!-- b000274 | prose | pages [25] -->
md = |Rs −Rd|

<!-- b000275 | caption | pages [25] -->
Figure 11: approach to avoid collision

<!-- b000276 | prose | pages [25] -->
If the minimum distance md is within the threshold , level-two plan will be activated. So it then adjusts the velocity of the spacecraft to change its orbit to avoid collision.

<!-- b000277 | furniture | pages [26] -->
Team # 48573

<!-- b000278 | furniture | pages [26] -->
Page 25 of 28

<!-- b000279 | prose | pages [26] -->
• Deﬁne another box area called inner box whose size is li, wi, hi respectively.

<!-- b000280 | prose | pages [26] -->
• If the predicted data indicates that the debris will across the inner box, then the level-three plan, which is speciﬁed for the serious situation, will be activated. Much more emergent measurements will be adopted.

<!-- b000281 | prose | pages [26] -->
• Based on the value of the spacecraft, we can classify the spacecraft into three categories: low value, commercial, high value. For different type of spacecraft, different box size and threshold is deﬁned.

<!-- b000282 | heading | pages [26] -->
6 Strengths and Weaknesses

<!-- b000283 | heading | pages [26] -->
6.1 Strengths

<!-- b000284 | prose | pages [26] -->
• We apply scientiﬁc methods in approximating our model parameters. Such as the impact into spacecraft structure formula

<!-- b000285 | prose | pages [26] -->
• Our model of the space debris removal process takes various factors into account.

<!-- b000286 | prose | pages [26] -->
• Our debris removal models are insensitive to parameter changes.

<!-- b000287 | prose | pages [26] -->
• We made extensions to our proﬁt model that takes the additional debris recycling beneﬁts into account.

<!-- b000288 | prose | pages [26] -->
• We evaluate the ODR system in basically two scales: the pure proﬁts aspect and the overall performance aspect

<!-- b000289 | prose | pages [26] -->
• We come up with a new method to perform collision avoidance which takes advantage of existing alternatives, reducing costs and enhancing per- formance.

<!-- b000290 | heading | pages [26] -->
6.2 Weaknesses

<!-- b000291 | prose | pages [26] -->
• The exponential model simulating debris growth may be unrealistic.

<!-- b000292 | prose | pages [26] -->
• The categorization of the earth orbits is rough, with only LEO and GEO separated.

<!-- b000293 | prose | pages [26] -->
• The value setting in pairwise-comparison criteria matrix of AHP is a little sensitive to parameters value.

<!-- b000294 | furniture | pages [27] -->
Team # 48573

<!-- b000295 | furniture | pages [27] -->
Page 26 of 28

<!-- b000296 | heading | pages [27] -->
7 Conclusions

<!-- b000297 | prose | pages [27] -->
According to our model, if no action is taken, the turning point of the debris increasing and number of collision will come in few decades. On the contrary, if human being start to send space debris cleaner from now, the appearance of the turning point will be postponed signiﬁcantly. Although the situation is emer- gent, the collision rate of spacecraft and debris is still at a low level currently. So, it is hard for one private company to make a money through ODR business in the short term. Moreover, our model predict it will not be proﬁtable until at least 50 years later.

<!-- b000298 | prose | pages [27] -->
Our cleaner assessment model is based on Analytic Hierarchy Process, the pairwise-comparison criteria matrix deﬁned including 5 criteria: cost, cleaning efﬁciency, production cycle, disturbance and life expectancy. In the paper we discuss four speciﬁc type including: space-based laser, SpaDE, water jet, teth- ered space tug. And it turns out SpaDE,conducted by NASA, is the best alterna- tive.

<!-- b000299 | prose | pages [27] -->
As mentioned above that ODR business will not make proﬁts in recent years, so collision avoidance method is preferred currently.We combine the strength of two separate collision method and build a new collision avoidance system. This method calculating the probability of collision in two ways based on the data of the trackable space object.

<!-- b000300 | heading | pages [27] -->
References

<!-- b000301 | references | pages [27] -->
[1] http://satellitedebris.net/Database

<!-- b000302 | references | pages [27] -->
[2] http://www.universetoday.com/42198/how-many-satellites-in-space/

<!-- b000303 | references | pages [27] -->
[3] Orbital Debris Frequently Asked Questions, Nasa Orbital Debris Program

<!-- b000304 | references | pages [27] -->
Ofﬁce, 2012

<!-- b000305 | references | pages [27] -->
[4] D. Kessler and B. Cour-Palais, ”Collision frequency of artiﬁcial satellites:

<!-- b000306 | references | pages [27] -->
The creation of a debris belt”, J. Geophys. Res., vol. 83, no. 6, p. 2637, 1978.

<!-- b000307 | references | pages [27] -->
[5] D. Kessler, N. Johnson, J. Liou and M. Matney, ”The Kessler Syndrome:

<!-- b000308 | references | pages [27] -->
Implications to Future Space operations”,33rd Annual AAS Guidance and

<!-- b000309 | references | pages [27] -->
Control Conference, 2010.

<!-- b000310 | references | pages [27] -->
[6] J. Pelton, New Solutions for the Space Debris Problem.Springer Internation-

<!-- b000311 | references | pages [27] -->
al Publishing, 2015.

<!-- b000312 | furniture | pages [28] -->
Team # 48573

<!-- b000313 | furniture | pages [28] -->
Page 27 of 28

<!-- b000314 | references | pages [28] -->
[7] Nasa Orbital Debris Program Ofﬁce, 2012

<!-- b000315 | references | pages [28] -->
[8] D. Gregory, J. Mergen and A. Ridley, ”Space Debris Elimination (SpaDE)

<!-- b000316 | references | pages [28] -->
Phase I Final Report”, NASA NIAC – 11- 11NIAC-0241, 2012.

<!-- b000317 | references | pages [28] -->
[9] S. Oliver and A. Pugliese, ”Active Debris Removal: A Business Opportuni-

<!-- b000318 | references | pages [28] -->
ty?”, Toulouse Business School, 2015.

<!-- b000319 | references | pages [28] -->
[10] Spacecraft

<!-- b000320 | references | pages [28] -->
Encyclopedia

<!-- b000321 | references | pages [28] -->
http://claudelaﬂeur.qc.ca/Spacecrafts-

<!-- b000322 | references | pages [28] -->
index.html

<!-- b000323 | references | pages [28] -->
[11] Laser Radiation for Cleaning Space Debrisfrom Lower Earth Orbits,W olf-

<!-- b000324 | references | pages [28] -->
gang O. Schall

<!-- b000325 | furniture | pages [29] -->
Team # 48573 Page 28 of 28

<!-- b000326 | heading | pages [29] -->
Executive Summary

<!-- b000327 | prose | pages [29] -->
Space debris is becoming increasingly alarming as nations worldwide are sending more satellites into space. Issues concerning this problem deserve more attention and proper measures need to be taken. Currently there are two kinds of approaches that can be adopted: ”doing nothing” or concentrate on the problem now. The ﬁrst approach will not cause obvious harm at present but future generations are at a risk of losing the space resources. The second approach is more advisable but a considerable cost is needed.

<!-- b000328 | prose | pages [29] -->
In order to know what we should do in this complex situation, we ﬁrst construct several models to study the effect of space junk on several basic assumptions. From the analysis of the results, we ﬁnd that the space will only contain space junk in the next few decade. We also ﬁnd that with the ODR(Orbital Debris Removal) system,it will take about 50- 60 years for the numbers of satellites to decrease. Additionally, launching specialized cleaners may be a better idea.

<!-- b000329 | prose | pages [29] -->
Our calculations also show that it is hard for a private company to make proﬁt in the near future, but there truly exist opportunities to make money several decades after. According to our model, the debris threat now is at a low level and the increasing rate of debris is at a low level. But the turning point will occur after about 50 years when debris start to grow exponentially and collision between spacecraft and debris become increasingly frequent. At that time, ODR may begins to make money through ﬁnance from government or companies that own satellites.

<!-- b000330 | prose | pages [29] -->
We construct another model to evaluate different types space debris cleaner. This model takes ﬁve properties of the cleaner into consideration including: cost, cleaning efﬁciency, production cycle, disturbance and life expectancy. Each of these criteria is assigned with different weights. We treat Cost as the most important factor, followed by cleaning efﬁciency, life expectancy, disturbance, production cycle. And the result is shown is the following table:

<!-- b000331 | source_object | pages [29] -->
Rank Approach 1 SpaDE 2 Water Jet 3 Laser 4 Tethered Tug

<!-- b000332 | prose | pages [29] -->
We think SpaDe is the best approach considering the overall performance. The is determined based on the fact that cost is the main obstacle in removing space debris now. Removing space debris can make proﬁts in future and contribute positively to the outer space environment. Therefore we strongly rec

<!-- b000333 | furniture | pages [30] -->
Team # 48573 Page 29 of 28

<!-- b000334 | prose | pages [30] -->
ommend the government ﬁnance the researches in this ﬁeld to achieve more beneﬁts both environmentally and economically.
