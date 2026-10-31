# P-B-2012-15878-825774ea

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
C.A.R.S.: Cellular Automaton Rafting Simulation

<!-- b000002 | title | pages [1] -->
Subtitle

<!-- b000003 | title | pages [1] -->
Control #15878

<!-- b000004 | heading | pages [1] -->
13 February 2012

<!-- b000005 | heading | pages [1] -->
Abstract

<!-- b000006 | prose | pages [1] -->
The Big Long River management company oﬀers white water rafting tours along its 225 mile long river with Y uniformly distributed camp sites. We were tasked to optimize the rafting schedule for this company and to formulate a method for determining the river’s carrying capacity. We repre- sent the river as a one-dimensional array populated by objects representing rafting parties of various trip length and propulsion methods. Thus the model we propose can be treated as a cellular automaton-like structure pro- vided there exists rules that govern how each cell behaves for each iteration. Rules for assigning raft destinations are iterated daily, allowing our model to dynamically respond to operating conditions such as new rafting trips, inclement weather, and load-dependent degradation of camp sites, while si- multaneously maintaining critical levels of a variety of visitor satisfaction criteria. Using this dynamic model, camp site conﬂicts were eliminated, the carrying capacity of the river was determined to be 1102 visitors per season, with more than 99% of visitors completing trips on-time and rejecting less than 2% of trips.

<!-- b000007 | prose | pages [1] -->
1

<!-- b000008 | contents | pages [2] -->
Control # 15878

<!-- b000009 | furniture | pages [2] -->
Page 2 of 23

<!-- b000010 | heading | pages [2] -->
Contents

<!-- b000011 | contents | pages [2] -->
1 Introduction

<!-- b000012 | contents | pages [2] -->
3

<!-- b000013 | contents | pages [2] -->
2 Plan of Attack

<!-- b000014 | contents | pages [2] -->
3

<!-- b000015 | contents | pages [2] -->
3 Our Assumptions

<!-- b000016 | contents | pages [2] -->
4

<!-- b000017 | contents | pages [2] -->
4 Important Deﬁnitions

<!-- b000018 | contents | pages [2] -->
5

<!-- b000019 | contents | pages [2] -->
4.1

<!-- b000020 | contents | pages [2] -->
Visitor Satisfaction . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000021 | contents | pages [2] -->
5

<!-- b000022 | contents | pages [2] -->
4.2 Carrying Capacity

<!-- b000023 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
6

<!-- b000025 | contents | pages [2] -->
5 Deﬁning a Good Model

<!-- b000026 | contents | pages [2] -->
6

<!-- b000027 | contents | pages [2] -->
6 Scheduling: Static vs Dynamic Approaches

<!-- b000028 | contents | pages [2] -->
7

<!-- b000029 | contents | pages [2] -->
6.1

<!-- b000030 | contents | pages [2] -->
The Static Strategy . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
7

<!-- b000032 | contents | pages [2] -->
6.2

<!-- b000033 | contents | pages [2] -->
The Dynamic Strategy . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
7

<!-- b000035 | contents | pages [2] -->
7 The Model: A Cellular Automaton-like Strategy

<!-- b000036 | contents | pages [2] -->
9

<!-- b000037 | contents | pages [2] -->
7.1

<!-- b000038 | contents | pages [2] -->
The Visitor Object . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
10

<!-- b000040 | contents | pages [2] -->
7.2 Governing Rules for the Model

<!-- b000041 | contents | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
10

<!-- b000043 | contents | pages [2] -->
7.3

<!-- b000044 | contents | pages [2] -->
An Ideal Implementation of the Model . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
11

<!-- b000046 | contents | pages [2] -->
7.4

<!-- b000047 | contents | pages [2] -->
Control Implementations . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
12

<!-- b000049 | contents | pages [2] -->
8 Clarifying the Metrics

<!-- b000050 | contents | pages [2] -->
12

<!-- b000051 | contents | pages [2] -->
9 Results

<!-- b000052 | contents | pages [2] -->
14

<!-- b000053 | contents | pages [2] -->
9.1

<!-- b000054 | contents | pages [2] -->
Number of Interactions . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
15

<!-- b000056 | contents | pages [2] -->
9.2

<!-- b000057 | contents | pages [2] -->
Number of Visitor Rejections . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
16

<!-- b000059 | contents | pages [2] -->
9.3

<!-- b000060 | contents | pages [2] -->
Oﬀ-Schedule Completions . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
17

<!-- b000062 | contents | pages [2] -->
9.4 Carrying Capacity

<!-- b000063 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
17

<!-- b000065 | contents | pages [2] -->
10 Further Investigations

<!-- b000066 | contents | pages [2] -->
19

<!-- b000067 | contents | pages [2] -->
10.1 Environmental Degradation . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
19

<!-- b000069 | contents | pages [2] -->
10.2 Mitigating Storms

<!-- b000070 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
20

<!-- b000072 | contents | pages [2] -->
11 Conclusion

<!-- b000073 | contents | pages [2] -->
20

<!-- b000074 | contents | pages [2] -->
12 Memo to Rafting Management

<!-- b000075 | contents | pages [2] -->
22

<!-- b000076 | contents | pages [2] -->
C.A.R.S

<!-- b000077 | contents | pages [2] -->
Cellular Automaton Rafting Simulation

<!-- b000078 | contents | pages [3] -->
Control # 15878

<!-- b000079 | furniture | pages [3] -->
Page 3 of 23

<!-- b000080 | heading | pages [3] -->
1 Introduction

<!-- b000081 | prose | pages [3] -->
White water rafting has become one of the fasting growing outdoor leisure activities in the United States1, with participation in rafting activities increasing 151% from 1987 levels.2 Multi-day trips of diﬀerent length, with opportunities for both rafting and traditional camping, have captured the interest of a public seeking a wilderness experience. As a result, park managers have sought to discover methods to accommodate more boating trips in a rafting season without loss of visitor satisfaction.

<!-- b000082 | prose | pages [3] -->
Previous models have emphasized social norm theory as an analytic tool for understand- ing the enjoyability of a camping/rafting trip.3 Stankey argued that the enjoyment of a wilderness experience is inversely related to the number of interactions that occur with members of other parties during the trip, thus setting a social carrying capacity to the system.4 Combining this Wilderness Simulation Model with trip logs, several researchers have constructed programs to generate optimal seasonal rafting schedules for various river systems.5

<!-- b000083 | prose | pages [3] -->
However, in order to reduce interactions between campers, a number of these models have generated seasonal schedules with trips of only one or two durations oﬀered at any given time. These models often fail to take into account customer demand, and reduce the number of options in trip varieties to be oﬀered to campers. To compensate, some rafting companies have set up multiple trips over diﬀerent rivers; however, this is clearly not practical for all rafting companies, and only partially mitigates the problem. Thus, we aim to develop a dynamic model to provide customers with a high quality rafting/camping trip of desired length.

<!-- b000084 | heading | pages [3] -->
2 Plan of Attack

<!-- b000085 | prose | pages [3] -->
We will develop our model based on The Big Long River, a 225 mile long white water river system with Y camp sites distributed evenly along its banks. Rafting trips on this river are characterized by both their duration (ranging from 6 - 18 days) and by the raft type used (oar-propelled or motor). Our goal is to propose a method to allow as many visitors to raft through the river during the six month rafting season while maintaining an enjoyable experience for the visitors. We also wish to be able to provide a variety of diﬀerent trip options to the customers. The breadth of these requirements demands that we break down each component of the problem and analyze it separately; we will thus seek to restate the problem mathematically and clarify our goals. We will proceed by:

<!-- b000086 | prose | pages [3] -->
• Stating Assumptions. By stating our assumptions, we will narrow the focus of our approach towards the problem and provide some insight into the nature of the white water river rafting system.

<!-- b000087 | prose | pages [3] -->
• Deﬁning Evaluation Criteria. To make clear what the aims of our model should be, we must state what factors are involved in determining the success of the model.

