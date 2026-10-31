Summary

In Question 1, this paper proposes a Hurdle-Tobit fusion model framework to address the characteristics of the discrete nature of the number of Olympic medals, the zero inflation characteristics, and the heterogeneity between countries. The Hurdle model solves the zero value problem through two-stage modeling (logit classification and truncated count distribution), and the Tobit model handles right censored data. Both models introduce the Revealed Comparative Advantage Index RCA and incorporate heterogeneity factors such as the discrete size of athletes and the host effect. Then, by comparison, we found that the hurdle and Tobit models were significantly better than the machine learning methods (random forest and XGboost) in terms of mean square error and prediction coverage. Among them, the Hurdle model has a better predictive effect on the number of medals of sports powers, while Tobit has a better predictive effect on countries that have won a few medals. The prediction results show that the United States, China, and India will see the largest increases in medals, while France, Russia, and Germany will see significant decreases. The probability of Angola, Bangladesh, and Cambodia winning their first medal is 49.2%, 46.7%, and 42.5%, respectively. Finally, using model complementation and variable reconstruction, it is revealed how the host selection project affects the number of medals.

In Question 2, the Bayesian Change-point Detection method is used to identify significant changes in the number of medals won by countries in specific events (such as a sudden breakthrough after a long period of depression), and attribute them to the “great coaching effect”. In order to solve the problem of frequent changes in the simple weighted medal data, an innovative data preprocessing algorithm with memory enhancement is used to preprocess the original medal data, which can effectively distinguish the significance of the medal data and the dynamic self-reinforcing mechanism from the real changes driven by the coaching effect. Then, a two-stage least squares (2SLS) method is used to construct a causal regression model to quantify the contribution of outstanding coaches to the number of medals, overcoming the endogeneity bias of the traditional OLS method. Model validation shows that 2SLS significantly outperforms OLS in explaining the coaching effect. Based on this, it is proposed that the United States, the United Kingdom, and France should prioritize the introduction of multinational coaches in wrestling, rowing, table tennis, and other events, which is expected to increase the number of medals by 1-2.

In Question 3, we continue the analysis of Questions 1 and 2. Based on the Bayesian change-point detection method, we identify the potential “great coaching effect” time nodes in each sport in previous Olympic Games and incorporate them into the Hurdle and Tobit models as key explanatory variables for reanalysis. At the same time, in order to capture the dynamic self-reinforcing mechanism of medal counts, we further explain the lagged terms (such as the host country effect lagged by 4 years, the historical medal count lagged term, etc.) to analyze the heterogeneity of short-term and long-term effects. Ultimately, we obtain policy implications for promoting post-competition resource redistribution and for balancing the “depth” and “breadth” of National Olympic Committees.

1 Introduction

1.1 Background

微信公众号：数学模型 The Olympic medal table reflects national sporting prowess and serves as a global competi- tive benchmark. At the 2024 Paris Olympics, the U.S. and China tied with 40 golds each, while host France ranked fifth in golds (16) but fourth overall. Notably, Albania and Cape Verde achieved their first-ever medals, yet over 60 countries remain without Olympic medals.

1.2 Restatement of the Problem

Task 1 Develop an Olympic medal prediction model using historical data to forecast: (1) 2028 Los Angeles medal counts per country with prediction intervals and accuracy metrics, identifying upward/downward mobility relative to 2024. (2) First-time medal-winning prob- ability for nations, contextualized through historical breakthrough patterns. (3) Sport-event 微信号：MATHmodels structure’s impact on medal distribution, including identification of national dominance events. (4) Quantification of host advantage through program adjustment impacts.

Task 2 (1) Statistically validate coach replacement effects on medal changes and quantify "great coach" contributions. (2) For three nations, identify underperforming sports with medal potential and assess feasibility/benefits of elite coach recruitment.

Task 3 (1) Identify non-traditional factors influencing medal allocations. (2) Generate evidence-based policy recommendations for Olympic committees.

1.3 Literature Overview

Empirical analysis of the Olympic Games has emerged as a critical area of research, en- compassing both forecasting (e.g., De Bosscher et al., 2006) and broader analytical perspectives (e.g., Streicher et al., 2020).

Since Ball (1972) introduced a correlation-based scoring model, forecasting methodologies have become increasingly sophisticated. Initially, many researchers relied on ordinary least squares (OLS) regressions due to their ease of interpretation (e.g., Baimbridge, 1998; Condon et al., 1999; Kuper and Sterken, 2001). However, a significant challenge in predicting Olympic medals is accurately reflecting the substantial number of nations that have yet to achieve any medals. The exponential function employed in these models tends to impose penalties on low predicted medal counts. Consequently, some scholars have transitioned to Poisson-based models (e.g., Lui and Suen, 2008; Leeds and Leeds, 2012; Blais-Morisset et al., 2017).

