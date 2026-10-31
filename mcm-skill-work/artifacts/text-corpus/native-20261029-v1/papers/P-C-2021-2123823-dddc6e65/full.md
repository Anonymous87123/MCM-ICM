# P-C-2021-2123823-dddc6e65

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | furniture | pages [1] -->
2021

<!-- b000003 | prose | pages [1] -->
Problem Chosen

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | furniture | pages [1] -->
2123823

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
Trace the Buzz:

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | title | pages [1] -->
A Comprehensive Study on the Reports About Hornets

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
With the fast rise of trade and tourism, invasive species have become a global concern. This paper aims to help the government make full use of the public reports to rationalize the deployment of limited resources to conduct investigations into the sparrow hornet.

<!-- b000014 | prose | pages [1] -->
For Problem (a), to predict the spread of the sparrow hornet, we construct a Combined Forecast Model. From the spatial perspective, factor analysis is used for variable selection (see Table 4.1) to measure the environmental suitability in a speciﬁed area. From the temporal perspective, we use K-means clustering on the three types of sightings (positive, unveriﬁed,

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
unprocessed) in diﬀerent months. The Gaussian mixture model (GMM) is applied to calculate the likelihood distribution of sparrow hornets in diﬀerent months. The combination of the two models illustrates the spread trend of hornets. The results show that Vs is less than 0.1 throughout the period, indicating our model’s high precision.

<!-- b000017 | prose | pages [1] -->
For Problem (b), we aim to predict the likelihood of misclassiﬁcation. First, we construct a Convolutional Neural Network (CNN) for image recognition and then carry out the text mining with an improved tf-idf model. Finally, we combine them for better estimation. The CNN predicts very well while the text mining can tell us the relative likelihood. After we combine these two methods, AUC(a measure of accuracy) increases by 1.08%.

<!-- b000018 | prose | pages [1] -->
For Problem (c), to prioritize investigation of the positive reports, we establish a compre- hensive model by combining the two models in Problem (a) and Problem (b), which is based on Regularized Logistic Regression. As a result of this model, we give more comprehensive judgments, with more than 99% accuracy.

<!-- b000019 | prose | pages [1] -->
For Problem (d), to update our model with new reports, pseudo labelling is introduced to utilize the unused (new) data. Compared with the result without pseudo labelling, AUC has increased to 0.96 by 2.13%. In terms of the appropriate update frequency, we use the subjective evaluation method to score each area based on ﬁve factors. Finally, we calculate the reporting frequency of a speciﬁc area based on its objective conditions and ﬁnd that the highest number of reports occurs in July and August (5.2/month).

<!-- b000020 | prose | pages [1] -->
For Problem (e), to determine the evidence of eradication in Washington, we use the regression model with longitudinal data to modify the model in Problem (a). The improved model’s advantage lies in its ability to predict changes in species populations with human intervention. We select local bee and sparrow hornet populations in 20 areas as samples. The state between two extreme points of the population curves indicates the eradication evidence.

<!-- b000021 | prose | pages [1] -->
At the very last, we analyze the strengths and weaknesses of our model as well as its sensitivity, whose results show that our model has high robustness, precision and accuracy. After that, a memo is attached.

<!-- b000022 | keywords | pages [1] -->
Keywords: Environmental suitability; K-means clustering; CNN; Text mining; Pseudo la-

<!-- b000023 | prose | pages [1] -->
belling; Regression model with longitudinal data

<!-- b000024 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000025 | prose | pages [1] -->
关注数学模型

<!-- b000026 | furniture | pages [1] -->
2

<!-- b000027 | furniture | pages [1] -->
MATHmodels

<!-- b000028 | furniture | pages [1] -->
获取更多资讯

<!-- b000029 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000030 | heading | pages [2] -->
Contents

<!-- b000031 | contents | pages [2] -->
1

<!-- b000032 | heading | pages [2] -->
Introduction

<!-- b000033 | prose | pages [2] -->
2

<!-- b000034 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000035 | prose | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2

<!-- b000036 | prose | pages [2] -->
Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2

<!-- b000037 | prose | pages [2] -->
Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000038 | prose | pages [2] -->
2

<!-- b000039 | heading | pages [2] -->
Assumptions and Justiﬁcations

<!-- b000040 | prose | pages [2] -->
3

<!-- b000041 | heading | pages [2] -->
Notation

<!-- b000042 | prose | pages [2] -->
4

<!-- b000043 | heading | pages [2] -->
Analysis and Modelling

<!-- b000044 | prose | pages [2] -->
2

<!-- b000045 | prose | pages [2] -->
3

<!-- b000046 | prose | pages [2] -->
3

<!-- b000047 | prose | pages [2] -->
4

<!-- b000048 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000049 | prose | pages [2] -->
Spread of sparrow hornet over time . . . . . . . . . . . . . . . . . . . . . . . . 4.1 4

<!-- b000050 | prose | pages [2] -->
Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 4

<!-- b000051 | prose | pages [2] -->
Model 1: Factor Analysis Method . . . . . . . . . . . . . . . . . . . . 4.1.2 4

<!-- b000052 | prose | pages [2] -->
Model 2: K-means clustering algorithm and Gaussian Mixture Model . 4.1.3 6

<!-- b000053 | prose | pages [2] -->
Combined Forecast Model . . . . . . . . . . . . . . . . . . . . . . . . 4.1.4 8

<!-- b000054 | prose | pages [2] -->
Prediction of Mistaken Classiﬁcation . . . . . . . . . . . . . . . . . . . . . . . 4.2 9

<!-- b000055 | prose | pages [2] -->
Model 3: Image Recognition Based on CNN 4.2.1 . . . . . . . . . . . . . .

<!-- b000056 | prose | pages [2] -->
9

<!-- b000057 | prose | pages [2] -->
Model 4: Text Mining in the Level of Words and Sentences . . . . . . . 4.2.2 10

<!-- b000058 | prose | pages [2] -->
Combination of Image Recognition and Text Mining . . . . . . . . . . 4.2.3 13

<!-- b000059 | prose | pages [2] -->
Determine the likelihood of a Positve Report . . . . . . . . . . . . . . . . . . . 4.3 14

<!-- b000060 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 Update of the Model 15

<!-- b000061 | prose | pages [2] -->
Model 3*: Improved CNN With Pseudo Labelling 4.4.1 . . . . . . . . . . .

<!-- b000062 | prose | pages [2] -->
15

<!-- b000063 | prose | pages [2] -->
Subjective Evaluation Method . . . . . . . . . . . . . . . . . . . . . . 4.4.2 16

<!-- b000064 | prose | pages [2] -->
Evidence of Eradication in Washington State . . . . . . . . . . . . . . . . . . . 4.5 18

<!-- b000065 | prose | pages [2] -->
Regression Model With Longitudinal Data 4.5.1

<!-- b000066 | prose | pages [2] -->
5

<!-- b000067 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000068 | prose | pages [2] -->
. . . . . . . . . . . . . . .

<!-- b000069 | prose | pages [2] -->
18

<!-- b000070 | prose | pages [2] -->
20

<!-- b000071 | prose | pages [2] -->
Model’s Sensitivity in Problem (a) . . . . . . . . . . . . . . . . . . . . . . . . 5.1 20

<!-- b000072 | prose | pages [2] -->
Model’s Sensitivity in Problem (c) . . . . . . . . . . . . . . . . . . . . . . . . 5.2

<!-- b000073 | prose | pages [2] -->
6

<!-- b000074 | heading | pages [2] -->
Model Evaluation

<!-- b000075 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000076 | prose | pages [2] -->
21

<!-- b000077 | prose | pages [2] -->
21

<!-- b000078 | prose | pages [2] -->
关注数学模型

<!-- b000079 | furniture | pages [2] -->
2

<!-- b000080 | furniture | pages [2] -->
MATHmodels

<!-- b000081 | furniture | pages [2] -->
获取更多资讯

<!-- b000082 | furniture | pages [3] -->
Team # 2123823

<!-- b000083 | prose | pages [3] -->
1

<!-- b000084 | heading | pages [3] -->
Introduction

<!-- b000085 | prose | pages [3] -->
1.1

<!-- b000086 | heading | pages [3] -->
Background

<!-- b000087 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000088 | furniture | pages [3] -->
Page 2 of 24

<!-- b000089 | prose | pages [3] -->
Nowadays, biological invasions are a global concern in agriculture, food production and

<!-- b000090 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000091 | prose | pages [3] -->
biodiversity. Invasive species have detrimental eﬀects on the newly colonized areas, such as impoverishment of local species assemblages, as well as the decline of critical insects providing herbivore control and pollination services [1].

<!-- b000092 | prose | pages [3] -->
The recent ﬁnding of Vespa mandarinia (Asian giant hornet) in Canada and the USA has prompted concern that it could become an invasive species. Until the Entomological Society of America decides on the oﬃcial common names for V. mandarinia, we are suggested to use ‘sparrow hornet’ [2]. Sparrow hornet tends to nest in low mountain foothills, lowland forests or green space in urban landscapes [3]. Sparrow hornet is a quarantine pest for the USA for it will cause a signiﬁcant loss to beekeepers [4]. Therefore, much care should be taken to predict the migration of hornets over time and identify manual reports to deploy government resources more eﬃciently to investigate the problem.

<!-- b000093 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000094 | prose | pages [3] -->
1.2

<!-- b000095 | heading | pages [3] -->
Problem Restatement

<!-- b000096 | prose | pages [3] -->
(a) Develop a model to predict the sparrow hornet’s spread over time, and analyze the degree

<!-- b000097 | prose | pages [3] -->
of precision of the model.

<!-- b000098 | prose | pages [3] -->
(b) Taking the look-alike species into account, study how to predict the likelihood of a

<!-- b000099 | prose | pages [3] -->
mistaken classiﬁcation using only the data set ﬁle and (possibly) the image ﬁles provided.

<!-- b000100 | prose | pages [3] -->
(c) Set a goal for taking priority in investigating the reports that are most likely to be positive

<!-- b000101 | prose | pages [3] -->
sightings, and discuss the way to conduct the classiﬁcation analysis.

<!-- b000102 | prose | pages [3] -->
(d) Address how to update the previous model using additional new reports over time, and

<!-- b000103 | prose | pages [3] -->
determine the optimum frequency of new reports.

<!-- b000104 | prose | pages [3] -->
(e) Based on the model, ﬁnd out what would constitute evidence that the pest has been

<!-- b000105 | prose | pages [3] -->
eradicated in Washington State.

<!-- b000106 | prose | pages [3] -->
1.3 Problem Analysis

<!-- b000107 | prose | pages [3] -->
For Problem (a), we plan to predict the spread of sparrow hornets from both spatial and temporal perspectives. First, the spread of hornets may be constrained by many natural factors, so we consider using factor analysis to calculate the environmental suitability, as this method is suitable for cases where data is not available or with low quality [5]; second, the spread may be aﬀected by seasonal and cyclical factors, so we can try to use clustering methods to determine the aggregation of hornets in diﬀerent periods.

<!-- b000108 | prose | pages [3] -->
For Problem (b), the data we can utilize are the reporters’ images and notes. We should make the most of them by statistical methods.

