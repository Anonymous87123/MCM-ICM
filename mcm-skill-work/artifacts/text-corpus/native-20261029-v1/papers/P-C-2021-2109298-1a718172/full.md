# P-C-2021-2109298-1a718172

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | prose | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
2021

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | title | pages [1] -->
#2109298

<!-- b000007 | prose | pages [1] -->
MCM/ICM

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | heading | pages [1] -->
summary

<!-- b000010 | prose | pages [1] -->
The Asian giant hornet (AGH, Vespa mandarinia) is one of the largest hornet species in the world. Native to the Indomalayan region, AGH is a voracious predator of various insects, including honey bees. On September 19th, 2019, a nest of AGH was found outside of Vancouver. Although the nest

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
was destroyed onsite, a swarm of surviving hornets continue to roam through nearby areas, agitating signiﬁcant public anxiety. An invading AGH population in North America could disrupt biodiversity and threaten public health [8]. It is therefore an urgent task to contain the spread of AGH, where we identify three important objectives: estimate AGH population dynamics, build an eﬀective report classiﬁcation system, form a set of strategies to allocate hornet-controlling personnel.

<!-- b000013 | prose | pages [1] -->
We address the ﬁrst problem by building a powerful cellular automata (CA) model with a set of self-deﬁned update rules. We ﬁrst divide Washington State and its surrounding area into 2925 regions (or cells), each spanning an area of size 12km * 12km. To increase the accuracy of CA, we introduce an index that captures seasonal variation in the reproductive and active level of AGH and a suitability measure of each cell’s habitability for AGH. These indices then collectively determine update rules for CA. The simulation given by CA depicts the following invasion dynamics: 1) Strait of Georgia will prevent the spread of AGH colony to the west, speciﬁcally, to the Vancouver Island;

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
2) A proportion of AGH will ﬁrst move toward the east, and then head south, most likely entering the Okanogan-Wenatchee National Forest. 3) Another group of AGH will approach the border of Canada where the suitability index is high. In the long run, CA simulation indicates that AGH colony will mainly converge towards the National Forest region. To investigate the sensitivity of our model to initial conditions, we perturb several key parameters of CA. We then calculate the distance between output population distribution of diﬀerent initialization by Kullback-Leibler divergence metric, and construct a 95% conﬁdence interval of AGH population for each cell region at each time step. Results show that our CA model is insensitive to considerable change in parameters.

<!-- b000016 | prose | pages [1] -->
Civilian reports are vital for AGH containment. For textual data analysis, we apply Latent Dirichlet Allocation to extract crucial semantics from texts. Model output indicates that most textual data are unrelated to the classiﬁcation task at hand, thus they add little value to this investigation. For image data analysis, we construct a two-stage image classiﬁcation model based on a pre-trained VGG-11 architecture followed by an SVM classiﬁer. To deal with an extremely imbalanced dataset, we augment images with positive labels by rotation, cropping, and Gaussian blurring. We then train our model on image data from 2019-09-19 to 2020-05-15 and test it on 2020-05-15 and onwards, obtaining a mean testing accuracy of 90.2% and AUROC score of 94.4%. The model also proves robust under adversarial attacks. For regional information, we design a measure of regional report credibility over space and time, which is crucial in the Bayesian analysis that follows. We then feed a ﬁne-tuned version of the obtained quantities into a Naïve Bayes inference model that outputs the likelihood of correct classiﬁcation of a given report, and can thus be used to prioritize report processing.

<!-- b000017 | prose | pages [1] -->
To further improve our model, we design a reliable update routine for incoming reports. We draw insight from Baum-Welch algorithm and propose a novel Bayesian update method for our cellular automata. This method makes use of Monte Carlo Sampling to calculate posterior probability of diﬀerent sets of parameters, and can extract information out of both positive and negative report.

<!-- b000018 | prose | pages [1] -->
Finally, based on the prediction of CA and the update routine, we propose a set of rules to decide whether AGH are eradicated in Washington State. We also write a memo to the Washington State Department of Agriculture, addressing the severity of AGH invasion and provide suggestions on detecting AGH colonies and processing sighting reports.

<!-- b000019 | keywords | pages [1] -->
Key Words: cellula automata, Naïve Bayes inference, Baum-Welch algorithm, AUROC score

<!-- b000020 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000021 | furniture | pages [1] -->
关注数学模型

<!-- b000022 | furniture | pages [1] -->
2

<!-- b000023 | furniture | pages [1] -->
MATHmodels

<!-- b000024 | furniture | pages [1] -->
获取更多资讯

<!-- b000025 | furniture | pages [2] -->
Team #2109298

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
1

<!-- b000028 | heading | pages [2] -->
Introduction

<!-- b000029 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000030 | prose | pages [2] -->
3 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000031 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000032 | prose | pages [2] -->
Our Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000033 | prose | pages [2] -->
2

<!-- b000034 | heading | pages [2] -->
Global Assumptions

<!-- b000035 | prose | pages [2] -->
3 Data Exploration

<!-- b000036 | prose | pages [2] -->
4

<!-- b000037 | prose | pages [2] -->
4

<!-- b000038 | prose | pages [2] -->
4 Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 4 Textual Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 Geographical Data 6

<!-- b000039 | prose | pages [2] -->
Spread of AGH based on Cellular Automata 4 6 Deﬁning the Cellular Automata Model . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 6 Introduction and Motivation of CA 4.1.1 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | prose | pages [2] -->
6

<!-- b000041 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000042 | prose | pages [2] -->
Cells Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.2 6 Update Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.3 8 Parameters Setting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.4 10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Results and Analysis 10 Sensitivity Analysis of CA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3

<!-- b000043 | prose | pages [2] -->
5 Identiﬁcation of Mistaken Classiﬁcation

<!-- b000044 | prose | pages [2] -->
12

<!-- b000045 | prose | pages [2] -->
13 Plan of Attack Based on Naive Bayes Inference 5.1 . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | prose | pages [2] -->
14 Part II: Image Identiﬁcation (Estimating P(퐻|퐼)) 5.2 . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | prose | pages [2] -->
16 Data Augmentation and Model Construction 5.2.1 . . . . . . . . . . . . . . . . . .

<!-- b000048 | prose | pages [2] -->
16 Training and Testing Results . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.2 17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3 Estimating P(퐻|퐼) 18 Estimate 푞. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 Results and Analysis

<!-- b000049 | prose | pages [2] -->
6 Further Improvements

<!-- b000050 | prose | pages [2] -->
19

<!-- b000051 | prose | pages [2] -->
21 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Baum-Welch Update for CA 21 Evidence of Eradication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000052 | prose | pages [2] -->
7

<!-- b000053 | heading | pages [2] -->
Strengths and Weakness

<!-- b000054 | prose | pages [2] -->
8

<!-- b000055 | heading | pages [2] -->
Conclusions

<!-- b000056 | prose | pages [2] -->
9

<!-- b000057 | heading | pages [2] -->
Memo

<!-- b000058 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000059 | prose | pages [2] -->
22

<!-- b000060 | prose | pages [2] -->
22

<!-- b000061 | prose | pages [2] -->
23

<!-- b000062 | prose | pages [2] -->
24

<!-- b000063 | furniture | pages [2] -->
关注数学模型

<!-- b000064 | furniture | pages [2] -->
2

<!-- b000065 | furniture | pages [2] -->
MATHmodels

<!-- b000066 | furniture | pages [2] -->
获取更多资讯

<!-- b000067 | furniture | pages [3] -->
Team #2109298

<!-- b000068 | prose | pages [3] -->
1

<!-- b000069 | heading | pages [3] -->
Introduction

<!-- b000070 | prose | pages [3] -->
1.1 Restatement of the Problem

<!-- b000071 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000072 | furniture | pages [3] -->
Page 3 of 25

<!-- b000073 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000074 | prose | pages [3] -->
Vespa mandarinia, commonly known as the Asian Giant Hornet (AGH), is native to temperate and tropical eastern Asia [2] and widely feared as a species of ﬁerce predator of honey bees. In September 2019, a nest of AGH was discovered in Vancouver and later in Washington State, agitating signiﬁcant anxiety among civilians. In order to prevent AGH from wreaking havoc on local agriculture and economies, it is imperative to track down the dynamics of AGH population. Currently, state oﬃcials have collected a dataset of reports featuring public sightings of AGH. This is the starting point for our exploration, in which we need to meet the following requirements:

<!-- b000075 | prose | pages [3] -->
• a model to predict the spread of AGH in the Washington State.

<!-- b000076 | prose | pages [3] -->
• a model that helps interpret public reports, by diﬀerentiating correct classiﬁcation from mistaken ones.

<!-- b000077 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000078 | prose | pages [3] -->
• a strategy that prioritizes report investigation based on the probability to ﬁnd a real AGH given a particular report.

<!-- b000079 | prose | pages [3] -->
• a method that regularly updates our model and a criterion which indicates eradication of the AGH population in Washington State.

<!-- b000080 | caption | pages [3] -->
Figure 1: Model Framework

<!-- b000081 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000082 | furniture | pages [3] -->
关注数学模型

<!-- b000083 | furniture | pages [3] -->
2

<!-- b000084 | furniture | pages [3] -->
MATHmodels

<!-- b000085 | furniture | pages [3] -->
获取更多资讯

<!-- b000086 | furniture | pages [4] -->
Team #2109298

<!-- b000087 | prose | pages [4] -->
1.2 Our Approach

<!-- b000088 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000089 | furniture | pages [4] -->
Page 4 of 25

<!-- b000090 | prose | pages [4] -->
We propose a model framework as shown in Figure 1, consisting of two major components, the cellular automata (CA) model and the Naïve Bayes Model, with several processes that prepare the

<!-- b000091 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000092 | prose | pages [4] -->
given dataset into inputs for the main model. Cellula automata simulate the dynamics of AGH colony, whereas the Naïve Bayes Inference combine three quantities: the output distribution of cellula automata, the estimates of spatial and temporal distribution of public reports frequency and the likelihood of a true AGH report conditioned on the accompanying image data. The latter procedure allows us to provide a score for each report, which forms our strategy in allocating resources for report investigation. As an improvement to this framework, we also introduce the Baum-Welch algorithm to regularly update CA with each new observations. This would lead to more robust estimate given by CA.

<!-- b000093 | prose | pages [4] -->
2

<!-- b000094 | heading | pages [4] -->
Global Assumptions

