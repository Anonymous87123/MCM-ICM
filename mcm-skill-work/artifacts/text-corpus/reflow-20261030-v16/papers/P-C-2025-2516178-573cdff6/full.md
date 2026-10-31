# P-C-2025-2516178-573cdff6

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2025

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | furniture | pages [1] -->
2516178

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Revealing the Hidden Forces Shaping Olympic Success

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
Predicting the number of Olympic medals each country will win is crucial for various stakeholders. We therefore developed an Olympic medal model based on the dataset of past Olympic Games.

<!-- b000011 | prose | pages [1] -->
First, following model screening, we developed a dual-stage XGBoost model for pre- dicting Olympic medal counts. The dual-stage XGBoost model is composed of an XGBoost binary classifier and a TPE-XGBoost regressor whose hyperparameters are optimized by the Tree-structured Parzen Estimator algorithm. The classifier serves to analyze historical data patterns in depth and effectively identify the potential competitiveness of small-scale partici- pating countries. The regressor, on the other hand, accurately forecasts the specific number of medals for countries likely to win. Given the time-series nature of Olympic data, we employed

<!-- b000012 | prose | pages [1] -->
Second, an evaluation of the dual-stage XGBoost model's prediction performance was carried out. The model demonstrated outstanding performance in predicting the 2021 and 2024 Olympic Games, achieving a classification accuracy of 95% and an overall prediction accuracy of 68%, significantly outperforming existing Olympic prediction models. Confidence interval estimation was conducted using the non-parametric Bootstrap method. After 1000 iterative ver- ifications, the model's sample coverage probability exceeded 0.95, and the probability that the predicted values fell within the confidence interval was over 70%. Based on these results, we predicted the medal distribution for the 2028 Olympic Games. Moreover, we innovatively combined the classifier and regressor to quantify the first-time medal-winning probability of small Olympic countries. Simultaneously, SHAP value analysis was utilized to uncover the

<!-- b000013 | title | pages [1] -->
contribution of different events to each country's medal-winning.

<!-- b000014 | prose | pages [1] -->
Third, we quantified the Olympic medal-winning scores and then developed a differ- ence-in-differences model. The double-difference term incorporated in this model effectively controlled interfering variables other than the coach factor. For the Chinese and Dutch teams, the p-values of the regression coefficient tests of the model were 0.03 and 0.05 respectively, both reaching the significance level, providing reliable statistical evidence for the existence of the “great coach" effect. When applying this model to relevant projects of other countries, the predicted medal-number growth trend was highly consistent with the actual situation.

<!-- b000015 | title | pages [1] -->
Finally, the SHAP Summary Plot was utilized to analyze the mechanism through which

<!-- b000016 | prose | pages [1] -->
the standardized number of participants affects the number of Olympic medals. Based on this, a two-track optimization strategy was proposed: strategically expanding the overall participa- tion scale while focusing on developing emerging projects with potential competitive ad- vantages.

<!-- b000017 | prose | pages [1] -->
In addition, a sensitivity analysis was conducted to assess the model's responsiveness to changes in input parameters. The results indicated that the model exhibited high accuracy and robustness in handling diverse scenarios.

<!-- b000018 | keywords | pages [1] -->
Keywords: Dual-stage XGBoost; Non-parametric Bootstrap algorithm; DID model; SHAP model

<!-- b000019 | furniture | pages [2] -->
Page 2 of 27

<!-- b000020 | furniture | pages [2] -->
Team # 2516178

<!-- b000021 | heading | pages [2] -->
Table of Contents

<!-- b000022 | contents | pages [2] -->
1 Introduction.

<!-- b000023 | contents | pages [2] -->
3

<!-- b000024 | contents | pages [2] -->
1.1 Problem Background

<!-- b000025 | contents | pages [2] -->
.3

<!-- b000026 | contents | pages [2] -->
1.2 Restatement of the Problem.

<!-- b000027 | contents | pages [2] -->
.3

<!-- b000028 | contents | pages [2] -->
4

<!-- b000029 | contents | pages [2] -->
1.3 Our Work.

<!-- b000030 | contents | pages [2] -->
2 Assumptions and Justifications.

<!-- b000031 | contents | pages [2] -->
3Notations

<!-- b000032 | contents | pages [2] -->
5

<!-- b000033 | contents | pages [2] -->
4Model Preparation

<!-- b000034 | contents | pages [2] -->
5

<!-- b000035 | contents | pages [2] -->
4.1 Data Pre-processing

<!-- b000036 | contents | pages [2] -->
.5

<!-- b000037 | contents | pages [2] -->
5 Model I: Dual-staged XGBoost Medal Prediction....

<!-- b000038 | contents | pages [2] -->
6

<!-- b000039 | contents | pages [2] -->
5.1 Parameterization of Influencing Factors.

<!-- b000040 | contents | pages [2] -->
.6

<!-- b000041 | contents | pages [2] -->
5.2 Developing of the XGBoost Classifier

<!-- b000042 | contents | pages [2] -->
.8

<!-- b000043 | contents | pages [2] -->
5.3 Developing of the TPE-XGBoost Regressor.

<!-- b000044 | contents | pages [2] -->
..9

<!-- b000045 | contents | pages [2] -->
6 Evaluation and Application of the Dual-Stage XGBoost Model

<!-- b000046 | contents | pages [2] -->
.12

<!-- b000047 | contents | pages [2] -->
.12

<!-- b000048 | contents | pages [2] -->
6.1 Model Evaluation Metrics...

<!-- b000049 | contents | pages [2] -->
6.2 Evaluation of Model Prediction Accuracy.

<!-- b000050 | contents | pages [2] -->
.12

<!-- b000051 | contents | pages [2] -->
6.3 Solving Confidence Intervals with the Non-parametric Bootstrap Algorithm

<!-- b000052 | contents | pages [2] -->
.13

<!-- b000053 | contents | pages [2] -->
6.4 Application and Analysis of the Model for the 2028 Olympics...

<!-- b000054 | contents | pages [2] -->
.15

<!-- b000055 | contents | pages [2] -->
6.5 Analysis of the Correlation between China-US Olympic Medals and Events Based on

<!-- b000056 | contents | pages [2] -->
SHAP Values.....

<!-- b000057 | contents | pages [2] -->
.16

<!-- b000058 | contents | pages [2] -->
.17

<!-- b000059 | contents | pages [2] -->
7 Model II: DID Regression Evaluating the Great Coach Effect ..

<!-- b000060 | contents | pages [2] -->
7.1 Identifying Independent Variables .....

<!-- b000061 | contents | pages [2] -->
.18

<!-- b000062 | contents | pages [2] -->
7.2 DID Model Building

<!-- b000063 | contents | pages [2] -->
.19

<!-- b000064 | contents | pages [2] -->
.20

<!-- b000065 | contents | pages [2] -->
7.3 Solution of the Model

<!-- b000066 | contents | pages [2] -->
8 Novel Insights from SHAP Analysis in Olympic Performance...

<!-- b000067 | contents | pages [2] -->
.22

<!-- b000068 | contents | pages [2] -->
.24

<!-- b000069 | contents | pages [2] -->
.24

<!-- b000070 | contents | pages [2] -->
10 Model Evaluation

<!-- b000071 | contents | pages [2] -->
10.1 Strengths

<!-- b000072 | contents | pages [2] -->
.24

<!-- b000073 | contents | pages [2] -->
.25

<!-- b000074 | contents | pages [2] -->
10.2 Weaknesses .

<!-- b000075 | contents | pages [2] -->
References...

<!-- b000076 | contents | pages [2] -->
.25

<!-- b000077 | contents | pages [2] -->
.26

<!-- b000078 | contents | pages [2] -->
Report on Use of AI.

<!-- b000079 | contents | pages [2] -->
关注数学模型

<!-- b000080 | furniture | pages [2] -->
获取更多资讯

<!-- b000081 | furniture | pages [3] -->
Team # 2516178

<!-- b000082 | furniture | pages [3] -->
Page 3 of 27

<!-- b000083 | heading | pages [3] -->
1 Introduction

<!-- b000084 | heading | pages [3] -->
1.1 Problem Background

<!-- b000085 | prose | pages [3] -->
In 2024, people worldwide witnessed the first Olympic Games following the COVID-19 pandemic. This grand event held in Paris rekindled the public's enthusiasm for this renowned sports event and spurred the audience's anticipation for the 2028 Los Angeles Olympics, spe- cifically, how countries would perform in the upcoming Olympics. To address this question, this paper endeavors to predict the outcomes of the next Olympics through model-building.

<!-- b000086 | prose | pages [3] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000087 | caption | pages [3] -->
Figure 1 The handover celebration of the 2028 Los Angeles Olympics

<!-- b000088 | prose | pages [3] -->
Since Ball [1] developed a correlation-based scoring model, the methodology for predict- ing Olympic results has witnessed remarkable evolution. Prediction models have advanced from the early ordinary least squares regression (OLS) to a probability-model system based on the Poisson distribution, encompassing Poisson regression and negative binomial models. Re- cently, research has trended towards a dual-stage approach: initially estimating the probability of medal-winning and subsequently predicting the specific number of medals. The Mundlak transformation of the Tobit model and the Hurdle model are the most emblematic. Simultane- ously, the dimensions of prediction data have been continuously broadened, manifested in finer-grained data, an extended time span, and diverse explanatory variables. Nevertheless, during the data-expansion process, the validity of variables and the issue of multicollinearity must be carefully considered.

<!-- b000089 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000090 | prose | pages [3, 4] -->
Considering the information given and conditions provided in the problem statement, we conclude that 4 objectives must be completed to finish all the goals required.  Objective 1: Accurately reflect and predict the medal-less status of many countries.  Objective 2: Build a mathematical model to evaluate if and how much “great coach” effect and other factors work.  Objective 3: Predict changes in the role of momentum, analyze what factors influence this fluctuation, and use the conclusions to guide player play. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m  Objective 4: Evaluate the results of the prediction and apply them to other sports events.

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

<!-- b000382 | furniture | pages [3] -->
m

<!-- b000383 | furniture | pages [3] -->
m

<!-- b000384 | furniture | pages [3] -->
m

<!-- b000385 | furniture | pages [3] -->
m

<!-- b000386 | furniture | pages [3] -->
m

<!-- b000387 | furniture | pages [3] -->
m

<!-- b000388 | furniture | pages [3] -->
m

<!-- b000389 | furniture | pages [3] -->
m

<!-- b000390 | furniture | pages [3] -->
m

<!-- b000391 | furniture | pages [3] -->
m

<!-- b000392 | furniture | pages [3] -->
m

<!-- b000393 | furniture | pages [3] -->
m

<!-- b000394 | furniture | pages [3] -->
m

<!-- b000395 | furniture | pages [3] -->
m

<!-- b000396 | furniture | pages [3] -->
m

<!-- b000397 | furniture | pages [3] -->
m

<!-- b000398 | furniture | pages [3] -->
m

<!-- b000399 | furniture | pages [3] -->
m

<!-- b000400 | furniture | pages [3] -->
m

<!-- b000401 | furniture | pages [3] -->
m

<!-- b000402 | furniture | pages [3] -->
m

<!-- b000403 | furniture | pages [3] -->
m

<!-- b000404 | furniture | pages [3] -->
m

<!-- b000405 | furniture | pages [3] -->
m

<!-- b000406 | furniture | pages [3] -->
m

<!-- b000407 | furniture | pages [3] -->
m

<!-- b000408 | furniture | pages [3] -->
m

<!-- b000409 | furniture | pages [3] -->
m

<!-- b000410 | furniture | pages [3] -->
m

<!-- b000411 | furniture | pages [3] -->
m

<!-- b000412 | furniture | pages [3] -->
m

<!-- b000413 | furniture | pages [3] -->
m

<!-- b000414 | furniture | pages [3] -->
m

<!-- b000415 | furniture | pages [4] -->
Team # 2516178

<!-- b000416 | furniture | pages [4] -->
Page 4 of 27

<!-- b000418 | heading | pages [4] -->
1.3 Our Work

<!-- b000419 | caption | pages [4] -->
Figure 2 Overview of our work

<!-- b000420 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000421 | prose | pages [4] -->
We make the following basic assumptions to simplify the problem, each of which is well justified.  Assumption 1: Only consider historical medal data, event factors, and coaching; ignore external non-sports-specific factors.

<!-- b000422 | prose | pages [4] -->
⇒ Justification: Political changes, natural disasters, and economic crises can have an impact on a country's sports development, which are difficult to predict and quantify. By fo- cusing on historical medal-winning data, event-related factors, and coaching, we can establish a relatively stable and analyzable model.  Assumption 2: Coaches' impacts are comparable across countries and sports, overlooking cultural differences.

<!-- b000423 | prose | pages [4] -->
⇒ Justification: The cultural background of a coach should not have an impact on their coaching performance when working with different national teams. A committed coach is ex- pected to provide thorough and unsparing guidance to their athletes, regardless of the country they are coaching in.  Assumption 3: Olympic event rules and scoring systems are stable.

<!-- b000424 | prose | pages [4] -->
⇒ Justification: The International Olympic Committee (IOC) has the responsibility and ability to maintain the stability of the Olympic competition rules. Over the past century or so, regardless of how turbulent the global situation has been, the competition rules have always remained immune to the influence of international political situations. This is one of the reasons why the Olympic Games have always enjoyed great trust.  Assumption 4: Based on the resolutions officially approved by the IOC, when predicting

<!-- b000425 | prose | pages [4, 5] -->
关注数学模型 the medal count for the 2028 Los Angeles Olympics, each of the Cricket, Squash, Base- ball/Softball, Lacrosse, and Flag Football events will have 2 additional medals.

<!-- b000426 | furniture | pages [4] -->
2

<!-- b000427 | furniture | pages [4] -->
MATHmodels

<!-- b000428 | furniture | pages [4] -->
获取更多资讯

<!-- b000429 | furniture | pages [5] -->
Page 5 of 27

<!-- b000430 | furniture | pages [5] -->
Team # 2516178

<!-- b000432 | prose | pages [5] -->
⇒ Justification: The model in this paper is built as of the current time, considering only the known event changes. The International Olympic Committee has the authority to decide on adding competition events and their associated medal arrangements. Given the available infor- mation, we only consider the approved new events and their corresponding medal increments to ensure the model is based on existing and certain data.

<!-- b000433 | heading | pages [5] -->
3 Notations

<!-- b000434 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000435 | prose | pages [5] -->
Table 1Notations used in this paper

<!-- b000436 | heading | pages [5] -->
Symbol

<!-- b000437 | prose | pages [5] -->
Description The total number of participants of country i in the Olympic Games held in Peoplei,t year t i Country number ● Year t Whether a country is a host country Host y predicted value of the ith sample under b Bootstrap models The medal score in the ith year scorei ATTe

<!-- b000438 | heading | pages [5] -->
4 Model Preparation

<!-- b000439 | heading | pages [5] -->
4.1 Data Pre-processing

<!-- b000440 | heading | pages [5] -->
4.1.1 Time Limitation

<!-- b000441 | prose | pages [5] -->
First, we only adapt data from 1952 onwards as the post-war period saw significant trans- formations in the global sports landscape with countries recovering and rebuilding their sports systems, greater standardization of sports events ensuring data comparability and reliability, an expansion of international sports participation providing a more diverse dataset. 4.1.2 Identification and Processing of Invalid Data Additionally, we excluded the data of years when countries such as East Germany and Russia, which had major scandals, participated. To be specific, incidents such as large-scale boycotts as occurred at the 1980 Moscow and 1984 Los Angeles Games and the East German doping program responsible for 17 percent of the medals awarded to female athletes in 1972 skewed the medal count in the past. 4.1.3 Processing of NOC We also merged the names of certain teams. For instance, "Taiwan" and "Chinese Taipei" were combined. And some countries' names have random spaces or numbers attached, which have also been processed. Furthermore, certain countries that have ceased to exist, like Yugo- slavia, were excluded from our analysis.

<!-- b000442 | heading | pages [5] -->
4.1.4 Event Data Cleaning

<!-- b000443 | prose | pages [5, 6] -->
Moreover, in the dataset, there was some data with format or content errors, such as some data showing incorrect characters or being vacant. By identifying and eliminating or correcting such faulty data, we have improved the quality of the dataset and made our subsequent analysis more reliable and valid. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000444 | furniture | pages [6] -->
Team # 2516178

<!-- b000445 | furniture | pages [6] -->
Page 6 of 27

<!-- b000447 | heading | pages [6] -->
4.1.5 Processing of Participant Numbers

<!-- b000448 | prose | pages [6] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We not only tabulated the number of participants from each country in every event but m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m also recorded the number of medals each event yielded. Given that the number of participants m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m varies across different events-for instance, a football team has eleven players, which might lead m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000449 | prose | pages [6] -->
to the misconception of counting 11 medals per team — we standardized the number of par- ticipants. Specifically, we set the number of participants in the team with the fewest members in a particular event as 1 and scaled down the numbers of other countries proportionally.

<!-- b000450 | heading | pages [6] -->
4.1.6 Processing of the Medal Standings

<!-- b000451 | prose | pages [6] -->
By collating data on athletes' participation and medal-winning, we identified a set of coun- tries that have never won medals throughout history.

<!-- b000452 | heading | pages [6] -->
5 Model I: Dual-staged XGBoost Medal Prediction

<!-- b000453 | prose | pages [6] -->
Based on the theoretical frameworks of the Tobit model and the Hurdle model, this paper proposes an innovative dual-stage machine learning approach [2].

<!-- b000454 | prose | pages [6] -->
 Stage 1: Addressing the Zero-Medal Scenario A classifier is employed to specifically address the "zero-medal problem". The signifi- cance of this design lies in its ability to effectively capture the competitive characteristics of small-scale participating countries, preventing their medal-winning potential from being masked by the data characteristics of Olympic powerhouses. By deeply analyzing the latent patterns in historical data, the classifier can identify countries on the verge of breaking through the zero-medal barrier.

<!-- b000455 | prose | pages [6] -->
 Stage 2: Medal Quantity Prediction A regressor is then introduced to estimate the specific number of medals for countries predicted to win medals. This design avoids systematic bias that could result from directly predicting medal counts for all participating countries, thereby significantly enhancing the overall prediction accuracy of the model.

<!-- b000456 | prose | pages [6] -->
This divide-and-conquer strategy not only improves the reliability of the predictions but also offers a novel methodological perspective for future research. Subsequently, the task is to select the most appropriate model architecture from existing machine learning algorithms to handle these two prediction tasks.

<!-- b000457 | heading | pages [6] -->
5.1 Parameterization of Influencing Factors

<!-- b000458 | prose | pages [6] -->
In this section, we identify the core independent variables of the developed model and elaborate on their quantification methods.

<!-- b000459 | heading | pages [6] -->
5.1.1 Standardization of Total Participants Number

<!-- b000460 | prose | pages [6] -->
After standardization, we define the total number of participants of country 𝑖 in the Olympic Games held in year 𝑡 as 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡. To enhance the model's interpretability and the robustness of its predictions, we apply the equal-frequency binning algorithm to discretize

<!-- b000461 | prose | pages [6, 7] -->
关注数学模型 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡. Specifically, we transform the continuous variable 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡 into the discrete var- iable 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑑𝑖𝑠𝑐𝑟𝑒𝑡𝑒 based on the 20%, 40%, 60%, and 80% frequency quantiles. The math- ematical expression is as follows:

<!-- b000462 | furniture | pages [6] -->
2

<!-- b000463 | furniture | pages [6] -->
MATHmodels

<!-- b000464 | furniture | pages [6] -->
获取更多资讯

<!-- b000465 | furniture | pages [7] -->
Team # 2516178

<!-- b000466 | furniture | pages [7] -->
Page 7 of 27

<!-- b000468 | prose | pages [7] -->
(1)

<!-- b000469 | prose | pages [7] -->
微信公众号：数学模型 Here, 𝑄𝑛 denotes the value of the total number of participants at the 𝑛% quantile. Due to the non-constant marginal returns between participant and medal counts, discretization ena- bles us to abandon the constant returns assumption, thereby enhancing model robustness.

<!-- b000470 | heading | pages [7] -->
5.1.2 Standardization of Participants Number in Each Event

<!-- b000471 | prose | pages [7] -->
We define the standardized number of participants of country 𝑖 in a particular event at the 𝑡 -year Olympic Games as 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡 , where 𝑠𝑝𝑜𝑟𝑡 represents the specific event name. This variable is a continuous variable reflecting differences in geographical conditions and sports development levels across regions.

<!-- b000472 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000473 | heading | pages [7] -->
5.1.3 The "Host-country Effect”

<!-- b000474 | prose | pages [7] -->
We define the "host-country effect” on country 𝑖 in the Olympic Games as 𝐻𝑜𝑠𝑡. Host nations enjoy significant advantages: athletes avoid travel fatigue and benefit from venue fa- miliarity, while potentially receiving favorable officiating decisions. The seven-year prepara- tion period following host selection enables systematic athletic development, often yielding performance improvements in pre-host Olympics. These enhancements frequently persist in post-hosting due to elite athletes' multi-Olympic career spans.

<!-- b000475 | prose | pages [7] -->
To quantify these temporal host-country effects, we implement three binary variables [3]:

<!-- b000476 | prose | pages [7] -->
(2)

<!-- b000477 | prose | pages [7] -->
Here, 𝑡ℎ𝑜𝑠𝑡 denotes the year when country 𝑖 hosts the Olympics. The discrete variables 𝐻𝑜𝑠𝑡𝑡, 𝐻𝑜𝑠𝑡𝑡−4, and 𝐻𝑜𝑠𝑡𝑡+4 are respectively used to capture the "host-country effect” dur- ing the hosting year, four years before, and four years after the hosting year for country 𝑖.

<!-- b000478 | heading | pages [7] -->
5.1.4 Host Year

<!-- b000479 | prose | pages [7] -->
We define the year of the Olympic Games as 𝑦𝑒𝑎𝑟. This variable not only captures the historical evolution of the Olympic Games' scale but also reflects the development trends of global competitive sports among countries.

<!-- b000480 | heading | pages [7] -->
5.1.5 Event Medal Setup

<!-- b000481 | prose | pages [7, 8] -->
Regarding the event-specific medal setup, we denote the total number of medals allocated by the IOC for a particular 𝑠𝑝𝑜𝑟𝑡 at the 𝑡-year Olympics as 𝑀𝑒𝑑𝑎𝑙𝑡,𝑠𝑝𝑜𝑟𝑡. These variable m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m measures event-specific competitive intensity, with variations in medal distribution signifi- cantly impacting national performance outcomes, particularly in a country's specialized events.

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

<!-- b000737 | furniture | pages [7] -->
m

<!-- b000738 | furniture | pages [7] -->
m

<!-- b000739 | furniture | pages [7] -->
m

<!-- b000740 | furniture | pages [7] -->
m

<!-- b000741 | furniture | pages [7] -->
m

<!-- b000742 | furniture | pages [7] -->
m

<!-- b000743 | furniture | pages [7] -->
m

<!-- b000744 | furniture | pages [7] -->
m

<!-- b000745 | furniture | pages [7] -->
m

<!-- b000746 | furniture | pages [7] -->
m

<!-- b000747 | furniture | pages [7] -->
m

<!-- b000748 | furniture | pages [7] -->
m

<!-- b000749 | furniture | pages [7] -->
m

<!-- b000750 | furniture | pages [7] -->
m

<!-- b000751 | furniture | pages [7] -->
m

<!-- b000752 | furniture | pages [7] -->
m

<!-- b000753 | furniture | pages [7] -->
m

<!-- b000754 | furniture | pages [7] -->
m

<!-- b000755 | furniture | pages [7] -->
m

<!-- b000756 | furniture | pages [7] -->
m

<!-- b000757 | furniture | pages [7] -->
m

<!-- b000758 | furniture | pages [7] -->
m

<!-- b000759 | furniture | pages [7] -->
m

<!-- b000760 | furniture | pages [7] -->
m

<!-- b000761 | furniture | pages [7] -->
m

<!-- b000762 | furniture | pages [7] -->
m

<!-- b000763 | furniture | pages [7] -->
m

<!-- b000764 | furniture | pages [7] -->
m

<!-- b000765 | furniture | pages [7] -->
m

