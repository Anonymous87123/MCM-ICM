# P-C-2023-2322645-8a06f4dc

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
2023 Problem Chosen

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
C

<!-- b000005 | title | pages [1] -->
2322645

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | prose | pages [1] -->
With the rising popularity of Wordle, people have eagerly taken to Twitter to report their results daily by the tens of thousands. Three very natural questions arise regarding this data: (1) Can we use this data to predict the difficulty of a given target word in Wordle? (2) Can we use this data to predict future Wordle player reporting trends? (3) How does the difficulty of given target word affect player reporting and results? In our paper, we develop a comprehensive Bayesian model consisting of three submodels which predict the distribution of the number of guesses, number of reported results on Twitter and the number of reporting players playing in hard mode.

<!-- b000008 | prose | pages [1] -->
Initially, we decompose words into quantifiable traits associated with rel- evant difficulty characteristics. Most notably, we formulate a novel Wordle- specific entropy measure we call Subset Entropy which effectively quantifies the average amount of information revealed by typical players after initial guesses. We also develop a method to represent the distribution of player attempts, and hence the observed difficulty of a word, using just two values α, β corresponding to the cumulative mass function of the Beta distribution. We use a preliminary Lasso regression to isolate the most relevant predictors of word difficulty, which we then use in our Bayesian model.

<!-- b000009 | prose | pages [1] -->
Our Bayesian model predicts, for a given date and word, the reported difficulty of a word, the number of player reports, and the number of players reporting playing in hard-mode. To accomplish these three tasks, it is made up of three submodels which are conditionally independent given the data, making it efficient to sample from its posterior using Markov Chain Monte- Carlo (MCMC).

<!-- b000010 | prose | pages [1] -->
We find that a word having a higher number of unique letters, usage frequency in English, average number of revealed yellow squares over all guesses, and Subset Entropy all make a word easier for players to guess. We also find that higher word difficulty decreases the number of player reports. Under the assumption that the Times choose words randomly, this can be interpreted as a causal effect.

<!-- b000011 | prose | pages [1] -->
Our model is able to predict outcomes for new data and retrodict for old data. Our model gives gives a 95% prediction interval that between 20238 and 27876 players will report results for “eerie” on March 1, 2023 and that it will be in the 50th percentile of difficulty. Most notably, our model does not just provide such simple point estimates and prediction intervals, but full posterior distributions.

<!-- b000012 | keywords | pages [1] -->
Keywords: Entropy, Lasso regression, MCMC, Bayesian methods,

<!-- b000013 | prose | pages [1] -->
Causal inference

<!-- b000014 | contents | pages [2] -->
How many Wordle words will Wordle guessers guess if

<!-- b000015 | contents | pages [2] -->
Wordle’s Wednesday Wordle word is “Eerie”?

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1 Introduction

<!-- b000018 | contents | pages [2] -->
3

<!-- b000019 | contents | pages [2] -->
2 Data

<!-- b000020 | contents | pages [2] -->
3

<!-- b000021 | contents | pages [2] -->
2.1

<!-- b000022 | contents | pages [2] -->
Data cleaning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000023 | contents | pages [2] -->
3

<!-- b000024 | contents | pages [2] -->
2.2

<!-- b000025 | contents | pages [2] -->
Wordbank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
4

<!-- b000027 | contents | pages [2] -->
3 Word & Difficulty Representation

<!-- b000028 | contents | pages [2] -->
4

<!-- b000029 | contents | pages [2] -->
3.1

<!-- b000030 | contents | pages [2] -->
Vowels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
5

<!-- b000032 | contents | pages [2] -->
3.2

<!-- b000033 | contents | pages [2] -->
Usage

<!-- b000034 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
5

<!-- b000036 | contents | pages [2] -->
3.3

<!-- b000037 | contents | pages [2] -->
Green & Yellow Tiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
5

<!-- b000039 | contents | pages [2] -->
3.4

<!-- b000040 | contents | pages [2] -->
Unique Letters

<!-- b000041 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
6

<!-- b000043 | contents | pages [2] -->
3.5

<!-- b000044 | contents | pages [2] -->
Entropies

<!-- b000045 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
6

<!-- b000047 | contents | pages [2] -->
3.6

<!-- b000048 | contents | pages [2] -->
Representation of word difficulty . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
8

<!-- b000050 | contents | pages [2] -->
4 Modeling Methodology

<!-- b000051 | contents | pages [2] -->
9

<!-- b000052 | contents | pages [2] -->
4.1

<!-- b000053 | contents | pages [2] -->
Lasso regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
9

<!-- b000055 | contents | pages [2] -->
4.2

<!-- b000056 | contents | pages [2] -->
Bayesian models for prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
10

<!-- b000058 | contents | pages [2] -->
5 Model Results

<!-- b000059 | contents | pages [2] -->
14

<!-- b000060 | contents | pages [2] -->
5.1

<!-- b000061 | contents | pages [2] -->
Interpretation of parameter posteriors . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
14

<!-- b000063 | contents | pages [2] -->
5.2

<!-- b000064 | contents | pages [2] -->
Retrodiction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
15

<!-- b000066 | contents | pages [2] -->
5.3

<!-- b000067 | contents | pages [2] -->
Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
15

<!-- b000069 | contents | pages [2] -->
5.4

<!-- b000070 | contents | pages [2] -->
Difficulty representation

<!-- b000071 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
16

<!-- b000073 | contents | pages [2] -->
6 Model Evaluation

<!-- b000074 | contents | pages [2] -->
18

<!-- b000075 | contents | pages [2] -->
6.1

<!-- b000076 | contents | pages [2] -->
Limitations

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
18

<!-- b000079 | contents | pages [2] -->
6.2

<!-- b000080 | contents | pages [2] -->
Strengths

<!-- b000081 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
18

<!-- b000083 | contents | pages [2] -->
7 Conclusion

<!-- b000084 | contents | pages [2] -->
19

<!-- b000085 | contents | pages [2] -->
2

<!-- b000086 | furniture | pages [3] -->
Team # 2322645

<!-- b000087 | furniture | pages [3] -->
Page 3 of 22

<!-- b000088 | heading | pages [3] -->
1 Introduction

<!-- b000089 | prose | pages [3] -->
Wordle is a language-based game currently owned by the New York Times that became a viral sensation in early 2022. The goal of the game is simple to understand: At the the start of each day there is a 5-letter target word that players have to guess. Players have six tries to do so, and attempt to get the word in as few attempts as possible, each time using a valid English word.

<!-- b000090 | prose | pages [3] -->
There are 11,881,376 possible 5-letter words if taking every possible sequence of five letters. Even restricting it to words found in English dictionaries and those in common usage today would only drop it down to around 12,000 and 4,000 words respectively[2]. For a person to randomly guess a target word in six tries would statistically be almost impossible. This, however, is where tile color feedback comes into play. For a given guess word, for each letter Wordle returns a green tile if the corresponding letter is in the target word and in the right location, a yellow tile if the corresponding letter is in the true word but in the wrong location, and a gray tile if neither of these is true. With this information, most players are able to guess the word from thousands of possibilities within six tries.

<!-- b000091 | prose | pages [3] -->
The game has captured the attention of millions, with people taking to social media to share their guess results and comment on the difficulty for certain words. One Twitter account that has popped up as a result of this trend is “@WordleStats”, a bot that tallies all posted Wordle attempts and the distribution of attempts each day. Via this data, we can discover a wealth of information about Wordle player behavior. Particularly, in this paper we develop a model which utilizes both the trends in twitter reporting and the resulting inferred difficulty of target words gleamed from this data to predict future Wordle statistics.

