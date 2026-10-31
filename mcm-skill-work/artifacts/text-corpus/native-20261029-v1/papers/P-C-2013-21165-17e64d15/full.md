# P-C-2013-21165-17e64d15

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
For office use only

<!-- b000006 | title | pages [1] -->
21165

<!-- b000007 | prose | pages [1] -->
T1 ________________ T2 ________________

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | prose | pages [1] -->
T3 ________________

<!-- b000010 | prose | pages [1] -->
F1 ________________ F2 ________________ F3 ________________

<!-- b000011 | prose | pages [1] -->
Problem Chosen

<!-- b000012 | prose | pages [1] -->
T4 ________________

<!-- b000013 | furniture | pages [1] -->


<!-- b000014 | prose | pages [1] -->
F4 ________________

<!-- b000015 | title | pages [1] -->
C

<!-- b000016 | furniture | pages [1] -->


<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | heading | pages [1] -->
2013 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000019 | prose | pages [1] -->
(Attach a copy of this page to your solution paper.)

<!-- b000020 | prose | pages [1] -->
Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | heading | pages [1] -->
Abstract

<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | furniture | pages [1] -->


<!-- b000030 | prose | pages [1] -->
In this paper, we build a model to measure the earth’s health in the aspect of air quality. We

<!-- b000031 | prose | pages [1] -->
choose Air Quality Index (AQI) as the basis of health measure, while using a weighted average as

<!-- b000032 | prose | pages [1] -->
the final expression. Our model takes the form of dual-layer network. Among the two layers, the

<!-- b000033 | prose | pages [1] -->
local network is implemented using neural network optimized by Particle Swarm Optimization

<!-- b000034 | prose | pages [1] -->
(PSO) algorithm, while the global network links the nodes with feedback links defined by certain

<!-- b000035 | prose | pages [1] -->
propagation function. The model takes the output from the former year as the input of the following

<!-- b000036 | prose | pages [1] -->
year, thus establishing an autonomous system by itself.

<!-- b000037 | prose | pages [1] -->
We then move on to verify the model. First we test the model’s fundamental network property

<!-- b000038 | prose | pages [1] -->
from the perspective of fit, critical nodes, and missing relationships. As case studies, we applied our

<!-- b000039 | prose | pages [1] -->
model to specific nations on a timespan of 1985-2008, namely Japan, India, and Hungary in hope to

<!-- b000040 | prose | pages [1] -->
demonstrate that our model is able to generate prediction and warnings of state changes, and

<!-- b000041 | prose | pages [1] -->
provide information for decision-makers. Our model has shown a completeness of functionality and

<!-- b000042 | prose | pages [1] -->
impressive flexibility in these tests. Furthermore, we have been able to see that the prediction test of

<!-- b000043 | prose | pages [1] -->
our model coincides fairly well with the fact.

<!-- b000044 | furniture | pages [1] -->


<!-- b000045 | keywords | pages [1] -->
Key words: global, neural network, Air Quality Index, autonomous

<!-- b000046 | furniture | pages [2] -->
Team #21165

<!-- b000047 | furniture | pages [2] -->


<!-- b000048 | furniture | pages [2] -->


<!-- b000049 | furniture | pages [2] -->
Page 1 of 18

<!-- b000050 | prose | pages [2] -->
Link Our Breath: A Linked Neural Network

<!-- b000051 | heading | pages [2] -->
Approach to A Global Environment Model

<!-- b000052 | furniture | pages [2] -->


<!-- b000053 | prose | pages [2] -->
Content 1 Introduction ....................................................................................................................................... 2 1.1 Background ............................................................................................................................ 2 1.2 An Overview of Air Quality................................................................................................... 2 1.2.1 Air Quality: A Reflection of Earth’s Health ............................................................... 2 1.2.2 Primary Influence Factors ........................................................................................... 3 1.3 Air Quality Index (AQI) ........................................................................................................ 3 1.4 Assumptions ........................................................................................................................... 4 1.5 Notations ................................................................................................................................ 4 2 Model ................................................................................................................................................ 4 2.1 Generic Methodology ............................................................................................................ 4 2.2 Basic Model ........................................................................................................................... 7 2.2.1 Input and Output of Local Network ............................................................................ 7 2.2.2 Global Network Aspect ............................................................................................... 7 2.3 Advanced Model .................................................................................................................... 7 2.3.1 Input and Output of Local Network ............................................................................ 7 2.3.2 Global Network Aspect ............................................................................................... 7 3 Verification ...................................................................................................................................... 8 3.1 Overview ................................................................................................................................ 8 3.2 Fit verification ........................................................................................................................ 9 3.3 Identifying critical nodes ..................................................................................................... 10 3.4 Sensitivity to a relationship change ..................................................................................... 10 3.5 Case Study............................................................................................................................ 12 4 Conclusion ...................................................................................................................................... 15 4.1 Strength and Weakness ........................................................................................................ 15 4.2 Extension .............................................................................................................................. 15 References .......................................................................................................................................... 17 Other References ................................................................................................................................ 17

<!-- b000054 | furniture | pages [2] -->


<!-- b000055 | prose | pages [2] -->
List of Figures

<!-- b000056 | furniture | pages [2] -->


<!-- b000057 | caption | pages [2] -->
Figure 1: World3 Computer Model Scenario 2: More Abundant Nonrenewable Resources [3] .............................. 2

<!-- b000058 | caption | pages [2] -->
Figure 2 (a) (b) The Increasing rates of change in human activity (c) Global scale changes in the Earth system as

<!-- b000059 | prose | pages [2] -->
a result of the dramatic increase in human activity: atmospheric N2O concentration [2] .............................. 3

<!-- b000060 | caption | pages [2] -->
Figure 3 The basic framework .................................................................................................................................. 5

<!-- b000061 | caption | pages [2] -->
Figure 4 The result of stepwise forecast: Belgium ................................................................................................... 9

<!-- b000062 | caption | pages [2] -->
Figure 5 Identifying the critical nodes .................................................................................................................... 10

<!-- b000063 | caption | pages [2] -->
Figure 6 (a) (b) Sensitivity to a relationship change: removing or not removing China ....................................... 11

<!-- b000064 | caption | pages [2] -->
Figure 7 (a) (b) The change of world pollution distribution .................................................................................. 12

<!-- b000065 | caption | pages [2] -->
Figure 8 Case Study using an autonomous forecast: Japan ................................................................................... 13

<!-- b000066 | caption | pages [2] -->
Figure 9 Case Study using an autonomous forecast: India .................................................................................... 14

<!-- b000067 | caption | pages [2] -->
Figure 10 Case Study using an autonomous forecast: Hungary ............................................................................ 14

<!-- b000068 | furniture | pages [2] -->


<!-- b000069 | prose | pages [2] -->
List of Tables

<!-- b000070 | caption | pages [2] -->
Table 1 ............................................................................................................................................................. 3

<!-- b000071 | caption | pages [2] -->
Table 2 ............................................................................................................................................................. 4

<!-- b000072 | caption | pages [2] -->
Table 3 ............................................................................................................................................................. 7

<!-- b000073 | furniture | pages [2] -->


<!-- b000074 | furniture | pages [3] -->
Team #21165

<!-- b000075 | furniture | pages [3] -->


<!-- b000076 | furniture | pages [3] -->


<!-- b000077 | furniture | pages [3] -->
Page 2 of 18

<!-- b000078 | heading | pages [3] -->
1 Introduction

<!-- b000079 | heading | pages [3] -->
1.1 Background

<!-- b000080 | prose | pages [3] -->
The growing stress on Earth’s environment and biological system are extremely apparent now. 15 out of 24 of the ecosystem services examined during the UN-based Millennium Ecosystem Assessment are being degraded or used unsustainably, including fresh water, capture fisheries, air and water purification and the regulation of regional and local climate, natural hazards, and pests [1].

<!-- b000081 | prose | pages [3] -->
Human activity is the main reason causing the significant changes of ecosystems which harm Earth health a lot. The largely growing demand of natural source over the past 50 years changed ecosystems more rapidly and extensively than in any comparable period of time in human history. [1] Moreover, excessive emission of the waste and pollutant leads to dramatic environmental changes as well.

<!-- b000082 | prose | pages [3] -->
Many global scale changes in ecosystems are displayed as exponential growth in the past half century. They can be large in magnitude and difficult or impossible to reverse once a threshold is crossed. As many of the trends appeared in the past century have continued, it is likely that the degradation of ecosystem services could grow worse in this century. In this way, global ecosystem may be approaching a planetary-scale ‘tipping point’. Therefore a prediction of potential state change of Earth’s health is needed. [2]

<!-- b000083 | furniture | pages [3] -->


