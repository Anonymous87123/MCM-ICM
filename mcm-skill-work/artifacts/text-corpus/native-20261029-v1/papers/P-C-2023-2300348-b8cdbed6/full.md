# P-C-2023-2300348-b8cdbed6

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
2300348

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Revitalizing a Classic Game: Uncovering the Secrets of

<!-- b000009 | heading | pages [1] -->
Wordle through Data Analysis

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
In the digital era, language is often conveyed through abbreviations, emojis, and voice messages. However, the Wordle game, provided by the New York Times, offers a chance to return to the basics of language. Thus, we conducted a data analysis of the results yielded by Wordle.

<!-- b000012 | prose | pages [1] -->
Firstly, we established a GRU Prediction Model to predict the number of reported results on March 1, 2023. The model uses the effective Gated Recurrent Unit (GRU) algorithm. Therefore, predictions made by the training set to the testing have the relative error rate of 2.1569%, and the relative RESE of 6.4957%, indicating a good accuracy of the model predictions. The predicted interval for the number of reported results on March 1, 2023 is 20367 ± 2.01569%.

<!-- b000013 | prose | pages [1] -->
Secondly, we conducted a data analysis on the attributes of words and score defined by the percentage of scores. Then, we defined four attributes of the words: word frequency, sum of letter frequencies,repetition patterns of letters(2/3 or none), and main part of speech. For the first two, we performed regression analysis with the variable "score". The Pearson correlation coefficient between fword and score is -0.3165, and fletter and score-0.4005.rep and pos can be used to categorize the words.The box plot results showed that the Median difference of the box plot for rep was 0.13004, while pos was only 0.05973.Therefore, we believe that fword, fletter, and rep can affect the percentage of scores, while pos can not.

<!-- b000014 | prose | pages [1] -->
Thirdly, we have developed GSRF Prediction Model to predict the percentages of 1 to X for EERIE on March 1, 2023. The Grid-Search Random Forest (GSRF) algorithm is an improved random forest algorithm by using the best combination of hyperparameters. We selected the three parameters, fword, fletter, and rep as inputs for the model. The model’s training results show a MSE of 20.70641 and a MAE of 3.24388,indicating good predictive performance.(Table 10)

<!-- b000015 | heading | pages [1] -->
The predicted results for EERIE are (1,7,23,30,23,13,3). In addition, we conducted sensitivity

<!-- b000016 | prose | pages [1] -->
analysis by adding Gaussian noise to fword and fletter separately, and the results showed that the model has low sensitivity and is thus highly stable.

<!-- b000017 | prose | pages [1] -->
Fourthly, Difficulty Rate Classification Model using the K-Means++are conducted. We first defined the difficulty date δ of each word first. The difficulty rate of EERIE is 0.35916 by predicted distribution. Then, we use K-Means++, to analyze the δ of each word and obtained five levels of difficulty (Table11). EERIE was classified into the third level. Finally, we compared the model’s classification with the manul difficulty ratings for a subset of sampled words and achieved a match rate of 93.33%, confirming the accuracy of the model.

<!-- b000018 | prose | pages [1] -->
Finally, we explored two other data features.Afterwards, a letter supported by our stable models has been written for the Puzzle Editor of the New York Times.

<!-- b000019 | keywords | pages [1] -->
Keywords: GRU;Regression Analysis;Box Plot Analysis;GSRF;K-Means++

<!-- b000020 | furniture | pages [2] -->
Team # 2300348

<!-- b000021 | furniture | pages [2] -->
Page 1 of 25

<!-- b000022 | heading | pages [2] -->
Contents

<!-- b000023 | contents | pages [2] -->
1

<!-- b000024 | heading | pages [2] -->
Introduction

<!-- b000025 | prose | pages [2] -->
3

<!-- b000026 | prose | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000027 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3

<!-- b000028 | prose | pages [2] -->
Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 4

<!-- b000029 | prose | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000030 | prose | pages [2] -->
2

<!-- b000031 | heading | pages [2] -->
Assumptions

<!-- b000032 | prose | pages [2] -->
3

<!-- b000033 | heading | pages [2] -->
Notations

<!-- b000034 | prose | pages [2] -->
4

<!-- b000035 | heading | pages [2] -->
GRU Prediction Model

<!-- b000036 | prose | pages [2] -->
4

<!-- b000037 | prose | pages [2] -->
5

<!-- b000038 | prose | pages [2] -->
5

<!-- b000039 | prose | pages [2] -->
5

<!-- b000040 | prose | pages [2] -->
Description of GRU Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 6

<!-- b000041 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Prediction on March 1,2023 7

<!-- b000042 | prose | pages [2] -->
Relationship of Word Attributes and Scores from Percentage 5 8

<!-- b000043 | prose | pages [2] -->
score Defined by Percentage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 9

<!-- b000044 | prose | pages [2] -->
Regression Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 9

<!-- b000045 | prose | pages [2] -->
fword:Word Frequency . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1

<!-- b000046 | prose | pages [2] -->
fLetter:Letter Frequency

<!-- b000047 | prose | pages [2] -->
9

<!-- b000048 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.2 10

<!-- b000049 | prose | pages [2] -->
Box Plot Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000050 | prose | pages [2] -->
rep:Repetition of Letter

<!-- b000051 | prose | pages [2] -->
11

<!-- b000052 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.1 11

<!-- b000053 | prose | pages [2] -->
pos:Part of Speech . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.2

<!-- b000054 | prose | pages [2] -->
6

<!-- b000055 | heading | pages [2] -->
GSRF Prediction Model

<!-- b000056 | prose | pages [2] -->
12

<!-- b000057 | prose | pages [2] -->
13

<!-- b000058 | prose | pages [2] -->
Description of GSRF Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 13

<!-- b000059 | prose | pages [2] -->
Prediction for EERIE on March 1,2023 . . . . . . . . . . . . . . . . . . . . . . . . 6.2 14

<!-- b000060 | prose | pages [2] -->
Prediction evaluation analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3 15

<!-- b000061 | heading | pages [2] -->
Difficulty Rate Classification Model by K-Means++

<!-- b000062 | prose | pages [2] -->
7 16

<!-- b000063 | prose | pages [2] -->
δ: Difficulty Rate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 16

<!-- b000064 | furniture | pages [3] -->
Team # 2300348

<!-- b000065 | furniture | pages [3] -->
Page 2 of 25

<!-- b000066 | prose | pages [3] -->
K-Means++ Clustering Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 16

<!-- b000067 | prose | pages [3] -->
Difficulty classification for EERIE . . . . . . . . . . . . . . . . . . . . . . . . . . 7.3 17

<!-- b000068 | prose | pages [3] -->
Accuracy Discussion of Classification Model 7.4

<!-- b000069 | prose | pages [3] -->
8 Interesting Features of Data

<!-- b000070 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000071 | prose | pages [3] -->
18

<!-- b000072 | prose | pages [3] -->
19

<!-- b000073 | prose | pages [3] -->
Feature 1:Relationship of Word Attributes and Hard Mode Percentage . . . . . . . 8.1 19

<!-- b000074 | prose | pages [3] -->
Feature 2:Why "PARER" Has The Most "Hellish" Level of Difficulty . . . . . . . . 8.2

<!-- b000075 | prose | pages [3] -->
9

<!-- b000076 | heading | pages [3] -->
Model Sensitivity Analysis

<!-- b000077 | prose | pages [3] -->
20

<!-- b000078 | prose | pages [3] -->
21

<!-- b000079 | prose | pages [3] -->
Sensitivity Analysis for fword in GSRF Prediction Model . . . . . . . . . . . . . . 9.1 21

<!-- b000080 | prose | pages [3] -->
Sensitivity Analysis for fletter in GSRF Prediction Model . . . . . . . . . . . . . . 9.2

