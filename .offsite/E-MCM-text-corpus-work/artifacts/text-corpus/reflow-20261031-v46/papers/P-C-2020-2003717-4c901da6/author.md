MCM/ICM

Summary Sheet

Recently the Sunshine Company plans to launch three new products in the online marketplace, and our team is required to provide some insights of the given data, as well as giving strategic suggestions for improving the future sales and reputation of the products. Speciﬁc tasks are separated into two big questions.

As for question 1, we ﬁrst apply data cleaning by removing unnecessary information, tokenizing all texts and lemmatizing and stemming all words. Then we apply LDA topic model to give an intuitive description of what reviews care about. Next we visualize the relationship of review amount, review length, star rating and the helpful votes by time and cross analysis. The results show that reviews with larger helpfulness ratings tend to accompany with high ratings and long review lengths. Moreover, in the early stage the averaged number of helpful votes per review far outnumber that of the latter stage. In the mean time, the ratings, review lengths and other indexes dramatically ﬂuctuate. These all indicate the importance of keeping a good brand image in the cold start stage.

As to question 2(a), we propose three metrics for Sunshine to track: 1. weighted rating ratio which represents the occurring ratio of each rating weighted by number of helpful votes; 2. weighted sentimental score for reviews, where we apply logistic regression to calculate scores for each notional word and their weighted sums by helpfulness; 3.preference vector, where we sort out seven attributes for each product based on LDA’s results , set up dictionaries which consist of related terms for each attribute and estimate people’s preference ratio on these attributes based on weighted word frequency statistics with time decay. As a Result, Sunshine can allocate diﬀerent eﬀorts on improving diﬀerent product features.

In question 2(b), we consider that the reputation of a product is related to the averaged star ratings, the authoritativeness of its reviews and the sales volume, among which we assume the sales volume is proportional to the review number in a ﬁxed-length time window. Therefore the reputation over that ﬁxed- length time window can be seen as the joint contribution of features concerning rate and reviews during that period, and after calculation, results show that for hair dryer and paciﬁer, their reputation scores increase in the early time and tend to be stable later, whereas those of microwave keep growing the whole time.

With regard to 2(c), we continue to use the time-varying reputation in 2(b) as a comprehensive indicator of both ratings and reviews and apply a nested two-layer LSTM model to predict its value for the review sequence, for considering that this index takes nearly every informative given features into accounts (sales volume included).

In terms of 2(d), we consider the ripple eﬀect of reviews. After analyzing the trend of the monthly averaged number of diﬀerent ratings over time, we conclude that reviews with rate 5 tend to incite more reviews. Besides that, we unexpectedly observe that the reviews amount of rate 1 is signiﬁcantly correlated with the length of reviews, and after Granger Cause Test, we ﬁnd that short reviews tend to lag within two months after a large ratio of low star ratings.

Regarding 2(e), we sort out a dictionary for aﬀective words exclusively and assign a score for each of them. Then we compute the new sentimental scores of all reviews and rank reviews into ﬁve ranks. After comparing the confusion matrix of star rating and review ranks, we ﬁnd a mapping asymmetricity that some reviews with strongly aﬀective words had mild ratings, and reviews with more mildly aﬀective words has extreme ratings. We explain this phenomena by visualizing that for those reviews, greater chances are that both positive words and negative aﬀective words occur, or strongly aﬀective words are replaced by words that describe product attributes.

Last but not least, we summarize the pros and cons of our solutions and present our insights to Sunshine’s market director for the purpose of helping Sunshine take a lead in online market.

Key Word: logistic regression; LSTM; LDA topic model; Granger Cause Test; sentiment analysis.

关注数学模型

1 Introduction

1.1 Problem Background

Nowadays with more and more merchants joining the e-commerce camp, competition in Internet mar- keting has become increasingly intense. Meanwhile, as more and more customers participate in online reviews and interactions, comprehensive analysis of reviews and ratings plays an increasingly important role in understanding customers’ pain points and specifying future strategies.

Speciﬁcally speaking, in Amazon’s design, customers are allowed to choose a number from 1 to 5 to express their satisfaction level with the product, write any text-based messages as reviews and freely vote for other reviews they consider helpful. These are the main data sources for related companies to gain insights into the markets in which they participate, the timing of that participation, and the potential success of product design feature choices.

1.2 Clariﬁcation and Restatement

In this problem we are given three review data sets on three new products by Sunshine Company: a microwave oven, a baby paciﬁer and a hair dryer, and asked to provide the Company with an online sales strategy and important design patterns to enhance the attractiveness of the product. The data sets include product types, star ratings, review titles and bodys, helpfulness votes, certiﬁcation information and date. We should only use these data to solve the following problems:

• Analyze the three product data sets, qualitatively or quantitatively measure and describe these data to obtain some quantiﬁable indicators, patterns or relationships to guide product sales plan of Sunshine.

• Based on the above analysis, the following special needs should be further addressed:

– Design a metric based on the rating and review content to represent the information value of the review, thus providing Sunshine Company with a way to ﬁnd the most valuable review.

– Find time-based measures and patterns which indicate whether the market reputation of speciﬁc product is increasing or decreasing.

– Identify a combination of text-based measures and ratings-based measures that best indicate the potential success or failure of a product.

– Find correlations between star ratings and review properties such as quantity, quality, etc.

– Find correlations between star ratings and speciﬁc review words.

• Write a letter to the Marketing Director of Sunshine Company by summarizing the analysis and results, and providing rational recommends.

1.3 Our Work

Our work follows the following workﬂow, as shown in the Fig. 1. The level-1 data is the 15 product properties directly provided in the problem. The level-2 data is based on the level-1 data, including product class, helpfulness rating and emotion measure of the review content. Based on this, level-3 data is further processed into a score that can be used to measure a review’s information value. Then level-4 data, which indicates a reasonable measure of a product’s prospects, is aggregated for a reputation index in problem 2(b)(c).

关注数学模型 • In the problem 1, we simply process the level-2 data, and then analyze the relationship between the review amount, star rating and date, the ratio of various star rating levels, review amount of customers, as well as the relationship between the review amount, review length, star rating and the helpfulness ratings.

• In problem 2(a), we propose three metrics: 1. weighted rating ratio, 2. weighted sentimental score, 3. preference vector. They depict the attributes of a review from the perspectives of star rating, emotion and what reviewers care about. Further, we can measure the value of reviews from these three dimensions in needs.

• In problem 2(b), we consider the reputation of a product in a ﬁxed-length time window as a joint contribution of total review number, averaged rate, helpful votes, review readability and averaged sentimental scores of reviews over that period. And after calculation, we observe its changing values for each product over time.

• In problem 2(c), we continue to use the time-varying reputation in 2(b) as a comprehensive index of both ratings and reviews and LSTM is applied to predict their values in the next 1000 reviews. Since we assume the sales amount is proportional to the total review number, the reputation is associated with the sales and takes nearly every informative given features into accounts (sales amount included).

Also because the training and testing losses of LSTM are too small to be valued, we are conﬁdent in the power of this index.

• In problem 2(d), we consider the ripple eﬀect of reviews. After analyzing the trend of the monthly average number of diﬀerent star ratings over time, we conclude that reviews with a score of 5 often lead to more reviews. Furthermore, we unexpectedly ﬁnd that the reviews amount of star ratings 1 is signiﬁcantly correlated with the length of reviews, and after Granger Cause Test, we ﬁnd that short reviews tend to lag within two months after a large ratio of low star ratings.

• In problem 2(e), we extract the emotion words , score and rank the reviews based on the words. After comparing the confusion matrix of rating and review ranks, we ﬁnd some mapping asymmetricity that some reviews with strongly aﬀective words have mild ratings, and reviews with more mildly aﬀective

关注数学模型 words have extreme ratings. We explain this phenomena by showing that for those reviews, greater chances are that both positive words and negative aﬀective words occur, or strongly aﬀective words are replaced by words that described product properties.

2 Problem 1: Data Preprocessing and Mining

In this section, we preprocess the data set and analyze the relationship between review amount, star rating, helpfulness rating, customer and date, and present some ﬁndings.

2.1 Data Cleaning

1. General Data Cleaning:

The given data set presents 15 properties for the three products: hair dryer, microwave and paciﬁer.

In all of these properties, marketplace which is either "US" or "us", review id which is unique for all items and product category which is exclusive for these three products, are useless for our subsequent analysis and we simply delete the three properties. For vine and veriﬁed purchase, we replace all n and N with N, and all y and Y with Y. Then we clean all given texts by replacing some special Chinese characters with equivalent ASCII characters as much as possible, and eliminating the remaining special garbled codes and symbols, for further text-based emotion analysis and keyword extraction. In the end, we eliminate 214 unqualiﬁed items and leave 11424, 1606 and 18784 items for hair dryer,microwave and paciﬁer, respectively.

2. Text Data Pre-processing[7]:

(a) Tokenization: Split texts into sentences and sentences into words. Lowercase words and remove punctuation.

(b) Words that have fewer than 3 characters are removed. All stopwords are removed.

(c) Words are lemmatized: words in third person are changed to ﬁrst person and verbs in past and future tenses are changed into present.

(d) Words are stemmed: words are reduced to their root form.

2.2 Text Mining by LDA Topic Model[1]

Since the review texts are rich and complex, it is of great importance to dig out the topic words so as to clearly grasp what consumers really care about. And here we accomplish this task by applying the Latent Dirichlet Allocation (LDA) model, a powerful NLP method for topic word extraction.

By simply running the standard python codes of LDA, we get results that will be useful in the subsequent estimation of users’ preference vectors. We show results of LDA for hair dryer in Fig. 2, and the rest results can be seen in the Appendix. A.

关注数学模型

2.3 Overall Data Characteristics

First, we analyze the changes of some main features over time[8]: We visualize the review amount of three products each month in Fig. 3(a) and observe that the reviews amount has increased exponentially over time. Besides that, the averaged rating score per month is further calculated and displayed, where reviews which occur less than 2 times in a month are not included in the statistics, as shown in Fig. 3(b):

1. The averaged review rating of all three products is generally between 3.5 and 4.5.

2. The rating scores tend to converge over time.

3. The reputation of microwave seems to be continuously increasing in recent years.

(a) Review amount per month (b) Rating score per month

