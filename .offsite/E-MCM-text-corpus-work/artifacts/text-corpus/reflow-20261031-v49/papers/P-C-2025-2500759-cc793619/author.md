MCM/ICM

Summary Sheet

Summary

To ensure a systematic and multidimensional approach to Olympic medal prediction, this study constructs a dynamic and coupled comprehensive prediction framework. This framework integrates various objectives, including medal distribution prediction, break-

through country identification, event performance evaluation, and the impact analysis of coaching resource allocation. By employing multi-source heterogeneous data fusion and machine learning integration methods, we achieve an in-depth analysis and reliable pre- diction of the development patterns in competitive sports.

First, we develop a multidimensional predictive model to analyze Olympic medal patterns. Utilizing Principal Component Analysis (PCA) for dimensionality reduction and noise filtering of the Olympic event dataset, we combine Long Short-Term Mem- ory (LSTM) networks to mine temporal features and integrate home advantage effects. A dual-channel XGBoost-Bootstrap model is established to generate predictions with a 95% confidence interval. The results indicate an upward trend for countries such as

the United States and the United Kingdom, while countries like France and China show a decline. The model has a low MAE and MAPE, exhibiting a high accuracy and strong ro- bustness. Through non-parametric testing, potential breakthrough countries are identified, with San Marino and Kuwait showing gold medal breakthrough probabilities of 84.7% and 68.4%, respectively. Event analysis reveals a strong correlation between swimming, athletics, and medal counts, while SHapley Additive exPlanations (SHAP) quantifies shooting as a core contributing event. Principal component analysis uncovers the positive driving effects of swimming and wrestling on medal augmentation, informing optimal sports event allocation.

Subsequently, we develop a Difference-in-Differences (DID) model to quantify the competitive benefits of coaching replacement and conduct statistical significance tests as well as parallel trends tests to ensure the reliability of our results. It is found that during the 2020-2024 period, Australia, South Korea, and Poland experienced significant "great coach" policy effects through strategic restructuring of their coaching teams. Based on this, we recommend prioritizing investment in high-elasticity projects.

Finally, we synthesize all models and analyses to present new insights and corre- sponding decision supports.

Introduction

3 1.1 Problem Background· 1.2 Clarifications and Restatements 1.3 Our Work· 3 2

Preparation for Modeling

2.1 Model Assumptions. 3 2.2 4

Notations

Data Preprocessing 2.3 4 3 Problem 1: Medal Prediction 5 Medal Ranking 5 3.1 PCA: Reducing Dimensions 3.1.1 5 3.1.2 LSTM: Trends Based on Time. 6 3.1.3

XGBoost-Bootstrap Modeling

Results Display

9 3.1.4 3.2 Breaking the Zero 10 3.3 13 Olympic Events and Medal Counts.

13 3.3.1 Spearman: A Mathematical Analysis 3.3.2 14 3.3.3 15 Analysis of Relationships and Importance Problem 2: The "Great Coach" Effect . . 18 4

4.1 DID Modeling

18 Hypothesis Testing and Contribution Coefficient Analysis 19 4.2 19 5

Sensitivity Analysis

21 6 21 6.1 The Number of Principal Components 21 6.2 Prediction Model Evaluation· 22 7

Model Analysis

22 7.1

Strength · ·

Weekness and Further Discussion·

23 7.2 Memorandum.. 24 8

1 Introduction

1.1 Problem Background

The medal standings of the 2024 Paris Summer Olympics illustrate the diversity of international sports competition: the United States led with 126 total medals, while China tied for the gold medal count. The host nation, France, underscores the advantages of hosting by securing the fourth position in total medal accumulation. Emerging powers such as Albania have achieved their first gold medal, whereas over 60 countries have yet to register any medals, reflecting the uneven distribution of competitive resources. 微信公众号：数学模型 Current predictions largely rely on pre-competition data6; however, key variables such as historical trends, adjustments to events, and coaching effects have not yet been adequately quantified. By constructing data-driven models2, it becomes possible to accurately iden- tify potential medal-winning events, optimize coaching resources, leverage host country advantages, and reveal the pathways to the emergence of "invisible champions". This ap- proach provides dynamic insights that can aid nations in formulating strategies and foster a rebalancing of the Olympic landscape.

1.2 Clarifications and Restatements

Given the background information and constraints of the problem, we must complete 微信号：MATHmodels the following tasks:

Task 1: Develop a model to predict gold and total medal counts for each country at the 2028 Los Angeles Olympics and compare predictions with the 2024 Paris Olympics. Task 2: Identify countries expected to win their first medals at the upcoming Olympics using the model from Task 1, and estimate the likelihood of a "zero breakthrough". Task 3: Analyze the relationship between Olympic sports and medal counts, considering the impact of the host nation and selected sports. Task 4: Create a model to identify countries with the "great coach" effect in specific sports and provide contribution coefficients. Task 5: Based on the topic and the work conducted, additional original insights are pre- sented.

1.3 Our Work

First, dimensionality reduction is performed using PCA. Next, trend information is incorporated through LSTM, leading to the establishment of an XGBoost prediction model. Subsequently, the Wlicoxon signed rank test is employed to investigate which countries achieve a breakthrough in winning their first medals and to determine the cor- responding probabilities. Furthermore, Spearman correlation coefficients and SHAP are utilized to conduct relationship and importance analyses. Finally, a DID approach is ap- plied to examine the "great coach" effect and provide new insights. For ease of description and visualization, we have drawn Fig. 1 to represent our work.

2 Preparation for Modeling

2.1 Model Assumptions

Some fundamental assumptions are listed below.

• Assumption 1: Athletes are in optimal physical condition throughout the competi- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m + +

