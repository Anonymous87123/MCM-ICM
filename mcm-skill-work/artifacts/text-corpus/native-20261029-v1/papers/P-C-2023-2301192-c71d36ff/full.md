# P-C-2023-2301192-c71d36ff

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
2301192

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Crack the Wordle Puzzle:

<!-- b000009 | title | pages [1] -->
Word Attribute Analysis Approaches

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
In the past 600 days, a five-letter puzzle game called ”Wordle” has been launching a blast of upsurge on Twitter. Wordle players’ scores reports are crucial for managers as they provide valu- able information for evaluating game difficulty, predicting player numbers and making timely adjustments. To better analyze the reports and provide game improvement suggestions, we con- duct in-depth and close studies on this topic from multiple perspectives and levels.

<!-- b000012 | prose | pages [1] -->
Firstly, to explain the changes in the number of Wordle reports and make predictions, we use an analogy between playing Wordle and the spread of infectious diseases. We compare playing Wordle with infection, players with infected individuals, individuals who have not played Wor- dle for a long time with susceptible individuals, individuals who have become tired of the game with recovered individuals, sharing on Twitter with transmission, and quitting the game with recovery. Based on these assumptions, we use the SIRS model to fit the curve and explain the overall trend. We also use the Prophet model to insert breakpoints to explain data oscillations and provide a prediction interval for future data. Model evaluation results show that our model has high interpretability and accuracy.

<!-- b000013 | prose | pages [1] -->
Next, we extract various word attributes from a word database containing a large amount of corpus information and use multiple linear regression to investigate whether there is a relation- ship between word attributes and Hard-Mode scores. We then test the significance of the model based on the F-statistic. The result shows no significant correlation between these two factors.

<!-- b000014 | prose | pages [1] -->
Besides, we construct a BP neural network model based on the previously extracted word attributes to predict the distribution of the number of word guesses. The evaluation results show that the model has high prediction accuracy and efficiency, laying a solid foundation for next step analysis.

<!-- b000015 | prose | pages [1] -->
Furthermore, we use K-means++ clustering algorithm to divide words into three categories: easy, medium, and hard. We analyze the relationship between word attributes and difficulty to classify solution words by difficulty. We find that the difficulty of a word is closely related to the number of different letters in the word, the sum of letter frequencies, and the breadth of usage of the word in different fields, but there is no significant evidence of a correlation between difficulty and word frequency. Combined with the previous BP neural network model, we can accurately classify words.

<!-- b000016 | prose | pages [1] -->
In addition, we find that common words such as ”mummy” and ”watch” have a higher guess- ing difficulty, and there is also a certain correlation between the first letter of a word and its guessing difficulty.

<!-- b000017 | prose | pages [1] -->
Finally, we present predictive data and improvement suggestions to the editors of The New York Times to assist in improving Wordle and boosting the appealing feature of the game.

<!-- b000018 | keywords | pages [1] -->
Keywords: Prophet; SIRS; Multiple Linear Regression; BP Neural Network; K-Means++

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1

<!-- b000021 | heading | pages [2] -->
Introduction

<!-- b000022 | prose | pages [2] -->
3 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000023 | prose | pages [2] -->
2

<!-- b000024 | heading | pages [2] -->
Assumptions and Notations

<!-- b000025 | prose | pages [2] -->
3

<!-- b000026 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1

<!-- b000027 | heading | pages [2] -->
Assumptions

<!-- b000028 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000029 | heading | pages [2] -->
Notations

<!-- b000030 | prose | pages [2] -->
4

<!-- b000031 | heading | pages [2] -->
Model 1-Integration of Interpretation and Prediction Model based on Prophet

<!-- b000032 | prose | pages [2] -->
3 and SIRS 5 Data Preprocessing and Exploratory Analysis . . . . . . . . . . . . . . . . . . 3.1 5 Data Collection and Pre-processing 3.1.1 . . . . . . . . . . . . . . . . . . .

<!-- b000033 | prose | pages [2] -->
5 Data Description and Exploratory Analysis . . . . . . . . . . . . . . . 3.1.2 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 Prophet Model 6 Explanation of the Changes in the Number of Reports . . . . . . . . . . . . . . 3.3 9 Extracting the Attributes of Words . . . . . . . . . . . . . . . . . . . . . . . . 3.4 10 Impact of Word Attributes on the Proportion of Hard-Mode Reports . . . . . . 3.5 12 Model Establishment . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.5.1 12 Significance Test of Regression Equation 3.5.2 . . . . . . . . . . . . . . . .

<!-- b000034 | prose | pages [2] -->
12

<!-- b000035 | heading | pages [2] -->
Model 2-Distribution Prediction Model based on BP Neural Network

<!-- b000036 | prose | pages [2] -->
4 13 Model Building of BP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 13 Model Uncertainty of BP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 Model Evaluation of BP 14 Model Prediction of BP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 14

<!-- b000037 | heading | pages [2] -->
Model 3-Diﬀiculty Classification based on K-Means++

<!-- b000038 | prose | pages [2] -->
5 14 Clustering Analysis based on K-Means++. . . . . . . . . . . . . . . . . . . . . 5.1 14 Relationship between Word Attributes and Difficulty Levels . . . . . . . . . . . 5.2 15 Relationship Between Difficulty Levels and NDLW . . . . . . . . . . . 5.2.1 15 Relationship between Difficulty Levels and SLF . . . . . . . . . . . . . 5.2.2 17 Relationship between Difficulty Levels and BU and Freq . . . . . . . . 5.2.3 17 PCA Discussion on the Accuracy of Model Classification . . . . . . . . . . . . 5.3 18 Determining the Difficulty Level of ”EERIE” . . . . . . . . . . . . . . . . . . 5.4

<!-- b000039 | prose | pages [2] -->
6 Interesting Surprise

<!-- b000040 | prose | pages [2] -->
19

<!-- b000041 | prose | pages [2] -->
20 Are These Words Really that Difficult? . . . . . . . . . . . . . . . . . . . . . . 6.1 20 Which Initial Letter Poses the Greatest Challenge for Solution Words? . . . . . 6.2 20 What Words Can Make Wordle Continue to be Popular? 6.3

<!-- b000042 | prose | pages [2] -->
7 Sensitivety Analysis

<!-- b000043 | prose | pages [2] -->
8

<!-- b000044 | heading | pages [2] -->
Model Assessment

<!-- b000045 | prose | pages [2] -->
. . . . . . . . . . . .

<!-- b000046 | prose | pages [2] -->
21

<!-- b000047 | prose | pages [2] -->
22

<!-- b000048 | prose | pages [2] -->
23 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 Strengths 23 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000049 | heading | pages [2] -->
References

<!-- b000050 | heading | pages [2] -->
Letter

<!-- b000051 | heading | pages [2] -->
Appendices

<!-- b000052 | heading | pages [2] -->
Appendix A Regression Equation

<!-- b000053 | prose | pages [2] -->
23

<!-- b000054 | prose | pages [2] -->
23

<!-- b000055 | prose | pages [2] -->
24

<!-- b000056 | prose | pages [2] -->
25

<!-- b000057 | prose | pages [2] -->
25

<!-- b000058 | furniture | pages [3] -->
Team # 2301192

<!-- b000059 | furniture | pages [3] -->
Page 3

<!-- b000060 | prose | pages [3] -->
1

<!-- b000061 | heading | pages [3] -->
Introduction

<!-- b000062 | prose | pages [3] -->
1.1

<!-- b000063 | heading | pages [3] -->
Background

<!-- b000064 | prose | pages [3] -->
Recently, Twitter has sparked a trend of sharing the Wordle report. Puzzle game developers in the past were often not very clear about the difficulty of their games for the public. Games that are too difficult can be frustrating, while too easy can be boring. With the development of information technology, using big data analysis to control the difficulty of puzzles has become the key to making puzzles more interesting. The New York Times’ Wordle game has collected statistics on the number of tries by players and the number of reports on Twitter. This data can be used to evaluate the number of players and the difficulty of a particular word, maintain players’ enthusiasm, and make the game more attractive.

<!-- b000065 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000066 | prose | pages [3] -->
The New York Times collected 359 days of Wordle player score reports, including report time, number, percentage of difficult mode reports, and number of attempts. To control for gameplay and estimate the number of players, it is necessary to analyze the trend of report numbers, mine information contained in word attributes, and measure the difficulty of words. To achieve these goals, we need to:

<!-- b000067 | prose | pages [3] -->
• Analyze the reasons for the changes in the number of reports on a large time scale (overall trend) and small time scale (data mutation).

