# P-C-2023-2307166-ec54f9ce

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
2307166

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Viral Spread Characteristics and Difficulty Determinants of Wordle

<!-- b000009 | prose | pages [1] -->
Modeling Based on Differential Equations and K-nearest Neighbors

<!-- b000010 | prose | pages [1] -->
Recently, Wordle, a puzzle game, has been spreading widely around the world and has a high level of buzz on social media such as Twitter. Understanding the spread mechanism of the Wordle craze and the factors influencing the difficulty of the game may shed some light on important issues such as understanding the viral spread in the Internet era and the way the human brain associates words.

<!-- b000011 | prose | pages [1] -->
We developed an epidemiology-like differential equation model describing the variation in the total number of reports based on the SIR model and fitted the model using a genetic algorithm to minimize the MSE. We then used the fitted model to make a point forecast of the total number of reports on March 1, 2023. To obtain confidence intervals for the predictions, we used the Bootstrap method. To improve the speed of fitting the Bootstrap sample, we used the computationally faster Nelder-Mead method, based on the same initial parameters optimized by a genetic algorithm. The 1000 Bootstrap estimates were arranged from smallest to largest, and the 25th and 975th estimates were selected as the lower and upper bounds of the prediction interval.

<!-- b000012 | prose | pages [1] -->
Two characteristic lexical internal features are built in this paper. We define regularity and purity (negentropy) features by assuming first-order Markovianity of the occurrence probability of characters in the English lexicon. All indications are that they are indeed related to the difficulty of the lexicon being guessed. Regularities such as the number of repeated characters and the frequency of vocabulary use in everyday life are also used in this paper for prediction and interpretation.

<!-- b000013 | prose | pages [1] -->
KNN regression has the excellent property of ensuring that the predicted distribution still sums to zero, so we use the KNN regression model to make predictions about the distribution of Wordle scores. The covariance matrix is widely used in this paper for initial selection of variables and determining the relationship between variables. In KNN regression, we use the covariance matrix to select independent variables that are significantly correlated with the distribution and use cross-validation to select the optimal independent variables and K values. To predict the future distribution of scores for a particular puzzle word, we again used the bootstrap method to obtain 95% confidence intervals.

<!-- b000014 | prose | pages [1] -->
We used the median scores of Wordle players to measure the difficulty of the words in the puzzle, classifying the difficulty as ‘easy’, ‘normal’, and ‘hard’.

<!-- b000015 | prose | pages [1] -->
We initially screened features that were significantly correlated with difficulty based on the covariance matrix, used a KNN classifier to classify the features based on the initial screening, and selected the K value with the highest prediction accuracy after cross-validation. The results show that the features can effectively predict the difficulty classification of words. For the prediction of word difficulty, we used the KNN classifier and the difficulty-related features we established to assign them to existing categories.

<!-- b000016 | prose | pages [1] -->
In further exploration of the data, our most important finding is that the variation in the percentage of Hard Mode shows a high degree of similarity to the variation in the faithful players assumed in our initially built contagion-like model, which somewhat corroborates the soundness of our model.

<!-- b000017 | furniture | pages [2] -->
Team # 2307166

<!-- b000018 | furniture | pages [2] -->
Page 1 of 24

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | heading | pages [2] -->
Letter

<!-- b000021 | prose | pages [2] -->
1

<!-- b000022 | heading | pages [2] -->
Introduction

<!-- b000023 | prose | pages [2] -->
2

<!-- b000024 | prose | pages [2] -->
4 Background and Question Restatement 1.1

<!-- b000025 | prose | pages [2] -->
2

<!-- b000026 | heading | pages [2] -->
Preparation for modeling

<!-- b000027 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | prose | pages [2] -->
4

<!-- b000029 | prose | pages [2] -->
5 Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 5 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 5 Data Cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3

<!-- b000030 | prose | pages [2] -->
3 Word Feature Engineering

<!-- b000031 | prose | pages [2] -->
6

<!-- b000032 | prose | pages [2] -->
6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 Regularity 6 Purity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 Repetition 8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 Frequency 9 Feature Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.5 9

<!-- b000033 | heading | pages [2] -->
Modeling the Number of Reported Results

<!-- b000034 | prose | pages [2] -->
4 9 . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Intuition: What is in the Trend 9 Terminology and Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 10 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.2

<!-- b000035 | heading | pages [2] -->
Assumptions

<!-- b000036 | prose | pages [2] -->
4.3 From SIR Model to Our PCQL Model 10 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | prose | pages [2] -->
11 Review of SIR Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.1 11 Our PCQL Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.2 11 . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 Model Fitting and Prediction

<!-- b000038 | prose | pages [2] -->
5 Is Word Itself affect Hard Mode Ratio

<!-- b000039 | prose | pages [2] -->
12

<!-- b000040 | prose | pages [2] -->
13 It Seems to Be True . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 13 It is Very Likely Not True . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2

<!-- b000041 | prose | pages [2] -->
6 Predicting Score Distribution

<!-- b000042 | prose | pages [2] -->
15

<!-- b000043 | prose | pages [2] -->
15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 KNN Regression 16 Feature Selection and Parameter Tuning . . . . . . . . . . . . . . . . . . . . . 6.2 16 Predicting and Bootstrapping . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3

<!-- b000044 | prose | pages [2] -->
7 Diﬀiculty Classification

<!-- b000045 | prose | pages [2] -->
18

<!-- b000046 | prose | pages [2] -->
20 Diﬀiculty Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Diﬀiculty Prediction

<!-- b000047 | prose | pages [2] -->
8 Other Interesting Insights

<!-- b000048 | heading | pages [2] -->
References

<!-- b000049 | references | pages [2] -->
20

<!-- b000050 | references | pages [2] -->
21

<!-- b000051 | references | pages [2] -->
24

<!-- b000052 | furniture | pages [3] -->
Team # 2307166

<!-- b000053 | furniture | pages [3] -->
Page 2 of 24

<!-- b000054 | heading | pages [3] -->
Letter

<!-- b000055 | prose | pages [3] -->
To: Puzzle Editor of the New York Times From: Team 2307166 Date: February 1st, 2023 Subject: Re: On Our Puzzle Game, Wordle

<!-- b000056 | prose | pages [3] -->
Dear Editor,

<!-- b000057 | prose | pages [3] -->
Thank you for your letter asking for information about your famous Wordle game. Con- sidering that it is a popular puzzle game worldwide, the analysis of its popularity trends and dissemination mechanism, as well as its word diﬀiculty, is important not only for your company, but also for the dissemination of Internet trends in general and for the under- standing of human language.

<!-- b000058 | prose | pages [3] -->
First, the number of Wordle game scores uploaded on Twitter fits well with the tradi- tional epidemic spread model; the difference is that epidemic patients eventually lose their ability to spread, while a fraction of Wordle players become veteran players who continue to play Wordle and spread related information. If the number of results on Twitter is a true reflection of Wordle’s hotness, then our epidemiology-like model tells us that Wordle has entered the tail end, or plateau, of its life cycle; for example, we predict that the number of reports for March 1, 2023 is included in the interval [11173.04,17069.15] at a 95% confi- dence level; we know from the model that in order to continue its spreading ability, you should broaden the user base - which, of course, is diﬀicult; or you can try to increase the stickiness of loyal users to continue the life of the game: for example, by adding special events to develop user habits and slow down the exit of old users.