Afterwards, machine learning techniques (e.g. Random forest and XGboost) have gained traction in sports-related contexts. The random forest approach has demonstrated exceptional performance in tasks such as predicting the outcome of football matches (Groll et al., 2019) or horse racing outcomes (Lessmann et al., 2010). However, random forests and XGBoost, as ensemble learning methods based on decision trees, excel at handling non-linear relationships and feature interactions, but they lack the ability to explicitly model truncation and zero-inflated data. This means that these algorithms may not accurately capture the truncation points or zero-value generation mechanisms in the data, leading to prediction bias (Breiman, 2001; Chen & Guestrin, 2016).

Given that the dependent variable, typically the number of medals, has been set to zero, most authors have employed Tobit regression to predict Olympic success (e.g., Tcha and Pershin,

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2003; Forrest et al., 2015; Rewilak, 2021). However, recently, a two-step approach, estimating the probability of winning any medal before determining the exact number of medals in case of success, has become more prevalent. In particular, both Scelles et al. (2020) and Rewilak (2021), employing a Mundlak transformation of the Tobit model, could, again, increase the prediction accuracy with their respective Hurdle models.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m This finding aligns with the modeling approach adopted in this study, which utilizes Tobit m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and Herdle models to address the unique challenges associated with Olympic medal forecasting. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

1.4 Our Work

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

2 Assumptions and Justification

• All models are built based on the normal holding of the Olympic Games, and situations such as the postponement of the Olympic Games will not occur.

• The models are built without the influence of external factors (such as political events and national bans), and are based only on existing data.

• All data used in this article is real data without statistical errors.

3 Notations

关注数学模型

Notation

Significance

Mapdisq∗ Potential medal ability i,t RCA National dominance sports index Nai,t Categories to which the number of players belongs NAE The number of events that won medals in a sport for a country Mi,t The expected number of medals won by country Medal_PCA The number of medals after dimensionality reduction

4 Data Processing

4.1 Data Cleaning

To facilitate forecasting, we exclude vacant items in the tabular data, harmonize country 微信公众号：数学模型 names (e.g., the Russian Olympic Committee and Unified Team in 2024 are grouped together as Russia), harmonize athlete names (e.g., due to differences in hosts and entry rules, Ma Long and Long Ma are actually the same ), harmonization of event names (e.g., “Tabble Tennis Men’s single” in 2024 is the same as “Men’s single “ of table tennis in 2020).

4.2 Data Overview

The following figure shows a box plot of the total number of medals for all participating countries in the Olympics from 1896-2024. At the same time, we extracted the total medal counts of USA, China, France, Great Britain and Australia to draw a line graph.

微信号：MATHmodels

As shown in the figure, it can be seen that the box plot shows a right-skewed distribution, i.e., the maximum is much higher than the median and the tails extend to the right, reflecting that a few countries dominate the medal table.

We calculated the mean, standard deviation, maximum and minimum values for the number of athletes, number of medals, total number of medals, host, number of sport type and number of events in which the countries participates for the 2024 Olympic Games in Paris, France, as shown in the following table.

Variable Mean SD Min Max

Number of Athletes 73.40 144.9809 2 856 Total Medals 11.42 19.7028 1 126 Gold Medals 1.59 4.97 0 40 Silver Medals 1.59 4.83 0 44 Bronze Medals 1.85 4.83 0 42 Host Country 0.01 0.07 0 1 Number of Events 31.27 46.84 1 234 Number of Sports 10.07 10.30 1 47

According to the above table, it can be seen that

• The large standard deviations of the number of athletes and medals indicate a large degree of dispersion.

• Only 1% of the observations are host countries, indicating that the sample of host countries is extremely small, which may affect its statistical significance, which may affect its statistical significance and should be interpreted with caution.

• The number of athletes is highly correlated with the number of medals, but it should be noted that there is covariance between the host country variable and the number of athletes in the model, resulting in the host country effect being explained by the number of athletes.

5 ComparativeModelingofOlympicMedalProjections: Hurdle-

Tobit Framework with Host Country Strategy Analysis

5.1 Hurdle and Tobit Models

Since the number of medals is a discrete non-negative integer (e.g., 0, 1, 2, etc.), it becomes critical to deal with such a large amount of discrete data, and therefore the counting model is used for the analysis. So we first considered the suggestion of Blais-Morissetr, and Fortin (2017) that a Poisson model be used for handling such data in this case. However, due to significant heterogeneity across countries, the variance is larger than the mean (i.e., the overdispersion problem), which makes the assumptions of the Poisson model not valid.

