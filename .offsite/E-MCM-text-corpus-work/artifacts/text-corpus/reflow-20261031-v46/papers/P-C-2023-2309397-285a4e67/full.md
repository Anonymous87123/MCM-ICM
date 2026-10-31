# P-C-2023-2309397-285a4e67

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2023

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
C

<!-- b000005 | title | pages [1] -->
2309397

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Uncover the Hidden Secrets in Wordle Results

<!-- b000008 | prose | pages [1] -->
Since Wordle has become a popular puzzle game, it has accumulated a large amount of data. In this paper, we define a series of metrics and build several models to explore the hidden information in Wordle results.

<!-- b000009 | prose | pages [1] -->
First, after preprocessing the given data and analyzing the time series diagram of the number of reported results, we found that the changes can be divided into 3 stages. To forecast the number of reported results, we developed a weighted optimization model based on ARIMA and BP neural network. The prediction interval is then given using the Bootstrap method. We packaged this process as ARIMA-BP Interval Prediction Model Based On Bootstrap. Thus, we finally predicted the interval prediction value obtained on March 1, 2023 at 95% confidence level to be about (19504.74, 20383.26).

<!-- b000010 | prose | pages [1] -->
Then, we defined 3 qualitative and 4 quantitative attributes of words and used them to build a Multiple Linear Regression Model with the percentage of hard mode’s players. We found that the proportion will decrease by an average of 0.618 when the initial letter changes from a vowel to a consonant while it will increase by an average of 0.017 for each one-unit increase in word internal distance.

<!-- b000011 | prose | pages [1] -->
After that, we made the percentage distribution prediction of the reported results based on LSTM Model. To ensure the percentage is around 100%, we first processed the component data using a spherical coordinate transformation. Then we use them as output variables, the 7 word attributes and number of results as input to train our LSTM model. The prediction of EERIE based on this are [2%, 11%, 25%, 24%, 19%, 14%, 5%]. We changed the model’s parameters and added noise to do sensitivity analysis. Meanwhile, we introduced COV to measure the uncertainty of the model prediction, and found that it is around 0.4. For error analysis, we use MSE, RMSE and R2 to measure the prediction accuracy, and their values are shown in Table 7.

<!-- b000012 | prose | pages [1] -->
We extracted 6 indicators: RDC, TE, SK, NFC, NON, and HL to measure the difficulty of words. We built a GMM Clustering Model based on these indicators and thus classifying 5 difficulty levels. We classified the word EERIE as difficulty level III.

<!-- b000013 | prose | pages [1] -->
In addition, by counting the frequency of each letter in five positions, we found S as the initial letter has the most frequency and more specific statistical results are shown in

<!-- b000014 | prose | pages [1] -->
Table 9. We also used the Association Rule Model based on Apriori algorithm to

<!-- b000015 | prose | pages [1] -->
mine the word combination pattern in Wordle. Ideally, we found that the letters A,S,E and F,T,L usually appear together in Wordle.

<!-- b000016 | prose | pages [1] -->
Finally, we evaluated and refined the model and reported the findings in a letter to the the Puzzle Editor of the New York Times.

<!-- b000017 | keywords | pages [1] -->
Keywords: ARIMA-BP, LSTM, GMM, Apriori Algorithm, Word Attributes

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | contents | pages [2] -->
1

<!-- b000020 | contents | pages [2] -->
Introduction ........................................................................................................... 3

<!-- b000021 | contents | pages [2] -->
1.1

<!-- b000022 | contents | pages [2] -->
Background .................................................................................................. 3

<!-- b000023 | contents | pages [2] -->
1.2

<!-- b000024 | contents | pages [2] -->
Problem Restatement .................................................................................... 3

<!-- b000025 | contents | pages [2] -->
1.3

<!-- b000026 | contents | pages [2] -->
Our Work ...................................................................................................... 4

<!-- b000027 | contents | pages [2] -->
2

<!-- b000028 | contents | pages [2] -->
Assumptions and Notations .................................................................................. 4

<!-- b000029 | contents | pages [2] -->
3

<!-- b000030 | contents | pages [2] -->
ARIMA-BP Interval Prediction Model Based On Bootstrap ........................... 5

<!-- b000031 | contents | pages [2] -->
3.1   Data Preprocessing....................................................................................... 5

<!-- b000032 | contents | pages [2] -->
3.2   Point Prediction Based on a Combined ARIMA-BP Model ........................ 5

<!-- b000033 | contents | pages [2] -->
3.3   Interval Prediction Based on Bootstrap Method .......................................... 9

<!-- b000034 | contents | pages [2] -->
4 Exploring the Impact of Word Attributes on Hard Mode Based on Multiple

<!-- b000035 | contents | pages [2] -->
Linear Regression Model .................................................................................... 10

<!-- b000036 | contents | pages [2] -->
4.1

<!-- b000037 | contents | pages [2] -->
Defining Qualitative Attributes of Words ................................................... 10

<!-- b000038 | contents | pages [2] -->
4.2

<!-- b000039 | contents | pages [2] -->
Defining Quantitative Attributes of Words ................................................. 11

<!-- b000040 | contents | pages [2] -->
4.3

<!-- b000041 | contents | pages [2] -->
Building a Multiple Linear Regression Model ........................................... 11

<!-- b000042 | contents | pages [2] -->
4.4

<!-- b000043 | contents | pages [2] -->
Results Analysis ......................................................................................... 12

<!-- b000044 | contents | pages [2] -->
5

<!-- b000045 | contents | pages [2] -->
Percentage Distribution Prediction Based on LSTM Model .......................... 13

<!-- b000046 | contents | pages [2] -->
5.1

<!-- b000047 | contents | pages [2] -->
Processing of Component Data .................................................................. 13

<!-- b000048 | contents | pages [2] -->
5.2

<!-- b000049 | contents | pages [2] -->
How to Predict ............................................................................................ 14

<!-- b000050 | contents | pages [2] -->
5.3

<!-- b000051 | contents | pages [2] -->
Sensitivity Analysis .................................................................................... 15

<!-- b000052 | contents | pages [2] -->
5.4

<!-- b000053 | contents | pages [2] -->
Error Analysis ............................................................................................. 17

<!-- b000054 | contents | pages [2] -->
6

<!-- b000055 | contents | pages [2] -->
Word Difficulty Evaluation Based on GMM Model ........................................ 18

<!-- b000056 | contents | pages [2] -->
6.1

<!-- b000057 | contents | pages [2] -->
Description of Indicators to Evaluate the Difficulty of Words ................... 18

<!-- b000058 | contents | pages [2] -->
6.2

<!-- b000059 | contents | pages [2] -->
GMM Clustering Model Building .............................................................. 19

<!-- b000060 | contents | pages [2] -->
6.3

<!-- b000061 | contents | pages [2] -->
Analysis of Clustering Results ................................................................... 20

<!-- b000062 | contents | pages [2] -->
7

<!-- b000063 | contents | pages [2] -->
Other interesting features of the dataset to explore ......................................... 21

<!-- b000064 | contents | pages [2] -->
7.1

<!-- b000065 | contents | pages [2] -->
Word Frequency Statistics for 5 Letter Positions ....................................... 21

<!-- b000066 | contents | pages [2] -->
7.2   Exploration of the Combination Pattern Between Words .......................... 21

<!-- b000067 | contents | pages [2] -->
8

<!-- b000068 | contents | pages [2] -->
Model Evaluation and Improvement ................................................................ 22

<!-- b000069 | contents | pages [2] -->
8.1

<!-- b000070 | contents | pages [2] -->
Strengths and Weaknesses .......................................................................... 22

<!-- b000071 | contents | pages [2] -->
8.2

<!-- b000072 | contents | pages [2] -->
Model Improvements ................................................................................. 23

<!-- b000073 | contents | pages [2] -->
9

