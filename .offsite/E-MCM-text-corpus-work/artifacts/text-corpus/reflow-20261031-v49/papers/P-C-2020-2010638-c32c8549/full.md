# P-C-2020-2010638-c32c8549

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2020

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
C

<!-- b000005 | title | pages [1] -->
2010638

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Sales Strategy Recommendation Based on Commodity Data Mining

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
We conduct data analysis and information mining from the following four aspects: correlation between review, star rating and helpfulness rating, product brand rating, prediction of product’s reputation and impact of star rating on reviews, so as to propose reliable sales strategies and suggestions for product improvement.

<!-- b000010 | prose | pages [1] -->
Firstly, after data pre-processing, We perform word segmentation and preliminary sentiment analysis on the text data through the NLTK tool, and quantify it as emotion score, ranging from [-1,1].We adopt the methods of data visualization, descriptive statistics and correlation analysis, and further construct a multivariate Logistic regression model to analyze the relationship between helpfulness rating and review length, star rating and compound. The results show that helpfulness rating has an inverted "U-type" relationship with review length and a positive "U-type" relationship with star rating.

<!-- b000011 | prose | pages [1] -->
The next step, we conduct analysis based on the rating and evaluation model. The LDA analysis model is constructed to find the topic feature of each product, based on which we can propose suggestions for improvement of products. At the same time, we summarize five indexes that affect the product sales from the topic features, namely quality, price, appearance, service and size. Then a computer search algorithm based on the text similarity is used to calculate the index score of each review. In addition, we combine the score with the analytic hierarchy process to determine the weight of each index and build a weighted brand scoring system. Finally, we cluster all product brands through systematic clustering to select potential high-quality brands and recommend them to sunshine company.

<!-- b000012 | prose | pages [1] -->
Further, we calculate the comprehensive score of review and star rating, and take it as the product’s reputation, which is conducive to forecast the future reputation of three products through time series analysis. And it depicts that the three products have seasonal characteristics and will probably maintain a stable seasonal cycle in the near future. However, the peak time of reputation comprehensive score of the three products is discrepant, and further analysis illustrates that the product sales figure is larger during the peak period of reputation score, according to which sunshine company can make a sales plan.

<!-- b000013 | prose | pages [1] -->
Finally, we analyze the relationship between star rating and review. Through the establishment of distributed lag model, it is found that customers' reviews in the current period will be affected by other customers' ratings and reviews. Meanwhile, we observe the time-varying synchrony between emotional score and star rating, which is clear that reviews containing positive words result in higher star ratings, while reviews containing negative words result in lower star ratings. In other words, there is a strong correlation between star ratings and specific quality descriptors.

<!-- b000014 | keywords | pages [1] -->
Key words: correlation analysis, multinomial logistic regression, natural language processing,

<!-- b000015 | prose | pages [1] -->
time series analysis

<!-- b000016 | prose | pages [1] -->
关注数学模型

<!-- b000017 | furniture | pages [1] -->
2

<!-- b000018 | furniture | pages [1] -->
MATHmodels

<!-- b000019 | furniture | pages [1] -->
获取更多资讯

<!-- b000020 | furniture | pages [2] -->
Team # 2010638                                                                   Page 1 of 20

<!-- b000021 | heading | pages [2] -->
Content

<!-- b000022 | contents | pages [2] -->
1. INTRODUCTION ......................................................................................................................................... 2

<!-- b000023 | contents | pages [2] -->
1.1 Background ............................................................................................................................................... 2

<!-- b000024 | contents | pages [2] -->
1.2 Problems Restatement ............................................................................................................................... 2

<!-- b000025 | contents | pages [2] -->
2. ASSUMPTIONS AND NOMENCLATURE .............................................................................................. 3

<!-- b000026 | contents | pages [2] -->
2.1

<!-- b000027 | contents | pages [2] -->
Assumptions ........................................................................................................................................ 3

<!-- b000028 | contents | pages [2] -->
2.2

<!-- b000029 | contents | pages [2] -->
Nomenclature ....................................................................................................................................... 3

<!-- b000030 | contents | pages [2] -->
3.

<!-- b000031 | contents | pages [2] -->
MODEL 1-ANALYSIS OF STAR RATING, HELPFULNESS RATING AND REVIEW .................. 4

<!-- b000032 | contents | pages [2] -->
3.1 Data Pre-processing .................................................................................................................................. 4

<!-- b000033 | contents | pages [2] -->
3.2 Word Segmentation and Sentiment Analysis ............................................................................................ 5

<!-- b000034 | contents | pages [2] -->
3.3 Data Description and Visual Analysis ....................................................................................................... 6

<!-- b000035 | contents | pages [2] -->
3.4 Correlation Analysis ................................................................................................................................. 7

<!-- b000036 | contents | pages [2] -->
3.5 Multinomial Logistic Regression Model .................................................................................................. 7

<!-- b000037 | contents | pages [2] -->
4.

<!-- b000038 | contents | pages [2] -->
MODEL 2-ESTABLISH A SCORING SYSTEM TO DETERMINE PRODUCT POSITIONING ... 9

<!-- b000039 | contents | pages [2] -->
4.1 LDA Model ............................................................................................................................................... 9

<!-- b000040 | contents | pages [2] -->
4.2 Determine index score ............................................................................................................................. 11

<!-- b000041 | contents | pages [2] -->
4.3 Analytic hierarchy process (AHP) .......................................................................................................... 12

<!-- b000042 | contents | pages [2] -->
4.3.1 The introduction of analytic hierarchy process .............................................................. 12

<!-- b000043 | contents | pages [2] -->
4.3.2 AHP Consistency Test .................................................................................................... 13

<!-- b000044 | contents | pages [2] -->
4.3.3 Results of AHP ............................................................................................................... 13

<!-- b000045 | contents | pages [2] -->
4.4 System Clustering Analysis ..................................................................................................................... 14

<!-- b000046 | contents | pages [2] -->
4.4.1 Model establishment ....................................................................................................... 14

<!-- b000047 | contents | pages [2] -->
4.4.2 Classification results ....................................................................................................... 14

<!-- b000048 | contents | pages [2] -->
5.

<!-- b000049 | contents | pages [2] -->
MODEL 3-TIME SERIES ANALYSIS .................................................................................................. 15

<!-- b000050 | contents | pages [2] -->
6.

<!-- b000051 | contents | pages [2] -->
MODEL 4-DISTRIBUTED LAG MODEL ........................................................................................... 17

<!-- b000052 | contents | pages [2] -->
6.1 Distributed lag model .............................................................................................................................. 17

<!-- b000053 | contents | pages [2] -->
6.2 Almon Method ........................................................................................................................................ 18

<!-- b000054 | contents | pages [2] -->
6.3 Correlation Analysis between Star Rating and Comments ..................................................................... 18

<!-- b000055 | contents | pages [2] -->
7.

<!-- b000056 | contents | pages [2] -->
SENSITIVITY ANALYSIS ..................................................................................................................... 19

<!-- b000057 | contents | pages [2] -->
8.

<!-- b000058 | contents | pages [2] -->
MODEL ASSESSMENT ......................................................................................................................... 20

<!-- b000059 | contents | pages [2] -->
8.1 Strengths ................................................................................................................................................. 20

<!-- b000060 | contents | pages [2] -->
8.2 Weaknesses ............................................................................................................................................. 20

<!-- b000061 | contents | pages [2] -->
REFERENCE .................................................................................................................................................. 20

<!-- b000062 | contents | pages [2] -->
LETTER ............................................................................................................................................................. 1

<!-- b000063 | contents | pages [2] -->
APPENDIX ........................................................................................................................................................ 1

<!-- b000064 | contents | pages [2] -->
关注数学模型

<!-- b000065 | furniture | pages [2] -->
2

<!-- b000066 | furniture | pages [2] -->
MATHmodels

<!-- b000067 | furniture | pages [2] -->
获取更多资讯

<!-- b000068 | furniture | pages [3] -->
Team # 2010638                                                                   Page 2 of 20

<!-- b000069 | heading | pages [3] -->
1. Introduction

<!-- b000070 | heading | pages [3] -->
1.1 Background

<!-- b000071 | prose | pages [3] -->
With the popularization and development of the Internet, online sales are gradually replacing offline sales and occupy a major position in the sales industry. The transformation of sales mode will also be a huge challenge for commodity companies. Analyzing and mining market information and consumer feedback has become the key of network marketing.

<!-- b000072 | prose | pages [3] -->
The online marketplace created by Amazon provides an opportunity for customers to evaluate their purchases. Customers can use quantities from 1 (low rating, low satisfaction) to 5 (high rating, high satisfaction) to express their satisfaction with the product. In addition, customers can submit their own reviews on the products to express their opinions. Other customers can use these reviews to gain an initial understanding of the product before purchasing it, and to distinguish between the reviews (called "helpfulness ratings") that are helpful or not. The data will be fed back to the company which can use the data to conduct in-depth analysis of the markets, determine the timing of their participation, and modify products based on customer suggestions.

<!-- b000073 | heading | pages [3] -->
1.2 Problems Restatement

<!-- b000074 | prose | pages [3] -->
Sunshine Company plans to launch and sell microwave ovens, hair dryers and baby pacifiers in the online marketplace. In order to understand these three commodity markets and develop sales strategies, it is necessary to analyze the customer feedback data. We will accomplish the following tasks according to the given data:

<!-- b000075 | prose | pages [3] -->
(1) Develop sales strategy for sunshine company.

<!-- b000076 | prose | pages [3] -->
(2) Identify potential important design features that would enhance product desirability.

<!-- b000077 | prose | pages [3] -->
In order to accomplish the above two tasks, our specific work is as follows:

<!-- b000078 | prose | pages [3] -->
 Analyze the relationship between star rating, helpful vote and review.

<!-- b000079 | prose | pages [3] -->
 Make in-depth analysis of reviews and ratings, and distinguish the advantages and disadvantages of products, so as to make suggestions for product improvement.

<!-- b000080 | prose | pages [3] -->
 Establish a product rating system based on the analysis of reviews and ratings, and select high-quality brand products to recommend to Sunshine Company for sales.

<!-- b000081 | prose | pages [3] -->
 Establish the reputation scoring system and predict the development trend of reputation.

<!-- b000082 | prose | pages [3] -->
 Analyze whether current reviews are influenced by prior star ratings and reviews.

<!-- b000083 | prose | pages [3] -->
 Analyze whether specific quality descriptors of text-based reviews strongly associated with rating levels.

<!-- b000084 | prose | pages [3] -->
关注数学模型

<!-- b000085 | furniture | pages [3] -->
2

<!-- b000086 | furniture | pages [3] -->
MATHmodels

<!-- b000087 | furniture | pages [3] -->
获取更多资讯

<!-- b000088 | furniture | pages [4] -->
Team # 2010638                                                                   Page 3 of 20

<!-- b000089 | caption | pages [4] -->
Figure 1: The Flow Chart in This Paper

<!-- b000090 | heading | pages [4] -->
2. Assumptions and Nomenclature

<!-- b000091 | heading | pages [4] -->
2.1 Assumptions

<!-- b000092 | prose | pages [4] -->
We make several assumptions in our model. Later we may relax some of these assumptions to optimize our model making it more applicable in the complex reality environment.

<!-- b000093 | prose | pages [4] -->
 All reviews are from customers and there is no automated review.

<!-- b000094 | prose | pages [4] -->
 There is no deliberate attempt to smear the product in customer rating and review.

<!-- b000095 | prose | pages [4] -->
 Unverified orders are not sold on Amazon. The sum of confirmed sales in the data set is total sales.

<!-- b000096 | prose | pages [4] -->
 The review of members certified by Amazon Vine has high credibility.

<!-- b000097 | heading | pages [4] -->
2.2 Nomenclature

<!-- b000098 | heading | pages [4] -->
Symbols

<!-- b000099 | prose | pages [4] -->
Definition

<!-- b000100 | prose | pages [4] -->
SS Star ratings squared

<!-- b000101 | prose | pages [4] -->
The number of words in each review. count

<!-- b000102 | prose | pages [4] -->
CS The number of words squared

<!-- b000103 | prose | pages [4] -->
compound Emotional score The percentage of helpful votes in the total votes. H r The weight of the thi index iw Total score of six indexes(quality、size、service、 SQ price、appearance、star ratings) Total score of product reputation SR

<!-- b000104 | prose | pages [4] -->
关注数学模型

<!-- b000105 | furniture | pages [4] -->
2

<!-- b000106 | furniture | pages [4] -->
MATHmodels

<!-- b000107 | furniture | pages [4] -->
获取更多资讯

<!-- b000108 | furniture | pages [5] -->
Team # 2010638                                                                   Page 4 of 20

<!-- b000109 | heading | pages [5] -->
3.  Model 1-Analysis of Star rating, Helpfulness rating and Review

<!-- b000110 | heading | pages [5] -->
3.1 Data Pre-processing