<!-- b000059 | prose | pages [3] -->
Regarding the issue of Hard Mode player ratio you mentioned; we conclude that the attributes of words do not affect this ratio. Since players should not know the information about the word of the day until they try the game every day; and since the evolution of loyal players in our model is similar to the trend of this ratio, it may mean that the change in this ratio can be explained by the life cycle of the game alone. There may be some teams that believe that certain specific indicators of diﬀiculty are related to this proportion, but that is likely because there is an overall trend in those characteristics over time, as is the case with the proportion of Hard Mode players, so statistical tools such as regression may misidentify this trend over time as a direct relationship between the two.

<!-- b000060 | prose | pages [3] -->
You have also asked us to predict the distribution of results for specific dates and spe- cific words. Based on our experiments, the effect of considering the date factor is not signif- icant, so we use only word information: we average the outcome distributions of a number of words that are similar to the words you wish to predict as the predicted outcome. The exact number of words to average and how the factors for evaluating similarity are cho- sen is determined by the machine through some testing methods. By assuming that the tweet data is representative, we determine the prediction interval by some special statisti- cal methods. For example, our distribution estimate for the word EERIE is (0.20 4.87 23.55 35.36 23.75 9.94 2.33). The prediction interval is around 5% above and below the predicted value - depending on the specific number of attempts. The uncertainty in our predictions lies mainly in the fact that we do not deal with changes in player structure - according to our class epidemiological model, the proportion of loyal players may increase, which

<!-- b000061 | furniture | pages [4] -->
Team # 2307166

<!-- b000062 | furniture | pages [4] -->
Page 3 of 24

<!-- b000063 | prose | pages [4] -->
might make changes in the number of attempts for the same words half a month later.

<!-- b000064 | prose | pages [4] -->
We believe that the distribution of the number of guesses people make is an important indicator of the diﬀiculty of a word. We therefore classify word diﬀiculty accordingly into three categories: easy, moderate and diﬀicult. By doing something similar to the previous paragraph, we can predict the diﬀiculty of new words; for example, we consider EERIE to be of average diﬀiculty. The number of repeated letters, weighted purity and weighted regularity are related to the diﬀiculty rating, with the first two positively correlated and the last two negatively correlated. The latter two are statistical indicators that we designed to measure the diﬀiculty properties of words.

<!-- b000065 | prose | pages [4] -->
In addition to the issues you were interested in earlier, there are also some other in- sights, that may be useful to you:

<!-- b000066 | prose | pages [4] -->
We found an increasing temporal trend in the proportion of challenge mode reports, which is consistent with the assumption of the presence of loyal players established in the model we used to predict the total number of reports in the previous section. In fact, the time trend of the challenge mode reporting ratio is highly similar to the time trend of our hypothetical loyal player ratio, and we have reason to believe that the challenge mode reporting ratio and the number of loyal players have some correlation, which means you can observe the trend of the challenge mode reporting ratio to determine the change of the wordle loyal player ratio and thus optimize your business strategy.

<!-- b000067 | prose | pages [4] -->
We also found that the distribution of wordle players’ scores has a certain pattern with the diﬀiculty of wordle, in which the percentage of successful guesses from the first to the third attempt is negatively correlated with the diﬀiculty level, while the percentage of successful guesses from the fourth to the seventh or more attempts is positively correlated with the diﬀiculty level. You can summarize the change in diﬀiculty of wordle by observing the change in the distribution of players’ scores.

<!-- b000068 | prose | pages [4] -->
Choosing words with repeating letters as the wordle significantly reduces the likeli- hood that a player will guess the wordle on the 1st attempt, which is likely related to the fact that players generally choose to use strategies that do not contain repeating letters as their initial guesses. If you want to reduce the diﬀiculty of the game to attract more players, you can increase the likelihood of players guessing the puzzle by indicating the number of repeating letters in the word at the time of play.

<!-- b000069 | prose | pages [4] -->
Best,

<!-- b000070 | prose | pages [4] -->
MCM Team #2307166

<!-- b000071 | furniture | pages [5] -->
Team # 2307166

<!-- b000072 | furniture | pages [5] -->
Page 4 of 24

<!-- b000073 | prose | pages [5] -->
1

<!-- b000074 | heading | pages [5] -->
Introduction

<!-- b000075 | prose | pages [5] -->
1.1

<!-- b000076 | heading | pages [5] -->
Background and Question Restatement

<!-- b000077 | prose | pages [5] -->
Wordle is a puzzle game in which Players try to solve the puzzle by guessing a five- letter word in six tries or less, receiving feedback with every guess. The flow is shown in

<!-- b000078 | caption | pages [5] -->
Figure 1.

<!-- b000079 | caption | pages [5] -->
Figure 1: Flow chart of Wordle

<!-- b000080 | prose | pages [5] -->
We are employed by the New York Times to use only the data they send us to analyze and answer following questions.

<!-- b000081 | prose | pages [5] -->
Question 1 Question 1 consists of two sub-questions:

<!-- b000082 | prose | pages [5] -->
1. How does the date and other factors influence the number of reported results?

<!-- b000083 | prose | pages [5] -->
If a certain date is given, how to predict the number of reported results? (A prediction interval is asked)

<!-- b000084 | heading | pages [5] -->
2. Is there any attributes of the word itself affect the percentage of scores reported

<!-- b000085 | prose | pages [5] -->
that were played in Hard Mode? (A mechanism analysis is in demand)

<!-- b000086 | furniture | pages [6] -->
Team # 2307166

<!-- b000087 | furniture | pages [6] -->
Page 5 of 24

<!-- b000088 | prose | pages [6] -->
Question 2 How to predict the distribution of tries if a certain date and solution word are

<!-- b000089 | prose | pages [6] -->
given? What factors that can influence the result might be omitted? (A prediction interval, or analysis of the predictive ability of the prediction model is needed)

<!-- b000090 | prose | pages [6] -->
Question 3 How to measure diﬀiculty? How to separate solution words into different

<!-- b000091 | prose | pages [6] -->
groups according to their diﬀiculty? For each group, what is the identity of the words? How to classify new solution words? (Analysis of the predictive ability of the classification model is needed)

<!-- b000092 | prose | pages [6] -->
Question 4 Find interesting features in the data set!

<!-- b000093 | prose | pages [6] -->
2

<!-- b000094 | heading | pages [6] -->
Preparation for modeling

<!-- b000095 | prose | pages [6] -->
2.1

<!-- b000096 | heading | pages [6] -->
Assumptions

<!-- b000097 | prose | pages [6] -->
Main assumptions are:

<!-- b000098 | prose | pages [6] -->
Words in English Words in the given data are English words, thereby share some com-

<!-- b000099 | prose | pages [6] -->
mon probabilistic identities with other English words in dictionaries.

<!-- b000100 | prose | pages [6] -->
Players Prefer Generality Words that look like valid English words are more easily remem-

<!-- b000101 | prose | pages [6] -->
bered and given priority for trial.

<!-- b000102 | prose | pages [6] -->
Model-specific assumptions will be presented in subsequent sections.

<!-- b000103 | prose | pages [6] -->
2.2

<!-- b000104 | heading | pages [6] -->
Notations

<!-- b000105 | prose | pages [6] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000106 | caption | pages [6] -->
Table 1: Notations

<!-- b000107 | prose | pages [6] -->
Symbol Definition