<!-- b000074 | contents | pages [2] -->
Conclusion ........................................................................................................... 23

<!-- b000075 | contents | pages [2] -->
10 Letter to the Puzzle Editor of the New York Times ......................................... 24

<!-- b000076 | contents | pages [2] -->
References ................................................................................................................... 25

<!-- b000077 | furniture | pages [3] -->
Team # 2309397                                                                Page 3  of  25

<!-- b000078 | heading | pages [3] -->
1 Introduction

<!-- b000079 | heading | pages [3] -->
1.1 Background

<!-- b000080 | prose | pages [3] -->
Wordle is an online word puzzle game invented by Josh Wardle during the epidemic. The New York Times newspaper which is well known for the games it publishes has bought Wordle on February 2021[1]. Wordle only allows one game to be played per day, and every player in the world plays to guess the same five-letter word in six tries or less each day[2]. Players can play in regular mode or hard mode. They can share their scores via Twitter, thus attracting more people to play and share.

<!-- b000081 | prose | pages [3] -->
Back in October 2021, less than 5,000 visits registered to its web page while by January 2022, traffic had skyrocketed to over 45 million. Some of us also love this game, Figure 1 shows one result that we got. The green tile indicates that the secret solution word has the letter in the precise location.

<!-- b000082 | prose | pages [3] -->
The yellow tile implies that the answer has the letter but not at the correct location. Grey tiles indicate the letters are not contained in the solution at all[3].

<!-- b000083 | caption | pages [3] -->
Figure 1: Wordle Game

<!-- b000084 | prose | pages [3] -->
Now we have a file of daily results from January 7, 2022 to December 31, 2022. This file includes twelve key variables that are crucial in our later research. In the file, the percentages of the number of people for the seven tries may not sum to 100% due to rounding.

<!-- b000085 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000086 | prose | pages [3] -->
By analyzing the above background, we summarize the tasks that need to be addressed as follows：

<!-- b000087 | prose | pages [3] -->
· Task 1: Develop a model to explain the daily variation in the total number of people reporting scores on Twitter and use it to give a prediction interval for the total number of people on March 1, 2023. · Task 2: Determine whether the attributes of words affect the percentage of players who choose the hard mode and explain the obtained results accordingly. · Task 3: If given a future date and the specific word, build a model to predict the percentage of 1-X tries in this day. After that, the word EERIE on March 1, 2023 should be used as a specific example of the model prediction, while analyzing the uncertainties of the model and the accuracy of the prediction. · Task 4: Develop a model to classify the difficulty of the words and identify the attributes of them under each category. Use this model to determine how difficult the word EERIE is? Finally, discuss the accuracy of the classification model. · Task 5: List and describe some other interesting features of the dataset.

<!-- b000088 | furniture | pages [4] -->
Team # 2309397                                                                Page 4  of  25

<!-- b000089 | heading | pages [4] -->
1.3 Our Work

<!-- b000090 | caption | pages [4] -->
Figure 2: Our work

<!-- b000091 | heading | pages [4] -->
2 Assumptions and Notations

<!-- b000092 | prose | pages [4] -->
Assumption 1: The number of daily online gamers in the data set is a time-dependent set of series and is independent of seasonal changes. Reason: Therefore, we can use ARIMA as well as LSTM models to predict a series of data for March 1,2023.

<!-- b000093 | prose | pages [4] -->
Assumption 2: The scores reported by players on Twitter on a daily basis are normal and reliable. Reason: To ensure that the model we build based on the dataset can reliably predict a range of data for March 1,2023.

<!-- b000094 | prose | pages [4] -->
Assumption 3: Assuming that Wordle's development process is consistent with the game's life cycle theory.

<!-- b000095 | heading | pages [4] -->
Reason: This assumption reduces the impact of external uncertainties on Wordle game

<!-- b000096 | prose | pages [4] -->
predictions, thus making the whole process of prediction and analysis more efficient.

<!-- b000097 | prose | pages [4] -->
In this work, we use the symbols in Table 1 in the model construction. Other none- frequent-used symbols will be introduced once they are used.

<!-- b000098 | caption | pages [4] -->
Table 1: Notations

<!-- b000099 | heading | pages [4] -->
Symbols

<!-- b000100 | prose | pages [4] -->
Definition

<!-- b000101 | prose | pages [4] -->
wA Weights of the ARIMA model wB Weights of the BP model PAi Predicted value of ARIMA model PBi Predicted value of BP model Li Distance between letters NF Noise factor Ci the ratio of players at different guess counts

<!-- b000102 | furniture | pages [5] -->
Team # 2309397                                                                Page 5  of  25

<!-- b000103 | heading | pages [5] -->
3 ARIMA-BP Interval Prediction Model Based On Bootstrap

<!-- b000104 | heading | pages [5] -->
3.1 Data Preprocessing

<!-- b000105 | prose | pages [5] -->
By reviewing the given data, we found that there are no missing values, but there are five outliers. One of them does not exist and two of them has less than 5 letters, we deleted these three rows of data due to the difficulty of obtaining the true values of these words. The two remaining outliers are caused by data entry errors. In order to avoid an excessive reduction in the amount of data, we changed them by combining the previous and later data as well as the semantics of them. In addition, the sum of the percentages in the original data are all in [98%, 102%], which is not much different from 100%, so they are reasonable and do not need to be processed. In summary, the preprocessing of the raw data is summarized in Table 2.

<!-- b000106 | caption | pages [5] -->
Table 2: Data Preprocessing

<!-- b000107 | prose | pages [5] -->
Outliers Variable Type Contest number Preprocessing method marxh Word 473 Delete an entire row clen Word 525 Delete an entire row tash Word 314 Delete an entire row 2569 Number of reported results 529 Change to 22569 rprobe Word 545 Change to probe

<!-- b000108 | heading | pages [5] -->
3.2 Point Prediction Based on a Combined ARIMA-BP Model

<!-- b000109 | heading | pages [5] -->
3.2.1 Variation Explaining

<!-- b000110 | prose | pages [5] -->
In the data preprocessing, although there are word entry errors, their corresponding numbers of reported results are not affected, so the complete reported data are analyzed in this problem. By observing and analyzing the characteristics of the changes in the number of reported results from Jan.7, 2022 to Dec 31, 2022, we found that they can be divided into 3 phases, as shown in Figure 3.

<!-- b000111 | prose | pages [5] -->
Based on the game lifecycle and player lifecycle theory[4], and combined with Wordle's game features, we explain the reasons for the changes as follows.

<!-- b000112 | prose | pages [5] -->
⚫ Phase 1: Rapid Growth Period (January 7, 2022 - February 2, 2022) Since the launch of Wordle's web version, it has been updated with only one puzzle a day. This artificial scarcity enhances players' desire for challenge and anticipation. The sharing function of Wordle uses emoji blocks to refer to the results of the game, which is very recognizable and easy to spread, while also avoiding spoilers, thus attracting more new players to play Wordle. In addition, the traditional popularity of crossword puzzles and the easy-to-play game mechanics have contributed to Wordle's further popularity. During this period, Wordle's overall growth in the number of results reported is 348.85%, with the number peaking at 361,908 on February 2.

<!-- b000113 | furniture | pages [6] -->
Team # 2309397                                                                Page 6  of  25

<!-- b000114 | caption | pages [6] -->
Figure 3: Changes in the number of reported results

<!-- b000115 | prose | pages [6] -->
⚫ Phase 2: Rapid Decline Period (February 3, 2022 - May 29, 2022) During this period, Wordle experiences an overall 84.29% decline in the number of reported results, which is the general nature of internet fads. When the popularity of the game reaches its peak, it faces a significant loss of players due to gamers’ declining interest and boredom with the game. The singularity of Wordle's game mechanic can contribute to this. Furthermore, the emergence of competing games in the market such as ‘Words with Friends’ and Wordle's pirated games makes Wordle lose players further.

