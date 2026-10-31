# P-C-2023-2314151-c97576e4

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2023

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | furniture | pages [1] -->
2314151

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Breaking the Wordle

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
As Wordle has become popular on social media, more and more users have played the scrabble game. How do time and word attributes affect the number of reports, distribution of attempts, and other report-related information? Therefore, a modeling analysis was conducted using the game data from 2022.

<!-- b000011 | prose | pages [1] -->
Before building the model, we cleaned and normalized the given data and identified word at- tributes such as the number of repeated letters, number of vowel letters, number of consonant letters, commonness, and frequency. Preliminary preparations were made for model building and solving.

<!-- b000012 | prose | pages [1] -->
First, to predict the number of future reports, a prophet-based time-series prediction model was built, considering the effects of trends, seasonality, and holidays. The predictions yielded a range of report numbers for March 1, 2023: [10355,18742]. Regarding the variation of report numbers, during the week, the number of reports tends to be highest on Wednesdays and lowest on weekends. In exploring the effect of word attributes on the proportion of difficulty reports, we calculated higher- order partial correlation coefficients for both, controlling for the interaction between word attributes, and found that the number of vowel letters, the number of non-repeats, and word commonness were negatively correlated. The number of consonant letters and the number of non-repeats was positively correlated.

<!-- b000013 | prose | pages [1] -->
Secondly, an optimized multi-objective regression prediction framework was developed to explore the effects of word attributes on the distribution of reported outcomes. The framework chose the optimal lasso regression to predict the test set with an RMSE of 0.80. The distribution of the number of attempts to predict ’EERIE’ was (0, 4, 17, 34, 30, 13, 2). The ranking importance of each attribute was calculated, and it was found that the number of consonant letters, number of vowel letters, and frequency had a more significant influence on the distribution of reported results with the influence factors of 4.226, 3.993, and 1.253, respectively.

<!-- b000014 | prose | pages [1] -->
Next, the above model was used to predict the distribution of reported outcomes for each word in the 5-letter word set. Then, K-means was used to classify the words into high (≥4.37), medium (4.13- 4.37), and low (<4.13) difficulty categories based on the average number of attempts, and it was found that the Number of duplicates, Maximum of repeats, Prevalence and Frequency differed significantly across categories. Moreover, the interval of each attribute was divided. According to the established model, ’EERIE’ is difficult. The model’s accuracy is 91.36 %by matching the attribute intervals for different difficulty words, and it can be inferred that the established model and the divided attribute intervals are reasonable.

<!-- b000015 | prose | pages [1] -->
Finally, the sensitivity analysis results demonstrate that our model is robust and reliable. In addition, The study of the data set also revealed the declining popularity of Wordle and the increasing percentage of difficult mode challenges, and provided the New York Times with suggestions for restoring the game’s popularity.

<!-- b000016 | keywords | pages [1] -->
Keywords: Wordle analysis, Prophet, High-order partial correlation, Multi-objective regression

<!-- b000017 | prose | pages [1] -->
forecasting, K-means

<!-- b000018 | furniture | pages [2] -->
Team # 2314151

<!-- b000019 | furniture | pages [2] -->
Page 1 of 24

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1 Introduction

<!-- b000022 | contents | pages [2] -->
2

<!-- b000023 | contents | pages [2] -->
1.1

<!-- b000024 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
2

<!-- b000026 | contents | pages [2] -->
1.2

<!-- b000027 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
2

<!-- b000029 | contents | pages [2] -->
1.3

<!-- b000030 | contents | pages [2] -->
Our Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
2

<!-- b000032 | contents | pages [2] -->
2 Preparation of the Models

<!-- b000033 | contents | pages [2] -->
3

<!-- b000034 | contents | pages [2] -->
2.1

<!-- b000035 | contents | pages [2] -->
Assumptions

<!-- b000036 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
3

<!-- b000038 | contents | pages [2] -->
2.2

<!-- b000039 | contents | pages [2] -->
Notations

<!-- b000040 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
3 Data Processing

<!-- b000043 | contents | pages [2] -->
4

<!-- b000044 | contents | pages [2] -->
3.1

<!-- b000045 | contents | pages [2] -->
Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
4

<!-- b000047 | contents | pages [2] -->
3.2

<!-- b000048 | contents | pages [2] -->
Outlier rejection and standardization . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
4

<!-- b000050 | contents | pages [2] -->
3.3

<!-- b000051 | contents | pages [2] -->
Word attribute determination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
5

<!-- b000053 | contents | pages [2] -->
4 Task 1

<!-- b000054 | contents | pages [2] -->
7

<!-- b000055 | contents | pages [2] -->
4.1

<!-- b000056 | contents | pages [2] -->
Prophet algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
7

<!-- b000058 | contents | pages [2] -->
4.2

<!-- b000059 | contents | pages [2] -->
Higher-order partial correlation analysis model

<!-- b000060 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
9

<!-- b000062 | contents | pages [2] -->
5 Task 2

<!-- b000063 | contents | pages [2] -->
12

<!-- b000064 | contents | pages [2] -->
5.1

<!-- b000065 | contents | pages [2] -->
Multi-objective regression prediction framework . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
12

<!-- b000067 | contents | pages [2] -->
5.2

<!-- b000068 | contents | pages [2] -->
Establishment of prediction model . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
13

<!-- b000070 | contents | pages [2] -->
5.3

<!-- b000071 | contents | pages [2] -->
Word prediction - EERIE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
14

<!-- b000073 | contents | pages [2] -->
5.4

<!-- b000074 | contents | pages [2] -->
Feature influence degree analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
15

<!-- b000076 | contents | pages [2] -->
5.5

<!-- b000077 | contents | pages [2] -->
Model reliability analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
15

<!-- b000079 | contents | pages [2] -->
6 Task 3

<!-- b000080 | contents | pages [2] -->
16

<!-- b000081 | contents | pages [2] -->
6.1

<!-- b000082 | contents | pages [2] -->
K-means clustering algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
17

<!-- b000084 | contents | pages [2] -->
6.2

<!-- b000085 | contents | pages [2] -->
Selection of parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
17

<!-- b000087 | contents | pages [2] -->
6.3

<!-- b000088 | contents | pages [2] -->
Clustering results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [2] -->
18

<!-- b000090 | contents | pages [2] -->
6.4

<!-- b000091 | contents | pages [2] -->
Word interval identification - EERIE . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [2] -->
18

<!-- b000093 | contents | pages [2] -->
6.5

<!-- b000094 | contents | pages [2] -->
Model reliability analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [2] -->
19

<!-- b000096 | contents | pages [2] -->
7 Interesting aspects of the data

<!-- b000097 | contents | pages [2] -->
20

<!-- b000098 | contents | pages [2] -->
8 Sensitivity Analysis

<!-- b000099 | contents | pages [2] -->
21

<!-- b000100 | contents | pages [2] -->
9 Strengths and Weaknesses

<!-- b000101 | contents | pages [2] -->
22

<!-- b000102 | contents | pages [2] -->
9.1

<!-- b000103 | contents | pages [2] -->
Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [2] -->
22

<!-- b000105 | contents | pages [2] -->
9.2

<!-- b000106 | contents | pages [2] -->
Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [2] -->
22

<!-- b000108 | contents | pages [2] -->
10 Letter

<!-- b000109 | contents | pages [2] -->
22

<!-- b000110 | furniture | pages [2] -->
1

<!-- b000111 | furniture | pages [3] -->
Team # 2314151

<!-- b000112 | furniture | pages [3] -->
Page 2 of 24

<!-- b000113 | heading | pages [3] -->
1 Introduction

<!-- b000114 | heading | pages [3] -->
1.1 Problem Background

