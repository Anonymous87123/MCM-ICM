# P-C-2025-2500759-cc793619

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2025

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | title | pages [1] -->
2500759

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Olympic Multi-dimensional Predictive Integrator

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
To ensure a systematic and multidimensional approach to Olympic medal prediction, this study constructs a dynamic and coupled comprehensive prediction framework. This framework integrates various objectives, including medal distribution prediction, break-

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
through country identification, event performance evaluation, and the impact analysis of coaching resource allocation. By employing multi-source heterogeneous data fusion and machine learning integration methods, we achieve an in-depth analysis and reliable pre- diction of the development patterns in competitive sports.

<!-- b000013 | prose | pages [1] -->
First, we develop a multidimensional predictive model to analyze Olympic medal patterns. Utilizing Principal Component Analysis (PCA) for dimensionality reduction and noise filtering of the Olympic event dataset, we combine Long Short-Term Mem- ory (LSTM) networks to mine temporal features and integrate home advantage effects. A dual-channel XGBoost-Bootstrap model is established to generate predictions with a 95% confidence interval. The results indicate an upward trend for countries such as

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
the United States and the United Kingdom, while countries like France and China show a decline. The model has a low MAE and MAPE, exhibiting a high accuracy and strong ro- bustness. Through non-parametric testing, potential breakthrough countries are identified, with San Marino and Kuwait showing gold medal breakthrough probabilities of 84.7% and 68.4%, respectively. Event analysis reveals a strong correlation between swimming, athletics, and medal counts, while SHapley Additive exPlanations (SHAP) quantifies shooting as a core contributing event. Principal component analysis uncovers the positive driving effects of swimming and wrestling on medal augmentation, informing optimal sports event allocation.

<!-- b000016 | prose | pages [1] -->
Subsequently, we develop a Difference-in-Differences (DID) model to quantify the competitive benefits of coaching replacement and conduct statistical significance tests as well as parallel trends tests to ensure the reliability of our results. It is found that during the 2020-2024 period, Australia, South Korea, and Poland experienced significant "great coach" policy effects through strategic restructuring of their coaching teams. Based on this, we recommend prioritizing investment in high-elasticity projects.

<!-- b000017 | prose | pages [1] -->
Finally, we synthesize all models and analyses to present new insights and corre- sponding decision supports.

<!-- b000018 | keywords | pages [1] -->
Keywords: Prediction Model, PCA, LSTM, XGBoost, SHAP, DID

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1

<!-- b000021 | heading | pages [2] -->
Introduction

<!-- b000022 | prose | pages [2] -->
3 1.1 Problem Background· 1.2 Clarifications and Restatements 1.3 Our Work· 3 2

<!-- b000023 | heading | pages [2] -->
Preparation for Modeling

<!-- b000024 | prose | pages [2] -->
2.1 Model Assumptions. 3 2.2 4

<!-- b000025 | heading | pages [2] -->
Notations

<!-- b000026 | prose | pages [2] -->
Data Preprocessing 2.3 4 3 Problem 1: Medal Prediction 5 Medal Ranking 5 3.1 PCA: Reducing Dimensions 3.1.1 5 3.1.2 LSTM: Trends Based on Time. 6 3.1.3

<!-- b000027 | heading | pages [2] -->
XGBoost-Bootstrap Modeling

<!-- b000028 | heading | pages [2] -->
Results Display

<!-- b000029 | prose | pages [2] -->
9 3.1.4 3.2 Breaking the Zero 10 3.3 13 Olympic Events and Medal Counts.

<!-- b000030 | prose | pages [2] -->
13 3.3.1 Spearman: A Mathematical Analysis 3.3.2 14 3.3.3 15 Analysis of Relationships and Importance Problem 2: The "Great Coach" Effect . . 18 4

<!-- b000031 | heading | pages [2] -->
4.1 DID Modeling

<!-- b000032 | prose | pages [2] -->
18 Hypothesis Testing and Contribution Coefficient Analysis 19 4.2 19 5

<!-- b000033 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000034 | prose | pages [2] -->
21 6 21 6.1 The Number of Principal Components 21 6.2 Prediction Model Evaluation· 22 7

<!-- b000035 | heading | pages [2] -->
Model Analysis

<!-- b000036 | prose | pages [2] -->
22 7.1

<!-- b000037 | heading | pages [2] -->
Strength · ·

<!-- b000038 | heading | pages [2] -->
Weekness and Further Discussion·

<!-- b000039 | prose | pages [2] -->
23 7.2 Memorandum.. 24 8

<!-- b000040 | heading | pages [2] -->
Reference

<!-- b000041 | references | pages [2] -->
25

<!-- b000042 | references | pages [2] -->
关注数学模型

<!-- b000043 | furniture | pages [2] -->
获取更多资讯

<!-- b000044 | furniture | pages [3] -->
Team # 2500759

<!-- b000045 | furniture | pages [3] -->
Page 3 of 26

<!-- b000046 | heading | pages [3] -->
1 Introduction

<!-- b000047 | heading | pages [3] -->
1.1 Problem Background

<!-- b000048 | prose | pages [3] -->
The medal standings of the 2024 Paris Summer Olympics illustrate the diversity of international sports competition: the United States led with 126 total medals, while China tied for the gold medal count. The host nation, France, underscores the advantages of hosting by securing the fourth position in total medal accumulation. Emerging powers such as Albania have achieved their first gold medal, whereas over 60 countries have yet to register any medals, reflecting the uneven distribution of competitive resources. 微信公众号：数学模型 Current predictions largely rely on pre-competition data6; however, key variables such as historical trends, adjustments to events, and coaching effects have not yet been adequately quantified. By constructing data-driven models2, it becomes possible to accurately iden- tify potential medal-winning events, optimize coaching resources, leverage host country advantages, and reveal the pathways to the emergence of "invisible champions". This ap- proach provides dynamic insights that can aid nations in formulating strategies and foster a rebalancing of the Olympic landscape.

<!-- b000049 | heading | pages [3] -->
1.2 Clarifications and Restatements

<!-- b000050 | prose | pages [3] -->
Given the background information and constraints of the problem, we must complete 微信号：MATHmodels the following tasks:

<!-- b000051 | prose | pages [3] -->
Task 1: Develop a model to predict gold and total medal counts for each country at the 2028 Los Angeles Olympics and compare predictions with the 2024 Paris Olympics. Task 2: Identify countries expected to win their first medals at the upcoming Olympics using the model from Task 1, and estimate the likelihood of a "zero breakthrough". Task 3: Analyze the relationship between Olympic sports and medal counts, considering the impact of the host nation and selected sports. Task 4: Create a model to identify countries with the "great coach" effect in specific sports and provide contribution coefficients. Task 5: Based on the topic and the work conducted, additional original insights are pre- sented.

<!-- b000052 | heading | pages [3] -->
1.3 Our Work

<!-- b000053 | prose | pages [3] -->
First, dimensionality reduction is performed using PCA. Next, trend information is incorporated through LSTM, leading to the establishment of an XGBoost prediction model. Subsequently, the Wlicoxon signed rank test is employed to investigate which countries achieve a breakthrough in winning their first medals and to determine the cor- responding probabilities. Furthermore, Spearman correlation coefficients and SHAP are utilized to conduct relationship and importance analyses. Finally, a DID approach is ap- plied to examine the "great coach" effect and provide new insights. For ease of description and visualization, we have drawn Fig. 1 to represent our work.

<!-- b000054 | heading | pages [3] -->
2 Preparation for Modeling

<!-- b000055 | heading | pages [3] -->
2.1 Model Assumptions

<!-- b000056 | prose | pages [3] -->
Some fundamental assumptions are listed below.

<!-- b000057 | prose | pages [3, 4] -->
• Assumption 1: Athletes are in optimal physical condition throughout the competi- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m + +

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

<!-- b000352 | furniture | pages [3] -->
m

<!-- b000353 | furniture | pages [3] -->
m

<!-- b000354 | furniture | pages [3] -->
m

<!-- b000355 | furniture | pages [3] -->
m

<!-- b000356 | furniture | pages [3] -->
m

<!-- b000357 | furniture | pages [3] -->
m

<!-- b000358 | furniture | pages [3] -->
m

<!-- b000359 | furniture | pages [3] -->
m

<!-- b000360 | furniture | pages [3] -->
m

<!-- b000361 | furniture | pages [3] -->
m

<!-- b000362 | furniture | pages [3] -->
m

<!-- b000363 | furniture | pages [3] -->
m

<!-- b000364 | furniture | pages [3] -->
m

<!-- b000365 | furniture | pages [3] -->
m

<!-- b000366 | furniture | pages [3] -->
m

<!-- b000367 | furniture | pages [3] -->
m

<!-- b000368 | furniture | pages [3] -->
m

<!-- b000369 | furniture | pages [3] -->
m

<!-- b000370 | furniture | pages [3] -->
m

<!-- b000371 | furniture | pages [3] -->
m

<!-- b000372 | furniture | pages [3] -->
m

<!-- b000373 | furniture | pages [3] -->
m

<!-- b000374 | furniture | pages [3] -->
m

<!-- b000375 | furniture | pages [3] -->
m

<!-- b000376 | furniture | pages [3] -->
m

<!-- b000377 | furniture | pages [3] -->
m

<!-- b000378 | furniture | pages [3] -->
m

<!-- b000379 | furniture | pages [3] -->
m

<!-- b000380 | furniture | pages [3] -->
m

<!-- b000381 | furniture | pages [3] -->
m

<!-- b000382 | furniture | pages [4] -->
Team # 2500759

<!-- b000383 | furniture | pages [4] -->
Page 4 of 26

<!-- b000385 | prose | pages [4] -->
Prepare Task 2 Task 1 Data collection Prediction Intervals for Gold and Medal Counts in the 2028 Olympics Probability Estimation Data pre-processing for à "Zero PCA for Redundant Breakthrough" LSTM for Trend XGBoost-Bootstrap Feature Elimination Prediction Model Incorporation P-value for Assessing Achie vement and Estimating Accuracy and Robustness Assessment of the Prediction Model Probability Left-sided Rank Sum Test 10-Fold Cross-Validation Evaluation Me trics & - R-squared Line Plot with Location Parameter (RMSE, MAE, etc.)

<!-- b000386 | prose | pages [4] -->
Theta - 1

<!-- b000387 | prose | pages [4] -->
Y + + Final Task 3 Task 4 &5 Cross fusion Advice for Corre lation and IOC Importance Analysis New DID Model Spearman's Correlation Insights Coefficient & SHAP Analysis Tools

<!-- b000388 | caption | pages [4] -->
Figure 1: The Flow Chart of Our Work

<!-- b000389 | prose | pages [4] -->
tion and their performance is solely influenced by competitive factors.

<!-- b000390 | prose | pages [4] -->
→ Justification: We assume that athletes will compete in peak condition, with per- formance primarily driven by training and competition, excluding factors such as injuries or external disturbances.

<!-- b000391 | prose | pages [4] -->
• Assumption 2: A country's past Olympic performance is a reliable indicator of future medal counts, and the host country tends to perform better due to home-field advantages.

<!-- b000392 | prose | pages [4] -->
→ Justification: We assume that historical performance reflects long-term trends in national sports development, and that host countries benefit from support from local spectators and familiarity with the competition environment.

<!-- b000393 | heading | pages [4] -->
2.2 Notations

<!-- b000394 | caption | pages [4] -->
Table 1: The List of Notation

<!-- b000395 | heading | pages [4] -->
Symbol

<!-- b000396 | prose | pages [4] -->
Definition Each country's home advantage coefficient αc pi The host advantage coefficient β₀ Intercept, the baseline medal count for the control group β1 The difference between the treatment and control groups β2 The overall change in medal counts from 2020 to 2024 β3 Contribution coefficient Xit Control variable matrix Coefficient of Xit γ Random error term €it Prept The preparatory period effect Threati Dummy variable indicating coach change, 1 if changed, 0 otherwise Post Time dummy variable, 1 if the Olympic year is 2024, 0 otherwise

<!-- b000397 | heading | pages [4] -->
2.3 Data Preprocessing

<!-- b000398 | prose | pages [4] -->
Overviewing the five attachments provided in this study, "data_dictionary", etc and synthesizing the information regarding medal predictions, event counts, and types,one

<!-- b000399 | prose | pages [4, 5] -->
关注数学模型 can observe that the scale of information constitutes a small dataset. However, the data is lengthy and complex, with intricate relationships among different data points, represent- ing a type of data pertinent to decision-making in real-world scenarios.

<!-- b000400 | furniture | pages [4] -->
获取更多资讯

<!-- b000401 | furniture | pages [5] -->
Team # 2500759

<!-- b000402 | furniture | pages [5] -->
Page 5 of 26

<!-- b000404 | prose | pages [5] -->
• For attachment 2, we will perform a natural join with the "summerOly_medal_counts" dataset to match the columns for country names and their abbreviations, thereby en- hancing the information provided.

<!-- b000405 | prose | pages [5] -->
• During the data aggregation process, we will retrieve and consolidate data from attachment 2 based on the fields "Team," "Year," "Sport," and "Medal," calculating the medal counts for each country in every Olympic event. Furthermore, we will merge and compute data for various sports across different years, thereby deriving the types and counts of events for each Olympic Games, which will provide vital 微信公众号：数学模型 data support for subsequent medal predictions and trend analysis.

<!-- b000406 | prose | pages [5] -->
• For attachment 5, we will address missing values in the columns "Code," "Sports Governing Body," and "Year" through interpolation methods and by removing rows or columns that contain missing values.

<!-- b000407 | heading | pages [5] -->
3 Problem 1: Medal Prediction

<!-- b000408 | prose | pages [5] -->
This study focuses on predicting medal counts for the 2028 Los Angeles Olympic Games. By considering the interval prediction of medal rankings and recognizing the memoryless characteristic of Olympic medal trends akin to Markov chains, we employ an 微信号：MATHmodels innovative XGBoost5 algorithm enhanced by PCA8,9 and LSTM3,7 to model predictions for gold and total medal rankings while assessing model uncertainty. Using the PCA- LSTM-enhanced dataset from 2024, we derive predictive intervals for the gold and total medals by country for 2028, facilitating performance prediction analysis.

<!-- b000409 | prose | pages [5] -->
In terms of predicting the probability of nations "breaking the zero" for gold medals, we analyze the interval prediction results from XGBoost. We perform a symmetric rank sum test on Bootstrap samples where point estimates are greater than or equal to 1, con- cluding that countries with a P-value less than 0.05 are likely to achieve at least one gold medal in 2028.

<!-- b000410 | prose | pages [5] -->
Additionally, we examine the correlation and importance of different Olympic events in relation to countries’ medal counts. We start with a Spearman correlation analysis be- tween gold and total medal counts for each country in 2024 and the weighted values of key Olympic events. Building on our PCA-LSTM-enhanced XGBoost model, we utilize SHAP analysis to assess the importance of each sport based on principal component im- portance values. Univariate dependence plots further explore the relationships between individual sports and overall gold and medal counts, while SHAP force plots provide insights into the interrelationships and significance of different sports within nations re- garding their gold and total medal counts.

<!-- b000411 | heading | pages [5] -->
3.1 Medal Ranking

<!-- b000412 | heading | pages [5] -->
3.1.1 PCA: Reducing Dimensions

<!-- b000413 | prose | pages [5, 6] -->
In predicting Olympic gold medals and rankings, outcomes are closely linked to the medal counts and compositions from previous Games. Thus, we weighted the gold, silver, and bronze medals of each country in major sporting events at 50%, 30%, and 20%, respectively, to assess their potential impact on future medal standings. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Principal Component Analysis (PCA) was employed to reduce the dimensionality of the weighted medal count dataset across 45 sporting events. This approach effec- tively addresses multicollinearity among original metrics by utilizing uncorrelated prin- cipal components, thereby eliminating redundancy and improving the convergence speed and accuracy of subsequent algorithms. Subsequently, Figs. 2(a)-(b) illustrate the first two dimensions of the PCA results.

<!-- b000414 | furniture | pages [5] -->
m

<!-- b000415 | furniture | pages [5] -->
m

<!-- b000416 | furniture | pages [5] -->
m

<!-- b000417 | furniture | pages [5] -->
m

<!-- b000418 | furniture | pages [5] -->
m

<!-- b000419 | furniture | pages [5] -->
m

<!-- b000420 | furniture | pages [5] -->
m

<!-- b000421 | furniture | pages [5] -->
m

<!-- b000422 | furniture | pages [5] -->
m

<!-- b000423 | furniture | pages [5] -->
m

<!-- b000424 | furniture | pages [5] -->
m

<!-- b000425 | furniture | pages [5] -->
m

<!-- b000426 | furniture | pages [5] -->
m

<!-- b000427 | furniture | pages [5] -->
m

<!-- b000428 | furniture | pages [5] -->
m

<!-- b000429 | furniture | pages [5] -->
m

<!-- b000430 | furniture | pages [5] -->
m

<!-- b000431 | furniture | pages [5] -->
m

<!-- b000432 | furniture | pages [5] -->
m

<!-- b000433 | furniture | pages [5] -->
m

<!-- b000434 | furniture | pages [5] -->
m

<!-- b000435 | furniture | pages [5] -->
m

<!-- b000436 | furniture | pages [5] -->
m

<!-- b000437 | furniture | pages [5] -->
m

<!-- b000438 | furniture | pages [5] -->
m

<!-- b000439 | furniture | pages [5] -->
m

<!-- b000440 | furniture | pages [5] -->
m

<!-- b000441 | furniture | pages [5] -->
m

<!-- b000442 | furniture | pages [5] -->
m

<!-- b000443 | furniture | pages [5] -->
m

<!-- b000444 | furniture | pages [5] -->
m

<!-- b000445 | furniture | pages [5] -->
m

<!-- b000446 | furniture | pages [5] -->
m

<!-- b000447 | furniture | pages [5] -->
m

<!-- b000448 | furniture | pages [5] -->
m

<!-- b000449 | furniture | pages [5] -->
m

<!-- b000450 | furniture | pages [5] -->
m

<!-- b000451 | furniture | pages [5] -->
m

<!-- b000452 | furniture | pages [5] -->
m

<!-- b000453 | furniture | pages [5] -->
m

<!-- b000454 | furniture | pages [5] -->
m

<!-- b000455 | furniture | pages [5] -->
m

<!-- b000456 | furniture | pages [5] -->
m

<!-- b000457 | furniture | pages [5] -->
m

<!-- b000458 | furniture | pages [5] -->
m

<!-- b000459 | furniture | pages [5] -->
m

<!-- b000460 | furniture | pages [5] -->
m

<!-- b000461 | furniture | pages [5] -->
m

<!-- b000462 | furniture | pages [5] -->
m

<!-- b000463 | furniture | pages [5] -->
m

<!-- b000464 | furniture | pages [5] -->
m

<!-- b000465 | furniture | pages [5] -->
m

<!-- b000466 | furniture | pages [5] -->
m

<!-- b000467 | furniture | pages [5] -->
m

<!-- b000468 | furniture | pages [5] -->
m

<!-- b000469 | furniture | pages [5] -->
m

<!-- b000470 | furniture | pages [5] -->
m

<!-- b000471 | furniture | pages [5] -->
m

<!-- b000472 | furniture | pages [5] -->
m

<!-- b000473 | furniture | pages [5] -->
m

<!-- b000474 | furniture | pages [5] -->
m

<!-- b000475 | furniture | pages [5] -->
m

<!-- b000476 | furniture | pages [5] -->
m

<!-- b000477 | furniture | pages [5] -->
m