<!-- b000116 | prose | pages [6] -->
⚫ Phase3: Stable Reduction Period (May 30, 2022 – December 31, 2022) The overall decrease in the number of results reported for Wordle in this phase is 64.14%. Rapidly losing players in Phase 2 go to play Wordle generally because of its popularity among the general public and they will quickly leave when Wordle is no longer hot or the next trend emerges. The remaining players are often loyal Wordle players or players who have developed user stickiness due to the game's social circle. At this point, the number of reports will still drop but not by much.

<!-- b000117 | heading | pages [6] -->
3.2.2 Reasons for Model Selection

<!-- b000118 | prose | pages [6] -->
Predicting the number of reported results is a problem in the field of time series analysis. The traditional ARIMA model is capable of extracting deterministic information from historical data in order to predict the trend of variables over time, however, this model requires extensive testing before application, and the process of determining the order of the model is subjective to some extent [5]. In recent years, with the development of artificial intelligence, machine learning algorithms have been widely applied to the field of data classification and prediction. Among which, BP neural network model which is efficient and convenient can effectively break the limits of traditional time series prediction models. Considering these factors, we decide to combine the advantages of traditional time series models and machine learning models. It means that first of all, we use ARIMA model and BP neural network model to predict the number of reported outcomes separately, and then we use weighted average to combine the two models to obtain a more reliable ARIMA-BP combined prediction model.

<!-- b000119 | furniture | pages [7] -->
Team # 2309397                                                                Page 7  of  25

<!-- b000120 | heading | pages [7] -->
3.2.3 ARIMA Forecasting

<!-- b000121 | prose | pages [7] -->
We first used the traditional ARIMA model for point prediction of the number of reported results, and this process is shown in Figure 4：

<!-- b000122 | caption | pages [7] -->
Figure 4: ARIMA model building process

<!-- b000123 | prose | pages [7] -->
First, we performed ADF smoothness test on the variable ‘Number of reported results’ in the preprocessed data set and found that it wasn’t smooth. Therefore, we differenced the series to the first order and tested the differenced series again. After that, we observed the ACF and PACF plot of the differenced series, and found that the ACF plot showed the characteristics of trailing tails and the PACF plot showed the characteristics of 1st order truncated tails. Therefore, the following ARIMA(1,1,0) model can be developed for the original series:

<!-- b000124 | prose | pages [7] -->
,

<!-- b000125 | prose | pages [7] -->
where xt is the tth time series value, B is the delay operator, is the coefficient of the

<!-- b000126 | prose | pages [7] -->
moving self-averaging polynomial.

<!-- b000127 | heading | pages [7] -->
3.2.4 BP Neural Network Prediction

<!-- b000128 | prose | pages [7] -->
BP neural network is a multilayer feedforward neural network trained according to the error back propagation algorithm, which can iterate and repair its own weights continuously based on the relationship between input and output variables so as to finally estimate the exact functional relationship[6]. Its algorithm is explained by the following pseudo-code.：

<!-- b000129 | heading | pages [7] -->
Algorithm 1: Prediction of the Number of Reported Results

<!-- b000130 | prose | pages [7] -->
Input：Training set D Output: test set E Learning rate η; Data normalization (normalization formula) Create network; Train the network repeat for D Forward propagation; Backward propagation until for reaches end condition Using the network; Inverse normalization of data BP neural network prediction with test set E end: The completed BP neural network trained

<!-- b000131 | furniture | pages [8] -->
Team # 2309397                                                                Page 8  of  25

<!-- b000132 | heading | pages [8] -->
3.2.5 Analysis of Results

<!-- b000133 | prose | pages [8] -->
The result obtained using the ARIMA(1,1,0) model prediction is shown in Figure 5, and using the BP neural network model prediction is shown in Figure 6:

<!-- b000134 | caption | pages [8] -->
Figure 6: BP neural network prediction effect

<!-- b000135 | caption | pages [8] -->
Figure 5: ARIMA prediction effect

<!-- b000136 | prose | pages [8] -->
It can be seen that the ARIMA model has a better effect prediction, and the point prediction PA obtained using this model for the number of results reported on March 1, 2023 is about 20598.84. BP neural network model has some bias in the early stage but has relatively good prediction effect in the later stage. The point prediction value PB obtained using this model on March 1, 2023 is about 19496.05.

<!-- b000137 | heading | pages [8] -->
3.2.6 Weighted Portfolio Model Forecast

<!-- b000138 | prose | pages [8] -->
In order to improve the accuracy and robustness of the model prediction, we derived a new combined ARIMA-BP prediction model based on ARIMA and BP neural network model by using the prediction errors to weight the two models. The design idea of this weighted combined forecasting model is shown in Figure 7:

<!-- b000139 | caption | pages [8] -->
Figure 7: Combined model design

<!-- b000140 | prose | pages [8] -->
We first calculate the average prediction error for each of the two prediction models:

<!-- b000141 | prose | pages [8] -->
.

<!-- b000142 | prose | pages [8] -->
After that, we use the share of the average prediction error squared of either model in the total average prediction error squared of the two models to reflect the weight accounted for by the other model, i.e.

<!-- b000143 | prose | pages [8] -->
.

<!-- b000144 | prose | pages [8] -->
Thus, the point prediction value of the ith series in the final ARIMA-BP combination model obtained is calculated as:

<!-- b000145 | prose | pages [8, 9] -->
. (1) Through the analysis of the prediction errors above, it is obvious that the overall prediction error of ARIMA model is relatively high, while the BP neural network model may be overfitted. Therefore, the combined ARIMA-BP prediction model can correct the errors of these two models, thus making the prediction results more realistic.

<!-- b000146 | furniture | pages [9] -->
Team # 2309397                                                                Page 9  of  25

<!-- b000148 | caption | pages [9] -->
Figure 8: Prediction errors of three models

<!-- b000149 | prose | pages [9] -->
The final point forecast for the number of results reported on March 1, 2023 using this combined ARIMA-BP model is approximately 19944.

<!-- b000150 | heading | pages [9] -->
3.3 Interval Prediction Based on Bootstrap Method

<!-- b000151 | prose | pages [9] -->
The Bootstrap method is an important method used in statistics for interval prediction, which first assumes that the data set obeys an unknown distribution, and later estimates the distribution interval of the sample by repeatedly sampling the given data set [7].We took the data predicted under the weighted combination model for the next 60 periods as the sample set, after which we sampled it 1000 times with put-back to obtain the 1000 Bootstrap sample set，YB=(Y1，Y2，……，Y1000).

<!-- b000152 | prose | pages [9] -->
For each subsample, the distribution is in line with that of the sample, so we calculated the standard deviation (SD) of these 1000 subsample sets as the SD of the sample:

<!-- b000153 | prose | pages [9] -->
.

<!-- b000154 | prose | pages [9] -->
According to the central limit theorem, it is known that the set of samples obtained by conducting 1000 draws approximately obeys the normal distribution. Therefore, the upper and lower limits of the confidence interval of the sample at confidence level 1-α can be calculated with the help of z-statistic：

<!-- b000155 | prose | pages [9] -->
. (2)

<!-- b000156 | prose | pages [9] -->
Taking the confidence levels of 95%, 90% and 80% respectively, the final prediction intervals for the number of results reported on March 1, 2023 are shown in Table 3.

<!-- b000157 | furniture | pages [10] -->
Team # 2309397                                                                Page 10  of  25

<!-- b000158 | caption | pages [10] -->
Table 3: Forecast interval

<!-- b000159 | prose | pages [10] -->
Confidence level Lower limit Upper limit 95% 19504.74 20383.26 90% 19575.33 20312.67 80% 19656.69 20231.31