<!-- b000115 | prose | pages [3] -->
Crossword puzzles have always seemed inseparably linked to the media. Since January 2022, Wor- dle, the New York Times’ digital crossword, has become more and more popular in many countries[1].

<!-- b000116 | prose | pages [3] -->
How do players play Wordle? They are permitted to select five letters from a pool of 26 to construct a five-letter word that can be solved in no more than six attempts to conclude the Wordle puzzle successfully. After the player submits the word, the sticker’s color will change. Green is the correct letter, and yellow is the letter in the word but in the wrong place. There are two modes of play: normal mode and hard mode. Hard mode is where the correct letter (green or yellow) is found in the previous attempt and must be used in subsequent attempts.

<!-- b000117 | prose | pages [3] -->
Wordle updates the puzzle once a day, and many players report their scores on social media. As a result, data such as the number of people reporting their scores that day, the number of players participating in hard mode, and the percentage of players completing the puzzle on different attempts are all collected and counted. By using the available data wisely, we can solve some interesting problems.

<!-- b000118 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000119 | prose | pages [3] -->
Considering the background information, constraints outlined in the problem statement and addi- tional guidance, we need to solve the following problems:

<!-- b000120 | prose | pages [3] -->
• Task 1: Establish a model that can explain and predict changes in the number of reported results and provide a prediction interval for the number of reported results on March 1, 2023. In addition, an examination of the impact of word attributes on the proportion of reports filed by players in the hard mode is necessary, accompanied by a rationale for this phenomenon.

<!-- b000121 | prose | pages [3] -->
• Task 2: Develop a model that predicts reported outcomes’ distribution and explore the uncer- tainties the model and predictions have.

<!-- b000122 | prose | pages [3] -->
• Task 3: Build a model for classifying words according to difficulty and determine the factors associated with word classification. This model is used to determine the difficulty of EERIE and to discuss the accuracy of the classification model.

<!-- b000123 | prose | pages [3] -->
• Task 4: Enumerate and explicate additional noteworthy characteristics inherent in this dataset.

<!-- b000124 | prose | pages [3] -->
• Task 5: Present a concise summary of the study findings in a letter addressed to the Puzzle Editor of the New York Times.

<!-- b000125 | heading | pages [3] -->
1.3 Our Works

<!-- b000126 | prose | pages [3] -->
Based on the analysis of the problem, we propose the model framework shown in figure 1, which is mainly composed of the following parts:

<!-- b000127 | prose | pages [3] -->
Data analysis: processes the reported data and identifies the characteristics of the words.

<!-- b000128 | furniture | pages [3] -->
2

<!-- b000129 | furniture | pages [4] -->
Team # 2314151

<!-- b000130 | furniture | pages [4] -->
Page 3 of 24

<!-- b000131 | prose | pages [4] -->
Predictive modeling: Prophet algorithm was chosen to build a time-series regression prediction model, and a higher-order partial correlation analysis was used to find the degree of influence of each attribute.

<!-- b000132 | prose | pages [4] -->
Development of a multi-objective regression prediction framework: use this framework to help us select a Lasso regression prediction model.

<!-- b000133 | prose | pages [4] -->
Difficulty interval division: the word difficulty was classified into three categories using the K-means algorithm and the classification results were validated by Lasso regression prediction.

<!-- b000134 | caption | pages [4] -->
Figure 1: Model framework

<!-- b000135 | heading | pages [4] -->
2 Preparation of the Models

<!-- b000136 | heading | pages [4] -->
2.1 Assumptions

<!-- b000137 | prose | pages [4] -->
• Assumption 1. Assume that the user data given in the question is independently and identically distributed.

<!-- b000138 | prose | pages [4] -->
Reason 1: this assumption ensures that the individual samples are independent of each other to avoid the influence of the modeling process due to the association between the samples.

<!-- b000139 | prose | pages [4] -->
• Assumption 2. Assume that the pre-processed data is reliable.

<!-- b000140 | prose | pages [4] -->
Reason 2: this assumption is made to ensure the accuracy of the model solution.

<!-- b000141 | prose | pages [4] -->
• Assumption 3. Assume that the external environment associated with the game does not change abruptly

<!-- b000142 | prose | pages [4] -->
Reason 3: external factors remain steady to ensure stable prediction models.

<!-- b000143 | furniture | pages [4] -->
3

<!-- b000144 | furniture | pages [5] -->
Team # 2314151

<!-- b000145 | furniture | pages [5] -->
Page 4 of 24

<!-- b000146 | heading | pages [5] -->
2.2 Notations

<!-- b000147 | caption | pages [5] -->
Table 1: Notations

<!-- b000148 | prose | pages [5] -->
Symbol Definition

<!-- b000149 | prose | pages [5] -->
sj Timestamp k Growth rate δj The amount of change in the growth rate on the timestamp m Offset amount ϵ Error term N Number of cycles in the seasonality model Di Period before and after a holiday κi Range of holiday effects P Significance level

<!-- b000150 | heading | pages [5] -->
3 Data Processing

<!-- b000151 | heading | pages [5] -->
3.1 Data Cleaning

<!-- b000152 | prose | pages [5] -->
Topic C reports on the use of Wordle in the past year. However, we found a lot of dirty data in this report.

<!-- b000153 | caption | pages [5] -->
Table 2: Dirty data

<!-- b000154 | prose | pages [5] -->
Contest number Word Number of reported results Number in hard mode 1 try 2 tries 3 tries 4 tries 5 tries 6 tries 7 or more tries (X) 525 clen 26381 2424 1 17 36 31 12 3 0 314 tash 106652 7001 2 19 34 27 13 4 1 na¨ıve 540 21947 2075 1 7 24 32 24 11 1 473 marxh 30935 2885 0 9 30 35 19 6 1 207 favor 137586 3073 1 4 15 26 29 21 4

<!-- b000155 | prose | pages [5] -->
In the data shown above, the two words numbered 525, and 314 do not match the game because they are only 4 in length, so we inferred that the dataset blundered by under-entering the letters. To solve such a problem, we found the most similar letters to them instead by comparing them with artificial intelligence algorithms. The word numbered 540 is due to a misspelling of the letter, which should be ”naive.” We searched the word database and found that the word ”marxh,” numbered 473, did not exist. We then compared the shapes of the words with database analysis and concluded that the correct spelling should be ”marsh.” The word numbered 207 has an extra space in the input, so it is also an outlier. We can delete the extra space to get the correct data.

<!-- b000156 | heading | pages [5] -->
3.2 Outlier rejection and standardization

<!-- b000157 | prose | pages [5, 6] -->
We use the 68–95–99.7 rule (3σ criterion) to screen and reject outliers[2]. We found an anomaly in the Number of reported results data for the word ’study’ on 2022/11/30, and we zeroed it to bring it back to the same order of magnitude.

<!-- b000158 | furniture | pages [5] -->
4

<!-- b000159 | furniture | pages [6] -->
Team # 2314151

<!-- b000160 | furniture | pages [6] -->
Page 5 of 24

<!-- b000162 | prose | pages [6] -->
(a) 3σ criterion (b) Deviation point rejection

<!-- b000163 | caption | pages [6] -->
Figure 2: Outlier rejection

<!-- b000164 | prose | pages [6] -->
In addition, we also use the StandardScaler data normalization method, which normalizes the training set data by calculating the mean and standard deviation of the training set[3], see equation z = x −u (1) s x is the sample, u is the mean of the feature columns of the training set, and s is the standard deviation of the feature columns of the training set.

<!-- b000165 | heading | pages [6] -->
3.3 Word attribute determination

<!-- b000166 | prose | pages [6] -->
In the topic for the prediction of the reported results, we need to analyze the properties of the words. Combining Wordle’s gameplay and reviewing the analysis information of the relevant games, we classify the attributes of words into the following points.

