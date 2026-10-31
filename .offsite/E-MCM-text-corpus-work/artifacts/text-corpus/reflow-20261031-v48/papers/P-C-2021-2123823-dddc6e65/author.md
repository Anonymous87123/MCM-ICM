MCM/ICM

Summary Sheet

Summary

With the fast rise of trade and tourism, invasive species have become a global concern. This paper aims to help the government make full use of the public reports to rationalize the deployment of limited resources to conduct investigations into the sparrow hornet.

For Problem (a), to predict the spread of the sparrow hornet, we construct a Combined Forecast Model. From the spatial perspective, factor analysis is used for variable selection (see Table 4.1) to measure the environmental suitability in a speciﬁed area. From the temporal perspective, we use K-means clustering on the three types of sightings (positive, unveriﬁed,

unprocessed) in diﬀerent months. The Gaussian mixture model (GMM) is applied to calculate the likelihood distribution of sparrow hornets in diﬀerent months. The combination of the two models illustrates the spread trend of hornets. The results show that Vs is less than 0.1 throughout the period, indicating our model’s high precision.

For Problem (b), we aim to predict the likelihood of misclassiﬁcation. First, we construct a Convolutional Neural Network (CNN) for image recognition and then carry out the text mining with an improved tf-idf model. Finally, we combine them for better estimation. The CNN predicts very well while the text mining can tell us the relative likelihood. After we combine these two methods, AUC(a measure of accuracy) increases by 1.08%.

For Problem (c), to prioritize investigation of the positive reports, we establish a compre- hensive model by combining the two models in Problem (a) and Problem (b), which is based on Regularized Logistic Regression. As a result of this model, we give more comprehensive judgments, with more than 99% accuracy.

For Problem (d), to update our model with new reports, pseudo labelling is introduced to utilize the unused (new) data. Compared with the result without pseudo labelling, AUC has increased to 0.96 by 2.13%. In terms of the appropriate update frequency, we use the subjective evaluation method to score each area based on ﬁve factors. Finally, we calculate the reporting frequency of a speciﬁc area based on its objective conditions and ﬁnd that the highest number of reports occurs in July and August (5.2/month).

For Problem (e), to determine the evidence of eradication in Washington, we use the regression model with longitudinal data to modify the model in Problem (a). The improved model’s advantage lies in its ability to predict changes in species populations with human intervention. We select local bee and sparrow hornet populations in 20 areas as samples. The state between two extreme points of the population curves indicates the eradication evidence.

At the very last, we analyze the strengths and weaknesses of our model as well as its sensitivity, whose results show that our model has high robustness, precision and accuracy. After that, a memo is attached.

belling; Regression model with longitudinal data

关注数学模型

1 Introduction

1.1 Background

Nowadays, biological invasions are a global concern in agriculture, food production and 微信公众号：数学模型 biodiversity. Invasive species have detrimental eﬀects on the newly colonized areas, such as impoverishment of local species assemblages, as well as the decline of critical insects providing herbivore control and pollination services [1].

The recent ﬁnding of Vespa mandarinia (Asian giant hornet) in Canada and the USA has prompted concern that it could become an invasive species. Until the Entomological Society of America decides on the oﬃcial common names for V. mandarinia, we are suggested to use ‘sparrow hornet’ [2]. Sparrow hornet tends to nest in low mountain foothills, lowland forests or green space in urban landscapes [3]. Sparrow hornet is a quarantine pest for the USA for it will cause a signiﬁcant loss to beekeepers [4]. Therefore, much care should be taken to predict the migration of hornets over time and identify manual reports to deploy government resources more eﬃciently to investigate the problem.

微信号：MATHmodels

1.2 Problem Restatement

(a) Develop a model to predict the sparrow hornet’s spread over time, and analyze the degree of precision of the model.

(b) Taking the look-alike species into account, study how to predict the likelihood of a mistaken classiﬁcation using only the data set ﬁle and (possibly) the image ﬁles provided.

(c) Set a goal for taking priority in investigating the reports that are most likely to be positive sightings, and discuss the way to conduct the classiﬁcation analysis.

(d) Address how to update the previous model using additional new reports over time, and determine the optimum frequency of new reports.

(e) Based on the model, ﬁnd out what would constitute evidence that the pest has been eradicated in Washington State.

1.3 Problem Analysis

For Problem (a), we plan to predict the spread of sparrow hornets from both spatial and temporal perspectives. First, the spread of hornets may be constrained by many natural factors, so we consider using factor analysis to calculate the environmental suitability, as this method is suitable for cases where data is not available or with low quality [5]; second, the spread may be aﬀected by seasonal and cyclical factors, so we can try to use clustering methods to determine the aggregation of hornets in diﬀerent periods.

For Problem (b), the data we can utilize are the reporters’ images and notes. We should make the most of them by statistical methods.

For Problem (c), to work out how to estimate the likelihood of reports being positive and prioritize investigation of them, we decide to consider all aspects of information involved above and establish a new evaluation model based on models we have applied in Problem (a) and Problem (b).

For Problem (d), pseudo labelling is an excellent way to improve the model accuracy when more unlabeled data are now available [6]; thus we want to use it to update our model based

关注数学模型 on the additional new reports. As the frequency of model updates is closely related to the frequency of report submissions, we need to determine an appropriate number of reports in a given period.

微信公众号：数学模型 For Problem (e), to determine whether the control measures have eradicated the pests, we can use the regression model with longitudinal data to modify the spread model by taking the changes of pest population with human intervention into account. With data on population changes after taking controlled measures, we can determine the point in time and evidence of pest eradication.

2 Assumptions and Justiﬁcations

