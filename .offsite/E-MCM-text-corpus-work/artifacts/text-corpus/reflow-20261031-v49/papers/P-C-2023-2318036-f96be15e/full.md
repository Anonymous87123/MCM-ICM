# P-C-2023-2318036-f96be15e

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
2318036

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | prose | pages [1] -->
Exploring Wordle: Insights into Puzzle Solving and Tweet Shares Pattern

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Wordle, a word puzzle that has attracted millions of people, is now owned by The New York Times. For the company’s game editor, how the game is solved and shared on social media is critical information, as it can be used to guide future puzzle design and ultimately maximise the total number of players. This paper aims to build a quantitative model based on word attributes and result reports on Twitter to predict the future pattern of players.

<!-- b000010 | prose | pages [1] -->
After examining and cleaning the raw data, we first define 12 attribute indicators measuring its familiarity (how often used), degree of association, degree of confusion and word composition features. They are computed in advance because the following models will frequently use these indicators.

<!-- b000011 | prose | pages [1] -->
For Problem 1, we build a dynamic system called Target-two-Players-Lost (T2PL) based on the SIR Model to explain the daily fluctuation of Wordle reports. Players are additionally divided into two categories: general players and loyal players, each with a different attrition rate. This allows the model to simulate unequal decline rates over different time periods better. The relationship between word attributes and the number of hard mode players is also explored, and it is found that certain attributes affect the percentage of Hard Mode reports.

<!-- b000012 | prose | pages [1] -->
For Problem 2, we develop a P&S Model, which is a model that uses simulation algorithms and gradient descent to mimic the behavior of players in guessing words and sharing the game results. The simulator works by eliminating all unsatisfactory words using observable information, then randomly sampling words from the remaining word list using word frequency as the weight. However, we found that the simulation result could not perfectly match the true distribution. Therefore, we rescaled the distribution with 7 variables representing how players are likely to share their score when given different scores. They are optimised by gradient descent, and better distribution predictions could be generated. Using the P&S Model, we predict the distribution of the word EERIE on March 1, 2023 is (0, 0, 9%, 29%, 45%, 14%, 3%).

<!-- b000013 | prose | pages [1] -->
For Problem 3, we are required to classify puzzles by difficulty. We perform a cluster analysis on all reported trial distributions using 3 clusters K-means, with each cluster labelled easy, medium and hard. We fit a Random Forest Model to divide the words into these three categories using the attribute indicators defined at the beginning. The correlation coefficient between each indicator and the difficulty is calculated, showing the direction in which these indicators affect the difficulty of the puzzles. The sensitivity of the clustering is discussed as well. Based on our model, the difficulty of EERIE is hard.

<!-- b000014 | prose | pages [1] -->
For Problem 4, we further explore the effects of word difficulty. Using Linear Regression, we found that word difficulty has an obvious effect on the number of results reported: harder puzzles lead to fewer reports. Difficulty also correlates with the percentage of people choosing Hard Mode, as we mentioned earlier. Through this part of the study, we find that the correlation is formed by word difficulty affecting the number of Normal Mode players.

<!-- b000015 | prose | pages [1] -->
With all the uncovered interactions between word attributes, puzzle difficulty, and game report pat- terns, Wordle operators could gain a deeper understanding of their players. Several sensible suggestions could also be made based on this discovery.

<!-- b000016 | keywords | pages [1] -->
Keywords: Wordle;

<!-- b000017 | prose | pages [1] -->
Dynamic system; Simulation; K-means; Random Forest

<!-- b000018 | furniture | pages [2] -->
Team 2318036

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1 Introduction

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
1.1

<!-- b000023 | contents | pages [2] -->
Background and Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
3

<!-- b000025 | contents | pages [2] -->
1.2

<!-- b000026 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
3

<!-- b000028 | contents | pages [2] -->
1.3

<!-- b000029 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
4

<!-- b000031 | contents | pages [2] -->
2 Assumptions and Notations

<!-- b000032 | contents | pages [2] -->
4

<!-- b000033 | contents | pages [2] -->
2.1

<!-- b000034 | contents | pages [2] -->
Model Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
4

<!-- b000036 | contents | pages [2] -->
2.2

<!-- b000037 | contents | pages [2] -->
Notations

<!-- b000038 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
3 Data Preprocessing

<!-- b000041 | contents | pages [2] -->
5

<!-- b000042 | contents | pages [2] -->
4 Task 1: Word Attribute Indicators

<!-- b000043 | contents | pages [2] -->
6

<!-- b000044 | contents | pages [2] -->
5 Task 2: Predicting Daily Reports & Hard Mode Percentage

<!-- b000045 | contents | pages [2] -->
8

<!-- b000046 | contents | pages [2] -->
5.1

<!-- b000047 | contents | pages [2] -->
Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
8

<!-- b000049 | contents | pages [2] -->
5.2

<!-- b000050 | contents | pages [2] -->
Establishment of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
8

<!-- b000052 | contents | pages [2] -->
5.3

<!-- b000053 | contents | pages [2] -->
Solving the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
10

<!-- b000055 | contents | pages [2] -->
5.4

<!-- b000056 | contents | pages [2] -->
Solution and Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
10

<!-- b000058 | contents | pages [2] -->
5.5

<!-- b000059 | contents | pages [2] -->
Hard Mode Percentage Estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
11

<!-- b000061 | contents | pages [2] -->
6 Task 3: Predicting Report Distribution

<!-- b000062 | contents | pages [2] -->
13

<!-- b000063 | contents | pages [2] -->
6.1

<!-- b000064 | contents | pages [2] -->
Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
13

<!-- b000066 | contents | pages [2] -->
6.2

<!-- b000067 | contents | pages [2] -->
Establishment of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
13

<!-- b000069 | contents | pages [2] -->
6.3

<!-- b000070 | contents | pages [2] -->
Predict Confidence and Uncertainties . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
15

<!-- b000072 | contents | pages [2] -->
7 Task 4: Word Difficulty Classification

<!-- b000073 | contents | pages [2] -->
16

<!-- b000074 | contents | pages [2] -->
7.1

<!-- b000075 | contents | pages [2] -->
Cluster Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
16

<!-- b000077 | contents | pages [2] -->
7.2

<!-- b000078 | contents | pages [2] -->
Difficulty Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
17

<!-- b000080 | contents | pages [2] -->
7.3

<!-- b000081 | contents | pages [2] -->
Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
19

<!-- b000083 | contents | pages [2] -->
8 Task 5: Other Features

<!-- b000084 | contents | pages [2] -->
20

<!-- b000085 | contents | pages [2] -->
8.1

<!-- b000086 | contents | pages [2] -->
Fluctuations in the Number of Reported Results . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
20

<!-- b000088 | contents | pages [2] -->
8.2

<!-- b000089 | contents | pages [2] -->
Effect of Word Difficulty on Hard Mode Reports Percentage

<!-- b000090 | contents | pages [2] -->
. . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
20

<!-- b000092 | contents | pages [2] -->
9 Strengths and Weaknesses

<!-- b000093 | contents | pages [2] -->
21

<!-- b000094 | contents | pages [2] -->
9.1

<!-- b000095 | contents | pages [2] -->
Strengths

<!-- b000096 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
21

<!-- b000098 | contents | pages [2] -->
9.2

<!-- b000099 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
22

<!-- b000101 | contents | pages [2] -->
9.3

<!-- b000102 | contents | pages [2] -->
Further Discussion

<!-- b000103 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [2] -->
22

<!-- b000105 | contents | pages [2] -->
9.3.1

<!-- b000106 | contents | pages [2] -->
Model Improvement

<!-- b000107 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000108 | contents | pages [2] -->
22

<!-- b000109 | contents | pages [2] -->
9.3.2

<!-- b000110 | contents | pages [2] -->
Model Extension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000111 | contents | pages [2] -->
22

<!-- b000112 | furniture | pages [3] -->
Team 2318036

<!-- b000113 | furniture | pages [3] -->
Page 3 of 24

<!-- b000114 | heading | pages [3] -->
1 Introduction

<!-- b000115 | heading | pages [3] -->
1.1 Background and Literature Review

<!-- b000116 | prose | pages [3] -->
The word puzzle Wordle invented by Josh Wardle has attract millions of people due to its simplicity and myriad variation. Beyond the game, perhaps the major factor that cause Wordle went viral is its integrated sharing format consists of emoji squares, which spread widely through Twitter. In January 2022, Wordle was purchased by The New York Times Company and operated by them ever since. Only one piece of puzzle is released every day at the game’s official website and this scarcity is also believed to contribute to Wordle’s success.