<!-- b000095 | prose | pages [4] -->
In this section, we introduce the following global assumptions; assumptions speciﬁc to each model will

<!-- b000096 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000097 | prose | pages [4] -->
be stated and justiﬁed in their corresponding model introduction and setup.

<!-- b000098 | prose | pages [4] -->
Assumption 1 We assume every AGH individual is the same, disregarding the actual diﬀerence between the workers, queens, and drones.

<!-- b000099 | prose | pages [4] -->
Assumption 2 We assume all the AGH in the Washington State are introduced by the eﬀect of the ﬁrst colony discovered at Vancouver in Sep, 2019.

<!-- b000100 | prose | pages [4] -->
Assumption 3 We assume AGH is able to explore around its surrounding environments and tend to stay at a suitable location.

<!-- b000101 | prose | pages [4] -->
Assumption 4 We assume that all the geographical features and human footprint is uniform within each cell (geographical regions deﬁned in Section 4.1.2).

<!-- b000102 | prose | pages [4] -->
Assumption 5 We assume the reproduction and activity rate of AGH and other bees are seasonal; the trend is the same for every year.

<!-- b000103 | prose | pages [4] -->
3 Data Exploration

<!-- b000104 | prose | pages [4] -->
3.1 Data Cleaning

<!-- b000105 | prose | pages [4] -->
Examining thedataﬁles(2021MCMProblemC_DataSet.xlsx, 2021MCMProblemC_Images_by_Global ID.xlsx, 2021MCM_ProblemC_Files.rar), we ﬁnd the dataset contains all numerical, textual, and visual data. We merged the two excel tables based on the global ID; then, we drop the outliers and exception values, including 138 public reports before 2019 September since we are only concerned about the situation after the ﬁrst positive incidents. We also drop the submitted images with data type other than "*.jpg", since they are diﬃcult to process as pictures and their amount is insigniﬁcant. Some reports have up to 11 images, while some has none. We keep both kinds of reports and handle them diﬀerently in Section 5.

<!-- b000106 | prose | pages [4] -->
3.2 Textual Data

<!-- b000107 | prose | pages [4] -->
To gain statistical insights into the textual data, we proceed by ﬁrst preprocessing it. We extract the "Notes" and "Lab Comments" columns from the data frame, and drop rows with null values due to a

<!-- b000108 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000109 | furniture | pages [4] -->
关注数学模型

<!-- b000110 | furniture | pages [4] -->
2

<!-- b000111 | furniture | pages [4] -->
MATHmodels

<!-- b000112 | furniture | pages [4] -->
获取更多资讯

<!-- b000113 | furniture | pages [5] -->
Team #2109298

<!-- b000114 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000115 | furniture | pages [5] -->
Page 5 of 25

<!-- b000116 | prose | pages [5] -->
lack of methods to interpolate strings. Next, We use the python nltk package to tokenize all sentences into lowercase words. Spaces, punctuations, and stopwords are removed. We also lemmatize each word to restore it back to its original forms.

<!-- b000117 | prose | pages [5] -->
Since there are numerous notes and lab comments that are grammatically and semantically com-

<!-- b000118 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000119 | prose | pages [5] -->
plicated, we want to extract the main topics from the notes and comments to identify whether the information are valuable to our main model. To do this, we apply the Latent Dirichlet Allocation

<!-- b000120 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000121 | prose | pages [5] -->
(a) LDA model for notes from public reports

<!-- b000122 | prose | pages [5] -->
(c) word-cloud of notes from public reports

<!-- b000123 | prose | pages [5] -->
(b) LDA model for lab comments

<!-- b000124 | prose | pages [5] -->
(d) word-cloud of lab comments

<!-- b000125 | caption | pages [5] -->
Figure 2: Results of the LDA topic model

<!-- b000126 | prose | pages [5] -->
(LDA) model [3], capable of extracting topics and keywords from texts. Using gensim, a standard NLP package in python, we obtain the results from the LDA model and visualize them with pyLDAvis package, which are shown in Figure 2a and 2b. In those ﬁgures, each circle represents a topic, and it is clearly shown that those topics have few intersections, so they are mostly unrelated. To get a more intuitive understanding, we plot the word-cloud for the two sets of texts in Figure 2c and 2d.

<!-- b000127 | prose | pages [5] -->
Most frequent words from public reports include "found", "hornet", and "bee", which fail to identify

<!-- b000128 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000129 | furniture | pages [5] -->
关注数学模型

<!-- b000130 | furniture | pages [5] -->
2

<!-- b000131 | furniture | pages [5] -->
MATHmodels

<!-- b000132 | furniture | pages [5] -->
获取更多资讯

<!-- b000133 | furniture | pages [6] -->
Team #2109298

<!-- b000134 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000135 | furniture | pages [6] -->
Page 6 of 25

<!-- b000136 | prose | pages [6] -->
a set of unique characteristics of AGH. Other less frequent words are also generic and vague. There is even one note that reads "scared the hell out of me". As for the lab comments, although some speciﬁc species of bees diﬀerent from AGH have been pinpointed, like "golden digger", "horntail sawﬂy", and "cicada killer", this information is useless for image identiﬁcation in Section 5.2 since we are mainly

<!-- b000137 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000138 | prose | pages [6] -->
interested in a binary classiﬁcation between AGH and non-AGH. Considering all the analysis above, we conclude that the textual part of the dataset will not play a big role in our model.

<!-- b000139 | prose | pages [6] -->
3.3 Geographical Data

<!-- b000140 | prose | pages [6] -->
In order to achieve optimal data visualization eﬀect, we have researched some background geographical information on the regions involved. All data presentation on maps are plotted using the built-in functions in Tableau, a data visualization software which helps us correspond the longitude-latitude coordinates to the locations on the map.

<!-- b000141 | prose | pages [6] -->
Spread of AGH based on Cellular Automata 4

<!-- b000142 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000143 | heading | pages [6] -->
Deﬁning the Cellular Automata Model

<!-- b000144 | prose | pages [6] -->
4.1

<!-- b000145 | prose | pages [6] -->
4.1.1

<!-- b000146 | heading | pages [6] -->
Introduction and Motivation of CA

<!-- b000147 | prose | pages [6] -->
In order to predict the spread of AGH in Washington State, we utilize cellular automata(CA), a widely used dynamic model capable of modeling biological spread and evolution of complex systems. It contains discrete grids called cells. Each cell records biological and sociological features as well as the magnitude of AGH populations in the region it occupies. In addition, cells will be updated according to a set of pre-deﬁned rules.

<!-- b000148 | prose | pages [6] -->
CA is chosen for this task because of the following reasons:

<!-- b000149 | prose | pages [6] -->
• With only a few initial values (as we have restricted to one starting location of the AGH invasion), CA can simulate the spread after many time steps.

<!-- b000150 | prose | pages [6] -->
• The future spread of AGH depends solely on the evolution in the past, while the update of each state depends only on the current state – a desirable Markov property.

<!-- b000151 | prose | pages [6] -->
• The self-deﬁned rules admit ﬂexibility: they allow us to use biological information to simulate the interaction of AGH with its surrounding environments at diﬀerent time step (speciﬁcally, winter and summer).

<!-- b000152 | prose | pages [6] -->
4.1.2 Cells Setup

<!-- b000153 | prose | pages [6] -->
In our CA, each cell is represented by a square geographical region. To avoid boundary cases, we look for the maximum and minimum latitude and longitude of the given reports and extend this range by 20% as the boundary condition, between (45.09°N, 49.95°N) and (−124.65°W, −116.87°W). Theoretically, the more cells, the more precise our model will be. With the maximum computational cost in mind, we set the size of each cell to be 12 km * 12 km, with 45 * 65 = 2925 cells in total.

<!-- b000154 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000155 | furniture | pages [6] -->
关注数学模型

<!-- b000156 | furniture | pages [6] -->
2

<!-- b000157 | furniture | pages [6] -->
MATHmodels

<!-- b000158 | furniture | pages [6] -->
获取更多资讯

<!-- b000159 | furniture | pages [7] -->
Team #2109298

<!-- b000160 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000161 | furniture | pages [7] -->
Page 7 of 25

<!-- b000162 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000163 | caption | pages [7] -->
Figure 3: The geographical region selected

<!-- b000164 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000165 | prose | pages [7] -->
At each time step, each cell records a single value – the expected number of AGH inside the region – which will later be propagated through the automaton based on a set of rules. The distribution of values across all cells forms our estimation of the distribution of AGH colonies throughout Washington State.

<!-- b000166 | prose | pages [7] -->
To accurately simulate AGH behaviours and predict their spread, regional biological characteristics Habitat suitability is a crucial driver of species migration, for each are also vital in our model. individual tends to settle down and reproduce in more habitable environments. To capture this feature, we introduce the AGH Habitat Suitability Index Matrix, 푆, to all regions, which ensembles human footprint and geographic barriers:

<!-- b000167 | prose | pages [7] -->
(1) 푆= −푙표푔(푃) + 퐵,

<!-- b000168 | prose | pages [7] -->
where 푃is the human population distribution matrix and 퐵is a matrix depicting geographic barriers. The −푙표푔(푃) term captures the idea that human activities reduce suitability of habitats for animals. Matrix 퐵seek to locate areas that are neither suitable for human nor for AGH. If a region is inhabitable, the corresponding entry in B has value 0; if a region is not inhabitable (e.g., ocean), the entry in B has value −∞.

<!-- b000169 | prose | pages [7] -->
Besides human footprint and geographical barriers, many other regional factors also inﬂuence species distribution in general (e.g., climate, food resources). Yet, none of them can be drawn from the data provided. Speciﬁcally, human population data is also not provided. Thus, we design a novel model to estimate human population distribution 푃based on accessible statistics.

<!-- b000170 | prose | pages [7] -->
Analysing Human Population from submitted reports Among the 4389 sightings provided, only 14 are identiﬁed as positive; the remaining sightings are either mistaken or unidentiﬁed, many of which even lack meaningful descriptions and feedback. These unveriﬁed and negative sightings provide us with little information about the distribution of AGH. Yet, they contain rich information about the distribution of human population.

<!-- b000171 | prose | pages [7] -->
Since only 0.3% sightings are positive, it is reasonable to assume the public do not possess knowledge to diﬀerentiate AGH from other similar bees; their frequent negative reports of AGH sightings more directly reﬂect their anxiety of an AGH invasion rather than the actual presence of

