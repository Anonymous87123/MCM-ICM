# P-C-2023-2310767-2f955db2

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
2310767

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Uncover the Puzzle of Words : Evidence from Wordle

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Using up to six guesses, players are asked to predict a five-letter word in Wordle, which provides feedback after each guess. We all know that different words have vari- ous characteristics that could influence how well a player performs. In this regard, our team modeled and evaluated the provided data to arrive at some intriguing conclu- sions.

<!-- b000010 | prose | pages [1] -->
For task 1, after data preprocessing, we first use the ARIMA model to forecast the number of reported results and find that it can only capture the linear part. Second, we take the LSTM model to capture the information of the non-linear part. Finally, we combine them to form ARIMA-LSTM model, which yields more accurate predictions with an RMSE of 0.0432. We finally arrive at a prediction interval of [9614,43109] for March 1, 2023. Subsequently, we define five word attributes, such as syllable count and entropy, and analyze their correlation with the percentage of people reporting scores in the difficult mode through the Spearman correlation coefficient, and find them to be significantly correlated.

<!-- b000011 | prose | pages [1] -->
For task 2, we use five preferred word attributes and competition number to pre- dict the distribution of results using a stacking model that combines linear regression models (Ridge regression, Lasso regression) and tree models (XGBoost, LightGBM). We find that the stacking model improves the goodness of fit of the prediction results to 83.77%. Moreover, the MSE, RMSE, and MAE all indicate that the stacking model has a better capacity for learning. On March 1, 2023, the anticipated distribution of “EERIE” will be [1,2,3,4,5,6,X]=[0,0,9,18,26,37,10].

<!-- b000012 | prose | pages [1] -->
For task 3, we select seven additional word attributes to measure the words’ diffi- culty level, and then downscale the metrics by principal component analysis (PCA). We then use Gaussian Mixture Model(GMM) to cluster the words into three cate- gories: difficult, moderate and easy. To get the true difficulty of the words, we calculate the expected number of tries for each word, which is used to compare with the classi- fication results. It demonstrates that our model has a 67% accuracy rate. We explore interesting findings on the properties of the given words associated with each classi- fication from three different perspectives: entropy, number of letters and frequency. Finally, we classified "EERIE" into the category of "difficult" based on its attribute.

<!-- b000013 | prose | pages [1] -->
For task 4, we perform a visual analysis of the provided dataset and discover some intriguing properties in three areas: (1) the number of reported results and the percent- age of players who try the hard mode; (2) the distribution of tries; and (3) the frequency of letters in each position. These characteristics provide some interesting and feasible ideas for players to solve the problem.

<!-- b000014 | prose | pages [1] -->
We also conduct sensitivity analysis, which shows how different samples affect the word difficulty clustering model. And then the strengths and weaknesses of our model are summarized. Finally, a letter to the editor of the New York Times presenting the overall ideas and results of our paper is written in the end of paper.

<!-- b000015 | keywords | pages [1] -->
Keywords: ARIMA-LSTM Model; Correlation Analysis; Stacking; PCA; GMM;

<!-- b000016 | prose | pages [1] -->
Wordle;

<!-- b000017 | furniture | pages [2] -->
Page 2 of 25

<!-- b000018 | furniture | pages [2] -->
Team # 2310767

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1 Introduction

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
2 Assumptions and Symbols

<!-- b000023 | contents | pages [2] -->
4

<!-- b000024 | contents | pages [2] -->
2.1

<!-- b000025 | contents | pages [2] -->
Model Hypothesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
4

<!-- b000027 | contents | pages [2] -->
2.2

<!-- b000028 | contents | pages [2] -->
Symbols and Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [2] -->
4

<!-- b000030 | contents | pages [2] -->
3 Data Pre-processing

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
4 Task 1: Interval Prediction & Correlation Analysis

<!-- b000033 | contents | pages [2] -->
5

<!-- b000034 | contents | pages [2] -->
4.1

<!-- b000035 | contents | pages [2] -->
Prediction for the Number of Reported Results . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
5

<!-- b000037 | contents | pages [2] -->
4.1.1

<!-- b000038 | contents | pages [2] -->
Autoregressive Integrated Moving Average Model

<!-- b000039 | contents | pages [2] -->
. . . . . . . .

<!-- b000040 | contents | pages [2] -->
5

<!-- b000041 | contents | pages [2] -->
4.1.2

<!-- b000042 | contents | pages [2] -->
Building Predictive Models . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
5

<!-- b000044 | contents | pages [2] -->
4.1.3

<!-- b000045 | contents | pages [2] -->
ARIMA-LSTM Model

<!-- b000046 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
7

<!-- b000048 | contents | pages [2] -->
4.1.4

<!-- b000049 | contents | pages [2] -->
Analysis of Results . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
7

<!-- b000051 | contents | pages [2] -->
4.2

<!-- b000052 | contents | pages [2] -->
Construction of Word Attributes

<!-- b000053 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
8

<!-- b000055 | contents | pages [2] -->
4.3

<!-- b000056 | contents | pages [2] -->
Correlation Analysis

<!-- b000057 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
10

<!-- b000059 | contents | pages [2] -->
4.3.1

<!-- b000060 | contents | pages [2] -->
Spearman Correlation Coefficient

<!-- b000061 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
10

<!-- b000063 | contents | pages [2] -->
4.3.2

<!-- b000064 | contents | pages [2] -->
Correlation Coefficient Heat Map

<!-- b000065 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
10

<!-- b000067 | contents | pages [2] -->
4.3.3

<!-- b000068 | contents | pages [2] -->
Significance Analysis . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
11

<!-- b000070 | contents | pages [2] -->
5 Task 2: Prediction of Result Distribution Based on Stacking Algorithm

<!-- b000071 | contents | pages [2] -->
12

<!-- b000072 | contents | pages [2] -->
5.1

<!-- b000073 | contents | pages [2] -->
Stacking Method Model Fusion . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
12

<!-- b000075 | contents | pages [2] -->
5.2

<!-- b000076 | contents | pages [2] -->
Introduction to Predictive Models

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
13

<!-- b000079 | contents | pages [2] -->
5.2.1

<!-- b000080 | contents | pages [2] -->
Linear regression model . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
13

<!-- b000082 | contents | pages [2] -->
5.2.2

<!-- b000083 | contents | pages [2] -->
Tree Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
14

<!-- b000085 | contents | pages [2] -->
5.3

<!-- b000086 | contents | pages [2] -->
Prediction Results and Analysis . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
14

<!-- b000088 | contents | pages [2] -->
5.4

<!-- b000089 | contents | pages [2] -->
Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
15

<!-- b000091 | contents | pages [2] -->
6 Task 3: Gaussian Mixture-Based Classification Model

<!-- b000092 | contents | pages [2] -->
15

<!-- b000093 | contents | pages [2] -->
6.1

<!-- b000094 | contents | pages [2] -->
Word Attribute and Difficulty Index Establishment

<!-- b000095 | contents | pages [2] -->
. . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
15

<!-- b000097 | contents | pages [2] -->
6.2

<!-- b000098 | contents | pages [2] -->
Classification Model of Gaussian Mixture . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
16

<!-- b000100 | contents | pages [2] -->
6.3

<!-- b000101 | contents | pages [2] -->
Visual Analysis of Single Word Features . . . . . . . . . . . . . . . . . . .

<!-- b000102 | contents | pages [2] -->
17

<!-- b000103 | contents | pages [2] -->
6.4

<!-- b000104 | contents | pages [2] -->
Analysis of Classification Effect of Gaussian Mixture Model

<!-- b000105 | contents | pages [2] -->
. . . . . . .

<!-- b000106 | contents | pages [2] -->
18

<!-- b000107 | contents | pages [2] -->
6.5

<!-- b000108 | contents | pages [2] -->
Identification of Word Attributes Associated with Classification Results

<!-- b000109 | contents | pages [2] -->
19

<!-- b000110 | contents | pages [2] -->
7 Task 4: Interesting Features

<!-- b000111 | contents | pages [2] -->
20

<!-- b000112 | contents | pages [2] -->
8 Sensitivity Analysis

<!-- b000113 | contents | pages [2] -->
22