Prepare Task 2 Task 1 Data collection Prediction Intervals for Gold and Medal Counts in the 2028 Olympics Probability Estimation Data pre-processing for à "Zero PCA for Redundant Breakthrough" LSTM for Trend XGBoost-Bootstrap Feature Elimination Prediction Model Incorporation P-value for Assessing Achie vement and Estimating Accuracy and Robustness Assessment of the Prediction Model Probability Left-sided Rank Sum Test 10-Fold Cross-Validation Evaluation Me trics & - R-squared Line Plot with Location Parameter (RMSE, MAE, etc.)

Theta - 1

Y + + Final Task 3 Task 4 &5 Cross fusion Advice for Corre lation and IOC Importance Analysis New DID Model Spearman's Correlation Insights Coefficient & SHAP Analysis Tools

tion and their performance is solely influenced by competitive factors.

→ Justification: We assume that athletes will compete in peak condition, with per- formance primarily driven by training and competition, excluding factors such as injuries or external disturbances.

• Assumption 2: A country's past Olympic performance is a reliable indicator of future medal counts, and the host country tends to perform better due to home-field advantages.

→ Justification: We assume that historical performance reflects long-term trends in national sports development, and that host countries benefit from support from local spectators and familiarity with the competition environment.

2.2 Notations

Symbol

Definition Each country's home advantage coefficient αc pi The host advantage coefficient β₀ Intercept, the baseline medal count for the control group β1 The difference between the treatment and control groups β2 The overall change in medal counts from 2020 to 2024 β3 Contribution coefficient Xit Control variable matrix Coefficient of Xit γ Random error term €it Prept The preparatory period effect Threati Dummy variable indicating coach change, 1 if changed, 0 otherwise Post Time dummy variable, 1 if the Olympic year is 2024, 0 otherwise

2.3 Data Preprocessing

Overviewing the five attachments provided in this study, "data_dictionary", etc and synthesizing the information regarding medal predictions, event counts, and types,one

关注数学模型 can observe that the scale of information constitutes a small dataset. However, the data is lengthy and complex, with intricate relationships among different data points, represent- ing a type of data pertinent to decision-making in real-world scenarios.

• For attachment 2, we will perform a natural join with the "summerOly_medal_counts" dataset to match the columns for country names and their abbreviations, thereby en- hancing the information provided.

• During the data aggregation process, we will retrieve and consolidate data from attachment 2 based on the fields "Team," "Year," "Sport," and "Medal," calculating the medal counts for each country in every Olympic event. Furthermore, we will merge and compute data for various sports across different years, thereby deriving the types and counts of events for each Olympic Games, which will provide vital 微信公众号：数学模型 data support for subsequent medal predictions and trend analysis.

• For attachment 5, we will address missing values in the columns "Code," "Sports Governing Body," and "Year" through interpolation methods and by removing rows or columns that contain missing values.

3 Problem 1: Medal Prediction

This study focuses on predicting medal counts for the 2028 Los Angeles Olympic Games. By considering the interval prediction of medal rankings and recognizing the memoryless characteristic of Olympic medal trends akin to Markov chains, we employ an 微信号：MATHmodels innovative XGBoost5 algorithm enhanced by PCA8,9 and LSTM3,7 to model predictions for gold and total medal rankings while assessing model uncertainty. Using the PCA- LSTM-enhanced dataset from 2024, we derive predictive intervals for the gold and total medals by country for 2028, facilitating performance prediction analysis.

In terms of predicting the probability of nations "breaking the zero" for gold medals, we analyze the interval prediction results from XGBoost. We perform a symmetric rank sum test on Bootstrap samples where point estimates are greater than or equal to 1, con- cluding that countries with a P-value less than 0.05 are likely to achieve at least one gold medal in 2028.

Additionally, we examine the correlation and importance of different Olympic events in relation to countries’ medal counts. We start with a Spearman correlation analysis be- tween gold and total medal counts for each country in 2024 and the weighted values of key Olympic events. Building on our PCA-LSTM-enhanced XGBoost model, we utilize SHAP analysis to assess the importance of each sport based on principal component im- portance values. Univariate dependence plots further explore the relationships between individual sports and overall gold and medal counts, while SHAP force plots provide insights into the interrelationships and significance of different sports within nations re- garding their gold and total medal counts.

3.1 Medal Ranking

3.1.1 PCA: Reducing Dimensions

In predicting Olympic gold medals and rankings, outcomes are closely linked to the medal counts and compositions from previous Games. Thus, we weighted the gold, silver, and bronze medals of each country in major sporting events at 50%, 30%, and 20%, respectively, to assess their potential impact on future medal standings. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Principal Component Analysis (PCA) was employed to reduce the dimensionality of the weighted medal count dataset across 45 sporting events. This approach effec- tively addresses multicollinearity among original metrics by utilizing uncorrelated prin- cipal components, thereby eliminating redundancy and improving the convergence speed and accuracy of subsequent algorithms. Subsequently, Figs. 2(a)-(b) illustrate the first two dimensions of the PCA results.

(a) (b)

In the five-dimensional principal components, the cumulative variance contributions reach 76.4%, effectively capturing most characteristics of the original data. This indicates that data can be reduced to five dimensions for analysis. Fig. 2(b) shows that shooting has the highest score on the principal components, indicating its significant influence among events. Following shooting, swimming, athletics, and wrestling also exhibit no- table medal weights. The remaining events cluster distinctly, likely due to their correlated medal weights. Collectively, swimming, athletics, wrestling, shooting, rhythmic gym- nastics, boxing, and diving significantly impact PC1, suggesting it represents a principal component for major sports. Conversely, the other components (PC2 to PC5) are influ- enced by fewer variables. This analysis yields five principal component characteristics regarding medal weights of sporting events at the 2020 Olympics through PCA dimen- sionality reduction.

3.1.2 LSTM: Trends Based on Time

Predicting the Olympic medal tally can be framed as a time series forecasting prob- lem, as countries’ medal counts show temporal continuity. Strong sports powers often maintain high medal counts, while emerging nations may experience short-term break- throughs. Thus, the model must capture patterns and long-term trends across different Olympic Games.

