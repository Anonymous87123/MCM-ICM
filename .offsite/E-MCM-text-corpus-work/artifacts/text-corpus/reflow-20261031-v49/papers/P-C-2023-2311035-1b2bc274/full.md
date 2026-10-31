# P-C-2023-2311035-1b2bc274

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
Problem Chosen 2023 MCM/ICM

<!-- b000003 | title | pages [1] -->
C

<!-- b000004 | title | pages [1] -->
2311035

<!-- b000005 | heading | pages [1] -->
Summary Sheet

<!-- b000006 | title | pages [1] -->
Winners in Wordle

<!-- b000007 | heading | pages [1] -->
Summary

<!-- b000008 | prose | pages [1] -->
Wordle is a phenomenal network game. Its appearance intensely aroused people’s attention. Although it looks tiny, the hidden information behind it is huge and meaningful. Capturing and understanding this information will help the New York Times better design and operate Wordle.

<!-- b000009 | prose | pages [1] -->
We built three models to ﬁnish the tasks. Model I uses LSTM to forecast the number of reported scores in the future. Model II uses seven XGBoost regressors to predict the percentage distribution of a given the word. Model III classiﬁes words by their diﬃculties using SVM with RBF kernel. Based on our three models, we can provide some advice to help improve Wordle.

<!-- b000010 | prose | pages [1] -->
The speciﬁc details are shown below:

<!-- b000011 | prose | pages [1] -->
Model I: LSTM is an improved recurrent neural network that can solve the long-distance dependence problem that other neural networks cannot handle. We trained processed data of the number of reported scores for the model and used an iterative method to predict the number until March 1st (2023). After 150 times of independent model training, the prediction interval is [20745.72, 22914.74]. Additionally, from the linear regression on the proportion of hard mode with word attributes, we can also ﬁnd no correlation between hard-mode-ratio and target word.

<!-- b000012 | prose | pages [1] -->
Model II: To get the percentage distribution of a given day associated with a speciﬁc word, we trained seven separate XGBoost models. The R2 of our model is 0.68, which can be accurately predicted with low uncertainty after testing. We apply "EERIE" to the model and gain a prediction percentage distribution, showing that ERRIE should be considered as an problematic word.

<!-- b000013 | prose | pages [1] -->
Model III: We quantiﬁed the diﬃculty of words by the unequally weighted average of percentage distribution and divided them into three levels: easy, medium and hard. Then we used labeled to ﬁt SVM model with RBF kernel and gain an accuracy score of 0.6556 and an F1 score of 0.6634. Also, the classiﬁcation result for EERIE is hard, consistent with the result in model 2.

<!-- b000014 | prose | pages [1] -->
Except for these three models, we also found some interesting observations from the dataset, one of which discussed the diﬀerences between human thinking and machine learning.

<!-- b000015 | prose | pages [1] -->
Finally, we write a letter including our models, results, and advice to the New York Times Wordle editor. We hope this letter will become a valuable reference for the further development of Wordle.

<!-- b000016 | keywords | pages [1] -->
Keywords: Wordle; LSTM; Recursive Regression; XGBoost; Feature Engineering

<!-- b000017 | furniture | pages [2] -->
Team # 2311035

<!-- b000018 | furniture | pages [2] -->
Page 1 of 22

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1 Introduction

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
1.1

<!-- b000023 | contents | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
3

<!-- b000025 | contents | pages [2] -->
1.2

<!-- b000026 | contents | pages [2] -->
Restatement of Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
3

<!-- b000028 | contents | pages [2] -->
1.3

<!-- b000029 | contents | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
4

<!-- b000031 | contents | pages [2] -->
1.4

<!-- b000032 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
5

<!-- b000034 | contents | pages [2] -->
2 Assumptions

<!-- b000035 | contents | pages [2] -->
5

<!-- b000036 | contents | pages [2] -->
3 Notations

<!-- b000037 | contents | pages [2] -->
5

<!-- b000038 | contents | pages [2] -->
4 Task 1: Fundamental Model for Predicting Results

<!-- b000039 | contents | pages [2] -->
6

<!-- b000040 | contents | pages [2] -->
4.1

<!-- b000041 | contents | pages [2] -->
Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
6

<!-- b000043 | contents | pages [2] -->
4.2

<!-- b000044 | contents | pages [2] -->
Formulating the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
6

<!-- b000046 | contents | pages [2] -->
4.2.1

<!-- b000047 | contents | pages [2] -->
Long-term and Short-term Memory . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
7

<!-- b000049 | contents | pages [2] -->
4.2.2

<!-- b000050 | contents | pages [2] -->
Data Normalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
8

<!-- b000052 | contents | pages [2] -->
4.2.3

<!-- b000053 | contents | pages [2] -->
Implementation of LSTM

<!-- b000054 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
9

<!-- b000056 | contents | pages [2] -->
4.2.4

<!-- b000057 | contents | pages [2] -->
Prediction Interval from the Result . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
9

<!-- b000059 | contents | pages [2] -->
4.3

<!-- b000060 | contents | pages [2] -->
Correlation between Hard-mode Percentage and Words . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
10

<!-- b000062 | contents | pages [2] -->
5 Task 2: Model for Predicting Percentage Distribution

<!-- b000063 | contents | pages [2] -->
11

<!-- b000064 | contents | pages [2] -->
5.1

<!-- b000065 | contents | pages [2] -->
Features Used to Measure the Performance of Reported Results . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
11

<!-- b000067 | contents | pages [2] -->
5.2

<!-- b000068 | contents | pages [2] -->
Feature Engineering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
11

<!-- b000070 | contents | pages [2] -->
5.3

