# P-C-2020-2010638-c32c8549

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | prose | pages [1] -->
2020

<!-- b000003 | prose | pages [1] -->
Problem Chosen

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | title | pages [1] -->
2010638

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | heading | pages [1] -->
Sales Strategy Recommendation Based on Commodity Data Mining

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
We conduct data analysis and information mining from the following four aspects: correlation between review, star rating and helpfulness rating, product brand rating, prediction of product’s reputation and impact of star rating on reviews, so as to propose reliable sales strategies and suggestions for product improvement.

<!-- b000013 | prose | pages [1] -->
Firstly, after data pre-processing, We perform word segmentation and preliminary sentiment analysis on the text data through the NLTK tool, and quantify it as emotion score, ranging from [-1,1].We adopt the methods of data visualization, descriptive statistics and correlation analysis, and further construct a multivariate Logistic regression model to analyze the relationship between helpfulness rating and review length, star rating and compound. The results show that helpfulness rating has an inverted "U-type" relationship with review length and a positive "U-type" relationship with star rating.

<!-- b000014 | prose | pages [1] -->
The next step, we conduct analysis based on the rating and evaluation model. The LDA analysis model is constructed to find the topic feature of each product, based on which we can propose suggestions for improvement of products. At the same time, we summarize five indexes that affect the product sales from the topic features, namely quality, price, appearance, service and size. Then a computer search algorithm based on the text similarity is used to calculate the index score of each review. In addition, we combine the score with the analytic hierarchy process to determine the weight of each index and build a weighted brand scoring system. Finally, we cluster all product brands through systematic clustering to select potential high-quality brands and recommend them to sunshine company.

<!-- b000015 | prose | pages [1] -->
Further, we calculate the comprehensive score of review and star rating, and take it as the product’s reputation, which is conducive to forecast the future reputation of three products through time series analysis. And it depicts that the three products have seasonal characteristics and will probably maintain a stable seasonal cycle in the near future. However, the peak time of reputation comprehensive score of the three products is discrepant, and further analysis illustrates that the product sales figure is larger during the peak period of reputation score, according to which sunshine company can make a sales plan.

<!-- b000016 | prose | pages [1] -->
Finally, we analyze the relationship between star rating and review. Through the establishment of distributed lag model, it is found that customers' reviews in the current period will be affected by other customers' ratings and reviews. Meanwhile, we observe the time-varying synchrony between emotional score and star rating, which is clear that reviews containing positive words result in higher star ratings, while reviews containing negative words result in lower star ratings. In other words, there is a strong correlation between star ratings and specific quality descriptors.

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | keywords | pages [1] -->
Key words: correlation analysis, multinomial logistic regression, natural language processing,

<!-- b000019 | prose | pages [1] -->
time series analysis

<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | prose | pages [1] -->
关注数学模型

<!-- b000022 | furniture | pages [1] -->
2

<!-- b000023 | furniture | pages [1] -->
MATHmodels

<!-- b000024 | furniture | pages [1] -->
获取更多资讯

<!-- b000025 | furniture | pages [2] -->
Team # 2010638                                                                   Page 1 of 20

<!-- b000026 | prose | pages [2] -->
Content

<!-- b000027 | prose | pages [2] -->
1. INTRODUCTION ......................................................................................................................................... 2

<!-- b000028 | prose | pages [2] -->
1.1 Background ............................................................................................................................................... 2 1.2 Problems Restatement ............................................................................................................................... 2

<!-- b000029 | prose | pages [2] -->
2. ASSUMPTIONS AND NOMENCLATURE .............................................................................................. 3

<!-- b000030 | prose | pages [2] -->
2.1 Assumptions ........................................................................................................................................ 3 2.2 Nomenclature ....................................................................................................................................... 3

<!-- b000031 | prose | pages [2] -->
3.

<!-- b000032 | prose | pages [2] -->
MODEL 1-ANALYSIS OF STAR RATING, HELPFULNESS RATING AND REVIEW .................. 4

<!-- b000033 | prose | pages [2] -->
3.1 Data Pre-processing .................................................................................................................................. 4 3.2 Word Segmentation and Sentiment Analysis ............................................................................................ 5 3.3 Data Description and Visual Analysis ....................................................................................................... 6 3.4 Correlation Analysis ................................................................................................................................. 7 3.5 Multinomial Logistic Regression Model .................................................................................................. 7

<!-- b000034 | prose | pages [2] -->
4.

<!-- b000035 | prose | pages [2] -->
MODEL 2-ESTABLISH A SCORING SYSTEM TO DETERMINE PRODUCT POSITIONING ... 9

<!-- b000036 | prose | pages [2] -->
4.1 LDA Model ............................................................................................................................................... 9 4.2 Determine index score ............................................................................................................................. 11 4.3 Analytic hierarchy process (AHP) .......................................................................................................... 12 4.3.1 The introduction of analytic hierarchy process .............................................................. 12 4.3.2 AHP Consistency Test .................................................................................................... 13 4.3.3 Results of AHP ............................................................................................................... 13 4.4 System Clustering Analysis ..................................................................................................................... 14 4.4.1 Model establishment ....................................................................................................... 14 4.4.2 Classification results ....................................................................................................... 14

<!-- b000037 | prose | pages [2] -->
5.

<!-- b000038 | prose | pages [2] -->
MODEL 3-TIME SERIES ANALYSIS .................................................................................................. 15

<!-- b000039 | prose | pages [2] -->
6.

<!-- b000040 | prose | pages [2] -->
MODEL 4-DISTRIBUTED LAG MODEL ........................................................................................... 17

<!-- b000041 | prose | pages [2] -->
6.1 Distributed lag model .............................................................................................................................. 17 6.2 Almon Method ........................................................................................................................................ 18 6.3 Correlation Analysis between Star Rating and Comments ..................................................................... 18

<!-- b000042 | prose | pages [2] -->
7.

<!-- b000043 | prose | pages [2] -->
SENSITIVITY ANALYSIS ..................................................................................................................... 19

<!-- b000044 | prose | pages [2] -->
8.

<!-- b000045 | prose | pages [2] -->
MODEL ASSESSMENT ......................................................................................................................... 20

<!-- b000046 | prose | pages [2] -->
8.1 Strengths ................................................................................................................................................. 20 8.2 Weaknesses ............................................................................................................................................. 20

<!-- b000047 | prose | pages [2] -->
REFERENCE .................................................................................................................................................. 20

<!-- b000048 | prose | pages [2] -->
LETTER ............................................................................................................................................................. 1

<!-- b000049 | prose | pages [2] -->
APPENDIX ........................................................................................................................................................ 1

<!-- b000050 | furniture | pages [2] -->


<!-- b000051 | furniture | pages [2] -->


<!-- b000052 | prose | pages [2] -->
关注数学模型

<!-- b000053 | furniture | pages [2] -->
2

<!-- b000054 | furniture | pages [2] -->
MATHmodels

<!-- b000055 | furniture | pages [2] -->
获取更多资讯

<!-- b000056 | furniture | pages [3] -->
Team # 2010638                                                                   Page 2 of 20

<!-- b000057 | heading | pages [3] -->
1. Introduction

<!-- b000058 | heading | pages [3] -->
1.1 Background

<!-- b000059 | prose | pages [3] -->
With the popularization and development of the Internet, online sales are gradually replacing offline sales and occupy a major position in the sales industry. The transformation of sales mode will also be a huge challenge for commodity companies. Analyzing and mining market information and consumer feedback has become the key of network marketing.

<!-- b000060 | prose | pages [3] -->
The online marketplace created by Amazon provides an opportunity for customers to evaluate their purchases. Customers can use quantities from 1 (low rating, low satisfaction) to 5 (high rating, high satisfaction) to express their satisfaction with the product. In addition, customers can submit their own reviews on the products to express their opinions. Other customers can use these reviews to gain an initial understanding of the product before purchasing it, and to distinguish between the reviews (called "helpfulness ratings") that are helpful or not. The data will be fed back to the company which can use the data to conduct in-depth analysis of the markets, determine the timing of their participation, and modify products based on customer suggestions.

<!-- b000061 | heading | pages [3] -->
1.2 Problems Restatement

<!-- b000062 | prose | pages [3] -->
Sunshine Company plans to launch and sell microwave ovens, hair dryers and baby pacifiers in the online marketplace. In order to understand these three commodity markets and develop sales strategies, it is necessary to analyze the customer feedback data. We will accomplish the following tasks according to the given data:

<!-- b000063 | prose | pages [3] -->
(1) Develop sales strategy for sunshine company. (2) Identify potential important design features that would enhance product desirability. In order to accomplish the above two tasks, our specific work is as follows:  Analyze the relationship between star rating, helpful vote and review.  Make in-depth analysis of reviews and ratings, and distinguish the advantages and disadvantages of products, so as to make suggestions for product improvement.  Establish a product rating system based on the analysis of reviews and ratings, and select high-quality brand products to recommend to Sunshine Company for sales.  Establish the reputation scoring system and predict the development trend of reputation.  Analyze whether current reviews are influenced by prior star ratings and reviews.  Analyze whether specific quality descriptors of text-based reviews strongly associated with rating levels.

<!-- b000064 | furniture | pages [3] -->


<!-- b000065 | prose | pages [3] -->
关注数学模型

<!-- b000066 | furniture | pages [3] -->
2

<!-- b000067 | furniture | pages [3] -->
MATHmodels

<!-- b000068 | furniture | pages [3] -->
获取更多资讯

<!-- b000069 | furniture | pages [4] -->
Team # 2010638                                                                   Page 3 of 20

<!-- b000070 | furniture | pages [4] -->


<!-- b000071 | caption | pages [4] -->
Figure 1: The Flow Chart in This Paper

<!-- b000072 | heading | pages [4] -->
2. Assumptions and Nomenclature

<!-- b000073 | heading | pages [4] -->
2.1 Assumptions

<!-- b000074 | prose | pages [4] -->
We make several assumptions in our model. Later we may relax some of these assumptions to optimize our model making it more applicable in the complex reality environment.

<!-- b000075 | prose | pages [4] -->
 All reviews are from customers and there is no automated review.  There is no deliberate attempt to smear the product in customer rating and review.  Unverified orders are not sold on Amazon. The sum of confirmed sales in the data set is total sales.  The review of members certified by Amazon Vine has high credibility.

<!-- b000076 | heading | pages [4] -->
2.2 Nomenclature

<!-- b000077 | heading | pages [4] -->
Symbols

<!-- b000078 | prose | pages [4] -->
SS

<!-- b000079 | prose | pages [4] -->
Definition

<!-- b000080 | prose | pages [4] -->
Star ratings squared

<!-- b000081 | prose | pages [4] -->
The number of words in each review. count

<!-- b000082 | prose | pages [4] -->
CS The number of words squared

<!-- b000083 | prose | pages [4] -->
compound Emotional score

<!-- b000084 | prose | pages [4] -->
The percentage of helpful votes in the total votes. H r

<!-- b000085 | prose | pages [4] -->
The weight of the iw thi index

<!-- b000086 | prose | pages [4] -->
Total score of six indexes(quality、size、service、 SQ

<!-- b000087 | prose | pages [4] -->
price、appearance、star ratings)

<!-- b000088 | prose | pages [4] -->
Total score of product reputation SR

<!-- b000089 | furniture | pages [4] -->


<!-- b000090 | prose | pages [4] -->
关注数学模型

<!-- b000091 | furniture | pages [4] -->
2

<!-- b000092 | furniture | pages [4] -->
MATHmodels

<!-- b000093 | furniture | pages [4] -->
获取更多资讯

<!-- b000094 | furniture | pages [5] -->
Team # 2010638                                                                   Page 4 of 20

<!-- b000095 | heading | pages [5] -->
3.  Model 1-Analysis of Star rating, Helpfulness rating and Review

<!-- b000096 | heading | pages [5] -->
3.1 Data Pre-processing

<!-- b000097 | prose | pages [5] -->
Before data analysis, the availability of data must be guaranteed. No measures, regardless of its value, can provide accurate assessments if based on unreliable data. We first remove useless information including product title, marketplace and product category, on the basis of which we can carry out data pre-processing.

<!-- b000098 | prose | pages [5] -->
To ameliorate the condition of data set, there are four steps: data classification, data cleaning, information filtration, set-up of new attribute and data-measuring, as shown in the figure.

<!-- b000099 | furniture | pages [5] -->


<!-- b000100 | caption | pages [5] -->
Figure 2: Data Pre-processing Flow Chart

<!-- b000101 | prose | pages [5] -->
Step 1: Firstly, divide the data into numeric and textual types and process them separately. Step 2: In the stage of data cleaning, initially we check the missing value by using the “duplicated () method” in python, while no item with a missing value was found.

<!-- b000102 | prose | pages [5] -->
Step 3: Outlier processing is mainly used in the text data. Take the pacifier as an example, it includes the

<!-- b000103 | prose | pages [5] -->
following contents:

<!-- b000104 | prose | pages [5] -->
 ，❤， Processing non-alphabetic text data. There are some non-alphabetic data like:

<!-- b000105 | prose | pages [5] -->
,They ，

<!-- b000106 | prose | pages [5] -->
can't be recognized by a computer program, while their emotional inclination can be intuitively identified by us. As a result, we transform all of them into "five stars”, so as to facilitate the later computer programming.  Spelling correction. Generally, English text may contain spelling errors, so a spelling check is required. Based on “PyEnchant library” in python program, all the review texts are checked and corrected.  Lowercase: the computer will react differently to the two texts: “Five stars” and “five stars”, whereas we expect them to be the same word when we count them. Therefore, we unify all text data to lowercase characters.

<!-- b000107 | furniture | pages [5] -->


<!-- b000108 | prose | pages [5] -->
Step 4: After the above steps, our data set has become more acceptable, but when we look more closely at the review content, we find that a lot of the review content is irrelevant to the product and can be regarded as redundant information, such as:

<!-- b000109 | furniture | pages [5] -->


<!-- b000110 | prose | pages [5] -->
关注数学模型

<!-- b000111 | furniture | pages [5] -->
2

<!-- b000112 | furniture | pages [5] -->
MATHmodels

<!-- b000113 | furniture | pages [5] -->
获取更多资讯

<!-- b000114 | furniture | pages [6] -->
Team # 2010638                                                                   Page 5 of 20

<!-- b000115 | prose | pages [6] -->
 “good cleaning cloths”  “I bought hits basket to store magazines and newspapers. It looks very nice in our room”  “I received this blanket as a gift from my mom and have never felt anything so soft.” Take the pacifier as an example, reviews that have nothing to do with the pacifier is needed to be weeded out. We identify the redundant information according to the text similarity, and the process is as follows:

<!-- b000116 | prose | pages [6] -->
The product review is regarded as a set of words, and the feature vector of the text is established by calculating the number of each word in the text. Afterwards, the cosine similarity between vectors is used to calculate the similarity between texts. If the average similarity between a review and others is less than the threshold value set by us, the review is removed.

<!-- b000117 | furniture | pages [6] -->


<!-- b000118 | prose | pages [6] -->
Step 5:Set-up of new attribute. To better analyze the usefulness of reviews, we establish a new attribute

<!-- b000119 | prose | pages [6] -->
named helpfulness rating (Hr), which is obtained by dividing “helpful votes” by “total votes”

<!-- b000120 | heading | pages [6] -->
3.2 Word Segmentation and Sentiment Analysis

<!-- b000121 | prose | pages [6] -->
Although the text data has been initially processed aforementioned, the information from reviews is s till needed to assess.However, the review data is unstructured and requires a different mechanism to ex tract the information. Emotion analysis or opinion mining is the process of computing to identify wh ether the author's attitude towards a text is positive, negative or neutral. For the review data, we con ducted a preliminary Sentiment analysis through data mining to determine and quantify the emotional inclination of each review, and further analysis will be discussed in the following questions. Based on this, NLTK (natural language toolkit),which is a leading platform that is able to work with human langu age data by python program, is used for sentiment analysis.

<!-- b000122 | prose | pages [6] -->
A basic sentiment analysis model is built in Python 3 using the NLTK library. The preprocessin g is operated by marking the text, normalizing the words, and removing the noise. Next, the NTLK emotional analyzer is used to build a model and associate the text with a specific emotion and quant ify it.

<!-- b000123 | furniture | pages [6] -->


<!-- b000124 | caption | pages [6] -->
Figure 3: Implementation process

<!-- b000125 | furniture | pages [6] -->


<!-- b000126 | prose | pages [6] -->
关注数学模型

<!-- b000127 | furniture | pages [6] -->
2

<!-- b000128 | furniture | pages [6] -->
MATHmodels

<!-- b000129 | furniture | pages [6] -->
获取更多资讯

<!-- b000130 | furniture | pages [7] -->
Team # 2010638                                                                   Page 6 of 20

<!-- b000131 | heading | pages [7] -->
3.3 Data Description and Visual Analysis

<!-- b000132 | prose | pages [7] -->
The table below describes the total, average and variance of the star rating of these three products. The average of the helpful votes and the number of the words in the review are also calculated. The figures below describe their distribution.

<!-- b000133 | caption | pages [7] -->
Table 1: Data Statistic

<!-- b000134 | prose | pages [7] -->
Star rating

<!-- b000135 | prose | pages [7] -->
Descriptive

<!-- b000136 | prose | pages [7] -->
Star rating Total

<!-- b000137 | prose | pages [7] -->
Helpful votes

<!-- b000138 | prose | pages [7] -->
Count Count

<!-- b000139 | prose | pages [7] -->
variance

<!-- b000140 | prose | pages [7] -->
statistics

<!-- b000141 | prose | pages [7] -->
average

<!-- b000142 | prose | pages [7] -->
average average 1.19043 Pacifier 18939 4.30456 0.827182 4841870 256 1.64524 Microwave oven 1615 3.44458 5.62167 748130 463 1.30033 Hair dryer 11470 4.11604

<!-- b000143 | furniture | pages [7] -->


<!-- b000144 | prose | pages [7] -->
2.17908 3268716 285

<!-- b000145 | furniture | pages [7] -->


<!-- b000146 | caption | pages [7] -->
Figure 4: Box Figure        Figure 5: Stacked Barplot     Figure 6:Star Rating Distributon

<!-- b000147 | furniture | pages [7] -->


<!-- b000148 | prose | pages [7] -->
The data is visualized to dig into the inherent rules, which is helpful for modeling. The figures below describe the relationship between the helpfulness rating, and star ratings, review length and emotional score.

<!-- b000149 | furniture | pages [7] -->


<!-- b000150 | furniture | pages [7] -->


<!-- b000151 | caption | pages [7] -->
Figure 7:Heat Map of Correlation

<!-- b000152 | prose | pages [7] -->
Note: sr represents “star rating”; cp represents “compound”; ct represents “count”; hr represents “helpfulness rating”

<!-- b000153 | furniture | pages [7] -->


<!-- b000154 | prose | pages [7] -->
The darker the color in the figure is, the greater the correlation between the two indicators will be. We can find that the emotional score and star ratings has a strong correlation in the three figures. The helpfulness rating and the review length has a light correlation.

<!-- b000155 | furniture | pages [7] -->


<!-- b000156 | prose | pages [7] -->
关注数学模型

<!-- b000157 | furniture | pages [7] -->
2

<!-- b000158 | furniture | pages [7] -->
MATHmodels

<!-- b000159 | furniture | pages [7] -->
获取更多资讯

<!-- b000160 | furniture | pages [8] -->
Team # 2010638                                                                   Page 7 of 20

<!-- b000161 | heading | pages [8] -->
3.4 Correlation Analysis

