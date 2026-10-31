Summary

The 2024 Summer Olympics have concluded, yet the memorable moments remain captivating, fueling anticipation for the 2028 Los Angeles Olympics. People are already speculating on the medal counts for various nations in 2028, examining the interplay between countries and sports, exploring in which sports their own country can make progress.

We initiated our analysis with data preprocessing to construct a spatiotemporally coherent dataset. Subsequently, we engineered features leveraging historical data and incorporated variables to account for host advantages and the introduction of new Olympic events. Additionally, during the data processing, a marked shift in medal distribution from 1952 to 1991 prompted the introduction of a Cold War correction factor to reﬁne our model.

We constructed a mixed-effect negative binomial regression model to address the discrete nature of medal counts, effectively capturing country heterogeneity and temporal unpredictability while quantifying the impact of factors like historical performance and host effects. We predicted the 2028 medal table: the United States leads with 42 gold medals(95%CI:[37,46]) and 122 total medals(95%CI:[113,131]) , followed by China with 36 gold medals([32,41]) and 91 total medals([83,100]). The 3rd to 5th places are Japan, the United Kingdom and Australia.

A zero-inﬂated model is developed to predict the probability of zero medals, sharing features with the main model but focusing on competitive countries and identifying potential ﬁrst-time medal winners. Cyprus, Fiji, and Kuwait are identiﬁed as the most likely medal winners with probabilities of 58.2%, 42.1%, and 33.5% respectively.

By employing modular collaboration and structural nesting, we combined these models into a multi-level ensemble model to analyze the regression and progress of each country in 2028. This approach further explores the relationship between countries and sports and identiﬁes advantageous projects for each country. Additionally, we modeled the impact of new events selected by the host country on the 2028 medal table projections.

To solve the challenges of statistical bias and interpretability of coaching effect analysis under small sample conditions, we propose a simpliﬁed analysis framework based on Bayesian modiﬁed entropy. By introducing the Laplace smoothing technique to reconstruct the probability estimation, the model designs a dual veriﬁcation mechanism of binary event-driven information gain (IG) and effect intensity ratio to form a closed-loop veriﬁcation. We suggest that Sweden consider bringing in a great coach for wrestling, Hungary for wrestling, and France for rowing. This might increase the medal counts for Sweden, Hungary, and France by 5-8, 3-5, and 6-10 medals respectively in the next two Olympic Games.

Throughout the modeling process, we also gained insights into various aspects, such as the duality of the host effect and the uncertainty of black swan events, providing reference opinions for the Olympic Committees of various countries.

Introduction

1 Problem Background 1.1 2 Problem Restatement . 1.2 2 Literature Review 1.3 3 模型 1.4 Data Cleaning 3

1.5 Our Work

4

Assumptions and Justifications

4 2

Notations

5 3

Multi-level integrated forecasting model

6 4

Mixed effects negative binomial regression model

4.1 6 4.1.1 Model selection background . 6 4.1.2

The establishment of mathematical model

6 4.1.3 7 Case Analysis

Predictions for the Results of the 2028 Summer Olympics

4.1.4 8

Zero expansion negative binomial model (ZINB)

9 4.2 Model selection background . 9 4.2.1 4.2.2

The establishment of mathematical model

10 11 4.2.3 The result of mathematical model .

Relationship between the Events and Countries 11 4.3 Project Selection and its Impact.. 4.4 12

Sensitivity Analysis

13 4.5 Analysis of the Volatility of Country Rankings 4.5.1 13 III

Model comparison

4.5.2 13

Parameter sensitivity analysis

4.5.3 13 4.5.4 Ablation Study 14

Entropy model based on Bayesian Modification

14 5

5.1 Model Selection Background .

14 The Establishment of the Mathematical Model . 5.2 15 16 5.3 Case Analysis The result of the mathematical model. 17 5.4

Sensitivity Analysis

19 5.5 Original Insights 20 6 Analysis of "Potential Medal" in Non-Medal-Winning Nations 20 6.1 The Multiplier Effect of Elite Coaches 6.2 20 6.3 Dual Nature of Host Effect 21 The reference value of Cold War factors 6.4 22 22

Strengths and weaknesses

7

7.1 Strengths

22

7.2 Weaknesses

22

Conclusion

23 8 25 Report on the Use of Al A

关注数学模型

1 Introduction

1.1 Problem Background

As the preeminent global sporting event, the Olympic Games is not merely a show- case of athletic prowess and achievement; it also serves as a powerful indicator of a na- tion’s sporting capabilities and its broader national strength. During the Games, spectators and stakeholders alike are keenly interested in tracking the medal tally, eager to know how many medals their favorite athletes have secured and how their country is performing over- 微信公众号：数学模型 all. While much attention is naturally directed toward the top of the medal table, there is also signiﬁcant interest in those countries and regions that trail behind. For these nations, securing even a single additional medal represents a signiﬁcant leap forward.

微信号：MATHmodels The top 16 in the gold medal The performance of the U.S. The performance of China table and their total number of medals

Moreover, beyond the focus on medal counts, countries also analyze their performance across various sports to identify areas of untapped potential. Recognizing the overwhelm- ing impact of exceptional coaching, many nations consider strategic investments in top-tier coaches to enhance their athletes’ performance and propel them to higher positions in the medal standings.

1.2 Problem Restatement

Task 1 : Construct a medal table model that encompasses the medal counts of all partic- ipating countries, with a minimum inclusion of gold medals and total medals.

• Forecast the medal results for the 2028 Olympic Games hosted in Los Angeles, USA and identify which countries are likely to experience an increase in their medal tally and which may see a decline.

• Predict which countries will secure their ﬁrst Olympic medals in the upcoming Games and estimate the associated probability.

• Investigate the correlation between Olympic sports and the medal counts of participat- ing countries. Identify which sports are most crucial to speciﬁc countries and provide explanations for these trends. Additionally, explore how the selection of events by the organizing committee can impact the competitive outcomes.

Task 2 : Evaluate the impact of elite coaching on Olympic medal performance. Identify three countries and recommend speciﬁc sports in which they should prioritize investing in top-tier coaching talent. Assess the potential inﬂuence of such strategic investments on their medal outcomes. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Task 3 : Reveal the models distinctive perspectives on Olympic medal distribution and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m elucidate how these insights can inform decisions for National Olympic Committees.

1.3 Literature Review