<!-- b000068 | prose | pages [3] -->
• Collect and mine potential word attributes.

<!-- b000069 | prose | pages [3] -->
• Analyze whether the percentage of difficult mode reports is related to word attributes.

<!-- b000070 | prose | pages [3] -->
• Analyze the distribution of attempts and its potential relationship with word attributes.

<!-- b000071 | prose | pages [3] -->
• Identify the influence of word attributes on difficulty.

<!-- b000072 | prose | pages [3] -->
• Mine other information that could help improve Wordle.

<!-- b000073 | caption | pages [3] -->
Figure 1: the Flow Chart in this Paper

<!-- b000074 | furniture | pages [4] -->
Team # 2301192

<!-- b000075 | prose | pages [4] -->
2

<!-- b000076 | heading | pages [4] -->
Assumptions and Notations

<!-- b000077 | prose | pages [4] -->
2.1

<!-- b000078 | heading | pages [4] -->
Assumptions

<!-- b000079 | furniture | pages [4] -->
Page 4

<!-- b000080 | prose | pages [4] -->
To simplify the model, we have made several assumptions. However, we may need to relax some of these assumptions to optimize the model and increase its applicability in complex real- world environments.

<!-- b000081 | prose | pages [4] -->
• The number of Twitter users is essentially constant, and the probability of each user re- ceiving information related to Wordle is equal.

<!-- b000082 | prose | pages [4] -->
• All Wordle players are Twitter users, and all Twitter users are potential Wordle players.

<!-- b000083 | prose | pages [4] -->
• The word for each day in Wordle is completely random and chosen from all five-letter words.

<!-- b000084 | prose | pages [4] -->
• Players who report their game results on Twitter are a random sample of all players.

<!-- b000085 | prose | pages [4] -->
• People may get tired of playing Wordle, but they may eventually want to play again after a long time.

<!-- b000086 | prose | pages [4] -->
2.2

<!-- b000087 | heading | pages [4] -->
Notations

<!-- b000088 | caption | pages [4] -->
Table 1: 18 Part-of-Speech Symbols

<!-- b000089 | heading | pages [4] -->
Symbols

<!-- b000090 | prose | pages [4] -->
NN

<!-- b000091 | prose | pages [4] -->
Definition

<!-- b000092 | prose | pages [4] -->
Noun, singular or mass JJ RB VBP Adjective Adverb Verb, non-3rd person singular present VBD NNS VBN VB IN Verb, past tense Noun, plural Verb, past participle Verb, base form Preposition or subordinating conjunction VBZ Verb, 3rd person singular present VBG Verb, gerund or present participle MD PRP RBR CC Modal Possessive pronoun Adverb, comparative Coordinating conjunction JJR Adjective, comparative DT JJS Determiner Adjective, superlative

<!-- b000093 | furniture | pages [5] -->
Team # 2301192

<!-- b000094 | furniture | pages [5] -->
Page 5

<!-- b000095 | caption | pages [5] -->
Table 2: Notations of Word Attributes Used in the Paper

<!-- b000096 | heading | pages [5] -->
Symbols

<!-- b000097 | prose | pages [5] -->
Definition

<!-- b000098 | prose | pages [5] -->
Freq Word Frequency SLF the Sum of Letter Frequencies BU the Breadth of Usage of a Word NDLW the Number of Different Letters in a Word a-z the Number of Letters from a to z in a Word

<!-- b000099 | prose | pages [5] -->
3

<!-- b000100 | heading | pages [5] -->
Model 1-Integration of Interpretation and Prediction Model

<!-- b000101 | prose | pages [5] -->
based on Prophet and SIRS

<!-- b000102 | prose | pages [5] -->
3.1 Data Preprocessing and Exploratory Analysis

<!-- b000103 | prose | pages [5] -->
3.1.1

<!-- b000104 | heading | pages [5] -->
Data Collection and Pre-processing

<!-- b000105 | prose | pages [5] -->
In addressing task 1, it is dispensable to analyze the attributes of words related to the prob- lem and collect relevant data.The possible factors include the frequency, the breadth of the usage in different fields, the number of different letters in words and parts of speech. In general Nat- ural Language Processing (NLP), there are 36 commonly used parts of speech[2], of which we selected 18 types relevant to this task as shown in Table 1.

<!-- b000106 | prose | pages [5] -->
To process missing values, abnormal values and repeated observations in the original data set, we apply a series of data processing methods: data cleaning, establishment of dummy variables for discrete variables, logarithmic transformation of the number of reports and set-up of new attributes. The four steps enable the elimination of extraneous information and facilitate the identification and extraction of relevant information from the dataset.

<!-- b000107 | prose | pages [5] -->
Step 1: In the stage of data cleaning, we use Python to check for missing, outlier and du- plicate values. By measuring length of words, we check for empty or unusually long values. We find that there are no empty values but three outliers: ”tash”, ”clen” and ”rprobe”. After searching and comparing online, we correct those words as ”trash”, ”clean” and ”probe”. Fur- thermore, using the ”duplicate()” method, we check for duplicate values with no duplicate value found.

<!-- b000108 | prose | pages [5] -->
Step 2: To make the discrete variable of part-of-speech easier to be processed by the model, we construct 17 dummy variables to convert the discrete variable into binary variables.

<!-- b000109 | prose | pages [5] -->
Step 3: We plan to use a time series model to predict the number of reports on March 1, 2023. In these types of models, it is crucial to eliminate heteroscedasticity in the data. Taking the logarithm of the data does not change its nature or correlation, but it compresses the scale of the variable. By shrinking the absolute values of the data, it is easier to eliminate the problem of heteroscedasticity. Therefore, we logarithmically transform the reported quantity.

<!-- b000110 | prose | pages [5] -->
Step 4: To comprehensively explore the influence of various word attributes on reported Hard-Mode-played scores, we further extract the attributes of words and establish several new variables. This will be elaborated in Section 3.4.

<!-- b000111 | prose | pages [5] -->
3.1.2 Data Description and Exploratory Analysis

<!-- b000112 | prose | pages [5] -->
The data is visualized to dig into the inherent rules, which is helpful for modeling. Figure

<!-- b000113 | furniture | pages [6] -->
Team # 2301192

<!-- b000114 | furniture | pages [6] -->
Page 6

<!-- b000115 | prose | pages [6] -->
2 depicts the correlation between the variables, while Figure 3 presents the distribution of the number of attempts in a histogram. Figure 4 displays the changing curve of the total number of reports and the proportion of reports in difficult mode over time.

<!-- b000116 | caption | pages [6] -->
Figure 2: Correlation Matrix

<!-- b000117 | caption | pages [6] -->
Figure 3: Distribution Histogram

<!-- b000118 | prose | pages [6] -->
We can see that the correlation between variables is generally weak, and the distribution of the number of attempts shows a state of low at both ends and high in the middle. The trend of the quantity curve is somewhat similar to the infection curve, which will be analyzed in detail in the following steps.

<!-- b000119 | prose | pages [6] -->
3.2

<!-- b000120 | heading | pages [6] -->
Prophet Model

<!-- b000121 | prose | pages [6] -->
The Prophet algorithm provided by Facebook[3] can not only handle time series data with some outliers but also deal with partially missing values. It can almost automatically predict the future trends of time series. Based on time series decomposition and machine learning fitting, it uses the open-source tool pyStan to fit the model, so it can obtain the predicted results quickly.

<!-- b000122 | prose | pages [6] -->
After performing a logarithmic transformation on the data(elaborated in Section 3.1.1), we use Prophet to establish a multiplication model with the parameters listed in Table 3, where τ is a

<!-- b000123 | furniture | pages [7] -->
Team # 2301192

<!-- b000124 | furniture | pages [7] -->
Page 7

<!-- b000125 | caption | pages [7] -->
Figure 4: Quantity Curve

<!-- b000126 | prose | pages [7] -->
parameter that controls the slope of the linear function at the breakpoint.For the rate of change at a changepoint, denoted as ∆, it follows that ∆∼Laplace(0, τ). As τ decreases, ∆approaches 0. Therefore, increasing τ will broaden the upper and lower limits of the predicted values. The trend term uses the default piecewise linear function. Setting more changepoints and increasing the range of breakpoints makes the model more sensitive to changes in time series data, which improves the fitting effect.

<!-- b000127 | caption | pages [7] -->
Table 3: Prophet Model Parameter Setting

<!-- b000128 | prose | pages [7] -->
the Number of Changepoints τ the Range of Changepoints

