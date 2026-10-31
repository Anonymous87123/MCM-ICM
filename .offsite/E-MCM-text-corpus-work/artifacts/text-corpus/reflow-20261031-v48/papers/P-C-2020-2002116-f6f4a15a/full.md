# P-C-2020-2002116-f6f4a15a

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2020

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | title | pages [1] -->
MCM/ICM

<!-- b000005 | furniture | pages [1] -->
2002116

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Riddle of Sphinx: Cracking the Secret of Amazon’s

<!-- b000009 | title | pages [1] -->
Ratings and Reviews

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
We have witnessed the rise of mass online marketplaces. For example Amazon, one of the biggest online platforms, is worth around $ 915 billion. Guided by the customer obsession principle, it provides an opportunity for the customers to rate the products from 1 to 5. More- over, buyers can submit a text-based message, namely review, to express their feeling towards the products. The massive data of those ratings and reviews offer a wealth of information re- mained to be mined. Analysis of text-based messages or rating-based values has received wide attention, yet there is not a method severs as the combination of both, especially for the case of an online marketplace.

<!-- b000012 | prose | pages [1] -->
To address the above-mentioned challenge, we propose a novel CE-VADER hybrid model for sentiment analysis in reviews, classifying messages into ﬁve groups of strong positive, weak positive, moderate, weak negative and strong negative. Empirical results indicate that the pro- posed ﬁve-group classiﬁcation model correlates to the ﬁve-star rating system well. Then a state-of-art informative evaluation model is proposed as the combination of the text-based and rating-based measures. We pick out 1% most informative reviews and ratings of each product to evaluate the properties and propose sales strategies.

<!-- b000013 | prose | pages [1] -->
We propose the “reputation” rate based on the differential equation model in the literature to evaluate the reputation of the product. Then we employ an Auto Regression (AR) model as the time series forecasting method to predict future “reputation” rate and the potential success or the failure of each product. AR model shows high accuracy on the validation set with a maximum Root Mean Square Error (RMSE) of 0.131. Paciﬁers have a good reputation and pre- dicted to be successful while microwaves and hair dryers have bad reputations and predicted to fail. The results show relevance with the proportions of the continuous ﬁve-star or one-star rating sequence. Lastly, we analyze speciﬁc words and descriptors to ﬁnd their correlation to the ratings.

<!-- b000014 | prose | pages [1] -->
According to our empirical results, we propose some conﬁdent sales strategies and recom- mendations for the online marketplace, e.g., the timing choice of introducing products into market, targeted adjustment according to star ratings, etc. We write a letter to the marketing director of Sunshine Company to summarize our analysis and results, together with our rec- ommendations.

<!-- b000015 | prose | pages [1] -->
Our framework shows a strong accuracy, robustness. It can be easily implemented to other data with our source codes.

<!-- b000016 | keywords | pages [1] -->
Keywords: Text-Based Measure, Informative Text Selection, Reputation Quantiﬁcation, Sales

<!-- b000017 | prose | pages [1] -->
Strategy Formation.

<!-- b000018 | furniture | pages [1] -->
关注数学模型

<!-- b000019 | furniture | pages [1] -->
2

<!-- b000020 | furniture | pages [1] -->
MATHmodels

<!-- b000021 | furniture | pages [1] -->
获取更多资讯

<!-- b000022 | furniture | pages [2] -->
Team # 2002116

<!-- b000023 | furniture | pages [2] -->
Page 1 of 38

<!-- b000024 | contents | pages [2] -->
Riddle of Sphinx: Cracking the Secret of Amazon’s

<!-- b000025 | contents | pages [2] -->
Ratings and Reviews

<!-- b000026 | contents | pages [2] -->
March 9, 2020

<!-- b000027 | heading | pages [2] -->
Contents

<!-- b000028 | contents | pages [2] -->
1 Introduction

<!-- b000029 | contents | pages [2] -->
3

<!-- b000030 | contents | pages [2] -->
2 Assumptions and Notations

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
2.1

<!-- b000033 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
4

<!-- b000035 | contents | pages [2] -->
2.2

<!-- b000036 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
4

<!-- b000038 | contents | pages [2] -->
3 Informative Evaluation Model

<!-- b000039 | contents | pages [2] -->
4

<!-- b000040 | contents | pages [2] -->
3.1

<!-- b000041 | contents | pages [2] -->
Vector Encoding Forms of Star Ratings . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
5

<!-- b000043 | contents | pages [2] -->
3.2

<!-- b000044 | contents | pages [2] -->
Contextual Entropy VADER Hybrid Model for Text-Based Measures

<!-- b000045 | contents | pages [2] -->
. . . . . . .

<!-- b000046 | contents | pages [2] -->
5

<!-- b000047 | contents | pages [2] -->
3.2.1

<!-- b000048 | contents | pages [2] -->
Manually Annotating the Seed Word

<!-- b000049 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
7

<!-- b000051 | contents | pages [2] -->
3.2.2

<!-- b000052 | contents | pages [2] -->
Contextual Entropy Block (CE) . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
7

<!-- b000054 | contents | pages [2] -->
3.2.3

<!-- b000055 | contents | pages [2] -->
VADER Block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
9

<!-- b000057 | contents | pages [2] -->
3.2.4

<!-- b000058 | contents | pages [2] -->
Proposed CE-VADER for Sentiment Analysis

<!-- b000059 | contents | pages [2] -->
. . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
9

<!-- b000061 | contents | pages [2] -->
3.3

<!-- b000062 | contents | pages [2] -->
Combination of Text-Based and Rating-Based Measures . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
10

<!-- b000064 | contents | pages [2] -->
3.4

<!-- b000065 | contents | pages [2] -->
Model Implementation, Sensitivity Analysis and Results

<!-- b000066 | contents | pages [2] -->
. . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
11

<!-- b000068 | contents | pages [2] -->
4 Difference Equation to Measure Time-Based Pattern

<!-- b000069 | contents | pages [2] -->
11

<!-- b000070 | contents | pages [2] -->
4.1

<!-- b000071 | contents | pages [2] -->
Difference Equation Based Model . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
11

<!-- b000073 | contents | pages [2] -->
4.2

<!-- b000074 | contents | pages [2] -->
Model Implementation, Sensitivity Analysis and Results

<!-- b000075 | contents | pages [2] -->
. . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
12

<!-- b000077 | contents | pages [2] -->
5 Predict Potential Success or Failure

<!-- b000078 | contents | pages [2] -->
14

<!-- b000079 | contents | pages [2] -->
5.1

<!-- b000080 | contents | pages [2] -->
Time Series Forecasting for Predicting Future Reputation . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
14

<!-- b000082 | contents | pages [2] -->
5.2

<!-- b000083 | contents | pages [2] -->
Evaluating the Success or Failure potential

<!-- b000084 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | contents | pages [2] -->
14

<!-- b000086 | contents | pages [2] -->
5.3

<!-- b000087 | contents | pages [2] -->
Model Implementation and Results . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
14

<!-- b000089 | contents | pages [2] -->
6 Speciﬁc Ratings and Descriptors Analysis

<!-- b000090 | contents | pages [2] -->
15

<!-- b000091 | contents | pages [2] -->
6.1

<!-- b000092 | contents | pages [2] -->
Speciﬁc Star Ratings Relevance to Rating Frequency . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [2] -->
16

<!-- b000094 | contents | pages [2] -->
6.2

<!-- b000095 | contents | pages [2] -->
Speciﬁc Quality Descriptors’ Relevance to Rating Levels

<!-- b000096 | contents | pages [2] -->
. . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
18

<!-- b000098 | contents | pages [2] -->
6.2.1

<!-- b000099 | contents | pages [2] -->
Naive Bayesian Model for Evaluation . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
18

<!-- b000101 | furniture | pages [2] -->
关注数学模型

<!-- b000102 | furniture | pages [2] -->
2

<!-- b000103 | furniture | pages [2] -->
MATHmodels

<!-- b000104 | furniture | pages [2] -->
获取更多资讯

<!-- b000105 | furniture | pages [3] -->
Team # 2002116

<!-- b000106 | furniture | pages [3] -->
Page 2 of 38

<!-- b000107 | contents | pages [3] -->
6.2.2

<!-- b000108 | contents | pages [3] -->
Model Implementation and Results

<!-- b000109 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | furniture | pages [3] -->
19

<!-- b000111 | heading | pages [3] -->
7 Attractiveness Analysis of Design Features

<!-- b000112 | prose | pages [3] -->
20

<!-- b000113 | heading | pages [3] -->
8 Sales Strategies and Recommendations

<!-- b000114 | prose | pages [3] -->
20

<!-- b000115 | heading | pages [3] -->
9 Strengths and Weaknesses

<!-- b000116 | prose | pages [3] -->
21 9.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 9.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

<!-- b000117 | heading | pages [3] -->
10 Conclusion

<!-- b000118 | prose | pages [3] -->
22

<!-- b000119 | heading | pages [3] -->
11 A Letter to the Marketing Director of Sunshine Company

<!-- b000120 | prose | pages [3] -->
22

<!-- b000121 | heading | pages [3] -->
Appendices

<!-- b000122 | prose | pages [3] -->
24

<!-- b000123 | heading | pages [3] -->
Appendix A Annotated Seed Words and Frequency

<!-- b000124 | prose | pages [3] -->
24

<!-- b000125 | heading | pages [3] -->
Appendix B

<!-- b000126 | prose | pages [3] -->
The Number of Keyword Occurrences in Different Keyword Groups 25

<!-- b000127 | heading | pages [3] -->
Appendix C Top 1% Most Informative Ratings and Reviews

<!-- b000128 | prose | pages [3] -->
26

<!-- b000129 | heading | pages [3] -->
Appendix D Source Code for VADER Sentiment Analysis

<!-- b000130 | prose | pages [3] -->
36

<!-- b000131 | heading | pages [3] -->
Appendix E

<!-- b000132 | heading | pages [3] -->
Source Code for Informative Algorithm

<!-- b000133 | prose | pages [3] -->
36

<!-- b000134 | heading | pages [3] -->
Appendix F

<!-- b000135 | prose | pages [3] -->
Source Code for Reputation Calculation 37

<!-- b000136 | heading | pages [3] -->
Appendix G Source Code for Beyes Model

<!-- b000137 | prose | pages [3] -->
37

<!-- b000138 | heading | pages [3] -->
Appendix H Source Code for Time Series Prediction

<!-- b000139 | prose | pages [3] -->
38

<!-- b000140 | heading | pages [3] -->
Appendix I

<!-- b000141 | prose | pages [3] -->
Source Code for Wordcloud Picture 38

<!-- b000142 | furniture | pages [3] -->
关注数学模型

<!-- b000143 | furniture | pages [3] -->
2

<!-- b000144 | furniture | pages [3] -->
MATHmodels

<!-- b000145 | furniture | pages [3] -->
获取更多资讯

<!-- b000146 | furniture | pages [4] -->
Team # 2002116

<!-- b000147 | furniture | pages [4] -->
Page 3 of 38

<!-- b000148 | heading | pages [4] -->
1 Introduction

<!-- b000149 | prose | pages [4] -->
Our society has witnessed the rise of many online marketplaces, with a total worldwide market value of 4.3 trillion dollars [1]. One salient feature of the online marketplace compared with traditional platforms is the massive review of texts and ratings. Among all of them, Ama- zon has received the most attention, as its greatest success [1]. Amazon also provides customers with chances to freely express their feeling and rate the products that they have purchased.

<!-- b000150 | prose | pages [4] -->
Previous work [2] indicates that customers will largely refer to the reviews and ratings be- fore they buy the product on the platforms. Platforms can adjust their sales strategy by checking these comments. Hence, the ratings and the reviews both provide references to other potential buyers and massive data to analyze the demand of the customers, which can help to develop adaptive strategies. By making full use of these data, we can achieve a win-win situation for both the buyers and the platform.

<!-- b000151 | prose | pages [4] -->
One of the biggest challenges is the complexity and diversity of the texts of the reviews [3, 4]. In this paper, we propose a novel sentiment analysis model as the text-based measure to address this issue. In this paper, we develop a series of models as the combination of text-based, rating- based, and time-based measures to pick out the most informative ratings and reviews to track. We also construct a novel evaluation framework to quantify the reputation of each product and predict potential success or failure. Then, we analyze the correlation between continuous same star ratings, word descriptors and the reputation of the products. We implement our model on the real data set generated from three different types of products, namely the paciﬁer, microwave, and the hair dryer.

<!-- b000152 | prose | pages [4] -->
Researchers have pointed out the necessity to study when and how the online platforms should adjust their marketing communication strategy in response to consumer reviews or rat- ings [5]. We propose several sales strategies and recommendations in this paper based on our analysis and results.

<!-- b000153 | prose | pages [4] -->
The rest of the paper is organized as follows. In section 2, we list the main assumptions in model construction and introduce the notations which will be frequently used in this paper. In section 3, a novel Information Evaluation Model is proposed. It is made up of a hybrid the state-of-art CE [6] and VADER [7] for sentiment analysis in the review text. Then we propose the "importance" rate as a combination of text-based measure (i.e., our proposed CE-VADER model) and ratings-based measure (i.e., the star-rating and the helpful votes) to indicate how informative the review and the rating are. To the best of our knowledge, we are the ﬁrst to propose a review-text-based sentiment analysis model. In section 4, we employ a difference equation model as the backbone to measure the time pattern of each product. Moreover, the "reputation" rate is proposed in this section to measure the growth or the decline of the repu- tation. In section 5, we employ an Auto Regression model (AR) to predict the change of rep- utation in the future time domain and propose a fuzzy system to predict the potential success or failure of each product. More details about the results of our model implemented on given data can be found in section 6,7,8. The strengths and weaknesses of the proposed model and framework are discussed in section 9. We conclude in section 10. All source codes are attached to the Appendix D-I and can be easily implemented to other data sets.

<!-- b000154 | furniture | pages [4] -->
关注数学模型

<!-- b000155 | furniture | pages [4] -->
2

<!-- b000156 | furniture | pages [4] -->
MATHmodels

<!-- b000157 | furniture | pages [4] -->
获取更多资讯

<!-- b000158 | furniture | pages [5] -->
Team # 2002116

<!-- b000159 | furniture | pages [5] -->
Page 4 of 38

<!-- b000160 | heading | pages [5] -->
2 Assumptions and Notations

<!-- b000161 | heading | pages [5] -->
2.1 Assumptions

<!-- b000162 | prose | pages [5] -->
To simplify our model and eliminate the complexity, we make the following main assump- tions in this literature. All assumptions will be re-emphasized once they are used in the con- struction of our model. Assumption 1. The online marketplace operates stably. And there were no situations such as an out- break of an epidemic which would seriously affect the production chain of online shopping.

<!-- b000163 | prose | pages [5] -->
Assumption 2. The ratings and reviews depict customers’ real experience and feeling about their pur- chased products. The sentiment in the review text reﬂects one’s feelings on the products.

<!-- b000164 | prose | pages [5] -->
Assumption 3. The vast majority of individual differences of customers e.g., economic status and edu- cational level, are ignored.

<!-- b000165 | prose | pages [5] -->
Assumption 4. It takes some time for shipping the product. Some customers would prefer making reviews sometime after receiving the purchased products.

<!-- b000166 | prose | pages [5] -->
Assumption 5. Consumers pay more attention to the negative comments e.g., low-star rating or nega- tive reviews when purchasing the products.

<!-- b000167 | heading | pages [5] -->
2.2 Notations

<!-- b000168 | prose | pages [5] -->
In this work, we use the nomenclature in Table 1 in the model construction. Other none- frequent-used symbols will be introduced once they are used.

<!-- b000169 | caption | pages [5] -->
Table 1: Notations used in this literature

<!-- b000170 | prose | pages [5] -->
Symbol Deﬁnition Type id review id String sid Star rate, subscript is its associated review id Scalar hvid Helpful votes, subscript is its associated review id Scalar Rid Review text, subscript is its associated review id String rdid Review date, subscript is its associated review id Date VEC Vector encoding of the star rating Mapping INT Vector encoding of intensity relevant to 5-class seed words Mapping IMP Importance rate of review and associated rating Mapping REP Reputation rate of product at some time Mapping