<!-- b000114 | contents | pages [2] -->
9 Model Advantages and Disadvantages

<!-- b000115 | contents | pages [2] -->
23

<!-- b000116 | contents | pages [2] -->
9.1

<!-- b000117 | contents | pages [2] -->
Advantages

<!-- b000118 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
23

<!-- b000120 | contents | pages [2] -->
9.2

<!-- b000121 | contents | pages [2] -->
Disadvantages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000122 | contents | pages [2] -->
23

<!-- b000123 | contents | pages [2] -->
References

<!-- b000124 | contents | pages [2] -->
24

<!-- b000125 | furniture | pages [3] -->
Page 3 of 25

<!-- b000126 | furniture | pages [3] -->
Team # 2310767

<!-- b000127 | heading | pages [3] -->
1 Introduction

<!-- b000128 | prose | pages [3] -->
Wordle is a daily puzzle offered by The New York Times that requires players to guess a five-letter real word within six attempts to solve, and is now available in more than 60 languages. Players receive feedback for each guess, specifically that the tile will change color to give feedback after the word is submitted. Players can play in either regular mode or hard mode. Hard mode requires that once the player has found the correct letters in a word, those letters must be used in subsequent guesses, which adds to the difficulty of the game.

<!-- b000129 | prose | pages [3] -->
As Wordle grew in popularity, The New York Times wanted us to analyze and model the data it provided.To address these issues, our team will take the following steps.

<!-- b000130 | prose | pages [3] -->
• Perform outlier processing on the data provided by COMAP official.

<!-- b000131 | prose | pages [3] -->
• An ARIMA-LSTM model was built to predict the number of reported results.

<!-- b000132 | prose | pages [3] -->
• Construct 12 word attributes and indicators reflecting the difficulty of the words.

<!-- b000133 | prose | pages [3] -->
• Develop models that can predict the distribution of reported results based on the given words at future dates using Stacking model fusion algorithms.

<!-- b000134 | prose | pages [3] -->
• Calculate mean square error (MSE), mean absolute error (MAE), and R2 as eval- uation metrics to verify the accuracy of the model.

<!-- b000135 | prose | pages [3] -->
• Classification and identification of solution words based on GMM clustering us- ing the constructed word difficulty metrics.

<!-- b000136 | prose | pages [3] -->
• Describe the number of player guesses, the position of the 26 letters appearing in the word, and other interesting properties we found.

<!-- b000137 | prose | pages [3] -->
• Write a letter for the editor of the New York Times that includes our prediction results and interesting findings.

<!-- b000138 | prose | pages [3] -->
Our modeling framework is shown in Figure 17.

<!-- b000139 | prose | pages [3] -->
Problem1：Predict the number of the reported results Problem3：Classify words by difficulty

<!-- b000140 | prose | pages [3] -->
word semantics ARIMA model history and new PCA Predict interval for the number attributes of a word phonetic of the reported results LSTM model Attributes of the word words’ difficulty GMM Three Level: The percentage of Hard Mode commonness rating entropy easy medium difficult number of letters frequency classify “EERIE” identify attributes The percentage of (1,2,3,4,5,6,X) number of vowels

<!-- b000141 | prose | pages [3] -->
1 try The number of reported results varied over time 2 tries a future word distribution of the … reported results The percent of Hard Mode over time Find some 6 tries a future date interesting things The distribution of the results (1,2,3,4,5,6,X) X tries linear models The proportion of the position of the 26 letters Stacking model in the word tree models predict “EERIE”

<!-- b000142 | prose | pages [3] -->
Problem2：Predict the distribution of the reported results Problem4：Some interesting features

<!-- b000143 | caption | pages [3] -->
Figure 1: Workflow

<!-- b000144 | furniture | pages [4] -->
Page 4 of 25

<!-- b000145 | furniture | pages [4] -->
Team # 2310767

<!-- b000146 | heading | pages [4] -->
2 Assumptions and Symbols

<!-- b000147 | heading | pages [4] -->
2.1 Model Hypothesis

<!-- b000148 | prose | pages [4] -->
To simplify our problem, we make the following basic assumptions, each of which is sufficiently reasonable.

<!-- b000149 | prose | pages [4] -->
• Assume that on January 1, 2023, March 1, 2023, there are no unexpected factors that will change the data substantially.

<!-- b000150 | prose | pages [4] -->
Since we can only use the data in the additional data file, which is up to December 31, 2022, we ignore the heat that this topic may bring to Wordle later or other influencing factors that may cause drastic fluctuations in the data.

<!-- b000151 | prose | pages [4] -->
• Assume that the scores that users report on Twitter are true and reliable.

<!-- b000152 | prose | pages [4] -->
If users report their scores on Twitter as false, the distribution of reported results in the dataset may be difficult to predict using only the properties of a given word for a given date.

<!-- b000153 | prose | pages [4] -->
• The disturbance term is assumed to follow an independent normal distribu- tion.

<!-- b000154 | heading | pages [4] -->
2.2 Symbols and Definitions

<!-- b000155 | caption | pages [4] -->
Table 1: Notations

<!-- b000156 | prose | pages [4] -->
Symbols Description

<!-- b000157 | prose | pages [4] -->
rt The number of results reported on day t H(X) The information entropy size of word X ρ Spearman rank correlation coefficient fr Word attribute: a measure of common usage in the coca dataset fn Word attribute: word frequency of SUBTLEX-US corpus ftn Word attribute: number of lexical labels fd Word property: consonant doubling fp Word property: phoneme length fvow Word property: number of vowels fc Word attribute: specificity rating λ GMM model parameters pk(di) Gaussian component density function µk Mean vector of the kth Gaussian component

<!-- b000158 | heading | pages [4] -->
3 Data Pre-processing

<!-- b000159 | prose | pages [4] -->
Since we can only use the official COMAP dataset ’Problem_C_Data_Wordle.xlsx’, and the given data is obtained by mining Twitter, there is a possibility of data anoma- lies, so we pre-processed this part of the data before building the model.

<!-- b000160 | prose | pages [4] -->
• Fill: We replace the outliers in Number of reported results with the average of the before and after data.

<!-- b000161 | furniture | pages [5] -->
Page 5 of 25

<!-- b000162 | furniture | pages [5] -->
Team # 2310767

<!-- b000163 | prose | pages [5] -->
• Reject: We remove the entire data where the sum of the distribution of the re- ported results deviates from 100%.

<!-- b000164 | prose | pages [5] -->
• We remove the entire word that has a number of letters not equal to 5, including "clen" and "tash".

<!-- b000165 | heading | pages [5] -->
4 Task 1: Interval Prediction & Correlation Analysis

<!-- b000166 | heading | pages [5] -->
4.1 Prediction for the Number of Reported Results

<!-- b000167 | heading | pages [5] -->
4.1.1 Autoregressive Integrated Moving Average Model

<!-- b000168 | prose | pages [5] -->
Since the data are time series and the amount of data is small, after considering various prediction models, we first chose the ARIMA model to predict the number of reported outcomes.

<!-- b000169 | heading | pages [5] -->
4.1.2 Building Predictive Models

<!-- b000170 | prose | pages [5] -->
In the ARIMA (p, d, q) model, AR is the autoregressive, p is the autoregressive term; MA is the moving average, q is the number of moving average terms, and d is the number of differences made when the time series becomes stationary. The model is based on the principle of converting a non-stationary series rt into a stationary series rt by differencing of order d. The regression is then performed with rt as the dependent variable and the lagged term of rt and the lagged terms of the random error terms at and at as the independent variables. For simplicity of writing, the latter denotes the number of reported results in terms of rt sequence.

<!-- b000171 | prose | pages [5] -->
Step 1. Sequence smoothing (determine the parameter d)

<!-- b000172 | prose | pages [5] -->
First of all, we perform a smoothness test on the time series rt of Number of re- ported results. As can be seen from figure2 below, the two time series have a clear trend and the autocorrelation coefficients decay relatively slowly. Also, we performed a unit root test and found that the series has a unit root.

<!-- b000173 | prose | pages [5] -->
(a) Sequence rt (b) Sequence ¯rt