<!-- b000108 | prose | pages [6] -->
𝑤𝑖 word i 𝑐𝑖 character i 𝑐𝑖,𝑗 j-th character in word i 𝑇𝑖 transition process i Reg (𝑤𝑖) regularity of word i Irr (𝑤𝑖) irregularity of word i Pur (𝑤𝑖) purity of word

<!-- b000109 | furniture | pages [7] -->
Team # 2307166

<!-- b000110 | prose | pages [7] -->
2.3 Data Cleaning

<!-- b000111 | furniture | pages [7] -->
Page 6 of 24

<!-- b000112 | prose | pages [7] -->
While examining the dataset we found two types of outliers in the dataset: word lengths that are not 5 and an unusually low number of total reports. Details of the anomalous data are as follows.

<!-- b000113 | prose | pages [7] -->
Number of

<!-- b000114 | prose | pages [7] -->
Word Date Contest number

<!-- b000115 | prose | pages [7] -->
reported results

<!-- b000116 | prose | pages [7] -->
rprobe 2022/12/16 545 2022/11/26 525 clen 2022/4/29 314 tash 22853 26381 106652 study 2022/11/30 529 2569

<!-- b000117 | prose | pages [7] -->
To ensure the correctness of the data, we chose to use the removal of anomalous data instead of correction and interpolation.

<!-- b000118 | prose | pages [7] -->
For KNN regression and classification, to avoid the effect of magnitudes on calculat- ing the distance between observations, we normalized the data according to the following equation.

<!-- b000119 | prose | pages [7] -->
𝑥∗

<!-- b000120 | prose | pages [7] -->
𝑖𝑗=

<!-- b000121 | prose | pages [7] -->
𝑥𝑖𝑗−𝑥

<!-- b000122 | prose | pages [7] -->
,

<!-- b000123 | prose | pages [7] -->
𝑠𝑑(𝑋𝑗)

<!-- b000124 | prose | pages [7] -->
where 𝑥𝑖𝑗is i-th observation of criteria j, 𝑋𝑗is all the observations of criteria j, 𝑥∗

<!-- b000125 | prose | pages [7] -->
𝑖𝑗is normalized data. The normalized data had a mean of 0 and a variance of 1.

<!-- b000126 | prose | pages [7] -->
3 Word Feature Engineering

<!-- b000127 | prose | pages [7] -->
3.1 Regularity

<!-- b000128 | prose | pages [7] -->
In English, valid words usually have regular patterns of form, which are quite hard to capture and formalize by mankind, but it can influence the choices of people when playing Wordle, because those words that are regular may be more familiar to English users.

<!-- b000129 | prose | pages [7] -->
Assuming that each character’s probabilistic distribution is just determined by its pre- vious character in the word, we try to model the process with a Bi-gram-like[1] chain, which estimate the possibility that one character emerge given that previous one character in the word is known; to make use of the information of the start and end of the word, we made two virtual characters BOW and EOW at the beginning and the end of the word, as described by Figure 2.

<!-- b000130 | prose | pages [7] -->
Regularity is defined as the geometric mean of the probability of the transfer process of each character to its successor, as described by the formula

<!-- b000131 | prose | pages [7] -->
√ √√

<!-- b000132 | prose | pages [7] -->
Reg (𝑤𝑖) = 𝑛

<!-- b000133 | prose | pages [7] -->
∏

<!-- b000134 | prose | pages [7] -->
𝑗=1

<!-- b000135 | prose | pages [7] -->
⎷

<!-- b000136 | prose | pages [7] -->
𝑛 𝑛

<!-- b000137 | prose | pages [7] -->
𝑃(𝑐𝑖,𝑗∣𝑐𝑖,𝑗−1),

<!-- b000138 | furniture | pages [8] -->
Team # 2307166

<!-- b000139 | furniture | pages [8] -->
Page 7 of 24

<!-- b000140 | caption | pages [8] -->
Figure 2: Virtual characters and transition processes

<!-- b000141 | prose | pages [8] -->
in which 𝑃(𝑐𝑖∣𝑐𝑖−1), sometimes also denoted as 𝑃(𝑇𝑖) in this paper, is used to represent the possibility of transition from character 𝑖−1 to character 𝑖.

<!-- b000142 | prose | pages [8] -->
3.2 Purity

<!-- b000143 | prose | pages [8] -->
If a character in the word is given, how much information can we gain about its succeed- ing character? This is a significant factor in Wordle, because the game’s feedback would tell us wether the guessed letter is actually in the word of the day, so if succeeding word is more unpredictable, it will to harder to solve the puzzle.

<!-- b000144 | prose | pages [8] -->
The purity of a character 𝑐𝑖is defined below:

<!-- b000145 | prose | pages [8] -->
𝑛

<!-- b000146 | prose | pages [8] -->
Pur (𝑐𝑖) =

<!-- b000147 | prose | pages [8] -->
∑

<!-- b000148 | prose | pages [8] -->
𝑃(𝑐𝑖+1 ∣𝑐𝑖) log (𝑃(𝑐𝑖+1 ∣𝑐𝑖)) ,

<!-- b000149 | prose | pages [8] -->
𝑗=1

<!-- b000150 | prose | pages [8] -->
that is, −Entro (𝑐𝑖+1), with the assumption from section 3.1 that each character’s prob- abilistic distribution is just determined by its previous character in the word.

<!-- b000151 | prose | pages [8] -->
The higher the purity of a character, the smaller the number of next characters inferred from that character and the higher the probability that some specific character will occur. In other words, the probability of guessing the correct next character is greater, i.e., the uncertainty of the next character is smaller, as shown in Figure 3. The probabilities and pu- rities are generated from 5 letter words from bestwordlist.com[6], without any frequency weighting.

<!-- b000152 | prose | pages [8] -->
The purity of word 𝑖is simply defined as

<!-- b000153 | prose | pages [8] -->
𝑛

<!-- b000154 | prose | pages [8] -->
𝑤𝑖=

<!-- b000155 | prose | pages [8] -->
∑

<!-- b000156 | prose | pages [8] -->
Pur (𝑐𝑖,𝑗) .

<!-- b000157 | prose | pages [8] -->
𝑗=1

<!-- b000158 | furniture | pages [9] -->
Team # 2307166

<!-- b000159 | furniture | pages [9] -->
Page 8 of 24

<!-- b000160 | caption | pages [9] -->
Figure 3: Purity and Succeeding Character

<!-- b000161 | prose | pages [9] -->
3.3 Repetition

<!-- b000162 | prose | pages [9] -->
The repetition index of words includes two items: the number of repeated letters and the maximum number of repeated letters. Repeated letters are defined as letters that ap- pear more than or equal to 2 times in a word. The number of repeated letters refers to the number of repeated letters in a word. For example, there are no repeated letters except ‘p’ in ‘apple’, so the number of repeated letters in ‘apple’ is 1, while the letters ‘c’ and ‘a’ in ‘cacao’ are repetitive letters, so the number of repeated letters in ‘cacao’ is 2. The max- imum number of repeated letters refers to the maximum number of repeated letters in a word. For example, the ‘m’ in ‘mummy’ is repeated 3 times, so the maximum number of repeated letters in ‘mummy’ is 3, ‘c’ and ‘a’ in ‘cacao’ are repeated twice, so the maximum number of repeated letters in cacao is 2, while the maximum number of repeated letters in words without repeating letters and the maximum number of repeated letters are 0.