<!-- b000171 | heading | pages [5] -->
3 Informative Evaluation Model

<!-- b000172 | prose | pages [5, 6] -->
In this section, we proposed the "importance" to evaluate how informative the review text and star rates are. The most informative factor we take into account is the sentiment of the review text. In this literature, we propose a CE-VADER model to address the sentiment analysis issue in the review text. Our model will classify the text into ﬁve groups: strong positive, weak positive, moderate, weak negative and strong negative in the consistency of the ﬁve-star rating scheme. Then our proposed "importance" will incorporate the text-based measure, star rating with their ﬁdelity, correlation. The higher the importance, the more informative it is. The rest of the section is arranged as follows. In section 3.1, we covert the integral star rate to vector form. In section 3.2, we propose the CE-VADER, a hybrid model for the text-based measures. In section 3.3, we introduce the "importance" to calculate how informative the review and the star rating together are. In section 3.4, we implemented our model on real data set of 3 types of products to indicate 1% most informative review and star ratings, and analyze the model sensitivity.

<!-- b000173 | furniture | pages [5] -->
关注数学模型

<!-- b000174 | furniture | pages [5] -->
2

<!-- b000175 | furniture | pages [5] -->
MATHmodels

<!-- b000176 | furniture | pages [5] -->
获取更多资讯

<!-- b000177 | furniture | pages [6] -->
Team # 2002116

<!-- b000178 | furniture | pages [6] -->
Page 5 of 38

<!-- b000180 | heading | pages [6] -->
3.1 Vector Encoding Forms of Star Ratings

<!-- b000181 | prose | pages [6] -->
Consumers can freely express their comments on the products on Amazon by rating one to ﬁve stars after purchasing. A one-star rating is associated with the least satisfaction while ﬁve-star with the highest satisfaction. The one-to-ﬁve star rating itself is a sufﬁcient measure. To combine the ratings-based measure with the text-based measure which we will discuss in the next section. We would like to convert the star-rating to vector forms in this section.

<!-- b000182 | prose | pages [6] -->
Firstly, we calculate the ration of each star rate of hair dryers, baby paciﬁers, and mi- crowaves from the given data respectively, as shown in Figure 1. We observe that baby paciﬁers have received the highest percentage of high star rating, while microwaves a lower star rating. Products with high technology content also face more quality problems, which is in line with actual expectations, indicating that star ratings can indeed reﬂect consumer satisfaction.

<!-- b000183 | prose | pages [6] -->
However, we would like to convert the rating to an equivalent 5−dimension vector en- coding forms. Denote the star-rate as s ∈{1, 2, 3, 4, 5}, the vector encoding forms of s can be s)T ∈R5 where the components deﬁned by: formulated by VEC(s) = (vec1 s, · · · , vec5

<!-- b000184 | prose | pages [6] -->
|i−s|2 e 2σ0 veci s = (1) |j−s|2 P5 j=1 e 2σ0

<!-- b000185 | prose | pages [6] -->
where σ0 is a tunable parameter, determining the robustness of our model, the bigger the more robust. The mapping VEC is one-to-one, hence we claim the converted form is equivalent to the s}, ii) P5 star-rating. Moreover, by our deﬁnition, we can ﬁnd: i) s = argmaxi{veci i=1 veci s = 1. VEC(s) encoding as a probabilistic vector with each component represents their possibility to be rated by the associated star e.g., the 4-star rate has the highest probability to be rated 4 stars, second-highest possibility to be rated as 3 or 5 stars.

<!-- b000186 | heading | pages [6] -->
3.2 Contextual Entropy VADER Hybrid Model for Text-Based Measures

<!-- b000187 | prose | pages [6] -->
In this literature, we construct a novel model for sentiment analysis based on the review text. To the sake of simplicity, the sentiment scored by the text is regarded as the only fact to measure the success or the failure of the product e.g., the positive attitudes usually indicate a higher potential of the product success while on the contrary, negative attitudes indicate a higher possibility for the product failure.

<!-- b000188 | prose | pages [6, 7] -->
In this section, we propose a contextual entropy and VADER [7] hybrid model, namely the CE-VADER to address the sentiment analysis challenge in the review text. The model is made up of the two blocks: the contextual entropy (CE) block and the VADER block. CE model shows its high capability in sentiment analysis of the stock market news [6] but its limitation in short ⭐⭐⭐⭐⭐ ⭐⭐⭐⭐ ⭐⭐⭐ ⭐⭐ ⭐ Total number

<!-- b000189 | furniture | pages [6] -->
关注数学模型

<!-- b000190 | furniture | pages [6] -->
2

<!-- b000191 | furniture | pages [6] -->
MATHmodels

<!-- b000192 | furniture | pages [6] -->
获取更多资讯

<!-- b000193 | furniture | pages [7] -->
Team # 2002116

<!-- b000194 | furniture | pages [7] -->
Page 6 of 38

<!-- b000196 | prose | pages [7] -->
pacifier 9451192 1426 18939 2716 12660

<!-- b000197 | prose | pages [7] -->
microwave 300 134 112 402 667 1615

<!-- b000198 | prose | pages [7] -->
11470 hair dryer 999 639 1032 6704 2096

<!-- b000199 | prose | pages [7] -->
0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%

<!-- b000200 | caption | pages [7] -->
Figure 1: Star rating distribution of paciﬁer, microwave and hair dryer based on the given data.

<!-- b000201 | prose | pages [7] -->
context e.g., the review in this literature. While the VADER model outperforms the state-of-art nature language model in short online texture but their accuracy depends a lot on the pre-listed lexicon words. The two blocks of CE-VADER will separative outcome a 5−dimension prob- abilistic vector with each component represents the probability of being its associated group. After a voting block, our proposed model will classify the review into one of the ﬁve groups together with an intensity showing how intense it is to be classiﬁed into the group. By hybridiz- ing both models, we show CE-VADER can classify the review context into ﬁve groups in the consistency of the star rating.

<!-- b000202 | prose | pages [7] -->
The rest of this section is arranged as follows. Firstly we show our strategy to generate the seed words for the CE model and expanding the gold-standard list of the VADER block. Then we introduce the CE and VADER model superlatively. Finial we propose the hybrid CE- VADER model. Our model will classify the review context into ﬁve classes: strong positive, weak positive, moderate, weak negative and strong negative, with its intensity. In the next section, we will propose a review ﬁdelity based on the classiﬁcation results and the intensity.

<!-- b000203 | prose | pages [7] -->
Seed word Annotated candidate Seed word generate

<!-- b000204 | prose | pages [7] -->
Seed words for CE Extend gold-standard list

<!-- b000205 | prose | pages [7] -->
Strength of Contextual co-occurrence distribution Sentiment analysis by VADER analysis analysis

<!-- b000206 | prose | pages [7] -->
Aggregation

<!-- b000207 | prose | pages [7] -->
Sentiment class and intensity

<!-- b000208 | caption | pages [7] -->
Figure 2: The overall architecture of our proposed CE-VADER model. The model is made up of

<!-- b000209 | prose | pages [7] -->
two blocks, namely the CE block and the VADER block.

<!-- b000210 | furniture | pages [7] -->
关注数学模型

<!-- b000211 | furniture | pages [7] -->
2

<!-- b000212 | furniture | pages [7] -->
MATHmodels

<!-- b000213 | furniture | pages [7] -->
获取更多资讯

<!-- b000214 | furniture | pages [8] -->
Team # 2002116

<!-- b000215 | furniture | pages [8] -->
Page 7 of 38

<!-- b000216 | heading | pages [8] -->
3.2.1 Manually Annotating the Seed Word

<!-- b000217 | prose | pages [8] -->
We put 80% of the data as the training set and all the rest 20% as the testing set of eval- uations. Sentences in the review body from the training set are broken down into separated words, among which are statistically calculated their frequency. The high-frequency emotion words are picked out as seed words and manually annotated by us, while the low-frequency ones are discarded. The annotator (one of our group members) will incorporate his expertise natural-language processing knowledge for the classifying all the selected emotion words into ﬁve groups i.e., strong positive, weak positive, moderate, weak negative and strong negative. Instead of coarse two-group annotations of either "positive" or "negative" [6], we detailedly sub-classify each one into "strong" and "weak" subgroups and set aside one more group labeled as "moderate". The ﬁve-group annotation strategies aim to correlate with the one-to-ﬁve-star- rating score e.g., "weak positive" maps to the four-star-rating. We denote the ﬁve groups of the seed word as Gi, with i = 1, 2, 3, 4, 5.

<!-- b000218 | prose | pages [8] -->
Representative words generated from the training set with "positive" or "negative" labels are depicted in Figure 3 with the cold tone or warm tone respectively. Annotated ﬁve-class seed words are attached to Appendix A.

<!-- b000219 | caption | pages [8] -->
Figure 3: Demonstration of some representative seed words. Words annotated as "positive" are

<!-- b000220 | prose | pages [8] -->
colored in light tone while the "negative" ones in a dark tone. The bigger the size, the higher word frequency.

<!-- b000221 | heading | pages [8] -->
3.2.2 Contextual Entropy Block (CE)

<!-- b000222 | prose | pages [8] -->
The contextual entropy block employs a part-contextual entropy model [6] as the back- bone architecture. A part-contextual entropy model can consider both the strength of the co- occurrence and the contextual distribution between the candidate of the most representative words from the review context and the generated seed words.

<!-- b000223 | prose | pages [8, 9] -->
We employ a vector to encode the strength between word and its context in the review. To be more speciﬁc, denote the left and the right context of the kth word wk in the n-word review context R = w1w2 · · · wkwk+1 · · · wn are {w1w2 · · · wk−1} and {wk+1wk+2 · · · wn} respectively. Note that we set review as a complete target instead of breaking it into sentences as in the ref.[6], in consideration of the short contextual style of online comments. The dimension of the vector depends on the length of the review i.e.,n. Denote the vector to record the left context of word wk as vleft(wk) = (vleft wk1, vleft wk2, · · · , vleft wkN) and the vector to record the right context as vright(wk) = wkN ), where the subscript i for the ith component of the vector. The value of (vright wk1 , vright wk2 , · · · , vright vwki representing the co-occurrence strength between the wk and wi. To calculate the possibility distance we will discuss soon validate, all the vectors have to be in the form of probabilistic representation. N ≤n is the dimension of the context vector, it counts the number of distinct words in the context of the review R.

<!-- b000224 | furniture | pages [8] -->
关注数学模型

<!-- b000225 | furniture | pages [8] -->
2

<!-- b000226 | furniture | pages [8] -->
MATHmodels

<!-- b000227 | furniture | pages [8] -->
获取更多资讯

<!-- b000228 | furniture | pages [9] -->
Team # 2002116

<!-- b000229 | furniture | pages [9] -->
Page 8 of 38

<!-- b000231 | prose | pages [9] -->
The weight vwki is formulated by:

<!-- b000232 | prose | pages [9] -->
e−|j−k|2 X vwki = (2) 2σ

<!-- b000233 | prose | pages [9] -->
j

<!-- b000234 | prose | pages [9] -->
It takes both the spatial factor and the distance factor into consideration. Here we employ a Gaussian function to measure the distance as we hold the assumption that the closer, the more weight it gains. Then to make the vector into probabilistic representations, we normalize it by:

<!-- b000235 | prose | pages [9] -->
vwki vwki ← (3) P i vwki

<!-- b000236 | prose | pages [9] -->
Then we change the candidate words or the seed words into probability vector representa- tions. Then we will employ a Kullback–Leibler (KL) distance[8] (denoted as KL(·∥·)) to mea- sure the distance between the vector v(ci) = (v(ci)left, v(ci)right) of the ith candidate word and v(seedj) = (v(seedj)left, v(seedj)right) of the jth seed word, that is:

<!-- b000237 | prose | pages [9] -->
N P(dk|ci) X D(ci∥seedj) := KL(v(ci)∥v(seedj)) = P(dk|ci)log (4) P(dk|seedj) k=1 where P(dk|ci) and P(dk|seedj denote probabilistic weights of the kth dimension of the left (or right) context vector of ci and seedj respectively and N is the dimensional of the context prob- abilistic vector. Due to the non-symmetry of the KL-distance i.e., D(ci∥seedj)̸ = D(seedj∥ci), we employ the following symmetry distance (denoted as SD(·, ·)):

<!-- b000238 | prose | pages [9] -->
SD(seedj, ci) = SD(ci, seedj) := D(ci∥seedj) + D(seedj∥ci) (5) The addition of D(ci∥seedj) and D(seedj∥ci) not only makes the symmetry of the SD(·, ·) but also accounts for both their left and right contextual distributions. Then we will deﬁne the similarity (denoted as SI(·, ·)) between the candidate word ci and seed word seedj based on the symmetry distance by:

<!-- b000239 | prose | pages [9] -->
1 SI(ci, seedj) := (6) 1 + SD(ci, seedj) SI(ci, seedj) ∈(0, 1] measures the similarity between two words, with the bigger the more simi- larity they share. In particular, SI(ci, seedj) equals 1 if and only if ci = seedj. After the calcula- tion of the similarity of candidate word and seed word, we will propose the similarity between the candidate word ci and one of the ﬁve groups Gj by:

<!-- b000240 | prose | pages [9] -->
1 X SI(ci, Gj) := SI(ci, seedk) (7) |Gj| seedk∈Gj SI(ci, Gj) ∈(0, 1] measures the similarity of candidate word ci to the jth group of the sentimental seed words. The similarity of review R to Gj is deﬁned by:

<!-- b000241 | prose | pages [9, 10] -->
N SI(R, Gj) := 1 X SI(ci, Gj) (8) N i=1 SI(R, Gj) ∈(0, 1] measures the similarity of review R to the jth group of the sentimental seed words, the bigger the more similarity. The output of the CE block is a 5−dimension probabilistic R)T ∈R5. The jth component CEj vector CE(R) = (CE1 R, · · · , CE5 R is the intensity associated with group Gj, it is deﬁned by:

<!-- b000242 | furniture | pages [9] -->
关注数学模型

<!-- b000243 | furniture | pages [9] -->
2

<!-- b000244 | furniture | pages [9] -->
MATHmodels

<!-- b000245 | furniture | pages [9] -->
获取更多资讯

<!-- b000246 | furniture | pages [10] -->
Team # 2002116

<!-- b000247 | furniture | pages [10] -->
Page 9 of 38

<!-- b000249 | prose | pages [10] -->
SI(R, Gj) CEj R = (9) P5 i=1 SI(R, Gi)

<!-- b000250 | heading | pages [10] -->
3.2.3 VADER Block

<!-- b000251 | prose | pages [10] -->
VADER [7] is a simple rule-based model for general sentiment analysis, especially for the social media text style. Based on manually generated a gold-standard list of lexical features [7], VADER does not require any training data, which shows its promising potential to extend to a wide range of tasks of sentiment analysis. Hence, in this literature, we extend the good- standard list of lexical features based on our generated seed words to address the sentiment analysis of the review context. Moreover, we also extend the original four group prediction results to ﬁve group prediction results, i.e., strong positive, weak positive, moderate, weak neg- ative and strong negative in the consistency of our CE block. Readers are referred to ref.[7] for more details about the framework of the VADER. The extended gold-standard list is attached to Appendix A. The outcome of the VADER Block is also a 5−dimension probabilistic vector with the jth component is the intensity corresponds to the jth seed word group Gj. Denoted the R)T ∈R5. outcome vector of review R as V ADER(R) = (V ADER1 R, · · · , V ADER5

<!-- b000252 | heading | pages [10] -->
3.2.4 Proposed CE-VADER for Sentiment Analysis

<!-- b000253 | prose | pages [10] -->
Our proposed CE-VADER hybrid model is made up of two blocks: CE block and VADER block. Both of the two blocks will provide a 5−dimension probabilistic vector CE(R) and V ADER(R) to a review context R with each component is the intensity to its corresponding group Gj. We will employ a smoothing convex linear combination of the two vectors as the ﬁnal intensity probabilistic vector of our CE-VADER model (denoted as INT(·)) i.e.,

<!-- b000254 | prose | pages [10] -->
INT(R) := softmax(λCE(R) + (1 −λ)V ADER(R)) (10)

<!-- b000255 | prose | pages [10] -->
where lambda is the fused coefﬁcient, in this literature we set λ = 0.5 to equally weigh the outcome of the two blocks. We employ softmax(·) as our smoothing function, which is deﬁned by:

<!-- b000256 | prose | pages [10] -->
1 i=1 exi (ex1, ex2, · · · , exs) softmax(x1, x2, · · · , xs) = (11) Ps

<!-- b000257 | prose | pages [10] -->
As our empirical results show after smoothing, the intensity vector will show a strong consis- tency to the star-rating.

<!-- b000258 | prose | pages [10] -->
The sentiment classiﬁcation result of the proposed CE-VADER on the review R is the group name of Gj associated with the component of INT(R) = (int1 R, · · · , int5 R) with the largest value, formulated by j0 = argmaxj{intj R}, with its corresponding intensity intj0 R.

<!-- b000259 | furniture | pages [10] -->
关注数学模型

<!-- b000260 | furniture | pages [10] -->
2

<!-- b000261 | furniture | pages [10] -->
MATHmodels

<!-- b000262 | furniture | pages [10] -->
获取更多资讯

<!-- b000263 | furniture | pages [11] -->
Team # 2002116

<!-- b000264 | furniture | pages [11] -->
Page 10 of 38

<!-- b000265 | heading | pages [11] -->
3.3 Combination of Text-Based and Rating-Based Measures

<!-- b000266 | prose | pages [11] -->
The unique review id is denoted as id. Review headline Rhid, review body Rbid, star rating sid, review date rdid, helpful votes hvid, product title ptid, product id pid ∈{B, M, H} (B, M, H stand for baby paciﬁer, microwave, and hair dryer respectively) are all associated with the subscript review id. Due to the strong relevant relationship (difference occurs lease than 0.01% in total) between product title, product parent and product id, namely, once one of them is given we can almost uniquely tell the other two, we only use the product title to depicts the product in this literature. We do not take the marketplace into account, since all of them are from the US. Denote the pair P(id) = (Rid, sid, hvid, rdid, ptid, pid), where Rid = (Rhid, Rbid) is the whole review text including the headline and body.

<!-- b000267 | prose | pages [11] -->
We propose the importance rate (denoted as IMP) of each review by taking its helpful votes, correspondence between the star-rating measure VEC(sid) and the text-based measure INT(Rid, review text clarity. It is deﬁned by the following formula.

<!-- b000268 | prose | pages [11] -->
5 INT(Rid) · VEC(sid) X IMP(id) := (1 + hvid) · exp[−α(1 − inti Rlog(inti ∥INT(Rid)∥∥VEC(sid)∥)] · exp[β( R))] (12) i=1

<!-- b000269 | prose | pages [11] -->
INT(Rid)·VEC(sid) Where the 1− ∥INT(Rid)∥∥VEC(sid)∥is the cosine distance between text-based measure and rating- based measure, calculating the ﬁdelity of correspondence between two, α > 0 is its associated weight. −P5 i=1 inti Rlog(inti R) is the entropy of the text context, the low the more clarity, β > 0 is the associated weight. The higher the importance, the more informative the review text and the rating are.

<!-- b000270 | caption | pages [11] -->
Figure 4: Implemented our proposed model on "Hair dryer" data set. We demonstrate the dis-

<!-- b000271 | prose | pages [11] -->
tribution of the top 1% most informative reviews and associated ratings generated by different parameters (α, β). The longer the liner, the more informative our model indicates. The settings of (α, β) are: a)(1,1); b)(1,3); c)(1,5); d)(2,1); e)(4,1); f)(5,5). As depicted in the ﬁgure, our model shows robustness on the two parameters.