<!-- b000117 | prose | pages [3] -->
In Wordle, player aim to crack a five-letter word within six guesses. Feedback is given after each guess is submitted: Letters highlighted in green indicates that the answer has the same letter at the same location. Yellow indicates this letter appears in the answer, but at another place. Grey indicates the letter is absent in the answer. Generally, it requires three to five tries for an average player, but it could vary significantly among different words. Addition to the normal version, there is also a Hard Mode Wordle, stipulating each discovered correct word (in Yellow or Green) must be maintained in the following guess[11].

<!-- b000118 | prose | pages [3] -->
Much research has focused on finding optimal strategy on solving the puzzle[1][4]. However, it seems that player’s pattern is worthy to explore as well. As a major product under The New York Times Games, its operator would like to trace and predict the number of shared games on Twitter. Besides, released word should be well-considered, since easy problems could not challenge experienced player, while rare word like ”rebus” or ”tapir” make most fans frustrated[10]. Therefore, a quantitative model to predict distribution of attempts according to a given word is also expected.

<!-- b000119 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000120 | prose | pages [3] -->
Considering the background, in this paper we are required to solve the following problems:

<!-- b000121 | prose | pages [3] -->
• Task 1: Combine the game mechanics of Wordle to build a set of indicators that reflect the attributes of words, and apply them to the subsequent model.

<!-- b000122 | prose | pages [3] -->
• Task 2: Develop a model that explains the trends in the number of reported results and the percentage of scores reported that were played in Hard Mode, and use it to predict the number of reported results on March 1, 2023. Further, analyze the effect of word attributes on the percentage of scores reported that were played in Hard Mode.

<!-- b000123 | prose | pages [3] -->
• Task 3: Develop a model that can predict the distribution of the reported results based on words and use it to predict the distribution for the word EERIE on March 1, 2023. In addition, illustrate the uncertainty and accuracy of the model.

<!-- b000124 | prose | pages [3] -->
• Task 4: Classify words according to their difficulty and explain the relationship between the attributes of the words and the difficulty of the words.

<!-- b000125 | prose | pages [3] -->
• Task 5: Perform a comprehensive analysis of the dataset, and give some interesting conclusions.

<!-- b000126 | furniture | pages [4] -->
Team 2318036

<!-- b000127 | furniture | pages [4] -->
Page 4 of 24

<!-- b000128 | heading | pages [4] -->
1.3 Our Work

<!-- b000129 | caption | pages [4] -->
Figure 1: Flow chart of our work

<!-- b000130 | prose | pages [4] -->
Firstly, we constructed four types of indicators that can measure the familiarity, composition features, degree of association and degree of confusion of words, and used these indicators to reflect the attributes of words.

<!-- b000131 | prose | pages [4] -->
Secondly, we developed the T2PL Model based on the SIR model, a dynamic model that can well explain the overall trends in the number of reported results and the percentage of reported Hard Mode results. Based on this, we explored the effect of word attributes on the percentage of reported Hard Mode results.

<!-- b000132 | prose | pages [4] -->
Thirdly, we used the algorithm to simulate the strategies of wordle players when guessing words, so as to simulate the initial distribution of results. Considering the psychological characteristics of players, we added parameters indicating players’ willingness to share their scores, and simulated the final distribution of reported results.

<!-- b000133 | prose | pages [4] -->
Fourthly, we clustered the words according to the distribution of scores and classified the words into 3 classes based on difficulty. The clustering results were used as labels to construct a Random Forest Model for classifying words’ difficulty based on their attributes.

<!-- b000134 | prose | pages [4] -->
Finally, based on the results of the above model, we conducted further exploration and found some interesting conclusions.

<!-- b000135 | heading | pages [4] -->
2 Assumptions and Notations

<!-- b000136 | heading | pages [4] -->
2.1 Model Assumptions

<!-- b000137 | prose | pages [4] -->
Considering the conditions required for modeling, we make following assumptions:

<!-- b000138 | furniture | pages [5] -->
Team 2318036

<!-- b000139 | furniture | pages [5] -->
Page 5 of 24

<!-- b000140 | prose | pages [5] -->
• Assumption 1: There will not be a shift in the general trend of Wordle’s daily user number.

<!-- b000141 | prose | pages [5] -->
Justification:This is required to predict future trend based on observed daily usage.

<!-- b000142 | prose | pages [5] -->
• Assumption 2: Most players use rational strategies.

<!-- b000143 | prose | pages [5] -->
Justification: To establish a mathematic model for potential player, it is necessary to assume that they are actually using a strategy and will not take unessential moves. Otherwise, it would become meaningless to simulate result based on potential strategies.

<!-- b000144 | prose | pages [5] -->
• Assumption 3: There is no significant change in players’ skill along time.

<!-- b000145 | prose | pages [5] -->
Justification: As Wordle is played for a period, players are expected to improve their strategies which might affect attempt times distributions at different date. However, experienced players are giving up Wordle while rookies are joining simultaneously, producing an opposite effect. It would be too complicated to consider these possibilities.

<!-- b000146 | prose | pages [5] -->
• Assumption 4: In task 2 (T2PL Model), player and those who share their result are not distin- guished. Justification: For convenience, players are modelled in Task 2, although Twitter report numbers are actually used. This is because there is not enough information to distinguish between the two categories in this step, and it makes sense to switch from modelling players to modelling players who share their results.

<!-- b000147 | heading | pages [5] -->
2.2 Notations

<!-- b000148 | prose | pages [5] -->
Symbol Definition 𝑁 Number of reported results 𝐻 Number of reports in Hard Mode Percentage of scores reported that 𝑃𝐻 were played in Hard Mode.

<!-- b000149 | prose | pages [5] -->
𝑃𝐻= 𝐻/𝑁× 100% All words of length 5 in dictionary 𝐷 data 𝑇 Number of Targeted Population Symbol Definition 𝑃 Number of all players 𝑃𝑙𝑜𝑦 Number of loyal players

<!-- b000150 | prose | pages [5] -->
𝑃𝑔𝑒𝑛 Number of general players

<!-- b000151 | prose | pages [5] -->
Probability of sharing when 𝑊𝑠𝑗 finishing with j tries Probability of solving Wordle #i 𝑝𝑖𝑗 with j tries

<!-- b000152 | caption | pages [5] -->
Table 1: Symbol table.

<!-- b000153 | prose | pages [5] -->
Word attribute indicators is not included, because they are explaned in detail below.

<!-- b000154 | heading | pages [5] -->
3 Data Preprocessing

<!-- b000155 | prose | pages [5] -->
The dataset Problem_C_Data_Wordle.xlsx contains 359 days of Wordle report information. Each row consists of date, the word of the day, the number of reported results, the hard mode results, and the distribution of each number of attempts. There are no missing values in the table, but on closer inspection several words are misspelled. We manually correct each of these by searching for the correct Wordle answer using the question number for that day.

<!-- b000156 | furniture | pages [6] -->
Team 2318036

<!-- b000157 | furniture | pages [6] -->
Page 6 of 24

<!-- b000158 | prose | pages [6] -->
Date Contest number original word correct word 2022/12/16 545 rprobe probe na¨ıve 2022/12/11 540 naive 2022/11/26 525 clen clean 2022/10/5 473 marxh marsh 2022/4/29 314 tash trash

<!-- b000159 | caption | pages [6] -->
Table 2: All corrected words

<!-- b000160 | prose | pages [6] -->
We also checked the sum of the percentages of each distribution and found that the sum of question 281 ”nymph” on 2022/3/27 was 126, which is likely to be an outlier. We do not know which of the percentages is wrong, so we cannot simply scale it back. Therefore, this row of data is not used in the prediction percentage problem. Question number 529 ”study” on 2022/11/30 seems like an outlier as well. The Number of reported results in this row is 2569 and the Number in hard mode is 2405, which is obviously very different from the data in other rows, so it is corrected to 25690.

<!-- b000161 | caption | pages [6] -->
Figure 2: calendar map of submissions

<!-- b000162 | prose | pages [6] -->
Considering a possible weekly periodic pattern in the number of submissions, a calendar graph (Figure 2) is created to visualise the weekly variation. Each day is referenced to the average value of the week in which it is located. The more it exceeds the average value, the redder it is, and the more it falls below the average value, the greener it is. It can be seen that although there are some differences between each day of the week, there is no general pattern. Therefore, we assume that the fluctuation is only based on the general trend of the reports and the difficulty of the word.

<!-- b000163 | heading | pages [6] -->
4 Task 1: Word Attribute Indicators

<!-- b000164 | prose | pages [6] -->
Considering the game characteristics of Wordle, the indicators we constructed should reflect the spelling structure of the word and the ease with which people associate it as much as possible. To achieve this, we constructed the following framework of indicators.