<!-- b000174 | caption | pages [5] -->
Figure 2: Autocorrelation plot and Partial Autocorrelation plot of rt sequence

<!-- b000175 | prose | pages [5] -->
Therefore rt is a non-stationary series and needs to be further smoothed.

<!-- b000176 | furniture | pages [6] -->
Page 6 of 25

<!-- b000177 | furniture | pages [6] -->
Team # 2310767

<!-- b000178 | prose | pages [6] -->
Let ¯rt = rt-rt−1. After taking the first order difference, the smoothness test is per- formed on the differenced rt. From the following figure3, we can observe that the series after difference always fluctuate randomly around some value and there is no significant trend. The autocorrelation coefficient decays rapidly, and only the closely spaced series values have a significant effect. Also, the p-values of the unit root tests all converge to 0. Therefore, there is no unit root. rt is already a smooth series. Since we use the first-order difference method to obtain the smooth series, d = 1.

<!-- b000179 | caption | pages [6] -->
Figure 3: Time series plots of sequence ¯rt

<!-- b000180 | prose | pages [6] -->
Step 2. determination of p and q order.

<!-- b000181 | prose | pages [6] -->
The ARIMA(p, d, q) model takes the form:

<!-- b000182 | prose | pages [6] -->
¯rt = rt −rt−1 (1) p q X X ϕi¯rt−i + εt − ¯rt = ϕ0 + θiεt−i (2) i=1 i=1

<!-- b000183 | prose | pages [6] -->
where εt is a white noise sequence and p and q are non-negative integers. The Bayesian information criterion (BIC) is commonly used to determine the optimal order of the model, which is constructed based on the likelihood function. Based on histor- ical data, the BIC values of the model at different orders are calculated by computer programming loops to find the order p and q that minimizes the BIC, i.e., the opti- mal order of the model. After determining the optimal order, we perform parameter estimation and test that the data are found to be statistically significant.

<!-- b000184 | prose | pages [6] -->
Step 3. residual test

<!-- b000185 | prose | pages [6] -->
To determine the validity of the model, a residual test is also required, in which a white noise verification of the residual series εt is required. If the residuals are ran- domly normally distributed and not autocorrelated, the residual series approximates the white noise series, indicating a good model fit. We use the Ljung-Box statistic Q(m) to test the proximity of white noise:

<!-- b000186 | prose | pages [6] -->
m ˆρ2 X l Q(m) = T(T + 2) (3) T −l l=1

<!-- b000187 | prose | pages [6] -->
When the p-value of the test is greater than 0.05, it means that the residual series εt passes the test at 5% confidence level, i.e., the residual series is white noise. The test of the residual series of the data in this paper finds that it is not white noise, which means that there is still useful information in the residuals and the model needs to be modified to extract further information.

<!-- b000188 | furniture | pages [7] -->
Page 7 of 25

<!-- b000189 | furniture | pages [7] -->
Team # 2310767

<!-- b000190 | prose | pages [7] -->
The ARIMA model’s prediction of the reported outcome quantities lacks a residual term that is not accurate enough, which is especially evident in the prediction outside the original data. However, the ARIMA model is still able to capture the trends in the reported number of outcomes well, which means that it can predict the linear part of the reported number of outcomes well.

<!-- b000191 | heading | pages [7] -->
4.1.3 ARIMA-LSTM Model

<!-- b000192 | prose | pages [7] -->
The prediction results of the ARIMA model are not very volatile due to the fact that the residual part of this result is not well predicted reasonably well, so this pa- per further improves the prediction model by combining ARIMA with LSTM neural network.

<!-- b000193 | prose | pages [7] -->
LSTM neural network nonlinear prediction model Long short-term memory net- work (LSTM) is a modified recurrent neural network that can solve the long-term de- pendence problem and remembering information for a long time is actually their de- fault behavior.LSTM adds a memory unit to each neural unit in the hidden layer based on RNN: the information transmission band called "cell state "The LSTM uses struc- tures such as forgetting gates, input gates, and output gates to control the memorized information on the time series. In this way, LSTM can dig deeper into the underlying patterns between the data, making the prediction more accurate and reliable.

<!-- b000194 | prose | pages [7] -->
Therefore, in order to compensate the shortcomings of ARIMA model and further improve the prediction accuracy, we use a combined linear and nonlinear model for prediction. To this end, we firstly, based on the ARIMA prediction results and the actual number of reported results on the residual series of number of reports, which is used as the expected output of the LSTM neural network; secondly, the phase space reconstruction of the original data is performed, and the optimal number of reports is finally determined as 18; thirdly, the data reconstructed in the optimal order is used as the LSTM input; fourthly, the training set is input into the LSTM neural network , the learning modeling and prediction of the residual series test set is performed to obtain the ARIMA residual series prediction value; finally, the prediction results of ARIMA and LSTM neural network models are summed to obtain the final prediction results of the reported number of outcomes.

<!-- b000195 | heading | pages [7] -->
4.1.4 Analysis of Results

<!-- b000196 | prose | pages [7] -->
The prediction results are shown in Figure 4. The predicted value curve and the actual value curve still basically match, and the fluctuation trend remains consistent, and the model can accurately predict the inflection point, and the prediction results are better. And compared with the single model prediction results, the results are more volatile and more realistic in terms of the number of results reported in real life.

<!-- b000197 | furniture | pages [8] -->
Page 8 of 25

<!-- b000198 | furniture | pages [8] -->
Team # 2310767

<!-- b000199 | caption | pages [8] -->
Figure 4: ARIMA-LSTM Model - The number of results reported forecast results

<!-- b000200 | prose | pages [8] -->
In this section, the ARIMA model was used to predict the number of reported out- comes in the interval, and the LSTM model was used to predict the residual series to correct the short comings of the ARIMA model, and the final predicted value of the number of reported outcomes on March 1, 2023 was calculated to be 22577, with a prediction interval of [9614,43109].

<!-- b000201 | heading | pages [8] -->
4.2 Construction of Word Attributes

<!-- b000202 | prose | pages [8] -->
To explore whether any attributes of words affect the percentage of people report- ing scores in the difficult mode, we first looked for attributes of a number of represen- tative words. The following are the definitions of the attributes.

<!-- b000203 | prose | pages [8] -->
Number of syllables

<!-- b000204 | prose | pages [8] -->
The number of syllables reflects the number of constituent elements of a word. In this paper, we choose the method of counting syllables to measure word length. A syl- lable is the smallest unit that an individual can produce in a single breath and usually contains a vowel or vowels plus one or more consonants.

<!-- b000205 | prose | pages [8] -->
Word Class

<!-- b000206 | prose | pages [8] -->
A word class is a group of words that display the same formal properties. The data set given in the question contains seven main word classes: nouns, verbs, adjectives, adverbs, pronouns, conjunctions, and prepositions. Since pronouns, conjunctions and prepositions account for a small percentage, we categorize them as other.

<!-- b000207 | prose | pages [8] -->
Vocabulary usage index

<!-- b000208 | prose | pages [8] -->
Vocabulary usage index. Generally speaking, the more words are used in daily life, the easier it is for players to answer the puzzle, and conversely the rare words will increase the difficulty for players to pass the game.

<!-- b000209 | prose | pages [8, 9] -->
The Corpus of Contemporary American English (COCA) is a collection of the most frequently used words in the English-speaking world. It is extracted from a large cor- pus of words. A big data approach was used to automatically generate a word fre- quency list from various genres (most representative US newspapers, magazines, fic- tion, academic, and spoken language from 1990-2012), which is considered to be the most accurate word frequency list available today. Therefore, with the help of COCA, we defined the lexical common usage index as

<!-- b000210 | furniture | pages [9] -->
Page 9 of 25

<!-- b000211 | furniture | pages [9] -->
Team # 2310767

<!-- b000213 | prose | pages [9] -->
fi = ln(pi) (4)

<!-- b000214 | prose | pages [9] -->
where fi the lexical common usage index and pi is the order in COCA, and COCA is ordered by word frequency from most frequent to least frequent, the further back the word is, the less common it is.

<!-- b000215 | prose | pages [9] -->
The number of letters

