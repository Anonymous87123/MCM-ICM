MCM/ICM

Summary Sheet

Summary

Since the inception of the first Olympic Games in history, discussions on predicting the Olympic medal tally have been ongoing. Against this backdrop, we develops an appropriate regression model to predict the medal standings for the 2028 Los Angeles Olympic Games and explores the impact of the "Great Coach Effect" on the performance of countries in Olympic

events.

Firstly, based on the rich data provided in the study, we conducted data preprocessing, including addressing anomalies caused by historical factors and developing models such as SARIMAX and ARIMA to predict future trends in the number of events. Secondly, to handle truncated data, such as countries with "0 medals," this study constructed the TMH-OMP model, which combines the Mundlak-modified Tobit regression model with the Hurdle model. The model achieved a prediction accuracy of 79.3% for countries winning more than 10 medals annually, and 77.8% for countries winning fewer than 10 medals annually. Addi- tionally, we predict that Andorra and the Maldives will win their first-ever Olympic medals, with probabilities of 0.39 and 0.32, respectively. An analysis of event types and project quantity

(participation rate) reveals a Pearson correlation coefficient of 0.416.

In order to analyze the "Great Coach" effect, we constructed a logistic regression model for fitting, and incorporated the Event-study method into the conventional Difference-in-Dif- ferences (DID) approach to design a dynamic DID method capable of effectively estimating the effect across multiple treatment groups. To mitigate the bias due to covariate differences, we included the Inverse Probability Weighting (IPW) method for estimating treatment effects, and applied the Double Robust Estimator (DR) framework to develop the DRD-CE model. Performance analysis of this model showed an R-squared value of 0.756, indicating good fit, and a "Great Coach" regression coefficient of 3.1084, highlighting the substantial impact of the "Great Coach" effect on specific countries and projects. Furthermore, we identified signif- icant effects in countries such as the United States in Women's Sabre Fencing, Japan in Women's Gymnastics, Germany in Women's Sabre Fencing, and Field Hockey.

Subsequently, we observed that changes in the number of smaller events within major categories had a significant impact on the medal outcomes of some smaller countries. Ap- proximately 104 nations are highly dependent on the variety of sports events to secure gold medals. Based on these findings, we proposed to the National Olympic Committees the pro- tection and expansion of their advantageous sports events.

Finally, we assessed and expanded the model's strengths and limitations, as well as ana- lyzed its sensitivity. By conducting error analysis between the total medal count derived from the sum of gold, silver, and bronze medals and the total medal count directly input into the model, we obtained an average error of 8.0783%. This result indicates that our model demonstrates high sensitivity.

bust estimator; Host country effect

2 Assumptions and Justifications.

3Notations

4 Data processing.

5

5 Model 1: Predict Olympic medal counts by TMP-OMP Model... 6

5.1 Explanation of the Dynamic Country Characteristies and Constant Country Properties 6

5.1.1 Dynamic country characteristics .6 .8

5.1.2 Constant country characteristics..

.

●

.8

5.2 The Establishment of Model 1.

.9

5.3 The Solution of Problem 1 by Model 1.

11

5.3.1 Predicting the 2028 Medal Table

11

.12

6 Model 2: Analysis “great coach" effect by DRD-CE Model..

16

6.1 The Establishment of Model 2.

.16

6.2 The Solution of Problem 2 by Model 2.

.18

6.2.1 Illustrate the impact of the great coaching effect .

.18 6.2.2: Selection of three countries and projects, analysis and results. .19 .20 6.2.3: Prediction of the Performance After Hiring a "Great Coach" ● .21

7 The Solution of Problem 3.

.21

7.1 Former host effect and Subsequent host effect.

.22 7.2 Strategies to Enhance Olympic Participation and Global Influence.. 8 Sensitivity Analys... .23 24

9 Model Evaluation and Further Discussion

9.1 Strengths

.24

9.2 Weaknesses and Further Discussion

.25

25

1 Introduction

1.1 Problem Background

The Olympic Games have long captured global attention with their diverse events and elite athletes. Each medal reflects not only an athlete's achievement but also the spirit of their country. As a result, predicting Olympic medal standings has become a focus of interest.

Time series forecasting, a common prediction method, uses historical medal counts to identify trends [1]. However, this approach is limited as it only considers past data and cannot adapt to sudden changes or uncertainties. The empirical model, which relies on real-world data and statistical analysis, also faces challenges, such as focusing mainly on population and GDP, while neglecting other key variables and time-independent factors like sports culture [2].

微信公众号：数学模型 微信号：MATHmodels

1.2 Restatement of the Problem

Based on the background information and restrictions related to the Olympic Games men- tioned in the problem statement, we need to address the following issues:

Problem 1: Medal Prediction Model

Develop a model to predict the gold, silver, bronze, and total medal counts for each coun- try. Evaluate the model's performance using relevant metrics.

2028 LA Olympics Prediction: Forecast medal rankings, identify countries with improved or declined performance compared to 2024, and predict potential first-time medalists.

Event-Medal Relationship: Analyze how the number and types of events influence medal distribution, considering the host country's event choices and their impact on medals.

Problem 2: Great Coach Effect Analysis Evaluate the impact of the "great coach effect" on medal distribution and estimate its con- tribution to the total medal count.

Coach Selection: Identify three countries and recommend which sports they should focus on to hire a "great coach," predicting the potential impact. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Problem 3: Insights from the Model

Present unique insights on medal distribution, highlighting practical recommendations for national Olympic committees.

1.3 Our Work

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

2 Assumptions and Justifications

Assumption 1: This paper assumes that all athletes active after 2020 are at the peak of their athletic performance and will compete in subsequent Olympic Games. Additionally, their performance will be predicted solely based on their medal-winning capabilities.