LSTM is advantageous for handling long-range dependencies in time series data. For instance, if a country’s medal count has steadily increased over the last three Games, LSTM can identify this trend to predict further increases. The four-year gap between Olympics makes traditional models less effective; however, LSTM’s gating mechanisms help retain essential historical information, improving prediction accuracy.

Additionally, Olympic medal data can be noisy, with some countries showing incon- sistent performances. LSTM mitigates this noise by learning broader trends. It can also incorporate extra features like host country metrics to enhance predictions. To tackle data m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m sparsity, especially for smaller nations with limited data points, we have implemented a m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m regularization technique. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The process of constructing the LSTM model is as follows. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 • Feature design Each country's home advantage coefficient αc is estimated through regression based on historical data, normalized to serve as weights:

Goldhost t − Goldavg (1) C αc 二 Goldavg

A binary variable Hostt ∈ {0, 1} is utilized to indicate whether the country is the host for the year t. A preparatory period effect is introduced to capture the impact of increased investments during the preparation phase:

if t ∈ [thost − 8, thost] 1 Prept = (2) otherwise 0

where thost denotes the year of hosting, and 8 is equivalent to two Olympic cycles.

• Input feature reconstruction The input vector for each time step is expanded to:

(3) xt = [Goldt, Totalt, Host, Prept, αc]