<!-- b000109 | prose | pages [3] -->
For Problem (c), to work out how to estimate the likelihood of reports being positive and prioritize investigation of them, we decide to consider all aspects of information involved above and establish a new evaluation model based on models we have applied in Problem (a) and Problem (b).

<!-- b000110 | prose | pages [3] -->
For Problem (d), pseudo labelling is an excellent way to improve the model accuracy when more unlabeled data are now available [6]; thus we want to use it to update our model based

<!-- b000111 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000112 | prose | pages [3] -->
关注数学模型

<!-- b000113 | furniture | pages [3] -->
2

<!-- b000114 | furniture | pages [3] -->
MATHmodels

<!-- b000115 | furniture | pages [3] -->
获取更多资讯

<!-- b000116 | furniture | pages [4] -->
Team # 2123823

<!-- b000117 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000118 | furniture | pages [4] -->
Page 3 of 24

<!-- b000119 | prose | pages [4] -->
on the additional new reports. As the frequency of model updates is closely related to the frequency of report submissions, we need to determine an appropriate number of reports in a given period.

<!-- b000120 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000121 | prose | pages [4] -->
For Problem (e), to determine whether the control measures have eradicated the pests, we can use the regression model with longitudinal data to modify the spread model by taking the changes of pest population with human intervention into account. With data on population changes after taking controlled measures, we can determine the point in time and evidence of pest eradication.

<!-- b000122 | heading | pages [4] -->
Assumptions and Justiﬁcations

<!-- b000123 | prose | pages [4] -->
2

<!-- b000124 | prose | pages [4] -->
To simplify our problems, we make the following basic assumptions, each of which is adequately justiﬁed.

<!-- b000125 | prose | pages [4] -->
(a) In each month, the number of clustering centers of sparrow hornets is positively correlated

<!-- b000126 | prose | pages [4] -->
with their activity level, reaching a peak in July and August.

<!-- b000127 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000128 | prose | pages [4] -->
(b) The activity period of sparrow hornets was from April to October of year. During other

<!-- b000129 | prose | pages [4] -->
times, the sparrow hornets were in hibernation. The events of sparrow hornets found by the public during these limited periods can be considered unreliable and ignored.

<!-- b000130 | prose | pages [4] -->
(c) The ethnic inﬂuence of sparrow hornets is normally distributed over distance.

<!-- b000131 | prose | pages [4] -->
(d) The environmental suitability of the same area is generally consistent from year to year.

<!-- b000132 | prose | pages [4] -->
3

<!-- b000133 | heading | pages [4] -->
Notation

<!-- b000134 | prose | pages [4] -->
Symbol

<!-- b000135 | prose | pages [4] -->
N(x, ui, di)

<!-- b000136 | prose | pages [4] -->
Description

<!-- b000137 | prose | pages [4] -->
The probability density function of the i-th Gaussian model The likelihood of sparrow hornets appearing in the position x P(x) πi weight of the i-th Gaussian model β Vs Weight of Model 2 coeﬃcient of variation c P(Neg) Term frequency Likelihood of negative things P(Pos) Likelihood of positive things P The actual number of positive reports N The acutal number of negative reports θ Regression parameters λ regularization coeﬃcient bk ηki Fixed eﬀect factor Random eﬀect factor

<!-- b000138 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000139 | prose | pages [4] -->
关注数学模型

<!-- b000140 | furniture | pages [4] -->
2

<!-- b000141 | furniture | pages [4] -->
MATHmodels

<!-- b000142 | furniture | pages [4] -->
获取更多资讯

<!-- b000143 | furniture | pages [5] -->
Team # 2123823

<!-- b000144 | prose | pages [5] -->
4

<!-- b000145 | heading | pages [5] -->
Analysis and Modelling

<!-- b000146 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000147 | furniture | pages [5] -->
Page 4 of 24

<!-- b000148 | prose | pages [5] -->
Spread of sparrow hornet over time 4.1

<!-- b000149 | prose | pages [5] -->
After analyzing the provided data set, we can ensure that the spread of sparrow hornet is

<!-- b000150 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000151 | prose | pages [5] -->
predictable.

<!-- b000152 | prose | pages [5] -->
Understanding the role of biotic (species ecology, predation and interspeciﬁc competition) and abiotic (anthropogenic role, climate change, geographical barriers) factors has become the major challenge in ecology and biogeography. In this problem, however, we rely on abiotic variables because little is known about other biotic factors, such as species evolution, predators and competitors, which may aﬀect the location of sparrow hornet [7].

<!-- b000153 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000154 | caption | pages [5] -->
Figure 4.1: The procedures of establishing Combined Forecast Model

<!-- b000155 | prose | pages [5] -->
4.1.1 Data Preprocessing

<!-- b000156 | prose | pages [5] -->
We ﬁrst weed out events where the date is incorrectly formatted though the number of these events is small. We screen out the data before September 2019. This is because sparrow hornets were ﬁrst found in Sep. 2019 in Vancouver Island, and in Dec. 2019 in Washington State. So any report before Sep. 2019 is certain to be negative; For each year, we select the data from April to October. According to reference [8], sparrow hornets will go through hibernation outside this interval. So reports from Apr. to Oct. are much more meaningful and valuable.

<!-- b000157 | prose | pages [5] -->
4.1.2

<!-- b000158 | heading | pages [5] -->
Model 1: Factor Analysis Method

<!-- b000159 | prose | pages [5] -->
The basic idea of factor analysis is to group variables according to the correlation so that variables are more correlated within the same group and less correlated in diﬀerent groups. Each group of variables represents a basic structure, which is referred to as a common factor. So it is possible to describe each component of the original observation in terms of a linear function of unmeasured common factors and the special factors.

<!-- b000160 | prose | pages [5] -->
The factor analysis can be expressed in the following model:

<!-- b000161 | prose | pages [5] -->
In which, x1, x2, . . ., xp mean p standardized variables with a mean of 0 and a standard deviation of 1, F1, F2, . . ., Fm refer to m factor variables. Moreover, this model can be translated into the form of the matrix.

<!-- b000162 | prose | pages [5] -->
X = AF + aε

<!-- b000163 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000164 | prose | pages [5] -->
关注数学模型

<!-- b000165 | furniture | pages [5] -->
2

<!-- b000166 | furniture | pages [5] -->
MATHmodels

<!-- b000167 | furniture | pages [5] -->
获取更多资讯

<!-- b000168 | furniture | pages [6] -->
Team # 2123823

<!-- b000169 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000170 | furniture | pages [6] -->
Page 5 of 24

<!-- b000171 | prose | pages [6] -->
in which, F is the common factor; A is the factor loading matrix, which is the loading of the i-th original variable on the j-th factor variable; aij is the projection of xi onto the coordinate axis Fj if the variable xi is viewed as a vector in an m-dimensional factor space; ε is the special factor, indicating the part of the original variable that cannot be explained by the factor variables

<!-- b000172 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000173 | prose | pages [6] -->
(which can be thought of as the residuals in a multiple regression model).

<!-- b000174 | heading | pages [6] -->
Results of Model 1

<!-- b000175 | prose | pages [6] -->
Environmental suitability is deﬁned as the conditional probability of occurrence of a species given the state of the environment at a location [9]. Many abiotic drivers determine sparrow hornet colonies distribution. For instance, the abundance of sparrow hornets is positively associated with green spaces in urban landscapes [3]. On the other hand, sparrow hornet has been described as a species highly sensitive to heat and extreme climate conditions, and negatively associated with high temperatures [10]. As a result, we consider as many documented or relevant impact variables a as possible when carrying out the factor analysis, in order to adequately estimate the environmental suitability of the Northwest United States. Finally, 16 variables that can explain sparrow hornet current distribution are selected.

<!-- b000176 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000177 | caption | pages [6] -->
Table 4.1: Variable used in the analysis

<!-- b000178 | prose | pages [6] -->
Classiﬁcation Factor Abbreviation

<!-- b000179 | prose | pages [6] -->
Annual mean temperature (◦C)

<!-- b000180 | prose | pages [6] -->
Climate

<!-- b000181 | prose | pages [6] -->
T_m · · · Annual mean radiation (MJ/m2) R_m

<!-- b000182 | prose | pages [6] -->
Forest stands (%)

<!-- b000183 | prose | pages [6] -->
Habitat structure

<!-- b000184 | prose | pages [6] -->
H_for · · · Scrubland (%) H_scr Normalised diﬀerence vegetation index Vegetation productivity HDVI Average distance to rivers (m) Hydrography Dist_riv Elevation (m) Topography Elv Average population Human activity D_pop

<!-- b000185 | prose | pages [6] -->
At last, values of all the variables are converted into z-score.

<!-- b000186 | prose | pages [6] -->
It can be seen from the cumulative percentage of variance that the ﬁrst four principal components already explain nearly 87.9% of the total variance, so these could be selected for analysis. The scree plot on the right illustrates that the fold’s slope is steeper for the ﬁrst four principal components. However, it tapers oﬀlater, which is another evidence that it is appropriate to take the ﬁrst four principal components.

<!-- b000187 | prose | pages [6] -->
aData Source:

<!-- b000188 | prose | pages [6] -->
Climatic variables are retrieved from the Weather Atlas (https://www.weather-us. The website Elevations and Distances in the United States (https://pubs.usgs.gov/gip/ com). Elevations-Distances/elvadist.html) is used to gather topographic data.

<!-- b000189 | prose | pages [6] -->
The data of vegetation pro- ductivity and hydrography can be obtained from http://glovis.usgs.gov/. Anthropogenic drivers such as population are derived from the Census Bureau (https://www.census.gov/).

<!-- b000190 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000191 | prose | pages [6] -->
关注数学模型

<!-- b000192 | furniture | pages [6] -->
2

<!-- b000193 | furniture | pages [6] -->
MATHmodels

<!-- b000194 | furniture | pages [6] -->
获取更多资讯

<!-- b000195 | furniture | pages [7] -->
Team # 2123823

<!-- b000196 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000197 | furniture | pages [7] -->
Page 6 of 24

<!-- b000198 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000199 | caption | pages [7] -->
Figure 4.2: The results of total variance explained and scree plot

<!-- b000200 | prose | pages [7] -->
Next, we apply the formula Y = Zx × t, where Zx is the normalized matrix and t is the normalized orthogonal eigenvector matrix to obtain the values of the four principal components. Based on the percentage of variance in Figure 4.2 for the weighting, we can calculate the overall score and the environmental suitability of 14,260 selected points.

<!-- b000201 | prose | pages [7] -->
Ytotal = 0.50196Y1 + 0.18929Y2 + 0.11459Y3 + 0.07326Y4

<!-- b000202 | prose | pages [7] -->
ES = 500 + 100Ytotal

<!-- b000203 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000204 | prose | pages [7] -->
From the two ﬁgures below, we can see that the USA and Canada’s western coasts are ideal for the survival of hornets. A second peak occurs in and around the North Cascades National Park on the Rosario Strait’s east coast. The Kootenay National Forest in the interior is the third best place for hornets - although not as suitable as the coastal areas, the environmental suitability has been primarily maintained at around 300. By comparison, we can see that ’ high-scoring’areas all share some common and distinctive characteristics, such as high forest cover and NDVI, proximity to water sources, low human presence etc. These ﬁndings are consistent with the habits of sparrow hornets recorded in related research material [3] [10], so we consider the level of environmental suitability calculated by factor analysis is convincing to some extent.

<!-- b000205 | caption | pages [7] -->
Figure 4.4: Contour map of environmental suitability

<!-- b000206 | caption | pages [7] -->
Figure 4.3: Two-dimensional map of envi-

<!-- b000207 | prose | pages [7] -->
ronmental suitability

<!-- b000208 | heading | pages [7] -->
Model 2: K-means clustering algorithm and Gaussian Mixture Model

<!-- b000209 | prose | pages [7] -->
4.1.3

<!-- b000210 | prose | pages [7] -->
In Model 2, considering that the sparrow hornets live in groups and are distributed around the queen, we ﬁrst thought of applying the K-means clustering algorithm to ﬁnd the sparrow hornets’ cluster centres. When applying the K-means clustering algorithm to ﬁnd the clustering centers, we, in order to improve the reliability of the data, directly delete the data judged as "Negative ID" and use the remaining part.

<!-- b000211 | prose | pages [7] -->
According to the reference [8], sparrow hornets’ growth can be divided into six stages, and

<!-- b000212 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000213 | prose | pages [7] -->
关注数学模型

<!-- b000214 | furniture | pages [7] -->
2

<!-- b000215 | furniture | pages [7] -->
MATHmodels

<!-- b000216 | furniture | pages [7] -->
获取更多资讯

<!-- b000217 | furniture | pages [8] -->
Team # 2123823

<!-- b000218 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000219 | furniture | pages [8] -->
Page 7 of 24

<!-- b000220 | prose | pages [8] -->
we correspond to months to determine the number of clustering centers in each month. We preset more clustering centers in the months when sparrow hornets are active. The speciﬁc settings have been shown in the ﬁgure below.

<!-- b000221 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000222 | caption | pages [8] -->
Figure 4.5: Variation of the number of clustering centers by month

<!-- b000223 | prose | pages [8] -->
Since the initial point selection of the K-means algorithm is random, this algorithm may fall into a local optimal solution instead of a global optimal solution. To avoid this situation,

<!-- b000224 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000225 | prose | pages [8] -->
we calculate many times and ﬁnd the situation with relatively good output as the global optimal solution. Based on the processed data, we ﬁnally used the K-means clustering algorithm to ﬁnd the clustering centers’ location in each month and calculated the categories of each event. The results are shown in Figure 4.6.

<!-- b000226 | prose | pages [8] -->
After getting each cluster center’s position and the number of ethnic groups in each month, we began to apply the Gaussian mixture model to calculate the likelihood distribution of sparrow hornets in various places within the speciﬁc geographic area.

<!-- b000227 | prose | pages [8] -->
Let us brieﬂy introduce the Gaussian mixture model. The Gaussian mixture model uses the Gaussian probability density function (normal distribution curve) to quantify things accurately. It is a model based on Gaussian probability density function (normal distribution curve) that decomposes things into several.

<!-- b000228 | caption | pages [8] -->
Figure 4.6: The distribution of clustering center

<!-- b000229 | prose | pages [8] -->
The mixed Gaussian model consists of K Gaussian models (that is, the data contains K clustering centers). The probability density function of GMM is as follows:

<!-- b000230 | prose | pages [8] -->
K ∑

<!-- b000231 | prose | pages [8] -->
K ∑

<!-- b000232 | prose | pages [8] -->
p(i)p(x|i) =

<!-- b000233 | prose | pages [8] -->
p(x) =

<!-- b000234 | prose | pages [8] -->
i=1

<!-- b000235 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000236 | prose | pages [8] -->
πiN(x, ui, di)

<!-- b000237 | prose | pages [8] -->
i=1

<!-- b000238 | prose | pages [8] -->
关注数学模型

<!-- b000239 | furniture | pages [8] -->
2

<!-- b000240 | furniture | pages [8] -->
MATHmodels

<!-- b000241 | furniture | pages [8] -->
获取更多资讯

<!-- b000242 | furniture | pages [9] -->
Team # 2123823

<!-- b000243 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000244 | furniture | pages [9] -->
Page 8 of 24

<!-- b000245 | prose | pages [9] -->
where x represents the position of the sample, represents the likelihood of sparrow hornets appearing in the position x, p(x|i) = N(x, ui, di) represents the probability density function of the i-th Gaussian model, and ui, di, πi represent the mean, standard deviation and weight of i-th Gaussian model respectively. πi is proportional to the number of ethnic group members, and

<!-- b000246 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000247 | prose | pages [9] -->
∑ K

<!-- b000248 | prose | pages [9] -->
πi = 1. The greater the number of ethnic group members, the greater the inﬂuence, which

<!-- b000249 | prose | pages [9] -->
i=1

<!-- b000250 | prose | pages [9] -->
is very reasonable.

<!-- b000251 | prose | pages [9] -->
In our model, the probability of sparrow hornets appearing in various places within a speciﬁc geographic area is aﬀected by multiple cluster centers in this area. The change curve of this eﬀect with distance is the probability density curve of the normal distribution.

<!-- b000252 | heading | pages [9] -->
Results of Model 2

<!-- b000253 | prose | pages [9] -->
We calculate the likelihood of sparrow hornets appearing everywhere in a speciﬁc geographic area in each month, rescale it between 0 and 1, and ﬁnally draw a contour map in Figure 7(a).

<!-- b000254 | prose | pages [9] -->
4.1.4

<!-- b000255 | heading | pages [9] -->
Combined Forecast Model

<!-- b000256 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000257 | prose | pages [9] -->
Model 1 calculates the environmental suitability according to the region’s natural conditions and scales it to between 0 and 1 to obtain the likelihood distribution of sparrow hornets. Model 2 predicts the likelihood distribution of sparrow hornets in diﬀerent months based on the existing data of the distribution of sparrow hornets. And then we combine the results of these two models at a ratio of 1 : β. In this part, let us set β = 1. Furthermore, we will study how to select its value in Sensitivity Analysis. Finally, we obtained the likelihood distribution of sparrow hornets in diﬀerent months in recent years, as shown in Figure 7(b).

<!-- b000258 | prose | pages [9] -->
Since the K-means clustering algorithm results are not necessarily consistent each time it runs but are similar, this causes the results obtained by our ﬁnal model to ﬂuctuate within a speciﬁc range. Therefore, we need to calculate the precision of our model predictions. Our deﬁnition of precision is the degree of error in the prediction results of the comprehensive prediction model, which corresponds to the magnitude of the error. Therefore, we use the coeﬃcient of variation Vs to reﬂect the level of precision.

<!-- b000259 | prose | pages [9] -->
The smaller the coeﬃcient of variation Vs, the smaller the variation range of the prediction results, which means the higher the precision level. The calculation of the coeﬃcient of variation is as follows where σ and ¯X represents standard deviation and average of data X.

<!-- b000260 | prose | pages [9] -->
Vs = σ

<!-- b000261 | prose | pages [9] -->
(a) results of Model 2

<!-- b000262 | prose | pages [9] -->
(4.1.1) ¯X

<!-- b000263 | prose | pages [9] -->
(b) results of the combined model in Problem (a)

<!-- b000264 | caption | pages [9] -->
Figure 4.7: Likelihood distribution of sparrow hornets in diﬀerent months

<!-- b000265 | prose | pages [9] -->
We calculated the coeﬃcient of variation of outputs predicted by month. From Figure 4.8,

<!-- b000266 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000267 | prose | pages [9] -->
关注数学模型

<!-- b000268 | furniture | pages [9] -->
2

<!-- b000269 | furniture | pages [9] -->
MATHmodels

<!-- b000270 | furniture | pages [9] -->
获取更多资讯

<!-- b000271 | furniture | pages [10] -->
Team # 2123823

<!-- b000272 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000273 | furniture | pages [10] -->
Page 9 of 24

<!-- b000274 | prose | pages [10] -->
we can ensure that our model’s precision is high enough to estimate the likelihood.

<!-- b000275 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000276 | caption | pages [10] -->
Figure 4.8: Vs of outputs by month

<!-- b000277 | prose | pages [10] -->
Prediction of Mistaken Classiﬁcation 4.2

<!-- b000278 | prose | pages [10] -->
After inspection of the given spreadsheet, we ﬁnd that most reported sightings are identiﬁed as mistaken ones. Hence, in this part, we are to establish a model to help predict the likelihood of a mistaken classiﬁcation.

<!-- b000279 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000280 | prose | pages [10] -->
N.B. We may call something such as a report, a ﬁgure, a note or even a word, as ‘positive’ or ‘negative’ in the following. This means its corresponding ‘Lab Status’ is positive or negative.

<!-- b000281 | heading | pages [10] -->
Model 3: Image Recognition Based on CNN

<!-- b000282 | prose | pages [10] -->
4.2.1

<!-- b000283 | prose | pages [10] -->
Data Preprocessing While the given data was cleaned in the last part, it still shows a severe imbalance of the data distribution, in that, there are 2028 negative reports versus only 14 positive ones. This is not good for the following learning of sparrow hornets’ features.b We come up with two approaches to solve this. For one thing, we increase the number of positive samples. In detailc,

<!-- b000284 | prose | pages [10] -->
• we ﬂipp the positive ﬁgures vertically and horizontally to triple its number;

<!-- b000285 | prose | pages [10] -->
• we download some ﬁgures from reliable websites.d

<!-- b000286 | prose | pages [10] -->
For another, we decreased the number of negative samples. In detail, we randomly selected some of them, making its number equal to positive ones.

<!-- b000287 | prose | pages [10] -->
Through preprocessing, now there are 258 positive samples and 258 negative ones. We mix them uniformly and split them by the ratio of 7 to 3 for training and test.

<!-- b000288 | prose | pages [10] -->
As to the targets, we label the positive and negative target as 1 and 0 respectively, denoting the likelihood of a positive target. Finally, there are 411 training samples & targets and 177 test samples & targets.

<!-- b000289 | prose | pages [10] -->
Convolutional Neural Network Convolutional neural networks(CNN) have played an im- portant role in the history of deep learning, especially in object recognition. For instance, they

<!-- b000290 | prose | pages [10] -->
bActually we had once attempted to use all of them to train our model. It was found that the model was inclined to predict all the samples as negative regardless of the real targets.

<!-- b000291 | prose | pages [10] -->
cResizing and normalization are also incorporated in preprocessing. They are not mentioned in the main body since they made no contributions to the increase of positive samples

<!-- b000292 | prose | pages [10] -->
dData Source:

<!-- b000293 | prose | pages [10] -->
Asian Giant Hornet(https://en.wikipedia.org/wiki/Asian_giant_hornet), Get to know the Asian giant hornet, or ’murder hornet’(https://agrilifetoday.tamu.edu/2020/05/11/ get-to-know-the-asian-giant-hornet-or-murder-hornet/)

<!-- b000294 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000295 | prose | pages [10] -->
关注数学模型

<!-- b000296 | furniture | pages [10] -->
2

<!-- b000297 | furniture | pages [10] -->
MATHmodels

<!-- b000298 | furniture | pages [10] -->
获取更多资讯

<!-- b000299 | furniture | pages [11] -->
Team # 2123823

<!-- b000300 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000301 | furniture | pages [11] -->
Page 10 of 24

<!-- b000302 | prose | pages [11] -->
were used to win many contests, including the ImageNet object recognition challenges [11]. So here we establish a CNN for preliminary prediction.

<!-- b000303 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000304 | caption | pages [11] -->
Figure 4.10: ROC curve of CNN’s prediction

<!-- b000305 | caption | pages [11] -->
Figure 4.9: The architecture of our CNN

<!-- b000306 | prose | pages [11] -->
We construct our CNN with PyTorch. The architecture of the network is displayed in Figure 4.9(drawn with TikZ). There are two convolutional layers, two pooling layers and two fully

<!-- b000307 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000308 | prose | pages [11] -->
connected layers. The shape of the input is (b × 3 × 96 × 96), where b denotes the batch size, 3 denotes the number of channels, and 96 × 96 are the height and width. The shape of the output is (b). Train for 200 epochs.

<!-- b000309 | prose | pages [11] -->
The test accuracy reaches its peak of 0.8968 at the 93rd epoch. The model at this epoch is saved as the ﬁnal predictor. We plot the ROC Curve in Figure 4.4.10. The horizontal and vertical axes are the false positive rate (FPR) and true positive rate (TPR). AUC denotes the Area Under ROC Curve. A model with AUC closer to one shows better performance in prediction. Now our model’s AUC equals to 0.93. With only 411 training samples, this result is quite acceptable.

<!-- b000310 | heading | pages [11] -->
Model 4: Text Mining in the Level of Words and Sentences

<!-- b000311 | prose | pages [11] -->
4.2.2

<!-- b000312 | prose | pages [11] -->
The given data set also includes some notes attached by the reporters, which are not to be ignored. We have just modelled the prediction of P(Pos) and P(Neg) based on images, while these notes are also thought to be helpful to our prediction.

<!-- b000313 | heading | pages [11] -->
Introduction of the improved tf-idf model

<!-- b000314 | prose | pages [11] -->
In information retrieval, tf–idf, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reﬂect how important a word is to a document in a collection or corpus [12]. Such a model is made up of two parts literally.

<!-- b000315 | prose | pages [11] -->
Term frequency, i.e., cw, is the number of times a term w occurs in a document, while inverse document frequency is a measure of how much information the word provides, i.e., if it’s common or rare across all documents. In most cases, a term with a higher cw tends to contribute more to the document. Nevertheless, a stopword like ‘the’ or ‘I’m’ can hardly give us any information.

<!-- b000316 | prose | pages [11] -->
This inspires us to estimate the ‘positive’ likelihood of each word, viz., Pw(Pos) according to its cw. What is diﬀerent here is about ‘Lab Status’. For instance, a ‘negative’ word will contribute inversely to the note. So we suggest an improved tf-idf model according to its cw considering the Lab Status.

<!-- b000317 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000318 | prose | pages [11] -->
关注数学模型

<!-- b000319 | furniture | pages [11] -->
2

<!-- b000320 | furniture | pages [11] -->
MATHmodels

<!-- b000321 | furniture | pages [11] -->
获取更多资讯

<!-- b000322 | furniture | pages [12] -->
Team # 2123823

<!-- b000323 | prose | pages [12] -->
Data Preprocessing & Qualitative Analysis

<!-- b000324 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000325 | furniture | pages [12] -->
Page 11 of 24

<!-- b000326 | prose | pages [12] -->
We continue using the data from Sep. 2019. For each note, eliminate the stopwords e. Then we group these notes by its Lab Status. Furthermore, we quantify Lab Status in the form of P(Pos).

<!-- b000327 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000328 | prose | pages [12] -->
For ‘Positive ID’, Ppos(Pos) = 1. For ‘Negative ID’, Pneg(Pos) = 0. For ‘Unveriﬁed’, Puv(Pos) = 0.5, because even oﬃcial specialist cannot identify it. Also, a matter with the

<!-- b000329 | prose | pages [12] -->
P likelihood of 0.5 is hardest to predict. For ‘Unprocessed’, Pup(Pos) = P + N , where P and N

<!-- b000330 | prose | pages [12] -->
denote the actual number of positive and negative reports separately. This is because it has not been classiﬁed rather than be unable to be classiﬁed. So we use the mathematical expectation as P(Pos).

<!-- b000331 | prose | pages [12] -->
Let n, p, up, uv represent the number of the four kinds of reports mentioned above in order. We will have these two equations.

<!-- b000332 | prose | pages [12] -->
N = n + up × N N + P + 0.5 × uv (4.2.1)

<!-- b000333 | prose | pages [12] -->
P N + P + 0.5 × uv P = p + up × (4.2.2)

<!-- b000334 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000335 | prose | pages [12] -->
Solve the simultaneous equations and we can obtain the value of N and P.

<!-- b000336 | prose | pages [12] -->
T = N + P = n + p + uv + up = 4440

<!-- b000337 | prose | pages [12] -->
N = n + uv/2

<!-- b000338 | prose | pages [12] -->
1 −up/T = 3251, P = T −N = 1189

<!-- b000339 | prose | pages [12] -->
After ﬁlling P(Pos) for each note, we create the word clouds of positive notes and negative notes. This can reﬂect a word’s ‘positive’ or ‘negative’ attribute qualitatively.

<!-- b000340 | prose | pages [12] -->
(a) for positive ones (b) for negative ones

<!-- b000341 | caption | pages [12] -->
Figure 4.11: Word clouds of notes

<!-- b000342 | prose | pages [12] -->
The word ‘hornet’ often appears both in positive and negative notes, which can be easily explained by the creature’s name. Additionally, the word ‘wsda’ is conspicuous in the positive word cloud. This may be because the notes including ‘wsda’ are submitted by WSDA or its staﬀwith more knowledge about the sparrow hornet.

<!-- b000343 | prose | pages [12] -->
For a ‘Lab Status’ i, Pi(Pos) can be regarded as a sort of score. We

<!-- b000344 | heading | pages [12] -->
Modelling of a Word

<!-- b000345 | prose | pages [12] -->
can grade each word except stopwords.

<!-- b000346 | prose | pages [12] -->
Now let us set the grading rule. If a word w appears ci times for status i, it will get a score of ci × Pi(Pos). The ﬁnal score is calculated by adding four scores together. This score have

<!-- b000347 | prose | pages [12] -->
eThe stopwords are provided by the corpus of Python’s Natural Language Toolkit

<!-- b000348 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000349 | prose | pages [12] -->
关注数学模型

<!-- b000350 | furniture | pages [12] -->
2

<!-- b000351 | furniture | pages [12] -->
MATHmodels

<!-- b000352 | furniture | pages [12] -->
获取更多资讯

<!-- b000353 | furniture | pages [13] -->
Team # 2123823

<!-- b000354 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000355 | furniture | pages [13] -->
Page 12 of 24

<!-- b000356 | prose | pages [13] -->
no upper limit. So we divide it by the total times it appears, i.e., ∑

<!-- b000357 | prose | pages [13] -->
i ci(w). We deﬁne this value as Pw(Pos). Apparently, Pw(Pos) is between 0 and 1.

<!-- b000358 | prose | pages [13] -->
∑

<!-- b000359 | prose | pages [13] -->
cw(i) × Pi(Pos)

<!-- b000360 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000361 | prose | pages [13] -->
def

<!-- b000362 | prose | pages [13] -->
i

<!-- b000363 | prose | pages [13] -->
∑

<!-- b000364 | prose | pages [13] -->
===

<!-- b000365 | prose | pages [13] -->
Pw(Pos)

<!-- b000366 | prose | pages [13] -->
cw(i)

<!-- b000367 | prose | pages [13] -->
i

<!-- b000368 | prose | pages [13] -->
If we rewrite Eq. 4.2.3 as

<!-- b000369 | prose | pages [13] -->
∑

<!-- b000370 | prose | pages [13] -->
i ∈{pos, neg, uv, up} , (4.2.3)

<!-- b000371 | prose | pages [13] -->
cw(i) ∑ Pi(Pos) ×

<!-- b000372 | prose | pages [13] -->
Pw(Pos) =

<!-- b000373 | prose | pages [13] -->
i

<!-- b000374 | prose | pages [13] -->
i

<!-- b000375 | prose | pages [13] -->
i ∈{pos, neg, uv, up} cw(i), (4.2.4)

<!-- b000376 | prose | pages [13] -->
cw(i) ∑ then Pw(Pos) is the weighted mean of Pi(Pos), whose weight equals

<!-- b000377 | heading | pages [13] -->
Modelling of a Note

<!-- b000378 | prose | pages [13] -->
cw(i).

<!-- b000379 | prose | pages [13] -->
i

<!-- b000380 | prose | pages [13] -->
A note is composed of several words. Thus the positive likelihood

<!-- b000381 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000382 | prose | pages [13] -->
of a note, viz., Pn(Pos) is also a composition of Pw(Pos). It is found that some words like ‘Manson’ and ‘incident’ only appears once, rendering them much less reliable for the positive likelihood. In this sense, they should contribute less to Pn(Pos). This means Pn(Pos) is positively correlated with a word’s term frequency, cw. Based on the above, we deﬁne Pn(Pos) as

<!-- b000383 | prose | pages [13] -->


<!-- b000384 | prose | pages [13] -->
∑

<!-- b000385 | prose | pages [13] -->
w∈Sn ln cw × Pw(Pos)

<!-- b000386 | prose | pages [13] -->
  

<!-- b000387 | prose | pages [13] -->
∑

<!-- b000388 | prose | pages [13] -->
def ===

<!-- b000389 | prose | pages [13] -->
Pn(Pos)

<!-- b000390 | prose | pages [13] -->


<!-- b000391 | prose | pages [13] -->
P

<!-- b000392 | prose | pages [13] -->
 

<!-- b000393 | prose | pages [13] -->
P + N

<!-- b000394 | prose | pages [13] -->
, Sn̸ = ∅;

<!-- b000395 | prose | pages [13] -->
w∈Sn ln cw

<!-- b000396 | prose | pages [13] -->
(4.2.5)

<!-- b000397 | prose | pages [13] -->
, Sn = ∅.

<!-- b000398 | prose | pages [13] -->
where Sn is the set of all words in the note n. As mentioned in the last part, the data distribution show a severe imbalance between negative and positive ones. So if a note is not empty, we will take a logarithm of cw to bridge the gap. However, there also exist some reports without notes. In this case, we choose the mathematical expectation as their value.

<!-- b000399 | prose | pages [13] -->
With this deﬁnition, let us recalculate the positive likelihood of each note. Notes are grouped by ‘Lab Status’(marked as G1, G2, G3, G4). The distribution of each group’s Pn(Pos) is shown in Figure 4.12. The subtitles represent the means of Pn(Pos).

<!-- b000400 | caption | pages [13] -->
Figure 4.12: Distribution histograms of four group’s Pn(Pos)

<!-- b000401 | prose | pages [13] -->
In general, G1 has the greatest mean Pn(pos) and G2 has the least mean Pn(Pos), which is consistent with reality. But the maximum of G1’s Pn(Pos) is less than 0.5. This is normal

<!-- b000402 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000403 | prose | pages [13] -->
关注数学模型

<!-- b000404 | furniture | pages [13] -->
2

<!-- b000405 | furniture | pages [13] -->
MATHmodels

<!-- b000406 | furniture | pages [13] -->
获取更多资讯

<!-- b000407 | furniture | pages [14] -->
Team # 2123823

<!-- b000408 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000409 | furniture | pages [14] -->
Page 13 of 24

<!-- b000410 | prose | pages [14] -->
for that many words appearing in positive notes also appear in negative ones. Moreover, the

<!-- b000411 | prose | pages [14] -->
N N + P is 0.262045. So it can be seen that both G2 and G3 have a spike calculated value of

<!-- b000412 | prose | pages [14] -->
when Pn(Pos) ≈0.26, which can be attributed to their ‘empty’ notes.

<!-- b000413 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000414 | prose | pages [14] -->
To check the eﬀect of the logarithm, we compare the distribution of G1’s Pn(Pos) con- The latter corresponding formula for a non-empty note sidering logarithm and without it. is

<!-- b000415 | prose | pages [14] -->


<!-- b000416 | prose | pages [14] -->
∑

<!-- b000417 | prose | pages [14] -->
w∈Sn cw × Pw(Pos)

<!-- b000418 | prose | pages [14] -->
  

<!-- b000419 | prose | pages [14] -->
∑

<!-- b000420 | prose | pages [14] -->
def

<!-- b000421 | prose | pages [14] -->
P ′

<!-- b000422 | prose | pages [14] -->
===

<!-- b000423 | prose | pages [14] -->
n(Pos)

<!-- b000424 | prose | pages [14] -->


<!-- b000425 | prose | pages [14] -->
P

<!-- b000426 | prose | pages [14] -->
 

<!-- b000427 | prose | pages [14] -->
P + N

<!-- b000428 | prose | pages [14] -->
, Sn̸ = ∅;

<!-- b000429 | prose | pages [14] -->
w∈Sn cw

<!-- b000430 | prose | pages [14] -->
(4.2.6)

<!-- b000431 | prose | pages [14] -->
, Sn = ∅.

<!-- b000432 | caption | pages [14] -->
Figure 4.13 informs us that G1’s Pn(Pos) moves towards 1 in general, and the mean has

<!-- b000433 | prose | pages [14] -->
increased from 0.301 to 0.326 by 8.31%. Thus Deﬁnition 4.2.5 proves to be more reliable than Deﬁnition 4.2.6.

<!-- b000434 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000435 | prose | pages [14] -->
(a) Using Deﬁnition 4.2.6 (b) Using Deﬁnition 4.2.5

<!-- b000436 | caption | pages [14] -->
Figure 4.13: Comparison of the distribution of G1’s Pn(Pos)

<!-- b000437 | prose | pages [14] -->
Combination of Image Recognition and Text Mining 4.2.3

<!-- b000438 | prose | pages [14] -->
Although our improved tf-idf model predicts worse than the CNN, the relative likelihood is accurate. Furthermore, it measures a report from a diﬀerent aspect. In this sense, we can combine these two models to increase the accuracy of prediction.

<!-- b000439 | prose | pages [14] -->
We plot the distribution of the prediction results in Figure 4.14. The two histograms diﬀer signiﬁcantly in shape, which is not suitable for linear combination. In this case, we turn to combine them in a nonlinear form.

<!-- b000440 | caption | pages [14] -->
Figure 4.15: 2-D visualization of the result’s distribution

<!-- b000441 | caption | pages [14] -->
Figure 4.14: Distribution of the results

<!-- b000442 | prose | pages [14] -->
for training data

<!-- b000443 | prose | pages [14] -->
In order ro represent the contributions of the images and the notes, we introduce the coeﬃcient C1 and C2 as their exponents. The general form is as below.

<!-- b000444 | prose | pages [14] -->
ln ˆP(Pos) = ln m × {k × [Pim(Pos)]C1 × [Pn(Pos)]C2 + b}

<!-- b000445 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000446 | prose | pages [14] -->
(4.2.7)

<!-- b000447 | prose | pages [14] -->
关注数学模型

<!-- b000448 | furniture | pages [14] -->
2

<!-- b000449 | furniture | pages [14] -->
MATHmodels

<!-- b000450 | furniture | pages [14] -->
获取更多资讯

<!-- b000451 | furniture | pages [15] -->
Team # 2123823

<!-- b000452 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000453 | furniture | pages [15] -->
Page 14 of 24

<!-- b000454 | prose | pages [15] -->
By ﬁtting the training data, the values of the coeﬃcients are

<!-- b000455 | prose | pages [15] -->
m = 0.6489, k = 0.0956, C1 = −39.3, C2 = −4.4, b = −3.806

<!-- b000456 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000457 | prose | pages [15] -->
C1 is nearly nine times larger than C2, which tells us the result depends much more on the image than the textual part. This is also consistent with Figure 4.15, where actual positive points only appear when Pm(Pos) is greater than 0.9.

<!-- b000458 | prose | pages [15] -->
We calculate the result of the test samples and display the distribution in Figure 4.16. The value of AUC is increased to 0.94 by 1.08%.

<!-- b000459 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000460 | caption | pages [15] -->
Figure 4.17: The ROC curve based on combined model

<!-- b000461 | caption | pages [15] -->
Figure 4.16: 3-D visualization of the re-

<!-- b000462 | prose | pages [15] -->
in Problem (b)

<!-- b000463 | prose | pages [15] -->
sult’s distribution for test data

<!-- b000464 | prose | pages [15] -->
Determine the likelihood of a Positve Report 4.3

<!-- b000465 | prose | pages [15] -->
Based on the work above, we intend to integrate these two models through Regularized Logistic Regression to improve prediction accuracy.

<!-- b000466 | prose | pages [15] -->
Regularized Logistic Regression We take the likelihood of sparrow hornets appearing obtained by the two models in Problem (a) and (b) as input values, respectively marked as pab1 and pab2, and the actual likelihood is the output value, which is marked as y. The data set we select refers to the events that provide the picture and are judged as positive or negative, where Positive ID corresponds to 1, and Negative ID corresponds to 0. Then we randomly divide this data set into the training set and test set.

<!-- b000467 | prose | pages [15] -->
Before training, considering the input only has two features, we need to apply the feature mapping method to expand the two features into 28 features.

<!-- b000468 | prose | pages [15] -->
mapFeature(pab) = [1, pab1, pab2, p2

<!-- b000469 | prose | pages [15] -->
ab1, pab1pab2, p2

<!-- b000470 | prose | pages [15] -->
ab2, · · · , p6

<!-- b000471 | prose | pages [15] -->
ab2]T

<!-- b000472 | prose | pages [15] -->
where pab andmapfeature(pab)respectivelyrepresentsthe2-dimensionalvectorand28-dimensional vector.

<!-- b000473 | prose | pages [15] -->
After that, we started to train the model on the training set. The cost function J(θ) is calculated as follows.

<!-- b000474 | prose | pages [15] -->
hθ(pab) =

<!-- b000475 | prose | pages [15] -->
m ∑

<!-- b000476 | prose | pages [15] -->
J(θ) = 1

<!-- b000477 | prose | pages [15] -->
[−y(i) ln(hθ(p(i)

<!-- b000478 | prose | pages [15] -->
1 1 + e−θT pab

<!-- b000479 | prose | pages [15] -->
n ∑

<!-- b000480 | prose | pages [15] -->
ab ))] + λ

<!-- b000481 | prose | pages [15] -->
ab )) −(1 −y(i)) ln(1 −hθ(p(i)

<!-- b000482 | prose | pages [15] -->
m

<!-- b000483 | prose | pages [15] -->
i=1

<!-- b000484 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000485 | prose | pages [15] -->
θ2

<!-- b000486 | prose | pages [15] -->
j

<!-- b000487 | prose | pages [15] -->
2m

<!-- b000488 | prose | pages [15] -->
j=1

<!-- b000489 | prose | pages [15] -->
关注数学模型

<!-- b000490 | furniture | pages [15] -->
2

<!-- b000491 | furniture | pages [15] -->
MATHmodels

<!-- b000492 | furniture | pages [15] -->
获取更多资讯

<!-- b000493 | furniture | pages [16] -->
Team # 2123823

<!-- b000494 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000495 | furniture | pages [16] -->
Page 15 of 24

<!-- b000496 | prose | pages [16] -->
where θ represents regression parameters, λ represents the regularization coeﬃcient, which we set as 0.6. When the cost function J(θ) is the smallest, the regression eﬀect is best, and the regression model can be considered the ﬁnal model.

<!-- b000497 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000498 | heading | pages [16] -->
Results and Analysis

<!-- b000499 | prose | pages [16] -->
To evaluate our model, we test this new model’s accuracy on the test set. The ﬁnal predicted result matches the real situation perfectly.

<!-- b000500 | prose | pages [16] -->
Analyzing the predicted results, we found that even though there were two misjudgments in the event, the overall accuracy rate has reached 0.99, which shows that our model is reliable. Therefore our model is helpful to determine the likelihood of positive reports positive and prioritize investigation of them.

<!-- b000501 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000502 | caption | pages [16] -->
Figure 4.18: Distribution of predicted outputs

<!-- b000503 | prose | pages [16] -->
4.4

<!-- b000504 | heading | pages [16] -->
Update of the Model

<!-- b000505 | prose | pages [16] -->
Although the CNN in section 4.2.1 has a relatively high accuracy of 0.8969, it can be furtherly improved due to a great deal of new data, especially from the additional new reports. Through pseudo labelling, we are now able to make use of the unexploited data.

<!-- b000506 | prose | pages [16] -->
Pseudo labelling is the process of using the labelled data model to predict labels for un- labelled data. It is often used in semi-supervised learning, where most data are unlabelled. Nowadays, this technique is used for hyperspectral image classiﬁcation and the identiﬁcation of COVID-19 on chest X-rays. [11][12] Based on image recognition results of CNN, we will use pseudo labelling to improve our model. The procedure is shown in the ﬂow chart below. (Figure 4.9)

<!-- b000507 | heading | pages [16] -->
Model 3*: Improved CNN With Pseudo Labelling

<!-- b000508 | prose | pages [16] -->
4.4.1

<!-- b000509 | prose | pages [16] -->
Pseudo labelling is the process of using the labelled data model to predict labels for unlabelled data. It is often used in semi-supervised learning, where most data are unlabelled. Nowadays, this technique is used for hyperspectral image classiﬁcation and the identiﬁcation of COVID-19 on chest X-rays [13][14].

<!-- b000510 | prose | pages [16] -->
Based on image recognition results of CNN, we will use pseudo labelling to improve our model. The procedure is shown in the ﬂow chart below. (Figure 4.19)

<!-- b000511 | prose | pages [16] -->
Because additional data from Washington state on Asian hornets similar to what was provided in the spreadsheet is explicitly not allowed in Problem (c), we add the unlabeled data (unveriﬁed and unprocessed) that were not originally in the training set as "new report data" to this model, which can help us test whether additional new reports will improve our model. We reckon that the precision of the value of P(Pos), which is farther away from 0.5 is more reliable and convincing. Therefore, we only label the predicted result which is either

<!-- b000512 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000513 | prose | pages [16] -->
关注数学模型

<!-- b000514 | furniture | pages [16] -->
2

<!-- b000515 | furniture | pages [16] -->
MATHmodels

<!-- b000516 | furniture | pages [16] -->
获取更多资讯

<!-- b000517 | furniture | pages [17] -->
Team # 2123823

<!-- b000518 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000519 | furniture | pages [17] -->
Page 16 of 24

<!-- b000520 | prose | pages [17] -->
larger than 0.9 or less than 0.1. To check this, we visualize some of the prediction results of unveriﬁed images in Figure 4.21.

<!-- b000521 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000522 | caption | pages [17] -->
Figure 4.19: The procedures of pseudo la-

<!-- b000523 | prose | pages [17] -->
belling

<!-- b000524 | caption | pages [17] -->
Figure 4.20: A real sparrow hornet

<!-- b000525 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000526 | prose | pages [17] -->
The 1st and the 3rd ﬁgures’ values of P(Neg) are below 0.1, showing they are likely to be positive sightings. We can compare them with a real sparrow hornet in Figure 4.20. They are very similar to the three typical characteristics of a real hornet’s appearance. Therefore, such prediction is relatively reliable and can be labelled as (pseudo) positive.

<!-- b000527 | prose | pages [17] -->
After pseudo labelling, we include them into the original labelled dataset and retrain our CNN obtained before. At the 7th epoch, test accuracy reaches a higher peak of 0.9096, which has increased by 1.43% compared to previous 0.8968.

<!-- b000528 | caption | pages [17] -->
Figure 4.21: Prediction result of unveriﬁed images

<!-- b000529 | prose | pages [17] -->
Compared with the result before pseudo labelling, the value of AUC has increased to 0.96 by 1.08%. The result demonstrates the eﬀectiveness of improving our model by setting the new report as a pseudo label added to the training model.

<!-- b000530 | prose | pages [17] -->
4.4.2 Subjective Evaluation Method

<!-- b000531 | prose | pages [17] -->
The key to solving an appropriate frequency of model updates lies in determining an appropri- ate number of reports in a given period. As a result, we use the subjective evaluation method to score each area based on diﬀerent factors closely correlated with the emergence of potential reporting cases. We ﬁnally select ﬁve key evaluation indicators for analysis: environmental

<!-- b000532 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000533 | prose | pages [17] -->
关注数学模型

<!-- b000534 | furniture | pages [17] -->
2

<!-- b000535 | furniture | pages [17] -->
MATHmodels

<!-- b000536 | furniture | pages [17] -->
获取更多资讯

<!-- b000537 | furniture | pages [18] -->
Team # 2123823

<!-- b000538 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000539 | furniture | pages [18] -->
Page 17 of 24

<!-- b000540 | prose | pages [18] -->
suitability (1), seasonal factors (2), major external events (3), economic development (4), and reporting stability (5). The ranking results of importance are as follows.

<!-- b000541 | prose | pages [18] -->
I2 > I3 > I1 > I4 > I5

<!-- b000542 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000543 | prose | pages [18] -->
The speciﬁc scoring rules are: each area’s score consists of two parts (initial score and additional score), where the initial score is dependent on the environmental suitability of this area, and other four factors determine the additional score. The area’s score is updated every day until the threshold (e.g. 100) is reached, which means that the area should submit new reports at this point. Then, all the scores of this area are cleared, and the scoring starts again. According to the data we have, we estimate there will be a report submitted from this area in almost six days, which also indicates that 17 points need to be added in average per day on a 100-point scale. After distributing the ﬁve factors’ weights, the initial score (IS) formula is as follows.

<!-- b000544 | prose | pages [18] -->
ISi = 17 × Weight3 × ESi

<!-- b000545 | prose | pages [18] -->
, i = 1, 2, . . . , 63

<!-- b000546 | prose | pages [18] -->
MedianES

<!-- b000547 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000548 | prose | pages [18] -->
in which Weight3 means the weight of the third factor (environment suitability) and 63 refers to the total number of the areas in Washington State.

<!-- b000549 | prose | pages [18] -->
There are also some rules regarding the determination of additional score:

<!-- b000550 | prose | pages [18] -->
(a) Seasonal factors require diﬀerent additional scores in diﬀerent months in the same area.

<!-- b000551 | prose | pages [18] -->
We will consider the number of clustering centers (NCC) in Model 2 as a determinant of the additional score. Its formula is as follows.

<!-- b000552 | prose | pages [18] -->
ASaj = 17 × Weight1 × NCCj

<!-- b000553 | prose | pages [18] -->
, j = 1, 2, . . . , 12

<!-- b000554 | prose | pages [18] -->
MedianNCC

<!-- b000555 | prose | pages [18] -->
(b) The impact of major external events is mainly reﬂected in the fact that when a positive

<!-- b000556 | prose | pages [18] -->
sighting occurs in the region, the area’s daily additional score can be set to 125% of the initial score for the next six months. (This eﬀect can be stacked)

<!-- b000557 | prose | pages [18] -->
(c) The higher the level of economic development in the area, the higher the frequency of

<!-- b000558 | prose | pages [18] -->
reporting. The following equation can express this relationship.

<!-- b000559 | prose | pages [18] -->
ASci = 17 × Weight4 × GDPi

<!-- b000560 | prose | pages [18] -->
, i = 1, 2, . . . , 63

<!-- b000561 | prose | pages [18] -->
MedianGDP

<!-- b000562 | prose | pages [18] -->
(d) Reporting stability can be positively correlated with the duration of consistently negative

<!-- b000563 | prose | pages [18] -->
reports for the area. Speciﬁcally, suppose an area has more than six months of consecutive negative reports recorded. In that case, the additional value is −50% of its initial value from the sixth month until a positive record occurs in the area.

<!-- b000564 | prose | pages [18] -->
Let us consider a speciﬁc example. Suppose there is a circular area A with a radius of GDPA 30km. In this area, MedianGDP = 1.2 and the expected environmental suitability is 84 (median is 115 in the whole state). Moreover, we assume that it is now at the beginning of May. It is also important to note that there was one positive case reported in the region at the end of April. The current estimate is that there will be no further positives in the area for six months after that.

<!-- b000565 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000566 | prose | pages [18] -->
关注数学模型

<!-- b000567 | furniture | pages [18] -->
2

<!-- b000568 | furniture | pages [18] -->
MATHmodels

<!-- b000569 | furniture | pages [18] -->
获取更多资讯

<!-- b000570 | furniture | pages [19] -->
Team # 2123823

<!-- b000571 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000572 | furniture | pages [19] -->
Page 18 of 24

<!-- b000573 | prose | pages [19] -->
By considering the various factors in our evaluation model, we conclude that the monthly reportable quantity in Region A varies over time in the next eight months, with the highest in July and August (5.2/month) and the lowest in November and December (1.3/month).

<!-- b000574 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000575 | prose | pages [19] -->
Evidence of Eradication in Washington State 4.5

<!-- b000576 | prose | pages [19] -->
Eradication is deﬁned as eliminating every individual of a species from an area to which recolonization is unlikely to occur [15]. There are various ways to eradicate the sparrow hornet recommended by the United States Department of Agriculture (USDA). For instance, we can use lethal traps during the early (pre-nesting and solitary stages) and late seasons (reproductive stage) to kill queens, or take a proactive approach to ﬁnd and eliminate nests during the middle seasons (cooperative and polyethic) [16]. As a result, judgements about the eﬀectiveness of eradication will directly determine the extent to which diﬀerent methods can be applied in diﬀerent areas.

<!-- b000577 | heading | pages [19] -->
Regression Model With Longitudinal Data

<!-- b000578 | prose | pages [19] -->
4.5.1

<!-- b000579 | prose | pages [19] -->
Some relevant literature reveals that invasive hornets are particularly problematic due to the

<!-- b000580 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000581 | prose | pages [19] -->
adverse impact on local bee assemblages [4]. So when constructing the model to evaluate eradication eﬀectiveness, we mainly focus on two crucial factors - changes in the population of local bees and sparrow hornets in a given area over time. According to our hypothesis, the local bee population theoretically shows an increase followed by a decrease during the control process. In contrast, the invasive hornet population shows the opposite trend, with a decrease followed by an increase. Given this, we can model a quadratic regression of density on time:

<!-- b000582 | prose | pages [19] -->
yij = b0i + b1itij + b2it2

<!-- b000583 | prose | pages [19] -->
ij + εij, i = 1, . . . , n, j = 1, . . . , ni (4.5.1)

<!-- b000584 | prose | pages [19] -->
where yij means the density of local bees (or sparrow hornets) of the j-th observation at the i-th site, and tij refers to the time point of the j-th observation at the i-th site; n is the number of sites where the invasive species occur, and ni is the number of observations at the i-th site during the whole period.

<!-- b000585 | prose | pages [19] -->
Based on the above, the quadratic regression model above is rewritten using a mixed model to highlight the area’s overall density data. A mixed-eﬀects model is a statistical model containing both ﬁxed eﬀects and random eﬀects [6].

<!-- b000586 | prose | pages [19] -->
bki = bk + ηki, k = 0, 1, 2 (4.5.2)

<!-- b000587 | prose | pages [19] -->
in which bk is the ﬁxed eﬀect factor for the whole area (not related to the observation site),

<!-- b000588 | caption | pages [19] -->
Figure 4.22:

<!-- b000589 | prose | pages [19] -->
Report Fre- quency Assessment Form

<!-- b000590 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000591 | caption | pages [19] -->
Figure 4.23: Report Frequency of Area A

<!-- b000592 | prose | pages [19] -->
关注数学模型

<!-- b000593 | furniture | pages [19] -->
2

<!-- b000594 | furniture | pages [19] -->
MATHmodels

<!-- b000595 | furniture | pages [19] -->
获取更多资讯

<!-- b000596 | furniture | pages [20] -->
Team # 2123823

<!-- b000597 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000598 | furniture | pages [20] -->
Page 19 of 24

<!-- b000599 | prose | pages [20] -->
while ηki is the random eﬀect factor varying with the observation site. The random eﬀect factor is assumed to obey normal distribution with a mean of zero and constant variance of d2

<!-- b000600 | prose | pages [20] -->
and be independent of each other.

<!-- b000601 | prose | pages [20] -->
k,

<!-- b000602 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000603 | prose | pages [20] -->
Substituting Eq. 4.5.2 into Eq. 4.5.1 yields a regression model with longitudinal data.

<!-- b000604 | prose | pages [20] -->
ij + η0i + η1itij + η2it2

<!-- b000605 | prose | pages [20] -->
yij = b0 + b1tij + b2t2

<!-- b000606 | prose | pages [20] -->
It can be rewritten in the form of the matrix.

<!-- b000607 | prose | pages [20] -->


<!-- b000608 | prose | pages [20] -->


<!-- b000609 | prose | pages [20] -->


<!-- b000610 | prose | pages [20] -->


<!-- b000611 | prose | pages [20] -->
t2

<!-- b000612 | prose | pages [20] -->
yi1

<!-- b000613 | prose | pages [20] -->
1 ti1

<!-- b000614 | prose | pages [20] -->
i1

<!-- b000615 | prose | pages [20] -->


<!-- b000616 | prose | pages [20] -->
,

<!-- b000617 | prose | pages [20] -->


<!-- b000618 | prose | pages [20] -->
,

<!-- b000619 | prose | pages [20] -->
t2

<!-- b000620 | prose | pages [20] -->
yi2

<!-- b000621 | prose | pages [20] -->
1 ti2

<!-- b000622 | prose | pages [20] -->
i2

<!-- b000623 | prose | pages [20] -->
Yi =

<!-- b000624 | prose | pages [20] -->
Xi =

<!-- b000625 | prose | pages [20] -->
...

<!-- b000626 | prose | pages [20] -->
...

<!-- b000627 | prose | pages [20] -->
...

<!-- b000628 | prose | pages [20] -->
... t2

<!-- b000629 | prose | pages [20] -->
yini

<!-- b000630 | prose | pages [20] -->
1 ti3

<!-- b000631 | prose | pages [20] -->
i3

<!-- b000632 | prose | pages [20] -->
ij + εij (4.5.3)

<!-- b000633 | prose | pages [20] -->


<!-- b000634 | prose | pages [20] -->


<!-- b000635 | prose | pages [20] -->


<!-- b000636 | prose | pages [20] -->


<!-- b000637 | prose | pages [20] -->
d2

<!-- b000638 | prose | pages [20] -->
b0

<!-- b000639 | prose | pages [20] -->
0 0 1

<!-- b000640 | prose | pages [20] -->


<!-- b000641 | prose | pages [20] -->
,

<!-- b000642 | prose | pages [20] -->


<!-- b000643 | prose | pages [20] -->


<!-- b000644 | prose | pages [20] -->
d2

<!-- b000645 | prose | pages [20] -->
b1

<!-- b000646 | prose | pages [20] -->
0

<!-- b000647 | prose | pages [20] -->
0

<!-- b000648 | prose | pages [20] -->
b =

<!-- b000649 | prose | pages [20] -->
D =

<!-- b000650 | prose | pages [20] -->
2 d2

<!-- b000651 | prose | pages [20] -->
b2

<!-- b000652 | prose | pages [20] -->
0 0

<!-- b000653 | prose | pages [20] -->
3

<!-- b000654 | prose | pages [20] -->
Vi = XiDXT

<!-- b000655 | prose | pages [20] -->
i + σ2I

<!-- b000656 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000657 | prose | pages [20] -->
in which Yi is assumed to obey normal distribution with a mean vector of Xib and variance matrix of Vi. The estimation of the coeﬃcients requires the application of Maximum Likelihood Estimation (MLE), instead of Original Least Squares (OLS) for it cannot handle cases where the model is not linear. The likelihood function for Yi is given as follows.

<!-- b000658 | prose | pages [20] -->
n ∏

<!-- b000659 | prose | pages [20] -->
2 exp[−1

<!-- b000660 | prose | pages [20] -->
{(2π)−ni

<!-- b000661 | prose | pages [20] -->
2 |Vi|−1

<!-- b000662 | prose | pages [20] -->
L(b, D, σ2) =

<!-- b000663 | prose | pages [20] -->
i=1

<!-- b000664 | prose | pages [20] -->
2(Yi −Xib)TV −1 (Yi −Xib)]} i

<!-- b000665 | prose | pages [20] -->
Finally, by solving the maximum point of the likelihood function L, the estimated values of b, D and σ2 can be calculated.

<!-- b000666 | prose | pages [20] -->
The model’s signiﬁcance is that the ﬁxed eﬀect coeﬃcient bk, which reﬂects the overall eﬀect in the area, can predict the time point of eradication in an average sense. In contrast, the random eﬀect coeﬃcient ηki incorporates the variability between diﬀerent sites (e.g. climate, topography, population), thus assessing the conﬁdence interval of time point of eradication under a certain level.

<!-- b000667 | heading | pages [20] -->
Results and Analysis

<!-- b000668 | prose | pages [20] -->
To determine the local bee population, we use data from the National Agricultural Statistics Services of the USAf, which reports the number of colonies per county where the honey was harvested. To get the valid data on the spread of hornets under controlled conditions, we modify the spread model mentioned in section 4.1 using the regression model with longitudinal data. The period of the controlling process is chosen from April (queens ﬁrst appear) to October (soon to be hibernating)

<!-- b000669 | prose | pages [20] -->
Next, we randomly select 20 areas and predict local bee and sparrow hornet populations’ changes over time after some control measures are taken. Figure 4.24 shows the situation of local bees in three of these areas.

<!-- b000670 | prose | pages [20] -->
fData Source: the National Agricultural Statistics Services of the USA(https://quickstats.nass.usda. gov/results/98D6C754-2F7A-319C95FE-CB8F673A140E)

<!-- b000671 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000672 | prose | pages [20] -->
关注数学模型

<!-- b000673 | furniture | pages [20] -->
2

<!-- b000674 | furniture | pages [20] -->
MATHmodels

<!-- b000675 | furniture | pages [20] -->
获取更多资讯

<!-- b000676 | furniture | pages [21] -->
Team # 2123823

<!-- b000677 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000678 | furniture | pages [21] -->
Page 20 of 24

<!-- b000679 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000680 | caption | pages [21] -->
Figure 4.24: Population of local bees with human intervention

<!-- b000681 | prose | pages [21] -->
We can plot the model results (Figure 4.25) by testing the model with the hypothetical data. When t = 6.83, the sparrow hornet population in the 20 areas of Washington will reach the minimum point with roughly 1; when t = 7.46, the local bee population in these areas will reach the maximum point with approximately 241. Therefore, we can conclude that when the time range is from 6.83 to 7.46, the number of local bees is not less than 240. The number of hornets is not higher than 1, which indicates that the pest has been eradicated in these 20 areas of Washington State. The model can also be used for calculations for other areas of the

<!-- b000682 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000683 | prose | pages [21] -->
state.

<!-- b000684 | caption | pages [21] -->
Figure 4.25: Population changes with and without human intervention

<!-- b000685 | prose | pages [21] -->
5

<!-- b000686 | heading | pages [21] -->
Sensitivity Analysis

<!-- b000687 | prose | pages [21] -->
In our model, the changes of several values may signiﬁcantly impact the model’s results, so we need to analyze them one by one.

<!-- b000688 | heading | pages [21] -->
Model’s Sensitivity in Problem (a)

<!-- b000689 | prose | pages [21] -->
5.1

<!-- b000690 | prose | pages [21] -->
In order to analyze the sensitivity of the weights of Model 1 and Model 2, we select diﬀerent values of β to calculate the precision of the Combined Forecast Model. We select each element in the set {0.1, 0.3, 0.6, 1, 3, 6, 10} in sequence as the value of β. The boxplot is showed below.

<!-- b000691 | caption | pages [21] -->
Figure 5.1: Sensitivity analysis of β

<!-- b000692 | prose | pages [21] -->
It can be concluded from the ﬁgure above that β has little eﬀect on the prediction precision of our model, which shows that our model is robust and very reliable.

<!-- b000693 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000694 | prose | pages [21] -->
关注数学模型

<!-- b000695 | furniture | pages [21] -->
2

<!-- b000696 | furniture | pages [21] -->
MATHmodels

<!-- b000697 | furniture | pages [21] -->
获取更多资讯

<!-- b000698 | furniture | pages [22] -->
Team # 2123823

<!-- b000699 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000700 | furniture | pages [22] -->
Page 21 of 24

<!-- b000701 | heading | pages [22] -->
Model’s Sensitivity in Problem (c)

<!-- b000702 | prose | pages [22] -->
5.2

<!-- b000703 | prose | pages [22] -->
To test the inﬂuence of the value change of the regularization coeﬃcient λ, we pick diﬀerent values of λ and predict the likelihood distribution of sparrow wasps appearing. The predicted

<!-- b000704 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000705 | prose | pages [22] -->
result is shown in Figure 5.2.

<!-- b000706 | caption | pages [22] -->
Figure 5.2: Sensitivity analysis of λ

<!-- b000707 | prose | pages [22] -->
When λ changes within a certain range, the accuracy of our model prediction is stable above 90%. When λ increases over 10, the prediction accuracy of the model drops rapidly. When

<!-- b000708 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000709 | prose | pages [22] -->
lambda is equal to 0.6, our model can achieve the best prediction.

<!-- b000710 | prose | pages [22] -->
6

<!-- b000711 | heading | pages [22] -->
Model Evaluation

<!-- b000712 | heading | pages [22] -->
Strengths:

<!-- b000713 | prose | pages [22] -->
• Comprehensive consideration: We have predicted the spread of the sparrow hornets from both temporal and spatial perspectives, and selected 16 factors to calculate the environmental suitability. Almost every useful factor has been included in Model 1. (see Section 4.1)

<!-- b000714 | prose | pages [22] -->
• Full utilization of information: When evaluating the likelihood distribution of sparrow hornets, we have applied the feature mapping method to expand the 2 features into 28 features, making the most of the features of limited data. (see Section 4.3)

<!-- b000715 | heading | pages [22] -->
• Sophisticated model improvement method: Through pseudo labelling, we are able

<!-- b000716 | prose | pages [22] -->
to make use of unexploited data, which can help improve the accuracy of the original prediction model. (see Section 4.4)

<!-- b000717 | heading | pages [22] -->
Weaknesses:

<!-- b000718 | prose | pages [22] -->
• Insuﬃcient data volume: The ratio of positive to negative reports is too extreme. Al- though we have taken some measures (e.g., ﬂipping the images horizontally and vertically to increase the amount of data) to reduce its negative impact on the training set, we could not eliminate it completely;

<!-- b000719 | prose | pages [22] -->
• Subjective error: When calculating the update frequency, we apply a subjective evalua- tion method to assign weights to ﬁve factors , which is reasonable to some extent but not accurate enough. (see Section 4.4)

<!-- b000720 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000721 | prose | pages [22] -->
关注数学模型

<!-- b000722 | furniture | pages [22] -->
2

<!-- b000723 | furniture | pages [22] -->
MATHmodels

<!-- b000724 | furniture | pages [22] -->
获取更多资讯

<!-- b000725 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000726 | heading | pages [23] -->
Memorandum

<!-- b000727 | prose | pages [23] -->
To: The Washington State Department of Agriculture

<!-- b000728 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000729 | prose | pages [23] -->
From: Team # 2123823

<!-- b000730 | prose | pages [23] -->
Subject: Prediction of the Spread of Sparrow Hornets

<!-- b000731 | prose | pages [23] -->
Date: February 9, 2021

<!-- b000732 | prose | pages [23] -->
Dear Sir:

<!-- b000733 | prose | pages [23] -->
With the growth of trade, transportation and tourism under globalization, the introduction of sparrow hornets is now one of the greatest threats to the ecological system of Washington State. In our work, we have built a series of models in hope to help the government make full

<!-- b000734 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000735 | prose | pages [23] -->
use of the data provided by the public reports to rationalize the deployment of limited resources to conduct investigations.

<!-- b000736 | prose | pages [23] -->
Analyzing the result predicted, we have many important discoveries and advice, which can help you signiﬁcantly improve the eﬃciency of the investigation.

<!-- b000737 | prose | pages [23] -->
i) Focus on the events occurring in the areas with a high likelihood of sparrow hornet

<!-- b000738 | prose | pages [23] -->
appearing, and prioritize investigation of these events. Comparing the environmental suitability between diﬀerent areas, we ﬁnd that there are three area centers ‘friendly’ to sparrow hornet: the ﬁrst is the northwestern coastal region of the United States; the second is the North Cascades National Park and its vicinity on the east coast of the Rosario Strait; the third is the Kootenay National Forest in the interior. Over time, sparrow hornets will migrate to these three area centers. Then combine with the data of the current year, we can accurately predict the distribution of sparrow hornets in the next year. There are detailed data in the text above. You can determine where to deploy the elimination measures to achieve the best eﬀects, given the limited resources of government agencies.

<!-- b000739 | prose | pages [23] -->
ii) Use image recognition and text mining methods to reduce your workload and eﬀectively

<!-- b000740 | prose | pages [23] -->
increase the investigation’s accuracy.

<!-- b000741 | prose | pages [23] -->
In addition, you can encourage people to take pictures or videos of sparrow hornets and upload them on the website to help you estimate the distribution of sparrow hornets. In this process, notes following the pictures or videos will improve the accuracy of your estimation. However, due to the low quality of the photos taken by the public, many of them are not suitable for image recognition, and most of the uploaded notes do not contain useful information. Therefore, you ought to appropriately promote relevant knowledge to the public to improve photos, videos and notes. For example, as to how to take photos of high quality, we suggest that the head, thorax and abdomen of sparrow hornet, which features are apparent, had better be taken in the photos. What’s more, public notes should contain useful information, such as color, stripe and body size and so on.

<!-- b000742 | prose | pages [23] -->
iii) Pay more attention to events taking place in the months of summer, when sparrow hornets