<!-- b000111 | prose | pages [5] -->
Before data analysis, the availability of data must be guaranteed. No measures, regardless of its value, can provide accurate assessments if based on unreliable data. We first remove useless information including product title, marketplace and product category, on the basis of which we can carry out data pre-processing.

<!-- b000112 | prose | pages [5] -->
To ameliorate the condition of data set, there are four steps: data classification, data cleaning, information filtration, set-up of new attribute and data-measuring, as shown in the figure.

<!-- b000113 | caption | pages [5] -->
Figure 2: Data Pre-processing Flow Chart

<!-- b000114 | prose | pages [5] -->
Step 1: Firstly, divide the data into numeric and textual types and process them separately.

<!-- b000115 | prose | pages [5] -->
Step 2: In the stage of data cleaning, initially we check the missing value by using the “duplicated () method” in python, while no item with a missing value was found.

<!-- b000116 | prose | pages [5] -->
Step 3: Outlier processing is mainly used in the text data. Take the pacifier as an example, it includes the following contents:

<!-- b000117 | prose | pages [5] -->
，❤，  Processing non-alphabetic text data. There are some non-alphabetic data like: ,They ，

<!-- b000118 | prose | pages [5] -->
can't be recognized by a computer program, while their emotional inclination can be intuitively identified by us. As a result, we transform all of them into "five stars”, so as to facilitate the later computer programming.

<!-- b000119 | prose | pages [5] -->
 Spelling correction. Generally, English text may contain spelling errors, so a spelling check is required. Based on “PyEnchant library” in python program, all the review texts are checked and corrected.

<!-- b000120 | prose | pages [5] -->
 Lowercase: the computer will react differently to the two texts: “Five stars” and “five stars”, whereas we expect them to be the same word when we count them. Therefore, we unify all text data to lowercase characters.

<!-- b000121 | prose | pages [5] -->
Step 4: After the above steps, our data set has become more acceptable, but when we look more closely at the review content, we find that a lot of the review content is irrelevant to the product and can be regarded as redundant information, such as:

<!-- b000122 | prose | pages [5, 6] -->
关注数学模型  “good cleaning cloths”  “I bought hits basket to store magazines and newspapers. It looks very nice in our room”  “I received this blanket as a gift from my mom and have never felt anything so soft.”

<!-- b000123 | furniture | pages [5] -->
2

<!-- b000124 | furniture | pages [5] -->
MATHmodels

<!-- b000125 | furniture | pages [5] -->
获取更多资讯

<!-- b000126 | furniture | pages [6] -->
Team # 2010638                                                                   Page 5 of 20

<!-- b000128 | prose | pages [6] -->
Take the pacifier as an example, reviews that have nothing to do with the pacifier is needed to be weeded out. We identify the redundant information according to the text similarity, and the process is as follows:

<!-- b000129 | prose | pages [6] -->
The product review is regarded as a set of words, and the feature vector of the text is established by calculating the number of each word in the text. Afterwards, the cosine similarity between vectors is used to calculate the similarity between texts. If the average similarity between a review and others is less than the threshold value set by us, the review is removed.

<!-- b000130 | prose | pages [6] -->
Step 5:Set-up of new attribute. To better analyze the usefulness of reviews, we establish a new attribute named helpfulness rating (Hr), which is obtained by dividing “helpful votes” by “total votes”

<!-- b000131 | heading | pages [6] -->
3.2 Word Segmentation and Sentiment Analysis

<!-- b000132 | prose | pages [6] -->
Although the text data has been initially processed aforementioned, the information from reviews is s till needed to assess.However, the review data is unstructured and requires a different mechanism to ex tract the information. Emotion analysis or opinion mining is the process of computing to identify wh ether the author's attitude towards a text is positive, negative or neutral. For the review data, we con ducted a preliminary Sentiment analysis through data mining to determine and quantify the emotional inclination of each review, and further analysis will be discussed in the following questions. Based on this, NLTK (natural language toolkit),which is a leading platform that is able to work with human langu age data by python program, is used for sentiment analysis.

<!-- b000133 | prose | pages [6] -->
A basic sentiment analysis model is built in Python 3 using the NLTK library. The preprocessin g is operated by marking the text, normalizing the words, and removing the noise. Next, the NTLK emotional analyzer is used to build a model and associate the text with a specific emotion and quant ify it.

<!-- b000134 | caption | pages [6] -->
Figure 3: Implementation process

<!-- b000135 | prose | pages [6] -->
关注数学模型

<!-- b000136 | furniture | pages [6] -->
2

<!-- b000137 | furniture | pages [6] -->
MATHmodels

<!-- b000138 | furniture | pages [6] -->
获取更多资讯

<!-- b000139 | furniture | pages [7] -->
Team # 2010638                                                                   Page 6 of 20

<!-- b000140 | heading | pages [7] -->
3.3 Data Description and Visual Analysis

<!-- b000141 | prose | pages [7] -->
The table below describes the total, average and variance of the star rating of these three products. The average of the helpful votes and the number of the words in the review are also calculated. The figures below describe their distribution.

<!-- b000142 | caption | pages [7] -->
Table 1: Data Statistic

<!-- b000143 | prose | pages [7] -->
Descriptive Star rating Star rating Helpful votes Count Total Count statistics average variance average average Pacifier 18939 4.30456 1.19043 0.827182 4841870 256 Microwave oven 1615 3.44458 1.64524 5.62167 748130 463 Hair dryer 11470 4.11604 1.30033 2.17908 3268716 285

<!-- b000144 | caption | pages [7] -->
Figure 4: Box Figure        Figure 5: Stacked Barplot     Figure 6:Star Rating Distributon

<!-- b000145 | prose | pages [7] -->
The data is visualized to dig into the inherent rules, which is helpful for modeling.

<!-- b000146 | prose | pages [7] -->
The figures below describe the relationship between the helpfulness rating, and star ratings, review length and emotional score.

<!-- b000147 | caption | pages [7] -->
Figure 7:Heat Map of Correlation

<!-- b000148 | prose | pages [7] -->
Note: sr represents “star rating”; cp represents “compound”; ct represents “count”; hr represents “helpfulness rating”

<!-- b000149 | prose | pages [7] -->
The darker the color in the figure is, the greater the correlation between the two indicators will be. We can find that the emotional score and star ratings has a strong correlation in the three figures. The helpfulness rating and the review length has a light correlation.

<!-- b000150 | prose | pages [7] -->
关注数学模型

<!-- b000151 | furniture | pages [7] -->
2

<!-- b000152 | furniture | pages [7] -->
MATHmodels

<!-- b000153 | furniture | pages [7] -->
获取更多资讯

<!-- b000154 | furniture | pages [8] -->
Team # 2010638                                                                   Page 7 of 20

<!-- b000155 | heading | pages [8] -->
3.4 Correlation Analysis