<!-- b000163 | prose | pages [9] -->
The effect of word repetition on the diﬀiculty of Wordle is obvious: Wordle will only provide information about whether the answer word contains the input letter and whether the letter is in the correct position, but not whether the letter is repeated or the number of times it is repeated. If the answer word contains duplicate letters, it may mislead the player to try other letters, thus increasing the number of attempts and making Wordle more

<!-- b000164 | furniture | pages [10] -->
Team # 2307166

<!-- b000165 | furniture | pages [10] -->
Page 9 of 24

<!-- b000166 | prose | pages [10] -->
diﬀicult. At the same time, if the repeated letters are repeated more times, the information about the answer words provided by Wordle will be further reduced, thus increasing the diﬀiculty of Wordle again.

<!-- b000167 | prose | pages [10] -->
3.4 Frequency

<!-- b000168 | prose | pages [10] -->
It is a reasonable assumption that people will preferentially think of those words in the available word space that they are most familiar with, regardless of whether the choice is constrained by available information, so word frequency in everyday use is a worthwhile factor both for evaluating word diﬀiculty and for predicting the distribution of attempts.

<!-- b000169 | prose | pages [10] -->
3.5 Feature Generation

<!-- b000170 | prose | pages [10] -->
For word frequency, we simply used a frequency list by Dave Hermit[2], whose corpus sources are movie subtitles

<!-- b000171 | prose | pages [10] -->
Regularity is trained on a 5-letter word list from bestwordlist.com[6]; both a frequency weighted version and a unweighted version are generated; notably that when training weighted version, log function is used to avoid float underflow, so the frequency of zero are set to 1 to avoid arithmetic problems.

<!-- b000172 | prose | pages [10] -->
Purity is trained on a some word list with similar method with Regularity.

<!-- b000173 | prose | pages [10] -->
4

<!-- b000174 | heading | pages [10] -->
Modeling the Number of Reported Results

<!-- b000175 | prose | pages [10] -->
4.1 Intuition: What is in the Trend

<!-- b000176 | prose | pages [10] -->
To give a thorough picture of how the number of reported results varies, we analyze the trend by hand, and have drawn some simple conclusions.

<!-- b000177 | prose | pages [10] -->
First, there is no periodicity in the trend that is visible to the naked eye. Given the characteristics of small games, weekly frequency periodicity is possible, but we found no periodicity under weekly frequency when we used the F-test.

<!-- b000178 | prose | pages [10] -->
The overall trend consists of a relatively steep upward segment and a long-tailed down- ward segment, and the sequence is rather smooth.

<!-- b000179 | prose | pages [10] -->
These properties are too obvious to be negligible. The trend satisfies the shape of a typ- ical sequence of the number of infected individuals in a disease epidemic. And speaking in terms of mechanism, the spread of the behavior of playing Wordle and sharing scores can be very viral, so we take a epidemiology-like approach to model the process.

<!-- b000180 | furniture | pages [11] -->
Team # 2307166

<!-- b000181 | furniture | pages [11] -->
Page 10 of 24

<!-- b000182 | caption | pages [11] -->
Figure 4: Number of Reported Scores and the Fitted Curve of Our Model

<!-- b000183 | prose | pages [11] -->
4.2

<!-- b000184 | heading | pages [11] -->
Terminology and Assumptions

<!-- b000185 | prose | pages [11] -->
4.2.1 Terminology

<!-- b000186 | prose | pages [11] -->
We define terminologies of this section as follows:

<!-- b000187 | prose | pages [11] -->
TP Twittering Playing: the behavior of playing Wordle and twittering about it;

<!-- b000188 | prose | pages [11] -->
TPer those who choose to do TP.

<!-- b000189 | prose | pages [11] -->
4.2.2

<!-- b000190 | heading | pages [11] -->
Assumptions

<!-- b000191 | prose | pages [11] -->
Consistency of Behavior TPers do TP everyday, and non-TPers, including those who trans-

<!-- b000192 | prose | pages [11] -->
formed from TPers, never do TP.

<!-- b000193 | prose | pages [11] -->
Viral Marketing the probability of non-TPers transforming into TPers is determined by

<!-- b000194 | prose | pages [11] -->
the number of TPers they may contact with.

<!-- b000195 | prose | pages [11] -->
Potential Customers while some non-TPers have the possibility to transform into TPers,

<!-- b000196 | prose | pages [11] -->
other non-TPers may not be possible to become TPers. The number of initial potential customers is represented with 𝑁in this section.

<!-- b000197 | prose | pages [11] -->
No Return non-TPers transformed from TPers will never become TPers again.

<!-- b000198 | furniture | pages [12] -->
Team # 2307166

<!-- b000199 | furniture | pages [12] -->
Page 11 of 24

<!-- b000200 | heading | pages [12] -->
From SIR Model to Our PCQL Model

<!-- b000201 | prose | pages [12] -->
4.3

<!-- b000202 | prose | pages [12] -->
4.3.1

<!-- b000203 | heading | pages [12] -->
Review of SIR Model

<!-- b000204 | prose | pages [12] -->
A basic SIR Model consists of a system of four differential equations[3]:

<!-- b000205 | prose | pages [12] -->
= −𝛽× 𝑆(𝑡) × 𝐼(𝑡)

<!-- b000206 | prose | pages [12] -->
d𝑆(𝑡)

<!-- b000207 | prose | pages [12] -->
d𝑡

<!-- b000208 | prose | pages [12] -->
𝑁 ,

<!-- b000209 | prose | pages [12] -->
= −𝛽× 𝑆(𝑡) × 𝐼(𝑡)

<!-- b000210 | prose | pages [12] -->
d𝐼(𝑡)

<!-- b000211 | prose | pages [12] -->
d𝑡

<!-- b000212 | prose | pages [12] -->
𝑁

<!-- b000213 | prose | pages [12] -->
d𝑅(𝑡)

<!-- b000214 | prose | pages [12] -->
= 𝛾× 𝐼(𝑡), d𝑡

<!-- b000215 | prose | pages [12] -->
−𝛾× 𝐼(𝑡),

<!-- b000216 | prose | pages [12] -->
where S means the susceptible population; I means the infected population; and R is the recovered population. This can match our question pretty well because we can deem S as target customers, I as score sharers, and R as those who tried and had been tired with this behavior.

<!-- b000217 | prose | pages [12] -->
However, there is still something different from epidemics: although most players shar- ing their scores might be just catching up with fashion, not all the score sharers would be cured quickly; some people sharing the score would pick up the habit and take playing the game and sharing the score as their daily tasks. So we are going to add something new in the SIR model.

<!-- b000218 | prose | pages [12] -->
4.3.2 Our PCQL Model

<!-- b000219 | prose | pages [12] -->
Our PCQL Model is an ODE model with 4 variables and 4 parameters, that are:

<!-- b000220 | prose | pages [12] -->
Variable P(otential) those who might become TPers, have chance to become the Crowd.

<!-- b000221 | prose | pages [12] -->
Variable C(rowd) normal TPers who will get bored quickly; a fraction of them will be-

<!-- b000222 | prose | pages [12] -->
come the Quitted or the Loyal everyday.

<!-- b000223 | prose | pages [12] -->
Variable Q(uitted) those who tired with the game or uploading scores.