<!-- b000167 | prose | pages [6] -->
1. The total frequency of letters appearing in words: Count the frequency of each letter appearing in the candidate word list. If a letter appears in 900 words, its frequency is 900. Then the candidate words are sorted by total letter frequency, and if a word contains more high-frequency letters, it is ranked first.

<!-- b000168 | caption | pages [6] -->
Figure 3: Total frequency of letters in a word

<!-- b000169 | furniture | pages [6] -->
5

<!-- b000170 | furniture | pages [7] -->
Team # 2314151

<!-- b000171 | furniture | pages [7] -->
Page 6 of 24

<!-- b000172 | prose | pages [7] -->
2. The number of vowel/consonant letters in a word: When players play Wordle, the first words are often chosen as AUDIO and LEFTY because this includes all the vowel letters: ’AEIOU.’ In the composition of words, vowel letters are easily known and, therefore, easily guessed.

<!-- b000173 | heading | pages [7] -->
3. The number of occurrences of different vowel/consonant letters in a word (no duplication):

<!-- b000174 | prose | pages [7] -->
The number of vowel/consonant letters is one of the attributes of a word that we infer affects the percentage of guessed words. Accordingly, the number of vowels/consonants is also essential in the percentage of reported words. Let us take ’there’ for example. The number of vowels is 2, The Number of vowels(no duplication) is 1, the number of consonants is 3, and the number of vowels(no duplication) is 3.

<!-- b000175 | caption | pages [7] -->
Table 3: Alphabetic properties

<!-- b000176 | prose | pages [7] -->
Word Number of vowels (no duplication) Number of consonants (no duplication)

<!-- b000177 | prose | pages [7] -->
there 2 1 3 3

<!-- b000178 | prose | pages [7] -->
4. Frequency of word usage: We use many words in our daily lives, some common and some not so familiar. People tend to guess common words more easily. Therefore, we have listed and sorted the frequency of use of all the five-letter words involved in this game. The following table shows the partially sorted data.

<!-- b000179 | caption | pages [7] -->
Table 4: Letter Commonness Ranking

<!-- b000180 | prose | pages [7] -->
Word Times Rank Word Times Rank Word Times Rank

<!-- b000181 | prose | pages [7] -->
which 0.002044 1 their 0.001954 2 would 0.001711 3 about 0.001407 4 could 0.001296 5 there 0.001273 6

<!-- b000182 | heading | pages [7] -->
5. The number of repeated letters and the maximum number of repetitions: There may be

<!-- b000183 | prose | pages [7] -->
several repeated letters in the formation of a word. It isn’t common, but the number of times the letter is repeated also affects how successful a player is at guessing the word. Therefore, we counted these two attributes of the letters in words in the report as their characteristics.

<!-- b000184 | caption | pages [7] -->
Table 5: Alphabetic properties

<!-- b000185 | prose | pages [7] -->
Word Number of duplicate Maximum number of repeats Word Number of duplicate Maximum number of repeats cross 1 2 exist 0 0 glass 1 2 apply 1 0

<!-- b000186 | furniture | pages [7] -->
6

<!-- b000187 | furniture | pages [8] -->
Team # 2314151

<!-- b000188 | furniture | pages [8] -->
Page 7 of 24

<!-- b000189 | heading | pages [8] -->
4 Task 1

<!-- b000190 | heading | pages [8] -->
4.1 Prophet algorithm

<!-- b000191 | heading | pages [8] -->
4.1.1 Background of the algorithm

<!-- b000192 | prose | pages [8] -->
Although neural network models have become increasingly popular in recent years, this model usually requires a large amount of data for training. A dataset with only 400 or so data is not a good place to consider a neural network model.

<!-- b000193 | prose | pages [8] -->
On balance, we decided to use the Prophet model, an algorithm based on an additive model for predicting time series data with characteristics such as seasonality, trends, and holidays. Also, Prophet[4] has strong robustness to handle problems such as non-stationary time series and outliers. For this dataset, Prophet is a good choice.

<!-- b000194 | heading | pages [8] -->
4.1.2 Prediction model building based on Prophet algorithm

<!-- b000195 | heading | pages [8] -->
1. Prophet algorithm principle

<!-- b000196 | prose | pages [8] -->
The principle of Prophet algorithm is as follows:

<!-- b000197 | prose | pages [8] -->
y(t) = g(t) + s(t) + h(t) + ϵ (2)

<!-- b000198 | prose | pages [8] -->
g(t) denotes the trend term, which represents the time series trend over the non-period. s(t) denotes the period term, which is generally measured in weeks or years. h(t) denotes the holiday term, which represents the effect of those potential non-periodic holidays in the time series on the predicted values. ϵ denotes the error term or residual term, which indicates the fluctuations not predicted by the model, and ϵ follows a Gaussian distribution.

<!-- b000199 | prose | pages [8] -->
The Prophet algorithm models each of the model’s three components and then combines them to generate the forecast data.

<!-- b000200 | heading | pages [8] -->
2. Trend term model

<!-- b000201 | prose | pages [8] -->
Prophet’s implementation of the trend part applies two main models, one is the saturated growth model, and the other is the segmented linear model.

<!-- b000202 | prose | pages [8] -->
• Saturation growth model The saturation growth model, also known as the logistic growth model, is a model used to describe a system in which the growth rate gradually decreases and eventually stabilizes.

<!-- b000203 | prose | pages [8] -->
C(t) g(t) = (3) 1 + exp(−(k + a(t)Tδ) · (t −(m + a(t)Tγ)))

<!-- b000204 | prose | pages [8] -->
C(t) denotes the carrying capacity, a time function limiting the maximum value that can be grown. k denotes the growth rate.

<!-- b000205 | prose | pages [8] -->
• Segmented growth model

<!-- b000206 | prose | pages [8, 9] -->
g(t) = (k + a(t)Tδ) · t + (m + a(t)Tγ) (4) It is worth noting that the most significant difference between the segmented linear function and the logistic regression function is that the setting of y is different in the segmented linear function.

<!-- b000207 | furniture | pages [8] -->
7

<!-- b000208 | furniture | pages [9] -->
Team # 2314151

<!-- b000209 | furniture | pages [9] -->
Page 8 of 24

<!-- b000211 | prose | pages [9] -->
γj=−sjδj (5)

<!-- b000212 | prose | pages [9] -->
The model defines the points corresponding to changes in the growth rate k, called n changepoints. changeepoint prior scale is defined as the flexibility of the growth trend model.

<!-- b000213 | heading | pages [9] -->
3. Seasonality trends model

<!-- b000214 | prose | pages [9] -->
Since a time series may contain seasonal trends with multiple days, weeks, months, years, and other cycle types, the Fourier scale can be used to approximate this cycle property. The Fourier series is shown as follows.

<!-- b000215 | prose | pages [9] -->
N (ancos(2πnt ) + bnsin(2πnt X s(t) = )) (6) P P n=1

<!-- b000216 | prose | pages [9] -->
N denotes the number of periods one wishes to use in the model. Larger values of N allow for more complex seasonal functions to be fitted. However, they also introduce more overfitting problems.

<!-- b000217 | heading | pages [9] -->
4. Holiday effect model

<!-- b000218 | prose | pages [9] -->
In the natural environment, holidays can significantly impact the time series. Each holiday is not always the same, so the effects of different holidays at different points in time are treated as independent models. For the ith holiday, Di denotes the period before and after the holiday.

<!-- b000219 | prose | pages [9] -->
In order to represent the holiday effect, a corresponding indicator function is needed, and a parameter κi is needed to represent the range of the holiday effect.

<!-- b000220 | prose | pages [9] -->
Assuming that there are L holidays, the holiday effect model is:

<!-- b000221 | prose | pages [9] -->
L X κi · 1{t∈Di} h(t) = Z(t)κ = (7) i=1