<!-- b000272 | furniture | pages [11] -->
关注数学模型

<!-- b000273 | furniture | pages [11] -->
2

<!-- b000274 | furniture | pages [11] -->
MATHmodels

<!-- b000275 | furniture | pages [11] -->
获取更多资讯

<!-- b000276 | furniture | pages [12] -->
Team # 2002116

<!-- b000277 | furniture | pages [12] -->
Page 11 of 38

<!-- b000278 | heading | pages [12] -->
3.4 Model Implementation, Sensitivity Analysis and Results

<!-- b000279 | prose | pages [12] -->
We implement our proposed model for the given data. We set the parameter σ0 = 1 in Eq.(1). The model proposed in section 3.3 contains two parameters α,β. We ﬁrst analyze the sensitivity of these two parameters.

<!-- b000280 | prose | pages [12] -->
As shown in Figure 4, we implemented our proposed model on "Hair dryer" data set, the top 1% most informative reviews indicated by our model show strong robustness on two pa- rameters α and β. We also employ the DTW similarity to quantify the robustness of our model on two parameters, as shown in Figure 5. The smaller DTW similarity, the more similar two rankings are. Readers are referred to ref.[9] for more details about the DTW similarity. We set α1 = 1, β = 1 as the baseline and calculate the DTW similarity, the maximum is 14.3, which is a small value in the case of 11470 pieces of reviews. Again, our model shows a strong robustness of α and β.

<!-- b000281 | prose | pages [12] -->
Top 1% most informative reviews and the associated ratings listed by their rankings of three kinds of products are attached to Appendix C.

<!-- b000282 | prose | pages [12] -->
=10, =10 =1, =1 =1, =3 =1, =5 =2, =1 =2, =3 =3, =4 =4, =1 =5, =5 =5, =7 16 0.0 6.9 6.9 11.6 9.8 11.3 11.4 13.0 13.7 14.3 =1, =1 14 6.9 0.0 5.7 10.9 11.3 9.5 11.5 11.5 12.0 13.6 =1, =3 6.9 5.7 0.0 11.7 12.3 11.0 12.4 12.2 13.0 16.0 =1, =5 12 11.6 10.9 11.7 0.0 7.5 9.3 9.7 10.3 10.3 13.1 =2, =1 10 DTW similarity 9.8 11.3 12.3 7.5 0.0 9.8 11.0 10.9 11.3 12.9 =2, =3 8 11.3 9.5 11.0 9.3 9.8 0.0 9.2 9.7 10.2 11.8 =3, =4 6 11.4 11.5 12.4 9.7 11.0 9.2 0.0 8.3 10.2 11.1 =4, =1 13.0 11.5 12.2 10.3 10.9 9.7 8.3 0.0 4.0 10.7 =5, =5 4 13.7 12.0 13.0 10.3 11.3 10.2 10.2 4.0 0.0 10.3 =5, =7 2 14.3 13.6 16.0 13.1 12.9 11.8 11.1 10.7 10.3 0.0 =10, =10 0

<!-- b000283 | caption | pages [12] -->
Figure 5: DTW similarity of our model implemented on "Hair dryer" data set with different

<!-- b000284 | prose | pages [12] -->
value of α and β. We set α = 1, β = 1 as the baseline. The maximum similarity is 14.3 which is a small value considering our case of 11470 total reviews. It shows the robustness of our model.

<!-- b000285 | heading | pages [12] -->
4 Difference Equation to Measure Time-Based Pattern

<!-- b000286 | prose | pages [12] -->
In this section, we construct a difference equation based model to formulate the change of product’s reputation. The rest of this section is arranged as follows. In section 4.1, we detailedly formulated our model. In section 4.2, we analyze the model sensitivity and implement the model on three kinds of products.

<!-- b000287 | heading | pages [12] -->
4.1 Difference Equation Based Model

<!-- b000288 | prose | pages [12, 13] -->
We propose the "reputation" to formulate the reputation of product P around time T. Denote reputation as REP. However, we assume that the reputation of products will change gradually by buyer’s review text and the star rates. We will employ a difference equation to formulate the reputation. The difference of the reputation (i.e., the growth rate of the reputation) can be formulated as follows.

<!-- b000289 | furniture | pages [12] -->
关注数学模型

<!-- b000290 | furniture | pages [12] -->
2

<!-- b000291 | furniture | pages [12] -->
MATHmodels

<!-- b000292 | furniture | pages [12] -->
获取更多资讯

<!-- b000293 | furniture | pages [13] -->
Team # 2002116

<!-- b000294 | furniture | pages [13] -->
Page 12 of 38

<!-- b000296 | prose | pages [13] -->
∆REPt0,θ(T, P) := 1 X IMP(id) · (θsid + (1 −θ)argmaxj{intj Rid} −3) 2z( (13) T−t0≤rdid≤T,pid=P

<!-- b000297 | prose | pages [13] -->
where Z is the normalization constant deﬁned by:

<!-- b000298 | prose | pages [13] -->
X IMP(id) Z = (14) T−t0≤rdid≤T,pid=P

<!-- b000299 | prose | pages [13] -->
For the sake of simplicity, we normalize the value of ∆REPt0,θ(T, P) to [−1, 1], with negative value associated with the negative feels or one-star and two-star ratings while the positive value with the positive feels or four-star or ﬁve-star ratings.

<!-- b000300 | prose | pages [13] -->
Parameter θ0 ∈[0, 1] is the weight coefﬁcient for the star rating and the text-based measure by our proposed CE-VADER model in section 3.2. We hold the assumption that it takes some time for shipping the product and some customers prefer making review sometime later after purchasing. Hence, we consider all id satisfying T −t0 ≤rdid ≤T as the time tag, where t0 is a threshold. Note that buyers have almost 90 days to leave feedback, hence t0 ≤90. In this literature, we set θ = 0.5 for the equal weight of star rate and the review context. And we set t0 = 10 is this literature. Then, the reputation can be formulated by the following difference equation:

<!-- b000301 | prose | pages [13] -->
REPt0,θ(T, P) −REPt0,θ(T −1, P) = ∆REPt0,θ(T, P) −PEN(T, P) (15) Where the PEN(T, P) is the penalty factor formulates how much the low-star rating or negative reviews destroys the reputations as we assume buyers pay more attention to those negative comments. It is formulated as follows.

<!-- b000302 | prose | pages [13] -->
PEN(T, P) = k2 × sigmoid(k1 × REPt0,θ(T −1, P)) × #{id|θsid + (1 −θ)argmaxj{intj Rid} ≤k3} #{id|T −t0 ≤rdid ≤T, pid = P} (16) k1, k2, k3 are the thresholds for the penalty factor. We set k3 = 2 as the threshold to quantify #{id|θsid+(1−θ)argmaxj{intj Rid}≤k3} the "negative comments". Hence, is the propagation of "negative #{id|T−t0≤rdid≤T,pid=P} 1 1+e−x ∈[0, 1]. We set the sigmoid items to comments". The sigmoid is deﬁned by sigmoid(x) = intimate the social behavior that once a product wins a good reputation, people will put more emphasis on the "negative comments". k2 values how much the penalty factor is comparing with the growth rate i.e., ∆REP.

<!-- b000303 | heading | pages [13] -->
4.2 Model Implementation, Sensitivity Analysis and Results

<!-- b000304 | prose | pages [13] -->
As the construction of our model in 4.1, there are two tunable parameters i.e., k1, k2. We implement our proposed model on the data of three types of products. And show the sensitivity of our model on these two parameters.

<!-- b000305 | caption | pages [13] -->
Figure 6 depicts the reputation curve with the parameter settings of k1 = 0.5 and k2 = 20.

<!-- b000306 | prose | pages [13, 14] -->
As shown, "microwave" owns a bad reputation for the negative valued reputation rate; while "paciﬁer" wins a good reputation. None of the products have a steady or monotonic growth or a hair dryer 100 microwave pacifier 80

<!-- b000307 | furniture | pages [13] -->
关注数学模型

<!-- b000308 | furniture | pages [13] -->
2

<!-- b000309 | furniture | pages [13] -->
MATHmodels

<!-- b000310 | furniture | pages [13] -->
获取更多资讯

<!-- b000311 | furniture | pages [14] -->
Team # 2002116

<!-- b000312 | furniture | pages [14] -->
Page 13 of 38

<!-- b000314 | prose | pages [14] -->
60 Reputation 40

<!-- b000315 | prose | pages [14] -->
20

<!-- b000316 | prose | pages [14] -->
0

<!-- b000317 | prose | pages [14] -->
20

<!-- b000318 | prose | pages [14] -->
time axis

<!-- b000319 | caption | pages [14] -->
Figure 6: The reputation curve of products with k1 = 0.5 and k2 = 20.

<!-- b000320 | prose | pages [14] -->
decline in reputation rate. Then, we analyze the sensitivity of our model on the two parameters i.e., k1 and k2. Our model shows extremely strong robustness on k1 and a gentle sensitivity on k2 in Figure 7. As depicted in Figure 7-B, different settings of k2 will lead to a different growth rate of the reputation rate on the data of "paciﬁer", but sharing the same tendency. But, the small value of k2 will lead to an exponential large reputation growth rate. As we have discussed before, the small setting of k2 indicates less attention to negative comments.

<!-- b000321 | prose | pages [14] -->
A B

<!-- b000322 | caption | pages [14] -->
Figure 7: Sensitivity analysis of the parameters k1 and k2. A)Our model shows extreme strong

<!-- b000323 | prose | pages [14] -->
robustness on k1. B)Our model shows sensitivity on k2.

<!-- b000324 | furniture | pages [14] -->
关注数学模型

<!-- b000325 | furniture | pages [14] -->
2

<!-- b000326 | furniture | pages [14] -->
MATHmodels

<!-- b000327 | furniture | pages [14] -->
获取更多资讯

<!-- b000328 | furniture | pages [15] -->
Team # 2002116

<!-- b000329 | furniture | pages [15] -->
Page 14 of 38

<!-- b000330 | heading | pages [15] -->
5 Predict Potential Success or Failure

<!-- b000331 | prose | pages [15] -->
In the last section, we construct a mapping REPt0θ : [T0, T1]×{B, M, H} →R+ where [T0, T1] is the time range of the given review date. In this section, we will employ time series forecasting method to predict the value of REPt0θ on extended future domain, namely [T1, T2] × {B, M, H} for some T2 > T1 in section 5.1. Based on the forecasted REPt0θ in the future time domain, we will evaluate the success or failure potential of each product in 5.2. We show the results on the real data and predicted their potential success or failure in section 5.3.

<!-- b000332 | heading | pages [15] -->
5.1 Time Series Forecasting for Predicting Future Reputation

<!-- b000333 | prose | pages [15] -->
We employ an auto regressive model (AR) as the time series forecasting to predict future growth or the decline of the reputation rate. The AR model can be depicted by the following difference equation.

<!-- b000334 | prose | pages [15] -->
p X REPt0,θ(T, P)) = a0 + akREPt0,θ(T −k, P)) + εT (17) k=1

<!-- b000335 | prose | pages [15] -->
where εT is the white noise. AR model goes to search the coefﬁcient (a0, a1, · · · , ap) in Eq.(17) to ﬁt the given data in the time domain [T0, T1] with the least root mean square error (RMSE).

<!-- b000336 | heading | pages [15] -->
5.2 Evaluating the Success or Failure potential

<!-- b000337 | prose | pages [15] -->
We deﬁne the average reputation of product P from T0 to T1 as:

<!-- b000338 | prose | pages [15] -->
Z T1 1 REPT0T1 REPt0,θ(T, P)dT t0,θ (P) := (18) T1 −T0 T0

<!-- b000339 | prose | pages [15] -->
Similarly, we can deﬁne the predicted average reputation of product P in the future time do- main [T1, t] for t < T2 based on the model constructed in section 5.1 as follows.

<!-- b000340 | prose | pages [15] -->
Z t 1 REPT1t REPt0,θ(T, P)dT t0,θ(P) := (19) t −T1 T1

<!-- b000341 | prose | pages [15] -->
The ration of the calculated average reputation by the given data and the predicted average reputation from Eq. (18) and Eq. (18) is deﬁned as the reputation change rate. It is deﬁned as:

<!-- b000342 | prose | pages [15] -->
γ(t, P) := REPT1t t0,θ(P)/REPT0T1 t0,θ (P) (20)

<!-- b000343 | prose | pages [15] -->
We propose a fuzzy evaluation system for predicting the success or the failure of the product P. The overall architecture of the system is depicted in Figure 8. We category the outcome into four classes, namely "strong success", "weak success", "weak failure", "strong failure".

<!-- b000344 | heading | pages [15] -->
5.3 Model Implementation and Results