<!-- b000172 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000173 | furniture | pages [7] -->
关注数学模型

<!-- b000174 | furniture | pages [7] -->
2

<!-- b000175 | furniture | pages [7] -->
MATHmodels

<!-- b000176 | furniture | pages [7] -->
获取更多资讯

<!-- b000177 | furniture | pages [8] -->
Team #2109298

<!-- b000178 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000179 | furniture | pages [8] -->
Page 8 of 25

<!-- b000180 | prose | pages [8] -->
any AGH. This assumption leads to the conclusion that, in the regions where AGH population is insigniﬁcant, the number of reports correlates strongly with the amount of people concerned about the AGH invasion issue. The latter quantity can be assumed to be proportional to the regional population, hence we derive the conclusion proposed. As we draw all the sightings on 4a, we ﬁnd that regions with

<!-- b000181 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000182 | prose | pages [8] -->
frequent reports are often located in large cities, further proving our conclusion.

<!-- b000183 | prose | pages [8] -->
Thus, we can ﬁt the human population distribution by the following formula:

<!-- b000184 | prose | pages [8] -->
Õ

<!-- b000185 | prose | pages [8] -->
푃(푥, 푦) =

<!-- b000186 | prose | pages [8] -->
(푟푥,푟푦)∈푅

<!-- b000187 | prose | pages [8] -->
(푥−푟푥)2+(푦−푟푦)2

<!-- b000188 | prose | pages [8] -->
1

<!-- b000189 | prose | pages [8] -->
푒−

<!-- b000190 | prose | pages [8] -->
2휎2

<!-- b000191 | prose | pages [8] -->
√

<!-- b000192 | prose | pages [8] -->
(2)

<!-- b000193 | prose | pages [8] -->
2휋휎

<!-- b000194 | prose | pages [8] -->
where 푅is the set of coordinates of reports given by the dataset, (푟푥, 푟푦) is the location of a report, and 휎is a parameter that one can tune. We have used a Gaussian distribution to capture the inﬂuence of (or the posterior information carried by) a point mass of population on the total distribution of population.

<!-- b000195 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000196 | prose | pages [8] -->
(a) report distribution (c) population statistics (b) population distribution

<!-- b000197 | prose | pages [8] -->
After ﬁtting, we roughly compared our population distribution with the major cities and geographical features in Washington State. Our distribution successfully indicates the location of Vancouver, Seattle, Portland, the chain of three large cities in the west, occupied by large population. It also manages to identify the location of Spokane and Kennewick, two major cities in the east and the south. In our population distribution, the middle-south of the state is especially empty.

<!-- b000198 | prose | pages [8] -->
This phenomenon corresponds well with the Yakama Indian Reservation, which locates on the east side of the Cascade Mountains in southern Washington, where the population is sparse. Therefore, we draw conclusion that the population distribution obtained from report is suﬃciently accurate.

<!-- b000199 | prose | pages [8] -->
4.1.3 Update Rules

<!-- b000200 | prose | pages [8] -->
To best predict the dynamics of AGH population, we design a set of suitable rules for CA in accordance with reality. The simulation initializes at the Paciﬁc Northwest where the ﬁrst 5 positive sightings occurred. At a given time step 푡, if a given region is occupied by AGH, its adjacent regions are likely to be visited by the species in the next time step 푡+ 훿푡, and if suitable for AGH reproduction, become occupied. This transition behaviour can be modelled by Moore-type cells [6], where each cell interacts with the eight adjacent cells as shown in Figure 5. Speciﬁcally, considering hornets movements are continuous, we use cells where 푑= 1.

<!-- b000201 | prose | pages [8] -->
Biological studies of AGH indicate that the hornets exhibit two sets of distinct action patterns in a given year. In summer [2], AGH participate in active reproduction and various other activities including In winter, worker AGH hornets decease and overwintering queens conﬁne scouting and hunting. themselves to a small region, and remain inactive until spring arrives. Based on this fact, we design two

<!-- b000202 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000203 | furniture | pages [8] -->
关注数学模型

<!-- b000204 | furniture | pages [8] -->
2

<!-- b000205 | furniture | pages [8] -->
MATHmodels

<!-- b000206 | furniture | pages [8] -->
获取更多资讯

<!-- b000207 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000208 | furniture | pages [9] -->
Team #2109298

<!-- b000209 | furniture | pages [9] -->
Page 9 of 25

<!-- b000210 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000211 | caption | pages [9] -->
Figure 5: The Moore neighborhood (red) of the blue cell, d = 1. [6]

<!-- b000212 | prose | pages [9] -->
sets of CA update rules, corresponding to summer and winter activity respectively. In summer, AGH enlarges in population based on a reproduction rate 푟푠푢푚푚푒푟, while nearby cells communicate more frequently with an active level 푎푠푢푚푚푒푟. In winter, the population of AGH diminishes with rate 푟푤푖푛푡푒푟, while the surviving hornets remain inactive in their region with an active level 푎푤푖푛푡푒푟. Regardless of season, any given AGH is more likely to move into nearby cell with larger suitability index. The complete cell update procedure is shown in Figure 6.

<!-- b000213 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000214 | caption | pages [9] -->
Figure 6: Cell update procedure

<!-- b000215 | prose | pages [9] -->
Using the above set of parameters, we now propose the transition formula of a single cell 퐶푐푢푟. For each neighbors of 퐶푐푢푟in the automaton (denoted by 퐶푎푑푗), the transition probability from 퐶푐푢푟to 퐶푎푑푗 is 푇푐푢푟,푎푑푗, where

<!-- b000216 | prose | pages [9] -->
푇푐푢푟,푎푑푗= softmax(푆푎푑푗) × 푎.

<!-- b000217 | prose | pages [9] -->
(3)

<!-- b000218 | prose | pages [9] -->
푎is one of 푎푠푢푚푚푒푟and 푎푤푖푛푡푒푟depending on time, the softmax function is utilized to normalize the weight of transition probability with respect to adjacent cells:

<!-- b000219 | prose | pages [9] -->
푒푆푎푑푗−푆푐푢푟 softmax(푆푎푑푗) =

<!-- b000220 | prose | pages [9] -->
(4) 퐶푎푑푗푒푆푎푑푗−푆푐푢푟

<!-- b000221 | prose | pages [9] -->
Í

<!-- b000222 | prose | pages [9] -->
where the summation is over the (2푑+ 1) × (2푑+ 1) Moore cells centered at 퐶푐푢푟. Note that this formula includes the case 퐶푎푑푗= 퐶푐푢푟. This means if AGH ﬁnds a suitable place (e.g., a region with local maximal suitability index) for nesting, it is likely that they will stay there and stop migrating. Thus, it is reasonable to consider 퐶푐푢푟itself as an adjacent cell.

<!-- b000223 | prose | pages [9] -->
Besides exploring around within a short distance, it is also vital to consider the dispersal of AGH over long distance. This phenomenon is always caused by hitchhiking on human activity [1]. Although

<!-- b000224 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000225 | furniture | pages [9] -->
关注数学模型

<!-- b000226 | furniture | pages [9] -->
2

<!-- b000227 | furniture | pages [9] -->
MATHmodels

<!-- b000228 | furniture | pages [9] -->
获取更多资讯

<!-- b000229 | furniture | pages [10] -->
Team #2109298

<!-- b000230 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000231 | furniture | pages [10] -->
Page 10 of 25

<!-- b000232 | prose | pages [10] -->
the possibility is small, this passive dispersal process is the major cause of many species invasions. Thus, in our CA, we also add a small transition probability that a small group of AGH can be carried away to further cells.

<!-- b000233 | prose | pages [10] -->
The states of all cells are updated concurrently. Let the state of a cell 퐶푐푢푟at this moment be

<!-- b000234 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000235 | prose | pages [10] -->
푁푐푢푟(푡). We obtain the next state 푁푐푢푟(푡+ 1) for all cells by three steps. First, we perform the AGH reproduction step:

<!-- b000236 | prose | pages [10] -->
(5) 푁푐푢푟(푡) = 푁푐푢푟(푡) × 푟.

<!-- b000237 | prose | pages [10] -->
where 푟is one of 푟푠푢푚푚푒푟and 푟푤푖푛푡푒푟depending on the current time step. Then, each cell is updated according to its activity degree. This accounts for the AGH that still stays inside its previous cell:

<!-- b000238 | prose | pages [10] -->
푁푐푢푟(푡+ 1) = 푁푐푢푟(푡) × (1 −푎).

<!-- b000239 | prose | pages [10] -->
(6)

<!-- b000240 | prose | pages [10] -->
Finally, we simulate the interaction of AGH with its surroundings using the transition probability 푇푐푢푟,푎푑푗:

<!-- b000241 | prose | pages [10] -->
푁푎푑푗(푡+ 1) := 푁푎푑푗(푡+ 1) + 푁푐푢푟(푡+ 1) × 푇푐푢푟,푎푑푗.

<!-- b000242 | prose | pages [10] -->
(7)

<!-- b000243 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000244 | prose | pages [10] -->
where := means updating the value on the left by one on the right. In addition, we have to speciﬁcally take care of the situation at the boundaries of our cells. For the North, South, and East boundaries, we assume the AGH will never go back once it has gone out, since those AGH would continue moving at those directions if all the cells outside the boundaries are just the same as the ones on the boundaries. As for the west boundary, the presence of the sea is handled by the suitability index.

<!-- b000245 | prose | pages [10] -->
4.1.4 Parameters Setting

<!-- b000246 | prose | pages [10] -->
To better simulate the reality, we use biological background information to set our parameters. The behavior of AGH is signiﬁcantly diﬀerent between fall and winter, and spring and summer. Since the ﬁrst outbreak of the AGH is in September, we deﬁne fall and winter as months from September to February, and spring and summer from March to August.

<!-- b000247 | prose | pages [10] -->
We interpret each consecutive time steps 훿푡as one day, meaning the one CA update represents the behaviour of AGH in one day. Since the AGH can ﬂy up to 100 km in a single day [2], it is reasonable to assume its daily activity range is about 10-20 km when optimizing location for nesting, roughly the size of a cell. Also, this value is adjusted according to the activity degree 푎during diﬀerent time of the year. In our model, we set 푎푠푢푚푚푒푟= 0.3, 푎푤푖푛푡푒푟= 0.1.

