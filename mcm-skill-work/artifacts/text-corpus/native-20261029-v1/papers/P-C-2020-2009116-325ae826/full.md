# P-C-2020-2009116-325ae826

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
2009116

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | prose | pages [1] -->
Market data tracking measurement based on sentiment analysis model

<!-- b000011 | prose | pages [1] -->
and ARIMA model

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
Amazon offers customers the opportunity to score and rate. Other customers can use these reviews to help them make purchasing decisions. Based on information such as customer reviews, companies can make decisions that increase product appeal. If the company masters the future development trend of the product, it can provide a basis for business decisions.

<!-- b000014 | prose | pages [1] -->
As for task I, in order to accurately capture the effective information in the data set, a series of data processing methods to process the missing values, abnormal values and repeated observations in the original data set, and uses the combination of qualitative and quantitative methods to screen the unrelated variables. Besides, for making a preliminary understanding of the product market satisfaction, descriptive statistics is applied. And then this paper employs Lexicon-based approach to analyze the text data, and establishes an emotion score evaluation system, which can quickly capture customer satisfaction from each comment.

<!-- b000015 | prose | pages [1] -->
The task II is divided into three subsections depending on the relevance of the issues. In subsection 1, a three-level evaluation system for star rating has been established. After using correlation test to judge the impact of comments and ratings on stars, a comprehensive evaluation system including voting information, comment content and customer identity was established by principal component analysis. On this basis, by referring to the Amazon platform crude oil star algorithm, the time span index is introduced to update the original three-level system, which makes the system more comprehensive.

<!-- b000016 | prose | pages [1] -->
For subsection 2, a time series model is introduced to study the influence of time on comment orientation. First, we visualize the time series to get the emotional trend chart of products and the time trend chart of other variables. Through image analysis, the trend of emotional score of different products is grasped, and the time trend of star rating, cumulative number of comments and cumulative number of likes of three products are obtained. Next, on the basis of the time series model, we introduce the difference autocorrelation moving average model (ARIMA), which can accurately predict the star rating situation and comment emotion trend in September and October 2015.

<!-- b000017 | prose | pages [1] -->
Finally, we discuss the influence of extreme reviews on other variables and the interaction between extreme reviews and extreme stars. In the study of the impact of the follow-up comments on the number and emotional direction of extreme stars, because the data does not conform to the characteristics of normal distribution, the non parametric test becomes the main method of this paper. The influence of extreme emotion words in the comments on the follow-up stars is analyzed in two directions: positive and negative.

<!-- b000018 | prose | pages [1] -->
In summary, the empirical analysis and models about three productions developed in this paper are also a powerful tool for other electronic business platform, showing an excellent performance.

<!-- b000019 | keywords | pages [1] -->
Keywords: Lexicon-based approach   emotion score evaluation system  principal

<!-- b000020 | prose | pages [1] -->
component analysis   time series model   ARIMA   non parametric test

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | prose | pages [1] -->
关注数学模型

<!-- b000023 | furniture | pages [1] -->
2

<!-- b000024 | furniture | pages [1] -->
MATHmodels

<!-- b000025 | furniture | pages [1] -->
获取更多资讯

<!-- b000026 | furniture | pages [2] -->
Team # 2009116

<!-- b000027 | furniture | pages [2] -->
Page 2 of 24

<!-- b000028 | prose | pages [2] -->
A Letter to the Marketing Director of the Sunshine company Dear Sir or Madam,

<!-- b000029 | prose | pages [2] -->
According to your online sales needs, our team provides some suggestions for you to solve the related problem. We propose the mathematical model to analyze the sentiment polarity and figure out the relationship between three kinds of customer feedback. We also consider how the time factor affect the rating changes and offer a simplistic model can be used to forecast rating and sentiment trend in the short term. And at last we form a COM_S parameter to define the recommended products.

<!-- b000030 | prose | pages [2] -->
More specifically, Lexicon-based approach which is based on the sentiment dictionary is used to make the text sentiment analysis in the customer-supplied review text. And an important sentiment score is developed by the approach to find out the internal relationship between review and rating variables. Then, we establish two parameters Customer Reviews (CR) and Customer Satisfaction (CS) in order to help present the specific relationship among three variables. One of these two parameters, Customer Reviews, is analyzed by the principal component analysis method. Three principal components respectively are voting information, review content and the customer. The other one of two parameter, Customer Satisfaction (CS) can also be determined by a detailed calculation formula. Finally, Comprehensive Satisfaction (COM_S) can be derived from the CS summary of the same product.

<!-- b000031 | prose | pages [2] -->
And when we consider the time factor, the time series model can be utilized to depict the trend of different variables. Moreover, we also focus on how the extreme sentiment which is manifested as one star or five stars changes itself or affects other rating variables. The result shows the extreme attitude would influence other customers, especially in a long period.

<!-- b000032 | prose | pages [2] -->
Then, we give some advices on the product current problems which is identified as the important points to modify in the future. In the process of analyzing the reviews of each products, some common product problems need paying more attention to. For microwave oven, you should pay attention to the performance and price of the product itself, and make timely improvements to the product. For the hair dryer, focus more on product performance and appearance. For pacifier, the evaluation is generally high, and the company should pay attention to the issue of product working life.We believe that our method can help your company select most possibly successful products and avoid the risky products. Followings are the recommended list:

<!-- b000033 | furniture | pages [2] -->


<!-- b000034 | prose | pages [2] -->
Successful Unsuccessful cosco alpha, Fisher, ameda, and Sealy Pacifier chicco keyfit, ikea kladd, and batman sharp, lg, magic chef, whirlpool, Microwave profile, and Panda Small

<!-- b000035 | prose | pages [2] -->
Samsung, Danby, and jx7227sfss Salon, Waterpik, Micro Tweeze, Hair dryer

<!-- b000036 | prose | pages [2] -->
Andis, conair, xtava,

<!-- b000037 | prose | pages [2] -->
DuWop, ISLAND HAWAII, Oral-B

<!-- b000038 | prose | pages [2] -->
Yours Sincerely,

<!-- b000039 | furniture | pages [2] -->
Team#2009116

<!-- b000040 | prose | pages [2] -->
mhd, remington

<!-- b000041 | prose | pages [2] -->
关注数学模型

<!-- b000042 | furniture | pages [2] -->
2

<!-- b000043 | furniture | pages [2] -->
MATHmodels

<!-- b000044 | furniture | pages [2] -->
获取更多资讯

<!-- b000045 | furniture | pages [3] -->
Team # 2009116

<!-- b000046 | furniture | pages [3] -->
Page 3 of 24

<!-- b000047 | heading | pages [3] -->
Contents

<!-- b000048 | contents | pages [3] -->
1  Introduction ......................................................................................................................... 5

<!-- b000049 | contents | pages [3] -->
Statement of the problem ......................................................................................... 5

<!-- b000050 | contents | pages [3] -->
1.1

<!-- b000051 | contents | pages [3] -->
Literature Review ...................................................................................................... 5

<!-- b000052 | contents | pages [3] -->
1.2

<!-- b000053 | contents | pages [3] -->
Overview of Our Work .............................................................................................. 5

<!-- b000054 | contents | pages [3] -->
1.3

<!-- b000055 | contents | pages [3] -->
Notations ................................................................................................................... 6

<!-- b000056 | contents | pages [3] -->
1.4

<!-- b000057 | contents | pages [3] -->
1.5 Assumptions .................................................................................................................... 6

<!-- b000058 | contents | pages [3] -->
2.Task 1 ...................................................................................................................................... 6

<!-- b000059 | contents | pages [3] -->
2.1 Problem Analysis ............................................................................................................ 6

<!-- b000060 | contents | pages [3] -->
2.2 Methodology ................................................................................................................... 7

<!-- b000061 | contents | pages [3] -->
2.3 Problem Solving .............................................................................................................. 7

<!-- b000062 | contents | pages [3] -->
2.3.1 Detail of data preprocessing ................................................................................... 8

<!-- b000063 | contents | pages [3] -->
2.3.2 Results of descriptive statistics ............................................................................... 9

<!-- b000064 | contents | pages [3] -->
2.3.3 Emotional analysis of reviews ............................................................................... 11

<!-- b000065 | contents | pages [3] -->
3. Task 2 ................................................................................................................................... 11

<!-- b000066 | contents | pages [3] -->
3.1 Problem Analysis .......................................................................................................... 11

<!-- b000067 | contents | pages [3] -->
3.2 Methodology ................................................................................................................. 11

<!-- b000068 | contents | pages [3] -->
3.3 Problem Solving ............................................................................................................ 12

<!-- b000069 | contents | pages [3] -->
3.2.1 Determination of star rating index CR .................................................................. 12

<!-- b000070 | contents | pages [3] -->
3.2.2 Analysis of Comprehensive Satisfaction ............................................................... 14

<!-- b000071 | contents | pages [3] -->
4. Task 3 ................................................................................................................................... 16

<!-- b000072 | contents | pages [3] -->
4.1 Problem Analysis .......................................................................................................... 16

<!-- b000073 | contents | pages [3] -->
4.2 Problem Solving ............................................................................................................ 16

<!-- b000074 | contents | pages [3] -->
4.2.1 Time series visualization and prediction of three variables ................................. 16

<!-- b000075 | contents | pages [3] -->
4.2.2 Prediction of star ratings ....................................................................................... 18

<!-- b000076 | contents | pages [3] -->
4.2.3 Prediction of reviews sentiment ........................................................................... 18

<!-- b000077 | contents | pages [3] -->
4.2.4 Time series analysis ............................................................................................... 18

<!-- b000078 | contents | pages [3] -->
4.2.5 Interaction between star_rating and review ........................................................ 19

<!-- b000079 | contents | pages [3] -->
5. Model Evaluation ................................................................................................................. 22

<!-- b000080 | contents | pages [3] -->
5.1 Model Limitations ......................................................................................................... 22

<!-- b000081 | contents | pages [3] -->
Time series analysis: ....................................................................................................... 22

<!-- b000082 | furniture | pages [3] -->


<!-- b000083 | furniture | pages [3] -->


<!-- b000084 | contents | pages [3] -->
关注数学模型

<!-- b000085 | furniture | pages [3] -->
2

<!-- b000086 | furniture | pages [3] -->
MATHmodels

<!-- b000087 | furniture | pages [3] -->
获取更多资讯

<!-- b000088 | furniture | pages [4] -->
Team # 2009116

<!-- b000089 | furniture | pages [4] -->
Page 4 of 24

<!-- b000090 | contents | pages [4] -->
Lexicon-based method: .................................................................................................. 22

<!-- b000091 | contents | pages [4] -->
Principal component analysis disadvantages: ............................................................... 22

<!-- b000092 | contents | pages [4] -->
5.2 Model Strengths ........................................................................................................... 22

<!-- b000093 | contents | pages [4] -->
Time series analysis: ....................................................................................................... 22

<!-- b000094 | contents | pages [4] -->
Lexicon-based method: .................................................................................................. 22

<!-- b000095 | contents | pages [4] -->
Advantages of principal component analysis: ............................................................... 23

<!-- b000096 | contents | pages [4] -->
6. Conclusion ........................................................................................................................... 23

<!-- b000097 | contents | pages [4] -->
7. References ........................................................................................................................... 24