• Time series modeling and feature fusion A dual-channel LSTM structure is employed to separately process the medal se- quence and home advantage features, with a final fusion for prediction: C4a) ● (1=x [-l (])   = o 1nsteps host = LSTMhost ([Host_k, PrePt−k,αc]k=1) 1nsteps (4b) Ît = FC (hmedal ⊕ hhost) (4c)

where nsteps = 3, represents using data from the last three Olympics.  represents vector concatenation, FC denotes a fully connected layer and Ît is the predictions.

• Loss function and joint optimization A hierarchical loss function is designed to constrain medal predictions and home advantage identification separately:

L = λ1Lmedal + λ2Lhost (5a) N ∑((yGld 1 ygold 2 + (yTotal 1− yTotal 2) Lmedal (5b) N ● i=1 N 1 (5c) Lhost

where λ1 = 0.7, λ2 = 0.3, pi = 0.1.

In the tuning process for the LSTM model, we primarily focused on two parame- ters: the number of neurons in the hidden layer (hidden_size) and the number of epochs allowed for early stopping (patience). We employed WMAE_Gold and WMAE_Total (Equation 6) as comparative metrics, starting with a constant hidden_size to conduct our comparisons. As illustrated in Figs. 3(a) and 3(d) (circle is the minimum of error), the optimal configuration is 32×6. Figs. 3(b) and 3(e) indicate that both 64×8 and 64×10 meet the objective; however, in Fig. 3(b), the model with 64×8 demonstrates a more sig- nificant reduction in error compared to the other parameter settings, leading us to select 64×8. Figs. 3(c) and 3(f) reveal that 128×10 exhibits the best performance.

Subsequently, we conducted a direct comparison of these three models. As shown in Fig. 4, the performance of the configurations 32×6 and 128×10 is quite similar; nonethe- less, the overall error for 128×10 is lower. Therefore, we ultimately determined the pa- rameters to be hidden_size=128 and patience=10. This selection provides critical trends measures for subsequent research involving XGBoost.

P wc|yc −ˆyc| P wc WMAE_Gold or Total = (6)

where wc is the weight of country c’s gold medals or total medals, yc is the true and ˆyc is the prediction.

(a) (b) (c)

(d) (e) (f)

关注数学模型

3.1.3 XGBoost-Bootstrap Modeling

Based on the aforementioned PCA dimensionality reduction and LSTM trend mea- surement, we obtain the input data for XGBoost. Subsequently, we construct XGBoost prediction models based on gold medal counts and total medal counts, respectively. A key aspect of this model (Fig. 5) is the construction of a relatively optimal XGBoost model through 10-fold cross-validation grid parameter tuning, along with the estimation of con- fidence intervals for medal prediction values using the Bootstrap resampling strategy.

微信公众号：数学模型 微信号：MATHmodels

XGBoost is an ensemble learning algorithm based on gradient-boosted trees, which centers on the incremental and parallel optimization of the loss function by constructing multiple CART base classifiers. It employs a second-order Taylor expansion of the ob- jective function, enhancing the efficiency of gradient descent while incorporating regular- ization into the objective function to effectively prevent model overfitting. This algorithm aims to leverage these features to elucidate the nonlinear relationships among gold medal counts, total medal counts, home advantage, weighted values for individual sport medals, and medal trend values. The objective function is Equation 7.

n K X X L(θ) = l(yi, ˆyi) + Ω(fk) (7) i=1 k=1

where l(·) is the loss function, Ω(·) is the regularization term.

Bootstrap is a non-parametric resampling method. By employing this approach, we independently run the constructed XGBoost model 1,000 times, allowing us to calculate the 95% confidence interval for each country’s fitted values of gold and total medals based on these iterations.

3.1.4 Results Display

The hyperparameter tuning of the predictive models employed RMSE as the evalua- tion criterion, aimed at selecting the model with the minimum RMSE value (see section 6.2 for a detailed analysis). During the training of the gold medal prediction model, the optimal combination of model parameters was determined through hyperparameter tun- ing, yielding: nrounds = 75, max_depth = 2, eta = 0.1, gamma = 0.5, colsample_bytree = 1, min_child_weight = 1, and subsample = 0.5. Notably, the subsample parameter re- mained constant throughout the tuning process, set at 0.5 to ensure a reasonable sampling proportion.

In the training process of the medal prediction model, the only change compared to the gold medal prediction model was the adjustment of the gamma parameter. In this model, the gamma value was set to 0.25 to optimize the model’s predictive ability for the number of medals. Consequently, the relatively optimal XGBoost model was utilized to perform Bootstrap resampling and interval estimation for "the trend values of gold and medal counts for various countries in 2028", "the five principal component dimensions of medal weights for various sports in 2024" and "the estimated home-field effect values for 2028." The results for the top 20 countries in both gold medal counts and total medal counts for the 2028 Los Angeles Olympic Games are illustrated in Figs. 6(a)-(b).

(a)

(b)

Based on Figs. 6(a)-(b) and Table 2, it can be observed that as the host country, the United States is projected to see a significant increase in both gold and medal counts for the 2028 Olympic Games. Additionally, countries such as the United Kingdom, Australia, Canada, and Cuba may also experience an increase in their respective gold and medal counts. In contrast, France, the host of the 2024 Olympic Games, is expected to achieve unprecedented results due to home-field advantage, but model predictions suggest that its gold and medal counts will notably decrease in the subsequent Olympic Games. Similarly, countries like China, Italy, South Korea, Japan, and Uzbekistan are also likely to perform poorly in the next Olympic Games.

3.2 Breaking the Zero

Based on the aforementioned analysis and the criteria for achieving a "breakthrough of zero," we identify the countries projected to achieve at least one gold medal in the 2028

关注数学模型 Gold Total

NOC Gold_Pred CI_95% Trend NOC Total_Pred CI_95% Trend

↑ ↑ USA 51 (32.08,58.34) USA 133 (79.60,147.35) ↓ ↓ CHN 34 (23.33,40.19) CHN 90 (59.13,103.51) ↑ ↑ AUS 19 (10.41,16.13) GBR 69 (43.12,75.84) ↓ ↓ JPN 17 (11.88,18.80) JPN 55 (38.19,64.94) 微信公众号：数学模型 ↑ ↑ GBR 16 (11.92,19.12) AUS 49 (33.37,63.77) ↓ ↓ FRA 12 (9.00,14.86) FRA 41 (29.86,60.60) ↓ ↑ GER 12 (8.41,14.38) NED 34 (24.58,39.30) ↓ ↓ ITA 11 (7.06,13.03) GER 33 (25.18,48.98) ↓ ↑ NED 11 (6.84,13.18) CAN 29 (21.72,33.68) ↑ ↓ NZL 11 (4.82,9.33) ITA 29 (22.58,34.13) ↑ ↓ CAN 10 (5.73,11.70) KOR 25 (18.08,34.28) ↑ ↑ HUN 8 (5.18,10.87) BRA 21 (14.67,24.32) ↓ ↓ KOR 7 (5.69,9.38) NZL 18 (13.98,23.86) ↓ ↓ BRA 6 (3.70,8.06) HUN 17 (13.00,22.69) ↓ ↑ ESP 5 (3.08,6.72) CUB 15 (10.91,18.57) 微信号：MATHmodels ↑ ↓ UKR 5 (3.39,7.88) ESP 14 (8.84,19.47) ↓ ↑ KEN 5 (2.51,6.01) SWE 12 (7.06,14.99) ↑ ↓ CUB 4 (2.36,5.92) UZB 11 (8.45,13.61) ↓ ↓ UZB 4 (1.96,5.83) KEN 9 (7.63,14.35) ↑ ↓ TPE 4 (2.79,4.53) UKR 9 (6.96,11.12)

Olympics as MKD, BFA, TKM, KSA, SMR, and KUW. We will conduct a signed rank test on the point estimates derived from Bootstrap resampling for these countries to sta- tistically assess whether they can achieve this gold medal breakthrough. The significance of these observations will be further elucidated by considering the size of the P-values, which indicate the probability of the events occurring.

The decision to utilize the signed rank test, rather than employing a one-sample t-test or defining a binary variable for "having won a gold medal" to apply logistic regression or binary classification machine learning algorithms, is based on the following consider- ations.

• The signed rank test is a non-parametric method that does not require any assump- tions regarding the distribution of the underlying population. In contrast, the t-test is a parametric method that assumes that the data originate from a normally dis- tributed population or that the sample itself is normally distributed. As such, the non-parametric test is more aligned with real-world scenarios, thus minimizing the likelihood of substantial errors.

• Implementing a binary variable for "winning a gold medal" to design a classification algorithm and calculate the estimated probability of countries achieving a "break- through of zero" would replace the quantitative variable of gold medal counts with a qualitative variable. This approach neglects the correlation between feature vari- ables and may lead to biased and unreasonable results.

Given the analysis outlined above, we will employ the signed rank test to statistically determine the significance of the gold medal breakthrough and to provide probability m m m m m m m m m m m m m m m estimates. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1) Hypothesis testing setup Let dij represent the i-th Bootstrap prediction value for the j-th country, and θj denote the symmetric center of the corresponding population. When the final prediction value ˆyj ≥1, we establish a left-sided signed rank test with a location parameter of 1:

H0 : θj = 1 H1 : θj < 1 vs.

2) Data transformation and statistic construction We perform a shift transformation on the original data d∗ ij = dij −1. Next, we compute the absolute value ranks R+ ij<0}(d∗ ij and the indicator variable: uij = I{d∗ ij). After excluding data points where d∗ ij = 0, we construct the signed rank sum statistic:

nj X w+ uijR+ j = ij i=1

where nj is the adjusted effective sample size.

3) Asymptotic distribution theory Under large sample conditions, when the null hypothesis is true, wj follows a normal distribution:

L w+ H0 N(µj, σ2 −→ j) j

µj = nj(nj + 1) 4 Pk i=1(t3 i −ti) j = nj(nj + 1)(2nj + 1) σ2 − 24 48

4) P-value calculation ! w+ j −µj P-value = Φ σj

If the P-value is less than or equal to 0.05, falling within the rejection region, it is concluded that the country is statistically unable to achieve a "breakthrough of zero" in gold medals at the 2028 Olympics. Conversely, if the P-value is greater than 0.05, it suggests that the country has a favorable chance of achieving a "breakthrough of zero" in gold medals. Furthermore, a larger P-value indicates a smaller probability of committing a Type II error, thereby increasing the likelihood of realizing the "breakthrough of zero" in gold medals. Based on the model established above, the results of the Wlicoxon signed rank test for the countries aiming to achieve this "breakthrough of zero" in gold medals are illustrated in Fig. 7 and Table 3 .

