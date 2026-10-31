# P-C-2023-2318982-4176d64a

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
2318982

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Wordle: One Letter Makes a Difference

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Since its launch in early 2022, Wordle has sparked a wave of sharing yellow, green and grey squares on social media. Wordle has simple but challenging rules that requiring only a short attention span. Based on the Wordle dataset, we dig into the information hidden behind the number and the percentage of reported results.

<!-- b000011 | prose | pages [1] -->
First, we focus on the number of reported results that varies over time. We try to build an ARIMA model providing us with a prediction interval for the number of reported results on March 1, 2023. It indicates that the Wordle still maintains a high level of enthusiasm one year after its release. Then, we explore the factors influencing the percentage of Hard Mode. By fitting a multiple linear regression model, the results show that the number of repeated letters and the frequency of words are correlated with the difficulty of the game. The difficulty information that players obtained from the community in advance may influence their choice of game mode.

<!-- b000012 | prose | pages [1] -->
Next, we are curious how the distribution of the reported results would change in the future. To simplify the model, we generalize the player’s game states to their known number of squares of each color. Wordle can then be modeled as a Markov chain, and the problem is transformed into solving the first-arrival distribution of it. This requires knowledge of the initial distribution and transfer probabilities relying on the strategies chosen by players. In addition, the transfer probability is assumed to depend on the difference in the amount of information between states. So we propose a method to measure the current amount of information in the states. Based on this, we model the entire Markov chain and solve the first reach-time distribution under different strategies.

<!-- b000013 | prose | pages [1] -->
To make the model more reasonable, it is assumed that the proportion of people choosing the above two strategies varies with time. Accordingly, a method based on historical data is proposed to estimate this proportion. Finally, we combine the estimated proportion with a Gaussian process regression model to predict the future proportion of player strategy choices. This is then combined with the Markov chains model to predict the distribution of future reported results. We finally obtain the distribution of EERIE, which is (0.00, 0.15, 11.05, 28.44, 35.46, 21.16, 3.76).

<!-- b000014 | prose | pages [1] -->
Finally, we want to classify words according to their difficulty. Since word difficulty is only related to the word itself, it is believed that clustering according to word attributes can reflect the difficulty level of words. For this idea, K-Prototypes clustering is performed and reasonable word difficulty index is set. Then, we extract the difficulty information of each category, and then plot the density function and calculate Kullback-Leibler divergence. Both of results show that words with different attributes have different difficulty levels. It proves that our idea is reasonable and the classification model is accurate. Further, we classify the EERIE into “hard” class by its attributes, which is consistent with the percentage distribution obtained above. In addition, we discuss other information about the dataset, such as the difficult words, the easy words and the unexpected words. Finally, the sensitivity analysis of the model shows the good robustness of our model.

<!-- b000015 | keywords | pages [1] -->
Keywords: ARIMA; multiple linear regression; Markov chains; K-Prototypes clustering

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1

<!-- b000018 | heading | pages [2] -->
Introduction

<!-- b000019 | prose | pages [2] -->
3 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Restatement of The Problem 3 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000020 | prose | pages [2] -->
2

<!-- b000021 | heading | pages [2] -->
Model Assumptions and Notations

<!-- b000022 | prose | pages [2] -->
3

<!-- b000023 | prose | pages [2] -->
4 Assumptions and Justification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000024 | heading | pages [2] -->
Notations

<!-- b000025 | prose | pages [2] -->
3 Data Preprocessing

<!-- b000026 | prose | pages [2] -->
4

<!-- b000027 | prose | pages [2] -->
5

<!-- b000028 | prose | pages [2] -->
Task 1: Number Prediction and Word Attributes 4 5 Number Prediction Based on ARIMA Model . . . . . . . . . . . . . . . . . . . . . 4.1 5 Effect of Word Attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 10 Attributes of The Word . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 10 Multiple Linear Regression . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.2 12

<!-- b000029 | heading | pages [2] -->
Task 2: Distribution based on Markov Chain Model

<!-- b000030 | prose | pages [2] -->
5 14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 State Space 15 Initial Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 16 Transfer Probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3 17 Distribution of Reported Results . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 18 Proportion of Two Strategies Used . . . . . . . . . . . . . . . . . . . . . . . . . . 5.5 19 Predicting The Distribution of Future Reporting Results . . . . . . . . . . . . . . . 5.6

<!-- b000031 | prose | pages [2] -->
6

<!-- b000032 | heading | pages [2] -->
Task 3: Classification of Solution Words

<!-- b000033 | prose | pages [2] -->
19

<!-- b000034 | prose | pages [2] -->
20 Difficulty Score . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 20 K-Prototypes Clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 20 Solving Steps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.1 20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.2 Results 20 Difficulty Classification of Solution Words . . . . . . . . . . . . . . . . . . . . . . 6.3 21 Difficulty of The Word EERIE . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.4

<!-- b000035 | prose | pages [2] -->
7 Task 4: Other Interesting Features

<!-- b000036 | prose | pages [2] -->
8

<!-- b000037 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000038 | prose | pages [2] -->
9

<!-- b000039 | heading | pages [2] -->
Modle Evaluation and Further Discussion

<!-- b000040 | prose | pages [2] -->
21

<!-- b000041 | prose | pages [2] -->
21

<!-- b000042 | prose | pages [2] -->
23

<!-- b000043 | prose | pages [2] -->
23 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 23 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2

<!-- b000044 | heading | pages [2] -->
10 A Letter to The Puzzle Editor

<!-- b000045 | heading | pages [2] -->
References

<!-- b000046 | references | pages [2] -->
23

<!-- b000047 | references | pages [2] -->
24

<!-- b000048 | references | pages [2] -->
25

<!-- b000049 | references | pages [2] -->
1

<!-- b000050 | references | pages [2] -->
1

<!-- b000051 | furniture | pages [3] -->
Team # 2318982

<!-- b000052 | furniture | pages [3] -->
Page 3 of 25

<!-- b000053 | references | pages [3] -->
1

<!-- b000054 | heading | pages [3] -->
Introduction

<!-- b000055 | prose | pages [3] -->
1.1

<!-- b000056 | heading | pages [3] -->
Background

<!-- b000057 | prose | pages [3] -->
Wordle is a popular five-letter puzzle game offered daily by the New York Times, where players try to guess the right words in 6 tries or less, getting feedback with each guess. It’s available in over 60 languages and has two levels: regular and Hard Mode. In Hard Mode, the letters that were correctly guessed must be used in subsequent guesses. After a guess, tiles change color: yellow = letter in wrong place, green = letter in right place and gray = letter not included.

<!-- b000058 | prose | pages [3] -->
1.2 Restatement of The Problem

<!-- b000059 | prose | pages [3] -->
Considering the background information and related conditions given in the title, we need to solve the following problems:

<!-- b000060 | prose | pages [3] -->
• Develop a model to explain daily variations of reported results, and use it to create a prediciton interval for the number of results on March 1, 2023. Is the percentage of Hard Mode scores affected by the word properties? If yes, how? If no, why not?

<!-- b000061 | prose | pages [3] -->
• Develop a model to predict the solution’s (1,2,3,4,5,6,X) distribution for a specific future word. Discuss the uncertainties associated with the prediction. Provide an example of the predictions for EERIE on March 1, 2023, and the confidence in the model.

<!-- b000062 | prose | pages [3] -->
• Create a classification model to classify the words based on their difficulty, and describe the particular attributes for each. How difficult is the word EERIE according to the model? Evaluate the model’s accuracy.

<!-- b000063 | prose | pages [3] -->
• Lastly, describe other interesting features in the dataset.

<!-- b000064 | prose | pages [3] -->
1.3 Our Work

<!-- b000065 | prose | pages [3] -->
Considering the background and the problems, our work mainly includes the following:

<!-- b000066 | prose | pages [3] -->
• We hypothesized that the number of reported results on March 1st, 2023 could be predicted through building an ARIMA model with optimal parameters. To gain further insight into the word attributes, we ran a multiple linear regression to examine the effect of word attributes on the percentage of scores reported in the difficulty model.

<!-- b000067 | prose | pages [3] -->
• We modeled the process of playing wordle games as a discrete-state Markov chain and derived two game strategies based on the derived information. We then estimated the distribution of reported outcomes for the two strategies, using theoretical tools such as information entropy and Markov chain properties. The obtained outcomes were subsequently combined to make predictions regarding the distribution of reported outcomes at a future date.

<!-- b000068 | prose | pages [3] -->
• Furthermore, the difficulty of any given word is determined by its attributes.

<!-- b000069 | prose | pages [3] -->
As such, clustering words by their attributes could provide valuable insight into the difficulty of each respective category.

<!-- b000070 | prose | pages [3] -->
• Finally, after a close analysis of the dataset, we observed several noteworthy characteristics.

<!-- b000071 | prose | pages [3] -->
In order to avoid complicated description, intuitively reflect our work process, the flow chart is shown in Figure 1.

<!-- b000072 | furniture | pages [4] -->
Team # 2318982

<!-- b000073 | furniture | pages [4] -->
Page 4 of 25

