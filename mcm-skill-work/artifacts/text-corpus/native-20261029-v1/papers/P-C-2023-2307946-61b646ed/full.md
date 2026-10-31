# P-C-2023-2307946-61b646ed

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2023

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | title | pages [1] -->
2307946

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Words Behind Wordle: Puzzle Game Analysis

<!-- b000009 | title | pages [1] -->
Using Machine Learning and Time Series Theory

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
Wordle is a popular puzzle currently offered daily by New York Times. Players try to solve the puzzle by guessing a five-letter word in six tries or less, receiving feedback with every guess. Making full use of relative information can effectively help editors to improve operational performance.

<!-- b000012 | prose | pages [1] -->
Firstly, to explain the variation and predict the future value, a time series model based on the number of reported results is introduced. After determining the optimal groups of orders, ARIMA(0,1,1) model is used to forecast the prediction interval of the number of reported results on March 1, 2023, which is [10139.23, 30808.07](80% confidence). To find out if any attributes of the word affect the hard mode percentage, a words attributes system and a LightGBM model are introduced. The results show that there are some lag attributes that have some but less effect than lag Hard Mode percentage itself.

<!-- b000013 | prose | pages [1] -->
Secondly, to predict the associated percentages of (1, 2, 3, 4, 5, 6, X), two models are established based on GBDT and MMoE. The results show that the MMoE model signif- icantly outperforms the GBDT model, with MSE of 145. Then, we attemptd to improve the model by using data augmentation and feature engineering methods. The former leads to a large amount of noise, which fails to achieve the expected effect, and the latter slightly improves the model performance. The prediction of the final model for the word EERIE is (0.649, 7.579, 26.298, 32.614, 20.930, 9.63, 2.298).

<!-- b000014 | prose | pages [1] -->
Thirdly, K-means model is introduced to cluster the samples into 4 groups with the distribution of attempt times as the features by difficulty. In order to determine which features of the words are associated with the classifications, we used the classification as the output feature and all the attributes of the words as the input feature to establish a LightGBM model for training. The accuracy of the test set reaches 70%. The importance of the output features is sorted. Finally, the model is used to predict the category of the EERIE word, and the prediction result is Group 2.

<!-- b000015 | prose | pages [1] -->
Finally, some interesting features of the dataset are found in dataset. The characteris- tics of large frequency words, the shape of distribution of attempt number and the corre- lation of the word features are discussed.

<!-- b000016 | prose | pages [1] -->
In addition, we evaluated the advantages and disadvantages of the model and pro- posed some suggestions, and carried out a sensitivity analysis of the model to the com- mission rate, thereby proved the reliability and stability of the model.

<!-- b000017 | keywords | pages [1] -->
Keywords: Wordle ; ARIMA; LightGBM; MMoE; data augmentation; feature engineer-

<!-- b000018 | prose | pages [1] -->
ing; K-means; sensitivity analysis

<!-- b000019 | furniture | pages [2] -->
Team # 2307946

<!-- b000020 | furniture | pages [2] -->
Page 1 of 25

<!-- b000021 | heading | pages [2] -->
Contents

<!-- b000022 | contents | pages [2] -->
1

<!-- b000023 | heading | pages [2] -->
Introduction

<!-- b000024 | prose | pages [2] -->
3

<!-- b000025 | prose | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000026 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 4

<!-- b000027 | heading | pages [2] -->
General Assumptions and Model Overview

<!-- b000028 | prose | pages [2] -->
2 4

<!-- b000029 | prose | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4

<!-- b000030 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 Model Overview

<!-- b000031 | prose | pages [2] -->
3

<!-- b000032 | heading | pages [2] -->
Model Preparation

<!-- b000033 | prose | pages [2] -->
4

<!-- b000034 | prose | pages [2] -->
5

<!-- b000035 | prose | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 5

<!-- b000036 | prose | pages [2] -->
Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000037 | prose | pages [2] -->
4

<!-- b000038 | heading | pages [2] -->
Model I: Time-Series Forecasting Model

<!-- b000039 | prose | pages [2] -->
5

<!-- b000040 | prose | pages [2] -->
7

<!-- b000041 | prose | pages [2] -->
The concept of Time Series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 7

<!-- b000042 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Stationarity of time series 7

<!-- b000043 | prose | pages [2] -->
Model Building . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 8

<!-- b000044 | prose | pages [2] -->
Forecasting Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 9

<!-- b000045 | prose | pages [2] -->
Extraction and Analyse Attributes of the Word 5 9

<!-- b000046 | prose | pages [2] -->
Extraction of Word Attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 9

<!-- b000047 | prose | pages [2] -->
Word Attributes Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 10

<!-- b000048 | heading | pages [2] -->
Model II: Explaining Hard Mode Percentage Using LightGBM

<!-- b000049 | prose | pages [2] -->
6 11

<!-- b000050 | prose | pages [2] -->
Introduction of LightGBM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1

<!-- b000051 | prose | pages [2] -->
6.2 Data Description and Preprocessing

<!-- b000052 | prose | pages [2] -->
11

<!-- b000053 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | prose | pages [2] -->
12

<!-- b000055 | prose | pages [2] -->
Model Results and Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 13

<!-- b000056 | heading | pages [2] -->
Model III: Multiple Input - Multiple Output Regression Model

<!-- b000057 | prose | pages [2] -->
7 15

<!-- b000058 | prose | pages [2] -->
White Noise Verification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 15

<!-- b000059 | prose | pages [2] -->
Model Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 16

<!-- b000060 | furniture | pages [3] -->
Team # 2307946

<!-- b000061 | furniture | pages [3] -->
Page 2 of 25

<!-- b000062 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3 Model Refinement 17

<!-- b000063 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3.1 Data Augmentation 17

<!-- b000064 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.4 Feature Engineering 17

<!-- b000065 | prose | pages [3] -->
Model Results and Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.5 17

<!-- b000066 | heading | pages [3] -->
Model IV: LightGBM Classifier based on K-means Clustering Model

<!-- b000067 | prose | pages [3] -->
8 18

<!-- b000068 | prose | pages [3] -->
Concept of K-means Clustering . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 18

<!-- b000069 | prose | pages [3] -->
Clustering Model Building . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 19

<!-- b000070 | prose | pages [3] -->
Evaluation of Clustering Result . . . . . . . . . . . . . . . . . . . . . . . . . . 8.3 20

<!-- b000071 | prose | pages [3] -->
Identification of Important Attributes 8.4 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | prose | pages [3] -->
20

<!-- b000073 | prose | pages [3] -->
Classfication Result and Evaluation . . . . . . . . . . . . . . . . . . . . . . . . 8.5 20

<!-- b000074 | prose | pages [3] -->
Other Interesting Features of the Data Set 9

<!-- b000075 | heading | pages [3] -->
10 Sensitivity Analysis

<!-- b000076 | prose | pages [3] -->
21

<!-- b000077 | prose | pages [3] -->
22

<!-- b000078 | prose | pages [3] -->
10.1 Sensitivity Analysis for Question 1 . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | prose | pages [3] -->
22

<!-- b000080 | prose | pages [3] -->
10.2 Sensitivity Analysis for Question 3 . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | heading | pages [3] -->
11 Strengths and Weaknesses

<!-- b000082 | prose | pages [3] -->
23

<!-- b000083 | prose | pages [3] -->
23

<!-- b000084 | prose | pages [3] -->
11.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000085 | prose | pages [3] -->
23

<!-- b000086 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.2 Weaknesses 24

<!-- b000087 | heading | pages [3] -->
12 A Memorandum to the New York Times Puzzle Editor

<!-- b000088 | prose | pages [3] -->
24

<!-- b000089 | furniture | pages [4] -->
Team # 2307946

<!-- b000090 | furniture | pages [4] -->
Page 3 of 25

<!-- b000091 | prose | pages [4] -->
1

<!-- b000092 | heading | pages [4] -->
Introduction

<!-- b000093 | prose | pages [4] -->
1.1 Problem Background