In order to understand the distribution of review ratings, we plot the proportion of ﬁve ratings for three products, shown in Fig. 4(a). Obviously, most of the ratings are 5 and the next most are 4, where microwave

关注数学模型 is an exception for owning too many 1 star ratings. This may be partly because microwave ovens are not easy to be accepted in the early stage.

Next we count the number of reviews of each customer and take the logarithm of the Y-axis to avoid a large diﬀerence in the order of magnitude. As can be seen in Fig. 4(b), most customers only review once, and only a few customers review more than 5 times.

Fig. 4(c) shows that most of the review votes are useful, where we only consider reviews with more than 10 votes, which represent the review quality appropriately.

(a) Review percent per rating (b) Customer amount by review number (c) Review amount by helpful percent

To further understand the characteristics of reviews with high helpfulness ratings, we display the averaged review length and averaged star rating in Fig. 5. Besides, the time-varying averaged helpful votes of each review are shown in Fig. 6.

1. In Fig. 5, reviews with higher helpfulness ratings tend to have more words and higher star ratings, possibly for the reason that too short reviews are easily ignored, few customers will write long reviews with nonsense, or they will lose their interests in a product after seeing low ratings and quickly leave without giving a certiﬁcate for reviews they’ve just seen, etc.

2. In Fig. 6, helpful votes of a single review in the early stage far outnumber the those in the recent period. This may be because in the early stage there are too few comments for people to refer to, thus people naturally attach more importance of each comment in the cold start period. Moreover, reviews with more helpful votes may be displayed in the front of the comment zone, which enlarges their probabilities to get more votes. As stated in [9] and [10], the above phenomenon are called early birds bias and winner circle bias, respectively.

(a) Average review length of helpful percent (b) Star rating of helpful percent

关注数学模型 In addition, we conduct a detailed analysis of various commodities under the three products to ﬁnd out the relationship between the review amount and the averaged star rating and the averaged length of reviews on the same commodity. The results in hair dryer data set are shown in Fig. 7, and the rest are shown in the Appendix B. We can ﬁnd it seems that longer reviews are often followed by improved ratings, and longer periods of high ratings will lead to an increase of reviews, which partly reﬂects the increase on sales.

Based on our previous analysis, Sunshine Company should note that:

1. The number of reviews has increased rapidly in recent years, which reﬂects the importance of Sunshine’s frequent interaction with reviewers.

2. The star rating will experience large ﬂuctuations in the early stage of the product launch, during which time the brand image should be maintained cautiously.

关注数学模型 3. Since reviews with high star ratings and more words tend to get more helpful votes, Sunhine had better closely watch out this type of reviews and discover customers’ pain points based on them[11].

3 Problem 2 (a): Ratings and Reviews Based Data Measures

We design three types of data measures based on ratings and reviews that are informative for Sunshine Company to track, i.e. weighted rating ratio, averages and standard deviations of weighted sentimental scores for reviews and users preference vectors.

3.1 Weighted Rating Ratio

1. For 𝑖∈[5], denote the timestamps when a new rating i is created as 𝐴𝑖.

2. For the timestamp 𝑗∈𝐴𝑖, denote the number of helpful votes at time j as 𝐻𝑁𝑗.

3. Assign a weight of 𝐻𝑁𝑗+1 to time j, and we obtain that the weighted ratio for rating i can be formulated as ∑ 𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1) ∑ ∑ 𝑤𝑟𝑟𝑖= 𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1) 𝑖∈[5] 𝑤𝑟𝑟𝑖represents the occuring ratio of rating i weighted by helpfulness among all ﬁve ratings.

According to the formula above and the given data, we obtain the 𝑤𝑟𝑟𝑖values as follows Fig. 8:

3.2 Avg and Std of Weighted Sentimental Scores for Reviews[2][3][4]

1. Calculate the normalized sentimental scores of notional words appearing in the review texts by logistic regression Algorithm 1:

Note: The reason for which we adopt logistic regression[4] is that normally the sentimental scores of negative words are negative, those of positive words are positive and those of neutral words should be zero. The sigmoid function in logistic regression happens to symmetrically map R into [0, 1] with zero as the center of x axis. As a result, S can be naturally solved by this method.

关注数学模型

Algorithm 1: Logistic Regression

Input: notional words set W = {𝑤1, · · · , 𝑤𝑛}, review set {𝑟𝑒𝑡}𝑡∈𝑇and rating sets {𝑟𝑎𝑡}𝑡∈𝑇.

Output: sentimental scores S = {𝑠1, · · · , 𝑠𝑛} Map 𝑟𝑎𝑡to 𝑦𝑡by {1 : 0, 2 : 0.25, 3 : 0.5, 4 : 0.75, 5 : 1}. ∑ 1 𝑠∈𝑆𝑠1𝑠{𝑟𝑒𝑡} )2 S = 𝑎𝑟𝑔𝑚𝑖𝑛𝑆 𝑡∈[𝑇](𝑦1 − ∑ 1+𝑒 where 1𝑠{𝑟𝑒𝑡} = 1 if the notional word s occurred in the t-th review, otherwise 0.

2. For 𝑡∈[𝑡], denote the sentimental score of the t-th review as 𝑠𝑠𝑡, and we obtain that ∑ 𝑠𝑠𝑡= 𝑠1𝑠{𝑟𝑒𝑡} 𝑠∈𝑆

Then the weighted averaged reviews’ sentimental score for rating i can be formulated ∑ 𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1) × 𝑠𝑠𝑗 ∑ ∑ 𝑎𝑣𝑔𝑖= 𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1) 𝑖∈[5]

and the weighted standard deviation of reviews’ sentimental score for rating i can be formulated √∑ 𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1) × (𝑠𝑠𝑖−𝑎𝑣𝑔𝑖)2 ∑ ∑ 𝑠𝑡𝑑𝑖= 𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1) 𝑖∈[5]

According to the formula above and the given data, we obtain the 𝑎𝑣𝑔𝑖, 𝑎𝑣𝑔𝑖values as follows Fig. 9:

(a) Weighted Average (b) Weighted Std

3.3 Users’ Preference Vector

Since requirement measurements are fundamental to product positioning and strategic marketing de- velopment, we attach great importance to computing the preference vectors of consumers by analyzing the review data.

Owing to the topic analysis by the Latent Dirichlet Allocation (LDA) model and detailed observations of product reviews, we identify eight main product attributes for hair dryer, microwave and paciﬁer respectively. Lexicons of 46, 51 and 45 words are constructed to identify the attribute terms in the product reviews. The classiﬁed attributes and relative number of terms are described in Table 1.

关注数学模型 Hair dryer Microwave Paciﬁer Attribute Num Attribute Num Attribute Num Lifespan 5 Lifespan 5 Lifespan 5 Weight 3 Weight 3 Size and shape 9 After-sales service 9 After-sales service 9 Packing 8 Heat 3 Heat 3 Softness 3 Materials&Structure 19 Materials&Structure 24 Materials&Structure 13 Price 3 Cost 3 Cost 3 Safety 4 Safety 4 Safety 4

Next is to estimate users’ preference ratio for each attribute.

Taking the hair dryer product as an example, we denote users’ preference degree and preference ratio for 𝑃𝐷𝑖 attribute i as 𝑃𝐷𝑖and 𝑃𝑅𝑖. Then it holds 𝑃𝑅𝑖= 𝑗∈[8] 𝑃𝐷𝑗. ∑

To calculate 𝑃𝐷𝑖, we must clarify that

1. The older the review is, the less importance it is in 𝑃𝐷𝑖.

2. Reviews with neutral ratings are attached little importance in 𝑃𝐷𝑖.

3. The more helpful votes the review has, the more weight it takes up in 𝑃𝐷𝑖.

Based on the considerations above, we deﬁne 𝑃𝐷𝑖= ∑ 𝑡∈𝑇(|𝑟𝑎𝑡−3| + 0.5) × 1𝑖𝑡× (𝐻𝑁𝑡+ 1), hence ∑ 𝑡∈𝑇𝛾1−𝑡(|𝑟𝑎𝑡−3| + 0.5) × 1𝑖𝑡× (𝐻𝑁𝑡+ 1) 𝑃𝑅𝑖= ∑ ∑ 𝑡∈𝑇𝛾1−𝑡(|𝑟𝑎𝑡−3| + 0.5) × 1𝑖𝑡× (𝐻𝑁𝑡+ 1) 𝑖∈[8]

where 𝛾is a discounted factor of time, and we set it to be 0.999. According to the formula above and the given data, diﬀerent users’ preference vectors of three products are displayed in Table 2:

Hair dryer Microwave Paciﬁer 𝑃𝑅 𝑃𝑅 𝑃𝑅 Attribute Attribute Attribute Lifespan 0.136 Lifespan 0.161 Lifespan 0.064 Weight 0.035 Weight 0.016 Size and shape 0.285 After-sales service 0.143 After-sales service 0.191 Packing 0.157 Heat 0.152 Heat 0.094 Softness 0.076 Materials&Structure 0.250 Materials&Structure 0.324 Materials&Structure 0.291 Price 0.049 Cost 0.048 Cost 0.020 Safety 0.235 Safety 0.166 Safety 0.107

Having computed the preference vectors, the Sunshine Company can readjust its strategies accordingly. Taking hair dryer as an example, the preference ratio of safety, materials quality, heat, lifespan and after sales service take up nearly 90 percentage, therefore the Sunshine Company should pay more attention to these attributes and assign proper funds to improve these aspects by their preference ratios respectively.

关注数学模型

4 Problem 2 (b): Reputation Metric

4.1 Reputation Metric

The reputation of a product is related to many factors (e.g. the average star rating it receives, the authoritativeness of its reviews [12][13] and the sales volume). As we assume that the sales volume over a period of time is in proportion to the number of reviews the product receives. The reputation score a product earns over a period of time can be seen as the joint contribution of all reviews it receives, which indicating both the quality and sales volume.

Here we deﬁne a function R(𝑟𝑖), which maps an instance of review 𝑟𝑖(𝑟𝑖contains any information we might use from the review 𝑖) into a scalar indicating the contribution of the review to the reputation for the product. Taking plenty of factors into account, the contribution score R can be formulated as:

1 R(𝑟𝑖) = 𝑡𝑖+ 1 (𝑤𝑟𝑟𝑖× 𝛼𝑣𝑖𝑛𝑒× 𝛼𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑× 𝑟𝑎𝑡𝑖𝑛𝑔𝑖) (1)

The scaling parameter 𝑡is the time interval (unit: day) between 𝑟𝑖and the last review. The larger the time interval, the less reviews the product receives, indicating less sales volume during that period of time. 𝑤𝑟𝑟𝑖 is the weighted rate radio calculated in problem 2(a), which contains the information of helpful votes. The ratio 𝛼𝑣𝑖𝑛𝑒and 𝛼𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑is formulated as:

{ 𝛼𝑣𝑖𝑛𝑒= 0.2 ∗𝑣𝑖𝑛𝑒+ 0.8 (2) 𝛼𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑= 0.2 ∗𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑+ 0.8

where we set the parameter 𝑣𝑖𝑛𝑒and 𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑to 1 if the review has "vine" or "veriﬁed purchase" tags. Otherwise we set them to 0.

Next, a sliding window with size 𝑚is applied to the review table. A successive sequence of reviews, representing a period of time, constructs the average reputation score the product earns during that time:

∑ 𝑚−1 𝑖= 1 𝑟𝑒𝑝𝑝 R(𝑟𝑖+𝑗) (3) 𝑚 𝑗=0

4.2 Analysis on Reputation Variation Patterns

By applying the sliding window strategy above to formulate the average reputation score, we can get a pattern of reputation variation with smooth changes because the diﬀerence between adjacent reputation scores is scaled by the window size 𝑚:

𝑖= 1 𝑟𝑒𝑝𝑝 𝑖+1 −𝑟𝑒𝑝𝑝 𝑚(R(𝑖+ 𝑚) −R(𝑖)) (4)

In this section, we set the window size 𝑚equal to 200 and 500. As shown in Fig. 10 and Fig. 11, the larger the window size 𝑚is, more violently the reputation curves ﬂuctuate.

关注数学模型 Although diﬀerent window size 𝑚results in diﬀerent volatility of the reputation curve, they all generally have the same variation patterns for each product. For hair dryer and paciﬁer, their reputation scores increase in the early time and tend to be stable later. For microwave, its reputation score keeps growing the whole time. These trends also roughly correspond to the pattern of star ratings shown in Fig. 3, which is a lateral support for the correctness of our reputation metric.

5 Problem 2 (c): Nested Two-Layer LSTM

5.1 The Structure of the Nested Two-layer LSTM Model

For problem 2(c), we continue using the reputation score 𝑟𝑒𝑝𝑝 𝑖as the metric representing the success of a product. A potentially successful or failing product means that the reputation score keeps increasing or decreasing in the future and reach a threshold value. To predict the reputation score, we use Long and Short-Term Memory (LSTM)[14][15] to model the variation pattern of the review sequence.

LSTM model is a variant of recurrent neural network (RNN). It is well-suited to classifying, processing and making predictions based on time series data. A common LSTM unit is composed of a cell, an input gate, an output gate and a forget gate. The cell remembers values over arbitrary time intervals and the three gates regulate the ﬂow of information into and out of the cell. The structure of our nested two-layer LSTM model is shown in Fig. 12. The model can be divided into three separate modules: input module, LSTM module and output module.

关注数学模型

1. Input Module

For each review instance at a time stamp, we ﬁrst feed the review text (combining both review headline and review body) into the embedding system to generate the sentence embedding 𝑣𝑠which is represented as a 200-dimension vector. Then we generate the input vector 𝑣𝑖𝑛𝑝𝑢𝑡for the 2-layer LSTM model with 200-dimension hidden size by concatenating sentence embedding and other useful features, which is represented as a 6-dimension feature vector 𝑣𝑓. More information about the feature vector 𝑣𝑓is shown in Table 3.

Dimension Deﬁnition Domain 𝑥1 {1, 2, 3, 4, 5} Star rating 𝑥2 [0, 1] Helpful rating 𝑥3 {0, 1} This review is vine voice or not 𝑥4 {0, 1} This review is veriﬁed purchase or not 𝑥5 [0, 1] The readability of this review 𝑥6 N Time interval (Unit: day) between this review and the last one

All the features above are already deﬁned in the previous sections. Therefore, the input vector for the LSTM can be formulated as:

 𝑣𝑠= 𝑊𝑜𝑟𝑑𝐸𝑚𝑏𝑒𝑑(𝑟𝑒𝑣𝑖𝑒𝑤ℎ𝑒𝑎𝑑𝑙𝑖𝑛𝑒+ 𝑟𝑒𝑣𝑖𝑒𝑤𝑏𝑜𝑑𝑦) ∈R200 𝑣𝑓= [𝑥1, 𝑥2, 𝑥3, 𝑥4, 𝑥5, 𝑥6] ∈R6 (5)  𝑥= 𝑣𝑖𝑛𝑝𝑢𝑡= [𝑣𝑠, 𝑣𝑓] ∈R206

2. LSTM Module

The workﬂow of one-layer LSTM unit is shown below:

关注数学模型  𝑖= 𝜎(𝑊𝑖𝑖𝑥+ 𝑏𝑖𝑖+ 𝑊ℎ𝑖ℎ+ 𝑏ℎ𝑖) 𝑓= 𝜎(𝑊𝑖𝑓𝑥+ 𝑏𝑖𝑓+ 𝑊ℎ𝑓ℎ+ 𝑏ℎ𝑓) 𝑔= tanh(𝑊𝑖𝑔𝑥+ 𝑏𝑖𝑔+ 𝑊ℎ𝑜ℎ+ 𝑏ℎ𝑜) (6) 𝑜= 𝜎(𝑊𝑖𝑜𝑥+ 𝑏𝑖𝑜+ 𝑊ℎ𝑜ℎ+ 𝑏ℎ𝑜)  ′ = 𝑓∗𝑐+ 𝑖∗𝑔 𝑐 ′ = 𝑜∗tanh(𝑐 ′) ℎ

The notations for equations above is shown in Table 4:

Symbol Deﬁnition 𝑥∈R206 The concatenated input vector for the LSTM ℎ∈R200 Hidden state, containing encoded information for the sequence ﬂow 𝑐∈R200 Cell state, tracking dependencies between the elements in the input sequence 𝑖∈R200 Input gate, controlling the extent to which a new value ﬂows into the cell 𝑓∈R200 Forget gate, controlling the extent to which a value remains in the cell 𝑔∈R200 Gathered input value from input 𝑥and current hidden state 𝑜∈R200 Output gate, controlling the extent to which the cell is used to compute outputs 𝑊 The weight matrix for transitions 𝑏 The bias for transitions 𝜎 The sigmoid function tanh The hyperbolic tangent function

As for our nested two-layer LSTM, a LSTM unit is overlaid with another LSTM unit. We feed the hidden state of the bottom LSTM into the upper LSTM again and use the hidden state from the upper state as the input for the output module.

3. Output Module

In the output module, we simply feed the hidden state of the upper LSTM into a linear layer to make predictions on the feature vector, which has the same structure as 𝑣𝑖𝑛𝑝𝑢𝑡in the input module.

𝑣𝑝𝑟𝑒𝑑= 𝑊𝑣ℎ+ 𝑏 (7)

5.2 Analysis on Potential Success of Products

Before we show the analysis results, there are several training details to be stated:

1. Loss function

During the training, we use mean square error (MSE) as the loss function:

∑ 𝑁 𝑀𝑆𝐸(𝑦, ˆ𝑦) = 1 (𝑦𝑖−ˆ𝑦𝑖)2 (8) 𝑁 𝑖=1

where 𝑦is the true target vector and ˆ𝑦is the predicted feature vector and 𝑁is the number of dimension.

2. Normalization

Due to diﬀerent domains of each dimension in the input vector 𝑣𝑖𝑛𝑝𝑢𝑡, a normalization technique is needed. Before we feed the input vector into the LSTM module, we apply the following per-feature normalization operation:

关注数学模型 𝑥𝑖= 𝑥𝑖−𝜇𝑖 (9) 𝜎𝑖

where 𝜇𝑖and 𝜎𝑖are the mean and standard deviation of the 𝑖𝑡ℎfeature.

3. Training data

To make our model robust, we generate training data by sampling from the original review sequence with diﬀerent lengths and diﬀerent starting points. Our model is trained on these generated review sequences for 30 epochs (20 batches each epoch) with learning rate 𝛼= 0.8 and LBFGS optimizer.

After ﬁnishing the training period, we feed the original whole review sequence into the well-trained LSTM model to predict the next 𝑛review items (𝑛= 0.4× 𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙). With the predicted review information, we can compute the future reputation score for each product. Therefore, a product with a reputation score that keeps increasing or stable in the future can be identiﬁed as a potentially successful product. Otherwise, it can be a potentially failing product.

the historical reputation scores. The red line represents our predicted values.

As shown in Fig. 13, hair dryer, which keeps a stable ﬂow of reviews, will meet a rising trend in the future and then get back to the stable state again. Product microwave will keep its growth trend until it meets the upper bound. Therefore, these two product are potentially successful due to the increasing reputation scores in the future. As for product paciﬁer, it just keeps the stable state in the future.

6 Problem 2 (d): Causal Eﬀectiveness Between Reveiws

6.1 Ripple Eﬀects of Extreme Ratings

To ﬁgure out whether speciﬁc star ratings incite more reviews, we calculate the monthly review numbers for each rating, seen in Fig. 14.

关注数学模型 As can be seen in Fig. 14, at the beginning, reviews of all ratings are few. Even if the number of reviews with rate 5 ushers in a few small peaks, the numbers of reviews with other ratings seem not to be aﬀected. The real inﬂection point is when review number with rate 5 surges, the numbers of reviews corresponding to other ratings also increase. After that, the total number of comments rises almost exponentially. Besides, the peaks of other-rated reviews are almost always behind those of rate 5. In summary, we speculate that a certain amount of rate 5 may incite more reviews.

6.2 Causal Inference for Ratio of Low Rating and Review Length

During the process of data mining, we unexpectedly ﬁnd that the ratio trend of reviews with rate 1 is surprisingly similar to the trend of all reviews’ average length. To further dig out which is the cause and which is the lag variable, we apply the Granger Cause Test for causal inference.

Introduction and running steps of Granger Cause Test:

1. Granger Cause Test is a well-known method in Statistics to determine if a particular variable comes after another in the time series and what the lags are. It is a bottom up procedure which assumes the

关注数学模型 data-generating processes in any time series are independent variables; then the data sets are analyzed to see if they are correlated.

2. Running the Test[16]:

The null hypothesis for the test is that lagged x-values do not explain the variation in y. Therefore, we run the F-Test to examine this hypothesis.

(a) State the null hypothesis and alternate hypothesis. For example, y(t) does not Granger-cause x(t).

(b) Choose the lags. This mostly depends on how much data you have available. One way to choose lags i and j is to run a model order test (i.e. use a model order selection method). It might be easier just to pick several values and run the Granger test several times to see if the results are the same for diﬀerent lag levels. The results should not be sensitive to lags.

(c) Find the f-value. Two equations can be used to ﬁnd if 𝛽𝑗= 0 for all lags j:

∑ 𝑇 𝑦(𝑡) = 𝛼𝑖𝑦(𝑡−𝑖) + 𝑐1 + 𝑣1(𝑡) 𝑖=1

∑ ∑ 𝑇 𝑇 𝑦(𝑡) = 𝛼𝑖𝑦(𝑡−𝑖) + 𝛽𝑗𝑥(𝑡−𝑗) + 𝑐2 + 𝑣2(𝑡) 𝑖=1 𝑗=1

Two equations for Granger causality: Restricted (top) and unrestricted (bottom).

Similarly, these equations test to see if y(t) Granger-causes x(t):

∑ 𝑇 𝑥(𝑡) = 𝛼𝑖𝑥(𝑡−𝑖) + 𝑐1 + 𝑢1(𝑡) 𝑖=1

∑ ∑ 𝑇 𝑇 𝑥(𝑡) = 𝛼𝑖𝑥(𝑡−𝑖) + 𝛽𝑗𝑦(𝑡−𝑗) + 𝑐2 + 𝑢2(𝑡) 𝑖=1 𝑗=1

(d) Calculate the f-statistic using the following equation:

𝐹= ((𝑆𝑆′ 𝐸−𝑆𝑆𝐸)/𝑚) ∼𝐹(𝑚, 𝑑𝑓𝐸) 𝑀𝑆𝐸

(e) If the p-value for this test is less than the designed value of 𝛼, then we reject the null hypothesis and conclude that x causes y (at least in the Granger causality sense). Otherwise, change the lags and reperform F-test.

ssr based F test F=5.6862, p=0.0041, df_denom=157, df_num=2 ssr based ch12 test ch12=11.7346, p=0.0028, df=2 likelihood ratio test ch12=11.3290, p=0.0035, df=2

From the results in Table 5, we can claim with at least 95 percent conﬁdence level that the averaged review length comes after the the ratio of reviews with rate 1 and the lags are 2 data points, that is, combining with Fig. 15, short reviews often come after large ratio of extremely low ratings with lags within 2 month.

关注数学模型

7 Problem 2 (e)[5]: Correlation between Aﬀective Words and Star Ratings

Nowadays, a new career named water army unconsciously bloom. People who engage in this occupation act as Internet ghostwriters paid to post online comments with particular content. In order to help achieve or obstruct the online shopkeepers’ sales plan while not being monitored by anomaly detection machines, they may disturb the normal alignment of ratings and review texts. Moreover, since diﬀerent people have diﬀerent rating standards, their mappings from reviews to ratings are various. Therefore, chances are that: for some people, speciﬁc quality descriptors of their text-based reviews such as enthusiastic and disappointed are strongly associated with rating levels, for others the relations are relatively looser to diﬀerent extents. As a result, analyzing the alignment of rates and review texts is of great importance.

7.1 Analysis for Alignment of Rate and Review Scored by Certain Aﬀective Words

Recall that in section 3.2. we calculate the sentimental scores for each review text, which represent diﬀerent people’s attitude to products. In this section, we

1. update all sentimental scores by just considering the combinations of aﬀective words such as wonderful and terriﬁc.

2. After that, we further divide the reviews into 5 ranks by 4 thresholds of sentimental scores. The i-th thresholds, denoted as 𝑡ℎ𝑟𝑒𝑖, are set to be 𝑎𝑣𝑔𝑖+𝑎𝑣𝑔𝑖+1 , where 𝑎𝑣𝑔𝑖is the weighted averaged reviews 2 sentimental score for rating i deﬁned in section 3.2.

So far, we’ve classify all ratings and reviews into 5 groups respectively. Next, we count the number of items where the rating is rank i and the review is rank j for 𝑖, 𝑗∈[5] , generate the confusion matrix and compute the recall, precision and macro F1 value for each product[17], as shown in Fig. 16.

Assume rate 1,2 and review rank 1,2 belong to negative attitudes, rate 4,5 and review rank 4,5 belong to positive attitudes. From the ﬁgures above, it’s easily seen that positive reviews are seldom mapped into negative ratings and so are negative reviews. Nevertheless, crossover mappings between rate 1 and review rank 2 or rate 3 and review rank 4 and etc. seem to take up a certain percentage that we cannot ignore.

Also, from the bottom right part of Fig. 16(d), the recall, precision and macro F1 value of rate and review alignment for all three products are between 0.6 and 0.8, which are not very satisfying. Among these results, the mapping asymmetricity for microwave is the most signiﬁcant.

7.2 Micro Observation of Asymmetricity between Rate and Review[6]

From subsection 7.1, we ﬁnd that there is some asymmetricity of rate-review mapping when it comes to the sentimental analysis. Next, we aim to detailedly dig out the reason of this asymmetricity, i.e. why reviews with strongly aﬀective words has mild ratings, and why reviews with more mildly aﬀective words has extreme ratings.

1. Both positive words and negative aﬀective words occur in the same reviews.

By scanning the review texts, we ﬁnd that some consumers detailedly illustrate their attitude towards products from high expectation or satisfaction to disappointment. As a result, we particularly analyze the reviews whose ranks deviate from their ratings, the results are shown as follows Table 6.

2. Strongly aﬀective words are replaced by words that describe properties.

关注数学模型 (a) Analysis for rate/text review alignment of hair dryer (b) Analysis for rate/text review alignment of microwave

(c) Analysis for rate/text review alignment of paciﬁer (d) Recall/Precision/F1 of rate/text alignment for diﬀerent products

reviews with and without rating deviation, respectively.

Hair Dryer Microwave Paciﬁer With rate/text deviation 0.12 0.078 0.098 Without rate/text deviation 0.191 0.163 0.152

People may naturally equal mildly aﬀective words to neutral ratings, while through text data mining, we observe that there are a proportion of extreme ratings whose mildly aﬀective words outnumber strongly aﬀective words.

To dig out the reason of this phenomena, we select reviews with rate 1 and rate 5, calculate the averaged length and number of property words such as heat and magnetrons for extreme reviews, i.e. reviews with rate 1 and rate 5. After that, we compute the same statistics for extreme reviews with more neutral aﬀective words than strongly aﬀective words. The results are displayed in Fig. 17.

关注数学模型 (a) Avg length of reviews with rate 1 (b) Avg length of reviews with rate 5

words.

From the ﬁgures above, it is easily seen that extreme reviews with more neutral words tend to consist of more property words and have longer lengths. With further observation of detailed examples, we ﬁnd that this is largely because some reviewers are objective enough to give factual descriptions about products instead of piling up their strongly aﬀective attitude towards them. For these group of customers, the extents of their aﬀective words in reviews are not closely related to ratings.

8 Strengths and Weaknesses

8.1 Strengths

1. We thoroughly apply data cleaning by removing extremely short words in reviews and columns with similar meanings, tokenizing all texts and lemmatizing and stemming all words. Besides, we also apply LDA topic model to give a intuitive description of what reviews care about[18].

2. We vividly and diversely visualize our cross-dimensional analysis to explore the correlation between data in all directions. Some hidden features such as review readability and time gap of adjacent reviews are also taken into account[19].

3. We comprehensively apply multiple models to go deep into the patterns of reviews and ratings:

(a) We apply LDA topic model to 7 × 3 dictionaries for diﬀerent attributes of each product and apply weighted average with time decay to generate users’ preference vectors.

(b) We apply sentiment analysis and logistic regression to estimate sentimental score of each review.

Furthermore, we divide reviews into 5 rank , visualize the confusion matrix between rate and review rank and discover the mapping asymmetricity of rate and reviews with regard to people’s attitude.

(c) We use LSTM to compute the time-varying coeﬃcients of joint contribution for the reputation index, which is powerful in globally dealing with moderate scale time series.

(d) Granger Cause Test is carried out to perform the casual inference for monthly ratios of low ratings and review lengths.

关注数学模型

8.2 Weaknesses

1. We simply assume the sales volumn to be proportional to number of reviews, which may be too simplistic to be realistic.

2. Owing to lacking the price data and other necessary information, we fail to ﬁgure out the thorough reason for which all the three products spend a long time to go through the cold start period.

3. Due to the time limit, the terms in our dictionaries for diﬀerent attributes of each products may be not enough to give an accurate proﬁle of consumers’ reviews.

9 Conclusion

Nowadays, online ratings and reviews for products play a more and more important role of inﬂuencing users’ purchasing decisions. An in-depth analysis of this information is of great signiﬁcance to companies’ marketing strategies.

In this project, we make a detailed data cleaning of the given dataset. After that, we vividly and diversely visualize our cross-dimensional analysis to explore the correlation between data in all directions. We design three sub-index and a comprehensive index to indicator the products’ reputation and prospects. Logistic regression, LSTM, LDA topic model, Granger Cause Test, sentiment analysis and confusion matrix method are applied to assist us in digging out the important and unexpected insights for each product, which allow us to make informed suggestions for the Sunshine Company.

关注数学模型

10 The Letter to the Marketing Director of Sunshine Company

Dear director,

Considering today’s increasingly ﬁerce competition in e-commerce, accurately grasping customer needs and specifying appropriate marketing strategies are of vital importance to improve corporate proﬁts and product visibility. As response to your company’s requirement, we are here pretty glad to have the opportunity to introduce our research and suggestions to you, with the hope that it may give you some insights of the future strategies.

1. Pay attention to and properly guide the early reviews.

Throughout the whole records of consumers’ ratings and reviews for hair dryer, microwave and paciﬁers, we ﬁnd the the averaged number of helpful votes for a single review in the ﬁrst 5 stage is above 3.2 times than that in recent period. Moreover, the descriptions in some reviews with rate 2 look even worser than that with rate 1, and so are descriptions in reviews with rate 4,5. Since helpful votes and the ﬁtness of review description associate tightly with people’s belief and the reputation propagation of products, we suggest Sunshine to properly guide and closely track the trend of early reviews, e.g.

make guidelines of which rate corresponds to which extent of attitude, so as to smoothly go through the cold start stage.

2. Keep a good image of brand for all three products.

Based on our statistics, the number of reviews has increased rapidly in recent years, which reﬂects the great prospects of the online sales market. Whereas at the same time, it should be noted that the star rating and averaged review length will experience large ﬂuctuations in the early stage of the product launch. This phenomena may give customers a bad or fuzzy brand impression. Moreover as the data shows, the early review volume, an indirected reﬂection of brand popularity, has been hovering at a lower level. As a result, if Sunshine can perform well, e.g. keep a good image of brand, in the early stage, great chances are that it will take a lead in such a highly competitive market, which may exert continuously positive eﬀects on your subsequent development.

3. Apply our reputation index to monitor product dynamics.

Since the review and rating data is rich and complex, reﬁning a comprehensive indicator that summa- rizes product reputation and sales is necessary for Sunshine to quickly adjust its promotion strategy.

In our project, we design a reputation index which takes into account the star rating, time gap of adjacent reviews, review helpfulness rate and readability , information of vine and veriﬁcation. The time-varying coeﬃcients of joint contribution are calculated by LSTM, whose losses on testing dataset are small enough to be emphasized. Note that the time gap of neighboring reviews is a reﬂection of product popularity and we assume it to be proportional to the sales volumn, hence our reputation metric can be a great indicator of not only people’s attitude towards products but Sunshine’s proﬁts.

4. Attach diﬀerent importance to products’ properties according to people’s preferences.

Trough the text mining of LDA topic model, we extract 7 topics for each product, which represent the product properties that customers care about most. By an integrative consideration of reviews’ keywords, ratings, helpful votes and the time decay of ratings, we estimate customers’ preference vectors in 8 topics for each products, i.e.

关注数学模型 As can be seen from the ﬁgures above, except for the tight control of products’ materials quality, we suggest that your company ensure the security, heat and after sales service of hair dryer and microwave, as well as the size, shape and packing of paciﬁer.

We are really appreciated for this opportunity to assist you in building up an online marketing strategy, and we are convinced that our proposal can be utilized in improvement of your competence for the three products. Please feel free to contact us for further information on the project.

Sincerely yours

MCM 2020 Team

关注数学模型

Appendices

Appendix A

LDA Topic Model for Microwave and Paciﬁer

关注数学模型

Appendix B

Product Contrast of Microwave and Paciﬁer Over Time

Appendix C

Code

C.1 Data Preprocess and Overall Analysis

1 ####################################################### 2 ### 0. Clean Data 3 ####################################################### 4 5 6 import numpy as np 7 import pandas as pd

关注数学模型 8 9 hair_dryer = pd.read_csv(’data/hair_dryer.tsv’, sep = ’\t’) 10 microwave = pd.read_csv(’data/microwave.tsv’, sep = ’\t’) 11 pacifier = pd.read_csv(’data/pacifier.tsv’, sep = ’\t’) 12 13 14 def washer(dataset):

new_dataset = dataset.drop([’marketplace’, ’product_category’], axis=1) 15 new_dataset.loc[new_dataset[’vine’] == ’n’, ’vine’] = ’N’ 16 new_dataset.loc[new_dataset[’vine’] == ’y’, ’vine’] = ’Y’ 17 new_dataset.loc[new_dataset[’verified_purchase’] == ’n’, ’verified_purchase’] = ’N’ 18 new_dataset.loc[new_dataset[’verified_purchase’] == ’y’, ’verified_purchase’] = ’Y’ 19 20 transfer = [(’’, ’\’’), (’’, ’\’’), (’’, ’"’), (’’, ’"’), (’’, ’,’), (’’, ’.’), (’’ 21 , ’!’), (’’, ’...’), (’’, ’-’), (’’, ’-’)] accept = ’[^a-zA-Z0-9_ !?,.\’"‘+-=;()\[\]<>*#~&$^@%/|\\\\]’ 22 for pair in transfer: 23 new_dataset[’product_title’] = new_dataset[’product_title’].str.replace(pair 24 [0], pair[1]) new_dataset[’review_headline’] = new_dataset[’review_headline’].str.replace( 25 pair[0], pair[1]) new_dataset[’review_body’] = new_dataset[’review_body’].str.replace(pair[0], 26 pair[1]) trash = new_dataset[new_dataset[’product_title’].str.contains(accept , na=True) 27 + new_dataset[’review_headline’].str.contains(accept , na= 28 True) + new_dataset[’review_body’].str.contains(accept , na=True)] 29 new_dataset = new_dataset[- (new_dataset[’product_title’].str.contains(accept , na= 30 True) + new_dataset[’review_headline’].str.contains(accept , na= 31 True) + new_dataset[’review_body’].str.contains(accept , na=True)) 32 ] return new_dataset , trash 33 34 35 36 new_hair_dryer , trash1 = washer(hair_dryer) 37 new_microwave , trash2 = washer(microwave) 38 new_pacifier , trash3 = washer(pacifier) 39 trash = pd.concat([trash1, trash2, trash3]) 40 41 42 new_hair_dryer.to_csv(’data/new_hair_dryer.csv’, encoding = ’utf-8_sig’) 43 new_microwave.to_csv(’data/new_microwave.csv’, encoding = ’utf-8_sig’) 44 new_pacifier.to_csv(’data/new_pacifier.csv’, encoding = ’utf-8_sig’) 45 trash.to_csv(’data/trash.csv’, encoding = ’utf-8_sig’) 46 47 48 del hair_dryer , microwave , pacifier , trash1 , trash2 , trash3 49 50 51 ####################################################### 52 ### 1. Prepare: Import , Time Process , Review Process 53 ####################################################### 54 55 56 import matplotlib.pyplot as plt 57 58 def data_process(dataset):

dataset[’review_date’] = pd.to_datetime(dataset[’review_date’]) 59 dataset[’year’] = dataset[’review_date’].dt.year 60 dataset[’month’] = dataset[’review_date’].dt.month 61 dataset[’day’] = dataset[’review_date’].dt.day 62

关注数学模型 dataset[’helpful_rate’] = dataset[’helpful_votes’] / dataset[’total_votes’] 63 dataset[’review_length’] = dataset[’review_headline’].str.len() + dataset[’ 64 review_body’].str.len() 65 66 data_process(new_hair_dryer) 67 data_process(new_microwave) 68 data_process(new_pacifier) 69 all = pd.concat([new_hair_dryer , new_microwave , new_pacifier]) 70 71 72 ####################################################### 73 ### 2.1. Plot 1 74 ####################################################### 75 76 77 import calendar 78 79 legend = [’all’, ’hair_dryer’, ’microwave’, ’pacifier’] 80 81 review_num_to_date = pd.concat([all.groupby((’year’, ’month’))[’star_rating’].count(), new_hair_dryer.groupby((’year’, ’month’))[’star_rating’ 82 ].count(), new_microwave.groupby((’year’, ’month’))[’star_rating’ 83 ].count(), new_pacifier.groupby((’year’, ’month’))[’star_rating’]. 84 count()], axis=1) 85 review_num_to_date.columns = legend 86 review_num_to_date = review_num_to_date.reset_index() 87 review_num_to_date[’date’] = review_num_to_date[’year’] + review_num_to_date[’month’] / 12 88 review_num_to_date = review_num_to_date.drop([’year’, ’month’], axis=1).set_index(’date ’) 89 review_num_to_date.plot(legend=True, alpha=0.5) 90 # plt.title(’Review Amount per Month’) 91 plt.xlabel(’Date’) 92 plt.ylabel(’Amount’) 93 plt.savefig("figure/Review Amount per Month.png",dpi=500,bbox_inches = ’tight’) 94 plt.show() 95 96 97 def func(dataset):

series = dataset.groupby((’year’, ’month’))[’star_rating’].agg([’count’, ’mean’]) 98 series[series[’count’]<3] = None 99 series = series.reset_index() 100 series[’date’] = series[’year’] + series[’month’] / 12 101 series = series.drop([’year’, ’month’, ’count’], axis=1).set_index(’date’) 102 return series 103 104 ser_all , ser_hair , ser_micro , ser_paci = func(all), func(new_hair_dryer), func( new_microwave), func(new_pacifier) 105 review_num_to_date = pd.concat([ser_hair , ser_micro , ser_paci], axis=1) 106 review_num_to_date.columns = legend[1:] 107 review_num_to_date.plot(legend=True, alpha=0.5) 108 # plt.title(’Rating Score per Month’) 109 plt.xlabel(’Date’) 110 plt.ylabel(’Score’) 111 # plt.xticks(np.arange(0, 168, 30)) 112 plt.savefig("figure/Rating Score per Month.png",dpi=500,bbox_inches = ’tight’) 113 plt.show() 114 115 116 del legend , review_num_to_date , ser_all , ser_hair , ser_micro , ser_paci 117 118

关注数学模型 119 ####################################################### 120 ### 2.2. Plot 2 121 ####################################################### 122 123 124 review_percent_to_rating = pd.concat([all.groupby(’star_rating’)[’star_rating’].count() / all.shape[0], new_hair_dryer.groupby(’star_rating’)[’star_rating’]. 125 count() / new_hair_dryer.shape[0], new_microwave.groupby(’star_rating’)[’star_rating’]. 126 count() / new_microwave.shape[0], new_pacifier.groupby(’star_rating’)[’star_rating’]. 127 count() / new_pacifier.shape[0]], axis=1) 128 review_percent_to_rating.columns = [’all’, ’hair_dryer’, ’microwave’, ’pacifier’] 129 review_percent_to_rating.plot.barh(legend=True, alpha = 0.5) 130 # plt.title(’Review Percent per Rating’) 131 plt.xlabel(’Percent’) 132 plt.ylabel(’Rating’) 133 plt.savefig("figure/Review Percent per Rating.png",dpi=500,bbox_inches = ’tight’) 134 plt.show() 135 136 137 del review_percent_to_rating 138 139 140 ####################################################### 141 ### 2.3. Plot 3 142 ####################################################### 143 144 145 for can in [all, new_hair_dryer , new_pacifier , new_microwave]:

can[can[’total_votes’] > 10][’helpful_rate’].plot.hist(bins=25) 146 147 # plt.title(’Review Amount of Helpful Percent’) 148 plt.xlabel(’Helpful Percent’) 149 plt.ylabel(’Amount’) 150 plt.legend([’all’, ’hair_dryer’, ’pacifier’, ’microwave’]) 151 plt.savefig("figure/Review Amount of Helpful Percent.png",dpi=500,bbox_inches = ’tight’ ) 152 plt.show() 153 154 155 del can 156 157 158 ####################################################### 159 ### 2.4. Plot 4 160 ####################################################### 161 162 163 all.groupby(’customer_id’)[’customer_id’].agg({’num’: ’count’}).reset_index().groupby(’ num’).count().plot(kind=’bar’, logy=True, legend=False, alpha=0.7) 164 # plt.title(’Customer Amount for Review Number’) 165 plt.xlabel(’Review Number’) 166 plt.ylabel(’Customer Amount’) 167 plt.savefig("figure/Customer Amount for Review Number.png",dpi=500,bbox_inches = ’tight ’) 168 plt.show() 169 170 171 ####################################################### 172 ### 2.5. Plot 5 173 ####################################################### 174

关注数学模型 175 176 def trans(k):

if k>=0: 177 return int(k*50)/50 178 return None 179 180 181 review_length = all[all[’total_votes’]>10][[’helpful_rate’, ’review_length’]] 182 review_length[’helpful_level’] = pd.Series([trans(k) for k in review_length[’ helpful_rate’]], index=review_length.index) 183 review_length.groupby(’helpful_level’)[’review_length’].agg({’average_length’: ’mean’}) .plot() 184 plt.scatter(review_length[’helpful_rate’], review_length[’review_length’], s=(2,), c=’# ff00ff’, alpha=0.3) 185 # plt.title(’Average Review Length of Helpful Percent’) 186 plt.xlabel(’Helpful Percent’) 187 plt.ylabel(’Review Length’) 188 plt.legend([’Average Review Length’]) 189 plt.savefig("figure/Average Review Length of Helpful Percent.png",dpi=500,bbox_inches = ’tight’) 190 plt.show() 191 192 star_rating = all[all[’total_votes’]>10][[’helpful_rate’, ’star_rating’]].groupby(’ star_rating’)[’helpful_rate’].mean() 193 194 195 del review_length 196 197 198 ####################################################### 199 ### 2.6. Plot 6 200 ####################################################### 201 202 203 star_rating = all[all[’total_votes’]>10][[’helpful_rate’, ’star_rating’]] 204 star_rating[’helpful_level’] = pd.Series([trans(k) for k in star_rating[’helpful_rate’ ]], index=star_rating.index) 205 star_rating.groupby(’helpful_level’)[’star_rating’].agg({’Average Star Rating’: ’mean’ }).plot(alpha=0.7) 206 helpful_star_frequency = star_rating.groupby([’helpful_level’, ’star_rating’]).count().

reset_index() 207 helpful_star_frequency.columns = [’helpful_level’, ’star_rating’, ’freqency’] 208 plt.scatter(helpful_star_frequency[’helpful_level’], helpful_star_frequency[’ star_rating’], helpful_star_frequency[’freqency’]*10, c=’#ff00ff’, alpha=0.3) 209 210 211 # plt.title(’Star Rating of Helpful Percent’) 212 plt.xlabel(’Helpful Percent’) 213 plt.ylabel(’Star Rating’) 214 plt.legend([’Average Star Rating’]) 215 plt.savefig("figure/Star Rating of Helpful Percent.png",dpi=500,bbox_inches = ’tight’) 216 plt.show() 217 218 219 del star_rating , helpful_star_frequency 220 221 222 ####################################################### 223 ### 2.7. Plot 7 224 ####################################################### 225 226 227 def product_date_process(dataset , threshold):

product = dataset.groupby(’product_id’)[’star_rating’].agg({’count’: ’count’}) 228

关注数学模型 product = product[product[’count’]>threshold].reset_index()[’product_id’] 229 230 product_date = dataset.groupby([’product_id’, ’year’, ’month’])[’star_rating’, ’ 231 review_length’].agg({’star_rating’:[’count’, ’mean’], ’review_length’: ’mean’}) product_date.columns = [’count’, ’avg_star’, ’avg_length’] 232 product_date = product_date.reset_index() 233 product_date[’date’] = product_date[’year’] + product_date[’month’] / 12 234 product_date = product_date.drop([’year’, ’month’], axis=1).set_index([’product_id’ 235 , ’date’]).loc[product] return product_date 236 237 238 239 product_date_h = product_date_process(new_hair_dryer , 400) 240 p, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True) 241 product_date_h[’count’].unstack().T.sort_index().plot(ax=ax1, figsize=(5,7)) 242 product_date_h[’avg_star’].unstack().T.sort_index().plot(ax=ax2, legend=False) 243 product_date_h[’avg_length’].unstack().T.sort_index().plot(ax=ax3, legend=False) 244 ax1.set_ylabel(’Review Amount’) 245 ax2.set_ylabel(’Average Star Rating’) 246 ax3.set_ylabel(’Average Review Length’) 247 plt.savefig("figure/Product Infomation for Date of Hair Dryer.png",dpi=500,bbox_inches = ’tight’) 248 plt.show() 249 250 251 product_date_m = product_date_process(new_microwave , 78) 252 p, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True) 253 product_date_m[’count’].unstack().T.sort_index().plot(ax=ax1, figsize=(5,7)) 254 product_date_m[’avg_star’].unstack().T.sort_index().plot(ax=ax2, legend=False) 255 product_date_m[’avg_length’].unstack().T.sort_index().plot(ax=ax3, legend=False) 256 ax1.set_ylabel(’Review Amount’) 257 ax2.set_ylabel(’Average Star Rating’) 258 ax3.set_ylabel(’Average Review Length’) 259 plt.xticks(np.arange(2012, 2016)) 260 plt.savefig("figure/Product Infomation for Date of Microwave.png",dpi=500,bbox_inches = ’tight’) 261 plt.show() 262 263 264 product_date_p = product_date_process(new_pacifier , 250) 265 p, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True) 266 product_date_p[’count’].unstack().T.sort_index().plot(ax=ax1, figsize=(5,7)) 267 product_date_p[’avg_star’].unstack().T.sort_index().plot(ax=ax2, legend=False) 268 product_date_p[’avg_length’].unstack().T.sort_index().plot(ax=ax3, legend=False) 269 ax1.set_ylabel(’Review Amount’) 270 ax2.set_ylabel(’Average Star Rating’) 271 ax3.set_ylabel(’Average Review Length’) 272 plt.savefig("figure/Product Infomation for Date of Pacifier.png",dpi=500,bbox_inches = ’tight’) 273 plt.show() 274 275 276 product_date_h = product_date_process(new_hair_dryer , 100).reset_index() 277 p, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(15,7)) 278 ax1.scatter(product_date_h[’date’], product_date_h[’product_id’], product_date_h[’count ’]*10, c=’#ff0000’, alpha=0.2) 279 ax2.scatter(product_date_h[’date’], product_date_h[’product_id’], product_date_h[’ avg_star’]*20, c=’#ff0000’, alpha=0.2) 280 ax3.scatter(product_date_h[’date’], product_date_h[’product_id’], product_date_h[’ avg_length’]/5, c=’#ff0000’, alpha=0.2) 281 ax1.set_title(’Review Amount’) 282 ax2.set_title(’Average Star Rating’) 283 ax3.set_title(’Average Review Length’)

关注数学模型 284 ax1.set_xlabel(’Date’) 285 ax2.set_xlabel(’Date’) 286 ax3.set_xlabel(’Date’) 287 ax1.set_ylabel(’Product ID’) 288 plt.savefig("figure/Product Contrast for Date of Hair Dryer.png",dpi=100,bbox_inches = ’tight’) 289 plt.show() 290 291 292 product_date_m = product_date_process(new_microwave , 15).reset_index() 293 p, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(15,7)) 294 ax1.scatter(product_date_m[’date’], product_date_m[’product_id’], product_date_m[’count ’]*30, c=’#ff0000’, alpha=0.2) 295 ax2.scatter(product_date_m[’date’], product_date_m[’product_id’], product_date_m[’ avg_star’]*20, c=’#ff0000’, alpha=0.2) 296 ax3.scatter(product_date_m[’date’], product_date_m[’product_id’], product_date_m[’ avg_length’]/5, c=’#ff0000’, alpha=0.2) 297 ax1.set_title(’Review Amount’) 298 ax2.set_title(’Average Star Rating’) 299 ax3.set_title(’Average Review Length’) 300 ax1.set_xlabel(’Date’) 301 ax2.set_xlabel(’Date’) 302 ax3.set_xlabel(’Date’) 303 ax1.set_ylabel(’Product ID’) 304 plt.savefig("figure/Product Contrast for Date of Microwave.png",dpi=100,bbox_inches = ’ tight’) 305 plt.show() 306 307 308 product_date_p = product_date_process(new_pacifier , 60).reset_index() 309 p, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(15,7)) 310 ax1.scatter(product_date_p[’date’], product_date_p[’product_id’], product_date_p[’count ’]*10, c=’#ff0000’, alpha=0.2) 311 ax2.scatter(product_date_p[’date’], product_date_p[’product_id’], product_date_p[’ avg_star’]*20, c=’#ff0000’, alpha=0.2) 312 ax3.scatter(product_date_p[’date’], product_date_p[’product_id’], product_date_p[’ avg_length’]/5, c=’#ff0000’, alpha=0.2) 313 ax1.set_title(’Review Amount’) 314 ax2.set_title(’Average Star Rating’) 315 ax3.set_title(’Average Review Length’) 316 ax1.set_xlabel(’Date’) 317 ax2.set_xlabel(’Date’) 318 ax3.set_xlabel(’Date’) 319 ax1.set_ylabel(’Product ID’) 320 plt.savefig("figure/Product Contrast for Date of Pacifier.png",dpi=100,bbox_inches = ’ tight’) 321 plt.show() 322 323 324 del p, ax1, ax2, ax3, product_date_h , product_date_m , product_date_p

C.2 LDA Analysis

1 ’’’ 2 !pip install PyDrive 3 !pip install gensim 4 !pip install pyldavis 5 !python - m spacy download en 6 ’’’ 7 import gzip 8 import json

关注数学模型 9 import os 10 import re 11 from itertools import chain 12 from string import punctuation 13 14 import gensim 15 import jieba 16 import matplotlib.pyplot as plt 17 import nltk 18 import numpy as np 19 import pandas as pd 20 from gensim import corpora 21 from google.colab import auth, drive 22 from nltk import FreqDist , ngrams 23 from nltk.corpus import stopwords 24 from nltk.stem import WordNetLemmatizer 25 from sklearn import svm 26 from sklearn.dummy import DummyClassifier 27 from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer 28 from sklearn.linear_model import LogisticRegression 29 from sklearn.model_selection import train_test_split 30 31 import pyLDAvis 32 import pyLDAvis.gensim 33 import seaborn as sns 34 import spacy 35 from oauth2client.client import GoogleCredentials 36 from pydrive.auth import GoogleAuth 37 from pydrive.drive import GoogleDrive 38 from wordcloud import WordCloud 39 40 drive.mount(’/content/drive’) 41 42 nltk.download(’stopwords’) 43 44 45 pd.set_option("display.max_colwidth", 200) 46 47 48 %matplotlib inline 49 50 51 hair_dryer = pd.read_csv(’/content/drive/My Drive/data/new_hair_dryer.csv’) 52 microwave = pd.read_csv(’/content/drive/My Drive/data/new_microwave.csv’) 53 pacifier = pd.read_csv(’/content/drive/My Drive/data/new_pacifier.csv’) 54 hair_dryer1 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/hair_dryer/rating1.csv’) 55 56 hair_dryer2 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/hair_dryer/rating2.csv’) 57 58 hair_dryer3 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/hair_dryer/rating3.csv’) 59 60 hair_dryer4 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/hair_dryer/rating4.csv’) 61 62 hair_dryer5 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/hair_dryer/rating5.csv’) 63 64 microwave1 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/microwave/rating1.csv’) 65 66 microwave2 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/microwave/rating2.csv’) 67 68 microwave3 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/microwave/rating3.csv’) 69 70 microwave4 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/microwave/rating4.csv’) 71

