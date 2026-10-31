# P-C-2023-2311717-64b80c37

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
2311717

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | heading | pages [1] -->
Riddle of Wordle: Mining the Secret of Number Scores & Solution Words

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
Wordle is a popular puzzle currently offered daily by the New York Times. The simple rules and clever propagation properties have contributed to its popularity. In this article, we build two prediction models for the prediction of the Twitter report number intervals and result distributions, respectively, and develop a model for classifying the difficulty of solution words.

<!-- b000012 | prose | pages [1] -->
In TASK 1: After data preprocessing, we build a Wordle report number prediction model based on 3rd-order gaussian regression and a non-homogeneous Poisson process from a statis- tical perspective. Among them, the Gaussian regression is used to predict the trend signs of report numbers, while the non-homogeneous Poisson process predicts the stochastic fluctua- tions of report numbers on this basis. Moreover, we use the popularity relaxation function to correct the stochastic process, which better approximates the popularity change. At a confi- dence level of 75%, we predict the interval of the number of reports on March 1, 2023 to be [7654, 20154]. In addition, we extract 8 attributes of words in terms of the number of letters, letter location and so on, finding that these attributes did not have an effect on the percentage of players' Hard Mode choices. Players' confidence in their performance ability and their play mentality may be the main reasons for whether they choose the Hard Mode or not.

<!-- b000013 | prose | pages [1] -->
In TASK 2: We first extract the data features that affect the distribution of reported results, including word attributes, and the percentage of difficulty patterns. Then, we build a BP neural network to make preliminary predictions on the distribution of guessing results for a certain solution word in the future. To improve the generalization performance of the prediction results, we build an integrated BP neural network based on Bagging. Then, we predict the distribu- tion of the reported results of EERIE on March 1, 2023 as (0, 1, 6, 25, 31, 25, 13) (in %). We have more than 80% confidence that the absolute error of the predicted outcome for the per- centage of each possible result does not exceed 5%.

<!-- b000014 | prose | pages [1] -->
In TASK 3: First, we build a word difficulty induction model based on the K-Means from the distribution of user's reported data, and divide the difficulty into 4 classes. Then, we explore the association between word attributes and difficulty based on Pearson’s coefficients, and take the attributes with correlation coefficients greater than 0.6 as difficulty classification at- tributes to build a word difficulty classification model. Moreover, we find that the frequency of the first and second letters of the solution words, the number of vowels contained in the pronunciation and the number of word properties have a high correlation with the difficulty classification. Finally, the difficulty classification result of EERIR is the most difficult.

<!-- b000015 | prose | pages [1] -->
In TASK 4: While exploring the statistical properties of the number of reports, we find that the distribution of the number of reports showed a similar pattern to its trend over time. In addition, we also notice that the percentage fluctuation of 3 tries to complete the game was the largest in the 359 days of reported outcome distribution data.

<!-- b000016 | prose | pages [1] -->
Finally, we perform a sensitivity analysis of the model and investigate the effect of changes in the variable parameters of the model on the results.

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | keywords | pages [1] -->
Keywords: Gaussian regression;  Poisson process;  BP neural network;  K-Means

<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | furniture | pages [2] -->
Team # 2311717

<!-- b000021 | furniture | pages [2] -->


<!-- b000022 | furniture | pages [2] -->


<!-- b000023 | furniture | pages [2] -->


<!-- b000024 | furniture | pages [2] -->


<!-- b000025 | furniture | pages [2] -->


<!-- b000026 | furniture | pages [2] -->


<!-- b000027 | furniture | pages [2] -->


<!-- b000028 | furniture | pages [2] -->


<!-- b000029 | furniture | pages [2] -->


<!-- b000030 | furniture | pages [2] -->


<!-- b000031 | furniture | pages [2] -->


<!-- b000032 | furniture | pages [2] -->


<!-- b000033 | furniture | pages [2] -->
Page 2 of 25

<!-- b000034 | heading | pages [2] -->
Contents

<!-- b000035 | contents | pages [2] -->
1 Introduction ...................................................................................................... 3

<!-- b000036 | contents | pages [2] -->
1.1 Problem Background ....................................................................................................... 3

<!-- b000037 | contents | pages [2] -->
1.2 Restatement of the Problem ............................................................................................. 3

<!-- b000038 | contents | pages [2] -->
1.3 Literature Review ............................................................................................................. 3

<!-- b000039 | contents | pages [2] -->
1.4 Our Work .......................................................................................................................... 4

<!-- b000040 | contents | pages [2] -->
2 Assumptions and Justifications ....................................................................... 5

<!-- b000041 | contents | pages [2] -->
3 Notations ........................................................................................................... 5

<!-- b000042 | contents | pages [2] -->
4 Data pre-processing ......................................................................................... 6

<!-- b000043 | heading | pages [2] -->
5 Task 1: Report Number Prediction Model & Game Mode Selection

<!-- b000044 | prose | pages [2] -->
Analysis ................................................................................................................ 6

<!-- b000045 | prose | pages [2] -->
5.1 Data Exploration .............................................................................................................. 7

<!-- b000046 | prose | pages [2] -->
5.2 Wordle Report Number Prediction Model ....................................................................... 8

<!-- b000047 | prose | pages [2] -->
5.3 Analysis of Game Mode Selection ................................................................................. 11

<!-- b000048 | heading | pages [2] -->
6 Task 2: A Prediction Model for The Distribution of The Reported Results

<!-- b000049 | prose | pages [2] -->
............................................................................................................................. 14

<!-- b000050 | prose | pages [2] -->
6.1 Building the BP Neural Network-based Prediction Model for the distribution of word- guessing results .................................................................................................................... 14

<!-- b000051 | prose | pages [2] -->
6.2 Analysis of Uncertainties Affecting the Model .............................................................. 16

<!-- b000052 | prose | pages [2] -->
6.3 Analysis of the Results of the Prediction Model ............................................................ 17

<!-- b000053 | prose | pages [2] -->
7 Task 3: Word Difficulty Classification Model ............................................. 17

<!-- b000054 | prose | pages [2] -->
7.1 The Establishment of Word Difficulty Classification .................................................... 18

<!-- b000055 | prose | pages [2] -->
7.2 Analysis of Word Difficulty Classification Results ....................................................... 20

<!-- b000056 | prose | pages [2] -->
8 Task 4: Other Interesting Features ............................................................... 21

<!-- b000057 | prose | pages [2] -->
9 Sensitivity Analysis ......................................................................................... 22

<!-- b000058 | prose | pages [2] -->
10 Model Evaluation and Further Discussion ................................................ 23

<!-- b000059 | prose | pages [2] -->
10.1 Strengths ...................................................................................................................... 23

<!-- b000060 | prose | pages [2] -->
10.2 Weaknesses .................................................................................................................. 23

<!-- b000061 | prose | pages [2] -->
10.3 Further Discussion ....................................................................................................... 23

<!-- b000062 | prose | pages [2] -->
11 Conclusion ..................................................................................................... 23

<!-- b000063 | prose | pages [2] -->
References .......................................................................................................... 24

<!-- b000064 | prose | pages [2] -->
Letter .................................................................................................................. 25

<!-- b000065 | furniture | pages [2] -->


<!-- b000066 | furniture | pages [2] -->


<!-- b000067 | furniture | pages [2] -->


<!-- b000068 | furniture | pages [3] -->
Team # 2311717

<!-- b000069 | furniture | pages [3] -->


<!-- b000070 | furniture | pages [3] -->


<!-- b000071 | furniture | pages [3] -->


<!-- b000072 | furniture | pages [3] -->


<!-- b000073 | furniture | pages [3] -->


<!-- b000074 | furniture | pages [3] -->


<!-- b000075 | furniture | pages [3] -->


<!-- b000076 | furniture | pages [3] -->


<!-- b000077 | furniture | pages [3] -->


<!-- b000078 | furniture | pages [3] -->


<!-- b000079 | furniture | pages [3] -->


<!-- b000080 | furniture | pages [3] -->


<!-- b000081 | furniture | pages [3] -->


<!-- b000082 | furniture | pages [3] -->
Page 3 of 25

<!-- b000083 | heading | pages [3] -->
1 Introduction

<!-- b000084 | heading | pages [3] -->
1.1 Problem Background

<!-- b000085 | prose | pages [3] -->
Homer is a term used in the sport of baseball and is an informal American English word. Amazingly, Homer (home run) was searched over 79,000 times on the Cambridge Dictionary website and was searched 65,401 times on May 5. With that, Homer became the Cambridge Dictionary's 2022 Word of the Year. You may be wondering why, but it starts with Wordle, a very popular word-guessing game overseas. In 2022, the online puzzle game Wordle was all over social media. And Wordle's answer that day was Homer, which was difficult for non-US users who were not familiar with the word.

<!-- b000086 | prose | pages [3] -->
Wordle is currently a popular daily puzzle offered by The New York Times and has grown in popularity with more than 60 versions available. Players can choose between "regular mode" or "hard mode. Players attempt to solve the puzzle by guessing a five-letter word in six or fewer attempts, with each guess receiving feedback and a change in the color of the tile (green, yellow, gray). Note: Each guess must be a real word in English. Guesses that are not recognized as words by the contest are not allowed.

<!-- b000087 | prose | pages [3] -->
： A green tile indicates that the letter in that tile is in the word and in the correct location. ： A yellow tile indicates that the letter in that tile is in the word but in the wrong location. ： A gray tile indicates that the letter in that tile is not included in the word.

<!-- b000088 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000089 | prose | pages [3] -->
Considering the background information and the results in this file, we need to solve the following problems:  Develop a model to account for changes in the number of reported outcomes and create a

<!-- b000090 | prose | pages [3] -->
prediction interval for the number of reported outcomes on March 1, 2023. Analyze the extent to which attributes of words affect players' mode choices.  Develop a model to predict the distribution of reported outcomes. Analyze the uncertainty

<!-- b000091 | prose | pages [3] -->
factors that exist in the model and predictions.  Develop a model to classify solution words by difficulty. Identify the attributes of the

<!-- b000092 | prose | pages [3] -->
words associated with each classification.  Describes other interesting features of the dataset.

<!-- b000093 | heading | pages [3] -->
1.3 Literature Review

<!-- b000094 | prose | pages [3] -->
In recent years, with the popularity of the Internet, social networks have gradually become the main medium for discussing what is happening in the real world, and users can generate and disseminate rich data streams on social platforms (e.g. Twitter) to gain insights into hot events that are happening. Popularity modeling and prediction have a wide range of applica- tions in marketing, opinion monitoring, advertising and other scenarios, and time-series-based trend analysis is a research topic that has received much attention in the field of data mining and social network analysis in recent years. The idea of this type of research mainly draws on financial and epidemiological models. Shen et al [1] first established a Reinforced Poisson

<!-- b000095 | furniture | pages [3] -->


<!-- b000096 | furniture | pages [4] -->
Team # 2311717

<!-- b000097 | furniture | pages [4] -->


<!-- b000098 | furniture | pages [4] -->


<!-- b000099 | furniture | pages [4] -->


<!-- b000100 | furniture | pages [4] -->


<!-- b000101 | furniture | pages [4] -->


<!-- b000102 | furniture | pages [4] -->


<!-- b000103 | furniture | pages [4] -->


<!-- b000104 | furniture | pages [4] -->


<!-- b000105 | furniture | pages [4] -->


<!-- b000106 | furniture | pages [4] -->


<!-- b000107 | furniture | pages [4] -->


<!-- b000108 | furniture | pages [4] -->


<!-- b000109 | furniture | pages [4] -->


<!-- b000110 | furniture | pages [4] -->
Page 4 of 25

<!-- b000111 | prose | pages [4] -->
Processes (RPP) model to predict dynamic prevalence using a heterogeneous Poisson process model, and considered the "rich get richer ". Zhao et al [2] developed a SEISMIC model based on the theory of self-excited point processes, assuming that past popularity will affect the future evolution of the process, and used a double stochastic process to portray the contagion of in- formation. Wu et al [3] proposed a Bayesian network-based popularity prediction model (EPAB) based on temporal characteristics, user characteristics and network structure characteristics, and proposed the concept of early patterns to establish the relationship between early feature information and future heat changes.

<!-- b000112 | prose | pages [4] -->
However, the time series model requires the data set to contain timing information, and the data set that does not meet this condition cannot be modeled. Meanwhile, the sequential model and the deep learning method based on node behavior dynamics are not suitable for the forecast situation of this task based only on the reported data. On the one hand, the existing data set does not contain specific information such as who the reporter is, how many players there are at any given time, etc., so a node model cannot be built based on this data set. On the other hand, techniques such as deep learning are not well interpretable and cannot explain the trend of heat change mathematically, and require more training data.

<!-- b000113 | prose | pages [4] -->
In this paper, we try our best to extract all the information from the Data File. Aiming at the specific application scenario of Wordle, we not only realize the interval prediction of the number of future reports, but also carry out further analysis on the distribution of report results and the classification of word difficulty.

<!-- b000114 | heading | pages [4] -->
1.4 Our Work

<!-- b000115 | prose | pages [4] -->
We put forward three models to mine the information of the reported result data. The structure of our paper is shown in Figure 1.

<!-- b000116 | prose | pages [4] -->
Trend indication

<!-- b000117 | prose | pages [4] -->
Random fluctuation

<!-- b000118 | prose | pages [4] -->
Popular timeliness

<!-- b000119 | prose | pages [4] -->
Twitter Report Results

<!-- b000120 | prose | pages [4] -->
Mode Selection Interval Prediction

<!-- b000121 | prose | pages [4] -->
3rd-order Gaussian

<!-- b000122 | prose | pages [4] -->
Hard Mode

<!-- b000123 | prose | pages [4] -->
Regression

<!-- b000124 | prose | pages [4] -->
selection ratio

<!-- b000125 | prose | pages [4] -->
non-homogeneous

<!-- b000126 | prose | pages [4] -->
Poisson Process

<!-- b000127 | prose | pages [4] -->
correction

<!-- b000128 | prose | pages [4] -->
Word attributes

<!-- b000129 | prose | pages [4] -->
Popularity relaxation

<!-- b000130 | prose | pages [4] -->
function

<!-- b000131 | heading | pages [4] -->
（b）Task 1: Report Number Prediction Model & Game Mode Selection Analysis

<!-- b000132 | prose | pages [4] -->
Correction

<!-- b000133 | prose | pages [4] -->
Data Feature

<!-- b000134 | prose | pages [4] -->
Number of

<!-- b000135 | prose | pages [4] -->
Extraction

<!-- b000136 | prose | pages [4] -->
Word

<!-- b000137 | prose | pages [4] -->
reports

<!-- b000138 | prose | pages [4] -->
Word attribute

<!-- b000139 | prose | pages [4] -->
（a）Data Preprocessing

<!-- b000140 | prose | pages [4] -->
Hard Mode

<!-- b000141 | prose | pages [4] -->
ratio

<!-- b000142 | prose | pages [4] -->
Letter Number

<!-- b000143 | prose | pages [4] -->
Bagging

<!-- b000144 | prose | pages [4] -->
BP Neural Network BP Neural Network BP Neural Network BP Neural Network BP Neural Network

<!-- b000145 | heading | pages [4] -->
（c）Task 2: The Distribution of the Reported Results Prediction Model