<!-- b000092 | heading | pages [3] -->
2 Data

<!-- b000093 | heading | pages [3] -->
2.1 Data cleaning

<!-- b000094 | prose | pages [3] -->
Data errors We fixed several errors that appear in the provided data by referencing the Twitter posts of the @WordleStats Twitter bot. These are logged below for full transparency.

<!-- b000095 | prose | pages [3] -->
• Day 239: hardmode 3249 →9249

<!-- b000096 | prose | pages [3] -->
• Day 314: tash →trash

<!-- b000097 | prose | pages [3] -->
• Day 500: hardmode 3667 →2667

<!-- b000098 | prose | pages [3] -->
• Day 525: clen →clean

<!-- b000099 | prose | pages [3] -->
• Day 529: Reported players 2569 →25569

<!-- b000100 | prose | pages [3] -->
• Day 540: na¨ıve →naive (¨ı is not a letter in Wordle)

<!-- b000101 | prose | pages [3] -->
• Day 545: rprobe →probe

<!-- b000102 | prose | pages [3] -->
Percentages to counts Because the percentages of reports in the different categories are rounded and do not necessarily sum to 100, we divided the percentages in each row by their sum to obtain proportions. As our Bayesian model predicts the number of players in each category, we converted these proportions into counts by applying the following method for each row:

<!-- b000103 | furniture | pages [4] -->
Team # 2322645

<!-- b000104 | furniture | pages [4] -->
Page 4 of 22

<!-- b000105 | prose | pages [4] -->
1. Multiply the proportions by the number of reports on that day to obtain “counts” with decimal values

<!-- b000106 | prose | pages [4] -->
2. Round the counts down

<!-- b000107 | prose | pages [4] -->
3. Add 1 back to the counts, in order from the count which was rounded down most to that which was rounded down least, until the total again matches the number of reports on that day.

<!-- b000108 | prose | pages [4] -->
This method gives counts which correspond to the given percentages, are integers, and whose sum is the number of reports on that day.

<!-- b000109 | heading | pages [4] -->
2.2 Wordbank

<!-- b000110 | prose | pages [4] -->
To model 5-letter words and their properties, we rely on the Stanford GraphBase (SGB) word- bank of 5757 5-letter words created by Donald Knuth [6], which provides a good approximation of the set of words that a player could guess and expect as a target. This word bank is then used in a few different ways. First off, it is used to build the Order Frequency table and the Letter Frequency table. The Letter Frequency table tells us how often each letter appears in 5-letter words, and follows what we would expect. S and E are the most common letters, followed by A and O. The Order Frequency table then shows given that a certain letter is in the word, what proportion of the time is that letter in each position (e.g. given A is in a word, it is the 4th letter 24% of the time).

<!-- b000111 | prose | pages [4] -->
As will be detailed later on, we also use this table in numerous word specific calculations, namely computing for a given word t the average number of green, yellow and colored tiles that are returned on any guess chosen uniformly at random from the SGB wordbank when t is the actual target word. Additionally, for any word g we compute the average number of colors returned when a target word t is chosen uniformly at random from the SGB wordbank and g is guessed, which gives a somewhat naive but reasonable metric to evaluate guess words players would use. Using this guess word metric, we compile a list of the 30 words with the highest corresponding average, which we take to be a set of common guess words (see Figure 1). This list will be used in the calculation of Subset Entropy later on.

<!-- b000112 | heading | pages [4] -->
3 Word & Difficulty Representation

<!-- b000113 | prose | pages [4] -->
Many factors contribute towards the difficulty associated with a given word. For example, ‘‘zingy’’ intuitively seems to be difficult for a variety of reasons - it has uncommon letters (“z” and “y”), only one “canonical” vowel, and is a generally infrequently used word in English. A word like ‘‘onion’’ on the other hand would also seem to be difficult, despite all of its letters being fairly common and its usage in every day spoken language being much higher. The reason it is perceived as difficult is due to a repetition of the letter “o” and “n”, which people may be less likely to guess again once they have already discovered one position of. Thus, given a word, our first task was to list and quantify such characteristics, so that when evaluating word difficulty later on we could instead simply consider the vector of values corresponding to these relevant characteristics.

<!-- b000114 | furniture | pages [5] -->
Team # 2322645

<!-- b000115 | furniture | pages [5] -->
Page 5 of 22

<!-- b000116 | caption | pages [5] -->
Figure 1: Left: 30 Most common words based on overlap. Right: Frequency of Letters in the SGB wordbank

<!-- b000117 | heading | pages [5] -->
3.1 Vowels

<!-- b000118 | prose | pages [5] -->
In all letter-guessing based games (beyond Wordle think hangman), a typical strategy is to exploit the higher frequency of letters which are vowels in words. In Wordle, the presence of particular vowel should tend to be discovered faster than those of non-vowels, leading to a reasonable assumption that words with more vowels will on average be easier to guess. Thus, one characteristic computed and considered for each word was the number of vowels it contained (excluding “y”, as this is a traditionally uncommon letter and hence does not align with the reasoning given above for why we consider vowels in the first place).

<!-- b000119 | heading | pages [5] -->
3.2 Usage

<!-- b000120 | prose | pages [5] -->
It makes sense that words which are used more commonly will be more familiar to people, and hence easier to guess from given clues. Using the wordfreq library [5] in python, this value was easily returned for each word under consideration.

<!-- b000121 | heading | pages [5] -->
3.3 Green & Yellow Tiles

<!-- b000122 | prose | pages [5] -->
Another desirable feature of a target word is that there is a high likelihood that after any given guess Wordle will return a large number of green and yellow squares. Once this occurs, players get very direct hints that they can immediately put into action. Thus, for any given word, we computed the the average number of green, yellow, and colored (i.e. non-gray) tiles returned considering the given word as the target and assuming guesses were drawn uniformly at random from the SGB wordbank.

<!-- b000123 | furniture | pages [6] -->
Team # 2322645

<!-- b000124 | furniture | pages [6] -->
Page 6 of 22

<!-- b000125 | heading | pages [6] -->
3.4 Unique Letters

<!-- b000126 | prose | pages [6] -->
When Wordle returns a color for a letter, it does not tell the player how many times that certain letter appears. Thus, while it may be easier to initially obtain green tiles for words with repeated letters, players may also be less likely to guess those same letters again in different positions. As a result, it seems justified to consider the number of unique letters in a word as playing a part in the difficulty of guessing it, and hence this value was computed for each considered word.

<!-- b000127 | caption | pages [6] -->
Figure 2: The repeated letter does not show up if the first guess is correct, it gives no indication that there is a

<!-- b000128 | prose | pages [6] -->
second k.

<!-- b000129 | heading | pages [6] -->
3.5 Entropies

<!-- b000130 | prose | pages [6] -->
One of the core ideas in information theory is that of entropy, which is a measure that quantifies the amount of information conveyed by a given event. In the context of a Wordle game, we can consider an event to be a particular choice of a player’s move, i.e. a guess word along with the corresponding positional colors Wordle returns as a result. Clearly this event gives us some information about the target word, and a reasonable question to ask is how much information? Once such a value is quantified formally, one can consider the “best” guess words to be those which result in a higher amount of information on average (over a uniform distribution of all possible 5-letter target words). Conversely, target words are more difficult to guess which, by some efficient text encoding, contain more information, or which result in lower amount of information being obtained on average (over some distribution of possible guessed words). These two ideas idea are formalized via two entropy formulations we give below, the first being a more typical application of the standard Shannon Entropy function, and the second being a more novel notion of entropy we developed specific to Wordle itself.