<!-- b000224 | prose | pages [12] -->
Variable L(oyal) those who would not easily giving up TP.

<!-- b000225 | prose | pages [12] -->
Parameter 𝛽(Participation Factor) (participation refers to participation in TP), represent-

<!-- b000226 | prose | pages [12] -->
ing the attractiveness of TP to the Potentials, the number of people attracted and participating in unit time at moment t is 𝛽×𝑃(𝑡)×(𝐶(𝑡)+𝐿(𝑡))

<!-- b000227 | prose | pages [12] -->
. 𝑁

<!-- b000228 | prose | pages [12] -->
Parameter 𝛾(Boredom Coeﬀicient) representing the rate at which people who have been

<!-- b000229 | prose | pages [12] -->
attracted to do TP get bored with TP, the number of people who have been TPers becoming the Quitted in unit time at moment t is 𝛾× 𝐶(𝑡).

<!-- b000230 | prose | pages [12] -->
Parameter 𝜆(Conversion Factor) representing the possibility of the Crowd TPers becom-

<!-- b000231 | prose | pages [12] -->
ing the Loyal TPers; the number of TPers at the moment of t who are converted into loyal TPers per unit time is 𝜆× 𝐶(𝑡).

<!-- b000232 | furniture | pages [13] -->
Team # 2307166

<!-- b000233 | furniture | pages [13] -->
Page 12 of 24

<!-- b000234 | prose | pages [13] -->
Parameter 𝜙(Loyal Player Boredom Coeﬀicient) representing the rate at which Wordle’s

<!-- b000235 | prose | pages [13] -->
loyal TPers get bored of TP, the number of loyal TPers who will no longer do TP in unit time at moment t is 𝜙× 𝐿(𝑡).

<!-- b000236 | prose | pages [13] -->
𝛽×(𝑃+𝐿)×𝐶

<!-- b000237 | prose | pages [13] -->
𝑁

<!-- b000238 | prose | pages [13] -->
𝑃

<!-- b000239 | prose | pages [13] -->
𝐿

<!-- b000240 | prose | pages [13] -->
𝜙× 𝐿 𝜆× 𝐶

<!-- b000241 | prose | pages [13] -->
𝑄 𝐶 𝐶

<!-- b000242 | prose | pages [13] -->
𝛾× 𝐶

<!-- b000243 | caption | pages [13] -->
Figure 5: Average Transition Quantity per Time Step

<!-- b000244 | caption | pages [13] -->
Figure 5 gives an intuitional impression of the model.

<!-- b000245 | prose | pages [13] -->
= −𝛽× 𝑃(𝑡) × (𝐶(𝑡) + 𝐿(𝑡))

<!-- b000246 | prose | pages [13] -->
d𝑃(𝑡)

<!-- b000247 | prose | pages [13] -->
d𝑡

<!-- b000248 | prose | pages [13] -->
𝑁 ,

<!-- b000249 | prose | pages [13] -->
= 𝛽× 𝑃(𝑡) × (𝐶(𝑡) + 𝐿(𝑡))

<!-- b000250 | prose | pages [13] -->
d𝐶(𝑡)

<!-- b000251 | prose | pages [13] -->
d𝑡

<!-- b000252 | prose | pages [13] -->
𝑁

<!-- b000253 | prose | pages [13] -->
d𝑄(𝑡)

<!-- b000254 | prose | pages [13] -->
= 𝛾× 𝐶(𝑡), d𝑡

<!-- b000255 | prose | pages [13] -->
d𝐿(𝑡)

<!-- b000256 | prose | pages [13] -->
= 𝜆× 𝐶(𝑡) −𝜙× 𝐿(𝑡). d𝑡

<!-- b000257 | prose | pages [13] -->
4.4

<!-- b000258 | heading | pages [13] -->
Model Fitting and Prediction

<!-- b000259 | prose | pages [13] -->
−𝛾× 𝐶(𝑡) −𝜆× 𝐶(𝑡),

<!-- b000260 | prose | pages [13] -->
The model uses MSE as the loss function to estimate the model parameters. since the formal solution of the system of differential equations is diﬀicult to compute and therefore cannot be estimated by least squares using conventional methods, only the numerical solu- tion of the differential equations can be computed directly and the MSE is minimized using an optimization algorithm. at the same time, the differential equations cannot be used to compute the prediction intervals using conventional algorithms, so we use the Bootstrap method to obtain the point predictions and prediction intervals.

<!-- b000261 | prose | pages [13] -->
The Bootstrap method requires a large number of calculations, and the time cost of fitting using the optimization algorithm is high, so we choose the Nelder-Mead method, which is computationally faster. Since the Nelder-Mead algorithm requires specifying an initial solution for the function, we first use the genetic algorithm[5] to obtain a relatively good initial solution, and then use the Nelder-Mead method to select the parameters that minimize the MSE, and the initial parameters obtained by the genetic algorithm are shown in the following table. The curve of the model from this set of parameters can be seen in

<!-- b000262 | caption | pages [13] -->
Figure 4.

<!-- b000263 | furniture | pages [14] -->
Team # 2307166

<!-- b000264 | prose | pages [14] -->
𝛽 𝛾

<!-- b000265 | prose | pages [14] -->
1.77e-01 1.77e-02

<!-- b000266 | furniture | pages [14] -->
Page 13 of 24

<!-- b000267 | prose | pages [14] -->
𝜆 𝜙

<!-- b000268 | prose | pages [14] -->
1.04e-03 1.14e-03

<!-- b000269 | prose | pages [14] -->
1000 Bootstrap samples were generated, and within each sample the initial parameters obtained using the genetic algorithm were used as the initial solution of the Nelder-Mead method, fitted to minimize the parameters of the MSE and to predict the number of reports on March 1, 2023, to obtain 1000 Bootstrap predictions. The obtained predicted values were arranged in ascending order and the predicted values at the 2.5% and 97.5% quartiles were selected as the upper and lower bounds of the 95% prediction interval. The obtained prediction intervals were as follows.

<!-- b000270 | prose | pages [14] -->
Mean 2.5%

<!-- b000271 | prose | pages [14] -->
14689.9 11173.04

<!-- b000272 | prose | pages [14] -->
97.5%

<!-- b000273 | prose | pages [14] -->
17069.15

<!-- b000274 | prose | pages [14] -->
We therefore estimate that the number of reports for March 1, 2023 is included in the interval [11173.04,17069.15] at a 95% confidence level.

<!-- b000275 | prose | pages [14] -->
Is Word Itself affect Hard Mode Ratio 5

<!-- b000276 | prose | pages [14] -->
5.1 It Seems to Be True

<!-- b000277 | prose | pages [14] -->
We use the covariance matrix to identify the variables that affect the percentage of play- ers participating in the Hard Mode. We counted the correlation coeﬀicients between the seven attributes corresponding to words: word frequency, weighted purity, unweighted purity, weighted regularity, unweighted regularity, number of repeated letters and max- imum number of letter repetitions and the percentage of players participating in the Hard Mode, and the results are shown in Figure 6.

<!-- b000278 | prose | pages [14] -->
The covariance matrix shows that none of the attributes of the words, except for weighted regularity and unweighted regularity, are significantly correlated with the percentage of players participating in the Hard Mode. Since players do not know the words before they play the Wordle, it is reasonable that most of the attributes of the words are not signifi- cantly correlated with the percentage of players participating in the Hard Mode.