<!-- b000146 | prose | pages [4] -->
K-Means

<!-- b000147 | prose | pages [4] -->
Letter Position

<!-- b000148 | prose | pages [4] -->
clustering

<!-- b000149 | prose | pages [4] -->
Other

<!-- b000150 | prose | pages [4] -->
Distribution of

<!-- b000151 | prose | pages [4] -->
report results

<!-- b000152 | prose | pages [4] -->
(e)Word Attribute

<!-- b000153 | prose | pages [4] -->
New words

<!-- b000154 | prose | pages [4] -->
Difficulty

<!-- b000155 | heading | pages [4] -->
summary

<!-- b000156 | prose | pages [4] -->
Correlation

<!-- b000157 | prose | pages [4] -->
Euclidean distance

<!-- b000158 | prose | pages [4] -->
coefficient

<!-- b000159 | prose | pages [4] -->
Word attribute

<!-- b000160 | prose | pages [4] -->
Difficulty classification

<!-- b000161 | heading | pages [4] -->
（d）Task 3: Word Difficulty Classification Model

<!-- b000162 | furniture | pages [4] -->


<!-- b000163 | caption | pages [4] -->
Figure 1: The structure of our paper

<!-- b000164 | furniture | pages [4] -->


<!-- b000165 | furniture | pages [5] -->
Team # 2311717

<!-- b000166 | furniture | pages [5] -->


<!-- b000167 | furniture | pages [5] -->


<!-- b000168 | furniture | pages [5] -->


<!-- b000169 | furniture | pages [5] -->


<!-- b000170 | furniture | pages [5] -->


<!-- b000171 | furniture | pages [5] -->


<!-- b000172 | furniture | pages [5] -->


<!-- b000173 | furniture | pages [5] -->


<!-- b000174 | furniture | pages [5] -->


<!-- b000175 | furniture | pages [5] -->


<!-- b000176 | furniture | pages [5] -->


<!-- b000177 | furniture | pages [5] -->


<!-- b000178 | furniture | pages [5] -->


<!-- b000179 | furniture | pages [5] -->
Page 5 of 25

<!-- b000180 | prose | pages [5] -->
The rest of this paper is organized as follows. In Section II, we introduce the premise assumptions and justifications, and common variables in the formulas are mentioned in Section III.  In Section IV, the data preprocessing before modeling is carried out. Section V establishes the prediction model of report number interval and explores the relationship between word attribute and pattern selection. In Section VI, we establish the report result distribution predic- tion model. In Section VII, we propose the word difficulty classification model. Section VIII continues to explore interesting features of the Data File. In Sections IX and X, the sensitivity of the model is analyzed and we further evaluate the advantages and disadvantages of the mod- els. Finally, Section XI gives out the conclusions.

<!-- b000181 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000182 | prose | pages [5] -->
We make some general assumptions to simplify our model. These assumptions together with corresponding justifications are listed below:

<!-- b000183 | heading | pages [5] -->
1. It is assumed that the change in the number of users in the report is a true reflection

<!-- b000184 | prose | pages [5] -->
of the change in players in the actual situation. There may be players who are enthusiastic about the game but do not tweet their results, so the number of reported users is often less than the actual value. However, we assume that players are willing to share their game results.

<!-- b000185 | heading | pages [5] -->
2. Assume that the game can be played only once per person per day, and that the ques-

<!-- b000186 | prose | pages [5] -->
tions are updated at 0:00 EST every day. This assumption serves as the established rule of the game. This rule reflects the analyza- bility of the reported data. Also, it demonstrates the original intention of the game designer, Wardle, who "did not want players to spend more than three minutes per day".

<!-- b000187 | heading | pages [5] -->
3. It is assumed that in the game's setting, players are seen as people with a certain level

<!-- b000188 | prose | pages [5] -->
of literacy and problem-solving skills. There is no special connection between the words given in each game, but the player's mastery of the vocabulary directly determines the steps, speed, and correctness of the an- swers. We assume that the player has the ability to solve the problem and has the option to find the answer online when he cannot guess the answer.

<!-- b000189 | heading | pages [5] -->
4. It is assumed that the historical data is a good representation of all possible Wordle

<!-- b000190 | prose | pages [5] -->
questions and player answers. Since we only have 359 days of reported results data for 2022 and as the only reference data set. The data may be unrepresentative, and for the sake of analysis, we assume that it can show the question-and-answer patterns to some extent.

<!-- b000191 | heading | pages [5] -->
3 Notations

<!-- b000192 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000193 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000194 | heading | pages [5] -->
Symbol

<!-- b000195 | prose | pages [5] -->
Description

<!-- b000196 | prose | pages [5] -->
time, where  represents the number of days from that date to January 7, 2022

<!-- b000197 | furniture | pages [5] -->


<!-- b000198 | furniture | pages [5] -->


<!-- b000199 | furniture | pages [6] -->
Team # 2311717

<!-- b000200 | furniture | pages [6] -->


<!-- b000201 | furniture | pages [6] -->


<!-- b000202 | furniture | pages [6] -->


<!-- b000203 | furniture | pages [6] -->


<!-- b000204 | furniture | pages [6] -->


<!-- b000205 | furniture | pages [6] -->


<!-- b000206 | furniture | pages [6] -->


<!-- b000207 | furniture | pages [6] -->


<!-- b000208 | furniture | pages [6] -->


<!-- b000209 | furniture | pages [6] -->


<!-- b000210 | furniture | pages [6] -->


<!-- b000211 | furniture | pages [6] -->


<!-- b000212 | furniture | pages [6] -->


<!-- b000213 | furniture | pages [6] -->
Page 6 of 25

<!-- b000214 | prose | pages [6] -->
number of results reported on the day

<!-- b000215 | furniture | pages [6] -->


<!-- b000216 | furniture | pages [6] -->


<!-- b000217 | prose | pages [6] -->
the mean value of the number of reports on the day

<!-- b000218 | furniture | pages [6] -->


<!-- b000219 | prose | pages [6] -->
frequency of a given letter

<!-- b000220 | furniture | pages [6] -->


<!-- b000221 | prose | pages [6] -->
in 359 words of result data

<!-- b000222 | prose | pages [6] -->
th letter to all words the ratio of words with the

<!-- b000223 | furniture | pages [6] -->


<!-- b000224 | furniture | pages [6] -->


<!-- b000225 | prose | pages [6] -->
number of clustering algorithm centers of mass

<!-- b000226 | heading | pages [6] -->
4 Data pre-processing

<!-- b000227 | prose | pages [6] -->
Before building the model, a preliminary check of the data in the report is needed. Ac- cording to the rules of Wordle, each word is 5 letters long. But there are unusual statistics of 4 or 6 letters in the data. Errors in words can interfere with the analysis of word attributes later, so the word data were corrected based on past answer data1. Based on the relationship between the number of reports, we found that there was a large deviation between the number of results of No. 529 and the values on the before and after dates. Therefore, we considered it as abnormal data and corrected it by taking the average value of the data for each of the two days before and after. The overall pre-processing process is shown in Figure 2.

<!-- b000228 | furniture | pages [6] -->


<!-- b000229 | caption | pages [6] -->
Figure 2: Data pre-processing

<!-- b000230 | heading | pages [6] -->
5 Task 1: Report Number Prediction Model & Game Mode Selec-

<!-- b000231 | prose | pages [6] -->
tion Analysis

<!-- b000232 | prose | pages [6] -->
To explore the variation pattern of the number of reported results obtained from Twitter over time, we first develop an interpretable model for describing and predicting the number of reports. From a statistical point of view, we portray the long-term temporal trends and stochas- tic fluctuations in the number of reports based on 3rd order gaussian regression and non-ho- mogeneous Poisson process, respectively. Moreover, we observe that the size of the stochastic fluctuations in the number of reports is not only time-dependent but also related to the current heat level, so we introduce a popularity relaxation function to modify the stochastic process model. Finally, we enumerate eight attributes related to words and analyze the influence of

<!-- b000233 | furniture | pages [6] -->


<!-- b000234 | prose | pages [6] -->
1 Data source: http://www.stockq.org/life/wordle-history.php#all

<!-- b000235 | furniture | pages [6] -->


<!-- b000236 | prose | pages [7] -->
校苑

<!-- b000237 | furniture | pages [7] -->
Team # 2311717

<!-- b000238 | furniture | pages [7] -->


<!-- b000239 | furniture | pages [7] -->


<!-- b000240 | furniture | pages [7] -->


<!-- b000241 | furniture | pages [7] -->


<!-- b000242 | furniture | pages [7] -->


<!-- b000243 | furniture | pages [7] -->


<!-- b000244 | prose | pages [7] -->
校苑数

<!-- b000245 | furniture | pages [7] -->
校苑数模

<!-- b000246 | furniture | pages [7] -->


<!-- b000247 | furniture | pages [7] -->


<!-- b000248 | furniture | pages [7] -->


<!-- b000249 | furniture | pages [7] -->


<!-- b000250 | furniture | pages [7] -->


<!-- b000251 | furniture | pages [7] -->


<!-- b000252 | furniture | pages [7] -->


<!-- b000253 | furniture | pages [7] -->
Page 7 of 25

<!-- b000254 | prose | pages [7] -->
word attributes on the choice of game mode with players through scatter plots.

<!-- b000255 | prose | pages [7] -->
校苑数模

<!-- b000256 | heading | pages [7] -->
5.1 Data Exploration

<!-- b000257 | prose | pages [7] -->
The number of reported results keeps changing over time, and Figure 3 shows the dynamic pattern of game hotness over time from the perspective of the number of people (the date takes January 7 as the starting point). In general, there is a certain pattern of popularity propagation

<!-- b000258 | prose | pages [7] -->
校苑

<!-- b000259 | prose | pages [7] -->
校苑数模

<!-- b000260 | prose | pages [7] -->
law in the number of reports on the time scale. When Wordle exploded in the early days, there was a significant increase in the number; however, when the popularity period passed, the num- ber showed a downward trend and leveled off, as shown in Figure 3(a). It is worth noting that there is a small random fluctuation between the number of reports per day and the overall trend. In addition, Figure 3(b) depicts the growth statistics of the cumulative number of reports over

<!-- b000261 | prose | pages [7] -->
校苑数模

<!-- b000262 | prose | pages [7] -->
time (359 days in total). In other words, the process of the number of reports over time can be divided into two parts, which are trend signs and random fluctuation.

<!-- b000263 | prose | pages [7] -->
校

<!-- b000264 | prose | pages [7] -->
校苑数模

<!-- b000265 | furniture | pages [7] -->


<!-- b000266 | prose | pages [7] -->
校苑数模

<!-- b000267 | furniture | pages [7] -->


<!-- b000268 | prose | pages [7] -->
(a) Short-term random fluctuations       (b) Long-term cumulative trend

<!-- b000269 | prose | pages [7] -->
模

<!-- b000270 | caption | pages [7] -->
Figure 3: Description of the number of reports

<!-- b000271 | prose | pages [7] -->
At the same time, we find that there is a correlation between the fluctuation of the number of reports within a short period and the number of reports of the game in that period. Consid-

<!-- b000272 | prose | pages [7] -->
校苑数模

<!-- b000273 | prose | pages [7] -->
ering the social property of sharing game reports on Twitter, we approximate that the number of reports in a certain period represents the recent hotness of the game.

<!-- b000274 | prose | pages [7] -->
苑数模

<!-- b000275 | prose | pages [7] -->
proximate maximum

<!-- b000276 | prose | pages [7] -->
fluctuation horizon

<!-- b000277 | furniture | pages [7] -->
校苑数模

<!-- b000278 | prose | pages [7] -->
苑数模

<!-- b000279 | furniture | pages [7] -->


<!-- b000280 | caption | pages [7] -->
Figure 4: The relationship between the size of fluctuations in the number of reports and

<!-- b000281 | prose | pages [7] -->
the popularity of the game As shown in Figure 4, its horizontal axis is the two-period moving average of the number

<!-- b000282 | furniture | pages [7] -->


<!-- b000283 | prose | pages [7] -->
模

<!-- b000284 | furniture | pages [8] -->
Team # 2311717

<!-- b000285 | furniture | pages [8] -->


<!-- b000286 | furniture | pages [8] -->


<!-- b000287 | furniture | pages [8] -->


<!-- b000288 | furniture | pages [8] -->


<!-- b000289 | furniture | pages [8] -->


<!-- b000290 | furniture | pages [8] -->


<!-- b000291 | furniture | pages [8] -->


<!-- b000292 | furniture | pages [8] -->


<!-- b000293 | furniture | pages [8] -->


<!-- b000294 | furniture | pages [8] -->


<!-- b000295 | furniture | pages [8] -->


<!-- b000296 | furniture | pages [8] -->


<!-- b000297 | furniture | pages [8] -->


<!-- b000298 | furniture | pages [8] -->
Page 8 of 25

<!-- b000299 | prose | pages [8] -->
of game reports, and its vertical axis is the fluctuation of the daily number of reports relative to the two-period moving average of the day. It can be seen that as the mean value of the sliding window for the number of reports increases, the magnitude of fluctuations becomes larger, and the boundaries of the magnitude of fluctuations appear roughly linear. It is more difficult to accurately predict the number of game reports in this period when the game is popular.

<!-- b000300 | heading | pages [8] -->
5.2 Wordle Report Number Prediction Model

<!-- b000301 | heading | pages [8] -->
5.2.1 The establishment of report number prediction model

<!-- b000302 | prose | pages [8] -->
We want to build a mathematical model based on existing data to describe the process of changing the number of reported results on Twitter over time and to predict the popularity in a certain period in the future, and the model is explanatory for the change process. The problem is a popularity prediction problem that has often been discussed in recent years.

<!-- b000303 | prose | pages [8] -->
By reviewing the literature [4], we learned that two classes of heat prediction algorithms are commonly used in the industry, including temporal models based on node behavior dynam- ics and deep learning-based methods. However, they do not apply to the scenario studied in this paper. This is mainly due to the following two reasons: 1) The existing dataset does not contain specific information such as who the reporter is and how many people in total. It is not sufficient to build a node model based on this dataset. 2) Deep learning does not have good interpretability and requires more training data to achieve better prediction results.

<!-- b000304 | prose | pages [8] -->
Therefore, we developed a Wordle Report Number Prediction model based on 3rd-order Gaussian regression and a non-homogeneous Poisson process from the statistical perspective.

<!-- b000305 | heading | pages [8] -->
⚫ A trend prediction model based on Gaussian regression

<!-- b000306 | prose | pages [8] -->
In the Data File, there is a clear sign of a trend in the time series of the number of reports. We tried several regression algorithms to fit the trend in the number of reports over time, and the best result was a 3rd order Gaussian regression with a regression equation of:

<!-- b000307 | furniture | pages [8] -->


<!-- b000308 | prose | pages [8] -->
(1)

<!-- b000309 | prose | pages [8] -->
is the regression coefficient and  is the time in where days.

<!-- b000310 | prose | pages [8] -->
Then, we use the least squares method to regress it. Let the observation of the number of , and the regression result be: daily reports be

<!-- b000311 | prose | pages [8] -->
Then its loss function is:

<!-- b000312 | furniture | pages [8] -->


<!-- b000313 | furniture | pages [8] -->


<!-- b000314 | prose | pages [8] -->
(2)