<!-- b000222 | prose | pages [9] -->
Z(t) = (1{t∈D1}, · · · , 1{t∈DL}) and κ = (κ1, · · · , κL)T

<!-- b000223 | heading | pages [9] -->
4.1.3 Parameter setting

<!-- b000224 | prose | pages [9] -->
We choose a trend term based on a segmented linear function for the trend term model. We set n changepoints to 25 and changepoint prior scale to 0.05. For seasonal trends, we set season- ality prior scale to 10. For holiday effects, we set holidays prior scale to 10. In addition, we set interval width to 0.80, mcmc samples to 0, and uncertainty samples to 1000.

<!-- b000225 | furniture | pages [9] -->
8

<!-- b000226 | furniture | pages [10] -->
Team # 2314151

<!-- b000227 | furniture | pages [10] -->
Page 9 of 24

<!-- b000228 | heading | pages [10] -->
4.1.4 Result

<!-- b000229 | prose | pages [10] -->
We set up the model using the parameter values shown in Figure a. When selecting a data range, it is usually necessary to consider the order of magnitude of the data. The reason for taking data starting from the same order of magnitude is to avoid the effects of data bias and errors and to ensure the accuracy and reliability of the data. Therefore, we screened the original data and selected data from after May 5, 2022. The final results we obtained are as follows.

<!-- b000230 | caption | pages [10] -->
Table 6: Predicted results

<!-- b000231 | prose | pages [10] -->
ds yhat yhat lower yhat upper

<!-- b000232 | prose | pages [10] -->
2023-03-01 14425.58926 10355.27753 18741.54302

<!-- b000233 | prose | pages [10] -->
The model predicts a range of 10355 to 18742 for the number of reports on March 1, 2023.

<!-- b000234 | prose | pages [10] -->
(a) Prediction Chart (b) Weekly Trend Chart

<!-- b000235 | caption | pages [10] -->
Figure 4: Forecast and trend charts

<!-- b000236 | prose | pages [10] -->
The graph above shows the time series trend and weekly seasonality. Figure a shows the general trend in the number of reports and the future forecast. From May 5, 2022, the number of reports decreases, and the decrease rate gradually becomes smaller. In addition, it predicts the report number interval for seventy days after January 1, 2023.

<!-- b000237 | prose | pages [10] -->
Figure b shows the weekly cyclical pattern, with significantly more people playing Wordle on Wednesdays. The number of weekend reports tends to be lower.

<!-- b000238 | heading | pages [10] -->
4.2 Higher-order partial correlation analysis model

<!-- b000239 | heading | pages [10] -->
4.2.1 Correlation analysis using Pearson’s correlation coefficient

<!-- b000240 | prose | pages [10, 11] -->
The problem to be solved in this model is to perform a correlation analysis between the attributes of the words and the percentage of difficulty patterns separately. The attributes of the words have been classified in the data processing, but after analyzing the data of this question, we find a strong correlation between the attributes of the words. Therefore, we first conducted correlation tests for each variable to examine the Pearson correlation coefficients of each attribute with the percentage of difficulty patterns without controlling for other variables:

<!-- b000241 | furniture | pages [10] -->
9

<!-- b000242 | furniture | pages [11] -->
Team # 2314151

<!-- b000243 | furniture | pages [11] -->
Page 10 of 24

<!-- b000245 | caption | pages [11] -->
Table 7: Pearson correlation coefficient distribution

<!-- b000246 | prose | pages [11] -->
Attributes of words R P

<!-- b000247 | prose | pages [11] -->
Number of vowels 0.083460383 0.093068989 Number of vowels(non-repetition) 0.05075013 0.307685109 Number of consonants -0.083460383 0.093068989 Number of consonants(non-repetition) -0.106284281 0.032271311 Word commonness 0.094056604 0.058285504 The sum of the frequencies of letters 0.008176597 0.869535404

<!-- b000248 | prose | pages [11] -->
From the above table, we can see that the p-values of the significance tests for the correlation tests of each attribute and percent hard are almost all weakly correlated, and only the total ranking of word frequency of letters in words is strongly correlated. This result is not satisfactory. We analyzed the attributes of the words again and find that there is a strong correlation between these attributes, and the influence between the attributes cannot be ignored. To sum up, we chose the algorithm of higher-order biased correlation analysis to do correlation analysis on the percentage of each attribute in the word with the difficulty pattern to solve this problem[5].

<!-- b000249 | heading | pages [11] -->
4.2.2 Establishment of Higher-order partial correlation analysis model

<!-- b000250 | prose | pages [11] -->
(1) First-order partial correlation coefficient: The partial correlation coefficient of any two of the three variables is calculated after excluding the effect of the remaining one variable and is called the first-order partial correlation coefficient with the following formula:

<!-- b000251 | prose | pages [11] -->
rij −rihrjh rij·h = (8) q    (1 −r2 1 −r2 ih) jh

<!-- b000252 | prose | pages [11] -->
In this equation, rij is the simple correlation coefficient between variables xi and xj, rih is the simple correlation coefficient between variables xi and xh, and rjh is the simple correlation coefficient between variables xj and xh.

<!-- b000253 | prose | pages [11] -->
(2) High-order partial correlation coefficient: Generally, if there are k (k > 2) variables x1, x2, ..., xk, then the formula of partial correlation coefficient of samples of order g (g ≤k-2) for any two variables xi and xj is:

<!-- b000254 | prose | pages [11] -->
rij·l1l2···lg = rij·l1l2···lg−1 −rilg·l1l2···lg−1rjlg·l1l2···lg−1 (9) q (1 −r2 ilg·l1l2···lg−1)(1 −r2 jlg·l1l2···lg−1)

<!-- b000255 | prose | pages [11] -->
where the right-hand sides are all partial correlation coefficients of order g-1.

<!-- b000256 | furniture | pages [11] -->
10

<!-- b000257 | furniture | pages [12] -->
Team # 2314151

<!-- b000258 | furniture | pages [12] -->
Page 11 of 24

<!-- b000259 | heading | pages [12] -->
4.2.3 Analysis of results

<!-- b000260 | prose | pages [12] -->
In the higher-order partial correlation analysis, we need to control for irrelevant variables as a way to eliminate the influence of other variables on the studied variables. The results are as follows:

<!-- b000261 | caption | pages [12] -->
Table 8: Distribution of high-order bias correlation results

<!-- b000262 | prose | pages [12] -->
Attributes of words High-order partial correlation coefficient P

<!-- b000263 | prose | pages [12] -->
Number of vowels -0.319578 4.37009E-11 Number of vowels(non-repetition) -0.271561 2.72256E-08 Number of consonants 0.319578 4.37009E-11 Number of consonants(non-repetition) 0.306104 3.00056E-10 Word commonness -0.080926 0.103481297 The sum of the frequencies of letters -0.133207 0.007197084

<!-- b000264 | prose | pages [12] -->
As shown in the above table, the P-values corresponding to the attributes of the above six words are much less than 0.05. Therefore, the results can be considered statistically significant.

<!-- b000265 | prose | pages [12] -->
In general, the higher-order partial correlation coefficient, after taking the absolute value, is no correlation when it is 0-0.09, weak correlation when it is 0.1-0.3, moderate correlation when it is 0.3-0.5, and strong correlation when it is 0.5-1.0.

<!-- b000266 | caption | pages [12] -->
Figure 5: Heat map of high-order partial correlations of word attributes with percent hard

<!-- b000267 | prose | pages [12] -->
By analyzing the data as well as the results of the heat map, we obtained the following correlations of word attributes with the percentage of hard modes:

<!-- b000268 | caption | pages [12] -->
Table 9: Word attribute correlation result distribution

<!-- b000269 | prose | pages [12] -->
Attributes of words Degree of correlation