<!-- b000743 | prose | pages [23] -->
tend to be more active, and increase the frequency of investigation and updating data.

<!-- b000744 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000745 | prose | pages [23] -->
关注数学模型

<!-- b000746 | furniture | pages [23] -->
22

<!-- b000747 | furniture | pages [23] -->
22

<!-- b000748 | furniture | pages [23] -->
2

<!-- b000749 | furniture | pages [23] -->
MATHmodels

<!-- b000750 | furniture | pages [23] -->
获取更多资讯

<!-- b000751 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000752 | prose | pages [24] -->
According to results predicted, we ﬁnd that sparrow hornets are most active in July and August. During the period from November to March of the next year, sparrow hornets are almost in hibernation and appear a little, when you had better properly decrease the frequency of investigation and updating data, to avoid the waste of human resources and

<!-- b000753 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000754 | prose | pages [24] -->
material resources.

<!-- b000755 | prose | pages [24] -->
iv) According to the predicted location of the migration of sparrow hornets, notify beekeepers

<!-- b000756 | prose | pages [24] -->
and farmers and other stakeholders in time to avoid unnecessary economic losses. As an alien specie, sparrow hornet tends to hunt bee colonies closer to it on a large scale, causing economic losses.

<!-- b000757 | prose | pages [24] -->
As to how to eradicate the sparrow hornets, after looking up relevant information, we provide several approaches as follows.

