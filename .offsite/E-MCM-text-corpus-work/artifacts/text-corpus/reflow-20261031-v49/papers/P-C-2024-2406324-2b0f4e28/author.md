MCM/ICM

Summary Sheet

Summary

This study addresses the complex phenomenon of momentum in tennis by analyzing data from Wimbledon 2023 men’s matches. By using the Exponential Weighted Moving Average (EWMA), an evaluation model is constructed to quantitatively define momentum and swings during the matches. The combined result of the run test and context study proves momentum is not random. Based on the numerical curves of momentum, we build a prediction model that combines the low error rate of Long Short-Term Memory (LSTM) networks and factor contribution analysis of Extreme Gradient Boosting (XGBoost). Clustered transfer learning is introduced with K-means clustering to improve the prediction model in accuracy. SHapley Additive exPlanations (SHAP) is applied to find out which

factors are most related to the swings in tennis matches. In sensitive analysis, we verified our choice of step size and cluster number, pointing out possible directions for future work. We have also collected data from Women’s matches (2023 WTA US Open). The prediction error becomes significantly larger, for which we have explained generally. With all the conclusions drawn, we write a memo for tennis coaches at the end of this paper.

EWMA LSTM K-means SHAP

1 Introduction

In many sports competitions, it might often occur that the stronger player or team loses the game. At any given time in a match, the score does not always reflect the true strength of the players, or even 微信公众号：数学模型 the state of the game (Higham, 2000). We can sometimes feel a kind of hidden force that controls the flow of the match, which is defined as the momentum of the game (Higham, 2000). It affects the outcome of the contest and adds to the overall unpredictablity. If the players and their coach can understand and predict the momentum of the game, they can adjust their strategy to take advantage of it and increase their chance of winning the game.

The appearence of momentum is especially obvious in tennis matches, since the game is divided into many periods and the situation on the field is constantly changing. In previous studies, a great deal of data was counted to statistically prove the existence of momentum in tennis matches (Moss & Donoghue, 2017). Most researchers have reached an agreement that success does breed success, which means that a series of consecutive winning points is likely to set up a good starting position for the next ball (Meier, Flepp, Ruedisser, & Franck, 2020). However, there are also arguments that falling 微信号：MATHmodels behind temporarily will push the players’ nerves and help them try harder to catch up (Fu, Ke, & Tan, 2015). Despite different opinions, they all agree that the momentum does exist and is often affected by interruptions such as rest periods and important events such as break points converted (Meier, Flepp, Ruedisser, & Franck, 2020).

In this paper, we have learned and concluded from previous studies the basic properties of mo- mentum in tennis. We cleaned and processed the data from Wimbledon 2023 men’s matches after the first 2 rounds as the basis of our research (COMAP, 2024). A model is then proposed to quantify the momentum of a game and predict the final outcome (Albert & Koning, 2007). We will show that the swings in a game are not random, and that good indicators could be found for them. We will also extend our model to Women’s Tennis, and discuss how generalizable our model is. The flowchart shown below summarizes the main work and results of our paper.

2 Assumptions and Notations

2.1 Assumptions

微信公众号：数学模型

• Only regular breaks The match is assumed not to be suspended due to any sudden events like weather changes (rain, snow, lawn conditions) or player injuries. The duration of the changeover interruptions between games and sets should strictly follow the official states in the International Tennis Federation’s (ITF’s) rule book.

• Full commitment Both athletes were fully committed to the match, without any abnormal situations like match-fixing or abandonment due to disparity in strength. Previous head-to-head records between the two players that could have affected their confidence are not considered.

• No extra disturbence 微信号：MATHmodels There are no disturbing incidents before or during the match that could have affected the players’ mentality, including family emergencies, public opinion influences, etc. In this sense, the mental fluctuations of both the two players can be attributed solely to limited factors such as scoring, running, and physical condition on the field.

• No physical exertion All players experienced the same number of matches in earlier rounds and were in good and consistent physical condition before this match. The physical exertion of the players due to different situations encountered in the previous rounds was negligible.

2.2 Notations

Symbol Definition

M(x) Momentum at point x P(x) Momentum based on points G(x) Momentum based on games ri Scoring rates in one game gi Game scores pi Point scores wi Weights for game scores ωi Weights for point scores P1/2(x) Player 1 or 2’s predicted momentum R1/2(x) Player 1 or 2’s real momentum L Loss function N Maximum point number in a match

3 Data Processing

3.1 Data Cleaning

微信公众号：数学模型 We based our study on the data from all Wimbledon 2023 men’s matches after the first 2 rounds (COMAP, 2024). In the table, we found some missing values and outliers. For example, in the ”speed mph” column on row 408, there is a missing value. Considering that a player’s serve speed tends to be continuous within a game, we used Lagrangian interpolation to fill in the missing values. It is worth mentioning that we chose the data points within the same game as the missing value as the given data points. This avoids overfitting and ensures the credibility of the missing value replacement. Taking the serve speed in row 408 as an example, the replaced value is 115mph. Due to limited space, the specific calculation process is not shown here.