<!-- b000315 | prose | pages [8] -->
as the regression result, and the corresponding We take

<!-- b000316 | prose | pages [8] -->
dicted trend.

<!-- b000317 | prose | pages [8] -->
is the pre-

<!-- b000318 | heading | pages [8] -->
⚫ Report number prediction model based on non-homogeneous Poisson process

<!-- b000319 | prose | pages [8] -->
The Poisson distribution describes the probability of a certain number of events occurring

<!-- b000320 | furniture | pages [8] -->


<!-- b000321 | furniture | pages [9] -->
Team # 2311717

<!-- b000322 | furniture | pages [9] -->


<!-- b000323 | furniture | pages [9] -->


<!-- b000324 | furniture | pages [9] -->


<!-- b000325 | furniture | pages [9] -->


<!-- b000326 | furniture | pages [9] -->


<!-- b000327 | furniture | pages [9] -->


<!-- b000328 | furniture | pages [9] -->


<!-- b000329 | furniture | pages [9] -->


<!-- b000330 | furniture | pages [9] -->


<!-- b000331 | furniture | pages [9] -->


<!-- b000332 | furniture | pages [9] -->


<!-- b000333 | furniture | pages [9] -->


<!-- b000334 | furniture | pages [9] -->


<!-- b000335 | furniture | pages [9] -->
Page 9 of 25

<!-- b000336 | prose | pages [9] -->
over a period of time under the condition that the event occurrence rate is constant, and thus can describe the probability of a certain number of reports uploaded in a day. We assume that the number of reports each day obeys a Poisson distribution, then these Poisson distributions form a non-homogeneous Poisson process in time, i.e., a Poisson process in which the arrival intensity varies with time.

<!-- b000337 | prose | pages [9] -->
The number of reports on the day  is a random process

<!-- b000338 | prose | pages [9] -->
neous Poisson process with arrival intensity

<!-- b000339 | prose | pages [9] -->
on the day  is:

<!-- b000340 | prose | pages [9] -->
that obeys a non-homoge-

<!-- b000341 | prose | pages [9] -->
. The probability that the number of reports

<!-- b000342 | furniture | pages [9] -->


<!-- b000343 | prose | pages [9] -->
(3)

<!-- b000344 | prose | pages [9] -->
is the mean value where the meaning of of the number of re-

<!-- b000345 | prose | pages [9] -->
ports on the day . However, the mean value function cannot be derived from the available statistics. Therefore, we retreat and use the trend prediction result from the previous Gaussian regression to approximate the mean function of the number of reports such that .

<!-- b000346 | prose | pages [9] -->
instead,

<!-- b000347 | prose | pages [9] -->
Thereby, the random fluctuations of the reported number can be well portrayed by intro- ducing a non-homogeneous Poisson process. ⚫ Random process correction based on popularity relaxation function

<!-- b000348 | prose | pages [9] -->
mentioned above is not a completely independent incre- Since the random process mental process in practice, the size of its random fluctuation is affected by its popularity. By analogy with the life cycle of online public opinion [5], this paper divides the life cycle of Word- le's popularity trend. Considering that the data are counted from January 7, the initial "for- mation" stage is omitted.

<!-- b000349 | prose | pages [9] -->
i.

<!-- b000350 | prose | pages [9] -->
Explosion Period: the number of players surges due to the growth of popularity and the sharing of results on social platforms. The index of attention and action of Twitter users on this type of topic soars to its peak and fluctuates with greater uncertainty in its scope. ii.

<!-- b000351 | prose | pages [9] -->
Fading Period: the popularity is time-sensitive as the novelty of the game has passed for players. And, players' desire to share their achievements decreases, but it does not mean that the number of players decreases at this time. Nevertheless, the overall fluctuation of popularity is lower compared to the burst period. iii.

<!-- b000352 | prose | pages [9] -->
Dormant Period: the popularity leveled off, there were still many loyal players to the game, and the conversation remained. In general, the ups and downs do not change much. In this paper, we observe that the random fluctuations in the number of reports do not exactly obey the Poisson distribution when the game is popular, and the fluctuations are sig- nificantly larger. As the game's popularity waned, so did the fluctuations. Therefore, we intro- duce a popularity relaxation function to modify the random process model.

<!-- b000353 | prose | pages [9] -->
As mentioned in Section 5.1, the boundary of the popularity relaxation phenomenon can be approximately reduced to a linear boundary, so we define the popularity relaxation function , with  being the number of reports and as being constants. The modified random process arrives at the intensity function as:

<!-- b000354 | furniture | pages [9] -->


<!-- b000355 | prose | pages [9] -->
(4)

<!-- b000356 | furniture | pages [9] -->


<!-- b000357 | furniture | pages [10] -->
Team # 2311717

<!-- b000358 | furniture | pages [10] -->


<!-- b000359 | furniture | pages [10] -->


<!-- b000360 | furniture | pages [10] -->


<!-- b000361 | furniture | pages [10] -->


<!-- b000362 | furniture | pages [10] -->


<!-- b000363 | furniture | pages [10] -->


<!-- b000364 | furniture | pages [10] -->


<!-- b000365 | furniture | pages [10] -->


<!-- b000366 | furniture | pages [10] -->


<!-- b000367 | furniture | pages [10] -->


<!-- b000368 | furniture | pages [10] -->


<!-- b000369 | furniture | pages [10] -->


<!-- b000370 | furniture | pages [10] -->


<!-- b000371 | furniture | pages [10] -->
Page 10 of 25

<!-- b000372 | prose | pages [10] -->
Therefore, the probability that the number of reports is  on the day  after the correction of equation (3) is:

<!-- b000373 | prose | pages [10] -->
We can calculate the prediction interval

<!-- b000374 | prose | pages [10] -->
on the day  with a certain confidence level

<!-- b000375 | prose | pages [10] -->
(5)

<!-- b000376 | furniture | pages [10] -->


<!-- b000377 | prose | pages [10] -->
for the number of reports

<!-- b000378 | prose | pages [10] -->
based on , as shown in equation (6).

<!-- b000379 | furniture | pages [10] -->


<!-- b000380 | prose | pages [10] -->
(6)

<!-- b000381 | heading | pages [10] -->
5.2.2 Establishing prediction intervals for future reported number results

<!-- b000382 | prose | pages [10] -->
Based on a trend forecasting model with Gaussian regression, we predict the long-term trend in the number of reports. The regression results in . This indicates that the regression results are more explanatory of the trend in the number of reports, and the root mean square error is about 2 orders of magnitude smaller than the number of reports. The regression coefficients are shown in Table 2, and we will show the specific trend prediction effects together with the prediction intervals.

<!-- b000383 | caption | pages [10] -->
Table 2: Regression coefficient of the trend prediction model

<!-- b000384 | furniture | pages [10] -->


<!-- b000385 | furniture | pages [10] -->


<!-- b000386 | prose | pages [10] -->
1.57e+05

<!-- b000387 | furniture | pages [10] -->


<!-- b000388 | furniture | pages [10] -->


<!-- b000389 | prose | pages [10] -->
9.69e+04

<!-- b000390 | furniture | pages [10] -->


<!-- b000391 | furniture | pages [10] -->


<!-- b000392 | prose | pages [10] -->
4.846e+04

<!-- b000393 | furniture | pages [10] -->


<!-- b000394 | furniture | pages [10] -->


<!-- b000395 | furniture | pages [10] -->


<!-- b000396 | prose | pages [10] -->
33.01 30.79

<!-- b000397 | furniture | pages [10] -->


<!-- b000398 | prose | pages [10] -->
48.2 75.31

<!-- b000399 | furniture | pages [10] -->


<!-- b000400 | prose | pages [10] -->
5.864 386.7

<!-- b000401 | prose | pages [10] -->
Then, by modifying the report number prediction model of the non-homogeneous Poisson process, the report number prediction interval of 75% confidence is obtained. Figure 5 shows the model's present description of the reported number results with future predictions, and the horizontal coordinates are the number of days to January 7, 2022.

<!-- b000402 | prose | pages [10] -->
Data of 2023-03-01

<!-- b000403 | prose | pages [10] -->
[7654, 20154]

<!-- b000404 | prose | pages [10] -->
(419)   13904

<!-- b000405 | furniture | pages [10] -->


<!-- b000406 | prose | pages [10] -->
Date

<!-- b000407 | caption | pages [10] -->
Figure 5: Report number trends and 75% confidence level intervals predicting

<!-- b000408 | furniture | pages [10] -->


<!-- b000409 | furniture | pages [11] -->
Team # 2311717

<!-- b000410 | furniture | pages [11] -->


<!-- b000411 | furniture | pages [11] -->


<!-- b000412 | furniture | pages [11] -->


<!-- b000413 | furniture | pages [11] -->


<!-- b000414 | furniture | pages [11] -->


<!-- b000415 | furniture | pages [11] -->


<!-- b000416 | furniture | pages [11] -->


<!-- b000417 | furniture | pages [11] -->


<!-- b000418 | furniture | pages [11] -->


<!-- b000419 | furniture | pages [11] -->


<!-- b000420 | furniture | pages [11] -->


<!-- b000421 | furniture | pages [11] -->


<!-- b000422 | furniture | pages [11] -->


<!-- b000423 | furniture | pages [11] -->
Page 11 of 25

<!-- b000424 | prose | pages [11] -->
From the figure above, we can find that our model can predict the long-term trend of the number of reports more accurately, and can also roughly estimate the random fluctuation inter- val of the number of reports per day. It is worth noting that the prediction interval is a good reflection of the timeliness of the heat, and the number of users shows a surge and significant fluctuation when the "Date" is about 40, as the number of users is in the "Explosion Period". When the "Date" is about 220, the number of users is in the "Dormant Period", and the number and fluctuation are relatively small and tend to be stable.

<!-- b000425 | prose | pages [11] -->
We predict that the number of reported results converges to 13,904 on March 1, 2023 (when the value of the horizontal coordinate is 419 in Figure 5). The results of the prediction intervals at different confidence levels are shown in Table 3.

<!-- b000426 | caption | pages [11] -->
Table 3: Prediction interval for the number of reports (on March 1st)

<!-- b000427 | prose | pages [11] -->
Confidence

<!-- b000428 | prose | pages [11] -->
Left border of the

<!-- b000429 | prose | pages [11] -->
level

<!-- b000430 | prose | pages [11] -->
Right border of the

<!-- b000431 | prose | pages [11] -->
prediction interval

<!-- b000432 | prose | pages [11] -->
75% 7654

<!-- b000433 | prose | pages [11] -->
85% 5434

<!-- b000434 | prose | pages [11] -->
prediction interval

<!-- b000435 | prose | pages [11] -->
20154

<!-- b000436 | prose | pages [11] -->
23657

<!-- b000437 | prose | pages [11] -->
In general, the overall change pattern of the number of reports is determined by the social attributes and social laws of the game. And this changing pattern shows a clear trend, so a better prediction effect can be obtained through the regression model.

<!-- b000438 | prose | pages [11] -->
Based on the overall change trend, the number of reports also has a certain degree of random fluctuation. This stochastic fluctuation has the statistical characteristic of changing with time and heat. Therefore, the stochastic process can be applied to describe it.

<!-- b000439 | heading | pages [11] -->
5.3 Analysis of Game Mode Selection

<!-- b000440 | heading | pages [11] -->
5.3.1 Analysis of word attributes

<!-- b000441 | prose | pages [11] -->
First, we analyze the possible word attributes involved, which can be mined from the ex- isting dataset in 3 main aspects: letter frequency, letter position and common word roots, etc.

<!-- b000442 | furniture | pages [11] -->


<!-- b000443 | caption | pages [11] -->
Figure 6: Analysis of word attributes

<!-- b000444 | prose | pages [11] -->
◼ Number of different letters: It is expressed as the number of different letters in a word.

<!-- b000445 | prose | pages [11] -->
Statistically, the range of values is 3 to 5. For example, the value of this attribute for the word "happy" is 4. This attribute reflects the internal variability of the word.

<!-- b000446 | furniture | pages [11] -->


<!-- b000447 | furniture | pages [12] -->
Team # 2311717

<!-- b000448 | furniture | pages [12] -->


<!-- b000449 | furniture | pages [12] -->


<!-- b000450 | furniture | pages [12] -->


<!-- b000451 | furniture | pages [12] -->


<!-- b000452 | furniture | pages [12] -->


<!-- b000453 | furniture | pages [12] -->


<!-- b000454 | furniture | pages [12] -->


<!-- b000455 | furniture | pages [12] -->


<!-- b000456 | furniture | pages [12] -->


<!-- b000457 | furniture | pages [12] -->


<!-- b000458 | furniture | pages [12] -->


<!-- b000459 | furniture | pages [12] -->


<!-- b000460 | furniture | pages [12] -->


<!-- b000461 | furniture | pages [12] -->
Page 12 of 25

<!-- b000462 | prose | pages [12] -->
◼ Total possible number of letters: It represents the sum of the frequencies of all letters in

<!-- b000463 | prose | pages [12] -->
a word. Assuming that the frequency of the letter " " in the 359-word result data is , the value of this attribute for the word "happy" is . This attribute is an indication of the overall usage tendency of the word. ◼ Frequency of first letter: It indicates the frequency of the first letter of a word. For ex-

<!-- b000464 | prose | pages [12] -->
ample, in 359 data items, the total number of the first letter of each word is 359, and the percentage of words with the first letter "h" is , then the value of this attribute for the . This attribute reflects the local position tendency of the word. word "happy" is ◼ Frequency of second letter: It indicates the frequency of the second letter of a word. For

<!-- b000465 | prose | pages [12] -->
example, in 359 data items, the total number of the second letter of each word is 359, and

<!-- b000466 | prose | pages [12] -->
the percentage of words with the second letter "a" is . The value of this attribute for the . This attribute reflects the local position tendency of the word. word "happy" is ◼ Frequency of third letter: It indicates the frequency of the third letter of a word. For ex-

<!-- b000467 | prose | pages [12] -->
ample, in 359 data items, the total number of the third letter of each word is 359, and the , then the value of this attribute for the percentage of words with the third letter "p" is . This attribute reflects the local position tendency of the word. word "happy" is ◼ Frequency of forth letter: It indicates the frequency of the fourth letter of a word. For

<!-- b000468 | prose | pages [12] -->
example, in 359 data items, the total number of the fourth letter of each word is 359, and the percentage of words with the fourth letter "p" is . The value of this attribute for the . This attribute reflects the local position tendency of the word. word "happy" is

<!-- b000469 | prose | pages [12] -->
◼ Frequency of fifth letter: It indicates the frequency of the fifth letter of a word. For ex-

<!-- b000470 | prose | pages [12] -->
ample, in 359 data items, the total number of the fifth letter of each word is also 359, and the percentage of words with the fifth letter "y" is , then the value of this attribute for . This attribute reflects the local position tendency of the word. the word "happy" is ◼ Whether a common root: It indicates whether a word has common roots within it. For

<!-- b000471 | prose | pages [12] -->
example, if the word "manly" contains the root "-ly", then the word has a value of 1; oth- erwise, it has a value of 0. This property reflects the local regularity of the word.

<!-- b000472 | heading | pages [12] -->
5.3.2 Analysis of the influence of word attributes on pattern selection

<!-- b000473 | prose | pages [12] -->
We wanted to find out whether the 8 attributes of the word listed in the previous section affected the user's choice of game mode. So, for each attribute, a scatter plot comparing the