<!-- b000098 | furniture | pages [4] -->


<!-- b000099 | furniture | pages [4] -->


<!-- b000100 | furniture | pages [4] -->


<!-- b000101 | furniture | pages [4] -->


<!-- b000102 | contents | pages [4] -->
关注数学模型

<!-- b000103 | furniture | pages [4] -->
2

<!-- b000104 | furniture | pages [4] -->
MATHmodels

<!-- b000105 | furniture | pages [4] -->
获取更多资讯

<!-- b000106 | furniture | pages [5] -->
Team # 2009116

<!-- b000107 | heading | pages [5] -->
1  Introduction

<!-- b000108 | heading | pages [5] -->
1.1 Statement of the problem

<!-- b000109 | furniture | pages [5] -->
Page 5 of 24

<!-- b000110 | prose | pages [5] -->
Online marketplace where Amazon takes the leading place has become the most important platform to trade for most companies. As the mechanism for customers to communicate shopping experience with each other, various kinds of reviews and ratings provide potential consumers with subjective evidence. It can also provide the guidance for new entrants in choosing a target market and target product. In addition, in the social media era, consumers have louder and stronger voices than ever before, which is shown as over 50% of consumers frequently factor in online reviews before buying a product.[1] Because this process can be seen as a direct link to the former customer, getting the first-hand information of product in order to avoid the exaggeration or of the seller.

<!-- b000111 | prose | pages [5] -->
However, at this stage, it is not clear that their interaction, and how they influence the corporate strategy. Thus, we aim to explore the internal relationship of three variables and design a composite data measure to assist companies in the selection of potential successful products. Meanwhile, we discuss how the customer group reviews influence on individual review attitude orientation. At last, we rank the alternative products according to our method and offer a recommendation list to Sunshine company.

<!-- b000112 | heading | pages [5] -->
1.2 Literature Review

<!-- b000113 | prose | pages [5] -->
At present, there are mainly two methods for sentiment analysis, one is based on machine learning, and the other is based on the lexicon. Several approaches based on the machine learning have come into the spotlight in recent years and most of them are based on the big amount of personalized reviews from social media. Due to the reviews in the social media are not only English, but other languages such as Arabic. [2] Many researchers from non-English regions also apply this method to solve the issue, showing that this method is quite mature.

<!-- b000114 | prose | pages [5] -->
And the other method is the Lexicon based approach. This method also utilizes the text which expresses people’s sentiment or emotion in their social media, such as the Twitter posts and Micro-blog text. [3,4] Latest researches on the sentiment polarity lexicon also show the resource of the lexicon is extended to a particular domain, the stock market, without human intervention and addressing the scaling and thresholding problem. [5] Therefore, we believe that this method is potential to be widely used.

<!-- b000115 | prose | pages [5] -->
After we compared the two methods, we determine to choose the Lexicon-based approach. We believe that this method is most applicable when time and resources are limited, that is, similar to the conclusions obtained in the study of Urdu's Sentiment Analysis. [6]

<!-- b000116 | prose | pages [5] -->
After introducing the time factor, we propose a time series model to discuss the changes of three variables in the time dimension. After comparing several applicable models, we choose to use the traditional time series models and the Autoregressive Integrated Moving Average (ARIMA) model to observe the influence of time factors on different reviews and to predict the future indicator trend. We think that during the forecasting phase, the ARIMA model can achieve a quite accurate forecasting as theories of Matyjaszek, M. et al. [7] At the same time, we also conducted product forecasting of different products by product. This is in line with Nguyen, H. et al. The model's predictions for different product prices are similar [8].

<!-- b000117 | heading | pages [5] -->
1.3 Overview of Our Work

<!-- b000118 | prose | pages [5] -->
Our main goals are to address three issues that need to be explored: (1) the sentiment analysis of text reviews; (2) the relationship between reviews and ratings indicators and (3) the impact of time. Then we propose the product sequencing method which these three contents combined with.

<!-- b000119 | prose | pages [5] -->
In order to solve these problems, we first analyze the data characteristics of each digital parameter, and then apply the sentiment lexicon-based method to analyze the emotional attitude of the text of the text review, extract the emotional words in the

<!-- b000120 | furniture | pages [5] -->


<!-- b000121 | furniture | pages [5] -->


<!-- b000122 | prose | pages [5] -->
关注数学模型

<!-- b000123 | furniture | pages [5] -->
2

<!-- b000124 | furniture | pages [5] -->
MATHmodels

<!-- b000125 | furniture | pages [5] -->
获取更多资讯

<!-- b000126 | furniture | pages [6] -->
Team # 2009116

<!-- b000127 | furniture | pages [6] -->
Page 6 of 24

<!-- b000128 | prose | pages [6] -->
sentence through the inner join, and then calculate the sentence sentiment scores. This process of sentiment scoring is used to distinguish between the positive and negative attitudes of a sentence. Then by comparing text reviews and two rating variables, we get Customer Review (CR) to discuss how star ratings are affected by review factors, and then we discuss the influencing factors of Customer Satisfaction (CS) and draw a quantitative relationship. After that, we formed Comprehensive Satisfaction (COM_S) according to the product satisfaction based on the satisfaction of each customer. And we use this data measure to screen our candidate products and provide Sunshine Company with a list of alternative product suitable for online sales.

<!-- b000129 | heading | pages [6] -->
1.4 Notations

<!-- b000130 | prose | pages [6] -->
Symbol P H M hv tv sq sr n v vp ci pp D 𝐹1 𝐹2 𝐹3 CR CS COM_S

<!-- b000131 | heading | pages [6] -->
1.5 Assumptions

<!-- b000132 | prose | pages [6] -->
Definition Pacifier Hair dryer Microwave helpful_votes total_votes SentimentQDAP star_rating number vine verified_purchase customer_id product_parent day First principal component Second principal component Third principal component Customer Review Customer Satisfaction Comprehensive Satisfaction

<!-- b000133 | prose | pages [6] -->
⚫ We assume that past trends of things will extend to the future. The reality of things is the result of historical development, and the future of things is an extension of reality. The past and future of things are connected. ⚫ We assume that the data which forecast based on is irregular. ⚫ We assume that there is no causality between market developments. ⚫ We assume that there are no other relevant random variable changes that affect the time series analysis. ⚫ We assume that the variables contained in the given data set can fully reflect the comprehensive score of the product. ⚫ We assume that the dictionary selected by Lexicon-based method sentiment analysis contains all the required words. ⚫ We assume when there are multiple sentences in a customer review, the average of the sentiment scores of all sentences can represent the emotional score of the customer. ⚫ We assume that customer reviews are simple logical relationship without the use of derogatory words to indicate positive meanings, nor the complex combination of negative words, degree adverbs, and emotional words. ⚫ We assume that the definition of affective words in the affective dictionary is not controversial.

<!-- b000134 | prose | pages [6] -->
2.Task 1

<!-- b000135 | heading | pages [6] -->
2.1 Problem Analysis

<!-- b000136 | prose | pages [6] -->
Because of the large amount of data provided by this topic, and mostly in the form of text, the focus of this topic is the preprocessing of original data and the extraction of

<!-- b000137 | prose | pages [6] -->
关注数学模型

<!-- b000138 | furniture | pages [6] -->
2

<!-- b000139 | furniture | pages [6] -->
MATHmodels

<!-- b000140 | furniture | pages [6] -->
获取更多资讯

<!-- b000141 | furniture | pages [7] -->
Team # 2009116

<!-- b000142 | furniture | pages [7] -->
Page 7 of 24

<!-- b000143 | prose | pages [7] -->
text information. In the processing of solving task 1, this paper first uses a series of

<!-- b000144 | heading | pages [7] -->
data processing methods to process the missing values, abnormal values and repeated

<!-- b000145 | prose | pages [7] -->
observations in the original data set, and uses the combination of qualitative and quantitative methods to screen the unrelated variables. This step can not only remove the interference of miscellaneous information, but also accurately capture the effective information in the data set. Next, this paper makes descriptive statistics on the different variables of three kinds of commodities to make a preliminary understanding of the product market satisfaction. Finally, this paper uses the Lexicon-based approach to analyze the text data, and establishes an emotion score evaluation system, which can quickly capture customer satisfaction from each comment.

<!-- b000146 | heading | pages [7] -->
2.2 Methodology

<!-- b000147 | prose | pages [7] -->
The section is parted into three subsections, data preprocessing, descriptive statistics and Lexicon-based approach. In these subsections, the ideology of modelling in task 1 are introduced. 2.2.1 Data preprocessing Due to the huge amount of data in the design of this problem, in order to remove the influence of interference information and extract the effective information in the data, the pretreatment of the original data is a crucial step in solving the problem. The data preprocessing in this paper can be divided into the following steps: Step 1. Check for duplicate observations in the original data set Step 2. Handling of missing value and abnormal value Step 3. Standardization of observation data Step 4. Delete useless variables 2.2.2 Lexicon-based approach At present, there are two methods to solve the problem of emotion analysis: one is based on machine learning, the other is based on emotion dictionary.

<!-- b000148 | prose | pages [7] -->
For machine learning based methods, a large number of manually labeled corpus is input as training set, and emotion classification is realized by extracting text features and constructing classifier. It’s difficult for us to do this because of the limitation of our personal computers and the length of the contest。 At the same time, because we are not clear about the internal relationship between the known classification and the comment text, this method is not suitable for the solution of this problem.

<!-- b000149 | prose | pages [7] -->
Therefore, we choose the method based on emotion dictionary, which only uses the known text and emotion dictionary first, and does not involve other rating indicators. The three dictionaries cited in this paper are: (1) Dictionary with opinionated words from the Harvard-IV dictionary asused in the General Inquirer software

<!-- b000150 | prose | pages [7] -->
Dictionary with a list of positive and negative words according to the psychological Harvard-IV dictionary as used in the General Inquirer software. This is a general-purpose dictionary developed by the Harvard University. (2) Dictionary with opinionated words from Henry’s Financial dictionary

<!-- b000151 | prose | pages [7] -->
Dictionary with a list of positive and negative words according to the Henry’s finance-specific dictionary. This dictionary was first presented in the Journal of Business Communication among one of the early adopters of text analysis in the finance discipline. (3) Dictionary with opinionated words from Loughran-McDonald Financial dictionary

<!-- b000152 | prose | pages [7] -->
Dictionary with a list of positive, negative and uncertainty words according to the Loughran-McDonald finance-specific dictionary. This dictionary was first presented in the Journal of Finance and has been widely used in the finance domain ever since.

<!-- b000153 | prose | pages [7] -->
General steps are shown as following. First, by collecting the related text information, they created the specific dataset with text, user, emotion, sentiment information. Then, the sentiment dictionary can be extended by extraction and construction of a series of related dictionaries. Next, the sentiment value of a text can be obtained through the calculation of the weight. Eventually, the researchers got influence score to achieve their final goal.

<!-- b000154 | heading | pages [7] -->
2.3 Problem Solving

<!-- b000155 | prose | pages [7] -->
关注数学模型

<!-- b000156 | furniture | pages [7] -->
2

<!-- b000157 | furniture | pages [7] -->
MATHmodels

<!-- b000158 | furniture | pages [7] -->
获取更多资讯