<!-- b000478 | furniture | pages [5] -->
m

<!-- b000479 | furniture | pages [5] -->
m

<!-- b000480 | furniture | pages [5] -->
m

<!-- b000481 | furniture | pages [5] -->
m

<!-- b000482 | furniture | pages [5] -->
m

<!-- b000483 | furniture | pages [5] -->
m

<!-- b000484 | furniture | pages [5] -->
m

<!-- b000485 | furniture | pages [5] -->
m

<!-- b000486 | furniture | pages [5] -->
m

<!-- b000487 | furniture | pages [5] -->
m

<!-- b000488 | furniture | pages [5] -->
m

<!-- b000489 | furniture | pages [5] -->
m

<!-- b000490 | furniture | pages [5] -->
m

<!-- b000491 | furniture | pages [5] -->
m

<!-- b000492 | furniture | pages [5] -->
m

<!-- b000493 | furniture | pages [5] -->
m

<!-- b000494 | furniture | pages [5] -->
m

<!-- b000495 | furniture | pages [5] -->
m

<!-- b000496 | furniture | pages [5] -->
m

<!-- b000497 | furniture | pages [5] -->
m

<!-- b000498 | furniture | pages [5] -->
m

<!-- b000499 | furniture | pages [5] -->
m

<!-- b000500 | furniture | pages [5] -->
m

<!-- b000501 | furniture | pages [5] -->
m

<!-- b000502 | furniture | pages [5] -->
m

<!-- b000503 | furniture | pages [5] -->
m

<!-- b000504 | furniture | pages [5] -->
m

<!-- b000505 | furniture | pages [5] -->
m

<!-- b000506 | furniture | pages [5] -->
m

<!-- b000507 | furniture | pages [5] -->
m

<!-- b000508 | furniture | pages [5] -->
m

<!-- b000509 | furniture | pages [5] -->
m

<!-- b000510 | furniture | pages [5] -->
m

<!-- b000511 | furniture | pages [5] -->
m

<!-- b000512 | furniture | pages [5] -->
m

<!-- b000513 | furniture | pages [5] -->
m

<!-- b000514 | furniture | pages [5] -->
m

<!-- b000515 | furniture | pages [5] -->
m

<!-- b000516 | furniture | pages [5] -->
m

<!-- b000517 | furniture | pages [5] -->
m

<!-- b000518 | furniture | pages [5] -->
m

<!-- b000519 | furniture | pages [5] -->
m

<!-- b000520 | furniture | pages [5] -->
m

<!-- b000521 | furniture | pages [5] -->
m

<!-- b000522 | furniture | pages [5] -->
m

<!-- b000523 | furniture | pages [5] -->
m

<!-- b000524 | furniture | pages [5] -->
m

<!-- b000525 | furniture | pages [5] -->
m

<!-- b000526 | furniture | pages [5] -->
m

<!-- b000527 | furniture | pages [5] -->
m

<!-- b000528 | furniture | pages [5] -->
m

<!-- b000529 | furniture | pages [5] -->
m

<!-- b000530 | furniture | pages [5] -->
m

<!-- b000531 | furniture | pages [5] -->
m

<!-- b000532 | furniture | pages [5] -->
m

<!-- b000533 | furniture | pages [5] -->
m

<!-- b000534 | furniture | pages [5] -->
m

<!-- b000535 | furniture | pages [5] -->
m

<!-- b000536 | furniture | pages [5] -->
m

<!-- b000537 | furniture | pages [5] -->
m

<!-- b000538 | furniture | pages [5] -->
m

<!-- b000539 | furniture | pages [5] -->
m

<!-- b000540 | furniture | pages [5] -->
m

<!-- b000541 | furniture | pages [5] -->
m

<!-- b000542 | furniture | pages [5] -->
m

<!-- b000543 | furniture | pages [5] -->
m

<!-- b000544 | furniture | pages [5] -->
m

<!-- b000545 | furniture | pages [5] -->
m

<!-- b000546 | furniture | pages [5] -->
m

<!-- b000547 | furniture | pages [5] -->
m

<!-- b000548 | furniture | pages [5] -->
m

<!-- b000549 | furniture | pages [5] -->
m

<!-- b000550 | furniture | pages [5] -->
m

<!-- b000551 | furniture | pages [5] -->
m

<!-- b000552 | furniture | pages [5] -->
m

<!-- b000553 | furniture | pages [5] -->
m

<!-- b000554 | furniture | pages [5] -->
m

<!-- b000555 | furniture | pages [5] -->
m

<!-- b000556 | furniture | pages [5] -->
m

<!-- b000557 | furniture | pages [5] -->
m

<!-- b000558 | furniture | pages [5] -->
m

<!-- b000559 | furniture | pages [5] -->
m

<!-- b000560 | furniture | pages [5] -->
m

<!-- b000561 | furniture | pages [5] -->
m

<!-- b000562 | furniture | pages [5] -->
m

<!-- b000563 | furniture | pages [5] -->
m

<!-- b000564 | furniture | pages [5] -->
m

<!-- b000565 | furniture | pages [5] -->
m

<!-- b000566 | furniture | pages [5] -->
m

<!-- b000567 | furniture | pages [5] -->
m

<!-- b000568 | furniture | pages [5] -->
m

<!-- b000569 | furniture | pages [5] -->
m

<!-- b000570 | furniture | pages [5] -->
m

<!-- b000571 | furniture | pages [5] -->
m

<!-- b000572 | furniture | pages [5] -->
m

<!-- b000573 | furniture | pages [5] -->
m

<!-- b000574 | furniture | pages [5] -->
m

<!-- b000575 | furniture | pages [5] -->
m

<!-- b000576 | furniture | pages [5] -->
m

<!-- b000577 | furniture | pages [5] -->
m

<!-- b000578 | furniture | pages [5] -->
m

<!-- b000579 | furniture | pages [5] -->
m

<!-- b000580 | furniture | pages [5] -->
m

<!-- b000581 | furniture | pages [5] -->
m

<!-- b000582 | furniture | pages [5] -->
m

<!-- b000583 | furniture | pages [5] -->
m

<!-- b000584 | furniture | pages [5] -->
m

<!-- b000585 | furniture | pages [5] -->
m

<!-- b000586 | furniture | pages [5] -->
m

<!-- b000587 | furniture | pages [5] -->
m

<!-- b000588 | furniture | pages [5] -->
m

<!-- b000589 | furniture | pages [5] -->
m

<!-- b000590 | furniture | pages [5] -->
m

<!-- b000591 | furniture | pages [5] -->
m

<!-- b000592 | furniture | pages [5] -->
m

<!-- b000593 | furniture | pages [5] -->
m

<!-- b000594 | furniture | pages [5] -->
m

<!-- b000595 | furniture | pages [5] -->
m

<!-- b000596 | furniture | pages [5] -->
m

<!-- b000597 | furniture | pages [5] -->
m

<!-- b000598 | furniture | pages [5] -->
m

<!-- b000599 | furniture | pages [5] -->
m

<!-- b000600 | furniture | pages [5] -->
m

<!-- b000601 | furniture | pages [5] -->
m

<!-- b000602 | furniture | pages [5] -->
m

<!-- b000603 | furniture | pages [5] -->
m

<!-- b000604 | furniture | pages [5] -->
m

<!-- b000605 | furniture | pages [5] -->
m

<!-- b000606 | furniture | pages [5] -->
m

<!-- b000607 | furniture | pages [5] -->
m

<!-- b000608 | furniture | pages [5] -->
m

<!-- b000609 | furniture | pages [5] -->
m

<!-- b000610 | furniture | pages [5] -->
m

<!-- b000611 | furniture | pages [5] -->
m

<!-- b000612 | furniture | pages [5] -->
m

<!-- b000613 | furniture | pages [5] -->
m

<!-- b000614 | furniture | pages [5] -->
m

<!-- b000615 | furniture | pages [5] -->
m

<!-- b000616 | furniture | pages [5] -->
m

<!-- b000617 | furniture | pages [5] -->
m

<!-- b000618 | furniture | pages [5] -->
m

<!-- b000619 | furniture | pages [5] -->
m

<!-- b000620 | furniture | pages [5] -->
m

<!-- b000621 | furniture | pages [5] -->
m

<!-- b000622 | furniture | pages [5] -->
m

<!-- b000623 | furniture | pages [5] -->
m

<!-- b000624 | furniture | pages [5] -->
m

<!-- b000625 | furniture | pages [5] -->
m

<!-- b000626 | furniture | pages [5] -->
m

<!-- b000627 | furniture | pages [5] -->
m

<!-- b000628 | furniture | pages [5] -->
m

<!-- b000629 | furniture | pages [5] -->
m

<!-- b000630 | furniture | pages [5] -->
m

<!-- b000631 | furniture | pages [5] -->
m

<!-- b000632 | furniture | pages [5] -->
m

<!-- b000633 | furniture | pages [5] -->
m

<!-- b000634 | furniture | pages [5] -->
m

<!-- b000635 | furniture | pages [5] -->
m

<!-- b000636 | furniture | pages [5] -->
m

<!-- b000637 | furniture | pages [5] -->
m

<!-- b000638 | furniture | pages [5] -->
m

<!-- b000639 | furniture | pages [5] -->
m

<!-- b000640 | furniture | pages [5] -->
m

<!-- b000641 | furniture | pages [5] -->
m

<!-- b000642 | furniture | pages [5] -->
m

<!-- b000643 | furniture | pages [5] -->
m

<!-- b000644 | furniture | pages [5] -->
m

<!-- b000645 | furniture | pages [5] -->
m

<!-- b000646 | furniture | pages [5] -->
m

<!-- b000647 | furniture | pages [5] -->
m

<!-- b000648 | furniture | pages [5] -->
m

<!-- b000649 | furniture | pages [5] -->
m

<!-- b000650 | furniture | pages [5] -->
m

<!-- b000651 | furniture | pages [5] -->
m

<!-- b000652 | furniture | pages [5] -->
m

<!-- b000653 | furniture | pages [5] -->
m

<!-- b000654 | furniture | pages [5] -->
m

<!-- b000655 | furniture | pages [5] -->
m

<!-- b000656 | furniture | pages [5] -->
m

<!-- b000657 | furniture | pages [5] -->
m

<!-- b000658 | furniture | pages [5] -->
m

<!-- b000659 | furniture | pages [5] -->
m

<!-- b000660 | furniture | pages [5] -->
m

<!-- b000661 | furniture | pages [5] -->
m

<!-- b000662 | furniture | pages [5] -->
m

<!-- b000663 | furniture | pages [5] -->
m

<!-- b000664 | furniture | pages [5] -->
m

<!-- b000665 | furniture | pages [5] -->
m

<!-- b000666 | furniture | pages [5] -->
m

<!-- b000667 | furniture | pages [5] -->
m

<!-- b000668 | furniture | pages [5] -->
m

<!-- b000669 | furniture | pages [5] -->
m

<!-- b000670 | furniture | pages [5] -->
m

<!-- b000671 | furniture | pages [5] -->
m

<!-- b000672 | furniture | pages [5] -->
m

<!-- b000673 | furniture | pages [5] -->
m

<!-- b000674 | furniture | pages [5] -->
m

<!-- b000675 | furniture | pages [5] -->
m

<!-- b000676 | furniture | pages [5] -->
m

<!-- b000677 | furniture | pages [5] -->
m

<!-- b000678 | furniture | pages [5] -->
m

<!-- b000679 | furniture | pages [5] -->
m

<!-- b000680 | furniture | pages [5] -->
m

<!-- b000681 | furniture | pages [5] -->
m

<!-- b000682 | furniture | pages [5] -->
m

<!-- b000683 | furniture | pages [5] -->
m

<!-- b000684 | furniture | pages [5] -->
m

<!-- b000685 | furniture | pages [5] -->
m

<!-- b000686 | furniture | pages [5] -->
m

<!-- b000687 | furniture | pages [5] -->
m

<!-- b000688 | furniture | pages [5] -->
m

<!-- b000689 | furniture | pages [5] -->
m

<!-- b000690 | furniture | pages [5] -->
m

<!-- b000691 | furniture | pages [5] -->
m

<!-- b000692 | furniture | pages [5] -->
m

<!-- b000693 | furniture | pages [5] -->
m

<!-- b000694 | furniture | pages [5] -->
m

<!-- b000695 | furniture | pages [5] -->
m

<!-- b000696 | furniture | pages [5] -->
m

<!-- b000697 | furniture | pages [5] -->
m

<!-- b000698 | furniture | pages [5] -->
m

<!-- b000699 | furniture | pages [5] -->
m

<!-- b000700 | furniture | pages [5] -->
m

<!-- b000701 | furniture | pages [5] -->
m

<!-- b000702 | furniture | pages [5] -->
m

<!-- b000703 | furniture | pages [5] -->
m

<!-- b000704 | furniture | pages [5] -->
m

<!-- b000705 | furniture | pages [5] -->
m

<!-- b000706 | furniture | pages [5] -->
m

<!-- b000707 | furniture | pages [5] -->
m

<!-- b000708 | furniture | pages [5] -->
m

<!-- b000709 | furniture | pages [5] -->
m

<!-- b000710 | furniture | pages [5] -->
m

<!-- b000711 | furniture | pages [5] -->
m

<!-- b000712 | furniture | pages [5] -->
m

<!-- b000713 | furniture | pages [5] -->
m

<!-- b000714 | furniture | pages [5] -->
m

<!-- b000715 | furniture | pages [5] -->
m

<!-- b000716 | furniture | pages [5] -->
m

<!-- b000717 | furniture | pages [5] -->
m

<!-- b000718 | furniture | pages [5] -->
m

<!-- b000719 | furniture | pages [5] -->
m

<!-- b000720 | furniture | pages [5] -->
m

<!-- b000721 | furniture | pages [5] -->
m

<!-- b000722 | furniture | pages [5] -->
m

<!-- b000723 | furniture | pages [5] -->
m

<!-- b000724 | furniture | pages [5] -->
m

<!-- b000725 | furniture | pages [5] -->
m

<!-- b000726 | furniture | pages [5] -->
m

<!-- b000727 | furniture | pages [5] -->
m

<!-- b000728 | furniture | pages [5] -->
m

<!-- b000729 | furniture | pages [5] -->
m

<!-- b000730 | furniture | pages [5] -->
m

<!-- b000731 | furniture | pages [5] -->
m

<!-- b000732 | furniture | pages [5] -->
m

<!-- b000733 | furniture | pages [5] -->
m

<!-- b000734 | furniture | pages [5] -->
m

<!-- b000735 | furniture | pages [5] -->
m

<!-- b000736 | furniture | pages [5] -->
m

<!-- b000737 | furniture | pages [5] -->
m

<!-- b000738 | furniture | pages [6] -->
Team # 2500759

<!-- b000739 | furniture | pages [6] -->
Page 6 of 26

<!-- b000741 | prose | pages [6] -->
(a) (b)

<!-- b000742 | caption | pages [6] -->
Figure 2: PCA Bioplot

<!-- b000743 | prose | pages [6] -->
In the five-dimensional principal components, the cumulative variance contributions reach 76.4%, effectively capturing most characteristics of the original data. This indicates that data can be reduced to five dimensions for analysis. Fig. 2(b) shows that shooting has the highest score on the principal components, indicating its significant influence among events. Following shooting, swimming, athletics, and wrestling also exhibit no- table medal weights. The remaining events cluster distinctly, likely due to their correlated medal weights. Collectively, swimming, athletics, wrestling, shooting, rhythmic gym- nastics, boxing, and diving significantly impact PC1, suggesting it represents a principal component for major sports. Conversely, the other components (PC2 to PC5) are influ- enced by fewer variables. This analysis yields five principal component characteristics regarding medal weights of sporting events at the 2020 Olympics through PCA dimen- sionality reduction.

<!-- b000744 | heading | pages [6] -->
3.1.2 LSTM: Trends Based on Time

<!-- b000745 | prose | pages [6] -->
Predicting the Olympic medal tally can be framed as a time series forecasting prob- lem, as countries’ medal counts show temporal continuity. Strong sports powers often maintain high medal counts, while emerging nations may experience short-term break- throughs. Thus, the model must capture patterns and long-term trends across different Olympic Games.

<!-- b000746 | prose | pages [6] -->
LSTM is advantageous for handling long-range dependencies in time series data. For instance, if a country’s medal count has steadily increased over the last three Games, LSTM can identify this trend to predict further increases. The four-year gap between Olympics makes traditional models less effective; however, LSTM’s gating mechanisms help retain essential historical information, improving prediction accuracy.

<!-- b000747 | prose | pages [6, 7] -->
Additionally, Olympic medal data can be noisy, with some countries showing incon- sistent performances. LSTM mitigates this noise by learning broader trends. It can also incorporate extra features like host country metrics to enhance predictions. To tackle data m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m sparsity, especially for smaller nations with limited data points, we have implemented a m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m regularization technique. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The process of constructing the LSTM model is as follows. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 • Feature design Each country's home advantage coefficient αc is estimated through regression based on historical data, normalized to serve as weights:

<!-- b000748 | furniture | pages [6] -->
2

<!-- b000749 | furniture | pages [6] -->
MATHmodels

<!-- b000750 | furniture | pages [6] -->
获取更多资讯

<!-- b000751 | furniture | pages [7] -->
Team # 2500759

<!-- b000752 | furniture | pages [7] -->
Page 7 of 26

<!-- b000754 | prose | pages [7] -->
Goldhost t − Goldavg (1) C αc 二 Goldavg

<!-- b000755 | prose | pages [7] -->
A binary variable Hostt ∈ {0, 1} is utilized to indicate whether the country is the host for the year t. A preparatory period effect is introduced to capture the impact of increased investments during the preparation phase:

<!-- b000756 | prose | pages [7] -->
if t ∈ [thost − 8, thost] 1 Prept = (2) otherwise 0

<!-- b000757 | prose | pages [7] -->
where thost denotes the year of hosting, and 8 is equivalent to two Olympic cycles.

<!-- b000758 | prose | pages [7] -->
• Input feature reconstruction The input vector for each time step is expanded to:

<!-- b000759 | prose | pages [7] -->
(3) xt = [Goldt, Totalt, Host, Prept, αc]