<!-- b000084 | caption | pages [3] -->
Figure 1: World3 Computer Model Scenario 2: More Abundant Nonrenewable Resources [3]

<!-- b000085 | furniture | pages [3] -->


<!-- b000086 | caption | pages [3] -->
Figure 1 postulates that advances in resource extraction technologies are capable of postponing

<!-- b000087 | prose | pages [3] -->
the onset of increasing extraction costs [3]. Under such postulation, the ‘tipping point’ will occur in around 2050.

<!-- b000088 | furniture | pages [3] -->


<!-- b000089 | heading | pages [3] -->
1.2 An Overview of Air Quality

<!-- b000090 | prose | pages [3] -->
1.2.1 Air Quality: A Reflection of Earth’s Health Air quality regulation is one of that fifteen ecosystem services which are being degraded and used unsustainably. Human need to pay much attention on air quality for not only it can reflect the condition of the Earth environment but also directly affect the health of many creatures. Moreover, it cannot be neglected that atmosphere activity helps the pollutant dispersion as well.

<!-- b000091 | prose | pages [3] -->
In most cases, climate changes and air quality are combined and many recent studies prefer to pay more attention on the greenhouse effect. However, both Great London Smog in 1952 and North China haze in 2013 show that heavy air pollution and particle pollution have lethal potential.

<!-- b000092 | furniture | pages [4] -->
Team #21165

<!-- b000093 | furniture | pages [4] -->


<!-- b000094 | prose | pages [4] -->
1.2.2 Primary Influence Factors

<!-- b000095 | furniture | pages [4] -->


<!-- b000096 | furniture | pages [4] -->
Page 3 of 18

<!-- b000097 | prose | pages [4] -->
 Population explosion and rapid economic growth

<!-- b000098 | prose | pages [4] -->
Between 1800 and 2000, the human population grew from about one billion to six billion, while energy use grew by about 40-fold and economic production by 50-fold [4]. In addition, the consumption of petroleum grew by a factor of 3.5 since 1960. The number of motor vehicles rose from only 40 million at the end of WWII to about 700 million by 1996, and continues to rise steadily [2]. Despite such rapid growth in population and economy, such a growth has also left a significant imprint on the environment, which is shown in the figures below.

<!-- b000099 | furniture | pages [4] -->


<!-- b000100 | furniture | pages [4] -->


<!-- b000101 | prose | pages [4] -->
(b)

<!-- b000102 | furniture | pages [4] -->


<!-- b000103 | furniture | pages [4] -->


<!-- b000104 | furniture | pages [4] -->


<!-- b000105 | prose | pages [4] -->
(a)

<!-- b000106 | furniture | pages [4] -->


<!-- b000107 | furniture | pages [4] -->


<!-- b000108 | furniture | pages [4] -->


<!-- b000109 | furniture | pages [4] -->


<!-- b000110 | prose | pages [4] -->
(c)

<!-- b000111 | caption | pages [4] -->
Figure 2 (a) (b) The Increasing rates of change in human activity (c) Global scale changes in the Earth system

<!-- b000112 | prose | pages [4] -->
as a result of the dramatic increase in human activity: atmospheric N2O concentration [2]

<!-- b000113 | furniture | pages [4] -->


<!-- b000114 | prose | pages [4] -->
 Forest coverage

<!-- b000115 | prose | pages [4] -->
Forest coverage is a notable factor to air quality. On the one hand, gaseous and particle pollutants can be dry-deposited by trees through a mechanism named dry deposition, thus improving air quality [6]. On the other hand, many gaseous and particle pollutants, acting individually or in combination, affects forests particularly [7].

<!-- b000116 | furniture | pages [4] -->


<!-- b000117 | heading | pages [4] -->
1.3 Air Quality Index (AQI)

<!-- b000118 | prose | pages [4] -->
Air Quality Index (AQI), developed by Environment Protection Agency (EPA) of United States, is aiming at helping people know what local air quality means to their health. This index is calculated by some major air pollutants which are regulated by the Clean Air Act, such as particle pollution and sulfur dioxide, etc. Table 1 [8] shows the six categories of AQI and their meanings, each of the categories is assigned by a specific color.

<!-- b000119 | prose | pages [4] -->
Table 1

<!-- b000120 | furniture | pages [4] -->


<!-- b000121 | furniture | pages [5] -->
Team #21165

<!-- b000122 | furniture | pages [5] -->


<!-- b000123 | furniture | pages [5] -->


<!-- b000124 | furniture | pages [5] -->
Page 4 of 18

<!-- b000125 | heading | pages [5] -->
1.4 Assumptions

<!-- b000126 | prose | pages [5] -->
 The health measure of earth’s atmosphere can be assessed by Air Quality Index (AQI)

<!-- b000127 | prose | pages [5] -->
We choose AQI as the earth health measure to associate the environmental and biological systems, more details of AQI can be found in the background part of the paper.

<!-- b000128 | furniture | pages [5] -->


<!-- b000129 | prose | pages [5] -->
The following three assumptions only constrain the basic model.  While considering the air flow, the impact of topography is ignored.  One year is taken as the minimal time unit in the model.  We choose the nations around the world as the Global Nodes. The coordinates of the nodes are

<!-- b000130 | prose | pages [5] -->
represented by the capitals’ longitude and latitude positions. The assumptions above are due to the limitation of the data we have. In fact, the more data we collect, the more accurate result that the model will catch.

<!-- b000131 | furniture | pages [5] -->


<!-- b000132 | heading | pages [5] -->
1.5 Notations

<!-- b000133 | prose | pages [5] -->
Table 2 Symbol Meaning the feedback function of a node coming from another node in the global f network g the influence degree function of a node derived from feedback function

<!-- b000134 | prose | pages [5] -->
population density of a nation d

<!-- b000135 | prose | pages [5] -->
r forest coverage rate of a nation

<!-- b000136 | prose | pages [5] -->
p proportion of secondary sector of the economy in GDP in a nation the sum of feedbacks to a node coming from other nodes in the whole network F

<!-- b000137 | prose | pages [5] -->
q AQI value of a nation land area of nation S

<!-- b000138 | prose | pages [5] -->
distance between every two nations l

<!-- b000139 | furniture | pages [5] -->


<!-- b000140 | heading | pages [5] -->
2 Model

<!-- b000141 | prose | pages [5] -->
In order to fulfill the requirements of International Coalition of Modelers (ICM), the goal of our team seems to be very clear. The content of our paper is aiming at building a dynamic global air quality network model to show the health condition of Planet Earth by identifying local elements of this condition and appropriately connecting them to track relationship and attribute effect. The model we build needs to include the human element and has the function of predicting Earth’s health future states by a specific health measure.

<!-- b000142 | furniture | pages [5] -->


<!-- b000143 | heading | pages [5] -->
2.1 Generic Methodology

<!-- b000144 | prose | pages [5] -->
We model the dynamic global air quality network as a combination of local and global networks with interlinked architecture, which has high similarity with Internet.

<!-- b000145 | caption | pages [5] -->
Figure 3 shows the basic framework visually. The left part show the whole framework of

<!-- b000146 | prose | pages [5] -->
global network while the right part displays the details of a single local network. To make the methodology more understandably, we defined seven concepts below.

<!-- b000147 | furniture | pages [5] -->


<!-- b000148 | furniture | pages [6] -->
Team #21165

<!-- b000149 | furniture | pages [6] -->


<!-- b000150 | prose | pages [6] -->
i+2

<!-- b000151 | prose | pages [6] -->
...

<!-- b000152 | prose | pages [6] -->
Global Link

<!-- b000153 | prose | pages [6] -->
(i+1, i+2)

<!-- b000154 | prose | pages [6] -->
Global Link

<!-- b000155 | prose | pages [6] -->
(i, i+2)

<!-- b000156 | prose | pages [6] -->
i+1

<!-- b000157 | prose | pages [6] -->
Global Link

<!-- b000158 | prose | pages [6] -->
(i, ...)

<!-- b000159 | prose | pages [6] -->
Global Link

<!-- b000160 | prose | pages [6] -->
(i, i+1)

<!-- b000161 | prose | pages [6] -->
Global Type

<!-- b000162 | prose | pages [6] -->
...

<!-- b000163 | prose | pages [6] -->
Output

<!-- b000164 | prose | pages [6] -->
... 1 2 n

<!-- b000165 | prose | pages [6] -->
i

<!-- b000166 | prose | pages [6] -->
...

<!-- b000167 | prose | pages [6] -->
Inputs

<!-- b000168 | prose | pages [6] -->
Global Nodes

<!-- b000169 | prose | pages [6] -->
Local Nodes

<!-- b000170 | furniture | pages [6] -->


<!-- b000171 | furniture | pages [6] -->