Based on the Table 2 and the gold medal counts from participating countries in 2024, it was determined that eight countries, which did not secure any gold medals in 2024, may potentially achieve a breakthrough in gold medals by 2028. Historical data shows that GHA and GRD achieved a breakthrough of zero gold medals in 1960 and 2012, respectively.

From Table 3, we can know only two countries, SMR and KWT, had test statistics corresponding to P-values greater than 0.05, indicating that they did not fall within the

关注数学模型 微信公众号：数学模型

w+ NOC p pred

GRD 538231 1 1 GHA 532048 1 1 SMR 498067 0.847 2 KWT 389859 0.684 1 SAU 222158 0.0011 1 TKM 197115 3.01e-09 1 MKD 153243 1.22e-26 1 微信号：MATHmodels BFA 153243 1.22e-26 1

rejection region. This suggests that the predicted gold medal counts for SMR and KWT at the 2028 Olympics are significantly greater than 1, implying that both countries are likely to achieve a “breakthrough of zero” in gold medals, with probabilities of 0.847 and 0.684, respectively.

According to Table 3, the predicted gold medal count for SMR at the 2028 Olympics is 2, with a 95% approximate confidence interval of [1, 3], indicating relatively stable predictions. For KWT, the predicted gold medal count is 1, with a 95% approximate confidence interval of [0, 2]. The violin plot in Fig. 7 illustrates that most of the prediction data for KWT falls within the range of 1 to 2.

3.3 Olympic Events and Medal Counts

We have chosen to utilize SHAP1,10 analysis tools for the correlation analysis and importance measurement between Olympic events and medal counts.

3.3.1 Spearman: A Mathematical Analysis

The Spearman correlation coefficient is a non-parametric measure of rank correla- tion. In contrast to the Pearson correlation coefficient, which is limited to characterizing linear relationships and requires data to follow a normal distribution, the Spearman corre- lation is computed based on rank orders. This approach makes it less sensitive to outliers and allows for a more robust representation of the degree of correlation between variables.

The Spearman correlation coefficient is defined mathematically as follows:

n 1     X R(xi) −R(x) R(yi) −R(y) n i=1 ρ = (8) v v n n u u t1 t1 2 2   X X u u R(xi) −R(x) · R(yi) −R(y) n n i=1 i=1

where R(·) denotes the rank of the variable within the sample.

Coming up with hypotheses:

H1 : ρ̸ = 0 H0 : ρ = 0 vs.

The t-test statistic is constructed, and a judgment is made using the rejection region:

|ρ| H0 ∼t(n −2) t = r ρ2 n −2 t > tα(n −2)   m m m m m m m m m m m m m m m m m m m m m m w = (x, y) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Significance t-test is typically conducted at a significance level of 0.05. In this study, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m we calculate the Spearman correlation coefficients and conduct hypothesis testing based m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m on the weighted values of the various sports in the 2024 Paris Olympics in relation to m m m m m m m m m m m m m m m m m m m m m m m m m

the number of gold medals and total medals won by each country. This analysis aims to explore the interrelationships between the different sports and their respective gold and medal counts from a mathematical perspective.

3.3.2 SHAP: Revealing Correlations and Importance

SHAP is a game theory-based tool that enhances the interpretability of machine learning models. Its core advantages lie in providing consistent, precise, and fair expla- nations. The rationale for selecting SHAP analysis tools to examine the interrelationships and importance of each sport in relation to various countries is as follows:

• Explanation of predictive models The fundamental function of SHAP is to compute the contribution of each feature to the final prediction outcome while also indicating the direction of this contribu- tion—positive or negative. Utilizing the beeswarm plot and importance plot, SHAP allows for the quantification of each sport’s significance regarding the number of gold and total medals won, in conjunction with the PCA loading matrix.

• Nonlinear processing and feature dependencies SHAP can reveal the nonlinear relationships of each feature within the XGBoost model when multiple features interact. It provides accurate contribution scores for each feature, with univariate dependence plots illustrating the impact of different sports’ principal components on gold and medal counts.

• Local and global explanations In addition to the aforementioned analyses, SHAP provides local explanations for

关注数学模型 individual samples, allowing for a detailed examination of the degree of contribu- tion from each feature. This facilitates an in-depth analysis of the associations be- tween different sports and various countries. Specifically, by leveraging the SHAP force plot for a single sample, one can observe which sports primarily influence the medal counts of a particular country.

3.3.3 Analysis of Relationships and Importance

Based on the formula for the Spearman correlation coefficient and hypothesis test- ing, sports with non-significant correlation coefficients, such as Wrestling, Beach Volley- ball, Handball, Trampoline Gymnastics, and Cycling, were excluded. Fig. 8 illustrates 微信公众号：数学模型 the correlation between gold medals, total medals, and various sports for the 2024 Paris Olympics.

微信号：MATHmodels The Spearman correlation analysis reveals several key insights: Sports such as Swim- ming, Athletics, and Shooting demonstrate a strong relationship between gold and total medals, primarily due to their multiple events that enhance medal potential, with strong nations particularly excelling in Swimming and Athletics. Conversely, team sports (e.g., Basketball, Volleyball) and some group sports (e.g., Rowing, Canoeing) exhibit weaker correlations between gold and total medals, as their gold counts are less concentrated despite higher total medal counts attributed to broader participation across nations. Addi- tionally, newly introduced sports like Skateboarding and Karate showcase a lower corre- lation for gold medals (0.210) but a higher correlation for total medals (0.496), indicating a more dispersed gold distribution alongside increased total medals. The growth of these sports likely stems from greater participation and competition, contributing to a more equitable medal distribution overall.