<!-- b000760 | prose | pages [7] -->
• Time series modeling and feature fusion A dual-channel LSTM structure is employed to separately process the medal se- quence and home advantage features, with a final fusion for prediction: C4a) ● (1=x [-l (])   = o 1nsteps host = LSTMhost ([Host_k, PrePt−k,αc]k=1) 1nsteps (4b) Ît = FC (hmedal ⊕ hhost) (4c)

<!-- b000761 | prose | pages [7] -->
where nsteps = 3, represents using data from the last three Olympics.  represents vector concatenation, FC denotes a fully connected layer and Ît is the predictions.

<!-- b000762 | prose | pages [7] -->
• Loss function and joint optimization A hierarchical loss function is designed to constrain medal predictions and home advantage identification separately:

<!-- b000763 | prose | pages [7] -->
L = λ1Lmedal + λ2Lhost (5a) N ∑((yGld 1 ygold 2 + (yTotal 1− yTotal 2) Lmedal (5b) N ● i=1 N 1 (5c) Lhost

<!-- b000764 | prose | pages [7] -->
where λ1 = 0.7, λ2 = 0.3, pi = 0.1.

<!-- b000765 | prose | pages [7, 8] -->
In the tuning process for the LSTM model, we primarily focused on two parame- ters: the number of neurons in the hidden layer (hidden_size) and the number of epochs allowed for early stopping (patience). We employed WMAE_Gold and WMAE_Total (Equation 6) as comparative metrics, starting with a constant hidden_size to conduct our comparisons. As illustrated in Figs. 3(a) and 3(d) (circle is the minimum of error), the optimal configuration is 32×6. Figs. 3(b) and 3(e) indicate that both 64×8 and 64×10 meet the objective; however, in Fig. 3(b), the model with 64×8 demonstrates a more sig- nificant reduction in error compared to the other parameter settings, leading us to select 64×8. Figs. 3(c) and 3(f) reveal that 128×10 exhibits the best performance.

<!-- b000766 | furniture | pages [8] -->
Team # 2500759

<!-- b000767 | furniture | pages [8] -->
Page 8 of 26

<!-- b000769 | prose | pages [8] -->
Subsequently, we conducted a direct comparison of these three models. As shown in Fig. 4, the performance of the configurations 32×6 and 128×10 is quite similar; nonethe- less, the overall error for 128×10 is lower. Therefore, we ultimately determined the pa- rameters to be hidden_size=128 and patience=10. This selection provides critical trends measures for subsequent research involving XGBoost.

<!-- b000770 | prose | pages [8] -->
P wc|yc −ˆyc| P wc WMAE_Gold or Total = (6)

<!-- b000771 | prose | pages [8] -->
where wc is the weight of country c’s gold medals or total medals, yc is the true and ˆyc is the prediction.

<!-- b000772 | prose | pages [8] -->
(a) (b) (c)

<!-- b000773 | prose | pages [8] -->
(d) (e) (f)

<!-- b000774 | caption | pages [8] -->
Figure 3: Variations in Parameter Tuning of WMAE_Gold and WMAE_Total

<!-- b000775 | caption | pages [8] -->
Figure 4: Comparison on Hidden_size

<!-- b000776 | prose | pages [8] -->
关注数学模型

<!-- b000777 | furniture | pages [8] -->
2

<!-- b000778 | furniture | pages [8] -->
MATHmodels

<!-- b000779 | furniture | pages [8] -->
获取更多资讯

<!-- b000780 | furniture | pages [9] -->
Team # 2500759

<!-- b000781 | furniture | pages [9] -->
Page 9 of 26

<!-- b000782 | heading | pages [9] -->
3.1.3 XGBoost-Bootstrap Modeling

<!-- b000783 | prose | pages [9] -->
Based on the aforementioned PCA dimensionality reduction and LSTM trend mea- surement, we obtain the input data for XGBoost. Subsequently, we construct XGBoost prediction models based on gold medal counts and total medal counts, respectively. A key aspect of this model (Fig. 5) is the construction of a relatively optimal XGBoost model through 10-fold cross-validation grid parameter tuning, along with the estimation of con- fidence intervals for medal prediction values using the Bootstrap resampling strategy.

<!-- b000784 | prose | pages [9] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000785 | caption | pages [9] -->
Figure 5: Schematic of XGBoost-Bootstrap

<!-- b000786 | prose | pages [9] -->
XGBoost is an ensemble learning algorithm based on gradient-boosted trees, which centers on the incremental and parallel optimization of the loss function by constructing multiple CART base classifiers. It employs a second-order Taylor expansion of the ob- jective function, enhancing the efficiency of gradient descent while incorporating regular- ization into the objective function to effectively prevent model overfitting. This algorithm aims to leverage these features to elucidate the nonlinear relationships among gold medal counts, total medal counts, home advantage, weighted values for individual sport medals, and medal trend values. The objective function is Equation 7.

<!-- b000787 | prose | pages [9] -->
n K X X L(θ) = l(yi, ˆyi) + Ω(fk) (7) i=1 k=1

<!-- b000788 | prose | pages [9] -->
where l(·) is the loss function, Ω(·) is the regularization term.

<!-- b000789 | prose | pages [9] -->
Bootstrap is a non-parametric resampling method. By employing this approach, we independently run the constructed XGBoost model 1,000 times, allowing us to calculate the 95% confidence interval for each country’s fitted values of gold and total medals based on these iterations.

<!-- b000790 | heading | pages [9] -->
3.1.4 Results Display

<!-- b000791 | prose | pages [9, 10] -->
The hyperparameter tuning of the predictive models employed RMSE as the evalua- tion criterion, aimed at selecting the model with the minimum RMSE value (see section 6.2 for a detailed analysis). During the training of the gold medal prediction model, the optimal combination of model parameters was determined through hyperparameter tun- ing, yielding: nrounds = 75, max_depth = 2, eta = 0.1, gamma = 0.5, colsample_bytree = 1, min_child_weight = 1, and subsample = 0.5. Notably, the subsample parameter re- mained constant throughout the tuning process, set at 0.5 to ensure a reasonable sampling proportion.

<!-- b000792 | furniture | pages [10] -->
Team # 2500759

<!-- b000793 | furniture | pages [10] -->
Page 10 of 26

<!-- b000795 | prose | pages [10] -->
In the training process of the medal prediction model, the only change compared to the gold medal prediction model was the adjustment of the gamma parameter. In this model, the gamma value was set to 0.25 to optimize the model’s predictive ability for the number of medals. Consequently, the relatively optimal XGBoost model was utilized to perform Bootstrap resampling and interval estimation for "the trend values of gold and medal counts for various countries in 2028", "the five principal component dimensions of medal weights for various sports in 2024" and "the estimated home-field effect values for 2028." The results for the top 20 countries in both gold medal counts and total medal counts for the 2028 Los Angeles Olympic Games are illustrated in Figs. 6(a)-(b).

<!-- b000796 | prose | pages [10] -->
(a)

<!-- b000797 | prose | pages [10] -->
(b)

<!-- b000798 | caption | pages [10] -->
Figure 6: Top 20 Predictions for Gold and Medal Counts at 2028 Olympics

<!-- b000799 | prose | pages [10] -->
Based on Figs. 6(a)-(b) and Table 2, it can be observed that as the host country, the United States is projected to see a significant increase in both gold and medal counts for the 2028 Olympic Games. Additionally, countries such as the United Kingdom, Australia, Canada, and Cuba may also experience an increase in their respective gold and medal counts. In contrast, France, the host of the 2024 Olympic Games, is expected to achieve unprecedented results due to home-field advantage, but model predictions suggest that its gold and medal counts will notably decrease in the subsequent Olympic Games. Similarly, countries like China, Italy, South Korea, Japan, and Uzbekistan are also likely to perform poorly in the next Olympic Games.

<!-- b000800 | heading | pages [10] -->
3.2 Breaking the Zero

<!-- b000801 | prose | pages [10] -->
Based on the aforementioned analysis and the criteria for achieving a "breakthrough of zero," we identify the countries projected to achieve at least one gold medal in the 2028

<!-- b000802 | prose | pages [10, 11] -->
关注数学模型 Gold Total

<!-- b000803 | furniture | pages [10] -->
2

<!-- b000804 | furniture | pages [10] -->
MATHmodels

<!-- b000805 | furniture | pages [10] -->
获取更多资讯

<!-- b000806 | furniture | pages [11] -->
Team # 2500759

<!-- b000807 | furniture | pages [11] -->
Page 11 of 26

<!-- b000808 | caption | pages [11] -->
Table 2: Predicted Medal Counts & CI for Top 20 Countries at 2028 Olympics

<!-- b000810 | prose | pages [11] -->
NOC Gold_Pred CI_95% Trend NOC Total_Pred CI_95% Trend

<!-- b000811 | prose | pages [11] -->
↑ ↑ USA 51 (32.08,58.34) USA 133 (79.60,147.35) ↓ ↓ CHN 34 (23.33,40.19) CHN 90 (59.13,103.51) ↑ ↑ AUS 19 (10.41,16.13) GBR 69 (43.12,75.84) ↓ ↓ JPN 17 (11.88,18.80) JPN 55 (38.19,64.94) 微信公众号：数学模型 ↑ ↑ GBR 16 (11.92,19.12) AUS 49 (33.37,63.77) ↓ ↓ FRA 12 (9.00,14.86) FRA 41 (29.86,60.60) ↓ ↑ GER 12 (8.41,14.38) NED 34 (24.58,39.30) ↓ ↓ ITA 11 (7.06,13.03) GER 33 (25.18,48.98) ↓ ↑ NED 11 (6.84,13.18) CAN 29 (21.72,33.68) ↑ ↓ NZL 11 (4.82,9.33) ITA 29 (22.58,34.13) ↑ ↓ CAN 10 (5.73,11.70) KOR 25 (18.08,34.28) ↑ ↑ HUN 8 (5.18,10.87) BRA 21 (14.67,24.32) ↓ ↓ KOR 7 (5.69,9.38) NZL 18 (13.98,23.86) ↓ ↓ BRA 6 (3.70,8.06) HUN 17 (13.00,22.69) ↓ ↑ ESP 5 (3.08,6.72) CUB 15 (10.91,18.57) 微信号：MATHmodels ↑ ↓ UKR 5 (3.39,7.88) ESP 14 (8.84,19.47) ↓ ↑ KEN 5 (2.51,6.01) SWE 12 (7.06,14.99) ↑ ↓ CUB 4 (2.36,5.92) UZB 11 (8.45,13.61) ↓ ↓ UZB 4 (1.96,5.83) KEN 9 (7.63,14.35) ↑ ↓ TPE 4 (2.79,4.53) UKR 9 (6.96,11.12)

<!-- b000812 | prose | pages [11] -->
Olympics as MKD, BFA, TKM, KSA, SMR, and KUW. We will conduct a signed rank test on the point estimates derived from Bootstrap resampling for these countries to sta- tistically assess whether they can achieve this gold medal breakthrough. The significance of these observations will be further elucidated by considering the size of the P-values, which indicate the probability of the events occurring.

<!-- b000813 | prose | pages [11] -->
The decision to utilize the signed rank test, rather than employing a one-sample t-test or defining a binary variable for "having won a gold medal" to apply logistic regression or binary classification machine learning algorithms, is based on the following consider- ations.

<!-- b000814 | prose | pages [11] -->
• The signed rank test is a non-parametric method that does not require any assump- tions regarding the distribution of the underlying population. In contrast, the t-test is a parametric method that assumes that the data originate from a normally dis- tributed population or that the sample itself is normally distributed. As such, the non-parametric test is more aligned with real-world scenarios, thus minimizing the likelihood of substantial errors.

<!-- b000815 | prose | pages [11] -->
• Implementing a binary variable for "winning a gold medal" to design a classification algorithm and calculate the estimated probability of countries achieving a "break- through of zero" would replace the quantitative variable of gold medal counts with a qualitative variable. This approach neglects the correlation between feature vari- ables and may lead to biased and unreasonable results.

<!-- b000816 | prose | pages [11, 12] -->
Given the analysis outlined above, we will employ the signed rank test to statistically determine the significance of the gold medal breakthrough and to provide probability m m m m m m m m m m m m m m m estimates. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1) Hypothesis testing setup Let dij represent the i-th Bootstrap prediction value for the j-th country, and θj denote the symmetric center of the corresponding population. When the final prediction value ˆyj ≥1, we establish a left-sided signed rank test with a location parameter of 1:

<!-- b000817 | furniture | pages [11] -->
m

<!-- b000818 | furniture | pages [11] -->
m

<!-- b000819 | furniture | pages [11] -->
m

<!-- b000820 | furniture | pages [11] -->
m

<!-- b000821 | furniture | pages [11] -->
m

<!-- b000822 | furniture | pages [11] -->
m

<!-- b000823 | furniture | pages [11] -->
m

<!-- b000824 | furniture | pages [11] -->
m

<!-- b000825 | furniture | pages [11] -->
m

<!-- b000826 | furniture | pages [11] -->
m

<!-- b000827 | furniture | pages [11] -->
m

<!-- b000828 | furniture | pages [11] -->
m

<!-- b000829 | furniture | pages [11] -->
m

<!-- b000830 | furniture | pages [11] -->
m

<!-- b000831 | furniture | pages [11] -->
m

<!-- b000832 | furniture | pages [11] -->
m

<!-- b000833 | furniture | pages [11] -->
m

<!-- b000834 | furniture | pages [11] -->
m

<!-- b000835 | furniture | pages [11] -->
m

<!-- b000836 | furniture | pages [11] -->
m

<!-- b000837 | furniture | pages [11] -->
m

<!-- b000838 | furniture | pages [11] -->
m

<!-- b000839 | furniture | pages [11] -->
m

<!-- b000840 | furniture | pages [11] -->
m

<!-- b000841 | furniture | pages [11] -->
m

<!-- b000842 | furniture | pages [11] -->
m

<!-- b000843 | furniture | pages [11] -->
m

<!-- b000844 | furniture | pages [11] -->
m

<!-- b000845 | furniture | pages [11] -->
m

<!-- b000846 | furniture | pages [11] -->
m

<!-- b000847 | furniture | pages [11] -->
m

<!-- b000848 | furniture | pages [11] -->
m

<!-- b000849 | furniture | pages [11] -->
m

<!-- b000850 | furniture | pages [11] -->
m

<!-- b000851 | furniture | pages [11] -->
m

<!-- b000852 | furniture | pages [11] -->
m

<!-- b000853 | furniture | pages [11] -->
m

<!-- b000854 | furniture | pages [11] -->
m

<!-- b000855 | furniture | pages [11] -->
m

<!-- b000856 | furniture | pages [11] -->
m

<!-- b000857 | furniture | pages [11] -->
m

<!-- b000858 | furniture | pages [11] -->
m

<!-- b000859 | furniture | pages [11] -->
m

<!-- b000860 | furniture | pages [11] -->
m

<!-- b000861 | furniture | pages [11] -->
m

<!-- b000862 | furniture | pages [11] -->
m

<!-- b000863 | furniture | pages [11] -->
m

<!-- b000864 | furniture | pages [11] -->
m

<!-- b000865 | furniture | pages [11] -->
m

<!-- b000866 | furniture | pages [11] -->
m

<!-- b000867 | furniture | pages [11] -->
m

<!-- b000868 | furniture | pages [11] -->
m

<!-- b000869 | furniture | pages [11] -->
m

<!-- b000870 | furniture | pages [11] -->
m

<!-- b000871 | furniture | pages [11] -->
m

<!-- b000872 | furniture | pages [11] -->
m

<!-- b000873 | furniture | pages [11] -->
m

<!-- b000874 | furniture | pages [11] -->
m

<!-- b000875 | furniture | pages [11] -->
m

<!-- b000876 | furniture | pages [11] -->
m

<!-- b000877 | furniture | pages [11] -->
m

<!-- b000878 | furniture | pages [11] -->
m

<!-- b000879 | furniture | pages [11] -->
m

<!-- b000880 | furniture | pages [11] -->
m

<!-- b000881 | furniture | pages [11] -->
m

<!-- b000882 | furniture | pages [11] -->
m

<!-- b000883 | furniture | pages [11] -->
m

<!-- b000884 | furniture | pages [11] -->
m

<!-- b000885 | furniture | pages [11] -->
m

<!-- b000886 | furniture | pages [11] -->
m

<!-- b000887 | furniture | pages [11] -->
m

<!-- b000888 | furniture | pages [11] -->
m

<!-- b000889 | furniture | pages [11] -->
m

<!-- b000890 | furniture | pages [11] -->
m

<!-- b000891 | furniture | pages [11] -->
m

<!-- b000892 | furniture | pages [11] -->
m

<!-- b000893 | furniture | pages [11] -->
m

<!-- b000894 | furniture | pages [11] -->
m

<!-- b000895 | furniture | pages [11] -->
m

<!-- b000896 | furniture | pages [11] -->
m

<!-- b000897 | furniture | pages [11] -->
m

<!-- b000898 | furniture | pages [11] -->
m

<!-- b000899 | furniture | pages [11] -->
m

<!-- b000900 | furniture | pages [11] -->
m

<!-- b000901 | furniture | pages [11] -->
m

<!-- b000902 | furniture | pages [11] -->
m

<!-- b000903 | furniture | pages [11] -->
m

<!-- b000904 | furniture | pages [11] -->
m

<!-- b000905 | furniture | pages [11] -->
m

<!-- b000906 | furniture | pages [11] -->
m

<!-- b000907 | furniture | pages [11] -->
m

<!-- b000908 | furniture | pages [11] -->
m

<!-- b000909 | furniture | pages [11] -->
m

<!-- b000910 | furniture | pages [11] -->
m

<!-- b000911 | furniture | pages [11] -->
m

<!-- b000912 | furniture | pages [11] -->
m

<!-- b000913 | furniture | pages [11] -->
m

<!-- b000914 | furniture | pages [11] -->
m

<!-- b000915 | furniture | pages [11] -->
m

<!-- b000916 | furniture | pages [11] -->
m

<!-- b000917 | furniture | pages [11] -->
m

<!-- b000918 | furniture | pages [11] -->
m

<!-- b000919 | furniture | pages [11] -->
m

<!-- b000920 | furniture | pages [11] -->
m

<!-- b000921 | furniture | pages [11] -->
m

<!-- b000922 | furniture | pages [11] -->
m

<!-- b000923 | furniture | pages [11] -->
m

<!-- b000924 | furniture | pages [11] -->
m

<!-- b000925 | furniture | pages [11] -->
m

<!-- b000926 | furniture | pages [11] -->
m

<!-- b000927 | furniture | pages [11] -->
m

<!-- b000928 | furniture | pages [11] -->
m

<!-- b000929 | furniture | pages [11] -->
m

<!-- b000930 | furniture | pages [11] -->
m

<!-- b000931 | furniture | pages [11] -->
m

<!-- b000932 | furniture | pages [11] -->
m

<!-- b000933 | furniture | pages [11] -->
m

<!-- b000934 | furniture | pages [11] -->
m

<!-- b000935 | furniture | pages [11] -->
m

<!-- b000936 | furniture | pages [11] -->
m

<!-- b000937 | furniture | pages [11] -->
m

<!-- b000938 | furniture | pages [11] -->
m

<!-- b000939 | furniture | pages [11] -->
m

<!-- b000940 | furniture | pages [11] -->
m

<!-- b000941 | furniture | pages [11] -->
m

<!-- b000942 | furniture | pages [11] -->
m

<!-- b000943 | furniture | pages [11] -->
m

<!-- b000944 | furniture | pages [11] -->
m

<!-- b000945 | furniture | pages [11] -->
m

<!-- b000946 | furniture | pages [11] -->
m

<!-- b000947 | furniture | pages [11] -->
m

<!-- b000948 | furniture | pages [11] -->
m

<!-- b000949 | furniture | pages [11] -->
m

<!-- b000950 | furniture | pages [11] -->
m

<!-- b000951 | furniture | pages [11] -->
m

<!-- b000952 | furniture | pages [11] -->
m

<!-- b000953 | furniture | pages [11] -->
m

<!-- b000954 | furniture | pages [11] -->
m

<!-- b000955 | furniture | pages [11] -->
m

<!-- b000956 | furniture | pages [11] -->
m

<!-- b000957 | furniture | pages [11] -->
m

<!-- b000958 | furniture | pages [11] -->
m

<!-- b000959 | furniture | pages [11] -->
m

<!-- b000960 | furniture | pages [11] -->
m

<!-- b000961 | furniture | pages [11] -->
m

<!-- b000962 | furniture | pages [11] -->
m

<!-- b000963 | furniture | pages [11] -->
m

<!-- b000964 | furniture | pages [11] -->
m

<!-- b000965 | furniture | pages [11] -->
m

<!-- b000966 | furniture | pages [11] -->
m

<!-- b000967 | furniture | pages [11] -->
m

<!-- b000968 | furniture | pages [11] -->
m

<!-- b000969 | furniture | pages [11] -->
m

<!-- b000970 | furniture | pages [11] -->
m

<!-- b000971 | furniture | pages [11] -->
m

<!-- b000972 | furniture | pages [11] -->
m

<!-- b000973 | furniture | pages [11] -->
m

<!-- b000974 | furniture | pages [11] -->
m

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

<!-- b001141 | furniture | pages [12] -->
Team # 2500759

<!-- b001142 | furniture | pages [12] -->
Page 12 of 26

<!-- b001144 | prose | pages [12] -->
H0 : θj = 1 H1 : θj < 1 vs.

<!-- b001145 | prose | pages [12] -->
2) Data transformation and statistic construction We perform a shift transformation on the original data d∗ ij = dij −1. Next, we compute the absolute value ranks R+ ij<0}(d∗ ij and the indicator variable: uij = I{d∗ ij). After excluding data points where d∗ ij = 0, we construct the signed rank sum statistic:

<!-- b001146 | prose | pages [12] -->
nj X w+ uijR+ j = ij i=1

<!-- b001147 | prose | pages [12] -->
where nj is the adjusted effective sample size.

<!-- b001148 | prose | pages [12] -->
3) Asymptotic distribution theory Under large sample conditions, when the null hypothesis is true, wj follows a normal distribution:

<!-- b001149 | prose | pages [12] -->
L w+ H0 N(µj, σ2 −→ j) j

<!-- b001150 | prose | pages [12] -->
µj = nj(nj + 1) 4 Pk i=1(t3 i −ti) j = nj(nj + 1)(2nj + 1) σ2 − 24 48

<!-- b001151 | prose | pages [12] -->
4) P-value calculation ! w+ j −µj P-value = Φ σj

<!-- b001152 | prose | pages [12] -->
If the P-value is less than or equal to 0.05, falling within the rejection region, it is concluded that the country is statistically unable to achieve a "breakthrough of zero" in gold medals at the 2028 Olympics. Conversely, if the P-value is greater than 0.05, it suggests that the country has a favorable chance of achieving a "breakthrough of zero" in gold medals. Furthermore, a larger P-value indicates a smaller probability of committing a Type II error, thereby increasing the likelihood of realizing the "breakthrough of zero" in gold medals. Based on the model established above, the results of the Wlicoxon signed rank test for the countries aiming to achieve this "breakthrough of zero" in gold medals are illustrated in Fig. 7 and Table 3 .

<!-- b001153 | prose | pages [12] -->
Based on the Table 2 and the gold medal counts from participating countries in 2024, it was determined that eight countries, which did not secure any gold medals in 2024, may potentially achieve a breakthrough in gold medals by 2028. Historical data shows that GHA and GRD achieved a breakthrough of zero gold medals in 1960 and 2012, respectively.

<!-- b001154 | prose | pages [12] -->
From Table 3, we can know only two countries, SMR and KWT, had test statistics corresponding to P-values greater than 0.05, indicating that they did not fall within the

<!-- b001155 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型

<!-- b001156 | furniture | pages [12] -->
2

<!-- b001157 | furniture | pages [12] -->
MATHmodels

<!-- b001158 | furniture | pages [12] -->
获取更多资讯

<!-- b001159 | furniture | pages [13] -->
Team # 2500759

<!-- b001160 | furniture | pages [13] -->
Page 13 of 26

<!-- b001161 | caption | pages [13] -->
Figure 7: Violin-Raincloud Hybrid Plot

<!-- b001163 | caption | pages [13] -->
Table 3: Sign Rank Sum Test Table

<!-- b001164 | prose | pages [13] -->
w+ NOC p pred

<!-- b001165 | prose | pages [13] -->
GRD 538231 1 1 GHA 532048 1 1 SMR 498067 0.847 2 KWT 389859 0.684 1 SAU 222158 0.0011 1 TKM 197115 3.01e-09 1 MKD 153243 1.22e-26 1 微信号：MATHmodels BFA 153243 1.22e-26 1

<!-- b001166 | prose | pages [13] -->
rejection region. This suggests that the predicted gold medal counts for SMR and KWT at the 2028 Olympics are significantly greater than 1, implying that both countries are likely to achieve a “breakthrough of zero” in gold medals, with probabilities of 0.847 and 0.684, respectively.

<!-- b001167 | prose | pages [13] -->
According to Table 3, the predicted gold medal count for SMR at the 2028 Olympics is 2, with a 95% approximate confidence interval of [1, 3], indicating relatively stable predictions. For KWT, the predicted gold medal count is 1, with a 95% approximate confidence interval of [0, 2]. The violin plot in Fig. 7 illustrates that most of the prediction data for KWT falls within the range of 1 to 2.

<!-- b001168 | heading | pages [13] -->
3.3 Olympic Events and Medal Counts

<!-- b001169 | prose | pages [13] -->
We have chosen to utilize SHAP1,10 analysis tools for the correlation analysis and importance measurement between Olympic events and medal counts.

<!-- b001170 | heading | pages [13] -->
3.3.1 Spearman: A Mathematical Analysis

<!-- b001171 | prose | pages [13] -->
The Spearman correlation coefficient is a non-parametric measure of rank correla- tion. In contrast to the Pearson correlation coefficient, which is limited to characterizing linear relationships and requires data to follow a normal distribution, the Spearman corre- lation is computed based on rank orders. This approach makes it less sensitive to outliers and allows for a more robust representation of the degree of correlation between variables.

<!-- b001172 | furniture | pages [14] -->
Team # 2500759

<!-- b001173 | furniture | pages [14] -->
Page 14 of 26

<!-- b001174 | prose | pages [14] -->
The Spearman correlation coefficient is defined mathematically as follows:

<!-- b001175 | prose | pages [14] -->
n 1     X R(xi) −R(x) R(yi) −R(y) n i=1 ρ = (8) v v n n u u t1 t1 2 2   X X u u R(xi) −R(x) · R(yi) −R(y) n n i=1 i=1

<!-- b001176 | prose | pages [14] -->
where R(·) denotes the rank of the variable within the sample.

<!-- b001177 | prose | pages [14] -->
Coming up with hypotheses:

<!-- b001178 | prose | pages [14] -->
H1 : ρ̸ = 0 H0 : ρ = 0 vs.

<!-- b001179 | prose | pages [14] -->
The t-test statistic is constructed, and a judgment is made using the rejection region:

<!-- b001180 | prose | pages [14] -->
|ρ| H0 ∼t(n −2) t = r ρ2 n −2 t > tα(n −2)   m m m m m m m m m m m m m m m m m m m m m m w = (x, y) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Significance t-test is typically conducted at a significance level of 0.05. In this study, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m we calculate the Spearman correlation coefficients and conduct hypothesis testing based m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m on the weighted values of the various sports in the 2024 Paris Olympics in relation to m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001181 | prose | pages [14] -->
the number of gold medals and total medals won by each country. This analysis aims to explore the interrelationships between the different sports and their respective gold and medal counts from a mathematical perspective.

<!-- b001182 | heading | pages [14] -->
3.3.2 SHAP: Revealing Correlations and Importance

<!-- b001183 | prose | pages [14] -->
SHAP is a game theory-based tool that enhances the interpretability of machine learning models. Its core advantages lie in providing consistent, precise, and fair expla- nations. The rationale for selecting SHAP analysis tools to examine the interrelationships and importance of each sport in relation to various countries is as follows:

<!-- b001184 | prose | pages [14] -->
• Explanation of predictive models The fundamental function of SHAP is to compute the contribution of each feature to the final prediction outcome while also indicating the direction of this contribu- tion—positive or negative. Utilizing the beeswarm plot and importance plot, SHAP allows for the quantification of each sport’s significance regarding the number of gold and total medals won, in conjunction with the PCA loading matrix.

<!-- b001185 | prose | pages [14] -->
• Nonlinear processing and feature dependencies SHAP can reveal the nonlinear relationships of each feature within the XGBoost model when multiple features interact. It provides accurate contribution scores for each feature, with univariate dependence plots illustrating the impact of different sports’ principal components on gold and medal counts.

<!-- b001186 | prose | pages [14] -->
• Local and global explanations In addition to the aforementioned analyses, SHAP provides local explanations for

<!-- b001187 | prose | pages [14, 15] -->
关注数学模型 individual samples, allowing for a detailed examination of the degree of contribu- tion from each feature. This facilitates an in-depth analysis of the associations be- tween different sports and various countries. Specifically, by leveraging the SHAP force plot for a single sample, one can observe which sports primarily influence the medal counts of a particular country.

<!-- b001188 | furniture | pages [14] -->
2

<!-- b001189 | furniture | pages [14] -->
MATHmodels

<!-- b001190 | furniture | pages [14] -->
获取更多资讯

<!-- b001191 | furniture | pages [15] -->
Team # 2500759

<!-- b001192 | furniture | pages [15] -->
Page 15 of 26

<!-- b001194 | heading | pages [15] -->
3.3.3 Analysis of Relationships and Importance

<!-- b001195 | prose | pages [15] -->
Based on the formula for the Spearman correlation coefficient and hypothesis test- ing, sports with non-significant correlation coefficients, such as Wrestling, Beach Volley- ball, Handball, Trampoline Gymnastics, and Cycling, were excluded. Fig. 8 illustrates 微信公众号：数学模型 the correlation between gold medals, total medals, and various sports for the 2024 Paris Olympics.

<!-- b001196 | caption | pages [15] -->
Figure 8: Spearman Correlation Coefficient Heatmap

<!-- b001197 | prose | pages [15] -->
微信号：MATHmodels The Spearman correlation analysis reveals several key insights: Sports such as Swim- ming, Athletics, and Shooting demonstrate a strong relationship between gold and total medals, primarily due to their multiple events that enhance medal potential, with strong nations particularly excelling in Swimming and Athletics. Conversely, team sports (e.g., Basketball, Volleyball) and some group sports (e.g., Rowing, Canoeing) exhibit weaker correlations between gold and total medals, as their gold counts are less concentrated despite higher total medal counts attributed to broader participation across nations. Addi- tionally, newly introduced sports like Skateboarding and Karate showcase a lower corre- lation for gold medals (0.210) but a higher correlation for total medals (0.496), indicating a more dispersed gold distribution alongside increased total medals. The growth of these sports likely stems from greater participation and competition, contributing to a more equitable medal distribution overall.

<!-- b001198 | prose | pages [15] -->
The XGBoost prediction model for gold and total medals at the 2028 Olympics, constructed previously, calculates SHAP values based on the training set, resulting in the hexagonal importance mix plot in Fig. 9 for five principal component features. In the gold medal prediction model, the two most important principal components are PC1 (0.8345) and PC2 (0.1055). For the total medal prediction model, the leading components are PC1 (0.6242) and PC5 (0.3024), aligning with the highest variance contribution from PC1. The absolute values of the loadings of individual items on the principal components are then weighted by the importance of the components, summed, and normalized to calculate their significance, as shown in Fig. 10.

<!-- b001199 | prose | pages [15, 16] -->
The PCA and SHAP analysis reveals important insights into sports. Shooting and Gymnastics rank among the top three in gold and total medal significance, emphasizing their vital Olympic roles. Shooting’s diversity and Gymnastics’ strong participation from countries like the USA and China contribute to their rankings. Swimming ranks third in m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001200 | furniture | pages [15] -->
m

<!-- b001201 | furniture | pages [15] -->
m

<!-- b001202 | furniture | pages [15] -->
m

<!-- b001203 | furniture | pages [15] -->
m

<!-- b001204 | furniture | pages [15] -->
m

<!-- b001205 | furniture | pages [15] -->
m

<!-- b001206 | furniture | pages [15] -->
m

<!-- b001207 | furniture | pages [15] -->
m

<!-- b001208 | furniture | pages [15] -->
m

<!-- b001209 | furniture | pages [15] -->
m

<!-- b001210 | furniture | pages [15] -->
m

<!-- b001211 | furniture | pages [15] -->
m

<!-- b001212 | furniture | pages [15] -->
m

<!-- b001213 | furniture | pages [15] -->
m

<!-- b001214 | furniture | pages [15] -->
m

<!-- b001215 | furniture | pages [15] -->
m

<!-- b001216 | furniture | pages [15] -->
m

<!-- b001217 | furniture | pages [15] -->
m

<!-- b001218 | furniture | pages [15] -->
m

<!-- b001219 | furniture | pages [15] -->
m

<!-- b001220 | furniture | pages [15] -->
m

<!-- b001221 | furniture | pages [15] -->
m

<!-- b001222 | furniture | pages [15] -->
m

<!-- b001223 | furniture | pages [15] -->
m

<!-- b001224 | furniture | pages [15] -->
m

<!-- b001225 | furniture | pages [15] -->
m

<!-- b001226 | furniture | pages [15] -->
m

<!-- b001227 | furniture | pages [15] -->
m

<!-- b001228 | furniture | pages [15] -->
m

<!-- b001229 | furniture | pages [15] -->
m

<!-- b001230 | furniture | pages [15] -->
m

<!-- b001231 | furniture | pages [15] -->
m

<!-- b001232 | furniture | pages [15] -->
m

<!-- b001233 | furniture | pages [15] -->
m

<!-- b001234 | furniture | pages [15] -->
m

<!-- b001235 | furniture | pages [15] -->
m

<!-- b001236 | furniture | pages [15] -->
m

<!-- b001237 | furniture | pages [15] -->
m

<!-- b001238 | furniture | pages [15] -->
m

<!-- b001239 | furniture | pages [15] -->
m

<!-- b001240 | furniture | pages [15] -->
m

<!-- b001241 | furniture | pages [15] -->
m

<!-- b001242 | furniture | pages [15] -->
m

<!-- b001243 | furniture | pages [15] -->
m

<!-- b001244 | furniture | pages [15] -->
m

<!-- b001245 | furniture | pages [15] -->
m

<!-- b001246 | furniture | pages [15] -->
m

<!-- b001247 | furniture | pages [15] -->
m

<!-- b001248 | furniture | pages [15] -->
m

<!-- b001249 | furniture | pages [15] -->
m

<!-- b001250 | furniture | pages [15] -->
m

<!-- b001251 | furniture | pages [15] -->
m

<!-- b001252 | furniture | pages [15] -->
m

<!-- b001253 | furniture | pages [15] -->
m

<!-- b001254 | furniture | pages [15] -->
m

<!-- b001255 | furniture | pages [15] -->
m

<!-- b001256 | furniture | pages [15] -->
m

<!-- b001257 | furniture | pages [15] -->
m

<!-- b001258 | furniture | pages [15] -->
m

<!-- b001259 | furniture | pages [15] -->
m

<!-- b001260 | furniture | pages [15] -->
m

<!-- b001261 | furniture | pages [15] -->
m

<!-- b001262 | furniture | pages [15] -->
m

<!-- b001263 | furniture | pages [15] -->
m

<!-- b001264 | furniture | pages [15] -->
m

<!-- b001265 | furniture | pages [15] -->
m

<!-- b001266 | furniture | pages [15] -->
m

<!-- b001267 | furniture | pages [15] -->
m

<!-- b001268 | furniture | pages [15] -->
m

<!-- b001269 | furniture | pages [15] -->
m

<!-- b001270 | furniture | pages [15] -->
m

<!-- b001271 | furniture | pages [15] -->
m

<!-- b001272 | furniture | pages [15] -->
m

<!-- b001273 | furniture | pages [15] -->
m

<!-- b001274 | furniture | pages [15] -->
m

<!-- b001275 | furniture | pages [15] -->
m

<!-- b001276 | furniture | pages [15] -->
m

<!-- b001277 | furniture | pages [15] -->
m

<!-- b001278 | furniture | pages [15] -->
m

<!-- b001279 | furniture | pages [15] -->
m

<!-- b001280 | furniture | pages [15] -->
m

<!-- b001281 | furniture | pages [15] -->
m

<!-- b001282 | furniture | pages [15] -->
m

<!-- b001283 | furniture | pages [15] -->
m

<!-- b001284 | furniture | pages [15] -->
m

<!-- b001285 | furniture | pages [15] -->
m

<!-- b001286 | furniture | pages [15] -->
m

<!-- b001287 | furniture | pages [15] -->
m

<!-- b001288 | furniture | pages [15] -->
m

<!-- b001289 | furniture | pages [15] -->
m

<!-- b001290 | furniture | pages [15] -->
m

<!-- b001291 | furniture | pages [15] -->
m

<!-- b001292 | furniture | pages [15] -->
m

<!-- b001293 | furniture | pages [15] -->
m

<!-- b001294 | furniture | pages [15] -->
m

<!-- b001295 | furniture | pages [15] -->
m

<!-- b001296 | furniture | pages [15] -->
m

<!-- b001297 | furniture | pages [15] -->
m

<!-- b001298 | furniture | pages [15] -->
m

<!-- b001299 | furniture | pages [15] -->
m

<!-- b001300 | furniture | pages [15] -->
m

<!-- b001301 | furniture | pages [15] -->
m

<!-- b001302 | furniture | pages [15] -->
m

<!-- b001303 | furniture | pages [15] -->
m

<!-- b001304 | furniture | pages [15] -->
m

<!-- b001305 | furniture | pages [15] -->
m

<!-- b001306 | furniture | pages [15] -->
m

<!-- b001307 | furniture | pages [15] -->
m

<!-- b001308 | furniture | pages [15] -->
m

<!-- b001309 | furniture | pages [15] -->
m

<!-- b001310 | furniture | pages [15] -->
m

<!-- b001311 | furniture | pages [15] -->
m

<!-- b001312 | furniture | pages [15] -->
m

<!-- b001313 | furniture | pages [15] -->
m

<!-- b001314 | furniture | pages [15] -->
m

<!-- b001315 | furniture | pages [15] -->
m

<!-- b001316 | furniture | pages [15] -->
m

<!-- b001317 | furniture | pages [15] -->
m

<!-- b001318 | furniture | pages [15] -->
m

<!-- b001319 | furniture | pages [15] -->
m

<!-- b001320 | furniture | pages [15] -->
m

<!-- b001321 | furniture | pages [15] -->
m

<!-- b001322 | furniture | pages [15] -->
m

<!-- b001323 | furniture | pages [15] -->
m

<!-- b001324 | furniture | pages [15] -->
m

<!-- b001325 | furniture | pages [15] -->
m

<!-- b001326 | furniture | pages [15] -->
m

<!-- b001327 | furniture | pages [15] -->
m

<!-- b001328 | furniture | pages [15] -->
m

<!-- b001329 | furniture | pages [15] -->
m

<!-- b001330 | furniture | pages [15] -->
m

<!-- b001331 | furniture | pages [15] -->
m

<!-- b001332 | furniture | pages [15] -->
m

<!-- b001333 | furniture | pages [15] -->
m

<!-- b001334 | furniture | pages [15] -->
m

<!-- b001335 | furniture | pages [15] -->
m

<!-- b001336 | furniture | pages [15] -->
m

<!-- b001337 | furniture | pages [15] -->
m

<!-- b001338 | furniture | pages [15] -->
m

<!-- b001339 | furniture | pages [15] -->
m

<!-- b001340 | furniture | pages [15] -->
m

<!-- b001341 | furniture | pages [15] -->
m

<!-- b001342 | furniture | pages [15] -->
m

<!-- b001343 | furniture | pages [15] -->
m

<!-- b001344 | furniture | pages [15] -->
m

<!-- b001345 | furniture | pages [15] -->
m

<!-- b001346 | furniture | pages [15] -->
m