<!-- b000758 | prose | pages [24] -->
i) Targeting Queens. The queen in an ethnic group tends to go out in April and October,

<!-- b000759 | prose | pages [24] -->
and you’d better conduct more traps during this time to catch and kill the queen. Once

<!-- b000760 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000761 | prose | pages [24] -->
the queen is dead, this ethnic group will disappear in a short time.

<!-- b000762 | prose | pages [24] -->
ii) Targeting Nests. You can track the sparrow hornets back to the nest, ﬁnd their nest and

<!-- b000763 | prose | pages [24] -->
destroy it.

<!-- b000764 | prose | pages [24] -->
iii) Public Outreach. In daily life, you need to strengthen the popularization of knowledge

<!-- b000765 | prose | pages [24] -->
about pest control.

<!-- b000766 | prose | pages [24] -->
The suggestions above will help you better predict the distribution of sparrow hornets, update the data promptly and more eﬀectively resist the invasion of alien species, protecting the local ecosystem. We sincerely hope that our study will beneﬁt you and better protect the ecology of Washington State, USA.

<!-- b000767 | prose | pages [24] -->
Sincerely,

<!-- b000768 | furniture | pages [24] -->
Team #2123823

<!-- b000769 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000770 | prose | pages [24] -->
关注数学模型

<!-- b000771 | furniture | pages [24] -->
23