<!-- b000074 | caption | pages [4] -->
Figure 1: Flow chart of our work

<!-- b000075 | prose | pages [4] -->
2

<!-- b000076 | heading | pages [4] -->
Model Assumptions and Notations

<!-- b000077 | prose | pages [4] -->
2.1

<!-- b000078 | heading | pages [4] -->
Assumptions and Justification

<!-- b000079 | prose | pages [4] -->
To simplify the problem and facilitate our modelling of the wordle game, we have made the following basic assumptions, each with appropriate justification.

<!-- b000080 | prose | pages [4] -->
(1) Players always make locally optimal choices based only on the information they currently know when playing wordle games.

<!-- b000081 | prose | pages [4] -->
(2) Most of the time, the correct answers to wordle games come from the more common words.

<!-- b000082 | prose | pages [4] -->
(3) Players are rational when playing wordle games and generally do not discard known infor- mation easily.

<!-- b000083 | prose | pages [4] -->
(4) Players play wordle by selecting fill-in words from a roughly identical word bank, and they hold the same subjective probability of whether a word is the correct answer.

<!-- b000084 | prose | pages [4] -->
(5) The higher the information gain of an event, the lower the probability of its occurrence

<!-- b000085 | prose | pages [4] -->
(6) Measuring the information content of a word on different sized thesauri gives roughly the same result.

<!-- b000086 | prose | pages [4] -->
(7) The proportion of players using each strategy does not change significantly throughout the day.

<!-- b000087 | prose | pages [4] -->
2.2

<!-- b000088 | heading | pages [4] -->
Notations

<!-- b000089 | furniture | pages [5] -->
Team # 2318982

<!-- b000090 | furniture | pages [5] -->
Page 5 of 25

<!-- b000091 | caption | pages [5] -->
Table 1: Notations

<!-- b000092 | heading | pages [5] -->
Symbols

<!-- b000093 | prose | pages [5] -->
Description

<!-- b000094 | prose | pages [5] -->
Ai The set of states that are reachable in one step of state i. S The state space of the Markov chain. W All the words a player may fill in. px The subjective probability that word x is the correct answer. freqx The word frequency of word x. Ix The amount of information obtained by filling in the word x at the opening. x(r)

<!-- b000095 | prose | pages [5] -->
The correct word of the r th day. true Gi The set of words that the player has guessed when he is in state i p(r)

<!-- b000096 | prose | pages [5] -->
k (i, j) The transfer probability from state i to j in Markov chain on day r. T (r)

<!-- b000097 | prose | pages [5] -->
The number of steps to first reach state j from state i on the Markov chain at day r. j C(r)

<!-- b000098 | prose | pages [5] -->
The set of absorbing states of Markov chains on day r. k T (r)

<!-- b000099 | prose | pages [5] -->
Number of steps before falling into an absorbing state on Markov chain at day r. absorbed qk(r) The proportion of all players using strategy k on day r.

<!-- b000100 | prose | pages [5] -->
where we define the main parameters while specific value of those parameters will be given later.

<!-- b000101 | prose | pages [5] -->
3 Data Preprocessing

<!-- b000102 | prose | pages [5] -->
Since we are only allowed to use the datasets “Problem_C_Data_Wordle.csv” by COMAP official, we need to pre-process the dataset before solving the problem. An initial inspection of the dataset showed that there are some outliers and missing values.

<!-- b000103 | prose | pages [5] -->
• In the word column, we find that the length of some words are not equal to five,such as “rprobe”, “clen” and “tash”. As mentioned by COMAP official, in line 18, for contest 545, the word listed is “rprobe” while it should be “probe”. By looking up the solution word of the day published by wordle, we also get that “clen” should be “clean” and “tash” should be “trash”.

<!-- b000104 | prose | pages [5] -->
• Additionally, in line 34, for contest 529, the number of reported results listed is “2569”, while the correct number should be “25569”.

<!-- b000105 | prose | pages [5] -->
4 Task 1: Number Prediction and Word Attributes

<!-- b000106 | prose | pages [5] -->
In this section, we predicted the number of reported results on March 1, 2023 by building an ARIMA model and choosing the optimal parameters. Then we summarize the word attributes and then explore the effect of word attributes on the percentage of scores reported in the difficulty model by building a multiple linear regression.

<!-- b000107 | prose | pages [5] -->
4.1

<!-- b000108 | heading | pages [5] -->
Number Prediction Based on ARIMA Model

<!-- b000109 | prose | pages [5] -->
Autoregressive integrated moving average, which is known as ARIMA, is a statistical analysis model that uses time-series data to predict the future trend. The basic idea of ARIMA is that the data sequence formed by the prediction over time is regarded as a random sequence and a

<!-- b000110 | furniture | pages [6] -->
Team # 2318982

<!-- b000111 | furniture | pages [6] -->
Page 6 of 25

<!-- b000112 | prose | pages [6] -->
model can be used to approximately describe this sequence. Once this sequence is identified, the model can predict future values from past and present values of the time series. ARIMA model comprises of auto-regression (AR) model and moving average (MA) model. AR model describes the relationship between the current value and lagged value and predicts the future value with the historical data. MA model leverage the linear combination of the past residual term to observe the future residual. The ARIMA prediction model can be written as the following formula:

<!-- b000113 | prose | pages [6] -->
p

<!-- b000114 | prose | pages [6] -->
q

<!-- b000115 | prose | pages [6] -->
γjp{t−j} +

<!-- b000116 | prose | pages [6] -->
ˆp{t} = p0 +

<!-- b000117 | prose | pages [6] -->
X

<!-- b000118 | prose | pages [6] -->
j=1

<!-- b000119 | prose | pages [6] -->
X

<!-- b000120 | prose | pages [6] -->
θjε{t−j}, (1)

<!-- b000121 | prose | pages [6] -->
j=1

<!-- b000122 | prose | pages [6] -->
where p is the order of Autoregressive Model (AR), q is the order of Moving Average Model (AM), ε{t} is the Error term between time t and t −1, γj and θj are the fitting coefficients, p0 is constant term.

<!-- b000123 | prose | pages [6] -->
Based on the relevant situation of this example, after comprehensively considering various time series analysis models, we choose the ARIMA model to analyze the number of reported results and give a prediction interval for that on March 1, 2023.

<!-- b000124 | prose | pages [6] -->
Our model construction and solution steps are as follows:

<!-- b000125 | prose | pages [6] -->
1. Preprocessing of time series

<!-- b000126 | prose | pages [6] -->
(1) Dividing the training set and test set

<!-- b000127 | prose | pages [6] -->
In order to evaluate the model more reasonably, the data are divided into training and test sets.

<!-- b000128 | prose | pages [6] -->
(2) Stationarity and the white noise test

<!-- b000129 | prose | pages [6] -->
When making statistical inferences about the structure of a stochastic process from the ob- served records, it is usually necessary to make certain simplifying (and approximately reasonable) assumptions about it. The most important of these assumptions is stationarity. The basic idea of stationarity is that the statistical laws that determine the properties of a process do not change with time.

<!-- b000130 | caption | pages [6] -->
Figure 2: Original time series correlation function graphs

<!-- b000131 | prose | pages [6] -->
Before conducting the stationarity test, the seasonality factor of the series is first identified simply by the ACF plot, and the time series does not have an obvious seasonal trend. The ACF plot, PACF plot and time series plot are shown in Figure 2.

<!-- b000132 | furniture | pages [7] -->
Team # 2318982

<!-- b000133 | furniture | pages [7] -->
Page 7 of 25

<!-- b000134 | prose | pages [7] -->
By plotting the time series of the number of reported results, we found that the series does not look stationary. For non-stationary processes, the transformation was performed using the differencing method. From the Figure 3 and Figure 4 below, we can observe that the sequence after difference always fluctuate randomly around a certain value, and there is no obvious trend.

<!-- b000135 | caption | pages [7] -->
Figure 3: Original time series

<!-- b000136 | caption | pages [7] -->
Figure 4: 1st order differential time series

<!-- b000137 | prose | pages [7] -->
Augmented Dickey-Fuller test to test the stationarity was performed. It is found that the original series does not reject the original hypothesis that the series is not stationary at the level of α = 0.05. The time series after the first-order difference then rejects the original hypothesis and passes the stationarity test. The statistics values before and after differencing are shown in Table 2 below.

<!-- b000138 | caption | pages [7] -->
Table 2: Augmented Dickey-Fuller test

<!-- b000139 | prose | pages [7] -->
p value Dickey-Full statistics lag

<!-- b000140 | prose | pages [7] -->
-2.8951 before difference 0.1989 6 -5.0648 after difference 0.01 6

<!-- b000141 | prose | pages [7] -->
It is further determined whether the series is a white noise series. In a white noise series, the random variables at any two points in time are not correlated and there are no dynamic laws in the series that can be exploited. Thus, historical data cannot be used to make predictions and inferences about the future. From the data, the statistics value of the Box-Ljung white noise test is 253.36, p = 0.000. The original hypothesis that the series is a white noise series is rejected at the level of α = 0.05. It indicates that the series can be predicted by an appropriate time series model.