<!-- b001347 | furniture | pages [15] -->
m

<!-- b001348 | furniture | pages [15] -->
m

<!-- b001349 | furniture | pages [15] -->
m

<!-- b001350 | furniture | pages [15] -->
m

<!-- b001351 | furniture | pages [15] -->
m

<!-- b001352 | furniture | pages [15] -->
m

<!-- b001353 | furniture | pages [15] -->
m

<!-- b001354 | furniture | pages [15] -->
m

<!-- b001355 | furniture | pages [15] -->
m

<!-- b001356 | furniture | pages [15] -->
m

<!-- b001357 | furniture | pages [15] -->
m

<!-- b001358 | furniture | pages [15] -->
m

<!-- b001359 | furniture | pages [15] -->
m

<!-- b001360 | furniture | pages [15] -->
m

<!-- b001361 | furniture | pages [15] -->
m

<!-- b001362 | furniture | pages [15] -->
m

<!-- b001363 | furniture | pages [15] -->
m

<!-- b001364 | furniture | pages [15] -->
m

<!-- b001365 | furniture | pages [15] -->
m

<!-- b001366 | furniture | pages [15] -->
m

<!-- b001367 | furniture | pages [15] -->
m

<!-- b001368 | furniture | pages [15] -->
m

<!-- b001369 | furniture | pages [15] -->
m

<!-- b001370 | furniture | pages [15] -->
m

<!-- b001371 | furniture | pages [15] -->
m

<!-- b001372 | furniture | pages [15] -->
m

<!-- b001373 | furniture | pages [15] -->
m

<!-- b001374 | furniture | pages [15] -->
m

<!-- b001375 | furniture | pages [15] -->
m

<!-- b001376 | furniture | pages [15] -->
m

<!-- b001377 | furniture | pages [15] -->
m

<!-- b001378 | furniture | pages [15] -->
m

<!-- b001379 | furniture | pages [15] -->
m

<!-- b001380 | furniture | pages [15] -->
m

<!-- b001381 | furniture | pages [15] -->
m

<!-- b001382 | furniture | pages [15] -->
m

<!-- b001383 | furniture | pages [15] -->
m

<!-- b001384 | furniture | pages [15] -->
m

<!-- b001385 | furniture | pages [15] -->
m

<!-- b001386 | furniture | pages [15] -->
m

<!-- b001387 | furniture | pages [15] -->
m

<!-- b001388 | furniture | pages [15] -->
m

<!-- b001389 | furniture | pages [15] -->
m

<!-- b001390 | furniture | pages [15] -->
m

<!-- b001391 | furniture | pages [15] -->
m

<!-- b001392 | furniture | pages [15] -->
m

<!-- b001393 | furniture | pages [15] -->
m

<!-- b001394 | furniture | pages [15] -->
m

<!-- b001395 | furniture | pages [15] -->
m

<!-- b001396 | furniture | pages [15] -->
m

<!-- b001397 | furniture | pages [15] -->
m

<!-- b001398 | furniture | pages [15] -->
m

<!-- b001399 | furniture | pages [15] -->
m

<!-- b001400 | furniture | pages [15] -->
m

<!-- b001401 | furniture | pages [15] -->
m

<!-- b001402 | furniture | pages [15] -->
m

<!-- b001403 | furniture | pages [15] -->
m

<!-- b001404 | furniture | pages [15] -->
m

<!-- b001405 | furniture | pages [15] -->
m

<!-- b001406 | furniture | pages [15] -->
m

<!-- b001407 | furniture | pages [15] -->
m

<!-- b001408 | furniture | pages [15] -->
m

<!-- b001409 | furniture | pages [15] -->
m

<!-- b001410 | furniture | pages [15] -->
m

<!-- b001411 | furniture | pages [15] -->
m

<!-- b001412 | furniture | pages [15] -->
m

<!-- b001413 | furniture | pages [15] -->
m

<!-- b001414 | furniture | pages [15] -->
m

<!-- b001415 | furniture | pages [15] -->
m

<!-- b001416 | furniture | pages [15] -->
m

<!-- b001417 | furniture | pages [15] -->
m

<!-- b001418 | furniture | pages [15] -->
m

<!-- b001419 | furniture | pages [15] -->
m

<!-- b001420 | furniture | pages [15] -->
m

<!-- b001421 | furniture | pages [15] -->
m

<!-- b001422 | furniture | pages [15] -->
m

<!-- b001423 | furniture | pages [15] -->
m

<!-- b001424 | furniture | pages [15] -->
m

<!-- b001425 | furniture | pages [15] -->
m

<!-- b001426 | furniture | pages [15] -->
m

<!-- b001427 | furniture | pages [15] -->
m

<!-- b001428 | furniture | pages [15] -->
m

<!-- b001429 | furniture | pages [15] -->
m

<!-- b001430 | furniture | pages [15] -->
m

<!-- b001431 | furniture | pages [15] -->
m

<!-- b001432 | furniture | pages [15] -->
m

<!-- b001433 | furniture | pages [15] -->
m

<!-- b001434 | furniture | pages [15] -->
m

<!-- b001435 | furniture | pages [15] -->
m

<!-- b001436 | furniture | pages [15] -->
m

<!-- b001437 | furniture | pages [15] -->
m

<!-- b001438 | furniture | pages [15] -->
m

<!-- b001439 | furniture | pages [15] -->
m

<!-- b001440 | furniture | pages [15] -->
m

<!-- b001441 | furniture | pages [15] -->
m

<!-- b001442 | furniture | pages [15] -->
m

<!-- b001443 | furniture | pages [15] -->
m

<!-- b001444 | furniture | pages [15] -->
m

<!-- b001445 | furniture | pages [15] -->
m

<!-- b001446 | furniture | pages [15] -->
m

<!-- b001447 | furniture | pages [15] -->
m

<!-- b001448 | furniture | pages [15] -->
m

<!-- b001449 | furniture | pages [15] -->
m

<!-- b001450 | furniture | pages [15] -->
m

<!-- b001451 | furniture | pages [15] -->
m

<!-- b001452 | furniture | pages [15] -->
m

<!-- b001453 | furniture | pages [15] -->
m

<!-- b001454 | furniture | pages [15] -->
m

<!-- b001455 | furniture | pages [15] -->
m

<!-- b001456 | furniture | pages [15] -->
m

<!-- b001457 | furniture | pages [15] -->
m

<!-- b001458 | furniture | pages [15] -->
m

<!-- b001459 | furniture | pages [15] -->
m

<!-- b001460 | furniture | pages [15] -->
m

<!-- b001461 | furniture | pages [15] -->
m

<!-- b001462 | furniture | pages [15] -->
m

<!-- b001463 | furniture | pages [15] -->
m

<!-- b001464 | furniture | pages [15] -->
m

<!-- b001465 | furniture | pages [15] -->
m

<!-- b001466 | furniture | pages [15] -->
m

<!-- b001467 | furniture | pages [15] -->
m

<!-- b001468 | furniture | pages [15] -->
m

<!-- b001469 | furniture | pages [15] -->
m

<!-- b001470 | furniture | pages [15] -->
m

<!-- b001471 | furniture | pages [15] -->
m

<!-- b001472 | furniture | pages [15] -->
m

<!-- b001473 | furniture | pages [15] -->
m

<!-- b001474 | furniture | pages [15] -->
m

<!-- b001475 | furniture | pages [15] -->
m

<!-- b001476 | furniture | pages [15] -->
m

<!-- b001477 | furniture | pages [15] -->
m

<!-- b001478 | furniture | pages [15] -->
m

<!-- b001479 | furniture | pages [15] -->
m

<!-- b001480 | furniture | pages [15] -->
m

<!-- b001481 | furniture | pages [15] -->
m

<!-- b001482 | furniture | pages [15] -->
m

<!-- b001483 | furniture | pages [15] -->
m

<!-- b001484 | furniture | pages [15] -->
m

<!-- b001485 | furniture | pages [15] -->
m

<!-- b001486 | furniture | pages [15] -->
m

<!-- b001487 | furniture | pages [15] -->
m

<!-- b001488 | furniture | pages [15] -->
m

<!-- b001489 | furniture | pages [15] -->
m

<!-- b001490 | furniture | pages [15] -->
m

<!-- b001491 | furniture | pages [15] -->
m

<!-- b001492 | furniture | pages [15] -->
m

<!-- b001493 | furniture | pages [15] -->
m

<!-- b001494 | furniture | pages [15] -->
m

<!-- b001495 | furniture | pages [15] -->
m

<!-- b001496 | furniture | pages [15] -->
m

<!-- b001497 | furniture | pages [15] -->
m

<!-- b001498 | furniture | pages [15] -->
m

<!-- b001499 | furniture | pages [15] -->
m

<!-- b001500 | furniture | pages [15] -->
m

<!-- b001501 | furniture | pages [15] -->
m

<!-- b001502 | furniture | pages [15] -->
m

<!-- b001503 | furniture | pages [15] -->
m

<!-- b001504 | furniture | pages [15] -->
m

<!-- b001505 | furniture | pages [15] -->
m

<!-- b001506 | furniture | pages [15] -->
m

<!-- b001507 | furniture | pages [15] -->
m

<!-- b001508 | furniture | pages [15] -->
m

<!-- b001509 | furniture | pages [15] -->
m

<!-- b001510 | furniture | pages [15] -->
m

<!-- b001511 | furniture | pages [15] -->
m

<!-- b001512 | furniture | pages [15] -->
m

<!-- b001513 | furniture | pages [15] -->
m

<!-- b001514 | furniture | pages [15] -->
m

<!-- b001515 | furniture | pages [15] -->
m

<!-- b001516 | furniture | pages [15] -->
m

<!-- b001517 | furniture | pages [15] -->
m

<!-- b001518 | furniture | pages [15] -->
m

<!-- b001519 | furniture | pages [15] -->
m

<!-- b001520 | furniture | pages [15] -->
m

<!-- b001521 | furniture | pages [15] -->
m

<!-- b001522 | furniture | pages [15] -->
m

<!-- b001523 | furniture | pages [15] -->
m

<!-- b001524 | furniture | pages [16] -->
m

<!-- b001525 | furniture | pages [16] -->
m

<!-- b001526 | furniture | pages [16] -->
m

<!-- b001527 | furniture | pages [16] -->
m

<!-- b001528 | furniture | pages [16] -->
m

<!-- b001529 | furniture | pages [16] -->
m

<!-- b001530 | furniture | pages [16] -->
m

<!-- b001531 | furniture | pages [16] -->
m

<!-- b001532 | furniture | pages [16] -->
m

<!-- b001533 | furniture | pages [16] -->
m

<!-- b001534 | furniture | pages [16] -->
m

<!-- b001535 | furniture | pages [16] -->
m

<!-- b001536 | furniture | pages [16] -->
m

<!-- b001537 | furniture | pages [16] -->
m

<!-- b001538 | furniture | pages [16] -->
m

<!-- b001539 | furniture | pages [16] -->
m

<!-- b001540 | furniture | pages [16] -->
m

<!-- b001541 | furniture | pages [16] -->
m

<!-- b001542 | furniture | pages [16] -->
m

<!-- b001543 | furniture | pages [16] -->
m

<!-- b001544 | furniture | pages [16] -->
m

<!-- b001545 | furniture | pages [16] -->
m

<!-- b001546 | furniture | pages [16] -->
m

<!-- b001547 | furniture | pages [16] -->
m

<!-- b001548 | furniture | pages [16] -->
m

<!-- b001549 | furniture | pages [16] -->
m

<!-- b001550 | furniture | pages [16] -->
m

<!-- b001551 | furniture | pages [16] -->
m

<!-- b001552 | furniture | pages [16] -->
m

<!-- b001553 | furniture | pages [16] -->
m

<!-- b001554 | furniture | pages [16] -->
m

<!-- b001555 | furniture | pages [16] -->
m

<!-- b001556 | furniture | pages [16] -->
m

<!-- b001557 | furniture | pages [16] -->
m

<!-- b001558 | furniture | pages [16] -->
m

<!-- b001559 | furniture | pages [16] -->
m

<!-- b001560 | furniture | pages [16] -->
m

<!-- b001561 | furniture | pages [16] -->
m

<!-- b001562 | furniture | pages [16] -->
m

<!-- b001563 | furniture | pages [16] -->
m

<!-- b001564 | furniture | pages [16] -->
m

<!-- b001565 | furniture | pages [16] -->
m

<!-- b001566 | furniture | pages [16] -->
m

<!-- b001567 | furniture | pages [16] -->
m

<!-- b001568 | furniture | pages [16] -->
m

<!-- b001569 | furniture | pages [16] -->
m

<!-- b001570 | furniture | pages [16] -->
m

<!-- b001571 | furniture | pages [16] -->
m

<!-- b001572 | furniture | pages [16] -->
m

<!-- b001573 | furniture | pages [16] -->
m

<!-- b001574 | furniture | pages [16] -->
m

<!-- b001575 | furniture | pages [16] -->
m

<!-- b001576 | furniture | pages [16] -->
m

<!-- b001577 | furniture | pages [16] -->
Team # 2500759

<!-- b001578 | furniture | pages [16] -->
Page 16 of 26

<!-- b001579 | furniture | pages [16] -->
m

<!-- b001580 | furniture | pages [16] -->
m

<!-- b001581 | furniture | pages [16] -->
m

<!-- b001582 | furniture | pages [16] -->
m

<!-- b001583 | furniture | pages [16] -->
m

<!-- b001584 | furniture | pages [16] -->
m

<!-- b001585 | furniture | pages [16] -->
m

<!-- b001586 | furniture | pages [16] -->
m

<!-- b001587 | furniture | pages [16] -->
m

<!-- b001588 | furniture | pages [16] -->
m

<!-- b001589 | furniture | pages [16] -->
m

<!-- b001590 | furniture | pages [16] -->
m

<!-- b001591 | furniture | pages [16] -->
m

<!-- b001592 | furniture | pages [16] -->
m

<!-- b001593 | furniture | pages [16] -->
m

<!-- b001594 | furniture | pages [16] -->
m

<!-- b001595 | furniture | pages [16] -->
m

<!-- b001596 | furniture | pages [16] -->
m

<!-- b001597 | furniture | pages [16] -->
m

<!-- b001598 | furniture | pages [16] -->
m

<!-- b001599 | furniture | pages [16] -->
m

<!-- b001600 | furniture | pages [16] -->
m

<!-- b001601 | furniture | pages [16] -->
m

<!-- b001602 | furniture | pages [16] -->
m

<!-- b001603 | furniture | pages [16] -->
m

<!-- b001604 | furniture | pages [16] -->
m

<!-- b001605 | furniture | pages [16] -->
m

<!-- b001606 | furniture | pages [16] -->
m

<!-- b001607 | furniture | pages [16] -->
m

<!-- b001608 | furniture | pages [16] -->
m

<!-- b001609 | furniture | pages [16] -->
m

<!-- b001610 | furniture | pages [16] -->
m

<!-- b001611 | furniture | pages [16] -->
m

<!-- b001612 | furniture | pages [16] -->
m

<!-- b001613 | furniture | pages [16] -->
m

<!-- b001614 | furniture | pages [16] -->
m

<!-- b001615 | furniture | pages [16] -->
m

<!-- b001616 | furniture | pages [16] -->
m

<!-- b001617 | furniture | pages [16] -->
m

<!-- b001618 | furniture | pages [16] -->
m

<!-- b001619 | furniture | pages [16] -->
m

<!-- b001620 | furniture | pages [16] -->
m

<!-- b001621 | furniture | pages [16] -->
m

<!-- b001622 | furniture | pages [16] -->
m

<!-- b001623 | furniture | pages [16] -->
m

<!-- b001624 | furniture | pages [16] -->
m

<!-- b001625 | furniture | pages [16] -->
m

<!-- b001626 | furniture | pages [16] -->
m

<!-- b001627 | furniture | pages [16] -->
m

<!-- b001628 | furniture | pages [16] -->
m

<!-- b001629 | furniture | pages [16] -->
m

<!-- b001630 | furniture | pages [16] -->
m

<!-- b001631 | furniture | pages [16] -->
m

<!-- b001632 | furniture | pages [16] -->
m

<!-- b001633 | furniture | pages [16] -->
m

<!-- b001634 | furniture | pages [16] -->
m

<!-- b001635 | furniture | pages [16] -->
m

<!-- b001636 | furniture | pages [16] -->
m

<!-- b001637 | furniture | pages [16] -->
m

<!-- b001638 | furniture | pages [16] -->
m

<!-- b001639 | furniture | pages [16] -->
m

<!-- b001640 | furniture | pages [16] -->
m

<!-- b001641 | furniture | pages [16] -->
m

<!-- b001642 | furniture | pages [16] -->
m

<!-- b001643 | furniture | pages [16] -->
m

<!-- b001644 | furniture | pages [16] -->
m

<!-- b001645 | furniture | pages [16] -->
m

<!-- b001646 | furniture | pages [16] -->
m

<!-- b001647 | furniture | pages [16] -->
m

<!-- b001648 | furniture | pages [16] -->
m

<!-- b001649 | furniture | pages [16] -->
m

<!-- b001650 | furniture | pages [16] -->
m

<!-- b001651 | furniture | pages [16] -->
m

<!-- b001652 | furniture | pages [16] -->
m

<!-- b001653 | furniture | pages [16] -->
m

<!-- b001654 | furniture | pages [16] -->
m

<!-- b001655 | furniture | pages [16] -->
m

<!-- b001656 | furniture | pages [16] -->
m

<!-- b001657 | furniture | pages [16] -->
m

<!-- b001658 | furniture | pages [16] -->
m

<!-- b001659 | furniture | pages [16] -->
m

<!-- b001660 | furniture | pages [16] -->
m

<!-- b001661 | furniture | pages [16] -->
m

<!-- b001662 | furniture | pages [16] -->
m

<!-- b001663 | furniture | pages [16] -->
m

<!-- b001664 | furniture | pages [16] -->
m

<!-- b001665 | furniture | pages [16] -->
m

<!-- b001666 | furniture | pages [16] -->
m

<!-- b001667 | furniture | pages [16] -->
m

<!-- b001668 | furniture | pages [16] -->
m

<!-- b001669 | furniture | pages [16] -->
m

<!-- b001670 | furniture | pages [16] -->
m

<!-- b001671 | furniture | pages [16] -->
m

<!-- b001672 | furniture | pages [16] -->
m

<!-- b001673 | furniture | pages [16] -->
m

<!-- b001674 | furniture | pages [16] -->
m

<!-- b001675 | furniture | pages [16] -->
m

<!-- b001676 | furniture | pages [16] -->
m

<!-- b001677 | furniture | pages [16] -->
m

<!-- b001678 | furniture | pages [16] -->
m

<!-- b001679 | furniture | pages [16] -->
m

<!-- b001680 | furniture | pages [16] -->
m

<!-- b001681 | furniture | pages [16] -->
m

<!-- b001682 | furniture | pages [16] -->
m

<!-- b001683 | furniture | pages [16] -->
m

<!-- b001684 | furniture | pages [16] -->
m

<!-- b001685 | furniture | pages [16] -->
m

<!-- b001686 | furniture | pages [16] -->
m

<!-- b001687 | furniture | pages [16] -->
m

<!-- b001688 | furniture | pages [16] -->
m

<!-- b001689 | furniture | pages [16] -->
m

<!-- b001690 | furniture | pages [16] -->
m

<!-- b001691 | furniture | pages [16] -->
m

<!-- b001692 | furniture | pages [16] -->
m

<!-- b001693 | furniture | pages [16] -->
m