<!-- b000172 | furniture | pages [6] -->
Page 5 of 18

<!-- b000173 | prose | pages [6] -->
... ...

<!-- b000174 | prose | pages [6] -->
Local Type

<!-- b000175 | prose | pages [6] -->
Output

<!-- b000176 | prose | pages [6] -->
Local View

<!-- b000177 | prose | pages [6] -->
Local Network Local Network n

<!-- b000178 | prose | pages [6] -->
Node

<!-- b000179 | furniture | pages [6] -->


<!-- b000180 | caption | pages [6] -->
Figure 3 The basic framework

<!-- b000181 | furniture | pages [6] -->


<!-- b000182 | prose | pages [6] -->
 Local Network: Neural network

<!-- b000183 | prose | pages [6] -->
Having considered the fact that the data available might be very limited, we decide to use neural network as local part of the whole system. Unlike the traditional mathematical methods such as regression or time series prediction, neural network is famous for its unique learning ability, and thus is able to extract the approximate feature of the data from a relatively small sample.

<!-- b000184 | prose | pages [6] -->
In the machine learning theory, the neural network method itself is further divided into several different categories. To reduce complexity, we choose the most basic BP model. Because a multiple output network will reduce the accuracy of the model (since the input edges are shared), each of our local network is dedicated to only one output.

<!-- b000185 | prose | pages [6] -->
The BP model, however, has a major setback of slow convergence. Noting that we may have myriad of such networks in a single system, a very long training time is surely not ideal. Hence we introduce Particle Swarm Optimization (PSO) to help the neural network define best weights of linking edges. PSO is a newly emerging optimization algorithm which optimizes the value of function by simulating multiple particles that travels freely in the solution space. Each particle communicates with others to decide where to go for the next iteration. Because the number of such particles can be large, the optimal value can be quickly found. At the same time, the goal function rarely gets stuck in a local optimal value.  Local Node: A single neuron

<!-- b000186 | prose | pages [6] -->
i) Input layer The neurons on the input layer are divided into two categories.  Neurons of the first category were dedicated to factors ranging from human element, biological system to environmental system that affect the air quality. In addition, another category of neurons is needed to be assigned to the

<!-- b000187 | furniture | pages [7] -->
Team #21165

<!-- b000188 | furniture | pages [7] -->


<!-- b000189 | furniture | pages [7] -->


<!-- b000190 | furniture | pages [7] -->
Page 6 of 18

<!-- b000191 | prose | pages [7] -->
sum of the feedback from other Global Nodes. For neurons in this category, their initial values are zero.

<!-- b000192 | prose | pages [7] -->
ii) Output layer The neuron on the output layer of each neural network represents one of the factors appeared on the input layer. The output of each neural network can be divided into two types: local and global. Local Type Output means that the factors do not have communication with other Global Nodes, they are calculated without feedbacks. While Global Type Output has communication with other Global Nodes.

<!-- b000193 | furniture | pages [7] -->


<!-- b000194 | prose | pages [7] -->
 Global Node: Node made up by n Local Networks

<!-- b000195 | prose | pages [7] -->
Node at this level may has more than one output, but each neural network should be dedicated to only one output, as we have just mentioned. Hence n Local Networks are needed to construct a Global Node.

<!-- b000196 | furniture | pages [7] -->


<!-- b000197 | prose | pages [7] -->
 Global Link: A distance value between nodes and a link function

<!-- b000198 | prose | pages [7] -->
The distance measures the tightness of relationship between nodes and is not confined to physical distance. The link function is a map from Global Type Output to the feedback input, which forms the communication between nodes.

<!-- b000199 | furniture | pages [7] -->


<!-- b000200 | prose | pages [7] -->
 Global network: A network consists of Global Nodes which connect and communicate with

<!-- b000201 | prose | pages [7] -->
each other by Global Link

<!-- b000202 | furniture | pages [7] -->