关注数学模型 Assumption 2: This paper assumes that the number of events in the 2028 and 2032 Olym- pic Games will be determined solely by the host country effect and international trends, without being influenced by other external factors or unforeseen circumstances.

Assumption 3: It is assumed that the achievements of countries undergoing regime changes or other special organizations (such as those competing on behalf of two countries or as independent entities) are reasonably incorporated into the current legitimate countries, based on historical and geographical factors.

3 Notations

The key mathematical notations used in this paper are listed in Table 1.

Description

Symbol

HEi,t Host effect ERi,t Event participation rate APi,t Athletic performance ERi Average Event participation rate NM Normalized Medal Average NAi,t Total country participants Mi,t Number of potential medals (untruncated values) ATH Mi,t Number of medals actually observed

First, we addressed outliers in the dataset, such as formatting errors and missing data, and took into account the impact of special events on the data, such as the cancellation of the Olympics during World War II, justifying the retention of missing values in those years.

We then reviewed the historical context of the Olympics, assessing past events, and con- cluded that they had minimal impact on the overall predictive task. Therefore, we disregarded these effects and proceeded with normal data handling.

Considering global circumstances and political changes, we consolidated the data of the former Soviet Union into Russia and merged East and West Germany into a unified Germany, retaining the results. For countries that emerged after the dissolution of the Soviet Union (e.g., Lithuania, Kazakhstan), we used their respective results.

we provided additional notes on data processing and usage: we combined the results of a country's first and second teams; due to the suspension of Russia and Belarus and the missing data, we did not forecast the medal counts for these two countries; data from mixed teams were excluded from medal predictions; dual-nationality athletes' medals were counted for both countries; and following Assumption 2, we removed data for athletes who competed be- fore 2020 and created a separate new dataset for future use.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Finally, for the other datasets, after encoding the variables, we used the median to fill in outliers and missing values, ensuring the completeness and accuracy of the data. Through these steps, we ensured the data's standardization and consistency, laying a solid foundation for subsequent analysis and modeling.

5 Model 1: Predict Olympic medal counts by TMP-OMP Model.

5.1 Explanation of the Dynamic Country Characteristics and Constant

Country Properties

5.1.1 Dynamic country characteristics

In the context of the Olympic Games, dynamic country characteristics refer to factors that have a significant impact in the short term and change over time. For example, the host country effect (𝑯𝑬), the proportion of events participated in by each country (𝑵𝑬) and athletes’ per- formance in recent Olympic Games ( 𝑨𝑷 𝒊), Number of athlete participants (𝐍𝐀𝐢,𝐭) and so on.

关注数学模型 To construct dynamic national characteristics, we first need to predict the types and quan- tities of future projects for 2028 and 2032. As shown in the figure, considering that the number of future projects is closely related to historical quantities, and project types are often related 微信公众号：数学模型 to the host country, we can divide them into: host country's advantageous projects, disadvanta- geous projects, and neutral projects. For advantageous and disadvantageous projects, we con- sider that the host country effect may lead to an increase in advantageous projects and a de- crease in disadvantageous projects, so we choose the SARIMAX model, which takes into ac- count exogenous variables. Neutral projects are often not affected by the host country effect, so the ARIMA model is used for prediction. In addition, we have used the same method to analyze the host country of 2032, Australia. Where the pie chart in the flowchart shows the percentage of advantaged items in orange, the percentage of neutral items in purple and the percentage of disadvantaged items in blue.

微信号：MATHmodels

These characteristics reflect a country's variations across different Olympic cycles and the temporary performance of its athletes, significantly influencing the prediction of medal counts. Therefore, in the modeling process, we selected 𝑯𝑬𝒊,𝒕 , 𝑬𝑹𝒊,𝒕 and  𝑨𝑷 𝒊,𝒕 as the three dy- namic country characteristics to more accurately capture the immediate impact of country traits on medal outcomes.

Characteristic Equation range of values

Host effect (𝑯𝑬𝒊,𝒕) Based on whether the previous and next sessions 0, 1 were hosted

Event participation Annual projects participated by country i  /An- [0,1] rate (𝑬𝑹𝒊,𝒕) nual total projects×100%

Athletic perfor- Sum of ability scores in the last two editions. [-1,1] mance (𝑨𝑷𝒊,𝒕)

𝐍𝐀𝐢,𝐭 Total country participants

is the host for the predicted Olympic Games, the value is set to 1. For all other countries, the value is 0. The calculation for  𝑨𝑷 𝒊 defines Ability scores as follows: When the prediction task is for gold medals, gold = 3, silver = 2, bronze = 1, and no medal =0. When the prediction task is for silver medals, both gold and bronze = 1，and silver =2. When the prediction task is for bronze medals, gold= 1, silver = 2, and bronze = 3. The total score for all athletes from a country is summed and standardized to obtain the overall athlete performance for that country. It is important to note that, due to age limitations, only the performance from the previous two Olympic Games of each athlete is considered.

5.1.2 Constant country characteristics

In the context of the Olympic Games, constant country characteristics refer to factors that remain relatively stable over long periods and do not fluctuate over time. These include sports of countries traditions, long-term policy support, infrastructure development, and historical strengths in certain events. These factors have a lasting impact on a country’s overall Olympic performance, thus providing long-term guidance for predicting medal counts. In the modeling process, constant country characteristics help us better understand a country’s performance trends across multiple Olympic cycles, rather than just changes within a single cycle. Based on the information provided in the dataset, we selected the country’s long-term event participation rate  𝑵Ē 𝒕, Normalized Medal Average  𝑵𝑴̅̅̅̅̅𝒊, to measure the long-term impact of a country’s sports culture and policies.

Characteristic Equation Range of values

Average Event partici- The sum of 𝑬𝑹𝒊,𝒕/ Number of participants [0,1] pation rate ( 𝑬𝑹̅̅̅̅𝒊)