<!-- b000071 | contents | pages [2] -->
XGBoost Model Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
11

<!-- b000073 | contents | pages [2] -->
5.4

<!-- b000074 | contents | pages [2] -->
Uncertainties Involved in the Model

<!-- b000075 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
12

<!-- b000077 | contents | pages [2] -->
5.5

<!-- b000078 | contents | pages [2] -->
Predicted Distribution of EERIE . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
13

<!-- b000080 | contents | pages [2] -->
6 Task 3: Classiﬁcation of Words

<!-- b000081 | contents | pages [2] -->
14

<!-- b000082 | contents | pages [2] -->
6.1

<!-- b000083 | contents | pages [2] -->
Deﬁnition of Word Diﬃculty . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
14

<!-- b000085 | contents | pages [2] -->
6.2

<!-- b000086 | contents | pages [2] -->
Feature Engineering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
15

<!-- b000088 | contents | pages [2] -->
6.3

<!-- b000089 | contents | pages [2] -->
Model Construction and Prediction . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
15

<!-- b000091 | furniture | pages [3] -->
Team # 2311035

<!-- b000092 | furniture | pages [3] -->
Page 2 of 22

<!-- b000093 | contents | pages [3] -->
6.4

<!-- b000094 | contents | pages [3] -->
Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [3] -->
15

<!-- b000096 | heading | pages [3] -->
7 Task 4: Other Interesting Findings

<!-- b000097 | prose | pages [3] -->
16 7.1 Fundamental Diﬀerence in Wordle Playing Strategy between Human Brain and Machine Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 7.2 Other Interesting Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

<!-- b000098 | heading | pages [3] -->
8 Strengths and Weaknesses

<!-- b000099 | prose | pages [3] -->
18 8.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 8.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

<!-- b000100 | heading | pages [3] -->
9 Letter

<!-- b000101 | prose | pages [3] -->
20

<!-- b000102 | heading | pages [3] -->
References

<!-- b000103 | references | pages [3] -->
22

<!-- b000104 | furniture | pages [4] -->
Team # 2311035

<!-- b000105 | furniture | pages [4] -->
Page 3 of 22

<!-- b000106 | heading | pages [4] -->
1 Introduction

<!-- b000107 | heading | pages [4] -->
1.1 Background

<!-- b000108 | prose | pages [4] -->
Nowadays, a puzzle game called "Wordle" has taken the world by storm with its light-hearted approach and confusing but attractive yellow, green, and grey squares.

<!-- b000109 | prose | pages [4] -->
Generally speaking, it is a game that requires players to guess the correct words within less than six times. Players can only guess a word that is oﬃcially recognized. Every time players make a guess (no more than six wrong guesses), they will be given a hint in the form of yellow, green, and grey squares. A green indicates correct; a yellow indicates correct letter in the wrong location; and a grey means that the letter is not included in the word. Wordles Hard Mode makes the game more challenging by forcing players to use correct letters found before in subsequent guesses. The example of "Wordle" is shown in Figure.1.

<!-- b000110 | caption | pages [4] -->
Figure 1: Example of Wordle Puzzle

<!-- b000111 | prose | pages [4] -->
To help the New York Times better understand the diﬃculty and audience of "Wordle", we hope to construct a prediction model using daily performance data posted by players on Twitter in 2022. In other words, to make the "Wordle" develop better, we should use the prediction model and get reasonable estimates of the number of future players, the distribution of reported results, and the measurement of word diﬃculty.

<!-- b000112 | heading | pages [4] -->
1.2 Restatement of Problem

<!-- b000113 | prose | pages [4] -->
• Construct a prediction model to explain the total variation and a prediction interval for the number of reported results on March 1st, 2023.

<!-- b000114 | prose | pages [4] -->
• Verify whether the attributes of words would aﬀect the percentage of players who post their hard-mode results on Twitter.

<!-- b000115 | furniture | pages [5] -->
Team # 2311035

<!-- b000116 | furniture | pages [5] -->
Page 4 of 22

<!-- b000117 | prose | pages [5] -->
• Given ﬁxed word, predict associated percentages of (1, 2, 3, 4, 5, 6, X) for a future date and explain uncertain factors. Apply the model on March 1st, 2023 with speciﬁc word "EERIE".

<!-- b000118 | prose | pages [5] -->
• Develop and summarize a model to classify solution words by diﬃculty and identify the attributes of a given word. Apply the model to classify the word "EERIE" and discuss the accuracy.

<!-- b000119 | prose | pages [5] -->
• List and describe other interesting ﬁndings of this dataset.

<!-- b000120 | heading | pages [5] -->
1.3 Literature Review

<!-- b000121 | prose | pages [5] -->
There are two primary tasks for the model: predicting the number of reported results with their associated percentages of (1, 2, 3, 4, 5, 6, X) along the time axis, and measuring the diﬃculty level of a given word "EERIE".

<!-- b000122 | prose | pages [5] -->
In the time series ﬁeld, models mainly focus on Long Short-Term Memory (LSTM), a kind of artiﬁcial neural network suitable for processing and predicting important events with very long intervals and delays in time series[1]. By using LSTM, we can gain much better performance than other traditional techniques. More speciﬁcally, the average reduction in the error rate obtained by LSTM compared to ARIMA was between 84% and 87% in forecasting time series[2].

<!-- b000123 | prose | pages [5] -->
In word classiﬁcation, Laurent has already found an optimal strategy through a decision tree to solve the "Wordle" puzzle[3]. He indicated that the optimal process will take four steps on average and at most six steps to match the word. Based on his decision tree, Selby[4] implemented the optimal strategy and provides a ﬁle to illustrate it, which works as shown in Figure.2. For an example in Figure.2, if we want to get the target word "nymph", we should follow the red track and the expected depth (number of guesses) is 3.

