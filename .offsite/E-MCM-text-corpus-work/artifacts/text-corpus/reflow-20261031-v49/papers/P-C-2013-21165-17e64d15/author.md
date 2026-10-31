Abstract

In this paper, we build a model to measure the earth’s health in the aspect of air quality. We choose Air Quality Index (AQI) as the basis of health measure, while using a weighted average as the final expression. Our model takes the form of dual-layer network. Among the two layers, the local network is implemented using neural network optimized by Particle Swarm Optimization (PSO) algorithm, while the global network links the nodes with feedback links defined by certain propagation function. The model takes the output from the former year as the input of the following year, thus establishing an autonomous system by itself.

We then move on to verify the model. First we test the model’s fundamental network property from the perspective of fit, critical nodes, and missing relationships. As case studies, we applied our model to specific nations on a timespan of 1985-2008, namely Japan, India, and Hungary in hope to demonstrate that our model is able to generate prediction and warnings of state changes, and provide information for decision-makers. Our model has shown a completeness of functionality and impressive flexibility in these tests. Furthermore, we have been able to see that the prediction test of our model coincides fairly well with the fact.

1 Introduction

1.1 Background

The growing stress on Earth’s environment and biological system are extremely apparent now. 15 out of 24 of the ecosystem services examined during the UN-based Millennium Ecosystem Assessment are being degraded or used unsustainably, including fresh water, capture fisheries, air and water purification and the regulation of regional and local climate, natural hazards, and pests [1].

Human activity is the main reason causing the significant changes of ecosystems which harm Earth health a lot. The largely growing demand of natural source over the past 50 years changed ecosystems more rapidly and extensively than in any comparable period of time in human history. [1] Moreover, excessive emission of the waste and pollutant leads to dramatic environmental changes as well.

Many global scale changes in ecosystems are displayed as exponential growth in the past half century. They can be large in magnitude and difficult or impossible to reverse once a threshold is crossed. As many of the trends appeared in the past century have continued, it is likely that the degradation of ecosystem services could grow worse in this century. In this way, global ecosystem may be approaching a planetary-scale ‘tipping point’. Therefore a prediction of potential state change of Earth’s health is needed. [2]

the onset of increasing extraction costs [3]. Under such postulation, the ‘tipping point’ will occur in around 2050.

1.2 An Overview of Air Quality

1.2.1 Air Quality: A Reflection of Earth’s Health Air quality regulation is one of that fifteen ecosystem services which are being degraded and used unsustainably. Human need to pay much attention on air quality for not only it can reflect the condition of the Earth environment but also directly affect the health of many creatures. Moreover, it cannot be neglected that atmosphere activity helps the pollutant dispersion as well.

In most cases, climate changes and air quality are combined and many recent studies prefer to pay more attention on the greenhouse effect. However, both Great London Smog in 1952 and North China haze in 2013 show that heavy air pollution and particle pollution have lethal potential.

1.2.2 Primary Influence Factors  Population explosion and rapid economic growth Between 1800 and 2000, the human population grew from about one billion to six billion, while energy use grew by about 40-fold and economic production by 50-fold [4]. In addition, the consumption of petroleum grew by a factor of 3.5 since 1960. The number of motor vehicles rose from only 40 million at the end of WWII to about 700 million by 1996, and continues to rise steadily [2]. Despite such rapid growth in population and economy, such a growth has also left a significant imprint on the environment, which is shown in the figures below.

(a) (b) (c)

as a result of the dramatic increase in human activity: atmospheric N2O concentration [2]

 Forest coverage Forest coverage is a notable factor to air quality. On the one hand, gaseous and particle pollutants can be dry-deposited by trees through a mechanism named dry deposition, thus improving air quality [6]. On the other hand, many gaseous and particle pollutants, acting individually or in combination, affects forests particularly [7].

1.3 Air Quality Index (AQI)

Air Quality Index (AQI), developed by Environment Protection Agency (EPA) of United States, is aiming at helping people know what local air quality means to their health. This index is calculated by some major air pollutants which are regulated by the Clean Air Act, such as particle pollution and sulfur dioxide, etc. Table 1 [8] shows the six categories of AQI and their meanings, each of the categories is assigned by a specific color.

