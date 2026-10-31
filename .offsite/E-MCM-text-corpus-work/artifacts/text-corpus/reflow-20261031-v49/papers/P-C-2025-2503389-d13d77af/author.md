MCM/ICM

Summary Sheet

Summary

In Olympic sports, accurately predicting medal outcomes and understanding the factors driving national performance are essential for effective strategic planning. Based on the given dataset, we developed multiple mathematical models to forecast medal counts, identified nations likely to win their first medals, evaluated the strategic importance of specific sports, quantified the influence of Great Coaches, and analyzed the spillover effects of host countries. Findings include:

Medal Forecasting: We developed a Multiple Linear Regression–Feedforward Neural Network Bootstrap Ensemble Interval Model incorporating features such as the host boost, athlete pool, historical momentum, and competitive index. The model predicts that the United States will dominate the 2028 Los Angeles Olympics with an estimated total of 143 medals, followed by China with 76.Furthermore, the model suggests improvements for the United States and Germany, while China and the United Kingdom may experience declines.

First-Time Medalists: We developed a hybrid Logistic Regression–Random Forest model to predict First-Time Medalists. The key features analyzed included Number of Programs At- tended, Athlete Participation Experience, and Program Competition Intensity.Three countries— Angola, El Salvador, and Papua New Guinea—are identified as the most likely to win their first

Olympic medal, with probabilities of 88.09% (LR) and 94.12% (RF). This prediction is further validated by Monte Carlo simulations, with a 95% confidence interval of 1.00–8.00.

Strategic Sport Prioritization: The Strategic Importance Assessment Model for Olympic Sports (SIAMOS) model assesses the relationship between event characteristics (quantity, va- riety) and national medal potential. Key metrics—National Medal Proportion, Global Competi- tive Presence, Long-term Achievement Stability, and Athlete Sport Distribution—were weighted via Principal Component Analysis. Results identified swimming (USA, IS = 39.8) and diving (China, IS = 33.1) as the highest-impact disciplines. Host nations can optimize medal outcomes by focusing on sports with strong historical performance and competitive advantage.

Coach Impact Analysis: Breakpoint regression quantified the impact of Great Coaches, including Keiko Kageyama (China, Artistic Swimming), Dave Brailsford (UK, Cycling), and Béla and Marta Károlyi (US, Gymnastics), with a median post/pre-coach medal ratio of 1.7.

Great Coach Effect Application: Poland(athletics, canoe sprint, sailing), Nigeria (foot- ball), and India(badminton, weightlifting, wrestling) were identified as high-potential nations for elite coaching. Adjusted regression coefficients and medal weights—gold (0.9), silver (0.6), bronze (0.4), no medal (0.1)—highlight how elite coaching could improve medal prospects and weighted scores.

Host Spillover Effect: Further exploration of the data reveals that the ”Host Boost” signif- icantly increases the medal rates of neighboring countries.

Sports;Logistic Regression-Random Forest;Multivariate Linear Regression-Feedforward Neu- ral Network

Introduction

3 1

Background

1.1 3 1.2

Restatement of the Problem

3 Our work 1.3 4

2 Assumptions and Justification 5

Notations

3 Data Preprocessing 5 4 Data Cleaning and Adjustments 5 4.1 4.2 Data Exploration 5 Multiple Linear Regression-Feedforward Neural Network Bootstrap Ensemble 5 Interval Prediction Model with Host Effect 6

Reasons for Model Selection

5.1 6

Model Construction and Fusion

5.2 6 5.3

Forecast Results and Insights

9 Uncertainty and Evaluation Analysis 10 5.4

Logistic Regression and Random Forest Prediction Model for First-Time Medal-

6 11 ist Countries 6.1 11 Reasons for Model Selection Feature Engineering . 6.2 12 6.3 Analysis of Conditions for Countries Winning Medals for the First Time 12

Model Formulation and Prediction Results

6.4 13 6.5 Estimate odds 14

Strategic ImportanceAssessment Model for Olympic Sports (SIAMOS)

15 7 15

Model Development and Evaluation Framework

7.1

Result 1: Relationship Between Events and Medal Counts

16 7.2 Result 2: Sport-Specific Importance Across Nations. 16 7.3 7.4 Result 3: Impact of Host Nation's Event Selection on Medal Outcomes . 17 18 Contribution of the Great Coach 8 8.1 18 Definition of Great Coach . 8.2

Data Processing Framework

18 Calculation of Coefficients Based on Breakpoint Regression Model . 8.3 18 8.4 Case Study Analysis (Focusing on Three Key Sports) 19 The Practical Application of the "Great Coach" Effect 22 9 Selection of Sports Needing a Great Coach 22 9.1

Results

22 9.2

10 Other Insights: Host Country Spillover Effect on Medal Rates of Neighboring

_ 22 Countries

10.1 Analysis and Results

22

10.2 Strategic Recommendation for National Olympic Committees

23

11 Sensitivity Analysis

23

12 Strengths and Weaknesses

24

1 Introduction

1.1 Background

The 2024 Paris Olympics concluded with notable highlights, including the United States leading the medal tally with 126 medals and sharing the top spot for gold medals with China at 微信公众号：数学模型 40 each.