<!-- b000081 | heading | pages [3] -->
10 Model Evaluation and Further Discussion

<!-- b000082 | prose | pages [3] -->
21

<!-- b000083 | prose | pages [3] -->
22

<!-- b000084 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.1 Strengths 22

<!-- b000085 | prose | pages [3] -->
10.2 Weaknesses And Further Discussion . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | heading | pages [3] -->
11 Letter

<!-- b000087 | prose | pages [3] -->
A Samples

<!-- b000088 | prose | pages [3] -->
B Difficluty Rate of Partial Words

<!-- b000089 | prose | pages [3] -->
22

<!-- b000090 | prose | pages [3] -->
24

<!-- b000091 | prose | pages [3] -->
25

<!-- b000092 | prose | pages [3] -->
25

<!-- b000093 | furniture | pages [4] -->
Team # 2300348

<!-- b000094 | furniture | pages [4] -->
Page 3 of 25

<!-- b000095 | prose | pages [4] -->
1

<!-- b000096 | heading | pages [4] -->
Introduction

<!-- b000097 | prose | pages [4] -->
1.1 Problem Background

<!-- b000098 | prose | pages [4] -->
In this digital age, we have become accustomed to using abbreviations, emojis, and voice messages to communicate. However, sometimes these modes of communication can strip away the beauty and depth of language itself. But a word-guessing game, Wordle allows us to return to the essence of language in a fresh way. By feeling the rhythm and meaning of each letter and word, we can gain a deeper understanding of the magic of language and appreciate its inherent charm.

<!-- b000099 | prose | pages [4] -->
Wordle is a popular daily puzzle that the New York Times currently provides, which challenges players to guess a secret five-letter word in six or fewer tries. At the beginning of each round, the system randomly selects a word, and the player must use deduction and logic to guess the answer within the allotted number of guesses. With each guess, the system indicates which letters appear in the word and whether they are in the correct position. What’s more, players can play in “Hard Mode”, which requires that once a player correctly guesses a letter in the answer, they must continue to use that letter in all subsequent guesses.

<!-- b000100 | prose | pages [4] -->
Numerous users, although not all, share their scores on Twitter. Wordle Stats, a Twitter robot developed by Benjamin Leis, can be used to track and analyze daily score reports of Wordle. By tracking and analyzing the daily data reports from Wordle Stats, we may be able to improve our word-guessing skills and gain a better understanding of the patterns and usage of the English language.

<!-- b000101 | caption | pages [4] -->
Figure 1: Wordle[2]

<!-- b000102 | prose | pages [4] -->
1.2 Restatement of the Problem

<!-- b000103 | prose | pages [4] -->
We need to analyze the data provided by the New York Times on Wordle and answer the following questions:

<!-- b000104 | prose | pages [4] -->
1. Develop a prediction model to forecast the number of reported results for a future day and provide a prediction interval.

<!-- b000105 | prose | pages [4] -->
2. Analyze whether word attributes have an impact on the percentage of scores reported that were played in Hard Mode, and how they impact.

<!-- b000106 | prose | pages [4] -->
3. Build another prediction model to forecast the percentages of (1, 2, 3, 4, 5, 6, X), and use EERIE on March 1, 2023 as an example to make specific predictions. Model evaluation is also required.

<!-- b000107 | furniture | pages [5] -->
Team # 2300348

<!-- b000108 | furniture | pages [5] -->
Page 4 of 25

<!-- b000109 | prose | pages [5] -->
4. Develop a classification model to classify the difficulty level of words and obtain the difficulty level of the word "EERIE". Model evaluation is also required.

<!-- b000110 | prose | pages [5] -->
5. Explore other possible interactions in the data and see if any interesting features can be found.

<!-- b000111 | prose | pages [5] -->
1.3 Data Cleaning

<!-- b000112 | prose | pages [5] -->
Observing the provided data, some problems and corresponding processing are found as follows.

<!-- b000113 | prose | pages [5] -->
Referencing the Wordle Status and we discovered that there were some erroneous data in the attachment. These included incorrect word lengths, spelling errors, and incorrect values in Number of reported results, among others. For instance, the word at 314 was mistakenly written as "tash". Additionally, the Number of reported results at 529 was erroneously recorded as 2569. To address these issues, we conducted data cleaning to minimize errors , and to enhance the quality and accuracy of our data . The following are the results of our data cleaning process.

<!-- b000114 | prose | pages [5] -->
tash(314) Original data marxh(473)

<!-- b000115 | prose | pages [5] -->
Data after cleaning marsh trash

<!-- b000116 | prose | pages [5] -->
clen(525) rprobe(545) 2569(529)

<!-- b000117 | prose | pages [5] -->
clean probe 25569

<!-- b000118 | caption | pages [5] -->
Table 1: Data cleaning

<!-- b000119 | prose | pages [5] -->
During our data inspection, we identified instances where the sum of the proportion of attempts for certain days did not equal 100% due to statistical errors. To address this issue, we recalculated the proportions for each day so that the sum would be exactly 100%. By doing so, we aimed to reduce errors associated with the same variable on different days and to improve the accuracy of our model.Our processing result is PX

<!-- b000120 | prose | pages [5] -->
i=1 pi = 100%.

<!-- b000121 | prose | pages [5] -->
1.4 Our Work

<!-- b000122 | caption | pages [5] -->
Figure 2: Our work

<!-- b000123 | furniture | pages [6] -->
Team # 2300348

<!-- b000124 | prose | pages [6] -->
2

<!-- b000125 | heading | pages [6] -->
Assumptions

<!-- b000126 | furniture | pages [6] -->
Page 5 of 25

<!-- b000127 | prose | pages [6] -->
To simplify our modeling, we make the following assumptions:

<!-- b000128 | prose | pages [6] -->
• Assumption1 The percentage of scores reported that were played in Hard Mode can be represented by the percentages of (1, 2, 3, 4, 5, 6, X). Because Wordle status had previously compiled the values of (1, 2, 3, 4, 5, 6, X) for both the overall and hard mode in Wordle 207, we found that the two sets of values differed by only 1%[1].This is beneficial for our subsequent analysis.

<!-- b000129 | prose | pages [6] -->
• Assumption2 No matter how many tries a player takes, the likelihood of sharing their Wordle results on Twitter is equal. This assumption can lead to more accurate data analysis.

<!-- b000130 | prose | pages [6] -->
• Assumption3 Every player does not know the answer before playing Wordle and does not cheat during the gameplay. This ensures that the percentage of scores is both objective and accurate.

<!-- b000131 | prose | pages [6] -->
3

<!-- b000132 | heading | pages [6] -->
Notations

<!-- b000133 | prose | pages [6] -->
Symbol

<!-- b000134 | prose | pages [6] -->
score

<!-- b000135 | prose | pages [6] -->
Decription

<!-- b000136 | prose | pages [6] -->
the combination of the percentage of scores

<!-- b000137 | prose | pages [6] -->
fword

<!-- b000138 | prose | pages [6] -->
fletter

<!-- b000139 | prose | pages [6] -->
rep

<!-- b000140 | prose | pages [6] -->
pos

<!-- b000141 | prose | pages [6] -->
σ

<!-- b000142 | prose | pages [6] -->
MSE

<!-- b000143 | prose | pages [6] -->
MAE

<!-- b000144 | prose | pages [6] -->
d

<!-- b000145 | prose | pages [6] -->
SSE

<!-- b000146 | prose | pages [6] -->
the word frequency

<!-- b000147 | prose | pages [6] -->
the letter frequency

<!-- b000148 | prose | pages [6] -->
the repetition of word

<!-- b000149 | prose | pages [6] -->
the part of speech of word

<!-- b000150 | prose | pages [6] -->
the difficulty rate

<!-- b000151 | prose | pages [6] -->
the Mean Squared Error