<!-- b000216 | prose | pages [9] -->
The words given in the question are all composed of 5 letters, and having more than one repeated letter in a word can reduce the complexity of the word, which may reduce the difficulty of passing the game; it may also be due to the player’s inertia that the word will be composed of five different letters, and the repeated letters will increase the difficulty of the game instead.

<!-- b000217 | prose | pages [9] -->
Word frequency

<!-- b000218 | prose | pages [9] -->
We consider the utilization of vocabulary on the web, where we use the number of relevant information on Google. With the help of Brysbert New’s study of the SUBTLEX-US corpus, we obtained frequency counts for all the words in the dataset.

<!-- b000219 | prose | pages [9] -->
Information entropy

<!-- b000220 | prose | pages [9] -->
Information entropy can be used to describe the uncertainty of the source. In the game, Wordle will feedback the result of player input by changing the color of the tiles. The probability of each possible pattern to multiply the information content conveyed by this pattern to get the expected information content that a word can bring is also known as information entropy, and the higher the information entropy also means the higher the information content brought by this word in various situations. The statistics of the frequency of occurrence of 26 letters in English text from the COCA dataset are shown in the following figure5.

<!-- b000221 | caption | pages [9] -->
Figure 5: Frequency of 26 letters in the COCA dataset

<!-- b000222 | prose | pages [9] -->
When making a guess, the player will try to get the most information from each guess. Therefore an attempt will be made to cover the most high frequency letters in the first two attempts. For example, the combination of other + nails will cover 10 of the 11 most frequently occurring letters, and with a bit of luck some letters will be identified. Therefore, we use information entropy as a property of a word to describe the size of the information contained in the word. The greater the uncertainty of the word, the more information it contains, and the greater the information entropy. The specific formula is as follows.

<!-- b000223 | prose | pages [9, 10] -->
n X H(X) = − p (xi) log p (xi) (5) i=1 where X denotes the word as a random variable, P(x) denotes the output probability function of the word, and H(X) denotes the information entropy size of the word X.

<!-- b000224 | furniture | pages [10] -->
Page 10 of 25

<!-- b000225 | furniture | pages [10] -->
Team # 2310767

<!-- b000227 | heading | pages [10] -->
4.3 Correlation Analysis

<!-- b000228 | heading | pages [10] -->
4.3.1 Spearman Correlation Coefficient

<!-- b000229 | prose | pages [10] -->
We applied the method of correlation analysis to the five word attribute indicators constructed above and the percentage of scores reported that were played in Hard Mode, as measured by the spearman rank correlation coefficient, with the following idea.

<!-- b000230 | prose | pages [10] -->
The Spearman correlation coefficients of variables x and y were actually calcu- lated using the rank order of the two columns of numbers. By arranging the vari- ables x = {x1, x2, · · · , xn} in ascending or descending order to obtain the sorted se- ries a = {a1, a2, · · · , an} , the position of each element xi within the variable x in the series a is denoted as ri , which is called the element x. By arranging the variables y = {y1, y2, · · · , yn} in the same way, we get the rank series y = {y1, y2, · · · , yn}, and then we get the rank series y = {y1, y2, · · · , yn}. The rank series s corresponding to the variable y. The rank difference series d = {d1, d2, · · · , dn is obtained by subtracting the series r and each element in the series s corresponding to each other, and then substituting it into the Spearman rank correlation coefficient formula.

<!-- b000231 | prose | pages [10] -->
i=1 d2 ρ = 1 −6 P i (6) n (n2 −1) where: n is the number of samples, corresponding to the total amount of data involved in the ranking; ρ is the Spearman rank correlation coefficient between the variables of word frequency and the number of letters.

<!-- b000232 | heading | pages [10] -->
4.3.2 Correlation Coefficient Heat Map

<!-- b000233 | prose | pages [10] -->
The following graph depicts the relationship between the above metrics and the percentage of scores reported that were played in Hard Mode.

<!-- b000234 | prose | pages [10] -->
As can be seen from the figure6, most of the indicators do not correlate significantly with the proportion of players who choose the difficult mode, and only the number of vowels has a strong positive correlation with it.

<!-- b000235 | prose | pages [10] -->
Few attempts: 1 try, 2 tries, 3 tries Many tries: 5 tries, 6 tries, 7 or more tries(X)

<!-- b000236 | prose | pages [10] -->
The lexical commonness index, number of vowels and information entropy have a strong negative correlation with the proportion of guesses by few tries and a strong positive correlation with the proportion of multiple tries , with the opposite correlation for word frequency. This is consistent with our guess that the more common the word is in daily life and the more often it occurs, the easier it is to guess it by fewer attempts. The more informative a word is the less likely it is to be guessed within three attempts. Words with a higher number of vowels are more complex to pronounce and less likely to be game cleared after a small number of guesses.

<!-- b000237 | prose | pages [10, 11] -->
The number of letters has a strong positive correlation with the proportion of in few attempts and a strong negative correlation with the proportion of multiple attempts, probably due to human inertia that repetitive letters make the game more difficult and therefore more difficult to guess after a small number of attempts.

<!-- b000238 | furniture | pages [11] -->
Page 11 of 25

<!-- b000239 | furniture | pages [11] -->
Team # 2310767

<!-- b000241 | prose | pages [11] -->
There is a smaller correlation between word lexicality and number of guesses, prob- ably because players consider word lexicality less when guessing.

<!-- b000242 | caption | pages [11] -->
Figure 6: Heat Map of Correlation

<!-- b000243 | heading | pages [11] -->
4.3.3 Significance Analysis

<!-- b000244 | prose | pages [11] -->
For space reasons, we only give the correlation coefficients and significance levels of the indicators that were significantly correlated with the percentage of scores reported that were played in Hard Mode.

<!-- b000245 | prose | pages [11, 12] -->
From the above table, we can see that there is a significant correlation (significant in the two-tailed test) between the five indicators for the number of syllables, the num- ber of letters, common word index, word frequency and information entropy and the proportion of guessed or unsolvable puzzles (X) in one attempt, two attempts, three attempts, five attempts and six attempts, which is consistent with the results of the heat map analysis. In contrast, none of the four indicators was significantly correlated with the proportion of guesses made at four attempts. The proportion of guesses at four attempts can be seen as the transition point, and often these four indicators are oppo- site in sign to the correlation coefficients between the proportion of guesses at less than four attempts and the proportion of guesses at more than four attempts.

<!-- b000246 | furniture | pages [12] -->
Page 12 of 25

<!-- b000247 | furniture | pages [12] -->
Team # 2310767

<!-- b000249 | caption | pages [12] -->
Table 2: Spearman’s correlation coefficient for each variable

<!-- b000250 | prose | pages [12] -->
x com.rating frequency num. of letters num. of vowels entropy

<!-- b000251 | prose | pages [12] -->
1try -0.231*** 0.298*** 0.208*** -0.243*** -0.192*** 2tries -0.264*** 0.355*** 0.424*** -0.276*** -0.464*** 3tries -0.206*** 0.242*** 0.347*** -0.207*** -0.428*** 4tries 0.055 -0.066 -0.005 0.082 0.089 5tries 0.208*** -0.261*** -0.368*** 0.247*** 0.443*** 6tries 0.189*** -0.202*** -0.263*** 0.163*** 0.317*** Xtries 0.212*** -0.201*** -0.164*** 0.094*** 0.231***

<!-- b000252 | heading | pages [12] -->
5 Task 2: Prediction of Result Distribution Based on Stack-

<!-- b000253 | prose | pages [12] -->
ing Algorithm

<!-- b000254 | prose | pages [12] -->
In order to predict the distribution of reported results at a given future date and future word, we train seven stacking models to predict the specific proportion of each number of attempts (1,2,3,4,5,6,X) separately, and then normalize their corresponding predicted values as the final distribution prediction.

<!-- b000255 | prose | pages [12] -->
We built two linear regression models, Ridge and Lasso regression, and two tree models, XGBoost and LightGBM, based on the preferred word attributes (including ranking of commonness, word frequency, number of letters, number of vowels, and information entropy) and competition number, respectively, for comparison analy- sis, and The models were fused by integrating primary learners using the Stacking method, and the fused results have more accurate and efficient prediction effects.

<!-- b000256 | prose | pages [12] -->
Predict the percentage Predict the predicted value_1 of 1 try percentage of 1 try

<!-- b000257 | prose | pages [12] -->
Predict the percentage Predict the predicted value_2 of 2 tries percentage of 1 try Seven Predict separately Normalization The distribution Stacking Stacking of the reported … … Model Models results Predict the percentage Predict the predicted value_6 of 6 tries percentage of 1 try

<!-- b000258 | prose | pages [12] -->
Predict the percentage Predict the predicted value_7 of X tries percentage of 1 try

<!-- b000259 | caption | pages [12] -->
Figure 7: Distribution prediction flow chart

<!-- b000260 | heading | pages [12] -->
5.1 Stacking Method Model Fusion

<!-- b000261 | prose | pages [12, 13] -->
The Stacking method is designed to reduce the generalization error of the models and is essentially a hierarchical structure of "stacking", which has the advantage of improving the accuracy of the prediction results. In this paper, a two-stage Stacking method is applied, and the steps are as follows.

<!-- b000262 | furniture | pages [13] -->
Page 13 of 25

<!-- b000263 | furniture | pages [13] -->
Team # 2310767

<!-- b000265 | prose | pages [13] -->
Layer 1.

<!-- b000266 | prose | pages [13] -->
1) In this paper, we split the data provided by the question into a training set and a test set in the ratio of 4:1, containing 286 and 71 data, respectively. 2) The training set is trained using Ridge regression, Lasso regression, XGBoost algorithm and Light- GBM algorithm. 3) Predict the data provided by the question using the four models completed in Step 2 and save the results.

