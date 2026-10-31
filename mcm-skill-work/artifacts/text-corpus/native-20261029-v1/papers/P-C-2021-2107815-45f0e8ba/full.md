# P-C-2021-2107815-45f0e8ba

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
2107815

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | prose | pages [1] -->
Strategies to Analyze the Invasion of the Vespa Mandarinia: A Comprehensive

<!-- b000011 | prose | pages [1] -->
Three-dimensional Model

<!-- b000012 | title | pages [1] -->
微信公众号：数学模型

<!-- b000013 | prose | pages [1] -->
The appearance of the Vespa mandarinia in Washington State may have a potential negative impact on the local ecology.In view of the limited resources of government agencies, researchers need to develop some strategies to analyze the investigation priorities of these wasps' public sighting reports. The specific task is divided into 5 questions.

<!-- b000014 | prose | pages [1] -->
As for question 1, we need to integrate the biological characteristics of the wasp and the data characteristics provided by the title to establish a growth-proliferation model for the wasp population. First of all, based on the Logistic-Model, we completed the establishment of a basic wasp colony growth model on the basis of changes of environmental factors such as temperature and the life habits. After that, we use Gaussian distribution function to describe the probability of natural events to simulate the time and space position of each sighting event, and establish a wasp colony propagation and prediction model so that we could analyze the probability of sighting events. This is because we fully consider that the sighting reports don‘t completely represent the accurate location of the wasp population and their occurrence has a certain randomness. The

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
spatiotemporal location of the incident has established a wasp colony propagation and prediction model. In the model's simulation of the positive-ID data distribution of the data set, the simulated distribution and the actual data point distribution are relatively close. Based on the distance relationship between the earliest occurrence point of the sighting event and each occurrence point, we established a method to analyze the fitting accuracy. In the verification, the fitting accuracy of the correct witness report is about 84.6%.

<!-- b000017 | prose | pages [1] -->
As for question 2, in order to make full use of the various data in the data set, we divide the data set into three dimensions: spatio-temporal data, text and image. After that, we use the growth-diffusion model to analyze spatio-temporal data, establish a text classification model based on the LDA for text analysis, and establish an image analysis model based on CNN. The verification results of each independent model show that the analysis of the possibility of the classification of the prediction data set requires the synthesis of all types of data provided in the data set. Therefore, we synthesize the prediction confidence levels independently given by the three-dimensional models and assign weights to them by the effective information of each

<!-- b000018 | heading | pages [1] -->
dimension to complete the three-dimensional comprehensive data analysis and prediction model. The

<!-- b000019 | prose | pages [1] -->
model obtained 92.86% (positive-ID) and 85.22% (negative-ID) goodness of fit in the fitting of existing data. The prediction results of the model can also be well explained for each data point.

<!-- b000020 | prose | pages [1] -->
As for question 3, we use the prediction confidence obtained by the model of question 2 to divide the data into six levels of S, A, B, C, D, and E according to the confidence interval. S grade is the highest grade. The higher the level is, the higher the investigation priority of the sighting report is.

<!-- b000021 | prose | pages [1] -->
As for to question 4, we proposed an incremental model update method based on the forgetting factor. When a new wasp sighting report is updated, the model calculates the defined forgetting factor and updates the original training data. The test shows that this update method increases the goodness of fit of the model by 10.68% (negative-ID), and can make certain self-correction to the predicted results.

<!-- b000022 | prose | pages [1] -->
As for question 5, we put forward three conditions which can prove that the wasps have been eradicated based on various factors,. We used the data from 2019 to 2020 for analysis and demonstration, which proved the correctness of the evaluation criteria. Finally, we forecast the development trend of events in 2021.

<!-- b000023 | prose | pages [1] -->
The model established in this paper has high comprehensiveness and accuracy. Besides, it can also give the prediction confidence of each data point and optimizes the researcher's strategy of analyzing the survey report.At the same time, we provided a two-page memorandum to the Washington State Department of Agriculture.

<!-- b000024 | keywords | pages [1] -->
Key Words:  Logistic-Model; LDA; CNN; Forgetting Factor; Correlation Analysis.

<!-- b000025 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000026 | furniture | pages [1] -->
关注数学模型

<!-- b000027 | furniture | pages [1] -->
2

<!-- b000028 | furniture | pages [1] -->
MATHmodels

<!-- b000029 | furniture | pages [1] -->
获取更多资讯

<!-- b000030 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000031 | furniture | pages [2] -->
Team # 2107815                                                                 Page 2 of 25

<!-- b000032 | heading | pages [2] -->
Contents

<!-- b000033 | furniture | pages [2] -->


<!-- b000034 | furniture | pages [2] -->


<!-- b000035 | contents | pages [2] -->
1    Introduction................................................................................................................................................. 3

<!-- b000036 | contents | pages [2] -->
1.1     Problem Background ......................................................................................................................... 3

<!-- b000037 | contents | pages [2] -->
1.2    Restatement of The Problem .............................................................................................................. 3

<!-- b000038 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000039 | contents | pages [2] -->
1.3    Our Approach ..................................................................................................................................... 3

<!-- b000040 | contents | pages [2] -->
2    Assumptions and Notations ....................................................................................................................... 3

<!-- b000041 | contents | pages [2] -->
2.2    Notations ............................................................................................................................................ 4

<!-- b000042 | contents | pages [2] -->
3    Data Pre-Analysis ....................................................................................................................................... 4

<!-- b000043 | contents | pages [2] -->
3.1    Data Preprocessing ............................................................................................................................. 4

<!-- b000044 | contents | pages [2] -->
3.2    Data Analysis ..................................................................................................................................... 5

<!-- b000045 | contents | pages [2] -->
3.3    Trend Analysis ................................................................................................................................... 6

<!-- b000046 | contents | pages [2] -->
4    The Diffusion and Prediction Model of Vespa Mandarinia.................................................................... 6

<!-- b000047 | contents | pages [2] -->
4.1    The Establishment of The Model ....................................................................................................... 6

<!-- b000048 | contents | pages [2] -->
4.2    Model Validation ................................................................................................................................ 7

<!-- b000049 | contents | pages [2] -->
4.3    Model Accuracy Analysis .................................................................................................................. 8

<!-- b000050 | contents | pages [2] -->
4.3.1    Preliminary Demonstration ..................................................................................................... 8

<!-- b000051 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000052 | contents | pages [2] -->
4.3.2    Precise Demonstration ............................................................................................................ 9

<!-- b000053 | heading | pages [2] -->
5    Establishment and Validation of Three Dimensional Comprehensive Analysis and Prediction

<!-- b000054 | prose | pages [2] -->
Model ............................................................................................................................................................... 10

<!-- b000055 | prose | pages [2] -->
5.1    Data Information Description ........................................................................................................... 10 5.2  LDA Based Text Classification Model .............................................................................................. 10 5.2.1  The Establishment of Text Classification Model ................................................................... 10 5.2.2    Text Analysis ........................................................................................................................ 11 5.3    CNN Based Image Recognition Model ............................................................................................ 13 5.3.1    Model Construction .............................................................................................................. 13 5.3.2    Model evaluation .................................................................................................................. 14 5.4    Establishment of Comprehensive Analysis and Prediction Model .................................................. 14 5.5    Verification and Prediction of Three-Dimensional Comprehensive Model..................................... 15 5.6    The Analyze of The Priority of The Investigation ........................................................................... 17 6    Update Method and Update Frequency ................................................................................................. 18 6.1    Method construction and frequency determination .......................................................................... 18 6.2    Method verification .......................................................................................................................... 19 7    Proof of Eradication ................................................................................................................................. 21 7.1    Data Analysis and Evaluation Standard Establishment ................................................................... 21 7.2    Evaluation Standard Demonstration and Development Trend Prediction ....................................... 21 8    Strengths and Weaknesses ....................................................................................................................... 22 8.1    Strengths ........................................................................................................................................... 22 8.2    Weaknesses ...................................................................................................................................... 22 9    Conclusion ................................................................................................................................................. 23 10    Reference ................................................................................................................................................. 23

<!-- b000056 | furniture | pages [2] -->


<!-- b000057 | prose | pages [2] -->
Memo ............................................................................................................................................................... 24

<!-- b000058 | furniture | pages [2] -->


<!-- b000059 | furniture | pages [2] -->


<!-- b000060 | furniture | pages [2] -->


<!-- b000061 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000062 | furniture | pages [2] -->


<!-- b000063 | furniture | pages [2] -->


<!-- b000064 | furniture | pages [2] -->


<!-- b000065 | furniture | pages [2] -->


<!-- b000066 | furniture | pages [2] -->
关注数学模型

<!-- b000067 | furniture | pages [2] -->
2

<!-- b000068 | furniture | pages [2] -->
MATHmodels

<!-- b000069 | furniture | pages [2] -->
获取更多资讯

<!-- b000070 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000071 | furniture | pages [3] -->
Team # 2107815                                                                 Page 3 of 25

<!-- b000072 | heading | pages [3] -->
1    Introduction

<!-- b000073 | heading | pages [3] -->
1.1     Problem Background

<!-- b000074 | prose | pages [3] -->
In September 2019, a colony of Vespa mandarinia (also known as the Asian giant hornet) was discovered on Vancouver Island in British Columbia, Canada. The news of the event spread rapidly throughout the area.

<!-- b000075 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000076 | prose | pages [3] -->
Since that time, several confirmed sightings of the pest have occurred in neighboring Washington State, as well as a multitude of mistaken sightings. Vespa mandarinia is the largest species of hornet in the world, and the occurrence of the nest was alarming. They are voracious predators of other insects that are considered agricultural pests. At the same time, much detailed information on Asian hornets is included in the problem attachments and can also be found online.

<!-- b000077 | prose | pages [3] -->
Due to the potential severe impact caused by the Vespa mandarinia, The State of Washington has created helplines and a website for people to report sightings of these hornets and must decide how to prioritize its limited resources to follow-up with additional investigation.

<!-- b000078 | heading | pages [3] -->
1.2    Restatement of The Problem

<!-- b000079 | prose | pages [3] -->
⚫ Build a mathematical model to address and discuss the spread of this pest over time and evaluate the level of

<!-- b000080 | prose | pages [3] -->
precision.

<!-- b000081 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000082 | prose | pages [3] -->
⚫ Using only the data set file provided and (possibly) the image file provided, build a model to analyze, discuss

<!-- b000083 | prose | pages [3] -->
and predict the likelihood of a mistaken classification. ⚫ Use the model to discuss how classification analyses lead to prioritizing investigation of the reports most

<!-- b000084 | prose | pages [3] -->
likely to be positive sightings. ⚫ Build a method to update the model given additional new reports over time and discuss the update frequency. ⚫ Address a kind of evidence that the pest has been eradicated in Washington State.

<!-- b000085 | heading | pages [3] -->
1.3    Our Approach

<!-- b000086 | prose | pages [3] -->
The topic requires us to address and discuss the spread of this pest over time, and use the data provided to analyze and predict the likelihood of a mistaken classification, find a method to determine the priority of the investigation for the positive sightings. What’s more, we need to build a method to update the model and address a kind of evidence that the pest has been eradicated in Washington State. Based on those, our work mainly includes the following:

<!-- b000087 | prose | pages [3] -->
⚫ Based on the biological habits of the Vespa mandarinia and the characteristics of the data provided, a

<!-- b000088 | prose | pages [3] -->
model which can analyze and predict the propagation of the Vespa mandarinia colony is established with a method to evaluate the level of precision. ⚫ To make full use of all kinds of information in the data set, a comprehensive analysis model is established

<!-- b000089 | prose | pages [3] -->
in three dimension is established to analyze all the space-time, text, and image information, which gives the likelihood of a mistaken classification. The model is verified on the test and prediction data sets and gets the confidence of the result. Using this model, we create a way to decide the priority of the investigation for the positive sightings. ⚫ Based on the model incremental updating algorithm with the forgetting factor, a method is built to update

<!-- b000090 | prose | pages [3] -->
the model get the update frequency. In the test results, this update method is proved to be able to significantly improve the analysis accuracy of the model. ⚫ Using the model we built and the data provided, we come up with a piece of evidence that the pest has

<!-- b000091 | prose | pages [3] -->
been eradicated in Washington State, discuss and analyze the validity of the evidence.

<!-- b000092 | furniture | pages [3] -->


<!-- b000093 | heading | pages [3] -->
2    Assumptions and Notations

<!-- b000094 | heading | pages [3] -->
2.1    Assumptions

<!-- b000095 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000096 | furniture | pages [3] -->
关注数学模型

<!-- b000097 | furniture | pages [3] -->
2

<!-- b000098 | furniture | pages [3] -->
MATHmodels

<!-- b000099 | furniture | pages [3] -->
获取更多资讯

<!-- b000100 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000101 | furniture | pages [4] -->
Team # 2107815                                                                 Page 4 of 25

<!-- b000102 | prose | pages [4] -->
To simplify our model and eliminate the complexity, we make the following main assumptions in this paper. Assumptions.1 The colony nests are distributed in a certain area around the location of the positive witness. Since the data provided only reported the occurrence of the sightings, according to the habits of the Vespa mandarinia, we believe that the correctly witnessed wasps came from a certain area around the incident site. This assumption makes the model better fit the distribution of data points.