<!-- b000474 | prose | pages [12] -->
relationship between daily word attributes and Hard Mode choices was plotted in Figure 7.

<!-- b000475 | prose | pages [12] -->
In the figure below, the horizontal coordinates of each scatter plot are the percentage of Hard Mode choices (in %). It can be noticed that the individual attributes do not have a strong correlation with the percentage of Hard Mode. The presented word attributes do not affect the proportion of reported data for the Hard Mode. We believe that the reason for this phenomenon is that players are not informed about the solution word in advance. That is, the word attributes are unknown before most players choose the game mode, so the player's choice is not highly correlated with it.

<!-- b000476 | furniture | pages [12] -->


<!-- b000477 | furniture | pages [13] -->
Team # 2311717

<!-- b000478 | furniture | pages [13] -->


<!-- b000479 | furniture | pages [13] -->


<!-- b000480 | furniture | pages [13] -->


<!-- b000481 | furniture | pages [13] -->


<!-- b000482 | furniture | pages [13] -->


<!-- b000483 | furniture | pages [13] -->


<!-- b000484 | prose | pages [13] -->
5

<!-- b000485 | prose | pages [13] -->
200

<!-- b000486 | prose | pages [13] -->
4.5

<!-- b000487 | prose | pages [13] -->
150

<!-- b000488 | prose | pages [13] -->
attribute

<!-- b000489 | prose | pages [13] -->
attribute

<!-- b000490 | prose | pages [13] -->
4

<!-- b000491 | prose | pages [13] -->
100

<!-- b000492 | prose | pages [13] -->
3.5

<!-- b000493 | prose | pages [13] -->
50

<!-- b000494 | prose | pages [13] -->
3

<!-- b000495 | prose | pages [13] -->
0

<!-- b000496 | prose | pages [13] -->
0 5 10 15

<!-- b000497 | prose | pages [13] -->
0

<!-- b000498 | prose | pages [13] -->
(a)Number of different letters

<!-- b000499 | furniture | pages [13] -->


<!-- b000500 | furniture | pages [13] -->


<!-- b000501 | furniture | pages [13] -->


<!-- b000502 | furniture | pages [13] -->


<!-- b000503 | furniture | pages [13] -->


<!-- b000504 | furniture | pages [13] -->


<!-- b000505 | furniture | pages [13] -->


<!-- b000506 | furniture | pages [13] -->
Page 13 of 25

<!-- b000507 | prose | pages [13] -->
0.15

<!-- b000508 | prose | pages [13] -->
0.1

<!-- b000509 | prose | pages [13] -->
attribute

<!-- b000510 | prose | pages [13] -->
0.05

<!-- b000511 | prose | pages [13] -->
0

<!-- b000512 | prose | pages [13] -->
5 5 10 15

<!-- b000513 | prose | pages [13] -->
0 5 10 15

<!-- b000514 | prose | pages [13] -->
(b)Total possible number of letters

<!-- b000515 | prose | pages [13] -->
0.15

<!-- b000516 | prose | pages [13] -->
0.15

<!-- b000517 | prose | pages [13] -->
0.1

<!-- b000518 | prose | pages [13] -->
0.1

<!-- b000519 | prose | pages [13] -->
attribute

<!-- b000520 | prose | pages [13] -->
attribute

<!-- b000521 | prose | pages [13] -->
0.05

<!-- b000522 | prose | pages [13] -->
0.05

<!-- b000523 | prose | pages [13] -->
0

<!-- b000524 | prose | pages [13] -->
0

<!-- b000525 | prose | pages [13] -->
0 5 10 15

<!-- b000526 | prose | pages [13] -->
0

<!-- b000527 | prose | pages [13] -->
(d)Frequency of second letter

<!-- b000528 | prose | pages [13] -->
(c)Frequency of first letter

<!-- b000529 | prose | pages [13] -->
0.1

<!-- b000530 | prose | pages [13] -->
attribute

<!-- b000531 | prose | pages [13] -->
0.05

<!-- b000532 | prose | pages [13] -->
0

<!-- b000533 | prose | pages [13] -->
5 5 10 15

<!-- b000534 | prose | pages [13] -->
0 5 10 15

<!-- b000535 | prose | pages [13] -->
(e)Frequency of third letter

<!-- b000536 | prose | pages [13] -->
1

<!-- b000537 | prose | pages [13] -->
0.2

<!-- b000538 | prose | pages [13] -->
0.15

<!-- b000539 | prose | pages [13] -->
attribute

<!-- b000540 | prose | pages [13] -->
attribute

<!-- b000541 | prose | pages [13] -->
0.5

<!-- b000542 | prose | pages [13] -->
0.1

<!-- b000543 | prose | pages [13] -->
0.05

<!-- b000544 | prose | pages [13] -->
0

<!-- b000545 | prose | pages [13] -->
0

<!-- b000546 | prose | pages [13] -->
0 5 10 15

<!-- b000547 | prose | pages [13] -->
0

<!-- b000548 | prose | pages [13] -->
(g)Frequency of fifth letter

<!-- b000549 | prose | pages [13] -->
(f)Frequency of forth letter

<!-- b000550 | prose | pages [13] -->
5 5 10 15

<!-- b000551 | furniture | pages [13] -->


<!-- b000552 | prose | pages [13] -->
(h)Whether a common root

<!-- b000553 | caption | pages [13] -->
Figure 7: Correlation between the proportion of Hard Mode choices and word attrib-

<!-- b000554 | prose | pages [13] -->
utes So what are the main factors associated with the Hard Mode selection ratio?

<!-- b000555 | caption | pages [13] -->
Table 4 provides a further visualization of the word content and date of some of the Hard

<!-- b000556 | prose | pages [13] -->
Mode percentages. We can find that there are no obvious word attribute characteristics in the top ten reports and the bottom ten reports in the proportion ranking. However, the data with a high percentage of Hard Mode choices tend to appear in the last three months of 2022, while the data with a low proportion tend to appear in the first month of 2022 with a high correlation with time.

<!-- b000557 | caption | pages [13] -->
Table 4: The percentage of scores reported in Hard Mode

<!-- b000558 | prose | pages [13] -->
Top 10

<!-- b000559 | prose | pages [13] -->
Date Word Percentage

<!-- b000560 | prose | pages [13] -->
2022/11/1 piney 13.33% 2022/9/16 parer 11.07% 2022/11/30 study 10.66% 2022/10/23 mummy 10.32% 2022/10/15 catch 10.27% 2022/12/26 judge 10.21% 2022/10/30 waltz 10.12% 2022/10/12 ionic 10.11% 2022/10/29 libel 10.08% 2022/12/25 extra 10.04%

<!-- b000561 | prose | pages [13] -->
Bottom 10

<!-- b000562 | prose | pages [13] -->
Date Word Percentage

<!-- b000563 | prose | pages [13] -->
2022/1/16 solar 2.36% 2022/1/14 tangy 2.35% 2022/1/15 panic 2.26% 2022/1/12 favor 2.23% 2022/1/10 query 2.09% 2022/1/9 gorge 2.09% 2022/1/11 drink 1.96% 2022/1/8 crank 1.74% 2022/1/7 slump 1.69% 2022/2/13 robin 1.17% To further explore this pattern, we visualized the change of the percentage of Hard Mode choice over time, as shown in Figure 8(a), the color of the heat map fades from blue to green as time increases, and there are only few dates with outlier fluctuations, i.e., the percentage of

<!-- b000564 | furniture | pages [13] -->


<!-- b000565 | prose | pages [14] -->
校苑

<!-- b000566 | furniture | pages [14] -->
Team # 2311717

<!-- b000567 | furniture | pages [14] -->


<!-- b000568 | furniture | pages [14] -->


<!-- b000569 | furniture | pages [14] -->


<!-- b000570 | furniture | pages [14] -->


<!-- b000571 | furniture | pages [14] -->


<!-- b000572 | furniture | pages [14] -->


<!-- b000573 | prose | pages [14] -->
校苑数

<!-- b000574 | furniture | pages [14] -->
校苑数模

<!-- b000575 | furniture | pages [14] -->


<!-- b000576 | furniture | pages [14] -->


<!-- b000577 | furniture | pages [14] -->


<!-- b000578 | furniture | pages [14] -->


<!-- b000579 | furniture | pages [14] -->


<!-- b000580 | furniture | pages [14] -->


<!-- b000581 | furniture | pages [14] -->


<!-- b000582 | furniture | pages [14] -->
Page 14 of 25

<!-- b000583 | prose | pages [14] -->
Hard Mode choice shows an increasing trend, which can also be seen in the scatter plot of

<!-- b000584 | prose | pages [14] -->
校苑数模

<!-- b000585 | prose | pages [14] -->
Figure 8(b). There is a very clear trend that the percentage of Hard Mode selection increases with time, not only incrementally, but also the growth rate is gradually slowing down.

<!-- b000586 | prose | pages [14] -->
14

<!-- b000587 | heading | pages [14] -->
Percentage of Hard Mode Results

<!-- b000588 | prose | pages [14] -->
12

<!-- b000589 | prose | pages [14] -->
50

<!-- b000590 | prose | pages [14] -->
12

<!-- b000591 | prose | pages [14] -->
10

<!-- b000592 | prose | pages [14] -->
10

<!-- b000593 | prose | pages [14] -->
100

<!-- b000594 | prose | pages [14] -->
校苑

<!-- b000595 | prose | pages [14] -->
校苑数模

<!-- b000596 | prose | pages [14] -->
8

<!-- b000597 | prose | pages [14] -->
150

<!-- b000598 | prose | pages [14] -->
8

<!-- b000599 | prose | pages [14] -->
Date

<!-- b000600 | prose | pages [14] -->
6

<!-- b000601 | prose | pages [14] -->
200

<!-- b000602 | prose | pages [14] -->
6

<!-- b000603 | prose | pages [14] -->
4

<!-- b000604 | prose | pages [14] -->
250

<!-- b000605 | prose | pages [14] -->
2

<!-- b000606 | prose | pages [14] -->
4

<!-- b000607 | prose | pages [14] -->
300

<!-- b000608 | prose | pages [14] -->
校苑数模

<!-- b000609 | prose | pages [14] -->
0

<!-- b000610 | prose | pages [14] -->
2

<!-- b000611 | prose | pages [14] -->
0

<!-- b000612 | prose | pages [14] -->
350

<!-- b000613 | prose | pages [14] -->
50 100 150 200 250 300 350 400

<!-- b000614 | furniture | pages [14] -->


<!-- b000615 | prose | pages [14] -->
Date

<!-- b000616 | prose | pages [14] -->
(a) Heat map over time         (b) Trends over time

<!-- b000617 | prose | pages [14] -->
校

<!-- b000618 | caption | pages [14] -->
Figure 8: Description of the Hard Mode selection percentage

<!-- b000619 | prose | pages [14] -->
We believe that, on the one hand, this is because as the time spent playing the game in- creases, the user's ability to perform in the game is also sufficiently improved, so some users

<!-- b000620 | prose | pages [14] -->
校苑数模

<!-- b000621 | prose | pages [14] -->
who love challenges will gradually tend to choose a higher difficulty mode. On the other hand, many users may play with a more casual mindset and do not consider increasing the difficulty of the game even though their ability has increased. In other words, players' confidence level in their performance ability and their playing mentality may be the main reason for whether they choose the Hard Mode, rather than the attributes of the words.

<!-- b000622 | prose | pages [14] -->
校苑数模

<!-- b000623 | heading | pages [14] -->
6 Task 2: A Prediction Model for The Distribution of The Re-

<!-- b000624 | prose | pages [14] -->
模

<!-- b000625 | heading | pages [14] -->
ported Results

<!-- b000626 | prose | pages [14] -->
To predict the distribution of future report results, we first extracted and constructed the

<!-- b000627 | prose | pages [14] -->
校苑数模

<!-- b000628 | prose | pages [14] -->
data features. Then, we build a BP neural network model to take 7 data features as input and

<!-- b000629 | prose | pages [14] -->
苑数模

<!-- b000630 | prose | pages [14] -->
output the distribution of 7 guessed word results. Finally, the Bagging algorithm was adopted to integrate multiple BP neural networks to derive the final prediction results through a hard voting mechanism to reduce the generalization error of the prediction results.

<!-- b000631 | heading | pages [14] -->
6.1 Building the BP Neural Network-based Prediction Model for the distri-

<!-- b000632 | heading | pages [14] -->
bution of word-guessing results

<!-- b000633 | furniture | pages [14] -->
校苑数模

<!-- b000634 | prose | pages [14] -->
Considering that the result distribution of the number of word guesses shared on Twitter is likely to be different from that of the entire player population, and is related to many factors that are difficult to quantify and count, including the players' mindset and the familiarity of most players with the word of the day. Therefore, mechanistic modeling of the word-guessing outcome distribution may be difficult and unrealistic, and we decided to model the data for this

<!-- b000635 | prose | pages [14] -->
苑数模

<!-- b000636 | prose | pages [14] -->
problem. Of course, the approach implicitly assumes the condition that the historical data is a good representation of all possible questions and player answers for wordle, which is the big- gest uncertainty of our model.

<!-- b000637 | furniture | pages [14] -->


<!-- b000638 | prose | pages [14] -->
模

<!-- b000639 | furniture | pages [15] -->
Team # 2311717

<!-- b000640 | furniture | pages [15] -->


<!-- b000641 | furniture | pages [15] -->


<!-- b000642 | furniture | pages [15] -->


<!-- b000643 | furniture | pages [15] -->


<!-- b000644 | furniture | pages [15] -->


<!-- b000645 | furniture | pages [15] -->


<!-- b000646 | furniture | pages [15] -->


<!-- b000647 | furniture | pages [15] -->


<!-- b000648 | furniture | pages [15] -->


<!-- b000649 | furniture | pages [15] -->


<!-- b000650 | furniture | pages [15] -->


<!-- b000651 | furniture | pages [15] -->


<!-- b000652 | furniture | pages [15] -->


<!-- b000653 | furniture | pages [15] -->
Page 15 of 25

<!-- b000654 | prose | pages [15] -->
Given the solution word and the corresponding date, we have access to the properties of the words and all the information that can be predicted based on the time course. The total number of historical data is 359, which is likely to cause underfitting problems for deep learn- ing algorithms, while the size of the data is acceptable for BP neural networks. Therefore, we decided to build a prediction model for the distribution of reports based on BP neural networks.

<!-- b000655 | heading | pages [15] -->
6.1.1 Extraction and construction of data features

<!-- b000656 | prose | pages [15] -->
Before building the neural network specifically, we first extract and construct the data features. As mentioned earlier, we want to predict the distribution of word-guessing results based on the solution words and the corresponding date. The sources of data features at this point include the words themselves and the predictable time course.

<!-- b000657 | prose | pages [15] -->
The information that can be obtained from the words themselves has been explored in Section 5.3.1, i.e., word attributes. We classified word attributes into 3 categories, including letter frequency, letter position, and common root words. Among them, our statistics for the attribute of whether it contains common word roots resulted in unbalanced data. As a Bool- ean value, only about 20 out of 359 data for this attribute had a true value. Therefore, this attribute is of no value for the training of the neural network, and we do not keep this feature. In addition, the feature Total possible number of letters, which has some repetitiveness, is also removed to compress the data dimension.