<!-- b000124 | caption | pages [5] -->
Figure 2: Working Process of Decision Trees

<!-- b000125 | furniture | pages [6] -->
Team # 2311035

<!-- b000126 | furniture | pages [6] -->
Page 5 of 22

<!-- b000127 | heading | pages [6] -->
1.4 Our Work

<!-- b000128 | prose | pages [6] -->
Figure.3 shows the process of our work:

<!-- b000129 | caption | pages [6] -->
Figure 3: The Process of Our Work

<!-- b000130 | heading | pages [6] -->
2 Assumptions

<!-- b000131 | prose | pages [6] -->
Assumptions are made as follows to simplify the problem. Each of them is properly justiﬁed.

<!-- b000132 | prose | pages [6] -->
• Ignore the inﬂuence of extreme events, such as holidays and natural disasters, since these events rarely happen. So, we can ignore its eﬀect on our model.

<!-- b000133 | prose | pages [6] -->
• The 2020 Word Frequency Table can represent the frequency of words that all participants daily use. And the usage frequence has not changed signiﬁcantly over the past three years.

<!-- b000134 | prose | pages [6] -->
• The results reported by players were independently made by themselves without cheating.

<!-- b000135 | prose | pages [6] -->
Other speciﬁc assumptions, if necessary, will be mentioned and illustrated while we’re estab- lishing models.

<!-- b000136 | heading | pages [6] -->
3 Notations

<!-- b000137 | prose | pages [6] -->
Table.1 shows notations that should be used in equations:

<!-- b000138 | furniture | pages [7] -->
Team # 2311035

<!-- b000139 | furniture | pages [7] -->
Page 6 of 22

<!-- b000140 | caption | pages [7] -->
Table 1: Notations

<!-- b000141 | prose | pages [7] -->
Symbol Deﬁnition The output of the long-term memory Ct The output of the short-term memory ht Average of the sample data µ Standard deviation of the sample data sd Percentage of i try, i can be 1 to 6 or X itry Weighted average of performances in reported results wt Unequally weighted average of score distribution Ew

<!-- b000142 | heading | pages [7] -->
4 Task 1: Fundamental Model for Predicting Results

<!-- b000143 | heading | pages [7] -->
4.1 Data Cleaning

<!-- b000144 | prose | pages [7] -->
After statistics and processing of data, it was found that there were two kinds of errors in the sample data: The ﬁrst one is the lexical error, including length inconsistency, null character, and other problems. We do the correction based on oﬃcial twitter as shown in Table.2; The second one is the data error. The total number of scores reported on January 30th, 2022 is an outlier because of its lack of magnitude. So we looked back at oﬃcial twitter on that day and found the correct number is 25,569.

<!-- b000145 | caption | pages [7] -->
Table 2: Correction of Lexical Errors

<!-- b000146 | prose | pages [7] -->
Previous Word rprobe clen tash favor (with space) na?ve marxh Corrected Word probe clean trash favor naive marsh

<!-- b000147 | heading | pages [7] -->
4.2 Formulating the Model

<!-- b000148 | prose | pages [7] -->
LSTM, unlike other kinds of artiﬁcial neural networks, combines long-term and short-term memory to ensure the stability and accuracy of the model along the time series. This unique feature can be shown as a repeating unit in Figure.4. Here we will brieﬂy describe the principles used in our prediction model[5].

<!-- b000149 | furniture | pages [8] -->
Team # 2311035

<!-- b000150 | furniture | pages [8] -->
Page 7 of 22

<!-- b000151 | caption | pages [8] -->
Figure 4: Principle Graph of LSTM

<!-- b000152 | heading | pages [8] -->
4.2.1 Long-term and Short-term Memory

<!-- b000153 | prose | pages [8] -->
To understand the long-term memory’s output, we should realize the function of oblivion gate (Figure.5). The oblivion gate is used to compare information between the hidden state in the previous layer and the current status information Xt, and select the one with larger weights.

<!-- b000154 | caption | pages [8] -->
Figure 5: Oblivion Gate

<!-- b000155 | prose | pages [8] -->
The long-term memory output (Ct) is the ouput above, and the formula is:

<!-- b000156 | prose | pages [8, 9] -->
(1) Ct = ft ∗Ct−1 + it ∗˜Ct which can be described as an addition of two parts. The ﬁrst part is the overlap of oblivion gate output ft and long-term memory output from the previous layer Ct−1, and the second part is the information puriﬁed from the current status information.

<!-- b000157 | furniture | pages [9] -->
Team # 2311035

<!-- b000158 | furniture | pages [9] -->
Page 8 of 22

<!-- b000160 | prose | pages [9] -->
The short-term memory output (ht) is the ouput below, and the formula is shown as below (Figure.6):

<!-- b000161 | caption | pages [9] -->
Figure 6: Short-term Memory output

<!-- b000162 | prose | pages [9] -->
It can be described as a multiplication of two parts, the ﬁrst part is an actication process just as the same as the oblivion gate, and the second part is the information puriﬁed from the current long-term memory output (Ct). The ﬁnal result will also present the overlap of activated signal and puriﬁed long-term memory ouput.

<!-- b000163 | heading | pages [9] -->
4.2.2 Data Normalization