<!-- b000162 | prose | pages [8] -->
H ), star ratings, the We apply the methods of correlation analysis on the percentage of helpful votes ( r number of words in each review (count) and emotional score (compound)., which is measured by Pearson correlation coefficient is as follows:

<!-- b000163 | prose | pages [8] -->
n

<!-- b000164 | prose | pages [8] -->


<!-- b000165 | prose | pages [8] -->


<!-- b000166 | prose | pages [8] -->
(X

<!-- b000167 | prose | pages [8] -->
i

<!-- b000168 | prose | pages [8] -->


<!-- b000169 | prose | pages [8] -->


<!-- b000170 | prose | pages [8] -->
i

<!-- b000171 | prose | pages [8] -->
1

<!-- b000172 | prose | pages [8] -->
r

<!-- b000173 | furniture | pages [8] -->


<!-- b000174 | prose | pages [8] -->
n

<!-- b000175 | prose | pages [8] -->


<!-- b000176 | prose | pages [8] -->


<!-- b000177 | prose | pages [8] -->
(

<!-- b000178 | prose | pages [8] -->
X X

<!-- b000179 | prose | pages [8] -->
)

<!-- b000180 | prose | pages [8] -->
i

<!-- b000181 | prose | pages [8] -->


<!-- b000182 | prose | pages [8] -->
i

<!-- b000183 | prose | pages [8] -->
1

<!-- b000184 | furniture | pages [8] -->


<!-- b000185 | prose | pages [8] -->


<!-- b000186 | prose | pages [8] -->
X)(Y Y)

<!-- b000187 | prose | pages [8] -->
i

<!-- b000188 | prose | pages [8] -->
(1)

<!-- b000189 | prose | pages [8] -->
n

<!-- b000190 | prose | pages [8] -->


<!-- b000191 | prose | pages [8] -->


<!-- b000192 | prose | pages [8] -->
2 2 2

<!-- b000193 | prose | pages [8] -->
(

<!-- b000194 | prose | pages [8] -->
Y Y

<!-- b000195 | prose | pages [8] -->
)

<!-- b000196 | prose | pages [8] -->
i

<!-- b000197 | prose | pages [8] -->


<!-- b000198 | prose | pages [8] -->
i

<!-- b000199 | prose | pages [8] -->
1

<!-- b000200 | prose | pages [8] -->
iY represents the helpfulness rating,. X , X represents the star rating, review length, emotional score, etc. i H and star Y represents the average number of these indexes. The r is the correlation coefficient between rating, count, compound, etc.

<!-- b000201 | prose | pages [8] -->
The results of the correlation analysis are

<!-- b000202 | prose | pages [8] -->
r

<!-- b000203 | caption | pages [8] -->
Table 2: Correlation Coefficient

<!-- b000204 | prose | pages [8] -->
Correlation

<!-- b000205 | prose | pages [8] -->
Correlation coefficient(Hair

<!-- b000206 | prose | pages [8] -->
Index

<!-- b000207 | prose | pages [8] -->
coefficient(Microwave

<!-- b000208 | prose | pages [8] -->
oven)

<!-- b000209 | prose | pages [8] -->
star rating -0.149** count -0.071** compound -0.024**

<!-- b000210 | prose | pages [8] -->
Correlation

<!-- b000211 | prose | pages [8] -->
dryer)

<!-- b000212 | prose | pages [8] -->
coefficient(Pacifier)

<!-- b000213 | prose | pages [8] -->
-0.138** -0.151** 0.356** 0.332** 0.057** -0.101** Note: ** means the result is significant at 0.01 level (two-side test)

<!-- b000214 | prose | pages [8] -->
From the table above we can see that, for the three data sets, there is a significant correlation between

<!-- b000215 | prose | pages [8] -->
H and star rating, count and compound (all of which are significant in the two-tailed test), which is r consistent with the results of visual analysis. More concretely, the star rating and emotional score of H . The counts of hair dryer and microwave oven, hair dryer and pacifier are negatively correlated with r H , while the counts of microwave oven are negatively correlated with pacifier are positively correlated with r

<!-- b000216 | prose | pages [8] -->
H . Besides, there is a negative correlation between the compound of microwave oven, pacifier and r H , r H is positive. while the correlation between the compound of hair dryer and r

<!-- b000217 | heading | pages [8] -->
3.5 Multinomial Logistic Regression Model

<!-- b000218 | prose | pages [8] -->
Multinomial logistic regression model is adopted to further analyze the impact of star rating, review length and emotional score on the helpfulness rating. In fact, the helpfulness rating is the cumulative result of each consumer’s voting (yes or no) . Therefore, the number of helpful votes is subject to binomial distribution, and logistic model is suitable for empirical analysis of such kind of data.

<!-- b000219 | prose | pages [8] -->
X in Multivariate logistic regression can determine the role and intensity of the explanatory variable n predicting the probability of occurrence of strain Y. Suppose X is the response variable and P is the response probability of the model, and the corresponding regression model is as follows:

<!-- b000220 | prose | pages [8] -->
p

<!-- b000221 | prose | pages [8] -->
k

<!-- b000222 | prose | pages [8] -->
 

<!-- b000223 | prose | pages [8] -->


<!-- b000224 | prose | pages [8] -->


<!-- b000225 | prose | pages [8] -->
1

<!-- b000226 | prose | pages [8] -->
ln( )

<!-- b000227 | furniture | pages [8] -->


<!-- b000228 | prose | pages [8] -->


<!-- b000229 | prose | pages [8] -->
1

<!-- b000230 | prose | pages [8] -->
p

<!-- b000231 | prose | pages [8] -->


<!-- b000232 | prose | pages [8] -->
k

<!-- b000233 | prose | pages [8] -->
1

<!-- b000234 | prose | pages [8] -->
  p P (y 1| x ,x , ,x )

<!-- b000235 | prose | pages [8] -->
 x

<!-- b000236 | prose | pages [8] -->
(2)

<!-- b000237 | prose | pages [8] -->
k ki

<!-- b000238 | prose | pages [8] -->
1 1

<!-- b000239 | prose | pages [8] -->
x ,x , ,x is the possibility that case i happens in case the values of 1 i 1 i 2 i ki are 1 i 2 i ki 1p is a binomial distribution parameter, which is the probability that a review receives a helpful given. Also x represents a series of independent variables. β is the corresponding estimation coefficient, and α is vote.

<!-- b000240 | prose | pages [8] -->
ki the intercept, which reflects the random effect at the product level.

<!-- b000241 | furniture | pages [8] -->


<!-- b000242 | prose | pages [8] -->
关注数学模型

<!-- b000243 | furniture | pages [8] -->
2

<!-- b000244 | furniture | pages [8] -->
MATHmodels

<!-- b000245 | furniture | pages [8] -->
获取更多资讯

<!-- b000246 | furniture | pages [9] -->
Team # 2010638                                                                   Page 8 of 20

<!-- b000247 | prose | pages [9] -->
The probability of an event happening of an event is a non-linear function composed of the explanatory variable Xi . Here is the expression:

<!-- b000248 | prose | pages [9] -->
   

<!-- b000249 | prose | pages [9] -->
exp( X

<!-- b000250 | prose | pages [9] -->


<!-- b000251 | prose | pages [9] -->
1 1

<!-- b000252 | prose | pages [9] -->
p

<!-- b000253 | furniture | pages [9] -->


<!-- b000254 | prose | pages [9] -->
  

<!-- b000255 | heading | pages [9] -->
1 exp(

<!-- b000256 | prose | pages [9] -->
X

<!-- b000257 | prose | pages [9] -->
1

<!-- b000258 | prose | pages [9] -->
   

<!-- b000259 | prose | pages [9] -->
X ...

<!-- b000260 | prose | pages [9] -->
X )

<!-- b000261 | prose | pages [9] -->
2 2

<!-- b000262 | prose | pages [9] -->
n n

<!-- b000263 | prose | pages [9] -->
(3)      

<!-- b000264 | prose | pages [9] -->
X ...

<!-- b000265 | prose | pages [9] -->
X )

<!-- b000266 | prose | pages [9] -->
1 1 2 2

<!-- b000267 | prose | pages [9] -->
n n

<!-- b000268 | prose | pages [9] -->
On top of these 3 indexes, we introduce two additional variables: star rating square(SQ) and review length square(CS) in order to further explore the influence of star rating and review length on the helpfulness ratings of reviews.

<!-- b000269 | prose | pages [9] -->
Meanwhile, considering the impact of whether the customers are vine members and whether the purchase is verified on the authenticity and validity of reviews, we take these two indicators as independent variables.

<!-- b000270 | prose | pages [9] -->
Independent variables are divided into three levels, which represent the intuitive evaluation (star rating, star rating square) respectively, characteristics of review content (review length, review length square, emotional score), and reviewers characteristics (vine, VP), to explore the various reasons that affect the helpfulness ratings in detail.

<!-- b000271 | prose | pages [9] -->
As for dependent variables, we divide them into four categories according to their numerical values, namely:

<!-- b000272 | furniture | pages [9] -->


<!-- b000273 | prose | pages [9] -->
  

<!-- b000274 | prose | pages [9] -->
1,0.75

<!-- b000275 | prose | pages [9] -->


<!-- b000276 | prose | pages [9] -->
compound

<!-- b000277 | prose | pages [9] -->
1

<!-- b000278 | prose | pages [9] -->
 

<!-- b000279 | prose | pages [9] -->
2,0.50

<!-- b000280 | prose | pages [9] -->
 

<!-- b000281 | prose | pages [9] -->
helpfulness ratings

<!-- b000282 | furniture | pages [9] -->


<!-- b000283 | furniture | pages [9] -->


<!-- b000284 | prose | pages [9] -->
compound

<!-- b000285 | prose | pages [9] -->
0.75

<!-- b000286 | prose | pages [9] -->
(4)

<!-- b000287 | prose | pages [9] -->
 

<!-- b000288 | prose | pages [9] -->
3,0.25

<!-- b000289 | prose | pages [9] -->
 

<!-- b000290 | prose | pages [9] -->
4,0

<!-- b000291 | prose | pages [9] -->


<!-- b000292 | prose | pages [9] -->
compound

<!-- b000293 | prose | pages [9] -->
0.50

<!-- b000294 | prose | pages [9] -->
 

<!-- b000295 | prose | pages [9] -->
compound

<!-- b000296 | prose | pages [9] -->
0.25

<!-- b000297 | prose | pages [9] -->
The independent variables are divided into blocks and do regression analysis respectively. The independent variables in models 1, 2 and 3 and the regression coefficients obtained by SPSS are summarized as Table.For reasons of space, the results of hair dryer and pacifier are included in the appendix.

<!-- b000298 | prose | pages [9] -->
independent

<!-- b000299 | prose | pages [9] -->
Abbreviations

<!-- b000300 | furniture | pages [9] -->


<!-- b000301 | prose | pages [9] -->
variables

<!-- b000302 | prose | pages [9] -->
star rating star rating

<!-- b000303 | prose | pages [9] -->
Intuitive

<!-- b000304 | prose | pages [9] -->
star rating

<!-- b000305 | prose | pages [9] -->
SS

<!-- b000306 | prose | pages [9] -->
evaluation

<!-- b000307 | prose | pages [9] -->
square

<!-- b000308 | prose | pages [9] -->
review length count review length

<!-- b000309 | prose | pages [9] -->
Characteristics

<!-- b000310 | prose | pages [9] -->
CS square

<!-- b000311 | prose | pages [9] -->
of review

<!-- b000312 | prose | pages [9] -->
emotional

<!-- b000313 | prose | pages [9] -->
content

<!-- b000314 | prose | pages [9] -->
compound score

<!-- b000315 | prose | pages [9] -->
vine vine

<!-- b000316 | prose | pages [9] -->
Reviewers’

<!-- b000317 | prose | pages [9] -->
verified

<!-- b000318 | prose | pages [9] -->
verified

<!-- b000319 | prose | pages [9] -->
characteristics

<!-- b000320 | prose | pages [9] -->
purchase

<!-- b000321 | prose | pages [9] -->
purchase

<!-- b000322 | heading | pages [9] -->
Model 1

<!-- b000323 | heading | pages [9] -->
Model 2

<!-- b000324 | heading | pages [9] -->
Model 3

<!-- b000325 | prose | pages [9] -->
0.213** 0.469** 0.423**

<!-- b000326 | prose | pages [9] -->
0.314** 0.207** 0.110**

<!-- b000327 | furniture | pages [9] -->


<!-- b000328 | prose | pages [9] -->
-0.020** -0.019**

<!-- b000329 | furniture | pages [9] -->


<!-- b000330 | prose | pages [9] -->
0.002** 0.002**

<!-- b000331 | furniture | pages [9] -->


<!-- b000332 | prose | pages [9] -->
-0.146** -0.160**

<!-- b000333 | furniture | pages [9] -->


<!-- b000334 | furniture | pages [9] -->


<!-- b000335 | prose | pages [9] -->
0.033**

<!-- b000336 | furniture | pages [9] -->


<!-- b000337 | furniture | pages [9] -->


<!-- b000338 | prose | pages [9] -->
0.398**

<!-- b000339 | caption | pages [9] -->
Table 3: Index and regression coefficient

<!-- b000340 | prose | pages [9] -->
Note:*: p<0.05; **: p<0.01; +: p<0.1; ns: not significant

<!-- b000341 | furniture | pages [9] -->


<!-- b000342 | prose | pages [9] -->
It is clear from the above table, each variable passed the significance test. The regression coefficients of star ratings of microwave oven, hair dryer and pacifier are all positive, and the regression coefficients of star rating square terms are also positive. It indicates that there is a "U-type” relationship between star ratings and

<!-- b000343 | furniture | pages [9] -->


<!-- b000344 | prose | pages [9] -->
关注数学模型

<!-- b000345 | furniture | pages [9] -->
2

<!-- b000346 | furniture | pages [9] -->
MATHmodels

<!-- b000347 | furniture | pages [9] -->
获取更多资讯

<!-- b000348 | furniture | pages [10] -->
Team # 2010638                                                                   Page 9 of 20

<!-- b000349 | prose | pages [10] -->
the helpfulness ratings of reviews, which is contrary to the research conclusions of Mudambi and Schuff [8]. Our analysis suggests that the reviewers who score higher or lower star ratings may be more willing to express a clear attitude towards the products, so as to provide more valuable reviews; while the reviewers who give intermediate star ratings may lack reference value due to their less distinctive attitude.

<!-- b000350 | furniture | pages [10] -->


<!-- b000351 | prose | pages [10] -->
Based on model 1, review length, review length square and emotion score are added into the model. From the data in the table, it is clear that the regression coefficient of the review length term is negative, while one of the square term of the review length is positive, which indicates that the review length and helpfulness rating are of an inverted-U-type. According to our analysis, reviews that are too short are often limited in content and cannot provide sufficient useful information. However, overlong reviews may provide a lot of valuable information though, other customers may not be patient to spend time and energy reading them. Therefore, reviews with high helpfulness ratings should be of moderate length.

<!-- b000352 | furniture | pages [10] -->


<!-- b000353 | prose | pages [10] -->
On the basis of model 2, in model 3 we introduce other reviewer-related features such as Vine and Verified Purchase. It can be seen that most customers are not vine members and many purchase are not verified in the sample data, thus it is difficult to analyze and draw valuable conclusions about these two indicators. In spite of this, they make the model more complete and more applicable.

<!-- b000354 | heading | pages [10] -->
4.  Model 2-Establish a Scoring System to Determine Product

<!-- b000355 | prose | pages [10] -->
Positioning

<!-- b000356 | prose | pages [10] -->
According to the three data sets, each product has hundreds of different brands. If sunshine company hopes to enter the market of microwave oven, hair dryer and pacifier, it is of great significance to accurately grasp the market positioning of each brand. The market positioning of different brands is mainly determined by the star rating and review from customers. The processing of star rating is relatively simple, so we mainly process text of customers’ reviews in detail.

<!-- b000357 | heading | pages [10] -->
4.1 LDA Model

<!-- b000358 | prose | pages [10] -->
Latent Dirichlet Allocation is a generative thematic model proposed by Blei et al [2] in 2003. It is also known as three-tier Bayesian probability model with three-tier structure of document (d), topic (z) and word (W), which can effectively model the text. Based on LDA topic model, we are able to mine the potential topics in the data set, and then analyze the main information of the data sets and related feature words.

<!-- b000359 | caption | pages [10] -->
Table 4:Symbol Explanation

<!-- b000360 | prose | pages [10] -->
，

<!-- b000361 | prose | pages [10] -->
，

<!-- b000362 | furniture | pages [10] -->


<!-- b000363 | prose | pages [10] -->
prior parameters of the Dirichlet function

<!-- b000364 | prose | pages [10] -->
the parameter of the topic's multiple

<!-- b000365 | prose | pages [10] -->
distribution in the document.

<!-- b000366 | prose | pages [10] -->
LDA model assumes that each review is randomly mixed by each subject according to a certain proportion. And the mixing proportion is subject to multiple distribution, which is recorded as follows:

<!-- b000367 | prose | pages [10] -->


<!-- b000368 | furniture | pages [10] -->


<!-- b000369 | prose | pages [10] -->
                  (5) Multionmial Z | =

<!-- b000370 | furniture | pages [10] -->


<!-- b000371 | prose | pages [10] -->
( )

<!-- b000372 | prose | pages [10] -->
关注数学模型

<!-- b000373 | furniture | pages [10] -->
2

<!-- b000374 | furniture | pages [10] -->
MATHmodels

<!-- b000375 | furniture | pages [10] -->
获取更多资讯

<!-- b000376 | furniture | pages [11] -->
Team # 2010638                                                                   Page 10 of 20

<!-- b000377 | prose | pages [11] -->
Each topic is made up of the words in the glossary in a certain proportion, and the proportion of the mixture is also subject to multiple distribution.

<!-- b000378 | prose | pages [11] -->
 

<!-- b000379 | furniture | pages [11] -->


<!-- b000380 | prose | pages [11] -->
W Z | ,  (6) Multionmial ( )

<!-- b000381 | prose | pages [11] -->
d , the probability of generating word Under the condition of review j

<!-- b000382 | prose | pages [11] -->
K

<!-- b000383 | prose | pages [11] -->
 

<!-- b000384 | furniture | pages [11] -->


<!-- b000385 | prose | pages [11] -->
P w

<!-- b000386 | prose | pages [11] -->
( |

<!-- b000387 | prose | pages [11] -->
d

<!-- b000388 | prose | pages [11] -->
)

<!-- b000389 | prose | pages [11] -->
P w

<!-- b000390 | prose | pages [11] -->
(

<!-- b000391 | prose | pages [11] -->
j j

<!-- b000392 | prose | pages [11] -->


<!-- b000393 | prose | pages [11] -->
i

<!-- b000394 | prose | pages [11] -->
1

<!-- b000395 | prose | pages [11] -->
 P w z ( | s ) is the probability that the word i th the probability that the s topic is in the review.

<!-- b000396 | prose | pages [11] -->
iw is expressed as:

<!-- b000397 | prose | pages [11] -->
   (7)

<!-- b000398 | prose | pages [11] -->
|

<!-- b000399 | prose | pages [11] -->
z s

<!-- b000400 | prose | pages [11] -->
)

<!-- b000401 | prose | pages [11] -->
P z

<!-- b000402 | prose | pages [11] -->
(

<!-- b000403 | prose | pages [11] -->
s d

<!-- b000404 | prose | pages [11] -->
| )

<!-- b000405 | prose | pages [11] -->
i i j

<!-- b000406 | prose | pages [11] -->
 iw belongs to the th s topic.

<!-- b000407 | prose | pages [11] -->
indicates P z ( s d | ) j

<!-- b000408 | prose | pages [11] -->
After sentiment analysis based on LDA , the review text is gathered into three topics, as a result 10 most frequently used words and their corresponding probability are generated under each topic. Table 5 shows the potential topics in the positive evaluation text of microwave ovens, and the other one depicts the negative evaluation. Considering the limited space of the article, we put the results of hair dryer and pacifier in the appendix.

<!-- b000409 | caption | pages [11] -->
Table 5:Microwave Oven Positive Topics

<!-- b000410 | prose | pages [11] -->
Theme 1 Theme 2 Theme 3 great good well well great great like well good good use use no small size

<!-- b000411 | furniture | pages [11] -->


<!-- b000412 | prose | pages [11] -->
Theme 1 Theme 2 Theme 3 product product small space no nice price price easy use nice product like like like

<!-- b000413 | caption | pages [11] -->
Table 6:Microwave Oven Negative Topics

<!-- b000414 | furniture | pages [11] -->


<!-- b000415 | prose | pages [11] -->
Theme 1 Theme 2 Theme 3

<!-- b000416 | furniture | pages [11] -->


<!-- b000417 | prose | pages [11] -->
new no like use use new easy like use no more service like new time Theme 1 Theme 2 Theme 3 time time no more service old product great more

<!-- b000418 | heading | pages [11] -->
model

<!-- b000419 | prose | pages [11] -->
small small service good well

<!-- b000420 | prose | pages [11] -->
According to the extraction of three potential subject words for positive and negative evaluation, we can determine the customer's attitudes towards 5 aspects of microwave oven characteristics.

<!-- b000421 | furniture | pages [11] -->


<!-- b000422 | furniture | pages [11] -->


<!-- b000423 | furniture | pages [11] -->


<!-- b000424 | furniture | pages [11] -->


<!-- b000425 | furniture | pages [11] -->


<!-- b000426 | furniture | pages [11] -->


<!-- b000427 | furniture | pages [11] -->


<!-- b000428 | furniture | pages [11] -->


<!-- b000429 | furniture | pages [11] -->


<!-- b000430 | furniture | pages [11] -->


<!-- b000431 | caption | pages [11] -->
Figure 8:Index of Microwave Oven                   Figure 9:Word Cloud

<!-- b000432 | furniture | pages [11] -->


<!-- b000433 | furniture | pages [11] -->


<!-- b000434 | prose | pages [11] -->
关注数学模型

<!-- b000435 | furniture | pages [11] -->
2

<!-- b000436 | furniture | pages [11] -->
MATHmodels

<!-- b000437 | furniture | pages [11] -->
获取更多资讯

<!-- b000438 | furniture | pages [12] -->
Team # 2010638                                                                   Page 11 of 20

<!-- b000439 | prose | pages [12] -->
These high-frequency words in reviews can also reflect the focus of customers when purchasing microwave ovens, that is the quality, price, size, service and appearance. These five indicators can reflect a product comprehensively. We conduct the same analysis on pacifiers and hair dryers, then it is found that these five indicators can also be taken as the criteria to consider whether they are worth purchasing.

<!-- b000440 | prose | pages [12] -->
Taking the quality, price, size, service, appearance and star rating as the evaluation indexes, we establish a scoring system to comprehensively evaluate these 3 product sold in the current market, so as to obtain the accurate market positioning of each brand of products, and then formulate a good sales strategy for sunshine company.

<!-- b000441 | prose | pages [12] -->
The steps of our brand scoring system are as below:

<!-- b000442 | furniture | pages [12] -->


<!-- b000443 | prose | pages [12] -->
• Determine the quality, price, size, service,

<!-- b000444 | furniture | pages [12] -->


<!-- b000445 | prose | pages [12] -->
appearance and star rating of each parent

<!-- b000446 | prose | pages [12] -->
Step1

<!-- b000447 | furniture | pages [12] -->


<!-- b000448 | furniture | pages [12] -->


<!-- b000449 | prose | pages [12] -->
• The weights of quality, price, size, service,

<!-- b000450 | furniture | pages [12] -->


<!-- b000451 | prose | pages [12] -->
appearance and star rating in comprehensive

<!-- b000452 | prose | pages [12] -->
Step2

<!-- b000453 | furniture | pages [12] -->


<!-- b000454 | prose | pages [12] -->
evaluation are obtained by AHP

<!-- b000455 | furniture | pages [12] -->


<!-- b000456 | prose | pages [12] -->
• The final score of each index is the weights

<!-- b000457 | furniture | pages [12] -->


<!-- b000458 | prose | pages [12] -->
mentioned above multiplied by the scores

<!-- b000459 | prose | pages [12] -->
Step3

<!-- b000460 | furniture | pages [12] -->


<!-- b000461 | furniture | pages [12] -->


<!-- b000462 | prose | pages [12] -->
• According to the scores of each index, use Q-

<!-- b000463 | furniture | pages [12] -->


<!-- b000464 | prose | pages [12] -->
cluster to grade the parent

<!-- b000465 | prose | pages [12] -->
Step4

<!-- b000466 | furniture | pages [12] -->


<!-- b000467 | furniture | pages [12] -->


<!-- b000468 | furniture | pages [12] -->


<!-- b000469 | heading | pages [12] -->
4.2 Determine index score

<!-- b000470 | prose | pages [12] -->
After implementing LDA algorithm, complex network is introduced to calculate the importance degree of each review. We use traversing search algorithm to implement the process, through which we can get weighted average score of each topic feature for all products. Here is the algorithm:

<!-- b000471 | furniture | pages [12] -->


<!-- b000472 | furniture | pages [12] -->


<!-- b000473 | prose | pages [12] -->
关注数学模型

<!-- b000474 | furniture | pages [12] -->
2

<!-- b000475 | furniture | pages [12] -->
MATHmodels

<!-- b000476 | furniture | pages [12] -->
获取更多资讯

<!-- b000477 | furniture | pages [13] -->
Team # 2010638                                                                   Page 12 of 20

<!-- b000478 | heading | pages [13] -->
4.3 Analytic hierarchy process (AHP)

<!-- b000479 | heading | pages [13] -->
4.3.1 The introduction of analytic hierarchy process

<!-- b000480 | prose | pages [13] -->
Analytic hierarchy process (AHP) can be used deeply analyze the essence, influencing factors and their internal relations of complex decision problems. It makes use of less quantitative information to make the thinking process of decision mathematical, so as to provide a simple method for complex decision problems. AHP can decompose the evaluation criteria into different hierarchical structures, and then calculate the weight of each factor by solving the eigenvectors of judgment matrix.

<!-- b000481 | prose | pages [13] -->
According to the LDA model, the indicators we extracted are quality, appearance, price, size and service satisfaction level. Now we construct the judgment matrix of the first-level evaluation index:

<!-- b000482 | prose | pages [13] -->


<!-- b000483 | prose | pages [13] -->
W W W

<!-- b000484 | prose | pages [13] -->
1 1 1

<!-- b000485 | prose | pages [13] -->


<!-- b000486 | prose | pages [13] -->
W W W

<!-- b000487 | prose | pages [13] -->


<!-- b000488 | prose | pages [13] -->
1 2 3

<!-- b000489 | prose | pages [13] -->


<!-- b000490 | prose | pages [13] -->
W W W

<!-- b000491 | prose | pages [13] -->
2 2 2

<!-- b000492 | prose | pages [13] -->


<!-- b000493 | prose | pages [13] -->
W W W

<!-- b000494 | prose | pages [13] -->


<!-- b000495 | prose | pages [13] -->
1 2 3

<!-- b000496 | prose | pages [13] -->


<!-- b000497 | prose | pages [13] -->
W W W

<!-- b000498 | prose | pages [13] -->
3 3 3

<!-- b000499 | prose | pages [13] -->


<!-- b000500 | prose | pages [13] -->
W W W

<!-- b000501 | prose | pages [13] -->


<!-- b000502 | prose | pages [13] -->
1 2 3

<!-- b000503 | prose | pages [13] -->


<!-- b000504 | furniture | pages [13] -->


<!-- b000505 | prose | pages [13] -->
A W W W

<!-- b000506 | prose | pages [13] -->
4 4 4

<!-- b000507 | prose | pages [13] -->


<!-- b000508 | prose | pages [13] -->
W W W

<!-- b000509 | prose | pages [13] -->


<!-- b000510 | prose | pages [13] -->
1 2 3

<!-- b000511 | prose | pages [13] -->


<!-- b000512 | prose | pages [13] -->
W W W

<!-- b000513 | prose | pages [13] -->


<!-- b000514 | prose | pages [13] -->
5 5 5

<!-- b000515 | prose | pages [13] -->
W W W

<!-- b000516 | prose | pages [13] -->


<!-- b000517 | prose | pages [13] -->
1 2 3

<!-- b000518 | prose | pages [13] -->


<!-- b000519 | prose | pages [13] -->
W W W

<!-- b000520 | prose | pages [13] -->


<!-- b000521 | prose | pages [13] -->
6 6 6

<!-- b000522 | prose | pages [13] -->


<!-- b000523 | prose | pages [13] -->
W W W

<!-- b000524 | prose | pages [13] -->


<!-- b000525 | prose | pages [13] -->
1 2 3

<!-- b000526 | prose | pages [13] -->
Calculate the product of the elements:

<!-- b000527 | prose | pages [13] -->
 n M a

<!-- b000528 | furniture | pages [13] -->


<!-- b000529 | prose | pages [13] -->
 i i 1

<!-- b000530 | prose | pages [13] -->
M : Take the NTH root of i

<!-- b000531 | prose | pages [13] -->
W

<!-- b000532 | furniture | pages [13] -->


<!-- b000533 | prose | pages [13] -->
Calculate the eigenvector:

<!-- b000534 | prose | pages [13] -->
W

<!-- b000535 | prose | pages [13] -->
i

<!-- b000536 | furniture | pages [13] -->


<!-- b000537 | prose | pages [13] -->
Calculate the maximum eigenvalue：

<!-- b000538 | prose | pages [13] -->


<!-- b000539 | prose | pages [13] -->
W W W

<!-- b000540 | prose | pages [13] -->
1 1 1

<!-- b000541 | prose | pages [13] -->


<!-- b000542 | prose | pages [13] -->
W W W

<!-- b000543 | prose | pages [13] -->


<!-- b000544 | prose | pages [13] -->
4 5 6

<!-- b000545 | prose | pages [13] -->


<!-- b000546 | prose | pages [13] -->
W W W

<!-- b000547 | prose | pages [13] -->
2 2 2

<!-- b000548 | prose | pages [13] -->


<!-- b000549 | prose | pages [13] -->
W W W

<!-- b000550 | prose | pages [13] -->


<!-- b000551 | prose | pages [13] -->
4 5 6

<!-- b000552 | prose | pages [13] -->


<!-- b000553 | prose | pages [13] -->
W W W

<!-- b000554 | prose | pages [13] -->
3 3 3

<!-- b000555 | prose | pages [13] -->


<!-- b000556 | prose | pages [13] -->
W W W

<!-- b000557 | prose | pages [13] -->


<!-- b000558 | prose | pages [13] -->
4 5 6

<!-- b000559 | prose | pages [13] -->
(8)

<!-- b000560 | prose | pages [13] -->


<!-- b000561 | prose | pages [13] -->
W W W

<!-- b000562 | prose | pages [13] -->
4 4 4

<!-- b000563 | prose | pages [13] -->


<!-- b000564 | prose | pages [13] -->
W W W

<!-- b000565 | prose | pages [13] -->


<!-- b000566 | prose | pages [13] -->
4 5 6

<!-- b000567 | prose | pages [13] -->


<!-- b000568 | prose | pages [13] -->
W W W

<!-- b000569 | prose | pages [13] -->


<!-- b000570 | prose | pages [13] -->
5 5 5

<!-- b000571 | prose | pages [13] -->
W W W

<!-- b000572 | prose | pages [13] -->


<!-- b000573 | prose | pages [13] -->
4 5 6

<!-- b000574 | prose | pages [13] -->


<!-- b000575 | prose | pages [13] -->
W W W

<!-- b000576 | prose | pages [13] -->


<!-- b000577 | prose | pages [13] -->
6 6 6

<!-- b000578 | prose | pages [13] -->


<!-- b000579 | prose | pages [13] -->
W W W

<!-- b000580 | prose | pages [13] -->


<!-- b000581 | prose | pages [13] -->
4 5 7

<!-- b000582 | prose | pages [13] -->
 ( ( i i 1,2,3,4,5,6) (9) ij ij

<!-- b000583 | prose | pages [13] -->
  M (10) n i i i

<!-- b000584 | prose | pages [13] -->
W

<!-- b000585 | prose | pages [13] -->
 

<!-- b000586 | prose | pages [13] -->
i

<!-- b000587 | prose | pages [13] -->
n

<!-- b000588 | prose | pages [13] -->
（11） 

<!-- b000589 | prose | pages [13] -->
W

<!-- b000590 | prose | pages [13] -->
j

<!-- b000591 | prose | pages [13] -->


<!-- b000592 | prose | pages [13] -->
j

<!-- b000593 | prose | pages [13] -->
1

<!-- b000594 | prose | pages [13] -->
(

<!-- b000595 | prose | pages [13] -->
AW

<!-- b000596 | prose | pages [13] -->
) n 1 1

<!-- b000597 | prose | pages [13] -->


<!-- b000598 | prose | pages [13] -->


<!-- b000599 | furniture | pages [13] -->


<!-- b000600 | prose | pages [13] -->
max

<!-- b000601 | prose | pages [13] -->
 

<!-- b000602 | prose | pages [13] -->
T W

<!-- b000603 | prose | pages [13] -->
=

<!-- b000604 | prose | pages [13] -->
W W W W W W

<!-- b000605 | prose | pages [13] -->
Where

<!-- b000606 | furniture | pages [13] -->


<!-- b000607 | prose | pages [13] -->
1 2 3 4 5 6

<!-- b000608 | furniture | pages [13] -->


<!-- b000609 | prose | pages [13] -->
i

<!-- b000610 | prose | pages [13] -->
（12）

<!-- b000611 | prose | pages [13] -->
n n W

<!-- b000612 | prose | pages [13] -->


<!-- b000613 | prose | pages [13] -->
i

<!-- b000614 | prose | pages [13] -->
1

<!-- b000615 | prose | pages [13] -->
i

<!-- b000616 | prose | pages [13] -->
关注数学模型

<!-- b000617 | furniture | pages [13] -->
2

<!-- b000618 | furniture | pages [13] -->
MATHmodels

<!-- b000619 | furniture | pages [13] -->
获取更多资讯

<!-- b000620 | furniture | pages [14] -->
Team # 2010638                                                                   Page 13 of 20

<!-- b000621 | heading | pages [14] -->
4.3.2 AHP Consistency Test

<!-- b000622 | prose | pages [14] -->
After the judgment matrix is constructed, the relative weight of each element in two levels is calculated by the judgment matrix, and the consistency test is carried out. It is not allowed for the judgment to deviate too much from the consistency, so the consistency test of the judgment matrix is needed. The specific test steps are as follows:

<!-- b000623 | prose | pages [14] -->
Step1: Calculated consistency indexCI :

<!-- b000624 | prose | pages [14] -->
CI

<!-- b000625 | furniture | pages [14] -->


<!-- b000626 | furniture | pages [14] -->


<!-- b000627 | prose | pages [14] -->


<!-- b000628 | prose | pages [14] -->


<!-- b000629 | prose | pages [14] -->
n

<!-- b000630 | prose | pages [14] -->
 

<!-- b000631 | prose | pages [14] -->
max

<!-- b000632 | prose | pages [14] -->
(13)

<!-- b000633 | prose | pages [14] -->


<!-- b000634 | prose | pages [14] -->
n

<!-- b000635 | prose | pages [14] -->
1

<!-- b000636 | prose | pages [14] -->
Step2:Check the criteria for testing the consistency of the judgement matrix from the relevant data

<!-- b000637 | prose | pages [14] -->
RI (n )

<!-- b000638 | furniture | pages [14] -->


<!-- b000639 | caption | pages [14] -->
Table 7: Relation Between RI and n

<!-- b000640 | prose | pages [14] -->
n 1 2 3 4 RI 0 0 0.52 0.89 5 6 7 8 9 1.12 1.26 1.36 1.41 1.46 Note: if the consistency ratio is less than 0.1, the judgment matrix of AHP has satisfactory consistency

<!-- b000641 | prose | pages [14] -->
Step3:Calculate the random consistency ratio of the judgment matrixCR ：

<!-- b000642 | prose | pages [14] -->
CR 

<!-- b000643 | furniture | pages [14] -->


<!-- b000644 | furniture | pages [14] -->


<!-- b000645 | prose | pages [14] -->
CI 1                       (14) RI

<!-- b000646 | prose | pages [14] -->
If the consistency ratio is less than 0.1, the judgement matrix of AHP has satisfactory consistency, namely its consistency degree is acceptable.

<!-- b000647 | heading | pages [14] -->
4.3.3 Results of AHP

<!-- b000648 | prose | pages [14] -->
After the sentiment analysis based on LDA , we screened out 5 indexes with significant influence, and combined with the star ratings, there were 6 evaluation indexes. The judgment matrix of each index is given by the expert scoring method to reflect its relative critical degree. According to the result of data processing, the judgment matrix of these indexes has passed the consistency test, which is shown in the appendix.

<!-- b000649 | caption | pages [14] -->
Table 8:Index judgment matrix

<!-- b000650 | furniture | pages [14] -->


<!-- b000651 | prose | pages [14] -->
quality appearance quality 1 2 appearance 0.5 1 price 1 1 size 0.5 1 service 0.5 0.5 price size service star ratings 1 2 2 1 1 1 2 1 1 2 1 1 0.5 1 0.5 1 1 2 1 0.5

<!-- b000652 | caption | pages [14] -->
Table 9:Evaluation Index and Weight

<!-- b000653 | prose | pages [14] -->
appearance

<!-- b000654 | furniture | pages [14] -->


<!-- b000655 | prose | pages [14] -->
quality Weight(microwave oven) 0.21 0.13 Weight(hair dryer) 0.22 0.14 Weight(pacifier) 0.28 0.27

<!-- b000656 | furniture | pages [14] -->


<!-- b000657 | furniture | pages [14] -->


<!-- b000658 | furniture | pages [14] -->


<!-- b000659 | furniture | pages [14] -->


<!-- b000660 | furniture | pages [14] -->


<!-- b000661 | furniture | pages [14] -->


<!-- b000662 | prose | pages [14] -->
price size service star ratings 0.20 0.13 0.13 0.20 0.21 0.10 0.13 0.20 0.10 0.15 0.10 0.10

<!-- b000663 | prose | pages [14] -->
关注数学模型

<!-- b000664 | furniture | pages [14] -->
2

<!-- b000665 | furniture | pages [14] -->
MATHmodels

<!-- b000666 | furniture | pages [14] -->
获取更多资讯

<!-- b000667 | furniture | pages [15] -->
Team # 2010638                                                                   Page 14 of 20

<!-- b000668 | heading | pages [15] -->
4.4 System Clustering Analysis

<!-- b000669 | heading | pages [15] -->
4.4.1 Model establishment

<!-- b000670 | prose | pages [15] -->
Cluster analysis is a method of classification step by step. Its main idea is to reasonably merge and classify the research objects according to certain similarity indexes. It is called system clustering when it is used to solve the classification problem of samples and R-clustering when it is used to solve the classification problem of variables. We mainly uses cluster analysis to solve the problem of brand classification and evaluation. According to the observation indexes (star rating, quality, service, appearance, price, size) and system clustering algorithm of different brands, it calculates the similarity degree between brands, and classifies the similar brands into one category and the different brands into another. The closely related to a small classification unit, the not closely related to a large classification unit.

<!-- b000671 | furniture | pages [15] -->


<!-- b000672 | prose | pages [15] -->
In a word, the result of system clustering analysis is to form a large to small classification pedigree or cluster diagram. Clustering graph can not only intuitively represent the similarity relationship and classification among the research objects, but also reflect all kinds of brands and quantitatively indicate the degree of similarity, so as to provide a good basis for the comprehensive evaluation.

<!-- b000673 | furniture | pages [15] -->


<!-- b000674 | prose | pages [15] -->
Distance coefficient is a common statistic in system cluster analysis. If n brands observed on m variables kx can jx and are regarded as n points in m dimension space, the similarity between any two brands points be expressed by the distance between two points in m dimension space, then the distance coefficient is defined as:

<!-- b000675 | prose | pages [15] -->
1

<!-- b000676 | prose | pages [15] -->
  d

<!-- b000677 | prose | pages [15] -->
[

<!-- b000678 | furniture | pages [15] -->


<!-- b000679 | prose | pages [15] -->
jk m i

<!-- b000680 | prose | pages [15] -->
1

<!-- b000681 | prose | pages [15] -->
m m

<!-- b000682 | prose | pages [15] -->


<!-- b000683 | prose | pages [15] -->
2

<!-- b000684 | prose | pages [15] -->
(x x ) ]

<!-- b000685 | prose | pages [15] -->
(15)

<!-- b000686 | prose | pages [15] -->
2

<!-- b000687 | prose | pages [15] -->
ij ik  

<!-- b000688 | prose | pages [15] -->
1 1

<!-- b000689 | prose | pages [15] -->
Similarity coefficient is a measure of similarity between brands. Each brand is regarded as a vector of kx is defined as the cosine of the jx and m-dimensional space, and the similarity between two brands angle between two vectors, that is

<!-- b000690 | prose | pages [15] -->


<!-- b000691 | prose | pages [15] -->


<!-- b000692 | prose | pages [15] -->
cos

<!-- b000693 | furniture | pages [15] -->


<!-- b000694 | prose | pages [15] -->
jk

<!-- b000695 | heading | pages [15] -->
4.4.2 Classification results

<!-- b000696 | prose | pages [15] -->
m

<!-- b000697 | prose | pages [15] -->


<!-- b000698 | prose | pages [15] -->
x x

<!-- b000699 | prose | pages [15] -->
ij ik

<!-- b000700 | prose | pages [15] -->


<!-- b000701 | prose | pages [15] -->
i

<!-- b000702 | prose | pages [15] -->
1

<!-- b000703 | prose | pages [15] -->
(16)

<!-- b000704 | prose | pages [15] -->
m m m

<!-- b000705 | prose | pages [15] -->
 

<!-- b000706 | prose | pages [15] -->
2 2

<!-- b000707 | prose | pages [15] -->
x x

<!-- b000708 | prose | pages [15] -->
ij ij

<!-- b000709 | prose | pages [15] -->
  

<!-- b000710 | prose | pages [15] -->
i i

<!-- b000711 | prose | pages [15] -->
1

<!-- b000712 | prose | pages [15] -->
i

<!-- b000713 | prose | pages [15] -->
1

<!-- b000714 | prose | pages [15] -->
We use SPSS to cluster different parents and divide them into 10 grades. The first-class products are the best, and the tenth class products are the worst. In our sales strategy, we will recommend the first-class brands with better response in the sales market of sunshine company. Limited to space, only 5 first-class brands of each product are listed in the text.

<!-- b000715 | caption | pages [15] -->
Table 10:Part of Classification results

<!-- b000716 | prose | pages [15] -->
Microwave oven 862802057 423421857 Hair dryer 244516305 266176173 Pacifier 22060147 22189989 692404913 464779766 423421857 468944538 741916038 112413045 51496920 62352351 79207704 Note: The number in the table corresponds to the product parent.

<!-- b000717 | furniture | pages [15] -->


<!-- b000718 | prose | pages [15] -->
关注数学模型

<!-- b000719 | furniture | pages [15] -->
2

<!-- b000720 | furniture | pages [15] -->
MATHmodels

<!-- b000721 | furniture | pages [15] -->
获取更多资讯

<!-- b000722 | furniture | pages [16] -->
Team # 2010638                                                                   Page 15 of 20

<!-- b000723 | heading | pages [16] -->
5. Model 3-Time Series Analysis

<!-- b000724 | prose | pages [16] -->
In this section, we construct a time series analysis model to analyze microwave reputation, hair dryer reputation and pacifier reputation. Afterwards the product reputation could be predicted after analyzing the reviews and star ratings about the products.

<!-- b000725 | prose | pages [16] -->
The product reputation is consisted with star rating and emotional inclination. According to statist ics, the customers are apt to pay more attention to the reviews when they buy goods, so the review shows greater impact on the product reputation than the star rating. Because of this, we assign 70% weight to the average emotional score and 30% weight to the average star rating. The sum of them is the comprehensive score of product reputation.

<!-- b000726 | prose | pages [16] -->
Due to hypotheses, the product reputation score will be influenced by autocorrelation in time seri th p -order Auto-Regression Model to fit curve, namely AR(p). es. As a consequence, we choose

<!-- b000727 | prose | pages [16] -->
   Y a Y a Y ...

<!-- b000728 | furniture | pages [16] -->


<!-- b000729 | prose | pages [16] -->
  n 1 n 1 2 n 2     a a Y (17)  p n p n

<!-- b000730 | prose | pages [16] -->
Where Y represents the product reputation score in year n.

<!-- b000731 | prose | pages [16] -->
  a a represent the influential coefficients of different lag orders. 1 p

<!-- b000732 | prose | pages [16] -->
 represents the error term whose mean value is 0 and variance is n

<!-- b000733 | prose | pages [16] -->
2 )

<!-- b000734 | prose | pages [16] -->
Noise Process WN(0, .The distribution matches White 2

<!-- b000735 | prose | pages [16] -->
Firstly, we collected the time series data of three products’ reputation scores. Then we solve the auto-regession model of the reputation score and calculate the time-series autocorrelation function and partial autocorrelation function of the reputation scores to identify the order, and specifically calculated the parameter

<!-- b000736 | prose | pages [16] -->
p .

<!-- b000737 | prose | pages [16] -->
The sequence correlation of the comprehensive scores of each product's reputation depicts an obvious autoregressive structure AR1, which means the involved functions don’t possess the property of truncation, and the partial functions possess the property of truncation. Therefore, we conclude that p=1 and the reputation score of all the three products share the same model setting.

<!-- b000738 | prose | pages [16] -->
    N N

<!-- b000739 | furniture | pages [16] -->


<!-- b000740 | prose | pages [16] -->
1 t 1 t t (18)

<!-- b000741 | prose | pages [16] -->
1and the error term is different from the reputation The mean variance of the coefficient

<!-- b000742 | prose | pages [16] -->
changing. By calculation, we apply the MLE to estimate the coefficient of these three products.

<!-- b000743 | heading | pages [16] -->
Here we list the results:

<!-- b000744 | caption | pages [16] -->
Table 11: ARE Model for Different Products

<!-- b000745 | prose | pages [16] -->
AR（1） product  R 2 P-Value

<!-- b000746 | prose | pages [16] -->
0.046 Hair dryer 0.125 0.007 0.901 0.043 pacifier 0.054 0.021 0.930 0.050 Microwave oven -0.075 0.000 0.952 It is clear that the results of coefficients testing are significant, meanwhile the overall fitting gets a good result with a high R-squared.

<!-- b000747 | prose | pages [16] -->
Afterwards we conduct over-fitting and under fitting test, which contributes to the accuracy of p=1.The test uses the Algorithm of information guidelines to consider both the error term and the parameters’ complexity.

<!-- b000748 | prose | pages [16] -->
  AIC ln

<!-- b000749 | furniture | pages [16] -->


<!-- b000750 | furniture | pages [16] -->


<!-- b000751 | prose | pages [16] -->
2 p 2  (19)

<!-- b000752 | prose | pages [16] -->
n

<!-- b000753 | prose | pages [16] -->
关注数学模型

<!-- b000754 | furniture | pages [16] -->
2

<!-- b000755 | furniture | pages [16] -->
MATHmodels

<!-- b000756 | furniture | pages [16] -->
获取更多资讯

<!-- b000757 | furniture | pages [17] -->
Team # 2010638                                                                   Page 16 of 20

<!-- b000758 | prose | pages [17] -->
  BIC ln

<!-- b000759 | furniture | pages [17] -->


<!-- b000760 | prose | pages [17] -->
Where n represents the size of sample.

<!-- b000761 | prose | pages [17] -->
p 2  ln

<!-- b000762 | prose | pages [17] -->
n

<!-- b000763 | prose | pages [17] -->
(20)

<!-- b000764 | prose | pages [17] -->
n

<!-- b000765 | prose | pages [17] -->
The test illustrates that when p=1, AIC and BIC get the minimum value. Therefore,

<!-- b000766 | prose | pages [17] -->
we consider the fitting of AR(1) is reasonable.

<!-- b000767 | prose | pages [17] -->
The AR (1) model is constructed to predict the comprehensive scores of product reputations. The results are as follows:

<!-- b000768 | prose | pages [17] -->
Taking the hair dryer as an example, in order to observe the relationship between the comprehensive score of product reputation and the time changing trends, we analyzed and predicted the time series in SPSS.

<!-- b000769 | furniture | pages [17] -->


<!-- b000770 | caption | pages [17] -->
Figure 10: Sequence Figure

<!-- b000771 | prose | pages [17] -->
Through the above sequence diagram, we find that the seasonal fluctuation of the time series is basically constant, so we choose the addition model to decompose the seasonal factors. After removing the seasonal factors, the value of error sequence is very small, so the long-term trend and cyclic change sequence (long-term trend + cyclic change) and the sequence after seasonal factor correction (long-term trend + cyclic change + irregular change, that is, error Poor) can basically coincide.

<!-- b000772 | furniture | pages [17] -->


<!-- b000773 | caption | pages [17] -->
Figure 11:A sequence chart that eliminates seasonal trends    Figure 12:The original sequence

<!-- b000774 | prose | pages [17] -->
By analyzing the seasonal trend, it can be found that the trend first drops in the first quarter of each year, then rises to the first peak. Then after a sharp decline, there is an obvious upward trend, reaching the second peak in about the eighth month, then comes a small decline. After that it reaches the peak in about October, and then falling till the beginning of the next year. In order to analyze the reasons for the seasonal changes, we introduced the annual sales volume with the time chart. It can be seen that the timing of reputation and sales have roughly the same seasonal trend, indicating that with the increase of sales, customers are more likely to give favorable reviews. So we conclude that it is consistent with the actual situation. In summer, people wash their hair more frequently. Therefore, they are apt to buy hair dryers from June to August and have a higher probability of making favorable reviews. However, when winter comes around October, the temperature is

<!-- b000775 | furniture | pages [17] -->


<!-- b000776 | prose | pages [17] -->
关注数学模型

<!-- b000777 | furniture | pages [17] -->
2

<!-- b000778 | furniture | pages [17] -->
MATHmodels

<!-- b000779 | furniture | pages [17] -->
获取更多资讯

<!-- b000780 | furniture | pages [18] -->
Team # 2010638                                                                   Page 17 of 20

<!-- b000781 | prose | pages [18] -->
colder and the blowing time becomes longer, which might also improve the demand and reputation of hair dryer.

<!-- b000782 | furniture | pages [18] -->


<!-- b000783 | caption | pages [18] -->
Figure 13: Time Series Forecasting               Figure 14:Annual sales for Three products

<!-- b000784 | prose | pages [18] -->
Through the prediction of time series, the data of 2016-2019 are obtained. It is found that the reputation and demand of hair dryer are highly related to the seasonality, and it is very likely to maintain a stable seasonal cycle mode in the future. Microwave ovens and pacifiers are about the same. The comprehensive score of the microwave oven reaches the peak in April and October, and that of the pacifier reaches the peak in November.

<!-- b000785 | prose | pages [18] -->
From the analysis above, it is believed that the market of hair dryer, microwave oven and pacifier is roughly stable. By referring to seasonal trend, sunshine company is capable to increase the sales share when the score of the product reputation rises up, or reduce the sales investment before the score is about to slump .

<!-- b000786 | heading | pages [18] -->
6. Model 4-Distributed lag model

<!-- b000787 | heading | pages [18] -->
6.1 Distributed lag model

<!-- b000788 | prose | pages [18] -->
In this part, we apply the distributed lag model to determine if the customer's reviews will be affected by others’ star ratings.

<!-- b000789 | prose | pages [18] -->
The distributed lag model is based on the fact that the explained variables are affected by the explanatory variables and distributed on the lagged values of the explanatory variables in different periods.

<!-- b000790 | prose | pages [18] -->
       Y X X

<!-- b000791 | furniture | pages [18] -->


<!-- b000792 | prose | pages [18] -->
 t 0 t 1 t 1

<!-- b000793 | prose | pages [18] -->
s is the lag length.

<!-- b000794 | prose | pages [18] -->
  X (21)  s t s

<!-- b000795 | prose | pages [18] -->
Each coefficient in this model reflects the different influence of each lag value of the explanatory variable on the explained variable, which is commonly referred to as multiplier effect:

<!-- b000796 | prose | pages [18] -->
0β ：Short-term multiplier, which represents the average influence of one unit of star rating change on

<!-- b000797 | furniture | pages [18] -->


<!-- b000798 | prose | pages [18] -->
the emotional score of the review;

<!-- b000799 | prose | pages [18] -->
iβ ：Delay multiplier, which represents the average influence of the change of one unit in the

<!-- b000800 | furniture | pages [18] -->


<!-- b000801 | prose | pages [18] -->
previous period star rating on the emotional score of the review;

<!-- b000802 | prose | pages [18] -->
s

<!-- b000803 | prose | pages [18] -->
 ：The long-term multiplier, which indicates the total impact of the star rating changing due to

<!-- b000804 | furniture | pages [18] -->


<!-- b000805 | prose | pages [18] -->
β

<!-- b000806 | prose | pages [18] -->
i i=

<!-- b000807 | prose | pages [18] -->
0

<!-- b000808 | prose | pages [18] -->
the lag effect.

<!-- b000809 | furniture | pages [18] -->


<!-- b000810 | prose | pages [18] -->
关注数学模型

<!-- b000811 | furniture | pages [18] -->
2

<!-- b000812 | furniture | pages [18] -->
MATHmodels

<!-- b000813 | furniture | pages [18] -->
获取更多资讯

<!-- b000814 | furniture | pages [19] -->
Team # 2010638                                                                   Page 18 of 20

<!-- b000815 | heading | pages [19] -->
6.2 Almon Method

<!-- b000816 | prose | pages [19] -->
The second-order Almon polynomial distribution lag model with a lag of 3 periods is used to establish the regression equation between current reviews and previous star ratings and reviews, so as to determine whether there is a phenomenon that previous star ratings affect current customer reviews. We select the data of the hair dryer whose product parent is 732252283, the pacifier of 392768822 and the microwave oven of 423421857 for analysis.

<!-- b000817 | prose | pages [19] -->
The following finite distribution lag model is estimated by Almon method. And the coefficients are approximated by quadratic polynomials.

<!-- b000818 | prose | pages [19] -->
Y = α+ β X + β X t

<!-- b000819 | prose | pages [19] -->
0

<!-- b000820 | prose | pages [19] -->
t

<!-- b000821 | prose | pages [19] -->
1

<!-- b000822 | prose | pages [19] -->
t-

<!-- b000823 | prose | pages [19] -->
1

<!-- b000824 | prose | pages [19] -->
β = α

<!-- b000825 | prose | pages [19] -->
0 0

<!-- b000826 | prose | pages [19] -->
β = α +α +α

<!-- b000827 | furniture | pages [19] -->


<!-- b000828 | prose | pages [19] -->
1 0 1 2

<!-- b000829 | prose | pages [19] -->
β

<!-- b000830 | prose | pages [19] -->
=

<!-- b000831 | prose | pages [19] -->
α

<!-- b000832 | prose | pages [19] -->
+ 2

<!-- b000833 | prose | pages [19] -->
α

<!-- b000834 | prose | pages [19] -->
+ 4

<!-- b000835 | prose | pages [19] -->
α

<!-- b000836 | prose | pages [19] -->
2 0 1 2

<!-- b000837 | prose | pages [19] -->
β

<!-- b000838 | prose | pages [19] -->
=

<!-- b000839 | prose | pages [19] -->
α

<!-- b000840 | prose | pages [19] -->
+3

<!-- b000841 | prose | pages [19] -->
α

<!-- b000842 | prose | pages [19] -->
+9

<!-- b000843 | prose | pages [19] -->
α

<!-- b000844 | prose | pages [19] -->
3 0 1 2

<!-- b000845 | prose | pages [19] -->
+ β X + β X +u

<!-- b000846 | prose | pages [19] -->
2

<!-- b000847 | prose | pages [19] -->
t-

<!-- b000848 | prose | pages [19] -->
2 3

<!-- b000849 | prose | pages [19] -->
t-

<!-- b000850 | prose | pages [19] -->
3

<!-- b000851 | prose | pages [19] -->
t

<!-- b000852 | prose | pages [19] -->
(22)

<!-- b000853 | prose | pages [19] -->
Then the original model can be transformed into

<!-- b000854 | prose | pages [19] -->


<!-- b000855 | prose | pages [19] -->


<!-- b000856 | prose | pages [19] -->


<!-- b000857 | prose | pages [19] -->


<!-- b000858 | prose | pages [19] -->


<!-- b000859 | prose | pages [19] -->


<!-- b000860 | prose | pages [19] -->


<!-- b000861 | prose | pages [19] -->


<!-- b000862 | prose | pages [19] -->
Y Z Z

<!-- b000863 | prose | pages [19] -->
t

<!-- b000864 | prose | pages [19] -->
0 0

<!-- b000865 | prose | pages [19] -->
t

<!-- b000866 | prose | pages [19] -->
1 1

<!-- b000867 | prose | pages [19] -->
t

<!-- b000868 | prose | pages [19] -->
   

<!-- b000869 | prose | pages [19] -->
Z X X X

<!-- b000870 | prose | pages [19] -->
 

<!-- b000871 | prose | pages [19] -->
0

<!-- b000872 | prose | pages [19] -->
t t t

<!-- b000873 | prose | pages [19] -->
1

<!-- b000874 | prose | pages [19] -->
t

<!-- b000875 | prose | pages [19] -->
2

<!-- b000876 | prose | pages [19] -->
  

<!-- b000877 | prose | pages [19] -->
Z X

<!-- b000878 | prose | pages [19] -->
2

<!-- b000879 | prose | pages [19] -->
X

<!-- b000880 | prose | pages [19] -->
3

<!-- b000881 | prose | pages [19] -->
X

<!-- b000882 | prose | pages [19] -->
 

<!-- b000883 | prose | pages [19] -->
1

<!-- b000884 | prose | pages [19] -->
t t

<!-- b000885 | prose | pages [19] -->
1

<!-- b000886 | prose | pages [19] -->
t

<!-- b000887 | prose | pages [19] -->
2

<!-- b000888 | prose | pages [19] -->
t

<!-- b000889 | prose | pages [19] -->
  

<!-- b000890 | prose | pages [19] -->
Z X

<!-- b000891 | prose | pages [19] -->
4

<!-- b000892 | prose | pages [19] -->
X

<!-- b000893 | prose | pages [19] -->
9

<!-- b000894 | prose | pages [19] -->
X

<!-- b000895 | furniture | pages [19] -->


<!-- b000896 | prose | pages [19] -->
 

<!-- b000897 | prose | pages [19] -->
2

<!-- b000898 | prose | pages [19] -->
t t

<!-- b000899 | prose | pages [19] -->
1

<!-- b000900 | prose | pages [19] -->
t

<!-- b000901 | prose | pages [19] -->
2

<!-- b000902 | prose | pages [19] -->


<!-- b000903 | prose | pages [19] -->


<!-- b000904 | prose | pages [19] -->
Z

<!-- b000905 | prose | pages [19] -->
2 2 2

<!-- b000906 | prose | pages [19] -->
t t

<!-- b000907 | prose | pages [19] -->
X X

<!-- b000908 | prose | pages [19] -->


<!-- b000909 | prose | pages [19] -->
t t

<!-- b000910 | prose | pages [19] -->
3

<!-- b000911 | furniture | pages [19] -->


<!-- b000912 | prose | pages [19] -->
 

<!-- b000913 | prose | pages [19] -->
3 3

<!-- b000914 | prose | pages [19] -->
(23)

<!-- b000915 | prose | pages [19] -->
 

<!-- b000916 | prose | pages [19] -->
t t

<!-- b000917 | prose | pages [19] -->
3 3

<!-- b000918 | prose | pages [19] -->
The final estimation formula of the distribution lag model can be obtained by regression. The regression results are as follows:

<!-- b000919 | caption | pages [19] -->
Table 12:Regression Results

<!-- b000920 | furniture | pages [19] -->


<!-- b000921 | prose | pages [19] -->
0β 1β

<!-- b000922 | prose | pages [19] -->
1.13221∗∗ 0.32379∗∗ Hair dryer

<!-- b000923 | prose | pages [19] -->
0.79191∗∗ 0.21743∗∗ Pacifier

<!-- b000924 | prose | pages [19] -->
1.05871∗∗ 0.17710∗∗ Microwave

<!-- b000925 | prose | pages [19] -->
2 R 2β 3β

<!-- b000926 | prose | pages [19] -->
-0.05354 0.00020 0.902197

<!-- b000927 | prose | pages [19] -->
-0.03039（0） 0.04845 0.929296

<!-- b000928 | prose | pages [19] -->
-0.13628 0.11858 0.835728

<!-- b000929 | prose | pages [19] -->
Note:*: p<0.05; **: p<0.01; +: p<0.1; ns: not significant

<!-- b000930 | prose | pages [19] -->
The regression equation between the comprehensive scores of past star ratings and the emotional score of the current reviews of the three products is as follows:

<!-- b000931 | prose | pages [19] -->
   

<!-- b000932 | prose | pages [19] -->
1.13221X

<!-- b000933 | prose | pages [19] -->
Y

<!-- b000934 | prose | pages [19] -->
0.34

<!-- b000935 | prose | pages [19] -->
247

<!-- b000936 | prose | pages [19] -->
2

<!-- b000937 | prose | pages [19] -->
t

<!-- b000938 | prose | pages [19] -->
 

<!-- b000939 | furniture | pages [19] -->


<!-- b000940 | prose | pages [19] -->
0.32379

<!-- b000941 | prose | pages [19] -->
X

<!-- b000942 | prose | pages [19] -->


<!-- b000943 | prose | pages [19] -->
t t

<!-- b000944 | prose | pages [19] -->
1

<!-- b000945 | prose | pages [19] -->


<!-- b000946 | prose | pages [19] -->
(24)

<!-- b000947 | prose | pages [19] -->
0.79191X

<!-- b000948 | prose | pages [19] -->
Y

<!-- b000949 | prose | pages [19] -->
0.054537

<!-- b000950 | prose | pages [19] -->
t

<!-- b000951 | prose | pages [19] -->
 

<!-- b000952 | prose | pages [19] -->
Y

<!-- b000953 | prose | pages [19] -->
0.226388 1.05871X

<!-- b000954 | prose | pages [19] -->
t

<!-- b000955 | prose | pages [19] -->
0.21743

<!-- b000956 | prose | pages [19] -->
X

<!-- b000957 | prose | pages [19] -->


<!-- b000958 | prose | pages [19] -->
t t

<!-- b000959 | prose | pages [19] -->
1

<!-- b000960 | prose | pages [19] -->


<!-- b000961 | prose | pages [19] -->
0.1771

<!-- b000962 | prose | pages [19] -->
0

<!-- b000963 | prose | pages [19] -->
X

<!-- b000964 | prose | pages [19] -->


<!-- b000965 | prose | pages [19] -->
t t

<!-- b000966 | prose | pages [19] -->
1

<!-- b000967 | prose | pages [19] -->
Therefore, it can be explained that there is a correlation between the current reviews of customers and the past star ratings and reviews, that is, the current evaluation of customers will be affected by the past ratings and evaluations.

<!-- b000968 | heading | pages [19] -->
6.3 Correlation Analysis between Star Rating and Comments

<!-- b000969 | prose | pages [19] -->
According to the time series model, the inflection points of customer reviews can be gotten quickly. By analyzing the specific quality descriptors in the reviews corresponding to these inflection points, and

<!-- b000970 | furniture | pages [19] -->


<!-- b000971 | prose | pages [19] -->
关注数学模型

<!-- b000972 | furniture | pages [19] -->
2

<!-- b000973 | furniture | pages [19] -->
MATHmodels

<!-- b000974 | furniture | pages [19] -->
获取更多资讯

<!-- b000975 | furniture | pages [20] -->
Team # 2010638                                                                   Page 19 of 20

<!-- b000976 | prose | pages [20] -->
comparing them with the star ratings corresponding to the reviews, it is easy to know whether these words are closely related to the star ratings. In the above model, the average score of reviews and star ratings in each time period has been obtained. By comparing the synchronicity of the two changes over time, we can draw the conclusion that the star ratings corresponding to the reviews with positive words are higher, while the star ratings corresponding to the reviews with negative words are lower. (Due to the space, we only put the picture of microwave oven in the text, the picture of hair dryer and pacifier in the appendix.)

<!-- b000977 | furniture | pages [20] -->


<!-- b000978 | caption | pages [20] -->
Figure 15: Sequence Diagram of Star rating and Review

<!-- b000979 | prose | pages [20] -->
However, it still can be seen from the diagrams that some reviews with higher star ratings have lower emotional scores, so it is not excluded that there are high scores, poor reviews (or vice versa) and false reviews.

<!-- b000980 | heading | pages [20] -->
7.  Sensitivity Analysis

<!-- b000981 | prose | pages [20] -->
In the time series analysis model, we give star ratings and reviews 0.3 and 0.7 weight respectively, representing the comprehensive evaluation of each customer on the products they buy. Based on the principle that the importance of reviews is higher than that of star ratings, in order to test the rationality of the weight, we change the weight of star ratings to test whether the results of the model change significantly under the weight ratio of 0.4 and 0.2 respectively. The results are as follows:

<!-- b000982 | caption | pages [20] -->
Table 13: Sensitivity Analysis on Weight of Star Rating

<!-- b000983 | prose | pages [20] -->
a b Change (in %) Product

<!-- b000984 | furniture | pages [20] -->


<!-- b000985 | prose | pages [20] -->
AR （1 ）

<!-- b000986 | prose | pages [20] -->
Hair Dryer 0.126 Pacifier 0.054 Microwave Oven -0.075

<!-- b000987 | prose | pages [20] -->
Change (in %)

<!-- b000988 | furniture | pages [20] -->


<!-- b000989 | prose | pages [20] -->
AR （1 ）

<!-- b000990 | prose | pages [20] -->
0.8% 0.127 20% -0.9% 0.054 18% 0.3% -0.074 -0.6% Note: 𝐴𝑅(1)𝑎: weight of star ratings: 0.4 ; 𝐴𝑅(1)𝑏: weight of star ratings: 0.2 From the table, we can see that the deviation of regression coefficient is not more than 1.8%, which shows that the change of weight has no significant impact on the results of the model, so the weight of 0.3 and 0.7 we set has certain rationality.

<!-- b000991 | furniture | pages [20] -->


<!-- b000992 | prose | pages [20] -->
关注数学模型

<!-- b000993 | furniture | pages [20] -->
2

<!-- b000994 | furniture | pages [20] -->
MATHmodels

<!-- b000995 | furniture | pages [20] -->
获取更多资讯

<!-- b000996 | furniture | pages [21] -->
Team # 2010638                                                                   Page 20 of 20

<!-- b000997 | heading | pages [21] -->
8. Model Assessment

<!-- b000998 | heading | pages [21] -->
8.1 Strengths

<!-- b000999 | prose | pages [21] -->
 Data visualization technology is applied to interpret the original data, and the results are presented

<!-- b001000 | prose | pages [21] -->
intuitively and concisely.  Through the analysis of LDA topic model, the strengths and weaknesses of the products can be given,

<!-- b001001 | prose | pages [21] -->
which is helpful for the design of products.  Our products brand rating system has a wide range of applicability, which can help sales companies

<!-- b001002 | prose | pages [21] -->
grasp customer reviews on the market.

<!-- b001003 | heading | pages [21] -->
8.2 Weaknesses

<!-- b001004 | prose | pages [21] -->
 Our product scoring system uses AHP to determine the weight of each index, which is to some

<!-- b001005 | prose | pages [21] -->
extent subjective.  Our time series model uses monthly data, which is not very accurate and does not take into account

<!-- b001006 | prose | pages [21] -->
special circumstances such as holidays, and may have a large gap with the actual results, and cannot effectively predict the product’s reputation in the long term.

<!-- b001007 | prose | pages [21] -->
Reference

<!-- b001008 | prose | pages [21] -->
[1]Arreola Elsa Vazquez,Wilson Jeffrey R. Bayesian multiple membership multiple classification logistic regression model on student performance with random effects in university instructors and majors.[J]. PloS one,2020,15(1). [2]Blei D M, Ng A Y, Jordan M I. Latent dirichlet allocation[J]. Journal of Machine Learning Research, 2003, 3:2003. [3]Cao Juan, Xia Tian, Li Jin Tao, A density method for adaptive LDA model selection[J]. Neurocomputing 2009(72):1775-1781. [4]Connors, L., Mudambi, S.M., Schuff, D.. Is It the Review or the Reviewer? a Multi-Method Approach to Determine the Antecedents of Online Review Helpfulness[P]. System Sciences (HICSS), 2011 44th Hawaii International Conference on,2011. [5]Changxuan Wan,Yun Peng,Keli Xiao,Xiping Liu,Tengjiao Jiang,Dexi Liu. An association-constrained LDA model for joint extraction of product aspects and opinions[J]. Information Sciences,2020,519. [6]Cheung, Christy M. K., and Dimple R. Thadani. “The Effectiveness of Electronic Word-of-Mouth Communication: A Literature Analysis.” Bled EConference, 2010, p. 18. [7]Kim, Soo-Min, et al. “Automatically Assessing Review Helpfulness.” Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing, 2006, pp. 423–430. [8]Mudambi, Susan M.,Schuff, David,Zhang, Zhewei. Why Aren't the Stars Aligned? An Analysis of Online Review Content and Star Ratings[P]. ,2014. [9]Yan Leng,Weiwei Zhao,Chan Lin,Chengli Sun,Rongyan Wang,Qi Yuan,Dengwang Li. LDA-based data augmentation algorithm for acoustic scene classification[J]. Knowledge-Based Systems,2020.

<!-- b001009 | furniture | pages [21] -->


<!-- b001010 | furniture | pages [21] -->


<!-- b001011 | prose | pages [21] -->
关注数学模型

<!-- b001012 | furniture | pages [21] -->
2

<!-- b001013 | furniture | pages [21] -->
MATHmodels

<!-- b001014 | furniture | pages [21] -->
获取更多资讯

<!-- b001015 | furniture | pages [22] -->
Team # 2010638                                                                   Page 1 of 2

<!-- b001016 | heading | pages [22] -->
Letter

<!-- b001017 | prose | pages [22] -->
Dear Sunshine Company Marketing Director:

<!-- b001018 | prose | pages [22] -->
We are honored to inform you of our recommendations for product improvement and sales strategies for your company after data analysis and modeling. The following are some suggestions based on our analysis.

<!-- b001019 | heading | pages [22] -->
1. Suggestions for product improvement

<!-- b001020 | prose | pages [22] -->
We apply the LDA analysis model to find the topic feature of each product, in which the negative topic words can reflect the customers' dissatisfaction with the existing products in the market.

<!-- b001021 | prose | pages [22] -->
Analysis of the review text revealed that the words like "cost", "heavy", "smoking" and "noise" appeared on the top of the list of negative reviews on the hair dryer. After analyzing these high-frequency words one by one, we discovered that there were some drawbacks with hair dryers from the customers’ point of view:

<!-- b001022 | prose | pages [22] -->
 Inefficiency: it takes a long time to blow-dry.  Weight: it is too heavy to use conveniently.  Bad quality: when using the product, there will be a lot of noise sometimes. Therefore, according to the feedback above, we believe that the improvement of hair dryer products is supposed to start from improving the working efficiency and quality of hair dryer. Lightweight materials can be used in the production, reducing the weight of the hair dryer, should also reduce the noise when it works. For instance, lightweight materials can be used to reduce the weight of the hair dryer and reduce the noise while it is working.

<!-- b001023 | furniture | pages [22] -->


<!-- b001024 | prose | pages [22] -->
As for microwave oven, words like "service" and "small" appeared on the top of the list of negative reviews. According to the feedback, we believe that the microwave oven may have the following defects:

<!-- b001025 | prose | pages [22] -->
 Size: someone considered that microwave ovens are too small, while others reckon that small ones are more convenient to use.

<!-- b001026 | prose | pages [22] -->
 Service: the after-sale service of some microwave ovens is not consummate. In view of the above two points, we hold that microwave oven products can be designed in different sizes to meet the diverse needs of different customers. Moreover, improving service level and customer satisfaction is also a top priority.

<!-- b001027 | furniture | pages [22] -->


<!-- b001028 | prose | pages [22] -->
"Hot" is the most frequently used negative word for a pacifier. Some customers think that the insulation function of the pacifier is poor, which reminds us that we should enhance the thermal insulation function in the design of the pacifier. In addition, we have noticed that customers attach great importance to the "appearance" of the pacifier and hence the cute product design will help to sell the product.

<!-- b001029 | furniture | pages [22] -->


<!-- b001030 | heading | pages [22] -->
2. Sales strategy

<!-- b001031 | prose | pages [22] -->
Through the in-depth analysis of star ratings and reviews, we will propose sales suggestions and strategies from three aspects: the product brand, the time of selling products and the evaluation psychology of customers.

<!-- b001032 | prose | pages [22] -->
 Recommend the product brand for sale.

<!-- b001033 | furniture | pages [22] -->


<!-- b001034 | prose | pages [22] -->
关注数学模型

<!-- b001035 | furniture | pages [22] -->
2

<!-- b001036 | furniture | pages [22] -->
MATHmodels

<!-- b001037 | furniture | pages [22] -->
获取更多资讯

<!-- b001038 | furniture | pages [23] -->
Team # 2010638                                                                   Page 2 of 2

<!-- b001039 | prose | pages [23] -->
Based on the analysis of star rating and review, we summarized five indexes that affect product sales, namely quality, price, appearance, service and size, as well as index weight, then built a brand scoring system based on this. Through the systematic clustering of each score, all product brands were clustered, and the high-quality product brands were selected eventually. The product parent of some premium brands is as follows:

<!-- b001040 | prose | pages [23] -->
microwave 862802057 423421857 Hair-dryer 244516305 266176173 pacifier 22060147 22189989 692404913 464779766 423421857 468944538 741916038 112413045 51496920 62352351 79207704 Our brand rating system takes full account of the characteristics of each product, so the conclusions are very reliable. It is believed that the high quality brands recommended for sale will be favored by more customers.

<!-- b001041 | prose | pages [23] -->
 Sales opportunities analysis. we predict the future reputation of the three products through time series analysis. The results demonstrate that the three products are highly correlated with seasonality, and the seasonal cycle pattern is likely to be stable in the future. However, the peaks of reputation composite scores of the three products occurred at different times.

<!-- b001042 | prose | pages [23] -->
Pacifiers peaked around November, hairdryers around August and October, and microwave ovens around April and October. The peak of reputation will lead to an increase in sales, so we suggest that your company adjust the sales structure according to the peak time of different products. When the product reputation is about to peak, your company can increase the sales investment of the product to obtain higher revenue.

<!-- b001043 | prose | pages [23] -->
 Psychological analysis of customer reviews. We analyze the relationship between star rating and review. Through the research of distributed lag model, it is found that customers' reviews in the current period will be influenced by other customers' ratings and reviews. Therefore, we suggest that your company should still pay attention to the customer's rating of the goods after selling the products, and try to make the rating of its own products at a high level, so as not to gain a bad impact on future sales. To sum up, by keeping an eye on customers' preferences and regarding them as standards for improving products and services, your company can gradually increase product sales and market share.

<!-- b001044 | furniture | pages [23] -->


<!-- b001045 | prose | pages [23] -->
These are all suggestions and strategies our team has provided to your company. Thank you again for taking the time to read our suggestions.

<!-- b001046 | prose | pages [23] -->
Hope that our models and these suggestions can be helpful to you!

<!-- b001047 | furniture | pages [23] -->


<!-- b001048 | furniture | pages [23] -->


<!-- b001049 | furniture | pages [23] -->


<!-- b001050 | furniture | pages [23] -->


<!-- b001051 | furniture | pages [23] -->


<!-- b001052 | furniture | pages [23] -->


<!-- b001053 | furniture | pages [23] -->


<!-- b001054 | furniture | pages [23] -->


<!-- b001055 | furniture | pages [23] -->


<!-- b001056 | furniture | pages [23] -->


<!-- b001057 | prose | pages [23] -->
Sincerely, MCM Team Members

<!-- b001058 | prose | pages [23] -->
关注数学模型

<!-- b001059 | furniture | pages [23] -->
2

<!-- b001060 | furniture | pages [23] -->
MATHmodels

<!-- b001061 | furniture | pages [23] -->
获取更多资讯

<!-- b001062 | furniture | pages [24] -->
Team # 2010638                                                                   Page 1 of 20

<!-- b001063 | heading | pages [24] -->
Appendix

<!-- b001064 | heading | pages [24] -->
Appendix 1

<!-- b001065 | furniture | pages [24] -->


<!-- b001066 | prose | pages [24] -->
Correlation analysis                          The distribution of the number of words

<!-- b001067 | furniture | pages [24] -->


<!-- b001068 | prose | pages [24] -->
 Consistency test of AHP

<!-- b001069 | prose | pages [24] -->
Consistency check ratio table Consis

<!-- b001070 | prose | pages [24] -->
qu

<!-- b001071 | prose | pages [24] -->
appeara price

<!-- b001072 | prose | pages [24] -->
tency ratio

<!-- b001073 | prose | pages [24] -->
ality

<!-- b001074 | prose | pages [24] -->
nce

<!-- b001075 | prose | pages [24] -->
0.0 0.00 CR 0.00857 0000 688

<!-- b001076 | furniture | pages [24] -->


<!-- b001077 | heading | pages [24] -->
Appendix 2

<!-- b001078 | furniture | pages [24] -->


<!-- b001079 | heading | pages [24] -->
Regression results of distribution lag model

<!-- b001080 | furniture | pages [24] -->


<!-- b001081 | heading | pages [24] -->
1. Hair dryer

<!-- b001082 | prose | pages [24] -->
Coefficie

<!-- b001083 | prose | pages [24] -->
Std.

<!-- b001084 | prose | pages [24] -->
Variable

<!-- b001085 | prose | pages [24] -->
nt

<!-- b001086 | prose | pages [24] -->
Error

<!-- b001087 | prose | pages [24] -->
-0.34247

<!-- b001088 | prose | pages [24] -->
0.06643

<!-- b001089 | prose | pages [24] -->
C

<!-- b001090 | prose | pages [24] -->
2

<!-- b001091 | prose | pages [24] -->
0

<!-- b001092 | prose | pages [24] -->
0.04057

<!-- b001093 | prose | pages [24] -->
PDL01 0.323795

<!-- b001094 | prose | pages [24] -->
2

<!-- b001095 | prose | pages [24] -->
-0.59287

<!-- b001096 | prose | pages [24] -->
0.04035

<!-- b001097 | prose | pages [24] -->
PDL02

<!-- b001098 | prose | pages [24] -->
8

<!-- b001099 | prose | pages [24] -->
2

<!-- b001100 | prose | pages [24] -->
0.02861

<!-- b001101 | prose | pages [24] -->
PDL03 0.215540

<!-- b001102 | prose | pages [24] -->
2

<!-- b001103 | furniture | pages [24] -->


<!-- b001104 | prose | pages [24] -->
servi

<!-- b001105 | prose | pages [24] -->
Star

<!-- b001106 | prose | pages [24] -->
size ce

<!-- b001107 | prose | pages [24] -->
ratings

<!-- b001108 | prose | pages [24] -->
0.00 0.00 0.00 0817 053 047

<!-- b001109 | prose | pages [24] -->
t-Statistic Prob.

<!-- b001110 | prose | pages [24] -->
-5.155354 0.0000

<!-- b001111 | prose | pages [24] -->
7.980680 0.0000

<!-- b001112 | prose | pages [24] -->
-14.69277 0.0000

<!-- b001113 | prose | pages [24] -->
7.533150 0.0000

<!-- b001114 | prose | pages [24] -->
关注数学模型

<!-- b001115 | furniture | pages [24] -->
2

<!-- b001116 | furniture | pages [24] -->
MATHmodels

<!-- b001117 | furniture | pages [24] -->
获取更多资讯

<!-- b001118 | furniture | pages [25] -->
Team # 2010638                                                                   Page 2 of 20

<!-- b001119 | prose | pages [25] -->
0.64829

<!-- b001120 | prose | pages [25] -->
Mean dependent var R-squared 0.902197

<!-- b001121 | prose | pages [25] -->
3

<!-- b001122 | prose | pages [25] -->
0.22365

<!-- b001123 | prose | pages [25] -->
S.D. dependent var Adjusted R-squared 0.896444

<!-- b001124 | prose | pages [25] -->
9

<!-- b001125 | prose | pages [25] -->
-2.3550

<!-- b001126 | prose | pages [25] -->
Akaike info criterion S.E. of regression 0.071974

<!-- b001127 | prose | pages [25] -->
86

<!-- b001128 | prose | pages [25] -->
-2.2090

<!-- b001129 | prose | pages [25] -->
Schwarz criterion Sum squared resid 0.264190

<!-- b001130 | prose | pages [25] -->
99

<!-- b001131 | prose | pages [25] -->
-2.2986

<!-- b001132 | prose | pages [25] -->
Hannan-Quinn criter. Log likelihood 68.76488

<!-- b001133 | prose | pages [25] -->
32

<!-- b001134 | prose | pages [25] -->
1.71152

<!-- b001135 | prose | pages [25] -->
Durbin-Watson stat F-statistic 156.8187

<!-- b001136 | prose | pages [25] -->
Prob(F-statistic) 0.000000

<!-- b001137 | furniture | pages [25] -->


<!-- b001138 | prose | pages [25] -->
Lag Distribution

<!-- b001139 | prose | pages [25] -->
Coeffici

<!-- b001140 | prose | pages [25] -->
of TOTAL

<!-- b001141 | furniture | pages [25] -->


<!-- b001142 | prose | pages [25] -->
ent

<!-- b001143 | prose | pages [25] -->
.              *|

<!-- b001144 | furniture | pages [25] -->


<!-- b001145 | prose | pages [25] -->
1.13221

<!-- b001146 | prose | pages [25] -->
.   *           |

<!-- b001147 | furniture | pages [25] -->


<!-- b001148 | prose | pages [25] -->
0.32379

<!-- b001149 | prose | pages [25] -->
-0.0535

<!-- b001150 | prose | pages [25] -->
*.               |

<!-- b001151 | furniture | pages [25] -->


<!-- b001152 | prose | pages [25] -->
4

<!-- b001153 | prose | pages [25] -->
*               |

<!-- b001154 | furniture | pages [25] -->


<!-- b001155 | prose | pages [25] -->
0.00020

<!-- b001156 | prose | pages [25] -->
Sum of

<!-- b001157 | prose | pages [25] -->
1.4026

<!-- b001158 | furniture | pages [25] -->


<!-- b001159 | prose | pages [25] -->
Lags

<!-- b001160 | prose | pages [25] -->
6

<!-- b001161 | heading | pages [25] -->
2. Pacifier

<!-- b001162 | prose | pages [25] -->
Coefficie

<!-- b001163 | prose | pages [25] -->
Std.

<!-- b001164 | prose | pages [25] -->
Variable

<!-- b001165 | prose | pages [25] -->
nt

<!-- b001166 | prose | pages [25] -->
Error

<!-- b001167 | prose | pages [25] -->
-0.05453

<!-- b001168 | prose | pages [25] -->
0.10941

<!-- b001169 | prose | pages [25] -->
C

<!-- b001170 | prose | pages [25] -->
7

<!-- b001171 | prose | pages [25] -->
9

<!-- b001172 | prose | pages [25] -->
0.05220

<!-- b001173 | prose | pages [25] -->
PDL01 0.217428

<!-- b001174 | prose | pages [25] -->
1

<!-- b001175 | prose | pages [25] -->
-0.41115

<!-- b001176 | prose | pages [25] -->
0.05242

<!-- b001177 | prose | pages [25] -->
PDL02

<!-- b001178 | prose | pages [25] -->
2

<!-- b001179 | prose | pages [25] -->
4

<!-- b001180 | prose | pages [25] -->
0.03664

<!-- b001181 | prose | pages [25] -->
PDL03 0.163331

<!-- b001182 | prose | pages [25] -->
1

<!-- b001183 | prose | pages [25] -->
2

<!-- b001184 | furniture | pages [25] -->


<!-- b001185 | furniture | pages [25] -->


<!-- b001186 | prose | pages [25] -->
t-Statisti

<!-- b001187 | prose | pages [25] -->
Std. Error

<!-- b001188 | prose | pages [25] -->
c

<!-- b001189 | prose | pages [25] -->
0.05595 20.2356

<!-- b001190 | prose | pages [25] -->
0.04057 7.98068

<!-- b001191 | prose | pages [25] -->
-1.3294

<!-- b001192 | prose | pages [25] -->
0.04027

<!-- b001193 | prose | pages [25] -->
8

<!-- b001194 | prose | pages [25] -->
0.05539 0.00358

<!-- b001195 | prose | pages [25] -->
15.175

<!-- b001196 | prose | pages [25] -->
0.09243

<!-- b001197 | prose | pages [25] -->
1

<!-- b001198 | prose | pages [25] -->
t-Statistic Prob.

<!-- b001199 | prose | pages [25] -->
-0.498424 0.6201

<!-- b001200 | prose | pages [25] -->
4.165216 0.0001

<!-- b001201 | prose | pages [25] -->
-7.842873 0.0000

<!-- b001202 | prose | pages [25] -->
4.457639 0.0000

<!-- b001203 | prose | pages [25] -->
0.73679

<!-- b001204 | prose | pages [25] -->
Mean dependent var R-squared 0.629296

<!-- b001205 | prose | pages [25] -->
9

<!-- b001206 | prose | pages [25] -->
0.16242

<!-- b001207 | prose | pages [25] -->
S.D. dependent var Adjusted R-squared 0.609786

<!-- b001208 | prose | pages [25] -->
3

<!-- b001209 | prose | pages [25] -->
-1.6749

<!-- b001210 | prose | pages [25] -->
Akaike info criterion S.E. of regression 0.101461

<!-- b001211 | furniture | pages [25] -->


<!-- b001212 | prose | pages [25] -->
65

<!-- b001213 | prose | pages [25] -->
关注数学模型

<!-- b001214 | furniture | pages [25] -->
2

<!-- b001215 | furniture | pages [25] -->
MATHmodels

<!-- b001216 | furniture | pages [25] -->
获取更多资讯

<!-- b001217 | furniture | pages [26] -->
Team # 2010638                                                                   Page 3 of 20

<!-- b001218 | prose | pages [26] -->
-1.5365

<!-- b001219 | prose | pages [26] -->
Schwarz criterion Sum squared resid 0.586774

<!-- b001220 | prose | pages [26] -->
47

<!-- b001221 | prose | pages [26] -->
-1.6207

<!-- b001222 | prose | pages [26] -->
Hannan-Quinn criter. Log likelihood 55.08642

<!-- b001223 | prose | pages [26] -->
17

<!-- b001224 | prose | pages [26] -->
1.59103

<!-- b001225 | prose | pages [26] -->
Durbin-Watson stat F-statistic 32.25389

<!-- b001226 | prose | pages [26] -->
Prob(F-statistic) 0.000000

<!-- b001227 | furniture | pages [26] -->


<!-- b001228 | prose | pages [26] -->
Lag Distribution

<!-- b001229 | prose | pages [26] -->
Coeffici

<!-- b001230 | prose | pages [26] -->
of TOTAL

<!-- b001231 | furniture | pages [26] -->


<!-- b001232 | prose | pages [26] -->
ent

<!-- b001233 | prose | pages [26] -->
.              *|

<!-- b001234 | furniture | pages [26] -->


<!-- b001235 | prose | pages [26] -->
0.79191

<!-- b001236 | prose | pages [26] -->
.   *           |

<!-- b001237 | furniture | pages [26] -->


<!-- b001238 | prose | pages [26] -->
0.21743

<!-- b001239 | prose | pages [26] -->
-0.0303

<!-- b001240 | prose | pages [26] -->
*.               |

<!-- b001241 | furniture | pages [26] -->


<!-- b001242 | prose | pages [26] -->
9

<!-- b001243 | prose | pages [26] -->
.*              |

<!-- b001244 | furniture | pages [26] -->


<!-- b001245 | prose | pages [26] -->
0.04845

<!-- b001246 | prose | pages [26] -->
Sum of

<!-- b001247 | prose | pages [26] -->
1.0273

<!-- b001248 | furniture | pages [26] -->


<!-- b001249 | prose | pages [26] -->
Lags

<!-- b001250 | prose | pages [26] -->
9

<!-- b001251 | heading | pages [26] -->
3. Microwave oven

<!-- b001252 | prose | pages [26] -->
Coefficie

<!-- b001253 | prose | pages [26] -->
Std.

<!-- b001254 | prose | pages [26] -->
Variable

<!-- b001255 | prose | pages [26] -->
nt

<!-- b001256 | prose | pages [26] -->
Error

<!-- b001257 | prose | pages [26] -->
-0.22638

<!-- b001258 | prose | pages [26] -->
0.07200

<!-- b001259 | prose | pages [26] -->
C

<!-- b001260 | prose | pages [26] -->
8

<!-- b001261 | prose | pages [26] -->
6

<!-- b001262 | prose | pages [26] -->
0.05482

<!-- b001263 | prose | pages [26] -->
PDL01 0.177103

<!-- b001264 | prose | pages [26] -->
2

<!-- b001265 | prose | pages [26] -->
-0.59749

<!-- b001266 | prose | pages [26] -->
0.05752

<!-- b001267 | prose | pages [26] -->
PDL02

<!-- b001268 | prose | pages [26] -->
4

<!-- b001269 | prose | pages [26] -->
5

<!-- b001270 | prose | pages [26] -->
0.04604

<!-- b001271 | prose | pages [26] -->
PDL03 0.284116

<!-- b001272 | prose | pages [26] -->
5

<!-- b001273 | prose | pages [26] -->
8

<!-- b001274 | furniture | pages [26] -->


<!-- b001275 | furniture | pages [26] -->


<!-- b001276 | prose | pages [26] -->
t-Statisti

<!-- b001277 | prose | pages [26] -->
Std. Error

<!-- b001278 | prose | pages [26] -->
c

<!-- b001279 | prose | pages [26] -->
0.08171 9.69200

<!-- b001280 | prose | pages [26] -->
0.05220 4.16522

<!-- b001281 | prose | pages [26] -->
-0.6099

<!-- b001282 | prose | pages [26] -->
0.04982

<!-- b001283 | prose | pages [26] -->
9

<!-- b001284 | prose | pages [26] -->
0.06081 0.79669

<!-- b001285 | prose | pages [26] -->
7.2225

<!-- b001286 | prose | pages [26] -->
0.14225

<!-- b001287 | prose | pages [26] -->
3

<!-- b001288 | prose | pages [26] -->
t-Statistic Prob.

<!-- b001289 | prose | pages [26] -->
-3.144010 0.0030

<!-- b001290 | prose | pages [26] -->
3.230494 0.0023

<!-- b001291 | prose | pages [26] -->
-10.38663 0.0000

<!-- b001292 | prose | pages [26] -->
6.170329 0.0000

<!-- b001293 | prose | pages [26] -->
0.52140

<!-- b001294 | prose | pages [26] -->
Mean dependent var R-squared 0.835728

<!-- b001295 | prose | pages [26] -->
9

<!-- b001296 | prose | pages [26] -->
0.22024

<!-- b001297 | prose | pages [26] -->
S.D. dependent var Adjusted R-squared 0.824528

<!-- b001298 | prose | pages [26] -->
0

<!-- b001299 | prose | pages [26] -->
-1.8488

<!-- b001300 | prose | pages [26] -->
Akaike info criterion S.E. of regression 0.092257

<!-- b001301 | prose | pages [26] -->
16

<!-- b001302 | prose | pages [26] -->
-1.6928

<!-- b001303 | prose | pages [26] -->
Schwarz criterion Sum squared resid 0.374502

<!-- b001304 | prose | pages [26] -->
83

<!-- b001305 | prose | pages [26] -->
-1.7898

<!-- b001306 | prose | pages [26] -->
Hannan-Quinn criter. Log likelihood 48.37159

<!-- b001307 | prose | pages [26] -->
89

<!-- b001308 | prose | pages [26] -->
1.49272

<!-- b001309 | prose | pages [26] -->
Durbin-Watson stat F-statistic 74.61626

<!-- b001310 | furniture | pages [26] -->


<!-- b001311 | prose | pages [26] -->
4

<!-- b001312 | prose | pages [26] -->
关注数学模型

<!-- b001313 | furniture | pages [26] -->
2

<!-- b001314 | furniture | pages [26] -->
MATHmodels

<!-- b001315 | furniture | pages [26] -->
获取更多资讯

<!-- b001316 | furniture | pages [27] -->
Team # 2010638                                                                   Page 4 of 20

<!-- b001317 | prose | pages [27] -->
Prob(F-statistic) 0.000000

<!-- b001318 | furniture | pages [27] -->


<!-- b001319 | prose | pages [27] -->
Lag Distribution

<!-- b001320 | prose | pages [27] -->
Coeffici

<!-- b001321 | prose | pages [27] -->
of TOTAL

<!-- b001322 | furniture | pages [27] -->


<!-- b001323 | prose | pages [27] -->
ent

<!-- b001324 | prose | pages [27] -->
.             *|

<!-- b001325 | furniture | pages [27] -->


<!-- b001326 | prose | pages [27] -->
1.05871

<!-- b001327 | prose | pages [27] -->
. *            |

<!-- b001328 | furniture | pages [27] -->


<!-- b001329 | prose | pages [27] -->
0.17710

<!-- b001330 | prose | pages [27] -->
-0.1362

<!-- b001331 | prose | pages [27] -->
* .              |

<!-- b001332 | furniture | pages [27] -->


<!-- b001333 | prose | pages [27] -->
8

<!-- b001334 | prose | pages [27] -->
. *            |

<!-- b001335 | furniture | pages [27] -->


<!-- b001336 | prose | pages [27] -->
0.11858

<!-- b001337 | prose | pages [27] -->
Sum of

<!-- b001338 | prose | pages [27] -->
1.2181

<!-- b001339 | furniture | pages [27] -->


<!-- b001340 | prose | pages [27] -->
Lags

<!-- b001341 | prose | pages [27] -->
2

<!-- b001342 | furniture | pages [27] -->


<!-- b001343 | furniture | pages [27] -->


<!-- b001344 | heading | pages [27] -->
Appendix 3

<!-- b001345 | heading | pages [27] -->
Partial system clustering results

<!-- b001346 | prose | pages [27] -->
1.

<!-- b001347 | prose | pages [27] -->
Microwave

<!-- b001348 | prose | pages [27] -->
10

<!-- b001349 | prose | pages [27] -->
9

<!-- b001350 | prose | pages [27] -->
8

<!-- b001351 | prose | pages [27] -->
7

<!-- b001352 | prose | pages [27] -->
oven

<!-- b001353 | prose | pages [27] -->
clusters

<!-- b001354 | prose | pages [27] -->
clusters

<!-- b001355 | prose | pages [27] -->
clusters

<!-- b001356 | prose | pages [27] -->
clusters

<!-- b001357 | prose | pages [27] -->
1:1092263

<!-- b001358 | prose | pages [27] -->
1 1 1

<!-- b001359 | prose | pages [27] -->
52

<!-- b001360 | prose | pages [27] -->
2:1474013

<!-- b001361 | prose | pages [27] -->
2 2 2

<!-- b001362 | prose | pages [27] -->
77

<!-- b001363 | prose | pages [27] -->
3:1495592

<!-- b001364 | prose | pages [27] -->
3 3 3

<!-- b001365 | prose | pages [27] -->
60

<!-- b001366 | prose | pages [27] -->
4:1555287

<!-- b001367 | prose | pages [27] -->
2 2 2

<!-- b001368 | prose | pages [27] -->
92

<!-- b001369 | prose | pages [27] -->
5:1664839

<!-- b001370 | prose | pages [27] -->
4 4 4

<!-- b001371 | prose | pages [27] -->
32

<!-- b001372 | prose | pages [27] -->
6:1681813

<!-- b001373 | prose | pages [27] -->
4 4 4

<!-- b001374 | prose | pages [27] -->
02

<!-- b001375 | prose | pages [27] -->
7:2159538

<!-- b001376 | prose | pages [27] -->
2 2 2

<!-- b001377 | prose | pages [27] -->
85

<!-- b001378 | prose | pages [27] -->
8:2427278

<!-- b001379 | prose | pages [27] -->
5 5 4

<!-- b001380 | prose | pages [27] -->
54

<!-- b001381 | prose | pages [27] -->
9:2955201

<!-- b001382 | prose | pages [27] -->
4 4 4

<!-- b001383 | prose | pages [27] -->
51

<!-- b001384 | prose | pages [27] -->
10:305608

<!-- b001385 | prose | pages [27] -->
1 1 1

<!-- b001386 | prose | pages [27] -->
994

<!-- b001387 | prose | pages [27] -->
11:309267

<!-- b001388 | prose | pages [27] -->
1 1 1

<!-- b001389 | prose | pages [27] -->
414

<!-- b001390 | furniture | pages [27] -->


<!-- b001391 | furniture | pages [27] -->


<!-- b001392 | furniture | pages [27] -->


<!-- b001393 | prose | pages [27] -->
t-Statisti

<!-- b001394 | prose | pages [27] -->
Std. Error

<!-- b001395 | prose | pages [27] -->
c

<!-- b001396 | prose | pages [27] -->
0.07634 13.8681

<!-- b001397 | prose | pages [27] -->
0.05482 3.23049

<!-- b001398 | prose | pages [27] -->
-2.4775

<!-- b001399 | prose | pages [27] -->
0.05500

<!-- b001400 | prose | pages [27] -->
9

<!-- b001401 | prose | pages [27] -->
0.07611 1.55802

<!-- b001402 | prose | pages [27] -->
10.594

<!-- b001403 | prose | pages [27] -->
0.11498

<!-- b001404 | prose | pages [27] -->
4

<!-- b001405 | prose | pages [27] -->
6

<!-- b001406 | prose | pages [27] -->
5

<!-- b001407 | prose | pages [27] -->
clusters

<!-- b001408 | prose | pages [27] -->
clusters

<!-- b001409 | prose | pages [27] -->
1 1 1 1

<!-- b001410 | prose | pages [27] -->
2 2 2 2

<!-- b001411 | prose | pages [27] -->
3 3 3 3

<!-- b001412 | prose | pages [27] -->
2 2 2 2

<!-- b001413 | prose | pages [27] -->
4 4 4 2

<!-- b001414 | prose | pages [27] -->
4 4 4 2

<!-- b001415 | prose | pages [27] -->
2 2 2 2

<!-- b001416 | prose | pages [27] -->
4 4 4 2

<!-- b001417 | prose | pages [27] -->
4 4 4 2

<!-- b001418 | prose | pages [27] -->
1 1 1 1

<!-- b001419 | prose | pages [27] -->
1 1 1 1

<!-- b001420 | prose | pages [27] -->
关注数学模型

<!-- b001421 | furniture | pages [27] -->
2

<!-- b001422 | furniture | pages [27] -->
MATHmodels

<!-- b001423 | furniture | pages [27] -->
获取更多资讯

<!-- b001424 | furniture | pages [28] -->
Team # 2010638                                                                   Page 5 of 20

<!-- b001425 | prose | pages [28] -->
12:311592

<!-- b001426 | prose | pages [28] -->
6 6 5

<!-- b001427 | prose | pages [28] -->
014

<!-- b001428 | prose | pages [28] -->
13:313983

<!-- b001429 | prose | pages [28] -->
7 7 6

<!-- b001430 | prose | pages [28] -->
847

<!-- b001431 | prose | pages [28] -->
14:379992

<!-- b001432 | prose | pages [28] -->
4 4 4

<!-- b001433 | prose | pages [28] -->
322

<!-- b001434 | prose | pages [28] -->
15:392967

<!-- b001435 | prose | pages [28] -->
2 2 2

<!-- b001436 | prose | pages [28] -->
251

<!-- b001437 | prose | pages [28] -->
16:423421

<!-- b001438 | prose | pages [28] -->
1 1 1

<!-- b001439 | prose | pages [28] -->
857

<!-- b001440 | prose | pages [28] -->
17:454581

<!-- b001441 | prose | pages [28] -->
7 7 6

<!-- b001442 | prose | pages [28] -->
724

<!-- b001443 | prose | pages [28] -->
18:459626

<!-- b001444 | prose | pages [28] -->
1 1 1

<!-- b001445 | prose | pages [28] -->
087

<!-- b001446 | prose | pages [28] -->
19:464779

<!-- b001447 | prose | pages [28] -->
4 4 4

<!-- b001448 | prose | pages [28] -->
766

<!-- b001449 | prose | pages [28] -->
20:486381

<!-- b001450 | prose | pages [28] -->
5 5 4

<!-- b001451 | prose | pages [28] -->
187

<!-- b001452 | prose | pages [28] -->
21:494028

<!-- b001453 | prose | pages [28] -->
2 2 2

<!-- b001454 | prose | pages [28] -->
413

<!-- b001455 | prose | pages [28] -->
22:494668

<!-- b001456 | prose | pages [28] -->
5 5 4

<!-- b001457 | prose | pages [28] -->
275

<!-- b001458 | prose | pages [28] -->
23:522487

<!-- b001459 | prose | pages [28] -->
6 6 5

<!-- b001460 | prose | pages [28] -->
135

<!-- b001461 | prose | pages [28] -->
24:523301

<!-- b001462 | prose | pages [28] -->
1 1 1

<!-- b001463 | prose | pages [28] -->
568

<!-- b001464 | prose | pages [28] -->
25:539049

<!-- b001465 | prose | pages [28] -->
2 2 2

<!-- b001466 | prose | pages [28] -->
610

<!-- b001467 | prose | pages [28] -->
26:542519

<!-- b001468 | prose | pages [28] -->
5 5 4

<!-- b001469 | prose | pages [28] -->
500

<!-- b001470 | prose | pages [28] -->
27:542731

<!-- b001471 | prose | pages [28] -->
2 2 2

<!-- b001472 | prose | pages [28] -->
946

<!-- b001473 | prose | pages [28] -->
28:544821

<!-- b001474 | prose | pages [28] -->
2 2 2

<!-- b001475 | prose | pages [28] -->
753

<!-- b001476 | prose | pages [28] -->
29:550562

<!-- b001477 | prose | pages [28] -->
8 8 7

<!-- b001478 | prose | pages [28] -->
680

<!-- b001479 | furniture | pages [28] -->


<!-- b001480 | prose | pages [28] -->
2.

<!-- b001481 | prose | pages [28] -->
10

<!-- b001482 | prose | pages [28] -->
9

<!-- b001483 | prose | pages [28] -->
8

<!-- b001484 | prose | pages [28] -->
7

<!-- b001485 | prose | pages [28] -->
Pacifier

<!-- b001486 | prose | pages [28] -->
clusters

<!-- b001487 | prose | pages [28] -->
clusters

<!-- b001488 | prose | pages [28] -->
clusters

<!-- b001489 | prose | pages [28] -->
clusters

<!-- b001490 | prose | pages [28] -->
1:

<!-- b001491 | prose | pages [28] -->
1 1 1 1

<!-- b001492 | prose | pages [28] -->
723849

<!-- b001493 | prose | pages [28] -->
2:

<!-- b001494 | prose | pages [28] -->
2 2 2 2

<!-- b001495 | prose | pages [28] -->
1006724

<!-- b001496 | furniture | pages [28] -->


<!-- b001497 | prose | pages [28] -->
5 5 5 4

<!-- b001498 | prose | pages [28] -->
6 6 6 5

<!-- b001499 | prose | pages [28] -->
4 4 4 2

<!-- b001500 | prose | pages [28] -->
2 2 2 2

<!-- b001501 | prose | pages [28] -->
1 1 1 1

<!-- b001502 | prose | pages [28] -->
6 6 6 5

<!-- b001503 | prose | pages [28] -->
1 1 1 1

<!-- b001504 | prose | pages [28] -->
4 4 4 2

<!-- b001505 | prose | pages [28] -->
4 4 4 2

<!-- b001506 | prose | pages [28] -->
2 2 2 2

<!-- b001507 | prose | pages [28] -->
4 4 4 2

<!-- b001508 | prose | pages [28] -->
5 5 5 4

<!-- b001509 | prose | pages [28] -->
1 1 1 1

<!-- b001510 | prose | pages [28] -->
2 2 2 2

<!-- b001511 | prose | pages [28] -->
4 4 4 2

<!-- b001512 | prose | pages [28] -->
2 2 2 2

<!-- b001513 | prose | pages [28] -->
2 2 2 2

<!-- b001514 | prose | pages [28] -->
7 7 5 4

<!-- b001515 | prose | pages [28] -->
6

<!-- b001516 | prose | pages [28] -->
5

<!-- b001517 | prose | pages [28] -->
clusters

<!-- b001518 | prose | pages [28] -->
clusters

<!-- b001519 | prose | pages [28] -->
1 1

<!-- b001520 | prose | pages [28] -->
2 2

<!-- b001521 | prose | pages [28] -->
关注数学模型

<!-- b001522 | furniture | pages [28] -->
2

<!-- b001523 | furniture | pages [28] -->
MATHmodels

<!-- b001524 | furniture | pages [28] -->
获取更多资讯

<!-- b001525 | furniture | pages [29] -->
Team # 2010638                                                                   Page 6 of 20

<!-- b001526 | prose | pages [29] -->
3:

<!-- b001527 | prose | pages [29] -->
3 3 1 1

<!-- b001528 | prose | pages [29] -->
1398002

<!-- b001529 | prose | pages [29] -->
4:

<!-- b001530 | prose | pages [29] -->
3 3 1 1

<!-- b001531 | prose | pages [29] -->
1439995

<!-- b001532 | prose | pages [29] -->
5:

<!-- b001533 | prose | pages [29] -->
4 2 2 2

<!-- b001534 | prose | pages [29] -->
1448183

<!-- b001535 | prose | pages [29] -->
6:

<!-- b001536 | prose | pages [29] -->
3 3 1 1

<!-- b001537 | prose | pages [29] -->
1696639

<!-- b001538 | prose | pages [29] -->
7:

<!-- b001539 | prose | pages [29] -->
4 2 2 2

<!-- b001540 | prose | pages [29] -->
1892472

<!-- b001541 | prose | pages [29] -->
8:

<!-- b001542 | prose | pages [29] -->
5 4 3 3

<!-- b001543 | prose | pages [29] -->
2143250

<!-- b001544 | prose | pages [29] -->
9:

<!-- b001545 | prose | pages [29] -->
4 2 2 2

<!-- b001546 | prose | pages [29] -->
2332208

<!-- b001547 | prose | pages [29] -->
10:

<!-- b001548 | prose | pages [29] -->
4 2 2 2

<!-- b001549 | prose | pages [29] -->
2341622

<!-- b001550 | prose | pages [29] -->
11:

<!-- b001551 | prose | pages [29] -->
4 2 2 2

<!-- b001552 | prose | pages [29] -->
2775015

<!-- b001553 | prose | pages [29] -->
12:

<!-- b001554 | prose | pages [29] -->
6 5 4 4

<!-- b001555 | prose | pages [29] -->
3090006

<!-- b001556 | prose | pages [29] -->
13:

<!-- b001557 | prose | pages [29] -->
3 3 1 1

<!-- b001558 | prose | pages [29] -->
3146962

<!-- b001559 | prose | pages [29] -->
14:

<!-- b001560 | prose | pages [29] -->
5 4 3 3

<!-- b001561 | prose | pages [29] -->
3179934

<!-- b001562 | prose | pages [29] -->
15:

<!-- b001563 | prose | pages [29] -->
2 2 2 2

<!-- b001564 | prose | pages [29] -->
3729223

<!-- b001565 | prose | pages [29] -->
16:

<!-- b001566 | prose | pages [29] -->
4 2 2 2

<!-- b001567 | prose | pages [29] -->
3916839

<!-- b001568 | prose | pages [29] -->
17:

<!-- b001569 | prose | pages [29] -->
1 1 1 1

<!-- b001570 | prose | pages [29] -->
4145037

<!-- b001571 | prose | pages [29] -->
18:

<!-- b001572 | prose | pages [29] -->
4 2 2 2

<!-- b001573 | prose | pages [29] -->
4569674

<!-- b001574 | prose | pages [29] -->
19:

<!-- b001575 | prose | pages [29] -->
3 3 1 1

<!-- b001576 | prose | pages [29] -->
4649401

<!-- b001577 | prose | pages [29] -->
20:

<!-- b001578 | prose | pages [29] -->
2 2 2 2

<!-- b001579 | prose | pages [29] -->
4792175

<!-- b001580 | prose | pages [29] -->
21:

<!-- b001581 | prose | pages [29] -->
2 2 2 2

<!-- b001582 | prose | pages [29] -->
5180901

<!-- b001583 | prose | pages [29] -->
22:

<!-- b001584 | prose | pages [29] -->
2 2 2 2

<!-- b001585 | prose | pages [29] -->
5471085

<!-- b001586 | prose | pages [29] -->
23:

<!-- b001587 | prose | pages [29] -->
4 2 2 2

<!-- b001588 | prose | pages [29] -->
5645959

<!-- b001589 | prose | pages [29] -->
24:

<!-- b001590 | prose | pages [29] -->
4 2 2 2

<!-- b001591 | prose | pages [29] -->
5747909

<!-- b001592 | furniture | pages [29] -->


<!-- b001593 | prose | pages [29] -->
1 1

<!-- b001594 | prose | pages [29] -->
1 1

<!-- b001595 | prose | pages [29] -->
2 2

<!-- b001596 | prose | pages [29] -->
1 1

<!-- b001597 | prose | pages [29] -->
2 2

<!-- b001598 | prose | pages [29] -->
3 3

<!-- b001599 | prose | pages [29] -->
2 2

<!-- b001600 | prose | pages [29] -->
2 2

<!-- b001601 | prose | pages [29] -->
2 2

<!-- b001602 | prose | pages [29] -->
3 3

<!-- b001603 | prose | pages [29] -->
1 1

<!-- b001604 | prose | pages [29] -->
3 3

<!-- b001605 | prose | pages [29] -->
2 2

<!-- b001606 | prose | pages [29] -->
2 2

<!-- b001607 | prose | pages [29] -->
1 1

<!-- b001608 | prose | pages [29] -->
2 2

<!-- b001609 | prose | pages [29] -->
1 1

<!-- b001610 | prose | pages [29] -->
2 2

<!-- b001611 | prose | pages [29] -->
2 2

<!-- b001612 | prose | pages [29] -->
2 2

<!-- b001613 | prose | pages [29] -->
2 2

<!-- b001614 | prose | pages [29] -->
2 2

<!-- b001615 | prose | pages [29] -->
关注数学模型

<!-- b001616 | furniture | pages [29] -->
2

<!-- b001617 | furniture | pages [29] -->
MATHmodels

<!-- b001618 | furniture | pages [29] -->
获取更多资讯

<!-- b001619 | furniture | pages [30] -->
Team # 2010638                                                                   Page 7 of 20

<!-- b001620 | prose | pages [30] -->
25:

<!-- b001621 | prose | pages [30] -->
4 2 2 2

<!-- b001622 | prose | pages [30] -->
5749221

<!-- b001623 | prose | pages [30] -->
26:

<!-- b001624 | prose | pages [30] -->
4 2 2 2

<!-- b001625 | prose | pages [30] -->
5848633

<!-- b001626 | prose | pages [30] -->
27:

<!-- b001627 | prose | pages [30] -->
4 2 2 2

<!-- b001628 | prose | pages [30] -->
5981131

<!-- b001629 | prose | pages [30] -->
28:

<!-- b001630 | prose | pages [30] -->
2 2 2 2

<!-- b001631 | prose | pages [30] -->
6156155

<!-- b001632 | prose | pages [30] -->
29:

<!-- b001633 | prose | pages [30] -->
2 2 2 2

<!-- b001634 | prose | pages [30] -->
6744486

<!-- b001635 | prose | pages [30] -->
30:

<!-- b001636 | prose | pages [30] -->
2 2 2 2

<!-- b001637 | prose | pages [30] -->
6784496

<!-- b001638 | prose | pages [30] -->
31:

<!-- b001639 | prose | pages [30] -->
4 2 2 2

<!-- b001640 | prose | pages [30] -->
7090204

<!-- b001641 | prose | pages [30] -->
3.

<!-- b001642 | prose | pages [30] -->
Hair

<!-- b001643 | prose | pages [30] -->
10

<!-- b001644 | prose | pages [30] -->
9

<!-- b001645 | prose | pages [30] -->
8

<!-- b001646 | prose | pages [30] -->
7

<!-- b001647 | prose | pages [30] -->
dryer

<!-- b001648 | prose | pages [30] -->
clusters

<!-- b001649 | prose | pages [30] -->
clusters

<!-- b001650 | prose | pages [30] -->
clusters

<!-- b001651 | prose | pages [30] -->
clusters

<!-- b001652 | prose | pages [30] -->
1:

<!-- b001653 | prose | pages [30] -->
1 1 1 1

<!-- b001654 | prose | pages [30] -->
423960

<!-- b001655 | prose | pages [30] -->
2:

<!-- b001656 | prose | pages [30] -->
2 2 2 1

<!-- b001657 | prose | pages [30] -->
4120409

<!-- b001658 | prose | pages [30] -->
3:

<!-- b001659 | prose | pages [30] -->
3 3 3 2

<!-- b001660 | prose | pages [30] -->
11468070

<!-- b001661 | prose | pages [30] -->
4:

<!-- b001662 | prose | pages [30] -->
2 2 2 1

<!-- b001663 | prose | pages [30] -->
12536427

<!-- b001664 | prose | pages [30] -->
5:

<!-- b001665 | prose | pages [30] -->
2 2 2 1

<!-- b001666 | prose | pages [30] -->
14552349

<!-- b001667 | prose | pages [30] -->
6:

<!-- b001668 | prose | pages [30] -->
1 1 1 1

<!-- b001669 | prose | pages [30] -->
16483457

<!-- b001670 | prose | pages [30] -->
7:

<!-- b001671 | prose | pages [30] -->
2 2 2 1

<!-- b001672 | prose | pages [30] -->
16983648

<!-- b001673 | prose | pages [30] -->
8:

<!-- b001674 | prose | pages [30] -->
2 2 2 1

<!-- b001675 | prose | pages [30] -->
21033180

<!-- b001676 | prose | pages [30] -->
9:

<!-- b001677 | prose | pages [30] -->
2 2 2 1

<!-- b001678 | prose | pages [30] -->
21750700

<!-- b001679 | prose | pages [30] -->
10:

<!-- b001680 | prose | pages [30] -->
1 1 1 1

<!-- b001681 | prose | pages [30] -->
26711891

<!-- b001682 | prose | pages [30] -->
11:

<!-- b001683 | prose | pages [30] -->
3 3 3 2

<!-- b001684 | prose | pages [30] -->
30965255

<!-- b001685 | prose | pages [30] -->
12:

<!-- b001686 | prose | pages [30] -->
4 4 4 3

<!-- b001687 | prose | pages [30] -->
44138644

<!-- b001688 | prose | pages [30] -->
13:

<!-- b001689 | prose | pages [30] -->
5 5 5 4

<!-- b001690 | prose | pages [30] -->
44703144

<!-- b001691 | furniture | pages [30] -->


<!-- b001692 | prose | pages [30] -->
2 2

<!-- b001693 | prose | pages [30] -->
2 2

<!-- b001694 | prose | pages [30] -->
2 2

<!-- b001695 | prose | pages [30] -->
2 2

<!-- b001696 | prose | pages [30] -->
2 2

<!-- b001697 | prose | pages [30] -->
2 2

<!-- b001698 | prose | pages [30] -->
2 2

<!-- b001699 | prose | pages [30] -->
6

<!-- b001700 | prose | pages [30] -->
clusters

<!-- b001701 | prose | pages [30] -->
1

<!-- b001702 | prose | pages [30] -->
1

<!-- b001703 | prose | pages [30] -->
2

<!-- b001704 | prose | pages [30] -->
1

<!-- b001705 | prose | pages [30] -->
1

<!-- b001706 | prose | pages [30] -->
1

<!-- b001707 | prose | pages [30] -->
1

<!-- b001708 | prose | pages [30] -->
1

<!-- b001709 | prose | pages [30] -->
1

<!-- b001710 | prose | pages [30] -->
1

<!-- b001711 | prose | pages [30] -->
2

<!-- b001712 | prose | pages [30] -->
3

<!-- b001713 | prose | pages [30] -->
4

<!-- b001714 | prose | pages [30] -->
关注数学模型

<!-- b001715 | furniture | pages [30] -->
2

<!-- b001716 | furniture | pages [30] -->
MATHmodels

<!-- b001717 | furniture | pages [30] -->
获取更多资讯

<!-- b001718 | furniture | pages [31] -->
Team # 2010638                                                                   Page 8 of 20

<!-- b001719 | prose | pages [31] -->
14:

<!-- b001720 | prose | pages [31] -->
1 1 1 1

<!-- b001721 | prose | pages [31] -->
45575190

<!-- b001722 | prose | pages [31] -->
15:

<!-- b001723 | prose | pages [31] -->
2 2 2 1

<!-- b001724 | prose | pages [31] -->
46450049

<!-- b001725 | prose | pages [31] -->
16:

<!-- b001726 | prose | pages [31] -->
2 2 2 1

<!-- b001727 | prose | pages [31] -->
46677591

<!-- b001728 | prose | pages [31] -->
17:

<!-- b001729 | prose | pages [31] -->
1 1 1 1

<!-- b001730 | prose | pages [31] -->
47684938

<!-- b001731 | prose | pages [31] -->
18:

<!-- b001732 | prose | pages [31] -->
2 2 2 1

<!-- b001733 | prose | pages [31] -->
50000317

<!-- b001734 | prose | pages [31] -->
19:

<!-- b001735 | prose | pages [31] -->
2 2 2 1

<!-- b001736 | prose | pages [31] -->
54378879

<!-- b001737 | prose | pages [31] -->
20:

<!-- b001738 | prose | pages [31] -->
4 4 4 3

<!-- b001739 | prose | pages [31] -->
54987170

<!-- b001740 | prose | pages [31] -->
21:

<!-- b001741 | prose | pages [31] -->
1 1 1 1

<!-- b001742 | prose | pages [31] -->
55445525

<!-- b001743 | prose | pages [31] -->
22:

<!-- b001744 | prose | pages [31] -->
2 2 2 1

<!-- b001745 | prose | pages [31] -->
55520986

<!-- b001746 | prose | pages [31] -->
23:

<!-- b001747 | prose | pages [31] -->
1 1 1 1

<!-- b001748 | prose | pages [31] -->
57056668

<!-- b001749 | prose | pages [31] -->
24:

<!-- b001750 | prose | pages [31] -->
4 4 4 3

<!-- b001751 | prose | pages [31] -->
61225676

<!-- b001752 | prose | pages [31] -->
25:

<!-- b001753 | prose | pages [31] -->
6 1 1 1

<!-- b001754 | prose | pages [31] -->
62808517

<!-- b001755 | prose | pages [31] -->
26:

<!-- b001756 | prose | pages [31] -->
2 2 2 1

<!-- b001757 | prose | pages [31] -->
64142513

<!-- b001758 | prose | pages [31] -->
27:

<!-- b001759 | prose | pages [31] -->
1 1 1 1

<!-- b001760 | prose | pages [31] -->
66014174

<!-- b001761 | prose | pages [31] -->
28:

<!-- b001762 | prose | pages [31] -->
1 1 1 1

<!-- b001763 | prose | pages [31] -->
66259499

<!-- b001764 | prose | pages [31] -->
29:

<!-- b001765 | prose | pages [31] -->
2 2 2 1

<!-- b001766 | prose | pages [31] -->
66279275

<!-- b001767 | prose | pages [31] -->
30:

<!-- b001768 | prose | pages [31] -->
1 1 1 1

<!-- b001769 | prose | pages [31] -->
68100320

<!-- b001770 | prose | pages [31] -->
31:

<!-- b001771 | prose | pages [31] -->
2 2 2 1

<!-- b001772 | prose | pages [31] -->
68816102

<!-- b001773 | prose | pages [31] -->
32:

<!-- b001774 | prose | pages [31] -->
4 4 4 3

<!-- b001775 | prose | pages [31] -->
71698270

<!-- b001776 | prose | pages [31] -->
33:

<!-- b001777 | prose | pages [31] -->
7 6 6 5

<!-- b001778 | prose | pages [31] -->
74202592

<!-- b001779 | prose | pages [31] -->
34:

<!-- b001780 | prose | pages [31] -->
1 1 1 1

<!-- b001781 | prose | pages [31] -->
74735317

<!-- b001782 | prose | pages [31] -->
35:

<!-- b001783 | prose | pages [31] -->
2 2 2 1

<!-- b001784 | prose | pages [31] -->
77898021

<!-- b001785 | furniture | pages [31] -->


<!-- b001786 | prose | pages [31] -->
1

<!-- b001787 | prose | pages [31] -->
1

<!-- b001788 | prose | pages [31] -->
1

<!-- b001789 | prose | pages [31] -->
1

<!-- b001790 | prose | pages [31] -->
1

<!-- b001791 | prose | pages [31] -->
1

<!-- b001792 | prose | pages [31] -->
3

<!-- b001793 | prose | pages [31] -->
1

<!-- b001794 | prose | pages [31] -->
1

<!-- b001795 | prose | pages [31] -->
1

<!-- b001796 | prose | pages [31] -->
3

<!-- b001797 | prose | pages [31] -->
1

<!-- b001798 | prose | pages [31] -->
1

<!-- b001799 | prose | pages [31] -->
1

<!-- b001800 | prose | pages [31] -->
1

<!-- b001801 | prose | pages [31] -->
1

<!-- b001802 | prose | pages [31] -->
1

<!-- b001803 | prose | pages [31] -->
1

<!-- b001804 | prose | pages [31] -->
3

<!-- b001805 | prose | pages [31] -->
5

<!-- b001806 | prose | pages [31] -->
1

<!-- b001807 | prose | pages [31] -->
1

<!-- b001808 | prose | pages [31] -->
关注数学模型

<!-- b001809 | furniture | pages [31] -->
2

<!-- b001810 | furniture | pages [31] -->
MATHmodels

<!-- b001811 | furniture | pages [31] -->
获取更多资讯

<!-- b001812 | furniture | pages [32] -->
Team # 2010638                                                                   Page 9 of 20

<!-- b001813 | prose | pages [32] -->
36:

<!-- b001814 | prose | pages [32] -->
8 7 7 6

<!-- b001815 | prose | pages [32] -->
80193353

<!-- b001816 | prose | pages [32] -->
37:

<!-- b001817 | prose | pages [32] -->
1 1 1 1

<!-- b001818 | prose | pages [32] -->
84440271

<!-- b001819 | prose | pages [32] -->
38:

<!-- b001820 | prose | pages [32] -->
2 2 2 1

<!-- b001821 | prose | pages [32] -->
91277457

<!-- b001822 | prose | pages [32] -->
39:

<!-- b001823 | prose | pages [32] -->
1 1 1 1

<!-- b001824 | prose | pages [32] -->
98133587

<!-- b001825 | prose | pages [32] -->
40:

<!-- b001826 | prose | pages [32] -->
2 2 2 1

<!-- b001827 | prose | pages [32] -->
99665579

<!-- b001828 | prose | pages [32] -->
41:10734

<!-- b001829 | prose | pages [32] -->
1 1 1 1

<!-- b001830 | prose | pages [32] -->
1965

<!-- b001831 | prose | pages [32] -->
42:10819

<!-- b001832 | prose | pages [32] -->
1 1 1 1

<!-- b001833 | prose | pages [32] -->
1918

<!-- b001834 | prose | pages [32] -->
43:10910

<!-- b001835 | prose | pages [32] -->
1 1 1 1

<!-- b001836 | prose | pages [32] -->
6777

<!-- b001837 | prose | pages [32] -->
44:11093

<!-- b001838 | prose | pages [32] -->
2 2 2 1

<!-- b001839 | prose | pages [32] -->
5305

<!-- b001840 | prose | pages [32] -->
45:11241

<!-- b001841 | prose | pages [32] -->
9 8 5 4

<!-- b001842 | prose | pages [32] -->
3045

<!-- b001843 | prose | pages [32] -->
46:11526

<!-- b001844 | prose | pages [32] -->
2 2 2 1

<!-- b001845 | prose | pages [32] -->
4052

<!-- b001846 | furniture | pages [32] -->


<!-- b001847 | furniture | pages [32] -->


<!-- b001848 | heading | pages [32] -->
Appendix 4

<!-- b001849 | prose | pages [32] -->
2

<!-- b001850 | prose | pages [32] -->
1

<!-- b001851 | prose | pages [32] -->
1

<!-- b001852 | prose | pages [32] -->
1

<!-- b001853 | prose | pages [32] -->
1

<!-- b001854 | prose | pages [32] -->
1

<!-- b001855 | prose | pages [32] -->
1

<!-- b001856 | prose | pages [32] -->
1

<!-- b001857 | prose | pages [32] -->
1

<!-- b001858 | prose | pages [32] -->
4

<!-- b001859 | prose | pages [32] -->
1

<!-- b001860 | prose | pages [32] -->
Part of the monthly score of review and star rating

<!-- b001861 | heading | pages [32] -->
1. Hair dryer

<!-- b001862 | prose | pages [32] -->
review

<!-- b001863 | prose | pages [32] -->
star_r

<!-- b001864 | prose | pages [32] -->
comp

<!-- b001865 | prose | pages [32] -->
_date

<!-- b001866 | prose | pages [32] -->
ating

<!-- b001867 | prose | pages [32] -->
ound 2002/3

<!-- b001868 | prose | pages [32] -->
3 0.97

<!-- b001869 | prose | pages [32] -->
/31

<!-- b001870 | prose | pages [32] -->
36 2002/4

<!-- b001871 | prose | pages [32] -->
5 0.73

<!-- b001872 | prose | pages [32] -->
/30

<!-- b001873 | prose | pages [32] -->
13 2002/5

<!-- b001874 | prose | pages [32] -->
3.829 0.50

<!-- b001875 | prose | pages [32] -->
/31

<!-- b001876 | prose | pages [32] -->
601 5325 2002/6

<!-- b001877 | prose | pages [32] -->
3.829 0.50

<!-- b001878 | prose | pages [32] -->
/30

<!-- b001879 | prose | pages [32] -->
601 5325 2002/7

<!-- b001880 | prose | pages [32] -->
5 0.95

<!-- b001881 | prose | pages [32] -->
/31

<!-- b001882 | prose | pages [32] -->
92 2002/8

<!-- b001883 | prose | pages [32] -->
3 0.57

<!-- b001884 | prose | pages [32] -->
/31

<!-- b001885 | prose | pages [32] -->
93 2002/9

<!-- b001886 | prose | pages [32] -->
3.829 0.50

<!-- b001887 | prose | pages [32] -->
/30

<!-- b001888 | prose | pages [32] -->
601 5325

<!-- b001889 | furniture | pages [32] -->


<!-- b001890 | prose | pages [32] -->
关注数学模型

<!-- b001891 | furniture | pages [32] -->
2

<!-- b001892 | furniture | pages [32] -->
MATHmodels

<!-- b001893 | furniture | pages [32] -->
获取更多资讯

<!-- b001894 | furniture | pages [33] -->
Team # 2010638                                                                   Page 10 of 20

<!-- b001895 | prose | pages [33] -->
2002/1 3.829 0.50 0/31 601 5325 2002/1 4 0.92 1/30 61 2002/1 5 -0.12 2/31 97 2003/1

<!-- b001896 | prose | pages [33] -->
4.5 0.75

<!-- b001897 | prose | pages [33] -->
/31

<!-- b001898 | prose | pages [33] -->
76 2003/2

<!-- b001899 | prose | pages [33] -->
4 0.89

<!-- b001900 | prose | pages [33] -->
/28

<!-- b001901 | prose | pages [33] -->
9 2003/3

<!-- b001902 | prose | pages [33] -->
4 0.88

<!-- b001903 | prose | pages [33] -->
/31

<!-- b001904 | prose | pages [33] -->
425 2003/4

<!-- b001905 | prose | pages [33] -->
5 0.82

<!-- b001906 | prose | pages [33] -->
/30

<!-- b001907 | prose | pages [33] -->
94 2003/5

<!-- b001908 | prose | pages [33] -->
3.829 0.50

<!-- b001909 | prose | pages [33] -->
/31

<!-- b001910 | prose | pages [33] -->
601 5325 2003/6

<!-- b001911 | prose | pages [33] -->
3.829 0.50

<!-- b001912 | prose | pages [33] -->
/30

<!-- b001913 | prose | pages [33] -->
601 5325 2003/7

<!-- b001914 | prose | pages [33] -->
3.829 0.50

<!-- b001915 | prose | pages [33] -->
/31

<!-- b001916 | prose | pages [33] -->
601 5325 2003/8

<!-- b001917 | prose | pages [33] -->
3.829 0.50

<!-- b001918 | prose | pages [33] -->
/31

<!-- b001919 | prose | pages [33] -->
601 5325 2003/9

<!-- b001920 | prose | pages [33] -->
3.829 0.50

<!-- b001921 | prose | pages [33] -->
/30

<!-- b001922 | prose | pages [33] -->
601 5325 2003/1 3.829 0.50 0/31 601 5325 2003/1 3.829 0.50 1/30 601 5325 2003/1 3.829 0.50 2/31 601 5325 2004/1

<!-- b001923 | prose | pages [33] -->
2.5 0.08

<!-- b001924 | prose | pages [33] -->
/31

<!-- b001925 | prose | pages [33] -->
485 2004/2

<!-- b001926 | prose | pages [33] -->
3.829 0.50

<!-- b001927 | prose | pages [33] -->
/29

<!-- b001928 | prose | pages [33] -->
601 5325 2004/3

<!-- b001929 | prose | pages [33] -->
5 0.95

<!-- b001930 | prose | pages [33] -->
/31

<!-- b001931 | prose | pages [33] -->
955 2004/4

<!-- b001932 | prose | pages [33] -->
3.829 0.50

<!-- b001933 | prose | pages [33] -->
/30

<!-- b001934 | prose | pages [33] -->
601 5325 2004/5

<!-- b001935 | prose | pages [33] -->
1 -0.47

<!-- b001936 | prose | pages [33] -->
/31

<!-- b001937 | prose | pages [33] -->
67 2004/6

<!-- b001938 | prose | pages [33] -->
3.829 0.50

<!-- b001939 | prose | pages [33] -->
/30

<!-- b001940 | prose | pages [33] -->
601 5325 2004/7

<!-- b001941 | prose | pages [33] -->
3.829 0.50

<!-- b001942 | prose | pages [33] -->
/31

<!-- b001943 | prose | pages [33] -->
601 5325

<!-- b001944 | furniture | pages [33] -->


<!-- b001945 | prose | pages [33] -->
关注数学模型

<!-- b001946 | furniture | pages [33] -->
2

<!-- b001947 | furniture | pages [33] -->
MATHmodels

<!-- b001948 | furniture | pages [33] -->
获取更多资讯

<!-- b001949 | furniture | pages [34] -->
Team # 2010638                                                                   Page 11 of 20

<!-- b001950 | prose | pages [34] -->
2004/8

<!-- b001951 | prose | pages [34] -->
2 0.45

<!-- b001952 | prose | pages [34] -->
/31

<!-- b001953 | prose | pages [34] -->
88 2004/9

<!-- b001954 | prose | pages [34] -->
3.829 0.50

<!-- b001955 | prose | pages [34] -->
/30

<!-- b001956 | prose | pages [34] -->
601 5325 2004/1 3.829 0.50 0/31 601 5325 2004/1 4 0.15 1/30 315 2004/1 3.829 0.50 2/31 601 5325 2005/1

<!-- b001957 | prose | pages [34] -->
3.829 0.50

<!-- b001958 | prose | pages [34] -->
/31

<!-- b001959 | prose | pages [34] -->
601 5325 2005/2

<!-- b001960 | prose | pages [34] -->
3.829 0.50

<!-- b001961 | prose | pages [34] -->
/28

<!-- b001962 | prose | pages [34] -->
601 5325 2005/3

<!-- b001963 | prose | pages [34] -->
3.829 0.50

<!-- b001964 | prose | pages [34] -->
/31

<!-- b001965 | prose | pages [34] -->
601 5325 2005/4

<!-- b001966 | prose | pages [34] -->
1 -0.47

<!-- b001967 | prose | pages [34] -->
/30

<!-- b001968 | prose | pages [34] -->
14 2005/5

<!-- b001969 | prose | pages [34] -->
1 -0.29

<!-- b001970 | prose | pages [34] -->
/31

<!-- b001971 | prose | pages [34] -->
66 2005/6

<!-- b001972 | prose | pages [34] -->
5 0.20

<!-- b001973 | prose | pages [34] -->
/30

<!-- b001974 | prose | pages [34] -->
08 2005/7

<!-- b001975 | prose | pages [34] -->
5 -0.40

<!-- b001976 | prose | pages [34] -->
/31

<!-- b001977 | prose | pages [34] -->
66 2005/8

<!-- b001978 | prose | pages [34] -->
3 0.82

<!-- b001979 | prose | pages [34] -->
/31

<!-- b001980 | prose | pages [34] -->
55 2005/9

<!-- b001981 | prose | pages [34] -->
4.333 0.80

<!-- b001982 | prose | pages [34] -->
/30

<!-- b001983 | prose | pages [34] -->
333 87 2005/1 5 0.83 0/31 9467 2005/1 3.5 0.88 1/30 995 2005/1 4.5 0.68 2/31 685 2006/1

<!-- b001984 | prose | pages [34] -->
3.357 0.66

<!-- b001985 | prose | pages [34] -->
/31

<!-- b001986 | prose | pages [34] -->
143 7943 2006/2

<!-- b001987 | prose | pages [34] -->
2.875 0.45

<!-- b001988 | prose | pages [34] -->
/28

<!-- b001989 | prose | pages [34] -->
3613 2006/3

<!-- b001990 | prose | pages [34] -->
3.309 0.21

<!-- b001991 | prose | pages [34] -->
/31

<!-- b001992 | prose | pages [34] -->
524 46 2006/4

<!-- b001993 | prose | pages [34] -->
3 0.39

<!-- b001994 | prose | pages [34] -->
/30

<!-- b001995 | prose | pages [34] -->
6333 2006/5

<!-- b001996 | prose | pages [34] -->
1.666 0.24

<!-- b001997 | prose | pages [34] -->
/31

<!-- b001998 | prose | pages [34] -->
667 26

<!-- b001999 | furniture | pages [34] -->


<!-- b002000 | prose | pages [34] -->
关注数学模型

<!-- b002001 | furniture | pages [34] -->
2

<!-- b002002 | furniture | pages [34] -->
MATHmodels

<!-- b002003 | furniture | pages [34] -->
获取更多资讯

<!-- b002004 | furniture | pages [35] -->
Team # 2010638                                                                   Page 12 of 20

<!-- b002005 | prose | pages [35] -->
2006/6

<!-- b002006 | prose | pages [35] -->
2 0.37

<!-- b002007 | prose | pages [35] -->
/30

<!-- b002008 | prose | pages [35] -->
806 2006/7

<!-- b002009 | prose | pages [35] -->
3.333 0.44

<!-- b002010 | prose | pages [35] -->
/31

<!-- b002011 | prose | pages [35] -->
333 7167

<!-- b002012 | furniture | pages [35] -->


<!-- b002013 | heading | pages [35] -->
2. Pacifier

<!-- b002014 | prose | pages [35] -->
review

<!-- b002015 | prose | pages [35] -->
star_r

<!-- b002016 | prose | pages [35] -->
comp

<!-- b002017 | prose | pages [35] -->
_date

<!-- b002018 | prose | pages [35] -->
ating

<!-- b002019 | prose | pages [35] -->
ound 2003/4

<!-- b002020 | prose | pages [35] -->
2 0.58

<!-- b002021 | prose | pages [35] -->
/30

<!-- b002022 | prose | pages [35] -->
35 2003/5

<!-- b002023 | prose | pages [35] -->
4.4 0.60

<!-- b002024 | prose | pages [35] -->
/31

<!-- b002025 | prose | pages [35] -->
842 2003/6

<!-- b002026 | prose | pages [35] -->
4.333 0.77

<!-- b002027 | prose | pages [35] -->
/30

<!-- b002028 | prose | pages [35] -->
333 0685 2003/7

<!-- b002029 | prose | pages [35] -->
3.375 0.74

<!-- b002030 | prose | pages [35] -->
/31

<!-- b002031 | prose | pages [35] -->
2837 2003/8

<!-- b002032 | prose | pages [35] -->
4.111 0.48

<!-- b002033 | prose | pages [35] -->
/31

<!-- b002034 | prose | pages [35] -->
111 7467 2003/9

<!-- b002035 | prose | pages [35] -->
4.210 0.57

<!-- b002036 | prose | pages [35] -->
/30

<!-- b002037 | prose | pages [35] -->
547 1278 2003/1 4.55 0.75 0/31 1675 2003/1 3.605 0.52 1/30 442 3395 2003/1 1 0.92 2/31

<!-- b002038 | prose | pages [35] -->
2004/1

<!-- b002039 | prose | pages [35] -->
4.137 0.69

<!-- b002040 | prose | pages [35] -->
/31

<!-- b002041 | prose | pages [35] -->
209 7009 2004/2

<!-- b002042 | prose | pages [35] -->
4.196 0.70

<!-- b002043 | prose | pages [35] -->
/29

<!-- b002044 | prose | pages [35] -->
297 3307 2004/3

<!-- b002045 | prose | pages [35] -->
4.146 0.45

<!-- b002046 | prose | pages [35] -->
/31

<!-- b002047 | prose | pages [35] -->
052 704 2004/4

<!-- b002048 | prose | pages [35] -->
4.5 0.67

<!-- b002049 | prose | pages [35] -->
/30

<!-- b002050 | prose | pages [35] -->
37 2004/5

<!-- b002051 | prose | pages [35] -->
2 0.91

<!-- b002052 | prose | pages [35] -->
/31

<!-- b002053 | prose | pages [35] -->
86 2004/6

<!-- b002054 | prose | pages [35] -->
2 0.81

<!-- b002055 | prose | pages [35] -->
/30

<!-- b002056 | prose | pages [35] -->
08 2004/7

<!-- b002057 | prose | pages [35] -->
4.499 0.65

<!-- b002058 | prose | pages [35] -->
/31

<!-- b002059 | prose | pages [35] -->
116 3345 2004/8

<!-- b002060 | prose | pages [35] -->
4.455 0.64

<!-- b002061 | prose | pages [35] -->
/31

<!-- b002062 | prose | pages [35] -->
441 6819 2004/9

<!-- b002063 | prose | pages [35] -->
4.361 0.58

<!-- b002064 | prose | pages [35] -->
/30

<!-- b002065 | prose | pages [35] -->
652 1429

<!-- b002066 | furniture | pages [35] -->


<!-- b002067 | prose | pages [35] -->
关注数学模型

<!-- b002068 | furniture | pages [35] -->
2

<!-- b002069 | furniture | pages [35] -->
MATHmodels

<!-- b002070 | furniture | pages [35] -->
获取更多资讯

<!-- b002071 | furniture | pages [36] -->
Team # 2010638                                                                   Page 13 of 20

<!-- b002072 | prose | pages [36] -->
2004/1 4.452 0.64 0/31 883 6562 2004/1 4.379 0.66 1/30 498 2509 2004/1 4.344 0.62 2/31 347 298 2005/1

<!-- b002073 | prose | pages [36] -->
4.333 0.59

<!-- b002074 | prose | pages [36] -->
/31

<!-- b002075 | prose | pages [36] -->
011 3006 2005/2

<!-- b002076 | prose | pages [36] -->
5 0.96

<!-- b002077 | prose | pages [36] -->
/28

<!-- b002078 | prose | pages [36] -->
96 2005/3

<!-- b002079 | prose | pages [36] -->
3.534 0.49

<!-- b002080 | prose | pages [36] -->
/31

<!-- b002081 | prose | pages [36] -->
091 2098 2005/4

<!-- b002082 | prose | pages [36] -->
3.883 0.63

<!-- b002083 | prose | pages [36] -->
/30

<!-- b002084 | prose | pages [36] -->
333 9112 2005/5

<!-- b002085 | prose | pages [36] -->
4.391 0.50

<!-- b002086 | prose | pages [36] -->
/31

<!-- b002087 | prose | pages [36] -->
507 169 2005/6

<!-- b002088 | prose | pages [36] -->
4.296 0.49

<!-- b002089 | prose | pages [36] -->
/30

<!-- b002090 | prose | pages [36] -->
748 209 2005/7

<!-- b002091 | prose | pages [36] -->
4.434 0.52

<!-- b002092 | prose | pages [36] -->
/31

<!-- b002093 | prose | pages [36] -->
554 5116 2005/8

<!-- b002094 | prose | pages [36] -->
4.332 0.49

<!-- b002095 | prose | pages [36] -->
/31

<!-- b002096 | prose | pages [36] -->
839 5799 2005/9

<!-- b002097 | prose | pages [36] -->
4.344 0.51

<!-- b002098 | prose | pages [36] -->
/30

<!-- b002099 | prose | pages [36] -->
876 9694 2005/1 5 0.84 0/31 72 2005/1 5 0.96 1/30 89 2005/1 4.541 0.72 2/31 667 4842 2006/1

<!-- b002100 | prose | pages [36] -->
4.637 0.75

<!-- b002101 | prose | pages [36] -->
/31

<!-- b002102 | prose | pages [36] -->
5 9315 2006/2

<!-- b002103 | prose | pages [36] -->
4 0.94

<!-- b002104 | prose | pages [36] -->
/28

<!-- b002105 | prose | pages [36] -->
06 2006/3

<!-- b002106 | prose | pages [36] -->
5 0.94

<!-- b002107 | prose | pages [36] -->
/31

<!-- b002108 | prose | pages [36] -->
94 2006/4

<!-- b002109 | prose | pages [36] -->
3.534 0.49

<!-- b002110 | prose | pages [36] -->
/30

<!-- b002111 | prose | pages [36] -->
091 2098 2006/5

<!-- b002112 | prose | pages [36] -->
2.7 0.75

<!-- b002113 | prose | pages [36] -->
/31

<!-- b002114 | prose | pages [36] -->
511 2006/6

<!-- b002115 | prose | pages [36] -->
3.666 0.21

<!-- b002116 | prose | pages [36] -->
/30

<!-- b002117 | prose | pages [36] -->
667 575 2006/7

<!-- b002118 | prose | pages [36] -->
4.267 0.54

<!-- b002119 | prose | pages [36] -->
/31

<!-- b002120 | prose | pages [36] -->
442 0129

<!-- b002121 | furniture | pages [36] -->


<!-- b002122 | prose | pages [36] -->
关注数学模型

<!-- b002123 | furniture | pages [36] -->
2

<!-- b002124 | furniture | pages [36] -->
MATHmodels

<!-- b002125 | furniture | pages [36] -->
获取更多资讯

<!-- b002126 | furniture | pages [37] -->
Team # 2010638                                                                   Page 14 of 20

<!-- b002127 | prose | pages [37] -->
2006/8

<!-- b002128 | prose | pages [37] -->
5 0.96

<!-- b002129 | prose | pages [37] -->
/31

<!-- b002130 | prose | pages [37] -->
91 2006/9

<!-- b002131 | prose | pages [37] -->
4.25 0.73

<!-- b002132 | prose | pages [37] -->
/30

<!-- b002133 | prose | pages [37] -->
5613 2006/1 5 0.95 0/31 905 2006/1 3 0.73 1/30 49

<!-- b002134 | heading | pages [37] -->
3. Microwave oven

<!-- b002135 | prose | pages [37] -->
review

<!-- b002136 | prose | pages [37] -->
star_r

<!-- b002137 | prose | pages [37] -->
comp

<!-- b002138 | prose | pages [37] -->
_date

<!-- b002139 | prose | pages [37] -->
ating

<!-- b002140 | prose | pages [37] -->
ound 2004/6

<!-- b002141 | prose | pages [37] -->
4 0.70

<!-- b002142 | prose | pages [37] -->
/30

<!-- b002143 | prose | pages [37] -->
5233 2004/7

<!-- b002144 | prose | pages [37] -->
3 -0.79

<!-- b002145 | prose | pages [37] -->
/31

<!-- b002146 | prose | pages [37] -->
92 2004/8

<!-- b002147 | prose | pages [37] -->
1 -0.42

<!-- b002148 | prose | pages [37] -->
/31

<!-- b002149 | prose | pages [37] -->
15 2004/9

<!-- b002150 | prose | pages [37] -->
1.333 0.24

<!-- b002151 | prose | pages [37] -->
/30

<!-- b002152 | prose | pages [37] -->
333 1867 2004/1 5 0.99 0/31 25 2004/1 3 0.50 1/30 63 2004/1 3 0.98 2/31 18 2005/1

<!-- b002153 | prose | pages [37] -->
5 0.98

<!-- b002154 | prose | pages [37] -->
/31

<!-- b002155 | prose | pages [37] -->
54 2005/2

<!-- b002156 | prose | pages [37] -->
3 0.34

<!-- b002157 | prose | pages [37] -->
/28

<!-- b002158 | prose | pages [37] -->
7794 2005/3

<!-- b002159 | prose | pages [37] -->
2.773 0.16

<!-- b002160 | prose | pages [37] -->
/31

<!-- b002161 | prose | pages [37] -->
333 9515 2005/4

<!-- b002162 | prose | pages [37] -->
2.865 0.36

<!-- b002163 | prose | pages [37] -->
/30

<!-- b002164 | prose | pages [37] -->
385 0717 2005/5

<!-- b002165 | prose | pages [37] -->
3 0.32

<!-- b002166 | prose | pages [37] -->
/31

<!-- b002167 | prose | pages [37] -->
0475 2005/6

<!-- b002168 | prose | pages [37] -->
3 0.41

<!-- b002169 | prose | pages [37] -->
/30

<!-- b002170 | prose | pages [37] -->
8019 2005/7

<!-- b002171 | prose | pages [37] -->
5 -0.52

<!-- b002172 | prose | pages [37] -->
/31

<!-- b002173 | prose | pages [37] -->
67 2005/8

<!-- b002174 | prose | pages [37] -->
2.773 0.16

<!-- b002175 | prose | pages [37] -->
/31

<!-- b002176 | prose | pages [37] -->
333 9515 2005/9

<!-- b002177 | prose | pages [37] -->
2.865 0.36

<!-- b002178 | prose | pages [37] -->
/30

<!-- b002179 | prose | pages [37] -->
385 0717

<!-- b002180 | furniture | pages [37] -->


<!-- b002181 | prose | pages [37] -->
关注数学模型

<!-- b002182 | furniture | pages [37] -->
2

<!-- b002183 | furniture | pages [37] -->
MATHmodels

<!-- b002184 | furniture | pages [37] -->
获取更多资讯

<!-- b002185 | furniture | pages [38] -->
Team # 2010638                                                                   Page 15 of 20

<!-- b002186 | prose | pages [38] -->
2005/1 4 0.87 0/31 4467 2005/1 5 0.99 1/30 25 2005/1 2 -0.57 2/31 07 2006/1

<!-- b002187 | prose | pages [38] -->
3.294 0.25

<!-- b002188 | prose | pages [38] -->
/31

<!-- b002189 | prose | pages [38] -->
118 3166 2006/2

<!-- b002190 | prose | pages [38] -->
3.857 0.48

<!-- b002191 | prose | pages [38] -->
/28

<!-- b002192 | prose | pages [38] -->
143 14 2006/3

<!-- b002193 | prose | pages [38] -->
3.177 0.29

<!-- b002194 | prose | pages [38] -->
/31

<!-- b002195 | prose | pages [38] -->
083 0946 2006/4

<!-- b002196 | prose | pages [38] -->
3.156 0.35

<!-- b002197 | prose | pages [38] -->
/30

<!-- b002198 | prose | pages [38] -->
25 2928 2006/5

<!-- b002199 | prose | pages [38] -->
3.115 0.60

<!-- b002200 | prose | pages [38] -->
/31

<!-- b002201 | prose | pages [38] -->
385 2631 2006/6

<!-- b002202 | prose | pages [38] -->
1 -0.42

<!-- b002203 | prose | pages [38] -->
/30

<!-- b002204 | prose | pages [38] -->
15 2006/7

<!-- b002205 | prose | pages [38] -->
3.634 0.31

<!-- b002206 | prose | pages [38] -->
/31

<!-- b002207 | prose | pages [38] -->
921 9398 2006/8

<!-- b002208 | prose | pages [38] -->
3.384 0.12

<!-- b002209 | prose | pages [38] -->
/31

<!-- b002210 | prose | pages [38] -->
615 6777 2006/9

<!-- b002211 | prose | pages [38] -->
3.291 0.51

<!-- b002212 | prose | pages [38] -->
/30

<!-- b002213 | prose | pages [38] -->
667 0772 2006/1 3.533 0.44 0/31 333 5201 2006/1 3.793 0.31 1/30 333 3961 2006/1 3.378 0.29 2/31 788 0235 2007/1

<!-- b002214 | prose | pages [38] -->
5 0.98

<!-- b002215 | prose | pages [38] -->
/31

<!-- b002216 | prose | pages [38] -->
68 2007/2

<!-- b002217 | prose | pages [38] -->
4.5 0.92

<!-- b002218 | prose | pages [38] -->
/28

<!-- b002219 | prose | pages [38] -->
94 2007/3

<!-- b002220 | prose | pages [38] -->
5 0.94

<!-- b002221 | prose | pages [38] -->
/31

<!-- b002222 | prose | pages [38] -->
59 2007/4

<!-- b002223 | prose | pages [38] -->
3.177 0.29

<!-- b002224 | prose | pages [38] -->
/30

<!-- b002225 | prose | pages [38] -->
083 0946 2007/5

<!-- b002226 | prose | pages [38] -->
3.156 0.35

<!-- b002227 | prose | pages [38] -->
/31

<!-- b002228 | prose | pages [38] -->
25 2928 2007/6

<!-- b002229 | prose | pages [38] -->
5 0.86

<!-- b002230 | prose | pages [38] -->
/30

<!-- b002231 | prose | pages [38] -->
13 2007/7

<!-- b002232 | prose | pages [38] -->
4 0.68

<!-- b002233 | prose | pages [38] -->
/31

<!-- b002234 | prose | pages [38] -->
08

<!-- b002235 | furniture | pages [38] -->


<!-- b002236 | prose | pages [38] -->
关注数学模型

<!-- b002237 | furniture | pages [38] -->
2

<!-- b002238 | furniture | pages [38] -->
MATHmodels

<!-- b002239 | furniture | pages [38] -->
获取更多资讯

<!-- b002240 | furniture | pages [39] -->
Team # 2010638                                                                   Page 16 of 20

<!-- b002241 | prose | pages [39] -->
2007/8

<!-- b002242 | prose | pages [39] -->
3 0.58

<!-- b002243 | prose | pages [39] -->
/31

<!-- b002244 | prose | pages [39] -->
66 2007/9

<!-- b002245 | prose | pages [39] -->
4 -0.55

<!-- b002246 | prose | pages [39] -->
/30

<!-- b002247 | prose | pages [39] -->
29 2007/1 2.364 -0.08 0/31 583 993 2007/1 4.5 0.70 1/30 06 2007/1 5 0.97 2/31 7667 2008/1

<!-- b002248 | prose | pages [39] -->
2.364 -0.08

<!-- b002249 | prose | pages [39] -->
/31

<!-- b002250 | prose | pages [39] -->
583 993 2008/2

<!-- b002251 | prose | pages [39] -->
3.666 -0.28

<!-- b002252 | prose | pages [39] -->
/29

<!-- b002253 | prose | pages [39] -->
667 567 2008/3

<!-- b002254 | prose | pages [39] -->
3 0.67

<!-- b002255 | prose | pages [39] -->
/31

<!-- b002256 | prose | pages [39] -->
05 2008/4

<!-- b002257 | prose | pages [39] -->
2 -0.51

<!-- b002258 | prose | pages [39] -->
/30

<!-- b002259 | prose | pages [39] -->
06 2008/5

<!-- b002260 | prose | pages [39] -->
3.4 0.41

<!-- b002261 | prose | pages [39] -->
/31

<!-- b002262 | prose | pages [39] -->
524 2008/6

<!-- b002263 | prose | pages [39] -->
2.865 0.36

<!-- b002264 | prose | pages [39] -->
/30

<!-- b002265 | prose | pages [39] -->
385 0717 2008/7

<!-- b002266 | prose | pages [39] -->
2.666 -0.13

<!-- b002267 | prose | pages [39] -->
/31

<!-- b002268 | prose | pages [39] -->
667 823 2008/8

<!-- b002269 | prose | pages [39] -->
3.666 0.79

<!-- b002270 | prose | pages [39] -->
/31

<!-- b002271 | prose | pages [39] -->
667 5633 2008/9

<!-- b002272 | prose | pages [39] -->
2.364 -0.08

<!-- b002273 | prose | pages [39] -->
/30

<!-- b002274 | prose | pages [39] -->
583 993 2008/1 3.433 0.17 0/31 333 2403 2008/1 2.364 -0.08 1/30 583 993 2008/1 4 0.63 2/31 69 2009/1

<!-- b002275 | prose | pages [39] -->
3.1 0.22

<!-- b002276 | prose | pages [39] -->
/31

<!-- b002277 | prose | pages [39] -->
467 2009/2

<!-- b002278 | prose | pages [39] -->
3 0.21

<!-- b002279 | prose | pages [39] -->
/28

<!-- b002280 | prose | pages [39] -->
4 2009/3

<!-- b002281 | prose | pages [39] -->
2.865 0.36

<!-- b002282 | prose | pages [39] -->
/31

<!-- b002283 | prose | pages [39] -->
385 0717 2009/4

<!-- b002284 | prose | pages [39] -->
5 0.92

<!-- b002285 | prose | pages [39] -->
/30

<!-- b002286 | prose | pages [39] -->
57 2009/5

<!-- b002287 | prose | pages [39] -->
2.25 0.08

<!-- b002288 | prose | pages [39] -->
/31

<!-- b002289 | prose | pages [39] -->
9067

<!-- b002290 | furniture | pages [39] -->


<!-- b002291 | prose | pages [39] -->
关注数学模型

<!-- b002292 | furniture | pages [39] -->
2

<!-- b002293 | furniture | pages [39] -->
MATHmodels

<!-- b002294 | furniture | pages [39] -->
获取更多资讯

<!-- b002295 | furniture | pages [40] -->
Team # 2010638                                                                   Page 17 of 20

<!-- b002296 | prose | pages [40] -->
2009/6

<!-- b002297 | prose | pages [40] -->
5 0.49

<!-- b002298 | prose | pages [40] -->
/30

<!-- b002299 | prose | pages [40] -->
495 2009/7

<!-- b002300 | prose | pages [40] -->
1 -0.85

<!-- b002301 | prose | pages [40] -->
/31

<!-- b002302 | prose | pages [40] -->
16 2009/8

<!-- b002303 | prose | pages [40] -->
1 0

<!-- b002304 | prose | pages [40] -->
/31

<!-- b002305 | furniture | pages [40] -->


<!-- b002306 | furniture | pages [40] -->


<!-- b002307 | heading | pages [40] -->
Appendix 5

<!-- b002308 | heading | pages [40] -->
1. Code of LDA model

<!-- b002309 | prose | pages [40] -->
import pandas as pd from snownlp import SnowNLP import re

<!-- b002310 | heading | pages [40] -->
from gensim import corpora,models

<!-- b002311 | prose | pages [40] -->
#from nltk.tokenize import word_tokenize data = pd.DataFrame(test2) print(type(data)) #data_null = data.drop_duplicates() #data_null.to_csv(&apos;C:/Users/lenovo/Desktop/comments_null.csv&apos;) #data_null_comments = data_null[&apos;contents&apos;] #data_null_comments.to_csv(&apos;C:/Users/lenovo/Desktop/contents.txt&apos;,index=False,enco ding=&apos;utf-8&apos;) #data_len = data_null_comments[data_null_comments.str.len()>4] #print(data_len) #data_len.to_csv(&apos;contents.txt&apos;,index=False,encoding=&apos;utf-8&apos;) coms = [] coms = data[0].apply(lambda x:SnowNLP(x).sentiments) data_post = data[coms>=0.01] data_neg = data[coms<0.01] print(data_post) print(data_neg) data_post[0].to_csv(&apos;C:/Users/lenovo/Desktop/comments_positive.txt&apos;,encoding=&apos ;utf-8&apos;,header=None) data_neg[0].to_csv(&apos;C:/Users/lenovo/Desktop/comments_negative.txt&apos;,encoding=&apos ;utf-8-sig&apos;,header=None) with open(&apos;C:/Users/lenovo/Desktop/comments_positive.txt&apos;,encoding=&apos;utf-8&ap os;) as fn1: string_data1 = fn1.read() pattern = re.compile(u&apos;\t|\n|\.|-|——|：|！|、|，|,|。|;|\)|\(|\?|"&apos;) string_data1 = re.sub(pattern, &apos;&apos;, string_data1) print(string_data1) fp = open(&apos;C:/Users/lenovo/Desktop/comments_post.txt&apos;,&apos;a&apos;,encoding =&apos;utf8&apos;)

<!-- b002312 | furniture | pages [40] -->


<!-- b002313 | prose | pages [40] -->
关注数学模型

<!-- b002314 | furniture | pages [40] -->
2

<!-- b002315 | furniture | pages [40] -->
MATHmodels

<!-- b002316 | furniture | pages [40] -->
获取更多资讯

<!-- b002317 | furniture | pages [41] -->
Team # 2010638                                                                   Page 18 of 20

<!-- b002318 | prose | pages [41] -->
fp.write(string_data1 + &apos;\n&apos;) fp.close() with open(&apos;C:/Users/lenovo/Desktop/comments_nagative.txt&apos;,encoding=&apos;utf-8&a pos;) as fn2: string_data2 = fn2.read() pattern = re.compile(u&apos;\t|\n|\.|-|——|：|！|、|，|,|。|;|\)|\(|\?|"&apos;) string_data2 = re.sub(pattern, &apos;&apos;, string_data2) print(string_data2) fp = open(&apos;C:/Users/lenovo/Desktop/comments_neg.txt&apos;,&apos;a&apos;,encoding =&apos;utf8&apos;) fp.write(string_data2 + &apos;\n&apos;) fp.close() data1 = pd.read_csv(&apos;C:/Users/lenovo/Desktop/comments_post.txt&apos;,encoding=&apos;utf -8&apos;,header=None) data2 = pd.read_csv(&apos;C:/Users/lenovo/Desktop/comments_neg.txt&apos;,encoding=&apos;utf -8&apos;,header=None) #mycut = lambda s: &apos; &apos;.join(word_tokenize(s)) #data1 = data1[0].apply(mycut) #data2 = data2[0].apply(mycut) #mycut = lambda s: &apos; &apos;.join(word_tokenize(s)) data1 = data1[0] data2 = data2[0] data1.to_csv(&apos;C:/Users/lenovo/Desktop/comments_post_cut.txt&apos;,index=False,header=Fa lse,encoding=&apos;utf-8&apos;) data2.to_csv(&apos;C:/Users/lenovo/Desktop/comments_neg_cut.txt&apos;,index=False,header=Fal se,encoding=&apos;utf-8&apos;) print(data2) post = pd.read_csv(&apos;C:/Users/lenovo/Desktop/comments_post_cut.txt&apos;,encoding=&apos ;utf-8&apos;,header=None,error_bad_lines=False) neg = pd.read_csv(&apos;C:/Users/lenovo/Desktop/comments_neg_cut.txt&apos;,encoding=&apos; utf-8&apos;,header=None,error_bad_lines=False) stop = pd.read_csv(&apos;C:/Users/lenovo/Desktop/stoplist.txt&apos;,encoding=&apos;utf-8&apos; ,header=None,sep=&apos;tipdm&apos;,engine=&apos;python&apos;) stop = [&apos; &apos;,&apos;&apos;] + list(stop[0]) post[1] = post[0].apply(lambda s: s.split(&apos; &apos;)) post[2] = post[1].apply(lambda x: [i for i in x if i not in stop]) neg[1] = neg[0].apply(lambda s: s.split(&apos; &apos;)) neg[2] = neg[1].apply(lambda x: [i for i in x if i not in stop]) post_dict = corpora.Dictionary(post[2]) post_corpus = [post_dict.doc2bow(i) for i in post[2]]

<!-- b002319 | heading | pages [41] -->
post_lda = models.LdaModel(post_corpus, num_topics=4, id2word=post_dict)

<!-- b002320 | prose | pages [41] -->
for i in range(3): print(post_lda.print_topic(i)) print(&apos)

<!-- b002321 | furniture | pages [41] -->


<!-- b002322 | prose | pages [41] -->
关注数学模型

<!-- b002323 | furniture | pages [41] -->
2

<!-- b002324 | furniture | pages [41] -->
MATHmodels

<!-- b002325 | furniture | pages [41] -->
获取更多资讯

<!-- b002326 | furniture | pages [42] -->
Team # 2010638                                                                   Page 19 of 20

<!-- b002327 | prose | pages [42] -->
neg_dict = corpora.Dictionary(neg[2]) neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]]

<!-- b002328 | heading | pages [42] -->
neg_lda = models.LdaModel(neg_corpus, num_topics=4, id2word=neg_dict)

<!-- b002329 | prose | pages [42] -->
for i in range(3): print(neg_lda.print_topic(i))

<!-- b002330 | furniture | pages [42] -->


<!-- b002331 | heading | pages [42] -->
2. Code of word segmentation and NLTK model

<!-- b002332 | prose | pages [42] -->
import pandas as pd import seaborn as sns import numpy as np from nltk.tokenize import word_tokenize,sent_tokenize import matplotlib.pyplot as plt pacifier=pd.read_csv(&apos;C:/Users/lenovo/Desktop/pacifier.tsv&apos;, sep=&apos;\t&apos;) b = pacifier[&apos;review_body&apos;].duplicated() pacifier[&apos;marketplace&apos;] = pacifier[&apos;marketplace&apos;].str.lower() pacifier[&apos;product_category&apos;] = pacifier[&apos;product_category&apos;].str.lower() pacifier[&apos;vine&apos;] = pacifier[&apos;vine&apos;].str.lower() pacifier[&apos;verified_purchase&apos;] = pacifier[&apos;verified_purchase&apos;].str.lower() text_a_count = [] for i in pacifier[&apos;review_body&apos;]: if isinstance(i,str): print(i,type(i)) print(len(i)) elif isinstance(i,float): print(i,type(i)) i = str(i) text_a_count.append(len(i)) #plt.figure(figsize = (8,6)) u = pacifier[&apos;helpful_votes&apos;] x = np.array(text_a_count) y = np.array(u) p = pd.DataFrame({&apos;review_body_length&apos;:x,&apos;helpful_votes&apos;:y}) #p = p.drop_duplicates([&apos;helpful_votes&apos;]) #color = [&apos;r&apos;,&apos;y&apos;,&apos;k&apos;,&apos;g&apos;,&apos;m&apos;] #plt.scatter(p[&apos;review_body_length&apos;],p[&apos;helpful_votes&apos;],c=color,marker=& apos;>&apos;) #plt.legend() #plt.show() v = pacifier.describe()

<!-- b002333 | prose | pages [42] -->
import pandas as pd import nltk import numpy as np from nltk.tokenize import word_tokenize,sent_tokenize pacifier=pd.read_excel(&apos;C:/Users/lenovo/Desktop

<!-- b002334 | furniture | pages [42] -->


<!-- b002335 | prose | pages [42] -->
关注数学模型

<!-- b002336 | furniture | pages [42] -->
2

<!-- b002337 | furniture | pages [42] -->
MATHmodels

<!-- b002338 | furniture | pages [42] -->
获取更多资讯

<!-- b002339 | furniture | pages [43] -->
Team # 2010638                                                                   Page 20 of 20

<!-- b002340 | prose | pages [43] -->
/pacifier_lower.xlsx&apos;, sep=&apos;\t&apos;) b = pacifier[&apos;review_body&apos;].duplicated() test11 = pacifier.groupby(&apos;product_parent&apos;).sum() pacifier[&apos;marketplace&apos;] = pacifier[&apos;marketplace&apos;].str.lower() pacifier[&apos;product_category&apos;] = pacifier[&apos;product_category&apos;].str.lower() pacifier[&apos;vine&apos;] =pacifier[&apos;vine&apos;].str.lower() pacifier[&apos;verified_purchase&apos;] = pacifier[&apos;verified_purchase&apos;].str.lower() test2 = pacifier[&apos;review_body&apos;].tolist() text_a_count = [] text_b_count = [] for sent in test2: words = word_tokenize(sent)

<!-- b002341 | prose | pages [43] -->
text_b_count.append(words) for word in words: if word.isalpha() == False: words.remove(word) text_a_count.append(len(words)) counts1 = {} for word in words: counts1[word] = counts1.get(word,0) + 1 items = list(counts1.items()) items.sort(key=lambda x:x[1], reverse=True) for i in range(len(items)): word, count1 = items[i] print ("{0:<10}{1:>5}".format(word, count1))

<!-- b002342 | prose | pages [43] -->
from collections import Counter import pandas as pd import numpy as np c={"counts" : text_a_count, "split" : text_b_count} data=pd.DataFrame(c) w = Counter(text_a_count) print(w) w1 = set(text_a_count) print(text_a_count) w2 = w.most_common(len(w)) m = [] for i in range(305): m.append(list(w2[i])) df = pd.DataFrame(m, columns=[&apos;number&apos;, &apos;count&apos;]) color = [&apos;r&apos;,&apos;y&apos;,&apos;k&apos;,&apos;g&apos;,&apos;m&apos;] plt.scatter(df[&apos;number&apos;],df[&apos;count&apos;],c=color,marker=&apos;>&apos;) plt.legend() plt.show()

<!-- b002343 | furniture | pages [43] -->


<!-- b002344 | prose | pages [43] -->
关注数学模型

<!-- b002345 | furniture | pages [43] -->
2

<!-- b002346 | furniture | pages [43] -->
MATHmodels

<!-- b002347 | furniture | pages [43] -->
获取更多资讯