3.2 Data Compression

The massive redundant tabular data volume does not necessarily benefit our subsequent prediction 微信号：MATHmodels model. Therefore, we hope to use the principal component analysis (PCA) method to reduce the dimensionality of the data. Before this, we first utilized the Spearman correlation analysis to find the correlations between different data categories. For example, the ”distance ran during points” of two players in a match has a strong correlation. Therefore, ”p1 distance run” and ”p2 distance run” can be compressed into one dimension. As shown in Figure 2 below, we can determine the objects for PCA compression through the Spearman correlation analysis.

moved by two players, break point conversion rates, and winning points. Blue indicates a positive correlation, while green indicates a negative correlation.

In the graph, there is a clear positive correlation between the distances moved by the two players, a negative correlation in the winning points category, and varying degrees of positive correlation between their individual break point performance and overall break point conversion. As a result, it is possible to compress this initial ten-dimensional data vector into a lower-dimensional representation. In the same 微信公众号：数学模型 way, we can broadly categorize these factors into three groups. The result will be a three-dimensional vector, which saves a lot of computational resources in following analysis.

3.3 Data Overview

Analyzing the ”Number of Won Games per Set for each player” in a tennis match reveals insights into performance consistency, adaptability, and resilience. It showcases stamina, strategic adjustments, and psychological strength as players’ effectiveness evolves. This metric signifies a player’s ability to maintain or elevate their performance level under match pressure.Additionally, evaluating the ”Scoring Differences of Each Game in Each Set” unveils the match’s competitiveness, highlighting moments of dominance or vulnerability. It aids in identifying critical turning points and strategy effectiveness, 微信号：MATHmodels providing a detailed view that complements broader performance trends observed through won games. Together, these analyses comprehensively assess player dynamics and strategic outcomes in tennis matches.

(a) (b)

point difference between the two players in each game of each match. The size of the dots represents the absolute value of the point difference, and the color depth of the dots indicates the frequency of occurrence of that point difference.

In essence, Figure 3 (a) portrays the competitive nature of a tennis match, with both players having their moments of strength and struggle. The second figure highlights the competitiveness, momentum swings, and ultimately, the outcome of the match based on each player’s performance in individual games. Through these two figures, we can have an overview of the whole match. Both figures devide the match into five sets, which allows us to analyze the match from different perspectives. In this way, we obtain the basic ideas for further analysis: devide match into sets, and then into games.

4 Evaluation: Momentum and Swings

4.1 Definition of Momentum

微信公众号：数学模型 In physics, momentum represents a kind of force that is generated by the movement of an object. The faster you go, the harder it will be for someone to stop you. Here in tennis, the concept of momentum is almost the same. It represents the difficulty of stopping a player from his scoring streak, or the effort needed to reverse current disadvantages. To be more specific, the momentum of a player is largely determined by:

• Microscopically, the scoring of several hits in the vicinity of the moment;

• Macroscopically, the overall performance of the player in the current set.

Based on our understanding of momentum, its minimum unit of change is accurate to each point. Therefore, when studying the momentum of a certain player in a match, we want to design a function M(x), where the independent variable x is the number of the point in the match, and the dependent variable is the standardized momentum. Overall, this function M(x) is obtained by adding two parts, 微信号：MATHmodels namely:

M(x) = α · G(x) + β · P(x) + ϵ

G(x) mainly focuses on a baseline momentum value that each game within a set should have. For any point in a game, we will calculate an invariant baseline momentum value for the player based on the scoring conditions of the previous and next five games, which exactly builds up G(x). Taking the exponential weighted moving average (EWMA) algorithm as our reference, we formulated a specific calculation formula for G(x) (Lucas & Saccucci, 1990; Cox, 1961). To be noted, the weights have been slightly simplified and adjusted to ensure the consistency of the calculation of G(x) for serving and receiving games.

In our algorithm, the largest weight w0 = 0.4 is assigned to the score of the current game, denoted as g0; the adjacent previous and next game scores g−1, g1 were assigned moderate weights w−1 = w1 = 0.25; the two games further backward and forward g−2, g2 were assigned the smallest weights w−2 = w2 = 0.05. Since g−2, g0, and g2 belong to serving games while the rest two g−1, and g1 belong to receiving games (or both two group reversed), we allocated a total weight of 0.5 to each category to ensure consistency in calculating G(x) for either serving or receiving games. In conclusion, we have:

i=2 X wi · gi = 0.05 g−2 + 0.25 g−1 + 0.4 g0 + 0.25 g1 + 0.05 g2 G(x) = i=−2

Considering the game scores gi assigned based on the scoring conditions of each game, we believe simply using the scoring rate linearly is flawed. For example, previous research has pointed out that a 100% scoring rate to win a game should boost momentum slightly more than a 67% rate, such as leading 40:30 then winning one more point (Weinberg & Jackson, 1989). However, losing the game with a 33% rate, although still only differing by 33% from 67%, represents a huge change in momentum. Therefore, we introduced sigmoid function instead of the linear relationship between game score and scoring rate, to greatly amplify the impact on momentum between winning and losing a game. Figure 4 provides a direct comparison, as the green region is largely expanded by the sigmoid function. Denote the scoring rate of the i-th game as ri, we have:

e10ri−5 0 ⩽ri ⩽1 gi = 1 + e10ri−5, 微信公众号：数学模型 微信号：MATHmodels (a) (b)

Linear relationship (b) Sigmoid relationship. The difference between 33% and 67% scoring rate is emphasized by the sigmoid function.

The two plots shown above serve as a direct comparison between the linear and sigmoid relationship between scoring rate and game score. The x-axis represents the scoring rate, and the y-axis represents the game score, both ranging from 0 to 1. Near the middle point (0.5, 0.5), the sigmoid function has a much steeper slope than the linear function, which means that the momentum change becomes more sensitive to the win or loss of the game. As shown in the figure, the sharp difference between 33% and 67% scoring rate is now very obvious, which is consistent with our expectations.

On this basis, P(x) focuses on momentum changes within a game due to differences in consecutive points or overall scoring situations. Similar to G(x), we applied EWMA at the more microscopic level of adjusting by points within a game (Hunter, 1986). Likewise, to ensure strong correlation between momentum and current scoring as well as previous and next scoring differences, we decided to assign different weights to the scoring conditions of the previous and next five points. To keep a sense of continuity, we set the weights for point scores to be the same as the weights for game scores, namely ωi = wi. Thus we have:

i=2 X ωi · pi = 0.05 p−2 + 0.25 p−1 + 0.4 p0 + 0.25 p1 + 0.05 p2 P(x) = i=−2

Here pi = 1 means the player wins the point while pi = −1 means the player loses the point. With the addition of G(x) and P(x), we have successfully defined the momentum function M(x). To be noted, we have standardized the momentum function M(x) and set α = 1, β = 0.05, γ = 0. The momentum of two players at one moment always add up to one. The core idea over the whole process is visualized in Figure 3 below. In the picture, the darker the pattern is, the further it is from the current moment. Green ball represents winning the point and black ball represents losing it there.

微信公众号：数学模型

微信号：MATHmodels

4.2 Model Visualization and Validation

With our definition of momentum, we are now able to identify which player is performing better at any moment. We can also visualize the momentum change over the whole preocess by plotting the momentum function M(x) against the point number x. Take the classical match between Alcaraz and Djokovic in the 2023 Wimbledon Gentlemen’s final as an example, we can see the momentum change of both players in Figure 6 below.

represents Djokovic’s momentum, while the blue stones correspond to Alcaraz. The scores for the five sets were 6:1, 6:7, 1:6, 6:3, 4:6. Djokovic narrowly lost to Alcaraz with a total score of 2:3.

As shown in the picture, the momentum of Djokovic largely repressed Alcaraz’s momentum in the first set. This is exactly the case as Djokovic won five games in a row at the very begining. The fluctuating curves that follow show both players becoming locked in a grueling battle in the second set, which is consistent with the final result of the second set being decided by a tiebreak. In this sense, we 微信公众号：数学模型 can say that our model is able to reflect the real situation of the match.

To further apply our model, we might be interested in the deep reasons behind the runs of success by one player. Intuitively speaking, the worth-noticing swings in play happen when the momentum of one player changes significantly. Put it graphically, these swings are located at the sharp corners of the momentum curve.

However, from our rough curve, we might end up with a lot of ”swinging points”, most of which happening When the two players are competing steadily but fiercely. For example, from the second set shown in Figure 4, we can find many sharp corners. This is a result from the two players’ good and steady performance in their own service games, which is not what we want for swings. To solve this problem, we came up with an idea to filter out the ”unimportant” corners by smoothening the curve.

微信号：MATHmodels (a) (b)

(c) (d)

Wavelet Filter (d) Convolutional Moving Average Filter. The one we chose is (c) Wavelet Filter. Grean circles show where the filtering algorithm performed unsatisfactorily.

The main idea behind smoothing the curves borrows from several algorithms in digital signal processing. Our goal is to filter outliers and anomalies while preserving the momentum change trends and other key features, in order to effectively process non-stationary and nonlinear data values.