<!-- b000131 | heading | pages [6] -->
3.5.1 Positional Entropy

<!-- b000132 | prose | pages [6] -->
The original use case of entropy came from encoding, with more frequent symbols and common arrangements taking less bits to transmit. Our Positional Entropy takes this approach by considering a word to contain more information if its letters and letter arrangements are less common/more unusual. Using the Letter Frequency table and Order frequency table from the SGB word bank, for a given letter ϕ we calculate Pi(ϕ) as the probability a word has the letter ϕ in its ith location. These probabilities can then be plugged into the standard Shannon Entropy function H [4], where X denotes a 5-letter word and Xi corresponds to its ith letter, as follows:

<!-- b000133 | prose | pages [6] -->
5 X −Pi(Xi) log2(Pi(Xi)) H(X) := i=1 Note that under this metric, words which have more unusual letter placements, and hence can reasonably be assumed to be more difficult, will have a higher value.

<!-- b000134 | furniture | pages [7] -->
Team # 2322645

<!-- b000135 | furniture | pages [7] -->
Page 7 of 22

<!-- b000136 | heading | pages [7] -->
3.5.2 Subset Entropy

<!-- b000137 | prose | pages [7] -->
Our second entropy formulation is that of Subset Entropy, which is a novel Wordle-inspired metric we developed that, on a given word, quantifies the average amount of information which is revealed about it following one Wordle guess chosen from some distribution. This metric is motivated by the idea that on a given target word t with a chosen guess word of g, information is obtained via the output colors and their corresponding positions which allows one to disqualify other candidate target words t′. For example, if the target word under consideration is bread and the word crumb is guessed, then the corresponding output from Wordle would allow us to eliminate words such as toast and crabs as possible target words, but not allow us to eliminate arbor. An example illustrating this idea and our notation is given in figure 3.

<!-- b000138 | prose | pages [7] -->
Before we detail Subset Entropy, first we define ft(g) as the factor by which the candidate answer pool shrinks after word g is guessed and t is the target word. More formally, considering the notation in figure 3 we have:

<!-- b000139 | prose | pages [7] -->
ft(g) = n n1 where n is the size of the original candidate answer pool and n1 is the size of the resulting candidate answer pool. As an example, a guess g when the given target word is t which results in the possible answer pool shrinking from 4, 000 to 1, 000 words would have ft(g) = 4. Note that if g1 is a better guess than g2 given the target word is t, we have that ft(g1) > ft(g2), while if a target word t1 is easier to guess than t2 using a guess g then ft1(g) > ft2(g).

<!-- b000140 | prose | pages [7] -->
In typical entropy style, we take the base 2 logarithm of this factor which is computed, and define:

<!-- b000141 | prose | pages [7] -->
It(g) = log2(ft(g))

<!-- b000142 | prose | pages [7] -->
We use this value to correspond to our notion of the information conveyed by the event of guessing g on target t. The motivation for choosing this value as opposed to ft(g) directly is that Subset Entropy will aim to quantify the average information following the first guess when word t is the target, and hence will need to take an average over some quantification of information. As ft effectively measures a multiplicative factor of information (rather than additive), taking a geometric rather than arithmetic mean would be more appropriate. However, as the average of the log value of some terms exactly corresponds to the log of the geometric mean of these terms, we can effectively instead consider the expectation of It(g) over some distribution of guesses D as a measure of the geometric mean of the factors. With this justification in hand, we have the following formulation of Subset Entropy:

<!-- b000143 | prose | pages [7] -->
e(t) = Eg∼D[It(g)]

<!-- b000144 | prose | pages [7] -->
where D is some distribution over the possible guess words.

<!-- b000145 | prose | pages [7] -->
In the actual implementation of our model, we considered D to be a uniform distribution over the 30 most common guess words list (see figure 1). In particular, this model assumes that players guess one of the 30 best words to guess according to the average color metric. We decided this was reasonable, as many common words guessed or words similar to them, such as “slate”, appeared to be on the list.

<!-- b000146 | furniture | pages [8] -->
Team # 2322645

<!-- b000147 | furniture | pages [8] -->
Page 8 of 22

<!-- b000148 | prose | pages [8] -->
n n1 n2 bread target word:

<!-- b000149 | prose | pages [8] -->
toast crumb guess: bread wheat arbor bagel brans crabs C R U M B : :

<!-- b000150 | caption | pages [8] -->
Figure 3: Diagram representing the Subset Entropy method. For a target word bread, a guess crumb is made

<!-- b000151 | prose | pages [8] -->
and Wordle tells the player that R must be in the second position and B is somewhere in the word, but not in the last position. Furthermore, Wordle tells the player that C, U and M are not in the target word. This information defines a subset of n1 words that are compatible with it.

<!-- b000152 | heading | pages [8] -->
3.6 Representation of word difficulty

<!-- b000153 | prose | pages [8] -->
To aid in modeling and interpretation, ideally the 7-vector data (of players who got the word in 1 try, 2 tries, . . . , failed) which effectively represents the observed difficulty of a word, should be encapsulated with fewer numbers. We can view these seven categories as a discrete space and the observed proportion as a discrete probability mass function over them. By assuming an ordering of 1 < 2 < . . . < X, we then take the cumulative mass function that corresponds to the probability mass function. After embedding the domain into the interval [0, 1] by the map (i tries)7→i/7 and X 7→1, it turns out that the Beta distribution, a two-parameter continuous distribution over [0, 1], has a cumulative distribution function that can fit the embedded cumu- lative mass function closely (see figure 4). We then model reader attempts with the cumulative distribution of the Beta distribution, whose probability density function is:

<!-- b000154 | prose | pages [8] -->
1 B(α, β)xα−1(1 −x)β−1, f(x; α, β) =

<!-- b000155 | prose | pages [8] -->
where B(α, β) is the Beta function. To figure out the exact values of α, β that best fit the embedded cumulative mass function, we use non-linear least-squares as implemented in scipy[7]. By observing the figures above and from the properties of the Beta distribution, we can conclude a few properties of α and β:

<!-- b000156 | prose | pages [8] -->
• As α ↑while all else is held equal, the word is considered more difficult

<!-- b000157 | prose | pages [8] -->
• As β ↑while all else is held equal, the word is considered easier

<!-- b000158 | prose | pages [8] -->
• α+β will give how concentrated the distribution is around the expected value, with higher values being more concentrated.

<!-- b000159 | prose | pages [8] -->
α

<!-- b000160 | prose | pages [8] -->
• The ratio α+β gives the expected value of the Beta distribution, which is a representation of the difficulty of a word, with higher values corresponding to a higher difficulty.

<!-- b000161 | prose | pages [8] -->
Because of these properties, particularly the final one, α and β together are an effective and simple representation of the difficulty of a word. Figure 5 shows α/(α + β) computed from the observed reported distributions for all previous words.

<!-- b000162 | furniture | pages [9] -->
Team # 2322645

<!-- b000163 | furniture | pages [9] -->
Page 9 of 22

<!-- b000164 | prose | pages [9] -->
Cumulative Beta Distribution for Wordle 'Brave' Cumulative Beta Distribution for Wordle 'Cheek' 1.0 1.0 Observed Observed Beta(3.8, 2.9) fit Beta(7.0, 6.2) fit 0.8 0.8 Proportion of reports Proportion of reports 0.6 0.6

