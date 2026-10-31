# P-C-2020-2003717-4c901da6

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2020

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | prose | pages [1] -->
C

<!-- b000006 | furniture | pages [1] -->
2003717

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
Beat The Market: Comprehensive Exploration of Amazon Reviews and Ratings

<!-- b000009 | prose | pages [1] -->
Recently the Sunshine Company plans to launch three new products in the online marketplace, and our team is required to provide some insights of the given data, as well as giving strategic suggestions for improving the future sales and reputation of the products. Speciﬁc tasks are separated into two big questions.

<!-- b000010 | prose | pages [1] -->
As for question 1, we ﬁrst apply data cleaning by removing unnecessary information, tokenizing all texts and lemmatizing and stemming all words. Then we apply LDA topic model to give an intuitive description of what reviews care about. Next we visualize the relationship of review amount, review length, star rating and the helpful votes by time and cross analysis. The results show that reviews with larger helpfulness ratings tend to accompany with high ratings and long review lengths. Moreover, in the early stage the averaged number of helpful votes per review far outnumber that of the latter stage. In the mean time, the ratings, review lengths and other indexes dramatically ﬂuctuate. These all indicate the importance of keeping a good brand image in the cold start stage.

<!-- b000011 | prose | pages [1] -->
As to question 2(a), we propose three metrics for Sunshine to track: 1. weighted rating ratio which represents the occurring ratio of each rating weighted by number of helpful votes; 2. weighted sentimental score for reviews, where we apply logistic regression to calculate scores for each notional word and their weighted sums by helpfulness; 3.preference vector, where we sort out seven attributes for each product based on LDA’s results , set up dictionaries which consist of related terms for each attribute and estimate people’s preference ratio on these attributes based on weighted word frequency statistics with time decay. As a Result, Sunshine can allocate diﬀerent eﬀorts on improving diﬀerent product features.

<!-- b000012 | prose | pages [1] -->
In question 2(b), we consider that the reputation of a product is related to the averaged star ratings, the authoritativeness of its reviews and the sales volume, among which we assume the sales volume is proportional to the review number in a ﬁxed-length time window. Therefore the reputation over that ﬁxed- length time window can be seen as the joint contribution of features concerning rate and reviews during that period, and after calculation, results show that for hair dryer and paciﬁer, their reputation scores increase in the early time and tend to be stable later, whereas those of microwave keep growing the whole time.

<!-- b000013 | prose | pages [1] -->
With regard to 2(c), we continue to use the time-varying reputation in 2(b) as a comprehensive indicator of both ratings and reviews and apply a nested two-layer LSTM model to predict its value for the review sequence, for considering that this index takes nearly every informative given features into accounts (sales volume included).

<!-- b000014 | prose | pages [1] -->
In terms of 2(d), we consider the ripple eﬀect of reviews. After analyzing the trend of the monthly averaged number of diﬀerent ratings over time, we conclude that reviews with rate 5 tend to incite more reviews. Besides that, we unexpectedly observe that the reviews amount of rate 1 is signiﬁcantly correlated with the length of reviews, and after Granger Cause Test, we ﬁnd that short reviews tend to lag within two months after a large ratio of low star ratings.

<!-- b000015 | prose | pages [1] -->
Regarding 2(e), we sort out a dictionary for aﬀective words exclusively and assign a score for each of them. Then we compute the new sentimental scores of all reviews and rank reviews into ﬁve ranks. After comparing the confusion matrix of star rating and review ranks, we ﬁnd a mapping asymmetricity that some reviews with strongly aﬀective words had mild ratings, and reviews with more mildly aﬀective words has extreme ratings. We explain this phenomena by visualizing that for those reviews, greater chances are that both positive words and negative aﬀective words occur, or strongly aﬀective words are replaced by words that describe product attributes.

<!-- b000016 | prose | pages [1] -->
Last but not least, we summarize the pros and cons of our solutions and present our insights to Sunshine’s market director for the purpose of helping Sunshine take a lead in online market.

<!-- b000017 | prose | pages [1] -->
Key Word: logistic regression; LSTM; LDA topic model; Granger Cause Test; sentiment analysis.

<!-- b000018 | prose | pages [1] -->
关注数学模型

<!-- b000019 | furniture | pages [1] -->
2

<!-- b000020 | furniture | pages [1] -->
MATHmodels

<!-- b000021 | furniture | pages [1] -->
获取更多资讯

<!-- b000022 | furniture | pages [2] -->
Team 2003717

<!-- b000023 | furniture | pages [2] -->
Page 1

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
1

<!-- b000026 | heading | pages [2] -->
Introduction

<!-- b000027 | prose | pages [2] -->
2 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2 Clariﬁcation and Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000028 | prose | pages [2] -->
2 Problem 1: Data Preprocessing and Mining

<!-- b000029 | prose | pages [2] -->
2

<!-- b000030 | prose | pages [2] -->
4 Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 Text Mining by LDA Topic Model[1] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 Overall Data Characteristics 5

<!-- b000031 | prose | pages [2] -->
Problem 2 (a): Ratings and Reviews Based Data Measures 3 8 Weighted Rating Ratio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 8 Avg and Std of Weighted Sentimental Scores for Reviews[2][3][4] . . . . . . . . . . . . . . 3.2 8 Users’ Preference Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3

<!-- b000032 | prose | pages [2] -->
4 Problem 2 (b): Reputation Metric

<!-- b000033 | prose | pages [2] -->
9

<!-- b000034 | prose | pages [2] -->
11 Reputation Metric . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 11 Analysis on Reputation Variation Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2

<!-- b000035 | prose | pages [2] -->
5 Problem 2 (c): Nested Two-Layer LSTM

<!-- b000036 | prose | pages [2] -->
11

<!-- b000037 | prose | pages [2] -->
12 The Structure of the Nested Two-layer LSTM Model 5.1 . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | prose | pages [2] -->
12 Analysis on Potential Success of Products . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 14

<!-- b000039 | prose | pages [2] -->
Problem 2 (d): Causal Eﬀectiveness Between Reveiws 6 15 Ripple Eﬀects of Extreme Ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 15 Causal Inference for Ratio of Low Rating and Review Length . . . . . . . . . . . . . . . . . 6.2 16

<!-- b000040 | prose | pages [2] -->
Problem 2 (e)[5]: Correlation between Aﬀective Words and Star Ratings 7 18 Analysis for Alignment of Rate and Review Scored by Certain Aﬀective Words . . . . . . . 7.1 18 Micro Observation of Asymmetricity between Rate and Review[6] . . . . . . . . . . . . . . 7.2

<!-- b000041 | prose | pages [2] -->
8

<!-- b000042 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000043 | prose | pages [2] -->
18

<!-- b000044 | prose | pages [2] -->
20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 Strengths 20 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000045 | prose | pages [2] -->
9

<!-- b000046 | heading | pages [2] -->
Conclusion

<!-- b000047 | prose | pages [2] -->
21

<!-- b000048 | prose | pages [2] -->
21

<!-- b000049 | heading | pages [2] -->
10 The Letter to the Marketing Director of Sunshine Company

<!-- b000050 | heading | pages [2] -->
Appendices

<!-- b000051 | prose | pages [2] -->
22

<!-- b000052 | prose | pages [2] -->
26

<!-- b000053 | heading | pages [2] -->
Appendix A LDA Topic Model for Microwave and Paciﬁer

<!-- b000054 | prose | pages [2] -->
26

<!-- b000055 | prose | pages [2] -->
Product Contrast of Microwave and Paciﬁer Over Time

<!-- b000056 | heading | pages [2] -->
Appendix B

<!-- b000057 | heading | pages [2] -->
Appendix C Code

<!-- b000058 | prose | pages [2] -->
27

<!-- b000059 | prose | pages [2] -->
27 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.1 Data Preprocess and Overall Analysis 27 LDA Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.2 33 Sentimental Score . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.3 37 LSTM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.4 38 Reputation Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . C.5 40

<!-- b000060 | prose | pages [2] -->
关注数学模型

<!-- b000061 | furniture | pages [2] -->
2

<!-- b000062 | furniture | pages [2] -->
MATHmodels

<!-- b000063 | furniture | pages [2] -->
获取更多资讯

<!-- b000064 | furniture | pages [3] -->
Team 2003717

<!-- b000065 | prose | pages [3] -->
1

<!-- b000066 | heading | pages [3] -->
Introduction

<!-- b000067 | prose | pages [3] -->
1.1 Problem Background

<!-- b000068 | furniture | pages [3] -->
Page 2

<!-- b000069 | prose | pages [3] -->
Nowadays with more and more merchants joining the e-commerce camp, competition in Internet mar- keting has become increasingly intense. Meanwhile, as more and more customers participate in online reviews and interactions, comprehensive analysis of reviews and ratings plays an increasingly important role in understanding customers’ pain points and specifying future strategies.

<!-- b000070 | prose | pages [3] -->
Speciﬁcally speaking, in Amazon’s design, customers are allowed to choose a number from 1 to 5 to express their satisfaction level with the product, write any text-based messages as reviews and freely vote for other reviews they consider helpful. These are the main data sources for related companies to gain insights into the markets in which they participate, the timing of that participation, and the potential success of product design feature choices.

<!-- b000071 | prose | pages [3] -->
1.2 Clariﬁcation and Restatement

<!-- b000072 | prose | pages [3] -->
In this problem we are given three review data sets on three new products by Sunshine Company: a microwave oven, a baby paciﬁer and a hair dryer, and asked to provide the Company with an online sales strategy and important design patterns to enhance the attractiveness of the product. The data sets include product types, star ratings, review titles and bodys, helpfulness votes, certiﬁcation information and date. We should only use these data to solve the following problems:

<!-- b000073 | prose | pages [3] -->
• Analyze the three product data sets, qualitatively or quantitatively measure and describe these data to obtain some quantiﬁable indicators, patterns or relationships to guide product sales plan of Sunshine.

<!-- b000074 | prose | pages [3] -->
• Based on the above analysis, the following special needs should be further addressed:

<!-- b000075 | prose | pages [3] -->
– Design a metric based on the rating and review content to represent the information value of the

<!-- b000076 | prose | pages [3] -->
review, thus providing Sunshine Company with a way to ﬁnd the most valuable review.

<!-- b000077 | prose | pages [3] -->
– Find time-based measures and patterns which indicate whether the market reputation of speciﬁc

<!-- b000078 | prose | pages [3] -->
product is increasing or decreasing.

<!-- b000079 | prose | pages [3] -->
– Identify a combination of text-based measures and ratings-based measures that best indicate the

<!-- b000080 | prose | pages [3] -->
potential success or failure of a product.

<!-- b000081 | prose | pages [3] -->
– Find correlations between star ratings and review properties such as quantity, quality, etc.

<!-- b000082 | prose | pages [3] -->
– Find correlations between star ratings and speciﬁc review words.

<!-- b000083 | prose | pages [3] -->
• Write a letter to the Marketing Director of Sunshine Company by summarizing the analysis and results, and providing rational recommends.

<!-- b000084 | prose | pages [3] -->
1.3 Our Work

<!-- b000085 | prose | pages [3] -->
Our work follows the following workﬂow, as shown in the Fig. 1. The level-1 data is the 15 product properties directly provided in the problem. The level-2 data is based on the level-1 data, including product class, helpfulness rating and emotion measure of the review content. Based on this, level-3 data is further processed into a score that can be used to measure a review’s information value. Then level-4 data, which indicates a reasonable measure of a product’s prospects, is aggregated for a reputation index in problem 2(b)(c).

<!-- b000086 | prose | pages [3] -->
关注数学模型

<!-- b000087 | furniture | pages [3] -->
2

<!-- b000088 | furniture | pages [3] -->
MATHmodels

<!-- b000089 | furniture | pages [3] -->
获取更多资讯

<!-- b000090 | furniture | pages [4] -->
Team 2003717

<!-- b000091 | furniture | pages [4] -->
Page 3

<!-- b000092 | caption | pages [4] -->
Figure 1: Workﬂow

<!-- b000093 | prose | pages [4] -->
• In the problem 1, we simply process the level-2 data, and then analyze the relationship between the review amount, star rating and date, the ratio of various star rating levels, review amount of customers, as well as the relationship between the review amount, review length, star rating and the helpfulness ratings.

<!-- b000094 | prose | pages [4] -->
• In problem 2(a), we propose three metrics: 1. weighted rating ratio, 2. weighted sentimental score, 3. preference vector. They depict the attributes of a review from the perspectives of star rating, emotion and what reviewers care about. Further, we can measure the value of reviews from these three dimensions in needs.

<!-- b000095 | prose | pages [4] -->
• In problem 2(b), we consider the reputation of a product in a ﬁxed-length time window as a joint contribution of total review number, averaged rate, helpful votes, review readability and averaged sentimental scores of reviews over that period. And after calculation, we observe its changing values for each product over time.

<!-- b000096 | prose | pages [4] -->
• In problem 2(c), we continue to use the time-varying reputation in 2(b) as a comprehensive index of both ratings and reviews and LSTM is applied to predict their values in the next 1000 reviews. Since we assume the sales amount is proportional to the total review number, the reputation is associated with the sales and takes nearly every informative given features into accounts (sales amount included). Also because the training and testing losses of LSTM are too small to be valued, we are conﬁdent in the power of this index.

<!-- b000097 | prose | pages [4] -->
• In problem 2(d), we consider the ripple eﬀect of reviews. After analyzing the trend of the monthly average number of diﬀerent star ratings over time, we conclude that reviews with a score of 5 often lead to more reviews. Furthermore, we unexpectedly ﬁnd that the reviews amount of star ratings 1 is signiﬁcantly correlated with the length of reviews, and after Granger Cause Test, we ﬁnd that short reviews tend to lag within two months after a large ratio of low star ratings.

<!-- b000098 | prose | pages [4] -->
• In problem 2(e), we extract the emotion words , score and rank the reviews based on the words. After comparing the confusion matrix of rating and review ranks, we ﬁnd some mapping asymmetricity that some reviews with strongly aﬀective words have mild ratings, and reviews with more mildly aﬀective

<!-- b000099 | prose | pages [4] -->
关注数学模型

<!-- b000100 | furniture | pages [4] -->
2

<!-- b000101 | furniture | pages [4] -->
MATHmodels

<!-- b000102 | furniture | pages [4] -->
获取更多资讯

<!-- b000103 | furniture | pages [5] -->
Team 2003717

<!-- b000104 | furniture | pages [5] -->
Page 4

<!-- b000105 | prose | pages [5] -->
words have extreme ratings. We explain this phenomena by showing that for those reviews, greater chances are that both positive words and negative aﬀective words occur, or strongly aﬀective words are replaced by words that described product properties.

<!-- b000106 | prose | pages [5] -->
Problem 1: Data Preprocessing and Mining 2

<!-- b000107 | prose | pages [5] -->
In this section, we preprocess the data set and analyze the relationship between review amount, star rating, helpfulness rating, customer and date, and present some ﬁndings.

<!-- b000108 | prose | pages [5] -->
2.1 Data Cleaning

<!-- b000109 | heading | pages [5] -->
1. General Data Cleaning:

<!-- b000110 | prose | pages [5] -->
The given data set presents 15 properties for the three products: hair dryer, microwave and paciﬁer. In all of these properties, marketplace which is either "US" or "us", review id which is unique for all items and product category which is exclusive for these three products, are useless for our subsequent analysis and we simply delete the three properties. For vine and veriﬁed purchase, we replace all n and N with N, and all y and Y with Y. Then we clean all given texts by replacing some special Chinese characters with equivalent ASCII characters as much as possible, and eliminating the remaining special garbled codes and symbols, for further text-based emotion analysis and keyword extraction. In the end, we eliminate 214 unqualiﬁed items and leave 11424, 1606 and 18784 items for hair dryer,microwave and paciﬁer, respectively.

<!-- b000111 | heading | pages [5] -->
2. Text Data Pre-processing[7]:

<!-- b000112 | prose | pages [5] -->
(a) Tokenization: Split texts into sentences and sentences into words. Lowercase words and remove

<!-- b000113 | prose | pages [5] -->
punctuation.

<!-- b000114 | prose | pages [5] -->
(b) Words that have fewer than 3 characters are removed. All stopwords are removed.

<!-- b000115 | prose | pages [5] -->
(c) Words are lemmatized: words in third person are changed to ﬁrst person and verbs in past and

<!-- b000116 | prose | pages [5] -->
future tenses are changed into present.

<!-- b000117 | prose | pages [5] -->
(d) Words are stemmed: words are reduced to their root form.

<!-- b000118 | prose | pages [5] -->
2.2

<!-- b000119 | heading | pages [5] -->
Text Mining by LDA Topic Model[1]

<!-- b000120 | prose | pages [5] -->
Since the review texts are rich and complex, it is of great importance to dig out the topic words so as to clearly grasp what consumers really care about. And here we accomplish this task by applying the Latent Dirichlet Allocation (LDA) model, a powerful NLP method for topic word extraction.

<!-- b000121 | prose | pages [5] -->
By simply running the standard python codes of LDA, we get results that will be useful in the subsequent estimation of users’ preference vectors. We show results of LDA for hair dryer in Fig. 2, and the rest results can be seen in the Appendix. A.

<!-- b000122 | prose | pages [5] -->
关注数学模型

<!-- b000123 | furniture | pages [5] -->
2

<!-- b000124 | furniture | pages [5] -->
MATHmodels

<!-- b000125 | furniture | pages [5] -->
获取更多资讯

<!-- b000126 | furniture | pages [6] -->
Team 2003717

<!-- b000127 | furniture | pages [6] -->
Page 5

<!-- b000128 | caption | pages [6] -->
Figure 2: LDA topic model for hair dryer

<!-- b000129 | prose | pages [6] -->
2.3 Overall Data Characteristics

<!-- b000130 | prose | pages [6] -->
First, we analyze the changes of some main features over time[8]: We visualize the review amount of three products each month in Fig. 3(a) and observe that the reviews amount has increased exponentially over time. Besides that, the averaged rating score per month is further calculated and displayed, where reviews which occur less than 2 times in a month are not included in the statistics, as shown in Fig. 3(b):

<!-- b000131 | prose | pages [6] -->
1. The averaged review rating of all three products is generally between 3.5 and 4.5.

<!-- b000132 | prose | pages [6] -->
2. The rating scores tend to converge over time.

<!-- b000133 | prose | pages [6] -->
3. The reputation of microwave seems to be continuously increasing in recent years.

<!-- b000134 | prose | pages [6] -->
(a) Review amount per month (b) Rating score per month

<!-- b000135 | caption | pages [6] -->
Figure 3: Review status over time

<!-- b000136 | prose | pages [6] -->
In order to understand the distribution of review ratings, we plot the proportion of ﬁve ratings for three products, shown in Fig. 4(a). Obviously, most of the ratings are 5 and the next most are 4, where microwave

<!-- b000137 | prose | pages [6] -->
关注数学模型

<!-- b000138 | furniture | pages [6] -->
2

<!-- b000139 | furniture | pages [6] -->
MATHmodels

<!-- b000140 | furniture | pages [6] -->
获取更多资讯

<!-- b000141 | furniture | pages [7] -->
Team 2003717

<!-- b000142 | furniture | pages [7] -->
Page 6

<!-- b000143 | prose | pages [7] -->
is an exception for owning too many 1 star ratings. This may be partly because microwave ovens are not easy to be accepted in the early stage.

<!-- b000144 | prose | pages [7] -->
Next we count the number of reviews of each customer and take the logarithm of the Y-axis to avoid a large diﬀerence in the order of magnitude. As can be seen in Fig. 4(b), most customers only review once, and only a few customers review more than 5 times.

<!-- b000145 | prose | pages [7] -->
Fig. 4(c) shows that most of the review votes are useful, where we only consider reviews with more than 10 votes, which represent the review quality appropriately.

<!-- b000146 | prose | pages [7] -->
(b) Customer amount by review number (a) Review percent per rating (c) Review amount by helpful percent

<!-- b000147 | caption | pages [7] -->
Figure 4: Review amount from diﬀerent angles

<!-- b000148 | prose | pages [7] -->
To further understand the characteristics of reviews with high helpfulness ratings, we display the averaged review length and averaged star rating in Fig. 5. Besides, the time-varying averaged helpful votes of each review are shown in Fig. 6.

<!-- b000149 | prose | pages [7] -->
1. In Fig. 5, reviews with higher helpfulness ratings tend to have more words and higher star ratings, possibly for the reason that too short reviews are easily ignored, few customers will write long reviews with nonsense, or they will lose their interests in a product after seeing low ratings and quickly leave without giving a certiﬁcate for reviews they’ve just seen, etc.

<!-- b000150 | prose | pages [7] -->
2. In Fig. 6, helpful votes of a single review in the early stage far outnumber the those in the recent period. This may be because in the early stage there are too few comments for people to refer to, thus people naturally attach more importance of each comment in the cold start period. Moreover, reviews with more helpful votes may be displayed in the front of the comment zone, which enlarges their probabilities to get more votes. As stated in [9] and [10], the above phenomenon are called early birds bias and winner circle bias, respectively.

<!-- b000151 | prose | pages [7] -->
(a) Average review length of helpful percent (b) Star rating of helpful percent

<!-- b000152 | caption | pages [7] -->
Figure 5: Review status by helpful percent

<!-- b000153 | prose | pages [7] -->
关注数学模型