微信公众号：数学模型 Initially, we adopted the moving median filter method similar to setting up a sliding window and weights as described above (Yin & Lin, 1996). We also tried to emulate hardware filtering implementations using an FIP filter (Lim, Yong, & Parker, 1983). In addition, we drew on more recent studies, trying wavelet filters and convolutional moving average filters respectively (Qiu & Hai, 2006; Trad, Daniel, & Travassos, 2000; Yin & Du, 2022). Figure 7 above combines and compares the results obtained by the four filtering algorithms when selecting wavelet ”coif5” and decomposition level to be three.

Comparing the four filtering effect charts, it is evident that the curve obtained by the wavelet filter meets our requirements best. The curves from the convolutional moving average filter do not stay close enough to the original function at the beginning and ending stages, and fail to fit the intense competition at the end of the fourth game. The FIR filter result exhibits significant lagging, while the moving median filter leads to many step-like functions, disqualifying both methods. From the curve 微信号：MATHmodels processed by the wavelet filter, we can identify the time points when the players’ momentums reach steady extreme values, capturing the important points during the match’s progression.

4.3 Randomness & Certainty of Swings

men’s final. The blue points are the swings we are looking for. As we are labeling integer points, there might be some deviation.

In fact, these extreme points on the momentum curve are not necessarily the swings we are looking for. When swings taken place, both players might expect a sharp change in momentum, which actually requires the a large enough curvature. In other words, the points with zero first derivatives of momentum and large absolute value of second derivatives are the swings we are looking for. As a result, we decided 微信公众号：数学模型 to calculate the first order difference of the momentum function M(x). The results are shown in Figure 8 above. The points with zero first-order difference and second-order difference with absolute value bigger than 0.03 is labeled blue as swings point.

Still take the 2023 Wimbledon Gentlemen’s final as an example, we now discuss whether the swings happen randomly. We first applies a run test to determine the randomness by labeling the swings as ”1” and other normal points as ”0”. The P value calculated by the run test is 0.000, far less than 0.05, which means the swings are random in the aspect of statistics.

However, when we try to find the events that lead to these turning points, we find that these swings in momentum have actual meanings. For example, the 68th point in the first set has zero first derivatives in momentumand a large second derivative. This is exactly the point when Djokovic, under a streak of consecutive losses, forcefully broke Alcaraz’s serve to break the slump. This turning point indicates 微信号：MATHmodels the swing from Alcaraz’s dominance to a phase of equilibrium established by two players.

Similarly, the 296th point in the second set is another very important turning point. Here the first derivative of momentum is zero and the second derivative is very large. This is the point when Alcaraz, under a streak of consecutive losses, broke Djokovic’s serve to break the slump. In the opening stages of the decisive set, a crucial break was efficiently achieved, breaking the deadlock. After that, there were no more turning points to assist Djokovic in making a comeback, signaling Alcaraz’s impending victory as he lifted the ultimate championship trophy.

In conclusion, the swings in momentum are random if they are viewed solely as a sequence of numbers. However, when we take other factors into consideration, we find that these swings are certain to happen to some extent. The certainty will be quantified and discussed in the next section. Now what our estimation model tells us is the momentum curve and the swings throughout any known man’s tennis match.

5 Prediction: Time Series Forcasting

5.1 Model Selection: RNN, GRU, & LSTM

Now that we have processed the data and obtained enough data for momentum and swings, we are ready to predict the future of a match. In last sections, we have verified the correlation between momentum and other factors like the distance covered by two players. Against this background, we would like to make use of the whole dataset in our prediction model. Although we have compressed the data by reducing its dimension (PCA), there still exists factors too many for us to adjust the weights manually. Therefore, we decided to apply different Rerrent Neural Network (RNN) to predict the future of a match.

Given our goal of processing sequential data, we ultimately decided to select the model with the best predictive performance from among basic RNN and its more advanced counterparts GRU and LSTM. We controlled the training dataset to be consistent and chose the first match in the table data (match id 2023-wimbledon-1301) as the unified test set. According to previous research, RNN might have difficulty with long-term dependencies due to vanishing gradients. GRU solves this problem by using gating mechanisms. For LSTM, those explicitly designed memory cells might perform better in modeling long-term dependencies, which is required in our task. So we expect LSTM to outperform 微信公众号：数学模型 the other two models. The loss function we use to train our networks is shown as follows:

sPN x=1[P1(x) −R1(x)]2 + PN x=1[P2(x) −R2(x)]2 L = 2N

Here, L represents the loss, N represents the maxmimum point number in this match, P1/2(x) represents the predicted momentum of the first/second player at the x-th point, while R1/2(x) represents the real momentum of the first/second player at the x-th point. In building the neural networks, we chose a structure of embedding GRU / LSTM / RNN (3 layers: 32 + 32 + 16 nodes respectively) with dense layers (16 + 2 nodes) for all three models. The number of layers and nodes were kept consistent. As shown in Figure 9 below, our three neural networks had overall similar structures, with 微信号：MATHmodels small differences in the details.