<!-- b000658 | prose | pages [15] -->
Finally, we also selected the percentage of people who chose the Hard Mode as a fea- ture because the difficult choice of the game also affected the distribution of the number of guesses. As analyzed in Section 5.3.2, this feature has a clear trend and small fluctuations over time, so the feature is predictable for a determined future date. The value of this characteristic in the second half of 2022 mostly fluctuates around 9.5% and the variation is not significant anymore. So we make some simplifications and assume that it will remain this way for some time to come, without making more precise predictions. We take the average value of the dif- ficult mode selection ratio for the latter 59 days as the forecast value.

<!-- b000659 | heading | pages [15] -->
6.1.2 Construction of BP neural network

<!-- b000660 | prose | pages [15] -->
For the report result distribution prediction problem, 7 data features such as Number of different letters constitute the input space, while 7 reported result distributions constitute the output space. The mathematical essence of the problem is to fit a mapping from a 7-dimensional input space to a 7-dimensional output space. A review of the literature [6] shows that for fitting such finite-dimensional space mappings, building neural networks usually requires only one hidden layer. Therefore, the BP neural network in this model has a total of three layers, which are the input layer, the hidden layer, and the output layer.

<!-- b000661 | prose | pages [15] -->
Since the input space and output space are both 7-dimensional, the number of neurons in and the number of neurons in the output layer the input layer are both 7. Referring to the empirical formula proposed in the literature [7], we set the number of hidden layer neurons

<!-- b000662 | prose | pages [15] -->
that satisfy equation (7).

<!-- b000663 | prose | pages [15] -->
where is the size of the training set and

<!-- b000664 | furniture | pages [15] -->


<!-- b000665 | prose | pages [15] -->
(7)

<!-- b000666 | prose | pages [15] -->
is a constant.

<!-- b000667 | prose | pages [15] -->
At this point, we have completed the construction of the BP neural network, the structure

<!-- b000668 | furniture | pages [15] -->


<!-- b000669 | prose | pages [16] -->
校苑

<!-- b000670 | furniture | pages [16] -->
Team # 2311717

<!-- b000671 | furniture | pages [16] -->


<!-- b000672 | furniture | pages [16] -->


<!-- b000673 | furniture | pages [16] -->


<!-- b000674 | furniture | pages [16] -->


<!-- b000675 | furniture | pages [16] -->


<!-- b000676 | furniture | pages [16] -->


<!-- b000677 | prose | pages [16] -->
of which is shown in Figure 9.

<!-- b000678 | prose | pages [16] -->
校苑数模

<!-- b000679 | prose | pages [16] -->
Input

<!-- b000680 | prose | pages [16] -->
校苑数

<!-- b000681 | furniture | pages [16] -->
校苑数模

<!-- b000682 | furniture | pages [16] -->


<!-- b000683 | furniture | pages [16] -->


<!-- b000684 | furniture | pages [16] -->


<!-- b000685 | furniture | pages [16] -->


<!-- b000686 | furniture | pages [16] -->


<!-- b000687 | furniture | pages [16] -->


<!-- b000688 | furniture | pages [16] -->


<!-- b000689 | furniture | pages [16] -->
Page 16 of 25

<!-- b000690 | prose | pages [16] -->
Hidden

<!-- b000691 | prose | pages [16] -->
Layer

<!-- b000692 | prose | pages [16] -->
1

<!-- b000693 | prose | pages [16] -->
2

<!-- b000694 | prose | pages [16] -->
Output

<!-- b000695 | prose | pages [16] -->
Layer

<!-- b000696 | prose | pages [16] -->
Layer

<!-- b000697 | prose | pages [16] -->
1 1

<!-- b000698 | prose | pages [16] -->
1

<!-- b000699 | prose | pages [16] -->
2 2

<!-- b000700 | prose | pages [16] -->
2

<!-- b000701 | prose | pages [16] -->
校苑

<!-- b000702 | prose | pages [16] -->
3 3

<!-- b000703 | prose | pages [16] -->
校苑数模

<!-- b000704 | prose | pages [16] -->
7

<!-- b000705 | prose | pages [16] -->
7

<!-- b000706 | prose | pages [16] -->
8 8

<!-- b000707 | prose | pages [16] -->
9 9

<!-- b000708 | furniture | pages [16] -->


<!-- b000709 | caption | pages [16] -->
Figure 9: Structure of BP neural network

<!-- b000710 | heading | pages [16] -->
6.1.3 Bagging-based prediction model with integrated BP neural network

<!-- b000711 | prose | pages [16] -->
校苑数模

<!-- b000712 | prose | pages [16] -->
In the training of the BP neural network, we randomly selected the training set according to 85%. After several tests, we found that the neural network obtained from each training al-

<!-- b000713 | prose | pages [16] -->
校

<!-- b000714 | prose | pages [16] -->
ways has unacceptable errors at very few samples in the test set. Moreover, the repetition rate of samples with large prediction errors was not high for different neural networks. Therefore, we decided to adopt the Bagging algorithm to integrate multiple BP neural networks. Then, the

<!-- b000715 | prose | pages [16] -->
校苑数模

<!-- b000716 | prose | pages [16] -->
final results are derived through a hard voting mechanism, which has the effect of reducing the generalization error of the prediction results.

<!-- b000717 | prose | pages [16] -->
In the integration algorithm, we obtain different sub-training sets by randomly sam- times, and each time the percentage of sampling is also 85%. pling 85% of the overall data neural networks are obtained based on these sub-training sets trained with the same Then,

<!-- b000718 | prose | pages [16] -->
校苑数模

<!-- b000719 | prose | pages [16] -->
parameters. Next, these neural networks are used to predict the distribution of word guesses. All neural networks output their respective predictions directly and the final prediction is ob-

<!-- b000720 | prose | pages [16] -->
模

<!-- b000721 | prose | pages [16] -->
tained by a minority-majority voting mechanism [8]. The flow of this integrated algorithm is shown in Figure 10.

<!-- b000722 | prose | pages [16] -->
Training Set

<!-- b000723 | prose | pages [16] -->
Subtraining

<!-- b000724 | prose | pages [16] -->
Training

<!-- b000725 | prose | pages [16] -->
Set 1

<!-- b000726 | prose | pages [16] -->
苑数模

<!-- b000727 | prose | pages [16] -->
Subtraining

<!-- b000728 | prose | pages [16] -->
Training

<!-- b000729 | prose | pages [16] -->
Set 2

<!-- b000730 | prose | pages [16] -->
Input

<!-- b000731 | prose | pages [16] -->
Output

<!-- b000732 | prose | pages [16] -->
Space

<!-- b000733 | prose | pages [16] -->
Space

<!-- b000734 | prose | pages [16] -->
Subtraining

<!-- b000735 | prose | pages [16] -->
Training

<!-- b000736 | prose | pages [16] -->
Set

<!-- b000737 | furniture | pages [16] -->
校苑数模

<!-- b000738 | prose | pages [16] -->
Test  Set

<!-- b000739 | prose | pages [16] -->
校苑数模

<!-- b000740 | prose | pages [16] -->
Network 1

<!-- b000741 | prose | pages [16] -->
Predict

<!-- b000742 | prose | pages [16] -->
Output

<!-- b000743 | prose | pages [16] -->
Network 2

<!-- b000744 | prose | pages [16] -->
Predict

<!-- b000745 | prose | pages [16] -->
Synthesize

<!-- b000746 | prose | pages [16] -->
Network

<!-- b000747 | prose | pages [16] -->
Predict

<!-- b000748 | furniture | pages [16] -->


<!-- b000749 | caption | pages [16] -->
Figure 10: Schematic diagram of integrated BP neural network

<!-- b000750 | prose | pages [16] -->
To avoid the influence of accidental errors on voting results, is used for training.

<!-- b000751 | heading | pages [16] -->
6.2 Analysis of Uncertainties Affecting the Model

<!-- b000752 | prose | pages [16] -->
苑数模

<!-- b000753 | prose | pages [16] -->
The dataset we have and the selected data features are perhaps not well representative of Wordle's questioning and players' answering, which would lead to poor generalization of our model.

<!-- b000754 | furniture | pages [16] -->


<!-- b000755 | prose | pages [16] -->
模

<!-- b000756 | prose | pages [17] -->
校苑

<!-- b000757 | furniture | pages [17] -->
Team # 2311717

<!-- b000758 | furniture | pages [17] -->


<!-- b000759 | furniture | pages [17] -->


<!-- b000760 | furniture | pages [17] -->


<!-- b000761 | furniture | pages [17] -->


<!-- b000762 | furniture | pages [17] -->


<!-- b000763 | furniture | pages [17] -->


<!-- b000764 | prose | pages [17] -->
校苑数

<!-- b000765 | furniture | pages [17] -->
校苑数模

<!-- b000766 | furniture | pages [17] -->


<!-- b000767 | furniture | pages [17] -->


<!-- b000768 | furniture | pages [17] -->


<!-- b000769 | furniture | pages [17] -->


<!-- b000770 | furniture | pages [17] -->


<!-- b000771 | furniture | pages [17] -->


<!-- b000772 | furniture | pages [17] -->


<!-- b000773 | furniture | pages [17] -->
Page 17 of 25

<!-- b000774 | prose | pages [17] -->
In addition, the size of the dataset used for training, although acceptable, is still relatively

<!-- b000775 | prose | pages [17] -->
校苑数模

<!-- b000776 | prose | pages [17] -->
limited. In the process of randomly selecting sub-training sets by the integration algorithm, the proportion of identical samples among the sub-training sets may be quite high. This can make the homogeneity between individual neural networks too high to function as an integration and voting mechanism.

<!-- b000777 | prose | pages [17] -->
校苑

<!-- b000778 | heading | pages [17] -->
6.3 Analysis of the Results of the Prediction Model

<!-- b000779 | prose | pages [17] -->
校苑数模

<!-- b000780 | prose | pages [17] -->
First, we arrange the data sets in descending order by time and select the top 85% of the data as the total training set. The remaining 15% of the data will be used as the test set to verify the model effect. Then, 85% of the total training set is randomly selected as the sub-training neural networks are trained. Finally, these set each time, and neural networks are inte- grated and the prediction effect is tested with the test set.

<!-- b000781 | prose | pages [17] -->
校苑数模

<!-- b000782 | prose | pages [17] -->
After several attempts, we found that we were able to achieve better prediction results . In the test set, the model’s when and the correlation co-

<!-- b000783 | prose | pages [17] -->
校

<!-- b000784 | prose | pages [17] -->
. As shown in Figure 11, the model has different prediction effects on efficient is the distribution of the seven guess word results. Among them, the prediction result of 3 tries has the largest error, but the mean square error still does not exceed 5%.

<!-- b000785 | prose | pages [17] -->
校苑数模

<!-- b000786 | prose | pages [17] -->
35

<!-- b000787 | prose | pages [17] -->
5

<!-- b000788 | prose | pages [17] -->
Predict

<!-- b000789 | prose | pages [17] -->
4.5

<!-- b000790 | prose | pages [17] -->
30

<!-- b000791 | prose | pages [17] -->
Observe Mean of error

<!-- b000792 | prose | pages [17] -->
Average Percentage

<!-- b000793 | prose | pages [17] -->
4

<!-- b000794 | prose | pages [17] -->
25

<!-- b000795 | prose | pages [17] -->
Mean of Error

<!-- b000796 | prose | pages [17] -->
3.5

<!-- b000797 | prose | pages [17] -->
20

<!-- b000798 | prose | pages [17] -->
3

<!-- b000799 | prose | pages [17] -->
15

<!-- b000800 | prose | pages [17] -->
2.5

<!-- b000801 | prose | pages [17] -->
10

<!-- b000802 | prose | pages [17] -->
2

<!-- b000803 | prose | pages [17] -->
5

<!-- b000804 | prose | pages [17] -->
1.5

<!-- b000805 | prose | pages [17] -->
0

<!-- b000806 | prose | pages [17] -->
1

<!-- b000807 | prose | pages [17] -->
1 2 3 4 5 6 7 Number of tries

<!-- b000808 | prose | pages [17] -->
模

<!-- b000809 | prose | pages [17] -->
150

<!-- b000810 | prose | pages [17] -->
100

<!-- b000811 | prose | pages [17] -->
Density

<!-- b000812 | prose | pages [17] -->
50

<!-- b000813 | prose | pages [17] -->
校苑数模

<!-- b000814 | prose | pages [17] -->
0

<!-- b000815 | prose | pages [17] -->
0 0.02 0.04 0.06 0.08 0.1 0.12 0.14 0.16 0.18 0.2

<!-- b000816 | furniture | pages [17] -->


<!-- b000817 | furniture | pages [17] -->


<!-- b000818 | prose | pages [17] -->
Absolute Error Range

<!-- b000819 | caption | pages [17] -->
Figure 11: Mean Comparison and Mean Squared Distribution         Figure 12: Absolute error distribution

<!-- b000820 | prose | pages [17] -->
The distribution of all errors was also counted. As shown in Figure 12. Although errors are inevitable, most of them are maintained within 6%. Among them, the absolute error within

<!-- b000821 | prose | pages [17] -->
校苑数模

<!-- b000822 | prose | pages [17] -->
2% accounts for about 38%, and the absolute error within 5% reaches more than 80%. There- fore, we have more than 80% confidence that the absolute error of the prediction result

<!-- b000823 | prose | pages [17] -->
苑数模

<!-- b000824 | prose | pages [17] -->
does not exceed 5%.

<!-- b000825 | prose | pages [17] -->
Finally, we predict the distribution of the number of guesses for the word ERRIE on March 1, 2023, as shown in Table 5.

<!-- b000826 | caption | pages [17] -->
Table 5: Prediction of the distribution of results for the word ERRIE

<!-- b000827 | heading | pages [17] -->
4 tries

<!-- b000828 | heading | pages [17] -->
1 try

<!-- b000829 | heading | pages [17] -->
2 tries

<!-- b000830 | heading | pages [17] -->
3 tries

<!-- b000831 | furniture | pages [17] -->
校苑数模

<!-- b000832 | heading | pages [17] -->
5 tries

<!-- b000833 | heading | pages [17] -->
6 tries

<!-- b000834 | prose | pages [17] -->
(X) 25% 0% 1% 6% 31% 25% 13%

<!-- b000835 | heading | pages [17] -->
7 Task 3: Word Difficulty Classification Model

<!-- b000836 | prose | pages [17] -->
To classify the solution words reasonably, we first classified the difficulty based on the K- Means clustering algorithm. Then, we explored the association between word attributes and

<!-- b000837 | prose | pages [17] -->
苑数模

<!-- b000838 | prose | pages [17] -->
difficulty classification based on Pearson correlation coefficients, and constructed a word dif- ficulty classification model. Finally, the new words can be classified according to this correla- tion.

<!-- b000839 | furniture | pages [17] -->


<!-- b000840 | prose | pages [17] -->
模

<!-- b000841 | furniture | pages [18] -->
Team # 2311717

<!-- b000842 | furniture | pages [18] -->


<!-- b000843 | furniture | pages [18] -->


<!-- b000844 | furniture | pages [18] -->


<!-- b000845 | furniture | pages [18] -->


<!-- b000846 | furniture | pages [18] -->


