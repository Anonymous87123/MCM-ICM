# P-C-2021-2101166-038bd4c8

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | furniture | pages [1] -->
2021

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | furniture | pages [1] -->
2101166

<!-- b000007 | prose | pages [1] -->
MCM/ICM

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
Fight for Washington State: Can Artiﬁcial

<!-- b000010 | title | pages [1] -->
Intelligence Beat the Asian Giant Hornet?

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
Recently, the Asian giant hornet has been observed in Washington State, which may cause damage to the ecosystem in the future. Therefore, the Washington State Department of Agri- culture (WSDA) has provided large amounts of observations on the species, hoping to get our assistance.

<!-- b000014 | prose | pages [1] -->
For problem 1, we propose two metrics: the resource competition coeﬃcient and the environmental friendliness to construct a time-step diﬀerence equation, and simulate the population dispersal of the Asian giant hornet. We predict the distribution of nests in Washington State within 10 years, and gain the range of activities of an Asian giant hornet

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
by adding noise. The results show that if no measures are taken against the spread of Asian giant hornets, the number of the species will show an approximate exponential growth at the initial stage in Washington State. To evaluate the accuracy of the model, we use Logistic Growth Model to test the accuracy of the model. The loss is 0.076, and the fastest growing year is the seventh year.These results indicate that we need to control the number of nests early.

<!-- b000017 | prose | pages [1] -->
In problem 2, we divide it into feature extraction and image classiﬁcation. For the former, we establish a model based on auto-encoder to condense images information, of which the minimum testing loss dips to 0.0274. For the latter, we build three models, the Binary Logistic Regression, the Support Vector Machine, and the Convolutional Neural Network (CNN). The highest accuracy of the three models on the testing set is 0.5303, 0.5758, and 0.8030 respectively, so we choose CNN as our classiﬁcation model. Finally, we summarize the features of negative images from three aspects: species characteristics, subject deﬁnition and background softness.

<!-- b000018 | prose | pages [1] -->
In terms of problem 3, we conduct Agglomerative Clustering according to the latitude and longitude of each sighting with unveriﬁed or unprocessed status, and divide them into 5 classes. Then we deﬁne the priority of a region based on the positive probabilities of input images in this area. Through analysis, we ﬁnd that Seattle is located in the center of the highest probability area.

<!-- b000019 | prose | pages [1] -->
With regard to problem 4, we update the model with diﬀerent intervals to ﬁnd optimal Selected indicators include the testing loss of auto-encoder and the update time interval. accuracy of CNN in testing dataset. The optimal time interval for updating models is deﬁned as the abscissa corresponding to the extremum of the numerical derivative of the

<!-- b000020 | heading | pages [1] -->
time-varying indicators. Finally, we get the following conclusions: the auto-encoder needs

<!-- b000021 | prose | pages [1] -->
to be updated every four months, and the CNN needs to be updated every three months.

<!-- b000022 | prose | pages [1] -->
As for problem 5, we design a number of variables based on observational data to characterize changes in the number of nests. We eliminate the inﬂuence of the image recognition model based on Bayesian inference. When K converges to 0, we think that the pest has been eradicate.

<!-- b000023 | prose | pages [1] -->
Last but not least, we summarize the suggestions and write a memorandum for the WSDA, to assist relevant departments in biological control.

<!-- b000024 | keywords | pages [1] -->
Keywords: Time-Step Diﬀerence Equation, Auto-Encoder, Convolutional Neural Network,

<!-- b000025 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000026 | prose | pages [1] -->
Agglomerative Clustering 关注数学模型

<!-- b000027 | furniture | pages [1] -->
2

<!-- b000028 | furniture | pages [1] -->
MATHmodels

<!-- b000029 | furniture | pages [1] -->
获取更多资讯

<!-- b000030 | furniture | pages [2] -->
Team # 2101166

<!-- b000031 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000032 | furniture | pages [2] -->
Page 2 of 25

<!-- b000033 | heading | pages [2] -->
Contents

<!-- b000034 | contents | pages [2] -->
1

<!-- b000035 | heading | pages [2] -->
Introduction

<!-- b000036 | prose | pages [2] -->
3 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000037 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000038 | prose | pages [2] -->
Clariﬁcations and Restatements . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000039 | prose | pages [2] -->
2

<!-- b000040 | heading | pages [2] -->
Reasonable Assumptions

<!-- b000041 | prose | pages [2] -->
3

<!-- b000042 | prose | pages [2] -->
4

<!-- b000043 | prose | pages [2] -->
Problem 1: Propagation Simulation Based on Yearly Time-Step Diﬀerence 3 Equation 5 Method Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 5 Model Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 6 Predictions of Population Dispersal . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 8

<!-- b000044 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000045 | heading | pages [2] -->
Problem 2: Image Recognition Model Based on Auto-Encoder and Convo-

<!-- b000046 | prose | pages [2] -->
4 lutional Neural Network 9 Data Cleaning and Data Augmentation . . . . . . . . . . . . . . . . . . . . . . . 4.1 10 The Structure and Training Results of Auto-Encoder . . . . . . . . . . . . . . . 4.2 12 Results of the Binary Classiﬁcation Problem . . . . . . . . . . . . . . . . . . . . 4.3 13 . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 Features for Negative Sightings 14

<!-- b000047 | heading | pages [2] -->
Problem 3: Priority Computation Model Based on Agglomerative Clustering 15

<!-- b000048 | prose | pages [2] -->
5 Region Division . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 15 Positive Probability Prediction and Priority Deﬁnition 5.2 . . . . . . . . . . . . . .

<!-- b000049 | prose | pages [2] -->
17

<!-- b000050 | prose | pages [2] -->
Problem 4: Optimal Updating Strategy Based on Numerical Derivative 6 17

<!-- b000051 | prose | pages [2] -->
Problem 5: Assessment Based on the Bayes Formula 7

<!-- b000052 | prose | pages [2] -->
8

<!-- b000053 | heading | pages [2] -->
Model Analysis

<!-- b000054 | prose | pages [2] -->
19

<!-- b000055 | prose | pages [2] -->
20 Strengths and Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 20 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000056 | prose | pages [2] -->
9

<!-- b000057 | heading | pages [2] -->
Conclusion

<!-- b000058 | heading | pages [2] -->
Appendices

<!-- b000059 | prose | pages [2] -->
21

<!-- b000060 | prose | pages [2] -->
21

<!-- b000061 | prose | pages [2] -->
23

<!-- b000062 | heading | pages [2] -->
Appendix A Core Codes for Auto-Encoder

<!-- b000063 | heading | pages [2] -->
Appendix B Core Codes for CNN

<!-- b000064 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000065 | prose | pages [2] -->
23

<!-- b000066 | prose | pages [2] -->
23

<!-- b000067 | prose | pages [2] -->
关注数学模型

<!-- b000068 | furniture | pages [2] -->
2

<!-- b000069 | furniture | pages [2] -->
MATHmodels

<!-- b000070 | furniture | pages [2] -->
获取更多资讯

<!-- b000071 | furniture | pages [3] -->
Team # 2101166

<!-- b000072 | furniture | pages [3] -->
1

<!-- b000073 | heading | pages [3] -->
Introduction

<!-- b000074 | prose | pages [3] -->
1.1 Problem Background

<!-- b000075 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000076 | furniture | pages [3] -->
Page 3 of 25

<!-- b000077 | prose | pages [3] -->
The Asian giant hornet is the largest hornet in the world, which is native to East Asia,

<!-- b000078 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000079 | prose | pages [3] -->
South Asia, mainland Southeast Asia and some far east parts of the Russian. Recently, it was discovered in the American Northwest at the end of 2019, and there had been lots of sightings in 2020. In fact, the invasion of the Asian giant hornet is not an isolated incident. In 2004, it ﬁrst appeared in Europe, and then began to spread to Spain, Belgium, Portugal and Italy, rapidly. According to European studies, the propagation speed of Asian giant hornet can reach 49.5 kilometers per year [2, 11].

<!-- b000080 | prose | pages [3] -->
Even worse, the Asian giant hornet attacks and hunts variety of insects such as bees, bum- blebees, praying mantises and other insects.

<!-- b000081 | prose | pages [3] -->
Moreover, if the Asian giant hornet reach all suitable habitats in North America, the cost for dealing with this disaster in America will ex- ceed $113.7 millions [1]. Therefore, it is very necessary to ﬁnd and process the Asian giant hornet eﬀectively.

<!-- b000082 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000083 | prose | pages [3] -->
Clariﬁcations and Restatements 1.2

<!-- b000084 | prose | pages [3] -->
In this problem, we are given the data of observations on the Asian giant hornet, which is perceived by local citizens, including the time, location, latitude and longitude, and the cor- responding observation photos. Washington State Department of Agriculture divided observa- tions into four status based on photos, namely: positive, negative, unveriﬁed, and unprocessed. We will solve the following problems based on the historial observations:

<!-- b000085 | heading | pages [3] -->
1. Based on positive observations and corresponding latitudes and longitudes, combined

<!-- b000086 | prose | pages [3] -->
with the biological characteristics of the Asian giant hornet, forecast the short-term spread of the species and analyze the accuracy of the prediction;

<!-- b000087 | heading | pages [3] -->
2. Establish a model for judging whether a photo contains at least an Asian giant hornet,

<!-- b000088 | prose | pages [3] -->
and analyze the image features that make the model output “Negative” results;

<!-- b000089 | heading | pages [3] -->
3. Based on the above classiﬁcation model, deﬁne the government’s priority in handling

<!-- b000090 | prose | pages [3] -->
citizen observations, for the reason that some unprocessed or unveriﬁed observations are most likely to be positive and require the government to explore;

<!-- b000091 | heading | pages [3] -->
4. Consider that more sightings have been observed, determine the update method and

<!-- b000092 | prose | pages [3] -->
update frequency of the model;

<!-- b000093 | heading | pages [3] -->
5. According to the model above, analyze what indicators of Washington State has achieved,

<!-- b000094 | prose | pages [3] -->
it can be said that the pest has been “eliminated”;

<!-- b000095 | heading | pages [3] -->
6. Submit a memorandum to to the Washington State Department of Agriculture to com-

<!-- b000096 | prose | pages [3] -->
prehensively supplement our research results and take corresponding protective measures at the same time.

<!-- b000097 | prose | pages [3] -->
1.3 Our Work

<!-- b000098 | prose | pages [3] -->
In problem 1, we construct and simulate a time-step diﬀerence equation with two metrics: the resource competition coeﬃcient and the environmental friendliness. We use this model to predict the distribution of nests in Washington State. Then, we gain the range of activities of a single Asian giant hornet by adding noise. After that, we use the Logistic Growth Model to test the accuracy of the model.

<!-- b000099 | prose | pages [3] -->
We divide problem 2 into two subproblems: feature extraction, and image classiﬁ-

<!-- b000100 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000101 | prose | pages [3] -->
关注数学模型 In order to reduce the impact of sample imbalance, we apply image ﬂipping and cation.

<!-- b000102 | furniture | pages [3] -->
2