<!-- b000156 | prose | pages [8] -->
H ), star ratings, the We apply the methods of correlation analysis on the percentage of helpful votes ( r number of words in each review (count) and emotional score (compound)., which is measured by Pearson correlation coefficient is as follows:

<!-- b000157 | prose | pages [8] -->
n    (X X)(Y Y) i i   i 1 r (1) n n     2 2 ( X X ) ( Y Y ) i i   i 1 i 1

<!-- b000158 | prose | pages [8] -->
X represents the star rating, review length, emotional score, etc. iY represents the helpfulness rating,. X , i H and star Y represents the average number of these indexes. The r is the correlation coefficient between r rating, count, compound, etc.

<!-- b000159 | prose | pages [8] -->
The results of the correlation analysis are

<!-- b000160 | caption | pages [8] -->
Table 2: Correlation Coefficient

<!-- b000161 | prose | pages [8] -->
Correlation Correlation coefficient(Hair Correlation Index coefficient(Microwave dryer) coefficient(Pacifier) oven) star rating -0.149** -0.138** -0.151** count -0.071** 0.356** 0.332** compound -0.024** 0.057** -0.101** Note: ** means the result is significant at 0.01 level (two-side test) From the table above we can see that, for the three data sets, there is a significant correlation between H and star rating, count and compound (all of which are significant in the two-tailed test), which is r consistent with the results of visual analysis. More concretely, the star rating and emotional score of H . The counts of hair dryer and microwave oven, hair dryer and pacifier are negatively correlated with r H , while the counts of microwave oven are negatively correlated with pacifier are positively correlated with r H . Besides, there is a negative correlation between the compound of microwave oven, pacifier and H , r r H is positive. while the correlation between the compound of hair dryer and r

<!-- b000162 | heading | pages [8] -->
3.5 Multinomial Logistic Regression Model

<!-- b000163 | prose | pages [8] -->
Multinomial logistic regression model is adopted to further analyze the impact of star rating, review length and emotional score on the helpfulness rating. In fact, the helpfulness rating is the cumulative result of each consumer’s voting (yes or no) . Therefore, the number of helpful votes is subject to binomial distribution, and logistic model is suitable for empirical analysis of such kind of data.

<!-- b000164 | prose | pages [8] -->
X in Multivariate logistic regression can determine the role and intensity of the explanatory variable n predicting the probability of occurrence of strain Y. Suppose X is the response variable and P is the response probability of the model, and the corresponding regression model is as follows:

<!-- b000165 | prose | pages [8] -->
p k      1 ln( ) x (2) k ki  1 p  k 1 1

<!-- b000166 | prose | pages [8] -->
  x ,x , ,x p P (y 1| x ,x , ,x ) is the possibility that case i happens in case the values of are 1 i 1 i 2 i ki 1 i 2 i ki 1p is a binomial distribution parameter, which is the probability that a review receives a helpful given. Also x represents a series of independent variables. β is the corresponding estimation coefficient, and α is vote. ki the intercept, which reflects the random effect at the product level.

<!-- b000167 | prose | pages [8, 9] -->
关注数学模型 The probability of an event happening of an event is a non-linear function composed of the explanatory variable Xi . Here is the expression:

<!-- b000168 | furniture | pages [8] -->
2

<!-- b000169 | furniture | pages [8] -->
MATHmodels

<!-- b000170 | furniture | pages [8] -->
获取更多资讯

<!-- b000171 | furniture | pages [9] -->
Team # 2010638                                                                   Page 8 of 20

<!-- b000173 | prose | pages [9] -->
        exp(

<!-- b000174 | heading | pages [9] -->
X X

<!-- b000175 | prose | pages [9] -->
... X )  1 1 2 2 n n p (3)         1 exp(

<!-- b000176 | heading | pages [9] -->
X X

<!-- b000177 | prose | pages [9] -->
... X ) 1 1 2 2 n n

<!-- b000178 | prose | pages [9] -->
On top of these 3 indexes, we introduce two additional variables: star rating square(SQ) and review length square(CS) in order to further explore the influence of star rating and review length on the helpfulness ratings of reviews.

<!-- b000179 | prose | pages [9] -->
Meanwhile, considering the impact of whether the customers are vine members and whether the purchase is verified on the authenticity and validity of reviews, we take these two indicators as independent variables.

<!-- b000180 | prose | pages [9] -->
Independent variables are divided into three levels, which represent the intuitive evaluation (star rating, star rating square) respectively, characteristics of review content (review length, review length square, emotional score), and reviewers characteristics (vine, VP), to explore the various reasons that affect the helpfulness ratings in detail.

<!-- b000181 | prose | pages [9] -->
As for dependent variables, we divide them into four categories according to their numerical values, namely:

<!-- b000182 | prose | pages [9] -->
   1,0.75 compound 1    2,0.50 compound 0.75   helpfulness ratings (4)   3,0.25 compound 0.50     4,0 compound 0.25 

<!-- b000183 | prose | pages [9] -->
The independent variables are divided into blocks and do regression analysis respectively. The independent variables in models 1, 2 and 3 and the regression coefficients obtained by SPSS are summarized as Table.For reasons of space, the results of hair dryer and pacifier are included in the appendix.

<!-- b000184 | prose | pages [9] -->
independent Abbreviations

<!-- b000185 | heading | pages [9] -->
Model 1

<!-- b000186 | heading | pages [9] -->
Model 2

<!-- b000187 | heading | pages [9] -->
Model 3

<!-- b000188 | prose | pages [9] -->
variables star rating star rating 0.213** 0.469** 0.423** Intuitive star rating SS 0.314** 0.207** 0.110** evaluation square review length count -0.020** -0.019** review length Characteristics CS 0.002** 0.002** square of review emotional

<!-- b000189 | heading | pages [9] -->
content

<!-- b000190 | contents | pages [9] -->
compound

<!-- b000191 | contents | pages [9] -->
-0.146**

<!-- b000192 | contents | pages [9] -->
-0.160**

<!-- b000193 | contents | pages [9] -->
score

<!-- b000194 | contents | pages [9] -->
vine

<!-- b000195 | contents | pages [9] -->
vine

<!-- b000196 | contents | pages [9] -->
0.033**

<!-- b000197 | contents | pages [9] -->
Reviewers’

<!-- b000198 | contents | pages [9] -->
verified

<!-- b000199 | contents | pages [9] -->
verified

<!-- b000200 | contents | pages [9] -->
0.398**

<!-- b000201 | contents | pages [9] -->
characteristics

<!-- b000202 | contents | pages [9] -->
purchase

<!-- b000203 | contents | pages [9] -->
purchase

<!-- b000204 | caption | pages [9] -->
Table 3: Index and regression coefficient

<!-- b000205 | contents | pages [9] -->
Note:*: p<0.05; **: p<0.01; +: p<0.1; ns: not significant

<!-- b000206 | contents | pages [9] -->
It is clear from the above table, each variable passed the significance test. The regression coefficients of

<!-- b000207 | contents | pages [9] -->
star ratings of microwave oven, hair dryer and pacifier are all positive, and the regression coefficients of star

<!-- b000208 | contents | pages [9] -->
rating square terms are also positive. It indicates that there is a "U-type” relationship between star ratings and

<!-- b000209 | contents | pages [9] -->
关注数学模型

<!-- b000210 | furniture | pages [9] -->
2

<!-- b000211 | furniture | pages [9] -->
MATHmodels

<!-- b000212 | furniture | pages [9] -->
获取更多资讯

<!-- b000213 | furniture | pages [10] -->
Team # 2010638                                                                   Page 9 of 20

<!-- b000214 | contents | pages [10] -->
the helpfulness ratings of reviews, which is contrary to the research conclusions of Mudambi and Schuff [8].

<!-- b000215 | contents | pages [10] -->
Our analysis suggests that the reviewers who score higher or lower star ratings may be more willing to express

<!-- b000216 | contents | pages [10] -->
a clear attitude towards the products, so as to provide more valuable reviews; while the reviewers who give

<!-- b000217 | contents | pages [10] -->
intermediate star ratings may lack reference value due to their less distinctive attitude.

<!-- b000218 | contents | pages [10] -->
Based on model 1, review length, review length square and emotion score are added into the model.

<!-- b000219 | contents | pages [10] -->
From the data in the table, it is clear that the regression coefficient of the review length term is negative, while

<!-- b000220 | contents | pages [10] -->
one of the square term of the review length is positive, which indicates that the review length and helpfulness

<!-- b000221 | contents | pages [10] -->
rating are of an inverted-U-type. According to our analysis, reviews that are too short are often limited in

<!-- b000222 | contents | pages [10] -->
content and cannot provide sufficient useful information. However, overlong reviews may provide a lot of

<!-- b000223 | contents | pages [10] -->
valuable information though, other customers may not be patient to spend time and energy reading them.

<!-- b000224 | contents | pages [10] -->
Therefore, reviews with high helpfulness ratings should be of moderate length.

<!-- b000225 | contents | pages [10] -->
On the basis of model 2, in model 3 we introduce other reviewer-related features such as Vine and

<!-- b000226 | contents | pages [10] -->
Verified Purchase. It can be seen that most customers are not vine members and many purchase are not

<!-- b000227 | contents | pages [10] -->
verified in the sample data, thus it is difficult to analyze and draw valuable conclusions about these two

<!-- b000228 | contents | pages [10] -->
indicators. In spite of this, they make the model more complete and more applicable.

<!-- b000229 | heading | pages [10] -->
4.  Model 2-Establish a Scoring System to Determine Product

<!-- b000230 | prose | pages [10] -->
Positioning

<!-- b000231 | prose | pages [10] -->
According to the three data sets, each product has hundreds of different brands. If sunshine company hopes to enter the market of microwave oven, hair dryer and pacifier, it is of great significance to accurately grasp the market positioning of each brand. The market positioning of different brands is mainly determined by the star rating and review from customers. The processing of star rating is relatively simple, so we mainly process text of customers’ reviews in detail.

<!-- b000232 | heading | pages [10] -->
4.1 LDA Model

<!-- b000233 | prose | pages [10] -->
Latent Dirichlet Allocation is a generative thematic model proposed by Blei et al [2] in 2003. It is also known as three-tier Bayesian probability model with three-tier structure of document (d), topic (z) and word (W), which can effectively model the text. Based on LDA topic model, we are able to mine the potential topics in the data set, and then analyze the main information of the data sets and related feature words.

<!-- b000234 | caption | pages [10] -->
Table 4:Symbol Explanation

<!-- b000235 | prose | pages [10] -->
prior parameters of the Dirichlet function ，

<!-- b000236 | prose | pages [10] -->
the parameter of the topic's multiple ， distribution in the document.

<!-- b000237 | prose | pages [10] -->
LDA model assumes that each review is randomly mixed by each subject according to a certain proportion. And the mixing proportion is subject to multiple distribution, which is recorded as follows:

<!-- b000238 | prose | pages [10] -->
                   (5) Z | = Multionmial ( )

<!-- b000239 | prose | pages [10, 11] -->
关注数学模型 Each topic is made up of the words in the glossary in a certain proportion, and the proportion of the mixture is also subject to multiple distribution.

<!-- b000240 | furniture | pages [10] -->
2

<!-- b000241 | furniture | pages [10] -->
MATHmodels

<!-- b000242 | furniture | pages [10] -->
获取更多资讯

<!-- b000243 | furniture | pages [11] -->
Team # 2010638                                                                   Page 10 of 20

<!-- b000245 | prose | pages [11] -->
   (6) W Z | , Multionmial ( )

<!-- b000246 | prose | pages [11] -->
d , the probability of generating word iw is expressed as: Under the condition of review j

<!-- b000247 | prose | pages [11] -->
K      (7) P w ( | d ) P w ( | z s ) P z ( s d | ) j j i j  i 1   P w z ( | s ) iw belongs to the th is the probability that the word s topic. indicates P z ( s d | ) i j th the probability that the s topic is in the review.

<!-- b000248 | prose | pages [11] -->
After sentiment analysis based on LDA , the review text is gathered into three topics, as a result 10 most frequently used words and their corresponding probability are generated under each topic. Table 5 shows the potential topics in the positive evaluation text of microwave ovens, and the other one depicts the negative evaluation. Considering the limited space of the article, we put the results of hair dryer and pacifier in the appendix.

<!-- b000249 | caption | pages [11] -->
Table 5:Microwave Oven Positive Topics

<!-- b000250 | prose | pages [11] -->
Theme 1 Theme 2 Theme 3 Theme 1 Theme 2 Theme 3 great good well product product small well great great space no nice like well good price price easy good use use use nice product no small size like like like

<!-- b000251 | caption | pages [11] -->
Table 6:Microwave Oven Negative Topics

<!-- b000252 | prose | pages [11] -->
Theme 1 Theme 2 Theme 3 Theme 1 Theme 2 Theme 3 new no like time time no use use new more service old easy like use product great more no more service model small small like new time service good well According to the extraction of three potential subject words for positive and negative evaluation, we can determine the customer's attitudes towards 5 aspects of microwave oven characteristics.

<!-- b000253 | caption | pages [11] -->
Figure 8:Index of Microwave Oven                   Figure 9:Word Cloud

<!-- b000254 | prose | pages [11, 12] -->
关注数学模型 These high-frequency words in reviews can also reflect the focus of customers when purchasing microwave ovens, that is the quality, price, size, service and appearance. These five indicators can reflect a product comprehensively. We conduct the same analysis on pacifiers and hair dryers, then it is found that these five indicators can also be taken as the criteria to consider whether they are worth purchasing.

<!-- b000255 | furniture | pages [11] -->
2

<!-- b000256 | furniture | pages [11] -->
MATHmodels

<!-- b000257 | furniture | pages [11] -->
获取更多资讯

<!-- b000258 | furniture | pages [12] -->
Team # 2010638                                                                   Page 11 of 20

<!-- b000260 | prose | pages [12] -->
Taking the quality, price, size, service, appearance and star rating as the evaluation indexes, we establish a scoring system to comprehensively evaluate these 3 product sold in the current market, so as to obtain the accurate market positioning of each brand of products, and then formulate a good sales strategy for sunshine company.

<!-- b000261 | prose | pages [12] -->
The steps of our brand scoring system are as below:

<!-- b000262 | prose | pages [12] -->
• Determine the quality, price, size, service, appearance and star rating of each parent Step1

<!-- b000263 | prose | pages [12] -->
• The weights of quality, price, size, service, appearance and star rating in comprehensive Step2 evaluation are obtained by AHP

<!-- b000264 | prose | pages [12] -->
• The final score of each index is the weights mentioned above multiplied by the scores Step3

<!-- b000265 | prose | pages [12] -->
• According to the scores of each index, use Q- cluster to grade the parent Step4

<!-- b000266 | heading | pages [12] -->
4.2 Determine index score

<!-- b000267 | prose | pages [12] -->
After implementing LDA algorithm, complex network is introduced to calculate the importance degree of each review. We use traversing search algorithm to implement the process, through which we can get weighted average score of each topic feature for all products. Here is the algorithm:

<!-- b000268 | prose | pages [12] -->
关注数学模型

<!-- b000269 | furniture | pages [12] -->
2

<!-- b000270 | furniture | pages [12] -->
MATHmodels

<!-- b000271 | furniture | pages [12] -->
获取更多资讯

<!-- b000272 | furniture | pages [13] -->
Team # 2010638                                                                   Page 12 of 20

<!-- b000273 | heading | pages [13] -->
4.3 Analytic hierarchy process (AHP)

<!-- b000274 | heading | pages [13] -->
4.3.1 The introduction of analytic hierarchy process

<!-- b000275 | prose | pages [13] -->
Analytic hierarchy process (AHP) can be used deeply analyze the essence, influencing factors and their internal relations of complex decision problems. It makes use of less quantitative information to make the thinking process of decision mathematical, so as to provide a simple method for complex decision problems. AHP can decompose the evaluation criteria into different hierarchical structures, and then calculate the weight of each factor by solving the eigenvectors of judgment matrix.

<!-- b000276 | prose | pages [13] -->
According to the LDA model, the indicators we extracted are quality, appearance, price, size and service satisfaction level. Now we construct the judgment matrix of the first-level evaluation index:

<!-- b000277 | prose | pages [13] -->
  W W W W W W 1 1 1 1 1 1   W W W W W W   1 2 3 4 5 6   W W W W W W 2 2 2 2 2 2   W W W W W W   1 2 3 4 5 6   W W W W W W 3 3 3 3 3 3   W W W W W W   1 2 3 4 5 6  (8) A  W W W W W W 4 4 4 4 4 4   W W W W W W   1 2 3 4 5 6   W W W W W W  5 5 5 5 5 5  W W W W W W   1 2 3 4 5 6   W W W W W W   6 6 6 6 6 6   W W W W W W   1 2 3 4 5 7 Calculate the product of the elements:

<!-- b000278 | prose | pages [13] -->
  n M a ( i 1,2,3,4,5,6) (9)  i i 1 ij

<!-- b000279 | prose | pages [13] -->
M : Take the NTH root of i  W M (10) n i i

<!-- b000280 | prose | pages [13] -->
Calculate the eigenvector:

<!-- b000281 | prose | pages [13] -->
W  i W i n （11）  W j  j 1 Calculate the maximum eigenvalue：

<!-- b000282 | prose | pages [13] -->
( AW ) 1 n   i （12） max n W  i 1 i

<!-- b000283 | prose | pages [13] -->
  T W = W W W W W W Where 1 2 3 4 5 6

<!-- b000284 | prose | pages [13] -->
关注数学模型

<!-- b000285 | furniture | pages [13] -->
2

<!-- b000286 | furniture | pages [13] -->
MATHmodels

<!-- b000287 | furniture | pages [13] -->
获取更多资讯

<!-- b000288 | furniture | pages [14] -->
Team # 2010638                                                                   Page 13 of 20

<!-- b000289 | heading | pages [14] -->
4.3.2 AHP Consistency Test

<!-- b000290 | prose | pages [14] -->
After the judgment matrix is constructed, the relative weight of each element in two levels is calculated by the judgment matrix, and the consistency test is carried out. It is not allowed for the judgment to deviate too much from the consistency, so the consistency test of the judgment matrix is needed. The specific test steps are as follows:

<!-- b000291 | prose | pages [14] -->
Step1: Calculated consistency indexCI :

<!-- b000292 | prose | pages [14] -->
  n  max CI (13)  n 1 Step2:Check the criteria for testing the consistency of the judgement matrix from the relevant data

<!-- b000293 | prose | pages [14] -->
RI (n )

<!-- b000294 | caption | pages [14] -->
Table 7: Relation Between RI and n

<!-- b000295 | prose | pages [14] -->
n 1 2 3 4 5 6 7 8 9 RI 0 0 0.52 0.89 1.12 1.26 1.36 1.41 1.46 Note: if the consistency ratio is less than 0.1, the judgment matrix of AHP has satisfactory consistency Step3:Calculate the random consistency ratio of the judgment matrixCR ： CI CR  1                       (14) RI If the consistency ratio is less than 0.1, the judgement matrix of AHP has satisfactory consistency, namely its consistency degree is acceptable.

<!-- b000296 | heading | pages [14] -->
4.3.3 Results of AHP

<!-- b000297 | prose | pages [14] -->
After the sentiment analysis based on LDA , we screened out 5 indexes with significant influence, and combined with the star ratings, there were 6 evaluation indexes. The judgment matrix of each index is given by the expert scoring method to reflect its relative critical degree. According to the result of data processing, the judgment matrix of these indexes has passed the consistency test, which is shown in the appendix.

<!-- b000298 | caption | pages [14] -->
Table 8:Index judgment matrix

<!-- b000299 | prose | pages [14] -->
quality appearance price size service star ratings quality 1 2 1 2 2 1 appearance 0.5 1 1 1 2 1 price 1 1 1 2 1 1 size 0.5 1 0.5 1 0.5 1 service 0.5 0.5 1 2 1 0.5

<!-- b000300 | caption | pages [14] -->
Table 9:Evaluation Index and Weight

<!-- b000301 | prose | pages [14] -->
quality appearance price size service star ratings Weight(microwave oven) 0.21 0.13 0.20 0.13 0.13 0.20 Weight(hair dryer) 0.22 0.14 0.21 0.10 0.13 0.20 Weight(pacifier) 0.28 0.27 0.10 0.15 0.10 0.10

<!-- b000302 | prose | pages [14] -->
关注数学模型

<!-- b000303 | furniture | pages [14] -->
2

<!-- b000304 | furniture | pages [14] -->
MATHmodels

<!-- b000305 | furniture | pages [14] -->
获取更多资讯

<!-- b000306 | furniture | pages [15] -->
Team # 2010638                                                                   Page 14 of 20

<!-- b000307 | heading | pages [15] -->
4.4 System Clustering Analysis

<!-- b000308 | heading | pages [15] -->
4.4.1 Model establishment

<!-- b000309 | prose | pages [15] -->
Cluster analysis is a method of classification step by step. Its main idea is to reasonably merge and classify the research objects according to certain similarity indexes. It is called system clustering when it is used to solve the classification problem of samples and R-clustering when it is used to solve the classification problem of variables. We mainly uses cluster analysis to solve the problem of brand classification and evaluation. According to the observation indexes (star rating, quality, service, appearance, price, size) and system clustering algorithm of different brands, it calculates the similarity degree between brands, and classifies the similar brands into one category and the different brands into another. The closely related to a small classification unit, the not closely related to a large classification unit.

<!-- b000310 | prose | pages [15] -->
In a word, the result of system clustering analysis is to form a large to small classification pedigree or cluster diagram. Clustering graph can not only intuitively represent the similarity relationship and classification among the research objects, but also reflect all kinds of brands and quantitatively indicate the degree of similarity, so as to provide a good basis for the comprehensive evaluation.

<!-- b000311 | prose | pages [15] -->
Distance coefficient is a common statistic in system cluster analysis. If n brands observed on m variables kx can jx and are regarded as n points in m dimension space, the similarity between any two brands points be expressed by the distance between two points in m dimension space, then the distance coefficient is defined as:

<!-- b000312 | prose | pages [15] -->
1 1 m    2 d [ (x x ) ] (15) 2 jk ij ik m  i 1

<!-- b000313 | prose | pages [15] -->
Similarity coefficient is a measure of similarity between brands. Each brand is regarded as a vector of kx is defined as the cosine of the jx and m-dimensional space, and the similarity between two brands angle between two vectors, that is

<!-- b000314 | prose | pages [15] -->
m  x x ij ik    i 1 cos (16) jk m m   2 2 x x ij ij   i 1 i 1

<!-- b000315 | heading | pages [15] -->
4.4.2 Classification results

<!-- b000316 | prose | pages [15] -->
We use SPSS to cluster different parents and divide them into 10 grades. The first-class products are the best, and the tenth class products are the worst. In our sales strategy, we will recommend the first-class brands with better response in the sales market of sunshine company. Limited to space, only 5 first-class brands of each product are listed in the text.

<!-- b000317 | caption | pages [15] -->
Table 10:Part of Classification results

<!-- b000318 | prose | pages [15] -->
Microwave oven 862802057 423421857 692404913 464779766 423421857 Hair dryer 244516305 266176173 468944538 741916038 112413045 Pacifier 22060147 22189989 51496920 62352351 79207704 Note: The number in the table corresponds to the product parent.

<!-- b000319 | prose | pages [15] -->
关注数学模型

<!-- b000320 | furniture | pages [15] -->
2

<!-- b000321 | furniture | pages [15] -->
MATHmodels

<!-- b000322 | furniture | pages [15] -->
获取更多资讯

<!-- b000323 | furniture | pages [16] -->
Team # 2010638                                                                   Page 15 of 20

<!-- b000324 | heading | pages [16] -->
5. Model 3-Time Series Analysis

<!-- b000325 | prose | pages [16] -->
In this section, we construct a time series analysis model to analyze microwave reputation, hair dryer reputation and pacifier reputation. Afterwards the product reputation could be predicted after analyzing the reviews and star ratings about the products.

<!-- b000326 | prose | pages [16] -->
The product reputation is consisted with star rating and emotional inclination. According to statist ics, the customers are apt to pay more attention to the reviews when they buy goods, so the review shows greater impact on the product reputation than the star rating. Because of this, we assign 70% weight to the average emotional score and 30% weight to the average star rating. The sum of them is the comprehensive score of product reputation.

<!-- b000327 | prose | pages [16] -->
Due to hypotheses, the product reputation score will be influenced by autocorrelation in time seri th p -order Auto-Regression Model to fit curve, namely AR(p). es. As a consequence, we choose

<!-- b000328 | prose | pages [16] -->
      Y a Y a Y ... a Y (17)    n 1 n 1 2 n 2 p n p n

<!-- b000329 | prose | pages [16] -->
Where Y represents the product reputation score in year n.

<!-- b000330 | prose | pages [16] -->
  a a represent the influential coefficients of different lag orders. 1 p  represents the error term whose mean value is 0 and variance is .The distribution matches White 2 n 2 ) Noise Process WN(0, Firstly, we collected the time series data of three products’ reputation scores. Then we solve the auto-regession model of the reputation score and calculate the time-series autocorrelation function and partial autocorrelation function of the reputation scores to identify the order, and specifically calculated the parameter p .

<!-- b000331 | prose | pages [16] -->
The sequence correlation of the comprehensive scores of each product's reputation depicts an obvious autoregressive structure AR1, which means the involved functions don’t possess the property of truncation, and the partial functions possess the property of truncation. Therefore, we conclude that p=1 and the reputation score of all the three products share the same model setting.

<!-- b000332 | prose | pages [16] -->
    N N (18) 1 t 1 t t

<!-- b000333 | prose | pages [16] -->
1and the error term is different from the reputation The mean variance of the coefficient

<!-- b000334 | prose | pages [16] -->
changing. By calculation, we apply the MLE to estimate the coefficient of these three products.

<!-- b000335 | heading | pages [16] -->
Here we list the results:

<!-- b000336 | caption | pages [16] -->
Table 11: ARE Model for Different Products

<!-- b000337 | prose | pages [16] -->
 R 2 AR（1） product P-Value Hair dryer 0.125 0.046 0.007 0.901 pacifier 0.054 0.043 0.021 0.930 Microwave oven -0.075 0.050 0.000 0.952 It is clear that the results of coefficients testing are significant, meanwhile the overall fitting gets a good result with a high R-squared.

<!-- b000338 | prose | pages [16] -->
Afterwards we conduct over-fitting and under fitting test, which contributes to the accuracy of p=1.The test uses the Algorithm of information guidelines to consider both the error term and the parameters’ complexity.

<!-- b000339 | prose | pages [16] -->
2 p 2    AIC ln (19) n

<!-- b000340 | prose | pages [16, 17] -->
关注数学模型 p 2    BIC ln ln n (20) n Where n represents the size of sample. The test illustrates that when p=1, AIC and BIC get the minimum value. Therefore, we consider the fitting of AR(1) is reasonable.

<!-- b000341 | furniture | pages [16] -->
2

<!-- b000342 | furniture | pages [16] -->
MATHmodels

<!-- b000343 | furniture | pages [16] -->
获取更多资讯

<!-- b000344 | furniture | pages [17] -->
Team # 2010638                                                                   Page 16 of 20

<!-- b000346 | prose | pages [17] -->
The AR (1) model is constructed to predict the comprehensive scores of product reputations. The results are as follows:

<!-- b000347 | prose | pages [17] -->
Taking the hair dryer as an example, in order to observe the relationship between the comprehensive score of product reputation and the time changing trends, we analyzed and predicted the time series in SPSS.

<!-- b000348 | caption | pages [17] -->
Figure 10: Sequence Figure

<!-- b000349 | prose | pages [17] -->
Through the above sequence diagram, we find that the seasonal fluctuation of the time series is basically constant, so we choose the addition model to decompose the seasonal factors. After removing the seasonal factors, the value of error sequence is very small, so the long-term trend and cyclic change sequence (long-term trend + cyclic change) and the sequence after seasonal factor correction (long-term trend + cyclic change + irregular change, that is, error Poor) can basically coincide.

<!-- b000350 | caption | pages [17] -->
Figure 11:A sequence chart that eliminates seasonal trends    Figure 12:The original sequence

<!-- b000351 | prose | pages [17] -->
By analyzing the seasonal trend, it can be found that the trend first drops in the first quarter of each year, then rises to the first peak. Then after a sharp decline, there is an obvious upward trend, reaching the second peak in about the eighth month, then comes a small decline. After that it reaches the peak in about October, and then falling till the beginning of the next year. In order to analyze the reasons for the seasonal changes, we introduced the annual sales volume with the time chart. It can be seen that the timing of reputation and sales have roughly the same seasonal trend, indicating that with the increase of sales, customers are more likely to give favorable reviews. So we conclude that it is consistent with the actual situation. In summer, people wash their hair more frequently. Therefore, they are apt to buy hair dryers from June to August and have a higher probability of making favorable reviews. However, when winter comes around October, the temperature is

<!-- b000352 | prose | pages [17, 18] -->
关注数学模型 colder and the blowing time becomes longer, which might also improve the demand and reputation of hair dryer.

<!-- b000353 | furniture | pages [17] -->
2

<!-- b000354 | furniture | pages [17] -->
MATHmodels

<!-- b000355 | furniture | pages [17] -->
获取更多资讯

<!-- b000356 | furniture | pages [18] -->
Team # 2010638                                                                   Page 17 of 20

<!-- b000358 | caption | pages [18] -->
Figure 13: Time Series Forecasting               Figure 14:Annual sales for Three products

<!-- b000359 | prose | pages [18] -->
Through the prediction of time series, the data of 2016-2019 are obtained. It is found that the reputation and demand of hair dryer are highly related to the seasonality, and it is very likely to maintain a stable seasonal cycle mode in the future. Microwave ovens and pacifiers are about the same. The comprehensive score of the microwave oven reaches the peak in April and October, and that of the pacifier reaches the peak in November.

<!-- b000360 | prose | pages [18] -->
From the analysis above, it is believed that the market of hair dryer, microwave oven and pacifier is roughly stable. By referring to seasonal trend, sunshine company is capable to increase the sales share when the score of the product reputation rises up, or reduce the sales investment before the score is about to slump .

<!-- b000361 | heading | pages [18] -->
6. Model 4-Distributed lag model

<!-- b000362 | heading | pages [18] -->
6.1 Distributed lag model

<!-- b000363 | prose | pages [18] -->
In this part, we apply the distributed lag model to determine if the customer's reviews will be affected by others’ star ratings.

<!-- b000364 | prose | pages [18] -->
The distributed lag model is based on the fact that the explained variables are affected by the explanatory variables and distributed on the lagged values of the explanatory variables in different periods.

<!-- b000365 | prose | pages [18] -->
         Y X X X (21)   t 0 t 1 t 1 s t s

<!-- b000366 | prose | pages [18] -->
s is the lag length.

<!-- b000367 | prose | pages [18] -->
Each coefficient in this model reflects the different influence of each lag value of the explanatory variable on the explained variable, which is commonly referred to as multiplier effect:

<!-- b000368 | prose | pages [18] -->
0β ：Short-term multiplier, which represents the average influence of one unit of star rating change on the emotional score of the review;

<!-- b000369 | prose | pages [18] -->
iβ ：Delay multiplier, which represents the average influence of the change of one unit in the previous period star rating on the emotional score of the review;

<!-- b000370 | prose | pages [18] -->
s  ：The long-term multiplier, which indicates the total impact of the star rating changing due to β i i= 0 the lag effect.

<!-- b000371 | prose | pages [18] -->
关注数学模型

<!-- b000372 | furniture | pages [18] -->
2

<!-- b000373 | furniture | pages [18] -->
MATHmodels

<!-- b000374 | furniture | pages [18] -->
获取更多资讯

<!-- b000375 | furniture | pages [19] -->
Team # 2010638                                                                   Page 18 of 20

<!-- b000376 | heading | pages [19] -->
6.2 Almon Method

<!-- b000377 | prose | pages [19] -->
The second-order Almon polynomial distribution lag model with a lag of 3 periods is used to establish the regression equation between current reviews and previous star ratings and reviews, so as to determine whether there is a phenomenon that previous star ratings affect current customer reviews. We select the data of the hair dryer whose product parent is 732252283, the pacifier of 392768822 and the microwave oven of 423421857 for analysis.

<!-- b000378 | prose | pages [19] -->
The following finite distribution lag model is estimated by Almon method. And the coefficients are approximated by quadratic polynomials.

<!-- b000379 | prose | pages [19] -->
Y = α+ β X + β X + β X + β X +u t 0 t 1 t- 1 2 t- 2 3 t- 3 t β = α 0 0 β = α +α +α (22) 1 0 1 2 β = α + 2 α + 4 α 2 0 1 2 β = α +3 α +9 α 3 0 1 2 Then the original model can be transformed into           Y Z Z Z t 0 0 t 1 1 t 2 2 t t     Z

<!-- b000380 | heading | pages [19] -->
X X

<!-- b000381 | heading | pages [19] -->
X X

<!-- b000382 | prose | pages [19] -->
   0 t t t 1 t 2 t 3    Z

<!-- b000383 | heading | pages [19] -->
X X

<!-- b000384 | prose | pages [19] -->
2 3 X    1 t t 1 t 2 t 3    Z

<!-- b000385 | heading | pages [19] -->
X X

<!-- b000386 | prose | pages [19] -->
4 9 X (23)    2 t t 1 t 2 t 3

<!-- b000387 | prose | pages [19] -->
The final estimation formula of the distribution lag model can be obtained by regression. The regression results are as follows:

<!-- b000388 | caption | pages [19] -->
Table 12:Regression Results

<!-- b000389 | prose | pages [19] -->
2 R 0β 1β 2β 3β 1.13221∗∗ 0.32379∗∗ Hair dryer -0.05354 0.00020 0.902197 -0.03039（0） 0.79191∗∗ 0.21743∗∗ Pacifier 0.04845 0.929296

<!-- b000390 | prose | pages [19] -->
1.05871∗∗ 0.17710∗∗ Microwave -0.13628 0.11858 0.835728

<!-- b000391 | prose | pages [19] -->
Note:*: p<0.05; **: p<0.01; +: p<0.1; ns: not significant The regression equation between the comprehensive scores of past star ratings and the emotional score of the current reviews of the three products is as follows:

<!-- b000392 | prose | pages [19] -->
    Y 0.34 247 2 1.13221X 0.32379 X  t t t 1    (24) Y 0.054537 0.79191X 0.21743 X  t t t 1    Y 0.226388 1.05871X 0.1771 0 X  t t t 1 Therefore, it can be explained that there is a correlation between the current reviews of customers and the past star ratings and reviews, that is, the current evaluation of customers will be affected by the past ratings and evaluations.

<!-- b000393 | heading | pages [19] -->
6.3 Correlation Analysis between Star Rating and Comments

<!-- b000394 | prose | pages [19] -->
According to the time series model, the inflection points of customer reviews can be gotten quickly. By analyzing the specific quality descriptors in the reviews corresponding to these inflection points, and

<!-- b000395 | prose | pages [19, 20] -->
关注数学模型 comparing them with the star ratings corresponding to the reviews, it is easy to know whether these words are closely related to the star ratings. In the above model, the average score of reviews and star ratings in each time period has been obtained. By comparing the synchronicity of the two changes over time, we can draw the conclusion that the star ratings corresponding to the reviews with positive words are higher, while the star ratings corresponding to the reviews with negative words are lower. (Due to the space, we only put the picture of microwave oven in the text, the picture of hair dryer and pacifier in the appendix.)

<!-- b000396 | furniture | pages [19] -->
2

<!-- b000397 | furniture | pages [19] -->
MATHmodels

<!-- b000398 | furniture | pages [19] -->
获取更多资讯

<!-- b000399 | furniture | pages [20] -->
Team # 2010638                                                                   Page 19 of 20

<!-- b000401 | caption | pages [20] -->
Figure 15: Sequence Diagram of Star rating and Review

<!-- b000402 | prose | pages [20] -->
However, it still can be seen from the diagrams that some reviews with higher star ratings have lower emotional scores, so it is not excluded that there are high scores, poor reviews (or vice versa) and false reviews.

<!-- b000403 | heading | pages [20] -->
7.  Sensitivity Analysis

<!-- b000404 | prose | pages [20] -->
In the time series analysis model, we give star ratings and reviews 0.3 and 0.7 weight respectively, representing the comprehensive evaluation of each customer on the products they buy. Based on the principle that the importance of reviews is higher than that of star ratings, in order to test the rationality of the weight, we change the weight of star ratings to test whether the results of the model change significantly under the weight ratio of 0.4 and 0.2 respectively. The results are as follows:

<!-- b000405 | caption | pages [20] -->
Table 13: Sensitivity Analysis on Weight of Star Rating

<!-- b000406 | prose | pages [20] -->
a b Product Change (in %) Change (in %) AR （1 AR （1 ） ）

<!-- b000407 | prose | pages [20] -->
Hair Dryer 0.126 0.8% 0.127 20% Pacifier 0.054 -0.9% 0.054 18% Microwave Oven -0.075 0.3% -0.074 -0.6% Note: 𝐴𝑅(1)𝑎: weight of star ratings: 0.4 ; 𝐴𝑅(1)𝑏: weight of star ratings: 0.2 From the table, we can see that the deviation of regression coefficient is not more than 1.8%, which shows that the change of weight has no significant impact on the results of the model, so the weight of 0.3 and 0.7 we set has certain rationality.

<!-- b000408 | prose | pages [20] -->
关注数学模型

<!-- b000409 | furniture | pages [20] -->
2

<!-- b000410 | furniture | pages [20] -->
MATHmodels

<!-- b000411 | furniture | pages [20] -->
获取更多资讯

<!-- b000412 | furniture | pages [21] -->
Team # 2010638                                                                   Page 20 of 20

<!-- b000413 | heading | pages [21] -->
8. Model Assessment

<!-- b000414 | heading | pages [21] -->
8.1 Strengths

<!-- b000415 | prose | pages [21] -->
 Data visualization technology is applied to interpret the original data, and the results are presented intuitively and concisely.

<!-- b000416 | prose | pages [21] -->
 Through the analysis of LDA topic model, the strengths and weaknesses of the products can be given, which is helpful for the design of products.

<!-- b000417 | prose | pages [21] -->
 Our products brand rating system has a wide range of applicability, which can help sales companies grasp customer reviews on the market.

<!-- b000418 | heading | pages [21] -->
8.2 Weaknesses

<!-- b000419 | prose | pages [21] -->
 Our product scoring system uses AHP to determine the weight of each index, which is to some extent subjective.

<!-- b000420 | prose | pages [21] -->
 Our time series model uses monthly data, which is not very accurate and does not take into account special circumstances such as holidays, and may have a large gap with the actual results, and cannot effectively predict the product’s reputation in the long term.

<!-- b000421 | heading | pages [21] -->
Reference

<!-- b000422 | references | pages [21] -->
[1]Arreola Elsa Vazquez,Wilson Jeffrey R. Bayesian multiple membership multiple classification logistic

<!-- b000423 | references | pages [21] -->
regression model on student performance with random effects in university instructors and majors.[J]. PloS

<!-- b000424 | references | pages [21] -->
one,2020,15(1).

<!-- b000425 | references | pages [21] -->
[2]Blei D M, Ng A Y, Jordan M I. Latent dirichlet allocation[J]. Journal of Machine Learning Research, 2003,

<!-- b000426 | references | pages [21] -->
3:2003.

<!-- b000427 | references | pages [21] -->
[3]Cao Juan, Xia Tian, Li Jin Tao, A density method for adaptive LDA model selection[J]. Neurocomputing

<!-- b000428 | references | pages [21] -->
2009(72):1775-1781.

<!-- b000429 | references | pages [21] -->
[4]Connors, L., Mudambi, S.M., Schuff, D.. Is It the Review or the Reviewer? a Multi-Method Approach to

<!-- b000430 | references | pages [21] -->
Determine the Antecedents of Online Review Helpfulness[P]. System Sciences (HICSS), 2011 44th Hawaii

<!-- b000431 | references | pages [21] -->
International Conference on,2011.

<!-- b000432 | references | pages [21] -->
[5]Changxuan Wan,Yun Peng,Keli Xiao,Xiping Liu,Tengjiao Jiang,Dexi Liu. An association-constrained LDA

<!-- b000433 | references | pages [21] -->
model for joint extraction of product aspects and opinions[J]. Information Sciences,2020,519.

<!-- b000434 | references | pages [21] -->
[6]Cheung, Christy M. K., and Dimple R. Thadani. “The Effectiveness of Electronic Word-of-Mouth

<!-- b000435 | references | pages [21] -->
Communication: A Literature Analysis.” Bled EConference, 2010, p. 18.

<!-- b000436 | references | pages [21] -->
[7]Kim, Soo-Min, et al. “Automatically Assessing Review Helpfulness.” Proceedings of the 2006 Conference

<!-- b000437 | references | pages [21] -->
on Empirical Methods in Natural Language Processing, 2006, pp. 423–430.

<!-- b000438 | references | pages [21] -->
[8]Mudambi, Susan M.,Schuff, David,Zhang, Zhewei. Why Aren't the Stars Aligned? An Analysis of Online

<!-- b000439 | references | pages [21] -->
Review Content and Star Ratings[P]. ,2014.

<!-- b000440 | references | pages [21] -->
[9]Yan Leng,Weiwei Zhao,Chan Lin,Chengli Sun,Rongyan Wang,Qi Yuan,Dengwang Li. LDA-based data

<!-- b000441 | references | pages [21] -->
augmentation algorithm for acoustic scene classification[J]. Knowledge-Based Systems,2020.

<!-- b000442 | references | pages [21] -->
关注数学模型

<!-- b000443 | furniture | pages [21] -->
2

<!-- b000444 | furniture | pages [21] -->
MATHmodels

<!-- b000445 | furniture | pages [21] -->
获取更多资讯

<!-- b000446 | furniture | pages [22] -->
Team # 2010638                                                                   Page 1 of 2

<!-- b000447 | heading | pages [22] -->
Letter

<!-- b000448 | prose | pages [22] -->
Dear Sunshine Company Marketing Director:

<!-- b000449 | prose | pages [22] -->
We are honored to inform you of our recommendations for product improvement and sales strategies for your company after data analysis and modeling. The following are some suggestions based on our analysis.

<!-- b000450 | heading | pages [22] -->
1. Suggestions for product improvement

<!-- b000451 | prose | pages [22] -->
We apply the LDA analysis model to find the topic feature of each product, in which the negative topic words can reflect the customers' dissatisfaction with the existing products in the market.

<!-- b000452 | prose | pages [22] -->
Analysis of the review text revealed that the words like "cost", "heavy", "smoking" and "noise" appeared on the top of the list of negative reviews on the hair dryer. After analyzing these high-frequency words one by one, we discovered that there were some drawbacks with hair dryers from the customers’ point of view:

<!-- b000453 | prose | pages [22] -->
 Inefficiency: it takes a long time to blow-dry.

<!-- b000454 | prose | pages [22] -->
 Weight: it is too heavy to use conveniently.

<!-- b000455 | prose | pages [22] -->
 Bad quality: when using the product, there will be a lot of noise sometimes.

<!-- b000456 | prose | pages [22] -->
Therefore, according to the feedback above, we believe that the improvement of hair dryer products is supposed to start from improving the working efficiency and quality of hair dryer. Lightweight materials can be used in the production, reducing the weight of the hair dryer, should also reduce the noise when it works. For instance, lightweight materials can be used to reduce the weight of the hair dryer and reduce the noise while it is working.

<!-- b000457 | prose | pages [22] -->
As for microwave oven, words like "service" and "small" appeared on the top of the list of negative reviews. According to the feedback, we believe that the microwave oven may have the following defects:

<!-- b000458 | prose | pages [22] -->
 Size: someone considered that microwave ovens are too small, while others reckon that small ones are more convenient to use.

<!-- b000459 | prose | pages [22] -->
 Service: the after-sale service of some microwave ovens is not consummate.

<!-- b000460 | prose | pages [22] -->
In view of the above two points, we hold that microwave oven products can be designed in different sizes to meet the diverse needs of different customers. Moreover, improving service level and customer satisfaction is also a top priority.

<!-- b000461 | prose | pages [22] -->
"Hot" is the most frequently used negative word for a pacifier. Some customers think that the insulation function of the pacifier is poor, which reminds us that we should enhance the thermal insulation function in the design of the pacifier. In addition, we have noticed that customers attach great importance to the "appearance" of the pacifier and hence the cute product design will help to sell the product.

<!-- b000462 | heading | pages [22] -->
2. Sales strategy

<!-- b000463 | prose | pages [22] -->
Through the in-depth analysis of star ratings and reviews, we will propose sales suggestions and strategies from three aspects: the product brand, the time of selling products and the evaluation psychology of customers.

<!-- b000464 | prose | pages [22] -->
 Recommend the product brand for sale.

<!-- b000465 | prose | pages [22, 23] -->
关注数学模型 Based on the analysis of star rating and review, we summarized five indexes that affect product sales, namely quality, price, appearance, service and size, as well as index weight, then built a brand scoring system based on this. Through the systematic clustering of each score, all product brands were clustered, and the high-quality product brands were selected eventually. The product parent of some premium brands is as follows:

<!-- b000466 | furniture | pages [22] -->
2

<!-- b000467 | furniture | pages [22] -->
MATHmodels

<!-- b000468 | furniture | pages [22] -->
获取更多资讯

<!-- b000469 | furniture | pages [23] -->
Team # 2010638                                                                   Page 2 of 2

<!-- b000471 | prose | pages [23] -->
microwave 862802057 423421857 692404913 464779766 423421857 Hair-dryer 244516305 266176173 468944538 741916038 112413045 pacifier 22060147 22189989 51496920 62352351 79207704 Our brand rating system takes full account of the characteristics of each product, so the conclusions are very reliable. It is believed that the high quality brands recommended for sale will be favored by more customers.

<!-- b000472 | prose | pages [23] -->
 Sales opportunities analysis.

<!-- b000473 | prose | pages [23] -->
we predict the future reputation of the three products through time series analysis. The results demonstrate that the three products are highly correlated with seasonality, and the seasonal cycle pattern is likely to be stable in the future. However, the peaks of reputation composite scores of the three products occurred at different times.

<!-- b000474 | prose | pages [23] -->
Pacifiers peaked around November, hairdryers around August and October, and microwave ovens around April and October. The peak of reputation will lead to an increase in sales, so we suggest that your company adjust the sales structure according to the peak time of different products. When the product reputation is about to peak, your company can increase the sales investment of the product to obtain higher revenue.

<!-- b000475 | prose | pages [23] -->
 Psychological analysis of customer reviews.

<!-- b000476 | prose | pages [23] -->
We analyze the relationship between star rating and review. Through the research of distributed lag model, it is found that customers' reviews in the current period will be influenced by other customers' ratings and reviews. Therefore, we suggest that your company should still pay attention to the customer's rating of the goods after selling the products, and try to make the rating of its own products at a high level, so as not to gain a bad impact on future sales. To sum up, by keeping an eye on customers' preferences and regarding them as standards for improving products and services, your company can gradually increase product sales and market share.

<!-- b000477 | prose | pages [23] -->
These are all suggestions and strategies our team has provided to your company. Thank you again for taking the time to read our suggestions.

<!-- b000478 | prose | pages [23] -->
Hope that our models and these suggestions can be helpful to you!

<!-- b000479 | prose | pages [23] -->
Sincerely,

<!-- b000480 | heading | pages [23] -->
MCM Team Members

<!-- b000481 | prose | pages [23] -->
关注数学模型

<!-- b000482 | furniture | pages [23] -->
2

<!-- b000483 | furniture | pages [23] -->
MATHmodels

<!-- b000484 | furniture | pages [23] -->
获取更多资讯

<!-- b000485 | furniture | pages [24] -->
Team # 2010638                                                                   Page 1 of 20

<!-- b000486 | heading | pages [24] -->
Appendix

<!-- b000487 | heading | pages [24] -->
Appendix 1

<!-- b000488 | prose | pages [24] -->
Correlation analysis                          The distribution of the number of words

<!-- b000489 | prose | pages [24] -->
 Consistency test of AHP Consistency check ratio table Consis qu appeara servi Star price size tency ratio ality nce ce ratings 0.0 0.00 0.00 0.00 0.00 CR 0.00857 0000 688 0817 053 047

<!-- b000490 | heading | pages [24] -->
Appendix 2

<!-- b000491 | heading | pages [24] -->
Regression results of distribution lag model

<!-- b000492 | heading | pages [24] -->
1. Hair dryer

<!-- b000493 | prose | pages [24] -->
Coefficie Std.

<!-- b000494 | prose | pages [24] -->
Variable nt Error t-Statistic Prob.

<!-- b000495 | prose | pages [24] -->
-0.34247 0.06643 C 2 0 -5.155354 0.0000 0.04057 PDL01 0.323795 2 7.980680 0.0000 -0.59287 0.04035 PDL02 8 2 -14.69277 0.0000 0.02861 PDL03 0.215540 2 7.533150 0.0000

<!-- b000496 | prose | pages [24, 25] -->
关注数学模型 0.64829 R-squared 0.902197 Mean dependent var 3 0.22365 Adjusted R-squared 0.896444 S.D. dependent var 9 -2.3550 S.E. of regression 0.071974 Akaike info criterion 86 -2.2090 Sum squared resid 0.264190 Schwarz criterion 99 -2.2986 Log likelihood 68.76488 Hannan-Quinn criter. 32 1.71152 F-statistic 156.8187 Durbin-Watson stat 2 Prob(F-statistic) 0.000000

<!-- b000497 | furniture | pages [24] -->
2

<!-- b000498 | furniture | pages [24] -->
MATHmodels

<!-- b000499 | furniture | pages [24] -->
获取更多资讯

<!-- b000500 | furniture | pages [25] -->
Team # 2010638                                                                   Page 2 of 20

<!-- b000502 | prose | pages [25] -->
Lag Distribution Coeffici t-Statisti of TOTAL ent Std. Error c

<!-- b000503 | prose | pages [25] -->
.              *| 1.13221 0.05595 20.2356 .   *           | 0.32379 0.04057 7.98068 -0.0535 -1.3294 *.               | 4 0.04027 8 *               | 0.00020 0.05539 0.00358

<!-- b000504 | prose | pages [25] -->
Sum of 1.4026 15.175 Lags 6 0.09243 1

<!-- b000505 | heading | pages [25] -->
2. Pacifier

<!-- b000506 | prose | pages [25] -->
Coefficie Std.

<!-- b000507 | prose | pages [25] -->
Variable nt Error t-Statistic Prob.

<!-- b000508 | prose | pages [25] -->
-0.05453 0.10941 C 7 9 -0.498424 0.6201 0.05220 PDL01 0.217428 1 4.165216 0.0001 -0.41115 0.05242 PDL02 2 4 -7.842873 0.0000 0.03664 PDL03 0.163331 1 4.457639 0.0000

<!-- b000509 | prose | pages [25] -->
0.73679 R-squared 0.629296 Mean dependent var 9 0.16242 Adjusted R-squared 0.609786 S.D. dependent var 3 -1.6749 S.E. of regression 0.101461 Akaike info criterion 65

<!-- b000510 | prose | pages [25, 26] -->
关注数学模型 -1.5365 Sum squared resid 0.586774 Schwarz criterion 47 -1.6207 Log likelihood 55.08642 Hannan-Quinn criter. 17 1.59103 F-statistic 32.25389 Durbin-Watson stat 8 Prob(F-statistic) 0.000000

<!-- b000511 | furniture | pages [25] -->
2

<!-- b000512 | furniture | pages [25] -->
MATHmodels

<!-- b000513 | furniture | pages [25] -->
获取更多资讯

<!-- b000514 | furniture | pages [26] -->
Team # 2010638                                                                   Page 3 of 20

<!-- b000516 | prose | pages [26] -->
Lag Distribution Coeffici t-Statisti of TOTAL ent Std. Error c

<!-- b000517 | prose | pages [26] -->
.              *| 0.79191 0.08171 9.69200 .   *           | 0.21743 0.05220 4.16522 -0.0303 -0.6099 *.               | 9 0.04982 9 .*              | 0.04845 0.06081 0.79669

<!-- b000518 | prose | pages [26] -->
Sum of 1.0273 7.2225 Lags 9 0.14225 3

<!-- b000519 | heading | pages [26] -->
3. Microwave oven

<!-- b000520 | prose | pages [26] -->
Coefficie Std.

<!-- b000521 | prose | pages [26] -->
Variable nt Error t-Statistic Prob.

<!-- b000522 | prose | pages [26] -->
-0.22638 0.07200 C 8 6 -3.144010 0.0030 0.05482 PDL01 0.177103 2 3.230494 0.0023 -0.59749 0.05752 PDL02 4 5 -10.38663 0.0000 0.04604 PDL03 0.284116 5 6.170329 0.0000

<!-- b000523 | prose | pages [26] -->
0.52140 R-squared 0.835728 Mean dependent var 9 0.22024 Adjusted R-squared 0.824528 S.D. dependent var 0 -1.8488 S.E. of regression 0.092257 Akaike info criterion 16 -1.6928 Sum squared resid 0.374502 Schwarz criterion 83 -1.7898 Log likelihood 48.37159 Hannan-Quinn criter. 89 1.49272 F-statistic 74.61626 Durbin-Watson stat 4

<!-- b000524 | prose | pages [26, 27] -->
关注数学模型 Prob(F-statistic) 0.000000

<!-- b000525 | furniture | pages [26] -->
2

<!-- b000526 | furniture | pages [26] -->
MATHmodels

<!-- b000527 | furniture | pages [26] -->
获取更多资讯

<!-- b000528 | furniture | pages [27] -->
Team # 2010638                                                                   Page 4 of 20

<!-- b000530 | prose | pages [27] -->
Lag Distribution Coeffici t-Statisti of TOTAL ent Std. Error c

<!-- b000531 | prose | pages [27] -->
.             *| 1.05871 0.07634 13.8681 . *            | 0.17710 0.05482 3.23049 -0.1362 -2.4775 * .              | 8 0.05500 9 . *            | 0.11858 0.07611 1.55802

<!-- b000532 | prose | pages [27] -->
Sum of 1.2181 10.594 Lags 2 0.11498 4

<!-- b000533 | heading | pages [27] -->
Appendix 3

<!-- b000534 | heading | pages [27] -->
Partial system clustering results

<!-- b000535 | prose | pages [27] -->
1.

<!-- b000536 | prose | pages [27] -->
Microwave 10 9 8 7 6 5 oven clusters clusters clusters clusters clusters clusters 1:1092263 1 1 1 1 1 1 52 2:1474013 2 2 2 2 2 2 77 3:1495592 3 3 3 3 3 3 60 4:1555287 2 2 2 2 2 2 92 5:1664839 4 4 4 4 4 2 32 6:1681813 4 4 4 4 4 2 02 7:2159538 2 2 2 2 2 2 85 8:2427278 5 5 4 4 4 2 54 9:2955201 4 4 4 4 4 2 51 10:305608 1 1 1 1 1 1 994 11:309267 1 1 1 1 1 1 414

<!-- b000537 | prose | pages [27, 28] -->
关注数学模型 12:311592 6 6 5 5 5 4 014 13:313983 7 7 6 6 6 5 847 14:379992 4 4 4 4 4 2 322 15:392967 2 2 2 2 2 2 251 16:423421 1 1 1 1 1 1 857 17:454581 7 7 6 6 6 5 724 18:459626 1 1 1 1 1 1 087 19:464779 4 4 4 4 4 2 766 20:486381 5 5 4 4 4 2 187 21:494028 2 2 2 2 2 2 413 22:494668 5 5 4 4 4 2 275 23:522487 6 6 5 5 5 4 135 24:523301 1 1 1 1 1 1 568 25:539049 2 2 2 2 2 2 610 26:542519 5 5 4 4 4 2 500 27:542731 2 2 2 2 2 2 946 28:544821 2 2 2 2 2 2 753 29:550562 8 8 7 7 5 4 680

<!-- b000538 | furniture | pages [27] -->
2

<!-- b000539 | furniture | pages [27] -->
MATHmodels

<!-- b000540 | furniture | pages [27] -->
获取更多资讯

<!-- b000541 | furniture | pages [28] -->
Team # 2010638                                                                   Page 5 of 20

<!-- b000543 | prose | pages [28] -->
2.

<!-- b000544 | prose | pages [28] -->
10 9 8 7 6 5 Pacifier clusters clusters clusters clusters clusters clusters 1: 1 1 1 1 1 1 723849 2: 2 2 2 2 2 2 1006724

<!-- b000545 | prose | pages [28, 29] -->
关注数学模型 3: 3 3 1 1 1 1 1398002 4: 3 3 1 1 1 1 1439995 5: 4 2 2 2 2 2 1448183 6: 3 3 1 1 1 1 1696639 7: 4 2 2 2 2 2 1892472 8: 5 4 3 3 3 3 2143250 9: 4 2 2 2 2 2 2332208 10: 4 2 2 2 2 2 2341622 11: 4 2 2 2 2 2 2775015 12: 6 5 4 4 3 3 3090006 13: 3 3 1 1 1 1 3146962 14: 5 4 3 3 3 3 3179934 15: 2 2 2 2 2 2 3729223 16: 4 2 2 2 2 2 3916839 17: 1 1 1 1 1 1 4145037 18: 4 2 2 2 2 2 4569674 19: 3 3 1 1 1 1 4649401 20: 2 2 2 2 2 2 4792175 21: 2 2 2 2 2 2 5180901 22: 2 2 2 2 2 2 5471085 23: 4 2 2 2 2 2 5645959 24: 4 2 2 2 2 2 5747909

<!-- b000546 | furniture | pages [28] -->
2

<!-- b000547 | furniture | pages [28] -->
MATHmodels

<!-- b000548 | furniture | pages [28] -->
获取更多资讯

<!-- b000549 | furniture | pages [29] -->
Team # 2010638                                                                   Page 6 of 20

<!-- b000551 | prose | pages [29, 30] -->
关注数学模型 25: 4 2 2 2 2 2 5749221 26: 4 2 2 2 2 2 5848633 27: 4 2 2 2 2 2 5981131 28: 2 2 2 2 2 2 6156155 29: 2 2 2 2 2 2 6744486 30: 2 2 2 2 2 2 6784496 31: 4 2 2 2 2 2 7090204 3.

<!-- b000552 | furniture | pages [29] -->
2

<!-- b000553 | furniture | pages [29] -->
MATHmodels

<!-- b000554 | furniture | pages [29] -->
获取更多资讯

<!-- b000555 | furniture | pages [30] -->
Team # 2010638                                                                   Page 7 of 20

<!-- b000557 | prose | pages [30] -->
Hair 10 9 8 7 6 dryer clusters clusters clusters clusters clusters 1: 1 1 1 1 1 423960 2: 2 2 2 1 1 4120409 3: 3 3 3 2 2 11468070 4: 2 2 2 1 1 12536427 5: 2 2 2 1 1 14552349 6: 1 1 1 1 1 16483457 7: 2 2 2 1 1 16983648 8: 2 2 2 1 1 21033180 9: 2 2 2 1 1 21750700 10: 1 1 1 1 1 26711891 11: 3 3 3 2 2 30965255 12: 4 4 4 3 3 44138644 13: 5 5 5 4 4 44703144

<!-- b000558 | prose | pages [30, 31] -->
关注数学模型 14: 1 1 1 1 1 45575190 15: 2 2 2 1 1 46450049 16: 2 2 2 1 1 46677591 17: 1 1 1 1 1 47684938 18: 2 2 2 1 1 50000317 19: 2 2 2 1 1 54378879 20: 4 4 4 3 3 54987170 21: 1 1 1 1 1 55445525 22: 2 2 2 1 1 55520986 23: 1 1 1 1 1 57056668 24: 4 4 4 3 3 61225676 25: 6 1 1 1 1 62808517 26: 2 2 2 1 1 64142513 27: 1 1 1 1 1 66014174 28: 1 1 1 1 1 66259499 29: 2 2 2 1 1 66279275 30: 1 1 1 1 1 68100320 31: 2 2 2 1 1 68816102 32: 4 4 4 3 3 71698270 33: 7 6 6 5 5 74202592 34: 1 1 1 1 1 74735317 35: 2 2 2 1 1 77898021

<!-- b000559 | furniture | pages [30] -->
2

<!-- b000560 | furniture | pages [30] -->
MATHmodels

<!-- b000561 | furniture | pages [30] -->
获取更多资讯

<!-- b000562 | furniture | pages [31] -->
Team # 2010638                                                                   Page 8 of 20

<!-- b000564 | prose | pages [31, 32] -->
关注数学模型 36: 8 7 7 6 2 80193353 37: 1 1 1 1 1 84440271 38: 2 2 2 1 1 91277457 39: 1 1 1 1 1 98133587 40: 2 2 2 1 1 99665579 41:10734 1 1 1 1 1 1965 42:10819 1 1 1 1 1 1918 43:10910 1 1 1 1 1 6777 44:11093 2 2 2 1 1 5305 45:11241 9 8 5 4 4 3045 46:11526 2 2 2 1 1 4052

<!-- b000565 | furniture | pages [31] -->
2

<!-- b000566 | furniture | pages [31] -->
MATHmodels

<!-- b000567 | furniture | pages [31] -->
获取更多资讯

<!-- b000568 | furniture | pages [32] -->
Team # 2010638                                                                   Page 9 of 20

<!-- b000570 | heading | pages [32] -->
Appendix 4

<!-- b000571 | prose | pages [32] -->
Part of the monthly score of review and star rating

<!-- b000572 | heading | pages [32] -->
1. Hair dryer

<!-- b000573 | prose | pages [32] -->
review star_r comp _date ating ound 2002/3 3 0.97 /31 36 2002/4 5 0.73 /30 13 2002/5 3.829 0.50 /31 601 5325 2002/6 3.829 0.50 /30 601 5325 2002/7 5 0.95 /31 92 2002/8 3 0.57 /31 93 2002/9 3.829 0.50 /30 601 5325

<!-- b000574 | prose | pages [32, 33] -->
关注数学模型 2002/1 3.829 0.50 0/31 601 5325 2002/1 4 0.92 1/30 61 2002/1 5 -0.12 2/31 97 2003/1 4.5 0.75 /31 76 2003/2 4 0.89 /28 9 2003/3 4 0.88 /31 425 2003/4 5 0.82 /30 94 2003/5 3.829 0.50 /31 601 5325 2003/6 3.829 0.50 /30 601 5325 2003/7 3.829 0.50 /31 601 5325 2003/8 3.829 0.50 /31 601 5325 2003/9 3.829 0.50 /30 601 5325 2003/1 3.829 0.50 0/31 601 5325 2003/1 3.829 0.50 1/30 601 5325 2003/1 3.829 0.50 2/31 601 5325 2004/1 2.5 0.08 /31 485 2004/2 3.829 0.50 /29 601 5325 2004/3 5 0.95 /31 955 2004/4 3.829 0.50 /30 601 5325 2004/5 1 -0.47 /31 67 2004/6 3.829 0.50 /30 601 5325 2004/7 3.829 0.50 /31 601 5325

<!-- b000575 | furniture | pages [32] -->
2

<!-- b000576 | furniture | pages [32] -->
MATHmodels

<!-- b000577 | furniture | pages [32] -->
获取更多资讯

<!-- b000578 | furniture | pages [33] -->
Team # 2010638                                                                   Page 10 of 20

<!-- b000580 | prose | pages [33, 34] -->
关注数学模型 2004/8 2 0.45 /31 88 2004/9 3.829 0.50 /30 601 5325 2004/1 3.829 0.50 0/31 601 5325 2004/1 4 0.15 1/30 315 2004/1 3.829 0.50 2/31 601 5325 2005/1 3.829 0.50 /31 601 5325 2005/2 3.829 0.50 /28 601 5325 2005/3 3.829 0.50 /31 601 5325 2005/4 1 -0.47 /30 14 2005/5 1 -0.29 /31 66 2005/6 5 0.20 /30 08 2005/7 5 -0.40 /31 66 2005/8 3 0.82 /31 55 2005/9 4.333 0.80 /30 333 87 2005/1 5 0.83 0/31 9467 2005/1 3.5 0.88 1/30 995 2005/1 4.5 0.68 2/31 685 2006/1 3.357 0.66 /31 143 7943 2006/2 2.875 0.45 /28 3613 2006/3 3.309 0.21 /31 524 46 2006/4 3 0.39 /30 6333 2006/5 1.666 0.24 /31 667 26

<!-- b000581 | furniture | pages [33] -->
2

<!-- b000582 | furniture | pages [33] -->
MATHmodels

<!-- b000583 | furniture | pages [33] -->
获取更多资讯

<!-- b000584 | furniture | pages [34] -->
Team # 2010638                                                                   Page 11 of 20

<!-- b000586 | prose | pages [34, 35] -->
关注数学模型 2006/6 2 0.37 /30 806 2006/7 3.333 0.44 /31 333 7167

<!-- b000587 | furniture | pages [34] -->
2

<!-- b000588 | furniture | pages [34] -->
MATHmodels

<!-- b000589 | furniture | pages [34] -->
获取更多资讯

<!-- b000590 | furniture | pages [35] -->
Team # 2010638                                                                   Page 12 of 20

<!-- b000592 | heading | pages [35] -->
2. Pacifier

<!-- b000593 | prose | pages [35] -->
review star_r comp _date ating ound 2003/4 2 0.58 /30 35 2003/5 4.4 0.60 /31 842 2003/6 4.333 0.77 /30 333 0685 2003/7 3.375 0.74 /31 2837 2003/8 4.111 0.48 /31 111 7467 2003/9 4.210 0.57 /30 547 1278 2003/1 4.55 0.75 0/31 1675 2003/1 3.605 0.52 1/30 442 3395 2003/1 1 0.92 2/31 2004/1 4.137 0.69 /31 209 7009 2004/2 4.196 0.70 /29 297 3307 2004/3 4.146 0.45 /31 052 704 2004/4 4.5 0.67 /30 37 2004/5 2 0.91 /31 86 2004/6 2 0.81 /30 08 2004/7 4.499 0.65 /31 116 3345 2004/8 4.455 0.64 /31 441 6819 2004/9 4.361 0.58 /30 652 1429

<!-- b000594 | prose | pages [35, 36] -->
关注数学模型 2004/1 4.452 0.64 0/31 883 6562 2004/1 4.379 0.66 1/30 498 2509 2004/1 4.344 0.62 2/31 347 298 2005/1 4.333 0.59 /31 011 3006 2005/2 5 0.96 /28 96 2005/3 3.534 0.49 /31 091 2098 2005/4 3.883 0.63 /30 333 9112 2005/5 4.391 0.50 /31 507 169 2005/6 4.296 0.49 /30 748 209 2005/7 4.434 0.52 /31 554 5116 2005/8 4.332 0.49 /31 839 5799 2005/9 4.344 0.51 /30 876 9694 2005/1 5 0.84 0/31 72 2005/1 5 0.96 1/30 89 2005/1 4.541 0.72 2/31 667 4842 2006/1 4.637 0.75 /31 5 9315 2006/2 4 0.94 /28 06 2006/3 5 0.94 /31 94 2006/4 3.534 0.49 /30 091 2098 2006/5 2.7 0.75 /31 511 2006/6 3.666 0.21 /30 667 575 2006/7 4.267 0.54 /31 442 0129

<!-- b000595 | furniture | pages [35] -->
2

<!-- b000596 | furniture | pages [35] -->
MATHmodels

<!-- b000597 | furniture | pages [35] -->
获取更多资讯

<!-- b000598 | furniture | pages [36] -->
Team # 2010638                                                                   Page 13 of 20

<!-- b000600 | prose | pages [36, 37] -->
关注数学模型 2006/8 5 0.96 /31 91 2006/9 4.25 0.73 /30 5613 2006/1 5 0.95 0/31 905 2006/1 3 0.73 1/30 49

<!-- b000601 | furniture | pages [36] -->
2

<!-- b000602 | furniture | pages [36] -->
MATHmodels

<!-- b000603 | furniture | pages [36] -->
获取更多资讯

<!-- b000604 | furniture | pages [37] -->
Team # 2010638                                                                   Page 14 of 20

<!-- b000606 | heading | pages [37] -->
3. Microwave oven

<!-- b000607 | prose | pages [37] -->
review star_r comp _date ating ound 2004/6 4 0.70 /30 5233 2004/7 3 -0.79 /31 92 2004/8 1 -0.42 /31 15 2004/9 1.333 0.24 /30 333 1867 2004/1 5 0.99 0/31 25 2004/1 3 0.50 1/30 63 2004/1 3 0.98 2/31 18 2005/1 5 0.98 /31 54 2005/2 3 0.34 /28 7794 2005/3 2.773 0.16 /31 333 9515 2005/4 2.865 0.36 /30 385 0717 2005/5 3 0.32 /31 0475 2005/6 3 0.41 /30 8019 2005/7 5 -0.52 /31 67 2005/8 2.773 0.16 /31 333 9515 2005/9 2.865 0.36 /30 385 0717

<!-- b000608 | prose | pages [37, 38] -->
关注数学模型 2005/1 4 0.87 0/31 4467 2005/1 5 0.99 1/30 25 2005/1 2 -0.57 2/31 07 2006/1 3.294 0.25 /31 118 3166 2006/2 3.857 0.48 /28 143 14 2006/3 3.177 0.29 /31 083 0946 2006/4 3.156 0.35 /30 25 2928 2006/5 3.115 0.60 /31 385 2631 2006/6 1 -0.42 /30 15 2006/7 3.634 0.31 /31 921 9398 2006/8 3.384 0.12 /31 615 6777 2006/9 3.291 0.51 /30 667 0772 2006/1 3.533 0.44 0/31 333 5201 2006/1 3.793 0.31 1/30 333 3961 2006/1 3.378 0.29 2/31 788 0235 2007/1 5 0.98 /31 68 2007/2 4.5 0.92 /28 94 2007/3 5 0.94 /31 59 2007/4 3.177 0.29 /30 083 0946 2007/5 3.156 0.35 /31 25 2928 2007/6 5 0.86 /30 13 2007/7 4 0.68 /31 08

<!-- b000609 | furniture | pages [37] -->
2

<!-- b000610 | furniture | pages [37] -->
MATHmodels

<!-- b000611 | furniture | pages [37] -->
获取更多资讯

<!-- b000612 | furniture | pages [38] -->
Team # 2010638                                                                   Page 15 of 20

<!-- b000614 | prose | pages [38, 39] -->
关注数学模型 2007/8 3 0.58 /31 66 2007/9 4 -0.55 /30 29 2007/1 2.364 -0.08 0/31 583 993 2007/1 4.5 0.70 1/30 06 2007/1 5 0.97 2/31 7667 2008/1 2.364 -0.08 /31 583 993 2008/2 3.666 -0.28 /29 667 567 2008/3 3 0.67 /31 05 2008/4 2 -0.51 /30 06 2008/5 3.4 0.41 /31 524 2008/6 2.865 0.36 /30 385 0717 2008/7 2.666 -0.13 /31 667 823 2008/8 3.666 0.79 /31 667 5633 2008/9 2.364 -0.08 /30 583 993 2008/1 3.433 0.17 0/31 333 2403 2008/1 2.364 -0.08 1/30 583 993 2008/1 4 0.63 2/31 69 2009/1 3.1 0.22 /31 467 2009/2 3 0.21 /28 4 2009/3 2.865 0.36 /31 385 0717 2009/4 5 0.92 /30 57 2009/5 2.25 0.08 /31 9067

<!-- b000615 | furniture | pages [38] -->
2

<!-- b000616 | furniture | pages [38] -->
MATHmodels

<!-- b000617 | furniture | pages [38] -->
获取更多资讯

<!-- b000618 | furniture | pages [39] -->
Team # 2010638                                                                   Page 16 of 20

<!-- b000620 | prose | pages [39, 40] -->
关注数学模型 2009/6 5 0.49 /30 495 2009/7 1 -0.85 /31 16 2009/8 1 0 /31

<!-- b000621 | furniture | pages [39] -->
2

<!-- b000622 | furniture | pages [39] -->
MATHmodels

<!-- b000623 | furniture | pages [39] -->
获取更多资讯

<!-- b000624 | furniture | pages [40] -->
Team # 2010638                                                                   Page 17 of 20

<!-- b000626 | heading | pages [40] -->
Appendix 5

<!-- b000627 | heading | pages [40] -->
1. Code of LDA model

<!-- b000628 | prose | pages [40] -->
import pandas as pd from snownlp import SnowNLP import re from gensim import corpora,models #from nltk.tokenize import word_tokenize data = pd.DataFrame(test2) print(type(data)) #data_null = data.drop_duplicates() #data_null.to_csv(&apos;C:/Users/lenovo/Desktop/comments_null.csv&apos;) #data_null_comments = data_null[&apos;contents&apos;] #data_null_comments.to_csv(&apos;C:/Users/lenovo/Desktop/contents.txt&apos;,index=False,enco ding=&apos;utf-8&apos;) #data_len = data_null_comments[data_null_comments.str.len()>4] #print(data_len) #data_len.to_csv(&apos;contents.txt&apos;,index=False,encoding=&apos;utf-8&apos;) coms = [] coms = data[0].apply(lambda x:SnowNLP(x).sentiments) data_post = data[coms>=0.01] data_neg = data[coms<0.01] print(data_post) print(data_neg) data_post[0].to_csv(&apos;C:/Users/lenovo/Desktop/comments_positive.txt&apos;,encoding=&apos ;utf-8&apos;,header=None) data_neg[0].to_csv(&apos;C:/Users/lenovo/Desktop/comments_negative.txt&apos;,encoding=&apos ;utf-8-sig&apos;,header=None) with open(&apos;C:/Users/lenovo/Desktop/comments_positive.txt&apos;,encoding=&apos;utf-8&ap os;) as fn1: string_data1 = fn1.read() pattern = re.compile(u&apos;\t|\n|\.|-|——|：|！|、|，|,|。|;|\)|\(|\?|"&apos;) string_data1 = re.sub(pattern, &apos;&apos;, string_data1) print(string_data1) fp = open(&apos;C:/Users/lenovo/Desktop/comments_post.txt&apos;,&apos;a&apos;,encoding =&apos;utf8&apos;)

<!-- b000629 | prose | pages [40, 41] -->
关注数学模型 fp.write(string_data1 + &apos;\n&apos;) fp.close() with open(&apos;C:/Users/lenovo/Desktop/comments_nagative.txt&apos;,encoding=&apos;utf-8&a pos;) as fn2: string_data2 = fn2.read() pattern = re.compile(u&apos;\t|\n|\.|-|——|：|！|、|，|,|。|;|\)|\(|\?|"&apos;) string_data2 = re.sub(pattern, &apos;&apos;, string_data2) print(string_data2) fp = open(&apos;C:/Users/lenovo/Desktop/comments_neg.txt&apos;,&apos;a&apos;,encoding =&apos;utf8&apos;) fp.write(string_data2 + &apos;\n&apos;) fp.close() data1 = pd.read_csv(&apos;C:/Users/lenovo/Desktop/comments_post.txt&apos;,encoding=&apos;utf -8&apos;,header=None) data2 = pd.read_csv(&apos;C:/Users/lenovo/Desktop/comments_neg.txt&apos;,encoding=&apos;utf -8&apos;,header=None) #mycut = lambda s: &apos; &apos;.join(word_tokenize(s)) #data1 = data1[0].apply(mycut) #data2 = data2[0].apply(mycut) #mycut = lambda s: &apos; &apos;.join(word_tokenize(s)) data1 = data1[0] data2 = data2[0] data1.to_csv(&apos;C:/Users/lenovo/Desktop/comments_post_cut.txt&apos;,index=False,header=Fa lse,encoding=&apos;utf-8&apos;) data2.to_csv(&apos;C:/Users/lenovo/Desktop/comments_neg_cut.txt&apos;,index=False,header=Fal se,encoding=&apos;utf-8&apos;) print(data2) post = pd.read_csv(&apos;C:/Users/lenovo/Desktop/comments_post_cut.txt&apos;,encoding=&apos ;utf-8&apos;,header=None,error_bad_lines=False) neg = pd.read_csv(&apos;C:/Users/lenovo/Desktop/comments_neg_cut.txt&apos;,encoding=&apos; utf-8&apos;,header=None,error_bad_lines=False) stop = pd.read_csv(&apos;C:/Users/lenovo/Desktop/stoplist.txt&apos;,encoding=&apos;utf-8&apos; ,header=None,sep=&apos;tipdm&apos;,engine=&apos;python&apos;) stop = [&apos; &apos;,&apos;&apos;] + list(stop[0]) post[1] = post[0].apply(lambda s: s.split(&apos; &apos;)) post[2] = post[1].apply(lambda x: [i for i in x if i not in stop]) neg[1] = neg[0].apply(lambda s: s.split(&apos; &apos;)) neg[2] = neg[1].apply(lambda x: [i for i in x if i not in stop]) post_dict = corpora.Dictionary(post[2]) post_corpus = [post_dict.doc2bow(i) for i in post[2]] post_lda = models.LdaModel(post_corpus, num_topics=4, id2word=post_dict) for i in range(3): print(post_lda.print_topic(i)) print(&apos)

<!-- b000630 | furniture | pages [40] -->
2

<!-- b000631 | furniture | pages [40] -->
MATHmodels

<!-- b000632 | furniture | pages [40] -->
获取更多资讯

<!-- b000633 | furniture | pages [41] -->
Team # 2010638                                                                   Page 18 of 20

<!-- b000635 | prose | pages [41, 42] -->
关注数学模型 neg_dict = corpora.Dictionary(neg[2]) neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]] neg_lda = models.LdaModel(neg_corpus, num_topics=4, id2word=neg_dict) for i in range(3): print(neg_lda.print_topic(i))