<!-- b000088 | prose | pages [3] -->
• Describing a Good Model. A powerful model should be practical in terms of ease of application and ability to cope with extreme circumstances. By highlighting the characteristics of a good model, we will be able to direct our eﬀorts in the correct direction.

<!-- b000089 | prose | pages [3] -->
Once we have stated all of our goals, assumptions, and criteria, we will delve into our strategy to model the white water rafting system. We will:

<!-- b000090 | prose | pages [3] -->
• Present Our Model. We develop and test a dynamic model to simulate the river as a one dimensional cellular automaton-like structure with cells representing camp sites. Each cell will be occupied by visitors with unique properties.

<!-- b000091 | prose | pages [3, 4] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000093 | furniture | pages [4] -->
Page 4 of 23

<!-- b000094 | prose | pages [4] -->
• Develop Several Implementations. We will construct and compare several rules to govern loading visitors and movement of visitors along our cellular automaton- like structure.

<!-- b000095 | prose | pages [4] -->
• Evaluate the Model. We will postulate and test the behavior of our model under various limiting circumstances. We will then evaluate the strengths and weaknesses of our model and our model’s applicability to diﬀerent situations.

<!-- b000096 | heading | pages [4] -->
3 Our Assumptions

<!-- b000097 | prose | pages [4] -->
To fully understand the whitewater river rafting system and to develop a model to simu- late this system, we must ﬁrst make some assumptions. Since these assumptions will be essential in assisting us to construct our system, we will seek to formulate assumptions that are logical and reasonable.

<!-- b000098 | prose | pages [4] -->
• There are ﬁxed ranges for both the duration of time visitors spend raft- ing as well as for the velocity of the rafts. We have estimated these ranges based on literature information such as the average velocity of white water rapids and sample rafting itineraries.6 7 These values are listed in the table below.

<!-- b000099 | prose | pages [4] -->
Oar-Propelled Raft Motor Raft Minimum Velocity 3 mph 3 mph Maximum Velocity 5 mph 10 mph Duration of Rafting 4 - 8 hours 4 - 8 hours

<!-- b000100 | caption | pages [4] -->
Table 1: Constant values used in our model based on industry standards.

<!-- b000101 | prose | pages [4] -->
• While rafting, visitors do not dramatically change their velocity over the course of the day. We assume that visitors will not extensively dawdle or backtrack along the river. A large majority of camp sites send experienced tour guides out with visitors to ensure that the boat keeps moving at the necessary speed. As a result, motion of visitors along the river is a state function - it only depends the initial and ﬁnal positions of the visitors along the river.

<!-- b000102 | prose | pages [4] -->
• Camp sites are equivalent and uniformly distributed alongside the river.

<!-- b000103 | prose | pages [4] -->
Thus, to evaluate the distance between camp sites, we simply need to consider the length of the river (225 miles) divided by Y , the number of camp sites.

<!-- b000104 | prose | pages [4] -->
• Camp sites are located a signiﬁcant distance away from the river bank.

<!-- b000105 | prose | pages [4] -->
Due to safety, construction, and privacy issues, it is very unlikely that the sites are built immediately on the banks of the river.

<!-- b000106 | prose | pages [4] -->
• Visitors will travel and explore within a small distance of the camp site once oﬀthe raft. While hiking is a very common outdoor leisure activity, part of the constraints of the Big Long River is that the river is inaccessible to hikers.

<!-- b000107 | prose | pages [4] -->
For this reason, we assume that no visitor will travel signiﬁcantly far from the camp site - a reasonable assumption, if we consider that a large portion of campers seek rest and relaxation. 8

<!-- b000108 | prose | pages [4] -->
• The camp sites are properly maintained on a routine basis by the river management. We assume that at all of the camp sites will remain functionally operative throughout the season. We also assume that the river management will frequently service camp sites to clean garbage and to ensure availability of and access to clean water and bathroom facilities.

<!-- b000109 | prose | pages [4] -->
• The mean number of visitors that are loaded onto the river on any day remains constant. Most rafting companies oﬀer a set number of trips on a daily basis, and thus this assumption is in accordance with standard industry practices.

<!-- b000110 | prose | pages [4, 5] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000112 | furniture | pages [5] -->
Page 5 of 23

<!-- b000113 | prose | pages [5] -->
• Visitors will schedule their rafting trips at least 24 hours in advance of their desired launch date. Given industry standards, this assumption is reasonable, as most white water rafting companies require advanced booking of trips.

<!-- b000114 | prose | pages [5] -->
Our assumptions allow us to simplify the complexities of real life white water rafting systems, as well as provide us with a better understanding of our problem. We will frequently reference these assumptions to help us develop our dynamic model.

<!-- b000115 | heading | pages [5] -->
4 Important Deﬁnitions

<!-- b000116 | prose | pages [5] -->
To evaluate our model, it will be necessary for us to deﬁne some of the primary criteria of our model:

<!-- b000117 | heading | pages [5] -->
1. Visitor Satisfaction - How do visitors perceive their wilderness experience?

<!-- b000118 | heading | pages [5] -->
2. Carrying Capacity - How many visitors can participate in white water raft-

<!-- b000119 | prose | pages [5] -->
ing/camping in a rafting season compared to the absolute capacity of the river system?

<!-- b000120 | prose | pages [5] -->
While these criteria, particularly visitor satisfaction, are somewhat subjective, we will seek to use both the literature as well as assumptions derived from common sense to justify our deﬁnitions.

<!-- b000121 | heading | pages [5] -->
4.1 Visitor Satisfaction

<!-- b000122 | prose | pages [5] -->
A signiﬁcant portion of research on leisure activities in camping and rafting systems has revolved around the role of social norms. Based on these studies, we propose the criterion of visitor satisfaction, and break this criterion down into several components:

<!-- b000123 | prose | pages [5] -->
• Visitor satisfaction is inversely correlated to the number of interactions a visitor has with other groups of people.9 For many, wilderness excursions are meant to be privately shared and enjoyed;

<!-- b000124 | prose | pages [5] -->
it is no surprise that the literature on public perception towards camping trips frequently revolves around overcrowding. Since visitors in our model will either spend their time rafting or camping, there are three modes of interaction4 that we will consider:

<!-- b000125 | prose | pages [5] -->
– Raft to Raft Interactions, which occur when one raft passes another on the river

<!-- b000126 | prose | pages [5] -->
– Raft to Camp Interactions, which occur when one raft passes a group at a camp site

<!-- b000127 | prose | pages [5] -->
– Camp to Camp Interactions, which occur when individuals walking around their camp sites encounter one another

<!-- b000128 | prose | pages [5] -->
• Visitor satisfaction decreases if a trip is completed oﬀ-schedule.

<!-- b000129 | prose | pages [5] -->
The amount that visitors pay for a trip is generally proportion to the duration of the trip; thus, if a trip is completed early, then the visitors may feel cheated out of their money. On the ﬂip side, most of the visitors only have a limited amount of leisure time, and if a trip is completed late, the visitors may be irate due to lost time.

<!-- b000130 | prose | pages [5] -->
• Visitor satisfaction decreases if visitors are unable to participate in de- sired trips.

<!-- b000131 | prose | pages [5] -->
Visitors all have diﬀerent personal schedules and commitments, and may desire a rafting trip that is uniquely customized to their needs. Thus, general satisfaction with a white water rafting company may decrease if the company is unable to accommodate customer demands.

<!-- b000132 | prose | pages [5, 6] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000134 | furniture | pages [6] -->
Page 6 of 23

<!-- b000135 | prose | pages [6] -->
Having broken down visitor satisfaction into these various components, we will seek to maintain satisfaction at a high level throughout the development and testing of our model. As these evaluation criteria for visitor satisfaction have been developed in the literature, our model can now be compared to established standards for white water rafting and camping.