<!-- b000267 | prose | pages [13] -->
Layer 2.

<!-- b000268 | prose | pages [13] -->
1) The four prediction result datasets from step 3 of the first layer are used as new training set features, and together with the actual features of the data provided by the topic, the XGBoost algorithm with higher single model evaluation criteria in the first layer is selected as the metamodel for secondary training prediction. 2) The final results are obtained by predicting the validation set of the data provided by the topic with the trained XGBoost algorithm.

<!-- b000269 | prose | pages [13] -->
training Classification models prediction

<!-- b000270 | prose | pages [13] -->
Predictions

<!-- b000271 | prose | pages [13] -->
Final �� prediction

<!-- b000272 | caption | pages [13] -->
Figure 8: Stacking Model Fusion Flowchart

<!-- b000273 | heading | pages [13] -->
5.2 Introduction to Predictive Models

<!-- b000274 | heading | pages [13] -->
5.2.1 Linear regression model

<!-- b000275 | prose | pages [13] -->
Ridge regression adds the least squares of the second-order regular term to the loss function, also called L2 parametrization, which has the effect of dimensionality reduc- tion, and also limits the matching of the model parameters to the abnormal samples and deals with the highly correlated data sets, thus improving the fitting accuracy of the model to most normal samples. Our team used RidgeCV to adjust the regulariza- tion strength alpha to achieve a better fit at alpha 14.

<!-- b000276 | prose | pages [13, 14] -->
Lasso regression is similar to the above mentioned Ridge regression in that it also deals with the co-linearity of the feature variables by constructing a penalty function. However, compared with Ridge regression, Lasso regression can compress the coeffi- cients of relatively insignificant characteristic variables to zero by changing the penalty term from L2 to L1 parametric, so as to eliminate the variables; whereas Ridge regres- sion only compresses the coefficients of characteristic variables to a certain extent and retains all variables of the regression model.

<!-- b000277 | furniture | pages [14] -->
Page 14 of 25

<!-- b000278 | furniture | pages [14] -->
Team # 2310767

<!-- b000280 | heading | pages [14] -->
5.2.2 Tree Model

<!-- b000281 | prose | pages [14] -->
The core idea of XGBoost regression model is to calculate the information gain to reflect the degree of information uncertainty reduction of each feature variable. It is an optimized distributed gradient boosting library designed to be efficient, flexible and portable.

<!-- b000282 | prose | pages [14] -->
The LightGBM model is a decision tree algorithm that traverses the data to find the optimal splitting point based on the discrete values of the histogram. Like the XGBoost algorithm, it is an efficient implementation of GBDT, and is similar to XGBoost in that it uses the negative gradient of the loss function as a residual approximation to the current decision tree to fit a new decision tree.

<!-- b000283 | heading | pages [14] -->
5.3 Prediction Results and Analysis

<!-- b000284 | prose | pages [14] -->
The reported results of the five models selected in this paper are shown in Fig9. The reported results of the linear model are shown in Lasso regression, and the regression results of the tree model are shown in LightGBM algorithm.

<!-- b000285 | prose | pages [14] -->
(a) Lasso regresion result (b) LightGBM result

<!-- b000286 | caption | pages [14] -->
Figure 9: Average Rating Value over the years

<!-- b000287 | caption | pages [14] -->
Figure 10: Stacking model result

<!-- b000288 | prose | pages [14] -->
The prediction results show that the linear model is more accurate in predicting data around the mean, while the tree model is more accurate in predicting the dis- tribution of extreme values, and the Stacking fusion model retains the advantages of both models and compensates each other’s shortcomings. The model prediction ac- curacy is higher. In conclusion, the forecasting effect of the Stacking fusion model is better. The ratio of predicted EERIE on March 1, 2023 is obtained as [1,2,3,4,5,6,X] = [0,0,9,18,26,37,10], respectively.

<!-- b000289 | furniture | pages [15] -->
Page 15 of 25

<!-- b000290 | furniture | pages [15] -->
Team # 2310767

<!-- b000291 | heading | pages [15] -->
5.4 Model Evaluation

<!-- b000292 | prose | pages [15] -->
In this study, the cross-validation method was used to verify the accuracy of each model, and the mean square error (MSE), root mean square error (RMSE), mean ab- solute error (MAE), and R2 generated from the cross-validation results were used as evaluation indicators for the accuracy of the estimated and validated models. The larger the R2 corresponding to the estimation model, the smaller the MSE, RMSE and MAE indicate the higher the prediction accuracy of the model. The following table shows the model prediction results of various models with four indicators: (with "2 tries" as the dependent variable)

<!-- b000293 | caption | pages [15] -->
Table 3: Spearman’s correlation coefficient for each variable

<!-- b000294 | prose | pages [15] -->
R2 MSE RMSE MAE

<!-- b000295 | prose | pages [15] -->
Lasso 2.3771 1.5417 1.0727 0.6847 Ridge 2.1292 1.4592 0.9909 0.7151 XGBoost 1.9289 1.3888 0.9186 0.7856 LightGBM 1.8562 1.3642 0.9045 0.8062 Stacking 1.6768 1.2949 0.8623 0.8377

<!-- b000296 | prose | pages [15] -->
Compared with the single model above, this paper finds that the R2 of the Stacking model improves, and MSE, RMSE, and MAE all decrease in varying degrees. However, due to the variability and unpredictability of player behavior, as well as the possibil- ity of unexpected events or external factors affecting player participation and perfor- mance, even the Stacking fusion model still has shortcomings in predicting the distri- bution of reported outcomes.

<!-- b000297 | heading | pages [15] -->
6 Task 3: Gaussian Mixture-Based Classification Model

<!-- b000298 | prose | pages [15] -->
To solve the third problem, we first selected seven English word attributes and fea- tures to measure the difficulty level of the words. The English words in the dataset were classified by visualization analysis and clustering of GMM through principal component analysis (PCA) for dimensionality reduction of the metrics. Finally, the classification results were compared with the real difficulty of the words, and the re- sults showed that the real classification results overlapped highly with our GMM clus- tering results, confirming that the word features selected in this paper have a close relationship with word difficulty.

<!-- b000299 | heading | pages [15] -->
6.1 Word Attribute and Difficulty Index Establishment

<!-- b000300 | prose | pages [15] -->
Dimension 1: Words