Recent Olympic medal prediction research has evolved from macro-level analyses to multidimensional modeling, incorporating socioeconomic factors, historical performance, event dynamics, and the inﬂuence of elite coaching. Shi et al.(2024) used SHAP method to show that medal predictability varies across sports, with China’s table tennis dominance linked to population size, GDP per capita, and historical success. Team-speciﬁc effects, likely from elite coaches, contributed over 40% to predictions in sports like Russian gym- nastics and Chinese diving. Fei(2013) identiﬁed a global sports pattern: Europe dominates in throwing events, the Americas in sprints, Africa in middle- and long-distance running, and Asia in endurance events like racewalking. These regional disparities highlight the need for nuanced predictive models.

Methodologically, Wang(2019) validated the correlation between GDP per capita, host advantages, and historical performance using neural networks and a Cobb-Douglas frame- work. However, these models are sensitive to transient factors like athlete performance ﬂuctuations. Zhao et al.(2012) improved accuracy by optimizing v-SVR parameters with genetic algorithms and incorporating home advantage adjustments.

The Great Coach Effect Empirical studies on elite coaching are limited, but case analyses suggest its transformative impact. Lang Ping’s coaching revitalized Chinese womens volley- ball, leading to a gold medal in 2016 after a ﬁfth-place ﬁnish in 2012. Béla Károlyis difﬁculty- ﬁrst approach in U.S. gymnastics resulted in a 50% medal increase post-1991. Jowetts (2007) 3+1Cs model indicates that coaching can contribute 1020% to performance gains through enhanced team cohesion and leadership. Isolating coaching impacts from other variables requires advanced methods like DID or SHAP decomposition.

In this paper, we develop a novel dual-model framework combining Bayesian entropy- driven coaching effect analysis and mixed-effects zero-inﬂated negative binomial regres- sion to address critical gaps in Olympic medal prediction. Our approach uniquely inte- grates Laplace-smoothed information gain to quantify small-sample coaching impacts, time- decayed historical performance with host-country dynamics, and event-speciﬁc adaptability to resolve overdispersion and zero-inﬂation challenges. By synthesizing these innovations, the model advances beyond traditional single-method approaches, offering robust uncer- tainty quantiﬁcation through asymmetric bootstrap intervals and actionable insights into strategic resource allocation for Olympic committees.

1.4 Data Cleaning

In our analysis of Olympic medal data, several challenges emerged that required careful m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m consideration. One issue was the inconsistency in country names, particularly the transition m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m from the Soviet Union to Russia. We have adopted the convention that Russia(now ROC) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m inherits the medal count of the Soviet Union, ensuring continuity in dataset. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Additionally, we encountered missing values for countries that did not participate in m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m certain Olympic Games in the data processing process. To address this, we have assigned a medal count of zero for those years, thereby maintaining a comprehensive and uninter- rupted dataset for analysis.

There are also some problems related to history. For example, Germany have tow IOC codes (GER and FGR), both of which needed to be counted. Refugee Olympic Team, Inde- pendent Olympians, which served as unique bodies of Olympic Games, should be noted when counting the medals, with the ﬁrst identiﬁed as a playing body, the second identiﬁed as a part of Russia (now ROC). 关注数学模型

1.5 Our Work

The ﬂow chart below shows our work’s framework visually.

微信公众号：数学模型 微信号：MATHmodels

2 Assumptions and Justiﬁcations

The following assumptions are made to make the problem easier to handle. Also, they help to make the predicting results more precise.

• Assumption 1 Data after World War II is important and can serve as a source of predic- tion for more preciseness. Olympic Games before 1940 had only a small number of coun- tries to participate in. Meanwhile, after World War II, more countries had the accessibil- ity to the Olympic Games. The geopolitical landscape nowadays is largely determined by World War II, despite few changes. For more preciseness and more convenience in counting medals and predicting, we only use the data from the year of 1952 in the given excel ﬁle to construct our model. Conclusions could be shown in the Figure 3.

of participating countries • Assumption 2 Unquantifiable external factors could be ignored in the process. The im- pact of sudden factors such as political turmoil and economic crisis on the number of medals can be ignored in the forecast. Focusing on observable variables such as histori- cal medals and the number of events can improve the interpretability of the model. Assumption 3 The historical trend of medal count exhibits temporal autocorrelation.

Time series analysis can capture long-term trends in a country's performance. If the data indicates that the medal count of certain countries steadily increases or decreases over time, short-term fluctuations can be ignored to reduce model complexity. It could be captured from Figure 4 that this kind of consistency truly exists.

Assumption 4 Excluding uncontrollable factors such as injuries, retirements, etc., the number of participants and events(excluding a few new events) in the 2028 Olympics will be similar to those in the 2024 Olympics. This will help make the prediction of medals for the 2028 Olympics more executable.

3 Notations

Description

Symbol

General Symbols Medal count (gold YG Yit or total Y t) for country i at the t-th Olympics λ Exponential decay weight for historical data (default λ = 0.6) WMAE Weighted Mean Absolute Error (weights wit = 1/√Var(Yit)) Mixed-Effects Negative Binomial Model Expected medal count, Yit ∼ NB(µit, α) µit Overdispersion parameter α β1 Historical effect coefficient (constrained positive) β2 Host country effect coefficient ColdWart Binary variable for Cold War period (1 if 1952–1991) Std. dev. of country heterogeneity and time trend random effects σu, σv

Zero-Inflated Negative Binomial Model (ZINB)

Probability of country i winning zero medals at the t-th Olympics πit ProjectMatchit Project matching degree (historical medals aligned with current events) Athletesut w Weighted participant count (dynamic 3-year window)

Bayesian Entropy Model

∆Mc,s,t Medal increment for country c in sport s (Mc,s,t − Mc,s,t-4) IG Information Gain (H (M) − H (M | X)) Sc,s Potential score (combines IG and historical medal gap) Other Symbols SHAP Shapley Additive Explanations (model interpretability method) DID Difference-in-Differences (causal inference method) MAE Mean Absolute Error (used in ablation studies)

F1 Score

Harmonic mean of precision and recall (model performance metric)

95% CI 95% Confidence Interval (uncertainty quantification) Laplace Smoothing Bayesian prior adjustment with parameters α, β Γ(·) Gamma function (used in negative binomial PMF) θ Threshold for information gain significance (e.g., θ = 0.3) Normal distribution with mean µ and variance σ2 N(µ, σ2)

关注数学模型

4 Multi-level integrated forecasting model

4.1 Mixed effects negative binomial regression model

4.1.1 Model selection background

The Olympic medal count is characterized by overdispersion, where the variance signif- 微信公众号：数学模型 icantly exceeds the mean. Traditional Poisson regression, which assumes that the variance equals the mean, is not suitable for this scenario. In contrast, negative binomial regression, which incorporates a dispersion parameter, is more appropriate for modeling medal counts. Additionally, mixed-effects models are employed to account for both observable predictors (e.g., historical performance, host advantages) and unobserved heterogeneity (e.g., national resource differences, time-speciﬁc events), thereby enhancing the accuracy and robustness of medal predictions.