<!-- b000103 | furniture | pages [3] -->
MATHmodels

<!-- b000104 | furniture | pages [3] -->
获取更多资讯

<!-- b000105 | furniture | pages [4] -->
Team # 2101166

<!-- b000106 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000107 | furniture | pages [4] -->
Page 4 of 25

<!-- b000108 | prose | pages [4] -->
Borderline-SMOTE methods for data augmentation ﬁrst, and then divide the data into the training set and the validation set (testing set). Next, we utilize auto-encoder to collect key features of images. To prevent over-ﬁtting, we store the best performance model in the testing set for subsequent use. Next, we establish three models, the Binary Logistic Regression, the Support Vector Machine, and the Convolutional Neural Network. After com-

<!-- b000109 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000110 | prose | pages [4] -->
paring their accuracy on the testing set, we choose CNN as our image classiﬁcation model. Finally, we summarize the main features of having negative labels from three aspects: species characteristics, subject deﬁnition and background softness.

<!-- b000111 | prose | pages [4] -->
As for problem 3, we take the scope of activities of one-time inspection by the government into account, and conduct Agglomerative Clustering according to the latitude and longitude of each sighting. Then we deﬁne the priority of a region based on the positive probabilities of input images.

<!-- b000112 | prose | pages [4] -->
With regard to problem 4, we discuss the eﬀect of updating the model with diﬀerent time intervals on the testing results, including the loss of auto-encoder and the accuracy of CNN. The

<!-- b000113 | heading | pages [4] -->
optimal time interval of updating models is deﬁned as the abscissa corresponding

<!-- b000114 | prose | pages [4] -->
to the extremum of the numerical derivative of the function, which is the maximum value for auto-encoder, and the opposite for CNN.

<!-- b000115 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000116 | prose | pages [4] -->
In terms of problem 5, the number of nests, the range of spatial distribution and the positive ratio in observations can all reﬂect the growth of pests. We design a number of variables to characterize changes in the number of nests. Since the image recognition model has a certain error probability, we have made a correction based on Bayesian inference.

<!-- b000117 | caption | pages [4] -->
Figure 1: The workﬂow.

<!-- b000118 | prose | pages [4] -->
2

<!-- b000119 | heading | pages [4] -->
Reasonable Assumptions

<!-- b000120 | prose | pages [4] -->
Assumptions about the data provided.

<!-- b000121 | prose | pages [4] -->
1. The uploaded location (latitude and longitude) has high accuracy and no deviation from the map on Google1;

<!-- b000122 | prose | pages [4] -->
2. The judgments made by the WSDA based on photos and the corresponding comments is accurate, and there is no error in recognition;

<!-- b000123 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000124 | prose | pages [4] -->
1https://www.google.com/map/ 关注数学模型

<!-- b000125 | furniture | pages [4] -->
2

<!-- b000126 | furniture | pages [4] -->
MATHmodels

<!-- b000127 | furniture | pages [4] -->
获取更多资讯

<!-- b000128 | furniture | pages [5] -->
Team # 2101166

<!-- b000129 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000130 | furniture | pages [5] -->
Page 5 of 25

<!-- b000131 | prose | pages [5] -->
3. The date of the photo was taken is always equal to the corresponding detection date, i.e., there is no delay in uploading photos;

<!-- b000132 | prose | pages [5] -->
4. Whether a photo contains an Asian giant hornet, is independent of the status of other photos.

<!-- b000133 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000134 | prose | pages [5] -->
Assumptions about the behavior of Asian giant hornet.

<!-- b000135 | prose | pages [5] -->
1. When the surrounding geographical environment is similar, the Asian giant hornet preys randomly, as well as the population dispersal. At the same time, the species tends to prey and migrate nearby.

<!-- b000136 | prose | pages [5] -->
2. The Asian giant hornet cannot build nests or prey in the water;

<!-- b000137 | prose | pages [5] -->
3. The environment is similar in diﬀerent regions, so ﬁtted hyperparameters in a certain small area can be regarded as constants. Therefore, hyperparameters can be promoted throughout Washington State.

<!-- b000138 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000139 | prose | pages [5] -->
Problem 1: Propagation Simulation Based on Yearly 3 Time-Step Diﬀerence Equation

<!-- b000140 | prose | pages [5] -->
The parameters used in our analysis in this section are as follows:

<!-- b000141 | caption | pages [5] -->
Table 1: Key parameters for problem 1.

<!-- b000142 | prose | pages [5] -->
Symbol Symbol Interpretation

<!-- b000143 | prose | pages [5] -->
C the set of cells Ei Nt the set of nests Ci γ r the growth rate Nt the number of nests ∆ij σc the predation distance

<!-- b000144 | prose | pages [5] -->
3.1 Method Overview

<!-- b000145 | prose | pages [5] -->
Interpretation

<!-- b000146 | prose | pages [5] -->
the environmental friendliness the resource competition coeﬃcient the resource dependence coeﬃcient the distance between cell i and cell j

<!-- b000147 | prose | pages [5] -->
(a) The life cycle of the Asian giant hornet. (b) Parameter relationship in propagation simulation.

<!-- b000148 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000149 | prose | pages [5] -->
关注数学模型

<!-- b000150 | caption | pages [5] -->
Figure 2: Introduction to pest extinction assessment model.

<!-- b000151 | furniture | pages [5] -->
2

<!-- b000152 | furniture | pages [5] -->
MATHmodels

<!-- b000153 | furniture | pages [5] -->
获取更多资讯

<!-- b000154 | furniture | pages [6] -->
Team # 2101166

<!-- b000155 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000156 | furniture | pages [6] -->
Page 6 of 25

<!-- b000157 | prose | pages [6] -->
By clustering and plotting the existing positive data, we get that there are three nests near the State of Washington currently. Therefore, we set the initial number of nests to 3, and their location coordinates are the center of the latitude and longitude observed by citizens. We build a time-step diﬀerence equation [8] model in years to predict propagation. Based on the probability distribution of each parameter, we utilize Monte Carlo simulation to solve the

<!-- b000158 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000159 | prose | pages [6] -->
model. The workﬂow is shown in Figure 2b.

<!-- b000160 | prose | pages [6] -->
3.2

<!-- b000161 | heading | pages [6] -->
Model Construction

<!-- b000162 | prose | pages [6] -->
Like other wasps, Asian giant hornets are an annual species, and the time points when queens produce male peak females are concentrated in September to November. Therefore, the life of the species has a strong periodicity, which belongs to rigid seasonal behaviour. This type of rigid seasonal behaviour is suitable for constructing a time-step diﬀerence equation, and iterating in units of years. In the annual Monte Carlo simulation, we conduct propagation on a single nest, and then calculate the number of nests each year.

<!-- b000163 | prose | pages [6] -->
Parameters Selection. When building the model, we select several parameters with practical signiﬁcance such as

<!-- b000164 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000165 | prose | pages [6] -->
biological populations and geographic conditions, which are introduced below.

<!-- b000166 | prose | pages [6] -->
First of all, we consider the inﬂuence between nests. Since the Asian giant hornet will inevitably produce more nests when spreads in Washington State, the resources suitable for the species in State of Washington will gradually become scarce, and intraspeciﬁc struggle will be inevitable. Therefore, we constructed a parameter to measure the competition for resources of diﬀerent nests: the intra-species resource competition coeﬃcient Cij, the formula is shown as follows:

<!-- b000167 | prose | pages [6] -->
(

<!-- b000168 | prose | pages [6] -->


<!-- b000169 | prose | pages [6] -->
−∆2

<!-- b000170 | prose | pages [6] -->
 

<!-- b000171 | prose | pages [6] -->
Cij = exp

<!-- b000172 | prose | pages [6] -->
 

<!-- b000173 | prose | pages [6] -->
2σ2

<!-- b000174 | prose | pages [6] -->
(

<!-- b000175 | prose | pages [6] -->
∑

<!-- b000176 | prose | pages [6] -->
  

<!-- b000177 | prose | pages [6] -->
Ci =

<!-- b000178 | prose | pages [6] -->
exp

<!-- b000179 | prose | pages [6] -->


<!-- b000180 | prose | pages [6] -->
j∈N

<!-- b000181 | prose | pages [6] -->
)

<!-- b000182 | prose | pages [6] -->
ij ij

<!-- b000183 | prose | pages [6] -->
c c

<!-- b000184 | prose | pages [6] -->
) , ∀i ∈N, (1)

<!-- b000185 | prose | pages [6] -->
−∆2

<!-- b000186 | prose | pages [6] -->
ij 2σ2 c

<!-- b000187 | prose | pages [6] -->
where ∆ij represents the distance between nest i and nest j, and σc is the predation distance of the Asian giant hornet. According to the knowledge of species biology, the farther the nest is, the smaller the intra-species competition, and when the predation range overlaps, the intra- species competition increases, so Cij is represented by Gaussian competition kernel. Then add up j to obtain the total intra-species resource competition coeﬃcient Ci of nest i.

<!-- b000188 | prose | pages [6] -->
Second, the Asian giant hornet needs to forage and build nests in order to live and breed, so it has certain requirements for the surrounding environment. We constructed an index to measure the quality of the environment near nest i: the environmental friendliness Eij, which mainly measures the geographical environment and spatial distribution of cell j surrounding nest i, reﬂecting the quality of the predation and nesting environment of Asian giant hornets. The formula is shown as follows:

<!-- b000189 | prose | pages [6] -->
(

<!-- b000190 | prose | pages [6] -->
)

<!-- b000191 | prose | pages [6] -->


<!-- b000192 | prose | pages [6] -->
−∆2

<!-- b000193 | prose | pages [6] -->


<!-- b000194 | prose | pages [6] -->
ij

<!-- b000195 | prose | pages [6] -->


<!-- b000196 | prose | pages [6] -->
Eij = exp

<!-- b000197 | prose | pages [6] -->
 

<!-- b000198 | prose | pages [6] -->
2σ2 c

<!-- b000199 | prose | pages [6] -->
(

<!-- b000200 | prose | pages [6] -->
∑

<!-- b000201 | prose | pages [6] -->
−∆2

<!-- b000202 | prose | pages [6] -->
  

<!-- b000203 | prose | pages [6] -->
Ei =

<!-- b000204 | prose | pages [6] -->
exp

<!-- b000205 | prose | pages [6] -->


<!-- b000206 | prose | pages [6] -->
2σ2

<!-- b000207 | prose | pages [6] -->
j∈C

<!-- b000208 | prose | pages [6] -->
· Tj

<!-- b000209 | prose | pages [6] -->
)

<!-- b000210 | prose | pages [6] -->
∀i ∈N, , (2)

<!-- b000211 | prose | pages [6] -->
ij ij

<!-- b000212 | prose | pages [6] -->
· Tj

<!-- b000213 | prose | pages [6] -->
c c

<!-- b000214 | prose | pages [6] -->
where parameter Tj represents the inﬂuence of terrain on environmental adaptation. Owing to the Asian giant hornet cannot prey or build nests at all when it is on the sea, the lake, or the river etc., so Tj equals 0 for all j ∈C, . Washington State haws good agricultural development