<!-- b000203 | prose | pages [7] -->
One thing should be noted that the Global Network we devised is an autonomous system. Here the term autonomous means that the output and the feedback of the j th year is taken as the input of the (j+1) th year. To fully understand the mechanism, consider the following example: suppose we nx ]. Using a one-step forecast, we are able to generate local ..., x x , , have initial input vector xj=[ 1 2 type output yi1 and global type output yi2, thus further generating the feedback input Fi. We then combine vectors yi1 and Fi to form a new input vector of xj+1 and start the forecasting process once  j  to j n 1 again. Henceforth, in this way, we can get all the results from year (for any n) using only a group of variables defining initial condition of the system. This property is important because it theoretically enables us to make an indefinitely long forecast of the future trend with very small amount of data.

<!-- b000204 | prose | pages [7] -->
We have finished the structural introduction of our methodology. At this point we are able to give the general expression of earth’s health measure from the perspective of air quality. Suppose in a certain year there is only one output (e.g. AQI value) that directly influences the final value of ky , thus forming a weight health measure. For each global node k, we assign a weight to this output

<!-- b000205 | prose | pages [7] -->
w ]. We calculate the weighted mean of this output as follows (suppose w w , ,..., vector of W= [ 1 2 n there are n nodes in total):

<!-- b000206 | prose | pages [7] -->
n

<!-- b000207 | prose | pages [7] -->


<!-- b000208 | prose | pages [7] -->
k

<!-- b000209 | prose | pages [7] -->
H

<!-- b000210 | prose | pages [7] -->


<!-- b000211 | prose | pages [7] -->
w y

<!-- b000212 | prose | pages [7] -->
k k

<!-- b000213 | prose | pages [7] -->
 

<!-- b000214 | prose | pages [7] -->
1 1

<!-- b000215 | prose | pages [7] -->
.

<!-- b000216 | prose | pages [7] -->
n n

<!-- b000217 | prose | pages [7] -->


<!-- b000218 | prose | pages [7] -->
w

<!-- b000219 | prose | pages [7] -->
k

<!-- b000220 | prose | pages [7] -->
 

<!-- b000221 | prose | pages [7] -->
k k

<!-- b000222 | prose | pages [7] -->
1

<!-- b000223 | prose | pages [7] -->
This is the expression of earth’s health measure. As for defining the tipping points, it is discussed in [5] that tipping points are often hard to define, but some features before the tipping points may help distinguish the state change, such as rising risk of nonlinear changes and fluctuations. Hence, we do not define generic judging criteria of tipping points here. From our perspective, it might be wiser that each case is specifically analyzed according to the feature it shows.

<!-- b000224 | furniture | pages [7] -->


<!-- b000225 | furniture | pages [8] -->
Team #21165

<!-- b000226 | furniture | pages [8] -->


<!-- b000227 | heading | pages [8] -->
2.2 Basic Model

<!-- b000228 | prose | pages [8] -->
2.2.1 Input and Output of Local Network

<!-- b000229 | furniture | pages [8] -->


<!-- b000230 | furniture | pages [8] -->
Page 7 of 18

<!-- b000231 | prose | pages [8] -->
Due to the limitation of the data that could be collected, we set the primary influence factors of air quality into three aspects of inputs and measured by rate to unify outputs because of the different nation scale.

<!-- b000232 | prose | pages [8] -->
Table 3 Input Output Initial Name and Notation

<!-- b000233 | prose | pages [8] -->
Name and Notation Type

<!-- b000234 | prose | pages [8] -->
Value

<!-- b000235 | prose | pages [8] -->
population density of a nation d d

<!-- b000236 | prose | pages [8] -->
forest coverage rate of a nation r 0r

<!-- b000237 | prose | pages [8] -->
the proportion of secondary sector of the

<!-- b000238 | prose | pages [8] -->
0p

<!-- b000239 | prose | pages [8] -->
economy in GDP of a nation  p

<!-- b000240 | prose | pages [8] -->
The sum of feedback to a Global Node coming from other Global Nodes in the whole Global Network  F

<!-- b000241 | furniture | pages [8] -->


<!-- b000242 | prose | pages [8] -->
2.2.2 Global Network Aspect

<!-- b000243 | prose | pages [8] -->
Local Type

<!-- b000244 | prose | pages [8] -->
population density d 0 0

<!-- b000245 | furniture | pages [8] -->


<!-- b000246 | prose | pages [8] -->
forest coverage rate r

<!-- b000247 | prose | pages [8] -->
Local Type

<!-- b000248 | furniture | pages [8] -->


<!-- b000249 | prose | pages [8] -->
the proportion of secondary

<!-- b000250 | furniture | pages [8] -->


<!-- b000251 | prose | pages [8] -->
sector of the economy in

<!-- b000252 | prose | pages [8] -->
Local Type

<!-- b000253 | prose | pages [8] -->
GDP  p

<!-- b000254 | furniture | pages [8] -->


<!-- b000255 | furniture | pages [8] -->


<!-- b000256 | furniture | pages [8] -->


<!-- b000257 | furniture | pages [8] -->


<!-- b000258 | prose | pages [8] -->
0 0

<!-- b000259 | prose | pages [8] -->
Global Type

<!-- b000260 | prose | pages [8] -->
Air Quality Index (AQI)  q

<!-- b000261 | furniture | pages [8] -->


<!-- b000262 | prose | pages [8] -->
 Global Nodes : made up by four Local Networks  Global Link:

<!-- b000263 | prose | pages [8] -->
The sum of feedbacks to a Global Node coming in the whole Global Network is defined by:

<!-- b000264 | prose | pages [8] -->
n

<!-- b000265 | prose | pages [8] -->
 F f q

<!-- b000266 | prose | pages [8] -->
( ,

<!-- b000267 | prose | pages [8] -->
S l

<!-- b000268 | prose | pages [8] -->
, )

<!-- b000269 | prose | pages [8] -->
( i: i th Global Node,  j: j th year)  j i j

<!-- b000270 | prose | pages [8] -->
, 1

<!-- b000271 | prose | pages [8] -->
i i  i

<!-- b000272 | prose | pages [8] -->
1

<!-- b000273 | prose | pages [8] -->
While the feedback from a single Global Node is:

<!-- b000274 | prose | pages [8] -->


<!-- b000275 | prose | pages [8] -->
f q S l

<!-- b000276 | prose | pages [8] -->
( , , )

<!-- b000277 | heading | pages [8] -->
2.3 Advanced Model

<!-- b000278 | prose | pages [8] -->
l l

<!-- b000279 | prose | pages [8] -->
 

<!-- b000280 | prose | pages [8] -->
1 280

<!-- b000281 | prose | pages [8] -->
 

<!-- b000282 | prose | pages [8] -->
q e S

<!-- b000283 | prose | pages [8] -->
55

<!-- b000284 | furniture | pages [8] -->


<!-- b000285 | prose | pages [8] -->
6 10

<!-- b000286 | furniture | pages [8] -->


<!-- b000287 | prose | pages [8] -->
The limitation of the basic model is mainly because of the data information. Therefore if the source of the different aspects’ factors that affect the air quality is comprehensive, with the generic methodology, a more advanced model could be implemented.

<!-- b000288 | furniture | pages [8] -->


<!-- b000289 | prose | pages [8] -->
2.3.1 Input and Output of Local Network Despite the existing factors mentioned in the basic model, the two aspects of factors below can be taken into consideration: air pollution created by nature including volcanic eruption, dust cloud etc.; other human activity, such as the amount of mobile vehicle, resource consumption, overgrazing and a very important one: policy.

<!-- b000290 | furniture | pages [8] -->


<!-- b000291 | prose | pages [8] -->
2.3.2 Global Network Aspect  Global Node

<!-- b000292 | prose | pages [8] -->
We choose the pollution source as the Global Node. These Global Nodes form a three- dimensional model which x-axis and y-axis represent longitude and latitude，while z-axis is

<!-- b000293 | furniture | pages [9] -->
Team #21165

<!-- b000294 | furniture | pages [9] -->


<!-- b000295 | prose | pages [9] -->
altitude.

<!-- b000296 | furniture | pages [9] -->


<!-- b000297 | prose | pages [9] -->
 Global Link：

<!-- b000298 | furniture | pages [9] -->


<!-- b000299 | furniture | pages [9] -->
Page 8 of 18

<!-- b000300 | prose | pages [9] -->
We use equation in the Gaussian Dispersion Model to calculate the feedback [9].

<!-- b000301 | prose | pages [9] -->
Q  C x y z

<!-- b000302 | prose | pages [9] -->
( , , ) exp(

<!-- b000303 | prose | pages [9] -->
  

<!-- b000304 | prose | pages [9] -->
2

<!-- b000305 | prose | pages [9] -->
u

<!-- b000306 | prose | pages [9] -->
y z

<!-- b000307 | furniture | pages [9] -->


<!-- b000308 | prose | pages [9] -->
C   Pollutant concentration Q   Pollutant emission per unit time

<!-- b000309 | prose | pages [9] -->
   Lateral diffusion coefficient: a function of x y

<!-- b000310 | prose | pages [9] -->
   Vertical diffusion coefficient: a function of x z

<!-- b000311 | furniture | pages [9] -->


<!-- b000312 | heading | pages [9] -->
3 Verification

<!-- b000313 | heading | pages [9] -->
3.1 Overview

<!-- b000314 | prose | pages [9] -->


<!-- b000315 | prose | pages [9] -->
2 2

<!-- b000316 | prose | pages [9] -->
y

<!-- b000317 | prose | pages [9] -->
(

<!-- b000318 | prose | pages [9] -->
z

<!-- b000319 | prose | pages [9] -->
500)

<!-- b000320 | prose | pages [9] -->
 

<!-- b000321 | furniture | pages [9] -->


<!-- b000322 | prose | pages [9] -->
){exp[ ]}

<!-- b000323 | prose | pages [9] -->
 

<!-- b000324 | prose | pages [9] -->
2 2 2 2 y z

<!-- b000325 | prose | pages [9] -->
u Average wind speed x The distance to any node downwind

<!-- b000326 | prose | pages [9] -->
y The distance to any node at right-angle

<!-- b000327 | prose | pages [9] -->
horizontal direction

<!-- b000328 | prose | pages [9] -->
z  The average altitude

<!-- b000329 | prose | pages [9] -->
In this section we seek to verify our model using some datasets that can be retrieved at present. As the problem requirement has mentioned, the global data which are needed to verify such complex network are often difficult to assess. For this very reason, we do not verify advanced model in this paper. All the model verifications discussed below are concerned with the basic model.

<!-- b000330 | prose | pages [9] -->
Although we are also not able to find a continuous air pollution record that has satisfactory time span and nation coverage, we managed to get world pollutant emission statistics (by nation) from the website of Emission Database for Global Atmospheric Research (EDGAR). This dataset contains data over a 39-year time span (1970-2008) from over 100 nations (After deleting some nations with too little data, the final dataset we get contains 115 nations).  Since the emission rate and AQI value is highly correlated, we estimate the pollution rate measured by AQI using the following formula:

<!-- b000331 | furniture | pages [9] -->


<!-- b000332 | furniture | pages [9] -->


<!-- b000333 | prose | pages [9] -->
(        )       .

<!-- b000334 | furniture | pages [9] -->


<!-- b000335 | prose | pages [9] -->
Where   and    are defined as follows:

<!-- b000336 | furniture | pages [9] -->


<!-- b000337 | furniture | pages [9] -->


<!-- b000338 | furniture | pages [9] -->


<!-- b000339 | furniture | pages [9] -->


<!-- b000340 | furniture | pages [9] -->


<!-- b000341 | furniture | pages [9] -->


<!-- b000342 | furniture | pages [9] -->


<!-- b000343 | furniture | pages [9] -->


<!-- b000344 | furniture | pages [9] -->


<!-- b000345 | furniture | pages [9] -->


<!-- b000346 | prose | pages [9] -->
In this category of formulas, E, S denotes the average emission rate per m2 and area by country, respectively.   and other variables in the second formula can be determined using a pair of datasets containing emission rate and AQI from any single year. In this paper we used data of 2008 offered by World Bank to define  . Comparison of our estimate with some small datasets from other sources indicates that such estimation is reasonable.

<!-- b000347 | prose | pages [9] -->
For the three other training statistics, namely the population density, the forest coverage rate and the proportion of secondary sector of the economy in GDP of a nation, direct data access is provided by World Bank. The link to all the data we use can be found in reference section.

<!-- b000348 | prose | pages [9] -->
As a basis of the verification section, we define the following 2 forecast methods:  Stepwise forecast: after getting the result of i th year, input data of i th year from the dataset to

<!-- b000349 | prose | pages [9] -->
get result of (i+1) th year.

<!-- b000350 | furniture | pages [10] -->
Team #21165

<!-- b000351 | furniture | pages [10] -->


<!-- b000352 | furniture | pages [10] -->


<!-- b000353 | furniture | pages [10] -->
Page 9 of 18

<!-- b000354 | prose | pages [10] -->
 Autonomous forecast: trigger the system using the data of the first year, then make the system

<!-- b000355 | prose | pages [10] -->
run autonomously to forecast the future results. By “autonomously” we mean that the result of i th year is taken as the input to get the result of (i+1) th year, as has been stated in generic methodology. Because only one sample of data is offered when performing autonomous forecast, the result we get from the model completely excludes exterior influences other than the input factors (e.g. policy). Plus, the error may accumulate over time and lead to some fluctuation in the prediction, but as we will see later in this paper, the trend can still be clearly judged from the resulting plot.

<!-- b000356 | furniture | pages [10] -->


<!-- b000357 | prose | pages [10] -->
Before we start to introduce the verification we make, it is worthy to be mentioned that all of our verifications are performed on local scale. The reason that we do not offer a statistical global verification is as follows:

<!-- b000358 | prose | pages [10] -->
Judging from the current earth condition, a decisive state switch may not happen in 100 years  or even longer time from the latest time point of our data. Due to the limited sample we have in hand and the error accumulation property we have just mentioned, it does not make any sense to make a forecast of that length. On the contrary, local state changes often happens in a more recent time, and samples are available to provide reliability assess of our forecast. The reason that our model are able to reflect global changes is that nations, denoted by global  nodes in the model, are interconnected by global feedback links so that they can interact with each other. Hence, global tipping points are in essentially accumulation results of local state changes. If the local state changes can be properly forecasted, it is highly possible that global tipping point is only a matter of quantity. The features indicating coming tipping points or state changes are similar between local or  global scale. So a model that can identify such features locally is also able to identify them globally.

<!-- b000359 | furniture | pages [10] -->


<!-- b000360 | prose | pages [10] -->
For the three reasons above, we consider it equivalent to make local and global verification on this model.

<!-- b000361 | furniture | pages [10] -->


<!-- b000362 | heading | pages [10] -->
3.2 Fit verification

<!-- b000363 | prose | pages [10] -->
We first verify that the parameters we set to train the local neural networks (e.g. learning rate, particle swarm size and hidden layer node numbers) do not make our model over-fitted. To achieve this goal, we train the neural with data of the first 30 years, and then we use autonomous forecast to generate results of the rest years. If these results differ greatly with the actual dataset, then we say this model is over-fitted and is not competent to make prediction of the future.

<!-- b000364 | prose | pages [10] -->
130

<!-- b000365 | prose | pages [10] -->
120

<!-- b000366 | prose | pages [10] -->
110

<!-- b000367 | prose | pages [10] -->
100

<!-- b000368 | prose | pages [10] -->
90

<!-- b000369 | prose | pages [10] -->
pollution/AQI

<!-- b000370 | prose | pages [10] -->
80

<!-- b000371 | prose | pages [10] -->
70

<!-- b000372 | prose | pages [10] -->
60

<!-- b000373 | prose | pages [10] -->
50

<!-- b000374 | prose | pages [10] -->
40

<!-- b000375 | prose | pages [10] -->
30

<!-- b000376 | furniture | pages [10] -->


<!-- b000377 | prose | pages [10] -->
1970 1975 1980 1985 1990

<!-- b000378 | prose | pages [10] -->
time/year

<!-- b000379 | furniture | pages [10] -->


<!-- b000380 | prose | pages [10] -->
forecast value actual value

<!-- b000381 | prose | pages [10] -->
1995 2000 2005 2010

<!-- b000382 | furniture | pages [10] -->


<!-- b000383 | caption | pages [10] -->
Figure 4 The result of stepwise forecast: Belgium

<!-- b000384 | furniture | pages [11] -->
Team #21165

<!-- b000385 | furniture | pages [11] -->


<!-- b000386 | furniture | pages [11] -->


<!-- b000387 | furniture | pages [11] -->
Page 10 of 18

<!-- b000388 | prose | pages [11] -->
Figures 4 contains an example of the results and corresponding datasets. From the figure we can see that the prediction approximately follows the curve, although some noise does exist. Considering that the networks we are trying to verify are only trained with 30 samples, such a result can be judged as satisfactory. Hence, we determine that both the training process and parameters are proper. In the following sections, we test the prediction ability and several other more advanced functions of this model.

<!-- b000389 | furniture | pages [11] -->


<!-- b000390 | heading | pages [11] -->
3.3 Identifying critical nodes

<!-- b000391 | prose | pages [11] -->
In our model, the feedback input is determined by other nations’ global type outputs. Reversely, the more critical a node is, the more “feedback” it will output to other topologically-adjacent nations. Like what we have done in basic model, the influence degree of a single node can be defined as follows:

<!-- b000392 | prose | pages [11] -->
n

<!-- b000393 | prose | pages [11] -->
 (i: i th Global Node,  j: j th year) G g q

<!-- b000394 | prose | pages [11] -->
( ,

<!-- b000395 | prose | pages [11] -->
S l

<!-- b000396 | prose | pages [11] -->
, )

<!-- b000397 | prose | pages [11] -->
 j i j

<!-- b000398 | prose | pages [11] -->
, 1

<!-- b000399 | prose | pages [11] -->
i i  i

<!-- b000400 | prose | pages [11] -->
1

<!-- b000401 | prose | pages [11] -->
Note that the global node here is “destination global node”, that is, the destination of the feedback, while the global node in what we have defined before is “source global node”.

<!-- b000402 | prose | pages [11] -->
Ideally, the function g (q, S, l) can be set the same as f (q, S, l). But we have noticed that f (q, S, l) stresses more on the local impact of a pollutant source, while people may want to find a critical node that has more “potential” to impose a larger impact to the whole earth. From this perspective, we improvise a new function that meets this need. The newly defined g (q, S, l) is:

<!-- b000403 | prose | pages [11] -->
q

<!-- b000404 | prose | pages [11] -->
( 1000

<!-- b000405 | prose | pages [11] -->


<!-- b000406 | prose | pages [11] -->
g q S l

<!-- b000407 | prose | pages [11] -->
( , , )

<!-- b000408 | prose | pages [11] -->
l S

<!-- b000409 | prose | pages [11] -->
  

<!-- b000410 | prose | pages [11] -->
1.2 1.2 2 ) )