<!-- b001694 | furniture | pages [16] -->
m

<!-- b001695 | furniture | pages [16] -->
m

<!-- b001696 | furniture | pages [16] -->
m

<!-- b001697 | furniture | pages [16] -->
m

<!-- b001698 | furniture | pages [16] -->
m

<!-- b001699 | furniture | pages [16] -->
m

<!-- b001700 | furniture | pages [16] -->
m

<!-- b001701 | furniture | pages [16] -->
m

<!-- b001702 | furniture | pages [16] -->
m

<!-- b001703 | furniture | pages [16] -->
m

<!-- b001704 | furniture | pages [16] -->
m

<!-- b001705 | furniture | pages [16] -->
m

<!-- b001706 | furniture | pages [16] -->
m

<!-- b001707 | furniture | pages [16] -->
m

<!-- b001708 | furniture | pages [16] -->
m

<!-- b001709 | furniture | pages [16] -->
m

<!-- b001710 | furniture | pages [16] -->
m

<!-- b001711 | furniture | pages [16] -->
m

<!-- b001712 | furniture | pages [16] -->
m

<!-- b001713 | furniture | pages [16] -->
m

<!-- b001714 | furniture | pages [16] -->
m

<!-- b001715 | furniture | pages [16] -->
m

<!-- b001716 | furniture | pages [16] -->
m

<!-- b001717 | furniture | pages [16] -->
m

<!-- b001718 | furniture | pages [16] -->
m

<!-- b001719 | furniture | pages [16] -->
m

<!-- b001720 | furniture | pages [16] -->
m

<!-- b001721 | furniture | pages [16] -->
m

<!-- b001722 | furniture | pages [16] -->
m

<!-- b001723 | furniture | pages [16] -->
m

<!-- b001724 | furniture | pages [16] -->
m

<!-- b001725 | furniture | pages [16] -->
m

<!-- b001726 | furniture | pages [16] -->
m

<!-- b001727 | furniture | pages [16] -->
m

<!-- b001728 | furniture | pages [16] -->
m

<!-- b001729 | furniture | pages [16] -->
m

<!-- b001730 | furniture | pages [16] -->
m

<!-- b001731 | furniture | pages [16] -->
m

<!-- b001732 | furniture | pages [16] -->
m

<!-- b001733 | furniture | pages [16] -->
m

<!-- b001734 | furniture | pages [16] -->
m

<!-- b001735 | furniture | pages [16] -->
m

<!-- b001736 | furniture | pages [16] -->
m

<!-- b001737 | furniture | pages [16] -->
m

<!-- b001738 | furniture | pages [16] -->
m

<!-- b001739 | furniture | pages [16] -->
m

<!-- b001740 | furniture | pages [16] -->
m

<!-- b001741 | furniture | pages [16] -->
m

<!-- b001742 | furniture | pages [16] -->
m

<!-- b001743 | furniture | pages [16] -->
m

<!-- b001744 | furniture | pages [16] -->
m

<!-- b001745 | furniture | pages [16] -->
m

<!-- b001746 | furniture | pages [16] -->
m

<!-- b001747 | furniture | pages [16] -->
m

<!-- b001748 | furniture | pages [16] -->
m

<!-- b001749 | furniture | pages [16] -->
m

<!-- b001750 | furniture | pages [16] -->
m

<!-- b001751 | furniture | pages [16] -->
m

<!-- b001752 | furniture | pages [16] -->
m

<!-- b001753 | furniture | pages [16] -->
m

<!-- b001754 | furniture | pages [16] -->
m

<!-- b001755 | furniture | pages [16] -->
m

<!-- b001756 | furniture | pages [16] -->
m

<!-- b001757 | furniture | pages [16] -->
m

<!-- b001758 | furniture | pages [16] -->
m

<!-- b001759 | furniture | pages [16] -->
m

<!-- b001760 | furniture | pages [16] -->
m

<!-- b001761 | furniture | pages [16] -->
m

<!-- b001762 | furniture | pages [16] -->
m

<!-- b001763 | furniture | pages [16] -->
m

<!-- b001764 | furniture | pages [16] -->
m

<!-- b001765 | furniture | pages [16] -->
m

<!-- b001766 | furniture | pages [16] -->
m

<!-- b001767 | furniture | pages [16] -->
m

<!-- b001768 | furniture | pages [16] -->
m

<!-- b001769 | furniture | pages [16] -->
m

<!-- b001770 | furniture | pages [16] -->
m

<!-- b001771 | furniture | pages [16] -->
m

<!-- b001772 | furniture | pages [16] -->
m

<!-- b001773 | furniture | pages [16] -->
m

<!-- b001774 | furniture | pages [16] -->
m

<!-- b001775 | furniture | pages [16] -->
m

<!-- b001776 | furniture | pages [16] -->
m

<!-- b001777 | furniture | pages [16] -->
m

<!-- b001778 | furniture | pages [16] -->
m

<!-- b001779 | furniture | pages [16] -->
m

<!-- b001780 | furniture | pages [16] -->
m

<!-- b001781 | furniture | pages [16] -->
m

<!-- b001782 | furniture | pages [16] -->
m

<!-- b001783 | furniture | pages [16] -->
m

<!-- b001784 | furniture | pages [16] -->
m

<!-- b001785 | furniture | pages [16] -->
m

<!-- b001786 | furniture | pages [16] -->
m

<!-- b001787 | furniture | pages [16] -->
m

<!-- b001788 | furniture | pages [16] -->
m

<!-- b001789 | furniture | pages [16] -->
m

<!-- b001790 | furniture | pages [16] -->
m

<!-- b001791 | furniture | pages [16] -->
m

<!-- b001792 | furniture | pages [16] -->
m

<!-- b001793 | furniture | pages [16] -->
m

<!-- b001794 | furniture | pages [16] -->
m

<!-- b001795 | furniture | pages [16] -->
m

<!-- b001796 | furniture | pages [16] -->
m

<!-- b001797 | furniture | pages [16] -->
m

<!-- b001798 | furniture | pages [16] -->
m

<!-- b001799 | furniture | pages [16] -->
m

<!-- b001800 | furniture | pages [16] -->
m

<!-- b001801 | furniture | pages [16] -->
m

<!-- b001802 | furniture | pages [16] -->
m

<!-- b001803 | furniture | pages [16] -->
m

<!-- b001804 | furniture | pages [16] -->
m

<!-- b001805 | furniture | pages [16] -->
m

<!-- b001806 | furniture | pages [16] -->
m

<!-- b001807 | furniture | pages [16] -->
m

<!-- b001808 | furniture | pages [16] -->
m

<!-- b001809 | furniture | pages [16] -->
m

<!-- b001810 | furniture | pages [16] -->
m

<!-- b001811 | furniture | pages [16] -->
m

<!-- b001812 | furniture | pages [16] -->
m

<!-- b001813 | furniture | pages [16] -->
m

<!-- b001814 | furniture | pages [16] -->
m

<!-- b001815 | furniture | pages [16] -->
m

<!-- b001816 | furniture | pages [16] -->
m

<!-- b001817 | furniture | pages [16] -->
m

<!-- b001818 | furniture | pages [16] -->
m

<!-- b001819 | furniture | pages [16] -->
m

<!-- b001820 | furniture | pages [16] -->
m

<!-- b001821 | furniture | pages [16] -->
m

<!-- b001822 | furniture | pages [16] -->
m

<!-- b001823 | furniture | pages [16] -->
m

<!-- b001824 | furniture | pages [16] -->
m

<!-- b001825 | furniture | pages [16] -->
m

<!-- b001826 | furniture | pages [16] -->
m

<!-- b001827 | furniture | pages [16] -->
m

<!-- b001828 | furniture | pages [16] -->
m

<!-- b001829 | furniture | pages [16] -->
m

<!-- b001830 | furniture | pages [16] -->
m

<!-- b001831 | furniture | pages [16] -->
m

<!-- b001832 | furniture | pages [16] -->
m

<!-- b001833 | furniture | pages [16] -->
m

<!-- b001834 | furniture | pages [16] -->
m

<!-- b001835 | furniture | pages [16] -->
m

<!-- b001836 | furniture | pages [16] -->
m

<!-- b001837 | furniture | pages [16] -->
m

<!-- b001838 | furniture | pages [16] -->
m

<!-- b001839 | furniture | pages [16] -->
m

<!-- b001840 | furniture | pages [16] -->
m

<!-- b001841 | furniture | pages [16] -->
m

<!-- b001842 | furniture | pages [16] -->
m

<!-- b001843 | furniture | pages [16] -->
m

<!-- b001844 | furniture | pages [16] -->
m

<!-- b001845 | furniture | pages [16] -->
m

<!-- b001846 | furniture | pages [16] -->
m

<!-- b001847 | furniture | pages [16] -->
m

<!-- b001848 | furniture | pages [16] -->
m

<!-- b001849 | furniture | pages [16] -->
m

<!-- b001850 | furniture | pages [16] -->
m

<!-- b001851 | furniture | pages [16] -->
m

<!-- b001852 | furniture | pages [16] -->
m

<!-- b001853 | furniture | pages [16] -->
m

<!-- b001854 | furniture | pages [16] -->
m

<!-- b001855 | furniture | pages [16] -->
m

<!-- b001856 | furniture | pages [16] -->
m

<!-- b001857 | furniture | pages [16] -->
m

<!-- b001859 | prose | pages [16] -->
(a) (b)

<!-- b001860 | caption | pages [16] -->
Figure 9: Cellular-Importance Mixed Plot

<!-- b001861 | caption | pages [16] -->
Figure 10: Top 15 Sports Event Importance Score

<!-- b001862 | prose | pages [16] -->
gold importance (0.9039) due to its variety and competition. Table Tennis, while lower in gold importance, is second in total medals (0.95), reflecting its global popularity and China’s dominance. Diving and Wrestling also hold significance, with Diving showcasing China’s strength.

<!-- b001863 | prose | pages [16] -->
Next, we will create univariate dependence plots for PC1, which has the highest SHAP importance. This analysis will illustrate the nonlinear relationship between PC1 and medal counts, highlighting contributions from sports such as Swimming, Athletics, Wrestling, Gymnastics, and Basketball.

<!-- b001864 | prose | pages [16] -->
In the gold medal prediction model (Fig. 11(a)), the negative region of PC1 is closely associated with sports that have high loadings, such as Swimming, Athletics, Wrestling, Gymnastics, and Basketball, which perform well when PC1 is negative, significantly con- tributing to the gold medal count. The upward trend in the dependence plot indicates that outstanding performances in these sports lead to a considerable increase in gold medals, highlighting their crucial impact, particularly in the negative PC1 area. As PC1 turns positive, their influence diminishes, demonstrating that their effects on gold medal counts are primarily concentrated in the negative region. Similarly, in the total medal prediction model (Fig. 11(b)), these same sports significantly impact the total medal count; high performance when PC1 is negative enhances both gold and overall medal tallies. The ascent of SHAP values in the dependence plot signifies that their excellence contributes notably not only to gold but also to silver and bronze medals. As PC1 becomes positive, their influence on total medal counts weakens, further confirming their critical role in the negative PC1 region.

<!-- b001865 | prose | pages [16, 17] -->
关注数学模型 微信公众号：数学模型 (a) (b) 微信号：MATHmodels

<!-- b001866 | furniture | pages [16] -->
2

<!-- b001867 | furniture | pages [16] -->
MATHmodels

<!-- b001868 | furniture | pages [16] -->
获取更多资讯

<!-- b001869 | furniture | pages [17] -->
Team # 2500759

<!-- b001870 | furniture | pages [17] -->
Page 17 of 26

<!-- b001872 | caption | pages [17] -->
Figure 11: PC1-SHAP Mixed Plot

<!-- b001873 | prose | pages [17] -->
Finally, this study incorporates SHAP values for individual samples to analyze the impact of different sports on gold and total medal predictions for the U.S. and France, particularly focusing on the contributions of traditional powerhouses like Swimming and Athletics. Additionally, it discusses the host country effect, exploring how the upcoming host nations, France in 2024 and the USA in 2028, can positively influence predictions of gold and total medal counts through home advantage.

<!-- b001874 | prose | pages [17] -->
(a) (b)

<!-- b001875 | caption | pages [17] -->
Figure 12: 2028 U.S. Medal and Gold Medal Prediction SHAP Plot

<!-- b001876 | prose | pages [17] -->
(a) (b)

<!-- b001877 | caption | pages [17] -->
Figure 13: 2028 France Medal and Gold Medal Prediction SHAP Plot

<!-- b001878 | prose | pages [17, 18] -->
Figs. 12(a)-(b) show that traditional power sports like Swimming and Athletics carry significant weight in the PCA components, particularly with high loadings in prin- cipal components PC1 and PC2, indicating their substantial contributions to the U.S. gold medal count. With a PC1 value of 18 for gold medal predictions, this confirms the driv- ing role of these sports. In contrast, the total medal count prediction for the U.S. is 133, with a contribution of 6.08 from PC2, revealing the impact of other sports like Gymnas- tics and Basketball, which, while contributing fewer golds, play a vital role in enhancing overall medal totals. For France, as the 2024 host, the predictions (Figs. 13(a)-(b)) are notably influenced by the "host country effect," with a total medal count forecast of 41 and a significant contribution of 2.89 from PC5, underscoring the importance of sports such as Cycling and Marathon. Despite a relatively lower gold prediction of 12, the host effect positively enhances France's overall performance, particularly in events like Swim- ming and Athletics, where the PC3 loading of 1.97 confirms their contributions. While France's traditional strengths in these events may not match those of the U.S., home ad- vantage helps bridge the gap.

<!-- b001879 | furniture | pages [18] -->
Page 18 of 26

<!-- b001880 | furniture | pages [18] -->
Team # 2500759

<!-- b001882 | prose | pages [18] -->
This analysis concludes that the choice of sports and traditional advantages play decisive roles in Olympic performances, with the U.S. primarily excelling in individual sports like Swimming and Athletics, while France benefits from team sports and the host country effect. Overall, the host effect significantly impacts both countries' Olympic performances, with France poised for a notable boost in 2024 as a host, while the U.S. faces new challenges in 2028.

<!-- b001883 | prose | pages [18] -->
Problem 2: The "Great Coach' Effect 4

<!-- b001884 | prose | pages [18] -->
It is evident from the problem 2 statement that the mobility of coaches is greater than that of athletes, suggesting that their transfers may have a direct impact on a coun- try's medal performance. The DID⁴ model is suitable for assessing the causal effects of policies or events by comparing the changes in the treatment group (country-sport combi- nations with a coaching change) and the control group (combinations without a coaching change) before and after the event. The problem also requires estimating the contribution of coaching effects to the number of medals, which necessitates quantifying the incremen- tal medals attributed to coaching changes. In addition, three countries need to be selected for which recommendations should be made regarding the sports in which to invest in coaching, while also estimating the potential impacts of such investments.

<!-- b001885 | heading | pages [18] -->
4.1 DID Modeling

<!-- b001886 | prose | pages [18] -->
The validity of the DID model relies on the parallel trends assumption, which states that the trends in medal counts for the treatment and control groups should be consistent prior to the coaching change. This assumption needs to be verified; otherwise, the re- sults may be biased. Finally, the analysis results must be structured clearly, specifying the recommended sports for each country, the current contribution coefficients of coach- ing effects, and the expected returns on investment. Additionally, the uncertainty of the estimates, such as confidence intervals and P-values, should be discussed to enhance the credibility of the conclusions. So we build the following DID model.

<!-- b001887 | prose | pages [18] -->
∑ (Medalsit − (β0 + β1Treati + β2Post + β3(Treati · Postt) + γXit))2 min β,γ i,t Medalsit = β0 + β1Treati + β2Postt + β3(Treati · Postt) + γXit + €it, ∀i, t (9) E[∆Medalsi | Treat = 1, Post = 0] = E[∆Medalsi | Treat = 0, Post = 0] s.t.

<!-- b001888 | prose | pages [18] -->
€it ⊥ Treati, Post

<!-- b001889 | prose | pages [18] -->
关注数学模型

<!-- b001890 | furniture | pages [18] -->
获取更多资讯

<!-- b001891 | furniture | pages [19] -->
Page 19 of 26

<!-- b001892 | furniture | pages [19] -->
Team # 2500759

<!-- b001893 | heading | pages [19] -->
4.2 Hypothesis Testing and Contribution Coefficient Analysis

<!-- b001894 | prose | pages [19] -->
We subsequently fit the model equation using ordinary least squares (OLS) to es- timate the coefficients β0, β1, β2, β3, γ. We calculate the P-value for β3 to assess it's significance. Additionally, we conduct a parallel trends test to verify whether the medal trends for the treatment and control groups were consistent prior to the coaching change. The comprehensive results are shown in Table 4.

<!-- b001895 | prose | pages [19] -->
模型

<!-- b001896 | caption | pages [19] -->
Table 4: Results of the DID Model on the Great Coach Effect

<!-- b001897 | prose | pages [19] -->
Sport β3 P-value NOC 95% confidence interval opnf 6.0 0.001 JPN [4.8, 7.2] 0.010 ITA 5.0 [3.5, 6.5] Athletics AUS 0.020 5.0 Swimming [3.0, 7.0] 4.0 Archery 0.030 KOR [2.0, 6.0] [1.5,6.5] POL 4.0 0.040 Athletics [-0.5, 6.5] 3.0 CUB 0.100 Boxing Fencing 3.0 0.200 [-1.0, 7.0] KOR dels Diving 3.0 0.150 CHN [-0.8, 6.8] ● Shooting 3.0 CHN 0.180 [-1.2, 7.2] ● 0.250 BRA 3.0 [-2.0, 8.0] Skateboarding

<!-- b001898 | prose | pages [19] -->
We selected the top 10 values of β3 for display in Fig. 14. It is evident that the coaching changes in Japanese judo, Italian athletics, Australian swimming, South Korean archery, and Polish athletics significantly increased the number of medals, as none of their confidence intervals include zero and all P-values are less than 0.05, from Table 4. In contrast, the β3 values for Cuban boxing, South Korean fencing, Chinese diving and shooting, and Brazilian skateboarding, although positive, have confidence intervals that include zero, and their P-values exceed 0.05, indicating that the causal effects of coaching changes in these countries did not pass the statistical significance test. Next, we conducted a parallel trends test using Japan as an example. Fig. 15 shows a clear upward trend in medal counts from 1996 to 2016, indicating that it successfully passed the parallel trends ● test. ●

<!-- b001899 | prose | pages [19] -->
and parallel trends tests. Upon reviewing the data123, it is confirmed that Australia, South Korea, and Poland indeed underwent coaching changes during the 2020-2024 period, specifically involving Rennie Taylor, Lee Changhoon, and Adam Kszczot, respectively. This aligns with the aforementioned results, suggesting that our model is effective.

<!-- b001900 | prose | pages [19] -->
Problem 3: New Insights 5

<!-- b001901 | prose | pages [19] -->
1. Dynamics of Medal Counts in Space and Time

<!-- b001902 | prose | pages [19] -->
(1) Insight: The model analyzes the spatiotemporal dynamics of Olympic medal counts through multiple iterations and Bootstrap resampling methods. The study indicates

<!-- b001903 | prose | pages [19, 20] -->
1https://olympics.com 2https://www.insidethegames.biz 3https://www.linkedin.com that certain countries display relatively stable performances across different Olympic cy- cles, while others experience significant fluctuations in their medal counts. For instance, some major nations show a limited range of variance in their medal counts, highlighting their sustained competitiveness across multiple events. In contrast, some smaller nations exhibit greater volatility in their medal counts, suggesting that their performance may be heavily influenced by specific events or sudden occurrences.