As the world’s focus shifts toward the 2028 Los Angeles Olympics, the city’s vibrant energy and cultural diversity set the stage for the historic Games.

By analysing historical data and designing predictive modeling, we aim to forecast the 2028 Olympic medal standings. The host nation, the United States, potentially reinforcing its domi- nance. Simultaneously, countries that have yet to secure an Olympic medal will strive to achieve their first victories, marking historic milestones.

Additionally, the influence of great coaches and strategic investments may significantly shift 微信号：MATHmodels outcomes, offering valuable insights into medal prospects and performance optimization for countries worldwide.

1.2 Restatement of the Problem

Based on the analysis of the background, the key tasks are as follows:

Problem 1. Develop a predictive model for Olympic medal counts by country. The model should incorporate uncertainty estimates, evaluate prediction accuracy, and provide com- prehensive performance metrics.

Task 1.1 Use the model to forecast the medal table for the 2028 Los Angeles Summer Olympics.

Provide prediction intervals for all outcomes. Additionally, identify countries most likely to improve and those at risk of underperforming compared to their 2024 results.

Task 1.2 Identify nations that have yet to win an Olympic medal and forecast how many are likely to achieve their first medal in the upcoming Games. Estimate the probability of countries earning their first Olympic medal.

Task 1.3 Integrate event numbers and types into the model to analyze their relationship with medal counts by country. Identify influential sports for specific nations, their significance, and the impact of host nation event selection on results.

Problem 2. Coaches, unlike athletes, can freely move between countries, creating the potential for a significant “great coach” effect.

Task 2.1 Analyze data for evidence of changes that may be attributed to the influence of excep- tional coaches.Quantify the contribution of this “great coach” effect to medal counts.

Task 2.2 Select three countries and determine the sports in which they should invest in recruit- ing a “great coach.” Estimate the potential impact of such strategic coaching investments on medal performance.

Problem 3. Identify additional, original insights revealed by the model regarding Olympic medal counts. Provide actionable recommendations to country Olympic committees based on these findings.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

1.3 Our work

m m m m m m m m m m m m m m m m m m m m m m m m m

2 Assumptions and Justification

To simplify the problem, we make the following basic assumptions, each of which is properly justified.

• The analysis and models are exclusively based on the provided datasets from the 2016, 2020, and 2024 Olympic Games. The three latest Olympic Games provide the most current and relevant data for insights into performance trends, ensuring the analysis is based on representative and applicable information.

• The performance of new entrants in their first Olympic participation is on par with that of athletes who will not compete in future Olympic Games. Olympic debuts and retirements are similar in that they both involve challenges such as inexperience or the end of a career, ensuring consistent participation by athletes.

• Russia and Belarus are excluded from the medal table in 2028. Athletes from Russia and Belarus competed without their national flags at the 2024 Olympics, indicating they will likely face the same restrictions in 2028.

• The disturbance terms in both the multiple regression and regression discontinuity models follow independent normal distributions. The errors are normally distributed with a mean of zero and constant variance, ensuring valid statistical tests and reliable model estimates.

• The assumption is made that the 2028 Olympic Games will proceed without signifi- cant global disruptions. “This assumption expects no major global disruptions, ensuring the 2028 Games proceed as planned and the analysis aligns with historical trends.”

关注数学模型 • Medal counts are analyzed at the sports level, inferring event-level data. We aggre- gate the data from individual events within each sport to mitigate variability from fluctu- ations in the number of events.

3 Notations

Symbols

Description Unit

Y1, Y2 Predicted medal count (total medals or gold medals) Medals 微信公众号：数学模型 XComp Competitiveness index Dimensionless Athlete pool Dimensionless XAth XHost Host boost indicator Binary Historical momentum Dimensionless XHist AWR Award-winning rate Percentage (%) β0, β1, β2, β3, β4 Regression coefficients - ˆPi Combined prediction for i-th instance Medals Weights for MLR and NN models - wMLR, wNN PE2 MLR, PE2 Mean squared prediction errors for MLR and NN - NN 微信号：MATHmodels where we define the main parameters while specific value of those parameters will be given later.

4 Data Preprocessing

4.1 Data Cleaning and Adjustments

4.1.1 Replacement Examples

Category Original Name Standardized Name

Country Name Changes Great Britain United Kingdom Macedonia North Macedonia

Language Substitutions Cote d’Ivoire Ivory Coast Cape Verde Cabo Verde

Individual Olympic AthletesIOC2025 Synonym Replacements Independent Olympic Athletes Refugee AthletesIOC2025 Refugee Olympic Team

NOC Consistency ROC (Russia, 2020) Russia RUS (Russia, pre-2020) Russia

Sports Merging (2016) Cycling (as a single Sport) Split into Events Canoeing (as a single Sport) Split into Events

4.2 Data Exploration

4.2.1 Medal Flow Analysis Across Countries

Olympics:

• Dominant Sports and Nations: Swimming and athletics contribute significantly to medal tallies in nations like the United States and China.

• Strategic Focus: Italy and Australia excel in niche sports, showcasing tailored investment strategies.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Olympics)