<!-- b000270 | prose | pages [12] -->
Number of vowels Moderate negative correlation Number of vowels(non-repetition) Weak negative correlation Number of consonants Moderate positive correlation Number of consonants(non-repetition) Moderate positive correlation Word commonness No correlation The sum of the frequencies of letters Weak negative correlation

<!-- b000271 | furniture | pages [12] -->
11

<!-- b000272 | furniture | pages [13] -->
Team # 2314151

<!-- b000273 | furniture | pages [13] -->
Page 12 of 24

<!-- b000274 | heading | pages [13] -->
5 Task 2

<!-- b000275 | heading | pages [13] -->
5.1 Multi-objective regression prediction framework

<!-- b000276 | prose | pages [13] -->
In this part, we need to address a prediction problem where the model we build can predict the percentage of user engagement related to the Wordle puzzle at a future date. We currently have user report data for Wordle during the past year, where we divide the words per day into several relevant attributes and take into account the effect of time of day, as users complete the game differently on weekends and weekdays.

<!-- b000277 | prose | pages [13] -->
Since the amount of data given in the question is very small, we give up using neural network to predict it, and instead use an optimized multi-objective regression prediction framework[6] to process it.

<!-- b000278 | prose | pages [13] -->
The specific process of using a multi-objective regression prediction framework to solve a forecast- ing problem is as follows:

<!-- b000279 | caption | pages [13] -->
Figure 6: Operational process of multi-objective regression prediction framework

<!-- b000280 | prose | pages [13] -->
Our framework currently supports partial least squares regression algorithms, Bayesian linear regression-based hyperparameter tuning and feature selection algorithms, elastic network regression models, LASSO regression algorithm models, ridge regression algorithms, and high-performance quantile regression algorithms models. All these regression models can perform well for small data while being able to handle multiple classification tasks and suitable for incremental training. In addition, their well-adaptive ability, self-learning ability, and generalization ability also meet our requirements.

<!-- b000281 | furniture | pages [13] -->
12

<!-- b000282 | furniture | pages [14] -->
Team # 2314151

<!-- b000283 | furniture | pages [14] -->
Page 13 of 24

<!-- b000284 | caption | pages [14] -->
Figure 7: Algorithm integrated evaluation analysis framework

<!-- b000285 | heading | pages [14] -->
5.2 Establishment of prediction model

<!-- b000286 | prose | pages [14] -->
(1) Establishment of a multi-objective regression prediction framework The multi-objective regression prediction framework divides the data into training and test sets and normalizes the data. It identifies the optimal parameters by grid search and evaluates the accuracy of the model based on the mean of the mean squared error, which in turn determines the best algorithmic model[7]. Then, the multi-objective regression prediction framework uses the best algorithm to make predictions on the data and returns the data at the original scale of inverse normalization. For our dataset, the output of the evaluation function-based algorithm evaluation framework is as shown below:

<!-- b000287 | caption | pages [14] -->
Figure 8: Output of a multi-objective regression prediction framework based on an evaluation function

<!-- b000288 | furniture | pages [14] -->
13

<!-- b000289 | furniture | pages [15] -->
Team # 2314151

<!-- b000290 | furniture | pages [15] -->
Page 14 of 24

<!-- b000291 | prose | pages [15] -->
From the output of the above figure, we can find that the root mean square error of the LASSO regression algorithm is the smallest, and the total average root mean square error of its multiple repeated fits is only 0.8, which can show that our regression model can predict the data very well.

<!-- b000292 | heading | pages [15] -->
(2) Establishment of Lasso Regression Model

<!-- b000293 | prose | pages [15] -->
Lasso regression (LASSO, least absolute shrinkage and selection operator) is the addition of a penalty term of L1 parity to the residuals tiling and minimization:

<!-- b000294 | prose | pages [15] -->
k (yi −ˆyi)2 + λ ˆβu i + λ||ˆβ∥1 = min X X X e2 min (10) u=1

<!-- b000295 | prose | pages [15] -->
Because the L1 parametrization is in the form of an absolute value, it is not derivable at the zero point. Thus, it no longer has an analytic solution and can be solved using gradient descent (to be precise, a subgradient algorithm). Ridge regression cannot eliminate variables. The excellent property of LASSO regression is that it can produce sparsity, which can reduce some insignificant regression coefficients to zero for the purpose of eliminating variables.Its loss function is:

<!-- b000296 | prose | pages [15] -->
m n 1 (ˆyi −yi)2 + α X X ∥wi∥ J(w, b) = 2margmin (11) w,b i=1 i=1

<!-- b000297 | heading | pages [15] -->
5.3 Word prediction - EERIE

<!-- b000298 | prose | pages [15] -->
First, the word EERIE can be attributed using the feature engineering established above. The relevant attributes of the word EERIE are as follows.

<!-- b000299 | caption | pages [15] -->
Table 10: Relevant attributes of the word EERIE

<!-- b000300 | prose | pages [15] -->
Date Number of vowels Number of vowels (non-repetition) 01/03/23 4 2 Word Number of consonant Word commonness EERIE 1 224 Contest number Number of consonant (non-repetition) The sum of the frequencies of letters 620 1 27903

<!-- b000301 | prose | pages [15] -->
After the above multi-objective regression prediction framework, we identified a modified Lasso regression model to achieve the prediction of the percentage of word relevance at a given date. We performed Lasso regression prediction for the word EERIE to predict its reported percentage on March 1, 2023. We take the average of multiple fits as the final prediction to make the results more accurate.

<!-- b000302 | caption | pages [15] -->
Table 11: Precise results-EERIE

<!-- b000303 | prose | pages [15, 16] -->
1 try 2 tries 3 tries 4 tries 5 tries 6 tries 7 or more tries (X) 0.023996469 3.60053273 16.9184627 33.8665962 30.5875392 12.9104259 2.09258948 Finally, the predicted percentage result was rounded, and the final predicted result was obtained:

<!-- b000304 | furniture | pages [15] -->
14

<!-- b000305 | furniture | pages [16] -->
Team # 2314151

<!-- b000306 | furniture | pages [16] -->
Page 15 of 24

<!-- b000308 | caption | pages [16] -->
Table 12: Final Results-EERIE

<!-- b000309 | prose | pages [16] -->
Date Contest number Word 1 try 2 tries 3 tries 4 tries 5 tries 6 tries 7 or more tries (X) 01/03/23 620 EERIE 0 4 17 34 30 13 2

<!-- b000310 | heading | pages [16] -->
5.4 Feature influence degree analysis

<!-- b000311 | prose | pages [16] -->
In order to get the word attributes that have a more significant influence on our prediction model, we propose an analysis based on Permutation Importance.

<!-- b000312 | prose | pages [16] -->
First, we obtain a trained Lasso model. Next, we disrupt the values of a certain column of data and then predict the obtained dataset. The predicted values are used with the true target values to calculate how much the loss function has been elevated due to random sorting. The amount of decay in the model performance represents the importance of the disordered column. Then, we recover the disordered column and repeat the previous operation on the next column of data until the importance of each column is calculated.

<!-- b000313 | prose | pages [16] -->
To make the results more general, we run the analysis three times to analyze the scores of different attributes and summarize the final fit results in the following figures, which help us to analyze the degree of influence of different attributes in the words on the model.

<!-- b000314 | caption | pages [16] -->
Figure 10: Heat map of the features importance of

<!-- b000315 | prose | pages [16] -->
the seven attributes of words

<!-- b000316 | caption | pages [16] -->
Figure 9: Feature importance score Lasso

<!-- b000317 | prose | pages [16] -->
In our model, we observed a strong correlation between the two attributes of the number of conso- nants (excluding repeated consonants) and the number of vowels (excluding repeated vowels) in words. Also, we found a moderate correlation between the sum of the frequencies of all letter occurrences in words, the number of consonants, and the number of vowels. In contrast, the correlations between word commonness and date were weaker.