<!-- b000248 | prose | pages [10] -->
According to information in [2], we simulate the life cycles of AGH by setting diﬀerent reproduction rate 푟for diﬀerent seasons. We set 푟푠푢푚푚푒푟= 1.05, corresponding to the fact that the peak of a new AGH colony is roughly triple of its initial amount at the beginning of the year; then, we set 푟푤푖푛푡푒푟= 0.995, so that the AGH workers and unfertilized queens (roughly two thirds of the total population) all eventually die during fall and winter.

<!-- b000249 | prose | pages [10] -->
The initial conditions are also crucial to the result of CA. As we have few data about the real distribution of the AGH, we set the cell of the ﬁrst incident of the AGH as our initial location, and September as the initial time. We set the initial AGH colony to be 1000.

<!-- b000250 | prose | pages [10] -->
4.2

<!-- b000251 | heading | pages [10] -->
Results and Analysis

<!-- b000252 | prose | pages [10] -->
Using the set parameters, we simulate the AGH colony evolution for 10 years, and the result is shown in Figure 9. We examine both short-term (within two years) trends and long-term trends (over ﬁve

<!-- b000253 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000254 | furniture | pages [10] -->
关注数学模型

<!-- b000255 | furniture | pages [10] -->
2

<!-- b000256 | furniture | pages [10] -->
MATHmodels

<!-- b000257 | furniture | pages [10] -->
获取更多资讯

<!-- b000258 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000259 | furniture | pages [11] -->
Team #2109298

<!-- b000260 | furniture | pages [11] -->
Page 11 of 25

<!-- b000261 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000262 | caption | pages [11] -->
Figure 7: Population of British Columbia [7]

<!-- b000263 | caption | pages [11] -->
Figure 8: Growth of total AGH population

<!-- b000264 | prose | pages [11] -->
years). Figure 9a to 9c is the evolution from 2019/09 to 2020/7. The AGH colony starts from cells around Vancouver, and we assume the initial AGH colony size is 1000, an estimate for at least the size of one nest. Comparing with the human population distribution of each cell shown in Figure 4b, we

<!-- b000265 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000266 | prose | pages [11] -->
summarize characteristics of the simulation and the reasons as the following:

<!-- b000267 | prose | pages [11] -->
• The presence of the Strait of Georgia constricts the spread of AGH colony to the west.

<!-- b000268 | prose | pages [11] -->
• The main trend of the AGH colony is toward the north and east, where the low population density leads to a high suitability index.

<!-- b000269 | prose | pages [11] -->
• A proportion of AGH passes through the northern boundary of our cells, entering Canada, where we cannot model precisely due to lack of data. However, this will not signiﬁcantly inﬂuence our simulation of the AGH spread in the Washington State, since the Canadian province adjacent to Washington state is British Columbia, whose main population is densely centered at Vancouver and the rest are mostly mountains and forests, as shown in Figure 7. So by our rules the AGH would indeed tend to spread in this direction.

<!-- b000270 | prose | pages [11] -->
• Another proportion of the AGH colony moves toward east ﬁrst, then spread to the south, mean- while avoiding the high population cells along the Interstate 5 (I-5), the main highway on the west coast of the US. The AGH colonies toward the south are smaller than those toward the north, due to the fact that the suitability index is very high in the north.

<!-- b000271 | prose | pages [11] -->
• Over the ﬁrst year, the AGH is still centered around Vancouver, matching the pattern we see from the public reports: almost all the reports are from places very close to the initial start.

<!-- b000272 | prose | pages [11] -->
As for the long-term spread of the AGH colony, the results are shown from Figure 9d to 9e. After ﬁve years (t=1800), the AGH colony spreads further into the south and is seperated into two branches, mainly along the national parks consisting of mountains and forests. After ten years (t=3600), the dynamic of the AGH colony is stabilized. The distribution of the AGH colony will not be changed signiﬁcantly any more, and it is only the absolute number of the AGH that increases. The total AGH population is shown in Figure 8, where the growth shows an oscillating exponential growth, reaching 10000 in the summmer 10 years later. If we were to model the quantity of AGH after 10 years, we could just use the spatial distribution at year 10 and model the temporal changes through logistic equations. We overlapped the human population distribution (the blue regions) with the AGH distribution result

<!-- b000273 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000274 | furniture | pages [11] -->
关注数学模型

<!-- b000275 | furniture | pages [11] -->
2

<!-- b000276 | furniture | pages [11] -->
MATHmodels

<!-- b000277 | furniture | pages [11] -->
获取更多资讯

<!-- b000278 | furniture | pages [12] -->
Team #2109298

<!-- b000279 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000280 | furniture | pages [12] -->
Page 12 of 25

<!-- b000281 | prose | pages [12] -->
together in Figure 9e. The two distributions complement each other, reﬂecting our assumption that the AGH tends to move to places with fewer humans. From our results, we notice that the Giﬀord Pinchot National Forest will become the cluster of future AGH colony, and special care and precautions should be taken.

<!-- b000282 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000283 | prose | pages [12] -->
(a) t=150 (c) t=600 (b) t=300

<!-- b000284 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000285 | prose | pages [12] -->
(d) t=1800 (e) t=3600 (overlapped with human population)

<!-- b000286 | caption | pages [12] -->
Figure 9: Results of the CA model

<!-- b000287 | prose | pages [12] -->
4.3

<!-- b000288 | heading | pages [12] -->
Sensitivity Analysis of CA

<!-- b000289 | prose | pages [12] -->
As there are various parameters associated with CA that is tunable, including the initial distribution of AGH population, the suitability index of each region, and size of the grid, it is critical that we assess the sensitivity of CA with respect to each of them. We will randomly perturb one set of parameters each time, implement CA evolution and evaluate the level of variation in model outputs: distribution of hornet population over space and time.

<!-- b000290 | prose | pages [12] -->
We ﬁrst investigate sensitivity with respect to suitability values. Note that by perturbing suitability, we adjust both our beliefs in a region’s habitability and the set of transition probabilities applied during updates. At each initialization, we perturb each suitability value by multiplying a Gaussian random variable with mean 1 and variance 휎2 = 0.2. At a selected time step, we compare 2 sets of initialization by calculating the Kullback-Leibler (KL) divergence distance between the probability distributions of AGH population associated with each initialization, the end result is displayed in Figure 10. Then, for

<!-- b000291 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000292 | furniture | pages [12] -->
关注数学模型

<!-- b000293 | furniture | pages [12] -->
2

<!-- b000294 | furniture | pages [12] -->
MATHmodels

<!-- b000295 | furniture | pages [12] -->
获取更多资讯

<!-- b000296 | furniture | pages [13] -->
Team #2109298

<!-- b000297 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000298 | furniture | pages [13] -->
Page 13 of 25

<!-- b000299 | prose | pages [13] -->
each region at a selected time step, we constructs a 95% conﬁdence interval of CA-predicted population upon multiple random initializations. This statistics is summarized in Figure 11.

<!-- b000300 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000301 | prose | pages [13] -->
(a) 300-th time step (b) 600-th time step (c) 1800-th time step (d) 3600-th time step

<!-- b000302 | caption | pages [13] -->
Figure 10: We sample 9 diﬀerent possible initial distributions of AGH population, simulate population

<!-- b000303 | prose | pages [13] -->
dynamics and record AGH population distribution for each initialization at 4 diﬀerent time steps (300, 600, 1800, 3600). We then calculate the Kullback-Leibler (KL) divergence distance between any pair of initializations.

<!-- b000304 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000305 | prose | pages [13] -->
(a) 150-th time step (b) 600-th time step (c) 1800-th time step (d) 3600-th time step

<!-- b000306 | caption | pages [13] -->
Figure 11: We sample 9 diﬀerent possible initial distributions of AGH population, and at a certain time

<!-- b000307 | prose | pages [13] -->
step record 9 sets of probability for a single region. These 9 values provide a conﬁdence interval for each of the region at a certain time step. We plot the distribution of the longest 100 95% conﬁdence intervals.

<!-- b000308 | prose | pages [13] -->
We then investigate sensitivity with respect to initial distribution. Again, we ﬁrst compare the spatial distribution of AGH population by KL divergence metric in Figure 12. Then, we select a number of particular regions to evaluate the dispersion of population value predicted by several initialization, which then provides a 95% conﬁdence interval of the actual population in the region in Figure 13. Result shows that our model is robust against disturbance, and the 95% conﬁdent interval tends to become even smaller as the evolution continues.

<!-- b000309 | prose | pages [13] -->
Identiﬁcation of Mistaken Classiﬁcation 5

<!-- b000310 | prose | pages [13] -->
In this section we aim to calculate the the likelihood of a mistaken sighting 푠in a certain grid 푟at time 푡. This likelihood consists of multiple contributing factors, including hornet distribution at time 푡, the frequency at which reports are ﬁled in the region 푟and the information conveyed by the images/texts data accompanying the report. To combine these three factors, we proceed in a step-by-step fashion.

<!-- b000311 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000312 | furniture | pages [13] -->
关注数学模型

<!-- b000313 | furniture | pages [13] -->
2

<!-- b000314 | furniture | pages [13] -->
MATHmodels

<!-- b000315 | furniture | pages [13] -->
获取更多资讯

<!-- b000316 | furniture | pages [14] -->
Team #2109298

<!-- b000317 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000318 | furniture | pages [14] -->
Page 14 of 25

<!-- b000319 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000320 | prose | pages [14] -->
(a) 150-th time step (b) 600-th time step (c) 1800-th time step (d) 3600-th time step

<!-- b000321 | caption | pages [14] -->
Figure 12: We sample 9 diﬀerent possible initial distributions of AGH population, simulate population

<!-- b000322 | prose | pages [14] -->
dynamics and record population distribution of each initialization at 4 diﬀerent time steps. We then calculate the Kullback-Leibler (KL) divergence between AGH probability distributions of any pair of initializations.

<!-- b000323 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000324 | prose | pages [14] -->
(b) 600-th time step (a) 150-th time step (d) 3600-th time step (c) 1800-th time step

<!-- b000325 | caption | pages [14] -->
Figure 13: We sample 9 diﬀerent possible initial distributions of AGH population, and at a certain

<!-- b000326 | prose | pages [14] -->
time step record 9 sets of probability for a single region. These 9 values provide a conﬁdence interval for each of the region at a certain time step. We plot a histogram recording the longest 100 95% conﬁdence intervals.

<!-- b000327 | prose | pages [14] -->
Plan of Attack Based on Naive Bayes Inference 5.1