<!-- b000215 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000216 | prose | pages [6] -->
关注数学模型 and good natural conditions. Therefore, we believe that places other than sea areas or rivers are

<!-- b000217 | furniture | pages [6] -->
2

<!-- b000218 | furniture | pages [6] -->
MATHmodels

<!-- b000219 | furniture | pages [6] -->
获取更多资讯

<!-- b000220 | furniture | pages [7] -->
Team # 2101166

<!-- b000221 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000222 | furniture | pages [7] -->
Page 7 of 25

<!-- b000223 | prose | pages [7] -->
more suitable for the survival of the Asian giant hornet, so Tj is 1 for any cell j on land. From the perspective of spatial distribution, cell j that is closer to nest i is more environmentally friendly to nest i, so Eij is represented by the product of Gaussian competition kernel and Tj. Calculate the Eij of nest i and cell j, and add up to j to obtain the total environmental friendliness Ei of nest i.

<!-- b000224 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000225 | prose | pages [7] -->
Model Hyperparameters Selection. For the total number of nests in a region, because of the small spatial range in the early stage of growth, the inﬂuence of spatial distribution on the total number of nests can be ignored. Therefore, we set the total number of nests in year t as Nt. According to the growth characteristics of nests, the total number of nests in year t is related to the situation in year t −1. We set Nt as a random variable and obey the following Poisson distribution formula. The expression of Nt is:

<!-- b000226 | prose | pages [7] -->
Nt = Poisson

<!-- b000227 | prose | pages [7] -->
( (

<!-- b000228 | prose | pages [7] -->
)

<!-- b000229 | prose | pages [7] -->
rNt−1

<!-- b000230 | prose | pages [7] -->
, (3)

<!-- b000231 | prose | pages [7] -->
1 + γ ¯CNt−1

<!-- b000232 | prose | pages [7] -->
where r and γ are hyperparameters, respectively, representing growth rate and resource depen- dence coeﬃcient. For parameter ¯C, we comprehensively consider the spatial distribution in the area, and the average is taken over all cells i and j in this area.The expression of ¯C is shown

<!-- b000233 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000234 | prose | pages [7] -->
as follows:

<!-- b000235 | prose | pages [7] -->
∑

<!-- b000236 | prose | pages [7] -->
∑

<!-- b000237 | prose | pages [7] -->
1 ¯C = |C|2

<!-- b000238 | prose | pages [7] -->
i∈C

<!-- b000239 | prose | pages [7] -->
j∈C

<!-- b000240 | prose | pages [7] -->
Time-Step Diﬀerence Equation.

<!-- b000241 | prose | pages [7] -->
(

<!-- b000242 | prose | pages [7] -->
)

<!-- b000243 | prose | pages [7] -->
−∆2

<!-- b000244 | prose | pages [7] -->
ij

<!-- b000245 | prose | pages [7] -->
exp

<!-- b000246 | prose | pages [7] -->
.

<!-- b000247 | prose | pages [7] -->
(4)

<!-- b000248 | prose | pages [7] -->
2σ2 c

<!-- b000249 | prose | pages [7] -->
After the above calculation, we construct an equation to measure nest i “fertility” Qi, which represents the number of successfully fertilized new queens produced by nest i in a certain year:

<!-- b000250 | prose | pages [7] -->
)

