# P-C-2023-2314151-c97576e4

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
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

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1

<!-- b000021 | heading | pages [2] -->
Introduction

<!-- b000022 | furniture | pages [2] -->
Page 1 of 24

<!-- b000023 | prose | pages [2] -->
2 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Our Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000024 | prose | pages [2] -->
2

<!-- b000025 | heading | pages [2] -->
Preparation of the Models

<!-- b000026 | prose | pages [2] -->
2

<!-- b000027 | prose | pages [2] -->
3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1

<!-- b000028 | heading | pages [2] -->
Assumptions

<!-- b000029 | prose | pages [2] -->
3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000030 | heading | pages [2] -->
Notations

<!-- b000031 | prose | pages [2] -->
3

<!-- b000032 | heading | pages [2] -->
Data Processing

<!-- b000033 | prose | pages [2] -->
4

<!-- b000034 | prose | pages [2] -->
4 Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 4 Outlier rejection and standardization . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 4 Word attribute determination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3

<!-- b000035 | prose | pages [2] -->
4 Task 1

<!-- b000036 | prose | pages [2] -->
5

<!-- b000037 | prose | pages [2] -->
7 Prophet algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 7 Higher-order partial correlation analysis model 4.2

<!-- b000038 | prose | pages [2] -->
5 Task 2

<!-- b000039 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | prose | pages [2] -->
9

<!-- b000041 | prose | pages [2] -->
12 Multi-objective regression prediction framework . . . . . . . . . . . . . . . . . . . . . 5.1 12 Establishment of prediction model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 13 Word prediction - EERIE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 14 Feature influence degree analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 15 Model reliability analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.5

<!-- b000042 | prose | pages [2] -->
6 Task 3

<!-- b000043 | prose | pages [2] -->
15

<!-- b000044 | prose | pages [2] -->
16 K-means clustering algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 17 Selection of parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 17 Clustering results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 18 Word interval identification - EERIE . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.4 18 Model reliability analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.5

<!-- b000045 | prose | pages [2] -->
7 Interesting aspects of the data

<!-- b000046 | prose | pages [2] -->
8

<!-- b000047 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000048 | prose | pages [2] -->
9

<!-- b000049 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000050 | prose | pages [2] -->
19

<!-- b000051 | prose | pages [2] -->
20

<!-- b000052 | prose | pages [2] -->
21

<!-- b000053 | prose | pages [2] -->
22 Strength . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 22 Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2

<!-- b000054 | heading | pages [2] -->
10 Letter

<!-- b000055 | prose | pages [2] -->
22

<!-- b000056 | prose | pages [2] -->
22

<!-- b000057 | furniture | pages [2] -->
1

<!-- b000058 | furniture | pages [3] -->
Team # 2314151

<!-- b000059 | furniture | pages [3] -->
Page 2 of 24

<!-- b000060 | prose | pages [3] -->
1

<!-- b000061 | heading | pages [3] -->
Introduction

<!-- b000062 | prose | pages [3] -->
1.1 Problem Background

<!-- b000063 | prose | pages [3] -->
Crossword puzzles have always seemed inseparably linked to the media. Since January 2022, Wor- dle, the New York Times’ digital crossword, has become more and more popular in many countries[1].

<!-- b000064 | prose | pages [3] -->
How do players play Wordle? They are permitted to select five letters from a pool of 26 to construct a five-letter word that can be solved in no more than six attempts to conclude the Wordle puzzle successfully. After the player submits the word, the sticker’s color will change. Green is the correct letter, and yellow is the letter in the word but in the wrong place. There are two modes of play: normal mode and hard mode. Hard mode is where the correct letter (green or yellow) is found in the previous attempt and must be used in subsequent attempts.

<!-- b000065 | prose | pages [3] -->
Wordle updates the puzzle once a day, and many players report their scores on social media. As a result, data such as the number of people reporting their scores that day, the number of players participating in hard mode, and the percentage of players completing the puzzle on different attempts are all collected and counted.

<!-- b000066 | prose | pages [3] -->
By using the available data wisely, we can solve some interesting problems.

<!-- b000067 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000068 | prose | pages [3] -->
Considering the background information, constraints outlined in the problem statement and addi- tional guidance, we need to solve the following problems:

<!-- b000069 | prose | pages [3] -->
• Task 1: Establish a model that can explain and predict changes in the number of reported results and provide a prediction interval for the number of reported results on March 1, 2023. In addition, an examination of the impact of word attributes on the proportion of reports filed by players in the hard mode is necessary, accompanied by a rationale for this phenomenon.

<!-- b000070 | prose | pages [3] -->
• Task 2: Develop a model that predicts reported outcomes’ distribution and explore the uncer- tainties the model and predictions have.

<!-- b000071 | prose | pages [3] -->
• Task 3: Build a model for classifying words according to difficulty and determine the factors associated with word classification. This model is used to determine the difficulty of EERIE and to discuss the accuracy of the classification model.

<!-- b000072 | prose | pages [3] -->
• Task 4: Enumerate and explicate additional noteworthy characteristics inherent in this dataset.

<!-- b000073 | prose | pages [3] -->
• Task 5: Present a concise summary of the study findings in a letter addressed to the Puzzle Editor of the New York Times.

<!-- b000074 | prose | pages [3] -->
1.3 Our Works

<!-- b000075 | prose | pages [3] -->
Based on the analysis of the problem, we propose the model framework shown in figure 1, which is mainly composed of the following parts:

<!-- b000076 | prose | pages [3] -->
Data analysis: processes the reported data and identifies the characteristics of the words.

<!-- b000077 | furniture | pages [3] -->
2

<!-- b000078 | furniture | pages [4] -->
Team # 2314151

<!-- b000079 | furniture | pages [4] -->
Page 3 of 24

<!-- b000080 | heading | pages [4] -->
Predictive modeling: Prophet algorithm was chosen to build a time-series regression prediction

<!-- b000081 | prose | pages [4] -->
model, and a higher-order partial correlation analysis was used to find the degree of influence of each attribute.

<!-- b000082 | prose | pages [4] -->
Development of a multi-objective regression prediction framework: use this framework to help us select a Lasso regression prediction model.

<!-- b000083 | prose | pages [4] -->
Difficulty interval division: the word difficulty was classified into three categories using the K-means algorithm and the classification results were validated by Lasso regression prediction.

<!-- b000084 | caption | pages [4] -->
Figure 1: Model framework

<!-- b000085 | prose | pages [4] -->
2

<!-- b000086 | heading | pages [4] -->
Preparation of the Models

<!-- b000087 | prose | pages [4] -->
2.1

<!-- b000088 | heading | pages [4] -->
Assumptions

<!-- b000089 | prose | pages [4] -->
• Assumption 1. Assume that the user data given in the question is independently and identically distributed.

<!-- b000090 | prose | pages [4] -->
Reason 1: this assumption ensures that the individual samples are independent of each other to avoid the influence of the modeling process due to the association between the samples.

<!-- b000091 | prose | pages [4] -->
• Assumption 2. Assume that the pre-processed data is reliable.

<!-- b000092 | prose | pages [4] -->
Reason 2: this assumption is made to ensure the accuracy of the model solution.

<!-- b000093 | prose | pages [4] -->
• Assumption 3. Assume that the external environment associated with the game does not change abruptly

<!-- b000094 | prose | pages [4] -->
Reason 3: external factors remain steady to ensure stable prediction models.

<!-- b000095 | furniture | pages [4] -->
3

<!-- b000096 | furniture | pages [5] -->
Team # 2314151

<!-- b000097 | prose | pages [5] -->
2.2

<!-- b000098 | heading | pages [5] -->
Notations

<!-- b000099 | furniture | pages [5] -->
Page 4 of 24

<!-- b000100 | caption | pages [5] -->
Table 1: Notations

<!-- b000101 | prose | pages [5] -->
Symbol

<!-- b000102 | prose | pages [5] -->
sj k δj

<!-- b000103 | prose | pages [5] -->
Definition