<!-- b000279 | prose | pages [14] -->
The relatively significant correlation between weighted and unweighted regularity on the percentage of participants in the Hard Mode seems to imply that the attributes of the Wordle can influence the percentage of participants in the Hard Mode to some extent. However, we ran separate linear regressions on the percentage of participation in the mode using weighted regularity and unweighted regularity, and the results are shown in the following table.

<!-- b000280 | furniture | pages [15] -->
Team # 2307166

<!-- b000281 | furniture | pages [15] -->
Page 14 of 24

<!-- b000282 | caption | pages [15] -->
Figure 6: Covariance Matrix

<!-- b000283 | caption | pages [15] -->
Table 5: Regression Results of Hard Mode Percentage on Weighted Regularity

<!-- b000284 | furniture | pages [15] -->


<!-- b000285 | prose | pages [15] -->
Estimate

<!-- b000286 | prose | pages [15] -->
(Intercept) 0.082177 Reg_weighted -0.021913 Multiple R-squared: 0.02212

<!-- b000287 | furniture | pages [15] -->


<!-- b000288 | prose | pages [15] -->
Adjusted R-squared: 0.01933

<!-- b000289 | furniture | pages [15] -->


<!-- b000290 | prose | pages [15] -->
Std.Error t value Pr(>|t|)

<!-- b000291 | furniture | pages [15] -->


<!-- b000292 | prose | pages [15] -->
0.00274 29.987 <2e-16 *** 0.007788 -2.814 0.00517 **

<!-- b000293 | furniture | pages [15] -->


<!-- b000294 | furniture | pages [15] -->


<!-- b000295 | furniture | pages [15] -->


<!-- b000296 | furniture | pages [15] -->


<!-- b000297 | furniture | pages [15] -->


<!-- b000298 | furniture | pages [15] -->


<!-- b000299 | furniture | pages [15] -->


<!-- b000300 | furniture | pages [15] -->


<!-- b000301 | furniture | pages [15] -->


<!-- b000302 | furniture | pages [15] -->


<!-- b000303 | caption | pages [15] -->
Table 6: Regression results of Hard Mode Percentage on Unweighted Regularity

<!-- b000304 | furniture | pages [15] -->


<!-- b000305 | prose | pages [15] -->
Estimate

<!-- b000306 | prose | pages [15] -->
(Intercept) 0.082177 Reg_unweighted -0.148223 Multiple R-squared: 0.01348

<!-- b000307 | furniture | pages [15] -->


<!-- b000308 | prose | pages [15] -->
Adjusted R-squared: 0.01066

<!-- b000309 | furniture | pages [15] -->


<!-- b000310 | prose | pages [15] -->
Std.Error t value Pr(>|t|)

<!-- b000311 | furniture | pages [15] -->


<!-- b000312 | prose | pages [15] -->
0.00274 29.987 <2e-16 *** 0.067780 -2.187 0.0294 **

<!-- b000313 | furniture | pages [15] -->


<!-- b000314 | furniture | pages [15] -->


<!-- b000315 | furniture | pages [15] -->


<!-- b000316 | furniture | pages [15] -->


<!-- b000317 | furniture | pages [15] -->


<!-- b000318 | furniture | pages [15] -->


<!-- b000319 | furniture | pages [15] -->


<!-- b000320 | furniture | pages [15] -->


<!-- b000321 | furniture | pages [15] -->


<!-- b000322 | furniture | pages [15] -->


<!-- b000323 | prose | pages [15] -->
The R2 and Adjust R2 of the weighted regularity versus Hard Mode percentage re- gression model are only 0.022 and 0.019, while the R2 and Adjust R2 of the unweighted regularity versus Hard Mode percentage regression model are only 0.013 and 0.011, which represents that the weighted regularity explains only about 2% of the change in challenge mode percentage, while the unweighted regularity explains only about 2% of the change in Hard Mode The unweighted regularity explains only about 1.2% of the variation in the percentage of the Hard Mode, which is not strong enough to explain. In addition, the regression coeﬀicient of weighted regularity is -0.022 and the regression coeﬀicient of un- weighted regularity is -0.01, while the weighted regularity of the observed samples in the dataset is 95% concentrated in the range of 0.081 to 0.612 and the unweighted regularity

<!-- b000324 | furniture | pages [16] -->
Team # 2307166

<!-- b000325 | furniture | pages [16] -->
Page 15 of 24

<!-- b000326 | prose | pages [16] -->
is 95% concentrated in the range of 0.041 to 0.109, which means that the extreme changes in weighted regularity and unweighted regularity in the dataset have an average effect on the percentage of Hard Mode of only 1%. This means that the average effect of extreme changes in weighted and unweighted regularity on the percentage of challenge patterns in the data set is only 1%, which is not significant compared to the average value of 7.52% for the percentage of challenge patterns.

<!-- b000327 | prose | pages [16] -->
5.2 It is Very Likely Not True

<!-- b000328 | prose | pages [16] -->
In addition to the lack of explanatory power, the significant correlation is most likely due to the pseudo-regression. The following table shows the results of the regressions of weighted regularity and percent Hard Mode on time.

<!-- b000329 | caption | pages [16] -->
Table 7: Regression Results of Hard Mode Percentage on Time

<!-- b000330 | furniture | pages [16] -->


<!-- b000331 | prose | pages [16] -->
Estimate

<!-- b000332 | prose | pages [16] -->
(Intercept) -2.893e-04 Date 1.988e-04 Multiple R-squared: 0.8507

<!-- b000333 | furniture | pages [16] -->


<!-- b000334 | prose | pages [16] -->
Adjusted R-squared: 0.8503

<!-- b000335 | furniture | pages [16] -->


<!-- b000336 | prose | pages [16] -->
Std.Error t value Pr(>|t|)

<!-- b000337 | furniture | pages [16] -->


<!-- b000338 | prose | pages [16] -->
1.751e-03 -0.165 0.869 *** 4.453e-06 44.655 <2e-16 ***

<!-- b000339 | furniture | pages [16] -->


<!-- b000340 | furniture | pages [16] -->


<!-- b000341 | furniture | pages [16] -->


<!-- b000342 | furniture | pages [16] -->


<!-- b000343 | furniture | pages [16] -->


<!-- b000344 | furniture | pages [16] -->


<!-- b000345 | furniture | pages [16] -->


<!-- b000346 | furniture | pages [16] -->


<!-- b000347 | furniture | pages [16] -->


<!-- b000348 | furniture | pages [16] -->


<!-- b000349 | caption | pages [16] -->
Table 8: Regression Results of Weighted Regularity on Time

<!-- b000350 | furniture | pages [16] -->


<!-- b000351 | prose | pages [16] -->
Estimate

<!-- b000352 | prose | pages [16] -->
(Intercept) 0.3814810 Date -1.668e-04 Multiple R-squared: 0.01299

<!-- b000353 | furniture | pages [16] -->


<!-- b000354 | prose | pages [16] -->
Adjusted R-squared: 0.01017

<!-- b000355 | furniture | pages [16] -->


<!-- b000356 | prose | pages [16] -->
Std.Error t value Pr(>|t|)

<!-- b000357 | furniture | pages [16] -->


<!-- b000358 | prose | pages [16] -->
0.0305641 12.481 <2e-16 *** 7.77e-05 -2.146 0.0325 *