<!-- b000847 | furniture | pages [18] -->


<!-- b000848 | furniture | pages [18] -->


<!-- b000849 | furniture | pages [18] -->


<!-- b000850 | furniture | pages [18] -->


<!-- b000851 | furniture | pages [18] -->


<!-- b000852 | furniture | pages [18] -->


<!-- b000853 | furniture | pages [18] -->


<!-- b000854 | furniture | pages [18] -->


<!-- b000855 | furniture | pages [18] -->
Page 18 of 25

<!-- b000856 | heading | pages [18] -->
7.1 The Establishment of Word Difficulty Classification

<!-- b000857 | heading | pages [18] -->
7.1.1 Word difficulty induction model based on K-Means clustering

<!-- b000858 | prose | pages [18] -->
Before categorizing solution words by difficulty, we need to define the difficulty first. To make the model result more similar to the user's game experience, we decided to define a dif- ficulty division based on the user's guess count distribution. It should be noted that this is only an indication of difficulty, not the reason for determining the difficulty of solution words.

<!-- b000859 | prose | pages [18] -->
According to our definition of difficulty, the distribution of guesses reflects the difficulty of the word. Therefore, the first step to classifying vocabulary difficulty is to summarize the distribution of guessing times into certain categories. The essence of this problem is to explore the homogeneity and difference between the frequency distribution of historical guessing words. From a mathematical point of view, the homogeneity and difference of data can be described by distance, and the data can be grouped by distance. Therefore, we decided to use the K-Means algorithm to summarize the difficulty of the word.

<!-- b000860 | prose | pages [18] -->
First, a higher percentage of completed guesses indicates a higher difficulty of the puzzle. Therefore, the difference in difficulty in the distribution of the number of guesses is an absolute difference that can be described by the Euclidean distance. Then the difference between the is reflected in the Euclidean distance of the dis- and the guessing result guessing result tribution vector of the two, as shown in equation (8).

<!-- b000861 | furniture | pages [18] -->


<!-- b000862 | prose | pages [18] -->
(8)

<!-- b000863 | prose | pages [18] -->
Then, we need to determine how many levels of difficulty to classify, i.e., determine the number  of centers of mass for the K-Means clustering algorithm. We will find the best result

<!-- b000864 | prose | pages [18] -->
by multiple attempts. The goal is to make the difficulty classification without duplication or omission.

<!-- b000865 | prose | pages [18] -->
Next,  samples are randomly selected as initial clustering centers in the whole set of

<!-- b000866 | prose | pages [18] -->
, respectively, and noted as: samples

<!-- b000867 | furniture | pages [18] -->


<!-- b000868 | furniture | pages [18] -->


<!-- b000869 | prose | pages [18] -->
Since we have decided to use the Euclidean distance to measure the differences between samples, we take equation (9) as the optimization objective of the algorithm, i.e., to minimize the Euclidean distance of all samples to their cluster centers.

<!-- b000870 | prose | pages [18] -->
Where is the cluster to which sample

<!-- b000871 | furniture | pages [18] -->


<!-- b000872 | prose | pages [18] -->
(9)

<!-- b000873 | prose | pages [18] -->
belongs.

<!-- b000874 | prose | pages [18] -->
The distance between each sample point and each centroid is calculated iteratively. At the same time, the samples are allocated to the cluster with the smallest distance from the corre- sponding centroid:

<!-- b000875 | furniture | pages [18] -->


<!-- b000876 | prose | pages [18] -->
At the end of each iteration, the average distance of sample points in each cluster is cal- culated as the centroid of the next iteration:

<!-- b000877 | furniture | pages [18] -->


<!-- b000878 | furniture | pages [19] -->
Team # 2311717

<!-- b000879 | furniture | pages [19] -->


<!-- b000880 | furniture | pages [19] -->


<!-- b000881 | furniture | pages [19] -->


<!-- b000882 | furniture | pages [19] -->


<!-- b000883 | furniture | pages [19] -->


<!-- b000884 | furniture | pages [19] -->


<!-- b000885 | furniture | pages [19] -->


<!-- b000886 | furniture | pages [19] -->


<!-- b000887 | furniture | pages [19] -->


<!-- b000888 | furniture | pages [19] -->


<!-- b000889 | furniture | pages [19] -->


<!-- b000890 | furniture | pages [19] -->


<!-- b000891 | furniture | pages [19] -->


<!-- b000892 | furniture | pages [19] -->
Page 19 of 25

<!-- b000893 | furniture | pages [19] -->


<!-- b000894 | prose | pages [19] -->
At the same time, the objective function value of this iteration is compared with that of the previous iteration. The objective function has converged, and then the cluster- of ing ends. The final  is the difficulty level of each sample, and corresponds to the typical value of each difficulty level. In addition, the distance matrix its clustering center is also obtained.

<!-- b000895 | prose | pages [19] -->
between each sample and

<!-- b000896 | heading | pages [19] -->
7.1.2 Correlation analysis of word attributes and difficulty ratings based on Pearson co-

<!-- b000897 | prose | pages [19] -->
efficients

<!-- b000898 | prose | pages [19] -->
After obtaining the difficulty grading results, we used Pearson correlation coefficients to analyze the association between each attribute of the word and the difficulty grading. This is because it is more difficult to confirm the causal relationship between attributes and difficulty, but correlation can be used instead when classifying.

<!-- b000899 | prose | pages [19] -->
First, we selected the frequency of occurrence of letters in five positions, such as Fre- quency of first letter (F1), Frequency of second letter (F2) mentioned in Section 5.3.1, as the word attributes to be analyzed. Based on this, we further counted the number of word classes (WCN) and the number of vowels (VN) contained in each solution word in the dataset. So far, we have obtained 7 word attributes to be analyzed. Then, we select the samples closest to the respective clustering centers as typical samples from the sets of representative typical attribute vectors difficulty levels. The are obtained, where , denotes the  th sample, and , denotes the typical sample serial number of the th difficulty grading. For the th attribute of the th sample, we calculate the Euclidean distance between that attribute of the sample and the corresponding attribute of the  typical samples, respectively.

<!-- b000900 | furniture | pages [19] -->


<!-- b000901 | prose | pages [19] -->
, denoted as the attribute distance vector. And let We let

<!-- b000902 | prose | pages [19] -->
, denote the clustering distance vector.

<!-- b000903 | prose | pages [19] -->
Next, we calculated the Pearson correlation coefficients for the attribute distance vector , and obtained the correlation coefficients: and the cluster distance vector

<!-- b000904 | furniture | pages [19] -->


<!-- b000905 | prose | pages [19] -->
denote the variances of Where and , respectively.

<!-- b000906 | prose | pages [19] -->
Finally, we counted the mean value of the correlation coefficient for all samples. We also set the boundary for each attribute when considering that the th word attribute and the difficulty are correlated. Finally, we filtered the attributes to obtain a vector of attributes .

<!-- b000907 | heading | pages [19] -->
7.1.3 Word difficulty discrimination based on Euclidean distance

<!-- b000908 | prose | pages [19] -->
For the future solution word, we can judge its difficulty by calculating its similarity to

<!-- b000909 | furniture | pages [19] -->


<!-- b000910 | furniture | pages [20] -->
Team # 2311717

<!-- b000911 | furniture | pages [20] -->


<!-- b000912 | furniture | pages [20] -->


<!-- b000913 | furniture | pages [20] -->


<!-- b000914 | furniture | pages [20] -->


<!-- b000915 | furniture | pages [20] -->


<!-- b000916 | furniture | pages [20] -->


<!-- b000917 | furniture | pages [20] -->


<!-- b000918 | furniture | pages [20] -->


<!-- b000919 | furniture | pages [20] -->


<!-- b000920 | furniture | pages [20] -->


<!-- b000921 | furniture | pages [20] -->


<!-- b000922 | furniture | pages [20] -->


<!-- b000923 | furniture | pages [20] -->


<!-- b000924 | furniture | pages [20] -->
Page 20 of 25

<!-- b000925 | prose | pages [20] -->
each typical sample. Since we built a prediction model for the distribution of the number of guesses for a given solution word at a future date in Section 6.2, we have two bases for judging the difficulty of words. One is based on the predicted distribution of the number of guess words, and the other is based on the attribute vector of the solution word . 1. Difficulty determination method based on the predicted distribution of reports:

<!-- b000926 | prose | pages [20] -->
The prediction model in Section 6.2 is used to predict the distribution of the number of guesses of words to obtain the prediction . Then the difficulty  is judged based on the Euclidean distance and the assignment principle of the K-Means algorithm.

<!-- b000927 | furniture | pages [20] -->


<!-- b000928 | prose | pages [20] -->
is the center of mass of the -th difficulty, where .

<!-- b000929 | prose | pages [20] -->
2. Difficulty determination method based on attribute vectors:

<!-- b000930 | prose | pages [20] -->
The attribute vector of the solution word is counted, and then its difficulty is judged based on the Euclidean distance and the assignment principle of the K-Means algorithm.

<!-- b000931 | furniture | pages [20] -->


<!-- b000932 | prose | pages [20] -->
is the typical sample attribute vector for the th difficulty, where .

<!-- b000933 | heading | pages [20] -->
7.2 Analysis of Word Difficulty Classification Results

<!-- b000934 | furniture | pages [20] -->


<!-- b000935 | furniture | pages [20] -->


<!-- b000936 | furniture | pages [20] -->


<!-- b000937 | furniture | pages [20] -->


<!-- b000938 | furniture | pages [20] -->


<!-- b000939 | furniture | pages [20] -->


<!-- b000940 | furniture | pages [20] -->


<!-- b000941 | furniture | pages [20] -->


<!-- b000942 | furniture | pages [20] -->


<!-- b000943 | furniture | pages [20] -->


<!-- b000944 | furniture | pages [20] -->


<!-- b000945 | furniture | pages [20] -->


<!-- b000946 | furniture | pages [20] -->


<!-- b000947 | furniture | pages [20] -->


<!-- b000948 | furniture | pages [20] -->


<!-- b000949 | furniture | pages [20] -->


<!-- b000950 | furniture | pages [20] -->


<!-- b000951 | furniture | pages [20] -->


<!-- b000952 | furniture | pages [20] -->


<!-- b000953 | furniture | pages [20] -->


<!-- b000954 | furniture | pages [20] -->


<!-- b000955 | furniture | pages [20] -->


<!-- b000956 | furniture | pages [20] -->


<!-- b000957 | furniture | pages [20] -->


<!-- b000958 | furniture | pages [20] -->


<!-- b000959 | furniture | pages [20] -->


<!-- b000960 | furniture | pages [20] -->


<!-- b000961 | furniture | pages [20] -->


<!-- b000962 | furniture | pages [20] -->


<!-- b000963 | furniture | pages [20] -->


<!-- b000964 | furniture | pages [20] -->


<!-- b000965 | furniture | pages [20] -->


<!-- b000966 | furniture | pages [20] -->


<!-- b000967 | furniture | pages [20] -->


<!-- b000968 | furniture | pages [20] -->


<!-- b000969 | furniture | pages [20] -->


<!-- b000970 | furniture | pages [20] -->


<!-- b000971 | furniture | pages [20] -->


<!-- b000972 | furniture | pages [20] -->


<!-- b000973 | furniture | pages [20] -->


<!-- b000974 | furniture | pages [20] -->


<!-- b000975 | furniture | pages [20] -->


<!-- b000976 | furniture | pages [20] -->


<!-- b000977 | furniture | pages [20] -->


<!-- b000978 | furniture | pages [20] -->


<!-- b000979 | furniture | pages [20] -->


<!-- b000980 | furniture | pages [20] -->


<!-- b000981 | furniture | pages [20] -->


<!-- b000982 | furniture | pages [20] -->


<!-- b000983 | furniture | pages [20] -->


<!-- b000984 | furniture | pages [20] -->


<!-- b000985 | furniture | pages [20] -->


<!-- b000986 | furniture | pages [20] -->


<!-- b000987 | furniture | pages [20] -->


<!-- b000988 | furniture | pages [20] -->


<!-- b000989 | furniture | pages [20] -->


<!-- b000990 | furniture | pages [20] -->


<!-- b000991 | furniture | pages [20] -->


<!-- b000992 | furniture | pages [20] -->


<!-- b000993 | furniture | pages [20] -->


<!-- b000994 | furniture | pages [20] -->


<!-- b000995 | furniture | pages [20] -->


<!-- b000996 | furniture | pages [20] -->


<!-- b000997 | furniture | pages [20] -->


<!-- b000998 | furniture | pages [20] -->


<!-- b000999 | furniture | pages [20] -->


<!-- b001000 | furniture | pages [20] -->


<!-- b001001 | furniture | pages [20] -->


<!-- b001002 | furniture | pages [20] -->


<!-- b001003 | furniture | pages [20] -->


<!-- b001004 | furniture | pages [20] -->


<!-- b001005 | furniture | pages [20] -->


<!-- b001006 | furniture | pages [20] -->


<!-- b001007 | furniture | pages [20] -->


<!-- b001008 | furniture | pages [20] -->


<!-- b001009 | furniture | pages [20] -->


<!-- b001010 | furniture | pages [20] -->


<!-- b001011 | furniture | pages [20] -->


<!-- b001012 | furniture | pages [20] -->


<!-- b001013 | furniture | pages [20] -->


<!-- b001014 | furniture | pages [20] -->


<!-- b001015 | furniture | pages [20] -->


<!-- b001016 | furniture | pages [20] -->


<!-- b001017 | furniture | pages [20] -->


<!-- b001018 | furniture | pages [20] -->


<!-- b001019 | furniture | pages [20] -->


<!-- b001020 | furniture | pages [20] -->


<!-- b001021 | furniture | pages [20] -->


<!-- b001022 | furniture | pages [20] -->


<!-- b001023 | furniture | pages [20] -->


<!-- b001024 | furniture | pages [20] -->


<!-- b001025 | furniture | pages [20] -->


<!-- b001026 | furniture | pages [20] -->


<!-- b001027 | furniture | pages [20] -->


<!-- b001028 | furniture | pages [20] -->


<!-- b001029 | furniture | pages [20] -->


<!-- b001030 | furniture | pages [20] -->


<!-- b001031 | furniture | pages [20] -->


<!-- b001032 | furniture | pages [20] -->


<!-- b001033 | furniture | pages [20] -->


<!-- b001034 | furniture | pages [20] -->


<!-- b001035 | furniture | pages [20] -->


<!-- b001036 | furniture | pages [20] -->


<!-- b001037 | furniture | pages [20] -->


<!-- b001038 | furniture | pages [20] -->


<!-- b001039 | furniture | pages [20] -->


<!-- b001040 | furniture | pages [20] -->


<!-- b001041 | furniture | pages [20] -->


<!-- b001042 | furniture | pages [20] -->


<!-- b001043 | furniture | pages [20] -->


<!-- b001044 | furniture | pages [20] -->


<!-- b001045 | furniture | pages [20] -->


<!-- b001046 | furniture | pages [20] -->


<!-- b001047 | furniture | pages [20] -->


<!-- b001048 | furniture | pages [20] -->


<!-- b001049 | furniture | pages [20] -->


<!-- b001050 | furniture | pages [20] -->


<!-- b001051 | furniture | pages [20] -->


<!-- b001052 | furniture | pages [20] -->


<!-- b001053 | furniture | pages [20] -->


