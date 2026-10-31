# P-C-2021-2107870-8021b684

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | title | pages [1] -->
C

<!-- b000003 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | furniture | pages [1] -->
2021

<!-- b000006 | furniture | pages [1] -->
2107870

<!-- b000007 | prose | pages [1] -->
MCM/ICM

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | prose | pages [1] -->
Swarming with Data: Prioritizing Sightings of Vespa Mandarinia with Semi-Supervised

<!-- b000010 | prose | pages [1] -->
Learning

<!-- b000011 | prose | pages [1] -->
Vespa mandarinia has been a highly discussed, invasive species since their non-native introduction to

<!-- b000012 | title | pages [1] -->
微信公众号：数学模型

<!-- b000013 | prose | pages [1] -->
the State of Washington. Vespa mandarinia are known to decimate honey bees, while the bees native to North America have no defense mechanisms against their attack.11 The Washington State Department of Agriculture (WSDA) made a call for public submissions of Vespa mandarinia sightings to address the disruption this invasive species could cause. This led to a swarm of data sent their way.

<!-- b000014 | prose | pages [1] -->
We developed a model that assigns a probability of misclassiﬁcation as Vespa mandarinia to each civilian sighting used to prioritize WSDA investigations. Our model consists of two tracks through which the data is fed and analyzed: image analysis and notes/detection date analysis.

<!-- b000015 | prose | pages [1] -->
The image analysis track implements a Semi-Supervised Machine Learning algorithm by estimat- ing PositiveID or NegativeID labels for Unveriﬁed or Unprocessed images using K-Means Clustering. These images and labels alongside the pre-labeled images (given as PositiveID or NegativeID) are used to train a Convolutional Neural Network. The network produces a mapping of GlobalIDs to probabilities of the sighting being positive for Vespa mandarinia.

<!-- b000016 | title | pages [1] -->
微信号：MATHmodels

<!-- b000017 | prose | pages [1] -->
The notes/detection date track implements Semantic Analysis by identifying key phrases in the notes that indicate a sighting is either more or less likely to be Vespa mandarinia. Some of the key phrases are dependent on the detection date; this means the probability of a sighting being a PositiveID increases when a particular phrase is found during one time of year and decreases for another time of year. This time dependency is based on the life-cycle of Vespa mandarinia. This track also produces a mapping of GlobalIDs to probabilities of each sighting being positive for Vespa mandarinia.

<!-- b000018 | prose | pages [1] -->
These two mappings of GlobalIDs to probabilities are uniﬁed into a singular metric for the prob- ability of a misclassiﬁcation (NegativeID for Vespa mandarinia). This is executed by deriving the probability of true negative classiﬁcation for each of the two tracks. Spatial bounds for unlikely citings of Vespa mandarinia are then used to adjust the ﬁnal deliverable: a mapping of GlobalIDs to probability of misclassiﬁcation. The mapping is then used to create intervals of high, medium, and low priority of investigation based upon the mean and standard deviation of the probabilities assigned to the respective NegativeID and PositiveID sightings.

<!-- b000019 | prose | pages [1] -->
We discuss a potential Reaction-Diﬀusion Model to demonstrate how the pest could spread over time; however, we ﬁnd that the current data given by the problem is insuﬃcient to properly model the Spatial Species Spread. Implementation of this model should reﬂect the precision of similar models in past literature.

<!-- b000020 | prose | pages [1] -->
With PositiveID data and the addition of climate data, we can update our model to better incorporate the Spatial Species Spread. The model should be updated every Vespa mandarinia seasonal cycle (annually) to evaluate spread.

<!-- b000021 | prose | pages [1] -->
Based upon our model, the eradication of Vespa mandarinia is conservatively evidenced by all probabilities of sightings being in the low priority interval within 30km of the known pest locations of the last 2 seasonal cycles.

<!-- b000022 | prose | pages [1] -->
Our model is unique in that it uses Semi-Supervised Learning techniques to account for the small amount of data on PositiveID sightings of Vespa mandarinia. This is an approach we have yet to see in the pre-existing literature on insect classiﬁcation using Machine Learning. This allows us to provide accurate standards for how WSDA can allocate its resources for maximum species containment.

<!-- b000023 | prose | pages [1] -->
Key Terms: Semi-Supervised Learning, K-Means Clustering, Convolutional Neural Network, Semantic Analysis, Spatial Species Spread, Reaction-Diﬀusion Model

<!-- b000024 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000025 | furniture | pages [1] -->
关注数学模型

<!-- b000026 | furniture | pages [1] -->
2

<!-- b000027 | furniture | pages [1] -->
MATHmodels

<!-- b000028 | furniture | pages [1] -->
获取更多资讯

<!-- b000029 | furniture | pages [2] -->
Team 2107870

<!-- b000030 | heading | pages [2] -->
Contents

<!-- b000031 | contents | pages [2] -->
1

<!-- b000032 | heading | pages [2] -->
Introduction

<!-- b000033 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000034 | prose | pages [2] -->
1 Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 1

<!-- b000035 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000036 | prose | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 1 Our Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 1 Data Cleaning/Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000037 | prose | pages [2] -->
2

<!-- b000038 | heading | pages [2] -->
Assumptions and Nomenclature

<!-- b000039 | prose | pages [2] -->
2

<!-- b000040 | prose | pages [2] -->
3 Photo/Video Submission of Reported Insect . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 Distinctive Features of Vespa mandarinia versus Look-alike Species 2.2 . . . . . . . . . .

<!-- b000041 | prose | pages [2] -->
4 Location and Life Cycle of Vespa mandarinia . . . . . . . . . . . . . . . . . . . . . . 2.3 5 Probability of Misclassiﬁcation with Zero Information 2.4

<!-- b000042 | prose | pages [2] -->
3 Image Classiﬁcation

<!-- b000043 | prose | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000044 | prose | pages [2] -->
5

<!-- b000045 | prose | pages [2] -->
5 K-Means Clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 6

<!-- b000046 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000047 | prose | pages [2] -->
Convolutional Neural Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000048 | prose | pages [2] -->
4 Semantics Analysis

<!-- b000049 | prose | pages [2] -->
5 Spatial and Temporal Pest Spread Analysis

<!-- b000050 | prose | pages [2] -->
6

<!-- b000051 | heading | pages [2] -->
Model Uniﬁcation Equation

<!-- b000052 | prose | pages [2] -->
7

<!-- b000053 | heading | pages [2] -->
Results and Discussion

<!-- b000054 | prose | pages [2] -->
8

<!-- b000055 | prose | pages [2] -->
11

<!-- b000056 | prose | pages [2] -->
12

<!-- b000057 | prose | pages [2] -->
13

<!-- b000058 | prose | pages [2] -->
14 Discussion of Spread Over Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 14 Results of Sighting Classiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 14 Prioritizing Investigation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3 15 Evidence for Eradication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.4

<!-- b000059 | prose | pages [2] -->
8

<!-- b000060 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000061 | prose | pages [2] -->
9

<!-- b000062 | heading | pages [2] -->
Model Evaluation

<!-- b000063 | prose | pages [2] -->
17

<!-- b000064 | prose | pages [2] -->
17

<!-- b000065 | prose | pages [2] -->
18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 Strengths 18 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2 19

<!-- b000066 | heading | pages [2] -->
10 Conclusion and Updating the Model for Future Work

<!-- b000067 | prose | pages [2] -->
20

<!-- b000068 | heading | pages [2] -->
11 Memorandum to the Washington State Department of Agriculture

<!-- b000069 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000070 | prose | pages [2] -->
21

<!-- b000071 | furniture | pages [2] -->
关注数学模型

<!-- b000072 | furniture | pages [2] -->
2

<!-- b000073 | furniture | pages [2] -->
MATHmodels

<!-- b000074 | furniture | pages [2] -->
获取更多资讯

<!-- b000075 | furniture | pages [3] -->
Team 2107870

<!-- b000076 | prose | pages [3] -->
1

<!-- b000077 | heading | pages [3] -->
Introduction

<!-- b000078 | prose | pages [3] -->
1.1

<!-- b000079 | heading | pages [3] -->
Problem Restatement

<!-- b000080 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000081 | furniture | pages [3] -->
Page 1 of 23

<!-- b000082 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000083 | prose | pages [3] -->
The discovery of a non-native Vespa mandarinia 2019 nest in Vancouver, B.C., Canada set oﬀalarms in the neighboring state of Washington. The state of Washington instated a program to collect alleged citizen sightings of Vespa mandardia in the form of pictures and textual reports. However, verifying the sightings has become an issue given the massive number of reports submitted and the limited resources of the state. In order to optimize the states allocation of resources, the following paper will:

<!-- b000084 | prose | pages [3] -->
• Model the likelihood of a mistaken classiﬁcation using the citizen sighting reports

<!-- b000085 | prose | pages [3] -->
• Discuss the use of our model to prioritize investigation of sightings most likely to be positive sightings

<!-- b000086 | prose | pages [3] -->
• Discuss to what precision the spread of this pest can be predicted over time given the sightings

<!-- b000087 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000088 | prose | pages [3] -->
and describe what would constitute evidence of Vespa mandarinia eradication in the State of Washington

<!-- b000089 | prose | pages [3] -->
• Assess the ability and need to update our model given new data over time

<!-- b000090 | prose | pages [3] -->
1.2 Literature Review

<!-- b000091 | prose | pages [3] -->
The spread of a related species of Asian hornet (Vespa velutina) in Europe in 2004 has been studied using various methods. A study was done modeling the invasion in France using veriﬁed nest sightings over the span of 2004 to 2009. They used a Reaction-Diﬀusion model to describe the population growth and spread throughout the districts of France.15 The information collected from this research was used to create a simulation of the potential invasiveness of Vespa velutina into Great Britian.10 In addition to conﬁrmed sightings, both papers utilized climate data to enhance their predictions.

<!-- b000092 | prose | pages [3] -->
Supervised machine learning techniques have successfully been applied by Kasinathan et.