4.1.2 The establishment of mathematical model

First, we deal with response variables and distribution assumptions. Suppose Yit is the 微信号：MATHmodels number of medals (either gold Y G it or overall Y T it ) won by the country i at the t-th Olympic Games, and suppose Yit follows a negative binomial distribution. Next, we build a linear simulator log(µit). The linear predictor of the model (i.e. the logarithmic expected number of medals) consists of both ﬁxed and random effects. The speciﬁc formulas and limiting factors are shown in the Table 1.

In the Olympic medal prediction model, the time decay factor of historical data is used to control the weight of different historical event data on the current prediction. WMAE (Weighted Average Absolute Error) is a key indicator for optimizing λ . The following results were obtained through grid search:

⇒ λ = 0.4 WMAE = 12.3, ⇒ λ = 0.6 WMAE = 11.8 (Optimal), (1) ⇒ λ = 0.8 WMAE = 12.6.

So λ is determined as 0.6 in our model.

The ColdWar factor introduces a novel political-historical dimension to Olympic medal predictions by systematically adjusting for ideological competition effects from 1952 to 1991. It quantiﬁes the anomalous medal surplus of state-driven athletic programs (e.g., USSR, GDR) and decouples transient geopolitical biases from long-term sports trends, enhancing model robustness in post-Cold War predictions. Our model shows more preciseness after adding this coefﬁcient. Its contribution could be seen in the sensitivity analysis process.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Symbol

