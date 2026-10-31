# P-C-2020-2004647-771d613e

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2020

<!-- b000002 | front_matter | pages [1] -->
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
1 Introduction

<!-- b000025 | contents | pages [2] -->
2

<!-- b000026 | contents | pages [2] -->
1.1

<!-- b000027 | contents | pages [2] -->
Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
2

<!-- b000029 | contents | pages [2] -->
1.2

<!-- b000030 | contents | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
2

<!-- b000032 | contents | pages [2] -->
1.3

<!-- b000033 | contents | pages [2] -->
Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
3

<!-- b000035 | contents | pages [2] -->
1.4

<!-- b000036 | contents | pages [2] -->
Modeling Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
3

<!-- b000038 | contents | pages [2] -->
2 Assumptions & Nomenclature

<!-- b000039 | contents | pages [2] -->
3

<!-- b000040 | contents | pages [2] -->
3

<!-- b000041 | contents | pages [2] -->
the RRBS Model

<!-- b000042 | contents | pages [2] -->
4

<!-- b000043 | contents | pages [2] -->
3.1

<!-- b000044 | contents | pages [2] -->
Model Overview

<!-- b000045 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
5

<!-- b000047 | contents | pages [2] -->
3.2

<!-- b000048 | contents | pages [2] -->
the Rating Vector

<!-- b000049 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
5

<!-- b000051 | contents | pages [2] -->
3.3

<!-- b000052 | contents | pages [2] -->
the Review Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
6

<!-- b000054 | contents | pages [2] -->
3.3.1

<!-- b000055 | contents | pages [2] -->
The Review-based Measure Equation . . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
8

<!-- b000057 | contents | pages [2] -->
3.3.2

<!-- b000058 | contents | pages [2] -->
the Sentiment Polarity Matrix . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
9

<!-- b000060 | contents | pages [2] -->
4

<!-- b000061 | contents | pages [2] -->
the Reputation Model

<!-- b000062 | contents | pages [2] -->
10

<!-- b000063 | contents | pages [2] -->
4.1

<!-- b000064 | contents | pages [2] -->
Time Weight Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
10

<!-- b000066 | contents | pages [2] -->
4.2

<!-- b000067 | contents | pages [2] -->
Quantiﬁcation of Reputation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
11

<!-- b000069 | contents | pages [2] -->
4.3

<!-- b000070 | contents | pages [2] -->
Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
11

<!-- b000072 | contents | pages [2] -->
4.3.1

<!-- b000073 | contents | pages [2] -->
Trend Similarity between Quantiﬁed Reputation and Sales . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
11

<!-- b000075 | contents | pages [2] -->
4.3.2

<!-- b000076 | contents | pages [2] -->
Kendall’s Tau Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
12

<!-- b000078 | contents | pages [2] -->
5

<!-- b000079 | contents | pages [2] -->
the Successfulness Prediction Model

<!-- b000080 | contents | pages [2] -->
13

<!-- b000081 | contents | pages [2] -->
5.1

<!-- b000082 | contents | pages [2] -->
Gaussian Process Regression

<!-- b000083 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
14

<!-- b000085 | contents | pages [2] -->
5.2

<!-- b000086 | contents | pages [2] -->
Reputation Mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
15

<!-- b000088 | contents | pages [2] -->
5.3

<!-- b000089 | contents | pages [2] -->
Successfulness Threshold

<!-- b000090 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
15

<!-- b000092 | contents | pages [2] -->
6 Results

<!-- b000093 | contents | pages [2] -->
16

<!-- b000094 | contents | pages [2] -->
6.1

<!-- b000095 | contents | pages [2] -->
Evaluation of Star Rating’s Incitement . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
16

<!-- b000097 | contents | pages [2] -->
6.2

<!-- b000098 | contents | pages [2] -->
Association between Review Wording and Rating Levels . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
18

<!-- b000100 | contents | pages [2] -->
6.3

<!-- b000101 | contents | pages [2] -->
Our Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000102 | contents | pages [2] -->
19

<!-- b000103 | contents | pages [2] -->
6.3.1

<!-- b000104 | contents | pages [2] -->
Marketing Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [2] -->
19

<!-- b000106 | contents | pages [2] -->
6.3.2

<!-- b000107 | contents | pages [2] -->
Important Design Features

<!-- b000108 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
19

<!-- b000110 | contents | pages [2] -->
7 Sensitivity Analysis

<!-- b000111 | contents | pages [2] -->
20

<!-- b000112 | contents | pages [2] -->
8 Strengths and Weaknesses

<!-- b000113 | contents | pages [2] -->
20

<!-- b000114 | contents | pages [2] -->
8.1

<!-- b000115 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000116 | contents | pages [2] -->
20

<!-- b000117 | contents | pages [2] -->
8.2

<!-- b000118 | contents | pages [2] -->
Weaknesses

<!-- b000119 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000120 | contents | pages [2] -->
21

<!-- b000121 | contents | pages [2] -->
9 Conclusion

<!-- b000122 | contents | pages [2] -->
21

<!-- b000123 | contents | pages [2] -->
10 Our Letter

<!-- b000124 | contents | pages [2] -->
22

<!-- b000125 | contents | pages [2] -->
Appendices

<!-- b000126 | contents | pages [2] -->
25

<!-- b000127 | contents | pages [2] -->
关注数学模型

<!-- b000128 | furniture | pages [2] -->
2

<!-- b000129 | furniture | pages [2] -->
MATHmodels

<!-- b000130 | furniture | pages [2] -->
获取更多资讯

<!-- b000131 | furniture | pages [3] -->
Team # 2004647

<!-- b000132 | furniture | pages [3] -->
Page 2 of 24

<!-- b000133 | heading | pages [3] -->
1 Introduction

<!-- b000134 | prose | pages [3] -->
"Amazing things will happen when you listen to the consumer."

<!-- b000135 | prose | pages [3] -->
—Jonathan Midenhall, CMO of Airbnb

<!-- b000136 | prose | pages [3] -->
E-commerce has sprouted for the last few decades all over the world, and now it has be- come one of the most prosperous and promising modern industries. During this process, the Review and Rating System has been playing a huge role all along. Not only does it help cus- tomers ﬁnd out what is best for them when making purchase decisions, but also it helps sellers realize what problems their products have and thus things can be improved. Therefore, it is signiﬁcant for companies to know how to make the most use of it and apply the knowledge to improving product designs and marketing strategies.

<!-- b000137 | heading | pages [3] -->
1.1 Problem Restatement

<!-- b000138 | prose | pages [3] -->
Sunshine Company is about to launch three new products in the marketplace, including a mi- crowave, a baby paciﬁer and a hair dryer. Data of customer-supplied reviews and ratings for microwave ovens, baby paciﬁers and hair dryers sold on Amazon.com are supplied, each of which has a time label on. Analysis of customers’ ratings and reviews of other companies’s competing products is required in order to ﬁgure out the optimal online marketing strategies and possible design features they can employ to make their products more desirable to cus- tomers.

<!-- b000139 | prose | pages [3] -->
To achieve our goals, speciﬁcally, we need to:

<!-- b000140 | prose | pages [3] -->
• Identify the most informative data measures based on reviews and ratings for Sunshine Company to track, once they launch their three new products in the online marketplace.

<!-- b000141 | prose | pages [3] -->
• Discover time-based measures and patterns that can suggest a product’s reputation’s trend of increase or decrease.

<!-- b000142 | prose | pages [3] -->
• Combine text-based measures and rating-based measures to discover measures that best indicate a product’s potential success or faliure.

<!-- b000143 | prose | pages [3] -->
• Find out whether speciﬁc star ratings incite more reviews.

<!-- b000144 | prose | pages [3] -->
• Find out whether rating levels and speciﬁc quality descriptors of text-based reviews are strongly associated.

<!-- b000145 | heading | pages [3] -->
1.2 Literature Review

<!-- b000146 | prose | pages [3] -->
Early work have proposed several methods for utilizing reviews and ratings of online prod- ucts. In 2009, Koren et al. [4] proposed Latent Factor Models (LFM) to address the rating prediction task. In 2013, McAuley et al. [5] took advantage of the abundunt information in reviews using Latent Dirichlet Allocation (LDA) to achieve topic distributions. Later in 2016, Tan et al. [8] proposed the Rating-Boosted Latent Topics (RBLT) Framework, combining tex- tual reviews with users’ sentiment orientations, and thus recommendations are made more accurate.

<!-- b000147 | prose | pages [3, 4] -->
However, some of the valuable information in reviews is not fully utilized in the introduced works, such as varying text lengths of different reviews and the sentiment intensity of speciﬁc 关注数学模型 words (e.g. "ﬁne" is less positively intense compared with "good"). Moreover, other impor- tant attributes in modern E-commerce recommendation systems, such as helpfulness ratings, reviewers’ credibility and whether or not reviewers are veriﬁed buyers, are rarely taken into account. The quantiﬁcation of reviews and ratings’ combinations are not yet proposed, and data measures based on reivews and ratings are not provided either.

<!-- b000148 | furniture | pages [3] -->
2

<!-- b000149 | furniture | pages [3] -->
MATHmodels

<!-- b000150 | furniture | pages [3] -->
获取更多资讯

<!-- b000151 | furniture | pages [4] -->
Team # 2004647

<!-- b000152 | furniture | pages [4] -->
Page 3 of 24

<!-- b000154 | heading | pages [4] -->
1.3 Data Cleaning

<!-- b000155 | prose | pages [4] -->
Upon observation on the provided data, we notice there are some misplaced data in each data set, where some review items belong to products of wrong categories. For example, in the ﬁle hair_dryer.tsv the review item with the product_parent value #466871293 (which uniquely identiﬁes a product) belongs to a hair spray product, instead of a hair dryer. Similarly, in the ﬁle microwave.tsv the review item with the product_parent value #311592014 belongs to a fridge, instead of a microwave. We ﬁnd these mistakes almost exclusively happen to those products with single digit review records. Along with the perception that sparse data do not contribute to our modeling well, we omit all product items with single digit review records.

<!-- b000156 | heading | pages [4] -->
1.4 Modeling Framework

<!-- b000157 | prose | pages [4] -->
Our modeling framework can be illustrated as shown in Figure 1.

<!-- b000158 | caption | pages [4] -->
Figure 1: Modeling Framework

<!-- b000159 | heading | pages [4] -->
2 Assumptions & Nomenclature

<!-- b000160 | prose | pages [4] -->
To simplify our modeling, we make the following assumptions:

<!-- b000161 | prose | pages [4, 5] -->
关注数学模型 Asm. 1 Provided data do not include spam reviews, either from competitors or mischievous customers.

<!-- b000162 | furniture | pages [4] -->
2

<!-- b000163 | furniture | pages [4] -->
MATHmodels

<!-- b000164 | furniture | pages [4] -->
获取更多资讯

<!-- b000165 | furniture | pages [5] -->
Team # 2004647

<!-- b000166 | furniture | pages [5] -->
Page 4 of 24

<!-- b000168 | prose | pages [5] -->
Asm. 2 Contents of every review are legitimate and unbiased.

<!-- b000169 | prose | pages [5] -->
Asm. 3 The number of review records of a product equals to the sales of the same product aggregated since it was launched, i.e., there are no missed or excluded records in any of the provided data sets.