<!-- b000165 | prose | pages [9] -->
0.4 0.4

<!-- b000166 | prose | pages [9] -->
0.2 0.2

<!-- b000167 | prose | pages [9] -->
0.0 0.0 ct1 ct2 ct3 ct4 ct5 ct6 ct1 ct2 ct3 ct4 ct5 ct6 Cumulative number of guesses Cumulative number of guesses Cumulative Beta Distribution for Wordle 'Saint' Cumulative Beta Distribution for Wordle 'Swill' 1.0 Observed Observed Beta(4.2, 5.4) fit Beta(5.0, 2.6) fit 0.8 0.8 Proportion of reports Proportion of reports 0.6 0.6 0.4 0.4

<!-- b000168 | prose | pages [9] -->
0.2 0.2

<!-- b000169 | prose | pages [9] -->
0.0 0.0 ct1 ct2 ct3 ct4 ct5 ct6 ct1 ct2 ct3 ct4 ct5 ct6 Cumulative number of guesses Cumulative number of guesses

<!-- b000170 | caption | pages [9] -->
Figure 4: Beta Distribution fit to the cumulative proportion of guesses for Wordle words of various difficulty.

<!-- b000171 | heading | pages [9] -->
4 Modeling Methodology

<!-- b000172 | heading | pages [9] -->
4.1 Lasso regression

<!-- b000173 | prose | pages [9] -->
Once we have all the variables that can be extracted from the word itself, we must use select a subset of them to include in the Bayesian model, as the time taken by MCMC increases signif- icantly with the number of variables in the model and we must keep the run-time reasonable. To select more important predictors, we use Lasso regression. Lasso regression penalizes large coefficients, which in turn forces less important variables to have coefficients of zero. Lasso Regression has the following cost function:

<!-- b000174 | prose | pages [9] -->
!2 n P P X X X yi − |βj|, min xijβj + λ β i=1 j=1 j=1

<!-- b000175 | prose | pages [9] -->
where xij is the value of the jth predictor for the ith data point, and βj is the jth coefficient. λ is a tuning parameter which after experimentation we set to 0.1 to obtain the desired number of parameters (four). As seen in the cost function, Lasso regression seeks to minimize the error between true and predicted, while also having the sum of all coefficients be small.

<!-- b000176 | prose | pages [9, 10] -->
With our parameters, there are seven separate Lasso Regression models being run simulta- neously, one on the proportion of people who succeeded in one try, one on those who succeeded in two tries, and so on until the final one for those who failed. Four parameters appeared re- Distribution of α/(α + β)

<!-- b000177 | furniture | pages [10] -->
Team # 2322645

<!-- b000178 | furniture | pages [10] -->
Page 10 of 22

<!-- b000180 | prose | pages [10] -->
8

<!-- b000181 | prose | pages [10] -->
6 Density 4

<!-- b000182 | prose | pages [10] -->
2

<!-- b000183 | prose | pages [10] -->
0 0.4 0.5 0.6 0.7 0.8 α/(α + β)

<!-- b000184 | caption | pages [10] -->
Figure 5: Observed distribution of α/(α + β), a measure of word difficulty.

<!-- b000185 | caption | pages [10] -->
Figure 6: Inputs into the Lasso Regression

<!-- b000186 | prose | pages [10] -->
peatedly with nonzero coefficients in these regressions: the number of unique letters, the word’s usage frequency, the average number of yellow squares revealed, and the Subset Entropy.

<!-- b000187 | heading | pages [10] -->
4.2 Bayesian models for prediction

<!-- b000188 | prose | pages [10, 11] -->
We use a Bayesian model comprising three conditionally independent submodels to model the distribution of tries (the Try model), the number of reports (the Reports model), and the number of hard-mode players (or “hardmoders,” in the Hardmoders model). This model is displayed in word

<!-- b000189 | caption | pages [10] -->
Figure 7.

<!-- b000190 | furniture | pages [11] -->
Team # 2322645

<!-- b000191 | furniture | pages [11] -->
Page 11 of 22

<!-- b000193 | prose | pages [11] -->
# unique letters word usage avgYellow S-entropy

<!-- b000194 | prose | pages [11] -->
a0 a1 b1 c1 a2 b2 c2 a3 b3 c3 a4 b4 c4 × × × × × × × × × × × × 7 7 7 7 7 + + + + + difficulty 7 + + + + difficulty + + + + difficulty σ Normal date day of week A γ θ ω λ 7 5 7 7 4 Dirichlet × × long-term periodic periodic long-term p 7 + + Mean number of reports B k Mean proportion of hardmoders β α Beta p Negative Binomial Multinomial Binomial Number of reports Number of hardmoders Try Distribution 7

<!-- b000195 | caption | pages [11] -->
Figure 7: Combined diagram of the three Bayesian models. Shapes with rounded corners are variables, and

<!-- b000196 | prose | pages [11] -->
rectangles are observed data. Numbers indicate the dimension of vectors (all other variables and data are scalars). In yellow is the model for predicting the proportion of hardmoders, in red is the model for predicting the number of reports, and in blue is the model for predicting the distribution of the number of tries. Numbers outside the shapes indicate the dimensions of data and variables when they are not scalars. Conditioned on the observed data, the random variables of all three models are independent, which allows their posteriors to be inferred in three separate runs of MCMC. Note that the number of reports from the Reports model is fed into the Try model and the Hardmoders model. In green are the α and β values, which are the parameters of the Beta distribution corresponding to a word’s difficulty distribution p.

<!-- b000197 | furniture | pages [12] -->
Team # 2322645

<!-- b000198 | furniture | pages [12] -->
Page 12 of 22

<!-- b000199 | heading | pages [12] -->
4.2.1 Common components

<!-- b000200 | prose | pages [12] -->
Word difficulty Each of the three Bayesian models takes in four predictors that somehow correspond with difficulty. Since the effect of difficulty on the try distribution, the number of reports and the number of hardmoders is not necessarily the same, we do a separate regression within each of these models:

<!-- b000201 | prose | pages [12] -->
dtry = a0 + a1x1 + a2x2 + a3x3 + a4x4 (1) dreports = b1x1 + b2x2 + b3x3 + b4x4 (2) dhardmoders = c1x1 + c2x2 + c3x3 + c4x4 (3)

<!-- b000202 | prose | pages [12] -->
, where a’s b’s, and c’s are coefficients to be estimated, and xi’s are predictors. Note that the Try model has both dtry and the ai coefficients as 7-vectors. Note also that the Try model is the only one with an intercept in this component, as in the others the intercept is captured by other terms. Each of the coefficients has a prior of Normal(0, 20), which is wide enough to be uninformative.

<!-- b000203 | prose | pages [12] -->
Day-of-week effects In both the number of reports and the proportion of hardmoders, there are periodic day-of-week effects. In the Reports and Hardmoders models, these are modeled similarly:

<!-- b000204 | prose | pages [12] -->
7 X θi · 1(ith day of week) Preports = (4) i=1 7 X ωi · 1(ith day of week) Phardmoders = (5) i=1

<!-- b000205 | prose | pages [12] -->
The θ and ω coefficients are modeled as having Normal(0, 1) prior distributions.

<!-- b000206 | heading | pages [12] -->
4.2.2 Try model