<!-- b000094 | prose | pages [4] -->
At the beginning of 2022, a simple but novel game gained great popularity on Twitter. This is the web word game Wordle written by Josh Wardle and published by the New York Times Company.

<!-- b000095 | prose | pages [4] -->
The game was fairly unknown at the very beginning, but after Wardle creatively added a function that allows players to copy the results into a grid of colored square emojis to share, it immediately attained public attention. As of mid-January 2022, there have been more than 2 million people have played and more than 1.2 million Wordle re- sults have been posted on Twitter.

<!-- b000096 | prose | pages [4] -->
In Wordle, players have to guess a word with five English letters within six chances in one day. After each attempt, the players may get three types of feedback: green if the letter is in the correct position; yellow if the answer contains the letter while the letter is in the wrong place; gray if the answer does not have the letter at all. The gameplay is similar to games like Mastermind, but Wordle will clearly indicate which letters were guessed correctly. [1]

<!-- b000097 | prose | pages [4] -->
Apart from that,Wordle has another game mode. On the basis of the above regular rules, the "Hard Mode" requires once a player has found a correct letter in a word, those letters must be used in subsequent guesses.

<!-- b000098 | prose | pages [4] -->
In fact, there is a profound mathematical mechanism behind the seemingly simple game. We can’t help wondering what mechanism affects the efficiency of players to make correct guesses, and what laws exist behind the constantly changing number of reported results on Twitter. On what basis do players choose Hard Mode?

<!-- b000099 | prose | pages [4] -->
We expect to solve the above problems through mathematical modeling to effectively predict the future operation of the game and provide Puzzle Editor of the New York Times with business suggestions.

<!-- b000100 | caption | pages [4] -->
Figure 1: NY Times Wordle

<!-- b000101 | caption | pages [4] -->
Figure 2: Example of solution

<!-- b000102 | furniture | pages [5] -->
Team # 2307946

<!-- b000103 | furniture | pages [5] -->
Page 4 of 25

<!-- b000104 | prose | pages [5] -->
1.2 Restatement of the Problem

<!-- b000105 | prose | pages [5] -->
As we have a data set containing the date, contest number, word of the day, the num- ber of people reporting scores that day, the number of players on Hard Mode, and the distribution of the reported results. We need to build mathematical models to solve the following problems for New York Times Company:

<!-- b000106 | prose | pages [5] -->
Question 1:

<!-- b000107 | prose | pages [5] -->
1. Develop a model which explains the variation of the reported results number, then make a prediction of this number for Match 1,2023 using the developed model.

<!-- b000108 | prose | pages [5] -->
2. Find out the possible attributes of the given word which may influence the per- centage of scores reported that were played in Hard Mode, and give the inherent mechanism of the influence.

<!-- b000109 | prose | pages [5] -->
Question 2: Develop a model that forecasts the distribution of the reported results of a given word on a day to come.Then discuss the uncertainties and the accuracy of the prediction model.

<!-- b000110 | prose | pages [5] -->
Question 3: Adopt a mathematical model to classify solution words by difficulty, iden- tify the attributes of a given word that link with each classification as well as evaluate the accuracy of the classification.

<!-- b000111 | prose | pages [5] -->
Question 4: Discuss and find other features within the data set.

<!-- b000112 | prose | pages [5] -->
2

<!-- b000113 | heading | pages [5] -->
General Assumptions and Model Overview

<!-- b000114 | prose | pages [5] -->
2.1

<!-- b000115 | heading | pages [5] -->
Assumptions

<!-- b000116 | prose | pages [5] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justified.

<!-- b000117 | prose | pages [5] -->
1. The number of reported results on Twitter can effectively represent the total number of players on the day, and the percentage of scores reported that were played in Hard Mode is the same as that of all players.

<!-- b000118 | prose | pages [5] -->
2. The distribution of the reported results recorded in the dataset is completely accu- rate.

<!-- b000119 | prose | pages [5] -->
3. There are correlations and differences between the associated percentages of 1 try, 2 tries,· · · , X.

<!-- b000120 | prose | pages [5] -->
4. The word difficulty is proportional to the average number of tries to guess the result.

<!-- b000121 | prose | pages [5] -->
2.2

<!-- b000122 | heading | pages [5] -->
Model Overview

<!-- b000123 | prose | pages [5] -->
In summary, the whole modeling process can be shown as follows:

<!-- b000124 | furniture | pages [6] -->
Team # 2307946

<!-- b000125 | furniture | pages [6] -->
Page 5 of 25

<!-- b000126 | caption | pages [6] -->
Figure 3: Model Overview

<!-- b000127 | prose | pages [6] -->
3

<!-- b000128 | heading | pages [6] -->
Model Preparation

<!-- b000129 | prose | pages [6] -->
3.1

<!-- b000130 | heading | pages [6] -->
Notations

<!-- b000131 | prose | pages [6] -->
Important notations used in this paper are listed in Table 1,

<!-- b000132 | prose | pages [6] -->
Symbols Definitions yT

<!-- b000133 | prose | pages [6] -->
The number of reported results at day t t yT ′

<!-- b000134 | prose | pages [6] -->
The first-order difference sequence of yT t

<!-- b000135 | prose | pages [6] -->
t yT ′‘

<!-- b000136 | prose | pages [6] -->
The first-order difference sequence of yT

<!-- b000137 | prose | pages [6] -->
t (after May 16, 2022)

<!-- b000138 | prose | pages [6] -->
t

<!-- b000139 | prose | pages [6] -->
yH

<!-- b000140 | prose | pages [6] -->
Number of reported results in Hard Mode at day t t pctt The percentage of scores reported that were played in Hard Mode at day t distributei The percentage that guessed the word in i tries

<!-- b000141 | caption | pages [6] -->
Table 1: Notations

<!-- b000142 | prose | pages [6] -->
3.2 Data Preprocessing

<!-- b000143 | prose | pages [6] -->
The data we use includes the data files given as Problem C Data Wordle.xlsx

<!-- b000144 | prose | pages [6] -->
This file gives nearly all the information we need for solving the problem. But before using it, the data needs to be preprocessed.

<!-- b000145 | prose | pages [6] -->
Firstly, we need to exclude outliers in the data set, that is, remove the points where the percentage of scores reported that were played in Hard Mode (hereinafter referred to as Hard Mode Percentage) is too far away from the other data. When making a scatter plot with a smooth line of the Reported results number, Number in hard mode, and Hard Mode Percentage concerning time, we can easily find the existence of outliers, which are marked with red dots in the following figures.

<!-- b000146 | furniture | pages [7] -->
Team # 2307946

<!-- b000147 | furniture | pages [7] -->
Page 6 of 25

<!-- b000148 | caption | pages [7] -->
Figure 4: Scatterplots of the three Time Series in the Dataset

<!-- b000149 | prose | pages [7] -->
Using the method of rolling boundary statistics, select the Hard Mode Percentage for 30 days before and 30 days after a certain day as the sample group, then construct the rolling interval according to the following equation:

<!-- b000150 | prose | pages [7] -->
Means ± 3 × (Standard Deviation) (1)

<!-- b000151 | prose | pages [7] -->
If the Hard Mode Percentage for that day falls outside this interval, it is an outlier. Ac- cording to this method, we tested the data set and obtained 4 outlier points. After elimi- nating the outliers, we used the linear interpolation method to complete the original data to obtain a more stationary data set.

<!-- b000152 | prose | pages [7] -->
In addition, we also found that there are spelling errors in the data set. For example, some given words only contain four letters, which contradicts the game’s rule of 5 letters. We removed the sample data with misspelled words to ensure the validity of the data.

<!-- b000153 | prose | pages [7] -->
All data samples to be processed and processing results are shown in the table below.

<!-- b000154 | caption | pages [7] -->
Table 2: Data Preprocessing Checklist(Outliers and Misspelling)