<!-- b000345 | prose | pages [15] -->
We implement our model to the given data with p = 50 in Eq.(17). We set 3 4 of the data in given time domain ([T0, T1]) i.e., [T0, 3 4T1 + 1 4T0] to ﬁt the regression coefﬁcients (a0, a1, · · · , ap).

<!-- b000346 | furniture | pages [15] -->
关注数学模型

<!-- b000347 | furniture | pages [15] -->
2

<!-- b000348 | furniture | pages [15] -->
MATHmodels

<!-- b000349 | furniture | pages [15] -->
获取更多资讯

<!-- b000350 | furniture | pages [16] -->
Team # 2002116

<!-- b000351 | furniture | pages [16] -->
Page 15 of 38

<!-- b000352 | prose | pages [16] -->
F T > 0 ? 𝜸𝒕> 𝟎?

<!-- b000353 | prose | pages [16] -->
F T F 𝜸𝒕> 𝟎?

<!-- b000354 | prose | pages [16] -->
T T T |𝜸𝒕| > 𝟏? |𝜸𝒕| > 𝟏?

<!-- b000355 | prose | pages [16] -->
F F

<!-- b000356 | prose | pages [16] -->
Success Weak Failure Weak Success Strong Failure

<!-- b000357 | caption | pages [16] -->
Figure 8: The overall architecture of our proposed fuzzy evaluation system for predicting the

<!-- b000358 | prose | pages [16] -->
potential success or the failure of each product.

<!-- b000359 | prose | pages [16] -->
The latter 1 4 to evaluate the AR model i.e., on the time domain [3 4T1 + 1 4T0, T1]. In the evaluation domain, we ﬁnd the model can ﬁt and predict the "reputation" rate surprisingly well, with the maximum RMSE rate of 0.031. We evaluate the potential success or failure on the domain [T1, T2] with T2 −T1 = 1 2(T1 −T0). The predicted reputation rates of paciﬁer, microwave and hair dryer are shown in Figure 9,10,11 respectively. They are predicted to be "weak success", "strong failure" and "strong failure" based on the proposed framework in section 5.2.

<!-- b000360 | caption | pages [16] -->
Figure 9: Model implementation on "paciﬁer" data. Predicted to be a weak success.

<!-- b000361 | heading | pages [16] -->
6 Speciﬁc Ratings and Descriptors Analysis

<!-- b000362 | prose | pages [16] -->
In this section, we analyze the speciﬁc ratings and descriptors repetitively in section 6.1 and section 6.2.

<!-- b000363 | furniture | pages [16] -->
关注数学模型

<!-- b000364 | furniture | pages [16] -->
2

<!-- b000365 | furniture | pages [16] -->
MATHmodels

<!-- b000366 | furniture | pages [16] -->
获取更多资讯

<!-- b000367 | furniture | pages [17] -->
Team # 2002116

<!-- b000368 | furniture | pages [17] -->
Page 16 of 38

<!-- b000369 | caption | pages [17] -->
Figure 10: Model implementation on "microwave" data. Predicted to be a strong failure.

<!-- b000370 | caption | pages [17] -->
Figure 11: Model implementation on "hair dryer" data. Predicted to be a strong failure.

<!-- b000371 | heading | pages [17] -->
6.1 Speciﬁc Star Ratings Relevance to Rating Frequency

<!-- b000372 | prose | pages [17] -->
In this section, we ﬁrst analyzed the relationship between the speciﬁc star-rating with the reputation rate i.e., strong negative cases of one-star rating and strong positive case of ﬁve-star rating. We employ our propose reputation rate as the text-based measure. As shown in Figure 12, we can observe that the growth in the ﬁve-star rating proportion leads to an instant increase in the "reputation" rate. While after the peak of the ﬁve-star rating proportion, the reputation rate decay immediately. The growth of the reputation rate is also strongly associated with the decline of the one-star rating proportion.

<!-- b000373 | prose | pages [17] -->
Then, we evaluate the correlation between star-ratings to the helpful votes in Figure 13. Once again, the ﬁve-star rating shows a much strong correlation to the helpful votes than the other four ratings among all types of the data i.e., baby paciﬁers, microwaves and hair dryers.

<!-- b000374 | prose | pages [17] -->
Moreover, researches in previous work [10] have also pointed out that people perceive ex- treme cases among all online comments (both positive and negative)as more useful information instead of the moderate ones e.g., the review text classiﬁed as "strong positive" or "strong neg- ative" and the one-star or ﬁve-star rate in our issue.

<!-- b000375 | prose | pages [17, 18] -->
Hence, in this literature, we would like to lay our emphasis on the impact of extreme ratings tion. The blue line indicates the reputation time series, the green line for the ﬁve-star rating proportion and the orange line for the one-star rating proportion. Red circles highlight typical examples that a higher percentage of ﬁve-star rating leads instant an increase in the reputation rate while one-star rating leads drop.

<!-- b000376 | furniture | pages [17] -->
关注数学模型

<!-- b000377 | furniture | pages [17] -->
2

<!-- b000378 | furniture | pages [17] -->
MATHmodels

<!-- b000379 | furniture | pages [17] -->
获取更多资讯

<!-- b000380 | furniture | pages [18] -->
Team # 2002116

<!-- b000381 | furniture | pages [18] -->
Page 17 of 38

<!-- b000382 | caption | pages [18] -->
Figure 12: Correlation between the "reputation" rate and one-star or ﬁve-star rating propor-

<!-- b000384 | prose | pages [18] -->
i.e., the one-star and ﬁve-star rating rather than two to four stars’ rates based on the above mentioned three facts.

<!-- b000385 | prose | pages [18] -->
Baby pacifier Two-star Microwave Hair dryer

<!-- b000386 | prose | pages [18] -->
Three-star

<!-- b000387 | prose | pages [18] -->
12000 8000 10000 4000 6000 2000 One-star

<!-- b000388 | prose | pages [18] -->
Four-stars

<!-- b000389 | prose | pages [18] -->
Five-star

<!-- b000390 | caption | pages [18] -->
Figure 13: Correlation between the star ratings with the helpful votes. Reviews associated with

<!-- b000391 | prose | pages [18] -->
ﬁve-star ratings are always voted as helpful.

<!-- b000392 | prose | pages [18, 19] -->
By verifying the pattern of review text word-frequency related to products rated as one or ﬁve stars we ﬁnd that consumers are less likely to purchase those products associated with low- star ratings and are more delighted to buy those with high-star ratings. We take a speciﬁc case of the consecutive occurrence of x reviews associated with one-star or ﬁve-star rates presented to people as the baseline with x = 10 for hairdryer, paciﬁer, and x = 5 for microwave. Due to the low percentage of ﬁve-star rating and the bad reputation it has (as we have previously discussed in section 4.2) the microwave compared to the other two cases, we set the x = 5 for it speciﬁcally for the low ﬁve-star rating proportion. Our empirical results show that a smaller x leads to a higher frequency while a bigger one leads to the lower frequency. For the sake of simplicity, we set a moderate x as mentioned above.

<!-- b000393 | furniture | pages [18] -->
关注数学模型

<!-- b000394 | furniture | pages [18] -->
2

<!-- b000395 | furniture | pages [18] -->
MATHmodels

<!-- b000396 | furniture | pages [18] -->
获取更多资讯

<!-- b000397 | furniture | pages [19] -->
Team # 2002116

<!-- b000398 | furniture | pages [19] -->
Page 18 of 38

<!-- b000400 | prose | pages [19] -->
As shown in Table 2, more reviews were incited after the consecutive occurrence of ﬁve- star ratings in both cases of owning a good or bad reputation (reputation is formulated by our model in section 4). It suggests that people are much more willing to rate the products after seeing a consecutive occurrence of high-star ratings. while after the consecutive occurrence of one-star ratings, people were less incited to rate in the case of products with bad reputation i.e., microwave and hair dryer. People were strongly incited to rate the products with a good reputation on seeing the consecutive occurrence of one-star ratings.

<!-- b000401 | caption | pages [19] -->
Table 2: Comparison between rating frequency with a series of extreme ratings cases, overall

<!-- b000402 | prose | pages [19] -->
rating frequency and the average reputation of a baby paciﬁer, microwave, and hair dryer data. The smaller the frequency, the more frequent buyers rate the products. The consecutive occur- rence of ﬁve-star ratings always incites people to rate. The consecutive occurrence of one-star ratings of bad-reputation products leads to a much lower rate frequency while strongly incited people to vote for the good-reputation products.

<!-- b000403 | prose | pages [19] -->
Rating Frequency Rating Frequency Overall after a Series of after a Series of Product Reputation Rating Frequency(day) Five-star Ratings(day) One-star Ratings(day) 1.9444 1.56000 2.37828 Baby paciﬁer good 8.66667 30.61904 24.39975 Microwave bad 1.58207 16.37500 4.29293 Hair dryer bad

<!-- b000404 | caption | pages [19] -->
Figure 14 indicates the total number of monthly star ratings and the number of one-star and

<!-- b000405 | prose | pages [19] -->
ﬁve-star ratings when the total number of ratings changed signiﬁcantly on the hair dryer from August 31, 2012, to August 31, 2015. We can observe that the concentration of ﬁve-star ratings is always associated with an increase in the total number of ratings, while a series of one-star ratings lead to a decline.

<!-- b000406 | heading | pages [19] -->
6.2 Speciﬁc Quality Descriptors’ Relevance to Rating Levels

<!-- b000407 | heading | pages [19] -->
6.2.1 Naive Bayesian Model for Evaluation

<!-- b000408 | prose | pages [19] -->
Some words are often strongly associated with the emotional feeling which leads to differ- ent rating levels as e.g., "enthusiastic" with positive and delighted feeling may lead to higher stars’ rating and “disappointed” with negative feelings. In this section, we employ the Naïve Bayesian Model to identify how the speciﬁc word is associated with the rating levels. The Naïve Bayesian distribution probability of star-rating s of speciﬁc word w is depicted as follows:

<!-- b000409 | prose | pages [19] -->
P(s|w) = P(w|s)P(s) (21) P(w)

<!-- b000410 | prose | pages [19] -->
By evaluating the probability P(s|w), we can measure the correlation between speciﬁc word w and star rate s.

<!-- b000411 | furniture | pages [19] -->
关注数学模型

<!-- b000412 | furniture | pages [19] -->
2

<!-- b000413 | furniture | pages [19] -->
MATHmodels

<!-- b000414 | furniture | pages [19] -->
获取更多资讯

<!-- b000415 | furniture | pages [20] -->
Team # 2002116

<!-- b000416 | furniture | pages [20] -->
Page 19 of 38

<!-- b000417 | prose | pages [20] -->
10 500

<!-- b000418 | prose | pages [20] -->
Overall star ratings Five-star ratings 8 400 One-star ratings

<!-- b000419 | prose | pages [20] -->
6 300

<!-- b000420 | prose | pages [20] -->
200 4

<!-- b000421 | prose | pages [20] -->
100 2

<!-- b000422 | prose | pages [20] -->
0 8/31/2012 8/31/2013 8/31/2014 8/31/2015 time axis

<!-- b000423 | caption | pages [20] -->
Figure 14: A representative example showing the correlation between the one-star rates or ﬁve-

<!-- b000424 | prose | pages [20] -->
star rates with the overall star ratings on hair dryer data from August 31, 2012, to August 31, 2015.

<!-- b000425 | heading | pages [20] -->
6.2.2 Model Implementation and Results

<!-- b000426 | prose | pages [20] -->
The higher P(s|w), the stronger correlation of word s and star rating s. With provided the massive data, we use the frequency to approximate the probability in Eq. (21) i.e.,p(s) = #{id|sid=s} . We demonstrated the top ten words associated with ﬁve-star ratings and one-star #{id} ratings respectively in Table 3.

<!-- b000427 | caption | pages [20] -->
Table 3: top ten words associated to ﬁve-star ratings and one-star ratings respectively.

<!-- b000428 | prose | pages [20] -->
Words strongly Words strongly P(s = 5|w) P(s = 1|w) associated with associated with 5-star rating 1-star rating 0.8518 0.1416 easy or 0.8333 0.1434 popcorn out 0.7809 0.1483 love not 0.7778 0.1513 feature no 0.7692 0.1546 button back 0.7685 0.1718 great hot 0.7452 0.1759 much because 0.7250 0.1940 high months 0.7200 0.2083 can off 0.7196 0.2125 also dryer

<!-- b000429 | furniture | pages [20] -->
关注数学模型

<!-- b000430 | furniture | pages [20] -->
2

<!-- b000431 | furniture | pages [20] -->
MATHmodels

<!-- b000432 | furniture | pages [20] -->
获取更多资讯

<!-- b000433 | furniture | pages [21] -->
Team # 2002116

<!-- b000434 | furniture | pages [21] -->
Page 20 of 38

<!-- b000435 | heading | pages [21] -->
7 Attractiveness Analysis of Design Features

<!-- b000436 | prose | pages [21] -->
In this section, we extract keywords describing the performance, appearance, etc. of the baby paciﬁer, microwave and hair dryer from the top 1% most informative reviews. By cal- culating the frequency of these keywords in all reviews and analyzing the content of the top 1% most informative reviews, we inform some design features attractive to consumers, and the groups of keywords and number of keyword occurrences are present in Appendix B.

<!-- b000437 | prose | pages [21] -->
1. Baby paciﬁer: Size, appearance, convenience, and safety of baby paciﬁers are most con- cerned by consumers according to Table 4. People are more concerned about whether it is suitable and safe for babies, so various alternatives of size and safe materials are neces- sary. Besides, cute patterns are popular with babies.

<!-- b000438 | prose | pages [21] -->
2. Microwave: Appearance, price, and component of microwaves are most concerned by consumers according to Table 5, which shows that people focus on the cost performance of the microwave. Many reviews welcome the multifunctional but expensive microwave.

<!-- b000439 | prose | pages [21] -->
People prefer to get as many features as possible when the product costs a lot, such as rotating grills, accurate timers, and multiple usage patterns.

<!-- b000440 | prose | pages [21] -->
3. Hair dryer: Power and appearance of the hair dryer are most concerned by consumers according to Table 6, indicating that consumers prefer a portable hair dryer with high power. Simultaneously, safety and working volume affect the user experience, making it signiﬁcant for Sunshine Company to maintain the balance between increased power a safe and quiet operating environment. In particular, some special designs may stimulate consumers to buy, e.g. a folding handle can improve the portability of the hair dryer.

<!-- b000441 | heading | pages [21] -->
8 Sales Strategies and Recommendations

<!-- b000442 | prose | pages [21] -->
In this section, we propose conﬁdent online marketing strategies and recommendations for Sunshine Company based on results generated in previous sections for three precise products: baby paciﬁer, microwave and hair dryer. Our most conﬁdent recommendations including the speciﬁc justiﬁcations (to the Sunshine Company) are listed as follows:

<!-- b000443 | prose | pages [21] -->
• (General recommendations) Reviews with high helpful votes and associated with strong feelings are often informative ones. Collect those reviews and star ratings in real-time.

<!-- b000444 | prose | pages [21] -->
Pay attention to text-based reviews equally as the star ratings.

<!-- b000445 | prose | pages [21] -->
• (General recommendations) Always keep high proportion ﬁve-star ratings, as it is strongly associated with the reputation of the products.

<!-- b000446 | prose | pages [21] -->
• (General recommendations) Lay more emphasis on the negative reviews or ones associ- ated with low-star ratings if the products have a bad reputation e.g. high proportion of low-star ratings. And make feedbacks and adjustments immediately, as those reviews or ratings will keep ruining the reputation of the product. Most people who rate one-star state that they will update my review once they have heard or not head from the com- pany. Around 30% of one-star ratings are associated with the untimely warranty service or feedback from the companies.

<!-- b000447 | furniture | pages [21] -->
关注数学模型

<!-- b000448 | furniture | pages [21] -->
2

<!-- b000449 | furniture | pages [21] -->
MATHmodels

<!-- b000450 | furniture | pages [21] -->
获取更多资讯

<!-- b000451 | furniture | pages [22] -->
Team # 2002116

<!-- b000452 | furniture | pages [22] -->
Page 21 of 38

<!-- b000453 | prose | pages [22] -->
• (Speciﬁc justiﬁcation for hair dryer) The condition for the hair dryer seems to be poor.