<!-- b000207 | prose | pages [12] -->
The model for the distribution of tries (the Try model) is fundamentally a Dirichlet-Multinomial model. For a given word on a given day, we model the vector (t1, t2, . . . , t7), where ti, i < 7 is the number of reports who got the word on the ith try, and t7 is the number of reported failures, as coming from the Multinomial distribution:

<!-- b000208 | prose | pages [12] -->
(t1, t2, t3, t4, t5, t6, t7) ∼Multinomial (n, 7, (p1, p2, p3, p4, p5, p7)) ,

<!-- b000209 | prose | pages [12] -->
where n is the number of reports on that day, and p = (p1, p2, p3, p4, p5, p7) is a probability 7-vector (P7 i=1 pi = 1) of the probabilities that a report reports success on the first try, second try, and so on. This vector itself is modeled as coming from the Dirichlet distribution, which is a distribution over discrete probability distributions:

<!-- b000210 | prose | pages [12] -->
(p1, p2, p3, p4, p5, p7) ∼Dirichlet(7, (A1, A2, A3, A4, A5, A6, A7)),

<!-- b000211 | prose | pages [12] -->
where A = (A1, A2, A3, A4, A5, A6, A7) is the vector of concentration parameters for the Dirichlet distribution, Ai > 0. The logarithm of these concentration parameters is itself drawn from a Normal distribution:

<!-- b000212 | prose | pages [12, 13] -->
ln(Ai) ∼Normal(dtry,i, σ), where dtry,i is as defined by Equation 1. σ is a variance parameter which has a prior of Exponential(1).

<!-- b000213 | furniture | pages [13] -->
Team # 2322645

<!-- b000214 | furniture | pages [13] -->
Page 13 of 22

<!-- b000216 | heading | pages [13] -->
4.2.3 Reports model

<!-- b000217 | prose | pages [13] -->
The model for the number of reports (the Reports model) is fundamentally an overdispersed Poisson regression. The number of reports on a given day can clearly be modeled as a Poisson distribution with a certain rate. However, since there is additional variation in the observed number of reports beyond just Poisson error that is not accounted for by the predictors, we must use an overdispersed version of the Poisson distribution (i.e. a distribution that behaves like the Poisson, but with additional errors). The Negative Binomial distribution, when parameterized correctly, has this property. Hence we model the number of reports for a given word on a given day as:

<!-- b000218 | prose | pages [13] -->
n ∼NegativeBinomial (exp(Lreports + Preports + dreports), B) . Lreports, Preports, and dreports correspond to the long-term trend in the number of reports, the periodic trend, and the effect of difficulty, respectively. The periodic trend is defined in Equation 4. The effect of difficulty is defined in Equation 2. B is a parameter describing the overdispersion, and is modeled as having an Exponential(0.01) prior distribution so as to allow it to be large.

<!-- b000219 | prose | pages [13] -->
Because of the correspondence of the long-term trend with the shape of a Gamma distribu- tion, we parameterize Lreports as a function that recalls the probability density function of the Gamma distribution:

<!-- b000220 | prose | pages [13] -->
Lreports = γ1((T −γ5)γ2) exp(−(T −γ5)/γ3) + γ4,

<!-- b000221 | prose | pages [13] -->
where T is a time value for the word. T is scaled such that the first word in the data has T = 0 and the last word has T = 1. The γi coefficients have, according to their role in the equation, different prior distributions. γ1, γ2, and γ3 all have an Exponential(1) prior distribution, γ4 has an Exponential(0.01) prior distribution, and γ5 has a Normal(0, 1) prior distribution. These choices of priors are uninformative when considering the scale of T.

<!-- b000222 | heading | pages [13] -->
4.2.4 Hardmoders model

<!-- b000223 | prose | pages [13] -->
The model for the number of people who reported playing in hard-mode (the Hardmoders model) is fundamentally a Beta-Binomial regression. Given the number of reports on a given day, the number of hardmoders is described by a Binomial distribution with a certain probability. However, since there is additional variation in the observed number of hardmoders beyond just the error of the Binomial which is not accounted for by the predictors, the probability itself is modeled as coming from a Beta distribution.

<!-- b000224 | prose | pages [13] -->
Hence we model the number of hardmoders nh for a given word on a given day as:

<!-- b000225 | prose | pages [13] -->
nh ∼Binomial (n, p)

<!-- b000226 | prose | pages [13] -->
where n is the number of reports on that day and p is the probability that someone reports playing in hardmode. p itself is modeled as:

<!-- b000227 | prose | pages [13, 14] -->
p ∼Beta (ηκ, (1 −η)κ) , where:

<!-- b000228 | furniture | pages [14] -->
Team # 2322645

<!-- b000229 | furniture | pages [14] -->
Page 14 of 22

<!-- b000231 | prose | pages [14] -->
η = logit−1(Lhardmoders + Phardmoders + dhardmoders) Note that η is the mean of this Beta distribution, as E[p] = ηκ/(ηκ + (1 −η)κ) = η. Cor- respondingly, κ controls the spread of the distribution. Lhardmoders, Phardmoders, and dhardmoders correspond to the long-term trend in the number of hardmoders, the periodic trend, and the effect of difficulty, respectively. The periodic trend is defined in Equation 5. The effect of dif- ficulty is defined in Equation 3. κ effectively controls the overdispersion of the Beta-Binomial model, and is modeled as having an HalfCauchy(0.5) prior distribution, which is has a long tail and acts as an uninformative prior.

<!-- b000232 | prose | pages [14] -->
We then parameterize Lhardmoders as a function that can follow the observed shape:

<!-- b000233 | prose | pages [14] -->
Lhardmoders = λ1((T −λ4)λ2) + λ3,

<!-- b000234 | prose | pages [14] -->
where T is a time value for the word. T is scaled such that the first word in the data has T = 0 and the last word has T = 1. The λi coefficients have, according to their role in the equation, different prior distributions. λ1, λ2, and λ3 all have an Exponential(1) prior distribution, λ4 has a Normal(0, 1) prior distribution. These choices of priors are uninformative when considering the scale of T.

<!-- b000235 | heading | pages [14] -->
4.2.5 Obtaining the posteriors

<!-- b000236 | prose | pages [14] -->
Rather than computing simple point estimates for the parameters, we obtain full posterior distributions given the data. These are obtained by using Markov Chain Monte-Carlo (MCMC) to iteratively sample from the joint posterior distribution of the variables. Because the three submodels are conditionally independent given the data, we run MCMC on the three submodels separately. In particular, we use the No U-Turn Sampler [1] as it is implemented in PyMC [3].

<!-- b000237 | heading | pages [14] -->
5 Model Results

<!-- b000238 | prose | pages [14] -->
Once the posterior distributions of the parameters of three submodels are obtained, we can glean information from the distributions, and both predict and retrodict by feeding words and dates through the model to obtain posterior predictions.

<!-- b000239 | heading | pages [14] -->
5.1 Interpretation of parameter posteriors

<!-- b000240 | prose | pages [14, 15] -->
The posteriors of the model parameters can tell us something about what attributes of a word affect a word’s difficulty, the number of scores reported, or the percentage of hardmoders. The posteriors on the ai coefficients obtained in the Try model all indicate an effect on the distribution of results in the seven different categories. A higher number of unique letters, frequency of word usage, average number of yellow squares revealed, or Subset Entropy all cause the word to be easier to guess, which is reflected in positive ai coefficients for the number of people guessing the word on the second try, and negative ai coefficients for the number of people guessing the word on the sixth try. The word cause is used intentionally here. The correlations that the coefficients indicate can be interpreted as causal with the simple assumption that Wordle words are chosen completely at random. This is because, if words are chosen randomly, any correlation Retrodictions for the numbers of reports and hardmoders for past words and dates.