<!-- b000104 | prose | pages [5] -->
Timestamp Growth rate The amount of change in the growth rate on the timestamp m ϵ N Offset amount Error term Number of cycles in the seasonality model Di Period before and after a holiday κi Range of holiday effects P Significance level

<!-- b000105 | prose | pages [5] -->
3

<!-- b000106 | heading | pages [5] -->
Data Processing

<!-- b000107 | prose | pages [5] -->
3.1 Data Cleaning

<!-- b000108 | prose | pages [5] -->
Topic C reports on the use of Wordle in the past year. However, we found a lot of dirty data in this report.

<!-- b000109 | caption | pages [5] -->
Table 2: Dirty data

<!-- b000110 | prose | pages [5] -->
Number in hard mode Contest number Word Number of reported results

<!-- b000111 | prose | pages [5] -->
525 clen 26381 2424 314 tash 106652 7001 na¨ıve 540 21947 2075 473 marxh 30935 2885 207 favor 137586 3073

<!-- b000112 | prose | pages [5] -->
1 try 2 tries 3 tries 4 tries 5 tries 6 tries 7 or more tries (X)

<!-- b000113 | prose | pages [5] -->
1 17 36 31 12 3 0 2 19 34 27 13 4 1 1 7 24 32 24 11 1 0 9 30 35 19 6 1 1 4 15 26 29 21 4

<!-- b000114 | prose | pages [5] -->
In the data shown above, the two words numbered 525, and 314 do not match the game because they are only 4 in length, so we inferred that the dataset blundered by under-entering the letters. To solve such a problem, we found the most similar letters to them instead by comparing them with artificial intelligence algorithms. The word numbered 540 is due to a misspelling of the letter, which should be ”naive.” We searched the word database and found that the word ”marxh,” numbered 473, did not exist. We then compared the shapes of the words with database analysis and concluded that the correct spelling should be ”marsh.” The word numbered 207 has an extra space in the input, so it is also an outlier. We can delete the extra space to get the correct data.

<!-- b000115 | prose | pages [5] -->
Outlier rejection and standardization 3.2

<!-- b000116 | prose | pages [5] -->
We use the 68–95–99.7 rule (3σ criterion) to screen and reject outliers[2]. We found an anomaly in the Number of reported results data for the word ’study’ on 2022/11/30, and we zeroed it to bring it

<!-- b000117 | furniture | pages [5] -->
4

<!-- b000118 | furniture | pages [6] -->
Team # 2314151

<!-- b000119 | prose | pages [6] -->
back to the same order of magnitude.

<!-- b000120 | prose | pages [6] -->
(a) 3σ criterion

<!-- b000121 | furniture | pages [6] -->
Page 5 of 24

<!-- b000122 | prose | pages [6] -->
(b) Deviation point rejection

<!-- b000123 | caption | pages [6] -->
Figure 2: Outlier rejection

<!-- b000124 | prose | pages [6] -->
In addition, we also use the StandardScaler data normalization method, which normalizes the training set data by calculating the mean and standard deviation of the training set[3], see equation

<!-- b000125 | prose | pages [6] -->
z = x −u

<!-- b000126 | prose | pages [6] -->
(1) s

<!-- b000127 | prose | pages [6] -->
x is the sample, u is the mean of the feature columns of the training set, and s is the standard deviation of the feature columns of the training set.

<!-- b000128 | prose | pages [6] -->
3.3 Word attribute determination

<!-- b000129 | prose | pages [6] -->
In the topic for the prediction of the reported results, we need to analyze the properties of the words. Combining Wordle’s gameplay and reviewing the analysis information of the relevant games, we classify the attributes of words into the following points.

<!-- b000130 | heading | pages [6] -->
1. The total frequency of letters appearing in words: Count the frequency of each letter appearing

<!-- b000131 | prose | pages [6] -->
in the candidate word list. If a letter appears in 900 words, its frequency is 900. Then the candidate words are sorted by total letter frequency, and if a word contains more high-frequency letters, it is ranked first.

<!-- b000132 | caption | pages [6] -->
Figure 3: Total frequency of letters in a word

<!-- b000133 | furniture | pages [6] -->
5

<!-- b000134 | furniture | pages [7] -->
Team # 2314151

<!-- b000135 | furniture | pages [7] -->
Page 6 of 24

<!-- b000136 | heading | pages [7] -->
2. The number of vowel/consonant letters in a word: When players play Wordle, the first words

<!-- b000137 | prose | pages [7] -->
are often chosen as AUDIO and LEFTY because this includes all the vowel letters: ’AEIOU.’ In the composition of words, vowel letters are easily known and, therefore, easily guessed.

<!-- b000138 | heading | pages [7] -->
3. The number of occurrences of different vowel/consonant letters in a word (no duplication):

<!-- b000139 | prose | pages [7] -->
The number of vowel/consonant letters is one of the attributes of a word that we infer affects the percentage of guessed words. Accordingly, the number of vowels/consonants is also essential in the percentage of reported words. Let us take ’there’ for example. The number of vowels is 2, The Number of vowels(no duplication) is 1, the number of consonants is 3, and the number of vowels(no duplication) is 3.

<!-- b000140 | caption | pages [7] -->
Table 3: Alphabetic properties

<!-- b000141 | prose | pages [7] -->
(no duplication) Word Number of vowels

<!-- b000142 | prose | pages [7] -->
there 2 1

<!-- b000143 | prose | pages [7] -->
Number of consonants (no duplication)

<!-- b000144 | prose | pages [7] -->
3 3

<!-- b000145 | heading | pages [7] -->
4. Frequency of word usage: We use many words in our daily lives, some common and some not

<!-- b000146 | prose | pages [7] -->
so familiar. People tend to guess common words more easily. Therefore, we have listed and sorted the frequency of use of all the five-letter words involved in this game. The following table shows the partially sorted data.

<!-- b000147 | caption | pages [7] -->
Table 4: Letter Commonness Ranking

<!-- b000148 | prose | pages [7] -->
Word Times Rank Word Times Rank Word Times Rank

<!-- b000149 | prose | pages [7] -->
0.001954 which 0.002044 1 their 2 would 0.001711 3 0.001296 about 0.001407 4 could 5 there 0.001273 6

<!-- b000150 | heading | pages [7] -->
5. The number of repeated letters and the maximum number of repetitions: There may be

<!-- b000151 | prose | pages [7] -->
several repeated letters in the formation of a word. It isn’t common, but the number of times the letter is repeated also affects how successful a player is at guessing the word. Therefore, we counted these two attributes of the letters in words in the report as their characteristics.

<!-- b000152 | caption | pages [7] -->
Table 5: Alphabetic properties

<!-- b000153 | prose | pages [7] -->
Word Number of duplicate Maximum number of repeats

<!-- b000154 | prose | pages [7] -->
cross 1 2 glass 1 2

<!-- b000155 | prose | pages [7] -->
Word Number of duplicate Maximum number of repeats

<!-- b000156 | prose | pages [7] -->
exist 0 0 apply 1 0

<!-- b000157 | furniture | pages [7] -->
6

<!-- b000158 | furniture | pages [8] -->
Team # 2314151

<!-- b000159 | prose | pages [8] -->
4 Task 1

<!-- b000160 | prose | pages [8] -->
4.1

<!-- b000161 | heading | pages [8] -->
Prophet algorithm

<!-- b000162 | prose | pages [8] -->
4.1.1

<!-- b000163 | heading | pages [8] -->
Background of the algorithm

<!-- b000164 | furniture | pages [8] -->
Page 7 of 24

<!-- b000165 | prose | pages [8] -->
Although neural network models have become increasingly popular in recent years, this model usually requires a large amount of data for training. A dataset with only 400 or so data is not a good place to consider a neural network model.

<!-- b000166 | prose | pages [8] -->
On balance, we decided to use the Prophet model, an algorithm based on an additive model for predicting time series data with characteristics such as seasonality, trends, and holidays. Also, Prophet[4] has strong robustness to handle problems such as non-stationary time series and outliers. For this dataset, Prophet is a good choice.