<!-- b000093 | prose | pages [3] -->
al to classify insect images.9 Supervised learning is characterized by training a model to classiﬁed (or la- beled) training data.4 This approach is less applicable in this problem, given the majority of data points are unlabeled. A common approach to handling limited amounts of labeled data is semi-supervised learning: machine learning models that self-cluster classiﬁcations and feed the estimated labels (as Pos- itiveID or NegativeID) alongside the known labels into a supervised learning algorithm.4,13 Therefore, semi-supervised learning can be applied to the problem of insect image classiﬁcation. This technique can improve upon the pre-existing insect classiﬁcation works by rectifying a common issues: labeling data is expensive.4

<!-- b000094 | prose | pages [3] -->
1.3 Our Model

<!-- b000095 | prose | pages [3] -->
The objective of our model is to produce a probability to GlobalID Mapping for the probability that the given sighting (corresponding to the GlobalID) was misclassiﬁed as Vespa mandarinia. From there, we perform an analysis of probabilities associated with Positive IDs and Negative IDs to produce intervals corresponding to high, medium, and low priority for further investigation.

<!-- b000096 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000097 | furniture | pages [3] -->
关注数学模型

<!-- b000098 | furniture | pages [3] -->
2

<!-- b000099 | furniture | pages [3] -->
MATHmodels

<!-- b000100 | furniture | pages [3] -->
获取更多资讯

<!-- b000101 | furniture | pages [4] -->
Team 2107870

<!-- b000102 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000103 | furniture | pages [4] -->
Page 2 of 23

<!-- b000104 | prose | pages [4] -->
The overall probability to GlobalID mapping is produced by three contributing mappings of probability to GlobalID corresponding to three tracks: Image Classiﬁcation, Semantic Analysis, and Spatial Pest Spread Analysis. Each of these three tracks operates on diﬀerent input types (e.g. images, notes, dates, and spatial

<!-- b000105 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000106 | prose | pages [4] -->
location) to produce their own probability to GlobalID mapping and a probability corresponding to the probability of a true negative identiﬁcation. These two inputs are run through the Model Uniﬁcation Equation to produce the generalized probability to GlobalID mapping that as mentioned above is used to prioritize investigation.

<!-- b000107 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000108 | caption | pages [4] -->
Figure 1: Model Activity Diagram-made using LucidChart

<!-- b000109 | prose | pages [4] -->
1.4 Data Cleaning/Preprocessing

<!-- b000110 | prose | pages [4] -->
The provided data included reported sightings given a unique GlobalID, Detection Date, Notes (from reporter of bug), Lab Status (i.e. Positive ID, Negative ID, Unprocessed, or Unveriﬁed), Lab Comments, Submission Date, Latitude of Sighting, and Longitude of Sighting. The Global IDs were often matched to provided photo or video ﬁles of the insect in question.

<!-- b000111 | heading | pages [4] -->
1. Video and Image Data Cleaning/Prepossessing: The video and image data set was parsed into

<!-- b000112 | prose | pages [4] -->
3 groupings: positive (corresponding to Positive IDs), negative (corresponding to Negative IDs), and unlabeled (corresponding to Unveriﬁed or Unprocessed Lab Status). Initially, we examined the videos and took screenshots of the insect in question resulting in data only consisting of still images. We also transformed all ﬁle types to JPEG ﬁle formats. All of the images were resized to be of size 224x224, and each pixel was divided by 255 to shift the values of the pixels into

<!-- b000113 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000114 | furniture | pages [4] -->
关注数学模型

<!-- b000115 | furniture | pages [4] -->
2

<!-- b000116 | furniture | pages [4] -->
MATHmodels

<!-- b000117 | furniture | pages [4] -->
获取更多资讯

<!-- b000118 | furniture | pages [5] -->
Team 2107870

<!-- b000119 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000120 | furniture | pages [5] -->
Page 3 of 23

<!-- b000121 | prose | pages [5] -->
the range [0,1]. From there, the processing of the classes of image data diverged based on which was being fed into the K-Means Clustering and/or the Convolutional Neural Network:

<!-- b000122 | prose | pages [5] -->
• K-Means Clustering: Unlabeled data was:

<!-- b000123 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000124 | prose | pages [5] -->
(a) ﬁltered by hand (throwing away data that were not images of insects or that were unclear

<!-- b000125 | prose | pages [5] -->
images and zooming into insect when backgrounds were noisy) (b) estimated by eye to determine which we thought were PositiveIDs

<!-- b000126 | prose | pages [5] -->
(c) undersampled majority/reduced sample size of majority, so there were equal amounts

<!-- b000127 | prose | pages [5] -->
of supposed NegativeID images and PositiveID images to reduce the eﬀect of the data majority being NegativeIDs18

<!-- b000128 | prose | pages [5] -->
(d) augmented saturation and value to increase sample size: we added to the set by

<!-- b000129 | prose | pages [5] -->
adjusting the saturation and value (stochastically, so each image was adjusted in the same way as every other image, but this adjustment was not ﬁxed) for each image four times to be within ±50 of their original saturation and value valuesopencv_2020

<!-- b000130 | prose | pages [5] -->
(e) augmented orientation to increase sample size: we then added rotated versions (rotated

<!-- b000131 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000132 | prose | pages [5] -->
by 90, 180, and 270 degrees) of the images to the setopencv_2020

<!-- b000133 | prose | pages [5] -->
(f) ﬂattened images to 1-dimensional arrays and fed this into the k-Means Clustering

<!-- b000134 | prose | pages [5] -->
After, the 푘clusters were formed, all of the unlabeled image data was ﬂattened into 1- dimensional arrays and fed into the k-Means Clustering for the resulting classiﬁcation predictions.

<!-- b000135 | prose | pages [5] -->
• Convolutional Neural Network: The positive images were augmented in eringturation and value with the same method as in the K-Means clustering to increase the sample size of the minority (PositiveIDs)opencv_2020

<!-- b000136 | heading | pages [5] -->
2. Notes/Textual Data Cleaning/Preprocessing: The notes data set was parsed into the same

<!-- b000137 | prose | pages [5] -->
three groupings as the video and image data set: positive, negative and unlabeled. The pairings between Detection Date, Global ID, and Notes were kept in tact. The Detection Date was parsed into month alone. The Notes were transformed into all lower case. After this preprocessing, each individual notes submission was searched for a set of references to key characteristics identifying Vespa mandarin and misconceptions identifying look-alike species.

<!-- b000138 | heading | pages [5] -->
3. Location and Time Data Cleaning/Prepossessing: Data was isolated to the State of Washing-

<!-- b000139 | prose | pages [5] -->
ton’s area, clearing the data point of the 2019 Vancouver nest. Data with missing Detection Date values and date values that can be attributed to civilian submission mistakes were removed. This cleared noise from data reported in the year 1899.

<!-- b000140 | heading | pages [5] -->
Assumptions and Nomenclature

<!-- b000141 | prose | pages [5] -->
2

<!-- b000142 | heading | pages [5] -->
Nomenclature

<!-- b000143 | prose | pages [5] -->
Diﬀusion Coeﬃcient 푘푚2/푦푒푎푟 퐷

<!-- b000144 | prose | pages [5] -->
False Negative: Classiﬁcation of sighting as Negative ID for Vespa mandarinia when the sighting 퐹푁 was actually a Positive Id

<!-- b000145 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000146 | furniture | pages [5] -->
关注数学模型

<!-- b000147 | furniture | pages [5] -->
2

<!-- b000148 | furniture | pages [5] -->
MATHmodels

<!-- b000149 | furniture | pages [5] -->
获取更多资讯

<!-- b000150 | furniture | pages [6] -->
Team 2107870

<!-- b000151 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000152 | furniture | pages [6] -->
Page 4 of 23

<!-- b000153 | prose | pages [6] -->
False Positive: Classiﬁcation of sighting as Positive ID for Vespa mandarinia when the sighting 퐹푃 was actually a Negative Id

<!-- b000154 | prose | pages [6] -->
Carrying Capacity 1/푘푚2 퐾

<!-- b000155 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000156 | prose | pages [6] -->
Mean 휇

<!-- b000157 | prose | pages [6] -->
Nest Density 1/푘푚2 푁

<!-- b000158 | prose | pages [6] -->
푃(퐹푁) Probability of False Negative classiﬁcation

<!-- b000159 | prose | pages [6] -->
푃(퐹푃) Probability of False Positive classiﬁcation

<!-- b000160 | prose | pages [6] -->
푃(푇푁) Probability of True Negative classiﬁcation

<!-- b000161 | prose | pages [6] -->
푃(푇푃) Probability of True Positive classiﬁcation

<!-- b000162 | prose | pages [6] -->
Growth Rate 1/푦푒푎푟 푟

<!-- b000163 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000164 | prose | pages [6] -->
Standard Deviation 휎

<!-- b000165 | prose | pages [6] -->
True Negative: Classiﬁcation of sighting as Negative ID for Vespa mandarinia when the sighting 푇푁 was actually a Negative Id

<!-- b000166 | prose | pages [6] -->
True Positive: Classiﬁcation of sighting as Positive ID for Vespa mandarinia when the sighting 푇푃 was actually a Positive Id

<!-- b000167 | prose | pages [6] -->
Photo/Video Submission of Reported Insect 2.1

<!-- b000168 | prose | pages [6] -->
For the Image Classiﬁcation, we assumed that if a sighting was submitted with a video or photo and that this video or photo was of an insect, that this insect was the insect sighted and that is being In other words, we assumed that the submitted picture or video was not of a diﬀerent reported. insect than the one being reported. This is a reasonable assumption given that most people submit relevant information/images about the sighting. It is a necessary assumption, because the image-based classiﬁcation attempts to model the probability that a submitted insect’s image is Vespa mandarinia.

<!-- b000169 | prose | pages [6] -->
Distinctive Features of Vespa mandarinia versus Look-alike Species 2.2

<!-- b000170 | prose | pages [6] -->
For Semantic Analysis of the Notes Data provided with each submission, we conﬁgured a series of words/phrases that reﬂects the distinguishing features of Vespa mandarinia from other species in the same Genus. The distinguishing words/phrases are references to color, size, and nest qualities of a Vespa mandarinia. Additionally, words/phrases not indicative of Vespa mandarinia that are tell-tale features of look-alike species were conﬁgured to extend the model’s applications of mistaken classiﬁcation of Vespa mandarinia. The key phrases in our Semantics Analysis akin to Vespa mandarinia are: "orange", "brown", "yellow head", "decapitate", "forest"/"wood", "big/giant", "2"/2 inch". The size "2 inch" was chosen because humans have the optical tendency to increase the size of an object based on perspective and shock value. The key phrases akin to look-alike species Vespa crabro (European hornet) and Sphecius speciosus (Eastern cicada killers) are: "dirt", "red", "black head", "orange legs". These assumptions were pulled from the scientiﬁc data presented in the PennState Extension supplement.11