<!-- b000160 | prose | pages [10] -->
From a statistical point of view, the number of people reporting Wordle scores on Twitter on March 1, 2023 will be approximately in the range of (19,504.74, 20,383.26), which will be a decrease compared to the current situation.

<!-- b000161 | heading | pages [10] -->
4 Exploring the Impact of Word Attributes on Hard Mode

<!-- b000162 | prose | pages [10] -->
Based on Multiple Linear Regression Model

<!-- b000163 | prose | pages [10] -->
Exploring the effects of certain attributes of words on the proportion of players choosing Hard Mode is a multiple-input variable, single-output variable modeling problem. We decided to develop a multiple linear regression model to derive whether word attributes affect the percentage of scores reported that were played in Hard Mode and the extent of their effects. The input variables X1-X7 are defined as follows.

<!-- b000164 | heading | pages [10] -->
4.1 Defining Qualitative Attributes of Words

<!-- b000165 | prose | pages [10] -->
First we made an overview of all the words in the dataset, and drew a word cloud map for the 356 words after preprocessing in Figure 9. We found that each word is different and its frequency is 1, so its size in the word cloud map is about the same.

<!-- b000166 | caption | pages [10] -->
Figure 9: A word cloud map for the 357 words

<!-- b000167 | prose | pages [10] -->
By searching for relevant literature, we classified the word attributes into 3 qualitative attributes and 4 quantitative attributes for a total of 7 word attributes.

<!-- b000168 | prose | pages [10] -->
⚫ Part of speech (X1) Part of speech is the most basic attribute of a word, the major classes are noun, verb and adjective[8]. By analyzing the parts of speeh of these 356 words, we divided the parts of speech of words into four categories: noun, verb, adjective and others.

<!-- b000169 | prose | pages [10] -->
⚫ Uncommon extent (X2) The extent of uncommonness is also one of the qualitative attributes of words. We used the COCA corpus to find the frequency of occurrence of each word in practical applications such as spoken speech, fiction books, magazines and newspapers, and academic journals. Using 3000 as a cut-off point, we divided the words into two categories: common and uncommon.

<!-- b000170 | furniture | pages [11] -->
Team # 2309397                                                                Page 11  of  25

<!-- b000171 | prose | pages [11] -->
⚫ Whether the initial letter a vowel or a consonant letter (X3) Starting with a vowel or consonant letter is also a qualitative attribute of a word. The vowel letters are a, e, i, o, u, which may affect the rate of players who uses Hard Mode.

<!-- b000172 | heading | pages [11] -->
4.2 Defining Quantitative Attributes of Words

<!-- b000173 | prose | pages [11] -->
⚫ Number of vowel letters (X4) The number of vowel letters is one of the quantitative attributes of words. By counting that number for each word, we found that it takes values in [0, 3] (the value is an integer).

<!-- b000174 | prose | pages [11] -->
⚫ Maximum number of letter repetitions (X5) A word can be composed of different letters or may contain repeated letters, and the maximum number of letter repetitions can also be used as a quantitative property of a word. By counting that number for each word, we found that it takes values in the range [1,3] (the value is an integer).

<!-- b000175 | prose | pages [11] -->
⚫ Emotional polarity value (X6) Each word tends to imply a certain emotional attitude, and we used the SenticNet emotion dictionary to get the emotional polarity values for 356 words. In that, negative values represent negative emotions and positive values imply positive emotions.

<!-- b000176 | prose | pages [11] -->
⚫ Word internal distance (X7) We define the internal distance of a word (WID) as the sum of the distances of each adjacent letter in it (see Equation 3), and the letter distance is the distance between their positions (L) in the alphabet, e.g. A and C have a letter distance of 2 and ABBEY has an internal distance of 24.

<!-- b000177 | prose | pages [11] -->
(3)

<!-- b000178 | heading | pages [11] -->
4.3 Building a Multiple Linear Regression Model

<!-- b000179 | prose | pages [11] -->
Currently we have obtained data for 7 independent variables, but since 3 qualitative data: X1-X3, are categorical variables, we need to assign values to them before substituting them into the model. We assigned values to each category as follows.

<!-- b000180 | prose | pages [11] -->
， ，

<!-- b000181 | prose | pages [11] -->
The dependent variable (Y) is the percentage of scores reported that were played in Hard Mode, which can be calculated according to equation (4).

<!-- b000182 | prose | pages [11] -->
(4)

<!-- b000183 | prose | pages [11, 12] -->
Descriptive statistics for all variables identified are shown in Figure 10 and Table 4. As seen in (a), there are more uncommon words in the dataset than common ones, and more words with initial consonant letters than vowel letters; as seen in (b), there are the most nouns in the dataset, accounting for 53%, 61% of words with only one vowel letter, and 29% of words with more than two maximum repetitions of letters.

<!-- b000184 | furniture | pages [12] -->
Team # 2309397                                                                Page 12  of  25

<!-- b000186 | prose | pages [12] -->
(a) X2 – X3 (b) X1, X4 – X5

<!-- b000187 | caption | pages [12] -->
Figure 10: Descriptive statistics of variables

<!-- b000188 | prose | pages [12] -->
As seen in Table 4, the average value of emotional polarity value among the 356 words is 0.0355, which is positive; the average value of word internal distance is 33.3726; the average percentage of people reported to play hard mode is 7.52%

<!-- b000189 | caption | pages [12] -->
Table 4: Descriptive statistics of variables

<!-- b000190 | prose | pages [12] -->
Variable Minimum Maximum Average Standard deviation X6 -1 0.999 0.0355 0.6448 X7 7 71 33.3726 11.9655 Y 1.17% 13.33% 7.52% 0.0223

<!-- b000191 | prose | pages [12] -->
Then, a multiple linear regression model can be developed as follows.

<!-- b000192 | prose | pages [12] -->
In the model, are the parameters of the model and is the error term.

<!-- b000193 | prose | pages [12] -->
Substituting the variable data, the final fitted regression model is:

<!-- b000194 | heading | pages [12] -->
4.4 Results Analysis

<!-- b000195 | prose | pages [12] -->
The results of the significance tests for the model as a whole and for the regression parameters of each independent variable are collated in Table 5.

<!-- b000196 | caption | pages [12] -->
Table 5: Model and parameter significance results

<!-- b000197 | prose | pages [12] -->
Variable t-value (F-value) P-value Variable t-value P-value Model 1.747 0.097 X4 0.662 0.509 X1 -0.053 0.958 X5 1.551 0.122 X2 1.210 0.227 X6 -0.138 0.890 X3 -1.798 0.073 X7 1.655 0.099

<!-- b000198 | prose | pages [12, 13] -->
First, the P-value of the model as a whole is 0.097, which is significant at the 10% level of significance, indicating that the model is significant. Second, among the 7 independent variables, only X3 and X7 have a P-value significant at the 10% level, which are 0.073 and 0.099 respectively, indicating that the regression coefficients of these two variables are significant. The p-values of the other variables are more than 0.1, so their regression coefficients are not significant.

<!-- b000199 | furniture | pages [13] -->
Team # 2309397                                                                Page 13  of  25

<!-- b000201 | prose | pages [13] -->
Thus, the two word attributes of whether the initial letter of a word is a vowel or a consonant letter and word internal distance have a significant effect on the proportion of players who report playing the hard mode, and other five variables of part of speech, uncommon extent, number of vowel letters, maximum number of letter repetitions, and emotional polarity value do not have a significant effect on this rate. When other variables are held constant, the proportion will decrease by an average of 0.618 when the initial letter changes from a vowel to a consonant; the proportion will increase by an average of 0.017 for each one-unit increase in word internal distance.

<!-- b000202 | heading | pages [13] -->
5 Percentage Distribution Prediction Based on LSTM Model

<!-- b000203 | heading | pages [13] -->
5.1 Processing of Component Data

