MCM/ICM

Summary Sheet

Summary

Predicting Olympic medal counts is a hot topic in the sports world. Based on the data of previous Olympic Games, we constructed a Random Forest regression model for predicting the number of medals in future Olympic Games, offering a new approach to medal prediction.

In the first part of Problem 1, we constructed a medal prediction model by considering factors such as the level of athletes, the number and types of events, and the identity of the host country. Through ten-fold cross-validation, we compared Random Forest Regression, Lasso

Regression, XGBoost Regression and Neural Network Regression models respectively, and evaluated model performance using metrics such as R2 and MSE. The results show that the Random Forest Regression model performed best with an R²of 0.92 on the test set. Based on the predictions from this model, the three countries with the highest total medal counts at the 2028 Los Angeles Olympics are projected to be the United States, China, and the United Kingdom. Compared to previous Olympic Games, the United States is expected to see a 10% increase in the number of gold medals, while Japan is predicted to experience a 5% decrease in its gold medal count.

In the second part of Problem 1, for countries that have never won a medal, we constructed

the Logistic Regression Model to predict their probability of winning, and the results show that four countries may win for the first time, with Angola's probability of winning for the first time being 0.81, making it the most likely to win for the first time. Subsequently, we explored the correlation between the events and the total number of medals by the Gray Cor- relation Analysis Model and found that there is a significant correlation between some of the events and the medal performance of specific countries.

For Problem 2, in order to explore the impact of the “great coach” effect on medal out- comes, we conducted the Two-sample mean hypothesis testing and the Chi-square test to examine the influence of great coaches on Olympic medal performance. The Logistic Regres- sion Model was also applied to quantify the coach effect. The results show that the impact lies between athlete skill and the number of participants. Based on the results of the model analysis, we suggest that the United States, China and Japan should focus on investing in sports with great coaches.

For Problem 3, we explored the impact of host advantage on Olympic medal potential from a game-theoretic perspective. By utilizing the N-player Game Theory and analyzing the Nash Equilibrium, we revealed the interplay of medal distributions across countries and fur- ther elucidated the key role of host advantage in Olympic medal prediction.

Finally, we performed error evaluation and sensitivity analysis of the Cross-validation folds, verified the higher prediction accuracy and model robustness.

1 Introduction

1.1 Problem Background

The Olympic medal table measures countries' sporting prowess and informs their preparations for the Games. In the 2024 Paris Olympics, the United States, China, France, and the United Kingdom ex- celled, with the U.S. leading with 126 medals and China tying for the most golds. Several countries, in- cluding Albania, Cape Verde, Dominica, and St. Lu- 微信公众号：数学模型 cia, won medals for the first time, highlighting global competitiveness. However, over 60 countries still haven't won an Olympic medal, showing disparities

in the global distribution of sports resources.

Predicting the number of Olympic medals has always been an important research problem, and traditional methods mostly rely on historical medal data. However, with the advance an- nouncement of athlete lists and program settings, medal prediction based on more data and factors is gradually becoming a trend. By taking into account the strength of athletes, the types of events and other key factors, medal prediction can not only provide decision support for 微信号：MATHmodels national Olympic committees but also help event organizations and related departments to op- timize the allocation of resources.

1.2 Restatement of the Problem

Based on the given data, we specifically address the following questions:

Question1: Build a model using the given data to predict the number of gold medals and total medals for each country. Evaluate the model's uncertainty, accuracy, and performance.

⚫ Based on the model, predict the medal standings for the 2028 Los Angeles Summer Olympics. Provide prediction intervals for all results and analyze which countries may show improvement and which countries may decline in performance.

⚫ Estimate the number of countries that have not won a medal yet, and predict the like- lihood of these countries winning their first medal in the next Olympic Games.

⚫ Explore the relationship between the number and type of Olympic events and medal counts, and analyze how different sports matter to countries and how the host coun- try's event selection affects competition results.

Question2: Analyze the impact of the "Great coach" Effect on medal counts, estimate its contribution, and recommend sports for three countries to invest in great coaches, along with the expected impact.

Question3: Present the novel insights revealed by the model regarding Olympic medal

counts and explain how these insights can serve as valuable reference information for national Olympic committees.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1.3 Literature Review

The prediction of Olympic medals has always been a hot topic in sports science research. [1]The research of Nagpal P, Gupta K and Verma Y et al predicted the medal table through various regression methods (such as linear regression, polynomial regression, ridge regression, etc.). They found that socio-economic factors (such as GDP and population) have a significant impact on the number of medals. [2]Zicheng Song's research predicted the number of Olympic medals of various countries based on a neural network model, emphasizing the advantages of deep learning in dealing with complex non-linear relationships. [3]J. Moolchandani, V. Chole, and S. Sahu et al used machine learning methods to predict the medal distribution of the 2024 Summer Olympics. They used models such as linear regression, random forest, and support vector machine for prediction. The results showed that the random forest model had the highest accuracy, reaching 99%. Based on their research, this paper will further discuss and predict the medals of the 2028 Olympic Games. 1.4 Our Work