<!-- b000159 | furniture | pages [8] -->
Team # 2009116

<!-- b000160 | furniture | pages [8] -->
Page 8 of 24

<!-- b000161 | prose | pages [8] -->
For the convenience of follow-up work, copy the contents of original hair dryer.tsv, microwave.tsv and pacifier.tsv files to excel and save them as CSV files. Data set pacifier.csv contains 18939 observations and 16 variables; microwave.csv contains 1615 observations and 16 variables; hair_dryer.csv contains 11470 observations and 16 variables. The 16 variables in the three files are the same, and the variables are divided into character type variables and numerical type variables. Among the variables, star rating, helpful voices and review body are the most important research objects; review ID is the comment number, which is the identification variable and unique. Variables also include product information, market information, customer information and comment information.

<!-- b000162 | heading | pages [8] -->
2.3.1 Detail of data preprocessing

<!-- b000163 | prose | pages [8] -->
Step 1. Check for duplicate observations in the original data set

<!-- b000164 | prose | pages [8] -->
Import the file into the SAS system, use the nodupkey option in the proc sort process to check whether there are duplicate observations in the data set, and use the review [ID] as the identification variable. If there are duplicate observations, store them in the work.dup data set. The inspection results of the three files show that there is no observation in the data set work.dup, so it shows that there is no repeated observation in the original data set. Step 2. Handling of missing value and abnormal value (1) Missing values

<!-- b000165 | prose | pages [8] -->
In Excel, you can simply check the missing value and fill in the missing value. The product "category" in pacifier.csv is missing. Pacifier is a baby product and can be filled directly. In addition, 8 observations with missing important information were found. These eight observations were deleted, leaving 18931 observations. There are 7 missing values in the review date variable of hair-dryer.csv, which can be supplemented manually. There is no missing value for microwave.csv. (2) Abnormal values

<!-- b000166 | prose | pages [8] -->
First, we use the proc contents process to generate the variable description table work.var, then we use the proc SQL process to define the character type variable as the macro variable var_char, and the numerical type variable as the macro variable var_num, In order to call character type variable and numerical type variable more efficiently in the later process; then use the nmiss option of proc means process to check the missing value in numerical type variable, use the missing option of tables statement in proc freq process to check the missing value in character type variable, and check the frequency distribution of character type variable. The results show that there are no missing values in character type variables, 14 missing values in review [data] in packer.csv file and no missing values in other variables. There are no obvious error values. Delete 14 observations with missing values in the pacifier file, 18917 observations and 1615 observations in the microwave file, including 11470 observations. Step 3. Standardization of observation data

<!-- b000167 | prose | pages [8] -->
Amazon is a platform with a strong freedom of comment, so there are a lot of junk comments that need to be removed. According to the observation, there are many junk comments or useless comments in the comments, and we need to filter them out. In addition, we need to analyze the emotion and attitude through the comment content, so useless comments with too short length also need to be removed. In order to facilitate the follow-up work, it is necessary to standardize the comment text. (1) Delete too short comment

<!-- b000168 | prose | pages [8] -->
Use the length statement to check the string length of the review body observed in each of the three files. If the string length is less than 20, delete the comment. There are 1674 observation review bodies in the pacifier file with a string length less than 20, 738 observation review bodies in the hair dryer file with a string length less than 20, and 79 observation review bodies in the microwave file with a string length less than 20. (2) Standardize data.

<!-- b000169 | prose | pages [8] -->
In order to facilitate the subsequent extraction of important information in review body, it is necessary to delete the punctuation in the review, modify all uppercase to lowercase, use tranwrd function to delete punctuation, and use translate function to

<!-- b000170 | prose | pages [8] -->
关注数学模型

<!-- b000171 | furniture | pages [8] -->
2

<!-- b000172 | furniture | pages [8] -->
MATHmodels

<!-- b000173 | furniture | pages [8] -->
获取更多资讯

<!-- b000174 | furniture | pages [9] -->
Team # 2009116

<!-- b000175 | furniture | pages [9] -->
Page 9 of 24

<!-- b000176 | prose | pages [9] -->
modify uppercase to lowercase in the review. In addition, use the translate function to modify the upper case observations of the variable vine and the variable verified_. Step 4. Delete useless variables

<!-- b000177 | prose | pages [9] -->
There are some useless variables in the file that can be deleted. The three files market place are the same, which can be deleted. Product ID, product title and product parent can uniquely identify the product. Just keep one of the three, and keep product parent. Product category and review headline are useless variables and can be deleted. Use drop statement to delete useless variables.

<!-- b000178 | prose | pages [9] -->
Finally, 1674 observations are deleted from the pacifier file, 17243 observations and 10 variables are reserved. 738 observations were deleted from the hair guy file, 10732 observations and 10 variables were reserved. In the microwave file, 79 observations are deleted, 1536 observations and 10 variables are reserved.

<!-- b000179 | heading | pages [9] -->
2.3.2 Results of descriptive statistics

<!-- b000180 | prose | pages [9] -->
(1) Star_ratings

<!-- b000181 | furniture | pages [9] -->


<!-- b000182 | caption | pages [9] -->
Figure 1  The satr_rating of product analysis chart

<!-- b000183 | prose | pages [9] -->
As shown in the table above, it is the star ratings frequency table and proportion of three products. According to the table data, we can preliminarily know that five-star rating accounts for the largest proportion of the three products, and two-star rating accounts for the smallest proportion. For microwave, star ratings are concentrated on one and five stars, while star ratings of hair player and pacifier are concentrated on five stars, and the proportion of other stars is very low.

<!-- b000184 | prose | pages [9] -->
The above figure is the star ratings frequency distribution diagram of the three products. According to the distribution diagram, one conclusion can be drawn that people buyers of pacifier and hair player are more likely to give favorable comments. Pacifier and hair player are relatively successful products made by Amazon. However, buyers of microwave are more likely to give a low rating, indicating that Amazon's microwave is not very successful. (2) Reviews

<!-- b000185 | prose | pages [9] -->
Customers' comments on products directly reflect the success of products. According to product reviews, we can explore customers' satisfaction with the use of the product, so as to find the popularity of the product and the existing problems. According to the top 50 words in the comments, we drew a word cloud map. As shown

<!-- b000186 | prose | pages [9] -->
关注数学模型

<!-- b000187 | furniture | pages [9] -->
2

<!-- b000188 | furniture | pages [9] -->
MATHmodels

<!-- b000189 | furniture | pages [9] -->
获取更多资讯

<!-- b000190 | furniture | pages [10] -->
Team # 2009116

<!-- b000191 | furniture | pages [10] -->
Page 10 of 24

<!-- b000192 | prose | pages [10] -->
in the figure below, it is a word cloud map drawn according to the reviews of three products.

<!-- b000193 | furniture | pages [10] -->


<!-- b000194 | furniture | pages [10] -->


<!-- b000195 | caption | pages [10] -->
Figure 2  Word cloud diagram based on three product reviews

<!-- b000196 | prose | pages [10] -->
For microave, the products discussed by customers are button, space, month, price, year, size, works, counter, small. The words reflecting customers' emotional attitude include great, well, problem, good, small, sampling, o ld, etc. It shows that customers' comments on microwave are good or bad. Sunshine company should pay attention to the performance and price of the product itself, and make timely improvement on the product.

<!-- b000197 | prose | pages [10] -->
Customers talk more about hair dryer products themselves, such as cord, long, setting, hot, air, power, price, nice, etc. The words that reflect customers' emotional attitude include great, love, right, like, dry, etc. It shows that the customer's evaluation of hair dryer is generally better. Sunshine company should pay attention to product performance and appearance, and find out the factors of product success.

<!-- b000198 | prose | pages [10] -->
For pacifier, the product itself is often discussed by customers in terms of month, time and cute. The words that reflect customers' emotional attitude include great, love, etc. It shows that customers generally have a high evaluation of pacifier, and sunshine company has done well in the baby market. The company should pay attention to the service life of the products. (3) Helpfulness ratings

<!-- b000199 | caption | pages [10] -->
Table 1  General analysis table of helpfulness ratings

<!-- b000200 | prose | pages [10] -->
product helpful_votes microwave 8996 hair dryer 24938 pacifier 15244 total_votes ratio 10635 0.846 29202 0.854 20708 0.736

<!-- b000201 | caption | pages [10] -->
Table 2  Relationship table of star_ratings and helpfulness ratings

<!-- b000202 | prose | pages [10] -->
ratings helpful_votes 1 9418 2 3052 3 4362 4 7948 5 24398 total_votes helpful/total 12798 0.735896234 4284 0.712418301 5778 0.754932503 9539 0.833211028 28146 0.866837206 As shown in the table above, the total number of useful votes, the total number of votes and the proportion of useful votes in the total votes of the sub products are depicted. According to the statistical results, the proportion of effective reviews of hair dryer customers is the largest, while that of pacifier is the smallest.

<!-- b000203 | prose | pages [10] -->
In addition, we think about whether there is a relationship between star ratings and helpfulness ratings. Therefore, we calculated the percentage of useful comments by star rating.

<!-- b000204 | prose | pages [10] -->
关注数学模型

<!-- b000205 | furniture | pages [10] -->
2

<!-- b000206 | furniture | pages [10] -->
MATHmodels

<!-- b000207 | furniture | pages [10] -->
获取更多资讯

<!-- b000208 | furniture | pages [11] -->
Team # 2009116

<!-- b000209 | furniture | pages [11] -->
Page 11 of 24

<!-- b000210 | caption | pages [11] -->
Table 3  Analysis table of helpful reviews proportion by star ratings

<!-- b000211 | prose | pages [11] -->
proportion 1 2 pacifier 0.61 0.66 microwave 0.806 0.70 hair dryer 0.78 0.78 3 4 5 0.65 0.78 0.805 0.80 0.82 0.91 0.801 0.88 0.90 According to the analysis of the effective voting percentage of the stars, for pacifier and hair dryer, it can provide more effective information to give high scoring customer reviews. However, for microave, whether it's high score or low score customer reviews, it can provide more effective information.

<!-- b000212 | heading | pages [11] -->
2.3.3 Emotional analysis of reviews

<!-- b000213 | prose | pages [11] -->
Step 1. Divide sentences

<!-- b000214 | prose | pages [11] -->
Because the comments and other variables in the design of this topic all exist in the text situation, the ontology first divides the text to be analyzed according to the grammar. In this paper, inner join is used to extract the emotional words in the text Step 2. Classification of emotional words

<!-- b000215 | prose | pages [11] -->
According to the emotional dictionary, the words extracted in the previous step are classified into commendatory words list, derogatory words list, neuter words list, negative words and degree adverbs, and then the emotional classifiers list and its emotional intensity are obtained, Step 3. Remove function words

<!-- b000216 | prose | pages [11] -->
Function words refer to a kind of words that have no actual meaning. Compared with other words, function words are frequently used, such as' the ',' is', 'at', 'which', 'on', etc. In addition, there is also a kind of words, such as the word "want". In search engines, such words do not help search results much. Their emergence is not only difficult to help users narrow the scope of search, but also reduce search efficiency. Therefore, this paper removes these words from the problem, so as to improve the efficiency of text utilization. Step 4. Calculate the sentiment score of each review