<!-- b000142 | prose | pages [7] -->
2. Determination of parameter d

<!-- b000143 | prose | pages [7] -->
According to the analysis of step 1, the time series becomes stable after the first-order difference. Thus, the parameter d of the ARIMA model can be determined as step 1.

<!-- b000144 | prose | pages [7] -->
3. Determination of parameter p, q

<!-- b000145 | caption | pages [7] -->
Table 3: Confirmation method of p value and q value

<!-- b000146 | prose | pages [7] -->
Model ACF

<!-- b000147 | prose | pages [7] -->
AR(p) attenuation tends to 0 MA(q) truncation after q-order

<!-- b000148 | prose | pages [7] -->
PACF

<!-- b000149 | prose | pages [7] -->
truncation after p-order attenuation tends to 0 attenuation tends to 0 after q-order ARMA(p, q) attenuation tends to 0 after p-order

<!-- b000150 | prose | pages [7] -->
We tried to use autocorrelation function (ACF) and partial autocorrelation function (PACF) to determine the values of p and q. The confirmation method is shown in the Table 3.

<!-- b000151 | furniture | pages [8] -->
Team # 2318982

<!-- b000152 | furniture | pages [8] -->
Page 8 of 25

<!-- b000153 | prose | pages [8] -->
After performing first-order differencing, the ACF and PACF plots are plotted.

<!-- b000154 | caption | pages [8] -->
Figure 5: 1st order differential sequence correlation function graphs

<!-- b000155 | prose | pages [8] -->
For this figure, there are three interpretations:

<!-- b000156 | prose | pages [8] -->
• ACF PACF are trailing, ARIMA(1,1,1) model can be considered.

<!-- b000157 | prose | pages [8] -->
• ACF trailing, PACF first order truncated, consider ARIMA(1,1,0).

<!-- b000158 | prose | pages [8] -->
• ACF third-order truncated, PACF trailing, consider ARIMA(0,1,3).

<!-- b000159 | prose | pages [8] -->
The interpretation about the ACF and PACF plots is difficult and subjective. It is not sufficient to judge the order of ARIMA by this alone. The best approach to fitting ARIMA is to start with a low order model, and then try to add a parameter at a time to see if the results change.

<!-- b000160 | prose | pages [8] -->
So, we implemented this through computer programming. An ARIMA model was obtained by minimizing the evaluation criterion AICc according to a variation of the Hyndman-Khandakar algorithm (Hyndman & Khandakar, 2008).

<!-- b000161 | prose | pages [8] -->
The order d has been determined in step 2. The values of p and q are then chosen by minimizing the AICc after differencing the data d times. Rather than considering every possible combination of p and q, the algorithm uses a stepwise search to traverse the model space:

<!-- b000162 | prose | pages [8] -->
(a)Fourinitial models are fitted: ARIMA(0,d,0), ARIMA(2,d,2), ARIMA(1,d,0), ARIMA(0,d,1). A constant is included unless d = 2. If d ≤1, an additional model is also fitted: ARIMA(0,d,0) without a constant.

<!-- b000163 | prose | pages [8] -->
(b) The best model (with the smallest AICc value) fitted in (a) is set to be the “current model”.

<!-- b000164 | prose | pages [8] -->
(c) Variations on the current model are considered:

<!-- b000165 | prose | pages [8] -->
• Vary p and/or q from the current model by ±1;

<!-- b000166 | prose | pages [8] -->
• Include/exclude c from the current model.

<!-- b000167 | prose | pages [8] -->
The best model considered so far (either the current model or one of these variations) becomes the new current model.

<!-- b000168 | prose | pages [8] -->
(d) Repeat (c) until no lower AICc can be found.

<!-- b000169 | furniture | pages [9] -->
Team # 2318982

<!-- b000170 | furniture | pages [9] -->
Page 9 of 25

<!-- b000171 | prose | pages [9] -->
According to the historical data, we perform the above steps to find the orders p and q that minimize the AICc, i.e., the optimal ordering of the model. The parameters of ARIMA were selected as (1,1,1).

<!-- b000172 | prose | pages [9] -->
4. Model fitting

<!-- b000173 | prose | pages [9] -->
After determining the optimal order, we perform parameter estimation. The model coefficients were tested to be significant. Fitted curve of the model is shown in Figure 6.

<!-- b000174 | caption | pages [9] -->
Figure 6: Fitting curve

<!-- b000175 | prose | pages [9] -->
5. Residual analysis

<!-- b000176 | prose | pages [9] -->
The p-values of the standardized residuals, the ACF of the residuals, and the Ljung-Box white noise test of the residuals are shown below in Figure 7. It can be seen that the autocorrelation coefficients of the residuals fall within the confidence interval after the 1st order difference, and the trend gradually converges to 0. The white noise test is calculated for multiple lagged values. A p-value above the horizontal dashed line (0.05 line) shows that the residual series is already white noise, indicating that the ARIMA model has sufficiently extracted useful information from the data.

<!-- b000177 | caption | pages [9] -->
Figure 7: Residuals

<!-- b000178 | prose | pages [9] -->
Also, by plotting Q-Q plots, the model residuals basically obey a normal distribution with a mean of zero. Combined with the results of the autocorrelation test, it is determined that the residuals after fitting the optimal model are white noise sequences and no further modeling is required.

<!-- b000179 | furniture | pages [10] -->
Team # 2318982

<!-- b000180 | furniture | pages [10] -->
Page 10 of 25

<!-- b000181 | prose | pages [10] -->
6. Prediction

<!-- b000182 | prose | pages [10] -->
Based on the ARIMA(1,1,1) model, using data from January 07, 2022 to December 31, 2022, the number of reported results can be predicted for 60 days thereafter, as shown in Figure 8. Further, we obtain a prediction interval [10517, 27007] with 90% confidence on March 1, 2023, with an expected forecast value of 16529.

<!-- b000183 | caption | pages [10] -->
Figure 8: Prediction results

<!-- b000184 | prose | pages [10] -->
4.2 Effect of Word Attributes

<!-- b000185 | prose | pages [10] -->
To explore the effect of word attributes on the percentage of scores reported that were played in Hard Mode, we firstly summarized the attributes of the word. Then, using attributes as independent variables and percentage as dependent variables, we further determined the relationship between them by establishing multiple linear regression model.

<!-- b000186 | prose | pages [10] -->
4.2.1 Attributes of The Word

<!-- b000187 | prose | pages [10] -->
By reviewing the literature related to word attributes, we summarize the following attributes.

<!-- b000188 | prose | pages [10] -->
1. Word class

<!-- b000189 | prose | pages [10] -->
According to NLTK, the most popular English natural language processing library in Python, we annotated the class of each word by the “nltk.pos_tag” function. Since the results of its class are relatively detailed, with 34 categories[x], combined with the actual situation of word classes in the “Problem_C_Data_Wordle.csv” dataset, we ultimately classify word class into the following four categories.

<!-- b000190 | prose | pages [10] -->
• NN: Noun.

<!-- b000191 | prose | pages [10] -->
• RB: Adverb very.

<!-- b000192 | prose | pages [10] -->
• JJ: Adjective.

<!-- b000193 | prose | pages [10] -->
• Other: Word classes other than the above three word classes.

<!-- b000194 | prose | pages [10] -->
2. Frequency

<!-- b000195 | prose | pages [10] -->
Clearly, the commonness of a word affects the number of times a person tries it. According to the “English Word Frequency” dataset on Kaggle, which contains the counts of the 333,333

<!-- b000196 | furniture | pages [11] -->
Team # 2318982

<!-- b000197 | furniture | pages [11] -->
Page 11 of 25

<!-- b000198 | prose | pages [11] -->
most commonly-used single words on the English language web, as derived from the Google Web Trillion Word Corpus.

<!-- b000199 | prose | pages [11] -->
We obtained the counts of each solution word, and divided each word’s own count by the total count to obtain its frequency of occurrence.

<!-- b000200 | prose | pages [11] -->
3. Number of syllables

<!-- b000201 | prose | pages [11] -->
Each word has a certain number of syllables, and a five-letter word usually has one or two syllables.

<!-- b000202 | prose | pages [11] -->
We calculated the number of syllables for each solution word using the “text- stat.syllable_count” function of the textstat library in Python.

<!-- b000203 | prose | pages [11] -->
4. Number of letter repetitions

<!-- b000204 | prose | pages [11] -->
Although Wordle’s solution word is a five-letter word, it is likely that there are two or even more repetitions of the same letter in it, so we count the number of repetitions of letters in each word. For example, if two a’s appear, it is recorded as one time, and three a’s are recorded as two times, and the occurrence of two a’s and two b’s is also recorded as two times.

<!-- b000205 | prose | pages [11] -->
5. Polarity

<!-- b000206 | prose | pages [11] -->
Normally a word will contain either positive or negative sentiment. We use the “blob.sentiment” function of the TextBlob library in Python to get the polarity of the word, whose value lies between (−1, 1), and the higher the value means the more positive the sentiment represented by the word.