<!-- b000167 | heading | pages [8] -->
Prediction model building based on Prophet algorithm

<!-- b000168 | prose | pages [8] -->
4.1.2

<!-- b000169 | heading | pages [8] -->
1. Prophet algorithm principle

<!-- b000170 | prose | pages [8] -->
The principle of Prophet algorithm is as follows:

<!-- b000171 | prose | pages [8] -->
y(t) = g(t) + s(t) + h(t) + ϵ (2)

<!-- b000172 | prose | pages [8] -->
g(t) denotes the trend term, which represents the time series trend over the non-period. s(t) denotes the period term, which is generally measured in weeks or years. h(t) denotes the holiday term, which represents the effect of those potential non-periodic holidays in the time series on the predicted values. ϵ denotes the error term or residual term, which indicates the fluctuations not predicted by the model, and ϵ follows a Gaussian distribution.

<!-- b000173 | prose | pages [8] -->
The Prophet algorithm models each of the model’s three components and then combines them to generate the forecast data.

<!-- b000174 | heading | pages [8] -->
2. Trend term model

<!-- b000175 | prose | pages [8] -->
Prophet’s implementation of the trend part applies two main models, one is the saturated growth model, and the other is the segmented linear model.

<!-- b000176 | heading | pages [8] -->
• Saturation growth model

<!-- b000177 | prose | pages [8] -->
The saturation growth model, also known as the logistic growth model, is a model used to describe a system in which the growth rate gradually decreases and eventually stabilizes.

<!-- b000178 | prose | pages [8] -->
g(t) = C(t) (3) 1 + exp(−(k + a(t)Tδ) · (t −(m + a(t)Tγ)))

<!-- b000179 | prose | pages [8] -->
C(t) denotes the carrying capacity, a time function limiting the maximum value that can be grown. k denotes the growth rate.

<!-- b000180 | heading | pages [8] -->
• Segmented growth model

<!-- b000181 | prose | pages [8] -->
g(t) = (k + a(t)Tδ) · t + (m + a(t)Tγ) (4)

<!-- b000182 | furniture | pages [8] -->
7

<!-- b000183 | furniture | pages [9] -->
Team # 2314151

<!-- b000184 | furniture | pages [9] -->
Page 8 of 24

<!-- b000185 | prose | pages [9] -->
It is worth noting that the most significant difference between the segmented linear function and the logistic regression function is that the setting of y is different in the segmented linear function.

<!-- b000186 | prose | pages [9] -->
γj=−sjδj (5)

<!-- b000187 | prose | pages [9] -->
The model defines the points corresponding to changes in the growth rate k, called n changepoints. changeepoint prior scale is defined as the flexibility of the growth trend model.

<!-- b000188 | heading | pages [9] -->
3. Seasonality trends model

<!-- b000189 | prose | pages [9] -->
Since a time series may contain seasonal trends with multiple days, weeks, months, years, and other cycle types, the Fourier scale can be used to approximate this cycle property. The Fourier series is shown as follows.

<!-- b000190 | prose | pages [9] -->
N

<!-- b000191 | prose | pages [9] -->
(ancos(2πnt

<!-- b000192 | prose | pages [9] -->
X

<!-- b000193 | prose | pages [9] -->
s(t) =

<!-- b000194 | prose | pages [9] -->
n=1

<!-- b000195 | prose | pages [9] -->
) + bnsin(2πnt

<!-- b000196 | prose | pages [9] -->
)) (6)

<!-- b000197 | prose | pages [9] -->
P

<!-- b000198 | prose | pages [9] -->
P

<!-- b000199 | prose | pages [9] -->
N denotes the number of periods one wishes to use in the model. Larger values of N allow for more complex seasonal functions to be fitted. However, they also introduce more overfitting problems.

<!-- b000200 | heading | pages [9] -->
4. Holiday effect model

<!-- b000201 | prose | pages [9] -->
In the natural environment, holidays can significantly impact the time series. Each holiday is not always the same, so the effects of different holidays at different points in time are treated as independent models. For the ith holiday, Di denotes the period before and after the holiday.

<!-- b000202 | prose | pages [9] -->
In order to represent the holiday effect, a corresponding indicator function is needed, and a parameter κi is needed to represent the range of the holiday effect.

<!-- b000203 | prose | pages [9] -->
Assuming that there are L holidays, the holiday effect model is:

<!-- b000204 | prose | pages [9] -->
L X

<!-- b000205 | prose | pages [9] -->
κi · 1{t∈Di}

<!-- b000206 | prose | pages [9] -->
h(t) = Z(t)κ =

<!-- b000207 | prose | pages [9] -->
(7)

<!-- b000208 | prose | pages [9] -->
i=1

<!-- b000209 | prose | pages [9] -->
Z(t) = (1{t∈D1}, · · · , 1{t∈DL}) and κ = (κ1, · · · , κL)T

<!-- b000210 | prose | pages [9] -->
4.1.3 Parameter setting

<!-- b000211 | prose | pages [9] -->
We choose a trend term based on a segmented linear function for the trend term model.

<!-- b000212 | prose | pages [9] -->
We set n changepoints to 25 and changepoint prior scale to 0.05. For seasonal trends, we set season- ality prior scale to 10. For holiday effects, we set holidays prior scale to 10. In addition, we set interval width to 0.80, mcmc samples to 0, and uncertainty samples to 1000.

<!-- b000213 | furniture | pages [9] -->
8

<!-- b000214 | furniture | pages [10] -->
Team # 2314151

<!-- b000215 | prose | pages [10] -->
4.1.4

<!-- b000216 | heading | pages [10] -->
Result

<!-- b000217 | furniture | pages [10] -->
Page 9 of 24

<!-- b000218 | prose | pages [10] -->
We set up the model using the parameter values shown in Figure a. When selecting a data range, it is usually necessary to consider the order of magnitude of the data. The reason for taking data starting from the same order of magnitude is to avoid the effects of data bias and errors and to ensure the accuracy and reliability of the data. Therefore, we screened the original data and selected data from after May 5, 2022. The final results we obtained are as follows.

<!-- b000219 | caption | pages [10] -->
Table 6: Predicted results

<!-- b000220 | prose | pages [10] -->
ds yhat

<!-- b000221 | prose | pages [10] -->
2023-03-01 14425.58926

<!-- b000222 | prose | pages [10] -->
yhat lower yhat upper

<!-- b000223 | prose | pages [10] -->
10355.27753 18741.54302

<!-- b000224 | prose | pages [10] -->
The model predicts a range of 10355 to 18742 for the number of reports on March 1, 2023.

<!-- b000225 | prose | pages [10] -->
(a) Prediction Chart (b) Weekly Trend Chart

<!-- b000226 | caption | pages [10] -->
Figure 4: Forecast and trend charts

<!-- b000227 | prose | pages [10] -->
The graph above shows the time series trend and weekly seasonality. Figure a shows the general trend in the number of reports and the future forecast. From May 5, 2022, the number of reports decreases, and the decrease rate gradually becomes smaller. In addition, it predicts the report number interval for seventy days after January 1, 2023.

<!-- b000228 | prose | pages [10] -->
Figure b shows the weekly cyclical pattern, with significantly more people playing Wordle on Wednesdays. The number of weekend reports tends to be lower.

<!-- b000229 | heading | pages [10] -->
Higher-order partial correlation analysis model

<!-- b000230 | prose | pages [10] -->
4.2

<!-- b000231 | prose | pages [10] -->
Correlation analysis using Pearson’s correlation coefficient 4.2.1

<!-- b000232 | prose | pages [10] -->
The problem to be solved in this model is to perform a correlation analysis between the attributes of the words and the percentage of difficulty patterns separately. The attributes of the words have been classified in the data processing, but after analyzing the data of this question, we find a strong correlation between the attributes of the words. Therefore, we first conducted correlation tests for

<!-- b000233 | furniture | pages [10] -->
9

<!-- b000234 | furniture | pages [11] -->
Team # 2314151

<!-- b000235 | furniture | pages [11] -->
Page 10 of 24