To deal with the over-dispersion problem, we turn to consider the Zinb model (Zero-Inflated Negative Binomial Model), which is applicable when there are a large number of zeros in the data and assumes that the zeros come from two different sources, a “structural zero” (e.g., the country did not (e.g. the country did not participate in the Olympic Games) and “sampling zeros” (e.g. the country participated but did not win a medal). However, since the study

关注数学模型 focuses on countries that have participated in the Olympics, structural zeros do not exist and the assumptions of the Zinb model no longer apply.

Then, we turn to use Hurdle model, which differs from the Zinb model in that it does not distinguish between the sources of the zero values, but rather divides the model into two parts: the first part is the decision of whether or not there is at least one medal (Binary Classification Problem), and the second part is the distribution of the number of medals in the event that there is at least one medal. This is similar to the Tobit model (Truncated Regression Model), but whereas the Tobit model assumes that observations below a certain Hurdle are truncated, the Hurdle model explicitly distinguishes between the two processes of whether or not that Hurdle 微信公众号：数学模型 is crossed.

Therefore, for the two different scenarios of countries that have never won a medal and sports powerhouses, we improve the use and compare the predictive effectiveness of the four methods of Tobit model, hurdle model, random forest and XGBoost, and select the optimal model for the different scenarios.

Step 1: Variable definition and treatment.

NAi,t denotes the number of athletes competing in the Olympics for countryi in year t, which was initially analyzed as a continuous variable. However, the marginal returns to the 微信号：MATHmodels number of athletes may be nonlinear and the exact number of participants cannot be known in advance when predicting future medal totals. Therefore, we introduce Nai,t to discretize the number of participating athletes into four categories:

• Nai,t = 1: 0 to 9 athletes;

• Nai,t = 2: 10 to 49 athletes;

• Nai,t = 3: 50 to 149 athletes;

• Nai,t = 4: 150 athletes and over

From the figures above, it is worth noting that there is a significant multicollinearity between the number of gold medals, silver medals, bronze medals, and medal table. To simplify the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m model, we actually use Principal Component Analysis (PCA) to downscale to one dimension before using it, i.e., Medal_PCA.

At the same time each country should have its dominant sport, in order to include it in the model we introduce RCA to refer to quantify the dominant sport of each country. RCA is given by the following formula:

RCA = Mij/Mi (1) Tj/T

Here, Mij represents the number of medals for country i in sport j;Mi represents the total number of medals for country i; Tj represents total global medals in sport j; T represents total medals in all sports.

RCA > 1: country has a comparative advantage in the given sport;

m m m m m m m m m m m m m m m m m m m m m m RCA < 1: country has a comparative disadvantage in the given sport.= m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The figure below shows the RCA index heat maps of the countries that won medals at Paris m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2024. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Step 2: Define latent variable Xi,tΘ and potential medal abilityMapdisq∗ i,t.

Depending on the set of explanatory variables selected, we define latent variable Xi,tΘ by:

X X X Xi,tΘ = c+λ ln Ni,t−4+ρHosti,t+ γRCAp,i+δMedal_PCAi,t−4+ ζNum_Eventsp,i,t+κ NAEp, p p p (2)

Here, Xi,tΘ = [Xi,tΘGold, Xi,tΘSilver, Xi,tΘBronze]T. Hosti,t isthehostvariable(Hosti,t=1, country i is the host of the t Olympic Games). Num_Eventsp,i,t is the number of events in

关注数学模型 which the i country participated in the p sport of the t Olympic Games. c, λ,ρ, γ, δ, ζ, κ ∈R3are all coefficients, representing the value of Xi,tΘ for gold, silver and bronze respectively, which are calculated by maximum likelihood estimation (MLE) based on historical data.

We define potential medal ability Mapdisq∗ i,t by: 微信公众号：数学模型 Mapdisq∗ i,t = Xi,tΘ + ui + ϵi,t (3)

Here, ui represents country-specific random effects (such as culture, training system and other unobserved factors), following a normal distribution N (0, σ2 u) ; ϵi,t is a random error term.

Step 3: Construct Tobit model.

For the Tobit Model, the general specification is:

 Mapdisq∗ , if Mapdisq∗ i,t > 0 i,t 微信号：MATHmodels Mapdisqi,t = (4) i,t ⩽0 , if Mapdisq∗ 0

The predicted medal count Mapdisqi,t is a truncated version of the potential medal ability Mapdisq∗ i,t.

Step 4: Construct Hurdle model.

Mapdisq∗    1) Calculate the probability of winning P i,t > 0 .

We use the Logit model to calculate the probability that the i country will get at least one medal, as follows:

1 Mapdisq∗    P i,t > 0 = (5) 1 + e−Xi,tΘ

2) Calculate the expected number of medals won by the winning countryMi,t.

First, we define µi,t as the theoretical mean of the number of medals for country i under the condition of "winning at least one medal", the formula is:

µi,t = eXi,tΘ (6)

Then, to adjust the expected value since only the winning country is considered (i.e. zero values are excluded), we define the truncated correction E(Mapdisq∗ i,t) as:

1 E(Mapdisq∗ i,t) = µi,t · (7) 1 −(1 + µi,t/r)−r

where r is a discrete parameter.

Finally, the expected number of medals won by the winning country Mi,t is given by:

Mapdisq∗ · E(Mapdisq∗    Mi,t = P i,t > 0 i,t) (8)

5.2 Model Selection and Validation

5.2.1 Model Selection: Hurdle, Tobit, XGBoost and Ramdom Forest