<!-- b000207 | prose | pages [11] -->
6. Subjectivity

<!-- b000208 | prose | pages [11] -->
A word usually also contains a competent or objective emotion. Same as 5, we can obtain the subjectivity of the word, whose value lies between (0, 1), the larger the value the more subjective the emotion represented by the word.

<!-- b000209 | caption | pages [11] -->
Figure 9: Attributes of the word

<!-- b000210 | furniture | pages [12] -->
Team # 2318982

<!-- b000211 | furniture | pages [12] -->
Page 12 of 25

<!-- b000212 | prose | pages [12] -->
4.2.2 Multiple Linear Regression

<!-- b000213 | prose | pages [12] -->
To explore the relationship between each attribute of the words and the percentage of scores reported that were played in Hard Mode, we chose to build a multiple linear regression model.

<!-- b000214 | prose | pages [12] -->
1. Model design

<!-- b000215 | prose | pages [12] -->
In order to investigate the relationship between the variables, we calculate the Pearson corre- lation coefficients of proportion and other independent variables, and conducts the significance test, the results are shown in Figure 10. It can be seen that there is a certain correlation between the independent variables, and the factors with strong correlation with proportion are “syllable”, “n_repeat”, “polarity”, “subjectivity” and “frequency”, which can be further investigated by estab- lishing a regression model.

<!-- b000216 | caption | pages [12] -->
Figure 10: Pearson correlation coefficients

<!-- b000217 | prose | pages [12] -->
2. Model building

<!-- b000218 | prose | pages [12] -->
The full model was developed through the previous study as follows:

<!-- b000219 | prose | pages [12] -->
Y = 0.0692 −0.0045X1 −0.0026X2 −0.0064X3 −0.0033X4 + 0.2823X5, (2)

<!-- b000220 | prose | pages [12] -->
where X1 represents number of syllables, X2 represents number of letter repetitions, X3 represents polarity, X4 represents subjectivity and X5 represents frequency.

<!-- b000221 | prose | pages [12] -->
The only significant variables found were “n_repeat” and “frequency”. Then, these two variables were filtered by LASSO regression method to establish the final regression model as follows:

<!-- b000222 | prose | pages [12] -->
Y = 0.0750 −0.0035X1 + 0.2663X2, (3)

<!-- b000223 | prose | pages [12] -->
where X1 represents number of letter repetitions and X2 represents frequency. And R2

<!-- b000224 | prose | pages [12] -->
adj reached 0.782. The regression equation and regression coefficients all pass the significance test.

<!-- b000225 | prose | pages [12] -->
3. Adequacy tests

<!-- b000226 | prose | pages [12] -->
For the linear regression model, the assumptions are: the errors are independently and iden- tically distributed and follow a normal distribution, there is no linear relationship between the

<!-- b000227 | furniture | pages [13] -->
Team # 2318982

<!-- b000228 | furniture | pages [13] -->
Page 13 of 25

<!-- b000229 | prose | pages [13] -->
explanatory variables, and the response variable is linearly related to the explanatory variables. These assumptions are tested in the following section. Using the “plot()” function for the “lm()” function in R, the regression diagnostic results are shown in Figure 11.

<!-- b000230 | caption | pages [13] -->
Figure 11: Adequacy test

<!-- b000231 | prose | pages [13] -->
• Residual normality test

<!-- b000232 | prose | pages [13] -->
The upper-right panel in Figure 11 of the regression diagnostic shows that all points are around the straight line, indicating that there is no reason to doubt the normality assumption.

<!-- b000233 | prose | pages [13] -->
• Independent homoscedasticity test for residuals

<!-- b000234 | prose | pages [13] -->
The bottom left panel in Figure 11 shows that there is no significant trend in the residuals, so the errors are considered to be independently and identically distributed.

<!-- b000235 | prose | pages [13] -->
• Model linearity test

<!-- b000236 | prose | pages [13] -->
There is no clear curvilinear relationship in the top left panel of Figure 11, so the linearity is considered to be valid.

<!-- b000237 | prose | pages [13] -->
• Model multicollinearity test

<!-- b000238 | caption | pages [13] -->
Table 4: V IF

<!-- b000239 | prose | pages [13] -->
X1 X2

<!-- b000240 | prose | pages [13] -->
V IF 1.166984 1.341964

<!-- b000241 | prose | pages [13] -->
One way to test for multicollinearity is to calculate the variance inflation factor (V IF), and multicollinearity is considered to exist if the variance inflation factor of a single variable is greater than 10. The results of calculating V IF for the two variables of model (x) are shown in Table 4, which shows that there is no significant multicollinearity in the model.

<!-- b000242 | prose | pages [13] -->
In summary, the above assumptions of the model are considered to be valid.

<!-- b000243 | prose | pages [13] -->
4. Results

<!-- b000244 | furniture | pages [14] -->
Team # 2318982

<!-- b000245 | furniture | pages [14] -->
Page 14 of 25

<!-- b000246 | prose | pages [14] -->
After a series of model tests, the final established multiple linear regression equation was determined to be:

<!-- b000247 | prose | pages [14] -->
Y = 0.0750 −0.0035X1 + 0.2663X2, (4)

<!-- b000248 | prose | pages [14] -->
where X1 represents number of letter repetitions and X2 represents frequency.

<!-- b000249 | prose | pages [14] -->
The equation shows that the significant variables affecting the percentage of scores reported that were played in Hard Mode are number of letter repetitions and frequency. Frequency is positively correlated with proportion and n_repeat is negatively correlated with proportion.

<!-- b000250 | prose | pages [14] -->
We know that Hard Mode is chosen before the start of the game and should have no relationship with attributes of the word. However, for the number of letter repetitions, its increase will make fewer players choose Hard Mode. This may be because when a word has more than one repeated letter, people generally do not think that there are still letters in the solution word hidden in the green square, so it is not easy to guess the right answer quickly, resulting in a much higher probability of not solving it. At this time, people will also know from Twitter that today’s solution word is difficult, so they will not choose Hard Mode.

<!-- b000251 | prose | pages [14] -->
Similarly, for frequency, it is positively correlated with the ratio, probably because when the frequency is high, people are more likely to get the answer right quickly and share the result on Twitter, so that other players will choose Hard Mode to challenge themselves when they find that the question is easier today. When the frequency is small, players will not choose Hard Mode in order to have a higher chance of guessing the solution word correctly.

<!-- b000252 | prose | pages [14] -->
5

<!-- b000253 | heading | pages [14] -->
Task 2: Distribution based on Markov Chain Model

<!-- b000254 | caption | pages [14] -->
Figure 12: Flow chart of Markov Chain

<!-- b000255 | prose | pages [14] -->
According to Assumption (1), players are rational (they do not give up information they already have) and greedy (they only try to give a locally optimal solution based on the situation at hand), so the game process can be modelled as a Markov chain. We generalise the player’s state in the wordle game to the number of squares of each colour that have been obtained, and obtain as the state space of this Markov chain all states that the player may reach in 6 steps. We also envisage two strategies for the player.

<!-- b000256 | furniture | pages [15] -->
Team # 2318982

<!-- b000257 | furniture | pages [15] -->
Page 15 of 25

<!-- b000258 | prose | pages [15] -->
• Probability first principle. According to Assumption (2), Common words are more likely to be the answer, so one can measure the frequency of use of a word to get a subjective probability that it is the correct answer, and fill in the word that has a high probability of being the correct answer each time.

<!-- b000259 | prose | pages [15] -->
• Information first principle. Playing the wordle game is essentially a process of acquiring information, narrowing down the range of possible words, and finally getting the only correct answer, so it is also a good strategy to fill in the words that have a high probability of providing more information each time.

<!-- b000260 | prose | pages [15] -->
Based on these two strategies, we propose two corresponding principles for selecting the first fill-in words, and thus obtain an initial distribution of the influence of the day’s answers under both strategies. In addition, we give a way to quantify the information obtained by the player in the current state, assuming that the transfer probability between the two states is a simple function of the corresponding information increment and is influenced by the strategy used by the player, thus obtaining the transfer probability of this Markov chain. At this point we can then calculate the distribution of reported outcomes under both strategies.

<!-- b000261 | prose | pages [15] -->
To better model the wordle game, we assume that the proportion of people using the two strategies varies from day to day and give a method for estimating the proportion of strategies for that day from the historical data. Finally, we use the estimate of the proportion on the historical data, combined with a Gaussian process regression model, to give an estimate of the future proportion of strategies, and use the predicted future proportion of strategies combined with the distribution of reported results under the different strategies to achieve a prediction of the distribution of reported results.

<!-- b000262 | prose | pages [15] -->
5.1 State Space

<!-- b000263 | prose | pages [15] -->
The player’s state in the wordle game can be represented by the set of green, yellow, and gray blocks that has been obtained, which represents all the information the player has about the current state, and the player’s decision is based entirely on this set (Assumption (1)). The green and yellow blocks in the set carry both position and letter information, thus there are 5(possible positions) × 26(possible letters) = 130 each, while the gray blocks represent only letter information and there are 26 in total.