<!-- b000136 | heading | pages [6] -->
4.2 Carrying Capacity

<!-- b000137 | prose | pages [6] -->
We ﬁrst consider the concept of absolute capacity, or the maximum number of visitors that can be accommodated in our white water river system. It is apparent that in our rafting system, the absolute capacity is:

<!-- b000138 | prose | pages [6] -->
6 (months/season) × 30 (days/month) × Y = 180Y (visitor groups per season)

<!-- b000139 | prose | pages [6] -->
However, we must be cautious with interpreting absolute capacity - to state that a white water system can allow 180Y visitor groups to be accommodated per season is akin to stating that the number of people that can ﬁt in a house is equal to the number of people that can be squashed into every inch of the house.

<!-- b000140 | prose | pages [6] -->
We thus deﬁne a criteria that could be used to better model white water river rafting systems:

<!-- b000141 | prose | pages [6] -->
• The carrying capacity of a model is the number of visitors that a model allows to participate in rafting/camping activities in any particular season while maintaining high standards of visitor satisfaction.

<!-- b000142 | heading | pages [6] -->
5 Deﬁning a Good Model

<!-- b000143 | prose | pages [6] -->
Having developed a better understanding of the problem in terms of assumptions and criteria, we seek to describe the characteristics of a good model. These qualities will guide us towards constructing our model.

<!-- b000144 | prose | pages [6] -->
• The model should maximize the carrying eﬃciency of the white water river rafting system while maintaining high levels of customer satisfac- tion. While the model’s goal is to allow greater numbers of visitor groups to participate in white water rafting than current industrial models allow, a good model will also minimize visitor interactions and oﬀ-schedule trip completions.

<!-- b000145 | prose | pages [6] -->
• The model should satisfy customer demands in terms of oﬀered trips.

<!-- b000146 | prose | pages [6] -->
A good model can allow customers to participate in trips suited to their personal needs and interests. The model should seek to minimize the number of individuals whose trip demands cannot be satisﬁed.

<!-- b000147 | prose | pages [6] -->
• The model should perform eﬀectively under a wide range of variable operating conditions. The model should provide satisfactory results for a range of values of Y and the number of people who are loaded into the river each day.

<!-- b000148 | prose | pages [6] -->
The model should also present a contingency plan for conditions that impede the ﬂow of visitors down the river, such as weather.

<!-- b000149 | prose | pages [6] -->
• The model must be easy to implement. A good model should be easy to operate, provide interpretable results, and can be utilized on a day-to-day basis in real-life situations.

<!-- b000150 | heading | pages [6] -->
6 Scheduling: Static vs Dynamic Approaches

<!-- b000151 | prose | pages [6] -->
We have up until now not considered the concept of “scheduling” visitors to the white water river park. Our goal of getting visitors through the river breaks down into providing each visitor group an itinerary of what camp site the group must

<!-- b000152 | prose | pages [6, 7] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000154 | furniture | pages [7] -->
Page 7 of 23

<!-- b000155 | prose | pages [7] -->
reach by the end of each day. There are some key concerns that must be addressed in scheduling:

<!-- b000156 | prose | pages [7] -->
• To ensure that every group is assigned a camp site for every day of their trip

<!-- b000157 | prose | pages [7] -->
• To reduce conﬂicts - that is, to ensure that no two groups are assigned to the same camp site on any given day

<!-- b000158 | prose | pages [7] -->
• To eﬀectively load new visitor onto the river

<!-- b000159 | prose | pages [7] -->
• To ensure that visitors complete their trip on schedule

<!-- b000160 | prose | pages [7] -->
To proceed, we must evaluate two diﬀerent strategies to schedule visitors to camp sites - the static approach and the dynamic approach.

<!-- b000161 | heading | pages [7] -->
6.1 The Static Strategy

<!-- b000162 | prose | pages [7] -->
Static approaches are the most widespread of scheduling strategies, and are extensively used by white water rafting companies across the nation. In the static approach, the rafting company selects a small number of trips to oﬀer to the public. These trips are selected and constructed such that conﬂicts in camp site scheduling can never occur. Furthermore, unless extenuating circumstances like storms occur, visitors will always complete their journey exactly on time. Visitors can pay to participate in one of these speciﬁc trips. Trips are seasonally oﬀered and rotated on a regular basis. While static models prevent the concern for conﬂicts in scheduling, they present several shortcomings for white water rafting systems.

<!-- b000163 | prose | pages [7] -->
• Static approaches fail to take into account customer demand. To prevent conﬂicts in scheduling, the static approach necessarily reduces the number of trips oﬀered. By rotating trips seasonally, the static approach also reduces the amount of time that any one trip is oﬀered. One can thus imagine a white water river rafting company losing customers due to lack of ﬂexibility in trips oﬀered.

<!-- b000164 | prose | pages [7] -->
• Static approaches reduce the number of visitors who can participate in rafting activities during the rafting season. Since the success of the static approach is built on preventing scheduling conﬂicts, a necessarily smaller number of visitors are allowed to take rafting trips at any time. While the static strategy provides optimal scheduling for any one type of rafting trip, it can only present optimal scheduling for multiple trips if fewer people participate in those trips.

<!-- b000165 | heading | pages [7] -->
6.2 The Dynamic Strategy

<!-- b000166 | prose | pages [7] -->
Unlike the static system, the dynamic system emphasizes maximizing the num- ber of trip options oﬀered to visitors. Such a system allows visitors to entirely cus- tomize their trip to suit their needs. The dynamic system requires a more complex conﬂict resolution strategy than the static approach, but ensures that customers can select any trip they desire at any point in the rafting system. The dynamic approach works in the following manner:

<!-- b000167 | heading | pages [7] -->
1. As per our assumption, the river management will always know the

<!-- b000168 | prose | pages [7] -->
desired trips of visitors the day before the visitors are to be loaded.

<!-- b000169 | prose | pages [7] -->
2. On the ﬁrst day of the trip, the visitor is assigned his/her ﬁrst destina- tion camp site. This assignment is based on the current occupancy of the camp sites on the river, as well as the desired duration of the trip and the raft type.

<!-- b000170 | heading | pages [7] -->
3. During this ﬁrst day, the rafting company receives information for all of

<!-- b000171 | prose | pages [7] -->
the rafters to be launched the next day.

<!-- b000172 | prose | pages [7] -->
4. At the end of the ﬁrst day, the visitor is given his second destination camp site. This assignment is made in the same manner as the ﬁrst, except that the model will also consider the other rafters who are to be loaded on to the river the next day.

<!-- b000173 | prose | pages [7, 8] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000175 | furniture | pages [8] -->
Page 8 of 23

<!-- b000176 | heading | pages [8] -->
5. Every day, the visitor receives the next destination site until the journey

<!-- b000177 | prose | pages [8] -->
is completed.

<!-- b000178 | prose | pages [8] -->
The dynamic method thus necessarily maximizes the number of trip options that visitors are given for any river system. The dynamic approach recalculates the route of each visitor at the end of each day to keep the visitor moving towards the anticipated complete date of the trip, but also considers how occupied the camp sites along the river are. The dynamic model does have some potential weakness, however, which we will consider here:

<!-- b000179 | prose | pages [8] -->
• The possibilities of conﬂict and of oﬀ-schedule arrivals is not necessarily zero in the dynamic model. However, with careful scheduling, the chance of either of these issues are occurring can be made negligible.

<!-- b000180 | prose | pages [8] -->
• The dynamic model may seem unsavory to river managers as it seemingly operates one day at a time. In an abstract sense, this is true; the dynamic model thus requires that the camp management has some way of remaining in contact with visitors throughout their trip. In a real-world scenario, however, rafting companies will be able to plan far in advance of one day. There are two immediate consequences to this assumption:

<!-- b000181 | prose | pages [8] -->
– With enough advanced planning, a dynamic model can provide itineraries for visitors that are just as “set-in-stone” as those gen- erated by static models.