<!-- b000164 | prose | pages [9] -->
The input data of the LSTM model should be normalized. However, the distribution of the number of reported scores is quite unbalanced. For example, the change of reported number from 07/24/2022 to 11/01/2022 is 39813 −27502 = 12311. However, the ratio of change is only 3.4%, scaled by the maximum number. In other words, the traditional Min-Max normalization will not take eﬀect in this situation. Moreover, the number of reported scores roughly follows the gamma distribution, which includes the natural constant term. As a solution, a natural logarithm will be applied to the number of reported scores in the ﬁrst step. After narrowing the gap, the number will be normalized by the Min-Max method to ﬁnally produce the LSTM model’s input data, the total process is shown as Figure.7.

<!-- b000165 | caption | pages [9] -->
Figure 7: Process of Data Normalization

<!-- b000166 | furniture | pages [10] -->
Team # 2311035

<!-- b000167 | furniture | pages [10] -->
Page 9 of 22

<!-- b000168 | heading | pages [10] -->
4.2.3 Implementation of LSTM

<!-- b000169 | prose | pages [10] -->
In our task, we implement LSTM neural network by Pytorch. We aim to predict the score- reported number on March 1st based on the sample data with scores reported for 359 days, and it is a single input - single output LSTM model. Additionally, fundamental LSTM can only make one prediction at one time. However, our target is to predict the expected value after 60 days, so we recursively applied regressions for 60 times. This recursive process can continuously update sample data by adding latest output.

<!-- b000170 | prose | pages [10] -->
We only used one LSTM layer and one fully connected layer because of the small sample. Moreover, after cross-validation, we found that the best number of LSTM units was 5. Then, we focused on adjusting the "look back" parameter, which determines the days short-term memory needs to record, and ﬁnally found 33 days of looking back for the best performance.

<!-- b000171 | prose | pages [10] -->
Because of the randomness of the neural network, after 150 times of training, we get the following prediction for the reported number on March 1st, 2023, and the predicted average score reported numbers for 60 days (Figure.8).

<!-- b000172 | prose | pages [10] -->
(a) Distribution of Predicted Results on March 1st (b) Average Reported Numbers on the Next 60 Days

<!-- b000173 | caption | pages [10] -->
Figure 8: The Prediction Result Graph of the Model

<!-- b000174 | heading | pages [10] -->
4.2.4 Prediction Interval from the Result

<!-- b000175 | prose | pages [10] -->
The LSTM model created in 4.2.2 was trained for 150 times. Then, we can obtain the conﬁdence interval of the variation in March 1st, 2023 by statistical calculation. The average for predicted data is 21, 843.73, and the standard deviation is 560.21. We choose the 95% conﬁdence interval with the |z| value of 1.96. The CI can be calculated by:

<!-- b000176 | prose | pages [10] -->
(2) [µ −|z| ∗sd, µ + |z| ∗sd] Therefore, the prediction interval is [20745.72, 22914.74] by 95% conﬁdence.

<!-- b000177 | furniture | pages [11] -->
Team # 2311035

<!-- b000178 | furniture | pages [11] -->
Page 10 of 22

<!-- b000179 | heading | pages [11] -->
4.3 Correlation between Hard-mode Percentage and Words

<!-- b000180 | prose | pages [11] -->
If we consider lexical attributes from sample data, the result of correlation analysis will be biased. Therefore, we extract some basic properties of the word itself. Here we use four attributes: daily frequency, initial letter, serial letters, and average letter frequency.

<!-- b000181 | prose | pages [11] -->
• Daily frequency: From the Leipzig Corpora Collection[6], we ﬁnd a word list that counts the frequency of words in daily life in 2022. Then, we extract all ﬁve-length English words and take their normalized rank as the ﬁrst feature.

<!-- b000182 | prose | pages [11] -->
• Initial letter: A binary variable shown whether the initial letter is a vowel.

<!-- b000183 | prose | pages [11] -->
• Consecutive letters: Another binary variable indicated whether the word contains consecu- tive letters, such as "rr" in "carry".

<!-- b000184 | prose | pages [11] -->
• Average letter frequency: By applying the frequency of letters in the alphabet from Concise Oxford Dictionary (9th edition, 1995), we create a variable to record the average frequency among ﬁve letters for each word[7].

<!-- b000185 | prose | pages [11] -->
We took a linear regression on the Hard Mode ratio to determine the eﬀect of these four lexical attributes. The detailed result is shown below in Figure.9:

<!-- b000186 | caption | pages [11] -->
Figure 9: Linear Regression on Ratio

<!-- b000187 | prose | pages [11] -->
Therefore, words will not aﬀect the The F-statistics is 1.69, less than 2.397 (α = 0.05). percentage of scores reported in Hard Mode at 5% signiﬁcance level. Moreover, the conclusions are the same if we turn to analyze those four t-statistics.

<!-- b000188 | furniture | pages [12] -->
Team # 2311035

<!-- b000189 | furniture | pages [12] -->
Page 11 of 22

<!-- b000190 | heading | pages [12] -->
5 Task 2: Model for Predicting Percentage Distribution

<!-- b000191 | heading | pages [12] -->
5.1 Features Used to Measure the Performance of Reported Results

<!-- b000192 | prose | pages [12] -->
Notice that there are two main aspects for estimating the model, time and diﬃculty of word. We ﬁrst verify the correlation between time and the percentage distribution in that case. We use a weighted average (wt) to represent the performances in reported results, with wt = !7 i=1 i ∗itry. Then we did the linear regression of wt on time and discovered that the p-value of time is 0.457, which is much larger than 0.05. It shows no signiﬁcant correlation between performance and time, so we consider the relationship between the performance and the diﬃculty of word. We will use those four attributes mentioned in chapter 4.3. Additionally, we add two new lexical attributes: depth and the maximum number of repeated letters.