<!-- b000103 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000104 | prose | pages [4] -->
Assumptions.2 The data provided have included the influence of human factors on the colony. It can be seen from the analysis of this problem that the witness event data of the Vespa mandarinia in the data can not fully represent the natural growth and diffusion of the Vespa mandarinia.  Because the Vespa mandarinia colony has the advantage of invasive species, the eradication of the Vespa mandarinia in Washington state also needs the intervention of human factors and cannot grow completely naturally.

<!-- b000105 | prose | pages [4] -->
Assumptions.3 In a certain period, there will not be a huge impact of climate change on the Vespa mandarinia colony. This assumption is to simplify the calculation of the model and remove the influence of unknown factors on the model.

<!-- b000106 | prose | pages [4] -->
Assumptions.4 The data provided in the topic are true and reliable to a certain degree. Because the model we built is base on the data provided in the topic, Only the high validity of the data can guarantee the high reliability of the model.

<!-- b000107 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000108 | heading | pages [4] -->
2.2    Notations

<!-- b000109 | prose | pages [4] -->
The main symbols we use in this paper and the explanations of them are put in Table 1. The symbols which are not frequently used will be introduced once we use them.

<!-- b000110 | prose | pages [4] -->
Table.2-1 Symbol 𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖) 𝑟 Explanation population density correction factor reproduction rate of the colony at the current time ∝ mortality rate of the colony at the current time 𝛽 population density threshold 𝐾 farthest distance between the predicted point and the propagation 𝑑𝑚𝑎𝑥

<!-- b000111 | prose | pages [4] -->
starting point of the propagation model 𝑤 weight value probability of space time 𝑃𝑆𝑝𝑎𝑐𝑒−𝑇𝑖𝑚𝑒 𝑃𝑇𝑒𝑥𝑡 probability of text probability of image information 𝑃𝐼𝑚𝑎𝑔𝑒 final classification possibility 𝑃𝑐𝑙𝑎𝑠𝑠𝑖𝑓𝑖𝑐𝑎𝑡𝑖𝑜𝑛 𝑆𝑙𝑎𝑠𝑡 farthest distance between the positive-ID point and the starting

<!-- b000112 | prose | pages [4] -->
point distance between the predicted point and the positive-ID points 𝑆𝑛𝑒𝑤 λ forgetting factor original data of LDA text classification model 𝐷𝐿𝐷𝐴 original data of CNN image recognition model 𝐷𝐶𝑁𝑁 D𝑛𝑒𝑤

<!-- b000113 | heading | pages [4] -->
3    Data Pre-Analysis

<!-- b000114 | heading | pages [4] -->
3.1    Data Preprocessing

<!-- b000115 | prose | pages [4] -->
updated new data

<!-- b000116 | prose | pages [4] -->
According to the official text and image data, three problems can be found after simple browsing:

<!-- b000117 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000118 | furniture | pages [4] -->
关注数学模型

<!-- b000119 | furniture | pages [4] -->
2

<!-- b000120 | furniture | pages [4] -->
MATHmodels

<!-- b000121 | furniture | pages [4] -->
获取更多资讯

<!-- b000122 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000123 | furniture | pages [5] -->
Team # 2107815                                                                 Page 5 of 25

<!-- b000124 | prose | pages [5] -->
⚫ The timeliness of some data is low. ⚫ The data correspondence is chaotic. ⚫ The picture format is not unified.

<!-- b000125 | prose | pages [5] -->
To solve the problems existing in the data and establish an effective data set, we have taken the following measures:

<!-- b000126 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000127 | prose | pages [5] -->
First of all, we screened the data in the table "2021MCMProblemC_DataSet.xlsx" according to the time. Considering that the first wasp was found in September 2019, and combined with the breeding Law of the wasp population, we only kept the records reported in 2019 and 2020.

<!-- b000128 | prose | pages [5] -->
Then, according to the corresponding relationship between the image name and its GlobalID in the table "2021MCM_ProblemC_Images_by_GlobalID.xlsx", we screen out all the corresponding data in the table"2021MCMProblemC_DataSet.xlsx" and record them as "valid data set". Through the Python program, all the images are preliminarily classified according to the image name and category in the "valid data set". There are 2127 data in the valid dataset.

<!-- b000129 | prose | pages [5] -->
Finally, considering that our model may use image recognition algorithm, we transform all PNG format images, MOV format video, PDF format documents into JPG format images for subsequent processing.

<!-- b000130 | heading | pages [5] -->
3.2    Data Analysis

<!-- b000131 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000132 | prose | pages [5] -->
After getting the effective data set, we can make a preliminary assessment of wasp invasion from the following two aspects:

<!-- b000133 | prose | pages [5] -->
⚫ The scale of the invasion. ⚫ The harmfulness of intrusion.

<!-- b000134 | prose | pages [5] -->
Firstly, according to the label of "Lab status", the “Notes” text data is divided into "positive-ID" and "negative-ID" as the analysis data of the model.

<!-- b000135 | prose | pages [5] -->
By analyzing the proportion of different kinds of data in the data, we divide all kinds of data in the "effective data set" into four categories: "unverified", "positive ID", "negative ID" and "unprocessed" according to the qualitative judgment given in the "lab status", and get the data proportion, as shown in the Fig.3-1 below:

<!-- b000136 | furniture | pages [5] -->


<!-- b000137 | prose | pages [5] -->
Fig.3-1  Image Statistics                                         Fig.3-2  High Line Map of Washington State.

<!-- b000138 | prose | pages [5] -->
Combined with the geographic coordinates of various reports, we obtained the DEM data of Washington state by consulting the open source data of the website[2], and drew the contour map of wasp invasion area and its surrounding area, as shown in the Fig.3-2.

<!-- b000139 | prose | pages [5] -->
Based on the analysis of the images, combined with the living habits of wasps living below 3000 meters above sea level, we believe that wasps are suitable for the survival and reproduction of wasps in the invasion area and its surrounding areas. Therefore, the geographical conditions of Washington state can not form an effective control on the reproduction and diffusion of wasps, and as an alien species, it has no natural enemies. Therefore, we think that the wasp invasion is more harmful.

<!-- b000140 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000141 | furniture | pages [5] -->
关注数学模型

<!-- b000142 | furniture | pages [5] -->
2

<!-- b000143 | furniture | pages [5] -->
MATHmodels

<!-- b000144 | furniture | pages [5] -->
获取更多资讯

<!-- b000145 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000146 | furniture | pages [6] -->
Team # 2107815                                                                 Page 6 of 25

<!-- b000147 | heading | pages [6] -->
3.3    Trend Analysis

<!-- b000148 | prose | pages [6] -->
According to the description of the topic, we first analyzed the changing trend of the number of effective reports and suspected reports over time, in order to observe the changing trend of the wasp population over time. According to the data in the "valid data set", the following results are obtained:

<!-- b000149 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000150 | furniture | pages [6] -->


<!-- b000151 | furniture | pages [6] -->


<!-- b000152 | furniture | pages [6] -->


<!-- b000153 | prose | pages [6] -->
Fig.3-3  Quantity-Time Curve

<!-- b000154 | prose | pages [6] -->
According to the results of our pre-analysis, combined with the data, we believe that the wasp will enter the

<!-- b000155 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000156 | prose | pages [6] -->
wintering state from November to march of the next year, and the population number will decrease; after entering the spring, the first breeding peak of wasp will be ushered in from April to May of the next year, and the population number will increase rapidly; due to the hot weather from June to July of each year, the reproduction of queen bee will increase from August to September every year, the second breeding peak of wasp will be ushered in, and its population will increase rapidly; from October to November every year, when the weather turns cold, the population of Vespa Mandarinia will decrease rapidly.

<!-- b000157 | prose | pages [6] -->
As an invasive species, wasps first appeared in North America in 2019, so the number of wasps reported in 2019 is not very large. It can be seen from the figure that after one year of adaptation and reproduction, the population of wasps will increase explosively in 2020.

<!-- b000158 | prose | pages [6] -->
These analyses provide the basis for the subsequent model establishment.

<!-- b000159 | heading | pages [6] -->
4    The Diffusion and Prediction Model of Vespa Mandarinia

<!-- b000160 | heading | pages [6] -->
4.1    The Establishment of The Model

<!-- b000161 | prose | pages [6] -->
As an insect population, the propagation of wasp colony should have certain biological characteristics. Therefore, the establishment of colony propagation model should first consider the biological characteristics of the Vespa Mandarinia.

<!-- b000162 | prose | pages [6] -->
In the study of the growth diffusion model of insect population[3], the author proposed a propagation model considering both growth and diffusion of insects. It can meet both the growth and diffusion of insects. Therefore, in this study, we first established a biological growth diffusion model based on its biological characteristics.

<!-- b000163 | prose | pages [6] -->
As the specific growth model of bee colony is not the focus of this paper, the established model mainly focuses on the propagation of wasp colony. For the colony itself in a certain place, let the population density be 𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖) , where 𝑥 and 𝑦 are the longitude and latitude of the colony. 𝑡 is the time. At the same time, the population density threshold is 𝐾.

<!-- b000164 | prose | pages [6] -->
We know that when：

<!-- b000165 | prose | pages [6] -->
𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖) < 𝐾

<!-- b000166 | prose | pages [6] -->
2

<!-- b000167 | prose | pages [6] -->
The growth rate of biological population density is high. And the colony density of a certain position at a certain time is as follows:

<!-- b000168 | prose | pages [6] -->
𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖+1) =∝𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖) −𝛽𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖)                                                  (Eq. 4-1)

<!-- b000169 | prose | pages [6] -->
Where, ∝ is the reproduction rate of the colony at the current time and 𝛽 is the mortality rate of the colony

<!-- b000170 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000171 | prose | pages [6] -->
at the current time. When:

<!-- b000172 | furniture | pages [6] -->
关注数学模型

<!-- b000173 | furniture | pages [6] -->
2

<!-- b000174 | furniture | pages [6] -->
MATHmodels

<!-- b000175 | furniture | pages [6] -->
获取更多资讯

<!-- b000176 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000177 | furniture | pages [7] -->
Team # 2107815                                                                 Page 7 of 25

<!-- b000178 | prose | pages [7] -->
𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖) ≥𝐾

<!-- b000179 | prose | pages [7] -->
2

<!-- b000180 | prose | pages [7] -->
The growth rate of biological population density gradually slowed down. In this case, based on the logistic growth model, the colony density at a certain position at a certain time is as follows:

<!-- b000181 | prose | pages [7] -->
𝑁(𝑥𝑖,𝑦𝑖,𝑡𝑖)

<!-- b000182 | prose | pages [7] -->
)/(1 + 𝑒−𝑟∙𝑡𝑖)                        (Eq. 4-2)

