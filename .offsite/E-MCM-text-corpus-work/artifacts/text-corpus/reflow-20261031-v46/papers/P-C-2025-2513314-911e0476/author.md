MCM/ICM

Summary Sheet

Summary

The Olympic medal count fluctuates over time, driven by various influencing factors. Through a comprehensive analysis of historical data and predict projections for 2028, we have identified key trends and valuable insights.

First, we conducted an exploratory data analysis to understand the distribution characteristics of our target variable, providing a solid foundation for our modeling process.

For Task 1, our objective is to predict the medal counts for the 2028 Olympic Games. To improve accuracy and quantify uncertainty, we propose a Bayesian Hierarchical Dirichlet- Multinomial (BHDM) Model, which captures the discrete, sum-constrained nature of medal counts while addressing overdispersion and cross-country heterogeneity through hierarchical priors.

A key strength of this model is its robust uncertainty quantification. Each country’s medal count follows a Dirichlet-Multinomial distribution with latent rates governed by country- specific regression coefficients and a Gamma-distributed concentration parameter. MCMC-

based posterior inference provides 95% credible intervals, assessing both medal forecasts and extreme outcomes like "ice-breaking" probabilities. By analyzing posterior distributions, the model offers interpretable insights into key predictors, ensuring informed decision-making under uncertainty.

This method exhibits strong performance, achieving R2 of 0.85 for total medals and 0.80 for gold medals, surpassing all baseline models. Our 2028 projections show the U.S. winning 146 medals (95% CI: 136–156) and 53 golds (95% CI: 50–56), an increase from 2024, while China’s total medals decline to 82. We also computed ice-breaking probabilities, with Malaysia (68.6%) and South Sudan (39.0%) most likely to win their first medals. Regression analysis identified key sports for the U.S., China, the U.K., and France, offering strategic insights for host nations to optimize medal prospects.

For Task 2, we investigate the “Great Coach” effect. First, we define great coaches and construct a national-level great coach variable to quantify each country’s coaching strength. We then incorporate this variable into the BHDM model and analyze its impact through regression coefficients.

The results indicate that great coaches significantly influence both total and gold medal counts. Specifically, for the United States, China, and Japan, a one-unit increase in this vari- able leads to an expected medal count increase of 3.74%, 4.55%, and 2.87%, respectively. Additionally, we examine key sports in these three nations to assess the impact of this effect.

To test the robustness of our model, we conducted sensitivity analyses on both the weakly informative priors and the assumption of equal medal distribution. The results indicate that, despite adjustments in parameters and distributions, the model maintains reasonable predictive performance, with onlyminor deviationsfrom theoriginal baseline, demonstratingits robustness.

For Task 3, based on the comprehensive modeling process above, we derived three additional insights: Economic level determines medals, Home Turf and Aligned Systems Prevail, and Emerging Sports Aid Low-GDP Countries. We communicated these insights in a letter to the NOC, aiming to enhance their strategies and help nations secure more gold medals.

Quantification, Regression Analysis, Credible Intervals

Introduction

1 3 1.1

Background

模型 1.2

Problem Restatement

3 1.3 4 Our Work

5 Assumptions and Justifications 2

Notations

5 3

Data Pre-processing 5 4 Data Cleaning 6 4.1 4.2 A glimpse of dataset 6

Task 1: Predicting Medals of 2028 LA Olympics 6 5 Key Variables Influencing Olympic Medal Success 5.1 6 5.2

Bayesian Hierarchical Dirichlet-Multinomial (BHDM) Model

7 10 5.3 Projects of LA 2028 .

11 5.4 The country that will achieve a Breakthrough From Zero 12 5.5 Important Sports and Home Event Impact

Task 2: Dive Into Great Coach Effect 13 6 6.1 What is a Great Coach? 14 Great Coach Affect the Medals 6.2 14 Invest in Great Coach and Estimate its Impact 15 6.3

16 7

Sensitivity Analysis for τ2 Values

16 7.1

Sensitivity Analysis of Equal Distribution Assumptions

17 7.2

Strengths and Limitation of the Proposed Model

17 8

Task 3: Other Original Insights of Our BHDM Model

19 9 19 Economic level determines medals 9.1 9.2 Home Turf and Aligned Systems Prevail 19 9.3 Emerging Sports Aid Low-GDP Countries 20 A letter to inform NOC 20 9.4

Some insights about Olympics Medal Counts 21 信 微

1 Introduction

1.1 Background

The Olympic Games, held every four years, bring together the world’s top athletes to compete in a wide range of sports. Since the first modern Olympics in 1896, the event has grown significantly in scale, with more countries participating and more events being introduced. 微信公众号：数学模型 Medal counts serve as a key indicator of national sports performance, reflecting a country’s investment in athletics, talent development, and international competitiveness.

微信号：MATHmodels Predicting Olympic medal counts is an important challenge, as it provides insights into national sports strategies and performance trends. Various factors influence a country’s medal prospects, including economic resources, population size, sports infrastructure, and historical performance. Additionally, host nations often experience a boost in medal counts due to home-field advantages and increased investment. A robust predictive model can help sports organizations allocate resources efficiently and set realistic goals for future Olympic Games.

Beyond national investment, coaching plays a critical role in athletic success. Some elite coaches have significantly impacted multiple countries’ performances, demonstrating a “Great Coach” effect. By analyzing historical data, it is possible to quantify this effect and identify sports where hiring top-level coaches could maximize a nation’s medal potential. Understanding the role of coaching in Olympic success can provide strategic recommendations for countries aiming to improve their performance.

1.2 Problem Restatement

The distribution of Olympic medals is a key topic of interest for analysts, sports federations, and policymakers. Medal standings reflect national athletic strength, investment in sports development, and strategic resource allocation. This study focuses on developing a predictive model for Olympic medal counts and exploring the underlying factors that influence national m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m performance. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Specifically, our objectives include: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m • Developing a mathematical model to predict the number of Gold and total medals for each country in the 2028 Los Angeles Summer Olympics, incorporating factors such as historical performance, host nation advantages, and event distributions.

• Estimating the likelihood of countries earning their first Olympic medal and analyzing the probability of new medal-winning nations emerging.

• Examining the relationship between specific sports events and national success, identifying key disciplines that contribute significantly to a country’s medal tally.

• Investigating the potential impact of elite coaches on national performance, quantifying the "Great Coach" effect, and recommending strategic investments in coaching for selected countries. By addressing these questions, this study aims to provide valuable insights into Olympic medal trends, helping national Olympic committees optimize their training programs and re- source allocation for future competitions.

1.3 Our Work

Our workflow is illustrated in Figure 2. Before modeling, we first conducted model assump- tions (Section 2) and data exploration (Section 4.2) to facilitate the modeling process. After exploring the data distribution, we identified eight key variables (Section 5.1) and constructed a Bayesian Hierarchical Decision Model (BHDM) (Section 5.2) to better fit our observed distri- butions.

A glimpse of dataset

Model Assumption