Normalized Medal Normalized average number of medals [0,1] won Average ( 𝑵𝑴̅̅̅̅̅𝒊)

关注数学模型 The number of times a country participates in the Olympic Games not only reflects its level of engagement but also implies its long-term athletic strength. To quantify this,  𝑵𝑴̅̅̅̅̅𝒊 is calculated by dividing the total number of Olympics a country has participated in by the total number of Olympic Games since the first edition, thereby measuring the country’s sustained involvement in the Olympics throughout history.

5.2 The Establishment of Model 1

微信公众号：数学模型 Inspired by the works of [3,4], we developed the Tobit-Mundlak- Hurdle Olympic

Medal Prediction Model (TMH-OMP) to provide accurate forecasts of Olympic medal

counts. In the dataset, we observed a large number of countries that have yet to win any med- als. To mitigate the impact of data from countries without medals on the predictions for coun- tries with medals, we employed the Tobit regression model to address the truncation issue in medal counts. Meanwhile, recognizing that a country's Olympic performance may be pro- foundly influenced by constant, country-specific factors, we incorporated the Mundlak cor- rection. By adding the time averages of country-specific variables, we capture these time-in- variant effects. Finally, to predict the country that will win a medal for the first time, and the 微信号：MATHmodels probability of winning a medal. Hurdle models for countries are constructed that have histor- ically won fewer than ten total medals.As shown in the figure 5.

Tobit Regression: When predicting Olympic medal counts, the medal count is a non- negative integer and can be zero (i.e., some countries may not win medals in certain events). This leads to truncation issues in traditional regression models. A simple linear regression model assumes the dependent variable is continuous and does not account for the possibility of zero values, leading to inaccurate predictions for countries with no medals. The Tobit re- gression model is specifically designed to handle data issues with truncated or censored de- pendent variables. In this case, the medal count is a truncated variable[3]. The Tobit model introduces latent variables to model the potential score for medal counts, assuming that the medal count can only be observed when the latent score is greater than zero. Based on dy- namic time characteristics such as the host country effect (𝑯𝑬𝒊,𝒕), the proportion of events each country participates in (𝑵𝑬𝒊,𝒕), and athlete performance in recent Olympic Games ( 𝑨𝑷 𝒊), we conduct an initial construction of the Tobit regression model.

∗= 𝛂+ 𝛃𝟏𝐇𝐄𝐢,𝐭+ 𝛃𝟐𝐍𝐄𝐢,𝐭+ 𝛃𝟑 𝐀𝐏 𝐢,𝐭+ 𝛌𝐭+ 𝛜𝐢,𝐭 (1) 𝐌𝐢,𝐭