<!-- b000217 | prose | pages [11] -->
For example, the review title of the review_id in hair_dryer is R100TKSFK51G4K and the title is: "great blow dryer great price and very light weight". The number of active words after segmentation and removal of function words is 7, the negative emotion score is 0, the positive emotion score is 0.2857, and the final emotional score is 0.2857.

<!-- b000218 | heading | pages [11] -->
3. Task 2

<!-- b000219 | heading | pages [11] -->
3.1 Problem Analysis

<!-- b000220 | prose | pages [11] -->
In order to explore the impact of reviews and ratings on the Customer Reviews （CR）, we sorted out seven variables and tested their correlations. Due to the correlation between the variables, we use the principal component method to divide the variables of the period into three principal components. Based on this, we obtain the calculation formula for Customer Reviews (CR). Combining CR and review time, we calculate the Customer Satisfaction (CS) for each review and standardize CS. Then, according to the product classification, the Comprehensive Satisfaction （COM_S） of the buyer for the specific product can be obtained. Finally, we sorted each product of pacifier, hair dryer, and Microwave oven according to the comprehensive satisfaction, and analyzed the information of successful products and information of failed products.

<!-- b000221 | heading | pages [11] -->
3.2 Methodology

<!-- b000222 | prose | pages [11] -->
Based on the study of the above models, we introduce a time series model to study the influence of time factors on comment orientation. (1) Autoregressive model: An autoregressive model is a model that describes the relationship between current values and historical values. It is a method of predicting itself using the historical event data of the variable itself.

<!-- b000223 | prose | pages [11] -->
关注数学模型

<!-- b000224 | furniture | pages [11] -->
2

<!-- b000225 | furniture | pages [11] -->
MATHmodels

<!-- b000226 | furniture | pages [11] -->
获取更多资讯

<!-- b000227 | furniture | pages [12] -->
Team # 2009116

<!-- b000228 | furniture | pages [12] -->
Page 12 of 24

<!-- b000229 | prose | pages [12] -->
𝑝 𝑝

<!-- b000230 | prose | pages [12] -->
𝜖𝑡

<!-- b000231 | prose | pages [12] -->
𝑦𝑡= 𝜇+ ∑𝛾𝑖𝑦𝑡−𝑖+

<!-- b000232 | prose | pages [12] -->
𝑖=1

<!-- b000233 | prose | pages [12] -->
𝑦𝑡 is the current value; 𝜇 is the constant term; p is the order; 𝛾𝑖 is the autocorrelation coefficient, and 𝜖𝑡 is the error value (2) Integrated: The most important part of the ARIMA model is the smoothness of the time series data. Stationarity is the requirement that the fitted curve obtained through the sample time series can continue inertia along the existing morphology in the short time in the future, that is, the mean and variance of the data should not theoretically change too much. (3) Moving average: The moving average model focuses on the accumulation of error terms in the autoregressive model. It can effectively eliminate random fluctuations in predictions.

<!-- b000234 | prose | pages [12] -->
𝑞

<!-- b000235 | furniture | pages [12] -->


<!-- b000236 | prose | pages [12] -->
𝑦𝑡= 𝜇+ 𝜖𝑡+ ∑𝜃𝑖𝜖𝑡−𝑖

<!-- b000237 | prose | pages [12] -->
𝑝

<!-- b000238 | prose | pages [12] -->
𝑦𝑡= 𝜇+ ∑𝛾𝑖𝑦𝑡−𝑖

<!-- b000239 | prose | pages [12] -->
𝑖=1

<!-- b000240 | heading | pages [12] -->
3.3 Problem Solving

<!-- b000241 | prose | pages [12] -->
𝑖=1

<!-- b000242 | prose | pages [12] -->
𝑞

<!-- b000243 | furniture | pages [12] -->


<!-- b000244 | prose | pages [12] -->
+ 𝜖𝑡+ ∑𝜃𝑖𝜖𝑡−𝑖

<!-- b000245 | prose | pages [12] -->
𝑖=1

<!-- b000246 | heading | pages [12] -->
3.2.1 Determination of star rating index CR

<!-- b000247 | prose | pages [12] -->
The number of characters in review_body that contain emotional information and comments. We choose the method based on sentiment lexicon to extract emotion words by using inner join, and calculate the emotion score of each text according to the score of emotion words. SentimentQDAP is used to express emotion score. In addition, the number of characters in the comments can also reflect the star rating results of customers. The number of characters for a comment is number. Step 1. Impact indicators of star ratings

<!-- b000248 | prose | pages [12] -->
In the discussion of the final result of star rating, if the time factor is not considered first, only the impact of comments and ratings on star rating is discussed. We call this star rating indicator customer reviews. The main factors influencing customer reviews are helpful_votes (hv), total_votes (tv), sentimentqdap (sq), star_rating (sr), number (n), vine (v), verified_purchase (vp), customer_id (ci) and product_parent (pp). There may be correlation between variables, so we test the correlation of variables first. If the correlation coefficient is greater than or equal to 0.3, we think that there is a good linear correlation between variables. According to the correlation test, we found that correlation exists in some of the variables.

<!-- b000249 | caption | pages [12] -->
Table 1  Test of correlation

<!-- b000250 | prose | pages [12] -->
Step 2. Principal component analysis

<!-- b000251 | furniture | pages [12] -->


<!-- b000252 | prose | pages [12] -->
Principal component analysis is to use the idea of dimensionality reduction to explain most of the variables in the original data with fewer variables, and transform many variables we have with high correlation into independent or uncorrelated variables. It will usually select several new variables that can explain most of the

<!-- b000253 | prose | pages [12] -->
关注数学模型

<!-- b000254 | furniture | pages [12] -->
2

<!-- b000255 | furniture | pages [12] -->
MATHmodels

<!-- b000256 | furniture | pages [12] -->
获取更多资讯

<!-- b000257 | furniture | pages [13] -->
Team # 2009116

<!-- b000258 | furniture | pages [13] -->
Page 13 of 24

<!-- b000259 | prose | pages [13] -->
variables, namely the so-called principal components, and use them to explain the comprehensive indicators of the data. ⚫ Justification of Our Approach

<!-- b000260 | prose | pages [13] -->
According to the results of Bartlett's test, the p value of Bartlett's test is less than 0.001, and the hypothesis of zero is rejected, that is to say, the research data can be extracted by principal components.

<!-- b000261 | caption | pages [13] -->
Table 2  KMO and Bartlett Test

<!-- b000262 | prose | pages [13] -->
Kaiser-Meyer-Olkin test sampling adequacy .524

<!-- b000263 | prose | pages [13] -->
Chi-square value Bartlett Sphericity Test

<!-- b000264 | prose | pages [13] -->
df

<!-- b000265 | prose | pages [13] -->
145929.849

<!-- b000266 | prose | pages [13] -->
21

<!-- b000267 | prose | pages [13] -->
Significance ⚫ Dividing principal components .000

<!-- b000268 | prose | pages [13] -->
Previous scholars also believed that the extracted principal components should account for 60-70% of data variation. The results of principal component extraction showed that the eigenvalues of the first three principal components are greater than 1, which account for 31.025%, 22.117% and 16.597% of the total data variation, and 69.738% of the total data. The number of principal components extracted is 3.

<!-- b000269 | caption | pages [13] -->
Table 3  Illustrated Variation Statistics

<!-- b000270 | prose | pages [13] -->
Intercept and load square

<!-- b000271 | furniture | pages [13] -->


<!-- b000272 | prose | pages [13] -->
Initial eigenvalue Loop and load square

<!-- b000273 | prose | pages [13] -->
Vara-

<!-- b000274 | prose | pages [13] -->
Total

<!-- b000275 | prose | pages [13] -->
Cumu-

<!-- b000276 | prose | pages [13] -->
Total

<!-- b000277 | prose | pages [13] -->
Vara-

<!-- b000278 | prose | pages [13] -->
Cumu-

<!-- b000279 | prose | pages [13] -->
Total Vara-

<!-- b000280 | prose | pages [13] -->
Cumu-

<!-- b000281 | prose | pages [13] -->
tion%

<!-- b000282 | prose | pages [13] -->
lative%

<!-- b000283 | prose | pages [13] -->
tion%

<!-- b000284 | prose | pages [13] -->
lative%

<!-- b000285 | prose | pages [13] -->
tion%

<!-- b000286 | prose | pages [13] -->
lative%

<!-- b000287 | prose | pages [13] -->
31.025 1 2.172 31.025 31.025 2.172 31.025 2.006 28.663 28.663 22.117 2 1.548 22.117 53.141 1.548 53.141 1.518 21.687 50.350 16.597 3 1.162 16.597 69.738 1.162 4 0.813 11.620 81.359

<!-- b000288 | furniture | pages [13] -->


<!-- b000289 | furniture | pages [13] -->


<!-- b000290 | prose | pages [13] -->
5 0.742 10.605 91.964

<!-- b000291 | furniture | pages [13] -->


<!-- b000292 | furniture | pages [13] -->


<!-- b000293 | prose | pages [13] -->
6 0.557 7.959 99.923

<!-- b000294 | furniture | pages [13] -->


<!-- b000295 | furniture | pages [13] -->


<!-- b000296 | prose | pages [13] -->
7 0.005 0.077 100.000

<!-- b000297 | furniture | pages [13] -->


<!-- b000298 | furniture | pages [13] -->


<!-- b000299 | prose | pages [13] -->
⚫ Judgment of interpretation ability 69.738 1.357 19.389 69.738

<!-- b000300 | furniture | pages [13] -->


<!-- b000301 | furniture | pages [13] -->


<!-- b000302 | furniture | pages [13] -->


<!-- b000303 | furniture | pages [13] -->


<!-- b000304 | furniture | pages [13] -->


<!-- b000305 | furniture | pages [13] -->


<!-- b000306 | furniture | pages [13] -->


<!-- b000307 | furniture | pages [13] -->


<!-- b000308 | furniture | pages [13] -->


<!-- b000309 | furniture | pages [13] -->


<!-- b000310 | furniture | pages [13] -->


<!-- b000311 | furniture | pages [13] -->


<!-- b000312 | furniture | pages [13] -->


<!-- b000313 | furniture | pages [13] -->


<!-- b000314 | furniture | pages [13] -->


<!-- b000315 | furniture | pages [13] -->


<!-- b000316 | prose | pages [13] -->
The extracted principal components should have certain significance, that is, the ability to interpret the research content. The ability of interpretation suggests that the first three principal components are in line with the actual needs of the study. The ability of each principal component to interpret the corresponding variables (the data with correlation coefficient less than 0.3 has been eliminated), as shown in the following table:

<!-- b000317 | prose | pages [13] -->
Interpretation ability of corresponding variables of principal components

<!-- b000318 | caption | pages [13] -->
Table 4  Interpretation ability of corresponding variables of principal components

<!-- b000319 | prose | pages [13] -->
1

<!-- b000320 | prose | pages [13] -->
helpful_votes .996

<!-- b000321 | prose | pages [13] -->
total_votes .995

<!-- b000322 | prose | pages [13] -->
SentimentQDAP

<!-- b000323 | prose | pages [13] -->
star_rating

<!-- b000324 | prose | pages [13] -->
number

<!-- b000325 | prose | pages [13] -->
vine