<!-- b000204 | prose | pages [13] -->
Currently, we know the percentage of players reporting scores on Twitter who guessed the word or were unable to solve the puzzle in 1 to 6 attempts per day, and these percentages add up to an approximate 100%.

<!-- b000205 | caption | pages [13] -->
Figure 11: Percentage of successful attempts

<!-- b000206 | prose | pages [13] -->
It can be seen that these percentage data together form a set of component data X=(x1,x2,……,x7), and that the values of the seven components in X approximately satisfy the constraint:

<!-- b000207 | prose | pages [13] -->
. (5)

<!-- b000208 | prose | pages [13] -->
Therefore, the prediction of the percentage of future dates with respect to (1,2,…,6,X) can be considered as a prediction problem for the component data. In order to satisfy the restrictions of equation (5), instead of directly using the original data set as the output variable for prediction, we first performed a spherical coordinate transformation on the component data.

<!-- b000209 | prose | pages [13] -->
We open the root of each component xi of the component data to obtain ,

<!-- b000210 | prose | pages [13, 14] -->
which gives us the new vector group . Y can be viewed as a point on the hypersphere, so we map Y into the hypersphere, i.e.

<!-- b000211 | furniture | pages [14] -->
Team # 2309397                                                                Page 14  of  25

<!-- b000213 | prose | pages [14] -->
After the above processing, we can use as the output variable and use the

<!-- b000214 | prose | pages [14] -->
model to predict it. After the prediction results are available, the final component data x1-x7 can be obtained by inverse transformation.

<!-- b000215 | heading | pages [14] -->
5.2 How to Predict

<!-- b000216 | prose | pages [14] -->
For the percentage prediction of the number of attempts by players in the specified future date, we view it as an information mapping problem between multiple inputs and multiple outputs. In this process, we consider the output variable as the percentage component data that we transformed using ball coordinates. As for the input variables, we consider two main aspects: the number of players and the properties of the words. From the previous analysis, we have found that the number of players changes over time, which may cause the percentage of attempts by players to change accordingly. On the other hand, the attributes of words will have a direct impact on the success rate of players' guesses and thus on the distribution of percentages. Therefore, in addition to the number of players per day, we include the seven words’ attributes already defined earlier as input variables. Finally, for the selection of the prediction model, we chose the LSTM deep learning model, and we will describe the application of this model in detail below.

<!-- b000217 | prose | pages [14] -->
LSTM model is a long short-term memory network model that allows the analysis of input data using time series and predicts the future trend of these input data by using the core idea of cell state operation [9]. The working principle of this model can be represented in Figure 12, where yellow represents the arithmetic operations and blue represents the learned neural network.

<!-- b000218 | caption | pages [14] -->
Figure 12: The working principle of LSTM

<!-- b000219 | prose | pages [14, 15] -->
The LSTM model has the ability to remove or add information to each module by setting up "gates", and in general it consists of four steps：

<!-- b000220 | furniture | pages [15] -->
Team # 2309397                                                                Page 15  of  25

<!-- b000222 | prose | pages [15] -->
Step 1: Decide the discarded information in the cell: this operation first reads the current input xt and the pre-neuron information ht-1, after which the forgetting gate ft determines the discarded information：

<!-- b000223 | prose | pages [15] -->
Step 2: Determine the new information stored in the cell state: this operation uses the sigmoid layer as the input gate layer to determine the updated values and creates a new vector of candidate values via the tanh layer which are then added to the state：

<!-- b000224 | prose | pages [15] -->
Step 3: Update the cell state. This operation updates ct-1 to ct and multiplies the old state with ft, while discarding the information that needs to be discarded, after which the new candidate value is determined.

<!-- b000225 | prose | pages [15] -->
Step 4: Determine the output: This operation uses the sigmoid layer to determine the portion of the cell state that is output, followed by processing the cell state through tanh and multiplying it with the output of the sigmoid layer by.

<!-- b000226 | prose | pages [15] -->
,

<!-- b000227 | prose | pages [15] -->
After that, we use the word EERIE as an example, and the number of players who report their scores on that day is predicted to be about 19944 using the ARIMA-BP weighted model, while the set of attribute vectors for this word is (3, 2, 4, 3, 1, 1, 26). Bringing these input attributes into our LSTM model, while inverse transforming the obtained results, we can get the final percentage distribution of the number of player attempts on March 1, 2023:

<!-- b000228 | caption | pages [15] -->
Table 6: Results

<!-- b000229 | prose | pages [15] -->
1 try 2 tries 3 tries 4 tries 5 tries 6 tries X 2% 11% 25% 24% 19% 14% 5%

<!-- b000230 | prose | pages [15] -->
It can be seen that on March 1, 2023, for the word EERIE, about 13% of the players could guess the word in 2 trys, about 49% of the players could guess it in 3 to 4 guesses, while 5% of the players failed to guess the word in the required number of attempts.

<!-- b000231 | heading | pages [15] -->
5.3 Sensitivity Analysis

<!-- b000232 | prose | pages [15] -->
We explored the uncertainties of our model and predictions through sensitivity analysis, which was performed separately for the model using two methods: adjusting the model parameters and adding noise in the form of a normal distribution to the variables.

<!-- b000233 | heading | pages [15] -->
⚫ Adjusting the model parameters

<!-- b000234 | prose | pages [15, 16] -->
For parameter adjustment, we adjusted the batchsize and epoch parameters of the LSTM model five times, with specific adjustment values of [25, 250], [50, 500], [75, 750], [100, 1000], and [125,1500]. We considered the percentage of players with 7 attempt types per word as a prediction whole and used the coefficient of variation (COV) to measure the degree of dispersion between the 7 percentage values. The formula for COV is:

<!-- b000235 | furniture | pages [16] -->
Team # 2309397                                                                Page 16  of  25

<!-- b000237 | prose | pages [16] -->
Based on the prediction idea of the LSTM model above, we re-predicted the data using the model after adjusting the parameters and calculated the COVs for the predicted data. If the overall distribution of COVs is similar as the model is adjusted, the uncertainty of the model is lower, and vice versa is higher. With the variation of batchsize (bs) and epoch (ep), the scatter plot of COVs of 356 words is shown in Figure 13.

<!-- b000238 | caption | pages [16] -->
Figure 13: Sensitivity and uncertainty analysis (1)

<!-- b000239 | prose | pages [16] -->
As seen in Figure 13, the variations of the model parameters (bs, ep)have an effect on the distribution of the COVs of the predicted data. The distributions of COVs are similar under the model parameters except for bs=75, ep=750 where the distribution are more concentrated, indicating that the uncertainty of the model and prediction is low.

<!-- b000240 | prose | pages [16] -->
⚫ Adjusting noise For adding noise, we first randomly generated a normal distribution matrix M356×7, which was then multiplied by a noise coefficient NF and added to a matrix T7×356 consisting of the original data from one try to X tries to calculate the new output data set N of the model. The formula is expressed as follows. We adjusted the values of NF to 0.1, 0.15, 0.2, 0.25 and 0.3 respectively.

<!-- b000241 | prose | pages [16] -->
Similarly, we re-predicted the data using the model after adding noise and calculated the COVs for the predicted data. With the variation of NF, the scatter plot of COVs of 356 words is shown in Figure 14.

<!-- b000242 | caption | pages [16] -->
Figure 14: Sensitivity and uncertainty analysis (2)

<!-- b000243 | furniture | pages [17] -->
Team # 2309397                                                                Page 17  of  25

<!-- b000244 | prose | pages [17] -->
As seen in Figure 14, the variations of the noise factor (NF) also have an effect on the distribution of the COVs of the predicted data. The distribution of COVs is more consistent across words when NF is 0.2 and above, which also indicates that the uncertainty of the model and prediction is lower at this time. We defined the overall extreme difference of the COV (Equation 6) to indicate the degree of uncertainty.

<!-- b000245 | prose | pages [17] -->
(6)