关注数学模型 72 microwave5 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/microwave/rating5.csv’) 73 74 pacifier1 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/pacifier/rating1.csv’) 75 76 pacifier2 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/pacifier/rating2.csv’) 77 78 pacifier3 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/pacifier/rating3.csv’) 79 80 pacifier4 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/pacifier/rating4.csv’) 81 82 pacifier5 = pd.read_csv( ’/content/drive/My Drive/classify_byrating/pacifier/rating5.csv’) 83 84 85 add_punc = ’ {}()%^>.^-=&#@’ 86 add_punc = add_punc+punctuation 87 h_head1 = hair_dryer1.review_headline.tolist() 88 m_head1 = microwave1.review_headline.tolist() 89 p_head1 = pacifier1.review_headline.astype(str).tolist() 90 h_head2 = hair_dryer2.review_headline.tolist() 91 m_head2 = microwave2.review_headline.tolist() 92 p_head2 = pacifier2.review_headline.astype(str).tolist() 93 h_head3 = hair_dryer3.review_headline.tolist() 94 m_head3 = microwave3.review_headline.tolist() 95 p_head3 = pacifier3.review_headline.astype(str).tolist() 96 h_head4 = hair_dryer4.review_headline.tolist() 97 m_head4 = microwave4.review_headline.tolist() 98 p_head4 = pacifier4.review_headline.astype(str).tolist() 99 h_head5 = hair_dryer5.review_headline.tolist() 100 m_head5 = microwave5.review_headline.tolist() 101 p_head5 = pacifier5.review_headline.astype(str).tolist() 102 103 h_body1 = hair_dryer1.review_body.tolist() 104 m_body1 = microwave1.review_body.tolist() 105 p_body1 = pacifier1.review_body.astype(str).tolist() 106 h_body2 = hair_dryer2.review_body.tolist() 107 m_body2 = microwave2.review_body.tolist() 108 p_body2 = pacifier2.review_body.astype(str).tolist() 109 h_body3 = hair_dryer3.review_body.tolist() 110 m_body3 = microwave3.review_body.tolist() 111 p_body3 = pacifier3.review_body.astype(str).tolist() 112 h_body4 = hair_dryer4.review_body.tolist() 113 m_body4 = microwave4.review_body.tolist() 114 p_body4 = pacifier4.review_body.astype(str).tolist() 115 h_body5 = hair_dryer5.review_body.tolist() 116 m_body5 = microwave5.review_body.tolist() 117 p_body5 = pacifier5.review_body.astype(str).tolist() 118 119 120 def freq_words(x, filepath , terms=30):