<!-- b000241 | furniture | pages [15] -->
Team # 2322645

<!-- b000242 | furniture | pages [15] -->
Page 15 of 22

<!-- b000244 | prose | pages [15] -->
Proportion of hardmoders Number of hardmoders 95% posterior 95% posterior 15000 Number of reports 0.10 300000 prediction interval prediction interval Observed value Observed value 10000 200000 0.05 95% posterior 5000 100000 prediction interval Observed value 0 0.00 0 0 100 200 300 0 100 200 300 0 100 200 300 Contest number Contest number Contest number

<!-- b000245 | caption | pages [15] -->
Figure 8: Posterior-predicted distributions for the number of reports, the number of hardmoders, and the

<!-- b000246 | prose | pages [15] -->
proportion of hardmoders over all past words and dates. The models seem to capture the long-term trend and variation in the data well.

<!-- b000247 | prose | pages [15] -->
between a word’s properties and the Try distribution must be due to an effect of the word’s properties on the Try distribution, and not due to a reverse effect or a confounding variable.

<!-- b000248 | prose | pages [15] -->
Likewise, the posterior distributions of the bi’s are largely positive. This indicates that, for easier words, more people report their results. The posterior distributions of almost all of the ci coefficients include zero, suggesting that, beyond the effect of the total number of reports decreasing, there is no additional effect on the number of hardmoders. On the contrary, the posterior for c1 is largely negative, which counteracts the effect of a decreased total number of reports on the number of hardmoder reports. Again, it is possible to read causation from correlation in these results as that is the only possible way to explain the variation under the assumption that a day’s Wordle word is chosen randomly. One possible causal interpretation is that the set of players who play on hard mode is more consistent with reporting their results.

<!-- b000249 | prose | pages [15] -->
Surprisingly, the θi and ωi coefficients are centered around zero, indicating no evidence for a periodic effect. This suggests that there are insufficient data to, in combination with the effects of word difficulty and long-term effects, reliably estimate a periodic effect.

<!-- b000250 | heading | pages [15] -->
5.2 Retrodiction

<!-- b000251 | prose | pages [15] -->
The model can be used to make predictions for past data. Figure 8 shows the posterior predic- tions for the number of reports, the number of hardmoders, and the proportion of hardmoders for the dates and words given, as well as the observed values. The model seems to capture the variation in the data as well as the long-term trend. Figure 9 shows the posterior predictions for the try distribution of fungi, a past Wordle word, and shows good agreement with the truth.

<!-- b000252 | heading | pages [15] -->
5.3 Prediction

<!-- b000253 | prose | pages [15] -->
The model can also be used to make predictions for future, unseen data. This can be done either for a future date and word, like eerie on March 1, 2023, or for a date alone (by the posterior predictions for that date averaged over all observed Wordle words). Figure 10 shows predictions for the difficulty of eerie. Figure 11 shows, in general and for eerie in particular, predictions for the number of reported scores on March 1, the number of hardmoders, and the proportion of hardmoders. Table 1 gives prediction intervals for several different quantities of interest if eerie is the word on March 1.

<!-- b000254 | furniture | pages [16] -->
Team # 2322645

<!-- b000255 | furniture | pages [16] -->
Page 16 of 22

<!-- b000256 | prose | pages [16] -->
Posterior-predicted diﬃculty of “fungi”

<!-- b000257 | prose | pages [16] -->
0.6 Proportion of reports 0.4

<!-- b000258 | prose | pages [16] -->
0.2

<!-- b000259 | prose | pages [16] -->
0.0 1 try 2 tries 3 tries 4 tries 5 tries 6 tries Fail

<!-- b000260 | caption | pages [16] -->
Figure 9: Posterior predictions for the try distribution of fungi as reported by Wordle players. The black points

<!-- b000261 | prose | pages [16] -->
and black lines indicating the median and 50% interval, and the red crosses indicate the true values.

<!-- b000262 | caption | pages [16] -->
Table 1: Prediction intervals of several quantities of interest for eerie appearing on March 1, 2023.

<!-- b000263 | prose | pages [16] -->
Variable 95% 80% 50% Median Number of reports [20238, 27876] [21479, 26365] [22622, 25169] 23884 Number of hardmoders [2194, 3239] [2355, 3048] [2509, 2870] 2683 Percentage of hardmoders [9.97, 12.62] [10.41, 12.15] [10.79, 11.72] 11.25 Percentage in 1 guess [0, 2.4] [0, 0.82] [0, 0.15] 0 Percentage in 2 guess [1.09, 14.01] [2.08, 10.45] [3.39, 7.70] 5.23 Percentage in 3 guess [12.16, 35,85] [15.34, 31.03] [18.49, 26.82] 22.46 Percentage in 4 guess [21.29, 48.16] [25.19, 43.2] [29.2, 38.51] 33.79 Percentage in 5 guess [12.48, 37.09] [16.16, 32.19] [19.4, 27.96] 23.54 Percentage in 6 guess [ 3.73, 21.33] [5.6, 16.99] [7.6, 13.53] 10.37 Percentage failed [0.06, 7.77] [0.24, 4.91] [0.66 3.09] 1.6

<!-- b000264 | heading | pages [16] -->
5.4 Difficulty representation

<!-- b000265 | prose | pages [16] -->
Given samples from the posterior distribution of a word’s p = (p1, . . . , p7) 7-vector representing difficulty, we can use the embedding and optimization method described above to compute posterior samples of the α and β values for a word. This is done for eerie in Figure 10. Notably, for eerie, the posterior samples for α and β lie along the α = β line, indicating a fairly stable difficulty estimate of α/(α + β) ≈0.52 but less certainity about the exact shape of the distribution (i.e. whether most people will get the word in three or four tries, or whether it will be more even between, say, two, three, four, and five tries). This places eerie in roughly the 50th percentile of words when compared to previous Wordle words according to this measure of difficulty.

<!-- b000266 | furniture | pages [17] -->
Team # 2322645

<!-- b000267 | furniture | pages [17] -->
Page 17 of 22

<!-- b000268 | prose | pages [17] -->
Posterior-predicted diﬃculty of “eerie”

<!-- b000269 | prose | pages [17] -->
0.6 Proportion of reports 0.4

<!-- b000270 | prose | pages [17] -->
0.2

<!-- b000271 | prose | pages [17] -->
0.0 1 try 2 tries 3 tries 4 tries 5 tries 6 tries Fail

<!-- b000272 | prose | pages [17] -->
0.00200 50 1 try 1 try 0.00175 2 tries 2 tries 40 3 tries 3 tries 0.00150 4 tries 4 tries 0.00125 30 5 tries 5 tries Density Density 6 tries 6 tries 0.00100 Fail Fail 20 0.00075

<!-- b000273 | prose | pages [17] -->
0.00050 10 0.00025

<!-- b000274 | prose | pages [17] -->
0.00000 0 0 5000 10000 0.0 0.2 0.4 Number of reports Proportion of reports

<!-- b000275 | prose | pages [17] -->
Posterior distribution of α, β Posterior distribution of α/(α + β) 10 0.30

<!-- b000276 | prose | pages [17] -->
9 15.0 0.25 8 12.5 0.20 7 10.0 Density Density 6 β 0.15 7.5 5 0.10 5.0 4 0.05 2.5 3