<!-- b000246 | prose | pages [17] -->
From the variation of model parameters, the uncertainty of model and prediction is 0.4321; from the variation of noise coefficient, this uncertainty is 0.4794.

<!-- b000247 | heading | pages [17] -->
5.4 Error Analysis

<!-- b000248 | prose | pages [17] -->
We use error analysis to measure the confidence of the model prediction. The smaller the prediction error, the higher our confidence in the model we build. By reviewing the literature[10], we determined to use the mean absolute error (MAE), the root mean squared error (RMSE) and the coefficient of determination (R2) to evaluate the effectiveness of the model prediction.

<!-- b000249 | prose | pages [17] -->
⚫ Mean absolute error (MAE) MAE is the weighted average of the absolute values of the differences between the

<!-- b000250 | prose | pages [17] -->
predicted ( ) and true values ( ) of the model. Mean absolute error does not consider

<!-- b000251 | prose | pages [17] -->
the direction of the error, but only the average error magnitude of the predicted value. Therefore, this indicator can avoid the problem of mutual offset, and then can reflect the size of the actual prediction error more accurately. The range of MAE is [0, +∞), and the smaller the MAE is, the better the model fitting. The formula is as follows.

<!-- b000252 | prose | pages [17] -->
⚫ Root mean squared error (RMSE) RMSE is the average root of the expected value of the square of the difference between the true value and the predicted value. It measures the deviation between the predicted and true values and is more intuitive in terms of order of magnitude. The range of the RMSE is [0, +∞), and the smaller the RMSE value, the better the model's predictive ability. The formula is as follows.

<!-- b000253 | prose | pages [17] -->
⚫ Coefficient of determination (R2) R2 is used to measure the goodness of fit of the model predictions to the actual values. The range of it is [0,1], a value close to 1 indicates that the model fits well; if the value is close to 0, the model is poorly fitted. The formula is as follows.

<!-- b000254 | furniture | pages [18] -->
Team # 2309397                                                                Page 18  of  25

<!-- b000255 | prose | pages [18] -->
According to the formula of the above 3 indicators, we calculated the prediction error of the percentage of players making 1 try - X tries respectively, and then found the mean value of them. The calculation results are collated in Table 7.

<!-- b000256 | caption | pages [18] -->
Table 7: Error analysis

<!-- b000257 | prose | pages [18] -->
Indicators 1 try 2 tries 3 tries 4 tries 5 tries 6 tries X tries Average MAE 0.543 3.361 7.168 4.162 5.350 5.443 2.403 4.062 RMSE 0.911 4.414 8.868 5.423 6.590 6.865 4.302 5.339 R2 0.899 0.986 0.993 0.989 0.986 0.993 0.998 0.978

<!-- b000258 | prose | pages [18] -->
As seen in Table 7, the MAE of all prediction results is within 8, with an average MAE of 4.062 and an average RMSE of 5.339, both of which have small values, indicating that the prediction error of the model is small. In addition, the overall R2 of the model is 0.978, which indicates that the model fits extremely well and the model has good prediction effect. Therefore, we have confidence in our model to a large extent.

<!-- b000259 | heading | pages [18] -->
6 Word Difficulty Evaluation Based on GMM Model

<!-- b000260 | heading | pages [18] -->
6.1 Description of Indicators to Evaluate the Difficulty of Words

<!-- b000261 | prose | pages [18] -->
The difficulty of a word is influenced by its natural properties, and it can also be reflected by the number of attempts made by the player. Therefore, before classifying the difficulty of words, we first defined some indicators that can measure the difficulty of words in terms of both subjectivity (S) and objectivity (O).

<!-- b000262 | prose | pages [18] -->
⚫ Calculating the relative difficulty coefficient (S) The number of players of each attempt of type can be obtained from the number of results reported and the later percentage, and to reduce the effect of decreasing numbers in time series changes, we preprocessed the number of players (NP) using extreme difference normalization:

<!-- b000263 | prose | pages [18] -->
.

<!-- b000264 | prose | pages [18] -->
We define the score for one guess-X guesses as [1, 7], where a higher score indicates a more difficult word. The score is multiplied by the number of people to obtain the total score (TS) for each word under different guesses. Then the importance of different number of guesses to word difficulty was assigned based on AHP, and the weights Wi were obtained by the eigenvalue method as [0.0285, 0.0428, 0.0662, 0.1016, 0.1558, 0.2404, 0.3648] respectively. The consistency index C.R is 0.0176<0.1, indicating that the weights calculated based on the judgment matrix weights are valid. From this we define the relative difficulty coefficient (RDC) of words as follows.

<!-- b000265 | prose | pages [18] -->
(7)

<!-- b000266 | prose | pages [18] -->
⚫ Try expectations (S) We consider the ratio of players at different guess counts (Ci) as the probability of occurrence of that count (Pi), and define the try expectation (TE) which is also the average times each word is guessed as follows. Harder words have bigger TE.

<!-- b000267 | furniture | pages [19] -->
Team # 2309397                                                                Page 19  of  25

<!-- b000268 | prose | pages [19] -->
(8)

<!-- b000269 | prose | pages [19] -->
⚫ Skewness coefficient (S) The skewness coefficient (SK) can reflect the distribution of the data. For the number of attempts data, words are more difficult when SK is less than 0 while the data are left- skewed distributed, and vice versa. Its calculation formula is as follows.

<!-- b000270 | prose | pages [19] -->
Word frequency coefficient (O) ⚫ Based on the COCA corpus, we counted the word frequencies of more than 350 words in Wordle, and then we defined the word frequency coefficient of the word with the highest frequency as 1, the coefficient of the word with the lowest frequency as 0, and the coefficient of the word with the middle frequency as 0.5. In this way, all of the word frequencies can be mapped to the interval [0, 1]. The conversion equation for the word frequency coefficient in the lower interval is：

<!-- b000271 | prose | pages [19] -->
.

<!-- b000272 | prose | pages [19] -->
The conversion equation for the word frequency coefficient in the upper interval is：

<!-- b000273 | prose | pages [19] -->
.

<!-- b000274 | prose | pages [19] -->
⚫ Number of orthographic neighbors (O) Orthographic neighbors are defined as words which are the same length but differ by one letter (such as scare and stare)[11]. We collect this data of each word from “MCWord: An Orthographic Wordform Database”. The more orthographic neighbors a word has, the more difficult it is for the player to pinpoint the word, and the more difficult it is.

<!-- b000275 | prose | pages [19] -->
⚫ Harmony level (O) We use the harmony level to indicate the degree of harmony between the reading and writing of a word from the perspective of the cognitive ability of Wordle players. First, we use H to denote the ratio between the length of a word and the length of its phonetic symbols, i.e.

<!-- b000276 | prose | pages [19] -->
The closer the value of H is to 1, the better the harmony level of the word. Therefore, we can calculate the absolute value of the difference between H and 1. We define the harmony level of the word corresponding to the smallest absolute value as 1, and the harmony level of the word corresponding to the largest absolute value as 0. In this way, the harmony levels of all words can be also mapped to the interval [0, 1].

<!-- b000277 | heading | pages [19] -->
6.2 GMM Clustering Model Building

<!-- b000278 | furniture | pages [20] -->
Team # 2309397                                                                Page 20  of  25

<!-- b000279 | prose | pages [20] -->
After specifying the indicators used to express the difficulty level of words, we chose a GMM model to cluster these indicator values to classify the difficulty level of words. Compared with the traditional K-means clustering, GMM clustering belongs to the hybrid clustering, which uses M’ distance to measure the constraint relationship between different variables, and can be considered as a better clustering method.

<!-- b000280 | prose | pages [20] -->
The GMM algorithm assumes that the samples obey k mixed Gaussian distribution functions, and for each sample point, the probability that it belongs to the kth multivariate Gaussian distribution can be calculated as follows.