<!-- b000359 | furniture | pages [16] -->


<!-- b000360 | furniture | pages [16] -->


<!-- b000361 | furniture | pages [16] -->


<!-- b000362 | furniture | pages [16] -->


<!-- b000363 | furniture | pages [16] -->


<!-- b000364 | furniture | pages [16] -->


<!-- b000365 | furniture | pages [16] -->


<!-- b000366 | furniture | pages [16] -->


<!-- b000367 | furniture | pages [16] -->


<!-- b000368 | furniture | pages [16] -->


<!-- b000369 | prose | pages [16] -->
The regression results indicate that the Hard Mode percentage is positively correlated with time, while the weighted regularity is negatively correlated with time, and the neg- ative correlation between them is most likely caused by the time trend rather than the existence of a causal relationship between them.

<!-- b000370 | prose | pages [16] -->
In summary, we conclude that the significant correlation between weighted regular- ity and unweighted regularity and Hard Mode percentages does not prove that word at- tributes influence whether players choose the Hard Mode, a finding that is also consistent with our hypothesis above that players do not know the puzzle words before participating in Wordle.

<!-- b000371 | prose | pages [16] -->
Predicting Score Distribution 6

<!-- b000372 | prose | pages [16] -->
In predicting the distribution of reported scores, we need to ensure that the sum of the scores is equal to 100%, and the K-Nearest-Neighbors Regression method can satisfy this constraint well, so we choose KNN regression to predict the distribution of scores.

<!-- b000373 | furniture | pages [17] -->
Team # 2307166

<!-- b000374 | furniture | pages [17] -->
Page 16 of 24

<!-- b000375 | caption | pages [17] -->
Figure 7: Time Trend of Hard Mode Report Ratio and Weighted Regularity

<!-- b000376 | prose | pages [17] -->
6.1 KNN Regression

<!-- b000377 | prose | pages [17] -->
KNN is a typical nonparametric method, the basic idea of which is to calculate the distance between observations in the training set, select the K observations closest to the observations and use the average of their corresponding dependent variables as the fitted values of the model, which is calculated as follows.

<!-- b000378 | prose | pages [17] -->
𝑓(𝑥0) = 1

<!-- b000379 | prose | pages [17] -->
∑

<!-- b000380 | prose | pages [17] -->
(𝑓(𝑥𝑖)) ,

<!-- b000381 | prose | pages [17] -->
𝐾 𝑥𝑖∈𝑁0

<!-- b000382 | prose | pages [17] -->
where 𝑁0 is the set of the K closest observations to 𝑥0, and̂ 𝑓(𝑥0) is the fitted value of the model.

<!-- b000383 | prose | pages [17] -->
Since KNN uses the mean value of the dependent variable as the prediction, it ensures that the predicted value obtained after fitting the seven scores to the observations still sums to 100%.

<!-- b000384 | prose | pages [17] -->
6.2 Feature Selection and Parameter Tuning

<!-- b000385 | prose | pages [17] -->
According to the covariance matrix, we can see that the distribution of guessing scores has a significant correlation with the number of Hard Mode Results, word frequency, the number of repeated letters, the purity of vocabulary, the weighted purity of vocabulary, the regularity of vocabulary, the weighted regularity of vocabulary, and the maximum number of repetitions of repeated letters. It can also be seen that there is a significant correlation between the purity of vocabulary and the weighted purity of vocabulary, the regularity of vocabulary and the weighted regularity of vocabulary, and repeated use may lead to poor prediction; at the same time, since we do not know the data of the number of people in the Hard Mode in the prediction, the prediction result will be unreliable if we use the predicted value of the number of people in the Hard Mode, so we need to conduct

<!-- b000386 | furniture | pages [18] -->
Team # 2307166

<!-- b000387 | furniture | pages [18] -->
Page 17 of 24

<!-- b000388 | caption | pages [18] -->
Figure 8: Covariance Matrix(1)

<!-- b000389 | caption | pages [18] -->
Figure 9: Covariance Matrix(2)

<!-- b000390 | furniture | pages [19] -->
Team # 2307166

<!-- b000391 | furniture | pages [19] -->
Page 18 of 24

<!-- b000392 | prose | pages [19] -->
further in these five variables filtering. Also, it is known from the idea of KNN method that the choice of K determines the performance of the model. We use the cross-validation method to calculate the prediction errors of KNN models using different independent vari- ables with different K values, and the K value that makes the smallest cross-validation error is used for the model. To ensure a moderate computational effort, we use ten-fold cross-validation.

<!-- b000393 | prose | pages [19] -->
Before performing the fit, to remove the effect of the magnitude on the distance between observations, we standardized the independent variables using the following equation, standardizing the mean of each independent variable to 0 and the variance to 1.

<!-- b000394 | prose | pages [19] -->
𝑖= 𝑋𝑖−𝑋

<!-- b000395 | prose | pages [19] -->
𝑋∗

<!-- b000396 | prose | pages [19] -->
𝑠𝑑(𝑋)

<!-- b000397 | prose | pages [19] -->
The cross-validation results are shown in Figure 10.

<!-- b000398 | caption | pages [19] -->
Figure 10: Cross-Validation Results

<!-- b000399 | prose | pages [19] -->
*: ‘&’ is including, while ‘!’ is excluding; ‘UnW’ is unweighted word features; ‘W’ is word frequency weighted word features.

<!-- b000400 | prose | pages [19] -->
From the figure, it can be seen that the KNN model using weighted regularity and weighted purity and without the number of challenge patterns performs best at K=15. Therefore, we chose word frequency, number of repeated letters, weighted purity of words, weighted regularity of words, and maximum number of repetitions of repeated letters as model independent variables and set the model K=15. The MSE of the model was 12.35.

<!-- b000401 | prose | pages [19] -->
6.3 Predicting and Bootstrapping

<!-- b000402 | prose | pages [19] -->
Now we determine each attribute of EERIE.

<!-- b000403 | furniture | pages [20] -->
Team # 2307166

<!-- b000404 | prose | pages [20] -->
Frequency

<!-- b000405 | prose | pages [20] -->
Weighted Purity Weighted Regularity Number of Repeated Word Max Times of Repeated

<!-- b000406 | furniture | pages [20] -->
Page 19 of 24

<!-- b000407 | prose | pages [20] -->
3264

<!-- b000408 | prose | pages [20] -->
10.86 0.32 1 3

<!-- b000409 | prose | pages [20] -->
The attributes of EERIE were input into the KNN model and their predicted distribu- tions were obtained as shown in the following table.

<!-- b000410 | prose | pages [20] -->
1 try 2 tries 3 tries 4 tries

<!-- b000411 | prose | pages [20] -->
0.20 4.87 23.55 35.36

<!-- b000412 | prose | pages [20] -->
5 tries 6 tries X

<!-- b000413 | prose | pages [20] -->
23.75 9.94 2.33

<!-- b000414 | prose | pages [20] -->
We calculated the prediction intervals for the KNN model using the Bootstrap method and obtained the 95% confidence intervals for the predicted values of each score as shown in Figure 11.

<!-- b000415 | caption | pages [20] -->
Figure 11: Predicted tries Distribution for EERIE and 95% Confidence Intervals

<!-- b000416 | prose | pages [20] -->
It can be seen that the error range of the model is small.