<!-- b000772 | furniture | pages [24] -->
23

<!-- b000773 | furniture | pages [24] -->
2

<!-- b000774 | furniture | pages [24] -->
MATHmodels

<!-- b000775 | furniture | pages [24] -->
获取更多资讯

<!-- b000776 | furniture | pages [25] -->
Team # 2123823

<!-- b000777 | heading | pages [25] -->
References

<!-- b000778 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000779 | furniture | pages [25] -->
Page 24 of 24

<!-- b000780 | references | pages [25] -->
[1] Adam M Baker and Daniel A Potter. Invasive paper wasp turns urban pollinator gardens

<!-- b000781 | references | pages [25] -->
into ecological traps for monarch butterﬂy larvae. Scientiﬁc Reports, 10(1):1–7, 2020.

<!-- b000782 | references | pages [25] -->
微信公众号：数学模型

<!-- b000783 | references | pages [25] -->
Retrieved from https://extension.psu.edu/

<!-- b000784 | references | pages [25] -->
[2] Unknown.

<!-- b000785 | references | pages [25] -->
Asian giant hornets.

<!-- b000786 | references | pages [25] -->
asian-giant-hornets Accessed Unknown.

<!-- b000787 | references | pages [25] -->
[3] Muna Maryam Azmy, Tetsuro Hosaka, and Shinya Numata. Responses of four hornet