<!-- b000326 | prose | pages [13] -->
verified_purchase

<!-- b000327 | prose | pages [13] -->
2 3

<!-- b000328 | prose | pages [13] -->
.801

<!-- b000329 | prose | pages [13] -->
.743

<!-- b000330 | prose | pages [13] -->
.503

<!-- b000331 | prose | pages [13] -->
.786

<!-- b000332 | prose | pages [13] -->
.726 It can be seen from the table above that the variable information interpreted by the first three principal components is basically the same as that of the classification. The first principal components (F1) are helpful_votes and total_votes. The second principal components (F2) are SentimentQDAP, star_rating and number. The third principal component (F3) is vine, verified purchase and number. Correspondingly, the first principal component mainly reflects the voting information of the comment, the second principal component mainly reflects the content of the comment, and the third principal

<!-- b000333 | prose | pages [13] -->
关注数学模型

<!-- b000334 | furniture | pages [13] -->
2

<!-- b000335 | furniture | pages [13] -->
MATHmodels

<!-- b000336 | furniture | pages [13] -->
获取更多资讯

<!-- b000337 | furniture | pages [14] -->
Team # 2009116

<!-- b000338 | furniture | pages [14] -->
Page 14 of 24

<!-- b000339 | prose | pages [14] -->
component mainly reflects the customer identity information. The extraction of the first three principal components has a good result interpretation ability.

<!-- b000340 | prose | pages [14] -->
Based on this, we can deduce the basic expressions of three principal components:

<!-- b000341 | prose | pages [14] -->
𝐹1 = 0.996 ∗ℎ𝑣+ 0.995 ∗𝑡𝑣 𝐹2 = 0.801 ∗𝑠𝑞+ 0.743 ∗𝑠𝑟+ 0.503 ∗𝑛

<!-- b000342 | prose | pages [14] -->
𝐹3 = 0.786 ∗𝑣+ 0.726 ∗𝑣𝑝 Step 3. Data element of Customer Reviews

<!-- b000343 | prose | pages [14] -->
According to the results of principal component analysis, the first principal component reflects the voting information of the comment, the second principal component reflects the content of the comment, and the third principal component reflects the customer identity information. It shows that the voting information is the main factor determining the final score of customer reviews, followed by the content of reviews, and finally the customer identity. The level of customer reviews directly reflects the level of customer satisfaction with products. The customer reviews (CR) score can be obtained by giving different weights to different variables. The CR calculation formula is as follows:

<!-- b000344 | prose | pages [14] -->
𝐶𝑅= 𝛼1 ∗𝐹1 + 𝛼2 ∗𝐹2 + 𝛼3 ∗𝐹3

<!-- b000345 | heading | pages [14] -->
3.2.2 Analysis of Comprehensive Satisfaction

<!-- b000346 | prose | pages [14] -->
Step 1. Customer satisfaction Influence factor

<!-- b000347 | prose | pages [14] -->
As the most experienced e-commerce company, Amazon will surely fully understand the psychology of customers, and in particular will extract the reviews that have been recognized by the most customers. It is understood that Amazon has a specialized intelligent machine (machine learned model) that uses a complex star algorithm to give products a star rating. The parameters with the highest weight in the star algorithm are: (1) The date of the review. The longer the date is, the more valuable it is; (2) Helpful clicks. When a customer clicks "helpful", it means that this review is useful. (3) Whether the review comes from Verified Purchases (VP).

<!-- b000348 | prose | pages [14] -->
In addition to the above three parameters with larger weights of Amazon rolls, the star algorithm also refers to other indicators with smaller weights: (1) The number of characters in the review, that is, the length of the sentence; (2) Review original score, that is, Review ratings given by each buyer; (3) The contents of the Review. When building the model, we chose a sentiment dictionary-based method to extract the sentiment words by using inner join, and calculated the sentiment score of each review according to the scores of the sentiment words.

<!-- b000349 | prose | pages [14] -->
In the above, we used the principal component analysis method to divide the factors that determine the Customer Reviews (CR) score into three categories: vote information for reviews, content of reviews, and customer identity information. The three data sets were reviewed from 03/02/2002 to 08/31/2015. We select 01/01/2016 as the standard time and use the intck function of SAS software to calculate the number of days between the comment time and 01/01/2016. The number of days in this interval is the "age" of the Review. The longer the "age" is, the more valuable the comment is. The interval between days is represented by day (D). Step 2. Calculation of Customer satisfaction

<!-- b000350 | prose | pages [14] -->
According to analysis, we can introduce the factors that affect customer satisfaction (CS): helpful_votes (hv), total_votes (tv), SentimentQDAP (sq), star_rating (sr), number (n), vine (v), verified_purchase (Vp) and day (D). So the basic expression of Customer satisfaction (CS) is:

<!-- b000351 | prose | pages [14] -->
𝐶𝑆= 𝛼∗𝐷+ 𝛼1 ∗𝐹1 + 𝛼2 ∗𝐹2 + 𝛼3 ∗𝐹3 Substituting the above formulas (1), (2), (3) into 𝐶𝑆= 0.3 ∗𝐷+ 0.3 ∗(0.996 ∗ hv + 0.995 ∗ tv) + 0.1 ∗(0.801 ∗ sq + 0.743 ∗ sr + 0.503

<!-- b000352 | prose | pages [14] -->
∗ n) + 0.3 ∗(0.786 ∗v + 0.726 ∗vp) 𝐶𝑆= 0.3 ∗𝐷+ 0.2988 ∗ hv + 0.2985 ∗ tv + 0.0801 ∗ sq + 0.0743 ∗ sr + 0.0503 ∗n

<!-- b000353 | prose | pages [14] -->
+ 0.2358 ∗v + 0.2178 ∗vp

<!-- b000354 | prose | pages [14] -->
关注数学模型

<!-- b000355 | furniture | pages [14] -->
2

<!-- b000356 | furniture | pages [14] -->
MATHmodels

<!-- b000357 | furniture | pages [14] -->
获取更多资讯

<!-- b000358 | furniture | pages [15] -->
Team # 2009116

<!-- b000359 | furniture | pages [15] -->
Page 15 of 24

<!-- b000360 | prose | pages [15] -->
We use 0-1MinMax normalization, and the Customer satisfaction score is scaled to the [0,1] interval. The normalized Customer satisfaction is represented by CS *. Step 3. Analysis of Comprehensive Satisfaction

<!-- b000361 | prose | pages [15] -->
After obtaining the satisfaction of each customer, the overall satisfaction of the product buyer can be obtained based on the product classification. Comprehensive Satisfaction (COM_S) is equal to the average value of buyer satisfaction for the same product,

<!-- b000362 | prose | pages [15] -->
𝑛 𝑛

<!-- b000363 | furniture | pages [15] -->


<!-- b000364 | prose | pages [15] -->
COM_S = ∑𝐶𝑆∗𝑖/𝑛

<!-- b000365 | prose | pages [15] -->
1 1

<!-- b000366 | prose | pages [15] -->
According to the analysis of the comprehensive product score, the highest product score of Pacifier is 0.713, and the lowest score is 0. Microwave oven's overall product score is highest at 0.533 and lowest at 0.01. The overall score of the hair dryer is 0.557, and the lowest is 0.013. Words show that for the three products of pacifier, Microwave and hair dryer, the company's best product is pacifier. Step 4. Analysis of the successful products

<!-- b000367 | prose | pages [15] -->
Analyze the top ten products of Comprehensive Satisfaction of the three products respectively. We found that parafierde has a long history of successful product reviews. The number of review characters is around 150 words. Positive reviews account for a large proportion of valid votes. Star ratings are concentrated at 3-5. Customers are hardly members of verified_purchase or Amazon Vine. . Microwave has a long history of successful product reviews. The number of review characters is around 100 words. The proportion of negative reviews has increased, the number of valid votes has decreased, and the star rating has no centralized trend. Most buyers are verified_purchase, and there are almost no Amazon Vine members. Hair dryer has a long history, the number of comment characters is about 50 words, the proportion of positive comments is large, the number of valid votes is very small, the star rating is concentrated on 3-5, half of the buyers are verified_purchase, almost no.

<!-- b000368 | prose | pages [15] -->
This shows that there are more positive emotional reviews of successful products in pacifier and hair dryer, and the star rating given by customers is also high. Microwave has both positive and negative sentiment reviews, and star ratings are scattered. This is in line with the conclusions we initially obtained when analyzing stars and valid votes.

<!-- b000369 | prose | pages [15] -->
products, For Microwave's successful there are more buyers with verified_purchase identity, followed by hair dryer, and finally pacifier. The reviews of Microwave's successful products are the most reliable, followed by the hair dryer, and the reviews of Pacifier's successful products are less reliable. And whether a reviewer is an Amazon Vine member has nothing to do with the success of the product.

<!-- b000370 | prose | pages [15] -->
It can also be seen that the reviews of verified_purchase or Amazon Vine members are not significantly related to the number of valid votes. Explain that customers judge whether reviews are useful and will not be affected by the identity of the reviewer.

<!-- b000371 | prose | pages [15] -->
In addition, all products with a higher rating account for a larger proportion of positive emotional reviews. However, products with lower ratings among all products have a larger positive emotional review than before. We cannot directly judge the relationship between review sentiment and comprehensive score.

<!-- b000372 | caption | pages [15] -->
Table 5  Pacifier Top 10 Products with highest COM_S

<!-- b000373 | prose | pages [15] -->
COM_S PRODUCT_TITLE PRODUCT_PARENT cosco alpha omega elite convertible car seat 0.713 485572042 Sealy Baby Soft Ultra MattressSealy 0.703 0.696 Fisher45;Price Aquarium Monitor 409107492 61825188 Velour Boppy Nursing Pillow - green 0.693 108369347 fisher-price infant-to-toddler rocker in blue/red 0.691 0.691 the ultimate baby wrap in navy 32051425 234474039 ameda purely yours breast pump with carry-all 0.691 985518895 baby jogger performance series double 20/navy 0.690 242140507 Vintage Teaberry 4 Piece Crib Set Vintage Teaberry 0.689 460235866

<!-- b000374 | prose | pages [15] -->
关注数学模型

<!-- b000375 | furniture | pages [15] -->
2

<!-- b000376 | furniture | pages [15] -->
MATHmodels

<!-- b000377 | furniture | pages [15] -->
获取更多资讯

<!-- b000378 | furniture | pages [16] -->
Team # 2009116

<!-- b000379 | furniture | pages [16] -->
Page 16 of 24

<!-- b000380 | prose | pages [16] -->
Among pacifier products, brands such as cosco alpha, Fisher, ameda, Sealy has the better performance. In the same way, we can get the following conclusions.Among microwave oven products, brands such as sharp, lg, magic chef, whirlpool, profile, and Panda Small are doing well. Among the hair dryer products, Salon, Waterpik, Micro Tweeze, DuWop, ISLAND HAWAII, Oral-B and other brands do a better job. Among Pacifier products, brands such as chicco keyfit, ikea kladd, and batman  perform bad. Among microwave oven products, brands such as Samsung, Danby, and jx7227sfss are not doing well. Among the hair dryer products, brands such as andis, conair, xtava, mhd, remington do a worse job.