To simplify our problems, we make the following basic assumptions, each of which is adequately justiﬁed.

(a) In each month, the number of clustering centers of sparrow hornets is positively correlated with their activity level, reaching a peak in July and August.

微信号：MATHmodels (b) The activity period of sparrow hornets was from April to October of year. During other times, the sparrow hornets were in hibernation. The events of sparrow hornets found by the public during these limited periods can be considered unreliable and ignored.

(c) The ethnic inﬂuence of sparrow hornets is normally distributed over distance.

(d) The environmental suitability of the same area is generally consistent from year to year.

3 Notation

Symbol Description

N(x, ui, di) The probability density function of the i-th Gaussian model P(x) The likelihood of sparrow hornets appearing in the position x πi weight of the i-th Gaussian model β Weight of Model 2 Vs coeﬃcient of variation c Term frequency P(Neg) Likelihood of negative things P(Pos) Likelihood of positive things P The actual number of positive reports N The acutal number of negative reports θ Regression parameters λ regularization coeﬃcient bk Fixed eﬀect factor ηki Random eﬀect factor

关注数学模型

4 Analysis and Modelling

4.1 Spread of sparrow hornet over time

After analyzing the provided data set, we can ensure that the spread of sparrow hornet is 微信公众号：数学模型 predictable.

Understanding the role of biotic (species ecology, predation and interspeciﬁc competition) and abiotic (anthropogenic role, climate change, geographical barriers) factors has become the major challenge in ecology and biogeography. In this problem, however, we rely on abiotic variables because little is known about other biotic factors, such as species evolution, predators and competitors, which may aﬀect the location of sparrow hornet [7].

微信号：MATHmodels

4.1.1 Data Preprocessing

We ﬁrst weed out events where the date is incorrectly formatted though the number of these events is small. We screen out the data before September 2019. This is because sparrow hornets were ﬁrst found in Sep. 2019 in Vancouver Island, and in Dec. 2019 in Washington State. So any report before Sep. 2019 is certain to be negative; For each year, we select the data from April to October. According to reference [8], sparrow hornets will go through hibernation outside this interval. So reports from Apr. to Oct. are much more meaningful and valuable.

4.1.2 Model 1: Factor Analysis Method

The basic idea of factor analysis is to group variables according to the correlation so that variables are more correlated within the same group and less correlated in diﬀerent groups. Each group of variables represents a basic structure, which is referred to as a common factor. So it is possible to describe each component of the original observation in terms of a linear function of unmeasured common factors and the special factors.

The factor analysis can be expressed in the following model:

In which, x1, x2, . . ., xp mean p standardized variables with a mean of 0 and a standard deviation of 1, F1, F2, . . ., Fm refer to m factor variables. Moreover, this model can be translated into the form of the matrix.

X = AF + aε

关注数学模型 in which, F is the common factor; A is the factor loading matrix, which is the loading of the i-th original variable on the j-th factor variable; aij is the projection of xi onto the coordinate axis Fj if the variable xi is viewed as a vector in an m-dimensional factor space; ε is the special factor, indicating the part of the original variable that cannot be explained by the factor variables 微信公众号：数学模型 (which can be thought of as the residuals in a multiple regression model).

Results of Model 1

Environmental suitability is deﬁned as the conditional probability of occurrence of a species given the state of the environment at a location [9]. Many abiotic drivers determine sparrow hornet colonies distribution. For instance, the abundance of sparrow hornets is positively associated with green spaces in urban landscapes [3]. On the other hand, sparrow hornet has been described as a species highly sensitive to heat and extreme climate conditions, and negatively associated with high temperatures [10]. As a result, we consider as many documented or relevant impact variables a as possible when carrying out the factor analysis, in order to adequately estimate the environmental suitability of the Northwest United States. Finally, 16 variables that can explain sparrow hornet current distribution are selected.

微信号：MATHmodels

Classiﬁcation Factor Abbreviation Annual mean temperature (◦C) T_m · · · Climate Annual mean radiation (MJ/m2) R_m Forest stands (%) H_for · · · Habitat structure Scrubland (%) H_scr Vegetation productivity Normalised diﬀerence vegetation index HDVI Average distance to rivers (m) Hydrography Dist_riv Elevation (m) Topography Elv Human activity Average population D_pop

At last, values of all the variables are converted into z-score.

It can be seen from the cumulative percentage of variance that the ﬁrst four principal components already explain nearly 87.9% of the total variance, so these could be selected for analysis. The scree plot on the right illustrates that the fold’s slope is steeper for the ﬁrst four principal components. However, it tapers oﬀlater, which is another evidence that it is appropriate to take the ﬁrst four principal components.