<!-- b000411 | prose | pages [11] -->
e

<!-- b000412 | prose | pages [11] -->
( ) 1000 10000

<!-- b000413 | prose | pages [11] -->
.

<!-- b000414 | prose | pages [11] -->
100

<!-- b000415 | prose | pages [11] -->
With this function, we are able to calculate the influence degree of the function. We use several nations among the most important ones to show our results. From Figure 5, it can be found out that this measure of nodal influence correctly shows the worldwide difference between nations while also avoid over-exaggerating them.

<!-- b000416 | furniture | pages [11] -->


<!-- b000417 | prose | pages [11] -->
600

<!-- b000418 | prose | pages [11] -->
500

<!-- b000419 | prose | pages [11] -->
400

<!-- b000420 | prose | pages [11] -->
300

<!-- b000421 | prose | pages [11] -->
200

<!-- b000422 | prose | pages [11] -->
100

<!-- b000423 | prose | pages [11] -->
0

<!-- b000424 | furniture | pages [11] -->


<!-- b000425 | caption | pages [11] -->
Figure 5 Identifying the critical nodes

<!-- b000426 | furniture | pages [11] -->


<!-- b000427 | heading | pages [11] -->
3.4 Sensitivity to a relationship change

<!-- b000428 | prose | pages [11] -->
We next move on to testify whether our model is able to react to relationship change. Usually, a system with more links between elements suffers more fluctuations, because under such a situation,

<!-- b000429 | furniture | pages [12] -->
Team #21165

<!-- b000430 | furniture | pages [12] -->


<!-- b000431 | furniture | pages [12] -->


<!-- b000432 | furniture | pages [12] -->
Page 11 of 18

<!-- b000433 | prose | pages [12] -->
the system is more likely to advance toward a dynamic balance. On the contrary, when some links or nodes are removed, the subsystem becomes relatively more constrained and is likely to enter a steady state.

<!-- b000434 | prose | pages [12] -->
160

<!-- b000435 | prose | pages [12] -->
140

<!-- b000436 | prose | pages [12] -->
120

<!-- b000437 | prose | pages [12] -->
pollution/AQI index

<!-- b000438 | prose | pages [12] -->
100

<!-- b000439 | prose | pages [12] -->
80

<!-- b000440 | prose | pages [12] -->
60

<!-- b000441 | prose | pages [12] -->
40

<!-- b000442 | prose | pages [12] -->
20

<!-- b000443 | prose | pages [12] -->
0

<!-- b000444 | furniture | pages [12] -->


<!-- b000445 | prose | pages [12] -->
1970 1975 1980 1985 1990 1995

<!-- b000446 | prose | pages [12] -->
time/year

<!-- b000447 | furniture | pages [12] -->


<!-- b000448 | prose | pages [12] -->
forecast value actual value

<!-- b000449 | prose | pages [12] -->
2000 2005 2010

<!-- b000450 | furniture | pages [12] -->


<!-- b000451 | prose | pages [12] -->
(a) With China

<!-- b000452 | prose | pages [12] -->
160

<!-- b000453 | prose | pages [12] -->
140