three hidden layers, which makes the difference.

provements. From the fit between the predicted curves and true momentum curves, we can see that the predictions from GRU and RNN were decent, while the most advanced LSTM was quite unsatis- factory. This could be because the training dataset is too small, and there exist noticeable differences between matches. This result, inconsistent with our expectations, prompted us to improve the models by introducing clustered transfer learning.

微信公众号：数学模型 微信号：MATHmodels

represents the true momentum curve, while the blue, green, and light purple curves represents the momentum curves predicted by RNN, GRU, and LSTM respectively.

5.2 Transfer Learning: PCA & K-means

In order to improve our model, we need to cluster the matches in the dataset into a few groups. Here we temporarily set the number to be 3, and use the K-means algorithm to cluster the matches. Due to computational constraints, we first used PCA to reduce the full dataset down to 3-dimensional data points, under the premise of preserving the correlations between the different factor data. We then randomly selected three points as cluster centers to start the iteration. In each iteration, we first computed the distances between all points and centers. Next, for each point we found its nearest center, and assigned it to the cluster represented by that center. Finally, we updated each center using the mean of the points in its cluster. The iteration stopped when the change in center positions was small enough.

Algorithm 1: k-Means Clustering Algorithm

Data: Dataset with n data points and cluster numbers k

Result: Cluster groups and cluster centroids

1 Initialize k centroids by randomly selecting k points

2 while Change of cluster center centroids is larger than a threshold do for Each data point do 3 for Each centroid do 4 Calculate the distance between the centroid and the data point 5

Assign the data point to the cluster with the nearest centroid 6 Append the cluster number to the data point 7

for Each cluster do 8 Calculate the mean and update it as the new centroid 9 After K-means clustering, we are then able to conduct clustered transfer learning. For the validation set, i.e. the first match, we first identified matches in the same cluster, i.e. closest matches, among the three clusters. We trained the models on these matches, and then trained again on the first match with its given dataset. The three plots (a), (b), and (c) at the first line of Figure 11 show the prediction 微信公众号：数学模型 capabilities of all three models were greatly improved. Among them, LSTM’s performance caught up with the other two models, reaching a level that was basically consistent with or even surpassing them. We can also stop training the model without going back to the first match (test dataset). It turned out to give us a better result, as shown in the corresponding three plots at second line of Figure 11.

微信号：MATHmodels

first line shows the results after training the model on the first match, while the second line shows the results after training the model without going back to the first match.

In order to more rigorously demonstrate the performance of the three prediction models after introducing clustered transfer learning, we recorded the train loss and test loss data for each model in the table (Figure 12) below. Reassuringly, the LSTM model achieved a test loss of 0.2 under the Only Transfer with Clustering training method, close to its performance on the training set and becoming the most accurate among the three models. Meanwhile, ”train loss = test loss” also means that if we expand the size of the training dataset, it is very likely that we can further easily improve the test performance of the LSTM model. At this point, we have determined to use the LSTM model as our prediction model, and further examination of its capabilities will be discussed in the sensitivity analysis.

微信公众号：数学模型

5.3 Related Factors: XGBoost & SHAP

Neural networks are well known for their excellent performance when working with large datasets. 微信号：MATHmodels With the current dataset, we have increased the prediction accuracy of LSTM on momentum to a relatively high level through various improvement methods. Through the algorithms mentioned previously, we can accurately identify the occurrences of swings based on the momentum curves, and provide tennis players and coaches with a proper predictive interval. The neural network is quite outstanding in terms of predictive capabilities.

However, as a nonlinear model, the mapping between inputs and outputs in a neural network is very complex, making it difficult to decompose the inputs and calculate each factor’s correlation. Moreover, as shown in Figure 8 above, although the embedding layers are different, all neural network models can have complex structure in one layer alone. The might also face the issue that the same input contributes differently at different time steps. In theory, we could try adding random noise to the input vectors and check which inputs affect the prediction results the most when noisy. But this requires us to abandon PCA dimensionality reduction on the original dataset, which means a training process that consumes huge computational resources and time. This poses considerable difficulties for our current team.

Therefore, we decided to introduce the XGBoost model along with the SHAP model to help us analyze the importance of each factor in the prediction. XGBoost is a kind of gradient boosting decision tree model, which is very good at analyzing the importance of each factor in the prediction. It provided us with a way to predict momentum and swings without reducing the dimensionality of the original dataset. We used the same dataset as the training set for the neural network, and the same test set as the validation set. The results are shown in Figure 13 below. The importance of each factor is calculated by the average gain of the factor in the decision tree. The larger the average gain, the more important the factor is in the prediction. In other words, the top 5 factors in the figure are the most related factors to the swings in man’s tennis matches.