<!-- b000277 | prose | pages [17] -->
0.0 2 0.00 0.45 0.50 0.55 0.60 2 4 6 8 10 α/(α + β) α

<!-- b000278 | caption | pages [17] -->
Figure 10: Posterior predictions for several representations of the difficulty of eerie as reported by Wordle

<!-- b000279 | prose | pages [17] -->
players. Top: violin plot of the posteriors on the proportion of reports in each of the seven categories, with the point and black lines indicating the median and 50% interval. Middle: histograms of the number of proportion of reports in each of the seven categories. Bottom: Posterior distributions of the fitted α, β and the expected value of the corresponding Beta distribution, with a dashed line indicating the median. Our model predicts that eerie is a word of middling difficulty, with most players having guessed it on the fourth try or before.

<!-- b000280 | furniture | pages [18] -->
Team # 2322645

<!-- b000281 | furniture | pages [18] -->
Page 18 of 22

<!-- b000282 | prose | pages [18] -->
Posterior distributions for the numbers of reports and hardmoders for eerie.

<!-- b000283 | prose | pages [18] -->
30 0.00020 0.0015

<!-- b000284 | prose | pages [18] -->
0.00015 20 density density 0.0010 density 0.00010 10 0.0005 0.00005

<!-- b000285 | prose | pages [18] -->
0.00000 0.0000 0 20000 30000 2000 3000 4000 0.10 0.15 Number of reports Number of hardmoders Proportion of hardmoders

<!-- b000286 | caption | pages [18] -->
Figure 11: Posterior-predicted distributions for the number of reports, the number of hardmoders, and the

<!-- b000287 | prose | pages [18] -->
proportion of hardmoders for March 1, 2023 (black) and if eerie is the Wordle word on March 1, 2023 (red). For each of the three variables, there is little if any difference between the distributions when averaged over all previous words, and when for eerie specifically.

<!-- b000288 | heading | pages [18] -->
6 Model Evaluation

<!-- b000289 | heading | pages [18] -->
6.1 Limitations

<!-- b000290 | prose | pages [18] -->
• The Subset Entropy predictor does not capture how difficult a word is to guess after the first guess. For instance, if a player, after the first guess, has revealed that a word ends in atch, the word could be watch, catch, latch, and so on. Subset Entropy does not reflect this source of difficulty.

<!-- b000291 | prose | pages [18] -->
• Subset Entropy requires us to make assumptions on the distribution of first guesses made by players.

<!-- b000292 | prose | pages [18] -->
• Compared to traditional statistical methods, Bayesian models sampled using MCMC are extremely slow. Using MCMC to sample from a posterior distribution is not nearly as efficient as using gradient-descent or an analytic solution to find optimal values for the parameters that minimize a cost function

<!-- b000293 | prose | pages [18] -->
• The model does not take into account changes in mean player skill across different days, though time was found to be less relevant than aspects of the word itself in a word’s difficulty distribution.

<!-- b000294 | prose | pages [18] -->
• The Reports and Hardmoders models do not take into account autocorrelation in the data and instead assume a stable long-term trend which may underestimate the uncertainty inherent in long-term predictions.

<!-- b000295 | heading | pages [18] -->
6.2 Strengths

<!-- b000296 | prose | pages [18, 19] -->
• Using a Bayesian framework allows full distributions to be obtained for any predictions, rather than a simple best-fit and prediction intervals that require approximations and strong distribution assumptions. For instance, other models may not capture the asym- metry in the posterior-predicted distributions for the number of people guessing eerie in 1 try and the number of people failing.

<!-- b000297 | furniture | pages [19] -->
Team # 2322645

<!-- b000298 | furniture | pages [19] -->
Page 19 of 22

<!-- b000300 | prose | pages [19] -->
• The uncertainty in the Bayesian predictions includes not only that from true noise in the data, but also uncertainty in the estimates of the coefficients and parameters of the model itself.

<!-- b000301 | prose | pages [19] -->
• Our model allows for the parameters of a word to have diverse effects on the Try distri- bution, the number of reports, and the number of hardmoders, which is appropriate as different aspects of word difficulty may affect these outcomes.

<!-- b000302 | prose | pages [19] -->
• Our model represents the difficulty of a word in just two parameters (α and β), which can be predicted with uncertainty. The “difficulty” of a Wordle word when played by real people with different backgrounds, strategies, and levels of commitment cannot be exactly measured.

<!-- b000303 | heading | pages [19] -->
7 Conclusion

<!-- b000304 | prose | pages [19] -->
We model how difficult words are to guess in Wordle using several approaches. Rather than having a single, prescriptive metric, we come up with several which correspond to a word’s difficulty in different ways. We then select a subset of these predictors using a Lasso regression.

<!-- b000305 | prose | pages [19] -->
By using the Beta distribution as a representation of distributions of numbers of guesses, we are able to condense the information about the difficulty of a word into just two numbers, and from there into a single number which allows us to directly compare words against each other.

<!-- b000306 | prose | pages [19] -->
Using an innovative Bayesian model, we are able to predict how many guesses future players will report making on future words, how many players will report their results on Twitter, and how many players will report playing in hard-mode. The innovative aspect of the model is that it is made up of three submodels which, when conditioned upon the data, are independent. Hence the overall model can be quite large while still being efficient enough to perform Markov Chain Monte-Carlo on (as MCMC can be run separately on each submodel) and obtain samples from the posterior distribution. Given the Bayesian nature of the model, it is also able to provide uncertainties on any predictions and retrodictions made in the form of probability distributions instead of simple prediction intervals. We provide several predictions supposing that eerie is the Wordle word on March 1, 2023 and provide several retrodictions to confirm that our model aligns with past data.

<!-- b000307 | furniture | pages [20] -->
Team # 2322645

<!-- b000308 | furniture | pages [20] -->
Page 20 of 22

<!-- b000309 | heading | pages [20] -->
References

<!-- b000310 | references | pages [20] -->
[1]

<!-- b000311 | references | pages [20] -->
Matthew D Hoffman, Andrew Gelman, et al. “The No-U-Turn sampler: adaptively setting

<!-- b000312 | references | pages [20] -->
path lengths in Hamiltonian Monte Carlo.” In: J. Mach. Learn. Res. 15.1 (2014), pp. 1593–

<!-- b000313 | references | pages [20] -->
1623.

<!-- b000314 | references | pages [20] -->
Oxford University Press. Home : Oxford English Dictionary. url: https://www.oed.com/

<!-- b000315 | references | pages [20] -->
[2]

<!-- b000316 | references | pages [20] -->
browsedictionary.

<!-- b000317 | references | pages [20] -->
[3]

<!-- b000318 | references | pages [20] -->
John Salvatier, Thomas V. Wiecki, and Christopher Fonnesbeck. “Probabilistic program-

<!-- b000319 | references | pages [20] -->
ming in Python using PyMC3”. In: PeerJ Computer Science 2 (Apr. 2016), e55. doi:

<!-- b000320 | references | pages [20] -->
10.7717/peerj-cs.55. url: https://doi.org/10.7717/peerj-cs.55.

<!-- b000321 | references | pages [20] -->
Claude Shannon. “A Mathematical Theory of Communication”. In: Bell System Technical

<!-- b000322 | references | pages [20] -->
[4]

<!-- b000323 | references | pages [20] -->
Journal 27.4 (Oct. 1948), pp. 623–656. doi: https : / / doi . org / 10 . 1002 / j . 1538 -