<!-- b000171 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000172 | furniture | pages [6] -->
关注数学模型

<!-- b000173 | furniture | pages [6] -->
2

<!-- b000174 | furniture | pages [6] -->
MATHmodels

<!-- b000175 | furniture | pages [6] -->
获取更多资讯

<!-- b000176 | furniture | pages [7] -->
Team 2107870

<!-- b000177 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000178 | furniture | pages [7] -->
Page 5 of 23

<!-- b000179 | prose | pages [7] -->
Location and Life Cycle of Vespa mandarinia 2.3

<!-- b000180 | prose | pages [7] -->
Based on the DNA analysis showing that the Vancouver specimens and the Washington specimens came from diﬀerent parts of the Asian continent6, we assumed that the initial introduction into the

<!-- b000181 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000182 | prose | pages [7] -->
state of Washington occurred in 2019 and the nest site was located at the mean of the 2019 positive ID hornet sighting points. We also assumed that the spread of Vespa mandarinia came by way of boat along routes into the bay connecting Vancouver and Seattle. This assumption was based oﬀof the locations of the alternate introduction sites. From the Penn State Extension’s Vespa mandarinia nesting cycle, we assumed positive sightings of live hornets and nest would not occur during the winter months, speciﬁcally, November through February.11 Based on entomological observations and data concerning similar hornets, it was also assumed that new nesting sites were bounded below a certain elevation constraint. For this reason we assumed Vespa mandarinia would not spread into or beyond the Cascade mountain range located at 121°W.15

<!-- b000183 | prose | pages [7] -->
Probability of Misclassiﬁcation with Zero Information 2.4

<!-- b000184 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000185 | prose | pages [7] -->
We assumed that when given no information on a sighting, the probability that it is a PositiveID sighting or a NegativeID sighting is equal (50%). This is because without information on a sighting, we can make no reasonable conclusions about whether or not it is actually a sighting of Vespa mandarinia.

<!-- b000186 | prose | pages [7] -->
3 Image Classiﬁcation

<!-- b000187 | prose | pages [7] -->
There are two objectives for the Image Classiﬁcation Track:

<!-- b000188 | prose | pages [7] -->
1. Develop Probability to GlobalID Mapping

<!-- b000189 | prose | pages [7] -->
2. Estimate metric accuracy of this probability assignment,

<!-- b000190 | prose | pages [7] -->
so that the probability for a submission can have its image analyzed, and then this probability will contribute to the overall metric for probability of false classiﬁcation as Vespa mandarinia, while still taking into account the propensity for inaccurate probability assignment in the Image Classiﬁcation track.

<!-- b000191 | prose | pages [7] -->
Each of these two objectives are accompanied by a major challenge:

<!-- b000192 | prose | pages [7] -->
1. Approximately 53.09% of the data is unlabeled (lab status of Unveriﬁed or Unprocessed). There- fore, the classiﬁcation of images as positive or negative with only labeled data greatly reduces the amount of data at our disposal. Predicting the probability of a particular image as a classiﬁcation would be signiﬁcantly less reliable as a result of a less generalized representation of the data learned by the algorithm.

<!-- b000193 | prose | pages [7] -->
2. The likelihood of a Vespa mandarinia sighting is much lower than the likelihood of a misclassi- ﬁcation. We can see from the data that only approximately 0.672% of the labeled (as PositiveID or NegativeID) data is labeled as a positive identiﬁcation. This incentives a learning-based algorithm to assign all images to NegativeID if certain actions to deal with such imbalanced data are not taken. For this same reason, accuracy alone is not a reliable metric of modeling

<!-- b000194 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000195 | furniture | pages [7] -->
关注数学模型

<!-- b000196 | furniture | pages [7] -->
2

<!-- b000197 | furniture | pages [7] -->
MATHmodels

<!-- b000198 | furniture | pages [7] -->
获取更多资讯

<!-- b000199 | furniture | pages [8] -->
Team 2107870

<!-- b000200 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000201 | furniture | pages [8] -->
Page 6 of 23

<!-- b000202 | prose | pages [8] -->
success. A model could guess NegativeID every time but still have a high accuracy, because the negative cases far outweigh the positive cases in population. This would not accomplish the goal of assessing the probability of a particular sighting being a misclassiﬁcation so as to motivate the prioritization of investigation.

<!-- b000203 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000204 | prose | pages [8] -->
We chose to solve the ﬁrst problem by using Semi-Supervised Machine Learning to infer the labels of the unlabeled data via K-Means Clustering (a non-supervised learning algorithm), and then feed these labeled data points (accompanied by the given labeled data points) into the Convolutional Neural Network (a supervised learning algorithm) for binary classiﬁcation. We chose to solve the second problem with the estimation of 푃(푇푃), 푃(푇퐹), 푃(퐹푃), and 푃(퐹푁) in order to accurately represent the "confusion" of the model, which will serve the same purpose as accuracy typically does by capturing the likelihood of a particular classiﬁcation as positive or negative being accurate.5

<!-- b000205 | prose | pages [8] -->
3.1 K-Means Clustering

<!-- b000206 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000207 | prose | pages [8] -->
K-Means Clustering groups data points into 푘clusters by minimizing the the inertia within each cluster, which is deﬁned as written by scikit-learn oﬃcial documentation as:

<!-- b000208 | prose | pages [8] -->
푛 Õ

<!-- b000209 | prose | pages [8] -->
inertia =

<!-- b000210 | prose | pages [8] -->
푖=0

<!-- b000211 | prose | pages [8] -->
휇푗(|푥푖−휇푗|2)

<!-- b000212 | prose | pages [8] -->
min

<!-- b000213 | prose | pages [8] -->
where 퐶is the set of clusters and 휇푗is the mean (also known as centroid) of each cluster 푗∈퐶.1

<!-- b000214 | prose | pages [8] -->
This algorithm works by

<!-- b000215 | prose | pages [8] -->
1. initializing 푘centroids (in this case choosing far initial centroids to avoid convergence to a local minimum)

<!-- b000216 | prose | pages [8] -->
2. assigning each data point to the cluster with the closest centroid

<!-- b000217 | prose | pages [8] -->
3. redeﬁning the centroids as the new means of each cluster 퐶

<!-- b000218 | prose | pages [8] -->
4. repeating steps 2-3 until the centroids stop moving

<!-- b000219 | prose | pages [8] -->
in order to form 푘clusters of minimal inertia.1 We used the sklearn package’s implementation of K-Means Clustering to group the images into clusters of minimal variance from one another.1

<!-- b000220 | prose | pages [8] -->
In choosing a 푘value for 푘-Means Clustering, we identiﬁed 3 prioritizes (ordered highest priority to lowest priority):

<!-- b000221 | prose | pages [8] -->
• Maximizing accuracy as measured by

<!-- b000222 | prose | pages [8] -->
acc = 푇푃+ 푇푁

<!-- b000223 | prose | pages [8] -->
9

<!-- b000224 | prose | pages [8] -->
푇푃+ 푇푁+ 퐹푃+ 퐹푁

<!-- b000225 | prose | pages [8] -->
where 푇푃, 푇푁, 퐹푃, and 퐹푁were estimated by our eyeball identiﬁcation of positive images for Vespa mandarinia.

<!-- b000226 | prose | pages [8] -->
• Minimizing 퐹푃, because these assignments as positive or negative would be fed into the CNN as their "true" labels and our goal is to use the CNN to recognize distinctive features of Vespa mandarinia, so false positives skew this ability

<!-- b000227 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000228 | furniture | pages [8] -->
关注数学模型

<!-- b000229 | furniture | pages [8] -->
2

<!-- b000230 | furniture | pages [8] -->
MATHmodels

<!-- b000231 | furniture | pages [8] -->
获取更多资讯

<!-- b000232 | furniture | pages [9] -->
Team 2107870

<!-- b000233 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000234 | furniture | pages [9] -->
Page 7 of 23

<!-- b000235 | prose | pages [9] -->
• Minimizing variance in assigned clusters for the images estimated (by our eyeball measure) to be positive

<!-- b000236 | prose | pages [9] -->
Running several tests for 푘−values yielded:

<!-- b000237 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000238 | prose | pages [9] -->
푇푃+푇푁 푘 퐹푃 푇푃+푇푁+퐹푃+퐹푁 Variance 0.6428571429 2 2 0.5345224838 0.5714285714 3 3 4 4 0.5 0.6900655593 0.9511897312 0.5714285714 5 2 1.214985793 0.4285714286 6 3 1.527525232 0.4285714286 7 4 8 2 0.5 1.032795559 2.497617913 0.5714285714 9 1 2 0.6428571429 10 2 1.133893419

<!-- b000239 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000240 | prose | pages [9] -->
0.5714285714 11 2 1.463850109 0.6428571429 12 0 3.408672413 0.6428571429 13 0 3.552329886 0.6428571429 14 0 3.804758925 0.5714285714 15 1 3.236694375 0.5714285714 16 1 3.785938897 0.6428571429 17 0 2.811540842 0.4285714286 18 3 4.84522347 0.6428571429 19 0 3.690399385 0.5714285714 20 0 3.302235895

<!-- b000241 | caption | pages [9] -->
Figure 2: 푘-Value Analysis

<!-- b000242 | prose | pages [9] -->
From the table, we can see that 푘= 17 yields the optimal values according to our priorities, so we choose such a 푘. From the 푇푃,푇푁, 퐹푃, 퐹푁data we were able to derive estimations for the probability of these terms for the K-Means Clustering:

<!-- b000243 | prose | pages [9] -->
푇푁 푇푁+ 퐹푁= 0.5833333333 푃(푇푁) =

<!-- b000244 | prose | pages [9] -->
퐹푁 푇푁+ 퐹푁= 0.4166666667 푃(퐹푁) =

<!-- b000245 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000246 | furniture | pages [9] -->
关注数学模型