<!-- b000301 | prose | pages [15, 16] -->
Frequent use (fr) Commonness is used to measure how often a word is used in daily life. This indicator is calculated by taking the logarithm of the ranking order of the common words of the word in the coca dataset, with higher values indicating a lower ranking, i.e., less common. Word frequency (fn) We considered the frequency of word usage and obtained frequency counts for all words in the dataset with the help of Brysbert New’s study of the SUBTLEX-US corpus. Number of letters contained (fd) We consider that a word is made up of several letters, and letters that appear multiple times are not counted repeatedly.

<!-- b000302 | furniture | pages [16] -->
Page 16 of 25

<!-- b000303 | furniture | pages [16] -->
Team # 2310767

<!-- b000305 | prose | pages [16] -->
Dimension 2: Phonology

<!-- b000306 | prose | pages [16] -->
Phoneme length (fp) Many English words contain unaccented consonant letters, thus making them more difficult to remember. Therefore, we collected the phonetic length of each word to express the number of silent letters that may increase the dif- ficulty of word memorization. By applying the CMU pronunciation dictionary data from NLTK, we obtained the phonetic sounds of all words.

<!-- b000307 | prose | pages [16] -->
Number of vowels (fvow) Beinborn et al used the ratio of vowels to consonants to find that words with very high and very low vowel ratios are more likely to cause spelling errors and are more difficult to spell than words with moderate vowel ratios. We directly introduce the number of vowels as a second phonological feature.

<!-- b000308 | prose | pages [16] -->
Dimension 3: Semantics

<!-- b000309 | prose | pages [16] -->
Concreteness rating (fc) Concreteness ratings measure the degree to which the con- cept represented by a word is associated with a perceptible entity. According to Paivio’s dual-coding theory, concrete words are easier to remember than abstract words be- cause they activate perceptual memory codes in addition to verbal codes, thus making concrete words relatively less difficult. We refer to Brysbaert’s findings to give the concreteness ratings of all words in the dataset given by the question.

<!-- b000310 | prose | pages [16] -->
Number of lexical labels (ftn) A word may have several lexical properties, which means that it can be used in a variety of contexts, and the more widely it is used the less difficult it is. NLTK, the Natural Language Toolkit, is what we use to label lexical properties.

<!-- b000311 | heading | pages [16] -->
6.2 Classification Model of Gaussian Mixture

<!-- b000312 | prose | pages [16] -->
In order to classify solution words, we built a word classification model based on Gaussian mixture model (GMM).

<!-- b000313 | prose | pages [16] -->
Gaussian mixture model (GMM) is a general probabilistic model. In general, as long as the Gaussian number is large enough, it can effectively model the continu- ous probability distribution of multidimensional vectors, and is therefore suitable for characterizing the semantic distribution of words and thus classifying them.

<!-- b000314 | prose | pages [16] -->
A Gaussian mixture model is a weighted combination of a series of Gaussian distri- butions. A Gaussian mixture density function consisting of M Gaussian components is a linear weighted sum of M Gaussian density functions.

<!-- b000315 | prose | pages [16] -->
M X p (di | λ) = wkpk (di) (7) k=1

<!-- b000316 | prose | pages [16] -->
In the above equation λ is the GMM model parameter ,pk(di)is the Gaussian com- ponent density function,wk is the weight of each Gaussian component.

<!-- b000317 | prose | pages [16] -->
  1 −1 2 (di −µk)T Σ−1 k (di −µk) pk(di) = 2 exp (8) 1 D 2 |Σk| (2π)

<!-- b000318 | prose | pages [16, 17] -->
Here µk is the mean vector of the kth Gaussian component , P k is the corresponding covariance matrix , and D is the dimension of the eigenvector . Thus, the GMM model can be represented by the following set of parameters :

<!-- b000319 | furniture | pages [17] -->
Page 17 of 25

<!-- b000320 | furniture | pages [17] -->
Team # 2310767

<!-- b000322 | prose | pages [17] -->
λ = {wk, µk, Σk} , k = 1, 2, · · · , M (9)

<!-- b000323 | prose | pages [17] -->
The use of GMM to classify words by word feature distribution is based on two starting points: 1) the Gaussian component of GMM can describe the distribution of certain word vectors; 2) the linear weighted Gaussian density function can approxi- mate the probability distribution of arbitrary shapes, and we are uncertain about the probability distribution of the data, so GMM is chosen to classify words.

<!-- b000324 | heading | pages [17] -->
6.3 Visual Analysis of Single Word Features

<!-- b000325 | prose | pages [17] -->
For the features introduced in the previous section, we first perform power oper- ations on the features such as consonant doubling fd, tag length ftn, phonetic fp, and specificity rating fc to obtain a better representation. Similarly, we take logarithms for the raw data of frequency fn. In addition, for word-to-vector features, we use Word2Vec’s Gensim implementation to convert all words into a 100-dimensional vec- tor as fvec. Thus, we combine all 7 features into a 107-dimensional feature vector (100 dimensions from word-to-vector feature fvec + 7 dimensions of 7 features, fr...fc).

<!-- b000326 | prose | pages [17] -->
Difficultyfeatures = (fr, fn, ftn, fd, fp, fvow, fc, fvec) (10)

<!-- b000327 | prose | pages [17] -->
For intuitive analysis, we first downscaled the features to visualize the relationship between all features and difficulty. Therefore, principal component analysis (PCA) was used to reduce the dimensionality of the f features from 107 to 3 dimensions in Figure 12.

<!-- b000328 | prose | pages [17] -->
4.00000 4.00000 2.00000 Difficulty Difficulty Difficulty level level level difficult difficult difficult middle middle 1.00000 middle easy easy easy 2.00000 2.00000 .00000 factor 3 factor 2 factor 3 -1.00000 .00000 .00000 -2.00000

<!-- b000329 | prose | pages [17] -->
-3.00000 -2.00000 -2.00000

<!-- b000330 | prose | pages [17, 18] -->
-4.00000 -4.00000 -3.00000 -2.00000 -1.00000 .00000 1.00000 2.00000 -4.00000 -2.00000 .00000 2.00000 4.00000 -4.00000 -2.00000 .00000 2.00000 4.00000 factor 1 factor 1 factor 2 ((a)) factor1 and factor2 ((b)) factor1 and factor3 ((c)) factor2 and factor3 Difficulty level 4.00000 difficult middle easy

<!-- b000331 | caption | pages [17] -->
Figure 11: Two-dimensional graph of clustering results

<!-- b000332 | furniture | pages [18] -->
Page 18 of 25

<!-- b000333 | furniture | pages [18] -->
Team # 2310767

<!-- b000335 | prose | pages [18] -->
2.00000

<!-- b000336 | prose | pages [18] -->
factor 1 .00000

<!-- b000337 | prose | pages [18] -->
-2.00000

<!-- b000338 | prose | pages [18] -->
-4.00000 -4.00000 -2.00000 -2.00000 .00000 .00000 2.00000 2.00000 factor 2 4.00000 factor 3

<!-- b000339 | caption | pages [18] -->
Figure 12: Three-dimensional graph of clustering results

<!-- b000340 | prose | pages [18] -->
In this figure, the three main axes represent the three common factors we obtained using factor analysis. The different colors indicate the different difficulty levels. In- terestingly, Mummy, a word that appears a lot in everyday life, is classified in the dif- ficulty category, which we believe is due to the presence of three identical letters "m" (which is hard to think of) making the word much more difficult. Although the first three principal components of the feature retain only about 72.8% of the variance, we can easily find that almost all words are grouped based on their difficulty level. This confirms that the features we have chosen are indeed closely related to the difficulty level.

<!-- b000341 | heading | pages [18] -->
6.4 Analysis of Classification Effect of Gaussian Mixture Model

<!-- b000342 | prose | pages [18] -->
To further classify the data, we used GMM to cluster the words. We called the Python scikit-learn package for GMM to train all the data and plotted the covariance of the data by the mean and covariance values. The results show that the covariances cover most of the data in their corresponding clusters. The total word counts of the GMM clusters for difficult, medium and easy words were 105, 100 and 150, respec- tively.

<!-- b000343 | prose | pages [18] -->
To explore the clustering effect in more detail, we defined the difficulty of each word based on the expected number of guesses needed to hit the word and compared it with the classification results, and the true difficulty of the word was defined as follows.