<!-- b000454 | prose | pages [22] -->
From the top 100 most informative review we evaluated, 13 reviews have reported a case of smoking or throwing out sparks or breaking down, which may lead to some danger.

<!-- b000455 | prose | pages [22] -->
Due to the decreasing reputation of the hair dryer, we recommend you do not put hair dryers into the market until its reputation increases, which is beneﬁcial for the smooth start of the product.

<!-- b000456 | prose | pages [22] -->
• (Speciﬁc justiﬁcation for microwave) Microwave has the worst reputation among all of the three products. It has the highest percentage of one-star ratings and strong negative reviews. Among the top 100 most informative reviews, people have widely complained about the bad condition, the potential danger of catching ﬁre. Our model suggests its potential failure. Hence, we recommend that wait until the reputation of microwaves recovers and remains stable.

<!-- b000457 | prose | pages [22] -->
• (Speciﬁc justiﬁcation for paciﬁer) Paciﬁer has a good reputation, with the highest propor- tion of positive reviews and ﬁve-star ratings. It is also predicted to be a success by our model, so it’s good timing to put it into the market. However, among the top 1% most informative reviews, they have reported cases of leaking water. Companies should pay attention to the connection or the joint part.

<!-- b000458 | prose | pages [22] -->
• (General recommendations) As low-cost products, paciﬁers, microwave and hair dryer have low professional requirements on consumers at the same time. The more complete the product information is, the less loss will be caused by the unequal information be- tween buyers and sellers. Of course, the authenticity of the information needs to be guar- anteed.

<!-- b000459 | prose | pages [22] -->
• (General recommendations) Our results indicate that a series of ﬁve-star ratings can incite consumer reviews. Therefore, we recommend that you increase your promotional efforts when there are more ﬁve-star ratings of your products to form positive feedback.

<!-- b000460 | prose | pages [22] -->
• (General recommendations) Creative and engaging advertising will increase product sales.

<!-- b000461 | prose | pages [22] -->
The online marketplace makes it easier for consumers to browse multiple alternatives of the commodity, which leads to ﬁerce competition among companies. Designing inter- esting and eye-catching advertisements can effectively enhance the competitiveness of products, so Sunshine Company should make the appropriate investments in advertising to make more proﬁt. Top 1% of most informative reviews suggest some consumers pay much attention to the company websites.

<!-- b000462 | heading | pages [22] -->
9 Strengths and Weaknesses

<!-- b000463 | heading | pages [22] -->
9.1 Strengths

<!-- b000464 | prose | pages [22] -->
1. Novelty. To the best of our knowledge, we are the ﬁrst to propose a CE-VADER hybrid model for review text-based sentiment evaluations on an online marketplace.

<!-- b000465 | prose | pages [22] -->
2. Accuracy. The maximum RMSE of the 50 order AR model is 0.031 on the validation time domain. The text-based measures correlate well with the rating-based measures.

<!-- b000466 | furniture | pages [22] -->
关注数学模型

<!-- b000467 | furniture | pages [22] -->
2

<!-- b000468 | furniture | pages [22] -->
MATHmodels

<!-- b000469 | furniture | pages [22] -->
获取更多资讯

<!-- b000470 | furniture | pages [23] -->
Team # 2002116

<!-- b000471 | furniture | pages [23] -->
Page 22 of 38

<!-- b000472 | heading | pages [23] -->
3. Generalization. Our proposed framework can freely be implemented to any data set e.g.,

<!-- b000473 | prose | pages [23] -->
reviews and star-ratings of any products from any online platforms.

<!-- b000474 | heading | pages [23] -->
4. Robustness. Our model shows great robustness to most of the parameters.

<!-- b000475 | heading | pages [23] -->
9.2 Weaknesses

<!-- b000476 | heading | pages [23] -->
1. Time consuming manual annotations. Annotating the seed words generated from re-

<!-- b000477 | prose | pages [23] -->
views for CE-VADER model manually is time-consuming.

<!-- b000478 | heading | pages [23] -->
2. CE-VADER model can not identify different forms of the same word with special vari-

<!-- b000479 | prose | pages [23] -->
ation rules. CE-VADER model cannot identify the past form of verbs, plural of nouns and comparative forms of adjectives with special variation e.g., is (v.s. was), children (v.s.

<!-- b000480 | prose | pages [23] -->
child) and better (v.s. good).

<!-- b000481 | heading | pages [23] -->
3. Missing other potentially relevant factors. We do not take marketing strategies of Amazon-

<!-- b000482 | prose | pages [23] -->
like sales promotion into consideration when analyzing speciﬁc ratings and descriptors.

<!-- b000483 | heading | pages [23] -->
10 Conclusion

<!-- b000484 | prose | pages [23] -->
To crack the secret of Amazon’s ratings and reviews, we proposed a series of novel models to address the sub-issues from selecting the most informative reviews to identifying reviews’ quality descriptors. The proposed model achieves high accuracy and robustness.

<!-- b000485 | prose | pages [23] -->
1. Information Evaluation Model can combine the text-based measure with the rating-based measure, where we propose a novel CE-VADER hybrid model for the sentiment analy- sis as the text-based measure. We can rank how informative each review and the rat- ing is with the proposed model. The informative rate correlates to the helpful votes. To be more speciﬁc, the more help votes there the more ﬁve-star ratings they own and the longer review bodies are, the more likely they are evaluated as informative reviews. How- ever, PLEASE REMEMBER that moderately-rated reviews with high information entropy, which have both positive and negative comments, marked by words like ”however” and “but” also have great reference value.

<!-- b000486 | prose | pages [23] -->
2. We employ the Difference Equation Model to construct a “reputation rate” to quantify the reputation of three products, namely baby paciﬁer, microwave and hair dryer. Baby paci- ﬁer has a positive reputation, hair dryer has a weak negative one, and the microwave has the worst reputation. With a modiﬁed AR algorithm, we predicted the future reputation tendency of these three products.

<!-- b000487 | prose | pages [23] -->
3. In analyzing the distribution of star ratings and speciﬁc words, we identiﬁed special re- view descriptors by employing a continuous extreme rating and a set of special words.

<!-- b000488 | prose | pages [23] -->
Continuous extreme ratings can obviously affect the total sale volume and special words’ appearance can judge the rating of reviews with high probability.

<!-- b000489 | heading | pages [23] -->
11 A Letter to the Marketing Director of Sunshine Company

<!-- b000490 | furniture | pages [23] -->
关注数学模型

<!-- b000491 | furniture | pages [23] -->
2

<!-- b000492 | furniture | pages [23] -->
MATHmodels

<!-- b000493 | furniture | pages [23] -->
获取更多资讯

<!-- b000494 | furniture | pages [24] -->
Team # 2002116

<!-- b000495 | furniture | pages [24] -->
Page 23 of 38

<!-- b000496 | prose | pages [24] -->
Dear Marketing Director of Sunshine Company, According to your requirements, we analyze the ratings and reviews of competitive prod- ucts on Amazon for baby paciﬁer, microwave and hair dryer to be introduced and sold by your company. We form three models dubbed as Informative Evaluation Model to assess the amount of information of each review, Difference Equation Based Model to formulate the change of product’s reputation and Time Series Forecasting Based Evaluation Model to predict potential success or failure of the product. And we get some meaningful results, which contribute to attract consumers and develop adaptable online sales strategies.

<!-- b000497 | prose | pages [24] -->
First of all, We construct the Informative Evaluation Model to help you track informative reviews and ratings conveniently. This model can assess whether each review is informative based on star rating, review text, and helpful votes, then rank the reviews based on the amount of information. We believe this informative evaluation is critical to your work when handling a large amount of review information, for informative reviews often provide more constructive input into the design features and therefore are more referential in reputation analysis.

<!-- b000498 | prose | pages [24] -->
We get consumer’s preferences and concerns by sifting through the top 1% most informative ratings and reviews of baby paciﬁer, microwave and hair dryer. The popular design features by our analysis are as follows:

<!-- b000499 | prose | pages [24] -->
• Baby paciﬁer: Various alternatives to size and safe materials are necessary. Besides, cute patterns are popular with babies.

<!-- b000500 | prose | pages [24] -->
• Microwaves: Multifunctional microwaves with rotating grills, accurate timers, multiple usage patterns, etc. are welcomed by consumers.

<!-- b000501 | prose | pages [24] -->
• Hair dryer: Consumers prefer hair dryers small with high-power (on the premise of safety). Some additional designs like folding handle are beneﬁcial to attracting con- sumers. Then we establish time-based measures to predict the increase or decrease of product reputation in the online marketplace. Our model can accurately predict the reputation change of a product over a long period of time in the future. This precise prediction makes sense for you to generate strategies before the decrease of the reputation.

<!-- b000502 | prose | pages [24] -->
Based on the reputation prediction, we stipulate that the degree to which reputation will increase or decrease in the future as judgment of the potential success or failure of the prod- uct. Our analysis shows that, overall, baby paciﬁers are potentially successful products, while microwaves and hair dryers are at greater risk of failure.

<!-- b000503 | prose | pages [24] -->
According to our analysis results, we formulate reasonable sales strategies for your com- pany: (1) We recommend that you put microwaves and hair dryers into the market when the reputation rises. While the reputation of baby paciﬁers is on the rise, and it’s best to put them on the market now. (2) The more complete the product information is, the less loss will be caused by the unequal information between buyers and sellers. (3) We recommend that you in- crease your promotional efforts when there are more ﬁve-star ratings of your products to form positive feedback. (4) When your product’s reputation declines, focus on one-star ratings and reviews.

<!-- b000504 | prose | pages [24] -->
Thanks for taking the time out of your busy schedule to read my letter. Hope our advice can help. MCM Team # 2002116

<!-- b000505 | furniture | pages [24] -->
关注数学模型

<!-- b000506 | furniture | pages [24] -->
2

<!-- b000507 | furniture | pages [24] -->
MATHmodels

<!-- b000508 | furniture | pages [24] -->
获取更多资讯

<!-- b000509 | furniture | pages [25] -->
Team # 2002116

<!-- b000510 | furniture | pages [25] -->
Page 24 of 38

<!-- b000511 | heading | pages [25] -->
References

<!-- b000512 | references | pages [25] -->
[1] Peter C Evans and Annabelle Gawer. The rise of the platform enterprise: a global survey.

<!-- b000513 | references | pages [25] -->
2016.

<!-- b000514 | references | pages [25] -->
[2] Seyed Pouyan Eslami, Maryam Ghasemaghaei, and Khaled Hassanein. Which online re-

<!-- b000515 | references | pages [25] -->
views do consumers ﬁnd most helpful? a multi-method investigation. Decision Support

<!-- b000516 | references | pages [25] -->
Systems, 113:32 – 42, 2018.

<!-- b000517 | references | pages [25] -->
[3] Understanding the determinants of online review helpfulness: A meta-analytic investiga-

<!-- b000518 | references | pages [25] -->
tion. Decision Support Systems, 102:1 – 11, 2017.

<!-- b000519 | references | pages [25] -->
[4] Ya-Han Hu and Kuanchin Chen. Predicting hotel review helpfulness: The impact of review

<!-- b000520 | references | pages [25] -->
visibility, and interaction between hotel stars and review ratings. International Journal of

<!-- b000521 | references | pages [25] -->
Information Management, 36(6, Part A):929 – 944, 2016.

<!-- b000522 | references | pages [25] -->
[5] Y.Chen and J.Xie. Online consumer review: word-of-mouth as a new element of marketing

<!-- b000523 | references | pages [25] -->
communication mix. Management Science, 54(3):477–491, 2008.

<!-- b000524 | references | pages [25] -->
[6] Liang-Chih Yu, Jheng-Long Wu, Pei-Chann Chang, and Hsuan-Shou Chu. Using a contex-

<!-- b000525 | references | pages [25] -->
tual entropy model to expand emotion words and their intensity for the sentiment classi-

<!-- b000526 | references | pages [25] -->
ﬁcation of stock market news. Knowledge-Based Systems, 41:89 – 97, 2013.

<!-- b000527 | references | pages [25] -->
[7] Clayton J Hutto and Eric Gilbert. Vader: A parsimonious rule-based model for sentiment

<!-- b000528 | references | pages [25] -->
analysis of social media text. In Eighth international AAAI conference on weblogs and social

<!-- b000529 | references | pages [25] -->
media, 2014.

<!-- b000530 | references | pages [25] -->
[8] Solomon Kullback. Information theory and statistics. john riley and sons. Inc. New York,

<!-- b000531 | references | pages [25] -->
1959.

<!-- b000532 | references | pages [25] -->
[9] Ira Assent, Marc Wichterich, Ralph Krieger, Hardy Kremer, and Thomas Seidl. Anticipa-

<!-- b000533 | references | pages [25] -->
tory dtw for efﬁcient similarity search in time series databases. Proceedings of the VLDB

<!-- b000534 | references | pages [25] -->
Endowment, 2(1):826–837, 2009.

<!-- b000535 | references | pages [25] -->
[10] Sangwon Park and Juan L. Nicolau. Asymmetric effects of online consumer reviews. An-

<!-- b000536 | references | pages [25] -->
nals of Tourism Research, 50:67 – 83, 2015.

<!-- b000537 | heading | pages [25] -->
Appendices

<!-- b000538 | heading | pages [25] -->
Appendix A

<!-- b000539 | prose | pages [25] -->
Annotated Seed Words and Frequency

<!-- b000540 | prose | pages [25] -->
We manually annotated seed words in to ﬁve groups, shown as follows.

<!-- b000541 | heading | pages [25] -->
1. Strong Positive: great (3006), recommend (1174), perfect (761), best (656), favorite (368),

<!-- b000542 | prose | pages [25] -->
perfectly (183), awesome (125), excellent(114).

<!-- b000543 | furniture | pages [25] -->
关注数学模型

<!-- b000544 | furniture | pages [25] -->
2

<!-- b000545 | furniture | pages [25] -->
MATHmodels

<!-- b000546 | furniture | pages [25] -->
获取更多资讯

<!-- b000547 | furniture | pages [26] -->
Team # 2002116

<!-- b000548 | furniture | pages [26] -->
Page 25 of 38

<!-- b000549 | heading | pages [26] -->
2. Weak Positive: like (3624), love (2766), loves (2753), easy (2154), good (1424), well (1286),

<!-- b000550 | prose | pages [26] -->
could (1054), cute (1002), loved (876), nice (855), better (821), able (738), ﬁt (731), right (687), likes (647) wish (644), want (585), happy (577), easier (521), ﬁts (395), liked (360), helps (311), glad (229), clean (193), adorable (191), cute (191), fun (181), Love (163), well (157), ﬁne (153), helped (152), pleased (141), Easy (131), wonderful (131), excited (118), comfort (114), warm (114), LOVES (103), cute! (99), enjoy (96), enjoys (86), cool (85).

<!-- b000551 | prose | pages [26] -->
3. Moderate: baby (4998), her (3852), she (3678), he (3537), can (2913), his (2658), use (2446), son (2239), daughter (2114), more (1867), him (1184), She (763), babies (626), easily (619), gift (556), worth (513), super (489), toy (448), wanted (437), well (407), won’t (400), smaller (302), wouldn’t (303), girl (293), attached (293), exactly (282), given (251), might (218), throw (213), heavy (210), friend (205), bigger (189), brands (171), issue (169), larger (167), anyone (166), worry (166), attach (165), clear (160), fast (159), prefers (158), lose (157), care (157), replace (157), stuck (151), granddaughter (150), issues (146), quick (142), cheap (142), daughter’s (140), safety (139), tiny (136), deal (136), expecting (131), wants (129), expected (128), prefer (128), clean (123), holes (123), gift (120), easily (118), simple (118), strong (113), cheaper (110), unless (106), original (107), slightly (105), nursing (103), gifts (98), thin (94), nephew (94), save (94), loose (93), adjust (92), better (92), dirty (87).

<!-- b000552 | heading | pages [26] -->
4. Weak Negative: doesn’t (1283), didn’t (1011), can’t (780), hard (734), less (354), problem

<!-- b000553 | prose | pages [26] -->
(346), wasn’t (297), couldn’t (285), however (252), difﬁcult (248), yet (244), cannot (211), however (175), Not (173), problems (149), aren’t (143), However (132), hit (126), against (124), harder (118), waste (118), wrong (102), trouble (101), pain (90), though (180).