<!-- b000193 | prose | pages [12] -->
• Depth: As mentioned in the literature review, depth can show the expected times for ﬁnding the correct answers with the help of the optimal decision tree – the larger the depth, the more challenging to answer the word.

<!-- b000194 | prose | pages [12] -->
• Maximum same letter numbers (charNum): Based on Wordle game mechanics, it is hard to think of the same letter when it gets a green or yellow square response. We tend to try a letter that has yet to get a response. Repeating words also reduces the amount of information given to the player. For example, with the target word "wheel", if the players have already known that the correct answer contains "e", "h", "l", and "w", they will prefer to guess "whale" instead of "wheel". Because "whale" can provide more information than "wheel".

<!-- b000195 | prose | pages [12] -->
Moreover, the larger the number of same letters is, the more complex the problem is.

<!-- b000196 | heading | pages [12] -->
5.2 Feature Engineering

<!-- b000197 | prose | pages [12] -->
After scanning the data, it was found that for the feature "Daily frequency", some words in the list have massive ranks. These ranks are so huge that should be considered as outliers. To reduce the impact of outliers in the model, RobustScaler is used to normalize the data.

<!-- b000198 | prose | pages [12] -->
Until now, the features that measure the diﬃculty of words are deﬁned by human intuition. Those features should be further analyzed and determined their contributions to the word diﬃculty. Therefore, Recursive Feature Elimination (RFE) algorithm was used to rank those six features. Finally, "Daily frequency", "CharNum" and "Letter frequency" were selected as three dominant features.

<!-- b000199 | heading | pages [12] -->
5.3 XGBoost Model Training

<!-- b000200 | prose | pages [12] -->
As shown in Figure.10, we use seven XGBoost models to train each associated percentage of (1, 2, 3, 4, 5, 6, X) for a ﬁxed word, using "Daily frequency", "CharNum" and "Initial letter". During the training process, cross-validation was used to determine the corresponding hyperparameters of each XGBoost model. Using the determined hyperparameters, the model’s coeﬃcient of determination (R2) is 0.68, showing that the model is indeed capable of predicting.

<!-- b000201 | furniture | pages [13] -->
Team # 2311035

<!-- b000202 | furniture | pages [13] -->
Page 12 of 22

<!-- b000203 | caption | pages [13] -->
Figure 10: The Process of XGBoost Training

<!-- b000204 | heading | pages [13] -->
5.4 Uncertainties Involved in the Model

<!-- b000205 | prose | pages [13] -->
Since our model was based on XGBoost, we need to use sensitivity analysis to measure the uncertainty of the model. We chose three words with similar diﬃculties: "Royal", "Sport", and "Prove", since diﬀerences among their daily frequency ranking and average letter frequency are both less than 2%. Additionally, "Royal" is a puzzle published on April 12th, 2022, which means its percentage distribution is known, while the remaining two are still unknown. We use our model to predict these two unknown percentage models and compare their diﬀerences with the distribution of "Royal".

<!-- b000206 | prose | pages [13] -->
Using a weighted average of distributions is a straightforward way to compare the diﬀerences between distributions, but equally weighted averages will make a loss in information. For example, the gap between 3 tries and 4 tries is smaller than the gap between 6 tries and X. After much deliberation, we ﬁnally settled on an unequally weighted average Ew on every word, which is:

<!-- b000207 | prose | pages [13] -->
(3) Ew = 1try + 3 ∗2try + 5 ∗3try + 6 ∗4try + 7 ∗5try + 9 ∗6try + 11 ∗Xtry

<!-- b000208 | prose | pages [13] -->
to compare the diﬀerences between distributions on diﬀerent words.

<!-- b000209 | caption | pages [13] -->
Table 3: Sensitivity Analysis

<!-- b000210 | prose | pages [13] -->
charNum letterFreq Freqrankscale Ew royal -0.3638 1 6.10164 605 sport -0.3624 (0.38%) 1 (0%) 6.1195 (0.29%) 601.3349 (0.66%) prove -0.3620 (0.50%) 1 (0%) 6.01592 (-1.4%) 607.6483 (0.44%)

<!-- b000211 | prose | pages [13, 14] -->
As results shown in Table.3 that the variation range of Ew is within 1%, thus the uncertainty of the model is low.

<!-- b000212 | furniture | pages [14] -->
Team # 2311035

<!-- b000213 | furniture | pages [14] -->
Page 13 of 22

<!-- b000215 | prose | pages [14] -->
The uncertainty may also caused by the prediction loss. When we trained seven independent XGBoost models, the sum percentages of 7 tries could not be completely equal to 100%. The predicted values of 25 randomly selected test data are shown in the ﬁgure.11 below:

<!-- b000216 | caption | pages [14] -->
Figure 11: Total Sum of Percentages in Performances

<!-- b000217 | prose | pages [14] -->
The sum of the 25 predicted values falls within the interval of (98,102), with a variance of 0.71 against 100. So the uncertainty is relatively small, indicating the low uncertainty.

<!-- b000218 | heading | pages [14] -->
5.5 Predicted Distribution of EERIE

<!-- b000219 | prose | pages [14] -->
Taking "EERIE" into the established model gives the following results (Figure.12).

<!-- b000220 | caption | pages [14] -->
Figure 12: Pie Chart of Expected Distribution of Reported Scores on EERIE

<!-- b000221 | prose | pages [14, 15] -->
This prediction result shows a relatively large Ew value of 709.9076, which means that this word is preliminarily diﬃcult. The diﬃculty analysis will be done in task 3. As mentioned above, with relatively high R2 and less uncertainty, we have relatively high conﬁdence in the prediction of "EERIE".