<!-- b000183 | prose | pages [7] -->
𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖+1) =∝∙𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖) ∙(1 −

<!-- b000184 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000185 | prose | pages [7] -->
𝐾 As to ∝ , according to the data analysis in the previous section, in different months of the year, due to temperature changes and other environmental factors, the breeding rate of the Vespa Mandarinia colony is different. After correction, the following results of ∝𝑖 are obtained:

<!-- b000186 | prose | pages [7] -->
0,          𝑁𝑜𝑣 − 𝑀𝑎𝑟

<!-- b000187 | prose | pages [7] -->
∝1, 𝐴𝑝𝑟 − 𝑀𝑎𝑦

<!-- b000188 | furniture | pages [7] -->


<!-- b000189 | prose | pages [7] -->
∝2, 𝐽𝑢𝑛 − 𝐽𝑢𝑙

<!-- b000190 | prose | pages [7] -->
∝=

<!-- b000191 | prose | pages [7] -->
(Eq. 4-3)

<!-- b000192 | prose | pages [7] -->
∝3, 𝐴𝑢𝑔 − 𝑆𝑒𝑝𝑡

<!-- b000193 | furniture | pages [7] -->


<!-- b000194 | prose | pages [7] -->
∝4, 𝐽𝑢𝑛 − 𝐽𝑢𝑙

<!-- b000195 | furniture | pages [7] -->


<!-- b000196 | prose | pages [7] -->
∝5, 𝑂𝑐𝑡 − 𝑁𝑜𝑣

<!-- b000197 | prose | pages [7] -->
{

<!-- b000198 | prose | pages [7] -->
So far, the basic colony growth model has been completed. Combined with the introduction of the Vespa Mandarinia (2021mcm)_ ProblemC_ Vespamandarina.pdf ）

<!-- b000199 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000200 | prose | pages [7] -->
According to the relevant information[2], we get that when the colony exceeds 𝐾, the colony begins to migrate outward. At this time, the queen of the colony will take away about half of the colony, and the maximum migration distance of the colony is about 30 km.

<!-- b000201 | prose | pages [7] -->
Based on this, each time the colony moves out:

<!-- b000202 | prose | pages [7] -->
𝑁(𝑥𝑖,𝑦𝑖,𝑡𝑖)

<!-- b000203 | prose | pages [7] -->
𝑁(𝑥𝑖+1, 𝑦𝑖+1, 𝑡𝑖+1) =

<!-- b000204 | prose | pages [7] -->
−𝜇𝑁(𝑥𝑖, 𝑦𝑖, 𝑡𝑖)                            (Eq. 4-4) 2 Represents the population density change of the next coordinate position. At the same time, the distance between 𝑥 and 𝑦 coordinates will not change more than 30 km.

<!-- b000205 | prose | pages [7] -->
From the analysis of the topic and the study of the characteristics of the data, we found that the data given by the topic are eyewitness reports at different times and places, but not necessarily represent the nest location of the Vespa Mandarinia. The time and space of its report are random due to certain human factors. In order to analyze the probability of eyewitness events, we use Gaussian distribution function to describe the probability of spontaneous combustion events

<!-- b000206 | prose | pages [7] -->
√2𝜋𝜎𝑒(− (𝑥−𝜇)2

<!-- b000207 | prose | pages [7] -->
𝑝(𝑥) =

<!-- b000208 | prose | pages [7] -->
1 1

<!-- b000209 | prose | pages [7] -->
2𝜎2 )                                                  (Eq. 4-5)

<!-- b000210 | prose | pages [7] -->
Then the change of each coordinate point is as follows： (𝑥𝑖+1, 𝑦𝑖+1) = (𝑥𝑖+ 𝑝(𝑥𝑖) ∙𝑑𝑥, 𝑦𝑖+ 𝑝(𝑦𝑖) ∙𝑑𝑦, )                                   (Eq. 4-6)

<!-- b000211 | prose | pages [7] -->
Where 𝑑𝑥 and 𝑑𝑦 represent the maximum degree of each latitude-longitude change. So far, we have completed the establishment of the colony propagation and prediction model for the sighting of the wasp. It should be noted that since the data given by the topic is the time and place of the eyewitness event, the propagation and prediction model is fitting and analyzing the eyewitness event rather than the population itself. Due to the randomness of human witness, the analysis results of the model will give the maximum latitude and longitude range of possible eyewitness events in the future.

<!-- b000212 | heading | pages [7] -->
4.2    Model Validation

<!-- b000213 | prose | pages [7] -->
Since the data corresponding to the "positive-ID" is the report of witnessing Vespa mandarinia which has been confirmed manually, we verify the model based on the "positive-ID" in the data set, so as to fit the real propagation range of the Vespa Mandarinia population as correctly as possible.

<!-- b000214 | prose | pages [7] -->
Take all the data of "positive-ID" and make the distribution map based on space:

<!-- b000215 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000216 | furniture | pages [7] -->
关注数学模型

<!-- b000217 | furniture | pages [7] -->
2

<!-- b000218 | furniture | pages [7] -->
MATHmodels

<!-- b000219 | furniture | pages [7] -->
获取更多资讯

<!-- b000220 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000221 | furniture | pages [8] -->
Team # 2107815                                                                 Page 8 of 25

<!-- b000222 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000223 | furniture | pages [8] -->


<!-- b000224 | furniture | pages [8] -->


<!-- b000225 | furniture | pages [8] -->


<!-- b000226 | prose | pages [8] -->
Fig.4-1    Data Distribution

<!-- b000227 | furniture | pages [8] -->


<!-- b000228 | prose | pages [8] -->
Fig.4-2    Comparison of "Positive ID"

<!-- b000229 | prose | pages [8] -->
Prediction and Actual Distribution

<!-- b000230 | prose | pages [8] -->
We can see that most of the "positive-ID" eyewitness events are concentrated in one area. As for the sightings on Vancouver Island, we do not think that the local bee colony may continue to spread because the nest were destroyed rapidly after the incident. For the relative deviation from the event concentration area (48.777534 °N,

<!-- b000231 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000232 | prose | pages [8] -->
22.418612 °W), we think that the wasp colony may arrive there for some reason, so we don't add its data in the validation of the model.

<!-- b000233 | prose | pages [8] -->
For the data of  the "positive-ID" centralized area, we select the point where the "positive-ID" witness event first occurs in this area as the propagation point of the propagation model, and apply the model to predict. The distribution range of "positive-ID" predicted by the model and the actual distribution map of "positive-ID" are as Fig.4-2.

<!-- b000234 | prose | pages [8] -->
It can be seen from the results that the maximum distribution range of predicted points basically includes the actual distribution of data points. And the distribution of predicted points is more fit with the distribution of actual data points. This proves the validity of the model to a certain extent.

<!-- b000235 | heading | pages [8] -->
4.3    Model Accuracy Analysis

<!-- b000236 | heading | pages [8] -->
4.3.1    Preliminary Demonstration

<!-- b000237 | prose | pages [8] -->
As mentioned earlier, the propagation model predicts the longest distance between the predicted point and the starting point of the communication as 𝑑𝑚𝑎𝑥. Besides, the radius of the range of activity of Vespa Mandarinia is 30 km, If 𝑑𝑚𝑎𝑥 is less than 30km or close to 30km, the accuracy of the propagation model is high and the model is reasonable. Because the probability of eyewitness events can be described by Gaussian distribution function:

<!-- b000238 | prose | pages [8] -->
√2𝜋𝜎𝑒(− (𝑥−𝜇)2

<!-- b000239 | prose | pages [8] -->
1

<!-- b000240 | prose | pages [8] -->
𝑝(𝑥) =

<!-- b000241 | prose | pages [8] -->
2𝜎2 )                                                        (Eq. 4-5)

<!-- b000242 | prose | pages [8] -->
So 𝑡he distribution of 𝑑𝑚𝑎𝑥 also conforms to Gaussian distribution function. After many simulations, we get a lot of 𝑑𝑚𝑎𝑥 After data statistics and curve fitting, the results are as follows:

<!-- b000243 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000244 | furniture | pages [8] -->


<!-- b000245 | prose | pages [8] -->
Fig.4-3    Distribution Curve of 𝑑𝑚𝑎𝑥

<!-- b000246 | furniture | pages [8] -->
关注数学模型

<!-- b000247 | furniture | pages [8] -->
2

<!-- b000248 | furniture | pages [8] -->
MATHmodels

<!-- b000249 | furniture | pages [8] -->
获取更多资讯

<!-- b000250 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000251 | furniture | pages [9] -->
Team # 2107815                                                                 Page 9 of 25

<!-- b000252 | prose | pages [9] -->
Its mean value is 20.9638km, less than 30km, which can preliminarily demonstrate the rationality and accuracy of the propagation model based on time and space.

<!-- b000253 | heading | pages [9] -->
4.3.2    Precise Demonstration

<!-- b000254 | prose | pages [9] -->
Since the eyewitness events of "positive ID" are concentrated in one area, the farther the location of the

<!-- b000255 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000256 | prose | pages [9] -->
eyewitness report to be confirmed is from the area of "positive ID" eyewitness events is, the lower the probability of it being determined as "positive ID" is, that is to say, the lower the accuracy of the model is.

<!-- b000257 | prose | pages [9] -->
We record the longest distance between the prediction point and the propagation starting point of the propagation model as 𝑑𝑚𝑎𝑥 based on this, we establish the relationship between the confidence degree 𝑦 and the distance 𝑑 between the incident point of the eyewitness report and the propagation starting point of the propagation model:

<!-- b000258 | prose | pages [9] -->
(𝑑𝑚𝑎𝑥+30) 𝑑2 + 1              0 ≤𝑑≤𝑑𝑚𝑎𝑥+ 30

<!-- b000259 | prose | pages [9] -->
0.5

<!-- b000260 | prose | pages [9] -->
𝑦= −

<!-- b000261 | prose | pages [9] -->
{

<!-- b000262 | prose | pages [9] -->
0.5(𝑑𝑚𝑎𝑥+30)

<!-- b000263 | prose | pages [9] -->
(Eq. 4-7)

<!-- b000264 | prose | pages [9] -->
𝑑≥𝑑𝑚𝑎𝑥+ 30

<!-- b000265 | prose | pages [9] -->
𝑦=

<!-- b000266 | prose | pages [9] -->
𝑥

<!-- b000267 | prose | pages [9] -->
𝑑𝑚𝑎𝑥 is the farthest distance between the predicted point and the propagation starting point of the propagation model, while the radius of the range of activity of Vespa Mandarinia is 30km, so the distance

<!-- b000268 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000269 | prose | pages [9] -->
between the predicted point and the propagation starting point of the propagation model is greater than 𝑑𝑚𝑎𝑥 + 30, the probability of occurrence of Vespa Mandarinia will be greatly reduced, and the accuracy of the model will decline, that is to say, the confidence y will decline.

<!-- b000270 | prose | pages [9] -->
The change curve of model confidence 𝑦 with distance 𝑑 is as follows:

<!-- b000271 | furniture | pages [9] -->


<!-- b000272 | heading | pages [9] -->
Fig .4-4    The Change Curve of Model Confidence 𝑦 with Distance 𝑑

<!-- b000273 | prose | pages [9] -->
Based on this consideration, after completing the model construction, we test the spatial position of the original "positive ID" and "negative ID" and get the verification results. The classification verification results of "positive ID" and "negative ID" are shown in the following table:

<!-- b000274 | prose | pages [9] -->
positive-ID Classification

<!-- b000275 | prose | pages [9] -->
Classification

<!-- b000276 | heading | pages [9] -->
results

<!-- b000277 | prose | pages [9] -->
confidence

<!-- b000278 | prose | pages [9] -->
Location_1 0.999632807 positive-ID Location _2 0.869928517 positive-ID Location _3 0.99715875 positive-ID Location _4 0.990021233 positive-ID Location _5 0.973325095 positive-ID Location _6 0.804770475 positive-ID Location _7 0.999273953 positive-ID Location _8 0.987370301 positive-ID Location _9 0.998269998 positive-ID Location _10

<!-- b000279 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000280 | furniture | pages [9] -->
0.998453137

<!-- b000281 | furniture | pages [9] -->
positive-ID

<!-- b000282 | prose | pages [9] -->
negative-ID Classification

<!-- b000283 | prose | pages [9] -->
Classification

<!-- b000284 | heading | pages [9] -->
results

<!-- b000285 | prose | pages [9] -->
confidence Location _1 0.100877 negative-ID Location _2 0.07113 negative-ID Location _3 0.082362 negative-ID Location _4 0.16729 negative-ID Location _5 0.163856 negative-ID Location _6 0.165152 negative-ID Location _7 0.065973 negative-ID Location _8 0.749729 positive-ID Location _9 0.147732 negative-ID Location _10

<!-- b000286 | furniture | pages [9] -->
0.127481

<!-- b000287 | prose | pages [9] -->
negative-ID

<!-- b000288 | furniture | pages [9] -->
关注数学模型

<!-- b000289 | furniture | pages [9] -->
2

<!-- b000290 | furniture | pages [9] -->
MATHmodels

<!-- b000291 | furniture | pages [9] -->
获取更多资讯

<!-- b000292 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000293 | furniture | pages [10] -->
Team # 2107815                                                                 Page 10 of 25

<!-- b000294 | prose | pages [10] -->
Location _11

<!-- b000295 | furniture | pages [10] -->
0.998503002

<!-- b000296 | furniture | pages [10] -->
positive-ID

<!-- b000297 | prose | pages [10] -->
Location _12 0.998269081 positive-ID Location _13 0.998268418 positive-ID Location _11

<!-- b000298 | furniture | pages [10] -->
0.123332

<!-- b000299 | prose | pages [10] -->
negative-ID Location _12 0.800434 positive-ID Location _13 0.259934 negative-ID

<!-- b000300 | prose | pages [10] -->
Table.4-1      The classification verification results of "positive ID" propagation model and part of

<!-- b000301 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000302 | prose | pages [10] -->
"negative ID" propagation model

<!-- b000303 | prose | pages [10] -->
The accuracy of positive ID is higher than that of negative ID, which is 84.6%. For this result, we think that the appearance of negative ID does not have absolute spatiotemporal characteristics because negative ID may also appear near positive ID. At the same time, it also shows that it is obviously insufficient to classify and predict the topic data set only from the perspective of temporal and spatial communication model. A comprehensive analysis of various types of data is needed. This will be elaborated in the subsequent model building.

<!-- b000304 | heading | pages [10] -->
5    Establishment and Validation of Three Dimensional Comprehensive Analysis

<!-- b000305 | heading | pages [10] -->
and Prediction Model

<!-- b000306 | heading | pages [10] -->
5.1    Data Information Description

<!-- b000307 | prose | pages [10] -->
We build three models according to the three parts of valid data

<!-- b000308 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000309 | prose | pages [10] -->
⚫ Communication model for analyzing the time and location of eyewitness reports. ⚫ LDA based text classification model for analyzing reporter's language description. ⚫ Image recognition model based on CNN for analyzing eyewitness report pictures. In order to improve the accuracy of the first mock exam and reduce the influence of single model error, we add a weighted sum to the three models according to certain weights and combine them into a comprehensive model to improve the accuracy of recognition.

<!-- b000310 | heading | pages [10] -->
5.2  LDA Based Text Classification Model

<!-- b000311 | heading | pages [10] -->
5.2.1  The Establishment of Text Classification Model

<!-- b000312 | prose | pages [10] -->
We already know that the “Notes” text information in the data set contains a certain description of the insect features in the report. The analysis and research of these feature description information will improve the sufficiency of the data feature utilization of the model. For this reason, according to the text characteristics of “Notes” information, we establish a text feature classification model based on LDA (Latent Dirichlet Allocation) model[4] to analyze the possibility of prediction error classification based on “Notes” text features.

<!-- b000313 | prose | pages [10] -->
The core of text classification is how to extract the key features that can reflect the characteristics of the text from the text, and capture the mapping between the features and the categories[5]. Using the bag-of-word model, we assume that each paragraph of "Notes" is a bag composed of characteristic words, and each word appears independently, regardless of the order of words. We can think that such an analysis method is effective in the context of this article.

<!-- b000314 | prose | pages [10] -->
When analyzing the characteristics of the text, we can regard the text as the result of constantly generating words randomly. Each word is generated independently. Then, we need to analyze two issues:

<!-- b000315 | prose | pages [10] -->
⚫ Solution of model parameters ⚫ The correspondence of the rules of generating words in the model.

<!-- b000316 | prose | pages [10] -->
As to the “Notes” text, we assume that the corpus has 𝑛  segments:𝜔1, 𝜔2, … … 𝜔𝑛 , and there are 𝑚 words: 𝜈1, 𝜈2, … … 𝜈𝑚.The probability of each word is as follows:

<!-- b000317 | prose | pages [10] -->
𝑝⃗= {𝑝1, 𝑝2, … … , 𝑝𝑚}                                               (Eq. 5-1) And it obeys multinomial distribution:

<!-- b000318 | prose | pages [10] -->
𝜈~𝑀𝑢𝑙𝑡(𝜈|𝑝⃗)                                                           (Eq. 5-2) Each time, the model independently generates a word to become the 𝑖th word of the text, and loops this process to generate the corresponding text. When considering that all parameters should be random variables, the

<!-- b000319 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000320 | furniture | pages [10] -->
关注数学模型

<!-- b000321 | furniture | pages [10] -->
2

<!-- b000322 | furniture | pages [10] -->
MATHmodels

<!-- b000323 | furniture | pages [10] -->
获取更多资讯

<!-- b000324 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000325 | furniture | pages [11] -->
Team # 2107815                                                                 Page 11 of 25

<!-- b000326 | prose | pages [11] -->
model should have a variety of words, and the probability of each word being selected is not the same. The parameter 𝑝⃗ of each word should obey a probability distribution 𝑝(𝑝⃗), which is called the prior distribution of 𝑝⃗. At the same time, we choose the Dirichlet distribution as the best choice of the prior distribution:

<!-- b000327 | prose | pages [11] -->
𝑘 Γ(∑ 𝛼𝑖 )

<!-- b000328 | prose | pages [11] -->
𝛼𝑖−1 𝑚 (Eq. 5-3)

<!-- b000329 | prose | pages [11] -->
𝑖=1

<!-- b000330 | prose | pages [11] -->
∏

<!-- b000331 | prose | pages [11] -->
𝐷𝑖𝑟(𝑥1, 𝑥2, … … 𝑥𝑘|𝛼1, 𝛼2, … … 𝛼𝑘) =

<!-- b000332 | prose | pages [11] -->
𝑥𝑖

<!-- b000333 | prose | pages [11] -->
𝑖=1

<!-- b000334 | prose | pages [11] -->
𝑘 ∏ Γ(𝛼𝑖)

<!-- b000335 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000336 | prose | pages [11] -->
𝑖=1

<!-- b000337 | prose | pages [11] -->
Since the conjugate prior distribution of multinomial distribution is Dirichlet distribution, the posterior distribution also follows Dirichlet distribution

<!-- b000338 | prose | pages [11] -->
𝑘 Γ(∑ (𝛼𝑖+𝑛𝑖) 𝑖=1

<!-- b000339 | prose | pages [11] -->
𝐷𝑖𝑟(𝑝⃗|𝑛⃗⃗+ 𝑎⃗) =

<!-- b000340 | prose | pages [11] -->
𝑘

<!-- b000341 | prose | pages [11] -->
)

<!-- b000342 | prose | pages [11] -->
𝛼𝑖+𝑛𝑖−1 𝑚 (Eq. 5-4)

<!-- b000343 | prose | pages [11] -->
∏ 𝑝𝑖

<!-- b000344 | prose | pages [11] -->
𝑖=1

<!-- b000345 | prose | pages [11] -->
Γ(𝛼𝑖+𝑛𝑖) ∏ 𝑖=1

<!-- b000346 | prose | pages [11] -->
Then, we use the expectation of Dirichlet distribution to estimate 𝑝⃗:

<!-- b000347 | prose | pages [11] -->
𝛼1+𝑛1

<!-- b000348 | prose | pages [11] -->
𝐸(𝑝⃗) = (

<!-- b000349 | prose | pages [11] -->
, 𝑚 ∑

<!-- b000350 | prose | pages [11] -->
∑

<!-- b000351 | prose | pages [11] -->
(𝛼𝑖+𝑛𝑖) 𝑖=1

<!-- b000352 | prose | pages [11] -->
𝛼2+𝑛2

<!-- b000353 | prose | pages [11] -->
𝛼𝑚+𝑛𝑚 )                            (Eq. 5-5)

<!-- b000354 | prose | pages [11] -->
, … … 𝑚 𝑚

<!-- b000355 | prose | pages [11] -->
𝑚 ∑

<!-- b000356 | prose | pages [11] -->
(𝛼𝑖+𝑛𝑖)

<!-- b000357 | prose | pages [11] -->
(𝛼𝑖+𝑛𝑖)

<!-- b000358 | prose | pages [11] -->
𝑖=1 𝑖=1

<!-- b000359 | prose | pages [11] -->
𝑖=1

<!-- b000360 | prose | pages [11] -->
According to the analysis of the  “Notes”  information in the data set, we think that when a reporter writes a paragraph of “Notes”, he may involve both "positive" and "negative" topics. Under each topic, the probability of words appearing is also different. When the best choice of prior distribution is still Dirichlet distribution, we set up LDA topic model which can be used to analyze “Notes” text features. The main process is shown in the

<!-- b000361 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000362 | prose | pages [11] -->
figure:

<!-- b000363 | prose | pages [11] -->
It can be seen from the figure that the model mainly includes two processes:

<!-- b000364 | prose | pages [11] -->
⚫ Randomly Extracting a topic 𝜃⃗𝑚 from text topics. Generating the topic and get the topic number 𝑧𝑚,𝑛. ⚫ Randomly selecting 𝑘 words from the subject words, and choose 𝑧𝑚,𝑛 as the number for the subject of

<!-- b000365 | prose | pages [11] -->
𝜑⃗⃗𝑘. And randomly Generating  words 𝜔𝑚,𝑛.

<!-- b000366 | furniture | pages [11] -->


<!-- b000367 | prose | pages [11] -->
Fig.5-1    LDA Probability Graph Model

<!-- b000368 | prose | pages [11] -->
So far, we have completed the establishment of LDA based text classification model for analyzing “Notes” text features. The Gibbs sampling algorithm is used to solve the topic distribution in each piece of text information and the word distribution in two kinds of topics.

<!-- b000369 | heading | pages [11] -->
5.2.2    Text Analysis

<!-- b000370 | prose | pages [11] -->
According to the data set provided by the topic “2021mcmproblem C_ DataSet.xlsx”, We extract the "Notes" comment text information as text analysis data.

<!-- b000371 | prose | pages [11] -->
Firstly, according to the label of "Lab status", the "“Notes”" text data is divided into "positive-ID" and "negative-ID" as the analysis data of the model.

<!-- b000372 | prose | pages [11] -->
After building the bag of words and using the model to analyze the data, we get the probability distribution of the feature words analyzed by the model in the two types of label text data:

<!-- b000373 | furniture | pages [11] -->


<!-- b000374 | furniture | pages [11] -->


<!-- b000375 | prose | pages [11] -->
Table.5-1     Probability Distribution of Feature Words of "Positive-ID" and "Negative-ID"

<!-- b000376 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000377 | furniture | pages [11] -->
关注数学模型

<!-- b000378 | furniture | pages [11] -->
2

<!-- b000379 | furniture | pages [11] -->
MATHmodels

<!-- b000380 | furniture | pages [11] -->
获取更多资讯

<!-- b000381 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000382 | furniture | pages [12] -->
Team # 2107815                                                                 Page 12 of 25

<!-- b000383 | prose | pages [12] -->
Feature words

<!-- b000384 | prose | pages [12] -->
𝑝⃗ positive-ID

<!-- b000385 | prose | pages [12] -->
hornet 0.017 inch 0.016 WSDA 0.011

<!-- b000386 | prose | pages [12] -->
Feature words

<!-- b000387 | prose | pages [12] -->
𝑝⃗ negative-ID

<!-- b000388 | prose | pages [12] -->
picture 0.014 found 0.013 dead 0.013

<!-- b000389 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000390 | prose | pages [12] -->
photo 0.008 wasp 0.007 Asian 0.007 dead 0.006 yellow 0.005 flew 0.005 orange 0.004 killed 0.011 hornet 0.011 caught 0.010 inch 0.008 stinger 0.006 September 0.005 feature 0.004 From this, it is not difficult for us to see that the "Notes" text information classified as "positive-ID" has a higher probability of feature words, such as "hornet", "wasp", "Asian" and "yellow", which are more prepared to describe the characteristics of Vespa mandarinia. However, the "Notes" text information feature words classified as "negative-ID" are relatively lack of accuracy. This proves the validity of the text classification model. Moreover, this classification result is more convenient for us to analyze the confidence level of the results produced by the model. In the "Notes" text analysis of this paper, we think that the classification result generated by the direct application model is the probability of a "Notes" information belonging to the correct or wrong classification.

<!-- b000391 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000392 | prose | pages [12] -->
Based on this consideration, after completing the model construction, we test the original "positive-ID" and "negative-ID" texts and get the verification results. The classification verification results of "positive ID" are shown in the following table:

<!-- b000393 | prose | pages [12] -->
Table.5-2       "Positive-ID" Text Classification Verification Results and Some "Negative-ID" Text

<!-- b000394 | prose | pages [12] -->
Classification Verification Results

<!-- b000395 | prose | pages [12] -->
Classification

<!-- b000396 | prose | pages [12] -->
Classification

<!-- b000397 | prose | pages [12] -->
positive-ID

<!-- b000398 | heading | pages [12] -->
Results

<!-- b000399 | prose | pages [12] -->
Confidence

<!-- b000400 | prose | pages [12] -->
“Notes”_1 positive-ID 0.087097965 “Notes”_2 negative-ID 0.462730795 “Notes”_3 unknown 0.5 “Notes”_4 unknown 0.5 “Notes”_5 positive-ID 0.067911513 “Notes”_6 unknown 0.5 “Notes”_7 negative-ID 0.127468228 “Notes”_8 positive-ID 0.951170862 “Notes”_9 positive-ID 0.932664335 “Notes”_10 positive-ID 0.865896285 “Notes”_11 negative-ID 0.150539279 “Notes”_12 positive-ID 0.903999627 “Notes”_13 negative-ID 0.121834569

<!-- b000401 | prose | pages [12] -->
Classification

<!-- b000402 | prose | pages [12] -->
Classification

<!-- b000403 | prose | pages [12] -->
negative-ID

<!-- b000404 | heading | pages [12] -->
Results

<!-- b000405 | prose | pages [12] -->
Confidence “Notes”_1 positive-ID 0.083589226 “Notes”_2 positive-ID 0.128571451 “Notes”_3 positive-ID 0.394981176 “Notes”_4 negative-ID 0.917768717 “Notes”_5 negative-ID 0.948983371 “Notes”_6 unknown 0.5 “Notes”_7 negative-ID 0.950886071 “Notes”_8 negative-ID 0.941335261 “Notes”_9 negative-ID 0.961205304 “Notes”_10 negative-ID 0.952122569 “Notes”_11 negative-ID 0.967354596 “Notes”_12 unknown 0.5 “Notes”_13 negative-ID 0.720488369 In the above experimental results, the confusion matrix of model classification is obtained:

<!-- b000406 | furniture | pages [12] -->


<!-- b000407 | prose | pages [12] -->
Fig.5-2           LDA Model Classification Result Confusion Matrix

<!-- b000408 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000409 | prose | pages [12] -->
In the statistical results, the classification accuracy of "negative-ID" is higher, while the classification

<!-- b000410 | furniture | pages [12] -->
关注数学模型

<!-- b000411 | furniture | pages [12] -->
2

<!-- b000412 | furniture | pages [12] -->
MATHmodels

<!-- b000413 | furniture | pages [12] -->
获取更多资讯

<!-- b000414 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000415 | furniture | pages [13] -->
Team # 2107815                                                                 Page 13 of 25

<!-- b000416 | prose | pages [13] -->
accuracy of "positive ID" is less than 50%. For this result, we think that too few text samples of "positive ID" may be the main reason for the low classification accuracy of the model, because the model can not fully understand the characteristics of "positive ID". At the same time, it also shows that it is obviously insufficient to classify and predict the topic data set only from the text aspect. A comprehensive analysis of various types of data is needed. This will be elaborated in the subsequent model building.

<!-- b000417 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000418 | heading | pages [13] -->
5.3    CNN Based Image Recognition Model

<!-- b000419 | heading | pages [13] -->
5.3.1    Model Construction

<!-- b000420 | prose | pages [13] -->
Suppose we have a training set 𝑇𝑟𝑖𝑎𝑛= {(𝑋1, 𝑦1), (𝑋2, 𝑦2), (𝑋3, 𝑦3), … , , (𝑋𝑛, 𝑦𝑛)}, which includes a set of n valid training pictures. Test set 𝑇𝑒𝑠𝑡= {(𝑈1, 𝑣1), (𝑈2, 𝑣2), (𝑈3, 𝑣3), … , , (𝑈𝑚, 𝑣𝑚)}, which includes a set of n valid test pictures. The number ratio between the training set and the test set is best maintained at around 7:3. Our goal is to design a deep learning model f, let:

<!-- b000421 | prose | pages [13] -->
𝑓(𝑋′) = 𝑦′

<!-- b000422 | furniture | pages [13] -->


<!-- b000423 | furniture | pages [13] -->


<!-- b000424 | prose | pages [13] -->
(Eq. 5-11) Where 𝑋′ is the picture to be recognized, and 𝑦′ is the classification result output by the model. According to the above model, we have constructed a convolutional neural network structure with 6 layers. The first layer is the input layer, and the first layer of the network receives a 32´32 3-channel image. Then through

<!-- b000425 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000426 | prose | pages [13] -->
multiple convolutions and pooling operations, and finally access to the fully connected layer, softmax classification of features is performed to obtain the inference result.

<!-- b000427 | prose | pages [13] -->
The softmax cross entropy loss function is a commonly used loss function, and its formula is as follows:

<!-- b000428 | prose | pages [13] -->
log 𝑦𝑖

<!-- b000429 | furniture | pages [13] -->


<!-- b000430 | furniture | pages [13] -->


<!-- b000431 | prose | pages [13] -->
(Eq. 5-12) E(t, y) = −∑𝑡𝑗 𝑗 Among them, t and y represent the target label and output of the neural network, respectively, and 𝑦𝑖 represents the softmax loss function:

<!-- b000432 | prose | pages [13] -->
𝑒𝑧𝑗

<!-- b000433 | furniture | pages [13] -->


<!-- b000434 | furniture | pages [13] -->


<!-- b000435 | furniture | pages [13] -->


<!-- b000436 | prose | pages [13] -->
(Eq. 5-13)

<!-- b000437 | prose | pages [13] -->
𝑦𝑖= 𝑠𝑜𝑓𝑡𝑚𝑎𝑥(𝑧𝑗) =

<!-- b000438 | prose | pages [13] -->
∑𝑒𝑧𝑗 𝑗

<!-- b000439 | prose | pages [13] -->
The neural network model we built is shown in the figure below; In the data set provided by the title, there are 14 positive-IDs, while the number of negative-IDs is as high as 3194. The number of positive-ID is too scarce, and the ratio of negative-ID to positive-ID is obviously out of balance. Therefore, if we directly use the data provided by the title, it may cause under-fitting or over-fitting.

<!-- b000440 | prose | pages [13] -->
In order to solve this problem, we downloaded dataset D from the open source dataset obtained on the website [7], which includes 4943 positive-IDs and 3183 negative-IDs and other insect data. The quality of the downloaded data is high, and the classification and labeling work has been done. We divide the data set D into two parts, the first part is TRAIN, training set, and the second part is VALIDATION, validation set. Finally, use the data set given by the title as the TEST, the test set.

<!-- b000441 | prose | pages [13] -->
Randomly select part of the data in the above data sets (train set, validation set, test set) as the model. Visualize the selected data, as shown in the figure below:

<!-- b000442 | prose | pages [13] -->
Based on the above convolutional neural network model, 15 rounds of iterative training are performed, and the performance evaluation of the model is completed by analyzing the accuracy value.

<!-- b000443 | furniture | pages [13] -->


<!-- b000444 | furniture | pages [13] -->


<!-- b000445 | prose | pages [13] -->
Fig.5-3  CNN Neural Network Model                            Fig.5-4  Train、Validation、Test

<!-- b000446 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000447 | furniture | pages [13] -->
关注数学模型

<!-- b000448 | furniture | pages [13] -->
2

<!-- b000449 | furniture | pages [13] -->
MATHmodels

<!-- b000450 | furniture | pages [13] -->
获取更多资讯

<!-- b000451 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000452 | furniture | pages [14] -->
Team # 2107815                                                                 Page 14 of 25

<!-- b000453 | heading | pages [14] -->
5.3.2    Model evaluation

<!-- b000454 | prose | pages [14] -->
After 15 iterations of the training set, validation set, and test set with the above neural network, we visualize the value of the training set loss, categorical_accuracy, and the test set loss val_loss, val_categorical_accuracy values:

<!-- b000455 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000456 | furniture | pages [14] -->


<!-- b000457 | furniture | pages [14] -->


<!-- b000458 | furniture | pages [14] -->


<!-- b000459 | prose | pages [14] -->
Fig.5-5 Trend Graph First of all, according to the trend, the loss of the training set continues to decline, and the loss of the test set

<!-- b000460 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000461 | prose | pages [14] -->
also continues to get down, indicating that the network is still learning, showing that the model has no data set problems. The continuous decrease of training set loss indicates the correctness of the parameter setting of the learning rate.

<!-- b000462 | prose | pages [14] -->
On the test set, the accuracy rate is above 75%, and the highest is 91.75%. It shows that the text identification model can accurately complete the classification of positive-IDs, negative-IDs and insect, and achieve good performance.

<!-- b000463 | prose | pages [14] -->
In summary, this paper transforms the recognition problem of bees and wasps into a pattern recognition problem by classifying the images of bees and wasps. We built a convolutional neural network model and set up an experimental environment. Through the evaluation and analysis of the experimental results, we achieved good experimental results. The above statement shows that this method can well identify different kinds of bees.

<!-- b000464 | heading | pages [14] -->
5.4    Establishment of Comprehensive Analysis and Prediction Model

<!-- b000465 | prose | pages [14] -->
At present, we have completed the establishment and verification of the analysis model of spatiotemporal, text and image information in the dataset. At the same time, from the verification results of each independent model, we can also see that only relying on a single type of information analysis model, we can not get higher goodness of fit for the two types of data. It also shows that it is necessary to integrate all types of data provided in the data set to analyze the possibility of correct and wrong classification of the prediction data set.

<!-- b000466 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000467 | furniture | pages [14] -->


<!-- b000468 | furniture | pages [14] -->
关注数学模型

<!-- b000469 | prose | pages [14] -->
Fig.5-6     3-D Analysis Model Structure

<!-- b000470 | furniture | pages [14] -->
2

<!-- b000471 | furniture | pages [14] -->
MATHmodels

<!-- b000472 | furniture | pages [14] -->
获取更多资讯

<!-- b000473 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000474 | furniture | pages [15] -->
Team # 2107815                                                                 Page 15 of 25

<!-- b000475 | prose | pages [15] -->
Here, we build a three-dimensional analysis model based on the above analysis. The model divides spatiotemporal, text and image information into three dimensions, and considers the final analysis results by integrating the effective information weight of each dimension. The structure of the model is shown in the Fig 5- 6.

<!-- b000476 | prose | pages [15] -->
The basic process is as follows:

<!-- b000477 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000478 | prose | pages [15] -->
⚫ For the eyewitness report in the data, extracting the space-time, text and image information, and give

<!-- b000479 | prose | pages [15] -->
each dimension of the model. ⚫ The model of each dimension analyzes the given information and gives the classification possibility of

<!-- b000480 | prose | pages [15] -->
a single dimension. ⚫ The model comprehensively reports the amount of effective information of each dimension and gives

<!-- b000481 | prose | pages [15] -->
weight to the classification possibility provided by each dimension:

<!-- b000482 | prose | pages [15] -->
𝑤1 × 𝑃𝑆𝑝𝑎𝑐𝑒−𝑇𝑖𝑚𝑒

<!-- b000483 | prose | pages [15] -->
𝑤2 × 𝑃𝑇𝑒𝑥𝑡 𝑤3 × 𝑃𝐼𝑚𝑎𝑔𝑒 Where, 𝑤1，𝑤2 and 𝑤3 is the weight value given to different dimensions, 𝑃1，𝑃2和𝑃3 is the classification possibility provided by each dimension model.

<!-- b000484 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000485 | prose | pages [15] -->
The final classification possibility given by the model is as follows: 𝑃𝑐𝑙𝑎𝑠𝑠𝑖𝑓𝑖𝑐𝑎𝑡𝑖𝑜𝑛= 𝑤1 × 𝑃𝑆𝑝𝑎𝑐𝑒−𝑇𝑖𝑚𝑒+ 𝑤2 × 𝑃𝑇𝑒𝑥𝑡+ 𝑤3 × 𝑃𝐼𝑚𝑎𝑔𝑒

<!-- b000486 | furniture | pages [15] -->


<!-- b000487 | furniture | pages [15] -->


<!-- b000488 | prose | pages [15] -->
(Eq. 5-14) So far, this paper has completed the establishment of data set comprehensive three-dimensional analysis and prediction model.

<!-- b000489 | heading | pages [15] -->
5.5    Verification and Prediction of Three-Dimensional Comprehensive Model

<!-- b000490 | prose | pages [15] -->
After the establishment of the model, we first use the positive-ID and negative-ID which have been manually labeled in the dataset to verify the goodness of fit of the model.After extracting the data, according to the algorithm flow of the three-dimensional comprehensive model, we assign three different kinds of data in the data to three-dimensional models and test them.

<!-- b000491 | prose | pages [15] -->
Table.5-3       Goodness of Fit of Test Data

<!-- b000492 | prose | pages [15] -->
Data Type positive-ID negative-ID Goodness of Fit 92.86% 85.22%

<!-- b000493 | prose | pages [15] -->
Table.5-4      Analysis Confidence of Each Data Point (Positive-ID and Partial Negative-ID Results)

<!-- b000494 | prose | pages [15] -->
Classification

<!-- b000495 | prose | pages [15] -->
Classification

<!-- b000496 | prose | pages [15] -->
positive-ID

<!-- b000497 | heading | pages [15] -->
Results

<!-- b000498 | prose | pages [15] -->
Confidence

<!-- b000499 | prose | pages [15] -->
data_1 positive-ID 0.590298 data_2 positive-ID 0.588034 data_3 negative-ID 0.446313 data_4 positive-ID 0.658625 data_5 positive-ID 0.645371 data_6 positive-ID 0.50535 data_7 positive-ID 0.621527 data_8 positive-ID 0.525908 data_9 positive-ID 0.781534 data_10 positive-ID 0.778071 data_11 positive-ID 0.545667 data_12 positive-ID 0.753277 data_13 positive-ID 0.578013

<!-- b000500 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000501 | prose | pages [15] -->
Classification

<!-- b000502 | prose | pages [15] -->
Classification

<!-- b000503 | prose | pages [15] -->
negative-ID

<!-- b000504 | heading | pages [15] -->
Results

<!-- b000505 | prose | pages [15] -->
Confidence data_1 negative-ID 0.941994 data_2 negative-ID 0.739541 data_3 negative-ID 0.776686 data_4 negative-ID 0.771844 data_5 negative-ID 0.684035 data_6 negative-ID 0.7519 data_7 negative-ID 0.781358 data_8 negative-ID 0.804744 data_9 negative-ID 0.66207 data_10 negative-ID 0.749756 data_11 positive-ID 0.473413 data_12 negative-ID 0.761956 data_13 negative-ID 0.801141

<!-- b000506 | furniture | pages [15] -->
关注数学模型

<!-- b000507 | furniture | pages [15] -->
2

<!-- b000508 | furniture | pages [15] -->
MATHmodels

<!-- b000509 | furniture | pages [15] -->
获取更多资讯

<!-- b000510 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000511 | furniture | pages [16] -->
Team # 2107815                                                                 Page 16 of 25

<!-- b000512 | furniture | pages [16] -->
data_14

<!-- b000513 | furniture | pages [16] -->
positive-ID

<!-- b000514 | furniture | pages [16] -->
0.541431

<!-- b000515 | furniture | pages [16] -->


<!-- b000516 | furniture | pages [16] -->
data_14

<!-- b000517 | prose | pages [16] -->
negative-ID

<!-- b000518 | furniture | pages [16] -->
0.865888

<!-- b000519 | prose | pages [16] -->
From the analysis confidence of each data point, after integrating the information of space-time, text and image, the analysis confidence of each data point is lower than that of the single-dimension model. But at the same time, the goodness of fit of the three-dimensional comprehensive model is more than 80%, which indicates

<!-- b000520 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000521 | prose | pages [16] -->
that after considering all aspects of data factors, according to the amount of information that each report can give, the confidence based on its total effective information is given, which is more reliable than the single-dimension model. This result verifies the correctness of the model.

<!-- b000522 | prose | pages [16] -->
Then, we use the total unverified data after data preprocessing to predict the correct and wrong eyewitness reports, and get the existing data distribution of different categories and the prediction classification distribution for unverified as follows:

<!-- b000523 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000524 | furniture | pages [16] -->


<!-- b000525 | prose | pages [16] -->
Fig.5-7     Existing Data Distribution and Prediction Classification Distribution for Unverified

<!-- b000526 | prose | pages [16] -->
Among them, due to too many data, the confidence level of prediction classification of some data is as follows:

<!-- b000527 | prose | pages [16] -->
Table.5-5         Prediction Classification and Confidence of Some Unverified Data

<!-- b000528 | prose | pages [16] -->
Classification

<!-- b000529 | prose | pages [16] -->
Classification

<!-- b000530 | prose | pages [16] -->
Unverified_data

<!-- b000531 | heading | pages [16] -->
Results

<!-- b000532 | prose | pages [16] -->
Confidence

<!-- b000533 | prose | pages [16] -->
0.836039 data_1 negative-ID 0.826574 data_2 negative-ID 0.820433 data_3 negative-ID 0.808652 data_4 negative-ID 0.80664 data_13 negative-ID 0.787758 data_14 negative-ID

<!-- b000534 | prose | pages [16] -->
Classification

<!-- b000535 | prose | pages [16] -->
Classification

<!-- b000536 | prose | pages [16] -->
Unverified_data

<!-- b000537 | heading | pages [16] -->
Results

<!-- b000538 | prose | pages [16] -->
Confidence 0.785515 data_1 negative-ID 0.782773 data_2 negative-ID 0.785515 data_3 negative-ID 0.80851 data_4 positive-ID 0.882065 data_13 positive-ID 0.901519 data_14 positive-ID According to the prediction results of the model, we draw the distribution map of possible "positive ID". After our manual verification, we find that two prediction points(circled in the picture Fig.5-7) deviate from the rest of the centralized distribution area. Given this abnormal situation, we find the picture and text information of the two abnormal data according to the effective data set:

<!-- b000539 | prose | pages [16] -->
Unverified_data Number of words

<!-- b000540 | prose | pages [16] -->
Abnormal_data_1 20

<!-- b000541 | furniture | pages [16] -->


<!-- b000542 | prose | pages [16] -->
Unverified_data Number of words

<!-- b000543 | prose | pages [16] -->
Abnormal_data_2 54 Table.5-6      Abnormal Data Text Information

<!-- b000544 | furniture | pages [16] -->


<!-- b000545 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000546 | furniture | pages [16] -->
关注数学模型

<!-- b000547 | furniture | pages [16] -->
2

<!-- b000548 | furniture | pages [16] -->
MATHmodels

<!-- b000549 | furniture | pages [16] -->
获取更多资讯

<!-- b000550 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000551 | furniture | pages [17] -->
Team # 2107815                                                                 Page 17 of 25

<!-- b000552 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000553 | furniture | pages [17] -->


<!-- b000554 | furniture | pages [17] -->


<!-- b000555 | prose | pages [17] -->
Fig.5-8     Abnormal_Data_1                          Fig.5-9      Abnormal_Data_2 The prediction classification confidence of the two abnormal data is as follows:

<!-- b000556 | prose | pages [17] -->
Classification

<!-- b000557 | prose | pages [17] -->
Unverified_data Classification

<!-- b000558 | prose | pages [17] -->
Confidence

<!-- b000559 | heading | pages [17] -->
Results

<!-- b000560 | prose | pages [17] -->
Space_Time

<!-- b000561 | prose | pages [17] -->
Abnormal_data_1 positive-ID 0.164281 Abnormal_data_2 positive-ID 0.179588

<!-- b000562 | prose | pages [17] -->
Classification

<!-- b000563 | prose | pages [17] -->
Classification

<!-- b000564 | prose | pages [17] -->
Classification

<!-- b000565 | prose | pages [17] -->
Confidence

<!-- b000566 | prose | pages [17] -->
Confidence

<!-- b000567 | prose | pages [17] -->
Confidence

<!-- b000568 | prose | pages [17] -->
Text

<!-- b000569 | prose | pages [17] -->
Image

<!-- b000570 | prose | pages [17] -->
0.873577 0.994101 0.543034 0.954202 0.890325 0.55412 Table.5-7   Abnormal Data Classification Confidence Level

<!-- b000571 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000572 | prose | pages [17] -->
Based on the above data, we can analyze the reasons for the anomalies: because the reporter's text description is more, the credibility of the text model prediction results is reduced; because the main part of the picture is not clear enough, the credibility of the image recognition model prediction results is reduced. This kind of phenomenon also proves that the comprehensive model is more reliable than the single dimension model.

<!-- b000573 | prose | pages [17] -->
It can be seen that the predicted classification results of the unverified data are relatively consistent with the original manually verified classification data in the temporal and spatial distribution of the data, so it can be considered that the prediction of the model has certain reliability. At the same time, the model gives the confidence of each prediction classification, which provides a reference for researchers to analyze the priority of processing reports, which will be described in detail below.

<!-- b000574 | heading | pages [17] -->
5.6    The Analyze of The Priority of The Investigation

<!-- b000575 | prose | pages [17] -->
In 5.5, we fitted our model, and used the total Unverified data obtained after data preprocessing to predict correct and false witness reports, and obtained the existing data distributions of different categories and the predicted classification for Unverified distributed.

<!-- b000576 | prose | pages [17] -->
For government departments, when there are multiple positive sighting reports, they need to prioritize the targets with high positive probability. Therefore, it is necessary to prioritize the collected sighting reports.

<!-- b000577 | prose | pages [17] -->
Here we define that the priority levels are divided into S, A, B, C, D, E 6 levels according to accuracy, and the corresponding accuracy rates are 100%~90%, 90%~80%, 70%~70%, 70%-60%, 60%-50% and below 50%. As shown in the following table:

<!-- b000578 | prose | pages [17] -->
Table.5-8       Priority Level Level S A Classification B C D E

<!-- b000579 | prose | pages [17] -->
Below 80%~70% 100%~90% 90%~80% Confidence 70%~60% 60%~50%

<!-- b000580 | prose | pages [17] -->
50% The data detected as positive in Unverified and their Classification Confidence are listed in the following table:

<!-- b000581 | prose | pages [17] -->
Unverified_data Classification

<!-- b000582 | prose | pages [17] -->
Unverified_data Classification

<!-- b000583 | prose | pages [17] -->
Classification

<!-- b000584 | heading | pages [17] -->
Results

<!-- b000585 | prose | pages [17] -->
Confidence

<!-- b000586 | prose | pages [17] -->
data_1 positive-ID 0.507015 data_2 positive-ID 0.539997 data_3 positive-ID 0.543034 data_4 positive-ID 0.55412

<!-- b000587 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000588 | furniture | pages [17] -->
data_5

<!-- b000589 | furniture | pages [17] -->
positive-ID

<!-- b000590 | furniture | pages [17] -->
0.573099

<!-- b000591 | prose | pages [17] -->
Classification

<!-- b000592 | heading | pages [17] -->
Results

<!-- b000593 | prose | pages [17] -->
Confidence data_10 positive-ID 0.705296 data_11 positive-ID 0.741258 data_12 positive-ID 0.766886 data_13 positive-ID 0.780861

<!-- b000594 | furniture | pages [17] -->
关注数学模型

<!-- b000595 | furniture | pages [17] -->
data_14

<!-- b000596 | furniture | pages [17] -->
positive-ID

<!-- b000597 | furniture | pages [17] -->
0.781631

<!-- b000598 | furniture | pages [17] -->
2

<!-- b000599 | furniture | pages [17] -->
MATHmodels

<!-- b000600 | furniture | pages [17] -->
获取更多资讯

<!-- b000601 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000602 | furniture | pages [18] -->
Team # 2107815                                                                 Page 18 of 25

<!-- b000603 | furniture | pages [18] -->
data_6

<!-- b000604 | furniture | pages [18] -->
positive-ID

<!-- b000605 | furniture | pages [18] -->
0.596436

<!-- b000606 | prose | pages [18] -->
data_7 positive-ID 0.646236 data_8 positive-ID 0.647331 data_9 positive-ID 0.70002

<!-- b000607 | furniture | pages [18] -->
data_15

<!-- b000608 | furniture | pages [18] -->
positive-ID

<!-- b000609 | furniture | pages [18] -->
0.80851

<!-- b000610 | prose | pages [18] -->
data_16 positive-ID 0.882065 data_17 positive-ID 0.901519

<!-- b000611 | furniture | pages [18] -->


<!-- b000612 | furniture | pages [18] -->


<!-- b000613 | furniture | pages [18] -->


<!-- b000614 | prose | pages [18] -->
Table.5-9

<!-- b000615 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000616 | prose | pages [18] -->
The 17 data are counted in priority levels, as shown in the following figure:

<!-- b000617 | prose | pages [18] -->
7 6 5 4 3 2 1 0

<!-- b000618 | prose | pages [18] -->
E D C B A S

<!-- b000619 | furniture | pages [18] -->


<!-- b000620 | prose | pages [18] -->
Fig.5-10 As you can see, there is one S-level, which should be the highest priority to be investigated. In the Unverified prediction classification distribution in 5.5, two unverified_predict_ID points are far away from the positive-ID

<!-- b000621 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000622 | prose | pages [18] -->
point, and the probability of being positive should be relatively low. After querying, it can be known that the priority level corresponding to these two points is D level, which is in line with the result.

<!-- b000623 | heading | pages [18] -->
6    Update Method and Update Frequency

<!-- b000624 | heading | pages [18] -->
6.1    Method construction and frequency determination

<!-- b000625 | prose | pages [18] -->
Over time, there may be new sighting reports of wasps. The existence of new reports may affect the accuracy of the model's predictions. Therefore, when a new sighting report appears, it should be judged whether the report will affect the existing model, and if it does, update the report.

<!-- b000626 | prose | pages [18] -->
In the data given in the title, there are 14 positive-IDs. The specific locations of these 14 positive-IDs have been marked down in Washington State. The appearance time of positive-IDs changes in order, and we record the first positive-ID in the data as the starting point O. At the same time, in the remaining 13 positive-IDs, the point farthest from the starting point is marked as point P. The distance between point O and point P is denoted as 𝑆𝑙𝑎𝑠𝑡. When a new positive-ID appears, this positive-ID will have a distance deviation from the starting point, which is counted as 𝑆𝑛𝑒𝑤.

<!-- b000627 | prose | pages [18] -->
The update method we use is the incremental update method of the model based on the forgetting factor. This update method is to set a forgetting factor that decays over time to decay the weight of the model vector, or to decay the weight of the text vector used to create the model.

<!-- b000628 | prose | pages [18] -->
In the process of model learning, when new data is added, some old data may not have that great influence on the model's fitting effect. The amount of information provided by the new data gradually weakens the old data. In order to prevent data saturation, we introduce the concept of forgetting factor to allow the model to properly forget part of the old data while accepting new data. The value of the forgetting factor is set to λ, as shown below:

<!-- b000629 | prose | pages [18] -->
0, 𝑆𝑛𝑒𝑤≤𝑆𝑙𝑎𝑠𝑡

<!-- b000630 | prose | pages [18] -->
λ = {

<!-- b000631 | prose | pages [18] -->
𝑆𝑙𝑎𝑠𝑡 𝑆𝑛𝑒𝑤)2

<!-- b000632 | prose | pages [18] -->
−(1−

<!-- b000633 | furniture | pages [18] -->


<!-- b000634 | furniture | pages [18] -->


<!-- b000635 | furniture | pages [18] -->


<!-- b000636 | prose | pages [18] -->
(Eq. 6-1)

<!-- b000637 | prose | pages [18] -->
, 𝑆𝑛𝑒𝑤> 𝑆𝑙𝑎𝑠𝑡

<!-- b000638 | prose | pages [18] -->
1 −e

<!-- b000639 | prose | pages [18] -->
In this formula, taking into account the model we have established, if the new positive-ID 𝑆𝑛𝑒𝑤≤𝑆𝑙𝑎𝑠𝑡. , We think that this positive-ID is the target in the existing hive, so the value of the forgetting factor λ is 0. If 𝑆𝑛𝑒𝑤> 𝑆𝑙𝑎𝑠𝑡 of the new positive-ID appears, then there may be a phenomenon of diffusion. At this time, set the forgetting

<!-- b000640 | prose | pages [18] -->
𝑆𝑙𝑎𝑠𝑡 𝑆𝑛𝑒𝑤)2

<!-- b000641 | prose | pages [18] -->
−(1−

<!-- b000642 | prose | pages [18] -->
factor λ = 1 −e

<!-- b000643 | prose | pages [18] -->
. When the value of λ is 0, we believe that there is no need to update the model. Therefore, our update frequency judgment is: when the new positive-ID 𝑆𝑛𝑒𝑤> 𝑆𝑙𝑎𝑠𝑡, we need to update the model.

<!-- b000644 | prose | pages [18] -->
The above-mentioned forgetting factor λ mainly acts on the data of the LDA text classification model and

<!-- b000645 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000646 | furniture | pages [18] -->
关注数学模型

<!-- b000647 | prose | pages [18] -->
the CNN image recognition model in our model. Suppose we have trained the model with existing data. Before

<!-- b000648 | furniture | pages [18] -->
2

<!-- b000649 | furniture | pages [18] -->
MATHmodels

<!-- b000650 | furniture | pages [18] -->
获取更多资讯

<!-- b000651 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000652 | furniture | pages [19] -->
Team # 2107815                                                                 Page 19 of 25

<!-- b000653 | prose | pages [19] -->
the emergence of a positive-IDs, we may receive new negative-IDs data one after another, but the negative-IDs hardly affect the prediction of the model. We will save the new negative-IDs data we received. Assuming that the original data of our LDA text classification model and CNN image recognition model are 𝐷𝐿𝐷𝐴 and 𝐷𝐶𝑁𝑁, when positive-ID appears, we have:

<!-- b000654 | prose | pages [19] -->
′ = 𝐷𝐿𝐷𝐴× (1 −λ)

<!-- b000655 | prose | pages [19] -->
D𝐿𝐷𝐴

<!-- b000656 | furniture | pages [19] -->


<!-- b000657 | furniture | pages [19] -->


<!-- b000658 | prose | pages [19] -->
(Eq. 6-2)

<!-- b000659 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000660 | prose | pages [19] -->
′ = 𝐷𝐶𝑁𝑁× (1 −λ)

<!-- b000661 | prose | pages [19] -->
D𝐶𝑁𝑁

<!-- b000662 | furniture | pages [19] -->


<!-- b000663 | furniture | pages [19] -->


<!-- b000664 | prose | pages [19] -->
(Eq. 6-3) Assuming that the data volume of the new negative-IDs collected at this time is 𝐷𝑛𝑒𝑔, there is

<!-- b000665 | prose | pages [19] -->
𝑛𝑒𝑤= 𝐷𝐿𝐷𝐴× (1 −λ) + 𝐷𝑛𝑒𝑔

<!-- b000666 | prose | pages [19] -->
D𝐿𝐷𝐴

<!-- b000667 | furniture | pages [19] -->


<!-- b000668 | furniture | pages [19] -->


<!-- b000669 | prose | pages [19] -->
(Eq. 6-4)

<!-- b000670 | prose | pages [19] -->
𝑛𝑒𝑤= 𝐷𝐶𝑁𝑁× (1 −λ) + 𝐷𝑛𝑒𝑔

<!-- b000671 | prose | pages [19] -->
D𝐶𝑁𝑁

<!-- b000672 | furniture | pages [19] -->


<!-- b000673 | furniture | pages [19] -->


<!-- b000674 | prose | pages [19] -->
(Eq. 6-5)

<!-- b000675 | prose | pages [19] -->
𝑛𝑒𝑤 as the updated new data, and then use the new data to retrain the LDA text

<!-- b000676 | prose | pages [19] -->
𝑛𝑒𝑤 and w𝐶𝑁𝑁

<!-- b000677 | prose | pages [19] -->
We use D𝐿𝐷𝐴

<!-- b000678 | prose | pages [19] -->
classification model and CNN image recognition model, and then integrate the propagation model into a new model. The flowchart is as Fig. 6-1:

<!-- b000679 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000680 | furniture | pages [19] -->


<!-- b000681 | prose | pages [19] -->
Fig.6-1 Flowchart

<!-- b000682 | heading | pages [19] -->
6.2    Method verification

<!-- b000683 | prose | pages [19] -->
In order to verify whether our method has good correctness, we use the positive-ID and negative-ID that have been manually labeled in the data set to verify the goodness of fit of the model. The following table is the update time node we selected:

<!-- b000684 | prose | pages [19] -->
The following table is the update time node we selected:

<!-- b000685 | prose | pages [19] -->
Table.6-1 Update Time Node Frequency Time radius Forgetting factor September 30, 2019 (discovered) 1

<!-- b000686 | furniture | pages [19] -->


<!-- b000687 | prose | pages [19] -->
2.4401(𝑆𝑙𝑎𝑠𝑡) November 13, 2019 (updated) 2 3 May 15, 2020 (updated) 4 June 7, 2020 (updated) 5 No more updates 3.9742 0.1384372799 7.4248 0.1942510696 7.4381 3.19726×10-6

<!-- b000688 | furniture | pages [19] -->


<!-- b000689 | furniture | pages [19] -->


<!-- b000690 | prose | pages [19] -->
Using the above update nodes and the update method we built, the model is updated and tested, and the testing goodness of fit results and the analysis confidence of each data point are:

<!-- b000691 | prose | pages [19] -->
Table.6-2  Goodness of Fit of Test Data

<!-- b000692 | prose | pages [19] -->
Data Type positive-ID negative-ID

<!-- b000693 | furniture | pages [19] -->


<!-- b000694 | prose | pages [19] -->
Goodness of Fit 92.88% 95.90%

<!-- b000695 | prose | pages [19] -->
Table.6-3     Analysis Confidence of Each Data Point (Positive-ID and Partial Negative-ID Results)

<!-- b000696 | prose | pages [19] -->
positive-

<!-- b000697 | prose | pages [19] -->
Classification

<!-- b000698 | prose | pages [19] -->
Classification

<!-- b000699 | prose | pages [19] -->
ID

<!-- b000700 | heading | pages [19] -->
Results

<!-- b000701 | prose | pages [19] -->
Confidence

<!-- b000702 | prose | pages [19] -->
data_1 positive-ID 0.529977

<!-- b000703 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000704 | furniture | pages [19] -->
data_2

<!-- b000705 | furniture | pages [19] -->
positive-ID

<!-- b000706 | furniture | pages [19] -->
0.678211

<!-- b000707 | prose | pages [19] -->
negative-

<!-- b000708 | prose | pages [19] -->
Classification

<!-- b000709 | prose | pages [19] -->
Classification

<!-- b000710 | prose | pages [19] -->
ID

<!-- b000711 | heading | pages [19] -->
Results

<!-- b000712 | prose | pages [19] -->
Confidence data_1 negative-ID 0.931902913 0.959242632 关注数学模型

<!-- b000713 | furniture | pages [19] -->
data_2

<!-- b000714 | prose | pages [19] -->
negative-ID

<!-- b000715 | furniture | pages [19] -->
2

<!-- b000716 | furniture | pages [19] -->
MATHmodels

<!-- b000717 | furniture | pages [19] -->
获取更多资讯

<!-- b000718 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000719 | furniture | pages [20] -->
Team # 2107815                                                                 Page 20 of 25

<!-- b000720 | furniture | pages [20] -->
data_3

<!-- b000721 | furniture | pages [20] -->
positive-ID

<!-- b000722 | furniture | pages [20] -->
0.446543

<!-- b000723 | prose | pages [20] -->
data_4 positive-ID 0.658624 data_5 positive-ID 0.648936 data_6 positive-ID 0.5079 data_7 positive-ID 0.621742

<!-- b000724 | furniture | pages [20] -->
data_3

<!-- b000725 | prose | pages [20] -->
negative-ID

<!-- b000726 | furniture | pages [20] -->
0.816905799

<!-- b000727 | prose | pages [20] -->
data_4 negative-ID 0.95720497 data_5 negative-ID 0.918108949 data_6 negative-ID 0.963946508 data_7 negative-ID 0.96480972

<!-- b000728 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000729 | prose | pages [20] -->
data_8 positive-ID 0.538165 data_9 positive-ID 0.782645 data_10 positive-ID 0.779281 data_11 positive-ID 0.7671 data_12 positive-ID 0.540662 data_13 positive-ID 0.820679 data_14 positive-ID 0.54537

<!-- b000730 | furniture | pages [20] -->


<!-- b000731 | prose | pages [20] -->
data_8 negative-ID 0.762568601 data_9 negative-ID 0.771223866 data_10 negative-ID 0.942466441 data_11 positive-ID 0.955948677 data_12 negative-ID 0.602054031 data_13 negative-ID 0.89882576 data_14 negative-ID 0.92329102

<!-- b000732 | prose | pages [20] -->
From the analysis confidence of each data, after updating the model, the goodness of fit of our model is more than 90%. Compared with before the update, the goodness of fit of the model has increased by about 10%, indicating that after the update, our prediction results for positive-IDs and negative-IDs have been improved, indicating the reliability of the method.

<!-- b000733 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000734 | prose | pages [20] -->
After that, we use the updated model to predict correct and false witness reports on the total Unverified data obtained after data preprocessing, and obtain the existing data distributions of different categories and the predicted classification distributions for Unverified as:

<!-- b000735 | furniture | pages [20] -->


<!-- b000736 | furniture | pages [20] -->


<!-- b000737 | prose | pages [20] -->
Fig.6-2   Data Distribution and Prediction Classification Distribution for Unverified We show the prediction classification confidence of the data after updating the model in the following table:

<!-- b000738 | furniture | pages [20] -->


<!-- b000739 | prose | pages [20] -->
Table.6-4     Partial Unverified Data Prediction Classification and Confidence (After Update)

<!-- b000740 | prose | pages [20] -->
Unverified_data Classification

<!-- b000741 | prose | pages [20] -->
Classification

<!-- b000742 | heading | pages [20] -->
Results

<!-- b000743 | prose | pages [20] -->
Confidence

<!-- b000744 | prose | pages [20] -->
data_1 negative-ID 0.841778 data_2 negative-ID 0.86378 data_3 negative-ID 0.958737 data_4 negative-ID 0.818994 data_13 negative-ID 0.906906 data_14 negative-ID 0.825228

<!-- b000745 | furniture | pages [20] -->


<!-- b000746 | prose | pages [20] -->
Unverified_data Classification

<!-- b000747 | prose | pages [20] -->
Classification

<!-- b000748 | heading | pages [20] -->
Results

<!-- b000749 | prose | pages [20] -->
Confidence data_1 negative-ID 0.888772 data_2 negative-ID 0.94193 data_3 negative-ID 0.917276 data_4 positive-ID 0.893923 data_13 positive-ID 0.915533 data_14 positive-ID 0.909485

<!-- b000750 | prose | pages [20] -->
It can be seen that the predicted classification results for Unverified data are relatively consistent with the original manually verified classification data in the temporal and spatial distribution of the data. This shows that

<!-- b000751 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000752 | prose | pages [20] -->
the prediction of the model has a certain degree of reliability. And compared with the forecast classification

<!-- b000753 | furniture | pages [20] -->
关注数学模型

<!-- b000754 | furniture | pages [20] -->
2

<!-- b000755 | furniture | pages [20] -->
MATHmodels

<!-- b000756 | furniture | pages [20] -->
获取更多资讯

<!-- b000757 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000758 | furniture | pages [21] -->
Team # 2107815                                                                 Page 21 of 25

<!-- b000759 | prose | pages [21] -->
distribution map in 5.5, the lower-left corner of the right figure is missing two more remote positive-ID points, which also reflects that the model has a certain degree of rationality.

<!-- b000760 | furniture | pages [21] -->


<!-- b000761 | heading | pages [21] -->
7    Proof of Eradication

<!-- b000762 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000763 | heading | pages [21] -->
7.1    Data Analysis and Evaluation Standard Establishment

<!-- b000764 | prose | pages [21] -->
In order to prove that this invasive species has been eradicated, we first need to delimit an area affected by the invasion of the Vespa mandarinia. According to the established model, we define a variable 𝑅𝑛𝑜𝑤 representing the distance between the location of the new "positive ID" and the starting point. Now, take the starting point as the center, draw a circle for the radius 𝑅𝑛𝑜𝑤, which is the area affected by the invasion of Vespa mandarinia. 𝑅𝑛𝑜𝑤 will continue to adjust with the new "positive ID" to ensure that our designated area can fully cover the area affected by the invasion of Vespa mandarinia. According to the existing "positive ID" data, we can get the following images:

<!-- b000765 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000766 | furniture | pages [21] -->


<!-- b000767 | prose | pages [21] -->
Fig.7- 1 “Positive ID” Curve along with the Time     Fig.7-2   𝑅𝑛𝑜𝑤Curve along with Time

<!-- b000768 | prose | pages [21] -->
According to the living habits of C. sinensis, the breeding peak is from May to October every year: And its growth cycle (from egg to adult) is 𝑡 = 25 days[2], so we set a time threshold  𝑇= 3 × 𝑡=75 days. If the value of 𝑅𝑛𝑜𝑤 does not change, then the integrated model will not be updated according to the updated rules of the integrated model established by us, which indicates that the influence scope of the invasion event of the Wasp has not spread; if the "positive" is added in the delimited area, it can be concluded that If the number of "Id" eyewitness reports is always 0 within a time threshold T, it can be used as direct evidence that the Vespa mandarinia has been eradicated in this area.

<!-- b000769 | prose | pages [21] -->
According to the above inference, we set up an evaluation standard when the following conditions are met: ⚫ Condition 1: between May and October in a year. ⚫ Condition 2: on the premise of satisfying condition 1, 𝑅𝑛𝑜𝑤 does not change within a time threshold  𝑇. ⚫ Condition 3: on the premise of meeting conditions 1 and 2, the number of new "positive ID" eyewitness

<!-- b000770 | prose | pages [21] -->
reports in the delimited area is always 0 within a time threshold 𝑇. It can be considered that the invasive species of Vespa mandarinia has been eradicated in relevant areas of Washington state.

<!-- b000771 | heading | pages [21] -->
7.2    Evaluation Standard Demonstration and Development Trend Prediction

<!-- b000772 | prose | pages [21] -->
According to the evaluation criteria established by us, combined with the above two images, we need to do the following work:

<!-- b000773 | prose | pages [21] -->
⚫ Analyze the data in 2019 as known data, and judge the correctness and rationality of the evaluation

<!-- b000774 | prose | pages [21] -->
standard based on the data in 2020. ⚫ And then analyze the data in 2020 as known data to predict the development trend in 2021.

<!-- b000775 | prose | pages [21] -->
Between May and October in 2019, 𝑅𝑛𝑜𝑤 does not remain unchanged within a complete time threshold 𝑇, only meets the evaluation standard condition 1, but does not meet the evaluation standard condition 2. Therefore, it can be determined that the Vespa mandarinia has not been eradicated in Washington state in 2019. According

<!-- b000776 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000777 | furniture | pages [21] -->
关注数学模型

<!-- b000778 | furniture | pages [21] -->
2

<!-- b000779 | furniture | pages [21] -->
MATHmodels

<!-- b000780 | furniture | pages [21] -->
获取更多资讯

<!-- b000781 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000782 | furniture | pages [22] -->
Team # 2107815                                                                 Page 22 of 25

<!-- b000783 | prose | pages [22] -->
to its living habits and population reproduction rules, it can be inferred that the impact scope of the invasion of Vespa mandarinia will increase in 2020, and its population number will increase The quantity will increase. Combined with the data of 2020, we can verify the correctness and rationality of our evaluation criteria.

<!-- b000784 | prose | pages [22] -->
Between May and October 2020, 𝑅𝑛𝑜𝑤 remains unchanged from April to July, but the number of new "positive ID" eyewitness reports in the delimited area does not remain unchanged within a time threshold 𝑇,

<!-- b000785 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000786 | prose | pages [22] -->
which meets condition 1 and condition 2 but does not meet condition 3. Therefore, we speculate that in July 2020, Vespa mandarinia will not be eradicated in Washington state; 𝑅𝑛𝑜𝑤 remains unchanged from July to October, but the number of newly added "positive ID" eyewitness reports in the delimited area does not remain unchanged within a time threshold 𝑇, "positive ID" The decrease in the number of " positive ID " eyewitness reports is due to the natural factors of cold weather. Condition 1 and condition 2 are met, but condition 3 is not met. Therefore, we speculate that in July 2020, the Vespa mandarinia will not be eradicated in Washington state.

<!-- b000787 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000788 | furniture | pages [22] -->


<!-- b000789 | furniture | pages [22] -->


<!-- b000790 | prose | pages [22] -->
Fig.7-3 Distribution range of "positive ID" in 2019        Fig. 7-4 Distribution Scope of "Positive ID" in 2020

<!-- b000791 | prose | pages [22] -->
According to the evaluation criteria, after May 2021, Vespa mandarinia will influence Washington state, but combined with 𝑅𝑛𝑜𝑤 from the curve,  we can find that the growth rate of its influence area is slowing down, which indicates that Washington state has taken positive measures to curb the development of the invasion of the Vespa mandarinia.

<!-- b000792 | heading | pages [22] -->
8    Strengths and Weaknesses

<!-- b000793 | heading | pages [22] -->
8.1    Strengths

<!-- b000794 | prose | pages [22] -->
Strength-1 Comprehensiveness : Our model makes full use of the spatiotemporal data, text and image information in the data set, and extracts the data features from the three-dimensional perspective, which is comprehensive.

<!-- b000795 | prose | pages [22] -->
Strength-2  Accuracy: When the forgetting factor is not added to update the model, the fitting degree of our model to the verified positive and negative data reaches 92.86% and 85.22%, and the fitting degree of the model reaches 95.50% and 92.86% after adding the updated measure. Moreover, the model with updating measures owns the ability of self-correcting. It has good accuracy.

<!-- b000796 | prose | pages [22] -->
Strength-3  Applicability: In the case of no huge climate change, over time, the model can be applied for a long time in the continuous self-renewal and has strong applicability.

<!-- b000797 | prose | pages [22] -->
Strength-4  Innovative: Our model can analyze and forecast the updated report in three dimensions, which is innovative.

<!-- b000798 | heading | pages [22] -->
8.2    Weaknesses

<!-- b000799 | prose | pages [22] -->
Weakness-1  Time consuming: Due to the combination of deep learning image processing model in 3D comprehensive analysis model, the model needs to be retrained every time the model is updated, which takes a certain amount of time. However, once the update is completed, the model can be used for a long time. So the influence of time cost is relatively small.

<!-- b000800 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000801 | furniture | pages [22] -->
关注数学模型

<!-- b000802 | furniture | pages [22] -->
2

<!-- b000803 | furniture | pages [22] -->
MATHmodels

<!-- b000804 | furniture | pages [22] -->
获取更多资讯

<!-- b000805 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000806 | furniture | pages [23] -->
Team # 2107815                                                                 Page 23 of 25

<!-- b000807 | prose | pages [23] -->
Weakness-2  Lack of human factor analysis: Due to the lack of description of human intervention factors in the data set, the model can not effectively analyze these factors.

<!-- b000808 | heading | pages [23] -->
9    Conclusion

<!-- b000809 | prose | pages [23] -->
Asian giant hornets are called the "Murder Hornet" by the media, and its recent appearance in the United

<!-- b000810 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000811 | prose | pages [23] -->
States has attracted national attention. If the wasp’s nest is not destroyed in time, the species invasion of this species will seriously affect the diversity of local species, cause local economic losses, and even casualties. How to predict the spread of wasp in a period time and other information is of great significance and effect to curb its spread.

<!-- b000812 | prose | pages [23] -->
In this project, we have designed a three-dimensional analysis model. This model divides time and space, text and image information into three dimensions, and considers the final analysis results based on the effective information weight of each dimension. Spatio-temporal corresponds to the propagation model, text corresponds to the LDA model, and image corresponds to the CNN model. We use the established model to process the given data set and the open source data set collected on the Internet. It turns out the results has a high accuracy rate, and other information such as the location of the wasp appears reasonably and well-documented.

<!-- b000813 | prose | pages [23] -->
When a new positive sighting report appears, the existing model needs to be updated. We use the method of model increment based on the forgetting factor to update our existing data set. After being tested, it proves

<!-- b000814 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000815 | prose | pages [23] -->
that this method has a high degree of classification confidence.

<!-- b000816 | prose | pages [23] -->
Finally, we set a set of evaluation criteria to determine whether this pest has died out in Washington State.

<!-- b000817 | heading | pages [23] -->
10    Reference

<!-- b000818 | prose | pages [23] -->
[1] http://www.gscloud.cn/ [2] https://baike.baidu.com/ [3] GuoFa Zhou. Study on The Growth Diffusion Model of Insect Population [J].JOURNAL OF BIOMATHEMATICS，1996，11（4）：172-175

<!-- b000819 | prose | pages [23] -->
[4] https://zhuanlan.zhihu.com/p/106009940 [5] https://blog.csdn.net/u014248127/article/details/80774668 [6]https://baike.baidu.com/item/%E5%8D%B7%E7%A7%AF%E7%A5%9E%E7%BB%8F%E7%BD%9 1%E7%BB%9C/17541100?fr=aladdin [7] https://www.kaggle.com/jerzydziewierz/bee-vs-wasp

<!-- b000820 | furniture | pages [23] -->


<!-- b000821 | furniture | pages [23] -->


<!-- b000822 | furniture | pages [23] -->


<!-- b000823 | furniture | pages [23] -->


<!-- b000824 | furniture | pages [23] -->


<!-- b000825 | furniture | pages [23] -->


<!-- b000826 | furniture | pages [23] -->


<!-- b000827 | furniture | pages [23] -->


<!-- b000828 | furniture | pages [23] -->


<!-- b000829 | furniture | pages [23] -->


<!-- b000830 | furniture | pages [23] -->


<!-- b000831 | furniture | pages [23] -->


<!-- b000832 | furniture | pages [23] -->


<!-- b000833 | furniture | pages [23] -->


<!-- b000834 | furniture | pages [23] -->


<!-- b000835 | furniture | pages [23] -->


<!-- b000836 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000837 | furniture | pages [23] -->
关注数学模型

<!-- b000838 | furniture | pages [23] -->
2

<!-- b000839 | furniture | pages [23] -->
MATHmodels

<!-- b000840 | furniture | pages [23] -->
获取更多资讯

<!-- b000841 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000842 | furniture | pages [24] -->
Team # 2107815                                                                 Page 24 of 25

<!-- b000843 | heading | pages [24] -->
Memo

<!-- b000844 | prose | pages [24] -->
To：The Washington State Department of Agriculture From: Team #2107815

<!-- b000845 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000846 | prose | pages [24] -->
Date: February 8, 2020 Subject: The Analysis of Public Reports and Strategies for Additional Investigation

<!-- b000847 | furniture | pages [24] -->


<!-- b000848 | prose | pages [24] -->
The Vespa mandarinia is the largest wasp species in the world. Since they are predators of European bees, their invasion may have a devastating impact on European bees in a short time. Besides, they are also agricultural pests. After the sighting in September 2019, the invasion of the Vespa mandarinia also attracted the attention of Washington state. Although, the Washington state has established a website for the public to report possible Bumblebee sightings, the situation of wasp invasion has not been fundamentally improved. How to deal with a large number of eyewitness reports with limited national resources has become an urgent problem.

<!-- b000849 | prose | pages [24] -->
Based on this, our team used the data provided to analyze the information reflected by the data. At the same time, a three-dimensional comprehensive data analysis and prediction model was established on the basis of using the biological characteristics and the data provided by the title, which could comprehensively utilize the

<!-- b000850 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000851 | prose | pages [24] -->
spatiotemporal data, comment description text and image information in the eyewitness report. Our team introduced the forgetting factor to establish an effective incremental updating method for the model. In the test of the existing data with the complete model, our model reaches a considerable accuracy: 92.88% (positive ID) and 95.90% (negative ID).

<!-- b000852 | heading | pages [24] -->
Result:

<!-- b000853 | prose | pages [24] -->
Based on the modeling and analysis of the data, we got the following results: (1) Most of the correct eyewitness reports of the Vespa mandarinia occur in month from June to October every year and there are two peaks in May and September. The reason is that there are two breeding peak of wasps before this two months, one is from April to May, the other is from August to September. During these months, not only increases the activity of wasps but also expands the activity of wasps at the same time. Moreover, the occurrence locations of correct sighting reports are relatively concentrated, which indicates that the spatial and temporal distribution of correct sighting reports should be relatively concentrated in a certain event segment due to the limitation of wasp population propagation distance.

<!-- b000854 | prose | pages [24] -->
(2) On the basis of the above conclusion, we first use the verified data to update and train the model incrementally, and then use the completed model to predict the data that has not been verified manually.

<!-- b000855 | furniture | pages [24] -->


<!-- b000856 | prose | pages [24] -->
Fig.11-1  The classification and Distribution of Forecast Data, and Comparison to the Distribution of

<!-- b000857 | prose | pages [24] -->
Actual Data

<!-- b000858 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000859 | furniture | pages [24] -->


<!-- b000860 | furniture | pages [24] -->
关注数学模型

<!-- b000861 | furniture | pages [24] -->
2

<!-- b000862 | furniture | pages [24] -->
MATHmodels

<!-- b000863 | furniture | pages [24] -->
获取更多资讯

<!-- b000864 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000865 | furniture | pages [25] -->
Team # 2107815                                                                 Page 25 of 25

<!-- b000866 | prose | pages [25] -->
(3) The prediction results Fig.11-1 clearly show that: t Among the data that has not been manually verified, the data that may be reported as correct sightings are still distributed around 48°N, 122°W. At the same time, the model also gives the confidence of each data point that may be correct eyewitness reports of wasps, which establishes the basis for the distribution strategy of investigation resources.

<!-- b000867 | prose | pages [25] -->
Strategies:

<!-- b000868 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000869 | prose | pages [25] -->
Because of  the limited human resources, it is impossible to verify every eyewitness report manually in time. At the same time, the investigation of a large number of actually wrong eyewitness reports can be a great waste of resources, since the correct eyewitness reports only account for about 0.5% of all eyewitness reports. Therefore, we have established a six-level system of priority investigation for the eyewitness reports provided based on the confidence prediction results of the model. With this the six-level system, staff can decide whether to give priority to investigation or give up investigation. The system is shown in the table below:

<!-- b000870 | prose | pages [25] -->
Table.  Priority Level Level S A Classification B C D E

<!-- b000871 | prose | pages [25] -->
Below 80%~70% 100%~90% 90%~80% Confidence

<!-- b000872 | furniture | pages [25] -->


<!-- b000873 | prose | pages [25] -->
70%~60% 60%~50%

<!-- b000874 | prose | pages [25] -->
50%

<!-- b000875 | prose | pages [25] -->
微信号：MATHmodels

<!-- b000876 | prose | pages [25] -->
The six-level system will optimize the resource allocation of laboratory report investigation. Considering the existence of human intervention, we use the model to put forward the evidence to judge whether the population of Vespa mandarinia is eradicated from Washington state.

<!-- b000877 | prose | pages [25] -->
⚫ Condition 1: Between May and October in a year. ⚫ Condition 2: Under the premise of satisfying condition 1, the 𝑅𝑛𝑜𝑤 provided by the model does not

<!-- b000878 | prose | pages [25] -->
change within a time threshold 𝑇. 𝑇 is about 75 days. ⚫ Condition 3: On the premise of meeting conditions 1 and 2, the number of new "positive-ID" eyewitness

<!-- b000879 | prose | pages [25] -->
reports in the delimited area is always 0 within a time threshold 𝑇.

<!-- b000880 | furniture | pages [25] -->


<!-- b000881 | prose | pages [25] -->
In conclusion, based on the analysis using the three-dimensional comprehensive data analysis and prediction model, we provide the following measures for the official classification staff:

<!-- b000882 | prose | pages [25] -->
⚫ Update the report data in the database in time. When updating the data, the model will introduce the

<!-- b000883 | prose | pages [25] -->
incremental updating method of forgetting factor to constantly self revise and optimize, so as to achieve higher analysis and prediction accuracy. ⚫ When a new data report is generated, the staff should determine the priority investigation order of the

<!-- b000884 | prose | pages [25] -->
new report based on the predicted confidence of the correct sighting report given by the model and the six-level priority investigation level, and the lowest-level report can appropriately abandon the investigation. ⚫ Whether or not the wasp has been eradicated in Washington State should be judged based on the above

<!-- b000885 | prose | pages [25] -->
three reference conditions.

<!-- b000886 | furniture | pages [25] -->


<!-- b000887 | furniture | pages [25] -->


<!-- b000888 | prose | pages [25] -->
Yours sincerely,

<!-- b000889 | furniture | pages [25] -->
Team #2107815

<!-- b000890 | furniture | pages [25] -->


<!-- b000891 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000892 | furniture | pages [25] -->
关注数学模型

<!-- b000893 | furniture | pages [25] -->
2

<!-- b000894 | furniture | pages [25] -->
MATHmodels

<!-- b000895 | furniture | pages [25] -->
获取更多资讯