Table 1

1.4 Assumptions

 The health measure of earth’s atmosphere can be assessed by Air Quality Index (AQI) We choose AQI as the earth health measure to associate the environmental and biological systems, more details of AQI can be found in the background part of the paper.

The following three assumptions only constrain the basic model.  While considering the air flow, the impact of topography is ignored.  One year is taken as the minimal time unit in the model.  We choose the nations around the world as the Global Nodes. The coordinates of the nodes are represented by the capitals’ longitude and latitude positions.

The assumptions above are due to the limitation of the data we have. In fact, the more data we collect, the more accurate result that the model will catch.

1.5 Notations

Table 2 Symbol Meaning the feedback function of a node coming from another node in the global f network g the influence degree function of a node derived from feedback function

population density of a nation d r forest coverage rate of a nation p proportion of secondary sector of the economy in GDP in a nation the sum of feedbacks to a node coming from other nodes in the whole network F

q AQI value of a nation land area of nation S distance between every two nations l

2 Model

In order to fulfill the requirements of International Coalition of Modelers (ICM), the goal of our team seems to be very clear. The content of our paper is aiming at building a dynamic global air quality network model to show the health condition of Planet Earth by identifying local elements of this condition and appropriately connecting them to track relationship and attribute effect. The model we build needs to include the human element and has the function of predicting Earth’s health future states by a specific health measure.

2.1 Generic Methodology

We model the dynamic global air quality network as a combination of local and global networks with interlinked architecture, which has high similarity with Internet.

global network while the right part displays the details of a single local network. To make the methodology more understandably, we defined seven concepts below.

i+2 ...

... Global Link (i+1, i+2) Global Link (i, i+2) i+1 Global Link (i, ...) Global Link Local Type (i, i+1) Output Global Type ... Local View Output

... 1 2 n

i

...

Inputs

Global Nodes

Local Nodes Local Network Local Network n Node

 Local Network: Neural network Having considered the fact that the data available might be very limited, we decide to use neural network as local part of the whole system. Unlike the traditional mathematical methods such as regression or time series prediction, neural network is famous for its unique learning ability, and thus is able to extract the approximate feature of the data from a relatively small sample.

In the machine learning theory, the neural network method itself is further divided into several different categories. To reduce complexity, we choose the most basic BP model. Because a multiple output network will reduce the accuracy of the model (since the input edges are shared), each of our local network is dedicated to only one output.

The BP model, however, has a major setback of slow convergence. Noting that we may have myriad of such networks in a single system, a very long training time is surely not ideal. Hence we introduce Particle Swarm Optimization (PSO) to help the neural network define best weights of linking edges. PSO is a newly emerging optimization algorithm which optimizes the value of function by simulating multiple particles that travels freely in the solution space. Each particle communicates with others to decide where to go for the next iteration. Because the number of such particles can be large, the optimal value can be quickly found. At the same time, the goal function rarely gets stuck in a local optimal value.  Local Node: A single neuron i) Input layer The neurons on the input layer are divided into two categories.  Neurons of the first category were dedicated to factors ranging from human element, biological system to environmental system that affect the air quality. In addition, another category of neurons is needed to be assigned to the sum of the feedback from other Global Nodes. For neurons in this category, their initial values are zero.

ii) Output layer The neuron on the output layer of each neural network represents one of the factors appeared on the input layer. The output of each neural network can be divided into two types: local and global. Local Type Output means that the factors do not have communication with other Global Nodes, they are calculated without feedbacks. While Global Type Output has communication with other Global Nodes.

 Global Node: Node made up by n Local Networks Node at this level may has more than one output, but each neural network should be dedicated to only one output, as we have just mentioned. Hence n Local Networks are needed to construct a Global Node.

 Global Link: A distance value between nodes and a link function The distance measures the tightness of relationship between nodes and is not confined to physical distance. The link function is a map from Global Type Output to the feedback input, which forms the communication between nodes.

 Global network: A network consists of Global Nodes which connect and communicate with each other by Global Link