<!-- b000155 | prose | pages [7] -->
Date Error location Adjustment Adjusted number Number of reported results 2022/11/30 2022/11/26 Word 2022/11/01 Number in hard mode 2022/10/05 Word 2022/09/16 Number in hard mode 2022/04/29 Word 2022/02/13 Number in hard mode interpolation 10.37% Deletion N/A interpolation 9.48% Deletion N/A interpolation 8.15% Deletion N/A interpolation 3.54%

<!-- b000156 | furniture | pages [8] -->
Team # 2307946

<!-- b000157 | furniture | pages [8] -->
Page 7 of 25

<!-- b000158 | heading | pages [8] -->
Model I: Time-Series Forecasting Model

<!-- b000159 | prose | pages [8] -->
4

<!-- b000160 | prose | pages [8] -->
4.1 The concept of Time Series

<!-- b000161 | prose | pages [8] -->
A time series is a sequence of numbers listed in time order. Most commonly, a time se- ries is a sequence taken at successive equally spaced points in time. Time series analysis includes methods for analyzing time series data to extract meaningful statistics and other characteristics of the data. Time series forecasting is the use of a model to predict future values based on previously observed values.

<!-- b000162 | prose | pages [8] -->
4.2 Stationarity of time series

<!-- b000163 | prose | pages [8] -->
If we want to make a time series forecast, we must first ensure its stationarity. A sta- tionary time series should have no trend and seasonality, that is to say, its mean and variance are constant.

<!-- b000164 | prose | pages [8] -->
However, from Figure 4, we can easily derive that the time series of the number of reported results has an obvious trend and isn’t stationary. To ensure our judgment, we then adopted the ADF (Augmented Dickey-Fuller) test. The null hypothesis of this test is that the time series is not stationary. [2] The resulting significant test statistic is -1.9608 while the p-value is 0.5934, which cannot reject the null hypothesis. This confirms our judgment.

<!-- b000165 | prose | pages [8] -->
In view of the non-stationarity of the data, we performed first-order difference pro- cessing on the data. We set the time series of the number of reported results as yT

<!-- b000166 | prose | pages [8] -->
t , and constructed its first-order difference sequence yT ′

<!-- b000167 | prose | pages [8] -->
smooth line, as shown in the figure below:

<!-- b000168 | caption | pages [8] -->
Figure 5: Time Series of yT

<!-- b000169 | prose | pages [8] -->
= yT

<!-- b000170 | prose | pages [8] -->
t −yT

<!-- b000171 | prose | pages [8] -->
t−1. Made a scatter plot with a

<!-- b000172 | prose | pages [8] -->
t

<!-- b000173 | prose | pages [8] -->
t After Difference Process

<!-- b000174 | prose | pages [8] -->
It can be seen from the figure that the time series of the number of reported results being processed has a large variance before May 16, 2022, with a small variance after that, so the data after May 16 is selected as the new time series to predict the future value,

<!-- b000175 | furniture | pages [9] -->
Team # 2307946

<!-- b000176 | prose | pages [9] -->
recorded as yT ′′

<!-- b000177 | prose | pages [9] -->
t .

<!-- b000178 | furniture | pages [9] -->
Page 8 of 25

<!-- b000179 | prose | pages [9] -->
After that, we carried out the ADF test for yT ′′

<!-- b000180 | prose | pages [9] -->
again, this time p-value is 0.01 which t rejects the null hypothesis, indicating that the time series after the first-order difference is stationary.

<!-- b000181 | prose | pages [9] -->
4.3

<!-- b000182 | heading | pages [9] -->
Model Building

<!-- b000183 | prose | pages [9] -->
After ensuring the stationarity of the time series, we can use the ARIMA (Autoregres- sive Integrated Moving Average Model) model for time series forecasting. [3] The gen- eral expression of the model has the following form, ARIMA(p,d,q):

<!-- b000184 | prose | pages [9] -->
p X

<!-- b000185 | prose | pages [9] -->
q X