<!-- b000129 | prose | pages [7] -->
Holidays

<!-- b000130 | prose | pages [7] -->
60 0.8 0.9

<!-- b000131 | prose | pages [7] -->
Valentine 2022/02/14 Easter 2022/04/24 Halloween 2022/10/31 Thanksgiving 2022/11/24 Christmas 2022/12/25

<!-- b000132 | prose | pages [7] -->
A Prophet model typically consists of a trend term g(t), a seasonal term s(t), a holiday effect term h(t) and an residual term ε(t). g(t) is a piecewise linear function that satisfies:

<!-- b000133 | prose | pages [7] -->
g(t) = (k + a(t)∆)t + (m + a(t)⊺γ) (1)

<!-- b000134 | prose | pages [7] -->
where k represents the growth rate, ∆represents the change in growth rate, and m represents the offset parameter. s(t) contains the weekly periodic changes:

<!-- b000135 | prose | pages [7] -->
2πnt

<!-- b000136 | prose | pages [7] -->


<!-- b000137 | prose | pages [7] -->
N X

<!-- b000138 | prose | pages [7] -->
an cos

<!-- b000139 | prose | pages [7] -->
s(t) =

<!-- b000140 | prose | pages [7] -->
n=1

<!-- b000141 | prose | pages [7] -->


<!-- b000142 | prose | pages [7] -->
2πnt

<!-- b000143 | prose | pages [7] -->


<!-- b000144 | prose | pages [7] -->
+ bn sin

<!-- b000145 | prose | pages [7] -->
(2)

<!-- b000146 | prose | pages [7] -->
P P

<!-- b000147 | prose | pages [7] -->
P

<!-- b000148 | prose | pages [7] -->
where P is the period time, and (an, bn) , (n = 1 . . . N) follow a normal distribution. h(t) illustrates the potential impact of holidays on the outcome:

<!-- b000149 | prose | pages [7] -->
L X

<!-- b000150 | prose | pages [7] -->
h(t) =

<!-- b000151 | prose | pages [7] -->
i=1

<!-- b000152 | prose | pages [7] -->
ki ∗l{t∈Di} (3)

<!-- b000153 | furniture | pages [8] -->
Team # 2301192

<!-- b000154 | furniture | pages [8] -->
Page 8

<!-- b000155 | prose | pages [8] -->
where ki, i = 1 . . . L follow a normal distribution. Based on the parameters and functions above, a multiplicative model is established:

<!-- b000156 | prose | pages [8] -->
y(t) = g(t) ∗s(t) ∗h(t) ∗ε(t) (4)

<!-- b000157 | prose | pages [8] -->
We use the data from 2022-01-07 to 2022-11-21 as the training set and the data from 2022- 11-21 to 2022-12-31 as the test set. The fitting result is shown in Figure 5, where the red vertical line represents the breakpoint we set.

<!-- b000158 | caption | pages [8] -->
Figure 5: Prophet Forecasting

<!-- b000159 | prose | pages [8] -->
We evaluate the effectiveness of the model using four metrics: R-squared, MSE, RMSE, and MAPE, which are as follows:

<!-- b000160 | prose | pages [8] -->
n X

<!-- b000161 | prose | pages [8] -->
MSE = 1

<!-- b000162 | prose | pages [8] -->
n

<!-- b000163 | prose | pages [8] -->
i=1

<!-- b000164 | prose | pages [8] -->
v u u t1

<!-- b000165 | prose | pages [8] -->
RMSE =

<!-- b000166 | prose | pages [8] -->
Pn

<!-- b000167 | prose | pages [8] -->
(yi −byi)2

<!-- b000168 | prose | pages [8] -->
n X

<!-- b000169 | prose | pages [8] -->
(yi −byi)2

<!-- b000170 | prose | pages [8] -->
n n

<!-- b000171 | prose | pages [8] -->
i=1

<!-- b000172 | prose | pages [8] -->
(5)

<!-- b000173 | prose | pages [8] -->
i=1 (yi −byi)2

<!-- b000174 | prose | pages [8] -->
R2 = 1 −

<!-- b000175 | prose | pages [8] -->
Pn

<!-- b000176 | prose | pages [8] -->
i=1 (yi −¯y)2

<!-- b000177 | furniture | pages [8] -->


<!-- b000178 | furniture | pages [8] -->


<!-- b000179 | prose | pages [8] -->
n X

<!-- b000180 | prose | pages [8] -->
byi −yi

<!-- b000181 | prose | pages [8] -->
MAPE = 100%

<!-- b000182 | prose | pages [8] -->
n n

<!-- b000183 | prose | pages [8] -->
yi

<!-- b000184 | prose | pages [8] -->
i=1

<!-- b000185 | prose | pages [8] -->
where ˆyi represents the fitted value and yi represents the actual value.The results are shown in

<!-- b000186 | caption | pages [8] -->
Table 4. The R-squared value is close to 1, indicating an excellent fit of the model. As our final

<!-- b000187 | prose | pages [8] -->
results are obtained by taking the exponential of the log-transformed data, the small RMSE and MSE can be considered. The MAPE of 4.8% indicates a small average absolute percentage error. Overall, the established model is suitable for prediction.

<!-- b000188 | prose | pages [8] -->
Based on the data above, we reduce τ to increase the precision of the prediction interval. We then reestablish the model and predict that the number of reported results on March 1, 2023

<!-- b000189 | furniture | pages [9] -->
Team # 2301192

<!-- b000190 | furniture | pages [9] -->
Page 9

<!-- b000191 | caption | pages [9] -->
Table 4: Evaluation of the Prophet

<!-- b000192 | prose | pages [9] -->
R-squared MSE RMSE MAPE 0.9924 60340502 7767.9149 4.8002

<!-- b000193 | prose | pages [9] -->
is 14534, with a prediction interval of (13175, 16128)(95% confidence level). These prediction results indicate that the popularity of Wordle is decreasing over time.

<!-- b000194 | prose | pages [9] -->
3.3 Explanation of the Changes in the Number of Reports

<!-- b000195 | prose | pages [9] -->
The changes in the number of reports can be decomposed into trend, seasonal, and holiday components as shown in Figure 6. We will explain the changes in report numbers from these three aspects.

<!-- b000196 | caption | pages [9] -->
Figure 6: Time Series Decomposition Plot

<!-- b000197 | prose | pages [9] -->
Seasonal and Holiday Effects:

<!-- b000198 | prose | pages [9] -->
Holidays cause a decrease in the number of reports, such as a slight dip in the number of reports around Valentine’s Day as seen in the linear trend chart. In the weekly effect, the number of reports increases from Sunday to Wednesday and decreases from Wednesday to Saturday (with a rebound on Friday). This suggests that people tend to play Wordle as a pastime on workdays, and have less interest on holidays.

<!-- b000199 | furniture | pages [10] -->
Team # 2301192

<!-- b000200 | furniture | pages [10] -->
Page 10

<!-- b000201 | prose | pages [10] -->
Explanation of Overall Variation:

<!-- b000202 | prose | pages [10] -->
The SIRS infectious disease model can explain changes in the trend component well. Our assumptions are as follows:

<!-- b000203 | heading | pages [10] -->
Assumption 1: All Twitter users A(t) can be divided into three groups:

<!-- b000204 | prose | pages [10] -->
(1) Ordinary Twitter users S(t). They may be influenced by seeing some Wordle player’s score reports on Twitter and may be motivated to become Wordle players. They correspond to ”susceptible individuals”;

<!-- b000205 | prose | pages [10] -->
(2) Wordle players I(t). Some players will post reports on Twitter, which will attract others to become Wordle players. They correspond to ”infected individuals”;

<!-- b000206 | prose | pages [10] -->
(3) Tired players R(t). They will not play Wordle for a period of time, but may start playing again after this time. They correspond to ”recovered individuals”.

<!-- b000207 | prose | pages [10] -->
Assumption 2: Ordinary players S may have a probability of λ of being infected; in players I, they have a probability of β of getting tired of playing Wordle and not playing for a period of time; in tired players R, there is a probability of η of being influenced by external factors and starting to play Wordle again. Ordinary players S, players I, and tired players R may all have a probability of natural removal of a certain θ.

<!-- b000208 | caption | pages [10] -->
Figure 7: Player State Transitions