<!-- b000182 | prose | pages [8] -->
– Dynamic models can allow river managers and rafting companies to predict whether a visitor’s desired trip plan can be accommo- dated given the current river occupancy. If a visitor’s trip results in scheduling conﬂicts, the rafting company can inform the visitor to resched- ule at a diﬀerent time. Though these “rejections” are generally undesirable, the predictive ability of the model allows it to function eﬀectively in the real world.

<!-- b000183 | prose | pages [8] -->
Given the robust ability of the dynamic model, we propose a dynamic system for scheduling visitors down Big Long River. Our strategy will seek to eliminate chances of conﬂict and minimize oﬀschedule arrivals and visitor rejections.

<!-- b000184 | heading | pages [8] -->
Static Model

<!-- b000185 | heading | pages [8] -->
Dynamic Model

<!-- b000186 | prose | pages [8] -->
Types of Trips Oﬀered Few Options Maximum Options

<!-- b000187 | prose | pages [8] -->
Frequency of Oﬀered Low, Trips are High, Trips are Oﬀered Trips Seasonal Seasonwide Maximum Possible Fixed, Low High Visitors Very Low with Careful Chance of Conﬂict Zero Scheduling Chance of Early or Late Low with Careful Zero Completions Scheduling

<!-- b000188 | caption | pages [8] -->
Table 2: A comparison of static and dynamic strategies of scheduling visitors to raft down

<!-- b000189 | prose | pages [8] -->
the river. While the static model oﬀers a more predictable output, with guarantees for no delays or mistimed trip completions, it also sacriﬁces a great deal of ﬂexibility in terms of trips oﬀered to visitors. The dynamic model oﬀers ﬂexibility as well as potential for more visitors participating in rafting/camping, though care and attention must be given to careful scheduling.

<!-- b000190 | prose | pages [8, 9] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000192 | furniture | pages [9] -->
Page 9 of 23

<!-- b000193 | heading | pages [9] -->
7 The Model: A Cellular Automaton-like Strategy

<!-- b000194 | prose | pages [9] -->
We here describe our dynamic model of white water river rafting scheduling over the course of a rafting season. We proceed by constructing a cellular automaton-like structure to represent the river, and deﬁne the movement rules for objects contained within the cells of the automaton. The deﬁnition of a cellular automaton has many variants, though it is generally accepted to be a grid of cells that can take on discrete values, or states. These cells evolve over discrete time steps based on speciﬁc rules, and can be iterated for inﬁnitely many desired time steps.10

<!-- b000195 | prose | pages [9] -->
Our model possesses certain similarities to a one-dimensional cellular automaton, as well as some diﬀerent characteristics that make it uniquely suited to our problem:

<!-- b000196 | prose | pages [9] -->
• We describe the river as a one-dimensional array containing Y cells.

<!-- b000197 | prose | pages [9] -->
Each cell represents a camp site, and can be in one of two states - occupied by one and only one visitor or unoccupied by a visitor. The cells will be numbered from 1 to Y , with larger numbers representing a camp site that is geographically more downstream along the river.

<!-- b000198 | prose | pages [9] -->
• We will deﬁne a visitor object that can occupy cells in the river array.

<!-- b000199 | prose | pages [9] -->
Visitors will be characterized by unique identiﬁers which we will develop in detail.

<!-- b000200 | prose | pages [9] -->
• There are a discrete number of visitor objects that can be constructed.

<!-- b000201 | prose | pages [9] -->
• Every iteration will be considered one day in real time.

<!-- b000202 | prose | pages [9] -->
• From day to day, we will apply a series of rules designed to move each visitor object in the river array to an unoccupied space in the array that is downstream from the visitor’s current position.

<!-- b000203 | prose | pages [9] -->
• Every day, new visitors will also be added to the array based on the governing rules of the automaton-like structure.

<!-- b000204 | prose | pages [9] -->
• To account for the discrete nature of the array, continuous distances are expressed as a function of the number of camp sites Y .

<!-- b000205 | caption | pages [9] -->
Figure 1: A visual demonstration of the one-dimensional cellular automaton-like structure

<!-- b000206 | prose | pages [9] -->
representing the river. Each cell represents a camp site, and is either occupied with a visitor or empty. Visitors are shown with two of the several deﬁning characteristics. Note: The data shown in this picture was arbitrarily selected and not related to any output generated by our model.

<!-- b000207 | prose | pages [9] -->
The cellular automaton-like model is highly ﬂexible in its ability to test a variety of conditions. Since the model is deﬁned by a series of governing rules, we can swap out diﬀerent sets of rules to produce diﬀerent implementations of our model. These various implementations will give us a sense of how to most ideally model the white water river rafting system. Having considered the general characteristics of the model in terms of cellular automaton terminology, we will now deﬁne the variables associated with the visitor object. We will then formulate the general rules to govern visitor movement from iteration to iteration, as well as consider speciﬁc implementations of the rules. We will ﬁnally deﬁne metrics to evaluate our results.

<!-- b000208 | prose | pages [9, 10] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000210 | furniture | pages [10] -->
Page 10 of 23

<!-- b000211 | heading | pages [10] -->
7.1 The Visitor Object

<!-- b000212 | prose | pages [10] -->
The visitor object is a central aspect of our model, as the movement rules from iteration to iteration of our one-dimensional automaton-like river will be determined by the unique characteristics of each object. We must thus state all of the relevant variables of the visitor object.

<!-- b000213 | prose | pages [10] -->
• The type of raft to be used - oar-powered or motor. The raft type deter- mines the minimum and maximum distance that a visitor can move in any given day.

<!-- b000214 | prose | pages [10] -->
• The anticipated trip length, Da. The anticipated trip length sets the initial move conditions of the visitor and is used to determine whether the visitor is on schedule upon ﬁnishing the trip.

<!-- b000215 | prose | pages [10] -->
• The current position of the visitor, y, where 1 < y ≤Y , and distance that the visitor will be moved in the next iteration, y∗. y∗is recalculated at the start of every iteration.

<!-- b000216 | prose | pages [10] -->
• The number of days traveled, Di, and the number of days left to complete the trip, Dr. In the instance that Dr is 0 but y < Y (which occurs when the raft is late), Dr is reset to 1; however, Di keeps track of this change and reports that the raft was late.

<!-- b000217 | prose | pages [10] -->
• The bump coeﬃcient, β. In the instance of conﬂicts, β is used to determine which visitor is placed in the desired camp site and which visitor is placed in a diﬀerent site. β depends on how far the visitor must travel to reach the end of the river as well as the number of days left in the trip.

<!-- b000218 | prose | pages [10] -->
Bump Coeﬃcient. β = Y −y Dr β is thus of equivalent form to the ideal number of camp sites that a visitor should travel in a day. However, β is continuous, while ideal travel distance is rounded up to produce a discrete value.

<!-- b000219 | prose | pages [10] -->
• The bump direction. Bump direction can either represent the upstream direction or the downstream direction, and plays a role in resolving conﬂicts. The value of bump direction is set based on the speciﬁc rules governing the model.

<!-- b000220 | heading | pages [10] -->
7.2 Governing Rules for the Model

<!-- b000221 | prose | pages [10] -->
We here consider the general outline of rules for scheduling of visitors in our cellular automaton-like model. This will serve as a template for generation of implementations of the model. Due to the highly ﬂexible nature of the model, variants on rules can be quickly substituted to produce other implementations, which we will also test. In general, in any given iteration of the model, the following procedures are followed:

<!-- b000222 | prose | pages [10] -->
1. Queueing and Loading: The visitors to be loaded on to the river are deﬁned (based on raft type and Da) and input into the model. To generate sample data for our model, we used a Poisson distribution with mean λ. Diﬀerent values of λ were tested, with λ ranging from 1 to 15.