<!-- b000281 | prose | pages [20] -->
After that, the parameters of each multivariate Gaussian distribution function can be updated by the EM algorithm：

<!-- b000282 | prose | pages [20] -->
.

<!-- b000283 | prose | pages [20] -->
Based on the above process, the iterative loop is continued until the Gaussian parameters converge and the loop is stopped. After that, we can classify the samples into categories by the calculated Gaussian parameters.

<!-- b000284 | heading | pages [20] -->
6.3 Analysis of Clustering Results

<!-- b000285 | prose | pages [20] -->
The clustering results based on the GMM model are shown in Table 8. Since the evaluation criteria of relative difficulty coefficient (RDC) is more comprehensive among these six indicators, which is a weight score calculated by refining the proportional characteristics of players under different guesses. It is more decisive for the difficulty of words than other indicators. Therefore, we mainly divided the difficulty level by the size of RDC of each category, and the division results are as follows.

<!-- b000286 | caption | pages [20] -->
Table 8: Clustering Results

<!-- b000287 | prose | pages [20] -->
Difficulty Level TE SK RDC WFC NON HL I 4.1548 0.6371 0.4158 0.351 0 0.3324 II 4.1920 0.4875 0.4345 0.3684 3.7589 0.3705 III 4.1866 0.5483 0.4656 0.3571 1.3984 0.3496 IIII 4.0888 0.1631 0.5786 0.4379 11.3750 0.4167 IIIII 4.2992 0.2261 0.5941 0.3782 6.8958 0.3524

<!-- b000288 | prose | pages [20] -->
The words in difficulty level I are the easiest compared to the words in other categories, with the lowest RDC in this category; the highest skewness coefficient (SK) and a right- skewed distribution, indicating that a higher percentage of players guessed the words in this category correctly with fewer attempts; the number of orthographic neighbors (NON) is 0, indicating that players are able to locate the words easily.

<!-- b000289 | prose | pages [20, 21] -->
The ROC of words in difficulty level IIIII is 0.5941, the highest; the try expectation is also the highest, and the average number of times players guessed the words in this category is 4.2992. The specific attribute values of the remaining difficulty categories are shown in Table 8.

<!-- b000290 | furniture | pages [21] -->
Team # 2309397                                                                Page 21  of  25

<!-- b000292 | prose | pages [21] -->
Based on the definitions and formulas of the 6 indicators, the 6 attribute values of EERIE were obtained as shown in Figure 15. By calculating the Marxist distance between the 6 indicator values of the word and the corresponding indicators of the 5 difficulty levels classified, we found that the distance between the word and difficulty level III is the closest, so we believe that EERIE belongs to difficulty level III.

<!-- b000293 | caption | pages [21] -->
Figure 16: Accuracy of the model

<!-- b000294 | caption | pages [21] -->
Figure 15: six attribute values of EERIE

<!-- b000295 | prose | pages [21] -->
As is shown in Figure 16, the Silhouette Value can reflect the accuracy of GMM model clustering. The closer the Silhouette Value is to 1, the higher the accuracy of the model has. According to the results, our Silhouette Values of the five categories aggregated into are all in the range of 0.8 attachment, which shows that the clustering effect we obtained using the GMM model has a high degree of accuracy.

<!-- b000296 | heading | pages [21] -->
7 Other interesting features of the dataset to explore

<!-- b000297 | heading | pages [21] -->
7.1 Word Frequency Statistics for 5 Letter Positions

<!-- b000298 | prose | pages [21] -->
We counted the frequency of letters in 5 letter positions for each of the 356 words, and

<!-- b000299 | caption | pages [21] -->
Table 9 demonstrates the letters with the top 8 frequencies in 5 letter positions and their

<!-- b000300 | prose | pages [21] -->
frequencies. We found that 's' as the initial letter has the most frequently, 'o' is most frequent as the 2nd and 3rd letter, and 'e' is most frequent as the 4th and 5th letter.

<!-- b000301 | caption | pages [21] -->
Table 9: Letters with the top 8 frequencies in 5 letter positions

<!-- b000302 | heading | pages [21] -->
7.2 Exploration of the Combination Pattern Between Words

<!-- b000303 | prose | pages [21, 22] -->
Generally speaking, the letters that make up a word are not independent of each other, but have certain back-and-forth associations. These letters with back-and-forth associations can form a pool of resources from which players can select letters for guessing to help improve the correct rate. Therefore, from this perspective, we aim to explore the combination pattern between individual words.

<!-- b000304 | furniture | pages [22] -->
Team # 2309397                                                                Page 22  of  25

<!-- b000306 | prose | pages [22] -->
To reduce the complexity of the discussion, we assume that the order of word occurrences is not considered, while only the combination pattern of the 255 words that do not appear with repeated letters is explored. We solve this problem with the help of the Association Rule Model, while using the following three definitions to determine the strength of the association between letters.

<!-- b000307 | prose | pages [22] -->
Sup: it indicates the probability that the item set X appears in the whole data N, i.e.：

<!-- b000308 | prose | pages [22] -->
Conf: It represents the probability that one variable X changes conditional on the other variable Y also changing, i.e.

<!-- b000309 | prose | pages [22] -->
Lift: It can reflect the degree of elevation of the probability of change of one variable X on the change of another variable Y. If its absolute value is greater than 1, it means that there is indeed a correlation between these two objects.

<!-- b000310 | prose | pages [22] -->
In exploring the combination laws between words using the association rule model, we first perform letter splitting of words and convert the split words into the form of Bool values of 0 or 1. After that, we used the efficient and streamlined Apriori Algorithm for the analysis of association rules, specifying Sup of 0.5, and filter out the association laws and confidence values between letters when the Lift is greater than 1.

<!-- b000311 | caption | pages [22] -->
Table 10: Word combination pattern

<!-- b000312 | prose | pages [22] -->
Letters that Letters that may Letters that Letters that may Conf Conf appear appear together appear appear together a / k / s e 1 e / n / r i 1 l / p / t a 1 p / r / t e 1 b / e / n i 1 g / h / t i 1 c / r / t e 1 i / m / s t 1 d / p / t e 1 d / f e / t 0.6 h / i / s e 1 f / t l / o 0.5

<!-- b000313 | prose | pages [22] -->
Using the Association Rule Model we can get a lot of laws between letter combinations, but due to pages limitation we only show 12 possible cases, according to which players can spell specific words more efficiently to some extent.

<!-- b000314 | heading | pages [22] -->
8 Model Evaluation and Improvement

<!-- b000315 | heading | pages [22] -->
8.1 Strengths and Weaknesses

<!-- b000316 | furniture | pages [23] -->
Team # 2309397                                                                Page 23  of  25

<!-- b000317 | prose | pages [23] -->
· In making the prediction of the number of people on March 1 2023, we used two models, ARIMA model as well as BP Neural Network, and performed a weighted calculation based on the sum of squared residuals of both, which compensated to some extent for the shortcomings of both algorithms. · We first transformed the original data with the spherical coordinates when using the LSTM model before, so that the sum of the predicted values of the percentages about (1, 2, 3, 4, 5, 6, X) in the future dates is more close to 100%. · When considering the uncertainties of the LSTM model, we added the disturbance of appropriate noise to perturb the model, and later calculated their coefficients of variation, thus making our prediction results more credible. · When considering the characteristics of the data set, we used the Apriori algorithm, and found that the occurrence of some letters among the words given daily has some correlation by mining the features between the data. · In our exploration, we found that the total number of players in the dataset reported daily was decreasing, but the percentage of those who chose the difficult mode was increasing when we were limited by space to give a literal description of it and did not explore it in depth.

<!-- b000318 | heading | pages [23] -->
8.2 Model Improvements