<!-- b001904 | furniture | pages [20] -->
Team # 2500759

<!-- b001905 | furniture | pages [20] -->
Page 20 of 26

<!-- b001906 | caption | pages [20] -->
Figure 14: The Top 10 Countries by Contribution Coefficient

<!-- b001907 | caption | pages [20] -->
Figure 15: Trends in Medals Acquisition in Japan from 1996 to 2016

<!-- b001909 | prose | pages [20] -->
(2) Decision support: The findings can assist the Olympic committees in developing more flexible strategies for future Olympic cycles. If a country exhibits instability in its medal counts, the committee can mitigate uncertainty by diversifying resource allocation, thereby avoiding excessive reliance on any single event. For example, increasing train- ing investments in unstable events and enhancing the competitiveness of other promising sports can help ensure consistent performance across various disciplines. Additionally, for countries showing more stable performances, the Olympic committees could focus on maintaining existing advantages while bolstering research and technical support to ensure they remain competitive at the forefront.

<!-- b001910 | prose | pages [20] -->
2. Correlation Between Olympic Medal Counts and Specific Events

<!-- b001911 | prose | pages [20] -->
(1) Insight: The model, through the integration of PCA and LSTM, reveals the sig- nificance of certain specific events in predicting medal counts. The research demonstrates that disciplines such as swimming, athletics, and shooting play a crucial role in the medal contributions of many countries. These events are not only widely recognized and highly competitive at the Olympics but also serve as essential battlegrounds for countries vying for medals. In particular, swimming and athletics stand out as primary sources of medal counts for many nations due to their frequent competitions and high viewer engagement.

<!-- b001912 | prose | pages [20, 21] -->
关注数学模型 (2) Decision support: Olympic committees can leverage these analytical findings for strategic planning, particularly in resource allocation and event development. For events that display a strong competitive advantage, countries can increase their invest- ments by providing additional training facilities and financial support. For instance, in nations where swimming and athletics are particularly strong, committees could enhance athlete training by collaborating with top domestic and international coaches to refine skills and improve overall performance. Furthermore, informed by data analysis, coun- tries can identify potential medal-winning events in advance, enabling them to formulate effective athlete development programs and promotional strategies for these disciplines. 微信公众号：数学模型 3. Coaching Investment Directions in National Strategies

<!-- b001913 | furniture | pages [20] -->
2

<!-- b001914 | furniture | pages [20] -->
MATHmodels

<!-- b001915 | furniture | pages [20] -->
获取更多资讯

<!-- b001916 | furniture | pages [21] -->
Team # 2500759

<!-- b001917 | furniture | pages [21] -->
Page 21 of 26

<!-- b001919 | prose | pages [21] -->
(1) Insight: Through model analysis, some countries exhibit strong medal returns following coaching changes, as seen in Australia. Conversely, other nations experience minimal impact from such coaching transitions, despite implementing changes.

<!-- b001920 | prose | pages [21] -->
(2) Decision support: Olympic committees should develop personalized strategies based on the specific circumstances of different countries, prioritizing support for events that demonstrate significant improvements post-coaching changes. For countries such as Japan, Italy, and Australia, the committees could enhance investments in judo, athletics, and swimming to increase medal returns. Meanwhile, for events that show less pro- 微信号：MATHmodels nounced results, committees could reduce excessive investments in those coaching staff and reallocate resources to focus on areas more likely to yield medals.

<!-- b001921 | heading | pages [21] -->
6 Sensitivity Analysis

<!-- b001922 | heading | pages [21] -->
6.1 The Number of Principal Components

<!-- b001923 | prose | pages [21] -->
To simplify the data structure and improve the efficiency of the prediction model, Principal Component Analysis (PCA) was used. PCA was performed on the Olympic event dataset, and the variance contribution rates of each principal component were cal- culated. The selection of five principal components was based on their explanation of 76.4% of the cumulative variance, effectively capturing most of the information in the original dataset. This choice is supported by Fig. 16, which shows a steep drop-off after the first few components, validating the use of five components. This approach reduces data dimensionality while retaining essential information and eliminating redundant fea- tures.

<!-- b001924 | caption | pages [21] -->
Figure 16: Scree Plot for Principal Component Selection

<!-- b001925 | heading | pages [21] -->
6.2 Prediction Model Evaluation

<!-- b001926 | prose | pages [21, 22] -->
In the model evaluation, we examined both the predictive accuracy and robustness of the gold medal and total medal prediction models. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1. Predictive accuracy

<!-- b001927 | furniture | pages [21] -->
m

<!-- b001928 | furniture | pages [21] -->
m

<!-- b001929 | furniture | pages [21] -->
m

<!-- b001930 | furniture | pages [21] -->
m

<!-- b001931 | furniture | pages [21] -->
m

<!-- b001932 | furniture | pages [21] -->
m

<!-- b001933 | furniture | pages [21] -->
m

<!-- b001934 | furniture | pages [21] -->
m

<!-- b001935 | furniture | pages [21] -->
m

<!-- b001936 | furniture | pages [21] -->
m

<!-- b001937 | furniture | pages [21] -->
m

<!-- b001938 | furniture | pages [21] -->
m

<!-- b001939 | furniture | pages [21] -->
m

<!-- b001940 | furniture | pages [21] -->
m

<!-- b001941 | furniture | pages [21] -->
m

<!-- b001942 | furniture | pages [21] -->
m

<!-- b001943 | furniture | pages [21] -->
m

<!-- b001944 | furniture | pages [21] -->
m

<!-- b001945 | furniture | pages [21] -->
m

<!-- b001946 | furniture | pages [21] -->
m

<!-- b001947 | furniture | pages [21] -->
m

<!-- b001948 | furniture | pages [21] -->
m

<!-- b001949 | furniture | pages [21] -->
m

<!-- b001950 | furniture | pages [21] -->
m

<!-- b001951 | furniture | pages [21] -->
m

<!-- b001952 | furniture | pages [21] -->
m

<!-- b001953 | furniture | pages [21] -->
m

<!-- b001954 | furniture | pages [21] -->
m

<!-- b001955 | furniture | pages [21] -->
m

<!-- b001956 | furniture | pages [21] -->
m

<!-- b001957 | furniture | pages [21] -->
m

<!-- b001958 | furniture | pages [21] -->
m

<!-- b001959 | furniture | pages [21] -->
m

<!-- b001960 | furniture | pages [21] -->
m

<!-- b001961 | furniture | pages [21] -->
m

<!-- b001962 | furniture | pages [21] -->
m

<!-- b001963 | furniture | pages [21] -->
m

<!-- b001964 | furniture | pages [21] -->
m

<!-- b001965 | furniture | pages [21] -->
m

<!-- b001966 | furniture | pages [21] -->
m

<!-- b001967 | furniture | pages [21] -->
m

<!-- b001968 | furniture | pages [21] -->
m

<!-- b001969 | furniture | pages [21] -->
m

<!-- b001970 | furniture | pages [21] -->
m

<!-- b001971 | furniture | pages [21] -->
m

<!-- b001972 | furniture | pages [21] -->
m

<!-- b001973 | furniture | pages [21] -->
m

<!-- b001974 | furniture | pages [21] -->
m

<!-- b001975 | furniture | pages [21] -->
m

<!-- b001976 | furniture | pages [21] -->
m

<!-- b001977 | furniture | pages [21] -->
m

<!-- b001978 | furniture | pages [21] -->
m

<!-- b001979 | furniture | pages [21] -->
m

<!-- b001980 | furniture | pages [21] -->
m

<!-- b001981 | furniture | pages [21] -->
m

<!-- b001982 | furniture | pages [21] -->
m

<!-- b001983 | furniture | pages [21] -->
m

<!-- b001984 | furniture | pages [21] -->
m

<!-- b001985 | furniture | pages [21] -->
m

<!-- b001986 | furniture | pages [21] -->
m

<!-- b001987 | furniture | pages [21] -->
m

<!-- b001988 | furniture | pages [21] -->
m

<!-- b001989 | furniture | pages [21] -->
m

<!-- b001990 | furniture | pages [21] -->
m

<!-- b001991 | furniture | pages [21] -->
m

<!-- b001992 | furniture | pages [21] -->
m

<!-- b001993 | furniture | pages [21] -->
m

<!-- b001994 | furniture | pages [21] -->
m

<!-- b001995 | furniture | pages [21] -->
m

<!-- b001996 | furniture | pages [21] -->
m

<!-- b001997 | furniture | pages [21] -->
m

<!-- b001998 | furniture | pages [21] -->
m

<!-- b001999 | furniture | pages [21] -->
m

<!-- b002000 | furniture | pages [21] -->
m

<!-- b002001 | furniture | pages [21] -->
m

<!-- b002002 | furniture | pages [21] -->
m

<!-- b002003 | furniture | pages [21] -->
m

<!-- b002004 | furniture | pages [21] -->
m

<!-- b002005 | furniture | pages [21] -->
m

<!-- b002006 | furniture | pages [21] -->
m

<!-- b002007 | furniture | pages [21] -->
m

<!-- b002008 | furniture | pages [21] -->
m

<!-- b002009 | furniture | pages [21] -->
m

<!-- b002010 | furniture | pages [21] -->
m

<!-- b002011 | furniture | pages [21] -->
m

<!-- b002012 | furniture | pages [21] -->
m

<!-- b002013 | furniture | pages [21] -->
m

<!-- b002014 | furniture | pages [21] -->
m

<!-- b002015 | furniture | pages [21] -->
m

<!-- b002016 | furniture | pages [21] -->
m

<!-- b002017 | furniture | pages [21] -->
m

<!-- b002018 | furniture | pages [21] -->
m

<!-- b002019 | furniture | pages [21] -->
m

<!-- b002020 | furniture | pages [21] -->
m

<!-- b002021 | furniture | pages [21] -->
m

<!-- b002022 | furniture | pages [21] -->
m

<!-- b002023 | furniture | pages [21] -->
m

<!-- b002024 | furniture | pages [21] -->
m

<!-- b002025 | furniture | pages [21] -->
m

<!-- b002026 | furniture | pages [21] -->
m

<!-- b002027 | furniture | pages [21] -->
m

<!-- b002028 | furniture | pages [21] -->
m

<!-- b002029 | furniture | pages [21] -->
m

<!-- b002030 | furniture | pages [21] -->
m

<!-- b002031 | furniture | pages [21] -->
m

<!-- b002032 | furniture | pages [21] -->
m

<!-- b002033 | furniture | pages [21] -->
m

<!-- b002034 | furniture | pages [21] -->
m

<!-- b002035 | furniture | pages [21] -->
m

<!-- b002036 | furniture | pages [21] -->
m

<!-- b002037 | furniture | pages [21] -->
m

<!-- b002038 | furniture | pages [21] -->
m

<!-- b002039 | furniture | pages [21] -->
m

<!-- b002040 | furniture | pages [21] -->
m

<!-- b002041 | furniture | pages [21] -->
m

<!-- b002042 | furniture | pages [21] -->
m

<!-- b002043 | furniture | pages [21] -->
m

<!-- b002044 | furniture | pages [21] -->
m

<!-- b002045 | furniture | pages [21] -->
m

<!-- b002046 | furniture | pages [21] -->
m

<!-- b002047 | furniture | pages [21] -->
m

<!-- b002048 | furniture | pages [21] -->
m

<!-- b002049 | furniture | pages [21] -->
m

<!-- b002050 | furniture | pages [21] -->
m

<!-- b002051 | furniture | pages [21] -->
m

<!-- b002052 | furniture | pages [21] -->
m

<!-- b002053 | furniture | pages [21] -->
m

<!-- b002054 | furniture | pages [21] -->
m

<!-- b002055 | furniture | pages [21] -->
m

<!-- b002056 | furniture | pages [21] -->
m

<!-- b002057 | furniture | pages [21] -->
m

<!-- b002058 | furniture | pages [21] -->
m

<!-- b002059 | furniture | pages [21] -->
m

<!-- b002060 | furniture | pages [21] -->
m

<!-- b002061 | furniture | pages [21] -->
m

<!-- b002062 | furniture | pages [21] -->
m

<!-- b002063 | furniture | pages [21] -->
m

<!-- b002064 | furniture | pages [21] -->
m

<!-- b002065 | furniture | pages [21] -->
m

<!-- b002066 | furniture | pages [21] -->
m

<!-- b002067 | furniture | pages [21] -->
m

<!-- b002068 | furniture | pages [21] -->
m

<!-- b002069 | furniture | pages [21] -->
m

<!-- b002070 | furniture | pages [21] -->
m

<!-- b002071 | furniture | pages [21] -->
m

<!-- b002072 | furniture | pages [21] -->
m

<!-- b002073 | furniture | pages [21] -->
m

<!-- b002074 | furniture | pages [21] -->
m

<!-- b002075 | furniture | pages [21] -->
m

<!-- b002076 | furniture | pages [21] -->
m

<!-- b002077 | furniture | pages [21] -->
m

<!-- b002078 | furniture | pages [21] -->
m

<!-- b002079 | furniture | pages [21] -->
m

<!-- b002080 | furniture | pages [21] -->
m

<!-- b002081 | furniture | pages [21] -->
m

<!-- b002082 | furniture | pages [21] -->
m

<!-- b002083 | furniture | pages [21] -->
m

<!-- b002084 | furniture | pages [21] -->
m

<!-- b002085 | furniture | pages [21] -->
m

<!-- b002086 | furniture | pages [21] -->
m

<!-- b002087 | furniture | pages [21] -->
m

<!-- b002088 | furniture | pages [21] -->
m

<!-- b002089 | furniture | pages [21] -->
m

<!-- b002090 | furniture | pages [21] -->
m

<!-- b002091 | furniture | pages [21] -->
m

<!-- b002092 | furniture | pages [21] -->
m

<!-- b002093 | furniture | pages [21] -->
m

<!-- b002094 | furniture | pages [21] -->
m

<!-- b002095 | furniture | pages [21] -->
m

<!-- b002096 | furniture | pages [21] -->
m

<!-- b002097 | furniture | pages [21] -->
m

<!-- b002098 | furniture | pages [21] -->
m

<!-- b002099 | furniture | pages [21] -->
m

<!-- b002100 | furniture | pages [21] -->
m

<!-- b002101 | furniture | pages [21] -->
m

<!-- b002102 | furniture | pages [21] -->
m

<!-- b002103 | furniture | pages [21] -->
m

<!-- b002104 | furniture | pages [21] -->
m

<!-- b002105 | furniture | pages [21] -->
m

<!-- b002106 | furniture | pages [21] -->
m

<!-- b002107 | furniture | pages [21] -->
m

<!-- b002108 | furniture | pages [21] -->
m

<!-- b002109 | furniture | pages [21] -->
m

<!-- b002110 | furniture | pages [21] -->
m

<!-- b002111 | furniture | pages [21] -->
m

<!-- b002112 | furniture | pages [21] -->
m

<!-- b002113 | furniture | pages [21] -->
m

<!-- b002114 | furniture | pages [21] -->
m

<!-- b002115 | furniture | pages [21] -->
m

<!-- b002116 | furniture | pages [21] -->
m

<!-- b002117 | furniture | pages [21] -->
m

<!-- b002118 | furniture | pages [21] -->
m

<!-- b002119 | furniture | pages [21] -->
m

<!-- b002120 | furniture | pages [21] -->
m

<!-- b002121 | furniture | pages [21] -->
m

<!-- b002122 | furniture | pages [21] -->
m

<!-- b002123 | furniture | pages [21] -->
m

<!-- b002124 | furniture | pages [21] -->
m

<!-- b002125 | furniture | pages [21] -->
m

<!-- b002126 | furniture | pages [21] -->
m

<!-- b002127 | furniture | pages [21] -->
m

<!-- b002128 | furniture | pages [21] -->
m

<!-- b002129 | furniture | pages [21] -->
m

<!-- b002130 | furniture | pages [21] -->
m

<!-- b002131 | furniture | pages [21] -->
m

<!-- b002132 | furniture | pages [21] -->
m

<!-- b002133 | furniture | pages [21] -->
m

<!-- b002134 | furniture | pages [21] -->
m

<!-- b002135 | furniture | pages [21] -->
m

<!-- b002136 | furniture | pages [21] -->
m

<!-- b002137 | furniture | pages [21] -->
m

<!-- b002138 | furniture | pages [21] -->
m

<!-- b002139 | furniture | pages [21] -->
m

<!-- b002140 | furniture | pages [21] -->
m

<!-- b002141 | furniture | pages [21] -->
m

<!-- b002142 | furniture | pages [21] -->
m

<!-- b002143 | furniture | pages [21] -->
m

<!-- b002144 | furniture | pages [21] -->
m

<!-- b002145 | furniture | pages [21] -->
m

<!-- b002146 | furniture | pages [21] -->
m

<!-- b002147 | furniture | pages [21] -->
m

<!-- b002148 | furniture | pages [21] -->
m

<!-- b002149 | furniture | pages [21] -->
m

<!-- b002150 | furniture | pages [21] -->
m

<!-- b002151 | furniture | pages [21] -->
m

<!-- b002152 | furniture | pages [21] -->
m

<!-- b002153 | furniture | pages [21] -->
m

<!-- b002154 | furniture | pages [21] -->
m

<!-- b002155 | furniture | pages [21] -->
m

<!-- b002156 | furniture | pages [21] -->
m

<!-- b002157 | furniture | pages [21] -->
m

<!-- b002158 | furniture | pages [21] -->
m

<!-- b002159 | furniture | pages [21] -->
m

<!-- b002160 | furniture | pages [21] -->
m

<!-- b002161 | furniture | pages [21] -->
m

<!-- b002162 | furniture | pages [21] -->
m

<!-- b002163 | furniture | pages [21] -->
m

<!-- b002164 | furniture | pages [21] -->
m

<!-- b002165 | furniture | pages [21] -->
m

<!-- b002166 | furniture | pages [21] -->
m

<!-- b002167 | furniture | pages [21] -->
m

<!-- b002168 | furniture | pages [21] -->
m

<!-- b002169 | furniture | pages [21] -->
m

<!-- b002170 | furniture | pages [21] -->
m

<!-- b002171 | furniture | pages [21] -->
m

<!-- b002172 | furniture | pages [21] -->
m

<!-- b002173 | furniture | pages [21] -->
m

<!-- b002174 | furniture | pages [21] -->
m

<!-- b002175 | furniture | pages [21] -->
m

<!-- b002176 | furniture | pages [21] -->
m

<!-- b002177 | furniture | pages [21] -->
m

<!-- b002178 | furniture | pages [21] -->
m

<!-- b002179 | furniture | pages [21] -->
m

<!-- b002180 | furniture | pages [21] -->
m

<!-- b002181 | furniture | pages [21] -->
m

<!-- b002182 | furniture | pages [21] -->
m

<!-- b002183 | furniture | pages [21] -->
m

<!-- b002184 | furniture | pages [21] -->
m

<!-- b002185 | furniture | pages [21] -->
m

<!-- b002186 | furniture | pages [21] -->
m

<!-- b002187 | furniture | pages [21] -->
m

<!-- b002188 | furniture | pages [21] -->
m

<!-- b002189 | furniture | pages [21] -->
m

<!-- b002190 | furniture | pages [21] -->
m

<!-- b002191 | furniture | pages [21] -->
m

<!-- b002192 | furniture | pages [21] -->
m

<!-- b002193 | furniture | pages [21] -->
m