<!-- b000318 | heading | pages [16] -->
5.5 Model reliability analysis

<!-- b000319 | prose | pages [16, 17] -->
To evaluate the reliability of our prediction model, we used two methods. First, we calculated the root mean square error of the model prediction results to measure the deviation of the prediction results from the actual data. Second, we used the prediction model to forecast the given data and then compared the forecast with the actual data to assess the accuracy of the prediction results.

<!-- b000320 | furniture | pages [16] -->
15

<!-- b000321 | furniture | pages [17] -->
Team # 2314151

<!-- b000322 | furniture | pages [17] -->
Page 16 of 24

<!-- b000324 | prose | pages [17] -->
The root means square error is obtained by calculating the sum of squares of the deviations between the predicted and actual values divided by the ratio of the number of observations n and then taking the square root. The formula for the root mean square error is as follows.

<!-- b000325 | prose | pages [17] -->
r 1 X (yi −yihat)2 n · RMSE = (12)

<!-- b000326 | prose | pages [17] -->
Where n is the number of samples, yi is the actual value of the ith sample, and yihat is the predicted value of the ith sample. The units of RMSE are the same as those of the target variable. We fit and graphically analyze the fitted lasso regression model results for the root mean square error.

<!-- b000327 | prose | pages [17] -->
According to the output plot of the lasso regression in Figure 7, we found that the RMSE of the three solutions did not exceed 0.85, and the average RMSE was 0.8. Generally speaking, the prediction accuracy is considered high when the RMSE does not exceed 2.

<!-- b000328 | prose | pages [17] -->
Here is an example of a graph comparing the degree of the trend of 5 successful guesses of words:

<!-- b000329 | caption | pages [17] -->
Figure 11: Comparison of the degree of the trend of 5 successful guesses of words

<!-- b000330 | prose | pages [17] -->
The blue curve is the percentage of 5 successes for the original data. In comparison, the orange curve is the percentage of 5 successes predicted by our prediction model, and it can be seen that the deviation of its prediction results is in the acceptable range.

<!-- b000331 | heading | pages [17] -->
6 Task 3

<!-- b000332 | prose | pages [17] -->
We think that the ”average number of tries” can represent the difficulty level of a word, but since the data set given in the question is too small, it would affect the performance of the clustering analysis. Therefore, we re-fit the framework of the Task 2 to the distribution of tries for the 12,974 words in the prediction dictionary after removing the time variable, and use this distribution to find the average number of tries. Following this, the average number of tries is clustered using K-means clustering[8].

<!-- b000333 | furniture | pages [17] -->
16

<!-- b000334 | furniture | pages [18] -->
Team # 2314151

<!-- b000335 | furniture | pages [18] -->
Page 17 of 24

<!-- b000336 | heading | pages [18] -->
6.1 K-means clustering algorithm

<!-- b000337 | prose | pages [18] -->
The K-means algorithm measures the similarity of different data objects by selecting a suitable distance formula[9]. The distance between data is inversely proportional to the similarity, i.e., the smaller the similarity, the larger the distance. K-means algorithm first needs to specify the initial number of clusters k and the corresponding initial cluster center C randomly from the given data objects, and calculate the distance from the initial cluster center to the rest of the data objects[10]. In this paper, we choose Euclidean distance. The Euclidean distance formula from the cluster center to other data objects in the space is:

<!-- b000338 | prose | pages [18] -->
v m u X (xj −Cij)2 u d (x, Ci) = (13) t j=1

<!-- b000339 | prose | pages [18] -->
where x is the data object, Ci is the i-th cluster center, m is the dimension of the data object, and xj, Cij are the attribute values of the j-th dimension of the data object x and the cluster center Ci.

<!-- b000340 | prose | pages [18] -->
According to the Euclidean distance measure of similarity, the target data with the highest similarity to the clustering center are assigned to the clusters of Ci. And then the data objects in k clusters are averaged to form a new round of clustering centers. The calculation formula is:

<!-- b000341 | prose | pages [18] -->
k X X |d (x, Ci)|2 SSE = (14) i=1 x∈Ci

<!-- b000342 | heading | pages [18] -->
6.2 Selection of parameters

<!-- b000343 | prose | pages [18] -->
• Silhouette Coefficient method: This method evaluates the clustering quality by calculating the silhouette coefficients of each sample point. Where the silhouette coefficient integrates the magnitude of intra-cluster distance and inter-cluster distance and takes a value between [-1,1], the closer to 1 means the better clustering effect.

<!-- b000344 | prose | pages [18] -->
• Davies-Bouldin index (abbreviated as DBI) method: This method evaluates the quality of clustering by calculating the ratio of the average distance of all points within each cluster to the cluster center and the shortest distance between different cluster centers.

<!-- b000345 | prose | pages [18] -->
After analysis, we classified the words into 3-5 categories based on difficulty, with the following parameters:

<!-- b000346 | caption | pages [18] -->
Table 13: Parameters

<!-- b000347 | prose | pages [18] -->
Number of clusters Silhouette Coefficient DBI

<!-- b000348 | prose | pages [18] -->
3 0.545003549 0.562683379 4 0.536022115 0.561324728 5 0.523517926 0.558397471

<!-- b000349 | prose | pages [18] -->
As illustrated in the table above, both Silhouette Coefficient and DBI are decreasing slightly as the number of clusters increases. To improve the accuracy of identifying word difficulty, we choose to cluster into 3 classes.

<!-- b000350 | furniture | pages [18] -->
17

<!-- b000351 | furniture | pages [19] -->
Team # 2314151

<!-- b000352 | furniture | pages [19] -->
Page 18 of 24

<!-- b000353 | heading | pages [19] -->
6.3 Clustering results

<!-- b000354 | prose | pages [19] -->
Based on the above analysis, we selected the K-means algorithm for clustering the data set into three classes and obtained the following clustering results.

<!-- b000355 | prose | pages [19] -->
Aggregate results:

<!-- b000356 | caption | pages [19] -->
Table 14: Aggregate results

<!-- b000357 | prose | pages [19] -->
Number of duplicate Maximum of repeats Number of vowels Number of vowels(non-repetition) Times 0 0.519623 0.63264 1.859318 1.546858 0.000002 1 0.019896 0.023617 1.77483 1.759786 0.000009 2 1.210897 1.182715 1.748239 1.354157 0.000001 Rank time Weighted sums Number of consonants Number of consonants(non-repetition) 0 18842.21231 423.226591 3.140682 2.933519 1 20294.22727 403.383609 3.22517 3.220317 2 16888.876 451.443208 3.251761 2.434946

<!-- b000358 | prose | pages [19] -->
Difficulty interval division:

<!-- b000359 | caption | pages [19] -->
Figure 12: Word difficulty interval

<!-- b000360 | prose | pages [19] -->
Analysis of the results shows that Number of duplicates, Maximum of repeats, Prevalence, and Frequency vary widely in different classifications. According to the quartile method, the normal value is generally defined as greater than QL −kIQR or less than QU + kIQR. Here, we k take 0.5, and the specific difficulty interval is shown below.

<!-- b000361 | caption | pages [19] -->
Table 15: Specific difficulty interv

<!-- b000362 | prose | pages [19] -->
Number of duplicate Maximum of repeats Normality Frequency easy (0, 0) (0, 0) (0.000009, 0.002044) (16767.75, 33314) mid (0, 1) (0, 2) (0.000003, 0.000012) (14969.25, 29574.25) hard (1, 3) (0, 2) (0, 0.000004) (6568, 28380.5)

<!-- b000363 | heading | pages [19] -->
6.4 Word interval identification - EERIE

<!-- b000364 | prose | pages [19] -->
’EERIE’ belongs to the difficulty interval.