<!-- b000170 | prose | pages [5] -->
Asm. 4 Customers’ reviews and ratings were posted the same day they purchased the prod- ucts, i.e., the time consumption of procedures such as packaging, delivery and users’ conﬁrmation of quality is neglected.

<!-- b000171 | prose | pages [5] -->
Asm. 5 Each customer has at most one review and rating record on one type of product (either a microwave, a paciﬁer or a hair dryer).

<!-- b000172 | prose | pages [5] -->
We have a list of the main notations we deﬁne during our modeling, as shown in Table 1.

<!-- b000173 | prose | pages [5] -->
3 the RRBS Model

<!-- b000174 | prose | pages [5] -->
In this section, we propose the RRBS Model (viz., the Rating and Review Based Score Model) to serve as a data measure, combining star ratings and textual information from reviews. When determining the quantiﬁcation process, we take into account nearly all inﬂuencing attributes from the provided data. As a result, a highly informative data measure is presented for Sun- shine Company to track, once their three new products are launched.

<!-- b000175 | caption | pages [5] -->
Table 1: Notations we use in future discussion.

<!-- b000176 | heading | pages [5] -->
Symbol

<!-- b000177 | prose | pages [5] -->
Description i Product type (either Microwaves, Paciﬁers or Hair dryers), i = 1, 2, 3 k Unique model identiﬁer of a type of products t Timestamp identiﬁer (unit: Month) n Number of rating and review records of a model within a speciﬁc month score(t) Measure for customer responses a product model receives i,k α Rating vector—an n-dimensional row vector β Review vector—an n-dimensional column vector λ Rating weight parameter A Sentiment polarity matrix—an n-by-n diagonal matrix Φ Review-quantifying vector—an n-dimensional column vector θj Vine factor sj Sentiment intensity factor vj Validity factor hj Helpfulness-rating factor Lj Review-length factor ϵj Correction term score Time series of a model’s scores Rep(t) Quantiﬁed reputation i,k

<!-- b000178 | prose | pages [5] -->
关注数学模型

<!-- b000179 | furniture | pages [5] -->
2

<!-- b000180 | furniture | pages [5] -->
MATHmodels

<!-- b000181 | furniture | pages [5] -->
获取更多资讯

<!-- b000182 | furniture | pages [6] -->
Team # 2004647

<!-- b000183 | furniture | pages [6] -->
Page 5 of 24

<!-- b000184 | heading | pages [6] -->
3.1 Model Overview

<!-- b000185 | prose | pages [6] -->
As part of our metric, we deﬁne score as a measure for a company’s particular product, based on the ratings and reviews it receives. It quantitatively indicates whether a product does well or badly in terms of receiving positive responses from customers. We deﬁne our metric as:

<!-- b000186 | prose | pages [6] -->
score(t) i,k = α◦λβ (1)

<!-- b000187 | prose | pages [6] -->
where:

<!-- b000188 | prose | pages [6] -->
• i ∈{1, 2, 3} denotes products of the ith type;

<!-- b000189 | prose | pages [6] -->
• k denotes the kth model (uniquely identiﬁed by the "product_parent" value) of the ith- type products;

<!-- b000190 | prose | pages [6] -->
• t denotes the tth month;

<!-- b000191 | prose | pages [6] -->
• α is an n-dimensional row vector whose value is determined by star ratings;

<!-- b000192 | prose | pages [6] -->
• β is an n-dimensional column vector whose value is determining by reviews and other inﬂuencing factors;

<!-- b000193 | prose | pages [6] -->
• λ is an impact factor that decides the weight of ratings in terms of impacting the score value. We initially set its value as 1.

<!-- b000194 | heading | pages [6] -->
3.2 Deﬁnition of α—the Rating Vector

<!-- b000195 | prose | pages [6] -->
The value of α is directly connected to a product’s star ratings, which vary from 1 to 5. And the value of 1 indicates "very unsatisﬁed" while the value of 5 indicating "very satisﬁed". We consider two star ratings, one with a value of 1 and the other one with a value of 5, have the same degree of intensity (i.e., one indicates "very" unsatisﬁed and the other one indicated "very" satisﬁed). Similarly, a 4-star rating is considerd having the same degree of intensity as a 2-star rating’s. And a 3-star rating represents a neutral stance, which we consider relatively less intense. Therefore, we conduct a mapping process, as shown in Table 2, so as to quantify the degree of both positivity and negativity of a star rating with a uniform measure.

<!-- b000196 | caption | pages [6] -->
Table 2: Mapping from star rating values to their corresponding mapped rating values (viz.,

<!-- b000197 | prose | pages [6] -->
degree of intensity).

<!-- b000198 | prose | pages [6] -->
Star Rating Mapped Rating

<!-- b000199 | prose | pages [6] -->
1-star & 5-star 3 2-star & 4-star 2 3-star 1

<!-- b000200 | prose | pages [6] -->
As stated above, α is an n-dimensional row vector that is exclusively associated with star ratings. The n non-zero elements in α represent n mapped rating values of a product within a month. We can obtain:

<!-- b000201 | prose | pages [6] -->
( ) α(t) α(t) α(t) α(t) α = . . . . . . (2) i,k,1 i,k,2 i,k,j i,k,n

<!-- b000202 | prose | pages [6] -->
where α(t) i,k,j ∈{1, 2, 3}. 关注数学模型

<!-- b000203 | furniture | pages [6] -->
2

<!-- b000204 | furniture | pages [6] -->
MATHmodels

<!-- b000205 | furniture | pages [6] -->
获取更多资讯

<!-- b000206 | furniture | pages [7] -->
Team # 2004647

<!-- b000207 | furniture | pages [7] -->
Page 6 of 24

<!-- b000208 | heading | pages [7] -->
3.3 Deﬁnition of β—the Review Vector

<!-- b000209 | prose | pages [7] -->
β is an n-dimensional column vector whose value is strongly associated with reviews and some other inﬂuencing factors. It comprehensively takes into account of the sentiment inten- sity of review text, varying lengths of different reviews, helpfulness ratings, the authority of reviewers (i.e., whether or not he/she is an Amazon Vine Reviewer 1) and whether or not the reviewers are veriﬁed buyers. Therefore, it is made possible to fully exploit the information within the provided data and effectively integrate textual reviews and other non-numerical inﬂuencing factors into our data measure.

<!-- b000210 | prose | pages [7] -->
We deﬁne it as:

<!-- b000211 | prose | pages [7] -->
( ) β(t) β(t) β(t) β(t) β = AΦ = . . . . . . (3) i,k,1 i,k,2 i,k,j i,k,n

<!-- b000212 | prose | pages [7] -->
where:

<!-- b000213 | prose | pages [7] -->
• A is an n-by-n diagonal matrix used to describe the sentiment polarity of reviews;

<!-- b000214 | prose | pages [7] -->
• Φ is an n-dimensional column vector used to quantify the semantic information and other inﬂuencing attributes of reviews.

<!-- b000215 | prose | pages [7] -->
Deﬁnition of Φ—the Review-quantifying Vector

<!-- b000216 | prose | pages [7] -->
To quantify the semantic information and other inﬂuencing attributes of reviews, we deﬁne Φ as an n-dimensional column vector, as is shown in Equation (4):

<!-- b000217 | prose | pages [7] -->
( )T ϕ(t) ϕ(t) ϕ(t) ϕ(t) Φ = . . . . . . (4) i,k,1 i,k,2 i,k,j i,k,n

<!-- b000218 | prose | pages [7] -->
where ϕ(t) i,k,j is the measure for semantic information, along with other inﬂuencing attributes, of a textual review, which is from the jth order of the kth model of the ith-type products.

<!-- b000219 | prose | pages [7] -->
We deﬁne this measure as:

<!-- b000220 | prose | pages [7] -->
vj ϕ(t) i,k,j = θj · s j · hj · Lj (5)

<!-- b000221 | prose | pages [7] -->
Deﬁnition of θj—the Vine Factor

<!-- b000222 | prose | pages [7] -->
According to Amazon.com [1], the most trusted reviewers identiﬁed by Amazon.com are invited to Amazon’s Vine Program, where they can post opinions about new and pre-release items to help their fellow customers make informed purchase decisions.

<!-- b000223 | prose | pages [7] -->
While Vine reviewers make independent opinions on offered products, the vendor can- not inﬂuence, modify or edit the reviews. Therefore, we have reason to believe that a review posted by Vine reviewers is more professional and trustworthy than regular reviews. Accord- ingly, we make our measure value contents of a review more when it is a Vine review, by deﬁning θj as:

<!-- b000224 | prose | pages [7] -->
{ 2, if the review is made by a Vine reviewer θj = (6) 1, otherwise

<!-- b000225 | prose | pages [7, 8] -->
1An Amazon Vine Reviewer is an member or Amazon’s Vine Program, who is invited to receive products for free in exchange for impartial reviews. 关注数学模型 Deﬁnition of sj—the Sentiment Intensity Factor

<!-- b000226 | furniture | pages [7] -->
2

<!-- b000227 | furniture | pages [7] -->
MATHmodels

<!-- b000228 | furniture | pages [7] -->
获取更多资讯

<!-- b000229 | furniture | pages [8] -->
Team # 2004647

<!-- b000230 | furniture | pages [8] -->
Page 7 of 24

<!-- b000232 | prose | pages [8] -->
Most of the time, when people post reviews about products they have purchased, they tend to include speciﬁc words that express some explicit sentiments and attitudes. It is also noticing that the sentiment intensities of reviewers’ chosen words vary. For example, "good" expresses a higher intensity of positiveness than "ﬁne" does. That is to say, we are able to quantify different sentiment intensities of different words, and thus the message a review is trying to express is made gradable when measuring semantic information.

<!-- b000233 | prose | pages [8] -->
With this mindset, we attempt to ﬁnd an existing data set that contains a decent amount of common adjectives, (most importantly) each one of which has a grade that indicates its sentiment intensity. Fortunately—thanks to the great open-source community—we are able to acquire a Python library called Aﬁnn [6] that consists of 2,477 graded-words, which fulﬁlls our exact requirements. We then use this word set to match contents of all the reviews in the provided data, ﬁltering out words that do not appear in any of the reviews (which we do not need).

<!-- b000234 | prose | pages [8] -->
As a result, we obtain a graded-word table (part of which is shown in Table 3) that cate- gorizes both positive and negative words into 3 groups of different grades (with 3 being the highest and 1 being the lowest).

<!-- b000235 | caption | pages [8] -->
Table 3: A fraction of the graded-word table acquired by matching the Aﬁnn word set with

<!-- b000236 | prose | pages [8] -->
contents of all reviews. Some of the most frequently-appeared graded-words are listed in this table. Note: We modify a few words’ grades with our own understanding of their sentiment intensities. Grade Positive Negative

<!-- b000237 | prose | pages [8] -->
outstanding, thrilled, awesome, wonderful, 3 catastrophic, horrible, dead, ridiculous, fantastic, fabulous, brilliant, terriﬁc awful, crappy, obnoxious, desperate

<!-- b000238 | prose | pages [8] -->
good, cute, powerful, comfortable, 2 clean, useful, satisﬁed, helpful

<!-- b000239 | prose | pages [8] -->
fair, ﬁne, easy, cool, 1 clear, safe, acceptible, capable bad, disappointed, wrong, useless, negative, poor, unhappy, annoying

<!-- b000240 | prose | pages [8] -->
strange, hard, difﬁcult, noisy, limited, silly, unsure, false

<!-- b000241 | prose | pages [8] -->
Hence, we can deﬁne sj as the sentiment intensity of the textual review contents of the jth order (of the kth model of the ith-type products). Its value is deﬁned as:

<!-- b000242 | prose | pages [8] -->
{ if matched words have a maximum grade of η η sj = 0, otherwise

<!-- b000243 | prose | pages [8] -->
Deﬁnition of vj—the Validity Factor (7)

<!-- b000244 | prose | pages [8] -->
Intuitively, if a review is not posted by a veriﬁed buyer, the validity of it is somewhat du- bious. Therefore, considering the potential inauthenticity of reviews from unveriﬁed buyers, we reduce the weights of such reviews in our measure. We deﬁne vj to represent a review’s validity, when it is low, the corresponding review has a less inﬂuence to our measure of the product’s score.

<!-- b000245 | prose | pages [8] -->
{ 1, if the reviewer is a veriﬁed buyer vj = 0.1, otherwise (8)

<!-- b000246 | prose | pages [8, 9] -->
关注数学模型 Deﬁnition of hj—the Helpfulness-rating Factor

<!-- b000247 | furniture | pages [8] -->
2

<!-- b000248 | furniture | pages [8] -->
MATHmodels

<!-- b000249 | furniture | pages [8] -->
获取更多资讯

<!-- b000250 | furniture | pages [9] -->
Team # 2004647

<!-- b000251 | furniture | pages [9] -->
Page 8 of 24

<!-- b000253 | prose | pages [9] -->
Undoubtedly, the helpfulness ratings of a review as an inﬂuence factor to our measure cannot be left out. Not only does it illustrate a review’s trustworthiness and overall quality, but also it exposes a review’s potential junk nature (being misleading or misconceived). This makes it easier to decide on a review should have whether more or less weights in our measure.

<!-- b000254 | prose | pages [9] -->
Therefore, we deﬁne hj as the helpfulness score in our measure, as shown in Equation (9). Its value should be 1 when nobody has yet voted its helpful, making it have the original weight in our measured in terms of helpfulness. If the "helpful" votes to total votes ratio is larger than 0.5, we consider this review a helpful review, thus should have a weight higher than 1; on the other hand, it is not helpful if the ratio is lower than 0.5 and should have a weight less than 1.

<!-- b000255 | prose | pages [9] -->
 helpful_votesj  −0.5,  e if total_votesj > 0  total_votesj hj = (9)    1, otherwise

<!-- b000256 | prose | pages [9] -->
where helpful_votesj is the number of "helpful" votes and total_votesj is the number of total votes on a review.

<!-- b000257 | prose | pages [9] -->
Deﬁnition of Lj—the Review-length Factor

<!-- b000258 | prose | pages [9] -->
Chua et al. [3] provided insight that a review’s helpfulness is positively related to its depth/length. Empirically, we know if a review is long to some degree, it is reasonable to assume it has more description on its target and the accuracy is more likely to be guaranteed.

<!-- b000259 | prose | pages [9] -->
Therefore, we can deﬁne Lj as a measure of a review’s helpfulness solely contributed by the review’s length. The more words a review contains, the more valuable we consider the review is. Yet it should be noted that the growth of Lj by review length should be non-linear and the growth rate should reduce as review length increases, otherwise it can affect our measure for products’ score too much. Hence, we deﬁne Lj as:

<!-- b000260 | prose | pages [9] -->
Lj = 1 2 log10 lenj (10)

<!-- b000261 | prose | pages [9] -->
where lenj is the literal number of words in the review of the jth order (of the kth model of the ith-type products).

<!-- b000262 | heading | pages [9] -->
3.3.1 The Review-based Measure Equation

<!-- b000263 | prose | pages [9] -->
By substituting Equation (6), (7), (8), (9) and (10) into Equation (5), we obtain:

<!-- b000264 | prose | pages [9] -->
helpful_votesj −0.5 · 1 vj ϕ(t) i,k,j = θj · s j · e 2 log10 lenj total_votesj (11)

<!-- b000265 | prose | pages [9] -->
This is the equation we deﬁne to measure semantic information and other inﬂuencing at- tributes of a textual review, taking into account of reviewers’ authority, reviews’ validity, re- views’ sentiment intensities, reviews’ helpfulness ratings and reviews’ textual lengths.

<!-- b000266 | prose | pages [9] -->
Note that the value of sj can be 0, for:

<!-- b000267 | prose | pages [9, 10] -->
• The wording of a review might be quite neutral and a clear sentiment (eith positive or negative) can not be inferred; 关注数学模型 • Some speciﬁc words within a review might suggest a sentiment and has some degree of intensity, but are not included in the graded-word set from Aﬁnn, making the evaluation of such reviews’ sentiment intensities infeasible.

<!-- b000268 | furniture | pages [9] -->
2

<!-- b000269 | furniture | pages [9] -->
MATHmodels

<!-- b000270 | furniture | pages [9] -->
获取更多资讯

<!-- b000271 | furniture | pages [10] -->
Team # 2004647

<!-- b000272 | furniture | pages [10] -->
Page 9 of 24

<!-- b000274 | prose | pages [10] -->
From equation (11) we know a review with a sj value of 0 also has the value of ϕ(t) i,k,j being 0, meaning the measure treats such a review as a "entirely-junk" review; this makes the multipli- cation of this review by its corresponding star rating result in a value of 0, meaning the rating loses its effect indirectly. This is not appropriate and we want to preserve our data measure ’s effect in this scenario. Therefore, we address this problem by introducing an correction term ϵj; its value is deﬁned as:

<!-- b000275 | prose | pages [10] -->
{ 1, if sj = 0 ϵj = (12) 0, otherwise

<!-- b000276 | prose | pages [10] -->
By adding this correction term to our measure (Equation (11)), we have:

<!-- b000277 | prose | pages [10] -->
helpful_votesj −0.5 · 1 vj ϕ(t) i,k,j = θj · s j · e 2 log10 lenj + ϵj total_votesj (13)

<!-- b000278 | prose | pages [10] -->
Now the value of ϕ(t) i,k,j will be 1 if the value of sj is 0, making the corresponding review have an initial weight; thus, from Equation (1) we know that the score which the review and its corresponding star rating collectively decide will solely depend on the star rating in this case.

<!-- b000279 | prose | pages [10] -->
By integrating nearly all useful information of reviews in a reasonable way, we can effec- tively measure reviews’ value , and thus can ﬁlter out poorly-written reviews with little value for paying attention to and retain valuable information from reviews which are worth listening to.

<!-- b000280 | prose | pages [10] -->
3.3.2 the Sentiment Polarity Matrix

<!-- b000281 | prose | pages [10] -->
A is an n-by-n diagonal matrix and is used to describe the sentiment polarity of reviews. We assign the value +1 to an element of A, if and only if the corresponding review (of the element) is measured as positive. Similarly, we assign the value −1 to the element if the corresponding review is measured as negative, as shown in Equation (14):

<!-- b000282 | prose | pages [10] -->
{ +1, if the corresponding review suggests a positive sentiment a(t) i,k,j = (14) −1, if the corresponding review suggests a negative sentiment

<!-- b000283 | prose | pages [10] -->
As for how to decide a review is whether positive or negative, we know that the Aﬁnn word set we use when matching reviews is comprised of graded-words with signs. For example, in the word set, the word "perfect" has a grade of +3 and the word "imperfect" has a grade of −2. Therefore, after a matching process of sentiment words and review contents, we extract the sign of the result and examine it. If it is a positive sign, we think of the review as positive; similarly, if is a negative sign, we consider the review negative.

<!-- b000284 | prose | pages [10] -->
For A, we have:

<!-- b000285 | prose | pages [10, 11] -->
A = diag(a(t) i,k,1, a(t) i,k,2, . . . , a(t) i,k,j, . . . , a(t) i,k,n) (15) 关注数学模型 We also take into account of the possibility that some reviews may contain words like "not" that invert the meaning of their next words. To assess the inﬂuence of such cases, we conduct statistics analysis. If the frequency of appearance of "negative-adjective" combinations (e.g., "not good") is low enough to be neglected, then we can be convinced this possibility has little effect on our results, if not addressed. As shown in Table 4, the percentage of such words’ appearance is 1166/101435 = 1.15%; thus, it is reasonable to ignore them.

<!-- b000286 | furniture | pages [10] -->
2

<!-- b000287 | furniture | pages [10] -->
MATHmodels

<!-- b000288 | furniture | pages [10] -->
获取更多资讯

<!-- b000289 | furniture | pages [11] -->
Team # 2004647

<!-- b000290 | furniture | pages [11] -->
Page 10 of 24

<!-- b000292 | prose | pages [11] -->
4 the Reputation Model

<!-- b000293 | prose | pages [11] -->
In Section 3.1, we deﬁne score to measure the positiveness/negativeness of customers’s overall responses for a product, based on the ratings and reviews it receives. On the grounds of this, in this section, we further introduce a time-based indicator—reputation—which intuitively de- scribes a product’s accumulated reputation over time periods. Accordingly, we build our Rep- utation Model to quantify a product’s time-based reputation, based on the measure provided by the RRBS Model (Section 3).

<!-- b000294 | heading | pages [11] -->
4.1 Time Weight Sequence

<!-- b000295 | prose | pages [11] -->
Intuitively, a reputation at a certain time is somewhat dependent to its previous reputation, instead of abruptly changes regardless of its states in the past or future. Generally, a prod- uct’s reputation at a certain time is closely connected to its reputations throughout its lifespan. With this mindset, we deﬁne the concept of Time Weight Sequence to describe the inﬂuences of previous reputations in a reputation at time t, denoted by a t-dimensional row vector γ:

<!-- b000296 | prose | pages [11] -->
( ) γ1 γ2 . . . γm . . . γt γ = (16)

<!-- b000297 | prose | pages [11] -->
where γm is the inﬂuence weight of a score in the mth month (with the 1st month being the ﬁrst month when a product is launched). We consider a reputation of a product in the mth month is more prone to be affected by the previous reputation in the (m −1)th month than the one in the (m −2)th month. We assume the growth of γm by time is exponential and perform normalization on this basis; thus, we obtain:

<!-- b000298 | prose | pages [11] -->
γj = aj at , a > 1 (17)

<!-- b000299 | prose | pages [11] -->
where a is a constant whose value is set as 1.1.

<!-- b000300 | caption | pages [11] -->
Table 4: Appearance counts of common adjectives (like "good") and "neg-adj" combinations

<!-- b000301 | prose | pages [11] -->
(like "not good") within all of the reviews. Adjectives are distinguished by an open-source Python word-processing library [2] and appearance is counted using Excel.

<!-- b000302 | prose | pages [11] -->
Common Adjective Count "Neg-adj" Combo. Count

<!-- b000303 | prose | pages [11] -->
great 4466 not sure 148 good 3055 not heavy 40 little 2963 not worth 34 ... ... ... ...

<!-- b000304 | prose | pages [11] -->
Total 101435 1166

<!-- b000305 | prose | pages [11] -->
关注数学模型

<!-- b000306 | furniture | pages [11] -->
2

<!-- b000307 | furniture | pages [11] -->
MATHmodels

<!-- b000308 | furniture | pages [11] -->
获取更多资讯

<!-- b000309 | furniture | pages [12] -->
Team # 2004647

<!-- b000310 | furniture | pages [12] -->
Page 11 of 24

<!-- b000311 | heading | pages [12] -->
4.2 Quantiﬁcation of Reputation

<!-- b000312 | prose | pages [12] -->
Firstly, based on Equation (1) we deﬁne a t-dimensional column vector denoted by score, to represent a product’s t months of scores:

<!-- b000313 | prose | pages [12] -->
( )T score(1) score(2) score(m) score(t) score = . . . . . . (18) i,k i,k i,k i,k

<!-- b000314 | prose | pages [12] -->
where score(m) i,k is the score of the kth model of ith-type products in the mth month.

<!-- b000315 | prose | pages [12] -->
We then deﬁne the quantiﬁcation of reputation as Rep(t) i,k, as shown in Equation (19)

<!-- b000316 | prose | pages [12] -->
Rep(t) i,k = γ · score (19)

<!-- b000317 | prose | pages [12] -->
where i denotes the type of a product model; k denotes the kth model of ith-type products; t denotes the tth month (since the product is launched).

<!-- b000318 | prose | pages [12] -->
From Equation (17) we know the Time Weight Sequence γ follows a monotonically increas- ing exponential pattern, which means a product’s score from a recent month impacts more on the new reputation than a score from a distant month does. Therefore, with the quantiﬁcation of products’ reputations, we should be able to address the task of observing and predicting products’ reputational increase or decrease in the online marketplace.

<!-- b000319 | heading | pages [12] -->
4.3 Model Evaluation

<!-- b000320 | prose | pages [12] -->
Based on empirical knowledge, a product with a good reputation (viz., the opinion customers have about how good it is) can induce more sales than one with a poorer reputation does. On the grounds of this, it is rational to say that a growth in a product’s reputation can stimulate a porportional amount of sales increase, and on the other hand, when a product’s reputation suffers, a decrease in sales is likely to happen.

<!-- b000321 | prose | pages [12] -->
With that being said, we can address the task of evaluating our models and measures’ correctness—which is tricky because the term reputation is quite abstract and there are no statistics of it for us to refer to—by comparing the trend of our quantiﬁed reputation to the trend of a product’s actual sales (derived from the rating and review records). Hence, after we quantify a product’s reputation with our measure, we can perform a comparison between the quantiﬁed reputation’s trend and the actual sales trend; thus the correctness of our models and measures are evaluated.

<!-- b000322 | heading | pages [12] -->
4.3.1 Trend Similarity between Quantiﬁed Reputation and Sales

<!-- b000323 | prose | pages [12] -->
We select 3 best-selling models from each of the 3 types of products to present and compare the trend of their reputation and their sales. Then, for each product model, we obtain a time series2 of quantiﬁed reputations and a time series of sales, and respectively present them in a scatter plot with points roughly connected to reveal trends. The result for each product model is shown in Figure 2. Next, for more comprehensiveness, we also select 1 rather poor-selling model from each type of products and perform the same operation, with results shown in

<!-- b000324 | caption | pages [12] -->
Figure 3.

<!-- b000325 | prose | pages [12] -->
With results in both ﬁgures, we can see trends of our quantiﬁed reputation and actual sales

<!-- b000326 | prose | pages [12, 13] -->
2A time series is a series of data points indexed (or listed or graphed) in time order. 关注数学模型 are very similar and might be highly correlated. To further prove this idea, we then conduct a correlation analysis.

<!-- b000327 | furniture | pages [12] -->
2

<!-- b000328 | furniture | pages [12] -->
MATHmodels

<!-- b000329 | furniture | pages [12] -->
获取更多资讯

<!-- b000330 | furniture | pages [13] -->
Team # 2004647

<!-- b000331 | furniture | pages [13] -->
Page 12 of 24

<!-- b000333 | caption | pages [13] -->
Figure 2: Visualization trends of reputation and sales of 3 best-selling models from each of the

<!-- b000334 | prose | pages [13] -->
3 types of products.

<!-- b000335 | caption | pages [13] -->
Figure 3: Visualization trends of reputation and sales of 1 rather poor-selling model from each

<!-- b000336 | prose | pages [13] -->
of the 3 types of products.

<!-- b000337 | heading | pages [13] -->
4.3.2 Kendall’s Tau Method

<!-- b000338 | prose | pages [13] -->
To evaluate the trend similarity between reputation and sales, we adopt Kendall’s Tau Method [9] to study the correlation between trends of reputation and trends of sales.

<!-- b000339 | prose | pages [13] -->
The procedure of Kendall’s Tau Method is as follows: suppose {x1, · · · , xi, · · · , xT} and { y1, · · · , yi, · · · , yT} are two randomly generated time series where i = 1, 2, · · · , T, we per- form sorting operation on both series respectively by the values of xi and yi. Then, we ob- tain two sorted time series—say, {x(1), x(2), · · · , x(T)} (termed the order statistics of the time series {x1, · · · , xi, · · · , xT}) and {y(1), y(2), · · · , y(T)} (termed the order statistics of the time series {y1, · · · , yi, · · · , yT}) —where x(1) ≤x(2) ≤· · · ≤x(T) and y(1) ≤y(2) ≤· · · ≤y(T).

<!-- b000340 | prose | pages [13, 14] -->
Take xj from the sorted series {x(1), x(2), · · · , x(T)} and suppose it is at its kth position, the number of 1 ≤k ≤T is termed the rank of xj and is denoted by pj. Similarly, from the sorted series {y(1), y(2), · · · , y(T)} we acquire the rank of yj denoted by qj. Let (xi, yi) and (xj, yj) with 关注数学模型 i = 1, · · · , T and j = i + 1, · · · , T be two data-pairs from the original time series. If (pj − pi)(qj −qi) > 0, we say the two data-pairs are concordant; otherwise, we say they are discordant. Let P denote the number of concordant pairs and Q denote the number of discordant pairs, it follows that P + Q = N(N −1)/2, and Kendall’s tau can be deﬁned as:

<!-- b000341 | furniture | pages [13] -->
2

<!-- b000342 | furniture | pages [13] -->
MATHmodels

<!-- b000343 | furniture | pages [13] -->
获取更多资讯

<!-- b000344 | furniture | pages [14] -->
Team # 2004647

<!-- b000345 | furniture | pages [14] -->
Page 13 of 24

<!-- b000347 | prose | pages [14] -->
τK(X, Y ) ≜P −Q P −Q P + Q = (20) N(N −1)/2

<!-- b000348 | prose | pages [14] -->
Hence, we know when two time series {x1, · · · , xi, · · · , xT} and { y1, · · · , yi, · · · , yT} have the exact same trend, then we have τK(X, Y ) →1; when the two series have the exact opposite trend, we have τK(X, Y ) →−1; and when the two series are not correlated at all, we have τK(X, Y ) →0. That is to say, |τK(X, Y )| ≈1 suggests trends of the two series are highly correlated while |τK(X, Y )| ≈0 suggests they are not correlated at all.

<!-- b000349 | prose | pages [14] -->
By adopting this method, with time series {x1, · · · , xi, · · · , xT} being the quantiﬁed reputa- tions and { y1, · · · , yi, · · · , yT} being the sales, we obtain results (shown in Figure 4) that suggest a high correlation between trends of reputation and sales: most of the calculated correlations are over 0.6, which is considered storng. The correlations calculated in the paciﬁer group are close to 0.8, which also indicates that a paciﬁer’s reputation is most correlated with its sales.

<!-- b000350 | caption | pages [14] -->
Figure 4: Calculated correlations of different models sperated into 3 groups by product types.

<!-- b000351 | prose | pages [14] -->
Each group contains correlations of 5 models, with top1 meaning the best-selling model in this group, top2 meaning the second-best-selling one and the ramaining 3 denoted the same way.

<!-- b000352 | prose | pages [14] -->
5 the Successfulness Prediction Model

<!-- b000353 | prose | pages [14] -->
Based on economic knowledge, a product’s success can be well quantiﬁed by its number of sales/orders over time. The more sales a product reaches, the greater the superiority it has in the marketplace, for it can gain ﬁne proﬁts to make room for possible enhancement (which costs money).

<!-- b000354 | prose | pages [14, 15] -->
In Section 4.3.1 we learn that a product’s sales trend is highly correlated with its reputation trend. Combining the knowledge we have, if a product’s reputation increases, then its sales are likely to increase within a similar degree, and thus we can suppose that this product is likely to succeed; on the other hand, a product’s reputational decrease might suggest its potential failure. Besides, we notice that the sales we have are of some degree of votality; thus, if we 关注数学模型 regress a product’s successfulness against its sales to predict the product’s future success or failure, the predictions can be highly error-prone.

<!-- b000355 | furniture | pages [14] -->
2

<!-- b000356 | furniture | pages [14] -->
MATHmodels

<!-- b000357 | furniture | pages [14] -->
获取更多资讯

<!-- b000358 | furniture | pages [15] -->
Team # 2004647

<!-- b000359 | furniture | pages [15] -->
Page 14 of 24

<!-- b000361 | prose | pages [15] -->
The RRBS Model we build in Section 3 effectively combines star-rating levels and informa- tion within text-based reviews, while the Reputation Model introduced in Section 4 provides a time-based measure that well quantiﬁes a product’s reputation over time. Considering our previously presented models’ strong capability and the fact the reputation changes much less abruptly compared with sales, we realize that by substituting our reputation measure for ac- tual sales when predicting a product’s successfulness and by predicting the product’s future reputation based on calculated reputation series, might turn out to be a good approach.

<!-- b000362 | heading | pages [15] -->
5.1 Gaussian Process Regression

<!-- b000363 | prose | pages [15] -->
Gaussian Processes (GP) are a generic supervised learning method designed to solve regres- sion and probabilistic classiﬁcation problems, while inference of continuous values with a Gaussian process prior is known as Gaussian Process Regression (GPR) [7]. We recognize GPR has several attributes we ﬁnd handy, e.g., it works well on small datasets and has the ability to provide uncertainty measurements on the predictions.

<!-- b000364 | prose | pages [15] -->
Therefore, we adopt GPR to ﬁt a product’s reputation series, hence predicting the product’s reputation in the future (later than the latest labeled-date in the provided data), and ﬁnally making it possible to predict the product’s future successfulness.

<!-- b000365 | prose | pages [15] -->
We ﬁrst try estimating the reputation of the best-selling paciﬁer model (with the "par- ent_product" value #246038397). Its rating and review records are within a date range of Jan.2010 to Aug. 2015. We ﬁrst obtain a time series of its reputations calculated with our Reputation Model, then we ﬁt the time series (leaving out values of July and August, 2015) by adopting GPR, and make predictions on its reputation in July and August, 2015, with a conﬁ- dence interval of 95%. The result shows that such short-term predictions have a high reliability, as seen in Figure 5.

<!-- b000366 | prose | pages [15] -->
(a) (b)

<!-- b000367 | caption | pages [15] -->
Figure 5: Subﬁgure (a) is the result of conducted short-term predictions (predicting reputations

<!-- b000368 | prose | pages [15] -->
in a few months); subﬁgure (b) is the result of long-term predictions (predicting reputations in a few years).

<!-- b000369 | prose | pages [15, 16] -->
Upon observations we realize the possibility of overﬁtting, so we obtain a time series (with a trimmed date range of Jan. 2010 to Dec. 2014) of the same model’s reputation, and predict its reputation after Jan. 2014. As shown in Figure 5(b), some real data points fall beyond the 关注数学模型 conﬁdence interval, indicating errors of our predictions. After deep analysis, we come up with the conclusion that the errors occur because the calculation of reputations is with a weight sequence of time (Section 4.1), making distant reputations have less effect. Therefore, it might be somewhat inaccurate when predicting reputations in the distant future; and thus all existing records should be used when performing predictions.

<!-- b000370 | furniture | pages [15] -->
2

<!-- b000371 | furniture | pages [15] -->
MATHmodels

<!-- b000372 | furniture | pages [15] -->
获取更多资讯

<!-- b000373 | furniture | pages [16] -->
Team # 2004647

<!-- b000374 | furniture | pages [16] -->
Page 15 of 24

<!-- b000376 | heading | pages [16] -->
5.2 Reputation Mapping

<!-- b000377 | prose | pages [16] -->
Considering predicted reputations after Aug. 2015 may vary a lot in values, we might not effec- tively ﬁnd an interval of convergence, which makes it hard to evaluate a product’s successful- ness. Therefore, we seek to ﬁnd a mapping approach to map our non-converging reputation predictions so that mapped reputations ﬂuctuate within an distinct interval of convergence, while the reputation values before and after mapping should indicate the same trend. We adopt the following function as our mapping approach:

<!-- b000378 | prose | pages [16] -->
1 pi,k(t) = (21) ˆ Rep(t) 1 + e− i,k

<!-- b000379 | prose | pages [16] -->
ˆ Rep(t) where − i,k is the predicted reputation in the tth month. It can be seen that p(t) →1 if ˆ ˆ Rep(t) Rep(t) − i,k →+∞; while p(t) →0 if − i,k →−∞. Therefore, our mapped reputation p(t) has an interval of convergence, while also having the same trend as the original’s.

<!-- b000380 | heading | pages [16] -->
5.3 Successfulness Threshold

<!-- b000381 | prose | pages [16] -->
To decide a product is either successful or failed, we need to determine a threshold. At ﬁrst deﬁne our threshold as a constant and set its value at 0.5:

<!-- b000382 | prose | pages [16] -->
threshold(t) i,k = 0.5 (22)

<!-- b000383 | prose | pages [16] -->
When evaluating the future successfulness of a product, we ﬁrst obtain a time series of its reputations calculated by its rating and review records with our Reputation Model, next we run regression analysis on the obtained time series and predict the product’s future reputation, then we map the predicted reputation to pi,k(t), and ﬁnally, we decide a product will have success in the future if pi,k(t) ≥threshold(t) i,k and is doomed to failure if pi,k(t) < threshold(t) i,k.

<!-- b000384 | prose | pages [16] -->
Using our method stated above, we perform predictions on some models’ potential suc- cessfulness in the future. Some of the results are listed in Table 5.

<!-- b000385 | caption | pages [16] -->
Table 5: A fraction of product models’ successfulness predictions.

<!-- b000386 | prose | pages [16] -->
Prediction/Product type Hair dryers Microwaves Paciﬁers Will succeed #732252283, #47684938, #423421857, #109226352, #246038397, #392768822 #486774008, #328811288... #771401205, #943347999... #667171015, #343148814...

<!-- b000387 | prose | pages [16] -->
Doomed to failure #862140913, #932955324 #392967251, #565545704, #671647927 #945323010, #768062995... #618770050... #130912179, #181638405...

<!-- b000388 | prose | pages [16, 17] -->
However, because different models in a set of products vary much in terms of their launch date (decided by the date of their ﬁrst rating and review records), our successfulness predic- tions could be inaccurate if we set the threshold as a constant. Suppose a newly-designed 关注数学模型 microwave is launched near Aug. 2015 and has great business potential, yet since it is a young product and has a relatively low reputation at the beginning, it might be considered a failure in the future—which it is likely not—if we neglect the consideration of products’ age when eval- uating future successfulness. Accordingly, we modify our threshold for successfulness and make it a function of time, as shown in Equation (23):

<!-- b000389 | furniture | pages [16] -->
2

<!-- b000390 | furniture | pages [16] -->
MATHmodels

<!-- b000391 | furniture | pages [16] -->
获取更多资讯

<!-- b000392 | furniture | pages [17] -->
Team # 2004647

<!-- b000393 | furniture | pages [17] -->
Page 16 of 24

<!-- b000395 | prose | pages [17] -->
i,k = 0.5 −0.1e−1 threshold(t) 10 (t−τ) (23)

<!-- b000396 | prose | pages [17] -->
where τ < t denotes the τth is month when the product is launched.

<!-- b000397 | prose | pages [17] -->
After the modiﬁcation, we re-evaluate the same set of models above and obtain a slightly different result, where Hair dryer #945323010, #767062995 and Paciﬁer #130912179, #181638405 re-predicted as potentially successful in the future. By looking up their review and sales in the data sets, we ﬁnd these re-predictions reasonable, for they appear to seem promising statisti- cally. Therefore, our model is reliable when predicting a product’s future successfulness.

<!-- b000398 | heading | pages [17] -->
6 Results

<!-- b000399 | heading | pages [17] -->
6.1 Evaluation of Star Rating’s Incitement

<!-- b000400 | prose | pages [17] -->
When discovering whether or not speciﬁc star ratings incite more some type of reviews, we mainly consider two scenarios: When seeing a series of high ratings, do customers tend to write some type of reviews? And when seeing a series of low ratings, do customers tend to write some type of reviews?

<!-- b000401 | prose | pages [17] -->
We deﬁne a high rating as a star rating of either 4 or 5, and a low rating as a star rating of either 1 or 2. To better address this section’s task, we also categorize reviews into three differ- ent types, including positive reviews, neutral reviews and negativive reviews. As previously deﬁned in Section 3.3, similar to the process of review score calculation—yet this time we do not include the correction term ϵ —we consider a review with β(t) i,k,j > 0 as a positive review; a review with β(t) i,k,j < 0 is considered a negativive review; and a review with β(t) i,k,j = 0 is considered a neutral review.

<!-- b000402 | prose | pages [17] -->
In order to observe the particular type of reviews that customers post after seeing a series of high ratings, we can sort a set of reviews (which are of the same product model, identiﬁed by the "parent_product" attribute) by time order and then record the type of reviews that are posted right after several high ratings occur. To make our solution more lucid, we deﬁne the event that k ratings (either of the type "high" or "low") subsequently occur as the k-event. Thus, once a k-event of high ratings occurs, we can record the type of the very next review, and after repeating this process for a good amount of times—enough for frequency to indicate probability. By varying the value of k, we can infer whether customers would write some type of reviews after seeing different numbers of subsequent speciﬁc ratings.

<!-- b000403 | prose | pages [17] -->
We ﬁrst apply our method while only considering top-5 models that have the largest sales throughout their lifespan (derived from the numbers of their review and rating records) of all three types of products, to ﬁnd out some patterns. The selected models are listed in Table 6.

<!-- b000404 | prose | pages [17, 18] -->
We then iterate through their k-events (k = 2, 3, 4, 5) of both high ratings and low ratings, record the type of review right after every k-event; thus we can obtain frequency of the three types of reviews (following k-events). By performing weighted summation with models’ num- bers of orders being the weights, we can obtain the approximate probabilities of different types 关注数学模型 Product Type Top-5 Models with Largest Sales Hair Dryer #732252283, #758099411, #47684938, #235105995, #694290590 Microwave #423421857, #544821753, #109226352, #771401205, #827502283 Paciﬁer #246038397, #392768822, #572944212, #450475749, #812583172

<!-- b000405 | furniture | pages [17] -->
2

<!-- b000406 | furniture | pages [17] -->
MATHmodels

<!-- b000407 | furniture | pages [17] -->
获取更多资讯

<!-- b000408 | furniture | pages [18] -->
Team # 2004647

<!-- b000409 | furniture | pages [18] -->
Page 17 of 24

<!-- b000410 | caption | pages [18] -->
Table 6: Top-5 models with largest sales.

<!-- b000412 | prose | pages [18] -->
of reviews which customers might post after a k-event. Results are listed in Table 7 and Table 8.

<!-- b000413 | caption | pages [18] -->
Table 7: Estimated probabilities of three types of reviews’s apperance following after k-events

<!-- b000414 | prose | pages [18] -->
(k = 2, 3, 4, 5) of high ratings, respectively measured for each type of products. Note: P+ is the probability of a review being type "positive"; P0 is the probability of a review being type "neutral"; P−is the probability of a review being type "negative".

<!-- b000415 | prose | pages [18] -->
P+/P0/P− k = 2 k = 3 k = 4 k = 5 Hair Dryer 0.5875/0.2040/0.2085 0.5899/0.2022/0.2078 0.5721/0.2141/0.2137 0.5723/0.2142/0.2134 Microwave 0.4856/0.2981/0.2163 0.4710/0.3032/0.2258 0.5088/0.2982/0.1930 0.5301/0.2892/0.1807 Paciﬁer 0.5839/0.2579/0.1582 0.5753/0.2650/0.1597 0.5892/0.2593/0.1515 0.5891/0.2518/0.1591

<!-- b000416 | caption | pages [18] -->
Table 8: Estimated probabilities of three types of reviews’s apperance following after k-events

<!-- b000417 | prose | pages [18] -->
(k = 2, 3, 4, 5) of high ratings, respectively measured for each type of products.

<!-- b000418 | prose | pages [18] -->
P+/P0/P− k = 2 k = 3 k = 4 k = 5 Hairdryer 0.3040/0.1486/0.5472 0.3472/0.1736/0.4791 0.1666/0.1666/0.6665 0/0/1 microwave 0.3750/0.2083//0.4167 0.2500/0.2500/0.5000 0.5000/0/0.5000 0.5000/0/0.5000 paciﬁer 0.0714/0.6429/0.2857 0.4120/0.1675/0.4205 0.2675/0.3089/0.4236 0.1156/0.2320/0.6524

<!-- b000419 | prose | pages [18] -->
From Table 7 we can see three types of products share some similarities: when seeing a k-event of high ratings take place, customers of all types of products are mostly likely to post positive reviews, with an average probability of 55.23%. Therefore, we can draw a rough conclusion that customers are incited to write positive reviews after seeing a series of high ratings being posted.

<!-- b000420 | prose | pages [18] -->
However, in comparison, results in Table 8 do not look very ideal. For hair dryers, the probability of negative reviews following a series of low ratings is the largest among those of positive and neutral reviews, which is reasonable. Yet for microwaves, untrustworthy results appear when k = 4, 5, where probabilities of negative and positive reviews are equal.

<!-- b000421 | prose | pages [18] -->
In fact, we ﬁnd out the number of low ratings on top selling models is signiﬁcantly lower than the number of high ratings—which makes sense since they are best sellers. Therefore, it is rare for subsequent low ratings to appear, making our measure error-prone. To draw a ﬁner conclusion, instead of covering merely hot-selling models, we broaden our coverage to 95% of models among each type of products in our measure. Nevertheless, the frequency of more than 4 subsequent low ratings appearing is still rather low compared with that of high ratings. Hence, we are not able to assess low ratings’ incitement to customers’ negative reviews with conﬁdence.

<!-- b000422 | prose | pages [18] -->
To sum it up, we do ﬁnd high ratings incite more positive reviews; at the other end, we cannot determine whether low ratings’ incitement to negative reviews.

<!-- b000423 | prose | pages [18] -->
关注数学模型

<!-- b000424 | furniture | pages [18] -->
2

<!-- b000425 | furniture | pages [18] -->
MATHmodels

<!-- b000426 | furniture | pages [18] -->
获取更多资讯

<!-- b000427 | furniture | pages [19] -->
Team # 2004647

<!-- b000428 | furniture | pages [19] -->
Page 18 of 24

<!-- b000429 | heading | pages [19] -->
6.2 Association between Review Wording and Rating Levels

<!-- b000430 | prose | pages [19] -->
Empirically, we suppose when people are giving ratings based on their feelings—which can be inferred by their reviews—towards products, the rating levels are likely somewhat associated with the reviews’ contents.

<!-- b000431 | prose | pages [19] -->
To verify our theory, we calculate our graded-words’ appearance in all of the reviews, recording their (viz., the reviews the words appear in) different corresponding star-rating lev- els at the same time. Note that multiple apperances of a word within the same review is only counted once. On the grounds of this, we deﬁne a word’s star-rate as its particular rating level’s percentage of all the ratings it is connected to.

<!-- b000432 | prose | pages [19] -->
Particularly, we achieve a list of top-5 words with the largest 5-star-rates (Table 9). As shown in the results, all of the words are positive adjectives and 4 out of 5 have a grade of 3 (the highest intensity level), with every one of them having a 5-star-rate over 80%. On the other hand, we also achieve a list of top-5 words with the largest 1-star-rates (Table 10). And from the results, we can see all of the words are negative words and 3 out of 5 have a grade of 3, with every one of them having a 1-star-rate over 35% (which is still a high percentage for one star ratings—people usually do not rate that low).

<!-- b000433 | prose | pages [19] -->
Since a small sample size cannot prove it all, we then calculate the high star-rates (with a star rating over 3) of all the frequent words (words appear more than 50 times among all reviews). And our result show that 37.84% of the words have high star-rates over 80%; all of these words are positive words while 60.87% of them have the highest level of positivity intensity. At the other end, we also calculate the low star-rates (with a star rating below 3) of all the frequent words, and 10.29% of the words have low star-rates over 50%, all of which are negative words and 100% of them have a level of negativity intensity equal or more than 2. Such results reveal strong associations between sentiment words (which also serve as quality descriptors) and rating levels.

<!-- b000434 | caption | pages [19] -->
Table 9: Top-5 words with the largest 5-star-rates. For the full top-30 one, see Table 13 in

<!-- b000435 | prose | pages [19] -->
Appendices.

<!-- b000436 | prose | pages [19] -->
Word Count Grade 1-Star-Rate 2-Star-Rate 3-Star-Rate 4-Star-Rate 5-Star-Rate 3 0.8696 awesome 92 0.0435 0.0109 0.0435 0.0326 3 0.8623 wonderful 138 0.0072 0.0145 0.0290 0.0870 3 0.8462 love 52 0.0192 0.0192 0.0192 0.0962 3 0.8299 adorable 241 0.0166 0.0249 0.0332 0.0954 2 0.8295 favorite 258 0.0078 0.0271 0.0271 0.1085

<!-- b000437 | caption | pages [19] -->
Table 10: Top-5 words with the largest 1-star-rates. For the full top-20 one, see Table 14 in

<!-- b000438 | prose | pages [19] -->
Appendices.

<!-- b000439 | prose | pages [19] -->
Word Count Grade 1-Star-Rate 2-Star-Rate 3-Star-Rate 4-Star-Rate 5-Star-Rate 3 0.6346 dangerous 52 0.0962 0.0769 0.0385 0.1538 3 0.5000 terrible 54 0.1111 0.0741 0.1481 0.1667 2 0.4255 poor 94 0.2447 0.1383 0.0638 0.1277 2 0.3622 disappointed 196 0.2245 0.1837 0.0867 0.1429 3 0.3607 horrible 61 0.1639 0.1475 0.1148 0.2131

<!-- b000440 | prose | pages [19] -->
关注数学模型

<!-- b000441 | furniture | pages [19] -->
2

<!-- b000442 | furniture | pages [19] -->
MATHmodels

<!-- b000443 | furniture | pages [19] -->
获取更多资讯

<!-- b000444 | furniture | pages [20] -->
Team # 2004647

<!-- b000445 | furniture | pages [20] -->
Page 19 of 24

<!-- b000446 | heading | pages [20] -->
6.3 Our Strategies

<!-- b000447 | prose | pages [20] -->
For Sunshine Company to improve their competition in the marketplace, we fully utilize our knowledge gained with our models, and come up with some marketing strategies and possibly important design features they can adopt.

<!-- b000448 | heading | pages [20] -->
6.3.1 Marketing Strategies

<!-- b000449 | prose | pages [20] -->
We notice the potential intensity of competition that comes along with entrance into different speciﬁc markets may vary, due to customers’ different established preference towards partic- ular products within a speciﬁc market. For example, if a large fraction of customers are loyal customers to—hypothetically speaking —Moonlight Company’s paciﬁers, it can be hard for Sunshine Company to induce those customers into buying their paciﬁers.

<!-- b000450 | prose | pages [20] -->
To measure this "preference" that customers have, we can utilize our reputation measure. We can perform weighted average of all product models’ reputations, which are weighted by the products’ sales. Then, by the scale of the results, we can tell if some strong loyalty in a market is established. Using this method, we obtain Table 11. As it can be seen, the paciﬁer market has the strongest loyalty while the microwaves has the weakest. That is to say, it takes the most effort to compete in the paciﬁer market.

<!-- b000451 | prose | pages [20] -->
Accordingly, we propose following marketing strategies:

<!-- b000452 | prose | pages [20] -->
• If Sunshine Company has enough effort to spare, we suggest they put more effort in selling paciﬁers, e.g., allocating more of their advertising budget to their paciﬁer;

<!-- b000453 | prose | pages [20] -->
• If Sunshine Company does not have enough effort to spare (due to shorthanded-ness or limited budget), we suggest they put more of their limited effort in selling microwaves, for they can pursue superiority in at least one market;

<!-- b000454 | prose | pages [20] -->
• No matter what, Sunshine Company should constantly track our score and reputation measure of their products, for they can ﬁnely reﬂect customers’ opinion on the products.

<!-- b000455 | heading | pages [20] -->
6.3.2 Important Design Features

<!-- b000456 | prose | pages [20] -->
To identify what important features customers care most about, we calculate appearance of words among all reviews of each type of products. Some operations are carried out to extract quality descriptors that indicate design features:

<!-- b000457 | prose | pages [20] -->
1 Leave out words that are not nouns, for nouns describe what speciﬁc features customers need;

<!-- b000458 | prose | pages [20] -->
2 Leave out words that do not refer to speciﬁc qualites of products.

<!-- b000459 | caption | pages [20] -->
Table 11: Estimated competition intensity in three different markets.

<!-- b000460 | prose | pages [20] -->
Product type Reputation weight average 239.7633 Hair dryers 184.0208 Microwaves 305.3781 Paciﬁers

<!-- b000461 | prose | pages [20, 21] -->
关注数学模型 Then we obtain a table of top-3 most mentioned features of each type of products, as shown in Table 12, which represent the most important features that Sunshine Company should con- sider most when designing their products. From it we can suppose customers expect a reason- able price for all three types of products. While speciﬁcally:

<!-- b000462 | furniture | pages [20] -->
2

<!-- b000463 | furniture | pages [20] -->
MATHmodels

<!-- b000464 | furniture | pages [20] -->
获取更多资讯

<!-- b000465 | furniture | pages [21] -->
Team # 2004647

<!-- b000466 | furniture | pages [21] -->
Page 20 of 24

<!-- b000468 | prose | pages [21] -->
• Customers might want a hair dryer to be able to produce enough heat and to have a high-quality cord;

<!-- b000469 | prose | pages [21] -->
• Microwaves are expected to have a sufﬁcient space and customer service is also valued since machines can break down any second;

<!-- b000470 | prose | pages [21] -->
• Paciﬁers are for babies, reasonably parents expect them to have a good quality and ap- propriate size so that babies feel comfortable biting on it.

<!-- b000471 | caption | pages [21] -->
Table 12: Top-3 most mentioned features of each type of products.

<!-- b000472 | prose | pages [21] -->
Hair dryers Microwaves Paciﬁers price(1063) space(183) quality(405) Word(Count) heat(960) price(147) size(395) cord(805 service(137) price(333)

<!-- b000473 | heading | pages [21] -->
7 Sensitivity Analysis

<!-- b000474 | prose | pages [21] -->
We carry out sensitivity analysis on two main parameters: λ (Equation (1)) and a (Equation (17)). First, we change the value of a from −10% to +10%, each time a step of 5%. The results, as shown in Figure 6(a), show that the reputation trend only slightly vary roughly before the 38th month, but it becomes quite sensitive as the timestamp moves on. It is reasonable since the score in the RRBS Model is exponentially weighted and summed up to acquire the reputation. Therefore, a is a critical parameter that should be carefully determined. Then, similarly, we change the value of λ from −10% to +10%, and evaluate its sensitivity. As shown in Figure 6(b), it does not appear to be noticeably sensitive.

<!-- b000475 | prose | pages [21] -->
To sum it up, one of our two parameters—a—is tested out to be a sensitive parameter. But in general, our models have a fair degree of robustness.

<!-- b000476 | heading | pages [21] -->
8 Strengths and Weaknesses

<!-- b000477 | heading | pages [21] -->
8.1 Strengths

<!-- b000478 | prose | pages [21] -->
• Full utilization of information: When designing our measures, not only do we com- bine star ratings and review contents, but also we consider other useful attributes in the provided data;

<!-- b000479 | prose | pages [21] -->
• Great model performance: The high correlation between trends of our quantiﬁed reputa- tion and acutal sales suggests our models have great performance and that our measures are accurate;

<!-- b000480 | prose | pages [21, 22] -->
• Good choice of methodology: We reveal the strong connections between positive words and high ratings, negative and low ratings, thanks to our choice of methodology; 关注数学模型 (a) (b)

<!-- b000481 | furniture | pages [21] -->
2

<!-- b000482 | furniture | pages [21] -->
MATHmodels

<!-- b000483 | furniture | pages [21] -->
获取更多资讯

<!-- b000484 | furniture | pages [22] -->
Team # 2004647

<!-- b000485 | furniture | pages [22] -->
Page 21 of 24

<!-- b000487 | caption | pages [22] -->
Figure 6: Sensitivity analysis results of our two main parameters: λ and a.

<!-- b000488 | prose | pages [22] -->
• High robustness: In general, our models are not insensitive to value change of parame- ters.

<!-- b000489 | heading | pages [22] -->
8.2 Weaknesses

<!-- b000490 | prose | pages [22] -->
• Certain degree of arbitrariness in model designs: We adopt an arbitrary mindset when designing part of our models;

<!-- b000491 | prose | pages [22] -->
• Limitations of our acquired word set: The word set we use to match review contents in the RBSS Model lacks in size to some degree, leaving out some information when measuring products’ scores;

<!-- b000492 | heading | pages [22] -->
9 Conclusion

<!-- b000493 | prose | pages [22] -->
In our work, we propose the RRBS Model and the Reputation Model to provide a rating-based, review-based and time-based measure that ﬁnely describes a product’s reputation over time periods. Using this measure, we are able to predict a product’s potential success or failure in the future. We also ﬁnd out that a sequence of high ratings can incite more positive reviews, yet cannot determine whether sequences of low ratings have similar effects. A strong associ- ation between rating levels and speciﬁc quality descriptors of reviews is also found by word matching and appearance calculation. Finally, we provide Sunshine Company our devised marketing strategies and point out some design features of products they can work on to, so as to improve their overall competitiveness in the marketplace.

<!-- b000494 | prose | pages [22] -->
关注数学模型

<!-- b000495 | furniture | pages [22] -->
2

<!-- b000496 | furniture | pages [22] -->
MATHmodels

<!-- b000497 | furniture | pages [22] -->
获取更多资讯

<!-- b000498 | furniture | pages [23] -->
Team # 2004647

<!-- b000499 | furniture | pages [23] -->
Page 22 of 24

<!-- b000500 | heading | pages [23] -->
10 Our Letter

<!-- b000501 | prose | pages [23] -->
From: Team #2004647 To: Marketing Director of Sunshine Company Date: March 9, 2020

<!-- b000502 | prose | pages [23] -->
Dear Marketing Director of Sunshine Company,

<!-- b000503 | prose | pages [23] -->
Thank you for hiring us as your consultants! We are informed of your speciﬁed require- ments and have fully evaluated the feasibility of our tasks. Here we present to you with our detailed solutions.

<!-- b000504 | prose | pages [23] -->
We thoroughly examined the data of reviews and ratings associated with our competitors’ products. We discovered that a lot of the attributes of the data can be utilized, along with the actual rating levels and review contents, to ﬁgure out an fairly informative measure for you to track. To perform quantiﬁcation on them, we proposed the Rating and Review Based Score Model, which introduces our deﬁned data measure—score. In our model, a product’s score describes customers’ responses to the product. It is based on both ratings and text reviews. When calculating the score of a product, we take into account of:

<!-- b000505 | prose | pages [23] -->
• Its received rating levels;

<!-- b000506 | prose | pages [23] -->
• Whether its reviews are from Vine reviewers;

<!-- b000507 | prose | pages [23] -->
• The sentiment intensity of the review contents (as "fair" is less intense than "wonderful", with both being positive words);

<!-- b000508 | prose | pages [23] -->
• Whether its reviews are from veriﬁed buyers;

<!-- b000509 | prose | pages [23] -->
• The helpness-ratings of its reviews, which help ﬁltering out reviews that are already unhelpful to other customers;

<!-- b000510 | prose | pages [23] -->
• The lengths of its reviews.

<!-- b000511 | prose | pages [23] -->
By combining these factors altogether, our measure should be able to pick out the most valuable ones among all kinds of voices, which your company should attach great importance to once your products are launched—because they contain crucial information for you to know what problems your products have and how you can improve.

<!-- b000512 | prose | pages [23] -->
Based on our score measure, we further proposed the Reputation Model, which straight- forwardly deﬁnes the reputation of a product—which is a time-based measure for quantifying a product’s reputations among customers over time periods. The measure was proved to be fairly accurate in terms of describing a product’s actual (but abstract) reputation, supported by the strong correlation between trends of the quantiﬁed reputations and the product’s sales.

<!-- b000513 | prose | pages [23] -->
Empirical knowledge suggests the successfulness of a product is closely connected to its sales. Since we know our reputation measure is reliable and strongly correlated with the prod- uct’s sales, we can utilize it to indicate a product’s future successfulness. We approached this by adopting Gaussian Process Regression, and it turns out we can ﬁnely predict a product’s reputations in the near future based on time series of its calculated reputations. Therefore, we are able to predict a product’s potential success or failure in the future in the short term; though it lacks in accuracy when making long-term predictions.

<!-- b000514 | prose | pages [23, 24] -->
As for the speciﬁc questions you are concerned about, we seeked to ﬁnd out whether a se- ries of speciﬁc ratings can incite some type of reviews. By recording customers’ reviews right 关注数学模型 after a series of same ratings, by calculating the chance of them being either positive, nega- tive or neutral, we managed to ﬁnd out that a series of high ratings do incite more positive reviews—which indicates a signiﬁcant reputational increase. However, due to lack of evi- dence, we cannot determine for sure whether a series of low ratings incite negative reviews.

<!-- b000515 | furniture | pages [23] -->
2

<!-- b000516 | furniture | pages [23] -->
MATHmodels

<!-- b000517 | furniture | pages [23] -->
获取更多资讯

<!-- b000518 | furniture | pages [24] -->
Team # 2004647

<!-- b000519 | furniture | pages [24] -->
Page 23 of 24

<!-- b000521 | prose | pages [24] -->
To address the other question that whether speciﬁc quality descriptors are strongly associ- ated with rating levels, we ﬁrst obtained a word set of 2,477 words, all of which are graded by its sentiment intensity (say "wonderful" is more positively intense than "fair"). Then we match all of the review contents in the provided data and calculate words’ appearance and associated rating levels. The results reveal noticeably strong connections between them. For example, of all the reviews that contain the word "awesome" (which has a maximum of positiveness inten- sity), 86.96% of them are associated with a 5-star rating. On the other hand, of all the reviews that contain "dangerous" (which has a maximum of negativeness intensity), 63.46% of them are associated with a 1-star rating.

<!-- b000522 | prose | pages [24] -->
Finally, with our modeling and methodology, we have devised a set of marketing strategies you can adopt, and a set of design features for each product that customers value the most. We ﬁrst performed weighted average of all product models’ reputations in each market, which are weighted by the products’ sales, and thus we have a measure for the potential competition that your company will encounter, for average reputations in a market can indicate the market’s customer loyalty. The results reveal that it takes the most effort to compete in the paciﬁer market and the least in the microwave market. Therefore, we present following marketing strategies:

<!-- b000523 | prose | pages [24] -->
• If your company has enough effort to spare, we suggest you put more effort in selling paciﬁers, e.g., allocating more of your advertising budget to your paciﬁer;

<!-- b000524 | prose | pages [24] -->
• If your company does not have enough effort to spare (due to shorthanded-ness or lim- ited budget), we suggest you put more of your limited effort in selling microwaves, for you can pursue superiority in at least one market;

<!-- b000525 | prose | pages [24] -->
• No matter what, your company should constantly track our score and reputation measure of your products, for they can ﬁnely reﬂect customers’ opinion on the products.

<!-- b000526 | prose | pages [24] -->
Subsequently, we matched the reviews with quality specifying nouns and calculated their appearance. Then we picked 3 words with most appearance for each product, which indicate design features customers value the most. The results show that customers expect a reasonable price for all three types of products. While speciﬁcly:

<!-- b000527 | prose | pages [24] -->
• Customers might want a hair dryer to be able to produce enough heat and to have a high-quality cord;

<!-- b000528 | prose | pages [24] -->
• Microwaves are expected to have a sufﬁcient space and customer service is also valued since machines can break down any second;

<!-- b000529 | prose | pages [24] -->
• Paciﬁers are for babies, reasonably parents expect them to have a good quality and ap- propriate size so that babies feel comfortable biting on it.

<!-- b000530 | prose | pages [24] -->
If you want to know more details, please refer to our thesis. We will be glad to discuss with you on our solution details.

<!-- b000531 | prose | pages [24] -->
关注数学模型

<!-- b000532 | furniture | pages [24] -->
2

<!-- b000533 | furniture | pages [24] -->
MATHmodels

<!-- b000534 | furniture | pages [24] -->
获取更多资讯

<!-- b000535 | furniture | pages [25] -->
Team # 2004647

<!-- b000536 | furniture | pages [25] -->
Page 24 of 24

<!-- b000537 | heading | pages [25] -->
References

<!-- b000538 | references | pages [25] -->
[1] I. AMAZON.COM, What is amazon vine?, accessed March 7, 2020.

<!-- b000539 | references | pages [25] -->
[2] S. BIRD AND E. LOPER, NLTK: The natural language toolkit, in Proceedings of the ACL In-

<!-- b000540 | references | pages [25] -->
teractive Poster and Demonstration Sessions, Barcelona, Spain, July 2004, Association for

<!-- b000541 | references | pages [25] -->
Computational Linguistics, pp. 214–217.

<!-- b000542 | references | pages [25] -->
[3] A. CHUA AND S. BANERJEE, Understanding review helpfulness as a function of reviewer reputa-

<!-- b000543 | references | pages [25] -->
tion, review rating, and review depth, Journal of the Association for Information Science and

<!-- b000544 | references | pages [25] -->
Technology, 66 (2014).

<!-- b000545 | references | pages [25] -->
[4] Y. KOREN, R. BELL, AND C. VOLINSKY, Matrix factorization techniques for recommender sys-

<!-- b000546 | references | pages [25] -->
tems, Computer, 42 (2009), pp. 30–37.

<!-- b000547 | references | pages [25] -->
[5] J. MCAULEY AND J. LESKOVEC, Hidden factors and hidden topics: Understanding rating dimen-

<!-- b000548 | references | pages [25] -->
sions with review text, in Proceedings of the 7th ACM Conference on Recommender Systems,

<!-- b000549 | references | pages [25] -->
RecSys 13, New York, NY, USA, 2013, Association for Computing Machinery, p. 165172.

<!-- b000550 | references | pages [25] -->
[6] F. Å. NIELSEN, Aﬁnn, mar 2011.

<!-- b000551 | references | pages [25] -->
[7] C. E. RASMUSSEN AND C. K. I. WILLIAMS, Gaussian Processes for Machine Learning (Adap-

<!-- b000552 | references | pages [25] -->
tive Computation and Machine Learning), The MIT Press, 2005.

<!-- b000553 | references | pages [25] -->
[8] Y. TAN, M. ZHANG, Y. LIU, AND S. MA, Rating-boosted latent topics: Understanding users

<!-- b000554 | references | pages [25] -->
and items with ratings and reviews, in Proceedings of the Twenty-Fifth International Joint

<!-- b000555 | references | pages [25] -->
Conference on Artiﬁcial Intelligence, IJCAI16, AAAI Press, 2016, p. 26402646.

<!-- b000556 | references | pages [25] -->
[9] W. XU, C. CHANG, Y. S. HUNG, S. K. KWAN, AND P. C. W. FUNG, Order statistics corre-

<!-- b000557 | references | pages [25] -->
lation coefﬁcient as a novel association measurement with applications to biosignal analysis, IEEE

<!-- b000558 | references | pages [25] -->
Transactions on Signal Processing, 55 (2007), pp. 5552–5563.

<!-- b000559 | references | pages [25] -->
关注数学模型

<!-- b000560 | furniture | pages [25] -->
2

<!-- b000561 | furniture | pages [25] -->
MATHmodels

<!-- b000562 | furniture | pages [25] -->
获取更多资讯

<!-- b000563 | furniture | pages [26] -->
Team # 2004647

<!-- b000564 | references | pages [26] -->
Page 25

<!-- b000565 | heading | pages [26] -->
Appendices

<!-- b000566 | prose | pages [26] -->
aﬁnn-matcher.py

<!-- b000567 | prose | pages [26] -->
# This program is used to match reviews with graded-words provided by Afinn word set import csv import nltk import re from afinn import Afinn

<!-- b000568 | prose | pages [26] -->
def split(delimiters, string, maxsplit=0):

<!-- b000569 | prose | pages [26] -->
regexPattern = ’|’.join(map(re.escape, delimiters)) return re.split(regexPattern, string, maxsplit)

<!-- b000570 | prose | pages [26] -->
delims = ",.;?<>()! "

<!-- b000571 | prose | pages [26] -->
af = Afinn(language=’en’) adjs = {} files = ["pacifier.csv", "microwave.csv", "hair_dryer.csv"]

<!-- b000572 | prose | pages [26] -->
cnt = 0 for file in files:

<!-- b000573 | prose | pages [26] -->
with open(file, "r", encoding="utf-8", errors=’ignore’) as f:

<!-- b000574 | prose | pages [26] -->
reader = csv.DictReader(f) for line in reader:

<!-- b000575 | prose | pages [26] -->
cnt += 1 if cnt % 100 == 0:

<!-- b000576 | prose | pages [26] -->
print("Reading line " + str(cnt) + ", dict size=" + str(len(adjs))) review = line["review_headline"] + line["review_body"] toks = split(delims, review) toks = set(filter(None, toks)) # print(toks) words = nltk.pos_tag(toks) for i in range(len(words)):

<!-- b000577 | prose | pages [26] -->
tup = words[i] if tup[1] == "JJ":

<!-- b000578 | prose | pages [26] -->
word = tup[0] word = word.lower() score = af.score(word) if score == 0:

<!-- b000579 | prose | pages [26] -->
continue adjs[word] = [sum(x) for x in zip( adjs.get(word, [0] * 7), [1, 0, 0, 0, 0, 0, 0])] rating = int(line["star_rating"]) if rating > 5 or rating < 1:

<!-- b000580 | prose | pages [26] -->
continue adjs[word][rating] += 1 adjs[word][6] = score

<!-- b000581 | prose | pages [26] -->
out = "matched_words.csv"

<!-- b000582 | prose | pages [26] -->
with open(out, "w", encoding="utf-8") as f:

<!-- b000583 | prose | pages [26] -->
writer = csv.writer(f, delimiter=",") for key, value in adjs.items():

<!-- b000584 | prose | pages [26] -->
row = [key] + value writer.writerow(row)

<!-- b000585 | prose | pages [26, 27] -->
关注数学模型 Page 26

<!-- b000586 | furniture | pages [26] -->
2

<!-- b000587 | furniture | pages [26] -->
MATHmodels

<!-- b000588 | furniture | pages [26] -->
获取更多资讯

<!-- b000589 | furniture | pages [27] -->
Team # 2004647

<!-- b000591 | prose | pages [27] -->
RRBS-reputation.m

<!-- b000592 | prose | pages [27] -->
for i=2:length(S(:,1)) index=find(item==cell2mat(S(i,5))); if mod(timer,12)~=0 if review_date(i,2)~=mod(timer,12) timer=timer+1; end else if review_date(i,2)==1 timer=timer+1; end end if ~isempty(index) if K(i,1)==0 beta=1; else if K(i,1)>0 beta=vine(i,1)*K(i,1)^verified(i,1)*exp(helpful_of_total_votes(i,1))*0.5*log else beta=vine(i,1)*(-1)*(abs(K(i,1)))^verified(i,1)*exp(helpful_of_total_votes( end end record(timer,1,index)=record(timer,1,index)+1; record(timer,2,index)=record(timer,2,index)+rating_123(i,1).*beta; end end

<!-- b000593 | prose | pages [27] -->
begin=zeros(1,top); alpha=1.1; for index=1:length(record(1,1,:))

<!-- b000594 | prose | pages [27] -->
exponent_window_origina=[]; begin(1,index)=find(record(:,1,index)>0, 1, ’first’); record(1:begin(1,index)-1,3,index)=zeros(begin(1,index)-1,1); for j=1:length(record(:,1,1))-begin(1,index)+1 exponent_window_origina=[exponent_window_origina,alpha^j]; end for i=begin(1,index):length(record(:,1,1)) exponent_window=exponent_window_origina./alpha^(i-begin(1,index)+1); record(i,3,index)=exponent_window(1,1:i-begin(1,index)+1)*record(begin(1,index):i,2 end end

<!-- b000595 | prose | pages [27, 28] -->
关注数学模型 Page 27

<!-- b000596 | furniture | pages [27] -->
2

<!-- b000597 | furniture | pages [27] -->
MATHmodels

<!-- b000598 | furniture | pages [27] -->
获取更多资讯

<!-- b000599 | furniture | pages [28] -->
Team # 2004647

<!-- b000601 | caption | pages [28] -->
Table 13: Top-30 words with the largest 5-star-rates

<!-- b000602 | prose | pages [28] -->
Word Count Grade 1-Star-Rate 2-Star-Rate 3-Star-Rate 4-Star-Rate 5-Star-Rate 3 0.869565217 awesome 92 0.043478261 0.010869565 0.043478261 0.032608696 3 0.862318841 wonderful 138 0.007246377 0.014492754 0.028985507 0.086956522 3 0.846153846 love 52 0.019230769 0.019230769 0.019230769 0.096153846 3 0.829875519 adorable 241 0.01659751 0.024896266 0.033195021 0.095435685 2 0.829457364 favorite 258 0.007751938 0.027131783 0.027131783 0.108527132 2 0.804597701 durable 174 0.011494253 0.040229885 0.040229885 0.103448276 3 0.803921569 fantastic 102 0.029411765 0.029411765 0.058823529 0.078431373 3 0.766595289 perfect 467 0.023554604 0.019271949 0.029978587 0.160599572 3 0.762195122 excellent 164 0.042682927 0 0.036585366 0.158536585 3 0.736842105 beautiful 57 0.087719298 0.01754386 0.070175439 0.087719298 2 0.736686391 cute 338 0.00591716 0.026627219 0.082840237 0.147928994 2 0.732142857 affordable 56 0 0 0.071428571 0.196428571 3 0.728813559 glad 59 0.016949153 0.033898305 0.016949153 0.203389831 1 0.722818792 easy 1490 0.01409396 0.019463087 0.040268456 0.203355705 3 0.720720721 pleased 222 0.018018018 0.022522523 0.031531532 0.207207207 2 0.709090909 satisﬁed 55 0.018181818 0.054545455 0.054545455 0.163636364 3 0.700980392 super 204 0.034313725 0.029411765 0.078431373 0.156862745 2 0.7 healthy 50 0.04 0.08 0.04 0.14 3 0.692390718 great 3706 0.031840259 0.036157582 0.062601187 0.177010254 3 0.692307692 funny 78 0.064102564 0.064102564 0.051282051 0.128205128 1 0.682692308 free 208 0.057692308 0.033653846 0.067307692 0.158653846 3 0.678066038 happy 848 0.053066038 0.048349057 0.036556604 0.183962264 3 0.674846626 loved 163 0.055214724 0.049079755 0.049079755 0.171779141 2 0.672064777 clean 494 0.046558704 0.046558704 0.062753036 0.172064777 2 0.666666667 recommend 114 0.087719298 0.070175439 0.052631579 0.122807018 2 0.654545455 effective 55 0.072727273 0.036363636 0.018181818 0.218181818 1 0.650205761 natural 243 0.057613169 0.037037037 0.065843621 0.189300412 2 0.638795987 worth 299 0.107023411 0.043478261 0.053511706 0.157190635 2 0.622474747 powerful 792 0.025252525 0.041666667 0.112373737 0.198232323 2 0.615384615 reliable 52 0.096153846 0.038461538 0.096153846 0.153846154

<!-- b000603 | prose | pages [28, 29] -->
关注数学模型 Page 28

<!-- b000604 | furniture | pages [28] -->
2

<!-- b000605 | furniture | pages [28] -->
MATHmodels

<!-- b000606 | furniture | pages [28] -->
获取更多资讯

<!-- b000607 | furniture | pages [29] -->
Team # 2004647

<!-- b000609 | caption | pages [29] -->
Table 14: Top-20 words with the largest 1-star-rates

<!-- b000610 | prose | pages [29] -->
Word Count Grade 1-Star-Rate 2-Star-Rate 3-Star-Rate 4-Star-Rate 5-Star-Rate -2 0.634615385 dangerous 52 0.096153846 0.076923077 0.038461538 0.153846154 -3 0.5 terrible 54 0.111111111 0.074074074 0.148148148 0.166666667 -2 0.425531915 poor 94 0.244680851 0.138297872 0.063829787 0.127659574 -2 0.362244898 disappointed 196 0.224489796 0.183673469 0.086734694 0.142857143 -3 0.360655738 horrible 61 0.163934426 0.147540984 0.114754098 0.213114754 -2 0.321428571 useless 56 0.25 0.196428571 0.142857143 0.089285714 -2 0.271317829 wrong 129 0.108527132 0.131782946 0.100775194 0.387596899 -3 0.246458924 bad 353 0.101983003 0.144475921 0.175637394 0.331444759 2 0.232142857 positive 56 0.107142857 0.089285714 0.107142857 0.464285714 1 0.176470588 certain 51 0.058823529 0.215686275 0.215686275 0.333333333 -2 0.175438596 weak 57 0.245614035 0.263157895 0.140350877 0.175438596 1 0.171171171 safe 111 0.045045045 0.063063063 0.135135135 0.585585586 1 0.167785235 clear 149 0.046979866 0.134228188 0.22147651 0.429530201 -1 0.132478632 difﬁcult 234 0.128205128 0.183760684 0.247863248 0.307692308 -3 0.12 loose 50 0.12 0.12 0.08 0.56 2 0.113821138 top 123 0.146341463 0.089430894 0.170731707 0.479674797 -1 0.112903226 hard 372 0.10483871 0.13172043 0.174731183 0.475806452 1 0.111111111 want 63 0.063492063 0.111111111 0.158730159 0.555555556 2 0.107023411 worth 299 0.043478261 0.053511706 0.157190635 0.638795987 -2 0.105691057 negative 123 0.032520325 0.056910569 0.284552846 0.520325203

<!-- b000611 | prose | pages [29] -->
关注数学模型

<!-- b000612 | furniture | pages [29] -->
2

<!-- b000613 | furniture | pages [29] -->
MATHmodels

<!-- b000614 | furniture | pages [29] -->
获取更多资讯
