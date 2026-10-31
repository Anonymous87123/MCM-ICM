# P-C-2020-2004647-771d613e

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2020

<!-- b000002 | prose | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | furniture | pages [1] -->
2004647

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Good Morning Sunshine:

<!-- b000009 | title | pages [1] -->
A Rating and Review Based Analysis

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
The Review and Rating System has been playing a huge role during the evolu- tion of E-commerce. Customers use it to help make the best purchase decisions, while vendors can utilize it to collect opinions on how to make improvements. Therefore, in a vendor’s perspective, it is of essential to learn to most efﬁciently extract the most valuable information out of mountains of customers’ voices.

<!-- b000012 | prose | pages [1] -->
Firstly, based on the attributes we ﬁnd useful in the provided data sets, we pro- pose the Rating and Review Based Score (RRBS) Model, which deﬁnes a product’s score—a data measure based on information reﬁned from ratings and reviews— that ﬁnely quantiﬁes and describes customers’ responses to a product. Based on the RRBS Model, we further introduce the Reputation Model, which gives a time- based quantiﬁcation of a product’s reputation over time periods. Our model eval- uation results show that a quantiﬁed reputation has a strong correlation with the corresponding product’s sales in terms of trend. This fact intuitively proves our models’ correctness.

<!-- b000013 | prose | pages [1] -->
Then, in order to predict a product’s potential success or failure in the future, we propose the the Successfulness Prediction Model, utilizing the knowledge ba- sis established from our previously proposed models. Based on the premise that a product’s success is closely connected to its sales, we are able to address the suc- cessfulness prediction task by predicting a product’s future reputation with calcu- lated reputation series, followed by comparison between the predicted values and a pre-set threshold. As a result, the successfulness of products can be effectively predicted.

<!-- b000014 | prose | pages [1] -->
Next, we evaluate star ratings’ incitement to custmoers’ speciﬁc reviews by record- ing customers’ reviews right after a series of same ratings (either high or low), and calculate the chance of them being either positive, negative or neutral. It turns out a series of high ratings do incite more positive reviews; at the other end, we cannot conﬁdently determine a series of low ratings’ incitement to negative reviews. Sub- sequently, we discover the association between rating levels and speciﬁc quality descriptors from review text by matching review contents with graded-words. The results reveal strong connection between postive words and high ratings, and simi- larly, negative words and low ratings.

<!-- b000015 | prose | pages [1] -->
Finally, to assist with Sunshine Company’s upcoming business, we propose our devised marketing strategies and some important design features for each product.

<!-- b000016 | keywords | pages [1] -->
Keywords: the RRBS Model; the Reputation Model; Correlation Analysis;

<!-- b000017 | prose | pages [1] -->
关注数学模型

<!-- b000018 | furniture | pages [1] -->
2

<!-- b000019 | furniture | pages [1] -->
MATHmodels

<!-- b000020 | furniture | pages [1] -->
获取更多资讯

<!-- b000021 | furniture | pages [2] -->
Team # 2004647

<!-- b000022 | furniture | pages [2] -->
Page 1 of 24

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
1

<!-- b000025 | heading | pages [2] -->
Introduction

<!-- b000026 | prose | pages [2] -->
2 Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2 Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 3

<!-- b000027 | prose | pages [2] -->
Modeling Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000028 | prose | pages [2] -->
2

<!-- b000029 | heading | pages [2] -->
Assumptions & Nomenclature

<!-- b000030 | prose | pages [2] -->
3

<!-- b000031 | heading | pages [2] -->
the RRBS Model

<!-- b000032 | prose | pages [2] -->
3

<!-- b000033 | prose | pages [2] -->
3

<!-- b000034 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 Model Overview 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 the Rating Vector 5

<!-- b000035 | prose | pages [2] -->
the Review Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 6 The Review-based Measure Equation . . . . . . . . . . . . . . . . . . . . . 3.3.1 8

<!-- b000036 | prose | pages [2] -->
the Sentiment Polarity Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.2

<!-- b000037 | prose | pages [2] -->
4

<!-- b000038 | heading | pages [2] -->
the Reputation Model

<!-- b000039 | prose | pages [2] -->
9

<!-- b000040 | prose | pages [2] -->
10

<!-- b000041 | prose | pages [2] -->
Time Weight Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 10

<!-- b000042 | prose | pages [2] -->
Quantiﬁcation of Reputation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 11

<!-- b000043 | prose | pages [2] -->
Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 11 Trend Similarity between Quantiﬁed Reputation and Sales . . . . . . . . . 4.3.1 11

<!-- b000044 | prose | pages [2] -->
Kendall’s Tau Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.2

<!-- b000045 | prose | pages [2] -->
5

<!-- b000046 | heading | pages [2] -->
the Successfulness Prediction Model

<!-- b000047 | prose | pages [2] -->
12

<!-- b000048 | prose | pages [2] -->
13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Gaussian Process Regression 14

<!-- b000049 | prose | pages [2] -->
Reputation Mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 15

<!-- b000050 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 Successfulness Threshold

<!-- b000051 | prose | pages [2] -->
6

<!-- b000052 | heading | pages [2] -->
Results

<!-- b000053 | prose | pages [2] -->
15

<!-- b000054 | prose | pages [2] -->
16 Evaluation of Star Rating’s Incitement . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 16

<!-- b000055 | prose | pages [2] -->
Association between Review Wording and Rating Levels . . . . . . . . . . . . . . 6.2 18

<!-- b000056 | prose | pages [2] -->
Our Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 19

<!-- b000057 | prose | pages [2] -->
Marketing Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3.1 19

<!-- b000058 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3.2 Important Design Features

<!-- b000059 | prose | pages [2] -->
7

<!-- b000060 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000061 | prose | pages [2] -->
8

<!-- b000062 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000063 | prose | pages [2] -->
19

<!-- b000064 | prose | pages [2] -->
20

<!-- b000065 | prose | pages [2] -->
20

<!-- b000066 | prose | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 20

<!-- b000067 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 Weaknesses

<!-- b000068 | prose | pages [2] -->
9

<!-- b000069 | heading | pages [2] -->
Conclusion

<!-- b000070 | heading | pages [2] -->
10 Our Letter

<!-- b000071 | heading | pages [2] -->
Appendices

<!-- b000072 | prose | pages [2] -->
21

<!-- b000073 | prose | pages [2] -->
21

<!-- b000074 | prose | pages [2] -->
22

<!-- b000075 | prose | pages [2] -->
25

<!-- b000076 | prose | pages [2] -->
关注数学模型

<!-- b000077 | furniture | pages [2] -->
2

<!-- b000078 | furniture | pages [2] -->
MATHmodels

<!-- b000079 | furniture | pages [2] -->
获取更多资讯

<!-- b000080 | furniture | pages [3] -->
Team # 2004647

<!-- b000081 | furniture | pages [3] -->
1

<!-- b000082 | heading | pages [3] -->
Introduction

<!-- b000083 | furniture | pages [3] -->
Page 2 of 24

<!-- b000084 | prose | pages [3] -->
"Amazing things will happen when you listen to the consumer."

<!-- b000085 | prose | pages [3] -->
—Jonathan Midenhall, CMO of Airbnb

<!-- b000086 | prose | pages [3] -->
E-commerce has sprouted for the last few decades all over the world, and now it has be- come one of the most prosperous and promising modern industries. During this process, the Review and Rating System has been playing a huge role all along. Not only does it help cus- tomers ﬁnd out what is best for them when making purchase decisions, but also it helps sellers realize what problems their products have and thus things can be improved. Therefore, it is signiﬁcant for companies to know how to make the most use of it and apply the knowledge to improving product designs and marketing strategies.

<!-- b000087 | prose | pages [3] -->
1.1

<!-- b000088 | heading | pages [3] -->
Problem Restatement

<!-- b000089 | prose | pages [3] -->
Sunshine Company is about to launch three new products in the marketplace, including a mi- crowave, a baby paciﬁer and a hair dryer. Data of customer-supplied reviews and ratings for microwave ovens, baby paciﬁers and hair dryers sold on Amazon.com are supplied, each of which has a time label on. Analysis of customers’ ratings and reviews of other companies’s competing products is required in order to ﬁgure out the optimal online marketing strategies and possible design features they can employ to make their products more desirable to cus- tomers.

<!-- b000090 | prose | pages [3] -->
To achieve our goals, speciﬁcally, we need to:

<!-- b000091 | prose | pages [3] -->
• Identify the most informative data measures based on reviews and ratings for Sunshine Company to track, once they launch their three new products in the online marketplace.

<!-- b000092 | prose | pages [3] -->
• Discover time-based measures and patterns that can suggest a product’s reputation’s trend of increase or decrease.

<!-- b000093 | prose | pages [3] -->
• Combine text-based measures and rating-based measures to discover measures that best indicate a product’s potential success or faliure.

<!-- b000094 | prose | pages [3] -->
• Find out whether speciﬁc star ratings incite more reviews.

<!-- b000095 | prose | pages [3] -->
• Find out whether rating levels and speciﬁc quality descriptors of text-based reviews are strongly associated.

<!-- b000096 | prose | pages [3] -->
1.2 Literature Review

<!-- b000097 | prose | pages [3] -->
Early work have proposed several methods for utilizing reviews and ratings of online prod- ucts. In 2009, Koren et al. [4] proposed Latent Factor Models (LFM) to address the rating prediction task. In 2013, McAuley et al. [5] took advantage of the abundunt information in reviews using Latent Dirichlet Allocation (LDA) to achieve topic distributions. Later in 2016, Tan et al. [8] proposed the Rating-Boosted Latent Topics (RBLT) Framework, combining tex- tual reviews with users’ sentiment orientations, and thus recommendations are made more accurate.

<!-- b000098 | prose | pages [3] -->
However, some of the valuable information in reviews is not fully utilized in the introduced works, such as varying text lengths of different reviews and the sentiment intensity of speciﬁc

<!-- b000099 | prose | pages [3] -->
关注数学模型

<!-- b000100 | furniture | pages [3] -->
2

<!-- b000101 | furniture | pages [3] -->
MATHmodels

<!-- b000102 | furniture | pages [3] -->
获取更多资讯

<!-- b000103 | furniture | pages [4] -->
Team # 2004647

<!-- b000104 | furniture | pages [4] -->
Page 3 of 24

<!-- b000105 | prose | pages [4] -->
words (e.g. "ﬁne" is less positively intense compared with "good"). Moreover, other impor- tant attributes in modern E-commerce recommendation systems, such as helpfulness ratings, reviewers’ credibility and whether or not reviewers are veriﬁed buyers, are rarely taken into account. The quantiﬁcation of reviews and ratings’ combinations are not yet proposed, and data measures based on reivews and ratings are not provided either.

<!-- b000106 | prose | pages [4] -->
1.3 Data Cleaning

<!-- b000107 | prose | pages [4] -->
Upon observation on the provided data, we notice there are some misplaced data in each data set, where some review items belong to products of wrong categories. For example, in the ﬁle hair_dryer.tsv the review item with the product_parent value #466871293 (which uniquely identiﬁes a product) belongs to a hair spray product, instead of a hair dryer. Similarly, in the ﬁle microwave.tsv the review item with the product_parent value #311592014 belongs to a fridge, instead of a microwave. We ﬁnd these mistakes almost exclusively happen to those products with single digit review records. Along with the perception that sparse data do not contribute to our modeling well, we omit all product items with single digit review records.

<!-- b000108 | prose | pages [4] -->
1.4

<!-- b000109 | heading | pages [4] -->
Modeling Framework

<!-- b000110 | prose | pages [4] -->
Our modeling framework can be illustrated as shown in Figure 1.

<!-- b000111 | caption | pages [4] -->
Figure 1: Modeling Framework

<!-- b000112 | heading | pages [4] -->
Assumptions & Nomenclature

<!-- b000113 | prose | pages [4] -->
2

<!-- b000114 | prose | pages [4] -->
To simplify our modeling, we make the following assumptions:

<!-- b000115 | prose | pages [4] -->
关注数学模型

<!-- b000116 | furniture | pages [4] -->
2

<!-- b000117 | furniture | pages [4] -->
MATHmodels

<!-- b000118 | furniture | pages [4] -->
获取更多资讯

<!-- b000119 | furniture | pages [5] -->
Team # 2004647

<!-- b000120 | furniture | pages [5] -->
Page 4 of 24

<!-- b000121 | prose | pages [5] -->
Asm. 1 Provided data do not include spam reviews, either from competitors or mischievous

<!-- b000122 | prose | pages [5] -->
customers.

<!-- b000123 | prose | pages [5] -->
Asm. 2 Contents of every review are legitimate and unbiased.

<!-- b000124 | prose | pages [5] -->
Asm. 3 The number of review records of a product equals to the sales of the same product