<!-- b000324 | references | pages [20] -->
7305.1948.tb00917.x.

<!-- b000325 | references | pages [20] -->
Robyn Speer. rspeer/wordfreq: v3.0. Version v3.0.2. Sept. 2022. doi: 10.5281/zenodo.

<!-- b000326 | references | pages [20] -->
[5]

<!-- b000327 | references | pages [20] -->
7199437. url: https://doi.org/10.5281/zenodo.7199437.

<!-- b000328 | references | pages [20] -->
Stanford University. Knuth: The Stanford GraphBase. url: https://www-cs-faculty.

<!-- b000329 | references | pages [20] -->
[6]

<!-- b000330 | references | pages [20] -->
stanford.edu/~knuth/sgb.html.

<!-- b000331 | references | pages [20] -->
[7]

<!-- b000332 | references | pages [20] -->
Pauli Virtanen et al. “SciPy 1.0: Fundamental Algorithms for Scientific Computing in

<!-- b000333 | references | pages [20] -->
Python”. In: Nature Methods 17 (2020), pp. 261–272. doi: 10.1038/s41592-019-0686-2.

<!-- b000334 | furniture | pages [21] -->
Team # 2322645

<!-- b000335 | furniture | pages [21] -->
Page 21 of 22

<!-- b000336 | heading | pages [21] -->
Letter to New York Times Puzzle Editor

<!-- b000337 | prose | pages [21] -->
Dear Puzzle Editor of the New York Times,

<!-- b000338 | prose | pages [21] -->
Playing the daily Wordle has become a pastime for many people across the world. The New York Times has built up a dedicated fanbase, and the ease of the game also allows for anybody to occasionally pick up the daily challenge and post their results to social media. Part of what we aimed to do was discover what causes this variation in daily reports, and how the difficulty of words you choose as the Puzzle Editor can affect player results. The Bayesian model that we have developed can provide a distribution on future player count, as well as a distribution of results based on any chosen word.

<!-- b000339 | prose | pages [21] -->
We discovered that the greatest variation in player reporting was due to the difficulty of the word. When the word was easier, a higher number of people reported results. There was an overall decreasing trend in the number of players, likely due to Wordle aging as a game. On the other hand, there was also no real effect of word difficulty on the number of players reporting playing in hard mode. We also see the proportion of hard mode players increasing over time, this is indicative of more casual players leaving the game, with the more dedicated players, which are those more likely to play in hard mode, occupying a larger portion of the playerbase.

<!-- b000340 | prose | pages [21] -->
Retrodictions for the numbers of reports and hardmoders for past words and dates.

<!-- b000341 | prose | pages [21] -->
Proportion of hardmoders Number of hardmoders 95% posterior 95% posterior 15000 Number of reports 0.10 300000 prediction interval prediction interval Observed value Observed value 10000 200000 0.05 95% posterior 5000 100000 prediction interval Observed value 0 0.00 0 0 100 200 300 0 100 200 300 0 100 200 300 Contest number Contest number Contest number

<!-- b000342 | caption | pages [21] -->
Figure 12: Posterior-predicted distributions for the number of reports, the number of hardmoders, and the

<!-- b000343 | prose | pages [21] -->
proportion of hardmoders over all past words and dates.

<!-- b000344 | prose | pages [21] -->
As for predicting the difficulty of words, we found that we could accurately model the distribu- tion of player attempts with a Beta distribution. Such a distribution is parameterized by (α, β), and we discovered that a higher α relative to β signified that the word was harder to guess. These differences can be seen in the different α and β values seen for the word “Swill,” which we are sure you will agree is a harder word to guess than a word like “Saint”. We then use various metrics including the number of unique letters, word usage in the English language, and letter differences with common starting guesses to predict these parameters.

<!-- b000345 | prose | pages [21] -->
According to our method for scoring word difficulty, the difficulty of “Eerie” is 0.52, which would fall into around the 50th percentile of words, similar in difficulty to words like “Rhyme”, “Equal’, and “Quirk” used in the past. This makes intuitive sense, because although it has a lot of repeated letters and is a fringe word, the commonality of “e”,“r”, and “i” makes it so that many of the most common starting guesses will reveal information about the word.

<!-- b000346 | furniture | pages [22] -->
Team # 2322645

<!-- b000347 | furniture | pages [22] -->
Page 22 of 22

<!-- b000348 | prose | pages [22] -->
Cumulative Beta Distribution for Wordle 'Saint' Cumulative Beta Distribution for Wordle 'Swill' 1.0 Observed Observed Beta(4.2, 5.4) fit Beta(5.0, 2.6) fit 0.8 0.8 Proportion of reports Proportion of reports 0.6 0.6 0.4 0.4 0.2 0.2

<!-- b000349 | prose | pages [22] -->
0.0 0.0 ct1 ct2 ct3 ct4 ct5 ct6 ct1 ct2 ct3 ct4 ct5 ct6 Cumulative number of guesses Cumulative number of guesses

<!-- b000350 | caption | pages [22] -->
Figure 13: Beta distribution fit to the cumulative proportion of guesses for Wordle words of various difficulty.

<!-- b000351 | prose | pages [22] -->
If the Wordle of the day on March 1, 2023 happened to be “Eerie”, then we are 95% confident that the range of players reporting on Twitter will be between [20238, 27876], with approximately 11.25% of them being hard mode players. We predict roughly 34% of players will report getting it on their fourth attempt, and we expect around 1.6% of the players to fail in guessing the word. These exact results are also summarized in the table and graphs below. We hope this analysis can help better inform future Wordle choices, and we look forward to the upcoming puzzles.

<!-- b000352 | caption | pages [22] -->
Table 2: Prediction intervals of several quantities of interest for eerie appearing on March 1, 2023.

<!-- b000353 | prose | pages [22] -->
Variable 95% 80% Median Number of reports [20238, 27876] [21479, 26365] 23884 Number of hardmoders [2194, 3239] [2355, 3048] 2683 Percentage of hardmoders [9.97, 12.62] [10.41, 12.15] 11.25 Percentage in 1 guess [0, 2.4] [0, 0.82] 0 Percentage in 2 guess [1.09, 14.01] [2.08, 10.45] 5.23 Percentage in 3 guess [12.16, 35,85] [15.34, 31.03] 22.46 Percentage in 4 guess [21.29, 48.16] [25.19, 43.2] 33.79 Percentage in 5 guess [12.48, 37.09] [16.16, 32.19] 23.54 Percentage in 6 guess [ 3.73, 21.33] [5.6, 16.99] 10.37 Percentage failed [0.06, 7.77] [0.24, 4.91] 1.6

<!-- b000354 | prose | pages [22] -->
Posterior-predicted diﬃculty of “eerie”

<!-- b000355 | prose | pages [22] -->
0.6 Proportion of reports 0.4

<!-- b000356 | prose | pages [22] -->
0.2

<!-- b000357 | prose | pages [22] -->
0.0 1 try 2 tries 3 tries 4 tries 5 tries 6 tries Fail

<!-- b000358 | caption | pages [22] -->
Figure 14: Violin plot of the posteriors on the proportion of reports in each of the seven categories, with the

<!-- b000359 | prose | pages [22] -->
point and black lines indicating the median and 50% interval.

<!-- b000360 | prose | pages [22] -->
Happy Puzzling, The Markov Chain Monte Carlo Mathematical Contest in Modeling Competitors