<!-- b000152 | prose | pages [6] -->
the Mean Absolute Error

<!-- b000153 | prose | pages [6] -->
the Euclidean distance

<!-- b000154 | prose | pages [6] -->
the Sum of Squared Errors

<!-- b000155 | caption | pages [6] -->
Table 2: Key notations used in this paper

<!-- b000156 | prose | pages [6] -->
4

<!-- b000157 | heading | pages [6] -->
GRU Prediction Model

<!-- b000158 | prose | pages [6] -->
The number of reported results varies from day to day, and analyzing the changes in this data can to some extent reflect the trends of active Wordle users. By studying historical data and trends, it may even be possible to make informed predictions about future reported results. So in this

<!-- b000159 | furniture | pages [7] -->
Team # 2300348

<!-- b000160 | furniture | pages [7] -->
Page 6 of 25

<!-- b000161 | prose | pages [7] -->
section, we applied the Gated Recurrent Unit(GRU) algorithm to perform machine learning on the provided number of reported results, and ultimately made a prediction for the number of reported results on March 1, 2023.

<!-- b000162 | prose | pages [7] -->
4.1

<!-- b000163 | heading | pages [7] -->
Description of GRU Algorithm

<!-- b000164 | prose | pages [7] -->
GRU (Gated Recurrent Unit) is a type of recurrent neural network (RNN) that is commonly used for time series analysis. It has similar properties to the LSTM (Long Short-Term Memory) architecture but is generally faster to compute.

<!-- b000165 | prose | pages [7] -->
The main idea behind the GRU architecture is to have two gates, a reset gate and an update gate, which control the flow of information through the network. The reset gate decides how much of the previous hidden state should be forgotten, while the update gate decides how much of the new input should be added to the current hidden state.

<!-- b000166 | caption | pages [7] -->
Figure 3: An Overview of the Algorithm Flow of GRU

<!-- b000167 | prose | pages [7] -->
The update equations of GRU are as follows:

<!-- b000168 | prose | pages [7] -->
rt = σ (Wirxt + bir + Whrht−1 + bhr) zt = σ (Wizxt + biz + Whzht−1 + bhz)

<!-- b000169 | prose | pages [7] -->
(1)

<!-- b000170 | prose | pages [7] -->
˜ht = tanh (Winxt + bin + rt ∗(Whnht−1 + bhn))

<!-- b000171 | prose | pages [7] -->
ht = (1 −zt) ∗˜ht + zt ∗h(t−1)

<!-- b000172 | prose | pages [7] -->
where:

<!-- b000173 | prose | pages [7] -->
Symbol

<!-- b000174 | prose | pages [7] -->
zt

<!-- b000175 | prose | pages [7] -->
rt

<!-- b000176 | prose | pages [7] -->
ht

<!-- b000177 | prose | pages [7] -->
Decription

<!-- b000178 | prose | pages [7] -->
the update gate

<!-- b000179 | prose | pages [7] -->
the reset gate

<!-- b000180 | prose | pages [7] -->
the hidden state at time t

<!-- b000181 | furniture | pages [8] -->
Team # 2300348

<!-- b000182 | prose | pages [8] -->
Symbol

<!-- b000183 | furniture | pages [8] -->
Page 7 of 25

<!-- b000184 | prose | pages [8] -->
Decription

<!-- b000185 | prose | pages [8] -->
the hidden state at time t −1 or at time 0 ht−1

<!-- b000186 | prose | pages [8] -->
˜ht

<!-- b000187 | prose | pages [8] -->
σ

<!-- b000188 | prose | pages [8] -->
∗

<!-- b000189 | prose | pages [8] -->
xt

<!-- b000190 | prose | pages [8] -->
Wir, Whr, Wiz, Whz, Win, Whn

<!-- b000191 | prose | pages [8] -->
the new candidate hidden state

<!-- b000192 | prose | pages [8] -->
the sigmoid function

<!-- b000193 | prose | pages [8] -->
the Hadamard product

<!-- b000194 | prose | pages [8] -->
the input

<!-- b000195 | prose | pages [8] -->
the parameters that need to be trained

<!-- b000196 | prose | pages [8] -->
bir, bhr, biz, bhz, bin, bhn the parameters that need to be trained

<!-- b000197 | caption | pages [8] -->
Table 3: Notations used in Equation1

<!-- b000198 | prose | pages [8] -->
In this approach, the historical data of a time series is fed into a GRU model to learn the patterns in the sequence, which can then be used to predict future data points.

<!-- b000199 | prose | pages [8] -->
4.2 Prediction on March 1,2023

<!-- b000200 | prose | pages [8] -->
With the support of Python’s extensive library, we have opted to use the GRU model provided by PyTorch. PyTorch is a machine learning library based on Python, and its distinctive feature is dynamic computational graph, which is different from static computational graphs. The dynamic computational graph can be changed during runtime, which means the model can be modified according to our needs. This is very useful when dealing with variable-length sequence data and is well-suited for predicting the number of reported results that we need to predict. In PyTorch, we can utilize the torch.nn.GRU[3] class to easily construct and train GRU models, as well as use the model for making predictions.

<!-- b000201 | prose | pages [8] -->
We used 80% of the daily "Number of reported results" time series data from January 7, 2022 to December 31, 2022 as the training set and the remaining 20% as the test set for our GRU model. The visualization of the prediction results on the test set is shown in Figure4:

<!-- b000202 | caption | pages [8] -->
Figure 4: The prediction results on the test set."Deviation" represents relative error rate of between

<!-- b000203 | prose | pages [8] -->
prediction data and original data.

<!-- b000204 | furniture | pages [9] -->
Team # 2300348

<!-- b000205 | furniture | pages [9] -->
Page 8 of 25

<!-- b000206 | prose | pages [9] -->
From Figure 3, it can be seen that the average deviation is around 0.06, indicating that the prediction data deviate from the original data by only about 6%. At the same time, an interesting phenomenon is observed: the deviation for December 25, 2022, Christmas Day, is close to 50%, which is due to a sharp drop in the number of reported results on this day in the original data. It is easy to associate this with the fact that it is a major holiday. Such a result belongs to the outlier in time series analysis, and there is enough reason to remove this value and calculate the mean and root-mean-square error(RMSE) of the remaining data. And the calculation method for RMSE is as follows:

<!-- b000207 | prose | pages [9] -->
rPn

<!-- b000208 | prose | pages [9] -->
RMSE =

<!-- b000209 | prose | pages [9] -->
i=1(xt −ˆxt)2

<!-- b000210 | prose | pages [9] -->
(2) n

<!-- b000211 | prose | pages [9] -->
As shown in Table 2 below, the relative error rate between the prediction data and the original data is 2.1569%, indicating a small deviation between the two values. Meanwhile, the relative RMSE is calculated by dividing the RMSE by the original data, and in statistics, an error is considered small when this value is less than 10%. Therefore, it can be concluded that the GRU model has good predictive performance for the number of reported results, and we select the relative error rate of 2.1569% as the error interval for model prediction.

<!-- b000212 | prose | pages [9] -->
¯ˆxt ¯xt Relative error

<!-- b000213 | prose | pages [9] -->
24956.1667 25494.4569 538.29019

<!-- b000214 | prose | pages [9] -->
Relative error rate RMSE Relative RESE

<!-- b000215 | prose | pages [9] -->
2.1569% 1621.0881 6.4957%

<!-- b000216 | caption | pages [9] -->
Table 4: Statistical analysis of prediction data and original data.

<!-- b000217 | prose | pages [9] -->
By leveraging the pre-trained GRU model, we can make predictions for the following 60 days and obtain a forecast interval for the number of reported results on March 1, 2023:

<!-- b000218 | prose | pages [9] -->
xMarch1,2023 = 20367 ± 2.01569%

