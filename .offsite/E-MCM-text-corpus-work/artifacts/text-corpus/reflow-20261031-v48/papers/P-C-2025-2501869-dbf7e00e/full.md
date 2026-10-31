# P-C-2025-2501869-dbf7e00e

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen C 2025 MCM/ICM Summary Sheet Team Control Number 2501869

<!-- b000002 | title | pages [1] -->
Medal Prediction Based on Tobit and Hurdle Models and Great Coach Effect Insights

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
In Question 1, this paper proposes a Hurdle-Tobit fusion model framework to address the characteristics of the discrete nature of the number of Olympic medals, the zero inflation characteristics, and the heterogeneity between countries. The Hurdle model solves the zero value problem through two-stage modeling (logit classification and truncated count distribution), and the Tobit model handles right censored data. Both models introduce the Revealed Comparative Advantage Index RCA and incorporate heterogeneity factors such as the discrete size of athletes and the host effect. Then, by comparison, we found that the hurdle and Tobit models were significantly better than the machine learning methods (random forest and XGboost) in terms of mean square error and prediction coverage. Among them, the Hurdle model has a better predictive effect on the number of medals of sports powers, while Tobit has a better predictive effect on countries that have won a few medals. The prediction results show that the United States, China, and India will see the largest increases in medals, while France, Russia, and Germany will see significant decreases. The probability of Angola, Bangladesh, and Cambodia winning their first medal is 49.2%, 46.7%, and 42.5%, respectively. Finally, using model complementation and variable reconstruction, it is revealed how the host selection project affects the number of medals.

<!-- b000005 | prose | pages [1] -->
In Question 2, the Bayesian Change-point Detection method is used to identify significant changes in the number of medals won by countries in specific events (such as a sudden breakthrough after a long period of depression), and attribute them to the “great coaching effect”. In order to solve the problem of frequent changes in the simple weighted medal data, an innovative data preprocessing algorithm with memory enhancement is used to preprocess the original medal data, which can effectively distinguish the significance of the medal data and the dynamic self-reinforcing mechanism from the real changes driven by the coaching effect. Then, a two-stage least squares (2SLS) method is used to construct a causal regression model to quantify the contribution of outstanding coaches to the number of medals, overcoming the endogeneity bias of the traditional OLS method. Model validation shows that 2SLS significantly outperforms OLS in explaining the coaching effect. Based on this, it is proposed that the United States, the United Kingdom, and France should prioritize the introduction of multinational coaches in wrestling, rowing, table tennis, and other events, which is expected to increase the number of medals by 1-2.

<!-- b000006 | prose | pages [1] -->
In Question 3, we continue the analysis of Questions 1 and 2. Based on the Bayesian change-point detection method, we identify the potential “great coaching effect” time nodes in each sport in previous Olympic Games and incorporate them into the Hurdle and Tobit models as key explanatory variables for reanalysis. At the same time, in order to capture the dynamic self-reinforcing mechanism of medal counts, we further explain the lagged terms (such as the host country effect lagged by 4 years, the historical medal count lagged term, etc.) to analyze the heterogeneity of short-term and long-term effects. Ultimately, we obtain policy implications for promoting post-competition resource redistribution and for balancing the “depth” and “breadth” of National Olympic Committees.

<!-- b000007 | keywords | pages [1] -->
Keywords: Tobit, Hurdle, 2SLS, Bayesian Change-Point Detection, Medal Prediction

<!-- b000008 | furniture | pages [1] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000009 | furniture | pages [1] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000010 | heading | pages [2] -->
Contents

<!-- b000011 | source_object | pages [2] -->
1 Introduction 3 1.1 Background 3 1.2 Restatement of the Problem 3 1.3 Literature Overview 3 1.4 Our Work 4 2 Assumptions and Justification 4 3 Notations 4 4 Data Processing 5 4.1 Data Cleaning 5 4.2 Data Overview 5 5 Comparative Modeling of Olympic Medal Projections: Hurdle-Tobit Framework with Host Country Strategy Analysis 6 5.1 Hurdle and Tobit Models 6 5.2 Model Selection and Validation 9 5.2.1 Model Selection: Hurdle, Tobit, XGBoost and Ramdom Forest 9 5.2.2 Model Validation: 2024 Olympic Games Predictions Based on Hurdle and Tobit 11 5.3 2028 Los Angeles Olympics Medal Count Projections 12 5.4 Projecting First-Time Medal Winners and Probability Estimates 12 5.5 The Influence of Item Selection on the Number of Medals . 13 5.5.1 Relationship Between Olympic Events and Medal Distribution 14 5.5.2 Analysis of Key Sports and Their Importance for Different Countries . 14 5.5.3 Impact of Host Country Event Selection on Performance 15 The Great Coach Effect: A Strategy Optimization Study Based on Bayesian 6 Change-Point Detection and Causal Inference Models 18 6.1 Discovery of Great Coach Effect Based on Bayesian Change-Point Detection . 18 Data Handling . 18 6. Bayesian Change-point Detection 19 Evidence of Coaching Effect in the United States 19 6.2 Quantitative Evaluation of Great Coaching Effect on Medal Counts 20 6.2.1 Regression Model Using 2SLS 20 6.2.2 Model Validation. 20 6.3 Targeted Coaching Inyestments for Three Nations 21 7 Insights: Strategic Resource Allocation and Path Dependency in Olympic Medal Performance 22 7.1 Dynamic Attenuation of the Host Country Effect and Resource Redistribution 22 7.2 The “Double-Eged Sword Effect" of the Number of Events and Sports 22 8 Sensitivity Analysis 23 9 Model Evaluation 23 9.1 Strength 23 9.2 Weakness 24 Reference 24

<!-- b000012 | furniture | pages [2] -->
关注数学模型 获取更多资讯

<!-- b000013 | furniture | pages [3] -->
Team # 2501869

<!-- b000014 | furniture | pages [3] -->
Page 3 of 25

<!-- b000015 | heading | pages [3] -->
1 Introduction

<!-- b000016 | heading | pages [3] -->
1.1 Background

<!-- b000017 | prose | pages [3] -->
微信公众号：数学模型 The Olympic medal table reflects national sporting prowess and serves as a global competi- tive benchmark. At the 2024 Paris Olympics, the U.S. and China tied with 40 golds each, while host France ranked fifth in golds (16) but fourth overall. Notably, Albania and Cape Verde achieved their first-ever medals, yet over 60 countries remain without Olympic medals.

<!-- b000018 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000019 | prose | pages [3] -->
Task 1 Develop an Olympic medal prediction model using historical data to forecast: (1) 2028 Los Angeles medal counts per country with prediction intervals and accuracy metrics, identifying upward/downward mobility relative to 2024. (2) First-time medal-winning prob- ability for nations, contextualized through historical breakthrough patterns. (3) Sport-event 微信号：MATHmodels structure’s impact on medal distribution, including identification of national dominance events. (4) Quantification of host advantage through program adjustment impacts.

<!-- b000020 | prose | pages [3] -->
Task 2 (1) Statistically validate coach replacement effects on medal changes and quantify "great coach" contributions. (2) For three nations, identify underperforming sports with medal potential and assess feasibility/benefits of elite coach recruitment.

<!-- b000021 | prose | pages [3] -->
Task 3 (1) Identify non-traditional factors influencing medal allocations. (2) Generate evidence-based policy recommendations for Olympic committees.

<!-- b000022 | heading | pages [3] -->
1.3 Literature Overview

<!-- b000023 | prose | pages [3] -->
Empirical analysis of the Olympic Games has emerged as a critical area of research, en- compassing both forecasting (e.g., De Bosscher et al., 2006) and broader analytical perspectives (e.g., Streicher et al., 2020).

<!-- b000024 | prose | pages [3] -->
Since Ball (1972) introduced a correlation-based scoring model, forecasting methodologies have become increasingly sophisticated. Initially, many researchers relied on ordinary least squares (OLS) regressions due to their ease of interpretation (e.g., Baimbridge, 1998; Condon et al., 1999; Kuper and Sterken, 2001). However, a significant challenge in predicting Olympic medals is accurately reflecting the substantial number of nations that have yet to achieve any medals. The exponential function employed in these models tends to impose penalties on low predicted medal counts. Consequently, some scholars have transitioned to Poisson-based models (e.g., Lui and Suen, 2008; Leeds and Leeds, 2012; Blais-Morisset et al., 2017).

<!-- b000025 | prose | pages [3] -->
Afterwards, machine learning techniques (e.g. Random forest and XGboost) have gained traction in sports-related contexts. The random forest approach has demonstrated exceptional performance in tasks such as predicting the outcome of football matches (Groll et al., 2019) or horse racing outcomes (Lessmann et al., 2010). However, random forests and XGBoost, as ensemble learning methods based on decision trees, excel at handling non-linear relationships and feature interactions, but they lack the ability to explicitly model truncation and zero-inflated data. This means that these algorithms may not accurately capture the truncation points or zero-value generation mechanisms in the data, leading to prediction bias (Breiman, 2001; Chen & Guestrin, 2016).