aData Source: Climatic variables are retrieved from the Weather Atlas (https://www.weather-us. com). The website Elevations and Distances in the United States (https://pubs.usgs.gov/gip/ Elevations-Distances/elvadist.html) is used to gather topographic data. The data of vegetation pro- ductivity and hydrography can be obtained from http://glovis.usgs.gov/. Anthropogenic drivers such as population are derived from the Census Bureau (https://www.census.gov/).

关注数学模型 微信公众号：数学模型

Next, we apply the formula Y = Zx × t, where Zx is the normalized matrix and t is the normalized orthogonal eigenvector matrix to obtain the values of the four principal components. Based on the percentage of variance in Figure 4.2 for the weighting, we can calculate the overall score and the environmental suitability of 14,260 selected points.

Ytotal = 0.50196Y1 + 0.18929Y2 + 0.11459Y3 + 0.07326Y4 ES = 500 + 100Ytotal 微信号：MATHmodels From the two ﬁgures below, we can see that the USA and Canada’s western coasts are ideal for the survival of hornets. A second peak occurs in and around the North Cascades National Park on the Rosario Strait’s east coast. The Kootenay National Forest in the interior is the third best place for hornets - although not as suitable as the coastal areas, the environmental suitability has been primarily maintained at around 300. By comparison, we can see that ’ high-scoring’areas all share some common and distinctive characteristics, such as high forest cover and NDVI, proximity to water sources, low human presence etc. These ﬁndings are consistent with the habits of sparrow hornets recorded in related research material [3] [10], so we consider the level of environmental suitability calculated by factor analysis is convincing to some extent.

ronmental suitability

4.1.3 Model 2: K-means clustering algorithm and Gaussian Mixture Model

In Model 2, considering that the sparrow hornets live in groups and are distributed around the queen, we ﬁrst thought of applying the K-means clustering algorithm to ﬁnd the sparrow hornets’ cluster centres. When applying the K-means clustering algorithm to ﬁnd the clustering centers, we, in order to improve the reliability of the data, directly delete the data judged as "Negative ID" and use the remaining part.

According to the reference [8], sparrow hornets’ growth can be divided into six stages, and

关注数学模型 we correspond to months to determine the number of clustering centers in each month. We preset more clustering centers in the months when sparrow hornets are active. The speciﬁc settings have been shown in the ﬁgure below.

微信公众号：数学模型

Since the initial point selection of the K-means algorithm is random, this algorithm may fall into a local optimal solution instead of a global optimal solution. To avoid this situation, 微信号：MATHmodels we calculate many times and ﬁnd the situation with relatively good output as the global optimal solution. Based on the processed data, we ﬁnally used the K-means clustering algorithm to ﬁnd the clustering centers’ location in each month and calculated the categories of each event. The results are shown in Figure 4.6.

After getting each cluster center’s position and the number of ethnic groups in each month, we began to apply the Gaussian mixture model to calculate the likelihood distribution of sparrow hornets in various places within the speciﬁc geographic area.

Let us brieﬂy introduce the Gaussian mixture model. The Gaussian mixture model uses the Gaussian probability density function (normal distribution curve) to quantify things accurately. It is a model based on Gaussian probability density function (normal distribution curve) that decomposes things into several.

The mixed Gaussian model consists of K Gaussian models (that is, the data contains K clustering centers). The probability density function of GMM is as follows:

K K ∑ ∑ p(i)p(x|i) = p(x) = πiN(x, ui, di) i=1 i=1

关注数学模型 where x represents the position of the sample, represents the likelihood of sparrow hornets appearing in the position x, p(x|i) = N(x, ui, di) represents the probability density function of the i-th Gaussian model, and ui, di, πi represent the mean, standard deviation and weight of i-th Gaussian model respectively. πi is proportional to the number of ethnic group members, and 微信公众号：数学模型 ∑ K πi = 1. The greater the number of ethnic group members, the greater the inﬂuence, which i=1 is very reasonable.

In our model, the probability of sparrow hornets appearing in various places within a speciﬁc geographic area is aﬀected by multiple cluster centers in this area. The change curve of this eﬀect with distance is the probability density curve of the normal distribution.

Results of Model 2

We calculate the likelihood of sparrow hornets appearing everywhere in a speciﬁc geographic area in each month, rescale it between 0 and 1, and ﬁnally draw a contour map in Figure 7(a).

4.1.4 Combined Forecast Model

微信号：MATHmodels Model 1 calculates the environmental suitability according to the region’s natural conditions and scales it to between 0 and 1 to obtain the likelihood distribution of sparrow hornets. Model 2 predicts the likelihood distribution of sparrow hornets in diﬀerent months based on the existing data of the distribution of sparrow hornets. And then we combine the results of these two models at a ratio of 1 : β. In this part, let us set β = 1. Furthermore, we will study how to select its value in Sensitivity Analysis. Finally, we obtained the likelihood distribution of sparrow hornets in diﬀerent months in recent years, as shown in Figure 7(b).

Since the K-means clustering algorithm results are not necessarily consistent each time it runs but are similar, this causes the results obtained by our ﬁnal model to ﬂuctuate within a speciﬁc range. Therefore, we need to calculate the precision of our model predictions. Our deﬁnition of precision is the degree of error in the prediction results of the comprehensive prediction model, which corresponds to the magnitude of the error. Therefore, we use the coeﬃcient of variation Vs to reﬂect the level of precision. The smaller the coeﬃcient of variation Vs, the smaller the variation range of the prediction results, which means the higher the precision level. The calculation of the coeﬃcient of variation is as follows where σ and ¯X represents standard deviation and average of data X.

Vs = σ (4.1.1) ¯X

(a) results of Model 2 (b) results of the combined model in Problem (a)

We calculated the coeﬃcient of variation of outputs predicted by month. From Figure 4.8,

关注数学模型 we can ensure that our model’s precision is high enough to estimate the likelihood.

微信公众号：数学模型

4.2 Prediction of Mistaken Classiﬁcation

After inspection of the given spreadsheet, we ﬁnd that most reported sightings are identiﬁed as mistaken ones. Hence, in this part, we are to establish a model to help predict the likelihood of a mistaken classiﬁcation.

微信号：MATHmodels N.B. We may call something such as a report, a ﬁgure, a note or even a word, as ‘positive’ or ‘negative’ in the following. This means its corresponding ‘Lab Status’ is positive or negative.

4.2.1 Model 3: Image Recognition Based on CNN

Data Preprocessing While the given data was cleaned in the last part, it still shows a severe imbalance of the data distribution, in that, there are 2028 negative reports versus only 14 positive ones. This is not good for the following learning of sparrow hornets’ features.b We come up with two approaches to solve this. For one thing, we increase the number of positive samples. In detailc,

• we ﬂipp the positive ﬁgures vertically and horizontally to triple its number;

• we download some ﬁgures from reliable websites.d

For another, we decreased the number of negative samples. In detail, we randomly selected some of them, making its number equal to positive ones.

Through preprocessing, now there are 258 positive samples and 258 negative ones. We mix them uniformly and split them by the ratio of 7 to 3 for training and test.

As to the targets, we label the positive and negative target as 1 and 0 respectively, denoting the likelihood of a positive target. Finally, there are 411 training samples & targets and 177 test samples & targets.

Convolutional Neural Network Convolutional neural networks(CNN) have played an im- portant role in the history of deep learning, especially in object recognition. For instance, they

bActually we had once attempted to use all of them to train our model. It was found that the model was inclined to predict all the samples as negative regardless of the real targets.

cResizing and normalization are also incorporated in preprocessing. They are not mentioned in the main body since they made no contributions to the increase of positive samples dData Source: Asian Giant Hornet(https://en.wikipedia.org/wiki/Asian_giant_hornet), Get to know the Asian giant hornet, or ’murder hornet’(https://agrilifetoday.tamu.edu/2020/05/11/ get-to-know-the-asian-giant-hornet-or-murder-hornet/)

关注数学模型 were used to win many contests, including the ImageNet object recognition challenges [11]. So here we establish a CNN for preliminary prediction.

微信公众号：数学模型

We construct our CNN with PyTorch. The architecture of the network is displayed in Figure 4.9(drawn with TikZ). There are two convolutional layers, two pooling layers and two fully 微信号：MATHmodels connected layers. The shape of the input is (b × 3 × 96 × 96), where b denotes the batch size, 3 denotes the number of channels, and 96 × 96 are the height and width. The shape of the output is (b). Train for 200 epochs.

The test accuracy reaches its peak of 0.8968 at the 93rd epoch. The model at this epoch is saved as the ﬁnal predictor. We plot the ROC Curve in Figure 4.4.10. The horizontal and vertical axes are the false positive rate (FPR) and true positive rate (TPR). AUC denotes the Area Under ROC Curve. A model with AUC closer to one shows better performance in prediction. Now our model’s AUC equals to 0.93. With only 411 training samples, this result is quite acceptable.

4.2.2 Model 4: Text Mining in the Level of Words and Sentences

The given data set also includes some notes attached by the reporters, which are not to be ignored. We have just modelled the prediction of P(Pos) and P(Neg) based on images, while these notes are also thought to be helpful to our prediction.

In information retrieval, tf–idf, short for term

Introduction of the improved tf-idf model

frequency–inverse document frequency, is a numerical statistic that is intended to reﬂect how important a word is to a document in a collection or corpus [12]. Such a model is made up of two parts literally.

Term frequency, i.e., cw, is the number of times a term w occurs in a document, while inverse document frequency is a measure of how much information the word provides, i.e., if it’s common or rare across all documents. In most cases, a term with a higher cw tends to contribute more to the document. Nevertheless, a stopword like ‘the’ or ‘I’m’ can hardly give us any information.

This inspires us to estimate the ‘positive’ likelihood of each word, viz., Pw(Pos) according to its cw. What is diﬀerent here is about ‘Lab Status’. For instance, a ‘negative’ word will contribute inversely to the note. So we suggest an improved tf-idf model according to its cw considering the Lab Status.

关注数学模型 Data Preprocessing & Qualitative Analysis We continue using the data from Sep. 2019. For each note, eliminate the stopwords e. Then we group these notes by its Lab Status. Furthermore, we quantify Lab Status in the form of P(Pos).

微信公众号：数学模型 For ‘Positive ID’, Ppos(Pos) = 1. For ‘Negative ID’, Pneg(Pos) = 0. For ‘Unveriﬁed’, Puv(Pos) = 0.5, because even oﬃcial specialist cannot identify it. Also, a matter with the P likelihood of 0.5 is hardest to predict. For ‘Unprocessed’, Pup(Pos) = P + N , where P and N denote the actual number of positive and negative reports separately. This is because it has not been classiﬁed rather than be unable to be classiﬁed. So we use the mathematical expectation as P(Pos).

Let n, p, up, uv represent the number of the four kinds of reports mentioned above in order. We will have these two equations.

N N = n + up × N + P + 0.5 × uv (4.2.1)

P P = p + up × N + P + 0.5 × uv (4.2.2) 微信号：MATHmodels Solve the simultaneous equations and we can obtain the value of N and P.

T = N + P = n + p + uv + up = 4440 N = n + uv/2 P = T −N = 1189 1 −up/T = 3251,

After ﬁlling P(Pos) for each note, we create the word clouds of positive notes and negative notes. This can reﬂect a word’s ‘positive’ or ‘negative’ attribute qualitatively.

(a) for positive ones (b) for negative ones

The word ‘hornet’ often appears both in positive and negative notes, which can be easily explained by the creature’s name. Additionally, the word ‘wsda’ is conspicuous in the positive word cloud. This may be because the notes including ‘wsda’ are submitted by WSDA or its staﬀwith more knowledge about the sparrow hornet.

For a ‘Lab Status’ i, Pi(Pos) can be regarded as a sort of score. We

Modelling of a Word

can grade each word except stopwords.

Now let us set the grading rule. If a word w appears ci times for status i, it will get a score of ci × Pi(Pos). The ﬁnal score is calculated by adding four scores together. This score have

eThe stopwords are provided by the corpus of Python’s Natural Language Toolkit

关注数学模型 no upper limit. So we divide it by the total times it appears, i.e., ∑ i ci(w). We deﬁne this value as Pw(Pos). Apparently, Pw(Pos) is between 0 and 1.

∑ cw(i) × Pi(Pos) 微信公众号：数学模型 def i ∑ === i ∈{pos, neg, uv, up} Pw(Pos) , (4.2.3) cw(i) i

If we rewrite Eq. 4.2.3 as

∑ cw(i) ∑ Pi(Pos) × i ∈{pos, neg, uv, up} Pw(Pos) = cw(i), (4.2.4) i i

cw(i) ∑ then Pw(Pos) is the weighted mean of Pi(Pos), whose weight equals cw(i).

i

Modelling of a Note

A note is composed of several words. Thus the positive likelihood 微信号：MATHmodels of a note, viz., Pn(Pos) is also a composition of Pw(Pos). It is found that some words like ‘Manson’ and ‘incident’ only appears once, rendering them much less reliable for the positive likelihood. In this sense, they should contribute less to Pn(Pos). This means Pn(Pos) is positively correlated with a word’s term frequency, cw. Based on the above, we deﬁne Pn(Pos) as  ∑ w∈Sn ln cw × Pw(Pos)    ∑ , Sn̸ = ∅; w∈Sn ln cw def === Pn(Pos) (4.2.5)  P   , Sn = ∅. P + N where Sn is the set of all words in the note n. As mentioned in the last part, the data distribution show a severe imbalance between negative and positive ones. So if a note is not empty, we will take a logarithm of cw to bridge the gap. However, there also exist some reports without notes. In this case, we choose the mathematical expectation as their value.

With this deﬁnition, let us recalculate the positive likelihood of each note. Notes are grouped by ‘Lab Status’(marked as G1, G2, G3, G4). The distribution of each group’s Pn(Pos) is shown in Figure 4.12. The subtitles represent the means of Pn(Pos).

In general, G1 has the greatest mean Pn(pos) and G2 has the least mean Pn(Pos), which is consistent with reality. But the maximum of G1’s Pn(Pos) is less than 0.5. This is normal

关注数学模型 for that many words appearing in positive notes also appear in negative ones. Moreover, the N N + P is 0.262045. So it can be seen that both G2 and G3 have a spike calculated value of when Pn(Pos) ≈0.26, which can be attributed to their ‘empty’ notes.

微信公众号：数学模型 To check the eﬀect of the logarithm, we compare the distribution of G1’s Pn(Pos) con- sidering logarithm and without it. The latter corresponding formula for a non-empty note is  ∑ w∈Sn cw × Pw(Pos)    ∑ , Sn̸ = ∅; w∈Sn cw def P ′ === n(Pos) (4.2.6)  P   , Sn = ∅. P + N

increased from 0.301 to 0.326 by 8.31%. Thus Deﬁnition 4.2.5 proves to be more reliable than Deﬁnition 4.2.6.

微信号：MATHmodels (a) Using Deﬁnition 4.2.6 (b) Using Deﬁnition 4.2.5

4.2.3 Combination of Image Recognition and Text Mining

Although our improved tf-idf model predicts worse than the CNN, the relative likelihood is accurate. Furthermore, it measures a report from a diﬀerent aspect. In this sense, we can combine these two models to increase the accuracy of prediction.

We plot the distribution of the prediction results in Figure 4.14. The two histograms diﬀer signiﬁcantly in shape, which is not suitable for linear combination. In this case, we turn to combine them in a nonlinear form.

for training data

In order ro represent the contributions of the images and the notes, we introduce the coeﬃcient C1 and C2 as their exponents. The general form is as below.

ln ˆP(Pos) = ln m × {k × [Pim(Pos)]C1 × [Pn(Pos)]C2 + b} (4.2.7)

关注数学模型 By ﬁtting the training data, the values of the coeﬃcients are

m = 0.6489, k = 0.0956, C1 = −39.3, C2 = −4.4, b = −3.806

微信公众号：数学模型 C1 is nearly nine times larger than C2, which tells us the result depends much more on the image than the textual part. This is also consistent with Figure 4.15, where actual positive points only appear when Pm(Pos) is greater than 0.9.

We calculate the result of the test samples and display the distribution in Figure 4.16. The value of AUC is increased to 0.94 by 1.08%.

微信号：MATHmodels

sult’s distribution for test data in Problem (b)

4.3 Determine the likelihood of a Positve Report

Based on the work above, we intend to integrate these two models through Regularized Logistic Regression to improve prediction accuracy.

Regularized Logistic Regression We take the likelihood of sparrow hornets appearing obtained by the two models in Problem (a) and (b) as input values, respectively marked as pab1 and pab2, and the actual likelihood is the output value, which is marked as y. The data set we select refers to the events that provide the picture and are judged as positive or negative, where Positive ID corresponds to 1, and Negative ID corresponds to 0. Then we randomly divide this data set into the training set and test set.

Before training, considering the input only has two features, we need to apply the feature mapping method to expand the two features into 28 features.

mapFeature(pab) = [1, pab1, pab2, p2 ab1, pab1pab2, p2 ab2, · · · , p6 ab2]T

where pab andmapfeature(pab)respectivelyrepresentsthe2-dimensionalvectorand28-dimensional vector.

After that, we started to train the model on the training set. The cost function J(θ) is calculated as follows.

1 hθ(pab) = 1 + e−θT pab m n ∑ ∑ J(θ) = 1 ab ))] + λ [−y(i) ln(hθ(p(i) ab )) −(1 −y(i)) ln(1 −hθ(p(i) θ2 j m 2m i=1 j=1

关注数学模型 where θ represents regression parameters, λ represents the regularization coeﬃcient, which we set as 0.6. When the cost function J(θ) is the smallest, the regression eﬀect is best, and the regression model can be considered the ﬁnal model.

微信公众号：数学模型

Results and Analysis

To evaluate our model, we test this new model’s accuracy on the test set. The ﬁnal predicted result matches the real situation perfectly.

Analyzing the predicted results, we found that even though there were two misjudgments in the event, the overall accuracy rate has reached 0.99, which shows that our model is reliable. Therefore our model is helpful to determine the likelihood of positive reports positive and prioritize investigation of them.

微信号：MATHmodels

4.4 Update of the Model

Although the CNN in section 4.2.1 has a relatively high accuracy of 0.8969, it can be furtherly improved due to a great deal of new data, especially from the additional new reports. Through pseudo labelling, we are now able to make use of the unexploited data.

Pseudo labelling is the process of using the labelled data model to predict labels for un- labelled data. It is often used in semi-supervised learning, where most data are unlabelled. Nowadays, this technique is used for hyperspectral image classiﬁcation and the identiﬁcation of COVID-19 on chest X-rays. [11][12] Based on image recognition results of CNN, we will use pseudo labelling to improve our model. The procedure is shown in the ﬂow chart below. (Figure 4.9)

4.4.1 Model 3*: Improved CNN With Pseudo Labelling

Pseudo labelling is the process of using the labelled data model to predict labels for unlabelled data. It is often used in semi-supervised learning, where most data are unlabelled. Nowadays, this technique is used for hyperspectral image classiﬁcation and the identiﬁcation of COVID-19 on chest X-rays [13][14].

Based on image recognition results of CNN, we will use pseudo labelling to improve our model. The procedure is shown in the ﬂow chart below. (Figure 4.19)

Because additional data from Washington state on Asian hornets similar to what was provided in the spreadsheet is explicitly not allowed in Problem (c), we add the unlabeled data (unveriﬁed and unprocessed) that were not originally in the training set as "new report data" to this model, which can help us test whether additional new reports will improve our model. We reckon that the precision of the value of P(Pos), which is farther away from 0.5 is more reliable and convincing. Therefore, we only label the predicted result which is either

关注数学模型 larger than 0.9 or less than 0.1. To check this, we visualize some of the prediction results of unveriﬁed images in Figure 4.21.

微信公众号：数学模型

belling

微信号：MATHmodels The 1st and the 3rd ﬁgures’ values of P(Neg) are below 0.1, showing they are likely to be positive sightings. We can compare them with a real sparrow hornet in Figure 4.20. They are very similar to the three typical characteristics of a real hornet’s appearance. Therefore, such prediction is relatively reliable and can be labelled as (pseudo) positive.

After pseudo labelling, we include them into the original labelled dataset and retrain our CNN obtained before. At the 7th epoch, test accuracy reaches a higher peak of 0.9096, which has increased by 1.43% compared to previous 0.8968.

Compared with the result before pseudo labelling, the value of AUC has increased to 0.96 by 1.08%. The result demonstrates the eﬀectiveness of improving our model by setting the new report as a pseudo label added to the training model.

4.4.2 Subjective Evaluation Method

The key to solving an appropriate frequency of model updates lies in determining an appropri- ate number of reports in a given period. As a result, we use the subjective evaluation method to score each area based on diﬀerent factors closely correlated with the emergence of potential reporting cases. We ﬁnally select ﬁve key evaluation indicators for analysis: environmental

关注数学模型 suitability (1), seasonal factors (2), major external events (3), economic development (4), and reporting stability (5). The ranking results of importance are as follows.

I2 > I3 > I1 > I4 > I5 微信公众号：数学模型 The speciﬁc scoring rules are: each area’s score consists of two parts (initial score and additional score), where the initial score is dependent on the environmental suitability of this area, and other four factors determine the additional score. The area’s score is updated every day until the threshold (e.g. 100) is reached, which means that the area should submit new reports at this point. Then, all the scores of this area are cleared, and the scoring starts again. According to the data we have, we estimate there will be a report submitted from this area in almost six days, which also indicates that 17 points need to be added in average per day on a 100-point scale. After distributing the ﬁve factors’ weights, the initial score (IS) formula is as follows. ESi ISi = 17 × Weight3 × , i = 1, 2, . . . , 63 MedianES 微信号：MATHmodels in which Weight3 means the weight of the third factor (environment suitability) and 63 refers to the total number of the areas in Washington State.

There are also some rules regarding the determination of additional score:

(a) Seasonal factors require diﬀerent additional scores in diﬀerent months in the same area.

We will consider the number of clustering centers (NCC) in Model 2 as a determinant of the additional score. Its formula is as follows.

NCCj ASaj = 17 × Weight1 × , j = 1, 2, . . . , 12 MedianNCC

(b) The impact of major external events is mainly reﬂected in the fact that when a positive sighting occurs in the region, the area’s daily additional score can be set to 125% of the initial score for the next six months. (This eﬀect can be stacked)

(c) The higher the level of economic development in the area, the higher the frequency of reporting. The following equation can express this relationship.

GDPi ASci = 17 × Weight4 × , i = 1, 2, . . . , 63 MedianGDP

(d) Reporting stability can be positively correlated with the duration of consistently negative reports for the area. Speciﬁcally, suppose an area has more than six months of consecutive negative reports recorded. In that case, the additional value is −50% of its initial value from the sixth month until a positive record occurs in the area.

Let us consider a speciﬁc example. Suppose there is a circular area A with a radius of GDPA 30km. In this area, MedianGDP = 1.2 and the expected environmental suitability is 84 (median is 115 in the whole state). Moreover, we assume that it is now at the beginning of May. It is also important to note that there was one positive case reported in the region at the end of April. The current estimate is that there will be no further positives in the area for six months after that.

关注数学模型 By considering the various factors in our evaluation model, we conclude that the monthly reportable quantity in Region A varies over time in the next eight months, with the highest in July and August (5.2/month) and the lowest in November and December (1.3/month).

微信公众号：数学模型

4.5 Evidence of Eradication in Washington State

Eradication is deﬁned as eliminating every individual of a species from an area to which recolonization is unlikely to occur [15]. There are various ways to eradicate the sparrow hornet recommended by the United States Department of Agriculture (USDA). For instance, we can use lethal traps during the early (pre-nesting and solitary stages) and late seasons (reproductive stage) to kill queens, or take a proactive approach to ﬁnd and eliminate nests during the middle seasons (cooperative and polyethic) [16]. As a result, judgements about the eﬀectiveness of eradication will directly determine the extent to which diﬀerent methods can be applied in diﬀerent areas.

4.5.1 Regression Model With Longitudinal Data

Some relevant literature reveals that invasive hornets are particularly problematic due to the 微信号：MATHmodels adverse impact on local bee assemblages [4]. So when constructing the model to evaluate eradication eﬀectiveness, we mainly focus on two crucial factors - changes in the population of local bees and sparrow hornets in a given area over time. According to our hypothesis, the local bee population theoretically shows an increase followed by a decrease during the control process. In contrast, the invasive hornet population shows the opposite trend, with a decrease followed by an increase. Given this, we can model a quadratic regression of density on time:

yij = b0i + b1itij + b2it2 ij + εij, i = 1, . . . , n, j = 1, . . . , ni (4.5.1)

where yij means the density of local bees (or sparrow hornets) of the j-th observation at the i-th site, and tij refers to the time point of the j-th observation at the i-th site; n is the number of sites where the invasive species occur, and ni is the number of observations at the i-th site during the whole period.

Based on the above, the quadratic regression model above is rewritten using a mixed model to highlight the area’s overall density data. A mixed-eﬀects model is a statistical model containing both ﬁxed eﬀects and random eﬀects [6].

bki = bk + ηki, k = 0, 1, 2 (4.5.2)

in which bk is the ﬁxed eﬀect factor for the whole area (not related to the observation site),

Report Fre-

quency Assessment Form

关注数学模型 while ηki is the random eﬀect factor varying with the observation site. The random eﬀect factor is assumed to obey normal distribution with a mean of zero and constant variance of d2 k, and be independent of each other.

微信公众号：数学模型 Substituting Eq. 4.5.2 into Eq. 4.5.1 yields a regression model with longitudinal data.

yij = b0 + b1tij + b2t2 ij + η0i + η1itij + η2it2 ij + εij (4.5.3)

It can be rewritten in the form of the matrix.

    t2 yi1 1 ti1     i1 d2 b0 0 0  ,  , t2 yi2 1 ti2 1 i2  ,   d2 b1 0 0 Yi = Xi = b = D = ... ... ... ... 2 d2 b2 0 0 3 t2 yini 1 ti3 i3

Vi = XiDXT i + σ2I 微信号：MATHmodels in which Yi is assumed to obey normal distribution with a mean vector of Xib and variance matrix of Vi. The estimation of the coeﬃcients requires the application of Maximum Likelihood Estimation (MLE), instead of Original Least Squares (OLS) for it cannot handle cases where the model is not linear. The likelihood function for Yi is given as follows.

n ∏ 2 exp[−1 {(2π)−ni 2 |Vi|−1 2(Yi −Xib)TV −1 L(b, D, σ2) = (Yi −Xib)]} i i=1

Finally, by solving the maximum point of the likelihood function L, the estimated values of b, D and σ2 can be calculated.

The model’s signiﬁcance is that the ﬁxed eﬀect coeﬃcient bk, which reﬂects the overall eﬀect in the area, can predict the time point of eradication in an average sense. In contrast, the random eﬀect coeﬃcient ηki incorporates the variability between diﬀerent sites (e.g. climate, topography, population), thus assessing the conﬁdence interval of time point of eradication under a certain level.

Results and Analysis

To determine the local bee population, we use data from the National Agricultural Statistics Services of the USAf, which reports the number of colonies per county where the honey was harvested. To get the valid data on the spread of hornets under controlled conditions, we modify the spread model mentioned in section 4.1 using the regression model with longitudinal data. The period of the controlling process is chosen from April (queens ﬁrst appear) to October (soon to be hibernating)

Next, we randomly select 20 areas and predict local bee and sparrow hornet populations’ changes over time after some control measures are taken. Figure 4.24 shows the situation of local bees in three of these areas.

fData Source: the National Agricultural Statistics Services of the USA(https://quickstats.nass.usda. gov/results/98D6C754-2F7A-319C95FE-CB8F673A140E)

关注数学模型 微信公众号：数学模型

We can plot the model results (Figure 4.25) by testing the model with the hypothetical data. When t = 6.83, the sparrow hornet population in the 20 areas of Washington will reach the minimum point with roughly 1; when t = 7.46, the local bee population in these areas will reach the maximum point with approximately 241. Therefore, we can conclude that when the time range is from 6.83 to 7.46, the number of local bees is not less than 240. The number of hornets is not higher than 1, which indicates that the pest has been eradicated in these 20 areas of Washington State. The model can also be used for calculations for other areas of the 微信号：MATHmodels state.

5 Sensitivity Analysis

In our model, the changes of several values may signiﬁcantly impact the model’s results, so we need to analyze them one by one.

5.1 Model’s Sensitivity in Problem (a)

In order to analyze the sensitivity of the weights of Model 1 and Model 2, we select diﬀerent values of β to calculate the precision of the Combined Forecast Model. We select each element in the set {0.1, 0.3, 0.6, 1, 3, 6, 10} in sequence as the value of β. The boxplot is showed below.

It can be concluded from the ﬁgure above that β has little eﬀect on the prediction precision of our model, which shows that our model is robust and very reliable.

关注数学模型

5.2 Model’s Sensitivity in Problem (c)

To test the inﬂuence of the value change of the regularization coeﬃcient λ, we pick diﬀerent values of λ and predict the likelihood distribution of sparrow wasps appearing. The predicted 微信公众号：数学模型 result is shown in Figure 5.2.

When λ changes within a certain range, the accuracy of our model prediction is stable above 90%. When λ increases over 10, the prediction accuracy of the model drops rapidly. When 微信号：MATHmodels lambda is equal to 0.6, our model can achieve the best prediction.

6 Model Evaluation

Strengths:

• Comprehensive consideration: We have predicted the spread of the sparrow hornets from both temporal and spatial perspectives, and selected 16 factors to calculate the environmental suitability. Almost every useful factor has been included in Model 1. (see Section 4.1)

• Full utilization of information: When evaluating the likelihood distribution of sparrow hornets, we have applied the feature mapping method to expand the 2 features into 28 features, making the most of the features of limited data. (see Section 4.3)

• Sophisticated model improvement method: Through pseudo labelling, we are able to make use of unexploited data, which can help improve the accuracy of the original prediction model. (see Section 4.4)

Weaknesses:

• Insuﬃcient data volume: The ratio of positive to negative reports is too extreme. Al- though we have taken some measures (e.g., ﬂipping the images horizontally and vertically to increase the amount of data) to reduce its negative impact on the training set, we could not eliminate it completely;

• Subjective error: When calculating the update frequency, we apply a subjective evalua- tion method to assign weights to ﬁve factors , which is reasonable to some extent but not accurate enough. (see Section 4.4)

关注数学模型

Memorandum

To: The Washington State Department of Agriculture 微信公众号：数学模型 From: Team # 2123823

Subject: Prediction of the Spread of Sparrow Hornets

Date: February 9, 2021

Dear Sir:

With the growth of trade, transportation and tourism under globalization, the introduction of sparrow hornets is now one of the greatest threats to the ecological system of Washington State. In our work, we have built a series of models in hope to help the government make full 微信号：MATHmodels use of the data provided by the public reports to rationalize the deployment of limited resources to conduct investigations.

Analyzing the result predicted, we have many important discoveries and advice, which can help you signiﬁcantly improve the eﬃciency of the investigation.

i) Focus on the events occurring in the areas with a high likelihood of sparrow hornet appearing, and prioritize investigation of these events. Comparing the environmental suitability between diﬀerent areas, we ﬁnd that there are three area centers ‘friendly’ to sparrow hornet: the ﬁrst is the northwestern coastal region of the United States; the second is the North Cascades National Park and its vicinity on the east coast of the Rosario Strait; the third is the Kootenay National Forest in the interior. Over time, sparrow hornets will migrate to these three area centers. Then combine with the data of the current year, we can accurately predict the distribution of sparrow hornets in the next year. There are detailed data in the text above. You can determine where to deploy the elimination measures to achieve the best eﬀects, given the limited resources of government agencies.

ii) Use image recognition and text mining methods to reduce your workload and eﬀectively increase the investigation’s accuracy. In addition, you can encourage people to take pictures or videos of sparrow hornets and upload them on the website to help you estimate the distribution of sparrow hornets. In this process, notes following the pictures or videos will improve the accuracy of your estimation. However, due to the low quality of the photos taken by the public, many of them are not suitable for image recognition, and most of the uploaded notes do not contain useful information. Therefore, you ought to appropriately promote relevant knowledge to the public to improve photos, videos and notes. For example, as to how to take photos of high quality, we suggest that the head, thorax and abdomen of sparrow hornet, which features are apparent, had better be taken in the photos. What’s more, public notes should contain useful information, such as color, stripe and body size and so on.

iii) Pay more attention to events taking place in the months of summer, when sparrow hornets tend to be more active, and increase the frequency of investigation and updating data.

关注数学模型 According to results predicted, we ﬁnd that sparrow hornets are most active in July and August. During the period from November to March of the next year, sparrow hornets are almost in hibernation and appear a little, when you had better properly decrease the frequency of investigation and updating data, to avoid the waste of human resources and 微信公众号：数学模型 material resources.

iv) According to the predicted location of the migration of sparrow hornets, notify beekeepers and farmers and other stakeholders in time to avoid unnecessary economic losses. As an alien specie, sparrow hornet tends to hunt bee colonies closer to it on a large scale, causing economic losses.

As to how to eradicate the sparrow hornets, after looking up relevant information, we provide several approaches as follows.

i) Targeting Queens. The queen in an ethnic group tends to go out in April and October, and you’d better conduct more traps during this time to catch and kill the queen. Once 微信号：MATHmodels the queen is dead, this ethnic group will disappear in a short time.

ii) Targeting Nests. You can track the sparrow hornets back to the nest, ﬁnd their nest and destroy it.

iii) Public Outreach. In daily life, you need to strengthen the popularization of knowledge about pest control.

The suggestions above will help you better predict the distribution of sparrow hornets, update the data promptly and more eﬀectively resist the invasion of alien species, protecting the local ecosystem. We sincerely hope that our study will beneﬁt you and better protect the ecology of Washington State, USA.

Sincerely,

关注数学模型