<!-- b000236 | prose | pages [11] -->
each variable to examine the Pearson correlation coefficients of each attribute with the percentage of difficulty patterns without controlling for other variables:

<!-- b000237 | caption | pages [11] -->
Table 7: Pearson correlation coefficient distribution

<!-- b000238 | prose | pages [11] -->
Attributes of words

<!-- b000239 | prose | pages [11] -->
Number of vowels

<!-- b000240 | prose | pages [11] -->
R P

<!-- b000241 | prose | pages [11] -->
0.083460383 0.093068989 Number of vowels(non-repetition) Number of consonants 0.05075013 0.307685109 -0.083460383 0.093068989 Number of consonants(non-repetition) Word commonness -0.106284281 0.032271311 0.094056604 0.058285504 The sum of the frequencies of letters 0.008176597 0.869535404

<!-- b000242 | prose | pages [11] -->
From the above table, we can see that the p-values of the significance tests for the correlation tests of each attribute and percent hard are almost all weakly correlated, and only the total ranking of word frequency of letters in words is strongly correlated. This result is not satisfactory. We analyzed the attributes of the words again and find that there is a strong correlation between these attributes, and the influence between the attributes cannot be ignored. To sum up, we chose the algorithm of higher-order biased correlation analysis to do correlation analysis on the percentage of each attribute in the word with the difficulty pattern to solve this problem[5].

<!-- b000243 | heading | pages [11] -->
Establishment of Higher-order partial correlation analysis model

<!-- b000244 | prose | pages [11] -->
4.2.2

<!-- b000245 | prose | pages [11] -->
(1) First-order partial correlation coefficient: The partial correlation coefficient of any two of the three variables is calculated after excluding the effect of the remaining one variable and is called the first-order partial correlation coefficient with the following formula:

<!-- b000246 | prose | pages [11] -->
rij·h = q rij −rihrjh

<!-- b000247 | prose | pages [11] -->
(8)

<!-- b000248 | prose | pages [11] -->
 

<!-- b000249 | prose | pages [11] -->


<!-- b000250 | prose | pages [11] -->
(1 −r2

<!-- b000251 | prose | pages [11] -->
1 −r2

<!-- b000252 | prose | pages [11] -->
ih)

<!-- b000253 | prose | pages [11] -->
jh

<!-- b000254 | prose | pages [11] -->
In this equation, rij is the simple correlation coefficient between variables xi and xj, rih is the simple correlation coefficient between variables xi and xh, and rjh is the simple correlation coefficient between variables xj and xh.

<!-- b000255 | prose | pages [11] -->
(2) High-order partial correlation coefficient: Generally, if there are k (k > 2) variables x1, x2, ..., xk, then the formula of partial correlation coefficient of samples of order g (g ≤k-2) for any two variables xi and xj is:

<!-- b000256 | prose | pages [11] -->
rij·l1l2···lg = rij·l1l2···lg−1 −rilg·l1l2···lg−1rjlg·l1l2···lg−1 q

<!-- b000257 | prose | pages [11] -->
(9)