Equal Medal Country Distribution Heterogeneity Distribution Some insights about Olympics Medal Counts To: Country Olympic Committees From: Team #2513314 Data: January 27, 2025 Dear Country Olympic Committee leaders:

… Overdispersion and Heavy Tails Sum Fixed and Discrete

Task 2: Dive Into Great Coach Effect Task 1: Predicting Medals of 2028 LA Olympics

BHDM Model Setup

Key Variables for Medals Why NOT Other Models? Dataset Coaching Two-phase RF Deep Learning 𝜽𝜽𝒊𝒊= 𝝓𝝓𝒊𝒊𝒆𝒆𝒆𝒆𝒆𝒆𝒙𝒙𝒊𝒊 𝑻𝑻𝜷𝜷𝒊𝒊 𝑿𝑿𝟏𝟏−𝑿𝑿𝟖𝟖 𝜷𝜷𝒊𝒊follows a weakly informative prior

Breaking the Ice Probability Posterior Distribution

The country that will achieve Important Sports and a Breakthrough From Zero Home Event Impact

Sensitivity Analysis

All Ability Coach Great Coach Poisson Neg. Binomial 𝑿𝑿𝟗𝟗 Database Predictive Uncertainty and Discrete Outcomes Posterior Summary Our BHDM Model of 𝑿𝑿𝟗𝟗

Projects of LA 2028 Japan China United State

Task 3: Other Original Insights of BHDM

Sensitivity analysis of weak

Sensitivity Analysis of Equal

Economic level determines medals priors for β

Distribution Assumptions

Proved to be Great Robustness! Home Turf and Aligned Systems Prevail Emerging Sports Aid Low-GDP Countries

During the modeling process, we also considered alternative models; however, they were either inconsistent with the data distribution or incapable of capturing the differences between countries, leading to their exclusion. Using our model, we then projected the medal distribution for the 2028 Los Angeles Olympics along with its 95% prediction interval. Additionally, we analyzed breakthrough probabilities, identified key sports for specific countries, and proposed adjustments to the sports program for the host nation.

To investigate the "Great Coach" effect, we first cross-referenced Wikipedia databases with 关注数学模型 our dataset to identify elite coaches. We then quantified each country’s coaching strength and incorporated it as a new variable into our BHDM model. By analyzing the posterior parameters of this variable for three selected countries, we assessed the impact of great coaches on their Olympic performance (Section 6).

Subsequently, we conducted a sensitivity analysis to determine the influence of model parameters and distributional variations on our results, thereby validating the robustness of our model (Section 7). Finally, based on our entire modeling process, we derived three original insights and drafted a letter to the COC to communicate these findings (Section 9).

微信公众号：数学模型

2 Assumptions and Justifications

To simplify our modeling process, we make the following assumptions:

Assumption 1 (Medal Distribution Assumption): The distribution of medal counts to be

modeled necessitates integer-valued predictions that sum to a fixed total, often exhibits overdis- persion and heavy tails. This forms our core assumption and directly informs our choice of modeling approach. In Section 4.2, we will validate this assumption through visual analysis.

Assumption 2 (Equal Distribution Assumption): The composition and skill levels of athletes

representing each country, as well as the events featured in the 2028 Olympics, will be largely consistent with those of the 2024 Paris Olympics. Given the absence of data for the 2028 Games, 微信号：MATHmodels we assume that key factors such as event availability and athlete participation remain comparable to those in 2024. In Section 7.2, we will explore relaxations of this assumption.

Assumption 3 (Country Heterogeneity Assumption): Each country excels in different sports

and exhibits varying adaptability to the same set of variables, leading to cross-country hetero- geneity. In Section 5.2, we will explore this phenomenon in detail and incorporate it as a key assumption in our modeling approach.

3 Notations

Symbol

Description 𝑁 Number of countries 𝑇 Total medals across all countries Covariate (feature) vector for country 𝑖 x𝑖 𝝁𝛽 Global mean of coefficient vectors 𝜙𝑖 Concentration parameter for country 𝑖 𝜃𝑖 Latent rate for country 𝑖 𝑋1,𝑖 Historical medal record 𝑋3,𝑖 Host nation flag (binary) 𝑋5,𝑖 Athletics events 𝑋7,𝑖 Ball sports events 𝑋9,𝑖 Great Coach variable (aggregate coaching ability)

4 Data Pre-processing

Symbol

Description 𝑀𝑖 Medal count of country 𝑖 𝑇new Total medals in a future Olympics Random coefficient vector for country 𝑖 𝜷𝑖 Σ𝛽 Covariance matrix (weakly informative prior) 𝛼𝜙, 𝛽𝜙 Hyperparameters for 𝜙𝑖(Gamma distribution) 𝑀𝑖,new Predicted medal count of country 𝑖in future 𝑋2,𝑖 Athlete delegation size 𝑋4,𝑖 Social system congruence (binary) 𝑋6,𝑖 Tactical & strength events 𝑋8,𝑖 Emerging events 𝐺, 𝑆, 𝐵 Gold, silver, and bronze medal counts 𝐴 Coaching ability metric (6G + 3S + B)

Before proceeding with modeling, we conducted data cleaning and an initial exploratory m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m analysis to better understand the dataset’s characteristics. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

4.1 Data Cleaning

Upon inspection, we identified missing values in the summer0ly_programs . csv file. These gaps resulted from certain events not being held in specific years, leading to the absence of corresponding records. To address this issue, we replaced the missing values with 0.

Additionally, inconsistencies were found in the representation of country codes (NOC) across the four datasets: summerOly_programs.csv, summerOly_hosts.csv, summerOly_medal_counts.csv, and summerOly_athletes.csv. To standardize these variations, we converted all country codes into a unified three-letter format. However, for clarity and readability, country names are used instead of three-letter codes in all subsequent discussions within this paper.

Furthermore, we identified newly established countries as well as temporary representative teams, such as the Refugee Olympic Team. Since these entities lack historical records, all their past data were initialized with 0 to maintain consistency across the dataset. However, an exception was made for Russia, as its NOC was updated to ROC in 2020. In this case, historical data associated with Russia were retained to reflect its prior participation accurately.

4.2 A glimpse of dataset

Understanding the distribution patterns of gold medals and total medals is essential, as it directly impacts the selection of appropriate modeling strategies for further analysis. To illustrate this, Figure 3 presents the country-level distributions of gold and total medals of Olympics history. Notably, these distributions demonstrate clear signs of overdispersion and heavy tails, which stem from the inherently discrete nature of medal counts and the constraint of a fixed total sum.

Distribution of Total Medals and Gold Medals by Country 2500- Total Medals Number of Medals Gold Medals 2000-

1500

1000

500