In this study, we employ four models—the Tobit model, the Hurdle model, Random Forest, and XGBoost—to predict the total number of medals won by the United States in the 2024 Olympic Games in Paris, France. This approach is taken to assess the accuracy of the four models’ prediction results.The comparison between the prediction results based on the four methods and the real data is shown below.

Hurdle Tobit XGBoost Ramdom Forest

MSE 20.15 23.01 63.67 51.25 R2 0.8545 0.8026 0.7121 0.758

As shown in the figure, Hurdle and Hurdle perform better, and the prediction results of Random Forest & XGBoost are poorly fitted to the real values. In the case of Random Forest with XGBoost, the predicted values are biased in the region of actual medal count >15, i.e., it is difficult to deal with the distributional characteristics of zero-inflated data effectively. Meanwhile, the prediction points in countries with large medal counts (actual values > 50) are scattered and irregular, reflecting the model’s insufficient ability to capture extreme values.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Meanwhile, the MSE of Hurdle and Tobit is significantly lower than that of XGBoost and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Random Forest, which indicates that the former two models are better in prediction accuracy.The m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m R2 of Hurdle and Tobit is significantly higher than that of the former two. This indicates that Hurdle and Tobit models are more effective in explaining data variability.

5.2.2 Model Validation: 2024 Olympic Games Predictions Based on Hurdle and Tobit

We choose the Hurdle and Tobit models with better prediction performance to present the prediction results for the prediction interval and accuracy of the total medal count of 2024 Paris Games.

微信公众号：数学模型

Hurdle Model Tobit Model Country Actual Medals Forecast Lower CI Upper CI Forecast Lower CI Upper CI

120 105 United States 126 103 134 95 113 89 106 China 91 86 93 95 117 68 56 Great Britain 65 63 53 51 61 70 69 France 64 63 77 66 71 48 46 Australia 53 44 52 44 58 47 44 Japan 45 42 51 42 46 微信号：MATHmodels 43 48 Italy 40 38 48 43 53

Rate of right forecasts for 2024 Paris Olympic Games

All countries (192) CI to 95%(+ or -2) 88.6% (93.2%) 83.8% (90.6%) Exact forecasts (+ or - 1) 21.9% (77.1%) 43.2% (74.5%) Exact forecasts (0 medal) 41.3% 69.1% (107 countries) Exact forecasts (non-0 medal) 22.4% 10.4% (85 countries) Countries with at least 3 medals(56) CI to 95%(+ or -2) 62.3% (76.8%) 50.2% (69.6%) Exact forecasts (+ or - 1) 8.9% (38.5%) 8.9% (31.4%) Note: CI = confidence interval; forecasts in bold.

First, in the 95% confidence interval prediction coverage, the Hurdle model covers 88.6% of all 192 countries, which is higher than the 83.8% of the Tobit model; among the 56 countries with at least 3 medals, its coverage (62.3%) is also much higher than that of the Tobit model (50.2%). In addition, the prediction accuracy of the Hurdle model for countries with non-zero medals (±1 error rate of 22.4%) is more than twice that of the Tobit model (10.4%), highlighting the advantage of its two-stage modeling in adapting to zero-inflated data.

Although the Tobit model has a higher rate of fully accurate predictions in zero-medal countries (69.1%) than the Hurdle model (41.3%), this advantage comes at the expense of the ability to predict non-zero medals.The Hurdle model is more balanced between the two types of scenarios by separating the mechanisms of zero value generation and positive prediction, and it is particularly robust in countries with high medal counts (±1 error bracket value 38.5% vs. 31.4%).

In summary, the Tobit model fits better around zero medals, thanks to its truncated regression m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m assumptions for the lower bound values. However, as the number of medals increases, the dispersion increases significantly, exposing the limitations of the single continuous distribution assumption. In contrast, Hurdle’s model, through two-stage modeling, shows better prediction results in both the zero-value region and the high medal region, with a concentrated distribution of points and low dispersion, which effectively balances the zero-value generating mechanism with the flexibility of positive prediction.

5.3 2028 Los Angeles Olympics Medal Count Projections

The figure below shows the medal standings for all participating countries that are predicted to win at least one medal.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Based on the above prediction results, we have listed the top five countries with the highest increase and decrease in total medals, as follows.

Improve USA China India Brazil Japan

Magnitude 15 10 7 5 5

Decline France Russia Germany Great Britain Australia

Magnitude -8 -4 -4 -3 -2

5.4 Projecting First-Time Medal Winners and Probability Estimates

The prediction results show that a total of three countries will win their first medals at the 2028 Los Angeles Olympics, namely: Angola, Bangladesh and Cambodia. The probability of

关注数学模型 each country winning their first medal is shown in the table below.

Country Angola Bangladesh Cambodia 49.23% 42.49% 46.67% Possibility

5.5 The Influence of Item Selection on the Number of Medals

The below table shows the mean values of the statistical results obtained by each country when Tobit and Hurdle were used.

Tobit Model