<!-- b000258 | prose | pages [11] -->
ilg·l1l2···lg−1)(1 −r2

<!-- b000259 | prose | pages [11] -->
(1 −r2

<!-- b000260 | prose | pages [11] -->
jlg·l1l2···lg−1)

<!-- b000261 | prose | pages [11] -->
where the right-hand sides are all partial correlation coefficients of order g-1.

<!-- b000262 | furniture | pages [11] -->
10

<!-- b000263 | furniture | pages [12] -->
Team # 2314151

<!-- b000264 | prose | pages [12] -->
4.2.3

<!-- b000265 | heading | pages [12] -->
Analysis of results

<!-- b000266 | furniture | pages [12] -->
Page 11 of 24

<!-- b000267 | prose | pages [12] -->
In the higher-order partial correlation analysis, we need to control for irrelevant variables as a way to eliminate the influence of other variables on the studied variables. The results are as follows:

<!-- b000268 | caption | pages [12] -->
Table 8: Distribution of high-order bias correlation results

<!-- b000269 | prose | pages [12] -->
High-order partial correlation coefficient Attributes of words

<!-- b000270 | prose | pages [12] -->
Number of vowels Number of vowels(non-repetition) Number of consonants Number of consonants(non-repetition) Word commonness The sum of the frequencies of letters

<!-- b000271 | prose | pages [12] -->
P

<!-- b000272 | prose | pages [12] -->
-0.319578 4.37009E-11 -0.271561 2.72256E-08 0.319578 4.37009E-11 0.306104 3.00056E-10 -0.080926 0.103481297 -0.133207 0.007197084

<!-- b000273 | prose | pages [12] -->
As shown in the above table, the P-values corresponding to the attributes of the above six words are much less than 0.05. Therefore, the results can be considered statistically significant.

<!-- b000274 | prose | pages [12] -->
In general, the higher-order partial correlation coefficient, after taking the absolute value, is no correlation when it is 0-0.09, weak correlation when it is 0.1-0.3, moderate correlation when it is 0.3-0.5, and strong correlation when it is 0.5-1.0.

<!-- b000275 | caption | pages [12] -->
Figure 5: Heat map of high-order partial correlations of word attributes with percent hard

<!-- b000276 | prose | pages [12] -->
By analyzing the data as well as the results of the heat map, we obtained the following correlations of word attributes with the percentage of hard modes:

<!-- b000277 | caption | pages [12] -->
Table 9: Word attribute correlation result distribution

<!-- b000278 | prose | pages [12] -->
Attributes of words

<!-- b000279 | prose | pages [12] -->
Number of vowels

<!-- b000280 | prose | pages [12] -->
Degree of correlation

<!-- b000281 | prose | pages [12] -->
Moderate negative correlation Number of vowels(non-repetition) Number of consonants Weak negative correlation Moderate positive correlation Number of consonants(non-repetition) Word commonness Moderate positive correlation No correlation The sum of the frequencies of letters Weak negative correlation

<!-- b000282 | furniture | pages [12] -->
11

<!-- b000283 | furniture | pages [13] -->
Team # 2314151

<!-- b000284 | furniture | pages [13] -->
Page 12 of 24

<!-- b000285 | prose | pages [13] -->
5 Task 2

<!-- b000286 | prose | pages [13] -->
5.1 Multi-objective regression prediction framework

<!-- b000287 | prose | pages [13] -->
In this part, we need to address a prediction problem where the model we build can predict the percentage of user engagement related to the Wordle puzzle at a future date. We currently have user report data for Wordle during the past year, where we divide the words per day into several relevant attributes and take into account the effect of time of day, as users complete the game differently on weekends and weekdays.

<!-- b000288 | prose | pages [13] -->
Since the amount of data given in the question is very small, we give up using neural network to predict it, and instead use an optimized multi-objective regression prediction framework[6] to process it.

<!-- b000289 | prose | pages [13] -->
The specific process of using a multi-objective regression prediction framework to solve a forecast- ing problem is as follows:

<!-- b000290 | caption | pages [13] -->
Figure 6: Operational process of multi-objective regression prediction framework

<!-- b000291 | prose | pages [13] -->
Our framework currently supports partial least squares regression algorithms, Bayesian linear regression-based hyperparameter tuning and feature selection algorithms, elastic network regression models, LASSO regression algorithm models, ridge regression algorithms, and high-performance quantile regression algorithms models. All these regression models can perform well for small data while being able to handle multiple classification tasks and suitable for incremental training. In addition, their well-adaptive ability, self-learning ability, and generalization ability also meet our requirements.

<!-- b000292 | furniture | pages [13] -->
12

<!-- b000293 | furniture | pages [14] -->
Team # 2314151

<!-- b000294 | furniture | pages [14] -->
Page 13 of 24

<!-- b000295 | caption | pages [14] -->
Figure 7: Algorithm integrated evaluation analysis framework

<!-- b000296 | prose | pages [14] -->
5.2

<!-- b000297 | heading | pages [14] -->
Establishment of prediction model

<!-- b000298 | prose | pages [14] -->
(1) Establishment of a multi-objective regression prediction framework The multi-objective regression prediction framework divides the data into training and test sets and normalizes the data. It identifies the optimal parameters by grid search and evaluates the accuracy of the model based on the mean of the mean squared error, which in turn determines the best algorithmic model[7]. Then, the multi-objective regression prediction framework uses the best algorithm to make predictions on the data and returns the data at the original scale of inverse normalization. For our dataset, the output of the evaluation function-based algorithm evaluation framework is as shown below:

<!-- b000299 | caption | pages [14] -->
Figure 8: Output of a multi-objective regression prediction framework based on an evaluation function

<!-- b000300 | furniture | pages [14] -->
13

<!-- b000301 | furniture | pages [15] -->
Team # 2314151

<!-- b000302 | furniture | pages [15] -->
Page 14 of 24

<!-- b000303 | prose | pages [15] -->
From the output of the above figure, we can find that the root mean square error of the LASSO regression algorithm is the smallest, and the total average root mean square error of its multiple repeated fits is only 0.8, which can show that our regression model can predict the data very well.

<!-- b000304 | heading | pages [15] -->
(2) Establishment of Lasso Regression Model

<!-- b000305 | prose | pages [15] -->
Lasso regression (LASSO, least absolute shrinkage and selection operator) is the addition of a penalty term of L1 parity to the residuals tiling and minimization:

<!-- b000306 | prose | pages [15] -->
k

<!-- b000307 | prose | pages [15] -->
(yi −ˆyi)2 + λ

<!-- b000308 | prose | pages [15] -->
ˆβu

<!-- b000309 | furniture | pages [15] -->


<!-- b000310 | prose | pages [15] -->
i + λ||ˆβ∥1 = min

<!-- b000311 | prose | pages [15] -->
X

<!-- b000312 | prose | pages [15] -->
e2

<!-- b000313 | prose | pages [15] -->
min

<!-- b000314 | prose | pages [15] -->
X

<!-- b000315 | prose | pages [15] -->
X

<!-- b000316 | prose | pages [15] -->
(10)

<!-- b000317 | prose | pages [15] -->
u=1

<!-- b000318 | prose | pages [15] -->
Because the L1 parametrization is in the form of an absolute value, it is not derivable at the zero point. Thus, it no longer has an analytic solution and can be solved using gradient descent (to be precise, a subgradient algorithm). Ridge regression cannot eliminate variables. The excellent property of LASSO regression is that it can produce sparsity, which can reduce some insignificant regression coefficients to zero for the purpose of eliminating variables.Its loss function is:

<!-- b000319 | prose | pages [15] -->
1 2margmin J(w, b) = w,b

<!-- b000320 | prose | pages [15] -->
5.3 Word prediction - EERIE

<!-- b000321 | prose | pages [15] -->
m

<!-- b000322 | prose | pages [15] -->
n

<!-- b000323 | prose | pages [15] -->
(ˆyi −yi)2 + α

<!-- b000324 | prose | pages [15] -->
X

<!-- b000325 | prose | pages [15] -->
X

<!-- b000326 | prose | pages [15] -->
∥wi∥ (11)

<!-- b000327 | prose | pages [15] -->
i=1

<!-- b000328 | prose | pages [15] -->
i=1

<!-- b000329 | prose | pages [15] -->
First, the word EERIE can be attributed using the feature engineering established above. The relevant attributes of the word EERIE are as follows.

<!-- b000330 | caption | pages [15] -->
Table 10: Relevant attributes of the word EERIE

<!-- b000331 | prose | pages [15] -->
Date Number of vowels

<!-- b000332 | prose | pages [15] -->
01/03/23 4

<!-- b000333 | prose | pages [15] -->
Number of vowels (non-repetition)

<!-- b000334 | prose | pages [15] -->
2

<!-- b000335 | prose | pages [15] -->
Number of consonant Word

<!-- b000336 | prose | pages [15] -->
EERIE 1

<!-- b000337 | prose | pages [15] -->
Word commonness

<!-- b000338 | prose | pages [15] -->
224

<!-- b000339 | prose | pages [15] -->
Number of consonant (non-repetition) Contest number

<!-- b000340 | prose | pages [15] -->
620 1

<!-- b000341 | prose | pages [15] -->
The sum of the frequencies of letters

<!-- b000342 | prose | pages [15] -->
27903

<!-- b000343 | prose | pages [15] -->
After the above multi-objective regression prediction framework, we identified a modified Lasso regression model to achieve the prediction of the percentage of word relevance at a given date. We performed Lasso regression prediction for the word EERIE to predict its reported percentage on March 1, 2023. We take the average of multiple fits as the final prediction to make the results more accurate.

<!-- b000344 | caption | pages [15] -->
Table 11: Precise results-EERIE

<!-- b000345 | prose | pages [15] -->
4 tries 1 try 2 tries 3 tries 5 tries 6 tries 7 or more tries (X)

<!-- b000346 | prose | pages [15] -->
33.8665962 0.023996469 3.60053273 16.9184627 30.5875392 12.9104259 2.09258948

<!-- b000347 | furniture | pages [15] -->
14

<!-- b000348 | furniture | pages [16] -->
Team # 2314151

<!-- b000349 | furniture | pages [16] -->
Page 15 of 24

<!-- b000350 | prose | pages [16] -->
Finally, the predicted percentage result was rounded, and the final predicted result was obtained:

<!-- b000351 | caption | pages [16] -->
Table 12: Final Results-EERIE

<!-- b000352 | prose | pages [16] -->
Date Contest number Word 1 try 2 tries

<!-- b000353 | prose | pages [16] -->
01/03/23 620 EERIE 0 4

<!-- b000354 | prose | pages [16] -->
5.4 Feature influence degree analysis

<!-- b000355 | prose | pages [16] -->
3 tries 4 tries 5 tries 6 tries 7 or more tries (X)

<!-- b000356 | prose | pages [16] -->
17 34 30 13 2

<!-- b000357 | prose | pages [16] -->
In order to get the word attributes that have a more significant influence on our prediction model, we propose an analysis based on Permutation Importance.

<!-- b000358 | prose | pages [16] -->
First, we obtain a trained Lasso model. Next, we disrupt the values of a certain column of data and then predict the obtained dataset. The predicted values are used with the true target values to calculate how much the loss function has been elevated due to random sorting. The amount of decay in the model performance represents the importance of the disordered column. Then, we recover the disordered column and repeat the previous operation on the next column of data until the importance of each column is calculated.

<!-- b000359 | prose | pages [16] -->
To make the results more general, we run the analysis three times to analyze the scores of different attributes and summarize the final fit results in the following figures, which help us to analyze the degree of influence of different attributes in the words on the model.

<!-- b000360 | caption | pages [16] -->
Figure 9: Feature importance score Lasso

<!-- b000361 | caption | pages [16] -->
Figure 10: Heat map of the features importance of

<!-- b000362 | prose | pages [16] -->
the seven attributes of words

<!-- b000363 | prose | pages [16] -->
In our model, we observed a strong correlation between the two attributes of the number of conso- nants (excluding repeated consonants) and the number of vowels (excluding repeated vowels) in words. Also, we found a moderate correlation between the sum of the frequencies of all letter occurrences in words, the number of consonants, and the number of vowels. In contrast, the correlations between word commonness and date were weaker.

<!-- b000364 | prose | pages [16] -->
5.5

<!-- b000365 | heading | pages [16] -->
Model reliability analysis

<!-- b000366 | prose | pages [16] -->
To evaluate the reliability of our prediction model, we used two methods. First, we calculated the root mean square error of the model prediction results to measure the deviation of the prediction

<!-- b000367 | furniture | pages [16] -->
15

<!-- b000368 | furniture | pages [17] -->
Team # 2314151

<!-- b000369 | furniture | pages [17] -->
Page 16 of 24

<!-- b000370 | prose | pages [17] -->
results from the actual data. Second, we used the prediction model to forecast the given data and then compared the forecast with the actual data to assess the accuracy of the prediction results.

<!-- b000371 | prose | pages [17] -->
The root means square error is obtained by calculating the sum of squares of the deviations between the predicted and actual values divided by the ratio of the number of observations n and then taking the square root. The formula for the root mean square error is as follows.

<!-- b000372 | prose | pages [17] -->
r

<!-- b000373 | prose | pages [17] -->
RMSE =

<!-- b000374 | prose | pages [17] -->
1 1

<!-- b000375 | prose | pages [17] -->
X

<!-- b000376 | prose | pages [17] -->
(yi −yihat)2

<!-- b000377 | prose | pages [17] -->
n ·

<!-- b000378 | prose | pages [17] -->
(12)

<!-- b000379 | prose | pages [17] -->
Where n is the number of samples, yi is the actual value of the ith sample, and yihat is the predicted value of the ith sample. The units of RMSE are the same as those of the target variable. We fit and graphically analyze the fitted lasso regression model results for the root mean square error.

<!-- b000380 | prose | pages [17] -->
According to the output plot of the lasso regression in Figure 7, we found that the RMSE of the three solutions did not exceed 0.85, and the average RMSE was 0.8. Generally speaking, the prediction accuracy is considered high when the RMSE does not exceed 2.

<!-- b000381 | prose | pages [17] -->
Here is an example of a graph comparing the degree of the trend of 5 successful guesses of words:

<!-- b000382 | caption | pages [17] -->
Figure 11: Comparison of the degree of the trend of 5 successful guesses of words

<!-- b000383 | prose | pages [17] -->
The blue curve is the percentage of 5 successes for the original data. In comparison, the orange curve is the percentage of 5 successes predicted by our prediction model, and it can be seen that the deviation of its prediction results is in the acceptable range.

<!-- b000384 | prose | pages [17] -->
6 Task 3

<!-- b000385 | prose | pages [17] -->
We think that the ”average number of tries” can represent the difficulty level of a word, but since the data set given in the question is too small, it would affect the performance of the clustering analysis. Therefore, we re-fit the framework of the Task 2 to the distribution of tries for the 12,974 words in the prediction dictionary after removing the time variable, and use this distribution to find the average number of tries. Following this, the average number of tries is clustered using K-means clustering[8].

<!-- b000386 | furniture | pages [17] -->
16

<!-- b000387 | furniture | pages [18] -->
Team # 2314151

<!-- b000388 | prose | pages [18] -->
6.1

<!-- b000389 | heading | pages [18] -->
K-means clustering algorithm

<!-- b000390 | furniture | pages [18] -->
Page 17 of 24

<!-- b000391 | prose | pages [18] -->
The K-means algorithm measures the similarity of different data objects by selecting a suitable distance formula[9]. The distance between data is inversely proportional to the similarity, i.e., the smaller the similarity, the larger the distance. K-means algorithm first needs to specify the initial number of clusters k and the corresponding initial cluster center C randomly from the given data objects, and calculate the distance from the initial cluster center to the rest of the data objects[10]. In this paper, we choose Euclidean distance. The Euclidean distance formula from the cluster center to other data objects in the space is:

<!-- b000392 | prose | pages [18] -->
d (x, Ci) =

<!-- b000393 | prose | pages [18] -->
v v

<!-- b000394 | prose | pages [18] -->
m

<!-- b000395 | prose | pages [18] -->
u u

<!-- b000396 | prose | pages [18] -->
X

<!-- b000397 | prose | pages [18] -->
(xj −Cij)2

<!-- b000398 | prose | pages [18] -->
u u

<!-- b000399 | prose | pages [18] -->
(13)

<!-- b000400 | prose | pages [18] -->
t t

<!-- b000401 | prose | pages [18] -->
j=1

<!-- b000402 | prose | pages [18] -->
where x is the data object, Ci is the i-th cluster center, m is the dimension of the data object, and xj, Cij are the attribute values of the j-th dimension of the data object x and the cluster center Ci.

<!-- b000403 | prose | pages [18] -->
According to the Euclidean distance measure of similarity, the target data with the highest similarity to the clustering center are assigned to the clusters of Ci. And then the data objects in k clusters are averaged to form a new round of clustering centers. The calculation formula is:

<!-- b000404 | prose | pages [18] -->
k X

<!-- b000405 | prose | pages [18] -->
SSE =

<!-- b000406 | prose | pages [18] -->
i=1

<!-- b000407 | prose | pages [18] -->
6.2 Selection of parameters

<!-- b000408 | prose | pages [18] -->
X

<!-- b000409 | prose | pages [18] -->
|d (x, Ci)|2 (14)

<!-- b000410 | prose | pages [18] -->
x∈Ci

<!-- b000411 | prose | pages [18] -->
• Silhouette Coefficient method: This method evaluates the clustering quality by calculating the silhouette coefficients of each sample point. Where the silhouette coefficient integrates the magnitude of intra-cluster distance and inter-cluster distance and takes a value between [-1,1], the closer to 1 means the better clustering effect.

<!-- b000412 | prose | pages [18] -->
• Davies-Bouldin index (abbreviated as DBI) method: This method evaluates the quality of clustering by calculating the ratio of the average distance of all points within each cluster to the cluster center and the shortest distance between different cluster centers.

<!-- b000413 | prose | pages [18] -->
After analysis, we classified the words into 3-5 categories based on difficulty, with the following parameters:

<!-- b000414 | caption | pages [18] -->
Table 13: Parameters

<!-- b000415 | prose | pages [18] -->
Silhouette Coefficient Number of clusters DBI

<!-- b000416 | prose | pages [18] -->
0.545003549 3 0.562683379 0.536022115 4 0.561324728 0.523517926 5 0.558397471

<!-- b000417 | prose | pages [18] -->
As illustrated in the table above, both Silhouette Coefficient and DBI are decreasing slightly as the number of clusters increases. To improve the accuracy of identifying word difficulty, we choose to cluster into 3 classes.

<!-- b000418 | furniture | pages [18] -->
17

<!-- b000419 | furniture | pages [19] -->
Team # 2314151

<!-- b000420 | prose | pages [19] -->
6.3

<!-- b000421 | heading | pages [19] -->
Clustering results

<!-- b000422 | furniture | pages [19] -->
Page 18 of 24

<!-- b000423 | prose | pages [19] -->
Based on the above analysis, we selected the K-means algorithm for clustering the data set into three classes and obtained the following clustering results.

<!-- b000424 | prose | pages [19] -->
Aggregate results:

<!-- b000425 | caption | pages [19] -->
Table 14: Aggregate results

<!-- b000426 | prose | pages [19] -->
Number of vowels Number of duplicate Maximum of repeats 0 0.519623 0.63264 1 0.019896 0.023617 2 1.210897 1.182715 Number of vowels(non-repetition) Times 1.859318 1.546858 0.000002 1.77483 1.759786 0.000009 1.748239 1.354157 0.000001 Number of consonants Rank time Weighted sums 0 18842.21231 423.226591 1 20294.22727 403.383609 2 16888.876 451.443208

<!-- b000427 | prose | pages [19] -->
Difficulty interval division:

<!-- b000428 | prose | pages [19] -->
Number of consonants(non-repetition) 3.140682 2.933519 3.22517 3.220317 3.251761 2.434946

<!-- b000429 | caption | pages [19] -->
Figure 12: Word difficulty interval

<!-- b000430 | prose | pages [19] -->
Analysis of the results shows that Number of duplicates, Maximum of repeats, Prevalence, and Frequency vary widely in different classifications. According to the quartile method, the normal value is generally defined as greater than QL −kIQR or less than QU + kIQR. Here, we k take 0.5, and the specific difficulty interval is shown below.

<!-- b000431 | caption | pages [19] -->
Table 15: Specific difficulty interv

<!-- b000432 | prose | pages [19] -->
Maximum of repeats Number of duplicate easy (0, 0) (0, 0) mid (0, 1) (0, 2) hard (1, 3) (0, 2) Normality Frequency (0.000009, 0.002044) (16767.75, 33314) (0.000003, 0.000012) (14969.25, 29574.25) (0, 0.000004) (6568, 28380.5)

<!-- b000433 | prose | pages [19] -->
Word interval identification - EERIE 6.4

<!-- b000434 | prose | pages [19] -->
’EERIE’ belongs to the difficulty interval.

<!-- b000435 | furniture | pages [19] -->
18

<!-- b000436 | furniture | pages [20] -->
Team # 2314151

<!-- b000437 | furniture | pages [20] -->
Page 19 of 24

<!-- b000438 | prose | pages [20] -->
We bring the word ’EERIE’ into the Lasso regression prediction model built in Part 2 and get its average number of attempts 4.384952125887, which means it belongs to the difficult word. It is easy to find that its attributes of Number of duplicate, Maximum of repeats, Normality, and Frequency are all in the difficult range we have classified. Therefore, we believe that the word ’EERIE’ belongs to the difficult interval.

<!-- b000439 | prose | pages [20] -->
6.5

<!-- b000440 | heading | pages [20] -->
Model reliability analysis

<!-- b000441 | prose | pages [20] -->
In order to evaluate the accuracy of our classification model, we used 405 data from January 7, 2022, to February 16, 2023, that had been identified for validation. The validation process was as follows.

<!-- b000442 | prose | pages [20] -->
First, we calculated the average number of guesses for each word. We classified the average number of word guesses into different intervals based on the clustering results described in the previous section. Then, we counted each attribute of each letter to compare which level of difficulty interval was hit for each attribute. The difficulty with the highest number of hits is the difficulty identified by the feature. If the classification result is the same as the result of the word hit interval, our model is considered accurate. The algorithm is implemented as follows:

<!-- b000443 | prose | pages [20] -->
The accuracy of our model is calculated to be 91. 3649025%. For small-scale data classification, our model has high accuracy.

<!-- b000444 | furniture | pages [20] -->
19

<!-- b000445 | furniture | pages [21] -->
Team # 2314151

<!-- b000446 | furniture | pages [21] -->
Page 20 of 24

<!-- b000447 | prose | pages [21] -->
7 Interesting aspects of the data

<!-- b000448 | prose | pages [21] -->
• The relationship between the number of reported results and the percentage of scores reported in Hard Mode

<!-- b000449 | prose | pages [21] -->
We try to find some other interesting features of this dataset, but we do not know where to start. So we search Wordle on social media to get a specific view of this game. During this period, we suddenly found that most of the reported results about this game were from the first half of 2022, while in the second half of the year, this game saw a significant drop in popularity. Accordingly, we associate and plot the relationship among the number of reports from players, the percentage of scores reported in Hard Mode, and the date. Because the difference between the percentage in Hard Mode and the number of reported results is too large, we multiply the value of the percentage of scores reported in Hard Mode by 106 in order to make the relationship graph more obvious.

<!-- b000450 | caption | pages [21] -->
Figure 13: Hard mode percentage vs. Date vs. Num of reported

<!-- b000451 | prose | pages [21] -->
From the graph above we discover that as the number of reported results began to grow, the percentage in hard mode steadily increased. However, when the number of reported results peaked, the percentage in hard mode plummeted. We suppose that there was an influx of new players who were less familiar with Wordle and less likely to try the hard mode, which caused the percentage of hard mode to plummet. Over time, the number of daily reported results for Wordle has gradually decreased, but the percentage of hard modes has steadily increased. In response, we think Wordle has a loyal fan base that often plays Wordle and prefers hard mode. This indicates that the gaming ability of the enthusiastic fans is also slowly improving, and it also shows that this game helps to improve players’ English skills.

<!-- b000452 | prose | pages [21] -->
• The relationship among the average number of successes, number of reported results, and date for Wordle

<!-- b000453 | prose | pages [21] -->
Next, we analyze the relationship between the average number of successes, the total number of reports, and the date of Wordle. To make the scatter plot more visible, we multiplied the value of Average number of successes by 105.

<!-- b000454 | furniture | pages [21] -->
20

<!-- b000455 | furniture | pages [22] -->
Team # 2314151

<!-- b000456 | furniture | pages [22] -->
Page 21 of 24

<!-- b000457 | caption | pages [22] -->
Figure 14: Average number of successes vs. Date vs. Num of reported

<!-- b000458 | prose | pages [22] -->
As shown in the figure, the values of Average number of successes are mostly distributed between 4 and 5. This shows that the difficulty of the game remains almost constant, with almost every word being guessed 4-5 times. This supports our previous interesting finding that the game helps to improve players’ English and that the longer they play the game, the more willing they are to try the Hard Mode.

<!-- b000459 | prose | pages [22] -->
8

<!-- b000460 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000461 | prose | pages [22] -->
In Part two, we artificially specify the proportion of the test set(POT) as 20%, and the change of this value will affect the model’s training. The results of the sensitivity analysis are shown in Table 7.

<!-- b000462 | caption | pages [22] -->
Table 16: Sensitivity analysis

<!-- b000463 | prose | pages [22] -->
POT =0.1 POT =0.2 POT =0.15 POT =0.25 POT =0.3 0.87(1.16% ↑) Partial least squares Regression 0.86 0.93(8.14% ↑) 0.89(3.49% ↑) 0.97(12.79% ↑) 0.94(2.08% ↓) 0.96 Elastic Net Regression 0.95(1.04% ↓) 0.92(4.17% ↓) 0.91(5.21% ↓) 0.97(3.19% ↑) 0.94 Bayesian linear regression 1.01(7.45% ↑) 0.89(5.32% ↓) 0.96(2.13% ↑) 0.83(3.75% ↑) 0.80 Lasso Regression 0.84(5.00% ↑) 0.86(7.50% ↑) 0.92(15.00% ↑) 0.91(7.14% ↓) 0.98 Ridge regression 0.93(5.10% ↓) 0.93(5.10% ↓) 0.92(6.12% ↓) 0.92(3.37% ↑) 0.89 Quantile regression 0.82(7.87% ↓) 0.90(1.12% ↑) 1.05(17.98% ↑)

<!-- b000464 | prose | pages [22] -->
As shown in the results, by changing the proportion of the test set, the maximum rate of change is 10%, while the RMSE of the models are all less than 1.0, which proves that our model is not sensitive to the change of this parameter within the range of 0.5 times itself, and our model is robust and reliable.

<!-- b000465 | furniture | pages [22] -->
21

<!-- b000466 | furniture | pages [23] -->
Team # 2314151

<!-- b000467 | furniture | pages [23] -->
Page 22 of 24

<!-- b000468 | prose | pages [23] -->
9

<!-- b000469 | heading | pages [23] -->
Strengths and Weaknesses

<!-- b000470 | prose | pages [23] -->
9.1

<!-- b000471 | heading | pages [23] -->
Strength

<!-- b000472 | prose | pages [23] -->
• Prophet model provides excellent predictions for small data sets and adjusts the parameters quite freely, thus facilitating more accurate predictions of the number of reports we will have for future dates.

<!-- b000473 | prose | pages [23] -->
• Higher-order partial correlation analysis can control irrelevant variables for correlation analysis of a variable, which facilitates us to eliminate the influence between words and more accurately analyze the degree of influence of variables.

<!-- b000474 | prose | pages [23] -->
• Lasso regression model can perform well on small data while handling multiple classification tasks and being suitable for incremental training to make more accurate regression predictions on small data sets.

<!-- b000475 | prose | pages [23] -->
• Permutation importance can perform data disruption and rearrangement analysis on the fitted model to more accurately derive the contribution of each piece of data.

<!-- b000476 | prose | pages [23] -->
9.2

<!-- b000477 | heading | pages [23] -->
Weakness

<!-- b000478 | prose | pages [23] -->
• Multi-objective regression prediction runs long, and the solution results need simple manual screening.

<!-- b000479 | prose | pages [23] -->
10

<!-- b000480 | heading | pages [23] -->
Letter

<!-- b000481 | prose | pages [23] -->
To: Puzzle Editor of the New York Times From: Team 2314151 Date: February 20, 2023

<!-- b000482 | heading | pages [23] -->
Subject: The results of our team

<!-- b000483 | prose | pages [23] -->
Dear Puzzle Editor of the New York Times,

<!-- b000484 | prose | pages [23] -->
By building several models, we have completed an analysis of MCM’s statistics based on players’ participation in the Wordle puzzles that your website provides daily. We are honored to present you with the results of what we’ve analyzed.

<!-- b000485 | prose | pages [23] -->
Before building the model, we clarified and normalized the dataset you gave us and identified word attributes such as the number of repeated letters, number of vowel letters, number of consonant letters, commonness, and frequency. Next, I will describe the modeling solution process for you:

<!-- b000486 | prose | pages [23] -->
First, we considered the effects of trends, seasonality, and holidays and built a prophet-based time- series forecasting model to explain the daily variation in the number of reports and to predict the interval of the number of reported outcomes on March 1, 2023: [10355,18742]. We found that the number of reported outcomes increased steeply from January to early February 2022 and that the number of reports tended to be highest on Wednesdays and lowest on weekends during the week in terms of the variation in the number of reports.

<!-- b000487 | prose | pages [23] -->
In exploring the influence of the attributes of the words on the reports, we first used a correla- tion analysis algorithm to solve for each attribute, however, we found that their Pearson correlation

<!-- b000488 | furniture | pages [23] -->
22

<!-- b000489 | furniture | pages [24] -->
Team # 2314151

<!-- b000490 | furniture | pages [24] -->
Page 23 of 24

<!-- b000491 | prose | pages [24] -->
coefficients were all less than or approximately 0.1 and were uncorrelated. In order to overcome this association, we used a higher-order partial correlation analysis algorithm to perform correlation analy- sis on each attribute of the word while controlling for the interaction between the attributes of the word, and finally obtained the results we wanted: the number of vowel letters, the number of non-repeats, and the word commonness were negatively correlated, and the number of consonant letters and the number of non-repeats numbers is positively correlated.

<!-- b000492 | prose | pages [24] -->
Next, an optimized multi-objective regression prediction framework was developed to explore the effect of word attributes on the distribution of reported results. By feeding the data into the framework, a prediction model was selected that was most suitable for this dataset: the Lasso regression prediction model, which performed very well for the test set with a root mean square error of 0.8. Therefore, we established the Lasso regression prediction model to predict the reported results, and we first processed ’EERIE ’, the results of its attempt count distribution were obtained as (0, 4, 17, 34, 30, 13, 2).

<!-- b000493 | prose | pages [24] -->
Following this, we proposed an algorithm for ranking importance analysis to evaluate the established but this attribute, and finally found that the three attributes of number of consonant letters, number of vowel letters and frequency had a greater impact on the distribution of reported results with impact factors of 4.226, 3.993, and 1.253, respectively.

<!-- b000494 | prose | pages [24] -->
Then, we used the established Lasso regression prediction model to distribute the reported results for all 5-letter words in the dictionary database, and then used the K-Means algorithm to classify the above results into three categories of difficulty: high (≥4.37) medium (4.13-4.37) low (< 4.13), and found that Number of duplicate, Maximum of repeats, Prevalence, and Frequency were found to differ significantly in different classifications, and the intervals for each attribute were divided.

<!-- b000495 | prose | pages [24] -->
Then we bring ’EERIE’ into the interval division model, and since all its attributes hit the interval value of difficulty, its degree of being guessed is difficult, and its average number of attempts matches the difficulty interval division predicted using the Lasso regression model. Therefore, the degree of ’EERIE’ being guessed is difficult. Meanwhile, we obtained the accuracy of our model by matching the attribute intervals for different difficulty words, which is 91.36%, and we can see that our model is robust.

<!-- b000496 | prose | pages [24] -->
Finally, we performed a sensitivity analysis of the model, as shown in the results, by changing the proportion of the test set, the maximum rate of change is 10%, while the RMSE of the models are all less than 1.0, which proves that our model is not sensitive to the change of this parameter within the range of 0.5 times itself, and our model is robust and reliable. In addition, the study of the data set has revealed the declining popularity of Wordle and the increasing proportion of difficult mode challenges, and offers two suggestions for restoring the popularity of the game:

<!-- b000497 | prose | pages [24] -->
• Introduced online multiplayer challenge mode, you can invite friends to challenge together, so as to attract more people to participate.

<!-- b000498 | prose | pages [24] -->
• Introducing Kids Mode, parents can let their children use this software to work on their English skills, playing and learning at the same time.

<!-- b000499 | prose | pages [24] -->
So that’s the summary of our research. We sincerely hope that it can provide you with useful information and look forward to your reply. Thank you!

<!-- b000500 | prose | pages [24] -->
Yours sincerely,

<!-- b000501 | furniture | pages [24] -->
Team # 2314151

<!-- b000502 | furniture | pages [24] -->
23

<!-- b000503 | furniture | pages [25] -->
Team # 2314151

<!-- b000504 | furniture | pages [25] -->
Page 24 of 24

<!-- b000505 | heading | pages [25] -->
References

<!-- b000506 | references | pages [25] -->
[1] Benton J. Anderson and Jesse G. Meyer. Finding the optimal human strategy for wordle using

<!-- b000507 | references | pages [25] -->
maximum correct letter probabilities and reinforcement learning, 2022.

<!-- b000508 | references | pages [25] -->
[2] Tarun Kumar. Solution of linear and non linear regression problem by k nearest neighbour

<!-- b000509 | references | pages [25] -->
approach: By using three sigma rule. In 2015 IEEE International Conference on Computational

<!-- b000510 | references | pages [25] -->
Intelligence Communication Technology, pages 197–201, 2015.

<!-- b000511 | references | pages [25] -->
[3] Michal S Gal and Daniel L Rubinfeld. Data standardization. NYUL Rev., 94:737, 2019.

<!-- b000512 | references | pages [25] -->
[4] Sean J Taylor and Benjamin Letham. Forecasting at scale. The American Statistician, 72(1):37–45,

<!-- b000513 | references | pages [25] -->
2018.

<!-- b000514 | references | pages [25] -->
[5] Qibin Zhao, Cesar F. Caiafa, Danilo P. Mandic, Zenas C. Chao, Yasuo Nagasaka, Naotaka Fujii,

<!-- b000515 | references | pages [25] -->
Liqing Zhang, and Andrzej Cichocki. Higher order partial least squares (hopls): A generalized

<!-- b000516 | references | pages [25] -->
multilinear regression method. IEEE Transactions on Pattern Analysis and Machine Intelligence,

<!-- b000517 | references | pages [25] -->
35(7):1660–1673, 2013.

<!-- b000518 | references | pages [25] -->
[6] Ertunga C ¨Ozelkan and Lucien Duckstein. Multi-objective fuzzy regression: a general framework.

<!-- b000519 | references | pages [25] -->
Computers & Operations Research, 27(7-8):635–652, 2000.

<!-- b000520 | references | pages [25] -->
[7] Mark Harman. Making the case for morto: Multi objective regression test optimization. In

<!-- b000521 | references | pages [25] -->
2011 IEEE Fourth International Conference on Software Testing, Verification and Validation

<!-- b000522 | references | pages [25] -->
Workshops, pages 111–114, 2011.

<!-- b000523 | references | pages [25] -->
[8] Aristidis Likas, Nikos Vlassis, and Jakob J Verbeek. The global k-means clustering algorithm.

<!-- b000524 | references | pages [25] -->
Pattern recognition, 36(2):451–461, 2003.

<!-- b000525 | references | pages [25] -->
[9] John A Hartigan and Manchek A Wong. Algorithm as 136: A k-means clustering algorithm.

<!-- b000526 | references | pages [25] -->
Journal of the royal statistical society. series c (applied statistics), 28(1):100–108, 1979.

<!-- b000527 | references | pages [25] -->
[10] Greg Hamerly and Charles Elkan. Learning the k in k-means. Advances in neural information

<!-- b000528 | references | pages [25] -->
processing systems, 16, 2003.

<!-- b000529 | furniture | pages [25] -->
24