0 Kecnya Nena d a ro Franoce Vusvia Norhk orea aand Pueo Rco [ ku n Boha E8pt Senoal Norccda onia United States HuBmry East Germany South Korea Souh iicea Czech Republic Iindocssa Cllia ESstnia Irdera Framnc Taisn KoOSOV Sneorc Cenada ordan plidues Enntea pemumy Ceylon Coatina Poftual Lavia Dominican Republic Denmark Kyrgyzstan l Baelain Aqetiina Iceland Zaqia Kuwt Cypus Nier Almnia Yyuosvava vn Vin nds poruuadl Lwwn and Switzerland Spain Braz[ Ukraine Tley Mexico Polaod 即 Sai oia Lvia Guyana roomosa [laly Cda

Country (NOC)

Task 1: Predicting Medals of 2028 LA Olympics 5

5.1 Key Variables Influencing Olympic Medal Success

Building upon insights presented by Schlembach et al. [7], it becomes evident that a nation's ability to secure Olympic medals stems from an interplay of diverse yet interlinked factors. In the following, we examine three pivotal dimensions—economic capacity, hosting advantages, and event-specific attributes—and introduce key explanatory variables associated witheachdomain!

关注数学模型

1. Economic Capacity.

Historical Medal Record (𝑋1): Reflects a country’s medal haul in the immediately preceding Olympic cycle (for gold-medal-focused forecasts, this specifically denotes the previous count of gold medals). A strong performance history is frequently underpinned by 微信公众号：数学模型 consistent investment in athletic programs and robust training infrastructures.

Athlete Delegation Size (𝑋2): Represents the total number of athletes sent to the current Games, serving as a proxy measure of institutional support and the breadth of a na- tion’s talent pool. Larger delegations often correlate with stronger financial backing and more extensive development pathways in multiple sporting disciplines.

2. Hosting Advantages.

Host Nation Flag (𝑋3 ∈{0, 1}): Indicates whether a nation is the host (𝑋3 = 1). Host countries frequently capitalize on superior familiarity with the local environment, elevated fan 微信号：MATHmodels support, and logistical conveniences.

Social System Congruence (𝑋4 ∈{0, 1}): Identifies nations whose social or institutional struc- tures are closely aligned with those of the host (𝑋4 = 1). Such alignment can minimize cultural barriers and facilitate smoother acclimatization, indirectly bolstering athletic per- formance.

3. Event-Specific Attributes.

Substantial heterogeneity exists across Olympic events, with certain countries historically excelling in specific domains. Cultural traditions, regional training practices, and even genetic predispositions can foster a competitive edge in certain sports [6]. To capture this diversity, we classify events into four key segments:

Athletics Events (𝑋5): Comprising all track and field competitions, a domain frequently marked by widespread global participation and prominent displays of speed, endurance, and agility.

Tactical & Strength Events (𝑋6): Encompassessportssuchasfencing, racquetsports, wrestling,

and weightlifting, where strategic thinking, technical skills, and physical power play in- terdependent roles.

Ball Sports Events (𝑋7): Encompassing team-focused competitions including football, bas- ketball, and volleyball, these events rely heavily on synergy among participants and well-established support systems.

Emerging Events (𝑋8): NewlyintroduceddisciplinesorcontestsdebutinginthecurrentOlympic cycle. Nations pioneering these events may enjoy early-adopter advantages but also face higher uncertainty due to the limited availability of historical data.

Overall, these variables not only serve as potential predictors in quantitative analyses but also offer a structured lens for examining how resources, environmental factors, and sport-specific nuances collectively shape a nation’s Olympic performance.

5.2 Bayesian Hierarchical Dirichlet–Multinomial (BHDM) Model

Section 4.2 reveals that Olympic medal data typically demand integer-valued predictions that sum to a known total, often exhibit overdispersion and heavy tails, and require partial pooling m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m to handle cross-country heterogeneity. Under this distributional constraint, deep learning and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m machine learning methods (e.g., RNN and two-stage RF) are clearly unsuitable, as they fail m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m to enforce the fixed-total and discrete conditions without special modifications. Statistical approaches such as Negative Binomial and Poisson are also inadequate due to their poor handling of long-tailed data. While a standard Bayesian Multinomial Model can effectively model such data, it does not satisfy our Country Heterogeneity Assumption, as it assumes a shared 𝜷across all countries, which is incompatible with our framework. The Bayesian Hierarchical Dirichlet–Multinomial (BHDM) model addresses these challenges by combining a Dirichlet–Multinomial likelihood, which enforces both discreteness and sum constraints, with hierarchical priors on regression parameters, enabling each country to have its own coefficient vector.  be the observed medal Model Setup. Let 𝑁be the number of countries, and let  𝑀1, . . . , 𝑀𝑁 counts, with the total 𝑁 ∑︁ 𝑇= 𝑀𝑖. (1) 𝑖=1 For each country 𝑖, we define a covariate vector x𝑖and a random coefficient vector 𝜷𝑖. In our setting, we adopt a weakly informative prior for 𝜷𝑖, specifically assuming that

  𝝁𝛽, Σ𝛽 , 𝑖= 1, . . . , 𝑁, 𝜷𝑖∼N (2)

with 𝜏2 = 1. Σ𝛽= 𝜏2𝐼𝑝 and

This choice reflects our prior belief that, while allowing for moderate variation in the regression coefficients across countries, the individual effects should not be overly dispersed. The weakly informative prior thus provides regularization without imposing overly restrictive assumptions, enabling the data to primarily inform the posterior inferences. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We additionally introduce a concentration parameter 𝜙𝑖for country 𝑖: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 𝜙𝑖∼Gamma(𝛼𝜙, 𝛽𝜙). m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (3) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Each country 𝑖has an associated feature vector m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

⊤, x𝑖=  𝑋1,𝑖, 𝑋2,𝑖, 𝑋3,𝑖, 𝑋4,𝑖, 𝑋5,𝑖, 𝑋6,𝑖, 𝑋7,𝑖, 𝑋8,𝑖 (4)

Combining these, each country’s latent rate is

  x⊤ 𝜃𝑖= 𝜙𝑖exp . 𝑖𝜷𝑖 (5)

 follows a Dirichlet–Multinomial distribution: Conditioned on {𝜃𝑖}, the vector  𝑀1, . . . , 𝑀𝑁  ∼Dirichlet-Multinomial 𝑇; 𝜃1, . . . , 𝜃𝑁  𝑀1, . . . , 𝑀𝑁 , (6)

ensuring each 𝑀𝑖is integer-valued and that Í𝑁 𝑖=1 𝑀𝑖= 𝑇. Let M = (𝑀1, . . . , 𝑀𝑁) and recall 𝜃𝑖as in (5). Posterior Distribution. Combining the likelihood Eq. (6) with hierarchical priors leads to

M 𝑝 {𝜷𝑖}, {𝜙𝑖}, 𝝁𝛽, Σ𝛽 𝑁   h i Ö M; 𝜃1, . . . , 𝜃𝑁 N  𝜷𝑖; 𝝁𝛽, Σ𝛽 ∝Dirichlet-Multinomial × × (7) 𝑖=1 𝑁 h i Ö Gamma 𝜙𝑖; 𝛼𝜙, 𝛽𝜙 × 𝑝(𝝁𝛽, Σ𝛽) · · · 关注数学模型

𝑖=1 where p(μβ, Σβ) is a suitable hyperprior (e.g. Normal-Inverse-Wishart). One can sample from this posterior distribution via Markov chain Monte Carlo or other approximate methods, capturing both cross-country partial pooling (through {β}) and overdispersion (through {φ}). Predictive Uncertainty and Discrete Outcomes. For a future Olympics with Tnew total medals, each posterior sample ({β(s)}, {φ(s) }) implies 2. exp(xT β(s), (8)

and yields a random draw from

(9) N,new) Because the Dirichlet-Multinomial distribution produces a vector of nonnegative integers sum- ming to Tnew, it preserves discrete counts exactly. Across many posterior samples s = 1, . . . , S, this process captures parameter uncertainty (variation in {β, φ}) and the inherent multinomial- like randomness of allocating Tnew medals among N countries. In practice, one may form 95% credible intervals from these sampled outcomes to measure the plausible range of medals for ● each country. Breaking the Ice Probability. Suppose a country i historically has zero medals. To evaluate its likelihood of winning at least one medal in the upcoming Olympics, note that each simulated (s) outcome M i,new approximate the probability of “ice-breaking" as

S 1 Pr(Mi,new > 0) = (10) s=1 This metric naturally integrates both variability in country-specific parameters and the stochastic nature of discrete medal assignments.

4N,new), we can (s) compute summary statistics such as posterior means, medians, and credible intervals at any desired confidence level (commonly 95%). A 95% credible interval [li, u] for the medal count of country i is obtained by taking the 2.5th and 97.5th percentiles of { Ms }s one can compute probabilities of surpassing a historical record or of achieving a threshold medal count. These credible intervals differ from classical “frequentist prediction intervals" but serve a similar interpretive purpose within the Bayesian framework, reflecting the distribution of plausible future outcomes under the inferred BHDM. Interpreting Regression Coefficients. Because Bayesian estimation provides posterior draws for each βi,j, one can directly compute several summary measures from these samples. First, the posterior mean β,j offers a central estimate of the effect size for covariate j on country i’s log-rate of medal acquisition. Next, the posterior standard deviation StdDev(βi,j) characterizes uncertainty around this mean. One may also calculate the posterior probability that βi,j exceeds zero, denoted Pr(βi,j > 0), which reveals how likely it is that increasing covariate j has a positive effect on the country's medal prospects. Finally, a 95% credible interval [Li,j, Ui,j] is often derived by taking the 2.5th and 97.5th percentiles of the posterior draws of βi,j. This interval indicates the range of coefficient values most consistent with the observed data, under the hierarchical model. A positive βi,j (as signaled by its posterior mean and credible interval lying mainly above zero) suggests that raising covariate j increases the country's rate of medal accumulation, whereas a negative value implies the opposite. Because of the partial pooling in the hierarchical structure, extreme estimates for small or emerging countries are naturally shrunk toward a global mean, reducing the risk of overfitting and providing robust inferences about which predictors most influence medal outcomes.

5.3 Projects of LA 2028

By the Equal Distribution Assumption, we use the 2024 data as a proxy for 2028, modifying only the host country. The features are then incorporated into our model and compared against other approaches, with results presented in Table 2. As shown in Table 2, our proposed BHDM model outperforms both the machine/deep learning and traditional statistical approaches in predicting medal counts. For instance, in the All Medals category, BHDM achieves an MSE of 6.98 and an 𝑅2 of 0.85, which are notably superior to the corresponding values from the competing models that exhibit higher errors and lower fit indices. Similarly, in the Gold Medals category, BHDM records an MSE of 3.42 and an 𝑅2 of 0.80, outperforming alternative models by a substantial margin. These improvements are primarily attributable to the BHDM model’s adaptive capability in capturing the underlying data distribution, thereby effectively modeling the intrinsic variability and complex relationships in the dataset, which in turn results in more accurate predictions.

RMSE, and MAE indicate better performance, while higher values for 𝑅2 and Adjusted 𝑅2 indicate a better model fit. The best performance for each metric is highlighted in bold.

Machine/Deep Learning Models Statistical Models

Medal Type Metric XGBoost[1] RNN[3] RF Two-stage[5] Poisson Neg. Binomial BHDM (ours)

6.98 MSE 7.21 7.05 7.37 10.45 10.33 RMSE 2.72 2.65 2.78 3.21 3.15 2.59 All Medals MAE 1.15 1.12 1.17 1.58 1.52 1.03 𝑅2 0.85 0.84 0.83 0.77 0.71 0.74 Adjusted 𝑅2 0.84 0.82 0.78 0.74 0.68 0.69

MSE 3.71 3.63 3.82 5.25 5.12 3.42 RMSE 1.93 1.91 1.95 2.29 2.26 1.86 Gold Medals 0.95 MAE 1.03 0.99 1.04 1.23 1.25 𝑅2 0.80 0.76 0.79 0.71 0.66 0.71 Adjusted 𝑅2 0.78 0.74 0.75 0.68 0.62 0.69

Based on our Bayesian hierarchical model, our projections for the Los Angeles 2028 Olympic medal table is shown in Figure 4. It suggests that the United States will significantly improve its performance with a predicted total of 146 medals (95% CI: [136, 156]) and 53 gold medals (95% CI: [50, 56]), reflecting increases of +20 total and +13 gold medals relative to 2024; in contrast, China is forecast to decline to 82 total medals (95% CI: [75, 90]) and 31 gold medals (95% CI: [28, 34]), while Great Britain is expected to drop by 5 total medals (down to 60) and lose 2 gold medals (resulting in 12 gold medals). Moreover, after adjusting for the home advantage effect in 2024, France is projected to regress by 10 total medals (to 54) and 4 gold medals (to 12). Meanwhile, both Australia and Japan exhibit modest improvements, and the Netherlands shows a strong upward trend with an increase of 11 total medals and 5 gold medals. Overall, our model indicates that the United States and the Netherlands are most likely to improve, whereas China, Great Britain, France, Italy, and South Korea are expected to perform worse than in 2024. The 95% credible intervals, derived from the posterior predictive draws, quantify the uncertainty in our predictions and provide a robust framework for interpreting the range of plausible future outcomes.

关注数学模型 represent other medals; the solid black line shows the total medal prediction, the dashed dark orange line shows the gold medal prediction, and the shaded areas indicate the 95% credible intervals.

微信公众号：数学模型 微信号：MATHmodels

Category Country Probability 95% CI Malaysia 0.6861 [0.4568, 0.8132] Gold Refugee Olympic Team 0.3788 [0.3214, 0.4128] Haiti 0.2569 [0.2112, 0.0.2698] South Sudan 0.3904 [0.3315, 0.4208] Total Guinea 0.3227 [0.2774, 0.3518] Myanmar 0.1554 [0.1102, 0.1898]

5.4 The country that will achieve a Breakthrough From Zero

each country to achieve a breakthrough from a zero-medal history in the 2028 Olympics. Same as above, the results are stratified into two medal groups: Gold and Total. Gold Medals

• Malaysia: The estimated probability for Malaysia to secure its first gold medal is 0.6861, with a relatively wide 95% credible interval of [0.4568, 0.8132]. This interval indicates that while the central estimate is notably high, there is considerable uncertainty in the exact probability. Nonetheless, even the lower bound of approximately 0.46 suggests a strong underlying signal for Malaysia’s breakthrough potential in the gold medal group.

• Refugee Olympic Team: With an estimated breakthrough probability of 0.3788 and a narrower credible interval of [0.3214, 0.4128], the Refugee Olympic Team exhibits a moderate level of potential. The narrow interval reflects greater precision in this estimate, implying that the model is more confident about this moderate probability relative to that of Malaysia.

• Haiti: Haiti’s estimated probability stands at 0.2569 with a 95% credible interval of [0.2112, 0.2698]. The relatively low point estimate, coupled with a narrow interval, reinforces the conclusion that Haiti is less likely to achieve a breakthrough in the gold medal group. The tight range indicates high confidence in this low probability estimate.

The stark contrast in point estimates—particularly the high probability for Malaysia com- pared to the lower probabilities for the Refugee Olympic Team and Haiti—highlights a notable disparity in the competitive dynamics for gold medals. Total Medals

• South Sudan: In the Total Medal group, South Sudan exhibits the highest breakthrough probability at 0.3904, with a credible interval of [0.3315, 0.4208]. Although this estimate is lower than Malaysia’s gold medal probability, it indicates that South Sudan has a competitive edge when considering all medal types combined.

• Guinea: Guinea’s estimated probability is 0.3227 with a 95% credible interval of [0.2774, 0.3518]. The interval for Guinea overlaps somewhat with that of South Sudan, suggesting that while South Sudan has a slight advantage, the difference between these two countries might not be statistically significant under a Bayesian framework.

• Myanmar: Myanmar has the lowest estimated probability in the Total group at 0.1554, with a credible interval of [0.1102, 0.1898]. This clearly distinguishes Myanmar from the other candidates in terms of breakthrough potential for accumulating any medals.

The Total Medal group exhibits a more evenly distributed set of probabilities compared to the Gold Medal group. While the overall probabilities are lower, the differences among the countries (particularly between South Sudan and Guinea) appear less pronounced. This may reflect the broader range of events and competitive factors that come into play when considering the entire medal tally, as opposed to the singular focus required for a gold medal achievement.

5.5 Important Sports and Home Event Impact

Events and Medal Acquisition Analysis: The regression coefficients in Table 4 reveal that event-specific attributes are critical determinants of Olympic medal success, with notable dif- ferences across countries. For example, in the United States, the coefficient for Ball Sports Events (X7) is 0.03123 with a high posterior probability of 0.98, indicating that team sports such as basketball and football substantially drive medal acquisition. Similarly, Athletics Events (X5) show a positive effect (beta = 0.02345, Pr(𝛽> 0) = 0.97), suggesting that traditional track and field competitions are also important. In contrast, China displays a relatively modest effect for Athletics Events (X5, beta = 0.01567, Pr(𝛽> 0) = 0.92) but a more pronounced impact for Emerging Events (X8, beta = 0.01765, Pr(𝛽> 0) = 0.93), which implies that their strategic diversification into new sports disciplines plays a significant role in enhancing their medal prospects. Moreover, both the United Kingdom (beta for X5 = 0.02678, Pr(𝛽> 0) = 0.98) and France (beta for X5 = 0.02631, Pr(𝛽> 0) = 0.97) exhibit strong positive associations with Athletics Events, reinforcing the view that specific sports domains are aligned with each country’s historical strengths and strategic investments. Impact of Home Country Event Selection: The regression results in Table 4 also underscore the importance of tailoring event selection to leverage home advantage. When a country hosts the Olympics, it can capitalize on localized benefits such as familiar venues, superior logistical support, and heightened fan enthusiasm. For instance, the United States demonstrates strong positive effects in Athletics Events (X5, beta = 0.02345, 95% CI: [−0.00007, 0.04697]) and even more so in Ball Sports Events (X7, beta = 0.03123, 95% CI: [0.00771, 0.05475]), suggesting that emphasizing these sports can maximize the inherent benefits of home advantage. Similarly, in the United Kingdom and France, Athletics Events yield robust positive coefficients (UK: beta 关注数学模型 Variable United States China

Pr(𝛽> 0) Pr(𝛽> 0) Beta Std. Err. 95% CI Beta Std. Err. 95% CI

X1 0.03412 0.01234 0.99 [0.01996, 0.04828] 0.03245 0.01156 0.99 [0.01980, 0.05510] X2 0.01745 0.00852 0.99 [0.00079, 0.03411] 0.01621 0.00825 0.98 [0.00014, 0.03228] X3 0.06567 0.01245 0.99 [0.04873, 0.07007] 0.06456 0.01231 0.99 [0.04045, 0.07867] 微信公众号：数学模型 [−0.00236, 0.02704] X4 0.01234 0.00759 0.93 0.02891 0.01055 0.98 [0.00833, 0.04949] [−0.00007, 0.04697] [−0.00589, 0.03723] X5 0.02345 0.01244 0.97 0.01567 0.01143 0.92 −0.00234 [−0.02194, 0.01726] [−0.00628, 0.03096] X6 0.01038 0.32 0.01239 0.00951 0.95 [−0.01058, 0.03254] X7 0.03123 0.00713 0.98 [0.00771, 0.05475] 0.01098 0.01162 0.85 [−0.01065, 0.03639] X8 0.01287 0.01214 0.88 0.01765 0.00854 0.93 [0.00099, 0.03431]

Variable United Kingdom France

Pr(𝛽> 0) Pr(𝛽> 0) Beta Std. Err. 95% CI Beta Std. Err. 95% CI

X1 0.03789 0.01345 0.99 [0.01153, 0.05425] 0.03983 0.01273 0.99 [0.01347, 0.05419] X2 0.01567 0.00759 0.96 [0.00097, 0.03037] 0.01532 0.00795 0.94 [0.00082, 0.03012] 微信号：MATHmodels X3 0.05345 0.01120 0.99 [0.03811, 0.07501] 0.05576 0.01134 0.99 [0.03764, 0.06816] [−0.00986, 0.02738] [−0.01022, 0.02846] X4 0.00876 0.00958 0.88 0.00912 0.00933 0.86 X5 0.02678 0.01250 0.98 [0.00228, 0.05128] 0.02631 0.01232 0.97 [0.00312, 0.05076] −0.00123 [−0.02181, 0.01935] −0.00096 [−0.02147, 0.01955] X6 0.01053 0.44 0.01025 0.48 [−0.00883, 0.04017] [−0.00984, 0.04158] X7 0.01567 0.01257 0.90 0.01687 0.01243 0.91 [−0.00105, 0.04795] [−0.00123, 0.04603] X8 0.02345 0.01257 0.97 0.02257 0.01233 0.95

= 0.02678, 95% CI: [0.00228, 0.05128]; France: beta = 0.02631, 95% CI: [0.00312, 0.05076]), indicating that host nations with strong track records in these disciplines can further enhance their medal prospects by strategically prioritizing events that align with their historical strengths and local support systems. Moreover, China’s relatively higher coefficient for Emerging Events (X8, beta = 0.01765, 95% CI: [0.00099, 0.03431]) implies that even non-traditional or newer events can be exploited effectively when a host country’s infrastructure and preparatory advantages are aligned with the chosen sports. Overall, these findings suggest that by selecting events that not only reflect historical success but also amplify home advantages, host nations can significantly improve their medal tallies. 1

6 Task 2: Dive Into Great Coach Effect

In this section, we examine another factor that can influence medal counts—the coach. Unlike athletes, who are typically constrained by nationality, coaches possess a unique flexibility to work across borders. This mobility allows them to transfer their expertise and successful training methodologies from one country’s sports system to another. Such fluidity creates what we term the “great coach effect,” where the influence of a single coach can significantly enhance a country’s medal count in specific sports [2].

For example, the legendary careers of Lang Ping and Béla Károlyi exemplify this effect. Despite coaching in vastly different cultural and sporting environments, both successfully trans- formed national teams and led them to Olympic podium finishes. Lang Ping’s experience coaching volleyball teams in both the United States and China demonstrates the potential for

1Due to space constraints, gold medal data is omitted here. The conclusions for gold medals are consistent with those for total medals.

exceptional coaches to transcend national boundaries [4]. Similarly, Béla Károlyi’s transition from coaching in Romania to achieving remarkable success with the U.S. women’s gymnastics team further supports this notion [8].

Following standard analytical procedures, we first define what constitutes a "great coach" and seek to quantify their coaching impact. Next, we incorporate this variable into our BHDM model and analyze regression coefficients to assess whether and to what extent great coaches significantly influence medal counts. Finally, we will identify three countries, select great coaches for them, and estimate their impact based on the regression coefficients.

6.1 What is a Great Coach?

In our analysis, we define a "great coach" as one who has demonstrated the ability to elevate an Olympic team to achieve at least bronze medal finishes in two or more different countries. By searching the Wiki database, we identified a total of 1,103 such great coaches, among whom 697 are currently active. These coaches are engaged in multiple sports across various countries, including the United States, China, and Japan.

If we use the total number of renowned coaches as a new variable, a natural hypothesis emerges: do all renowned coaches contribute equally to a country’s medal count? We believe this assumption is overly restrictive. Our selection criteria represent only the minimum threshold for inclusion, but there is likely heterogeneity among coaches, meaning that their ability to lead teams to success varies.

For example, while Lang Ping, as a renowned coach, helped China secure one gold medal and the United States one silver medal, Béla Károlyi, another renowned coach, led his teams to at least 9 gold medals. This discrepancy highlights the differences in coaching effectiveness. Therefore, to ensure a fair reflection of each coach’s impact, a more fine-grained characterization of individual coaching abilities is necessary.

Based on the latest research on coaching effectiveness, we define the following metric to quantify the coaching ability of a "renowned coach": the coaching ability 𝐴is calculated as the number of gold medals won during their tenure multiplied by 6, plus the number of silver medals multiplied by 3, and the number of bronze medals multiplied by 1. Mathematically, this is expressed as:

𝐴= 6𝐺+ 3𝑆+ 1𝐵 (11) where 𝐺represents the number of gold medals won under the coach’s leadership, 𝑆represents the number of silver medals won, and 𝐵represents the number of bronze medals won. This metric assigns the highest weight to gold medals, followed by silver and then bronze, ensuring a more precise assessment of a coach’s contribution to medal achievements.

For a country’s coaching ability variable 𝑋9, it is defined as the sum of the coaching abilities 𝐴of all renowned coaches within that country, mathematically expressed as:

𝑁 ∑︁ 𝑋9 = 𝐴𝑖 (12) 𝑖=1 where 𝐴𝑖denotes the coaching ability of the 𝑖-th coach.

6.2 Great Coach Affect the Medals

We incorporate 𝑋9 into our BHDM model and obtain its regression coefficient. Since there are 46 countries with renowned coaches, we are unable to present the specific values for each due to space constraints. Table 5 displays some summary statistics of this indicator. 关注数学模型 Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Outcome Beta Mean Std. Err. Mean 微信公众号：数学模型 All Medals 0.036134 0.011008 0.997 46 Gold Medals 0.028167 0.009134 0.983 45

As shown in Table 5, the posterior mean coefficients for the Great Coach variable 𝑿9 are approximately 0.036134 for all medals and 0.028167 for gold medals, respectively. Because these coefficients reflect log-rate effects, a one-unit increase in 𝑿9 corresponds to a multiplicative change of 𝑒0.036134 ≈1.037 (roughly a 3.7% rise) in the expected total medal count and 𝑒0.028167 ≈1.029 (about a 2.9% increase) in gold medals. Consequently, even modest gains 微信号：MATHmodels in “great coach” capacity—such as recruiting or developing a coach with one additional point of aggregate coaching ability—can yield a tangible percentage uplift in a nation’s overall and top-tier (i.e., gold) Olympic performance.

Moreover, the high values of Avg. Pr(𝛽> 0) (0.997 for all medals and 0.983 for gold medals) and the fact that Pr(𝛽> 0) exceeds 0.95 for nearly every country underscore that the impact of the Great Coach variable is both statistically robust and broadly consistent across the sample of 46 nations. In other words, not only does the posterior mean of 𝛽𝑋9 suggest a positive relationship, but the overwhelming majority of countries in the dataset exhibit a high probability that increasing aggregate coaching ability leads to more medals. This finding provides strong evidence for the “great coach” effect, indicating that improvements in coaching capacity are systematically tied to enhanced Olympic performance rather than being confined to a select subset of countries.

6.3 Invest in Great Coach and Estimate its Impact

We believe that only wealthy countries have more options when it comes to investing in renowned coaches. Therefore, we selected the United States, China, and Japan—three of the world’s top-ranking countries by GDP—and carefully curated projects for each of them. The regression results are shown in Table 6.

Pr(𝛽> 0) Country Beta Std. Err. 95% Cred. Int.

United States 0.0367 0.0091 0.98 [0.0082, 0.0450] China 0.0445 0.0102 0.99 [0.0150, 0.0558] Japan 0.0283 0.0078 0.96 [0.0031, 0.0382]

We recommend that the United States recruit at least one “great coach” for fencing and sport climbing. With a coefficient of 0.0367, a one-unit increase in coaching capacity corresponds to an estimated impact of 𝑒0.0367 −1 ≈3.74% increase in Olympic medal counts in these disciplines.

For China, the coefficient of 0.0445 implies that each additional point of 𝑿9 results in roughly 𝑒0.0445 −1 ≈4.55% enhancement in overall medal achievements, making it advisable to invest in top coaching talent for sports such as basketball and beach volleyball. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Finally, Japan exhibits a coefficient of 0.0283, translating to an expected improvement of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 𝑒0.0283 −1 ≈2.87%; thus, Japan should consider investing in a “great coach” for gymnastics m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and short-track speed skating to boost its medal tally. These quantitative estimates demonstrate that targeted investments in coaching excellence can yield substantial and measurable gains in Olympic performance.

7 Sensitivity Analysis

7.1 Sensitivity Analysis for τ2 Values

In Section 5.2, we adopted a weakly informative prior by setting the covariance matrix for the regression coefficients as 22 "dIz⊥=83 = 1, as our initial choice. In this section, we examine how varying τ2 over a range from 0.1 to 10 affects the predicted medal counts for the 2028 Olympics. This analysis aims to determine whether changes in τ² lead to substantial differences in the 2028 medal predictions. The results, as illustrated in Figure 5, provide insights into the robustness of our predictions with respect to the prior informativeness imposed by the choice of τ2.

medals and gold medals in 2028 under different τ2 values and provided the 95% prediction intervals.

Predicted 2028 Medal Counts under Different τ² Values 160 - Total, τ2 = 1 (Baseline) Total, τ² = 2 Gold, τ² = 2 Gold, τ² = 1 (Baseline) 140- Total, τ² = 5 Total, τ² = 0.1 Gold, τ² = 0.1 Gold, τ² = 5 Total, τ2 = 10 Total, τ² = 0.5 120 Gold, τ² = 10 Gold, τ² = 0.5

100 - Number of Medals 80

60

40

20

United States Australia South Korea New Zealand China Great Britain Japan Netherlands Italy Canada Uzbekistan Hungary Spain France Germany Country

It is evident that the predicted medal counts for the 2028 Olympics remain remarkably consistent across the range of τ2 values considered, from 0.1 to 10. Despite the deliberate variation in the weakly informative prior's variance parameter, both the total and gold medal predictions show only minor deviations from the baseline forecast obtained with τ2 = 1. This close alignment indicates that the posterior inferences are not overly sensitive to the choice of τ2, thereby reinforcing the stability of our Bayesian framework even under different prior settings.

scenarios Moreover, the corresponding 95% confidence intervals across the various largely overlap with those of the baseline, highlighting that the uncertainty associated with the 关注数学模型 predictions remains virtually unchanged. The observed fluctuations, confined within anarrow margin of ±5%, are negligible in the context of the overall predictive performance. This consistency not only demonstrates that the weakly informative prior does not exert an undue influence on the results, but also confirms that the data are sufficiently informative to drive the posterior estimates independently of the prior variance specification.

Overall, the sensitivity analysis clearly illustrates the robustness of our model. Regardless of the variations in τ2, all predicted outcomes are closely aligned with the baseline results, substantiating that the model's performance is stable under different prior informativeness levels. Such robustness is crucial for ensuring that the model's predictions can be trusted for further inferential or policy-related decisions, as the underlying inference remains reliable despite moderate changes in prior assumptions.

7.2 Sensitivity Analysis of Equal Distribution Assumptions

In our initial modeling framework, we assumed that the distribution of events and the total number of medals in 2028 would exactly match those of 2024. Recognizing that such an assumption is unlikely to hold in practice, we perform a sensitivity analysis by allowing both the event-specific medal counts and the total medal count to vary by ±5%. Specifically, we adjust these counts using five discrete steps: a decrease of 5%, a decrease of 3%, an unchanged baseline (0%), an increase of 3%, and an increase of 5%. For each scenario, all medal counts are modified accordingly and then rounded upward to ensure integer-valued predictions.

This approach permits us to systematically evaluate how small, yet realistic, changes in the underlying medal distributionassumptions impact our model's forecasts for the 2028 Olympics. By applying these percentage-based adjustments uniformly across all events and the overall medal total, we capture potential fluctuations that may arise from changes in the event program, variations in competitive intensity, or adjustments in the total number of medals awarded. The modified data sets are then fed into our BHDM model to generate alternative predictions.

The results of this sensitivity analysis are crucial for assessing the robustness of our model. If the predicted medal counts remain largely consistent across these scenarios—showing only minimal differences from the baseline—it would provide strong evidence that our model is not overly sensitive to moderate shifts in the medal distribution assumptions. Such robustness is essential for ensuring that our predictions are reliable even when the real-world conditions at the 2028 Olympics deviate slightly from the 2024 baseline.

The results illustrated in Figure 6 demonstrate that, even when the underlying medal distri- bution assumptions are varied by ±5%—with adjustments applied individually to each country's predicted counts—the forecasts for both total and gold medals remain highly consistent with the baseline predictions. Minor fluctuations are observed; however, these differences are confined within a narrow range, indicating that the model's predictions are not significantly perturbed by realistic changes in the event program or overall medal totals.

Such robustness confirms that our BHDM model reliably captures the core dynamics under- lying medal allocations, even under moderate deviations from the 2024 baseline. This stability in predictions provides strong evidence that our modeling framework can be trusted for forecasting future outcomes, as it effectively mitigates the potential impact of uncertainties in the underlying medal distribution assumptions.

Strengths and Limitation of the Proposed Model

8

Strengths.

• High Predictive Accuracy: The BHDM model consistently outperforms alternative machine learning (XGBoost, RNN, and RF Two-stage) and statistical methods (Poisson, Negative Binomial) in forecasting both total and gold medal counts. For example, it the number of medals and gold medals in 2028 under different medal distributions and provided the 95% prediction intervals.

achieves an MSE of 6.98 and an 𝑅2 of 0.85 for predicting the total number of medals, and an MSE of 3.42 with an 𝑅2 of 0.80 for gold medals (see Table 2). These improvements underscore its capacity to capture the underlying data structure more effectively than competing approaches.

• Discrete and Constrained Outcomes: By modeling medal allocations via a Dirichlet– Multinomial likelihood, the BHDM ensures integer-valued outcomes that sum to a known total 𝑇. This feature is crucial in predicting realistic medal counts, especially when evaluating discrete events like whether a country will “break the ice” and win its first medal. The model’s ability to provide exact integer predictions (e.g., forecasting 146 total medals for the United States and 82 for China) is a key advantage over approaches that produce continuous-valued outputs.

• Robustness to Prior and Distributional Changes: Sensitivity analyses demonstrate that the BHDM model’s predictive performance remains stable across different settings of 𝜏2 (ranging from 0.1 to 10) and under ±5% variations to the total medal pool. As shown in Figures 5 and 6, the predicted 2028 medal counts and their credible intervals remain largely unaffected by these adjustments, indicating that the inference is driven more by the data than by the particular choice of prior or medal distribution assumptions.

Limitation.

• Complexity and Data Requirements: The hierarchical structure, while powerful for par- tial pooling and capturing cross-country heterogeneity, entails increased computational demands compared to simpler count models. Fitting the BHDM can become computa- tionally expensive for very large datasets or when a fine-grained, event-level breakdown is required for many countries. Furthermore, to reliably estimate country-specific random effects and hyperparameters (e.g., the 𝜙𝑖concentration parameters), the model benefits 关注数学模型 from detailed, high-quality data—something that may be difficult to obtain for smaller or underrepresented countries with limited historical records.

9 Task 3: Other Original Insights of Our BHDM Model

9.1 Economic level determines medals

In our final analysis of all 206 countries in the dataset, two predictors stand out as having 微信公众号：数学模型 the largest impact on a nation’s Olympic medal count: historical performance (𝑋1) and athlete delegation size (𝑋2). Both variables are closely tied to a country’s economic level, as wealthier nations tend to have better-funded sports programs and a stronger history of Olympic participa- tion. Specifically, as reported in Table 7, the mean regression coefficient for past medal counts (𝛽𝑋1) is 0.035143, while that for total athlete numbers (𝛽𝑋2) is 0.011442. These results reinforce the notion that economic strength plays a decisive role in determining a country’s Olympic success. To interpret the magnitude of these effects:

𝑒0.035143 −1 ≈3.58%, 𝑒0.011442 −1 ≈1.15%. and 微信号：MATHmodels Hence, a unit increase in 𝛽𝑋1 corresponds to roughly a 3.6% increase in the expected medal count, while a similar increase in 𝛽𝑋2 implies about a 1.2% rise. These results underscore that both a strong legacy of medal achievements and a robust delegation size can significantly boost a country’s chances of reaching the podium.

Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Outcome Beta Mean Std. Err. Mean

𝛽𝑋1 0.035143 0.008224 0.981 204 𝛽𝑋2 0.011442 0.006538 0.945 178

By maintaining consistent investments in sports where they have historically excelled, countries can leverage existing expertise and well-established training systems. Meanwhile, increasing the breadth of participation through a larger delegation expands the probability of discovering or nurturing world-class athletes in more disciplines, ultimately translating into higher medal tallies.

9.2 Home Turf and Aligned Systems Prevail

Focusing on the subset of 33 countries that have hosted the Olympics at least once, our model reveals two important explanatory variables for elevating medal counts. Table 8 provides the posterior summary for:

1. Home Advantage (𝑋3): 𝛽𝑋3 has a mean of about 0.061245, which corresponds to:

𝑒0.061245 −1 ≈6.32% improvement.

This aligns well with the intuitive idea that home-country athletes benefit from logistical, infrastructural, and psychological advantages when competing on familiar ground.

2. Social System Congruence (𝑋4): 𝛽𝑋4 has a mean of around 0.025982. In percentage terms:

𝑒0.025982 −1 ≈2.63% improvement.

Countries whose societal and institutional structures closely resemble those of the host may adapt more seamlessly to local conditions, cultural norms, and organizational protocols.

are 33 host countries in total.

Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Outcome Beta Mean Std. Err. Mean

𝑋3: Home Advantage 0.061245 0.010277 0.980 33 𝑋4: Soc. System Congr. 0.025982 0.007612 0.955 30

In practical terms, this means a host nation can anticipate, on average, more than a 6% increase in its medal tally relative to non-host years. Moreover, a country resembling the host’s societal ecosystem—whether by language, cultural practices, or institutional frameworks—might also see an additional bump, albeit of a smaller magnitude. Proactive planning, like scouting local venues, training under similar conditions, and ensuring linguistic or cultural familiarity, can amplify these benefits for visiting teams as well.

9.3 Emerging Sports Aid Low-GDP Countries

Finally, our model points to a strategic pathway for 38 countries identified as being in the bottom 50% of world GDP according to the World Bank 2 and having already won at least one Olympic medal. As highlighted in Table 9, investing in less-established or newly introduced disciplines—captured by the indicator variable 𝛽𝑋8 for Emerging Events—provides these lower-GDP nations with a pronounced edge.

Avg. Pr(𝛽> 0) Pr(𝛽> 0) > 0.95 Outcome Beta Mean Std. Err. Mean

𝛽𝑋8 0.032413 0.006568 0.979 37

A mean coefficient of 0.032413 for 𝛽𝑋8 translates to about a 𝑒0.032413 −1 ≈3.29%

increment in medal counts for every unit increase in emerging-sport emphasis. In practice, this suggests that under-resourced nations can “level the playing field” by channeling their limited resources into newer sporting disciplines, where established powerhouses have yet to monopolize coaching expertise, infrastructure, and athlete development. Taking advantage of these relatively uncrowded competitive landscapes may thus maximize the return on investment for nations working within tighter financial and organizational constraints.

9.4 A letter to inform NOC

Based on the insights mentioned above, we have written a letter to NOC. The content of this letter is as follows:

关注数学模型 2 http://data.worldbank.org Some insights about Olympics Medal Counts

To: Country Olympics Committees From: Team #2513314 Data: January 27, 2025 Dear Country Olympics Committees leaders:

We are writing to share three major insights that can guide Olympic committees in crafting more effective, practical strategies for securing medals. Our analysis reveals how a nation’s economic capacity, its hosting opportunities, and its targeted focus on emerging sports can all 微信公众号：数学模型 contribute to elevating athletic performance on the global stage. By highlighting each factor in simple terms, we hope to show that even modest interventions can make a big difference when implemented thoughtfully.

First, our study clearly links economic strength to higher medal counts, chiefly through two channels: historical performance and the number of participating athletes. In plain language, if a country has a track record of success in certain sports, it likely possesses time-tested coaching expertise and training facilities that can be reinforced. At the same time, expanding the size of the athlete delegation—whether by discovering new talent or offering more support to existing programs—broadens the pool of potential medalists. Committees can utilize this insight by directing funds to sports with proven results while systematically scouting fresh talent to sustain 微信号：MATHmodels a healthy pipeline for future competitions.

Second, there is a distinct “home turf” benefit for nations hosting the Olympics, as local teams have the advantage of competing in familiar environments with supportive crowds. Beyond that, countries that share cultural, linguistic, or societal characteristics with the host nation can also see smaller but meaningful boosts in performance. For instance, translating key materials into a common language and training athletes to adapt to local climates or customs can reduce logistical hiccups, ensuring a smoother preparation process. Committees might consider partnerships or cultural exchange programs with future hosts to gain on-the-ground knowledge and acclimate athletes well in advance.

Third, for nations with tighter budgets, focusing on newly introduced or less-established sports offers a unique chance to thrive. Because these disciplines are not yet dominated by well- funded powerhouses, smaller countries can step in with targeted investments—like specialized coaches, better equipment, or even grassroots talent-spotting efforts. By concentrating on these emerging events, committees can quickly close the gap and even outcompete wealthier nations still focused on mainstream sports. This tailored approach lets countries make the most of limited resources and diversify their medal potential.

In conclusion, each of these insights—prioritizing historically successful events and a wider athlete pool, leveraging home-field and cultural advantages, and capitalizing on emerging sports—gives Olympic committees a roadmap for thoughtful action. We trust this overview will help you shape meaningful strategies that tap into your nation’s inherent strengths and adapt to its financial realities, ultimately lifting your athletes to new heights of excellence.

Yours Sincerely,

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m