微信公众号：数学模型 微信号：MATHmodels

As we can clearly see from the figure, the factor most related with the swings are the distance run by the two players during points. Following are the game numbers of the two players, whose importance is self-evident. Other related factors are the speed, direction, and depth of serve. The depth of return also plays an important role.

With the conclusion above at hand, we are now able to give advice to players who are going to start a match with different opponents. Analysis of the momentum curve data from their previous matches should play the most important role here. We can analyze the curve and swings from an overall point of view, or compare the correlation between momentum and those most-important factors one by one.

For example, if player A’s past momentum swings show a concentrated distribution, it indicates relatively stable state changes. In contrast, a more dispersed distribution for player B suggests less stable fluctuations. We can then recommend the more stable player A to adopt an aggressive offensive play, as once gaining an advantage, he is more likely to maintain momentum until winning. Meanwhile, player B with larger state variations should play cautiously and avoid falling behind early.

We can also compare the timing distribution of momentum swings in past matches. This also provides useful suggestions. For example, if player A often drops momentum (concentrated negative swings) in late 2nd set, it is very likely that he will experience a physical limit during that point. As a result, he is suggested to pay more attention and assign more strength to that stage of match.

In summary, by examining differences in momentum curve characteristics between the two players’ previous matches, we can identify rhythmic and psychological fluctuation patterns unique to each player. This helps us offer strategic advice to tennis players for their new matches. It demonstrates the extensibility and practical value of our momentum prediction model.

6 Sensitivity Analysis

The real sports competition environment is often much more complex than these theoretical data tables. While our neural network model has achieved very good performance on existing datasets, 微信公众号：数学模型 considering unexpected factors in real-world scenarios, it’s very likely that there may be inaccuracies in the data collected before the game. After data processing and cleaning, the number of eligible data points may be limited and may not reach our expected optimal number of around ten data points. Therefore, we are conducting sensitivity testing on the model here to assess its practical applicability in real sports competition scenarios.

6.1 Step Size in the LSTM Model

Since we have chosen LSTM as the basis for the momentum prediction model, the sensitivity analysis will focus on its step size. That is, we want to obtain the relationship between model prediction accuracy and the amount of data provided by the test set. The final results are shown in Figure 14, 微信号：MATHmodels the bar chart below, which is beyond our expectations. For LSTM alone, even increasing the step size to 30 is far from the amount of data it needs to achieve the ideal prediction effect, which is also why we introduced cluster and transfer learning. For the LSTM only with transfer learning prediction method we approve as the most accurate, we find that a step size around 10 is already sufficient to make relatively accurate predictions, and further expanding the step size may even risk reducing accuracy.

size, and the y-axis represents the prediction accuracy. The blue bar represents the prediction accuracy of the LSTM model, and the orange bar represents the prediction accuracy of the LSTM model with transfer learning.

As a result, we suggest that when making predictions for men’s tennis matches with a five-set system, try to use a step size of 10-15 balls to predict the next ball, and even the general trend of the entire match. Under the current situation where the training set size is limited, blindly increasing the step size not only fails to achieve better results, but also risks reducing the credibility of the prediction. 微信公众号：数学模型 In more intuitive terms, from the perspective of neural network models, the trend of each point in a men’s tennis match often has a higher correlation with the local context than the global context. The sensitivity analysis tells us that coaches may want to pay more attention to players’ performances in the first two to three sets, in order to assess their current state. Standing from a higher perspective and using the overall trend as the logical fulcrum, it is actually more likely to misjudge the current situation.

6.2 The Number of Clusters in K-means

In our prediction model (LSTM), another parameter worth further research is the number of clusters K in the K-means algorithm. Here, we will explain why all matches are divided into three categories in the previous section, and show the impact of the number of clusters on the prediction capability of 微信号：MATHmodels the model, taking LSTM as an example. We set the number of clusters to be 1-5, 10, 15 respectively, and present the deviation rate of the prediction model on the test case (Match 1301) in the form of a bar chart in Figure (a) below.

(a) (b)

numbers of clusters. (b): The three-cluster result in the 3-dimensional space.

As can be seen from the above figure, the performance of the prediction model reaches its minimum when the number of clusters is 3. Therefore, we choose to divide all matches into three categories in the previous analysis. The three-cluster result in the 3-dimensional space is shown in Figure (b) above. In future work, we will further explore the impact of the number of clusters on the prediction model with a much bigger dataset.

7 Conclusion

7.1 Strength and Weakness