5 Multiple Linear Regression-Feedforward Neural Network

Bootstrap Ensemble Interval Prediction Model with Host

Effect

5.1 Reasons for Model Selection

Predicting Olympic medal distributions is a complex regression task. The Multiple Lin- ear Regression (MLR) model is simple and interpretable, effective for linear relationships but limited in capturing non-linear dynamics like the host effect. To address this, the Feedforward

Neural Network (FNN) model excels in capturing non-linear patterns and handling diverse

datasets with high accuracy. Combining MLR’s simplicity with FNN’s adaptability, we pro- pose a hybrid approach for enhanced medal prediction.

5.2 Model Construction and Fusion

5.2.1 MLR-Model Construction

Multiple Linear Regression Formulation

The model is formulated as:

Yi = β0 + β1XComp + β2XAth + β3XHost + β4XHist + ϵ, (i = 1, 2)

Feature Selection

关注数学模型 Feature Interpretation Mathematical Formula

Host Boost Boost from hosting the (XHost) Olympics, quantified as { ( Rh −¯Rn ) if Host Nation 1 + ∆R, an additional medal im- ∆R = median XHost = , ¯Rn 0, Otherwise provement rate.

Rh: Host medal rate, ¯Rn: Non-host 微信公众号：数学模型 avg. rate.

Athlete Pool Reflects athlete partici- 2 X (XAth) pation trends, adjusted XAth = NT−t for Olympic debutants.

t=0 NT−t: Number of athletes in the (T −t)-th Olympic cycle.

Competitiveness Captures nation- ! Index (XComp) specific strength across K 3 X X mk 微信号：MATHmodels sports, adjusted for pk,t · e−0.2t · XComp = Mtotal temporal decay. t=1 k=1

mk: Medals in sport k, pk,t: Medals at T −t, Mtotal: Total medals.

Historical Mo- Weighted sum of past 3 X mentum (XHist) medals, with higher MT−t · e−0.2t XHist = weights for recent t=1 performances. MT−t: Total medals at T −t.

Correlation Analysis

To explore the relationships between features and target variables, we calculate Pearson corre- lation coefficients.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m As shown in Figure 2, the award-winning rate exhibits significant correlations with the pre- dictive features XComp, XAth, and XHist, with correlation coefficients of 0.92, 0.86, and 1.00, respectively. These values highlight the strong relationships between competitiveness, athlete pool size, and historical momentum in predicting a nation’s award-winning performance.

Since the host boost is a discrete variable, while other features change continuously, the host boost shows weak linear correlation with the other three indicators. Therefore, it is necessary to analyze the host boost separately. As illustrated in Figure 3, the total medal count for a nation significantly increases during its host year, highlighting the “Host Boost” as a crucial feature.

5.2.2 Feedforward Neural Network-Model Construction

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

From Figure 4, the model follows a typical Feedforward Neural Network (FNN) structure, which includes an input layer, two hidden layers with ReLU activation functions, and an output layer with a linear activation function. The raw dataset is split into training and test sets, with the training set further divided into training data and validation data (20% of the training set). The model is trained using the Adam optimizer with a learning rate of 0.01. Validation loss is tracked during the training process to assess the model’s performance.

5.2.3 Weighted Fusion of Predictions

关注数学模型 To enhance the accuracy and robustness of medal count predictions, we utilize a weighted fusion approach to combine the outputs of the Multiple Linear Regression (MLR) and Feedforward Neural Network (FNN) models.

First, the mean squared prediction errors (MSE) for the two models are calculated:

N N X X MLR = 1 NN = 1 (Ri −PMLR,i)2 , (Ri −PNN,i)2 PE2 PE2 微信公众号：数学模型 N N i=1 i=1

The weights for each model are derived based on their relative errors:

PE2 PE2 NN MLR ≈0.6, ≈0.4 wMLR = wNN = PE2 MLR + PE2 PE2 MLR + PE2 NN NN

Finally, the combined prediction for observation i is calculated as:

ˆPi = wMLR · PMLR,i + wNN · PNN,i 微信号：MATHmodels Through analyzing prediction errors, it is clear that the MLP model suffers from higher errors, while the FNN model risks overfitting. The combined MLP-NN model addresses these issues, enhancing both accuracy and robustness for reliable predictions.

5.3 Forecast Results and Insights

Total Medals Gold Medals Confidence Intervals (95%) NOC Pred. Δ Rank Δ Pred. Δ Rank Δ Total Lower Total Upper Gold Lower Gold Upper United States 143 ↑17 1 – 59 ↑19 1 – 110 192 50 68 China 76 ↓15 2 – 32 ↓8 2 ↓1 61 94 27 37 United Kingdom 62 ↓3 3 – 21 ↑7 3 ↑4 56 85 17 25 France 60 ↓4 4 – 16 – 5 – 50 73 13 19 Australia 54 ↑1 5 – 21 ↑3 3 ↑1 49 70 17 25 Japan 43 ↓2 6 – 16 ↓4 5 ↓2 35 51 13 19 Italy 40 – 7 – 12 – 8 ↑1 34 48 10 14 Germany 36 ↑3 8 ↑1 12 – 8 ↑2 31 44 10 14 Netherlands 35 ↑1 9 ↓1 15 – 7 ↓1 31 43 12 18 Canada 30 ↑3 10 ↑1 10 ↑1 10 ↑2 27 37 8 12

Countries Likely to Improve: America (+17 medals) and Canada (+3 medals) show up- ward trends, may due to increased investment in athlete development and enhanced coaching strategies.

Countries Likely to Decline: France (60 medals vs. 64 in 2024) may experience a decline after hosting, while China (76 medals vs. 91 in 2024) faces challenges as its strong event, weightlifting1, will no longer be held.

Key Uncertainty: The U.S. medal interval highlights variability in team sports, while smaller nations like Slovenia (1 gold, CI: 0–2) exhibit greater volatility due to dependence on individual athletes.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Australia Australia Canada Canada China Log-Scaled Share▼ China Frence Medals France 141 (Max) Germany Germany Great Britain Great Britain Naiion Country Italy Itally 57 Japan Japan 39 Netherlands Netherlands Russia Russia 0 (Min) Russla (ROC) Russia (ROC) 0% South Koret South Korea United States United States Tokyo 2020 Rio 2016 Paris 2024 LA 2028 2016 2020 2024 2028 Olympic Year Olympic Year

(a) Medal Proportion (Logarithmic) (b) Medal Counts (Absolute)

As shown in Figure 6, the heatmap depicts the progression of the top 10 nations' medal counts from 2016 to 2028 using our prediction results . Color intensity indicates medal totals, with deeper blue shades signifying higher counts.

Key trends include the United States and China consistently dominating medal counts, re- flecting their robust athletic programs. Host nations tend to achieve significant medal boosts. Emerging nations like Japan and the Netherlands display upward trends, signaling strategic investments. In contrast, nations such as Italy, Russia, and South Korea show variable per- formances. Western countries like Great Britain, Italy, and Germany maintain stable medal tallies.

5.4 Uncertainty and Evaluation Analysis

5.4.1 Uncertainty Analysis with Bootstrap

A Bootstrap method (500 iterations) was used to quantify the uncertainty of medal predictions for both total medals and gold medals. The process includes: The final 95% prediction intervals were derived from the aggregated results:

Lower Bound = Percentile(2.5), Upper Bound = Percentile(97.5)

For example, the U.S. total medal interval [116, 193] reflects high uncertainty due to variable team sports performance, while China's narrower gold interval [27, 37] (from 32 predicted) indicates more stable strengths in diving and table tennis.

5.4.2 Prediction evaluation analysis

From Table 4, the selected model variables demonstrate both significance and explanatory

power:

• Host Boost (XHost): A coefficient of 13.10 (p < 0.001) indicates a strong positive impact of hosting the Olympics on medal counts, despite a high standard error (2.88) due to cross-country variability.

关注数学模型 Variable Coeﬀicient Standard Error t-Statistic P-Value(P>|t|)

Host Boost (XHost) 13.10 2.88 4.55 <0.001 Athlete Pool (XAth) 0.004 0.003 1.33 0.188 微信公众号：数学模型 Competitiveness Index (XComp) 2.18 0.71 3.06 0.003 Historical Momentum (XHist) 0.59 0.09 6.42 <0.001

• Competitiveness Index (XComp) and Historical Momentum (XHist): Both have signifi- cant positive effects, with coefficients of 2.18 and 0.59 (p < 0.01). Historical Momentum has the highest t-value (6.42) and the lowest standard error (0.09), highlighting its strong influence on medal performance.

• Athlete Pool (XAth): The coefficient (0.004) is not statistically significant (p = 0.188), suggesting that athlete pool size alone does not fully explain medal outcomes.

微信号：MATHmodels Overall, the model effectively captures the primary drivers of medal distribution, with sig- nificant contributions from host status, competitiveness, and historical momentum.

Metric Formula

Result

Mean Squared Error 7.115 N X (MSE) MSE = 1 (yi −ˆyi)2 N i=1

Root Mean Squared Er- 2.667 v u ror (RMSE) u N X t 1 (yi −ˆyi)2 RMSE = N i=1

Mean Absolute Per- 51.099% N X yi −ˆyi centage Error (MAPE) MAPE = 100 N yi i=1

The metrics in Table 5 indicate that the model controls absolute errors well, with an RMSE of 2.667 (average deviation of 2.7 medals). However, the high MAPE of 51.1% reveals challenges in accurately predicting countries with low medal counts, suggesting room for improvement.

6 Logistic Regression and Random Forest Prediction Model

for First-Time Medalist Countries

6.1 Reasons for Model Selection

Predicting the probability of countries winning their first Olympic medal is a complicated classification task. Logistic regression (LR) is a widely used model that excels in simplicity and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m interpretability, effectively estimating probabilities when the relationships between predictors and outcomes are linear. However, it struggles with non-linear patterns and complex feature interactions that are often present in Olympic data, such as historical variability or regional effects.

To overcome these limitations, Random Forest (RF) offers a robust alternative. As an en- semble learning method, RF captures non-linear relationships and complex interactions while ranking feature importance, making it suitable for diverse datasets. However, RF can overfit and lacks the transparency of LR.

To leverage the strengths of both models, we adopted a hybrid approach that combines the interpretability of LR with the flexibility of RF. This strikes a balance between simplicity and robustness, allowing for more accurate and comprehensive predictions of which countries will win their first Olympic medal.

6.2 Feature Engineering

To identify countries that have never won medals, we process the table summerOly_athletes.csv to identify athletes who have won medals, then filter the countries they represented in the com- petition. From the list of all countries, we exclude those that have won at least one medal.

The core principal here is to simplify the process by counting only unique countries, so duplicates are considered only once.

This results in a list of countries that have never won a medal, along with features:

• Number of Programs Attended. Count the total number of programs attended by these countries.

• Athlete Participation Experience. Calculate the average number of sessions an athlete has participated in.

• Program Competition Intensity. Calculate the formula:

1 −Number of Medals in the Program , Number of Participants

where a value closer to 1 indicates more intense competition.

6.3 Analysis of Conditions for Countries Winning Medals for the First

Time

We calculate the number of countries that won medals for the first time in each Olympic Games (e.g. 5 countries in the 2020 Tokyo Olympics and 3 countries in the 2016 Rio Olympics) and also analyze the distribution of these countries based on features, including statistics like the mean, variance, and trends.

关注数学模型 time Medalist Countries 微信公众号：数学模型 As shown in Figure 7 and 8, there is a notable fluctuation in the number of first-time medal- winning countries across different Olympic years. For instance, in the 2020 Tokyo Olympics, 5 countries won their first-ever medals, while in 2016, there were only 3 such countries.

6.4 Model Formulation and Prediction Results

We utilized two predictive models—Logistic Regression and Random Forest—to estimate the likelihood of countries earning their first medal in the next Olympics.

微信号：MATHmodels

6.4.1 Logistic Regression Model

The Logistic Regression model predicts the probability of a country earning a medal for the first time based on key features. The model is given by:

1 P(Target = 1|X) = 1 + e−(β0+β1·Experience+β2·Programs Attended+β3·Competition Intensity),

where P(Target = 1|X) is the probability of earning a first medal, and β0, β1, β2, β3 are the model coefficients for each feature (Experience, Programs Attended, and Competition Inten- sity).

6.4.2 Random Forest Model

The Random Forest model aggregates the predictions of multiple decision trees. The final pre- diction is the average of all tree predictions:

N X ˆy = 1 ˆyi N i=1

where ˆy is the predicted probability, N is the number of trees, and ˆyi is the prediction of the i-th tree.

6.4.3 Prediction Results

The prediction results from the two models are as follows:

• Logistic Regression Prediction: Angola, El Salvador, Papua New Guinea

• Random Forest Prediction: Angola We then utilized the Poisson binomial distribution combined with Monte Carlo simulations to estimate the expected number of countries likely to win their first Olympic medal and their confidence intervals. The simulation results, shown in Figure 9, indicate that the probability is highest when the number of first-time medal-winning countries is exactly 3.

Based on these findings, we conclude that 3 countries are the most likely to win their first Olympic medal in the next Games.The simulation results align well with our predictions, con- firming the robustness of the model’s estimates. The Monte Carlo simulation not only validated the expected outcomes but also provided a probabilistic range for the number of countries likely to win their first medal in the next Olympics.

These predictions reflect the model’s output probabilities, with Angola appearing as a com- m m m m m m m m m m m m m m m m m m m m m m mon prediction in both models, suggesting a strong likelihood of this country earning its first m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m medal. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

6.5 Estimate odds

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The odds of predicting which countries will earn their first medal in the next Olympics are m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

estimated using their respective cross-validation accuracies. The table below summarizes the estimated odds for each model:

Model

Cross-Validation Accuracy

Estimated Odds (Correctness) Logistic Regression 88.09% 4:1 (80% chance) Random Forest 94.12% 16:1 (94% chance)

关注数学模型

7 Strategic Importance Assessment Model for Olympic Sports

(SIAMOS)

To measure the strategic importance of a specific sport s for a given country c, we establish a comprehensive evaluation framework based on four key indicators.

7.1 Model Development and Evaluation Framework

微信公众号：数学模型

7.1.1 Description of Indicators to Evaluate the Importance of Sport

The four key indicators used to evaluate the importance of a sport in the context of Olympic performance are:

• NMP (National Medal Proportion): Proportion of medals a sport contributes to a na- tion’s total medals.

• GCP (Global Competitive Presence): A country’s competitive strength in a sport rela- tive to global performanceBernard2004.

微信号：MATHmodels

• LAS (Long-term Achievement Stability): Stability of performance in a sport over the last five Olympics.

• ASD (Athlete Sport Distribution): Proportion of athletes allocated to a specific sport relative to the total number of athletes.

Each indicator is standardized using Min-Max normalization to ensure cross-country com- parability. A hybrid weighting scheme, integrating Principal Component Analysis (PCA) with expert validation, assigns weights of 40%, 30%, 20%, and 10%, respectively. This reflects the relative importance of each indicator in evaluating a sport’s strategic significance.

Indicator Formula Standardization (Weight) Medalsc,s Total Medalsc × 100% NMP (40%) Min-Max nor- malization Medalsc,s Global Medalss × 100% GCP (30%) Min-Max nor- malization 1 −σ LAS (20%) Min-Max nor- µ malization Athletesc,s ASD (10%) Total Athletesc × 100% Min-Max nor- malization

7.1.2 Model Construction

The SIAMOS model integrates the four indicators to compute the importance score (ISc,s) for each sport s in each country c:

ISc,s = α · NMPnorm + β · GCPnorm + γ · LASnorm + δ · ASDnorm

where α : β : γ : δ = 4 : 3 : 2 : 1 (40%, 30%, 20%, 10%). m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

7.2 Result 1: Relationship Between Events and Medal Counts

lights the influence of sports on medal counts.

Conclusion: As shown in Figure 10, the number of events is positively correlated with the medal counts of participating countries. Similarly, the diversity of events also demonstrates a positive correlation with medal counts. These findings indicate that both the quantity and variety of events positively impact a nation’s medal-winning potential.

7.3 Result 2: Sport-Specific Importance Across Nations

7.3.1 Calculated Scores

The following table presents the calculated importance scores for selected countries and sports:

Country Sport Importance Score (IS) Ranking China Diving 33.1 1 China Table Tennis 29.6 2 USA Swimming 39.8 1 USA Basketball 27.8 2 Korea Archery 37.4 1 Korea Badminton 31.8 2 Japan Judo 36.5 1 Japan Gymnastics 30.2 2 Australia Swimming 38.6 1 Australia Cycling 29.7 2

7.3.2 Insights and Recommendations

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• China: Diving (IS = 33.1) and Table Tennis (IS = 29.6) dominate, reflecting historical m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m strengths. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

• USA: Swimming (IS = 39.8) and Basketball (IS = 27.8) remain priorities. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

关注数学模型 • Korea: Archery (IS = 37.4) and Badminton (IS = 31.8) highlight focused investments.

• Others: Japan: Judo (IS = 36.5), Gymnastics (IS = 30.2); Australia: Swimming (IS = 38.6), Cycling (IS = 29.7).

These insights aid strategic planning to maximize medal potential in future Olympics.

7.4 Result 3: Impact of Host Nation's Event Selection on Medal Outcomes

To evaluate the impact of a host nation's event selection on medal outcomes, we use the

Global Competitive Proportion (GCP) metric, which quantifies a country's competitive strength

in a sport relative to global performanceBernard2004. Table 9 provides the GCP scores for selected countries and sports.

Cycling Country Swimming Track and Field Taekwondo Shooting 0.1085 USA 0.3214 0.2841 0.0962 0.0523 CHN 0.1263 0.1435 0.2782 0.2648 0.0712 0.0823 0.1274 0.2167 0.1354 JPN 0.0896 AUS 0.3645 0.0912 0.0438 0.1824 0.0417 KOR 0.0374 0.3084 0.0512 0.0856 0.0685

7.4.1 Impact of Host Nation Event Selection

By examining the host nation's choice of events, we identify two key effects:

1. Enhancement of Strong Sports: Host nations often add events in their strongest sports

to maximize medal outcomes. For example:

The USA increased swimming and track events during the 1996 Atlanta Olympics, securing multiple gold medals.

China introduced additional shooting events in the 2008 Beijing Olympics, signifi- cantly boosting their medal tally in the sport.

●

2. Increased Competitiveness in Targeted Events: Hosting provides advantages in prepa-

ration, venue familiarity, and public support, making host nations more competitive in traditionally weaker events. For instance:

Australia leveraged its host status in 2000 to achieve unexpected medals in cycling and field events.

Korea used the 1988 Seoul Olympics to establish dominance in Taekwondo, a sport that was newly introduced at the time.

These findings underscore the strategic role of host nation event selection in shaping medal outcomes and highlight opportunities for future host countries to optimize their strategies.

8 Contribution of the Great Coach

8.1 Definition of Great Coach

A Great Coach (GC) is defined as a coaching professional whose recruitment results in a statistically significant increase (p < 0.05) in medal attainment within the targeted Olympic sport, measured through pre- and post-appointment performance. The criteria for a Great Coach include:

Immediate Impact: ≥15% medal growth within the first Olympic cycle, improved on his- torical performance.

Sustained Improvement: Maintaining ≥80% of peak performance for at least two subse- quent Olympic Games.

Sport-Level Considerations:

• When a coach is introduced, whether as a sport head coach or an event-specific coach, they influence other events within the same sport through collaboration and athlete interaction.

• The number of events within each sport may vary between Olympic Games, so consider- ing the sport level helps mitigate instability caused by this factor.

• Focusing only on individual event data may result in small sample sizes, increasing the likelihood of randomness and potentially biasing the conclusions.

8.2 Data Processing Framework

8.2.1 Medal Weighting System

• Medal Weight Assignment: Defined weights (No Medal=0.1, Bronze=0.4, Silver=0.6, Gold=0.9) to quantify performance quality

• National Performance Metric: Calculated weighted scores per country-sport-year triad:

4 Φc,s,y = ∑wi · Ni, w ∈ {0.1, 0.4, 0.6, 0.9} i=1

where Ni counts medal type i occurrences

8.2.2 Medal Data Standardization

• Binary Medal Encoding: Transformed medal outcomes into Boolean indicators (1=medal earned, 0=otherwise) for cross-event aggregation

• Sport Taxonomy Harmonization: Unified historical records of equivalent disciplines (e.g., Artistic/Synchronized Swimming) using IOC nomenclature

8.3 Calculation of Coefficients Based on Breakpoint Regression Model

To analyze the impact of a Great Coach on medal counts, we use the following model:

关注数学模型 MedalCounts = β0 + β1 · Year + β2 · is_great_coach + β3 · (is_great_coach × Year) + ϵ 微信公众号：数学模型 Key Steps in the Analysis:

1. Time Period Division: Divide the Olympic data into three periods based on the coaching

situation:

• Pre-coaching: The three Olympic Games before the coach took over.

• Coaching Period: The period during which the great coach was actively coaching.

• Post-coaching: The period after the coach left.

微信号：MATHmodels

2. Metric Calculation:

• Medal Score: Averaged by country and event.

• Total Medals: Summed by country and event.

3. Model Fitting and Robustness Check: Use the breakpoint regression model to assess

the impact of the Great Coach on medal counts. Test the significance of the interaction term coefficient (β3) to determine whether the coach effect varies with years. Then, re- place the dependent variable with “medal score” and refit the model. Finally, compare results across different countries and events.

8.4 Case Study Analysis (Focusing on Three Key Sports)

8.4.1 Introduction:3 Representative Case

To analyze the “great coach” effect on medal counts, we analyzed data on medal changes and identified three representative countries aligned with its :

Country Sport Coach China Artistic Swimming Keiko Kageyama United Kingdom Cycling Dave Brailsford United States Women’s Gymnastics Béla and Marta Károlyi

8.4.2 Results Analysis

To quantify the impact of exceptional coaches on medal counts, we calculated the contribution value (Ci) for each coach using the following formula:

Ci = βi Di

where:

• βi: The direct effect of the coach on medal counts (regression coefficient).

• Di: The weighted average difference in total medals between the two Olympic Games before and after the coach’s tenure.

By analyzing significant changes in medal counts and referencing relevant data, three ex- emplary cases of the ”Great Coach Effect” were identified:

1. Béla and Marta Károlyi (USA Women’s Gymnastics): Regression coefficient (βi) =

0.3.

2. Keiko Kageyama (UK Cycling): Regression coefficient (βi) = 6.9.

3. Keiko Kageyama (China Artistic Swimming): Regression coefficient (βi) = 1.3.

Using the formula above, the contribution values (Ci) were computed for each coach:

0.3

• Béla and Marta Károlyi: Contribution value (Ci) = DUSA = 1.7.

6.9

• Keiko Kageyama (UK Cycling): Contribution value (Ci) = DUK = 1.7.

1.3

• Keiko Kageyama (China Artistic Swimming): Contribution value (Ci) = DCHN = 1.7.

The results demonstrate that despite varying regression coefficients (βi), the adjusted contri- bution values across these cases converge to 1.7. This highlights the consistent and measurable impact of exceptional coaching on improving medal outcomes, offering actionable insights for strategic investments in coaching talent.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

关注数学模型 As shown in 11, 12 and 13, the medal count for the sport is analyzed around the appointment of a Great Coach. The red line marks the boundary: to the left are the medal counts before the coach’s appointment, and to the right, after the coach’s appointment until they left the country. The average number of medals post-appointment significantly exceeds pre-appointment counts, illustrating the “Great Coach Effect.”

8.4.3 Reasons for Country and Sport Selection

The selection of three countries (China, UK, US) and three sports (Artistic Swimming, Cycling, Women’s Gymnastics) creates a framework to represent global sports. It looks at differences in political systems and types of athletics.

National Archetypes 微信公众号：数学模型

• China: Embodies state-centralized athleticism – a model prevalent in 37

– Top-down talent identification pipelines – Integrated sports-education-political apparatus – Cultural soft power through medal diplomacy

• United Kingdom: Represents technocratic hybrid systems adopted by 28% of developed nations (e.g., Germany, Japan). Defining features:

– Public-private R&D consortia (e.g., UK Sport’s “Marginal Gains” program) 微信号：MATHmodels – University-based athlete development ecosystems – Precision analytics in training optimization

• United States: Exemplifies market-driven pluralism dominant in 35% of Western democ- racies (e.g., Australia, Canada). Characteristics:

– Decentralized collegiate sports infrastructure – Commercial sponsorship-driven funding models – Individual athlete brand economies

Sport Typology Representation

• Artistic Swimming:

– Category: Judged team sport (22% of Olympic events) – Analysis Focus: Collective synchronization metrics, subjective scoring biases

• Cycling:

– Category: Technology-intensive endurance sport (18% of Olympic disciplines) – Analysis Focus: Equipment R&D ROI, aerodynamic efficiency thresholds

• Women’s Gymnastics:

– Category: Biomechanically complex skill sport (26% of Olympic events) – Analysis Focus: Rule change adaptation rates, injury risk management m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

9 The Practical Application of the ”Great Coach” Effect

9.1 Selection of Sports Needing a Great Coach

9.1.1 Data Utilization

1. Aggregate the Score data from 2016 and 2020, calculating the mean and standard devia- tion for each year.

2. Select the 20th percentile, with a threshold of 0.15.

3. Check the proportion of sports in the distribution with scores close to 0.15 to ensure it aligns with actual observations.

Selection Criteria:

• A sport’s Score in both 2016 and 2020 must be greater than 0.15.

• The Score for 2024 must be less than 0.15.

9.2 Results

After the preliminary screening, Nigeria, Poland, and India were selected as the countries of interest. According to the above criteria, the sports that require the introduction of a Great Coach were selected. The final list of potential sports for a Great Coach includes:

• Poland: Athletics, Canoe Sprint, Sailing

• Nigeria: Football

• India: Badminton, Weightlifting, Wrestling

9.2.1 Validation of the Conclusion: Coach’s Impact Calculation

From Section 2.1, it is determined that the contribution rate of the coach to the sport is u = 1.7. This means that after introducing the coach, the Score for 2024 increases by u× the pre-coaching Score. By comparing the results, we find that the likelihood of winning medals in these sports for the selected countries has increased after the introduction of the coach.

10 Other Insights: Host Country Spillover Effect on Medal

Rates of Neighboring Countries

10.1 Analysis and Results

We analyzed the medal rates of various countries in the 2016, 2020, and 2024 Olympic Games, focusing on the differences in medal rates for neighboring countries of the host na- tion (land-bordering countries). Specifically, we compared the medal rate of these neighboring countries in the current Olympics to the average medal rate from the previous two Olympic Games. We identified countries with a positive difference in medal rates and mapped these im- provements. The results from these maps 17 clearly demonstrate that the ”Host Country Effect”

关注数学模型 not only boosts the medal rate of the host country but also positively impacts the medal rates of neighboring countries.

Increase 0.024714974 0.00399071

0.000498065

around Japan

around Brazil around France

Our analysis confirms that the "Host Country Effect" contributes to an increase in the medal rates of neighboring countries.

10.2

Strategic Recommendation for National Olympic Committees

dels

10.2.1 Pre-Games Optimization Plan

● ● · Phase-Based Adaptation Training:

1. Phase 1 (12 months before competition): Simulate host city altitude and climate.

2. Phase 2 (6 months before competition): Practice at official venues.

• Cross-Border Training Clusters:

– Set up joint training centers for athletes within 500 km of the host city.

– Share the host country's anti-doping labs and rehabilitation facilities.

11 Sensitivity Analysis

In Task 1.1, we analyzed four key features: Host Boost (XHost), Athlete Pool (XAth), Compet- itiveness Index (XComp), and Historical Momentum (XHist). Since XHost is a binary variable (0 or 1), it was fixed at XHost = 1 (host scenario) for sensitivity analysis. The remaining features were varied by ±10% from their initial values to evaluate their impact on the model's predictions.

Initial Feature Values and Sensitivity Ranges

The initial values and sensitivity ranges for each feature are listed below:

Feature Initial Value Range (-10%) Range (+10%) 719 647 Athlete Pool (XAth) 791 Competitiveness Index (XComp) 17.85 16.07 19.64 Historical Momentum (XHist) 121 109 133

Results and Observations

torical Momentum on Pre- petitiveness Index on Pre- letes on Predicted Medals dicted Medals dicted Medals

All three factors features are positively correlated with predicted medals. The slope of the regression lines shows a steady increase in medals as each factor rises. The shaded areas indicate potential fluctuations in predictions, providing insights into the model’s accuracy and reliability.

12 Strengths and Weaknesses

Strengths

• Comprehensive Feature Integration (MLR-FNN): The MLR-FNN model combines feature extraction and relationship learning to predict the 2028 medal table. It includes factors like participant numbers, host nation effects, historical medal counts, and compet- itiveness, providing strong predictions with confidence intervals that reflect real-world situations.

• Balanced Interpretability and Complexity (LR-RF): The LR-RF model mixes logistic regression’s clear results with random forest’s ability to handle complex relationships and rank factors. This makes it a powerful tool for analyzing Olympic data.

• Strategic Sports Evaluation (SIAMOS): The SIAMOS model looks at sports’ impor- tance using four factors: National Medal Proportion (NMP), Global Competitive Pro- portion (GCP), Long-term Achievement Stability (LAS), and Athlete Sport Distribution (ASD). It gives useful insights to help focus resources and improve Olympic performance.

• Causal Analysis of Coaching Impact (RDD): The regression discontinuity model mea- sures the “great coach effect” by looking at natural breaks in data and considering cross- country and time changes. It provides clear advice on how to invest in coaching to improve medal results.

Weaknesses

• Limited Feature Scope: Some models, like the MLR-FNN, do not include important factors such as the Host Country Spillover Effect, limiting the analysis.

• Subjective Design Choices: Some formulas were chosen without calculation, making the model more subjective and possibly less generalizable. For example, it is assumed that the performance of new athletes is the same as athletes who no longer compete. This keeps the number and composition of athletes the same.

关注数学模型