<!-- b000381 | heading | pages [16] -->
4. Task 3

<!-- b000382 | heading | pages [16] -->
4.1 Problem Analysis

<!-- b000383 | prose | pages [16] -->
In order to explore the changes in customer reviews over time, and to give the trend of product reputation in the market. When solving task2, first of all, the original time series data with breakpoints in units of days is used to calculate the cumulative dynamic mean to obtain continuous time series data in units of months, and the data is modeled in conjunction with the time series ARMA model Fit and predict future trends. Next, calculate the change in the number of reviews and the change in review sentiment before and after each rating in each specific product, and use non-parametric tests to determine the impact of star rating on reviews. Finally, find out all reviews with extreme emotions, use non-parametric tests to determine whether they have an impact on star ratings, and combine KMEANS clustering to give the characteristics of customer reviews and discuss potential false reviews.

<!-- b000384 | heading | pages [16] -->
4.2 Problem Solving

<!-- b000385 | heading | pages [16] -->
4.2.1 Time series visualization and prediction of three variables

<!-- b000386 | prose | pages [16] -->
Drawing a line graph can intuitively show the evolution of emotional scores, and you can see the trend of emotional scores of product reviews in the time dimension. The data in the following time series models are processed by month, because the original data is from day to day, but there are cases where there are no comments for many consecutive days, so we analyze all data after integrating them monthly, and then In order to ensure the validity of the data, we filter out the first few months with a small number of valid comments that affect the quality of the modeling. We find that the probability of extreme emotion reviews is low, but with the increase of time and the increase in sales of goods, the number of extreme emotions will increase accordingly. The figure below shows the sentiment trends of the three product reviews, Pacifier, hair dryer, and microwave. It can be seen that the emotional score in product reviews increases with time and the volatility increases. Generally speaking, positive (positive) emotions are higher than negative (negative) emotions in comments. The product model

<!-- b000387 | prose | pages [16] -->
Pacifier

<!-- b000388 | prose | pages [16] -->
Pacifier_246038397

<!-- b000389 | prose | pages [16] -->
Hair dryer Microwave

<!-- b000390 | prose | pages [16] -->
Hair dryer_732252283 Microwave_423421857

<!-- b000391 | prose | pages [16] -->
关注数学模型

<!-- b000392 | furniture | pages [16] -->
2

<!-- b000393 | furniture | pages [16] -->
MATHmodels

<!-- b000394 | furniture | pages [16] -->
获取更多资讯

<!-- b000395 | furniture | pages [17] -->
Team # 2009116

<!-- b000396 | furniture | pages [17] -->
Page 17 of 24

<!-- b000397 | prose | pages [17] -->
with the most number of reviews is extracted from the three products, and their product_parent codes are 246038397 (philips avent bpa free soothie pacifier, 0-3 months, 2 pack, packaging may vary), and 732252283 (remington ac2015 t | studio salon collection pearl ceramic hair dryer, deep purple), 423421857 (danby 0.7 cu.ft. countertop microwave), the emotional scores of the three products are all positive, but the emotional scores of Pacifier and Hair dryer show a downward trend, and Microwave products are in the rising stage later.

<!-- b000398 | caption | pages [17] -->
Figure 3  Emotional chart of three products

<!-- b000399 | prose | pages [17] -->
The figure shows a line chart of the three product ratings of Pacifier, Hair dryer and Microwave Oven over time. Observation from the vertical line (April 2005) shows that the stars have an upward trend, and the final stars are divided into 4.26. The number of likes rises faster, showing an exponential upward trend; H products The previous period fluctuated greatly. From 2005 to 2006, the star rating experienced a sharp decline, and then slowly rebounded. The final rating in August 2015 was 4.08. As a durable product, the number of likes is much higher than the number of reviews, that is, "watch and see" is more To the purchaser. After experiencing a sharp decline in the second half of 2004, the star rating of M products gradually rebounded. After reaching a peak in early 2008, it gradually decreased. After falling to a trough in mid-2012, it gradually rebounded. The final score in March 2015 was 3.39 points. It will continue to rise slowly. It is worth noting that M as a durable product sales and reviews are much lower than the two categories of products, but its number of likes is much higher than the number of reviews, the cumulative number of likes is 8996, the cumulative number of reviews is 1536 , The difference is almost 5 times, and in some time periods, the number of likes rose in a stepwise manner. At the end of 2014, with the sudden increase of vine comments, the number of likes rose sharply.

<!-- b000400 | prose | pages [17] -->
5 4 3 2 1 0

<!-- b000401 | prose | pages [17] -->
200410 200304 200310 200404 200504 200510 200604 200610 200704 200710 200804 200810 200904

<!-- b000402 | prose | pages [17] -->
20000

<!-- b000403 | prose | pages [17] -->
201508, 4.26 17243

<!-- b000404 | prose | pages [17] -->
15000

<!-- b000405 | prose | pages [17] -->
15244

<!-- b000406 | prose | pages [17] -->
10000

<!-- b000407 | prose | pages [17] -->
5000

<!-- b000408 | prose | pages [17] -->
0

<!-- b000409 | prose | pages [17] -->
200910 200910 201004 201010 201104 201110 201204 201210 201304 201310 201404 201410 201504

<!-- b000410 | prose | pages [17] -->
sum_star_rating pacifier_star_rating sum_helpful_votes

<!-- b000411 | furniture | pages [17] -->


<!-- b000412 | caption | pages [17] -->
Figure 4  Pacifier Trend graph of cumulative number of star ratings, reviews and helpfulness ratings

<!-- b000413 | prose | pages [17] -->
5.00 4.00 3.00 2.00 1.00 0.00

<!-- b000414 | prose | pages [17] -->
200203 200209 200303 200309 200403 200409 200503 200509 200603 200609 200703 200709 200803 200809

<!-- b000415 | prose | pages [17] -->
30000

<!-- b000416 | prose | pages [17] -->
201508, 4.08 24938

<!-- b000417 | prose | pages [17] -->
25000 20000 15000

<!-- b000418 | prose | pages [17] -->
10732

<!-- b000419 | prose | pages [17] -->
10000 5000 0

<!-- b000420 | prose | pages [17] -->
200903 200909 201003 201009 201103 201109 201203 201209 201303 201309 201403 201409 201503

<!-- b000421 | prose | pages [17] -->
sum_helpful_votes hairdryer_star_rating sum_star_rating

<!-- b000422 | furniture | pages [17] -->


<!-- b000423 | caption | pages [17] -->
Figure 5  Hair dryer Trend graph of cumulative number of star ratings, reviews and helpfulness

<!-- b000424 | prose | pages [17] -->
ratings

<!-- b000425 | prose | pages [17] -->
关注数学模型

<!-- b000426 | furniture | pages [17] -->
2

<!-- b000427 | furniture | pages [17] -->
MATHmodels

<!-- b000428 | furniture | pages [17] -->
获取更多资讯

<!-- b000429 | furniture | pages [18] -->
Team # 2009116

<!-- b000430 | prose | pages [18] -->
5.00 4.00 3.00 2.00 1.00 0.00

<!-- b000431 | prose | pages [18] -->
200406 200411 200504 200509 200602 200607 200612 200705 200710 200803 200808 200901 200906 200911

<!-- b000432 | furniture | pages [18] -->
Page 18 of 24

<!-- b000433 | prose | pages [18] -->
10000

<!-- b000434 | prose | pages [18] -->
8996

<!-- b000435 | prose | pages [18] -->
8000 6000

<!-- b000436 | prose | pages [18] -->
201508, 3.39

<!-- b000437 | prose | pages [18] -->
4000

<!-- b000438 | prose | pages [18] -->
1536

<!-- b000439 | prose | pages [18] -->
2000 0

<!-- b000440 | prose | pages [18] -->
201004 201009 201102 201107 201112 201205 201210 201303 201308 201401 201406 201411 201504

<!-- b000441 | prose | pages [18] -->
sum_helpful_votes microwave_star_rating sum_star_rating

<!-- b000442 | furniture | pages [18] -->


<!-- b000443 | caption | pages [18] -->
Figure 6 Microwave Trend graph of cumulative number of star ratings, reviews and helpfulness ratings

<!-- b000444 | heading | pages [18] -->
4.2.2 Prediction of star ratings

<!-- b000445 | prose | pages [18] -->
We then use a time series model to predict star ratings. First, we use the time series visualization described above to obtain the main trends of the three products. Then we check the stability of the time series and draw the ACF / PACF chart to find the optimal parameters. Then, a differential autocorrelation moving average model (ARIMA) model is established, and the star ratings in September and October 2015 can be predicted as follows:

<!-- b000446 | furniture | pages [18] -->


<!-- b000447 | caption | pages [18] -->
Figure 7  Star ratings Forecasting Graph

<!-- b000448 | prose | pages [18] -->
Microwave oven star ratings prediction for September: 3.401379; October: 3.395562.Hair dryer star ratings prediction for September: 4.080642; October: 4.081117.Pacifier star ratings prediction for September: 4.268717; October: 4.268825.

<!-- b000449 | heading | pages [18] -->
4.2.3 Prediction of reviews sentiment

<!-- b000450 | prose | pages [18] -->
We can use the same method to predict the sentiment trends of the three products in the next three months. The results are shown in the table below. Similar to the results obtained from the emotional trend chart, the sentiment scores of future reviews of P and H products will decline. The negative and positive emotions of P products will first increase and then decrease, while the negative emotions of H products will not change much , The decline in positive emotions is more serious, reflecting the possible problem of customer enthusiasm; M as a durable product, sales and reviews are very few compared to the other two products, relatively more data more consistent with the normal distribution, and relatively Less data is more volatile. Therefore, the emotional trend of future reviews of M products is rising, falling, and rising fluctuation trends, but generally it is rising.

<!-- b000451 | caption | pages [18] -->
table 6  Emotional charts of three product reviews in the next three months

<!-- b000452 | heading | pages [18] -->
4.2.4 Time series analysis

<!-- b000453 | furniture | pages [18] -->


<!-- b000454 | prose | pages [18] -->
First, select star ratings, next_past, next_past_sen, and use multiple independent sample nonparametric tests. The test method is J-T test (Jonckheere-Terpstra):

<!-- b000455 | prose | pages [18] -->
关注数学模型

<!-- b000456 | furniture | pages [18] -->
2

<!-- b000457 | furniture | pages [18] -->
MATHmodels

<!-- b000458 | furniture | pages [18] -->
获取更多资讯

<!-- b000459 | furniture | pages [19] -->
Team # 2009116

<!-- b000460 | furniture | pages [19] -->
Page 19 of 24

<!-- b000461 | prose | pages [19] -->
It can be known by the results that p1 is approximately 0, and p2 = 0.531> 0.05. At the confidence level of 0.05, there is a significant difference in the number of reviews before and after the occurrence of different star reviews, but there is no significant difference in the sentiment between the reviews before and after.

<!-- b000462 | prose | pages [19] -->
Check whether the one-star evaluation will cause significant changes in comments and comment sentiment. Select the number of front and rear comments and comment sentiment corresponding to the one-star sample, and use Wilcoxon to perform a non-parametric test on two paired samples.

<!-- b000463 | caption | pages [19] -->
Table 7  Test Statistics