<!-- b000454 | prose | pages [12] -->
120

<!-- b000455 | prose | pages [12] -->
pollution/AQI index

<!-- b000456 | prose | pages [12] -->
100

<!-- b000457 | prose | pages [12] -->
80

<!-- b000458 | prose | pages [12] -->
60

<!-- b000459 | prose | pages [12] -->
40

<!-- b000460 | prose | pages [12] -->
20

<!-- b000461 | prose | pages [12] -->
0

<!-- b000462 | furniture | pages [12] -->


<!-- b000463 | prose | pages [12] -->
1970 1975 1980 1985 1990 1995

<!-- b000464 | prose | pages [12] -->
time/year

<!-- b000465 | furniture | pages [12] -->


<!-- b000466 | prose | pages [12] -->
forecast value actual value

<!-- b000467 | prose | pages [12] -->
2000 2005 2010

<!-- b000468 | furniture | pages [12] -->


<!-- b000469 | prose | pages [12] -->
(b) Without China

<!-- b000470 | furniture | pages [12] -->


<!-- b000471 | furniture | pages [12] -->


<!-- b000472 | caption | pages [12] -->
Figure 6 (a) (b) Sensitivity to a relationship change: removing or not removing China

<!-- b000473 | furniture | pages [12] -->


<!-- b000474 | prose | pages [12] -->
In order to show that our model is able to simulate such a change, we remove China from the network (a node of significant influence to its surroundings) and retrain the model in the same way we done before. We then perform an autonomous forecast from the year of 1985 on both models to see if the results generated differ. Contained in Figure 6 are two results we get respectively in a forecast on India, a geographically adjacent country of China. From these figures it’s obvious that the fluctuation of the forecast is much smaller after the node representing China is removed. From this comparison, we consider the model being able to reflect the changes in the relationships between the nodes.

<!-- b000475 | furniture | pages [13] -->
Team #21165

<!-- b000476 | furniture | pages [13] -->


<!-- b000477 | heading | pages [13] -->
3.5 Case Study

<!-- b000478 | furniture | pages [13] -->


<!-- b000479 | furniture | pages [13] -->
Page 12 of 18

<!-- b000480 | prose | pages [13] -->
In this part of the paper, we consider a more realistic situation in order to verify that our model is able to accomplish more complicated tasks: predicting state changes and tipping points, reflecting changes that may be brought in by the policies, and provide adequate warnings to decision makers. These functions are partially intertwined and are not suitable to be discussed separately. Hence, we use a case study to address the problem.

<!-- b000481 | prose | pages [13] -->
The last 50 years witness the move of manufacture industry centers from fortune-rich, developed countries to resource-rich, developing countries [10]. So does air pollutions.  This trend can be easily seen in Figure 7 (a) (b) below. Note that the darker the color, the more serious the pollution. To demonstrate that our model is able to show this trend, we pick two countries that are among the most typical ones in both categories: Japan and India.

<!-- b000482 | furniture | pages [13] -->


<!-- b000483 | prose | pages [13] -->
(a) 1970

<!-- b000484 | furniture | pages [13] -->


<!-- b000485 | prose | pages [13] -->
(b) 2008

<!-- b000486 | furniture | pages [13] -->


<!-- b000487 | furniture | pages [13] -->


<!-- b000488 | caption | pages [13] -->
Figure 7 (a) (b) The change of world pollution distribution

<!-- b000489 | furniture | pages [13] -->


<!-- b000490 | prose | pages [13] -->
In the period of rapid economic growth after World War II, environmental policies were downplayed by the Japanese government and industrial corporations; as a result, environmental pollution was widespread in the 1950s and 1960s [14]. In response to such situation, the government enacted a series of laws and bills to ameliorate the situation. Although great improvements were made in water pollution, obvious change in air quality does not take place. It was not until more strict legislations were enacted in1990s did the situation really began to change [12]. At present, Japan is considered one of the most eco-friendly nations, which also holds true from the perspective of air pollution.

<!-- b000491 | furniture | pages [14] -->
Team #21165

<!-- b000492 | furniture | pages [14] -->


<!-- b000493 | furniture | pages [14] -->


<!-- b000494 | furniture | pages [14] -->
Page 13 of 18

<!-- b000495 | prose | pages [14] -->
Before 1991, India is a nation which followed protectionist policies that were influenced by socialist economics, but an acute balance of payments crisis in 1991 forced the nation to liberalize its economy [13]. While transforming into one of the fastest-growing economy in the developing world, India has also suffered a significant growth in industrial, energy, transport, urban population since then. Up to 2013, air pollution has become a serious barrier in its social and economic development. Sukinda and Vapi are even elected as the 3rd and 4th most polluted cities in the world [11].

<!-- b000496 | caption | pages [14] -->
Figure 8 is the plot we get from an autonomous forecast by our model. The forecast starts from

<!-- b000497 | prose | pages [14] -->
the year of 1985, when the air condition in Japan is still poor.  From the figure, it can be seen that in the first 8 years, the pollution rate increases approximately the same as the actual value, but in 1993, a sudden bounce has taken place and the pollution rate has risen to a much higher value. This point, in our view, is the “tipping point” of Japan air condition. This is the exact time point where if no additional air pollution reduction measures were taken, a major state change will take place, and it will be irreversible.

<!-- b000498 | prose | pages [14] -->
160

<!-- b000499 | prose | pages [14] -->
140

<!-- b000500 | prose | pages [14] -->
120

<!-- b000501 | prose | pages [14] -->
pollution/AQI index

<!-- b000502 | prose | pages [14] -->
100

<!-- b000503 | prose | pages [14] -->
80

<!-- b000504 | prose | pages [14] -->
60

<!-- b000505 | prose | pages [14] -->
40

<!-- b000506 | prose | pages [14] -->
20

<!-- b000507 | prose | pages [14] -->
0

<!-- b000508 | furniture | pages [14] -->


<!-- b000509 | prose | pages [14] -->
1970 1975 1980 1985 1990 1995

<!-- b000510 | prose | pages [14] -->
time/year

<!-- b000511 | furniture | pages [14] -->


<!-- b000512 | prose | pages [14] -->
forecast value actual value

<!-- b000513 | prose | pages [14] -->
2000 2005 2010

<!-- b000514 | furniture | pages [14] -->


<!-- b000515 | caption | pages [14] -->
Figure 8 Case Study using an autonomous forecast: Japan

<!-- b000516 | furniture | pages [14] -->


<!-- b000517 | prose | pages [14] -->
We move on to examine the case of India. Figure 9 is the plot we get from an autonomous forecast by our model in which no condition has changed except the nation. From this plot, it can be concluded that if it is not the liberalism reform of its economy in 1991, its air pollution condition might remain in a relatively steady state where the average nationwide AQI would be about 50, like what it was in 1985. However, as the actual value curve indicates, the fact is that India’s pollution index value has reached about 150 by 2008, among the highest ones we have been able to seen in this dataset.

<!-- b000518 | prose | pages [14] -->
These two examples are typical in two aspects: social and functional.  The examples are socially-typical because these two nations have included what most countries in this world have undergone in the past 50 years: pollute-and-control, or polluting-while-developing. It is also obvious that most of the developing countries are experiencing what developed countries had experienced 40 years ago, and the warnings shown in Figure 8 indicates that the result might be very serious.  The examples are functionally-typical because the forecast we performed on these two nations have included almost all of the functions the requirements ask from us: state-change and tipping point prediction, warning providing and information to the decision makers.  The result has verified that the model is capable of these tasks and the results we get from them contain useful information that can be used for decision-making.

<!-- b000519 | furniture | pages [15] -->
Team #21165

<!-- b000520 | furniture | pages [15] -->


<!-- b000521 | prose | pages [15] -->
160

<!-- b000522 | prose | pages [15] -->
140

<!-- b000523 | prose | pages [15] -->
120

<!-- b000524 | prose | pages [15] -->
pollution/AQI index

<!-- b000525 | prose | pages [15] -->
100

<!-- b000526 | prose | pages [15] -->
80

<!-- b000527 | prose | pages [15] -->
60

<!-- b000528 | prose | pages [15] -->
40

<!-- b000529 | prose | pages [15] -->
20

<!-- b000530 | prose | pages [15] -->
0

<!-- b000531 | furniture | pages [15] -->


<!-- b000532 | prose | pages [15] -->
1970 1975 1980 1985 1990

<!-- b000533 | prose | pages [15] -->
time/year

<!-- b000534 | furniture | pages [15] -->


<!-- b000535 | furniture | pages [15] -->
Page 14 of 18

<!-- b000536 | furniture | pages [15] -->


<!-- b000537 | prose | pages [15] -->
forecast value actual value