One thing should be noted that the Global Network we devised is an autonomous system. Here the term autonomous means that the output and the feedback of the j th year is taken as the input of the (j+1) th year. To fully understand the mechanism, consider the following example: suppose we x x , , ..., nx ]. Using a one-step forecast, we are able to generate local have initial input vector xj=[ 1 2 type output yi1 and global type output yi2, thus further generating the feedback input Fi. We then combine vectors yi1 and Fi to form a new input vector of xj+1 and start the forecasting process once  j  to j n 1 again. Henceforth, in this way, we can get all the results from year (for any n) using only a group of variables defining initial condition of the system. This property is important because it theoretically enables us to make an indefinitely long forecast of the future trend with very small amount of data.

We have finished the structural introduction of our methodology. At this point we are able to give the general expression of earth’s health measure from the perspective of air quality. Suppose in a certain year there is only one output (e.g. AQI value) that directly influences the final value of ky , thus forming a weight health measure. For each global node k, we assign a weight to this output w w , ,..., w ]. We calculate the weighted mean of this output as follows (suppose vector of W= [ 1 2 n there are n nodes in total):

n   w y k k  k 1 H . n  w k  k 1 This is the expression of earth’s health measure. As for defining the tipping points, it is discussed in [5] that tipping points are often hard to define, but some features before the tipping points may help distinguish the state change, such as rising risk of nonlinear changes and fluctuations. Hence, we do not define generic judging criteria of tipping points here. From our perspective, it might be wiser that each case is specifically analyzed according to the feature it shows.

2.2 Basic Model

2.2.1 Input and Output of Local Network Due to the limitation of the data that could be collected, we set the primary influence factors of air quality into three aspects of inputs and measured by rate to unify outputs because of the different nation scale.

Table 3 Input Output Name and Notation Initial Name and Notation Type Value Local Type population density of a nation d population density d d 0

forest coverage rate of a nation r forest coverage rate r Local Type 0r

the proportion of secondary sector of the the proportion of secondary 0p sector of the economy in Local Type economy in GDP of a nation  p GDP  p The sum of feedback to a Global Node coming from other Global Nodes in the 0 Global Type Air Quality Index (AQI)  q whole Global Network  F

2.2.2 Global Network Aspect  Global Nodes : made up by four Local Networks  Global Link:

The sum of feedbacks to a Global Node coming in the whole Global Network is defined by:

n  F f q ( , S l , ) ( i: i th Global Node,  j: j th year)  j i j , 1 i i  i 1 While the feedback from a single Global Node is:

l l   1 280   q e S 55  f q S l ( , , ) 6 10

2.3 Advanced Model

The limitation of the basic model is mainly because of the data information. Therefore if the source of the different aspects’ factors that affect the air quality is comprehensive, with the generic methodology, a more advanced model could be implemented.

2.3.1 Input and Output of Local Network Despite the existing factors mentioned in the basic model, the two aspects of factors below can be taken into consideration: air pollution created by nature including volcanic eruption, dust cloud etc.; other human activity, such as the amount of mobile vehicle, resource consumption, overgrazing and a very important one: policy.

2.3.2 Global Network Aspect  Global Node We choose the pollution source as the Global Node. These Global Nodes form a three- dimensional model which x-axis and y-axis represent longitude and latitude，while z-axis is altitude.

 Global Link： We use equation in the Gaussian Dispersion Model to calculate the feedback [9].

 2 2 Q y ( z 500)    C x y z ( , , ) exp( ){exp[ ]}      2 2 2 u 2 2 y z y z

C   Pollutant concentration u Average wind speed Q   Pollutant emission per unit time x The distance to any node downwind    Lateral diffusion coefficient: a function of x y The distance to any node at right-angle y horizontal direction    Vertical diffusion coefficient: a function of x z  The average altitude z

3 Verification

3.1 Overview

In this section we seek to verify our model using some datasets that can be retrieved at present. As the problem requirement has mentioned, the global data which are needed to verify such complex network are often difficult to assess. For this very reason, we do not verify advanced model in this paper. All the model verifications discussed below are concerned with the basic model.

Although we are also not able to find a continuous air pollution record that has satisfactory time span and nation coverage, we managed to get world pollutant emission statistics (by nation) from the website of Emission Database for Global Atmospheric Research (EDGAR). This dataset contains data over a 39-year time span (1970-2008) from over 100 nations (After deleting some nations with too little data, the final dataset we get contains 115 nations).  Since the emission rate and AQI value is highly correlated, we estimate the pollution rate measured by AQI using the following formula:

(        )       .

Where   and    are defined as follows:

In this category of formulas, E, S denotes the average emission rate per m2 and area by country, respectively.   and other variables in the second formula can be determined using a pair of datasets containing emission rate and AQI from any single year. In this paper we used data of 2008 offered by World Bank to define  . Comparison of our estimate with some small datasets from other sources indicates that such estimation is reasonable.

For the three other training statistics, namely the population density, the forest coverage rate and the proportion of secondary sector of the economy in GDP of a nation, direct data access is provided by World Bank. The link to all the data we use can be found in reference section.

As a basis of the verification section, we define the following 2 forecast methods:  Stepwise forecast: after getting the result of i th year, input data of i th year from the dataset to get result of (i+1) th year.

 Autonomous forecast: trigger the system using the data of the first year, then make the system run autonomously to forecast the future results. By “autonomously” we mean that the result of i th year is taken as the input to get the result of (i+1) th year, as has been stated in generic methodology. Because only one sample of data is offered when performing autonomous forecast, the result we get from the model completely excludes exterior influences other than the input factors (e.g. policy). Plus, the error may accumulate over time and lead to some fluctuation in the prediction, but as we will see later in this paper, the trend can still be clearly judged from the resulting plot.

Before we start to introduce the verification we make, it is worthy to be mentioned that all of our verifications are performed on local scale. The reason that we do not offer a statistical global verification is as follows:

Judging from the current earth condition, a decisive state switch may not happen in 100 years  or even longer time from the latest time point of our data. Due to the limited sample we have in hand and the error accumulation property we have just mentioned, it does not make any sense to make a forecast of that length. On the contrary, local state changes often happens in a more recent time, and samples are available to provide reliability assess of our forecast.

The reason that our model are able to reflect global changes is that nations, denoted by global  nodes in the model, are interconnected by global feedback links so that they can interact with each other. Hence, global tipping points are in essentially accumulation results of local state changes. If the local state changes can be properly forecasted, it is highly possible that global tipping point is only a matter of quantity.

The features indicating coming tipping points or state changes are similar between local or  global scale. So a model that can identify such features locally is also able to identify them globally.

For the three reasons above, we consider it equivalent to make local and global verification on this model.

3.2 Fit verification

We first verify that the parameters we set to train the local neural networks (e.g. learning rate, particle swarm size and hidden layer node numbers) do not make our model over-fitted. To achieve this goal, we train the neural with data of the first 30 years, and then we use autonomous forecast to generate results of the rest years. If these results differ greatly with the actual dataset, then we say this model is over-fitted and is not competent to make prediction of the future.

130 forecast value actual value 120

110

100

90 pollution/AQI 80

70

60

50

40

30 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year Figures 4 contains an example of the results and corresponding datasets. From the figure we can see that the prediction approximately follows the curve, although some noise does exist. Considering that the networks we are trying to verify are only trained with 30 samples, such a result can be judged as satisfactory. Hence, we determine that both the training process and parameters are proper. In the following sections, we test the prediction ability and several other more advanced functions of this model.

3.3 Identifying critical nodes

In our model, the feedback input is determined by other nations’ global type outputs. Reversely, the more critical a node is, the more “feedback” it will output to other topologically-adjacent nations. Like what we have done in basic model, the influence degree of a single node can be defined as follows:

n  (i: i th Global Node,  j: j th year) G g q ( , S l , )  j i j , 1 i i  i 1 Note that the global node here is “destination global node”, that is, the destination of the feedback, while the global node in what we have defined before is “source global node”.

Ideally, the function g (q, S, l) can be set the same as f (q, S, l). But we have noticed that f (q, S, l) stresses more on the local impact of a pollutant source, while people may want to find a critical node that has more “potential” to impose a larger impact to the whole earth. From this perspective, we improvise a new function that meets this need. The newly defined g (q, S, l) is:

l q S    1.2 2 ( ) e ( ) 1000 1000 10000  g q S l ( , , ) . 100 With this function, we are able to calculate the influence degree of the function. We use several nations among the most important ones to show our results. From Figure 5, it can be found out that this measure of nodal influence correctly shows the worldwide difference between nations while also avoid over-exaggerating them.

600

500

400

300

200

100

0

3.4 Sensitivity to a relationship change

We next move on to testify whether our model is able to react to relationship change. Usually, a system with more links between elements suffers more fluctuations, because under such a situation, the system is more likely to advance toward a dynamic balance. On the contrary, when some links or nodes are removed, the subsystem becomes relatively more constrained and is likely to enter a steady state.

160 forecast value actual value 140

120

pollution/AQI index 100

80

60

40

20

0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year (a) With China

160 forecast value actual value 140

120

pollution/AQI index 100

80

60

40

20

0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year (b) Without China

In order to show that our model is able to simulate such a change, we remove China from the network (a node of significant influence to its surroundings) and retrain the model in the same way we done before. We then perform an autonomous forecast from the year of 1985 on both models to see if the results generated differ. Contained in Figure 6 are two results we get respectively in a forecast on India, a geographically adjacent country of China. From these figures it’s obvious that the fluctuation of the forecast is much smaller after the node representing China is removed. From this comparison, we consider the model being able to reflect the changes in the relationships between the nodes.

3.5 Case Study

In this part of the paper, we consider a more realistic situation in order to verify that our model is able to accomplish more complicated tasks: predicting state changes and tipping points, reflecting changes that may be brought in by the policies, and provide adequate warnings to decision makers. These functions are partially intertwined and are not suitable to be discussed separately. Hence, we use a case study to address the problem.

The last 50 years witness the move of manufacture industry centers from fortune-rich, developed countries to resource-rich, developing countries [10]. So does air pollutions.  This trend can be easily seen in Figure 7 (a) (b) below. Note that the darker the color, the more serious the pollution. To demonstrate that our model is able to show this trend, we pick two countries that are among the most typical ones in both categories: Japan and India.

(a) 1970

(b) 2008

In the period of rapid economic growth after World War II, environmental policies were downplayed by the Japanese government and industrial corporations; as a result, environmental pollution was widespread in the 1950s and 1960s [14]. In response to such situation, the government enacted a series of laws and bills to ameliorate the situation. Although great improvements were made in water pollution, obvious change in air quality does not take place. It was not until more strict legislations were enacted in1990s did the situation really began to change [12]. At present, Japan is considered one of the most eco-friendly nations, which also holds true from the perspective of air pollution.

Before 1991, India is a nation which followed protectionist policies that were influenced by socialist economics, but an acute balance of payments crisis in 1991 forced the nation to liberalize its economy [13]. While transforming into one of the fastest-growing economy in the developing world, India has also suffered a significant growth in industrial, energy, transport, urban population since then. Up to 2013, air pollution has become a serious barrier in its social and economic development. Sukinda and Vapi are even elected as the 3rd and 4th most polluted cities in the world [11].

the year of 1985, when the air condition in Japan is still poor.  From the figure, it can be seen that in the first 8 years, the pollution rate increases approximately the same as the actual value, but in 1993, a sudden bounce has taken place and the pollution rate has risen to a much higher value. This point, in our view, is the “tipping point” of Japan air condition. This is the exact time point where if no additional air pollution reduction measures were taken, a major state change will take place, and it will be irreversible.

160 forecast value actual value 140

120

pollution/AQI index 100

80

60

40

20

0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year

We move on to examine the case of India. Figure 9 is the plot we get from an autonomous forecast by our model in which no condition has changed except the nation. From this plot, it can be concluded that if it is not the liberalism reform of its economy in 1991, its air pollution condition might remain in a relatively steady state where the average nationwide AQI would be about 50, like what it was in 1985. However, as the actual value curve indicates, the fact is that India’s pollution index value has reached about 150 by 2008, among the highest ones we have been able to seen in this dataset.

These two examples are typical in two aspects: social and functional.  The examples are socially-typical because these two nations have included what most countries in this world have undergone in the past 50 years: pollute-and-control, or polluting-while-developing. It is also obvious that most of the developing countries are experiencing what developed countries had experienced 40 years ago, and the warnings shown in Figure 8 indicates that the result might be very serious.  The examples are functionally-typical because the forecast we performed on these two nations have included almost all of the functions the requirements ask from us: state-change and tipping point prediction, warning providing and information to the decision makers.  The result has verified that the model is capable of these tasks and the results we get from them contain useful information that can be used for decision-making.

160 forecast value actual value 140

120

pollution/AQI index 100

80

60

40

20

0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year

To further illustrate the effect our model can reflect about the policies and the way our model helps with the decision making, we include yet another example about the policy: Hungary. Hungary was under Soviet domination until the collapse of the Union in 1989. For this reason, the industry production suffered a major fall in early 1990s, which has partly contributed to the significant decrease of its air pollution. While restoring its economy, the newly established Hungarian Parliament enacted the first Nation Environment Program (NEP) in 1997. The program covers the period of 1997 to 2002 and enormously ameliorated the pollution condition in the past [15]

have discovered a similar forecast curve as in Figure 8. A state change point (tipping point) exists on 1991, where a bounce of AQI value brings the country to an irreversible change. But conversely, the actual curve goes all the way down and reached its lowest value of 10 (approx.) in the year of 2008.

200 forecast value actual value 180

160

140 pollution/AQI index 120

100

80

60

40

20

0 1970 1975 1980 1985 1990 1995 2000 2005 2010 time/year The history of Hungary and India resembles in certain respect. Both have undergone a liberalism reform in the economy and both have enjoyed significant boom in their economic achievement. But in the respect of air pollution control they are definitely different: the Indians have pushed themselves into the list of most air-polluted countries, while Hungarians are harmonizing their living environment at the same time. From the forecast of our model, the difference is clear, and, from our perspective, so are the optimal development decisions of the decision makers.

4 Conclusion

4.1 Strength and Weakness

Strengths

 Embracing the complexity of Earth’s interrelated systems Although the development of our model is quite plain, it still manages to achieve satisfying flexibility. Such flexibility in setting input, output and the link make the whole model a complex interlinked system with multiple factors. In this way, the model can be devised into different scales and types to apply to various situations.

 The complete functionality of  the model The functions of the model include predicting and providing warnings about state changes, helping with policy-making, etc. Our model is also capable of identifying critical nodes and relationships. Such complete functionality results from the good structural designs and careful algorithm picking.

 Autonomous forecast mechanism Our model can perform an autonomous forecast with a set of initial data. The forecast can last a long enough time depending on the requests.

Weaknesses

 Relatively higher sensitivity In our model, we only had 30 samples to train the neural network because of the lack of data. For the same reason, some important factors may not present.  Hence, the accuracy is affected and the result is probably more interfered by the small fluctuation of inputs.

 Difficulty in finding a proper link function When devising our model, we found that most of the scientific studies concerning network system links are constrained in relatively small model. Hence, these results may not suitable to be introduced into the global model.  And we infer that some other network with a huge scale may face the same difficulty as well.

 Long training time spending on neural network This is defined the structural feature of neural network.

4.2 Extension

The dual-layer network design and the flexible setting of input, output and the link make the whole model a complex interlinked system with multiple factors. The lower level network performs prediction while the higher level network sets up the links. This kind of system matches the reality well and can be extended to some other aspects.

For example, water quality can also be seen as a reflection of the Earth’s health. Changing the link and some of the inputs and outputs properly, with the autonomous mechanism, prediction can be made and the condition can be measured. In addition, our model can apply to some small ecosystems and biological system for the similarity of network structure. Moreover, we believe that the ubiquity of the model make it possible to help people make prediction in other domains.
