MCM/ICM

Summary Sheet

Summary

The Olympics have always been a topic of great interest. With the 2028 Summer Olympics set to take place in Los Angeles, there is much anticipation not only for the exciting competitions but also for which countries will achieve success or experience setbacks in the medal standings. Meanwhile, a greater and more intriguing challenge has emerged: utilizing information from past Olympics to predict future Olympic medal outcomes. This is the primary question we address in this paper.

To establish a reasonable model, our first task is to develop an appropriate model for national medal counts. We built a bottom-up medal analysis and prediction model using the TrueSkill-SARIMAX- RF method. For traditional events, the TrueSkill model is used to evaluate a country’s performance in each event. Then, the SARIMAX model is applied to predict the country’s performance level for

2028. The host country factor was considered in this step. To account for potential errors, a Bayesian prediction method is employed. Finally, the predicted performance for 2028 determines the medal allocation. The results from these two parts of events are aggregated to form the final medal count model for each country.

For Task 1, using our model, we predicted medal winners for each event. Based on our simu- lated medal table, we also predicted which countries are most likely to show the greatest decline or improvement. Our model then address the second major question in Task 1: predicting medal-winning probabilities for countries that have never won medals. Through rigorous probability analysis, we con- cluded that in 2028, there is a 0.25 probability that 2 countries without previous medals will win their first medals. Regarding the third question in Task 1, since we derived overall national medal outcomes from event-level predictions, we aggregate event performance predictions to determine which sports are most crucial for each country. Finally, we analyzed the host country’s newly chosen events and various countries’ medal performances, discovering that host countries have higher chances of winning medals in home competitions and newly selected events.

For Task 2, we performed residual analysis to find evidence of how coaches influence athletes’ performance and medal counts. By analyzing different variables, we identified anomaly information in the data, providing evidence of how the possible “great coach” effect alters the data. Subsequently, we introduced LR-SCAD model to study how the “great coach” effect contributed to changes in the total medal count for different countries and created visualizations for this. Finally, we selected USA NOC , SWE NOC , and CHN NOC and identified the sports in which these countries should invest in a great coach. We then evaluated the impact of the great coach on their medal counts.

For Task 3, based on the model, we analyzed and derived 2 factors that affect a country’s medal count, which were not covered in Tasks 1 and 2. We found that countries without previous medals should introduce coaches in events with higher winning probabilities to significantly increase their chances of success. Additionally, we discovered that the proportion of experienced athletes in a team affects medal-winning probabilities.

Lastly, we conducted sensitivity analysis on our model, finding that it demonstrates strong gener- alizability across different datasets, proving its robustness.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Introduction

3 1 3 1.1 Problem Background 模 1.2

Restatement of The Problem

3 1.3 4 Our Work

5

Assumptions

2

Notations

5 3

Data Preprocessing 6 4

Medal Projection Model

6 5 5.1

TrueSkill Sports Performance Evaluation Model

7 5.2

SARIMAX-Bayesian Model: Predicting Future Medals

8 5.3

Random Forest Model: Predicting Medals in New Events

10 5.4

Model Aggregation

11 IIm0c 5.5 11 Model Evaluation

Task 1: Medal Prediction and Analysis for the 2028 Olympics 12 6 Medal Table Projections 12 6.1 6.2 First Ever Medal 13 14 6.3 Task 1.3

Task 2: Great Coach Effect 16 7 16 Residuals Test: Evidence of Changes That Might Be Due to Great Coach Effect 7.1 LR-SCAD: Estimate Great Coach Effect Contributes To Medal Counts 7.2 18 Choose three countries and identify sports where they should consider investing in a 7.3 “great" coach and estimate that impact 19

TASK 3: Oringinal Insights 20 8 20 8.1 Insights and Recommendations for Countries That Have Never Won Medals Insights and Advice for NOCs on Deploying Experienced Athletes 8.2 21

22 Model Evaluation 9

10 Sensitivity Analysis

23

11 Conclusion

24

25

关注数学模型

1 Introduction

1.1 Problem Background

The Olympics have always been a topic of great interest. With the 2028 Summer Olympics set to take place in Los Angeles, there is much anticipation not only for the exciting competitions but also for which countries will achieve success or experience setbacks in the medal standings, as well as whether 微信公众号：数学模型 countries that have never won medals will secure their first one. Also, predicting the medal counts for the United States in the 2028 Olympics, as the host nation, is an exciting and dynamic challenge.

微信号：MATHmodels

1.2 Restatement of The Problem

We have divided the entire problem into three main tasks:

Task1: Medal Prediction and Analysis for the 2028 Olympics For Task 1, the following objectives must be accomplished: Build a model to represent and predict the medal counts for each country, including gold medals and total medals, while evaluating the model’s accuracy and performance. Once the model is constructed, the subsequent tasks based on its outputs must be completed:

• Predict the medal table for the 2028 Los Angeles Olympics and obtain prediction intervals.

Identify the countries most likely to improve or decline in the medal table according to our predictions.

• Predict how many countries that have never won a medal in the Olympics will win medals in the 2028 Los Angeles Olympics, along with the probability of this occurrence.

• Identify the most important sports for different countries, provide reasons, and analyze how the events chosen by the host country influence the gold and total medal counts of various countries.

Task 2 The Impact of the “Great Coach” Effect For Task 2, the study of the “great coach” effect is required. First, evidence needs to be found showing how the “great coach” effect changes the data. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Then, analyze the contribution of the “great coach” effect to changes in the total medal count. Lastly, select three countries, identify which sports they should invest in a “great” coach, and assess the impact on their medal counts.

Task 3 Exploring Strategic Insights For Task 3, additional insights need to be derived from the model, and these insights must be explained in a way that they can provide useful reference for the national Olympic committees.

1.3 Our Work

For Task 1, we built a bottom-up medal projection model using the TrueSkill-SARIMAX-RF method. The model first categorizes all events into traditional events and new events. For traditional events, the TrueSkill-SARIMAX model is applied to predict the country’s performance level for 2028. To account for potential errors, a Bayesian prediction method is employed. The model determines the allocation of medals based on the predicted performance rankings. For new events, a Random Forest model is used to predict medal allocation. The results from these two parts are aggregated to form the final medal count model for each country. We used the model to predict and analyze all the issues mentioned in the statement of the problem, and provided an analysis of the model’s accuracy.

For Task 2, we performed residual analysis. By analyzing different variables, we identified outliers in the data, providing evidence of how the “great coach” effect alters the data. Subsequently, we studied how the “great coach” effect contributed to changes in the total medal count for different countries and created visualizations for this. Finally, we selected USA, CHN and SWE to identify the sports in which these countries should invest in a “great” coach. We then evaluated the impact of the “great” coach on their medal counts.

关注数学模型 For Task 3, Based on the model, we analyzed and identified several factors that affect a country’s medal count, which were not covered in Tasks 1 and 2. These factors were then integrated into insights, and based on these insights, we provided recommendations for the concerned national Olympic committees.

2 Assumptions

To ensure the accuracy of our proposed model, we make the below assumptions, which are properly 微信公众号：数学模型 justified:

1. The performance in different sports does not affect each other. This assumption aligns with the International Olympic Committee’s sport categorization framework that treats disciplines as distinct competitive domains.

2. All athletes without medals can be treated as holding equivalent competitive standing to fourth- place finishers, because of limited historical records.

3. Each country is restricted to obtaining at most one medal per event, regardless of the number of participating athletes, which enables holistic evaluation of national athletic ecosystems by preventing single-event dominance from overshadowing broader capability distributions. 微信号：MATHmodels 4. Since dissolved states without internationally recognized successor entities can contaminate modern Olympics prediction result, they are excluded from the modeling framework, with their historical data truncated at the dissolution timestamp.

5. Consistent with IOC sanctions on Russia, Russian athlete participation parameters for the 2028 Olympiad can be excluded, reflecting suspension measures in response to geopolitical conflicts.

3 Notations

The key mathematical notations used in this paper are listed in Table 1:

Symbol

Description

Symbol

Description Δ𝜇 𝜎𝑡𝑒𝑎𝑚 Difference in Athlete National Team Std Performance Dev 𝑃𝑒𝑟𝑓𝑡 𝜖𝑡 Athlete’s Real White Noise Error 𝑖 Performance Term 𝑃𝑒𝑟𝑓𝑆𝑝𝑜𝑟𝑡𝑠𝑘 𝑃𝑒𝑟𝑓team Team Performance Country Sport 𝑖 Performance 𝜎𝑎𝑡ℎ𝑙𝑒𝑡𝑒 𝐶𝑜𝑎𝑐ℎ𝑖,𝑘 Athlete Std Dev Coaching Effect

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

4 Data Preprocessing

Our data preprocessing work primarily focused on the summerOly athletes.csv dataset.

1. We removed data from countries that no longer exist and those no longer competing, like RUS.

For merged countries like East and West Germany, we merged them under a single NOC.

2. To better utilize the data, we standardized event names. Events were categorized into currently existing and discontinued events. Discontinued events were removed from the dataset. For existing events, we mapped historical names to their 2024 counterparts.

3. Based on the assumptions outlined in section 2, we consolidated athletes from different teams of the same country into their respective national teams.

5 Medal Projection Model

We first divide all events into two categories: traditional events that occur in every Olympics and new events being introduced every year.