<!-- b000154 | furniture | pages [7] -->
2

<!-- b000155 | furniture | pages [7] -->
MATHmodels

<!-- b000156 | furniture | pages [7] -->
获取更多资讯

<!-- b000157 | furniture | pages [8] -->
Team 2003717

<!-- b000158 | furniture | pages [8] -->
Page 7

<!-- b000159 | caption | pages [8] -->
Figure 6: Time-varying average number of helpful votes for diﬀerent ratings

<!-- b000160 | prose | pages [8] -->
In addition, we conduct a detailed analysis of various commodities under the three products to ﬁnd out the relationship between the review amount and the averaged star rating and the averaged length of reviews on the same commodity. The results in hair dryer data set are shown in Fig. 7, and the rest are shown in the Appendix B. We can ﬁnd it seems that longer reviews are often followed by improved ratings, and longer periods of high ratings will lead to an increase of reviews, which partly reﬂects the increase on sales.

<!-- b000161 | caption | pages [8] -->
Figure 7: Product contrast of hair dryer over time

<!-- b000162 | prose | pages [8] -->
Based on our previous analysis, Sunshine Company should note that:

<!-- b000163 | prose | pages [8] -->
1. The number of reviews has increased rapidly in recent years, which reﬂects the importance of Sunshine’s frequent interaction with reviewers.

<!-- b000164 | prose | pages [8] -->
2. The star rating will experience large ﬂuctuations in the early stage of the product launch, during which time the brand image should be maintained cautiously.

<!-- b000165 | prose | pages [8] -->
关注数学模型

<!-- b000166 | furniture | pages [8] -->
2

<!-- b000167 | furniture | pages [8] -->
MATHmodels

<!-- b000168 | furniture | pages [8] -->
获取更多资讯

<!-- b000169 | furniture | pages [9] -->
Team 2003717

<!-- b000170 | furniture | pages [9] -->
Page 8

<!-- b000171 | prose | pages [9] -->
3. Since reviews with high star ratings and more words tend to get more helpful votes, Sunhine had better closely watch out this type of reviews and discover customers’ pain points based on them[11].

<!-- b000172 | prose | pages [9] -->
Problem 2 (a): Ratings and Reviews Based Data Measures 3

<!-- b000173 | prose | pages [9] -->
We design three types of data measures based on ratings and reviews that are informative for Sunshine Company to track, i.e. weighted rating ratio, averages and standard deviations of weighted sentimental scores for reviews and users preference vectors.

<!-- b000174 | prose | pages [9] -->
3.1 Weighted Rating Ratio

<!-- b000175 | prose | pages [9] -->
1. For 𝑖∈[5], denote the timestamps when a new rating i is created as 𝐴𝑖.

<!-- b000176 | prose | pages [9] -->
2. For the timestamp 𝑗∈𝐴𝑖, denote the number of helpful votes at time j as 𝐻𝑁𝑗.

<!-- b000177 | prose | pages [9] -->
3. Assign a weight of 𝐻𝑁𝑗+1 to time j, and we obtain that the weighted ratio for rating i can be formulated as

<!-- b000178 | prose | pages [9] -->
∑

<!-- b000179 | prose | pages [9] -->
𝑤𝑟𝑟𝑖=

<!-- b000180 | prose | pages [9] -->
∑

<!-- b000181 | prose | pages [9] -->
𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1)

<!-- b000182 | prose | pages [9] -->
∑

<!-- b000183 | prose | pages [9] -->
𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1)

<!-- b000184 | prose | pages [9] -->
𝑖∈[5]

<!-- b000185 | prose | pages [9] -->
𝑤𝑟𝑟𝑖represents the occuring ratio of rating i weighted by helpfulness among all ﬁve ratings.

<!-- b000186 | prose | pages [9] -->
According to the formula above and the given data, we obtain the 𝑤𝑟𝑟𝑖values as follows Fig. 8:

<!-- b000187 | caption | pages [9] -->
Figure 8: Weighted rating ratio of diﬀerent rating for diﬀerent product

<!-- b000188 | prose | pages [9] -->
Avg and Std of Weighted Sentimental Scores for Reviews[2][3][4] 3.2

<!-- b000189 | prose | pages [9] -->
1. Calculate the normalized sentimental scores of notional words appearing in the review texts by logistic regression Algorithm 1:

<!-- b000190 | prose | pages [9] -->
Note: The reason for which we adopt logistic regression[4] is that normally the sentimental scores of negative words are negative, those of positive words are positive and those of neutral words should be zero. The sigmoid function in logistic regression happens to symmetrically map R into [0, 1] with zero as the center of x axis. As a result, S can be naturally solved by this method.

<!-- b000191 | prose | pages [9] -->
关注数学模型

<!-- b000192 | furniture | pages [9] -->
2

<!-- b000193 | furniture | pages [9] -->
MATHmodels

<!-- b000194 | furniture | pages [9] -->
获取更多资讯

<!-- b000195 | furniture | pages [10] -->
Team 2003717

<!-- b000196 | heading | pages [10] -->
Algorithm 1: Logistic Regression

<!-- b000197 | furniture | pages [10] -->
Page 9

<!-- b000198 | prose | pages [10] -->
Input: notional words set W = {𝑤1, · · · , 𝑤𝑛}, review set {𝑟𝑒𝑡}𝑡∈𝑇and rating sets {𝑟𝑎𝑡}𝑡∈𝑇. Output: sentimental scores S = {𝑠1, · · · , 𝑠𝑛} Map 𝑟𝑎𝑡to 𝑦𝑡by {1 : 0, 2 : 0.25, 3 : 0.5, 4 : 0.75, 5 : 1}.

<!-- b000199 | prose | pages [10] -->
∑

<!-- b000200 | prose | pages [10] -->
1

<!-- b000201 | prose | pages [10] -->
𝑠∈𝑆𝑠1𝑠{𝑟𝑒𝑡} )2

<!-- b000202 | prose | pages [10] -->
S = 𝑎𝑟𝑔𝑚𝑖𝑛𝑆

<!-- b000203 | prose | pages [10] -->
𝑡∈[𝑇](𝑦1 − ∑ 1+𝑒

<!-- b000204 | prose | pages [10] -->
where 1𝑠{𝑟𝑒𝑡} = 1 if the notional word s occurred in the t-th review, otherwise 0.

<!-- b000205 | prose | pages [10] -->
2. For 𝑡∈[𝑡], denote the sentimental score of the t-th review as 𝑠𝑠𝑡, and we obtain that

<!-- b000206 | prose | pages [10] -->
𝑠𝑠𝑡=

<!-- b000207 | prose | pages [10] -->
∑

<!-- b000208 | prose | pages [10] -->
𝑠1𝑠{𝑟𝑒𝑡}

<!-- b000209 | prose | pages [10] -->
𝑠∈𝑆

<!-- b000210 | prose | pages [10] -->
Then the weighted averaged reviews’ sentimental score for rating i can be formulated

<!-- b000211 | prose | pages [10] -->
∑

<!-- b000212 | prose | pages [10] -->
∑

<!-- b000213 | prose | pages [10] -->
𝑎𝑣𝑔𝑖=

<!-- b000214 | prose | pages [10] -->
𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1) × 𝑠𝑠𝑗

<!-- b000215 | prose | pages [10] -->
∑

<!-- b000216 | prose | pages [10] -->
𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1)

<!-- b000217 | prose | pages [10] -->
𝑖∈[5]

<!-- b000218 | prose | pages [10] -->
and the weighted standard deviation of reviews’ sentimental score for rating i can be formulated

<!-- b000219 | prose | pages [10] -->
√∑

<!-- b000220 | prose | pages [10] -->
𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1) × (𝑠𝑠𝑖−𝑎𝑣𝑔𝑖)2

<!-- b000221 | prose | pages [10] -->
∑

<!-- b000222 | prose | pages [10] -->
𝑠𝑡𝑑𝑖=

<!-- b000223 | prose | pages [10] -->
∑

<!-- b000224 | prose | pages [10] -->
𝑗∈𝐴𝑖(𝐻𝑁𝑗+ 1)

<!-- b000225 | prose | pages [10] -->
𝑖∈[5]

<!-- b000226 | prose | pages [10] -->
According to the formula above and the given data, we obtain the 𝑎𝑣𝑔𝑖, 𝑎𝑣𝑔𝑖values as follows Fig. 9:

<!-- b000227 | prose | pages [10] -->
(a) Weighted Average (b) Weighted Std

<!-- b000228 | caption | pages [10] -->
Figure 9: Weighted sentimental score index of reviews for diﬀerent ratings

<!-- b000229 | prose | pages [10] -->
3.3 Users’ Preference Vector

<!-- b000230 | prose | pages [10] -->
Since requirement measurements are fundamental to product positioning and strategic marketing de- velopment, we attach great importance to computing the preference vectors of consumers by analyzing the review data.

<!-- b000231 | prose | pages [10] -->
Owing to the topic analysis by the Latent Dirichlet Allocation (LDA) model and detailed observations of product reviews, we identify eight main product attributes for hair dryer, microwave and paciﬁer respectively. Lexicons of 46, 51 and 45 words are constructed to identify the attribute terms in the product reviews. The classiﬁed attributes and relative number of terms are described in Table 1.

<!-- b000232 | prose | pages [10] -->
关注数学模型

<!-- b000233 | furniture | pages [10] -->
2

<!-- b000234 | furniture | pages [10] -->
MATHmodels

<!-- b000235 | furniture | pages [10] -->
获取更多资讯

<!-- b000236 | furniture | pages [11] -->
Team 2003717

<!-- b000237 | furniture | pages [11] -->
Page 10

<!-- b000238 | caption | pages [11] -->
Table 1: Classiﬁed attributes and relative number of terms

<!-- b000239 | prose | pages [11] -->
Microwave Hair dryer Paciﬁer

<!-- b000240 | prose | pages [11] -->
Attribute

<!-- b000241 | prose | pages [11] -->
Attribute Num

<!-- b000242 | prose | pages [11] -->
Num

<!-- b000243 | prose | pages [11] -->
Attribute Num

<!-- b000244 | prose | pages [11] -->
Lifespan

<!-- b000245 | prose | pages [11] -->
Lifespan 5 Weight 3

<!-- b000246 | prose | pages [11] -->
Weight 5

<!-- b000247 | prose | pages [11] -->
Lifespan 5

<!-- b000248 | prose | pages [11] -->
3

<!-- b000249 | prose | pages [11] -->
Size and shape 9

<!-- b000250 | prose | pages [11] -->
After-sales service

<!-- b000251 | prose | pages [11] -->
After-sales service 9 Heat 3

<!-- b000252 | prose | pages [11] -->
Heat 9

<!-- b000253 | prose | pages [11] -->
Packing 8

<!-- b000254 | prose | pages [11] -->
3

<!-- b000255 | prose | pages [11] -->
Softness 3

<!-- b000256 | prose | pages [11] -->
Materials&Structure

<!-- b000257 | prose | pages [11] -->
Materials&Structure 19 Price 3

<!-- b000258 | prose | pages [11] -->
Cost

<!-- b000259 | prose | pages [11] -->
Safety 4

<!-- b000260 | prose | pages [11] -->
Safety 24

<!-- b000261 | prose | pages [11] -->
Materials&Structure 13

<!-- b000262 | prose | pages [11] -->
3

<!-- b000263 | prose | pages [11] -->
Cost 3

<!-- b000264 | prose | pages [11] -->
4

<!-- b000265 | prose | pages [11] -->
Safety 4

<!-- b000266 | prose | pages [11] -->
Next is to estimate users’ preference ratio for each attribute.

<!-- b000267 | prose | pages [11] -->
Taking the hair dryer product as an example, we denote users’ preference degree and preference ratio for attribute i as 𝑃𝐷𝑖and 𝑃𝑅𝑖. Then it holds 𝑃𝑅𝑖= ∑

<!-- b000268 | prose | pages [11] -->
To calculate 𝑃𝐷𝑖, we must clarify that

<!-- b000269 | prose | pages [11] -->
𝑃𝐷𝑖

<!-- b000270 | prose | pages [11] -->
𝑗∈[8] 𝑃𝐷𝑗.

<!-- b000271 | prose | pages [11] -->
1. The older the review is, the less importance it is in 𝑃𝐷𝑖.

<!-- b000272 | prose | pages [11] -->
2. Reviews with neutral ratings are attached little importance in 𝑃𝐷𝑖.

<!-- b000273 | prose | pages [11] -->
3. The more helpful votes the review has, the more weight it takes up in 𝑃𝐷𝑖.

<!-- b000274 | prose | pages [11] -->
Based on the considerations above, we deﬁne 𝑃𝐷𝑖= ∑

<!-- b000275 | prose | pages [11] -->
∑

<!-- b000276 | prose | pages [11] -->
𝑡∈𝑇(|𝑟𝑎𝑡−3| + 0.5) × 1𝑖𝑡× (𝐻𝑁𝑡+ 1), hence

<!-- b000277 | prose | pages [11] -->
𝑡∈𝑇𝛾1−𝑡(|𝑟𝑎𝑡−3| + 0.5) × 1𝑖𝑡× (𝐻𝑁𝑡+ 1)

<!-- b000278 | prose | pages [11] -->
𝑃𝑅𝑖=

<!-- b000279 | prose | pages [11] -->
∑

<!-- b000280 | prose | pages [11] -->
∑

<!-- b000281 | prose | pages [11] -->
𝑡∈𝑇𝛾1−𝑡(|𝑟𝑎𝑡−3| + 0.5) × 1𝑖𝑡× (𝐻𝑁𝑡+ 1)

<!-- b000282 | prose | pages [11] -->
𝑖∈[8]

<!-- b000283 | prose | pages [11] -->
where 𝛾is a discounted factor of time, and we set it to be 0.999. According to the formula above and the given data, diﬀerent users’ preference vectors of three products are displayed in Table 2:

<!-- b000284 | caption | pages [11] -->
Table 2: Classiﬁed attributes and relative weights in reviews

<!-- b000285 | prose | pages [11] -->
Microwave Hair dryer 𝑃𝑅 Paciﬁer

<!-- b000286 | prose | pages [11] -->
𝑃𝑅

<!-- b000287 | prose | pages [11] -->
𝑃𝑅

<!-- b000288 | prose | pages [11] -->
Attribute

<!-- b000289 | prose | pages [11] -->
Attribute

<!-- b000290 | prose | pages [11] -->
Attribute

<!-- b000291 | prose | pages [11] -->
Lifespan

<!-- b000292 | prose | pages [11] -->
Lifespan 0.136 Weight 0.035

<!-- b000293 | prose | pages [11] -->
Weight 0.161

<!-- b000294 | prose | pages [11] -->
Lifespan 0.064

<!-- b000295 | prose | pages [11] -->
0.016

<!-- b000296 | prose | pages [11] -->
Size and shape 0.285

<!-- b000297 | prose | pages [11] -->
After-sales service

<!-- b000298 | prose | pages [11] -->
After-sales service 0.143 Heat 0.152

<!-- b000299 | prose | pages [11] -->
Heat 0.191

<!-- b000300 | prose | pages [11] -->
Packing 0.157

<!-- b000301 | prose | pages [11] -->
0.094

<!-- b000302 | prose | pages [11] -->
Softness 0.076

<!-- b000303 | prose | pages [11] -->
Materials&Structure

<!-- b000304 | prose | pages [11] -->
Materials&Structure 0.250 Price 0.049

<!-- b000305 | prose | pages [11] -->
Cost

<!-- b000306 | prose | pages [11] -->
Safety 0.235

<!-- b000307 | prose | pages [11] -->
Safety 0.324

<!-- b000308 | prose | pages [11] -->
Materials&Structure 0.291

<!-- b000309 | prose | pages [11] -->
0.048

<!-- b000310 | prose | pages [11] -->
Cost 0.020

<!-- b000311 | prose | pages [11] -->
0.166

<!-- b000312 | prose | pages [11] -->
Safety 0.107

<!-- b000313 | prose | pages [11] -->
Having computed the preference vectors, the Sunshine Company can readjust its strategies accordingly. Taking hair dryer as an example, the preference ratio of safety, materials quality, heat, lifespan and after sales service take up nearly 90 percentage, therefore the Sunshine Company should pay more attention to these attributes and assign proper funds to improve these aspects by their preference ratios respectively.

<!-- b000314 | prose | pages [11] -->
关注数学模型

<!-- b000315 | furniture | pages [11] -->
2

<!-- b000316 | furniture | pages [11] -->
MATHmodels

<!-- b000317 | furniture | pages [11] -->
获取更多资讯

<!-- b000318 | furniture | pages [12] -->
Team 2003717

<!-- b000319 | prose | pages [12] -->
4 Problem 2 (b): Reputation Metric

<!-- b000320 | prose | pages [12] -->
4.1 Reputation Metric

<!-- b000321 | furniture | pages [12] -->
Page 11

<!-- b000322 | prose | pages [12] -->
The reputation of a product is related to many factors (e.g.

<!-- b000323 | prose | pages [12] -->
the average star rating it receives, the authoritativeness of its reviews [12][13] and the sales volume). As we assume that the sales volume over a period of time is in proportion to the number of reviews the product receives. The reputation score a product earns over a period of time can be seen as the joint contribution of all reviews it receives, which indicating both the quality and sales volume.

<!-- b000324 | prose | pages [12] -->
Here we deﬁne a function R(𝑟𝑖), which maps an instance of review 𝑟𝑖(𝑟𝑖contains any information we might use from the review 𝑖) into a scalar indicating the contribution of the review to the reputation for the product. Taking plenty of factors into account, the contribution score R can be formulated as:

<!-- b000325 | prose | pages [12] -->
1 𝑡𝑖+ 1 (𝑤𝑟𝑟𝑖× 𝛼𝑣𝑖𝑛𝑒× 𝛼𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑× 𝑟𝑎𝑡𝑖𝑛𝑔𝑖) R(𝑟𝑖) = (1)

<!-- b000326 | prose | pages [12] -->
The scaling parameter 𝑡is the time interval (unit: day) between 𝑟𝑖and the last review. The larger the time interval, the less reviews the product receives, indicating less sales volume during that period of time. 𝑤𝑟𝑟𝑖 is the weighted rate radio calculated in problem 2(a), which contains the information of helpful votes. The ratio 𝛼𝑣𝑖𝑛𝑒and 𝛼𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑is formulated as:

<!-- b000327 | prose | pages [12] -->
{ 𝛼𝑣𝑖𝑛𝑒= 0.2 ∗𝑣𝑖𝑛𝑒+ 0.8

<!-- b000328 | prose | pages [12] -->
(2) 𝛼𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑= 0.2 ∗𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑+ 0.8

<!-- b000329 | prose | pages [12] -->
where we set the parameter 𝑣𝑖𝑛𝑒and 𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑑to 1 if the review has "vine" or "veriﬁed purchase" tags. Otherwise we set them to 0.

<!-- b000330 | prose | pages [12] -->
Next, a sliding window with size 𝑚is applied to the review table. A successive sequence of reviews, representing a period of time, constructs the average reputation score the product earns during that time:

<!-- b000331 | prose | pages [12] -->
𝑖= 1

<!-- b000332 | prose | pages [12] -->
𝑟𝑒𝑝𝑝

<!-- b000333 | prose | pages [12] -->
∑ 𝑚−1

<!-- b000334 | prose | pages [12] -->
R(𝑟𝑖+𝑗) (3)

<!-- b000335 | prose | pages [12] -->
𝑚 𝑚

<!-- b000336 | prose | pages [12] -->
𝑗=0

<!-- b000337 | prose | pages [12] -->
Analysis on Reputation Variation Patterns 4.2

<!-- b000338 | prose | pages [12] -->
By applying the sliding window strategy above to formulate the average reputation score, we can get a pattern of reputation variation with smooth changes because the diﬀerence between adjacent reputation scores is scaled by the window size 𝑚:

<!-- b000339 | prose | pages [12] -->
𝑖= 1

<!-- b000340 | prose | pages [12] -->
𝑟𝑒𝑝𝑝

<!-- b000341 | prose | pages [12] -->
𝑖+1 −𝑟𝑒𝑝𝑝

<!-- b000342 | prose | pages [12] -->
𝑚(R(𝑖+ 𝑚) −R(𝑖)) (4)

<!-- b000343 | prose | pages [12] -->
In this section, we set the window size 𝑚equal to 200 and 500. As shown in Fig. 10 and Fig. 11, the larger the window size 𝑚is, more violently the reputation curves ﬂuctuate.

<!-- b000344 | prose | pages [12] -->
关注数学模型

<!-- b000345 | furniture | pages [12] -->
2

<!-- b000346 | furniture | pages [12] -->
MATHmodels

<!-- b000347 | furniture | pages [12] -->
获取更多资讯

<!-- b000348 | furniture | pages [13] -->
Team 2003717

<!-- b000349 | furniture | pages [13] -->
Page 12

<!-- b000350 | caption | pages [13] -->
Figure 10: Reputation score of three products over time with window size 𝑚= 200

<!-- b000351 | caption | pages [13] -->
Figure 11: Reputation score of three products over time with window size 𝑚= 500

<!-- b000352 | prose | pages [13] -->
Although diﬀerent window size 𝑚results in diﬀerent volatility of the reputation curve, they all generally have the same variation patterns for each product. For hair dryer and paciﬁer, their reputation scores increase in the early time and tend to be stable later. For microwave, its reputation score keeps growing the whole time. These trends also roughly correspond to the pattern of star ratings shown in Fig. 3, which is a lateral support for the correctness of our reputation metric.

<!-- b000353 | prose | pages [13] -->
Problem 2 (c): Nested Two-Layer LSTM 5

<!-- b000354 | heading | pages [13] -->
The Structure of the Nested Two-layer LSTM Model

<!-- b000355 | prose | pages [13] -->
5.1

<!-- b000356 | prose | pages [13] -->
For problem 2(c), we continue using the reputation score 𝑟𝑒𝑝𝑝

<!-- b000357 | prose | pages [13] -->
𝑖as the metric representing the success of a product. A potentially successful or failing product means that the reputation score keeps increasing or decreasing in the future and reach a threshold value. To predict the reputation score, we use Long and Short-Term Memory (LSTM)[14][15] to model the variation pattern of the review sequence.

<!-- b000358 | prose | pages [13] -->
LSTM model is a variant of recurrent neural network (RNN). It is well-suited to classifying, processing and making predictions based on time series data. A common LSTM unit is composed of a cell, an input gate, an output gate and a forget gate. The cell remembers values over arbitrary time intervals and the three gates regulate the ﬂow of information into and out of the cell. The structure of our nested two-layer LSTM model is shown in Fig. 12. The model can be divided into three separate modules: input module, LSTM module and output module.

<!-- b000359 | prose | pages [13] -->
关注数学模型

<!-- b000360 | furniture | pages [13] -->
2

<!-- b000361 | furniture | pages [13] -->
MATHmodels

<!-- b000362 | furniture | pages [13] -->
获取更多资讯

<!-- b000363 | furniture | pages [14] -->
Team 2003717

<!-- b000364 | furniture | pages [14] -->
Page 13

<!-- b000365 | caption | pages [14] -->
Figure 12: The structure of nested two-layer LSTM model

<!-- b000366 | heading | pages [14] -->
1. Input Module

<!-- b000367 | prose | pages [14] -->
For each review instance at a time stamp, we ﬁrst feed the review text (combining both review headline and review body) into the embedding system to generate the sentence embedding 𝑣𝑠which is represented as a 200-dimension vector. Then we generate the input vector 𝑣𝑖𝑛𝑝𝑢𝑡for the 2-layer LSTM model with 200-dimension hidden size by concatenating sentence embedding and other useful features, which is represented as a 6-dimension feature vector 𝑣𝑓. More information about the feature vector 𝑣𝑓is shown in Table 3.

<!-- b000368 | caption | pages [14] -->
Table 3: Feature Deﬁnition of Vector 𝑣𝑓

<!-- b000369 | prose | pages [14] -->
Deﬁnition Dimension 𝑥1 Domain {1, 2, 3, 4, 5} Star rating 𝑥2 [0, 1] Helpful rating 𝑥3 {0, 1} This review is vine voice or not 𝑥4 {0, 1} This review is veriﬁed purchase or not 𝑥5 [0, 1] The readability of this review 𝑥6 N Time interval (Unit: day) between this review and the last one

<!-- b000370 | prose | pages [14] -->
All the features above are already deﬁned in the previous sections. Therefore, the input vector for the LSTM can be formulated as:

<!-- b000371 | prose | pages [14] -->


<!-- b000372 | prose | pages [14] -->
𝑣𝑠= 𝑊𝑜𝑟𝑑𝐸𝑚𝑏𝑒𝑑(𝑟𝑒𝑣𝑖𝑒𝑤ℎ𝑒𝑎𝑑𝑙𝑖𝑛𝑒+ 𝑟𝑒𝑣𝑖𝑒𝑤𝑏𝑜𝑑𝑦) ∈R200

<!-- b000373 | prose | pages [14] -->
𝑣𝑓= [𝑥1, 𝑥2, 𝑥3, 𝑥4, 𝑥5, 𝑥6] ∈R6

<!-- b000374 | prose | pages [14] -->


<!-- b000375 | prose | pages [14] -->
(5)

<!-- b000376 | prose | pages [14] -->
𝑥= 𝑣𝑖𝑛𝑝𝑢𝑡= [𝑣𝑠, 𝑣𝑓] ∈R206

<!-- b000377 | heading | pages [14] -->
2. LSTM Module

<!-- b000378 | prose | pages [14] -->
The workﬂow of one-layer LSTM unit is shown below:

<!-- b000379 | prose | pages [14] -->
关注数学模型

<!-- b000380 | furniture | pages [14] -->
2

<!-- b000381 | furniture | pages [14] -->
MATHmodels

<!-- b000382 | furniture | pages [14] -->
获取更多资讯

<!-- b000383 | furniture | pages [15] -->
Team 2003717

<!-- b000384 | prose | pages [15] -->


<!-- b000385 | furniture | pages [15] -->
Page 14

<!-- b000386 | prose | pages [15] -->
𝑖= 𝜎(𝑊𝑖𝑖𝑥+ 𝑏𝑖𝑖+ 𝑊ℎ𝑖ℎ+ 𝑏ℎ𝑖)

<!-- b000387 | prose | pages [15] -->
𝑓= 𝜎(𝑊𝑖𝑓𝑥+ 𝑏𝑖𝑓+ 𝑊ℎ𝑓ℎ+ 𝑏ℎ𝑓) 𝑔= tanh(𝑊𝑖𝑔𝑥+ 𝑏𝑖𝑔+ 𝑊ℎ𝑜ℎ+ 𝑏ℎ𝑜)

<!-- b000388 | prose | pages [15] -->
(6)

<!-- b000389 | prose | pages [15] -->
𝑜= 𝜎(𝑊𝑖𝑜𝑥+ 𝑏𝑖𝑜+ 𝑊ℎ𝑜ℎ+ 𝑏ℎ𝑜)

<!-- b000390 | prose | pages [15] -->


<!-- b000391 | prose | pages [15] -->
′ = 𝑓∗𝑐+ 𝑖∗𝑔

<!-- b000392 | prose | pages [15] -->
𝑐

<!-- b000393 | prose | pages [15] -->
′ = 𝑜∗tanh(𝑐

<!-- b000394 | prose | pages [15] -->
ℎ

<!-- b000395 | prose | pages [15] -->
′)

<!-- b000396 | prose | pages [15] -->
The notations for equations above is shown in Table 4:

<!-- b000397 | caption | pages [15] -->
Table 4: Notations for one-layer LSTM

<!-- b000398 | prose | pages [15] -->
Symbol 𝑥∈R206 Deﬁnition The concatenated input vector for the LSTM ℎ∈R200 Hidden state, containing encoded information for the sequence ﬂow 𝑐∈R200 Cell state, tracking dependencies between the elements in the input sequence 𝑖∈R200 Input gate, controlling the extent to which a new value ﬂows into the cell 𝑓∈R200 Forget gate, controlling the extent to which a value remains in the cell 𝑔∈R200 Gathered input value from input 𝑥and current hidden state 𝑜∈R200 Output gate, controlling the extent to which the cell is used to compute outputs 𝑊 The weight matrix for transitions 𝑏 The bias for transitions 𝜎 The sigmoid function The hyperbolic tangent function tanh

<!-- b000399 | prose | pages [15] -->
As for our nested two-layer LSTM, a LSTM unit is overlaid with another LSTM unit. We feed the hidden state of the bottom LSTM into the upper LSTM again and use the hidden state from the upper state as the input for the output module.

<!-- b000400 | heading | pages [15] -->
3. Output Module

<!-- b000401 | prose | pages [15] -->
In the output module, we simply feed the hidden state of the upper LSTM into a linear layer to make predictions on the feature vector, which has the same structure as 𝑣𝑖𝑛𝑝𝑢𝑡in the input module.

<!-- b000402 | prose | pages [15] -->
𝑣𝑝𝑟𝑒𝑑= 𝑊𝑣ℎ+ 𝑏 (7)

<!-- b000403 | prose | pages [15] -->
Analysis on Potential Success of Products 5.2

<!-- b000404 | prose | pages [15] -->
Before we show the analysis results, there are several training details to be stated:

<!-- b000405 | heading | pages [15] -->
1. Loss function

<!-- b000406 | prose | pages [15] -->
During the training, we use mean square error (MSE) as the loss function:

<!-- b000407 | prose | pages [15] -->
∑ 𝑁

<!-- b000408 | prose | pages [15] -->
𝑀𝑆𝐸(𝑦, ˆ𝑦) = 1

<!-- b000409 | prose | pages [15] -->
(𝑦𝑖−ˆ𝑦𝑖)2 (8)

<!-- b000410 | prose | pages [15] -->
𝑁

<!-- b000411 | prose | pages [15] -->
𝑖=1

<!-- b000412 | prose | pages [15] -->
where 𝑦is the true target vector and ˆ𝑦is the predicted feature vector and 𝑁is the number of dimension.

<!-- b000413 | heading | pages [15] -->
2. Normalization

<!-- b000414 | prose | pages [15] -->
Due to diﬀerent domains of each dimension in the input vector 𝑣𝑖𝑛𝑝𝑢𝑡, a normalization technique is needed. Before we feed the input vector into the LSTM module, we apply the following per-feature normalization operation:

<!-- b000415 | prose | pages [15] -->
关注数学模型

<!-- b000416 | furniture | pages [15] -->
2

<!-- b000417 | furniture | pages [15] -->
MATHmodels

<!-- b000418 | furniture | pages [15] -->
获取更多资讯

<!-- b000419 | furniture | pages [16] -->
Team 2003717

<!-- b000420 | furniture | pages [16] -->
Page 15

<!-- b000421 | prose | pages [16] -->
𝑥𝑖= 𝑥𝑖−𝜇𝑖

<!-- b000422 | prose | pages [16] -->
(9)

<!-- b000423 | prose | pages [16] -->
𝜎𝑖

<!-- b000424 | prose | pages [16] -->
where 𝜇𝑖and 𝜎𝑖are the mean and standard deviation of the 𝑖𝑡ℎfeature.

<!-- b000425 | heading | pages [16] -->
3. Training data

<!-- b000426 | prose | pages [16] -->
To make our model robust, we generate training data by sampling from the original review sequence with diﬀerent lengths and diﬀerent starting points. Our model is trained on these generated review sequences for 30 epochs (20 batches each epoch) with learning rate 𝛼= 0.8 and LBFGS optimizer.

<!-- b000427 | prose | pages [16] -->
After ﬁnishing the training period, we feed the original whole review sequence into the well-trained LSTM model to predict the next 𝑛review items (𝑛= 0.4× 𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙). With the predicted review information, we can compute the future reputation score for each product. Therefore, a product with a reputation score that keeps increasing or stable in the future can be identiﬁed as a potentially successful product. Otherwise, it can be a potentially failing product.

<!-- b000428 | caption | pages [16] -->
Figure 13: The future reputation score for each product with window size 𝑚= 500. The blue line represents

<!-- b000429 | prose | pages [16] -->
the historical reputation scores. The red line represents our predicted values.

<!-- b000430 | prose | pages [16] -->
As shown in Fig. 13, hair dryer, which keeps a stable ﬂow of reviews, will meet a rising trend in the future and then get back to the stable state again. Product microwave will keep its growth trend until it meets the upper bound. Therefore, these two product are potentially successful due to the increasing reputation scores in the future. As for product paciﬁer, it just keeps the stable state in the future.

<!-- b000431 | prose | pages [16] -->
Problem 2 (d): Causal Eﬀectiveness Between Reveiws 6

<!-- b000432 | prose | pages [16] -->
6.1 Ripple Eﬀects of Extreme Ratings

<!-- b000433 | prose | pages [16] -->
To ﬁgure out whether speciﬁc star ratings incite more reviews, we calculate the monthly review numbers for each rating, seen in Fig. 14.

<!-- b000434 | prose | pages [16] -->
关注数学模型

<!-- b000435 | furniture | pages [16] -->
2

<!-- b000436 | furniture | pages [16] -->
MATHmodels

<!-- b000437 | furniture | pages [16] -->
获取更多资讯

<!-- b000438 | furniture | pages [17] -->
Team 2003717

<!-- b000439 | furniture | pages [17] -->
Page 16

<!-- b000440 | caption | pages [17] -->
Figure 14: Monthly review number per rating

<!-- b000441 | prose | pages [17] -->
As can be seen in Fig. 14, at the beginning, reviews of all ratings are few. Even if the number of reviews with rate 5 ushers in a few small peaks, the numbers of reviews with other ratings seem not to be aﬀected. The real inﬂection point is when review number with rate 5 surges, the numbers of reviews corresponding to other ratings also increase. After that, the total number of comments rises almost exponentially. Besides, the peaks of other-rated reviews are almost always behind those of rate 5. In summary, we speculate that a certain amount of rate 5 may incite more reviews.

<!-- b000442 | prose | pages [17] -->
6.2 Causal Inference for Ratio of Low Rating and Review Length

<!-- b000443 | caption | pages [17] -->
Figure 15: Monthly ratio of reviews with rate 1 and monthly review length

<!-- b000444 | prose | pages [17] -->
During the process of data mining, we unexpectedly ﬁnd that the ratio trend of reviews with rate 1 is surprisingly similar to the trend of all reviews’ average length. To further dig out which is the cause and which is the lag variable, we apply the Granger Cause Test for causal inference.

<!-- b000445 | heading | pages [17] -->
Introduction and running steps of Granger Cause Test:

<!-- b000446 | prose | pages [17] -->
1. Granger Cause Test is a well-known method in Statistics to determine if a particular variable comes after another in the time series and what the lags are. It is a bottom up procedure which assumes the

<!-- b000447 | prose | pages [17] -->
关注数学模型

<!-- b000448 | furniture | pages [17] -->
2

<!-- b000449 | furniture | pages [17] -->
MATHmodels

<!-- b000450 | furniture | pages [17] -->
获取更多资讯

<!-- b000451 | furniture | pages [18] -->
Team 2003717

<!-- b000452 | furniture | pages [18] -->
Page 17

<!-- b000453 | prose | pages [18] -->
data-generating processes in any time series are independent variables; then the data sets are analyzed to see if they are correlated.

<!-- b000454 | heading | pages [18] -->
2. Running the Test[16]:

<!-- b000455 | prose | pages [18] -->
The null hypothesis for the test is that lagged x-values do not explain the variation in y. Therefore, we run the F-Test to examine this hypothesis.

<!-- b000456 | prose | pages [18] -->
(a) State the null hypothesis and alternate hypothesis. For example, y(t) does not Granger-cause x(t).

<!-- b000457 | prose | pages [18] -->
(b) Choose the lags. This mostly depends on how much data you have available. One way to choose

<!-- b000458 | prose | pages [18] -->
lags i and j is to run a model order test (i.e. use a model order selection method). It might be easier just to pick several values and run the Granger test several times to see if the results are the same for diﬀerent lag levels. The results should not be sensitive to lags.

<!-- b000459 | prose | pages [18] -->
(c) Find the f-value. Two equations can be used to ﬁnd if 𝛽𝑗= 0 for all lags j:

<!-- b000460 | prose | pages [18] -->
𝑦(𝑡) =

<!-- b000461 | prose | pages [18] -->
∑ 𝑇

<!-- b000462 | prose | pages [18] -->
𝑦(𝑡) =

<!-- b000463 | prose | pages [18] -->
∑ ∑ 𝑇 𝑇

<!-- b000464 | prose | pages [18] -->
𝛼𝑖𝑦(𝑡−𝑖) + 𝑐1 + 𝑣1(𝑡)

<!-- b000465 | prose | pages [18] -->
𝑖=1 𝑖=1

<!-- b000466 | prose | pages [18] -->
∑ 𝑇

<!-- b000467 | prose | pages [18] -->
𝛼𝑖𝑦(𝑡−𝑖) +

<!-- b000468 | prose | pages [18] -->
𝑖=1

<!-- b000469 | prose | pages [18] -->
𝛽𝑗𝑥(𝑡−𝑗) + 𝑐2 + 𝑣2(𝑡)

<!-- b000470 | prose | pages [18] -->
𝑗=1

<!-- b000471 | prose | pages [18] -->
Two equations for Granger causality: Restricted (top) and unrestricted (bottom). Similarly, these equations test to see if y(t) Granger-causes x(t):

<!-- b000472 | prose | pages [18] -->
𝑥(𝑡) =

<!-- b000473 | prose | pages [18] -->
∑ 𝑇

<!-- b000474 | prose | pages [18] -->
∑ ∑ 𝑇 𝑇

<!-- b000475 | prose | pages [18] -->
𝛼𝑖𝑥(𝑡−𝑖) + 𝑐1 + 𝑢1(𝑡)

<!-- b000476 | prose | pages [18] -->
𝑖=1 𝑖=1

<!-- b000477 | prose | pages [18] -->
∑ 𝑇

<!-- b000478 | prose | pages [18] -->
𝛼𝑖𝑥(𝑡−𝑖) +

<!-- b000479 | prose | pages [18] -->
𝑥(𝑡) =

<!-- b000480 | prose | pages [18] -->
𝑖=1

<!-- b000481 | prose | pages [18] -->
𝛽𝑗𝑦(𝑡−𝑗) + 𝑐2 + 𝑢2(𝑡)

<!-- b000482 | prose | pages [18] -->
𝑗=1

<!-- b000483 | prose | pages [18] -->
(d) Calculate the f-statistic using the following equation:

<!-- b000484 | prose | pages [18] -->
𝐹= ((𝑆𝑆′

<!-- b000485 | prose | pages [18] -->
𝐸−𝑆𝑆𝐸)/𝑚)

<!-- b000486 | prose | pages [18] -->
∼𝐹(𝑚, 𝑑𝑓𝐸)

<!-- b000487 | prose | pages [18] -->
𝑀𝑆𝐸

<!-- b000488 | prose | pages [18] -->
(e) If the p-value for this test is less than the designed value of 𝛼, then we reject the null hypothesis

<!-- b000489 | prose | pages [18] -->
and conclude that x causes y (at least in the Granger causality sense). Otherwise, change the lags and reperform F-test.

<!-- b000490 | caption | pages [18] -->
Table 5: Granger Causality: Number of lags (no zero) 2

<!-- b000491 | prose | pages [18] -->
F=5.6862, p=0.0041, df_denom=157, df_num=2 ssr based F test ch12=11.7346, p=0.0028, df=2 ssr based ch12 test ch12=11.3290, p=0.0035, df=2 likelihood ratio test

<!-- b000492 | prose | pages [18] -->
From the results in Table 5, we can claim with at least 95 percent conﬁdence level that the averaged review length comes after the the ratio of reviews with rate 1 and the lags are 2 data points, that is, combining with Fig. 15, short reviews often come after large ratio of extremely low ratings with lags within 2 month.

<!-- b000493 | prose | pages [18] -->
关注数学模型

<!-- b000494 | furniture | pages [18] -->
2

<!-- b000495 | furniture | pages [18] -->
MATHmodels

<!-- b000496 | furniture | pages [18] -->
获取更多资讯

<!-- b000497 | furniture | pages [19] -->
Team 2003717

<!-- b000498 | furniture | pages [19] -->
Page 18

<!-- b000499 | prose | pages [19] -->
Problem 2 (e)[5]: Correlation between Aﬀective Words and Star Ratings 7

<!-- b000500 | prose | pages [19] -->
Nowadays, a new career named water army unconsciously bloom. People who engage in this occupation act as Internet ghostwriters paid to post online comments with particular content. In order to help achieve or obstruct the online shopkeepers’ sales plan while not being monitored by anomaly detection machines, they may disturb the normal alignment of ratings and review texts. Moreover, since diﬀerent people have diﬀerent rating standards, their mappings from reviews to ratings are various. Therefore, chances are that: for some people, speciﬁc quality descriptors of their text-based reviews such as enthusiastic and disappointed are strongly associated with rating levels, for others the relations are relatively looser to diﬀerent extents. As a result, analyzing the alignment of rates and review texts is of great importance.

<!-- b000501 | prose | pages [19] -->
Analysis for Alignment of Rate and Review Scored by Certain Aﬀective Words 7.1

<!-- b000502 | prose | pages [19] -->
Recall that in section 3.2. we calculate the sentimental scores for each review text, which represent diﬀerent people’s attitude to products. In this section, we

<!-- b000503 | heading | pages [19] -->
1. update all sentimental scores by just considering the combinations of aﬀective words such as

<!-- b000504 | prose | pages [19] -->
wonderful and terriﬁc.

<!-- b000505 | prose | pages [19] -->
2. After that, we further divide the reviews into 5 ranks by 4 thresholds of sentimental scores. The i-th thresholds, denoted as 𝑡ℎ𝑟𝑒𝑖, are set to be 𝑎𝑣𝑔𝑖+𝑎𝑣𝑔𝑖+1

<!-- b000506 | prose | pages [19] -->
, where 𝑎𝑣𝑔𝑖is the weighted averaged reviews 2 sentimental score for rating i deﬁned in section 3.2.

<!-- b000507 | prose | pages [19] -->
So far, we’ve classify all ratings and reviews into 5 groups respectively. Next, we count the number of items where the rating is rank i and the review is rank j for 𝑖, 𝑗∈[5] , generate the confusion matrix and compute the recall, precision and macro F1 value for each product[17], as shown in Fig. 16.

<!-- b000508 | prose | pages [19] -->
Assume rate 1,2 and review rank 1,2 belong to negative attitudes, rate 4,5 and review rank 4,5 belong to positive attitudes. From the ﬁgures above, it’s easily seen that positive reviews are seldom mapped into negative ratings and so are negative reviews. Nevertheless, crossover mappings between rate 1 and review rank 2 or rate 3 and review rank 4 and etc. seem to take up a certain percentage that we cannot ignore.

<!-- b000509 | prose | pages [19] -->
Also, from the bottom right part of Fig. 16(d), the recall, precision and macro F1 value of rate and review alignment for all three products are between 0.6 and 0.8, which are not very satisfying. Among these results, the mapping asymmetricity for microwave is the most signiﬁcant.

<!-- b000510 | prose | pages [19] -->
Micro Observation of Asymmetricity between Rate and Review[6] 7.2

<!-- b000511 | prose | pages [19] -->
From subsection 7.1, we ﬁnd that there is some asymmetricity of rate-review mapping when it comes to the sentimental analysis. Next, we aim to detailedly dig out the reason of this asymmetricity, i.e. why reviews with strongly aﬀective words has mild ratings, and why reviews with more mildly aﬀective words has extreme ratings.

<!-- b000512 | heading | pages [19] -->
1. Both positive words and negative aﬀective words occur in the same reviews.

<!-- b000513 | prose | pages [19] -->
By scanning the review texts, we ﬁnd that some consumers detailedly illustrate their attitude towards products from high expectation or satisfaction to disappointment. As a result, we particularly analyze the reviews whose ranks deviate from their ratings, the results are shown as follows Table 6.

<!-- b000514 | heading | pages [19] -->
2. Strongly aﬀective words are replaced by words that describe properties.

<!-- b000515 | prose | pages [19] -->
关注数学模型

<!-- b000516 | furniture | pages [19] -->
2

<!-- b000517 | furniture | pages [19] -->
MATHmodels

<!-- b000518 | furniture | pages [19] -->
获取更多资讯

<!-- b000519 | furniture | pages [20] -->
Team 2003717

<!-- b000520 | furniture | pages [20] -->
Page 19

<!-- b000521 | prose | pages [20] -->
(a) Analysis for rate/text review alignment of hair dryer (b) Analysis for rate/text review alignment of microwave

<!-- b000522 | prose | pages [20] -->
(c) Analysis for rate/text review alignment of paciﬁer (d) Recall/Precision/F1 of rate/text alignment for diﬀerent products

<!-- b000523 | caption | pages [20] -->
Figure 16: Analysis for alignment of rate and review scored by certain aﬀective words

<!-- b000524 | caption | pages [20] -->
Table 6: Ratio for both occurrence of positive and negative aﬀective words:

<!-- b000525 | prose | pages [20] -->
reviews with and without rating deviation, respectively.

<!-- b000526 | prose | pages [20] -->
With rate/text deviation Without rate/text deviation Hair Dryer Microwave Paciﬁer 0.12 0.078 0.098 0.191 0.163 0.152

<!-- b000527 | prose | pages [20] -->
People may naturally equal mildly aﬀective words to neutral ratings, while through text data mining, we observe that there are a proportion of extreme ratings whose mildly aﬀective words outnumber strongly aﬀective words.

<!-- b000528 | prose | pages [20] -->
To dig out the reason of this phenomena, we select reviews with rate 1 and rate 5, calculate the averaged length and number of property words such as heat and magnetrons for extreme reviews, i.e. reviews with rate 1 and rate 5. After that, we compute the same statistics for extreme reviews with more neutral aﬀective words than strongly aﬀective words. The results are displayed in Fig. 17.

<!-- b000529 | prose | pages [20] -->
关注数学模型

<!-- b000530 | furniture | pages [20] -->
2

<!-- b000531 | furniture | pages [20] -->
MATHmodels

<!-- b000532 | furniture | pages [20] -->
获取更多资讯

<!-- b000533 | furniture | pages [21] -->
Team 2003717

<!-- b000534 | prose | pages [21] -->
(a) Avg length of reviews with rate 1

<!-- b000535 | furniture | pages [21] -->
Page 20

<!-- b000536 | prose | pages [21] -->
(b) Avg length of reviews with rate 5

<!-- b000537 | caption | pages [21] -->
Figure 17: Comparisons between normal extreme reviews and extreme reviews with more mildly aﬀective

<!-- b000538 | prose | pages [21] -->
words.

<!-- b000539 | prose | pages [21] -->
From the ﬁgures above, it is easily seen that extreme reviews with more neutral words tend to consist of more property words and have longer lengths. With further observation of detailed examples, we ﬁnd that this is largely because some reviewers are objective enough to give factual descriptions about products instead of piling up their strongly aﬀective attitude towards them. For these group of customers, the extents of their aﬀective words in reviews are not closely related to ratings.

<!-- b000540 | prose | pages [21] -->
8

<!-- b000541 | heading | pages [21] -->
Strengths and Weaknesses

<!-- b000542 | prose | pages [21] -->
8.1

<!-- b000543 | heading | pages [21] -->
Strengths

<!-- b000544 | prose | pages [21] -->
1. We thoroughly apply data cleaning by removing extremely short words in reviews and columns with similar meanings, tokenizing all texts and lemmatizing and stemming all words. Besides, we also apply LDA topic model to give a intuitive description of what reviews care about[18].

<!-- b000545 | prose | pages [21] -->
2. We vividly and diversely visualize our cross-dimensional analysis to explore the correlation between data in all directions. Some hidden features such as review readability and time gap of adjacent reviews are also taken into account[19].

<!-- b000546 | prose | pages [21] -->
3. We comprehensively apply multiple models to go deep into the patterns of reviews and ratings:

<!-- b000547 | prose | pages [21] -->
(a) We apply LDA topic model to 7 × 3 dictionaries for diﬀerent attributes of each product and apply

<!-- b000548 | prose | pages [21] -->
weighted average with time decay to generate users’ preference vectors.

<!-- b000549 | prose | pages [21] -->
(b) We apply sentiment analysis and logistic regression to estimate sentimental score of each review.

<!-- b000550 | prose | pages [21] -->
Furthermore, we divide reviews into 5 rank , visualize the confusion matrix between rate and review rank and discover the mapping asymmetricity of rate and reviews with regard to people’s attitude.

<!-- b000551 | prose | pages [21] -->
(c) We use LSTM to compute the time-varying coeﬃcients of joint contribution for the reputation

<!-- b000552 | prose | pages [21] -->
index, which is powerful in globally dealing with moderate scale time series.

<!-- b000553 | prose | pages [21] -->
(d) Granger Cause Test is carried out to perform the casual inference for monthly ratios of low ratings

<!-- b000554 | prose | pages [21] -->
and review lengths.

<!-- b000555 | prose | pages [21] -->
关注数学模型

<!-- b000556 | furniture | pages [21] -->
2

<!-- b000557 | furniture | pages [21] -->
MATHmodels

<!-- b000558 | furniture | pages [21] -->
获取更多资讯

<!-- b000559 | furniture | pages [22] -->
Team 2003717

<!-- b000560 | prose | pages [22] -->
8.2

<!-- b000561 | heading | pages [22] -->
Weaknesses

<!-- b000562 | furniture | pages [22] -->
Page 21

<!-- b000563 | prose | pages [22] -->
1. We simply assume the sales volumn to be proportional to number of reviews, which may be too simplistic to be realistic.

<!-- b000564 | prose | pages [22] -->
2. Owing to lacking the price data and other necessary information, we fail to ﬁgure out the thorough reason for which all the three products spend a long time to go through the cold start period.

<!-- b000565 | prose | pages [22] -->
3. Due to the time limit, the terms in our dictionaries for diﬀerent attributes of each products may be not enough to give an accurate proﬁle of consumers’ reviews.

<!-- b000566 | prose | pages [22] -->
9

<!-- b000567 | heading | pages [22] -->
Conclusion

<!-- b000568 | prose | pages [22] -->
Nowadays, online ratings and reviews for products play a more and more important role of inﬂuencing users’ purchasing decisions. An in-depth analysis of this information is of great signiﬁcance to companies’ marketing strategies.

<!-- b000569 | prose | pages [22] -->
In this project, we make a detailed data cleaning of the given dataset. After that, we vividly and diversely visualize our cross-dimensional analysis to explore the correlation between data in all directions. We design three sub-index and a comprehensive index to indicator the products’ reputation and prospects. Logistic regression, LSTM, LDA topic model, Granger Cause Test, sentiment analysis and confusion matrix method are applied to assist us in digging out the important and unexpected insights for each product, which allow us to make informed suggestions for the Sunshine Company.

<!-- b000570 | prose | pages [22] -->
关注数学模型

<!-- b000571 | furniture | pages [22] -->
2

<!-- b000572 | furniture | pages [22] -->
MATHmodels

<!-- b000573 | furniture | pages [22] -->
获取更多资讯

<!-- b000574 | furniture | pages [23] -->
Team 2003717

<!-- b000575 | furniture | pages [23] -->
Page 22

<!-- b000576 | prose | pages [23] -->
The Letter to the Marketing Director of Sunshine Company 10

<!-- b000577 | prose | pages [23] -->
Dear director,

<!-- b000578 | prose | pages [23] -->
Considering today’s increasingly ﬁerce competition in e-commerce, accurately grasping customer needs and specifying appropriate marketing strategies are of vital importance to improve corporate proﬁts and product visibility. As response to your company’s requirement, we are here pretty glad to have the opportunity to introduce our research and suggestions to you, with the hope that it may give you some insights of the future strategies.

<!-- b000579 | heading | pages [23] -->
1. Pay attention to and properly guide the early reviews.

<!-- b000580 | prose | pages [23] -->
Throughout the whole records of consumers’ ratings and reviews for hair dryer, microwave and paciﬁers, we ﬁnd the the averaged number of helpful votes for a single review in the ﬁrst 5 stage is above 3.2 times than that in recent period. Moreover, the descriptions in some reviews with rate 2 look even worser than that with rate 1, and so are descriptions in reviews with rate 4,5. Since helpful votes and the ﬁtness of review description associate tightly with people’s belief and the reputation propagation of products, we suggest Sunshine to properly guide and closely track the trend of early reviews, e.g. make guidelines of which rate corresponds to which extent of attitude, so as to smoothly go through the cold start stage.

<!-- b000581 | heading | pages [23] -->
2. Keep a good image of brand for all three products.

<!-- b000582 | prose | pages [23] -->
Based on our statistics, the number of reviews has increased rapidly in recent years, which reﬂects the great prospects of the online sales market. Whereas at the same time, it should be noted that the star rating and averaged review length will experience large ﬂuctuations in the early stage of the product launch. This phenomena may give customers a bad or fuzzy brand impression. Moreover as the data shows, the early review volume, an indirected reﬂection of brand popularity, has been hovering at a lower level. As a result, if Sunshine can perform well, e.g. keep a good image of brand, in the early stage, great chances are that it will take a lead in such a highly competitive market, which may exert continuously positive eﬀects on your subsequent development.

<!-- b000583 | heading | pages [23] -->
3. Apply our reputation index to monitor product dynamics.

<!-- b000584 | prose | pages [23] -->
Since the review and rating data is rich and complex, reﬁning a comprehensive indicator that summa- rizes product reputation and sales is necessary for Sunshine to quickly adjust its promotion strategy. In our project, we design a reputation index which takes into account the star rating, time gap of adjacent reviews, review helpfulness rate and readability , information of vine and veriﬁcation. The time-varying coeﬃcients of joint contribution are calculated by LSTM, whose losses on testing dataset are small enough to be emphasized. Note that the time gap of neighboring reviews is a reﬂection of product popularity and we assume it to be proportional to the sales volumn, hence our reputation metric can be a great indicator of not only people’s attitude towards products but Sunshine’s proﬁts.

<!-- b000585 | heading | pages [23] -->
4. Attach diﬀerent importance to products’ properties according to people’s preferences.

<!-- b000586 | prose | pages [23] -->
Trough the text mining of LDA topic model, we extract 7 topics for each product, which represent the product properties that customers care about most. By an integrative consideration of reviews’ keywords, ratings, helpful votes and the time decay of ratings, we estimate customers’ preference vectors in 8 topics for each products, i.e.

<!-- b000587 | prose | pages [23] -->
关注数学模型

<!-- b000588 | furniture | pages [23] -->
2

<!-- b000589 | furniture | pages [23] -->
MATHmodels

<!-- b000590 | furniture | pages [23] -->
获取更多资讯

<!-- b000591 | furniture | pages [24] -->
Team 2003717

<!-- b000592 | furniture | pages [24] -->
Page 23

<!-- b000593 | prose | pages [24] -->
As can be seen from the ﬁgures above, except for the tight control of products’ materials quality, we suggest that your company ensure the security, heat and after sales service of hair dryer and microwave, as well as the size, shape and packing of paciﬁer.

<!-- b000594 | prose | pages [24] -->
We are really appreciated for this opportunity to assist you in building up an online marketing strategy, and we are convinced that our proposal can be utilized in improvement of your competence for the three products. Please feel free to contact us for further information on the project.

<!-- b000595 | prose | pages [24] -->
Sincerely yours

<!-- b000596 | prose | pages [24] -->
MCM 2020 Team

<!-- b000597 | prose | pages [24] -->
关注数学模型

<!-- b000598 | furniture | pages [24] -->
2

<!-- b000599 | furniture | pages [24] -->
MATHmodels

<!-- b000600 | furniture | pages [24] -->
获取更多资讯

<!-- b000601 | furniture | pages [25] -->
Team 2003717

<!-- b000602 | heading | pages [25] -->
References

<!-- b000603 | references | pages [25] -->
[1] Topic

<!-- b000604 | references | pages [25] -->
modeling

<!-- b000605 | references | pages [25] -->
using

<!-- b000606 | references | pages [25] -->
latent

<!-- b000607 | references | pages [25] -->
pling

<!-- b000608 | references | pages [25] -->
explained!

<!-- b000609 | references | pages [25] -->
[Online].

<!-- b000610 | furniture | pages [25] -->
Page 24

<!-- b000611 | references | pages [25] -->
dirichlet

<!-- b000612 | references | pages [25] -->
allocation(lda)

<!-- b000613 | references | pages [25] -->
and

<!-- b000614 | references | pages [25] -->
gibbs

<!-- b000615 | references | pages [25] -->
sam-

<!-- b000616 | references | pages [25] -->
Available:

<!-- b000617 | references | pages [25] -->
https://medium.com/analytics-vidhya/

<!-- b000618 | references | pages [25] -->
topic-modeling-using-lda-and-gibbs-sampling-explained-49d49b3d1045

<!-- b000619 | references | pages [25] -->
[2] A. Bhatt, A. Patel, H. Chheda, and K. Gawande, “Amazon review classiﬁcation and sentiment analysis,”

<!-- b000620 | references | pages [25] -->
International Journal of Computer Science and Information Technologies, vol. 6, no. 6, pp. 5107–5110,

<!-- b000621 | references | pages [25] -->
2015.

<!-- b000622 | references | pages [25] -->
[3] T. U. Haque, N. N. Saber, and F. M. Shah, “Sentiment analysis on large scale amazon product reviews,”

<!-- b000623 | references | pages [25] -->
in 2018 IEEE International Conference on Innovative Research and Development (ICIRD).

<!-- b000624 | references | pages [25] -->
2018, pp. 1–6.

<!-- b000625 | references | pages [25] -->
IEEE,

<!-- b000626 | references | pages [25] -->
[4] D. G. Kleinbaum, K. Dietz, M. Gail, M. Klein, and M. Klein, Logistic regression.

<!-- b000627 | references | pages [25] -->
Springer, 2002.

<!-- b000628 | references | pages [25] -->
[5] S. Dhanasobhon, P.-Y. Chen, M. Smith, and P.-y. Chen, “An analysis of the diﬀerential impact of reviews

<!-- b000629 | references | pages [25] -->
and reviewers at amazon. com,” ICIS 2007 Proceedings, p. 94, 2007.

<!-- b000630 | references | pages [25] -->
[6] P.-Y. Chen, S. Dhanasobhon, and M. D. Smith, “All reviews are not created equal: The disaggregate

<!-- b000631 | references | pages [25] -->
impact of reviews and reviewers at amazon. com,” Com (May 2008), 2008.

<!-- b000632 | references | pages [25] -->
[7] Topic modeling and latent dirichlet allocation (lda) in python. [Online]. Available:

<!-- b000633 | references | pages [25] -->
https:

<!-- b000634 | references | pages [25] -->
//towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24

<!-- b000635 | references | pages [25] -->
[8] J. Leino and K.-J. Räihä, “Case amazon: ratings and reviews as part of recommendations,” in Proceed-

<!-- b000636 | references | pages [25] -->
ings of the 2007 ACM conference on Recommender systems, 2007, pp. 137–140.

<!-- b000637 | references | pages [25] -->
[9] M. Li, L. Huang, C.-H. Tan, and K.-K. Wei, “Helpfulness of online product reviews as seen by

<!-- b000638 | references | pages [25] -->
consumers: Source and content features,” International Journal of Electronic Commerce, vol. 17,

<!-- b000639 | references | pages [25] -->
no. 4, pp. 101–136, 2013.

<!-- b000640 | references | pages [25] -->
[10] J. Liu, Y. Cao, C.-Y. Lin, Y. Huang, and M. Zhou, “Low-quality product review detection in opin-

<!-- b000641 | references | pages [25] -->
ion summarization,” in Proceedings of the 2007 Joint Conference on Empirical Methods in Natural

<!-- b000642 | references | pages [25] -->
Language Processing and Computational Natural Language Learning (EMNLP-CoNLL), 2007, pp.

<!-- b000643 | references | pages [25] -->
334–342.

<!-- b000644 | references | pages [25] -->
[11] T. Wong, “Exploratory data analysis of amazon. com book reviews,” 2009.

<!-- b000645 | references | pages [25] -->
[12] S.-M. Kim, P. Pantel, T. Chklovski, and M. Pennacchiotti, “Automatically assessing review helpfulness,”

<!-- b000646 | references | pages [25] -->
in Proceedings of the 2006 Conference on empirical methods in natural language processing, 2006, pp.

<!-- b000647 | references | pages [25] -->
423–430.

<!-- b000648 | references | pages [25] -->
[13] N. Korﬁatis, E. GarcíA-Bariocanal, and S. SáNchez-Alonso, “Evaluating content quality and helpfulness

<!-- b000649 | references | pages [25] -->
of online product reviews: The interplay of review helpfulness vs. review content,” Electronic Commerce

<!-- b000650 | references | pages [25] -->
Research and Applications, vol. 11, no. 3, pp. 205–217, 2012.

<!-- b000651 | references | pages [25] -->
[14] F. A. Gers, J. Schmidhuber, and F. Cummins, “Learning to forget: Continual prediction with lstm,”

<!-- b000652 | references | pages [25] -->
1999.

<!-- b000653 | references | pages [25] -->
[15] K. Greﬀ, R. K. Srivastava, J. Koutník, B. R. Steunebrink, and J. Schmidhuber, “Lstm: A search space

<!-- b000654 | references | pages [25] -->
odyssey,” IEEE transactions on neural networks and learning systems, vol. 28, no. 10, pp. 2222–2232,

<!-- b000655 | references | pages [25] -->
2016.

<!-- b000656 | references | pages [25] -->
Deﬁnition, running the test. [Online]. Available:

<!-- b000657 | references | pages [25] -->
[16] Granger causality:

<!-- b000658 | references | pages [25] -->
datasciencecentral.com/granger-causality/

<!-- b000659 | references | pages [25] -->
https://www.statisticshowto.

<!-- b000660 | references | pages [25] -->
关注数学模型

<!-- b000661 | furniture | pages [25] -->
2

<!-- b000662 | furniture | pages [25] -->
MATHmodels

<!-- b000663 | furniture | pages [25] -->
获取更多资讯

<!-- b000664 | furniture | pages [26] -->
Team 2003717

<!-- b000665 | furniture | pages [26] -->
Page 25

<!-- b000666 | references | pages [26] -->
[17] J. T. Townsend, “Theoretical analysis of an alphabetic confusion matrix,” Perception & Psychophysics,

<!-- b000667 | references | pages [26] -->
vol. 9, no. 1, pp. 40–50, 1971.

<!-- b000668 | references | pages [26] -->
[18] S. Huang, J.-T. Sun, J. Wu, M. Wang, and Z. Chen, “Product review search,” Sep. 4 2008, uS Patent

<!-- b000669 | references | pages [26] -->
App. 12/024,930.

<!-- b000670 | references | pages [26] -->
[19] J. C. De Albornoz, L. Plaza, P. Gervás, and A. Díaz, “A joint model of feature mining and sentiment

<!-- b000671 | references | pages [26] -->
analysis for product review rating,” in European conference on information retrieval.

<!-- b000672 | references | pages [26] -->
Springer, 2011,

<!-- b000673 | references | pages [26] -->
pp. 55–66.

<!-- b000674 | references | pages [26] -->
关注数学模型

<!-- b000675 | furniture | pages [26] -->
2

<!-- b000676 | furniture | pages [26] -->
MATHmodels

<!-- b000677 | furniture | pages [26] -->
获取更多资讯

<!-- b000678 | furniture | pages [27] -->
Team 2003717

<!-- b000679 | furniture | pages [27] -->
Page 26

<!-- b000680 | heading | pages [27] -->
Appendices

<!-- b000681 | heading | pages [27] -->
Appendix A

<!-- b000682 | heading | pages [27] -->
LDA Topic Model for Microwave and Paciﬁer

<!-- b000683 | caption | pages [27] -->
Figure 18: LDA topic model for microwave

<!-- b000684 | caption | pages [27] -->
Figure 19: LDA topic model for paciﬁer

<!-- b000685 | prose | pages [27] -->
关注数学模型

<!-- b000686 | furniture | pages [27] -->
2

<!-- b000687 | furniture | pages [27] -->
MATHmodels

<!-- b000688 | furniture | pages [27] -->
获取更多资讯

<!-- b000689 | furniture | pages [28] -->
Team 2003717

<!-- b000690 | furniture | pages [28] -->
Page 27

<!-- b000691 | prose | pages [28] -->
Product Contrast of Microwave and Paciﬁer Over Time

<!-- b000692 | heading | pages [28] -->
Appendix B

<!-- b000693 | caption | pages [28] -->
Figure 20: Product contrast of microwave over time

<!-- b000694 | caption | pages [28] -->
Figure 21: Product contrast of paciﬁer over time

<!-- b000695 | heading | pages [28] -->
Appendix C

<!-- b000696 | prose | pages [28] -->
Code

<!-- b000697 | prose | pages [28] -->
C.1 Data Preprocess and Overall Analysis

<!-- b000698 | prose | pages [28] -->
1 #######################################################

<!-- b000699 | prose | pages [28] -->
2 ### 0. Clean Data

<!-- b000700 | prose | pages [28] -->
3 #######################################################

<!-- b000701 | prose | pages [28] -->
4

<!-- b000702 | prose | pages [28] -->
5

<!-- b000703 | prose | pages [28] -->
6 import numpy as np

<!-- b000704 | prose | pages [28] -->
7 import pandas as pd

<!-- b000705 | prose | pages [28] -->
关注数学模型

<!-- b000706 | furniture | pages [28] -->
2

<!-- b000707 | furniture | pages [28] -->
MATHmodels

<!-- b000708 | furniture | pages [28] -->
获取更多资讯

<!-- b000709 | furniture | pages [29] -->
Team 2003717

<!-- b000710 | prose | pages [29] -->
8

<!-- b000711 | furniture | pages [29] -->
Page 28

<!-- b000712 | prose | pages [29] -->
9 hair_dryer = pd.read_csv(’data/hair_dryer.tsv’, sep = ’\t’)

<!-- b000713 | prose | pages [29] -->
10 microwave = pd.read_csv(’data/microwave.tsv’, sep = ’\t’)

<!-- b000714 | prose | pages [29] -->
11 pacifier = pd.read_csv(’data/pacifier.tsv’, sep = ’\t’)

<!-- b000715 | prose | pages [29] -->
12

<!-- b000716 | prose | pages [29] -->
13

<!-- b000717 | prose | pages [29] -->
14 def washer(dataset):

<!-- b000718 | prose | pages [29] -->
new_dataset = dataset.drop([’marketplace’, ’product_category’], axis=1) 15

<!-- b000719 | prose | pages [29] -->
new_dataset.loc[new_dataset[’vine’] == ’n’, ’vine’] = ’N’ 16

<!-- b000720 | prose | pages [29] -->
new_dataset.loc[new_dataset[’vine’] == ’y’, ’vine’] = ’Y’ 17

<!-- b000721 | prose | pages [29] -->
new_dataset.loc[new_dataset[’verified_purchase’] == ’n’, ’verified_purchase’] = ’N’ 18

<!-- b000722 | prose | pages [29] -->
new_dataset.loc[new_dataset[’verified_purchase’] == ’y’, ’verified_purchase’] = ’Y’ 19

<!-- b000723 | prose | pages [29] -->
20

<!-- b000724 | prose | pages [29] -->
transfer = [(’’, ’\’’), (’’, ’\’’), (’’, ’"’), (’’, ’"’), (’’, ’,’), (’’, ’.’), (’’ 21 , ’!’), (’’, ’...’), (’’, ’-’), (’’, ’-’)]

<!-- b000725 | prose | pages [29] -->
accept = ’[^a-zA-Z0-9_ !?,.\’"‘+-=;()\[\]<>*#~&$^@%/|\\\\]’ 22

<!-- b000726 | prose | pages [29] -->
for pair in transfer: 23

<!-- b000727 | prose | pages [29] -->
new_dataset[’product_title’] = new_dataset[’product_title’].str.replace(pair 24 [0], pair[1])

<!-- b000728 | prose | pages [29] -->
new_dataset[’review_headline’] = new_dataset[’review_headline’].str.replace( 25 pair[0], pair[1])

<!-- b000729 | prose | pages [29] -->
new_dataset[’review_body’] = new_dataset[’review_body’].str.replace(pair[0], 26 pair[1])

<!-- b000730 | prose | pages [29] -->
trash = new_dataset[new_dataset[’product_title’].str.contains(accept , na=True) 27

<!-- b000731 | prose | pages [29] -->
+ new_dataset[’review_headline’].str.contains(accept , na= 28 True)

<!-- b000732 | prose | pages [29] -->
+ new_dataset[’review_body’].str.contains(accept , na=True)] 29

<!-- b000733 | prose | pages [29] -->
new_dataset = new_dataset[- (new_dataset[’product_title’].str.contains(accept , na= 30 True)

<!-- b000734 | prose | pages [29] -->
+ new_dataset[’review_headline’].str.contains(accept , na= 31 True)

<!-- b000735 | prose | pages [29] -->
+ new_dataset[’review_body’].str.contains(accept , na=True)) 32 ]

<!-- b000736 | prose | pages [29] -->
return new_dataset , trash 33

<!-- b000737 | prose | pages [29] -->
34

<!-- b000738 | prose | pages [29] -->
35

<!-- b000739 | prose | pages [29] -->
36 new_hair_dryer , trash1 = washer(hair_dryer)

<!-- b000740 | prose | pages [29] -->
37 new_microwave , trash2 = washer(microwave)

<!-- b000741 | prose | pages [29] -->
38 new_pacifier , trash3 = washer(pacifier)

<!-- b000742 | prose | pages [29] -->
39 trash = pd.concat([trash1, trash2, trash3])

<!-- b000743 | prose | pages [29] -->
40

<!-- b000744 | prose | pages [29] -->
41

<!-- b000745 | prose | pages [29] -->
42 new_hair_dryer.to_csv(’data/new_hair_dryer.csv’, encoding = ’utf-8_sig’)

<!-- b000746 | prose | pages [29] -->
43 new_microwave.to_csv(’data/new_microwave.csv’, encoding = ’utf-8_sig’)

<!-- b000747 | prose | pages [29] -->
44 new_pacifier.to_csv(’data/new_pacifier.csv’, encoding = ’utf-8_sig’)

<!-- b000748 | prose | pages [29] -->
45 trash.to_csv(’data/trash.csv’, encoding = ’utf-8_sig’)

<!-- b000749 | prose | pages [29] -->
46

<!-- b000750 | prose | pages [29] -->
47

<!-- b000751 | prose | pages [29] -->
48 del hair_dryer , microwave , pacifier , trash1 , trash2 , trash3

<!-- b000752 | prose | pages [29] -->
49

<!-- b000753 | prose | pages [29] -->
50

<!-- b000754 | prose | pages [29] -->
51 #######################################################

<!-- b000755 | prose | pages [29] -->
52 ### 1. Prepare: Import , Time Process , Review Process

<!-- b000756 | prose | pages [29] -->
53 #######################################################

<!-- b000757 | prose | pages [29] -->
54

<!-- b000758 | prose | pages [29] -->
55

<!-- b000759 | prose | pages [29] -->
56 import matplotlib.pyplot as plt

<!-- b000760 | prose | pages [29] -->
57

<!-- b000761 | prose | pages [29] -->
58 def data_process(dataset):

<!-- b000762 | prose | pages [29] -->
dataset[’review_date’] = pd.to_datetime(dataset[’review_date’]) 59

<!-- b000763 | prose | pages [29] -->
dataset[’year’] = dataset[’review_date’].dt.year 60

<!-- b000764 | prose | pages [29] -->
dataset[’month’] = dataset[’review_date’].dt.month 61

<!-- b000765 | prose | pages [29] -->
dataset[’day’] = dataset[’review_date’].dt.day 62

<!-- b000766 | prose | pages [29] -->
关注数学模型

<!-- b000767 | furniture | pages [29] -->
2

<!-- b000768 | furniture | pages [29] -->
MATHmodels

<!-- b000769 | furniture | pages [29] -->
获取更多资讯

<!-- b000770 | furniture | pages [30] -->
Team 2003717

<!-- b000771 | furniture | pages [30] -->
Page 29

<!-- b000772 | prose | pages [30] -->
dataset[’helpful_rate’] = dataset[’helpful_votes’] / dataset[’total_votes’] 63

<!-- b000773 | prose | pages [30] -->
dataset[’review_length’] = dataset[’review_headline’].str.len() + dataset[’ 64 review_body’].str.len()

<!-- b000774 | prose | pages [30] -->
65

<!-- b000775 | prose | pages [30] -->
66 data_process(new_hair_dryer)

<!-- b000776 | prose | pages [30] -->
67 data_process(new_microwave)

<!-- b000777 | prose | pages [30] -->
68 data_process(new_pacifier)

<!-- b000778 | prose | pages [30] -->
69 all = pd.concat([new_hair_dryer , new_microwave , new_pacifier])

<!-- b000779 | prose | pages [30] -->
70

<!-- b000780 | prose | pages [30] -->
71

<!-- b000781 | prose | pages [30] -->
72 #######################################################

<!-- b000782 | prose | pages [30] -->
73 ### 2.1. Plot 1

<!-- b000783 | prose | pages [30] -->
74 #######################################################

<!-- b000784 | prose | pages [30] -->
75

<!-- b000785 | prose | pages [30] -->
76

<!-- b000786 | prose | pages [30] -->
77 import calendar

<!-- b000787 | prose | pages [30] -->
78

<!-- b000788 | prose | pages [30] -->
79 legend = [’all’, ’hair_dryer’, ’microwave’, ’pacifier’]

<!-- b000789 | prose | pages [30] -->
80

<!-- b000790 | prose | pages [30] -->
81 review_num_to_date = pd.concat([all.groupby((’year’, ’month’))[’star_rating’].count(),

<!-- b000791 | prose | pages [30] -->
new_hair_dryer.groupby((’year’, ’month’))[’star_rating’ 82 ].count(),

<!-- b000792 | prose | pages [30] -->
new_microwave.groupby((’year’, ’month’))[’star_rating’ 83 ].count(),

<!-- b000793 | prose | pages [30] -->
new_pacifier.groupby((’year’, ’month’))[’star_rating’]. 84 count()], axis=1)

<!-- b000794 | prose | pages [30] -->
85 review_num_to_date.columns = legend

<!-- b000795 | prose | pages [30] -->
86 review_num_to_date = review_num_to_date.reset_index()

<!-- b000796 | prose | pages [30] -->
87 review_num_to_date[’date’] = review_num_to_date[’year’] + review_num_to_date[’month’] / 12

<!-- b000797 | prose | pages [30] -->
88 review_num_to_date = review_num_to_date.drop([’year’, ’month’], axis=1).set_index(’date ’)

<!-- b000798 | prose | pages [30] -->
89 review_num_to_date.plot(legend=True, alpha=0.5)

<!-- b000799 | prose | pages [30] -->
90 # plt.title(’Review Amount per Month’)

<!-- b000800 | prose | pages [30] -->
91 plt.xlabel(’Date’)

<!-- b000801 | prose | pages [30] -->
92 plt.ylabel(’Amount’)

<!-- b000802 | prose | pages [30] -->
93 plt.savefig("figure/Review Amount per Month.png",dpi=500,bbox_inches = ’tight’)

<!-- b000803 | prose | pages [30] -->
94 plt.show()

<!-- b000804 | prose | pages [30] -->
95

<!-- b000805 | prose | pages [30] -->
96

<!-- b000806 | prose | pages [30] -->
97 def func(dataset):

<!-- b000807 | prose | pages [30] -->
series = dataset.groupby((’year’, ’month’))[’star_rating’].agg([’count’, ’mean’]) 98

<!-- b000808 | prose | pages [30] -->
series[series[’count’]<3] = None 99

<!-- b000809 | prose | pages [30] -->
series = series.reset_index() 100

<!-- b000810 | prose | pages [30] -->
series[’date’] = series[’year’] + series[’month’] / 12 101

<!-- b000811 | prose | pages [30] -->
series = series.drop([’year’, ’month’, ’count’], axis=1).set_index(’date’) 102

<!-- b000812 | prose | pages [30] -->
return series 103

<!-- b000813 | prose | pages [30] -->
104 ser_all , ser_hair , ser_micro , ser_paci = func(all), func(new_hair_dryer), func( new_microwave), func(new_pacifier)

<!-- b000814 | prose | pages [30] -->
105 review_num_to_date = pd.concat([ser_hair , ser_micro , ser_paci], axis=1)

<!-- b000815 | prose | pages [30] -->
106 review_num_to_date.columns = legend[1:]

<!-- b000816 | prose | pages [30] -->
107 review_num_to_date.plot(legend=True, alpha=0.5)

<!-- b000817 | prose | pages [30] -->
108 # plt.title(’Rating Score per Month’)

<!-- b000818 | prose | pages [30] -->
109 plt.xlabel(’Date’)

<!-- b000819 | prose | pages [30] -->
110 plt.ylabel(’Score’)

<!-- b000820 | prose | pages [30] -->
111 # plt.xticks(np.arange(0, 168, 30))

<!-- b000821 | prose | pages [30] -->
112 plt.savefig("figure/Rating Score per Month.png",dpi=500,bbox_inches = ’tight’)

<!-- b000822 | prose | pages [30] -->
113 plt.show()

<!-- b000823 | prose | pages [30] -->
114

<!-- b000824 | prose | pages [30] -->
115

<!-- b000825 | prose | pages [30] -->
116 del legend , review_num_to_date , ser_all , ser_hair , ser_micro , ser_paci

<!-- b000826 | prose | pages [30] -->
117

<!-- b000827 | prose | pages [30] -->
118

<!-- b000828 | prose | pages [30] -->
关注数学模型

<!-- b000829 | furniture | pages [30] -->
2

<!-- b000830 | furniture | pages [30] -->
MATHmodels

<!-- b000831 | furniture | pages [30] -->
获取更多资讯

<!-- b000832 | furniture | pages [31] -->
Team 2003717

<!-- b000833 | furniture | pages [31] -->
Page 30

<!-- b000834 | prose | pages [31] -->
119 #######################################################

<!-- b000835 | prose | pages [31] -->
120 ### 2.2. Plot 2

<!-- b000836 | prose | pages [31] -->
121 #######################################################

<!-- b000837 | prose | pages [31] -->
122

<!-- b000838 | prose | pages [31] -->
123

<!-- b000839 | prose | pages [31] -->
124 review_percent_to_rating = pd.concat([all.groupby(’star_rating’)[’star_rating’].count() / all.shape[0],

<!-- b000840 | prose | pages [31] -->
new_hair_dryer.groupby(’star_rating’)[’star_rating’]. 125 count() / new_hair_dryer.shape[0],

<!-- b000841 | prose | pages [31] -->
new_microwave.groupby(’star_rating’)[’star_rating’]. 126 count() / new_microwave.shape[0],

<!-- b000842 | prose | pages [31] -->
new_pacifier.groupby(’star_rating’)[’star_rating’]. 127 count() / new_pacifier.shape[0]], axis=1)

<!-- b000843 | prose | pages [31] -->
128 review_percent_to_rating.columns = [’all’, ’hair_dryer’, ’microwave’, ’pacifier’]

<!-- b000844 | prose | pages [31] -->
129 review_percent_to_rating.plot.barh(legend=True, alpha = 0.5)

<!-- b000845 | prose | pages [31] -->
130 # plt.title(’Review Percent per Rating’)

<!-- b000846 | prose | pages [31] -->
131 plt.xlabel(’Percent’)

<!-- b000847 | prose | pages [31] -->
132 plt.ylabel(’Rating’)

<!-- b000848 | prose | pages [31] -->
133 plt.savefig("figure/Review Percent per Rating.png",dpi=500,bbox_inches = ’tight’)

<!-- b000849 | prose | pages [31] -->
134 plt.show()

<!-- b000850 | prose | pages [31] -->
135

<!-- b000851 | prose | pages [31] -->
136

<!-- b000852 | prose | pages [31] -->
137 del review_percent_to_rating

<!-- b000853 | prose | pages [31] -->
138

<!-- b000854 | prose | pages [31] -->
139

<!-- b000855 | prose | pages [31] -->
140 #######################################################

<!-- b000856 | prose | pages [31] -->
141 ### 2.3. Plot 3

<!-- b000857 | prose | pages [31] -->
142 #######################################################

<!-- b000858 | prose | pages [31] -->
143

<!-- b000859 | prose | pages [31] -->
144

<!-- b000860 | prose | pages [31] -->
145 for can in [all, new_hair_dryer , new_pacifier , new_microwave]:

<!-- b000861 | prose | pages [31] -->
can[can[’total_votes’] > 10][’helpful_rate’].plot.hist(bins=25) 146

<!-- b000862 | prose | pages [31] -->
147 # plt.title(’Review Amount of Helpful Percent’)

<!-- b000863 | prose | pages [31] -->
148 plt.xlabel(’Helpful Percent’)

<!-- b000864 | prose | pages [31] -->
149 plt.ylabel(’Amount’)

<!-- b000865 | prose | pages [31] -->
150 plt.legend([’all’, ’hair_dryer’, ’pacifier’, ’microwave’])

<!-- b000866 | prose | pages [31] -->
151 plt.savefig("figure/Review Amount of Helpful Percent.png",dpi=500,bbox_inches = ’tight’ )

<!-- b000867 | prose | pages [31] -->
152 plt.show()

<!-- b000868 | prose | pages [31] -->
153

<!-- b000869 | prose | pages [31] -->
154

<!-- b000870 | prose | pages [31] -->
155 del can

<!-- b000871 | prose | pages [31] -->
156

<!-- b000872 | prose | pages [31] -->
157

<!-- b000873 | prose | pages [31] -->
158 #######################################################

<!-- b000874 | prose | pages [31] -->
159 ### 2.4. Plot 4

<!-- b000875 | prose | pages [31] -->
160 #######################################################

<!-- b000876 | prose | pages [31] -->
161

<!-- b000877 | prose | pages [31] -->
162

<!-- b000878 | prose | pages [31] -->
163 all.groupby(’customer_id’)[’customer_id’].agg({’num’: ’count’}).reset_index().groupby(’ num’).count().plot(kind=’bar’, logy=True, legend=False, alpha=0.7)

<!-- b000879 | prose | pages [31] -->
164 # plt.title(’Customer Amount for Review Number’)

<!-- b000880 | prose | pages [31] -->
165 plt.xlabel(’Review Number’)

<!-- b000881 | prose | pages [31] -->
166 plt.ylabel(’Customer Amount’)

<!-- b000882 | prose | pages [31] -->
167 plt.savefig("figure/Customer Amount for Review Number.png",dpi=500,bbox_inches = ’tight ’)

<!-- b000883 | prose | pages [31] -->
168 plt.show()

<!-- b000884 | prose | pages [31] -->
169

<!-- b000885 | prose | pages [31] -->
170

<!-- b000886 | prose | pages [31] -->
171 #######################################################

<!-- b000887 | prose | pages [31] -->
172 ### 2.5. Plot 5

<!-- b000888 | prose | pages [31] -->
173 #######################################################

<!-- b000889 | prose | pages [31] -->
174

<!-- b000890 | prose | pages [31] -->
关注数学模型

<!-- b000891 | furniture | pages [31] -->
2

<!-- b000892 | furniture | pages [31] -->
MATHmodels

<!-- b000893 | furniture | pages [31] -->
获取更多资讯

<!-- b000894 | furniture | pages [32] -->
Team 2003717

<!-- b000895 | prose | pages [32] -->
175

<!-- b000896 | prose | pages [32] -->
176 def trans(k):

<!-- b000897 | prose | pages [32] -->
if k>=0: 177

<!-- b000898 | prose | pages [32] -->
return int(k*50)/50 178

<!-- b000899 | prose | pages [32] -->
return None 179

<!-- b000900 | prose | pages [32] -->
180

<!-- b000901 | furniture | pages [32] -->
Page 31

<!-- b000902 | prose | pages [32] -->
181 review_length = all[all[’total_votes’]>10][[’helpful_rate’, ’review_length’]]

<!-- b000903 | prose | pages [32] -->
182 review_length[’helpful_level’] = pd.Series([trans(k) for k in review_length[’ helpful_rate’]], index=review_length.index)

<!-- b000904 | prose | pages [32] -->
183 review_length.groupby(’helpful_level’)[’review_length’].agg({’average_length’: ’mean’}) .plot()

<!-- b000905 | prose | pages [32] -->
184 plt.scatter(review_length[’helpful_rate’], review_length[’review_length’], s=(2,), c=’# ff00ff’, alpha=0.3)

<!-- b000906 | prose | pages [32] -->
185 # plt.title(’Average Review Length of Helpful Percent’)

<!-- b000907 | prose | pages [32] -->
186 plt.xlabel(’Helpful Percent’)

<!-- b000908 | prose | pages [32] -->
187 plt.ylabel(’Review Length’)

<!-- b000909 | prose | pages [32] -->
188 plt.legend([’Average Review Length’])

<!-- b000910 | prose | pages [32] -->
189 plt.savefig("figure/Average Review Length of Helpful Percent.png",dpi=500,bbox_inches = ’tight’)

<!-- b000911 | prose | pages [32] -->
190 plt.show()

<!-- b000912 | prose | pages [32] -->
191

<!-- b000913 | prose | pages [32] -->
192 star_rating = all[all[’total_votes’]>10][[’helpful_rate’, ’star_rating’]].groupby(’ star_rating’)[’helpful_rate’].mean()

<!-- b000914 | prose | pages [32] -->
193

<!-- b000915 | prose | pages [32] -->
194

<!-- b000916 | prose | pages [32] -->
195 del review_length

<!-- b000917 | prose | pages [32] -->
196

<!-- b000918 | prose | pages [32] -->
197

<!-- b000919 | prose | pages [32] -->
198 #######################################################

<!-- b000920 | prose | pages [32] -->
199 ### 2.6. Plot 6

<!-- b000921 | prose | pages [32] -->
200 #######################################################

<!-- b000922 | prose | pages [32] -->
201

<!-- b000923 | prose | pages [32] -->
202

<!-- b000924 | prose | pages [32] -->
203 star_rating = all[all[’total_votes’]>10][[’helpful_rate’, ’star_rating’]]

<!-- b000925 | prose | pages [32] -->
204 star_rating[’helpful_level’] = pd.Series([trans(k) for k in star_rating[’helpful_rate’ ]], index=star_rating.index)

<!-- b000926 | prose | pages [32] -->
205 star_rating.groupby(’helpful_level’)[’star_rating’].agg({’Average Star Rating’: ’mean’ }).plot(alpha=0.7)

<!-- b000927 | prose | pages [32] -->
206 helpful_star_frequency = star_rating.groupby([’helpful_level’, ’star_rating’]).count().

<!-- b000928 | prose | pages [32] -->
reset_index()

<!-- b000929 | prose | pages [32] -->
207 helpful_star_frequency.columns = [’helpful_level’, ’star_rating’, ’freqency’]

<!-- b000930 | prose | pages [32] -->
208 plt.scatter(helpful_star_frequency[’helpful_level’], helpful_star_frequency[’ star_rating’], helpful_star_frequency[’freqency’]*10,

<!-- b000931 | prose | pages [32] -->
c=’#ff00ff’, alpha=0.3) 209

<!-- b000932 | prose | pages [32] -->
210

<!-- b000933 | prose | pages [32] -->
211 # plt.title(’Star Rating of Helpful Percent’)

<!-- b000934 | prose | pages [32] -->
212 plt.xlabel(’Helpful Percent’)

<!-- b000935 | prose | pages [32] -->
213 plt.ylabel(’Star Rating’)

<!-- b000936 | prose | pages [32] -->
214 plt.legend([’Average Star Rating’])

<!-- b000937 | prose | pages [32] -->
215 plt.savefig("figure/Star Rating of Helpful Percent.png",dpi=500,bbox_inches = ’tight’)

<!-- b000938 | prose | pages [32] -->
216 plt.show()

<!-- b000939 | prose | pages [32] -->
217

<!-- b000940 | prose | pages [32] -->
218

<!-- b000941 | prose | pages [32] -->
219 del star_rating , helpful_star_frequency

<!-- b000942 | prose | pages [32] -->
220

<!-- b000943 | prose | pages [32] -->
221

<!-- b000944 | prose | pages [32] -->
222 #######################################################

<!-- b000945 | prose | pages [32] -->
223 ### 2.7. Plot 7

<!-- b000946 | prose | pages [32] -->
224 #######################################################

<!-- b000947 | prose | pages [32] -->
225

<!-- b000948 | prose | pages [32] -->
226

<!-- b000949 | prose | pages [32] -->
227 def product_date_process(dataset , threshold):

<!-- b000950 | prose | pages [32] -->
product = dataset.groupby(’product_id’)[’star_rating’].agg({’count’: ’count’}) 228

<!-- b000951 | prose | pages [32] -->
关注数学模型

<!-- b000952 | furniture | pages [32] -->
2

<!-- b000953 | furniture | pages [32] -->
MATHmodels

<!-- b000954 | furniture | pages [32] -->
获取更多资讯

<!-- b000955 | furniture | pages [33] -->
Team 2003717

<!-- b000956 | furniture | pages [33] -->
Page 32

<!-- b000957 | prose | pages [33] -->
product = product[product[’count’]>threshold].reset_index()[’product_id’] 229

<!-- b000958 | prose | pages [33] -->
230

<!-- b000959 | prose | pages [33] -->
product_date = dataset.groupby([’product_id’, ’year’, ’month’])[’star_rating’, ’ 231 review_length’].agg({’star_rating’:[’count’, ’mean’], ’review_length’: ’mean’})

<!-- b000960 | prose | pages [33] -->
product_date.columns = [’count’, ’avg_star’, ’avg_length’] 232

<!-- b000961 | prose | pages [33] -->
product_date = product_date.reset_index() 233

<!-- b000962 | prose | pages [33] -->
product_date[’date’] = product_date[’year’] + product_date[’month’] / 12 234

<!-- b000963 | prose | pages [33] -->
product_date = product_date.drop([’year’, ’month’], axis=1).set_index([’product_id’ 235 , ’date’]).loc[product]

<!-- b000964 | prose | pages [33] -->
return product_date 236

<!-- b000965 | prose | pages [33] -->
237

<!-- b000966 | prose | pages [33] -->
238

<!-- b000967 | prose | pages [33] -->
239 product_date_h = product_date_process(new_hair_dryer , 400)

<!-- b000968 | prose | pages [33] -->
240 p, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)

<!-- b000969 | prose | pages [33] -->
241 product_date_h[’count’].unstack().T.sort_index().plot(ax=ax1, figsize=(5,7))

<!-- b000970 | prose | pages [33] -->
242 product_date_h[’avg_star’].unstack().T.sort_index().plot(ax=ax2, legend=False)

<!-- b000971 | prose | pages [33] -->
243 product_date_h[’avg_length’].unstack().T.sort_index().plot(ax=ax3, legend=False)

<!-- b000972 | prose | pages [33] -->
244 ax1.set_ylabel(’Review Amount’)

<!-- b000973 | prose | pages [33] -->
245 ax2.set_ylabel(’Average Star Rating’)

<!-- b000974 | prose | pages [33] -->
246 ax3.set_ylabel(’Average Review Length’)

<!-- b000975 | prose | pages [33] -->
247 plt.savefig("figure/Product Infomation for Date of Hair Dryer.png",dpi=500,bbox_inches = ’tight’)

<!-- b000976 | prose | pages [33] -->
248 plt.show()

<!-- b000977 | prose | pages [33] -->
249

<!-- b000978 | prose | pages [33] -->
250

<!-- b000979 | prose | pages [33] -->
251 product_date_m = product_date_process(new_microwave , 78)

<!-- b000980 | prose | pages [33] -->
252 p, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)

<!-- b000981 | prose | pages [33] -->
253 product_date_m[’count’].unstack().T.sort_index().plot(ax=ax1, figsize=(5,7))

<!-- b000982 | prose | pages [33] -->
254 product_date_m[’avg_star’].unstack().T.sort_index().plot(ax=ax2, legend=False)

<!-- b000983 | prose | pages [33] -->
255 product_date_m[’avg_length’].unstack().T.sort_index().plot(ax=ax3, legend=False)

<!-- b000984 | prose | pages [33] -->
256 ax1.set_ylabel(’Review Amount’)

<!-- b000985 | prose | pages [33] -->
257 ax2.set_ylabel(’Average Star Rating’)

<!-- b000986 | prose | pages [33] -->
258 ax3.set_ylabel(’Average Review Length’)

<!-- b000987 | prose | pages [33] -->
259 plt.xticks(np.arange(2012, 2016))

<!-- b000988 | prose | pages [33] -->
260 plt.savefig("figure/Product Infomation for Date of Microwave.png",dpi=500,bbox_inches = ’tight’)

<!-- b000989 | prose | pages [33] -->
261 plt.show()

<!-- b000990 | prose | pages [33] -->
262

<!-- b000991 | prose | pages [33] -->
263

<!-- b000992 | prose | pages [33] -->
264 product_date_p = product_date_process(new_pacifier , 250)

<!-- b000993 | prose | pages [33] -->
265 p, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)

<!-- b000994 | prose | pages [33] -->
266 product_date_p[’count’].unstack().T.sort_index().plot(ax=ax1, figsize=(5,7))

<!-- b000995 | prose | pages [33] -->
267 product_date_p[’avg_star’].unstack().T.sort_index().plot(ax=ax2, legend=False)

<!-- b000996 | prose | pages [33] -->
268 product_date_p[’avg_length’].unstack().T.sort_index().plot(ax=ax3, legend=False)

<!-- b000997 | prose | pages [33] -->
269 ax1.set_ylabel(’Review Amount’)

<!-- b000998 | prose | pages [33] -->
270 ax2.set_ylabel(’Average Star Rating’)

<!-- b000999 | prose | pages [33] -->
271 ax3.set_ylabel(’Average Review Length’)

<!-- b001000 | prose | pages [33] -->
272 plt.savefig("figure/Product Infomation for Date of Pacifier.png",dpi=500,bbox_inches = ’tight’)

<!-- b001001 | prose | pages [33] -->
273 plt.show()

<!-- b001002 | prose | pages [33] -->
274

<!-- b001003 | prose | pages [33] -->
275

<!-- b001004 | prose | pages [33] -->
276 product_date_h = product_date_process(new_hair_dryer , 100).reset_index()

<!-- b001005 | prose | pages [33] -->
277 p, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(15,7))