<!-- b000636 | furniture | pages [41] -->
2

<!-- b000637 | furniture | pages [41] -->
MATHmodels

<!-- b000638 | furniture | pages [41] -->
获取更多资讯

<!-- b000639 | furniture | pages [42] -->
Team # 2010638                                                                   Page 19 of 20

<!-- b000641 | heading | pages [42] -->
2. Code of word segmentation and NLTK model

<!-- b000642 | prose | pages [42] -->
import pandas as pd import seaborn as sns import numpy as np from nltk.tokenize import word_tokenize,sent_tokenize import matplotlib.pyplot as plt pacifier=pd.read_csv(&apos;C:/Users/lenovo/Desktop/pacifier.tsv&apos;, sep=&apos;\t&apos;) b = pacifier[&apos;review_body&apos;].duplicated() pacifier[&apos;marketplace&apos;] = pacifier[&apos;marketplace&apos;].str.lower() pacifier[&apos;product_category&apos;] = pacifier[&apos;product_category&apos;].str.lower() pacifier[&apos;vine&apos;] = pacifier[&apos;vine&apos;].str.lower() pacifier[&apos;verified_purchase&apos;] = pacifier[&apos;verified_purchase&apos;].str.lower() text_a_count = [] for i in pacifier[&apos;review_body&apos;]: if isinstance(i,str): print(i,type(i)) print(len(i)) elif isinstance(i,float): print(i,type(i)) i = str(i) text_a_count.append(len(i)) #plt.figure(figsize = (8,6)) u = pacifier[&apos;helpful_votes&apos;] x = np.array(text_a_count) y = np.array(u) p = pd.DataFrame({&apos;review_body_length&apos;:x,&apos;helpful_votes&apos;:y}) #p = p.drop_duplicates([&apos;helpful_votes&apos;]) #color = [&apos;r&apos;,&apos;y&apos;,&apos;k&apos;,&apos;g&apos;,&apos;m&apos;] #plt.scatter(p[&apos;review_body_length&apos;],p[&apos;helpful_votes&apos;],c=color,marker=& apos;>&apos;) #plt.legend() #plt.show() v = pacifier.describe() import pandas as pd import nltk import numpy as np from nltk.tokenize import word_tokenize,sent_tokenize pacifier=pd.read_excel(&apos;C:/Users/lenovo/Desktop