<!-- b000365 | furniture | pages [19] -->
18

<!-- b000366 | furniture | pages [20] -->
Team # 2314151

<!-- b000367 | furniture | pages [20] -->
Page 19 of 24

<!-- b000368 | prose | pages [20] -->
We bring the word ’EERIE’ into the Lasso regression prediction model built in Part 2 and get its average number of attempts 4.384952125887, which means it belongs to the difficult word. It is easy to find that its attributes of Number of duplicate, Maximum of repeats, Normality, and Frequency are all in the difficult range we have classified. Therefore, we believe that the word ’EERIE’ belongs to the difficult interval.

<!-- b000369 | heading | pages [20] -->
6.5 Model reliability analysis

<!-- b000370 | prose | pages [20] -->
In order to evaluate the accuracy of our classification model, we used 405 data from January 7, 2022, to February 16, 2023, that had been identified for validation. The validation process was as follows.

<!-- b000371 | prose | pages [20] -->
First, we calculated the average number of guesses for each word. We classified the average number of word guesses into different intervals based on the clustering results described in the previous section. Then, we counted each attribute of each letter to compare which level of difficulty interval was hit for each attribute. The difficulty with the highest number of hits is the difficulty identified by the feature. If the classification result is the same as the result of the word hit interval, our model is considered accurate. The algorithm is implemented as follows:

<!-- b000372 | prose | pages [20] -->
The accuracy of our model is calculated to be 91. 3649025%. For small-scale data classification, our model has high accuracy.

<!-- b000373 | furniture | pages [20] -->
19

<!-- b000374 | furniture | pages [21] -->
Team # 2314151

<!-- b000375 | furniture | pages [21] -->
Page 20 of 24

<!-- b000376 | heading | pages [21] -->
7 Interesting aspects of the data

<!-- b000377 | prose | pages [21] -->
• The relationship between the number of reported results and the percentage of scores reported in Hard Mode

<!-- b000378 | prose | pages [21] -->
We try to find some other interesting features of this dataset, but we do not know where to start. So we search Wordle on social media to get a specific view of this game. During this period, we suddenly found that most of the reported results about this game were from the first half of 2022, while in the second half of the year, this game saw a significant drop in popularity. Accordingly, we associate and plot the relationship among the number of reports from players, the percentage of scores reported in Hard Mode, and the date. Because the difference between the percentage in Hard Mode and the number of reported results is too large, we multiply the value of the percentage of scores reported in Hard Mode by 106 in order to make the relationship graph more obvious.

<!-- b000379 | caption | pages [21] -->
Figure 13: Hard mode percentage vs. Date vs. Num of reported

<!-- b000380 | prose | pages [21] -->
From the graph above we discover that as the number of reported results began to grow, the percentage in hard mode steadily increased. However, when the number of reported results peaked, the percentage in hard mode plummeted. We suppose that there was an influx of new players who were less familiar with Wordle and less likely to try the hard mode, which caused the percentage of hard mode to plummet. Over time, the number of daily reported results for Wordle has gradually decreased, but the percentage of hard modes has steadily increased. In response, we think Wordle has a loyal fan base that often plays Wordle and prefers hard mode. This indicates that the gaming ability of the enthusiastic fans is also slowly improving, and it also shows that this game helps to improve players’ English skills.

<!-- b000381 | prose | pages [21] -->
• The relationship among the average number of successes, number of reported results, and date for Wordle

<!-- b000382 | prose | pages [21] -->
Next, we analyze the relationship between the average number of successes, the total number of reports, and the date of Wordle. To make the scatter plot more visible, we multiplied the value of Average number of successes by 105.

<!-- b000383 | furniture | pages [21] -->
20

<!-- b000384 | furniture | pages [22] -->
Team # 2314151

<!-- b000385 | furniture | pages [22] -->
Page 21 of 24

<!-- b000386 | caption | pages [22] -->
Figure 14: Average number of successes vs. Date vs. Num of reported

<!-- b000387 | prose | pages [22] -->
As shown in the figure, the values of Average number of successes are mostly distributed between 4 and 5. This shows that the difficulty of the game remains almost constant, with almost every word being guessed 4-5 times. This supports our previous interesting finding that the game helps to improve players’ English and that the longer they play the game, the more willing they are to try the Hard Mode.

<!-- b000388 | heading | pages [22] -->
8 Sensitivity Analysis

<!-- b000389 | prose | pages [22] -->
In Part two, we artificially specify the proportion of the test set(POT) as 20%, and the change of this value will affect the model’s training. The results of the sensitivity analysis are shown in Table 7.

<!-- b000390 | caption | pages [22] -->
Table 16: Sensitivity analysis

<!-- b000391 | prose | pages [22] -->
POT =0.2 POT =0.1 POT =0.15 POT =0.25 POT =0.3 0.87(1.16% ↑) 0.93(8.14% ↑) 0.89(3.49% ↑) 0.97(12.79% ↑) Partial least squares Regression 0.86 0.94(2.08% ↓) 0.95(1.04% ↓) 0.92(4.17% ↓) 0.91(5.21% ↓) Elastic Net Regression 0.96 0.97(3.19% ↑) 1.01(7.45% ↑) 0.89(5.32% ↓) 0.96(2.13% ↑) Bayesian linear regression 0.94 0.83(3.75% ↑) 0.84(5.00% ↑) 0.86(7.50% ↑) 0.92(15.00% ↑) Lasso Regression 0.80 0.91(7.14% ↓) 0.93(5.10% ↓) 0.93(5.10% ↓) 0.92(6.12% ↓) Ridge regression 0.98 0.92(3.37% ↑) 0.82(7.87% ↓) 0.90(1.12% ↑) 1.05(17.98% ↑) Quantile regression 0.89

<!-- b000392 | prose | pages [22] -->
As shown in the results, by changing the proportion of the test set, the maximum rate of change is 10%, while the RMSE of the models are all less than 1.0, which proves that our model is not sensitive to the change of this parameter within the range of 0.5 times itself, and our model is robust and reliable.

<!-- b000393 | furniture | pages [22] -->
21

<!-- b000394 | furniture | pages [23] -->
Team # 2314151

<!-- b000395 | furniture | pages [23] -->
Page 22 of 24

<!-- b000396 | heading | pages [23] -->
9 Strengths and Weaknesses

<!-- b000397 | heading | pages [23] -->
9.1 Strength

<!-- b000398 | prose | pages [23] -->
• Prophet model provides excellent predictions for small data sets and adjusts the parameters quite freely, thus facilitating more accurate predictions of the number of reports we will have for future dates.

<!-- b000399 | prose | pages [23] -->
• Higher-order partial correlation analysis can control irrelevant variables for correlation analysis of a variable, which facilitates us to eliminate the influence between words and more accurately analyze the degree of influence of variables.

<!-- b000400 | prose | pages [23] -->
• Lasso regression model can perform well on small data while handling multiple classification tasks and being suitable for incremental training to make more accurate regression predictions on small data sets.

<!-- b000401 | prose | pages [23] -->
• Permutation importance can perform data disruption and rearrangement analysis on the fitted model to more accurately derive the contribution of each piece of data.

<!-- b000402 | heading | pages [23] -->
9.2 Weakness

<!-- b000403 | prose | pages [23] -->
• Multi-objective regression prediction runs long, and the solution results need simple manual screening.

<!-- b000404 | heading | pages [23] -->
10 Letter

<!-- b000405 | prose | pages [23] -->
To: Puzzle Editor of the New York Times From: Team 2314151 Date: February 20, 2023

<!-- b000406 | heading | pages [23] -->
Subject: The results of our team

<!-- b000407 | prose | pages [23] -->
Dear Puzzle Editor of the New York Times, By building several models, we have completed an analysis of MCM’s statistics based on players’ participation in the Wordle puzzles that your website provides daily. We are honored to present you with the results of what we’ve analyzed.