<!-- b000223 | prose | pages [10] -->
2. Moving: For each visitor, y∗is calculated based on the move rules of the imple- mentation. If this distance is between the moving constraints of the visitor (as deﬁned in Table 1), the visitor is moved y* camp sites downstream in the river ar- ray. Otherwise, the visitor is moved according to the absolute minimum or absolute maximum moving distance, based on the speciﬁc scenario.

<!-- b000224 | heading | pages [10] -->
3. Resolving Conﬂicts: For all cells with more than two visitors, the bump rules

<!-- b000225 | prose | pages [10] -->
of the implementation are used to resolve conﬂicts. These rules are implemented until no conﬂicts remain.

<!-- b000226 | prose | pages [10] -->
4. Perform Calculations: The desired metrics are calculated. If any visitors have y > Y , they are dequeued from the model.

<!-- b000227 | prose | pages [10, 11] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000229 | furniture | pages [11] -->
Page 11 of 23

<!-- b000230 | prose | pages [11] -->
Pois(λ) Load Move Resolve Perform Queue River Tourists Conflicts Calculations

<!-- b000231 | prose | pages [11] -->
Iterate for 180 Days

<!-- b000232 | caption | pages [11] -->
Figure 2: A schematic for the generalized rules governing our cellular automaton-like river

<!-- b000233 | prose | pages [11] -->
model. Note that both the Moving and Resolving Conﬂicts steps can be quickly replaced with variants to test desired conditions.

<!-- b000234 | heading | pages [11] -->
7.3 An Ideal Implementation of the Model

<!-- b000235 | prose | pages [11] -->
Having considered the generalized rules for the model, we develop a speciﬁc implementa- tion of the model. This implementation utilizes an ideal bumping procedure to ensure that scheduling conﬂicts are minimized. To fully describe this implementa- tion, we deﬁne the move rules and the bump rules for the implementation:

<!-- b000236 | prose | pages [11] -->
• Move: At the beginning of every turn, y* is calculated for each visitor with the formula y∗= (Y −y)/Dr This ideal moving distance is then used to move each visitor down the river. We stress that in this implementation, y* is calculated every iteration - that is, movement is self-correcting.

<!-- b000237 | prose | pages [11] -->
• Bump: In case of scheduling conﬂict, the visitor with the highest β remains at the originally assigned camp site. All other visitors search for the nearest unoccupied camp site within their movement range in their bump di- rection. If such a camp site does not exist, then the visitor searches for the nearest unoccupied camp site within their movement range opposite the bump direction.

<!-- b000238 | prose | pages [11] -->
– If such a camp site does not exist, then the visitor is removed from the model and a note is made of this error. In our real world predictive model, where visitor data is known well in advance of the visitor launch date, this action corresponds to the river management informing a customer that his desired trip is not available.

<!-- b000239 | prose | pages [11] -->
• Bump Direction: When each visitor is loaded into the model, the visitor is assigned a random bump direction. After this initialization, the bump direction is

<!-- b000240 | prose | pages [11] -->
If NO: Visitor Queue: Populate Reservoir of Rejected Desired trip offered? Completed Visitors

<!-- b000241 | prose | pages [11] -->
If YES: If YES:

<!-- b000242 | prose | pages [11] -->
Evaluate Visitors: Move Visitors: Resolve Conflicts: Load River Any visitors y* If βA > βB Bump B completed?

<!-- b000243 | prose | pages [11] -->
If NO: Perform Calculations:

<!-- b000244 | prose | pages [11] -->
Optimize y* # Interactions

<!-- b000245 | caption | pages [11] -->
Figure 3: A schematic for a speciﬁc implementation of our automaton-like model. In this

<!-- b000246 | prose | pages [11] -->
particular implementation, y∗is the ideal moving distance of each visitor. Though the chart points out that it is possible that any given implementation does not oﬀer all of the trips, in our data testing we allowed visitors to select any trip.

<!-- b000247 | prose | pages [11, 12] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000249 | furniture | pages [12] -->
Page 12 of 23

<!-- b000250 | prose | pages [12] -->
reversed every time the visitor is bumped. This reduces the likelihood that a visitor is bumped twice in the same direction, thus assisting in keeping the visitor on schedule.

<!-- b000251 | heading | pages [12] -->
7.4 Control Implementations

<!-- b000252 | prose | pages [12] -->
To be able to assess the capacity of our ideal implementation of our model, we must have some standards of comparison. We thus generate variants of our ideal imple- mentation to serve as control implementations. These variants will constructed to highlight the unique characteristics that make our ideal implementation optimal. We will consider two major experiments:

<!-- b000253 | heading | pages [12] -->
1. We determine the role of both recalculating y∗every turn and the use

<!-- b000254 | prose | pages [12] -->
of an ideal bump procedure on our model. Our ideal implementation recal- culates y∗from iteration to iteration so as to be a self-correcting approach; we will thus create a variant implementation where y∗is only calculated upon loading the visitor into the river. We will also create an implementation that does not bump visitors in case of scheduling conﬂict.

<!-- b000255 | heading | pages [12] -->
2. We will consider how the initialization of bump direction as well as the

<!-- b000256 | prose | pages [12] -->
reversing of bump direction following a bump aﬀect our model. In our ideal implementation, bump direction is initially set randomly; bump direction is then reversed every time a visitor is bumped. We will thus test variants in which the initial bump direction is always the same, as well variants in which bump direction is not reversed following a bump. This experiment will allow us to consider the self-correcting nature of our ideal bump rule.

<!-- b000257 | prose | pages [12] -->
We summarize all of the implementations to be tested in the table below.

<!-- b000258 | prose | pages [12] -->
Initial Bump Unidirectional y∗recalculated? Implementation Direction Bumping?

<!-- b000259 | prose | pages [12] -->
A (Ideal) Yes Random No B (Exp. 1 Control) No Random No C (Exp. 1 Control) Yes N/A N/A D (Exp. 1 Control) No N/A N/A E (Exp. 2 Control) Yes Downstream Yes F (Exp. 2 Control) Yes Upstream Yes G (Exp. 2 Control) Yes Random Yes

<!-- b000260 | caption | pages [12] -->
Table 3: The ideal implementation as well as several control implementations. Since our

<!-- b000261 | prose | pages [12] -->
model allows for a great variety of rules to deﬁne movement, each unique aspect of our ideal implementation can be compared to a control implementation.

<!-- b000262 | heading | pages [12] -->
8 Clarifying the Metrics

<!-- b000263 | prose | pages [12] -->
Having developed our dynamic cellular automaton-like model for white water river rafting systems, it is appropriate that we redeﬁne our criteria in terms of our model. We will here seek to construct metrics that can be used to evaluate the results of our model. Our metrics should serve as a tool in allowing us to compare the various implementations of our automaton model; they will also allow us to evaluate our results based on industry standards.

<!-- b000264 | heading | pages [12] -->
1. Raft-to-Raft Interactions. According to our assumptions, when on the river,

<!-- b000265 | prose | pages [12] -->
visitors do not dramatically change velocity while travelling down the river. As a result, motion down the river is a state function, and only depends on initial and ﬁnal conditions. In our model, where camp sites were represented by cells in an array, we need only consider which camp sites two visitors start and end at to determine whether an interaction has occurred.

<!-- b000266 | prose | pages [12, 13] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000268 | furniture | pages [13] -->
Page 13 of 23

<!-- b000269 | caption | pages [13] -->
Figure 4: Our assumption that visitors maintain a constant velocity throughout the day

<!-- b000270 | prose | pages [13] -->
allows us to treat movement as a state function. Thus, we need only consider which camps visitors start the day and end the day at to determine whether interactions have occurred.

<!-- b000271 | prose | pages [13] -->
Deﬁnition. Let us consider the set of visitors V that are in the river grid. For some v1, v2 ∈V , a raft-to-raft interaction occurs between v1 and v2 if and only v1 begins the day at a camp upstream from v2 and ends the day at a camp downstream from v2.