<!-- b000209 | prose | pages [10] -->
Based on the above assumptions, after setting the parameters, the number of players can be fitted by solving the differential equations, and then multiplied by a certain proportion to calculate the number of score reports on Twitter. The corresponding fitting curve of the report quantity is shown in Figure 8, which conforms to the trend curve of Prophet. Therefore, the SIRS model can be used to explain the overall trend of the change. Wordle became popular from January 2022, and the number of players reached its peak around February (the number of reports also reached its peak). After that, the game gradually cooled down, the number of players decreased, and the number of reports also decreased.

<!-- b000210 | prose | pages [10] -->
3.4 Extracting the Attributes of Words

<!-- b000211 | prose | pages [10] -->
To investigate the impact of the attributes of words on the proportion of reports of challeng- ing patterns, we first need to extract various useful properties of words.

<!-- b000212 | heading | pages [10] -->
1. the Number of Different Letters in a Word(NDLW)

<!-- b000213 | prose | pages [10] -->
In general, the fewer different letters a word has, the lower the probability of guessing a letter in the trial, and the more difficult the puzzle becomes. We count the distribution of words with different numbers of letters and the average proportion of people who made 5+ tries, and the results are shown in Table 5. As can be seen from the table, the fewer

<!-- b000214 | furniture | pages [11] -->
Team # 2301192

<!-- b000215 | furniture | pages [11] -->
Page 11

<!-- b000216 | caption | pages [11] -->
Figure 8: Fitted Curve of the SIRS

<!-- b000217 | prose | pages [11] -->
different letters a word has, the higher the proportion of people who made 5+ tries, in- dicating that the puzzle is more difficult. Therefore, the number of different letters in a word is an important attribute of the word.

<!-- b000218 | caption | pages [11] -->
Table 5: Varieties of Letters in Words and Proportion of 5+ Tries

<!-- b000219 | prose | pages [11] -->
Number of Words Different Letters 3 6 4 94 5 259 Proportion of 5+ Tries 62.50% 45.10% 34.90%

<!-- b000220 | heading | pages [11] -->
2. the Frequency of Word Usage in Daily Life(Freq)

<!-- b000221 | prose | pages [11] -->
In general, the more frequently a word is used in daily life, the more familiar people are with it, and vice versa. The more unfamiliar a word in a puzzle is, the more difficult the puzzle becomes. Therefore, the frequency of word usage in daily life is also an essential attribute. We use the word frequency data from Wolfram[4], which is calculated from the Google Books dataset.

<!-- b000222 | heading | pages [11] -->
3. the Breadth of Word Usage in Different Fields(BU)

<!-- b000223 | prose | pages [11] -->
The more widespread the usage of a word, the more people are familiar with it, and vice versa. The less familiar people are with the words in a puzzle, the more difficult the puzzle becomes. The prevalence of a word is defined as the number of corpora in which the word appears among 100 corpora (data from ”Word Frequencies in Written and Spoken English”).

<!-- b000224 | heading | pages [11] -->
4. the Sum of Letter Usage Frequency(SLF)

<!-- b000225 | prose | pages [11] -->
When playing the Wordle game, players usually try words that contain more common letters to gain more information. Therefore, whether the letters in a word are common or not is also an important attribute to measure the difficulty of a word. We define the SLF to describe this attribute of a word:

<!-- b000226 | prose | pages [11] -->
SLF =

<!-- b000227 | prose | pages [11] -->
5 X

<!-- b000228 | prose | pages [11] -->
(6) frequencyi

<!-- b000229 | prose | pages [11] -->
i=1

<!-- b000230 | furniture | pages [12] -->
Team # 2301192

<!-- b000231 | furniture | pages [12] -->
Page 12

<!-- b000232 | prose | pages [12] -->
where frequencyi represents the frequency of the ith letter in the word. The letter- frequency data is obtained from the website Algoritmy[1].

<!-- b000233 | heading | pages [12] -->
5. the Sum of a Letter in a Word

<!-- b000234 | prose | pages [12] -->
The sum of a letter in a word is also an attribute of the word, as the puzzles consist of five letters that can be the same or different.

<!-- b000235 | heading | pages [12] -->
6. Part-of-Speech of a Word

<!-- b000236 | prose | pages [12] -->
The part-of-speech of a word is one of the most common attributes of a word.

<!-- b000237 | prose | pages [12] -->
Impact of Word Attributes on the Proportion of Hard-Mode Reports 3.5

<!-- b000238 | prose | pages [12] -->
The proportion of reports in the hard mode is defined as follows:

<!-- b000239 | prose | pages [12] -->
percentagehard = numberhard

<!-- b000240 | prose | pages [12] -->
(7)

<!-- b000241 | prose | pages [12] -->
numberreported

<!-- b000242 | prose | pages [12] -->
We establish a multiple linear regression model based on the least squares method and use the significance test of the regression equation (i.e., F-test) to study whether word attributes have an impact on the proportion of Hard-Mode reports.

<!-- b000243 | prose | pages [12] -->
3.5.1

<!-- b000244 | heading | pages [12] -->
Model Establishment

<!-- b000245 | prose | pages [12] -->
Multiple linear regression describes the relationship of the dependent variable y with inde- pendent variables x1, x2, . . . , xm by the following equation:

<!-- b000246 | prose | pages [12] -->
ˆy = β0 + β1x1 + β2x2 + · · · + βmxm + ε (8)

<!-- b000247 | prose | pages [12] -->
where β0 is the constant term, βk is the regression coefficient of the kth independent vari- able, and ε is the random error term.We perform a multiple linear regression with Freq, SLF, NDLW,BU, the Sum of a Letter in a Word, Part-of-Speech of a Word as independent variables, and percentagehard as the dependent variable. Due to the length of the obtained regression equation, it is included in Appendix A.

<!-- b000248 | prose | pages [12] -->
Significance Test of Regression Equation 3.5.2

<!-- b000249 | heading | pages [12] -->
1. Hypothesis Formulation:

<!-- b000250 | prose | pages [12] -->
Null hypothesis: H0 : β0 = β1 = · · · βm = 0;

<!-- b000251 | prose | pages [12] -->
Alternative hypothesis: H1 : β0, β1, · · · , βm are not all equal to 0.

<!-- b000252 | heading | pages [12] -->
2. Calculate F-statistic:

<!-- b000253 | prose | pages [12] -->
SSR/m SSE/(n −m −1) ∼F(m, n −m −1) F =

<!-- b000254 | prose | pages [12] -->
where SSR = Pn

<!-- b000255 | prose | pages [12] -->
(9)

<!-- b000256 | prose | pages [12] -->
i=1(ˆyi −¯y)2 represents the regression sum of squares, and SSE = P i = 1n(yi −ˆyi)2 represents the residual sum of squares.

<!-- b000257 | furniture | pages [13] -->
Team # 2301192

<!-- b000258 | furniture | pages [13] -->
Page 13

<!-- b000259 | heading | pages [13] -->
3. Making Decisions The rejection region of the test is F > Fα(m, n −m −1), based on

<!-- b000260 | prose | pages [13] -->
the given significance level of α = 0.05. We establish a multiple linear regression model with word attributes as independent variables and the proportion of reports in hard mode as the dependent variable.

<!-- b000261 | prose | pages [13] -->
The F-statistic of the regression equation is 1.058 with a corresponding P-value of 0.379 (> α = 0.05), indicating that the regression equation does not exhibit statistical significance. Therefore, we conclude that word attributes do not have a significant impact on the proportion of reports in hard mode.

<!-- b000262 | prose | pages [13] -->
4

<!-- b000263 | heading | pages [13] -->
Model 2-Distribution Prediction Model based on BP Neu-

<!-- b000264 | prose | pages [13] -->
ral Network

<!-- b000265 | prose | pages [13] -->
4.1

<!-- b000266 | heading | pages [13] -->
Model Building of BP

<!-- b000267 | prose | pages [13] -->
We first preprocess the data by combining pretraining with Global Vectors model (GloVe) and dimensionality reduction with PCA.Word embedding is a technique that maps words to real-valued vectors and is a fundamental application in natural language processing. GloVe model is one of the word embedding models, which adopts squared loss and fits the word vectors to the global statistical information calculated based on the entire dataset. We use pre-trained word vectors from the GloVe model as features.

<!-- b000268 | caption | pages [13] -->
Figure 9: Implementation Process

<!-- b000269 | prose | pages [13] -->
In addressing task 2, we use the word properties obtained from the first sub-question as part of the features, normalize them, and extract the principal components using PCA. We combine the extracted principal components with the word vectors pre-trained using the GloVe model and use them as the input features for the BP neural network. In the BP neural network, we input the word features and use the percentage distribution of each word as the label. We select 80% of the data as the training set and 20% as the test set to train the neural network and test its