微信公众号：数学模型 Our model is mainly divided into two parts: evaluation and prediction. Although completely different basic models are chosen, they share very similar strengths and weaknesses. Our main strength lies in the evaluation curve fitting the match situation changes, swings being almost always related to crucial moments on court, and the prediction results also providing some valuable information.

Our main weaknesses are the small dataset, lack of strong transferability of the model, and insuf- ficient neural network training. This results in a currently narrow applicable scope of our model, and limited prediction accuracy. To some extent, our model is not convincing enough.

7.2 Future Work

By testing our model on other matches, we regretfully find that our model does not possess 微信号：MATHmodels strong generalizability. When we use our model to predict the momentum changes in women’s tennis matches, there are significant divergences between the predictions and reality (data from https://www.livesport.com/en/tennis/wta-singles/us-open/). Part of the reason, of course, is that our training dataset is entirely based on men’s Wimbledon tennis matches played over five sets. The differ- ences between five-set matches and three-set matches in terms of score distribution, physical exertion, and game dynamics are quite substantial, making such a model transfer inappropriate.

Furthermore, in previous research, we have learned that gender plays an important role in momentum (Page & Coats, 2017). From the results of the winner effect (success breeds success) studies, it seems that women are less influenced by momentum due to their lower circulating testosterone levels compared to men (Page & Coats, 2017). Of course, there were also arguments that the difference between male and female tennis players was gradually closing in term of their reaction toward momentum (Weinberg, Robert, & Jackson, 1989). In the future, we may consider increasing the weight of factors that objectively affect players’ physical fitness reserves, while reducing the weight of factors which have a greater impact on players’ psychological fluctuations for women’s model.

Similarly, when we use the momentum model for assessing and predicting the situation in team sports, the results are not ideal either. Take volleyball matches as an example; it is challenging to predict the course of a match through momentum, let alone the fact that volleyball team coaches can strategically call timeouts to disrupt or break the opponent’s advantageous momentum. Our findings align with previous research, which suggests that in team sports with multiple players, the overall impact of momentum is greatly weakened (Fu, Ke & Tan, 2015). The on-court scoring reflects the teamwork and synergy of the team more than the individual players’ psychological activities or skills. In these cases, we may consider focusing more on strategic momentum rather than psychological momentum.

For the prediction model of tennis momentum, two methods can be used to further improve it. On one hand, better clustering methods can be applied. Clustering methods for time series data have been emerging in recent years, which achieve better effects in grouping the elements (Saito et al. 2024; Inoue et al. 2024). On the other hand, various data synthesizing methods have been proposed, which can solve the problem of insufficient data, thus upgrading the performance of deep learning models (Yoon et al. 2019; Theodorou et al. 2023).

8 Memorandum

To: Tennis Coaches and Players From: MCM Team #2406324 微信公众号：数学模型 Date: Feb 6th, 2024 RE: Utilizing Momentum Analysis for Enhanced Performance in Tennis Matches

Executive Summary:

This memorandum summarizes our findings on the role of momentum in tennis, drawing on comprehensive analysis conducted on Wimbledon 2023 men’s matches data. Our research underscores the impact of momentum swings on match outcomes and provides actionable strategies for coaches to prepare players for effectively managing these dynamics. For detailed insights and data-driven evidence, readers are directed to sections covering the evaluation of momentum (Section 4), its prediction (Section 5), and sensitivity analysis (Section 6) within our full research paper.

Understanding Momentum’s Role: 微信号：MATHmodels Our analysis unequivocally demonstrates that momentum significantly influences the flow and eventual outcomes of tennis matches. An increase in momentum correlates with improved performance, while a decrease often precedes a shift in match dynamics. Key indicators of momentum shifts include consecutive winning points and critical game-winning performances, which can serve as precursors to changes in the game’s flow.

Strategies for Coaches and Players: 1. Psychological Resilience Training Encourage mental toughness and focus, particularly in situations where momentum is not in the player’s favor. Techniques such as visualization, positive self-talk, and stress reduction can be invaluable in maintaining composure and concentration during pivotal moments.

2. Analyzing Opponent Data Leverage match data to identify patterns or weaknesses in opponents that could lead to momentum shifts. This involves a thorough analysis of previous matches to understand potential triggers for momentum changes and developing strategies to exploit these opportunities.

3. Simulating Momentum Shifts in Practice Incorporate scenarios in training sessions that mimic situations where momentum shifts occur. This will help players adapt to various match situations, enhancing their ability to respond effectively to both positive and negative momentum swings.

Conclusion and Suggestions:

Momentum plays a crucial role in the dynamics of tennis matches, influencing both the psychological state of players and the overall match outcome. By recognizing the signs of momentum shifts and preparing strategies to manage these changes, coaches and players can gain a competitive edge. It is essential to integrate momentum management into training regimes and match strategies to optimize performance and achieve success in competitive tennis play.

For further details on our methodologies, data analysis, and additional recommendations, please refer to the comprehensive sections within our research paper.

9 Appendices

1 import matplotlib.pyplot as plt 微信公众号：数学模型 2 import pandas as pd 3 import numpy as np 4 import math 5 from sklearn.preprocessing import MinMaxScaler 6 from sklearn.metrics import mean_squared_error 7 import preprocessing 8 import tensorflow as tf 9 from tensorflow.keras.layers import GRU, Dense,SimpleRNN ,LSTM 10 from tensorflow.keras.models import Sequential 11 import seaborn as sns 12 from transferdata import transferdata 13 np.random.seed(7) 14 transfer = 1 微信号：MATHmodels 15 transfer_option = 4 16 data = pd.read_csv(’2023-wimbledon -1301.csv’, usecols=list(range(5,50))) 17 dataset = data.to_numpy() 18 scaler = MinMaxScaler(feature_range=(0, 1)) 19 dataset[:,range(43)] = scaler.fit_transform(dataset[:,range(43)]) 20 train_number = int(len(dataset) * 0.7) 21 test_number = len(dataset) - train_number 22 train_original , test_original = dataset[0:train_number ,:], dataset[ train_number:len(dataset),:] 23 step_size = 6 24 trainX , trainY = preprocessing.new_dataset(train_original , step_size) 25 testX, testY = preprocessing.new_dataset(test_original , step_size) 26 #getting transfer trainX and trainY in similar ways 27 model = Sequential() 28 model.add(LSTM(32,input_shape=(step_size ,45), return_sequences=True)) 29 model.add(LSTM(32, return_sequences=True)) 30 model.add(LSTM(16)) 31 model.add(Dense(16, activation=’sigmoid’)) 32 model.add(Dense(2, activation=’sigmoid’)) 33 model.compile(loss=’mean_squared_error’, optimizer=’adam’) 34 if transfer == 1:

model.fit(trainX_transfer , trainY_transfer , epochs=60, batch_size=16, 35 verbose=2) 36 else:

model.fit(trainX , trainY , epochs=60, batch_size=4,verbose=2) 37

38 39 if transfer_option==1:

for layer in model.layers[:4]: 40 layer.trainable = False 41 model.fit(trainX , trainY , epochs=30, batch_size=4, verbose=2) 42 43 elif transfer_option==2:

for layer in model.layers[-3:]: 44 layer.trainable = False 45 model.fit(trainX , trainY , epochs=30, batch_size=4, verbose=2) 46 47 elif transfer_option==0 or transfer_option==3: 微信公众号：数学模型 model.fit(trainX , trainY , epochs=30, batch_size=4, verbose=2) 48 49 trainPredict = model.predict(trainX) 50 testPredict = model.predict(testX) 51 trainScore = math.sqrt(mean_squared_error(trainY, trainPredict)) 52 print(’Train RMSE: %.2f’ % (trainScore)) 53 testScore = math.sqrt(mean_squared_error(testY, testPredict)) 54 print(’Test RMSE: %.2f’ % (testScore)) 55 Real_Y_1 = np.vstack([trainY[:,0].reshape((-1,1)),testY[:,0].reshape ((-1,1))]) 56 Real_Y_2 = np.vstack([trainY[:,1].reshape((-1,1)),testY[:,1].reshape ((-1,1))]) 57 Predict_Y_1 = np.vstack([trainPredict[:,0].reshape((-1,1)),testPredict 微信号：MATHmodels [:,0].reshape((-1,1))]) 58 Predict_Y_2 = np.vstack([trainPredict[:,1].reshape((-1,1)),testPredict [:,1].reshape((-1,1))]) 59 x = np.arange(1, len(Real_Y_1) + 1, 1) 60 plt.plot(x, Real_Y_1 , label=’Real_momentum_1’) 61 plt.plot(x, Predict_Y_1 , label=’Predict_momentum_1’) 62 plt.title(’Real and predicted momentum for player 1(LSTM only with transfer learning)’) 63 plt.legend() 64 plt.show() 65 plt.plot(x, Real_Y_2 , label=’Real_momentum_2’) 66 plt.plot(x, Predict_Y_2 , label=’Predict_momentum_2’) 67 plt.title(’Real and predicted momentum for player 2(LSTM only with transfer learning)’) 68 plt.legend() 69 plt.show() 70 data_to_save = np.column_stack((Real_Y_1.flatten(), Real_Y_2.flatten(), Predict_Y_1.flatten(), Predict_Y_2.flatten())) 71 np.savetxt(’LSTM only with transfer learning.csv’, data_to_save , delimiter =’,’, header=’Real_Y_1 ,Real_Y_2 ,Predict_Y_1 ,Predict_Y_2’, comments=’’)

Listing 1: my Python code