<!-- b000554 | heading | pages [26] -->
5. Strong Negative: but (7128), disappointed (170), NOT (90), No (113).

<!-- b000555 | heading | pages [26] -->
Appendix B

<!-- b000556 | prose | pages [26] -->
The Number of Keyword Occurrences in Differ- ent Keyword Groups

<!-- b000557 | prose | pages [26] -->
The number of keyword occurrences of baby paciﬁer is listed in Table 4 in a total of 18937 reviews.

<!-- b000558 | caption | pages [26] -->
Table 4: The number of keyword occurrences in different keyword groups of baby paciﬁer

<!-- b000559 | prose | pages [26] -->
Group The number of keyword occurrences Size 3402 Appearance 3399 Convenience 3138 Safety 2374 Component 706

<!-- b000560 | prose | pages [26] -->
The number of keyword occurrences of hair dryer is listed in Table 5 in a total of 1616 re- views.

<!-- b000561 | prose | pages [26] -->
The number of keyword occurrences of hair dryer is listed in Table 6 in a total of 11470 reviews.

<!-- b000562 | furniture | pages [26] -->
关注数学模型

<!-- b000563 | furniture | pages [26] -->
2

<!-- b000564 | furniture | pages [26] -->
MATHmodels

<!-- b000565 | furniture | pages [26] -->
获取更多资讯

<!-- b000566 | furniture | pages [27] -->
Team # 2002116

<!-- b000567 | furniture | pages [27] -->
Page 26 of 38

<!-- b000568 | caption | pages [27] -->
Table 5: The number of keyword occurrences in different keyword groups of microwave

<!-- b000569 | prose | pages [27] -->
Group The number of keyword occurrences Appearance 2350 Component 2289 Price 2234 Setting 1049 Safety 617 Power 594

<!-- b000570 | caption | pages [27] -->
Table 6: The number of keyword occurrences in different keyword groups of hair dryer

<!-- b000571 | prose | pages [27] -->
Group The number of keyword occurrences Power 6774 Appearance 4656 Special design 3973 Hair quality 2666 Safety 1544 Working volume 1542

<!-- b000572 | prose | pages [27] -->
Top 1% Most Informative Ratings and Reviews

<!-- b000573 | heading | pages [27] -->
Appendix C

<!-- b000574 | prose | pages [27] -->
We list following top 1% most informative reviews and their associated ratings according the the "importance" rate our model predicted on "Hair dryer" data set.

<!-- b000575 | prose | pages [27] -->
1. <No problems>(5-star rating): Better than expected. Great product, excellent delivery.

<!-- b000576 | prose | pages [27] -->
2. <GREAT - Powerful and small for travel>(5-star rating): I am small with shoulder prob- lems and this is very compact and light weight. It packs a punch with power!

<!-- b000577 | prose | pages [27] -->
3. <Good product.. love it!>(5-star rating): I have frizzy thick hair and using this product makes it more manageable. Adds shine and softness.. not oily/heavy.. love it.

<!-- b000578 | prose | pages [27] -->
4. <good purchase great quality>(5-star rating): I use it a lot, i am a stylist and use this with my really curly hair clients and it never disappoint me. great price, great quality, great buy.

<!-- b000579 | prose | pages [27] -->
5. <Thick hair, no worries.>(5-star rating): Love this dryer, works so great and fast too.

<!-- b000580 | prose | pages [27] -->
Bought it for my mom as a gift and she absolutely loves it! She has very thick hair and hair dryer worked great for her.

<!-- b000581 | prose | pages [27] -->
6. <Excellent! Perfect for my thick hair.>(5-star rating): I have thick shoulder length hair, that usually takes 35 - 40 minutes to dry. With this dryer, I’m done in 20 minutes and my hair looks smooth and soft. I was skeptical about the whole thing, but it has made a big difference with my hair. The removable<BR>ﬁlter was the deciding factor. I’ve thrown away dryers just because I couldn’t clean them. Excellent product!

<!-- b000582 | prose | pages [27, 28] -->
7. <LOVE this dryer!!!!>(5-star rating): being a professional hairstylist i got so tired of ex- pensive blowdryers that dont dry the hair any better than the cheap ones. THEN, i read the reviews for this dryer and again i thought, yeah right. SOOO, i bought it and i must say, this blow dryer rocks. it dries the hair in half the time and leaves it smooth and shiny!!! FINALLY, i found one that delivers on its promise

<!-- b000583 | furniture | pages [27] -->
关注数学模型

<!-- b000584 | furniture | pages [27] -->
2

<!-- b000585 | furniture | pages [27] -->
MATHmodels

<!-- b000586 | furniture | pages [27] -->
获取更多资讯

<!-- b000587 | furniture | pages [28] -->
Team # 2002116

<!-- b000588 | furniture | pages [28] -->
Page 27 of 38

<!-- b000590 | prose | pages [28] -->
8. <great dryer, great price>(5-star rating): great dryer, works well. Lots of heat and volume when I need it, nice cooling button. Dries my hair fast. Amazon got it to me overnight when mine died, so I only went 1 day with bad hair. Not bad, because I don’t have time to shop at the brick and mortar.

<!-- b000591 | prose | pages [28] -->
9. <Excellent value!>(5-star rating): This was so cheap but the product is NOT - excellent quality!! LOVE it and use it a lot!

<!-- b000592 | prose | pages [28] -->
10. <excellent, powerful action>(5-star rating): We’ve been using this hair dryer for a few weeks now on a constant basis. Overall, this is a powerful blower that gets your hair dry quickly with excellent balance of heat. No hot spots that cheapo dryers can develop. Yes, it is on the heavy and bulky side but that’s because of the quality construction. I have no doubt this dryer will continue to last for years to come.

<!-- b000593 | prose | pages [28] -->
11. <Pretty neat little dryer>(5-star rating): My wife used one of these at a motel we stayed in. She really wanted one so I bought it. Your old lady will dig it too because it is powerful and has a cord reel. You will hate yourself later when you have to disassemble it to dig her hair out of it because she complains about it not blowing hard like it used to. But women are like that.........blah blah blah complain blah blah.....<br />If you can disassemble this thing, clean it and re-assemble it in working order before she needs it to dry her wet head consider yourself lucky. I think a nuclear bomb would be easier to work on.

<!-- b000594 | prose | pages [28] -->
12. <Great product, great price.>(5-star rating): This is my second hair blower of the exact same model. (Conair Ionic Conditioning Pro Style 1875-Watt Hair Dryer)[[ASIN:B00005O0MZ Conair Ionic Conditioning Pro Style 1875-Watt Hair Dryer]] I would by it again.

<!-- b000595 | prose | pages [28] -->
13. <luv it!!!! best dryer ever>(5-star rating): It let my hair so nice and without freeze!!!!! im so sad that i drop mine by mistake after 3 years that i have it with me, but ill defenetly buy it again!!!

<!-- b000596 | prose | pages [28] -->
14. <Great for ﬁne hair!>(5-star rating): I have very ﬁne hair that doesn’t like to be styled.

<!-- b000597 | prose | pages [28] -->
Using this dryer, I have;<br /><br />Volume<br />Body<br />Curl<br /><br />AND, I don’t have to use any product to get it that way. I believe the key is not only the dryer, but, the shampoo you use. I use a Keratin infused shampoo with Ion ultra light weight conditioner. Bottom line- this blow dryer is incredible!

<!-- b000598 | prose | pages [28] -->
15. <Good dryer for a good price>(5-star rating): I have VERY thick hair, and this really did cut down on my drying time. I use the cold button when I’m done and it seems to make my hair a little more manageable.

<!-- b000599 | prose | pages [28] -->
16. <Best investment!!!>(5-star rating): I will now be saving money by going less to my hairstylist. This blowdryer dried my hair 2x faster than a previous blowdryer I had. I wished I had bought this blowdryer years ago!

<!-- b000600 | prose | pages [28] -->
17. <Excellent!!!>(5-star rating): I have one in my guest bathroom and my visitors can use it.

<!-- b000601 | prose | pages [28] -->
You dont have to looking one in the lower of the lavatory.

<!-- b000602 | furniture | pages [28] -->
关注数学模型

<!-- b000603 | furniture | pages [28] -->
2

<!-- b000604 | furniture | pages [28] -->
MATHmodels

<!-- b000605 | furniture | pages [28] -->
获取更多资讯

<!-- b000606 | furniture | pages [29] -->
Team # 2002116

<!-- b000607 | furniture | pages [29] -->
Page 28 of 38

<!-- b000608 | prose | pages [29] -->
18. <T>(5-star rating): This dryer is wonderful, the power you have is second to none .., a little heavy but worth it for the results it leaves. I am very happy.

<!-- b000609 | prose | pages [29] -->
19. <My wife loves it (I did good on this one)>(5-star rating): It will seriously dim the lights in your house, but man can it dry hair!

<!-- b000610 | prose | pages [29] -->
20. <I LOVE this hair dryer!>(5-star rating): It dries my hair quickly, is small enough to pack in my suitcase, has a retractable cord, and makes my hair incredibly silky and smooth.

<!-- b000611 | prose | pages [29] -->
And you can’t beat the price either. I’m never buying another dryer brand/model as long as this one is in production.

<!-- b000612 | prose | pages [29] -->
21. <Love it!>(5-star rating): Small but packs some serious heat and power!

<!-- b000613 | prose | pages [29] -->
22. <Love it!>(5-star rating): I probably bought and returned ﬁve other hair dryers before keeping this one. My kids and I all have LOTS of hair that takes forever to dry. This hair dryer is the best; it dries our hair much faster than our old one did. No worrying about accidentally turning it off or changing the setting, you don’t have to hold the button for the cold shot, and if the regular setting isn’t quick enough for you, there’s even a turbo setting. This saves us so much time in the mornings! I’m thinking about buying a second one to have in the other bathroom so two of us can dry our hair at once. It did seem a bit big at ﬁrst, but it didn’t take long to get used to it. Other dryers had too much air ﬂow and I couldn’t control how I was styling my hair, or the high heat setting was too hot, but the settings on this one are just right.

<!-- b000614 | prose | pages [29] -->
23. <Convienience as well as a great product.>(5-star rating): Exactly what we were looking for.

<!-- b000615 | prose | pages [29] -->
24. <Colored Hair no longer dry looking>(5-star rating): I bought this because of the great reviews. I color my hair (to cover gray) and blow drying always takes too long and hair looks dry and have some sticking up all over. I bought this and OMG!!! It took half the time to dry and no ﬂy-away hair!! I have gotten so many compliments. I loved it but never thought anyone would notice. I really do get such nice compliments. Remember I am over the hill and hair seems to get dryer with the years and coloring doesn’t help that except cover the gray which I am so happy for that. But if you feel your hair is getting too dry and/or frizzy, ﬂy-away hair — this will take care of it. Its a one-time purchase and so worth it. 3-temperatures and a cool button which I love. What can I say, oh it is not all that heavy, regular weight as other unless you want a little blow and a lot of noise from a much cheaper hair blower. Been there done that... this is the BOMB!!! Don’t waste more time or money on frustrating hair blowers, be good to yourself and buy this awesome hair blower. Take care and you will not regret it for one second.

<!-- b000616 | prose | pages [29] -->
25. <Works great!>(5-star rating): Very affordable, reviews were accurate. It is quieter than my old one and quick. No need to spend a lot of money on a dryer when you have the quality with Conair.

<!-- b000617 | prose | pages [29] -->
26. <Great dryer!>(5-star rating): Discovered this little gem in a hotel in NYC. Dries hair without leaving frizz or ﬂy-aways. Folding handle makes it convenient for storing and travel.

<!-- b000618 | furniture | pages [29] -->
关注数学模型

<!-- b000619 | furniture | pages [29] -->
2

<!-- b000620 | furniture | pages [29] -->
MATHmodels

<!-- b000621 | furniture | pages [29] -->
获取更多资讯

<!-- b000622 | furniture | pages [30] -->
Team # 2002116

<!-- b000623 | furniture | pages [30] -->
Page 29 of 38

<!-- b000624 | prose | pages [30] -->
27. <Great hairdryer!>(5-star rating): This hairdryer is the lightest and quietest I’ve ever used. In fact, my husband now wants one of his own!

<!-- b000625 | prose | pages [30] -->
28. <so hot. love Nd low noise>(5-star rating): I love love love this hair dryer....wash my hair seat for 30 min Nd I’m done...

<!-- b000626 | prose | pages [30] -->
29. <LOVE IT!!!>(5-star rating): Every day I used to dread blow drying my hair. It’s long and thick and after a half an hour it still wouldn’t be dry. This hair dryer gets my hair completely dry in 3-4 minutes max. It has totally changed my life. I have bought one more just to have on hand. You never know how long a hair dryer will last.

<!-- b000627 | prose | pages [30] -->
30. <Love it!>(5-star rating): I got this dryer to replace my old one and wow does it make a difference. My hair is so soft and shiny. I can even use this to dry my 1 year old daughter’s hair and I couldn’t to that with my old one because it would get too hot even on the lower setting. It dries fast without burning. Deﬁnitely worth every cent!

<!-- b000628 | prose | pages [30] -->
31. <Super little dynamo!!>(5-star rating): I already have one of these, but because I travel a lot, I have one at home and one for my travel trailer. Lots of heat & power in a small little dryer.

<!-- b000629 | prose | pages [30] -->
32. <IN LOVE>(5-star rating): I LOVEEEEEEEEEE IT

<!-- b000630 | prose | pages [30] -->
33. <love it>(5-star rating): Still using this after a year.....love the retractable cord

<!-- b000631 | prose | pages [30] -->
34. <I love it>(5-star rating): It is faster compared to my old one, the cord doesn’t use extra space as it rolls inside, which I ﬁnd very convenient.

<!-- b000632 | prose | pages [30] -->
35. <love it>(5-star rating): use it every day

<!-- b000633 | prose | pages [30] -->
36. <I love it>(5-star rating): Was everything they said it was takes up very little space and does the job

<!-- b000634 | prose | pages [30] -->
37. <Love it>(5-star rating): This is a replacement for the one I have had for many years.

<!-- b000635 | prose | pages [30] -->
38. <Great!!>(5-star rating): Expensive but worth every penny. professional hair dryer with professional results. Cuts time spent in the bathroom drying my hair

<!-- b000636 | prose | pages [30] -->
39. <Love it!>(5-star rating): I have thick hair and this baby gets my hair dry quickly and WITHOUT frizzies! Love it!

<!-- b000637 | prose | pages [30] -->
40. <great low dryer>(5-star rating): This blow dryer is great for traveling. The fold up han- dle allows for easy packing. The cord retractor is great

<!-- b000638 | prose | pages [30] -->
41. <It works like a dryer... :)>(5-star rating): I don’t use my hair dryer for much more than drying purposes... Lol... It’s simple, in-expensive, and it blows a lot of hot air... ;)<br /><br />It serves its purpose well...

<!-- b000639 | prose | pages [30, 31] -->
42. <Love it!>(5-star rating): It dries so fast it is great! I had brought one over from France that my mom had gotten years and years ago but unfortunately I was never able to get the same power due to the voltage difference. I ordered this one and it is the same to the T (except color). Cut down my hair routine in half.<br />It does fume and heats up A LOT so be careful!<br />(I have black relaxed hair) 43. <Works like a charm!>(5-star rating): I considered shelling out some serious cash to buy a high end blow-dryer but then I realized that’s stupid...and I’m cheap, so I bought this instead and I honestly could not be happier! I have long hair (like to the middle of my back) and it’s pretty thick and this dryer dries my hair in under 10 minutes. My last dryer took FOR.EV.ER so to avoid getting stared down by my husband and watching the hate build in his eyes because I was taking so long to get ready and thus withholding whatever meal we are trying to go eat from him, I would just not bother drying and curling my hair and instead would just rock my natural fro but with this new dryer I can do my hair and still get out of the house quickly (relatively, anyway).<br /><br />I recommend this dryer highly! No need to waste your hard earned cash on a high end dryer; this one does the job!

<!-- b000640 | furniture | pages [30] -->
关注数学模型