Question 1 Task 1 Task 2 Task 3 Number of Sports Host Mother Types of Athlete's Subsequence: Number of Numberof Olympic events & country's sequence: Medal counts sports level athletes Games athletes quantities advantages participated Total medals per sport participated per country

Input variable

Random Forest Trained logistic regression Cross - validation Grey XGBoost Lasso correlation Neural Network

Compare R² etc Probability of winning Random Host - selected the first medal Forest event - medal relationshíp

Event - medal Prediction Performance Medal table relationship prediction interval comparison

Question 3 Question 2 Coaching Medals won Number of duration of in event event excellent hístory participants coaches Invest in Concentrate emerging resources projects Trained logistic regression Two-sample Chí-square test mean test The host sets up Event medal- Regression advantageous winning coefficient projects probability Significantl y affected Optimal Coach investment contribution event

关注数学模型

2 Assumptions and Justifications

微信公众号：数学模型 To simplify the problem, we make the following basic assumptions, each of which is properly justified. Additional, more specific assumptions will be introduced as needed to refine our models. ⚫ Assumption 1: There will be no changes to the list of sports announced for the 2028 Los Angeles Olympics.

Justification: This assumption means that we assume that all new or existing Olympic sports will not undergo any changes before the 2028 Los Angeles Olympics, i.e. no new sports will be added and no existing sports will be deleted or canceled. This assumption helps us to simplify the model and to focus on existing data and known changes to the Olympic sports. 微信号：MATHmodels ⚫ Assumption 2: New projects will have less impact on non-winning countries Justification: We assume that for countries that have not yet won an Olympic medal, the addition of new sport will not immediately change their chances of winning a medal. These countries may be able to compete for medals in some of the new sports, but given their overall strength and athlete pool, the impact of the new sports is expected to be small, especially in the short term. ⚫ Assumption 3: Assuming that the level of sports in each country remains stable.

Justification: This assumption means that we assume that there will be no significant changes in the level of athletes ( including skill, fitness, athleticism, etc. ) in the different Olympic sports in each country. ⚫ Assumption 4: U.S will be competitive with home-field advantage in additional events at the 2028 Los Angeles Olympics.

Justification: With this assumption, we believe that the United States may be in a more favorable position than other countries to compete for medals in the five additional Olym- pic sports, especially since it has a clear competitive advantage in terms of technological accumulation and resource investment.

3 Notations

The key mathematical notations used in this paper are listed in Table 1.

Symbol

Description Number of gold medals won in the j-th event of the i-th sport Number of silver medals won in the j-th event of the i-th sport Number of bronze medals won in the j-th event of the i-th sport Non-medal participants in the j-th event of the ith sport Number of athletes who did not win a medal Number of participation in the programme Number of sessions of participation Number of hours of great coaching in the sport Historical medal count Number of participating athletes

4 Data Pre-processing and Visual Analytics

4.1 Data Pre-processing

Analyzing the given data reveals redundancy and scatter, so we first perform outlier re- moval, data complementation, integration, and collection to prepare for model construction later in the paper.

◆ Outlier Handling The 1906 data in the summerOly_athletes attachment pertains to the unofficial Olympic Games and should be removed as outliers. Additionally, data from several Olympic Games affected by international situations and other factors will be deleted to prevent negative impact on the model.

◆ Data Completion The summerOly_programs annex contains some missing data. After review, the missing values are filled in to ensure completeness and avoid affecting subsequent analysis.

◆ Data Consolidation （1）Text Data Processing Gold medals are coded as 1, silver as 2, bronze as 3, and no medals as 0. The host country for each year is labeled as 1, while all others are labeled as 0.

（2）Data Aggregation Data aggregation is performed based on country, event, and year, with the following ag- gregation rules:

①Each event is categorized by sport, and the number of gold, silver, and bronze medals, as well as the number of participants, are calculated.

②If an event is missing in a certain year, all countries will have a value of 0 for that event.

（3）Data Encoding Countries are sorted in ascending order by name, and each country is assigned a numerical code starting from 1 to replace the country name.

（4）Standardization of region names In the annex 'summerOly_medal_counts', add a column with the Olympic Games country abbreviation in the NOC column to facilitate subsequent modeling.

◆ Data Collection

Given that the total number of medals depends entirely on the events included in the Sum- mer Olympics and that countries specialize in different sports, it is crucial to know the events scheduled for the 2028 Games. Relevant event details have been compiled and recorded in the annex 'summerOly_programs' for unified processing. Below are the data sources：

Database Names Database Websites Data 2028 Olympic sports https://la28.org/ Countries participating in the 2028 Olympic Games https://www.olympics.com/en/ International Coach Council https://coachfederation.org/ Entertainment Sports Programming Network https://www.espn.com/

关注数学模型

4.2 Visual Analytics

This section presents a visual analysis of Olympic medal counts through statistical charts, offering insights into the distribution of medals across countries and highlighting their compet- itive strengths over time and in different sports.

◆ Number of medals by country Analyze the data and draw the following statistical graphs：