<!-- b000270 | furniture | pages [14] -->
Team # 2301192

<!-- b000271 | furniture | pages [14] -->
Page 14

<!-- b000272 | prose | pages [14] -->
performance. Since the amount of data given is small, we choose to establish a low-complexity network, which includes an input layer, a single hidden layer, and an output layer. The hidden layer contains 1024 hidden units, and the ReLU function is used as the activation function. Dropout is applied during training to drop 50% of the network units to counter overfitting. The L2-norm is selected as the loss function, the Adam optimizer is used for gradient optimization during backpropagation, and the learning rate is set to 0.05. Xavier random initialization is used.

<!-- b000273 | prose | pages [14] -->
4.2

<!-- b000274 | heading | pages [14] -->
Model Uncertainty of BP

<!-- b000275 | prose | pages [14] -->
Neural networks have considerable randomness, and the initialization parameters in the Xavier method of the neural network are sampled from a uniform distribution. Additionally, dropout randomly drops neurons in the hidden layer. This means that the training results of the neural network may vary each time. To address this issue, we try to train the model multiple times and select the best model.

<!-- b000276 | prose | pages [14] -->
The model output may be negative, and to address this issue, we choose to adjust the negative values to 0.

<!-- b000277 | prose | pages [14] -->
Since the output values cannot be directly used as percentages, as their sum may exceed or be less than 100, we divide each output by the total sum to obtain the final predicted percentages.

<!-- b000278 | prose | pages [14] -->
4.3

<!-- b000279 | heading | pages [14] -->
Model Evaluation of BP

<!-- b000280 | prose | pages [14] -->
The evaluation results on the test set are as follows:

<!-- b000281 | caption | pages [14] -->
Table 6: Evaluation on Test Set

<!-- b000282 | prose | pages [14] -->
MAE MSE MAPE 3.2302 21.857 32.9194

<!-- b000283 | prose | pages [14] -->
On the test set, the mean absolute error (MAE) of the neural network is around 4, indicat- ing that the average absolute difference between predicted values and true values is 4, which indicates a high accuracy of the model. Other metrics also support this conclusion.

<!-- b000284 | prose | pages [14] -->
4.4

<!-- b000285 | heading | pages [14] -->
Model Prediction of BP

<!-- b000286 | prose | pages [14] -->
We predict the distribution of people trying different times and the result is as follows. We are confident that the error is within 3%.

<!-- b000287 | prose | pages [14] -->
5

<!-- b000288 | heading | pages [14] -->
Model 3-Diﬀiculty Classification based on K-Means++

<!-- b000289 | prose | pages [14] -->
5.1 Clustering Analysis based on K-Means++.

<!-- b000290 | prose | pages [14] -->
The K-Means algorithm is an unsupervised learning method and a clustering algorithm based on partitioning. It usually uses Euclidean distance as the metric to measure the simi- larity between data objects, and the similarity is inversely proportional to the distance between data objects. The larger the similarity, the smaller the distance. The algorithm requires a pre- determined initial number of clusters k and k initial cluster centers. Based on the similarity between the data object and the cluster center, the algorithm continuously updates the position of the cluster center and reduces the sum of squared errors (SSE) of the clusters. When SSE no

<!-- b000291 | furniture | pages [15] -->
Team # 2301192

<!-- b000292 | prose | pages [15] -->
Try Times Percentage(%) 1 0 2 6 3 18 4 29 5 27 6 15 7+ 5

<!-- b000293 | caption | pages [15] -->
Table 7: Predicted Result of ”EERIE”

<!-- b000294 | furniture | pages [15] -->
Page 15

<!-- b000295 | prose | pages [15] -->
1 try

<!-- b000296 | prose | pages [15] -->
23

<!-- b000297 | prose | pages [15] -->
2 tries

<!-- b000298 | prose | pages [15] -->
12

<!-- b000299 | prose | pages [15] -->
3 tries 4 tries

<!-- b000300 | prose | pages [15] -->
4

<!-- b000301 | prose | pages [15] -->
0

<!-- b000302 | prose | pages [15] -->
5 tries

<!-- b000303 | prose | pages [15] -->
6

<!-- b000304 | prose | pages [15] -->
32

<!-- b000305 | prose | pages [15] -->
6 tries 7+ tries

<!-- b000306 | prose | pages [15] -->
22

<!-- b000307 | caption | pages [15] -->
Figure 10: Predicted Result of ”EERIE”

<!-- b000308 | prose | pages [15] -->
longer changes or the objective function converges, the clustering ends, and the final result is obtained.

<!-- b000309 | prose | pages [15] -->
The categories ”1 try”, ”2 tries”, up to ”7+ tries” well reflect the difficulty of the puzzles. We use these variables as inputs and employ the K-Means++ algorithm to classify the difficulty of the words. The specific process is as follows:

<!-- b000310 | prose | pages [15] -->
Step 1:Determine the number of clusters k and initialize k cluster centers.

<!-- b000311 | prose | pages [15] -->
Step 2:Calculate the Euclidean distance between the data points and the k initial cluster centers, and cluster partition based on the minimum distance, resulting in k regions.

<!-- b000312 | prose | pages [15] -->
Step 3:Calculate the center position of each cluster obtained in the previous step and use it as the next iteration’s cluster center.

<!-- b000313 | prose | pages [15] -->
Step 4:Repeat the above steps until the change between the last two clustering results meets the accuracy requirements.

<!-- b000314 | prose | pages [15] -->
The elbow rule chart in Figure 11 is used along with our experience in differentiating game difficulty to determine the number of clusters. We choose the number of clusters to be k=3, representing three levels of difficulty: hard, medium, and easy.

<!-- b000315 | prose | pages [15] -->
Finally, we obtain the clustering results, which show that cluster 1 contains 135 words, clus- ter 2 contains 156 words, and cluster 3 contains 68 words. The statistical results of the mean and standard deviation of each property in the clusters are shown in Table 8. By calculating the average proportion of tries with 5+ tries in each cluster, we obtain Table 9. By observing Table 8 and Table 9, we categorize the words in Cluster 1, Cluster 2, and Cluster 3 as easy, medium, and hard, respectively.

<!-- b000316 | prose | pages [15] -->
Relationship between Word Attributes and Diﬀiculty Levels 5.2

<!-- b000317 | prose | pages [15] -->
Relationship Between Diﬀiculty Levels and NDLW 5.2.1

<!-- b000318 | prose | pages [15] -->
The distribution of word difficulty levels for words with different NDLW is shown in Figure 12, and the proportion of NDLW of different difficulty levels is shown in Table 10. We found that the proportion of words with fewer different letters increases with increasing difficulty level. In the dataset provided for this study, there are six words that have only three different letters.

<!-- b000319 | furniture | pages [16] -->
Team # 2301192

<!-- b000320 | furniture | pages [16] -->
Page 16

<!-- b000321 | caption | pages [16] -->
Figure 11: K-value Optimization

<!-- b000322 | caption | pages [16] -->
Table 8: Results and Significance Tests of K-means Clusters for Different Categories

<!-- b000323 | prose | pages [16] -->
Cluster Categories (means ± sd) 1 (n=135) 2 (n=156) 3 (n=68) F-value P-value

<!-- b000324 | prose | pages [16] -->
0.269 ± 0.459 0.8 ± 1.057 1 try 0.279 ± 0.452 0.000*** 21.307 4.013 ± 1.749 9.459 ± 4.168 2 tries 2.868 ± 1.962 0.000*** 168.146 20.212 ± 3.516 30.748 ± 3.81 3 tries 12.574 ± 4.108 0.000*** 594.862 35.487 ± 3.819 33.637 ± 3.824 4 tries 25.647 ± 4.485 0.000*** 150.08 26.436 ± 3.115 17.807 ± 3.159 5 tries 28.794 ± 5.732 0.000*** 268.933 11.596 ± 3.05 6.43 ± 2.261 6 tries 21.662 ± 4.188 0.000*** 565.646 1.974 ± 1.169 1.081 ± 0.931 7+ tries (X) 8.132 ± 7.035 0.000*** 119.123

<!-- b000325 | caption | pages [16] -->
Table 9: Average Proportion of 5+ tries for Different Categories

<!-- b000326 | prose | pages [16] -->
Average Proportion of 5+ tries Cluster categories

<!-- b000327 | prose | pages [16] -->
Cluster 1 Cluster 2 Cluster 3 25.35% 39.92% 58.59%