<!-- b000222 | furniture | pages [15] -->
Team # 2311035

<!-- b000223 | furniture | pages [15] -->
Page 14 of 22

<!-- b000225 | heading | pages [15] -->
6 Task 3: Classiﬁcation of Words

<!-- b000226 | heading | pages [15] -->
6.1 Deﬁnition of Word Diﬃculty

<!-- b000227 | prose | pages [15] -->
In this task, it is required to classify solution words by diﬃculty. Since the distribution of reported results depends mainly on the diﬃculty of the word, we decided to use the unequally weighted average mentioned in chapter 5.4 as the measurement of word diﬃculty.

<!-- b000228 | prose | pages [15] -->
To label the data provided, we ﬁrst calculated the unequally weighted average of each word. We found that nearly 60% of the points fell between 600 and 700, while the other 40% was distributed almost evenly on two sides (Figure.13). Thus, we decided classiﬁcation labels as "easy", "medium", and "hard" (Table.4). The smaller the unequally weighted average represents, the higher percentage of itry with small i. In other words, the word is more simple.

<!-- b000229 | caption | pages [15] -->
Figure 13: Distribution of Weighted AveragePerformances

<!-- b000230 | caption | pages [15] -->
Table 4: Standard of Diﬃculty Label

<!-- b000231 | prose | pages [15] -->
<600 600-700 >700 wt label easy medium hard

<!-- b000232 | furniture | pages [16] -->
Team # 2311035

<!-- b000233 | furniture | pages [16] -->
Page 15 of 22

<!-- b000234 | heading | pages [16] -->
6.2 Feature Engineering

<!-- b000235 | prose | pages [16] -->
Since the classiﬁcation of word diﬃculty is related to the distribution of the performance, we will still use the three features selected by the RFE algorithm in chapter 5. According to these three features and assigned labels, the classiﬁcation diagram of 359 provided data is shown in Figure.14(a):

<!-- b000236 | prose | pages [16] -->
(a) Without Target Word "EERIE" (b) With Target Word "EERIE"

<!-- b000237 | caption | pages [16] -->
Figure 14: Classiﬁcation Diagrams of Weighted Perfomances

<!-- b000238 | prose | pages [16] -->
It shows that the blue dots (easy) are concentrated in areas where freqRankscale is low (more common in life), letterFreq is high (more common in composing letters), and charNum is low (fewer repeated letters). The red dots (hard) are spread over contrary areas, while the green dots (median) are mostly in areas between them.

<!-- b000239 | heading | pages [16] -->
6.3 Model Construction and Prediction

<!-- b000240 | prose | pages [16] -->
We divided the sample data into the training set and the test set with the proportion of 3:1, and trained the RBF kernel SVM model. The three-dimensional features of EERIE is (0.0226, 9.7215, 3). After taking it into the model, we got the prediction label of "EERIE" as "hard", which was also consistent with the unequally weighted average result of its performance distribution in chapter 5 (709.9076>700). The above ﬁgure shows the position of the "EERIE" in the sample data space (Fig.14(b))

<!-- b000241 | heading | pages [16] -->
6.4 Model Evaluation

<!-- b000242 | prose | pages [16] -->
• The Table.5 below shows four important metrics of classiﬁcation model evaluation. They are all above 0.6, reﬂecting the high accuracy (can be described as higher than 60%) of the model.

<!-- b000243 | furniture | pages [17] -->
Team # 2311035

<!-- b000244 | furniture | pages [17] -->
Page 16 of 22

<!-- b000245 | caption | pages [17] -->
Table 5: Four Criterias for Evaluating Model

<!-- b000246 | prose | pages [17] -->
Precision score Recall score F1 score Accuracy score 0.6762 0.6556 0.6634 0.6556

<!-- b000247 | prose | pages [17] -->
• The confusion matrix(Figure.15(a)) shows that the classiﬁcation for "easy" and "medium" is very good, but the classiﬁcation for "Hard" is relatively weak.

<!-- b000248 | prose | pages [17] -->
• The ROC curve (Figure.15(b)) shows the average curve of three types. The closer the ROC curve is to the upper left corner, the higher its sensitivity and the lower the misdiagnosis rate, thus our model have a good performance of prediction.

<!-- b000249 | prose | pages [17] -->
(a) Confusion Matrix of the Model (b) ROC Curve of the Model

<!-- b000250 | caption | pages [17] -->
Figure 15: Classiﬁcation Diagrams of Weighted Perfomances

<!-- b000251 | heading | pages [17] -->
7 Task 4: Other Interesting Findings

<!-- b000252 | heading | pages [17] -->
7.1 Fundamental Diﬀerence in Wordle Playing Strategy between Human

<!-- b000253 | prose | pages [17] -->
Brain and Machine Learning As mentioned in Literature Review, there is an optimal strategy developed by the decision tree algorithm, in which the only thing that aﬀects the number of tries used for each word is the word depth in the tree. However, when we analyzed the percentage distribution of the reported results (Figure.16), we found that the correlation between Depth and wt in the data set is very low, even smaller than the correlation between charNum and wt.

<!-- b000254 | furniture | pages [18] -->
Team # 2311035

<!-- b000255 | furniture | pages [18] -->
Page 17 of 22

<!-- b000256 | caption | pages [18] -->
Figure 16: Heat Map about Correlation among wt, CharNum and Depth

<!-- b000257 | prose | pages [18] -->
It indicates that the depth feature contributes little to the performance of the player of Wordle.