<!-- b000272 | heading | pages [13] -->
2. OﬀSchedule Completions. Oﬀschedule completions can be broken down into

<!-- b000273 | prose | pages [13] -->
both early and late completions, both of which are weighted equally when consid- ering oﬀ-schedule completions.

<!-- b000274 | prose | pages [13] -->
Deﬁnition. Let us consider the set of visitors Vf who have completed their trips successfully. The number of early completions for the river system is equal to the number of v ∈Vf such that va > vi. The number of late completions for the river system is equal to the number of v ∈Vf such that va < vi. The number of oﬀ schedule completions is equal to the sum of early and late completions.

<!-- b000275 | prose | pages [13] -->
3. System Rejections. In some rare cases, our dynamic model was unable to resolve a scheduling conﬂict, and thus removed the visitor with the lower β from the system.

<!-- b000276 | prose | pages [13] -->
In a static case, an analogy would be turning away visitors whose demands were not accommodated. Our ideal implementation of the model should seek to minimize system rejections to make the model more powerful.

<!-- b000277 | prose | pages [13] -->
Deﬁnition. Let us consider the set R of visitors who have been rejected from the model owing to unresolved scheduling conﬂicts (both prior to and after loading).

<!-- b000278 | prose | pages [13] -->
The number of rejections for system is equal to |R|.

<!-- b000279 | heading | pages [13] -->
4. Carrying Capacity. The carrying capacity of a model or implementation of a

<!-- b000280 | prose | pages [13] -->
model is, as per our previous discussion, the maximum number of visitors that can be accommodated in a white water rafting system per season while maintaining high standards of visitor satisfaction. We now present a more developed deﬁnition of carrying capacity in terms of the other metrics used to evaluate the model.

<!-- b000281 | prose | pages [13] -->
Deﬁnition. Let us consider a model or implementation of a model M. The carrying capacity of M is the maximum number of visitors that the model allows to complete a trip in one rafting reason over all values of Y and λ such that three standards are met: 1) System rejections are fewer than 10% of the visitors that travel down the river throughout the season, 2) The number of visitors who complete the trip oﬀschedule is less than 10% of the total visitors for the season, and 3) There are fewer than 10 boat-to-boat interactions per person per day.

<!-- b000282 | heading | pages [13] -->
5. Camp-to-Camp Interactions. Our assumptions stated that visitors will only

<!-- b000283 | prose | pages [13] -->
move within a short distance of their camp site. Given that our visitors will have spent a signiﬁcant period of time rafting, it is unlikely that they will follow up this rafting with extensive hiking; furthermore, for reasonable values of Y , the probability of two visitors from even adjacent camp sites interacting is very low.

<!-- b000284 | prose | pages [13] -->
As a result, we state that the number of camp-to-camp interactions in our model is zero.

<!-- b000285 | prose | pages [13] -->
6. Raft-to-Camp Interactions. As per our assumptions, camp sites are located at a distance from the river shore. As a result, we state that the number of raft-to-camp interactions in our model is zero.

<!-- b000286 | prose | pages [13, 14] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000288 | furniture | pages [14] -->
Page 14 of 23

<!-- b000289 | heading | pages [14] -->
9 Results

<!-- b000290 | prose | pages [14] -->
No. of % Rejec- % Oﬀ Implementation % Early % Late Visitors tions Schedule A (Ideal) 756 3.8 2.1 0.4 1.7 B (Constant y∗) 753 5.5 42.3 30.3 12 C (No Bump 182 75.5 0 0 0 Rule) D (Constant y∗, 190 74.6 27.5 27.5 0 No Bump Rule)

<!-- b000291 | caption | pages [14] -->
Table 4: Results of our ﬁrst experiment, in which two variations were considered: 1) y∗

<!-- b000292 | prose | pages [14] -->
is not recalculated at the start of every iteration and 2) the bump rule is removed. We tested these implementations with Y = 100 and λ = 5.

<!-- b000293 | prose | pages [14] -->
No. of % Rejec- Interactions % Oﬀ Implementation Visitors tions per Visitor Schedule A (Ideal) 754 4.86 7.10 2.2 E (Unidirectional Downstream 719 8.73 7.34 2.2 Bumping) F (Unidirectional Upstream Bump- 516 35.0 4.79 1.44 ing) G (Unidirectional 190 74.6 27.5 27.5 Random Bump)

<!-- b000294 | caption | pages [14] -->
Table 5: Results of our second experiment, in which we investigated unidirectional bump-

<!-- b000295 | prose | pages [14] -->
ing. We tested these implementations with Y = 100 and λ = 5.

<!-- b000296 | prose | pages [14] -->
We present here the comparison of our ideal implementation (with idealized movement and bump rules) against control implementations designed to high- light the key components our the ideal implementation. From examining the results in Tables 4 and 5, we note the following:

<!-- b000297 | prose | pages [14] -->
• Implementations with bumping rules increase the maximum number of visitors that completed trips during the season by nearly 400% over implementations without bumping rules. However, as seen in implementation B, without recalculating y∗at the start of each iteration of the model, the number of visitors that ﬁnish oﬀ-schedule also increases.

<!-- b000298 | prose | pages [14] -->
• The implementations that lack bumping move the visitors down the river in a manner analogous to that of a static model. In these implementations, each visitor has an ideal camp site that they travel to everyday regardless of other parameters. Therefore, everyone arrives on time, but the number rejected visitors is very high.

<!-- b000299 | prose | pages [14] -->
• Recalculating y∗has very little impact on the total number of visitors but nearly eliminates the number of visitors who arrive oﬀschedule.

<!-- b000300 | prose | pages [14] -->
• Bumping in only one direction lowers the number of visitors who com- plete trips. This can be explained from the fact that when bumping in only one direction, there are less ways to resolve conﬂicts at camp sites and therefore less visitors can be on the river at any one time.

<!-- b000301 | prose | pages [14] -->
• While bumping in only one direction has the potential to reduce average boat interactions compared to bidirectional bumping implementations, unidirectional bumping implementations also reject a greater percentage of visitors.

<!-- b000302 | prose | pages [14, 15] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000304 | furniture | pages [15] -->
Page 15 of 23

<!-- b000305 | prose | pages [15] -->
• Bidirectional bumping rules increase the number of ways to resolve conﬂicts at camp sites. As a result, such implementations allow more visitors to complete trips during the season, and reject fewer visitors.

<!-- b000306 | prose | pages [15] -->
• While bidirectional bumping may increase the percentage of visitors who complete their trip oﬀschedule, this increase is oﬀset by a signiﬁcant diminishing of the number of rejected visitors.

<!-- b000307 | prose | pages [15] -->
These experiments have allowed us to demonstrate that Implementation A is in fact the ideal implementation of our model. Implementation A performs optimally from both a customer satisfaction and a business point of view. Not only is the number of visitors who participate in rafting throughout the season maximized, but the number of visitors whose desired trips are not accommodated is minimized. We will now test Implementation A over a wide variety of Y values and λ to determine how successful our model is at scheduling white water river rafting systems.

<!-- b000308 | heading | pages [15] -->
9.1 Number of Interactions

<!-- b000309 | prose | pages [15] -->
In order to ensure high standards of customer satisfaction, we want to ensure that the

<!-- b000310 | caption | pages [15] -->
Figure 5: Surface and contour plot for average number of boat interactions per person

<!-- b000311 | prose | pages [15] -->
with respect to λ and Y .

<!-- b000312 | prose | pages [15, 16] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000314 | furniture | pages [16] -->
Page 16 of 23

<!-- b000315 | prose | pages [16] -->
number of boat-to-boat interactions per visitor is lower than the standard industry value. According to literature, customer satisfaction decreases if visitors experience more than 10 interactions per day. For Implementation A of our model, however, the total number of interactions per visitor over the course of the season is less than 10 interactions. Furthermore, values of boat-to-boat interactions are generally constant across variable values of λ and Y , showing the powerful nature of our model in maintaining high customer satisfaction standards. This observation also implies that carrying capacity of the model is not impacted signiﬁcantly by boat-to-boat interactions.