微信公众号：数学模型 微信号：MATHmodels

Analysis of the graph reveals that the United States leads in both gold medals (1,027) and total medals (2,583), demonstrating its strong competitiveness. The USSR and China rank sec- ond and third with 352 and 303 gold medals, respectively, though China surpasses the USSR in total medals (727 vs. 907). Countries like Great Britain, France, and Germany show more balanced performances, with Great Britain achieving 292 gold medals and 944 total medals. In conclusion, the United States remains dominant in Olympic performance, while other nations show varying strengths in gold and total medal counts.

◆ Time series chart of the number of medals in each event Under normal circumstances, the number of medals won by each country should follow a stable trend, either gradually increasing or decreasing, with no abrupt fluctuations. This is due to each country's unique geographical position and specialization in specific events, with per- formance trends accumulating over time. Taking the United States as an example, the medal count for each edition of the Games and the four disciplines where it performed most promi- nently were selected and analyzed, as shown in the chart below:

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m cantly over the years. Notably, the U.S. reached peak medal counts in 1904 and 1984, likely due to its role as host. During both World Wars, U.S. medal counts declined, possibly reflecting the disruption caused by the wars. Since the 21st century, while fluctuations have occurred, the U.S. has maintained a generally high medal count.

with high medal counts sustained over most years. Basketball, since its Olympic debut in 1936, has been another stable area of success, reflecting the U.S.'s continued dominance, particularly through professional leagues like the NBA, which has kept U.S. basketball at the forefront globally.

5 Olympic Medal Prediction Based on Machine Learning

5.1 Medal Table Prediction Model Based on Random Forest

5.1.1 Determination of Input Variables

⚫ The level of athletes in various sports: Different countries have significant advantages in certain Olympic events. Usually, this is because the athletes in these countries have undergone long-term training and possess high-level technical and tactical capabili- ties as well as excellent physical fitness.

⚫ The number and types of competition events: The number and types of events in each

关注数学模型 Olympic Games affect a country's chances of winning medals. Some countries may have traditional advantages in the events that are added or removed from the Olym- pics, which will impact the number of medals they can obtain.

⚫ The impact of being the host country on medal performance: The host country usually has certain advantages in terms of psychology, resources, funding, and audience sup- port. This may enhance its performance in some events, and this is a typical 0 - 1 variable.

⚫ The number of athletes a country sends to the Olympics: Countries with a larger num- ber of participating athletes can usually compete in multiple events, thus increasing their chances of winning medals. More athletes mean more opportunities to perform 微信公众号：数学模型 and greater potential to increase the number of medals.

5.1.2 Comprehensive Strength Evaluation of Each Event

By analyzing the medal distribution of each event in the previous Olympic Games and the number of non-winning participants, a quantitative indicator was constructed to measure the comprehensive competitive strength of each country in that event. Based on the total number of historical medals of athletes, it is possible to effectively evaluate a country's performance and competitiveness in the event, providing a reliable reference for medal predictions in future Olympic Games.

微信号：MATHmodels Step1: Determine variables Let be the number of gold medals won in the j-th event of the i-th sport, be the number of silver medals won in the j-th event of the i-th sport, be the number of bronze medals won in the j-th event of the i-th sport, and be the non-medal participants in the j-th Event of the i-th Sport Step 2: Subjectively assign weights Each indicator (such as the number of gold medals, silver medals, bronze medals, and the number of non-medalists) contributes differently to the comprehensive strength. Therefore, we assign the following weights:

Step3: Quantification of the comprehensive strength of each country in each event

Let the comprehensive strength of the i-th event of the m-th country be , which can

be expressed as:

(1)

5.1.3 Establishment of the National Medal Quantity Prediction Model

Predicting the number of Olympic medals is a complex regression problem that involves multiple factors. To accurately predict the number of medals for each country, choosing an m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m appropriate machine-learning model is of great significance. Especially when dealing with multiple features and complex data relationships, different regression models have different advantages and applicable scenarios.

For this reason, this paper will compare four machine learning models widely used in regression problems: Random Forest regression, Lasso regression, XGBoost regression, and Neural Network regression. By comparing the prediction effects of these models, the aim is to find the model most suitable for the task of predicting the number of Olympic medals. To improve the accuracy of the regression models, this paper uses ten-fold cross-validation. The hold-out method is adopted, with 90% of the samples used as the training set and 10% of the samples used as the test set. The evaluation metrics of the four regression models are calculated, as shown in the following table：

During the comparison of multiple regression models, after comprehensive evaluation and verification, the Random Forest regression model outperforms other models in evaluation metrics such as , MSE and MAE. Therefore, based on its high prediction accuracy and strong generalization ability, this study finally selects the Random Forest regression model as the main tool for predicting the number of medals in the 2028 Olympic Games.

5.1.4 Medal Table Prediction Results Based on Random Forest