<!-- b000165 | prose | pages [6] -->
• Familiarity: how familiar people are with the word and how commonly the word is used.

<!-- b000166 | prose | pages [6] -->
• Composition features: structural features of words, such as whether they contain the same letters.

<!-- b000167 | furniture | pages [7] -->
Team 2318036

<!-- b000168 | furniture | pages [7] -->
Page 7 of 24

<!-- b000169 | prose | pages [7] -->
• Degree of association: the likelihood that the Wordle will give more valid information (i.e., green or yellow tiles) when the player guesses the word.

<!-- b000170 | prose | pages [7] -->
• Degree of confusion: the degree of similarity between the word and other words. When the degree of similarity is too great, the player may need to spend more times to verify which of the many similar words is the correct answer.

<!-- b000171 | prose | pages [7] -->
Based on the above framework, we constructed 12 indicators:

<!-- b000172 | prose | pages [7] -->
Measured Feature

<!-- b000173 | heading | pages [7] -->
Symbol

<!-- b000174 | prose | pages [7] -->
Meanings 𝐹 Familiarity Frequency of the word 𝑁𝑐 Number of the most repeated letter in the word Composition feature 𝑁𝑣 Number of vowels in the word

<!-- b000175 | prose | pages [7] -->
Frequency that the ith letter of the word appears 𝐿𝐹𝑖 in the ith position of all words. (𝑖= 1, 2, 3, 4, 5) Degree of association 𝐿𝐹𝑠𝑢𝑚 Letter Frequency Sum 𝑁𝐹𝐼2 Number of frequent 2-itmes Number of all the words in 𝐷whose 𝑁𝐷1 Levenshtein distance is 1 from the word Degree of confusion Number of all the words in 𝐷whose 𝑁𝐷2 Levenshtein distance is 2 from the word

<!-- b000176 | caption | pages [7] -->
Table 3: Symbol table of all selected parameters

<!-- b000177 | prose | pages [7] -->
A detailed description of certain symbols are present below:

<!-- b000178 | prose | pages [7] -->
• Number of the most repeated letters (𝑁𝑐): For example, 𝑁𝑐(”apple”) = 2, 𝑁𝑐(”mummy”) = 3.

<!-- b000179 | prose | pages [7] -->
Because players don’t usually try two or three of the same letters at the same time, we predict the greater 𝑁𝑐, the less likely the word is to be guessed.

<!-- b000180 | prose | pages [7] -->
• Letter Frequency of the ith Letter (𝐿𝐹𝑖): For example, the first letter of apple is a, then 𝐿𝐹1(”apple”) is the proportion of words with the first letter a in 𝐷. The greater 𝐿𝐹𝑖is , the greater the probability of a green tile appears at the ith position.

<!-- b000181 | prose | pages [7] -->
• Letter Frequency Sum (𝐿𝐹𝑠𝑢𝑚): Indicator 𝐿𝐹𝑠𝑢𝑚, representing the sum of letter frequency in the word. First, letter frequency(𝐿𝐹) is calculated by:

<!-- b000182 | prose | pages [7, 8] -->
h i 𝐿𝐹(𝑐) = 0 (initialize) (1) ∀ 𝑐∈𝐶 ( 𝑖𝑓𝑐1 = 𝑐2 1 h i ∑︁ 𝐿𝐹(𝑐1) = 𝐿𝐹(𝑐1) +  (repeat) (2) ∀ ∀ 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 0 𝑊∈𝐷 𝑐1∈𝐶 𝑐2∈𝑊 𝐿𝐹(𝑐1) 𝐿𝐹(𝑐1) =   (finally) (3) ∀ 𝑙𝑒𝑛(𝑊) Í 𝑐1∈𝐶 𝑊∈𝐷 Where 𝐶is the alphabet set, 𝐷is the word set, 𝑙𝑒𝑛(𝑤) represent the length of the word.

<!-- b000183 | furniture | pages [8] -->
Team 2318036

<!-- b000184 | furniture | pages [8] -->
Page 8 of 24

<!-- b000186 | prose | pages [8] -->
After calculating 𝐿𝐹, 𝐿𝐹𝑠𝑢𝑚could be produced by summing all characters in a word:

<!-- b000187 | prose | pages [8] -->
5 ∑︁ 𝐿𝐹𝑠𝑢𝑚(”𝑐1𝑐2𝑐3𝑐4𝑐5”) = 𝐿𝐹(𝑐𝑖) (4) 𝑖=1

<!-- b000188 | prose | pages [8] -->
The greater the 𝐿𝐹𝑠𝑢𝑚, the greater the probability of yellow tiles appearing when playing Wordle.

<!-- b000189 | prose | pages [8] -->
• Number of frequent 2-items (𝑁𝐹𝐼2): This indicator count the number of frequent items contained in a word in the frequent 2-itenset(𝐹𝐼2). 𝐹𝐼2 is calculated by FP-Growth algorithm, an algorithm for frequent pattern mining, with supporting degree |𝐷| 10 . Greater 𝑁𝐹𝐼2 increase the probability of information gain by close guesses, so it is assumed to be easier when 𝑁𝐹𝐼2 is high.

<!-- b000190 | prose | pages [8] -->
• Number of 1/2 Levenshtein Distanced Words (𝑁𝐷1, 𝑁𝐷2): Levenshtein distance is the mini- mum number of editing operations required to change from one to the other between two strings, so all words with Levenshtein distance equals to 1 or 2 are all similar words to the answer. When 𝑁𝐷1 and 𝑁𝐷2 are high, player may need to spend more times to verify which of the many similar words is the correct answer, and more likely fail to guess a word.

<!-- b000191 | heading | pages [8] -->
5 Task 2: Predicting Daily Reports & Hard Mode Percentage

<!-- b000192 | heading | pages [8] -->
5.1 Problem Analysis

<!-- b000193 | prose | pages [8] -->
It is obvious that Wordle has become viral last year. People send these iconic Wordle result tweets, attracting more people to try the game and share it. At the beginning of February, shared tweets rise in an exponential rate, then it drops gradually after March. Thus, this tendency could well be captured by SIR(Suspected-Infected-Recovered) model, which is originally intended to explain infectious diseases[9]. Establishing similar dynamic model to explain game user amount fluctuations is also observed in many researches, proved to be successful[5].

<!-- b000194 | heading | pages [8] -->
5.2 Establishment of the Model

<!-- b000195 | prose | pages [8] -->
Like SIR model, we can assume three groups of people: targeted population, current players, and lost players. Targeted population has the potential to become player, and this rate of transformation is proportional to total current players, owing to the advertising effect of their tweets. Therefore, decrease of target population could be written as the multiple of targeted population, current players and a constant 𝛼. For current players, beside new players joining in, there are also players who became tired and give up the game. These group of people is related only to the number of current players and constant 𝛽. With these conditions, a dynamic system could be formulated as follow:

<!-- b000196 | furniture | pages [9] -->
Team 2318036

<!-- b000197 | furniture | pages [9] -->
Page 9 of 24

<!-- b000198 | prose | pages [9] -->
𝜕𝑇 𝜕𝑡= −𝛼· 𝑇· 𝑃  𝜕𝑃 𝜕𝑡= 𝛼· 𝑇· 𝑃−𝛽· 𝑃 (5)  𝜕𝐿 𝜕𝑡= 𝛽· 𝑃

<!-- b000199 | caption | pages [9] -->
Figure 3: two-type player dynamic system

<!-- b000200 | prose | pages [9] -->
However, this model failed to satisfy both the sharp decrease after peaking in February and mild decrease in the second half of the year. After all, while many people might gradually abandon the game, others might maintain their fondness for Wordle. Modelling all players having the same player leaving rate 𝛽might not work well. Therefore, we improved the model by dividing all players into loyal players who has lower tendency to get tired with Wordle and keep sending Wordle tweets, and general players who follow the trend and leave with the trend, Which is named T2PL(Target-2-players-Lost) model. Each two category has a unique decay rate 𝛽and 𝛾. Both types of player’s tweets would have similar effects, so the sum of two categories is used when calculating decrease in potential population. What percentage do players fall into each category also need to be determined. We set variable 𝜏as the rate of new players becoming a loyal player and variable 𝑝as the initial split of two types. In case there were players who wants to try Wordle again after leaving for a while, an additional variable 𝜃is used to describe the lost-return rate, and this means the initial value of lost player 𝐿0 also has to be modeled in advance. Now the final formulation would be:

<!-- b000201 | prose | pages [9] -->
𝜕𝑇 𝜕𝑡= −𝛼𝑇· (𝑃𝑙𝑜𝑦+ 𝑃𝑔𝑒𝑛)  𝜕𝑃𝑙𝑜𝑦 h i = 𝜏· 𝛼𝑇· (𝑃𝑙𝑜𝑦+ 𝑃𝑔𝑒𝑛) + 𝜃𝐿 −𝛽· 𝑃𝑙𝑜𝑦 𝜕𝑡 𝜕𝑃𝑔𝑒𝑛 (6) h i = (1 −𝜏) · 𝛼𝑇· (𝑃𝑙𝑜𝑦+ 𝑃𝑔𝑒𝑛) + 𝜃𝐿 −𝛾· 𝑃𝑔𝑒𝑛  𝜕𝑡 𝜕𝐿 𝜕𝑡= 𝛽· 𝑃𝑙𝑜𝑦+ 𝛾· 𝑃𝑔𝑒𝑛−𝜃𝐿

<!-- b000202 | prose | pages [9] -->
With initial values: 𝑇0, 𝑃𝑙𝑜𝑦0 = 𝑃0 · 𝑝, 𝑃𝑔𝑒𝑛0 = 𝑃0 · (1 −𝑝), 𝐿0

<!-- b000203 | furniture | pages [10] -->
Team 2318036

<!-- b000204 | furniture | pages [10] -->
Page 10 of 24

<!-- b000205 | heading | pages [10] -->
5.3 Solving the Model

<!-- b000206 | prose | pages [10] -->
By estimating a set of initial values (𝛼, 𝛽, 𝛾, 𝑇0, 𝐿0, 𝜏, 𝜃, 𝑝) and observed initial value 𝑃0, the dynamic system can be numerically solved using forward Euler method. Our goal is to fit the dynamic system towards the result curve. The objective function is the mean square error between 1 and the ratio between estimated value and actual value at each sample point. It is re-scaled because the range between maximum and minimum value at the ground truth curve is too large.

<!-- b000207 | prose | pages [10] -->
𝑁 ˆ𝑃𝑖(𝛼, 𝛽, 𝛾, 𝑇0, 𝜏, 𝑝) 2  ∑︁ 1 − min (7) 𝑃𝑖 𝛼,𝛽,𝛾,𝑇0,𝜏,𝑝 𝑡=1

<!-- b000208 | prose | pages [10] -->
Without explicitly solving the function, our team use auto-gradient package (Pytorch) to optimize the parameters. Each parameter is updated by gradient descent. As long as the initial value are roughly the correct scale, it will find the local minimum of the parameters that produce a well-fit curve.

<!-- b000209 | heading | pages [10] -->
5.4 Solution and Result

<!-- b000210 | prose | pages [10] -->
After 5000 epoch of training with learning rate 0.01, we find the optimal value of each variable.

<!-- b000211 | prose | pages [10] -->
𝛼 𝛽 𝛾 𝜃 𝑇0 𝐿0 𝜏 𝑝 5 × 10−7 2 × 10−3 2 × 10−4 initial value 0.02 310000 30000 0.2 0.2 3.03 × 10−7 3.7 × 10−3 2.0 × 10−4 optimal value 0.0228 431193 29918 0.0992 0.1683

<!-- b000212 | caption | pages [10] -->
Table 4: initial value and optimal value of all variable

<!-- b000213 | caption | pages [10] -->
Figure 4: Predicted number of reports. Predicted days are drawn with dotted line.

<!-- b000214 | prose | pages [10, 11] -->
The plotted curve is shown in Figure 4. The model is proved to excellently capture the tendency of reported Wordle result in 2022. In 2023.3.1, it is predicted to have 19367 users sending Wordle results. Because the model cannot provide a range of possible prediction by itself, we estimate by considering the MAPE (Mean Absolute Percentage Error), which is often used as a measurement of prediction accuracy. It is defined as:

<!-- b000215 | furniture | pages [11] -->
Team 2318036

<!-- b000216 | furniture | pages [11] -->
Page 11 of 24

<!-- b000218 | prose | pages [11] -->
𝑛 ˆ𝑃𝑡−𝑃𝑡 MAPE = 100% ∑︁ (8) 𝑛 𝑃𝑡 𝑡=1

<!-- b000219 | prose | pages [11] -->
Given MAPE = 0.083 on observable date, we can assume the result will fall within ±MAPE. Therefore, the estimated region is given as:

<!-- b000220 | prose | pages [11] -->
Confidence Interval(𝑡) = (1 −MAPE) · ˆ𝑃𝑡, (1 + MAPE) · ˆ𝑃𝑡   (9)

<!-- b000221 | prose | pages [11] -->
Therefore, the prediction interval for the number of reports is [17760, 20976].

<!-- b000222 | prose | pages [11] -->
In addition, this model could provide additional insight into the structure of Wordle players. We have plotted the change in each category in 2022. According to Figure5, general players increase rapidly in February and then decrease to a very low level at the end. Loyal players, on the other hand, don’t change much throughout the process. The model predicts that there will be only 19% general players on 31 December 2022 and 21% on 1 March 2023, showing that the majority of players will be loyal and probably more skilled players in the near future.

<!-- b000223 | caption | pages [11] -->
Figure 5: two-type player dynamic system

<!-- b000224 | heading | pages [11] -->
5.5 Hard Mode Percentage Estimation

<!-- b000225 | prose | pages [11, 12] -->
Unlike the trend in the number of reported results, the percentage of scores reported that were played in Hard Mode posting slowly increased from 2% to 10% and then remained stable. This overall trend can perhaps be explained by the change in player structure mentioned above, where loyal players are more likely to choose Hard Mode because of their higher level of play and love for the game. As shown in the figure below, the trend of the percentage of loyal players in the overall player base is basically the same as the trend of the percentage of scores reported that were played in Hard Mode.

<!-- b000226 | furniture | pages [12] -->
Team 2318036

<!-- b000227 | furniture | pages [12] -->
Page 12 of 24

<!-- b000229 | caption | pages [12] -->
Figure 6: Curve of hard mode reports’ percentage and loyal players’ percentage, re-scaled.

<!-- b000230 | prose | pages [12] -->
In addition, there were always small fluctuations in the percentage of reported scores played in Hard Mode around the overall trend, and these fluctuations may be related to the attributes of the word of the day. To explore this relationship, we established a multiple linear regression model with the percentage of Hard Mode reports as the dependent variable, and all indicators reflecting word attributes as independent variables. In order to avoid the influence of the overall trend on the exploration of fluctuations, the percentage of scores reported in the previous day is selected as the control variable.

<!-- b000231 | prose | pages [12] -->
The regression results were as follows (only the results of variables with significant regression coefficients are given here):

<!-- b000232 | prose | pages [12] -->
𝑃𝐻on the previous day 𝐹 𝑁𝑐 𝐿𝐹4 𝐿𝐹𝑠𝑢𝑚 𝑁𝐹𝐼2 0.9608∗∗∗ −6.342 × 10−12∗ 2.776 × 10−3∗∗∗ 0.0291∗ −0.0423∗∗∗ 6.777 × 10−4∗ (2.814 × 10−12) (5.959 × 10−4) (2.761 × 10−4) (0.0111) (0.0113) (0.0110)

<!-- b000233 | caption | pages [12] -->
Table 5: Regression result, showing coefficient and corresponding standard error.

<!-- b000234 | prose | pages [12] -->
Note: *, **, *** represent 𝑝< 0.05, 𝑝< 0.01, 𝑝< 0.001.

<!-- b000235 | prose | pages [12] -->
The results show that 𝐹and 𝐿𝐹𝑠𝑢𝑚have a significant negative effect on the percentage of scores reported that were played in Hard Mode, while 𝑁𝑐, 𝐿𝐹4 and 𝑁𝐹𝐼2 have a significant positive effect on it. And it can be found through the later analysis that these indicators are the important factors that determine the difficulty of words.

<!-- b000236 | prose | pages [12] -->
Select the two attributes with the strongest salience and plot the categorical box plot of the percentage of scores reported that were played in Hard Mode about them. The results show that the percentage of scores reported that were played in Hard Mode is higher when the words contain the same letters, and lower when the words have a higher frequency of letters.

<!-- b000237 | furniture | pages [13] -->
Team 2318036

<!-- b000238 | furniture | pages [13] -->
Page 13 of 24

<!-- b000239 | caption | pages [13] -->
Figure 7: Box plot result

<!-- b000240 | heading | pages [13] -->
6 Task 3: Predicting Report Distribution

<!-- b000241 | heading | pages [13] -->
6.1 Problem Analysis

<!-- b000242 | prose | pages [13] -->
Wordle is an interactive game. When a player fills in a word, Wordle gives feedback and the player chooses a new word based on Wordle’s feedback. Each step of the player’s strategy is related to the word filled in the previous step, which provides so many possibilities for the game to proceed that it is almost impossible to calculate the probability of the player guessing the word within a specified number of times. In order to predict the associated percentages of (1, 2, 3, 4, 5, 6, X) for a future date, we designed a simulation algorithm to simulate the player’s strategy of playing Wordle, and obtained the simulated distribution by performing 5000 simulations for each word.

<!-- b000243 | heading | pages [13] -->
6.2 Establishment of the Model

<!-- b000244 | prose | pages [13] -->
The main idea of the simulation algorithm is: Players randomly select a word from the dictionary to guess, and get the game state of Wordle. For the state of each letter:

<!-- b000245 | prose | pages [13] -->
1. If it is green, only the word with the letter in the corresponding position will be selected for subsequent guesses;

<!-- b000246 | prose | pages [13] -->
2. If it is yellow, only words with that letter in other positions will be selected for subsequent guesses;

<!-- b000247 | prose | pages [13] -->
3. If it is gray and not among the yellow letters, the subsequent guesses will not select words containing this letter.

<!-- b000248 | prose | pages [13] -->
Above process is repeated until the player has succeeded or guessed more than 6 times.

<!-- b000249 | prose | pages [13] -->
Note: Here we assume that players know all the words in the dictionary D.

<!-- b000250 | furniture | pages [14] -->
Team 2318036

<!-- b000251 | furniture | pages [14] -->
Page 14 of 24

<!-- b000252 | heading | pages [14] -->
Algorithm 1 Simulate(𝑊𝑆)

<!-- b000253 | prose | pages [14] -->
Evaluate-Guess(𝑊𝑆,𝑊𝐺) return a game state of wordle. 𝑊𝑆=”tools”, (Note: For example: 𝑊𝐺=”brook”, it return ”NNYMN”. ”Y” means the letter is in the answer and in the correct posi- tion. ”M” means the letter is in the answer but in a different position. ”N” means the letter is not in the answer.)

<!-- b000254 | heading | pages [14] -->
Input: Solution word 𝑊𝑆

<!-- b000255 | prose | pages [14] -->
Output: The list of game states 𝐿𝐺 1: 𝐷𝑊←−𝐷; 2: 𝐿𝐺←−𝜙; 3: for 𝑖from 1 to 6 do random choose a guess word 𝑊𝐺from 𝐷𝑊; 4:

<!-- b000256 | prose | pages [14] -->
𝑆𝑖←−Evaluate-Guess(𝑊𝑆, 𝑊𝐺); 5:

<!-- b000257 | prose | pages [14] -->
𝐿𝐺←−𝐿𝐺 Ð{𝑆𝑖}; 6:

<!-- b000258 | prose | pages [14] -->
if 𝑆𝑖=”YYYYY” then break; 7:

<!-- b000259 | prose | pages [14] -->
end if 8:

<!-- b000260 | prose | pages [14] -->
for 𝑗from 1 to 5 do 9: if 𝑆𝑗 𝑖=”Y” then 10:

<!-- b000261 | prose | pages [14] -->
remove from 𝐷𝑊the words 𝑊satisfying 𝑊𝑗≠𝑊𝑗 𝐺; 11:

<!-- b000262 | prose | pages [14] -->
else if 𝑆𝑗 𝑖=”M” then 12:

<!-- b000263 | prose | pages [14] -->
filter out the word 𝑊satisfying 𝑊𝑘= 𝑊𝑗 𝐺, 𝑘≠𝑗from 𝐷𝑤; 13:

<!-- b000264 | prose | pages [14] -->
else if 𝑆𝑗 𝑖=”N” & 𝑊𝑗 𝐺∉{𝑊𝑘 𝐺|𝑆𝑘 𝑖=”M”, 𝑘= 0, 1, 2, 3, 4} then 14:

<!-- b000265 | prose | pages [14] -->
remove from 𝐷𝑊the words 𝑊satisfying 𝑊𝑗= 𝑊𝑗 𝐺; 15:

<!-- b000266 | prose | pages [14] -->
end if 16:

<!-- b000267 | prose | pages [14] -->
end for 17: 18: end for 19: return 𝐿𝐺;

<!-- b000268 | prose | pages [14] -->
We subtracted the probabilities on the corresponding points of the simulated distribution and the real distribution, and took the absolute value as error. The value of error is 5.36%, which was not satisfactory. By comparing the mean value of the simulated distribution with the mean value of the real distribution, we found that the mean value of 79.6% of the simulated distribution was larger than that of the real distribution, i.e., the simulation results showed that players needed more attempts to guess. We believe this is due to the fact that players who guessed correctly with fewer attempts were more likely to share their results on Twitter, while players who guessed correctly after many attempts were more likely not to share on Twitter.

<!-- b000269 | prose | pages [14] -->
According to above considerations, we propose P&S(Played and Shared) model. Probability of a player sharing after playing Wordle(either successfully or failed) is defined as 𝑊𝑠𝑖, indicating the willingness to share after making i attempts to success(𝑊𝑠𝑖∈[0, 1]). We corrected the simulated distribution according to 𝑊𝑠𝑖and used gradient descent method to minimize error. The corrected formula is as follows:

<!-- b000270 | prose | pages [14, 15] -->
𝑝𝑖𝑗𝑊𝑠𝑗 ˆ𝑝𝑖𝑗= × 100% (10) 𝑘=1 𝑝𝑖𝑘𝑊𝑠𝑘 Í5 𝑝𝑖𝑗is the percentage of players who succeeded after j attempts for the ith word, ˆ𝑝𝑖𝑗is the percentage of players who succeeded after j attempts for the ith word after correction.

<!-- b000271 | furniture | pages [15] -->
Team 2318036

<!-- b000272 | furniture | pages [15] -->
Page 15 of 24

<!-- b000274 | prose | pages [15] -->
The optimal parameters obtained by the gradient descent method are shown below:

<!-- b000275 | prose | pages [15] -->
𝑊𝑠1 𝑊𝑠2 𝑊𝑠3 𝑊𝑠4 𝑊𝑠5 𝑊𝑠6 𝑊𝑠7 1.000 0.993 0.940 0.755 0.698 0.696 0.301

<!-- b000276 | caption | pages [15] -->
Table 6: Scale parameters’ optimal value

<!-- b000277 | prose | pages [15] -->
We corrected the simulated distribution with the above parameters and compared it with the real distribution again, and found that the corrected distribution could fit the distribution of the data set better. The error is reduced from 5.36% to 1.50%, and only 45.6% of the simulated distributions have a mean value greater than the real distribution, which is a more desirable result. We named this model P&S Model, where P stands for playing the game and S stands for sharing the results.

<!-- b000278 | caption | pages [15] -->
Figure 8: Visualize the simulated distribution versus the true distribution, before and after correction.

<!-- b000279 | heading | pages [15] -->
6.3 Predict Confidence and Uncertainties

<!-- b000280 | prose | pages [15] -->
Basedon our model, the distribution of the word EERIE on March 1, 2023 is (0, 0, 9%, 29%, 45%, 14%, 3%). Because the value of error is 1.50%, we speculated that the probability of each point of the real distri- bution will probably fall within plus or minus 1.50% of the simulated distribution.

<!-- b000281 | prose | pages [15] -->
Due to the stochastic nature of the simulation, the prediction results of the P&S Model will not always be the same, which will lead to some uncertainty in the prediction results.

<!-- b000282 | furniture | pages [16] -->
Team 2318036

<!-- b000283 | furniture | pages [16] -->
Page 16 of 24

<!-- b000284 | heading | pages [16] -->
7 Task 4: Word Difficulty Classification

<!-- b000285 | prose | pages [16] -->
In the previous section we built a model to analyse the possible distribution for each word. However, puzzle designers seeking insight from this model would find it difficult to use this information. It is expected that a comprehensive label describing the difficulty of the puzzle will be created and that the classification into these categories will be produced by explainable attributes of each 5-letter word. Therefore, we perform a cluster analysis on the score distributions in the dataset, hoping to identify 3 types of difficulty: Easy, Medium and Hard. We then enumerate all possible attributes in each word and run a classification algorithm into three difficulty levels using these attributes. In this way, the most important attributes for classification could be discovered, and then we could gain a thoughtful understanding of how each category relates to the word feature.

<!-- b000286 | heading | pages [16] -->
7.1 Cluster Analysis

<!-- b000287 | prose | pages [16] -->
For clustering algorithms, we compare two commonly used methods: k-means[3] and Gaussian Mixture Model (GMM)[7].

<!-- b000288 | prose | pages [16] -->
K-means tries to divide the data into k categories, generating k category centroids 𝐶𝑘. For each point, its nearest centroid is expected to be the centroid of the category to which it belongs. By initiating several random points as the centroid, it is iteratively updated using this formula:

<!-- b000289 | prose | pages [16] -->
𝑥𝑛∈𝐶(𝑡+1) 𝑑(𝑥𝑛, 𝑐(𝑡) , if 𝑘= arg min 𝑘) (11) 𝑘 𝑘 1 𝑐(𝑡+1) ∑︁ 𝑥𝑛 = (12) 𝑘 |𝐶(𝑡+1) | 𝑥𝑛∈𝐶(𝑡+1) 𝑘 𝑘

<!-- b000290 | prose | pages [16] -->
GMM considers all observed data sampled from k normal distributions N𝑘(𝜇𝑘, Σ𝑘) and tries to find the maximum likelihood pairs of parameters 𝜇𝑘, Σ𝑘. It can be solved using the expectation maximisation (EM) algorithm. In the E-step, the responsibility (posterior distribution of clusters) of each sample point is calculated.

<!-- b000291 | prose | pages [16] -->
𝑝(𝑥𝑛; 𝜇(𝑡) 𝑘, Σ(𝑡) 𝑘) 𝑝(𝑡)(𝑘|𝑥𝑛) = (13) 𝑖=1 𝑝(𝑥𝑛; 𝜇(𝑡) 𝑖, Σ(𝑡) Í𝐾 𝑖)

<!-- b000292 | prose | pages [16] -->
Then in M-step, the responsibility is fixed and the model parameters are updated as:

<!-- b000293 | prose | pages [16] -->
𝑛=1 𝑝(𝑡)(𝑘|𝑥𝑛)(𝑥𝑛−𝜇(𝑡+1) )(𝑥𝑛−𝜇(𝑡+1) Í𝑁 Í𝑁 )𝑇 𝑛=1 𝑝(𝑡)(𝑘|𝑥𝑛)𝑥𝑛 𝜇(𝑡+1) Σ(𝑡+1) 𝑘 𝑘 = = (14) 𝑘 𝑘 Í𝑁 Í𝑁 𝑛=1 𝑝(𝑡)(𝑘|𝑥𝑛) 𝑛=1 𝑝(𝑡)(𝑘|𝑥𝑛)

<!-- b000294 | prose | pages [16] -->
After convergence, each sample point belongs to the distribution with maximum responsibility.

<!-- b000295 | prose | pages [16] -->
𝑥𝑛∈𝐶𝑘, if 𝑘= arg max 𝑝(𝑘|𝑥𝑛) (15) 𝑘

<!-- b000296 | prose | pages [16, 17] -->
In order to decide the better algorithm and choose the appropriate number of clusters, we compare the results using the Silhouette Coefficient[8] and the Calinski-Harabasz Index[6]. The silhouette coefficient is obtained by averaging the silhouette values of all sample points, which describe how close the sample point is to its cluster compared to others. The greater silhouette values is, more distinguishable the cluster would be. Its mathematical formulation is:

<!-- b000297 | furniture | pages [17] -->
Team 2318036

<!-- b000298 | furniture | pages [17] -->
Page 17 of 24

<!-- b000300 | prose | pages [17] -->
𝑁 𝑏(𝑥𝑛) −𝑎(𝑥𝑛) 𝑆𝐶= 1 ∑︁ 𝑠(𝑥𝑛) , 𝑠(𝑥𝑛) = (16) 𝑁 max(𝑎(𝑥𝑛), 𝑏(𝑥𝑛) 𝑖=1

<!-- b000301 | prose | pages [17] -->
1 ∑︁ Where : 𝑎(𝑥𝑛) = 𝑑(𝑥𝑚, 𝑥𝑛) (same cluster closeness) 𝐶𝑖−1 𝑥𝑚∈𝐶𝑖,𝑚≠𝑛 1 ∑︁ 𝑏(𝑥𝑛) = min 𝑑(𝑥𝑚, 𝑥𝑛) (different cluster closeness) 𝐶𝑗 𝑗≠𝑖 𝑥𝑚∈𝐶𝑗

<!-- b000302 | prose | pages [17] -->
The Calinski-Harabasz index is a ratio between the variance of the cluster centres and the variance of each cluster. If the centres of each cluster are spread apart and the sample points are clustered around each cluster centroids, then the Calinski-Harabasz Index is expected to be high.

<!-- b000303 | prose | pages [17] -->
i.hÍ𝐾 hÍ𝐾 𝑥∈𝐶𝑘||𝑥−𝑐𝑘||2 𝑘=1 |𝐶𝑘| · ||𝑐𝑘−𝜇||2 Í 𝑘=1 i (𝑐𝑘is the centriod of 𝐶𝑘) C-H Index = 𝐾−1 𝑁−𝐾 (17) Score of both indicators in shown in the table:

<!-- b000304 | prose | pages [17] -->
k-means (3) GNN(3) k-means(2) GNN(2) silhouette coefficient 0.369 0.306 0.425 0.366 Calinski-Harabasz index 311.9 203.4 329.6 122.3

<!-- b000305 | caption | pages [17] -->
Table 7: scores for different kinds of cluster algorithm

<!-- b000306 | prose | pages [17] -->
Finally, we decide to create 3 clusters using k-means. Although 2 class k-means seems to have a higher evaluation score, detailed classification is better for drawing more specific conclusions, and the performance of 3 class k-means is not too far from it. To observe the clustering effect more intuitively, we use the t-SNE algorithm to reduce the data to 2 dimensions. Figure 9 visualize all three clusters, labeled ”easy”, ”medium” and ”hard” according to expected attempts of each class centroids. Therefore, we successfully find a method to allocate each word into three difficulties based on how they are reported to be solved.

<!-- b000307 | heading | pages [17] -->
7.2 Difficulty Classification

<!-- b000308 | prose | pages [17, 18] -->
Now that all the word features have been quantized into 12 numerical values and assigned a difficulty level, a supervised classification model could be built to predict the difficulty level based on word attributes. We use Random Forest classification[2] in this task. Random Forest has been shown to provide stable classification results on a wide range of data. The motivation of the algorithm is to reduce variance by bagging on the training set and feature space. B decision tree is trained on a sampled set of all data with certain feature is masked, and classification result is produced by summarising all 𝐵votes from each decision tree.

<!-- b000309 | furniture | pages [18] -->
Team 2318036

<!-- b000310 | furniture | pages [18] -->
Page 18 of 24

<!-- b000311 | caption | pages [18] -->
Figure 9: Visualized 3 clusters projected on 2 dimensions

<!-- b000313 | prose | pages [18] -->
𝑓𝑏= arg min 𝑓𝑏𝐿( 𝑓𝑏(𝑋𝑏),𝑌𝑏) (𝑏= 1, ..., 𝐵) (train) (18)

<!-- b000314 | prose | pages [18] -->
𝐵 ˆ𝑓= 1 ∑︁ 𝑓𝑏(𝑋) (predict) (19) 𝐵 𝑏=1

<!-- b000315 | prose | pages [18] -->
All record is split into 80% training set and 20% testing set. After training the model, Classification metric on test data is shown in table 8. It seems that classification score is generally even among each categories and accuracy(0.68) is high, meaning the model could successfully grasp the relation between word attributes and its difficulty.

<!-- b000316 | prose | pages [18] -->
precision recall f1-score support number easy 0.63 0.70 0.67 27 medium 0.77 0.68 0.72 34 hard 0.58 0.64 0.61 11 accuracy 0.68 72 weighted average 0.69 0.69 0.68 72

<!-- b000317 | caption | pages [18] -->
Table 8: Classification metric.

<!-- b000318 | prose | pages [18] -->
Beside total accuracy, precision, recall and f1-score is calculated on each categories and averaged by weight.

<!-- b000319 | prose | pages [18] -->
Our model also provides insight into how each feature affects puzzle difficulty. Figure 10 shows the correlation of each feature with word difficulty. This factor is obtained by assigning values to each difficulty level (easy=0, medium=1, hard=2) and calculating the covariance matrix with each feature.

<!-- b000320 | furniture | pages [19] -->
Team 2318036

<!-- b000321 | furniture | pages [19] -->
Page 19 of 24

<!-- b000322 | caption | pages [19] -->
Figure 10: Each feature’s correlation with difficulty, ranked by its importance in model

<!-- b000323 | prose | pages [19] -->
The pattern is very obvious: if a word is used more often (familiarity) or can be easily associated with another word, it would have a negative correlation with difficulty, i.e. it is easier to guess. Furthermore, if it is often confused with another word, it becomes more difficult. The effect of compositional features can also be explained: It is relatively less instinctive to try words with multiple identical letters, and human players prefer to solve Wordle by cracking the vowel first, which makes the word with multiple vowels easier. Therefore, the number of same letters is positively correlated with difficulty, and the number of vowels is negatively correlated with difficulty.

<!-- b000324 | prose | pages [19] -->
Based on our model, ”EERIE” is classified as a hard answer. Precision of this category is 0.58 on testing set.

<!-- b000325 | heading | pages [19] -->
7.3 Sensitivity Analysis

<!-- b000326 | prose | pages [19] -->
Sensitivity analysis determines how the variations of an independent variable affect a particular dependent result under a given set of assumptions, in which way we can test the robustness of the results. To test whether our models’ results are sensitive to the change of the input parameters, we need to carry out sensitivity analysis. In the actual data calculation, the percentages in data may not sum to 100% due to rounding. In order to analyze the stability of our clustering model when the original data is inaccurate, we use sensitivity analysis to evaluate the model. To simulate the loss of precision caused by rounding, we add a stochastic disturbance term 𝜀𝑖to the data. We assume the stochastic disturbance fluctuates randomly in the range of 5% of the original data. We define the data after adding the stochastic disturbance as:

<!-- b000327 | prose | pages [19] -->
𝑝′ 𝑖𝑗= 𝑝𝑖𝑗× 𝜀𝑖 𝜀𝑖∼U(0.95, 1.05) (20)

<!-- b000328 | prose | pages [19] -->
Then, we use the new data for clustering. By comparing the clustering results with and without stochastic disturbance, we find that 3.34% of the clustering results changed, which indicates that the clustering results were not seriously affected by data errors and our model is relatively stable.

<!-- b000329 | furniture | pages [20] -->
Team 2318036

<!-- b000330 | furniture | pages [20] -->
Page 20 of 24

<!-- b000331 | prose | pages [20] -->
Easy Medium Hard without stochastic disturbance 133 153 73 with stochastic disturbance 132 159 68

<!-- b000332 | caption | pages [20] -->
Table 9: Clustering result with or without disturbance

<!-- b000333 | heading | pages [20] -->
8 Task 5: Other Features

<!-- b000334 | heading | pages [20] -->
8.1 Fluctuations in the Number of Reported Results

<!-- b000335 | prose | pages [20] -->
Similar to the change in the percentage of scores reported that were played in Hard Mode, the number of reported results always fluctuates up and down around the overall trend. Since people are always more willing to share out their better scores, we speculate that this fluctuation may be related to the difficulty of the word. To explore the relationship between the two, we subtracted the results fitted by the T2PL Model in part 4 from the real number of reported results and used it as the dependent variable, and used the difficulty level derived from clustering in part 6 as the independent variable to establish a linear regression model.

<!-- b000336 | prose | pages [20] -->
The results are as follows:

<!-- b000337 | prose | pages [20] -->
𝑅2 Easy Medium Hard 6589.5∗∗∗ −2649.3∗∗∗ 1087.5 0.09 (1143.7) (1371.6) (781.3)

<!-- b000338 | caption | pages [20] -->
Table 10: The effect of word difficulty on the number of reported results

<!-- b000339 | prose | pages [20] -->
Note: Because difficulty level is a categorical variable, dummy variables are set for it in the regression.

<!-- b000340 | prose | pages [20] -->
The regression results show that the difficulty of the word can explain the change of the number of reported results to some extent. Specifically, the number of reported results will be 6589.5 higher than the fitted results when the word is easy, 1087.5 higher than the fitted results when the word is moderately difficult, and 2649.3 less than the fitted results when the word is hard. We corrected the interval predicted by the T2PL Model. Because the word EERIE is hard, so we subtracted 2649 from the endpoint value of the original interval at the same time to obtain the corrected prediction interval [15111, 18327].

<!-- b000341 | heading | pages [20] -->
8.2 Effect of Word Difficulty on Hard Mode Reports Percentage

<!-- b000342 | prose | pages [20] -->
Combining the findings from Part 5 and Part 7, we can find that the word attributes that affect the percentage of scores reported that were played in Hard Mode happen to be important attributes that affect the difficulty of the words, so it is reasonable to believe that there is some relationship between the percentage of scores reported that were played in Hard Mode and the difficulty of the words. Similar to 7.1, we explored the relationship by creating a linear regression equation (adding 𝑃𝐻on the previous day as a control variable, and the same for each of the following regressions).

<!-- b000343 | prose | pages [20] -->
The results are as follows:

<!-- b000344 | furniture | pages [21] -->
Team 2318036

<!-- b000345 | furniture | pages [21] -->
Page 21 of 24

<!-- b000346 | prose | pages [21] -->
Easy Hard −0.0021938∗∗∗ 0.0021471∗∗∗ (0.0005296) (0.0006389)

<!-- b000347 | caption | pages [21] -->
Table 11: The effect of word difficulty on the percentage of reported Hard Mode results.

<!-- b000348 | prose | pages [21] -->
Note: This section replaces dummy variables of moderate difficulty with constant terms, so the coefficients of median are no longer reported.

<!-- b000349 | prose | pages [21] -->
Surprisingly, the percentage of scores reported that were played in Hard Mode increases when the word is difficult, while decreasing when the word is easy. To investigate the reason for this phenomenon, we ran another two regressions with the number of scores reported that were played in Normal Mode (N-H) and the number of scores reported that were played in Hard Mode as dependent variables.

<!-- b000350 | prose | pages [21] -->
The results are as follows:

<!-- b000351 | prose | pages [21] -->
Easy Hard 6374∗∗∗ −5125∗∗∗ 𝑁−𝐻 (1430) (1718)

<!-- b000352 | prose | pages [21] -->
166.8 229.0 𝐻 (90.27) (158.5)

<!-- b000353 | caption | pages [21] -->
Table 12: The effect of word difficulty on 𝑁−𝐻and 𝐻

<!-- b000354 | prose | pages [21] -->
It can be found that the number of scores reported that were played in Normal Mode decreases significantly when the word is difficult, and on the contrary, increases significantly when the word is easy. While the word difficulty has no significant effect on the number of scores reported that were played in Hard Mode. Therefore, we can analyze the reason for this strange phenomenon: players who choose Hard Mode may have a higher level of word guessing and enjoy the game more, so they are able to maintain a more stable level of guessing the correct word even when the word difficulty increases. Furthermore, they are eager to share their game results even if they cannot guess the word. But players in Normal Mode may not share their game results when they cannot guess the word. As a result, when the word is difficult, the percentage of scores reported that were played in Hard Mode increases.

<!-- b000355 | heading | pages [21] -->
9 Strengths and Weaknesses

<!-- b000356 | heading | pages [21] -->
9.1 Strengths

<!-- b000357 | prose | pages [21] -->
1. The selection of evaluation indicators is scientific and easy to understand. We have taken into account the game characteristics of Wordle and constructed four categories of indicators that can comprehensively reflect the spelling structure of words and the ease with which people associate it.

<!-- b000358 | prose | pages [21, 22] -->
2. The model is constructed with full consideration of the realistic situation and has good interpretability. Considering the faithfulness of players to Wordle, the T2PL Model is improved on the basis of SIR Model by dividing players into two categories: general players and loyal players. The results prove that this improvement enables the model to simulate and explain the changing trend of the number of reported results very well. The P&S Model, based on the simulation of players’ strategies of guessing words, also sets the sharing probability for players with different numbers of tries, which well simulates the psychological characteristics of people.

<!-- b000359 | furniture | pages [22] -->
Team 2318036

<!-- b000360 | furniture | pages [22] -->
Page 22 of 24

<!-- b000362 | prose | pages [22] -->
3. The consideration is very comprehensive. When exploring the trends in the number of reported results and the percentage of scores reported that were played in Hard Mode, we analyzed not only their overall trends, but also their fluctuations around the overall trends. Furthermore, we explained the reasons for the formation of the fluctuations. Based on the results of this analysis, we revised the prediction interval of the first question.

<!-- b000363 | prose | pages [22] -->
4. The models are interlinked and corroborate each other. The indicators we constructed to reflect word attributes were applied to both the analysis in Part 5 and Part 7. The distribution of EERIE predicted by the P&S Model was clustered for difficulty, and the result was consistent with that of the classifier in Part 7.

<!-- b000364 | prose | pages [22] -->
5. Overfitting problem is avoided. Considering that the amount of data is not very large, we did not use a model containing a large number of parameters to avoid the overfitting problem.

<!-- b000365 | heading | pages [22] -->
9.2 Weaknesses

<!-- b000366 | prose | pages [22] -->
1. There is still a gap between the model and the reality. Different people will use different strate- gies to guess word, and different people have different vocabularies, but we did not sufficiently consider in the P&S Model.

<!-- b000367 | prose | pages [22] -->
2. The accuracy of the classification model is not high enough. The accuracy of the classifier in Part 7 is only 68%, which is not particularly good, probably because we omitted some characteristics of the words when constructing the indicators.

<!-- b000368 | heading | pages [22] -->
9.3 Further Discussion

<!-- b000369 | heading | pages [22] -->
9.3.1 Model Improvement

<!-- b000370 | prose | pages [22] -->
Considering that different players have different strategies and vocabularies, we can use different algorithms to simulate different players’ strategies, use different lexicons to simulate different players’ vocabularies, and finally use the optimization algorithm to calculate the proportion of each type of player in the overall players.

<!-- b000371 | heading | pages [22] -->
9.3.2 Model Extension

<!-- b000372 | prose | pages [22] -->
The T2PL Model we constructed can well simulate the popularity of Wordle and explains the changes in the structure of the players. By modifying some parameters, this model can be applied to other games.

<!-- b000373 | furniture | pages [23] -->
Team 2318036

<!-- b000374 | furniture | pages [23] -->
Page 23 of 24

<!-- b000375 | heading | pages [23] -->
References

<!-- b000376 | references | pages [23] -->
[1] Benton J Anderson and Jesse G Meyer. Finding the optimal human strategy for wordle using max-

<!-- b000377 | references | pages [23] -->
imum correct letter probabilities and reinforcement learning. arXiv preprint arXiv:2202.00557,

<!-- b000378 | references | pages [23] -->
2022.

<!-- b000379 | references | pages [23] -->
[2] Leo Breiman. Random forests. Machine learning, 45:5–32, 2001.

<!-- b000380 | references | pages [23] -->
[3] John A Hartigan and Manchek A Wong. Algorithm as 136: A k-means clustering algorithm.

<!-- b000381 | references | pages [23] -->
Journal of the royal statistical society. series c (applied statistics), 28(1):100–108, 1979.

<!-- b000382 | references | pages [23] -->
[4] Peter G Jensen, Kim G Larsen, and Marius Mikuˇcionis. Playing wordle with uppaal stratego. In

<!-- b000383 | references | pages [23] -->
A Journey from Process Algebra via Timed Automata to Model Learning: Essays Dedicated to

<!-- b000384 | references | pages [23] -->
Frits Vaandrager on the Occasion of His 60th Birthday, pages 283–305. Springer, 2022.

<!-- b000385 | references | pages [23] -->
[5] Xian Jiang, Jing Hua, and Yimin Li. Dynamic research on game communication. Mathematic in

<!-- b000386 | references | pages [23] -->
Practice and Theory, (277-283), 2016.

<!-- b000387 | references | pages [23] -->
[6] Ujjwal Maulik and Sanghamitra Bandyopadhyay. Performance evaluation of some clustering

<!-- b000388 | references | pages [23] -->
algorithms and validity indices. IEEE Transactions on pattern analysis and machine intelligence,

<!-- b000389 | references | pages [23] -->
24(12):1650–1654, 2002.

<!-- b000390 | references | pages [23] -->
[7] Douglas A Reynolds et al. Gaussian mixture models. Encyclopedia of biometrics, 741(659-663),

<!-- b000391 | references | pages [23] -->
2009.

<!-- b000392 | references | pages [23] -->
[8] Peter J. Rousseeuw. Silhouettes: A graphical aid to the interpretation and validation of cluster

<!-- b000393 | references | pages [23] -->
analysis. Journal of Computational and Applied Mathematics, 20:53–65, 1987.

<!-- b000394 | references | pages [23] -->
[9] David Smith, Lang Moore, et al. The sir model for spread of disease-the differential equation

<!-- b000395 | references | pages [23] -->
model. Convergence, 2004.

<!-- b000396 | references | pages [23] -->
[10] Daniel Victor. Wordle is a love story. The New York Times, 2022.

<!-- b000397 | references | pages [23] -->
[11] Wikipedia contributors. Wordle Wikipedia, the free encyclopedia. https://en.wikipedia.

<!-- b000398 | references | pages [23] -->
org/w/index.php?title=Wordle&oldid=1139735175, 2023.

<!-- b000399 | references | pages [24] -->
Dear Sir/Madam:

<!-- b000400 | references | pages [24] -->
Hello, we are a group of Wordle fanatics. We wake up every day to new Wordle puzzles on your

<!-- b000401 | references | pages [24] -->
app. The game has certainly brought a lot of joy to our daily lives, and we want to do something to

<!-- b000402 | references | pages [24] -->
improve the game in return. So we are building a mathematical model of all Twitter Wordle reports in

<!-- b000403 | references | pages [24] -->
2022. We hope our analysis can help your team improve Wordle.

<!-- b000404 | references | pages [24] -->
Because the rules of Wordle are fixed, perhaps the most (and only) challenging part of running

<!-- b000405 | references | pages [24] -->
the game is choosing an appropriate word. But how do we know if a word is appropriate enough?

<!-- b000406 | references | pages [24] -->
Is it better to be common or rare? And more fundamentally, how hard should the puzzle be? To

<!-- b000407 | references | pages [24] -->
answer these questions, we need to consider the complex relationship between four important factors:

<!-- b000408 | references | pages [24] -->
word features, distribution of guessing times, puzzle difficulty, and number of players. We could build

<!-- b000409 | references | pages [24] -->
models to explore them and the relation between.

<!-- b000410 | references | pages [24] -->
First, we extract 12 indicators from each word, measuring its familiarity (how often it is used),

<!-- b000411 | references | pages [24] -->
degree of association, degree of confusion, and word composition features, including all dimensions

<!-- b000412 | references | pages [24] -->
of how different words influence guessing.

<!-- b000413 | references | pages [24] -->
Next, we modelled the general trend of total reports with a dynamic system called Target-two-

<!-- b000414 | references | pages [24] -->
Players-Lost (T2PL), dividing players into general and loyal two categories. This model can predict

<!-- b000415 | references | pages [24] -->
future report numbers (for example, reports on 1 March are expected to fall between [17760, 20976]).

<!-- b000416 | references | pages [24] -->
It can also explain player structues, shows that most Wordle players now are loyal players.

<!-- b000417 | references | pages [24] -->
Then we try to predict the solution distribution using simulation algorithms. To improve the result,

<!-- b000418 | references | pages [24] -->
the distribution is rescaled by considering how likely people would share their result if they received a

<!-- b000419 | references | pages [24] -->
different score, hence it is called P&S (Played and Shared) Model. For any word (e.g. ”eerie”) the

<!-- b000420 | references | pages [24] -->
distribution is expected to be (0, 0, 9%, 29%, 45%, 14%, 3%) according to P&S Model.

<!-- b000421 | references | pages [24] -->
The difficulty of each puzzle needs to be defined. We run k-means on the report distributions

<!-- b000422 | references | pages [24] -->
and categorize them into 3 types, labelled easy, medium and hard. Then we classify word attributes

<!-- b000423 | references | pages [24] -->
into three difficulty levels. We know the difficulty of each word (the example ”eerie” used above is of

<!-- b000424 | references | pages [24] -->
course labelled hard) and we know how indicators affect word difficulty from correlation analysis.

<!-- b000425 | references | pages [24] -->
The last piece of the puzzle is the relationship between word difficulty and number of reports.

<!-- b000426 | references | pages [24] -->
Using linear regression, we found that easier Wordle puzzles encourage more shared tweets. We also

<!-- b000427 | references | pages [24] -->
discovered that word attribute could influence the percentage of Hard Mode players. Although this is

<!-- b000428 | references | pages [24] -->
a little counterintuitive, we ultimately explain this by saying that Normal Mode players are less likely

<!-- b000429 | references | pages [24] -->
to share when the word is difficult, while Hard Mode players are not.

<!-- b000430 | references | pages [24] -->
For your team, we wonder if our model can be used to predict player response before each puzzle

<!-- b000431 | references | pages [24] -->
is released and estimate the number of future players. Also, a difficult word might not be an appropriate

<!-- b000432 | references | pages [24] -->
choice as it might discourage intermediate players from sharing their results. We recommend words

<!-- b000433 | references | pages [24] -->
with only one or two indicators that make it difficult, so it doesn’t fall into the hard category. If the

<!-- b000434 | references | pages [24] -->
chosen indicators that make words difficult could vary from day to day (e.g. one day with less word

<!-- b000435 | references | pages [24] -->
frequency, another day with less vowels), it might even give daily Wordle players a sense of freshness.

<!-- b000436 | references | pages [24] -->
We would be happy to discuss the game further with your team. We look forward to playing great

<!-- b000437 | references | pages [24] -->
Wordle puzzles in the future.

<!-- b000438 | references | pages [24] -->
Yours sincerely,

<!-- b000439 | furniture | pages [24] -->
Team #2318036