The XGBoost prediction model for gold and total medals at the 2028 Olympics, constructed previously, calculates SHAP values based on the training set, resulting in the hexagonal importance mix plot in Fig. 9 for five principal component features. In the gold medal prediction model, the two most important principal components are PC1 (0.8345) and PC2 (0.1055). For the total medal prediction model, the leading components are PC1 (0.6242) and PC5 (0.3024), aligning with the highest variance contribution from PC1. The absolute values of the loadings of individual items on the principal components are then weighted by the importance of the components, summed, and normalized to calculate their significance, as shown in Fig. 10.

The PCA and SHAP analysis reveals important insights into sports. Shooting and Gymnastics rank among the top three in gold and total medal significance, emphasizing their vital Olympic roles. Shooting’s diversity and Gymnastics’ strong participation from countries like the USA and China contribute to their rankings. Swimming ranks third in m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

(a) (b)

gold importance (0.9039) due to its variety and competition. Table Tennis, while lower in gold importance, is second in total medals (0.95), reflecting its global popularity and China’s dominance. Diving and Wrestling also hold significance, with Diving showcasing China’s strength.

Next, we will create univariate dependence plots for PC1, which has the highest SHAP importance. This analysis will illustrate the nonlinear relationship between PC1 and medal counts, highlighting contributions from sports such as Swimming, Athletics, Wrestling, Gymnastics, and Basketball.

In the gold medal prediction model (Fig. 11(a)), the negative region of PC1 is closely associated with sports that have high loadings, such as Swimming, Athletics, Wrestling, Gymnastics, and Basketball, which perform well when PC1 is negative, significantly con- tributing to the gold medal count. The upward trend in the dependence plot indicates that outstanding performances in these sports lead to a considerable increase in gold medals, highlighting their crucial impact, particularly in the negative PC1 area. As PC1 turns positive, their influence diminishes, demonstrating that their effects on gold medal counts are primarily concentrated in the negative region. Similarly, in the total medal prediction model (Fig. 11(b)), these same sports significantly impact the total medal count; high performance when PC1 is negative enhances both gold and overall medal tallies. The ascent of SHAP values in the dependence plot signifies that their excellence contributes notably not only to gold but also to silver and bronze medals. As PC1 becomes positive, their influence on total medal counts weakens, further confirming their critical role in the negative PC1 region.

关注数学模型 微信公众号：数学模型 (a) (b) 微信号：MATHmodels

Finally, this study incorporates SHAP values for individual samples to analyze the impact of different sports on gold and total medal predictions for the U.S. and France, particularly focusing on the contributions of traditional powerhouses like Swimming and Athletics. Additionally, it discusses the host country effect, exploring how the upcoming host nations, France in 2024 and the USA in 2028, can positively influence predictions of gold and total medal counts through home advantage.

(a) (b)

(a) (b)

Figs. 12(a)-(b) show that traditional power sports like Swimming and Athletics carry significant weight in the PCA components, particularly with high loadings in prin- cipal components PC1 and PC2, indicating their substantial contributions to the U.S. gold medal count. With a PC1 value of 18 for gold medal predictions, this confirms the driv- ing role of these sports. In contrast, the total medal count prediction for the U.S. is 133, with a contribution of 6.08 from PC2, revealing the impact of other sports like Gymnas- tics and Basketball, which, while contributing fewer golds, play a vital role in enhancing overall medal totals. For France, as the 2024 host, the predictions (Figs. 13(a)-(b)) are notably influenced by the "host country effect," with a total medal count forecast of 41 and a significant contribution of 2.89 from PC5, underscoring the importance of sports such as Cycling and Marathon. Despite a relatively lower gold prediction of 12, the host effect positively enhances France's overall performance, particularly in events like Swim- ming and Athletics, where the PC3 loading of 1.97 confirms their contributions. While France's traditional strengths in these events may not match those of the U.S., home ad- vantage helps bridge the gap.

This analysis concludes that the choice of sports and traditional advantages play decisive roles in Olympic performances, with the U.S. primarily excelling in individual sports like Swimming and Athletics, while France benefits from team sports and the host country effect. Overall, the host effect significantly impacts both countries' Olympic performances, with France poised for a notable boost in 2024 as a host, while the U.S. faces new challenges in 2028.

Problem 2: The "Great Coach' Effect 4

It is evident from the problem 2 statement that the mobility of coaches is greater than that of athletes, suggesting that their transfers may have a direct impact on a coun- try's medal performance. The DID⁴ model is suitable for assessing the causal effects of policies or events by comparing the changes in the treatment group (country-sport combi- nations with a coaching change) and the control group (combinations without a coaching change) before and after the event. The problem also requires estimating the contribution of coaching effects to the number of medals, which necessitates quantifying the incremen- tal medals attributed to coaching changes. In addition, three countries need to be selected for which recommendations should be made regarding the sports in which to invest in coaching, while also estimating the potential impacts of such investments.

4.1 DID Modeling

The validity of the DID model relies on the parallel trends assumption, which states that the trends in medal counts for the treatment and control groups should be consistent prior to the coaching change. This assumption needs to be verified; otherwise, the re- sults may be biased. Finally, the analysis results must be structured clearly, specifying the recommended sports for each country, the current contribution coefficients of coach- ing effects, and the expected returns on investment. Additionally, the uncertainty of the estimates, such as confidence intervals and P-values, should be discussed to enhance the credibility of the conclusions. So we build the following DID model.

∑ (Medalsit − (β0 + β1Treati + β2Post + β3(Treati · Postt) + γXit))2 min β,γ i,t Medalsit = β0 + β1Treati + β2Postt + β3(Treati · Postt) + γXit + €it, ∀i, t (9) E[∆Medalsi | Treat = 1, Post = 0] = E[∆Medalsi | Treat = 0, Post = 0] s.t.

€it ⊥ Treati, Post

关注数学模型