<!-- b000328 | caption | pages [16] -->
Table 10: Proportion of NDLW Across Difficulty Levels

<!-- b000329 | prose | pages [16] -->
Cluster Categories Proportion of NDLW

<!-- b000330 | prose | pages [16] -->
5 5 4 3

<!-- b000331 | prose | pages [16] -->
90.78% Easy 9.22% 0% 63.13% Medium 35.63% 1.24% 52.94% Hard 41.18% 5.88%

<!-- b000332 | furniture | pages [17] -->
Team # 2301192

<!-- b000333 | furniture | pages [17] -->
Page 17

<!-- b000334 | caption | pages [17] -->
Figure 12: Relationship between Difficulty Levels and NDLW

<!-- b000335 | prose | pages [17] -->
Two of them are classified as medium difficulty, namely ”motto” and ”madam”, while the other four are classified as difficult, namely ”fluff”, ”mummy”, ”cacao”, and ”vivid”. Based on the above analysis, we have sufficient evidence to suggest that the fewer different letters a word contains, the more diﬀicult it is to guess.

<!-- b000336 | prose | pages [17] -->
5.2.2 Relationship between Diﬀiculty Levels and SLF

<!-- b000337 | caption | pages [17] -->
Figure 13: Relationship between Difficulty Levels and NDLW

<!-- b000338 | prose | pages [17] -->
The distribution of the SLF for words of different difficulty levels is shown in Figure 13 and

<!-- b000339 | caption | pages [17] -->
Table 11. We focus mainly on the part where the SLF is less than 0.2 and greater than 0.4 because

<!-- b000340 | prose | pages [17] -->
it represents the relationship between the difficulty level and the majority of letter frequency sum. It can be observed that as the difficulty level increases, the proportion of whose SLF less than 0.2 will increase, while the proportion of whose SLF greater than 0.4 will decrease. This means that the more commonly used letters in a word, the easier it is to be guessed, and vice versa.

<!-- b000341 | prose | pages [17] -->
5.2.3 Relationship between Diﬀiculty Levels and BU and Freq

<!-- b000342 | caption | pages [17] -->
Table 12 shows the distribution of word breadth for different levels of difficulty. The breadth

<!-- b000343 | prose | pages [17] -->
of a word is defined as the number of corpora in which the word appears out of a total of 100

<!-- b000344 | furniture | pages [18] -->
Team # 2301192

<!-- b000345 | furniture | pages [18] -->
Page 18

<!-- b000346 | caption | pages [18] -->
Table 11: Distribution of the SLF Across Difficulty Levels

<!-- b000347 | prose | pages [18] -->
Cluster Categories Proportion of SLF

<!-- b000348 | prose | pages [18] -->
< 0.2 0.2-0.4 > 0.4

<!-- b000349 | prose | pages [18] -->
2.84% Easy Medium 86.52% 10.64% 10% 85.63% 4.37% 13.24% Hard 85.29% 1.47%

<!-- b000350 | prose | pages [18] -->
corpora, and it takes integer values between 0 and 100. The table indicates that the more widely a word is used in different fields, the easier the corresponding puzzle, and vice versa.

<!-- b000351 | prose | pages [18] -->
At the same time, we attempt to find a relationship between the difficulty level of a word and its frequency of use in everyday life. Although there is a difference in the mean frequency of different levels of difficulty, the mean value is sensitive to outliers. Therefore, we first sort the words by frequency and then use a histogram to show their distribution, as shown in Figure 14. Ultimately, we find that there is no significant relationship between the diﬀiculty level and the frequency of use in everyday life, as the distribution of word frequencies for different levels of diﬀiculty is fairly uniform.

<!-- b000352 | caption | pages [18] -->
Table 12: Distribution of BU Across Difficulty Levels

<!-- b000353 | prose | pages [18] -->
Cluster Categories

<!-- b000354 | prose | pages [18] -->
0-33.33

<!-- b000355 | prose | pages [18] -->
Easy 9.93% Medium 19.38% Hard 22.06%

<!-- b000356 | prose | pages [18] -->
BU

<!-- b000357 | prose | pages [18] -->
33.33-66.66 66.66-100

<!-- b000358 | prose | pages [18] -->
12.77% 77.30% 21.87% 58.75% 26.47% 51.47%

<!-- b000359 | caption | pages [18] -->
Figure 14: Relationship between Difficulty Levels and Freq

<!-- b000360 | heading | pages [18] -->
PCA Discussion on the Accuracy of Model Classification

<!-- b000361 | prose | pages [18] -->
5.3

<!-- b000362 | prose | pages [18] -->
The discussion of model classification accuracy can be divided into two parts. The first part is whether there is a significant difficulty difference among the words in each cluster, and the second part is the effectiveness of K-Means clustering. As mentioned earlier, in the first part,

<!-- b000363 | furniture | pages [19] -->
Team # 2301192

<!-- b000364 | furniture | pages [19] -->
Page 19

<!-- b000365 | prose | pages [19] -->
the average proportion of tries with 5+ tries for each cluster’s words is 25.35%, 39.92%, and 58.59%, respectively, which shows a significant difficulty difference among the clusters.

<!-- b000366 | prose | pages [19] -->
Regarding the second part, we conduct principal component analysis (PCA) on seven fea- tures, including ”1 try”, ”2 tries” to ”7+ tries”. We find that the variance explained by the first two principal components reaches 82.88% (> 80%). Therefore, we take the first two principal components to create a scatter plot, as shown in Figure 15. From this scatter plot, it is evident that the words are well differentiated, and the K-Means clustering effect is good.

<!-- b000367 | caption | pages [19] -->
Figure 15: PCA on the Accuracy of Model Classification

<!-- b000368 | prose | pages [19] -->
From the perspective of evaluation metrics, we compared K-Means++ with other clustering methods like the Partitioning Around Medoids(PAM) and the Gaussian Mixture Model(GMM) and the results are shown in Table 13. From the comparison results, it can be seen that K- Means++ has a better clustering effect.

<!-- b000369 | caption | pages [19] -->
Table 13: Model Evaluation

<!-- b000370 | prose | pages [19] -->
Silhouette Coefficient Model CH Score

<!-- b000371 | prose | pages [19] -->
0.372 K-Means++ 309.326 0.347 PAM 303.049 0.347 GMM 291.637

<!-- b000372 | prose | pages [19] -->
Determining the Diﬀiculty Level of ”EERIE” 5.4

<!-- b000373 | prose | pages [19] -->
According to the results of the second question, we obtain the distribution of EERIE’s rel- evant percentages (1, 2, 3, 4, 5, 6, X), which is [0, 6, 18, 29, 27, 15, 5]. By inputting this distribution into our model, we determine that the difficulty level of ”EERIE” is ”medium”.

<!-- b000374 | furniture | pages [20] -->
Team # 2301192

<!-- b000375 | prose | pages [20] -->
6 Interesting Surprise

<!-- b000376 | furniture | pages [20] -->
Page 20

<!-- b000377 | prose | pages [20] -->
Are These Words Really that Diﬀicult? 6.1

<!-- b000378 | prose | pages [20] -->
After categorizing words by their difficulty levels, we find that the difficulty level of the word ”mummy” is ”difficult”. When we calculate the proportion of words that have been attempted ”5 times or more” and sort them in descending order, we are surprised to find that ”mummy” is ranked second in difficulty, with 82% of people attempting it five or more times. As we have been familiar with the word ”mummy” since childhood, we subjectively thought it was an easy word, making the opposite result all the more surprising. Additionally, other similar words include ”watch”, ”catch”, ”prize”, etc. In fact, this confirms our view that ”there is no significant relationship between word frequency and difficulty level.”

<!-- b000379 | prose | pages [20] -->
Which Initial Letter Poses the Greatest Challenge for Solution Words? 6.2

<!-- b000380 | prose | pages [20] -->
We use hypothesis testing to identify which initial letter makes for the most difficult word puzzles. Firstly, we tally the frequency of each initial letter among all the words. Next, we define the difficulty coefficient of a word as the sum of the ”5 tries”, ”6 tries”, and ”7 or more tries (X)” categories, and calculate the difficulty coefficient of all the words. After sorting the difficulty coefficients and selecting the top 20% most difficult words, we tally the initial letters of these words. We then calculate the probability of each letter being the initial letter of a word that enters the top 20% most difficult list. Some of the results are shown in Table 14.

<!-- b000381 | prose | pages [20] -->
Assuming that the probability of a word starting with a certain letter entering the top 20% most difficult list is 0.2, that is