<!-- b000316 | heading | pages [16] -->
9.2 Number of Visitor Rejections

<!-- b000317 | prose | pages [16] -->
As one of the key aspects of our model is that it accommodates for the demands of the customer, we sought to minimize the number of rejected visitors from our model. Through visual inspection of the surface, it is clear that the value for % rejections drops oﬀrapidly as a function of Y and is largely independent of λ at large values of Y . Thus, at large values of Y , Implementation A of our model is able to greatly maximize the number of visitors accommodated into the white water river rafting system.

<!-- b000318 | caption | pages [16] -->
Figure 6: Surface and contour plot for the percentage of visitors who are rejected over the

<!-- b000319 | prose | pages [16] -->
course of the season with respect to λ and Y .

<!-- b000320 | prose | pages [16, 17] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000322 | furniture | pages [17] -->
Page 17 of 23

<!-- b000323 | heading | pages [17] -->
9.3 Oﬀ-Schedule Completions

<!-- b000324 | caption | pages [17] -->
Figure 7: Surface and contour plot for the percentage of visitors who complete their trip

<!-- b000325 | prose | pages [17] -->
early or late with respect to λ and Y .

<!-- b000326 | prose | pages [17] -->
We here consider the number of visitors who completed their trip oﬀschedule. We note that when visitors in our implementation of our model are oﬀschedule, they are often oﬀ schedule by only one day. By examining the surface, we see that the percentage of oﬀ schedule visitors drops oﬀrapidly as Y increases and becomes independent of λ at large values of Y . This observation is similar to the change in the percent of visitor rejections with respect to λ and Y . Furthermore, we note that the % of oﬀschedule visitors approaches zero with increasing Y , implying that it is possible with enough camp sites to eﬀectively eliminate the chance that a visitor will arrive early or late.

<!-- b000327 | heading | pages [17] -->
9.4 Carrying Capacity

<!-- b000328 | prose | pages [17] -->
Based on the data from our various tests of Implementation A of our model, we can now consider a carrying capacity for our model.

<!-- b000329 | prose | pages [17] -->
Our deﬁnition of carrying capacity was based on determining the maximum number of visitors who could complete trips in a rafting season based on certain constraints of visi- tor satisfaction. Having analyzed the data, we can see that the carrying capacity for

<!-- b000330 | prose | pages [17, 18] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000332 | furniture | pages [18] -->
Page 18 of 23

<!-- b000333 | caption | pages [18] -->
Figure 8: Surface and contour plot for the number of visitors who are able to complete

<!-- b000334 | prose | pages [18] -->
trips in our white water river rafting system over a rafting season of six months.

<!-- b000335 | prose | pages [18] -->
Implementation A of our model is 1102 visitors per season. This carrying ca- pacity occurs when the system has 180 camp sites and is loading an average of 15 visitors a day into the model. At this carrying capacity, we note that:

<!-- b000336 | prose | pages [18] -->
• The percentage of visitors who are rejected by the model is 1.79%. Thus, our model accounts for the trip desires of 98.21% of visitors.

<!-- b000337 | prose | pages [18] -->
• The percentage of visitors who complete their trip oﬀschedule is 0.67%.

<!-- b000338 | prose | pages [18] -->
Thus, our model completes 99.33% of visitors trips perfectly on schedule.

<!-- b000339 | prose | pages [18] -->
• The average number of interactions per person per season is 10.35. We note again that this value is signiﬁcantly lower than the established standard for white water river rafting systems.

<!-- b000340 | prose | pages [18] -->
However, we make the observation that the carrying capacity of our model occurs when the river system has 180 camp sites, which from an economic standpoint may be very costly to maintain. We note that a more economic decision would be to sacriﬁce some of the carrying capacity and reduce the number of camp sites along the river. For example, at Y = 100 and λ = 15, the capacity is 1025 visitor groups per season, which is remarkably high and more cost eﬃcient than the actual carrying capacity.

<!-- b000341 | prose | pages [18, 19] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000343 | furniture | pages [19] -->
Page 19 of 23

<!-- b000344 | heading | pages [19] -->
10 Further Investigations

<!-- b000345 | prose | pages [19] -->
Based on the data collected so far, it is clear that Implementation A of our dynamic model performs excellently in idealized conditions; however, the real world performance of implementation A should also be analyzed. This can be accomplished by breaking some of the assumptions used in making the model and seeing if the model can perform adequately and if not, what this means and how poor performance in the real world can be rectiﬁed.

<!-- b000346 | heading | pages [19] -->
10.1 Environmental Degradation

<!-- b000347 | prose | pages [19] -->
In our model, we assumed that camp sites would remain functional throughout the season. However, this is not realistic. Currently research has shown that frequency of use of camp sites is a major factor in soil quality and vegetation at the camp site. After a certain point of degradation, camp sites can even become unusable.

<!-- b000348 | prose | pages [19] -->
We can thus model a more realistic system based on the literature for the river sys- tem by deﬁning the number of operational camp sites on any given day in the river system as:

<!-- b000349 | prose | pages [19] -->
[Y −α log(λ)]

<!-- b000350 | prose | pages [19] -->
Based on this formula, we present environmental degradation data from our model:

<!-- b000351 | prose | pages [19] -->
Number of λ Visitors α = 0 769 910 973 1071 10 755 880 900 830 20 680 751 570 525 30 556 497 323 298

<!-- b000352 | prose | pages [19] -->
% Oﬀ λ Schedule α = 0 1.8 2.3 3.5 4.0 10 3.7 6.1 8.0 10 20 9.1 10 24 18 30 12 28 33 54

<!-- b000353 | prose | pages [19] -->
% Rejected λ Visitors α = 0 0.5 0.7 1.9 2.9 10 2.6 3.5 15.3 23.6 20 9.9 19.2 45.7 49.6 30 28.3 47.7 71.0 75.1

<!-- b000354 | caption | pages [19] -->
Table 6: We consider the possibility that environmental degradation could cause camp

<!-- b000355 | prose | pages [19] -->
sites to become unusable. Here, we present data for our environmental degradation model, where Y = 110 camp sites.

<!-- b000356 | prose | pages [19] -->
From these tables it is clear that very high values of α greatly eﬀect the per- formance of Implementation A. When α is equal to zero, the number of camp sites

<!-- b000357 | prose | pages [19, 20] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000359 | furniture | pages [20] -->
Page 20 of 23

<!-- b000360 | prose | pages [20] -->
remains unchanged; for larger values of α the number of available camp sites greatly de- creases. Furthermore, the % rejected and % oﬀ-schedule visitors are greatly perturbed by increasing α. It can be concluded that for locations that are prone to factors that can render camp sites unusable should expect to have higher % rejected visitors and % oﬀ-schedule visitors for a lower number of visitors total for any given Y . The eﬀects of high alpha can be mediated in two ways:

<!-- b000361 | heading | pages [20] -->
1. The rafting service can build more camp sites to mask the eﬀect of α.

<!-- b000362 | heading | pages [20] -->
2. The rafting company can take measures to protect the environmental

<!-- b000363 | prose | pages [20] -->
integrity and maintenance of the camp sites.

<!-- b000364 | heading | pages [20] -->
10.2 Mitigating Storms