<!-- b000247 | furniture | pages [9] -->
2

<!-- b000248 | furniture | pages [9] -->
MATHmodels

<!-- b000249 | furniture | pages [9] -->
获取更多资讯

<!-- b000250 | furniture | pages [10] -->
Team 2107870

<!-- b000251 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000252 | furniture | pages [10] -->
Page 8 of 23

<!-- b000253 | prose | pages [10] -->
Algorithm 1: Applying K-Means Clustering. In developing the code for this algorithm we referenced Hrishi Patel’s article on K-Means Clustering for Image Segregation and utilized libraries sklearn, glob, OpenCV, numpy, os, and OpenPyxl12

<!-- b000254 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000255 | heading | pages [10] -->
1. Pre-process image data (see section 1.5) including ﬁltration by hand, estimation of labels, under-

<!-- b000256 | prose | pages [10] -->
sampling majority, augmenting the photos to increase sample size (using OpenCV), and ﬂattening the 2D image arrays to ﬂat 1D arrays14

<!-- b000257 | prose | pages [10] -->
2. Fit k-clusters to the pre-proceessed image data. 3. Average the cluster assignments of each image across all of its augmented versions (rotated and adjusted saturation/value), so that each image is assigned one cluster. 3. Track the classiﬁcations of the images that are estimated as positive cases, average these values, and ﬁnd the most common occurring cluster classiﬁcation for the supposedly positive data. If the most common occurring cluster classiﬁcation only occurs in the set of positive images once, then take the average to be the cluster corresponding to the positive images. Otherwise, take the cluster classiﬁcation of positive images to be the cluster classiﬁcation that occurs most often in this set. 4. Classify 58.33% of the images that diﬀer from the cluster chosen as the positive cluster as negative

<!-- b000258 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000259 | prose | pages [10] -->
cases. This percentage corresponds to the probability of a true negative classiﬁcation, which serves to potentially correct the error in k-means classiﬁcation when feeding these estimated labels into the Convolutional Neural Network. 5. Classify all images that have the same cluster classiﬁcation as the positive cluster as positive cases. Yields: Estimated labels for the unclassiﬁed images that will be fed into the training of the Convolutional Neural Network alongside the labeled data.

<!-- b000260 | prose | pages [10] -->
3.2 Convolutional Neural Network

<!-- b000261 | prose | pages [10] -->
Convolutional Neural Networks (CNN) are commonly used in problems of computer vision.8 Convo- lutional neural networks apply learned ﬁlters to images in order to reduce the size of an image and illuminate salient features of the image.16 As any deep learning technique, it is characterized by several layers that the data is fed through (and that the gradients are back-propagated through).3 For this reason, lower level layers in a CNN typically learn the lower level features (lines, basic shapes, etc.); whereas, higher level layers in a CNN learn the higher level features (e.g. object classiﬁcation). This leads to CNNs often being called hierarchical in nature.8

<!-- b000262 | prose | pages [10] -->
CNNs go through repeated steps of applying convolutions and performing pooling. In convolution, you step through each grouping of pixels equal in size to the ﬁlter. You multiply corresponding entries and add those values to one another forming a more compact image. Then pooling reduces each grouping of pixels the size of the ﬁlter down to one value. In our model, we used a process called max-pooling where you take the maximum value of the pixels in this grouping so as to reduce noise in the image.16

<!-- b000263 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000264 | furniture | pages [10] -->
关注数学模型

<!-- b000265 | furniture | pages [10] -->
2

<!-- b000266 | furniture | pages [10] -->
MATHmodels

<!-- b000267 | furniture | pages [10] -->
获取更多资讯

<!-- b000268 | furniture | pages [11] -->
Team 2107870

<!-- b000269 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000270 | furniture | pages [11] -->
Page 9 of 23

<!-- b000271 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000272 | caption | pages [11] -->
Figure 3: Convolutional Neural Network Process-made using LucidChart

<!-- b000273 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000274 | prose | pages [11] -->
We used TensorFlow with Keras to create our CNN, referencing examples from Chollet’s Deep Learning with Python and utilizing os, glob, numpy, openpyxl, and OpenCV as helper libraries7. In forming the network, we chose to use 3 2D Convolutional layers with 3 corresponding 2D maxpooling From there, we ﬂattened the tensor (structure holding the data) being passed through the layers. network and passed it into two densely connected layers for classiﬁcation using the Sigmoid activation function and the Binary-Cross Entropy loss function:

<!-- b000275 | prose | pages [11] -->
• The Sigmoid activation function is a non-linear function to which the probability of a positive classiﬁcation of an image is ﬁt. It ranges in values from 0 to 1, making it ideal for a binary classiﬁcation problem (positive or negative for Vespa mandarinia), and is diﬀerentiable, which allows for the use of the backpropogation method essential to adjusting the weights of a neural network according to the loss function717.

<!-- b000276 | prose | pages [11] -->
• The Binary-Cross Entropy loss function measures the diﬀerence in entropy of an approximated (by the neural net) entropy and the actual entropy of a probability distribution (in this case one for binary classiﬁcation)godoy_daniel_20182. It is given by Daniel Godoy as

<!-- b000277 | prose | pages [11] -->
푛

<!-- b000278 | prose | pages [11] -->
−1

<!-- b000279 | prose | pages [11] -->
Õ

<!-- b000280 | prose | pages [11] -->
푦푖log(푝(푦푖)) + (1 −푦푖) ∗log(1 −푝(푦푖))

<!-- b000281 | prose | pages [11] -->
푁

<!-- b000282 | prose | pages [11] -->
푖=1

<!-- b000283 | prose | pages [11] -->
godoy_daniel_2018

<!-- b000284 | prose | pages [11] -->
where 푁is the number of points in an input data vector (e.g.

<!-- b000285 | prose | pages [11] -->
our image), 푦푖is the actual probability of a positive classiﬁcation, and 푝(푦푖) is the approximated probability of a positive classiﬁcation by the modelgodoy_daniel_2018. The idea behind such a loss function is that for low probabilities of 푦푖푙표푔(푝(푦푖)) will be large causing a high loss and vice versa for when the probability of 푦푖is highgodoy_daniel_2018.

<!-- b000286 | prose | pages [11] -->
In our CNN, we input images in the shape (224, 224, 3) where the image was 224 by 224 with 3 color channels (red, green, blue). The model summary showing the changing of tensor shape as well as the number of trainable parameters in each layer of the model is detailed below. From this ﬁgure we can see the gradual reduction in size of the image.

<!-- b000287 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000288 | furniture | pages [11] -->
关注数学模型

<!-- b000289 | furniture | pages [11] -->
2

<!-- b000290 | furniture | pages [11] -->
MATHmodels

<!-- b000291 | furniture | pages [11] -->
获取更多资讯

<!-- b000292 | furniture | pages [12] -->
Team 2107870

<!-- b000293 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000294 | furniture | pages [12] -->
Page 10 of 23

<!-- b000295 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000296 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000297 | caption | pages [12] -->
Figure 4: CNN Model Summary

<!-- b000298 | prose | pages [12] -->
We apply dropout to this model in order to curb the eﬀects of the model overﬁtting to the data (especially given the relatively small data set). Dropout is the process of randomly dropping values in a neural network in order to add stochasticity and prevent overﬁtting.7 Adding a dropout rate of 0.5 is a relatively common practice in Deep Learning.7

<!-- b000299 | prose | pages [12] -->
We also set the initial bias value of the CNN in order to accommodate for how skewed the data is towards the majority of negative classiﬁcation. This manual bias initialization allows the network to immediately begin approximating better probability values for the classiﬁcation of the images and is found using:

<!-- b000300 | prose | pages [12] -->
푛푒푔) = log( 푇푃

<!-- b000301 | prose | pages [12] -->
푏0 = log( 푝표푠

<!-- b000302 | prose | pages [12] -->
푇푁)

<!-- b000303 | prose | pages [12] -->
as speciﬁed by Tensor Flow tutorials/documentation5.

<!-- b000304 | heading | pages [12] -->
Algorithm 2: Applying CNN

<!-- b000305 | heading | pages [12] -->
1. Pre-process image data (see section 1.5) including by resizing and augmenting the photos (by adding

<!-- b000306 | prose | pages [12] -->
copies with stochastically changed saturation and value within ±50 of the original values) to increase sample size (using OpenCV). 2. Under-sample the majority (negative classiﬁcations) to two-thirds of their original sample-size to allow for less of a bias towards negative classiﬁcation. 3. Train the CNN on the preprocessed data and their accompanying labels (including those estimated by the K-Means Clustering) for a total of 25 epochs with a batch size of 128 images. 4. Preprocess all of the image data (that was not thrown out for being irrelevant or for being un- clear/noisy) by resizing to 224 by 224. 5. Allow the model to predict the probabilities of each image being a positive classiﬁcation. Yields: Probabilities for all of the image data where higher probabilities represent a higher likelihood of being Vespa mandarinia.

<!-- b000307 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000308 | furniture | pages [12] -->
关注数学模型

<!-- b000309 | furniture | pages [12] -->
2

<!-- b000310 | furniture | pages [12] -->
MATHmodels

<!-- b000311 | furniture | pages [12] -->
获取更多资讯

<!-- b000312 | furniture | pages [13] -->
Team 2107870

<!-- b000313 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000314 | furniture | pages [13] -->
Page 11 of 23

<!-- b000315 | prose | pages [13] -->
Probability distributions for PositiveID, NegativeID, and Unlabeled image datasets made using mat- plotlib:

<!-- b000316 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000317 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000318 | caption | pages [13] -->
Figure 5: Box Plots for Unlabeled, Positive, and Negative Probability Distributions.

<!-- b000319 | prose | pages [13] -->
Note: The scale of the y-axis in the above plots has been adjusted.

<!-- b000320 | prose | pages [13] -->
4 Semantics Analysis

<!-- b000321 | prose | pages [13] -->
The objective for the Semantics Track is to develop a probability reﬂecting whether a civilian report and its associated Detection Date and Notes Description suggest a PositiveID Vespa mandarinia. This probability will contribute to the overall metric for probability of a false classiﬁcation as Vespa mandarinia. The ﬁrst step in this analysis is the already referenced data cleaning and preprocessing. The cleaned monthly data and lower case notes data was then passed for semantics analysis.

<!-- b000322 | prose | pages [13] -->
The objective of parsing through language data posed a massive challenge. By the conventions of the English language semiotics, there can be many diﬀerent signiﬁers (words) to a signiﬁed (object) meaning. For example, in describing the nest location of Vespa mandarinia some civilians referred to the "forest" others the "woods". Both reference the same signiﬁed object but do so using diﬀerent signiﬁers.

<!-- b000323 | prose | pages [13] -->
Based oﬀthe Penn State Extension on Vespa mandarinia, we made assumptions stemming from the scientiﬁc journal about the qualities and timelines associated with this species versus look-alike species. Each key word was given equal weight in determining the probability of whether the Detection Date, Global ID and Notes triad reﬂected a possible PositiveID. Using key word extraction, we parse through the Notes data for the following terms: (1) orange, (2) brown, (3) yellow head / yellowish head,

<!-- b000324 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000325 | furniture | pages [13] -->
关注数学模型

<!-- b000326 | furniture | pages [13] -->
2

<!-- b000327 | furniture | pages [13] -->
MATHmodels

<!-- b000328 | furniture | pages [13] -->
获取更多资讯

<!-- b000329 | furniture | pages [14] -->
Team 2107870

<!-- b000330 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000331 | furniture | pages [14] -->
Page 12 of 23

<!-- b000332 | prose | pages [14] -->
(4) decapitate, (5) forest / wood, (6) 2" / 2 inch, (7) big / giant, (8) dirt, (9) red, (10) black head, (11) orange legs.

<!-- b000333 | prose | pages [14] -->
Each phrase parsed through in the data was given a positive or negtive weight of 0.05 depending on whether this phrase was indicative of Vespa manadrina, its description and life cycle. Terms 8 -

<!-- b000334 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000335 | prose | pages [14] -->
11 are indicative of look-alike species to the Vespa mandarinia; for this reason, it is less likely that a report is of Vespa mandarinia if terms 8-11 are referenced. These terms were included to gauge the misclassiﬁcation of Vespa mandarinia. The probability that the sighting was a positive classiﬁcation was initialized to 0.5 to reﬂect our assumption that a sighting is equally likely to be positive or negative with zero information. If a phrase from Terms 1 - 7 was found in the notes section, we increased the probability of positive classiﬁcation by 0.05. If a phrase from Terms 8 - 11 was found in the notes section, we decreased the probability of a positive classiﬁcation by 0.05. Certain phrases’ probability assignments are dependent upon the life cycle of Vespa mandarinia: (1) dead / specimen, (2) live / killed, (3) nest / hive. If phrase 1 is presen with detection date between October and January (Winter months), the probability of positive classiﬁcation increases by 0.05. If it

<!-- b000336 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000337 | prose | pages [14] -->
is present in other times, the probability decreases by 0.05. If phrase 2 is present in February through September, then the probability of positive classiﬁcation increases by 0.05, and decreases otherwise. Lastly, if phrase 3 is present with detection date in March or April, then the probability of positive classiﬁcation increases by 0.05 and decreases otherwise. The resulting distribution of probability assignments for PositiveID, NegativeID, and Unlabeled Notes and Detection Date datasets made using matplotlib:

<!-- b000338 | caption | pages [14] -->
Figure 6: Box Plots for Unlabeled, Positive, and Negative Probability Distributions.

<!-- b000339 | prose | pages [14] -->
Note: The scale of the y-axis in the above plots has been adjusted.

<!-- b000340 | prose | pages [14] -->
Spatial and Temporal Pest Spread Analysis 5

<!-- b000341 | prose | pages [14] -->
The common method of modeling the population growth and spread of an invasive species is the Reaction-Diﬀusion Model as used by Robinet et al.

<!-- b000342 | prose | pages [14] -->
when modeling the spacial spread of Vespa velutina in France.15 The model is described by the Fisher equation:

<!-- b000343 | prose | pages [14] -->
휕푥2 + 휕2푁

<!-- b000344 | prose | pages [14] -->
휕2푁

<!-- b000345 | prose | pages [14] -->
휕푁

<!-- b000346 | prose | pages [14] -->
휕푡= 퐷

<!-- b000347 | prose | pages [14] -->
1 −푁

<!-- b000348 | prose | pages [14] -->


<!-- b000349 | prose | pages [14] -->


<!-- b000350 | prose | pages [14] -->


<!-- b000351 | prose | pages [14] -->
(1)

<!-- b000352 | prose | pages [14] -->
+ 푟푁

<!-- b000353 | prose | pages [14] -->
휕푥2

<!-- b000354 | prose | pages [14] -->
퐾

<!-- b000355 | prose | pages [14] -->
√

<!-- b000356 | prose | pages [14] -->
whose solution produces the following travelling wave equation: 푐= 2

<!-- b000357 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000358 | prose | pages [14] -->
푟퐷

<!-- b000359 | furniture | pages [14] -->
关注数学模型

<!-- b000360 | furniture | pages [14] -->
2

<!-- b000361 | furniture | pages [14] -->
MATHmodels

<!-- b000362 | furniture | pages [14] -->
获取更多资讯

<!-- b000363 | furniture | pages [15] -->
Team 2107870

<!-- b000364 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000365 | furniture | pages [15] -->
Page 13 of 23

<!-- b000366 | prose | pages [15] -->
This model is eﬀective when accurate estimations of c, K, and r can be made from empirical data. Unfortunately, there is relatively little historical data concerning the Vespa mandarinia’s population growth. The Citizen Sighting data itself also lacks suﬃcient positive ID data points to estimate these In order to use this model given the current data, the variables had to be derived from metrics.

<!-- b000367 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000368 | prose | pages [15] -->
entomological observations11. The estimations are as follows: c = 9.74, K = 1, r = 1.35.

<!-- b000369 | prose | pages [15] -->
Given that these are merely estimates, the entire model could not be reliably implemented to help predict the spread of Vespa mandarinia in the state of Washington. However it allowed us to create maximum area bounds outside of which we applied a zero probability of a Vespa mandarinia sighting, along with an area of maximum interest for further study.

<!-- b000370 | prose | pages [15] -->
The maximum area bounds were made by evaluating the worst case scenario.

<!-- b000371 | prose | pages [15] -->
We made the assumptions of long-range dispersal (c=30 km/year) and multiple introduction locations into various port cities of the state of Washington, as far south as Olympia, WA (47.0379°N, 122.9007°W). These assumptions were made for this situation because the value of c is not currently backed by empirical data, and the form of introduction of the species to the Paciﬁc Northwest is still unknown. It is for these reasons that the probabilities of these events are still nonzero and should be considered in the spacial

<!-- b000372 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000373 | prose | pages [15] -->
realm of possibility.

<!-- b000374 | prose | pages [15] -->
The area of maximum interest for further study was calculated as the area predicted to have the highest nest density in the state of Washington in 2021. Where the spacial sample mean of the 2019 positive ID sightings was taken as the initial nest location and the values of c, K, and r come from the table above. This metric was calculated solely as a recommendation to the state as an area whose study could help produce an accurate prediction of the spread of Vespa mandarinia, not as a probability contribution to our model.

<!-- b000375 | prose | pages [15] -->
6

<!-- b000376 | heading | pages [15] -->
Model Uniﬁcation Equation

<!-- b000377 | prose | pages [15] -->
The Model Uniﬁcation Equation produces a singular metric for the probability of a reported sighting being misclassiﬁed as a sighting of Vespa mandarinia (meaning it is not genuinely Vespa mandarinia). It does so by adding 1 minus the probabilities produced by the image track and the notes track weighted by the probability of a true negative for each of these tracks. From there, the probability of misclassiﬁ- cation is set to 1 if the longitude is greater than -121 or if the latitude is less than 46.7 due to the practical impossibility of Vespa mandarinia existing in these locations unless they were intentionally moved there.

<!-- b000378 | prose | pages [15] -->
• 푃푛표푡푒푠(푇푁) is estimated by ﬁnding the estimated probability of all of the sightings with Lab Statuses of Negative. Then the mean and standard deviation of this set of probabilities is found using the statisics library in python. Any sightings with probability, from semantic analysis, within the range of [0, 휇+ 휎) are labeled negative and all others are labeled positive sightings. Then the estimated labels from the K-Means Clustering algorithm as well as the given labels are compared against these newly assigned labels to determine estimated values for푇푃,푇푁, 퐹푃, 퐹푁.

<!-- b000379 | prose | pages [15] -->
푇푁 Then 푃(푇푁) = 퐹푁+푇푁.

<!-- b000380 | prose | pages [15] -->
• 푃푖푚푎푔푒푠(푇푁) is a metric tracked by the convolutions neural network as it trains.

<!-- b000381 | prose | pages [15] -->
Let 푀푖be the mapping of GlobalIDs to probabilities from images and 푀푛be the mapping of GlobalIDs to probabilities from notes. The resulting uniﬁed value for the probability of misclassiﬁed sighting

<!-- b000382 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000383 | furniture | pages [15] -->
关注数学模型

<!-- b000384 | furniture | pages [15] -->
2

<!-- b000385 | furniture | pages [15] -->
MATHmodels

<!-- b000386 | furniture | pages [15] -->
获取更多资讯

<!-- b000387 | furniture | pages [16] -->
Team 2107870

<!-- b000388 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000389 | furniture | pages [16] -->
Page 14 of 23

<!-- b000390 | prose | pages [16] -->
corresponding to a particular Global ID, 푖, is given by

<!-- b000391 | prose | pages [16] -->
(1 −푝푛표푡푒푠) ∗푃푛표푡푒푠(푇푁) + (1 −푝푖푚푎푔푒푠) ∗푃푖푚푎푔푒푠(푇푁)

<!-- b000392 | prose | pages [16] -->


<!-- b000393 | prose | pages [16] -->
(1 −푝푛표푡푒푠) ∗푃푛표푡푒푠(푇푁) 푖∈푀푖, 푀푛 if 푖∈푀푛, 푖∉푀푖

<!-- b000394 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000395 | prose | pages [16] -->
푝=

<!-- b000396 | prose | pages [16] -->
(1 −푝푖푚푎푔푒푠) ∗푃푖푚푎푔푒푠(푇푁) 0.5 if 푖∉푀푛, 푀푖

<!-- b000397 | prose | pages [16] -->


<!-- b000398 | prose | pages [16] -->
1 if lat > -122.06 or long < 46.7 if 푖∈푀푖, 푖∉푀푛

<!-- b000399 | prose | pages [16] -->
If this equation produces some 푝> 1, then 푝is set to 1. If this equation produces some 푝< 0, then 푝 is set to 0.

<!-- b000400 | prose | pages [16] -->
7

<!-- b000401 | heading | pages [16] -->
Results and Discussion

<!-- b000402 | prose | pages [16] -->
7.1

<!-- b000403 | heading | pages [16] -->
Discussion of Spread Over Time

<!-- b000404 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000405 | prose | pages [16] -->
Given the small amount of current data of Vespa mandarinia sightings in the state of Washington, it is not possible to produce an accurate prediction of species spread and population growth over time. However, comparing estimates based on entomological observations to values of similar species (french spread) allowed us to produce spacial bounds outside of which the probability of a positive sighting in 2020 is zero. (Maximum Easterly Longitude Bound: -122.063°, Maximum Southerly Latitude Bound: 46.77°) The area of maximum interest for further study lies within 23.63 km circle of the assumed initial nest site (-122.72558475, 48.9931665). The furthest point from the spacial mean using a simpliﬁed short- distance dispersal model would be located 29.22 km away from the assumed point of introduction. It is within this area that data points could be gathered that would give further insight into Vespa mandarinia nesting patterns, speciﬁcally lending data that would allow for empirical estimations of carrying capacity and population growth rate.

<!-- b000406 | prose | pages [16] -->
If high-integrity data is collected in the spring, summer and fall seasons, regarding nest locations and hornet sights, the spread of Vespa mandarinia could be accurately modelled using the reaction- diﬀusion model. Integrating research on habitat suitability metrics from CLIMEX modelling15 into the spacial model would create a metric that could strengthen our current model by determining the spacial probability of a positive sighting.

<!-- b000407 | prose | pages [16] -->
An uncertainty analysis done using a similar model with a larger dataset15, showed a sensitivity in the model to calculation of r. Their calculations of r depended on habitat suitability metrics that incorporated CLIMEX modelling. The modelling showed estimations of K and c as the mean baseline to be the optimal solution and the model to be considered robust. Therefore, given more high-integrity data in 2021, our model can be utilized to produce a similar precision.

<!-- b000408 | prose | pages [16] -->
Once this portion of the model is implemented and integrated into the generalized model, annual updates to the true pest locations are necessary in order to adjust the probability that a sighting is positive or negative for Vespa mandarinia.

<!-- b000409 | prose | pages [16] -->
7.2

<!-- b000410 | heading | pages [16] -->
Results of Sighting Classiﬁcation

<!-- b000411 | prose | pages [16] -->
From the Model Uniﬁcation Equation, we received a probability mapping from each GlobalID to the probability that the sighting was a misclassiﬁcation (negative for Vespa mandarinia). From this

<!-- b000412 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000413 | furniture | pages [16] -->
关注数学模型

<!-- b000414 | furniture | pages [16] -->
2

<!-- b000415 | furniture | pages [16] -->
MATHmodels

<!-- b000416 | furniture | pages [16] -->
获取更多资讯

<!-- b000417 | furniture | pages [17] -->
Team 2107870

<!-- b000418 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000419 | furniture | pages [17] -->
Page 15 of 23

<!-- b000420 | prose | pages [17] -->
mapping, we could split the probabilities into three sets: positive, negative, and unlabeled (Unveriﬁed or Unprocessed) as given by the original dataset. The standard deviation and mean of the probabilities corresponding to each of these three sets is given below-found using statistics library in python:

<!-- b000421 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000422 | prose | pages [17] -->
Set 휇 휎 0.4798952739096558 Positive 0.02384031216308337 0.9710264772650146 Negative 0.11967336173438212 0.5982794013488542 Unlabeled 0.2213738686521228

<!-- b000423 | caption | pages [17] -->
Figure 7: Probability Mean and Deviation

<!-- b000424 | prose | pages [17] -->
The probabilities associated with each set is demonstrated by these box plots made using matplotib:

<!-- b000425 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000426 | caption | pages [17] -->
Figure 8: Box Plots for Unlabeled, Positive, and Negative Probability Distributions.

<!-- b000427 | prose | pages [17] -->
Note: The scale of the y-axis in these plots has been adjusted.

<!-- b000428 | prose | pages [17] -->
7.3 Prioritizing Investigation

<!-- b000429 | prose | pages [17] -->
Based upon the probability associated with each of the 3 sets mentioned in section 7.2 (Positive, Negative, and Unlabeled) as well as their associated mean and standard deviations (found using the statistics library in python), we have come up with intervals of probabilities from the model corresponding to high, medium and low priority for investigation:

<!-- b000430 | prose | pages [17] -->
Priority

<!-- b000431 | prose | pages [17] -->
Interval

<!-- b000432 | prose | pages [17] -->
Level

<!-- b000433 | prose | pages [17] -->
Low [0.8513531155306324, 1] [0.5037355860727392, 0.8513531155306324] Medium High [0, 0.5037355860727392]

<!-- b000434 | caption | pages [17] -->
Figure 9: Priority Levels and Corresponding Intervals of Probability

<!-- b000435 | prose | pages [17] -->
The idea behind these intervals is that the Washington State Department of Agriculture would be able to feed the sightings data point (as characterized by detection date, image of insect, reported notes, latitude of detection, and longitude of detection), which would be analyzed by the model in the following process:

<!-- b000436 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000437 | furniture | pages [17] -->
关注数学模型

<!-- b000438 | furniture | pages [17] -->
2

<!-- b000439 | furniture | pages [17] -->
MATHmodels

<!-- b000440 | furniture | pages [17] -->
获取更多资讯

<!-- b000441 | furniture | pages [18] -->
Team 2107870

<!-- b000442 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000443 | furniture | pages [18] -->
Page 16 of 23

<!-- b000444 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000445 | caption | pages [18] -->
Figure 10: View of the model from the Washington State Department made using LucidChart.

<!-- b000446 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000447 | prose | pages [18] -->
resulting in a single metric for the probability of misclassiﬁcation of sighting as Vespa mandarinia. The priority level of investigation would then be determined by under which of the above intervals the assigned probability falls. For example, sighting {09F8A9C3-1692-4DE3-9EE1-3FD1DEACFFD5} was assigned a probability of being a misclassiﬁcation of 0.965601349, which is within the low priority interval. Here are the corresponding relevant data points for this sighting:

<!-- b000448 | caption | pages [18] -->
Figure 11: Sighting {09F8A9C3-1692-4DE3-9EE1-3FD1DEACFFD5} Image.

<!-- b000449 | prose | pages [18] -->
Detection Date Notes 7/31/20 Null Latitude Longitude 48.06114 -122.1769

<!-- b000450 | caption | pages [18] -->
Figure 12: Detection Date, Notes, and Location data for sighting {09F8A9C3-1692-4DE3-9EE1-

<!-- b000451 | prose | pages [18] -->
3FD1DEACFFD5}.

<!-- b000452 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000453 | furniture | pages [18] -->
关注数学模型

<!-- b000454 | furniture | pages [18] -->
2

<!-- b000455 | furniture | pages [18] -->
MATHmodels

<!-- b000456 | furniture | pages [18] -->
获取更多资讯

<!-- b000457 | furniture | pages [19] -->
Team 2107870

<!-- b000458 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000459 | furniture | pages [19] -->
Page 17 of 23

<!-- b000460 | prose | pages [19] -->
The Notes data was not included within the data and the location is well within the bounds of a valid sighting; however, the image classiﬁcation track deems this insect dissimilar to Vespa mandarinia; therefore, it is assigned to the low priority interval for investigation.

<!-- b000461 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000462 | prose | pages [19] -->
7.4 Evidence for Eradication

<!-- b000463 | prose | pages [19] -->
We are able to extrapolate our model out in time to discuss how our Model Uniﬁcation Equation, that gives discrete probability points, can be mapped to determine the status of eradicating Vespa mandarinia in the State of Washington. Based on our Spatian and Temporal Pest Spread Analysis, the long range dispersal is a generous 30 km spread per year. This metric was based on a short distance dispersal model and reﬂects the ability of Vespa mandarinia to not only navigate the Washington terrain and altitude, and also the conﬁdence in understanding species in a smaller range based on the relative size of the habitable locations in Washington for Vesapa mandarinia. Based on our model, the eradication of Vespa mandarinia is conservatively evidenced by all probabilities of sightings being in the low priority interval within 30km of the known pest locations of the last 2 seasonal cycles.

<!-- b000464 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000465 | caption | pages [19] -->
Figure 13: 30 km range around all current 2019 and 2020 PostiveID Vespa mandarinia.

<!-- b000466 | prose | pages [19] -->
This evidence must be applied to all 30km ranges of the Northwest most part of the state. Evidence for Eradication by our model is most accurate after the unveriﬁed data has been parsed and after the urgent locations have been excavated.

<!-- b000467 | prose | pages [19] -->
8

<!-- b000468 | heading | pages [19] -->
Sensitivity Analysis

<!-- b000469 | prose | pages [19] -->
In order to determine the sensitivity of the image-based model against diﬀering sets of training data, we performed K-Fold Cross Validation with 푘= 3 folds. K-Fold Cross Validation involves seperating all of the image data into two groups: training and validation with the size of those two datasets being

<!-- b000470 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000471 | furniture | pages [19] -->
关注数学模型

<!-- b000472 | furniture | pages [19] -->
2

<!-- b000473 | furniture | pages [19] -->
MATHmodels

<!-- b000474 | furniture | pages [19] -->
获取更多资讯

<!-- b000475 | furniture | pages [20] -->
Team 2107870

<!-- b000476 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000477 | furniture | pages [20] -->
Page 18 of 23

<!-- b000478 | prose | pages [20] -->
equal to length(image dataset)/3 and 2 ∗length(image dataset)/3 respectively, when 푘= 3. 3 models are run after having been trained on 3 disjoint training sets and validated on the rest of the data. The result is an ability to assess the sensitivity of the model to diﬀerent training data sets. Below are the confusion matrices for each of these 3 iterations at training and validation (made using seaborn and

<!-- b000479 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000480 | prose | pages [20] -->
referencing TensorFlow’s documentation/examples).

<!-- b000481 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000482 | caption | pages [20] -->
Figure 14: Confusion Matrices for each of 3-folds with division between positive and negative at

<!-- b000483 | prose | pages [20] -->
푝= 0.5 where 0 coresponds to negative classiﬁcation and 1 responds to positive classiﬁcation.

<!-- b000484 | prose | pages [20] -->
As we can see above, the largest diﬀerence in 푇푃,푇푁, 퐹푁, 퐹푃is in the last iteration’s 푇푁and 푇푃 rates, which, respectively, only diﬀer by 0.84% and 6.06% maximally. Therefore, we can conclude that the image classiﬁcations are largely unsensitive to changes in training data.

<!-- b000485 | prose | pages [20] -->
9

<!-- b000486 | heading | pages [20] -->
Model Evaluation

<!-- b000487 | prose | pages [20] -->
9.1

<!-- b000488 | heading | pages [20] -->
Strengths

<!-- b000489 | prose | pages [20] -->
1. Our model utilizes diverse methods of parsing through the unstructured data. We leverage the use of image processing in a convolutional neural net, automated keyword extraction in the submission notes to create a comprehensive metric of whether the submission is likely to be

<!-- b000490 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000491 | furniture | pages [20] -->
关注数学模型

<!-- b000492 | furniture | pages [20] -->
2

<!-- b000493 | furniture | pages [20] -->
MATHmodels

<!-- b000494 | furniture | pages [20] -->
获取更多资讯

<!-- b000495 | furniture | pages [21] -->
Team 2107870

<!-- b000496 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000497 | furniture | pages [21] -->
Page 19 of 23

<!-- b000498 | prose | pages [21] -->
Vespa mandarinia. The use of image, video, date, location, notes, and lab status data allows gives our model the necessary scalability to combat the high volumes of reporting.

<!-- b000499 | heading | pages [21] -->
2. Data fed through our Semantics model is evaluated with consistent criteria.

<!-- b000500 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000501 | heading | pages [21] -->
3. Our model produces real time analysis and probabilities that predict the likelihood of a mistaken

<!-- b000502 | prose | pages [21] -->
classiﬁcation. This gives our model the needed ﬂexibility to process additional new reports over time, bolstering the longevity of our model with the only requirement being an annual update to the spatial portion of the model to reﬂect pest spread.

<!-- b000503 | prose | pages [21] -->
4. Many of the assumptions made for the model image, description and location analysis were rooted in validated scientiﬁc knowledge on Vespa mandarinia by Penn State Extension.

<!-- b000504 | prose | pages [21] -->
5. Our model has a modular approach allowing the Image, Semantics, and Spatial Analysis to be updated individually without inﬂuencing the other forms of analysis.

<!-- b000505 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000506 | prose | pages [21] -->
9.2

<!-- b000507 | heading | pages [21] -->
Weaknesses

<!-- b000508 | prose | pages [21] -->
1. The Convolutional Neural Net would produce greater accuracy in identiﬁcation if there was more PositiveID image data available. More data over time will only strengthen the model.

<!-- b000509 | heading | pages [21] -->
2. The variability in the English language and the ability to convey the same idea using a myriad

<!-- b000510 | prose | pages [21] -->
of word combinations took a toll on the Semantics Analysis. Some key words or phrases may be overlooked because the civilian chose a unique, nontrivial description of the alleged Vespa mandarinia.

<!-- b000511 | heading | pages [21] -->
3. There is a large amount of variance within the probabilities associated with the NegativeID set

<!-- b000512 | prose | pages [21] -->
in particular (made using matplotlib):

<!-- b000513 | caption | pages [21] -->
Figure 15: Boxplot with outliers for NegativeID probability distribution.

<!-- b000514 | prose | pages [21] -->
This leads to diﬃculty in deﬁning eradication with certainty given some negative data will be assigned high level investigation priority.

<!-- b000515 | prose | pages [21] -->
4. Image segmentation was not performed by the Convolutional Neural Network, meaning image classiﬁcation may be less accurate when there are multiple insects of varying species in an image.

<!-- b000516 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000517 | furniture | pages [21] -->
关注数学模型

<!-- b000518 | furniture | pages [21] -->
2

<!-- b000519 | furniture | pages [21] -->
MATHmodels

<!-- b000520 | furniture | pages [21] -->
获取更多资讯

<!-- b000521 | furniture | pages [22] -->
Team 2107870

<!-- b000522 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000523 | furniture | pages [22] -->
Page 20 of 23

<!-- b000524 | heading | pages [22] -->
Conclusion and Updating the Model for Future Work

<!-- b000525 | prose | pages [22] -->
10

<!-- b000526 | prose | pages [22] -->
In this paper we formulated a model that the Washington State Department of Agriculture can apply to prioritize investigating the species Vespa mandarinia. We produced probabilities of positive iden-

<!-- b000527 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000528 | prose | pages [22] -->
tiﬁcation as Vespa mandarinia based on Image, Semantics, and Spatial Classiﬁcation techniques. We modeled the likelihood of TN data classiﬁcation from each of the approaches. 푃(푇푁), as well as the Image, Semantics and Spatial Classiﬁcations were all fed into the Model Uniﬁcation Equation.

<!-- b000529 | prose | pages [22] -->
Our results indicate that modeled probabilities are to be classiﬁed into 3 priority levels based upon the mean and standard deviation of probabilities assigned to the classes of NegativeID and PositiveID data:

<!-- b000530 | prose | pages [22] -->
Priority

<!-- b000531 | prose | pages [22] -->
Interval of Probability

<!-- b000532 | prose | pages [22] -->
Level

<!-- b000533 | prose | pages [22] -->
Low [0.8513531155306324, 1] [0.5037355860727392, 0.8513531155306324] Medium High [0, 0.5037355860727392]

<!-- b000534 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000535 | prose | pages [22] -->
Given additional new reports over time, we can update our model by strengthening our evaluation of pest spread. For future work, our model should be updated to include additional climate data. Outlined in the strengths, our model allows for real-time analysis, so our updates can occur within moments of a proper submission. Climate data can be easily integrated into the Species Spatial Spread to reconﬁgure our Model Uniﬁcation Equation deliverable.

<!-- b000536 | prose | pages [22] -->
The Spatial Analysis portion should be updated annually to reﬂect the pest spread over time, which eﬀects the overall probability of a positive or negative classiﬁcation as Vespa mandarina.

<!-- b000537 | prose | pages [22] -->
While our Model leverages every subset of the given data set to conﬁgure a metric to prioritizing civilian report investigation, there are many improvements that can be made given extended time and research.

<!-- b000538 | prose | pages [22] -->
1. Access to a pre-trained neural net would produce better accuracy of shape recognition. This would be complemented with more data on PostiveIDs of Vespa mandarinia to continue to train the CNN on.

<!-- b000539 | prose | pages [22] -->
2. Rather than doing statistical key word extraction from the Notes data subset, an improvement of this model would be to create a text sentiment neural net. Crafting a second neural net would make our model more robust in analysing human patterns and deviations.

<!-- b000540 | prose | pages [22] -->
3. With more data on the density of the spread of the data, a better picture of the spread of this pest over time can be predicted with increasing precision. There were only 12 veriﬁed PositiveIDs of Vespa mandarinia which allows for sparse conclusions to be made on the origins of any infestations or nests.

<!-- b000541 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000542 | furniture | pages [22] -->
关注数学模型

<!-- b000543 | furniture | pages [22] -->
2

<!-- b000544 | furniture | pages [22] -->
MATHmodels

<!-- b000545 | furniture | pages [22] -->
获取更多资讯

<!-- b000546 | furniture | pages [23] -->
Team 2107870

<!-- b000547 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000548 | furniture | pages [23] -->
Page 21 of 23

<!-- b000549 | heading | pages [23] -->
Memorandum to the Washington State Department of Agri-

<!-- b000550 | prose | pages [23] -->
11 culture

<!-- b000551 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000552 | prose | pages [23] -->
TO: The Washington State Department of Agriculture

<!-- b000553 | prose | pages [23] -->
FROM: MCM Team 2107870

<!-- b000554 | prose | pages [23] -->
DATE: February 8, 2021

<!-- b000555 | heading | pages [23] -->
SUBJECT: Analysis of Vespa mandarinia Sightings and Recommendations for Investigation

<!-- b000556 | prose | pages [23] -->
We are writing to address the State of Washington’s ongoing eﬀorts to detect occurrences and spread of the Vespa mandarinia species, commonly known as the Asian Giant Hornet. Vespa mandarinia poses a great threat to the Washington state ecology. In our new partnership, we are dedicated to protecting

<!-- b000557 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000558 | prose | pages [23] -->
the State of Washington and greater area ecology, helping the community ﬁnd safety in nature, and most importantly, developing a concrete metric that allows better allocation your resources in these eﬀorts.

<!-- b000559 | prose | pages [23] -->
By sifting through the image, text and location data collected in your initial eﬀorts to track pub- lic sightings of Vespa mandarinia, our team has developed a long-term process and metric which will assist your department in identifying which civilian submissions should be allocated highest pri- ority and conversely lowest priority investigation. We will walk you through the development of the model used to process reports, and furthermore provide concrete recommendations to your department.

<!-- b000560 | prose | pages [23] -->
OUR APPROACH We developed a model with two analysis tracks: image data analysis and notes/date of detection analysis.

<!-- b000561 | prose | pages [23] -->
1. The image data analysis track requires the input of still images of the insect being reported.

<!-- b000562 | prose | pages [23] -->
The output of this track is a list that links the GlobalIDs of the sighting to the probability that the image is of Vespa mandarinia. These probabilities range from 0 to 1. A value of 0 means the image is not of Vespa mandarinia, and a value of 1 means the image is an image of Vespa mandarinia.

<!-- b000563 | prose | pages [23] -->
2. The notes/date of detection detection analysis requires the input of these two data points and outputs the a list linking the GlobalIDs of the sightings to the probability that the notes data of that sighting refers to Vespa mandarinia on a the same scale of 0 to 1.

<!-- b000564 | prose | pages [23] -->
Our model takes these two lists from the separate tracks, as well as the location data of longitude and latitude, and combines them. You are given a list of pairings between GlobalIDs and the probability that the reported sighting is not of Vespa mandarinia on a scale of 0 to 1. A value 1 indicates that the sighting is not Vespa mandarinia and 0 indicates that the sighting is Vespa mandarinia. The following table presents the priority levels assigned to the probability deliverable:

<!-- b000565 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000566 | furniture | pages [23] -->
关注数学模型

<!-- b000567 | furniture | pages [23] -->
2

<!-- b000568 | furniture | pages [23] -->
MATHmodels

<!-- b000569 | furniture | pages [23] -->
获取更多资讯

<!-- b000570 | furniture | pages [24] -->
Team 2107870

<!-- b000571 | prose | pages [24] -->
Priority

<!-- b000572 | prose | pages [24] -->
Criteria

<!-- b000573 | prose | pages [24] -->
Level

<!-- b000574 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000575 | furniture | pages [24] -->
Page 22 of 23

<!-- b000576 | prose | pages [24] -->
assigned probability is greater than 0.8513531155306324 and less than Low

<!-- b000577 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000578 | prose | pages [24] -->
or equal to 1 assigned probability is greater than 0.5037355860727392 and less than Medium or equal to 0.8513531155306324 assigned probability is greater than or equal to 0 and less than or equal High to 0.5037355860727392

<!-- b000579 | caption | pages [24] -->
Figure 16: Priority Levels Table

<!-- b000580 | prose | pages [24] -->
To continue our ongoing partnership, we also propose a model for future use that assigns a proba- bility of a sighting being Vespa mandarinia based upon pest spread from past seasonal cycles. Such a model will be useful as more data on the location of positive sightings are collected.

<!-- b000581 | heading | pages [24] -->
OUR FINDINGS AND RECOMMENDATIONS

<!-- b000582 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000583 | prose | pages [24] -->
Our short term recommendations follow as such:

<!-- b000584 | prose | pages [24] -->
1. The most urgent locations that should be investigated are: Whatcom county, Skagit County, and San Juan County. After running our model on all the unveriﬁed and unprocessed data, these three counties scored the highest probability of being a Vespa mandarinia sighting.

<!-- b000585 | prose | pages [24] -->
2. Our short term logistical recommendation is that the Agricultural Department make great amend- ments to the civilian submission form. When preprocessing the initial data, our team had to remove many submissions because records contained incorrect dates and photos. The prepro- cessed notes suﬀered from noisy data because many submissions contained additional irrelevant description of possibly identifying Vespa mandarinia, but did not go into any details of what the alleged insect looked like. This makes distinction of ID increasingly diﬃcult. We suggest specifying on the form uploads of "Insect Photos" and "Vivid Description of Insect Seen" to curate better civilian data.

<!-- b000586 | prose | pages [24] -->
Our long term recommendations follow as such:

<!-- b000587 | prose | pages [24] -->
1. Investigation into high priority sightings (according to the Priority Levels Table above) should be emphasized most; however, this is not to say that a sighting with a low priority level is not Vespa mandarinia. It is simply less likely to be Vespa mandarinia than the other sightings. For this reason, some level of investigation into all of the priority levels should be allocated; however, the most urgent are the sightings in the high priority level.

<!-- b000588 | prose | pages [24] -->
2. Evidence of eradication of this pest in a region can be determined by this model when all of the reported sightings exist in the low priority level within a 30km radius of the region of interest for two Vespa mandarinia seasonal cycles (two years).

<!-- b000589 | prose | pages [24] -->
We appreciate your time and consideration and hope to expand upon this partnership to help ensure the ecological safety of the State of Washington in the future.

<!-- b000590 | prose | pages [24] -->
Sincerely, Team 2107870

<!-- b000591 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000592 | furniture | pages [24] -->
关注数学模型

<!-- b000593 | furniture | pages [24] -->
2

<!-- b000594 | furniture | pages [24] -->
MATHmodels

<!-- b000595 | furniture | pages [24] -->
获取更多资讯

<!-- b000596 | furniture | pages [25] -->
Team 2107870

<!-- b000597 | heading | pages [25] -->
References

<!-- b000598 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000599 | furniture | pages [25] -->
Page 23 of 23

<!-- b000600 | references | pages [25] -->
2.3. Clustering. url: https://rb.gy/kqg4bx.

<!-- b000601 | references | pages [25] -->
[1]

<!-- b000602 | references | pages [25] -->
微信公众号：数学模型

<!-- b000603 | references | pages [25] -->
Binary Cross Entropy. url: https://rb.gy/0dlvzz.

<!-- b000604 | references | pages [25] -->
[2]

<!-- b000605 | references | pages [25] -->
Jason Brownlee. A Gentle Introduction to the Rectiﬁed Linear Unit (ReLU). Aug. 2020. url:

<!-- b000606 | references | pages [25] -->
[3]

<!-- b000607 | references | pages [25] -->
https://rb.gy/rbdwcl..

<!-- b000608 | references | pages [25] -->
Jason Brownlee. Supervised and Unsupervised Machine Learning Algorithms. Aug. 2020. url:

<!-- b000609 | references | pages [25] -->
[4]

<!-- b000610 | references | pages [25] -->
https://rb.gy/wfcmao.

<!-- b000611 | references | pages [25] -->
Classiﬁcation on imbalanced data nbsp;: nbsp; TensorFlow Core. url: https://rb.gy/

<!-- b000612 | references | pages [25] -->
[5]

<!-- b000613 | references | pages [25] -->
02grv4.

<!-- b000614 | references | pages [25] -->
Paige Embry. How Mitochondrial DNA Oﬀers Clues to Giant Hornets’ Invasion. Nov. 2020.

<!-- b000615 | references | pages [25] -->
[6]

<!-- b000616 | references | pages [25] -->
url: https://rb.gy/27qs0p.

<!-- b000617 | references | pages [25] -->
Chollet François. Deep learning with Python. Manning Publications Co., 2018.

<!-- b000618 | references | pages [25] -->
[7]

<!-- b000619 | references | pages [25] -->
微信号：MATHmodels

<!-- b000620 | references | pages [25] -->
Implementing k-means Clustering with TensorFlow. June 2019. url: https://rb.gy/onthws.

<!-- b000621 | references | pages [25] -->
[8]

<!-- b000622 | references | pages [25] -->
Thenmozhi Kasinathan, Dakshayani Singaraju, and Srinivasulu Reddy Uyyala. Insect classiﬁ-

<!-- b000623 | references | pages [25] -->
[9]

<!-- b000624 | references | pages [25] -->
cation and detection in ﬁeld crops using modern machine learning techniques. Oct. 2020. url:

<!-- b000625 | references | pages [25] -->
https://rb.gy/jqp7as.

<!-- b000626 | references | pages [25] -->
Matt J. Keeling et al. Predicting the spread of the Asian hornet ( Vespa velutina ) following

<!-- b000627 | references | pages [25] -->
[10]

<!-- b000628 | references | pages [25] -->
its incursion into Great Britain. July 2017. url: https://www.nature.com/articles/

<!-- b000629 | references | pages [25] -->
s41598-017-06212-0.

<!-- b000630 | references | pages [25] -->
Michael J Michael J. Skvarla. Asian Giant Hornets. Jan. 2021. url: https://extension.

<!-- b000631 | references | pages [25] -->
[11]

<!-- b000632 | references | pages [25] -->
psu.edu/asian-giant-hornets.

<!-- b000633 | references | pages [25] -->
Hrishi Patel. Using K-Means Clustering for Image Segregation. June 2020. url: https://rb.

<!-- b000634 | references | pages [25] -->
[12]

<!-- b000635 | references | pages [25] -->
gy/dxbxpt.

<!-- b000636 | references | pages [25] -->
Jernej Puc. Semi-supervised learning in satellite image classiﬁcation. Feb. 2020. url: https:

<!-- b000637 | references | pages [25] -->
[13]

<!-- b000638 | references | pages [25] -->
//rb.gy/5plbhc.

<!-- b000639 | references | pages [25] -->
Python cv2.add() Examples. url: https://www.programcreek.com/python/example/

<!-- b000640 | references | pages [25] -->
[14]

<!-- b000641 | references | pages [25] -->
89358/cv2.add.

<!-- b000642 | references | pages [25] -->
Christelle Robinet, Christelle Suppo, and Eric Darrouzet. “Rapid spread of the invasive yellow-

<!-- b000643 | references | pages [25] -->
[15]

<!-- b000644 | references | pages [25] -->
legged hornet in France”. In: Journal of Applied Ecology 54.1 (June 2016). doi: https :

<!-- b000645 | references | pages [25] -->
//doi.org/10.1111/1365-2664.12724.

<!-- b000646 | references | pages [25] -->
Sumit Saha. A Comprehensive Guide to Convolutional Neural Networks-the ELI5 way. Dec.

<!-- b000647 | references | pages [25] -->
[16]

<!-- b000648 | references | pages [25] -->
2018. url: https://rb.gy/nxajwf.

<!-- b000649 | references | pages [25] -->
Sagar Sharma. Activation Functions in Neural Networks. Sept. 2017. url: https://rb.gy/

<!-- b000650 | references | pages [25] -->
[17]

<!-- b000651 | references | pages [25] -->
kvihlt.

<!-- b000652 | references | pages [25] -->
Zichen Wang. Practical tips for class imbalance in binary classiﬁcation. Jan. 2019. url: https:

<!-- b000653 | references | pages [25] -->
[18]

<!-- b000654 | references | pages [25] -->
//rb.gy/qtfmqx.

<!-- b000655 | references | pages [25] -->
Coding Packages Used: matplotlib, numpy, geopandas, pandas, scipy, seaborn, OpenCv, Open-

<!-- b000656 | references | pages [25] -->
Pyxl, numpy, statistics, os, glob

<!-- b000657 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000658 | furniture | pages [25] -->
关注数学模型

<!-- b000659 | furniture | pages [25] -->
2

<!-- b000660 | furniture | pages [25] -->
MATHmodels

<!-- b000661 | furniture | pages [25] -->
获取更多资讯