<!-- b000344 | prose | pages [18] -->
n X j ∗pj E(diffi) = (11) j=1

<!-- b000345 | prose | pages [18] -->
where E(diffi) is the expected difficulty of the word, j is the number of times the word is guessed after j attempts, and if it is not guessed, we set the value of j to 7; pj is the proportion of guesses made in j attempts, and similarly p7 is the proportion of puzzles that cannot be solved. Finally, we sorted the expected difficulty in descending order, taking the trichotomies of difficulty and classifying them into three categories: difficult, moderate, and easy, to facilitate comparison with our prediction results.

<!-- b000346 | prose | pages [18, 19] -->
In the three leftmost bars of the figure 16, we can find that the number of words with difficulty level 1 is the highest in this cluster. Accordingly, we named it "pre- dicted difficulty level 1", which corresponds to the green area at the bottom right of the figure above. The rightmost set of bars in Figure 2 has the highest number of words in difficulty level 3, and therefore corresponds to the purple area at the bottom left of the figure above, which is "predicted difficulty level 3". For the middle set of bars, since this cluster overlaps with the other two clusters, the prediction is not as good as for the difficulty level and the easy level, and we only get an accuracy of 60% for the clustering of words at the medium level of difficulty, i.e., the number of words with the same pre- diction level as the difficulty label as a percentage of the total number of words in each cluster. The middle bar corresponds to the red area at the top of the above figure13.

<!-- b000347 | furniture | pages [19] -->
Page 19 of 25

<!-- b000348 | furniture | pages [19] -->
Team # 2310767

<!-- b000350 | caption | pages [19] -->
Figure 13: Distribution of prediction clusters with different difficulty levels

<!-- b000351 | heading | pages [19] -->
6.5 Identification of Word Attributes Associated with Classification

<!-- b000352 | heading | pages [19] -->
Results

<!-- b000353 | prose | pages [19] -->
To identify the attributes of a given word associated with each category, we ex- plored whether word attributes such as information entropy, The number of letters, and word frequency differed at different prediction difficulty levels.

<!-- b000354 | prose | pages [19] -->
Information entropy perspective

<!-- b000355 | prose | pages [19] -->
As shown in the figure14, the information entropy contained in words with diffi- culty level one is much smaller than that of words with higher difficulty levels, i.e., the higher the difficulty level of a word, the greater the information entropy and the more information it contains. This conclusion is consistent with the results of our previous analysis. The higher information entropy also means that the word brings higher in- formation content in various situations, and therefore the higher the difficulty of the word.

<!-- b000356 | caption | pages [19] -->
Figure 14: Information entropy of different difficulty levels

<!-- b000357 | furniture | pages [20] -->
Page 20 of 25

<!-- b000358 | furniture | pages [20] -->
Team # 2310767

<!-- b000359 | prose | pages [20] -->
The number of letters perspective

<!-- b000360 | prose | pages [20] -->
As can be seen from the figure15, difficulty level one and difficulty level two con- tain words with five non-repeating letters, while difficulty level three contains 26% of words with two repeating letters and even 2% of words with three repeating letters, in- dicating that the presence of repeating letters in words does have an increasing effect on the difficulty of words.

<!-- b000361 | prose | pages [20] -->
((a)) 1 ((b)) 2 ((c)) 3

<!-- b000362 | caption | pages [20] -->
Figure 15: The number of letters by Difficulty Level

<!-- b000363 | prose | pages [20] -->
Word frequency perspective

<!-- b000364 | prose | pages [20] -->
The figure16 shows that words in difficulty level one appear more frequently in the database, while words in difficulty level three mostly appear between 0 and 7000 in the database, which shows that the more frequently words appear in daily life, the easier they are to be recognized, and the opposite is more difficult. This is consistent with our prediction results.

<!-- b000365 | caption | pages [20] -->
Figure 16: Word frequency of different difficulty levels

<!-- b000366 | heading | pages [20] -->
7 Task 4: Interesting Features

<!-- b000367 | prose | pages [20, 21] -->
From the figure17, we find that the number of reported results shows a rapid growth trend in January and February 2022, and from March onwards the heat of Wordle slowly decreases, and the number of reported results shows a decreasing trend of re- cession type. After August 2022, the number of reported results does not change much, showing a fluctuating decline. The number of players who are willing to try the dif- ficult mode tends to increase over time, with three large fluctuations, illustrating the unpredictability and unpredictability of player behavior, as well as the unpredictable impact of unexpected events or external factors on players’ participation in the game.

<!-- b000368 | furniture | pages [21] -->
Page 21 of 25

<!-- b000369 | furniture | pages [21] -->
Team # 2310767

<!-- b000371 | prose | pages [21] -->
(a) Number of reported results (b) Hard Mode ratio

<!-- b000372 | caption | pages [21] -->
Figure 17: Player information time series trend

<!-- b000373 | prose | pages [21] -->
We plotted a line graph of the percentage of guesses or the percentage of puzzles that could not be solved (X) after 1-6 attempts and found that the percentage of guesses after 4 attempts was usually higher than the other percentages, followed by the per- centage of guesses after 3 attempts, while the percentage of guesses in one attempt was almost equal to 0 (the percentage of results with 0 guesses in one attempt was 61.21% of the total results), and a few people were able to guess on the second (the average percentage of second guesses was 5.84%). In addition, the percentage of people who could not solve the puzzle (X) was more volatile, with a mean value of 2.80%, but a maximum value (word "parer") of 48%, indicating that there are words in the data that are above the ability level of most people, which makes the Wordle game more challenging.

<!-- b000374 | caption | pages [21] -->
Figure 18: Proportion of correct guesses or unable to solve the puzzle after 1-6 attempts (X) (in

<!-- b000375 | prose | pages [21] -->
ascending order of proportion of correct guesses in five attempts)

<!-- b000376 | prose | pages [21] -->
We explored the proportion of the 26 letters appearing in the positions of the words in the dataset, and the results showed that the five letters b, f, j, q, and s appear more frequently as the first letters of words, while d, l, t, and y appear more frequently at the end of words, and q appears only at the beginning and end of words. s appears most frequently in the position of the first letter, d appears most frequently at the last letter, and the middle three letters are n, o, and e appear most frequently. This can provide some interesting and feasible ideas for players to guess words and letters that are placed in words but misplaced.

<!-- b000377 | furniture | pages [22] -->
Page 22 of 25

<!-- b000378 | furniture | pages [22] -->
Team # 2310767

<!-- b000379 | caption | pages [22] -->
Figure 19: Proportion of the 26 letters appearing in words

<!-- b000380 | heading | pages [22] -->
8 Sensitivity Analysis

<!-- b000381 | prose | pages [22] -->
To test the reasonableness and generalizability of our GMM classification model, we expand the training samples to observe the changes in classification accuracy. The training sample in this paper comes from a word set W, which has 11998 English words that have been classified into three difficulty levels: easy, medium and difficult. Each difficulty level contains about 4000 words. Therefore we selected different training sets for words with letter numbers 4, 5, 6, 7, and 8. The number of words in each training set fluctuates up and down from 400, consistent with the amount of data provided by the question. Thus we get a total of 25 accuracies for different training sets of different words. We compared the difficulty labels calculated by the clustering model with the difficulty labels of the word set W. The accuracy rates were calculated according to the method described above.

<!-- b000382 | prose | pages [22] -->
0.8

<!-- b000383 | prose | pages [22] -->
0.6 Accuracy rate 0.4

<!-- b000384 | prose | pages [22] -->
0.2

<!-- b000385 | prose | pages [22] -->
0

<!-- b000386 | prose | pages [22] -->
set1 set2 8 set3 7 set4 6 set5 5 Train set 4 Word length

<!-- b000387 | caption | pages [22] -->
Figure 20: Accuracy of clustering for words containing different number of letters

<!-- b000388 | prose | pages [22, 23] -->
As can be seen from the figure20, since the clustering model in this paper is trained on data containing words with five letters, the five training sets of words containing five letters show better classification results, followed by the training sets of words containing four or six letters. The classification accuracy decreases as the number of letters of words increases, especially for the training set 5 of words with 8 letters, which has an accuracy of only 49.31%. However, the accuracy of words with the number of letters around 5 all fluctuate slightly above and below 60%, indicating that our GMM classification model is robust and suitable for classifying words containing 5 letters with difficulty.