<!-- b000417 | furniture | pages [21] -->
Team # 2307166

<!-- b000418 | furniture | pages [21] -->
Page 20 of 24

<!-- b000419 | prose | pages [21] -->
7 Diﬀiculty Classification

<!-- b000420 | prose | pages [21] -->
7.1 Diﬀiculty Evaluation

<!-- b000421 | prose | pages [21] -->
The diﬀiculty of Wordle can be measured by the number of attempts players make to guess the puzzle word, and the higher the number of attempts, the more diﬀicult Wordle is. We can obtain the distribution of the final number of attempts from the dataset, and we define the median number of attempts to measure the diﬀiculty of the wordle. The median number of attempts refers to the number of attempts made by players at 50% of the score distribution to guess the word. The median number of attempts for ‘abbey’ is 5.

<!-- b000422 | prose | pages [21] -->
Since there are only three words with a median of 6, we combined the words with a median of 6 with those with a median of 5 to obtain three diﬀiculty levels: easy, normal, and hard, which correspond to a median of 3, 4, and 5 or 6, respectively.

<!-- b000423 | prose | pages [21] -->
7.2 Diﬀiculty Prediction

<!-- b000424 | prose | pages [21] -->
We use the covariance matrix to filter the word attributes corresponding to diﬀiculty, and filter out the number of repeated letters, weighted purity and weighted regularity as attributes related to classification. We use KNN to verify the accuracy of the classification.

<!-- b000425 | caption | pages [21] -->
Figure 12: Covariance Matrix

<!-- b000426 | prose | pages [21] -->
We used cross-validation to obtain the best K values for KNN using accuracy (i.e., the number of correct predictions as a percentage of all predictions) as the selection criterion, and the results of cross-validation are shown in Figure 13.

<!-- b000427 | prose | pages [21] -->
We chose K=8 as the parameter, and the prediction accuracy was 75.28%.

<!-- b000428 | prose | pages [21] -->
We substituted the three data of EERIE and obtained the prediction result that EERIE

<!-- b000429 | furniture | pages [22] -->
Team # 2307166

<!-- b000430 | furniture | pages [22] -->
Page 21 of 24

<!-- b000431 | caption | pages [22] -->
Figure 13: The Results of Cross-Validation

<!-- b000432 | prose | pages [22] -->
belongs to the ordinary diﬀiculty. Based on the cross-validation error of the model at K=8, we consider the accuracy of this prediction to be about 75.28%, with an accuracy interval of [63.16%,82.76%].

<!-- b000433 | prose | pages [22] -->
8 Other Interesting Insights

<!-- b000434 | prose | pages [22] -->
As shown in Figure 14, the proportion of Hard Mode in the total number of reports gradually increases as time passes. In fact, this phenomenon is consistent with our PCQL Model, in which we assume that there are loyal TPers, or loyal players, and that the pro- portion of loyal players will increase as time passes because loyal players are much less likely to quit playing than regular players, as shown in Figure 15. We can assume that the proportion of loyal players prefers challenges, so the increase in the proportion of Hard Mode reflects the increase in the proportion of loyal players to some extent.

<!-- b000435 | prose | pages [22] -->
The proportion of words guessed in the riddle on the 4th time is the cut-off for vocab- ulary diﬀiculty. The covariance matrix shows that as the indicator positively correlated with diﬀiculty increases, the proportion of riddles that are guessed the 4th to 7th time increases and the proportion of riddles that are guessed the 1st to 3rd time decreases.

<!-- b000436 | prose | pages [22] -->
As shown in the figure below, the proportion of players guessing correctly on the first try is positively correlated with the total number of reported scores, which may be due to the fact that as the number of reports increases, the probability of people knowing the puzzle in advance from social media increases, thus leading to a positive correlation between the proportion of first guesses and the total number of reported scores. At the same time, the proportion of players' first guesses was significantly negatively correlated with the number of puzzle words with repeating letters, reflecting the possible strategy of using words that do not have repeating letters as initial guesses when players play wordle, as this eliminates as many incorrect letters and positions as possible.

<!-- b000437 | furniture | pages [23] -->
Team # 2307166

<!-- b000438 | furniture | pages [23] -->
Page 22 of 24

<!-- b000439 | caption | pages [23] -->
Figure 14: The Proportion of Hard Mode in the Total Number of Reports

<!-- b000440 | caption | pages [23] -->
Figure 15: The Proportion of Ls in TPs in Our Model with Parameters as Previous Mentioned

<!-- b000441 | furniture | pages [24] -->
Team # 2307166

<!-- b000442 | furniture | pages [24] -->
Page 23 of 24

<!-- b000443 | caption | pages [24] -->
Figure 16: Covariance Matrix

<!-- b000444 | caption | pages [24] -->
Figure 17: The Proportion of Guessing Correctly on the First Try and the Total Number of Reported

<!-- b000445 | prose | pages [24] -->
Scores

<!-- b000446 | furniture | pages [25] -->
Team # 2307166

<!-- b000447 | furniture | pages [25] -->
Page 24 of 24

<!-- b000448 | heading | pages [25] -->
References

<!-- b000449 | references | pages [25] -->
[1]

<!-- b000450 | references | pages [25] -->
Markov A. A. “An Example of Statistical Investigation of the Text Eugene Onegin

<!-- b000451 | references | pages [25] -->
Concerning the Connection of Samples in Chains.” In: Science in Context 19 (2007),

<!-- b000452 | references | pages [25] -->
pp. 591–600. ISSN: 1474-0664.

<!-- b000453 | references | pages [25] -->
Hermit Dave. GitHub - hermitdave/FrequencyWords: Repository for Frequency Word List

<!-- b000454 | references | pages [25] -->
[2]

<!-- b000455 | references | pages [25] -->
Generator and processed files. GitHub. URL: https://github.com/hermitdave/FrequencyWords

<!-- b000456 | references | pages [25] -->
(visited on 02/18/2023).

<!-- b000457 | references | pages [25] -->
[3]

<!-- b000458 | references | pages [25] -->
W. O. Kermack and A. G. McKendrick. “A Contribution to the Mathematical Theory

<!-- b000459 | references | pages [25] -->
of Epidemics.” In: Proceedings of the Royal Society of London. Series A, Containing Papers

<!-- b000460 | references | pages [25] -->
of a Mathematical and Physical Character 115.772 (1927), pp. 700–721. ISSN: 09501207.

<!-- b000461 | references | pages [25] -->
R Core Team. R: A Language and Environment for Statistical Computing. R Foundation

<!-- b000462 | references | pages [25] -->
[4]

<!-- b000463 | references | pages [25] -->
for Statistical Computing. Vienna, Austria, 2022. URL: https://www.R-project.org/.

<!-- b000464 | references | pages [25] -->
[5]

<!-- b000465 | references | pages [25] -->
Luca Scrucca. “GA: A Package for Genetic Algorithms in R”. In: Journal of Statistical

<!-- b000466 | references | pages [25] -->
Software 53.4 (2013), pp. 1–37. DOI: 10.18637/jss.v053.i04.

<!-- b000467 | references | pages [25] -->
Word Lists - 5-Letter Words. URL: https://www.bestwordlist.com/5letterwords.htm

<!-- b000468 | references | pages [25] -->
[6]

<!-- b000469 | references | pages [25] -->
(visited on 02/18/2023).