<!-- b000264 | prose | pages [15] -->
To simplify the model, the set is reduced to a triple (ngreen, nyellow, ngrey), where ncolor represents the number of “color” blocks the player currently obtains.

<!-- b000265 | prose | pages [15] -->
According to Assumption (3), the player will keep the already obtained green blocks in the next guess, i.e. the number of known green blocks will not decrease and the total number of obtained new color blocks will not exceed (5 - the number of already obtained green blocks). Obviously, the known yellow blocks can only be transformed into green blocks, so the sum of green and yellow blocks does not decrease. In addition, the number of gray blocks does not decrease either. Let Ai = {j : j is accessible from i in one step}. To sum up, for state i = (ngreen, nyellow, ngrey) and state j = (n′

<!-- b000266 | prose | pages [15] -->
green, n′

<!-- b000267 | prose | pages [15] -->
yellow, n′

<!-- b000268 | prose | pages [15] -->
grey),

<!-- b000269 | prose | pages [15] -->
j ∈Ai ⇔

<!-- b000270 | furniture | pages [16] -->
Team # 2318982

<!-- b000271 | prose | pages [16] -->


<!-- b000272 | prose | pages [16] -->
ngreen̸ = 5

<!-- b000273 | prose | pages [16] -->
 

<!-- b000274 | prose | pages [16] -->
n′

<!-- b000275 | prose | pages [16] -->
green ≥ngreen

<!-- b000276 | prose | pages [16] -->
    

<!-- b000277 | prose | pages [16] -->
n′

<!-- b000278 | prose | pages [16] -->
grey ≥ngrey n′

<!-- b000279 | prose | pages [16] -->
green + n′

<!-- b000280 | prose | pages [16] -->


<!-- b000281 | furniture | pages [16] -->
Page 16 of 25

<!-- b000282 | prose | pages [16] -->
ngreen = 5

<!-- b000283 | prose | pages [16] -->
  

<!-- b000284 | prose | pages [16] -->
n′

<!-- b000285 | prose | pages [16] -->
green = ngreen

<!-- b000286 | prose | pages [16] -->
 

<!-- b000287 | prose | pages [16] -->
or

<!-- b000288 | prose | pages [16] -->
(5)

<!-- b000289 | prose | pages [16] -->
n′

<!-- b000290 | prose | pages [16] -->
yellow = nyellow

<!-- b000291 | prose | pages [16] -->


<!-- b000292 | prose | pages [16] -->
yellow ≥ngreen + nyellow

<!-- b000293 | prose | pages [16] -->
    

<!-- b000294 | prose | pages [16] -->
n′

<!-- b000295 | prose | pages [16] -->
green + n′

<!-- b000296 | prose | pages [16] -->
yellow + n′

<!-- b000297 | prose | pages [16] -->
 

<!-- b000298 | prose | pages [16] -->
n′

<!-- b000299 | prose | pages [16] -->


<!-- b000300 | prose | pages [16] -->
grey = ngrey

<!-- b000301 | prose | pages [16] -->
grey ≤nyellow + ngrey + 5

<!-- b000302 | prose | pages [16] -->


<!-- b000303 | prose | pages [16] -->
Let Bi be the set of states that the player may reach after the ith guess, then

<!-- b000304 | prose | pages [16] -->
6[

<!-- b000305 | prose | pages [16] -->
!

<!-- b000306 | prose | pages [16] -->
B0 = {(0, 0, 0)}, Bi+1 = {j : ∃i ∈Bi s.t. j ∈Ai}, i = 0, 1, 2, · · · , S =

<!-- b000307 | prose | pages [16] -->
∪{X}

<!-- b000308 | prose | pages [16] -->
Bi

<!-- b000309 | prose | pages [16] -->
(6)

<!-- b000310 | prose | pages [16] -->
i=0

<!-- b000311 | prose | pages [16] -->
where state X means the game has failed. S is the state space of the Markov chain. There are 384 states in total, and a chain is shown below as a example.

<!-- b000312 | caption | pages [16] -->
Figure 13: Markov Chain

<!-- b000313 | prose | pages [16] -->
5.2 Initial Distribution

<!-- b000314 | prose | pages [16] -->
According to Assumption (4), wordle players have approximately the same word bank and hold the same subjective probability of whether a word is the correct answer. Let W be all the words a player may fill in, and the subjective probability that a word x ∈W is the correct answer is px.

<!-- b000315 | prose | pages [16] -->
A dataset from internet can be used as an approximation of W, which contains about 36,000 of the most common five-letter words and their word frequencies. The sigmoid function can map any real number to [0, 1] and has the characteristic of changing faster around zero, so for a word x, we can put

<!-- b000316 | prose | pages [16] -->
px = 1 (7) 1 + e−(freqx−k)

<!-- b000317 | prose | pages [16] -->
as the subjective probability that x is the correct answer, where freqx is the word frequency of word x and k is a positive integer. Taking k to be the median of its word frequency, we get {px : x ∈W}.

<!-- b000318 | furniture | pages [17] -->
Team # 2318982

<!-- b000319 | furniture | pages [17] -->
Page 17 of 25

<!-- b000320 | prose | pages [17] -->
For players who use the second strategy (information first), we can assume that they use

<!-- b000321 | prose | pages [17] -->
card({y ∈W : match(x, y) = match(x, xtrue)})

<!-- b000322 | prose | pages [17] -->
Ix = −log2

<!-- b000323 | prose | pages [17] -->
(8) card(W)

<!-- b000324 | prose | pages [17] -->
to measure the amount of information obtained by filling in the word x at the opening, where card(·) denotes the number of elements in the set, match(x, y) denotes the match obtained by filling in the word x when the correct answer is the word y, and x(r)

<!-- b000325 | prose | pages [17] -->
day. Obviously,

<!-- b000326 | prose | pages [17] -->
∀x ∈W, E[Ix] = E[E[Ix|x(r)

<!-- b000327 | prose | pages [17] -->
true]] =

<!-- b000328 | prose | pages [17] -->
Replacing P(x(r)

<!-- b000329 | prose | pages [17] -->
true denotes the correct word of the r th

<!-- b000330 | prose | pages [17] -->
E[Ix|x(r)

<!-- b000331 | prose | pages [17] -->
true = x0]P(x(r)

<!-- b000332 | prose | pages [17] -->
X

<!-- b000333 | prose | pages [17] -->
true = x0).

<!-- b000334 | prose | pages [17] -->
(9)

<!-- b000335 | prose | pages [17] -->
x0∈W

<!-- b000336 | prose | pages [17] -->
true = x0) with the subjective probability px0, we obtain

<!-- b000337 | prose | pages [17] -->
card({y ∈W : match(x, y) = match(x, x0)})

<!-- b000338 | prose | pages [17] -->
X

<!-- b000339 | prose | pages [17] -->
E[Ix] ≈

<!-- b000340 | prose | pages [17] -->
−log2

<!-- b000341 | prose | pages [17] -->
x0∈W

<!-- b000342 | prose | pages [17] -->
px0 ≜˜E[Ix].

<!-- b000343 | prose | pages [17] -->
(10) card(W)

<!-- b000344 | prose | pages [17] -->
˜E[Ix]

<!-- b000345 | prose | pages [17] -->
We can assume that the player using the second strategy picks the word x with probability

<!-- b000346 | prose | pages [17] -->
as the first word to fill in.

<!-- b000347 | prose | pages [17] -->
A mapping can be created

<!-- b000348 | prose | pages [17] -->


<!-- b000349 | prose | pages [17] -->
y∈W ˜E[Iy]

<!-- b000350 | prose | pages [17] -->
P

<!-- b000351 | prose | pages [17] -->


<!-- b000352 | prose | pages [17] -->
The number of green blocks in match(x, x(r)

<!-- b000353 | prose | pages [17] -->
true) The number of yellow blocks in match(x, x(r)

<!-- b000354 | prose | pages [17] -->
f : W →S, f(x) =

<!-- b000355 | prose | pages [17] -->
 

<!-- b000356 | prose | pages [17] -->
, ∀x ∈W.

<!-- b000357 | prose | pages [17] -->
(11)

<!-- b000358 | prose | pages [17] -->
true)

<!-- b000359 | prose | pages [17] -->


<!-- b000360 | prose | pages [17] -->
The number of grey blocks in match(x, x(r)

<!-- b000361 | prose | pages [17] -->
true)

<!-- b000362 | prose | pages [17] -->
Let the Markov chain for the wordle game on day r be {X(r)

<!-- b000363 | prose | pages [17] -->
players using the first type of strategy holds

<!-- b000364 | prose | pages [17] -->
P(X(r)

<!-- b000365 | prose | pages [17] -->
= i) = 0

<!-- b000366 | prose | pages [17] -->
∈S : i = 0, 1, 2, . . . }, then for i

<!-- b000367 | prose | pages [17] -->
X

<!-- b000368 | prose | pages [17] -->
px, ∀i ∈S, (12)

<!-- b000369 | prose | pages [17] -->
x∈W:f(x)=i

<!-- b000370 | prose | pages [17] -->
for players using the second strategy holds

<!-- b000371 | prose | pages [17] -->
x∈W:f(x)=i ˜E[Ix]

<!-- b000372 | prose | pages [17] -->
P

<!-- b000373 | prose | pages [17] -->
P(X(r)

<!-- b000374 | prose | pages [17] -->
= i) = 0

<!-- b000375 | prose | pages [17] -->
P

<!-- b000376 | prose | pages [17] -->
, ∀i ∈S.

<!-- b000377 | prose | pages [17] -->
(13)

<!-- b000378 | prose | pages [17] -->
y∈W ˜E[Iy]

<!-- b000379 | prose | pages [17] -->
This gives the initial distribution of players using different strategies on the Markov chain for that day.

<!-- b000380 | prose | pages [17] -->
5.3 Transfer Probability

<!-- b000381 | prose | pages [17] -->
Let

<!-- b000382 | prose | pages [17] -->
card({x ∈W : S

<!-- b000383 | prose | pages [17] -->
Ii = −log2

<!-- b000384 | prose | pages [17] -->
y∈Gi match(x, y) = i}) , (14) card(W)

<!-- b000385 | furniture | pages [18] -->
Team # 2318982

<!-- b000386 | furniture | pages [18] -->
Page 18 of 25

<!-- b000387 | prose | pages [18] -->
where Gi is the set of words that the player has guessed when he is in state i. Then Ii measures the information amount of state i (the degree to which the number of alternative words decreases after knowing that the match results in i).

<!-- b000388 | prose | pages [18] -->
Denote the transfer probability from state i to j in Markov chain {X(r)

<!-- b000389 | prose | pages [18] -->
p(r) ∈S : i = 0, 1, 2, . . . } as i

<!-- b000390 | prose | pages [18] -->
k (i, j) when the k th strategy (k = 1, 2) is used. By assumption (5), and noting that the second strategy (information-first) is more focused on obtaining more information compared to the first (probability-first), we can simply let

<!-- b000391 | prose | pages [18] -->


<!-- b000392 | prose | pages [18] -->
ek(Ij−Ii)+C

<!-- b000393 | prose | pages [18] -->
j ∈Ai k(Ij−Ii)+C ,

<!-- b000394 | prose | pages [18] -->
 

<!-- b000395 | prose | pages [18] -->
p(r)

<!-- b000396 | prose | pages [18] -->
P

<!-- b000397 | prose | pages [18] -->
j:j∈Ai e

<!-- b000398 | prose | pages [18] -->
k (i, j) =

<!-- b000399 | prose | pages [18] -->


<!-- b000400 | prose | pages [18] -->
0,

<!-- b000401 | prose | pages [18] -->


<!-- b000402 | prose | pages [18] -->
, C ∈R+.

<!-- b000403 | prose | pages [18] -->
(15)

<!-- b000404 | prose | pages [18] -->
j̸ ∈Ai

<!-- b000405 | prose | pages [18] -->
According to Assumption (6), for state i = (ngreen, nyellow, ngrey) ∈S, Ii can be estimated by

<!-- b000406 | prose | pages [18] -->
card({(xi, xj) ∈W × W : match(xi, xj) = i})

<!-- b000407 | prose | pages [18] -->
, (16) card2(W)

<!-- b000408 | prose | pages [18] -->
which gives the transfer probability of the Marxian chain {X(r)

<!-- b000409 | prose | pages [18] -->
th strategy.

<!-- b000410 | prose | pages [18] -->
5.4

<!-- b000411 | heading | pages [18] -->
Distribution of Reported Results

<!-- b000412 | prose | pages [18] -->
For a Markov chain {X(r)

<!-- b000413 | prose | pages [18] -->
∈S : i = 0, 1, 2, . . . } under the k i

<!-- b000414 | prose | pages [18] -->
∈S : i = 0, 1, 2, . . . }, denote its transfer probability matrix under i strategy k as P(r)

<!-- b000415 | prose | pages [18] -->
k . Let

<!-- b000416 | prose | pages [18] -->
T (r)

<!-- b000417 | prose | pages [18] -->
= j}, ρ(r)