<!-- b000643 | prose | pages [42, 43] -->
关注数学模型 /pacifier_lower.xlsx&apos;, sep=&apos;\t&apos;) b = pacifier[&apos;review_body&apos;].duplicated() test11 = pacifier.groupby(&apos;product_parent&apos;).sum() pacifier[&apos;marketplace&apos;] = pacifier[&apos;marketplace&apos;].str.lower() pacifier[&apos;product_category&apos;] = pacifier[&apos;product_category&apos;].str.lower() pacifier[&apos;vine&apos;] =pacifier[&apos;vine&apos;].str.lower() pacifier[&apos;verified_purchase&apos;] = pacifier[&apos;verified_purchase&apos;].str.lower() test2 = pacifier[&apos;review_body&apos;].tolist() text_a_count = [] text_b_count = [] for sent in test2: words = word_tokenize(sent) text_b_count.append(words) for word in words: if word.isalpha() == False: words.remove(word) text_a_count.append(len(words)) counts1 = {} for word in words: counts1[word] = counts1.get(word,0) + 1 items = list(counts1.items()) items.sort(key=lambda x:x[1], reverse=True) for i in range(len(items)): word, count1 = items[i] print ("{0:<10}{1:>5}".format(word, count1)) from collections import Counter import pandas as pd import numpy as np c={"counts" : text_a_count, "split" : text_b_count} data=pd.DataFrame(c) w = Counter(text_a_count) print(w) w1 = set(text_a_count) print(text_a_count) w2 = w.most_common(len(w)) m = [] for i in range(305): m.append(list(w2[i])) df = pd.DataFrame(m, columns=[&apos;number&apos;, &apos;count&apos;]) color = [&apos;r&apos;,&apos;y&apos;,&apos;k&apos;,&apos;g&apos;,&apos;m&apos;] plt.scatter(df[&apos;number&apos;],df[&apos;count&apos;],c=color,marker=&apos;>&apos;) plt.legend() plt.show()

<!-- b000644 | furniture | pages [42] -->
2

<!-- b000645 | furniture | pages [42] -->
MATHmodels

<!-- b000646 | furniture | pages [42] -->
获取更多资讯

<!-- b000647 | furniture | pages [43] -->
Team # 2010638                                                                   Page 20 of 20

<!-- b000649 | prose | pages [43] -->
关注数学模型

<!-- b000650 | furniture | pages [43] -->
2

<!-- b000651 | furniture | pages [43] -->
MATHmodels

<!-- b000652 | furniture | pages [43] -->
获取更多资讯