<!-- b000382 | prose | pages [20] -->
H0 :

<!-- b000383 | prose | pages [20] -->
(10) p = 0.2

<!-- b000384 | prose | pages [20] -->
Let n be the total number of times the letter appears as the first letter and k be the number of times the letter appears as the first letter in a word that enters the top 20% most difficult list. Then we have

<!-- b000385 | prose | pages [20] -->
k ∼B(n, 0.2) (11)

<!-- b000386 | prose | pages [20] -->
Since both n and k are known, we can calculate the probability P of this situation occurring. Taking the significance level α as 0.05, when P < α = 0.05, we reject the null hypothesis and believe that p is not equal to 0.2. We have calculated the P values for all the letters and sorted them in ascending order. Some of the results are shown in Table 15.

<!-- b000387 | prose | pages [20] -->
According to Table 15, for the letters e, s, f, w, and a, their corresponding P values are less

<!-- b000388 | caption | pages [20] -->
Table 14: the Relationship of First Letters and Difficulty

<!-- b000389 | prose | pages [20] -->
the First Letter Total Hard(20%) a 28 2 b 20 4 c 33 7 d 12 4 e 10 6 f 22 8 g 17 5 h 11 4 · · · · · · · · · Easy(20%) Hard Rate Easy Rate 5 0.071 0.179 3 0.200 0.150 10 0.212 0.303 5 0.333 0.418 0 0.600 0.000 2 0.364 0.091 1 0.294 0.059 2 0.364 0.182 · · · · · · · · ·

<!-- b000390 | furniture | pages [21] -->
Team # 2301192

<!-- b000391 | furniture | pages [21] -->
Page 21

<!-- b000392 | caption | pages [21] -->
Table 15: Statistics of Initial Letters of Difficult Words

<!-- b000393 | prose | pages [21] -->
Hard(20%) the First Letter Total e 10 s 51 f 22 w 11 a 28 r 13 t 30 · · · · · · Hard rate P value 6 0.6 0.006 4 0.078 0.011 8 0.364 0.036 5 0.455 0.039 2 0.071 0.046 0 0 0.055 3 0.1 0.079 · · · · · · · · ·

<!-- b000394 | prose | pages [21] -->
than 0.05, so p̸ = 0.2 is significant. The Hard rates of words with initial letters e, f, and w are greater than 0.2. Therefore, we have sufficient reason to believe that words with initial letters e, f, and w are difficult, with words starting with e being the most difficult. Likewise, we can find that the letter t corresponds to the easiest words when used as the first letter. Specific data can be found in Table 16.

<!-- b000395 | caption | pages [21] -->
Table 16: Statistics of Initial Letters of Easy Words

<!-- b000396 | prose | pages [21] -->
Easy(20%) The first letter Total t 30 d 12 c 33 s 51 · · · · · · Easy rate P value 16 0.533 0 5 0.417 0.053 10 0.303 0.056 13 0.255 0.081 · · · · · · · · ·

<!-- b000397 | prose | pages [21] -->
What Words Can Make Wordle Continue to be Popular? 6.3

<!-- b000398 | prose | pages [21] -->
An upward mutation point indicates a sudden increase in a trend that was supposed to de- cline. This may mean that the word corresponding to the upward mutation point is more likely to stimulate communication and spread among people, which led to an increase in the number of reports on that day. To detect upward mutation points, we first used the Isolation Forest al- gorithm to detect all mutation points, and then used the positivity or negativity of the first-order difference to search for upward mutation points. At the same time, we calculated the mutation rate and selected mutation points with a mutation rate greater than 5% as the final points. The results are shown in the table below.

<!-- b000399 | prose | pages [21] -->
Date Word Date 2022/2/8 frame 2022/3/18 2022/2/15 aroma 2022/3/21 2022/2/17 shake 2022/3/24 2022/2/19 swill 2022/3/27 2022/2/22 thorn 2022/3/30 2022/3/2 nasty 2022/4/1 2022/3/5 brine 2022/4/2 2022/3/11 watch 2022/4/8 2022/3/15 tease 2022/4/13 Word Date Word saute 2022/4/18 flair their 2022/4/22 plant chest 2022/4/26 heist nymph 2022/4/29 tarsh stove 2022/5/2 story snout 2022/5/4 train trope 2022/5/9 shine scare 2022/5/11 farce chunk 2022/12/26 judge

<!-- b000400 | furniture | pages [22] -->
Team # 2301192

<!-- b000401 | furniture | pages [22] -->
Page 22

<!-- b000402 | caption | pages [22] -->
Figure 16: Sensitivety Analysis

<!-- b000403 | prose | pages [22] -->
The New York Times may be able to learn from the characteristics of these upsurge words to enhance the fun of Wordle.

<!-- b000404 | prose | pages [22] -->
7 Sensitivety Analysis

<!-- b000405 | caption | pages [22] -->
Figure 17: Sensitivety Analysis

<!-- b000406 | prose | pages [22] -->
In improving the BP neural network model, we used a random forest model to perform re- gression on the results of three attempts. We selected parameters nestimators(the number of weak evaluators), maxfeatures(the maximum number of sampling features),maxsamples(the maximum sample size for random sampling), and maxdepth(the maximum depth of the tree) for sensitivity analysis. In each parameter analysis, we only varied that parameter while keeping the other pa-

<!-- b000407 | furniture | pages [23] -->
Team # 2301192

<!-- b000408 | furniture | pages [23] -->
Page 23

<!-- b000409 | prose | pages [23] -->
rameters at their default values. We performed 5-fold cross-validation on the dataset, and took the average of the RMSE on the training and test sets as the result for each parameter value. As shown in Figure 17, the RMSE on the training and test sets gradually decreases and stabilizes as the parameter values increase. The RMSE under various parameter changes is stable at around 6.60. This indicates that the model is not sensitive to parameter changes and is relatively stable.

<!-- b000410 | prose | pages [23] -->
8

<!-- b000411 | heading | pages [23] -->
Model Assessment

<!-- b000412 | prose | pages [23] -->
8.1

<!-- b000413 | heading | pages [23] -->
Strengths

<!-- b000414 | heading | pages [23] -->
1. The Prophet model takes into account the influence of holidays on time series and has

<!-- b000415 | prose | pages [23] -->
stronger interpretability of the model parameters, which helps us understand the changes in the number of reports.

<!-- b000416 | heading | pages [23] -->
2. The SIRS model has excellent explanatory power for the trend term of the Prophet model.

<!-- b000417 | heading | pages [23] -->
3. The BP neural network has the ability to output multiple targets and does not require

<!-- b000418 | prose | pages [23] -->
separate models for each target.

<!-- b000419 | heading | pages [23] -->
4. The K-Means++ model has the characteristics of simplicity and practicality and is suitable

<!-- b000420 | prose | pages [23] -->
for the dataset of this question.

<!-- b000421 | prose | pages [23] -->
8.2

<!-- b000422 | heading | pages [23] -->
Weaknesses

<!-- b000423 | heading | pages [23] -->
1. The Prophet model is somewhat inadequate for long-term forecasting, similar to tradi-

<!-- b000424 | prose | pages [23] -->
tional time series models to some extent.

<!-- b000425 | heading | pages [23] -->
2. The parameters of the BP neural network have randomness during initialization, and the

<!-- b000426 | prose | pages [23] -->
trained model contains this randomness, which means that in some cases, the output re- sults of the model are not always a unique value.

<!-- b000427 | heading | pages [23] -->
3. Although we are working hard to find word attributes related to the difficulty of the puzzle,

<!-- b000428 | prose | pages [23] -->
there may still be some word attributes that we have overlooked.

<!-- b000429 | heading | pages [23] -->
References

<!-- b000430 | references | pages [23] -->
[1] Algoritmy.net. Letter frequency english, Accessed on 2023-02-18.

<!-- b000431 | references | pages [23] -->
[2] Steven Bird, Ewan Klein, and Edward Loper. Natural Language Processing with Python.

<!-- b000432 | references | pages [23] -->
O’Reilly Media, 2009.

<!-- b000433 | references | pages [23] -->
[3] Sean J Taylor and Benjamin Letham. Forecasting at scale. The American Statistician, pages

<!-- b000434 | references | pages [23] -->
0–0, 2017.

<!-- b000435 | references | pages [23] -->
[4] Wolfram.com. Wordfrequencydata, Accessed on 2023-02-18.

<!-- b000436 | furniture | pages [24] -->
Team # 2301192

<!-- b000437 | furniture | pages [24] -->
Page 24