<!-- b000788 | references | pages [25] -->
species to levels of urban greenness in nagoya city, japan: Implications for ecosystem

<!-- b000789 | references | pages [25] -->
disservices of urban green spaces. Urban Forestry & Urban Greening, 18:117–125, 2016.

<!-- b000790 | references | pages [25] -->
[4] Alberto J Alaniz, Mario A Carvajal, and Pablo M Vergara. Giants are coming? Predicting

<!-- b000791 | references | pages [25] -->
the potential spread and impacts of the giant asian hornet (vespa mandarinia, hymenoptera:

<!-- b000792 | references | pages [25] -->
Vespidae) in the usa. Pest Management Science, 77(1):104–112, 2021.

<!-- b000793 | references | pages [25] -->
[5] MP Robertson, N Caithness, and MH Villet.

<!-- b000794 | references | pages [25] -->
A PCA-based modelling technique for

<!-- b000795 | references | pages [25] -->
predicting environmental suitability for organisms from presence records. Diversity and

<!-- b000796 | references | pages [25] -->
distributions, 7(1-2):15–27, 2001.

<!-- b000797 | references | pages [25] -->
[6] Fernanda L Schumacher, Clecio S Ferreira, Marcos O Prates, Alberto Lachos, and Victor H

<!-- b000798 | references | pages [25] -->
Lachos. A robust nonlinear mixed-eﬀects model for covid-19 deaths data. arXiv preprint