<!-- b001054 | furniture | pages [20] -->


<!-- b001055 | furniture | pages [20] -->


<!-- b001056 | furniture | pages [20] -->


<!-- b001057 | furniture | pages [20] -->


<!-- b001058 | furniture | pages [20] -->


<!-- b001059 | furniture | pages [20] -->


<!-- b001060 | furniture | pages [20] -->


<!-- b001061 | furniture | pages [20] -->


<!-- b001062 | furniture | pages [20] -->


<!-- b001063 | furniture | pages [20] -->


<!-- b001064 | furniture | pages [20] -->


<!-- b001065 | furniture | pages [20] -->


<!-- b001066 | furniture | pages [20] -->


<!-- b001067 | furniture | pages [20] -->


<!-- b001068 | furniture | pages [20] -->


<!-- b001069 | furniture | pages [20] -->


<!-- b001070 | furniture | pages [20] -->


<!-- b001071 | furniture | pages [20] -->


<!-- b001072 | furniture | pages [20] -->


<!-- b001073 | furniture | pages [20] -->


<!-- b001074 | furniture | pages [20] -->


<!-- b001075 | furniture | pages [20] -->


<!-- b001076 | furniture | pages [20] -->


<!-- b001077 | furniture | pages [20] -->


<!-- b001078 | furniture | pages [20] -->


<!-- b001079 | furniture | pages [20] -->


<!-- b001080 | furniture | pages [20] -->


<!-- b001081 | furniture | pages [20] -->


<!-- b001082 | furniture | pages [20] -->


<!-- b001083 | furniture | pages [20] -->


<!-- b001084 | furniture | pages [20] -->


<!-- b001085 | furniture | pages [20] -->


<!-- b001086 | furniture | pages [20] -->


<!-- b001087 | furniture | pages [20] -->


<!-- b001088 | furniture | pages [20] -->


<!-- b001089 | furniture | pages [20] -->


<!-- b001090 | furniture | pages [20] -->


<!-- b001091 | furniture | pages [20] -->


<!-- b001092 | furniture | pages [20] -->


<!-- b001093 | furniture | pages [20] -->


<!-- b001094 | furniture | pages [20] -->


<!-- b001095 | furniture | pages [20] -->


<!-- b001096 | furniture | pages [20] -->


<!-- b001097 | furniture | pages [20] -->


<!-- b001098 | furniture | pages [20] -->


<!-- b001099 | furniture | pages [20] -->


<!-- b001100 | furniture | pages [20] -->


<!-- b001101 | furniture | pages [20] -->


<!-- b001102 | furniture | pages [20] -->


<!-- b001103 | furniture | pages [20] -->


<!-- b001104 | furniture | pages [20] -->


<!-- b001105 | furniture | pages [20] -->


<!-- b001106 | furniture | pages [20] -->


<!-- b001107 | furniture | pages [20] -->


<!-- b001108 | furniture | pages [20] -->


<!-- b001109 | furniture | pages [20] -->


<!-- b001110 | furniture | pages [20] -->


<!-- b001111 | furniture | pages [20] -->


<!-- b001112 | furniture | pages [20] -->


<!-- b001113 | furniture | pages [20] -->


<!-- b001114 | furniture | pages [20] -->


<!-- b001115 | furniture | pages [20] -->


<!-- b001116 | furniture | pages [20] -->


<!-- b001117 | furniture | pages [20] -->


<!-- b001118 | furniture | pages [20] -->


<!-- b001119 | furniture | pages [20] -->


<!-- b001120 | furniture | pages [20] -->


<!-- b001121 | furniture | pages [20] -->


<!-- b001122 | furniture | pages [20] -->


<!-- b001123 | furniture | pages [20] -->


<!-- b001124 | furniture | pages [20] -->


<!-- b001125 | furniture | pages [20] -->


<!-- b001126 | furniture | pages [20] -->


<!-- b001127 | furniture | pages [20] -->


<!-- b001128 | furniture | pages [20] -->


<!-- b001129 | furniture | pages [20] -->


<!-- b001130 | furniture | pages [20] -->


<!-- b001131 | furniture | pages [20] -->


<!-- b001132 | furniture | pages [20] -->


<!-- b001133 | furniture | pages [20] -->


<!-- b001134 | furniture | pages [20] -->


<!-- b001135 | furniture | pages [20] -->


<!-- b001136 | furniture | pages [20] -->


<!-- b001137 | furniture | pages [20] -->


<!-- b001138 | furniture | pages [20] -->


<!-- b001139 | furniture | pages [20] -->


<!-- b001140 | furniture | pages [20] -->


<!-- b001141 | furniture | pages [20] -->


<!-- b001142 | furniture | pages [20] -->


<!-- b001143 | furniture | pages [20] -->


<!-- b001144 | furniture | pages [20] -->


<!-- b001145 | furniture | pages [20] -->


<!-- b001146 | furniture | pages [20] -->


<!-- b001147 | furniture | pages [20] -->


<!-- b001148 | furniture | pages [20] -->


<!-- b001149 | furniture | pages [20] -->


<!-- b001150 | furniture | pages [20] -->


<!-- b001151 | furniture | pages [20] -->


<!-- b001152 | furniture | pages [20] -->


<!-- b001153 | furniture | pages [20] -->


<!-- b001154 | furniture | pages [20] -->


<!-- b001155 | furniture | pages [20] -->


<!-- b001156 | furniture | pages [20] -->


<!-- b001157 | furniture | pages [20] -->


<!-- b001158 | furniture | pages [20] -->


<!-- b001159 | furniture | pages [20] -->


<!-- b001160 | furniture | pages [20] -->


<!-- b001161 | furniture | pages [20] -->


<!-- b001162 | furniture | pages [20] -->


<!-- b001163 | furniture | pages [20] -->


<!-- b001164 | furniture | pages [20] -->


<!-- b001165 | furniture | pages [20] -->


<!-- b001166 | furniture | pages [20] -->


<!-- b001167 | furniture | pages [20] -->


<!-- b001168 | furniture | pages [20] -->


<!-- b001169 | furniture | pages [20] -->


<!-- b001170 | furniture | pages [20] -->


<!-- b001171 | furniture | pages [20] -->


<!-- b001172 | furniture | pages [20] -->


<!-- b001173 | furniture | pages [20] -->


<!-- b001174 | furniture | pages [20] -->


<!-- b001175 | furniture | pages [20] -->


<!-- b001176 | furniture | pages [20] -->


<!-- b001177 | furniture | pages [20] -->


<!-- b001178 | furniture | pages [20] -->


<!-- b001179 | furniture | pages [20] -->


<!-- b001180 | furniture | pages [20] -->


<!-- b001181 | furniture | pages [20] -->


<!-- b001182 | furniture | pages [20] -->


<!-- b001183 | furniture | pages [20] -->


<!-- b001184 | furniture | pages [20] -->


<!-- b001185 | furniture | pages [20] -->


<!-- b001186 | furniture | pages [20] -->


<!-- b001187 | furniture | pages [20] -->


<!-- b001188 | furniture | pages [20] -->


<!-- b001189 | furniture | pages [20] -->


<!-- b001190 | furniture | pages [20] -->


<!-- b001191 | furniture | pages [20] -->


<!-- b001192 | furniture | pages [20] -->


<!-- b001193 | furniture | pages [20] -->


<!-- b001194 | furniture | pages [20] -->


<!-- b001195 | furniture | pages [20] -->


<!-- b001196 | furniture | pages [20] -->


<!-- b001197 | furniture | pages [20] -->


<!-- b001198 | furniture | pages [20] -->


<!-- b001199 | furniture | pages [20] -->


<!-- b001200 | furniture | pages [20] -->


<!-- b001201 | furniture | pages [20] -->


<!-- b001202 | furniture | pages [20] -->


<!-- b001203 | furniture | pages [20] -->


<!-- b001204 | furniture | pages [20] -->


<!-- b001205 | furniture | pages [20] -->


<!-- b001206 | furniture | pages [20] -->


<!-- b001207 | furniture | pages [20] -->


<!-- b001208 | furniture | pages [20] -->


<!-- b001209 | furniture | pages [20] -->


<!-- b001210 | furniture | pages [20] -->


<!-- b001211 | furniture | pages [20] -->


<!-- b001212 | furniture | pages [20] -->


<!-- b001213 | furniture | pages [20] -->


<!-- b001214 | furniture | pages [20] -->


<!-- b001215 | furniture | pages [20] -->


<!-- b001216 | furniture | pages [20] -->


<!-- b001217 | furniture | pages [20] -->


<!-- b001218 | furniture | pages [20] -->


<!-- b001219 | furniture | pages [20] -->


<!-- b001220 | furniture | pages [20] -->


<!-- b001221 | furniture | pages [20] -->


<!-- b001222 | furniture | pages [20] -->


<!-- b001223 | furniture | pages [20] -->


<!-- b001224 | furniture | pages [20] -->


<!-- b001225 | furniture | pages [20] -->


<!-- b001226 | furniture | pages [20] -->


<!-- b001227 | furniture | pages [20] -->


<!-- b001228 | furniture | pages [20] -->


<!-- b001229 | furniture | pages [20] -->


<!-- b001230 | furniture | pages [20] -->


<!-- b001231 | furniture | pages [20] -->


<!-- b001232 | furniture | pages [20] -->


<!-- b001233 | furniture | pages [20] -->


<!-- b001234 | furniture | pages [20] -->


<!-- b001235 | furniture | pages [20] -->


<!-- b001236 | furniture | pages [20] -->


<!-- b001237 | furniture | pages [20] -->


<!-- b001238 | furniture | pages [20] -->


<!-- b001239 | furniture | pages [20] -->


<!-- b001240 | caption | pages [20] -->
Figure 13: Difficulty classification result word cloud

<!-- b001241 | prose | pages [20] -->
The results were obtained by K-Means clustering in four categories of difficulty, which were classified as Easy, Normal, Hard, and Master in order of difficulty from small to large, and a typical word was selected for visual analysis, as shown in Figure 14.

<!-- b001242 | furniture | pages [20] -->


<!-- b001243 | furniture | pages [21] -->
Team # 2311717

<!-- b001244 | furniture | pages [21] -->


<!-- b001245 | furniture | pages [21] -->


<!-- b001246 | furniture | pages [21] -->


<!-- b001247 | furniture | pages [21] -->


<!-- b001248 | furniture | pages [21] -->


<!-- b001249 | furniture | pages [21] -->


<!-- b001250 | prose | pages [21] -->
Master

<!-- b001251 | prose | pages [21] -->
Dandy

<!-- b001252 | prose | pages [21] -->
2

<!-- b001253 | prose | pages [21] -->
11

<!-- b001254 | prose | pages [21] -->
23

<!-- b001255 | prose | pages [21] -->
Hard

<!-- b001256 | prose | pages [21] -->
Bough

<!-- b001257 | prose | pages [21] -->
3

<!-- b001258 | prose | pages [21] -->
17

<!-- b001259 | prose | pages [21] -->
35

<!-- b001260 | prose | pages [21] -->
Normal

<!-- b001261 | prose | pages [21] -->
Maple

<!-- b001262 | prose | pages [21] -->
1

<!-- b001263 | prose | pages [21] -->
6

<!-- b001264 | prose | pages [21] -->
26

<!-- b001265 | prose | pages [21] -->
Easy

<!-- b001266 | prose | pages [21] -->
Chest

<!-- b001267 | prose | pages [21] -->
1

<!-- b001268 | prose | pages [21] -->
14

<!-- b001269 | prose | pages [21] -->
35

<!-- b001270 | prose | pages [21] -->
0% 10% 20% 30% 40%

<!-- b001271 | prose | pages [21] -->
1 try 2 tries 3 tries

<!-- b001272 | furniture | pages [21] -->


<!-- b001273 | furniture | pages [21] -->


<!-- b001274 | furniture | pages [21] -->


<!-- b001275 | furniture | pages [21] -->


<!-- b001276 | furniture | pages [21] -->


<!-- b001277 | furniture | pages [21] -->


<!-- b001278 | furniture | pages [21] -->


<!-- b001279 | furniture | pages [21] -->
Page 21 of 25

<!-- b001280 | prose | pages [21] -->
29

<!-- b001281 | prose | pages [21] -->
24

<!-- b001282 | furniture | pages [21] -->


<!-- b001283 | prose | pages [21] -->
28

<!-- b001284 | prose | pages [21] -->
13

<!-- b001285 | furniture | pages [21] -->


<!-- b001286 | prose | pages [21] -->
36

<!-- b001287 | prose | pages [21] -->
21

<!-- b001288 | prose | pages [21] -->
8

<!-- b001289 | furniture | pages [21] -->


<!-- b001290 | prose | pages [21] -->
31

<!-- b001291 | prose | pages [21] -->
14

<!-- b001292 | prose | pages [21] -->
5

<!-- b001293 | furniture | pages [21] -->


<!-- b001294 | prose | pages [21] -->
50% 60% 70% 80% 90% 100%

<!-- b001295 | prose | pages [21] -->
4 tries 5 tries 6 tries (X)

<!-- b001296 | furniture | pages [21] -->


<!-- b001297 | caption | pages [21] -->
Figure 14: Word difficulty classification results bar chart

<!-- b001298 | prose | pages [21] -->
As we can see from the above graph, when the puzzle is easier, the distribution of reports tends to guess the solved word less often, and vice versa. For example, the distribution of re- ports for the word "Chest" is mainly in 2tries, 3tries, and 4tries, and the distribution is smaller in 6tries and 7tries.

<!-- b001299 | caption | pages [21] -->
Table 6: Correlation coefficient of word attributes and difficulty

<!-- b001300 | prose | pages [21] -->
F1 F2 F3

<!-- b001301 | furniture | pages [21] -->


<!-- b001302 | prose | pages [21] -->
F4 F5 WCN VN

<!-- b001303 | prose | pages [21] -->
0.637634 0.813854 0.336972 0.417339 0.311806 0.81528 0.8989

<!-- b001304 | prose | pages [21] -->
After calculating the Pearson correlation coefficients between word attributes and diffi- culty ratings, we obtain the results in Table 6. The above table shows that some attributes have a strong correlation with difficulty. We take the word attributes with greater than 0.6 as the difficulty classification attributes and form the attribute vector .

<!-- b001305 | prose | pages [21] -->
Finally, we calculate the distance from the attribute vector of the word EERIR to the at- th difficulty typical sample tribute vector of the , which are R1 4.2385, R2 3.0021, R3 2.1823, R4 0.6250, and the closest distance to "Dandy". Thus, the difficulty of the word EERIR was obtained as "Master".

<!-- b001306 | heading | pages [21] -->
8 Task 4: Other Interesting Features

<!-- b001307 | prose | pages [21] -->
In exploring the statistical properties of the number of reports, we found that the density of the distribution of the number of reports over 359 days showed a similar pattern to its trend over time. Then, we fitted the distribution of the number of reports. As shown in Figure 15, a good result can be achieved by fitting the number of reports using a log-normal distribution. Referring to Figure 16, it can be found that the distribution obtained from the fit shows a fairly high similarity to the change in the number of reports over time.

<!-- b001308 | furniture | pages [21] -->


<!-- b001309 | prose | pages [22] -->
校苑

<!-- b001310 | furniture | pages [22] -->
Team # 2311717