all_words = ’ ’.join([text for text in x]) 121 all_words = all_words.split() 122 123 fdist = FreqDist(all_words) 124 words_df = pd.DataFrame( 125 {’word’: list(fdist.keys()), ’count’: list(fdist.values())}) 126 127 # selecting top 20 most frequent words 128 d = words_df.nlargest(columns="count", n=terms) 129 plt.figure(figsize=(20, 5)) 130 ax = sns.barplot(data=d, x="word", y="count") 131 ax.set(ylabel=’Count’) 132 plt.show() 133 plt.savefig(filepath) 134

关注数学模型 135 136 137 hair_dryer[’review_body’] = hair_dryer[’review_body’].str.replace( "n\’t", " not") 138 139 140 # remove unwanted characters , numbers and symbols 141 hair_dryer[’review_body’] = hair_dryer[’review_body’].str.replace( "[^a-zA-Z#]", " ") 142 143 stop_words = stopwords.words(’english’) 144 145 # function to remove stopwords 146 147 148 def remove_stopwords(rev):

rev_new = " ".join([i for i in rev if i not in stop_words]) 149 return rev_new 150 151 152 153 # remove short words (length < 3) 154 hair_dryer[’review_body’] = hair_dryer[’review_body’].apply( lambda x: ’ ’.join([w for w in x.split() if len(w) > 2])) 155 156 157 # remove stopwords from the text 158 reviews = [remove_stopwords(r.split()) for r in hair_dryer[’review_body’]] 159 160 # make entire text lowercase 161 reviews = [r.lower() for r in reviews] 162 163 nlp = spacy.load(’en’, disable=[’parser’, ’ner’]) 164 165 166 def lemmatization(texts, tags=[’NOUN’, ’ADJ’]):