<!-- b000328 | prose | pages [14] -->
Given a sighting of a creature which may or may not be an AGH in a particular region 푟at time 푡we denote the probability event as follows:

<!-- b000329 | prose | pages [14] -->
• R: the event that the sighting seen is reported

<!-- b000330 | prose | pages [14] -->
• H: the event that the sighting is associated with an AGH

<!-- b000331 | prose | pages [14] -->
• I: the event that a particular set of image and text (could be empty) information is included in the report

<!-- b000332 | prose | pages [14] -->
We are interested in the quantity 1 −P(퐻|푅, 퐼) as this is the probability that a report mistakenly identiﬁes an AGH. By conditional Bayes Theorem we yield:

<!-- b000333 | prose | pages [14] -->
If in the report information such as image and text is given, it is then the case that 푅∩퐼= 퐼and we have:

<!-- b000334 | prose | pages [14] -->
P(퐻|푅, 퐼) = P(푅|퐻, 퐼)P(퐻|퐼)

<!-- b000335 | prose | pages [14] -->
P(푅|퐼)

<!-- b000336 | prose | pages [14] -->
(8)

<!-- b000337 | prose | pages [14] -->
= P(퐻|퐼)

<!-- b000338 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000339 | furniture | pages [14] -->
关注数学模型

<!-- b000340 | furniture | pages [14] -->
2

<!-- b000341 | furniture | pages [14] -->
MATHmodels

<!-- b000342 | furniture | pages [14] -->
获取更多资讯

<!-- b000343 | furniture | pages [15] -->
Team #2109298

<!-- b000344 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000345 | furniture | pages [15] -->
Page 15 of 25

<!-- b000346 | prose | pages [15] -->
Note that in the process we assume that P(푅|퐻, 퐼) = 1 because AGH is visually intimidating and upon sighting, a person always chooses to report the dangerous-looking species to local authority. If no image or useful text information is given, we instead get:

<!-- b000347 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000348 | prose | pages [15] -->
P(퐻|푅, 퐼) = P(퐻|푅)

<!-- b000349 | prose | pages [15] -->
= P(푅|퐻)P(퐻)

<!-- b000350 | prose | pages [15] -->
P(푅)

<!-- b000351 | prose | pages [15] -->
=

<!-- b000352 | prose | pages [15] -->
(9)

<!-- b000353 | prose | pages [15] -->
P(푅|퐻)P(퐻) P(푅|퐻)P(퐻) + P(푅|퐻푐)P(퐻푐)

<!-- b000354 | prose | pages [15] -->
= P(퐻) P(퐻) + P(푅|퐻푐)(1 −P(퐻))

<!-- b000355 | prose | pages [15] -->
where 퐻푐is the complement of the probability event 퐻.

<!-- b000356 | prose | pages [15] -->
We also used the assumption that P(푅|퐻) = 1 due to the same reason given in the ﬁrst derivation. It is also safe to assume here that P(퐻) ≪1 due to the rareness of discovering an escaping AGH demonstrated by the dataset and based on common sense. Rewriting Equation 9 yields:

<!-- b000357 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000358 | prose | pages [15] -->
P(퐻|푅, 퐼) =

<!-- b000359 | prose | pages [15] -->
≈

<!-- b000360 | prose | pages [15] -->
=

<!-- b000361 | prose | pages [15] -->
P(퐻) 1−P(퐻) P(퐻) 1−P(퐻) + P(푅|퐻푐)

<!-- b000362 | prose | pages [15] -->
푝

<!-- b000363 | prose | pages [15] -->
(10)

<!-- b000364 | prose | pages [15] -->
푀 푝 푝 푀+ P(푅|퐻푐)

<!-- b000365 | prose | pages [15] -->
푝 푝+ 푞

<!-- b000366 | prose | pages [15] -->
where 푝is the expected amount of AGH population in 푟at time 푡, 푀is the expected amount of reported bug sightings in 푟at time 푡and 푞= P(푅|퐻푐)푀.

<!-- b000367 | prose | pages [15] -->
Note that the above calculations provide two sets of probabilities for mistaken classiﬁcation, one based on the image and text involved, the other does not. It is then left for us to estimate the quantities involved in Equation 8 and 10. In particular, the remaining parts of the section will be dedicated to estimating each quantity, in particular:

<!-- b000368 | prose | pages [15] -->
• 푝: this is calculated by the distribution of AGH population simulated by CA in Section 4.2.

<!-- b000369 | prose | pages [15] -->
• P(퐻|퐼): this will be calculated as a result of the image classiﬁcation task and text sentiment analysis probability in Section 5.2. Since we have concluded in 3.2 that textual data provides little to no information for classiﬁcation purposes, we rely mainly on images in this approximation.

<!-- b000370 | prose | pages [15] -->
• 푞: this is quantity will be ﬁtted based on existing report number given in the dataset.

<!-- b000371 | prose | pages [15] -->
This would also solve the third question we post in the beginning, asking for a strategy to deploy hornet hunters. In fact, at region 푟at time 푡, we give 푟a score 푠which is deﬁned as the maximum probability of correct identiﬁcation across all reports in 푟at 푡.

<!-- b000372 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000373 | furniture | pages [15] -->
关注数学模型

<!-- b000374 | furniture | pages [15] -->
2

<!-- b000375 | furniture | pages [15] -->
MATHmodels

<!-- b000376 | furniture | pages [15] -->
获取更多资讯

<!-- b000377 | furniture | pages [16] -->
Team #2109298

<!-- b000378 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000379 | furniture | pages [16] -->
Page 16 of 25

<!-- b000380 | prose | pages [16] -->
Part II: Image Identiﬁcation (Estimating P(퐻|퐼)) 5.2

<!-- b000381 | prose | pages [16] -->
Upon exploring the image dataset given, we notice a strong imbalance between positive training data (13 images in total) and negative training data. We construct a two-stage image classiﬁcation based on

<!-- b000382 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000383 | prose | pages [16] -->
a pretrained VGG-11 architecture followed by a SVM classiﬁer. We also utilized data augmentation technique to improve model generalization ability.

<!-- b000384 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000385 | caption | pages [16] -->
Figure 14: VGG-11 + SVM pipeline for image classiﬁcation

<!-- b000386 | heading | pages [16] -->
Data Augmentation and Model Construction

<!-- b000387 | prose | pages [16] -->
5.2.1

<!-- b000388 | prose | pages [16] -->
To attain better generalization, we ﬁrst augment the given positive ID images using transformations including: rotation, Gaussian blurring, cropping and aﬃne shifting, all of which have corresponding implementations in the Pytorch library. We also make sure that all such obtained images contain visible AGH. This process addresses the problem of lacking positive labeled data, and signiﬁcantly increases the accuracy of our Machine Learning model. A particular example of such augmentation is given below.

<!-- b000389 | prose | pages [16] -->
By augmentation, we are able to extend the original 13 data images to a total of 87. Then, we propose a two-stage pipeline consisting of a dimension reduction treatment followed by a classiﬁer. There are many alternatives for both parts of the model – we survey PCA analysis and various pretrained image encoding models on large image classiﬁcation tasks for dimension reduction techniques; we always implemented K-Nearest Neighbour (kNN) and Support Vector Machine (SVM) for robust classiﬁer under heavily imbalanced datasets. By cross examining several models, we decide on a VGG-11 + SVM model pipeline which achieves desirable performance under both the mean accuracy and AUROC metric, the latter we will thoroughly introduce later.

<!-- b000390 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000391 | furniture | pages [16] -->
关注数学模型

<!-- b000392 | furniture | pages [16] -->
2

<!-- b000393 | furniture | pages [16] -->
MATHmodels

<!-- b000394 | furniture | pages [16] -->
获取更多资讯

<!-- b000395 | furniture | pages [17] -->
Team #2109298

<!-- b000396 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000397 | furniture | pages [17] -->
Page 17 of 25

<!-- b000398 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000399 | prose | pages [17] -->
(a) Original Image (b) Cropped Image (d) Rotated Image (c) Aﬃne-Transform Image

<!-- b000400 | caption | pages [17] -->
Figure 15: Examples of data augmentation results.

<!-- b000401 | prose | pages [17] -->
Mean Accuracy Model Pipeline VGG16-bn + k-NN VGG11-bn + k-NN VGG16-bn + SVM VGG11-bn + SVM AUROC Score 77.1% 84.3% 84.1% 92.1% 90.3% 94.4% 90.2% 95.4%

<!-- b000402 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000403 | caption | pages [17] -->
Table 1: Accuracy and AUROC score of various model pipeline designs. Each row is composed of

<!-- b000404 | prose | pages [17] -->
two probability score, the ﬁrst is mean accuracy on test dataset, and the second term records AUROC score.

<!-- b000405 | prose | pages [17] -->
5.2.2

<!-- b000406 | heading | pages [17] -->
Training and Testing Results

<!-- b000407 | prose | pages [17] -->
To further enhance the reliability of our testings and capability of our model, we split all images by "before and after a certain moment", and conduct all testings strictly based on time.

<!-- b000408 | prose | pages [17] -->
For training, we select all image data from 2019-09-19 to 2020-05-15 as training dataset, consisting in total of 60 images corresponding to positive ID and 300 images corresponding to negative ID. Upon conducting compression via VGG-11 network, we couple each feature vector with its corresponding label and train a SVM model using the Python sklearn package.

<!-- b000409 | prose | pages [17] -->
For testing, we select all image data from 2019-05-16 to 2020-10-01 as testing dataset, consisting in total of 27 images corresponding to positive ID and remaining 500 corresponding to negative ID. We record both test accuracy and AUROC score in Table 1. AUROC (Area Under ROC Curve) score is an evaluation metric that captures model prediction accuracy under imbalanced inference dataset scenarios. Given an unbalanced test dataset 푇, the ROC curve is created by plotting the true positive rate (TPR) of the trained model in 푇against the false positive rate (FPR) at various threshold settings. AUROC is calculated by ﬁnding the area under the ROC curve, which is typically a value between 0 and 1. Higher AUROC indicates better predictive ability.

<!-- b000410 | prose | pages [17] -->
We also test the robustness of our model under Adversarial Attacks. We use mainly the images of European hornets and Eastern cicada killers (Sphecius speciosus) which are visually similar to AGH according to [2]. The images are also collected from [2]. We display one such images in Figure 16.