<!-- b001311 | furniture | pages [22] -->


<!-- b001312 | furniture | pages [22] -->


<!-- b001313 | furniture | pages [22] -->


<!-- b001314 | furniture | pages [22] -->


<!-- b001315 | furniture | pages [22] -->


<!-- b001316 | furniture | pages [22] -->


<!-- b001317 | prose | pages [22] -->
校苑数模

<!-- b001318 | prose | pages [22] -->
校苑数

<!-- b001319 | furniture | pages [22] -->
校苑数模

<!-- b001320 | furniture | pages [22] -->


<!-- b001321 | furniture | pages [22] -->


<!-- b001322 | furniture | pages [22] -->


<!-- b001323 | furniture | pages [22] -->


<!-- b001324 | furniture | pages [22] -->


<!-- b001325 | furniture | pages [22] -->


<!-- b001326 | furniture | pages [22] -->


<!-- b001327 | furniture | pages [22] -->
Page 22 of 25

<!-- b001328 | prose | pages [22] -->
校苑

<!-- b001329 | prose | pages [22] -->
校苑数模

<!-- b001330 | furniture | pages [22] -->


<!-- b001331 | furniture | pages [22] -->


<!-- b001332 | furniture | pages [22] -->


<!-- b001333 | caption | pages [22] -->
Figure 15: Fitting to the distribution of report number   Figure 16: Change in report number over time

<!-- b001334 | prose | pages [22] -->
However, we note that the distribution of the number of reports is not uniform in time, and this distribution does not take into account the time factor. So this fit does not provide

<!-- b001335 | prose | pages [22] -->
校苑数模

<!-- b001336 | prose | pages [22] -->
much information for predicting the number of reports. This led us not to investigate the phe- nomenon in more depth. However, we speculate that there may be some interesting statistical properties under this phenomenon.

<!-- b001337 | prose | pages [22] -->
校

<!-- b001338 | prose | pages [22] -->
In addition, when we explored the distribution of users' reported results, we found that the percentage fluctuation of 3 attempts to complete the game was the largest. As shown in Figure 17, we believe that this phenomenon is strongly related to the low prediction accuracy of our

<!-- b001339 | prose | pages [22] -->
校苑数模

<!-- b001340 | prose | pages [22] -->
report distribution prediction model for 3-attempt game completion.

<!-- b001341 | prose | pages [22] -->
模

<!-- b001342 | prose | pages [22] -->
苑数模

<!-- b001343 | prose | pages [22] -->
校苑数模

<!-- b001344 | prose | pages [22] -->
校苑数模

<!-- b001345 | furniture | pages [22] -->


<!-- b001346 | caption | pages [22] -->
Figure 17: Report distribution box chart

<!-- b001347 | heading | pages [22] -->
9 Sensitivity Analysis

<!-- b001348 | prose | pages [22] -->
For the prediction model of the number of reports in Task 1, we fine-tune the intercept

<!-- b001349 | furniture | pages [22] -->
校苑数模

<!-- b001350 | prose | pages [22] -->
of the popularity relaxation function by multiplying it by a certain scale factor  to observe the sensitivity of the model. The average change in the corresponding prediction interval when the confidence level is 75% is then calculated as:

<!-- b001351 | prose | pages [22] -->
苑数模

<!-- b001352 | furniture | pages [22] -->


<!-- b001353 | prose | pages [22] -->
is the length of the sequence. Then, we take where

<!-- b001354 | furniture | pages [22] -->


<!-- b001355 | prose | pages [22] -->
separately for

<!-- b001356 | prose | pages [22] -->
模

<!-- b001357 | furniture | pages [23] -->
Team # 2311717

<!-- b001358 | furniture | pages [23] -->


<!-- b001359 | furniture | pages [23] -->


<!-- b001360 | furniture | pages [23] -->


<!-- b001361 | furniture | pages [23] -->


<!-- b001362 | furniture | pages [23] -->


<!-- b001363 | furniture | pages [23] -->


<!-- b001364 | furniture | pages [23] -->


<!-- b001365 | furniture | pages [23] -->


<!-- b001366 | furniture | pages [23] -->


<!-- b001367 | furniture | pages [23] -->


<!-- b001368 | furniture | pages [23] -->


<!-- b001369 | furniture | pages [23] -->


<!-- b001370 | furniture | pages [23] -->


<!-- b001371 | furniture | pages [23] -->
Page 23 of 25

<!-- b001372 | prose | pages [23] -->
observation. When , the average variation of the prediction interval reached about 8.3%. When , the average variation of the prediction interval reaches about 32.71%. When , the average variation of the prediction interval reaches about 78.2%, and the left boundary of the prediction interval is close to 0 at this time.

<!-- b001373 | prose | pages [23] -->
This indicates that the model we have developed is somewhat robust, but is not very ap- plicable to situations where there are large stochastic fluctuations even in steady periods.

<!-- b001374 | heading | pages [23] -->
10 Model Evaluation and Further Discussion

<!-- b001375 | heading | pages [23] -->
10.1 Strengths

<!-- b001376 | prose | pages [23] -->
⚫ We decompose the time series into trend signs and stochastic fluctuations and then make

<!-- b001377 | prose | pages [23] -->
separate predictions. The model built according to this has a good interpretation of the time series patterns. ⚫ We do not define the difficulty of words by ourselves, but generalize the difficulty based

<!-- b001378 | prose | pages [23] -->
on the results of user play. Therefore, the difficulty rating we obtained is more relevant to the user's play experience. ⚫ We applied the integration algorithm to weaken the generalization error caused by chance

<!-- b001379 | prose | pages [23] -->
due to neural network training. Eventually, better prediction accuracy than individual neu- ral networks is achieved.

<!-- b001380 | heading | pages [23] -->
10.2 Weaknesses

<!-- b001381 | prose | pages [23] -->
⚫ For the popular phases of the game, the prediction interval given by our reported volume prediction model is much wider compared to other phases. This leads to the possibility that our model's prediction results in such phases may not be very informative. ⚫ Our model for predicting the distribution of reported outcomes relies heavily on the repre- sentativeness of the dataset. However, for the size of the provided dataset, it is more difficult to ensure the representativeness of the overall sample space.

<!-- b001382 | heading | pages [23] -->
10.3 Further Discussion

<!-- b001383 | prose | pages [23] -->
The model we build is based only on the existing data given in the report, but other avail- able information can be further integrated. In the prediction model of the number of players, in addition to using time series information, we can also analyze the attractiveness of the game based on the text information posted by users and obtain players' emotional experience of the game; based on the personal information of users who share the results, we can simulate users as nodes and build an information dissemination model based on social network analysis, which in turn can portray the user behavior that affects the heat of game dissemination and make a more comprehensive popularity prediction.

<!-- b001384 | heading | pages [23] -->
11 Conclusion

<!-- b001385 | prose | pages [23] -->
To mine the Wordle report information, we propose a series of novel models to solve the problem of predicting the number of reports and the distribution of results. At the same time, we fully analyze the attributes of solution words and can classify the difficulty of a given word.

<!-- b001386 | furniture | pages [23] -->


<!-- b001387 | furniture | pages [24] -->
Team # 2311717

<!-- b001388 | furniture | pages [24] -->


<!-- b001389 | furniture | pages [24] -->


<!-- b001390 | furniture | pages [24] -->


<!-- b001391 | furniture | pages [24] -->


<!-- b001392 | furniture | pages [24] -->


<!-- b001393 | furniture | pages [24] -->


<!-- b001394 | furniture | pages [24] -->


<!-- b001395 | furniture | pages [24] -->


<!-- b001396 | furniture | pages [24] -->


<!-- b001397 | furniture | pages [24] -->


<!-- b001398 | furniture | pages [24] -->


<!-- b001399 | furniture | pages [24] -->


<!-- b001400 | furniture | pages [24] -->


<!-- b001401 | furniture | pages [24] -->
Page 24 of 25

<!-- b001402 | prose | pages [24] -->
The proposed model only depends on the Data File and has good interpretation and rationality. 1. The report number prediction model can combine the long-term trend of quantity change over time with random fluctuations. The results of Gaussian regression on the number of reports describe the trend of the number of reports over time, while the non-homogeneous Poisson process describes the random fluctuation of the number of reports based on the trend. According to the life cycle of heat, we also introduce the popularity relaxation func- tion to modify the random process model. 2. The proportion of players choosing a game mode is less affected by the attributes of words, but is highly correlated with time. The level of confidence players have in their ability to perform and how they play is probably the main reason why they choose Hard Mode. 3. The distribution of the reported results prediction model can combine the word attribute characteristics and the time characteristics that affect the proportion of Hard Mode. We predict the distribution of guessing results based on the BP neural network, and integrate the predicted results of neural networks through the Bagging algorithm to improve the generalization performance of the model. 4. The word difficulty classification model can combine the distribution of report results with the attributes of words. Among them, the distribution of reported results only reflects the difficulty, while the word attributes are the root cause of the different difficulties. We di- vided the difficulty based on the K-Means algorithm, and explored the correlation between word attributes and difficulty classification based on the Pearson correlation coefficient. Finally, new words can be classified by difficulty based on this correlation.

<!-- b001403 | heading | pages [24] -->
References

<!-- b001404 | references | pages [24] -->
[1] Q. Zhao, M. A. Erdogdu, H. Y. He, A. Rajaraman, and J. Leskovec, "SEISMIC: A Self-

<!-- b001405 | references | pages [24] -->
Exciting Point Process Model for Predicting Tweet Popularity," ACM, 2015.

<!-- b001406 | references | pages [24] -->
[2] H. W. Shen, D. Wang, C. Song, and A. Barabási, "Modeling and Predicting Popularity

<!-- b001407 | references | pages [24] -->
Dynamics via Reinforced Poisson Processes," AAAI Press, 2014.

<!-- b001408 | references | pages [24] -->
[3] Q. Wu, C. Yang, X. Gao, H. Peng, and G. Chen, "EPAB: Early Pattern Aware Bayesian

<!-- b001409 | references | pages [24] -->
Model for Social Content Popularity Prediction," in 2018 IEEE International Conference

<!-- b001410 | references | pages [24] -->
on Data Mining (ICDM), 2018.

<!-- b001411 | references | pages [24] -->
[4] Z. Zhen, S. Shao, X. Gao, G.Chen, "Social Circle and Attention Based Information Pop-

<!-- b001412 | references | pages [24] -->
ularity Prediction," Journal of Co puter Science, 2021.

<!-- b001413 | references | pages [24] -->
[5] J. Feng, "Research on social network event heat prediction based on text analysis," Harbin

<!-- b001414 | references | pages [24] -->
Institute of Tec nolog , 2018.

<!-- b001415 | references | pages [24] -->
[6] G. Ian, B. Yoshua, C. Aaron, "Deep Learning: Adaptive Computation and Machine Learn-

<!-- b001416 | references | pages [24] -->
ing series," The MIT Press, 2016.

<!-- b001417 | references | pages [24] -->
[7] C. D. Ari, "How to choose the number of hidden layers and nodes in a feedforward neu-

<!-- b001418 | references | pages [24] -->
ral net-work? " StackE c ange, https://stats.stackexchange.com/questions/181/how-to-

<!-- b001419 | references | pages [24] -->
choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw.

<!-- b001420 | references | pages [24] -->
[8] L. Kai, L. J. Cui, "Diversity and Performance Comparison for Ensemble Learning

<!-- b001421 | references | pages [24] -->
Algorithms," Co puter Engineering, 2008.

<!-- b001422 | furniture | pages [24] -->


<!-- b001423 | furniture | pages [25] -->
Team # 2311717

<!-- b001424 | furniture | pages [25] -->


<!-- b001425 | furniture | pages [25] -->


<!-- b001426 | furniture | pages [25] -->


<!-- b001427 | furniture | pages [25] -->


<!-- b001428 | furniture | pages [25] -->


<!-- b001429 | furniture | pages [25] -->


<!-- b001430 | heading | pages [25] -->
Letter

<!-- b001431 | prose | pages [25] -->
Dear Puzzle Editor of the New York Times,

<!-- b001432 | furniture | pages [25] -->


<!-- b001433 | furniture | pages [25] -->


<!-- b001434 | furniture | pages [25] -->


<!-- b001435 | furniture | pages [25] -->


<!-- b001436 | furniture | pages [25] -->


<!-- b001437 | furniture | pages [25] -->


<!-- b001438 | furniture | pages [25] -->


<!-- b001439 | furniture | pages [25] -->
Page 25 of 25

<!-- b001440 | prose | pages [25] -->
We were happy to dig into the mystery behind Wordle's data through this modeling. Either for the joy of uncovering a puzzle or to spit out a question that is too difficult, the share button that appears immediately after completing Wordle allows players to bring their emotions of the moment to more people. Wordle has become a social currency as people continue to share it.

<!-- b001441 | prose | pages [25] -->
Based on the reported results data collected on Twitter over the past year, we built three models: a report number prediction model for interval prediction of future report numbers; a report distribution prediction model for predicting the distribution of the number of guesses on future report results; and a word difficulty classification model for classifying the difficulty of solving a given vocabulary. We have obtained some valuable findings that come from compre- hensively digging into the deeper information of the reports, helping you to discover the secrets in last year's game data and to develop new puzzles.

<!-- b001442 | prose | pages [25] -->
First, we built a report number prediction model to describe past or predict future report number intervals to help you more easily track Wordle's popularity trends. We found that the overall pattern of change in the number of reports is determined by the social properties and social patterns of the game, while the random fluctuations in the number of reports have statis- tical properties that vary over time and in popularity.

<!-- b001443 | prose | pages [25] -->
We analyzed the properties of the daily solution words, which included features such as the number of letters, their locations and special roots. We preliminarily analyzed whether words influenced players' game mode choices. We concluded that the proportion of Hard Mode choices increased over time and then leveled off, while word attributes did not affect the pro- portion for Hard Mode. Players' level of confidence in their performance ability and their play mentality may be the main reasons for whether they choose the Hard Mode or not.

<!-- b001444 | prose | pages [25] -->
Next, we built a prediction model for the distribution of reported results based on Bag- ging's integrated BP neural network. We can predict the distribution of reported outcomes based on the future date and the solution word on that date. Simply put, this model takes into account both time series and word attributes, and helps you predict the distribution of players' guesses for a word on a given day after you have decided on the puzzle.

<!-- b001445 | prose | pages [25] -->
Then, based on the distribution of reported results, we classify the word difficulty based on the K-Means algorithm and explore the association between word attributes and difficulty by the Pearson correlation coefficient. Thus, we can calculate the difficulty of the solution word from the attributes of a newly given word based on the difficulty classification model.

<!-- b001446 | prose | pages [25] -->
Finally, we list the following results, which may provide some reference for you: The interval for the number of reported results on March 1, 2023 is [7654, 20154]. The distribution of the results of EERIR on March 1, 2023 is (0, 1, 6, 25, 31, 25, 13). The difficulty of EERIE words is “Master” (Hardest).

<!-- b001447 | prose | pages [25] -->
Thanks for taking the time out of your busy schedule to read my letter. Hope our advice can help.

<!-- b001448 | furniture | pages [25] -->


<!-- b001449 | prose | pages [25] -->
Yours Sincerely,

<!-- b001450 | furniture | pages [25] -->
Team # 2311717