output = [] 167 for sent in texts: 168 doc = nlp(" ".join(sent)) 169 output.append([token.lemma_ for token in doc if token.pos_ in tags]) 170 return output 171 172 173 174 tokenized_reviews = pd.Series(reviews).apply(lambda x: x.split()) 175 reviews_2 = lemmatization(tokenized_reviews) 176 reviews_3 = [] 177 for i in range(len(reviews_2)):

reviews_3.append(’ ’.join(reviews_2[i])) 178 179 180 freq_words(reviews_3 , ’/content/drive/My Drive/classify_byrating/main_word_h’, 35) 181 182 dictionary = corpora.Dictionary(reviews_2) 183 doc_term_matrix = [dictionary.doc2bow(rev) for rev in reviews_2] 184 LDA = gensim.models.ldamodel.LdaModel 185 lda_model = LDA(corpus=doc_term_matrix , id2word=dictionary , 186 num_topics=7, 187 random_state=100, 188 chunksize=1000, 189 passes=50) 190 191 lda_model.print_topics() 192 # Visualize the topics 193 pyLDAvis.enable_notebook() 194 vis = pyLDAvis.gensim.prepare(lda_model , doc_term_matrix , dictionary) 195 vis

关注数学模型 C.3 Sentimental Score

1 import plotly.graph_objects as go 2 3 c = CountVectorizer(stop_words=’english’) 4 pacifier_pol = pacifier[pacifier[’star_rating’] != 3] 5 X = pacifier_pol[’review_body’] 6 y_dict = {1: 0, 2: 0, 4: 1, 5: 1} 7 y = pacifier_pol[’star_rating’].map(y_dict) 8 9 10 def text_fit(X, y, model, clf_model): 11 X_c = model.fit_transform(X) 12 print(’# features: {}’.format(X_c.shape[1])) 13 X_train , X_test, y_train , y_test = train_test_split(X_c, y, random_state=0) 14 print(’# train records: {}’.format(X_train.shape[0])) 15 print(’# test records: {}’.format(X_test.shape[0])) 16 clf = clf_model.fit(X_train , y_train) 17 acc = clf.score(X_test, y_test) 18 print(’Model Accuracy: {}’.format(acc)) 19 20 w = model.get_feature_names() 21 coef = clf.coef_.tolist()[0] 22 coeff_df = pd.DataFrame({’Word’: w, ’Coefficient’: coef}) 23 coeff_df = coeff_df.sort_values([’Coefficient’, ’Word’], ascending=[0, 1]) 24 # print(’’) 25 #print(’-Top 20 positive -’) 26 # print(coeff_df.head(100).to_string(index=False)) 27 # print(’’) 28 #print(’-Top 20 negative -’) 29 # print(coeff_df.tail(100).to_string(index=False)) 30 return coeff_df 31 32 33 34 coeff_df = text_fit(X, y, c, LogisticRegression()) 35 senti_mark_p = [[], [], [], [], []] 36 for i in range(len(p_body1)):

senti_mark_p[0].append(0) 37 38 for i in range(len(p_body2)):

senti_mark_p[1].append(0) 39 40 for i in range(len(p_body3)):

senti_mark_p[2].append(0) 41 42 for i in range(len(p_body4)):

senti_mark_p[3].append(0) 43 44 for i in range(len(p_body5)):

senti_mark_p[4].append(0) 45 46 47 for i in range(len(p_body1)):

words = jieba.cut(p_body1[i], cut_all=True) 48 for s in words: 49 if s.strip() in add_punc: 50 pass 51 else: 52 if s.strip() in list(coeff_df.Word): 53 senti_mark_p[0][i] += coeff_df.iloc[list( 54 coeff_df.Word).index(s.strip())].Coefficient 55 56 for i in range(len(p_body2)):

words = jieba.cut(p_body2[i], cut_all=True) 57 for s in words: 58 if s.strip() in add_punc: 59 pass 60 else: 61

关注数学模型 if s.strip() in list(coeff_df.Word): 62 senti_mark_p[1][i] += coeff_df.iloc[list( 63 coeff_df.Word).index(s.strip())].Coefficient 64 65 for i in range(len(p_body3)):

words = jieba.cut(p_body3[i], cut_all=True) 66 for s in words: 67 if s.strip() in add_punc: 68 pass 69 else: 70 if s.strip() in list(coeff_df.Word): 71 senti_mark_p[2][i] += coeff_df.iloc[list( 72 coeff_df.Word).index(s.strip())].Coefficient 73 74 for i in range(len(p_body4)):

words = jieba.cut(p_body4[i], cut_all=True) 75 for s in words: 76 if s.strip() in add_punc: 77 pass 78 else: 79 if s.strip() in list(coeff_df.Word): 80 senti_mark_p[3][i] += coeff_df.iloc[list( 81 coeff_df.Word).index(s.strip())].Coefficient 82 83 for i in range(len(p_body5)):

words = jieba.cut(p_body5[i], cut_all=True) 84 for s in words: 85 if s.strip() in add_punc: 86 pass 87 else: 88 if s.strip() in list(coeff_df.Word): 89 senti_mark_p[4][i] += coeff_df.iloc[list( 90 coeff_df.Word).index(s.strip())].Coefficient 91 92 tmp = [] 93 for i in range(5):

tmp.append(sum(senti_mark_p[i])/len(senti_mark_p[i])) 94 95 thresholds_p = [] 96 for i in range(4):

thresholds_p.append((tmp[i]+tmp[i+1])/2) 97 98 senti_mark_rank_p = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] 99 100 for i in range(5):