Hurdle Model Variables Coef Coef SD SD Constant 8.864*** 0.336* 2.02 0.1 Host country in 4 years 1.566*** 0.11 12.520*** 2.03 Host country t -4.760** 0.85 0.11 2.08 Host country 4 years ago 0.016* 0.897* 0.02 Athletes [0,10] 0 0.510* 5.126*** 0.23 0.67 Athletes [10,50] 0.87 0.989* 0.24 7.394*** Athletes [50,150] 1.559*** 9.314*** 0.27 1.15 150 athletes and more 3.42*** 3.725*** 0.12 4.57 Medals_PCA(t-4) 2.538*** 1.828** RCA 0.22 1.07 3.42*** 3.725*** 0.12 4.57 0.538** 1.828** 0.22 1.07 Num_Events 0.618** 1.719** 0.21 0.97 2.742*** 2.705*** 0.22 NAE 0.26 -3.408*** 0.25 gi,t 0.115*** 26.68*** 2 0.03 1.66 u 529 1232 Observations total 529 Observations noncensored Note: ***Significant at the 1 percent level; **5 percent level; *10 percent level.

The results show that both the number of events and NAE have a positive and significant effect, and this significance is common to all countries. The coefficient of RC A is large and the variance is large, which may indicate significant heterogeneity in the importance of different sports for different countries. At the same time, the host country has a positive impact in both the Tobit and Hurdle models, and in the Hurdle model, the coefficient of the host country is smaller than that of the Tobit. The explanation is that there is obvious multiple collinearity between the host country and other variables such as NAE and RCA, and these variables will dilute the significance of the host country, and Hurdle is more likely to capture this effect.

5.5.1 Relationship Between Olympic Events and Medal Distribution

Initially, an effortwasmadetoconstructagraphrepresentingtherelationshipbetweenMeanNAE, Num_Events, and Total in historical data for China, the United States, Japan, and France. Subsequently, the Pearson correlation coefficients of these countries regarding the two covari- ates and Total were calculated. The graph of the relationship between Total and meanNAE and correlation coefficient tables are presented below.

Mean SD

num_events 0.238 0.216 NAE 0.952 0.051

The findings revealed a robust linear relationship between MeanNAE and Total, with a concomitant small standard deviation, suggesting its universality. However, the significance of Num_Event is negligible, and this phenomenon exhibits substantial heterogeneity across different countries.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

5.5.2 Analysis of Key Sports and Their Importance for Different Countries

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The RCA index is a quantitative metric that can be used to compare the relative popularity of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m different sports in different countries. As illustrated by the heatmap, Modern Pentathlon has m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m emerged as Egypt’s preeminent sport, a finding that aligns with its status as the nation’s sole gold m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m medalist and world record holder in this discipline. A similar observation can be made when examining the United States, another nation with a strong sporting reputation. The RCA index for the United States exceeds 1 in several sports, suggesting a comparable level of dominance in various sports. This finding is consistent with the notion that the United States possesses a diverse array of sports with similar levels of strength.

In order to ascertain the sports that are of the utmost importance to each nation, the present study utilizes Egypt and the United States as exemplars. The Tobit and Hurdle models are

关注数学模型 employed to predict the total for the 2024 Summer Olympics, calculate the corresponding RC A and coefficient, use these as a benchmark to rank the sports, and extract the number of medals contributed by these sports. In essence, the sports displayed in the figure represent the most significant contributors to the overall medal count of the United States and Egypt, as evidenced by their substantial RCA and corresponding coefficient values.

Athletics Modern Pentathlon 27 Fencing Swimming Artistic Gymnastics Weightlifting 9 Wrestling Shooting Fencing Skateboarding Cycling Track Sport Climbing 2 22 Tennis Archery 22 Rowing Volleyball 2 Sport Discipline Weightlifting 2 Basketball Canoe Sprint Water Polo Artistic Swimming Boxing Breaking Canoe Slalom Taekwondo Cycling BMX Freestyle Cycling Mountain Bike Surfing Diving Equestrian Football Golf Rugby Sevens Sailing 3x3 Basketball 10 15 20 25 30 35 5 Medal Count 1

5.5.3 Impact of Host Country Event Selection on Performance

Based on historical data observations, there is a significant synergistic growth between the host country's RC A and NAE (as shown in the figure below).

微信 This phenomenon may be attributed to two non-mutually exclusive mechanisms:

• Strategic project selection, wherein the host country utilizes the rules of the competition to incorporate temporary advantageous projects (such as niche unpopular projects) to artificially augment RCA through "institutional dividends".

• Systematic capacity enhancement. The long-term resource investment (e.g., athlete train- ing) brought about by hosting the event promotes the overall upgrading of sports strength, which in turn enhances NAE and RCA.

To quantify the independent impact of these mechanisms, this study employs a dual strategy of model complementarity and variable reconstruction. While the hurdle model has been demonstrated to more effectively capture the host effect, the Tobit model has been shown to be more adept at addressing sports with weaker nations (i.e., medal count less than or equal to 0). This is due to the truncated regression characteristics of the Tobit model, which are more conducive to the "zero value accumulation + low value continuity" distribution. Consequently, the Tobit model can more sensitively detect the marginal effect of the host country surpassing the zero medal threshold through RCA_add and NAE. Consequently, it is imperative to construct two models based on Tobit and Hurdle through variable refinement.