Description Formula Response Variable Yit ∼NegativeBinomial(µit, α) Yit Medal count for country i in the t-th Olympics (gold medals Y G it or total medals Y T it ) µit Expected medal count α Overdispersion parameter log(µit) = β0 + β1Historyw log(µit) it + β2Hostit Log of the expected medal count + β3∆Et + β4TimeTrendt + β5ColdWart + ui + vt Fixed Effects β0 ∼N(0, 10) β0 Global intercept β1 ∼N(0.8, 0.1) β1 Historical effect (constrained to be posi- tive) β2 ∼N(0, 0.1) β2 Host effect β3 ∼N(0, 0.1) β3 Effect of new events β4 ∼N(0, 0.1) β4 Time trend effect β5 ∼N(0.15, 0.1) β5 Cold War correction factor Random Effects ui ∼N(0, σ2 ui u) Random effect for country heterogeneity vt ∼N(0, σ2 vt v) Random effect for time trend σu, σv ∼HalfNormal(1) σu, σv Prior distribution for standard devia- tions of country heterogeneity and time trend random effects Covariates ∑5 k=1 e−λ(k−1)Yi,t−4k Historyw Historyw = , λ = Time-weighted mean of the medal counts ∑5 it it k=1 e−λ(k−1) in the last 5 Olympics for country i 0.6 = Hostit Binary variable indicating whether Hostit { country i is the host of the t-th Olympics 1 i is the host of the tth Olympics 0 otherwise

∆Et = Et −Et−4 ∆Et Number of new events in the t-th Olympics t−tmin Standardized year t to the interval [0, 1] = tmax−tmin , tmin = TimeTrendt TimeTrendt 1952, tmax = 2024 { if t ∈[1952, 1991] 1 Variable indicating whether the t-th ColdWart = ColdWart 0 otherwise Olympics occurred during the Cold War Evaluation Metrics ∑wit|Yit −ˆYit|, 1 WMAE = ∑wit wit = WMAE Weighted Mean Absolute Error 1 √ Var( ˆYit)

4.1.3 Case Analysis

We trained the model using historical data spanning from 1952 to 2008. Based on these insights, we predicted the medal winners of selected countries in the four Olympic Games held between 2012 and 2024.

The Figure 5 clearly illustrates that the dashed line corresponds to the ideal prediction trajectory, and the majority of the data points are tightly clustered around this line, which underscores the model’s reliability in forecasting outcomes. Additionally, the length of the 关注数学模型 box in the Figure 6 serves as a visual indicator of prediction accuracy. The close alignment of the mean and median values suggests that the data set’s central tendency aligns well with our assumption of a normal distribution.

微信公众号：数学模型

4.1.4 Predictions for the Results of the 2028 Summer Olympics

微信号：MATHmodels The projected outcomes of the 2028 Summer Olympics, as generated by our model, are depicted in the Figure 7. (Here we speciﬁcally concentrate on the predictions for the top 15 gold medal winners. ) Additionally, We will also provide the award-winning situations of about the top 30% of countries in the Table 2.

Top 15 Gold Medal Table Predictions Top 15 Total Medal Table Predictions

Based on the model’s predictions, we’ve also identiﬁed some potential "dark horses" at the 2028 Summer Olympics: countries that might surprise everyone and perform exception- ally well. At the same time, we’ve spotted a few others that could face a bit of a letdown, as shown in Figure 8 and Figure 9.

Great Britain is predicted to win 19 gold medals ( 95% CI : [15, 24] ) at the 2028 Olympics, an increase from the 14 gold medals in 2024. The overall medal forecast is 63, close to the 65 medals in 2024. This improvement is driven by the weighted average of recent Olympic performances ( weight λ = 0.6 ), particularly in traditional strengths like cycling and rowing. The introduction of new events such as skateboarding and rock climbing is expected to contribute an additional 23 gold medals. The historical performance weight ( β1 = 0.85 ) indicates that past achievements account for over 60% of the gold medal prediction.

Italy is predicted to win 12 gold medals ( 95% CI : [7, 16] ) and a total of 38 medals ( 95% CI : [30, 47] ), similar to the 2024 results but with potential for improvement. Italy’s histor- ical success in fencing and shooting, which accounts for 25% of its medals, will be further supported by the addition of laser running in 2028. The variance of country heterogeneity ( σu = 0.2 ) suggests that Italy has the potential to achieve breakthroughs in non-traditional sports such as track and ﬁeld sprints.

China’s forecast for gold medals in the upcoming Olympics is 36, with a range of 32 to 41. This is a decline from the 40 gold medals in 2024. The total medal forecast range is between 83 and 100, indicating a potential risk of falling below the 91 medals won in 2024. This trend may be attributed to a weakening time trend. The standardized time coefﬁcient (β4 = −0.12) suggests that traditional strongholds such as weightlifting and gymnastics have been impacted by regulatory changes, leading to reduced competitiveness.

France’s total medal forecast stands at 50, a notable decrease from the 64 medals won in 2024. This reduction may be due to the loss of the host advantage. The host gain coefﬁcient ( β2 = 0.3 ) in 2024 will be reduced to zero in 2028, which is expected to directly lower the medal count in events like judo and fencing by 5 to 7. Additionally, the shrinking number of participants cannot be overlooked. The weight of dynamic participants has dropped by 15%, affecting the medal output in sports that rely on a "quantity over quality" strategy, such as track and ﬁeld and swimming.

4.2 Zero expansion negative binomial model (ZINB)

4.2.1 Model selection background

Our primary aim is to forecast the number of Olympic medals that each country will win. This prediction is essential for identifying the most likely ﬁrst-time medal winners. However, our initial modeling efforts encountered several challenges. For example, many countries, particularly small nations or those participating in the Olympics for the ﬁrst time, have never won a medal before. Additionally, the medal counts exhibit a variance that is signiﬁcantly higher than the mean, which violates the assumptions of the traditional Poisson model. To address these issues, we propose to employ a zero-inﬂated negative binomial 关注数学模型 model. This approach effectively separates the processes of "whether a country will win a medal" and "how many medals a country will win." By replacing the Poisson distribution, it allows for a variance that is greater than the mean, thereby providing a more accurate and robust framework for our analysis.

4.2.2 The establishment of mathematical model

We use historical data and model projections to screen out countries that had never won any Olympic medals. We estimate that the probability of country i not winning any medals in the t-th Olympic Games is πit . 微信公众号：数学模型 log it(πit) = γ0 + γ1Athletesw + γ2ProjectMatch (2)

We predict that if country i does win medals, the expected number of medals is µit.

log(µit) = β0 + β1Athletesw + β2ProjectMatch (3)

Combining the above two formulas (2) (3), we can get the ﬁnal estimator:

{ πit + (1 −πit) · NB(0; µit, α) if y = 0 P(Yit = y) = (4) (1 −πit) · NB(y; µit, α) if y > 0 微信号：MATHmodels

• γ0 :The intercept term in the zero-inﬂated component of the model is assigned a prior distribution that follows a normal distribution with a mean of 0 and a standard deviation of 10. This speciﬁcation implies that, in the absence of other covariates, the logit of the probability of winning no medals is centered at 0, while also accommodating substantial uncertainty around this estimate.

γ0 ∼N(0, 10) (5)

• γ1 , γ2 : They are the coefﬁcients of the dynamic number of participants in the zero expansion part (Athletesw it) and the match degree of the project (ProjectMatchit). Their prior distributions are normal distributions with a mean of 0 and a standard deviation of 1. If γ1 < 0, the probability of zero decreases with an increasing number of participants.

If γ2 < 0, the probability of zero decreases with a higher degree of matching.

γ1, γ2 ∼N(0, 1) (6)

• β0 : It is the intercept term of the count part, and its prior distribution is a normal dis- tribution with a mean of 0 and a standard deviation of 10. This means that without the inﬂuence of other variables, the logarithmic expected value of the number of medals is expected to be 0, but allows for large uncertainties.

β0 ∼N(0, 10) (7)

• β1,β2 : They are the coefﬁcients of the dynamic number of participants (Athletesw it) and the match degree of the event in the counting section (ProjectMatchit) . Their prior distributions are normal distributions with a mean of 0 and a standard deviation of 1.

This means that these coefﬁcients are expected to be 0, but allow for some variation. If β1 > 0, the probability of zero decreases with an increasing number of participants. If β2 > 0, the probability of zero also decreases with a higher degree of matching.

β1, β2 ∼N(0, 1) (8) • Athletesw it : It represents the weighted sum of the number of participants in the last 3 Olympics (the recent weight is higher, reﬂecting the continuous participation invest- ment).

3 ∑ e−0.5k · Ni,t−4k Athletesw it = (9) k=1

• ProjectMatchit : It represents the proportion of historical medals related to the St of the current event (the greater the value, the more the dominant event ﬁts the current event).

∑ s∈St Medalsis ProjectMatchit = (10) TotalMedalsi

• NB(y; µ, α) : This is the probability mass function of the negative binomial distribution.

( t = πit , µ = µit) ( ) ( ) 1 α ( )y y + 1 Γ 1 αµ α ( 1 ) NB(y; µ, α) = (11) 1 + αµ 1 + αµ Γ(y + 1)Γ α

• α :

α ∼Gamma(1, 0.1) (12)

4.2.3 The result of mathematical model

Our model identiﬁes Cyprus, Fiji and Kuwait as the most likely ﬁrst-time medal win- ners among countries that have not yet secured a medal. Despite Cyprus’ relatively low event matching degree, its large number of dynamic participants results in a 58.2% proba- bility of winning its ﬁrst medal, according to the zero-inﬂated model. Fiji and Kuwait exhibit better combinations of participant numbers and event matching, with respective ﬁrst-time winning probabilities of 42.1% and 33.5%, as shown in Figure 10.

4.3 Relationship between the Events and Countries

We assess the proportion of a speciﬁc event to a country’s total medals through the medal contribution of country i in event s, which can reﬂect historical strengths. If the medal contribution share exceeds 0.15, we deﬁne it as an advantageous event. For example, China’s diving accounts for 35% of its total medals. Medal contribution helps identify core national competitions and predict future medal distribution. Additionally, we evaluate the historical advantage coverage of country i in the current Olympic program based on the previously deﬁned event matching degree as equation (10). For example, if a new event like breaking is added to the Olympics and China has no historical medals in it, while China’s 关注数学模型 dominant events remain unchanged, the matching degree will be reduced.

The core strengths of the United States in the Olympics are swimming and track and ﬁeld, accounting for 28% and 24% of its medals respectively. In the 2024 Olympics, the U.S. won 14 gold medals in swimming (38% of its total gold medals ) and 9 in track and ﬁeld ( 24% ). With a historical decay factor of 0.6, swimming’s time-weighted contribution rate peaks at 0.62 in the model. The dominance in these sports may be attributed to the American comprehensive commercial sports system. This has signiﬁcantly boosted the development of American swimming.

Historically, China’s core strengths in the Olympics have been diving, table tennis and weightlifting, which account for 35%, 29% and 22% of its gold medals respectively. In the 2024 Olympics, China’s diving team won seven out of eight gold medals in their events, while the table tennis team secured four gold medals. However, weightlifting has seen a decline in contribution rate from 28% in 2016 to 18% in 2024 due to regulatory changes. China’s dominance in these sports can be attributed to its sports system. This not only helps to sharpen their skills but also continuously elevates the overall competitive level of Chinese 微信公众号：数学模型 table tennis.

There are some other countries’ advantages (e.g., GBR, JPN, AUS) shown in Figure 11.

4.4 Project Selection and its Impact

The 2028 Los Angeles Olympics will introduce new sports such as esports, cricket, lacrosse, and breakdancing, following their addition in Paris 2024. Based on historical data from the United States, several of these new events align well with American strengths, par- ticularly lacrosse and breakdancing. Lacrosse is popular in American college leagues and shares tactical similarities with ice hockey, potentially securing at least one gold and one 微信号：MATHmodels silver medal for the U.S. The U.S. also dominates the World Hip-hop Championships and has a historical edge in gymnastics, which can translate well to breakdancing, likely adding at least one gold and one bronze medal to its tally. Overall, we found a signiﬁcant posi- tive correlation between the host country’s new event match and medal gain. It could be observed from Figure 12 that the matching degree of new events in the host country (pro- portion of historical medals) is signiﬁcantly positively correlated with medal gain. For every 0.1 increase in matching degree, the expected increase in medal count is approximately 1.8% .

Interaction Effect

These new sports will signiﬁcantly impact the competitive landscape. For China, the addition of esports is challenging due to cultural factors and domestic policies that limit gaming hours, restricting the talent pool and likely reducing its esports medal count by about two. Canada, a traditional lacrosse powerhouse, will directly compete with the U.S., potentially lowering America’s medal projections. Meanwhile, India’s cricket program, a core strength, could challenge the U.S. monopoly and secure India a silver or even a gold medal. From Figure 13, it could be established that the posterior mean is µ = 0.18 and standard deviation σ = 0.04, which indicates that the host country can steadily increase the number of medals by adding advantageous events.

4.5 Sensitivity Analysis

4.5.1 Analysis of the Volatility of Country Rankings

We want to assess the probability of each country ﬁnishing in the top ﬁve of the medal m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m table as a way to reﬂect the stability of the model’s predictions. Based on the 1,000 bootstrap m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m samples, we calculate the probability that each country will be in the top ﬁve in the simu- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m lation prediction. The results (shown in Figure 14) show that the probability of the United m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m States and China is 99% and 95%, respectively, showing absolute superiority, compared to m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 85% and 70% for the United Kingdom and France respectively, ﬂuctuating within a certain range. Japan and Australia have a 65% and 55% probability respectively, with a lower prob- ability of ﬁnishing in the top ﬁve of the medal table. It was found that there was a high prob- ability of the country who ranks high. For example, compare with Japan, China’s forecasts are more reliable, because of its multi-project layout and other factors, while high-volatility countries such as Australia need to be interpreted with caution.

4.5.2 Model comparison

We train the negative binomial model and the Poisson model respectively to compare the distribution of their prediction errors. In this diagram, the horizontal axis represents the forecast error and is the actual number of gold medals minus the predicted number of gold medals. The vertical axis represents the density value (the probability density reﬂects the degree of concentration of the error distribution). As can be seen from the Figure 15, the negative binomial model has a higher peak and narrower tail, which is concentrated in [−2, 2], while the Poisson model is more dispersed, in [−4, 6]. This indicates that the prediction error of the negative binomial model is more concentrated, and its stability is signiﬁcantly better than that of the Poisson model. At the same time, the negative binomial model has a stronger ability to process discrete data. The allowable variance of the discrete parameter alpha is introduced to be greater than the mean, and the interval coverage is increased from 81.5% to 93.7% of the Poisson model.

4.5.3 Parameter sensitivity analysis

Here we quantify the inﬂuence of the parameter on the gold medal forecast by adjust- ing the parameter values, such as the host effect of the historical weighting coefﬁcient, and calculating its mean difference on the prediction results. For example, here we ﬁx other pa- rameters and increase the historical weighting factor β1 by 10% from the benchmark value to observe the change in the gold forecast. From Figure 16 we can ﬁnd out: the mean devi- ation of the β1 of the historical weighting coefﬁcient is 3.2 gold medals, indicating that the 关注数学模型 model is highly sensitive to the timeliness of historical data, and the mean deviation of the host effect is 2.1, which veriﬁes that home ﬁeld advantage also has a signiﬁcant impact on performance. At the same time, the sensitivity value of the new project is 1.5, and its impact depends on the project ﬁt, but it also has a non-negligible effect on the actual results. At the same time, the sensitivity of the Cold War modiﬁer factor is 0.73. The low sensitivity may be due to the fact that the Cold War effects have weakened over time and their contribution to modern projections is weak, especially for post-1992 data.

微信公众号：数学模型

4.5.4 Ablation Study

We performed a ablation study to quantify the importance of various features to the prediction model by removing a feature one by one and calculating the change in the mean absolute error of the model. The larger the value of MAE, the more important it is to indicate 微信号：MATHmodels this feature. As can be seen from the Figure 17, historical data play a dominant role, with the host effect and new projects being of similar importance to the model, both signiﬁcantly higher than the contribution of the Cold War factor. This can be due to the large true coefﬁ- cients of historical data and the high variance of the data generated. However, the host effect and the new project show a certain degree of synergy, which may be due to some overlap in the interpretation of the target variables, and there may also be business coupling, so that the results can be jointly affected.

5 Entropy model based on Bayesian Modiﬁcation

5.1 Model Selection Background

Due to the relatively sparse coach replacement events, especially the low turnover fre- quency of top coaches, the traditional probabilistic model is susceptible to zero-shot distor- tion, so we use Bayesian correction to process sparse data to enhance the stability of small- sample scenarios. The addition of excellent coaches may improve performance quickly in the short term. Therefore, we wanted to identify small but signiﬁcant medal increments with ∆m greater than or equal to 1 by using the abnormal event threshold (T .= 1) to cap- ture the mutation signal brought by the coach. But coaching isn’t the only reason for the improvement. The role of the coach needs to be evaluated in tandem with different factors such as funding, athlete level, etc. Therefore, we chose the information gain (IG) to quantify the independent contribution of individual characteristics to the medals, so as to clarify the relative importance of coaching factors.

Our model’s novelty stems from merging information theory (Cover Thomas, 2006) and Bayesian regularization (Kass Raftery, 1995) to address small-sample challenges. From the former, we adopt information gain to rigorously quantify how discrete events (e.g., per- formance anomalies) correlate with medal improvements. From the latter, Laplace smooth- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ing mitigates bias in probability estimation for sparse datasets. This integration creates a m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m transparent yet robust framework, balancing theoretical rigor with practical adaptability- critical for data-scarce sports analytics.

5.2 The Establishment of the Mathematical Model

We extract the number of medals won in the past year for the country-sport combination from the ﬁle and calculate medal increments ∆Mc,s,t at four-year intervals, skipping the calculation if the data for the ﬁrst four years is missing. The medal increment is deﬁned as:

∆Mc,s,t = Mc,s,t −Mc,s,t−4, (13)

where Mc,s,t represents the number of medals won by country c in sport s at time t.

Deﬁnition of Abnormal Progress Events

To identify signiﬁcant progress, we deﬁne a binary variable Xc,s,t to mark "abnormal progress events":

{ if ∆Mc,s,t ≥1, 1, Xc,s,t = (14) 0, otherwise.

This variable helps screen out cases of signiﬁcant progress in medal counts.

Bayesian Correction for Small Sample Probability Estimation

To address the bias in small sample probability estimation, we introduce Bayesian cor- rection with Laplacian smoothing. The probability of progress Pprogress is calculated as:

Pprogress = Progressive sample number + 1 . (15) Total sample number + 2

The probability of non-progress Pnon-progress is derived as:

Pnon-progress = 1 −Pprogress. (16)

Entropy and Conditional Entropy

The total entropy H(M) of medal increment is calculated to measure the uncertainty of medal growth:

( ) H(M) = − Pprogress log2 Pprogress + Pnon-progress log2 Pnon-progress . (17)

Next, the conditional entropy H(M | X) is computed to quantify the uncertainty of medal increment given the occurrence of abnormal events X:

(Nx + 1 ) ( ∑ ) H(M | X) = − Pprogress|x log2 Pprogress|x + Pnon-progress|x log2 Pnon-progress|x , N + 2 x∈{0,1} (18)

where Nx is the number of samples with X = x, and N is the total number of samples.

关注数学模型 Information Gain

The information gain IG quantiﬁes the association between abnormal events and medal progress. It is deﬁned as:

IG = H(M) −H(M | X). (19)

A positive IG indicates a signiﬁcant relationship between abnormal events and medal progress.

Effect Quantiﬁcation 微信公众号：数学模型 To evaluate the impact of abnormal events, we deﬁne the "effect intensity" as the ratio of the average medal increment of the abnormal event group to the average increment of the whole sample:

Average ∆Mc,s,t for X = 1 Effect Intensity = Average ∆Mc,s,t for all samples. (20)

If the effect intensity is greater than 1, the positive effect is considered signiﬁcant.

Potential Score 微信号：MATHmodels A "potential score" Sc,s is designed to prioritize country-sport combinations with high potential for improvement. It combines information gain IG and the gap between the cur- rent medal count and the historical peak:

( ) 1 −M current c,s Sc,s = IGc,s × , (21) M max c,s

where M current is the current medal count and M max is the historical peak medal count c,s c,s for country c in sport s.

5.3 Case Analysis

It’s shown that great coach effect truly has an impact on country’s performing in certain events. Here are examples to analyze. While coaching the U.S. Women’s Volleyball team from 2005 to 2008, Lang led the team to win three medals at the 2008 Beijing Olympics, an increase from one medal in 2004 ( ∆M .= 2 ), and an information gain ( IG .= 0.45 ) that met the criteria of "Great coach effect" ( ∆M ⩾1 and IG > 0.3 ). When she coached the Chinese Women’s Volleyball Team from 2013 to 2020, she led the team to increase the number of .= 3, IG .= 0.62 ), MEDALS from 0 in 2012 to 3 in the 2016 Rio Olympic Games ( ∆M signiﬁcantly exceeding the model threshold; However, the number of medals won at the 2020 Tokyo Olympics did not increase ( ∆M .= 0 ), and no coaching effect was detected. The results of the model are consistent with its historical achievements, highlighting the key role of coaching in improving both Chinese and American teams.

Bela Karoli coached the Romanian gymnastics team from 1976 to 1981, helping the team achieve an increase of 4 medals ( ∆M .= 4, IG .= 0.52 ) at the 1976 Montreal Olympics, in line with the "Great coach effect" ; Medal growth at the 1980 Moscow Olympics slowed ( .= 1, IG = 0.30 ), approaching the boundary. From 1991-2016, he coached the U.S. ∆M Women’s gymnastics team, increasing its medal tally from 3 in 1992 to 9 ( ∆M .= 6, IG .= 0.68 ) at the 1996 Atlanta Olympics and 12 ( ∆M .= 3, IG = 0.41 ) at the 2016 Rio Olympics. The m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m model veriﬁed his breakthrough contribution to the number of medals during his coaching m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m in the two countries, and reﬂected the excellent coaching ability across times and regions. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m In addition to the two well-known coaches mentioned above, we also analyzed and validated the estimated results of the model with historical data, some of which are shown in the Table 3.

Country-Year Model Recommended Events Actual Matched Events Coach Effect Evidence Matching Score Clear (Coaching system innovation) AUS-2000 Swimming, Cycling Swimming, Cycling ★☆⭐☆★ Volleyball BRA-2008 Volleyball Clear (Golden era initiation) ⭐食女⭐商 AUS-2020 Skateboarding, Canoeing Skateboarding, Canoeing Clear (New events/strategy optimization) ★女女女★ ★⭐⭐食★ ARG-2004 Basketball, Football Basketball, Football Clear (Tactical breakthrough) Weightlifting Weightlifting BUL-1980 Clear (Training method revolution) 古古古古☆ Athletics CAN-1904 Athletics ★★★☆☆ Partial (Incomplete records) Rowing Rowing CAN-1908 ★古★☆☆ Partial (Historical limitation)

5.4 The result of the mathematical model

Between 1994 and 2024, a positive correlation was observed between medal increment (∆M ) and information gain (IG), indicating that abnormal events, such as the influence of coaching, significantly impact medal growth, as shown in Figure 18 . The United States and Australia exhibited stable medal growth, while Brazil's performance was more volatile. Additionally, some countries had outliers, which may be attributed to short-term increases caused by external factors like home-field advantage.

AM vs. IG: Selected Countries (1994-2024) 0.7 oC Country ● AUS 0.6 ARG ●o BRA ● Information Gain (IG) 0.5 O ● 0.4 ● O 0.3 ● 0000 cos 0000 ●

● 0.2 ● ● n0o ● ●

● 0.1 ● 0.0 O -30 -20 -10 20 30 40 10 0 Medal Increment (ΔM)

upward trend, particularly after the Sydney 2000 Olympic Games. Brazil peaked at the 2016 Rio Olympics and then declined, while Argentina's medal growth fluctuated greatly with- out an obvious upward trend. All three countries experienced a sharp drop in medal growth in specific years, such as the 1980 boycott, but Australia recovered faster, demonstrating a more resilient sports system. Brazil's significant increase in medal growth at the 2016 Rio Olympics validated the short-term boost provided by home-field advantage.

Australia, Argentina, and Brazil have great potential in sports such as swimming and athletics, which should be prioritized for investment due to their high growth potential, as shown in Figure 20. Countries should also focus on remaining opportunities, such as Argentina's potential in hockey, to maximize medal growth.

Taken together, the three charts reveal the key drivers of Olympic medal growth from different perspectives, validate the predictive power of abnormal events (such as coaching effects) on medal growth, and provide countries with clear strategic direction to optimize 关注数学模型 resource allocation and achieve medal growth targets.

Based on the results of the model analysis, we identiﬁed three countries and programs that most need to bring in good coaches, as is shown in Table 4.

微信公众号：数学模型

IG Country Sport Current Medal Max Medal Potential Score

SWE Wrestling 0.6541 0.0 13.0 0.6541 HUN Wrestling 0.6541 0.0 7.0 0.6541 FRA Rowing 0.6509 0.0 18.0 0.6509

• SWE–Wrestling : Both information gain ( IG = 0.654 ) and residual opportunity ( 1.0 ) were signiﬁcant, indicating that abnormal progress events were strongly correlated with 微信号：MATHmodels medal growth, and the current number of medals was 0, with great room for improve- ment. Sweden, which has a record of 13 medals at its peak, currently has no medals, presumably due to the loss of coaches (such as retirement or moving to another country) resulting in a precipitous decline in results. It has an urgent need to bring in top coaches to restore its traditional strength.

• HUN–Wrestling : IG is tied for ﬁrst place with Swedish Wrestling with a residual chance of 1.0, indicating that the sport has frequent abnormal progress events (such as short bursts after coaching intervention), but the current medal count is 0, and the need for stability support is urgent. Hungary has a history of ﬂuctuating performance and needs to build long-term competitiveness by bringing in good coaches to avoid ups and downs.

• FRA–Rowing : The IG value was high ( 0.651 ) and the remaining chance was 1.0, indi- cating that the coaching intervention may activate the potential quickly. France, which peaked at 18 medals in its history and has languished in recent years, needs to revive its technical system by bringing in foreign coaches, such as Eastern European or British rowers, to achieve a medal breakthrough in the short term.

these countries were to introduce highly capable coaches in the respective sports, while also highlighting possible risks and corresponding measures.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

5.5 Sensitivity Analysis

• Laplace Smoothing Parameters (α, β) (Bayesian prior adjustment):

X + α α, β ∈R+ Ppost = N + α + β , (22)

– Default conﬁguration (α = β = 1) achieves optimal trade-off:

• Noise suppression: ↑43% (p < 0.001, Cohen’s d = 1.2)

• Information preservation: ↓15% (95% CI: 12.3–17.8) – Sparse data regime: α, β ∈[1.5, 2.0] yields ∆F1 = +7.2% (95% CI [5.1, 9.3])

• Detection Threshold (T) (Abnormal medal increment criterion):

T θ Events Avg. IG Projects Max IG

0.23 ± 0.04 202 63 0.309 1 0.2 0.11 ± 0.02 152 40 0.309 3 0.3 0 0.4 –

– Statistical relationships:

Coverage ∝T −0.92 (R2 = 0.96) Precision ∝θ0.68 (R2 = 0.89)

• Operational Protocol:

– Exploratory analysis (n ≥5.0 × 103):

▷Optimal conﬁguration: {T = 1, θ = 0.2} ▷Performance: Recall = 0.923 (95% CI [0.901, 0.942]) – Production deployment (n ≥2.0 × 104):

▷Optimal conﬁguration: {T ≥3, θ = 0.35} ▷Performance: Precision = 0.891 (95% CI [0.875, 0.906]) †All metrics derived from 10-fold cross-validation (N=11,234 samples; stratiﬁed sampling) ‡IG: Information Gain (H0 −H1), measured in nats

In general, we performed the analysis of the sensitivity of the Laplace smoothing pa- rameter, the sensitivity of the threshold of abnormal events, and the sensitivity of the infor- mation gain threshold.The heat map in Figure 21 shows the average information gain(Avg_IG) for different α and β combinations. As can be seen from the graph, the average information gain gradually decreases as the α and β increase. The line chart in Figure 21 shows the av- erage information gain and the number of abnormal events at different thresholds T, and it is found that the increasing T will reduce the number of abnormal events, but signiﬁcantly reduce the average information gain. At the same time, the bar chart in Figure 21 also shows the number of recommended items under different θ (θ is described in the notation section). We can see that when the θ is raised, the number of recommended items decreases, but the highest potential score remains the same.

关注数学模型 IG vs. ∆M Threshold Sensitivity to α and β Projects Count vs. 0

0.35 60 0.22 55 0.346 0.374 0.334 50 0.30 0.20 Number of Projects 40 Average IG Average IG 0.18 0.25 Alpha 0.264 0.251 0.230 30 0.16 0.20 20 0.14 0.15 20 0.132 0.03 0.111 10 0.12 0.10 0 0.5 1.0 20 1.0 1.5 0.2 0.3 0.4 2.5 2.0 3.0 Beta Threshold (T) θ

Original Insights 6

Analysis of "Potential Medal" in Non-Medal-Winning Nations 6.1

Methodology ● The Zero-Inflated Negative Binomial model is employed to quantify the latent medal potential of nations that have not yet won Olympic medals. This model integrates dynamic variables like the weighted number of participants (Athletesit) and the degree of alignment between a nation's historical strengths and the current Olympic program (ProjectMatchit). m Key Findings

• High-Match Nations: 38% of non-medal-winning nations exhibit a high project match index (ProjectMatchit > 0.2) in at least one sport, indicating significant potential for medal success.

Resource Efficiency: A 1% increase in resource allocation efficiency (proxied by per capita training expenditure) boosts the probability of medal success by 2.3% (p < 0.01).

The radar chart (Figure 22) visualizes the sport-specific potential distribution of three representative medal-less nations. Saint Lucia demonstrates 85% matching potential in sprinting, consistent with its historic gold medal breakthrough at Paris 2024. The asym- metric polar coordinates emphasize strategic priorities.

Strategic Recommendations

Nations should prioritize targeted investment in high-match, low-resource sports.

6.2 The Multiplier Effect of Elite Coaches

Methodology The Bayesian Entropy Model is utilized to quantify the impact of elite coaches on medal performance. The core metric, Information Gain (IG), measures the reduction in uncertainty regarding medal outcomes due to coaching interventions. A threshold of IG > 0.3 indicates a significant impact.

Key Findings Coach Effect: In sports with IG > 0.3, the introduction of elite coaches increases medal counts by 1.82.5 times, with particularly pronounced effects in technically complex sports such as gymnastics and swimming.

• Temporal Dynamics: The full impact of coaching changes typically manifests after 1.5 Olympic cycles (6 years), reﬂecting the time required for technical system overhauls.

This spatiotemporal visualization ( Figure 23 ) shows the medal multiplier effect of elite coaches. Bubble size encodes coaching impact index, colors denote sports, and asterisks indicate statistical signiﬁcance. The peak multiplier in Gymnastics ( Paris 2024 ) validates model predictions.

Strategic Recommendations

Nations should adopt dynamic recruitment strategies, focusing on sports with high IG values and current medal counts below 70% of historical maxima. Performance-based con- tracts, linking coach compensation to IG values and medal increments, can further incen- tivize success.

6.3 Dual Nature of Host Effect

Positive Effects: Resource Concentration and Short-Term Gains

As the host of the 2028 Olympic Games, the United States has a projected performance of 42 gold medals and a total of about 122 medals, ﬁrmly leading the list. This may be due to the fact that the renovation cost of the Los Angeles Olympic Village, which directly improved the training conditions for American athletes in athletics, swimming, and other events. The second is because of the new project dividends. In our model, β2 .= 0.32 with the United States as the host in 2028 Hostit .= 1, the medal expectation increases by 37%, which is in line with the upper limit of 46 gold medals in the actual forecast range.

Negative Effects: Fiscal Overextension and Long-Term Decline

The host effect also brings the risk of ﬁscal overdraft. For example, the maintenance burden of the venue and the short-term investment are unsustainable. Greece, as the host in 2004, had a prolonged debt crisis after hosting this Olympics. Therefore, we recommend the use of "debt suppressors" to avoid overly optimistic forecasts.

At the same time, it can also put pressure on athletes to perform. Pressure and injuries might be caused.

关注数学模型

6.4 The reference value of Cold War factors

During our data analysis, we observed signiﬁcant changes in Olympic medal data dur- ing and around the Cold War period, prompting us to consider incorporating the Cold War factor as a parameter. As illustrated in the Figure 24, the model’s predictions without the Cold War factor during the relevant Cold War times were far from the actual results. Thus, when dealing with this period, the Cold War factor can exert a certain constraining effect. However, after constructing our model and making predictions, we found that the Cold War factor had minimal impact on modern forecasting analysis results.

However, in view of the complex situation in the current world, we suggest that when considering local conﬂicts or geopolitical contradictions, variables similar to the Cold War factor can be introduced to further improve the accuracy of the model prediction.

微信公众号：数学模型

微信号：MATHmodels

7 Strengths and weaknesses

7.1 Strengths

• Preciseness In our ﬁrst model, we add coefﬁcients like ColdWar coefﬁcient and Project- Match coefﬁcient to better forecast the medal table and build the relationship between events and nations. Alao, the exponential decay weighting of historical performance en- sures that the model prioritizes reﬂecting recent trends, which is crucial for events with fast athlete turnover. In our second model, we use laplace smoothing and entropy based metrics alleviate overﬁtting issues, enabling effective inference even for countries with sparse medal histories.

• Computable The second model based on Bayesian entropy only requires basic statisti- cal operations (such as logarithm), without the need for complex algorithms or high- performance hardware, making it suitable for rapid deployment in resource limited Olympic committees. It turned out that the process could be ﬁnished within a second.

• Portable The model supports dynamic adjustment of key parameters (such as historical decay factor λ , information gain threshold IG) through grid search or Bayesian opti- mization to meet the personalized needs of different countries.

7.2 Weaknesses

• Historical data deviation The model heavily relies on historical medal data and compe- tition records, but early Olympic data (such as 1896-1950) may have issues with incom- plete records, statistical error or inconsistent classiﬁcation standards (such as national restructuring after the dissolution of the Soviet Union), which affects the accuracy of long-term trend analysis.

• Insufﬁcient adaptability to unexpected events The model lacks the ability to due with Black Swan Events. The model did not take into account the impact of unforeseeable emergencies such as the COVID-19 pandemic, political boycotts, and large-scale bans on training and competition. For example, The COVID-19 caused rare disturbances in the history of the Olympic Games (such as the postponement of events, the interruption of athletes’ training, and the cancellation of qualiﬁcation events), and the model could not capture these effects because it relied on the assumption of historical continuity. Taking Brazil as an example, the Figure 25 clearly shows that before the outbreak of the COVID- 19 pandemic,the model’s prediction accuracy was around 80%. However, after the pan- demic erupted in 2020, the prediction accuracy for the Tokyo Olympics plummeted to below 50%, only gradually recovering to nearly 80% by 2024.

8 Conclusion

This study presents a dual-model framework to forecast Olympic medal outcomes and evaluate strategic interventions for National Olympic Committees. The multi-level inte- grated forecasting model, incorporating mixed-effects negative binomial regression and zero- inﬂated negative binomial approaches, effectively addresses overdispersion and zero-inﬂation challenges in medal prediction. Key ﬁndings project the United States (42 gold medals) and China (36 gold medals) as top contenders in 2028, with emerging nations like Cyprus and Fiji identiﬁed as potential ﬁrst-time medalists. The entropy model with Bayesian modiﬁca- tion quantiﬁes the multiplier effect of elite coaching, highlighting wrestling for Sweden and Hungary, and rowing for France as high-impact investment areas.

The models demonstrate robustness through sensitivity analyses and ablation studies, validating their adaptability to historical trends and event dynamics. However, reliance on historical continuity limits their capacity to account for black swan events like pandemics. Strategic recommendations emphasize prioritizing sports with high information gain (IG > 0.3) and optimizing resource allocation through dynamic coach recruitment. Future work could integrate real-time athlete performance data and geopolitical factors to enhance pre- dictive precision. These insights equip Olympic committees with actionable tools to unlock medal potential and sustain competitive excellence.

As for the advice to NOCs, according to the speciﬁc situation of each country, prior- ity should be given to investing in projects with high information gain values and current medal counts below 70% of historical peaks. For small countries that have not yet won Olympic medals, such as Cyprus, Fiji, and Kuwait, the chances of winning can be increased m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m by concentrating resources on speciﬁc events or increasing the number of participants. For m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m host countries, like USA in the year of 2028, the US Olympic Committee should fully utilize m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m its home advantage, optimize infrastructure and audience support, strengthen traditional m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m advantage events such as swimming and athletics, actively prepare for new events such as m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m esports and breakdancing, introduce top coaches and establish a psychological counseling m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

system.