<!-- b000219 | prose | pages [9] -->
Relationship of Word Attributes and Scores from Percentage 5

<!-- b000220 | prose | pages [9] -->
In this section, we conducted a data analysis on four attributes of words and score which is derived from the percentage of scores. Through regression analysis, we found that word frequency and letter frequency of words are linearly correlated with score. Through boxplot analysis, we found that score of words with different letter repetition patterns has some differences, while the score of words with different parts of speech does not show significant differences. The overview of the results are shown in Figure5

<!-- b000221 | furniture | pages [10] -->
Team # 2300348

<!-- b000222 | furniture | pages [10] -->
Page 9 of 25

<!-- b000223 | caption | pages [10] -->
Figure 5: The overview of the results in Section 4

<!-- b000224 | prose | pages [10] -->
score Defined by Percentage 5.1

<!-- b000225 | prose | pages [10] -->
The percentage of daily attempts is the percentage of scores on that day.

<!-- b000226 | prose | pages [10] -->
However, when investigating the relationship between word attributes and percentages of scores, it is difficult and not conducive to analysis the relationship between a word attribute and the distribution of the percentage of scores composed of seven numbers. Therefore, we processed the seven percentage values into a single number, defining it as the score.

<!-- b000227 | prose | pages [10] -->
score is composed of two parts. One part is the weighted average of tris from 1 to 6, and the other part is the percentage of "X". The reason for considering the percentage of "X" is that Wordle allows only one attempt per day, so the percentage of "X" actually represents the failure rate of guessing on that day, which cannot be ignored. However, since "X" does not have a specific number of tries, it cannot participate in the calculation of the weighted average, so we have divided the score into two parts and assigned weights to them using the Entropy Weighting Method.score is defined as follows:

<!-- b000228 | prose | pages [10] -->
6 X

<!-- b000229 | prose | pages [10] -->
score = ω1 ∗

<!-- b000230 | prose | pages [10] -->
i ∗pi + ω2 ∗pX (3)

<!-- b000231 | prose | pages [10] -->
i=1

<!-- b000232 | prose | pages [10] -->
where:

<!-- b000233 | prose | pages [10] -->
• pi denotes the percentage of i tries(try) and i ∈{1, 2, 3, 4, 5, 6, X}

<!-- b000234 | prose | pages [10] -->
• ω1 and ω2 denote the weights of two parts of score respectively. And we set ω1 as 0.5 and ω2 as 0.5 by Entropy Weighting Method.

<!-- b000235 | prose | pages [10] -->
5.2 Regression Analysis

<!-- b000236 | prose | pages [10] -->
fword:Word Frequency 5.2.1

<!-- b000237 | prose | pages [10] -->
When attempting Wordle puzzles, words that are more commonly used in everyday language are often easier for people to recall, such as "study" and "train." Therefore, when the solution word has a high frequency of use, it is likely that the percentage distribution of tries will be skewed towards fewer tries, leading to a decrease in the value of score. To address this issue, we first used

<!-- b000238 | furniture | pages [11] -->
Team # 2300348

<!-- b000239 | furniture | pages [11] -->
Page 10 of 25

<!-- b000240 | prose | pages [11] -->
a combination of website[4] and Python to obtain reliable usage frequencies fword for each word. Then, we conducted regression analyses on both the fword and score.

<!-- b000241 | prose | pages [11] -->
The regression analysis results of word frequency and score are shown in Figure6(a) and Table3. The Pearson correlation coefficient is -0.3165, and the Spearman correlation coefficient is -0.2956, indicating a certain linear correlation between word frequency and score. Also, by observing the scatter plot in Figure6(a), it can be seen that there is no data distribution in the lower left and upper right corners of the image. This suggests that situations where a word has a high frequency but is difficult to guess and thus results in a low score, as well as situations where a word has a low frequency but is easy to guess and thus results in a high score, are unlikely to occur. Therefore, it is reasonable to conclude that there is a certain linear correlation between word frequency and score.

<!-- b000242 | prose | pages [11] -->
(a) Word frequency (b) Letter frequency

<!-- b000243 | caption | pages [11] -->
Figure 6: Regression analysis between word attributes and score

<!-- b000244 | prose | pages [11] -->
Regression with score

<!-- b000245 | prose | pages [11] -->
Word frequency

<!-- b000246 | prose | pages [11] -->
Letter frequency

<!-- b000247 | prose | pages [11] -->
Pearson Spearman

<!-- b000248 | prose | pages [11] -->
-0.3165 -0.3256

<!-- b000249 | prose | pages [11] -->
-0.4238 -0.4005

<!-- b000250 | caption | pages [11] -->
Table 5: Regression analysis between word attributes and score

<!-- b000251 | prose | pages [11] -->
fLetter:Letter Frequency 5.2.2

<!-- b000252 | prose | pages [11] -->
Each letter has its own usage frequency. When Wordle players use words with higher letter frequencies for guessing, they may have a higher chance of hitting the letters in the answer and thus receive more clues, reducing the number of tries.

<!-- b000253 | prose | pages [11] -->
Letter frequency,fLetter is obtained by adding up the usage frequency of each letter in the words. The data on letter frequency is obtained from the Google Books Ngram Viewer[4], which includes a corpus of books and other publications from 1500 to 2008 with high reliability. For example,

<!-- b000254 | furniture | pages [12] -->
Team # 2300348

<!-- b000255 | furniture | pages [12] -->
Page 11 of 25

<!-- b000256 | prose | pages [12] -->
the frequency of the letter "e" is 11.1607%, while the frequency of the letter "z" is only 0.0772%. fLetter is defined as follows:

<!-- b000257 | prose | pages [12] -->
fLetter =

<!-- b000258 | prose | pages [12] -->
5 X

<!-- b000259 | prose | pages [12] -->
fa,b,c...

<!-- b000260 | prose | pages [12] -->
(4) 1

<!-- b000261 | prose | pages [12] -->
We conducted a regression analysis between fLetter and score, similar to word frequency. The regression analysis results of letter frequency and score are shown in Figure6(b) and Table3. The Pearson correlation coefficient is -0.4238, and the Spearman correlation coefficient is -0.4005, indicating a certain linear correlation between letter frequency and score(even more than word frequency). Also, by observing the scatter plot in Figure6(b), it can be seen that there is no data distribution in the lower left and upper right corners of the image. This also suggests that situations where a word has a high frequency but is difficult to guess and thus results in a low score, as well as situations where a word has a low frequency but is easy to guess and thus results in a high score, are unlikely to occur. Therefore, it is reasonable to conclude that there is a certain linear correlation between letter frequency and score.

<!-- b000262 | prose | pages [12] -->
5.3 Box Plot Analysis

<!-- b000263 | prose | pages [12] -->
rep:Repetition of Letter 5.3.1

<!-- b000264 | prose | pages [12] -->
When there are repeated letters in the answer word, there may be a greater chance of hitting the letter when guessing and obtaining a hint, reducing the number of attempts, given a fixed word length. Analyzing the words from January 7, 2022 to December 31, 2022, we found that there are cases where a letter was repeated twice or three times(very few cases) in a word. Therefore, we divided the words into two categories: with or without repeated letters. We wanted to know if there was a significant difference in the score of words with and without repeated letters. To this end, we used box plot analysis:

<!-- b000265 | prose | pages [12] -->
(a) Boxplot of repetition (b) Density of repetition

<!-- b000266 | caption | pages [12] -->
Figure 7: Boxplot analysis between Repetition of Letter and score

<!-- b000267 | furniture | pages [13] -->
Team # 2300348

<!-- b000268 | furniture | pages [13] -->
Page 12 of 25

<!-- b000269 | prose | pages [13] -->
Box length difference Median difference

<!-- b000270 | prose | pages [13] -->
0.130037 0.00556

<!-- b000271 | prose | pages [13] -->
Number difference of outliers