<!-- b000411 | prose | pages [17] -->
Our model successfully classiﬁes both European hornets and Sphecius speciosus as negative ID, an illustration of our model’s accuracy in the adversarial regime.

<!-- b000412 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000413 | furniture | pages [17] -->
关注数学模型

<!-- b000414 | furniture | pages [17] -->
2

<!-- b000415 | furniture | pages [17] -->
MATHmodels

<!-- b000416 | furniture | pages [17] -->
获取更多资讯

<!-- b000417 | furniture | pages [18] -->
Team #2109298

<!-- b000418 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000419 | furniture | pages [18] -->
Page 18 of 25

<!-- b000420 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000421 | caption | pages [18] -->
Figure 16: European Hornet: Highly similar to AGH in appearance.

<!-- b000422 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000423 | prose | pages [18] -->
Estimating P(퐻|퐼) 5.2.3

<!-- b000424 | prose | pages [18] -->
At time 푡, given a report in region 푟equipped with image data 퐼, a trained classiﬁer takes in the image/images, and for each image 푖provides a probability 푝푖that 푖identiﬁes an AGH. The prob- ability calculation of an SVM classiﬁer is implemented using the ’predict_proba’ function in the sklearn.svm.SVC package. If a single image is provided, we simply uses the probability given by the classiﬁer. If multiple images are given, we take the maximum of all 푝푖, 푖∈퐼. This concludes our method of approximation.

<!-- b000425 | prose | pages [18] -->
Estimate 푞 5.3

<!-- b000426 | prose | pages [18] -->
푞= P(푅|퐻푐)푀is a quantity in the formula for the probability of mistaken sighting, 푞is not related to AGH distribution at all, but represents "the likelihood of a false report appearing in certain regions", The meaning of P(푅|퐻푐) in other words, the "discredibility" of the report from certain regions. component is: the probability of a person reporting an insect other than AGH upon seeing it. Though this quantity largely varies among person to person, it doesn’t correlate with region or time. Therefore, it is reasonable to assume the average P(푅|퐻푐) is constant in all regions. Next, we also need a regional quantity 푀푟, denoting the expected bug sightings in a region. This quantity, together with the universal constant P(푅|퐻푐), calculates 푞in a given region, thus directly relates to discredibility.

<!-- b000427 | prose | pages [18] -->
The ideal way to obtain 푀푟is to draw from historical report frequency. Higher frequency in the past implies larger 푀푟, and lower historical frequency implies lower 푀푟. Due to the lack of data points in many regions, we again apply Gaussian Distribution to approximate geographic information carried by each report:

<!-- b000428 | prose | pages [18] -->
Õ

<!-- b000429 | prose | pages [18] -->
푀푟=

<!-- b000430 | prose | pages [18] -->
(푟푥,푟푦)∈푅

<!-- b000431 | prose | pages [18] -->
(푥−푟푥)2+(푦−푟푦)2

<!-- b000432 | prose | pages [18] -->
1

<!-- b000433 | prose | pages [18] -->
푒−

<!-- b000434 | prose | pages [18] -->
2휎2

<!-- b000435 | prose | pages [18] -->
√ √

<!-- b000436 | prose | pages [18] -->
(11)

<!-- b000437 | prose | pages [18] -->
2휋휎

<!-- b000438 | prose | pages [18] -->
where (푟푥, 푟푦) is the location of a historical report and (x, y) is the center of region 푟. Fitting in this way, we can obtain 푀for each region, representing the discredibility of the report from certain region.

<!-- b000439 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000440 | furniture | pages [18] -->
关注数学模型

<!-- b000441 | furniture | pages [18] -->
2

<!-- b000442 | furniture | pages [18] -->
MATHmodels

<!-- b000443 | furniture | pages [18] -->
获取更多资讯

<!-- b000444 | furniture | pages [19] -->
Team #2109298

<!-- b000445 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000446 | furniture | pages [19] -->
Page 19 of 25

<!-- b000447 | prose | pages [19] -->
While 푀푟addresses the discredibility distribution among space, it is also noticeable that the frequency of reports vary dramatically among seasons. Speciﬁcally, in some regions, the frequency of reports in summer could be 20 times larger than in winter, resulting in credibility of reports in summer and winter. This phenomenon generally correspond with the general activity and reproduction

<!-- b000448 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000449 | prose | pages [19] -->
patterns of insects. To address this seasonal inﬂuence, we deﬁne another quantity, 푁(푡), that captures the seasonal change of report amounts in time.

<!-- b000450 | prose | pages [19] -->
Since the pattern of insect activity can be seen as a periodic function, we applied a simple trigono- metric function, combined with ReLU function, to ﬁt this pattern:

<!-- b000451 | prose | pages [19] -->
푁(푡) = 푅푒퐿푈(푝sin(푞푡+ 푟) + 푐) (12)

<!-- b000452 | prose | pages [19] -->
where t denotes the number of months on a year, and N(t) is the predicted number of reports found in that month. We implemented the ﬁtting process by Sklearn and obtained the following result:

<!-- b000453 | prose | pages [19] -->
푝= −0.18054375, 푞= 0.53359878, 푟= 7.07317231, 푐= 0.04970395 (13)

<!-- b000454 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000455 | caption | pages [19] -->
Figure 17: Prediction curve of request distribution in time

<!-- b000456 | prose | pages [19] -->
Finally, we superpose the spatial discredibility distribution 푀푟and the seasonal request periodic function, we can obtain the spatial-time credibility index, 푀(푟), that comprehensively evaluate the discredibility of a request from spatial and time perspective. Given a report , we can obtain 푞푟by the following formula:

<!-- b000457 | prose | pages [19] -->
(14) 푞푟= 푀(푟) = 푀푟∗푁(푡푟)

<!-- b000458 | prose | pages [19] -->
5.4

<!-- b000459 | heading | pages [19] -->
Results and Analysis

<!-- b000460 | prose | pages [19] -->
Using various estimates given in the previous sections, we evaluate two probabilities given a report:

<!-- b000461 | prose | pages [19] -->
푝 푝+푞when image data is P(푅|퐻, 퐼) = P(퐻|퐼) when image data accompanies the report, and P(푅|퐻) = not provided. Notice that even if some images is provided in a report, the quality of the image might be doubtful due to human-induced corruptions. Therefore, we consider both probabilities when image 푝 data is provided. In addition, as argued in the previous section, we need to modify P(푅|퐻) as 푝+푐푞, where 푐is a tunable parameter. We apply Maximum Likelihood Estimation (MLE) of 푐using historic data to maximise the quantity:

<!-- b000462 | prose | pages [19] -->
Õ

<!-- b000463 | prose | pages [19] -->
log

<!-- b000464 | prose | pages [19] -->
log(P(data|푝, 푞)) =

<!-- b000465 | prose | pages [19] -->
(푟,푡)∈Pos

<!-- b000466 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000467 | prose | pages [19] -->
푝(푡)

<!-- b000468 | prose | pages [19] -->
푐푞(푡)

<!-- b000469 | prose | pages [19] -->
푟

<!-- b000470 | prose | pages [19] -->
푟

<!-- b000471 | prose | pages [19] -->
Õ

<!-- b000472 | prose | pages [19] -->
log

<!-- b000473 | prose | pages [19] -->
(15)

<!-- b000474 | prose | pages [19] -->
+

<!-- b000475 | prose | pages [19] -->
푝(푡)

<!-- b000476 | prose | pages [19] -->
+ 푐푞(푡)

<!-- b000477 | prose | pages [19] -->
푝(푡)

<!-- b000478 | prose | pages [19] -->
+ 푐푞(푡)

<!-- b000479 | prose | pages [19] -->
푟 푟

<!-- b000480 | prose | pages [19] -->
푟

<!-- b000481 | prose | pages [19] -->
푟

<!-- b000482 | prose | pages [19] -->
푟

<!-- b000483 | prose | pages [19] -->
(푟,푡)∈Neg

<!-- b000484 | furniture | pages [19] -->
关注数学模型

<!-- b000485 | furniture | pages [19] -->
2

<!-- b000486 | furniture | pages [19] -->
MATHmodels

<!-- b000487 | furniture | pages [19] -->
获取更多资讯

<!-- b000488 | furniture | pages [20] -->
Team #2109298

<!-- b000489 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000490 | furniture | pages [20] -->
Page 20 of 25

<!-- b000491 | prose | pages [20] -->
Note the sum is over all positive identiﬁcation reports and all negative identiﬁcation reports, indexed by region 푟and time step 푡. 푝(푡)

<!-- b000492 | prose | pages [20] -->
푟and 푞(푡)

<!-- b000493 | prose | pages [20] -->
푟are estimates of 푝and 푞in the region 푟at time 푡. Diﬀerentiating right hand side and set it equal to zero, we obtain 푐≈0.05990657. The variance of 푐depends on the

<!-- b000494 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000495 | prose | pages [20] -->
variance of estimates of 푝, 푞. Since there is no explicit way of writing 푐in terms of 푝, 푞, we convince ourselves that 푐is a reasonably accurate estimate as 푝, 푞have small variance as shown previously.

<!-- b000496 | prose | pages [20] -->
After obtaining the scaling factor 푐, we calculate probabilities derived from image and Bayesian inference for each report starting from 2019-05-16 to 2020-10-01, note this is in accordance with the testing set we used in Section 5.2. We ﬁrst provide some summary statistics of the two sets of probabilities for negative reports and positive reports respectively in Table 2.

<!-- b000497 | prose | pages [20] -->
Mean probability without image 15% / 5% probability conditioned on image 10.4% / 4% Standard Deviation 25% percentile 75% percentile 0.15 / 0.1 8.8% / 0.05% 16.6% / 2% 0.1 / 0.09 1% / 0.4% 10% / 2%

<!-- b000498 | caption | pages [20] -->
Table 2: Bayesian probability of positive report with no visual knowledge and probability of positive

<!-- b000499 | prose | pages [20] -->
reports conditioned on images for positive and negative classes of reports given in the dataset. Each

<!-- b000500 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000501 | prose | pages [20] -->
entry is of the form pos% / neg% corresponding to positive reports and negative reports.

<!-- b000502 | prose | pages [20] -->
We observe that probability without image diﬀerentiates positive reports from their negative coun- terparts better than pure image classiﬁcation. We attribute this to a lack of training example for image classiﬁcation task and a lack of visibility of images provided by civilians. We also notice that Bayesian probability without visual clues becomes less performant as time moves on. This is most likely the result of a lack of updates in cellular automata designed in Section 4. We address this problem in the Section 6. We also design and evaluate strategies based on two sets of probabilities: each strategy