<!-- b002194 | furniture | pages [21] -->
m

<!-- b002195 | furniture | pages [21] -->
m

<!-- b002196 | furniture | pages [21] -->
m

<!-- b002197 | furniture | pages [21] -->
m

<!-- b002198 | furniture | pages [21] -->
m

<!-- b002199 | furniture | pages [21] -->
m

<!-- b002200 | furniture | pages [21] -->
m

<!-- b002201 | furniture | pages [21] -->
m

<!-- b002202 | furniture | pages [21] -->
m

<!-- b002203 | furniture | pages [21] -->
m

<!-- b002204 | furniture | pages [21] -->
m

<!-- b002205 | furniture | pages [21] -->
m

<!-- b002206 | furniture | pages [21] -->
m

<!-- b002207 | furniture | pages [21] -->
m

<!-- b002208 | furniture | pages [21] -->
m

<!-- b002209 | furniture | pages [21] -->
m

<!-- b002210 | furniture | pages [21] -->
m

<!-- b002211 | furniture | pages [21] -->
m

<!-- b002212 | furniture | pages [21] -->
m

<!-- b002213 | furniture | pages [21] -->
m

<!-- b002214 | furniture | pages [21] -->
m

<!-- b002215 | furniture | pages [21] -->
m

<!-- b002216 | furniture | pages [21] -->
m

<!-- b002217 | furniture | pages [21] -->
m

<!-- b002218 | furniture | pages [21] -->
m

<!-- b002219 | furniture | pages [21] -->
m

<!-- b002220 | furniture | pages [21] -->
m

<!-- b002221 | furniture | pages [21] -->
m

<!-- b002222 | furniture | pages [21] -->
m

<!-- b002223 | furniture | pages [21] -->
m

<!-- b002224 | furniture | pages [21] -->
m

<!-- b002225 | furniture | pages [21] -->
m

<!-- b002226 | furniture | pages [21] -->
m

<!-- b002227 | furniture | pages [21] -->
m

<!-- b002228 | furniture | pages [21] -->
m

<!-- b002229 | furniture | pages [21] -->
m

<!-- b002230 | furniture | pages [21] -->
m

<!-- b002231 | furniture | pages [21] -->
m

<!-- b002232 | furniture | pages [21] -->
m

<!-- b002233 | furniture | pages [21] -->
m

<!-- b002234 | furniture | pages [21] -->
m

<!-- b002235 | furniture | pages [21] -->
m

<!-- b002236 | furniture | pages [21] -->
m

<!-- b002237 | furniture | pages [21] -->
m

<!-- b002238 | furniture | pages [21] -->
m

<!-- b002239 | furniture | pages [21] -->
m

<!-- b002240 | furniture | pages [21] -->
m

<!-- b002241 | furniture | pages [21] -->
m

<!-- b002242 | furniture | pages [21] -->
m

<!-- b002243 | furniture | pages [21] -->
m

<!-- b002244 | furniture | pages [21] -->
m

<!-- b002245 | furniture | pages [21] -->
m

<!-- b002246 | furniture | pages [21] -->
m

<!-- b002247 | furniture | pages [21] -->
m

<!-- b002248 | furniture | pages [21] -->
m

<!-- b002249 | furniture | pages [21] -->
m

<!-- b002250 | furniture | pages [21] -->
m

<!-- b002251 | furniture | pages [22] -->
Team # 2500759

<!-- b002252 | furniture | pages [22] -->
Page 22 of 26

<!-- b002254 | prose | pages [22] -->
Through 10-fold cross-validation and Bootstrap resampling, we obtained prediction intervals and confidence levels for both models. In the gold medal prediction model, the MSE of the test set was 6.83, and the RMSE was 2.61. Although these values were slightly higher compared to the training set, the MAE was 0.52, and the MAPE was 14.47%, indicating that the model’s accuracy remains acceptable for new data. The total medal prediction model showed more stable performance, with lower MSE and RMSE, indicating higher predictive accuracy. These results are summarized in Table 5.

<!-- b002255 | caption | pages [22] -->
Table 5: Model Evaluation Metrics

<!-- b002256 | prose | pages [22] -->
Gold Total Training Test Training Test MSE 1.33 6.83 28.5 6.46 RMSE 1.16 2.61 5.34 2.54 MAE 1.49 0.52 3.68 1.04 MAPE 17.50% 14.47% 18.63% 16.13%

<!-- b002257 | prose | pages [22] -->
2. Robustness evaluation

<!-- b002258 | prose | pages [22] -->
To assess the robustness of the model, we focused on the R² value and the R-squared line plot from 10-fold cross-validation, as shown in Figs. 17(a)-(b). The results showed that both the gold medal and total medal prediction models had R² values close to 1, indicating that the models fit the data well and demonstrate consistent performance across different datasets, showcasing strong generalizability.

<!-- b002259 | prose | pages [22] -->
(a) (b)

<!-- b002260 | caption | pages [22] -->
Figure 17: R2 Values Across 10-Fold Cross-Validation

<!-- b002261 | heading | pages [22] -->
7 Model Analysis

<!-- b002262 | heading | pages [22] -->
7.1 Strength

<!-- b002263 | prose | pages [22] -->
The innovation and advantages of this study lie in the development of a predictive model for Olympic medal counts by integrating the PCA-LSTM-enhanced XGBoost- Bootstrap algorithm. Additionally, it conducts a comprehensive validation of the model’s accuracy and stability through various statistical methods, while employing a DID frame- work to assess the impact of coaching changes on Olympic medal counts. This is specifi- cally reflected in the following aspects:

<!-- b002264 | prose | pages [22, 23] -->
关注数学模型 • The introduction of the Bootstrap resampling method facilitates confidence interval estimation for the predictive outcomes, quantifying the model’s uncertainty and bolstering the credibility of the results. Additionally, the application of parallel trend hypothesis testing ensures that the experimental and control groups exhibited consistent medal trend patterns prior to coaching changes, further enhancing the stability of the model and the accuracy of inferences.

<!-- b002265 | furniture | pages [22] -->
2

<!-- b002266 | furniture | pages [22] -->
MATHmodels

<!-- b002267 | furniture | pages [22] -->
获取更多资讯

<!-- b002268 | furniture | pages [23] -->
Team # 2500759

<!-- b002269 | furniture | pages [23] -->
Page 23 of 26

<!-- b002271 | prose | pages [23] -->
• By integrating SHAP value analysis, this study conducts a thorough assessment of the contributions of different sports to medal counts, revealing key factors that in- fluence outcomes. Notably, when analyzing host nations, the findings illustrate the home advantage’s significant effect on medal totals, thereby enhancing the model’s interpretability and providing more actionable insights for decision-making.

<!-- b002272 | prose | pages [23] -->
• The use of the DID model allows for the evaluation of the causal effects of coach- 微信公众号：数学模型 ing changes on medal counts, providing an accurate quantification of the impact of such changes on Olympic performance and ensuring the reliability of causal in- ferences. Furthermore, the combination of PCA for dimensionality reduction and LSTM for trend modeling enhances the predictive accuracy of medal counts, show- casing strong modeling capabilities, particularly in addressing complex nonlinear relationships and time series data.

<!-- b002273 | heading | pages [23] -->
7.2 Weekness and Further Discussion

<!-- b002274 | prose | pages [23] -->
Our model has several limitations and incompatibilities. For instance, the computa- tional cost of the XGBoost and Bootstrap methods is relatively high, particularly when 微信号：MATHmodels dealing with large datasets, which affects the model’s real-time applicability. Addition- ally, the application of PCA for dimensionality reduction may lead to information loss, thereby impacting the model’s performance in capturing complex relationships. While LSTM are capable of identifying trends, their predictive ability is limited when it comes to sudden events and drastic fluctuations, which reduces the robustness of the model. Fur- thermore, the DID model assumes that the impact of coaching changes on medal counts is linear; however, in reality, these effects may be nonlinear, resulting in a failure to ad- equately capture the complex relationships present in the data and affecting the accuracy of causal inferences.

<!-- b002275 | prose | pages [23] -->
Future improvements to the model focus on two key areas. First, the Olympic medal count prediction model will enhance its integration of fluctuations from the Games, po- litical factors, and athlete performance variations through advanced ensemble learning techniques. By optimizing weighted averaging and stacked modeling, the model will in- corporate a wider range of variables and improve short-term predictive accuracy via a robust real-time data update mechanism. The use of reinforcement learning will further strengthen its long-term forecasting abilities, enhancing adaptability to sudden events and policy changes, while also improving computational efficiency for better timeliness and accuracy in predictions. Second, the enhanced-DID model will merge differentiated im- pact analysis with deep learning techniques to refine medal predictions. By incorporating stochastic simulations, this model will dynamically adjust the effects of coaching changes on medal counts, significantly boosting its adaptability in fluctuating environments and improving overall predictive effectiveness.

<!-- b002276 | furniture | pages [24] -->
Team # 2500759

<!-- b002277 | furniture | pages [24] -->
Page 24 of 26

<!-- b002278 | heading | pages [24] -->
8 Memorandum

<!-- b002279 | prose | pages [24] -->
To: International Olympic Committee

<!-- b002280 | prose | pages [24] -->
From: Team #2500759

<!-- b002281 | prose | pages [24] -->
Subject: 2028 Olympics Medal Prediction and Insights

<!-- b002282 | prose | pages [24] -->
Date: January 26, 2025

<!-- b002283 | prose | pages [24] -->
Dear Members of International Olympic Committee,

<!-- b002284 | prose | pages [24] -->
We are pleased to submit our solution to the medal prediction model for the 2028 Los Angeles Summer Olympics. Our team developed this model based on the data from the 2024 Paris Olympics and additional background information, offering both precise medal predictions and valuable insights for improving Olympic performance.

<!-- b002285 | prose | pages [24] -->
To construct the model, we utilize historical medal data and employ a PCA-LSTM- enhanced XGBoost-Bootstrap approach for preliminary predictions. Subsequently, we adjust these predictions by considering the event configurations and competitive structures of the 2024 Olympic Games, analyzing how these factors influence the medal counts of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m different countries. To estimate the uncertainty in our predictions, we provide confidence m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m intervals for gold medals and total medal counts. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m An essential component of our model is the analysis of the "great coach" effect, m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m which we integrate using the DID model. By comparing countries with and without m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m coaching changes, we estimate the incremental impact of coaching transitions on medal outcomes. We fit the model using OLS and conduct statistical significance tests as well as parallel trends tests to ensure the reliability of our results.

<!-- b002286 | prose | pages [24] -->
Beyond simply predicting medal counts, our model also offers insights on optimizing Olympic performance. It highlights which countries are likely to make breakthroughs in specific sports by strategically increasing investments in those areas. Furthermore, our model suggests potential improvements in the types and settings of Olympic events, recommending adjustments that could help maximize medal outcomes. These findings can guide the decision-making processes of National Olympic Committees as they plan for the 2028 Olympics and beyond.

<!-- b002287 | prose | pages [24] -->
Thank you for providing the opportunity to participate in this important project. We look forward to your valuable feedback.

<!-- b002288 | prose | pages [24] -->
Sincerely yours,

<!-- b002289 | furniture | pages [24] -->
Team #2500759

<!-- b002290 | prose | pages [24] -->
关注数学模型

<!-- b002291 | furniture | pages [24] -->
2

<!-- b002292 | furniture | pages [24] -->
MATHmodels

<!-- b002293 | furniture | pages [24] -->
获取更多资讯

<!-- b002294 | furniture | pages [25] -->
Team # 2500759

<!-- b002295 | furniture | pages [25] -->
Page 25 of 26

<!-- b002296 | heading | pages [25] -->
References

<!-- b002297 | references | pages [25] -->
[1] SM Khorshed Alam, Peiyue Li, Mahbubur Rahman, Misbah Fida, and Vetrimu-

<!-- b002298 | references | pages [25] -->
rugan Elumalai. Key factors affecting groundwater nitrate levels in the yinchuan

<!-- b002299 | references | pages [25] -->
region, northwest china: Research using the extreme gradient boosting (xgboost)

<!-- b002300 | references | pages [25] -->
model with the shapley additive explanations (shap) method. Environmental Pollu-

<!-- b002301 | references | pages [25] -->
tion, 364:125336, 2025.

<!-- b002302 | references | pages [25] -->
[2] Ruobing Chen, Mingxin Zhang, Xiao Xu, and Yongfeng Liu. Game-related statistics

<!-- b002303 | references | pages [25] -->
for distinguishing winning and losing teams in olympic basketball: The impact of

<!-- b002304 | references | pages [25] -->
game pace. Journal of Sports Sciences, pages 1–12, 2025.

<!-- b002305 | references | pages [25] -->
[3] Yuejian Chen, Xuemei Liu, Meng Rao, Yong Qin, Zhipeng Wang, and Yuanjin Ji.

<!-- b002306 | references | pages [25] -->
Explicit speed-integrated lstm network for non-stationary gearbox vibration repre-

<!-- b002307 | references | pages [25] -->
微信公众号：数学模型

<!-- b002308 | references | pages [25] -->
sentation and fault detection under varying speed conditions. Reliability Engineering

<!-- b002309 | references | pages [25] -->
& System Safety, 254:110596, 2025.

<!-- b002310 | references | pages [25] -->
[4] Andrew Goodman-Bacon. Difference-in-differences with variation in treatment tim-

<!-- b002311 | references | pages [25] -->
ing. Journal of econometrics, 225(2):254–277, 2021.

<!-- b002312 | references | pages [25] -->
[5] Jiangtao Li, Xingqin An, Qingyong Li, Chao Wang, Haomin Yu, Xinyuan Zhou, and

<!-- b002313 | references | pages [25] -->
Yangli-ao Geng. Application of xgboost algorithm in the optimization of pollutant

<!-- b002314 | references | pages [25] -->
concentration. Atmospheric Research, 276:106238, 2022.

<!-- b002315 | references | pages [25] -->
[6] Wenlong Liao, Shouxiang Wang, Dechang Yang, Zhe Yang, Jiannong Fang, Chris-

<!-- b002316 | references | pages [25] -->
微信号：MATHmodels

<!-- b002317 | references | pages [25] -->
tian Rehtanz, and Fernando Porté-Agel. Timegpt in load forecasting: A large time

<!-- b002318 | references | pages [25] -->
series model perspective. Applied Energy, 379:124973, 2025.

<!-- b002319 | references | pages [25] -->
[7] Benjamin Lindemann, Benjamin Maschler, Nada Sahlab, and Michael Weyrich. A

<!-- b002320 | references | pages [25] -->
survey on anomaly detection for technical systems using lstm networks. Computers

<!-- b002321 | references | pages [25] -->
in Industry, 131:103498, 2021.

<!-- b002322 | references | pages [25] -->
[8] Tui H Nolan, Jeff Goldsmith, and David Ruppert. Bayesian functional principal

<!-- b002323 | references | pages [25] -->
components analysis via variational message passing with multilevel extensions.

<!-- b002324 | references | pages [25] -->
Bayesian Analysis, 20(1):1459–1485, 2025.

<!-- b002325 | references | pages [25] -->
[9] Cheng-Hong Yang, Borcy Lee, Yi-In Lee, Yu-Fang Chung, and Yu-Da Lin. An

<!-- b002326 | references | pages [25] -->
autoencoder-based arithmetic optimization clustering algorithm to enhance principal

<!-- b002327 | references | pages [25] -->
component analysis to study the relations between industrial market stock indices in

<!-- b002328 | references | pages [25] -->
real estate. Expert Systems with Applications, 266:126165, 2025.

<!-- b002329 | references | pages [25] -->
[10] Junyi Zhang, Xianglong Ma, Jialan Zhang, Deliang Sun, Xinzhi Zhou, Changlin

<!-- b002330 | references | pages [25] -->
Mi, and Haijia Wen. Insights into geospatial heterogeneity of landslide suscepti-

<!-- b002331 | references | pages [25] -->
bility based on the shap-xgboost model. Journal of environmental management,

<!-- b002332 | references | pages [25] -->
332:117357, 2023.

<!-- b002333 | furniture | pages [26] -->
Team # 2500759

<!-- b002334 | furniture | pages [26] -->
Page 26 of 26

<!-- b002335 | heading | pages [26] -->
Report on Use of AI

<!-- b002336 | ai_disclosure | pages [26] -->
1. OpenAI ChatGPT (January 25, 2025 version, ChatGPT-4)

<!-- b002337 | ai_disclosure | pages [26] -->
Query1: How PCA does reducing dimensions?

<!-- b002338 | ai_disclosure | pages [26] -->
Output: Start with data normalization as this is a prerequisite for PCA. Next, cal-

<!-- b002339 | ai_disclosure | pages [26] -->
culate the covariance matrix or correlation matrix, this step is to capture the relationship

<!-- b002340 | ai_disclosure | pages [26] -->
between variables. Then, eigenvalue decomposition is performed, and choosing the num-

<!-- b002341 | ai_disclosure | pages [26] -->
ber of principal components is a key step. Finally, the data is projected into the new

<!-- b002342 | ai_disclosure | pages [26] -->
feature space, which is the reduced dimensionality.

<!-- b002343 | ai_disclosure | pages [26] -->
2. OpenAI ChatGPT (January 25, 2025 version, ChatGPT-4)

<!-- b002344 | ai_disclosure | pages [26] -->
Query2: How to use SHAP?

<!-- b002345 | ai_disclosure | pages [26] -->
Output: SHAP is a game theory-based method for interpreting the predictions of a

<!-- b002346 | ai_disclosure | pages [26] -->
model. It helps to understand how the model makes a certain prediction by calculating the

<!-- b002347 | ai_disclosure | pages [26] -->
contribution of each feature to the model output. Assuming you have installed the SHAP

<!-- b002348 | ai_disclosure | pages [26] -->
library, you next need to choose a model to interpret. For example, you can use a trained

<!-- b002349 | ai_disclosure | pages [26] -->
random forest model and then use SHAP to interpret its predictions. The steps might

<!-- b002350 | ai_disclosure | pages [26] -->
include: loading the data, training the model, creating a SHAP interpreter, calculating the

<!-- b002351 | ai_disclosure | pages [26] -->
SHAP values, and finally visualizing the results. When loading data, you need to make

<!-- b002352 | ai_disclosure | pages [26] -->
sure that the data is preprocessed, such as normalized or coded categorical variables. Then

<!-- b002353 | ai_disclosure | pages [26] -->
train the model, e.g. with a random forest classifier. After that, create an interpreter object

<!-- b002354 | ai_disclosure | pages [26] -->
for SHAP, which may need to be passed in the model and data. When calculating SHAP

<!-- b002355 | ai_disclosure | pages [26] -->
values, you may need to pass in test samples using the interpreter’s shap_values method.

<!-- b002356 | ai_disclosure | pages [26] -->
3. OpenAI ChatGPT (January 25, 2025 version, ChatGPT-4)

<!-- b002357 | ai_disclosure | pages [26] -->
Query3: How do you quantify the impact of the great coach effect?

<!-- b002358 | ai_disclosure | pages [26] -->
Output: Using the number of medals as the dependent variable, consider factors

<!-- b002359 | ai_disclosure | pages [26] -->
such as historical medal counts, host country advantage, number of athletes, economic

<!-- b002360 | ai_disclosure | pages [26] -->
indicators (if any), and whether or not to bring in good coaches (as a dummy variable).

<!-- b002361 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b002362 | furniture | pages [26] -->
2

<!-- b002363 | furniture | pages [26] -->
MATHmodels

<!-- b002364 | furniture | pages [26] -->
获取更多资讯