<!-- b000258 | prose | pages [18] -->
This uncorrelation shows that when people play Wordle, they are less likely to do the puzzle with the help of the optimal strategy developed by the machine. Instead, humans have their own strategies and minds to deal with the puzzle. The given data illustrates the diﬀerence between machine "thinking" and human thinking, which is a provoking aspect that can be further studied.

<!-- b000259 | heading | pages [18] -->
7.2 Other Interesting Features

<!-- b000260 | prose | pages [18] -->
• Over time, the players’ performances on the problem barely improved. This is a counter- intuitive trait. Because intuitively, the longer a game is released, the better it will be understood and performed by the game players. Maybe it is caused by the problem of insuﬃcient sample data.

<!-- b000261 | prose | pages [18] -->
• Holidays also aﬀect players’ reported scores and performances to some extent. For example, both the number of reported results and the number in hard mode on Christmas Day are signiﬁcantly lower than the data on adjacent days.

<!-- b000262 | prose | pages [18] -->
• We have estimated that the percentages in hard mode has no correlation with the attributes of words in chapter 4. However, according to Figure.17, the percentage of hard mode tend to keep growing in the future.

<!-- b000263 | furniture | pages [19] -->
Team # 2311035

<!-- b000264 | furniture | pages [19] -->
Page 18 of 22

<!-- b000265 | caption | pages [19] -->
Figure 17: The Percentage of Hard Mode

<!-- b000266 | prose | pages [19] -->
Based on this information, we can speculate that the percentage of hard mode is related to the time, aﬀected by players’ familiarity with the game mechanics. With the increase of time, Players tend to become more and more challenging.

<!-- b000267 | prose | pages [19] -->
• Figure.18 shows the scatter diagram of the distribution on the percentage of (1, 2, 3, 4, 5, 6, X). The yellow points, which indicate the percentage of 4 tries, are always on the top of the plots. No matter how the time and diﬃculty of the word change, the maximum-occupied try is always 4. It veriﬁes the conclusion that the average optimal solution of the optimal decision tree is 4.

<!-- b000268 | caption | pages [19] -->
Figure 18: The Scatter Diagram of Distribution in Performances

<!-- b000269 | heading | pages [19] -->
8 Strengths and Weaknesses

<!-- b000270 | heading | pages [19] -->
8.1 Strengths

<!-- b000271 | prose | pages [19] -->
• The model we used (LSTM neural networks) has higher accuracy and better performance than classical methods, such as ARIMA. In addition, it can process both single data points and the entire data series, making it suitable for processing datasets with time series and dealing with the main problems in task 1.

<!-- b000272 | furniture | pages [20] -->
Team # 2311035

<!-- b000273 | furniture | pages [20] -->
Page 19 of 22

<!-- b000274 | prose | pages [20] -->
• The result we concluded in task 2 and task 3 are perfectly matched, which shows a high accuracy and high level of conﬁdence in our model. More speciﬁcally, the result of task 2 shows that people have poor performance dealing with "EERIE" in Wordle in general. At the same time, the result of task 3 shows that "EERIE" is a diﬃcult word in the "hard" label.

<!-- b000275 | heading | pages [20] -->
8.2 Weaknesses

<!-- b000276 | prose | pages [20] -->
• The impact of special days (such as holidays or the MCM contests) is not taken into account.

<!-- b000277 | prose | pages [20] -->
• The data is collected by tweeets reported by players, may existing information gaps and inﬂuence the ﬁnal expecatation results.

<!-- b000278 | prose | pages [20] -->
• As the percentage data given by sample is rounded oﬀ, precision errors between data may occur when we substitute it into the model, and the total number of percentage in performances may not be 100.

<!-- b000279 | prose | pages [20] -->
• The SVM classiﬁcation model is weak in recognizing "hard" words.

<!-- b000280 | furniture | pages [21] -->
Team # 2311035

<!-- b000281 | furniture | pages [21] -->
Page 20 of 22

<!-- b000282 | prose | pages [21] -->
Shenzhen, 518000 February 21, 2023

<!-- b000283 | prose | pages [21] -->
129 W. 29th Street 11th Floor New York, NY, 10001-5105

<!-- b000284 | prose | pages [21] -->
Dear Puzzle Editor of the New York Times, I’m writing to express our keen interest in the Wordle game on your website. Even one of our team members has been a big fan of Wordle since its launch, so we strongly hope that our model and predictions results will lead to a better future for your game.

<!-- b000285 | prose | pages [21] -->
Firstly, we used the LSTM model to predict the total number of players in the future. Although the total number of players will continue to decline, the percentage of the hard mode will fluctuate to rise. It indicates the hidden nature of players' challenging. However, this challenge has no significant correlation with the attributes of the word, so we suggest tweaking the game mechanics to take advantage of the players’ challenge (more details below).

<!-- b000286 | prose | pages [21] -->
Secondly, we used XGBoost to predict the distribution of players' performances on a certain word. If the target word on March 1st were EERIE, the distribution would look like figure shown on the right. Although the small error caused by the round-off may affect the correctness, it is guaranteed that the fluctuation is less than 1%. We have a great deal of confidence in the correctness of the distribution prediction.

<!-- b000287 | prose | pages [21] -->
Finally, we developed a model to measure the difficulty levels of words based on the sample data and the attributes of the words themselves. We quantified word difficulty for levels below 600 as easy, 600 to 700 as medium, and more than 700 as hard. For example, the word EERIE will have a difficulty level of 709.9076 (as a hard word). We use the confusion matrix, ROC, and other metrics to evaluate the model with a high accuracy of nearly 70%. Therefore, this model can help you accurately measure the word difficulty in Wordle game.