• Convert continuous NAE to a three-category variable (low/medium/high) to identify nonlinear threshold effects accumulated empirically, and calculate the average RCA of traditional events that have existed stably in previous events to reflect the country’s long-term competitiveness.

• Separate the RCA of permanent events and new events. For new event RCA_add: extract the historical maximum (max(RCA)) of the RCA of temporary events added by the host country to capture the peak effect of its strategic selection of events. maximum value (max(RCA)) to capture the peak effect of its strategic selection of events.

关注数学模型 The ensuing results are presented in the subsequent table.

Model (1)–Hurdle Model (1)–Tobit Model (2)–Hurdle Model (2)–Tobit Variables Coef SD Coef SD Coef SD Coef SD

Host country 0.136* 0.21 5.864*** 0.12 0.236* 0.12 5.864*** 0.22 in 4 years Host country 1.354*** 0.41 5.520*** 0.23 1.546*** 0.21 5.520*** 0.03 t 微信公众号：数学模型 Host country 1.085*** 0.21 4.145** 0.18 0.879** 0.11 4.547** 0.12 4 years ago Athletes 0.016* 0 0.745* 0.22 0.016* 0 0.789* 0.22 [0,10] Athletes 0.241* 0.34 0.826*** 0.88 0.510* 0.12 0.726*** 0.57 [10,50] Athletes 0.789** 0.54 0.924*** 0.65 0.989** 0.23 0.954*** 0.65 [50,150] 150 athletes 0.978*** 0.25 9.314*** 1.15 0.834*** 0.12 0.614*** 1.15 and more 微信号：MATHmodels Medals_PCA(t- 3.725*** 0.28 3.42*** 4.57 3.702*** 0.23 3.42*** 4.47 4) RCA 1.548*** 0.32 1.828** 1.42 2.538*** 0.24 1.828** 1.17 RCA_usual 0.538* 0.22 0.778** 0.92 RCA_add 2.618*** 0.41 1.994** 0.93 NAE 2.911*** 0.122 2.414*** 0.48 NAE [0,20] 1.745*** 0.24 2.948** 1.15 NAE [20,50] 1.857*** 1.71 1.011** 0.75 NAE 50 and 1.912*** 0.92 1.112*** 0.36 more Num_Events 0.575** 0.24 1.148** 1.72 0.538* 0.22 1.178** 0.92 Num_sports 0.487** 1.69 1.572** 1.07 0.618** 0.41 0.994** 0.93 gi,t -3.408*** 0.75 — — -3.408*** 0.235 — — σ2 0.350*** 0.05 26.68*** 23.67 0.334*** 0.03 51.907*** 8.36 u Observations 554 — 1289 — 554 — 1289 — total Observations 554 554 noncensored Note: ***Significant at the 1 percent level; **5 percent level; *10 percent level..

According to the results in the table, strategically adding temporary dominant events (RCAadd) is the core driver of host countries’ medal gains. In Model 2, the coefficient of RCAadd is significantly positive (2.618, 1.994), indicating that host countries can significantly increase their medal gains in the short term by adding new events with the best historical per- formance (such as karate at the Tokyo Olympics) and focusing their resources on these events. In contrast, the impact of long-term competitiveness (RCAusual) is relatively limited, and the significance is not prominent in Model 1 and Model 2. Secondly, for Tobit, the number and type of events (Num_Events, Num_Sports) are significantly positive (Num_Sports coefficient 1.572 in Model 1), indicating that adding sub-events or new sports types can create more medal opportunities for weak sports countries. In addition, Model 1 shows that experience accumu- lation (NAE categorical variable) and breaking through the zero medal threshold as a host country for weak sports countries are particularly critical through the addition of events (NAE low group coefficient 2.948*); while the host effect (Host country t coefficient 5.520***) is stronger in the Tobit model, which confirms its marginal effect on the breakthrough of medals for weak countries. In summary, the host country achieves structural growth in the number of medals through a three-pronged approach to event selection: “short-term focus on strengths + expansion of event scale + preferential treatment of home resources”. This mechanism is of even greater decisive significance for countries with low competitiveness.

6 The Great Coach Effect: A Strategy Optimization Study

Based on Bayesian Change-Point Detection and Causal In- ference Models

6.1 Discovery of Great Coach Effect Based on Bayesian Change-Point

Detection

When there is a significant change in the number of medals won by a country in a certain event in a certain edition, e.g. winning at least one medal in a certain edition but failing to win a medal in several consecutive Olympic Games, or a significant increase in the number of medals won but also winning gold medals in previous editions. We believe that such significant changes are the result of the “great coach effect”. The reason for this idea is that a sudden breakthrough after a long period of downturn, or a significant increase in strength in a certain edition of the Games, may be related to an outstanding coach, even if the country had previously had a certain level of sporting strength. Such obvious turning points can be identified using a Bayesian change-point detection.