<!-- b000418 | prose | pages [18] -->
ijn = P(T (r)

<!-- b000419 | prose | pages [18] -->
= inf{n ≥1 : X(r)

<!-- b000420 | prose | pages [18] -->
n

<!-- b000421 | prose | pages [18] -->
j

<!-- b000422 | prose | pages [18] -->
= n|X(r)

<!-- b000423 | prose | pages [18] -->
n = [ρ(r)

<!-- b000424 | prose | pages [18] -->
= i), G(r)

<!-- b000425 | prose | pages [18] -->
ijn]i,j∈S (17)

<!-- b000426 | prose | pages [18] -->
0

<!-- b000427 | prose | pages [18] -->
j

<!-- b000428 | prose | pages [18] -->
c = card(S), E = 1c1T

<!-- b000429 | prose | pages [18] -->
now the following equation holds

<!-- b000430 | prose | pages [18] -->
n = P(r)

<!-- b000431 | prose | pages [18] -->
k (. . . (P(r)

<!-- b000432 | prose | pages [18] -->
k (P(r)

<!-- b000433 | prose | pages [18] -->
G(r)

<!-- b000434 | prose | pages [18] -->
{z | n

<!-- b000435 | prose | pages [18] -->
c −Ic, (18)

<!-- b000436 | prose | pages [18] -->
k (P(r)

<!-- b000437 | prose | pages [18] -->
·E) · E) · . . . ) · E), (19)

<!-- b000438 | prose | pages [18] -->
k }

<!-- b000439 | prose | pages [18] -->
where · means the element-by-element multiplication of the matrix. Obviously this Markov chain is absorbing. Let

<!-- b000440 | prose | pages [18] -->
k (i, j) = 0, ∀j̸ = i}, T (r)

<!-- b000441 | prose | pages [18] -->
C(r)

