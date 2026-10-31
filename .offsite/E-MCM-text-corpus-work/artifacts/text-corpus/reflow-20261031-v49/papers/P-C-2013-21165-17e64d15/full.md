# P-C-2013-21165-17e64d15

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only

<!-- b000003 | front_matter | pages [1] -->
21165

<!-- b000004 | front_matter | pages [1] -->
T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000005 | front_matter | pages [1] -->
C

<!-- b000006 | front_matter | pages [1] -->
2013 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000007 | front_matter | pages [1] -->
(Attach a copy of this page to your solution paper.)

<!-- b000008 | front_matter | pages [1] -->
Type a summary of your results on this page. Do not include

<!-- b000009 | front_matter | pages [1] -->
the name of your school, advisor, or team members on this page.

<!-- b000010 | heading | pages [1] -->
Abstract

<!-- b000011 | prose | pages [1] -->
In this paper, we build a model to measure the earth’s health in the aspect of air quality. We choose Air Quality Index (AQI) as the basis of health measure, while using a weighted average as the final expression. Our model takes the form of dual-layer network. Among the two layers, the local network is implemented using neural network optimized by Particle Swarm Optimization (PSO) algorithm, while the global network links the nodes with feedback links defined by certain propagation function. The model takes the output from the former year as the input of the following year, thus establishing an autonomous system by itself.

<!-- b000012 | prose | pages [1] -->
We then move on to verify the model. First we test the model’s fundamental network property from the perspective of fit, critical nodes, and missing relationships. As case studies, we applied our model to specific nations on a timespan of 1985-2008, namely Japan, India, and Hungary in hope to demonstrate that our model is able to generate prediction and warnings of state changes, and provide information for decision-makers. Our model has shown a completeness of functionality and impressive flexibility in these tests. Furthermore, we have been able to see that the prediction test of our model coincides fairly well with the fact.

<!-- b000013 | keywords | pages [1] -->
Key words: global, neural network, Air Quality Index, autonomous

<!-- b000014 | furniture | pages [2] -->
Team #21165

<!-- b000015 | furniture | pages [2] -->
Page 1 of 18

<!-- b000016 | contents | pages [2] -->
Link Our Breath: A Linked Neural Network

<!-- b000017 | contents | pages [2] -->
Approach to A Global Environment Model

<!-- b000018 | heading | pages [2] -->
Content

<!-- b000019 | contents | pages [2] -->
1 Introduction ....................................................................................................................................... 2

<!-- b000020 | contents | pages [2] -->
1.1 Background ............................................................................................................................ 2

<!-- b000021 | contents | pages [2] -->
1.2 An Overview of Air Quality................................................................................................... 2

<!-- b000022 | contents | pages [2] -->
1.2.1 Air Quality: A Reflection of Earth’s Health ............................................................... 2

<!-- b000023 | contents | pages [2] -->
1.2.2 Primary Influence Factors ........................................................................................... 3

<!-- b000024 | contents | pages [2] -->
1.3 Air Quality Index (AQI) ........................................................................................................ 3

<!-- b000025 | contents | pages [2] -->
1.4 Assumptions ........................................................................................................................... 4

<!-- b000026 | contents | pages [2] -->
1.5 Notations ................................................................................................................................ 4

<!-- b000027 | contents | pages [2] -->
2 Model ................................................................................................................................................ 4

<!-- b000028 | contents | pages [2] -->
2.1 Generic Methodology ............................................................................................................ 4

<!-- b000029 | contents | pages [2] -->
2.2 Basic Model ........................................................................................................................... 7

<!-- b000030 | contents | pages [2] -->
2.2.1 Input and Output of Local Network ............................................................................ 7

<!-- b000031 | contents | pages [2] -->
2.2.2 Global Network Aspect ............................................................................................... 7

<!-- b000032 | contents | pages [2] -->
2.3 Advanced Model .................................................................................................................... 7

<!-- b000033 | contents | pages [2] -->
2.3.1 Input and Output of Local Network ............................................................................ 7

<!-- b000034 | contents | pages [2] -->
2.3.2 Global Network Aspect ............................................................................................... 7

<!-- b000035 | contents | pages [2] -->
3 Verification ...................................................................................................................................... 8

<!-- b000036 | contents | pages [2] -->
3.1 Overview ................................................................................................................................ 8

<!-- b000037 | contents | pages [2] -->
3.2 Fit verification ........................................................................................................................ 9

<!-- b000038 | contents | pages [2] -->
3.3 Identifying critical nodes ..................................................................................................... 10

<!-- b000039 | contents | pages [2] -->
3.4 Sensitivity to a relationship change ..................................................................................... 10

<!-- b000040 | contents | pages [2] -->
3.5 Case Study............................................................................................................................ 12

<!-- b000041 | contents | pages [2] -->
4 Conclusion ...................................................................................................................................... 15

<!-- b000042 | contents | pages [2] -->
4.1 Strength and Weakness ........................................................................................................ 15

<!-- b000043 | contents | pages [2] -->
4.2 Extension .............................................................................................................................. 15

<!-- b000044 | contents | pages [2] -->
References .......................................................................................................................................... 17

<!-- b000045 | contents | pages [2] -->
Other References ................................................................................................................................ 17

<!-- b000046 | contents | pages [2] -->
List of Figures

<!-- b000047 | contents | pages [2] -->
Figure 1: World3 Computer Model Scenario 2: More Abundant Nonrenewable Resources [3] .............................. 2

<!-- b000048 | contents | pages [2] -->
Figure 2 (a) (b) The Increasing rates of change in human activity (c) Global scale changes in the Earth system as

<!-- b000049 | contents | pages [2] -->
a result of the dramatic increase in human activity: atmospheric N2O concentration [2] .............................. 3

<!-- b000050 | contents | pages [2] -->
Figure 3 The basic framework .................................................................................................................................. 5

<!-- b000051 | contents | pages [2] -->
Figure 4 The result of stepwise forecast: Belgium ................................................................................................... 9

<!-- b000052 | contents | pages [2] -->
Figure 5 Identifying the critical nodes .................................................................................................................... 10

<!-- b000053 | contents | pages [2] -->
Figure 6 (a) (b) Sensitivity to a relationship change: removing or not removing China ....................................... 11

<!-- b000054 | contents | pages [2] -->
Figure 7 (a) (b) The change of world pollution distribution .................................................................................. 12