<!-- b000319 | prose | pages [23] -->
· In the subsequent study, when clustering the data using the GMM mixture model, we can take into account the importance of each indicator in depth, so that we can add certain weights to each indicator. · We only used the Association Rule Algorithm to find correlations for some letter combinations, but in reality, the composition of words is much more complex than we thought (such as different positions of each letter), so we should also start to consider building a more comprehensive model to describe them.

<!-- b000320 | heading | pages [23] -->
9 Conclusion

<!-- b000321 | prose | pages [23] -->
In this article, we employed different models to analyze the information of Wordle results. In general, we have achieved the following conclusions：

<!-- b000322 | prose | pages [23] -->
· Compared to 2022, the number of players reporting results will approximately be in the range of (19,504.74, 20,383.26) at a 95% confidence level. · Whether the initial letter of a word is a vowel or a consonant letter and word internal distance will affect the proportion of players who report playing the hard mode, and the proportion will decrease by an average of 0.618 when the former change from a vowel to a consonant while increasing by an average of 0.017 for each one-unit increase in word internal distance. · On 2023/3/1, for the word EERIE, about 49% of the players could guess it in 3 to 4 guesses, and the uncertainty of this result is about 0.4 and at the same time the average prediction error is about 5.339. In addition, we found that EERIE belongs to difficulty level III, which is moderately difficult.

<!-- b000323 | furniture | pages [24] -->
Team # 2309397                                                                Page 24  of  25

<!-- b000324 | heading | pages [24] -->
10 Letter to the Puzzle Editor of the New York Times

<!-- b000325 | prose | pages [24] -->
Feburary 20th, 2023 Dear Sir / Madam,

<!-- b000326 | prose | pages [24] -->
We are writing this letter to you because we want to report to you our basic findings on Wordle game data from January 31, 2022 to December 31, 2022. We hope that these results will be useful to you.

<!-- b000327 | prose | pages [24] -->
First, we found that the changes of the number of reported results on Twitter can be roughly divided into 3 phases: Rapid Growth Period (Jan.7, 2022-Feb.2, 2022), Rapid Decline Period (Feb.3, 2022-May 29, 2022) and Stable Reduction Period (May 30, 2022-Dec.31, 2022). By building a weighted ARIMA-BP model, we predict that the number of reported results on March 1, 2023 will be 19,944, and with the help of the Bootstrap method, we obtain a 95% prediction interval of (19,504.74, 20,383.26).

<!-- b000328 | prose | pages [24] -->
Second, we defined the word attributes of solution words in Wordle and divided them into 3 qualitative attributes and 4 quantitative attributes, and by building a multiple linear regression model for these 7 attribute variables and the percentage of players in Hard Mode, we found whether the initial letter of a word is a vowel or a consonant letter and word internal distance have a significant effect on the proportion.

<!-- b000329 | prose | pages [24] -->
Then, based on these 7 defined word attributes and the number of reported results, we established their relationship with the result distribution by LSTM model and predicted the distribution for the word EERIE on March 1, 2023 as [2%, 11%, 25%, 24%, 19%, 14%, 5%], which corresponded to a number of guesses ranging from one to more than seven. This prediction method can also apply to other solution words.

<!-- b000330 | prose | pages [24] -->
Again, based on the data of the number of guesses made by players for each word and the attributes of words, we defined three subjective indicators: relative difficulty coefficient, try expectations, skewness coefficient, and three objective ones: word frequency coefficient, number of orthographic neighbors, and harmony level to jointly measure the difficulty of words. Using these 6 indicators, we classify the words in Wordle into 5 difficulty levels by GMM clustering model. Taking the word EERIE as an example, we classified it into Difficulty level III according to its data for 6 indicators.

<!-- b000331 | prose | pages [24] -->
Finally, we counted the frequency of each letter in the 5 positions of the word in the dataset and found that the solution words tend to have ‘s’ as the initial letter, the highest frequency of the 2nd and 3rd positions is the letter ‘o’, and the highest frequency of the 4th and last positions is ‘e’. In addition, we have used the algorithm of association rules to explore the inter-letter connections in Wordle puzzles, and obtained the association rule that when ‘a’, ‘k’, and ‘s’ appear at the same time, ‘e’ tends to appear as well.

<!-- b000332 | prose | pages [24] -->
Thanks for taking your time out of your busy schedule to read the letter. We hope this can help you manage and operate Wordle better.

<!-- b000333 | prose | pages [24] -->
Sincerely,

<!-- b000334 | furniture | pages [24] -->
Team#2309397

<!-- b000335 | furniture | pages [25] -->
Team # 2309397                                                                Page 25  of  25

<!-- b000336 | heading | pages [25] -->
References

<!-- b000337 | references | pages [25] -->
[1] Match, S. (2022). The New York Times buys Wordle. The New York Times.

<!-- b000338 | references | pages [25] -->
[2] Anderson, B. J., & Meyer, J. G. (2022). Finding the optimal human strategy for

<!-- b000339 | references | pages [25] -->
wordle using maximum correct letter probabilities and reinforcement learning.

<!-- b000340 | references | pages [25] -->
arXiv preprint arXiv:2202.00557.

<!-- b000341 | references | pages [25] -->
[3] Short, M. B. (2022). Winning Wordle Wisely—or How to Ruin a Fun Little

<!-- b000342 | references | pages [25] -->
Internet Game with Math. The Mathematical Intelligencer, 44(3), 227-237.

<!-- b000343 | references | pages [25] -->
[4] Kummer, L. B. M., Nievola, J. C., & Paraiso, E. C. (2017). Digital Game Usage

<!-- b000344 | references | pages [25] -->
Lifecycle: a systematic literature review. In Brazilian Symposium on Computer

<!-- b000345 | references | pages [25] -->
Games and Digital Entertainment (SBGames) (pp. 1163-1172).

<!-- b000346 | references | pages [25] -->
[5] Ariyo, A. A., Adewumi, A. O., & Ayo, C. K. (2014, March). Stock price prediction

<!-- b000347 | references | pages [25] -->
using the ARIMA model. In 2014 UKSim-AMSS 16th international conference on

<!-- b000348 | references | pages [25] -->
computer modelling and simulation (pp. 106-112). IEEE.

<!-- b000349 | references | pages [25] -->
[6] Buscema, M. (1998). Back propagation neural networks. Substance use & misuse,

<!-- b000350 | references | pages [25] -->
33(2), 233-270.

<!-- b000351 | references | pages [25] -->
[7] Masarotto G. Bootstrap prediction in tervals for auto regressions [J]. International

<!-- b000352 | references | pages [25] -->
Journal of Forecasting. 1990,6(2),229-239.

<!-- b000353 | references | pages [25] -->
[8] Kornfilt, J. (2020). Parts of speech, lexical categories, and word classes in

<!-- b000354 | references | pages [25] -->
morphology. In Oxford Research Encyclopedia of Linguistics.

<!-- b000355 | references | pages [25] -->
[9] S. Siami-Namini, N. Tavakoli and A. S. Namin, "The Performance of LSTM and

<!-- b000356 | references | pages [25] -->
BiLSTM in Forecasting Time Series," 2019 IEEE International Conference on Big

<!-- b000357 | references | pages [25] -->
Data (Big Data), Los Angeles, CA, USA, 2019, pp. 3285-3292.

<!-- b000358 | references | pages [25] -->
[10] Chicco, D., Warrens, M. J., & Jurman, G. (2021). The coefficient of

<!-- b000359 | references | pages [25] -->
determination R-squared is more informative than SMAPE, MAE, MAPE, MSE

<!-- b000360 | references | pages [25] -->
and RMSE in regression analysis evaluation. PeerJ Computer Science, 7, e623.

<!-- b000361 | references | pages [25] -->
[11] Li, I. (2022). Analyzing difficulty of Wordle using linguistic characteristics to

<!-- b000362 | references | pages [25] -->
determine average success of Twitter players.