<!-- b000766 | furniture | pages [7] -->
m

<!-- b000767 | furniture | pages [7] -->
m

<!-- b000768 | furniture | pages [7] -->
m

<!-- b000769 | furniture | pages [7] -->
m

<!-- b000770 | furniture | pages [7] -->
m

<!-- b000771 | furniture | pages [7] -->
m

<!-- b000772 | furniture | pages [7] -->
m

<!-- b000773 | furniture | pages [7] -->
m

<!-- b000774 | furniture | pages [7] -->
m

<!-- b000775 | furniture | pages [7] -->
m

<!-- b000776 | furniture | pages [7] -->
m

<!-- b000777 | furniture | pages [7] -->
m

<!-- b000778 | furniture | pages [7] -->
m

<!-- b000779 | furniture | pages [7] -->
m

<!-- b000780 | furniture | pages [7] -->
m

<!-- b000781 | furniture | pages [7] -->
m

<!-- b000782 | furniture | pages [7] -->
m

<!-- b000783 | furniture | pages [7] -->
m

<!-- b000784 | furniture | pages [7] -->
m

<!-- b000785 | furniture | pages [7] -->
m

<!-- b000786 | furniture | pages [7] -->
m

<!-- b000787 | furniture | pages [7] -->
m

<!-- b000788 | furniture | pages [7] -->
m

<!-- b000789 | furniture | pages [7] -->
m

<!-- b000790 | furniture | pages [7] -->
m

<!-- b000791 | furniture | pages [7] -->
m

<!-- b000792 | furniture | pages [7] -->
m

<!-- b000793 | furniture | pages [7] -->
m

<!-- b000794 | furniture | pages [7] -->
m

<!-- b000795 | furniture | pages [7] -->
m

<!-- b000796 | furniture | pages [7] -->
m

<!-- b000797 | furniture | pages [7] -->
m

<!-- b000798 | furniture | pages [7] -->
m

<!-- b000799 | furniture | pages [7] -->
m

<!-- b000800 | furniture | pages [7] -->
m

<!-- b000801 | furniture | pages [7] -->
m

<!-- b000802 | furniture | pages [7] -->
m

<!-- b000803 | furniture | pages [7] -->
m

<!-- b000804 | furniture | pages [7] -->
m

<!-- b000805 | furniture | pages [7] -->
m

<!-- b000806 | furniture | pages [8] -->
Team # 2516178

<!-- b000807 | furniture | pages [8] -->
Page 8 of 27

<!-- b000809 | heading | pages [8] -->
5.1.6 Number of Medals Won by Each Country in Each Event

<!-- b000810 | prose | pages [8] -->
The total number of medals that country 𝑖 wins in the 𝑠𝑝𝑜𝑟𝑡 event at the 𝑡-year Olym- pics is defined as 𝑀𝑒𝑑𝑎𝑙𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡. These metric captures both a nation's event-specific compet- itive strength and its strategic sports development priorities. Event-level granularity enables more precise evaluation of competitive advantages.

<!-- b000811 | heading | pages [8] -->
5.2 Developing of the XGBoost Classifier

<!-- b000812 | prose | pages [8] -->
XGBoost, an efficient gradient-boosting algorithm, has shown remarkable performance in supervised learning [4]. Its superior predictive power and broad application scope lead us to select this algorithm for developing a binary classifier. The algorithm's schematic diagram is presented below:

<!-- b000813 | caption | pages [8] -->
Figure 3 XGBoost schematic diagram

<!-- b000814 | prose | pages [8] -->
Specifically, XGBoost's objective function comprises two components: the loss function and the regularization term:

<!-- b000815 | prose | pages [8] -->
(3)

<!-- b000816 | prose | pages [8] -->
The loss function 𝑙(𝑦𝑖, 𝑦𝑖̂) measures the discrepancy between the predicted value 𝑦𝑖̂ and 𝐾 the true value 𝑦𝑖. The regularization term ∑ controls the model's complexity. The 𝛺(𝑓𝑘) 𝑘=1 model's predicted value is the sum of the predictions from 𝐾 decision trees:

<!-- b000817 | prose | pages [8] -->
(4)

<!-- b000818 | prose | pages [8] -->
Where 𝑓𝑘(𝑥𝑖)  denotes the prediction of the 𝑘 th decision tree for sample 𝑥𝑖 . The XGBoost model generates the final prediction by aggregating the forecasts of multiple decision trees. Each decision tree, to some degree, captures diverse patterns and characteristics.

<!-- b000819 | prose | pages [8] -->
When building a medal-number classifier using the XGBoost model, we need to binarize the total number of medals won by different countries. For country 𝑖's performance at the 𝑡 year Olympics, we define the binary variable as:

<!-- b000820 | prose | pages [8] -->
(5)

<!-- b000821 | prose | pages [8, 9] -->
关注数学模型 To optimize the binary classifier's performance and address the data imbalance between large and small participating countries, thereby better capturing the competitive characteristics of small-scale participants, we only consider four indicators—𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡 , 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡 , 微信公众号：数学模型 𝑔𝑜𝑙𝑑, 𝐻𝑜𝑠𝑡, and 𝑦𝑒𝑎𝑟—as independent variables. By incorporating the dependent variables 𝑦𝑖,𝑡 𝑠𝑖𝑙𝑣𝑒𝑟, and 𝑦𝑖,𝑡 𝑏𝑟𝑜𝑛𝑧𝑒 into the objective function for XGBoost model training, we obtain three 𝑦𝑖,𝑡 target binary classifiers.

<!-- b000822 | furniture | pages [8] -->
2

<!-- b000823 | furniture | pages [8] -->
MATHmodels

<!-- b000824 | furniture | pages [8] -->
获取更多资讯

<!-- b000825 | furniture | pages [9] -->
Team # 2516178

<!-- b000826 | furniture | pages [9] -->
Page 9 of 27

<!-- b000828 | prose | pages [9] -->
To systematically evaluate the classifier's performance, we take total-medal prediction as an example and compare three models: XGBoost, binary logistic regression, and random forest. We use the ROC (Receiver Operating Characteristic) curve as an evaluation tool, which com- prehensively reflects the binary-classification model's discriminatory ability under different decision thresholds [5]. The resulting ROC curve is as follows:

<!-- b000829 | prose | pages [9] -->
XGBoost Random Forest Multiple Logistic Regression 微信号：MATHmodels

<!-- b000830 | caption | pages [9] -->
Figure 4 ROC curves of three models

<!-- b000831 | prose | pages [9] -->
Experimental results show that the XGBoost model significantly outperforms the others in classification, with the highest AUC (Area Under Curve) value of 0.957. This indicates a 95.7% accuracy in distinguishing between countries that "won gold medals" and those that "did not". This highly accurate prediction not only validates XGBoost's excellence in handling com- plex non-linear classification problems but also shows its ability to effectively capture multi- dimensional factors influencing Olympic medal winning. Based on these findings, choosing XGBoost as the final classifier is well-supported empirically.

<!-- b000832 | heading | pages [9] -->
5.3 Developing of the TPE-XGBoost Regressor

<!-- b000833 | prose | pages [9] -->
Next, we aim to build a machine-learning regressor for the countries predicted to win medals by the classifier. To enhance the regressor's prediction accuracy, we select six indicators —𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡,𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡, 𝐻𝑜𝑠𝑡, 𝑦𝑒𝑎𝑟, 𝑀𝑒𝑑𝑎𝑙𝑡,𝑠𝑝𝑜𝑟𝑡, and 𝑀𝑒𝑑𝑎𝑙𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡—as independent variables for precise model developion. Given the continuous nature of Olympic medal-count prediction, we adopt the mean squared error as the loss function:

<!-- b000834 | prose | pages [9] -->
(6) As every machine-learning regressor involves a set of hyperparameters, when the dimen- sionality of our independent variables is high, the proper setting of hyperparameters signifi- cantly affects the model's prediction accuracy and generalizability [6]. Commonly used hy- perparameter optimization methods include grid search (GS) and random search (RS). How- ever, these two methods demand substantial computational resources [7, 8]. Therefore, we em- ploy the Bayesian algorithm, specifically the Tree-structured Parzen Estimator (TPE), to de- velop a TPE-XGBoost model for optimizing XGBoost's feature selection and hyperparameter tuning.

<!-- b000835 | furniture | pages [10] -->
Page 10 of 27

<!-- b000836 | furniture | pages [10] -->
Team # 2516178

<!-- b000837 | prose | pages [10] -->
We continuously optimize the hyperparameter configuration, such as the maximum tree depth, learning rate, and minimum child weight, using TPE. This optimization process adap- tively balances the model's fitting capacity and generalization performance.

<!-- b000838 | prose | pages [10] -->
To evaluate the machine-learning results, we introduce the coefficient of determination R²:

<!-- b000839 | prose | pages [10] -->
n ∑(yi − yi)2 i=1 R² =1− (7) n ∑(yi− y)2 j=1 For the XGBoost model, we obtain the changes in R² of the prediction regression models for gold, silver, and bronze medals after TPE hyperparameter optimization, as presented in the following table:

<!-- b000840 | caption | pages [10] -->
Table 2 R² of the prediction regression model

<!-- b000841 | prose | pages [10] -->
After Optimization Before Optimization Gold 0.910 0.938 Silver 0.828 0.905 0.893 Bronze 0.841 To further prevent overfitting, we divide the dataset into a training set and a validation set using cross-validation. The training data is used to train the model, while the validation data is employed to ensure the model's ability to generalize beyond the training sample. Given the temporal evolution and dependency between the independent and dependent variables in this regression model, randomly splitting the dataset to build the model is inappropriate. Thus, we adopt the last block cross-validation method, which takes the time series into account by using the most recent data points as test data. This is reflected in our approach to using data from the 2008-2021 Olympic Games as the training set to predict the medal table of the 2024 Olympic Games when selecting the best machine-learning model to develop the regressor, as shown in the following figure:

<!-- b000842 | prose | pages [10] -->
Years of Olympic Games 1952 1956 2008 2012 2016 2020 2024 2028 Training of VaL Train Different Models Model Selection Train Test Model Benchmarking Train Test Model Benchmarking F.c. Forecasting Train

<!-- b000843 | caption | pages [10] -->
Figure 5 Model selecting, benchmarking and applying

<!-- b000844 | prose | pages [10] -->
We selected the Random Forest and Multiple Logistic Regression models for compara- tive analysis. The following is the visualized chart of R² for the three different models after

<!-- b000845 | prose | pages [10, 11] -->
关注数学模型 TPE hyperparameter optimization:

<!-- b000846 | furniture | pages [10] -->
获取更多资讯

<!-- b000847 | furniture | pages [11] -->
Team # 2516178

<!-- b000848 | furniture | pages [11] -->
Page 11 of 27

<!-- b000850 | prose | pages [11] -->
XGBoost Random Forest Multiple Logistic Regression

<!-- b000851 | prose | pages [11] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000852 | caption | pages [11] -->
Figure 6 Visualization of 3 models’ 𝑹𝟐

<!-- b000853 | prose | pages [11] -->
Based on the 𝑅2 values of the test and training sets, the XGBoost model exhibits the best performance. In gold-medal prediction, XGBoost achieves a test-set 𝑅2 of 0.938 and a train- ing – set 𝑅2 of 0.983. The random forest model, in contrast, has a test-set 𝑅2 of 0.724, while the linear regression model only reaches 0.570, indicating a significant performance disparity. This superiority is also evident in the prediction of silver and bronze medals.

<!-- b000854 | prose | pages [11] -->
Observing the scatter-point distribution, the prediction points of the XGBoost model are more closely clustered around the diagonal, suggesting the highest consistency between pre- dicted and actual values. Particularly when predicting many medals, XGBoost shows signifi- cantly less prediction deviation than the other two models.

<!-- b000855 | prose | pages [11] -->
Based on the width of the confidence interval, the XGBoost model yields the narrowest confidence band for its predictions, reflecting the highest level of stability and reliability.

<!-- b000856 | prose | pages [11, 12] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Finally，a dual-stage XGBoost framework can be established, where the first stage em- ploys an XGBoost classifier for preliminary screening, followed by a second stage utilizing a TPE-XGBoost regressor for precise prediction. The detailed workflow is illustrated as follows:

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

<!-- b001181 | furniture | pages [12] -->
Team # 2516178

<!-- b001182 | furniture | pages [12] -->
Page 12 of 27

<!-- b001184 | caption | pages [12] -->
Figure 7 Visualization of a dual-stage XGBoost’s worklow

<!-- b001185 | heading | pages [12] -->
6 Evaluation and Application of the Dual-Stage XGBoost Model

<!-- b001186 | heading | pages [12] -->
6.1 Model Evaluation Metrics

<!-- b001187 | prose | pages [12] -->
To further quantitatively assess the medal-prediction performance of the dual-stage XGBoost model, we introduce four evaluation parameters, 𝑀1–𝑀4.

<!-- b001188 | prose | pages [12] -->
- 𝑀1 is the overall prediction accuracy, used to evaluate the model's overall prediction capability.

<!-- b001189 | prose | pages [12] -->
- 𝑀2 refers to the prediction accuracy for medal-winning countries, measuring how ac- curately the model predicts countries that will win medals.

<!-- b001190 | prose | pages [12] -->
- 𝑀3 represents the prediction accuracy for zero-medal countries, evaluating the model's prediction accuracy for countries that won't win any medals.

<!-- b001191 | prose | pages [12] -->
- 𝑀4 is the accuracy within the 95% confidence interval, which gauges the stability and reliability of the model's predictions.

<!-- b001192 | prose | pages [12] -->
, (8) ,

<!-- b001193 | prose | pages [12] -->
Here, 𝐶𝑜𝑟𝑟𝑒𝑐𝑡𝑡𝑜𝑡𝑎𝑙denotes the total number of countries for which the medal count is accurately predicted. 𝑁𝑎𝑡𝑖𝑜𝑛𝑠𝑡𝑜𝑡𝑎𝑙 stands for the total number of countries included in the prediction. 𝐶𝑜𝑟𝑟𝑒𝑐𝑡𝑛𝑜𝑛𝑧𝑒𝑟𝑜 represents the number of countries for which medal-winning is accurately predicted, while Nationsmedal is the total number of countries that actually win medals. 𝐶𝑜𝑟𝑟𝑒𝑐𝑡𝑧𝑒𝑟𝑜 is the number of countries for which zero-medal status is accurately pre- dicted, and 𝑁𝑎𝑡𝑖𝑜𝑛𝑠𝑧𝑒𝑟𝑜  is the total number of countries with zero medals in reality. 𝑁𝑎𝑡𝑖𝑜𝑛𝑠𝑐𝑜𝑛𝑓𝑖𝑑𝑒𝑛𝑐𝑒 refers to the number of countries whose predicted values fall within the 95% confidence interval.

<!-- b001194 | heading | pages [12] -->
6.2 Evaluation of Model Prediction Accuracy

<!-- b001195 | prose | pages [12] -->
Subsequently, the dual-stage XGBoost model is evaluated by continuously applying the

<!-- b001196 | prose | pages [12, 13] -->
关注数学模型 last block cross-validation method. To be specific, the data from the Olympic Games held be- tween 1952 and 2016 are utilized to build a training set. After that, the trained model is em- ployed to predict the medal distribution of the 2021 Tokyo Olympics.

<!-- b001197 | furniture | pages [12] -->
2

<!-- b001198 | furniture | pages [12] -->
MATHmodels

<!-- b001199 | furniture | pages [12] -->
获取更多资讯

<!-- b001200 | furniture | pages [13] -->
Team # 2516178

<!-- b001201 | furniture | pages [13] -->
Page 13 of 27

<!-- b001203 | prose | pages [13] -->
Following this, the actual data of the 2021 Tokyo Olympics are incorporated into the train- ing set. The model is then retrained to predict the medal distribution of the 2024 Paris Olympics. The detailed process is depicted in Figure 5 Model selecting, benchmarking and applying.

<!-- b001204 | prose | pages [13] -->
Based on the quantitative assessment results of the dual-stage XGBoost model, we con- duct a systematic analysis of the prediction performance for the 2020 Tokyo Olympics and the 2024 Paris Olympics. Table below presents the prediction accuracy indicators (𝑀1–𝑀3) for different medal levels. 微信公众号：数学模型

<!-- b001205 | caption | pages [13] -->
Table 3 Evaluation Results of Prediction Performance for the 2020 and 2024 Olympics

<!-- b001206 | prose | pages [13] -->
2020 Tokyo 20204 Paris Prediction 𝑀1 𝑀2 𝑀3 𝑀1 𝑀2 𝑀3 Gold 59% 11% 92% 68% 22% 95% Silver 61% 14% 92% 63% 19% 95% Bronze 57% 13% 92% 68% 17% 95% Quantitative analysis reveals that the model's prediction accuracy for the 2024 Paris Olympics far exceeds that for the 2020 Tokyo Olympics. We can attribute this variance in pre- 微信号：MATHmodels diction precision to the unique impact of the COVID-19 pandemic on the 2021 Olympics. The pandemic significantly altered the training schedules and preparatory strategies of participating countries.

<!-- b001207 | prose | pages [13] -->
Notably, the 2024-oriented prediction model demonstrates astonishing accuracy. For in- stance, in gold-medal prediction, our dual-stage XGBoost model significantly outperforms cur- rent mainstream prediction models, such as the Dual-staged Random Forest and Tobit models [9], in terms of both gold-medal prediction accuracy (68%) and range prediction accuracy (22%).

<!-- b001208 | heading | pages [13] -->
6.3 Solving Confidence Intervals with the Non-parametric Bootstrap Algo-

<!-- b001209 | prose | pages [13] -->
rithm

<!-- b001210 | prose | pages [13] -->
When evaluating the confidence intervals of neural network models, traditional ap- proaches predominantly rely on the Delta method and the Mean-Variance Estimation (MVE) method. However, these methods exhibit limitations such as high computational costs and low coverage rates in practical applications [10].

<!-- b001211 | prose | pages [13] -->
Given that machine-learning prediction results typically do not conform to the normal- distribution assumption and are influenced by multiple non-linear factors, this study employs the non-parametric Bootstrap method to develop the confidence interval for the regressor part within the dual-stage XGBoost model.

<!-- b001212 | prose | pages [13] -->
During the model-building process, we generate B Bootstrap samples. In this paper, B is set to 1000. For each sample, we train an XGBoost model to obtain the predicted value yib̂ of 2̂ and the 𝑖th sample under 𝑏 Bootstrap models. Then, we calculate the model's variance 𝜎𝑦̂ regression mean 𝑦̂ as follows:

<!-- b001213 | furniture | pages [14] -->
Team # 2516178

<!-- b001214 | furniture | pages [14] -->
Page 14 of 27

<!-- b001215 | prose | pages [14] -->
, (9)

<!-- b001216 | prose | pages [14] -->
2 using the data from the validation set. Next, we estimate the error variance σe (10) Finally, for a new observation 𝑖, we develop its (1 −α) × 100% prediction interval as:

<!-- b001217 | prose | pages [14] -->
(11) Here, 𝛼 represents the significance level. Since we are conducting an evaluation with a 95% confidence factor, 𝛼 is set to 0.05. 𝑡1−𝛼/2 is the critical value of the t-distribution with (B-1) degrees of freedom.

<!-- b001218 | prose | pages [14] -->
To assess the performance of this prediction interval, we use the Prediction Interval Cov- erage Probability (PICP), calculated as follows:

<!-- b001219 | prose | pages [14] -->
(12)

<!-- b001220 | prose | pages [14] -->
where ci = 1 when the actual value falls within the prediction interval, andci = 0 oth- erwise.

<!-- b001221 | prose | pages [14] -->
After 1000 rounds of Bootstrap-sample training, the PICP values of the dual-stage XGBoost model all exceed 0.95, validating the reliability of the confidence-interval estimation.

<!-- b001222 | prose | pages [14] -->
We conduct a visual analysis of the prediction interval, taking the gold-medal prediction of the 2020 Tokyo Olympics as an example.

<!-- b001223 | caption | pages [14] -->
Figure 8 Visualization of prediction interval

<!-- b001224 | prose | pages [14] -->
Evidently, for countries with a relatively small number of medals per year, the probability that their actual results fall within the predicted confidence interval is markedly higher than that of Olympic powerhouses.

<!-- b001225 | prose | pages [14] -->
This phenomenon is attributed to the algorithmic features of the machine-learning model. When handling data points distant from the main sample distribution, the model tends to treat them as potential outliers, thereby moderately reducing the degree of fitting to these extreme situations.

<!-- b001226 | prose | pages [14] -->
Subsequently, we calculate the 𝑀4 values for the 2020 Tokyo Olympics and the 2024 Paris Olympics, as presented in the following table:

<!-- b001227 | caption | pages [14] -->
Table 4 Comparison of Prediction Interval Coverage Rates (𝑴𝟒) for the 2020 and 2024 Olympics

<!-- b001228 | prose | pages [14, 15] -->
关注数学模型 Gold Model Silver Model Bronze Model 2020 Tokyo 72% 75% 71% 2024 Paris 82% 81% 78% The relatively high 𝑀4 values suggest that the model can reliably capture the underlying patterns of Olympic medal counts.

<!-- b001229 | furniture | pages [14] -->
2

<!-- b001230 | furniture | pages [14] -->
MATHmodels

<!-- b001231 | furniture | pages [14] -->
获取更多资讯

<!-- b001232 | furniture | pages [15] -->
Team # 2516178

<!-- b001233 | furniture | pages [15] -->
Page 15 of 27

<!-- b001235 | prose | pages [15] -->
微信公众号：数学模型 Considering the sociological impact of the pandemic, the data for 2024 outperform those for 2021.

<!-- b001236 | heading | pages [15] -->
6.4 Application and Analysis of the Model for the 2028 Olympics

<!-- b001237 | heading | pages [15] -->
6.4.1 Prediction of Olympic Medal Counts and Confidence Intervals

<!-- b001238 | prose | pages [15] -->
Finally, we use the dataset from 1952 to 2024 to build the final dual-stage XGBoost pre- diction model and calculate the confidence interval with the non-parametric Bootstrap algo- rithm. The resulting table is presented below:

<!-- b001239 | caption | pages [15] -->
Table 5 Prediction Results and Confidence Intervals of Medals for 2028 Olympics

<!-- b001240 | prose | pages [15] -->
Sil- Bron- 95% CI Sil- 95% CI 微信号：MATHmodels Rank Team Gold Total 95% CI Gold ver ze ver Bronze 1 USA 45 48 49 142 [39.7, 51.0] [42.0, 54.0] [43.2, 55.0] 2 CHN 40 27 24 91 [35.0, 46.0] [23.0, 31.0] [20.0, 27.0] 3 JPN 20 12 13 45 [17.0, 23.0] [10.0, 14.0] [11.0, 15.0] 4 AUS 18 19 16 53 [15.0, 21.0] [16.0, 22.0] [13.0, 18.0] 5 FRA 16 26 22 64 [13.0, 18.0] [22.0, 30.0] [19.0, 25.0] By systematically comparing the actual results of the 2024 Olympics with the predicted results of the 2028 Olympics, we can observe the dynamic evolution of the Olympic competi- tive landscape, as the table shown below:

<!-- b001241 | caption | pages [15] -->
Table 6 Typical cases of predicted increases and decreases in the number of medals

<!-- b001242 | prose | pages [15] -->
Increased Cases Decreased Cases REF USA ROM SRB AZE KOR KEN IRI BUL CUB 2024 1 126 9 5 7 32 11 12 7 9 2028 4 142 19 10 9 25 7 9 5 8 Dif. 3 16 10 5 2 -7 -4 -3 -2 -1

<!-- b001243 | heading | pages [15] -->
6.4.2 Quantitative Analysis of First-Medal-winning Probability

<!-- b001244 | prose | pages [15] -->
In the Dual-stage XGBoost model, we developed an accurate probability assessment mechanism to quantify the likelihood of small participating countries winning their first Olym- pic medal.