<!-- b000055 | contents | pages [2] -->
Figure 8 Case Study using an autonomous forecast: Japan ................................................................................... 13

<!-- b000056 | contents | pages [2] -->
Figure 9 Case Study using an autonomous forecast: India .................................................................................... 14

<!-- b000057 | contents | pages [2] -->
Figure 10 Case Study using an autonomous forecast: Hungary ............................................................................ 14

<!-- b000058 | contents | pages [2] -->
List of Tables

<!-- b000059 | contents | pages [2] -->
Table 1 ............................................................................................................................................................. 3

<!-- b000060 | contents | pages [2] -->
Table 2 ............................................................................................................................................................. 4

<!-- b000061 | contents | pages [2] -->
Table 3 ............................................................................................................................................................. 7

<!-- b000062 | furniture | pages [3] -->
Team #21165

<!-- b000063 | furniture | pages [3] -->
Page 2 of 18

<!-- b000064 | heading | pages [3] -->
1 Introduction

<!-- b000065 | heading | pages [3] -->
1.1 Background

<!-- b000066 | prose | pages [3] -->
The growing stress on Earth’s environment and biological system are extremely apparent now. 15 out of 24 of the ecosystem services examined during the UN-based Millennium Ecosystem Assessment are being degraded or used unsustainably, including fresh water, capture fisheries, air and water purification and the regulation of regional and local climate, natural hazards, and pests [1].

<!-- b000067 | prose | pages [3] -->
Human activity is the main reason causing the significant changes of ecosystems which harm Earth health a lot. The largely growing demand of natural source over the past 50 years changed ecosystems more rapidly and extensively than in any comparable period of time in human history. [1] Moreover, excessive emission of the waste and pollutant leads to dramatic environmental changes as well.

<!-- b000068 | prose | pages [3] -->
Many global scale changes in ecosystems are displayed as exponential growth in the past half century. They can be large in magnitude and difficult or impossible to reverse once a threshold is crossed. As many of the trends appeared in the past century have continued, it is likely that the degradation of ecosystem services could grow worse in this century. In this way, global ecosystem may be approaching a planetary-scale ‘tipping point’. Therefore a prediction of potential state change of Earth’s health is needed. [2]

<!-- b000069 | caption | pages [3] -->
Figure 1: World3 Computer Model Scenario 2: More Abundant Nonrenewable Resources [3]

<!-- b000070 | caption | pages [3] -->
Figure 1 postulates that advances in resource extraction technologies are capable of postponing

<!-- b000071 | prose | pages [3] -->
the onset of increasing extraction costs [3]. Under such postulation, the ‘tipping point’ will occur in around 2050.

<!-- b000072 | heading | pages [3] -->
1.2 An Overview of Air Quality

<!-- b000073 | prose | pages [3] -->
1.2.1 Air Quality: A Reflection of Earth’s Health Air quality regulation is one of that fifteen ecosystem services which are being degraded and used unsustainably. Human need to pay much attention on air quality for not only it can reflect the condition of the Earth environment but also directly affect the health of many creatures. Moreover, it cannot be neglected that atmosphere activity helps the pollutant dispersion as well.

<!-- b000074 | prose | pages [3] -->
In most cases, climate changes and air quality are combined and many recent studies prefer to pay more attention on the greenhouse effect. However, both Great London Smog in 1952 and North China haze in 2013 show that heavy air pollution and particle pollution have lethal potential.

<!-- b000075 | furniture | pages [4] -->
Team #21165

<!-- b000076 | furniture | pages [4] -->
Page 3 of 18

<!-- b000077 | prose | pages [4] -->
1.2.2 Primary Influence Factors  Population explosion and rapid economic growth Between 1800 and 2000, the human population grew from about one billion to six billion, while energy use grew by about 40-fold and economic production by 50-fold [4]. In addition, the consumption of petroleum grew by a factor of 3.5 since 1960. The number of motor vehicles rose from only 40 million at the end of WWII to about 700 million by 1996, and continues to rise steadily [2]. Despite such rapid growth in population and economy, such a growth has also left a significant imprint on the environment, which is shown in the figures below.

<!-- b000078 | prose | pages [4] -->
(a) (b) (c)

<!-- b000079 | caption | pages [4] -->
Figure 2 (a) (b) The Increasing rates of change in human activity (c) Global scale changes in the Earth system

<!-- b000080 | prose | pages [4] -->
as a result of the dramatic increase in human activity: atmospheric N2O concentration [2]

<!-- b000081 | prose | pages [4] -->
 Forest coverage Forest coverage is a notable factor to air quality. On the one hand, gaseous and particle pollutants can be dry-deposited by trees through a mechanism named dry deposition, thus improving air quality [6]. On the other hand, many gaseous and particle pollutants, acting individually or in combination, affects forests particularly [7].

<!-- b000082 | heading | pages [4] -->
1.3 Air Quality Index (AQI)

<!-- b000083 | prose | pages [4] -->
Air Quality Index (AQI), developed by Environment Protection Agency (EPA) of United States, is aiming at helping people know what local air quality means to their health. This index is calculated by some major air pollutants which are regulated by the Clean Air Act, such as particle pollution and sulfur dioxide, etc. Table 1 [8] shows the six categories of AQI and their meanings, each of the categories is assigned by a specific color.

<!-- b000084 | prose | pages [4] -->
Table 1

<!-- b000085 | furniture | pages [5] -->
Team #21165

<!-- b000086 | furniture | pages [5] -->
Page 4 of 18

<!-- b000087 | heading | pages [5] -->
1.4 Assumptions

<!-- b000088 | prose | pages [5] -->
 The health measure of earth’s atmosphere can be assessed by Air Quality Index (AQI) We choose AQI as the earth health measure to associate the environmental and biological systems, more details of AQI can be found in the background part of the paper.

<!-- b000089 | prose | pages [5] -->
The following three assumptions only constrain the basic model.  While considering the air flow, the impact of topography is ignored.  One year is taken as the minimal time unit in the model.  We choose the nations around the world as the Global Nodes. The coordinates of the nodes are represented by the capitals’ longitude and latitude positions.

<!-- b000090 | prose | pages [5] -->
The assumptions above are due to the limitation of the data we have. In fact, the more data we collect, the more accurate result that the model will catch.

<!-- b000091 | heading | pages [5] -->
1.5 Notations