<!-- b000464 | prose | pages [19] -->
past_sen - next_sen past - next

<!-- b000465 | prose | pages [19] -->
-39.067b Z

<!-- b000466 | prose | pages [19] -->
Asymp. Sig. (2-tailed) .000

<!-- b000467 | prose | pages [19] -->
a. Wilcoxon Signed Ranks Test

<!-- b000468 | prose | pages [19] -->
b. Based on positive ranks.

<!-- b000469 | prose | pages [19] -->
-37.732b

<!-- b000470 | prose | pages [19] -->
.000

<!-- b000471 | prose | pages [19] -->
P is approximately 0, and there is a significant difference at a significance level of 0.001, that is, a one-star review will cause a significant change in the number of reviews and a significant change in review emotions.

<!-- b000472 | prose | pages [19] -->
Similarly, check whether the five-star evaluation will cause a significant change in the review:

<!-- b000473 | prose | pages [19] -->
P is close to 0, and there is a significant difference at a significance level of 0.001, that is, a five-star review will cause a significant change in the number of reviews and review sentiment.

<!-- b000474 | prose | pages [19] -->
In combination with the above, there is a difference in the number of reviews before and after different star reviews, so it cannot be judged that special star reviews will affect the number of reviews, but special star reviews, such as one-star and five-star, will cause changes in review emotions.

<!-- b000475 | caption | pages [19] -->
Table 8  Final Cluster Centers

<!-- b000476 | prose | pages [19] -->
Cluster

<!-- b000477 | prose | pages [19] -->
1

<!-- b000478 | prose | pages [19] -->
star 3.55

<!-- b000479 | prose | pages [19] -->
next_past_sen .56

<!-- b000480 | prose | pages [19] -->
2 3

<!-- b000481 | prose | pages [19] -->
3.90 4.17

<!-- b000482 | prose | pages [19] -->
-1.44 6.66 K-MEANS clustering is based on the star rating of each item and the emotional changes before and after the one-star review. It can be found that 1 group of products in the table has the lowest star rating and is least affected by the one-star review; 2 groups publish more with one-star review Negative reviews. The star rating of these products is 3.9, which is relatively high. It may be that the customer ’s star rating is too high and does not match the product, resulting in a large number of negative reviews and one-star ratings. High, 1-star reviews in such products will cause a large number of positive reviews from customers. Possible situations are: first, when a good product is discredited, customers will praise it more positively; Influence, the phenomenon of good comments appears.

<!-- b000483 | heading | pages [19] -->
4.2.5 Interaction between star_rating and review

<!-- b000484 | prose | pages [19] -->
The data is summarized according to product_parent and date, and the number of reviews and the sentiment of reviews before and after a review of a certain type of product (excluding this review) are obtained. In order to eliminate the influence of time, the longer the time between the two comments, the smaller the mutual influence, so the time weight is 1 / [(date_after-date_before) +1], where +1 is for processing Comments occurred when the denominator was zero on the same day.

<!-- b000485 | prose | pages [19] -->
The pseudo code for the variable processing of comment number next and comment emotion next_sen after the comment has occurred is:

<!-- b000486 | prose | pages [19] -->
关注数学模型

<!-- b000487 | furniture | pages [19] -->
2

<!-- b000488 | furniture | pages [19] -->
MATHmodels

<!-- b000489 | furniture | pages [19] -->
获取更多资讯

<!-- b000490 | furniture | pages [20] -->
Team # 2009116

<!-- b000491 | furniture | pages [20] -->
Page 20 of 24

<!-- b000492 | prose | pages [20] -->
Original data

<!-- b000493 | prose | pages [20] -->
data ascending

<!-- b000494 | prose | pages [20] -->
Assign k to

<!-- b000495 | prose | pages [20] -->
deleting one-review observation

<!-- b000496 | prose | pages [20] -->
k=25331

<!-- b000497 | prose | pages [20] -->
remaining data

<!-- b000498 | prose | pages [20] -->
Matrix X has k rows and 2 columns

<!-- b000499 | prose | pages [20] -->
Generate zero matrix X

<!-- b000500 | prose | pages [20] -->
i=0, i=i+1

<!-- b000501 | prose | pages [20] -->
i=k

<!-- b000502 | prose | pages [20] -->
No

<!-- b000503 | prose | pages [20] -->
j=i+1

<!-- b000504 | furniture | pages [20] -->


<!-- b000505 | furniture | pages [20] -->


<!-- b000506 | furniture | pages [20] -->


<!-- b000507 | furniture | pages [20] -->


<!-- b000508 | prose | pages [20] -->
Output X

<!-- b000509 | prose | pages [20] -->
Yes

<!-- b000510 | prose | pages [20] -->
x[i,1]=1/(date[j]-

<!-- b000511 | prose | pages [20] -->
Yes

<!-- b000512 | prose | pages [20] -->
date[i]+1)+x[i,1]

<!-- b000513 | prose | pages [20] -->
product_parent[j]=

<!-- b000514 | prose | pages [20] -->
product_parent[i]

<!-- b000515 | prose | pages [20] -->
No

<!-- b000516 | prose | pages [20] -->
Yes

<!-- b000517 | prose | pages [20] -->
j=k+1

<!-- b000518 | prose | pages [20] -->
x[i,2]=sentiment*1/( date[j]- date[i]+1)+x[i,2]

<!-- b000519 | prose | pages [20] -->
No

<!-- b000520 | furniture | pages [20] -->


<!-- b000521 | caption | pages [20] -->
Figure 8  Process of variable handling pseudo code

<!-- b000522 | prose | pages [20] -->
The original data set is sorted by date in descending order, and according to the above pseudo-code calculation process, you can get the number of reviews before the comment occurs, and the change in comment sentiment past_sen, which is not repeated, and then you can get the change in the number of reviews before and after a certain comment next_past and comment sentiment Changes next_past_sen. After testing, both do not conform to the normal distribution, so non-parametric tests are selected for subsequent tests.

<!-- b000523 | prose | pages [20] -->
We selected 17 extreme negative words including disappointed and 17 extremely positive words including enthusiastic to obtain extreme emotional values NEG and POS.

<!-- b000524 | caption | pages [20] -->
Table 9  Final Cluster Centers

<!-- b000525 | prose | pages [20] -->
Cluster 1 2 3

<!-- b000526 | prose | pages [20] -->
COM_S 0.1283 0.1321 0.1699 star_rating 4 4 4 helpful_votes 1 156 23 vine 0 0 0 verified_purchase 1 1 0 reviewzishu 51 115 291 NEG 0 0 0 POS 0 0 1 reviews 46 205 17

<!-- b000527 | prose | pages [20] -->
4 5 6 7 8

<!-- b000528 | prose | pages [20] -->
0.1334 0.0399 0.0909 0.0982 0.1235 4 5 4 4 4 331 814 0 17 1 0 1 0 0 0 1 0 1 1 1 67 233 38 254 44 0 1 0 0 0 0 0 0 1 0 518 43 722 619 379 The number of classifications is determined through the stone map, and the entire sample is divided into 8 categories in the table using Kmeans clustering. You can see that extreme negative words appear in category 5, which is characterized by low

<!-- b000529 | prose | pages [20] -->
关注数学模型

<!-- b000530 | furniture | pages [20] -->
2

<!-- b000531 | furniture | pages [20] -->
MATHmodels

<!-- b000532 | furniture | pages [20] -->
获取更多资讯

<!-- b000533 | furniture | pages [21] -->
Team # 2009116

<!-- b000534 | furniture | pages [21] -->
Page 21 of 24

<!-- b000535 | prose | pages [21] -->
product satisfaction, few reviews, but star ratings. High ratings, high number of valid points and VINE reviews, long word reviews, and false information. Such products are either good products that have been maliciously smeared or bad products that have been touted;

<!-- b000536 | prose | pages [21] -->
Positive vocabulary appears in categories 3 and 7, of which the third category has high product satisfaction, fewer reviews and likes, longer reviews, fewer vine reviews, and fewer verified_purchase certifications, and doubts the validity and credibility of reviews , Or there is a phenomenon of praise; the satisfaction of the seventh category of products is acceptable, the number of reviews is high, and the number of likes is small. With the increase of the number of reviews, the probability of occurrence of extreme words will increase accordingly, so there is no abnormal review behavior in this group.

<!-- b000537 | caption | pages [21] -->
Table 10  Table of Negative words Correlations

<!-- b000538 | prose | pages [21] -->
Pearson Correlation

<!-- b000539 | prose | pages [21] -->
star_rating

<!-- b000540 | prose | pages [21] -->
Sig. (2-tailed)

<!-- b000541 | prose | pages [21] -->
N

<!-- b000542 | prose | pages [21] -->
Pearson Correlation

<!-- b000543 | prose | pages [21] -->
NEG

<!-- b000544 | prose | pages [21] -->
Sig. (2-tailed)

<!-- b000545 | prose | pages [21] -->
N

<!-- b000546 | prose | pages [21] -->
star_rating NEG

<!-- b000547 | prose | pages [21] -->
-.209** 1

<!-- b000548 | prose | pages [21] -->
.000

<!-- b000549 | prose | pages [21] -->
29511 29511

<!-- b000550 | prose | pages [21] -->
-.209** 1

<!-- b000551 | prose | pages [21] -->
.000

<!-- b000552 | prose | pages [21] -->
29511 29511

<!-- b000553 | prose | pages [21] -->
**. Correlation is significant at the 0.01 level (2-tailed).

<!-- b000554 | caption | pages [21] -->
Table 11  Table of Positive words Correlations

<!-- b000555 | prose | pages [21] -->
Pearson Correlation

<!-- b000556 | prose | pages [21] -->
star_rating

<!-- b000557 | prose | pages [21] -->
Sig. (2-tailed)

<!-- b000558 | prose | pages [21] -->
N

<!-- b000559 | prose | pages [21] -->
Pearson Correlation

<!-- b000560 | prose | pages [21] -->
POS

<!-- b000561 | prose | pages [21] -->
Sig. (2-tailed)

<!-- b000562 | prose | pages [21] -->
N

<!-- b000563 | prose | pages [21] -->
star_rating POS

<!-- b000564 | prose | pages [21] -->
.240** 1

<!-- b000565 | prose | pages [21] -->
.000

<!-- b000566 | prose | pages [21] -->
29511 29511

<!-- b000567 | prose | pages [21] -->
.240** 1

<!-- b000568 | prose | pages [21] -->
.000

<!-- b000569 | prose | pages [21] -->
29511 29511

<!-- b000570 | prose | pages [21] -->
**. Correlation is significant at the 0.01 level (2-tailed). It can be seen that at a confidence level of 0.01, there is a correlation between extreme emotions and star ratings. There is a negative correlation between extreme negative emotions and star ratings. There is a positive correlation between extreme positive emotions and star ratings. The coefficients are all less than 0.3, and the correlation is low. Considering the frequency of extreme emotional words, non- parametric tests are performed. The results are as follows:

<!-- b000571 | caption | pages [21] -->
Table 12  Test Statistics

<!-- b000572 | prose | pages [21] -->
Mann-Whitney U Wilcoxon W Z Asymp. Sig. (2-tailed)

<!-- b000573 | prose | pages [21] -->
star_rating