<!-- b000442 | prose | pages [18] -->
= {i ∈S : p(r) k

<!-- b000443 | prose | pages [18] -->
then

<!-- b000444 | prose | pages [18] -->
∈C(r)

<!-- b000445 | prose | pages [18] -->
absorbed = inf{n ≥1 : X(r)

<!-- b000446 | prose | pages [18] -->
k }, (20)

<!-- b000447 | prose | pages [18] -->
n

<!-- b000448 | prose | pages [18] -->
ijn, P(T (r)

<!-- b000449 | prose | pages [18] -->
P(T (r)

<!-- b000450 | prose | pages [18] -->
absorbed = n|X(r)

<!-- b000451 | prose | pages [18] -->
ρ(r)

<!-- b000452 | prose | pages [18] -->
X

<!-- b000453 | prose | pages [18] -->
= i) = 0

<!-- b000454 | prose | pages [18] -->
j∈C

<!-- b000455 | prose | pages [18] -->
Now we have the distribution of T (r)

<!-- b000456 | prose | pages [18] -->
ρ(r)

<!-- b000457 | prose | pages [18] -->
ijnP(X(r)

<!-- b000458 | prose | pages [18] -->
X

<!-- b000459 | prose | pages [18] -->
X

<!-- b000460 | prose | pages [18] -->
absorbed = n) =

<!-- b000461 | prose | pages [18] -->
= i) (21) 0

<!-- b000462 | prose | pages [18] -->
i∈S

<!-- b000463 | prose | pages [18] -->
j∈C

<!-- b000464 | prose | pages [18] -->
absorbed, which gives us the distribution of reported results under strategy k

<!-- b000465 | prose | pages [18] -->
P (r)

<!-- b000466 | prose | pages [18] -->
k (reported results = X) = P(T (r)

<!-- b000467 | prose | pages [18] -->
6

<!-- b000468 | prose | pages [18] -->
P(T (r)

<!-- b000469 | prose | pages [18] -->
X

<!-- b000470 | prose | pages [18] -->
absorbed ≥7) = 1 −

<!-- b000471 | prose | pages [18] -->
absorbed = i), (22)

<!-- b000472 | prose | pages [18] -->
i=1

<!-- b000473 | prose | pages [18] -->
k (reported results = i tries) = P(T (r)

<!-- b000474 | prose | pages [18] -->
P (r)

<!-- b000475 | prose | pages [18] -->
absorbed = i), i = 1, 2, . . . , 6.

<!-- b000476 | prose | pages [18] -->
(23)

<!-- b000477 | furniture | pages [19] -->
Team # 2318982

<!-- b000478 | furniture | pages [19] -->
Page 19 of 25

<!-- b000479 | prose | pages [19] -->
Proportion of Two Strategies Used 5.5

<!-- b000480 | prose | pages [19] -->
According to Assumption (7), the proportion of all players using strategy k on day r is qk(r), k = 1, 2, where q1(r) + q2(r) = 1. The theoretical distribution of reported results among all players on that day is

<!-- b000481 | prose | pages [19] -->
2 X

<!-- b000482 | prose | pages [19] -->
P (r)(reported results = X) =

<!-- b000483 | prose | pages [19] -->
k=1

<!-- b000484 | prose | pages [19] -->
2

<!-- b000485 | prose | pages [19] -->
qk(r)P (r)

<!-- b000486 | prose | pages [19] -->
X

<!-- b000487 | prose | pages [19] -->
P (r)( reported results = i tries) =

<!-- b000488 | prose | pages [19] -->
qk(r)P (r)

<!-- b000489 | prose | pages [19] -->
k (reported results = X), (24)

<!-- b000490 | prose | pages [19] -->
k (reported results = i tries), i = 1, 2, . . . , 6. (25)

<!-- b000491 | prose | pages [19] -->
k=1

<!-- b000492 | prose | pages [19] -->
Suppose the true distribution of reported results for that day is

<!-- b000493 | prose | pages [19] -->
true(reported results = X) = l(r)

<!-- b000494 | prose | pages [19] -->
P (r)

<!-- b000495 | prose | pages [19] -->
P (r)

<!-- b000496 | prose | pages [19] -->
X , (26)

<!-- b000497 | prose | pages [19] -->
true(reported results = i tries) = l(r)

<!-- b000498 | prose | pages [19] -->
i , i = 1, 2, . . . , 6.

<!-- b000499 | prose | pages [19] -->
(27)

<!-- b000500 | prose | pages [19] -->
Then, similar to the MLE method, the q1, q2 minimizing the cross-entropy between the theoretical distribution and the true distribution can be taken as a estimate of qk(r), i.e.

<!-- b000501 | prose | pages [19] -->
h

<!-- b000502 | prose | pages [19] -->
i 1 (reported results = X) + (1 −q)P (r)

<!-- b000503 | prose | pages [19] -->
qP (r)

<!-- b000504 | prose | pages [19] -->
{−ln

<!-- b000505 | prose | pages [19] -->
ˆq1(r) = arg min

<!-- b000506 | prose | pages [19] -->
q∈[0,1]

<!-- b000507 | prose | pages [19] -->
6

<!-- b000508 | prose | pages [19] -->
h

<!-- b000509 | prose | pages [19] -->
l(r)

<!-- b000510 | prose | pages [19] -->
2 (reported results = X)

<!-- b000511 | prose | pages [19] -->
X

<!-- b000512 | prose | pages [19] -->
i 1 (reported results = i) + (1 −q)P (r)

<!-- b000513 | prose | pages [19] -->
qP (r)

<!-- b000514 | prose | pages [19] -->
X

<!-- b000515 | prose | pages [19] -->
−

<!-- b000516 | prose | pages [19] -->
ln

<!-- b000517 | prose | pages [19] -->
i=1

<!-- b000518 | prose | pages [19] -->
},

<!-- b000519 | prose | pages [19] -->
2 (reported results = i)

<!-- b000520 | prose | pages [19] -->
(28)

<!-- b000521 | prose | pages [19] -->
ˆq2(r) = 1 −ˆq1(r).

<!-- b000522 | prose | pages [19] -->
(29)

<!-- b000523 | heading | pages [19] -->
Predicting The Distribution of Future Reporting Results

<!-- b000524 | prose | pages [19] -->
5.6

<!-- b000525 | prose | pages [19] -->
Gaussian Processes (GP) are a generic supervised learning method designed to solve regression and probabilistic classification problems, while inference of continuous values with a Gaussian process prior is known as Gaussian Process Regression (GPR).

<!-- b000526 | prose | pages [19] -->
We estimate ˆq1(r) for each day from January 7, 2022 to December 31, 2022 based on the above model, obtain a time series and fit it with the GPR model to get the predicted value and confidence interval of q1(r) for March 1, 2023. In addition, we can also use the above model together with the correct word "eerie" on March 1, 2023 to obtain the distribution of reported results under both strategies.

<!-- b000527 | prose | pages [19] -->
Using the above method, we obtain q1(r) with a predicted value of 0.63 and 95% confi- dence interval of [0.59, 0.67], and the distribution of reported results under the two strategies are (0, 0, 12.6, 22.0, 39.6, 21.6, 4.2) and (0, 0.4, 8.4, 39.4, 28.4, 20.4, 3.0) respectively.

<!-- b000528 | prose | pages [19] -->
Our final prediction for the distribution of reported results is (0.000, 0.148, 11.046, 28.438, 35.456, 21.156, 3.756).

<!-- b000529 | furniture | pages [20] -->
Team # 2318982

<!-- b000530 | furniture | pages [20] -->
Page 20 of 25

<!-- b000531 | prose | pages [20] -->
6

<!-- b000532 | heading | pages [20] -->
Task 3: Classification of Solution Words

<!-- b000533 | prose | pages [20] -->
The difficulty of a word is determined by the word itself and is reflected in the multiple attributes of the word. We conjecture that clustering words according to their attributes will give us information about the difficulty of the words embedded in each category.

<!-- b000534 | prose | pages [20] -->
6.1 Difficulty Score

<!-- b000535 | prose | pages [20] -->
From the previous study, it is clear that the percentages of (1, 2, 3, 4, 5, 6, X) are only related to the words themselves and not to other factors. Since X represents the result of 7 or more guesses, and unless the player intentionally guesses a five-letter word many times without getting the result, the average value of the number of guesses is estimated to be 8. We combine the percentage of each possible number of attempts to obtain the weighting formula for calculating the difficulty score:

<!-- b000536 | prose | pages [20] -->
score = x1 + 2x2 + 3x3 + 4x4 + 5x5 + 6x6 + 8x7, (30)

<!-- b000537 | prose | pages [20] -->
where x1 represents percentage of 1 try, x2 represents percentage of 2 tries, x3 represents percentage of 3 tries, x4 represents percentage of 4 tries, x5 represents percentage of 5 tries, x6 represents percentage of 6 tries, x7 represents percentage of 7 or more tries.

<!-- b000538 | prose | pages [20] -->
6.2 K-Prototypes Clustering

<!-- b000539 | prose | pages [20] -->
6.2.1 Solving Steps

<!-- b000540 | prose | pages [20] -->
• Select a prototype (central sample) for each cluster from the data set X.

<!-- b000541 | prose | pages [20] -->
• Assign the samples in X to the category closest to the prototype and update the prototype of the category after each assignment.

<!-- b000542 | prose | pages [20] -->
• After all the samples are assigned to their respective classes, recalculate the distance of the samples to the present prototype. If a sample is closer to the new prototype than the original prototype, then reassign it to the category of the new prototype.

<!-- b000543 | prose | pages [20] -->
• Repeat the process of the previous step until no samples change categories.

<!-- b000544 | prose | pages [20] -->
6.2.2

<!-- b000545 | heading | pages [20] -->
Results

<!-- b000546 | caption | pages [20] -->
Figure 14: Clustering result

<!-- b000547 | prose | pages [20] -->
Three classes of words are obtained according to K-Prototypes clustering, and their class characteristics are summarized by their clustering centers as Figure 14.

<!-- b000548 | furniture | pages [21] -->
Team # 2318982

<!-- b000549 | furniture | pages [21] -->
Page 21 of 25

<!-- b000550 | prose | pages [21] -->
6.3

<!-- b000551 | heading | pages [21] -->
Difficulty Classification of Solution Words

<!-- b000552 | prose | pages [21] -->
According to the difficulty score density plot x, the differences between the three distributions were obvious; the Kullback-Leibler divergence between the three categories was calculated and was 109.59, 271.9 and 864.3 respectively, which proves that our model is accurate for the classification of difficulty. From the above analysis, the categories obtained according to word attributes better distinguished word difficulty.

<!-- b000553 | caption | pages [21] -->
Figure 15: Word Classification by Difficulty

<!-- b000554 | prose | pages [21] -->
Easy words tend to be monosyllabic, adjectival, and subjective in emotional attitude. And difficult words tend to be bisyllabic, presence of repeated letters, objective, negative.

<!-- b000555 | prose | pages [21] -->
6.4 Difficulty of The Word EERIE

<!-- b000556 | prose | pages [21] -->
In the word EERIE, the letter E is repeated three times, the word itself has a negative meaning and is not commonly used in life. According to these attributes, ERRIE is classified as the first of the three categories, whose difficulty level is hard.

<!-- b000557 | prose | pages [21] -->
7 Task 4: Other Interesting Features

<!-- b000558 | prose | pages [21] -->
After a close analysis of the dataset, we observed several noteworthy characteristics.

<!-- b000559 | prose | pages [21] -->
• Volatility of the number of reported results

<!-- b000560 | prose | pages [21] -->
As Figure 4 shown before, the difference between the daily Number of reported results and the previous day has a very uncertain volatility, so we selected the dates where the absolute value of the volatility is greater than 40,000 to present the following Table 5.

<!-- b000561 | caption | pages [21] -->
Table 5: Volatility

<!-- b000562 | prose | pages [21] -->
Date

<!-- b000563 | prose | pages [21] -->
Sudden increase 2022-2-18, 2022-3-17 Sudden decrease 2022-1-19, 2022-2-17, 2022-2-8, 2022-1-11, 2022-1-31

<!-- b000564 | prose | pages [21] -->
Then we selected 2022-2-18 and 2022-1-11 to analyze the reasons for the fluctuations.

<!-- b000565 | prose | pages [21] -->
For the plunge in the number reported for 2022-2-18, it may be due to the fact that the word dodge was so difficult that people could not guess it and therefore did not choose to share their scores.

<!-- b000566 | furniture | pages [22] -->
Team # 2318982

<!-- b000567 | furniture | pages [22] -->
Page 22 of 25

<!-- b000568 | prose | pages [22] -->
For 2022-1-11, the sudden increase in the number of reported scores may be due to the fact that the word drink was easy and people guessed it quickly, so they chose to share their scores.

<!-- b000569 | prose | pages [22] -->
• The easiest words

<!-- b000570 | prose | pages [22] -->
If only the first correct guesses are considered, there are 15 words with a percentage of 1 correct guess greater than 0.01. It was found that none of these words had duplicate letters, and the most frequent letter was “a”, which appeared 11 times, followed by “e” and “t”, both of which appeared 10 times. Since it was the first time to guess, and the questions were random, people would optimally choose to guess a word with 5 different letters, thus achieving maximum elimination efficiency. In addition, since “a”, “e” and “t” are the letters that appear more frequently in the words that make up the 5 words, people’s guesses also mostly include them.

<!-- b000571 | caption | pages [22] -->
Figure 16: First guess

<!-- b000572 | caption | pages [22] -->
Figure 17: First two guesses

<!-- b000573 | prose | pages [22] -->
Considering the randomness of the first guess, if we consider the 20 words with the first two correct guesses greater than 0.15, 2 of them contain the same letter, “treat” and “tease”. most of these words also have 1 correct guess greater than 0.01, and the letter with the highest number of occurrences is still “a”, reaching 14 times The most frequent letter is “a”, with 14 times, followed by “t”, with 11 times. The possible reasons for this are roughly the same as for the first correct guesses.

<!-- b000574 | prose | pages [22] -->
• The hardest words

<!-- b000575 | prose | pages [22] -->
The word with the largest proportion of 7 or more tries is “parer” (0.48), far ahead of the second largest (0.26), “foyer”. Both words can be used in architecture to refer to a particular area or space within a larger building. They both also have similar etymological roots. Parer comes from the Latin word “parare” meaning “to prepare”, while foyer comes from the French “fouyer” meaning “hearth”.

<!-- b000576 | prose | pages [22] -->
• Misrepresentation or answer leakage

<!-- b000577 | prose | pages [22] -->
There may be cases of misrepresentation or answer leakage. For example, for a word like poise, the probability of getting it right on the first try is far less than 1% for both strategies in task2. It is hard to imagine that 2% or more of people guess correctly using only one guess.

<!-- b000578 | furniture | pages [23] -->
Team # 2318982

<!-- b000579 | furniture | pages [23] -->
Page 23 of 25

<!-- b000580 | prose | pages [23] -->
8

<!-- b000581 | heading | pages [23] -->
Sensitivity Analysis

<!-- b000582 | prose | pages [23] -->
In order to analyse the sensitivity of the Markov chain model to the parameters, we chose different values of C to calculate hatq(r)

<!-- b000583 | prose | pages [23] -->
k , and used the GPR model to make predictions for them. The selected C values are (1, 2, 3) respectively.

<!-- b000584 | caption | pages [23] -->
Figure 18: Sensitivity analysis

<!-- b000585 | prose | pages [23] -->
From Figure 18, we can conclude that C has little effect on the prediction accuracy of our model, which indicates that our model is robust and very reliable.

<!-- b000586 | prose | pages [23] -->
9

<!-- b000587 | heading | pages [23] -->
Modle Evaluation and Further Discussion

<!-- b000588 | prose | pages [23] -->
9.1

<!-- b000589 | heading | pages [23] -->
Strengths

<!-- b000590 | prose | pages [23] -->
• Novelty. We used concepts such as information entropy to model the initial distribution and transfer probabilities of Markov chains, proposed two game strategies and successfully estimated the proportion of use of the two strategies in historical data, and used time series prediction methods on them, eventually combining them to obtain the results.

<!-- b000591 | prose | pages [23] -->
• Interpretability. We use ARIMA and GPR models for time series forecasting, K-Prototypes methods for cluster analysis and Markov chains for modelling wordle games, all of which have a strong interpretability or deep statistical basis. The innovative part of the model also has a convincing structure.

<!-- b000592 | prose | pages [23] -->
9.2

<!-- b000593 | heading | pages [23] -->
Weaknesses

<!-- b000594 | prose | pages [23] -->
• Missing other potentially useful features. The model we built only uses part of the features of words, and there may be some unexplored features that can improve the model.

<!-- b000595 | prose | pages [23] -->
• Certain degree of arbitrariness in model designs.

<!-- b000596 | prose | pages [23] -->
We adopt an arbitrary mindset when designing part of our models.

<!-- b000597 | furniture | pages [24] -->
Team # 2318982

<!-- b000598 | furniture | pages [24] -->
Page 24 of 25

<!-- b000599 | prose | pages [24] -->
10 A Letter to The Puzzle Editor

<!-- b000600 | prose | pages [24] -->
Dear Sir or Madam:

<!-- b000601 | prose | pages [24] -->
Based on the file you provided, we have performed some interesting analyses of the data to answer the questions you have asked.

<!-- b000602 | prose | pages [24] -->
First, we have developed a time series model ARIMA, which is the result of a rigorous selection and iterative comparison of parameters. We are confident that this model will perform well in future forecasts. According to this model, the number of reported results on March 1, 2023 will be between 10517 and 27007, with the number 16529 being particularly likely. This shows the strong vitality of wordle. In this era of bombardment of various games and short videos, it is surprising that a game still has such a high attention span one year after its launch. Moreover, with some visualizations, we found that the number of wordle games gradually stabilized in Q3 2022 after a crazy growth in Q1 2022. This means that a significant number of players have gotten used to wordle games and made them part of their daily lives, rather than trying them once out of novelty.

<!-- b000603 | prose | pages [24] -->
Next, we found that the percentage of hard mode is related to the attributes of the solution word. We conjecture that players will use the information shared by the community to decide whether to turn on the Hard Mode. When players find that today’s wordle lacks challenge, Hard Mode is preferred. After all, the rules of Hard Mode make the way to approach the correct answer more singular.

<!-- b000604 | prose | pages [24] -->
We also develop a Markov chain to model the process of players playing wordle games and propose two game strategies. Finally, the prediction of the distribution of reported results at a future date is achieved by combining these results. Based on this model, the percentage distribution of the number of attempts for the word EERIE on March 1, 2023, showed a tendency to concentrate on three times and beyond, indicating the challenging nature of the word.

<!-- b000605 | prose | pages [24] -->
Ultimately, we categorized the words according to their attributes. As we conjectured, the resulting word categories imply information about the difficulty of the words.

<!-- b000606 | prose | pages [24] -->
Multi-syllabic, repeated-letter, objective, negative, and uncommon words are more difficult to guess than mono- syllabic, emotionally rich, and common ones. From this we predict that the word EERIE will be a great challenge for players, in line with the results of the Markov chain model we have developed.

<!-- b000607 | prose | pages [24] -->
In the process of solving the problem, we found some interesting features of this dataset. For example, the increase or decrease in the number of reported words may be due to the difficulty or ease of the word that day; words that are easy to guess correctly often contain common letters such as a, t; results misrepresentation or answer leakage may occur.

<!-- b000608 | prose | pages [24] -->
Many players say that wordle has become the first warm-up for their brains when they wake up. This is all due to your constant efforts to create a good gaming atmosphere and a harmonious gaming community. Here, everyone is able to share their achievements freely and happily without being dramatized. We sincerely thank you for your efforts and hope that our analysis will help you.

<!-- b000609 | prose | pages [24] -->
Sincerely,

<!-- b000610 | furniture | pages [24] -->
Team #2318982

<!-- b000611 | furniture | pages [25] -->
Team # 2318982

<!-- b000612 | furniture | pages [25] -->
Page 25 of 25

<!-- b000613 | heading | pages [25] -->
References

<!-- b000614 | references | pages [25] -->
[1] J. D. Cryer and K. S. Chan. Time Series Analysis. Time Series Analysis, 2005.

<!-- b000615 | references | pages [25] -->
[2] Renato Feres. Notes for math 450 matlab listings for markov chains. 2007.

<!-- b000616 | references | pages [25] -->
[3] Robin John Hyndman and George Athanasopoulos. Forecasting: Principles and Practice.

<!-- b000617 | references | pages [25] -->
OTexts, Australia, 2nd edition, 2018.

<!-- b000618 | references | pages [25] -->
[4] Carl Edward Rasmussen and Christopher K. I. Williams. Gaussian processes for machine

<!-- b000619 | references | pages [25] -->
learning (adaptive computation and machine learning). 2005.

<!-- b000620 | references | pages [25] -->
[5] Xiangxiang Yan. Using arima model to predict green area of park. Computer Science,

<!-- b000621 | references | pages [25] -->
47(S02):5, 2020.