<!-- b000641 | furniture | pages [30] -->
2

<!-- b000642 | furniture | pages [30] -->
MATHmodels

<!-- b000643 | furniture | pages [30] -->
获取更多资讯

<!-- b000644 | furniture | pages [31] -->
Team # 2002116

<!-- b000645 | furniture | pages [31] -->
Page 30 of 38

<!-- b000647 | prose | pages [31] -->
44. <Looks great>(5-star rating): Return is no longer needed

<!-- b000648 | prose | pages [31] -->
45. <Awesome product>(5-star rating): We had one of these over 18yrs old and it ﬁnally gave out! The new one outdoes the previous model!

<!-- b000649 | prose | pages [31] -->
46. <Great dryer>(5-star rating): This was purchased to replace the one that got stomped (by accident). It is of a very professional quality, without the high price tag.

<!-- b000650 | prose | pages [31] -->
47. <Great power>(5-star rating): Fast drying with lots of shine - I was ﬁrst introduced to this hair dryer at a 5-star hotel I stayed at - it dries hair fast with lots of shine.

<!-- b000651 | prose | pages [31] -->
48. <Great dryer>(5-star rating): Wanted same brand and wattage they have on the wall at our Y.<br />Perfect. Just what my spouse was looking for.

<!-- b000652 | prose | pages [31] -->
49. <Great dryer>(5-star rating): My hair is so soft with this dryer and it doesnt frizz out.

<!-- b000653 | prose | pages [31] -->
Also, it isnt as loud as my previous cheaper dryer.

<!-- b000654 | prose | pages [31] -->
50. <Great hairdryer>(5-star rating): This hair dryer has a lot of power. The wall mount keeps it out of the way, but readily accessible when needed. This is a replacement hair dryer for us and we purchased the same one when the other quit working.

<!-- b000655 | prose | pages [31] -->
51. <Great Product!>(5-star rating): I read about the John Frieda Full Volume Hair Dryer in a magazine, and it has more than lived up to its review. Dries quickly, leaves hair soft, WITH NO FRIZZIES, and with lots of body. It’s made my wavy, mind-of-its-own hair behave for the ﬁrst time. I highly recommend this product. Couldn’t live without it.

<!-- b000656 | prose | pages [31] -->
52. <Great>(5-star rating): This dryer is exactly what I wanted very lightweight and does the job

<!-- b000657 | prose | pages [31] -->
53. <Great>(5-star rating): Exactly as expected

<!-- b000658 | prose | pages [31] -->
54. <No more tangled cords!>(5-star rating): This hairdryer has great power and different heat settings. The price and quality are great, it is very heavy duty. The automatically recoiling cord is a bonus!

<!-- b000659 | prose | pages [31] -->
55. <Great Dryer!>(5-star rating): I bought this hair dryer to replace my previous Hot Tools hair dryer that had broken after many years of use. This hair dryer is even better than my old one! It is much lighter and still has the same fast drying power of the last one. I take it everywhere because no other hair dryer can dry my long layered hair as quickly and easily.

<!-- b000660 | furniture | pages [31] -->
关注数学模型

<!-- b000661 | furniture | pages [31] -->
2

<!-- b000662 | furniture | pages [31] -->
MATHmodels

<!-- b000663 | furniture | pages [31] -->
获取更多资讯

<!-- b000664 | furniture | pages [32] -->
Team # 2002116

<!-- b000665 | furniture | pages [32] -->
Page 31 of 38

<!-- b000666 | prose | pages [32] -->
56. <Wonderful. Steamy. Affordable. sets up in few mins. excellent>(5-star rating): Sets up very easily and quickly. No tools needed. Literally just a few minutes. I put in a bar stool to sit on and a towel over the vent holes. As others have said, the towel over the fresh air hole is needed in order to keep the steam in. I don’t know why people complain about the air vent holes. For 2 bucks you can buy a towel for them or for $2000 you can buy a different style of steam sauna. Seriously folks, buy a towel. Add a little aromatherapy salts and it is bliss! Hard to ﬁnd this kind of bliss for a mere 200 bucks. I get mine almost painfully hot in 30 mins then lower the temp, get in, and reset the timer. The picture displayed is a little off as the door opens from one side and not down the middle as pictured. No worries though. It’s nice. I would buy it again.

<!-- b000667 | prose | pages [32] -->
57. <Best blowdryer on earth!>(5-star rating): awesome!!!!!!!!!!!!!!!!!!!!

<!-- b000668 | prose | pages [32] -->
58. <Love this Hair Dryer!>(5-star rating): This hair dryer is great–it’s lightweight and dries my hair in half the time of all other hair dryers I’ve used.

<!-- b000669 | prose | pages [32] -->
59. <Great Hair Dryer for a low price>(5-star rating): I was really surprised when I received this hair dryer because the quality of the product IT IS GREAT<br />The dryer is very affordable and has a great look and feel and puts out nice heat. I would deﬁnitely recom- mend this product to friends and am very happy with it.

<!-- b000670 | prose | pages [32] -->
60. <we love it>(5-star rating): I add the conditioner to my routine. My husband found that it really helped when he use both the shampoo and the conditioner and left the conditioner on for a couple of minutes

<!-- b000671 | prose | pages [32] -->
61. <Love my hairdryer>(5-star rating): I couldn’t live without it!

<!-- b000672 | prose | pages [32] -->
62. <the best around>(5-star rating): This is the third wall mount I have purchased. Love the convenience and that I don’t have to keep in a drawer.

<!-- b000673 | prose | pages [32] -->
63. <Best darn hair dryer I’ve ever had!!!>(5-star rating): None available.

<!-- b000674 | prose | pages [32] -->
64. <Love it>(5-star rating): I bought this hair dryer a few months ago to replace my old one (a different brand). This new hair dryer is as powerful as my last one (which I loved), but much quieter and my hair does not feel frizzy afterwards. My only complaint is that the handle is peeling a little at the bottom.

<!-- b000675 | prose | pages [32] -->
65. <Super quiet>(5-star rating): This is very, very quiet. It has the longest cord. I have ever seen on a dryer. I don’t understand the ion thing.

<!-- b000676 | prose | pages [32] -->
66. <Excellent!>(5-star rating): This has cut my drying time in half! It’s a bit heavier than I was expecting but still exceeded expectations.

<!-- b000677 | prose | pages [32] -->
67. <Excellent!!!>(5-star rating): This stuff worked miracles on my callused feet and my cu- ticles. Along with being antimicrobial you can’t miss with this product. Very little goes along way so it will last you.

<!-- b000678 | prose | pages [32] -->
68. <Great Blow Dryer>(5-star rating): Live this hairdryer

<!-- b000679 | prose | pages [32] -->
69. <Great Hair Dryer>(5-star rating): This hair dryer really dose make your hair softer, I have had it a month now and I use it only if I have wet hair before bed or going out and it only takes about 5 min to dry my hair (my older one took 30) I highly recimend it.

<!-- b000680 | furniture | pages [32] -->
关注数学模型

<!-- b000681 | furniture | pages [32] -->
2

<!-- b000682 | furniture | pages [32] -->
MATHmodels

<!-- b000683 | furniture | pages [32] -->
获取更多资讯

<!-- b000684 | furniture | pages [33] -->
Team # 2002116

<!-- b000685 | furniture | pages [33] -->
Page 32 of 38

<!-- b000686 | prose | pages [33] -->
70. <A great dryer.>(5-star rating): When you don’t feel like itting under a dryer or blw dry- ing your hair this is what you need. I can carry it around the house whille it drys your hair.

<!-- b000687 | prose | pages [33] -->
71. <perfect>(5-star rating): I took one hair drier from my country. but it doesn’t work be- cause of .different voltages.<br /><br />so I had to buy a new one, then I select it, I got it in two days. it is so fast!<br /><br />It is perfect@!

<!-- b000688 | prose | pages [33] -->
72. <Perfect>(5-star rating): Just what I wanted. Small, but powerfull.

<!-- b000689 | prose | pages [33] -->
73. <Great product!>(5-star rating): This is a great dryer! My ﬁrst one ﬁnally died after 5 years of constant use and I ended up trying a similar Gold N Hot and it stopped working and overheated on the ﬁrst use. I quickly ordered the Andis and have had no issues! I have long curly hair and it drys my hair in under 20 min. I will deﬁnitely purchase this product a third time once I’ve worn the one I just bought out.

<!-- b000690 | prose | pages [33] -->
74. <great idea>(5-star rating): we have a tiny bathroom with no storage.this hair dryer is so perfect.it’s out of the way when not in use.does not take up drawer space.even has a night light.

<!-- b000691 | prose | pages [33] -->
75. <great product>(5-star rating): Dries fast and leaves my hair shiny and straight. Its a little loud, but it puts out a lot of air so I guess that is to be expected.

<!-- b000692 | prose | pages [33] -->
76. <Great Product>(5-star rating): Dryer is lightweight and delivers a lot of heat. Dries and smoothes hair quickly. Cuts down drying time down in half. Wont go back to standard dryers.

<!-- b000693 | prose | pages [33] -->
77. <Amazing!>(5-star rating): This will curl even the thinnest ﬁnest hair and the curls last all day.Instantly heats up and doesn’t burn hair. Hairspray and/or styling gel will extend the life of the curls but is not necessary.I can do my whole head myself in around 15- 20minutes and i have long hair. The only down side I have found is that if you burn yourself-you DEFINATELY know it. Not safe for kids to use because of how hot it gets.

<!-- b000694 | prose | pages [33] -->
78. <Works great!>(5-star rating): Drys my hair quickly. My hair is thick this dryer cuts my time in half. I would recommend it for anyone.

<!-- b000695 | prose | pages [33] -->
79. <Great Product>(5-star rating): I’ve been using this exact same hair dryer for 20 years!

<!-- b000696 | prose | pages [33] -->
There’s a reason I keep buying it even though it seems to die after 4-5 yrs of constant use.

<!-- b000697 | prose | pages [33] -->
The nightlight is perfect for the master bath. Now we don’t wake each other up in the middle of the night by turning on the normal light.

<!-- b000698 | prose | pages [33] -->
80. <Amazing :)>(5-star rating): i been using this face wash for last 3 years now and all i can say is this face wash does wonders, it cleared away all my acne, all my scars that were left by the acne, and made my skin way softer, of course this wasnt only because the face wash, i had to put on facial lotion as well for the acne to really go away but this face wash does what it does and not heavy on your skin compare to many other acne facial wash i tried

<!-- b000699 | prose | pages [33, 34] -->
81. <There’s no such thing as a quiet hair-dryer.>(5-star rating): This dryer is not quiet but the noise is so much more tolerable compared to some dryers that has whistling noise or just super loud. I love that it is foldable and retractable - makes it easier for storage and for traveling.

<!-- b000700 | furniture | pages [33] -->
关注数学模型

<!-- b000701 | furniture | pages [33] -->
2

<!-- b000702 | furniture | pages [33] -->
MATHmodels

<!-- b000703 | furniture | pages [33] -->
获取更多资讯

<!-- b000704 | furniture | pages [34] -->
Team # 2002116

<!-- b000705 | furniture | pages [34] -->
Page 33 of 38

<!-- b000707 | prose | pages [34] -->
82. <Awesome Dryer>(5-star rating): I have wanted this for Christmas two years in a row and ﬁnally someone in my family purchased it, NOW they want one!

<!-- b000708 | prose | pages [34] -->
83. <The best>(5-star rating): Best hair dryer I’ve ever had. My ﬁrst one lasted 12 to 15 years of daily use, lost count of how old it was. My guess that it died at age 110 in hair dyer years.

<!-- b000709 | prose | pages [34] -->
84. <awesome dryer>(5-star rating): I picked up this dryer when I was staying some nights at my ﬁancee’s apartment, so I could stash it out of his way when I wasn’t there. It folds in half and the cord retracts into the handle, making it very small. I was immediately impressed with the power, I have pretty thick hair but I could completely dry it in just a few minutes. When we got married and bought a house it has stayed on with me, becoming my primary hair dryer. I have used it daily for about 3 years now and it has not faltered, deﬁnitely worth it!

<!-- b000710 | prose | pages [34] -->
85. <Great buy.>(5-star rating): Although I bought this for travel, I like it more then my regular sized dryer.<br />Its pink but appears purple in the picture, thats the only reason I gave it a 4 instead of a 5.

<!-- b000711 | prose | pages [34] -->
86. <great hair dryer!>(5-star rating): I never realized a hair dryer could actually make your hair feel soft! This one does that and dries my hair in 2 seconds. Okay - maybe not 2 seconds, but it really is fast.

<!-- b000712 | prose | pages [34] -->
87. <Happy Customer>(5-star rating): Met my expectations.

<!-- b000713 | prose | pages [34] -->
88. <Perfect product>(5-star rating): Product was shipped promptly, is exactly as advertised.

<!-- b000714 | prose | pages [34] -->
Not too much, not too little.....does the job to dry both my hair and my Chihuahua’s after a bath.

<!-- b000715 | prose | pages [34] -->
89. <best>(5-star rating): Had the blow dryer for several months now... no problem does not over heat.... best investment

<!-- b000716 | prose | pages [34] -->
90. <The Best>(5-star rating): The only hair dryer manufactured with the vents on the side.

<!-- b000717 | prose | pages [34] -->
This is essential for my work, the newer backk vent ones are worthless to me.

<!-- b000718 | prose | pages [34] -->
91. <Love it.>(5-star rating): Dryer was delivered on time. It is powerful, dries my short hair in 2 minutes and isn’t heavy. Love it.

<!-- b000719 | prose | pages [34] -->
92. <The BEST I have ever owned>(5-star rating): I can not say enough good things about this hair dryer. I have long curly hair that took over an hour to dry. Now I can actually leave for work on time. My previous dryer was more expensive and not even close to being as good or as fast. No reason to ever spend more money again. I am a very satiﬁed customer. Without a doubt, I will be a repeat customer next time I need a new hair dryer.

<!-- b000720 | prose | pages [34, 35] -->
93. <I love it>(5-star rating): Ingenious product. Simple and convenient. I glued it to my mirror and stayed there. No more trouble holding the dryer on one hand and brushing my hair with the other one! worth every penny 94. <Five Stars>(5-star rating): Great air pressure

<!-- b000721 | furniture | pages [34] -->
关注数学模型

<!-- b000722 | furniture | pages [34] -->
2

<!-- b000723 | furniture | pages [34] -->
MATHmodels

<!-- b000724 | furniture | pages [34] -->
获取更多资讯

<!-- b000725 | furniture | pages [35] -->
Team # 2002116

<!-- b000726 | furniture | pages [35] -->
Page 34 of 38

<!-- b000728 | prose | pages [35] -->
95. <THE BEST BLOWDRYER I HAVE EVER HAD!>(5-star rating): Quickly dries your hair without frying it !!!

<!-- b000729 | prose | pages [35] -->
96. <works great>(5-star rating): it does everything a good dryer should do. The retractable cord doesn’t work as well as it should unfortunately but can be managed.

<!-- b000730 | prose | pages [35] -->
97. <LOVE IT!!! Couldn’t be happier with my purchase.>(5-star rating): I bought this hair dryer to replace one that I borrowed from a friend that burnt out because I used the electric converter incorrectly. Because the price was so reasonable and because I had to reach $25 for free shipping, I bought two and kept one for myself. I use this dryer every day and couldn’t be happier with it. My hair is somewhat long (little below shoulders) and this dryer is light, powerful, and drys my hair quickly. It would make a terriﬁc travel dryer.

<!-- b000731 | prose | pages [35] -->
It works much better than those found in most hotel rooms. At this price you can’t go wrong. The fact that it has the dual voltage is a nice plus.

<!-- b000732 | prose | pages [35] -->
98. <Love it>(5-star rating): Love this hair dryer. Everything as described. Seriously people, hold the plug while you push the button to retract and no one gets hurt!

<!-- b000733 | prose | pages [35] -->
99. <i love it>(5-star rating): have everything i want, go ooo oo o o o o o o o o o o oo o o d

<!-- b000734 | prose | pages [35] -->
100. <Great travel blow dryer.>(5-star rating): Just the right size and power for travel.