<!-- b000574 | prose | pages [21] -->
5310158.500 5655854.500 -31.131 .000

<!-- b000575 | prose | pages [21] -->
a. Grouping Variable: NEG

<!-- b000576 | prose | pages [21] -->
Mann-Whitney U Wilcoxon W Z Asymp. Sig. (2-tailed)

<!-- b000577 | prose | pages [21] -->
star_rating

<!-- b000578 | prose | pages [21] -->
63602803.000 266080429.000 -43.030 .000

<!-- b000579 | prose | pages [21] -->
a. Grouping Variable: POS It can be seen that there is a significant difference between star ratings and other star ratings for comments with extreme emotional words, which can explain that there is indeed a relationship between extreme emotions and star ratings. The relationship between extreme negative emotions and star ratings is Negative correlation, positive correlation between extreme positive emotion and star rating.

<!-- b000580 | prose | pages [21] -->
关注数学模型

<!-- b000581 | furniture | pages [21] -->
2

<!-- b000582 | furniture | pages [21] -->
MATHmodels

<!-- b000583 | furniture | pages [21] -->
获取更多资讯

<!-- b000584 | furniture | pages [22] -->
Team # 2009116

<!-- b000585 | heading | pages [22] -->
5. Model Evaluation

<!-- b000586 | heading | pages [22] -->
5.1 Model Limitations

<!-- b000587 | prose | pages [22] -->
Time series analysis:

<!-- b000588 | furniture | pages [22] -->
Page 22 of 24

<!-- b000589 | prose | pages [22] -->
(1) The model has the defect of prediction error and ignores the changes of other random variables. When there are large changes in the outside world, there are often large deviations. (2) The time series prediction method is effective to predict the effect of changes in the short term. Because objective things, especially economic phenomena, are more likely to change external factors over a longer period of time, they must have a significant impact on market economic phenomena. Lexicon-based method: (1) The sentiment score of a review is the average of all its sentence scores. This method is not consistent with the actual situation. Just as the paragraphs in the article are of different importance. In a sentence, the sentence before and after the sentence also have important differences. (2) There is a type of text that uses a derogatory word to indicate positive meaning. Lexicon-based method cannot recognize this situation. For this problem, deep learning methods are needed to effectively solve it. It is difficult to solve this problem with ordinary machine learning methods. (3) For the judgment of positive and negative comments, the algorithm ignores many other negative words, degree adverbs, and emotion words; it is too simple to judge the strength of emotions. (4) The accuracy rate of Lexicon-based method is high (more than 80%), but the manual workload is relatively large. (5) Ignore the existence of emoticons and the emotions expressed in the comments. Emoticons often carry some emotional polarity, which expresses the emotions of customers more clearly. But the emoticons were ignored in the emotional score. Principal component analysis disadvantages: (1) Principal component analysis is suitable for data that has a strong correlation between variables. If the original data is weakly correlated, it will not play a good role in reducing dimensions. (2) After the dimensionality reduction, there is a small amount of information loss and it is impossible to contain 100% of the original data. (3) After the original data is standardized, the meaning will change, and the interpretation meaning of the principal components will be more vague than the original data.

<!-- b000590 | heading | pages [22] -->
5.2 Model Strengths

<!-- b000591 | prose | pages [22] -->
Time series analysis:

<!-- b000592 | prose | pages [22] -->
The time series analysis and prediction method highlights the role of time factors in forecasting, and does not consider the impact of specific external factors for the time being. Time series analysis carries out volume prediction. In fact, all the influencing factors are attributed to the time factor, and only the comprehensive effect of all influencing factors is recognized, and it will still play a role in predicting objects in the future. The input variables can be adjusted according to the time series model to keep the system development process at the target value, that is, the necessary control can be performed when the process is predicted to deviate from the target. By analyzing time series, we can make reasonable predictions and grasp the future development trends in advance to provide a basis for business decisions. Lexicon-based method:

<!-- b000593 | prose | pages [22] -->
Lexicon-based approach outperforms Supervised Machine Learning approach not only in terms of Accuracy, Precision, Recall and F-measure but also in terms of economy of time and efforts used. The ARIMA model achieves a more accurate forecast and it is a simplistic modeling technique.

<!-- b000594 | prose | pages [22] -->
关注数学模型

<!-- b000595 | furniture | pages [22] -->
2

<!-- b000596 | furniture | pages [22] -->
MATHmodels

<!-- b000597 | furniture | pages [22] -->
获取更多资讯

<!-- b000598 | furniture | pages [23] -->
Team # 2009116

<!-- b000599 | furniture | pages [23] -->
Page 23 of 24

<!-- b000600 | prose | pages [23] -->
Advantages of principal component analysis: (1) The data is not required to be normally distributed. The principal component is to rotate the base group in the direction in which the data is most discrete. (2) Through the synthesis and simplification of the original variables, the weight of each indicator can be objectively determined, and the randomness of subjective judgment can be avoided. The final result is only related to the data, and has nothing to do with model selection. (3) PCA transforms the original indicators into independent principal components. Practice has shown that PCA is a linear dimensionality reduction method with the least amount of lost original data information.

<!-- b000601 | heading | pages [23] -->
6. Conclusion

<!-- b000602 | prose | pages [23] -->
1. By analyzing star_ratings, reviews, helpfulness ratings, and SentimentQDAP, the overall characteristics of three products are initially obtained. (1) For microwave, star ratings are concentrated on 1 star and 5 stars, while hair dryer and pacifier are concentrated on 5 stars. In addition, high-rated customer reviews provided by hair dryer and pacifier can provide more effective information. It can be assumed that pacifier and hair dryer are Amazon's more successful products. (2) For microwave, the company should pay attention to the performance and price of the product, and make timely improvements to the product. For the hair dryer, the company should focus on product performance and appearance issues to find out the factors of product success. For pacifier, the evaluation is generally high, and the company should pay attention to the product life. 2. Use time series visualization to depict the trend of comment sentiment and star rating, cumulative number of comments, and cumulative number of likes in the time dimension. (1) With time flowing and the increase in sales of goods, the number of extreme attitudes will increase accordingly. (2) Positive (positive) emotions are higher than negative (negative) emotions in the three product reviews. However, the emotional scores of Pacifier and Hair dryer showed a downward trend, and Microwave products were in a rising stage in the later period. 3.The ARIMA model is used to predict the emotional score. Once the product is sold on the market, based on customer ratings and reviews, it can be inferred that the product's score will be within a certain period of time. The company's grasp of future development trends can provide a basis for business decisions. Here are the prediction results for the sentiment scores of the three commodities over the next three months: (1) Both negative and positive emotions of Pacifier show a trend of rising first and then falling. (2) The negative emotion of the Hair dryer changes little, and the decline of the positive emotion is relatively serious, reflecting the possible problem of customer enthusiasm. (3) As a durable product, Microwave has fewer sales and reviews than the other two products. The emotional trend of future reviews is a rising, falling, and rising trend, but it is generally on the rise. 4. The decision indicators for Customer Reviews were determined using the principal component analysis method. The first principal component is voting information, the second principal component is the review content, and the third principal component is the customer. Identity information.  With the influence of the “age” of the Review, the calculation formula for determining the Customer Satisfaction (CS) was obtained. Comprehensive Satisfaction (COM_S) is derived from the CS summary of the same product. 5. Using non-parametric test methods, we conclude that special star reviews (one star, five stars) can cause emotional changes in reviews. 6. Using the non-parametric test method, there is a correlation between extreme attitude reviews and ratings: there is a relationship between extreme attitudes and star ratings, there is a negative correlation between extreme negative attitudes and ratings, and extreme positive attitudes and ratings are: Positive relationship.

<!-- b000603 | furniture | pages [23] -->


<!-- b000604 | prose | pages [23] -->
关注数学模型

<!-- b000605 | furniture | pages [23] -->
2

<!-- b000606 | furniture | pages [23] -->
MATHmodels

<!-- b000607 | furniture | pages [23] -->
获取更多资讯

<!-- b000608 | furniture | pages [24] -->
Team # 2009116

<!-- b000609 | heading | pages [24] -->
7. References

<!-- b000610 | furniture | pages [24] -->
Page 24 of 24

<!-- b000611 | references | pages [24] -->
[1] Carolanne, M. (2017). Understanding the Value of Online Customer Reviews

<!-- b000612 | references | pages [24] -->
[2] Gamal, D., Alfonse, M., EI-Horbaty, E., & Salem, A. (2019). Implementation of Machine Learning

<!-- b000613 | references | pages [24] -->
Algorithms in Arabic Sentiment Analysis Using N-Gram Features. Procedia Computer Science, Volume

<!-- b000614 | references | pages [24] -->
154, 2019, Pages 332-340

<!-- b000615 | references | pages [24] -->
[3] Sailunaz, K., & Alhajj, R. (2019). Emotion and sentiment analysis from Twitter text. Journal of

<!-- b000616 | references | pages [24] -->
Computational Science, Volume 36, September 2019, 101003

<!-- b000617 | references | pages [24] -->
[4] Zhang, S., Wei, Z., Wang, Y., & Liao, T. (2018). Sentiment analysis of Chinese micro-blog text based

<!-- b000618 | references | pages [24] -->
on extended sentiment dictionary. Future Generation Computer Systems, Volume 81, April 2018, Pages

<!-- b000619 | references | pages [24] -->
395-403

<!-- b000620 | references | pages [24] -->
[5] Bernabé-Moreno, J., Tejeda-Lorente, A., Herce-Zelaya, J., Porcel, C., & Herrera-Viedma, E. (2020).

<!-- b000621 | references | pages [24] -->
A context-aware embedding supported method to extract a fuzzy sentiment polarity dictionary.

<!-- b000622 | references | pages [24] -->
Knowledge-Based Systems, Volume 190, 29 February 2020, 105236

<!-- b000623 | references | pages [24] -->
[6] Mukhtar, N., Khan, M., & Chiragh, N. (2018). Lexicon-based approach outperforms Supervised

<!-- b000624 | references | pages [24] -->
Machine Learning approach for Urdu Sentiment Analysis in multiple domains. Telematics and

<!-- b000625 | references | pages [24] -->
Informatics, Volume 35, Issue 8, December 2018, Pages 2173-2183

<!-- b000626 | references | pages [24] -->
[7] Matyjaszek, M., Fernández, P., Krzemień, A., Wodarski, K., & Valverde, G. (2019). Forecasting

<!-- b000627 | references | pages [24] -->
coking coal prices by means of ARIMA models and neural networks, considering the transgenic time

<!-- b000628 | references | pages [24] -->
series theory. Resources Policy, Volume 61, June 2019, Pages 283-292

<!-- b000629 | references | pages [24] -->
[8] Nguyen, H., AsifNaeem, M., Wichitaksorn, N., & Pears, R. (2019) A smart system for short-term

<!-- b000630 | references | pages [24] -->
price prediction using time series models. Computers & Electrical Engineering, Volume 76, June 2019,

<!-- b000631 | references | pages [24] -->
Pages 339-352

<!-- b000632 | references | pages [24] -->
关注数学模型

<!-- b000633 | furniture | pages [24] -->
2

<!-- b000634 | furniture | pages [24] -->
MATHmodels

<!-- b000635 | furniture | pages [24] -->
获取更多资讯