<!-- b000186 | prose | pages [9] -->
αiLi)(1 −L)dyt = α0 + (1 +

<!-- b000187 | prose | pages [9] -->
(1 −

<!-- b000188 | prose | pages [9] -->
i=1

<!-- b000189 | prose | pages [9] -->
βiLi)ϵt (2)

<!-- b000190 | prose | pages [9] -->
i=1

<!-- b000191 | prose | pages [9] -->
Its essence is to combine difference(d), autoregressive model(AR(p)), and moving av- erage model(MA(q)). p is the order of the autoregressive model, d is the order of dif- ference, and q is the order of the moving average model. By drawing the autocorre- lation (ACF) diagram and partial autocorrelation (PACF) diagram of the time series yT ′′

<!-- b000192 | prose | pages [9] -->
t , it is found that ACF is first-order truncated and PACF is tailed, so we can choose ARIMA(0,1,1)as the target model.

<!-- b000193 | caption | pages [9] -->
Figure 6: Autocorrelation and Partial Autocorrelation

<!-- b000194 | prose | pages [9] -->
At the same time, the best ARIMA parameters can also be obtained by using the auto.arima command in R language, resulting ARIMA(1,1,1) and ARIMA(3,1,1).

<!-- b000195 | prose | pages [9] -->
In order to determine the best of all obtained ARIMA parameters, we use the infor- mation criterion (Akaike Information Criterion) to aid judgment. The AIC values of the three optional models are 4200.897/4202.825/4205.466, and ARIMA(0,1,1) has the small- est AIC value, so it is selected as the final model.

<!-- b000196 | prose | pages [9] -->
To determine the validity of the ARIMA(0,1,1) model, we further made a white noise residual test. Test result shows that the p-values of the LB statistics are all above the threshold of 0.05, so the model passed the test and we can use ARIMA(0,1,1) to explain the variation of the number of reported results.

<!-- b000197 | furniture | pages [10] -->
Team # 2307946

<!-- b000198 | furniture | pages [10] -->
Page 9 of 25

<!-- b000199 | prose | pages [10] -->
4.4

<!-- b000200 | heading | pages [10] -->
Forecasting Results

<!-- b000201 | prose | pages [10] -->
Using the ARIMA(0,1,1) model and substituting the date, the forecast results are shown as the following graph:

<!-- b000202 | caption | pages [10] -->
Figure 7: Forecasting Results

<!-- b000203 | prose | pages [10] -->
For March 31, 2023, the prediction interval of the number of reported results with a confidence level of 80% is [10139.23, 30808.07], the prediction interval with a confidence level of 95% is [4668.516, 36278.78], and the predicted expected value is 20473.65.

<!-- b000204 | prose | pages [10] -->
5 Extraction and Analyse Attributes of the Word

<!-- b000205 | prose | pages [10] -->
5.1 Extraction of Word Attributes

<!-- b000206 | prose | pages [10] -->
The difficulty of word-quiz games like Wordle is closely related to the attributes of the given word. In view of the characteristics of the Wordle game rules, the difficulty of it mainly depends on the memorability of the given word and the difficulty for the player to recall this word. Many educators and linguists have studied the factors that affect students’ vocabulary memorization. For example, Laufer, B. (1990) [4] listed many word attributes that influence vocabulary learning performance. For Wordle, in order to get the answer, in addition to learning and memorizing words, it is also essential to infer the result based on known information, which difficulty is affected by many attributes of the word as well.

<!-- b000207 | prose | pages [10] -->
When selecting the attributes of the word, referring to existing research such as Jakub Jagoda & Tomasz Boi´nski (2018) [5], we can get some common word attributes that af- fect quiz difficulty, such as word frequency, part of speech, number of vowels, number of repeated letters and the word’s emotional tendency. In addition, the research of psy- cholinguists also provides us with many innovative indicators, such as the number of orthographic neighbors that a word has, the number of syllables in the main pronuncia- tion, and so on.

<!-- b000208 | furniture | pages [11] -->
Team # 2307946

<!-- b000209 | furniture | pages [11] -->
Page 10 of 25

<!-- b000210 | prose | pages [11] -->
5.2 Word Attributes Overview

<!-- b000211 | prose | pages [11] -->
Our attributes data mainly originate from The English Lexicon Project [6], a linguistics project jointly participated by several universities, which aims to provide standardized behavioral and descriptive datasets for 40,481 words and 40,481 non-words. The data can be obtained by visiting elexicon.wustl.edu. In addition, some Python packages and algorithms can also provide us with data about word attributes.

<!-- b000212 | prose | pages [11] -->
Other research results we have used include the SUBTLEX language library, Bysbaert et al. (2014) research on Concreteness Rating [7], Hoffman et al. (2013) research on Se- mantic Diversity [8] and DeDeyne, et al. (2018) on Association Frequency Research [9].

<!-- b000213 | prose | pages [11] -->
It is worth noting that word attributes in different time periods may have different effects on game difficulty. For example, actually, players do not know what exactly is today’s given word before they start playing, so we can naturally guess that the word attributes of today’s word have limited influence on the difficulty of today’s game. But at the same time, the word attributes of the past may significantly affect the difficulty of the game that players assume. If the word of the past few days is difficult to infer, then the players of the day may be less inclined to choose Hard Mode, and even lose the game because of a lack of confidence. Research on the hysteresis effect of past word attributes will become one of the focuses of the modeling below.

<!-- b000214 | prose | pages [11] -->
The following table lists all the word features extracted in our research, their mean- ings, and data sources:

<!-- b000215 | furniture | pages [12] -->
Team # 2307946

<!-- b000216 | furniture | pages [12] -->
Page 11 of 25

<!-- b000217 | caption | pages [12] -->
Table 3: Word Attributes Overview

<!-- b000218 | prose | pages [12] -->
Meaning of the Attribute Attribute Notation Data Sources How often the word is used in everyday life Database from Kaggle word_freq Number of vowels in the word num_vowel Counted using python Number of repeated letters num_repeat Counted using python Such as nouns, pronouns, etc. part of speech Python package NLTK Sentimental attributes of words1 sentiment Package vaderSentiment

<!-- b000219 | prose | pages [12] -->
The number of orthographic neighbors Ortho_N that a word has English Lexicon Project

<!-- b000220 | prose | pages [12] -->
The number of phonological neighbors Phono_N that a word has

<!-- b000221 | prose | pages [12] -->
2 English Lexicon Project

<!-- b000222 | prose | pages [12] -->
The number of phonographic neighbors OG_N that a word has

<!-- b000223 | prose | pages [12] -->
3 English Lexicon Project

<!-- b000224 | prose | pages [12] -->
The sum of the bigram count for a BG_Sum particular word English Lexicon Project

<!-- b000225 | prose | pages [12] -->
The number of phonemes in the main NPhon pronunciation

<!-- b000226 | prose | pages [12] -->
4 English Lexicon Project

<!-- b000227 | prose | pages [12] -->
The SUBTLEX contextual diversity5 SUBTLCD SUBTLEX

<!-- b000228 | prose | pages [12] -->
The mean of the closest 20 LD neighbors OLD for the orthograph English Lexicon Project

<!-- b000229 | prose | pages [12] -->
The mean of the closest 20 LD neighbors PLD for the phonology English Lexicon Project

<!-- b000230 | prose | pages [12] -->
Concreteness_Rating The mean of the Concreteness Ratings Bysbaert et al. (2013) The Semantic Diversity Semantic_Diversity Hoffman et al.(2013)

<!-- b000231 | prose | pages [12] -->
Number of Times Word is one of Assoc_Freq_R123 first three associates DeDeyne, et al.(2018)

<!-- b000232 | prose | pages [12] -->
The number of Morphemes NMorph

<!-- b000233 | prose | pages [12] -->
1 Such as positive, negative, etc. 2 This statistic excludes homophones 3 This statistic excludes homophones

<!-- b000234 | prose | pages [12] -->
English Lexicon Project

<!-- b000235 | prose | pages [12] -->
4 The diphthongs /aI/, /aU/, /OI/, and the affricates /tS/ and /dZ/, each count as single phonemes 5 % of films containing the word

<!-- b000236 | heading | pages [12] -->
Model II: Explaining Hard Mode Percentage Using Light-

<!-- b000237 | prose | pages [12] -->
6 GBM

<!-- b000238 | prose | pages [12] -->
6.1

<!-- b000239 | heading | pages [12] -->
Introduction of LightGBM

<!-- b000240 | heading | pages [12] -->
LightGBM is a novel GBDT (Gradient Boosted Decision Tree) algorithm proposed

<!-- b000241 | prose | pages [12] -->
by Ke in 2017 (Ke et al., 2017) [10]. GBDT has the functional characteristics of Gradient Boosting and Decision Tree, and has the advantages of good training effect and not easy to overfit. Its advantages include fast training speed, high accuracy, low memory usage,

<!-- b000242 | furniture | pages [13] -->
Team # 2307946

<!-- b000243 | furniture | pages [13] -->
Page 12 of 25

<!-- b000244 | prose | pages [13] -->
and support for parallel computing. It can be used to solve the problems encountered by GBDT in massive data processing.

<!-- b000245 | prose | pages [13] -->
One of the characteristics of LightGBM is the use of a Histogram-based decision tree algorithm, which first discretizes the continuous eigenvalues into k values, and then gen- erates a histogram with a width of k. When traversing samples, it uses the discretized value as an index. After a traversal, the histogram accumulates the required statistics and then traverses to find the optimal segmentation point through the discrete value of the histogram.

<!-- b000246 | caption | pages [13] -->
Figure 8: Histogram-Based Decision Tree Algorithm

<!-- b000247 | prose | pages [13] -->
Another feature of LightGBM is to adopt a more efficient leaf growth strategy, namely the leaf growth strategy with depth limitation (Leaf-wise). Before splitting, this strategy first traverses all the leaves in the tree, and then finds the leaf with the largest splitting gain to split again, and repeats this operation. Experiments have proved that under the same number of splits, Leaf-wise can get higher accuracy, and a maximum depth limit to prevent over-fitting has been added to Leaf-wise.

<!-- b000248 | prose | pages [13] -->
The leaf-wise leaf growth strategy is shown in the figure below, where the white and black dots represent the leaves with the maximum and non-maximum split gains, respec- tively:

<!-- b000249 | caption | pages [13] -->
Figure 9: Schematic Diagram of Leaf-Wise Tree Growth

<!-- b000250 | prose | pages [13] -->
6.2 Data Description and Preprocessing

<!-- b000251 | prose | pages [13] -->
The main purpose of this model is to identify whether the attributes of words affect the Hard Mode percentage, as well as explore the mechanism of influence. Therefore, the label of the model is the Hard Mode percentage of the current period, denoted as pctt.

<!-- b000252 | furniture | pages [14] -->
Team # 2307946

<!-- b000253 | furniture | pages [14] -->
Page 13 of 25

<!-- b000254 | prose | pages [14] -->
Considering the hysteresis effect of the previous word attributes and label itself on the label of the current period, our feature sequence includes the lag terms from one period(1 day) to five period (5 days of all the attributes indicators involved in Table 3, as well as the current value of Hard Mode percentage and one period to five period lag terms of it. If all the attributes of the given word in period t are denoted as X, then the model input contains:

<!-- b000255 | prose | pages [14] -->
pctt−1, pctt−2, · · · , pctt−5; Xt, Xt−1, · · · , Xt−5 (3)

<!-- b000256 | prose | pages [14] -->
In order to ensure the validity and reliability of the model, the data set needs to be preprocessed. A very important step is to normalize the value of each attribute and map the data to [0, 1]. The method is listed below:

<!-- b000257 | prose | pages [14] -->
v −vmin vs =

<!-- b000258 | prose | pages [14] -->
(4)

<!-- b000259 | prose | pages [14] -->
vmax −vmin

<!-- b000260 | prose | pages [14] -->
Among them, vs is the standardized value, v is the original value, vmax, and vmin rep- resent the maximum and minimum values of the attribute respectively. The normalized data are collectively referred to as Datainput.

<!-- b000261 | prose | pages [14] -->
6.3

<!-- b000262 | heading | pages [14] -->
Model Results and Evaluation

<!-- b000263 | prose | pages [14] -->
We utilized the above data, and input the feature sequence to train the model with the ratio of training set : test set = 4 : 1. Then the model would assign different weights to different features by making a large amount of historical data correlation calculation, and output the estimated (or predicted) value of Hard Mode Percentage using these weights.

<!-- b000264 | prose | pages [14] -->
For the purpose of verifying the reliability of the LightGBM model, we used MSE, RMSE, and SMAPE of the prediction results as the measurement indicators of the model accuracy. After parameter optimization, the calculation results of each indicator within the training set and validation set are as follows:

<!-- b000265 | caption | pages [14] -->
Table 4: Model Accuracy Test Results

<!-- b000266 | prose | pages [14] -->
MSE RMSE SMAPE 3.623 × 10−6 Training set 0.0019 0.0253 3.382 × 10−5 validation set 0.0058 0.0690

<!-- b000267 | prose | pages [14] -->
As all the indicators are apparently small, we can easily assert that the model result fits the real data very well. This conclusion can also be drawn from the scatter plot of the predicted value and the observed value below.

<!-- b000268 | furniture | pages [15] -->
Team # 2307946

<!-- b000269 | furniture | pages [15] -->
Page 14 of 25

<!-- b000270 | caption | pages [15] -->
Figure 10: Comparison of Predicted Results of LightGBM and Observed Value

<!-- b000271 | prose | pages [15] -->
Due to the reliability of the model, we can use the weight of each feature to judge whether the attributes of the word affect the Hard Mode Percentage. It can be concluded from the weight map of the feature that time lag items of the label itself are the most influential, while the time lag items of the word attributes are the next. Therefore, the Hard Mode Percentage of the current day’s game is related to the given words’ attributes of the previous periods and has almost nothing to do with the word attributes today, despite the ratio being mainly affected by its own lag terms.

<!-- b000272 | prose | pages [15] -->
As mentioned in subsection 5.2, if the words in the previous periods are difficult, the player will be more inclined not to choose Hard Mode for the current period. What’s more, since the player does not know the difficulty of the current period of words before choosing, the word attributes of the current period should not affect the player’s choice which is consistent with the predictions of our model.

<!-- b000273 | caption | pages [15] -->
Figure 11: Relative Importance of Features

<!-- b000274 | furniture | pages [16] -->
Team # 2307946

<!-- b000275 | furniture | pages [16] -->
Page 15 of 25

<!-- b000276 | prose | pages [16] -->
7

<!-- b000277 | heading | pages [16] -->
Model III: Multiple Input - Multiple Output Regression

<!-- b000278 | heading | pages [16] -->
Model

<!-- b000279 | prose | pages [16] -->
Multiple input - multiple output regression model is mainly used to solve the regres- sion problem involving predicting two or more values when given an input example. Generally, there are two types of ideas - one is to train multiple regressors based on the machine learning model, and the other is to modify the number of output layers based on the deep learning model. Experience has shown that due to the large amount of neu- ral network parameters, when the data amount is small, using feature engineering and ensemble learning method may have better prediction results than directly using deep learning models.

<!-- b000280 | prose | pages [16] -->
7.1

<!-- b000281 | heading | pages [16] -->
White Noise Verification

<!-- b000282 | prose | pages [16] -->
Firstly, we ran a white noise test 1on each of the associated percentages of guess at- tempts for a future date2. If the data passed the white noise test, it means that it is not affected by the time trend. Therefore, we can use the cross-sectional data of word at- tributes and distribution for subsequent modeling and predictions.

<!-- b000283 | prose | pages [16] -->
Take date as the horizontal axis and the percentage of 1 to 7 or more tries as the vertical axis to make a smooth-lined scatter plot. It can be seen from the figure that the trend of 2-6tries is relatively stationary, while the percentage of 1 and 7tries have some less stationary values. The reason may be that there are extremely easy and extremely difficult questions on certain days.

<!-- b000284 | prose | pages [16] -->
At the same time, it can be seen from the ACF diagram that the autocorrelation co- efficients of 2-7 tries are relatively small, while the autocorrelation coefficient of 1 try is slightly larger.

<!-- b000285 | caption | pages [16] -->
Figure 12: Scatted Plot and ACF Diagram For the Distribution of Reported Results

<!-- b000286 | prose | pages [16] -->
We conducted the Box-Pierce White Noise Test on these 7 percentages, and found out their p-values were all higher than 0.05, which passed the test.

<!-- b000287 | prose | pages [16] -->
1white noise means a purely random sequence, with no relationship between yesterday’s and today’s values

<!-- b000288 | prose | pages [16] -->
2(1 try, 2 tries, 3 tries,· · · , 6 tries, and X)

<!-- b000289 | furniture | pages [17] -->
Team # 2307946

<!-- b000290 | furniture | pages [17] -->
Page 16 of 25

<!-- b000291 | prose | pages [17] -->
7.2

<!-- b000292 | heading | pages [17] -->
Model Introduction

<!-- b000293 | prose | pages [17] -->
Therefore, our analysis tried to compare the effects of the following two models on this data set, then adopted data augmentation, feature engineering and other methods to improve the model effect.

<!-- b000294 | prose | pages [17] -->
• Multiple output regression model based on GBDT algorithm:

<!-- b000295 | prose | pages [17] -->
The idea of this model is to train multiple regressors based on the GBDT algorithm, respectively fitting the seven dependent variables of 1 try to 7 or more tries (X), with no correlation between the regressors.

<!-- b000296 | prose | pages [17] -->
• Multiple output regression model based on MMoE:

<!-- b000297 | prose | pages [17] -->
Multi-task learning refers to the method of training multiple objective functions at the same time. Its main advantage is that it can improve the learning efficiency and quality of each task. In addition, it can effectively overcome the shortcomings of large task noise, insufficient training samples, high data dimensionality, and sparse data sets.

<!-- b000298 | prose | pages [17] -->
The framework of multi-task learning widely adopts the shared-bottom structure, which means the hidden layer at the bottom is shared between different tasks. This struc- ture can essentially reduce the risk of overfitting, but the effect may be affected by task differences and data distribution.

<!-- b000299 | caption | pages [17] -->
Figure 13: MMoE’s Advantage Shown by Comparison

<!-- b000300 | prose | pages [17] -->
Therefore, a content recommendation team at Google proposed a Multi-gate Mixture- of-Experts (MMoE) multi-task learning structure. The improvement of MmoE is that, compared with the basic shared-bottom structure, it captures the differences in tasks without significantly increasing the requirements of model parameters. Compared with all tasks sharing a gating network (One-gate MoE model, as shown above), each task in MMoE uses separate gating networks. The gating networks of each task realize the se- lective utilization of experts through different final output weights. Gating networks of different tasks can learn different modes of combining experts, so the model takes into

<!-- b000301 | furniture | pages [18] -->
Team # 2307946

<!-- b000302 | furniture | pages [18] -->
Page 17 of 25

<!-- b000303 | prose | pages [18] -->
account the relevance and differences of captured tasks, which is very suitable for pre- dicting the number of player attempts in this problem.

<!-- b000304 | prose | pages [18] -->
We input word attributes and ran the two models described in Section 7.2 to predict the distribution of the reported results, but the prediction results still need to be opti- mized.

<!-- b000305 | prose | pages [18] -->
7.3

<!-- b000306 | heading | pages [18] -->
Model Refinement

<!-- b000307 | prose | pages [18] -->
7.3.1 Data Augmentation

<!-- b000308 | prose | pages [18] -->
For multi-input and multi-output problems, neural networks are generally used for modeling processing, but neural networks or deep learning require a large amount of data to be used for training. As the total sample size in this question is 359, it is difficult to get sufficient data for training the neural network. However, it may be possible to expand the data set through data augmentation.

<!-- b000309 | prose | pages [18] -->
CTGAN is a collection of Deep Learning based synthetic data generators for single tabular data, which is able to learn from observed data and generate synthetic data with high fidelity [11]. It should be noted that the data generator cannot limit the relationship between variables, the sum of percentage from 1 try to 7 tries in the generated sample may be quite different from 100%. So we used CTGAN to generate new samples, filtered out the samples that meet the conditions and merge them into the original data set. Finally, our sample size was about 4000.

<!-- b000310 | prose | pages [18] -->
After obtaining the enhanced samples, the above two models were retrained. How- ever, we found that the training results did not improve significantly, possibly because the original sample size was too small.

<!-- b000311 | prose | pages [18] -->
7.4 Feature Engineering

<!-- b000312 | prose | pages [18] -->
Generally speaking, data and features determine the upper limit of machine learning, and models and algorithms only approach this upper limit. In addition to optimizing the model from the perspective of data, it is also possible to extract features from the original data to the maximum extent, that is, feature engineering.

<!-- b000313 | prose | pages [18] -->
OpenFE is a new framework for automated feature generation for tabular data. [12]Us- ing OpenFE as a tool, we perform feature engineering on the unaugmented and aug- mented datasets separately to generate datasets containing new features. After this pro- cess, we retrained the above two models using the new data set. Luckily, the results have been significantly improved.

<!-- b000314 | prose | pages [18] -->
7.5

<!-- b000315 | heading | pages [18] -->
Model Results and Evaluation

<!-- b000316 | prose | pages [18] -->
Our prediction for the word EERIE on March 1, 2023 is as follows:

<!-- b000317 | prose | pages [18] -->
The predictive effectiveness of the two types of models shows obvious differences. The multiple output regression model based on GBDT has a large variance in total MSE between the training set and the verification set. This indicates that the machine learning model has poor model generalization performance when the data set is small. The MSE

<!-- b000318 | furniture | pages [19] -->
Team # 2307946

<!-- b000319 | furniture | pages [19] -->
Page 18 of 25

<!-- b000320 | prose | pages [19] -->
of the training set and validation set when using the multiple output regression model based on MMoE are relatively close. What’s more, they are apparently lower than the former model, showing an obvious advantage.

<!-- b000321 | prose | pages [19] -->
Unexpectedly, data augmentation led to a significant decline in the performance of both types of models, indicating that the new data brings greater noise to model training; feature engineering has no effect on the former, however brings a small improvement in the performance of the latter. Therefore, we finally chose the multiple output regression

<!-- b000322 | heading | pages [19] -->
model based on MMoE plus features engineering mode. After parameter optimization,

<!-- b000323 | prose | pages [19] -->
the prediction results of the word EERIE on March 1, 2023 are as follows:

<!-- b000324 | prose | pages [19] -->
Percent in 1 try 2 tries 3 tries 4 tries Number 0.649 7.579 26.298 32.614 5 tries 6 tries 7 or more tries (X) Total 20.930 9.63 2.298 99.998

<!-- b000325 | caption | pages [19] -->
Table 5: Prediction Result of Distribution

<!-- b000326 | heading | pages [19] -->
Model IV: LightGBM Classifier based on K-means Clus-

<!-- b000327 | prose | pages [19] -->
8

<!-- b000328 | heading | pages [19] -->
tering Model

<!-- b000329 | prose | pages [19] -->
The purpose of this model is to classify solution words by difficulty. When making classification, We first use the K-means clustering model to divide the word samples in the data set into several groups according to the average number of puzzle-solving

<!-- b000330 | heading | pages [19] -->
attempts. After that, use the LightGBM algorithm to classify them into corresponding

<!-- b000331 | prose | pages [19] -->
groups by using the attributes of the given words.

<!-- b000332 | prose | pages [19] -->
8.1 Concept of K-means Clustering

<!-- b000333 | prose | pages [19] -->
Distance-based clustering often uses measurement methods, such as K-means, K-medoids, etc. Among them, the current most popular heuristic method is the K-means algorithm. So we used the percentage that guessed the word in one to seven tries given in the data set as clustering basis and ran the K-means clustering model.

<!-- b000334 | prose | pages [19] -->
Given a set of data points and the number of clusters required, the K-means algorithm moves the data points into each cluster domain iteratively according to a specific distance function, the general implementation steps are as follows:

<!-- b000335 | prose | pages [19] -->
1. Given a sample word data set with a size of n, let the number of iterations be R, and randomly select k words as the initial cluster centers according to the specified number of clusters k, labeled as Cj(r), j= 1, 2, 3,· · · ,k; r=1, 2, 3,· · · , R.

<!-- b000336 | prose | pages [19] -->
2. Calculate the similarity distance D(Xi, Cj(r)) between each data object in the sample and the initial cluster center; among them, i=1, 2, 3,..., n, then form a cluster Wj, if it satisfies the formula (5)

<!-- b000337 | prose | pages [19] -->
n

<!-- b000338 | prose | pages [19] -->
|D (Xi+1, Cj(r)) −D (Xi, Cj(r))|2 < ε

<!-- b000339 | prose | pages [19] -->
X

<!-- b000340 | prose | pages [19] -->
i=1

<!-- b000341 | prose | pages [19] -->
(5)

<!-- b000342 | prose | pages [19] -->
ThenXi ∈Wj,Xi is denoted as w, where ϵ is any given positive number.

<!-- b000343 | furniture | pages [20] -->
Team # 2307946

<!-- b000344 | furniture | pages [20] -->
Page 19 of 25

<!-- b000345 | prose | pages [20] -->
3. Calculate k new cluster centers, the calculation formula is as follows:

<!-- b000346 | prose | pages [20] -->
nj

<!-- b000347 | prose | pages [20] -->
Cj(r + 1) = 1

<!-- b000348 | prose | pages [20] -->
X(j)

<!-- b000349 | prose | pages [20] -->
X

<!-- b000350 | prose | pages [20] -->
(6) i

<!-- b000351 | prose | pages [20] -->
n

<!-- b000352 | prose | pages [20] -->
i=1

<!-- b000353 | prose | pages [20] -->
The formula for calculating the value of the clustering criterion function is as fol- lows:

<!-- b000354 | prose | pages [20] -->
k X

<!-- b000355 | prose | pages [20] -->
E(r + 1) =

<!-- b000356 | prose | pages [20] -->
i=1

<!-- b000357 | prose | pages [20] -->
X

<!-- b000358 | prose | pages [20] -->
|w −Cj(r + 1)|2 (7)

<!-- b000359 | prose | pages [20] -->
w∈Wj

<!-- b000360 | prose | pages [20] -->
4. To judge whether the clustering is reasonable, the discriminant formula is listed below:

<!-- b000361 | prose | pages [20] -->
|E(r + 1) −E(r)| < ε (8)

<!-- b000362 | prose | pages [20] -->
If the result is reasonable, the iteration terminates; while if it is not, return to steps 2 and 3.

<!-- b000363 | prose | pages [20] -->
8.2

<!-- b000364 | heading | pages [20] -->
Clustering Model Building

<!-- b000365 | prose | pages [20] -->
In order to determine a reasonable number of clusters k, we first made k=1, 2, 3...,10 as the experimental number of clusters, then used Python to run the K-means clustering model. Finally, calculate the sum of squares due to error (SSE) of the results with different k values. With the number of clusters k as the horizontal axis and SSE as the vertical axis, a scatter diagram with a trend line is made as follows:

<!-- b000366 | caption | pages [20] -->
Figure 14: Determine the Number of Clusters

<!-- b000367 | prose | pages [20] -->
We had to make a balance between the minimal value of SSE and the smallest possible amount of the number of groups. It can be derived from the figure that when the k value is less than 4, as the number of clusters increases, the SSE decreases rapidly. On the contrary, when k is greater than 4, the downward trend is not obvious. So the most suitable k value Which achieves the aforementioned balance is 4.

<!-- b000368 | furniture | pages [21] -->
Team # 2307946

<!-- b000369 | prose | pages [21] -->
8.3

<!-- b000370 | heading | pages [21] -->
Evaluation of Clustering Result

<!-- b000371 | furniture | pages [21] -->
Page 20 of 25

<!-- b000372 | prose | pages [21] -->
In order to verify the effectiveness of clustering, we calculated the mean difficulty value for each group, which is represented by the average number of attempts a player has to make to guess the word. The more tries a player made, the more difficult the given word is. The calculation formula is as follows:

<!-- b000373 | prose | pages [21] -->
7 X

<!-- b000374 | prose | pages [21] -->
distributei × i

<!-- b000375 | prose | pages [21] -->
Average Number of Tries =

<!-- b000376 | prose | pages [21] -->
(9)

<!-- b000377 | prose | pages [21] -->
i=1

<!-- b000378 | prose | pages [21] -->
The number of words in each group, the average number of tries to guess the word as well as Skewnesses in each group are shown in the table below.

<!-- b000379 | caption | pages [21] -->
Table 6: Clustering Result Evaluation

<!-- b000380 | prose | pages [21] -->
Group 0 No.of Words 34 Average Difficulty 3.574 Skew 0.320 1 2 3 127 125 57 3.951 4.326 4.800 0.246 0.0918 -0.181

<!-- b000381 | prose | pages [21] -->
The data in the table shows that the average number of tries and skewness of each group are significantly different, indicating that our Clustering is relatively effective.

<!-- b000382 | prose | pages [21] -->
Identification of Important Attributes 8.4

<!-- b000383 | prose | pages [21] -->
We have divided words into groups according to difficulty in the analysis above. Next, we would further make an in-depth analysis, hoping to link the classification of word dif- ficulty with its own attributes, and solve the problem of "why is this word more difficult"?

<!-- b000384 | prose | pages [21] -->
We again used the LightGBM model, taking the 4 clustered groups obtained by the clustering algorithm as labels, and used the word attributes listed in subsection 5.2 as input features to train the lightGBM model. The training result(Figure 15) reflects the importance of each attribute of the word in terms of affecting the word’s difficulty level. What’s more, we can utilise the model to classify a given word into clustered groups above.

<!-- b000385 | prose | pages [21] -->
Therefore, most of the attributes of the word are related to classification, while the most relevant attributes are BG_sum, num_repeat, Semantic_diversity, PLD, and Phono_N. The impact of word attributes on difficulty also mainly comes from these five indicators.

<!-- b000386 | heading | pages [21] -->
Classfication Result and Evaluation

<!-- b000387 | prose | pages [21] -->
8.5

<!-- b000388 | prose | pages [21] -->
Referring to the result of 7.4,the key attributes of the word "EERIE" are:

<!-- b000389 | prose | pages [21] -->
We input these attributes into the LightGBM classification model, and the output showed that this word belongs to the second category, which is the second lowest level of difficulty.

<!-- b000390 | furniture | pages [22] -->
Team # 2307946

<!-- b000391 | furniture | pages [22] -->
Page 21 of 25

<!-- b000392 | caption | pages [22] -->
Figure 15: Importance of Features in Classfication

<!-- b000393 | caption | pages [22] -->
Table 7: Part of key attributes of EERIE

<!-- b000394 | prose | pages [22] -->
Word Phono_N BG_Sum PLD EERIE 8 11159 1.4 Semantic_Diversity num_repeat 1.487 4

<!-- b000395 | prose | pages [22] -->
We used a variety of indicators to measure the accuracy of the LightGBM classification model. The results are shown in the table below. By analyzing the results, we could assert that our model made a quite accurate classification regarding the words in the data set.

<!-- b000396 | caption | pages [22] -->
Table 8: Mesuring Accuracy of Classification

<!-- b000397 | prose | pages [22] -->
Accuracy Validation set 71.13% Traning set 98.28% Precision Recall F1-score 71.85% 66.54% 69.09% 98.82% 98.79% 98.28%

<!-- b000398 | prose | pages [22] -->
Other Interesting Features of the Data Set 9

<!-- b000399 | prose | pages [22] -->
1. It can be seen from Figure 4 that the number of users of the game rose rapidly in a short period of time, while then declining rapidly, reflecting the short-term popu- larity of the game. In addition, the percentage of people who chose the Hard Mode gradually increased over time, indicating that users gradually mastered the game.

<!-- b000400 | prose | pages [22] -->
2. Figure 16 is a word cloud diagram drawn according to the frequency of use. Most of the high-frequency words are pronouns and auxiliary verbs, followed by nouns.

<!-- b000401 | prose | pages [22] -->
3. Observing the distribution of the number of user attempts in Figure 17, the kernel density function of less difficult words is flat and skewed to the right; while the kernel density function of more difficult words has a higher peak value, mostly concentrated at 4 times.

<!-- b000402 | furniture | pages [23] -->
Team # 2307946

<!-- b000403 | furniture | pages [23] -->
Page 22 of 25

<!-- b000404 | caption | pages [23] -->
Figure 16: The Word Cloud

<!-- b000405 | prose | pages [23] -->
4. It can be seen from Figure 18 that, among the various word attributes, the correla- tions between OrthoN, PhonoN, and word frequency are strong.

<!-- b000406 | caption | pages [23] -->
Figure 17: Kernel Density Function Plot

<!-- b000407 | caption | pages [23] -->
Figure 18: Correlation of Attributes

<!-- b000408 | prose | pages [23] -->
10

<!-- b000409 | heading | pages [23] -->
Sensitivity Analysis

<!-- b000410 | prose | pages [23] -->
10.1

<!-- b000411 | heading | pages [23] -->
Sensitivity Analysis for Question 1

<!-- b000412 | prose | pages [23] -->
By constructing the LightGBM model, we solved the problem of what factors (con- temporaneous or lagged) influence the current Hard Mode percentage. In order to test the sensitivity of the model, we applied random perturbations to the top five influential attributes derived in 8.4. Then observed whether there was a significant change in the relative importance of attributes. The results are shown in the table below:

<!-- b000413 | prose | pages [23] -->
Within it, the disturbance range p means that for the original value x, a random num- ber within the range of [(1 −p)x, (1 + p)x] is used to reassign x. No matter which number is drawn, it will not cause a great impact on the importance of attributes regarding pre- dicting Hard Mode Percentage.

<!-- b000414 | furniture | pages [24] -->
Team # 2307946

<!-- b000415 | furniture | pages [24] -->
Page 23 of 25

<!-- b000416 | caption | pages [24] -->
Table 9: Sensitivity Analysis for Model of Question 1

<!-- b000417 | prose | pages [24] -->
Attribute Name Disturbance range p When p is less than 0.15, the ranking of word attributes remains unchanged BG_Sum_1 BG_Sum_2

<!-- b000418 | prose | pages [24] -->
Ranking of word attributes with the second-largest to fifth-largest influence Semantic_Diversity_1 Semantic_Diversity_2 keeps steady when p is less than 0.1

<!-- b000419 | prose | pages [24] -->
OLD_1

<!-- b000420 | prose | pages [24] -->
It can be derived from the table that, to a certain extent, small-scale data disturbance will not affect the importance ranking of word attributes, which means that the model passed the sensitivity test.

<!-- b000421 | heading | pages [24] -->
Sensitivity Analysis for Question 3

<!-- b000422 | prose | pages [24] -->
10.2

<!-- b000423 | prose | pages [24] -->
In order to analyze the sensitivity of the classification model in this paper, we repeat- edly deleted x randomly selected samples from the total samples. We subsequently ana- lyzed whether the classification results had changed significantly, which is shown in the table below:

<!-- b000424 | caption | pages [24] -->
Table 10: Sensitivity Analysis for Model of Question 3

<!-- b000425 | prose | pages [24] -->
The number of times among 100 repeated tests heightx

<!-- b000426 | prose | pages [24] -->
when the classification result didn’t change 1 2 3 4 5 100 100 98 95 90

<!-- b000427 | prose | pages [24] -->
We can derive from the table that after 100 times of random deletion of 1-5 samples from the overall data set, the number of times among 100 repeated tests when the classi- fication result didn’t changes still reaches more than 90. That means, to a certain extent, small-scale sample changes will not have a significant impact on the classification result. The model for question 3 passed the sensitivity test as well.

<!-- b000428 | heading | pages [24] -->
Strengths and Weaknesses

<!-- b000429 | prose | pages [24] -->
11

<!-- b000430 | prose | pages [24] -->
11.1

<!-- b000431 | heading | pages [24] -->
Strengths

<!-- b000432 | prose | pages [24] -->
1. We have fully exploited a variety of word attributes that adequately reflected the information content of words as much as possible.

<!-- b000433 | prose | pages [24] -->
2. The model fully considered the data of the current period and lagged terms.

<!-- b000434 | prose | pages [24] -->
3. We tried a variety of machine learning and deep learning models as well as made an in-depth comparison of their performances.

<!-- b000435 | furniture | pages [25] -->
Team # 2307946

<!-- b000436 | furniture | pages [25] -->
Page 24 of 25

<!-- b000437 | prose | pages [25] -->
11.2

<!-- b000438 | heading | pages [25] -->
Weaknesses

<!-- b000439 | prose | pages [25] -->
1. We didn’t try to adopt a time series prediction model based on deep learning.

<!-- b000440 | prose | pages [25] -->
2. We didn’t fully overcome the problem of poor prediction accuracy caused by a small amount of data.

<!-- b000441 | prose | pages [25] -->
12

<!-- b000442 | heading | pages [25] -->
A Memorandum to the New York Times Puzzle Editor

<!-- b000443 | prose | pages [25] -->
Dear Editor:

<!-- b000444 | prose | pages [25] -->
We are a professional business analysis team from MCM. It‘s a great honor to be in- vited to answer your operation questions.

<!-- b000445 | prose | pages [25] -->
We are very delighted to see the game Wordle achieved great success in 2022. But to ensure long-term steady operation, you also need to have a deep understanding of the game’s operating mechanism. At your request, we analyzed the data mined from Twitter and we are here to answer your questions with confidence:

<!-- b000446 | prose | pages [25] -->
First of all, we adopted a time-series forecasting model which effectively explained the variation of the reported results’ number. Using this model, we are 80% sure that the number of reported results on March 1, 2023, should be between [10139, 30808]. Then, by adopting a machine learning model, we found out that the word attributes from the past have a limited impact on the percentage of scores reported that were played in Hard Mode, whereas word attributes of today’s word almost have no impact at all.

<!-- b000447 | prose | pages [25] -->
Then, we used a refined deep-learning model to predict the distribution of the re- ported results. For instance, for the word EERIE on March 1, 2023, the forecasted proba- bility distribution should be [0.649,7.579,26.298,32.614,20.930,9.63,2.298] (%)from 1 to 7 or more tries. This result passed a set of accuracy evaluations so it could be trusted.

<!-- b000448 | prose | pages [25] -->
After that, we established a difficulty classification model which is capable of classi- fying any given word by analyzing its attributes. When considering the word EERIE, the classification model infers that it should belong to the second easiest group of all 4 groups classified by difficulty. What’s more, we derived the top 5 attributes that are associated with classification.

<!-- b000449 | prose | pages [25] -->
Lastly, we further explored other interesting features of this data set, including word cloud map, kernel density classification map, etc.

<!-- b000450 | prose | pages [25] -->
By analyzing the recent operational performance of Wordle, we further made several suggestions on Wordle’s future operation:

<!-- b000451 | prose | pages [25] -->
1. There is a downward trend of the number of players, so new playing mode should be introduced to attract new players.

<!-- b000452 | prose | pages [25] -->
2. The hard mode pct is increasing steadily. In order to improve the gaming experi- ence, you should consider improving the difficulty of certain days’ game.

<!-- b000453 | furniture | pages [26] -->
Team # 2307946

<!-- b000454 | furniture | pages [26] -->
Page 25 of 25

<!-- b000455 | prose | pages [26] -->
3. In the future, you can consider setting 4 different game difficulties according to the classification result we acquired above.

<!-- b000456 | prose | pages [26] -->
Hope you find our suggestions helpful and wish Wordle become better and better!

<!-- b000457 | prose | pages [26] -->
Yours, Sincerely

<!-- b000458 | prose | pages [26] -->
MCM Team # 2307946

<!-- b000459 | heading | pages [26] -->
References

<!-- b000460 | references | pages [26] -->
[1] W. contributors, “Wordle. in wikipedia, the free encyclopedia,” Wikipedia, 2023.

<!-- b000461 | references | pages [26] -->
[2] C. R. Nelson and C. I. Plosser, “Trends and random walks in macroeconmic time

<!-- b000462 | references | pages [26] -->
series: Some evidence and implications,” Journal of Monetary Economics, vol. 10(2),

<!-- b000463 | references | pages [26] -->
pp. 139–162, 1982.

<!-- b000464 | references | pages [26] -->
[3] T. Jakaša, I. Androˇcec, and P. Sprˇci´c, “Electricity price forecasting — arima model

<!-- b000465 | references | pages [26] -->
approach,” in 2011 8th International Conference on the European Energy Market (EEM),

<!-- b000466 | references | pages [26] -->
pp. 222–225, 2011.

<!-- b000467 | references | pages [26] -->
[4] B. Laufer, “Ease and difficulty in vocabulary learning: Some teaching implications,”

<!-- b000468 | references | pages [26] -->
Foreign Language Annals, vol. 23, pp. 147–155, 1990.

<!-- b000469 | references | pages [26] -->
[5] J. Jagoda and T. Boi´nski, “Assessing word difficulty for quiz-like game,” pp. 70–79,

<!-- b000470 | references | pages [26] -->
2018.

<!-- b000471 | references | pages [26] -->
[6] D. Balota, M. Yap, and t. Hutchison, K.A., “The english lexicon project,” Behavior

<!-- b000472 | references | pages [26] -->
Research Methods, vol. 39, p. 445–459, 2007.

<!-- b000473 | references | pages [26] -->
[7] M. Brysbaert and V. Warriner, A. B.and Kuperman, “Concreteness ratings for

<!-- b000474 | references | pages [26] -->
40 thousand generally known english word lemmas,” Behavior Research Methods,

<!-- b000475 | references | pages [26] -->
vol. 46(3), p. 904–911, 2014.

<!-- b000476 | references | pages [26] -->
[8] P. Hoffman, M. Lambon Ralph, and T. Rogers, “Semantic diversity: A measure of

<!-- b000477 | references | pages [26] -->
semantic ambiguity based on variability in the contextual usage of words,” Behavior

<!-- b000478 | references | pages [26] -->
Research Methods, vol. 45, p. 718–730, 2013.

<!-- b000479 | references | pages [26] -->
[9] S. De Deyne, D. Navarro, A. Perfors, and et al., “The “small world of words” en-

<!-- b000480 | references | pages [26] -->
glish word association norms for over 12,000 cue words,” Behavior Research Methods,

<!-- b000481 | references | pages [26] -->
vol. 51, p. 987–1006, 2019.

<!-- b000482 | references | pages [26] -->
[10] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-Y. Liu, “Lightgbm:

<!-- b000483 | references | pages [26] -->
A highly efficient gradient boosting decision tree,” vol. 30, 2017.

<!-- b000484 | references | pages [26] -->
[11] L. Xu, M. Skoularidou, A. Cuesta-Infante, and K. Veeramachaneni, “Modeling tabu-

<!-- b000485 | references | pages [26] -->
lar data using conditional gan,” NeurIPS, 2019.

<!-- b000486 | references | pages [26] -->
[12] T. Zhang, Z. Zhang, Z. Fan, H. Luo, F. Liu, W. Cao, and J. Li, “Openfe: Automated

<!-- b000487 | references | pages [26] -->
feature generation beyond expert-level performance,” 2022.