<!-- b000272 | prose | pages [13] -->
2

<!-- b000273 | caption | pages [13] -->
Table 6: Boxplot analysis between Repetition of Letter and score

<!-- b000274 | prose | pages [13] -->
From Figure7(a) and Table6, the median difference was 0.130037 and the box length difference was 0.00556. From Figure7(b), it can be seen that there is a significant difference in the distribution of the two categories of data. Therefore, we believe that there is a certain difference in the score situation between words with and without repeated letters.

<!-- b000275 | prose | pages [13] -->
pos:Part of Speech 5.3.2

<!-- b000276 | prose | pages [13] -->
Part of speech(POS) is also an important attribute of a word. We are interested in whether there are differences in score among words with different POS.

<!-- b000277 | prose | pages [13] -->
We used the popular Python natural language processing toolkit Natural Language Toolkit[5], which contains various text processing and language analysis tools, including Part-of-Speech Tagging. Using this tool, we performed Part-of-Speech Tagging on the words from January 7, 2022 to December 31, 2022. Words were mainly divided into four categories: Nouns, Adjectives, Adverbs, and Verbs. Subsequently, we conducted a box plot analysis of the "score" of these four types of words:

<!-- b000278 | prose | pages [13] -->
(a) Boxplot of POS (b) Density of POS

<!-- b000279 | caption | pages [13] -->
Figure 8: Boxplot analysis between POS and score

<!-- b000280 | prose | pages [13] -->
Median difference2 Median difference1 Median difference3

<!-- b000281 | prose | pages [13] -->
-0.05973 0.024991 -0.05972

<!-- b000282 | caption | pages [13] -->
Table 7: Boxplot analysis between POS and score

<!-- b000283 | furniture | pages [14] -->
Team # 2300348

<!-- b000284 | furniture | pages [14] -->
Page 13 of 25

<!-- b000285 | prose | pages [14] -->
From Figure8(a) and Table7, the median difference between Noun and Adjective is 0.024991, the median difference between Noun and Adverb is -0.05973 and the median difference between Noun and Verb is -0.05972. From Figure8(b), it can be observed that the central tendency of the four categories of data is quite similar. Therefore, we conclude that the score of words does not show significant differences across different POS.

<!-- b000286 | prose | pages [14] -->
6

<!-- b000287 | heading | pages [14] -->
GSRF Prediction Model

<!-- b000288 | prose | pages [14] -->
In Section 4, we processed the percentages of (1, 2, 3, 4, 5, 6, X) into a single parameter score. While a single parameter can capture some overall characteristics of these seven numbers, the specific meanings of these seven numbers cannot be expressed individually and important details and meanings may also be lost.

<!-- b000289 | prose | pages [14] -->
Unlike the time series prediction in Section 4, the distribution of the reported results theoretically should be determined by the attributes of the answer words on that day rather than the time series. Therefore, we chose the Grid-Search Random Forest (GSRF) algorithm to determine the best strategy for predicting the distribution of the reported results using the three attributes of the words themselves. With the best strategy obtained from the model trained on existing data, we predicted the distribution of the reported results of EERIE on March 1, 2023, and achieved good prediction performance.

<!-- b000290 | prose | pages [14] -->
6.1

<!-- b000291 | heading | pages [14] -->
Description of GSRF Algorithm

<!-- b000292 | prose | pages [14] -->
The GSRF algorithm consists of Random Forest and GridSearchCV.

<!-- b000293 | prose | pages [14] -->
GridSearchCV is a parameter optimization algorithm commonly used to fine-tune hyperparam- eters in machine learning models to optimize their performance. It iterates through a specified parameter grid and trains and evaluates the model for each possible parameter combination, ulti- mately outputting the best parameter set and corresponding model performance metric.

<!-- b000294 | prose | pages [14] -->
Random Forest is a machine learning algorithm that is an ensemble of multiple decision trees. The training process of Random Forest is based on multiple decision trees, with the algorithm randomly selecting a subset of features for training in each decision tree.

<!-- b000295 | prose | pages [14] -->
During prediction, Random Forest aggregates the predictions from each decision tree by averaging or voting to obtain the final prediction.

<!-- b000296 | prose | pages [14] -->
Different from the ordinary Random Forest algorithm, the GSRF algorithm can train and predict the Random Forest model using the best hyperparameter combination, which significantly improves the model’s performance and avoids issues such as overfitting or underfitting.The algorithmic flow of GSRF is shown Figure9.

<!-- b000297 | furniture | pages [15] -->
Team # 2300348

<!-- b000298 | furniture | pages [15] -->
Page 14 of 25

<!-- b000299 | caption | pages [15] -->
Figure 9: The algorithmic flow of GSRF

<!-- b000300 | prose | pages [15] -->
Prediction for EERIE on March 1,2023 6.2

<!-- b000301 | prose | pages [15] -->
In Section 4, we performed data analysis on the relationship between word attributes and the percentage of scores. We found that the word frequency fword, letter frequency fletter, and repetition of letters rep have some influence on the percentage of scores. Therefore, we used these three attributes of the word itself as input parameters for the Random Forest model to predict the distribution of the reported results:

<!-- b000302 | prose | pages [15] -->
GSRF −→(1, 2, 3, 4, 5, 6, X)

<!-- b000303 | prose | pages [15] -->
(fword, fletter, rep)

<!-- b000304 | prose | pages [15] -->
(5)

<!-- b000305 | prose | pages [15] -->
We take the word "eerie" that we want to predict for example, and its three input word attributes are shown in Table8. It should be noted that we set the rep value to 1.5 for words with repeated letters, and set the rep value to 1 for words without repeated letters. This is reasonable because GSRF normalizes the input data before calculation. Since rep has only two possible values, it will be processed as 0 and 1.

<!-- b000306 | prose | pages [15] -->
fword, fletter, ref

<!-- b000307 | prose | pages [15] -->
0.418799 0.00023% 1.5

<!-- b000308 | caption | pages [15] -->
Table 8: Word attributes of EERIE

<!-- b000309 | prose | pages [15] -->
Next, we trained the GSRF model using the word frequency, letter frequency, and repetition information of each word from January 7, 2022 to December 31, 2022, in order to learn the distribution of their reported results. To achieve this, we utilized the RandomForestRegressor algorithm from the scikit-learn (sklearn) machine learning library’s ensemble module [6], as well as the GridSearchCV algorithm from the sklearn.model_selection module [7]. With the trained GSRF model, we made predictions on the distribution of reported results for the word "eerie" using its three word attributes. The results are presented in Table9 and Table10:

<!-- b000310 | furniture | pages [16] -->
Team # 2300348

<!-- b000311 | furniture | pages [16] -->
Page 15 of 25

<!-- b000312 | prose | pages [16] -->
min samples leaf max depth, max features,

<!-- b000313 | prose | pages [16] -->
10 ’sqrt’ 2

<!-- b000314 | prose | pages [16] -->
min samples split n estimators

<!-- b000315 | prose | pages [16] -->
10 200

<!-- b000316 | caption | pages [16] -->
Table 9: The best hyperparameter combination by GridSearchCV

<!-- b000317 | prose | pages [16] -->
1 2 3 4 5 6 X

<!-- b000318 | prose | pages [16] -->
30.29725% 1.07508% 6.51769% 23.30265%

<!-- b000319 | prose | pages [16] -->
MSE: 20.70641 MAE: 3.24388

<!-- b000320 | prose | pages [16] -->
23.13552% 13.27519% 2.40859%

<!-- b000321 | caption | pages [16] -->
Table 10: Prediction for the word EERIE on March 1, 2023

<!-- b000322 | prose | pages [16] -->
6.3 Prediction evaluation analysis