<!-- b000799 | references | pages [25] -->
微信号：MATHmodels

<!-- b000800 | references | pages [25] -->
arXiv:2007.00848, 2020.

<!-- b000801 | references | pages [25] -->
[7] Makoto Matsuura. Comparative biology of the ﬁve japanese species of the genus vespa

<!-- b000802 | references | pages [25] -->
(hymenoptera, vespidae). 1984.

<!-- b000803 | references | pages [25] -->
[8] Makoto Matsuura and Shôichi F Sakagami. A bionomic sketch of the giant hornet, vespa

<!-- b000804 | references | pages [25] -->
mandarinia, a serious pest for japanese apiculture (with 12 text-ﬁgures and 5 tables).

<!-- b000805 | references | pages [25] -->
Journal of the Faculty of Science, Hokkaido University, 19(1):125–162, 1973.

<!-- b000806 | references | pages [25] -->
[9] John M Drake and Robert L Richards. Estimating environmental suitability. Ecosphere,

<!-- b000807 | references | pages [25] -->
9(9):e02373, 2018.

<!-- b000808 | references | pages [25] -->
[10] Ana S Bessa, Joao Carvalho, Alberto Gomes, and Frederico Santarem. Climate and land-

<!-- b000809 | references | pages [25] -->
use drivers of invasion: predicting the expansion of vespa velutina nigrithorax into the

<!-- b000810 | references | pages [25] -->
iberian peninsula. Insect Conservation and Diversity, 9(1):27–37, 2016.

<!-- b000811 | references | pages [25] -->
[11] Ian Goodfellow, Yoshua Bengio, and Aaron Courville. Deep Learning. The MIT Press,

<!-- b000812 | references | pages [25] -->
2016.

<!-- b000813 | references | pages [25] -->
[12] Anand Rajaraman and Jeﬀrey David Ullman. Mining of massive datasets. Cambridge

<!-- b000814 | references | pages [25] -->
University Press, 2011.

<!-- b000815 | references | pages [25] -->
[13] Hao Wu and Saurabh Prasad. Semi-supervised deep learning using pseudo labels for

<!-- b000816 | references | pages [25] -->
hyperspectral image classiﬁcation. IEEE Transactions on Image Processing, 27(3):1259–

<!-- b000817 | references | pages [25] -->
1270, 2017.

<!-- b000818 | references | pages [25] -->
[14] Angelica I Aviles-Rivero, Philip Sellars, Carola-Bibiane Schönlieb, and Nicolas Pa-

<!-- b000819 | references | pages [25] -->
padakis. Graphxcovid: Explainable deep graph diﬀusion pseudo-labelling for identifying

<!-- b000820 | references | pages [25] -->
covid-19 on chest x-rays. arXiv preprint arXiv:2010.00378, 2020.

<!-- b000821 | references | pages [25] -->
[15] Judith H Myers, Anne Savoie, and Ed van Randen. Eradication and pest management.

<!-- b000822 | references | pages [25] -->
Annual review of entomology, 43(1):471–491, 1998.

<!-- b000823 | references | pages [25] -->
[16] Small Banded Pine Weevil. New pest response guidelines. Dec.ny.gov, 2004.

<!-- b000824 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000825 | references | pages [25] -->
关注数学模型

<!-- b000826 | furniture | pages [25] -->
2

<!-- b000827 | furniture | pages [25] -->
MATHmodels

<!-- b000828 | furniture | pages [25] -->
获取更多资讯