<!-- b001245 | prose | pages [15] -->
For countries classified as having no winning possibility by the classifier (𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑦(i) = 0), we directly assign a winning probability of 0. For countries classified as having winning potential (𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑦(i) = 1), we transform the probability based on the predicted value of the regressor. If the regression-predicted value is less than 1, it is directly taken as the winning probability. If the predicted value is greater than 1, we consider it a certain-winning event and set the probability to 100%. For any country 𝑖 that has never won an Olympic medal, the probability 𝑃(𝐹𝑖𝑟𝑠𝑡𝑀𝑒𝑑𝑎𝑙|𝑖) of winning its first Olympic medal is defined as:

<!-- b001246 | furniture | pages [16] -->
Team # 2516178

<!-- b001247 | furniture | pages [16] -->
Page 16 of 27

<!-- b001248 | prose | pages [16] -->
(13)

<!-- b001249 | prose | pages [16] -->
Where 𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑦(𝑖)  reflects the binary-classification result of the classifier, and 𝑅𝑒𝑔𝑟𝑒𝑠𝑠𝑖𝑜𝑛(𝑖) represents the predicted value of the regressor.

<!-- b001250 | prose | pages [16] -->
Based on this framework, we set the winning-probability threshold at 0.2. When 𝑃(𝐹𝑖𝑟𝑠𝑡𝑀𝑒𝑑𝑎𝑙|𝑖) > 0.2, we consider the country to have significant potential to win medals in the next Olympics, as shown in table below:

<!-- b001251 | caption | pages [16] -->
Table 7 Probability Analysis of Countries with Significant Potential to Win Their First Medal

<!-- b001252 | prose | pages [16] -->
NOC NGA EST LAT FIN VEN MNE KSA SYR PRY 0.76 0.48 0.45 0.44 0.40 0.35 0.28 0.25 0.20 𝑃(𝐹𝑖𝑟𝑠𝑡𝑀𝑒𝑑𝑎𝑙|𝑖)

<!-- b001253 | heading | pages [16] -->
6.5 Analysis of the Correlation between China-US Olympic Medals and

<!-- b001254 | prose | pages [16] -->
Events Based on SHAP Values

<!-- b001255 | prose | pages [16] -->
SHAP (Shapley Additive Explanations), a sophisticated machine-learning model interpre- tation tool, can effectively quantify the contribution of features to prediction results.

<!-- b001256 | prose | pages [16] -->
Given that the XGBoost model intrinsically supports the calculation and integration of SHAP values, this study opts to apply it to explore the underlying relationship between event settings and a country's medal attainment [11].

<!-- b001257 | prose | pages [16] -->
Taking the prediction of the 2028 Olympics as an instance, we performed a SHAP-value 𝑔𝑜𝑙𝑑 analysis of the number of gold medals 𝑀𝑒𝑑𝑎𝑙𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡 that China and the United States are expected to win in each event:

<!-- b001258 | caption | pages [16] -->
Figure 9 Comparison of the SHAP Value Distributions of Olympic Events' Contribution to Gold

<!-- b001259 | prose | pages [16] -->
Medals in China and the United States The SHAP value magnitude directly reflects the influence degree of a specific event on a

<!-- b001260 | prose | pages [16, 17] -->
关注数学模型 country's gold-medal winning. For instance, the United States shows the largest SHAP value in the Athletics event, while China's SHAP value in this event is relatively small. This disparity indicates that the United States enjoys a significant competitive advantage in Athletics.

<!-- b001261 | furniture | pages [16] -->
2

<!-- b001262 | furniture | pages [16] -->
MATHmodels

<!-- b001263 | furniture | pages [16] -->
获取更多资讯

<!-- b001264 | furniture | pages [17] -->
Team # 2516178

<!-- b001265 | furniture | pages [17] -->
Page 17 of 27

<!-- b001267 | prose | pages [17] -->
Conversely, in the Weightlifting and Diving events, China demonstrates significantly 微信公众号：数学模型 higher SHAP values than the United States, suggesting that these are China's traditional strong- suit events.

<!-- b001268 | prose | pages [17] -->
To gain a deeper understanding of how event settings affect different countries, we carried out a more meticulous study. We used the SHAP method to conduct a quantitative analysis of the silver-medal prediction models for the 2028 Olympics in China and the United States.Fig- ures below respectively present the waterfall plots of event contribution levels for the United States and China:

<!-- b001269 | prose | pages [17] -->
微信号：MATHmodels

<!-- b001270 | caption | pages [17] -->
Figure 10 Analysis of the SHAP-value Waterfall Plot for U.S. 2028 Olympics Silver-medal Prediction

<!-- b001271 | prose | pages [17] -->
We can observe from the SHAP-value distribution of the United States (Figure 6.6) that the Swimming and Athletics events make significant positive contributions, with their SHAP values markedly higher than those of other events.This distribution feature indicates that the United States retains a strong competitive edge in these traditional advantageous events.

<!-- b001272 | prose | pages [17] -->
Observing from the SHAP-value distribution of the United States, the Swimming and Athletics events exhibit significant positive contributions, with their SHAP values markedly higher than those of other events. This distribution feature reveals that the United States retains a strong competitive edge in these traditional strong-suit events.

<!-- b001273 | caption | pages [17] -->
Figure 11 Analysis of the SHAP-value Waterfall Plot for U.S. 2028 Olympics Silver-medal Prediction

<!-- b001274 | prose | pages [17] -->
In contrast, the SHAP-value distribution in China presents a distinct pattern.The Swim- ming and Shooting events exert the most significant positive influences, suggesting a strong positive correlation with China's silver-medal-winning probability. This reflects the crucial im- portance of these events for China to achieve excellent results.

<!-- b001275 | prose | pages [17] -->
A comparative analysis reveals significant differences in the composition of advantageous events among different countries, which directly impacts their overall Olympic performance. The historical performance and development potential of an event are mirrored in the predic- tion model through the SHAP-value magnitude.

<!-- b001276 | prose | pages [17] -->
However, a country's final Olympic achievements are related not only to its own advan- tageous event types but also, to a greater extent, to the total number of medals allocated to each event in the Olympics. For events with a relatively large number of total medals, a country's investment in the development of these events is more likely to boost its final medal count.

<!-- b001277 | heading | pages [17] -->
7 Model II: DID Regression Evaluating the Great Coach Effect

<!-- b001278 | prose | pages [17, 18] -->
The “great coach” effect means that outstanding coaches can inspire the potential of teams or individuals through professional guidance, enabling them to surpass their limits and achieve remarkable results. Nevertheless, a country's medal count is influenced by multiple factors, including the host-country effect and athlete turnover.

<!-- b001279 | furniture | pages [18] -->
Team # 2516178

<!-- b001280 | furniture | pages [18] -->
Page 18 of 27

<!-- b001282 | heading | pages [18] -->
7.1 Identifying Independent Variables

<!-- b001283 | prose | pages [18] -->
To precisely verify and quantify the great coach effect, we first identify the independent variables necessary for developing this model:

<!-- b001284 | heading | pages [18] -->
7.1.1 Calculation of medal scores

<!-- b001285 | prose | pages [18] -->
For each athlete's medal results, we convert medal types into numerical values using map- ping rules to facilitate subsequent statistical analysis. The specific mapping rules are as follows:

<!-- b001286 | prose | pages [18] -->
0, Medal𝑖= “𝑁𝑜 𝑀𝑒𝑑𝑒𝑙” 1, Medal𝑖= “𝐵𝑟𝑜𝑛𝑧𝑒” (14) Score𝑖= { 2, Medal𝑖= “𝑆𝑖𝑙𝑣𝑒𝑟” 3, Medal𝑖= “𝐺𝑜𝑙𝑑” These rules transform medal types into numerical values, facilitating quantitative pro- cessing. Subsequently, we group the data by year and calculate the total medal score TotalScore𝑦𝑒𝑎𝑟for each year:

<!-- b001287 | prose | pages [18] -->
𝑛 (15) TotalScore𝑦𝑒𝑎𝑟= ∑ Score𝑖 𝑖=1 Where 𝑖 represents the 𝑖 th athlete in that year, and 𝑛 is the total number of athletes competing that year. Using this approach, we can obtain the annual total medal score of the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Chinese men's table-tennis team at the Olympics. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001288 | heading | pages [18] -->
7.1.2 Developion of the "Coaching Status" Variable

<!-- b001289 | prose | pages [18] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m To assess the coaching impact of Coach Alyson Annan, following the developion of pre- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m vious variables, we define a new variable, "Coaching Status". This variable is determined based m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001290 | prose | pages [18] -->
on whether Alyson Annan coached the Chinese and Dutch women's hockey teams in a given year, as described by the following formulas:

<!-- b001291 | prose | pages [18] -->
For the Chinese women's hockey team, we define the variable 𝐶𝑜𝑎𝑐ℎ_𝐶ℎ𝑖𝑛𝑎:

<!-- b001292 | prose | pages [18] -->
𝐶𝑜𝑎𝑐ℎ_𝐶ℎ𝑖𝑛𝑎= {0, 𝑌𝑒𝑎𝑟< 2022 (16) 𝑌𝑒𝑎𝑟≥2022 1, For the Dutch women's hockey team, we define the variable 𝐶𝑜𝑎𝑐ℎ_𝑁𝑒𝑡ℎ𝑒𝑟𝑙𝑎𝑛𝑑𝑠:

<!-- b001293 | prose | pages [18] -->
0, 𝑌𝑒𝑎𝑟< 2015 2015≤𝑌𝑒𝑎𝑟< 2022 (17) 𝐶𝑜𝑎𝑐ℎ_𝑁𝑒𝑡ℎ𝑒𝑟𝑙𝑎𝑛𝑑𝑠= { 1, 0, 𝑌𝑒𝑎𝑟≥2022 Using these variables, we can partition the data into pre-coaching and post-coaching seg- ments, which will serve as the basis for subsequent hypothesis testing.

<!-- b001294 | prose | pages [18, 19] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b001295 | furniture | pages [18] -->
2

<!-- b001296 | furniture | pages [18] -->
MATHmodels

<!-- b001297 | furniture | pages [18] -->
获取更多资讯

<!-- b001298 | furniture | pages [19] -->
Team # 2516178

<!-- b001299 | furniture | pages [19] -->
Page 19 of 27

<!-- b001301 | caption | pages [19] -->
Figure 12 Pre-coaching and post-coaching medal count comparison

<!-- b001302 | prose | pages [19] -->
Through these steps, we have processed the data on Chinese and Dutch women's hockey teams from 1988 to 2024 in the summerOly_athletes dataset. The processed data now includes the total medal scores and "Coaching Status" identifiers, providing the necessary data founda- tion for developing and analyzing a difference-in-differences model. This pre-processing step ensures data consistency and reliability, which is crucial for quantitatively evaluating the “great coach” effect.

<!-- b001303 | heading | pages [19] -->
7.2 DID Model Building

<!-- b001304 | prose | pages [19] -->
We have developed a linear regression model to investigate how the coaching change (whether Coach Alyson Annan is in charge) affects the medal scores of the Chinese and Dutch women's hockey teams. To achieve our research objective, we adopt the ordinary least squares (OLS) method, which effectively estimates the linear relationship between independent and dependent variables.

<!-- b001305 | prose | pages [19] -->
To quantify the impact of the coaching change on the medal count, we formulate the fol- lowing DID regression model:

<!-- b001306 | prose | pages [19] -->
(18) 𝑠𝑐𝑜𝑟𝑒𝑖= 𝛽0 + 𝛽1Coach𝑖+ 𝛽2Time𝑖+ 𝛽3Coach_Time𝑖+ 𝜖𝑖 Here, scorei represents the medal score of the Chinese or Dutch women's hockey team in year 𝑖. Coacℎi is a binary variable: 1 when Coach Alyson Annan is coaching, 0 otherwise, differentiating coaching and non-coaching periods. Timei is also binary, 1 after a predefined time node, 0 before, distinguishing post and pre-coaching change periods.

<!-- b001307 | prose | pages [19] -->
𝐶𝑜𝑎𝑐ℎ𝑖× 𝑇𝑖𝑚𝑒𝑖 , the interaction term of 𝐶𝑜𝑎𝑐ℎ𝑖 and 𝑇𝑖𝑚𝑒𝑖 , is the core of the DID model. Its coefficient 𝛽3 reflects the differential effect between coaching and non coaching periods before and after the coaching change, capturing the additional impact of Coach Alyson Annan's coaching on medal scores.

<!-- b001308 | prose | pages [19, 20] -->
𝛽0 is the regression model's intercept, representing the medal score unaffected by Coach Alyson Annan's coaching. 𝛽1 and 𝛽2 are regression coefficients for the impacts of coaching change and post-node time on medal scores respectively. ϵi is the error term for unobservable m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m factors affecting medal scores, helping to determine time-period impacts.

<!-- b001309 | furniture | pages [19] -->
m

<!-- b001310 | furniture | pages [19] -->
m

<!-- b001311 | furniture | pages [19] -->
m

<!-- b001312 | furniture | pages [19] -->
m

<!-- b001313 | furniture | pages [19] -->
m

<!-- b001314 | furniture | pages [19] -->
m

<!-- b001315 | furniture | pages [19] -->
m

<!-- b001316 | furniture | pages [19] -->
m

<!-- b001317 | furniture | pages [19] -->
m

<!-- b001318 | furniture | pages [19] -->
m

<!-- b001319 | furniture | pages [19] -->
m

<!-- b001320 | furniture | pages [19] -->
m

<!-- b001321 | furniture | pages [19] -->
m

<!-- b001322 | furniture | pages [19] -->
m

<!-- b001323 | furniture | pages [19] -->
m

<!-- b001324 | furniture | pages [19] -->
m

<!-- b001325 | furniture | pages [19] -->
m

<!-- b001326 | furniture | pages [19] -->
m

<!-- b001327 | furniture | pages [19] -->
m

<!-- b001328 | furniture | pages [19] -->
m

<!-- b001329 | furniture | pages [19] -->
m

<!-- b001330 | furniture | pages [19] -->
m

<!-- b001331 | furniture | pages [19] -->
m

<!-- b001332 | furniture | pages [19] -->
m

<!-- b001333 | furniture | pages [19] -->
m

<!-- b001334 | furniture | pages [19] -->
m

<!-- b001335 | furniture | pages [19] -->
m

<!-- b001336 | furniture | pages [19] -->
m

<!-- b001337 | furniture | pages [19] -->
m

<!-- b001338 | furniture | pages [19] -->
m

<!-- b001339 | furniture | pages [19] -->
m

<!-- b001340 | furniture | pages [19] -->
m

<!-- b001341 | furniture | pages [19] -->
m

<!-- b001342 | furniture | pages [19] -->
m

<!-- b001343 | furniture | pages [19] -->
m

<!-- b001344 | furniture | pages [19] -->
m

<!-- b001345 | furniture | pages [19] -->
m

<!-- b001346 | furniture | pages [19] -->
m

<!-- b001347 | furniture | pages [19] -->
m

<!-- b001348 | furniture | pages [19] -->
m

<!-- b001349 | furniture | pages [19] -->
m

<!-- b001350 | furniture | pages [19] -->
m

<!-- b001351 | furniture | pages [19] -->
m

<!-- b001352 | furniture | pages [19] -->
m

<!-- b001353 | furniture | pages [19] -->
m

<!-- b001354 | furniture | pages [19] -->
m

<!-- b001355 | furniture | pages [19] -->
m

<!-- b001356 | furniture | pages [19] -->
m

<!-- b001357 | furniture | pages [19] -->
m

<!-- b001358 | furniture | pages [19] -->
m

<!-- b001359 | furniture | pages [19] -->
m

<!-- b001360 | furniture | pages [19] -->
m

<!-- b001361 | furniture | pages [19] -->
m

<!-- b001362 | furniture | pages [19] -->
m

<!-- b001363 | furniture | pages [19] -->
m

<!-- b001364 | furniture | pages [19] -->
m

<!-- b001365 | furniture | pages [19] -->
m

<!-- b001366 | furniture | pages [19] -->
m

<!-- b001367 | furniture | pages [19] -->
m

<!-- b001368 | furniture | pages [19] -->
m

<!-- b001369 | furniture | pages [19] -->
m

<!-- b001370 | furniture | pages [19] -->
m

<!-- b001371 | furniture | pages [19] -->
m

<!-- b001372 | furniture | pages [19] -->
m

<!-- b001373 | furniture | pages [19] -->
m

<!-- b001374 | furniture | pages [19] -->
m

<!-- b001375 | furniture | pages [19] -->
m

<!-- b001376 | furniture | pages [19] -->
m

<!-- b001377 | furniture | pages [19] -->
m

<!-- b001378 | furniture | pages [19] -->
m

<!-- b001379 | furniture | pages [19] -->
m

<!-- b001380 | furniture | pages [19] -->
m

<!-- b001381 | furniture | pages [19] -->
m

<!-- b001382 | furniture | pages [19] -->
m

<!-- b001383 | furniture | pages [19] -->
m

<!-- b001384 | furniture | pages [19] -->
m

<!-- b001385 | furniture | pages [19] -->
m

<!-- b001386 | furniture | pages [19] -->
m

<!-- b001387 | furniture | pages [19] -->
m

<!-- b001388 | furniture | pages [19] -->
m

<!-- b001389 | furniture | pages [19] -->
m

<!-- b001390 | furniture | pages [19] -->
m

<!-- b001391 | furniture | pages [19] -->
m

<!-- b001392 | furniture | pages [19] -->
m

<!-- b001393 | furniture | pages [19] -->
m

<!-- b001394 | furniture | pages [19] -->
m

<!-- b001395 | furniture | pages [19] -->
m

<!-- b001396 | furniture | pages [19] -->
m

<!-- b001397 | furniture | pages [19] -->
m

<!-- b001398 | furniture | pages [19] -->
m

<!-- b001399 | furniture | pages [19] -->
m

<!-- b001400 | furniture | pages [19] -->
m

<!-- b001401 | furniture | pages [19] -->
m

<!-- b001402 | furniture | pages [19] -->
m

<!-- b001403 | furniture | pages [19] -->
m

<!-- b001404 | furniture | pages [19] -->
m

<!-- b001405 | furniture | pages [19] -->
m

<!-- b001406 | furniture | pages [19] -->
m

<!-- b001407 | furniture | pages [19] -->
m

<!-- b001408 | furniture | pages [19] -->
m

<!-- b001409 | furniture | pages [19] -->
m

<!-- b001410 | furniture | pages [19] -->
m

<!-- b001411 | furniture | pages [19] -->
m

<!-- b001412 | furniture | pages [19] -->
m

<!-- b001413 | furniture | pages [19] -->
m

<!-- b001414 | furniture | pages [19] -->
m

<!-- b001415 | furniture | pages [19] -->
m

<!-- b001416 | furniture | pages [19] -->
m

<!-- b001417 | furniture | pages [19] -->
m

<!-- b001418 | furniture | pages [19] -->
m

<!-- b001419 | furniture | pages [19] -->
m

<!-- b001420 | furniture | pages [19] -->
m

<!-- b001421 | furniture | pages [19] -->
m

<!-- b001422 | furniture | pages [19] -->
m

<!-- b001423 | furniture | pages [19] -->
m

<!-- b001424 | furniture | pages [19] -->
m

<!-- b001425 | furniture | pages [19] -->
m

<!-- b001426 | furniture | pages [19] -->
m

<!-- b001427 | furniture | pages [19] -->
m

<!-- b001428 | furniture | pages [19] -->
m

<!-- b001429 | furniture | pages [19] -->
m

<!-- b001430 | furniture | pages [19] -->
m

<!-- b001431 | furniture | pages [19] -->
m

<!-- b001432 | furniture | pages [19] -->
m

<!-- b001433 | furniture | pages [19] -->
m

<!-- b001434 | furniture | pages [19] -->
m

<!-- b001435 | furniture | pages [19] -->
m

<!-- b001436 | furniture | pages [19] -->
m

<!-- b001437 | furniture | pages [19] -->
m

<!-- b001438 | furniture | pages [19] -->
m

<!-- b001439 | furniture | pages [19] -->
m

<!-- b001440 | furniture | pages [19] -->
m

<!-- b001441 | furniture | pages [19] -->
m

<!-- b001442 | furniture | pages [19] -->
m

<!-- b001443 | furniture | pages [19] -->
m

<!-- b001444 | furniture | pages [19] -->
m

<!-- b001445 | furniture | pages [19] -->
m

<!-- b001446 | furniture | pages [19] -->
m

<!-- b001447 | furniture | pages [19] -->
m

<!-- b001448 | furniture | pages [19] -->
m

<!-- b001449 | furniture | pages [19] -->
m

<!-- b001450 | furniture | pages [19] -->
m

<!-- b001451 | furniture | pages [19] -->
m

<!-- b001452 | furniture | pages [19] -->
m

<!-- b001453 | furniture | pages [19] -->
m

<!-- b001454 | furniture | pages [19] -->
m

<!-- b001455 | furniture | pages [19] -->
m

<!-- b001456 | furniture | pages [19] -->
m

<!-- b001457 | furniture | pages [19] -->
m

<!-- b001458 | furniture | pages [19] -->
m

<!-- b001459 | furniture | pages [19] -->
m

<!-- b001460 | furniture | pages [19] -->
m

<!-- b001461 | furniture | pages [19] -->
m

<!-- b001462 | furniture | pages [19] -->
m

<!-- b001463 | furniture | pages [19] -->
m

<!-- b001464 | furniture | pages [19] -->
m

<!-- b001465 | furniture | pages [19] -->
m

<!-- b001466 | furniture | pages [19] -->
m

<!-- b001467 | furniture | pages [19] -->
m

<!-- b001468 | furniture | pages [19] -->
m

<!-- b001469 | furniture | pages [19] -->
m

<!-- b001470 | furniture | pages [19] -->
m

<!-- b001471 | furniture | pages [19] -->
m

<!-- b001472 | furniture | pages [19] -->
m

<!-- b001473 | furniture | pages [19] -->
m

<!-- b001474 | furniture | pages [19] -->
m

<!-- b001475 | furniture | pages [19] -->
m

<!-- b001476 | furniture | pages [19] -->
m

<!-- b001477 | furniture | pages [19] -->
m

<!-- b001478 | furniture | pages [19] -->
m

<!-- b001479 | furniture | pages [19] -->
m

<!-- b001480 | furniture | pages [19] -->
m

<!-- b001481 | furniture | pages [19] -->
m

<!-- b001482 | furniture | pages [19] -->
m

<!-- b001483 | furniture | pages [19] -->
m

<!-- b001484 | furniture | pages [19] -->
m

<!-- b001485 | furniture | pages [19] -->
m

<!-- b001486 | furniture | pages [19] -->
m

<!-- b001487 | furniture | pages [19] -->
m

<!-- b001488 | furniture | pages [19] -->
m

<!-- b001489 | furniture | pages [19] -->
m

<!-- b001490 | furniture | pages [19] -->
m

<!-- b001491 | furniture | pages [19] -->
m

<!-- b001492 | furniture | pages [19] -->
m

<!-- b001493 | furniture | pages [19] -->
m

<!-- b001494 | furniture | pages [19] -->
m

<!-- b001495 | furniture | pages [19] -->
m

<!-- b001496 | furniture | pages [19] -->
m

<!-- b001497 | furniture | pages [19] -->
m

<!-- b001498 | furniture | pages [19] -->
m

<!-- b001499 | furniture | pages [19] -->
m

<!-- b001500 | furniture | pages [19] -->
m

<!-- b001501 | furniture | pages [19] -->
m

<!-- b001502 | furniture | pages [19] -->
m

<!-- b001503 | furniture | pages [19] -->
m

<!-- b001504 | furniture | pages [19] -->
m

<!-- b001505 | furniture | pages [19] -->
m

<!-- b001506 | furniture | pages [19] -->
m

<!-- b001507 | furniture | pages [19] -->
m

<!-- b001508 | furniture | pages [19] -->
m

<!-- b001509 | furniture | pages [19] -->
m

<!-- b001510 | furniture | pages [19] -->
m

<!-- b001511 | furniture | pages [19] -->
m

<!-- b001512 | furniture | pages [19] -->
m

<!-- b001513 | furniture | pages [19] -->
m

<!-- b001514 | furniture | pages [19] -->
m

<!-- b001515 | furniture | pages [19] -->
m

<!-- b001516 | furniture | pages [19] -->
m

<!-- b001517 | furniture | pages [19] -->
m

<!-- b001518 | furniture | pages [19] -->
m

<!-- b001519 | furniture | pages [19] -->
m

<!-- b001520 | furniture | pages [19] -->
m

<!-- b001521 | furniture | pages [19] -->
m

<!-- b001522 | furniture | pages [19] -->
m

<!-- b001523 | furniture | pages [19] -->
m

<!-- b001524 | furniture | pages [19] -->
m

<!-- b001525 | furniture | pages [19] -->
m

<!-- b001526 | furniture | pages [19] -->
m

<!-- b001527 | furniture | pages [19] -->
m

<!-- b001528 | furniture | pages [19] -->
m

<!-- b001529 | furniture | pages [19] -->
m

<!-- b001530 | furniture | pages [19] -->
m

<!-- b001531 | furniture | pages [19] -->
m

<!-- b001532 | furniture | pages [19] -->
m

<!-- b001533 | furniture | pages [19] -->
m

<!-- b001534 | furniture | pages [19] -->
m

<!-- b001535 | furniture | pages [19] -->
m

<!-- b001536 | furniture | pages [19] -->
m

<!-- b001537 | furniture | pages [19] -->
m

<!-- b001538 | furniture | pages [19] -->
m

<!-- b001539 | furniture | pages [19] -->
m

<!-- b001540 | furniture | pages [19] -->
m

<!-- b001541 | furniture | pages [19] -->
m

<!-- b001542 | furniture | pages [19] -->
m

<!-- b001543 | furniture | pages [19] -->
m

<!-- b001544 | furniture | pages [19] -->
m

<!-- b001545 | furniture | pages [19] -->
m

<!-- b001546 | furniture | pages [19] -->
m

<!-- b001547 | furniture | pages [19] -->
m

<!-- b001548 | furniture | pages [19] -->
m

<!-- b001549 | furniture | pages [19] -->
m

<!-- b001550 | furniture | pages [19] -->
m

<!-- b001551 | furniture | pages [19] -->
m

<!-- b001552 | furniture | pages [19] -->
m

<!-- b001553 | furniture | pages [19] -->
m

<!-- b001554 | furniture | pages [19] -->
m

<!-- b001555 | furniture | pages [19] -->
m

<!-- b001556 | furniture | pages [19] -->
m

<!-- b001557 | furniture | pages [19] -->
m

<!-- b001558 | furniture | pages [19] -->
m

<!-- b001559 | furniture | pages [19] -->
m

<!-- b001560 | furniture | pages [19] -->
m

<!-- b001561 | furniture | pages [19] -->
m

<!-- b001562 | furniture | pages [19] -->
m

<!-- b001563 | furniture | pages [19] -->
m

<!-- b001564 | furniture | pages [19] -->
m

<!-- b001565 | furniture | pages [19] -->
m

<!-- b001566 | furniture | pages [19] -->
m

<!-- b001567 | furniture | pages [19] -->
m

<!-- b001568 | furniture | pages [19] -->
m

<!-- b001569 | furniture | pages [19] -->
m

<!-- b001570 | furniture | pages [19] -->
m

<!-- b001571 | furniture | pages [19] -->
m

<!-- b001572 | furniture | pages [19] -->
m

<!-- b001573 | furniture | pages [19] -->
m

<!-- b001574 | furniture | pages [19] -->
m

<!-- b001575 | furniture | pages [19] -->
m

<!-- b001576 | furniture | pages [19] -->
m

<!-- b001577 | furniture | pages [19] -->
m

<!-- b001578 | furniture | pages [19] -->
m

<!-- b001579 | furniture | pages [19] -->
m

<!-- b001580 | furniture | pages [19] -->
m

<!-- b001581 | furniture | pages [19] -->
m

<!-- b001582 | furniture | pages [19] -->
m

<!-- b001583 | furniture | pages [19] -->
m

<!-- b001584 | furniture | pages [19] -->
m

<!-- b001585 | furniture | pages [19] -->
m

<!-- b001586 | furniture | pages [19] -->
m

<!-- b001587 | furniture | pages [19] -->
m

<!-- b001588 | furniture | pages [19] -->
m

<!-- b001589 | furniture | pages [19] -->
m

<!-- b001590 | furniture | pages [19] -->
m

<!-- b001591 | furniture | pages [19] -->
m

<!-- b001592 | furniture | pages [19] -->
m

<!-- b001593 | furniture | pages [19] -->
m

<!-- b001594 | furniture | pages [19] -->
m

<!-- b001595 | furniture | pages [19] -->
m

<!-- b001596 | furniture | pages [19] -->
m

<!-- b001597 | furniture | pages [19] -->
m

<!-- b001598 | furniture | pages [19] -->
m

<!-- b001599 | furniture | pages [19] -->
m

<!-- b001600 | furniture | pages [19] -->
m

<!-- b001601 | furniture | pages [19] -->
m

<!-- b001602 | furniture | pages [19] -->
m

<!-- b001603 | furniture | pages [19] -->
m

<!-- b001604 | furniture | pages [19] -->
m

<!-- b001605 | furniture | pages [19] -->
m

<!-- b001606 | furniture | pages [19] -->
m

<!-- b001607 | furniture | pages [19] -->
m

<!-- b001608 | furniture | pages [19] -->
m

<!-- b001609 | furniture | pages [19] -->
m

<!-- b001610 | furniture | pages [19] -->
m

<!-- b001611 | furniture | pages [19] -->
m

<!-- b001612 | furniture | pages [19] -->
m

<!-- b001613 | furniture | pages [19] -->
m

<!-- b001614 | furniture | pages [19] -->
m

<!-- b001615 | furniture | pages [19] -->
m

<!-- b001616 | furniture | pages [19] -->
m

<!-- b001617 | furniture | pages [19] -->
m

<!-- b001618 | furniture | pages [19] -->
m

<!-- b001619 | furniture | pages [19] -->
m

<!-- b001620 | furniture | pages [19] -->
m

<!-- b001621 | furniture | pages [19] -->
m

<!-- b001622 | furniture | pages [19] -->
m

<!-- b001623 | furniture | pages [19] -->
m

<!-- b001624 | furniture | pages [19] -->
m

<!-- b001625 | furniture | pages [19] -->
m

<!-- b001626 | furniture | pages [19] -->
m

<!-- b001627 | furniture | pages [19] -->
m

<!-- b001628 | furniture | pages [19] -->
m

<!-- b001629 | furniture | pages [19] -->
m

<!-- b001630 | furniture | pages [19] -->
m

<!-- b001631 | furniture | pages [19] -->
m

<!-- b001632 | furniture | pages [19] -->
m

<!-- b001633 | furniture | pages [20] -->
Team # 2516178

<!-- b001634 | furniture | pages [20] -->
Page 20 of 27

<!-- b001636 | prose | pages [20] -->
The regression coefficient 𝛽3 is crucial for evaluating the great-coach effect. Its signifi- cance is determined by the t statistic and p value. If 𝑝< 0.05, the null hypothesis is rejected, indicating a significant impact on medal numbers. If 𝑝≥0.05, the null cannot be rejected, meaning no significant impact.

<!-- b001637 | prose | pages [20] -->
Based on regression results, we test the impacts of coaching, time, and their interaction on medal scores. A significant positive coefficient implies a positive correlation, otherwise a negative one. Using regression and DID, we quantify the "great coach" (Alyson Annan) effect on medal scores of Chinese and Dutch women's hockey. High statistical significance of 𝛽3 supports the “great coach” effect.

<!-- b001638 | heading | pages [20] -->
7.3 Solution of the Model

<!-- b001639 | prose | pages [20] -->
Based on the results of the Ordinary Least Squares (OLS) regression analysis, the model successfully quantified the impact of the "Great Coach" (Coach Alyson Annan) effect on the medal scores of the Chinese and Dutch women's hockey programs. Through regression model analysis, we evaluated the relationship between Coach Alyson Annan's coaching and the num- ber of medals, obtaining the following regression coefficients and statistics.

<!-- b001640 | caption | pages [20] -->
Table 8 Results of Linear Regression Analysis

<!-- b001641 | prose | pages [20] -->
𝑅2 Team 𝛽3 𝑡 𝑝 𝛽0 9.556 2.45 0.03 0.92 China 5.33 Dutch 4.875 2.131 0.05 0.83 28.37 The regression analysis results reveal that Coach Alyson Annan's coaching significantly influences the medal scores of both the Chinese and Dutch women's hockey teams. The change in coaching by Coach Alyson Annan has significantly boosted the medal scores. Specifically, the Chinese women's hockey team's medal score has increased by an average of 9.556 points, and the Dutch women's hockey team's has increased by an average of 4.875 points.

<!-- b001642 | prose | pages [20] -->
This conclusion suggests that the “great coach” effect plays a crucial role in the perfor- mance of the Chinese and Dutch women's hockey teams. The regression coefficients and their significance strongly support investment in coaching, especially in terms of coaching-resource allocation and strategic decision-making. Based on this analysis, when other countries recruit top-level coaches, they can predict the return on coaching investment based on this effect and make corresponding strategic arrangements.

<!-- b001643 | heading | pages [20] -->
7.3.1 Investment Analysis of Excellent Coaches

<!-- b001644 | prose | pages [20] -->
m m m m m m m m m m m m m m m m m m m m m m By analyzing the data from 2000 to 2024, we screened out the data of women's hockey m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m teams from different countries and counted the scores of each year according to country and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m year. To draw more representative conclusions, we calculated the average annual score for each m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m country and ranked them accordingly. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We set two-fold screening criteria. First, a country should have shown unsatisfactory per- m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001645 | prose | pages [20] -->
formance in the women's hockey event in the last two Olympic Games. Second, it should have demonstrated excellent overall performance from 2000 to 2024, measured by the average an- nual score. Based on these criteria, we selected the top three countries with the highest average annual scores to determine the priority targets for coach investment.

<!-- b001646 | prose | pages [20] -->
After data processing, we found that the countries meeting the screening criteria were

<!-- b001647 | prose | pages [20, 21] -->
关注数学模型 Australia, Great Britain, and Germany. These countries had an outstanding overall perfor- mance in the women's hockey event from 2000 to 2024, yet their performance in the last two Olympics was poor. This indicates that they possess a solid foundation and potential in this sport, perhaps only lacking a "great coach" to unlock their potential.

<!-- b001648 | furniture | pages [20] -->
2

<!-- b001649 | furniture | pages [20] -->
MATHmodels

<!-- b001650 | furniture | pages [20] -->
获取更多资讯

<!-- b001651 | furniture | pages [21] -->
Team # 2516178

<!-- b001652 | furniture | pages [21] -->
Page 21 of 27

<!-- b001654 | prose | pages [21] -->
Therefore, for the coach-investment strategies in these countries, we recommend focusing on the women's hockey event, with the aim of significantly enhancing medal-winning perfor- 微信公众号：数学模型 mance based on the existing good foundation.

<!-- b001655 | heading | pages [21] -->
7.3.2 Impacts of Excellent Coach Investment

<!-- b001656 | prose | pages [21] -->
To quantify the return on coach investment, we'll, based on the previous analysis frame- work, predict the returns of coach investment in different countries, providing a reference for future coach-resource allocation. We'll analyze the medal performance of women's hockey in various countries to predict the potential impact of great-coach investment on medal-count growth.

<!-- b001657 | heading | pages [21] -->
1. Definition of Medal Benchmark Score

<!-- b001658 | prose | pages [21] -->
The benchmark score is the average score calculated above, defined as ccountry.

<!-- b001659 | prose | pages [21] -->
微信号：MATHmodels

<!-- b001660 | heading | pages [21] -->
2. Adjustment Coefficient

<!-- b001661 | prose | pages [21] -->
During Coach Alyson Annan's non-coaching period, assume the average medal score of a reference women's hockey team is c𝑐𝑜𝑢𝑛𝑡𝑟𝑦 . We calculate the adjustment coefficient 𝑎𝑑𝑗𝑢𝑠𝑡𝑚𝑒𝑛𝑡 for each investing country by computing the ratio of its average medal score c𝑐𝑜𝑢𝑛𝑡𝑟𝑦 to that of the reference team. The formula is:

<!-- b001662 | prose | pages [21] -->
𝑎𝑑𝑗𝑢𝑠𝑡𝑚𝑒𝑛𝑡= c𝑐𝑜𝑢𝑛𝑡𝑟𝑦 (19) 𝑐𝑟𝑒𝑓𝑒𝑟𝑒𝑛𝑐𝑒 This adjustment coefficient reflects each country's medal performance relative to the ref- erence team under the same conditions. The larger the coefficient, the more competitive the country is under similar circumstances.

<!-- b001663 | heading | pages [21] -->
3. Prediction of Medal Score Increase

<!-- b001664 | prose | pages [21] -->
We calculate the predicted medal-increase value for each country after coach investment by multiplying the adjustment coefficient by the effect value 𝛽3 of Coach Alyson Annan. The formula is:

<!-- b001665 | prose | pages [21] -->
(20) 𝑃𝐼𝑐𝑜𝑢𝑛𝑡𝑖 = 𝑎𝑑𝑗𝑢𝑠𝑡𝑚𝑒𝑛𝑡𝑖× 𝛽3 Here, 𝑃𝐼𝑐𝑜𝑢𝑛𝑡𝑖 represents the predicted medal-increase value for the 𝑖th country after investing in an excellent coach.

<!-- b001666 | heading | pages [21] -->
4. Prediction of Final Medal Score

<!-- b001667 | prose | pages [21] -->
Finally, we obtain the predicted medal score by adding the predicted medal-score increase value to the benchmark medal score of each country. The formula is:

<!-- b001668 | prose | pages [21] -->
𝑃𝑐𝑜𝑢𝑛𝑡𝑖= 𝑐𝑐𝑜𝑢𝑛𝑡𝑟𝑦+ 𝑃𝐼𝑐𝑜𝑢𝑛𝑡𝑖 (21) This value represents the medal score a country may reach after coach investment, assum- ing the effect of Coach Alyson Annan. Based on these calculations, we get the prediction results.

<!-- b001669 | prose | pages [21] -->
The final prediction results are as follows:

<!-- b001670 | caption | pages [21] -->
Table 9 Prediction of medal score of women's hockey with a “great coach”

<!-- b001671 | prose | pages [21] -->
Great Australia Great Britain Germany Year Australia Germany Britain Predicted Predicted Predicted

<!-- b001672 | prose | pages [21, 22] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1984 0 0.0 0.0 11.8 8.3 7.7 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

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

<!-- b001758 | furniture | pages [21] -->
m

<!-- b001759 | furniture | pages [21] -->
m

<!-- b001760 | furniture | pages [21] -->
m

<!-- b001761 | furniture | pages [21] -->
m

<!-- b001762 | furniture | pages [21] -->
m

<!-- b001763 | furniture | pages [21] -->
m

<!-- b001764 | furniture | pages [21] -->
m

<!-- b001765 | furniture | pages [21] -->
m

<!-- b001766 | furniture | pages [21] -->
m

<!-- b001767 | furniture | pages [21] -->
m

<!-- b001768 | furniture | pages [21] -->
m

<!-- b001769 | furniture | pages [21] -->
m

<!-- b001770 | furniture | pages [21] -->
m

<!-- b001771 | furniture | pages [21] -->
m

<!-- b001772 | furniture | pages [21] -->
m

<!-- b001773 | furniture | pages [21] -->
m

<!-- b001774 | furniture | pages [21] -->
m

<!-- b001775 | furniture | pages [21] -->
m

<!-- b001776 | furniture | pages [21] -->
m

<!-- b001777 | furniture | pages [21] -->
m

<!-- b001778 | furniture | pages [21] -->
m

<!-- b001779 | furniture | pages [21] -->
m

<!-- b001780 | furniture | pages [21] -->
m

<!-- b001781 | furniture | pages [21] -->
m

<!-- b001782 | furniture | pages [21] -->
m

<!-- b001783 | furniture | pages [21] -->
m

<!-- b001784 | furniture | pages [21] -->
m

<!-- b001785 | furniture | pages [21] -->
m

<!-- b001786 | furniture | pages [21] -->
m

<!-- b001787 | furniture | pages [21] -->
m

<!-- b001788 | furniture | pages [21] -->
m

<!-- b001789 | furniture | pages [21] -->
m

<!-- b001790 | furniture | pages [21] -->
m

<!-- b001791 | furniture | pages [21] -->
m

<!-- b001792 | furniture | pages [21] -->
m

<!-- b001793 | furniture | pages [21] -->
m

<!-- b001794 | furniture | pages [21] -->
m

<!-- b001795 | furniture | pages [21] -->
m

<!-- b001796 | furniture | pages [21] -->
m

<!-- b001797 | furniture | pages [21] -->
m

<!-- b001798 | furniture | pages [21] -->
m

<!-- b001799 | furniture | pages [21] -->
m

<!-- b001800 | furniture | pages [21] -->
m

<!-- b001801 | furniture | pages [21] -->
m

<!-- b001802 | furniture | pages [21] -->
m

<!-- b001803 | furniture | pages [21] -->
m

<!-- b001804 | furniture | pages [21] -->
m

<!-- b001805 | furniture | pages [21] -->
m

<!-- b001806 | furniture | pages [21] -->
m

<!-- b001807 | furniture | pages [21] -->
m

<!-- b001808 | furniture | pages [21] -->
m

<!-- b001809 | furniture | pages [21] -->
m

<!-- b001810 | furniture | pages [21] -->
m

<!-- b001811 | furniture | pages [21] -->
m

<!-- b001812 | furniture | pages [21] -->
m

<!-- b001813 | furniture | pages [21] -->
m

<!-- b001814 | furniture | pages [21] -->
m

<!-- b001815 | furniture | pages [21] -->
m

<!-- b001816 | furniture | pages [21] -->
m

<!-- b001817 | furniture | pages [21] -->
m

<!-- b001818 | furniture | pages [21] -->
m

<!-- b001819 | furniture | pages [21] -->
m

<!-- b001820 | furniture | pages [21] -->
m

<!-- b001821 | furniture | pages [21] -->
m

<!-- b001822 | furniture | pages [21] -->
m

<!-- b001823 | furniture | pages [21] -->
m

<!-- b001824 | furniture | pages [21] -->
m

<!-- b001825 | furniture | pages [21] -->
m

<!-- b001826 | furniture | pages [21] -->
m

<!-- b001827 | furniture | pages [21] -->
m

<!-- b001828 | furniture | pages [21] -->
m

<!-- b001829 | furniture | pages [21] -->
m

<!-- b001830 | furniture | pages [21] -->
m

<!-- b001831 | furniture | pages [21] -->
m

<!-- b001832 | furniture | pages [21] -->
m

<!-- b001833 | furniture | pages [21] -->
m

<!-- b001834 | furniture | pages [21] -->
m

<!-- b001835 | furniture | pages [21] -->
m

<!-- b001836 | furniture | pages [21] -->
m

<!-- b001837 | furniture | pages [21] -->
m

<!-- b001838 | furniture | pages [21] -->
m

<!-- b001839 | furniture | pages [21] -->
m

<!-- b001840 | furniture | pages [21] -->
m

<!-- b001841 | furniture | pages [21] -->
m

<!-- b001842 | furniture | pages [21] -->
m

<!-- b001843 | furniture | pages [21] -->
m

<!-- b001844 | furniture | pages [21] -->
m

<!-- b001845 | furniture | pages [21] -->
m

<!-- b001846 | furniture | pages [21] -->
m

<!-- b001847 | furniture | pages [21] -->
m

<!-- b001848 | furniture | pages [21] -->
m

<!-- b001849 | furniture | pages [21] -->
m

<!-- b001850 | furniture | pages [21] -->
m

<!-- b001851 | furniture | pages [21] -->
m

<!-- b001852 | furniture | pages [21] -->
m

<!-- b001853 | furniture | pages [21] -->
m

<!-- b001854 | furniture | pages [21] -->
m

<!-- b001855 | furniture | pages [21] -->
m

<!-- b001856 | furniture | pages [21] -->
m

<!-- b001857 | furniture | pages [21] -->
m

<!-- b001858 | furniture | pages [21] -->
m

<!-- b001859 | furniture | pages [21] -->
m

<!-- b001860 | furniture | pages [21] -->
m

<!-- b001861 | furniture | pages [21] -->
m

<!-- b001862 | furniture | pages [21] -->
m

<!-- b001863 | furniture | pages [21] -->
m

<!-- b001864 | furniture | pages [21] -->
m

<!-- b001865 | furniture | pages [21] -->
m

<!-- b001866 | furniture | pages [21] -->
m

<!-- b001867 | furniture | pages [21] -->
m

<!-- b001868 | furniture | pages [21] -->
m

<!-- b001869 | furniture | pages [21] -->
m

<!-- b001870 | furniture | pages [21] -->
m

<!-- b001871 | furniture | pages [21] -->
m

<!-- b001872 | furniture | pages [21] -->
m

<!-- b001873 | furniture | pages [21] -->
m

<!-- b001874 | furniture | pages [21] -->
m

<!-- b001875 | furniture | pages [21] -->
m

<!-- b001876 | furniture | pages [21] -->
m

<!-- b001877 | furniture | pages [21] -->
m

<!-- b001878 | furniture | pages [21] -->
m

<!-- b001879 | furniture | pages [21] -->
m

<!-- b001880 | furniture | pages [21] -->
m

<!-- b001881 | furniture | pages [21] -->
m

<!-- b001882 | furniture | pages [21] -->
m

<!-- b001883 | furniture | pages [21] -->
m

<!-- b001884 | furniture | pages [21] -->
m

<!-- b001885 | furniture | pages [21] -->
m

<!-- b001886 | furniture | pages [21] -->
m

<!-- b001887 | furniture | pages [21] -->
m

<!-- b001888 | furniture | pages [21] -->
m

<!-- b001889 | furniture | pages [21] -->
m

<!-- b001890 | furniture | pages [21] -->
m

<!-- b001891 | furniture | pages [21] -->
m

<!-- b001892 | furniture | pages [21] -->
m

<!-- b001893 | furniture | pages [21] -->
m

<!-- b001894 | furniture | pages [21] -->
m

<!-- b001895 | furniture | pages [21] -->
m

<!-- b001896 | furniture | pages [21] -->
m

<!-- b001897 | furniture | pages [21] -->
m

<!-- b001898 | furniture | pages [21] -->
m

<!-- b001899 | furniture | pages [21] -->
m

<!-- b001900 | furniture | pages [21] -->
m

<!-- b001901 | furniture | pages [21] -->
m

<!-- b001902 | furniture | pages [21] -->
m

<!-- b001903 | furniture | pages [21] -->
m

<!-- b001904 | furniture | pages [21] -->
m

<!-- b001905 | furniture | pages [21] -->
m

<!-- b001906 | furniture | pages [21] -->
m

<!-- b001907 | furniture | pages [21] -->
m

<!-- b001908 | furniture | pages [21] -->
m

<!-- b001909 | furniture | pages [21] -->
m

<!-- b001910 | furniture | pages [21] -->
m

<!-- b001911 | furniture | pages [21] -->
m

<!-- b001912 | furniture | pages [21] -->
m

<!-- b001913 | furniture | pages [21] -->
m

<!-- b001914 | furniture | pages [21] -->
m

<!-- b001915 | furniture | pages [21] -->
m

<!-- b001916 | furniture | pages [21] -->
m

<!-- b001917 | furniture | pages [21] -->
m

<!-- b001918 | furniture | pages [21] -->
m

<!-- b001919 | furniture | pages [21] -->
m

<!-- b001920 | furniture | pages [21] -->
m

<!-- b001921 | furniture | pages [21] -->
m

<!-- b001922 | furniture | pages [21] -->
m

<!-- b001923 | furniture | pages [21] -->
m

<!-- b001924 | furniture | pages [21] -->
m

<!-- b001925 | furniture | pages [21] -->
m

<!-- b001926 | furniture | pages [21] -->
m

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

<!-- b001997 | furniture | pages [22] -->
m

<!-- b001998 | furniture | pages [22] -->
m

<!-- b001999 | furniture | pages [22] -->
m

<!-- b002000 | furniture | pages [22] -->
m

<!-- b002001 | furniture | pages [22] -->
m

<!-- b002002 | furniture | pages [22] -->
m

<!-- b002003 | furniture | pages [22] -->
m

<!-- b002004 | furniture | pages [22] -->
m

<!-- b002005 | furniture | pages [22] -->
m

<!-- b002006 | furniture | pages [22] -->
m

<!-- b002007 | furniture | pages [22] -->
m

<!-- b002008 | furniture | pages [22] -->
m

<!-- b002009 | furniture | pages [22] -->
m

<!-- b002010 | furniture | pages [22] -->
m

<!-- b002011 | furniture | pages [22] -->
m

<!-- b002012 | furniture | pages [22] -->
m

<!-- b002013 | furniture | pages [22] -->
m

<!-- b002014 | furniture | pages [22] -->
m

<!-- b002015 | furniture | pages [22] -->
m

<!-- b002016 | furniture | pages [22] -->
m

<!-- b002017 | furniture | pages [22] -->
m

<!-- b002018 | furniture | pages [22] -->
m

<!-- b002019 | furniture | pages [22] -->
m

<!-- b002020 | furniture | pages [22] -->
m

<!-- b002021 | furniture | pages [22] -->
m

<!-- b002022 | furniture | pages [22] -->
m

<!-- b002023 | furniture | pages [22] -->
m

<!-- b002024 | furniture | pages [22] -->
m

<!-- b002025 | furniture | pages [22] -->
m

<!-- b002026 | furniture | pages [22] -->
m

<!-- b002027 | furniture | pages [22] -->
m

<!-- b002028 | furniture | pages [22] -->
m

<!-- b002029 | furniture | pages [22] -->
m

<!-- b002030 | furniture | pages [22] -->
m

<!-- b002031 | furniture | pages [22] -->
m

<!-- b002032 | furniture | pages [22] -->
m

<!-- b002033 | furniture | pages [22] -->
m

<!-- b002034 | furniture | pages [22] -->
m

<!-- b002035 | furniture | pages [22] -->
m

<!-- b002036 | furniture | pages [22] -->
m

<!-- b002037 | furniture | pages [22] -->
m

<!-- b002038 | furniture | pages [22] -->
m

<!-- b002039 | furniture | pages [22] -->
m

<!-- b002040 | furniture | pages [22] -->
m

<!-- b002041 | furniture | pages [22] -->
m

<!-- b002042 | furniture | pages [22] -->
m

<!-- b002043 | furniture | pages [22] -->
m

<!-- b002044 | furniture | pages [22] -->
m

<!-- b002045 | furniture | pages [22] -->
m

<!-- b002046 | furniture | pages [22] -->
m

<!-- b002047 | furniture | pages [22] -->
m

<!-- b002048 | furniture | pages [22] -->
m

<!-- b002049 | furniture | pages [22] -->
m

<!-- b002050 | furniture | pages [22] -->
m

<!-- b002051 | furniture | pages [22] -->
m

<!-- b002052 | furniture | pages [22] -->
m

<!-- b002053 | furniture | pages [22] -->
m

<!-- b002054 | furniture | pages [22] -->
m

<!-- b002055 | furniture | pages [22] -->
m

<!-- b002056 | furniture | pages [22] -->
m

<!-- b002057 | furniture | pages [22] -->
m

<!-- b002058 | furniture | pages [22] -->
m

<!-- b002059 | furniture | pages [22] -->
m

<!-- b002060 | furniture | pages [22] -->
m

<!-- b002061 | furniture | pages [22] -->
m

<!-- b002062 | furniture | pages [22] -->
m

<!-- b002063 | furniture | pages [22] -->
m

<!-- b002064 | furniture | pages [22] -->
m

<!-- b002065 | furniture | pages [22] -->
m

<!-- b002066 | furniture | pages [22] -->
m

<!-- b002067 | furniture | pages [22] -->
m

<!-- b002068 | furniture | pages [22] -->
m

<!-- b002069 | furniture | pages [22] -->
m

<!-- b002070 | furniture | pages [22] -->
m

<!-- b002071 | furniture | pages [22] -->
m

<!-- b002072 | furniture | pages [22] -->
m

<!-- b002073 | furniture | pages [22] -->
m

<!-- b002074 | furniture | pages [22] -->
m

<!-- b002075 | furniture | pages [22] -->
m

<!-- b002076 | furniture | pages [22] -->
m

<!-- b002077 | furniture | pages [22] -->
m

<!-- b002078 | furniture | pages [22] -->
m

<!-- b002079 | furniture | pages [22] -->
m

<!-- b002080 | furniture | pages [22] -->
m

<!-- b002081 | furniture | pages [22] -->
m

<!-- b002082 | furniture | pages [22] -->
m

<!-- b002083 | furniture | pages [22] -->
m

<!-- b002084 | furniture | pages [22] -->
m

<!-- b002085 | furniture | pages [22] -->
m

<!-- b002086 | furniture | pages [22] -->
m

<!-- b002087 | furniture | pages [22] -->
m

<!-- b002088 | furniture | pages [22] -->
m

<!-- b002089 | furniture | pages [22] -->
m

<!-- b002090 | furniture | pages [22] -->
m

<!-- b002091 | furniture | pages [22] -->
m

<!-- b002092 | furniture | pages [22] -->
m

<!-- b002093 | furniture | pages [22] -->
m

<!-- b002094 | furniture | pages [22] -->
m

<!-- b002095 | furniture | pages [22] -->
m

<!-- b002096 | furniture | pages [22] -->
m

<!-- b002097 | furniture | pages [22] -->
m

<!-- b002098 | furniture | pages [22] -->
m

<!-- b002099 | furniture | pages [22] -->
m

<!-- b002100 | furniture | pages [22] -->
m

<!-- b002101 | furniture | pages [22] -->
m

<!-- b002102 | furniture | pages [22] -->
m

<!-- b002103 | furniture | pages [22] -->
m

<!-- b002104 | furniture | pages [22] -->
m

<!-- b002105 | furniture | pages [22] -->
m

<!-- b002106 | furniture | pages [22] -->
m

<!-- b002107 | furniture | pages [22] -->
m

<!-- b002108 | furniture | pages [22] -->
m

<!-- b002109 | furniture | pages [22] -->
m

<!-- b002110 | furniture | pages [22] -->
m

<!-- b002111 | furniture | pages [22] -->
m

<!-- b002112 | furniture | pages [22] -->
m

<!-- b002113 | furniture | pages [22] -->
m

<!-- b002114 | furniture | pages [22] -->
m

<!-- b002115 | furniture | pages [22] -->
m

<!-- b002116 | furniture | pages [22] -->
m

<!-- b002117 | furniture | pages [22] -->
m

<!-- b002118 | furniture | pages [22] -->
m

<!-- b002119 | furniture | pages [22] -->
m

<!-- b002120 | furniture | pages [22] -->
m

<!-- b002121 | furniture | pages [22] -->
m

<!-- b002122 | furniture | pages [22] -->
m

<!-- b002123 | furniture | pages [22] -->
m

<!-- b002124 | furniture | pages [22] -->
m

<!-- b002125 | furniture | pages [22] -->
m

<!-- b002126 | furniture | pages [22] -->
m

<!-- b002127 | furniture | pages [22] -->
m

<!-- b002128 | furniture | pages [22] -->
m

<!-- b002129 | furniture | pages [22] -->
m

<!-- b002130 | furniture | pages [22] -->
m

<!-- b002131 | furniture | pages [22] -->
m

<!-- b002132 | furniture | pages [22] -->
m

<!-- b002133 | furniture | pages [22] -->
m

<!-- b002134 | furniture | pages [22] -->
m

<!-- b002135 | furniture | pages [22] -->
m

<!-- b002136 | furniture | pages [22] -->
m

<!-- b002137 | furniture | pages [22] -->
m

<!-- b002138 | furniture | pages [22] -->
m

<!-- b002139 | furniture | pages [22] -->
m

<!-- b002140 | furniture | pages [22] -->
m

<!-- b002141 | furniture | pages [22] -->
m

<!-- b002142 | furniture | pages [22] -->
m

<!-- b002143 | furniture | pages [22] -->
m

<!-- b002144 | furniture | pages [22] -->
m

<!-- b002145 | furniture | pages [22] -->
m

<!-- b002146 | furniture | pages [22] -->
m

<!-- b002147 | furniture | pages [22] -->
m

<!-- b002148 | furniture | pages [22] -->
m

<!-- b002149 | furniture | pages [22] -->
m

<!-- b002150 | furniture | pages [22] -->
m

<!-- b002151 | furniture | pages [22] -->
m

<!-- b002152 | furniture | pages [22] -->
m

<!-- b002153 | furniture | pages [22] -->
m

<!-- b002154 | furniture | pages [22] -->
m

<!-- b002155 | furniture | pages [22] -->
m

<!-- b002156 | furniture | pages [22] -->
m

<!-- b002157 | furniture | pages [22] -->
m

<!-- b002158 | furniture | pages [22] -->
m

<!-- b002159 | furniture | pages [22] -->
m

<!-- b002160 | furniture | pages [22] -->
m

<!-- b002161 | furniture | pages [22] -->
m

<!-- b002162 | furniture | pages [22] -->
m

<!-- b002163 | furniture | pages [22] -->
m

<!-- b002164 | furniture | pages [22] -->
m

<!-- b002165 | furniture | pages [22] -->
m

<!-- b002166 | furniture | pages [22] -->
m

<!-- b002167 | furniture | pages [22] -->
m

<!-- b002168 | furniture | pages [22] -->
m

<!-- b002169 | furniture | pages [22] -->
m

<!-- b002170 | furniture | pages [22] -->
m

<!-- b002171 | furniture | pages [22] -->
m

<!-- b002172 | furniture | pages [22] -->
m

<!-- b002173 | furniture | pages [22] -->
m

<!-- b002174 | furniture | pages [22] -->
m

<!-- b002175 | furniture | pages [22] -->
m

<!-- b002176 | furniture | pages [22] -->
m

<!-- b002177 | furniture | pages [22] -->
m

<!-- b002178 | furniture | pages [22] -->
m

<!-- b002179 | furniture | pages [22] -->
m

<!-- b002180 | furniture | pages [22] -->
m

<!-- b002181 | furniture | pages [22] -->
m

<!-- b002182 | furniture | pages [22] -->
m

<!-- b002183 | furniture | pages [22] -->
m

<!-- b002184 | furniture | pages [22] -->
m

<!-- b002185 | furniture | pages [22] -->
m

<!-- b002186 | furniture | pages [22] -->
m

<!-- b002187 | furniture | pages [22] -->
m

<!-- b002188 | furniture | pages [22] -->
m

<!-- b002189 | furniture | pages [22] -->
m

<!-- b002190 | furniture | pages [22] -->
m

<!-- b002191 | furniture | pages [22] -->
m

<!-- b002192 | furniture | pages [22] -->
m

<!-- b002193 | furniture | pages [22] -->
m

<!-- b002194 | furniture | pages [22] -->
m

<!-- b002195 | furniture | pages [22] -->
m

<!-- b002196 | furniture | pages [22] -->
m

<!-- b002197 | furniture | pages [22] -->
m

<!-- b002198 | furniture | pages [22] -->
m

<!-- b002199 | furniture | pages [22] -->
m

<!-- b002200 | furniture | pages [22] -->
m

<!-- b002201 | furniture | pages [22] -->
m

<!-- b002202 | furniture | pages [22] -->
m

<!-- b002203 | furniture | pages [22] -->
m

<!-- b002204 | furniture | pages [22] -->
m

<!-- b002205 | furniture | pages [22] -->
m

<!-- b002206 | furniture | pages [22] -->
m

<!-- b002207 | furniture | pages [22] -->
m

<!-- b002208 | furniture | pages [22] -->
m

<!-- b002209 | furniture | pages [22] -->
m

<!-- b002210 | furniture | pages [22] -->
m

<!-- b002211 | furniture | pages [22] -->
m

<!-- b002212 | furniture | pages [22] -->
m

<!-- b002213 | furniture | pages [22] -->
m

<!-- b002214 | furniture | pages [22] -->
m

<!-- b002215 | furniture | pages [22] -->
m

<!-- b002216 | furniture | pages [22] -->
m

<!-- b002217 | furniture | pages [22] -->
m

<!-- b002218 | furniture | pages [22] -->
m

<!-- b002219 | furniture | pages [22] -->
m

<!-- b002220 | furniture | pages [22] -->
m

<!-- b002221 | furniture | pages [22] -->
m

<!-- b002222 | furniture | pages [22] -->
m

<!-- b002223 | furniture | pages [22] -->
m

<!-- b002224 | furniture | pages [22] -->
m

<!-- b002225 | furniture | pages [22] -->
m

<!-- b002226 | furniture | pages [22] -->
m

<!-- b002227 | furniture | pages [22] -->
m

<!-- b002228 | furniture | pages [22] -->
m

<!-- b002229 | furniture | pages [22] -->
m

<!-- b002230 | furniture | pages [22] -->
m

<!-- b002231 | furniture | pages [22] -->
m

<!-- b002232 | furniture | pages [22] -->
m

<!-- b002233 | furniture | pages [22] -->
m

<!-- b002234 | furniture | pages [22] -->
m

<!-- b002235 | furniture | pages [22] -->
m

<!-- b002236 | furniture | pages [22] -->
m

<!-- b002237 | furniture | pages [22] -->
m

<!-- b002238 | furniture | pages [22] -->
m

<!-- b002239 | furniture | pages [22] -->
m

<!-- b002240 | furniture | pages [22] -->
m

<!-- b002241 | furniture | pages [22] -->
m

<!-- b002242 | furniture | pages [22] -->
m

<!-- b002243 | furniture | pages [22] -->
m

<!-- b002244 | furniture | pages [22] -->
m

<!-- b002245 | furniture | pages [22] -->
m

<!-- b002246 | furniture | pages [22] -->
m

<!-- b002247 | furniture | pages [22] -->
m

<!-- b002248 | furniture | pages [22] -->
m

<!-- b002249 | furniture | pages [22] -->
m

<!-- b002250 | furniture | pages [22] -->
m

<!-- b002251 | furniture | pages [22] -->
m

<!-- b002252 | furniture | pages [22] -->
m

<!-- b002253 | furniture | pages [22] -->
m

<!-- b002254 | furniture | pages [22] -->
m

<!-- b002255 | furniture | pages [22] -->
m

<!-- b002256 | furniture | pages [22] -->
m

<!-- b002257 | furniture | pages [22] -->
m

<!-- b002258 | furniture | pages [22] -->
m

<!-- b002259 | furniture | pages [22] -->
m

<!-- b002260 | furniture | pages [22] -->
m

<!-- b002261 | furniture | pages [22] -->
m

<!-- b002262 | furniture | pages [22] -->
m

<!-- b002263 | furniture | pages [22] -->
m

<!-- b002264 | furniture | pages [22] -->
m

<!-- b002265 | furniture | pages [22] -->
m

<!-- b002266 | furniture | pages [22] -->
m

<!-- b002267 | furniture | pages [22] -->
m

<!-- b002268 | furniture | pages [22] -->
m

<!-- b002269 | furniture | pages [22] -->
m

<!-- b002270 | furniture | pages [22] -->
m

<!-- b002271 | furniture | pages [22] -->
m

<!-- b002272 | furniture | pages [22] -->
m

<!-- b002273 | furniture | pages [22] -->
m

<!-- b002274 | furniture | pages [22] -->
m

<!-- b002275 | furniture | pages [22] -->
m

<!-- b002276 | furniture | pages [22] -->
m

<!-- b002277 | furniture | pages [22] -->
m

<!-- b002278 | furniture | pages [22] -->
m

<!-- b002279 | furniture | pages [22] -->
m

<!-- b002280 | furniture | pages [22] -->
m

<!-- b002281 | furniture | pages [22] -->
m

<!-- b002282 | furniture | pages [22] -->
m

<!-- b002283 | furniture | pages [22] -->
m

<!-- b002284 | furniture | pages [22] -->
m

<!-- b002285 | furniture | pages [22] -->
m

<!-- b002286 | furniture | pages [22] -->
m

<!-- b002287 | furniture | pages [22] -->
m

<!-- b002288 | furniture | pages [22] -->
m

<!-- b002289 | furniture | pages [22] -->
m

<!-- b002290 | furniture | pages [22] -->
m

<!-- b002291 | furniture | pages [22] -->
m

<!-- b002292 | furniture | pages [22] -->
m

<!-- b002293 | furniture | pages [22] -->
m

<!-- b002294 | furniture | pages [22] -->
m

<!-- b002295 | furniture | pages [22] -->
m

<!-- b002296 | furniture | pages [22] -->
m

<!-- b002297 | furniture | pages [22] -->
m

<!-- b002298 | furniture | pages [22] -->
m

<!-- b002299 | furniture | pages [22] -->
m

<!-- b002300 | furniture | pages [22] -->
m

<!-- b002301 | furniture | pages [22] -->
m

<!-- b002302 | furniture | pages [22] -->
m

<!-- b002303 | furniture | pages [22] -->
m

<!-- b002304 | furniture | pages [22] -->
m

<!-- b002305 | furniture | pages [22] -->
m

<!-- b002306 | furniture | pages [22] -->
m

<!-- b002307 | furniture | pages [22] -->
m

<!-- b002308 | furniture | pages [22] -->
m

<!-- b002309 | furniture | pages [22] -->
m

<!-- b002310 | furniture | pages [22] -->
m

<!-- b002311 | furniture | pages [22] -->
m

<!-- b002312 | furniture | pages [22] -->
m

<!-- b002313 | furniture | pages [22] -->
m

<!-- b002314 | furniture | pages [22] -->
m

<!-- b002315 | furniture | pages [22] -->
m

<!-- b002316 | furniture | pages [22] -->
m

<!-- b002317 | furniture | pages [22] -->
m

<!-- b002318 | furniture | pages [22] -->
m

<!-- b002319 | furniture | pages [22] -->
m

<!-- b002320 | furniture | pages [22] -->
m

<!-- b002321 | furniture | pages [22] -->
m

<!-- b002322 | furniture | pages [22] -->
m

<!-- b002323 | furniture | pages [22] -->
m

<!-- b002324 | furniture | pages [22] -->
m

<!-- b002325 | furniture | pages [22] -->
m

<!-- b002326 | furniture | pages [22] -->
m

<!-- b002327 | furniture | pages [22] -->
m

<!-- b002328 | furniture | pages [22] -->
m

<!-- b002329 | furniture | pages [22] -->
Team # 2516178

<!-- b002330 | furniture | pages [22] -->
Page 22 of 27

<!-- b002331 | furniture | pages [22] -->
m

<!-- b002332 | furniture | pages [22] -->
m

<!-- b002333 | furniture | pages [22] -->
m

<!-- b002334 | furniture | pages [22] -->
m

<!-- b002335 | furniture | pages [22] -->
m

<!-- b002336 | furniture | pages [22] -->
m

<!-- b002337 | furniture | pages [22] -->
m

<!-- b002338 | furniture | pages [22] -->
m

<!-- b002339 | furniture | pages [22] -->
m

<!-- b002340 | furniture | pages [22] -->
m

<!-- b002341 | furniture | pages [22] -->
m

<!-- b002342 | furniture | pages [22] -->
m

<!-- b002343 | furniture | pages [22] -->
m

<!-- b002344 | furniture | pages [22] -->
m

<!-- b002345 | furniture | pages [22] -->
m

<!-- b002346 | furniture | pages [22] -->
m

<!-- b002347 | furniture | pages [22] -->
m

<!-- b002348 | furniture | pages [22] -->
m

<!-- b002349 | furniture | pages [22] -->
m

<!-- b002350 | furniture | pages [22] -->
m

<!-- b002351 | furniture | pages [22] -->
m

<!-- b002352 | furniture | pages [22] -->
m

<!-- b002353 | furniture | pages [22] -->
m

<!-- b002354 | furniture | pages [22] -->
m

<!-- b002355 | furniture | pages [22] -->
m

<!-- b002356 | furniture | pages [22] -->
m

<!-- b002357 | furniture | pages [22] -->
m

<!-- b002358 | furniture | pages [22] -->
m

<!-- b002359 | furniture | pages [22] -->
m

<!-- b002360 | furniture | pages [22] -->
m

<!-- b002361 | furniture | pages [22] -->
m

<!-- b002362 | furniture | pages [22] -->
m

<!-- b002363 | furniture | pages [22] -->
m

<!-- b002364 | furniture | pages [22] -->
m

<!-- b002365 | furniture | pages [22] -->
m

<!-- b002366 | furniture | pages [22] -->
m

<!-- b002367 | furniture | pages [22] -->
m

<!-- b002368 | furniture | pages [22] -->
m

<!-- b002369 | furniture | pages [22] -->
m

<!-- b002370 | furniture | pages [22] -->
m

<!-- b002371 | furniture | pages [22] -->
m

<!-- b002372 | furniture | pages [22] -->
m

<!-- b002373 | furniture | pages [22] -->
m

<!-- b002374 | furniture | pages [22] -->
m

<!-- b002375 | furniture | pages [22] -->
m

<!-- b002376 | furniture | pages [22] -->
m

<!-- b002377 | furniture | pages [22] -->
m

<!-- b002378 | furniture | pages [22] -->
m

<!-- b002379 | furniture | pages [22] -->
m

<!-- b002380 | furniture | pages [22] -->
m

<!-- b002381 | furniture | pages [22] -->
m

<!-- b002382 | furniture | pages [22] -->
m

<!-- b002383 | furniture | pages [22] -->
m

<!-- b002384 | furniture | pages [22] -->
m

<!-- b002385 | furniture | pages [22] -->
m

<!-- b002386 | furniture | pages [22] -->
m

<!-- b002387 | furniture | pages [22] -->
m

<!-- b002388 | furniture | pages [22] -->
m

<!-- b002389 | furniture | pages [22] -->
m

<!-- b002390 | furniture | pages [22] -->
m

<!-- b002391 | furniture | pages [22] -->
m

<!-- b002392 | furniture | pages [22] -->
m

<!-- b002393 | furniture | pages [22] -->
m

<!-- b002394 | furniture | pages [22] -->
m

<!-- b002395 | furniture | pages [22] -->
m

<!-- b002396 | furniture | pages [22] -->
m

<!-- b002397 | furniture | pages [22] -->
m

<!-- b002398 | furniture | pages [22] -->
m

<!-- b002399 | furniture | pages [22] -->
m

<!-- b002400 | furniture | pages [22] -->
m

<!-- b002401 | furniture | pages [22] -->
m

<!-- b002402 | furniture | pages [22] -->
m

<!-- b002403 | furniture | pages [22] -->
m

<!-- b002404 | furniture | pages [22] -->
m

<!-- b002405 | furniture | pages [22] -->
m

<!-- b002406 | furniture | pages [22] -->
m

<!-- b002407 | furniture | pages [22] -->
m

<!-- b002408 | furniture | pages [22] -->
m

<!-- b002409 | furniture | pages [22] -->
m

<!-- b002410 | furniture | pages [22] -->
m

<!-- b002411 | furniture | pages [22] -->
m

<!-- b002412 | furniture | pages [22] -->
m

<!-- b002413 | furniture | pages [22] -->
m

<!-- b002414 | furniture | pages [22] -->
m

<!-- b002415 | furniture | pages [22] -->
m

<!-- b002416 | furniture | pages [22] -->
m

<!-- b002417 | furniture | pages [22] -->
m

<!-- b002418 | furniture | pages [22] -->
m

<!-- b002419 | furniture | pages [22] -->
m

<!-- b002420 | furniture | pages [22] -->
m

<!-- b002421 | furniture | pages [22] -->
m

<!-- b002422 | furniture | pages [22] -->
m

<!-- b002423 | furniture | pages [22] -->
m

<!-- b002424 | furniture | pages [22] -->
m

<!-- b002425 | furniture | pages [22] -->
m

<!-- b002426 | furniture | pages [22] -->
m

<!-- b002427 | furniture | pages [22] -->
m

<!-- b002428 | furniture | pages [22] -->
m

<!-- b002429 | furniture | pages [22] -->
m

<!-- b002430 | furniture | pages [22] -->
m

<!-- b002431 | furniture | pages [22] -->
m

<!-- b002432 | furniture | pages [22] -->
m

<!-- b002433 | furniture | pages [22] -->
m

<!-- b002434 | furniture | pages [22] -->
m

<!-- b002435 | furniture | pages [22] -->
m

<!-- b002436 | furniture | pages [22] -->
m

<!-- b002437 | furniture | pages [22] -->
m

<!-- b002438 | furniture | pages [22] -->
m

<!-- b002439 | furniture | pages [22] -->
m

<!-- b002440 | furniture | pages [22] -->
m

<!-- b002441 | furniture | pages [22] -->
m

<!-- b002442 | furniture | pages [22] -->
m

<!-- b002443 | furniture | pages [22] -->
m

<!-- b002444 | furniture | pages [22] -->
m

<!-- b002445 | furniture | pages [22] -->
m

<!-- b002446 | furniture | pages [22] -->
m

<!-- b002447 | furniture | pages [22] -->
m

<!-- b002448 | furniture | pages [22] -->
m

<!-- b002449 | furniture | pages [22] -->
m

<!-- b002450 | furniture | pages [22] -->
m

<!-- b002451 | furniture | pages [22] -->
m

<!-- b002452 | furniture | pages [22] -->
m

<!-- b002453 | furniture | pages [22] -->
m

<!-- b002454 | furniture | pages [22] -->
m

<!-- b002455 | furniture | pages [22] -->
m

<!-- b002456 | furniture | pages [22] -->
m

<!-- b002457 | furniture | pages [22] -->
m

<!-- b002458 | furniture | pages [22] -->
m

<!-- b002459 | furniture | pages [22] -->
m

<!-- b002460 | furniture | pages [22] -->
m

<!-- b002461 | furniture | pages [22] -->
m

<!-- b002462 | furniture | pages [22] -->
m

<!-- b002463 | furniture | pages [22] -->
m

<!-- b002464 | furniture | pages [22] -->
m

<!-- b002465 | furniture | pages [22] -->
m

<!-- b002466 | furniture | pages [22] -->
m

<!-- b002467 | furniture | pages [22] -->
m

<!-- b002468 | furniture | pages [22] -->
m

<!-- b002469 | furniture | pages [22] -->
m

<!-- b002470 | furniture | pages [22] -->
m

<!-- b002471 | furniture | pages [22] -->
m

<!-- b002472 | furniture | pages [22] -->
m

<!-- b002473 | furniture | pages [22] -->
m

<!-- b002474 | furniture | pages [22] -->
m

<!-- b002475 | furniture | pages [22] -->
m

<!-- b002476 | furniture | pages [22] -->
m

<!-- b002477 | furniture | pages [22] -->
m

<!-- b002478 | furniture | pages [22] -->
m

<!-- b002479 | furniture | pages [22] -->
m

<!-- b002480 | furniture | pages [22] -->
m

<!-- b002481 | furniture | pages [22] -->
m

<!-- b002482 | furniture | pages [22] -->
m

<!-- b002483 | furniture | pages [22] -->
m

<!-- b002484 | furniture | pages [22] -->
m

<!-- b002485 | furniture | pages [22] -->
m

<!-- b002486 | furniture | pages [22] -->
m

<!-- b002487 | furniture | pages [22] -->
m

<!-- b002488 | furniture | pages [22] -->
m

<!-- b002489 | furniture | pages [22] -->
m

<!-- b002490 | furniture | pages [22] -->
m

<!-- b002491 | furniture | pages [22] -->
m

<!-- b002492 | furniture | pages [22] -->
m

<!-- b002493 | furniture | pages [22] -->
m

<!-- b002494 | furniture | pages [22] -->
m

<!-- b002495 | furniture | pages [22] -->
m

<!-- b002496 | furniture | pages [22] -->
m

<!-- b002497 | furniture | pages [22] -->
m

<!-- b002498 | furniture | pages [22] -->
m

<!-- b002499 | furniture | pages [22] -->
m

<!-- b002500 | furniture | pages [22] -->
m

<!-- b002501 | furniture | pages [22] -->
m

<!-- b002502 | furniture | pages [22] -->
m

<!-- b002503 | furniture | pages [22] -->
m

<!-- b002504 | furniture | pages [22] -->
m

<!-- b002505 | furniture | pages [22] -->
m

<!-- b002506 | furniture | pages [22] -->
m

<!-- b002507 | furniture | pages [22] -->
m

<!-- b002508 | furniture | pages [22] -->
m

<!-- b002509 | furniture | pages [22] -->
m

<!-- b002510 | furniture | pages [22] -->
m

<!-- b002511 | furniture | pages [22] -->
m

<!-- b002512 | furniture | pages [22] -->
m

<!-- b002513 | furniture | pages [22] -->
m

<!-- b002514 | furniture | pages [22] -->
m

<!-- b002516 | prose | pages [22] -->
1988 48 0.0 0.0 58.5 6.6 7.7 1992 0 16.0 32.0 10.9 22.5 39.6 1996 48 0.0 0.0 57.9 9.0 11.2 2000 48 0.0 0.0 66.0 11.3 7.3 2004 0 0.0 48.0 11.9 7.6 57.3 2008 0 0.0 0.0 11.8 6.4 6.5 2012 0 16.0 0.0 10.1 23.7 10.5 2016 0 48.0 17.0 10.0 56.6 29.1 2020 0 18.0 0.0 9.6 28.6 9.2 2024 0 0.0 0.0 9.6 15.9 7.4 The British women's hockey team has had a mediocre track record in the past, often rank- ing in the lower-middle positions in international competitions. With the new coach on board, the team has demonstrated a clear upward trend, and we anticipate a significant rise in its medal-winning rate in various future events.

<!-- b002517 | prose | pages [22] -->
Australia, a traditional powerhouse, achieved an outstanding five-consecutive-champion- ship feat in the 1990s and claimed gold medals in numerous Olympic Games. Despite signifi- cant performance fluctuations in recent years, under the new coach's guidance, we expect the number of medals it wins to increase steadily. However, as the team already has a well-estab- lished system, it will take time for the new and old coaching concepts to be harmonized.

<!-- b002518 | prose | pages [22] -->
The German team has long struggled with performance instability. Even after the new coach took over, this situation has not seen fundamental improvement. This suggests that the team may be facing profound challenges in areas such as player selection and tactics, and it will be difficult for the coach alone to overcome these bottlenecks in the short term.

<!-- b002519 | heading | pages [22] -->
8 Novel Insights from SHAP Analysis in Olympic Performance

<!-- b002520 | prose | pages [22] -->
SHAP values provide a sophisticated framework for model interpretation through SHAP Summary Plots. These plots offer two complementary visualization approaches to demonstrate feature impacts on model predictions [12]: feature importance ranking and feature effect sum- mary:

<!-- b002521 | prose | pages [22, 23] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b002522 | furniture | pages [22] -->
2

<!-- b002523 | furniture | pages [22] -->
MATHmodels

<!-- b002524 | furniture | pages [22] -->
获取更多资讯

<!-- b002525 | furniture | pages [23] -->
Team # 2516178

<!-- b002526 | furniture | pages [23] -->
Page 23 of 27

<!-- b002528 | caption | pages [23] -->
Figure 13 Analysis of SHAP Values of Participation Numbers and Events on Medal Winning

<!-- b002529 | prose | pages [23] -->
The SHAP Summary Plot reveals intricate patterns of feature influence through point dis- tribution and color coding, illustrating both the direction and magnitude of feature effects on prediction outcomes. For instance, in the case of country_Athletics, the concentration of yellow points (indicating high participation) in the positive SHAP value region demonstrates a strong positive correlation between high participation in athletics and improved medal predictions.

<!-- b002530 | prose | pages [23] -->
The bar chart component displays mean absolute SHAP values, quantifying each feature's overall importance to prediction outcomes. Total participation emerges as the dominant factor, exhibiting the highest SHAP value and confirming its critical role in Olympic medal acquisition. Following closely are country_Athletics and country_Swimming, validating these disciplines' fundamental importance in Olympic competition.

<!-- b002531 | prose | pages [23] -->
Based on these SHAP analyses, we propose a dual-track approach to optimizing Olympic competitive strategies. The first track involves maintaining competitiveness in traditional strength events while strategically expanding participation scales. The second track emphasizes data-driven identification and development of emerging events with potential competitive ad- vantages. This quantitative approach to strategy optimization not only enhances performance in individual events but also promotes balanced development of national Olympic capabilities.

<!-- b002532 | prose | pages [23] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b002533 | furniture | pages [23] -->
m

<!-- b002534 | furniture | pages [23] -->
m

<!-- b002535 | furniture | pages [23] -->
m

<!-- b002536 | furniture | pages [23] -->
m

<!-- b002537 | furniture | pages [23] -->
m

<!-- b002538 | furniture | pages [23] -->
m

<!-- b002539 | furniture | pages [23] -->
m

<!-- b002540 | furniture | pages [23] -->
m

<!-- b002541 | furniture | pages [23] -->
m

<!-- b002542 | furniture | pages [23] -->
m

<!-- b002543 | furniture | pages [23] -->
m

<!-- b002544 | furniture | pages [23] -->
m

<!-- b002545 | furniture | pages [23] -->
m

<!-- b002546 | furniture | pages [23] -->
m

<!-- b002547 | furniture | pages [23] -->
m

<!-- b002548 | furniture | pages [23] -->
m

<!-- b002549 | furniture | pages [23] -->
m

<!-- b002550 | furniture | pages [23] -->
m

<!-- b002551 | furniture | pages [23] -->
m

<!-- b002552 | furniture | pages [23] -->
m

<!-- b002553 | furniture | pages [23] -->
m

<!-- b002554 | furniture | pages [23] -->
m

<!-- b002555 | furniture | pages [23] -->
m

<!-- b002556 | furniture | pages [23] -->
m

<!-- b002557 | furniture | pages [23] -->
m

<!-- b002558 | furniture | pages [23] -->
m

<!-- b002559 | furniture | pages [23] -->
m

<!-- b002560 | furniture | pages [23] -->
m

<!-- b002561 | furniture | pages [23] -->
m

<!-- b002562 | furniture | pages [23] -->
m

<!-- b002563 | furniture | pages [23] -->
m

<!-- b002564 | furniture | pages [23] -->
m

<!-- b002565 | furniture | pages [23] -->
m

<!-- b002566 | furniture | pages [23] -->
m

<!-- b002567 | furniture | pages [23] -->
m

<!-- b002568 | furniture | pages [23] -->
m

<!-- b002569 | furniture | pages [23] -->
m

<!-- b002570 | furniture | pages [23] -->
m

<!-- b002571 | furniture | pages [23] -->
m

<!-- b002572 | furniture | pages [23] -->
m

<!-- b002573 | furniture | pages [23] -->
m

<!-- b002574 | furniture | pages [23] -->
m

<!-- b002575 | furniture | pages [23] -->
m

<!-- b002576 | furniture | pages [23] -->
m

<!-- b002577 | furniture | pages [23] -->
m

<!-- b002578 | furniture | pages [23] -->
m

<!-- b002579 | furniture | pages [23] -->
m

<!-- b002580 | furniture | pages [23] -->
m

<!-- b002581 | furniture | pages [23] -->
m

<!-- b002582 | furniture | pages [23] -->
m

<!-- b002583 | furniture | pages [23] -->
m

<!-- b002584 | furniture | pages [23] -->
m

<!-- b002585 | furniture | pages [23] -->
m

<!-- b002586 | furniture | pages [23] -->
m

<!-- b002587 | furniture | pages [23] -->
m

<!-- b002588 | furniture | pages [23] -->
m

<!-- b002589 | furniture | pages [23] -->
m

<!-- b002590 | furniture | pages [23] -->
m

<!-- b002591 | furniture | pages [23] -->
m

<!-- b002592 | furniture | pages [23] -->
m

<!-- b002593 | furniture | pages [23] -->
m

<!-- b002594 | furniture | pages [23] -->
m

<!-- b002595 | furniture | pages [23] -->
m

<!-- b002596 | furniture | pages [23] -->
m

<!-- b002597 | furniture | pages [23] -->
m

<!-- b002598 | furniture | pages [23] -->
m

<!-- b002599 | furniture | pages [23] -->
m

<!-- b002600 | furniture | pages [23] -->
m

<!-- b002601 | furniture | pages [23] -->
m

<!-- b002602 | furniture | pages [23] -->
m

<!-- b002603 | furniture | pages [23] -->
m

<!-- b002604 | furniture | pages [23] -->
m

<!-- b002605 | furniture | pages [23] -->
m

<!-- b002606 | furniture | pages [23] -->
m

<!-- b002607 | furniture | pages [23] -->
m

<!-- b002608 | furniture | pages [23] -->
m

<!-- b002609 | furniture | pages [23] -->
m

<!-- b002610 | furniture | pages [23] -->
m

<!-- b002611 | furniture | pages [23] -->
m

<!-- b002612 | furniture | pages [23] -->
m

<!-- b002613 | furniture | pages [23] -->
m

<!-- b002614 | furniture | pages [23] -->
m

<!-- b002615 | furniture | pages [23] -->
m

<!-- b002616 | furniture | pages [23] -->
m

<!-- b002617 | furniture | pages [23] -->
m

<!-- b002618 | furniture | pages [23] -->
m

<!-- b002619 | furniture | pages [23] -->
m

<!-- b002620 | furniture | pages [23] -->
m

<!-- b002621 | furniture | pages [23] -->
m

<!-- b002622 | furniture | pages [23] -->
m

<!-- b002623 | furniture | pages [23] -->
m

<!-- b002624 | furniture | pages [23] -->
m

<!-- b002625 | furniture | pages [23] -->
m

<!-- b002626 | furniture | pages [23] -->
m

<!-- b002627 | furniture | pages [23] -->
m

<!-- b002628 | furniture | pages [23] -->
m

<!-- b002629 | furniture | pages [23] -->
m

<!-- b002630 | furniture | pages [23] -->
m

<!-- b002631 | furniture | pages [23] -->
m

<!-- b002632 | furniture | pages [23] -->
m

<!-- b002633 | furniture | pages [23] -->
m

<!-- b002634 | furniture | pages [23] -->
m

<!-- b002635 | furniture | pages [23] -->
m

<!-- b002636 | furniture | pages [23] -->
m

<!-- b002637 | furniture | pages [23] -->
m

<!-- b002638 | furniture | pages [23] -->
m

<!-- b002639 | furniture | pages [23] -->
m

<!-- b002640 | furniture | pages [23] -->
m

<!-- b002641 | furniture | pages [23] -->
m

<!-- b002642 | furniture | pages [23] -->
m

<!-- b002643 | furniture | pages [23] -->
m

<!-- b002644 | furniture | pages [23] -->
m

<!-- b002645 | furniture | pages [23] -->
m

<!-- b002646 | furniture | pages [23] -->
m

<!-- b002647 | furniture | pages [23] -->
m

<!-- b002648 | furniture | pages [23] -->
m

<!-- b002649 | furniture | pages [23] -->
m

<!-- b002650 | furniture | pages [23] -->
m

<!-- b002651 | furniture | pages [23] -->
m

<!-- b002652 | furniture | pages [23] -->
m

<!-- b002653 | furniture | pages [23] -->
m

<!-- b002654 | furniture | pages [23] -->
m

<!-- b002655 | furniture | pages [23] -->
m

<!-- b002656 | furniture | pages [23] -->
m

<!-- b002657 | furniture | pages [23] -->
m

<!-- b002658 | furniture | pages [23] -->
m

<!-- b002659 | furniture | pages [23] -->
m

<!-- b002660 | furniture | pages [23] -->
m

<!-- b002661 | furniture | pages [23] -->
m

<!-- b002662 | furniture | pages [23] -->
m

<!-- b002663 | furniture | pages [23] -->
m

<!-- b002664 | furniture | pages [23] -->
m

<!-- b002665 | furniture | pages [23] -->
m

<!-- b002666 | furniture | pages [23] -->
m

<!-- b002667 | furniture | pages [23] -->
m

<!-- b002668 | furniture | pages [23] -->
m

<!-- b002669 | furniture | pages [23] -->
m

<!-- b002670 | furniture | pages [23] -->
m

<!-- b002671 | furniture | pages [23] -->
m

<!-- b002672 | furniture | pages [23] -->
m

<!-- b002673 | furniture | pages [23] -->
m

<!-- b002674 | furniture | pages [23] -->
m

<!-- b002675 | furniture | pages [23] -->
m

<!-- b002676 | furniture | pages [23] -->
m

<!-- b002677 | furniture | pages [23] -->
m

<!-- b002678 | furniture | pages [23] -->
m

<!-- b002679 | furniture | pages [23] -->
m

<!-- b002680 | furniture | pages [23] -->
m

<!-- b002681 | furniture | pages [23] -->
m

<!-- b002682 | furniture | pages [23] -->
m

<!-- b002683 | furniture | pages [23] -->
m

<!-- b002684 | furniture | pages [23] -->
m

<!-- b002685 | furniture | pages [23] -->
m

<!-- b002686 | furniture | pages [23] -->
m

<!-- b002687 | furniture | pages [23] -->
m

<!-- b002688 | furniture | pages [23] -->
m

<!-- b002689 | furniture | pages [23] -->
m

<!-- b002690 | furniture | pages [23] -->
m

<!-- b002691 | furniture | pages [23] -->
m

<!-- b002692 | furniture | pages [23] -->
m

<!-- b002693 | furniture | pages [23] -->
m

<!-- b002694 | furniture | pages [23] -->
m

<!-- b002695 | furniture | pages [23] -->
m

<!-- b002696 | furniture | pages [23] -->
m

<!-- b002697 | furniture | pages [23] -->
m

<!-- b002698 | furniture | pages [23] -->
m

<!-- b002699 | furniture | pages [23] -->
m

<!-- b002700 | furniture | pages [23] -->
m

<!-- b002701 | furniture | pages [23] -->
m

<!-- b002702 | furniture | pages [23] -->
m

<!-- b002703 | furniture | pages [23] -->
m

<!-- b002704 | furniture | pages [23] -->
m

<!-- b002705 | furniture | pages [23] -->
m

<!-- b002706 | furniture | pages [23] -->
m

<!-- b002707 | furniture | pages [23] -->
m

<!-- b002708 | furniture | pages [23] -->
m

<!-- b002709 | furniture | pages [23] -->
m

<!-- b002710 | furniture | pages [23] -->
m

<!-- b002711 | furniture | pages [23] -->
m

<!-- b002712 | furniture | pages [23] -->
m

<!-- b002713 | furniture | pages [23] -->
m

<!-- b002714 | furniture | pages [23] -->
m

<!-- b002715 | furniture | pages [23] -->
m

<!-- b002716 | furniture | pages [23] -->
m

<!-- b002717 | furniture | pages [23] -->
m

<!-- b002718 | furniture | pages [23] -->
m

<!-- b002719 | furniture | pages [23] -->
m

<!-- b002720 | furniture | pages [23] -->
m

<!-- b002721 | furniture | pages [23] -->
m

<!-- b002722 | furniture | pages [23] -->
m

<!-- b002723 | furniture | pages [23] -->
m

<!-- b002724 | furniture | pages [23] -->
m

<!-- b002725 | furniture | pages [23] -->
m

<!-- b002726 | furniture | pages [23] -->
m

<!-- b002727 | furniture | pages [23] -->
m

<!-- b002728 | furniture | pages [23] -->
m

<!-- b002729 | furniture | pages [23] -->
m

<!-- b002730 | furniture | pages [23] -->
m

<!-- b002731 | furniture | pages [23] -->
m

<!-- b002732 | furniture | pages [23] -->
m

<!-- b002733 | furniture | pages [23] -->
m

<!-- b002734 | furniture | pages [23] -->
m

<!-- b002735 | furniture | pages [23] -->
m

<!-- b002736 | furniture | pages [23] -->
m

<!-- b002737 | furniture | pages [23] -->
m

<!-- b002738 | furniture | pages [23] -->
m

<!-- b002739 | furniture | pages [23] -->
m

<!-- b002740 | furniture | pages [23] -->
m

<!-- b002741 | furniture | pages [23] -->
m

<!-- b002742 | furniture | pages [23] -->
m

<!-- b002743 | furniture | pages [23] -->
m

<!-- b002744 | furniture | pages [23] -->
m

<!-- b002745 | furniture | pages [23] -->
m

<!-- b002746 | furniture | pages [23] -->
m

<!-- b002747 | furniture | pages [23] -->
m

<!-- b002748 | furniture | pages [23] -->
m

<!-- b002749 | furniture | pages [23] -->
m

<!-- b002750 | furniture | pages [23] -->
m

<!-- b002751 | furniture | pages [23] -->
m

<!-- b002752 | furniture | pages [23] -->
m

<!-- b002753 | furniture | pages [23] -->
m

<!-- b002754 | furniture | pages [23] -->
m

<!-- b002755 | furniture | pages [23] -->
m

<!-- b002756 | furniture | pages [23] -->
m

<!-- b002757 | furniture | pages [23] -->
m

<!-- b002758 | furniture | pages [23] -->
m

<!-- b002759 | furniture | pages [23] -->
m

<!-- b002760 | furniture | pages [23] -->
m

<!-- b002761 | furniture | pages [23] -->
m

<!-- b002762 | furniture | pages [23] -->
m

<!-- b002763 | furniture | pages [23] -->
m

<!-- b002764 | furniture | pages [23] -->
m

<!-- b002765 | furniture | pages [23] -->
m

<!-- b002766 | furniture | pages [23] -->
m

<!-- b002767 | furniture | pages [23] -->
m

<!-- b002768 | furniture | pages [23] -->
m

<!-- b002769 | furniture | pages [23] -->
m

<!-- b002770 | furniture | pages [23] -->
m

<!-- b002771 | furniture | pages [23] -->
m

<!-- b002772 | furniture | pages [23] -->
m

<!-- b002773 | furniture | pages [23] -->
m

<!-- b002774 | furniture | pages [23] -->
m

<!-- b002775 | furniture | pages [23] -->
m

<!-- b002776 | furniture | pages [23] -->
m

<!-- b002777 | furniture | pages [23] -->
m

<!-- b002778 | furniture | pages [23] -->
m

<!-- b002779 | furniture | pages [23] -->
m

<!-- b002780 | furniture | pages [23] -->
m

<!-- b002781 | furniture | pages [23] -->
m

<!-- b002782 | furniture | pages [23] -->
m

<!-- b002783 | furniture | pages [23] -->
m

<!-- b002784 | furniture | pages [23] -->
m

<!-- b002785 | furniture | pages [23] -->
m

<!-- b002786 | furniture | pages [23] -->
m

<!-- b002787 | furniture | pages [23] -->
m

<!-- b002788 | furniture | pages [23] -->
m

<!-- b002789 | furniture | pages [23] -->
m

<!-- b002790 | furniture | pages [23] -->
m

<!-- b002791 | furniture | pages [23] -->
m

<!-- b002792 | furniture | pages [23] -->
m

<!-- b002793 | furniture | pages [23] -->
m

<!-- b002794 | furniture | pages [23] -->
m

<!-- b002795 | furniture | pages [23] -->
m

<!-- b002796 | furniture | pages [23] -->
m

<!-- b002797 | furniture | pages [23] -->
m

<!-- b002798 | furniture | pages [23] -->
m

<!-- b002799 | furniture | pages [23] -->
m

<!-- b002800 | furniture | pages [23] -->
m

<!-- b002801 | furniture | pages [23] -->
m

<!-- b002802 | furniture | pages [23] -->
m

<!-- b002803 | furniture | pages [23] -->
m

<!-- b002804 | furniture | pages [23] -->
m

<!-- b002805 | furniture | pages [23] -->
m

<!-- b002806 | furniture | pages [23] -->
m

<!-- b002807 | furniture | pages [23] -->
m

<!-- b002808 | furniture | pages [23] -->
m

<!-- b002809 | furniture | pages [23] -->
m

<!-- b002810 | furniture | pages [23] -->
m

<!-- b002811 | furniture | pages [23] -->
m

<!-- b002812 | furniture | pages [23] -->
m

<!-- b002813 | furniture | pages [23] -->
m

<!-- b002814 | furniture | pages [23] -->
m

<!-- b002815 | furniture | pages [23] -->
m

<!-- b002816 | furniture | pages [23] -->
m

<!-- b002817 | furniture | pages [23] -->
m

<!-- b002818 | furniture | pages [23] -->
m

<!-- b002819 | furniture | pages [23] -->
m

<!-- b002820 | furniture | pages [23] -->
m

<!-- b002821 | furniture | pages [23] -->
m

<!-- b002822 | furniture | pages [23] -->
m

<!-- b002823 | furniture | pages [23] -->
m

<!-- b002824 | furniture | pages [23] -->
m

<!-- b002825 | furniture | pages [23] -->
m

<!-- b002826 | furniture | pages [23] -->
m

<!-- b002827 | furniture | pages [23] -->
m

<!-- b002828 | furniture | pages [23] -->
m

<!-- b002829 | furniture | pages [23] -->
m

<!-- b002830 | furniture | pages [23] -->
m

<!-- b002831 | furniture | pages [23] -->
m

<!-- b002832 | furniture | pages [23] -->
m

<!-- b002833 | furniture | pages [23] -->
m

<!-- b002834 | furniture | pages [23] -->
m

<!-- b002835 | furniture | pages [23] -->
m

<!-- b002836 | furniture | pages [23] -->
m

<!-- b002837 | furniture | pages [23] -->
m

<!-- b002838 | furniture | pages [23] -->
m

<!-- b002839 | furniture | pages [23] -->
m

<!-- b002840 | furniture | pages [23] -->
m

<!-- b002841 | furniture | pages [23] -->
m

<!-- b002842 | furniture | pages [23] -->
m

<!-- b002843 | furniture | pages [23] -->
m

<!-- b002844 | furniture | pages [23] -->
m

<!-- b002845 | furniture | pages [23] -->
m

<!-- b002846 | furniture | pages [23] -->
m

<!-- b002847 | furniture | pages [23] -->
m

<!-- b002848 | furniture | pages [23] -->
m

<!-- b002849 | furniture | pages [23] -->
m

<!-- b002850 | furniture | pages [23] -->
m

<!-- b002851 | furniture | pages [23] -->
m

<!-- b002852 | furniture | pages [23] -->
m

<!-- b002853 | furniture | pages [23] -->
m

<!-- b002854 | furniture | pages [23] -->
m

<!-- b002855 | furniture | pages [23] -->
m

<!-- b002856 | furniture | pages [23] -->
m

<!-- b002857 | furniture | pages [24] -->
Page 24 of 27

<!-- b002858 | furniture | pages [24] -->
Team # 2516178

<!-- b002859 | heading | pages [24] -->
9 Sensitivity Analysis

<!-- b002860 | prose | pages [24] -->
In the model-building process, when performing a sensitivity analysis of XGBoost's hy- perparameters, the max_depth parameter is selected as a crucial factor in controlling the com- plexity of the decision tree.

<!-- b002861 | prose | pages [24] -->
40 max_depth=4 (default) max_depth=3 Gold Medal Number 30 max_depth=6 max_depth=9 20

<!-- b002862 | prose | pages [24] -->
10

<!-- b002863 | prose | pages [24] -->
0

<!-- b002864 | prose | pages [24] -->
20 40 60 80 0

<!-- b002865 | caption | pages [24] -->
Figure 14 Visualization of Sensitivity Analysis

<!-- b002866 | prose | pages [24] -->
max_depth directly determines the tree's depth, thereby influencing the model's capacity to learn data features and its generalization ability. A large value of max_depth tends to result in over-fitting, while a small value may lead to under-fitting. Based on the results presented in the line chart, the prediction curves for different max_depth values exhibit significant discrep- ancies.

<!-- b002867 | prose | pages [24] -->
With an initial setting of max_depth = 4, the model's prediction results are at a certain level. When max_depth is decreased to 3, the prediction curve experiences an increased fluc- tuation range, suggesting heightened instability in the predicted values. When max_depth is set to 6, the prediction curve remains relatively stable, indicating that the model performs stably at this point. When max_depth = 9, the prediction curve shows a substantial upward trend in the later phase.

<!-- b002868 | prose | pages [24] -->
These results demonstrate that the choice of the max_depth hyperparameter significantly impacts the accuracy and stability of the model's gold-medal-count prediction. In practical ap- plications, it is essential to finely tune this parameter according to the dataset characteristics and model performance metrics to optimize the model's performance.

<!-- b002869 | heading | pages [24] -->
10 Model Evaluation

<!-- b002870 | heading | pages [24] -->
10.1 Strengths

<!-- b002871 | heading | pages [24] -->
1. Model innovation: The dual-staged XGBoost model combines classifiers and regres-

<!-- b002872 | prose | pages [24] -->
sors, enhancing the accuracy of medal predictions.

<!-- b002873 | prose | pages [24] -->
f  st do so-dd at  ss ds ssd at amosns ts ensure data quality.

<!-- b002874 | prose | pages [24, 25] -->
关注数学模型 3. Comprehensive model evaluation: Various evaluation indicators are adopted to com- prehensively measure the performance of the dual-stage XGBoost model and display its pre- diction effects from multiple dimensions.

<!-- b002875 | furniture | pages [24] -->
获取更多资讯

<!-- b002876 | furniture | pages [25] -->
Team # 2516178

<!-- b002877 | furniture | pages [25] -->
Page 25 of 27

<!-- b002879 | prose | pages [25] -->
4. In-depth variable analysis: Variables are analyzed and quantified in detail, and SHAP values are used to analyze the influence of events on medal acquisition in China and the US, exploring variable relationships and providing a basis for practical applications.

<!-- b002880 | heading | pages [25] -->
10.2 Weaknesses

<!-- b002881 | prose | pages [25] -->
1.  There is a lack of exploration of the impact of more factors on medal performance.

<!-- b002882 | prose | pages [25] -->
2.  The model for the "coaching effect" can be further optimized.

<!-- b002883 | prose | pages [25] -->
微信公众号：数学模型

<!-- b002884 | heading | pages [25] -->
References

<!-- b002885 | references | pages [25] -->
1. Ball, D.W., Olympic Games Competition: Structural Correlates of National Success.

<!-- b002886 | references | pages [25] -->
International Journal of Comparative Sociology, 1972. 13: p. 186 - 200.

<!-- b002887 | references | pages [25] -->
2. Schlembach, C., et al., Forecasting the Olympic medal distribution – A socioeconomic

<!-- b002888 | references | pages [25] -->
machine learning model. Technological Forecasting and Social Change, 2022. 175: p. 121314.

<!-- b002889 | references | pages [25] -->
3. Bernard, A.B. and M.R. Busse, Who Wins the Olympic Games: Economic Resources

<!-- b002890 | references | pages [25] -->
and Medal Totals. The Review of Economics and Statistics, 2004. 86(1): p. 413-417.

<!-- b002891 | references | pages [25] -->
4. Ibrahem Ahmed Osman, A., et al., Extreme gradient boosting (Xgboost) model to

<!-- b002892 | references | pages [25] -->
微信号：MATHmodels

<!-- b002893 | references | pages [25] -->
predict the groundwater levels in Selangor Malaysia. Ain Shams Engineering Journal, 2021.

<!-- b002894 | references | pages [25] -->
12.

<!-- b002895 | references | pages [25] -->
5. Nellore, S.B. Various performance measures in Binary classification –An Overview of

<!-- b002896 | references | pages [25] -->
ROC study. 2015.

<!-- b002897 | references | pages [25] -->
6. Zhou, J., et al., Estimation of the TBM advance rate under hard rock conditions using

<!-- b002898 | references | pages [25] -->
XGBoost and Bayesian optimization. Underground Space, 2021. 6(5): p. 506-515.

<!-- b002899 | references | pages [25] -->
7. Putatunda, S. and D. Kiran R, A Comparative Analysis of Hyperopt as Against Other

<!-- b002900 | references | pages [25] -->
Approaches for Hyper-Parameter Optimization of XGBoost. 2018. 6-10.

<!-- b002901 | references | pages [25] -->
8. Bergstra, J. and Y. Bengio, Random Search for Hyper-Parameter Optimization. J.

<!-- b002902 | references | pages [25] -->
Mach. Learn. Res., 2012. 13: p. 281-305.

<!-- b002903 | references | pages [25] -->
9. Kumbhakar, S.C. and Y. Wang, Global COVID-19 under-reporting: A Tobit model.

<!-- b002904 | references | pages [25] -->
Economic Modelling, 2024. 141: p. 106917.

<!-- b002905 | references | pages [25] -->
10. Vulimiri, P.S., et al., A mean–variance estimation bidirectional convolutional long

<!-- b002906 | references | pages [25] -->
short-term memory surrogate model predicting residual stress and model error for laser

<!-- b002907 | references | pages [25] -->
powder bed fusion. Additive Manufacturing, 2025. 97: p. 104591.

<!-- b002908 | references | pages [25] -->
11. Bergmeir, C. and J.M. Benítez, On the use of cross-validation for time series predictor

<!-- b002909 | references | pages [25] -->
evaluation. Information Sciences, 2012. 191: p. 192-213.

<!-- b002910 | references | pages [25] -->
12. Yu, R., et al., Interpretable predictive modelling of outlet temperatures in Central

<!-- b002911 | references | pages [25] -->
Alberta’s hydrothermal system using boosting-based ensemble learning incorporating Shapley

<!-- b002912 | references | pages [25] -->
Additive exPlanations (SHAP) approach. Energy, 2025: p. 134738.

<!-- b002913 | furniture | pages [26] -->
Team # 2516178

<!-- b002914 | furniture | pages [26] -->
Page 26 of 27

<!-- b002915 | heading | pages [26] -->
Report on Use of AI

<!-- b002916 | ai_disclosure | pages [26] -->
OpenAI ChatGPT(March, 2023 version, ChatGPT v2)

<!-- b002917 | ai_disclosure | pages [26] -->
Query1: What's the pros and cons between XGBoost and Random Forest model?

<!-- b002918 | ai_disclosure | pages [26] -->
Output:

<!-- b002919 | ai_disclosure | pages [26] -->
XGBoost vs. Random Forest

<!-- b002920 | ai_disclosure | pages [26] -->
XGBoost

<!-- b002921 | ai_disclosure | pages [26] -->
Pros: High accuracy, handles imbalanced data well, supports regulariza-

<!-- b002922 | ai_disclosure | pages [26] -->
tion, and is highly flexible.

<!-- b002923 | ai_disclosure | pages [26] -->
Cons: Complex, requires careful tuning, prone to overfitting, and slower

<!-- b002924 | ai_disclosure | pages [26] -->
for large datasets.

<!-- b002925 | ai_disclosure | pages [26] -->
Random Forest

<!-- b002926 | ai_disclosure | pages [26] -->
Pros: Simple, robust, less prone to overfitting, faster to train, and easier

<!-- b002927 | ai_disclosure | pages [26] -->
to interpret.

<!-- b002928 | ai_disclosure | pages [26] -->
Cons: Lower accuracy on complex datasets, treats all samples equally,

<!-- b002929 | ai_disclosure | pages [26] -->
and can be inefficient on large data.

<!-- b002930 | ai_disclosure | pages [26] -->
When to Use

<!-- b002931 | ai_disclosure | pages [26] -->
XGBoost: For complex, structured data requiring high accuracy and

<!-- b002932 | ai_disclosure | pages [26] -->
fine-tuning.

<!-- b002933 | ai_disclosure | pages [26] -->
Random Forest: For simpler problems needing quick, interpretable re-

<!-- b002934 | ai_disclosure | pages [26] -->
sults with minimal tuning.

<!-- b002935 | ai_disclosure | pages [26] -->
Query2: What advantage would a host country of the Olympics get? In terms of com-

<!-- b002936 | ai_disclosure | pages [26] -->
petition wise.

<!-- b002937 | ai_disclosure | pages [26] -->
Output:

<!-- b002938 | ai_disclosure | pages [26] -->
Hosting the Olympics offers several competitive advantages:

<!-- b002939 | ai_disclosure | pages [26] -->
Home Field Advantage: Athletes benefit from familiar venues, support-

<!-- b002940 | ai_disclosure | pages [26] -->
ive crowds, and no travel fatigue.

<!-- b002941 | ai_disclosure | pages [26] -->
Increased Participation: Host nations often qualify automatically for

<!-- b002942 | ai_disclosure | pages [26] -->
certain events and can field larger teams.

<!-- b002943 | ai_disclosure | pages [26] -->
Enhanced Preparation: More resources are invested in training, coach-

<!-- b002944 | ai_disclosure | pages [26] -->
ing, and facilities.

<!-- b002945 | ai_disclosure | pages [26] -->
Psychological Boost: Competing on home soil boosts morale and na-

<!-- b002946 | ai_disclosure | pages [26] -->
tional pride.

<!-- b002947 | ai_disclosure | pages [26] -->
Event Scheduling: Hosts can influence schedules to favor their athletes.

<!-- b002948 | ai_disclosure | pages [26] -->
Historically, host countries often see a "medal boost," as seen with Aus-

<!-- b002949 | ai_disclosure | pages [26] -->
tralia in 2000 and Great Britain in 2012.

<!-- b002950 | ai_disclosure | pages [26] -->
Query3: What factors could have a great influence on Olympic Games' results? Other

<!-- b002951 | ai_disclosure | pages [26] -->
than training or coaching.

<!-- b002952 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b002953 | furniture | pages [26] -->
2

<!-- b002954 | furniture | pages [26] -->
MATHmodels

<!-- b002955 | furniture | pages [26] -->
获取更多资讯

<!-- b002956 | furniture | pages [27] -->
Team # 2516178

<!-- b002957 | furniture | pages [27] -->
Page 27 of 27

<!-- b002958 | ai_disclosure | pages [27] -->
Output:

<!-- b002959 | ai_disclosure | pages [27] -->
Key factors influencing Olympic results beyond training and coaching

<!-- b002960 | ai_disclosure | pages [27] -->
include:

<!-- b002961 | ai_disclosure | pages [27] -->
Home Advantage: Familiar venues, supportive crowds, and reduced

<!-- b002962 | ai_disclosure | pages [27] -->
travel fatigue.

<!-- b002963 | ai_disclosure | pages [27] -->
Environment: Climate, altitude, and weather conditions.

<!-- b002964 | ai_disclosure | pages [27] -->
Technology: Advanced equipment and resources.

<!-- b002965 | ai_disclosure | pages [27] -->
Health: Injury prevention and illness management.

<!-- b002966 | ai_disclosure | pages [27] -->
微信公众号：数学模型

<!-- b002967 | ai_disclosure | pages [27] -->
Mental Factors: Stress, focus, and handling pressure.

<!-- b002968 | ai_disclosure | pages [27] -->
Travel Impact: Jet lag and acclimatization.

<!-- b002969 | ai_disclosure | pages [27] -->
Economic Resources: Access to better facilities and support.

<!-- b002970 | ai_disclosure | pages [27] -->
Judging Bias: Subjective scoring in certain sports.

<!-- b002971 | ai_disclosure | pages [27] -->
Team Dynamics: Cohesion and morale.

<!-- b002972 | ai_disclosure | pages [27] -->
Unpredictable Events: Weather changes or equipment failure.

<!-- b002973 | ai_disclosure | pages [27] -->
These elements add complexity to Olympic success.

<!-- b002974 | ai_disclosure | pages [27] -->
微信号：MATHmodels

<!-- b002975 | ai_disclosure | pages [27] -->
m

<!-- b002976 | ai_disclosure | pages [27] -->
m

<!-- b002977 | ai_disclosure | pages [27] -->
m

<!-- b002978 | ai_disclosure | pages [27] -->
m

<!-- b002979 | ai_disclosure | pages [27] -->
m

<!-- b002980 | ai_disclosure | pages [27] -->
m

<!-- b002981 | ai_disclosure | pages [27] -->
m

<!-- b002982 | ai_disclosure | pages [27] -->
m

<!-- b002983 | ai_disclosure | pages [27] -->
m

<!-- b002984 | ai_disclosure | pages [27] -->
m

<!-- b002985 | ai_disclosure | pages [27] -->
m

<!-- b002986 | ai_disclosure | pages [27] -->
m

<!-- b002987 | ai_disclosure | pages [27] -->
m

<!-- b002988 | ai_disclosure | pages [27] -->
m

<!-- b002989 | ai_disclosure | pages [27] -->
m

<!-- b002990 | ai_disclosure | pages [27] -->
m

<!-- b002991 | ai_disclosure | pages [27] -->
m

<!-- b002992 | ai_disclosure | pages [27] -->
m

<!-- b002993 | ai_disclosure | pages [27] -->
m

<!-- b002994 | ai_disclosure | pages [27] -->
m

<!-- b002995 | ai_disclosure | pages [27] -->
m

<!-- b002996 | ai_disclosure | pages [27] -->
m

<!-- b002997 | ai_disclosure | pages [27] -->
m

<!-- b002998 | ai_disclosure | pages [27] -->
m

<!-- b002999 | ai_disclosure | pages [27] -->
m

<!-- b003000 | ai_disclosure | pages [27] -->
m

<!-- b003001 | ai_disclosure | pages [27] -->
m

<!-- b003002 | ai_disclosure | pages [27] -->
m

<!-- b003003 | ai_disclosure | pages [27] -->
m

<!-- b003004 | ai_disclosure | pages [27] -->
m

<!-- b003005 | ai_disclosure | pages [27] -->
m

<!-- b003006 | ai_disclosure | pages [27] -->
m

<!-- b003007 | ai_disclosure | pages [27] -->
m

<!-- b003008 | ai_disclosure | pages [27] -->
m

<!-- b003009 | ai_disclosure | pages [27] -->
m

<!-- b003010 | ai_disclosure | pages [27] -->
m

<!-- b003011 | ai_disclosure | pages [27] -->
m

<!-- b003012 | ai_disclosure | pages [27] -->
m

<!-- b003013 | ai_disclosure | pages [27] -->
m

<!-- b003014 | ai_disclosure | pages [27] -->
m

<!-- b003015 | ai_disclosure | pages [27] -->
m

<!-- b003016 | ai_disclosure | pages [27] -->
m

<!-- b003017 | ai_disclosure | pages [27] -->
m

<!-- b003018 | ai_disclosure | pages [27] -->
m

<!-- b003019 | ai_disclosure | pages [27] -->
m

<!-- b003020 | ai_disclosure | pages [27] -->
m

<!-- b003021 | ai_disclosure | pages [27] -->
m

<!-- b003022 | ai_disclosure | pages [27] -->
m

<!-- b003023 | ai_disclosure | pages [27] -->
m

<!-- b003024 | ai_disclosure | pages [27] -->
m

<!-- b003025 | ai_disclosure | pages [27] -->
m

<!-- b003026 | ai_disclosure | pages [27] -->
m

<!-- b003027 | ai_disclosure | pages [27] -->
m

<!-- b003028 | ai_disclosure | pages [27] -->
m

<!-- b003029 | ai_disclosure | pages [27] -->
m

<!-- b003030 | ai_disclosure | pages [27] -->
m

<!-- b003031 | ai_disclosure | pages [27] -->
m

<!-- b003032 | ai_disclosure | pages [27] -->
m

<!-- b003033 | ai_disclosure | pages [27] -->
m

<!-- b003034 | ai_disclosure | pages [27] -->
m

<!-- b003035 | ai_disclosure | pages [27] -->
m

<!-- b003036 | ai_disclosure | pages [27] -->
m

<!-- b003037 | ai_disclosure | pages [27] -->
m

<!-- b003038 | ai_disclosure | pages [27] -->
m

<!-- b003039 | ai_disclosure | pages [27] -->
m

<!-- b003040 | ai_disclosure | pages [27] -->
m

<!-- b003041 | ai_disclosure | pages [27] -->
m

<!-- b003042 | ai_disclosure | pages [27] -->
m

<!-- b003043 | ai_disclosure | pages [27] -->
m

<!-- b003044 | ai_disclosure | pages [27] -->
m

<!-- b003045 | ai_disclosure | pages [27] -->
m

<!-- b003046 | ai_disclosure | pages [27] -->
m

<!-- b003047 | ai_disclosure | pages [27] -->
m

<!-- b003048 | ai_disclosure | pages [27] -->
m

<!-- b003049 | ai_disclosure | pages [27] -->
m

<!-- b003050 | ai_disclosure | pages [27] -->
m

<!-- b003051 | ai_disclosure | pages [27] -->
m

<!-- b003052 | ai_disclosure | pages [27] -->
m

<!-- b003053 | ai_disclosure | pages [27] -->
m

<!-- b003054 | ai_disclosure | pages [27] -->
m

<!-- b003055 | ai_disclosure | pages [27] -->
m

<!-- b003056 | ai_disclosure | pages [27] -->
m

<!-- b003057 | ai_disclosure | pages [27] -->
m

<!-- b003058 | ai_disclosure | pages [27] -->
m

<!-- b003059 | ai_disclosure | pages [27] -->
m

<!-- b003060 | ai_disclosure | pages [27] -->
m

<!-- b003061 | ai_disclosure | pages [27] -->
m

<!-- b003062 | ai_disclosure | pages [27] -->
m

<!-- b003063 | ai_disclosure | pages [27] -->
m

<!-- b003064 | ai_disclosure | pages [27] -->
m

<!-- b003065 | ai_disclosure | pages [27] -->
m

<!-- b003066 | ai_disclosure | pages [27] -->
m

<!-- b003067 | ai_disclosure | pages [27] -->
m

<!-- b003068 | ai_disclosure | pages [27] -->
m

<!-- b003069 | ai_disclosure | pages [27] -->
m

<!-- b003070 | ai_disclosure | pages [27] -->
m

<!-- b003071 | ai_disclosure | pages [27] -->
m

<!-- b003072 | ai_disclosure | pages [27] -->
m

<!-- b003073 | ai_disclosure | pages [27] -->
m

<!-- b003074 | ai_disclosure | pages [27] -->
m

<!-- b003075 | ai_disclosure | pages [27] -->
m

<!-- b003076 | ai_disclosure | pages [27] -->
m

<!-- b003077 | ai_disclosure | pages [27] -->
m

<!-- b003078 | ai_disclosure | pages [27] -->
m

<!-- b003079 | ai_disclosure | pages [27] -->
m

<!-- b003080 | ai_disclosure | pages [27] -->
m

<!-- b003081 | ai_disclosure | pages [27] -->
m

<!-- b003082 | ai_disclosure | pages [27] -->
m

<!-- b003083 | ai_disclosure | pages [27] -->
m

<!-- b003084 | ai_disclosure | pages [27] -->
m

<!-- b003085 | ai_disclosure | pages [27] -->
m

<!-- b003086 | ai_disclosure | pages [27] -->
m

<!-- b003087 | ai_disclosure | pages [27] -->
m

<!-- b003088 | ai_disclosure | pages [27] -->
m

<!-- b003089 | ai_disclosure | pages [27] -->
m

<!-- b003090 | ai_disclosure | pages [27] -->
m

<!-- b003091 | ai_disclosure | pages [27] -->
m

<!-- b003092 | ai_disclosure | pages [27] -->
m

<!-- b003093 | ai_disclosure | pages [27] -->
m

<!-- b003094 | ai_disclosure | pages [27] -->
m

<!-- b003095 | ai_disclosure | pages [27] -->
m

<!-- b003096 | ai_disclosure | pages [27] -->
m

<!-- b003097 | ai_disclosure | pages [27] -->
m

<!-- b003098 | ai_disclosure | pages [27] -->
m

<!-- b003099 | ai_disclosure | pages [27] -->
m

<!-- b003100 | ai_disclosure | pages [27] -->
m

<!-- b003101 | ai_disclosure | pages [27] -->
m

<!-- b003102 | ai_disclosure | pages [27] -->
m

<!-- b003103 | ai_disclosure | pages [27] -->
m

<!-- b003104 | ai_disclosure | pages [27] -->
m

<!-- b003105 | ai_disclosure | pages [27] -->
m

<!-- b003106 | ai_disclosure | pages [27] -->
m

<!-- b003107 | ai_disclosure | pages [27] -->
m

<!-- b003108 | ai_disclosure | pages [27] -->
m

<!-- b003109 | ai_disclosure | pages [27] -->
m

<!-- b003110 | ai_disclosure | pages [27] -->
m

<!-- b003111 | ai_disclosure | pages [27] -->
m

<!-- b003112 | ai_disclosure | pages [27] -->
m

<!-- b003113 | ai_disclosure | pages [27] -->
m

<!-- b003114 | ai_disclosure | pages [27] -->
m

<!-- b003115 | ai_disclosure | pages [27] -->
m

<!-- b003116 | ai_disclosure | pages [27] -->
m

<!-- b003117 | ai_disclosure | pages [27] -->
m

<!-- b003118 | ai_disclosure | pages [27] -->
m

<!-- b003119 | ai_disclosure | pages [27] -->
m

<!-- b003120 | ai_disclosure | pages [27] -->
m

<!-- b003121 | ai_disclosure | pages [27] -->
m

<!-- b003122 | ai_disclosure | pages [27] -->
m

<!-- b003123 | ai_disclosure | pages [27] -->
m

<!-- b003124 | ai_disclosure | pages [27] -->
m

<!-- b003125 | ai_disclosure | pages [27] -->
m

<!-- b003126 | ai_disclosure | pages [27] -->
m

<!-- b003127 | ai_disclosure | pages [27] -->
m

<!-- b003128 | ai_disclosure | pages [27] -->
m

<!-- b003129 | ai_disclosure | pages [27] -->
m

<!-- b003130 | ai_disclosure | pages [27] -->
m

<!-- b003131 | ai_disclosure | pages [27] -->
m

<!-- b003132 | ai_disclosure | pages [27] -->
m

<!-- b003133 | ai_disclosure | pages [27] -->
m

<!-- b003134 | ai_disclosure | pages [27] -->
m

<!-- b003135 | ai_disclosure | pages [27] -->
m

<!-- b003136 | ai_disclosure | pages [27] -->
m

<!-- b003137 | ai_disclosure | pages [27] -->
m

<!-- b003138 | ai_disclosure | pages [27] -->
m

<!-- b003139 | ai_disclosure | pages [27] -->
m

<!-- b003140 | ai_disclosure | pages [27] -->
m

<!-- b003141 | ai_disclosure | pages [27] -->
m

<!-- b003142 | ai_disclosure | pages [27] -->
m

<!-- b003143 | ai_disclosure | pages [27] -->
m

<!-- b003144 | ai_disclosure | pages [27] -->
m

<!-- b003145 | ai_disclosure | pages [27] -->
m

<!-- b003146 | ai_disclosure | pages [27] -->
m

<!-- b003147 | ai_disclosure | pages [27] -->
m

<!-- b003148 | ai_disclosure | pages [27] -->
m

<!-- b003149 | ai_disclosure | pages [27] -->
m

<!-- b003150 | ai_disclosure | pages [27] -->
m

<!-- b003151 | ai_disclosure | pages [27] -->
m

<!-- b003152 | ai_disclosure | pages [27] -->
m

<!-- b003153 | ai_disclosure | pages [27] -->
m

<!-- b003154 | ai_disclosure | pages [27] -->
m

<!-- b003155 | ai_disclosure | pages [27] -->
m

<!-- b003156 | ai_disclosure | pages [27] -->
m

<!-- b003157 | ai_disclosure | pages [27] -->
m

<!-- b003158 | ai_disclosure | pages [27] -->
m

<!-- b003159 | ai_disclosure | pages [27] -->
m

<!-- b003160 | ai_disclosure | pages [27] -->
m

<!-- b003161 | ai_disclosure | pages [27] -->
m

<!-- b003162 | ai_disclosure | pages [27] -->
m

<!-- b003163 | ai_disclosure | pages [27] -->
m

<!-- b003164 | ai_disclosure | pages [27] -->
m

<!-- b003165 | ai_disclosure | pages [27] -->
m

<!-- b003166 | ai_disclosure | pages [27] -->
m

<!-- b003167 | ai_disclosure | pages [27] -->
m

<!-- b003168 | ai_disclosure | pages [27] -->
m

<!-- b003169 | ai_disclosure | pages [27] -->
m

<!-- b003170 | ai_disclosure | pages [27] -->
m

<!-- b003171 | ai_disclosure | pages [27] -->
m

<!-- b003172 | ai_disclosure | pages [27] -->
m

<!-- b003173 | ai_disclosure | pages [27] -->
m

<!-- b003174 | ai_disclosure | pages [27] -->
m

<!-- b003175 | ai_disclosure | pages [27] -->
m

<!-- b003176 | ai_disclosure | pages [27] -->
m

<!-- b003177 | ai_disclosure | pages [27] -->
m

<!-- b003178 | ai_disclosure | pages [27] -->
m

<!-- b003179 | ai_disclosure | pages [27] -->
m

<!-- b003180 | ai_disclosure | pages [27] -->
m

<!-- b003181 | ai_disclosure | pages [27] -->
m

<!-- b003182 | ai_disclosure | pages [27] -->
m

<!-- b003183 | ai_disclosure | pages [27] -->
m

<!-- b003184 | ai_disclosure | pages [27] -->
m

<!-- b003185 | ai_disclosure | pages [27] -->
m

<!-- b003186 | ai_disclosure | pages [27] -->
m

<!-- b003187 | ai_disclosure | pages [27] -->
m

<!-- b003188 | ai_disclosure | pages [27] -->
m

<!-- b003189 | ai_disclosure | pages [27] -->
m

<!-- b003190 | ai_disclosure | pages [27] -->
m

<!-- b003191 | ai_disclosure | pages [27] -->
m

<!-- b003192 | ai_disclosure | pages [27] -->
m

<!-- b003193 | ai_disclosure | pages [27] -->
m

<!-- b003194 | ai_disclosure | pages [27] -->
m

<!-- b003195 | ai_disclosure | pages [27] -->
m

<!-- b003196 | ai_disclosure | pages [27] -->
m

<!-- b003197 | ai_disclosure | pages [27] -->
m

<!-- b003198 | ai_disclosure | pages [27] -->
m

<!-- b003199 | ai_disclosure | pages [27] -->
m

<!-- b003200 | ai_disclosure | pages [27] -->
m

<!-- b003201 | ai_disclosure | pages [27] -->
m

<!-- b003202 | ai_disclosure | pages [27] -->
m

<!-- b003203 | ai_disclosure | pages [27] -->
m

<!-- b003204 | ai_disclosure | pages [27] -->
m

<!-- b003205 | furniture | pages [27] -->
m

<!-- b003206 | furniture | pages [27] -->
m

<!-- b003207 | furniture | pages [27] -->
m

<!-- b003208 | furniture | pages [27] -->
m

<!-- b003209 | furniture | pages [27] -->
m

<!-- b003210 | furniture | pages [27] -->
m

<!-- b003211 | furniture | pages [27] -->
m

<!-- b003212 | furniture | pages [27] -->
m

<!-- b003213 | furniture | pages [27] -->
m

<!-- b003214 | furniture | pages [27] -->
m

<!-- b003215 | furniture | pages [27] -->
m

<!-- b003216 | furniture | pages [27] -->
m

<!-- b003217 | furniture | pages [27] -->
m

<!-- b003218 | furniture | pages [27] -->
m

<!-- b003219 | furniture | pages [27] -->
m

<!-- b003220 | furniture | pages [27] -->
m

<!-- b003221 | furniture | pages [27] -->
m

<!-- b003222 | furniture | pages [27] -->
m

<!-- b003223 | furniture | pages [27] -->
m

<!-- b003224 | furniture | pages [27] -->
m

<!-- b003225 | furniture | pages [27] -->
m

<!-- b003226 | furniture | pages [27] -->
m

<!-- b003227 | furniture | pages [27] -->
m

<!-- b003228 | furniture | pages [27] -->
m

<!-- b003229 | furniture | pages [27] -->
m

<!-- b003230 | furniture | pages [27] -->
m

<!-- b003231 | furniture | pages [27] -->
m

<!-- b003232 | furniture | pages [27] -->
m

<!-- b003233 | furniture | pages [27] -->
m

<!-- b003234 | furniture | pages [27] -->
m

<!-- b003235 | furniture | pages [27] -->
m

<!-- b003236 | furniture | pages [27] -->
m

<!-- b003237 | furniture | pages [27] -->
m

<!-- b003238 | furniture | pages [27] -->
m

<!-- b003239 | furniture | pages [27] -->
m

<!-- b003240 | furniture | pages [27] -->
m

<!-- b003241 | furniture | pages [27] -->
m

<!-- b003242 | furniture | pages [27] -->
m

<!-- b003243 | furniture | pages [27] -->
m

<!-- b003244 | furniture | pages [27] -->
m

<!-- b003245 | furniture | pages [27] -->
m

<!-- b003246 | furniture | pages [27] -->
m

<!-- b003247 | furniture | pages [27] -->
m

<!-- b003248 | furniture | pages [27] -->
m

<!-- b003249 | furniture | pages [27] -->
m

<!-- b003250 | furniture | pages [27] -->
m

<!-- b003251 | furniture | pages [27] -->
m

<!-- b003252 | furniture | pages [27] -->
m

<!-- b003253 | furniture | pages [27] -->
m

<!-- b003254 | furniture | pages [27] -->
m

<!-- b003255 | furniture | pages [27] -->
m

<!-- b003256 | furniture | pages [27] -->
m

<!-- b003257 | furniture | pages [27] -->
m

<!-- b003258 | furniture | pages [27] -->
m

<!-- b003259 | furniture | pages [27] -->
m

<!-- b003260 | furniture | pages [27] -->
m

<!-- b003261 | furniture | pages [27] -->
m

<!-- b003262 | furniture | pages [27] -->
m

<!-- b003263 | furniture | pages [27] -->
m

<!-- b003264 | furniture | pages [27] -->
m

<!-- b003265 | furniture | pages [27] -->
m

<!-- b003266 | furniture | pages [27] -->
m

<!-- b003267 | furniture | pages [27] -->
m

<!-- b003268 | furniture | pages [27] -->
m

<!-- b003269 | furniture | pages [27] -->
m

<!-- b003270 | furniture | pages [27] -->
m

<!-- b003271 | furniture | pages [27] -->
m

<!-- b003272 | furniture | pages [27] -->
m

<!-- b003273 | furniture | pages [27] -->
m

<!-- b003274 | furniture | pages [27] -->
m

<!-- b003275 | furniture | pages [27] -->
m

<!-- b003276 | furniture | pages [27] -->
m

<!-- b003277 | furniture | pages [27] -->
m

<!-- b003278 | furniture | pages [27] -->
m

<!-- b003279 | furniture | pages [27] -->
m

<!-- b003280 | furniture | pages [27] -->
m

<!-- b003281 | furniture | pages [27] -->
m

<!-- b003282 | furniture | pages [27] -->
m

<!-- b003283 | furniture | pages [27] -->
m

<!-- b003284 | furniture | pages [27] -->
m

<!-- b003285 | furniture | pages [27] -->
m

<!-- b003286 | furniture | pages [27] -->
m

<!-- b003287 | furniture | pages [27] -->
m

<!-- b003288 | furniture | pages [27] -->
m

<!-- b003289 | furniture | pages [27] -->
m

<!-- b003290 | furniture | pages [27] -->
m

<!-- b003291 | furniture | pages [27] -->
m

<!-- b003292 | furniture | pages [27] -->
m

<!-- b003293 | furniture | pages [27] -->
m

<!-- b003294 | furniture | pages [27] -->
m

<!-- b003295 | furniture | pages [27] -->
m

<!-- b003296 | furniture | pages [27] -->
m

<!-- b003297 | furniture | pages [27] -->
m

<!-- b003298 | furniture | pages [27] -->
m

<!-- b003299 | furniture | pages [27] -->
m

<!-- b003300 | furniture | pages [27] -->
m

<!-- b003301 | furniture | pages [27] -->
m

<!-- b003302 | furniture | pages [27] -->
m

<!-- b003303 | furniture | pages [27] -->
m

<!-- b003304 | furniture | pages [27] -->
m

<!-- b003305 | furniture | pages [27] -->
m

<!-- b003306 | furniture | pages [27] -->
m

<!-- b003307 | furniture | pages [27] -->
m

<!-- b003308 | furniture | pages [27] -->
m

<!-- b003309 | furniture | pages [27] -->
m

<!-- b003310 | furniture | pages [27] -->
m

<!-- b003311 | furniture | pages [27] -->
m

<!-- b003312 | furniture | pages [27] -->
m

<!-- b003313 | furniture | pages [27] -->
m

<!-- b003314 | furniture | pages [27] -->
m

<!-- b003315 | furniture | pages [27] -->
m

<!-- b003316 | furniture | pages [27] -->
m

<!-- b003317 | furniture | pages [27] -->
m

<!-- b003318 | furniture | pages [27] -->
m

<!-- b003319 | furniture | pages [27] -->
m

<!-- b003320 | furniture | pages [27] -->
m

<!-- b003321 | furniture | pages [27] -->
m

<!-- b003322 | furniture | pages [27] -->
m

<!-- b003323 | furniture | pages [27] -->
m

<!-- b003324 | furniture | pages [27] -->
m

<!-- b003325 | furniture | pages [27] -->
m

<!-- b003326 | furniture | pages [27] -->
m

<!-- b003327 | furniture | pages [27] -->
m

<!-- b003328 | furniture | pages [27] -->
m

<!-- b003329 | furniture | pages [27] -->
m

<!-- b003330 | furniture | pages [27] -->
m

<!-- b003331 | furniture | pages [27] -->
m

<!-- b003332 | furniture | pages [27] -->
m

<!-- b003333 | furniture | pages [27] -->
m

<!-- b003334 | furniture | pages [27] -->
m

<!-- b003335 | furniture | pages [27] -->
m

<!-- b003336 | furniture | pages [27] -->
m

<!-- b003337 | furniture | pages [27] -->
m

<!-- b003338 | furniture | pages [27] -->
m

<!-- b003339 | furniture | pages [27] -->
m

<!-- b003340 | furniture | pages [27] -->
m

<!-- b003341 | furniture | pages [27] -->
m

<!-- b003342 | furniture | pages [27] -->
m

<!-- b003343 | furniture | pages [27] -->
m

<!-- b003344 | furniture | pages [27] -->
m

<!-- b003345 | furniture | pages [27] -->
m

<!-- b003346 | furniture | pages [27] -->
m

<!-- b003347 | furniture | pages [27] -->
m

<!-- b003348 | furniture | pages [27] -->
m

<!-- b003349 | furniture | pages [27] -->
m

<!-- b003350 | furniture | pages [27] -->
m

<!-- b003351 | furniture | pages [27] -->
m

<!-- b003352 | furniture | pages [27] -->
m

<!-- b003353 | furniture | pages [27] -->
m

<!-- b003354 | furniture | pages [27] -->
m

<!-- b003355 | furniture | pages [27] -->
m

<!-- b003356 | furniture | pages [27] -->
m

<!-- b003357 | furniture | pages [27] -->
m

<!-- b003358 | furniture | pages [27] -->
m

<!-- b003359 | furniture | pages [27] -->
m

<!-- b003360 | furniture | pages [27] -->
m

<!-- b003361 | furniture | pages [27] -->
m

<!-- b003362 | furniture | pages [27] -->
m

<!-- b003363 | furniture | pages [27] -->
m

<!-- b003364 | furniture | pages [27] -->
m

<!-- b003365 | furniture | pages [27] -->
m

<!-- b003366 | furniture | pages [27] -->
m

<!-- b003367 | furniture | pages [27] -->
m

<!-- b003368 | furniture | pages [27] -->
m

<!-- b003369 | furniture | pages [27] -->
m

<!-- b003370 | furniture | pages [27] -->
m

<!-- b003371 | furniture | pages [27] -->
m

<!-- b003372 | furniture | pages [27] -->
m

<!-- b003373 | furniture | pages [27] -->
m

<!-- b003374 | furniture | pages [27] -->
m

<!-- b003375 | furniture | pages [27] -->
m

<!-- b003376 | furniture | pages [27] -->
m

<!-- b003377 | furniture | pages [27] -->
m

<!-- b003378 | furniture | pages [27] -->
m

<!-- b003379 | furniture | pages [27] -->
m

<!-- b003380 | furniture | pages [27] -->
m

<!-- b003381 | furniture | pages [27] -->
m

<!-- b003382 | furniture | pages [27] -->
m

<!-- b003383 | furniture | pages [27] -->
m

<!-- b003384 | furniture | pages [27] -->
m

<!-- b003385 | furniture | pages [27] -->
m

<!-- b003386 | furniture | pages [27] -->
m

<!-- b003387 | furniture | pages [27] -->
m

<!-- b003388 | furniture | pages [27] -->
m

<!-- b003389 | furniture | pages [27] -->
m

<!-- b003390 | furniture | pages [27] -->
m

<!-- b003391 | furniture | pages [27] -->
m

<!-- b003392 | furniture | pages [27] -->
m

<!-- b003393 | furniture | pages [27] -->
m

<!-- b003394 | furniture | pages [27] -->
m

<!-- b003395 | furniture | pages [27] -->
m

<!-- b003396 | furniture | pages [27] -->
m

<!-- b003397 | furniture | pages [27] -->
m

<!-- b003398 | furniture | pages [27] -->
m

<!-- b003399 | furniture | pages [27] -->
m

<!-- b003400 | furniture | pages [27] -->
m

<!-- b003401 | furniture | pages [27] -->
m

<!-- b003402 | furniture | pages [27] -->
m

<!-- b003403 | furniture | pages [27] -->
m

<!-- b003404 | furniture | pages [27] -->
m

<!-- b003405 | furniture | pages [27] -->
m

<!-- b003406 | furniture | pages [27] -->
m

<!-- b003407 | furniture | pages [27] -->
m

<!-- b003408 | furniture | pages [27] -->
m

<!-- b003409 | furniture | pages [27] -->
m

<!-- b003410 | furniture | pages [27] -->
m

<!-- b003411 | furniture | pages [27] -->
m

<!-- b003412 | furniture | pages [27] -->
m

<!-- b003413 | furniture | pages [27] -->
m

<!-- b003414 | furniture | pages [27] -->
m

<!-- b003415 | furniture | pages [27] -->
m

<!-- b003416 | furniture | pages [27] -->
m

<!-- b003417 | furniture | pages [27] -->
m

<!-- b003418 | furniture | pages [27] -->
m

<!-- b003419 | furniture | pages [27] -->
m

<!-- b003420 | furniture | pages [27] -->
m

<!-- b003421 | furniture | pages [27] -->
m

<!-- b003422 | furniture | pages [27] -->
m

<!-- b003423 | furniture | pages [27] -->
m

<!-- b003424 | furniture | pages [27] -->
m

<!-- b003425 | furniture | pages [27] -->
m

<!-- b003426 | furniture | pages [27] -->
m

<!-- b003427 | furniture | pages [27] -->
m

<!-- b003428 | furniture | pages [27] -->
m

<!-- b003429 | furniture | pages [27] -->
m

<!-- b003430 | furniture | pages [27] -->
m

<!-- b003431 | furniture | pages [27] -->
m

<!-- b003432 | furniture | pages [27] -->
m

<!-- b003433 | furniture | pages [27] -->
m

<!-- b003434 | furniture | pages [27] -->
m

<!-- b003435 | furniture | pages [27] -->
m

<!-- b003436 | furniture | pages [27] -->
m

<!-- b003437 | furniture | pages [27] -->
m

<!-- b003438 | furniture | pages [27] -->
m

<!-- b003439 | furniture | pages [27] -->
m

<!-- b003440 | furniture | pages [27] -->
m

<!-- b003441 | furniture | pages [27] -->
m

<!-- b003442 | furniture | pages [27] -->
m

<!-- b003443 | furniture | pages [27] -->
m

<!-- b003444 | furniture | pages [27] -->
m

<!-- b003445 | furniture | pages [27] -->
m

<!-- b003446 | furniture | pages [27] -->
m

<!-- b003447 | furniture | pages [27] -->
m

<!-- b003448 | furniture | pages [27] -->
m

<!-- b003449 | furniture | pages [27] -->
m

<!-- b003450 | furniture | pages [27] -->
m

<!-- b003451 | furniture | pages [27] -->
m

<!-- b003452 | furniture | pages [27] -->
m

<!-- b003453 | furniture | pages [27] -->
m

<!-- b003454 | furniture | pages [27] -->
m

<!-- b003455 | furniture | pages [27] -->
m

<!-- b003456 | furniture | pages [27] -->
m

<!-- b003457 | furniture | pages [27] -->
m

<!-- b003458 | furniture | pages [27] -->
m

<!-- b003459 | furniture | pages [27] -->
m

<!-- b003460 | furniture | pages [27] -->
m

<!-- b003461 | furniture | pages [27] -->
m

<!-- b003462 | furniture | pages [27] -->
m

<!-- b003463 | furniture | pages [27] -->
m

<!-- b003464 | furniture | pages [27] -->
m

<!-- b003465 | furniture | pages [27] -->
m

<!-- b003466 | furniture | pages [27] -->
m

<!-- b003467 | furniture | pages [27] -->
m

<!-- b003468 | furniture | pages [27] -->
m

<!-- b003469 | furniture | pages [27] -->
m

<!-- b003470 | furniture | pages [27] -->
m

<!-- b003471 | furniture | pages [27] -->
m

<!-- b003472 | furniture | pages [27] -->
m

<!-- b003473 | furniture | pages [27] -->
m

<!-- b003474 | furniture | pages [27] -->
m

<!-- b003475 | furniture | pages [27] -->
m

<!-- b003476 | furniture | pages [27] -->
m

<!-- b003477 | furniture | pages [27] -->
m

<!-- b003478 | furniture | pages [27] -->
m

<!-- b003479 | furniture | pages [27] -->
m

<!-- b003480 | furniture | pages [27] -->
m

<!-- b003481 | furniture | pages [27] -->
m

<!-- b003482 | furniture | pages [27] -->
m

<!-- b003483 | furniture | pages [27] -->
m

<!-- b003484 | furniture | pages [27] -->
m

<!-- b003485 | furniture | pages [27] -->
m

<!-- b003486 | furniture | pages [27] -->
m

<!-- b003487 | furniture | pages [27] -->
m

<!-- b003488 | furniture | pages [27] -->
m

<!-- b003489 | furniture | pages [27] -->
m

<!-- b003490 | furniture | pages [27] -->
m

<!-- b003491 | furniture | pages [27] -->
m

<!-- b003492 | furniture | pages [27] -->
m

<!-- b003493 | furniture | pages [27] -->
m

<!-- b003494 | furniture | pages [27] -->
m

<!-- b003495 | furniture | pages [27] -->
m

<!-- b003496 | furniture | pages [27] -->
m

<!-- b003497 | furniture | pages [27] -->
m

<!-- b003498 | furniture | pages [27] -->
m

<!-- b003499 | furniture | pages [27] -->
m

<!-- b003500 | furniture | pages [27] -->
m

<!-- b003501 | furniture | pages [27] -->
m

<!-- b003502 | furniture | pages [27] -->
m

<!-- b003503 | furniture | pages [27] -->
m

<!-- b003504 | furniture | pages [27] -->
m

<!-- b003505 | furniture | pages [27] -->
m

<!-- b003506 | furniture | pages [27] -->
m

<!-- b003507 | furniture | pages [27] -->
m

<!-- b003508 | furniture | pages [27] -->
m

<!-- b003509 | furniture | pages [27] -->
m

<!-- b003510 | furniture | pages [27] -->
m

<!-- b003511 | furniture | pages [27] -->
m

<!-- b003512 | furniture | pages [27] -->
m

<!-- b003513 | furniture | pages [27] -->
m

<!-- b003514 | furniture | pages [27] -->
m

<!-- b003515 | furniture | pages [27] -->
m

<!-- b003516 | furniture | pages [27] -->
m

<!-- b003517 | furniture | pages [27] -->
m

<!-- b003518 | furniture | pages [27] -->
m

<!-- b003519 | furniture | pages [27] -->
m

<!-- b003520 | furniture | pages [27] -->
m

<!-- b003521 | furniture | pages [27] -->
m

<!-- b003522 | furniture | pages [27] -->
m

<!-- b003523 | furniture | pages [27] -->
m

<!-- b003524 | furniture | pages [27] -->
m

<!-- b003525 | furniture | pages [27] -->
m

<!-- b003526 | furniture | pages [27] -->
m

<!-- b003527 | furniture | pages [27] -->
m

<!-- b003528 | furniture | pages [27] -->
m