<!-- b000538 | prose | pages [15] -->
1995 2000 2005 2010

<!-- b000539 | furniture | pages [15] -->


<!-- b000540 | caption | pages [15] -->
Figure 9 Case Study using an autonomous forecast: India

<!-- b000541 | prose | pages [15] -->
To further illustrate the effect our model can reflect about the policies and the way our model helps with the decision making, we include yet another example about the policy: Hungary. Hungary was under Soviet domination until the collapse of the Union in 1989. For this reason, the industry production suffered a major fall in early 1990s, which has partly contributed to the significant decrease of its air pollution. While restoring its economy, the newly established Hungarian Parliament enacted the first Nation Environment Program (NEP) in 1997. The program covers the period of 1997 to 2002 and enormously ameliorated the pollution condition in the past [15]

<!-- b000542 | caption | pages [15] -->
Figure 10 is the plot from the autonomous of our model (start from 1985). In this figure we

<!-- b000543 | prose | pages [15] -->
have discovered a similar forecast curve as in Figure 8. A state change point (tipping point) exists on 1991, where a bounce of AQI value brings the country to an irreversible change. But conversely, the actual curve goes all the way down and reached its lowest value of 10 (approx.) in the year of 2008.

<!-- b000544 | prose | pages [15] -->
200

<!-- b000545 | prose | pages [15] -->
180

<!-- b000546 | prose | pages [15] -->
160

<!-- b000547 | prose | pages [15] -->
140

<!-- b000548 | prose | pages [15] -->
pollution/AQI index

<!-- b000549 | prose | pages [15] -->
120

<!-- b000550 | prose | pages [15] -->
100

<!-- b000551 | prose | pages [15] -->
80

<!-- b000552 | prose | pages [15] -->
60

<!-- b000553 | prose | pages [15] -->
40

<!-- b000554 | prose | pages [15] -->
20

<!-- b000555 | prose | pages [15] -->
0

<!-- b000556 | furniture | pages [15] -->


<!-- b000557 | prose | pages [15] -->
1970 1975 1980 1985 1990

<!-- b000558 | prose | pages [15] -->
time/year

<!-- b000559 | furniture | pages [15] -->


<!-- b000560 | prose | pages [15] -->
forecast value actual value

<!-- b000561 | prose | pages [15] -->
1995 2000 2005 2010

<!-- b000562 | furniture | pages [15] -->


<!-- b000563 | caption | pages [15] -->
Figure 10 Case Study using an autonomous forecast: Hungary

<!-- b000564 | furniture | pages [16] -->
Team #21165

<!-- b000565 | furniture | pages [16] -->


<!-- b000566 | furniture | pages [16] -->


<!-- b000567 | furniture | pages [16] -->
Page 15 of 18

<!-- b000568 | prose | pages [16] -->
The history of Hungary and India resembles in certain respect. Both have undergone a liberalism reform in the economy and both have enjoyed significant boom in their economic achievement. But in the respect of air pollution control they are definitely different: the Indians have pushed themselves into the list of most air-polluted countries, while Hungarians are harmonizing their living environment at the same time. From the forecast of our model, the difference is clear, and, from our perspective, so are the optimal development decisions of the decision makers.

<!-- b000569 | furniture | pages [16] -->


<!-- b000570 | heading | pages [16] -->
4 Conclusion

<!-- b000571 | heading | pages [16] -->
4.1 Strength and Weakness

<!-- b000572 | heading | pages [16] -->
Strengths

<!-- b000573 | furniture | pages [16] -->


<!-- b000574 | prose | pages [16] -->
 Embracing the complexity of Earth’s interrelated systems

<!-- b000575 | prose | pages [16] -->
Although the development of our model is quite plain, it still manages to achieve satisfying flexibility. Such flexibility in setting input, output and the link make the whole model a complex interlinked system with multiple factors. In this way, the model can be devised into different scales and types to apply to various situations.

<!-- b000576 | furniture | pages [16] -->


<!-- b000577 | prose | pages [16] -->
 The complete functionality of  the model

<!-- b000578 | prose | pages [16] -->
The functions of the model include predicting and providing warnings about state changes, helping with policy-making, etc. Our model is also capable of identifying critical nodes and relationships. Such complete functionality results from the good structural designs and careful algorithm picking.

<!-- b000579 | furniture | pages [16] -->


<!-- b000580 | prose | pages [16] -->
 Autonomous forecast mechanism

<!-- b000581 | prose | pages [16] -->
Our model can perform an autonomous forecast with a set of initial data. The forecast can last a long enough time depending on the requests.

<!-- b000582 | furniture | pages [16] -->


<!-- b000583 | heading | pages [16] -->
Weaknesses

<!-- b000584 | furniture | pages [16] -->


<!-- b000585 | prose | pages [16] -->
 Relatively higher sensitivity

<!-- b000586 | prose | pages [16] -->
In our model, we only had 30 samples to train the neural network because of the lack of data. For the same reason, some important factors may not present.  Hence, the accuracy is affected and the result is probably more interfered by the small fluctuation of inputs.

<!-- b000587 | furniture | pages [16] -->


<!-- b000588 | prose | pages [16] -->
 Difficulty in finding a proper link function

<!-- b000589 | prose | pages [16] -->
When devising our model, we found that most of the scientific studies concerning network system links are constrained in relatively small model. Hence, these results may not suitable to be introduced into the global model.  And we infer that some other network with a huge scale may face the same difficulty as well.

<!-- b000590 | furniture | pages [16] -->


<!-- b000591 | prose | pages [16] -->
 Long training time spending on neural network

<!-- b000592 | prose | pages [16] -->
This is defined the structural feature of neural network.

<!-- b000593 | furniture | pages [16] -->


<!-- b000594 | heading | pages [16] -->
4.2 Extension

<!-- b000595 | prose | pages [16] -->
The dual-layer network design and the flexible setting of input, output and the link make the whole model a complex interlinked system with multiple factors. The lower level network performs prediction while the higher level network sets up the links. This kind of system matches the reality well and can be extended to some other aspects.

<!-- b000596 | furniture | pages [17] -->
Team #21165

<!-- b000597 | furniture | pages [17] -->


<!-- b000598 | furniture | pages [17] -->


<!-- b000599 | furniture | pages [17] -->
Page 16 of 18

<!-- b000600 | prose | pages [17] -->
For example, water quality can also be seen as a reflection of the Earth’s health. Changing the link and some of the inputs and outputs properly, with the autonomous mechanism, prediction can be made and the condition can be measured. In addition, our model can apply to some small ecosystems and biological system for the similarity of network structure. Moreover, we believe that the ubiquity of the model make it possible to help people make prediction in other domains.

<!-- b000601 | furniture | pages [17] -->


<!-- b000602 | furniture | pages [17] -->


<!-- b000603 | furniture | pages [17] -->


<!-- b000604 | furniture | pages [17] -->


<!-- b000605 | furniture | pages [17] -->


<!-- b000606 | furniture | pages [17] -->


<!-- b000607 | furniture | pages [17] -->


<!-- b000608 | furniture | pages [17] -->


<!-- b000609 | furniture | pages [17] -->


<!-- b000610 | furniture | pages [17] -->


<!-- b000611 | furniture | pages [17] -->


<!-- b000612 | furniture | pages [17] -->


<!-- b000613 | furniture | pages [17] -->


<!-- b000614 | furniture | pages [17] -->


<!-- b000615 | furniture | pages [17] -->


<!-- b000616 | furniture | pages [17] -->


<!-- b000617 | furniture | pages [17] -->


<!-- b000618 | furniture | pages [17] -->


<!-- b000619 | furniture | pages [17] -->


<!-- b000620 | furniture | pages [17] -->


<!-- b000621 | furniture | pages [17] -->


<!-- b000622 | furniture | pages [17] -->


<!-- b000623 | furniture | pages [17] -->


<!-- b000624 | furniture | pages [17] -->


<!-- b000625 | furniture | pages [17] -->


<!-- b000626 | furniture | pages [17] -->


<!-- b000627 | furniture | pages [17] -->


<!-- b000628 | furniture | pages [17] -->


<!-- b000629 | furniture | pages [17] -->


<!-- b000630 | furniture | pages [17] -->


<!-- b000631 | furniture | pages [17] -->


<!-- b000632 | furniture | pages [17] -->


<!-- b000633 | furniture | pages [17] -->


<!-- b000634 | furniture | pages [17] -->


<!-- b000635 | furniture | pages [17] -->


<!-- b000636 | furniture | pages [17] -->


<!-- b000637 | furniture | pages [17] -->


<!-- b000638 | furniture | pages [17] -->


<!-- b000639 | furniture | pages [17] -->


<!-- b000640 | furniture | pages [17] -->