<!-- b000288 | prose | pages [21] -->
In addition, we found that the average guessing time was always four with different words and dates. Some important holidays also affect the number of players. For better forecasting and planning in the future, it is essential to increase players' willingness to report their scores. At the same time, we compared the optimal solution of the Poirrier decision tree with the players’ strategy and thinking. Although we could get the same expected average (four times), the process from the human brain is very different from the optimal solution of the decision tree. It shows the difference between the human brain and machine learning towards Wordle game.

<!-- b000289 | furniture | pages [22] -->
Team # 2311035

<!-- b000290 | furniture | pages [22] -->
Page 21 of 22

<!-- b000291 | prose | pages [22] -->
Based on these conclusions, we strongly recommend adding a difficulty factor and a reward item to wordle games. The difficulty level determines the players’ final score according to the mode chosen by the player and the difficulty label of the words by our classification model. In addition, the player can rank himself among all players according to his accumulated scores, which will significantly improve players' willingness to challenge. Moreover, we have simulated the reward mechanism of the game in the following figure.

<!-- b000292 | prose | pages [22] -->
One of the two props can be randomly gained at the first sharing of results in one day, improving the accuracy of future samples and spreading the game's influence.

<!-- b000293 | prose | pages [22] -->
Our model and suggestions can help increase awareness and participation in your game. Good luck with your future development

<!-- b000294 | prose | pages [22] -->
Best wishes!

<!-- b000295 | prose | pages [22] -->
Yours sincerely,

<!-- b000296 | furniture | pages [22] -->
Team #2311035

<!-- b000297 | furniture | pages [23] -->
Team # 2311035

<!-- b000298 | furniture | pages [23] -->
Page 22 of 22

<!-- b000299 | heading | pages [23] -->
References

<!-- b000300 | references | pages [23] -->
[1] Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computation,

<!-- b000301 | references | pages [23] -->
9(8), 17351780. https://doi.org/10.1162/neco.1997.9.8.1735

<!-- b000302 | references | pages [23] -->
[2] Siami-Namini, S., Tavakoli, N., & Siami Namin, A. (2018). A comparison of Arima and LSTM

<!-- b000303 | references | pages [23] -->
in forecasting time series. 2018 17th IEEE International Conference on Machine Learning

<!-- b000304 | references | pages [23] -->
and Applications (ICMLA). https://doi.org/10.1109/icmla.2018.00227

<!-- b000305 | references | pages [23] -->
[3] Poirrier,

<!-- b000306 | references | pages [23] -->
L. (2022,

<!-- b000307 | references | pages [23] -->
January 23). Laurent’s Notes. Mathematical optimization over

<!-- b000308 | references | pages [23] -->
Wordle

<!-- b000309 | references | pages [23] -->
decision

<!-- b000310 | references | pages [23] -->
trees

<!-- b000311 | references | pages [23] -->
–

<!-- b000312 | references | pages [23] -->
Laurent’s

<!-- b000313 | references | pages [23] -->
notes.

<!-- b000314 | references | pages [23] -->
Retrieved

<!-- b000315 | references | pages [23] -->
February

<!-- b000316 | references | pages [23] -->
18,

<!-- b000317 | references | pages [23] -->
2023,

<!-- b000318 | references | pages [23] -->
from

<!-- b000319 | references | pages [23] -->
https://www.poirrier.ca/notes/wordle/#decision-trees

<!-- b000320 | references | pages [23] -->
[4] Selby,

<!-- b000321 | references | pages [23] -->
A.

<!-- b000322 | references | pages [23] -->
(2022,

<!-- b000323 | references | pages [23] -->
January

<!-- b000324 | references | pages [23] -->
19).

<!-- b000325 | references | pages [23] -->
The

<!-- b000326 | references | pages [23] -->
best

<!-- b000327 | references | pages [23] -->
strategies

<!-- b000328 | references | pages [23] -->
for

<!-- b000329 | references | pages [23] -->
wordle.

<!-- b000330 | references | pages [23] -->
The

<!-- b000331 | references | pages [23] -->
best

<!-- b000332 | references | pages [23] -->
strategies

<!-- b000333 | references | pages [23] -->
for

<!-- b000334 | references | pages [23] -->
Wordle

<!-- b000335 | references | pages [23] -->
-

<!-- b000336 | references | pages [23] -->
Things

<!-- b000337 | references | pages [23] -->
(various).

<!-- b000338 | references | pages [23] -->
Retrieved

<!-- b000339 | references | pages [23] -->
February

<!-- b000340 | references | pages [23] -->
18,

<!-- b000341 | references | pages [23] -->
2023,

<!-- b000342 | references | pages [23] -->
from

<!-- b000343 | references | pages [23] -->
https://sonorouschocolate.com/notes/index.php?title=The_best_strategies_for_Wordle

<!-- b000344 | references | pages [23] -->
[5] Olah, C. (2015, August 27). Understanding LSTM networks. Understanding LSTM Net-

<!-- b000345 | references | pages [23] -->
works – colah’s blog. Retrieved February 19, 2023, from http://colah.github.io/posts/2015-

<!-- b000346 | references | pages [23] -->
08-Understanding-LSTMs/

<!-- b000347 | references | pages [23] -->
[6] Corpora collection. Download Corpora English. (n.d.). Retrieved February 18, 2023, from

<!-- b000348 | references | pages [23] -->
https://wortschatz.uni-leipzig.de/en/download/English

<!-- b000349 | references | pages [23] -->
[7] University Communications | University of Notre Dame. (1970, February 23). University of

<!-- b000350 | references | pages [23] -->
Notre Dame. Retrieved February 18, 2023, from https://www.nd.edu/