<!-- b000503 | prose | pages [20] -->
(a) tuning alpha (b) performance on test set

<!-- b000504 | caption | pages [20] -->
Figure 18: We tune 훼to achieve best performance on training datset, and validate it on test dataset.

<!-- b000505 | prose | pages [20] -->
can be parametrized by 푎∈[0, 1], which weights of two probabilities: Bayesian probability P푏푎푦푒푠 without image information and P푖푚푎푔푒conditioned on image. Given a report with image, we calculate a credibility score of the report by 푎P푏푎푦푒푠+ (1 −푎)P푖푚푎푔푒. Given a report without image data, we calculate a credibility score by P푏푎푦푒푠. At each time step, we sort all report scores in decreasing order, and then prioritize reports with higher marks. In fact, each report can then be given a normalized

<!-- b000506 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000507 | furniture | pages [20] -->
关注数学模型

<!-- b000508 | furniture | pages [20] -->
2

<!-- b000509 | furniture | pages [20] -->
MATHmodels

<!-- b000510 | furniture | pages [20] -->
获取更多资讯

<!-- b000511 | furniture | pages [21] -->
Team #2109298

<!-- b000512 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000513 | furniture | pages [21] -->
Page 21 of 25

<!-- b000514 | prose | pages [21] -->
probability score. We can then vary threshold for verifying the report from 0 to 1 while recording false positive and true negative rates. The imbalanced nature of the dataset again allows us to evaluate model performance, by the AUROC metric. We chooses dataset from 2020-05-16 to 2020-08-13 as training dataset for tuning 푎, and remaining dataset from 2020-08-13 to 2020-10-01 as testing dataset.

<!-- b000515 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000516 | prose | pages [21] -->
AUROC for train set and test set is summarized in Figure 18.

<!-- b000517 | prose | pages [21] -->
It could be concluded that as a sound strategy, we could assign a value for each report using the weighting scheme with parameter 푎= 0.1. This is a reasonable parameter as the image encompasses more uncertainty and the model used for inference based on images is not as robust as CA. Given the score, government oﬃcials could then deploy personnel to deal with possible AGH sightings associated with the reports. Good luck!

<!-- b000518 | prose | pages [21] -->
6 Further Improvements

<!-- b000519 | prose | pages [21] -->
6.1 Baum-Welch Update for CA

<!-- b000520 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000521 | prose | pages [21] -->
Although previously described models produce fruitful results in report classiﬁcation, a reliable update routine for our Cellular Automata is yet to be designed. We draw insights from Baum Welch algorithm, a model commonly used to estimate the parameters of a Hidden Markov Model given a set of observations. In the scenario we are working with, the transition of bees can be modelled by a Markov Process, whose parameter is unknown. However, we observe a series of reports, some of which are designated as successfully identifying AGH. Taken together, one can describe the setup as a hidden Markov Model tracing the travel of AGH, as well as a Bernoulli random variable with parameter depending on the quantities given in Section 5.3, that generates a series of report in some regions. Recognising this similarity, we propose a novel paradigm that seeks to update the parameters of CA using fresh observations.

<!-- b000522 | prose | pages [21] -->
Recall that in the previous section, a set of transition rules for CA depends on the setting of a suitability measure for each region given. At each initialization of CA, the suitability measure is drawn from a prior distribution 푝(푆) of suitability values for each region, and the model evolves based on the drawn set of parameters. Once we encounter an observation 표푡at time 푡, we need to update the prior by a posterior probability distribution given by:

<!-- b000523 | prose | pages [21] -->
P(푆= 푠|표푡) = P(표푡|푆= 푠)P(푆= 푠)

<!-- b000524 | prose | pages [21] -->
P(표푡) P(표푡|푆= 푠)P(푆= 푠)

<!-- b000525 | prose | pages [21] -->
(16)

<!-- b000526 | prose | pages [21] -->
=

<!-- b000527 | prose | pages [21] -->
P(표푡|푆= 푠)P(푆= 푠)푑푠

<!-- b000528 | prose | pages [21] -->
∫

<!-- b000529 | prose | pages [21] -->
We could approximate the intractable integral in Equation 16 by Monte Carlo sampling.

<!-- b000530 | prose | pages [21] -->
In fact, following [5], we propose the following procedure for Bayesian update, which is termed sequential importance resampling (SIR) in the article:

<!-- b000531 | prose | pages [21] -->
• Step 1: Draw 푁unique samples from the initial probability distribution 푝(푠), suppose the unique samples are {푠1, ..., 푠푁} with corresponding probability 푝푖= P(푆= 푠푖), 푖= 1, ..., 푁;

<!-- b000532 | prose | pages [21] -->
• Step 2: Evolve the model for a ﬁxed time step 푡, collect all reports that are ﬁled during this period, denote this collection 표푡. Calculate P(표푡|푆= 푠푖) for each 푠푖, 푖= 1, .., 푁. Update 푝푖to 푝′

<!-- b000533 | prose | pages [21] -->
푖

<!-- b000534 | prose | pages [21] -->
푗= P(표푡|푠푖)푝푖/P(표푡|푠푗)푝푗for any 푖, 푗.

<!-- b000535 | prose | pages [21] -->
such that 푝′

<!-- b000536 | prose | pages [21] -->
푖/푝′

<!-- b000537 | prose | pages [21] -->
• Step 3: iterate this process until the next time step and make similar updates.

<!-- b000538 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000539 | furniture | pages [21] -->
关注数学模型

<!-- b000540 | furniture | pages [21] -->
2

<!-- b000541 | furniture | pages [21] -->
MATHmodels

<!-- b000542 | furniture | pages [21] -->
获取更多资讯

<!-- b000543 | furniture | pages [22] -->
Team #2109298

<!-- b000544 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000545 | furniture | pages [22] -->
Page 22 of 25

<!-- b000546 | prose | pages [22] -->
This procedure is reminiscent of the forward-backward algorithm given in the Baum-Welch algo- rithm. We also attempted to update probability transition matrix based on observed data using B-W algorithm. Yet, due to the lack of observations and sparseness of the correlation matrix, the update is unsuccessful. However, in the SIR model we described, we have implicitly conducted this forward-

<!-- b000547 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000548 | prose | pages [22] -->
backward propagation directly on the initial distribution of transition probability, without needing to calculate the intermediary steps described in the Baum-Welch algorithm.

<!-- b000549 | prose | pages [22] -->
We believe that this framework allows for frequent updates based on fresh observations. However, due to computation restrictions our model is not implemented fully, but based on preliminary results, this routine is more robust to temporal changes, and provide useful information on species eradication discussed in the following section.

<!-- b000550 | prose | pages [22] -->
6.2 Evidence of Eradication

<!-- b000551 | prose | pages [22] -->
With the above-described update routine, our CA model is able to utilize all report information and simulate the distribution of AGH stably in the long term, so it is a reasonable metric to predict

<!-- b000552 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000553 | prose | pages [22] -->
eradication. Based on scientiﬁc features of AGH and our CA model, we propose the following set of rules to determine whether AGH eradicates in Washington State:

<!-- b000554 | prose | pages [22] -->
• If the most recent positive sighting occurred later than last winter, then there’s no sign of eradication.

<!-- b000555 | prose | pages [22] -->
Explanation: Due to recent studies [4], AGH tends to spread rapidly and has much higher reproduction rate in summer. Thus, it’s highly unlikely that a AGH colony is spotted but die out before winter.

<!-- b000556 | prose | pages [22] -->
• If the most recent positive sighting occurred before last winter, we run the updated CA model for one more year, and examine the resulting distribution.

<!-- b000557 | prose | pages [22] -->
– If result indicates that AGH population will ﬂuctuate or increase, then there’s no sign of

<!-- b000558 | prose | pages [22] -->
eradication.

<!-- b000559 | prose | pages [22] -->
– If result indicates that AGH population will diminish steadily, then AGH will possibly die

<!-- b000560 | prose | pages [22] -->
out in Washington State during the next year.

<!-- b000561 | prose | pages [22] -->
• No conclusion should be drawn before long-term observation and thorough detection. Especially, previous CA simulation results suggest it is highly likely that AGH establishes colonies in the national park or Reservation, where human contacts are rare. Thus, we should always actively detect these regions before claiming eradication.

<!-- b000562 | prose | pages [22] -->
7

<!-- b000563 | heading | pages [22] -->
Strengths and Weakness

<!-- b000564 | heading | pages [22] -->
Strengths:

<!-- b000565 | prose | pages [22] -->
• Our model is robust under the sensitivity tests, indicating that small change in parameters won’t lead to huge diﬀerences in results.

<!-- b000566 | prose | pages [22] -->
• Using the Bayesian theorem, we convert a complex probability into independently calculable parts obtained through CA, image classiﬁer, and the spatial-time credibility index.

<!-- b000567 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000568 | furniture | pages [22] -->
关注数学模型

<!-- b000569 | furniture | pages [22] -->
2

<!-- b000570 | furniture | pages [22] -->
MATHmodels

<!-- b000571 | furniture | pages [22] -->
获取更多资讯

<!-- b000572 | furniture | pages [23] -->
Team #2109298

<!-- b000573 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000574 | furniture | pages [23] -->
Page 23 of 25

<!-- b000575 | prose | pages [23] -->
• In every procedures relating to data, we take special care of the small and unbalanced dataset in this problem. For example, our image classiﬁer uses pre-trained model ﬁne-tuned by our augmented training set.

<!-- b000576 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000577 | prose | pages [23] -->
• Using the Baum-Welch algorithm, we improve the traditional cellular automata by enabling it to carry the future information and go back in time to re-evolve.

<!-- b000578 | heading | pages [23] -->
Weakness:

<!-- b000579 | prose | pages [23] -->
• Due to the constraints on dataset, there are many data that we could have considered in our CA model to get a better measurement of the suitability index for simulation, such as the direct data of population distribution, the temperature, altitude, topography.

<!-- b000580 | prose | pages [23] -->
• The long-term prediction of our model may not be precise enough, considering the fact that we don’t have long-term data to validate the long-term predictions.

<!-- b000581 | prose | pages [23] -->
• To simplify our model, we have made some assumptions that are not close enough to the reality,

<!-- b000582 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000583 | prose | pages [23] -->
which would also lead to errors in the results.