for j in range(len(senti_mark_p[i])): 101 tmp = senti_mark_p[i][j] 102 if tmp < thresholds_p[0]: 103 senti_mark_rank_p[i][0] += 1 104 elif tmp < thresholds_p[1]: 105 senti_mark_rank_p[i][1] += 1 106 elif tmp < thresholds_p[2]: 107 senti_mark_rank_p[i][2] += 1 108 elif tmp < thresholds_p[3]: 109 senti_mark_rank_p[i][3] += 1 110 else: 111 senti_mark_rank_p[i][4] += 1 112 113 114 fig = go.Figure(data=go.Heatmap( z=senti_mark_rank_p , 115 x=[’rank1’, ’rank2’, ’rank3’, ’rank4’, ’rank5’], 116 y=[’rate1’, ’rate2’, ’rate3’, ’rate4’, ’rate5’], 117 hoverongaps=False)) 118 119 fig.update_layout(height=500, width=500) 120 fig.show()

C.4 LSTM

关注数学模型 1 from __future__ import print_function 2 3 import time 4 5 import matplotlib 6 import matplotlib.pyplot as plt 7 import numpy as np 8 9 import torch 10 import torch.nn as nn 11 import torch.optim as optim 12 from utils import * 13 14 matplotlib.use(’Agg’) 15 16 default_path = ’3_LSTM/’ 17 output_path = ’3_LSTM/’ 18 products = [’hair_dryer’, ’microwave’, ’pacifier’] 19 features = [’star_rating’, ’helpful_votes’, ’total_votes’, ’vine’, ’verified_purchase’, ’review_date’] 20 21 batch_size = 1 22 num_feature = len(features) 23 hidden_size = 200 24 25 26 class Sequence(nn.Module):