<!-- b000641 | furniture | pages [17] -->


<!-- b000642 | furniture | pages [17] -->


<!-- b000643 | furniture | pages [17] -->


<!-- b000644 | furniture | pages [17] -->


<!-- b000645 | furniture | pages [17] -->


<!-- b000646 | furniture | pages [18] -->
Team #21165

<!-- b000647 | furniture | pages [18] -->


<!-- b000648 | furniture | pages [18] -->


<!-- b000649 | furniture | pages [18] -->
Page 17 of 18

<!-- b000650 | heading | pages [18] -->
References

<!-- b000651 | references | pages [18] -->
[1] Robert Watson and A. Hamid Zakri, 2005, UN Millennium Ecosystem Assessment Synthesis

<!-- b000652 | references | pages [18] -->
Report, United Nations Report (pp 16-30)

<!-- b000653 | references | pages [18] -->
[2] Will Steffen, Jacques Grinevald, Paul Crutzen and John McNeill, 2010, The Anthropocene:

<!-- b000654 | references | pages [18] -->
conceptual and historical perspectives, AMBIO 40, 739–761

<!-- b000655 | references | pages [18] -->
[3] Donella Meadows, Jorgen Randers, and Dennis Meadows, 2004, Limits to Growth: The 30-year

<!-- b000656 | references | pages [18] -->
update, (pp15)

<!-- b000657 | references | pages [18] -->
[4] McNeill, J. R. 2000 Something new under the sun: an environmental history of the twentieth

<!-- b000658 | references | pages [18] -->
century world. London, UK: W.W. Norton

<!-- b000659 | references | pages [18] -->
[5] Anthony D. Barnosky, Elizabeth A. Hadly, Jordi Bascompte, Eric L. Berlow, James H.

<!-- b000660 | references | pages [18] -->
Brown,Mikael Fortelius, Wayne M. Getz, John Harte, Alan Hastings, Pablo A. Marquet, Neo

<!-- b000661 | references | pages [18] -->
D.Martinez, Arne Mooers, Peter Roopnarine, Geerat Vermeij, John W. Williams, Rosemary

<!-- b000662 | references | pages [18] -->
Gillespie, Justin Kitzes, Charles Marshall, Nicholas Matzke, David P. Mindell, Eloy Revilla,

<!-- b000663 | references | pages [18] -->
Adam B. Smith. 2012, "Approaching a state shift in Earth's biosphere". Nature, 2012; 486

<!-- b000664 | references | pages [18] -->
(7401): 52 DOI: 10.1038/nature11018

<!-- b000665 | references | pages [18] -->
[6] McPherson, E. Gregory; Nowak, David J.; Rowntree, Rowan A. eds. 1994. Chicago's urban

<!-- b000666 | references | pages [18] -->
forest ecosystem: results of the Chicago Urban Forest Climate Project. Gen. Tech. Rep. NE-

<!-- b000667 | references | pages [18] -->
186.  Radnor, PA: U.S. Department of Agriculture, Forest Service, Northeastern Forest

<!-- b000668 | references | pages [18] -->
Experiment Station: 201 p

<!-- b000669 | references | pages [18] -->
[7] George E. Taylor, Dale W. Johnson and Christian P. Andersen, 1994, Air Pollution and

<!-- b000670 | references | pages [18] -->
Forest Ecosystem: A Regional to Global Perspective, Ecological Applications, Vol.4.No.4

<!-- b000671 | references | pages [18] -->
(Nov, 1994), (pp 662-689) Ecological Society of America

<!-- b000672 | references | pages [18] -->
[8] 2003, Air Quality Index A Guide to Air Quality and Your Health, Retrieved February 1st, 2013,

<!-- b000673 | references | pages [18] -->
from United States Environment Protect Agency

<!-- b000674 | references | pages [18] -->
Web site: http://www.epa.gov/airnow/aqi_cl.pdf

<!-- b000675 | references | pages [18] -->
[9] G. Grigoras, V. Cuculeanu, G. Ene, G. Mocioaca, A. Deneanu, 2012, Air Pollution Dispersion

<!-- b000676 | references | pages [18] -->
Modeling In A Polluted Industrial Area Of Complex Terrain From Romania ,Romania Reports

<!-- b000677 | references | pages [18] -->
in Physics, Vol. 64, No. 1, P. 173–186

<!-- b000678 | references | pages [18] -->
[10] Chun Gong, Zhenglin Wang, 2009, Master Matlab Optimized Calculation, pp 270-303, Beijing,

<!-- b000679 | references | pages [18] -->
Publishing House of Electronics Indstry(712108251)

<!-- b000680 | references | pages [18] -->
[11] Staff Writers,10 Most Polluted Cities In The World In 2013, Retrieved February 4th, 2013,

<!-- b000681 | references | pages [18] -->
form O,Pish, Posh!

<!-- b000682 | references | pages [18] -->
Web site: http://opishposh.com/most-polluted-cities-in-the-world/

<!-- b000683 | references | pages [18] -->
[12] Environment Issues, Japan Fact Sheet, Retrieved February 4th, 2013, from Web

<!-- b000684 | references | pages [18] -->
Japan

<!-- b000685 | references | pages [18] -->
Web site: http://web-japan.org/factsheet/en/pdf/e45_environment.pdf

<!-- b000686 | references | pages [18] -->
[13] India, Retrieved February 4th, 2013, from Wikipedia

<!-- b000687 | furniture | pages [18] -->


<!-- b000688 | references | pages [18] -->
Web site: http://en.wikipedia.org/wiki/India#Economy

<!-- b000689 | references | pages [18] -->
[14] Japan, Retrieved February 4th, 2013, from Wikipedia

<!-- b000690 | references | pages [18] -->
Web site:  http://en.wikipedia.org/wiki/Japan#Environment

<!-- b000691 | references | pages [18] -->
[15] Hungary Environment Report, Retrieved February 4th, 2013, form OECD

<!-- b000692 | references | pages [18] -->
Web site: http://www.oecd.org/env/

<!-- b000693 | furniture | pages [18] -->


<!-- b000694 | references | pages [18] -->
Other References

<!-- b000695 | references | pages [18] -->
[1] GHG (CO2, CH4, N2O, F-gases) emission time series 1990-2010 per region/country. Retrieved

<!-- b000696 | references | pages [18] -->
February 1st, 2013, from EDGAR-Emission Database for Global Atmospheric Research

<!-- b000697 | references | pages [18] -->
Web site: http://edgar.jrc.ec.europa.eu/overview.php?v=GHGts1990-2010

<!-- b000698 | references | pages [18] -->
[2] GDP (current US$), Retrieved February 1st, 2013, from The World Bank

<!-- b000699 | references | pages [18] -->
Web site: http://data.worldbank.org/indicator/NY.GDP.MKTP.CD?page=1

<!-- b000700 | furniture | pages [19] -->
Team #21165

<!-- b000701 | furniture | pages [19] -->


<!-- b000702 | furniture | pages [19] -->


<!-- b000703 | furniture | pages [19] -->
Page 18 of 18

<!-- b000704 | references | pages [19] -->
[3] Industry, value added (% of GDP), Retrieved February 1st, 2013, from The World Bank

<!-- b000705 | references | pages [19] -->
Web site: http://data.worldbank.org/indicator/NV.IND.TOTL.ZS

<!-- b000706 | references | pages [19] -->
[4] Population, total, Retrieved February 1st, 2013, from The World Bank

<!-- b000707 | references | pages [19] -->
Web site: http://data.worldbank.org/indicator/SP.POP.TOTL

<!-- b000708 | references | pages [19] -->
[5] Forest area (% of land area), Retrieved February 1st, 2013, from The World Bank

<!-- b000709 | references | pages [19] -->
Web site: http://data.worldbank.org/indicator/AG.LND.FRST.ZS

<!-- b000710 | references | pages [19] -->
[6] Countries, Capitals, Latitude and Longitude Table, Retrieved February 1st, 2013, from

<!-- b000711 | references | pages [19] -->
CSGNetWork

<!-- b000712 | furniture | pages [19] -->


<!-- b000713 | references | pages [19] -->
Web site: http://www.csgnetwork.com/llinfotable.html

<!-- b000714 | references | pages [19] -->
[7] Surface area Retrieved February 1st, 2013, from The World Bank

<!-- b000715 | references | pages [19] -->
Web site: http://search.worldbank.org/data?qterm=area&language=EN

<!-- b000716 | references | pages [19] -->
[8] Feng Shi, Xiaochuan Wang, Lei Yu, Yang Li, YanLiang Zhang, 2010, MATLAB neural

<!-- b000717 | references | pages [19] -->
networks: 30 case studies, pp21-35, Beijing: BUAA Press, 7-5124-0034-4