<!-- b000323 | prose | pages [16] -->
When using machine learning algorithms for prediction, two commonly used evaluation metrics are the Mean Squared Error (MSE) and Mean Absolute Error (MAE). MSE is the average of the squared differences between the prediction and origin data, while MAE is the average of the absolute differences between the prediction and origin data. They are calculated as follows:

<!-- b000324 | prose | pages [16] -->
MSE = 1

<!-- b000325 | prose | pages [16] -->
n

<!-- b000326 | prose | pages [16] -->
MAE = 1

<!-- b000327 | prose | pages [16] -->
n

<!-- b000328 | prose | pages [16] -->
where:

<!-- b000329 | prose | pages [16] -->
n n X

<!-- b000330 | prose | pages [16] -->
(yi −ˆyi)2 (6)

<!-- b000331 | prose | pages [16] -->
i=1

<!-- b000332 | prose | pages [16] -->
n X

<!-- b000333 | prose | pages [16] -->
|yi −ˆyi| (7)

<!-- b000334 | prose | pages [16] -->
i=1

<!-- b000335 | prose | pages [16] -->
• n denotes the number of samples, yi denotes the origin data, and ˆyi denotes the prediction data.

<!-- b000336 | prose | pages [16] -->
According to the data presented in Table10, the GSRF Prediction Model had a very good prediction performance for the distribution of reported results for "EERIE" on March 1, 2023, with a MSE of 20.70641 and MAE of 3.24388. This indicates that the model was able to accurately predict the reported results for the word based on its attributes, demonstrating the effectiveness of the GSRF algorithm for this task.

<!-- b000337 | prose | pages [16] -->
Considering that a word’s attributes are not limited to the three we applied, other unexplored attributes could also influence the distribution of the reported results. Incorporating these additional attributes as inputs to the model could potentially improve its predictive accuracy. Moreover, the time when a word appears might also have an impact on the distribution, as was the case with the special instance of "Christmas Day".

<!-- b000338 | furniture | pages [17] -->
Team # 2300348

<!-- b000339 | furniture | pages [17] -->
Page 16 of 25

<!-- b000340 | prose | pages [17] -->
• Regarding the issue of incomplete word attributes, our model has already attempted to comprehensively consider the properties that are beneficial to the prediction.

<!-- b000341 | prose | pages [17] -->
• As for whether time is a factor, it remains uncertain.

<!-- b000342 | prose | pages [17] -->
Based on the above analysis, we consider our prediction model to be a comprehensive and accurate one.

<!-- b000343 | prose | pages [17] -->
7

<!-- b000344 | heading | pages [17] -->
Difficulty Rate Classification Model by K-Means++

<!-- b000345 | prose | pages [17] -->
In this section, we define the difficulty rate δ of words using the distribution of reported results and calculated δ for "EERIE" and the words from January 7, 2022, to December 31, 2022. Then, we used the K-Means++ algorithm to perform clustering analysis on the difficulty rate of words and obtained a scientific classification of the difficulty rate. EERIE was classified in level 3. Finally, we randomly sampled words, manually labeled their difficulty levels, and used the K-Means++ model for clustering analysis. The results show that our classification model is relatively accurate.

<!-- b000346 | prose | pages [17] -->
δ: Difficulty Rate 7.1

<!-- b000347 | prose | pages [17] -->
The difficulty level of a word can be directly determined by the percentages of (1, 2, 3, 4, 5, 6, X). It is observed that when a word is particularly difficult or hard to guess, the percentage of larger tries (e.g. 5 or 6) increases.

<!-- b000348 | prose | pages [17] -->
Similar to the score in Section 4, the difficulty rate δ is still composed of two parts. One part is the weighted average of the percentages of (1, 2, 3, 4, 5, 6), and the other part is X. However, unlike the X component in score which is calculated as a percentage, the difference in magnitude between X and the other part is relatively larger when calculating δ. As X reflects the percentage of people who failed to answer the question on a given day, it should be given more weight when measuring the difficulty of a word. To balance the two parameters of δ, we use the Sigmoid function to normalize these two data and then assign weights using the Entropy Weighting Method to obtain the difficulty rate δ:

<!-- b000349 | prose | pages [17] -->
6 X

<!-- b000350 | prose | pages [17] -->
δ = σω1 ∗

<!-- b000351 | prose | pages [17] -->
i ∗pi + σω2 ∗pX (8)

<!-- b000352 | prose | pages [17] -->
i=1

<!-- b000353 | prose | pages [17] -->
where:

<!-- b000354 | prose | pages [17] -->
• pi denotes the percentage of i tries(try) and i ∈{1, 2, 3, 4, 5, 6, X}

<!-- b000355 | prose | pages [17] -->
• σ denotes the sigmoid function

<!-- b000356 | prose | pages [17] -->
• ω1 and ω2 denote the weights of two parts of score respectively. And we set ω1 as 0.5 and ω2 as 0.5 by Entropy Weighting Method.

<!-- b000357 | prose | pages [17] -->
7.2 K-Means++ Clustering Analysis

<!-- b000358 | prose | pages [17] -->
K-Means clustering algorithm is a common unsupervised machine learning algorithm used to divide data into several categories. It pre-specifies the initial number of clusters and the initial

<!-- b000359 | furniture | pages [18] -->
Team # 2300348

<!-- b000360 | furniture | pages [18] -->
Page 17 of 25

<!-- b000361 | prose | pages [18] -->
cluster centers, and divides the sample set into different clusters according to the size of the distance between the samples. The Euclidean distance is used as a measure of the similarity between data objects, with similarity being inversely proportional to the distance between data objects. The larger the similarity, the smaller the distance. Based on the similarity between the data objects and the cluster centers, the position of the cluster centers is continuously updated, and the sum of squared errors (SSE) of the clusters is continuously reduced. When the SSE no longer changes or the objective function converges, the clustering ends and the final result is obtained.

<!-- b000362 | prose | pages [18] -->
The Euclidean distance formula between data objects and cluster centers in space is:

<!-- b000363 | prose | pages [18] -->
v u u

<!-- b000364 | prose | pages [18] -->
d (X, Ci) =

<!-- b000365 | prose | pages [18] -->
t

<!-- b000366 | prose | pages [18] -->
where:

<!-- b000367 | prose | pages [18] -->
• X denotes data objects

<!-- b000368 | prose | pages [18] -->
• Ci denotes the ith cluster center

<!-- b000369 | prose | pages [18] -->
• m denotes dimensionality of data objects

<!-- b000370 | prose | pages [18] -->
m X

<!-- b000371 | prose | pages [18] -->
(Xj −Cij)2 (9)

<!-- b000372 | prose | pages [18] -->
j=1

<!-- b000373 | prose | pages [18] -->
• Xj and Cij denote the j-th attribute values of X and Ci, respectively

<!-- b000374 | prose | pages [18] -->
The formula for calculating the SSE of the entire dataset is:

<!-- b000375 | prose | pages [18] -->
k X

<!-- b000376 | prose | pages [18] -->
SSE =

<!-- b000377 | prose | pages [18] -->
i=1

<!-- b000378 | prose | pages [18] -->
X

<!-- b000379 | prose | pages [18] -->
|d (X, Ci)|2 (10)

<!-- b000380 | prose | pages [18] -->
X∈Ci

<!-- b000381 | prose | pages [18] -->
where:

<!-- b000382 | prose | pages [18] -->
• k denotes the number of clusters

<!-- b000383 | prose | pages [18] -->
In traditional K-Means algorithm, the initialization of cluster centers is usually randomly selected from k sample points. However, this random selection method is prone to local optima, leading to poor clustering results. The probability selection process introduced by K-Means++ algorithm can make the cluster centers more dispersed, making it easier to find the global optimal solution, and thereby improving the quality of clustering results.

<!-- b000384 | prose | pages [18] -->
7.3 Difficulty classification for EERIE