<!-- b000438 | references | pages [24] -->
Dear Sir or Madam,

<!-- b000439 | references | pages [24] -->
We are honored to present our analysis on the number of reports and word difficulty of

<!-- b000440 | references | pages [24] -->
Wordle after data analysis and modeling. We are confident that our interesting findings will be

<!-- b000441 | references | pages [24] -->
beneficial to you. The following are some of our theoretical analyses and numerical predictions.

<!-- b000442 | heading | pages [24] -->
1. The number of reports will decrease slightly, but will rise again. The process of playing

<!-- b000443 | prose | pages [24] -->
games is like an infection, people will always tire of it after liking, and like it again after being tired of. The number of players is just like an infection curve, which increases over time, reaches a peak, and then gradually decreases. Furthermore, the number of reports tends to decrease during holidays and weekends, resulting in small oscillations in the curve. Ac- cording to our model, the number of reports will drop to the range of (10,452, 21,454) on March 1, 2023(95% confidence level). Nonetheless, it will increase later.

<!-- b000444 | heading | pages [24] -->
2. No word attribute affects the proportion of scores reported that were played in Hard

<!-- b000445 | prose | pages [24] -->
Mode. The multiple linear regression model obtained by fitting shows an R-squared value of only 0.129. Correspondingly, the p-value is 0.379, which is much greater than 0.05. This indicates that there is almost no correlation between word attributes and the proportion of Hard- Mode reports. This is reasonable because no one knows what the word is before playing, and therefore, a word’s attributes do not affect whether one plays in difficult mode or not.

<!-- b000446 | heading | pages [24] -->
3. We can predict the distribution of the answer tries more accurately based on the at-

<!-- b000447 | prose | pages [24] -->
tributes of words. By training a BP neural network model, we can grasp the answer rate of words based on their properties. For example, for the word ”EERIE”, the distribution of the number of people’tries should be as follows: 0% passed in one try, 6% passed in two tries, 22% passed in three tries, 32% passed in four tries, 23% passed in five tries, 12% passed in six tries, and 4% failed to pass. We are confident that the margin of error is within 3%.

<!-- b000448 | heading | pages [24] -->
4. The attributes that contribute to the diﬀiculty of guessing words may be different from

<!-- b000449 | prose | pages [24] -->
what you imagine. Through K-means++ clustering, we divided word difficulty into three levels based on the proportion of successful tries and analyzed the relationship between difficulty and word attributes. Combining the neural network model mentioned earlier, we can directly judge the difficulty of a word based on its attributes. People may think that the difficulty of guessing a word is related to its frequency of use, but in fact, this is incorrect. In Wordle, the diﬀiculty of guessing a word is related to the variety of letters in the word, the sum of the frequencies of use of each letter, and the breadth of its usage in different fields. Based on our analysis, the word ”EERIE” should be classified as having medium difficulty.K-means++ model performed better than other similar models, thereby increasing the credibility of our results.

<!-- b000450 | prose | pages [24] -->
Next, we will introduce some interesting findings: We bet you never thought ”mummy” is the second most difficult word to guess! Up to 82% of players need to try five or more times to solve it. Other similar words include ”watch”, ”catch”, ”prize”, and so on. This is because the difficulty of guessing a word is related to what letter it starts with, for example, words starting with ”e”, ”s”, ”f”, ”w”, and ”a” are more diﬀicult to guess, while starting with ”t” easier to guess. You can try to use these interesting characteristics to design games.

<!-- b000451 | prose | pages [24] -->
These are all suggestions and strategies our team has provided to your company. Thank you for precious time. Hope that our models and these conclusion can be helpful to you!

<!-- b000452 | prose | pages [24] -->
Sincerely,

<!-- b000453 | prose | pages [24] -->
MCM Team Members

<!-- b000454 | furniture | pages [25] -->
Team # 2301192

<!-- b000455 | heading | pages [25] -->
Appendices

<!-- b000456 | furniture | pages [25] -->
Page 25

<!-- b000457 | prose | pages [25] -->
Regression Equation

<!-- b000458 | heading | pages [25] -->
Appendix A

<!-- b000459 | prose | pages [25] -->
Here is the regression equation refered in 3.5.1

<!-- b000460 | prose | pages [25] -->
(0.000) SLF −0.003

<!-- b000461 | prose | pages [25] -->
(0.000) −8.696

<!-- b000462 | prose | pages [25] -->
ˆy = 0.045

<!-- b000463 | prose | pages [25] -->
(0.365) Freq + 0.007

<!-- b000464 | prose | pages [25] -->
(0.250) NDLW + 0.008

<!-- b000465 | prose | pages [25] -->
(0.003) a

<!-- b000466 | prose | pages [25] -->
(0.013) d + 0.010

<!-- b000467 | prose | pages [25] -->
+ 0.007

<!-- b000468 | prose | pages [25] -->
(0.133) b + 0.006

<!-- b000469 | prose | pages [25] -->
(0.045) c + 0.009

<!-- b000470 | prose | pages [25] -->
(0.000) e + 0.010

<!-- b000471 | prose | pages [25] -->
(0.011) f + 0.008

<!-- b000472 | prose | pages [25] -->
(0.014) g

<!-- b000473 | prose | pages [25] -->
(0.018) j + 0.003

<!-- b000474 | prose | pages [25] -->
+ 0.007

<!-- b000475 | prose | pages [25] -->
(0.040) h + 0.010

<!-- b000476 | prose | pages [25] -->
(0.003) i + 0.027

<!-- b000477 | prose | pages [25] -->
(0.430) k + 0.006

<!-- b000478 | prose | pages [25] -->
(0.011) l + 0.007

<!-- b000479 | prose | pages [25] -->
(0.037) m

<!-- b000480 | prose | pages [25] -->
(0.052) p + 0.007

<!-- b000481 | prose | pages [25] -->
+ 0.006

<!-- b000482 | prose | pages [25] -->
(0.069) n + 0.005

<!-- b000483 | prose | pages [25] -->
(0.048) o + 0.007

<!-- b000484 | prose | pages [25] -->
(0.515) q + 0.004

<!-- b000485 | prose | pages [25] -->
(0.123) r + 0.004

<!-- b000486 | prose | pages [25] -->
(0.144) s

<!-- b000487 | prose | pages [25] -->
(0.047) v + 0.005

<!-- b000488 | prose | pages [25] -->
+ 0.008

<!-- b000489 | prose | pages [25] -->
(0.004) t + 0.009

<!-- b000490 | prose | pages [25] -->
(0.011) u + 0.010

<!-- b000491 | prose | pages [25] -->
(0.309) w + 0.011

<!-- b000492 | prose | pages [25] -->
(0.227) x + 0.010

<!-- b000493 | prose | pages [25] -->
(0.003) y

<!-- b000494 | prose | pages [25] -->
(12)

<!-- b000495 | prose | pages [25] -->
(0.320) V BG −0.020

<!-- b000496 | prose | pages [25] -->
+ 0.022

<!-- b000497 | prose | pages [25] -->
(0.032) z + 0.016

<!-- b000498 | prose | pages [25] -->
(0.062) V B −0.016

<!-- b000499 | prose | pages [25] -->
(0.477) CC + 0.008

<!-- b000500 | prose | pages [25] -->
(0.079) JJ

<!-- b000501 | prose | pages [25] -->
(0.052) V BD −0.010

<!-- b000502 | prose | pages [25] -->
(0.118) V BN + 0.016

<!-- b000503 | prose | pages [25] -->
+ 0.019

<!-- b000504 | prose | pages [25] -->
(0.156) V BZ + 0.019

<!-- b000505 | prose | pages [25] -->
(0.525) MD

<!-- b000506 | prose | pages [25] -->
(0.348) NNS + 0.014

<!-- b000507 | prose | pages [25] -->
+ 0.008

<!-- b000508 | prose | pages [25] -->
(0.066) NN + 0.010

<!-- b000509 | prose | pages [25] -->
−0.008

<!-- b000510 | prose | pages [25] -->
(0.700) JJS −0.007

<!-- b000511 | prose | pages [25] -->
(0.042) RBR + 0.012

<!-- b000512 | prose | pages [25] -->
(0.102) V BP

<!-- b000513 | prose | pages [25] -->
(0.918) PRP −0.019

<!-- b000514 | prose | pages [25] -->
(0.742) JJR + 0.003

<!-- b000515 | prose | pages [25] -->
(0.377) DT

<!-- b000516 | prose | pages [25] -->
R2 = 0.129, N = 359