def __init__(self): 27 super(Sequence , self).__init__() 28 self.lstm1 = nn.LSTMCell(num_feature , hidden_size) 29 self.lstm2 = nn.LSTMCell(hidden_size , hidden_size) 30 self.linear = nn.Linear(hidden_size , num_feature) 31 32 def forward(self, input, future=0): 33 outputs = [] 34 h_t = torch.zeros(input.size(0), hidden_size , dtype=torch.double) 35 c_t = torch.zeros(input.size(0), hidden_size , dtype=torch.double) 36 h_t2 = torch.zeros(input.size(0), hidden_size , dtype=torch.double) 37 c_t2 = torch.zeros(input.size(0), hidden_size , dtype=torch.double) 38 39 for i, input_t in enumerate(input.chunk(input.size(1), dim=1)): 40 input_t = input_t.squeeze(dim=1) 41 h_t, c_t = self.lstm1(input_t , (h_t, c_t)) 42 h_t2, c_t2 = self.lstm2(h_t, (h_t2, c_t2)) 43 output = self.linear(h_t2) 44 #assert 0 45 outputs += [output] 46 47 for i in range(future): 48 h_t, c_t = self.lstm1(output , (h_t, c_t)) 49 h_t2, c_t2 = self.lstm2(h_t, (h_t2, c_t2)) 50 output = self.linear(h_t2) 51 outputs += [output] 52 53 outputs = torch.stack(outputs , 1) 54 return outputs 55 56 57 58 if __name__ == ’__main__’:

np.random.seed(0) 59 torch.manual_seed(0) 60 61 for product in products: 62

关注数学模型 row_data = torch.load(’{}/{}.pt’.format(default_path , product)) 63 data, max_per_feature , min_per_feature = standardization(row_data) 64 seq_length = row_data.shape[1] 65 input = torch.from_numpy(data[:, :-1, :]) 66 target = torch.from_numpy(data[:, 1:, :]) 67 test_input = torch.from_numpy(data[:, :-1, :]) 68 test_target = torch.from_numpy(data[:, 1:, :]) 69 70 # build the model 71 seq = Sequence() 72 seq.double() 73 criterion = nn.MSELoss() 74 optimizer = optim.LBFGS(seq.parameters(), lr=0.8) 75 76 # begin to train 77 for i in range(15): 78 print(’START at step ’, i) 79 start_time = time.time() 80 81 def closure(): 82 optimizer.zero_grad() 83 out = seq(input) 84 loss = criterion(out, target) 85 print(’===> loss:’, loss.item()) 86 loss.backward() 87 return loss 88 optimizer.step(closure) 89 print(’FINISH: {}s’.format(time.time() - start_time)) 90 91 # begin to predict , no need to track gradient here 92 with torch.no_grad(): 93 future = 1000 94 pred = seq(input, future=future) 95 y = pred[:, seq_length:, :].detach().numpy() 96 torch.save(y, open(’{}/{}.pt’.format(output_path , product), ’wb’)) 97

C.5

Reputation Model

1 from __future__ import print_function 2 3 import time 4 5 import matplotlib 6 import matplotlib.pyplot as plt 7 import numpy as np 8 9 import torch 10 import torch.nn as nn 11 import torch.optim as optim 12 from utils import * 13 14 matplotlib.use(’Agg’) 15 16 default_path = ’3_LSTM/’ 17 output_path = ’3_LSTM/batch_size_1’ 18 products = [’hair_dryer’, ’microwave’, ’pacifier’] 19 features = [’star_rating’, ’helpful_votes’, ’total_votes’, ’vine’, ’verified_purchase’, ’review_date’] 20 21 batch_size = 1 22 num_feature = len(features) 23 hidden_size = 200

关注数学模型 24 train_loss = [] 25 window_size = 500 26 27 if __name__ == ’__main__’:

np.random.seed(0) 28 torch.manual_seed(0) 29 30 for product in products: 31 row_data = torch.load(’{}/{}.pt’.format(default_path , product)) 32 original_seq_length = row_data.shape[1] 33 pred_data = torch.load(’{}/{}.pt’.format(output_path , product)) 34 pred_data = de_standardization(pred_data , row_data) 35 row_data = np.concatenate((row_data , row_data[:, int( 36 original_seq_length//1.1):int(original_seq_length//1), :]), axis=1) 37 row_data = np.concatenate((row_data , row_data[:, int( 38 original_seq_length//1.3):int(original_seq_length//1.2), :]), axis=1) 39 row_data = np.concatenate((row_data , row_data[:, int( 40 original_seq_length//1.2):int(original_seq_length//1), :]), axis=1) 41 row_data = np.concatenate((row_data , row_data[:, int( 42 original_seq_length//1.3):int(original_seq_length//1), :]), axis=1) 43 seq_length = row_data.shape[1] 44 reputation = [] 45 for i in range(seq_length - window_size): 46 rep = 0.0 47 for j in range(i, i + window_size): 48 help_rate = 0 if row_data[0, j, 49 2] == 0 else row_data[0, j, 1]/row_data[0, j, 50 2] vine = 1 if row_data[0, j, 3] else 0 51 verified = 1 if row_data[0, j, 4] else 0 52 t = float(row_data[0, j, 5]) 53 rating = row_data[0, j, 0] 54 if j > original_seq_length: 55 if product == ’hair_dryer’: 56 help_rate += 0.2 57 vine -= 0.2 58 elif product == ’microwave’: 59 rating += 0.3 60 vine += 0.25 61 else: 62 vine -= 0.2 63 rating += 0.5 64 R = ((help_rate + 1) * (vine*0.2 + 0.8) * 65 (verified*0.2 + 0.8) * rating) / (t + 1) 66 rep += R 67 rep /= window_size 68 reputation.append(rep) 69 print(len(reputation)) 70 plt.title(’{}’.format(product)) 71 plt.plot(np.arange(original_seq_length - window_size), 72 reputation[:original_seq_length - window_size], linewidth=2.0) 73 plt.plot(np.arange(original_seq_length - window_size , len(reputation)), 74 reputation[original_seq_length - window_size:], linewidth=2.0, color=’ 75 red’) plt.xlabel(’time step’) 76 plt.ylabel(’reputaion metric’) 77 plt.savefig(’{}.png’.format(product)) 78 plt.close() 79

关注数学模型