<!-- b000389 | furniture | pages [23] -->
Page 23 of 25

<!-- b000390 | furniture | pages [23] -->
Team # 2310767

<!-- b000392 | heading | pages [23] -->
9 Model Advantages and Disadvantages

<!-- b000393 | heading | pages [23] -->
9.1 Advantages

<!-- b000394 | prose | pages [23] -->
• By combining the ARIMA model with the LSTM model, both linear and non- linear cases are taken into account, thus focusing on both trend changes and volatility changes in the number of reported outcomes.

<!-- b000395 | prose | pages [23] -->
• The ARIMA-LSTM model can simply use the historical data of the number of reported outcomes themselves to predict their future trends and give the size of the prediction interval, which is more in line with real-life fluctuations than traditional mathematical and statistical methods.

<!-- b000396 | prose | pages [23] -->
• Based on Stacking model fusion algorithm combines multiple models to predict the distribution of results, which can give full play to the advantages of each model, has stronger learning ability and gets better prediction results, and pro- vides a new idea for modeling.

<!-- b000397 | prose | pages [23] -->
• According to the results of sensitivity analysis, the GMM clustering model we established has excellent classification and recognition of the difficulty of words with 4-6 letters, and the model is applicable to a wide range of objects and has a high accuracy rate.

<!-- b000398 | heading | pages [23] -->
9.2 Disadvantages

<!-- b000399 | prose | pages [23] -->
• There are more computational indicators, which are tedious, and the model run- ning speed needs to be improved.

<!-- b000400 | prose | pages [23] -->
• Due to time constraints, our description of word attributes and difficulty metrics may not be comprehensive enough, and more word attributes and larger English word difficulty data sets can be used for training in the future.

<!-- b000401 | furniture | pages [24] -->
Page 24 of 25

<!-- b000402 | furniture | pages [24] -->
Team # 2310767

<!-- b000403 | heading | pages [24] -->
References

<!-- b000404 | references | pages [24] -->
[1] Brysbaert, M., Warriner, A. B., Kuperman, V. (2014). Concreteness ratings for 40

<!-- b000405 | references | pages [24] -->
thousand generally known English word lemmas. Behavior Research Methods,

<!-- b000406 | references | pages [24] -->
46(3), 904–911.

<!-- b000407 | references | pages [24] -->
[2] Paivio, A. (2013). Dual Coding Theory, Word Abstractness, and Emotion: A Crit-

<!-- b000408 | references | pages [24] -->
ical Review of Kousta et al. (2011). Journal of Experimental Psychology: General,

<!-- b000409 | references | pages [24] -->
142, 282–287.

<!-- b000410 | references | pages [24] -->
[3] Lisa Beinborn, Torsten Zesch, and Iryna Gurevych, “Predicting the Spelling Dif-

<!-- b000411 | references | pages [24] -->
ficulty of Words for Language Learners,” Proceedings of the 11th Workshop on

<!-- b000412 | references | pages [24] -->
Innovative Use of NLP for Building Educational Applications, pp. 73–83, 2016.

<!-- b000413 | references | pages [24] -->
[4] Brysbaert, M., New, B. (2009). Moving beyond Kucera and Francis: A critical eval-

<!-- b000414 | references | pages [24] -->
uation of current word frequency norms and the introduction of a new and im-

<!-- b000415 | references | pages [24] -->
proved word frequency measure for American English. Behavior Research Meth-

<!-- b000416 | references | pages [24] -->
ods, 41(4), 977–90.

<!-- b000417 | references | pages [24] -->
[5] A survey of trust and reputation systems for online service provision[J] . Decision

<!-- b000418 | references | pages [24] -->
Support Systems . 2005 (2).

<!-- b000419 | references | pages [24] -->
[6] Hunter M. Breland, “Word Frequency and Word Difficulty: A Comparison of

<!-- b000420 | references | pages [24] -->
Counts in Four Corpora.” Psychological Science, vol. 7(2), pp. 96–99, 1996.

<!-- b000421 | references | pages [24] -->
[7] Edward Loper, and S. Bird, “NLTK: the Natural Language Toolkit,” ETMTNLP

<!-- b000422 | references | pages [24] -->
’02 Proceedings of the ACL-02 Workshop on Effective tools and methodologies

<!-- b000423 | references | pages [24] -->
for teaching natural language processing and computational linguistics, vol. 1,

<!-- b000424 | references | pages [24] -->
pp.:63–70, 2002.

<!-- b000425 | references | pages [24] -->
[8] gensim models.word2bec-Word2vec embeddings,

<!-- b000426 | references | pages [24] -->
url:

<!-- b000427 | references | pages [24] -->
https:

<!-- b000428 | references | pages [24] -->
//radimre-

<!-- b000429 | references | pages [24] -->
hurek.com/gensim/models/word2vec.html.

<!-- b000430 | references | pages [24] -->
[9] scikit-learn Machine Learning in Python, url: http://scikit-learn.org/ stable/.

<!-- b000431 | references | pages [24] -->
[10] Douglas Reynolds, “Gaussian mixture models,” Encyclopedia of biometrics, pp.

<!-- b000432 | references | pages [24] -->
827-832, 2015.

<!-- b000433 | references | pages [25] -->
Dear Puzzle Editor,

<!-- b000434 | references | pages [25] -->
Thank you for providing us with the file of the daily results of the interesting puzzle Wordle so that

<!-- b000435 | references | pages [25] -->
we could analyze and model the results of Wordle, which allowed us to discover some interesting

<!-- b000436 | references | pages [25] -->
conclusions about the given dataset. At the request of your journal, we are pleased to have the

<!-- b000437 | references | pages [25] -->
opportunity to present to you our findings and conclusions, which we hope will be of interest to you.

<!-- b000438 | heading | pages [25] -->
·Results of interval prediction & correlation analysis

<!-- b000439 | prose | pages [25] -->
We predicted the number of reported outcomes by constructing an ARIMA-LSTM model, which yielded a prediction interval of [9614,43109] for March 1, 2023. Subsequently, we defined five word attributes such as syllable count and word class, which were found to be significantly correlated with each other by Spearman's correlation coefficient analysis. Among them, lexical commonness index, number of vowels, and information entropy, had strong negative correlations with the proportion of guesses in one attempt, two attempts, and three attempts, and strong positive correlations with the proportion of guesses in five and six attempts or the inability to solve the puzzle (X); word frequency and letter richness were the opposite.

<!-- b000440 | heading | pages [25] -->
·Distribution of results & EERIE distribution prediction

<!-- b000441 | prose | pages [25] -->
After that, we developed the Stacking model fusion algorithm to predict the distribution of the results and came up with the predicted distribution of EERIE on March 1, 2023 as [1,2,3,4,5,6,X]=[0,0,9,18,26,37,10]. We also used R2 and others as evaluation metrics for estimating the accuracy of the model and validating it, and proved that the performance of our model is optimal with a goodness-of-fit of 0.8377. ·Classification & EERIE Difficulty Prediction In addition, we classify words into difficult, medium and easy categories according to their difficulty, and classify them into the category of "difficult" according to the attribute value of "EERIE". From three different perspectives of information entropy, letter richness and word frequency, we found that the information entropy of words in difficulty level 1 is much smaller than that of words in higher difficulty levels, and they appear more frequently in the database, and the words in difficulty level 3 contain more repeated letters. ·Some interesting features Finally, our visual analysis of the data revealed that: most people guessed the puzzle after 3 or 4 attempts; very few were able to guess the puzzle in one go; and the percentage of people who could not solve the puzzle (X) fluctuated more, up to 48%. Among the words in the dataset, b, f, j, q, and s appear more frequently as the first letter of the word, while q appears only at the beginning and end of the word, and s, n, o, e, and d are the most frequently occurring letters. We appreciate this opportunity to predict Wordle results and analyze the interesting findings in the dataset. Feel free to contact us for further information about the article. Yours sincerely MCM 2023 Team