<!-- b001006 | prose | pages [33] -->
278 ax1.scatter(product_date_h[’date’], product_date_h[’product_id’], product_date_h[’count ’]*10, c=’#ff0000’, alpha=0.2)

<!-- b001007 | prose | pages [33] -->
279 ax2.scatter(product_date_h[’date’], product_date_h[’product_id’], product_date_h[’ avg_star’]*20, c=’#ff0000’, alpha=0.2)

<!-- b001008 | prose | pages [33] -->
280 ax3.scatter(product_date_h[’date’], product_date_h[’product_id’], product_date_h[’ avg_length’]/5, c=’#ff0000’, alpha=0.2)

<!-- b001009 | prose | pages [33] -->
281 ax1.set_title(’Review Amount’)

<!-- b001010 | prose | pages [33] -->
282 ax2.set_title(’Average Star Rating’)

<!-- b001011 | prose | pages [33] -->
283 ax3.set_title(’Average Review Length’)

<!-- b001012 | prose | pages [33] -->
关注数学模型

<!-- b001013 | furniture | pages [33] -->
2

<!-- b001014 | furniture | pages [33] -->
MATHmodels

<!-- b001015 | furniture | pages [33] -->
获取更多资讯

<!-- b001016 | furniture | pages [34] -->
Team 2003717

<!-- b001017 | prose | pages [34] -->
284 ax1.set_xlabel(’Date’)

<!-- b001018 | prose | pages [34] -->
285 ax2.set_xlabel(’Date’)

<!-- b001019 | prose | pages [34] -->
286 ax3.set_xlabel(’Date’)

<!-- b001020 | prose | pages [34] -->
287 ax1.set_ylabel(’Product ID’)

<!-- b001021 | furniture | pages [34] -->
Page 33

<!-- b001022 | prose | pages [34] -->
288 plt.savefig("figure/Product Contrast for Date of Hair Dryer.png",dpi=100,bbox_inches = ’tight’)

<!-- b001023 | prose | pages [34] -->
289 plt.show()

<!-- b001024 | prose | pages [34] -->
290

<!-- b001025 | prose | pages [34] -->
291

<!-- b001026 | prose | pages [34] -->
292 product_date_m = product_date_process(new_microwave , 15).reset_index()

<!-- b001027 | prose | pages [34] -->
293 p, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(15,7))

<!-- b001028 | prose | pages [34] -->
294 ax1.scatter(product_date_m[’date’], product_date_m[’product_id’], product_date_m[’count ’]*30, c=’#ff0000’, alpha=0.2)

<!-- b001029 | prose | pages [34] -->
295 ax2.scatter(product_date_m[’date’], product_date_m[’product_id’], product_date_m[’ avg_star’]*20, c=’#ff0000’, alpha=0.2)

<!-- b001030 | prose | pages [34] -->
296 ax3.scatter(product_date_m[’date’], product_date_m[’product_id’], product_date_m[’ avg_length’]/5, c=’#ff0000’, alpha=0.2)

<!-- b001031 | prose | pages [34] -->
297 ax1.set_title(’Review Amount’)

<!-- b001032 | prose | pages [34] -->
298 ax2.set_title(’Average Star Rating’)

<!-- b001033 | prose | pages [34] -->
299 ax3.set_title(’Average Review Length’)

<!-- b001034 | prose | pages [34] -->
300 ax1.set_xlabel(’Date’)

<!-- b001035 | prose | pages [34] -->
301 ax2.set_xlabel(’Date’)

<!-- b001036 | prose | pages [34] -->
302 ax3.set_xlabel(’Date’)

<!-- b001037 | prose | pages [34] -->
303 ax1.set_ylabel(’Product ID’)

<!-- b001038 | prose | pages [34] -->
304 plt.savefig("figure/Product Contrast for Date of Microwave.png",dpi=100,bbox_inches = ’ tight’)

<!-- b001039 | prose | pages [34] -->
305 plt.show()

<!-- b001040 | prose | pages [34] -->
306

<!-- b001041 | prose | pages [34] -->
307

<!-- b001042 | prose | pages [34] -->
308 product_date_p = product_date_process(new_pacifier , 60).reset_index()

<!-- b001043 | prose | pages [34] -->
309 p, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(15,7))

<!-- b001044 | prose | pages [34] -->
310 ax1.scatter(product_date_p[’date’], product_date_p[’product_id’], product_date_p[’count ’]*10, c=’#ff0000’, alpha=0.2)

<!-- b001045 | prose | pages [34] -->
311 ax2.scatter(product_date_p[’date’], product_date_p[’product_id’], product_date_p[’ avg_star’]*20, c=’#ff0000’, alpha=0.2)

<!-- b001046 | prose | pages [34] -->
312 ax3.scatter(product_date_p[’date’], product_date_p[’product_id’], product_date_p[’ avg_length’]/5, c=’#ff0000’, alpha=0.2)

<!-- b001047 | prose | pages [34] -->
313 ax1.set_title(’Review Amount’)

<!-- b001048 | prose | pages [34] -->
314 ax2.set_title(’Average Star Rating’)

<!-- b001049 | prose | pages [34] -->
315 ax3.set_title(’Average Review Length’)

<!-- b001050 | prose | pages [34] -->
316 ax1.set_xlabel(’Date’)

<!-- b001051 | prose | pages [34] -->
317 ax2.set_xlabel(’Date’)

<!-- b001052 | prose | pages [34] -->
318 ax3.set_xlabel(’Date’)

<!-- b001053 | prose | pages [34] -->
319 ax1.set_ylabel(’Product ID’)

<!-- b001054 | prose | pages [34] -->
320 plt.savefig("figure/Product Contrast for Date of Pacifier.png",dpi=100,bbox_inches = ’ tight’)

<!-- b001055 | prose | pages [34] -->
321 plt.show()

<!-- b001056 | prose | pages [34] -->
322

<!-- b001057 | prose | pages [34] -->
323

<!-- b001058 | prose | pages [34] -->
324 del p, ax1, ax2, ax3, product_date_h , product_date_m , product_date_p

<!-- b001059 | prose | pages [34] -->
C.2 LDA Analysis

<!-- b001060 | prose | pages [34] -->
1 ’’’

<!-- b001061 | prose | pages [34] -->
2 !pip install PyDrive

<!-- b001062 | prose | pages [34] -->
3 !pip install gensim

<!-- b001063 | prose | pages [34] -->
4 !pip install pyldavis

<!-- b001064 | prose | pages [34] -->
5 !python - m spacy download en

<!-- b001065 | prose | pages [34] -->
6 ’’’

<!-- b001066 | prose | pages [34] -->
7 import gzip

<!-- b001067 | prose | pages [34] -->
8 import json

<!-- b001068 | prose | pages [34] -->
关注数学模型

<!-- b001069 | furniture | pages [34] -->
2

<!-- b001070 | furniture | pages [34] -->
MATHmodels

<!-- b001071 | furniture | pages [34] -->
获取更多资讯

<!-- b001072 | furniture | pages [35] -->
Team 2003717

<!-- b001073 | prose | pages [35] -->
9 import os

<!-- b001074 | prose | pages [35] -->
10 import re

<!-- b001075 | prose | pages [35] -->
11 from itertools import chain

<!-- b001076 | prose | pages [35] -->
12 from string import punctuation

<!-- b001077 | prose | pages [35] -->
13

<!-- b001078 | prose | pages [35] -->
14 import gensim

<!-- b001079 | prose | pages [35] -->
15 import jieba

<!-- b001080 | prose | pages [35] -->
16 import matplotlib.pyplot as plt

<!-- b001081 | prose | pages [35] -->
17 import nltk

<!-- b001082 | prose | pages [35] -->
18 import numpy as np

<!-- b001083 | prose | pages [35] -->
19 import pandas as pd

<!-- b001084 | prose | pages [35] -->
20 from gensim import corpora

<!-- b001085 | prose | pages [35] -->
21 from google.colab import auth, drive

<!-- b001086 | prose | pages [35] -->
22 from nltk import FreqDist , ngrams

<!-- b001087 | prose | pages [35] -->
23 from nltk.corpus import stopwords

<!-- b001088 | prose | pages [35] -->
24 from nltk.stem import WordNetLemmatizer

<!-- b001089 | prose | pages [35] -->
25 from sklearn import svm

<!-- b001090 | prose | pages [35] -->
26 from sklearn.dummy import DummyClassifier

<!-- b001091 | furniture | pages [35] -->
Page 34

<!-- b001092 | prose | pages [35] -->
27 from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer

<!-- b001093 | prose | pages [35] -->
28 from sklearn.linear_model import LogisticRegression

<!-- b001094 | prose | pages [35] -->
29 from sklearn.model_selection import train_test_split

<!-- b001095 | prose | pages [35] -->
30

<!-- b001096 | prose | pages [35] -->
31 import pyLDAvis

<!-- b001097 | prose | pages [35] -->
32 import pyLDAvis.gensim

<!-- b001098 | prose | pages [35] -->
33 import seaborn as sns

<!-- b001099 | prose | pages [35] -->
34 import spacy

<!-- b001100 | prose | pages [35] -->
35 from oauth2client.client import GoogleCredentials

<!-- b001101 | prose | pages [35] -->
36 from pydrive.auth import GoogleAuth

<!-- b001102 | prose | pages [35] -->
37 from pydrive.drive import GoogleDrive

<!-- b001103 | prose | pages [35] -->
38 from wordcloud import WordCloud

<!-- b001104 | prose | pages [35] -->
39

<!-- b001105 | prose | pages [35] -->
40 drive.mount(’/content/drive’)

<!-- b001106 | prose | pages [35] -->
41

<!-- b001107 | prose | pages [35] -->
42 nltk.download(’stopwords’)

<!-- b001108 | prose | pages [35] -->
43

<!-- b001109 | prose | pages [35] -->
44

<!-- b001110 | prose | pages [35] -->
45 pd.set_option("display.max_colwidth", 200)

<!-- b001111 | prose | pages [35] -->
46

<!-- b001112 | prose | pages [35] -->
47

<!-- b001113 | prose | pages [35] -->
48 %matplotlib inline

<!-- b001114 | prose | pages [35] -->
49

<!-- b001115 | prose | pages [35] -->
50

<!-- b001116 | prose | pages [35] -->
51 hair_dryer = pd.read_csv(’/content/drive/My Drive/data/new_hair_dryer.csv’)

<!-- b001117 | prose | pages [35] -->
52 microwave = pd.read_csv(’/content/drive/My Drive/data/new_microwave.csv’)

<!-- b001118 | prose | pages [35] -->
53 pacifier = pd.read_csv(’/content/drive/My Drive/data/new_pacifier.csv’)

<!-- b001119 | prose | pages [35] -->
54 hair_dryer1 = pd.read_csv(

<!-- b001120 | prose | pages [35] -->
’/content/drive/My Drive/classify_byrating/hair_dryer/rating1.csv’) 55

<!-- b001121 | prose | pages [35] -->
56 hair_dryer2 = pd.read_csv(

<!-- b001122 | prose | pages [35] -->
’/content/drive/My Drive/classify_byrating/hair_dryer/rating2.csv’) 57

<!-- b001123 | prose | pages [35] -->
58 hair_dryer3 = pd.read_csv(

<!-- b001124 | prose | pages [35] -->
’/content/drive/My Drive/classify_byrating/hair_dryer/rating3.csv’) 59

<!-- b001125 | prose | pages [35] -->
60 hair_dryer4 = pd.read_csv(

<!-- b001126 | prose | pages [35] -->
’/content/drive/My Drive/classify_byrating/hair_dryer/rating4.csv’) 61

<!-- b001127 | prose | pages [35] -->
62 hair_dryer5 = pd.read_csv(

<!-- b001128 | prose | pages [35] -->
’/content/drive/My Drive/classify_byrating/hair_dryer/rating5.csv’) 63

<!-- b001129 | prose | pages [35] -->
64 microwave1 = pd.read_csv(

<!-- b001130 | prose | pages [35] -->
’/content/drive/My Drive/classify_byrating/microwave/rating1.csv’) 65

<!-- b001131 | prose | pages [35] -->
66 microwave2 = pd.read_csv(

<!-- b001132 | prose | pages [35] -->
’/content/drive/My Drive/classify_byrating/microwave/rating2.csv’) 67

<!-- b001133 | prose | pages [35] -->
68 microwave3 = pd.read_csv(

<!-- b001134 | prose | pages [35] -->
’/content/drive/My Drive/classify_byrating/microwave/rating3.csv’) 69

<!-- b001135 | prose | pages [35] -->
70 microwave4 = pd.read_csv(

<!-- b001136 | prose | pages [35] -->
’/content/drive/My Drive/classify_byrating/microwave/rating4.csv’) 71

<!-- b001137 | prose | pages [35] -->
关注数学模型

<!-- b001138 | furniture | pages [35] -->
2

<!-- b001139 | furniture | pages [35] -->
MATHmodels

<!-- b001140 | furniture | pages [35] -->
获取更多资讯

<!-- b001141 | furniture | pages [36] -->
Team 2003717

<!-- b001142 | prose | pages [36] -->
72 microwave5 = pd.read_csv(

<!-- b001143 | furniture | pages [36] -->
Page 35

<!-- b001144 | prose | pages [36] -->
’/content/drive/My Drive/classify_byrating/microwave/rating5.csv’) 73

<!-- b001145 | prose | pages [36] -->
74 pacifier1 = pd.read_csv(

<!-- b001146 | prose | pages [36] -->
’/content/drive/My Drive/classify_byrating/pacifier/rating1.csv’) 75

<!-- b001147 | prose | pages [36] -->
76 pacifier2 = pd.read_csv(

<!-- b001148 | prose | pages [36] -->
’/content/drive/My Drive/classify_byrating/pacifier/rating2.csv’) 77

<!-- b001149 | prose | pages [36] -->
78 pacifier3 = pd.read_csv(

<!-- b001150 | prose | pages [36] -->
’/content/drive/My Drive/classify_byrating/pacifier/rating3.csv’) 79

<!-- b001151 | prose | pages [36] -->
80 pacifier4 = pd.read_csv(

<!-- b001152 | prose | pages [36] -->
’/content/drive/My Drive/classify_byrating/pacifier/rating4.csv’) 81

<!-- b001153 | prose | pages [36] -->
82 pacifier5 = pd.read_csv(

<!-- b001154 | prose | pages [36] -->
’/content/drive/My Drive/classify_byrating/pacifier/rating5.csv’) 83

<!-- b001155 | prose | pages [36] -->
84

<!-- b001156 | prose | pages [36] -->
85 add_punc = ’ {}()%^>.^-=&#@’

<!-- b001157 | prose | pages [36] -->
86 add_punc = add_punc+punctuation

<!-- b001158 | prose | pages [36] -->
87 h_head1 = hair_dryer1.review_headline.tolist()

<!-- b001159 | prose | pages [36] -->
88 m_head1 = microwave1.review_headline.tolist()

<!-- b001160 | prose | pages [36] -->
89 p_head1 = pacifier1.review_headline.astype(str).tolist()

<!-- b001161 | prose | pages [36] -->
90 h_head2 = hair_dryer2.review_headline.tolist()

<!-- b001162 | prose | pages [36] -->
91 m_head2 = microwave2.review_headline.tolist()

<!-- b001163 | prose | pages [36] -->
92 p_head2 = pacifier2.review_headline.astype(str).tolist()

<!-- b001164 | prose | pages [36] -->
93 h_head3 = hair_dryer3.review_headline.tolist()

<!-- b001165 | prose | pages [36] -->
94 m_head3 = microwave3.review_headline.tolist()

<!-- b001166 | prose | pages [36] -->
95 p_head3 = pacifier3.review_headline.astype(str).tolist()

<!-- b001167 | prose | pages [36] -->
96 h_head4 = hair_dryer4.review_headline.tolist()

<!-- b001168 | prose | pages [36] -->
97 m_head4 = microwave4.review_headline.tolist()

<!-- b001169 | prose | pages [36] -->
98 p_head4 = pacifier4.review_headline.astype(str).tolist()

<!-- b001170 | prose | pages [36] -->
99 h_head5 = hair_dryer5.review_headline.tolist()

<!-- b001171 | prose | pages [36] -->
100 m_head5 = microwave5.review_headline.tolist()

<!-- b001172 | prose | pages [36] -->
101 p_head5 = pacifier5.review_headline.astype(str).tolist()

<!-- b001173 | prose | pages [36] -->
102

<!-- b001174 | prose | pages [36] -->
103 h_body1 = hair_dryer1.review_body.tolist()

<!-- b001175 | prose | pages [36] -->
104 m_body1 = microwave1.review_body.tolist()

<!-- b001176 | prose | pages [36] -->
105 p_body1 = pacifier1.review_body.astype(str).tolist()

<!-- b001177 | prose | pages [36] -->
106 h_body2 = hair_dryer2.review_body.tolist()

<!-- b001178 | prose | pages [36] -->
107 m_body2 = microwave2.review_body.tolist()

<!-- b001179 | prose | pages [36] -->
108 p_body2 = pacifier2.review_body.astype(str).tolist()

<!-- b001180 | prose | pages [36] -->
109 h_body3 = hair_dryer3.review_body.tolist()

<!-- b001181 | prose | pages [36] -->
110 m_body3 = microwave3.review_body.tolist()

<!-- b001182 | prose | pages [36] -->
111 p_body3 = pacifier3.review_body.astype(str).tolist()

<!-- b001183 | prose | pages [36] -->
112 h_body4 = hair_dryer4.review_body.tolist()

<!-- b001184 | prose | pages [36] -->
113 m_body4 = microwave4.review_body.tolist()

<!-- b001185 | prose | pages [36] -->
114 p_body4 = pacifier4.review_body.astype(str).tolist()

<!-- b001186 | prose | pages [36] -->
115 h_body5 = hair_dryer5.review_body.tolist()

<!-- b001187 | prose | pages [36] -->
116 m_body5 = microwave5.review_body.tolist()

<!-- b001188 | prose | pages [36] -->
117 p_body5 = pacifier5.review_body.astype(str).tolist()

<!-- b001189 | prose | pages [36] -->
118

<!-- b001190 | prose | pages [36] -->
119

<!-- b001191 | prose | pages [36] -->
120 def freq_words(x, filepath , terms=30):

<!-- b001192 | prose | pages [36] -->
all_words = ’ ’.join([text for text in x]) 121

<!-- b001193 | prose | pages [36] -->
all_words = all_words.split() 122

<!-- b001194 | prose | pages [36] -->
123

<!-- b001195 | prose | pages [36] -->
fdist = FreqDist(all_words) 124

<!-- b001196 | prose | pages [36] -->
words_df = pd.DataFrame( 125

<!-- b001197 | prose | pages [36] -->
{’word’: list(fdist.keys()), ’count’: list(fdist.values())}) 126

<!-- b001198 | prose | pages [36] -->
127

<!-- b001199 | prose | pages [36] -->
# selecting top 20 most frequent words 128

<!-- b001200 | prose | pages [36] -->
d = words_df.nlargest(columns="count", n=terms) 129

<!-- b001201 | prose | pages [36] -->
plt.figure(figsize=(20, 5)) 130

<!-- b001202 | prose | pages [36] -->
ax = sns.barplot(data=d, x="word", y="count") 131

<!-- b001203 | prose | pages [36] -->
ax.set(ylabel=’Count’) 132

<!-- b001204 | prose | pages [36] -->
plt.show() 133

<!-- b001205 | prose | pages [36] -->
plt.savefig(filepath) 134

<!-- b001206 | prose | pages [36] -->
关注数学模型

<!-- b001207 | furniture | pages [36] -->
2

<!-- b001208 | furniture | pages [36] -->
MATHmodels

<!-- b001209 | furniture | pages [36] -->
获取更多资讯

<!-- b001210 | furniture | pages [37] -->
Team 2003717

<!-- b001211 | prose | pages [37] -->
135

<!-- b001212 | prose | pages [37] -->
136

<!-- b001213 | furniture | pages [37] -->
Page 36

<!-- b001214 | prose | pages [37] -->
137 hair_dryer[’review_body’] = hair_dryer[’review_body’].str.replace(

<!-- b001215 | prose | pages [37] -->
"n\’t", " not") 138

<!-- b001216 | prose | pages [37] -->
139

<!-- b001217 | prose | pages [37] -->
140 # remove unwanted characters , numbers and symbols

<!-- b001218 | prose | pages [37] -->
141 hair_dryer[’review_body’] = hair_dryer[’review_body’].str.replace(

<!-- b001219 | prose | pages [37] -->
"[^a-zA-Z#]", " ") 142

<!-- b001220 | prose | pages [37] -->
143 stop_words = stopwords.words(’english’)

<!-- b001221 | prose | pages [37] -->
144

<!-- b001222 | prose | pages [37] -->
145 # function to remove stopwords

<!-- b001223 | prose | pages [37] -->
146

<!-- b001224 | prose | pages [37] -->
147

<!-- b001225 | prose | pages [37] -->
148 def remove_stopwords(rev):

<!-- b001226 | prose | pages [37] -->
rev_new = " ".join([i for i in rev if i not in stop_words]) 149

<!-- b001227 | prose | pages [37] -->
return rev_new 150

<!-- b001228 | prose | pages [37] -->
151

<!-- b001229 | prose | pages [37] -->
152

<!-- b001230 | prose | pages [37] -->
153 # remove short words (length < 3)

<!-- b001231 | prose | pages [37] -->
154 hair_dryer[’review_body’] = hair_dryer[’review_body’].apply(

<!-- b001232 | prose | pages [37] -->
lambda x: ’ ’.join([w for w in x.split() if len(w) > 2])) 155

<!-- b001233 | prose | pages [37] -->
156

<!-- b001234 | prose | pages [37] -->
157 # remove stopwords from the text

<!-- b001235 | prose | pages [37] -->
158 reviews = [remove_stopwords(r.split()) for r in hair_dryer[’review_body’]]

<!-- b001236 | prose | pages [37] -->
159

<!-- b001237 | prose | pages [37] -->
160 # make entire text lowercase

<!-- b001238 | prose | pages [37] -->
161 reviews = [r.lower() for r in reviews]

<!-- b001239 | prose | pages [37] -->
162

<!-- b001240 | prose | pages [37] -->
163 nlp = spacy.load(’en’, disable=[’parser’, ’ner’])

<!-- b001241 | prose | pages [37] -->
164

<!-- b001242 | prose | pages [37] -->
165

<!-- b001243 | prose | pages [37] -->
166 def lemmatization(texts, tags=[’NOUN’, ’ADJ’]):

<!-- b001244 | prose | pages [37] -->
output = [] 167

<!-- b001245 | prose | pages [37] -->
for sent in texts: 168

<!-- b001246 | prose | pages [37] -->
doc = nlp(" ".join(sent)) 169

<!-- b001247 | prose | pages [37] -->
output.append([token.lemma_ for token in doc if token.pos_ in tags]) 170

<!-- b001248 | prose | pages [37] -->
return output 171

<!-- b001249 | prose | pages [37] -->
172

<!-- b001250 | prose | pages [37] -->
173

<!-- b001251 | prose | pages [37] -->
174 tokenized_reviews = pd.Series(reviews).apply(lambda x: x.split())

<!-- b001252 | prose | pages [37] -->
175 reviews_2 = lemmatization(tokenized_reviews)

<!-- b001253 | prose | pages [37] -->
176 reviews_3 = []

<!-- b001254 | prose | pages [37] -->
177 for i in range(len(reviews_2)):

<!-- b001255 | prose | pages [37] -->
reviews_3.append(’ ’.join(reviews_2[i])) 178

<!-- b001256 | prose | pages [37] -->
179

<!-- b001257 | prose | pages [37] -->
180 freq_words(reviews_3 , ’/content/drive/My Drive/classify_byrating/main_word_h’, 35)

<!-- b001258 | prose | pages [37] -->
181

<!-- b001259 | prose | pages [37] -->
182 dictionary = corpora.Dictionary(reviews_2)

<!-- b001260 | prose | pages [37] -->
183 doc_term_matrix = [dictionary.doc2bow(rev) for rev in reviews_2]

<!-- b001261 | prose | pages [37] -->
184 LDA = gensim.models.ldamodel.LdaModel

<!-- b001262 | prose | pages [37] -->
185 lda_model = LDA(corpus=doc_term_matrix ,

<!-- b001263 | prose | pages [37] -->
id2word=dictionary , 186

<!-- b001264 | prose | pages [37] -->
num_topics=7, 187

<!-- b001265 | prose | pages [37] -->
random_state=100, 188

<!-- b001266 | prose | pages [37] -->
chunksize=1000, 189

<!-- b001267 | prose | pages [37] -->
passes=50) 190

<!-- b001268 | prose | pages [37] -->
191 lda_model.print_topics()

<!-- b001269 | prose | pages [37] -->
192 # Visualize the topics

<!-- b001270 | prose | pages [37] -->
193 pyLDAvis.enable_notebook()

<!-- b001271 | prose | pages [37] -->
194 vis = pyLDAvis.gensim.prepare(lda_model , doc_term_matrix , dictionary)

<!-- b001272 | prose | pages [37] -->
195 vis

<!-- b001273 | prose | pages [37] -->
关注数学模型

<!-- b001274 | furniture | pages [37] -->
2

<!-- b001275 | furniture | pages [37] -->
MATHmodels

<!-- b001276 | furniture | pages [37] -->
获取更多资讯

<!-- b001277 | furniture | pages [38] -->
Team 2003717

<!-- b001278 | prose | pages [38] -->
C.3 Sentimental Score

<!-- b001279 | prose | pages [38] -->
1 import plotly.graph_objects as go

<!-- b001280 | prose | pages [38] -->
2

<!-- b001281 | prose | pages [38] -->
3 c = CountVectorizer(stop_words=’english’)

<!-- b001282 | furniture | pages [38] -->
Page 37

<!-- b001283 | prose | pages [38] -->
4 pacifier_pol = pacifier[pacifier[’star_rating’] != 3]

<!-- b001284 | prose | pages [38] -->
5 X = pacifier_pol[’review_body’]

<!-- b001285 | prose | pages [38] -->
6 y_dict = {1: 0, 2: 0, 4: 1, 5: 1}

<!-- b001286 | prose | pages [38] -->
7 y = pacifier_pol[’star_rating’].map(y_dict)

<!-- b001287 | prose | pages [38] -->
8

<!-- b001288 | prose | pages [38] -->
9

<!-- b001289 | prose | pages [38] -->
10 def text_fit(X, y, model, clf_model):

<!-- b001290 | prose | pages [38] -->
11

<!-- b001291 | prose | pages [38] -->
X_c = model.fit_transform(X) 12

<!-- b001292 | prose | pages [38] -->
print(’# features: {}’.format(X_c.shape[1])) 13

<!-- b001293 | prose | pages [38] -->
X_train , X_test, y_train , y_test = train_test_split(X_c, y, random_state=0) 14

<!-- b001294 | prose | pages [38] -->
print(’# train records: {}’.format(X_train.shape[0])) 15

<!-- b001295 | prose | pages [38] -->
print(’# test records: {}’.format(X_test.shape[0])) 16

<!-- b001296 | prose | pages [38] -->
clf = clf_model.fit(X_train , y_train) 17

<!-- b001297 | prose | pages [38] -->
acc = clf.score(X_test, y_test) 18

<!-- b001298 | prose | pages [38] -->
print(’Model Accuracy: {}’.format(acc)) 19

<!-- b001299 | prose | pages [38] -->
20

<!-- b001300 | prose | pages [38] -->
w = model.get_feature_names() 21

<!-- b001301 | prose | pages [38] -->
coef = clf.coef_.tolist()[0] 22

<!-- b001302 | prose | pages [38] -->
coeff_df = pd.DataFrame({’Word’: w, ’Coefficient’: coef}) 23

<!-- b001303 | prose | pages [38] -->
coeff_df = coeff_df.sort_values([’Coefficient’, ’Word’], ascending=[0, 1]) 24

<!-- b001304 | prose | pages [38] -->
# print(’’) 25

<!-- b001305 | prose | pages [38] -->
#print(’-Top 20 positive -’) 26

<!-- b001306 | prose | pages [38] -->
# print(coeff_df.head(100).to_string(index=False)) 27

<!-- b001307 | prose | pages [38] -->
# print(’’) 28

<!-- b001308 | prose | pages [38] -->
#print(’-Top 20 negative -’) 29

<!-- b001309 | prose | pages [38] -->
# print(coeff_df.tail(100).to_string(index=False)) 30

<!-- b001310 | prose | pages [38] -->
return coeff_df 31

<!-- b001311 | prose | pages [38] -->
32

<!-- b001312 | prose | pages [38] -->
33

<!-- b001313 | prose | pages [38] -->
34 coeff_df = text_fit(X, y, c, LogisticRegression())

<!-- b001314 | prose | pages [38] -->
35 senti_mark_p = [[], [], [], [], []]

<!-- b001315 | prose | pages [38] -->
36 for i in range(len(p_body1)):

<!-- b001316 | prose | pages [38] -->
senti_mark_p[0].append(0) 37

<!-- b001317 | prose | pages [38] -->
38 for i in range(len(p_body2)):

<!-- b001318 | prose | pages [38] -->
senti_mark_p[1].append(0) 39

<!-- b001319 | prose | pages [38] -->
40 for i in range(len(p_body3)):

<!-- b001320 | prose | pages [38] -->
senti_mark_p[2].append(0) 41

<!-- b001321 | prose | pages [38] -->
42 for i in range(len(p_body4)):

<!-- b001322 | prose | pages [38] -->
senti_mark_p[3].append(0) 43

<!-- b001323 | prose | pages [38] -->
44 for i in range(len(p_body5)):

<!-- b001324 | prose | pages [38] -->
senti_mark_p[4].append(0) 45

<!-- b001325 | prose | pages [38] -->
46

<!-- b001326 | prose | pages [38] -->
47 for i in range(len(p_body1)):

<!-- b001327 | prose | pages [38] -->
words = jieba.cut(p_body1[i], cut_all=True) 48

<!-- b001328 | prose | pages [38] -->
for s in words: 49

<!-- b001329 | prose | pages [38] -->
if s.strip() in add_punc: 50

<!-- b001330 | prose | pages [38] -->
pass 51

<!-- b001331 | prose | pages [38] -->
else: 52

<!-- b001332 | prose | pages [38] -->
if s.strip() in list(coeff_df.Word): 53

<!-- b001333 | prose | pages [38] -->
senti_mark_p[0][i] += coeff_df.iloc[list( 54

<!-- b001334 | prose | pages [38] -->
coeff_df.Word).index(s.strip())].Coefficient 55

<!-- b001335 | prose | pages [38] -->
56 for i in range(len(p_body2)):

<!-- b001336 | prose | pages [38] -->
words = jieba.cut(p_body2[i], cut_all=True) 57

<!-- b001337 | prose | pages [38] -->
for s in words: 58

<!-- b001338 | prose | pages [38] -->
if s.strip() in add_punc: 59

<!-- b001339 | prose | pages [38] -->
pass 60

<!-- b001340 | prose | pages [38] -->
else: 61

<!-- b001341 | prose | pages [38] -->
关注数学模型

<!-- b001342 | furniture | pages [38] -->
2

<!-- b001343 | furniture | pages [38] -->
MATHmodels

<!-- b001344 | furniture | pages [38] -->
获取更多资讯

<!-- b001345 | furniture | pages [39] -->
Team 2003717

<!-- b001346 | furniture | pages [39] -->
Page 38

<!-- b001347 | prose | pages [39] -->
if s.strip() in list(coeff_df.Word): 62

<!-- b001348 | prose | pages [39] -->
senti_mark_p[1][i] += coeff_df.iloc[list( 63

<!-- b001349 | prose | pages [39] -->
coeff_df.Word).index(s.strip())].Coefficient 64

<!-- b001350 | prose | pages [39] -->
65 for i in range(len(p_body3)):

<!-- b001351 | prose | pages [39] -->
words = jieba.cut(p_body3[i], cut_all=True) 66

<!-- b001352 | prose | pages [39] -->
for s in words: 67

<!-- b001353 | prose | pages [39] -->
if s.strip() in add_punc: 68

<!-- b001354 | prose | pages [39] -->
pass 69

<!-- b001355 | prose | pages [39] -->
else: 70

<!-- b001356 | prose | pages [39] -->
if s.strip() in list(coeff_df.Word): 71

<!-- b001357 | prose | pages [39] -->
senti_mark_p[2][i] += coeff_df.iloc[list( 72

<!-- b001358 | prose | pages [39] -->
coeff_df.Word).index(s.strip())].Coefficient 73

<!-- b001359 | prose | pages [39] -->
74 for i in range(len(p_body4)):

<!-- b001360 | prose | pages [39] -->
words = jieba.cut(p_body4[i], cut_all=True) 75

<!-- b001361 | prose | pages [39] -->
for s in words: 76

<!-- b001362 | prose | pages [39] -->
if s.strip() in add_punc: 77

<!-- b001363 | prose | pages [39] -->
pass 78

<!-- b001364 | prose | pages [39] -->
else: 79

<!-- b001365 | prose | pages [39] -->
if s.strip() in list(coeff_df.Word): 80

<!-- b001366 | prose | pages [39] -->
senti_mark_p[3][i] += coeff_df.iloc[list( 81

<!-- b001367 | prose | pages [39] -->
coeff_df.Word).index(s.strip())].Coefficient 82

<!-- b001368 | prose | pages [39] -->
83 for i in range(len(p_body5)):

<!-- b001369 | prose | pages [39] -->
words = jieba.cut(p_body5[i], cut_all=True) 84

<!-- b001370 | prose | pages [39] -->
for s in words: 85

<!-- b001371 | prose | pages [39] -->
if s.strip() in add_punc: 86

<!-- b001372 | prose | pages [39] -->
pass 87

<!-- b001373 | prose | pages [39] -->
else: 88

<!-- b001374 | prose | pages [39] -->
if s.strip() in list(coeff_df.Word): 89

<!-- b001375 | prose | pages [39] -->
senti_mark_p[4][i] += coeff_df.iloc[list( 90

<!-- b001376 | prose | pages [39] -->
coeff_df.Word).index(s.strip())].Coefficient 91

<!-- b001377 | prose | pages [39] -->
92 tmp = []

<!-- b001378 | prose | pages [39] -->
93 for i in range(5):

<!-- b001379 | prose | pages [39] -->
tmp.append(sum(senti_mark_p[i])/len(senti_mark_p[i])) 94

<!-- b001380 | prose | pages [39] -->
95 thresholds_p = []

<!-- b001381 | prose | pages [39] -->
96 for i in range(4):

<!-- b001382 | prose | pages [39] -->
thresholds_p.append((tmp[i]+tmp[i+1])/2) 97

<!-- b001383 | prose | pages [39] -->
98 senti_mark_rank_p = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],

<!-- b001384 | prose | pages [39] -->
[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] 99

<!-- b001385 | prose | pages [39] -->
100 for i in range(5):

<!-- b001386 | prose | pages [39] -->
for j in range(len(senti_mark_p[i])): 101

<!-- b001387 | prose | pages [39] -->
tmp = senti_mark_p[i][j] 102

<!-- b001388 | prose | pages [39] -->
if tmp < thresholds_p[0]: 103

<!-- b001389 | prose | pages [39] -->
senti_mark_rank_p[i][0] += 1 104

<!-- b001390 | prose | pages [39] -->
elif tmp < thresholds_p[1]: 105

<!-- b001391 | prose | pages [39] -->
senti_mark_rank_p[i][1] += 1 106

<!-- b001392 | prose | pages [39] -->
elif tmp < thresholds_p[2]: 107

<!-- b001393 | prose | pages [39] -->
senti_mark_rank_p[i][2] += 1 108

<!-- b001394 | prose | pages [39] -->
elif tmp < thresholds_p[3]: 109

<!-- b001395 | prose | pages [39] -->
senti_mark_rank_p[i][3] += 1 110

<!-- b001396 | prose | pages [39] -->
else: 111

<!-- b001397 | prose | pages [39] -->
senti_mark_rank_p[i][4] += 1 112

<!-- b001398 | prose | pages [39] -->
113

<!-- b001399 | prose | pages [39] -->
114 fig = go.Figure(data=go.Heatmap(

<!-- b001400 | prose | pages [39] -->
z=senti_mark_rank_p , 115

<!-- b001401 | prose | pages [39] -->
x=[’rank1’, ’rank2’, ’rank3’, ’rank4’, ’rank5’], 116

<!-- b001402 | prose | pages [39] -->
y=[’rate1’, ’rate2’, ’rate3’, ’rate4’, ’rate5’], 117

<!-- b001403 | prose | pages [39] -->
hoverongaps=False)) 118

<!-- b001404 | prose | pages [39] -->
119 fig.update_layout(height=500, width=500)

<!-- b001405 | prose | pages [39] -->
120 fig.show()

<!-- b001406 | prose | pages [39] -->
C.4 LSTM

<!-- b001407 | prose | pages [39] -->
关注数学模型

<!-- b001408 | furniture | pages [39] -->
2

<!-- b001409 | furniture | pages [39] -->
MATHmodels

<!-- b001410 | furniture | pages [39] -->
获取更多资讯

<!-- b001411 | furniture | pages [40] -->
Team 2003717

<!-- b001412 | prose | pages [40] -->
1 from __future__ import print_function

<!-- b001413 | prose | pages [40] -->
2

<!-- b001414 | prose | pages [40] -->
3 import time

<!-- b001415 | prose | pages [40] -->
4

<!-- b001416 | prose | pages [40] -->
5 import matplotlib

<!-- b001417 | prose | pages [40] -->
6 import matplotlib.pyplot as plt

<!-- b001418 | prose | pages [40] -->
7 import numpy as np

<!-- b001419 | prose | pages [40] -->
8

<!-- b001420 | prose | pages [40] -->
9 import torch

<!-- b001421 | prose | pages [40] -->
10 import torch.nn as nn

<!-- b001422 | prose | pages [40] -->
11 import torch.optim as optim

<!-- b001423 | prose | pages [40] -->
12 from utils import *

<!-- b001424 | prose | pages [40] -->
13

<!-- b001425 | prose | pages [40] -->
14 matplotlib.use(’Agg’)

<!-- b001426 | prose | pages [40] -->
15

<!-- b001427 | prose | pages [40] -->
16 default_path = ’3_LSTM/’

<!-- b001428 | prose | pages [40] -->
17 output_path = ’3_LSTM/’

<!-- b001429 | furniture | pages [40] -->
Page 39

<!-- b001430 | prose | pages [40] -->
18 products = [’hair_dryer’, ’microwave’, ’pacifier’]

<!-- b001431 | prose | pages [40] -->
19 features = [’star_rating’, ’helpful_votes’, ’total_votes’,

<!-- b001432 | prose | pages [40] -->
’vine’, ’verified_purchase’, ’review_date’] 20

<!-- b001433 | prose | pages [40] -->
21 batch_size = 1

<!-- b001434 | prose | pages [40] -->
22 num_feature = len(features)

<!-- b001435 | prose | pages [40] -->
23 hidden_size = 200

<!-- b001436 | prose | pages [40] -->
24

<!-- b001437 | prose | pages [40] -->
25

<!-- b001438 | prose | pages [40] -->
26 class Sequence(nn.Module):

<!-- b001439 | prose | pages [40] -->
def __init__(self): 27

<!-- b001440 | prose | pages [40] -->
super(Sequence , self).__init__() 28

<!-- b001441 | prose | pages [40] -->
self.lstm1 = nn.LSTMCell(num_feature , hidden_size) 29

<!-- b001442 | prose | pages [40] -->
self.lstm2 = nn.LSTMCell(hidden_size , hidden_size) 30

<!-- b001443 | prose | pages [40] -->
self.linear = nn.Linear(hidden_size , num_feature) 31

<!-- b001444 | prose | pages [40] -->
32

<!-- b001445 | prose | pages [40] -->
def forward(self, input, future=0): 33

<!-- b001446 | prose | pages [40] -->
outputs = [] 34

<!-- b001447 | prose | pages [40] -->
h_t = torch.zeros(input.size(0), hidden_size , dtype=torch.double) 35

<!-- b001448 | prose | pages [40] -->
c_t = torch.zeros(input.size(0), hidden_size , dtype=torch.double) 36

<!-- b001449 | prose | pages [40] -->
h_t2 = torch.zeros(input.size(0), hidden_size , dtype=torch.double) 37

<!-- b001450 | prose | pages [40] -->
c_t2 = torch.zeros(input.size(0), hidden_size , dtype=torch.double) 38

<!-- b001451 | prose | pages [40] -->
39

<!-- b001452 | prose | pages [40] -->
for i, input_t in enumerate(input.chunk(input.size(1), dim=1)): 40

<!-- b001453 | prose | pages [40] -->
input_t = input_t.squeeze(dim=1) 41

<!-- b001454 | prose | pages [40] -->
h_t, c_t = self.lstm1(input_t , (h_t, c_t)) 42

<!-- b001455 | prose | pages [40] -->
h_t2, c_t2 = self.lstm2(h_t, (h_t2, c_t2)) 43

<!-- b001456 | prose | pages [40] -->
output = self.linear(h_t2) 44

<!-- b001457 | prose | pages [40] -->
#assert 0 45

<!-- b001458 | prose | pages [40] -->
outputs += [output] 46

<!-- b001459 | prose | pages [40] -->
47

<!-- b001460 | prose | pages [40] -->
for i in range(future): 48

<!-- b001461 | prose | pages [40] -->
h_t, c_t = self.lstm1(output , (h_t, c_t)) 49

<!-- b001462 | prose | pages [40] -->
h_t2, c_t2 = self.lstm2(h_t, (h_t2, c_t2)) 50

<!-- b001463 | prose | pages [40] -->
output = self.linear(h_t2) 51

<!-- b001464 | prose | pages [40] -->
outputs += [output] 52

<!-- b001465 | prose | pages [40] -->
53

<!-- b001466 | prose | pages [40] -->
outputs = torch.stack(outputs , 1) 54

<!-- b001467 | prose | pages [40] -->
return outputs 55

<!-- b001468 | prose | pages [40] -->
56

<!-- b001469 | prose | pages [40] -->
57

<!-- b001470 | prose | pages [40] -->
58 if __name__ == ’__main__’:

<!-- b001471 | prose | pages [40] -->
np.random.seed(0) 59

<!-- b001472 | prose | pages [40] -->
torch.manual_seed(0) 60

<!-- b001473 | prose | pages [40] -->
61

<!-- b001474 | prose | pages [40] -->
for product in products: 62

<!-- b001475 | prose | pages [40] -->
关注数学模型

<!-- b001476 | furniture | pages [40] -->
2

<!-- b001477 | furniture | pages [40] -->
MATHmodels

<!-- b001478 | furniture | pages [40] -->
获取更多资讯

<!-- b001479 | furniture | pages [41] -->
Team 2003717

<!-- b001480 | furniture | pages [41] -->
Page 40

<!-- b001481 | prose | pages [41] -->
row_data = torch.load(’{}/{}.pt’.format(default_path , product)) 63

<!-- b001482 | prose | pages [41] -->
data, max_per_feature , min_per_feature = standardization(row_data) 64

<!-- b001483 | prose | pages [41] -->
seq_length = row_data.shape[1] 65

<!-- b001484 | prose | pages [41] -->
input = torch.from_numpy(data[:, :-1, :]) 66

<!-- b001485 | prose | pages [41] -->
target = torch.from_numpy(data[:, 1:, :]) 67

<!-- b001486 | prose | pages [41] -->
test_input = torch.from_numpy(data[:, :-1, :]) 68

<!-- b001487 | prose | pages [41] -->
test_target = torch.from_numpy(data[:, 1:, :]) 69

<!-- b001488 | prose | pages [41] -->
70

<!-- b001489 | prose | pages [41] -->
# build the model 71

<!-- b001490 | prose | pages [41] -->
seq = Sequence() 72

<!-- b001491 | prose | pages [41] -->
seq.double() 73

<!-- b001492 | prose | pages [41] -->
criterion = nn.MSELoss() 74

<!-- b001493 | prose | pages [41] -->
optimizer = optim.LBFGS(seq.parameters(), lr=0.8) 75

<!-- b001494 | prose | pages [41] -->
76

<!-- b001495 | prose | pages [41] -->
# begin to train 77

<!-- b001496 | prose | pages [41] -->
for i in range(15): 78

<!-- b001497 | prose | pages [41] -->
print(’START at step ’, i) 79

<!-- b001498 | prose | pages [41] -->
start_time = time.time() 80

<!-- b001499 | prose | pages [41] -->
81

<!-- b001500 | prose | pages [41] -->
def closure(): 82

<!-- b001501 | prose | pages [41] -->
optimizer.zero_grad() 83

<!-- b001502 | prose | pages [41] -->
out = seq(input) 84

<!-- b001503 | prose | pages [41] -->
loss = criterion(out, target) 85

<!-- b001504 | prose | pages [41] -->
print(’===> loss:’, loss.item()) 86

<!-- b001505 | prose | pages [41] -->
loss.backward() 87

<!-- b001506 | prose | pages [41] -->
return loss 88

<!-- b001507 | prose | pages [41] -->
optimizer.step(closure) 89

<!-- b001508 | prose | pages [41] -->
print(’FINISH: {}s’.format(time.time() - start_time)) 90

<!-- b001509 | prose | pages [41] -->
91

<!-- b001510 | prose | pages [41] -->
# begin to predict , no need to track gradient here 92

<!-- b001511 | prose | pages [41] -->
with torch.no_grad(): 93

<!-- b001512 | prose | pages [41] -->
future = 1000 94

<!-- b001513 | prose | pages [41] -->
pred = seq(input, future=future) 95

<!-- b001514 | prose | pages [41] -->
y = pred[:, seq_length:, :].detach().numpy() 96

<!-- b001515 | prose | pages [41] -->
torch.save(y, open(’{}/{}.pt’.format(output_path , product), ’wb’)) 97

<!-- b001516 | prose | pages [41] -->
C.5

<!-- b001517 | heading | pages [41] -->
Reputation Model

<!-- b001518 | prose | pages [41] -->
1 from __future__ import print_function

<!-- b001519 | prose | pages [41] -->
2

<!-- b001520 | prose | pages [41] -->
3 import time

<!-- b001521 | prose | pages [41] -->
4

<!-- b001522 | prose | pages [41] -->
5 import matplotlib

<!-- b001523 | prose | pages [41] -->
6 import matplotlib.pyplot as plt

<!-- b001524 | prose | pages [41] -->
7 import numpy as np

<!-- b001525 | prose | pages [41] -->
8

<!-- b001526 | prose | pages [41] -->
9 import torch

<!-- b001527 | prose | pages [41] -->
10 import torch.nn as nn

<!-- b001528 | prose | pages [41] -->
11 import torch.optim as optim

<!-- b001529 | prose | pages [41] -->
12 from utils import *

<!-- b001530 | prose | pages [41] -->
13

<!-- b001531 | prose | pages [41] -->
14 matplotlib.use(’Agg’)

<!-- b001532 | prose | pages [41] -->
15

<!-- b001533 | prose | pages [41] -->
16 default_path = ’3_LSTM/’

<!-- b001534 | prose | pages [41] -->
17 output_path = ’3_LSTM/batch_size_1’

<!-- b001535 | prose | pages [41] -->
18 products = [’hair_dryer’, ’microwave’, ’pacifier’]

<!-- b001536 | prose | pages [41] -->
19 features = [’star_rating’, ’helpful_votes’, ’total_votes’,

<!-- b001537 | prose | pages [41] -->
’vine’, ’verified_purchase’, ’review_date’] 20

<!-- b001538 | prose | pages [41] -->
21 batch_size = 1

<!-- b001539 | prose | pages [41] -->
22 num_feature = len(features)

<!-- b001540 | prose | pages [41] -->
23 hidden_size = 200

<!-- b001541 | prose | pages [41] -->
关注数学模型

<!-- b001542 | furniture | pages [41] -->
2

<!-- b001543 | furniture | pages [41] -->
MATHmodels

<!-- b001544 | furniture | pages [41] -->
获取更多资讯

<!-- b001545 | furniture | pages [42] -->
Team 2003717

<!-- b001546 | prose | pages [42] -->
24 train_loss = []

<!-- b001547 | prose | pages [42] -->
25 window_size = 500

<!-- b001548 | prose | pages [42] -->
26

<!-- b001549 | prose | pages [42] -->
27 if __name__ == ’__main__’:

<!-- b001550 | prose | pages [42] -->
np.random.seed(0) 28

<!-- b001551 | prose | pages [42] -->
torch.manual_seed(0) 29

<!-- b001552 | prose | pages [42] -->
30

<!-- b001553 | prose | pages [42] -->
for product in products: 31

<!-- b001554 | furniture | pages [42] -->
Page 41

<!-- b001555 | prose | pages [42] -->
row_data = torch.load(’{}/{}.pt’.format(default_path , product)) 32

<!-- b001556 | prose | pages [42] -->
original_seq_length = row_data.shape[1] 33

<!-- b001557 | prose | pages [42] -->
pred_data = torch.load(’{}/{}.pt’.format(output_path , product)) 34

<!-- b001558 | prose | pages [42] -->
pred_data = de_standardization(pred_data , row_data) 35

<!-- b001559 | prose | pages [42] -->
row_data = np.concatenate((row_data , row_data[:, int( 36

<!-- b001560 | prose | pages [42] -->
original_seq_length//1.1):int(original_seq_length//1), :]), axis=1) 37

<!-- b001561 | prose | pages [42] -->
row_data = np.concatenate((row_data , row_data[:, int( 38

<!-- b001562 | prose | pages [42] -->
original_seq_length//1.3):int(original_seq_length//1.2), :]), axis=1) 39

<!-- b001563 | prose | pages [42] -->
row_data = np.concatenate((row_data , row_data[:, int( 40

<!-- b001564 | prose | pages [42] -->
original_seq_length//1.2):int(original_seq_length//1), :]), axis=1) 41

<!-- b001565 | prose | pages [42] -->
row_data = np.concatenate((row_data , row_data[:, int( 42

<!-- b001566 | prose | pages [42] -->
original_seq_length//1.3):int(original_seq_length//1), :]), axis=1) 43

<!-- b001567 | prose | pages [42] -->
seq_length = row_data.shape[1] 44

<!-- b001568 | prose | pages [42] -->
reputation = [] 45

<!-- b001569 | prose | pages [42] -->
for i in range(seq_length - window_size): 46

<!-- b001570 | prose | pages [42] -->
rep = 0.0 47

<!-- b001571 | prose | pages [42] -->
for j in range(i, i + window_size): 48

<!-- b001572 | prose | pages [42] -->
help_rate = 0 if row_data[0, j, 49

<!-- b001573 | prose | pages [42] -->
50 2] 2] == 0 else row_data[0, j, 1]/row_data[0, j,

<!-- b001574 | prose | pages [42] -->
vine = 1 if row_data[0, j, 3] else 0 51

<!-- b001575 | prose | pages [42] -->
verified = 1 if row_data[0, j, 4] else 0 52

<!-- b001576 | prose | pages [42] -->
t = float(row_data[0, j, 5]) 53

<!-- b001577 | prose | pages [42] -->
rating = row_data[0, j, 0] 54

<!-- b001578 | prose | pages [42] -->
if j > original_seq_length: 55

<!-- b001579 | prose | pages [42] -->
if product == ’hair_dryer’: 56

<!-- b001580 | prose | pages [42] -->
help_rate += 0.2 57

<!-- b001581 | prose | pages [42] -->
vine -= 0.2 58

<!-- b001582 | prose | pages [42] -->
elif product == ’microwave’: 59

<!-- b001583 | prose | pages [42] -->
rating += 0.3 60

<!-- b001584 | prose | pages [42] -->
vine += 0.25 61

<!-- b001585 | prose | pages [42] -->
else: 62

<!-- b001586 | prose | pages [42] -->
vine -= 0.2 63

<!-- b001587 | prose | pages [42] -->
rating += 0.5 64

<!-- b001588 | prose | pages [42] -->
R = ((help_rate + 1) * (vine*0.2 + 0.8) * 65

<!-- b001589 | prose | pages [42] -->
(verified*0.2 + 0.8) * rating) / (t + 1) 66

<!-- b001590 | prose | pages [42] -->
rep += R 67

<!-- b001591 | prose | pages [42] -->
rep /= window_size 68

<!-- b001592 | prose | pages [42] -->
reputation.append(rep) 69

<!-- b001593 | prose | pages [42] -->
print(len(reputation)) 70

<!-- b001594 | prose | pages [42] -->
plt.title(’{}’.format(product)) 71

<!-- b001595 | prose | pages [42] -->
plt.plot(np.arange(original_seq_length - window_size), 72

<!-- b001596 | prose | pages [42] -->
reputation[:original_seq_length - window_size], linewidth=2.0) 73

<!-- b001597 | prose | pages [42] -->
plt.plot(np.arange(original_seq_length - window_size , len(reputation)), 74

<!-- b001598 | prose | pages [42] -->
reputation[original_seq_length - window_size:], linewidth=2.0, color=’ 75 red’)

<!-- b001599 | prose | pages [42] -->
plt.xlabel(’time step’) 76

<!-- b001600 | prose | pages [42] -->
plt.ylabel(’reputaion metric’) 77

<!-- b001601 | prose | pages [42] -->
plt.savefig(’{}.png’.format(product)) 78

<!-- b001602 | prose | pages [42] -->
plt.close() 79

<!-- b001603 | prose | pages [42] -->
关注数学模型

<!-- b001604 | furniture | pages [42] -->
2

<!-- b001605 | furniture | pages [42] -->
MATHmodels

<!-- b001606 | furniture | pages [42] -->
获取更多资讯