<!-- b000408 | prose | pages [23] -->
Before building the model, we clarified and normalized the dataset you gave us and identified word attributes such as the number of repeated letters, number of vowel letters, number of consonant letters, commonness, and frequency. Next, I will describe the modeling solution process for you:

<!-- b000409 | prose | pages [23] -->
First, we considered the effects of trends, seasonality, and holidays and built a prophet-based time- series forecasting model to explain the daily variation in the number of reports and to predict the interval of the number of reported outcomes on March 1, 2023: [10355,18742]. We found that the number of reported outcomes increased steeply from January to early February 2022 and that the number of reports tended to be highest on Wednesdays and lowest on weekends during the week in terms of the variation in the number of reports.

<!-- b000410 | prose | pages [23, 24] -->
In exploring the influence of the attributes of the words on the reports, we first used a correla- tion analysis algorithm to solve for each attribute, however, we found that their Pearson correlation coefficients were all less than or approximately 0.1 and were uncorrelated. In order to overcome this association, we used a higher-order partial correlation analysis algorithm to perform correlation analy- sis on each attribute of the word while controlling for the interaction between the attributes of the word, and finally obtained the results we wanted: the number of vowel letters, the number of non-repeats, and the word commonness were negatively correlated, and the number of consonant letters and the number of non-repeats numbers is positively correlated.

<!-- b000411 | furniture | pages [23] -->
22

<!-- b000412 | furniture | pages [24] -->
Team # 2314151

<!-- b000413 | furniture | pages [24] -->
Page 23 of 24

<!-- b000415 | prose | pages [24] -->
Next, an optimized multi-objective regression prediction framework was developed to explore the effect of word attributes on the distribution of reported results. By feeding the data into the framework, a prediction model was selected that was most suitable for this dataset: the Lasso regression prediction model, which performed very well for the test set with a root mean square error of 0.8. Therefore, we established the Lasso regression prediction model to predict the reported results, and we first processed ’EERIE ’, the results of its attempt count distribution were obtained as (0, 4, 17, 34, 30, 13, 2).

<!-- b000416 | prose | pages [24] -->
Following this, we proposed an algorithm for ranking importance analysis to evaluate the established but this attribute, and finally found that the three attributes of number of consonant letters, number of vowel letters and frequency had a greater impact on the distribution of reported results with impact factors of 4.226, 3.993, and 1.253, respectively.

<!-- b000417 | prose | pages [24] -->
Then, we used the established Lasso regression prediction model to distribute the reported results for all 5-letter words in the dictionary database, and then used the K-Means algorithm to classify the above results into three categories of difficulty: high (≥4.37) medium (4.13-4.37) low (< 4.13), and found that Number of duplicate, Maximum of repeats, Prevalence, and Frequency were found to differ significantly in different classifications, and the intervals for each attribute were divided.

<!-- b000418 | prose | pages [24] -->
Then we bring ’EERIE’ into the interval division model, and since all its attributes hit the interval value of difficulty, its degree of being guessed is difficult, and its average number of attempts matches the difficulty interval division predicted using the Lasso regression model. Therefore, the degree of ’EERIE’ being guessed is difficult. Meanwhile, we obtained the accuracy of our model by matching the attribute intervals for different difficulty words, which is 91.36%, and we can see that our model is robust.

<!-- b000419 | prose | pages [24] -->
Finally, we performed a sensitivity analysis of the model, as shown in the results, by changing the proportion of the test set, the maximum rate of change is 10%, while the RMSE of the models are all less than 1.0, which proves that our model is not sensitive to the change of this parameter within the range of 0.5 times itself, and our model is robust and reliable. In addition, the study of the data set has revealed the declining popularity of Wordle and the increasing proportion of difficult mode challenges, and offers two suggestions for restoring the popularity of the game:

<!-- b000420 | prose | pages [24] -->
• Introduced online multiplayer challenge mode, you can invite friends to challenge together, so as to attract more people to participate.

<!-- b000421 | prose | pages [24] -->
• Introducing Kids Mode, parents can let their children use this software to work on their English skills, playing and learning at the same time.

<!-- b000422 | prose | pages [24] -->
So that’s the summary of our research. We sincerely hope that it can provide you with useful information and look forward to your reply. Thank you!

<!-- b000423 | prose | pages [24] -->
Yours sincerely,

<!-- b000424 | furniture | pages [24] -->
Team # 2314151

<!-- b000425 | furniture | pages [24] -->
23

<!-- b000426 | furniture | pages [25] -->
Team # 2314151

<!-- b000427 | furniture | pages [25] -->
Page 24 of 24

<!-- b000428 | heading | pages [25] -->
References

<!-- b000429 | references | pages [25] -->
[1] Benton J. Anderson and Jesse G. Meyer. Finding the optimal human strategy for wordle using

<!-- b000430 | references | pages [25] -->
maximum correct letter probabilities and reinforcement learning, 2022.

<!-- b000431 | references | pages [25] -->
[2] Tarun Kumar. Solution of linear and non linear regression problem by k nearest neighbour

<!-- b000432 | references | pages [25] -->
approach: By using three sigma rule. In 2015 IEEE International Conference on Computational

<!-- b000433 | references | pages [25] -->
Intelligence Communication Technology, pages 197–201, 2015.

<!-- b000434 | references | pages [25] -->
[3] Michal S Gal and Daniel L Rubinfeld. Data standardization. NYUL Rev., 94:737, 2019.

<!-- b000435 | references | pages [25] -->
[4] Sean J Taylor and Benjamin Letham. Forecasting at scale. The American Statistician, 72(1):37–45,

<!-- b000436 | references | pages [25] -->
2018.

<!-- b000437 | references | pages [25] -->
[5] Qibin Zhao, Cesar F. Caiafa, Danilo P. Mandic, Zenas C. Chao, Yasuo Nagasaka, Naotaka Fujii,

<!-- b000438 | references | pages [25] -->
Liqing Zhang, and Andrzej Cichocki. Higher order partial least squares (hopls): A generalized

<!-- b000439 | references | pages [25] -->
multilinear regression method. IEEE Transactions on Pattern Analysis and Machine Intelligence,

<!-- b000440 | references | pages [25] -->
35(7):1660–1673, 2013.

<!-- b000441 | references | pages [25] -->
[6] Ertunga C ¨Ozelkan and Lucien Duckstein. Multi-objective fuzzy regression: a general framework.

<!-- b000442 | references | pages [25] -->
Computers & Operations Research, 27(7-8):635–652, 2000.

<!-- b000443 | references | pages [25] -->
[7] Mark Harman. Making the case for morto: Multi objective regression test optimization. In

<!-- b000444 | references | pages [25] -->
2011 IEEE Fourth International Conference on Software Testing, Verification and Validation

<!-- b000445 | references | pages [25] -->
Workshops, pages 111–114, 2011.

<!-- b000446 | references | pages [25] -->
[8] Aristidis Likas, Nikos Vlassis, and Jakob J Verbeek. The global k-means clustering algorithm.

<!-- b000447 | references | pages [25] -->
Pattern recognition, 36(2):451–461, 2003.

<!-- b000448 | references | pages [25] -->
[9] John A Hartigan and Manchek A Wong. Algorithm as 136: A k-means clustering algorithm.

<!-- b000449 | references | pages [25] -->
Journal of the royal statistical society. series c (applied statistics), 28(1):100–108, 1979.

<!-- b000450 | references | pages [25] -->
[10] Greg Hamerly and Charles Elkan. Learning the k in k-means. Advances in neural information

<!-- b000451 | references | pages [25] -->
processing systems, 16, 2003.

<!-- b000452 | furniture | pages [25] -->
24