For traditional events, we use a TrueSkill-SARIMAX model with a bottom-up approach. This involves evaluating each national team’s performance at the event level, predicting their future perfor- mance, and determining medal outcomes based on predicted performance rankings.

关注数学模型 For new events, we use a random forest model to predict medal outcomes for 2028’s new events, using historical data from previously introduced events and their medal distributions.

Finally, we aggregate the medal predictions and their confidence intervals from both categories to produce the overall medal table.

5.1 TrueSkill Sports Performance Evaluation Model

Research indicates that Olympic medal predictions cannot rely solely on historical medal tables. 微信公众号：数学模型 A country’s success in specific events depends on their relative Performance level. To evaluate a country’s performance and uncertainty in various events, we innovatively introduced the TrueSkill[2] sports performance evaluation model.

For each event, athletes are grouped by their national teams. Assume each athlete 𝑖has a real-valued skill at time 𝑡, denoted as skill𝑡 𝑖. The initial Skill is drawn from a Gaussian distribution with mean 𝑚0 and variance 𝑣0, expressed as: Skill𝑡0 𝑖∼N (𝑚0, 𝑣0) (1) where 𝑡0 represents the athlete’s first Olympic appearance time, and 𝑚0 and 𝑣0 are adjustable parameters.

After each Olympics, each athlete’s Skill changes by a value drawn from a Gaussian distribution. 微信号：MATHmodels Athletes also gain experience from competitions: where 𝑡′ > 𝑡 𝑖, 𝜏2(𝑡′ −𝑡)), Skill𝑡+𝐿 ∼N (Skill𝑡 Skill𝑡′ 𝑖∼N (Skill𝑡 𝑖, 𝛾2) (2) 𝑖 where 𝐿represents the number of Olympics participated.

The next step generates match results based on athlete skills. TrueSkill assumes each athlete has a real-valued performance in each match:

Perf𝑡 𝑖∼N (skill𝑡 𝑖+ teamOffset(size of team), 𝛽2) (3) where 𝛽is an adjustable parameter reflecting game randomness.

For subsequent discussion, we omit Perf𝑖’s dependence on 𝑡as we’re discussing specific matches. During Olympic competitions, each team’s performance is defined as the weighted sum of all athletes’ performances, with weights proportional to their participation time to account for experience:

Perf𝑖· timePlayed𝑖 ∑︁ Perfteam = (4) 𝐿 𝑖∈team Then rank the national performance Perfteam in descending order to determine which countries can win medals. We adjust 𝑚0 and 𝑣0 according to the actual results of that year. Based on this process, we obtained each country’s performance in a particular event for each year.

We also need to determine the error of the event performance. For the error calculation of individual athlete’s Skill𝑖, it is divided into two cases: case 1 is applied when comparing different athletes, while case 2 is applied due to long-term non-participation:

√︃ 𝑣𝑡𝑜𝑡𝑎𝑙· 𝑤), 𝑤= 𝜙(𝑥) Φ(𝑥) ( 𝜙(𝑥) Δ𝜇 𝜎2 𝜎2(1 − √𝑣𝑡𝑜𝑡𝑎𝑙), case 1  Φ(𝑥) + 𝜎𝑎𝑡ℎ𝑙𝑒𝑡𝑒= (5) 𝜎2 + (𝜏· 𝑡)2, case 2 √︁  where 𝑣𝑡𝑜𝑡𝑎𝑙represents the total variance, calculated as 𝑣𝑡𝑜𝑡𝑎𝑙= Í𝑛 𝑖=1 𝜎2 𝑖+ 2𝛽2, 𝜏is the time decay factor, 𝑡is the number of days without participation in the competition.

Subsequently, the national team's standard deviation is derived from the standard deviation values of all athletes within the team:

n ∑ (6) σteam 二 player,i i=1 In this way, we obtain the yearly Performance values Perf, for each country in each event and its standard deviation σteam· Part of our results is illustrated in the following Figure 4, showing changes over time in the performance of different countries in various events.

Canada Japan

China United States

米 France United Kingdom

二

5.2 SARIMAX-Bayesian Model: Predicting Future Medals

From subsection 5.1, we obtained the performance levels of different countries in each Olympic event from 1896-2024. Since a country's performance level in an event shows periodic fluctuations and is directly related to the Olympic host country, we innovatively introduced the SARIMAX time series prediction model to predict future national performance levels in specific events using these factors.

SARIMAX Prediction Largo Predicted event Evend-lievel Hoat Country Effect amount level Smal Linear Regression

关注数学模型

The SARIMAX model combines autoregression AR, moving average MA, seasonal patterns S,

and exogenous variables X[3]. It requires target, a country's performance on a typical event, donated as Perft, where t represents time. Host country, donated as Host,, is the exogenous variable model use.

To begin with, SARIMAX process the AR part, representing the relationship between the current target value and its past values. Also, MA part is processed to represent the relationship between current error and past errors. Periodic patterns are then captured by SARIMAX through seasonal auto-regression coefficients φk:

S p q Perft = ∈t + ∑ θj∈t−j Per    = it- Perft = ∑φkyt-k·s (7) i=1 j=1 k=1 Where: α is the constant term. β1, . . . , βp are autoregression coefficients, representing the relationship between the current value and previous p moments values. θ1, . .., θq are moving average coefficients that represent the relationship between current error and previous q moment errors. s is the period of time, and φk is the seasonal autoregression coefficient.

Then, fit the AR and MA coefficients by minimizing the sum of squared residuals:

O βi, θj, φk,  = arg min ∑ (Perf, − Perft)2 (8) 1=1 This completes the model training. Finally, aggregate all parts to obtain the complete model and use the complete model to predict future data:

●

b (9) k=1 j=1 i=1 Additionally, the SARIMAX model performs very inaccurately on small datasets. For events with shorter time spans, we used simple linear regression.

Through this method, we obtain the performance levels of events of each country Pêrft+1 for _ traditional events in 2028.

In section 5.1, the result Pêrft+1 of the TrueSkill model involves a standard deviation. Similarly, the prediction results from SARIMAX also have a standard deviation. Since this standard deviation cannot be predicted using the SARIMAX model, we use a Bayesian prediction method, based on the same principle as TrueSkill, to predict the standard deviation.

We model the future standard deviation using an Inverse Gamma distribution, which is a natural conjugate prior for variance parameters[4]:

σ2 ∼ InvGamma(α, β) (10) Given historical standard deviations σ 2 2 we can updaate the parameters as:

T T 1 ∑(σ7 − µ)2 (11) βT = β0 + 12 + 0x = Lxp 2 t=1 Finallyupdating αT and βT to obtain the new predicted standard deviation:

βT (12) T+1 αT − 1 Using this method, we can obtain the predicted values for the standard deviation ˆ𝜎𝑡+1 of the ˆ performance level Perf𝑡+1. We made a heatmap to show the predicted performance of certain countries in various events, as shown in the following Figure 6. We also made a heatmap to illustrate the predicted standard deviation of certain countries in various events, as shown in the following Figure 7:

Countries in Various Events tain Countries in Various Events

5.3 Random Forest Model: Predicting Medals in New Events

For newly added events, since the new events in each Olympic Games are uncertain, and independent from other events, they cannot be evaluated using the TrueSkill model or predicted with SARIMAX. Therefore, we applied the Random Forest model to predict the number of medals in new events.

Random Forest regression[5] is an ensemble learning method that builds multiple decision trees for regression prediction. Each tree is trained on a different subset of the data and features, and the final prediction is obtained by averaging the results from all trees.

Our model should first determine the input variables. Input variables include the total number of medals in both new and traditional events for each Olympic Games, the number of medals won by the host country in these two types of events, and the number of medals won by other countries in each of these events.

These variables are then fed into the Random Forest model, which outputs predictions and model errors on test cases, including MSE and MAE. We selected the best-performing parameters to complete the model training. The errors on the test set are shown in Table 2:

Target Variable MAE

Host Gold 0.1988

Host Silver 0.3460

Host Bronze 0.2784

It can be observed that our model does have a certain degree of accuracy.

Finally, we used the medal predictions for traditional events in 2028 (from sections 5.1 and 5.2) as inputs to predict the performance in new events for each country.

关注数学模型

5.4 Model Aggregation

The predictions from the 3 sections above are then aggregated to predict medals. By adding the medal counts of traditional events and newly added events, we obtain the predicted medal values.

微信公众号：数学模型 However, we must also determine the prediction intervals for the medals. The method is as follows:

For a specific event, for the predicted Pref from Section 5.1, we have Pref𝑡∼N (𝜇, 𝜎2). Therefore, the actual Pref𝑡of the country will always lie within the interval (Pref −3𝜎, Pref + 3𝜎). From this, we can obtain the best possible performance and the worst possible performance, denoted as Prefmin and Prefmax.

For a given country, the worst-case scenario occurs when its performance is Prefmin and the performance of other countries is Prefmax. We use these Prefextreme to reorder the countries in descending order and determine whether the country will win a medal in that event. This process is repeated for all countries in all events to obtain a worst-case medal table. Similarly, we can use this method to obtain the best-case medal table.

微信号：MATHmodels By combining the two medal table above, we obtained our predicted medal table with prediction intervals.

5.5 Model Evaluation

We use the 2024 data as a test set to evaluate the accuracy of our model. We applied our model to data from the 2020 Olympics and earlier, obtaining medal count prediction intervals. Then, we compared these intervals with the actual values from 2024, resulting in the following Figure:

As shown in the figure above, our model predictions generally fall within the correct range, demonstrating the accuracy of our model.

6 Task 1: Medal Prediction and Analysis for the 2028 Olympics

We have completed the model construction in Section 5. In the following section, we are going to focus on solving the task.

6.1 Medal Table Projections

Using data from 2024 and earlier Olympics as input to the model, we obtained the virtual medal table with intervals, as shown in Figure 9 below:

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We then compare the medal table we obtained with the 2024 medal table and identify the countries m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m that are most likely to improve or worsen in the medal table and gold medal table, as shown in Figure 10 and Figure 11 below:

关注数学模型 微信公众号：数学模型

微信号：MATHmodels

It is evident that the USA, GBR, and POL are likely to see significant improvements in their gold medal counts, while FRA and NED are likely to experience a decline in their total medal counts.

6.2 First Ever Medal

We have just focused on the top positions in the predicted medal table. Now, let us shift our attention to the bottom of the predicted medal table. By analyzing the historical data, we find that the countries AND and SOL, which had never earned medals in the past, earned medals in our predictions. They each won their country’s first medal in the events Athletics Men’s 3000m Steeplechase and Athletics Women’s 100m, respectively. This suggests that our model can predict medal results for countries that have never won medals before.

So, how many countries are most likely to win medals in 2028? We conducted a Monte Carlo simulation for all countries that had never earned medals in the past, and the specific method is as follows. For each country 𝑖, its performance level Perf𝑖in each event follows a normal distribution:

Perf𝑖∼N (𝜇𝑖, 𝜎2 𝑖) (13) To account for the competition for medals, suppose there are 𝑛countries participating in event 𝐸, each with performance level Perf𝑖following a normal distribution N (𝜇𝑖, 𝜎2 𝑖). We perform 𝑁simulation draws. In each draw, for each country 𝑖(including smaller countries 𝑗), we sample from the normal distribution N (𝜇𝑖, 𝜎2 𝑖) to obtain the performance level Perf𝑖for each country.

By comparing the performance levels of all countries, we determine the ranking of each country in event 𝐸. If a smaller country 𝑗ranks in the top three, it is considered to have won a medal.

We then count the number of times country 𝑗wins a medal in 𝑁simulations, denoted as 𝑁𝑗, and calculate the probability that country 𝑗wins a medal in event 𝐸:

𝑃𝑗(𝐸) = 𝑁𝑗 (14) 𝑁 For other possible events 𝐸1, 𝐸2, . . . , 𝐸𝑚in which country 𝑗might win a medal, we repeat the process above to calculate the medal-winning probability for country 𝑗in each event 𝐸𝑘. Then, the total probability of country 𝑗winning a medal across all possible events can be computed by a weighted average: 𝑚 ∑︁ 𝑃𝑗(medal) = 𝑤𝑘𝑃𝑗(𝐸𝑘) (15) 𝑘=1 Using the multiplication rule of probability, we calculated the probability of the number of countries that have never won a medal winning one, as shown in the Table 3 below:

Number 0 1 2 3 4 5 6 7 8 9

P 0.06 0.18 0.25 0.22 0.14 0.08 0.03 0.01 0.01 0.00

The expected number of countries that have never won a medal to win one is 2.67. According to probability theory, we believe that two smaller countries are most likely to win medals in 2028, with a probability of 0.24.

6.3 Task 1.3

Since we use a bottom-up approach by obtaining the performance values for each country in each event every year, the ranking of each country in each event is determined by its performance value 𝑃𝑒𝑟𝑓𝑖𝑗, where a smaller ranking indicates better performance. Let 𝑅𝑖𝑗denote the ranking of country 𝐶𝑖in event 𝐸𝑗, which satisfies:𝑅𝑖𝑗= Rank(𝑃𝑒𝑟𝑓𝑖𝑗). Rank(𝑃𝑒𝑟𝑓𝑖𝑗) is the rank of 𝑃𝑒𝑟𝑓𝑖𝑗among all countries.

To standardize the performance values across different events, we first normalize the performance values for each event. The normalized performance value 𝑃𝑒𝑟𝑓′ 𝑖𝑗is given by:

𝑃𝑒𝑟𝑓𝑖𝑗−min𝑗𝑃𝑒𝑟𝑓𝑖𝑗 𝑃𝑒𝑟𝑓′ 𝑖𝑗= (16) max𝑗𝑃𝑒𝑟𝑓𝑖𝑗−min𝑗𝑃𝑒𝑟𝑓𝑖𝑗

This ensures that the performance values of all events are within the same range.

For each country 𝐶𝑖and sport 𝑆𝑝𝑜𝑟𝑡𝑠𝑘, which consists of multiple events, the overall performance of country 𝐶𝑖in sport 𝑆𝑝𝑜𝑟𝑡𝑠𝑘is the average performance of all events within the sport:

𝑞 = 1 𝑃𝑒𝑟𝑓𝑆𝑝𝑜𝑟𝑡𝑠𝑘 ∑︁ 𝑃𝑒𝑟𝑓′ (17) 𝑖𝑗𝑘 𝑖 𝑞 𝑗=1 where 𝑞is the number of events in sport 𝑆𝑝𝑜𝑟𝑡𝑠𝑘.

关注数学模型 If 𝑃𝑒𝑟𝑓𝑆𝑝𝑜𝑟𝑡𝑠𝑘 is larger, it indicates that country 𝐶𝑖has a better average ranking in that sport, 𝑖 implying that the sport is more important to the country.

We have created a heatmap to visually represent the process of identifying the most important sports for various countries, as shown in Figure 12:

微信公众号：数学模型 微信号：MATHmodels

According to the random forest model in Section 5.3, we have estimated the number of medals the host country is likely to win in newly added events. Additionally, our model found that host countries tend to perform better in these new events. The number of medals won by the host country in newly introduced events is significantly higher than that of other countries. By comparing with past data, it is also evident that the proportion of medals won by host countries in newly introduced events is much higher than that of other countries.

We visualized this phenomenon, as shown in Figure 13 and Figure 14 below, where red represents the proportion of total medals held by the host country, purple represents other countries, and the other colors represent the countries ranked higher on the medal table.

Host Country and Other Countries In New Host Country and Other Countries in Tradi- Events tional Events

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The inclusion of new sports or the re-emphasis of certain disciplines will likely boost the medal count for host nations in those typical areas.

7 Task 2: Great Coach Effect

In addition to the athletes’ own performance, coaches may also influence the allocation of medals. In this task, we will focus on an unknown variable: the coach. We need to accomplish the following tasks:

• Find evidence of how coaches influence athletes’ performance and medal counts.

• Analyze the impact of coach effects on medal counts.

• Conduct an analysis for three different countries to assess in which sports they should hire a great coach.

7.1 Residuals Test: Evidence of Changes That Might Be Due to Great Coach

Effect

To identify which countries have evidence of great coaches in certain events, we implement a residuals test.

First, we analyze the variables most likely to be influenced by the coach effect.The following symbols all represent a specific NOC. Four variables were selected:

• Event Performance Perf𝑡: This is the yearly event performance measured in section 5.

关注数学模型 • Sport Performance Sport𝑡: The performance level in each sport, calculated in section 5.

微信公众号：数学模型

• Number of participants N: The number of athletes participating in an event.

• Medal count 𝑦𝑖𝑘: Medal count of country 𝑖in event 𝑘.

The core principle of anomaly year detection is to identify outliers through time series modeling combined with residual analysis.

First, the VARMAX model is introduced to perform maximum likelihood estimation to fit the time series data and solve for the model parameters[6], capturing the dynamic relationships between multiple variables.

The model is expressed as:

微信号：MATHmodels 𝑌𝑡= 𝐴1𝑌𝑡−1 + 𝐴2𝑌𝑡−2 + · · · + 𝐴𝑝𝑌𝑡−𝑝+ 𝐵𝑋𝑡+ 𝜖𝑡 (18)

where: 𝑌𝑡is the vector of response variables, 𝐴𝑖is the autoregressive coefficient matrix, 𝑋𝑡is the exogenous variable, as is shown above, 𝐵is the coefficient matrix for the exogenous variable, 𝜖𝑡is the white noise error term.

Next, two anomaly detection methods are introduced. The Mahalanobis distance is used to calculate the standardized residual distance, considering the covariance between variables, with the following formula:

𝑡= (𝜖⊤ 𝑡Σ−1𝜖𝑡) 𝐷2 (19)

where: 𝜖𝑡is the residual vector, Σ−1 is the inverse of the covariance matrix, 𝐷2 𝑡is the square of the Mahalanobis distance.

Robust covariance estimation is used to reduce the impact of outliers. If the computed Mahalanobis distance exceeds the .95 percentile, it is considered an outlier.

The second method is CUSUM, which detects anomalies by calculating the cumulative sum of squared residuals:

𝑡∑︁ 𝑆𝑡= (𝜖2 𝑖−𝜇) (20) 𝑖=1

where: 𝜖2 𝑖is the squared residual, 𝜇is the mean of the residuals.

If the cumulative sum 𝑆𝑡exceeds 3 times the standard deviation, a shift point is detected, and the point is considered an anomaly.

Finally, the joint decision-making process involves taking the union of the two methods to avoid missing outliers. Anomalous points are determined by the results of both the Mahalanobis distance and CUSUM detection. The anomaly information we obtained is shown in Figure 16 below:

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We found that the coaches mentioned in the problem, Lang Ping and B´ela K´arolyi, had data anomalies in the years they coached, confirming our hypothesis.

7.2 LR-SCAD: Estimate Great Coach Effect Contributes To Medal Counts

Next, based on the results of the residual test, we list a set of coach effect variables. Coach𝑖𝑘is the coach effect variable for event 𝑘in country 𝑖. These variables represent the coach effect across different sports. To verify whether the coach effect significantly impacts the medal count, we include multiple potential variables affecting the medal count and the coach effect variables as independent variables in the LR-SCAD model[7].

The goal of the LR-SCAD model is to select key independent variables that affect the medal count and assess their impact. The regression equation is set as follows:

𝑦𝑖𝑘= 𝛽0 + 𝛽1 · 𝑋𝑖𝑘1 + 𝛽2 · 𝑋𝑖𝑘2 + · · · + 𝛽𝑚· 𝑋𝑖𝑘𝑚+ 𝛽coach · Coach𝑖𝑘+ 𝜖𝑖𝑘 (21)

where 𝑦𝑖𝑘is the medal count for country 𝑖in event 𝑘. 𝑋𝑖𝑘1, 𝑋𝑖𝑘2, . . . , 𝑋𝑖𝑘𝑚are other variables that may influence the medal count. 𝜖𝑖𝑘is the error term.

After performing the SCAD model selection, if the coefficient 𝛽coach is still significant (i.e., non- zero) in the regression model, it indicates that the coach effect has an independent impact on the medal count. This means that even when controlling for other variables, the coach effect still plays an irreplaceable role and cannot be explained by other variables. This result shows that the coach’s role in certain sports (e.g., team sports) is crucial, and even if athletes are highly skilled, a lack of the right coach will prevent them from achieving good results.

By analyzing the SCAD parameters from the model, we can determine the specific contribution of the coach effect to the medal count for each country in each sport. We then sum these contributions to find the coach effect’s contribution to the total medal count for the country:

关注数学模型 𝐾 ∑︁ 𝛽coach,𝑘· Coach𝑖𝑘 Contribution = (22) 𝑘=1

where 𝛽coach,𝑘is the coach effect coefficient for event 𝑘.

Thus, by summing the contributions from various sports, we can determine the total contribution of the great coach effect to the country’s overall medal count, as shown in Figure 17 below:

微信公众号：数学模型 微信号：MATHmodels

7.3 Choose three countries and identify sports where they should consider

investing in a “great” coach and estimate that impact

Next, we selected three NOCs, namely USA, SWE, and CHN, and calculated the great coach effect contribution for each sport. We chose the one that brings the highest benefit and calculated the resulting change in medal count, as shown in Figure 18 below:

In this regard, we made the following recommendations:

• For the USA NOC, we suggested hiring a great coach for Rowing, Fencing, and Canoeing. With the influence of a great coach, these sports are expected to add 0.8 medals to the medal table.

• For the SWE NOC, we recommended hiring a great coach for Table Tennis, expecting an increase of 0.9 medals in the medal table.

• For the CHN NOC, we advised hiring a great coach for Football, expecting an increase of 1 medal in the medal table.

In conclusion, these changes demonstrate that our model effectively captures potential scenarios involving the coach, analyzes the changes it brings to the variables, and incorporates these changes back into the model, which led to the expected impact of the coach on the medal count.

8 TASK 3: Oringinal Insights

In this section, we will focus on original insights that were not addressed in the task but were proposed through the analysis of our model results. Based on these original insights, we will also provide effective recommendations for the Olympic Committees of the relevant countries.

8.1 Insights and Recommendations for Countries That Have Never Won Medals

Based on Section 6.2, our model identified several events in which countries that have never won medals are most likely to win. It also quantitatively shows the contribution of the coach effect to a country’s medal count. This means that for countries that have never won a medal, hiring an excellent coach for the most likely events can significantly increase the probability of winning a medal.

关注数学模型 To investigate this specific impact, we applied our model to two NOCs that have never won any medals before: BEN NOC and BOL NOC. Their predicted probabilities of winning medals in the following events are illustrated in Figure 19 and Figure 20 below:

微信公众号：数学模型 微信号：MATHmodels

medals for BOL medals for BEN

Based on this, we suggest that BEN NOC and BOL NOC should adopt our model and hire Great Coaches for Swimming Men’s 50m Freestyle and Athletics Women’s 20km Race Walk respectively, in order to pursue their first historical medals.

Moreover, we recommend that the Olympic Committees of countries that have not yet won medals refer to our model and, taking their own strengths into account, look for excellent coaches in specific events to increase the probability of winning their first medal.

8.2 Insights and Advice for NOCs on Deploying Experienced Athletes

We also found that experienced athletes in certain events in specific countries have a significant impact on the overall level, which in turn influences the total medal count. Our model measures the country’s event performance level in the sport using the Trueskill system, where the experience of athletes influences the level. Below are the overall medal statistics for USA NOC in the Fencing Men’s Foil Team, the proportion of veteran athletes, and the level changes. These changes are shown in m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Time

This means that for USA NOC in the Fencing Men’s Foil Team, having more experienced athletes participating in the event may increase the likelihood of winning a medal, compared to sending more new athletes.

Therefore, we suggest that the Olympic Committees of different countries use our model to analyze past event performance and, based on the analysis, send more experienced athletes to the competition to improve their chances of winning medals.

9 Model Evaluation

Strengths:

• We innovatively employed a variety of methods to comprehensively integrate as much useful information as possible, achieving a relatively high prediction accuracy.

• Compared to directly predicting using medal counts, the model compensate for missing cases.

• When a country doesn’t participate in an event in a certain year, its level doesn’t reset to zero and can still be used in subsequent predictions.

• We innovatively proposed the LR-SCAD model to accurately measure the coaching effect, which holds significant guiding value for Olympic competitions.

Weaknesses:

To ensure accuracy, a relatively large amount of computation is inevitably required. In the future, we can further optimize the model to reduce the computational cost.

关注数学模型

10 Sensitivity Analysis

In the sensitivity analysis, we selected two hyperparameters from the TrueSkill model and two from the SARIMAX model that significantly influence the results. The following Figure 22 illustrates the variation in final medal prediction accuracy with changes in σ and β for TrueSkill, as well as p and q for SARIMAX, within a specified range.

WR 100% 100% 100% 87.5% -87.5% 100% 88.9% 75% 75% RSI Intensity RSI Intensity %82% 83.3% 62.5% 62.5% RSI Value 66.7% RSI Value 66.7% 50% 50% 55.6% 50% 44.4% 37.5% 37.5% 33.3% 25% 25% 33.3% 22.2% 12.5% 12.5% 16.7% 10 11.1% 5 0% 0% Value of σ 9 0% 0% Value of p 202.94458 0.00 0.71 1.42 2.13 2.84 2 6 Value of β 5 3.56 Value of q 5.00 4.28 0 5.00

●

It can be observed that when σ and β change, the prediction accuracy remains relatively stable overall, demonstrating the strong robustness of our model. This is because TrueSkill's influence on the level of each event is nearly uniform. However, prediction accuracy exhibits slightly larger fluctuations we  t  arte e a asee se so h  d  s dton è outcomes.

The Following Figure 23 shows that as the average number of samples used for time series prediction decreases, the final prediction accuracy initially tends to decline.

1.0 -60 -80 0.7 0.6 Precision 0.5 0.4 0.3 0.2 0.1 0.0 100 25 9 0 8 や 10 65 60 5 6 ふ 多 20 心 % 8 4 6 Average Number However, after a certain point, the downward trend slows. This is because our model automatically transitions to a simple linear regression prediction when there is less time series data, thereby avoid- ing larger errors introduced by time series forecasting. As a result, our model demonstrates strong adaptability across different datasets.

11 Conclusion

For Task 1, we built a bottom-up medal analysis and prediction model using the TrueSkill- SARIMAX-RF method. The model first categorizes all events into traditional events and new events. For traditional events, the TrueSkill model is used to evaluate a country’s performance in each event. Then, the SARIMAX model is applied to predict the country’s performance level for 2028. To account for potential errors, a Bayesian prediction method is employed. Finally, the predicted performance for 2028 determines the medal allocation. For new events, a Random Forest model is used to predict medal allocation. The results from these two parts of events are aggregated to form the final medal count model for each country.

For Task 2, we performed residual analysis to find evidence of how coaches influence athletes’ performance and medal counts. By analyzing different variables, we identified anomaly information in the data, providing evidence of how the “great coach” effect alters the data. Subsequently, we studied how the “great coach” effect contributed to changes in the total medal count for different countries and created visualizations for this. Finally, we selected USA NOC , SWE NOC , and CHN NOC and identified the sports in which these countries should invest in a great coach. We then evaluated the impact of the great coach on their medal counts.

For Task 3, based on the model, we analyzed and derived 2 factors that affect a country’s medal count, which were not covered in Tasks 1 and 2. These factors were then integrated into insights and explained how these insights could provide valuable reference for national Olympic committees.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

关注数学模型 微信公众号：数学模型