<!-- b000125 | prose | pages [5] -->
aggregated since it was launched, i.e., there are no missed or excluded records in any of the provided data sets.

<!-- b000126 | prose | pages [5] -->
Asm. 4 Customers’ reviews and ratings were posted the same day they purchased the prod-

<!-- b000127 | prose | pages [5] -->
ucts, i.e., the time consumption of procedures such as packaging, delivery and users’ conﬁrmation of quality is neglected.

<!-- b000128 | prose | pages [5] -->
Asm. 5 Each customer has at most one review and rating record on one type of product (either

<!-- b000129 | prose | pages [5] -->
a microwave, a paciﬁer or a hair dryer).

<!-- b000130 | prose | pages [5] -->
We have a list of the main notations we deﬁne during our modeling, as shown in Table 1.

<!-- b000131 | prose | pages [5] -->
3

<!-- b000132 | heading | pages [5] -->
the RRBS Model

<!-- b000133 | prose | pages [5] -->
In this section, we propose the RRBS Model (viz., the Rating and Review Based Score Model) to serve as a data measure, combining star ratings and textual information from reviews. When determining the quantiﬁcation process, we take into account nearly all inﬂuencing attributes from the provided data. As a result, a highly informative data measure is presented for Sun- shine Company to track, once their three new products are launched.

<!-- b000134 | caption | pages [5] -->
Table 1: Notations we use in future discussion.

<!-- b000135 | heading | pages [5] -->
Symbol

<!-- b000136 | prose | pages [5] -->
Description Product type (either Microwaves, Paciﬁers or Hair dryers), i = 1, 2, 3 i k Unique model identiﬁer of a type of products t Timestamp identiﬁer (unit: Month) n Number of rating and review records of a model within a speciﬁc month score(t)

<!-- b000137 | prose | pages [5] -->
Measure for customer responses a product model receives i,k Rating vector—an n-dimensional row vector α Review vector—an n-dimensional column vector β λ Rating weight parameter Sentiment polarity matrix—an n-by-n diagonal matrix A Review-quantifying vector—an n-dimensional column vector Φ θj Vine factor sj Sentiment intensity factor vj Validity factor hj Helpfulness-rating factor Lj Review-length factor ϵj Correction term score Time series of a model’s scores Rep(t)

<!-- b000138 | prose | pages [5] -->
Quantiﬁed reputation i,k

<!-- b000139 | prose | pages [5] -->
关注数学模型

<!-- b000140 | furniture | pages [5] -->
2

<!-- b000141 | furniture | pages [5] -->
MATHmodels

<!-- b000142 | furniture | pages [5] -->
获取更多资讯

<!-- b000143 | furniture | pages [6] -->
Team # 2004647

<!-- b000144 | prose | pages [6] -->
3.1

<!-- b000145 | heading | pages [6] -->
Model Overview

<!-- b000146 | furniture | pages [6] -->
Page 5 of 24

<!-- b000147 | prose | pages [6] -->
As part of our metric, we deﬁne score as a measure for a company’s particular product, based on the ratings and reviews it receives. It quantitatively indicates whether a product does well or badly in terms of receiving positive responses from customers. We deﬁne our metric as:

<!-- b000148 | prose | pages [6] -->
score(t)

<!-- b000149 | prose | pages [6] -->
i,k = α◦λβ

<!-- b000150 | prose | pages [6] -->
where:

<!-- b000151 | prose | pages [6] -->
(1)

<!-- b000152 | prose | pages [6] -->
• i ∈{1, 2, 3} denotes products of the ith type;

<!-- b000153 | prose | pages [6] -->
• k denotes the kth model (uniquely identiﬁed by the "product_parent" value) of the ith- type products;

<!-- b000154 | prose | pages [6] -->
• t denotes the tth month;

<!-- b000155 | prose | pages [6] -->
• α is an n-dimensional row vector whose value is determined by star ratings;

<!-- b000156 | prose | pages [6] -->
• β is an n-dimensional column vector whose value is determining by reviews and other inﬂuencing factors;

<!-- b000157 | prose | pages [6] -->
• λ is an impact factor that decides the weight of ratings in terms of impacting the score value. We initially set its value as 1.

<!-- b000158 | prose | pages [6] -->
Deﬁnition of α—the Rating Vector 3.2

<!-- b000159 | prose | pages [6] -->
The value of α is directly connected to a product’s star ratings, which vary from 1 to 5. And the value of 1 indicates "very unsatisﬁed" while the value of 5 indicating "very satisﬁed". We consider two star ratings, one with a value of 1 and the other one with a value of 5, have the same degree of intensity (i.e., one indicates "very" unsatisﬁed and the other one indicated "very" satisﬁed). Similarly, a 4-star rating is considerd having the same degree of intensity as a 2-star rating’s. And a 3-star rating represents a neutral stance, which we consider relatively less intense. Therefore, we conduct a mapping process, as shown in Table 2, so as to quantify the degree of both positivity and negativity of a star rating with a uniform measure.

<!-- b000160 | caption | pages [6] -->
Table 2: Mapping from star rating values to their corresponding mapped rating values (viz.,

<!-- b000161 | prose | pages [6] -->
degree of intensity).

<!-- b000162 | prose | pages [6] -->
Star Rating

<!-- b000163 | prose | pages [6] -->
1-star & 5-star 2-star & 4-star 3-star

<!-- b000164 | prose | pages [6] -->
Mapped Rating

<!-- b000165 | prose | pages [6] -->
3 2 1

<!-- b000166 | prose | pages [6] -->
As stated above, α is an n-dimensional row vector that is exclusively associated with star ratings. The n non-zero elements in α represent n mapped rating values of a product within a month. We can obtain:

<!-- b000167 | prose | pages [6] -->
(

<!-- b000168 | prose | pages [6] -->
α(t)

<!-- b000169 | prose | pages [6] -->
α(t)

<!-- b000170 | prose | pages [6] -->
α =

<!-- b000171 | prose | pages [6] -->
i,k,1

<!-- b000172 | prose | pages [6] -->
i,k,2

<!-- b000173 | prose | pages [6] -->
where α(t)

<!-- b000174 | prose | pages [6] -->
i,k,j ∈{1, 2, 3}.

<!-- b000175 | prose | pages [6] -->
)

<!-- b000176 | prose | pages [6] -->
α(t)

<!-- b000177 | prose | pages [6] -->
α(t)

<!-- b000178 | prose | pages [6] -->
. . . . . .

<!-- b000179 | prose | pages [6] -->
. . .

<!-- b000180 | prose | pages [6] -->
(2)

<!-- b000181 | prose | pages [6] -->
i,k,j

<!-- b000182 | prose | pages [6] -->
i,k,n

<!-- b000183 | prose | pages [6] -->
关注数学模型

<!-- b000184 | furniture | pages [6] -->
2

<!-- b000185 | furniture | pages [6] -->
MATHmodels

<!-- b000186 | furniture | pages [6] -->
获取更多资讯

<!-- b000187 | furniture | pages [7] -->
Team # 2004647

<!-- b000188 | furniture | pages [7] -->
Page 6 of 24

<!-- b000189 | prose | pages [7] -->
Deﬁnition of β—the Review Vector 3.3

<!-- b000190 | prose | pages [7] -->
β is an n-dimensional column vector whose value is strongly associated with reviews and some other inﬂuencing factors. It comprehensively takes into account of the sentiment inten- sity of review text, varying lengths of different reviews, helpfulness ratings, the authority of reviewers (i.e., whether or not he/she is an Amazon Vine Reviewer 1) and whether or not the reviewers are veriﬁed buyers. Therefore, it is made possible to fully exploit the information within the provided data and effectively integrate textual reviews and other non-numerical inﬂuencing factors into our data measure.

<!-- b000191 | prose | pages [7] -->
We deﬁne it as:

<!-- b000192 | prose | pages [7] -->
(

<!-- b000193 | prose | pages [7] -->
β(t)

<!-- b000194 | prose | pages [7] -->
β(t)

<!-- b000195 | prose | pages [7] -->
β = AΦ =

<!-- b000196 | prose | pages [7] -->
i,k,1

<!-- b000197 | prose | pages [7] -->
i,k,2

<!-- b000198 | prose | pages [7] -->
where:

<!-- b000199 | prose | pages [7] -->
)

<!-- b000200 | prose | pages [7] -->
β(t)

<!-- b000201 | prose | pages [7] -->
β(t)

<!-- b000202 | prose | pages [7] -->
. . .

<!-- b000203 | prose | pages [7] -->
. . .

<!-- b000204 | prose | pages [7] -->
(3)

<!-- b000205 | prose | pages [7] -->
i,k,j

<!-- b000206 | prose | pages [7] -->
i,k,n

<!-- b000207 | prose | pages [7] -->
• A is an n-by-n diagonal matrix used to describe the sentiment polarity of reviews;

<!-- b000208 | prose | pages [7] -->
• Φ is an n-dimensional column vector used to quantify the semantic information and other inﬂuencing attributes of reviews.

<!-- b000209 | prose | pages [7] -->
Deﬁnition of Φ—the Review-quantifying Vector

<!-- b000210 | prose | pages [7] -->
To quantify the semantic information and other inﬂuencing attributes of reviews, we deﬁne Φ as an n-dimensional column vector, as is shown in Equation (4):

<!-- b000211 | prose | pages [7] -->
(

<!-- b000212 | prose | pages [7] -->
ϕ(t)

<!-- b000213 | prose | pages [7] -->
ϕ(t)

<!-- b000214 | prose | pages [7] -->
Φ =

<!-- b000215 | prose | pages [7] -->
. . .

<!-- b000216 | prose | pages [7] -->
i,k,1

<!-- b000217 | prose | pages [7] -->
i,k,2

<!-- b000218 | prose | pages [7] -->
where ϕ(t)

<!-- b000219 | prose | pages [7] -->
)T

<!-- b000220 | prose | pages [7] -->
ϕ(t)

<!-- b000221 | prose | pages [7] -->
ϕ(t) . . .

<!-- b000222 | prose | pages [7] -->
(4)

<!-- b000223 | prose | pages [7] -->
i,k,j

<!-- b000224 | prose | pages [7] -->
i,k,n

<!-- b000225 | prose | pages [7] -->
i,k,j is the measure for semantic information, along with other inﬂuencing attributes, of a textual review, which is from the jth order of the kth model of the ith-type products.

<!-- b000226 | prose | pages [7] -->
We deﬁne this measure as:

<!-- b000227 | prose | pages [7] -->
ϕ(t)

<!-- b000228 | prose | pages [7] -->
i,k,j = θj · s

<!-- b000229 | prose | pages [7] -->
Deﬁnition of θj—the Vine Factor

<!-- b000230 | prose | pages [7] -->
vj j · hj · Lj (5)

<!-- b000231 | prose | pages [7] -->
According to Amazon.com [1], the most trusted reviewers identiﬁed by Amazon.com are invited to Amazon’s Vine Program, where they can post opinions about new and pre-release items to help their fellow customers make informed purchase decisions.

<!-- b000232 | prose | pages [7] -->
While Vine reviewers make independent opinions on offered products, the vendor can- not inﬂuence, modify or edit the reviews. Therefore, we have reason to believe that a review posted by Vine reviewers is more professional and trustworthy than regular reviews. Accord- ingly, we make our measure value contents of a review more when it is a Vine review, by deﬁning θj as:

<!-- b000233 | prose | pages [7] -->
{

<!-- b000234 | prose | pages [7] -->
2, if the review is made by a Vine reviewer

<!-- b000235 | prose | pages [7] -->
θj =

<!-- b000236 | prose | pages [7] -->
1, otherwise (6)

<!-- b000237 | prose | pages [7] -->
1An Amazon Vine Reviewer is an member or Amazon’s Vine Program, who is invited to receive products for free in exchange for impartial reviews.

<!-- b000238 | prose | pages [7] -->
关注数学模型

<!-- b000239 | furniture | pages [7] -->
2

<!-- b000240 | furniture | pages [7] -->
MATHmodels

<!-- b000241 | furniture | pages [7] -->
获取更多资讯

<!-- b000242 | furniture | pages [8] -->
Team # 2004647

<!-- b000243 | furniture | pages [8] -->
Page 7 of 24

<!-- b000244 | prose | pages [8] -->
Deﬁnition of sj—the Sentiment Intensity Factor

<!-- b000245 | prose | pages [8] -->
Most of the time, when people post reviews about products they have purchased, they tend to include speciﬁc words that express some explicit sentiments and attitudes. It is also noticing that the sentiment intensities of reviewers’ chosen words vary. For example, "good" expresses a higher intensity of positiveness than "ﬁne" does. That is to say, we are able to quantify different sentiment intensities of different words, and thus the message a review is trying to express is made gradable when measuring semantic information.

<!-- b000246 | prose | pages [8] -->
With this mindset, we attempt to ﬁnd an existing data set that contains a decent amount of common adjectives, (most importantly) each one of which has a grade that indicates its sentiment intensity. Fortunately—thanks to the great open-source community—we are able to acquire a Python library called Aﬁnn [6] that consists of 2,477 graded-words, which fulﬁlls our exact requirements. We then use this word set to match contents of all the reviews in the provided data, ﬁltering out words that do not appear in any of the reviews (which we do not need).

<!-- b000247 | prose | pages [8] -->
As a result, we obtain a graded-word table (part of which is shown in Table 3) that cate- gorizes both positive and negative words into 3 groups of different grades (with 3 being the highest and 1 being the lowest).

<!-- b000248 | caption | pages [8] -->
Table 3: A fraction of the graded-word table acquired by matching the Aﬁnn word set with

<!-- b000249 | prose | pages [8] -->
contents of all reviews. Some of the most frequently-appeared graded-words are listed in this table. Note: We modify a few words’ grades with our own understanding of their sentiment intensities.

<!-- b000250 | prose | pages [8] -->
Grade Positive Negative

<!-- b000251 | prose | pages [8] -->
outstanding, thrilled, awesome, wonderful, 3 catastrophic, horrible, dead, ridiculous, fantastic, fabulous, brilliant, terriﬁc awful, crappy, obnoxious, desperate

<!-- b000252 | prose | pages [8] -->
good, cute, powerful, comfortable, 2 clean, useful, satisﬁed, helpful

<!-- b000253 | prose | pages [8] -->
fair, ﬁne, easy, cool, 1 clear, safe, acceptible, capable

<!-- b000254 | prose | pages [8] -->
bad, disappointed, wrong, useless, negative, poor, unhappy, annoying

<!-- b000255 | prose | pages [8] -->
strange, hard, difﬁcult, noisy, limited, silly, unsure, false

<!-- b000256 | prose | pages [8] -->
Hence, we can deﬁne sj as the sentiment intensity of the textual review contents of the jth order (of the kth model of the ith-type products). Its value is deﬁned as:

<!-- b000257 | prose | pages [8] -->
{

<!-- b000258 | prose | pages [8] -->
if matched words have a maximum grade of η η

<!-- b000259 | prose | pages [8] -->
sj =

<!-- b000260 | prose | pages [8] -->
0, otherwise

<!-- b000261 | prose | pages [8] -->
Deﬁnition of vj—the Validity Factor

<!-- b000262 | prose | pages [8] -->
(7)

<!-- b000263 | prose | pages [8] -->
Intuitively, if a review is not posted by a veriﬁed buyer, the validity of it is somewhat du- bious. Therefore, considering the potential inauthenticity of reviews from unveriﬁed buyers, we reduce the weights of such reviews in our measure. We deﬁne vj to represent a review’s validity, when it is low, the corresponding review has a less inﬂuence to our measure of the product’s score.

<!-- b000264 | prose | pages [8] -->
{

<!-- b000265 | prose | pages [8] -->
1, if the reviewer is a veriﬁed buyer

<!-- b000266 | prose | pages [8] -->
vj =

<!-- b000267 | prose | pages [8] -->
0.1, otherwise (8)

<!-- b000268 | prose | pages [8] -->
关注数学模型

<!-- b000269 | furniture | pages [8] -->
2

<!-- b000270 | furniture | pages [8] -->
MATHmodels

<!-- b000271 | furniture | pages [8] -->
获取更多资讯

<!-- b000272 | furniture | pages [9] -->
Team # 2004647

<!-- b000273 | furniture | pages [9] -->
Page 8 of 24

<!-- b000274 | prose | pages [9] -->
Deﬁnition of hj—the Helpfulness-rating Factor

<!-- b000275 | prose | pages [9] -->
Undoubtedly, the helpfulness ratings of a review as an inﬂuence factor to our measure cannot be left out. Not only does it illustrate a review’s trustworthiness and overall quality, but also it exposes a review’s potential junk nature (being misleading or misconceived). This makes it easier to decide on a review should have whether more or less weights in our measure.

<!-- b000276 | prose | pages [9] -->
Therefore, we deﬁne hj as the helpfulness score in our measure, as shown in Equation (9). Its value should be 1 when nobody has yet voted its helpful, making it have the original weight in our measured in terms of helpfulness. If the "helpful" votes to total votes ratio is larger than 0.5, we consider this review a helpful review, thus should have a weight higher than 1; on the other hand, it is not helpful if the ratio is lower than 0.5 and should have a weight less than 1.

<!-- b000277 | prose | pages [9] -->


<!-- b000278 | prose | pages [9] -->
helpful_votesj

<!-- b000279 | prose | pages [9] -->


<!-- b000280 | prose | pages [9] -->
−0.5,

<!-- b000281 | prose | pages [9] -->


<!-- b000282 | prose | pages [9] -->
e

<!-- b000283 | prose | pages [9] -->
total_votesj

<!-- b000284 | prose | pages [9] -->


<!-- b000285 | prose | pages [9] -->
hj =

<!-- b000286 | prose | pages [9] -->
  

<!-- b000287 | prose | pages [9] -->
1,

<!-- b000288 | prose | pages [9] -->
if total_votesj > 0

<!-- b000289 | prose | pages [9] -->
(9)

<!-- b000290 | prose | pages [9] -->
otherwise

<!-- b000291 | prose | pages [9] -->
where helpful_votesj is the number of "helpful" votes and total_votesj is the number of total votes on a review.

<!-- b000292 | prose | pages [9] -->
Deﬁnition of Lj—the Review-length Factor

<!-- b000293 | prose | pages [9] -->
Chua et al.

<!-- b000294 | prose | pages [9] -->
[3] provided insight that a review’s helpfulness is positively related to its depth/length. Empirically, we know if a review is long to some degree, it is reasonable to assume it has more description on its target and the accuracy is more likely to be guaranteed.

<!-- b000295 | prose | pages [9] -->
Therefore, we can deﬁne Lj as a measure of a review’s helpfulness solely contributed by the review’s length. The more words a review contains, the more valuable we consider the review is. Yet it should be noted that the growth of Lj by review length should be non-linear and the growth rate should reduce as review length increases, otherwise it can affect our measure for products’ score too much. Hence, we deﬁne Lj as:

<!-- b000296 | prose | pages [9] -->
Lj = 1

<!-- b000297 | prose | pages [9] -->
2 log10 lenj (10)

<!-- b000298 | prose | pages [9] -->
where lenj is the literal number of words in the review of the jth order (of the kth model of the ith-type products).

<!-- b000299 | prose | pages [9] -->
3.3.1 The Review-based Measure Equation

<!-- b000300 | prose | pages [9] -->
By substituting Equation (6), (7), (8), (9) and (10) into Equation (5), we obtain:

<!-- b000301 | prose | pages [9] -->
helpful_votesj

<!-- b000302 | prose | pages [9] -->
vj

<!-- b000303 | prose | pages [9] -->
ϕ(t)

<!-- b000304 | prose | pages [9] -->
i,k,j = θj · s

<!-- b000305 | prose | pages [9] -->
j · e

<!-- b000306 | prose | pages [9] -->
−0.5 · 1

<!-- b000307 | prose | pages [9] -->
2 log10 lenj

<!-- b000308 | prose | pages [9] -->
total_votesj

<!-- b000309 | prose | pages [9] -->
(11)

<!-- b000310 | prose | pages [9] -->
This is the equation we deﬁne to measure semantic information and other inﬂuencing at- tributes of a textual review, taking into account of reviewers’ authority, reviews’ validity, re- views’ sentiment intensities, reviews’ helpfulness ratings and reviews’ textual lengths.

<!-- b000311 | prose | pages [9] -->
Note that the value of sj can be 0, for:

<!-- b000312 | prose | pages [9] -->
• The wording of a review might be quite neutral and a clear sentiment (eith positive or negative) can not be inferred;

<!-- b000313 | prose | pages [9] -->
关注数学模型

<!-- b000314 | furniture | pages [9] -->
2

<!-- b000315 | furniture | pages [9] -->
MATHmodels

<!-- b000316 | furniture | pages [9] -->
获取更多资讯

<!-- b000317 | furniture | pages [10] -->
Team # 2004647

<!-- b000318 | furniture | pages [10] -->
Page 9 of 24

<!-- b000319 | prose | pages [10] -->
• Some speciﬁc words within a review might suggest a sentiment and has some degree of intensity, but are not included in the graded-word set from Aﬁnn, making the evaluation of such reviews’ sentiment intensities infeasible.

<!-- b000320 | prose | pages [10] -->
From equation (11) we know a review with a sj value of 0 also has the value of ϕ(t)

<!-- b000321 | prose | pages [10] -->
i,k,j being 0, meaning the measure treats such a review as a "entirely-junk" review; this makes the multipli- cation of this review by its corresponding star rating result in a value of 0, meaning the rating loses its effect indirectly. This is not appropriate and we want to preserve our data measure ’s effect in this scenario. Therefore, we address this problem by introducing an correction term ϵj; its value is deﬁned as:

<!-- b000322 | prose | pages [10] -->
{

<!-- b000323 | prose | pages [10] -->
1,

<!-- b000324 | prose | pages [10] -->
ϵj =

<!-- b000325 | prose | pages [10] -->
0, if sj = 0 (12) otherwise

<!-- b000326 | prose | pages [10] -->
By adding this correction term to our measure (Equation (11)), we have:

<!-- b000327 | prose | pages [10] -->
helpful_votesj

<!-- b000328 | prose | pages [10] -->
vj

<!-- b000329 | prose | pages [10] -->
ϕ(t)

<!-- b000330 | prose | pages [10] -->
i,k,j = θj · s

<!-- b000331 | prose | pages [10] -->
j · e

<!-- b000332 | prose | pages [10] -->
−0.5 · 1

<!-- b000333 | prose | pages [10] -->
2 log10 lenj + ϵj

<!-- b000334 | prose | pages [10] -->
total_votesj

<!-- b000335 | prose | pages [10] -->
Now the value of ϕ(t)

<!-- b000336 | prose | pages [10] -->
(13)

<!-- b000337 | prose | pages [10] -->
i,k,j will be 1 if the value of sj is 0, making the corresponding review have an initial weight; thus, from Equation (1) we know that the score which the review and its corresponding star rating collectively decide will solely depend on the star rating in this case.

<!-- b000338 | prose | pages [10] -->
By integrating nearly all useful information of reviews in a reasonable way, we can effec- tively measure reviews’ value , and thus can ﬁlter out poorly-written reviews with little value for paying attention to and retain valuable information from reviews which are worth listening to.

<!-- b000339 | prose | pages [10] -->
3.3.2 the Sentiment Polarity Matrix

<!-- b000340 | prose | pages [10] -->
A is an n-by-n diagonal matrix and is used to describe the sentiment polarity of reviews. We assign the value +1 to an element of A, if and only if the corresponding review (of the element) is measured as positive. Similarly, we assign the value −1 to the element if the corresponding review is measured as negative, as shown in Equation (14):

<!-- b000341 | prose | pages [10] -->
{

<!-- b000342 | prose | pages [10] -->
+1, if the corresponding review suggests a positive sentiment

<!-- b000343 | prose | pages [10] -->
a(t)

<!-- b000344 | prose | pages [10] -->
i,k,j =

<!-- b000345 | prose | pages [10] -->
−1, (14) if the corresponding review suggests a negative sentiment

<!-- b000346 | prose | pages [10] -->
As for how to decide a review is whether positive or negative, we know that the Aﬁnn word set we use when matching reviews is comprised of graded-words with signs. For example, in the word set, the word "perfect" has a grade of +3 and the word "imperfect" has a grade of −2. Therefore, after a matching process of sentiment words and review contents, we extract the sign of the result and examine it. If it is a positive sign, we think of the review as positive; similarly, if is a negative sign, we consider the review negative.

<!-- b000347 | prose | pages [10] -->
For A, we have:

<!-- b000348 | prose | pages [10] -->
i,k,2, . . . , a(t)

<!-- b000349 | prose | pages [10] -->
A = diag(a(t)

<!-- b000350 | prose | pages [10] -->
i,k,1, a(t)

<!-- b000351 | prose | pages [10] -->
i,k,j, . . . , a(t)

<!-- b000352 | prose | pages [10] -->
i,k,n) (15)

<!-- b000353 | prose | pages [10] -->
关注数学模型

<!-- b000354 | furniture | pages [10] -->
2

<!-- b000355 | furniture | pages [10] -->
MATHmodels

<!-- b000356 | furniture | pages [10] -->
获取更多资讯

<!-- b000357 | furniture | pages [11] -->
Team # 2004647

<!-- b000358 | furniture | pages [11] -->
Page 10 of 24

<!-- b000359 | prose | pages [11] -->
We also take into account of the possibility that some reviews may contain words like "not" that invert the meaning of their next words. To assess the inﬂuence of such cases, we conduct statistics analysis. If the frequency of appearance of "negative-adjective" combinations (e.g., "not good") is low enough to be neglected, then we can be convinced this possibility has little effect on our results, if not addressed. As shown in Table 4, the percentage of such words’ appearance is 1166/101435 = 1.15%; thus, it is reasonable to ignore them.

<!-- b000360 | prose | pages [11] -->
4

<!-- b000361 | heading | pages [11] -->
the Reputation Model

<!-- b000362 | prose | pages [11] -->
In Section 3.1, we deﬁne score to measure the positiveness/negativeness of customers’s overall responses for a product, based on the ratings and reviews it receives. On the grounds of this, in this section, we further introduce a time-based indicator—reputation—which intuitively de- scribes a product’s accumulated reputation over time periods. Accordingly, we build our Rep- utation Model to quantify a product’s time-based reputation, based on the measure provided by the RRBS Model (Section 3).

<!-- b000363 | prose | pages [11] -->
4.1 Time Weight Sequence

<!-- b000364 | prose | pages [11] -->
Intuitively, a reputation at a certain time is somewhat dependent to its previous reputation, instead of abruptly changes regardless of its states in the past or future. Generally, a prod- uct’s reputation at a certain time is closely connected to its reputations throughout its lifespan. With this mindset, we deﬁne the concept of Time Weight Sequence to describe the inﬂuences of previous reputations in a reputation at time t, denoted by a t-dimensional row vector γ:

<!-- b000365 | prose | pages [11] -->
(

<!-- b000366 | prose | pages [11] -->
γ1 γ2

<!-- b000367 | prose | pages [11] -->
γ =

<!-- b000368 | prose | pages [11] -->
)

<!-- b000369 | prose | pages [11] -->
. . . . . .

<!-- b000370 | prose | pages [11] -->
γm . . .

<!-- b000371 | prose | pages [11] -->
γt

<!-- b000372 | prose | pages [11] -->
(16)

<!-- b000373 | prose | pages [11] -->
where γm is the inﬂuence weight of a score in the mth month (with the 1st month being the ﬁrst month when a product is launched). We consider a reputation of a product in the mth month is more prone to be affected by the previous reputation in the (m −1)th month than the one in the (m −2)th month. We assume the growth of γm by time is exponential and perform normalization on this basis; thus, we obtain:

<!-- b000374 | prose | pages [11] -->
γj = aj

<!-- b000375 | prose | pages [11] -->
at ,

<!-- b000376 | prose | pages [11] -->
where a is a constant whose value is set as 1.1.

<!-- b000377 | prose | pages [11] -->
a > 1 (17)

<!-- b000378 | caption | pages [11] -->
Table 4: Appearance counts of common adjectives (like "good") and "neg-adj" combinations

<!-- b000379 | prose | pages [11] -->
(like "not good") within all of the reviews. Adjectives are distinguished by an open-source Python word-processing library [2] and appearance is counted using Excel.

<!-- b000380 | prose | pages [11] -->
Count Common Adjective "Neg-adj" Combo.

<!-- b000381 | prose | pages [11] -->
Count

<!-- b000382 | prose | pages [11] -->
4466 great not sure 148 3055 good not heavy 40 2963 little ...

<!-- b000383 | prose | pages [11] -->
not worth 34 ... ...

<!-- b000384 | prose | pages [11] -->
...

<!-- b000385 | prose | pages [11] -->
...

<!-- b000386 | prose | pages [11] -->
101435 Total 1166

<!-- b000387 | prose | pages [11] -->
关注数学模型

<!-- b000388 | furniture | pages [11] -->
2

<!-- b000389 | furniture | pages [11] -->
MATHmodels

<!-- b000390 | furniture | pages [11] -->
获取更多资讯

<!-- b000391 | furniture | pages [12] -->
Team # 2004647

<!-- b000392 | prose | pages [12] -->
4.2 Quantiﬁcation of Reputation

<!-- b000393 | furniture | pages [12] -->
Page 11 of 24

<!-- b000394 | prose | pages [12] -->
Firstly, based on Equation (1) we deﬁne a t-dimensional column vector denoted by score, to represent a product’s t months of scores:

<!-- b000395 | prose | pages [12] -->
(

<!-- b000396 | prose | pages [12] -->
score(1)

<!-- b000397 | prose | pages [12] -->
score(2)

<!-- b000398 | prose | pages [12] -->
score =

<!-- b000399 | prose | pages [12] -->
i,k

<!-- b000400 | prose | pages [12] -->
i,k

<!-- b000401 | prose | pages [12] -->
where score(m)

<!-- b000402 | prose | pages [12] -->
)T

<!-- b000403 | prose | pages [12] -->
score(m)

<!-- b000404 | prose | pages [12] -->
score(t)

<!-- b000405 | prose | pages [12] -->
. . .

<!-- b000406 | prose | pages [12] -->
. . .

<!-- b000407 | prose | pages [12] -->
(18)

<!-- b000408 | prose | pages [12] -->
i,k

<!-- b000409 | prose | pages [12] -->
i,k

<!-- b000410 | prose | pages [12] -->
i,k is the score of the kth model of ith-type products in the mth month.

<!-- b000411 | prose | pages [12] -->
We then deﬁne the quantiﬁcation of reputation as Rep(t)

<!-- b000412 | prose | pages [12] -->
Rep(t)

<!-- b000413 | prose | pages [12] -->
i,k, as shown in Equation (19)

<!-- b000414 | prose | pages [12] -->
i,k = γ · score (19)

<!-- b000415 | prose | pages [12] -->
where i denotes the type of a product model; k denotes the kth model of ith-type products; t denotes the tth month (since the product is launched).

<!-- b000416 | prose | pages [12] -->
From Equation (17) we know the Time Weight Sequence γ follows a monotonically increas- ing exponential pattern, which means a product’s score from a recent month impacts more on the new reputation than a score from a distant month does. Therefore, with the quantiﬁcation of products’ reputations, we should be able to address the task of observing and predicting products’ reputational increase or decrease in the online marketplace.

<!-- b000417 | prose | pages [12] -->
4.3

<!-- b000418 | heading | pages [12] -->
Model Evaluation

<!-- b000419 | prose | pages [12] -->
Based on empirical knowledge, a product with a good reputation (viz., the opinion customers have about how good it is) can induce more sales than one with a poorer reputation does. On the grounds of this, it is rational to say that a growth in a product’s reputation can stimulate a porportional amount of sales increase, and on the other hand, when a product’s reputation suffers, a decrease in sales is likely to happen.

<!-- b000420 | prose | pages [12] -->
With that being said, we can address the task of evaluating our models and measures’ correctness—which is tricky because the term reputation is quite abstract and there are no statistics of it for us to refer to—by comparing the trend of our quantiﬁed reputation to the trend of a product’s actual sales (derived from the rating and review records). Hence, after we quantify a product’s reputation with our measure, we can perform a comparison between the quantiﬁed reputation’s trend and the actual sales trend; thus the correctness of our models and measures are evaluated.

<!-- b000421 | prose | pages [12] -->
Trend Similarity between Quantiﬁed Reputation and Sales 4.3.1

<!-- b000422 | prose | pages [12] -->
We select 3 best-selling models from each of the 3 types of products to present and compare the trend of their reputation and their sales. Then, for each product model, we obtain a time series2 of quantiﬁed reputations and a time series of sales, and respectively present them in a scatter plot with points roughly connected to reveal trends. The result for each product model is shown in Figure 2. Next, for more comprehensiveness, we also select 1 rather poor-selling model from each type of products and perform the same operation, with results shown in

<!-- b000423 | caption | pages [12] -->
Figure 3.

<!-- b000424 | prose | pages [12] -->
With results in both ﬁgures, we can see trends of our quantiﬁed reputation and actual sales

<!-- b000425 | prose | pages [12] -->
2A time series is a series of data points indexed (or listed or graphed) in time order.

<!-- b000426 | prose | pages [12] -->
关注数学模型

<!-- b000427 | furniture | pages [12] -->
2

<!-- b000428 | furniture | pages [12] -->
MATHmodels

<!-- b000429 | furniture | pages [12] -->
获取更多资讯

<!-- b000430 | furniture | pages [13] -->
Team # 2004647

<!-- b000431 | furniture | pages [13] -->
Page 12 of 24

<!-- b000432 | prose | pages [13] -->
are very similar and might be highly correlated. To further prove this idea, we then conduct a correlation analysis.

<!-- b000433 | caption | pages [13] -->
Figure 2: Visualization trends of reputation and sales of 3 best-selling models from each of the

<!-- b000434 | prose | pages [13] -->
3 types of products.

<!-- b000435 | caption | pages [13] -->
Figure 3: Visualization trends of reputation and sales of 1 rather poor-selling model from each

<!-- b000436 | prose | pages [13] -->
of the 3 types of products.

<!-- b000437 | prose | pages [13] -->
4.3.2 Kendall’s Tau Method

<!-- b000438 | prose | pages [13] -->
To evaluate the trend similarity between reputation and sales, we adopt Kendall’s Tau Method [9] to study the correlation between trends of reputation and trends of sales.

<!-- b000439 | prose | pages [13] -->
The procedure of Kendall’s Tau Method is as follows: suppose {x1, · · · , xi, · · · , xT} and { y1, · · · , yi, · · · , yT} are two randomly generated time series where i = 1, 2, · · · , T, we per- form sorting operation on both series respectively by the values of xi and yi. Then, we ob- tain two sorted time series—say, {x(1), x(2), · · · , x(T)} (termed the order statistics of the time series {x1, · · · , xi, · · · , xT}) and {y(1), y(2), · · · , y(T)} (termed the order statistics of the time series {y1, · · · , yi, · · · , yT}) —where x(1) ≤x(2) ≤· · · ≤x(T) and y(1) ≤y(2) ≤· · · ≤y(T).

<!-- b000440 | prose | pages [13] -->
Take xj from the sorted series {x(1), x(2), · · · , x(T)} and suppose it is at its kth position, the number of 1 ≤k ≤T is termed the rank of xj and is denoted by pj. Similarly, from the sorted series {y(1), y(2), · · · , y(T)} we acquire the rank of yj denoted by qj. Let (xi, yi) and (xj, yj) with

<!-- b000441 | prose | pages [13] -->
关注数学模型

<!-- b000442 | furniture | pages [13] -->
2

<!-- b000443 | furniture | pages [13] -->
MATHmodels

<!-- b000444 | furniture | pages [13] -->
获取更多资讯

<!-- b000445 | furniture | pages [14] -->
Team # 2004647

<!-- b000446 | furniture | pages [14] -->
Page 13 of 24

<!-- b000447 | prose | pages [14] -->
i = 1, · · · , T and j = i + 1, · · · , T be two data-pairs from the original time series. If (pj − pi)(qj −qi) > 0, we say the two data-pairs are concordant; otherwise, we say they are discordant. Let P denote the number of concordant pairs and Q denote the number of discordant pairs, it follows that P + Q = N(N −1)/2, and Kendall’s tau can be deﬁned as:

<!-- b000448 | prose | pages [14] -->
τK(X, Y ) ≜P −Q

<!-- b000449 | prose | pages [14] -->
P −Q P + Q = (20) N(N −1)/2

<!-- b000450 | prose | pages [14] -->
Hence, we know when two time series {x1, · · · , xi, · · · , xT} and { y1, · · · , yi, · · · , yT} have the exact same trend, then we have τK(X, Y ) →1; when the two series have the exact opposite trend, we have τK(X, Y ) →−1; and when the two series are not correlated at all, we have τK(X, Y ) →0. That is to say, |τK(X, Y )| ≈1 suggests trends of the two series are highly correlated while |τK(X, Y )| ≈0 suggests they are not correlated at all.

<!-- b000451 | prose | pages [14] -->
By adopting this method, with time series {x1, · · · , xi, · · · , xT} being the quantiﬁed reputa- tions and { y1, · · · , yi, · · · , yT} being the sales, we obtain results (shown in Figure 4) that suggest a high correlation between trends of reputation and sales: most of the calculated correlations are over 0.6, which is considered storng. The correlations calculated in the paciﬁer group are close to 0.8, which also indicates that a paciﬁer’s reputation is most correlated with its sales.

<!-- b000452 | caption | pages [14] -->
Figure 4: Calculated correlations of different models sperated into 3 groups by product types.

<!-- b000453 | prose | pages [14] -->
Each group contains correlations of 5 models, with top1 meaning the best-selling model in this group, top2 meaning the second-best-selling one and the ramaining 3 denoted the same way.

<!-- b000454 | prose | pages [14] -->
5

<!-- b000455 | heading | pages [14] -->
the Successfulness Prediction Model

<!-- b000456 | prose | pages [14] -->
Based on economic knowledge, a product’s success can be well quantiﬁed by its number of sales/orders over time. The more sales a product reaches, the greater the superiority it has in the marketplace, for it can gain ﬁne proﬁts to make room for possible enhancement (which costs money).

<!-- b000457 | prose | pages [14] -->
In Section 4.3.1 we learn that a product’s sales trend is highly correlated with its reputation trend. Combining the knowledge we have, if a product’s reputation increases, then its sales are likely to increase within a similar degree, and thus we can suppose that this product is likely to succeed; on the other hand, a product’s reputational decrease might suggest its potential failure. Besides, we notice that the sales we have are of some degree of votality; thus, if we

<!-- b000458 | prose | pages [14] -->
关注数学模型

<!-- b000459 | furniture | pages [14] -->
2

<!-- b000460 | furniture | pages [14] -->
MATHmodels

<!-- b000461 | furniture | pages [14] -->
获取更多资讯

<!-- b000462 | furniture | pages [15] -->
Team # 2004647

<!-- b000463 | furniture | pages [15] -->
Page 14 of 24

<!-- b000464 | prose | pages [15] -->
regress a product’s successfulness against its sales to predict the product’s future success or failure, the predictions can be highly error-prone.

<!-- b000465 | prose | pages [15] -->
The RRBS Model we build in Section 3 effectively combines star-rating levels and informa- tion within text-based reviews, while the Reputation Model introduced in Section 4 provides a time-based measure that well quantiﬁes a product’s reputation over time. Considering our previously presented models’ strong capability and the fact the reputation changes much less abruptly compared with sales, we realize that by substituting our reputation measure for ac- tual sales when predicting a product’s successfulness and by predicting the product’s future reputation based on calculated reputation series, might turn out to be a good approach.

<!-- b000466 | prose | pages [15] -->
5.1 Gaussian Process Regression

<!-- b000467 | prose | pages [15] -->
Gaussian Processes (GP) are a generic supervised learning method designed to solve regres- sion and probabilistic classiﬁcation problems, while inference of continuous values with a Gaussian process prior is known as Gaussian Process Regression (GPR) [7]. We recognize GPR has several attributes we ﬁnd handy, e.g., it works well on small datasets and has the ability to provide uncertainty measurements on the predictions.

<!-- b000468 | prose | pages [15] -->
Therefore, we adopt GPR to ﬁt a product’s reputation series, hence predicting the product’s reputation in the future (later than the latest labeled-date in the provided data), and ﬁnally making it possible to predict the product’s future successfulness.

<!-- b000469 | prose | pages [15] -->
We ﬁrst try estimating the reputation of the best-selling paciﬁer model (with the "par- Its rating and review records are within a date range of ent_product" value #246038397). Jan.2010 to Aug. 2015. We ﬁrst obtain a time series of its reputations calculated with our Reputation Model, then we ﬁt the time series (leaving out values of July and August, 2015) by adopting GPR, and make predictions on its reputation in July and August, 2015, with a conﬁ- dence interval of 95%. The result shows that such short-term predictions have a high reliability, as seen in Figure 5.

<!-- b000470 | prose | pages [15] -->
(a) (b)

<!-- b000471 | caption | pages [15] -->
Figure 5: Subﬁgure (a) is the result of conducted short-term predictions (predicting reputations

<!-- b000472 | prose | pages [15] -->
in a few months); subﬁgure (b) is the result of long-term predictions (predicting reputations in a few years).

<!-- b000473 | prose | pages [15] -->
Upon observations we realize the possibility of overﬁtting, so we obtain a time series (with a trimmed date range of Jan. 2010 to Dec. 2014) of the same model’s reputation, and predict its reputation after Jan. 2014. As shown in Figure 5(b), some real data points fall beyond the

<!-- b000474 | prose | pages [15] -->
关注数学模型

<!-- b000475 | furniture | pages [15] -->
2

<!-- b000476 | furniture | pages [15] -->
MATHmodels

<!-- b000477 | furniture | pages [15] -->
获取更多资讯

<!-- b000478 | furniture | pages [16] -->
Team # 2004647

<!-- b000479 | furniture | pages [16] -->
Page 15 of 24

<!-- b000480 | prose | pages [16] -->
conﬁdence interval, indicating errors of our predictions. After deep analysis, we come up with the conclusion that the errors occur because the calculation of reputations is with a weight sequence of time (Section 4.1), making distant reputations have less effect. Therefore, it might be somewhat inaccurate when predicting reputations in the distant future; and thus all existing records should be used when performing predictions.

<!-- b000481 | prose | pages [16] -->
5.2 Reputation Mapping

<!-- b000482 | prose | pages [16] -->
Considering predicted reputations after Aug. 2015 may vary a lot in values, we might not effec- tively ﬁnd an interval of convergence, which makes it hard to evaluate a product’s successful- ness. Therefore, we seek to ﬁnd a mapping approach to map our non-converging reputation predictions so that mapped reputations ﬂuctuate within an distinct interval of convergence, while the reputation values before and after mapping should indicate the same trend. We adopt the following function as our mapping approach:

<!-- b000483 | prose | pages [16] -->
pi,k(t) =

<!-- b000484 | prose | pages [16] -->
ˆ Rep(t) where −

<!-- b000485 | prose | pages [16] -->
1

<!-- b000486 | prose | pages [16] -->
(21)

<!-- b000487 | prose | pages [16] -->
ˆ Rep(t) 1 + e−

<!-- b000488 | prose | pages [16] -->
i,k

<!-- b000489 | prose | pages [16] -->
i,k is the predicted reputation in the tth month. It can be seen that p(t) →1 if

<!-- b000490 | prose | pages [16] -->
ˆ

<!-- b000491 | prose | pages [16] -->
ˆ

<!-- b000492 | prose | pages [16] -->
Rep(t)

<!-- b000493 | prose | pages [16] -->
Rep(t)

<!-- b000494 | prose | pages [16] -->
−

<!-- b000495 | prose | pages [16] -->
i,k →+∞; while p(t) →0 if −

<!-- b000496 | prose | pages [16] -->
i,k →−∞. Therefore, our mapped reputation p(t) has an interval of convergence, while also having the same trend as the original’s.

<!-- b000497 | prose | pages [16] -->
5.3 Successfulness Threshold

<!-- b000498 | prose | pages [16] -->
To decide a product is either successful or failed, we need to determine a threshold. At ﬁrst deﬁne our threshold as a constant and set its value at 0.5:

<!-- b000499 | prose | pages [16] -->
threshold(t)

<!-- b000500 | prose | pages [16] -->
i,k = 0.5 (22)

<!-- b000501 | prose | pages [16] -->
When evaluating the future successfulness of a product, we ﬁrst obtain a time series of its reputations calculated by its rating and review records with our Reputation Model, next we run regression analysis on the obtained time series and predict the product’s future reputation, then we map the predicted reputation to pi,k(t), and ﬁnally, we decide a product will have

<!-- b000502 | prose | pages [16] -->
i,k and is doomed to failure if pi,k(t) < threshold(t)

<!-- b000503 | prose | pages [16] -->
success in the future if pi,k(t) ≥threshold(t)

<!-- b000504 | prose | pages [16] -->
i,k.

<!-- b000505 | prose | pages [16] -->
Using our method stated above, we perform predictions on some models’ potential suc- cessfulness in the future. Some of the results are listed in Table 5.

<!-- b000506 | caption | pages [16] -->
Table 5: A fraction of product models’ successfulness predictions.

<!-- b000507 | prose | pages [16] -->
Prediction/Product type Hair dryers Will succeed #732252283, #47684938, #486774008, #328811288... Doomed to failure #862140913, #932955324 #945323010, #768062995...

<!-- b000508 | prose | pages [16] -->
Microwaves Paciﬁers #423421857, #109226352, #246038397, #392768822 #771401205, #943347999...

<!-- b000509 | prose | pages [16] -->
#667171015, #343148814... #392967251, #565545704, #671647927 #618770050...

<!-- b000510 | prose | pages [16] -->
#130912179, #181638405...

<!-- b000511 | prose | pages [16] -->
However, because different models in a set of products vary much in terms of their launch date (decided by the date of their ﬁrst rating and review records), our successfulness predic- tions could be inaccurate if we set the threshold as a constant. Suppose a newly-designed

<!-- b000512 | prose | pages [16] -->
关注数学模型

<!-- b000513 | furniture | pages [16] -->
2

<!-- b000514 | furniture | pages [16] -->
MATHmodels

<!-- b000515 | furniture | pages [16] -->
获取更多资讯

<!-- b000516 | furniture | pages [17] -->
Team # 2004647

<!-- b000517 | furniture | pages [17] -->
Page 16 of 24

<!-- b000518 | prose | pages [17] -->
microwave is launched near Aug. 2015 and has great business potential, yet since it is a young product and has a relatively low reputation at the beginning, it might be considered a failure in the future—which it is likely not—if we neglect the consideration of products’ age when eval- uating future successfulness. Accordingly, we modify our threshold for successfulness and make it a function of time, as shown in Equation (23):

<!-- b000519 | prose | pages [17] -->
i,k = 0.5 −0.1e−1

<!-- b000520 | prose | pages [17] -->
threshold(t)

<!-- b000521 | prose | pages [17] -->
10 (t−τ) (23)

<!-- b000522 | prose | pages [17] -->
where τ < t denotes the τth is month when the product is launched.

<!-- b000523 | prose | pages [17] -->
After the modiﬁcation, we re-evaluate the same set of models above and obtain a slightly different result, where Hair dryer #945323010, #767062995 and Paciﬁer #130912179, #181638405 re-predicted as potentially successful in the future. By looking up their review and sales in the data sets, we ﬁnd these re-predictions reasonable, for they appear to seem promising statisti- cally. Therefore, our model is reliable when predicting a product’s future successfulness.

<!-- b000524 | prose | pages [17] -->
6

<!-- b000525 | heading | pages [17] -->
Results

<!-- b000526 | prose | pages [17] -->
Evaluation of Star Rating’s Incitement 6.1

<!-- b000527 | prose | pages [17] -->
When discovering whether or not speciﬁc star ratings incite more some type of reviews, we mainly consider two scenarios: When seeing a series of high ratings, do customers tend to write some type of reviews? And when seeing a series of low ratings, do customers tend to write some type of reviews?

<!-- b000528 | prose | pages [17] -->
We deﬁne a high rating as a star rating of either 4 or 5, and a low rating as a star rating of either 1 or 2. To better address this section’s task, we also categorize reviews into three differ- ent types, including positive reviews, neutral reviews and negativive reviews. As previously deﬁned in Section 3.3, similar to the process of review score calculation—yet this time we do not include the correction term ϵ —we consider a review with β(t)

<!-- b000529 | prose | pages [17] -->
a review with β(t)

<!-- b000530 | prose | pages [17] -->
i,k,j > 0 as a positive review;

<!-- b000531 | prose | pages [17] -->
i,k,j < 0 is considered a negativive review; and a review with β(t)

<!-- b000532 | prose | pages [17] -->
considered a neutral review.

<!-- b000533 | prose | pages [17] -->
i,k,j = 0 is

<!-- b000534 | prose | pages [17] -->
In order to observe the particular type of reviews that customers post after seeing a series of high ratings, we can sort a set of reviews (which are of the same product model, identiﬁed by the "parent_product" attribute) by time order and then record the type of reviews that are posted right after several high ratings occur. To make our solution more lucid, we deﬁne the event that k ratings (either of the type "high" or "low") subsequently occur as the k-event. Thus, once a k-event of high ratings occurs, we can record the type of the very next review, and after repeating this process for a good amount of times—enough for frequency to indicate probability. By varying the value of k, we can infer whether customers would write some type of reviews after seeing different numbers of subsequent speciﬁc ratings.

<!-- b000535 | prose | pages [17] -->
We ﬁrst apply our method while only considering top-5 models that have the largest sales throughout their lifespan (derived from the numbers of their review and rating records) of all three types of products, to ﬁnd out some patterns. The selected models are listed in Table 6.

<!-- b000536 | prose | pages [17] -->
We then iterate through their k-events (k = 2, 3, 4, 5) of both high ratings and low ratings, record the type of review right after every k-event; thus we can obtain frequency of the three types of reviews (following k-events). By performing weighted summation with models’ num- bers of orders being the weights, we can obtain the approximate probabilities of different types

<!-- b000537 | prose | pages [17] -->
关注数学模型

<!-- b000538 | furniture | pages [17] -->
2

<!-- b000539 | furniture | pages [17] -->
MATHmodels

<!-- b000540 | furniture | pages [17] -->
获取更多资讯

<!-- b000541 | furniture | pages [18] -->
Team # 2004647

<!-- b000542 | furniture | pages [18] -->
Page 17 of 24

<!-- b000543 | caption | pages [18] -->
Table 6: Top-5 models with largest sales.

<!-- b000544 | prose | pages [18] -->
Top-5 Models with Largest Sales Product Type #732252283, #758099411, #47684938, #235105995, #694290590 Hair Dryer #423421857, #544821753, #109226352, #771401205, #827502283 Microwave #246038397, #392768822, #572944212, #450475749, #812583172 Paciﬁer

<!-- b000545 | prose | pages [18] -->
of reviews which customers might post after a k-event. Results are listed in Table 7 and Table 8.

<!-- b000546 | caption | pages [18] -->
Table 7: Estimated probabilities of three types of reviews’s apperance following after k-events

<!-- b000547 | prose | pages [18] -->
(k = 2, 3, 4, 5) of high ratings, respectively measured for each type of products. Note: P+ is the probability of a review being type "positive"; P0 is the probability of a review being type "neutral"; P−is the probability of a review being type "negative".

<!-- b000548 | prose | pages [18] -->
P+/P0/P− k = 2 k = 3 k = 4 k = 5 0.5899/0.2022/0.2078 Hair Dryer 0.5875/0.2040/0.2085 0.5721/0.2141/0.2137 0.5723/0.2142/0.2134 0.4710/0.3032/0.2258 Microwave 0.4856/0.2981/0.2163 0.5088/0.2982/0.1930 0.5301/0.2892/0.1807 0.5753/0.2650/0.1597 Paciﬁer 0.5839/0.2579/0.1582 0.5892/0.2593/0.1515 0.5891/0.2518/0.1591

<!-- b000549 | caption | pages [18] -->
Table 8: Estimated probabilities of three types of reviews’s apperance following after k-events

<!-- b000550 | prose | pages [18] -->
(k = 2, 3, 4, 5) of high ratings, respectively measured for each type of products.

<!-- b000551 | prose | pages [18] -->
P+/P0/P− k = 2 k = 3 k = 4 k = 5 0.3472/0.1736/0.4791 Hairdryer 0.3040/0.1486/0.5472 0.1666/0.1666/0.6665 0/0/1 0.2500/0.2500/0.5000 microwave 0.3750/0.2083//0.4167 0.5000/0/0.5000 0.5000/0/0.5000 0.4120/0.1675/0.4205 paciﬁer 0.0714/0.6429/0.2857 0.2675/0.3089/0.4236 0.1156/0.2320/0.6524

<!-- b000552 | prose | pages [18] -->
From Table 7 we can see three types of products share some similarities: when seeing a k-event of high ratings take place, customers of all types of products are mostly likely to post positive reviews, with an average probability of 55.23%. Therefore, we can draw a rough conclusion that customers are incited to write positive reviews after seeing a series of high ratings being posted.

<!-- b000553 | prose | pages [18] -->
However, in comparison, results in Table 8 do not look very ideal. For hair dryers, the probability of negative reviews following a series of low ratings is the largest among those of positive and neutral reviews, which is reasonable. Yet for microwaves, untrustworthy results appear when k = 4, 5, where probabilities of negative and positive reviews are equal.

<!-- b000554 | prose | pages [18] -->
In fact, we ﬁnd out the number of low ratings on top selling models is signiﬁcantly lower than the number of high ratings—which makes sense since they are best sellers. Therefore, it is rare for subsequent low ratings to appear, making our measure error-prone. To draw a ﬁner conclusion, instead of covering merely hot-selling models, we broaden our coverage to 95% of models among each type of products in our measure. Nevertheless, the frequency of more than 4 subsequent low ratings appearing is still rather low compared with that of high ratings. Hence, we are not able to assess low ratings’ incitement to customers’ negative reviews with conﬁdence.

<!-- b000555 | prose | pages [18] -->
To sum it up, we do ﬁnd high ratings incite more positive reviews; at the other end, we cannot determine whether low ratings’ incitement to negative reviews.

<!-- b000556 | prose | pages [18] -->
关注数学模型

<!-- b000557 | furniture | pages [18] -->
2

<!-- b000558 | furniture | pages [18] -->
MATHmodels

<!-- b000559 | furniture | pages [18] -->
获取更多资讯

<!-- b000560 | furniture | pages [19] -->
Team # 2004647

<!-- b000561 | furniture | pages [19] -->
Page 18 of 24

<!-- b000562 | prose | pages [19] -->
Association between Review Wording and Rating Levels 6.2

<!-- b000563 | prose | pages [19] -->
Empirically, we suppose when people are giving ratings based on their feelings—which can be inferred by their reviews—towards products, the rating levels are likely somewhat associated with the reviews’ contents.

<!-- b000564 | prose | pages [19] -->
To verify our theory, we calculate our graded-words’ appearance in all of the reviews, recording their (viz., the reviews the words appear in) different corresponding star-rating lev- els at the same time. Note that multiple apperances of a word within the same review is only counted once. On the grounds of this, we deﬁne a word’s star-rate as its particular rating level’s percentage of all the ratings it is connected to.

<!-- b000565 | prose | pages [19] -->
Particularly, we achieve a list of top-5 words with the largest 5-star-rates (Table 9). As shown in the results, all of the words are positive adjectives and 4 out of 5 have a grade of 3 (the highest intensity level), with every one of them having a 5-star-rate over 80%. On the other hand, we also achieve a list of top-5 words with the largest 1-star-rates (Table 10). And from the results, we can see all of the words are negative words and 3 out of 5 have a grade of 3, with every one of them having a 1-star-rate over 35% (which is still a high percentage for one star ratings—people usually do not rate that low).

<!-- b000566 | prose | pages [19] -->
Since a small sample size cannot prove it all, we then calculate the high star-rates (with a star rating over 3) of all the frequent words (words appear more than 50 times among all reviews). And our result show that 37.84% of the words have high star-rates over 80%; all of these words are positive words while 60.87% of them have the highest level of positivity intensity. At the other end, we also calculate the low star-rates (with a star rating below 3) of all the frequent words, and 10.29% of the words have low star-rates over 50%, all of which are negative words and 100% of them have a level of negativity intensity equal or more than 2. Such results reveal strong associations between sentiment words (which also serve as quality descriptors) and rating levels.

<!-- b000567 | caption | pages [19] -->
Table 9: Top-5 words with the largest 5-star-rates. For the full top-30 one, see Table 13 in

<!-- b000568 | prose | pages [19] -->
Appendices.

<!-- b000569 | prose | pages [19] -->
2-Star-Rate Word Count Grade 1-Star-Rate 3 3-Star-Rate 4-Star-Rate 5-Star-Rate 0.8696 0.0109 awesome 92 0.0435 3 0.0435 0.0326 0.8623 0.0145 wonderful 138 0.0072 3 0.0290 0.0870 0.8462 0.0192 love 52 0.0192 3 0.0192 0.0962 0.8299 0.0249 adorable 241 0.0166 2 0.0332 0.0954 0.8295 0.0271 favorite 258 0.0078 0.0271 0.1085

<!-- b000570 | caption | pages [19] -->
Table 10: Top-5 words with the largest 1-star-rates. For the full top-20 one, see Table 14 in

<!-- b000571 | prose | pages [19] -->
Appendices.

<!-- b000572 | prose | pages [19] -->
2-Star-Rate Word Count Grade 1-Star-Rate 3 0.6346 dangerous 52 3 0.5000 terrible 54 2 0.4255 poor 94 2 0.3622 disappointed 196 3 0.3607 horrible 61 3-Star-Rate 4-Star-Rate 5-Star-Rate 0.0962 0.0769 0.0385 0.1538 0.1111 0.0741 0.1481 0.1667 0.2447 0.1383 0.0638 0.1277 0.2245 0.1837 0.0867 0.1429 0.1639 0.1475 0.1148 0.2131

<!-- b000573 | prose | pages [19] -->
关注数学模型

<!-- b000574 | furniture | pages [19] -->
2

<!-- b000575 | furniture | pages [19] -->
MATHmodels

<!-- b000576 | furniture | pages [19] -->
获取更多资讯

<!-- b000577 | furniture | pages [20] -->
Team # 2004647

<!-- b000578 | prose | pages [20] -->
6.3 Our Strategies

<!-- b000579 | furniture | pages [20] -->
Page 19 of 24

<!-- b000580 | prose | pages [20] -->
For Sunshine Company to improve their competition in the marketplace, we fully utilize our knowledge gained with our models, and come up with some marketing strategies and possibly important design features they can adopt.

<!-- b000581 | prose | pages [20] -->
6.3.1 Marketing Strategies

<!-- b000582 | prose | pages [20] -->
We notice the potential intensity of competition that comes along with entrance into different speciﬁc markets may vary, due to customers’ different established preference towards partic- ular products within a speciﬁc market. For example, if a large fraction of customers are loyal customers to—hypothetically speaking —Moonlight Company’s paciﬁers, it can be hard for Sunshine Company to induce those customers into buying their paciﬁers.

<!-- b000583 | prose | pages [20] -->
To measure this "preference" that customers have, we can utilize our reputation measure. We can perform weighted average of all product models’ reputations, which are weighted by the products’ sales. Then, by the scale of the results, we can tell if some strong loyalty in a market is established. Using this method, we obtain Table 11. As it can be seen, the paciﬁer market has the strongest loyalty while the microwaves has the weakest. That is to say, it takes the most effort to compete in the paciﬁer market.

<!-- b000584 | prose | pages [20] -->
Accordingly, we propose following marketing strategies:

<!-- b000585 | prose | pages [20] -->
• If Sunshine Company has enough effort to spare, we suggest they put more effort in selling paciﬁers, e.g., allocating more of their advertising budget to their paciﬁer;

<!-- b000586 | prose | pages [20] -->
• If Sunshine Company does not have enough effort to spare (due to shorthanded-ness or limited budget), we suggest they put more of their limited effort in selling microwaves, for they can pursue superiority in at least one market;

<!-- b000587 | prose | pages [20] -->
• No matter what, Sunshine Company should constantly track our score and reputation measure of their products, for they can ﬁnely reﬂect customers’ opinion on the products.

<!-- b000588 | prose | pages [20] -->
6.3.2 Important Design Features

<!-- b000589 | prose | pages [20] -->
To identify what important features customers care most about, we calculate appearance of words among all reviews of each type of products. Some operations are carried out to extract quality descriptors that indicate design features:

<!-- b000590 | prose | pages [20] -->
1 Leave out words that are not nouns, for nouns describe what speciﬁc features customers need;

<!-- b000591 | prose | pages [20] -->
2 Leave out words that do not refer to speciﬁc qualites of products.

<!-- b000592 | caption | pages [20] -->
Table 11: Estimated competition intensity in three different markets.

<!-- b000593 | prose | pages [20] -->
Reputation weight average Product type Hair dryers Microwaves Paciﬁers 239.7633 184.0208 305.3781

<!-- b000594 | prose | pages [20] -->
关注数学模型

<!-- b000595 | furniture | pages [20] -->
2

<!-- b000596 | furniture | pages [20] -->
MATHmodels

<!-- b000597 | furniture | pages [20] -->
获取更多资讯

<!-- b000598 | furniture | pages [21] -->
Team # 2004647

<!-- b000599 | furniture | pages [21] -->
Page 20 of 24

<!-- b000600 | prose | pages [21] -->
Then we obtain a table of top-3 most mentioned features of each type of products, as shown in Table 12, which represent the most important features that Sunshine Company should con- sider most when designing their products. From it we can suppose customers expect a reason- able price for all three types of products. While speciﬁcally:

<!-- b000601 | prose | pages [21] -->
• Customers might want a hair dryer to be able to produce enough heat and to have a high-quality cord;

<!-- b000602 | prose | pages [21] -->
• Microwaves are expected to have a sufﬁcient space and customer service is also valued since machines can break down any second;

<!-- b000603 | prose | pages [21] -->
• Paciﬁers are for babies, reasonably parents expect them to have a good quality and ap- propriate size so that babies feel comfortable biting on it.

<!-- b000604 | caption | pages [21] -->
Table 12: Top-3 most mentioned features of each type of products.

<!-- b000605 | prose | pages [21] -->
Hair dryers price(1063) Word(Count) heat(960) cord(805

<!-- b000606 | prose | pages [21] -->
7

<!-- b000607 | heading | pages [21] -->
Sensitivity Analysis

<!-- b000608 | prose | pages [21] -->
Microwaves Paciﬁers space(183) quality(405) price(147) size(395) service(137) price(333)

<!-- b000609 | prose | pages [21] -->
We carry out sensitivity analysis on two main parameters: λ (Equation (1)) and a (Equation (17)). First, we change the value of a from −10% to +10%, each time a step of 5%. The results, as shown in Figure 6(a), show that the reputation trend only slightly vary roughly before the 38th month, but it becomes quite sensitive as the timestamp moves on. It is reasonable since the score in the RRBS Model is exponentially weighted and summed up to acquire the reputation. Therefore, a is a critical parameter that should be carefully determined. Then, similarly, we change the value of λ from −10% to +10%, and evaluate its sensitivity. As shown in Figure 6(b), it does not appear to be noticeably sensitive.

<!-- b000610 | prose | pages [21] -->
To sum it up, one of our two parameters—a—is tested out to be a sensitive parameter. But in general, our models have a fair degree of robustness.

<!-- b000611 | prose | pages [21] -->
8

<!-- b000612 | heading | pages [21] -->
Strengths and Weaknesses

<!-- b000613 | prose | pages [21] -->
8.1

<!-- b000614 | heading | pages [21] -->
Strengths

<!-- b000615 | prose | pages [21] -->
• Full utilization of information: When designing our measures, not only do we com- bine star ratings and review contents, but also we consider other useful attributes in the provided data;

<!-- b000616 | prose | pages [21] -->
• Great model performance: The high correlation between trends of our quantiﬁed reputa- tion and acutal sales suggests our models have great performance and that our measures are accurate;

<!-- b000617 | prose | pages [21] -->
• Good choice of methodology: We reveal the strong connections between positive words and high ratings, negative and low ratings, thanks to our choice of methodology;

<!-- b000618 | prose | pages [21] -->
关注数学模型

<!-- b000619 | furniture | pages [21] -->
2

<!-- b000620 | furniture | pages [21] -->
MATHmodels

<!-- b000621 | furniture | pages [21] -->
获取更多资讯

<!-- b000622 | furniture | pages [22] -->
Team # 2004647

<!-- b000623 | prose | pages [22] -->
(a)

<!-- b000624 | furniture | pages [22] -->
Page 21 of 24

<!-- b000625 | prose | pages [22] -->
(b)

<!-- b000626 | caption | pages [22] -->
Figure 6: Sensitivity analysis results of our two main parameters: λ and a.

<!-- b000627 | prose | pages [22] -->
• High robustness: In general, our models are not insensitive to value change of parame- ters.

<!-- b000628 | prose | pages [22] -->
8.2

<!-- b000629 | heading | pages [22] -->
Weaknesses

<!-- b000630 | prose | pages [22] -->
• Certain degree of arbitrariness in model designs: We adopt an arbitrary mindset when designing part of our models;

<!-- b000631 | prose | pages [22] -->
• Limitations of our acquired word set: The word set we use to match review contents in the RBSS Model lacks in size to some degree, leaving out some information when measuring products’ scores;

<!-- b000632 | prose | pages [22] -->
9

<!-- b000633 | heading | pages [22] -->
Conclusion

<!-- b000634 | prose | pages [22] -->
In our work, we propose the RRBS Model and the Reputation Model to provide a rating-based, review-based and time-based measure that ﬁnely describes a product’s reputation over time periods. Using this measure, we are able to predict a product’s potential success or failure in the future. We also ﬁnd out that a sequence of high ratings can incite more positive reviews, yet cannot determine whether sequences of low ratings have similar effects. A strong associ- ation between rating levels and speciﬁc quality descriptors of reviews is also found by word matching and appearance calculation. Finally, we provide Sunshine Company our devised marketing strategies and point out some design features of products they can work on to, so as to improve their overall competitiveness in the marketplace.

<!-- b000635 | prose | pages [22] -->
关注数学模型

<!-- b000636 | furniture | pages [22] -->
2

<!-- b000637 | furniture | pages [22] -->
MATHmodels

<!-- b000638 | furniture | pages [22] -->
获取更多资讯

<!-- b000639 | furniture | pages [23] -->
Team # 2004647

<!-- b000640 | furniture | pages [23] -->
10

<!-- b000641 | prose | pages [23] -->
Our Letter

<!-- b000642 | prose | pages [23] -->
From: Team #2004647

<!-- b000643 | furniture | pages [23] -->
Page 22 of 24

<!-- b000644 | prose | pages [23] -->
To: Marketing Director of Sunshine Company Date: March 9, 2020

<!-- b000645 | prose | pages [23] -->
Dear Marketing Director of Sunshine Company,

<!-- b000646 | prose | pages [23] -->
Thank you for hiring us as your consultants! We are informed of your speciﬁed require- ments and have fully evaluated the feasibility of our tasks. Here we present to you with our detailed solutions.

<!-- b000647 | prose | pages [23] -->
We thoroughly examined the data of reviews and ratings associated with our competitors’ products. We discovered that a lot of the attributes of the data can be utilized, along with the actual rating levels and review contents, to ﬁgure out an fairly informative measure for you to track. To perform quantiﬁcation on them, we proposed the Rating and Review Based Score Model, which introduces our deﬁned data measure—score. In our model, a product’s score describes customers’ responses to the product. It is based on both ratings and text reviews. When calculating the score of a product, we take into account of:

<!-- b000648 | prose | pages [23] -->
• Its received rating levels;

<!-- b000649 | prose | pages [23] -->
• Whether its reviews are from Vine reviewers;

<!-- b000650 | prose | pages [23] -->
• The sentiment intensity of the review contents (as "fair" is less intense than "wonderful", with both being positive words);

<!-- b000651 | prose | pages [23] -->
• Whether its reviews are from veriﬁed buyers;

<!-- b000652 | prose | pages [23] -->
• The helpness-ratings of its reviews, which help ﬁltering out reviews that are already unhelpful to other customers;

<!-- b000653 | prose | pages [23] -->
• The lengths of its reviews.

<!-- b000654 | prose | pages [23] -->
By combining these factors altogether, our measure should be able to pick out the most valuable ones among all kinds of voices, which your company should attach great importance to once your products are launched—because they contain crucial information for you to know what problems your products have and how you can improve.

<!-- b000655 | prose | pages [23] -->
Based on our score measure, we further proposed the Reputation Model, which straight- forwardly deﬁnes the reputation of a product—which is a time-based measure for quantifying a product’s reputations among customers over time periods. The measure was proved to be fairly accurate in terms of describing a product’s actual (but abstract) reputation, supported by the strong correlation between trends of the quantiﬁed reputations and the product’s sales.

<!-- b000656 | prose | pages [23] -->
Empirical knowledge suggests the successfulness of a product is closely connected to its sales. Since we know our reputation measure is reliable and strongly correlated with the prod- uct’s sales, we can utilize it to indicate a product’s future successfulness. We approached this by adopting Gaussian Process Regression, and it turns out we can ﬁnely predict a product’s reputations in the near future based on time series of its calculated reputations. Therefore, we are able to predict a product’s potential success or failure in the future in the short term; though it lacks in accuracy when making long-term predictions.

<!-- b000657 | prose | pages [23] -->
As for the speciﬁc questions you are concerned about, we seeked to ﬁnd out whether a se- ries of speciﬁc ratings can incite some type of reviews. By recording customers’ reviews right

<!-- b000658 | prose | pages [23] -->
关注数学模型

<!-- b000659 | furniture | pages [23] -->
2

<!-- b000660 | furniture | pages [23] -->
MATHmodels

<!-- b000661 | furniture | pages [23] -->
获取更多资讯

<!-- b000662 | furniture | pages [24] -->
Team # 2004647

<!-- b000663 | furniture | pages [24] -->
Page 23 of 24

<!-- b000664 | prose | pages [24] -->
after a series of same ratings, by calculating the chance of them being either positive, nega- tive or neutral, we managed to ﬁnd out that a series of high ratings do incite more positive reviews—which indicates a signiﬁcant reputational increase. However, due to lack of evi- dence, we cannot determine for sure whether a series of low ratings incite negative reviews.

<!-- b000665 | prose | pages [24] -->
To address the other question that whether speciﬁc quality descriptors are strongly associ- ated with rating levels, we ﬁrst obtained a word set of 2,477 words, all of which are graded by its sentiment intensity (say "wonderful" is more positively intense than "fair"). Then we match all of the review contents in the provided data and calculate words’ appearance and associated rating levels. The results reveal noticeably strong connections between them. For example, of all the reviews that contain the word "awesome" (which has a maximum of positiveness inten- sity), 86.96% of them are associated with a 5-star rating. On the other hand, of all the reviews that contain "dangerous" (which has a maximum of negativeness intensity), 63.46% of them are associated with a 1-star rating.

<!-- b000666 | prose | pages [24] -->
Finally, with our modeling and methodology, we have devised a set of marketing strategies you can adopt, and a set of design features for each product that customers value the most. We ﬁrst performed weighted average of all product models’ reputations in each market, which are weighted by the products’ sales, and thus we have a measure for the potential competition that your company will encounter, for average reputations in a market can indicate the market’s customer loyalty. The results reveal that it takes the most effort to compete in the paciﬁer market and the least in the microwave market. Therefore, we present following marketing strategies:

<!-- b000667 | prose | pages [24] -->
• If your company has enough effort to spare, we suggest you put more effort in selling paciﬁers, e.g., allocating more of your advertising budget to your paciﬁer;

<!-- b000668 | prose | pages [24] -->
• If your company does not have enough effort to spare (due to shorthanded-ness or lim- ited budget), we suggest you put more of your limited effort in selling microwaves, for you can pursue superiority in at least one market;

<!-- b000669 | prose | pages [24] -->
• No matter what, your company should constantly track our score and reputation measure of your products, for they can ﬁnely reﬂect customers’ opinion on the products.

<!-- b000670 | prose | pages [24] -->
Subsequently, we matched the reviews with quality specifying nouns and calculated their appearance. Then we picked 3 words with most appearance for each product, which indicate design features customers value the most. The results show that customers expect a reasonable price for all three types of products. While speciﬁcly:

<!-- b000671 | prose | pages [24] -->
• Customers might want a hair dryer to be able to produce enough heat and to have a high-quality cord;

<!-- b000672 | prose | pages [24] -->
• Microwaves are expected to have a sufﬁcient space and customer service is also valued since machines can break down any second;

<!-- b000673 | prose | pages [24] -->
• Paciﬁers are for babies, reasonably parents expect them to have a good quality and ap- propriate size so that babies feel comfortable biting on it.

<!-- b000674 | prose | pages [24] -->
If you want to know more details, please refer to our thesis. We will be glad to discuss with you on our solution details.

<!-- b000675 | prose | pages [24] -->
关注数学模型

<!-- b000676 | furniture | pages [24] -->
2

<!-- b000677 | furniture | pages [24] -->
MATHmodels

<!-- b000678 | furniture | pages [24] -->
获取更多资讯

<!-- b000679 | furniture | pages [25] -->
Team # 2004647

<!-- b000680 | heading | pages [25] -->
References

<!-- b000681 | furniture | pages [25] -->
Page 24 of 24

<!-- b000682 | references | pages [25] -->
[1] I. AMAZON.COM, What is amazon vine?, accessed March 7, 2020.

<!-- b000683 | references | pages [25] -->
[2] S. BIRD AND E. LOPER, NLTK: The natural language toolkit, in Proceedings of the ACL In-

<!-- b000684 | references | pages [25] -->
teractive Poster and Demonstration Sessions, Barcelona, Spain, July 2004, Association for

<!-- b000685 | references | pages [25] -->
Computational Linguistics, pp. 214–217.

<!-- b000686 | references | pages [25] -->
[3] A. CHUA AND S. BANERJEE, Understanding review helpfulness as a function of reviewer reputa-

<!-- b000687 | references | pages [25] -->
tion, review rating, and review depth, Journal of the Association for Information Science and

<!-- b000688 | references | pages [25] -->
Technology, 66 (2014).

<!-- b000689 | references | pages [25] -->
[4] Y. KOREN, R. BELL, AND C. VOLINSKY, Matrix factorization techniques for recommender sys-

<!-- b000690 | references | pages [25] -->
tems, Computer, 42 (2009), pp. 30–37.

<!-- b000691 | references | pages [25] -->
[5] J. MCAULEY AND J. LESKOVEC, Hidden factors and hidden topics: Understanding rating dimen-

<!-- b000692 | references | pages [25] -->
sions with review text, in Proceedings of the 7th ACM Conference on Recommender Systems,

<!-- b000693 | references | pages [25] -->
RecSys 13, New York, NY, USA, 2013, Association for Computing Machinery, p. 165172.

<!-- b000694 | references | pages [25] -->
[6] F. Å. NIELSEN, Aﬁnn, mar 2011.

<!-- b000695 | references | pages [25] -->
[7] C. E. RASMUSSEN AND C. K. I. WILLIAMS, Gaussian Processes for Machine Learning (Adap-

<!-- b000696 | references | pages [25] -->
tive Computation and Machine Learning), The MIT Press, 2005.

<!-- b000697 | references | pages [25] -->
[8] Y. TAN, M. ZHANG, Y. LIU, AND S. MA, Rating-boosted latent topics: Understanding users

<!-- b000698 | references | pages [25] -->
and items with ratings and reviews, in Proceedings of the Twenty-Fifth International Joint

<!-- b000699 | references | pages [25] -->
Conference on Artiﬁcial Intelligence, IJCAI16, AAAI Press, 2016, p. 26402646.

<!-- b000700 | references | pages [25] -->
[9] W. XU, C. CHANG, Y. S. HUNG, S. K. KWAN, AND P. C. W. FUNG, Order statistics corre-

<!-- b000701 | references | pages [25] -->
lation coefﬁcient as a novel association measurement with applications to biosignal analysis, IEEE

<!-- b000702 | references | pages [25] -->
Transactions on Signal Processing, 55 (2007), pp. 5552–5563.

<!-- b000703 | references | pages [25] -->
关注数学模型

<!-- b000704 | furniture | pages [25] -->
2

<!-- b000705 | furniture | pages [25] -->
MATHmodels

<!-- b000706 | furniture | pages [25] -->
获取更多资讯

<!-- b000707 | furniture | pages [26] -->
Team # 2004647

<!-- b000708 | heading | pages [26] -->
Appendices

<!-- b000709 | prose | pages [26] -->
aﬁnn-matcher.py

<!-- b000710 | prose | pages [26] -->
Page 25

<!-- b000711 | prose | pages [26] -->
# This program is used to match reviews with graded-words provided by Afinn word set import csv import nltk import re from afinn import Afinn

<!-- b000712 | prose | pages [26] -->
def split(delimiters, string, maxsplit=0):

<!-- b000713 | prose | pages [26] -->
regexPattern = ’|’.join(map(re.escape, delimiters)) return re.split(regexPattern, string, maxsplit)

<!-- b000714 | prose | pages [26] -->
delims = ",.;?<>()! "

<!-- b000715 | prose | pages [26] -->
af = Afinn(language=’en’) adjs = {} files = ["pacifier.csv", "microwave.csv", "hair_dryer.csv"]

<!-- b000716 | prose | pages [26] -->
cnt = 0 for file in files:

<!-- b000717 | prose | pages [26] -->
with open(file, "r", encoding="utf-8", errors=’ignore’) as f:

<!-- b000718 | prose | pages [26] -->
reader = csv.DictReader(f) for line in reader:

<!-- b000719 | prose | pages [26] -->
cnt += 1 if cnt % 100 == 0:

<!-- b000720 | prose | pages [26] -->
print("Reading line " + str(cnt) +

<!-- b000721 | prose | pages [26] -->
", dict size=" + str(len(adjs))) review = line["review_headline"] + line["review_body"] toks = split(delims, review) toks = set(filter(None, toks)) # print(toks) words = nltk.pos_tag(toks) for i in range(len(words)):

<!-- b000722 | prose | pages [26] -->
tup = words[i] if tup[1] == "JJ":

<!-- b000723 | prose | pages [26] -->
word = tup[0] word = word.lower() score = af.score(word) if score == 0:

<!-- b000724 | prose | pages [26] -->
continue adjs[word] = [sum(x) for x in zip(

<!-- b000725 | prose | pages [26] -->
adjs.get(word, [0] * 7), [1, 0, 0, 0, 0, 0, 0])] rating = int(line["star_rating"]) if rating > 5 or rating < 1:

<!-- b000726 | prose | pages [26] -->
continue adjs[word][rating] += 1 adjs[word][6] = score

<!-- b000727 | prose | pages [26] -->
out = "matched_words.csv"

<!-- b000728 | prose | pages [26] -->
with open(out, "w", encoding="utf-8") as f:

<!-- b000729 | prose | pages [26] -->
writer = csv.writer(f, delimiter=",") for key, value in adjs.items():

<!-- b000730 | prose | pages [26] -->
row = [key] + value writer.writerow(row)

<!-- b000731 | prose | pages [26] -->
关注数学模型

<!-- b000732 | furniture | pages [26] -->
2

<!-- b000733 | furniture | pages [26] -->
MATHmodels

<!-- b000734 | furniture | pages [26] -->
获取更多资讯

<!-- b000735 | furniture | pages [27] -->
Team # 2004647

<!-- b000736 | prose | pages [27] -->
RRBS-reputation.m

<!-- b000737 | prose | pages [27] -->
for i=2:length(S(:,1))

<!-- b000738 | prose | pages [27] -->
index=find(item==cell2mat(S(i,5))); if mod(timer,12)~=0

<!-- b000739 | prose | pages [27] -->
if review_date(i,2)~=mod(timer,12)

<!-- b000740 | prose | pages [27] -->
timer=timer+1; end else

<!-- b000741 | prose | pages [27] -->
if review_date(i,2)==1

<!-- b000742 | prose | pages [27] -->
timer=timer+1; end end if ~isempty(index)

<!-- b000743 | prose | pages [27] -->
if K(i,1)==0

<!-- b000744 | prose | pages [27] -->
beta=1; else

<!-- b000745 | prose | pages [27] -->
if K(i,1)>0

<!-- b000746 | prose | pages [27] -->
Page 26

<!-- b000747 | prose | pages [27] -->
beta=vine(i,1)*K(i,1)^verified(i,1)*exp(helpful_of_total_votes(i,1))*0.5*log else

<!-- b000748 | prose | pages [27] -->
beta=vine(i,1)*(-1)*(abs(K(i,1)))^verified(i,1)*exp(helpful_of_total_votes( end end record(timer,1,index)=record(timer,1,index)+1; record(timer,2,index)=record(timer,2,index)+rating_123(i,1).*beta; end end

<!-- b000749 | prose | pages [27] -->
begin=zeros(1,top); alpha=1.1; for index=1:length(record(1,1,:))

<!-- b000750 | prose | pages [27] -->
exponent_window_origina=[]; begin(1,index)=find(record(:,1,index)>0, 1, ’first’); record(1:begin(1,index)-1,3,index)=zeros(begin(1,index)-1,1); for j=1:length(record(:,1,1))-begin(1,index)+1

<!-- b000751 | prose | pages [27] -->
exponent_window_origina=[exponent_window_origina,alpha^j]; end for i=begin(1,index):length(record(:,1,1))

<!-- b000752 | prose | pages [27] -->
exponent_window=exponent_window_origina./alpha^(i-begin(1,index)+1); record(i,3,index)=exponent_window(1,1:i-begin(1,index)+1)*record(begin(1,index):i,2 end end

<!-- b000753 | prose | pages [27] -->
关注数学模型

<!-- b000754 | furniture | pages [27] -->
2

<!-- b000755 | furniture | pages [27] -->
MATHmodels

<!-- b000756 | furniture | pages [27] -->
获取更多资讯

<!-- b000757 | furniture | pages [28] -->
Team # 2004647

<!-- b000758 | prose | pages [28] -->
Page 27

<!-- b000759 | caption | pages [28] -->
Table 13: Top-30 words with the largest 5-star-rates

<!-- b000760 | prose | pages [28] -->
2-Star-Rate Word Count Grade 1-Star-Rate 3 3-Star-Rate 4-Star-Rate 5-Star-Rate 0.869565217 0.010869565 awesome 92 0.043478261 3 0.043478261 0.032608696 0.862318841 0.014492754 wonderful 138 0.007246377 3 0.028985507 0.086956522 0.846153846 0.019230769 love 52 0.019230769 3 0.019230769 0.096153846 0.829875519 0.024896266 adorable 241 0.01659751 2 0.033195021 0.095435685 0.829457364 0.027131783 favorite 258 0.007751938 2 0.027131783 0.108527132 0.804597701 0.040229885 durable 174 0.011494253 3 0.040229885 0.103448276 0.803921569 0.029411765 fantastic 102 0.029411765 3 0.058823529 0.078431373 0.766595289 0.019271949 perfect 467 0.023554604 3 excellent 164 0.042682927 3 0.029978587 0.160599572 0.762195122 0 0.036585366 0.158536585 0.736842105 0.01754386 beautiful 57 0.087719298 2 0.070175439 0.087719298 0.736686391 0.026627219 cute 338 0.00591716 2 affordable 56 0 3 0.082840237 0.147928994 0.732142857 0 0.071428571 0.196428571 0.728813559 0.033898305 glad 59 0.016949153 1 0.016949153 0.203389831 0.722818792 0.019463087 easy 1490 0.01409396 3 0.040268456 0.203355705 0.720720721 0.022522523 pleased 222 0.018018018 2 0.031531532 0.207207207 0.709090909 0.054545455 satisﬁed 55 0.018181818 3 0.054545455 0.163636364 0.700980392 0.029411765 super 204 0.034313725 2 healthy 50 0.04 3 0.078431373 0.156862745 0.7 0.08 0.04 0.14 0.692390718 0.036157582 great 3706 0.031840259 3 0.062601187 0.177010254 0.692307692 0.064102564 funny 78 0.064102564 1 0.051282051 0.128205128 0.682692308 0.033653846 free 208 0.057692308 3 0.067307692 0.158653846 0.678066038 0.048349057 happy 848 0.053066038 3 0.036556604 0.183962264 0.674846626 0.049079755 loved 163 0.055214724 2 0.049079755 0.171779141 0.672064777 0.046558704 clean 494 0.046558704 2 0.062753036 0.172064777 0.666666667 0.070175439 recommend 114 0.087719298 2 0.052631579 0.122807018 0.654545455 0.036363636 effective 55 0.072727273 1 0.018181818 0.218181818 0.650205761 0.037037037 natural 243 0.057613169 2 0.065843621 0.189300412 0.638795987 0.043478261 worth 299 0.107023411 2 0.053511706 0.157190635 0.622474747 0.041666667 powerful 792 0.025252525 2 0.112373737 0.198232323 0.615384615 0.038461538 reliable 52 0.096153846 0.096153846 0.153846154

<!-- b000761 | prose | pages [28] -->
关注数学模型

<!-- b000762 | furniture | pages [28] -->
2

<!-- b000763 | furniture | pages [28] -->
MATHmodels

<!-- b000764 | furniture | pages [28] -->
获取更多资讯

<!-- b000765 | furniture | pages [29] -->
Team # 2004647

<!-- b000766 | prose | pages [29] -->
Page 28

<!-- b000767 | caption | pages [29] -->
Table 14: Top-20 words with the largest 1-star-rates

<!-- b000768 | prose | pages [29] -->
2-Star-Rate Word Count Grade 1-Star-Rate -2 0.634615385 3-Star-Rate 4-Star-Rate 5-Star-Rate 0.096153846 dangerous 52 -3 0.5 0.076923077 0.038461538 0.153846154 0.111111111 terrible 54 -2 0.425531915 0.074074074 0.148148148 0.166666667 0.244680851 poor 94 -2 0.362244898 0.138297872 0.063829787 0.127659574 0.224489796 disappointed 196 -3 0.360655738 0.183673469 0.086734694 0.142857143 0.163934426 horrible 61 -2 0.321428571 useless 56 -2 0.271317829 0.147540984 0.114754098 0.213114754 0.25 0.196428571 0.142857143 0.089285714 0.108527132 wrong 129 -3 0.246458924 0.131782946 0.100775194 0.387596899 0.101983003 bad 353 2 0.232142857 0.144475921 0.175637394 0.331444759 0.107142857 positive 56 1 0.176470588 0.089285714 0.107142857 0.464285714 0.058823529 certain 51 -2 0.175438596 0.215686275 0.215686275 0.333333333 0.245614035 weak 57 1 0.171171171 0.263157895 0.140350877 0.175438596 0.045045045 safe 111 1 0.167785235 0.063063063 0.135135135 0.585585586 0.046979866 clear 149 -1 0.132478632 0.134228188 0.22147651 0.429530201 0.128205128 difﬁcult 234 -3 0.12 loose 50 2 0.113821138 0.183760684 0.247863248 0.307692308 0.12 0.12 0.08 0.56 0.146341463 top 123 -1 0.112903226 0.089430894 0.170731707 0.479674797 0.10483871 hard 372 1 0.111111111 0.13172043 0.174731183 0.475806452 0.063492063 want 63 2 0.107023411 0.111111111 0.158730159 0.555555556 0.043478261 worth 299 -2 0.105691057 0.053511706 0.157190635 0.638795987 0.032520325 negative 123 0.056910569 0.284552846 0.520325203

<!-- b000769 | prose | pages [29] -->
关注数学模型

<!-- b000770 | furniture | pages [29] -->
2

<!-- b000771 | furniture | pages [29] -->
MATHmodels

<!-- b000772 | furniture | pages [29] -->
获取更多资讯