<!-- b000385 | prose | pages [18] -->
Using the K-Means algorithm in the scikit-learn library of Python[8] with the "k-means++" initialization parameter set, we can perform a clustering analysis on the calculated difficulty rate δ of each word. The analysis divides the difficulty coefficients of the words into five levels, ranging from level 1 to level 5, with a higher level indicating a greater difficulty of the word. The calculated difficulty rate δ of the word "ERRIE" is 0.35916, which corresponds to level 3 in the difficulty hierarchy.The results are shown in Figure10 and Table11 as follows:

<!-- b000386 | furniture | pages [19] -->
Team # 2300348

<!-- b000387 | prose | pages [19] -->
(a)

<!-- b000388 | furniture | pages [19] -->
Page 18 of 25

<!-- b000389 | prose | pages [19] -->
(b)

<!-- b000390 | caption | pages [19] -->
Figure 10: Difficulty rate classification

<!-- b000391 | prose | pages [19] -->
Percentage Level Number Valuable Percentage

<!-- b000392 | prose | pages [19] -->
36.2% 1 131 36.2%

<!-- b000393 | prose | pages [19] -->
42.4% 2 152 42.4%

<!-- b000394 | prose | pages [19] -->
19.1% 3 69

<!-- b000395 | prose | pages [19] -->
4 7 2%

<!-- b000396 | prose | pages [19] -->
19.1%

<!-- b000397 | prose | pages [19] -->
2%

<!-- b000398 | prose | pages [19] -->
0.3% 5 1 0.3%

<!-- b000399 | prose | pages [19] -->
23.30265% Sum 6.51769% 30.29725%

<!-- b000400 | caption | pages [19] -->
Table 11: Results of clustering analysis

<!-- b000401 | heading | pages [19] -->
Accuracy Discussion of Classification Model

<!-- b000402 | prose | pages [19] -->
7.4

<!-- b000403 | prose | pages [19] -->
Finally, we randomly sampled 30 words, manually labeled their difficulty levels, and used the K-Means++ model for clustering analysis. Comparing the manually labeled difficulty levels of sample words with the difficulty levels obtained from the clustering analysis, 28 out of 30 data points matched, resulting in a 93.33% match rate. This indicates that the difficulty level classification obtained by the model is consistent with our subjective judgment of word difficulty. Therefore, we believe that our classification model is relatively accurate. The data for the word samples are presented in the AppendixA.

<!-- b000404 | furniture | pages [20] -->
Team # 2300348

<!-- b000405 | furniture | pages [20] -->
Page 19 of 25

<!-- b000406 | prose | pages [20] -->
8 Interesting Features of Data

<!-- b000407 | prose | pages [20] -->
8.1 Feature 1:Relationship of Word Attributes and Hard Mode Percentage

<!-- b000408 | prose | pages [20] -->
We are interested in whether the properties of words are related to the proportion of users who choose the Hard Mode daily. Since the properties of words are to some extent related to difficulty, if the words are too difficult one day and increase users’ frustration, users may not choose the Hard Mode the next day. Therefore, we conducted data analysis on the four attributes of words and the daily percentage of Hard Mode, including regression analysis and boxplot analysis. The results show that the percentage of Hard Mode is not linearly related to word frequency and letter frequency. There is also no significant difference in the percentage of Hard Mode among words with different letter repetitions and different parts of speech. The results are shown as follows:

<!-- b000409 | prose | pages [20] -->
(a) Word frequency (b) Letter frequency

<!-- b000410 | caption | pages [20] -->
Figure 11: Regression analysis between word attributes and Hard Mode peercentage

<!-- b000411 | prose | pages [20] -->
(a) Boxplot of repetition (b) Density of repetition

<!-- b000412 | furniture | pages [21] -->
Team # 2300348

<!-- b000413 | furniture | pages [21] -->
Page 20 of 25

<!-- b000414 | prose | pages [21] -->
(c) Boxplot of POS (d) Density of POS

<!-- b000415 | caption | pages [21] -->
Figure 12: Boxplot analysis between POS and Hard Mode peercentage

<!-- b000416 | prose | pages [21] -->
8.2 Feature 2:Why "PARER" Has The Most "Hellish" Level of Difficulty

<!-- b000417 | prose | pages [21] -->
In Section 8, we found that the difficulty date of the word "parer" is as high as 0.98, far exceeding the second-place word "mummy" with a score of 0.69. Looking back at the original data, we are surprised to discover that on the day of "parer", the "X" percentage was as high as 48%, indicating that 48% of players were unable to guess the answer. While browsing the user comments on Wordle Stats, some comments provided a possible explanation.(Figure13) It suggested that when the word to be guessed has many similar words (i.e. with similar letter composition or positions), and those similar words have a higher frequency of everyday use than the solution word, it becomes difficult to guess the correct word.

<!-- b000418 | prose | pages [21] -->
(a) User comment1[9] (b) User comment2[10]

<!-- b000419 | caption | pages [21] -->
Figure 13: User comments

<!-- b000420 | furniture | pages [22] -->
Team # 2300348

<!-- b000421 | prose | pages [22] -->
9

<!-- b000422 | heading | pages [22] -->
Model Sensitivity Analysis

<!-- b000423 | furniture | pages [22] -->
Page 21 of 25

<!-- b000424 | prose | pages [22] -->
We conducted a sensitivity analysis on the input parameters of the GSRF Prediction Model to test its sensitivity to changes in the input parameters in predicting the distribution of the reported results. The specific method is to add Gaussian noise to the model’s input parameters. However, for the word repetition level, there are only two types of data, and the noise added to rep will be directly eliminated by the model when normalizing the input data. Therefore, we only conducted sensitivity analysis on word frequency and letter frequency. Gaussian noise is defined as follows:

<!-- b000425 | prose | pages [22] -->
1

<!-- b000426 | prose | pages [22] -->
√

<!-- b000427 | prose | pages [22] -->
−(x −µ)2

<!-- b000428 | prose | pages [22] -->


<!-- b000429 | prose | pages [22] -->


<!-- b000430 | prose | pages [22] -->
2π exp

<!-- b000431 | prose | pages [22] -->
p(x) = σ

<!-- b000432 | prose | pages [22] -->
where:

<!-- b000433 | prose | pages [22] -->
(11)

<!-- b000434 | prose | pages [22] -->
2σ2

<!-- b000435 | prose | pages [22] -->
• x the amplitude of a random signal, µ denotes the mean, σ denotes the standard deviations

<!-- b000436 | heading | pages [22] -->
Sensitivity Analysis for fword in GSRF Prediction Model

<!-- b000437 | prose | pages [22] -->
9.1

<!-- b000438 | prose | pages [22] -->
After adding 1 Gaussian noise to the word frequency, the results are shown in Figure14:

<!-- b000439 | prose | pages [22] -->
(a) (b)

<!-- b000440 | caption | pages [22] -->
Figure 14: Sensitivity of word frequency

<!-- b000441 | prose | pages [22] -->
The visual results from sensitivity analysis indicate that the GSRF Prediction Model exhibits low sensitivity to changes in word frequency, indicating a high level of stability.

<!-- b000442 | heading | pages [22] -->
Sensitivity Analysis for fletter in GSRF Prediction Model

<!-- b000443 | prose | pages [22] -->
9.2

<!-- b000444 | prose | pages [22] -->
After adding 1 Gaussian noise to the letter frequency, the results are shown in Figure15:

<!-- b000445 | furniture | pages [23] -->
Team # 2300348

<!-- b000446 | furniture | pages [23] -->
Page 22 of 25

<!-- b000447 | prose | pages [23] -->
(a) (b)

<!-- b000448 | caption | pages [23] -->
Figure 15: Sensitivity of letter frequency

<!-- b000449 | prose | pages [23] -->
The visual results from sensitivity analysis indicate that the GSRF Prediction Model exhibits relatively low sensitivity to changes in letter frequency, indicating a high level of stability.