<!-- b000092 | prose | pages [5] -->
Table 2 Symbol Meaning the feedback function of a node coming from another node in the global f network g the influence degree function of a node derived from feedback function

<!-- b000093 | prose | pages [5] -->
population density of a nation d r forest coverage rate of a nation p proportion of secondary sector of the economy in GDP in a nation the sum of feedbacks to a node coming from other nodes in the whole network F

<!-- b000094 | prose | pages [5] -->
q AQI value of a nation land area of nation S distance between every two nations l

<!-- b000095 | heading | pages [5] -->
2 Model

<!-- b000096 | prose | pages [5] -->
In order to fulfill the requirements of International Coalition of Modelers (ICM), the goal of our team seems to be very clear. The content of our paper is aiming at building a dynamic global air quality network model to show the health condition of Planet Earth by identifying local elements of this condition and appropriately connecting them to track relationship and attribute effect. The model we build needs to include the human element and has the function of predicting Earth’s health future states by a specific health measure.

<!-- b000097 | heading | pages [5] -->
2.1 Generic Methodology

<!-- b000098 | prose | pages [5] -->
We model the dynamic global air quality network as a combination of local and global networks with interlinked architecture, which has high similarity with Internet.

<!-- b000099 | caption | pages [5] -->
Figure 3 shows the basic framework visually. The left part show the whole framework of

<!-- b000100 | prose | pages [5] -->
global network while the right part displays the details of a single local network. To make the methodology more understandably, we defined seven concepts below.

<!-- b000101 | furniture | pages [6] -->
Team #21165

<!-- b000102 | furniture | pages [6] -->
Page 5 of 18

<!-- b000103 | prose | pages [6] -->
i+2 ...

<!-- b000104 | prose | pages [6] -->
... Global Link (i+1, i+2) Global Link (i, i+2) i+1 Global Link (i, ...) Global Link Local Type (i, i+1) Output Global Type ... Local View Output

<!-- b000105 | prose | pages [6] -->
... 1 2 n

<!-- b000106 | prose | pages [6] -->
i

<!-- b000107 | prose | pages [6] -->
...

<!-- b000108 | prose | pages [6] -->
Inputs

<!-- b000109 | prose | pages [6] -->
Global Nodes

<!-- b000110 | prose | pages [6] -->
Local Nodes Local Network Local Network n Node

<!-- b000111 | caption | pages [6] -->
Figure 3 The basic framework

<!-- b000112 | prose | pages [6] -->
 Local Network: Neural network Having considered the fact that the data available might be very limited, we decide to use neural network as local part of the whole system. Unlike the traditional mathematical methods such as regression or time series prediction, neural network is famous for its unique learning ability, and thus is able to extract the approximate feature of the data from a relatively small sample.

<!-- b000113 | prose | pages [6] -->
In the machine learning theory, the neural network method itself is further divided into several different categories. To reduce complexity, we choose the most basic BP model. Because a multiple output network will reduce the accuracy of the model (since the input edges are shared), each of our local network is dedicated to only one output.

<!-- b000114 | prose | pages [6, 7] -->
The BP model, however, has a major setback of slow convergence. Noting that we may have myriad of such networks in a single system, a very long training time is surely not ideal. Hence we introduce Particle Swarm Optimization (PSO) to help the neural network define best weights of linking edges. PSO is a newly emerging optimization algorithm which optimizes the value of function by simulating multiple particles that travels freely in the solution space. Each particle communicates with others to decide where to go for the next iteration. Because the number of such particles can be large, the optimal value can be quickly found. At the same time, the goal function rarely gets stuck in a local optimal value.  Local Node: A single neuron i) Input layer The neurons on the input layer are divided into two categories.  Neurons of the first category were dedicated to factors ranging from human element, biological system to environmental system that affect the air quality. In addition, another category of neurons is needed to be assigned to the sum of the feedback from other Global Nodes. For neurons in this category, their initial values are zero.

<!-- b000115 | furniture | pages [7] -->
Team #21165

<!-- b000116 | furniture | pages [7] -->
Page 6 of 18

<!-- b000118 | prose | pages [7] -->
ii) Output layer The neuron on the output layer of each neural network represents one of the factors appeared on the input layer. The output of each neural network can be divided into two types: local and global. Local Type Output means that the factors do not have communication with other Global Nodes, they are calculated without feedbacks. While Global Type Output has communication with other Global Nodes.

<!-- b000119 | prose | pages [7] -->
 Global Node: Node made up by n Local Networks Node at this level may has more than one output, but each neural network should be dedicated to only one output, as we have just mentioned. Hence n Local Networks are needed to construct a Global Node.

<!-- b000120 | prose | pages [7] -->
 Global Link: A distance value between nodes and a link function The distance measures the tightness of relationship between nodes and is not confined to physical distance. The link function is a map from Global Type Output to the feedback input, which forms the communication between nodes.

<!-- b000121 | prose | pages [7] -->
 Global network: A network consists of Global Nodes which connect and communicate with each other by Global Link