6.1.1 Data Handling

Bayesian change-point detection has a wide range of applications in fields such as medicine, such as real-time detection of sudden changes in a patient’s heart rate. Or the time point at which significant changes occur in historical data. For medal data, however, if bronze, gold, and silver medals are respectively set to 1, 2, and 3, the fluctuations in a unit of time are too

关注数学模型 large, causing the model to identify a large number of change points. Therefore, we process the medal data to make it more stable within a unit of time. The calculation uses a sliding window method, and the formula is as follows:

  a   1   · · b NGold NSilver NBronze St = 1 + (9)  NTotal c

K X St−4,ie−i Scoret = (10) i=0 微信公众号：数学模型 Before and after data processing:

微信号：MATHmodels

6.1.2 Bayesian Change-point Detection

The fundamental principle of Bayesian change-point detection involves the segmentation of data into distinct components, under the assumption that each segment follows a specific probability distribution (e.g., the normal distribution). This approach entails the estimation of the location and number of change points through the application of Bayesian inference. This method integrates the observed data, the parameter prior, and the change point prior through a joint posterior distribution, leveraging marginal likelihood to streamline the calculation. This facilitates the inference of the most probable change point configuration.

6.1.3 Evidence of Coaching Effect in the United States

By bringing in the data of the US volleyball team and the gymnastics team and using Bayesian Change-point Detection, we found that it detected the change point, i.e., great coaching effect, as shown in the table below.

Sports Change- Posterior Data Variance Confidence point Probability Segment Interval (95%)

Volleyball 2008 0.95 2004-2008 1.3 [4.8, 5.6] Gymnastics 1984 0.87 1980-1984 2.1 [7.3, 8.3]

6.2 Quantitative Evaluation of Great Coaching Effect on Medal Counts

Regression models are an important tool in statistics for estimating the relationship between variables. They are significantly superior to machine learning models such as XGBoost and random forests in terms of interpretability (cited literature). However, when using regression models to analyze the contribution of great coaches to the number of medals, it is impossible to avoid the estimation bias caused by endogeneity (i.e., the influence of the mutual relationship between variables, missing variables, etc.), which makes it impossible to accurately identify the true influence of coaches. Therefore, here we must abandon general parameter estimation methods (such as OLS, DID, and IV) and develop a parameter estimation method that eliminates endogeneity and focuses on the strong causal effect of coaches and medals, namely two-stage least squares(2SLS).

6.2.1 Regression Model Using 2SLS

Step 1: Regress Endogenous Variable D Using Instrumental Variable Scoret

The endogenous variable D indicates whether or not the coach is great. If D = 1, it indicates that the coach has a great effect; otherwise, D = 0. The expression that defines D is:

D = α0 + ∂1Score + α2RCA + α3Num_Events + α4Num_Athlete + α5NAE + m (11)

where Score is the instrumental variable strongly correlated and satisfying exogeneity (not directly affecting the existence of a great coach). The remaining explanatory variables are exogenous variables.

Step 2: Regress the Number of Medals N Using the Predicted Value D

The number of medals N can be expressed as

N = β0 + β1D + β2RCA + β3Num_Events + β4Num_Athlete + β5NAE + n (12)

where N = [Ngold, Nsilver, NBronze]T, β0, β1, β2, β3, β4, β5 ∈ R3 are coefficient.

If β1 is positive, the three components of β1 represent the contributions of great coaching effect to the gold, silver and bronze medals, respectively.

6.2.2 Model Validation

We use the United States as an example and use historical data from 1960 to 2024. First, Bayesian change-point detection is used for each sport to statistically determine the possible event of the great coaching effect. Then, MLE regression is performed on each sport using 2SLS and OLS in turn to statistically determine the impact of 2SLS and OLS on the number of medals won by great coaches for each event and compare the results with the actual values, as shown in the figure.

关注数学模型 微信公众号：数学模型 微信号：MATHmodels

Both 2SLS and OLS are explanatory of the impact of great coaches on the number of medals, but 2SLS is significantly better than OLS in terms of explanatory effect, and the problem of endogeneity is better solved.

6.3 Targeted Coaching Investments for Three Nations

The statistical results show that the United States, the United Kingdom, and France can obtain marginal benefits through strategic investment in coaches. The expected increase in the number of medals for each country after the introduction of coaches is shown in the figure below.

United States, the Great Britain, and France

The United States Magnitude Great Britain Magnitude France Magnitude

Wrestling 2 Wrestling 1 Table tennis 1 Rowing 1 Canoeing 2 Badminton 1 Judo 1 Judo 1 Athletics 1 Archery 1 Shooting 1 Gymnastics 2 Triathlon 2 Weightlifting 1 Rowing 1

The above strategy is based on two core logics: first, selecting projects with outstanding marginal benefits with the intervention of existing coaches to achieve medal growth at minimal cost; second, targeting weaknesses in the international competitive landscape (e.g., table tennis is dominated by Asia) and filling technical gaps through cross-border coach cooperation. In the long term, such investment can improveshort-term results and build sustainablecompetitiveness, especially in Olympic events with a highly concentrated distribution of medals.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