4.2 Hypothesis Testing and Contribution Coefficient Analysis

We subsequently fit the model equation using ordinary least squares (OLS) to es- timate the coefficients β0, β1, β2, β3, γ. We calculate the P-value for β3 to assess it's significance. Additionally, we conduct a parallel trends test to verify whether the medal trends for the treatment and control groups were consistent prior to the coaching change. The comprehensive results are shown in Table 4.

模型

Sport β3 P-value NOC 95% confidence interval opnf 6.0 0.001 JPN [4.8, 7.2] 0.010 ITA 5.0 [3.5, 6.5] Athletics AUS 0.020 5.0 Swimming [3.0, 7.0] 4.0 Archery 0.030 KOR [2.0, 6.0] [1.5,6.5] POL 4.0 0.040 Athletics [-0.5, 6.5] 3.0 CUB 0.100 Boxing Fencing 3.0 0.200 [-1.0, 7.0] KOR dels Diving 3.0 0.150 CHN [-0.8, 6.8] ● Shooting 3.0 CHN 0.180 [-1.2, 7.2] ● 0.250 BRA 3.0 [-2.0, 8.0] Skateboarding

We selected the top 10 values of β3 for display in Fig. 14. It is evident that the coaching changes in Japanese judo, Italian athletics, Australian swimming, South Korean archery, and Polish athletics significantly increased the number of medals, as none of their confidence intervals include zero and all P-values are less than 0.05, from Table 4. In contrast, the β3 values for Cuban boxing, South Korean fencing, Chinese diving and shooting, and Brazilian skateboarding, although positive, have confidence intervals that include zero, and their P-values exceed 0.05, indicating that the causal effects of coaching changes in these countries did not pass the statistical significance test. Next, we conducted a parallel trends test using Japan as an example. Fig. 15 shows a clear upward trend in medal counts from 1996 to 2016, indicating that it successfully passed the parallel trends ● test. ●

and parallel trends tests. Upon reviewing the data123, it is confirmed that Australia, South Korea, and Poland indeed underwent coaching changes during the 2020-2024 period, specifically involving Rennie Taylor, Lee Changhoon, and Adam Kszczot, respectively. This aligns with the aforementioned results, suggesting that our model is effective.

Problem 3: New Insights 5

1. Dynamics of Medal Counts in Space and Time

(1) Insight: The model analyzes the spatiotemporal dynamics of Olympic medal counts through multiple iterations and Bootstrap resampling methods. The study indicates

1https://olympics.com 2https://www.insidethegames.biz 3https://www.linkedin.com that certain countries display relatively stable performances across different Olympic cy- cles, while others experience significant fluctuations in their medal counts. For instance, some major nations show a limited range of variance in their medal counts, highlighting their sustained competitiveness across multiple events. In contrast, some smaller nations exhibit greater volatility in their medal counts, suggesting that their performance may be heavily influenced by specific events or sudden occurrences.

(2) Decision support: The findings can assist the Olympic committees in developing more flexible strategies for future Olympic cycles. If a country exhibits instability in its medal counts, the committee can mitigate uncertainty by diversifying resource allocation, thereby avoiding excessive reliance on any single event. For example, increasing train- ing investments in unstable events and enhancing the competitiveness of other promising sports can help ensure consistent performance across various disciplines. Additionally, for countries showing more stable performances, the Olympic committees could focus on maintaining existing advantages while bolstering research and technical support to ensure they remain competitive at the forefront.

2. Correlation Between Olympic Medal Counts and Specific Events

(1) Insight: The model, through the integration of PCA and LSTM, reveals the sig- nificance of certain specific events in predicting medal counts. The research demonstrates that disciplines such as swimming, athletics, and shooting play a crucial role in the medal contributions of many countries. These events are not only widely recognized and highly competitive at the Olympics but also serve as essential battlegrounds for countries vying for medals. In particular, swimming and athletics stand out as primary sources of medal counts for many nations due to their frequent competitions and high viewer engagement.

关注数学模型 (2) Decision support: Olympic committees can leverage these analytical findings for strategic planning, particularly in resource allocation and event development. For events that display a strong competitive advantage, countries can increase their invest- ments by providing additional training facilities and financial support. For instance, in nations where swimming and athletics are particularly strong, committees could enhance athlete training by collaborating with top domestic and international coaches to refine skills and improve overall performance. Furthermore, informed by data analysis, coun- tries can identify potential medal-winning events in advance, enabling them to formulate effective athlete development programs and promotional strategies for these disciplines. 微信公众号：数学模型 3. Coaching Investment Directions in National Strategies

(1) Insight: Through model analysis, some countries exhibit strong medal returns following coaching changes, as seen in Australia. Conversely, other nations experience minimal impact from such coaching transitions, despite implementing changes.

(2) Decision support: Olympic committees should develop personalized strategies based on the specific circumstances of different countries, prioritizing support for events that demonstrate significant improvements post-coaching changes. For countries such as Japan, Italy, and Australia, the committees could enhance investments in judo, athletics, and swimming to increase medal returns. Meanwhile, for events that show less pro- 微信号：MATHmodels nounced results, committees could reduce excessive investments in those coaching staff and reallocate resources to focus on areas more likely to yield medals.

6 Sensitivity Analysis

6.1 The Number of Principal Components

To simplify the data structure and improve the efficiency of the prediction model, Principal Component Analysis (PCA) was used. PCA was performed on the Olympic event dataset, and the variance contribution rates of each principal component were cal- culated. The selection of five principal components was based on their explanation of 76.4% of the cumulative variance, effectively capturing most of the information in the original dataset. This choice is supported by Fig. 16, which shows a steep drop-off after the first few components, validating the use of five components. This approach reduces data dimensionality while retaining essential information and eliminating redundant fea- tures.

6.2 Prediction Model Evaluation

In the model evaluation, we examined both the predictive accuracy and robustness of the gold medal and total medal prediction models. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1. Predictive accuracy