<!-- b000122 | prose | pages [7] -->
One thing should be noted that the Global Network we devised is an autonomous system. Here the term autonomous means that the output and the feedback of the j th year is taken as the input of the (j+1) th year. To fully understand the mechanism, consider the following example: suppose we x x , , ..., nx ]. Using a one-step forecast, we are able to generate local have initial input vector xj=[ 1 2 type output yi1 and global type output yi2, thus further generating the feedback input Fi. We then combine vectors yi1 and Fi to form a new input vector of xj+1 and start the forecasting process once  j  to j n 1 again. Henceforth, in this way, we can get all the results from year (for any n) using only a group of variables defining initial condition of the system. This property is important because it theoretically enables us to make an indefinitely long forecast of the future trend with very small amount of data.

<!-- b000123 | prose | pages [7] -->
We have finished the structural introduction of our methodology. At this point we are able to give the general expression of earth’s health measure from the perspective of air quality. Suppose in a certain year there is only one output (e.g. AQI value) that directly influences the final value of ky , thus forming a weight health measure. For each global node k, we assign a weight to this output w w , ,..., w ]. We calculate the weighted mean of this output as follows (suppose vector of W= [ 1 2 n there are n nodes in total):

<!-- b000124 | prose | pages [7] -->
n   w y k k  k 1 H . n  w k  k 1 This is the expression of earth’s health measure. As for defining the tipping points, it is discussed in [5] that tipping points are often hard to define, but some features before the tipping points may help distinguish the state change, such as rising risk of nonlinear changes and fluctuations. Hence, we do not define generic judging criteria of tipping points here. From our perspective, it might be wiser that each case is specifically analyzed according to the feature it shows.

<!-- b000125 | furniture | pages [8] -->
Team #21165

<!-- b000126 | furniture | pages [8] -->
Page 7 of 18

<!-- b000127 | heading | pages [8] -->
2.2 Basic Model

<!-- b000128 | prose | pages [8] -->
2.2.1 Input and Output of Local Network Due to the limitation of the data that could be collected, we set the primary influence factors of air quality into three aspects of inputs and measured by rate to unify outputs because of the different nation scale.

<!-- b000129 | prose | pages [8] -->
Table 3 Input Output Name and Notation Initial Name and Notation Type Value Local Type population density of a nation d population density d d 0

<!-- b000130 | prose | pages [8] -->
forest coverage rate of a nation r forest coverage rate r Local Type 0r

<!-- b000131 | prose | pages [8] -->
the proportion of secondary sector of the the proportion of secondary 0p sector of the economy in Local Type economy in GDP of a nation  p GDP  p The sum of feedback to a Global Node coming from other Global Nodes in the 0 Global Type Air Quality Index (AQI)  q whole Global Network  F

<!-- b000132 | prose | pages [8] -->
2.2.2 Global Network Aspect  Global Nodes : made up by four Local Networks  Global Link:

<!-- b000133 | prose | pages [8] -->
The sum of feedbacks to a Global Node coming in the whole Global Network is defined by:

<!-- b000134 | prose | pages [8] -->
n  F f q ( , S l , ) ( i: i th Global Node,  j: j th year)  j i j , 1 i i  i 1 While the feedback from a single Global Node is:

<!-- b000135 | prose | pages [8] -->
l l   1 280   q e S 55  f q S l ( , , ) 6 10

<!-- b000136 | heading | pages [8] -->
2.3 Advanced Model

<!-- b000137 | prose | pages [8] -->
The limitation of the basic model is mainly because of the data information. Therefore if the source of the different aspects’ factors that affect the air quality is comprehensive, with the generic methodology, a more advanced model could be implemented.

<!-- b000138 | prose | pages [8] -->
2.3.1 Input and Output of Local Network Despite the existing factors mentioned in the basic model, the two aspects of factors below can be taken into consideration: air pollution created by nature including volcanic eruption, dust cloud etc.; other human activity, such as the amount of mobile vehicle, resource consumption, overgrazing and a very important one: policy.

<!-- b000139 | prose | pages [8, 9] -->
2.3.2 Global Network Aspect  Global Node We choose the pollution source as the Global Node. These Global Nodes form a three- dimensional model which x-axis and y-axis represent longitude and latitude，while z-axis is altitude.

<!-- b000140 | furniture | pages [9] -->
Team #21165

<!-- b000141 | furniture | pages [9] -->
Page 8 of 18

<!-- b000143 | prose | pages [9] -->
 Global Link： We use equation in the Gaussian Dispersion Model to calculate the feedback [9].

<!-- b000144 | prose | pages [9] -->
 2 2 Q y ( z 500)    C x y z ( , , ) exp( ){exp[ ]}      2 2 2 u 2 2 y z y z

<!-- b000145 | prose | pages [9] -->
C   Pollutant concentration u Average wind speed Q   Pollutant emission per unit time x The distance to any node downwind    Lateral diffusion coefficient: a function of x y The distance to any node at right-angle y horizontal direction    Vertical diffusion coefficient: a function of x z  The average altitude z

<!-- b000146 | heading | pages [9] -->
3 Verification

<!-- b000147 | heading | pages [9] -->
3.1 Overview

<!-- b000148 | prose | pages [9] -->
In this section we seek to verify our model using some datasets that can be retrieved at present. As the problem requirement has mentioned, the global data which are needed to verify such complex network are often difficult to assess. For this very reason, we do not verify advanced model in this paper. All the model verifications discussed below are concerned with the basic model.

<!-- b000149 | prose | pages [9] -->
Although we are also not able to find a continuous air pollution record that has satisfactory time span and nation coverage, we managed to get world pollutant emission statistics (by nation) from the website of Emission Database for Global Atmospheric Research (EDGAR). This dataset contains data over a 39-year time span (1970-2008) from over 100 nations (After deleting some nations with too little data, the final dataset we get contains 115 nations).  Since the emission rate and AQI value is highly correlated, we estimate the pollution rate measured by AQI using the following formula:

<!-- b000150 | prose | pages [9] -->
(        )       .

<!-- b000151 | prose | pages [9] -->
Where   and    are defined as follows:

<!-- b000152 | prose | pages [9] -->
In this category of formulas, E, S denotes the average emission rate per m2 and area by country, respectively.   and other variables in the second formula can be determined using a pair of datasets containing emission rate and AQI from any single year. In this paper we used data of 2008 offered by World Bank to define  . Comparison of our estimate with some small datasets from other sources indicates that such estimation is reasonable.

<!-- b000153 | prose | pages [9] -->
For the three other training statistics, namely the population density, the forest coverage rate and the proportion of secondary sector of the economy in GDP of a nation, direct data access is provided by World Bank. The link to all the data we use can be found in reference section.

<!-- b000154 | prose | pages [9] -->
As a basis of the verification section, we define the following 2 forecast methods:  Stepwise forecast: after getting the result of i th year, input data of i th year from the dataset to get result of (i+1) th year.

<!-- b000155 | furniture | pages [10] -->
Team #21165

<!-- b000156 | furniture | pages [10] -->
Page 9 of 18

<!-- b000157 | prose | pages [10] -->
 Autonomous forecast: trigger the system using the data of the first year, then make the system run autonomously to forecast the future results. By “autonomously” we mean that the result of i th year is taken as the input to get the result of (i+1) th year, as has been stated in generic methodology. Because only one sample of data is offered when performing autonomous forecast, the result we get from the model completely excludes exterior influences other than the input factors (e.g. policy). Plus, the error may accumulate over time and lead to some fluctuation in the prediction, but as we will see later in this paper, the trend can still be clearly judged from the resulting plot.

<!-- b000158 | prose | pages [10] -->
Before we start to introduce the verification we make, it is worthy to be mentioned that all of our verifications are performed on local scale. The reason that we do not offer a statistical global verification is as follows:

<!-- b000159 | prose | pages [10] -->
Judging from the current earth condition, a decisive state switch may not happen in 100 years  or even longer time from the latest time point of our data. Due to the limited sample we have in hand and the error accumulation property we have just mentioned, it does not make any sense to make a forecast of that length. On the contrary, local state changes often happens in a more recent time, and samples are available to provide reliability assess of our forecast.

<!-- b000160 | prose | pages [10] -->
The reason that our model are able to reflect global changes is that nations, denoted by global  nodes in the model, are interconnected by global feedback links so that they can interact with each other. Hence, global tipping points are in essentially accumulation results of local state changes. If the local state changes can be properly forecasted, it is highly possible that global tipping point is only a matter of quantity.

<!-- b000161 | prose | pages [10] -->
The features indicating coming tipping points or state changes are similar between local or  global scale. So a model that can identify such features locally is also able to identify them globally.

<!-- b000162 | prose | pages [10] -->
For the three reasons above, we consider it equivalent to make local and global verification on this model.

<!-- b000163 | heading | pages [10] -->
3.2 Fit verification

<!-- b000164 | prose | pages [10] -->
We first verify that the parameters we set to train the local neural networks (e.g. learning rate, particle swarm size and hidden layer node numbers) do not make our model over-fitted. To achieve this goal, we train the neural with data of the first 30 years, and then we use autonomous forecast to generate results of the rest years. If these results differ greatly with the actual dataset, then we say this model is over-fitted and is not competent to make prediction of the future.

<!-- b000165 | prose | pages [10] -->
130 forecast value actual value 120

<!-- b000166 | prose | pages [10] -->
110

<!-- b000167 | prose | pages [10] -->
100

<!-- b000168 | prose | pages [10] -->
90 pollution/AQI 80

<!-- b000169 | prose | pages [10] -->
70

<!-- b000170 | prose | pages [10] -->
60

<!-- b000171 | prose | pages [10] -->
50

<!-- b000172 | prose | pages [10] -->
40

<!-- b000173 | prose | pages [10, 11] -->
30 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year Figures 4 contains an example of the results and corresponding datasets. From the figure we can see that the prediction approximately follows the curve, although some noise does exist. Considering that the networks we are trying to verify are only trained with 30 samples, such a result can be judged as satisfactory. Hence, we determine that both the training process and parameters are proper. In the following sections, we test the prediction ability and several other more advanced functions of this model.

<!-- b000174 | caption | pages [10] -->
Figure 4 The result of stepwise forecast: Belgium

<!-- b000175 | furniture | pages [11] -->
Team #21165

<!-- b000176 | furniture | pages [11] -->
Page 10 of 18

<!-- b000178 | heading | pages [11] -->
3.3 Identifying critical nodes

<!-- b000179 | prose | pages [11] -->
In our model, the feedback input is determined by other nations’ global type outputs. Reversely, the more critical a node is, the more “feedback” it will output to other topologically-adjacent nations. Like what we have done in basic model, the influence degree of a single node can be defined as follows:

<!-- b000180 | prose | pages [11] -->
n  (i: i th Global Node,  j: j th year) G g q ( , S l , )  j i j , 1 i i  i 1 Note that the global node here is “destination global node”, that is, the destination of the feedback, while the global node in what we have defined before is “source global node”.

<!-- b000181 | prose | pages [11] -->
Ideally, the function g (q, S, l) can be set the same as f (q, S, l). But we have noticed that f (q, S, l) stresses more on the local impact of a pollutant source, while people may want to find a critical node that has more “potential” to impose a larger impact to the whole earth. From this perspective, we improvise a new function that meets this need. The newly defined g (q, S, l) is:

<!-- b000182 | prose | pages [11] -->
l q S    1.2 2 ( ) e ( ) 1000 1000 10000  g q S l ( , , ) . 100 With this function, we are able to calculate the influence degree of the function. We use several nations among the most important ones to show our results. From Figure 5, it can be found out that this measure of nodal influence correctly shows the worldwide difference between nations while also avoid over-exaggerating them.

<!-- b000183 | prose | pages [11] -->
600

<!-- b000184 | prose | pages [11] -->
500

<!-- b000185 | prose | pages [11] -->
400

<!-- b000186 | prose | pages [11] -->
300

<!-- b000187 | prose | pages [11] -->
200

<!-- b000188 | prose | pages [11] -->
100

<!-- b000189 | prose | pages [11] -->
0

<!-- b000190 | caption | pages [11] -->
Figure 5 Identifying the critical nodes

<!-- b000191 | heading | pages [11] -->
3.4 Sensitivity to a relationship change

<!-- b000192 | prose | pages [11, 12] -->
We next move on to testify whether our model is able to react to relationship change. Usually, a system with more links between elements suffers more fluctuations, because under such a situation, the system is more likely to advance toward a dynamic balance. On the contrary, when some links or nodes are removed, the subsystem becomes relatively more constrained and is likely to enter a steady state.

<!-- b000193 | furniture | pages [12] -->
Team #21165

<!-- b000194 | furniture | pages [12] -->
Page 11 of 18

<!-- b000196 | prose | pages [12] -->
160 forecast value actual value 140

<!-- b000197 | prose | pages [12] -->
120

<!-- b000198 | prose | pages [12] -->
pollution/AQI index 100

<!-- b000199 | prose | pages [12] -->
80

<!-- b000200 | prose | pages [12] -->
60

<!-- b000201 | prose | pages [12] -->
40

<!-- b000202 | prose | pages [12] -->
20

<!-- b000203 | prose | pages [12] -->
0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year (a) With China

<!-- b000204 | prose | pages [12] -->
160 forecast value actual value 140

<!-- b000205 | prose | pages [12] -->
120

<!-- b000206 | prose | pages [12] -->
pollution/AQI index 100

<!-- b000207 | prose | pages [12] -->
80

<!-- b000208 | prose | pages [12] -->
60

<!-- b000209 | prose | pages [12] -->
40

<!-- b000210 | prose | pages [12] -->
20

<!-- b000211 | prose | pages [12] -->
0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year (b) Without China

<!-- b000212 | caption | pages [12] -->
Figure 6 (a) (b) Sensitivity to a relationship change: removing or not removing China

<!-- b000213 | prose | pages [12] -->
In order to show that our model is able to simulate such a change, we remove China from the network (a node of significant influence to its surroundings) and retrain the model in the same way we done before. We then perform an autonomous forecast from the year of 1985 on both models to see if the results generated differ. Contained in Figure 6 are two results we get respectively in a forecast on India, a geographically adjacent country of China. From these figures it’s obvious that the fluctuation of the forecast is much smaller after the node representing China is removed. From this comparison, we consider the model being able to reflect the changes in the relationships between the nodes.

<!-- b000214 | furniture | pages [13] -->
Team #21165

<!-- b000215 | furniture | pages [13] -->
Page 12 of 18

<!-- b000216 | heading | pages [13] -->
3.5 Case Study

<!-- b000217 | prose | pages [13] -->
In this part of the paper, we consider a more realistic situation in order to verify that our model is able to accomplish more complicated tasks: predicting state changes and tipping points, reflecting changes that may be brought in by the policies, and provide adequate warnings to decision makers. These functions are partially intertwined and are not suitable to be discussed separately. Hence, we use a case study to address the problem.

<!-- b000218 | prose | pages [13] -->
The last 50 years witness the move of manufacture industry centers from fortune-rich, developed countries to resource-rich, developing countries [10]. So does air pollutions.  This trend can be easily seen in Figure 7 (a) (b) below. Note that the darker the color, the more serious the pollution. To demonstrate that our model is able to show this trend, we pick two countries that are among the most typical ones in both categories: Japan and India.

<!-- b000219 | prose | pages [13] -->
(a) 1970

<!-- b000220 | prose | pages [13] -->
(b) 2008

<!-- b000221 | caption | pages [13] -->
Figure 7 (a) (b) The change of world pollution distribution

<!-- b000222 | prose | pages [13] -->
In the period of rapid economic growth after World War II, environmental policies were downplayed by the Japanese government and industrial corporations; as a result, environmental pollution was widespread in the 1950s and 1960s [14]. In response to such situation, the government enacted a series of laws and bills to ameliorate the situation. Although great improvements were made in water pollution, obvious change in air quality does not take place. It was not until more strict legislations were enacted in1990s did the situation really began to change [12]. At present, Japan is considered one of the most eco-friendly nations, which also holds true from the perspective of air pollution.

<!-- b000223 | furniture | pages [14] -->
Team #21165

<!-- b000224 | furniture | pages [14] -->
Page 13 of 18

<!-- b000225 | prose | pages [14] -->
Before 1991, India is a nation which followed protectionist policies that were influenced by socialist economics, but an acute balance of payments crisis in 1991 forced the nation to liberalize its economy [13]. While transforming into one of the fastest-growing economy in the developing world, India has also suffered a significant growth in industrial, energy, transport, urban population since then. Up to 2013, air pollution has become a serious barrier in its social and economic development. Sukinda and Vapi are even elected as the 3rd and 4th most polluted cities in the world [11].

<!-- b000226 | caption | pages [14] -->
Figure 8 is the plot we get from an autonomous forecast by our model. The forecast starts from

<!-- b000227 | prose | pages [14] -->
the year of 1985, when the air condition in Japan is still poor.  From the figure, it can be seen that in the first 8 years, the pollution rate increases approximately the same as the actual value, but in 1993, a sudden bounce has taken place and the pollution rate has risen to a much higher value. This point, in our view, is the “tipping point” of Japan air condition. This is the exact time point where if no additional air pollution reduction measures were taken, a major state change will take place, and it will be irreversible.

<!-- b000228 | prose | pages [14] -->
160 forecast value actual value 140

<!-- b000229 | prose | pages [14] -->
120

<!-- b000230 | prose | pages [14] -->
pollution/AQI index 100

<!-- b000231 | prose | pages [14] -->
80

<!-- b000232 | prose | pages [14] -->
60

<!-- b000233 | prose | pages [14] -->
40

<!-- b000234 | prose | pages [14] -->
20

<!-- b000235 | prose | pages [14] -->
0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year

<!-- b000236 | caption | pages [14] -->
Figure 8 Case Study using an autonomous forecast: Japan

<!-- b000237 | prose | pages [14] -->
We move on to examine the case of India. Figure 9 is the plot we get from an autonomous forecast by our model in which no condition has changed except the nation. From this plot, it can be concluded that if it is not the liberalism reform of its economy in 1991, its air pollution condition might remain in a relatively steady state where the average nationwide AQI would be about 50, like what it was in 1985. However, as the actual value curve indicates, the fact is that India’s pollution index value has reached about 150 by 2008, among the highest ones we have been able to seen in this dataset.

<!-- b000238 | prose | pages [14] -->
These two examples are typical in two aspects: social and functional.  The examples are socially-typical because these two nations have included what most countries in this world have undergone in the past 50 years: pollute-and-control, or polluting-while-developing. It is also obvious that most of the developing countries are experiencing what developed countries had experienced 40 years ago, and the warnings shown in Figure 8 indicates that the result might be very serious.  The examples are functionally-typical because the forecast we performed on these two nations have included almost all of the functions the requirements ask from us: state-change and tipping point prediction, warning providing and information to the decision makers.  The result has verified that the model is capable of these tasks and the results we get from them contain useful information that can be used for decision-making.

<!-- b000239 | furniture | pages [15] -->
Team #21165

<!-- b000240 | furniture | pages [15] -->
Page 14 of 18

<!-- b000241 | prose | pages [15] -->
160 forecast value actual value 140

<!-- b000242 | prose | pages [15] -->
120

<!-- b000243 | prose | pages [15] -->
pollution/AQI index 100

<!-- b000244 | prose | pages [15] -->
80

<!-- b000245 | prose | pages [15] -->
60

<!-- b000246 | prose | pages [15] -->
40

<!-- b000247 | prose | pages [15] -->
20

<!-- b000248 | prose | pages [15] -->
0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year

<!-- b000249 | caption | pages [15] -->
Figure 9 Case Study using an autonomous forecast: India

<!-- b000250 | prose | pages [15] -->
To further illustrate the effect our model can reflect about the policies and the way our model helps with the decision making, we include yet another example about the policy: Hungary. Hungary was under Soviet domination until the collapse of the Union in 1989. For this reason, the industry production suffered a major fall in early 1990s, which has partly contributed to the significant decrease of its air pollution. While restoring its economy, the newly established Hungarian Parliament enacted the first Nation Environment Program (NEP) in 1997. The program covers the period of 1997 to 2002 and enormously ameliorated the pollution condition in the past [15]

<!-- b000251 | caption | pages [15] -->
Figure 10 is the plot from the autonomous of our model (start from 1985). In this figure we

<!-- b000252 | prose | pages [15] -->
have discovered a similar forecast curve as in Figure 8. A state change point (tipping point) exists on 1991, where a bounce of AQI value brings the country to an irreversible change. But conversely, the actual curve goes all the way down and reached its lowest value of 10 (approx.) in the year of 2008.

<!-- b000253 | prose | pages [15] -->
200 forecast value actual value 180

<!-- b000254 | prose | pages [15] -->
160

<!-- b000255 | prose | pages [15] -->
140 pollution/AQI index 120

<!-- b000256 | prose | pages [15] -->
100

<!-- b000257 | prose | pages [15] -->
80

<!-- b000258 | prose | pages [15] -->
60

<!-- b000259 | prose | pages [15] -->
40

<!-- b000260 | prose | pages [15] -->
20

<!-- b000261 | prose | pages [15, 16] -->
0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year The history of Hungary and India resembles in certain respect. Both have undergone a liberalism reform in the economy and both have enjoyed significant boom in their economic achievement. But in the respect of air pollution control they are definitely different: the Indians have pushed themselves into the list of most air-polluted countries, while Hungarians are harmonizing their living environment at the same time. From the forecast of our model, the difference is clear, and, from our perspective, so are the optimal development decisions of the decision makers.

<!-- b000262 | caption | pages [15] -->
Figure 10 Case Study using an autonomous forecast: Hungary

<!-- b000263 | furniture | pages [16] -->
Team #21165

<!-- b000264 | furniture | pages [16] -->
Page 15 of 18

<!-- b000266 | heading | pages [16] -->
4 Conclusion

<!-- b000267 | heading | pages [16] -->
4.1 Strength and Weakness

<!-- b000268 | heading | pages [16] -->
Strengths

<!-- b000269 | prose | pages [16] -->
 Embracing the complexity of Earth’s interrelated systems Although the development of our model is quite plain, it still manages to achieve satisfying flexibility. Such flexibility in setting input, output and the link make the whole model a complex interlinked system with multiple factors. In this way, the model can be devised into different scales and types to apply to various situations.

<!-- b000270 | prose | pages [16] -->
 The complete functionality of  the model The functions of the model include predicting and providing warnings about state changes, helping with policy-making, etc. Our model is also capable of identifying critical nodes and relationships. Such complete functionality results from the good structural designs and careful algorithm picking.

<!-- b000271 | prose | pages [16] -->
 Autonomous forecast mechanism Our model can perform an autonomous forecast with a set of initial data. The forecast can last a long enough time depending on the requests.

<!-- b000272 | heading | pages [16] -->
Weaknesses

<!-- b000273 | prose | pages [16] -->
 Relatively higher sensitivity In our model, we only had 30 samples to train the neural network because of the lack of data. For the same reason, some important factors may not present.  Hence, the accuracy is affected and the result is probably more interfered by the small fluctuation of inputs.

<!-- b000274 | prose | pages [16] -->
 Difficulty in finding a proper link function When devising our model, we found that most of the scientific studies concerning network system links are constrained in relatively small model. Hence, these results may not suitable to be introduced into the global model.  And we infer that some other network with a huge scale may face the same difficulty as well.

<!-- b000275 | prose | pages [16] -->
 Long training time spending on neural network This is defined the structural feature of neural network.

<!-- b000276 | heading | pages [16] -->
4.2 Extension

<!-- b000277 | prose | pages [16] -->
The dual-layer network design and the flexible setting of input, output and the link make the whole model a complex interlinked system with multiple factors. The lower level network performs prediction while the higher level network sets up the links. This kind of system matches the reality well and can be extended to some other aspects.

<!-- b000278 | furniture | pages [17] -->
Team #21165

<!-- b000279 | furniture | pages [17] -->
Page 16 of 18

<!-- b000280 | prose | pages [17] -->
For example, water quality can also be seen as a reflection of the Earth’s health. Changing the link and some of the inputs and outputs properly, with the autonomous mechanism, prediction can be made and the condition can be measured. In addition, our model can apply to some small ecosystems and biological system for the similarity of network structure. Moreover, we believe that the ubiquity of the model make it possible to help people make prediction in other domains.

<!-- b000281 | furniture | pages [18] -->
Team #21165

<!-- b000282 | furniture | pages [18] -->
Page 17 of 18

<!-- b000283 | heading | pages [18] -->
References

<!-- b000284 | references | pages [18] -->
[1] Robert Watson and A. Hamid Zakri, 2005, UN Millennium Ecosystem Assessment Synthesis

<!-- b000285 | references | pages [18] -->
Report, United Nations Report (pp 16-30)

<!-- b000286 | references | pages [18] -->
[2] Will Steffen, Jacques Grinevald, Paul Crutzen and John McNeill, 2010, The Anthropocene:

<!-- b000287 | references | pages [18] -->
conceptual and historical perspectives, AMBIO 40, 739–761

<!-- b000288 | references | pages [18] -->
[3] Donella Meadows, Jorgen Randers, and Dennis Meadows, 2004, Limits to Growth: The 30-year

<!-- b000289 | references | pages [18] -->
update, (pp15)

<!-- b000290 | references | pages [18] -->
[4] McNeill, J. R. 2000 Something new under the sun: an environmental history of the twentieth

<!-- b000291 | references | pages [18] -->
century world. London, UK: W.W. Norton

<!-- b000292 | references | pages [18] -->
[5] Anthony D. Barnosky, Elizabeth A. Hadly, Jordi Bascompte, Eric L. Berlow, James H.

<!-- b000293 | references | pages [18] -->
Brown,Mikael Fortelius, Wayne M. Getz, John Harte, Alan Hastings, Pablo A. Marquet, Neo

<!-- b000294 | references | pages [18] -->
D.Martinez, Arne Mooers, Peter Roopnarine, Geerat Vermeij, John W. Williams, Rosemary

<!-- b000295 | references | pages [18] -->
Gillespie, Justin Kitzes, Charles Marshall, Nicholas Matzke, David P. Mindell, Eloy Revilla,

<!-- b000296 | references | pages [18] -->
Adam B. Smith. 2012, "Approaching a state shift in Earth's biosphere". Nature, 2012; 486

<!-- b000297 | references | pages [18] -->
(7401): 52 DOI: 10.1038/nature11018

<!-- b000298 | references | pages [18] -->
[6] McPherson, E. Gregory; Nowak, David J.; Rowntree, Rowan A. eds. 1994. Chicago's urban

<!-- b000299 | references | pages [18] -->
forest ecosystem: results of the Chicago Urban Forest Climate Project. Gen. Tech. Rep. NE-

<!-- b000300 | references | pages [18] -->
186.  Radnor, PA: U.S. Department of Agriculture, Forest Service, Northeastern Forest

<!-- b000301 | references | pages [18] -->
Experiment Station: 201 p

<!-- b000302 | references | pages [18] -->
[7] George E. Taylor, Dale W. Johnson and Christian P. Andersen, 1994, Air Pollution and

<!-- b000303 | references | pages [18] -->
Forest Ecosystem: A Regional to Global Perspective, Ecological Applications, Vol.4.No.4

<!-- b000304 | references | pages [18] -->
(Nov, 1994), (pp 662-689) Ecological Society of America

<!-- b000305 | references | pages [18] -->
[8] 2003, Air Quality Index A Guide to Air Quality and Your Health, Retrieved February 1st, 2013,

<!-- b000306 | references | pages [18] -->
from United States Environment Protect Agency

<!-- b000307 | references | pages [18] -->
Web site: http://www.epa.gov/airnow/aqi_cl.pdf

<!-- b000308 | references | pages [18] -->
[9] G. Grigoras, V. Cuculeanu, G. Ene, G. Mocioaca, A. Deneanu, 2012, Air Pollution Dispersion

<!-- b000309 | references | pages [18] -->
Modeling In A Polluted Industrial Area Of Complex Terrain From Romania ,Romania Reports

<!-- b000310 | references | pages [18] -->
in Physics, Vol. 64, No. 1, P. 173–186

<!-- b000311 | references | pages [18] -->
[10] Chun Gong, Zhenglin Wang, 2009, Master Matlab Optimized Calculation, pp 270-303, Beijing,

<!-- b000312 | references | pages [18] -->
Publishing House of Electronics Indstry(712108251)

<!-- b000313 | references | pages [18] -->
[11] Staff Writers,10 Most Polluted Cities In The World In 2013, Retrieved February 4th, 2013,

<!-- b000314 | references | pages [18] -->
form O,Pish, Posh!

<!-- b000315 | references | pages [18] -->
Web site: http://opishposh.com/most-polluted-cities-in-the-world/

<!-- b000316 | references | pages [18] -->
[12] Environment Issues, Japan Fact Sheet, Retrieved February 4th, 2013, from Web

<!-- b000317 | references | pages [18] -->
Japan

<!-- b000318 | references | pages [18] -->
Web site: http://web-japan.org/factsheet/en/pdf/e45_environment.pdf

<!-- b000319 | references | pages [18] -->
[13] India, Retrieved February 4th, 2013, from Wikipedia

<!-- b000320 | references | pages [18] -->
Web site: http://en.wikipedia.org/wiki/India#Economy

<!-- b000321 | references | pages [18] -->
[14] Japan, Retrieved February 4th, 2013, from Wikipedia

<!-- b000322 | references | pages [18] -->
Web site:  http://en.wikipedia.org/wiki/Japan#Environment

<!-- b000323 | references | pages [18] -->
[15] Hungary Environment Report, Retrieved February 4th, 2013, form OECD

<!-- b000324 | references | pages [18] -->
Web site: http://www.oecd.org/env/

<!-- b000325 | references | pages [18] -->
Other References

<!-- b000326 | references | pages [18] -->
[1] GHG (CO2, CH4, N2O, F-gases) emission time series 1990-2010 per region/country. Retrieved

<!-- b000327 | references | pages [18] -->
February 1st, 2013, from EDGAR-Emission Database for Global Atmospheric Research

<!-- b000328 | references | pages [18] -->
Web site: http://edgar.jrc.ec.europa.eu/overview.php?v=GHGts1990-2010

<!-- b000329 | references | pages [18] -->
[2] GDP (current US$), Retrieved February 1st, 2013, from The World Bank

<!-- b000330 | references | pages [18] -->
Web site: http://data.worldbank.org/indicator/NY.GDP.MKTP.CD?page=1

<!-- b000331 | furniture | pages [19] -->
Team #21165

<!-- b000332 | furniture | pages [19] -->
Page 18 of 18

<!-- b000333 | references | pages [19] -->
[3] Industry, value added (% of GDP), Retrieved February 1st, 2013, from The World Bank

<!-- b000334 | references | pages [19] -->
Web site: http://data.worldbank.org/indicator/NV.IND.TOTL.ZS

<!-- b000335 | references | pages [19] -->
[4] Population, total, Retrieved February 1st, 2013, from The World Bank

<!-- b000336 | references | pages [19] -->
Web site: http://data.worldbank.org/indicator/SP.POP.TOTL

<!-- b000337 | references | pages [19] -->
[5] Forest area (% of land area), Retrieved February 1st, 2013, from The World Bank

<!-- b000338 | references | pages [19] -->
Web site: http://data.worldbank.org/indicator/AG.LND.FRST.ZS

<!-- b000339 | references | pages [19] -->
[6] Countries, Capitals, Latitude and Longitude Table, Retrieved February 1st, 2013, from

<!-- b000340 | references | pages [19] -->
CSGNetWork

<!-- b000341 | references | pages [19] -->
Web site: http://www.csgnetwork.com/llinfotable.html

<!-- b000342 | references | pages [19] -->
[7] Surface area Retrieved February 1st, 2013, from The World Bank

<!-- b000343 | references | pages [19] -->
Web site: http://search.worldbank.org/data?qterm=area&language=EN

<!-- b000344 | references | pages [19] -->
[8] Feng Shi, Xiaochuan Wang, Lei Yu, Yang Li, YanLiang Zhang, 2010, MATLAB neural

<!-- b000345 | references | pages [19] -->
networks: 30 case studies, pp21-35, Beijing: BUAA Press, 7-5124-0034-4