7 Insights: Strategic Resource Allocation and Path Depen-

dency in Olympic Medal Performance

For question 3, we continue the analysis of questions 1 and 2, and use Bayesian variable point detection to label the possible great coaching effects of various sports in each country in previous Olympic Games, and add them as explanatory variables to the Hurdle and Tobit models. At the same time, due to the self-reinforcing mechanism of medal dynamics, we treat the explanatory variables in the same way (i.e., (further explaining the lagged terms), and then regress them. The results are shown in the table below.

Hurdle Model Tobit Model Variables Coef SD Coef SD

Host country t 1.354*** 0.41 5.520*** 0.23 Host country 4 years ago 1.085*** 0.21 4.145*** 0.18 Athletes [150+] 0.978*** 0.25 2.314*** 1.15 Medals_PCA 1.548*** 0.32 1.828*** 1.42 Num_Events vs. Num_Sports 0.575** vs. 0.487** 0.19 1.148*** vs. 1.572*** 1.03

Note: Only display the variables to be analyzed to interpret the coefficients; ***Significant at the 1 percent level;

**5 percent level; *10 percent level.

7.1 Dynamic Attenuation of the Host Country Effect and Resource Re-

distribution

From a temporal perspective, in the short term, the coefficient of host country t is 1.354* (Hurdle model), indicating that the advantage of the host country is most significant during the current Olympic Games. In the long term, the coefficient of host country 4 years ago is 1.085* (Hurdle model), indicating that the host country effect still exists 4 years later, but the strength has decreased by about 20%.

Policy implications:

• The host country needs to transform the infrastructure into a long-term training base within 2-4 years after the event to avoid idle resources.

• Non-host countries can target the “post-Olympic trough period” of previous host countries and obtain their surplus resources (such as venue leasing and coach exchanges) through cooperation.

7.2 The “Double-Eged Sword Effect” of the Number of Events and Sports

The coefficient of the Num_Events is 0.575* (Hurdle model)**, which shows that increas- ing the number of events can improve medal opportunities. However, the coefficient of the Num_Sports is only 0.487* (Hurdle model)**, indicating that excessive diversification may dilute resources.

Policy implications: National Olympic committees need to balance “breadth vs. depth”.

关注数学模型 • Small countries: choose 3-5 high-potential sports to avoid fighting on multiple fronts.

• Large countries: leverage the advantages of multiple sports, but need to establish a “core- peripheral” echelon (e.g., track and field as the core, modern pentathlon as a supplement).

8 Sensitivity Analysis

When using the hurdle model, a binary classifier is required in the first stage to classify which countries can win at least one medal. We use a logit classifier. Therefore, we will conduct a sensitivity analysis on the selection of the binary classifier to explore whether the selection of the binary classifier will affect the interpretability of the hurdle model for the number of medals and thus affect its predictive performance. We use the random forest classifier, decision tree, 微信公众号：数学模型 and logistic regression to replace the logit classifier in the hurdle, use the output probability as the result of the hurdle stage 1, regress it, and use the logit classifier as the benchmark to compare the changes in the coefficients of each covariate in the original model.

Variables Random Forest Classifier Decision Tree Logistic Regression

Host country in 4 years 0.052 0.022 -0.057 Host country t -0.011 0.025 -0.088 Host country 4 years ago 0.062 -0.013 0.565 Athletes [0,10] -0.122 0.051 -0.041 Athletes [10,50] 0.011 0.052 0.251 微信号：MATHmodels Athletes [50,150] 0.062 -0.045 0.051 150 athletes and more 0.032 0.000 0.152 Medals_PCA(t-4) -0.052 0.052 0.142 RCA 0.012 0.069 -0.098 Medals_PCA(t-4) 0.012 -0.052 -0.095 Num_Events 0.012 0.021 0.054 Num_sports 0.041 0.065 0.013 NAE -0.032 0.054 -0.064 gi,t 0.055 -0.048 0.052 σ2 -0.011 0.054 -0.098 u Observations total 0.072 -0.067 -0.052 Observations noncensored -0.065 0.002 0.082 0.025 0.051 -0.054

As can be seen from the table, the error between all the coefficients of the covariates and the explanatory variables is less than 10%, indicating that the classifier model we selected has no significant impact on the performance of the hurdle model, and our model is relatively robust.

9 Model Evaluation

9.1 Strength

• The interpretability and performance of the Hurdle and Topit models are both strong, rather than simple machine learning algorithms.

• Before using Bayesian variable point detection, the data is first preprocessed to reflect the significance of medals and the dynamic self-reinforcement mechanism.

• When explaining the great coaching effect, the use of 2SLS eliminates endogeneity between variables.

9.2 Weakness

• Due to the limitations of the subject, the model does not introduce the influence of factors such as economics and humanities, which may lead to errors.