<!-- b000450 | prose | pages [23] -->
10

<!-- b000451 | heading | pages [23] -->
Model Evaluation and Further Discussion

<!-- b000452 | prose | pages [23] -->
10.1

<!-- b000453 | heading | pages [23] -->
Strengths

<!-- b000454 | heading | pages [23] -->
1. GRU: The GRU algorithm in Section 4 has several advantages when used for prediction tasks.

<!-- b000455 | prose | pages [23] -->
GRU can effectively handle sequential data with variable-length inputs, making it well-suited for time series prediction. And GRU typically requires fewer parameters to train compared to other recurrent neural networks, such as LSTM, making it computationally more efficient and easier to train. Therefore, the relative error rate of our prediction result is only 2.1569.

<!-- b000456 | heading | pages [23] -->
2. GSRF: Different from the ordinary Random Forest algorithm, the GSRF algorithm in Section

<!-- b000457 | prose | pages [23] -->
6 can train and predict the Random Forest model using the best hyperparameter combination, which significantly improves the model’s performance and avoids issues such as overfitting or underfitting.

<!-- b000458 | heading | pages [23] -->
3. K-Means++:In traditional K-Means algorithm, is prone to local optima, leading to poor

<!-- b000459 | prose | pages [23] -->
clustering results. The probability selection process introduced by K-Means++ algorithm Section 7 can make the cluster centers more dispersed, making it easier to find the global optimal solution, and thereby improving the quality of clustering results.

<!-- b000460 | heading | pages [23] -->
4. K-Means++Our analysis in the word attribute analysis in Section 5 and data feature mining

<!-- b000461 | prose | pages [23] -->
in Section 8 is relatively comprehensive and constructive.

<!-- b000462 | prose | pages [23] -->
10.2

<!-- b000463 | heading | pages [23] -->
Weaknesses And Further Discussion

<!-- b000464 | prose | pages [23] -->
1. There are more attributes of words, such as vowels and consonants.

<!-- b000465 | prose | pages [23] -->
2. Time factor may be incorporated into the prediction of the distribution of the reported results.

<!-- b000466 | furniture | pages [24] -->
Team # 2300348

<!-- b000467 | furniture | pages [24] -->
Page 23 of 25

<!-- b000468 | prose | pages [24] -->
3. Our model uses a large number of machine learning algorithms. More advanced methods and data training techniques can be selected. For example, the K-Means algorithm has variations such as Mini-Batch K-Means and Genetic K-Means algorithms. The most suitable algorithm from each variation can be selected for analyzing the current data.

<!-- b000469 | heading | pages [24] -->
References

<!-- b000470 | references | pages [24] -->
[1] https://twitter.com/WordleStats/status/1481687496241164291

<!-- b000471 | references | pages [24] -->
[2] https://www.marca.com/tecnologia/2022/02/14/620a2ee522601da7288b4599.

<!-- b000472 | references | pages [24] -->
html

<!-- b000473 | references | pages [24] -->
[3] https://pytorch.org/docs/stable/generated/torch.nn.GRU.html

<!-- b000474 | references | pages [24] -->
[4] https://books.google.com/ngrams/

<!-- b000475 | references | pages [24] -->
[5] http://www.nltk.org/

<!-- b000476 | references | pages [24] -->
[6] https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.

<!-- b000477 | references | pages [24] -->
RandomForestRegressor.html

<!-- b000478 | references | pages [24] -->
[7] https://scikit-learn.org/stable/modules/generated/sklearn.model_

<!-- b000479 | references | pages [24] -->
selection.GridSearchCV.html

<!-- b000480 | references | pages [24] -->
[8] https://scikit-learn.org/stable/modules/generated/sklearn.cluster.

<!-- b000481 | references | pages [24] -->
KMeans.html

<!-- b000482 | references | pages [24] -->
[9] https://twitter.com/WordleStats/status/1571182427007221764

<!-- b000483 | references | pages [24] -->
[10] https://twitter.com/s_harmony_/status/1570624760530477057

<!-- b000484 | furniture | pages [25] -->
Team # 2300348

<!-- b000485 | furniture | pages [25] -->
Page 24 of 25

<!-- b000486 | references | pages [25] -->
11

<!-- b000487 | heading | pages [25] -->
Letter

<!-- b000488 | prose | pages [25] -->
Dear Puzzle Editor of the New York Times.

<!-- b000489 | prose | pages [25] -->
I hope this message finds you well.I am writing to share the results of our analyses of Wordle data.

<!-- b000490 | prose | pages [25] -->
Firstly, we established a GRU Prediction Model to predict the number of reported results on March 1, 2023. The model uses the effective Gated Recurrent Unit (GRU) algorithm. Therefore, predictions made by the training set to the testing have the relative error rate of 2.1569%, and the relative RESE of 6.4957%, indicating a good accuracy of the model predictions. The predicted interval for the number of reported results on March 1, 2023 is 20367 ± 2.01569

<!-- b000491 | prose | pages [25] -->
Secondly, we conducted a data analysis on the attributes of words and score defined by the percentage of scores played in Hard Mode to explore their relationship. Then, we defined four attributes of the words: word frequency, sum of letter frequencies, repetition patterns of letters (2/3 or none), and pos: main part of speech. For fword and fletter, we performed regression analysis with the variable "score". The Pearson correlation coefficient between fword and score is -0.3165, and fletter and score -0.4005. rep and pos can be used to categorize the words. The box plot results showed that the Median difference of the box plot for rep was 0.13004, while pos was only 0.05973. Therefore, we believe that fword, fletter, and rep can affect the percentage of scores, while pos can not.

<!-- b000492 | prose | pages [25] -->
Thirdly, we have developed GSRF Prediction Model to predict the percentages of 1 to X for EERIE on March 1, 2023. The Grid-Search Random Forest (GSRF) algorithm is an improved random forest algorithm by using the best combination of hyperparameters. We selected the three parameters, fword, fletter, and rep as inputs for the model. The model’s training results show a MSE of 20.70641 and a MAE of 3.24388, indicating good predictive performance. (Table 10) The predicted results for EERIE are (1,7,23,30,23,13,3). In addition, we conducted sensitivity analysis by adding Gaussian noise to fword and fletter separately, and the results showed that the model has low sensitivity and is thus highly stable.

<!-- b000493 | prose | pages [25] -->
Fourthly, Difficulty Rate Classification Model using the K-Means++ are conducted. We first defined the difficulty date δ of each word first. The difficulty rate of EERIE is 0.35916 by predicted distribution. Then, we used the improved clustering analysis algorithm, K-Means++, to analyze the δ of each word and obtained five levels of difficulty (Table11). EERIE was classified into the third level. Finally, we compared the model’s classification with the manul difficulty ratings for a subset of sampled words and achieved a match rate of 93.33%, confirming the accuracy of the model.

<!-- b000494 | prose | pages [25] -->
Finally, we found that the four word attributes we analyzed do not affect the percentage of users selecting the hard mode. We also investigated why "parer" is the only word in the fifth difficulty level, with a high difficulty coefficient of 0.98. It turns out that the difficulty of a word may be linked to the word’s similarity to other words and the frequency of use of these similar words.

<!-- b000495 | prose | pages [25] -->
You can read the full text of our model if you would like to learn more detailed information.

<!-- b000496 | prose | pages [25] -->
Sincerely,

<!-- b000497 | prose | pages [25] -->
Team 2300348

<!-- b000498 | furniture | pages [26] -->
Team # 2300348

<!-- b000499 | furniture | pages [26] -->
Page 25 of 25

<!-- b000500 | prose | pages [26] -->
A Samples

<!-- b000501 | prose | pages [26] -->
B Difficluty Rate of Partial Words