<!-- b000251 | prose | pages [7] -->
( r · Ei

<!-- b000252 | prose | pages [7] -->
Qi = Poisson

<!-- b000253 | prose | pages [7] -->
∀i ∈N. , (5)

<!-- b000254 | prose | pages [7] -->
1 + γCi

<!-- b000255 | prose | pages [7] -->
According to biological knowledge, when the growth rate r is larger, the overall environ- mental friendliness Ei is larger, and the Qi of nest i is larger. When the total intra-species resource competition coeﬃcient Ci is larger, the resource dependence coeﬃcient γ is larger, the Qi of nest i is smaller. Therefore, r and Ei are proportional to Qi, and Ci and are inversely proportional to Qi. According to reference materials, the queen’s successful fertilization rate is only 35%, i.e., P0 = 35%. Considering that some factors such as temperature and crowd density are not taken into consideration, instead of setting it to a constant, we set Qi to a Poisson distribution, and introduce a certain noise to be more in line with the actual situation.

<!-- b000256 | prose | pages [7] -->
For the spatial distribution, we use Pij to represent the probability that the new queen goes from nest i to cell j to build a nest. The expression of Pij is as follows:

<!-- b000257 | prose | pages [7] -->
(

<!-- b000258 | prose | pages [7] -->
)

<!-- b000259 | prose | pages [7] -->
−∆ij

<!-- b000260 | prose | pages [7] -->
Pij = exp

<!-- b000261 | prose | pages [7] -->
µ

<!-- b000262 | prose | pages [7] -->
· Tj, ∀i ∈N, j ∈C.

<!-- b000263 | prose | pages [7] -->
(6)

<!-- b000264 | prose | pages [7] -->
Considering that the Asian giant hornet cannot nest in sea areas or rivers, the terrain parameter Tj will aﬀect Pij. In terms of spatial distribution, because organisms always migrate to the nearest base when they migrate, that is, as the distance between nest i and cell j increases, the probability of migration to cell j decreases, which is expressed as an exponential in the formula.

<!-- b000265 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000266 | prose | pages [7] -->
关注数学模型

<!-- b000267 | furniture | pages [7] -->
2

<!-- b000268 | furniture | pages [7] -->
MATHmodels

<!-- b000269 | furniture | pages [7] -->
获取更多资讯

<!-- b000270 | furniture | pages [8] -->
Team # 2101166

<!-- b000271 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000272 | furniture | pages [8] -->
Page 8 of 25

<!-- b000273 | prose | pages [8] -->
Predictions of Population Dispersal 3.3

<!-- b000274 | heading | pages [8] -->
Algorithm 1: Simulation of the Asian giant hornet propagation

<!-- b000275 | prose | pages [8] -->
Input: Due time Ttotal, number of the initial population N0 and corresponding

<!-- b000276 | prose | pages [8] -->
coordinates (x0, y0), growth rate r, resource dependence coeﬃcient γ.

<!-- b000277 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000278 | prose | pages [8] -->
Output: Population number Nt and its corresponding coordinates (xt, yt).

<!-- b000279 | heading | pages [8] -->
1 Initialize the set of cells C and the set of nests N0 based on N0 and (x0, y0);

<!-- b000280 | heading | pages [8] -->
2 for t = 0 to Ttotal −1 do

<!-- b000281 | prose | pages [8] -->
for i ∈Nt do 3

<!-- b000282 | prose | pages [8] -->
Calculate Ci and Ei based on Equations (1) and (2); 4

<!-- b000283 | prose | pages [8] -->
Randomly select Qi based on Equation (5); 5

<!-- b000284 | prose | pages [8] -->
Calculate Pij for each j ∈C based on Equation (6); 6

<!-- b000285 | prose | pages [8] -->
Set Pi = (Pij)|C|×1 for all j ∈C; 7

<!-- b000286 | prose | pages [8] -->
for x = 0 to Qi do 8

<!-- b000287 | prose | pages [8] -->
Selecting a destination j based on the probability vector Pi; 9

<!-- b000288 | prose | pages [8] -->
Add j into Nt+1; 10

<!-- b000289 | prose | pages [8] -->
end 11

<!-- b000290 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000291 | prose | pages [8] -->
end 12

<!-- b000292 | prose | pages [8] -->
return Nt+1 and its corresponding coordinates (xt+1, yt+1); 13

<!-- b000293 | heading | pages [8] -->
14 end

<!-- b000294 | caption | pages [8] -->
Figure 3: The results of problem 1, including predicted propagation diagrams (subﬁgure a to

<!-- b000295 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000296 | prose | pages [8] -->
f) and the ﬁtted logistic curve (subﬁgure g).

<!-- b000297 | prose | pages [8] -->
关注数学模型

<!-- b000298 | furniture | pages [8] -->
2

<!-- b000299 | furniture | pages [8] -->
MATHmodels

<!-- b000300 | furniture | pages [8] -->
获取更多资讯

<!-- b000301 | furniture | pages [9] -->
Team # 2101166

<!-- b000302 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000303 | furniture | pages [9] -->
Page 9 of 25

<!-- b000304 | prose | pages [9] -->
Finally, by iterating the time-step diﬀerence equation in years according to 1, we got the results of the Asian giant hornet spreading around Washington State. There are two series of results. The ﬁrst series is the result of the location of the Asian giant hornet’s nest, and the second series is the result of a single hornet observed when the Asian giant hornet preys and wanders near the nest during propagation.

<!-- b000305 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000306 | prose | pages [9] -->
The pictures2 in Figure 3 show our results. Subﬁgure (a) to (c) in Figure 3 are migration process of nests of the Asian giant hornet and the red points are nests of hornets. Subﬁgure(d) to (f) in Figure 3 are the activity range of the Asian giant hornet in the current year.

<!-- b000307 | prose | pages [9] -->
It can be seen from the propagation image of nest that at the beginning of the simulation, the growth was slow, and the spread of the Asian giant hornet accelerated after the number of nests had reached a certain number. This phenomenon is consistent with biological knowledge.

<!-- b000308 | prose | pages [9] -->
Error Analysis Based on Logistic Growth Model. We utilize the Logistic Equation to measure the accuracy of our constructed model, which can be calculated as:

<!-- b000309 | prose | pages [9] -->
N · er(t−t0)

<!-- b000310 | prose | pages [9] -->
1 + N (er(t−t0) −1),

<!-- b000311 | prose | pages [9] -->
f(t) =

<!-- b000312 | prose | pages [9] -->
(7)

<!-- b000313 | prose | pages [9] -->
where r represents growth rate in time-step diﬀerence equation model, t0 represents the year

<!-- b000314 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000315 | prose | pages [9] -->
with the fastest growth, and N represents stable population of the Asian giant hornet.

<!-- b000316 | prose | pages [9] -->
We have performed eleven iterations using the annual time-step diﬀerence equation. We use the RMSProp optimizer to ﬁt the Logistic Equation, and apply the MSE as loss function, with the minimum value 0.076. The ﬁtting result shows that the fastest growing year of the Asian giant hornet is 2027, which means t0 equals to 7. Due to the excellent ﬁtting results, our model and the corresponding predictions conform to the actual theory of ecology.

<!-- b000317 | heading | pages [9] -->
Problem 2: Image Recognition Model Based on Auto-

<!-- b000318 | prose | pages [9] -->
4 Encoder and Convolutional Neural Network

<!-- b000319 | caption | pages [9] -->
Figure 4: The structure diagram of Convolutional Neural Network.

<!-- b000320 | prose | pages [9] -->
In the past decade, deep learning has been made a great success in both computer vision [9], speech recognition [5, 12] and even in playing Atari games [10]. A wild range of neural network architectures have been utilized including fully connected neural networks, convolutional neural networks, and recurrent neural network to those problems.

<!-- b000321 | prose | pages [9] -->
For problem 2, we establish two models based on auto-encoder [14] and convolutional neural One for feature extraction, and the other for prediction. network [4] respectively.

<!-- b000322 | prose | pages [9] -->
In this section, we will ﬁrst introduce our methods of data cleaning and data augmentation; and then, we will introduce the structure of auto-encoder and CNN, and give the prediction results on the

<!-- b000323 | prose | pages [9] -->
2The background is downloaded from Google map: https://www.google.com/maps/@48.5668576,-121.5766197,6.8z?hl=en.

<!-- b000324 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000325 | prose | pages [9] -->
关注数学模型

<!-- b000326 | furniture | pages [9] -->
2

<!-- b000327 | furniture | pages [9] -->
MATHmodels

<!-- b000328 | furniture | pages [9] -->
获取更多资讯

<!-- b000329 | furniture | pages [10] -->
Team # 2101166

<!-- b000330 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000331 | furniture | pages [10] -->
Page 10 of 25

<!-- b000332 | prose | pages [10] -->
validation set; ﬁnally, we will summarize the image features that are most possibly identiﬁed as “Negative” by our model.

<!-- b000333 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000334 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000335 | caption | pages [10] -->
Figure 5: The structure diagram of Auto-Encoder.

<!-- b000336 | prose | pages [10] -->
Data Cleaning and Data Augmentation 4.1

<!-- b000337 | prose | pages [10] -->
As mentioned at part 1.2, we are given 4426 sightings of the Asian giant hornet, with 4 diﬀerent status conﬁrmed by the government: positive, negative, unveriﬁed, and unprocessed. The evidences provided by each sighting include image format, video format and even Microsoft Word format. We manually converted all the other format to image: the most suitable frame was extracted from videos, and save all the pictures in each Word or PDF. and remain 2127 valid observations in total.

<!-- b000338 | prose | pages [10] -->
(a) For negative sightings’ comments length.

<!-- b000339 | prose | pages [10] -->
(b) For positive sightings’ comments length.

<!-- b000340 | caption | pages [10] -->
Figure 6: Frequency histograms of the comment length.

<!-- b000341 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000342 | prose | pages [10] -->
关注数学模型 As shown in Figure 6, the probability distributions of the length of comments with diﬀerent

<!-- b000343 | furniture | pages [10] -->
2

<!-- b000344 | furniture | pages [10] -->
MATHmodels

<!-- b000345 | furniture | pages [10] -->
获取更多资讯

<!-- b000346 | furniture | pages [11] -->
Team # 2101166

<!-- b000347 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000348 | furniture | pages [11] -->
Page 11 of 25

<!-- b000349 | prose | pages [11] -->
status are similar. For a more detailed discussion, we build a linear model, with the status x (0/1) as input and the length of corresponding comment y as output:

<!-- b000350 | prose | pages [11] -->
y = β0 + β1x + ϵ, (8)

<!-- b000351 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000352 | prose | pages [11] -->
where β0 and β1 are parameters to be ﬁtted, and ϵ is an unobservable error term, which obeys normal distribution.

<!-- b000353 | caption | pages [11] -->
Table 2: Variance analysis for the linear regression model.

<!-- b000354 | prose | pages [11] -->
Mean

<!-- b000355 | prose | pages [11] -->
Degrees of

<!-- b000356 | prose | pages [11] -->
Sum of

<!-- b000357 | prose | pages [11] -->
Value of F Signiﬁcance of F

<!-- b000358 | prose | pages [11] -->
Square (MS)

<!-- b000359 | prose | pages [11] -->
Freedom

<!-- b000360 | prose | pages [11] -->
Squares (SS)

<!-- b000361 | prose | pages [11] -->
17382.96 Regression 1 17382.96 1.097 × 108 3.25 0.072 5346.42 Error 2052 1.099 × 108 Total 2053

<!-- b000362 | caption | pages [11] -->
Table 2 shows the result of variance analysis and the corresponding signiﬁcance. We can

<!-- b000363 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000364 | prose | pages [11] -->
tell from the regression model that under the condition of 5% signiﬁcance, whether the image is positive or not has no signiﬁcant relationship with the length of comments sent when people upload the picture (the signiﬁcance of F is bigger than 0.05). Therefore, we can conclude that the comments when uploading an image have nothing to do with the status of the image itself at the signiﬁcance level of 0.05, so we only use images in the subsequent analysis, not the corresponding comments.

<!-- b000365 | prose | pages [11] -->
Data Cleaning. After deleting the invalid sightings, we divide the data set into four groups according to the status of each observation.

<!-- b000366 | prose | pages [11] -->
There are 2043 sighting with negative status, 11 with positive, 67 with unveriﬁed, and 5 with unprocessed. In order to verify the training eﬀect of the model, we divide the data set into the training set and the testing or veriﬁcation set.

<!-- b000367 | prose | pages [11] -->
Reasons for Augmentation. According to the result of above, we ﬁnd that the number of negative observations is above 2000, while the number of positive sightings is only 193. Such imbalance of positive and negative samples will lead to various problems in model training [13], such as under ﬁtting, gradient disappearance and so on. Therefore, in this paper, we ﬁrst ﬂip the positive images in three directions (vertical, horizontal and diagonal) to form 76 images including the original image; then we select 28 of them as the testing set, the rest as the training set, and randomly select 38 negative images as the testing set. However, the number of positive images in the training set (48) is still signiﬁcantly less than the number of negative images, so we use the unbalanced data sampling method.

<!-- b000368 | prose | pages [11] -->
Methods for Augmentation. SMOTE (synthetic minority oversampling technique) [3] is an improved oversampling algorithm based on random sampling, which is easy to implement but has some obvious disadvantages at the same time. SMOTE treats all the minority samples equally and does not consider the class information of the nearest neighbor samples, it often leads to aliasing of samples, resulting in poor classiﬁcation eﬀect. Borderline-SMOTE [6] is an improved over sampling algorithm based on SMOTE, which only uses a few class samples on the boundary to synthesize new samples, so as to improve the class distribution of samples. According to [13], when dealing with the problem of binary classiﬁcation, the ratio of positive and negative samples should not be less than 1 : 4. Therefore, we sampled 697 observations from the original 48 positive training sets through Borderline-SMOTE for subsequent training.

<!-- b000369 | prose | pages [11] -->
3We download 8 more images of the species from 2021MCM_ProblemC_Vespamandarinia.pdf.

<!-- b000370 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000371 | prose | pages [11] -->
关注数学模型

<!-- b000372 | furniture | pages [11] -->
2

<!-- b000373 | furniture | pages [11] -->
MATHmodels

<!-- b000374 | furniture | pages [11] -->
获取更多资讯

<!-- b000375 | furniture | pages [12] -->
Team # 2101166

<!-- b000376 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000377 | furniture | pages [12] -->
Page 12 of 25

<!-- b000378 | heading | pages [12] -->
The Structure and Training Results of Auto-Encoder

<!-- b000379 | prose | pages [12] -->
4.2

<!-- b000380 | prose | pages [12] -->
As is shown in Figure 5, we establish an Auto-Encoder to reduce the dimension of input images, as well as extract their key features. The model has two main parts, the encoder and the decoder. In the following subsection, we will introduce the structure of these two parts in

<!-- b000381 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000382 | prose | pages [12] -->
detail.

<!-- b000383 | prose | pages [12] -->
The Structure of Encoder. The encoder contains 4 convolutional blocks. Each block has 4 parts, the convolution, the activation function, the batch normalization, and the down sampling (pooling). For the convolution part, when we take x1 ∈RC × RH × RW as input, we will get an output x2 ∈RC′ × RH′ × RW ′. The dimensions of x2 depend on parameters of convolution (channel, padding, stride, and kernel size) and the stride of down sampling. In order to simplify the calculation, we set the channel equals to 2C, the padding and the stride equals to 1, the kernel to 3x3 shape, and the stride of down sampling equals 2, which contribute to x2 ∈R2C × RH/2 × RW/2. Therefore, if we input an image x1 ∈RC × RH × RW

<!-- b000384 | prose | pages [12] -->
to our encoder, the output tensor x2 will be shape (24C, 2−4H, 2−4W), which will be activated by ReLU function.

<!-- b000385 | prose | pages [12] -->
The Structure of Decoder. Similar to the encoder, our decoder contains 4 deconvolu-

<!-- b000386 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000387 | prose | pages [12] -->
tional blocks with the deconcolution part, the up sampling part, and the activation function. The only diﬀerence between the parameters of decoder and encoder is that, we set the channel equals to C/2 rather than 2C. Therefore, if we input an image x1 ∈RC × RH × RW to our decoder, the output tensor x2 will be shape (2−4C, 24H, 24W), which will be also activated by ReLU function.

<!-- b000388 | prose | pages [12] -->
Training Results of Auto-Encoder. We set the loss function as MSE, which can be calculated as follows:

<!-- b000389 | prose | pages [12] -->
f(x1, x2) = ||x1 −x2||2

<!-- b000390 | prose | pages [12] -->
2, (9)

<!-- b000391 | prose | pages [12] -->
where x1 and x2 are inputs. Figure 7a shows the trend of training losses and testing losses with the increase of training iterations. To increase the robustness of the model, we regard the model with the smallest testing loss as the best, and save its weights and biases for subsequent use. The minimum testing loss during the training is 0.0274 after training 1605 iterations. Figure 7b are examples of input image and decoded image, output by the best model.

<!-- b000392 | prose | pages [12] -->
(a) The loss curve for auto-encoder.

<!-- b000393 | prose | pages [12] -->
(b) Examples of auto-encoder.

<!-- b000394 | caption | pages [12] -->
Figure 7: The loss curve and results for auto-encoder.

<!-- b000395 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000396 | prose | pages [12] -->
关注数学模型

<!-- b000397 | furniture | pages [12] -->
2

<!-- b000398 | furniture | pages [12] -->
MATHmodels

<!-- b000399 | furniture | pages [12] -->
获取更多资讯

<!-- b000400 | furniture | pages [13] -->
Team # 2101166

<!-- b000401 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000402 | furniture | pages [13] -->
Page 13 of 25

<!-- b000403 | heading | pages [13] -->
Results of the Binary Classiﬁcation Problem

<!-- b000404 | prose | pages [13] -->
4.3

<!-- b000405 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000406 | caption | pages [13] -->
Figure 8: The workﬂow of predicting whether an input image contains an Asian giant hornet.

<!-- b000407 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000408 | prose | pages [13] -->
After extract features of input images by auto-encoder, we build three models: Binary Logistic Regression, Support Vector Machine (SVM), and Convolutional Neural Network (CNN) for forecasting. The workﬂow is shown in Figure 8, when we have an image to be recognized, we ﬁrst put it into auto-encoder, and take the output of encoder as the classiﬁcation model’s input, and then we will get the probability of positive or negative (they are equivalent because they always add up to one). After comparing the performance of each model on the testing set, we ﬁnally choose CNN as our prediction model.

<!-- b000409 | prose | pages [13] -->
Binary Logistic Regression. We utilize L2 norm as cost function which supposed to be minimized, and apply Newton’s method for iterative optimization. After optimization, the accuracy of the model in the testing set reaches 0.5303.

<!-- b000410 | prose | pages [13] -->
Support Vector Machine. Due to the small amount of samples and the large number of features, we use Gaussian kernel to experiment, and adjust the γ parameter, which inﬂuences the Gauss’s range of action corresponding to each support vector. We set γ range from 0 to 2 with an interval of 0.01. The maximum accuracy of testing set reaches 0.5758 when γ = 1.64.

<!-- b000411 | prose | pages [13] -->
Convolutional Neural Network. As shown in Figure 4, CNN contains 2 convolutional blocks with batch normalization, and two fully connected layers. To prevent over ﬁtting, the ﬁrst layer has a 25% probability of dropping connections between nerves. We utilize the Cross Entropy loss while training, which can be calculated as follows:

<!-- b000412 | prose | pages [13] -->
∑

<!-- b000413 | prose | pages [13] -->
H(p, q) = −

<!-- b000414 | prose | pages [13] -->
p(x) log q(x), (10)

<!-- b000415 | prose | pages [13] -->
x x

<!-- b000416 | prose | pages [13] -->
where p and q are two diﬀerent probability density functions of the same random variable x, and p represents the ground truth and q is the current estimation. In our case, x is an input image, and both p and q are the PDFs of 0-1 distribution, whose output implies the probability of input x. Figure 9a shows the trend of losses and the accuracy in testing set. Similar to auto- encoder, we regard the model with the maximum accuracy in testing set as the best model, and save its weights and biases. The maximum accuracy reaches 0.8030 after training 490 iterations. Figure 9b are 6 examples predictions sampled randomly, 5 of which are correct.

<!-- b000417 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000418 | prose | pages [13] -->
关注数学模型

<!-- b000419 | furniture | pages [13] -->
2

<!-- b000420 | furniture | pages [13] -->
MATHmodels

<!-- b000421 | furniture | pages [13] -->
获取更多资讯

<!-- b000422 | furniture | pages [14] -->
Team # 2101166

<!-- b000423 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000424 | furniture | pages [14] -->
Page 14 of 25

<!-- b000425 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000426 | prose | pages [14] -->
(a) The loss curve and testing accuracy for CNN.

<!-- b000427 | prose | pages [14] -->
(b) Examples of predictions and labels.

<!-- b000428 | caption | pages [14] -->
Figure 9: The loss curve and results for CNN.

<!-- b000429 | prose | pages [14] -->
Features for Negative Sightings 4.4

<!-- b000430 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000431 | caption | pages [14] -->
Figure 10: Pictures with the highest negative probability and corresponding values.

<!-- b000432 | caption | pages [14] -->
Figure 10 shows the 10 images with the highest negative probability. The predictions about

<!-- b000433 | prose | pages [14] -->
these pictures are all correct, i.e., ground truths of images above are all negative. To summarize, pictures containing following features are tend to be recognized as negative:

<!-- b000434 | heading | pages [14] -->
1. Other species in the picture, not wasps, let alone the Asian giant hornet.

<!-- b000435 | prose | pages [14] -->
Obviously, there is an insect resembling a dragonﬂy in Figure 10a. Figure 10 is deﬁnitely not an Asian giant hornet, because the Asian giant hornet should have wings. Figure 10j contains something similar to a cocoon.

<!-- b000436 | heading | pages [14] -->
2. The insect is too small. For both Figure 10f, Figure 10d, and Figure 10h, the insects

<!-- b000437 | prose | pages [14] -->
are too small to distinguish.

<!-- b000438 | heading | pages [14] -->
3. The background is diﬃcult to discriminate from the insect itself. For Figure 10f

<!-- b000439 | prose | pages [14] -->
and Figure 10g we can’t even see where the insect is at a glance because of its background.

<!-- b000440 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000441 | prose | pages [14] -->
关注数学模型

<!-- b000442 | furniture | pages [14] -->
2

<!-- b000443 | furniture | pages [14] -->
MATHmodels

<!-- b000444 | furniture | pages [14] -->
获取更多资讯

<!-- b000445 | furniture | pages [15] -->
Team # 2101166

<!-- b000446 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000447 | furniture | pages [15] -->
Page 15 of 25

<!-- b000448 | prose | pages [15] -->
In conclusion, for problem 2, we ﬁrst clean the data and apply Borderline-SMOTE method to deal with the imbalanced training set. Next, we build a model to extract features in images based on auto-encoder. After that, we build 3 models, the Binary Logistic Regression, the SVM, and the CNN, and compare their performance on testing set, and select CNN for subsequent use. Finally, we choose 10 pictures with the highest negative probability output by CNN, and

<!-- b000449 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000450 | prose | pages [15] -->
summarize their three most salient common characteristics.

<!-- b000451 | heading | pages [15] -->
Priority Computation Model Based on

<!-- b000452 | prose | pages [15] -->
5 Problem 3: Agglomerative Clustering

<!-- b000453 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000454 | caption | pages [15] -->
Figure 11: The workﬂow of problem 3.

<!-- b000455 | prose | pages [15] -->
In this section, we ﬁrst conduct further screening based on the data set processed in problem 2. We select all valid data with unprocessed or unveriﬁed status, 63 in total. Next, we input each image into the prediction procedure shown in Figure 2b, and get the positive probability of each image. Meanwhile, we take the scope of activities of one-time inspection by government personnel into account, and conduct Agglomerative Clustering according to the latitude and longitude of each sighting, and divide them into ﬁve categories. Then, combining the clustering results and positive probabilities, we deﬁne the priority of a region, and ﬁnally we provide suggestions based on this priority for future treatments of government departments.

<!-- b000456 | prose | pages [15] -->
5.1 Region Division

<!-- b000457 | prose | pages [15] -->
Agglomerative clustering starts from n clusters, where n is the total number of samples. Each cluster initially contains only one object, and then the two most similar clusters are merged in each iteration, until a cluster almost containing all the data is formed. According to how to deﬁne the diﬀerences between diﬀerent clusters, there are three variants of the algorithm, the single link (nearest neighbor), the complete link (furthest neighbor), and the average link. In this paper, we utilize the ﬁrst method to calculate distances between clusters, shown as follows:

<!-- b000458 | prose | pages [15] -->
D(I, J ) = i∈I,j∈J dij, min (11)

<!-- b000459 | prose | pages [15] -->
where i and j are points in cluster I and cluster J , respectively. dij represents the Euclidean distance between point i and point j, which is calculated according to their longitude and latitude, and D(I, J ) means the distance between the two diﬀerent clusters.

<!-- b000460 | prose | pages [15] -->
We utilize the siloette coeﬃcient [7] to evaluate the quality of clustering.

<!-- b000461 | prose | pages [15] -->
In order to calculate the siloette coeﬃcient of point i in cluster I, we ﬁrst deﬁne:

<!-- b000462 | prose | pages [15] -->


<!-- b000463 | prose | pages [15] -->
J̸ =I D(J , I)

<!-- b000464 | prose | pages [15] -->
K = arg min

<!-- b000465 | prose | pages [15] -->
  

<!-- b000466 | prose | pages [15] -->
∑

<!-- b000467 | prose | pages [15] -->
a(i) = 1

<!-- b000468 | prose | pages [15] -->


<!-- b000469 | prose | pages [15] -->
dij,

<!-- b000470 | prose | pages [15] -->
 

<!-- b000471 | prose | pages [15] -->
|I|

<!-- b000472 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000473 | prose | pages [15] -->
j∈I

<!-- b000474 | prose | pages [15] -->
∑

<!-- b000475 | prose | pages [15] -->
, (12)

<!-- b000476 | prose | pages [15] -->
b(i) = 1

<!-- b000477 | prose | pages [15] -->
dik

<!-- b000478 | prose | pages [15] -->
|K|

<!-- b000479 | prose | pages [15] -->
关注数学模型

<!-- b000480 | prose | pages [15] -->
k∈K

<!-- b000481 | furniture | pages [15] -->
2

<!-- b000482 | furniture | pages [15] -->
MATHmodels

<!-- b000483 | furniture | pages [15] -->
获取更多资讯

<!-- b000484 | furniture | pages [16] -->
Team # 2101166

<!-- b000485 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000486 | furniture | pages [16] -->
Page 16 of 25

<!-- b000487 | prose | pages [16] -->
where a(i) means the average of distance from i to all other points in cluster I. K is the closet cluster to I, and b(i) means the average distance from i to all points in cluster K. Then, the siloette coeﬃcient S(i) can be calculated as:

<!-- b000488 | prose | pages [16] -->
b(i) −a(i) S(i) = max{a(i), b(i)}, (13)

<!-- b000489 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000490 | prose | pages [16] -->
then the siloette coeﬃcient ¯S of the current clustering scheme is simply the average of S(i).

<!-- b000491 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000492 | prose | pages [16] -->
(a) The curve of Silhouette Coeﬃcient changing with the number of clusters.

<!-- b000493 | prose | pages [16] -->
(c) The number of clusters is equal to two.

<!-- b000494 | prose | pages [16] -->
(b) The dendrogram of Agglomerative Clustering when 5 clusters.

<!-- b000495 | prose | pages [16] -->
(d) The number of clusters is equal to ﬁve.

<!-- b000496 | caption | pages [16] -->
Figure 12: Images for clustering results.

<!-- b000497 | prose | pages [16] -->
To select the best number of clusters, we calculate the siloette coeﬃcient with the number of clusters varies from 2 to 9, shown in Figure 12a. From the Figure we can tell that cluster samples into 2 classes has the best ¯S, followed by 5 clusters. In order to further select the most suitable number of clusters, we calculate the maximum distance points belong to the same cluster and its corresponding distance when the number of clusters is 2 and 5 respectively. The result of clustering is shown in Figure 12c and Figure 12d. In the case of diﬀerent number of categories, the maximum distance pair of points in the same clusters is 329.2 kilometers when we divide the system into 2 classes, which is far beyond the diameter of a single operation of the government. When 5 groups were clustered, the value drops to 189.6 and decreases by 42%. A diameter of nearly 200 kilometers seems to make sense. Therefore, we decide to cluster the system into 5 groups, whose dendrogram is shown in Figure 12b.

<!-- b000498 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000499 | prose | pages [16] -->
关注数学模型

<!-- b000500 | furniture | pages [16] -->
2

<!-- b000501 | furniture | pages [16] -->
MATHmodels

<!-- b000502 | furniture | pages [16] -->
获取更多资讯

<!-- b000503 | furniture | pages [17] -->
Team # 2101166

<!-- b000504 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000505 | furniture | pages [17] -->
Page 17 of 25

<!-- b000506 | prose | pages [17] -->
Positive Probability Prediction and Priority Deﬁnition 5.2

<!-- b000507 | prose | pages [17] -->
We assume that whether a photo contains an Asian giant hornet, is independent of the status of other photos. Therefore, when we take n pictures as a system x = (x1, x2, · · · , xn), the probability of the whole system being positive Pr(x) is as follows:

<!-- b000508 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000509 | prose | pages [17] -->
Pr(x) = Pr(x1 ∪x2 ∪· · · ∪xn)

<!-- b000510 | prose | pages [17] -->
n ∏

<!-- b000511 | prose | pages [17] -->
= 1 −

<!-- b000512 | prose | pages [17] -->
i=1

<!-- b000513 | prose | pages [17] -->
, (14) (1 −Pr(xi))

<!-- b000514 | prose | pages [17] -->
where Pr(xi) represents the positive probability of image i, which is the output of our prediction model–CNN. If the positive probability of a system reaches a high value (e.g., 0.8, 0.9, or even higher), the Asian giant hornet will be likely to exist in this area, and the government should prioritize the observation. Based on this reasoning, we deﬁne the probability of system positivity Pr(x) as the priority of the region. Observations sent from places of high priority should be processed ﬁrst. Table 3 shows the detailed information of each cluster, including the number of observations, central latitude and longitude, and priority etc.

<!-- b000515 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000516 | caption | pages [17] -->
Table 3: Attributes of clusters.

<!-- b000517 | prose | pages [17] -->
Central Latitude Index Central Longitude

<!-- b000518 | prose | pages [17] -->
0 -122.2903 47.5641 1 -117.6439 47.3892 2 -122.4812 48.7551 3 -120.4284 47.2251 4 -122.5077 45.6566

<!-- b000519 | prose | pages [17] -->
Observations Priority Rank Color

<!-- b000520 | prose | pages [17] -->
41 0.9982 1 Red 4 0.0036 5 Green 20 0.6507 2 Blue 5 0.0746 4 Yellow 3 0.2480 3 Black

<!-- b000521 | prose | pages [17] -->
So far, we can give the government the following advice:

<!-- b000522 | prose | pages [17] -->
1. If an observation is sent from an area close to the central coordinate of cluster 0, it should be highly valued;

<!-- b000523 | prose | pages [17] -->
2. If an observation is sent from an area close to the central coordinate of cluster 1 or 3, it is most likely to be negative;

<!-- b000524 | prose | pages [17] -->
3. If an observation is sent from an area close to the central coordinate of cluster 3 or 4, there is a certain possibility that he may be positive, so the government can check carefully when it is not in an emergency situation.

<!-- b000525 | prose | pages [17] -->
Problem 4: Optimal Updating Strategy Based on Nu- 6 merical Derivative

<!-- b000526 | prose | pages [17] -->
In this section, we will discuss the eﬀect of updating the model at diﬀerent intervals on the testing results, including the testing loss of auto-encoder and the accuracy of CNN in testing dataset. To ﬁgure this out, we keep the same testing set as problem two in section 4, but the images of the training set are screened twice according to the time interval.

<!-- b000527 | prose | pages [17] -->
We ﬁrst utilize the latest detection date in the data, November 20, 2020, as the current time, and select a series of time interval thresholds. We make the diﬀerence between the observation time and the current time, and apply the threshold strategy to ﬁlter the images. That is, when

<!-- b000528 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000529 | prose | pages [17] -->
关注数学模型

<!-- b000530 | furniture | pages [17] -->
2

<!-- b000531 | furniture | pages [17] -->
MATHmodels

<!-- b000532 | furniture | pages [17] -->
获取更多资讯

<!-- b000533 | furniture | pages [18] -->
Team # 2101166

<!-- b000534 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000535 | furniture | pages [18] -->
Page 18 of 25

<!-- b000536 | prose | pages [18] -->
we set the threshold of time interval to t0, we only consider the observation images whose time diﬀerence is greater than t0.

<!-- b000537 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000538 | caption | pages [18] -->
Figure 13: The workﬂow of problem 4.

<!-- b000539 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000540 | prose | pages [18] -->
Update Frequency. We chose 11 diﬀerent threshold, 0, 5, 10, 15, 25, 40, 60, 80, 100, 120, and 150, in days. The results in details, including the testing loss of auto-encoder and the testing accuracy of CNN, are shown in Table 4.

<!-- b000541 | caption | pages [18] -->
Table 4: Detailed results of problem 4.

<!-- b000542 | prose | pages [18] -->
t0 Loss Accuracy t0 Loss

<!-- b000543 | prose | pages [18] -->
0 0.0274 0.8030 25 0.0280 5 0.0280 0.8030 40 0.0278 60 0.0291 10 0.0280 0.8030 15 0.0280 0.8030 80 0.0313

<!-- b000544 | prose | pages [18] -->
Accuracy t0 Loss Accuracy

<!-- b000545 | prose | pages [18] -->
0.8030 100 0.0298 0.7576 0.8030 120 0.0363 0.7727 0.7879 150 0.0424 0.7879 0.7727

<!-- b000546 | prose | pages [18] -->
In order to further analyze the loss and the accuracy, we apply cubic spline interpolation method, and obtain their corresponding numerical derivatives by using the central diﬀerence formula:

<!-- b000547 | prose | pages [18] -->
k(x) ≈fk+1(x) −fk−1(x)

<!-- b000548 | prose | pages [18] -->
f ′

<!-- b000549 | prose | pages [18] -->
, (15) 2h

<!-- b000550 | prose | pages [18] -->
where h is the small step size. The smaller h is, the more accurate the result is. The truncation error of central diﬀerence has been proofed to be o(h2/6). The optimal time interval for updating models is deﬁned as the abscissa corresponding to the extremum of the numerical derivative of the time-varying functions (the testing loss curve for auto-encoder, and the testing accuracy for CNN).

<!-- b000551 | caption | pages [18] -->
Figure 14 shows the testing loss of auto-encoder and the testing accuracy of CNN changing

<!-- b000552 | prose | pages [18] -->
with the time interval. According to the diagram, we can draw the following conclusions:

<!-- b000553 | heading | pages [18] -->
1. The auto-encoder model needs to be updated every 4 months.

<!-- b000554 | prose | pages [18] -->
Because when t0 = 119.39, the numerical derivative of the testing loss reaches the maxi- mum value of 0.0042, which indicates at this time the error grows the fastest;

<!-- b000555 | heading | pages [18] -->
2. The CNN model needs to be updated every 3 months.

<!-- b000556 | prose | pages [18] -->
Because when t0 = 85.71, the numerical derivative of accuracy reaches the minimum

<!-- b000557 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000558 | prose | pages [18] -->
关注数学模型 value of −0.0092, which implies at this time the accuracy decreases the fastest.

<!-- b000559 | furniture | pages [18] -->
2

<!-- b000560 | furniture | pages [18] -->
MATHmodels

<!-- b000561 | furniture | pages [18] -->
获取更多资讯

<!-- b000562 | furniture | pages [19] -->
Team # 2101166

<!-- b000563 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000564 | furniture | pages [19] -->
Page 19 of 25

<!-- b000565 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000566 | prose | pages [19] -->
(a) The loss of auto-encoder.

<!-- b000567 | prose | pages [19] -->
(b) The accuracy of CNN.

<!-- b000568 | caption | pages [19] -->
Figure 14: The loss and the accuracy changing with time interval for updating models. The

<!-- b000569 | prose | pages [19] -->
light shade is the numerical derivative calculated based on the central diﬀerence.

<!-- b000570 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000571 | prose | pages [19] -->
Update Method. The method to update the model is to utilize the data cleaning and enhancement methods mentioned in section 4 to process the newly generated observations, and then put them into the training set.

<!-- b000572 | prose | pages [19] -->
Problem 5: Assessment Based on the Bayes Formula 7

<!-- b000573 | prose | pages [19] -->
For invasive species, due to their strong survivability and reproductive ability, it is still possible to erupt again when the destruction is not thorough enough. Therefore, we need to establish a suﬃciently complete monitoring and evaluation system. Since the actual number and distribution of nests are diﬃcult to obtain directly, we made judgments based on positive observations and established a multi-dimensional evaluation system as follows:

<!-- b000574 | prose | pages [19] -->
Growth Ratio gt. For the number of positives, growth rate refers to the ratio of the current population to the previous year, which can reﬂect the growth of nests. When gt is less than 1, the size of population will decrease.

<!-- b000575 | prose | pages [19] -->
gt = Nt

<!-- b000576 | prose | pages [19] -->
.

<!-- b000577 | prose | pages [19] -->
(16)

<!-- b000578 | prose | pages [19] -->
Nt−1

<!-- b000579 | prose | pages [19] -->
Distribution Range Ratio dt. As diﬀerent nests compete with each other, the distribu- tion range of nests will increase as the number grows. We calculate the average value between all positive positions i and j to represent the distribution range of nests. In order to reﬂect the dynamic change characteristics of the distribution range, we calculate the ratio of the current average to the average of the previous year.

<!-- b000580 | prose | pages [19] -->
∑

<!-- b000581 | prose | pages [19] -->
i,j∈Nt−1 ∆2

<!-- b000582 | prose | pages [19] -->
∑

<!-- b000583 | prose | pages [19] -->
dt =

<!-- b000584 | prose | pages [19] -->
ij

<!-- b000585 | prose | pages [19] -->
.

<!-- b000586 | prose | pages [19] -->
(17)

<!-- b000587 | prose | pages [19] -->
i,j∈Nt ∆2

<!-- b000588 | prose | pages [19] -->
ij

<!-- b000589 | prose | pages [19] -->
Positive Probability Ratio pt. From the perspective of probability theory, each sighting can be regarded as a sampling, so the ratio of all positive observation reports can imply the proportion of the Asian giant hornet in the nature of all bees. Similarly, we calculate the ratio of the current value to the previous year’s average.

<!-- b000590 | prose | pages [19] -->
Positivet/Allt

<!-- b000591 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000592 | prose | pages [19] -->
pt =

<!-- b000593 | prose | pages [19] -->
, (18) 关注数学模型

<!-- b000594 | prose | pages [19] -->
Positivet−1/Allt−1

<!-- b000595 | furniture | pages [19] -->
2

<!-- b000596 | furniture | pages [19] -->
MATHmodels

<!-- b000597 | furniture | pages [19] -->
获取更多资讯

<!-- b000598 | furniture | pages [20] -->
Team # 2101166

<!-- b000599 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000600 | furniture | pages [20] -->
Page 20 of 25

<!-- b000601 | prose | pages [20] -->
where Positivet represents the number of positive observations in year t, while Allt is the total number of sightings.

<!-- b000602 | prose | pages [20] -->
Evaluation Coeﬃcient Kt. It can be obtained by multiplying the above three param- eters. Considering that the neural network model has a certain error rate, we use Bayesian inference to correct it. Suppose the posterior probability of Kt is Pr(Kt | θ), and the correct

<!-- b000603 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000604 | prose | pages [20] -->
rate of neural network model is θ.

<!-- b000605 | prose | pages [20] -->
Pr (Kt) · Pr (Kt | θ) Pr (Kt | θ) = ∑

<!-- b000606 | prose | pages [20] -->
i∈Nt Pr

<!-- b000607 | prose | pages [20] -->
(

<!-- b000608 | prose | pages [20] -->
)

<!-- b000609 | prose | pages [20] -->
(

<!-- b000610 | prose | pages [20] -->
).

<!-- b000611 | prose | pages [20] -->
(19)

<!-- b000612 | prose | pages [20] -->
K(i)

<!-- b000613 | prose | pages [20] -->
K(i)

<!-- b000614 | prose | pages [20] -->
· Pr

<!-- b000615 | prose | pages [20] -->
| θ

<!-- b000616 | prose | pages [20] -->
t

<!-- b000617 | prose | pages [20] -->
t

<!-- b000618 | prose | pages [20] -->
When K converges to 0, we are fully conﬁdent that the pest has been eradicated. We test the accuracy of the evaluation model by simulating the increase and decrease of nests. In the growth phase, the number of nests conforms to the logistic growth, and K is always greater than 1. After measures are taken, the environmental carrying capacity is greatly reduced, nests begin to decrease rapidly, and K decreases rapidly. This shows that the observation indicators are eﬀective.

<!-- b000619 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000620 | prose | pages [20] -->
(a) Introduction of Evaluation coeﬃcient.

<!-- b000621 | prose | pages [20] -->
(b) Changes in N and K after taking actions.

<!-- b000622 | caption | pages [20] -->
Figure 15: Introduction to pest extinction assessment model.

<!-- b000623 | prose | pages [20] -->
8

<!-- b000624 | heading | pages [20] -->
Model Analysis

<!-- b000625 | prose | pages [20] -->
8.1

<!-- b000626 | heading | pages [20] -->
Strengths and Weaknesses

<!-- b000627 | prose | pages [20] -->
Strengths. 1. When setting the parameters of the equation in problem 1, many inﬂuencing factors such as intraspeciﬁc competition and environmental parameters are considered;

<!-- b000628 | prose | pages [20] -->
2. In problem 1,the model uses a suitable probability distribution to get random results, which makes the model more realistic; 3. We use auto-encoder to eﬀectively condense the image information in problem 2, making CNN training faster and better;

<!-- b000629 | prose | pages [20] -->
4. In the data processing, a regression analysis is performed on the comments, and it is concluded that the photo category and the length of the comments are irrelevant under the 95% signiﬁcance condition, which proves to a certain extent that the text does not need to be considered in problem 2.

<!-- b000630 | prose | pages [20] -->
Weaknesses.

<!-- b000631 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000632 | prose | pages [20] -->
关注数学模型

<!-- b000633 | furniture | pages [20] -->
2

<!-- b000634 | furniture | pages [20] -->
MATHmodels

<!-- b000635 | furniture | pages [20] -->
获取更多资讯

<!-- b000636 | furniture | pages [21] -->
Team # 2101166

<!-- b000637 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000638 | furniture | pages [21] -->
Page 21 of 25

<!-- b000639 | prose | pages [21] -->
1. Due to the lack of data used to ﬁt hyperparameters, there may be some errors in the estimation of hyperparameters in problem 1;

<!-- b000640 | prose | pages [21] -->
2. Although we take various measures to solve the problem of category imbalance, the problem of category imbalance still exists due to the large disparity between the negative samples and positive samples in the dataset.

<!-- b000641 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000642 | prose | pages [21] -->
8.2

<!-- b000643 | heading | pages [21] -->
Sensitivity Analysis

<!-- b000644 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000645 | caption | pages [21] -->
Figure 16: Figures for sensitivity analysis

<!-- b000646 | prose | pages [21] -->
Figure 16a, shows the variation trend of nest number with r and γ. From the ﬁgure we can tell that: the number of nests is positively correlated with r and negatively correlated with γ, which is consistent with Equation (3) and (5). In addition, when r increases or γ decreases separately, N has little eﬀect. But when r and γ change synchronously, N increases rapidly.

<!-- b000647 | prose | pages [21] -->
From Figure 16b and c, we can tell that: as the negative images increases, the imbalance of positive and negative samples increases, and the loss of auto-encoder tends to drop at the same time. This is because the loss is negatively correlated with the number of images, i.e., the more training pictures, the smaller the error. Furthermore, with the increase of sample imbalance, the testing accuracy ﬁrst decreases signiﬁcantly and then increases slowly. This is because at the beginning, the sample imbalance is the dominant factor aﬀecting the accuracy, and with the increasing number of training images, the size of training set is gradually dominant.

<!-- b000648 | prose | pages [21] -->
9

<!-- b000649 | heading | pages [21] -->
Conclusion

<!-- b000650 | prose | pages [21] -->
Nowadays, the biological invasion of the Asian giant hornet has become an issue that needs attention in Washington State. Therefore, accurately identifying the Asian giant hornet, pre- dicting the future spread of the Asian giant hornet in Washington State, and establishing an eﬀective evaluation system is of great signiﬁcance to Washington State’s biological control.

<!-- b000651 | prose | pages [21] -->
In this project, we ﬁrst carefully screened the dataset to retain meaningful pictures and geographic information. After that, we use time-step diﬀerence equation to simulate the population migration process of the Asian giant hornet, and use auto-encoder and CNN to identify the Asian giant hornet images, and use Agglomerative Clustering and image recognition methods to help prioritize regional investigations. In the end, we built an evaluation system to assist the Washington State Department of Agriculture in judging the degree of the Asian giant hornet biological invasion.

<!-- b000652 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000653 | prose | pages [21] -->
关注数学模型

<!-- b000654 | furniture | pages [21] -->
2

<!-- b000655 | furniture | pages [21] -->
MATHmodels

<!-- b000656 | furniture | pages [21] -->
获取更多资讯

<!-- b000657 | furniture | pages [22] -->
Team # 2101166

<!-- b000658 | heading | pages [22] -->
References

<!-- b000659 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000660 | furniture | pages [22] -->
Page 22 of 25

<!-- b000661 | references | pages [22] -->
[1] A. Alaniz, M. Carvajal, and P. Vergara. Giants are Coming? Predicting the Potential

<!-- b000662 | references | pages [22] -->
Spread and Impacts of the Giant Asian hornet (Vespa Mandarinia, Hymenoptera: Vespi-

<!-- b000663 | references | pages [22] -->
dae) in the USA. Pest Management Science, 77(1):104–112, 2021.

<!-- b000664 | references | pages [22] -->
微信公众号：数学模型

<!-- b000665 | references | pages [22] -->
[2] S. Bertolino, S. Lioy, D. Laurino, A. Manino, and M. Porporato. Spread of the Inva-

<!-- b000666 | references | pages [22] -->
sive Yellow-Legged Hornet Vespa Velutina (Hymenoptera: Vespidae) in Italy. Applied

<!-- b000667 | references | pages [22] -->
Entomology and Zoology, 51(4):589–597, 2016.

<!-- b000668 | references | pages [22] -->
[3] N. Chawla, K. Bowyer, L. Hall, and W. Kegelmeyer. SMOTE: Synthetic Minority Over-

<!-- b000669 | references | pages [22] -->
Sampling Technique. Journal of Artiﬁcial Intelligence Research, 16(1):321–357, 2002.

<!-- b000670 | references | pages [22] -->
[4] M. Egmont-Petersen, D. Ridder, and H. Handels. Image Processing with Neural Networks-

<!-- b000671 | references | pages [22] -->
a Review. Pattern Recognition, 35(10):2279–2301, 2002.

<!-- b000672 | references | pages [22] -->
[5] A. Graves, A. Mohamed, and G. Hinton. Speech Recognition with Deep Recurrent Neural

<!-- b000673 | references | pages [22] -->
Networks. Acoustics Speech & Signal Processing .icassp.international Conference on, 2013.

<!-- b000674 | references | pages [22] -->
微信号：MATHmodels

<!-- b000675 | references | pages [22] -->
[6] H. Han, W. Wang, and B. Mao. Borderline-SMOTE: A New Over-Sampling Method in

<!-- b000676 | references | pages [22] -->
Imbalanced Data Sets Learning. In Advances in Intelligent Computing, pages 878–887,

<!-- b000677 | references | pages [22] -->
2005.

<!-- b000678 | references | pages [22] -->
[7] Peter J. Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster

<!-- b000679 | references | pages [22] -->
Analysis. Journal of Computational and Applied Mathematics, 20:53–65, 1987.

<!-- b000680 | references | pages [22] -->
[8] M. Keeling, D. Franklin, S. Datta, M. Brown, and G. Budge. Predicting the Spread of

<!-- b000681 | references | pages [22] -->
the Asian Hornet (Vespa Velutina) Following its Incursion into Great Britain. Scientiﬁc

<!-- b000682 | references | pages [22] -->
Reports, 7(1), 2017.

<!-- b000683 | references | pages [22] -->
[9] A. Krizhevsky, I. Sutskever, and G. Hinton. ImageNet Classiﬁcation with Deep Convolu-

<!-- b000684 | references | pages [22] -->
tional Neural Networks. Communications of the Acm, 60(6):84–90, 2017.

<!-- b000685 | references | pages [22] -->
[10] V. Mnih, K. Kavukcuoglu, D. Silver, A. Graves, I. Antonoglou, D. Wierstra, and M. Ried-

<!-- b000686 | references | pages [22] -->
miller. Playing Atari with Deep Reinforcement Learning. Computer ence, 2013.

<!-- b000687 | references | pages [22] -->
[11] C. Robinet, C. Suppo, and E. Darrouzet. Rapid Spread of the Invasive Yellow-Legged

<!-- b000688 | references | pages [22] -->
Hornet in France: the Role of Human-Mediated Dispersal and the Eﬀects of Control

<!-- b000689 | references | pages [22] -->
Measures. Journal of Applied Ecology, 54(1):205–215, 2017.

<!-- b000690 | references | pages [22] -->
[12] P. Sermanet, K. Kavukcuoglu, S. Chintala, and Y. LeCun.

<!-- b000691 | references | pages [22] -->
Context-Dependent Pre-

<!-- b000692 | references | pages [22] -->
Trained Deep Neural Networks for Large-Vocabulary Speech Recognition. IEEE Transac-

<!-- b000693 | references | pages [22] -->
tions on Audio, Speech, and Language Processing, 20(1):30–42, 2012.

<!-- b000694 | references | pages [22] -->
[13] M. Zheng, T. Li, L. Sun, T. Wang, B. Jie, W. Yang, M. Tang, and C. Lv.

<!-- b000695 | references | pages [22] -->
An Au-

<!-- b000696 | references | pages [22] -->
tomatic Sampling Ratio Detection Method Based on Genetic Algorithm for Imbalanced

<!-- b000697 | references | pages [22] -->
Data Classiﬁcation. Knowledge-Based Systems, page 106800, 2021.

<!-- b000698 | references | pages [22] -->
[14] H. Zhou, C. Long, and D. Huang. Cross-Lingual Sentiment Classiﬁcation Based on De-

<!-- b000699 | references | pages [22] -->
noising Autoencoder. Communications in Computer

<!-- b000700 | references | pages [22] -->
2014.

<!-- b000701 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000702 | references | pages [22] -->
Information Science, 496:181–192,

<!-- b000703 | references | pages [22] -->
关注数学模型

<!-- b000704 | furniture | pages [22] -->
2

<!-- b000705 | furniture | pages [22] -->
MATHmodels

<!-- b000706 | furniture | pages [22] -->
获取更多资讯

<!-- b000707 | furniture | pages [23] -->
Team # 2101166

<!-- b000708 | heading | pages [23] -->
Appendices

<!-- b000709 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000710 | furniture | pages [23] -->
Page 23 of 25

<!-- b000711 | prose | pages [23] -->
Core Codes for Auto-Encoder

<!-- b000712 | heading | pages [23] -->
Appendix A

<!-- b000713 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000714 | prose | pages [23] -->
import torch import torch.nn as nn

<!-- b000715 | prose | pages [23] -->
class AutoEncoder(nn.Module): def __init__(self): super(AutoEncoder , self).__init__ () self.DownSampling = nn.Sequential(

<!-- b000716 | prose | pages [23] -->
nn.Conv2d(3, 6, 3, 1, 1), nn.ReLU (), nn.BatchNorm2d(6), nn.MaxPool2d(2), nn.Conv2d(6, 12 , 3, 1, 1), nn.ReLU (), nn.BatchNorm2d(12), nn.MaxPool2d(2), nn.Conv2d(12 , 24 , 3, 1, 1), nn.ReLU (), nn.BatchNorm2d(24), nn.MaxPool2d(2), nn.Conv2d(24 , 48 , 3, 1, 1), nn.ReLU (), nn.BatchNorm2d(48), nn.MaxPool2d(2),

<!-- b000717 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000718 | prose | pages [23] -->
) self.UpSampling = nn.Sequential(

<!-- b000719 | prose | pages [23] -->
nn.Conv2d(48 , 24 , 3, 1, 1), nn. ConvTranspose2d (24 , 24 , 3, 2, 1, 1), nn.ReLU (), nn.Conv2d(24 , 12 , 3, 1, 1), nn. ConvTranspose2d (12 , 12 , 3, 2, 1, 1), nn.ReLU (), nn.Conv2d(12 , 6, 3, 1, 1), nn. ConvTranspose2d (6, 6, 3, 2, 1, 1), nn.ReLU (), nn.Conv2d(6, 3, 3, 1, 1), nn. ConvTranspose2d (3, 3, 3, 2, 1, 1), ) def forward(self , x): return self.DownSampling(x), self.UpSampling(self.DownSampling(x))

<!-- b000720 | prose | pages [23] -->
Core Codes for CNN

<!-- b000721 | heading | pages [23] -->
Appendix B

<!-- b000722 | prose | pages [23] -->
import torch import torch.nn as nn

<!-- b000723 | prose | pages [23] -->
class CNN(nn.Module):

<!-- b000724 | prose | pages [23] -->
def __init__(self): super(CNN , self).__init__ () self.conv = nn.Sequential(

<!-- b000725 | prose | pages [23] -->
nn.Conv2d(48 , 96 , 3, 1, 1), nn.ReLU (), nn.BatchNorm2d(96), nn.MaxPool2d(2), nn.Conv2d(96 , 192 , 3, 1, 1), nn.ReLU (), nn.BatchNorm2d(192), nn.MaxPool2d(2), ) self.out = nn.Sequential(

<!-- b000726 | prose | pages [23] -->
nn.Linear(3072 , 128), nn.Dropout(0.25), nn.ReLU (), nn.Linear(128 , 2), nn.Softmax(dim=1), ) def forward(self , x): return self.out(self.conv(x).view(x.shape[0], -1))

<!-- b000727 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000728 | prose | pages [23] -->
关注数学模型

<!-- b000729 | furniture | pages [23] -->
2

<!-- b000730 | furniture | pages [23] -->
MATHmodels

<!-- b000731 | furniture | pages [23] -->
获取更多资讯

<!-- b000732 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000733 | prose | pages [24] -->
Fight the Plague of Asian Giant Hornets

<!-- b000734 | heading | pages [24] -->
Background

<!-- b000735 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000736 | prose | pages [24] -->
In December 2019, WSDA received and verified two reports of the Asian giant hornet near Blaine. In 2020, both Washington and Canada have had new confirmed sightings of Asian giant hornet in October of 2020. This is not an isolated incident. In 2004, it first appeared in Europe, and spread to Spain, Belgium, Portugal and Italy, rapidly.

<!-- b000737 | prose | pages [24] -->
Characteristics of Asian giant hornet:

<!-- b000738 | prose | pages [24] -->
• Aggressive: attack many kinds of insects. • Strong: destroy a hive in a matter of hours. • Fast: the population spreads quickly.

<!-- b000739 | prose | pages [24] -->
Descriptions

<!-- b000740 | prose | pages [24] -->
Actual distribution of Asian giant hornets in Europe

<!-- b000741 | prose | pages [24] -->
How fast will the Asian giant hornet spread?

<!-- b000742 | prose | pages [24] -->
We combine the biological information and ecological principles of the

<!-- b000743 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000744 | prose | pages [24] -->
Asian giant hornet.

<!-- b000745 | prose | pages [24] -->
Growth Foundation

<!-- b000746 | prose | pages [24] -->
Reproduction Wintering

<!-- b000747 | prose | pages [24] -->
If the Asian giant hornet is allowed to breed freely, Washington State will be filled with the Asian giant hornet’s nests in just a few years.

<!-- b000748 | prose | pages [24] -->
How can we identify the Asian giant hornet?

<!-- b000749 | prose | pages [24] -->
We conduct deep learning with the data provided. After inputting the observation picture, the model can give positive and negative judgments.

<!-- b000750 | prose | pages [24] -->
Positive Output Input AI

<!-- b000751 | prose | pages [24] -->
or

<!-- b000752 | prose | pages [24] -->
Negative

<!-- b000753 | heading | pages [24] -->
The accuracy of the model reached 80.3%, which can effectively

<!-- b000754 | prose | pages [24] -->
judge the observation photos.

<!-- b000755 | prose | pages [24] -->
Which area has the highest risk?

<!-- b000756 | prose | pages [24] -->
Number: priority of the area

<!-- b000757 | prose | pages [24] -->
The most risk city: Seattle

<!-- b000758 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000759 | prose | pages [24] -->
How often to update the model?

<!-- b000760 | prose | pages [24] -->
As new observations increase, errors will gradually increase.

<!-- b000761 | heading | pages [24] -->
4 months

<!-- b000762 | heading | pages [24] -->
3 months

<!-- b000763 | prose | pages [24] -->
关注数学模型

<!-- b000764 | furniture | pages [24] -->
2

<!-- b000765 | furniture | pages [24] -->
MATHmodels

<!-- b000766 | furniture | pages [24] -->
获取更多资讯

<!-- b000767 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000768 | prose | pages [25] -->
Fight the Plague of Asian Giant Hornets

<!-- b000769 | prose | pages [25] -->
Descriptions

<!-- b000770 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000771 | prose | pages [25] -->
How can we make sure the Asian giant hornet has been eradicated?

<!-- b000772 | prose | pages [25] -->
We design three indicators to characterize changes in the population.

<!-- b000773 | prose | pages [25] -->
Number of nests

<!-- b000774 | prose | pages [25] -->
Converges to 0 Range of spatial distribution

<!-- b000775 | prose | pages [25] -->
Positive ratio in observations

<!-- b000776 | prose | pages [25] -->
Suggestions

<!-- b000777 | prose | pages [25] -->
微信号：MATHmodels

<!-- b000778 | prose | pages [25] -->
As the number of nests of the Asian giant hornet explodes in the simulation, we suggest that the government should pay close attention to the biological invasion of the Asian giant hornet.

<!-- b000779 | prose | pages [25] -->
How to educate the public?

<!-- b000780 | prose | pages [25] -->
We recommend that the Asian giant hornet be popularized with the people of Washington State through the media or popular science books.

<!-- b000781 | prose | pages [25] -->
• Popularize the biological characteristics of the species to the public.

<!-- b000782 | prose | pages [25] -->
• Emphasize the selection of the background which is easy to distinguish when taking photos.

<!-- b000783 | prose | pages [25] -->
• Upload the correct image, not the reference image downloaded from the official website.

<!-- b000784 | prose | pages [25] -->
• Write comments carefully and realistically, which describe the scene of the photo.

<!-- b000785 | prose | pages [25] -->
• Unify the upload format into the picture format.

<!-- b000786 | prose | pages [25] -->
What should we do in the future?

<!-- b000787 | prose | pages [25] -->
We suggest that you and your department conduct identification of uploaded samples on a regular basis.

<!-- b000788 | prose | pages [25] -->
• Update the auto-encoder for every 3 months, and the CNN for every 4 months.

<!-- b000789 | prose | pages [25] -->
• Set up a professional team to assist the further iteration of image recognition algorithm.

<!-- b000790 | prose | pages [25] -->
• Employ computer vision algorithm engineers to further improve the accuracy of the model.

<!-- b000791 | prose | pages [25] -->
• Handle observations strictly according to priority.

<!-- b000792 | heading | pages [25] -->
References

<!-- b000793 | references | pages [25] -->
S. Bertolino, S. Lioy, D. Laurino, A. Manino, and M. Porporato. Spread of the Invasive Yellow-Legged Hornet Vespa Velutina (Hymenoptera:

<!-- b000794 | references | pages [25] -->
Vespidae) in Italy. Applied Entomology and Zoology, 51(4):589–597, 2016.

<!-- b000795 | references | pages [25] -->
A. Alaniz, M. Carvajal, and P. Vergara. Giants are Coming? Predicting the Potential Spread and Impacts of the Giant Asian hornet (Vespa

<!-- b000796 | references | pages [25] -->
Mandarinia, Hymenoptera: Vespi-dae) in the USA. Pest Management Science, 77(1):104–112, 2021.

<!-- b000797 | references | pages [25] -->
M. Keeling, D. Franklin, S. Datta, M. Brown, and G. Budge. Predicting the Spread of the Asian Hornet (Vespa Velutina) Following its Incursion into

<!-- b000798 | references | pages [25] -->
Great Britain. Scientific Reports, 7(1), 2017.

<!-- b000799 | references | pages [25] -->
P. Sermanet, K. Kavukcuoglu, S. Chintala, and Y. LeCun. Context-Dependent Pre-Trained Deep Neural Networks for Large-Vocabulary Speech

<!-- b000800 | references | pages [25] -->
Recognition. IEEE Transac-tions on Audio, Speech, and Language Processing, 20(1):30–42, 2012.

<!-- b000801 | references | pages [25] -->
H. Zhou, C. Long, and D. Huang. Cross-Lingual Sentiment Classification Based on De-noising Autoencoder. Communications in Computer

<!-- b000802 | references | pages [25] -->
Information Science, 496:181–192,2014.

<!-- b000803 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000804 | references | pages [25] -->
关注数学模型

<!-- b000805 | furniture | pages [25] -->
2

<!-- b000806 | furniture | pages [25] -->
MATHmodels

<!-- b000807 | furniture | pages [25] -->
获取更多资讯