In order to accurately predict the number of medals of each country in the 2028 Olympic Games, we adopt the Random Forest regres- sion model. This model achieves efficient pre- diction by integrating multiple decision trees m m m m m m m m m m m m m m m m m m m m m m and is particularly suitable for dealing with data m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m with complex non-linear relationships and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m multi-dimensional features. The advantages of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the random forest regression model lie in its m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m strong feature selection ability, low risk of over- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m fitting, and excellent generalization ability. Through multiple trainings and evaluations, it has been confirmed that this model performs outstandingly when dealing with the task of Olympic medal prediction.

Based on the collected data of the 2028 Olympic Games, the trained Random Forest regression model is used for prediction. The model predicts the number of medals each coun- try will win in the Olympics based on features such as the level and quantity of athletes from

关注数学模型 each country, as well as the number of competition events. Due to space limitations, this paper only presents the prediction results of some countries. The specific prediction results are as follows (all values are integers):

Gold Silver Total Bronze

44 132 46 United States 42

96 China 40 30 26

69 25 30 14 Great Britain

20 16 56 Australia 20

Japan 11 46 19 16

From the analysis, it can be seen that in the prediction for the 2028 Olympic Games, the number of gold medals won by the United States will increase by 10%, and it will still rank first in the total number of medals. The number of gold medals won by China remains un- changed, but the total number of medals will increase by 5%. The number of gold medals won by Japan will decrease by 5%.

5.1.5 Confidence Interval

● ● To further evaluate the reliability and uncertainty of the model's predictions, this study also calculated the upper and lower limit intervals for the predicted medal counts of each country. By introducing the prediction interval, the upper and lower limits of each predicted value can be given, thereby indicating the possible range of the true medal count under a certain confidence level. The following figure shows the prediction results of some countries and their corresponding upper and lower limitintervals of the predictions. All values are integers.

Total Gold lower confidence bound lower confidence bound 138.9 Higher confidence bound 46.9 50 40 Higher-confidence-bound 42.6 30 45 20 40 104.2 125.1 10 35 42.1 38.4 D 00 30 22.1 25 20.4 90 99.8 72.9 15.8 20 80 15 70 59.6 17.6 17.9 12.2 10 60 48.8 65.1 5 50 52.4 40 0 China Great Britain Australia Japan United States United States China Great Britain Australia Japan

As shown above, introducing the prediction interval can present the possible range of each country's true medal count at a certain confidence level. This not only enhances the transpar- ency of prediction results but also offers more reliable information for decision-makers to eval- uate potential uncertainties and risks.

5.2  Prediction of First Medal Wins for Medal-less Countries

5.2.1 Model Preparation

(1) Determination of independent and dependent variables ⚫ Independent variables：

X The number of medal - less athletes （ ） 1 X The number of events participated in （ ） 2 The number of Olympic Games participated X （ ） in 3

⚫ Dependent variable:

Figure 9：Flowchart of part 2 of question 1

(2) Establish a Logistic regression model

[4]Logistic regression is a statistical model widely used for classification problems, mainly for binary classification . It linearly combines features and uses the Sigmoid function to map the result to a probability value between 0 and 1 to address binary classification issues. The model uses maximum likelihood estimation to optimize parameters and interprets the impact of features on the probability of an event occurring through regression coefficients. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The steps of Logistic regression are as follows: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Step1: Data preparation

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Collect a dataset that includes multiple features and a target variable , m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m which is a binary classification variable (0 or 1). Then standardize or normalize the data. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Step2: Define the Logistic regression model

Express the linear combination of input features as:

=  +  +  +  z X X X (2) 0 1 1 2 2 3 3

Map the linear combination to the interval [0, 1] through the Sigmoid function. The probability of the event occurring is 1 1 = = −= P ( Y 1 X ) (3) −  +  +  +  + ( X X X ) z 1 e e 0 1 1 2 2 3 3

Step3: Model training

Based on the training data, define the likelihood function of Logistic regression, which represents the probability of observing the data given the parameter :

m = − ( − Y 1 Y L ) P ( Y X ) 1( P ( Y X )) (4) i i i i i i = i 1

To simplify the calculation, take the logarithm to obtain the log-likelihood function:

  m   = + − − log L ( ) Y log P ( Y X ) 1( Y ) log( 1 P ( Y X )) (5) i i i i i i = i 1

关注数学模型 Estimate the parameter of the model by maximizing the log-likelihood function:

ˆ  =  arg max log L ( ) (6)

Step4: Calculate the predicted probability and make a classification decision For each sample in the test set, calculate the probability that its class is 1:

1 (ˆ = = P Y 1 X ) (7) ˆ ˆ ˆ −  +  + +  + ( X ... nX ) 1 e 0 1 1 n

Based on the probability value, classify the sample as 0 or 1, setting the threshold at 0.5:

𝑌̂ = {1, 𝑖𝑓 𝑃̂(𝑌= 1|𝑋) ≥0.5 (8) 0, 𝑖𝑓 𝑃̂(𝑌= 1|𝑋) < 0.5

5.2.2 Model results

微信公众号：数学模型 We trained the model using 10-fold cross-validation. The final regression model obtained is:

1 (9) (ˆ = = P Y 1 X ) − + + + + ( .0 006 .0 14 X .0 28 X .0 34 X ) 1 e 1 2 3

In a logistic regression model, the odds ratio is the ratio of the probability of an event occurring to the probability of the event not occurring, that is:

P = 1 (10) Odds − P 微信号：MATHmodels Solving based on the data, the results are as shown in the following table:

Team P Odds Whether to win a medal

Angola 0.81 4.26 1

EI Salvador 0.72 2.57 1

Honduras 0.69 2.23 1

Nicaragua 0.67 2.03 1

Calculations show that only the p-values of the above four countries are all greater than 0.5 and the odds ratios are relatively large. That is, these countries have a relatively high pos- sibility of winning their first medals at the 2028 Olympic Games. Among them, Angola has the largest p-value of 0.81, meaning it is the most likely to win its first medal.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

5.3 Analysis of Factors Influencing Country Medal Counts

5.3.1 Analysis of the Influence of Olympic Events

(1) Analysis of the Medal Distribution of Olympic Events for Each Country Based on Radar Charts To more intuitively display the medal distribution of each country in different Olympic events, this study uses radar charts as a visualization tool. Radar charts can effectively present multi-dimensional data and help compare the advantages and disadvantages of each country in various events. Taking the United States, China, and France as examples, the drawn radar charts are as follows:

The above figure shows the performance differences among China, the United States, and France in five Olympic events. China stands out in swimming, wrestling, and diving, with par- ticularly obvious advantages in diving and wrestling. The United States takes a dominant po- sition in track and field and swimming, demonstrating its strong competitiveness in multiple events. France shows a relatively balanced performance, with certain advantages in shooting and swimming. Overall, it reflects the differences in competitiveness of the three countries in their respective advantageous events.

关注数学模型 (2) Grey Relational Analysis Grey Relational Analysis quantifies the degree of association between different factors by comparing their changing trends[5]. It is particularly suitable for situations with incomplete in- formation or uncertainty. This method identifies key influencing factors or conducts pattern recognition by calculating the degree of association. In this study, the number of medals in each sports event is regarded as a subsequence, and the total number of medals of each country is 微信公众号：数学模型 regarded as the mother sequence. The degree of association between each event and the total number of medals of each country is calculated, and the strength of their correlation is meas- ured by the value of the degree of association.

The analysis steps are as follows:： Step1: Determine the mother sequence and subsequences Suppose there are evaluation objects and evaluation indicators. The mother sequence = = = = x x ( k ) k 2,1 ,..., n x x ( k ) k 2,1 ,..., m is , and the subsequences are . 0 0 i i Step2: Preprocess the variables Pre-process each indicator in the mother sequence and subsequences respectively. First, 微信号：MATHmodels calculate the mean of each indicator, and then divide each element in the indicator by its mean. This can eliminate the influence of dimensions and narrow the range of variables to simplify calculations. Let the standardized matrix be Z, and the elements in Z be denoted as , The calculation formula is as follows:

x i j = Z (11) i j x i j

Obtain the standardized matrix: Z   Z Z Z 11 12 1 m   Z Z Z (12)   21 22 2 m     Z Z Z   n 1 n 2 nm

Step3: Calculate the correlation coefficients between each indicator in the subse- quences and the mother sequence

+  a b (13) = = = y x k ( ( ), x k ( )) ( i 1,2, m k , 1,2, n ) 0 i − +  | x k ( ) x k ( ) | b 0 i

Among them, is the distinguishing coefficient, usually taken as 0.5. is the mini- mum difference of the two levels, and is the maximum difference of the two levels. The calculation formulas are as follows:

= − a min min | x k ( ) x k ( ) | (14) 0 i i k = − b max max | x k ( ) x k ( ) | 0 i i k Step4: Calculate the grey relational degree +  n n 1 1 a b (15)   = = y x x ( , ) y x k ( ( ), x k ( )) 0 i 0 i − +  n n | x k ( ) x k ( ) | b = = k 1 k 1 0 i

This study uses the grey relational analysis model to quantify the degree of association between each sports event and the total number of medals, and further explore their correlation. The following table shows the degree of association between some events and the total number of medals of some countries:

Athletics Swimming Diving Volleyball Triathlon

United 0.84 0.83 0.45 0.67 0.51 States

China 0.54 0.65 0.87 0.79 0.21

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Great m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 0.45 0.66 0.12 0.34 0.82 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Britain m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Australia 0.5 0.54 0.56 0.21 0.56 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Japan 0.44 0.32 0.45 0.45 0.11

By analyzing the above table, it can be seen that the United States has a high degree of association with track and field and swimming events, which are 0.84 and 0.83 respectively. This indicates that these two events are crucial to the number of its medals. China has the highest degree of association with the diving event (0.87), highlighting the dominant position of diving in its Olympic performance. The degree of association of the United Kingdom with the triathlon is 0.82, showing the significant impact of this emerging event on the total number of its medals. In contrast, Japan has a generally low degree of association with various events, indicating its relatively balanced overall competitiveness in multiple events.

5.3.2 Influence of the Events Chosen by the Host Country on the Results

(1) Visual analysis To visually display the changes in the medal performances of various countries in succes- sive Olympic Games, the following chart shows the number of medals of different countries in each Olympic Games. The horizontal axis represents the year of the Olympic Games, the ver- tical axis represents the number of medals, and each line represents the number of medals of a particular country.

关注数学模型 微信公众号：数学模型

From the graph, it can be observed that the total number of medals of the United States reached its peak in 1984, and this phenomenon is closely related to the fact that the Olympic Games were held in the United States that year. Similarly, China also achieved a record-high number of medals in 2008, reflecting the positive impact of the host status on its performance. In 2020, the total number of medals of France also reached its peak, which is inseparable from 微信号：MATHmodels Paris being the host city. Thus, it can be seen that the host status significantly promotes the medal performance of the host country in the Olympic Games.

(2) The potential impact of the United States' host status on its medal performance in 2028 The five new sports added to the 2028 Los Angeles Olympics - baseball/softball, lacrosse, cricket, squash, and flag football - will enhance the United States' medal potential. Baseball and lacrosse, as traditional strong suits of the United States, are expected to contribute a large number of medals. Although cricket and squash are relatively niche sports, their inclusion is expected to boost the United States' performance in these events. Flag football provides new opportunities for the young population, further increasing the United States' competitiveness in the Olympics.

6 The Study of a “Great Coach” Effect

6.1 Analysis of the “great coach” effect

6.1.1 Two-sample Mean Hypothesis Testing

To explore whether the "great coach" effect has an impact on Olympic medal performance, we selected the two-sample mean hypothesis testing method. This method is applicable for comparing whether there is a significant difference between the means of two independent samples. In this study, we defined the two samples as follows: one set of data represents the perfor-

mance before a great coach took charge, and the other represents the performance after the coach started coaching. By examining the differences in the number of Olympic medals between the two groups of countries, we can evaluate the potential impact of the "great coach" effect. Step1: Formulate hypotheses

Null Hypothesis H0 :µ1 = µ2 (16) Alternative Hypothesis H1 :µ1 ≠μµ2

Set the confidence level at 95%. Step2: Calculate the P – value According to the results of the hypothesis test, when the P-value is less than the set sig- nificance level, we reject the null hypothesis and conclude that the coach's coaching has a sig- nificant impact on the country's performance. If the P-value is greater than 0.05, it indicates that there is no significant change in performance before and after the coach takes charge.

For the convenience of statistics, we record the total number of medals as follows:

Total = 4× Gold + 2× Silver + Bronze We use SPSS for significance testing, and the results are shown in the following table (both Pre - coaching medals and Post - coaching medals in the table below are average values):

Pre-coaching Post-coaching Sport Coach Time Team P medals medals US 0.5 0.05 Volleyball 2005-2008 2 Lang Ping US 0.71 0.01 Gymnastics 1981-2016 3 Martha Karolyi CHI Volleyball 2013-2016 1.5 0.007 Lang Ping 4 JAP Béla Károlyi 2000-2012 1.16 0.09 2.67 Gymnastics

In the table, based on the analysis of the P - values, Lang Ping's coaching of the US wom- en's volleyball team and the Chinese women's volleyball team significantly increased the medal counts of both teams. The P - values are 0.05 and 0.007 respectively, indicating her significant influence. Martha Karolyi's coaching of the US gymnastics team also significantly increased the medal count, with a P-value of 0.01, demonstrating her significant contribution. Although Béla Károlyi's influence on the Japanese gymnastics team led to an increase, the P-value is 0.07, indicating that the change is not significant. This shows that the "great coach" effect has played a key role in some teams. 6.1.2 Chi-square Test The chi-square test is used to determine whether two categorical variables are related or independent[6]. By comparing the differences between the actual observed frequencies and the expected frequencies, if the p-value is significantly small, it indicates that there is a statistical association between the variables; otherwise, they are considered independent. In this paper, the frequency data of multiple categorical characteristics were analyzed, and contingency ta- bles were constructed for the test.

First, when analyzing whether there is a relationship between great coaches and the award results, take Coach Lang Ping's guidance of the Chinese team and the US team as an example, by organizing the award-winning situations of the Chinese and US women's volleyball teams in 2008 and 2016, the following two - dimensional contingency table can be obtained:

关注数学模型 Presence of an excellent coach Total Yes No 12 CHI 13 1 USA 4 5 1 Total 16 2 18 Set up the null hypothesis H0 : There is no relationship between the presence of a great coach and the number of medals won, that is, they are independent, which can be expressed as follows:

(17) H0 : pij = Pi.p.j Next, under the condition that the null hypothesis holds, the maximum likelihood esti- 模型 mates of each parameter can be obtained:

ni. (i = 1,2) pi. = (18) n n.j (j =1,2) p.j n Its test statistic is:

(nij −npij 2 x²=∑∑ (19) npij j=1 i=1 Finally, the calculated p-value is 0.009, which is less than the significance level of 0.05. There is sufficient evidence to reject the null hypothesis H0 . Therefore, it can be concluded that the guidance of a great coach has a significant impact on the award-winning situation of this event.

6.2 Contribution of “great coach" Based on the Logistic

1mc Input Ouput

Coaching duration of excellent coaches Coach Regression contribution coefficient Medals won in Trained logistic event history regression Event medal- Optimal winning investment probability event ● Number of event ● participants

In order to deeply explore the potential impact of "great coaches" on Olympic perfor- mance and provide guidance for countries in sports investment decisions, this study will use the Logistic regression model to test whether great coaches have significantly increased the medal counts of certain countries and explore the investment directions in which great coaches should be prioritized when different countries select sports events.

Let the coaching time of a great coach be x1 (if there is no great coach for a certain event, x1 = 0), the number of medals won in the history of this event be x2 (x2 has been converted.), 3x , and y be a 0 - 1 the number of athletes participating in this event for this country be variable indicating whether the sports event wins an award.

After substituting the standardized data into the logistic regression model and estimating the model parameters, the regression model is obtained as follows:

1 (ˆ = = P y 1 x ) − + + + + ( .2 12 4.14 x 7.25 x .1 98 x ) 1 e 1 2 3 (20) p = + + + ln( ) .2 12 .4 14 x .7 25 x .1 98 x 1 2 3 − 1 p A significance test was conducted on the regression coefficients, and the results are as follows:

Varible Standard Error P

Coaching Duration 4.14 0.67 0.04

Historical medal tally 7.25 0.91 0.006

Number of participants 1.98 0.39 0.05

As can be seen from the above table, the influence of the coaching time of a great coach on whether the sports event wins an award is significant, and it shows a positive correlation. Based on the values of the regression coefficients, it can be seen that the contribution of the coaching duration to the award-winning result lies between the level of the athletes in this event and the number of participating athletes.

6.3 Investment in “great coach”

We select China, the United States, and Japan as the research objects.

(1) Screen out the events in which each country has not won any medals in the past four Olympic Games.

We believe that the events that have won medals in the past four Olympic Games are already mature enough. We also believe that there is greater room for improvement in the events in which countries have not won medals in the past four Olympic Games, and these events are in more urgent need of the guidance of great coaches.

(2) Selection of investment projects 1x =4, input it into the trained Change the guidance time of the already selected events, set logistic regression model, and select the projects for investment by comparing the probabilities of these projects winning awards. Take the Chinese team as an example:

关注数学模型 According to the analysis of the logistic regression model, the men's volleyball event has the highest probability of the Chinese team winning an award. Therefore, it is recommended to prioritize investment in "great coaches" to increase the winning chances of this event. In contrast, the probability of the Chinese men's football team winning an award is relatively low, 微信公众号：数学模型 and it may not be the main investment direction.

For the United States, the probabilities of winning awards in badminton and table tennis events are relatively high. It is recommended to allocate "great coach" resources to these two events. The Japanese team should increase its investment in coaches for the swimming event to enhance its competitiveness and medal potential in this field.

7 Predicting Olympic Medals: Insights and Strategies

7.1 The Number of Participating Athletes and the Potential to Win Medals

微信号：MATHmodels The model demonstrates the impact of the number of participating athletes on the number of medals. More athletes mean more competition opportunities and potential medal opportuni- ties. Specifically, countries with a large number of participants, such as the United States and China, usually have strong competitiveness in multiple events.

National Olympic Committees can increase the overall number of medals by expanding the scope of athlete selection and increasing the number of participating athletes in certain events. Diversify the events of participation: In addition to traditional dominant events, Na- tional Olympic Committees can also encourage athletes to participate in more emerging or less popular events to increase the chances of winning awards in these events.

7.2 Medal Distribution of Different Countries in Various Events

We used the grey relational analysis model to reveal the medal distribution of different countries in various events. For example, the United States has a high degree of correlation with track and field and swimming events, indicating that these events have a significant impact on its total medal count; China has the highest correlation with the diving event, demonstrating the decisive role of diving in China's medal performance.

Based on this insight, countries can adopt the following strategies: ⚫ Concentrate resources: National Olympic Committees can use grey relational analysis to identify the events that contribute the most to their total medal count. Then, they can concentrate resources on training and selection in these events to enhance their competi- tiveness in them. ⚫ Invest in emerging events: At the same time, grey relational analysis can also help iden- tify those potentially overlooked and underdeveloped events, providing countries with more potential medal opportunities.

7.3 Set Advantageous Events

The advantages of the host country in the Olympic Games come not only from factors such as psychology, resources, and audience support but also from its influence on event set- ting, schedule arrangement and rule adjustment, which can further enhance this advantage.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m From the perspective of game theory, the status of the host country actually provides a unique strategic gaming opportunity for the host nation.

7.3.1 N-player game

In a multi-party game[7], the goal of each player is usually to maximize their own utility (such as winning more medals), and the strategic choices of each player will affect the outcomes of other players. Therefore, the overall outcome of the game depends not only on the strategy of each individual player but also on the combination of strategies of all players. This requires us to take into account the interaction of the strategies of each player during the analysis. Suppose there are multiple countries involved, in- cluding the host country and other participating countries. Each country has its own "strategy space", that is, choosing which events to compete for medals and maximizing its own interests (the number of medals) through strategic choices. Figure 15：N-Player Game Composition

7.3.2 The strategies chosen by the host country and

other countries ⚫ Strategies of the host country: The host country can create more medal opportunities in its own advantageous events. For example, it can increase the number of matches in certain competitions or optimize the competition format to enhance the probability of its own ath- letes winning medals. The host country can also use its control over the schedule to reduce the competition pressure on foreign athletes or increase the training time for its own ath- letes.

Strategies of other countries: Other countries will decide their investment in certain ⚫ events based on the choices made by the host country. If the host country dominates in certain events, other countries may choose to avoid these events and instead allocate more resources to other events, especially those in which the host country may not have an edge.

7.3.3 Nash Equilibrium

Ultimately, this game will tend towards an equilibrium state[8]. In this state, each country's strategy reaches its best response strategy. That is, considering the choices of other countries, neither the host country nor other participating countries can increase their medal counts by unilaterally changing their own strategies. Under this equilibrium, the strategic choices of countries will influence each other and jointly determine the final medal distribution.

8 Sensitivity Analysis and Error Analysis

8.1 Sensitivity Analysis

We examined the sensitivity of the classification results by changing the number of folds for cross-validation of the logistic regression model. The number of folds for cross-testing is set to be 8, 9, 10, 11, respectively. The coefficient of variation of the classification results is detected to judge whether the model is robust or not.

Introducing the coefficient of variation , define：

关注数学模型  (21)  =  Where  represents the accuracy of the model cross-validated at 10 fold of the original scheme， indicates the absolute value of the change in the accuracy rate after changing the number of folds.

coefficient of variatio  Cross-checking Folds 8 5% 微信公众号：数学模型 9 0 11 3.46% From the above table, we can see that changing the number of cross folds changes the accuracy of the trained model within 5%, which indicates that the change in accuracy is not significant. Thus, this model is robust.

8.2 Error Analysis

In order to assess the prediction accuracy of the Random Forest regression model used in this study, a detailed error analysis was performed. By analyzing the performance of the model 微信号：MATHmodels on the test set, it is possible to get a better understanding of the generalization ability and sta- bility of the model under different conditions. And in this section, the error of the model is presented through visual graphs.

Firstly, we assessed the prediction accuracy of the model by plotting the true values of the test set against the fitted values of the model as follows：

Figure 16：Comparision of test set prediction results

As can be seen from the figure, the model performs relatively accurately in predicting the number of medals for most countries, with small errors between the true and fitted values. However, some countries have relatively large prediction errors, which may be related to the characteristics of some specific events, data noise, or underfitting of the model to some varia- bles.

To further analyze the performance of the Random Forest regression model, we explored the effect of the number of decision trees on the model error. We plotted the relationship be- tween the number of decision trees and the error as follows：

Figure 17：Plot of the relationship between the number of decision trees and error

It can be observed from the figure that the error of the model gradually decreases as the number of decision trees increases, indicating that more decision trees help to improve the stability and accuracy of the model. When the number of decision trees reaches a certain value, the decrease of the error tends to level off, indicating that the fitting ability of the model is close to saturation at this point, and further increasing the number of decision trees has a limited effect on the improvement of the error.

9 Strengths and Weaknesses

9.1 Strengths

⚫ The model we proposed makes full use of official data and analyses the data in depth, and the results of the study are highly informative and can be applied to future predictions about Olympic medals. ⚫ Random forests are more accurate, robust, and less prone to overfitting, and are used to predict the 2028 Olympic medal table with less error. ⚫ We use logistic regression to predict the probability of first-time winners for non-winning countries, taking full account of relevant factors, and is relatively robust to outliers, with reliable results. ⚫ The use of two-sample mean hypothesis tests and chi-square tests to simultaneously ana- lyse the “great coach” effect reduces chance error and produces convincing results.

9.2 Weaknesses

⚫ The model we presented is very comprehensive in its consideration of the problem indi- cators, but the lack of data for some of the indicators may make the results subject to some errors.

关注数学模型

10 Conclusion

We performed a multi-dimensional analysis of factors affecting Olympic medal counts and developed a machine learning prediction model. Key factors such as athlete performance, event types, host status, and participation were found to influence medal outcomes. The Ran- dom Forest regression model demonstrated high accuracy, with predictions for the 2028 Olym- pics indicating continued dominance by the U.S. and China, while Japan's gold medal count may decline.

Grey correlation analysis reveals performance differences across disciplines, helping countries identify competitive areas. The study emphasizes the impact of host status on medal 微信公众号：数学模型 counts, particularly for the U.S. at the 2028 Los Angeles Olympics, where new sports may boost medal potential. Overall, the findings offer a scientific basis for the Olympic Committee to optimize training and resource allocation strategies.