<!-- b000365 | prose | pages [20] -->
In addition to the assumption that camp sites do not degrade or get damaged over time, our initial implementation was not designed explicitly to handle events that interrupt the normal ﬂow of visitors down the river. However, in the real world, happenings such as storms can interrupt this ﬂow and any good model must be able to account for these events. Therefore, we added a rule to implementation A that is called whenever ﬂow down the river is prevented. This rule prevents movement and the loading of new visitors for N number of days. For each day that this rule is active, each visitor has their Di incremented, eﬀectively putting them behind schedule to reﬂect the fact that they were unable to move to the next camp site that day. This rule allows for the simulation of any event that occurs at a ﬁxed probability and lasts for a ran- dom number of days distributed according to a Poisson distribution of given µ, where µ is the average length of the event. For testing purposes, we treated this random event as a storm with a ﬁxed chance of occurring in any given trial and an average length of 1 day. For 4 values of λ, 4 diﬀerent probabilities of a storm occurring were tested at Y = 110.

<!-- b000366 | prose | pages [20] -->
Based on the results of these additional calculations, we noted that for low values of the % chance of storm the model performed very well. The eﬀect upon the number of visitors total is minimal. Furthermore, for values of %chance of storm 5%, the % of oﬀschedule visitors is only marginally above the 10% cut-oﬀfor customer satisfac- tion. This is acceptable as visitors would likely understand that the weather is beyond the control of the rafting company.

<!-- b000367 | heading | pages [20] -->
11 Conclusion

<!-- b000368 | prose | pages [20] -->
Using our dynamic model, we have demonstrated that it is possible to maintain high carrying capacities on the Big Long River while continuing to oﬀer a wide range of trip options and maximizing customer satisfaction. Furthermore, using this dynamic model, conﬂicts for camp sites can be eliminated ensuring that each rafting group has its own camp site. In order to evaluate the model’s performance we deﬁned a number of customer satisfaction metrics such as the percentage of visitors unable to book, the percentage of visitors that do not ﬁnish the trip on schedule and the average number of boat to boat interaction over the entire season. After analyzing the values of these metrics at varying values of lambda and Y we discovered that the only metric that limits the carrying capacity of the river is the percent of visitors that are unable to book. When Y ¿ 110, all the metrics indicate that customer satisfaction is suﬃciently high, regardless of the value for lambda. The carrying capacity of the river was deﬁned to be the maximum number of visitors that could be served during a season. The carrying capacity was equal to 1102.8 and occurred

<!-- b000369 | prose | pages [20, 21] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000371 | furniture | pages [21] -->
Page 21 of 23

<!-- b000372 | prose | pages [21] -->
at Y = 180 and λ = 15. Furthermore, the practical carrying capacity, the point where the ratio between the number of people and camp sites was minimized was found to be when there were 1074 visitors, Y = 110 and λ = 15. In order to test the applicability of implementation to real life scenarios, real life phenom- ena such as storms and environmental degradation of camp sites were added. In these circumstances, the implementation performed well and oﬀered insight into better ways that rafting companies could design their systems to better handle adverse events. Fur- thermore, since our implementation was deﬁned in terms of generic variables representing the properties of the river, this implementation can be applied to any rafting system that can be modelled as a one-dimensional array.

<!-- b000373 | prose | pages [21, 22] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000375 | furniture | pages [22] -->
Page 22 of 23

<!-- b000376 | heading | pages [22] -->
12 Memo to Rafting Management

<!-- b000377 | prose | pages [22] -->
As the number of people participating in white water river rafting increases every year, it has become necessary to develop a powerful method of scheduling multi-day rafting trips. Current industrial models provide river managers with a ﬁxed number and type of trips to oﬀer throughout the rafting season. However, while ensuring perfect scheduling, these static models fail to account for customer demands and may cause rafting companies to lose customers. We instead propose a highly powerful dynamic scheduling model that is built around maximizing the number of trip options provided to customers.

<!-- b000378 | prose | pages [22] -->
In this dynamic model, visitors are allowed to choose a trip that is customized to suit their speciﬁc needs. The rafting agency can then input the customer data into our model, which will consider the visitor’s movement down the river on a day-to-day basis. In each iteration of the model, the visitor is moved to a camp site based on their trip characteristics and the current camp site occupancy. If the model encounters a conﬂict in scheduling, it will calculate the best method to reassign one of the visitors. In the rare instance that a visitor cannot be reassigned to some camp site, the model returns an error to the rafting management. Since the rafting agency can input data into our model far before the launch date of the visitor, the agency can predict ahead of time whether a visitor’s desired trip can be accommodated based on the current camp site occupancy.

<!-- b000379 | prose | pages [22] -->
To test our model, we generated random visitors with diﬀerent trip requests. We varied the number of camp sites along the river as well as the number of visitors added daily to the model. The maximum number of visitors for a six-month rafting season that can be accommodated by our model is 1102, and occurs when 180 camp sites are present and 15 visitors are loaded per day on average. At this maximum capacity, roughly 98% of customers are provided their desired trips, and 99.33% of the visitors complete their trip on time. Similar capacities can be obtained for a more practical number of camp sites as well. Our model also maintained high levels of customer satisfaction by minimizing visitor interactions on the river to a level far lower than the current industrial standard. We also noted the eﬃcacy of our model under circumstances that prevented the ﬂow of visitors down the river, such as storms. Finally, in line with current interests in terms of wildlife ecology, we developed a method to account for environmental degradation and implemented it into our model.

<!-- b000380 | prose | pages [22] -->
Our novel dynamic model allows for highly robust scheduling of white water rafting trips. We note that in our simulations, we tested the model over a single, 225 mile long river. In reality, rafting companies often schedule over several, much longer rivers. Thus, when applied to real life situations, our model could accommodate thousands of visitors per rafting season while providing maximum ﬂexibility in choice to visitors.

<!-- b000381 | prose | pages [22, 23] -->
C.A.R.S Cellular Automaton Rafting Simulation Control # 15878

<!-- b000383 | furniture | pages [23] -->
Page 23 of 23

<!-- b000384 | prose | pages [23] -->
Notes

<!-- b000385 | prose | pages [23] -->
1English, Donald B.K. ”Economic Impacts of Guided Whitewater Rafting: A Study of Five Rivers.” Water Resources Bulletin. 32.6 (1996): 1328. Print.

<!-- b000386 | prose | pages [23] -->
2English, Donald B.K. et. al. ”Regional Demands and Supply Projections for Outdoor Recreation.” Print.

<!-- b000387 | prose | pages [23] -->
3Whittaker, Doug et. al. ”Types of Norms for Recreation Impacts: Extending the Social Norms Concept.” Journal of Leisure Research. 20.4 (1988): 261-273. Print.

<!-- b000388 | prose | pages [23] -->
4”The Wilderness Simulation Model.” International Journal of Wilderness. 9.2 (2003): 9 - 13. Print.

<!-- b000389 | prose | pages [23] -->
5”The Wilderness Use Simulation Model Applied to the Colorado River Boating in Grand Canyon National Park, USA.” Environmental Management. 10.3 367-374. Print.

<!-- b000390 | prose | pages [23] -->
6”RIVER SAFETY.” Texas River Guide. Texas Parks and Wildlife, n.d. Web. ¡http://www.tpwd.state.tx.us/landwater/water/habitats/rivers/safety.phtml¿.

<!-- b000391 | prose | pages [23] -->
7”Sample Itinerary.” . Wilderness Awareness Rafting, n.d. Web. 13 Feb 2012. ¡http://www.inaraft.com/pdf/itinerary/itin-ark river 5-day.pdf¿.

<!-- b000392 | prose | pages [23] -->
8Haas, Glenn E. RECREATION AND PARKS:. The Pennsylvania State University, 1997. Print.

<!-- b000393 | prose | pages [23] -->
9Vaske, Jerry J. et. al. ”Backcountry Encounter Norms: Theory, Method, and Empir- ical Evidence.” Journal of Lesiure. 18.3 (1986): 137-153. Print.

<!-- b000394 | prose | pages [23] -->
10”Cellular Automaton – from Wolfram MathWorld.” Wolfram MathWorld: The Web’s Most Extensive Mathematics Resource. Web. 13 Feb. 2012.

<!-- b000395 | prose | pages [23] -->
C.A.R.S Cellular Automaton Rafting Simulation