𝒊 represents different countries, and 𝒕 represents different years. 𝜶 is the constant term, and 𝜷𝟏, 𝜷𝟐, and 𝜷𝟑 are the model coefficients, corresponding to the host country ef- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m fect and the number of events, respectively. 𝝀𝒕 is the time fixed effect, which controls for m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m variations across different years. 𝝐𝒊,𝒕 is the error term. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ∗ ∗> 𝟎 m m m m m m m m m m m m m m 𝐌𝐢,𝐭= {𝐌𝐢,𝐭 𝐢𝐟 𝐌𝐢,𝐭 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (2) ∗≤𝟎 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 𝟎 𝐢𝐟 𝐌𝐢,𝐭

𝑴𝒊,𝒕 represents the actual observed medal count. It is used to estimate the probability of zero medals and accurately predict the number of non-zero medals.

Mundlak Correction: The Olympic performance of many countries may be influenced by constant, country-specific factors, such as hosting the Games multiple times, the long-term average performance of its athletes, and the country's sustained participation in certain events. Failing to account for these time-invariant factors could lead to estimation bias, par- ticularly when handling long-term country characteristics. The Mundlak correction is a technique used to address bias between fixed and random effects by introducing the mean of constant country-specific factors into the model. This allows the model to account for the im- pact of each constant country factor on medal counts. We combine the aforementioned con- stant country factors, long-term event participation rate ( 𝑬𝑹̅̅̅̅𝒊), and Normalized Medal Average ( 𝑵𝑴̅̅̅̅̅𝒊), with the Mundlak correction.

∗= 𝜶+ 𝜷𝟏𝑯𝑬𝒊,𝒕+ 𝜷𝟐𝑵𝑬𝒊,𝒕+ 𝜷𝟑 𝑨𝑷 𝒊,𝒕+ 𝒅𝟏 𝑬𝑹̅̅̅̅𝒊 + 𝒅𝟐 𝑵𝑴̅̅̅̅̅𝒊+ 𝝀𝒕+ 𝝐𝒊,𝒕 (3) 𝑴𝒊,𝒕

𝒅𝟏 and 𝒅𝟐 are the coefficients for the mean variables, representing the influence of long-term event participation rate and normalized medal average on medal counts, respec- tively. By introducing these time-invariant constant factors, the Mundlak correction effec- tively adjusts the model, providing more accurate medal predictions.

The Hurdle model typically consists of two stages: Step 1: Determining zero versus non-zero values: A binary choice model is used to predict whether an observation is zero. This stage focuses on whether the event occurs, i.e., whether the "hurdle" is crossed. Step 2: Quantifying non-zero values: For non-zero observations, an appropriate distribution is used to model the magnitude of these values. This part focuses on the quantity or degree of the obser- vation once the event has occurred. For the task of predicting first-time medalists, we devel- oped the following formula.

关注数学模型 (4) P(Mi,t > 0) = φ(Xi,tΘ + ui + ∈i,t)

To allow more countries that have never won a medal to cross the "hurdle", we predict that a country will win a medal in a given Olympics if P(Mi,t > 0) > 0.3. Φ is the cumu- lative distribution function (CDF) of the standard normal distribution, mapping the results of a linear combination to the [0, 1] interval, representing the probability that a country will win a medal. Xi,t is the matrix of explanatory variables for country i in year t. Θ is the regres- sion coefficient, representing the impact of each variable on the likelihood of winning a medal. ui is the country-specific effect, typically assumed to follow a normal distribution. €,t is the error term, usually assumed to be normally distributed. The definition of X,tΘ is as follows:

(5) exp (α + β1HEi,t + β2NEi,t + β3APi,t +t+ vNA,t + λt + ∈i,t)

Since the main goal of the Hurdle model is to predict first-time medal winners, we focus more on fitting countries that have won few medals in previous years, as this relationship is difficult to capture using linear models. Therefore, we employ Poisson regression. We also found that for countries with no medals, their athletes' performance APi,t is zero, and their participation rate NEi,t is extremely low. As a result, we introduce the number of participants each year NAi,t as a new variable. v is the coefficient for NAi,t.

In summary, the Mundlak-modified Tobit regression model helps mitigate the impact of non-medal-winning countries on predictions for medal-winning countries, while improving the accuracy of medal predictions for countries that haye won. The Hurdle model expands the study by identifying countries likely to win their first medal, accurately predicting those breaking the "zero medal" barrier. Although it slightly affects predictions for medal-winning countries, its main advantage lies in forecasting potential breakthroughs. Combining Tobit and Hurdle models allows for accurate predictions for both existing medal winners and emerging countries. Finally, Particle Swarm Optimization (PSO) is used to optimize pre- dictions for truncated data, commonly applied in economics and social sciences.

● ●

5.3 The Solution of Problem 1 by Model 1.

5.3.1 Predicting the 2028 Medal Table

Prior to the 2028 medal table, we used the existing data to predict the medal count for the 2024 Paris Olympics in order to evaluate the accuracy of our model. Due to the limitations of table space, and given that countries winning their first medals typically struggle to secure gold, we focus on analyzing and evaluating the total medal count for each country, rather than the specific breakdown of gold, silver, and bronze. It is worth noting that, for the athlete per- formance indicator (APi,t), all medals (gold, silver, and bronze) are assigned a score of 1 point.

Hurble Tobit Mundlak Actual Upper CI Upper CI Lower CI Forecast Lower CI Forecast number Countries 126 130 138 121 117 126 122 United States 91 94 90 97 90 87 83 China 63 65 66 72 62 59 67 Korea 57 69 64 62 58 61 65 France 50 47 53 57 50 59 54 Australia 43 41 45 46 53 46 51 Japan Italy 40 47 42 51 44 42 46 35 32 32 34 34 39 30 Netherlands 28 33 29 35 29 Germany 32 38 28 32 30 34 29 28 38 Great Britain Accuracy of Hurble Accuracy of Tobit Mundlak 72.9% 63.3% All countries (+ or -3) Countries with at least 79.3% 41.9% 10 medal (+ or -3) Countries with Less 62.9% 77.8% than 10 medal(+ or -1) 0% 37.5% First-time medalists

Overall Accuracy: The Tobit Mundlak model achieved an accuracy of 72.9% in pre- dicting medal counts within a margin of ±3 medals for all countries, outperforming the Hur- dle model's accuracy of 63.3%. This indicates that the Tobit Mundlak model provides more stable performance overall.

Countries with at least 10 medals: For countries winning at least 10 medals, the Tobit Mundlak model achieved an accuracy of 79.3%, significantly higher than the Hurdle model. This highlights the Tobit Mundlak model's predictive advantage for countries with medium to large medal counts. Countries with fewer than 10 medals: In countries with fewer than 10 medals, the Hurdle model's accuracy of 62.9% was higher than that of the Tobit Mundlak model. This suggests that the Hurdle model performs better for countries with smaller medal counts. Countries winning medals for the first time: For countries winning medals for the first time, the Tobit Mundlak model had an accuracy of 0%, whereas the Hurdle model achieved an accuracy of 37.5%. Of the eight countries predicted by the Hurdle model to win their first medals, three actually did. This indicates that the Hurdle model has some advantage in predicting first-time medal winners.

We combined the predictions from both the Tobit Mundlak and Hurdle models for countries with at least 10 medals and those with fewer than 10 medals. We predicted the gold, silver, and bronze medal counts separately, then summed the results to obtain the total medal count. The final rankings were determined according to the Olympic ranking rules.

关注数学模型 微信公众号：数学模型 微信号：MATHmodels

The grey numbers in the graph represent the intervals in which the number of medals is predicted. According to the analysis, the top two positions (USA and China) remained stable. However, Canada and the United Kingdom saw significant improvements in their rankings, rising to third and fourth, respectively. Although their total medal counts may still be lower than some other traditional powerhouses, this shift likely reflects notable progress by Canada and the UK in events with strengths similar to those of the United States. Specifically, these countries increased their participation in these events, boosting their gold medal counts. As a result, they surpassed several countries with higher total medal counts and secured higher po- sitions in the rankings. On the other hand, France's ranking declined, suggesting that the ad- vantage it gained from the host nation effect has almost diminished.

5.3.2 Visualizing the progress of countries in the Olympics

The bar chart below visually presents the predicted medal counts for each country based on the applied forecasting model, while the heatmap below reveals the dynamic changes in Olympic medal performance across countries. The deep red regions indicate countries that have withdrawn from the Olympics for specific reasons, such as Russia and Belarus. The var- iation in other colors reflects the trend of changes in medal performance: the closer the color is to red, the more significant the progress indicated by the prediction; conversely, the closer the color is to blue, the more it suggests a decline in the country's predicted performance. No- tably, the yellow-green regions on the heatmap highlight countries predicted to win medals for the first time, such as the Maldives and Andorra, with predicted probabilities of 0.32 and 0.39, respectively.

These countries may achieve their first medals due to emerging potential in certain sports (e.g., swimming, athletics) that are similar to events where the United States excels, thereby increasing their participation rate and number of athletes, which in turn enhances the likeli- hood of winning medals. From the chart, it can be observed that most countries in Africa, South America, and Europe are facing a trend of decline, suggesting that these regions may struggle to maintain or improve their medal performances in future Olympic Games. In con- trast, countries in North America generally show a significant upward trend. Progress in other continents is more scattered, with no clear regional clustering of improvements.5.3.3：Ana- lyzing event relevance and giving advice.

To analyze the contribution of individual sports to a country's total medal count, we in- troduce the Sport Contribution Score (SCS). This indicator quantifies the impact of each country's performance in different Olympic events on its overall medal tally. The formula is as follows:

∑ 𝒄𝒐𝒖𝒏𝒕𝒎,𝒊,𝒔× 𝒔𝒄𝒐𝒓𝒆𝒎 𝒎∈𝑴 (6) 𝒔𝒄𝒔𝒊,𝒔= 𝒄𝒐𝒖𝒏𝒕𝒎,𝒊,𝒔′ × 𝒔𝒄𝒐𝒓𝒆𝒎 ∑ ∑ 𝒔 ∈𝑺 𝒎∈𝑴

关注数学模型 𝒔𝒄𝒔𝒊,𝒔 represents the contribution score of country i in sport s. M includes gold, silver, and bronze medals，𝒄𝒐𝒖𝒏𝒕𝒎,𝒊,𝒔 refers to the number of medals won by country i in sport s. 𝒔𝒄𝒐𝒓𝒆𝒎 denotes the score assigned to each type of medal in event m. Consistent with the previous definitions, the scores for gold, silver, and bronze medals are 3, 2, and 1, respec- tively. However, unlike before, not winning any medals counts as 0. 𝒔′ represents all events, and 𝒄𝒐𝒖𝒏𝒕𝒎,𝒊,𝒔′is the total number of medals won by country i across all events. The SCS score reflects the impact of each sport on the country's total medal count; a value close to 1 indicates a significant contribution, while a lower value suggests a smaller impact. Specifi- 微信公众号：数学模型 cally, the SCS value for the sport with the highest medal proportion for a country reflects that sport’s dominant impact on the country's overall medal performance. The pseudo-code is as follows：

Algorithm 1 Calculate the contribution of Sport Contribution Score

For each country i in the countries of dataset: For each sport category s in the sport categories of dataset: medals_s = Get all medal data for sport category s in country c total_score_s = 0 For each medal type m in {Gold, Silver, Bronze}: 微信号：MATHmodels count_m_s = Number of medals of type m in sport category s for country c total_score_s += count_m_s * (Gold if m = Gold, Silver if m = Silver, Bronze if m = Bronze) sport_contributions[c, s] = total_score_s / total_scores[c] Return sport_contributions

Across countries, the highest SCS value represents the degree of influence from that par- ticular sport. For example, if a country’s highest SCS corresponds to water sports, a reduction in water sports events at the Olympics would significantly affect that country's medal count. Thus, the SCS of the sport with the highest medal proportion in each country represents the impact of that sport on the country's medal performance. After calculating the SCS for all sports, the sport with the highest SCS for each country is selected for further analysis.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Effects of sport types: The x-axis represents 206 countries which participate the Olympics, and the y-axis represents the SCS score. A score of 0 indicates countries with no medals, while lower scores suggest that countries are more susceptible to the influence of event types. Countries least affected by this influence include China, Russia, and the United States, while countries most affected include the Niger, and Togo. In this part Niger and Togo are very susceptible to track and field events. More details are shown in problem 3.

Effects of event number：The participation rate reflects the number of events a country par- ticipates in at each Olympic Games. Therefore, we conducted a Pearson correlation analysis on the two models we developed and averaged the resulting coefficients. As shown in the confusion matrix below, there is a significant positive correlation between the event participa- tion rate and the total medal count, with a correlation coefficient of approximately 0.416. This indicates that the event participation rate significantly contributes to the growth of a country's medal count, with a notable positive impact. It suggests that a country's active participation in more events may increase its chances, and the total number of medals won.

6 Model 2: Analysis “great coach” effect by DRD-CE Model.

The "Great Coach Effect" can be defined as the phenomenon where a coach signifi- cantly improves an athlete's performance through exceptional expertise, tactical guidance, and motivational methods, leading the team to achieve outstanding results in international competitions. Inspired by the work of [4,5,6], a great coach's impact can be compared to a significant policy change in a country's sports programs. Therefore, mathematical models used to analyze policy changes, such as the Difference-in-Differences (DID) method and dy- namic panel data models, are appropriate choices for this analysis. This study combines the Difference-in-Differences (DID) method with a double robust estimator to construct a spe- cialized model for analyzing the "Great Coach Effect." This model is referred to as the Du- rable Robust Coach Effect Model (DRD-CE Model).

6.1 The Establishment of Model 2

Dynamic Difference-in-Differences (DID): The standard DID method typically as- sumes a comparison between treatment and control groups at two time points. However, when treatment occurs at different time points across multiple groups (i.e., different countries or regions receiving treatment at different times), the standard DID method may fail to accu- rately capture the treatment effect. The "Great Coach Effect" typically occurs at different time points. To address this challenge, we designed a dynamic DID method by incorporating an event-study approach. This allows us to effectively estimate the "Great Coach Effect" across multiple time periods and treatment groups, even when each group experiences treat- ment at different times. The formula is as follows:

关注数学模型 𝑲 (7) ⋅ 𝑷𝑪 𝒊𝒕+𝒌+ 𝜸⋅𝑿𝒊+ 𝜹⋅ 𝒀 𝒕+ 𝝐𝒊𝒕 𝑴𝒊,𝒕= 𝜶+ ∑𝜷𝒌 𝒌=−𝑲 𝑷𝑪 𝒊𝒕+𝒌 is a binary variable indicating whether country i experienced a coach change at time t. If a coach change occurred at time t, then  𝑷𝒐𝒔𝒕𝑪𝒐𝒂𝒄𝒉 𝒊𝒕+𝒌= 𝟏; otherwise, it is 0. 𝑿𝒊 represents country i's covariates, which include dynamic national characteristics such as Host Effect (𝑯𝑬), participation ratio in events (𝑵𝑬) and athlete performance in recent Olym- pics( 𝑨𝑷 𝒊).  𝒀 𝒕 represents constant national characteristics, including long-term project par- ticipation rate( 𝑵Ē 𝒕) and Normalized Medal Average( 𝑵𝑴̅̅̅̅̅𝒊).

Inverse Probability Weighting (IPW): The IPW method estimates treatment effects by 微信公众号：数学模型 weighting each individual's probability of receiving treatment. These weights are calculated based on the likelihood of receiving treatment, helping to correct for bias caused by imbal- anced covariates. By using weighted samples, IPW ensures that treatment effects between different groups are comparable, thus avoiding bias caused by differences in covariates.

𝑵 𝑵 𝑰𝑷𝑾= 𝟏 𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) ⋅𝑴𝒊,𝒕] −𝟏 𝑷𝑪𝒊𝒕 𝟏−𝑷𝑪𝒊𝒕 ^ (8) 𝟏−𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) ⋅𝑴𝒊,𝒕] 𝝉 𝑵∑[ 𝑵∑[ 𝒊=𝟏 𝒊=𝟏 ^ represents the treatment effect, which reflects the causal impact of an intervention (e.g., 𝝉 微信号：MATHmodels coach impact) on an outcome (e.g., Olympic medal count). 𝑷(𝑮𝒊𝒕∣𝑿𝒊) is the probability that 𝑮𝒊𝒕 𝟏−𝑮𝒊𝒕 country i receives a great coach at time t, based on the covariates . 𝑷(𝑮𝒊𝒕∣𝑿𝒊) and 𝟏−𝑷(𝑮𝒊𝒕∣𝑿𝒊) are the weighting factors for each country, indicating the weighted probabilities for the treatment and control groups, respectively. 𝑷(𝑮𝒊𝒕∣𝑿𝒊) is predicted using logistic regression based on the covariates, and the simplified formula is as follows:

𝟏 𝟏+ 𝐞𝐱𝐩 (−(𝒄𝒕+ 𝒅𝑿𝒊)) (9) 𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) =

𝒄𝒕 is the time fixed effect at time t, representing the time effect of the treatment. d is the regression coefficient of covariates 𝑿𝒊, indicating the influence of covariates on the probability of treatment.

Double Robust Estimator: The double robust estimator combines the advantages of outcome regression and inverse probability weighting. It estimates treatment effects by simul- taneously using a regression model for covariates and a weighted model for treatment proba- bilities. The double robust estimator provides consistent estimates as long as at least one of the estimation methods is correctly specified.

𝑵 𝑫𝑹= 𝟏 𝑷𝑪𝒊𝒕 ^ ^(𝑿𝒊)) + 𝝁 ^(𝑿𝒊)] 𝝉 𝑵∑[ 𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) ⋅(𝑴𝒊𝒕−𝝁 𝒊=𝟏

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 𝑵 −𝟏 𝟏−𝑮𝒊𝒕 ^(𝑿𝒊)) + 𝝁 ^(𝑿𝒊)] 𝑵∑[ 𝟏−𝑷(𝑷𝑪𝒊𝒕∣𝑿𝒊) ⋅(𝑴𝒊𝒕−𝝁 (10) 𝒊=𝟏

^(𝑿𝒊) represents the predicted outcome for country i’s covariates 𝑿𝒊, which reflects the 𝝁 counterfactual or untreated potential outcome. The double robust estimator provides dual pro- tection: it controls covariates through regression on one hand and adjusts for covariate imbal- ances using weights on the other. Therefore, even if one model (regression or weighting) has errors, the other model ensures consistent estimation.

In summary, this model, tailored to the context of the Olympics, overcomes the limitations of traditional Difference-in-Differences (DID) methods—such as self-selection bias, covariate imbalance, and omitted variable bias—by integrating inverse probability weighting (IPW) and the double robust estimator (DR). IPW adjusts for covariate differences between treat- ment and control groups by applying weights to each individual, reducing bias. On the other hand, DR combines weighting and regression models to ensure that, even if one model is mis specified, the other can still provide consistent estimates.

6.2 The Solution of Problem 2 by Model 2

6.2.1 Illustrate the impact of the great coaching effect

Initially, we visualized the "summerOly_athletes.csv" dataset and identified certain pe- riods where countries experienced a sharp increase in medal counts for specific events. This raised the hypothesis that the "great coach effect" might have influenced these periods. Sub- sequently, we examined the history of "great coaches" in these events and their corresponding coaching tenures as a background, to assess whether these periods overlapped with the identi- fied increases in medal counts.

We identified several instances in the dataset, such as the Japanese men's saber team, which, after the introduction of "great coach" Erwan Le Pechoux in 2021, saw a remarkable performance improvement, rising from no medals to winning gold in 2024. Additionally, we analyzed three other representative cases: the U.S. women's gymnastics medal data from 1984 to 1996, China's women's field hockey data from 2008 to 2024, and China's women's epee data from 2000 to 2016. In all these cases, the introduction of a "great coach" during the respective periods led to noticeable changes in medal counts. In this context, we extracted the medal data of athletes from the corresponding events during the significant periods of change, where a "great coach" was involved, from the dataset. We then applied the "DRD-CE" model to analyze these data. After testing the relevant model parameters, we confirmed the existence of the "great coach effect".

As shown in Table 4, the coefficients of 𝑷𝑪𝒊𝒕 and 𝑷𝑪𝒊𝒕+𝟏 are significantly positive, in- dicating that after the appointment of a new coach, the country's medal count shows a signifi- cant increase during the current and next Olympic cycle. The estimated coefficient of 𝑷𝑪𝒊𝒕−𝟏 is positive but does not reach significance, which may suggest that the effect of medal count improvement after the coach change has not fully manifested in the previous cycle (or imme-

关注数学模型 diately after the coach's appointment). Other covariates, such as the home advantage, compe- tition depth, and recent performance, are positively correlated with the increase in medal counts, which aligns with the expected results.  From Table 5, it can be observed that the model fits well, with an R-squared value of 0.756, indicating that the model explains most of the variation in the dependent variable. The F-statistic and the corresponding p-value suggest that the model is overall significant. The AIC and BIC values indicate that the model strikes a good balance

微信公众号：数学模型 微信号：MATHmodels between complexity and fit. The Durbin-Watson value is close to 2, suggesting that there is no significant autocorrelation in the model's residuals. As shown in Table 6, using the doubly robust estimation method, the effect estimates of the "Great Coach Effect" becomes more sig- nificant. In contrast, using the traditional (simple) DID method alone may underestimate the effect or result in insignificant effect estimates due to sample imbalance.

6.2.2：Selection of three countries and projects, analysis and results

We ultimately selected Japan, Germany, and the United States for analysis, and identi- fied the corresponding projects where investment in "great coaches" could be beneficial. Spe- cifically, Japan could invest in women's gymnastics etc, the United States in women's epee etc, and Germany in women's field hockey and women's epee etc. We recommend that these countries invest in hiring "great coaches" for these specific events to improve their medal counts. The analysis is as follows:

In terms of country and event selection, we first consider the overall economic strength. We focus only on developed countries and developing countries with the financial capacity to support the costs associated with hiring "great coaches."  Furthermore, using this data, we identify countries in the past three Olympic Games whose rankings in the event were similar to those of the coached country prior to the coach’s involvement. To ensure that the data used for predictions is sufficiently broad and that the "great coach effect" is clearly evident, we selected eight sports with a large number of events or high popularity (e.g., volleyball). Using the aforementioned method, we narrowed the scope to eight countries—Japan, Italy, France, the United Kingdom, Germany, the United States, and China—that can be linked to five spe- cific events: women’s volleyball, men’s saber, women’s gymnastics, women’s epee, and women’s field hockey. We also identified the corresponding "great coaches" for these events, such as Daniel Levavasseur, the coach of China’s women’s epee team who had a notable "great coach effect," and Alyson Annan, the coach of the Netherlands women’s field hockey team. This ensures the relevance and credibility of our results.

6.2.3：Prediction of the Performance After Hiring a "Great Coach"

Based on our analysis of the identified events and the coaching tenures of historically successful "great coaches," we found that significant improvements typically occur within a coaching period of four to eight years, which coincides with the Olympic cycle. Therefore, we focused on the subsequent two Olympic Games. According to the results derived from the DRD-CE model, if these three countries introduce the respective "great coaches" for the iden- tified events and undergo a similar coaching period, the performance (expected outcome) in these events is expected to show a noticeable improvement. In the end, it turns out that in their

关注数学模型 corresponding events in 2028 and 2032, respectively, the U.S. and Germany are likely to achieve silver, while Japan is expected to win gold.

7 The Solution of Problem 3

7.1 Former host effect and Subsequent host effect.

In the previous experiments, we identified the "former host effect" and the "subsequent 微信公众号：数学模型 host effect." The "former host effect" refers to the phenomenon where a country, upon learn- ing that it will host the upcoming Olympic Games, performs above its average level in the subsequent Olympic Games until the country hosts its own Olympic Games. The "subsequent host effect" refers to the significant decline in the host country's performance in the following Olympic Games, indicating that the competitive sports strength not only reverts from the "home advantage" to the normal level, but may also drop one or more levels below the nor- mal level. For example, in our previous prediction, Japan, as the host of the 2021 Olympic Games, showed an improvement in performance during the 2016 Rio Olympics. Similarly, as the host of the 2024 Olympics, France experienced a certain degree of performance decline in 微信号：MATHmodels the 2028 Olympic Games.

Therefore, in constructing the model, we introduced two new variables,  BE i,t, AF i,t , which represent the impact of the former host effect and the subsequent host effect on the pre- diction results, respectively, and developed a new model.

∗= 𝜶+ 𝜷𝟏𝑯𝑬𝒊,𝒕+ 𝜷𝟐𝑵𝑬𝒊,𝒕+ 𝜷𝟑𝑨𝑷𝒊,𝒕+ 𝜷𝟒 𝑩𝑬 𝒊,𝒕+ 𝜷𝟓𝑨𝑭𝒊,𝒕 𝑴𝒊,𝒕 (11) + 𝒅𝟏 𝑬𝑹̅̅̅̅𝒊 + 𝒅𝟐 𝑵𝑴̅̅̅̅̅𝒊+ 𝝀𝒕+ 𝝐𝒊,𝒕

For BE i,t, since countries typically know whether they will host the Olympic Games one cycle in advance (on average, 7 years), this variable only impacts the previous Olympic Games. Therefore, we set the value of this variable to 1 if it applies, and 0 if it does not.

𝑩𝑭 𝒊,𝒕= {𝟎,    (𝐢𝐬 𝐧𝐨𝐭  𝐭𝐡𝐞 𝐡𝐨𝐬𝐭 𝐨𝐟 𝐭𝐡𝐞 𝐧𝐞𝐱𝐭 𝐆𝐚𝐦𝐞𝐬) (12) 𝟏,    (𝐢𝐬 𝐭𝐡𝐞 𝐡𝐨𝐬𝐭 𝐨𝐟 𝐭𝐡𝐞 𝐧𝐞𝐱𝐭 𝐆𝐚𝐦𝐞𝐬)

For  AF i,t, we introduced a "decay factor" to quantify its impact on the subsequent Olym- pic Games after a country becomes the host. The definition is as follows:

𝑨𝑭 𝒊,𝒕= 𝐌𝐢,𝐭+𝛍−𝐌𝐢,𝐭 × 𝛅𝛍     (𝛍= 𝟏, 𝟐, 𝟑) (13) 𝐌𝐢,𝐭

In this context,𝛅𝛍 represents the decay factor for the μ-th Olympic Games after a country becomes the host, with decreasing values𝜹𝟏= 𝟏 𝜹𝝁= 𝟎. 𝟔  𝜹𝝁= 𝟎. 𝟑 indicating that the per- formance gradually declines in subsequent Olympic Games.After constructing the model, we applied it to predict the results using our original data. We found that, in our prediction for the 2028 Olympic Games, Australia's total medal count increased from the original 45 to 66, which is higher than the 53 medals predicted for the 2024 Paris Olympics. This result further validates the rationale behind the "former host effect" and similar effects from another perspective.

7.2 Strategies to Enhance Olympic Participation and Global Influence.

Using the above method in section 1.3. We derived the most dominant sports for each country along with their respective SCS. The study finds that the fewer the medals, the higher the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m SCS may be. Based on the values of the sport_contribution_score, we categorize countries m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m into groups: Sporting Power Nation (0, 0.25): These countries typically have more than 4 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m dominant sports, indicating strong performance across multiple events with stable overall per- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m formance. Sports Middle-tier Nation [0.25, 0.75): These nations excel in some sports but m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

lack consistent competitiveness, resulting in a balanced performance influenced by multiple events. Sports Lagging Nation [0.75, 1]: These countries have a higher SCS, with medals concentrated in a few sports, leading to more specialized performance and weaker overall re- sults. Sports Emerging Nation (0): These countries have an SCS of 0, indicating a lack of significant medal-winning potential and being in the early stages of sports development with limited capacity to compete internationally.To promote the participation of Sports Emerging Nations and Sports Lagging Nations in the Olympics and enhance the global influence of the Games, we propose the following two recommendations to the organizers:

Protection of Advantageous Events: For Sports Lagging Nations, we suggest preserving their advantages in specific events and ensuring these countries have more opportunities to participate in those events. By protecting these countries' strong events, their medal perfor- mance can be improved, encouraging more investment in their areas of strength and enhanc- ing overall competitiveness.

Addition or Expansion of Events: Based on the traditional strengths and potential of Sports Emerging Nations and Sports Lagging Nations, we recommend adding new Olympic events or increasing the number of entries for these countries in existing events. This would allow

关注数学模型 these nations to showcase their advantages in more fields, providing more opportunities for medal contention and motivating more athletes to participate in the Games.

微信公众号：数学模型 微信号：MATHmodels Figure 11．Classification of countries and recommendations.

8 Sensitivity Analysis

The content you described is primarily intended to test the sensitivity of the model and to ver- ify its accuracy and stability by comparing the medal predictions with different weight set- tings. Here is a more professional expression:In solving Question 1, for the calculation of the total number of medals, we first calculated the number of gold, silver, and bronze medals sep- arately using the TMP-OMP model, and then summed these to obtain the total number of medals. To further validate the model's sensitivity, we could set the weights for gold, silver, and bronze to 1 and re-run the model to obtain a new total medal count. We then compare the two methods to test the model's sensitivity to changes in medal weights.

Taking the United States as an example, in the solution to Question 1, we obtained the num- ber of gold medals as 51, silver medals as 50, and bronze medals as 47, resulting in a total of 148 medals. After performing the sensitivity test by setting the weights for all medal types to 1, the recalculated total number of medals for the United States was 142, with an error of 4.054% (compared to the original result of 148 medals). This error indicates that the model has a high sensitivity to changes in medal weights, and the results remain relatively stable, suggesting that the model performs well in predicting total medal counts. To further verify the

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m stability of the model, we conducted a sensitivity analysis for the top 10 countries. The re- sults showed that the error values for all countries were less than 0.16, indicating that the

model has high prediction accuracy for different countries, with a small error range, demon- strating good stability and reliability. The final results, as shown in the following chart, fur- ther validate the model's accuracy and sensitivity under different weight settings.

9 Model Evaluation and Further Discussion

9.1 Strengths

The Advantages of Two Model:

⚫ Medal Censoring Handling: The Tobit regression is used to address the censoring prob- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m lem of countries with zero medal counts, improving prediction accuracy for nations with- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m out medals. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ⚫ Control of Country-Specific Effects: The Mundlak correction is applied, integrating m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m long-term country features (such as host nation effects, participation rate, average medal m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

count, etc.) to effectively control for time-invariant country characteristics and enhance prediction accuracy. ⚫

Double Robust Estimation (DR): Combines regression and weighting models to pro-

vide consistent estimates even if one model is misspecified, enhancing the model's relia- bility. ⚫ Flexibility: The dynamic DID approach accommodates varying time points and multiple treatment groups, making the analysis both precise and widely applicable.

关注数学模型

9.2 Weaknesses and Further Discussion

⚫ While the current model’s accuracy can still be improved, future efforts could focus on incorporating additional country-level data, such as population size and GDP. These macroeconomic indicators can provide a more comprehensive understanding of a na- tion's overall strength and its potential impact on Olympic medal performance, thereby 微信公众号：数学模型 improving prediction accuracy. ⚫ The model currently relies on medal counts to evaluate athlete performance and predict future medal outcomes. To better assess athletes' true performance, future data collection should focus on athletes in the top 16, which will allow for a more nuanced analysis of their capabilities and provide more professional insights for medal predictions.