<!-- b000026 | prose | pages [3] -->
Given that the dependent variable, typically the number of medals, has been set to zero, most authors have employed Tobit regression to predict Olympic success (e.g., Tcha and Pershin,

<!-- b000027 | prose | pages [3, 4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2003; Forrest et al., 2015; Rewilak, 2021). However, recently, a two-step approach, estimating the probability of winning any medal before determining the exact number of medals in case of success, has become more prevalent. In particular, both Scelles et al. (2020) and Rewilak (2021), employing a Mundlak transformation of the Tobit model, could, again, increase the prediction accuracy with their respective Hurdle models.

<!-- b000028 | furniture | pages [3] -->
m

<!-- b000029 | furniture | pages [3] -->
m

<!-- b000030 | furniture | pages [3] -->
m

<!-- b000031 | furniture | pages [3] -->
m

<!-- b000032 | furniture | pages [3] -->
m

<!-- b000033 | furniture | pages [3] -->
m

<!-- b000034 | furniture | pages [3] -->
m

<!-- b000035 | furniture | pages [3] -->
m

<!-- b000036 | furniture | pages [3] -->
m

<!-- b000037 | furniture | pages [3] -->
m

<!-- b000038 | furniture | pages [3] -->
m

<!-- b000039 | furniture | pages [3] -->
m

<!-- b000040 | furniture | pages [3] -->
m

<!-- b000041 | furniture | pages [3] -->
m

<!-- b000042 | furniture | pages [3] -->
m

<!-- b000043 | furniture | pages [3] -->
m

<!-- b000044 | furniture | pages [3] -->
m

<!-- b000045 | furniture | pages [3] -->
m

<!-- b000046 | furniture | pages [3] -->
m

<!-- b000047 | furniture | pages [3] -->
m

<!-- b000048 | furniture | pages [3] -->
m

<!-- b000049 | furniture | pages [3] -->
m

<!-- b000050 | furniture | pages [3] -->
m

<!-- b000051 | furniture | pages [3] -->
m

<!-- b000052 | furniture | pages [3] -->
m

<!-- b000053 | furniture | pages [3] -->
m

<!-- b000054 | furniture | pages [3] -->
m

<!-- b000055 | furniture | pages [3] -->
m

<!-- b000056 | furniture | pages [3] -->
m

<!-- b000057 | furniture | pages [3] -->
m

<!-- b000058 | furniture | pages [3] -->
m

<!-- b000059 | furniture | pages [3] -->
m

<!-- b000060 | furniture | pages [3] -->
m

<!-- b000061 | furniture | pages [3] -->
m

<!-- b000062 | furniture | pages [3] -->
m

<!-- b000063 | furniture | pages [3] -->
m

<!-- b000064 | furniture | pages [3] -->
m

<!-- b000065 | furniture | pages [3] -->
m

<!-- b000066 | furniture | pages [3] -->
m

<!-- b000067 | furniture | pages [3] -->
m

<!-- b000068 | furniture | pages [3] -->
m

<!-- b000069 | furniture | pages [3] -->
m

<!-- b000070 | furniture | pages [3] -->
m

<!-- b000071 | furniture | pages [3] -->
m

<!-- b000072 | furniture | pages [3] -->
m

<!-- b000073 | furniture | pages [3] -->
m

<!-- b000074 | furniture | pages [3] -->
m

<!-- b000075 | furniture | pages [3] -->
m

<!-- b000076 | furniture | pages [3] -->
m

<!-- b000077 | furniture | pages [3] -->
m

<!-- b000078 | furniture | pages [3] -->
m

<!-- b000079 | furniture | pages [3] -->
m

<!-- b000080 | furniture | pages [3] -->
m

<!-- b000081 | furniture | pages [3] -->
m

<!-- b000082 | furniture | pages [3] -->
m

<!-- b000083 | furniture | pages [3] -->
m

<!-- b000084 | furniture | pages [3] -->
m

<!-- b000085 | furniture | pages [3] -->
m

<!-- b000086 | furniture | pages [3] -->
m

<!-- b000087 | furniture | pages [3] -->
m

<!-- b000088 | furniture | pages [3] -->
m

<!-- b000089 | furniture | pages [3] -->
m

<!-- b000090 | furniture | pages [3] -->
m

<!-- b000091 | furniture | pages [3] -->
m

<!-- b000092 | furniture | pages [3] -->
m

<!-- b000093 | furniture | pages [3] -->
m

<!-- b000094 | furniture | pages [3] -->
m

<!-- b000095 | furniture | pages [3] -->
m

<!-- b000096 | furniture | pages [3] -->
m

<!-- b000097 | furniture | pages [3] -->
m

<!-- b000098 | furniture | pages [3] -->
m

<!-- b000099 | furniture | pages [3] -->
m

<!-- b000100 | furniture | pages [3] -->
m

<!-- b000101 | furniture | pages [3] -->
m

<!-- b000102 | furniture | pages [3] -->
m

<!-- b000103 | furniture | pages [3] -->
m

<!-- b000104 | furniture | pages [3] -->
m

<!-- b000105 | furniture | pages [3] -->
m

<!-- b000106 | furniture | pages [3] -->
m

<!-- b000107 | furniture | pages [3] -->
m

<!-- b000108 | furniture | pages [3] -->
m

<!-- b000109 | furniture | pages [3] -->
m

<!-- b000110 | furniture | pages [3] -->
m

<!-- b000111 | furniture | pages [3] -->
m

<!-- b000112 | furniture | pages [3] -->
m

<!-- b000113 | furniture | pages [3] -->
m

<!-- b000114 | furniture | pages [3] -->
m

<!-- b000115 | furniture | pages [3] -->
m

<!-- b000116 | furniture | pages [3] -->
m

<!-- b000117 | furniture | pages [3] -->
m

<!-- b000118 | furniture | pages [3] -->
m

<!-- b000119 | furniture | pages [3] -->
m

<!-- b000120 | furniture | pages [3] -->
m

<!-- b000121 | furniture | pages [3] -->
m

<!-- b000122 | furniture | pages [3] -->
m

<!-- b000123 | furniture | pages [3] -->
m

<!-- b000124 | furniture | pages [3] -->
m

<!-- b000125 | furniture | pages [3] -->
m

<!-- b000126 | furniture | pages [3] -->
m

<!-- b000127 | furniture | pages [3] -->
m

<!-- b000128 | furniture | pages [3] -->
m

<!-- b000129 | furniture | pages [3] -->
m

<!-- b000130 | furniture | pages [3] -->
m

<!-- b000131 | furniture | pages [3] -->
m

<!-- b000132 | furniture | pages [3] -->
m

<!-- b000133 | furniture | pages [3] -->
m

<!-- b000134 | furniture | pages [3] -->
m

<!-- b000135 | furniture | pages [3] -->
m

<!-- b000136 | furniture | pages [3] -->
m

<!-- b000137 | furniture | pages [3] -->
m

<!-- b000138 | furniture | pages [3] -->
m

<!-- b000139 | furniture | pages [3] -->
m

<!-- b000140 | furniture | pages [3] -->
m

<!-- b000141 | furniture | pages [3] -->
m

<!-- b000142 | furniture | pages [3] -->
m

<!-- b000143 | furniture | pages [3] -->
m

<!-- b000144 | furniture | pages [3] -->
m

<!-- b000145 | furniture | pages [3] -->
m

<!-- b000146 | furniture | pages [3] -->
m

<!-- b000147 | furniture | pages [3] -->
m

<!-- b000148 | furniture | pages [3] -->
m

<!-- b000149 | furniture | pages [3] -->
m

<!-- b000150 | furniture | pages [3] -->
m

<!-- b000151 | furniture | pages [3] -->
m

<!-- b000152 | furniture | pages [3] -->
m

<!-- b000153 | furniture | pages [3] -->
m

<!-- b000154 | furniture | pages [3] -->
m

<!-- b000155 | furniture | pages [3] -->
m

<!-- b000156 | furniture | pages [3] -->
m

<!-- b000157 | furniture | pages [3] -->
m

<!-- b000158 | furniture | pages [3] -->
m

<!-- b000159 | furniture | pages [3] -->
m

<!-- b000160 | furniture | pages [3] -->
m

<!-- b000161 | furniture | pages [3] -->
m

<!-- b000162 | furniture | pages [3] -->
m

<!-- b000163 | furniture | pages [3] -->
m

<!-- b000164 | furniture | pages [3] -->
m

<!-- b000165 | furniture | pages [3] -->
m

<!-- b000166 | furniture | pages [3] -->
m

<!-- b000167 | furniture | pages [3] -->
m

<!-- b000168 | furniture | pages [3] -->
m

<!-- b000169 | furniture | pages [3] -->
m

<!-- b000170 | furniture | pages [3] -->
m

<!-- b000171 | furniture | pages [3] -->
m

<!-- b000172 | furniture | pages [3] -->
m

<!-- b000173 | furniture | pages [3] -->
m

<!-- b000174 | furniture | pages [3] -->
m

<!-- b000175 | furniture | pages [3] -->
m

<!-- b000176 | furniture | pages [3] -->
m

<!-- b000177 | furniture | pages [3] -->
m

<!-- b000178 | furniture | pages [3] -->
m

<!-- b000179 | furniture | pages [3] -->
m

<!-- b000180 | furniture | pages [3] -->
m

<!-- b000181 | furniture | pages [3] -->
m

<!-- b000182 | furniture | pages [3] -->
m

<!-- b000183 | furniture | pages [3] -->
m

<!-- b000184 | furniture | pages [3] -->
m

<!-- b000185 | furniture | pages [3] -->
m

<!-- b000186 | furniture | pages [3] -->
m

<!-- b000187 | furniture | pages [3] -->
m

<!-- b000188 | furniture | pages [3] -->
m

<!-- b000189 | furniture | pages [3] -->
m

<!-- b000190 | furniture | pages [3] -->
m

<!-- b000191 | furniture | pages [3] -->
m

<!-- b000192 | furniture | pages [3] -->
m

<!-- b000193 | furniture | pages [3] -->
m

<!-- b000194 | furniture | pages [3] -->
m

<!-- b000195 | furniture | pages [3] -->
m

<!-- b000196 | furniture | pages [3] -->
m

<!-- b000197 | furniture | pages [3] -->
m

<!-- b000198 | furniture | pages [3] -->
m

<!-- b000199 | furniture | pages [3] -->
m

<!-- b000200 | furniture | pages [3] -->
m

<!-- b000201 | furniture | pages [3] -->
m

<!-- b000202 | furniture | pages [3] -->
m

<!-- b000203 | furniture | pages [3] -->
m

<!-- b000204 | furniture | pages [3] -->
m

<!-- b000205 | furniture | pages [3] -->
m

<!-- b000206 | furniture | pages [3] -->
m

<!-- b000207 | furniture | pages [3] -->
m

<!-- b000208 | furniture | pages [3] -->
m

<!-- b000209 | furniture | pages [3] -->
m

<!-- b000210 | furniture | pages [3] -->
m

<!-- b000211 | furniture | pages [3] -->
m

<!-- b000212 | furniture | pages [3] -->
m

<!-- b000213 | furniture | pages [3] -->
m

<!-- b000214 | furniture | pages [3] -->
m

<!-- b000215 | furniture | pages [3] -->
m

<!-- b000216 | furniture | pages [3] -->
m

<!-- b000217 | furniture | pages [3] -->
m

<!-- b000218 | furniture | pages [3] -->
m

<!-- b000219 | furniture | pages [3] -->
m

<!-- b000220 | furniture | pages [3] -->
m

<!-- b000221 | furniture | pages [3] -->
m

<!-- b000222 | furniture | pages [3] -->
m

<!-- b000223 | furniture | pages [3] -->
m

<!-- b000224 | furniture | pages [3] -->
m

<!-- b000225 | furniture | pages [3] -->
m

<!-- b000226 | furniture | pages [3] -->
m

<!-- b000227 | furniture | pages [3] -->
m

<!-- b000228 | furniture | pages [3] -->
m

<!-- b000229 | furniture | pages [3] -->
m

<!-- b000230 | furniture | pages [3] -->
m

<!-- b000231 | furniture | pages [3] -->
m

<!-- b000232 | furniture | pages [3] -->
m

<!-- b000233 | furniture | pages [3] -->
m

<!-- b000234 | furniture | pages [3] -->
m

<!-- b000235 | furniture | pages [3] -->
m

<!-- b000236 | furniture | pages [3] -->
m

<!-- b000237 | furniture | pages [3] -->
m

<!-- b000238 | furniture | pages [3] -->
m

<!-- b000239 | furniture | pages [3] -->
m

<!-- b000240 | furniture | pages [3] -->
m

<!-- b000241 | furniture | pages [3] -->
m

<!-- b000242 | furniture | pages [3] -->
m

<!-- b000243 | furniture | pages [3] -->
m

<!-- b000244 | furniture | pages [3] -->
m

<!-- b000245 | furniture | pages [3] -->
m

<!-- b000246 | furniture | pages [3] -->
m

<!-- b000247 | furniture | pages [3] -->
m

<!-- b000248 | furniture | pages [3] -->
m

<!-- b000249 | furniture | pages [3] -->
m

<!-- b000250 | furniture | pages [3] -->
m

<!-- b000251 | furniture | pages [3] -->
m

<!-- b000252 | furniture | pages [3] -->
m

<!-- b000253 | furniture | pages [3] -->
m

<!-- b000254 | furniture | pages [3] -->
m

<!-- b000255 | furniture | pages [3] -->
m

<!-- b000256 | furniture | pages [3] -->
m

<!-- b000257 | furniture | pages [3] -->
m

<!-- b000258 | furniture | pages [3] -->
m

<!-- b000259 | furniture | pages [3] -->
m

<!-- b000260 | furniture | pages [3] -->
m

<!-- b000261 | furniture | pages [3] -->
m

<!-- b000262 | furniture | pages [3] -->
m

<!-- b000263 | furniture | pages [3] -->
m

<!-- b000264 | furniture | pages [3] -->
m

<!-- b000265 | furniture | pages [3] -->
m

<!-- b000266 | furniture | pages [3] -->
m

<!-- b000267 | furniture | pages [3] -->
m

<!-- b000268 | furniture | pages [3] -->
m

<!-- b000269 | furniture | pages [3] -->
m

<!-- b000270 | furniture | pages [3] -->
m

<!-- b000271 | furniture | pages [3] -->
m

<!-- b000272 | furniture | pages [3] -->
m

<!-- b000273 | furniture | pages [3] -->
m

<!-- b000274 | furniture | pages [3] -->
m

<!-- b000275 | furniture | pages [3] -->
m

<!-- b000276 | furniture | pages [3] -->
m

<!-- b000277 | furniture | pages [3] -->
m

<!-- b000278 | furniture | pages [3] -->
m

<!-- b000279 | furniture | pages [3] -->
m

<!-- b000280 | furniture | pages [3] -->
m

<!-- b000281 | furniture | pages [3] -->
m

<!-- b000282 | furniture | pages [3] -->
m

<!-- b000283 | furniture | pages [3] -->
m

<!-- b000284 | furniture | pages [3] -->
m

<!-- b000285 | furniture | pages [3] -->
m

<!-- b000286 | furniture | pages [3] -->
m

<!-- b000287 | furniture | pages [3] -->
m

<!-- b000288 | furniture | pages [3] -->
m

<!-- b000289 | furniture | pages [3] -->
m

<!-- b000290 | furniture | pages [3] -->
m

<!-- b000291 | furniture | pages [3] -->
m

<!-- b000292 | furniture | pages [3] -->
m

<!-- b000293 | furniture | pages [3] -->
m

<!-- b000294 | furniture | pages [3] -->
m

<!-- b000295 | furniture | pages [3] -->
m

<!-- b000296 | furniture | pages [3] -->
m

<!-- b000297 | furniture | pages [3] -->
m

<!-- b000298 | furniture | pages [3] -->
m

<!-- b000299 | furniture | pages [3] -->
m

<!-- b000300 | furniture | pages [3] -->
m

<!-- b000301 | furniture | pages [3] -->
m

<!-- b000302 | furniture | pages [3] -->
m

<!-- b000303 | furniture | pages [3] -->
m

<!-- b000304 | furniture | pages [3] -->
m

<!-- b000305 | furniture | pages [3] -->
m

<!-- b000306 | furniture | pages [3] -->
m

<!-- b000307 | furniture | pages [3] -->
m

<!-- b000308 | furniture | pages [3] -->
m

<!-- b000309 | furniture | pages [3] -->
m

<!-- b000310 | furniture | pages [3] -->
m

<!-- b000311 | furniture | pages [3] -->
m

<!-- b000312 | furniture | pages [3] -->
m

<!-- b000313 | furniture | pages [3] -->
m

<!-- b000314 | furniture | pages [3] -->
m

<!-- b000315 | furniture | pages [3] -->
m

<!-- b000316 | furniture | pages [3] -->
m

<!-- b000317 | furniture | pages [3] -->
m

<!-- b000318 | furniture | pages [3] -->
m

<!-- b000319 | furniture | pages [3] -->
m

<!-- b000320 | furniture | pages [3] -->
m

<!-- b000321 | furniture | pages [3] -->
m

<!-- b000322 | furniture | pages [3] -->
m

<!-- b000323 | furniture | pages [3] -->
m

<!-- b000324 | furniture | pages [3] -->
m

<!-- b000325 | furniture | pages [3] -->
m

<!-- b000326 | furniture | pages [3] -->
m

<!-- b000327 | furniture | pages [3] -->
m

<!-- b000328 | furniture | pages [3] -->
m

<!-- b000329 | furniture | pages [3] -->
m

<!-- b000330 | furniture | pages [3] -->
m

<!-- b000331 | furniture | pages [3] -->
m

<!-- b000332 | furniture | pages [3] -->
m

<!-- b000333 | furniture | pages [3] -->
m

<!-- b000334 | furniture | pages [3] -->
m

<!-- b000335 | furniture | pages [3] -->
m

<!-- b000336 | furniture | pages [3] -->
m

<!-- b000337 | furniture | pages [3] -->
m

<!-- b000338 | furniture | pages [3] -->
m

<!-- b000339 | furniture | pages [3] -->
m

<!-- b000340 | furniture | pages [3] -->
m

<!-- b000341 | furniture | pages [3] -->
m

<!-- b000342 | furniture | pages [3] -->
m

<!-- b000343 | furniture | pages [3] -->
m

<!-- b000344 | furniture | pages [3] -->
m

<!-- b000345 | furniture | pages [3] -->
m

<!-- b000346 | furniture | pages [3] -->
m

<!-- b000347 | furniture | pages [3] -->
m

<!-- b000348 | furniture | pages [3] -->
m

<!-- b000349 | furniture | pages [3] -->
m

<!-- b000350 | furniture | pages [3] -->
m

<!-- b000351 | furniture | pages [3] -->
m

<!-- b000352 | furniture | pages [4] -->
Team # 2501869

<!-- b000353 | furniture | pages [4] -->
Page 4 of 25

<!-- b000355 | prose | pages [4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m This finding aligns with the modeling approach adopted in this study, which utilizes Tobit m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and Herdle models to address the unique challenges associated with Olympic medal forecasting. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000356 | heading | pages [4] -->
1.4 Our Work

<!-- b000357 | prose | pages [4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000358 | caption | pages [4] -->
Figure 1 Our Work

<!-- b000359 | heading | pages [4] -->
2 Assumptions and Justification

<!-- b000360 | prose | pages [4] -->
• All models are built based on the normal holding of the Olympic Games, and situations such as the postponement of the Olympic Games will not occur.

<!-- b000361 | prose | pages [4] -->
• The models are built without the influence of external factors (such as political events and national bans), and are based only on existing data.

<!-- b000362 | prose | pages [4] -->
• All data used in this article is real data without statistical errors.

<!-- b000363 | heading | pages [4] -->
3 Notations

<!-- b000364 | prose | pages [4] -->
关注数学模型

<!-- b000365 | furniture | pages [4] -->
2

<!-- b000366 | furniture | pages [4] -->
MATHmodels

<!-- b000367 | furniture | pages [4] -->
获取更多资讯

<!-- b000368 | furniture | pages [5] -->
Team # 2501869

<!-- b000369 | furniture | pages [5] -->
Page 5 of 25

<!-- b000370 | heading | pages [5] -->
Notation

<!-- b000371 | prose | pages [5] -->
Significance

<!-- b000372 | prose | pages [5] -->
Mapdisq∗ Potential medal ability i,t RCA National dominance sports index Nai,t Categories to which the number of players belongs NAE The number of events that won medals in a sport for a country Mi,t The expected number of medals won by country Medal_PCA The number of medals after dimensionality reduction

<!-- b000373 | heading | pages [5] -->
4 Data Processing

<!-- b000374 | heading | pages [5] -->
4.1 Data Cleaning

<!-- b000375 | prose | pages [5] -->
To facilitate forecasting, we exclude vacant items in the tabular data, harmonize country 微信公众号：数学模型 names (e.g., the Russian Olympic Committee and Unified Team in 2024 are grouped together as Russia), harmonize athlete names (e.g., due to differences in hosts and entry rules, Ma Long and Long Ma are actually the same ), harmonization of event names (e.g., “Tabble Tennis Men’s single” in 2024 is the same as “Men’s single “ of table tennis in 2020).

<!-- b000376 | heading | pages [5] -->
4.2 Data Overview

<!-- b000377 | prose | pages [5] -->
The following figure shows a box plot of the total number of medals for all participating countries in the Olympics from 1896-2024. At the same time, we extracted the total medal counts of USA, China, France, Great Britain and Australia to draw a line graph.

<!-- b000378 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000379 | caption | pages [5] -->
Figure 2 Box Plots of Total Medals from 1896 to 2024 and Ray Plots of Medals for 5 Countries

<!-- b000380 | prose | pages [5] -->
As shown in the figure, it can be seen that the box plot shows a right-skewed distribution, i.e., the maximum is much higher than the median and the tails extend to the right, reflecting that a few countries dominate the medal table.

<!-- b000381 | furniture | pages [6] -->
Team # 2501869

<!-- b000382 | furniture | pages [6] -->
Page 6 of 25

<!-- b000383 | prose | pages [6] -->
We calculated the mean, standard deviation, maximum and minimum values for the number of athletes, number of medals, total number of medals, host, number of sport type and number of events in which the countries participates for the 2024 Olympic Games in Paris, France, as shown in the following table.

<!-- b000384 | caption | pages [6] -->
Table 1 Descriptive Statistics

<!-- b000385 | prose | pages [6] -->
Variable Mean SD Min Max

<!-- b000386 | prose | pages [6] -->
Number of Athletes 73.40 144.9809 2 856 Total Medals 11.42 19.7028 1 126 Gold Medals 1.59 4.97 0 40 Silver Medals 1.59 4.83 0 44 Bronze Medals 1.85 4.83 0 42 Host Country 0.01 0.07 0 1 Number of Events 31.27 46.84 1 234 Number of Sports 10.07 10.30 1 47

<!-- b000387 | prose | pages [6] -->
According to the above table, it can be seen that

<!-- b000388 | prose | pages [6] -->
• The large standard deviations of the number of athletes and medals indicate a large degree of dispersion.

<!-- b000389 | prose | pages [6] -->
• Only 1% of the observations are host countries, indicating that the sample of host countries is extremely small, which may affect its statistical significance, which may affect its statistical significance and should be interpreted with caution.

<!-- b000390 | prose | pages [6] -->
• The number of athletes is highly correlated with the number of medals, but it should be noted that there is covariance between the host country variable and the number of athletes in the model, resulting in the host country effect being explained by the number of athletes.

<!-- b000391 | heading | pages [6] -->
5 ComparativeModelingofOlympicMedalProjections: Hurdle-

<!-- b000392 | prose | pages [6] -->
Tobit Framework with Host Country Strategy Analysis

<!-- b000393 | heading | pages [6] -->
5.1 Hurdle and Tobit Models

<!-- b000394 | prose | pages [6] -->
Since the number of medals is a discrete non-negative integer (e.g., 0, 1, 2, etc.), it becomes critical to deal with such a large amount of discrete data, and therefore the counting model is used for the analysis. So we first considered the suggestion of Blais-Morissetr, and Fortin (2017) that a Poisson model be used for handling such data in this case. However, due to significant heterogeneity across countries, the variance is larger than the mean (i.e., the overdispersion problem), which makes the assumptions of the Poisson model not valid.

<!-- b000395 | prose | pages [6] -->
To deal with the over-dispersion problem, we turn to consider the Zinb model (Zero-Inflated Negative Binomial Model), which is applicable when there are a large number of zeros in the data and assumes that the zeros come from two different sources, a “structural zero” (e.g., the country did not (e.g. the country did not participate in the Olympic Games) and “sampling zeros” (e.g. the country participated but did not win a medal). However, since the study

<!-- b000396 | prose | pages [6, 7] -->
关注数学模型 focuses on countries that have participated in the Olympics, structural zeros do not exist and the assumptions of the Zinb model no longer apply.

<!-- b000397 | furniture | pages [6] -->
2

<!-- b000398 | furniture | pages [6] -->
MATHmodels

<!-- b000399 | furniture | pages [6] -->
获取更多资讯

<!-- b000400 | furniture | pages [7] -->
Team # 2501869

<!-- b000401 | furniture | pages [7] -->
Page 7 of 25

<!-- b000403 | prose | pages [7] -->
Then, we turn to use Hurdle model, which differs from the Zinb model in that it does not distinguish between the sources of the zero values, but rather divides the model into two parts: the first part is the decision of whether or not there is at least one medal (Binary Classification Problem), and the second part is the distribution of the number of medals in the event that there is at least one medal. This is similar to the Tobit model (Truncated Regression Model), but whereas the Tobit model assumes that observations below a certain Hurdle are truncated, the Hurdle model explicitly distinguishes between the two processes of whether or not that Hurdle 微信公众号：数学模型 is crossed.

<!-- b000404 | prose | pages [7] -->
Therefore, for the two different scenarios of countries that have never won a medal and sports powerhouses, we improve the use and compare the predictive effectiveness of the four methods of Tobit model, hurdle model, random forest and XGBoost, and select the optimal model for the different scenarios.

<!-- b000405 | prose | pages [7] -->
Step 1: Variable definition and treatment.

<!-- b000406 | prose | pages [7] -->
NAi,t denotes the number of athletes competing in the Olympics for countryi in year t, which was initially analyzed as a continuous variable. However, the marginal returns to the 微信号：MATHmodels number of athletes may be nonlinear and the exact number of participants cannot be known in advance when predicting future medal totals. Therefore, we introduce Nai,t to discretize the number of participating athletes into four categories:

<!-- b000407 | prose | pages [7] -->
• Nai,t = 1: 0 to 9 athletes;

<!-- b000408 | prose | pages [7] -->
• Nai,t = 2: 10 to 49 athletes;

<!-- b000409 | prose | pages [7] -->
• Nai,t = 3: 50 to 149 athletes;

<!-- b000410 | prose | pages [7] -->
• Nai,t = 4: 150 athletes and over

<!-- b000411 | caption | pages [7] -->
Figure 3 The correlation between medal counts

<!-- b000412 | prose | pages [7, 8] -->
From the figures above, it is worth noting that there is a significant multicollinearity between the number of gold medals, silver medals, bronze medals, and medal table. To simplify the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m model, we actually use Principal Component Analysis (PCA) to downscale to one dimension before using it, i.e., Medal_PCA.

<!-- b000413 | furniture | pages [7] -->
m

<!-- b000414 | furniture | pages [7] -->
m

<!-- b000415 | furniture | pages [7] -->
m

<!-- b000416 | furniture | pages [7] -->
m

<!-- b000417 | furniture | pages [7] -->
m

<!-- b000418 | furniture | pages [7] -->
m

<!-- b000419 | furniture | pages [7] -->
m

<!-- b000420 | furniture | pages [7] -->
m

<!-- b000421 | furniture | pages [7] -->
m

<!-- b000422 | furniture | pages [7] -->
m

<!-- b000423 | furniture | pages [7] -->
m

<!-- b000424 | furniture | pages [7] -->
m

<!-- b000425 | furniture | pages [7] -->
m

<!-- b000426 | furniture | pages [7] -->
m

<!-- b000427 | furniture | pages [7] -->
m

<!-- b000428 | furniture | pages [7] -->
m

<!-- b000429 | furniture | pages [7] -->
m

<!-- b000430 | furniture | pages [7] -->
m

<!-- b000431 | furniture | pages [7] -->
m

<!-- b000432 | furniture | pages [7] -->
m

<!-- b000433 | furniture | pages [7] -->
m

<!-- b000434 | furniture | pages [7] -->
m

<!-- b000435 | furniture | pages [7] -->
m

<!-- b000436 | furniture | pages [7] -->
m

<!-- b000437 | furniture | pages [7] -->
m

<!-- b000438 | furniture | pages [7] -->
m

<!-- b000439 | furniture | pages [7] -->
m

<!-- b000440 | furniture | pages [7] -->
m

<!-- b000441 | furniture | pages [7] -->
m

<!-- b000442 | furniture | pages [7] -->
m

<!-- b000443 | furniture | pages [7] -->
m

<!-- b000444 | furniture | pages [7] -->
m

<!-- b000445 | furniture | pages [7] -->
m

<!-- b000446 | furniture | pages [7] -->
m

<!-- b000447 | furniture | pages [7] -->
m

<!-- b000448 | furniture | pages [7] -->
m

<!-- b000449 | furniture | pages [7] -->
m

<!-- b000450 | furniture | pages [7] -->
m

<!-- b000451 | furniture | pages [7] -->
m

<!-- b000452 | furniture | pages [7] -->
m

<!-- b000453 | furniture | pages [7] -->
m

<!-- b000454 | furniture | pages [7] -->
m

<!-- b000455 | furniture | pages [7] -->
m

<!-- b000456 | furniture | pages [7] -->
m

<!-- b000457 | furniture | pages [7] -->
m

<!-- b000458 | furniture | pages [7] -->
m

<!-- b000459 | furniture | pages [7] -->
m

<!-- b000460 | furniture | pages [7] -->
m

<!-- b000461 | furniture | pages [7] -->
m

<!-- b000462 | furniture | pages [7] -->
m

<!-- b000463 | furniture | pages [7] -->
m

<!-- b000464 | furniture | pages [7] -->
m

<!-- b000465 | furniture | pages [7] -->
m

<!-- b000466 | furniture | pages [7] -->
m

<!-- b000467 | furniture | pages [7] -->
m

<!-- b000468 | furniture | pages [7] -->
m

<!-- b000469 | furniture | pages [7] -->
m

<!-- b000470 | furniture | pages [7] -->
m

<!-- b000471 | furniture | pages [7] -->
m

<!-- b000472 | furniture | pages [7] -->
m

<!-- b000473 | furniture | pages [7] -->
m

<!-- b000474 | furniture | pages [7] -->
m

<!-- b000475 | furniture | pages [7] -->
m

<!-- b000476 | furniture | pages [7] -->
m

<!-- b000477 | furniture | pages [7] -->
m

<!-- b000478 | furniture | pages [7] -->
m

<!-- b000479 | furniture | pages [7] -->
m

<!-- b000480 | furniture | pages [7] -->
m

<!-- b000481 | furniture | pages [7] -->
m

<!-- b000482 | furniture | pages [7] -->
m

<!-- b000483 | furniture | pages [7] -->
m

<!-- b000484 | furniture | pages [7] -->
m

<!-- b000485 | furniture | pages [7] -->
m

<!-- b000486 | furniture | pages [7] -->
m

<!-- b000487 | furniture | pages [7] -->
m

<!-- b000488 | furniture | pages [7] -->
m

<!-- b000489 | furniture | pages [7] -->
m

<!-- b000490 | furniture | pages [7] -->
m

<!-- b000491 | furniture | pages [7] -->
m

<!-- b000492 | furniture | pages [7] -->
m

<!-- b000493 | furniture | pages [7] -->
m

<!-- b000494 | furniture | pages [7] -->
m

<!-- b000495 | furniture | pages [7] -->
m

<!-- b000496 | furniture | pages [7] -->
m

<!-- b000497 | furniture | pages [7] -->
m

<!-- b000498 | furniture | pages [7] -->
m

<!-- b000499 | furniture | pages [7] -->
m

<!-- b000500 | furniture | pages [7] -->
m

<!-- b000501 | furniture | pages [7] -->
m

<!-- b000502 | furniture | pages [7] -->
m

<!-- b000503 | furniture | pages [7] -->
m

<!-- b000504 | furniture | pages [7] -->
m

<!-- b000505 | furniture | pages [7] -->
m

<!-- b000506 | furniture | pages [7] -->
m

<!-- b000507 | furniture | pages [7] -->
m

<!-- b000508 | furniture | pages [7] -->
m

<!-- b000509 | furniture | pages [7] -->
m

<!-- b000510 | furniture | pages [7] -->
m

<!-- b000511 | furniture | pages [7] -->
m

<!-- b000512 | furniture | pages [7] -->
m

<!-- b000513 | furniture | pages [7] -->
m

<!-- b000514 | furniture | pages [7] -->
m

<!-- b000515 | furniture | pages [7] -->
m

<!-- b000516 | furniture | pages [7] -->
m

<!-- b000517 | furniture | pages [7] -->
m

<!-- b000518 | furniture | pages [7] -->
m

<!-- b000519 | furniture | pages [7] -->
m

<!-- b000520 | furniture | pages [7] -->
m

<!-- b000521 | furniture | pages [7] -->
m

<!-- b000522 | furniture | pages [7] -->
m

<!-- b000523 | furniture | pages [7] -->
m

<!-- b000524 | furniture | pages [7] -->
m

<!-- b000525 | furniture | pages [7] -->
m

<!-- b000526 | furniture | pages [7] -->
m

<!-- b000527 | furniture | pages [7] -->
m

<!-- b000528 | furniture | pages [7] -->
m

<!-- b000529 | furniture | pages [7] -->
m

<!-- b000530 | furniture | pages [7] -->
m

<!-- b000531 | furniture | pages [7] -->
m

<!-- b000532 | furniture | pages [7] -->
m

<!-- b000533 | furniture | pages [7] -->
m

<!-- b000534 | furniture | pages [7] -->
m

<!-- b000535 | furniture | pages [7] -->
m

<!-- b000536 | furniture | pages [7] -->
m

<!-- b000537 | furniture | pages [7] -->
m

<!-- b000538 | furniture | pages [7] -->
m

<!-- b000539 | furniture | pages [7] -->
m

<!-- b000540 | furniture | pages [7] -->
m

<!-- b000541 | furniture | pages [7] -->
m

<!-- b000542 | furniture | pages [7] -->
m

<!-- b000543 | furniture | pages [7] -->
m

<!-- b000544 | furniture | pages [7] -->
m

<!-- b000545 | furniture | pages [7] -->
m

<!-- b000546 | furniture | pages [7] -->
m

<!-- b000547 | furniture | pages [7] -->
m

<!-- b000548 | furniture | pages [7] -->
m

<!-- b000549 | furniture | pages [7] -->
m

<!-- b000550 | furniture | pages [7] -->
m

<!-- b000551 | furniture | pages [7] -->
m

<!-- b000552 | furniture | pages [7] -->
m

<!-- b000553 | furniture | pages [7] -->
m

<!-- b000554 | furniture | pages [7] -->
m

<!-- b000555 | furniture | pages [7] -->
m

<!-- b000556 | furniture | pages [7] -->
m

<!-- b000557 | furniture | pages [7] -->
m

<!-- b000558 | furniture | pages [7] -->
m

<!-- b000559 | furniture | pages [7] -->
m

<!-- b000560 | furniture | pages [7] -->
m

<!-- b000561 | furniture | pages [7] -->
m

<!-- b000562 | furniture | pages [7] -->
m

<!-- b000563 | furniture | pages [7] -->
m

<!-- b000564 | furniture | pages [7] -->
m

<!-- b000565 | furniture | pages [7] -->
m

<!-- b000566 | furniture | pages [7] -->
m

<!-- b000567 | furniture | pages [7] -->
m

<!-- b000568 | furniture | pages [7] -->
m

<!-- b000569 | furniture | pages [7] -->
m

<!-- b000570 | furniture | pages [7] -->
m

<!-- b000571 | furniture | pages [7] -->
m

<!-- b000572 | furniture | pages [7] -->
m

<!-- b000573 | furniture | pages [7] -->
m

<!-- b000574 | furniture | pages [7] -->
m

<!-- b000575 | furniture | pages [7] -->
m

<!-- b000576 | furniture | pages [7] -->
m

<!-- b000577 | furniture | pages [7] -->
m

<!-- b000578 | furniture | pages [7] -->
m

<!-- b000579 | furniture | pages [7] -->
m

<!-- b000580 | furniture | pages [7] -->
m

<!-- b000581 | furniture | pages [7] -->
m

<!-- b000582 | furniture | pages [7] -->
m

<!-- b000583 | furniture | pages [7] -->
m

<!-- b000584 | furniture | pages [7] -->
m

<!-- b000585 | furniture | pages [7] -->
m

<!-- b000586 | furniture | pages [7] -->
m

<!-- b000587 | furniture | pages [7] -->
m

<!-- b000588 | furniture | pages [7] -->
m

<!-- b000589 | furniture | pages [7] -->
m

<!-- b000590 | furniture | pages [7] -->
m

<!-- b000591 | furniture | pages [7] -->
m

<!-- b000592 | furniture | pages [7] -->
m

<!-- b000593 | furniture | pages [7] -->
m

<!-- b000594 | furniture | pages [7] -->
m

<!-- b000595 | furniture | pages [7] -->
m

<!-- b000596 | furniture | pages [7] -->
m

<!-- b000597 | furniture | pages [7] -->
m

<!-- b000598 | furniture | pages [7] -->
m

<!-- b000599 | furniture | pages [7] -->
m

<!-- b000600 | furniture | pages [7] -->
m

<!-- b000601 | furniture | pages [7] -->
m

<!-- b000602 | furniture | pages [7] -->
m

<!-- b000603 | furniture | pages [7] -->
m

<!-- b000604 | furniture | pages [7] -->
m

<!-- b000605 | furniture | pages [7] -->
m

<!-- b000606 | furniture | pages [7] -->
m

<!-- b000607 | furniture | pages [7] -->
m

<!-- b000608 | furniture | pages [7] -->
m

<!-- b000609 | furniture | pages [7] -->
m

<!-- b000610 | furniture | pages [7] -->
m

<!-- b000611 | furniture | pages [7] -->
m

<!-- b000612 | furniture | pages [7] -->
m

<!-- b000613 | furniture | pages [7] -->
m

<!-- b000614 | furniture | pages [7] -->
m

<!-- b000615 | furniture | pages [7] -->
m

<!-- b000616 | furniture | pages [7] -->
m

<!-- b000617 | furniture | pages [7] -->
m

<!-- b000618 | furniture | pages [7] -->
m

<!-- b000619 | furniture | pages [7] -->
m

<!-- b000620 | furniture | pages [7] -->
m

<!-- b000621 | furniture | pages [7] -->
m

<!-- b000622 | furniture | pages [7] -->
m

<!-- b000623 | furniture | pages [7] -->
m

<!-- b000624 | furniture | pages [7] -->
m

<!-- b000625 | furniture | pages [7] -->
m

<!-- b000626 | furniture | pages [7] -->
m

<!-- b000627 | furniture | pages [7] -->
m

<!-- b000628 | furniture | pages [7] -->
m

<!-- b000629 | furniture | pages [7] -->
m

<!-- b000630 | furniture | pages [7] -->
m

<!-- b000631 | furniture | pages [7] -->
m

<!-- b000632 | furniture | pages [7] -->
m

<!-- b000633 | furniture | pages [7] -->
m

<!-- b000634 | furniture | pages [7] -->
m

<!-- b000635 | furniture | pages [7] -->
m

<!-- b000636 | furniture | pages [7] -->
m

<!-- b000637 | furniture | pages [7] -->
m

<!-- b000638 | furniture | pages [7] -->
m

<!-- b000639 | furniture | pages [7] -->
m

<!-- b000640 | furniture | pages [7] -->
m

<!-- b000641 | furniture | pages [7] -->
m

<!-- b000642 | furniture | pages [7] -->
m

<!-- b000643 | furniture | pages [7] -->
m

<!-- b000644 | furniture | pages [7] -->
m

<!-- b000645 | furniture | pages [7] -->
m

<!-- b000646 | furniture | pages [7] -->
m

<!-- b000647 | furniture | pages [7] -->
m

<!-- b000648 | furniture | pages [7] -->
m

<!-- b000649 | furniture | pages [7] -->
m

<!-- b000650 | furniture | pages [7] -->
m

<!-- b000651 | furniture | pages [7] -->
m

<!-- b000652 | furniture | pages [7] -->
m

<!-- b000653 | furniture | pages [7] -->
m

<!-- b000654 | furniture | pages [7] -->
m

<!-- b000655 | furniture | pages [7] -->
m

<!-- b000656 | furniture | pages [7] -->
m

<!-- b000657 | furniture | pages [7] -->
m

<!-- b000658 | furniture | pages [7] -->
m

<!-- b000659 | furniture | pages [7] -->
m

<!-- b000660 | furniture | pages [7] -->
m

<!-- b000661 | furniture | pages [7] -->
m

<!-- b000662 | furniture | pages [7] -->
m

<!-- b000663 | furniture | pages [7] -->
m

<!-- b000664 | furniture | pages [7] -->
m

<!-- b000665 | furniture | pages [7] -->
m

<!-- b000666 | furniture | pages [7] -->
m

<!-- b000667 | furniture | pages [7] -->
m

<!-- b000668 | furniture | pages [7] -->
m

<!-- b000669 | furniture | pages [7] -->
m

<!-- b000670 | furniture | pages [7] -->
m

<!-- b000671 | furniture | pages [7] -->
m

<!-- b000672 | furniture | pages [7] -->
m

<!-- b000673 | furniture | pages [7] -->
m

<!-- b000674 | furniture | pages [7] -->
m

<!-- b000675 | furniture | pages [7] -->
m

<!-- b000676 | furniture | pages [7] -->
m

<!-- b000677 | furniture | pages [7] -->
m

<!-- b000678 | furniture | pages [7] -->
m

<!-- b000679 | furniture | pages [7] -->
m

<!-- b000680 | furniture | pages [7] -->
m

<!-- b000681 | furniture | pages [7] -->
m

<!-- b000682 | furniture | pages [7] -->
m

<!-- b000683 | furniture | pages [7] -->
m

<!-- b000684 | furniture | pages [7] -->
m

<!-- b000685 | furniture | pages [7] -->
m

<!-- b000686 | furniture | pages [7] -->
m

<!-- b000687 | furniture | pages [7] -->
m

<!-- b000688 | furniture | pages [7] -->
m

<!-- b000689 | furniture | pages [7] -->
m

<!-- b000690 | furniture | pages [7] -->
m

<!-- b000691 | furniture | pages [7] -->
m

<!-- b000692 | furniture | pages [7] -->
m

<!-- b000693 | furniture | pages [7] -->
m

<!-- b000694 | furniture | pages [7] -->
m

<!-- b000695 | furniture | pages [7] -->
m

<!-- b000696 | furniture | pages [7] -->
m

<!-- b000697 | furniture | pages [7] -->
m

<!-- b000698 | furniture | pages [7] -->
m

<!-- b000699 | furniture | pages [7] -->
m

<!-- b000700 | furniture | pages [7] -->
m

<!-- b000701 | furniture | pages [7] -->
m

<!-- b000702 | furniture | pages [7] -->
m

<!-- b000703 | furniture | pages [7] -->
m

<!-- b000704 | furniture | pages [7] -->
m

<!-- b000705 | furniture | pages [7] -->
m

<!-- b000706 | furniture | pages [7] -->
m

<!-- b000707 | furniture | pages [7] -->
m

<!-- b000708 | furniture | pages [7] -->
m

<!-- b000709 | furniture | pages [7] -->
m

<!-- b000710 | furniture | pages [7] -->
m

<!-- b000711 | furniture | pages [7] -->
m

<!-- b000712 | furniture | pages [7] -->
m

<!-- b000713 | furniture | pages [7] -->
m

<!-- b000714 | furniture | pages [7] -->
m

<!-- b000715 | furniture | pages [7] -->
m

<!-- b000716 | furniture | pages [7] -->
m

<!-- b000717 | furniture | pages [7] -->
m

<!-- b000718 | furniture | pages [7] -->
m

<!-- b000719 | furniture | pages [7] -->
m

<!-- b000720 | furniture | pages [7] -->
m

<!-- b000721 | furniture | pages [7] -->
m

<!-- b000722 | furniture | pages [7] -->
m

<!-- b000723 | furniture | pages [7] -->
m

<!-- b000724 | furniture | pages [7] -->
m

<!-- b000725 | furniture | pages [7] -->
m

<!-- b000726 | furniture | pages [7] -->
m

<!-- b000727 | furniture | pages [7] -->
m

<!-- b000728 | furniture | pages [7] -->
m

<!-- b000729 | furniture | pages [7] -->
m

<!-- b000730 | furniture | pages [7] -->
m

<!-- b000731 | furniture | pages [7] -->
m

<!-- b000732 | furniture | pages [7] -->
m

<!-- b000733 | furniture | pages [7] -->
m

<!-- b000734 | furniture | pages [7] -->
m

<!-- b000735 | furniture | pages [7] -->
m

<!-- b000736 | furniture | pages [7] -->
m

<!-- b000737 | furniture | pages [8] -->
Team # 2501869

<!-- b000738 | furniture | pages [8] -->
Page 8 of 25

<!-- b000740 | prose | pages [8] -->
At the same time each country should have its dominant sport, in order to include it in the model we introduce RCA to refer to quantify the dominant sport of each country. RCA is given by the following formula:

<!-- b000741 | prose | pages [8] -->
RCA = Mij/Mi (1) Tj/T

<!-- b000742 | prose | pages [8] -->
Here, Mij represents the number of medals for country i in sport j;Mi represents the total number of medals for country i; Tj represents total global medals in sport j; T represents total medals in all sports.

<!-- b000743 | prose | pages [8] -->
RCA > 1: country has a comparative advantage in the given sport;

<!-- b000744 | prose | pages [8] -->
m m m m m m m m m m m m m m m m m m m m m m RCA < 1: country has a comparative disadvantage in the given sport.= m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The figure below shows the RCA index heat maps of the countries that won medals at Paris m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2024. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000745 | caption | pages [8] -->
Figure 4 RCA Index Heatmap

<!-- b000746 | prose | pages [8] -->
Step 2: Define latent variable Xi,tΘ and potential medal abilityMapdisq∗ i,t.

<!-- b000747 | prose | pages [8] -->
Depending on the set of explanatory variables selected, we define latent variable Xi,tΘ by:

<!-- b000748 | prose | pages [8] -->
X X X Xi,tΘ = c+λ ln Ni,t−4+ρHosti,t+ γRCAp,i+δMedal_PCAi,t−4+ ζNum_Eventsp,i,t+κ NAEp, p p p (2)

<!-- b000749 | prose | pages [8] -->
Here, Xi,tΘ = [Xi,tΘGold, Xi,tΘSilver, Xi,tΘBronze]T. Hosti,t isthehostvariable(Hosti,t=1, country i is the host of the t Olympic Games). Num_Eventsp,i,t is the number of events in

<!-- b000750 | prose | pages [8, 9] -->
关注数学模型 which the i country participated in the p sport of the t Olympic Games. c, λ,ρ, γ, δ, ζ, κ ∈R3are all coefficients, representing the value of Xi,tΘ for gold, silver and bronze respectively, which are calculated by maximum likelihood estimation (MLE) based on historical data.

<!-- b000751 | furniture | pages [8] -->
2

<!-- b000752 | furniture | pages [8] -->
MATHmodels

<!-- b000753 | furniture | pages [8] -->
获取更多资讯

<!-- b000754 | furniture | pages [9] -->
Team # 2501869

<!-- b000755 | furniture | pages [9] -->
Page 9 of 25

<!-- b000757 | prose | pages [9] -->
We define potential medal ability Mapdisq∗ i,t by: 微信公众号：数学模型 Mapdisq∗ i,t = Xi,tΘ + ui + ϵi,t (3)

<!-- b000758 | prose | pages [9] -->
Here, ui represents country-specific random effects (such as culture, training system and other unobserved factors), following a normal distribution N (0, σ2 u) ; ϵi,t is a random error term.

<!-- b000759 | prose | pages [9] -->
Step 3: Construct Tobit model.

<!-- b000760 | prose | pages [9] -->
For the Tobit Model, the general specification is:

<!-- b000761 | prose | pages [9] -->
 Mapdisq∗ , if Mapdisq∗ i,t > 0 i,t 微信号：MATHmodels Mapdisqi,t = (4) i,t ⩽0 , if Mapdisq∗ 0

<!-- b000762 | prose | pages [9] -->
The predicted medal count Mapdisqi,t is a truncated version of the potential medal ability Mapdisq∗ i,t.

<!-- b000763 | prose | pages [9] -->
Step 4: Construct Hurdle model.

<!-- b000764 | prose | pages [9] -->
Mapdisq∗    1) Calculate the probability of winning P i,t > 0 .

<!-- b000765 | prose | pages [9] -->
We use the Logit model to calculate the probability that the i country will get at least one medal, as follows:

<!-- b000766 | prose | pages [9] -->
1 Mapdisq∗    P i,t > 0 = (5) 1 + e−Xi,tΘ

<!-- b000767 | prose | pages [9] -->
2) Calculate the expected number of medals won by the winning countryMi,t.

<!-- b000768 | prose | pages [9] -->
First, we define µi,t as the theoretical mean of the number of medals for country i under the condition of "winning at least one medal", the formula is:

<!-- b000769 | prose | pages [9] -->
µi,t = eXi,tΘ (6)

<!-- b000770 | prose | pages [9] -->
Then, to adjust the expected value since only the winning country is considered (i.e. zero values are excluded), we define the truncated correction E(Mapdisq∗ i,t) as:

<!-- b000771 | prose | pages [9] -->
1 E(Mapdisq∗ i,t) = µi,t · (7) 1 −(1 + µi,t/r)−r

<!-- b000772 | prose | pages [9] -->
where r is a discrete parameter.

<!-- b000773 | prose | pages [9] -->
Finally, the expected number of medals won by the winning country Mi,t is given by:

<!-- b000774 | prose | pages [9] -->
Mapdisq∗ · E(Mapdisq∗    Mi,t = P i,t > 0 i,t) (8)

<!-- b000775 | heading | pages [9] -->
5.2 Model Selection and Validation

<!-- b000776 | heading | pages [9] -->
5.2.1 Model Selection: Hurdle, Tobit, XGBoost and Ramdom Forest

<!-- b000777 | prose | pages [9, 10] -->
In this study, we employ four models—the Tobit model, the Hurdle model, Random Forest, and XGBoost—to predict the total number of medals won by the United States in the 2024 Olympic Games in Paris, France. This approach is taken to assess the accuracy of the four models’ prediction results.The comparison between the prediction results based on the four methods and the real data is shown below.

<!-- b000778 | furniture | pages [10] -->
Team # 2501869

<!-- b000779 | furniture | pages [10] -->
Page 10 of 25

<!-- b000781 | caption | pages [10] -->
Figure 5 Prediction Results Based on the Four Methods Compared with the Real Data

<!-- b000782 | caption | pages [10] -->
Table 2 Model Performance Comparison (MSE and R2)

<!-- b000783 | prose | pages [10] -->
Hurdle Tobit XGBoost Ramdom Forest

<!-- b000784 | prose | pages [10] -->
MSE 20.15 23.01 63.67 51.25 R2 0.8545 0.8026 0.7121 0.758

<!-- b000785 | prose | pages [10] -->
As shown in the figure, Hurdle and Hurdle perform better, and the prediction results of Random Forest & XGBoost are poorly fitted to the real values. In the case of Random Forest with XGBoost, the predicted values are biased in the region of actual medal count >15, i.e., it is difficult to deal with the distributional characteristics of zero-inflated data effectively. Meanwhile, the prediction points in countries with large medal counts (actual values > 50) are scattered and irregular, reflecting the model’s insufficient ability to capture extreme values.

<!-- b000786 | prose | pages [10, 11] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Meanwhile, the MSE of Hurdle and Tobit is significantly lower than that of XGBoost and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Random Forest, which indicates that the former two models are better in prediction accuracy.The m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m R2 of Hurdle and Tobit is significantly higher than that of the former two. This indicates that Hurdle and Tobit models are more effective in explaining data variability.

<!-- b000787 | furniture | pages [10] -->
2

<!-- b000788 | furniture | pages [10] -->
m

<!-- b000789 | furniture | pages [10] -->
m

<!-- b000790 | furniture | pages [10] -->
m

<!-- b000791 | furniture | pages [10] -->
m

<!-- b000792 | furniture | pages [10] -->
m

<!-- b000793 | furniture | pages [10] -->
m

<!-- b000794 | furniture | pages [10] -->
m

<!-- b000795 | furniture | pages [10] -->
m

<!-- b000796 | furniture | pages [10] -->
m

<!-- b000797 | furniture | pages [10] -->
m

<!-- b000798 | furniture | pages [10] -->
m

<!-- b000799 | furniture | pages [10] -->
m

<!-- b000800 | furniture | pages [10] -->
m

<!-- b000801 | furniture | pages [10] -->
m

<!-- b000802 | furniture | pages [10] -->
m

<!-- b000803 | furniture | pages [10] -->
m

<!-- b000804 | furniture | pages [10] -->
m

<!-- b000805 | furniture | pages [10] -->
m

<!-- b000806 | furniture | pages [10] -->
m

<!-- b000807 | furniture | pages [10] -->
m

<!-- b000808 | furniture | pages [10] -->
m

<!-- b000809 | furniture | pages [10] -->
m

<!-- b000810 | furniture | pages [10] -->
m

<!-- b000811 | furniture | pages [10] -->
m

<!-- b000812 | furniture | pages [10] -->
m

<!-- b000813 | furniture | pages [10] -->
m

<!-- b000814 | furniture | pages [10] -->
m

<!-- b000815 | furniture | pages [10] -->
m

<!-- b000816 | furniture | pages [10] -->
m

<!-- b000817 | furniture | pages [10] -->
m

<!-- b000818 | furniture | pages [10] -->
m

<!-- b000819 | furniture | pages [10] -->
m

<!-- b000820 | furniture | pages [10] -->
m

<!-- b000821 | furniture | pages [10] -->
m

<!-- b000822 | furniture | pages [10] -->
m

<!-- b000823 | furniture | pages [10] -->
m

<!-- b000824 | furniture | pages [10] -->
m

<!-- b000825 | furniture | pages [10] -->
m

<!-- b000826 | furniture | pages [10] -->
m

<!-- b000827 | furniture | pages [10] -->
m

<!-- b000828 | furniture | pages [10] -->
m

<!-- b000829 | furniture | pages [10] -->
m

<!-- b000830 | furniture | pages [10] -->
m

<!-- b000831 | furniture | pages [10] -->
m

<!-- b000832 | furniture | pages [10] -->
m

<!-- b000833 | furniture | pages [10] -->
m

<!-- b000834 | furniture | pages [10] -->
m

<!-- b000835 | furniture | pages [10] -->
m

<!-- b000836 | furniture | pages [10] -->
m

<!-- b000837 | furniture | pages [10] -->
m

<!-- b000838 | furniture | pages [10] -->
m

<!-- b000839 | furniture | pages [10] -->
m

<!-- b000840 | furniture | pages [10] -->
m

<!-- b000841 | furniture | pages [10] -->
m

<!-- b000842 | furniture | pages [10] -->
m

<!-- b000843 | furniture | pages [10] -->
m

<!-- b000844 | furniture | pages [10] -->
m

<!-- b000845 | furniture | pages [10] -->
m

<!-- b000846 | furniture | pages [10] -->
m

<!-- b000847 | furniture | pages [10] -->
m

<!-- b000848 | furniture | pages [10] -->
m

<!-- b000849 | furniture | pages [10] -->
m

<!-- b000850 | furniture | pages [10] -->
m

<!-- b000851 | furniture | pages [10] -->
m

<!-- b000852 | furniture | pages [10] -->
m

<!-- b000853 | furniture | pages [10] -->
m

<!-- b000854 | furniture | pages [10] -->
m

<!-- b000855 | furniture | pages [10] -->
m

<!-- b000856 | furniture | pages [10] -->
m

<!-- b000857 | furniture | pages [10] -->
m

<!-- b000858 | furniture | pages [10] -->
m

<!-- b000859 | furniture | pages [10] -->
m

<!-- b000860 | furniture | pages [10] -->
m

<!-- b000861 | furniture | pages [10] -->
m

<!-- b000862 | furniture | pages [10] -->
m

<!-- b000863 | furniture | pages [10] -->
m

<!-- b000864 | furniture | pages [10] -->
m

<!-- b000865 | furniture | pages [10] -->
m

<!-- b000866 | furniture | pages [10] -->
m

<!-- b000867 | furniture | pages [10] -->
m

<!-- b000868 | furniture | pages [10] -->
m

<!-- b000869 | furniture | pages [10] -->
m

<!-- b000870 | furniture | pages [10] -->
m

<!-- b000871 | furniture | pages [10] -->
m

<!-- b000872 | furniture | pages [10] -->
m

<!-- b000873 | furniture | pages [10] -->
m

<!-- b000874 | furniture | pages [10] -->
m

<!-- b000875 | furniture | pages [10] -->
m

<!-- b000876 | furniture | pages [10] -->
m

<!-- b000877 | furniture | pages [10] -->
m

<!-- b000878 | furniture | pages [10] -->
m

<!-- b000879 | furniture | pages [10] -->
m

<!-- b000880 | furniture | pages [10] -->
m

<!-- b000881 | furniture | pages [10] -->
m

<!-- b000882 | furniture | pages [10] -->
m

<!-- b000883 | furniture | pages [10] -->
m

<!-- b000884 | furniture | pages [10] -->
m

<!-- b000885 | furniture | pages [10] -->
m

<!-- b000886 | furniture | pages [10] -->
m

<!-- b000887 | furniture | pages [10] -->
m

<!-- b000888 | furniture | pages [10] -->
m

<!-- b000889 | furniture | pages [10] -->
m

<!-- b000890 | furniture | pages [10] -->
m

<!-- b000891 | furniture | pages [10] -->
m

<!-- b000892 | furniture | pages [10] -->
m

<!-- b000893 | furniture | pages [10] -->
m

<!-- b000894 | furniture | pages [10] -->
m

<!-- b000895 | furniture | pages [10] -->
m

<!-- b000896 | furniture | pages [10] -->
m

<!-- b000897 | furniture | pages [10] -->
m

<!-- b000898 | furniture | pages [10] -->
m

<!-- b000899 | furniture | pages [10] -->
MATHmodels

<!-- b000900 | furniture | pages [10] -->
获取更多资讯

<!-- b000901 | furniture | pages [10] -->
m

<!-- b000902 | furniture | pages [10] -->
m

<!-- b000903 | furniture | pages [10] -->
m

<!-- b000904 | furniture | pages [10] -->
m

<!-- b000905 | furniture | pages [10] -->
m

<!-- b000906 | furniture | pages [10] -->
m

<!-- b000907 | furniture | pages [10] -->
m

<!-- b000908 | furniture | pages [10] -->
m

<!-- b000909 | furniture | pages [10] -->
m

<!-- b000910 | furniture | pages [10] -->
m

<!-- b000911 | furniture | pages [10] -->
m

<!-- b000912 | furniture | pages [10] -->
m

<!-- b000913 | furniture | pages [10] -->
m

<!-- b000914 | furniture | pages [10] -->
m

<!-- b000915 | furniture | pages [10] -->
m

<!-- b000916 | furniture | pages [10] -->
m

<!-- b000917 | furniture | pages [10] -->
m

<!-- b000918 | furniture | pages [10] -->
m

<!-- b000919 | furniture | pages [10] -->
m

<!-- b000920 | furniture | pages [10] -->
m

<!-- b000921 | furniture | pages [10] -->
m

<!-- b000922 | furniture | pages [10] -->
m

<!-- b000923 | furniture | pages [10] -->
m

<!-- b000924 | furniture | pages [10] -->
m

<!-- b000925 | furniture | pages [10] -->
m

<!-- b000926 | furniture | pages [10] -->
m

<!-- b000927 | furniture | pages [10] -->
m

<!-- b000928 | furniture | pages [10] -->
m

<!-- b000929 | furniture | pages [10] -->
m

<!-- b000930 | furniture | pages [10] -->
m

<!-- b000931 | furniture | pages [10] -->
m

<!-- b000932 | furniture | pages [10] -->
m

<!-- b000933 | furniture | pages [10] -->
m

<!-- b000934 | furniture | pages [10] -->
m

<!-- b000935 | furniture | pages [10] -->
m

<!-- b000936 | furniture | pages [10] -->
m

<!-- b000937 | furniture | pages [10] -->
m

<!-- b000938 | furniture | pages [10] -->
m

<!-- b000939 | furniture | pages [10] -->
m

<!-- b000940 | furniture | pages [10] -->
m

<!-- b000941 | furniture | pages [10] -->
m

<!-- b000942 | furniture | pages [10] -->
m

<!-- b000943 | furniture | pages [10] -->
m

<!-- b000944 | furniture | pages [10] -->
m

<!-- b000945 | furniture | pages [10] -->
m

<!-- b000946 | furniture | pages [10] -->
m

<!-- b000947 | furniture | pages [10] -->
m

<!-- b000948 | furniture | pages [10] -->
m

<!-- b000949 | furniture | pages [10] -->
m

<!-- b000950 | furniture | pages [10] -->
m

<!-- b000951 | furniture | pages [10] -->
m

<!-- b000952 | furniture | pages [10] -->
m

<!-- b000953 | furniture | pages [10] -->
m

<!-- b000954 | furniture | pages [10] -->
m

<!-- b000955 | furniture | pages [10] -->
m

<!-- b000956 | furniture | pages [10] -->
m

<!-- b000957 | furniture | pages [10] -->
m

<!-- b000958 | furniture | pages [10] -->
m

<!-- b000959 | furniture | pages [10] -->
m

<!-- b000960 | furniture | pages [10] -->
m

<!-- b000961 | furniture | pages [11] -->
Team # 2501869

<!-- b000962 | furniture | pages [11] -->
Page 11 of 25

<!-- b000964 | heading | pages [11] -->
5.2.2 Model Validation: 2024 Olympic Games Predictions Based on Hurdle and Tobit

<!-- b000965 | prose | pages [11] -->
We choose the Hurdle and Tobit models with better prediction performance to present the prediction results for the prediction interval and accuracy of the total medal count of 2024 Paris Games.

<!-- b000966 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000967 | caption | pages [11] -->
Table 3 Forecast of Olympic Medals for the 2024 Paris Games

<!-- b000968 | prose | pages [11] -->
Hurdle Model Tobit Model Country Actual Medals Forecast Lower CI Upper CI Forecast Lower CI Upper CI

<!-- b000969 | prose | pages [11] -->
120 105 United States 126 103 134 95 113 89 106 China 91 86 93 95 117 68 56 Great Britain 65 63 53 51 61 70 69 France 64 63 77 66 71 48 46 Australia 53 44 52 44 58 47 44 Japan 45 42 51 42 46 微信号：MATHmodels 43 48 Italy 40 38 48 43 53

<!-- b000970 | prose | pages [11] -->
Rate of right forecasts for 2024 Paris Olympic Games

<!-- b000971 | prose | pages [11] -->
All countries (192) CI to 95%(+ or -2) 88.6% (93.2%) 83.8% (90.6%) Exact forecasts (+ or - 1) 21.9% (77.1%) 43.2% (74.5%) Exact forecasts (0 medal) 41.3% 69.1% (107 countries) Exact forecasts (non-0 medal) 22.4% 10.4% (85 countries) Countries with at least 3 medals(56) CI to 95%(+ or -2) 62.3% (76.8%) 50.2% (69.6%) Exact forecasts (+ or - 1) 8.9% (38.5%) 8.9% (31.4%) Note: CI = confidence interval; forecasts in bold.

<!-- b000972 | prose | pages [11] -->
First, in the 95% confidence interval prediction coverage, the Hurdle model covers 88.6% of all 192 countries, which is higher than the 83.8% of the Tobit model; among the 56 countries with at least 3 medals, its coverage (62.3%) is also much higher than that of the Tobit model (50.2%). In addition, the prediction accuracy of the Hurdle model for countries with non-zero medals (±1 error rate of 22.4%) is more than twice that of the Tobit model (10.4%), highlighting the advantage of its two-stage modeling in adapting to zero-inflated data.

<!-- b000973 | prose | pages [11] -->
Although the Tobit model has a higher rate of fully accurate predictions in zero-medal countries (69.1%) than the Hurdle model (41.3%), this advantage comes at the expense of the ability to predict non-zero medals.The Hurdle model is more balanced between the two types of scenarios by separating the mechanisms of zero value generation and positive prediction, and it is particularly robust in countries with high medal counts (±1 error bracket value 38.5% vs. 31.4%).

<!-- b000974 | prose | pages [11, 12] -->
In summary, the Tobit model fits better around zero medals, thanks to its truncated regression m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m assumptions for the lower bound values. However, as the number of medals increases, the dispersion increases significantly, exposing the limitations of the single continuous distribution assumption. In contrast, Hurdle’s model, through two-stage modeling, shows better prediction results in both the zero-value region and the high medal region, with a concentrated distribution of points and low dispersion, which effectively balances the zero-value generating mechanism with the flexibility of positive prediction.

<!-- b000975 | furniture | pages [11] -->
m

<!-- b000976 | furniture | pages [11] -->
m

<!-- b000977 | furniture | pages [11] -->
m

<!-- b000978 | furniture | pages [11] -->
m

<!-- b000979 | furniture | pages [11] -->
m

<!-- b000980 | furniture | pages [11] -->
m

<!-- b000981 | furniture | pages [11] -->
m

<!-- b000982 | furniture | pages [11] -->
m

<!-- b000983 | furniture | pages [11] -->
m

<!-- b000984 | furniture | pages [11] -->
m

<!-- b000985 | furniture | pages [11] -->
m

<!-- b000986 | furniture | pages [11] -->
m

<!-- b000987 | furniture | pages [11] -->
m

<!-- b000988 | furniture | pages [11] -->
m

<!-- b000989 | furniture | pages [11] -->
m

<!-- b000990 | furniture | pages [11] -->
m

<!-- b000991 | furniture | pages [11] -->
m

<!-- b000992 | furniture | pages [11] -->
m

<!-- b000993 | furniture | pages [11] -->
m

<!-- b000994 | furniture | pages [11] -->
m

<!-- b000995 | furniture | pages [11] -->
m

<!-- b000996 | furniture | pages [11] -->
m

<!-- b000997 | furniture | pages [11] -->
m

<!-- b000998 | furniture | pages [11] -->
m

<!-- b000999 | furniture | pages [11] -->
m

<!-- b001000 | furniture | pages [11] -->
m

<!-- b001001 | furniture | pages [11] -->
m

<!-- b001002 | furniture | pages [11] -->
m

<!-- b001003 | furniture | pages [11] -->
m

<!-- b001004 | furniture | pages [11] -->
m

<!-- b001005 | furniture | pages [11] -->
m

<!-- b001006 | furniture | pages [11] -->
m

<!-- b001007 | furniture | pages [11] -->
m

<!-- b001008 | furniture | pages [11] -->
m

<!-- b001009 | furniture | pages [11] -->
m

<!-- b001010 | furniture | pages [11] -->
m

<!-- b001011 | furniture | pages [11] -->
m

<!-- b001012 | furniture | pages [11] -->
m

<!-- b001013 | furniture | pages [11] -->
m

<!-- b001014 | furniture | pages [11] -->
m

<!-- b001015 | furniture | pages [11] -->
m

<!-- b001016 | furniture | pages [11] -->
m

<!-- b001017 | furniture | pages [11] -->
m

<!-- b001018 | furniture | pages [11] -->
m

<!-- b001019 | furniture | pages [11] -->
m

<!-- b001020 | furniture | pages [11] -->
m

<!-- b001021 | furniture | pages [11] -->
m

<!-- b001022 | furniture | pages [11] -->
m

<!-- b001023 | furniture | pages [11] -->
m

<!-- b001024 | furniture | pages [11] -->
m

<!-- b001025 | furniture | pages [11] -->
m

<!-- b001026 | furniture | pages [11] -->
m

<!-- b001027 | furniture | pages [11] -->
m

<!-- b001028 | furniture | pages [11] -->
m

<!-- b001029 | furniture | pages [11] -->
m

<!-- b001030 | furniture | pages [11] -->
m

<!-- b001031 | furniture | pages [11] -->
m

<!-- b001032 | furniture | pages [11] -->
m

<!-- b001033 | furniture | pages [11] -->
m

<!-- b001034 | furniture | pages [11] -->
m

<!-- b001035 | furniture | pages [11] -->
m

<!-- b001036 | furniture | pages [11] -->
m

<!-- b001037 | furniture | pages [11] -->
m

<!-- b001038 | furniture | pages [11] -->
m

<!-- b001039 | furniture | pages [11] -->
m

<!-- b001040 | furniture | pages [11] -->
m

<!-- b001041 | furniture | pages [11] -->
m

<!-- b001042 | furniture | pages [11] -->
m

<!-- b001043 | furniture | pages [11] -->
m

<!-- b001044 | furniture | pages [11] -->
m

<!-- b001045 | furniture | pages [11] -->
m

<!-- b001046 | furniture | pages [11] -->
m

<!-- b001047 | furniture | pages [11] -->
m

<!-- b001048 | furniture | pages [11] -->
m

<!-- b001049 | furniture | pages [11] -->
m

<!-- b001050 | furniture | pages [11] -->
m

<!-- b001051 | furniture | pages [11] -->
m

<!-- b001052 | furniture | pages [11] -->
m

<!-- b001053 | furniture | pages [11] -->
m

<!-- b001054 | furniture | pages [11] -->
m

<!-- b001055 | furniture | pages [11] -->
m

<!-- b001056 | furniture | pages [11] -->
m

<!-- b001057 | furniture | pages [11] -->
m

<!-- b001058 | furniture | pages [11] -->
m

<!-- b001059 | furniture | pages [11] -->
m

<!-- b001060 | furniture | pages [11] -->
m

<!-- b001061 | furniture | pages [11] -->
m

<!-- b001062 | furniture | pages [11] -->
m

<!-- b001063 | furniture | pages [11] -->
m

<!-- b001064 | furniture | pages [11] -->
m

<!-- b001065 | furniture | pages [11] -->
m

<!-- b001066 | furniture | pages [11] -->
m

<!-- b001067 | furniture | pages [11] -->
m

<!-- b001068 | furniture | pages [11] -->
m

<!-- b001069 | furniture | pages [11] -->
m

<!-- b001070 | furniture | pages [11] -->
m

<!-- b001071 | furniture | pages [11] -->
m

<!-- b001072 | furniture | pages [11] -->
m

<!-- b001073 | furniture | pages [11] -->
m

<!-- b001074 | furniture | pages [11] -->
m

<!-- b001075 | furniture | pages [11] -->
m

<!-- b001076 | furniture | pages [11] -->
m

<!-- b001077 | furniture | pages [11] -->
m

<!-- b001078 | furniture | pages [11] -->
m

<!-- b001079 | furniture | pages [11] -->
m

<!-- b001080 | furniture | pages [11] -->
m

<!-- b001081 | furniture | pages [11] -->
m

<!-- b001082 | furniture | pages [11] -->
m

<!-- b001083 | furniture | pages [11] -->
m

<!-- b001084 | furniture | pages [11] -->
m

<!-- b001085 | furniture | pages [11] -->
m

<!-- b001086 | furniture | pages [11] -->
m

<!-- b001087 | furniture | pages [11] -->
m

<!-- b001088 | furniture | pages [11] -->
m

<!-- b001089 | furniture | pages [11] -->
m

<!-- b001090 | furniture | pages [11] -->
m

<!-- b001091 | furniture | pages [11] -->
m

<!-- b001092 | furniture | pages [11] -->
m

<!-- b001093 | furniture | pages [11] -->
m

<!-- b001094 | furniture | pages [11] -->
m

<!-- b001095 | furniture | pages [11] -->
m

<!-- b001096 | furniture | pages [11] -->
m

<!-- b001097 | furniture | pages [11] -->
m

<!-- b001098 | furniture | pages [11] -->
m

<!-- b001099 | furniture | pages [11] -->
m

<!-- b001100 | furniture | pages [11] -->
m

<!-- b001101 | furniture | pages [11] -->
m

<!-- b001102 | furniture | pages [11] -->
m

<!-- b001103 | furniture | pages [11] -->
m

<!-- b001104 | furniture | pages [11] -->
m

<!-- b001105 | furniture | pages [11] -->
m

<!-- b001106 | furniture | pages [11] -->
m

<!-- b001107 | furniture | pages [11] -->
m

<!-- b001108 | furniture | pages [11] -->
m

<!-- b001109 | furniture | pages [11] -->
m

<!-- b001110 | furniture | pages [11] -->
m

<!-- b001111 | furniture | pages [11] -->
m

<!-- b001112 | furniture | pages [11] -->
m

<!-- b001113 | furniture | pages [11] -->
m

<!-- b001114 | furniture | pages [11] -->
m

<!-- b001115 | furniture | pages [11] -->
m

<!-- b001116 | furniture | pages [11] -->
m

<!-- b001117 | furniture | pages [11] -->
m

<!-- b001118 | furniture | pages [11] -->
m

<!-- b001119 | furniture | pages [11] -->
m

<!-- b001120 | furniture | pages [11] -->
m

<!-- b001121 | furniture | pages [11] -->
m

<!-- b001122 | furniture | pages [11] -->
m

<!-- b001123 | furniture | pages [11] -->
m

<!-- b001124 | furniture | pages [11] -->
m

<!-- b001125 | furniture | pages [11] -->
m

<!-- b001126 | furniture | pages [11] -->
m

<!-- b001127 | furniture | pages [11] -->
m

<!-- b001128 | furniture | pages [11] -->
m

<!-- b001129 | furniture | pages [11] -->
m

<!-- b001130 | furniture | pages [11] -->
m

<!-- b001131 | furniture | pages [11] -->
m

<!-- b001132 | furniture | pages [11] -->
m

<!-- b001133 | furniture | pages [11] -->
m

<!-- b001134 | furniture | pages [11] -->
m

<!-- b001135 | furniture | pages [11] -->
m

<!-- b001136 | furniture | pages [11] -->
m

<!-- b001137 | furniture | pages [11] -->
m

<!-- b001138 | furniture | pages [11] -->
m

<!-- b001139 | furniture | pages [11] -->
m

<!-- b001140 | furniture | pages [11] -->
m

<!-- b001141 | furniture | pages [11] -->
m

<!-- b001142 | furniture | pages [11] -->
m

<!-- b001143 | furniture | pages [11] -->
m

<!-- b001144 | furniture | pages [11] -->
m

<!-- b001145 | furniture | pages [11] -->
m

<!-- b001146 | furniture | pages [11] -->
m

<!-- b001147 | furniture | pages [11] -->
m

<!-- b001148 | furniture | pages [11] -->
m

<!-- b001149 | furniture | pages [11] -->
m

<!-- b001150 | furniture | pages [11] -->
m

<!-- b001151 | furniture | pages [11] -->
m

<!-- b001152 | furniture | pages [11] -->
m

<!-- b001153 | furniture | pages [11] -->
m

<!-- b001154 | furniture | pages [11] -->
m

<!-- b001155 | furniture | pages [11] -->
m

<!-- b001156 | furniture | pages [11] -->
m

<!-- b001157 | furniture | pages [11] -->
m

<!-- b001158 | furniture | pages [11] -->
m

<!-- b001159 | furniture | pages [11] -->
m

<!-- b001160 | furniture | pages [11] -->
m

<!-- b001161 | furniture | pages [11] -->
m

<!-- b001162 | furniture | pages [11] -->
m

<!-- b001163 | furniture | pages [11] -->
m

<!-- b001164 | furniture | pages [11] -->
m

<!-- b001165 | furniture | pages [11] -->
m

<!-- b001166 | furniture | pages [11] -->
m

<!-- b001167 | furniture | pages [11] -->
m

<!-- b001168 | furniture | pages [11] -->
m

<!-- b001169 | furniture | pages [11] -->
m

<!-- b001170 | furniture | pages [11] -->
m

<!-- b001171 | furniture | pages [11] -->
m

<!-- b001172 | furniture | pages [11] -->
m

<!-- b001173 | furniture | pages [11] -->
m

<!-- b001174 | furniture | pages [11] -->
m

<!-- b001175 | furniture | pages [11] -->
m

<!-- b001176 | furniture | pages [11] -->
m

<!-- b001177 | furniture | pages [11] -->
m

<!-- b001178 | furniture | pages [11] -->
m

<!-- b001179 | furniture | pages [11] -->
m

<!-- b001180 | furniture | pages [11] -->
m

<!-- b001181 | furniture | pages [11] -->
m

<!-- b001182 | furniture | pages [11] -->
m

<!-- b001183 | furniture | pages [11] -->
m

<!-- b001184 | furniture | pages [11] -->
m

<!-- b001185 | furniture | pages [11] -->
m

<!-- b001186 | furniture | pages [11] -->
m

<!-- b001187 | furniture | pages [11] -->
m

<!-- b001188 | furniture | pages [11] -->
m

<!-- b001189 | furniture | pages [11] -->
m

<!-- b001190 | furniture | pages [11] -->
m

<!-- b001191 | furniture | pages [11] -->
m

<!-- b001192 | furniture | pages [11] -->
m

<!-- b001193 | furniture | pages [11] -->
m

<!-- b001194 | furniture | pages [11] -->
m

<!-- b001195 | furniture | pages [11] -->
m

<!-- b001196 | furniture | pages [11] -->
m

<!-- b001197 | furniture | pages [11] -->
m

<!-- b001198 | furniture | pages [11] -->
m

<!-- b001199 | furniture | pages [11] -->
m

<!-- b001200 | furniture | pages [11] -->
m

<!-- b001201 | furniture | pages [11] -->
m

<!-- b001202 | furniture | pages [11] -->
m

<!-- b001203 | furniture | pages [11] -->
m

<!-- b001204 | furniture | pages [11] -->
m

<!-- b001205 | furniture | pages [11] -->
m

<!-- b001206 | furniture | pages [11] -->
m

<!-- b001207 | furniture | pages [11] -->
m

<!-- b001208 | furniture | pages [11] -->
m

<!-- b001209 | furniture | pages [11] -->
m

<!-- b001210 | furniture | pages [11] -->
m

<!-- b001211 | furniture | pages [11] -->
m

<!-- b001212 | furniture | pages [11] -->
m

<!-- b001213 | furniture | pages [11] -->
m

<!-- b001214 | furniture | pages [11] -->
m

<!-- b001215 | furniture | pages [11] -->
m

<!-- b001216 | furniture | pages [11] -->
m

<!-- b001217 | furniture | pages [11] -->
m

<!-- b001218 | furniture | pages [11] -->
m

<!-- b001219 | furniture | pages [11] -->
m

<!-- b001220 | furniture | pages [11] -->
m

<!-- b001221 | furniture | pages [11] -->
m

<!-- b001222 | furniture | pages [11] -->
m

<!-- b001223 | furniture | pages [11] -->
m

<!-- b001224 | furniture | pages [11] -->
m

<!-- b001225 | furniture | pages [11] -->
m

<!-- b001226 | furniture | pages [11] -->
m

<!-- b001227 | furniture | pages [11] -->
m

<!-- b001228 | furniture | pages [11] -->
m

<!-- b001229 | furniture | pages [11] -->
m

<!-- b001230 | furniture | pages [11] -->
m

<!-- b001231 | furniture | pages [11] -->
m

<!-- b001232 | furniture | pages [11] -->
m

<!-- b001233 | furniture | pages [11] -->
m

<!-- b001234 | furniture | pages [11] -->
m

<!-- b001235 | furniture | pages [11] -->
m

<!-- b001236 | furniture | pages [11] -->
m

<!-- b001237 | furniture | pages [11] -->
m

<!-- b001238 | furniture | pages [11] -->
m

<!-- b001239 | furniture | pages [11] -->
m

<!-- b001240 | furniture | pages [11] -->
m

<!-- b001241 | furniture | pages [11] -->
m

<!-- b001242 | furniture | pages [11] -->
m

<!-- b001243 | furniture | pages [11] -->
m

<!-- b001244 | furniture | pages [11] -->
m

<!-- b001245 | furniture | pages [11] -->
m

<!-- b001246 | furniture | pages [11] -->
m

<!-- b001247 | furniture | pages [11] -->
m

<!-- b001248 | furniture | pages [11] -->
m

<!-- b001249 | furniture | pages [11] -->
m

<!-- b001250 | furniture | pages [11] -->
m

<!-- b001251 | furniture | pages [11] -->
m

<!-- b001252 | furniture | pages [11] -->
m

<!-- b001253 | furniture | pages [11] -->
m

<!-- b001254 | furniture | pages [11] -->
m

<!-- b001255 | furniture | pages [11] -->
m

<!-- b001256 | furniture | pages [11] -->
m

<!-- b001257 | furniture | pages [11] -->
m

<!-- b001258 | furniture | pages [11] -->
m

<!-- b001259 | furniture | pages [11] -->
m

<!-- b001260 | furniture | pages [11] -->
m

<!-- b001261 | furniture | pages [11] -->
m

<!-- b001262 | furniture | pages [11] -->
m

<!-- b001263 | furniture | pages [11] -->
m

<!-- b001264 | furniture | pages [11] -->
m

<!-- b001265 | furniture | pages [11] -->
m

<!-- b001266 | furniture | pages [11] -->
m

<!-- b001267 | furniture | pages [11] -->
m

<!-- b001268 | furniture | pages [11] -->
m

<!-- b001269 | furniture | pages [11] -->
m

<!-- b001270 | furniture | pages [11] -->
m

<!-- b001271 | furniture | pages [11] -->
m

<!-- b001272 | furniture | pages [11] -->
m

<!-- b001273 | furniture | pages [11] -->
m

<!-- b001274 | furniture | pages [11] -->
m

<!-- b001275 | furniture | pages [11] -->
m

<!-- b001276 | furniture | pages [11] -->
m

<!-- b001277 | furniture | pages [11] -->
m

<!-- b001278 | furniture | pages [11] -->
m

<!-- b001279 | furniture | pages [11] -->
m

<!-- b001280 | furniture | pages [11] -->
m

<!-- b001281 | furniture | pages [11] -->
m

<!-- b001282 | furniture | pages [11] -->
m

<!-- b001283 | furniture | pages [11] -->
m

<!-- b001284 | furniture | pages [11] -->
m

<!-- b001285 | furniture | pages [11] -->
m

<!-- b001286 | furniture | pages [11] -->
m

<!-- b001287 | furniture | pages [11] -->
m

<!-- b001288 | furniture | pages [11] -->
m

<!-- b001289 | furniture | pages [11] -->
m

<!-- b001290 | furniture | pages [11] -->
m

<!-- b001291 | furniture | pages [11] -->
m

<!-- b001292 | furniture | pages [11] -->
m

<!-- b001293 | furniture | pages [11] -->
m

<!-- b001294 | furniture | pages [11] -->
m

<!-- b001295 | furniture | pages [11] -->
m

<!-- b001296 | furniture | pages [11] -->
m

<!-- b001297 | furniture | pages [11] -->
m

<!-- b001298 | furniture | pages [11] -->
m

<!-- b001299 | furniture | pages [12] -->
Team # 2501869

<!-- b001300 | furniture | pages [12] -->
Page 12 of 25

<!-- b001302 | prose | pages [12] -->
5.3 2028 Los Angeles Olympics Medal Count Projections

<!-- b001303 | prose | pages [12] -->
The figure below shows the medal standings for all participating countries that are predicted to win at least one medal.

<!-- b001304 | prose | pages [12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001305 | caption | pages [12] -->
Figure 6 2028 Olympic Medal Predictions Gold/Silver/Bronze Distribution by Country

<!-- b001306 | prose | pages [12] -->
Based on the above prediction results, we have listed the top five countries with the highest increase and decrease in total medals, as follows.

<!-- b001307 | caption | pages [12] -->
Table 4 Top 5 Countries with the Highest Improve and Decline

<!-- b001308 | prose | pages [12] -->
Improve USA China India Brazil Japan

<!-- b001309 | prose | pages [12] -->
Magnitude 15 10 7 5 5

<!-- b001310 | prose | pages [12] -->
Decline France Russia Germany Great Britain Australia

<!-- b001311 | prose | pages [12] -->
Magnitude -8 -4 -4 -3 -2

<!-- b001312 | heading | pages [12] -->
5.4 Projecting First-Time Medal Winners and Probability Estimates

<!-- b001313 | prose | pages [12] -->
The prediction results show that a total of three countries will win their first medals at the 2028 Los Angeles Olympics, namely: Angola, Bangladesh and Cambodia. The probability of

<!-- b001314 | prose | pages [12, 13] -->
关注数学模型 each country winning their first medal is shown in the table below.

<!-- b001315 | furniture | pages [12] -->
2

<!-- b001316 | furniture | pages [12] -->
MATHmodels

<!-- b001317 | furniture | pages [12] -->
获取更多资讯

<!-- b001318 | furniture | pages [13] -->
Page 13 of 25

<!-- b001319 | furniture | pages [13] -->
Team # 2501869

<!-- b001321 | caption | pages [13] -->
Table 5 Projected First-Time Medal Winners and Probability

<!-- b001322 | prose | pages [13] -->
Country Angola Bangladesh Cambodia 49.23% 42.49% 46.67% Possibility

<!-- b001323 | heading | pages [13] -->
5.5 The Influence of Item Selection on the Number of Medals

<!-- b001324 | prose | pages [13] -->
The below table shows the mean values of the statistical results obtained by each country when Tobit and Hurdle were used.

<!-- b001325 | caption | pages [13] -->
Table 6 Results of Two Forecasting Models

<!-- b001326 | heading | pages [13] -->
Tobit Model

<!-- b001327 | prose | pages [13] -->
Hurdle Model Variables Coef Coef SD SD Constant 8.864*** 0.336* 2.02 0.1 Host country in 4 years 1.566*** 0.11 12.520*** 2.03 Host country t -4.760** 0.85 0.11 2.08 Host country 4 years ago 0.016* 0.897* 0.02 Athletes [0,10] 0 0.510* 5.126*** 0.23 0.67 Athletes [10,50] 0.87 0.989* 0.24 7.394*** Athletes [50,150] 1.559*** 9.314*** 0.27 1.15 150 athletes and more 3.42*** 3.725*** 0.12 4.57 Medals_PCA(t-4) 2.538*** 1.828** RCA 0.22 1.07 3.42*** 3.725*** 0.12 4.57 0.538** 1.828** 0.22 1.07 Num_Events 0.618** 1.719** 0.21 0.97 2.742*** 2.705*** 0.22 NAE 0.26 -3.408*** 0.25 gi,t 0.115*** 26.68*** 2 0.03 1.66 u 529 1232 Observations total 529 Observations noncensored Note: ***Significant at the 1 percent level; **5 percent level; *10 percent level.

<!-- b001328 | prose | pages [13] -->
The results show that both the number of events and NAE have a positive and significant effect, and this significance is common to all countries. The coefficient of RC A is large and the variance is large, which may indicate significant heterogeneity in the importance of different sports for different countries. At the same time, the host country has a positive impact in both the Tobit and Hurdle models, and in the Hurdle model, the coefficient of the host country is smaller than that of the Tobit. The explanation is that there is obvious multiple collinearity between the host country and other variables such as NAE and RCA, and these variables will dilute the significance of the host country, and Hurdle is more likely to capture this effect.

<!-- b001329 | furniture | pages [14] -->
Team # 2501869

<!-- b001330 | furniture | pages [14] -->
Page 14 of 25

<!-- b001331 | heading | pages [14] -->
5.5.1 Relationship Between Olympic Events and Medal Distribution

<!-- b001332 | prose | pages [14] -->
Initially, an effortwasmadetoconstructagraphrepresentingtherelationshipbetweenMeanNAE, Num_Events, and Total in historical data for China, the United States, Japan, and France. Subsequently, the Pearson correlation coefficients of these countries regarding the two covari- ates and Total were calculated. The graph of the relationship between Total and meanNAE and correlation coefficient tables are presented below.

<!-- b001333 | caption | pages [14] -->
Figure 7 Comparison of RCA, Num_Events and Total by Country

<!-- b001334 | caption | pages [14] -->
Table 7 Pearson Correlation Coefficient Tables

<!-- b001335 | prose | pages [14] -->
Mean SD

<!-- b001336 | prose | pages [14] -->
num_events 0.238 0.216 NAE 0.952 0.051

<!-- b001337 | prose | pages [14] -->
The findings revealed a robust linear relationship between MeanNAE and Total, with a concomitant small standard deviation, suggesting its universality. However, the significance of Num_Event is negligible, and this phenomenon exhibits substantial heterogeneity across different countries.

<!-- b001338 | prose | pages [14] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001339 | heading | pages [14] -->
5.5.2 Analysis of Key Sports and Their Importance for Different Countries

<!-- b001340 | prose | pages [14] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The RCA index is a quantitative metric that can be used to compare the relative popularity of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m different sports in different countries. As illustrated by the heatmap, Modern Pentathlon has m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m emerged as Egypt’s preeminent sport, a finding that aligns with its status as the nation’s sole gold m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m medalist and world record holder in this discipline. A similar observation can be made when examining the United States, another nation with a strong sporting reputation. The RCA index for the United States exceeds 1 in several sports, suggesting a comparable level of dominance in various sports. This finding is consistent with the notion that the United States possesses a diverse array of sports with similar levels of strength.

<!-- b001341 | prose | pages [14] -->
In order to ascertain the sports that are of the utmost importance to each nation, the present study utilizes Egypt and the United States as exemplars. The Tobit and Hurdle models are

<!-- b001342 | prose | pages [14, 15] -->
关注数学模型 employed to predict the total for the 2024 Summer Olympics, calculate the corresponding RC A and coefficient, use these as a benchmark to rank the sports, and extract the number of medals contributed by these sports. In essence, the sports displayed in the figure represent the most significant contributors to the overall medal count of the United States and Egypt, as evidenced by their substantial RCA and corresponding coefficient values.

<!-- b001343 | furniture | pages [14] -->
2

<!-- b001344 | furniture | pages [14] -->
MATHmodels

<!-- b001345 | furniture | pages [14] -->
获取更多资讯

<!-- b001346 | furniture | pages [15] -->
Page 15 of 25

<!-- b001347 | furniture | pages [15] -->
Team # 2501869

<!-- b001349 | prose | pages [15] -->
Athletics Modern Pentathlon 27 Fencing Swimming Artistic Gymnastics Weightlifting 9 Wrestling Shooting Fencing Skateboarding Cycling Track Sport Climbing 2 22 Tennis Archery 22 Rowing Volleyball 2 Sport Discipline Weightlifting 2 Basketball Canoe Sprint Water Polo Artistic Swimming Boxing Breaking Canoe Slalom Taekwondo Cycling BMX Freestyle Cycling Mountain Bike Surfing Diving Equestrian Football Golf Rugby Sevens Sailing 3x3 Basketball 10 15 20 25 30 35 5 Medal Count 1

<!-- b001350 | caption | pages [15] -->
Figure 8 Top Contributing Sports to Medal Counts: the United States and Egypt"

<!-- b001351 | heading | pages [15] -->
5.5.3 Impact of Host Country Event Selection on Performance

<!-- b001352 | prose | pages [15] -->
Based on historical data observations, there is a significant synergistic growth between the host country's RC A and NAE (as shown in the figure below).

<!-- b001353 | prose | pages [15, 16] -->
微信 This phenomenon may be attributed to two non-mutually exclusive mechanisms:

<!-- b001354 | furniture | pages [16] -->
Team # 2501869

<!-- b001355 | furniture | pages [16] -->
Page 16 of 25

<!-- b001356 | caption | pages [16] -->
Figure 9 NAE and RCA Indices of the Host Country

<!-- b001358 | prose | pages [16] -->
• Strategic project selection, wherein the host country utilizes the rules of the competition to incorporate temporary advantageous projects (such as niche unpopular projects) to artificially augment RCA through "institutional dividends".

<!-- b001359 | prose | pages [16] -->
• Systematic capacity enhancement. The long-term resource investment (e.g., athlete train- ing) brought about by hosting the event promotes the overall upgrading of sports strength, which in turn enhances NAE and RCA.

<!-- b001360 | prose | pages [16] -->
To quantify the independent impact of these mechanisms, this study employs a dual strategy of model complementarity and variable reconstruction. While the hurdle model has been demonstrated to more effectively capture the host effect, the Tobit model has been shown to be more adept at addressing sports with weaker nations (i.e., medal count less than or equal to 0). This is due to the truncated regression characteristics of the Tobit model, which are more conducive to the "zero value accumulation + low value continuity" distribution. Consequently, the Tobit model can more sensitively detect the marginal effect of the host country surpassing the zero medal threshold through RCA_add and NAE. Consequently, it is imperative to construct two models based on Tobit and Hurdle through variable refinement.

<!-- b001361 | prose | pages [16] -->
• Convert continuous NAE to a three-category variable (low/medium/high) to identify nonlinear threshold effects accumulated empirically, and calculate the average RCA of traditional events that have existed stably in previous events to reflect the country’s long-term competitiveness.

<!-- b001362 | prose | pages [16] -->
• Separate the RCA of permanent events and new events. For new event RCA_add: extract the historical maximum (max(RCA)) of the RCA of temporary events added by the host country to capture the peak effect of its strategic selection of events. maximum value (max(RCA)) to capture the peak effect of its strategic selection of events.

<!-- b001363 | prose | pages [16, 17] -->
关注数学模型 The ensuing results are presented in the subsequent table.

<!-- b001364 | furniture | pages [16] -->
2

<!-- b001365 | furniture | pages [16] -->
MATHmodels

<!-- b001366 | furniture | pages [16] -->
获取更多资讯

<!-- b001367 | furniture | pages [17] -->
Team # 2501869

<!-- b001368 | furniture | pages [17] -->
Page 17 of 25

<!-- b001370 | caption | pages [17] -->
Table 8 Results of Four Explanatory Models

<!-- b001371 | prose | pages [17] -->
Model (1)–Hurdle Model (1)–Tobit Model (2)–Hurdle Model (2)–Tobit Variables Coef SD Coef SD Coef SD Coef SD

<!-- b001372 | prose | pages [17] -->
Host country 0.136* 0.21 5.864*** 0.12 0.236* 0.12 5.864*** 0.22 in 4 years Host country 1.354*** 0.41 5.520*** 0.23 1.546*** 0.21 5.520*** 0.03 t 微信公众号：数学模型 Host country 1.085*** 0.21 4.145** 0.18 0.879** 0.11 4.547** 0.12 4 years ago Athletes 0.016* 0 0.745* 0.22 0.016* 0 0.789* 0.22 [0,10] Athletes 0.241* 0.34 0.826*** 0.88 0.510* 0.12 0.726*** 0.57 [10,50] Athletes 0.789** 0.54 0.924*** 0.65 0.989** 0.23 0.954*** 0.65 [50,150] 150 athletes 0.978*** 0.25 9.314*** 1.15 0.834*** 0.12 0.614*** 1.15 and more 微信号：MATHmodels Medals_PCA(t- 3.725*** 0.28 3.42*** 4.57 3.702*** 0.23 3.42*** 4.47 4) RCA 1.548*** 0.32 1.828** 1.42 2.538*** 0.24 1.828** 1.17 RCA_usual 0.538* 0.22 0.778** 0.92 RCA_add 2.618*** 0.41 1.994** 0.93 NAE 2.911*** 0.122 2.414*** 0.48 NAE [0,20] 1.745*** 0.24 2.948** 1.15 NAE [20,50] 1.857*** 1.71 1.011** 0.75 NAE 50 and 1.912*** 0.92 1.112*** 0.36 more Num_Events 0.575** 0.24 1.148** 1.72 0.538* 0.22 1.178** 0.92 Num_sports 0.487** 1.69 1.572** 1.07 0.618** 0.41 0.994** 0.93 gi,t -3.408*** 0.75 — — -3.408*** 0.235 — — σ2 0.350*** 0.05 26.68*** 23.67 0.334*** 0.03 51.907*** 8.36 u Observations 554 — 1289 — 554 — 1289 — total Observations 554 554 noncensored Note: ***Significant at the 1 percent level; **5 percent level; *10 percent level..

<!-- b001373 | prose | pages [17, 18] -->
According to the results in the table, strategically adding temporary dominant events (RCAadd) is the core driver of host countries’ medal gains. In Model 2, the coefficient of RCAadd is significantly positive (2.618, 1.994), indicating that host countries can significantly increase their medal gains in the short term by adding new events with the best historical per- formance (such as karate at the Tokyo Olympics) and focusing their resources on these events. In contrast, the impact of long-term competitiveness (RCAusual) is relatively limited, and the significance is not prominent in Model 1 and Model 2. Secondly, for Tobit, the number and type of events (Num_Events, Num_Sports) are significantly positive (Num_Sports coefficient 1.572 in Model 1), indicating that adding sub-events or new sports types can create more medal opportunities for weak sports countries. In addition, Model 1 shows that experience accumu- lation (NAE categorical variable) and breaking through the zero medal threshold as a host country for weak sports countries are particularly critical through the addition of events (NAE low group coefficient 2.948*); while the host effect (Host country t coefficient 5.520***) is stronger in the Tobit model, which confirms its marginal effect on the breakthrough of medals for weak countries. In summary, the host country achieves structural growth in the number of medals through a three-pronged approach to event selection: “short-term focus on strengths + expansion of event scale + preferential treatment of home resources”. This mechanism is of even greater decisive significance for countries with low competitiveness.

<!-- b001374 | furniture | pages [18] -->
Team # 2501869

<!-- b001375 | furniture | pages [18] -->
Page 18 of 25

<!-- b001377 | heading | pages [18] -->
6 The Great Coach Effect: A Strategy Optimization Study

<!-- b001378 | prose | pages [18] -->
Based on Bayesian Change-Point Detection and Causal In- ference Models

<!-- b001379 | heading | pages [18] -->
6.1 Discovery of Great Coach Effect Based on Bayesian Change-Point

<!-- b001380 | prose | pages [18] -->
Detection

<!-- b001381 | prose | pages [18] -->
When there is a significant change in the number of medals won by a country in a certain event in a certain edition, e.g. winning at least one medal in a certain edition but failing to win a medal in several consecutive Olympic Games, or a significant increase in the number of medals won but also winning gold medals in previous editions. We believe that such significant changes are the result of the “great coach effect”. The reason for this idea is that a sudden breakthrough after a long period of downturn, or a significant increase in strength in a certain edition of the Games, may be related to an outstanding coach, even if the country had previously had a certain level of sporting strength. Such obvious turning points can be identified using a Bayesian change-point detection.

<!-- b001382 | caption | pages [18] -->
Figure 10 Two Types of Change-Point

<!-- b001383 | heading | pages [18] -->
6.1.1 Data Handling

<!-- b001384 | prose | pages [18] -->
Bayesian change-point detection has a wide range of applications in fields such as medicine, such as real-time detection of sudden changes in a patient’s heart rate. Or the time point at which significant changes occur in historical data. For medal data, however, if bronze, gold, and silver medals are respectively set to 1, 2, and 3, the fluctuations in a unit of time are too

<!-- b001385 | prose | pages [18, 19] -->
关注数学模型 large, causing the model to identify a large number of change points. Therefore, we process the medal data to make it more stable within a unit of time. The calculation uses a sliding window method, and the formula is as follows:

<!-- b001386 | furniture | pages [18] -->
2

<!-- b001387 | furniture | pages [18] -->
MATHmodels

<!-- b001388 | furniture | pages [18] -->
获取更多资讯

<!-- b001389 | furniture | pages [19] -->
Team # 2501869

<!-- b001390 | furniture | pages [19] -->
Page 19 of 25

<!-- b001392 | prose | pages [19] -->
  a   1   · · b NGold NSilver NBronze St = 1 + (9)  NTotal c

<!-- b001393 | prose | pages [19] -->
K X St−4,ie−i Scoret = (10) i=0 微信公众号：数学模型 Before and after data processing:

<!-- b001394 | prose | pages [19] -->
微信号：MATHmodels

<!-- b001395 | caption | pages [19] -->
Figure 11 Two Types of Change-Point

<!-- b001396 | heading | pages [19] -->
6.1.2 Bayesian Change-point Detection

<!-- b001397 | prose | pages [19] -->
The fundamental principle of Bayesian change-point detection involves the segmentation of data into distinct components, under the assumption that each segment follows a specific probability distribution (e.g., the normal distribution). This approach entails the estimation of the location and number of change points through the application of Bayesian inference. This method integrates the observed data, the parameter prior, and the change point prior through a joint posterior distribution, leveraging marginal likelihood to streamline the calculation. This facilitates the inference of the most probable change point configuration.

<!-- b001398 | heading | pages [19] -->
6.1.3 Evidence of Coaching Effect in the United States

<!-- b001399 | prose | pages [19] -->
By bringing in the data of the US volleyball team and the gymnastics team and using Bayesian Change-point Detection, we found that it detected the change point, i.e., great coaching effect, as shown in the table below.

<!-- b001400 | caption | pages [19] -->
Table 9 Evidence of Great Coaching Effect for the United States

<!-- b001401 | prose | pages [19] -->
Sports Change- Posterior Data Variance Confidence point Probability Segment Interval (95%)

<!-- b001402 | prose | pages [19] -->
Volleyball 2008 0.95 2004-2008 1.3 [4.8, 5.6] Gymnastics 1984 0.87 1980-1984 2.1 [7.3, 8.3]

<!-- b001403 | furniture | pages [20] -->
Page 20 of 25

<!-- b001404 | furniture | pages [20] -->
Team # 2501869

<!-- b001405 | heading | pages [20] -->
6.2 Quantitative Evaluation of Great Coaching Effect on Medal Counts

<!-- b001406 | prose | pages [20] -->
Regression models are an important tool in statistics for estimating the relationship between variables. They are significantly superior to machine learning models such as XGBoost and random forests in terms of interpretability (cited literature). However, when using regression models to analyze the contribution of great coaches to the number of medals, it is impossible to avoid the estimation bias caused by endogeneity (i.e., the influence of the mutual relationship between variables, missing variables, etc.), which makes it impossible to accurately identify the true influence of coaches. Therefore, here we must abandon general parameter estimation methods (such as OLS, DID, and IV) and develop a parameter estimation method that eliminates endogeneity and focuses on the strong causal effect of coaches and medals, namely two-stage least squares(2SLS).

<!-- b001407 | prose | pages [20] -->
6.2.1 Regression Model Using 2SLS

<!-- b001408 | prose | pages [20] -->
Step 1: Regress Endogenous Variable D Using Instrumental Variable Scoret

<!-- b001409 | prose | pages [20] -->
The endogenous variable D indicates whether or not the coach is great. If D = 1, it indicates that the coach has a great effect; otherwise, D = 0. The expression that defines D is:

<!-- b001410 | prose | pages [20] -->
D = α0 + ∂1Score + α2RCA + α3Num_Events + α4Num_Athlete + α5NAE + m (11)

<!-- b001411 | prose | pages [20] -->
where Score is the instrumental variable strongly correlated and satisfying exogeneity (not directly affecting the existence of a great coach). The remaining explanatory variables are exogenous variables.

<!-- b001412 | prose | pages [20] -->
Step 2: Regress the Number of Medals N Using the Predicted Value D

<!-- b001413 | prose | pages [20] -->
The number of medals N can be expressed as

<!-- b001414 | prose | pages [20] -->
N = β0 + β1D + β2RCA + β3Num_Events + β4Num_Athlete + β5NAE + n (12)

<!-- b001415 | prose | pages [20] -->
where N = [Ngold, Nsilver, NBronze]T, β0, β1, β2, β3, β4, β5 ∈ R3 are coefficient.

<!-- b001416 | prose | pages [20] -->
If β1 is positive, the three components of β1 represent the contributions of great coaching effect to the gold, silver and bronze medals, respectively.

<!-- b001417 | prose | pages [20] -->
6.2.2 Model Validation

<!-- b001418 | prose | pages [20] -->
We use the United States as an example and use historical data from 1960 to 2024. First, Bayesian change-point detection is used for each sport to statistically determine the possible event of the great coaching effect. Then, MLE regression is performed on each sport using 2SLS and OLS in turn to statistically determine the impact of 2SLS and OLS on the number of medals won by great coaches for each event and compare the results with the actual values, as shown in the figure.

<!-- b001419 | prose | pages [20, 21] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b001420 | furniture | pages [20] -->
获取更多资讯

<!-- b001421 | furniture | pages [21] -->
Team # 2501869

<!-- b001422 | furniture | pages [21] -->
Page 21 of 25

<!-- b001424 | caption | pages [21] -->
Figure 12 Comparison of SLS, OLS Models vs Real Data

<!-- b001425 | prose | pages [21] -->
Both 2SLS and OLS are explanatory of the impact of great coaches on the number of medals, but 2SLS is significantly better than OLS in terms of explanatory effect, and the problem of endogeneity is better solved.

<!-- b001426 | heading | pages [21] -->
6.3 Targeted Coaching Investments for Three Nations

<!-- b001427 | prose | pages [21] -->
The statistical results show that the United States, the United Kingdom, and France can obtain marginal benefits through strategic investment in coaches. The expected increase in the number of medals for each country after the introduction of coaches is shown in the figure below.

<!-- b001428 | caption | pages [21] -->
Table 10 The Targeted Coaching Investments and Predicted Improvement Magnitude in the

<!-- b001429 | prose | pages [21] -->
United States, the Great Britain, and France

<!-- b001430 | prose | pages [21] -->
The United States Magnitude Great Britain Magnitude France Magnitude

<!-- b001431 | prose | pages [21] -->
Wrestling 2 Wrestling 1 Table tennis 1 Rowing 1 Canoeing 2 Badminton 1 Judo 1 Judo 1 Athletics 1 Archery 1 Shooting 1 Gymnastics 2 Triathlon 2 Weightlifting 1 Rowing 1

<!-- b001432 | prose | pages [21] -->
The above strategy is based on two core logics: first, selecting projects with outstanding marginal benefits with the intervention of existing coaches to achieve medal growth at minimal cost; second, targeting weaknesses in the international competitive landscape (e.g., table tennis is dominated by Asia) and filling technical gaps through cross-border coach cooperation. In the long term, such investment can improveshort-term results and build sustainablecompetitiveness, especially in Olympic events with a highly concentrated distribution of medals.

<!-- b001433 | prose | pages [21] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001434 | furniture | pages [21] -->
m

<!-- b001435 | furniture | pages [21] -->
m

<!-- b001436 | furniture | pages [21] -->
m

<!-- b001437 | furniture | pages [21] -->
m

<!-- b001438 | furniture | pages [21] -->
m

<!-- b001439 | furniture | pages [21] -->
m

<!-- b001440 | furniture | pages [21] -->
m

<!-- b001441 | furniture | pages [21] -->
m

<!-- b001442 | furniture | pages [21] -->
m

<!-- b001443 | furniture | pages [21] -->
m

<!-- b001444 | furniture | pages [21] -->
m

<!-- b001445 | furniture | pages [21] -->
m

<!-- b001446 | furniture | pages [21] -->
m

<!-- b001447 | furniture | pages [21] -->
m

<!-- b001448 | furniture | pages [21] -->
m

<!-- b001449 | furniture | pages [21] -->
m

<!-- b001450 | furniture | pages [21] -->
m

<!-- b001451 | furniture | pages [21] -->
m

<!-- b001452 | furniture | pages [21] -->
m

<!-- b001453 | furniture | pages [21] -->
m

<!-- b001454 | furniture | pages [21] -->
m

<!-- b001455 | furniture | pages [21] -->
m

<!-- b001456 | furniture | pages [21] -->
m

<!-- b001457 | furniture | pages [21] -->
m

<!-- b001458 | furniture | pages [21] -->
m

<!-- b001459 | furniture | pages [21] -->
m

<!-- b001460 | furniture | pages [21] -->
m

<!-- b001461 | furniture | pages [21] -->
m

<!-- b001462 | furniture | pages [21] -->
m

<!-- b001463 | furniture | pages [21] -->
m

<!-- b001464 | furniture | pages [21] -->
m

<!-- b001465 | furniture | pages [21] -->
m

<!-- b001466 | furniture | pages [21] -->
m

<!-- b001467 | furniture | pages [21] -->
m

<!-- b001468 | furniture | pages [21] -->
m

<!-- b001469 | furniture | pages [21] -->
m

<!-- b001470 | furniture | pages [21] -->
m

<!-- b001471 | furniture | pages [21] -->
m

<!-- b001472 | furniture | pages [21] -->
m

<!-- b001473 | furniture | pages [21] -->
m

<!-- b001474 | furniture | pages [21] -->
m

<!-- b001475 | furniture | pages [21] -->
m

<!-- b001476 | furniture | pages [21] -->
m

<!-- b001477 | furniture | pages [21] -->
m

<!-- b001478 | furniture | pages [21] -->
m

<!-- b001479 | furniture | pages [21] -->
m

<!-- b001480 | furniture | pages [21] -->
m

<!-- b001481 | furniture | pages [21] -->
m

<!-- b001482 | furniture | pages [21] -->
m

<!-- b001483 | furniture | pages [21] -->
m

<!-- b001484 | furniture | pages [21] -->
m

<!-- b001485 | furniture | pages [21] -->
m

<!-- b001486 | furniture | pages [21] -->
m

<!-- b001487 | furniture | pages [21] -->
m

<!-- b001488 | furniture | pages [21] -->
m

<!-- b001489 | furniture | pages [21] -->
m

<!-- b001490 | furniture | pages [21] -->
m

<!-- b001491 | furniture | pages [21] -->
m

<!-- b001492 | furniture | pages [21] -->
m

<!-- b001493 | furniture | pages [21] -->
m

<!-- b001494 | furniture | pages [21] -->
m

<!-- b001495 | furniture | pages [21] -->
m

<!-- b001496 | furniture | pages [21] -->
m

<!-- b001497 | furniture | pages [21] -->
m

<!-- b001498 | furniture | pages [21] -->
m

<!-- b001499 | furniture | pages [21] -->
m

<!-- b001500 | furniture | pages [21] -->
m

<!-- b001501 | furniture | pages [21] -->
m

<!-- b001502 | furniture | pages [21] -->
m

<!-- b001503 | furniture | pages [21] -->
m

<!-- b001504 | furniture | pages [21] -->
m

<!-- b001505 | furniture | pages [21] -->
m

<!-- b001506 | furniture | pages [21] -->
m

<!-- b001507 | furniture | pages [21] -->
m

<!-- b001508 | furniture | pages [21] -->
m

<!-- b001509 | furniture | pages [21] -->
m

<!-- b001510 | furniture | pages [21] -->
m

<!-- b001511 | furniture | pages [21] -->
m

<!-- b001512 | furniture | pages [21] -->
m

<!-- b001513 | furniture | pages [21] -->
m

<!-- b001514 | furniture | pages [21] -->
m

<!-- b001515 | furniture | pages [21] -->
m

<!-- b001516 | furniture | pages [21] -->
m

<!-- b001517 | furniture | pages [21] -->
m

<!-- b001518 | furniture | pages [21] -->
m

<!-- b001519 | furniture | pages [21] -->
m

<!-- b001520 | furniture | pages [21] -->
m

<!-- b001521 | furniture | pages [21] -->
m

<!-- b001522 | furniture | pages [21] -->
m

<!-- b001523 | furniture | pages [21] -->
m

<!-- b001524 | furniture | pages [21] -->
m

<!-- b001525 | furniture | pages [21] -->
m

<!-- b001526 | furniture | pages [21] -->
m

<!-- b001527 | furniture | pages [21] -->
m

<!-- b001528 | furniture | pages [21] -->
m

<!-- b001529 | furniture | pages [21] -->
m

<!-- b001530 | furniture | pages [21] -->
m

<!-- b001531 | furniture | pages [21] -->
m

<!-- b001532 | furniture | pages [21] -->
m

<!-- b001533 | furniture | pages [21] -->
m

<!-- b001534 | furniture | pages [21] -->
m

<!-- b001535 | furniture | pages [21] -->
m

<!-- b001536 | furniture | pages [21] -->
m

<!-- b001537 | furniture | pages [21] -->
m

<!-- b001538 | furniture | pages [21] -->
m

<!-- b001539 | furniture | pages [21] -->
m

<!-- b001540 | furniture | pages [21] -->
m

<!-- b001541 | furniture | pages [21] -->
m

<!-- b001542 | furniture | pages [21] -->
m

<!-- b001543 | furniture | pages [21] -->
m

<!-- b001544 | furniture | pages [21] -->
m

<!-- b001545 | furniture | pages [21] -->
m

<!-- b001546 | furniture | pages [21] -->
m

<!-- b001547 | furniture | pages [21] -->
m

<!-- b001548 | furniture | pages [21] -->
m

<!-- b001549 | furniture | pages [21] -->
m

<!-- b001550 | furniture | pages [21] -->
m

<!-- b001551 | furniture | pages [21] -->
m

<!-- b001552 | furniture | pages [21] -->
m

<!-- b001553 | furniture | pages [21] -->
m

<!-- b001554 | furniture | pages [21] -->
m

<!-- b001555 | furniture | pages [21] -->
m

<!-- b001556 | furniture | pages [21] -->
m

<!-- b001557 | furniture | pages [21] -->
m

<!-- b001558 | furniture | pages [21] -->
m

<!-- b001559 | furniture | pages [21] -->
m

<!-- b001560 | furniture | pages [21] -->
m

<!-- b001561 | furniture | pages [21] -->
m

<!-- b001562 | furniture | pages [21] -->
m

<!-- b001563 | furniture | pages [21] -->
m

<!-- b001564 | furniture | pages [21] -->
m

<!-- b001565 | furniture | pages [21] -->
m

<!-- b001566 | furniture | pages [21] -->
m

<!-- b001567 | furniture | pages [21] -->
m

<!-- b001568 | furniture | pages [21] -->
m

<!-- b001569 | furniture | pages [21] -->
m

<!-- b001570 | furniture | pages [21] -->
m

<!-- b001571 | furniture | pages [21] -->
m

<!-- b001572 | furniture | pages [21] -->
m

<!-- b001573 | furniture | pages [21] -->
m

<!-- b001574 | furniture | pages [21] -->
m

<!-- b001575 | furniture | pages [21] -->
m

<!-- b001576 | furniture | pages [21] -->
m

<!-- b001577 | furniture | pages [21] -->
m

<!-- b001578 | furniture | pages [21] -->
m

<!-- b001579 | furniture | pages [21] -->
m

<!-- b001580 | furniture | pages [21] -->
m

<!-- b001581 | furniture | pages [21] -->
m

<!-- b001582 | furniture | pages [21] -->
m

<!-- b001583 | furniture | pages [21] -->
m

<!-- b001584 | furniture | pages [21] -->
m

<!-- b001585 | furniture | pages [21] -->
m

<!-- b001586 | furniture | pages [21] -->
m

<!-- b001587 | furniture | pages [21] -->
m

<!-- b001588 | furniture | pages [21] -->
m

<!-- b001589 | furniture | pages [21] -->
m

<!-- b001590 | furniture | pages [21] -->
m

<!-- b001591 | furniture | pages [21] -->
m

<!-- b001592 | furniture | pages [21] -->
m

<!-- b001593 | furniture | pages [21] -->
m

<!-- b001594 | furniture | pages [21] -->
m

<!-- b001595 | furniture | pages [21] -->
m

<!-- b001596 | furniture | pages [21] -->
m

<!-- b001597 | furniture | pages [21] -->
m

<!-- b001598 | furniture | pages [21] -->
m

<!-- b001599 | furniture | pages [21] -->
m

<!-- b001600 | furniture | pages [21] -->
m

<!-- b001601 | furniture | pages [21] -->
m

<!-- b001602 | furniture | pages [21] -->
m

<!-- b001603 | furniture | pages [21] -->
m

<!-- b001604 | furniture | pages [21] -->
m

<!-- b001605 | furniture | pages [21] -->
m

<!-- b001606 | furniture | pages [21] -->
m

<!-- b001607 | furniture | pages [21] -->
m

<!-- b001608 | furniture | pages [21] -->
m

<!-- b001609 | furniture | pages [21] -->
m

<!-- b001610 | furniture | pages [21] -->
m

<!-- b001611 | furniture | pages [21] -->
m

<!-- b001612 | furniture | pages [21] -->
m

<!-- b001613 | furniture | pages [21] -->
m

<!-- b001614 | furniture | pages [21] -->
m

<!-- b001615 | furniture | pages [21] -->
m

<!-- b001616 | furniture | pages [21] -->
m

<!-- b001617 | furniture | pages [21] -->
m

<!-- b001618 | furniture | pages [21] -->
m

<!-- b001619 | furniture | pages [21] -->
m

<!-- b001620 | furniture | pages [21] -->
m

<!-- b001621 | furniture | pages [21] -->
m

<!-- b001622 | furniture | pages [21] -->
m

<!-- b001623 | furniture | pages [21] -->
m

<!-- b001624 | furniture | pages [21] -->
m

<!-- b001625 | furniture | pages [21] -->
m

<!-- b001626 | furniture | pages [21] -->
m

<!-- b001627 | furniture | pages [21] -->
m

<!-- b001628 | furniture | pages [21] -->
m

<!-- b001629 | furniture | pages [21] -->
m

<!-- b001630 | furniture | pages [21] -->
m

<!-- b001631 | furniture | pages [21] -->
m

<!-- b001632 | furniture | pages [21] -->
m

<!-- b001633 | furniture | pages [21] -->
m

<!-- b001634 | furniture | pages [21] -->
m

<!-- b001635 | furniture | pages [21] -->
m

<!-- b001636 | furniture | pages [21] -->
m

<!-- b001637 | furniture | pages [21] -->
m

<!-- b001638 | furniture | pages [21] -->
m

<!-- b001639 | furniture | pages [21] -->
m

<!-- b001640 | furniture | pages [21] -->
m

<!-- b001641 | furniture | pages [21] -->
m

<!-- b001642 | furniture | pages [21] -->
m

<!-- b001643 | furniture | pages [21] -->
m

<!-- b001644 | furniture | pages [21] -->
m

<!-- b001645 | furniture | pages [21] -->
m

<!-- b001646 | furniture | pages [21] -->
m

<!-- b001647 | furniture | pages [21] -->
m

<!-- b001648 | furniture | pages [21] -->
m

<!-- b001649 | furniture | pages [21] -->
m

<!-- b001650 | furniture | pages [21] -->
m

<!-- b001651 | furniture | pages [21] -->
m

<!-- b001652 | furniture | pages [21] -->
m

<!-- b001653 | furniture | pages [21] -->
m

<!-- b001654 | furniture | pages [21] -->
m

<!-- b001655 | furniture | pages [21] -->
m

<!-- b001656 | furniture | pages [21] -->
m

<!-- b001657 | furniture | pages [21] -->
m

<!-- b001658 | furniture | pages [21] -->
m

<!-- b001659 | furniture | pages [21] -->
m

<!-- b001660 | furniture | pages [21] -->
m

<!-- b001661 | furniture | pages [21] -->
m

<!-- b001662 | furniture | pages [21] -->
m

<!-- b001663 | furniture | pages [21] -->
m

<!-- b001664 | furniture | pages [21] -->
m

<!-- b001665 | furniture | pages [21] -->
m

<!-- b001666 | furniture | pages [21] -->
m

<!-- b001667 | furniture | pages [21] -->
m

<!-- b001668 | furniture | pages [21] -->
m

<!-- b001669 | furniture | pages [21] -->
m

<!-- b001670 | furniture | pages [21] -->
m

<!-- b001671 | furniture | pages [21] -->
m

<!-- b001672 | furniture | pages [21] -->
m

<!-- b001673 | furniture | pages [21] -->
m

<!-- b001674 | furniture | pages [21] -->
m

<!-- b001675 | furniture | pages [21] -->
m

<!-- b001676 | furniture | pages [21] -->
m

<!-- b001677 | furniture | pages [21] -->
m

<!-- b001678 | furniture | pages [21] -->
m

<!-- b001679 | furniture | pages [21] -->
m

<!-- b001680 | furniture | pages [21] -->
m

<!-- b001681 | furniture | pages [21] -->
m

<!-- b001682 | furniture | pages [21] -->
m

<!-- b001683 | furniture | pages [21] -->
m

<!-- b001684 | furniture | pages [21] -->
m

<!-- b001685 | furniture | pages [21] -->
m

<!-- b001686 | furniture | pages [21] -->
m

<!-- b001687 | furniture | pages [21] -->
m

<!-- b001688 | furniture | pages [21] -->
m

<!-- b001689 | furniture | pages [21] -->
m

<!-- b001690 | furniture | pages [21] -->
m

<!-- b001691 | furniture | pages [21] -->
m

<!-- b001692 | furniture | pages [21] -->
m

<!-- b001693 | furniture | pages [21] -->
m

<!-- b001694 | furniture | pages [21] -->
m

<!-- b001695 | furniture | pages [21] -->
m

<!-- b001696 | furniture | pages [21] -->
m

<!-- b001697 | furniture | pages [21] -->
m

<!-- b001698 | furniture | pages [21] -->
m

<!-- b001699 | furniture | pages [21] -->
m

<!-- b001700 | furniture | pages [21] -->
m

<!-- b001701 | furniture | pages [21] -->
m

<!-- b001702 | furniture | pages [21] -->
m

<!-- b001703 | furniture | pages [21] -->
m

<!-- b001704 | furniture | pages [21] -->
m

<!-- b001705 | furniture | pages [21] -->
m

<!-- b001706 | furniture | pages [21] -->
m

<!-- b001707 | furniture | pages [21] -->
m

<!-- b001708 | furniture | pages [21] -->
m

<!-- b001709 | furniture | pages [21] -->
m

<!-- b001710 | furniture | pages [21] -->
m

<!-- b001711 | furniture | pages [21] -->
m

<!-- b001712 | furniture | pages [21] -->
m

<!-- b001713 | furniture | pages [21] -->
m

<!-- b001714 | furniture | pages [21] -->
m

<!-- b001715 | furniture | pages [21] -->
m

<!-- b001716 | furniture | pages [21] -->
m

<!-- b001717 | furniture | pages [21] -->
m

<!-- b001718 | furniture | pages [21] -->
m

<!-- b001719 | furniture | pages [21] -->
m

<!-- b001720 | furniture | pages [21] -->
m

<!-- b001721 | furniture | pages [21] -->
m

<!-- b001722 | furniture | pages [21] -->
m

<!-- b001723 | furniture | pages [21] -->
m

<!-- b001724 | furniture | pages [21] -->
m

<!-- b001725 | furniture | pages [21] -->
m

<!-- b001726 | furniture | pages [21] -->
m

<!-- b001727 | furniture | pages [21] -->
m

<!-- b001728 | furniture | pages [21] -->
m

<!-- b001729 | furniture | pages [21] -->
m

<!-- b001730 | furniture | pages [21] -->
m

<!-- b001731 | furniture | pages [21] -->
m

<!-- b001732 | furniture | pages [21] -->
m

<!-- b001733 | furniture | pages [21] -->
m

<!-- b001734 | furniture | pages [21] -->
m

<!-- b001735 | furniture | pages [21] -->
m

<!-- b001736 | furniture | pages [21] -->
m

<!-- b001737 | furniture | pages [21] -->
m

<!-- b001738 | furniture | pages [21] -->
m

<!-- b001739 | furniture | pages [21] -->
m

<!-- b001740 | furniture | pages [21] -->
m

<!-- b001741 | furniture | pages [21] -->
m

<!-- b001742 | furniture | pages [21] -->
m

<!-- b001743 | furniture | pages [21] -->
m

<!-- b001744 | furniture | pages [21] -->
m

<!-- b001745 | furniture | pages [21] -->
m

<!-- b001746 | furniture | pages [21] -->
m

<!-- b001747 | furniture | pages [21] -->
m

<!-- b001748 | furniture | pages [21] -->
m

<!-- b001749 | furniture | pages [21] -->
m

<!-- b001750 | furniture | pages [21] -->
m

<!-- b001751 | furniture | pages [21] -->
m

<!-- b001752 | furniture | pages [21] -->
m

<!-- b001753 | furniture | pages [21] -->
m

<!-- b001754 | furniture | pages [21] -->
m

<!-- b001755 | furniture | pages [21] -->
m

<!-- b001756 | furniture | pages [21] -->
m

<!-- b001757 | furniture | pages [21] -->
m

<!-- b001758 | furniture | pages [22] -->
Team # 2501869

<!-- b001759 | furniture | pages [22] -->
Page 22 of 25

<!-- b001760 | heading | pages [22] -->
7 Insights: Strategic Resource Allocation and Path Depen-

<!-- b001761 | prose | pages [22] -->
dency in Olympic Medal Performance

<!-- b001762 | prose | pages [22] -->
For question 3, we continue the analysis of questions 1 and 2, and use Bayesian variable point detection to label the possible great coaching effects of various sports in each country in previous Olympic Games, and add them as explanatory variables to the Hurdle and Tobit models. At the same time, due to the self-reinforcing mechanism of medal dynamics, we treat the explanatory variables in the same way (i.e., (further explaining the lagged terms), and then regress them. The results are shown in the table below.

<!-- b001763 | caption | pages [22] -->
Table 11 Results of Explanatory Models

<!-- b001764 | prose | pages [22] -->
Hurdle Model Tobit Model Variables Coef SD Coef SD

<!-- b001765 | prose | pages [22] -->
Host country t 1.354*** 0.41 5.520*** 0.23 Host country 4 years ago 1.085*** 0.21 4.145*** 0.18 Athletes [150+] 0.978*** 0.25 2.314*** 1.15 Medals_PCA 1.548*** 0.32 1.828*** 1.42 Num_Events vs. Num_Sports 0.575** vs. 0.487** 0.19 1.148*** vs. 1.572*** 1.03

<!-- b001766 | prose | pages [22] -->
Note: Only display the variables to be analyzed to interpret the coefficients; ***Significant at the 1 percent level;

<!-- b001767 | prose | pages [22] -->
**5 percent level; *10 percent level.

<!-- b001768 | heading | pages [22] -->
7.1 Dynamic Attenuation of the Host Country Effect and Resource Re-

<!-- b001769 | prose | pages [22] -->
distribution

<!-- b001770 | prose | pages [22] -->
From a temporal perspective, in the short term, the coefficient of host country t is 1.354* (Hurdle model), indicating that the advantage of the host country is most significant during the current Olympic Games. In the long term, the coefficient of host country 4 years ago is 1.085* (Hurdle model), indicating that the host country effect still exists 4 years later, but the strength has decreased by about 20%.

<!-- b001771 | prose | pages [22] -->
Policy implications:

<!-- b001772 | prose | pages [22] -->
• The host country needs to transform the infrastructure into a long-term training base within 2-4 years after the event to avoid idle resources.

<!-- b001773 | prose | pages [22] -->
• Non-host countries can target the “post-Olympic trough period” of previous host countries and obtain their surplus resources (such as venue leasing and coach exchanges) through cooperation.

<!-- b001774 | heading | pages [22] -->
7.2 The “Double-Eged Sword Effect” of the Number of Events and Sports

<!-- b001775 | prose | pages [22] -->
The coefficient of the Num_Events is 0.575* (Hurdle model)**, which shows that increas- ing the number of events can improve medal opportunities. However, the coefficient of the Num_Sports is only 0.487* (Hurdle model)**, indicating that excessive diversification may dilute resources.

<!-- b001776 | prose | pages [22] -->
Policy implications: National Olympic committees need to balance “breadth vs. depth”.

<!-- b001777 | prose | pages [22, 23] -->
关注数学模型 • Small countries: choose 3-5 high-potential sports to avoid fighting on multiple fronts.

<!-- b001778 | furniture | pages [22] -->
2

<!-- b001779 | furniture | pages [22] -->
MATHmodels

<!-- b001780 | furniture | pages [22] -->
获取更多资讯

<!-- b001781 | furniture | pages [23] -->
Team # 2501869

<!-- b001782 | furniture | pages [23] -->
Page 23 of 25

<!-- b001784 | prose | pages [23] -->
• Large countries: leverage the advantages of multiple sports, but need to establish a “core- peripheral” echelon (e.g., track and field as the core, modern pentathlon as a supplement).

<!-- b001785 | heading | pages [23] -->
8 Sensitivity Analysis

<!-- b001786 | prose | pages [23] -->
When using the hurdle model, a binary classifier is required in the first stage to classify which countries can win at least one medal. We use a logit classifier. Therefore, we will conduct a sensitivity analysis on the selection of the binary classifier to explore whether the selection of the binary classifier will affect the interpretability of the hurdle model for the number of medals and thus affect its predictive performance. We use the random forest classifier, decision tree, 微信公众号：数学模型 and logistic regression to replace the logit classifier in the hurdle, use the output probability as the result of the hurdle stage 1, regress it, and use the logit classifier as the benchmark to compare the changes in the coefficients of each covariate in the original model.

<!-- b001787 | prose | pages [23] -->
Variables Random Forest Classifier Decision Tree Logistic Regression

<!-- b001788 | prose | pages [23] -->
Host country in 4 years 0.052 0.022 -0.057 Host country t -0.011 0.025 -0.088 Host country 4 years ago 0.062 -0.013 0.565 Athletes [0,10] -0.122 0.051 -0.041 Athletes [10,50] 0.011 0.052 0.251 微信号：MATHmodels Athletes [50,150] 0.062 -0.045 0.051 150 athletes and more 0.032 0.000 0.152 Medals_PCA(t-4) -0.052 0.052 0.142 RCA 0.012 0.069 -0.098 Medals_PCA(t-4) 0.012 -0.052 -0.095 Num_Events 0.012 0.021 0.054 Num_sports 0.041 0.065 0.013 NAE -0.032 0.054 -0.064 gi,t 0.055 -0.048 0.052 σ2 -0.011 0.054 -0.098 u Observations total 0.072 -0.067 -0.052 Observations noncensored -0.065 0.002 0.082 0.025 0.051 -0.054

<!-- b001789 | prose | pages [23] -->
As can be seen from the table, the error between all the coefficients of the covariates and the explanatory variables is less than 10%, indicating that the classifier model we selected has no significant impact on the performance of the hurdle model, and our model is relatively robust.

<!-- b001790 | heading | pages [23] -->
9 Model Evaluation

<!-- b001791 | heading | pages [23] -->
9.1 Strength

<!-- b001792 | prose | pages [23] -->
• The interpretability and performance of the Hurdle and Topit models are both strong, rather than simple machine learning algorithms.

<!-- b001793 | prose | pages [23] -->
• Before using Bayesian variable point detection, the data is first preprocessed to reflect the significance of medals and the dynamic self-reinforcement mechanism.

<!-- b001794 | furniture | pages [24] -->
Team # 2501869

<!-- b001795 | furniture | pages [24] -->
Page 24 of 25

<!-- b001796 | prose | pages [24] -->
• When explaining the great coaching effect, the use of 2SLS eliminates endogeneity between variables.

<!-- b001797 | heading | pages [24] -->
9.2 Weakness

<!-- b001798 | prose | pages [24] -->
• Due to the limitations of the subject, the model does not introduce the influence of factors such as economics and humanities, which may lead to errors.

<!-- b001799 | heading | pages [24] -->
References

<!-- b001800 | references | pages [24] -->
m

<!-- b001801 | references | pages [24] -->
m

<!-- b001802 | references | pages [24] -->
m

<!-- b001803 | references | pages [24] -->
m

<!-- b001804 | references | pages [24] -->
m

<!-- b001805 | references | pages [24] -->
m

<!-- b001806 | references | pages [24] -->
m

<!-- b001807 | references | pages [24] -->
m

<!-- b001808 | references | pages [24] -->
m

<!-- b001809 | references | pages [24] -->
m

<!-- b001810 | references | pages [24] -->
m

<!-- b001811 | references | pages [24] -->
m

<!-- b001812 | references | pages [24] -->
m

<!-- b001813 | references | pages [24] -->
m

<!-- b001814 | references | pages [24] -->
m

<!-- b001815 | references | pages [24] -->
m

<!-- b001816 | references | pages [24] -->
m

<!-- b001817 | references | pages [24] -->
m

<!-- b001818 | references | pages [24] -->
m

<!-- b001819 | references | pages [24] -->
m

<!-- b001820 | references | pages [24] -->
m

<!-- b001821 | references | pages [24] -->
m

<!-- b001822 | references | pages [24] -->
m

<!-- b001823 | references | pages [24] -->
m

<!-- b001824 | references | pages [24] -->
m

<!-- b001825 | references | pages [24] -->
m

<!-- b001826 | references | pages [24] -->
m

<!-- b001827 | references | pages [24] -->
m

<!-- b001828 | references | pages [24] -->
m

<!-- b001829 | references | pages [24] -->
m

<!-- b001830 | references | pages [24] -->
m

<!-- b001831 | references | pages [24] -->
m

<!-- b001832 | references | pages [24] -->
m

<!-- b001833 | references | pages [24] -->
m

<!-- b001834 | references | pages [24] -->
m

<!-- b001835 | references | pages [24] -->
m

<!-- b001836 | references | pages [24] -->
m

<!-- b001837 | references | pages [24] -->
m

<!-- b001838 | references | pages [24] -->
m

<!-- b001839 | references | pages [24] -->
m

<!-- b001840 | references | pages [24] -->
m

<!-- b001841 | references | pages [24] -->
m

<!-- b001842 | references | pages [24] -->
m

<!-- b001843 | references | pages [24] -->
m

<!-- b001844 | references | pages [24] -->
m

<!-- b001845 | references | pages [24] -->
m

<!-- b001846 | references | pages [24] -->
m

<!-- b001847 | references | pages [24] -->
m

<!-- b001848 | references | pages [24] -->
m

<!-- b001849 | references | pages [24] -->
m

<!-- b001850 | references | pages [24] -->
m

<!-- b001851 | references | pages [24] -->
m

<!-- b001852 | references | pages [24] -->
m

<!-- b001853 | references | pages [24] -->
m

<!-- b001854 | references | pages [24] -->
m

<!-- b001855 | references | pages [24] -->
m

<!-- b001856 | references | pages [24] -->
m

<!-- b001857 | references | pages [24] -->
m

<!-- b001858 | references | pages [24] -->
m

<!-- b001859 | references | pages [24] -->
m

<!-- b001860 | references | pages [24] -->
m

<!-- b001861 | references | pages [24] -->
m

<!-- b001862 | references | pages [24] -->
m

<!-- b001863 | references | pages [24] -->
m

<!-- b001864 | references | pages [24] -->
m

<!-- b001865 | references | pages [24] -->
m

<!-- b001866 | references | pages [24] -->
m

<!-- b001867 | references | pages [24] -->
m

<!-- b001868 | references | pages [24] -->
m

<!-- b001869 | references | pages [24] -->
m

<!-- b001870 | references | pages [24] -->
m

<!-- b001871 | references | pages [24] -->
m

<!-- b001872 | references | pages [24] -->
m

<!-- b001873 | references | pages [24] -->
m

<!-- b001874 | references | pages [24] -->
m

<!-- b001875 | references | pages [24] -->
m

<!-- b001876 | references | pages [24] -->
m

<!-- b001877 | references | pages [24] -->
m

<!-- b001878 | references | pages [24] -->
m

<!-- b001879 | references | pages [24] -->
m

<!-- b001880 | references | pages [24] -->
m

<!-- b001881 | references | pages [24] -->
m

<!-- b001882 | references | pages [24] -->
m

<!-- b001883 | references | pages [24] -->
m

<!-- b001884 | references | pages [24] -->
m

<!-- b001885 | references | pages [24] -->
m

<!-- b001886 | references | pages [24] -->
m

<!-- b001887 | references | pages [24] -->
m

<!-- b001888 | references | pages [24] -->
m

<!-- b001889 | references | pages [24] -->
m

<!-- b001890 | references | pages [24] -->
m

<!-- b001891 | references | pages [24] -->
m

<!-- b001892 | references | pages [24] -->
m

<!-- b001893 | references | pages [24] -->
m

<!-- b001894 | references | pages [24] -->
m

<!-- b001895 | references | pages [24] -->
m

<!-- b001896 | references | pages [24] -->
m

<!-- b001897 | references | pages [24] -->
m

<!-- b001898 | references | pages [24] -->
m

<!-- b001899 | references | pages [24] -->
m

<!-- b001900 | references | pages [24] -->
m

<!-- b001901 | references | pages [24] -->
m

<!-- b001902 | references | pages [24] -->
m

<!-- b001903 | references | pages [24] -->
m

<!-- b001904 | references | pages [24] -->
m

<!-- b001905 | references | pages [24] -->
m

<!-- b001906 | references | pages [24] -->
m

<!-- b001907 | references | pages [24] -->
m

<!-- b001908 | references | pages [24] -->
m

<!-- b001909 | references | pages [24] -->
m

<!-- b001910 | references | pages [24] -->
m

<!-- b001911 | references | pages [24] -->
m

<!-- b001912 | references | pages [24] -->
m

<!-- b001913 | references | pages [24] -->
m

<!-- b001914 | references | pages [24] -->
m

<!-- b001915 | references | pages [24] -->
m

<!-- b001916 | references | pages [24] -->
m

<!-- b001917 | references | pages [24] -->
m

<!-- b001918 | references | pages [24] -->
m

<!-- b001919 | references | pages [24] -->
m

<!-- b001920 | references | pages [24] -->
m

<!-- b001921 | references | pages [24] -->
m

<!-- b001922 | references | pages [24] -->
m

<!-- b001923 | references | pages [24] -->
m

<!-- b001924 | references | pages [24] -->
m

<!-- b001925 | references | pages [24] -->
m

<!-- b001926 | references | pages [24] -->
m

<!-- b001927 | references | pages [24] -->
m

<!-- b001928 | references | pages [24] -->
m

<!-- b001929 | references | pages [24] -->
m

<!-- b001930 | references | pages [24] -->
[1] De Bosscher, V., de Knop, P., van Bottenburg, M., & Shibli, S. (2006). A conceptual

<!-- b001931 | references | pages [24] -->
m

<!-- b001932 | references | pages [24] -->
m

<!-- b001933 | references | pages [24] -->
m

<!-- b001934 | references | pages [24] -->
m

<!-- b001935 | references | pages [24] -->
m

<!-- b001936 | references | pages [24] -->
m

<!-- b001937 | references | pages [24] -->
m

<!-- b001938 | references | pages [24] -->
m

<!-- b001939 | references | pages [24] -->
m

<!-- b001940 | references | pages [24] -->
m

<!-- b001941 | references | pages [24] -->
m

<!-- b001942 | references | pages [24] -->
m

<!-- b001943 | references | pages [24] -->
m

<!-- b001944 | references | pages [24] -->
m

<!-- b001945 | references | pages [24] -->
m

<!-- b001946 | references | pages [24] -->
m

<!-- b001947 | references | pages [24] -->
m

<!-- b001948 | references | pages [24] -->
m

<!-- b001949 | references | pages [24] -->
m

<!-- b001950 | references | pages [24] -->
m

<!-- b001951 | references | pages [24] -->
m

<!-- b001952 | references | pages [24] -->
m

<!-- b001953 | references | pages [24] -->
m

<!-- b001954 | references | pages [24] -->
m

<!-- b001955 | references | pages [24] -->
m

<!-- b001956 | references | pages [24] -->
m

<!-- b001957 | references | pages [24] -->
m

<!-- b001958 | references | pages [24] -->
m

<!-- b001959 | references | pages [24] -->
m

<!-- b001960 | references | pages [24] -->
m

<!-- b001961 | references | pages [24] -->
m

<!-- b001962 | references | pages [24] -->
m

<!-- b001963 | references | pages [24] -->
m

<!-- b001964 | references | pages [24] -->
m

<!-- b001965 | references | pages [24] -->
m

<!-- b001966 | references | pages [24] -->
m

<!-- b001967 | references | pages [24] -->
m

<!-- b001968 | references | pages [24] -->
m

<!-- b001969 | references | pages [24] -->
m

<!-- b001970 | references | pages [24] -->
m

<!-- b001971 | references | pages [24] -->
m

<!-- b001972 | references | pages [24] -->
m

<!-- b001973 | references | pages [24] -->
m

<!-- b001974 | references | pages [24] -->
m

<!-- b001975 | references | pages [24] -->
m

<!-- b001976 | references | pages [24] -->
m

<!-- b001977 | references | pages [24] -->
m

<!-- b001978 | references | pages [24] -->
m

<!-- b001979 | references | pages [24] -->
m

<!-- b001980 | references | pages [24] -->
m

<!-- b001981 | references | pages [24] -->
m

<!-- b001982 | references | pages [24] -->
m

<!-- b001983 | references | pages [24] -->
m

<!-- b001984 | references | pages [24] -->
m

<!-- b001985 | references | pages [24] -->
m

<!-- b001986 | references | pages [24] -->
m

<!-- b001987 | references | pages [24] -->
m

<!-- b001988 | references | pages [24] -->
m

<!-- b001989 | references | pages [24] -->
m

<!-- b001990 | references | pages [24] -->
m

<!-- b001991 | references | pages [24] -->
m

<!-- b001992 | references | pages [24] -->
m

<!-- b001993 | references | pages [24] -->
m

<!-- b001994 | references | pages [24] -->
m

<!-- b001995 | references | pages [24] -->
m

<!-- b001996 | references | pages [24] -->
m

<!-- b001997 | references | pages [24] -->
m

<!-- b001998 | references | pages [24] -->
m

<!-- b001999 | references | pages [24] -->
m

<!-- b002000 | references | pages [24] -->
m

<!-- b002001 | references | pages [24] -->
m

<!-- b002002 | references | pages [24] -->
m

<!-- b002003 | references | pages [24] -->
m

<!-- b002004 | references | pages [24] -->
m

<!-- b002005 | references | pages [24] -->
m

<!-- b002006 | references | pages [24] -->
m

<!-- b002007 | references | pages [24] -->
m

<!-- b002008 | references | pages [24] -->
m

<!-- b002009 | references | pages [24] -->
m

<!-- b002010 | references | pages [24] -->
m

<!-- b002011 | references | pages [24] -->
m

<!-- b002012 | references | pages [24] -->
m

<!-- b002013 | references | pages [24] -->
m

<!-- b002014 | references | pages [24] -->
m

<!-- b002015 | references | pages [24] -->
m

<!-- b002016 | references | pages [24] -->
m

<!-- b002017 | references | pages [24] -->
m

<!-- b002018 | references | pages [24] -->
m

<!-- b002019 | references | pages [24] -->
m

<!-- b002020 | references | pages [24] -->
m

<!-- b002021 | references | pages [24] -->
m

<!-- b002022 | references | pages [24] -->
m

<!-- b002023 | references | pages [24] -->
m

<!-- b002024 | references | pages [24] -->
m

<!-- b002025 | references | pages [24] -->
m

<!-- b002026 | references | pages [24] -->
m

<!-- b002027 | references | pages [24] -->
m

<!-- b002028 | references | pages [24] -->
m

<!-- b002029 | references | pages [24] -->
m

<!-- b002030 | references | pages [24] -->
m

<!-- b002031 | references | pages [24] -->
m

<!-- b002032 | references | pages [24] -->
m

<!-- b002033 | references | pages [24] -->
m

<!-- b002034 | references | pages [24] -->
m

<!-- b002035 | references | pages [24] -->
m

<!-- b002036 | references | pages [24] -->
m

<!-- b002037 | references | pages [24] -->
m

<!-- b002038 | references | pages [24] -->
m

<!-- b002039 | references | pages [24] -->
m

<!-- b002040 | references | pages [24] -->
m

<!-- b002041 | references | pages [24] -->
m

<!-- b002042 | references | pages [24] -->
m

<!-- b002043 | references | pages [24] -->
m

<!-- b002044 | references | pages [24] -->
m

<!-- b002045 | references | pages [24] -->
m

<!-- b002046 | references | pages [24] -->
m

<!-- b002047 | references | pages [24] -->
m

<!-- b002048 | references | pages [24] -->
m

<!-- b002049 | references | pages [24] -->
m

<!-- b002050 | references | pages [24] -->
m

<!-- b002051 | references | pages [24] -->
m

<!-- b002052 | references | pages [24] -->
m

<!-- b002053 | references | pages [24] -->
m

<!-- b002054 | references | pages [24] -->
m

<!-- b002055 | references | pages [24] -->
m

<!-- b002056 | references | pages [24] -->
m

<!-- b002057 | references | pages [24] -->
m

<!-- b002058 | references | pages [24] -->
m

<!-- b002059 | references | pages [24] -->
m

<!-- b002060 | references | pages [24] -->
m

<!-- b002061 | references | pages [24] -->
m

<!-- b002062 | references | pages [24] -->
m

<!-- b002063 | references | pages [24] -->
m

<!-- b002064 | references | pages [24] -->
m

<!-- b002065 | references | pages [24] -->
m

<!-- b002066 | references | pages [24] -->
m

<!-- b002067 | references | pages [24] -->
m

<!-- b002068 | references | pages [24] -->
m

<!-- b002069 | references | pages [24] -->
m

<!-- b002070 | references | pages [24] -->
m

<!-- b002071 | references | pages [24] -->
m

<!-- b002072 | references | pages [24] -->
m

<!-- b002073 | references | pages [24] -->
m

<!-- b002074 | references | pages [24] -->
m

<!-- b002075 | references | pages [24] -->
m

<!-- b002076 | references | pages [24] -->
m

<!-- b002077 | references | pages [24] -->
m

<!-- b002078 | references | pages [24] -->
m

<!-- b002079 | references | pages [24] -->
m

<!-- b002080 | references | pages [24] -->
m

<!-- b002081 | references | pages [24] -->
m

<!-- b002082 | references | pages [24] -->
m

<!-- b002083 | references | pages [24] -->
m

<!-- b002084 | references | pages [24] -->
m

<!-- b002085 | references | pages [24] -->
framework for analysing sports policy factors leading to international sporting success.

<!-- b002086 | references | pages [24] -->
m

<!-- b002087 | references | pages [24] -->
m

<!-- b002088 | references | pages [24] -->
m

<!-- b002089 | references | pages [24] -->
m

<!-- b002090 | references | pages [24] -->
m

<!-- b002091 | references | pages [24] -->
m

<!-- b002092 | references | pages [24] -->
m

<!-- b002093 | references | pages [24] -->
m

<!-- b002094 | references | pages [24] -->
m

<!-- b002095 | references | pages [24] -->
m

<!-- b002096 | references | pages [24] -->
m

<!-- b002097 | references | pages [24] -->
m

<!-- b002098 | references | pages [24] -->
m

<!-- b002099 | references | pages [24] -->
m

<!-- b002100 | references | pages [24] -->
m

<!-- b002101 | references | pages [24] -->
m

<!-- b002102 | references | pages [24] -->
m

<!-- b002103 | references | pages [24] -->
m

<!-- b002104 | references | pages [24] -->
m

<!-- b002105 | references | pages [24] -->
m

<!-- b002106 | references | pages [24] -->
m

<!-- b002107 | references | pages [24] -->
m

<!-- b002108 | references | pages [24] -->
m

<!-- b002109 | references | pages [24] -->
m

<!-- b002110 | references | pages [24] -->
m

<!-- b002111 | references | pages [24] -->
m

<!-- b002112 | references | pages [24] -->
m

<!-- b002113 | references | pages [24] -->
m

<!-- b002114 | references | pages [24] -->
m

<!-- b002115 | references | pages [24] -->
m

<!-- b002116 | references | pages [24] -->
m

<!-- b002117 | references | pages [24] -->
m

<!-- b002118 | references | pages [24] -->
m

<!-- b002119 | references | pages [24] -->
m

<!-- b002120 | references | pages [24] -->
m

<!-- b002121 | references | pages [24] -->
m

<!-- b002122 | references | pages [24] -->
m

<!-- b002123 | references | pages [24] -->
m

<!-- b002124 | references | pages [24] -->
m

<!-- b002125 | references | pages [24] -->
m

<!-- b002126 | references | pages [24] -->
m

<!-- b002127 | references | pages [24] -->
m

<!-- b002128 | references | pages [24] -->
m

<!-- b002129 | references | pages [24] -->
m

<!-- b002130 | references | pages [24] -->
m

<!-- b002131 | references | pages [24] -->
m

<!-- b002132 | references | pages [24] -->
m

<!-- b002133 | references | pages [24] -->
m

<!-- b002134 | references | pages [24] -->
m

<!-- b002135 | references | pages [24] -->
m

<!-- b002136 | references | pages [24] -->
m

<!-- b002137 | references | pages [24] -->
m

<!-- b002138 | references | pages [24] -->
m

<!-- b002139 | references | pages [24] -->
m

<!-- b002140 | references | pages [24] -->
m

<!-- b002141 | references | pages [24] -->
m

<!-- b002142 | references | pages [24] -->
m

<!-- b002143 | references | pages [24] -->
m

<!-- b002144 | references | pages [24] -->
m

<!-- b002145 | references | pages [24] -->
m

<!-- b002146 | references | pages [24] -->
m

<!-- b002147 | references | pages [24] -->
m

<!-- b002148 | references | pages [24] -->
m

<!-- b002149 | references | pages [24] -->
m

<!-- b002150 | references | pages [24] -->
m

<!-- b002151 | references | pages [24] -->
m

<!-- b002152 | references | pages [24] -->
m

<!-- b002153 | references | pages [24] -->
m

<!-- b002154 | references | pages [24] -->
m

<!-- b002155 | references | pages [24] -->
m

<!-- b002156 | references | pages [24] -->
m

<!-- b002157 | references | pages [24] -->
m

<!-- b002158 | references | pages [24] -->
m

<!-- b002159 | references | pages [24] -->
m

<!-- b002160 | references | pages [24] -->
m

<!-- b002161 | references | pages [24] -->
m

<!-- b002162 | references | pages [24] -->
m

<!-- b002163 | references | pages [24] -->
m

<!-- b002164 | references | pages [24] -->
m

<!-- b002165 | references | pages [24] -->
m

<!-- b002166 | references | pages [24] -->
m

<!-- b002167 | references | pages [24] -->
m

<!-- b002168 | references | pages [24] -->
m

<!-- b002169 | references | pages [24] -->
m

<!-- b002170 | references | pages [24] -->
m

<!-- b002171 | references | pages [24] -->
m

<!-- b002172 | references | pages [24] -->
m

<!-- b002173 | references | pages [24] -->
m

<!-- b002174 | references | pages [24] -->
m

<!-- b002175 | references | pages [24] -->
m

<!-- b002176 | references | pages [24] -->
m

<!-- b002177 | references | pages [24] -->
m

<!-- b002178 | references | pages [24] -->
m

<!-- b002179 | references | pages [24] -->
m

<!-- b002180 | references | pages [24] -->
m

<!-- b002181 | references | pages [24] -->
m

<!-- b002182 | references | pages [24] -->
m

<!-- b002183 | references | pages [24] -->
m

<!-- b002184 | references | pages [24] -->
m

<!-- b002185 | references | pages [24] -->
m

<!-- b002186 | references | pages [24] -->
m

<!-- b002187 | references | pages [24] -->
m

<!-- b002188 | references | pages [24] -->
m

<!-- b002189 | references | pages [24] -->
m

<!-- b002190 | references | pages [24] -->
m

<!-- b002191 | references | pages [24] -->
m

<!-- b002192 | references | pages [24] -->
m

<!-- b002193 | references | pages [24] -->
m

<!-- b002194 | references | pages [24] -->
m

<!-- b002195 | references | pages [24] -->
m

<!-- b002196 | references | pages [24] -->
m

<!-- b002197 | references | pages [24] -->
m

<!-- b002198 | references | pages [24] -->
m

<!-- b002199 | references | pages [24] -->
m

<!-- b002200 | references | pages [24] -->
m

<!-- b002201 | references | pages [24] -->
m

<!-- b002202 | references | pages [24] -->
m

<!-- b002203 | references | pages [24] -->
m

<!-- b002204 | references | pages [24] -->
m

<!-- b002205 | references | pages [24] -->
m

<!-- b002206 | references | pages [24] -->
m

<!-- b002207 | references | pages [24] -->
m

<!-- b002208 | references | pages [24] -->
European Sport Management Quarterly, 6(2), 185-215.

<!-- b002209 | references | pages [24] -->
m

<!-- b002210 | references | pages [24] -->
m

<!-- b002211 | references | pages [24] -->
m

<!-- b002212 | references | pages [24] -->
m

<!-- b002213 | references | pages [24] -->
m

<!-- b002214 | references | pages [24] -->
m

<!-- b002215 | references | pages [24] -->
m

<!-- b002216 | references | pages [24] -->
m

<!-- b002217 | references | pages [24] -->
m

<!-- b002218 | references | pages [24] -->
m

<!-- b002219 | references | pages [24] -->
m

<!-- b002220 | references | pages [24] -->
m

<!-- b002221 | references | pages [24] -->
m

<!-- b002222 | references | pages [24] -->
m

<!-- b002223 | references | pages [24] -->
m

<!-- b002224 | references | pages [24] -->
m

<!-- b002225 | references | pages [24] -->
m

<!-- b002226 | references | pages [24] -->
m

<!-- b002227 | references | pages [24] -->
m

<!-- b002228 | references | pages [24] -->
m

<!-- b002229 | references | pages [24] -->
m

<!-- b002230 | references | pages [24] -->
m

<!-- b002231 | references | pages [24] -->
m

<!-- b002232 | references | pages [24] -->
m

<!-- b002233 | references | pages [24] -->
m

<!-- b002234 | references | pages [24] -->
m

<!-- b002235 | references | pages [24] -->
m

<!-- b002236 | references | pages [24] -->
m

<!-- b002237 | references | pages [24] -->
m

<!-- b002238 | references | pages [24] -->
m

<!-- b002239 | references | pages [24] -->
m

<!-- b002240 | references | pages [24] -->
m

<!-- b002241 | references | pages [24] -->
m

<!-- b002242 | references | pages [24] -->
m

<!-- b002243 | references | pages [24] -->
m

<!-- b002244 | references | pages [24] -->
m

<!-- b002245 | references | pages [24] -->
m

<!-- b002246 | references | pages [24] -->
m

<!-- b002247 | references | pages [24] -->
m

<!-- b002248 | references | pages [24] -->
m

<!-- b002249 | references | pages [24] -->
m

<!-- b002250 | references | pages [24] -->
m

<!-- b002251 | references | pages [24] -->
m

<!-- b002252 | references | pages [24] -->
m

<!-- b002253 | references | pages [24] -->
m

<!-- b002254 | references | pages [24] -->
m

<!-- b002255 | references | pages [24] -->
m

<!-- b002256 | references | pages [24] -->
m

<!-- b002257 | references | pages [24] -->
m

<!-- b002258 | references | pages [24] -->
m

<!-- b002259 | references | pages [24] -->
m

<!-- b002260 | references | pages [24] -->
m

<!-- b002261 | references | pages [24] -->
m

<!-- b002262 | references | pages [24] -->
m

<!-- b002263 | references | pages [24] -->
m

<!-- b002264 | references | pages [24] -->
m

<!-- b002265 | references | pages [24] -->
m

<!-- b002266 | references | pages [24] -->
m

<!-- b002267 | references | pages [24] -->
m

<!-- b002268 | references | pages [24] -->
m

<!-- b002269 | references | pages [24] -->
m

<!-- b002270 | references | pages [24] -->
m

<!-- b002271 | references | pages [24] -->
m

<!-- b002272 | references | pages [24] -->
m

<!-- b002273 | references | pages [24] -->
m

<!-- b002274 | references | pages [24] -->
m

<!-- b002275 | references | pages [24] -->
m

<!-- b002276 | references | pages [24] -->
m

<!-- b002277 | references | pages [24] -->
m

<!-- b002278 | references | pages [24] -->
m

<!-- b002279 | references | pages [24] -->
m

<!-- b002280 | references | pages [24] -->
m

<!-- b002281 | references | pages [24] -->
m

<!-- b002282 | references | pages [24] -->
m

<!-- b002283 | references | pages [24] -->
m

<!-- b002284 | references | pages [24] -->
m

<!-- b002285 | references | pages [24] -->
m

<!-- b002286 | references | pages [24] -->
m

<!-- b002287 | references | pages [24] -->
m

<!-- b002288 | references | pages [24] -->
m

<!-- b002289 | references | pages [24] -->
m

<!-- b002290 | references | pages [24] -->
m

<!-- b002291 | references | pages [24] -->
m

<!-- b002292 | references | pages [24] -->
m

<!-- b002293 | references | pages [24] -->
m

<!-- b002294 | references | pages [24] -->
m

<!-- b002295 | references | pages [24] -->
m

<!-- b002296 | references | pages [24] -->
m

<!-- b002297 | references | pages [24] -->
m

<!-- b002298 | references | pages [24] -->
m

<!-- b002299 | references | pages [24] -->
m

<!-- b002300 | references | pages [24] -->
m

<!-- b002301 | references | pages [24] -->
m

<!-- b002302 | references | pages [24] -->
m

<!-- b002303 | references | pages [24] -->
m

<!-- b002304 | references | pages [24] -->
m

<!-- b002305 | references | pages [24] -->
m

<!-- b002306 | references | pages [24] -->
m

<!-- b002307 | references | pages [24] -->
m

<!-- b002308 | references | pages [24] -->
m

<!-- b002309 | references | pages [24] -->
m

<!-- b002310 | references | pages [24] -->
m

<!-- b002311 | references | pages [24] -->
m

<!-- b002312 | references | pages [24] -->
m

<!-- b002313 | references | pages [24] -->
m

<!-- b002314 | references | pages [24] -->
m

<!-- b002315 | references | pages [24] -->
m

<!-- b002316 | references | pages [24] -->
m

<!-- b002317 | references | pages [24] -->
m

<!-- b002318 | references | pages [24] -->
m

<!-- b002319 | references | pages [24] -->
m

<!-- b002320 | references | pages [24] -->
m

<!-- b002321 | references | pages [24] -->
m

<!-- b002322 | references | pages [24] -->
m

<!-- b002323 | references | pages [24] -->
m

<!-- b002324 | references | pages [24] -->
m

<!-- b002325 | references | pages [24] -->
m

<!-- b002326 | references | pages [24] -->
m

<!-- b002327 | references | pages [24] -->
m

<!-- b002328 | references | pages [24] -->
m

<!-- b002329 | references | pages [24] -->
m

<!-- b002330 | references | pages [24] -->
m

<!-- b002331 | references | pages [24] -->
m

<!-- b002332 | references | pages [24] -->
m

<!-- b002333 | references | pages [24] -->
m

<!-- b002334 | references | pages [24] -->
m

<!-- b002335 | references | pages [24] -->
m

<!-- b002336 | references | pages [24] -->
m

<!-- b002337 | references | pages [24] -->
m

<!-- b002338 | references | pages [24] -->
m

<!-- b002339 | references | pages [24] -->
m

<!-- b002340 | references | pages [24] -->
m

<!-- b002341 | references | pages [24] -->
m

<!-- b002342 | references | pages [24] -->
m

<!-- b002343 | references | pages [24] -->
m

<!-- b002344 | references | pages [24] -->
m

<!-- b002345 | references | pages [24] -->
m

<!-- b002346 | references | pages [24] -->
m

<!-- b002347 | references | pages [24] -->
m

<!-- b002348 | references | pages [24] -->
m

<!-- b002349 | references | pages [24] -->
m

<!-- b002350 | references | pages [24] -->
m

<!-- b002351 | references | pages [24] -->
m

<!-- b002352 | references | pages [24] -->
m

<!-- b002353 | references | pages [24] -->
m

<!-- b002354 | references | pages [24] -->
m

<!-- b002355 | references | pages [24] -->
m

<!-- b002356 | references | pages [24] -->
m

<!-- b002357 | references | pages [24] -->
m

<!-- b002358 | references | pages [24] -->
m

<!-- b002359 | references | pages [24] -->
m

<!-- b002360 | references | pages [24] -->
m

<!-- b002361 | references | pages [24] -->
m

<!-- b002362 | references | pages [24] -->
m

<!-- b002363 | references | pages [24] -->
m

<!-- b002364 | references | pages [24] -->
m

<!-- b002365 | references | pages [24] -->
m

<!-- b002366 | references | pages [24] -->
m

<!-- b002367 | references | pages [24] -->
m

<!-- b002368 | references | pages [24] -->
m

<!-- b002369 | references | pages [24] -->
m

<!-- b002370 | references | pages [24] -->
m

<!-- b002371 | references | pages [24] -->
m

<!-- b002372 | references | pages [24] -->
m

<!-- b002373 | references | pages [24] -->
m

<!-- b002374 | references | pages [24] -->
m

<!-- b002375 | references | pages [24] -->
m

<!-- b002376 | references | pages [24] -->
m

<!-- b002377 | references | pages [24] -->
m

<!-- b002378 | references | pages [24] -->
m

<!-- b002379 | references | pages [24] -->
m

<!-- b002380 | references | pages [24] -->
m

<!-- b002381 | references | pages [24] -->
m

<!-- b002382 | references | pages [24] -->
m

<!-- b002383 | references | pages [24] -->
m

<!-- b002384 | references | pages [24] -->
m

<!-- b002385 | references | pages [24] -->
m

<!-- b002386 | references | pages [24] -->
m

<!-- b002387 | references | pages [24] -->
m

<!-- b002388 | references | pages [24] -->
m

<!-- b002389 | references | pages [24] -->
m

<!-- b002390 | references | pages [24] -->
m

<!-- b002391 | references | pages [24] -->
m

<!-- b002392 | references | pages [24] -->
m

<!-- b002393 | references | pages [24] -->
m

<!-- b002394 | references | pages [24] -->
m

<!-- b002395 | references | pages [24] -->
m

<!-- b002396 | references | pages [24] -->
m

<!-- b002397 | references | pages [24] -->
m

<!-- b002398 | references | pages [24] -->
m

<!-- b002399 | references | pages [24] -->
m

<!-- b002400 | references | pages [24] -->
m

<!-- b002401 | references | pages [24] -->
m

<!-- b002402 | references | pages [24] -->
m

<!-- b002403 | references | pages [24] -->
m

<!-- b002404 | references | pages [24] -->
m

<!-- b002405 | references | pages [24] -->
m

<!-- b002406 | references | pages [24] -->
m

<!-- b002407 | references | pages [24] -->
m

<!-- b002408 | references | pages [24] -->
m

<!-- b002409 | references | pages [24] -->
m

<!-- b002410 | references | pages [24] -->
m

<!-- b002411 | references | pages [24] -->
m

<!-- b002412 | references | pages [24] -->
m

<!-- b002413 | references | pages [24] -->
m

<!-- b002414 | references | pages [24] -->
m

<!-- b002415 | references | pages [24] -->
m

<!-- b002416 | references | pages [24] -->
m

<!-- b002417 | references | pages [24] -->
m

<!-- b002418 | references | pages [24] -->
m

<!-- b002419 | references | pages [24] -->
m

<!-- b002420 | references | pages [24] -->
m

<!-- b002421 | references | pages [24] -->
m

<!-- b002422 | references | pages [24] -->
m

<!-- b002423 | references | pages [24] -->
m

<!-- b002424 | references | pages [24] -->
m

<!-- b002425 | references | pages [24] -->
m

<!-- b002426 | references | pages [24] -->
m

<!-- b002427 | references | pages [24] -->
m

<!-- b002428 | references | pages [24] -->
m

<!-- b002429 | references | pages [24] -->
m

<!-- b002430 | references | pages [24] -->
m

<!-- b002431 | references | pages [24] -->
m

<!-- b002432 | references | pages [24] -->
m

<!-- b002433 | references | pages [24] -->
m

<!-- b002434 | references | pages [24] -->
m

<!-- b002435 | references | pages [24] -->
m

<!-- b002436 | references | pages [24] -->
m

<!-- b002437 | references | pages [24] -->
m

<!-- b002438 | references | pages [24] -->
m

<!-- b002439 | references | pages [24] -->
m

<!-- b002440 | references | pages [24] -->
m

<!-- b002441 | references | pages [24] -->
m

<!-- b002442 | references | pages [24] -->
m

<!-- b002443 | references | pages [24] -->
m

<!-- b002444 | references | pages [24] -->
m

<!-- b002445 | references | pages [24] -->
m

<!-- b002446 | references | pages [24] -->
m

<!-- b002447 | references | pages [24] -->
m

<!-- b002448 | references | pages [24] -->
[2] Streicher, T., Schmidt, S. L., Schreyer, D., & Torgler, B. (2020). Anticipated feelings and

<!-- b002449 | references | pages [24] -->
m

<!-- b002450 | references | pages [24] -->
m

<!-- b002451 | references | pages [24] -->
m

<!-- b002452 | references | pages [24] -->
m

<!-- b002453 | references | pages [24] -->
m

<!-- b002454 | references | pages [24] -->
m

<!-- b002455 | references | pages [24] -->
m

<!-- b002456 | references | pages [24] -->
m

<!-- b002457 | references | pages [24] -->
m

<!-- b002458 | references | pages [24] -->
m

<!-- b002459 | references | pages [24] -->
m

<!-- b002460 | references | pages [24] -->
m

<!-- b002461 | references | pages [24] -->
m

<!-- b002462 | references | pages [24] -->
m

<!-- b002463 | references | pages [24] -->
m

<!-- b002464 | references | pages [24] -->
m

<!-- b002465 | references | pages [24] -->
m

<!-- b002466 | references | pages [24] -->
m

<!-- b002467 | references | pages [24] -->
m

<!-- b002468 | references | pages [24] -->
m

<!-- b002469 | references | pages [24] -->
m

<!-- b002470 | references | pages [24] -->
m

<!-- b002471 | references | pages [24] -->
m

<!-- b002472 | references | pages [24] -->
m

<!-- b002473 | references | pages [24] -->
m

<!-- b002474 | references | pages [24] -->
m

<!-- b002475 | references | pages [24] -->
m

<!-- b002476 | references | pages [24] -->
m

<!-- b002477 | references | pages [24] -->
m

<!-- b002478 | references | pages [24] -->
m

<!-- b002479 | references | pages [24] -->
m

<!-- b002480 | references | pages [24] -->
m

<!-- b002481 | references | pages [24] -->
m

<!-- b002482 | references | pages [24] -->
m

<!-- b002483 | references | pages [24] -->
m

<!-- b002484 | references | pages [24] -->
m

<!-- b002485 | references | pages [24] -->
m

<!-- b002486 | references | pages [24] -->
m

<!-- b002487 | references | pages [24] -->
m

<!-- b002488 | references | pages [24] -->
m

<!-- b002489 | references | pages [24] -->
m

<!-- b002490 | references | pages [24] -->
m

<!-- b002491 | references | pages [24] -->
support for public mega projects: Hosting the Olympic Games. Technological Forecasting

<!-- b002492 | references | pages [24] -->
and Social Change, 158, 120158.

<!-- b002493 | references | pages [24] -->
[3] Ball, D. W. (1972). Olympic games competition: Structural correlates of national success.

<!-- b002494 | references | pages [24] -->
International Journal of Comparative Sociology, 13(2), 186-200.

<!-- b002495 | references | pages [24] -->
[4] Bainbridge, M. (1998). Outcome uncertainty in sporting competition: The Olympic Games

<!-- b002496 | references | pages [24] -->
1896–1996. Applied Economics Letters, 5(3), 161-164.

<!-- b002497 | references | pages [24] -->
[5] Condon, E. M., Golden, B. L., & Wasil, E. A. (1999). Predicting the success of nations at

<!-- b002498 | references | pages [24] -->
the summer Olympics using neural networks. Computers & Operations Research, 26(13),

<!-- b002499 | references | pages [24] -->
1243-1265.

<!-- b002500 | references | pages [24] -->
[6] Kuper, G. H., & Sterken, E. (2001). Olympic participation and performance since 1896.

<!-- b002501 | references | pages [24] -->
SSRN Electronic Journal. https://doi.org/10.2139/ssrn.274295

<!-- b002502 | references | pages [24] -->
[7] Lui, H.-K., & Suen, W. (2008). Men, money, and medals: An econometric analysis of the

<!-- b002503 | references | pages [24] -->
Olympic Games. Pacific Economic Review, 13(1), 1-16.

<!-- b002504 | references | pages [24] -->
[8] Leeds, E. M., & Leeds, M. A. (2012). Gold, silver, and bronze: Determining national

<!-- b002505 | references | pages [24] -->
success in men’s and women’s Summer Olympic events. Jahrbücher für Nationalökonomie

<!-- b002506 | references | pages [24] -->
und Statistik, 232(3), 279-292.

<!-- b002507 | references | pages [24] -->
[9] Blais-Morisset, P., Boucher, N., & Fortin, B. (2017). The impact of public investment in

<!-- b002508 | references | pages [24] -->
sports on the Olympic medals. Revue économique, 68(4), 623-642.

<!-- b002509 | references | pages [24] -->
[10] Groll, A., Ley, C., Schauberger, G., & van Eetvelde, H. (2019). A hybrid random forest to

<!-- b002510 | references | pages [24] -->
predict soccer matches in international tournaments. Journal of Quantitative Analysis in

<!-- b002511 | references | pages [24] -->
Sports, 15(4), 271-287.

<!-- b002512 | references | pages [24] -->
[11] Lessmann, S., Sung, M.-C., & Johnson, J. E. (2010). Alternative methods of predicting

<!-- b002513 | references | pages [24] -->
competitive events: An application in horserace betting markets. International Journal of

<!-- b002514 | references | pages [24] -->
Forecasting, 26(3), 518-536.

<!-- b002515 | references | pages [24] -->
[12] Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5-32.

<!-- b002516 | references | pages [24] -->
关注数学模型

<!-- b002517 | furniture | pages [24] -->
2

<!-- b002518 | furniture | pages [24] -->
MATHmodels

<!-- b002519 | furniture | pages [24] -->
获取更多资讯

<!-- b002520 | furniture | pages [25] -->
Team # 2501869

<!-- b002521 | furniture | pages [25] -->
Page 25 of 25

<!-- b002522 | references | pages [25] -->
[13] Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In Proceedings

<!-- b002523 | references | pages [25] -->
of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data

<!-- b002524 | references | pages [25] -->
Mining (pp. 785-794). ACM. https://doi.org/10.1145/2939672.2939785

<!-- b002525 | references | pages [25] -->
微信公众号：数学模型

<!-- b002526 | references | pages [25] -->
[14] Tcha, M., & Pershin, V. (2003). Reconsidering performance at the summer Olympics and

<!-- b002527 | references | pages [25] -->
revealed comparative advantages. Journal of Sports Economics, 4(3), 216-239.

<!-- b002528 | references | pages [25] -->
[15] Forrest, D., McHale, I. G., Sanz, I., & Tena, J. D. (2015). Determinants of national

<!-- b002529 | references | pages [25] -->
medal totals at the summer Olympic games: An analysis disaggregated by sport. In The

<!-- b002530 | references | pages [25] -->
Economics of Competitive Sports. Edward Elgar Publishing.

<!-- b002531 | references | pages [25] -->
[16] Rewilak, J. (2021). The (non) determinants of Olympic success. Journal of Sports Eco-

<!-- b002532 | references | pages [25] -->
nomics, 22(7), 152700252199283.

<!-- b002533 | references | pages [25] -->
[17] Scelles, N., Andreff, W., Bonnal, L., Andreff, M., & Favard, P. (2020). Forecasting national

<!-- b002534 | references | pages [25] -->
微信号：MATHmodels

<!-- b002535 | references | pages [25] -->
medal totals at the summer Olympic games reconsidered. Social Science Quarterly, 101(2),

<!-- b002536 | references | pages [25] -->
697-711.

<!-- b002537 | references | pages [25] -->
[18] Streicher, T., Schmidt, S. L., Schreyer, D., & Torgler, B. (2020). Anticipated feelings and

<!-- b002538 | references | pages [25] -->
support for public mega projects: Hosting the Olympic Games. Technological Forecasting

<!-- b002539 | references | pages [25] -->
and Social Change, 158, 120158.

<!-- b002540 | references | pages [25] -->
[19] Scelles, N. , Andreff, W. , Bonnal, L. , Andreff, M. ,& Favard, P. . (2020). Forecasting

<!-- b002541 | references | pages [25] -->
national medal totals at the summer olympic games reconsidered. Social Science Quarterly,

<!-- b002542 | references | pages [25] -->
101(2).