Through 10-fold cross-validation and Bootstrap resampling, we obtained prediction intervals and confidence levels for both models. In the gold medal prediction model, the MSE of the test set was 6.83, and the RMSE was 2.61. Although these values were slightly higher compared to the training set, the MAE was 0.52, and the MAPE was 14.47%, indicating that the model’s accuracy remains acceptable for new data. The total medal prediction model showed more stable performance, with lower MSE and RMSE, indicating higher predictive accuracy. These results are summarized in Table 5.

Gold Total Training Test Training Test MSE 1.33 6.83 28.5 6.46 RMSE 1.16 2.61 5.34 2.54 MAE 1.49 0.52 3.68 1.04 MAPE 17.50% 14.47% 18.63% 16.13%

2. Robustness evaluation

To assess the robustness of the model, we focused on the R² value and the R-squared line plot from 10-fold cross-validation, as shown in Figs. 17(a)-(b). The results showed that both the gold medal and total medal prediction models had R² values close to 1, indicating that the models fit the data well and demonstrate consistent performance across different datasets, showcasing strong generalizability.

(a) (b)

7 Model Analysis

7.1 Strength

The innovation and advantages of this study lie in the development of a predictive model for Olympic medal counts by integrating the PCA-LSTM-enhanced XGBoost- Bootstrap algorithm. Additionally, it conducts a comprehensive validation of the model’s accuracy and stability through various statistical methods, while employing a DID frame- work to assess the impact of coaching changes on Olympic medal counts. This is specifi- cally reflected in the following aspects:

关注数学模型 • The introduction of the Bootstrap resampling method facilitates confidence interval estimation for the predictive outcomes, quantifying the model’s uncertainty and bolstering the credibility of the results. Additionally, the application of parallel trend hypothesis testing ensures that the experimental and control groups exhibited consistent medal trend patterns prior to coaching changes, further enhancing the stability of the model and the accuracy of inferences.

• By integrating SHAP value analysis, this study conducts a thorough assessment of the contributions of different sports to medal counts, revealing key factors that in- fluence outcomes. Notably, when analyzing host nations, the findings illustrate the home advantage’s significant effect on medal totals, thereby enhancing the model’s interpretability and providing more actionable insights for decision-making.

• The use of the DID model allows for the evaluation of the causal effects of coach- 微信公众号：数学模型 ing changes on medal counts, providing an accurate quantification of the impact of such changes on Olympic performance and ensuring the reliability of causal in- ferences. Furthermore, the combination of PCA for dimensionality reduction and LSTM for trend modeling enhances the predictive accuracy of medal counts, show- casing strong modeling capabilities, particularly in addressing complex nonlinear relationships and time series data.

7.2 Weekness and Further Discussion

Our model has several limitations and incompatibilities. For instance, the computa- tional cost of the XGBoost and Bootstrap methods is relatively high, particularly when 微信号：MATHmodels dealing with large datasets, which affects the model’s real-time applicability. Addition- ally, the application of PCA for dimensionality reduction may lead to information loss, thereby impacting the model’s performance in capturing complex relationships. While LSTM are capable of identifying trends, their predictive ability is limited when it comes to sudden events and drastic fluctuations, which reduces the robustness of the model. Fur- thermore, the DID model assumes that the impact of coaching changes on medal counts is linear; however, in reality, these effects may be nonlinear, resulting in a failure to ad- equately capture the complex relationships present in the data and affecting the accuracy of causal inferences.

Future improvements to the model focus on two key areas. First, the Olympic medal count prediction model will enhance its integration of fluctuations from the Games, po- litical factors, and athlete performance variations through advanced ensemble learning techniques. By optimizing weighted averaging and stacked modeling, the model will in- corporate a wider range of variables and improve short-term predictive accuracy via a robust real-time data update mechanism. The use of reinforcement learning will further strengthen its long-term forecasting abilities, enhancing adaptability to sudden events and policy changes, while also improving computational efficiency for better timeliness and accuracy in predictions. Second, the enhanced-DID model will merge differentiated im- pact analysis with deep learning techniques to refine medal predictions. By incorporating stochastic simulations, this model will dynamically adjust the effects of coaching changes on medal counts, significantly boosting its adaptability in fluctuating environments and improving overall predictive effectiveness.

8 Memorandum

To: International Olympic Committee

From: Team #2500759

Subject: 2028 Olympics Medal Prediction and Insights

Date: January 26, 2025

Dear Members of International Olympic Committee,

We are pleased to submit our solution to the medal prediction model for the 2028 Los Angeles Summer Olympics. Our team developed this model based on the data from the 2024 Paris Olympics and additional background information, offering both precise medal predictions and valuable insights for improving Olympic performance.

To construct the model, we utilize historical medal data and employ a PCA-LSTM- enhanced XGBoost-Bootstrap approach for preliminary predictions. Subsequently, we adjust these predictions by considering the event configurations and competitive structures of the 2024 Olympic Games, analyzing how these factors influence the medal counts of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m different countries. To estimate the uncertainty in our predictions, we provide confidence m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m intervals for gold medals and total medal counts. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m An essential component of our model is the analysis of the "great coach" effect, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m which we integrate using the DID model. By comparing countries with and without m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m coaching changes, we estimate the incremental impact of coaching transitions on medal outcomes. We fit the model using OLS and conduct statistical significance tests as well as parallel trends tests to ensure the reliability of our results.

Beyond simply predicting medal counts, our model also offers insights on optimizing Olympic performance. It highlights which countries are likely to make breakthroughs in specific sports by strategically increasing investments in those areas. Furthermore, our model suggests potential improvements in the types and settings of Olympic events, recommending adjustments that could help maximize medal outcomes. These findings can guide the decision-making processes of National Olympic Committees as they plan for the 2028 Olympics and beyond.

Thank you for providing the opportunity to participate in this important project. We look forward to your valuable feedback.

Sincerely yours,

关注数学模型