<!-- b000735 | prose | pages [35] -->
101. <This thing is awesome!>(5-star rating): I was actually looking for something else when I stumbled upon this and thought &#34;why not&#34;. I am very pleased with this pur- chase. I have ﬁne shoulder length hair and it did not take an hour to dry, as another reviewer stated. (Of course, I didn’t attempt to dry my hair when it is dripping wet either.

<!-- b000736 | prose | pages [35] -->
I wrap my hair in a towel and do other things for a while before attempting to blow dry.)

<!-- b000737 | prose | pages [35] -->
Anyway, I was worried at ﬁrst because the packaging and most of the instructions are in Japanese. But I used it on the lower voltage and it was ﬁne. I used the regular brush to dry my hair, as I’m not sure how to use the round brush yet. I dried most of my hair and then used this upside down to give my hair some lift and bounce, which it did. Also, my hair does not look frizzy, like it does at times when using a regular blow dryer (I believe because sometimes a regular blow dryer both damages and tends to tangle your hair). My hair actually looks shiny as well as smooth (as if I ﬂat ironed it). I would give this a try if you are someone who likes the look of their hair when it is blow dried and/or ﬂat ironed but with what seems much less damage. I think you could get away with using just this dryer and a little serum (depending on how naturally straight your hair is). I am excited to use this and try to ﬁgure out the round brush too.

<!-- b000738 | prose | pages [35] -->
102. <Great product>(5-star rating): My wife has tried many hairdryers and I couldn’t believe how satisﬁed she was with this hair dryer... Totally worth it!

<!-- b000739 | prose | pages [35] -->
103. <love it>(5-star rating): Three speeds (noise) and two heat settings. My 4yr old no longer complains about blow dfying his hair cause of the queiter speeds. Great buy for yhe price.

<!-- b000740 | prose | pages [35] -->
104. <Great value!>(5-star rating): Heats instantly, dries hair very quickly and it’s much qui- eter than any other brand I’ve ever had...well worth the price.

<!-- b000741 | furniture | pages [35] -->
关注数学模型

<!-- b000742 | furniture | pages [35] -->
2

<!-- b000743 | furniture | pages [35] -->
MATHmodels

<!-- b000744 | furniture | pages [35] -->
获取更多资讯

<!-- b000745 | furniture | pages [36] -->
Team # 2002116

<!-- b000746 | furniture | pages [36] -->
Page 35 of 38

<!-- b000747 | prose | pages [36] -->
105. <Perfect>(5-star rating): Does exactly what it needs to do. Solid and durable. Gets so hot makes you wanna smack yo mama. Buy it.

<!-- b000748 | prose | pages [36] -->
106. <Love this dryer>(5-star rating): This one dries so much more quickly than my previous hair dryer and seems to provide a smoother ﬁnish. Recommended.

<!-- b000749 | prose | pages [36] -->
107. <Best Damn Hair Dryer...Period!>(5-star rating): True Story....I have spent approximately 500−700 on different hair and blow dryers. I have all from the cheap ones to the expensive ones and this is by far the best damn blow/hair dryer I’ve owned. I am a black woman with natural 4c hair that means thick and coarse and typically when blow drying my hair it feels crunchy but this dryer did not make my hair feel like that. Of course I used the LOC method with Alikay Naturals products before blow drying my hair and it turned out straight like I needed it to be. I’m super happy and satisﬁed. Also I used the hair pick yo blow dry my hair and it did not pop off nor did I break the teeth in the pick. Dynamite! If it pick does pop off just use heat resistant double side tape to keep it on.

<!-- b000750 | prose | pages [36] -->
108. <Love this hair dryer>(5-star rating): I had this hair dryer for years until the surge pro- tector button on the plug kept popping out. I bought a Conair hair dryer at Wal Mart to replace it, got home, plugged it in, and couldn’t believe how cheap and loud it sounded.

<!-- b000751 | prose | pages [36] -->
I returned it immediately, and was happy to ﬁnd that the Remington was available from Amazon.com. I’m completely sold on this hair dryer. The motor is quiet and drying time is short. The only problem is that it felt slightly heavy at ﬁrst. But after using it a few times, I suppose I got used to it because now that’s not an issue.

<!-- b000752 | prose | pages [36] -->
109. <Don’t Let The Cheap Price Fool Ya>(5-star rating): I was in need of a new hair dryer af- ter mine broke and I discovered that they don’t make it anymore. I purchased a hairdryer at a local beauty supply chain, thinking that it would work about as well as my dearly departed one. Wrong! It left my hair feeling very dry, in spite of the product I use on my hair prior to blowing it dry. I was going to invest in a CHI, but after reading mostly neg- ative reviews on that model, I decided to save my money and get this Andis hair dryer.

<!-- b000753 | prose | pages [36] -->
I have very thick, coarse, long hair (4 inches past my shoulders), and I’m transitioning from relaxer to natural. I have about 3-4 inches of new growth, and the rest is still relaxed, so straighter styles work for the time being. This hair dryer is EVERYTHING! Not only was it easy on the wallet, it gets my hair dry super quickly, while not sucking all of the moisture out of my hair. It takes less than 20 minutes to dry my hair, which is quicker than even my original blow dryer, and gets my roots pretty straight (I use the small tooth comb attachment). It’s easy to hold and gets hot without burning my scalp. Coupled with my Sedu ﬂat iron, my hair is almost salon quality, super soft and shiny! I would recommend this to anyone with the same hair texture as me. I am VERY pleased!

<!-- b000754 | prose | pages [36] -->
110. <Great Blow Dryer>(5-star rating): I bought this to replace another Remington that I’d used for a few years. So far, I’ve been really happy with my purchase. I chose this because of the quality of Remingtons I’ve had in the past, and this one seems to be just the same as the others. Quality. The blow dryer does have a slight rubbery feel. I’ve never had one like that. Can’t say I care; it’s just different. Not better or worse.<br /><br />I did choose this one speciﬁcally because of the attached diffuser. Essential for those of us with curly hair, and it works well.

<!-- b000755 | furniture | pages [36] -->
关注数学模型

<!-- b000756 | furniture | pages [36] -->
2

<!-- b000757 | furniture | pages [36] -->
MATHmodels

<!-- b000758 | furniture | pages [36] -->
获取更多资讯

<!-- b000759 | furniture | pages [37] -->
Team # 2002116

<!-- b000760 | furniture | pages [37] -->
Page 36 of 38

<!-- b000761 | prose | pages [37] -->
111. <Great dryer...>(5-star rating): Own this for a while. No problems so far. Worked as well as it did on the ﬁrst day I purchased it. Some nice features for the money

<!-- b000762 | prose | pages [37] -->
112. <honest>(5-star rating): my wife and I have used this product for at least 10 years every day and it ﬁnally wore out so I had to buy a new one.

<!-- b000763 | prose | pages [37] -->
113. <Great hair dryer wrapped into a small size!>(5-star rating): Perfect size. Does just what I want!!! No complaints!

<!-- b000764 | prose | pages [37] -->
114. <Great Product>(5-star rating): I had an Andis Hair Dryer for at least 8 years until it died on me recently.<br />The replacement is wonderful; product still as reliable as it was before!

<!-- b000765 | prose | pages [37] -->
115. <Great dryer>(5-star rating): It worked well for me, since I use it everyday. No complaints on this product. Easy to use and handle.

<!-- b000766 | heading | pages [37] -->
Appendix D

<!-- b000767 | prose | pages [37] -->
Source Code for VADER Sentiment Analysis

<!-- b000768 | prose | pages [37] -->
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #VADER is freely available athttps://github.com/cjhutto/vaderSentiment data = pd.read_csv(loadurl,sep=’\t’)[[’star_rating’,’review_headline’,’review_body’ ]] #VADER Model def transform(df):

<!-- b000769 | prose | pages [37] -->
d=df.values.tolist() for element in d:

<!-- b000770 | prose | pages [37] -->
vs1 = analyzer.polarity_scores(str(element[1])) l1=list(vs1.values()) vs2 = analyzer.polarity_scores(str(element[2])) l2=list(vs2.values()) element.append(l1,l2) return pd.DataFrame(d) data=transform(data) data.columns=[’star’,’head’,’body’,’h_sn’,’h_wn’,’h_m’,’h_wp’,’h_sp’,’b_sn’,’b_wn’, ’b_m’’b_wp’,’b_sp’] data.to_csv(outputurl)

<!-- b000771 | heading | pages [37] -->
Appendix E

<!-- b000772 | heading | pages [37] -->
Source Code for Informative Algorithm

<!-- b000773 | prose | pages [37] -->
def cosdistance(v1,v2):

<!-- b000774 | prose | pages [37] -->
vec1=v1 vec2=v2 fenmu1=1 fenmu2=math.sqrt(vec2[0]*vec2[0]+vec2[1]*vec2[1]+vec2[2]*vec2[2]+vec2[3]*vec2[3 ]+vec2[4]*vec2[4]) fenzi=vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2]+vec1[3]*vec2[3]+vec1[4]* vec2[4] return 1-fenzi/(fenmu1*fenmu2) def entropy(v1):

<!-- b000775 | prose | pages [37] -->
total=0 vec=v1 for i in range(5):

<!-- b000776 | prose | pages [37] -->
total+= vec[i]*math.log(vec[i]) return total #change data to one-hot-vector form def onehotvec(df):

<!-- b000777 | prose | pages [37] -->
data=df.values.tolist() result=np.zeros([len(data),5]).tolist() for i in range(len(data)):

<!-- b000778 | prose | pages [37, 38] -->
result[i][data[i]-1]=1 return pd.DataFrame(result) #data import data=pd.read_csv(loadurl) intvec=onehotvec(data[’star’]).values.tolist() vecvec=data[[’p1’,’p2’,’p3’,’p4’,’p5’]].values.tolist() help=pd.read_csv(r’D:\Problem_C_Data\hair_dryer.tsv’,sep=’\t’)[’helpful_votes’].

<!-- b000779 | furniture | pages [37] -->
关注数学模型

<!-- b000780 | furniture | pages [37] -->
2

<!-- b000781 | furniture | pages [37] -->
MATHmodels

<!-- b000782 | furniture | pages [37] -->
获取更多资讯

<!-- b000783 | furniture | pages [38] -->
Team # 2002116

<!-- b000784 | furniture | pages [38] -->
Page 37 of 38

<!-- b000786 | prose | pages [38] -->
values.tolist() date=pd.read_csv(r’D:\Problem_C_Data\hair_dryer.tsv’,sep=’\t’)[’review_date’] #get informative value cal=[] for i in range(len(help)):

<!-- b000787 | prose | pages [38] -->
x=(1+help[i])*pow(np.e,(-1)*cosdistance(intvec[i],vecvec[i]))*pow(np.e,1* entropy(vecvec[i])) cal.append(x) result=pd.DataFrame(cal)

<!-- b000788 | heading | pages [38] -->
Appendix F

<!-- b000789 | prose | pages [38] -->
Source Code for Reputation Calculation

<!-- b000790 | prose | pages [38] -->
def sigmoid(x):

<!-- b000791 | prose | pages [38] -->
return 1/(1+pow(np.e,(-1)*x)) def get_reputation(df):

<!-- b000792 | prose | pages [38] -->
data=df.values.tolist() data=data[::-1] curve=np.zeros(len(data)).tolist() curve[0]=1 #param set p=0.75 n=0.25 k1=25 k2=20 #k=2 for i in range(1,len(data)):

<!-- b000793 | prose | pages [38] -->
if data[i][0]>=0:

<!-- b000794 | prose | pages [38] -->
if data[i][3]==0:

<!-- b000795 | prose | pages [38] -->
curve[i]=curve[i-1]+(p-n)*data[i][0] else:

<!-- b000796 | prose | pages [38] -->
curve[i]=curve[i-1]+(p-n)*data[i][0]-sigmoid(k1*curve[i-1])*k2*data [i][1]/data[i][3] else:

<!-- b000797 | prose | pages [38] -->
if data[i][3]==0:

<!-- b000798 | prose | pages [38] -->
curve[i]=curve[i-1]+(p+n)*data[i][0] else:

<!-- b000799 | prose | pages [38] -->
curve[i]=curve[i-1]+(p+n)*data[i][0]-sigmoid(k1*curve[i-1])*k2*data [i][2]/data[i][3] return pd.DataFrame(curve) #calculate curve1=get_reputation(inputdata)

<!-- b000800 | heading | pages [38] -->
Appendix G

<!-- b000801 | heading | pages [38] -->
Source Code for Beyes Model

<!-- b000802 | prose | pages [38] -->
def word_freq(df,s):

<!-- b000803 | prose | pages [38] -->
data=df[’body’].values.tolist() count=0 for i in range(len(data)):

<!-- b000804 | prose | pages [38] -->
if s in data[i]:

<!-- b000805 | prose | pages [38] -->
count+=1 return count/len(data) def countfive_prob(data):

<!-- b000806 | prose | pages [38] -->
d=data[’star’].values.tolist() total=len(d) count=0 for i in range(len(d)):

<!-- b000807 | prose | pages [38] -->
if d[i]==5:

<!-- b000808 | prose | pages [38] -->
count+=1 return count/total def countfive_word(df,s):

<!-- b000809 | prose | pages [38, 39] -->
count=0 total=0 data=df[[’star’,’body’]].values.tolist() for i in range(len(data)):

<!-- b000810 | furniture | pages [38] -->
关注数学模型

<!-- b000811 | furniture | pages [38] -->
2

<!-- b000812 | furniture | pages [38] -->
MATHmodels

<!-- b000813 | furniture | pages [38] -->
获取更多资讯

<!-- b000814 | furniture | pages [39] -->
Team # 2002116

<!-- b000815 | furniture | pages [39] -->
Page 38 of 38

<!-- b000817 | prose | pages [39] -->
if data[i][0]==5:

<!-- b000818 | prose | pages [39] -->
total+=1 if s in str(data[i][1]):

<!-- b000819 | prose | pages [39] -->
count+=1 return count/total def train(str):

<!-- b000820 | prose | pages [39] -->
s=str data=pd.concat([data1,data2,data3],axis=0) data=data[[’head’,’body’,’0’,’star’]] five_prob=countfive_prob(data) word_star=countfive_word(data,s) word_freqency=word_freq(data,s) result=word_star*five_prob/word_freqency return result textdata=pd.read_csv(loadurl)[[’review_body’,’review_head’]] wordlist=pd.read_csv(loadurl2) #get beyes prob value of each highly frequent word result=[] for i in word:

<!-- b000821 | prose | pages [39] -->
result.append([i,train(i)]) r=pd.DataFrame(result)

<!-- b000822 | heading | pages [39] -->
Appendix H

<!-- b000823 | prose | pages [39] -->
Source Code for Time Series Prediction

<!-- b000824 | prose | pages [39] -->
from statsmodels.tsa.ar_model import AR # train autoregression model = AR(train) model_fit = model.fit() window = model_fit.k_ar coef = model_fit.params # walk forward over time steps in test history = train[len(train)-window:] history = [history[i] for i in range(len(history))] predictions = list() for t in range(len(test)):

<!-- b000825 | prose | pages [39] -->
length = len(history) lag = [history[i] for i in range(length-window,length)] yhat = coef[0] for d in range(window):

<!-- b000826 | prose | pages [39] -->
yhat += coef[d+1] * lag[window-d-1] predictions.append(yhat) error = mean_squared_error(test, predictions) print(’Test MSE: %.3f’ % error) print(’Test RMSE: %.3f’ % math.sqrt(error))

<!-- b000827 | heading | pages [39] -->
Appendix I

<!-- b000828 | prose | pages [39] -->
Source Code for Wordcloud Picture

<!-- b000829 | prose | pages [39] -->
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS txt=pd.read_csv(loadurl) my_wordcloud = WordCloud( background_color=’white’, mask=imageio.imread(pictureurl), #param set max_words=100, max_font_size=100, random_state=50, width=1000, min_font_size=20, relative_scaling=0.4, color_func=genclr, ).generate(txt) # show word cloud picture plt.imshow(my_wordcloud)

<!-- b000830 | furniture | pages [39] -->
关注数学模型

<!-- b000831 | furniture | pages [39] -->
2

<!-- b000832 | furniture | pages [39] -->
MATHmodels

<!-- b000833 | furniture | pages [39] -->
获取更多资讯