<!-- b000584 | prose | pages [23] -->
8

<!-- b000585 | heading | pages [23] -->
Conclusions

<!-- b000586 | prose | pages [23] -->
In this paper, we build a comprehensive model to simulate the evolution of AGH population in Wash- ington State. This model is achieved by considering the inﬂuence of human population, geographical barriers, AGH activity patterns, and AGH dispersal methods into a powerful Cellular Automaton model that propagates the expected number of AGH in each region. Human population distribution is ob- tained by ﬁtting the spatial density function of sighting reports. Our CA model is far diﬀerent from a typical one, since it gives each cell great freedom to decide the transformation procedure and involves stochasticity to ensure accuracy. Based on the result, we analyzed the short-term patterns of AGH dynamics, and gave prediction to the long-term distribution and population as well. We also prove the robustness of our model by sensitivity tests.

<!-- b000587 | prose | pages [23] -->
Then, we consider the textual, visual, and regional information provided by each report, in hope of building a superposed model to evaluate the likelihood of positive reports. First, by topic correlation analysis, we found that texts’ topics are diverse and unrelated, hardly contribute to our classiﬁcation. Secondly, we build a VGG + SVM model to perform image classiﬁcation, with several techniques to deal with unbalanced data. Thirdly, we manage to ﬁnd a regional distribution and time distribution of "report credibility". Finally, we use a Bayes Model to combine all factors and achieved a model to evaluate reports. Based on the score outputted, we are able to assign an optical detection strategy.

<!-- b000588 | prose | pages [23] -->
We also come up with a method to update the state of CA by positive and negative reports. This method is done by rewinding the cells by certain steps, adjust the transformation parameters, and evolve back to the current state. The update method allows us to make the maximum use of all detection results, and keep the result of our CA accurate for a longer period of time. In addition, we designed a step-wise process to determine eradication, and wrote a memo to the Washington State Department of Agriculture, with the best hope of helping them control the invasion of AGH.

<!-- b000589 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000590 | furniture | pages [23] -->
关注数学模型

<!-- b000591 | furniture | pages [23] -->
2

<!-- b000592 | furniture | pages [23] -->
MATHmodels

<!-- b000593 | furniture | pages [23] -->
获取更多资讯

<!-- b000594 | furniture | pages [24] -->
Team #2109298

<!-- b000595 | prose | pages [24] -->
9

<!-- b000596 | heading | pages [24] -->
Memo

<!-- b000597 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000598 | furniture | pages [24] -->
Page 24 of 25

<!-- b000599 | prose | pages [24] -->
To: Washington State Department of Agriculture From: MCM Team #2109298

<!-- b000600 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000601 | prose | pages [24] -->
Date: Feb 8th, 2021 Subject: Strategies to deal with the Asian Giant Hornet

<!-- b000602 | prose | pages [24] -->
Dear Oﬃcer of the Department of Agriculture,

<!-- b000603 | prose | pages [24] -->
Please be alarmed! In order to address the newly found Asian Giant Hornet (AGH) around and within your State, we have modeled the dynamics of AGH and successfully simulated its trends for the next decade. We have also analyzed all historical public reports of sightings, with which we built a model to prioritize future reports and decide whether the State should spend eﬀorts investigating each one.

<!-- b000604 | prose | pages [24] -->
First of all, unfortunately, we have to tell you that the current situation is not optimistic: At least two incidents of positive AGH sightings are recorded: one in September 2019, and the other in March 2020. This means that some AGH individuals have successfully overcome the winter in Washington States.

<!-- b000605 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000606 | prose | pages [24] -->
Those individuals are highly likely to be fertilized queens that have nested in the spring of 2020. Based on this initial information, our model predicted that the total number of AGH will ﬂuctuate around its initial value 1000 for the ﬁrst ﬁve years. Even though the number won’t change signiﬁcantly, our model indicates that AGH are actively ﬁnding suitable locations to stay and grow. Once they have found some suitable locations, they will reside and grow exponentially, which will only reach a limit when the local honeybees are eaten out so that the environment is no longer suitable for the AGH. Based on multiple simulations of our model, we estimate the "ﬁnding" process will take up about 8 years. After that, the population will start to grow exponentially, reaching 10,000 in the 10th year. As for the dynamics, our model predicts that AGH colonies will move from Vancouver to the north ﬁrst, with some portion of the AGH entering Canada, and the rest spread gradually toward the south along places with little human activity. Several locations the AGH may eventually converge at are listed below (ordered by severity):

<!-- b000607 | prose | pages [24] -->
region severity Giﬀord Pincohot National Forest 193.01 Mount Rainier Natinoal Park 153.17 Yakama Indian Reservation 144.25 Granby Provincial Park 120.62 North Casacades National Park 51.26

<!-- b000608 | prose | pages [24] -->
Special cautions should be taken with respect to these locations before the AGH colony gets uncontrollably large in these regions.

<!-- b000609 | prose | pages [24] -->
Next, our model combined these predictions of AGH population distribution and the information from each report to help prioritize the State’s resources. Our model assigns a score for each report, and based on the level of resources available, we recommend diﬀerent strategies. This is accomplished by changing the threshold value in the model, which you can adjust by yourself according to the current resource availability.

<!-- b000610 | prose | pages [24] -->
• High level: Immediately investigate every report whose score is higher than the threshold value.

<!-- b000611 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000612 | furniture | pages [24] -->
关注数学模型

<!-- b000613 | furniture | pages [24] -->
2

<!-- b000614 | furniture | pages [24] -->
MATHmodels

<!-- b000615 | furniture | pages [24] -->
获取更多资讯

<!-- b000616 | furniture | pages [25] -->
Team #2109298

<!-- b000617 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000618 | furniture | pages [25] -->
Page 25 of 25

<!-- b000619 | prose | pages [25] -->
• Low level: For every period of report accumulations (e.g a month’s reports), investigate reports that are close in space.

<!-- b000620 | prose | pages [25] -->
In addition, to further increase the accuracy of our model and reduce human labour, please encourage

<!-- b000621 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000622 | prose | pages [25] -->
the public to submit their report with clear photos of the hornets. In this way, our image classiﬁer can get more and more proﬁcient (current accuracy is 90%), and they can exclude some reports directly, without the need to be processed by human labour.

<!-- b000623 | prose | pages [25] -->
Last but not least, don’t just regard the AGH is dieing out based on short-term observations or predictions. Please remember the criterion of eradication of AGH: If the most recent positive sighting occurred before last winter, run the updated CA model for one more year and examine the result. If result indicates that AGH population will diminish steadily, then AGH will possibly die our in Wash- ington State during the next year. No conclusion should be drawn before long-term observation and thorough detection.

<!-- b000624 | prose | pages [25] -->
Best, MCM Team #2109298

<!-- b000625 | prose | pages [25] -->
微信号：MATHmodels

<!-- b000626 | heading | pages [25] -->
References

<!-- b000627 | references | pages [25] -->
Robin Engler, Wim Hordĳk, and Antoine Guisan. “The MIGCLIM R package–seamless integra-

<!-- b000628 | references | pages [25] -->
[1]

<!-- b000629 | references | pages [25] -->
tion of dispersal constraints into projections of species distribution models”. In: Ecography 35.10

<!-- b000630 | references | pages [25] -->
(2012), pp. 872–878.

<!-- b000631 | references | pages [25] -->
Penn State Extension. “Asian Giant Hornets”. In: https://extension.psu.edu/asian-giant-hornets

<!-- b000632 | references | pages [25] -->
[2]

<!-- b000633 | references | pages [25] -->
(2020).

<!-- b000634 | references | pages [25] -->
Shashank Kapadia. Topic Modeling in Python: Latent Dirichlet Allocation (LDA). url: https:

<!-- b000635 | references | pages [25] -->
[3]

<!-- b000636 | references | pages [25] -->
//towardsdatascience.com/end- to- end- topic- modeling- in- python- latent-

<!-- b000637 | references | pages [25] -->
dirichlet-allocation-lda-35ce4ed6b3e0.

<!-- b000638 | references | pages [25] -->
Claudia Nuñez-Penichet et al. “Geographic potential of the world’s largest hornet, Vespa man-

<!-- b000639 | references | pages [25] -->
[4]

<!-- b000640 | references | pages [25] -->
darinia Smith (Hymenoptera: Vespidae), worldwide and particularly in North America”. In: PeerJ

<!-- b000641 | references | pages [25] -->
9 (2021), e10690.

<!-- b000642 | references | pages [25] -->
Judith A. Verstegen et al. “Identifying a land use change cellular automaton by Bayesian data

<!-- b000643 | references | pages [25] -->
[5]

<!-- b000644 | references | pages [25] -->
assimilation”. In: Environmental Modelling Software 53 (2014), pp. 121–136. issn: 1364-8152.

<!-- b000645 | references | pages [25] -->
doi: https://doi.org/10.1016/j.envsoft.2013.11.009. url: https://www.

<!-- b000646 | references | pages [25] -->
sciencedirect.com/science/article/pii/S1364815213002909.

<!-- b000647 | references | pages [25] -->
Wikipedia. Cellular automaton. url: https : / / en . wikipedia . org / wiki / Cellular _

<!-- b000648 | references | pages [25] -->
[6]

<!-- b000649 | references | pages [25] -->
automaton.

<!-- b000650 | references | pages [25] -->
Wikipedia. File:Canada British Columbia Density 2016.png. [Online; accessed Feb 8, 2021].

<!-- b000651 | references | pages [25] -->
[7]

<!-- b000652 | references | pages [25] -->
2016. url: https://en.wikipedia.org/wiki/File:Canada_British_Columbia_

<!-- b000653 | references | pages [25] -->
Density_2016.png.

<!-- b000654 | references | pages [25] -->
Aya Yanagawa, Fumio Yokohari, and Susumu Shimizu. “Defense mechanism of the termite, Cop-

<!-- b000655 | references | pages [25] -->
[8]

<!-- b000656 | references | pages [25] -->
totermes formosanus Shiraki, to entomopathogenic fungi”. In: Journal of invertebrate pathology

<!-- b000657 | references | pages [25] -->
97.2 (2008), pp. 165–170.

<!-- b000658 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000659 | furniture | pages [25] -->
关注数学模型

<!-- b000660 | furniture | pages [25] -->
2

<!-- b000661 | furniture | pages [25] -->
MATHmodels

<!-- b000662 | furniture | pages [25] -->
获取更多资讯
