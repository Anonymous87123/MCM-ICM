# P-C-2025-2510862-925774c8

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

<!-- b000006 | furniture | pages [1] -->
2510862

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
2028 Olympic Medal Predictions:

<!-- b000009 | title | pages [1] -->
微信公众号：数学模型

<!-- b000010 | title | pages [1] -->
Multi-Effect Analysis and Strategic Insights

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
The Olympic Games are a global event that unites nations in pursuit of excellence. This study develops a model to predict medal counts for the 2028 Los Angeles Olympics, identifies potential first-time medal-winning countries, analyzes the influence of different sports, and evaluates the "great coach effect."

<!-- b000013 | prose | pages [1] -->
In Task 1: We prepared the data by creating three key indicators: medal lag, host coun-

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
try effect, and participant count. These, combined with additional features, served as in- puts for a Stacking ensemble model, which outperformed individual algorithms with an R² of 0.88. Using linear interpolation, we estimated 2028 feature values and predicted the top three gold medal winners: the United States (56), China (33), and Australia (25). We also calculated 95% confidence intervals using the Bootstrap method. The findings suggest that the U.S., Australia, and France will improve, while China, Japan, and the Netherlands may decline.

<!-- b000016 | prose | pages [1] -->
In Task 2: To identify countries likely to win their first medals in 2028, we analyzed participation trends for non-medal-winning nations (1960–2024) and introduced a binary variable ("Olympic investment level") based on these trends. We also identified Athlet- ics, Taekwondo, and Wrestling as key breakthrough sports. The model predicted Mali, Sierra Leone, Honduras, Bolivia, and Gambia as the most likely to win their first medals, with prediction accuracies above 70%.

<!-- b000017 | prose | pages [1] -->
In Task 3: We calculated Pearson correlation coefficients and used a heatmap to ana- lyze the relationship between sports and medal counts. Athletics, Shooting, and Swim- ming showed strong correlations (above 0.6), significantly influencing medal growth. SHAP analysis revealed that for the U.S., Athletics and Rugby-related events contributed most to medal gains. The addition of flag football could further enhance U.S. perfor- mance.

<!-- b000018 | prose | pages [1] -->
In Task 4: To evaluate the "great coach effect," we examined medal trends for the U.S. women’s gymnastics team, focusing on coach Béla Károlyi. Using a PSM-DID model with 2000 as the intervention year, we estimated a 3.213 medal increase per Olympics, significant at the 2% level. K-Means clustering identified Spain, Japan, and Canada as na- tions with potential to benefit from hiring great coaches, with predicted medal increases of 4.32, 2.89, and 4.75, respectively.

<!-- b000019 | prose | pages [1] -->
Finally, 10-fold cross-validation confirmed the Stacking model’s stability, while bal- ance and sensitivity tests supported the robustness of the PSM-DID model. These find- ings demonstrate the reliability of our methods and provide valuable insights into medal predictions. We have shared these results with National Olympic Committees to assist their strategic planning for the 2028 Olympics.

<!-- b000020 | keywords | pages [1] -->
Keywords: Medal predictions ; Stacking ensemble ; SHAP analysis ; PSM-DID model

<!-- b000021 | furniture | pages [2] -->
Page 2 of 25

<!-- b000022 | furniture | pages [2] -->
Team # 2510862

<!-- b000023 | heading | pages [2] -->
Contents

<!-- b000024 | contents | pages [2] -->
模型

<!-- b000025 | heading | pages [2] -->
Introduction

<!-- b000026 | prose | pages [2] -->
3 1

<!-- b000027 | prose | pages [2] -->
Problem background. 3 1.1

<!-- b000028 | heading | pages [2] -->
Restatement of the problem

<!-- b000029 | prose | pages [2] -->
1.2 3 1.3 3 Our work .

<!-- b000030 | heading | pages [2] -->
Assumptions

<!-- b000031 | prose | pages [2] -->
4 2

<!-- b000032 | heading | pages [2] -->
Notations

<!-- b000033 | prose | pages [2] -->
5 3 Data Pre-processing 5 4 5 6 5.1

<!-- b000034 | heading | pages [2] -->
Develop a model for medal counts for each country

<!-- b000035 | prose | pages [2] -->
6 Prediction for the Olympics in 2028 . . 5.2 9 Projections for the medal table in the Los Angeles, Olympics in 2028 5.2.1 9 5.2.2 Include prediction intervals for all results. 10 5.2.3 11 Possible Countries to Improve or Decline Task 2: Multifaceted analysis for Predicting the Next "First-Medal" Winner 12 6 Task 3:Exploration of the Relationship Between Olympic Events and Medal Win 15 7 Explore the relationship between the events and how many medals countries 7.1 15 earn 16 7.2

<!-- b000036 | heading | pages [2] -->
7.3 Impact of Host Country's Event Selection on medal

<!-- b000037 | prose | pages [2] -->
18 Task 4: Analysis of the "Great Coach" Effect and Its Impact on Medals' Perfor- 8 _ 18 mance

<!-- b000038 | heading | pages [2] -->
8.1 The effect contributes to medal counts

<!-- b000039 | prose | pages [2] -->
18 8.2 3 Countries should consider investing "Great Coach" 22

<!-- b000040 | heading | pages [2] -->
Model Testing

<!-- b000041 | prose | pages [2] -->
23 9 9.1 Tests of the stacking model . . . . 23

<!-- b000042 | heading | pages [2] -->
9.2 Tests of the PSM-DID model .

<!-- b000043 | prose | pages [2] -->
24

<!-- b000044 | heading | pages [2] -->
10 Letter

<!-- b000045 | prose | pages [2] -->
25

<!-- b000046 | prose | pages [2] -->
信 微

<!-- b000047 | prose | pages [2] -->
关注数学模型

<!-- b000048 | furniture | pages [2] -->
获取更多资讯

<!-- b000049 | furniture | pages [3] -->
Team # 2510862

<!-- b000050 | furniture | pages [3] -->
Page 3 of 25

<!-- b000051 | heading | pages [3] -->
1 Introduction

<!-- b000052 | heading | pages [3] -->
1.1 Problem background

<!-- b000053 | prose | pages [3] -->
As one of the most influential sporting events in the world, the Olympic Games have always attracted attention and participation from all over the world. Since the first mod- 微信公众号：数学模型 ern Olympic Games in 1896, the Olympic medal table, especially the gold medal table, has become an important platform for countries to demonstrate their sports strength, national image and culture. In addition to the traditional sports strength, international political and socio-economic factors also affect the distribution of Olympic medals to dif- ferent degrees. The accelerating process of globalisation and inter-country cooperation and competition are shaping the landscape of the Olympic Games.

<!-- b000054 | prose | pages [3] -->
With the development of big data, artificial intelligence and other technologies, data- based analysis and prediction models have become a hot research topic in the field of sports. These technologies are not only capable of handling complex multi-dimensional 微信号：MATHmodels data, but also provide countries with a scientific basis for Olympic medal predictions through simulation and prediction. However, medal prediction is more than a simple analysis of data; it also needs to consider cultural, economic and social factors in the context of globalisation, which makes Olympic medal prediction an interdisciplinary and complex challenge.

<!-- b000055 | heading | pages [3] -->
1.2 Restatement of the problem

<!-- b000056 | prose | pages [3] -->
• Creating a model to predict the number of gold medals versus the total number of medals for each country and based on the model predicting the medal standings for the 2028 Summer Olympics in Los Angeles, USA as well as the prediction intervals and analysing whether certain countries are expected to improve or decline in their achievements in 2028 compared to 2024.

<!-- b000057 | prose | pages [3] -->
• To predict which countries that have not won medals are likely to make a break- through at the upcoming 2028 Olympic Games in Los Angeles and evaluate the predicted results.

<!-- b000058 | prose | pages [3] -->
• Analyse the number and type of Olympic events, explore the relationship between events and the number of medals won by each country, identify the events that have a significant impact on each country and analyse the impact of the events chosen by the host country on the outcome of the games.

<!-- b000059 | prose | pages [3] -->
• Analyse the impact of the ’Great Coach Effect’ on the number of medals won based on relevant data. Select three countries to analyse the sports in which they should invest in ’great coaches’ and analyse their potential impact.

<!-- b000060 | heading | pages [3] -->
1.3 Our work

<!-- b000061 | prose | pages [3] -->
The content is summarized in Figure 1 and organized as follows:

<!-- b000062 | prose | pages [3, 4] -->
Section 2 outlines the assumptions and rationale. Section 3 explains the study’s nota- tions. Section 4 details data preprocessing. Section 5 develops the Olympic medal predic- tion model. Section 6 analyzes the likelihood of first-time medalists. Section 7 examines m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the impact of sports on medal counts. Section 8 quantifies the "great coach effect." Section 9 tests the models, and Section 10 evaluates their strengths and weaknesses.

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

<!-- b000387 | furniture | pages [4] -->
Team # 2510862

<!-- b000388 | furniture | pages [4] -->
Page 4 of 25

<!-- b000390 | caption | pages [4] -->
Figure 1: Structure of our paper

<!-- b000391 | heading | pages [4] -->
2 Assumptions

<!-- b000392 | prose | pages [4] -->
1. Historically, the merging of different teams in a country has no significant effect on exploring a country’s Olympic strength.

<!-- b000393 | prose | pages [4] -->
The Olympic teams of some countries historically may have been divided into sub- teams, such as ’Argentina-1’, ’Argentina-2’, etc., especially in team events where there may have been multiple teams competing. We believe that combining the results of these different teams historically will not have an impact on analysing the overall strength of the country in the Olympic Games.

<!-- b000394 | prose | pages [4] -->
2. There is a correlation between the number of participants from a country in an event and the country’s investment in that event.

<!-- b000395 | prose | pages [4] -->
It is hypothesised that a higher number of participants from a country means that the country has invested more resources (e.g. training facilities, professional coaches, etc.) in the sport. An increase in the number of participants usually reflects the level of interest and importance the country attaches to the sport, and by increasing the participation of athletes, the country is likely to become more competitive in the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m sport and thus improve its chances of winning medals. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 3. Certain countries are likely to win Olympic medals for the first time in 2028, and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m sports that have historically had a high number of first-time winners from other m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m countries are also relatively more likely to win for the first time. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Based on past history, certain sports are typically more likely to be breakthroughs for

<!-- b000396 | prose | pages [4, 5] -->
关注数学模型 微信公众号：数学模型 first-time medal-winning countries, particularly among emerging or less competi- tive countries. These sports have lower thresholds, more opportunities to compete, and can offer potential winning opportunities for countries that have not historically won an Olympic medal. 4. The effects of coaching do not diminish or enhance over time, but rather are main- tained at a stable level that influences athletes’ performance over time.

<!-- b000397 | furniture | pages [4] -->
2

<!-- b000398 | furniture | pages [4] -->
MATHmodels

<!-- b000399 | furniture | pages [4] -->
获取更多资讯

<!-- b000400 | furniture | pages [5] -->
Team # 2510862

<!-- b000401 | furniture | pages [5] -->
Page 5 of 25

<!-- b000403 | prose | pages [5] -->
Specifically, we argue that the effects of coaching in terms of tactical instruction, technical enhancement, and psychological motivation will remain stable through- out an athlete’s career and have a sustained positive effect on his or her Olympic performance. This influence does not diminish as the athlete gains experience or 微信号：MATHmodels changes in competitive status. For example, a coach’s training methods and strate- gic philosophy can still have a positive impact on an athlete in the long term, despite changes in age or fitness.

<!-- b000404 | heading | pages [5] -->
3 Notations

<!-- b000405 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000406 | heading | pages [5] -->
Symbol

<!-- b000407 | prose | pages [5] -->
Description Features of the attribute xj The regularization term that penalizes model complexity Ω(f) Slack variables represent the allowed tolerance for each data point ξi The learned weights for each base learner αi Parameters to be estimated β Random error term ϵit Policy dummy variable ri

<!-- b000408 | heading | pages [5] -->
4 Data Pre-processing

<!-- b000409 | prose | pages [5] -->
• Step 1: Special Data Handling Firstly, we deal with data format inconsistencies. In the summerOly_athletes.csv file, there were duplicate event names in the Sports column (Cycling Road, Cycling Track; Cycling Road, Triathlon), which were merged into the larger category, and there were multiple teams from the same country in the Team column, which were correctly grouped together. For example: Argentina-1, Argentina-2, they have been correctly grouped together. In addition, the historical data for Russia (RUS) and Russia 2020 (ROC), even though Russia has already missed the 2024 Olympics for other reasons and may continue to miss the 2028 Olympics, is informative, so we merged them and kept their data, but they are not involved in the subsequent medal predictions.

<!-- b000410 | prose | pages [5, 6] -->
• Step 2: Mapping the ’Team’ column to ’NOC’ We mapped the ’Team’ column (containing the full name of the country) in the sum- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m merOly_athletes.csv file to the corresponding ’NOC’ (National Olympic Committee 3-letter code) to ensure that all participating teams matched their corresponding NOC codes, thus ensuring data consistency.

<!-- b000411 | furniture | pages [5] -->
m

<!-- b000412 | furniture | pages [5] -->
m

<!-- b000413 | furniture | pages [5] -->
m

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

<!-- b000735 | furniture | pages [6] -->
Team # 2510862

<!-- b000736 | furniture | pages [6] -->
Page 6 of 25

<!-- b000738 | prose | pages [6] -->
• Step 3: Feature Engineering In order to enhance the predictive power of the model, several new features were created, as shown below. These new features provide valuable insight into under- standing the impact of Olympic host country effects on medal performance.

<!-- b000739 | prose | pages [6] -->
Data Feature Engineering

<!-- b000740 | prose | pages [6] -->
Features

<!-- b000741 | prose | pages [6] -->
Lagged Features Related Host Country-Related Athlete-Related Features to Medal Performance Features

<!-- b000742 | prose | pages [6] -->
Athlete Count will next Male Athlete Female Athlete was previous Average Gold Average Total Medals Athlete is  host in Sports Count Count (Last 3 Olympics) (Last 3 Olympics) host host Count

<!-- b000743 | caption | pages [6] -->
Figure 2: Fearture Engineering

<!-- b000744 | prose | pages [6] -->
We input the number of entries from each country in different events as features into the model and can predict the number of medals more accurately than each event individually.

<!-- b000745 | prose | pages [6] -->
• Step 4: Data Merging and Final Adjustments In the final step, we merged the summerOly_athletes.csv, summerOly_hosts.csv, and summerOly_medal_counts.csv datasets. NOC and Year were used as key vari- ables to ensure that the data could be accurately linked. In the end, a complete dataset was obtained containing all relevant information about each Olympic event, athlete performance and medal results for each country.

<!-- b000746 | heading | pages [6] -->
5 Task 1: 2028 Olympics Medal Prediction Model

<!-- b000747 | heading | pages [6] -->
5.1 Develop a model for medal counts for each country

<!-- b000748 | prose | pages [6] -->
In order to predict the number of medals for each country at the 2028 Summer Olympics in Los Angeles, in particular the number of gold medals and the total number of medals, the first step is to construct a machine learning regression prediction model that can make predictions with full consideration of multiple features constructed in the preprocessing portion of the data and use multiple evaluation metrics to measure the accuracy and stability of the predictions. The second step is to obtain prediction intervals for medals through a sampling method, and the third step is to analyse the results to explore which countries are likely to improve or decline.

<!-- b000749 | prose | pages [6, 7] -->
关注数学模型 微信公众号：数学模型 ⋇Step 1: Principle of Stacking Stacking is an integrated learning approach that combines multiple base learners (LGBM, SVM, XGBoost, and RF) into a final prediction model. Each base learner is trained independently and their predictions are then fed as features into a meta- learner (logistic regression) to generate the final prediction. The core advantage of stacking is the ability to combine the strengths of different models to improve the overall prediction performance. The Olympic medal prediction problem faces mul- tiple challenges, including taking into account the historical performance of coun- tries, the impact of different events and disciplines, home country effects, and pos- sible future changes. 微信号：MATHmodels

<!-- b000750 | furniture | pages [6] -->
2

<!-- b000751 | furniture | pages [6] -->
MATHmodels

<!-- b000752 | furniture | pages [6] -->
获取更多资讯

<!-- b000753 | furniture | pages [7] -->
Team # 2510862

<!-- b000754 | furniture | pages [7] -->
Page 7 of 25

<!-- b000756 | caption | pages [7] -->
Figure 3: Principle of Stacking

<!-- b000757 | prose | pages [7] -->
In predicting the number of medals at the 2028 Olympics, the stacked approach al- lows us to integrate the unique strengths of each of the underlying models.LGBM, SVM, XGBoost, and RF are able to capture different patterns in the data, such as non-linear relationships, feature interactions, and variance, respectively. By com- bining the outputs of these models, the stacked approach provides more robust and accurate predictions that can effectively predict the total number of medals and gold medals for each country.

<!-- b000758 | heading | pages [7] -->
⋇Step 2: Base Models

<!-- b000759 | heading | pages [7] -->
1. LightGBM (LGBM)

<!-- b000760 | prose | pages [7, 8] -->
LightGBM is a gradient boosting algorithm based on decision trees. It gradually improves the predictive power of the model at each iteration step by constructing a series of decision trees, each one correcting the residuals of the previous one. Light- GBM is extremely efficient when dealing with large datasets and is fast to train. By splitting the tree model, it is able to identify complex interactions between different features (e.g. the relationship between host country and historical performance) and accurately predict the number of medals. The overall objective function is:Equation 1 X N (1) L(θ) = l(yi, byi) + Ω(f) i=1 Where: l(yi, byi) is the loss function, typically the Mean Squared Error (MSE) for re- gression problems. Ω(f) is the regularization term that penalizes model complexity m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m to avoid overfitting.

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

<!-- b000806 | furniture | pages [7] -->
m

<!-- b000807 | furniture | pages [7] -->
m

<!-- b000808 | furniture | pages [7] -->
m

<!-- b000809 | furniture | pages [7] -->
m

<!-- b000810 | furniture | pages [7] -->
m

<!-- b000811 | furniture | pages [7] -->
m

<!-- b000812 | furniture | pages [7] -->
m

<!-- b000813 | furniture | pages [7] -->
m

<!-- b000814 | furniture | pages [7] -->
m

<!-- b000815 | furniture | pages [7] -->
m

<!-- b000816 | furniture | pages [7] -->
m

<!-- b000817 | furniture | pages [7] -->
m

<!-- b000818 | furniture | pages [7] -->
m

<!-- b000819 | furniture | pages [7] -->
m

<!-- b000820 | furniture | pages [7] -->
m

<!-- b000821 | furniture | pages [7] -->
m

<!-- b000822 | furniture | pages [7] -->
m

<!-- b000823 | furniture | pages [7] -->
m

<!-- b000824 | furniture | pages [7] -->
m

<!-- b000825 | furniture | pages [7] -->
m

<!-- b000826 | furniture | pages [7] -->
m

<!-- b000827 | furniture | pages [7] -->
m

<!-- b000828 | furniture | pages [7] -->
m

<!-- b000829 | furniture | pages [7] -->
m

<!-- b000830 | furniture | pages [7] -->
m

<!-- b000831 | furniture | pages [7] -->
m

<!-- b000832 | furniture | pages [7] -->
m

<!-- b000833 | furniture | pages [7] -->
m

<!-- b000834 | furniture | pages [7] -->
m

<!-- b000835 | furniture | pages [7] -->
m

<!-- b000836 | furniture | pages [7] -->
m

<!-- b000837 | furniture | pages [7] -->
m

<!-- b000838 | furniture | pages [7] -->
m

<!-- b000839 | furniture | pages [7] -->
m

<!-- b000840 | furniture | pages [7] -->
m

<!-- b000841 | furniture | pages [7] -->
m

<!-- b000842 | furniture | pages [7] -->
m

<!-- b000843 | furniture | pages [7] -->
m

<!-- b000844 | furniture | pages [7] -->
m

<!-- b000845 | furniture | pages [7] -->
m

<!-- b000846 | furniture | pages [7] -->
m

<!-- b000847 | furniture | pages [7] -->
m

<!-- b000848 | furniture | pages [7] -->
m

<!-- b000849 | furniture | pages [7] -->
m

<!-- b000850 | furniture | pages [7] -->
m

<!-- b000851 | furniture | pages [7] -->
m

<!-- b000852 | furniture | pages [7] -->
m

<!-- b000853 | furniture | pages [7] -->
m

<!-- b000854 | furniture | pages [7] -->
m

<!-- b000855 | furniture | pages [7] -->
m

<!-- b000856 | furniture | pages [7] -->
m

<!-- b000857 | furniture | pages [7] -->
m

<!-- b000858 | furniture | pages [7] -->
m

<!-- b000859 | furniture | pages [7] -->
m

<!-- b000860 | furniture | pages [7] -->
m

<!-- b000861 | furniture | pages [7] -->
m

<!-- b000862 | furniture | pages [7] -->
m

<!-- b000863 | furniture | pages [7] -->
m

<!-- b000864 | furniture | pages [7] -->
m

<!-- b000865 | furniture | pages [7] -->
m

<!-- b000866 | furniture | pages [7] -->
m

<!-- b000867 | furniture | pages [7] -->
m

<!-- b000868 | furniture | pages [7] -->
m

<!-- b000869 | furniture | pages [7] -->
m

<!-- b000870 | furniture | pages [7] -->
m

<!-- b000871 | furniture | pages [7] -->
m

<!-- b000872 | furniture | pages [7] -->
m

<!-- b000873 | furniture | pages [7] -->
m

<!-- b000874 | furniture | pages [7] -->
m

<!-- b000875 | furniture | pages [7] -->
m

<!-- b000876 | furniture | pages [7] -->
m

<!-- b000877 | furniture | pages [7] -->
m

<!-- b000878 | furniture | pages [7] -->
m

<!-- b000879 | furniture | pages [7] -->
m

<!-- b000880 | furniture | pages [7] -->
m

<!-- b000881 | furniture | pages [7] -->
m

<!-- b000882 | furniture | pages [7] -->
m

<!-- b000883 | furniture | pages [7] -->
m

<!-- b000884 | furniture | pages [7] -->
m

<!-- b000885 | furniture | pages [7] -->
m

<!-- b000886 | furniture | pages [7] -->
m

<!-- b000887 | furniture | pages [7] -->
m

<!-- b000888 | furniture | pages [7] -->
m

<!-- b000889 | furniture | pages [7] -->
m

<!-- b000890 | furniture | pages [7] -->
m

<!-- b000891 | furniture | pages [7] -->
m

<!-- b000892 | furniture | pages [7] -->
m

<!-- b000893 | furniture | pages [7] -->
m

<!-- b000894 | furniture | pages [7] -->
m

<!-- b000895 | furniture | pages [7] -->
m

<!-- b000896 | furniture | pages [7] -->
m

<!-- b000897 | furniture | pages [7] -->
m

<!-- b000898 | furniture | pages [7] -->
m

<!-- b000899 | furniture | pages [7] -->
m

<!-- b000900 | furniture | pages [7] -->
m

<!-- b000901 | furniture | pages [7] -->
m

<!-- b000902 | furniture | pages [7] -->
m

<!-- b000903 | furniture | pages [7] -->
m

<!-- b000904 | furniture | pages [7] -->
m

<!-- b000905 | furniture | pages [7] -->
m

<!-- b000906 | furniture | pages [7] -->
m

<!-- b000907 | furniture | pages [7] -->
m

<!-- b000908 | furniture | pages [7] -->
m

<!-- b000909 | furniture | pages [7] -->
m

<!-- b000910 | furniture | pages [7] -->
m

<!-- b000911 | furniture | pages [7] -->
m

<!-- b000912 | furniture | pages [7] -->
m

<!-- b000913 | furniture | pages [7] -->
m

<!-- b000914 | furniture | pages [7] -->
m

<!-- b000915 | furniture | pages [7] -->
m

<!-- b000916 | furniture | pages [7] -->
m

<!-- b000917 | furniture | pages [7] -->
m

<!-- b000918 | furniture | pages [7] -->
m

<!-- b000919 | furniture | pages [7] -->
m

<!-- b000920 | furniture | pages [7] -->
m

<!-- b000921 | furniture | pages [7] -->
m

<!-- b000922 | furniture | pages [7] -->
m

<!-- b000923 | furniture | pages [7] -->
m

<!-- b000924 | furniture | pages [7] -->
m

<!-- b000925 | furniture | pages [7] -->
m

<!-- b000926 | furniture | pages [7] -->
m

<!-- b000927 | furniture | pages [7] -->
m

<!-- b000928 | furniture | pages [7] -->
m

<!-- b000929 | furniture | pages [7] -->
m

<!-- b000930 | furniture | pages [7] -->
m

<!-- b000931 | furniture | pages [7] -->
m

<!-- b000932 | furniture | pages [7] -->
m

<!-- b000933 | furniture | pages [7] -->
m

<!-- b000934 | furniture | pages [7] -->
m

<!-- b000935 | furniture | pages [7] -->
m

<!-- b000936 | furniture | pages [7] -->
m

<!-- b000937 | furniture | pages [7] -->
m

<!-- b000938 | furniture | pages [7] -->
m

<!-- b000939 | furniture | pages [7] -->
m

<!-- b000940 | furniture | pages [7] -->
m

<!-- b000941 | furniture | pages [7] -->
m

<!-- b000942 | furniture | pages [7] -->
m

<!-- b000943 | furniture | pages [7] -->
m

<!-- b000944 | furniture | pages [7] -->
m

<!-- b000945 | furniture | pages [7] -->
m

<!-- b000946 | furniture | pages [7] -->
m

<!-- b000947 | furniture | pages [7] -->
m

<!-- b000948 | furniture | pages [7] -->
m

<!-- b000949 | furniture | pages [7] -->
m

<!-- b000950 | furniture | pages [7] -->
m

<!-- b000951 | furniture | pages [7] -->
m

<!-- b000952 | furniture | pages [7] -->
m

<!-- b000953 | furniture | pages [7] -->
m

<!-- b000954 | furniture | pages [7] -->
m

<!-- b000955 | furniture | pages [7] -->
m

<!-- b000956 | furniture | pages [7] -->
m

<!-- b000957 | furniture | pages [7] -->
m

<!-- b000958 | furniture | pages [7] -->
m

<!-- b000959 | furniture | pages [7] -->
m

<!-- b000960 | furniture | pages [7] -->
m

<!-- b000961 | furniture | pages [7] -->
m

<!-- b000962 | furniture | pages [7] -->
m

<!-- b000963 | furniture | pages [7] -->
m

<!-- b000964 | furniture | pages [7] -->
m

<!-- b000965 | furniture | pages [7] -->
m

<!-- b000966 | furniture | pages [7] -->
m

<!-- b000967 | furniture | pages [7] -->
m

<!-- b000968 | furniture | pages [7] -->
m

<!-- b000969 | furniture | pages [7] -->
m

<!-- b000970 | furniture | pages [7] -->
m

<!-- b000971 | furniture | pages [7] -->
m

<!-- b000972 | furniture | pages [7] -->
m

<!-- b000973 | furniture | pages [7] -->
m

<!-- b000974 | furniture | pages [7] -->
m

<!-- b000975 | furniture | pages [7] -->
m

<!-- b000976 | furniture | pages [7] -->
m

<!-- b000977 | furniture | pages [7] -->
m

<!-- b000978 | furniture | pages [7] -->
m

<!-- b000979 | furniture | pages [7] -->
m

<!-- b000980 | furniture | pages [7] -->
m

<!-- b000981 | furniture | pages [7] -->
m

<!-- b000982 | furniture | pages [7] -->
m

<!-- b000983 | furniture | pages [7] -->
m

<!-- b000984 | furniture | pages [7] -->
m

<!-- b000985 | furniture | pages [7] -->
m

<!-- b000986 | furniture | pages [7] -->
m

<!-- b000987 | furniture | pages [7] -->
m

<!-- b000988 | furniture | pages [7] -->
m

<!-- b000989 | furniture | pages [7] -->
m

<!-- b000990 | furniture | pages [7] -->
m

<!-- b000991 | furniture | pages [7] -->
m

<!-- b000992 | furniture | pages [7] -->
m

<!-- b000993 | furniture | pages [7] -->
m

<!-- b000994 | furniture | pages [7] -->
m

<!-- b000995 | furniture | pages [7] -->
m

<!-- b000996 | furniture | pages [7] -->
m

<!-- b000997 | furniture | pages [7] -->
m

<!-- b000998 | furniture | pages [7] -->
m

<!-- b000999 | furniture | pages [7] -->
m

<!-- b001000 | furniture | pages [7] -->
m

<!-- b001001 | furniture | pages [7] -->
m

<!-- b001002 | furniture | pages [7] -->
m

<!-- b001003 | furniture | pages [7] -->
m

<!-- b001004 | furniture | pages [7] -->
m

<!-- b001005 | furniture | pages [7] -->
m

<!-- b001006 | furniture | pages [7] -->
m

<!-- b001007 | furniture | pages [7] -->
m

<!-- b001008 | furniture | pages [7] -->
m

<!-- b001009 | furniture | pages [7] -->
m

<!-- b001010 | furniture | pages [7] -->
m

<!-- b001011 | furniture | pages [7] -->
m

<!-- b001012 | furniture | pages [7] -->
m

<!-- b001013 | furniture | pages [7] -->
m

<!-- b001014 | furniture | pages [7] -->
m

<!-- b001015 | furniture | pages [7] -->
m

<!-- b001016 | furniture | pages [7] -->
m

<!-- b001017 | furniture | pages [7] -->
m

<!-- b001018 | furniture | pages [7] -->
m

<!-- b001019 | furniture | pages [7] -->
m

<!-- b001020 | furniture | pages [7] -->
m

<!-- b001021 | furniture | pages [7] -->
m

<!-- b001022 | furniture | pages [7] -->
m

<!-- b001023 | furniture | pages [7] -->
m

<!-- b001024 | furniture | pages [7] -->
m

<!-- b001025 | furniture | pages [7] -->
m

<!-- b001026 | furniture | pages [7] -->
m

<!-- b001027 | furniture | pages [7] -->
m

<!-- b001028 | furniture | pages [7] -->
m

<!-- b001029 | furniture | pages [7] -->
m

<!-- b001030 | furniture | pages [7] -->
m

<!-- b001031 | furniture | pages [7] -->
m

<!-- b001032 | furniture | pages [7] -->
m

<!-- b001033 | furniture | pages [7] -->
m

<!-- b001034 | furniture | pages [7] -->
m

<!-- b001035 | furniture | pages [7] -->
m

<!-- b001036 | furniture | pages [7] -->
m

<!-- b001037 | furniture | pages [7] -->
m

<!-- b001038 | furniture | pages [7] -->
m

<!-- b001039 | furniture | pages [7] -->
m

<!-- b001040 | furniture | pages [7] -->
m

<!-- b001041 | furniture | pages [7] -->
m

<!-- b001042 | furniture | pages [7] -->
m

<!-- b001043 | furniture | pages [7] -->
m

<!-- b001044 | furniture | pages [7] -->
m

<!-- b001045 | furniture | pages [7] -->
m

<!-- b001046 | furniture | pages [7] -->
m

<!-- b001047 | furniture | pages [7] -->
m

<!-- b001048 | furniture | pages [7] -->
m

<!-- b001049 | furniture | pages [7] -->
m

<!-- b001050 | furniture | pages [7] -->
m

<!-- b001051 | furniture | pages [7] -->
m

<!-- b001052 | furniture | pages [7] -->
m

<!-- b001053 | furniture | pages [7] -->
m

<!-- b001054 | furniture | pages [7] -->
m

<!-- b001055 | furniture | pages [7] -->
m

<!-- b001056 | furniture | pages [7] -->
m

<!-- b001057 | furniture | pages [7] -->
m

<!-- b001058 | furniture | pages [7] -->
m

<!-- b001059 | furniture | pages [7] -->
m

<!-- b001060 | furniture | pages [7] -->
m

<!-- b001061 | furniture | pages [7] -->
m

<!-- b001062 | furniture | pages [7] -->
m

<!-- b001063 | furniture | pages [7] -->
m

<!-- b001064 | furniture | pages [7] -->
m

<!-- b001065 | furniture | pages [7] -->
m

<!-- b001066 | furniture | pages [7] -->
m

<!-- b001067 | furniture | pages [7] -->
m

<!-- b001068 | furniture | pages [7] -->
m

<!-- b001069 | furniture | pages [7] -->
m

<!-- b001070 | furniture | pages [7] -->
m

<!-- b001071 | furniture | pages [7] -->
m

<!-- b001072 | furniture | pages [7] -->
m

<!-- b001073 | furniture | pages [7] -->
m

<!-- b001074 | furniture | pages [7] -->
m

<!-- b001075 | furniture | pages [7] -->
m

<!-- b001076 | furniture | pages [7] -->
m

<!-- b001077 | furniture | pages [7] -->
m

<!-- b001078 | furniture | pages [7] -->
m

<!-- b001079 | furniture | pages [7] -->
m

<!-- b001080 | furniture | pages [7] -->
m

<!-- b001081 | furniture | pages [7] -->
m

<!-- b001082 | furniture | pages [7] -->
m

<!-- b001083 | furniture | pages [7] -->
m

<!-- b001084 | furniture | pages [7] -->
m

<!-- b001085 | furniture | pages [8] -->
Team # 2510862

<!-- b001086 | furniture | pages [8] -->
Page 8 of 25

<!-- b001088 | prose | pages [8] -->
By minimising this objective function, LightGBM optimises the parameters of the decision tree to improve the accuracy of Olympic medal count predictions.

<!-- b001089 | heading | pages [8] -->
2. Support Vector Machine (SVM)

<!-- b001090 | prose | pages [8] -->
SVM maximises the spacing between different classes of data points by finding an optimal hyperplane.The strength of SVM lies in its ability to model complex pat- terns, especially when the data is highly non-linear and noisy. It is able to find an optimal decision boundary to distinguish between different predictive trends, espe- cially when dealing with features that have complex interactions, and it is effective in identifying which features (e.g., strength of a particular sport) have the greatest impact on medal counts.

<!-- b001091 | prose | pages [8] -->
The objective function of an SVM in regression is: Equation 2 X N L(w, b, ϵ) = 1 2|w|2 + C (2) ξi i=1 Where: w and b are the weights and bias of the hyperplane. ξi are the slack variables that represent the margin of tolerance for each data point. C is the regularization parameter that controls the trade-off between minimizing the error and maximizing the margin.

<!-- b001092 | prose | pages [8] -->
3.Extreme Gradient Boosting(XGBoost) Unlike traditional boosting algorithms, XGBoost introduces Hessian matrices, mak- ing it faster in convergence and improving prediction accuracy. It also introduces regularisation to control model complexity and prevent overfitting.XGBoost is able to model complex interactions between features and is particularly well suited to deal with the combined effects of multiple factors.

<!-- b001093 | prose | pages [8] -->
The objective function of XGBoost is: Equation 3 X X N T (3) |wj|2 L(θ) = l(yi, byi) + λ i=1 j=1 Where: λ is a regularization parameter that penalizes large values of the tree param- eters wj.

<!-- b001094 | heading | pages [8] -->
4. Random Forest (RF)

<!-- b001095 | prose | pages [8] -->
Random Forest is an integrated method that combines multiple decision trees trained on random subsets. By using Bagging strategy, it reduces variance, improves stabil- ity and avoids over-fitting. Since each tree is trained independently, Random Forest is able to handle multiple feature combinations, capturing complex patterns and potential feature associations in the data.

<!-- b001096 | heading | pages [8] -->
⋇Step 3: Final Stacking Model Integration

<!-- b001097 | prose | pages [8] -->
Ultimately, the stacked model combines the predictions of LGBM, SVM, XGBoost, and RF into one final prediction. The prediction results of each base model are weighted and combined by a logistic regression model.

<!-- b001098 | prose | pages [8] -->
The integration formula is:Equation 4 Equation 5

<!-- b001099 | prose | pages [8, 9] -->
关注数学模型 T ∑ ft(xi) f2(xi) = y VM (4) t 1 T 1T ∑ft(xi) f4(xi) = yRF ∑ft(xi) XGBoost f3(xi) = yx (5) t=1 t=1 The final prediction is a weighted sum of the base models' outputs:Equation 6 ¯i = α1f1(xi) + α2f2(xi) + α3f3(xi) + α4f4(xi) + β (6) Where: α1,α2,α3,α4 are the learned weights for each base learner, and β is the bias term. The meta-learner adjusts these weights during training to minimize the error and produce the most accurate prediction for the total medal count and gold medals for each country in the 2028 Olympic Games.

<!-- b001100 | furniture | pages [8] -->
2

<!-- b001101 | furniture | pages [8] -->
MATHmodels

<!-- b001102 | furniture | pages [8] -->
获取更多资讯

<!-- b001103 | furniture | pages [9] -->
Page 9 of 25

<!-- b001104 | furniture | pages [9] -->
Team # 2510862

<!-- b001106 | prose | pages [9] -->
●

<!-- b001107 | heading | pages [9] -->
5.2 Prediction for the Olympics in 2028

<!-- b001108 | prose | pages [9] -->
●

<!-- b001109 | prose | pages [9] -->
Projections for the medal table in the Los Angeles, Olympics in 2028 5.2.1

<!-- b001110 | prose | pages [9] -->
We have developed an Olympic medal prediction model capable of predicting the medal table for the 2028 Summer Olympics in Los Angeles. For the number of athletes per country in 2028 and the number of participants in each sport, we have used linear interpolation based on data from 2012 to 2024 to estimate the corresponding values for 2028. For other characteristic data (historical performance, host country effects), they were filled in as appropriate. For model training, we chose data from 1908 to 2000 as the training set and data from 2004 to 2024 as the test set. After the model training, inputting the feature data of 2028, we can get the medal prediction results as below.

<!-- b001111 | prose | pages [9] -->
V0 V V NOC Country Total Medal table CUB 11 Los Angeles Olympics ZZ8 3 4 4 10 ε ε KEN 4 O VO Country Total NOC 14 IRI 3 5 6 USA 56 133 41 36 JAM 10 3 5 2 30 90 CHN 33 27 NOR 13 3 6 4 25 AUS 20 28 73 POL 3 3 3 9 FRA 19 24 25 68 RSA 3 9 3 3 15 10 13 38 GER SWE 8 3 2 3 14 13 16 43 GBR UKR 3 2 4 9 JPN 11 14 36 11 UZB 8 3 2 3 16 37 ITA 10 11 CZE 2 3 8 3 KOR 25 10 9 6 AZE 3 8 2 3 BRA 22 7 9 9 BEL 7 2 2 3 CAN 25 11 7 7 BLR 2 2 2 6 NED 25 10 7 8 BUL 2 2 2 6 18 NZL 6 6 6 AUT 2 1 3 6 ESP 20 5 8 7 CRO 2 2 5 1 HUN 15 5 5 5

<!-- b001112 | caption | pages [9] -->
Figure 4: Prediction for medal table in 2028

<!-- b001113 | prose | pages [9, 10] -->
To further validate the performance of the model, the following assessment metrics were used: coefficient of determination (R²), mean square error (MSE) and mean abso- lute percentage error (MAPE). These metrics are able to assess the accuracy and predic- tive effectiveness of the model from different perspectives.Equation 7 Pn i=1(yi −byi)2 R2 = 1 − Pn (7) i=1(yi −y)2 R² can help us assess the overall fit of the model and understand whether the model explains the variance of the data.Equation 8 X n MSE = 1 (8) (yi −byi)2 n i=1 The MSE provides a quantitative assessment of the prediction error to help us under- stand the absolute magnitude of the prediction error.Equation 9 X n MAPE = 100 yi −byi (9) n yi i=1 MAPE, on the other hand, provides a standardised measure of error that is particu- larly suitable for making comparisons across countries and medal types, making it easy to assess the predictive effectiveness of the model on different countries.

<!-- b001114 | furniture | pages [10] -->
Team # 2510862

<!-- b001115 | furniture | pages [10] -->
Page 10 of 25

<!-- b001117 | prose | pages [10] -->
These three indicators combine the model fit, error size and error ratio, which help us to comprehensively assess the predictive effectiveness of the model from multiple dimen- sions. The calculation results are shown in Table:

<!-- b001118 | prose | pages [10] -->
LGBM SVM XGBOOST RF Stacking R2 0.78 0.73 0.86 0.84 0.88 MSE 0.53 0.62 0.37 0.39 0.32 MAPE 0.42 0.48 0.32 0.33 0.30

<!-- b001119 | caption | pages [10] -->
Figure 5: Model evaluation results

<!-- b001120 | prose | pages [10] -->
Overall, the Stacking model has the strongest fitting ability R² and the smallest MSE and MAPE prediction errors due to the integration of multiple base models, obtaining the most stable and accurate prediction results.

<!-- b001121 | prose | pages [10] -->
5.2.2 Include prediction intervals for all results.

<!-- b001122 | prose | pages [10] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m In Olympic medal prediction, the Bootstrap method quantifies the prediction error m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m through data resampling without the need to make assumptions, and is able to efficiently m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m estimate the distribution and uncertainty of the prediction results. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001123 | prose | pages [10] -->
• Step 1: Randomly draw n samples from the original dataset to generate a resampled m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m dataset X∗= {x∗ n}. m m m m m m m m m m m m m m m m m m 1, x∗ 2, ..., x∗ m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001124 | prose | pages [10] -->
• Step 2: Compute the statisticon bθ∗the resampled dataset.

<!-- b001125 | prose | pages [10] -->
• Step 3: Repeat the above process B times to obtain B statistics, bθ∗ B. θ∗ 1, ..., c

<!-- b001126 | prose | pages [10] -->
• Step 4: Estimate Standard Error and Confidence Interval. Based on the B resampling results, estimate the standard error (SE) and confidence interval for the statistic. As- suming bθ∗has a sample mean [ mean , the standard error is calculated as:Equation 10 θ∗ v u    2 u X B t 1 b −[ (10) θ∗ SE bθ = bθ∗ mean B b=1

<!-- b001127 | prose | pages [10, 11] -->
关注数学模型 For the confidence interval, if we want to calculate the 95% confidence interval, we can use the percentiles of the B statistics:   θ.0∗ θ∗ Lower bound = percentile 2.5%, bθ∗ 1, d 2, ..., c 微信公众号：数学模型 B   θ∗ Upper bound = percentile 97.5%, bθ∗ 1, bθ∗ 2, ..., c B

<!-- b001128 | furniture | pages [10] -->
2

<!-- b001129 | furniture | pages [10] -->
MATHmodels

<!-- b001130 | furniture | pages [10] -->
获取更多资讯

<!-- b001131 | furniture | pages [11] -->
Team # 2510862

<!-- b001132 | furniture | pages [11] -->
Page 11 of 25

<!-- b001134 | prose | pages [11] -->
微信号：MATHmodels

<!-- b001135 | caption | pages [11] -->
Figure 6: prediction intervals for medal counts

<!-- b001136 | heading | pages [11] -->
5.2.3 Possible Countries to Improve or Decline

<!-- b001137 | prose | pages [11] -->
Possible Countries to Improve:

<!-- b001138 | heading | pages [11] -->
1. United States (2024: 40 Golds, Predicted 2028: 56 Golds): As the host country for

<!-- b001139 | prose | pages [11] -->
the 2028 Los Angeles Olympics, the United States will benefit from the home advantage, which is expected to enhance its performance. Furthermore, the U.S. has consistently ranked among the top countries in terms of gold medals in past Olympics, with a strong pool of athletes. Therefore, it is expected that the U.S. will maintain its lead in 2028 and further increase its gold medal count.

<!-- b001140 | heading | pages [11] -->
2. Australia (2024: 18 Golds, Predicted 2028: 25 Golds): As the host country for the

<!-- b001141 | prose | pages [11] -->
2032 Olympics, Australia has been preparing extensively for future Games. A traditional sports powerhouse, Australia has already demonstrated strong performances across var- ious events. In 2028, Australia is expected to make significant progress, especially in swimming, rowing, and other aquatic sports, resulting in a likely increase in gold medals.

<!-- b001142 | heading | pages [11] -->
3. France (2024: 16 Golds, Predicted 2028: 19 Golds): Having successfully hosted the

<!-- b001143 | prose | pages [11] -->
2024 Paris Olympics, France has made significant improvements in athlete training and infrastructure. With a well-established athlete development system and solid training ex- perience, France’s preparations for 2024 are expected to positively impact its performance in the 2028 Los Angeles Olympics.

<!-- b001144 | prose | pages [11] -->
Possible Countries to Decline:

<!-- b001145 | prose | pages [11, 12] -->
1. China (2024: 40 Golds, Predicted 2028: 33 Golds): Although China has consistently performed strongly in the Olympics, its gold medal count is predicted to decrease slightly in 2028. With other countries, such as the U.S. and Australia, becoming more competitive, China may face increased challenges. The U.S. will have the home advantage in 2028, which could make it more difficult for China to dominate in key events.

<!-- b001146 | furniture | pages [12] -->
Team # 2510862

<!-- b001147 | furniture | pages [12] -->
Page 12 of 25

<!-- b001149 | heading | pages [12] -->
2. Japan (2024: 20 Golds, Predicted 2028: 14 Golds): Despite Japan’s impressive

<!-- b001150 | prose | pages [12] -->
performance in 2024, by 2028, it will have been eight years since the Tokyo Olympics. Over time, many of the athletes who won gold medals in Tokyo may have retired, and there is uncertainty about whether new athletes can quickly fill these gaps. Therefore, Japan is expected to see a decline in its gold medal count in 2028.

<!-- b001151 | heading | pages [12] -->
3. Netherlands (2024: 15 Golds, Predicted 2028: 7 Golds): The Netherlands ranked

<!-- b001152 | prose | pages [12] -->
6th in the gold medal tally in 2024, achieving outstanding results, likely aided by its prox- imity to Paris, which boosted athlete morale and fan support. However, with the 2028 Olympics being held in Los Angeles, far from Europe, several factors could affect the Dutch athletes’ preparation and performance. As a result, despite strong results in 2024, the Netherlands is expected to see a decrease in its gold medal count in 2028.

<!-- b001153 | heading | pages [12] -->
6 Task 2: Multifaceted analysis for Predicting the Next "First-

<!-- b001154 | prose | pages [12] -->
Medal" Winner Behind the medals at each Olympic Games is not only a representation of the strength of the country’s athletes, but also a reflection of the investment, nurturing and develop- ment of the Olympic Movement in each country. Based on the available historical data of the Olympic Games, there are many countries in the world that have long failed to win m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m medals, and their performance in the past few Olympic Games has often fallen short of m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m significant expectations. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001155 | caption | pages [12] -->
Figure 7: Countries that have never won a medal

<!-- b001156 | prose | pages [12] -->
With the continued efforts of the IOC and various national sports organisations, par- ticipation in Olympic sports in these countries is increasing year on year. As the Olympic Games become more popular around the world and resources are distributed more eq- uitably, it is still possible that in the future there will be a few ’dark horse’ countries that could win medals for the first time at future Olympic Games.

<!-- b001157 | prose | pages [12] -->
In order to predict which non-medal-winning countries are likely to make a break-

<!-- b001158 | prose | pages [12, 13] -->
关注数学模型 through at the upcoming 2028 Olympic Games in Los Angeles, we have conducted a multi-dimensional analysis of these countries, using data modelling methods to extract key characteristics to more accurately assess their potential for a first medal.

<!-- b001159 | furniture | pages [12] -->
2

<!-- b001160 | furniture | pages [12] -->
MATHmodels

<!-- b001161 | furniture | pages [12] -->
获取更多资讯

<!-- b001162 | furniture | pages [13] -->
Team # 2510862

<!-- b001163 | furniture | pages [13] -->
Page 13 of 25

<!-- b001165 | heading | pages [13] -->
1. Impact of changes in the number of participants

<!-- b001166 | prose | pages [13] -->
Firstly, we analysed the changes in the number of participants of the non-winning countries over the period 1960-2024. By looking at the trends in their participation num- bers over the past few Olympics, we are able to surmise their commitment and involve- ment in the Olympic Games. If a country’s participation numbers are increasing year on year, this tends to imply that the country is increasing its investment in the Olympic Movement, increasing the support it provides to its athletes, and in turn increasing its 微信公众号：数学模型 potential to win medals.

<!-- b001167 | prose | pages [13] -->
微信号：MATHmodels

<!-- b001168 | caption | pages [13] -->
Figure 8: Participant Trends for Non-Medal-Winning Countries (Top 28)

<!-- b001169 | prose | pages [13] -->
In an effort to quantify the changes in these countries’ inputs, we fitted a trend line to the change in the number of participants for each country. If the slope of the trend line is positive (The red fitted line in Figure 7) indicates an increase in participation, we labelled these countries as ’1’, indicating that their inputs are increasing, and ’0’, vice versa. This characteristic reflects whether countries have the potential to win medals at future Olympic Games.

<!-- b001170 | heading | pages [13] -->
2. Projects more likely to be first-time winners

<!-- b001171 | prose | pages [13, 14] -->
In addition to changes in the number of entries, another key factor is which projects are more likely to be ‘breakthroughs’ for first-time winners. By analysing the countries that have won first-time prizes in the period 2000-2024, as shown in Figures. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001172 | furniture | pages [13] -->
m

<!-- b001173 | furniture | pages [13] -->
m

<!-- b001174 | furniture | pages [13] -->
m

<!-- b001175 | furniture | pages [13] -->
m

<!-- b001176 | furniture | pages [13] -->
m

<!-- b001177 | furniture | pages [13] -->
m

<!-- b001178 | furniture | pages [13] -->
m

<!-- b001179 | furniture | pages [13] -->
m

<!-- b001180 | furniture | pages [13] -->
m

<!-- b001181 | furniture | pages [13] -->
m

<!-- b001182 | furniture | pages [13] -->
m

<!-- b001183 | furniture | pages [13] -->
m

<!-- b001184 | furniture | pages [13] -->
m

<!-- b001185 | furniture | pages [13] -->
m

<!-- b001186 | furniture | pages [13] -->
m

<!-- b001187 | furniture | pages [13] -->
m

<!-- b001188 | furniture | pages [13] -->
m

<!-- b001189 | furniture | pages [13] -->
m

<!-- b001190 | furniture | pages [13] -->
m

<!-- b001191 | furniture | pages [13] -->
m

<!-- b001192 | furniture | pages [13] -->
m

<!-- b001193 | furniture | pages [13] -->
m

<!-- b001194 | furniture | pages [13] -->
m

<!-- b001195 | furniture | pages [13] -->
m

<!-- b001196 | furniture | pages [13] -->
m

<!-- b001197 | furniture | pages [13] -->
m

<!-- b001198 | furniture | pages [13] -->
m

<!-- b001199 | furniture | pages [13] -->
m

<!-- b001200 | furniture | pages [13] -->
m

<!-- b001201 | furniture | pages [13] -->
m

<!-- b001202 | furniture | pages [13] -->
m

<!-- b001203 | furniture | pages [13] -->
m

<!-- b001204 | furniture | pages [13] -->
m

<!-- b001205 | furniture | pages [13] -->
m

<!-- b001206 | furniture | pages [13] -->
m

<!-- b001207 | furniture | pages [13] -->
m

<!-- b001208 | furniture | pages [13] -->
m

<!-- b001209 | furniture | pages [13] -->
m

<!-- b001210 | furniture | pages [13] -->
m

<!-- b001211 | furniture | pages [13] -->
m

<!-- b001212 | furniture | pages [13] -->
m

<!-- b001213 | furniture | pages [13] -->
m

<!-- b001214 | furniture | pages [13] -->
m

<!-- b001215 | furniture | pages [13] -->
m

<!-- b001216 | furniture | pages [13] -->
m

<!-- b001217 | furniture | pages [13] -->
m

<!-- b001218 | furniture | pages [13] -->
m

<!-- b001219 | furniture | pages [13] -->
m

<!-- b001220 | furniture | pages [13] -->
m

<!-- b001221 | furniture | pages [13] -->
m

<!-- b001222 | furniture | pages [13] -->
m

<!-- b001223 | furniture | pages [13] -->
m

<!-- b001224 | furniture | pages [13] -->
m

<!-- b001225 | furniture | pages [13] -->
m

<!-- b001226 | furniture | pages [13] -->
m

<!-- b001227 | furniture | pages [13] -->
m

<!-- b001228 | furniture | pages [13] -->
m

<!-- b001229 | furniture | pages [13] -->
m

<!-- b001230 | furniture | pages [13] -->
m

<!-- b001231 | furniture | pages [13] -->
m

<!-- b001232 | furniture | pages [13] -->
m

<!-- b001233 | furniture | pages [13] -->
m

<!-- b001234 | furniture | pages [13] -->
m

<!-- b001235 | furniture | pages [13] -->
m

<!-- b001236 | furniture | pages [13] -->
m

<!-- b001237 | furniture | pages [13] -->
m

<!-- b001238 | furniture | pages [13] -->
m

<!-- b001239 | furniture | pages [13] -->
m

<!-- b001240 | furniture | pages [13] -->
m

<!-- b001241 | furniture | pages [13] -->
m

<!-- b001242 | furniture | pages [13] -->
m

<!-- b001243 | furniture | pages [13] -->
m

<!-- b001244 | furniture | pages [13] -->
m

<!-- b001245 | furniture | pages [13] -->
m

<!-- b001246 | furniture | pages [13] -->
m

<!-- b001247 | furniture | pages [13] -->
m

<!-- b001248 | furniture | pages [13] -->
m

<!-- b001249 | furniture | pages [13] -->
m

<!-- b001250 | furniture | pages [13] -->
m

<!-- b001251 | furniture | pages [13] -->
m

<!-- b001252 | furniture | pages [13] -->
m

<!-- b001253 | furniture | pages [13] -->
m

<!-- b001254 | furniture | pages [13] -->
m

<!-- b001255 | furniture | pages [13] -->
m

<!-- b001256 | furniture | pages [13] -->
m

<!-- b001257 | furniture | pages [13] -->
m

<!-- b001258 | furniture | pages [13] -->
m

<!-- b001259 | furniture | pages [13] -->
m

<!-- b001260 | furniture | pages [13] -->
m

<!-- b001261 | furniture | pages [13] -->
m

<!-- b001262 | furniture | pages [13] -->
m

<!-- b001263 | furniture | pages [13] -->
m

<!-- b001264 | furniture | pages [13] -->
m

<!-- b001265 | furniture | pages [13] -->
m

<!-- b001266 | furniture | pages [13] -->
m

<!-- b001267 | furniture | pages [13] -->
m

<!-- b001268 | furniture | pages [13] -->
m

<!-- b001269 | furniture | pages [13] -->
m

<!-- b001270 | furniture | pages [13] -->
m

<!-- b001271 | furniture | pages [13] -->
m

<!-- b001272 | furniture | pages [13] -->
m

<!-- b001273 | furniture | pages [13] -->
m

<!-- b001274 | furniture | pages [13] -->
m

<!-- b001275 | furniture | pages [13] -->
m

<!-- b001276 | furniture | pages [13] -->
m

<!-- b001277 | furniture | pages [13] -->
m

<!-- b001278 | furniture | pages [13] -->
m

<!-- b001279 | furniture | pages [13] -->
m

<!-- b001280 | furniture | pages [13] -->
m

<!-- b001281 | furniture | pages [13] -->
m

<!-- b001282 | furniture | pages [13] -->
m

<!-- b001283 | furniture | pages [13] -->
m

<!-- b001284 | furniture | pages [13] -->
m

<!-- b001285 | furniture | pages [13] -->
m

<!-- b001286 | furniture | pages [13] -->
m

<!-- b001287 | furniture | pages [13] -->
m

<!-- b001288 | furniture | pages [13] -->
m

<!-- b001289 | furniture | pages [13] -->
m

<!-- b001290 | furniture | pages [13] -->
m

<!-- b001291 | furniture | pages [13] -->
m

<!-- b001292 | furniture | pages [13] -->
m

<!-- b001293 | furniture | pages [13] -->
m

<!-- b001294 | furniture | pages [13] -->
m

<!-- b001295 | furniture | pages [13] -->
m

<!-- b001296 | furniture | pages [13] -->
m

<!-- b001297 | furniture | pages [13] -->
m

<!-- b001298 | furniture | pages [13] -->
m

<!-- b001299 | furniture | pages [13] -->
m

<!-- b001300 | furniture | pages [13] -->
m

<!-- b001301 | furniture | pages [13] -->
m

<!-- b001302 | furniture | pages [13] -->
m

<!-- b001303 | furniture | pages [13] -->
m

<!-- b001304 | furniture | pages [13] -->
m

<!-- b001305 | furniture | pages [13] -->
m

<!-- b001306 | furniture | pages [13] -->
m

<!-- b001307 | furniture | pages [13] -->
m

<!-- b001308 | furniture | pages [13] -->
m

<!-- b001309 | furniture | pages [13] -->
m

<!-- b001310 | furniture | pages [13] -->
m

<!-- b001311 | furniture | pages [13] -->
m

<!-- b001312 | furniture | pages [13] -->
m

<!-- b001313 | furniture | pages [13] -->
m

<!-- b001314 | furniture | pages [13] -->
m

<!-- b001315 | furniture | pages [13] -->
m

<!-- b001316 | furniture | pages [13] -->
m

<!-- b001317 | furniture | pages [13] -->
m

<!-- b001318 | furniture | pages [13] -->
m

<!-- b001319 | furniture | pages [13] -->
m

<!-- b001320 | furniture | pages [13] -->
m

<!-- b001321 | furniture | pages [13] -->
m

<!-- b001322 | furniture | pages [13] -->
m

<!-- b001323 | furniture | pages [13] -->
m

<!-- b001324 | furniture | pages [13] -->
m

<!-- b001325 | furniture | pages [13] -->
m

<!-- b001326 | furniture | pages [13] -->
m

<!-- b001327 | furniture | pages [13] -->
m

<!-- b001328 | furniture | pages [13] -->
m

<!-- b001329 | furniture | pages [13] -->
m

<!-- b001330 | furniture | pages [13] -->
m

<!-- b001331 | furniture | pages [13] -->
m

<!-- b001332 | furniture | pages [13] -->
m

<!-- b001333 | furniture | pages [13] -->
m

<!-- b001334 | furniture | pages [13] -->
m

<!-- b001335 | furniture | pages [13] -->
m

<!-- b001336 | furniture | pages [13] -->
m

<!-- b001337 | furniture | pages [13] -->
m

<!-- b001338 | furniture | pages [13] -->
m

<!-- b001339 | furniture | pages [13] -->
m

<!-- b001340 | furniture | pages [13] -->
m

<!-- b001341 | furniture | pages [13] -->
m

<!-- b001342 | furniture | pages [13] -->
m

<!-- b001343 | furniture | pages [13] -->
m

<!-- b001344 | furniture | pages [13] -->
m

<!-- b001345 | furniture | pages [13] -->
m

<!-- b001346 | furniture | pages [13] -->
m

<!-- b001347 | furniture | pages [13] -->
m

<!-- b001348 | furniture | pages [13] -->
m

<!-- b001349 | furniture | pages [13] -->
m

<!-- b001350 | furniture | pages [13] -->
m

<!-- b001351 | furniture | pages [13] -->
m

<!-- b001352 | furniture | pages [13] -->
m

<!-- b001353 | furniture | pages [13] -->
m

<!-- b001354 | furniture | pages [13] -->
m

<!-- b001355 | furniture | pages [13] -->
m

<!-- b001356 | furniture | pages [13] -->
m

<!-- b001357 | furniture | pages [13] -->
m

<!-- b001358 | furniture | pages [13] -->
m

<!-- b001359 | furniture | pages [13] -->
m

<!-- b001360 | furniture | pages [13] -->
m

<!-- b001361 | furniture | pages [13] -->
m

<!-- b001362 | furniture | pages [13] -->
m

<!-- b001363 | furniture | pages [13] -->
m

<!-- b001364 | furniture | pages [13] -->
m

<!-- b001365 | furniture | pages [13] -->
m

<!-- b001366 | furniture | pages [13] -->
m

<!-- b001367 | furniture | pages [13] -->
m

<!-- b001368 | furniture | pages [13] -->
m

<!-- b001369 | furniture | pages [13] -->
m

<!-- b001370 | furniture | pages [13] -->
m

<!-- b001371 | furniture | pages [13] -->
m

<!-- b001372 | furniture | pages [13] -->
m

<!-- b001373 | furniture | pages [13] -->
m

<!-- b001374 | furniture | pages [13] -->
m

<!-- b001375 | furniture | pages [13] -->
m

<!-- b001376 | furniture | pages [13] -->
m

<!-- b001377 | furniture | pages [13] -->
m

<!-- b001378 | furniture | pages [13] -->
m

<!-- b001379 | furniture | pages [13] -->
m

<!-- b001380 | furniture | pages [13] -->
m

<!-- b001381 | furniture | pages [13] -->
m

<!-- b001382 | furniture | pages [13] -->
m

<!-- b001383 | furniture | pages [13] -->
m

<!-- b001384 | furniture | pages [13] -->
m

<!-- b001385 | furniture | pages [13] -->
m

<!-- b001386 | furniture | pages [13] -->
m

<!-- b001387 | furniture | pages [13] -->
m

<!-- b001388 | furniture | pages [13] -->
m

<!-- b001389 | furniture | pages [13] -->
m

<!-- b001390 | furniture | pages [13] -->
m

<!-- b001391 | furniture | pages [13] -->
m

<!-- b001392 | furniture | pages [13] -->
m

<!-- b001393 | furniture | pages [13] -->
m

<!-- b001394 | furniture | pages [13] -->
m

<!-- b001395 | furniture | pages [13] -->
m

<!-- b001396 | furniture | pages [13] -->
m

<!-- b001397 | furniture | pages [13] -->
m

<!-- b001398 | furniture | pages [13] -->
m

<!-- b001399 | furniture | pages [13] -->
m

<!-- b001400 | furniture | pages [13] -->
m

<!-- b001401 | furniture | pages [13] -->
m

<!-- b001402 | furniture | pages [13] -->
m

<!-- b001403 | furniture | pages [13] -->
m

<!-- b001404 | furniture | pages [13] -->
m

<!-- b001405 | furniture | pages [13] -->
m

<!-- b001406 | furniture | pages [13] -->
m

<!-- b001407 | furniture | pages [13] -->
m

<!-- b001408 | furniture | pages [13] -->
m

<!-- b001409 | furniture | pages [13] -->
m

<!-- b001410 | furniture | pages [13] -->
m

<!-- b001411 | furniture | pages [13] -->
m

<!-- b001412 | furniture | pages [13] -->
m

<!-- b001413 | furniture | pages [13] -->
m

<!-- b001414 | furniture | pages [13] -->
m

<!-- b001415 | furniture | pages [13] -->
m

<!-- b001416 | furniture | pages [13] -->
m

<!-- b001417 | furniture | pages [13] -->
m

<!-- b001418 | furniture | pages [13] -->
m

<!-- b001419 | furniture | pages [13] -->
m

<!-- b001420 | furniture | pages [13] -->
m

<!-- b001421 | furniture | pages [13] -->
m

<!-- b001422 | furniture | pages [13] -->
m

<!-- b001423 | furniture | pages [13] -->
m

<!-- b001424 | furniture | pages [13] -->
m

<!-- b001425 | furniture | pages [13] -->
m

<!-- b001426 | furniture | pages [13] -->
m

<!-- b001427 | furniture | pages [13] -->
m

<!-- b001428 | furniture | pages [13] -->
m

<!-- b001429 | furniture | pages [13] -->
m

<!-- b001430 | furniture | pages [13] -->
m

<!-- b001431 | furniture | pages [13] -->
m

<!-- b001432 | furniture | pages [13] -->
m

<!-- b001433 | furniture | pages [13] -->
m

<!-- b001434 | furniture | pages [13] -->
m

<!-- b001435 | furniture | pages [13] -->
m

<!-- b001436 | furniture | pages [13] -->
m

<!-- b001437 | furniture | pages [13] -->
m

<!-- b001438 | furniture | pages [13] -->
m

<!-- b001439 | furniture | pages [13] -->
m

<!-- b001440 | furniture | pages [13] -->
m

<!-- b001441 | furniture | pages [13] -->
m

<!-- b001442 | furniture | pages [13] -->
m

<!-- b001443 | furniture | pages [13] -->
m

<!-- b001444 | furniture | pages [13] -->
m

<!-- b001445 | furniture | pages [13] -->
m

<!-- b001446 | furniture | pages [13] -->
m

<!-- b001447 | furniture | pages [13] -->
m

<!-- b001448 | furniture | pages [13] -->
m

<!-- b001449 | furniture | pages [13] -->
m

<!-- b001450 | furniture | pages [13] -->
m

<!-- b001451 | furniture | pages [13] -->
m

<!-- b001452 | furniture | pages [13] -->
m

<!-- b001453 | furniture | pages [13] -->
m

<!-- b001454 | furniture | pages [13] -->
m

<!-- b001455 | furniture | pages [13] -->
m

<!-- b001456 | furniture | pages [13] -->
m

<!-- b001457 | furniture | pages [13] -->
m

<!-- b001458 | furniture | pages [13] -->
m

<!-- b001459 | furniture | pages [13] -->
m

<!-- b001460 | furniture | pages [13] -->
m

<!-- b001461 | furniture | pages [13] -->
m

<!-- b001462 | furniture | pages [13] -->
m

<!-- b001463 | furniture | pages [13] -->
m

<!-- b001464 | furniture | pages [13] -->
m

<!-- b001465 | furniture | pages [13] -->
m

<!-- b001466 | furniture | pages [13] -->
m

<!-- b001467 | furniture | pages [13] -->
m

<!-- b001468 | furniture | pages [13] -->
m

<!-- b001469 | furniture | pages [13] -->
m

<!-- b001470 | furniture | pages [13] -->
m

<!-- b001471 | furniture | pages [13] -->
m

<!-- b001472 | furniture | pages [13] -->
m

<!-- b001473 | furniture | pages [13] -->
m

<!-- b001474 | furniture | pages [13] -->
m

<!-- b001475 | furniture | pages [13] -->
m

<!-- b001476 | furniture | pages [13] -->
m

<!-- b001477 | furniture | pages [13] -->
m

<!-- b001478 | furniture | pages [13] -->
m

<!-- b001479 | furniture | pages [13] -->
m

<!-- b001480 | furniture | pages [13] -->
m

<!-- b001481 | furniture | pages [13] -->
m

<!-- b001482 | furniture | pages [13] -->
m

<!-- b001483 | furniture | pages [13] -->
m

<!-- b001484 | furniture | pages [13] -->
m

<!-- b001485 | furniture | pages [13] -->
m

<!-- b001486 | furniture | pages [13] -->
m

<!-- b001487 | furniture | pages [13] -->
m

<!-- b001488 | furniture | pages [13] -->
m

<!-- b001489 | furniture | pages [13] -->
m

<!-- b001490 | furniture | pages [13] -->
m

<!-- b001491 | furniture | pages [13] -->
m

<!-- b001492 | furniture | pages [13] -->
m

<!-- b001493 | furniture | pages [13] -->
m

<!-- b001494 | furniture | pages [13] -->
m

<!-- b001495 | furniture | pages [13] -->
m

<!-- b001496 | furniture | pages [14] -->
Team # 2510862

<!-- b001497 | furniture | pages [14] -->
Page 14 of 25

<!-- b001499 | caption | pages [14] -->
Figure 9: Relationship Between Sports and Countries Winning First Medals

<!-- b001500 | prose | pages [14] -->
We found that certain sports such as Athletics, Taekwondo and Wrestling are more likely to be breakthrough areas for these countries. These disciplines typically have lower barriers to entry and a wider participation base than other traditional strengths, providing more opportunities for those countries that did not win.

<!-- b001501 | prose | pages [14] -->
Therefore, in our model, we assign higher weights to these projects to better reflect the importance of these projects among first-time award-winning countries. Such weighting assignments help our prediction model to capture the potential of these projects more accurately, thus improving the accuracy of the predictions.

<!-- b001502 | heading | pages [14] -->
3. Integrated prediction in conjunction with the Stacking model

<!-- b001503 | prose | pages [14] -->
Combining the above two features, we introduced them into the Stacking model in the previous section. We have combined the trends in the number of entries from each coun- try, the weighting of the events and the historical medal data in our model to produce the following predictions.

<!-- b001504 | prose | pages [14] -->
Based on the predictions of the Stacking model, the following five countries are con- sidered to be the most likely to win medals for the first time at the 2028 Olympics:

<!-- b001505 | caption | pages [14] -->
Figure 10: Countries Likely to Win Their First Medal in 2028 and Probabilities

<!-- b001506 | prose | pages [14] -->
关注数学模型

<!-- b001507 | furniture | pages [14] -->
2

<!-- b001508 | furniture | pages [14] -->
MATHmodels

<!-- b001509 | furniture | pages [14] -->
获取更多资讯

<!-- b001510 | furniture | pages [15] -->
Team # 2510862

<!-- b001511 | furniture | pages [15] -->
Page 15 of 25

<!-- b001512 | heading | pages [15] -->
7 Task 3:Exploration of the Relationship Between Olympic

<!-- b001513 | prose | pages [15] -->
Events and Medal Wins In the Olympic medal prediction model, the number and type of events is one of the key factors affecting medal allocation. We believe that the number of participants of a country in a particular event can better reflect the predictive power of that event on the number of medals won by that country, and the number of participants of each country in 微信公众号：数学模型 different events has been input into the model as a substitute for the number of events in the previous section. In order to further explore the relationship between the medals won by the events and the countries, a correlation between the number of entries in different events and the number of medals has been analysed. Finally, using the SHAP method- ology, it was possible to explain the importance of individual features of the model in predicting outcomes and to analyse which events had the greatest impact on the number of medals won by each country.

<!-- b001514 | heading | pages [15] -->
7.1 Explore the relationship between the events and how many medals

<!-- b001515 | prose | pages [15] -->
countries earn 微信号：MATHmodels We consider the number of participants from all countries in each event as the char- acteristics and the number of gold, silver, bronze and total medals as the target vari- ables. The Pearson Correlation Coefficient enables us to calculate the linear correlation between the number of participants and the number of medals, and then to determine which events are most closely related to the number of medals, and which events have a lesser impact on the distribution of medals.

<!-- b001516 | caption | pages [15] -->
Figure 11: Correlation Coefficients Between Different Sports and Medal Counts

<!-- b001517 | prose | pages [15, 16] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The Pearson Correlation Coefficient is a statistic that measures the strength and di- rection of the linear relationship between two variables, taking values from -1 to 1. Its formula is:Equation 11

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

<!-- b001524 | furniture | pages [15] -->
m

<!-- b001525 | furniture | pages [15] -->
m

<!-- b001526 | furniture | pages [15] -->
m

<!-- b001527 | furniture | pages [15] -->
m

<!-- b001528 | furniture | pages [15] -->
m

<!-- b001529 | furniture | pages [15] -->
m

<!-- b001530 | furniture | pages [15] -->
m

<!-- b001531 | furniture | pages [15] -->
m

<!-- b001532 | furniture | pages [15] -->
m

<!-- b001533 | furniture | pages [15] -->
m

<!-- b001534 | furniture | pages [15] -->
m

<!-- b001535 | furniture | pages [15] -->
m

<!-- b001536 | furniture | pages [15] -->
m

<!-- b001537 | furniture | pages [15] -->
m

<!-- b001538 | furniture | pages [15] -->
m

<!-- b001539 | furniture | pages [15] -->
m

<!-- b001540 | furniture | pages [15] -->
m

<!-- b001541 | furniture | pages [15] -->
m

<!-- b001542 | furniture | pages [15] -->
m

<!-- b001543 | furniture | pages [15] -->
m

<!-- b001544 | furniture | pages [15] -->
m

<!-- b001545 | furniture | pages [15] -->
m

<!-- b001546 | furniture | pages [15] -->
m

<!-- b001547 | furniture | pages [15] -->
m

<!-- b001548 | furniture | pages [15] -->
m

<!-- b001549 | furniture | pages [15] -->
m

<!-- b001550 | furniture | pages [15] -->
m

<!-- b001551 | furniture | pages [15] -->
m

<!-- b001552 | furniture | pages [15] -->
m

<!-- b001553 | furniture | pages [15] -->
m

<!-- b001554 | furniture | pages [15] -->
m

<!-- b001555 | furniture | pages [15] -->
m

<!-- b001556 | furniture | pages [15] -->
m

<!-- b001557 | furniture | pages [15] -->
m

<!-- b001558 | furniture | pages [15] -->
m

<!-- b001559 | furniture | pages [15] -->
m

<!-- b001560 | furniture | pages [15] -->
m

<!-- b001561 | furniture | pages [15] -->
m

<!-- b001562 | furniture | pages [15] -->
m

<!-- b001563 | furniture | pages [15] -->
m

<!-- b001564 | furniture | pages [15] -->
m

<!-- b001565 | furniture | pages [15] -->
m

<!-- b001566 | furniture | pages [15] -->
m

<!-- b001567 | furniture | pages [15] -->
m

<!-- b001568 | furniture | pages [15] -->
m

<!-- b001569 | furniture | pages [15] -->
m

<!-- b001570 | furniture | pages [15] -->
m

<!-- b001571 | furniture | pages [15] -->
m

<!-- b001572 | furniture | pages [15] -->
m

<!-- b001573 | furniture | pages [15] -->
m

<!-- b001574 | furniture | pages [15] -->
m

<!-- b001575 | furniture | pages [15] -->
m

<!-- b001576 | furniture | pages [15] -->
m

<!-- b001577 | furniture | pages [15] -->
m

<!-- b001578 | furniture | pages [15] -->
m

<!-- b001579 | furniture | pages [15] -->
m

<!-- b001580 | furniture | pages [15] -->
m

<!-- b001581 | furniture | pages [15] -->
m

<!-- b001582 | furniture | pages [15] -->
m

<!-- b001583 | furniture | pages [15] -->
m

<!-- b001584 | furniture | pages [15] -->
m

<!-- b001585 | furniture | pages [15] -->
m

<!-- b001586 | furniture | pages [15] -->
m

<!-- b001587 | furniture | pages [15] -->
m

<!-- b001588 | furniture | pages [15] -->
m

<!-- b001589 | furniture | pages [15] -->
m

<!-- b001590 | furniture | pages [15] -->
m

<!-- b001591 | furniture | pages [15] -->
m

<!-- b001592 | furniture | pages [15] -->
m

<!-- b001593 | furniture | pages [15] -->
m

<!-- b001594 | furniture | pages [15] -->
m

<!-- b001595 | furniture | pages [15] -->
m

<!-- b001596 | furniture | pages [15] -->
m

<!-- b001597 | furniture | pages [15] -->
m

<!-- b001598 | furniture | pages [15] -->
m

<!-- b001599 | furniture | pages [15] -->
m

<!-- b001600 | furniture | pages [15] -->
m

<!-- b001601 | furniture | pages [15] -->
m

<!-- b001602 | furniture | pages [15] -->
m

<!-- b001603 | furniture | pages [15] -->
m

<!-- b001604 | furniture | pages [15] -->
m

<!-- b001605 | furniture | pages [15] -->
m

<!-- b001606 | furniture | pages [15] -->
m

<!-- b001607 | furniture | pages [15] -->
m

<!-- b001608 | furniture | pages [15] -->
m

<!-- b001609 | furniture | pages [15] -->
m

<!-- b001610 | furniture | pages [15] -->
m

<!-- b001611 | furniture | pages [15] -->
m

<!-- b001612 | furniture | pages [15] -->
m

<!-- b001613 | furniture | pages [15] -->
m

<!-- b001614 | furniture | pages [15] -->
m

<!-- b001615 | furniture | pages [15] -->
m

<!-- b001616 | furniture | pages [15] -->
m

<!-- b001617 | furniture | pages [15] -->
m

<!-- b001618 | furniture | pages [15] -->
m

<!-- b001619 | furniture | pages [15] -->
m

<!-- b001620 | furniture | pages [15] -->
m

<!-- b001621 | furniture | pages [15] -->
m

<!-- b001622 | furniture | pages [15] -->
m

<!-- b001623 | furniture | pages [15] -->
m

<!-- b001624 | furniture | pages [15] -->
m

<!-- b001625 | furniture | pages [15] -->
m

<!-- b001626 | furniture | pages [15] -->
m

<!-- b001627 | furniture | pages [15] -->
m

<!-- b001628 | furniture | pages [15] -->
m

<!-- b001629 | furniture | pages [15] -->
m

<!-- b001630 | furniture | pages [15] -->
m

<!-- b001631 | furniture | pages [15] -->
m

<!-- b001632 | furniture | pages [15] -->
m

<!-- b001633 | furniture | pages [15] -->
m

<!-- b001634 | furniture | pages [15] -->
m

<!-- b001635 | furniture | pages [15] -->
m

<!-- b001636 | furniture | pages [15] -->
m

<!-- b001637 | furniture | pages [15] -->
m

<!-- b001638 | furniture | pages [15] -->
m

<!-- b001639 | furniture | pages [15] -->
m

<!-- b001640 | furniture | pages [15] -->
m

<!-- b001641 | furniture | pages [15] -->
m

<!-- b001642 | furniture | pages [15] -->
m

<!-- b001643 | furniture | pages [15] -->
m

<!-- b001644 | furniture | pages [15] -->
m

<!-- b001645 | furniture | pages [15] -->
m

<!-- b001646 | furniture | pages [15] -->
m

<!-- b001647 | furniture | pages [15] -->
m

<!-- b001648 | furniture | pages [15] -->
m

<!-- b001649 | furniture | pages [15] -->
m

<!-- b001650 | furniture | pages [15] -->
m

<!-- b001651 | furniture | pages [15] -->
m

<!-- b001652 | furniture | pages [15] -->
m

<!-- b001653 | furniture | pages [15] -->
m

<!-- b001654 | furniture | pages [15] -->
m

<!-- b001655 | furniture | pages [15] -->
m

<!-- b001656 | furniture | pages [15] -->
m

<!-- b001657 | furniture | pages [15] -->
m

<!-- b001658 | furniture | pages [15] -->
m

<!-- b001659 | furniture | pages [15] -->
m

<!-- b001660 | furniture | pages [15] -->
m

<!-- b001661 | furniture | pages [15] -->
m

<!-- b001662 | furniture | pages [15] -->
m

<!-- b001663 | furniture | pages [15] -->
m

<!-- b001664 | furniture | pages [15] -->
m

<!-- b001665 | furniture | pages [15] -->
m

<!-- b001666 | furniture | pages [15] -->
m

<!-- b001667 | furniture | pages [15] -->
m

<!-- b001668 | furniture | pages [15] -->
m

<!-- b001669 | furniture | pages [15] -->
m

<!-- b001670 | furniture | pages [15] -->
m

<!-- b001671 | furniture | pages [15] -->
m

<!-- b001672 | furniture | pages [15] -->
m

<!-- b001673 | furniture | pages [15] -->
m

<!-- b001674 | furniture | pages [15] -->
m

<!-- b001675 | furniture | pages [15] -->
m

<!-- b001676 | furniture | pages [15] -->
m

<!-- b001677 | furniture | pages [15] -->
m

<!-- b001678 | furniture | pages [15] -->
m

<!-- b001679 | furniture | pages [15] -->
m

<!-- b001680 | furniture | pages [15] -->
m

<!-- b001681 | furniture | pages [15] -->
m

<!-- b001682 | furniture | pages [15] -->
m

<!-- b001683 | furniture | pages [15] -->
m

<!-- b001684 | furniture | pages [15] -->
m

<!-- b001685 | furniture | pages [15] -->
m

<!-- b001686 | furniture | pages [15] -->
m

<!-- b001687 | furniture | pages [15] -->
m

<!-- b001688 | furniture | pages [15] -->
m

<!-- b001689 | furniture | pages [15] -->
m

<!-- b001690 | furniture | pages [15] -->
m

<!-- b001691 | furniture | pages [15] -->
m

<!-- b001692 | furniture | pages [15] -->
m

<!-- b001693 | furniture | pages [15] -->
m

<!-- b001694 | furniture | pages [15] -->
m

<!-- b001695 | furniture | pages [15] -->
m

<!-- b001696 | furniture | pages [15] -->
m

<!-- b001697 | furniture | pages [15] -->
m

<!-- b001698 | furniture | pages [15] -->
m

<!-- b001699 | furniture | pages [15] -->
m

<!-- b001700 | furniture | pages [15] -->
m

<!-- b001701 | furniture | pages [15] -->
m

<!-- b001702 | furniture | pages [15] -->
m

<!-- b001703 | furniture | pages [15] -->
m

<!-- b001704 | furniture | pages [15] -->
m

<!-- b001705 | furniture | pages [15] -->
m

<!-- b001706 | furniture | pages [15] -->
m

<!-- b001707 | furniture | pages [15] -->
m

<!-- b001708 | furniture | pages [15] -->
m

<!-- b001709 | furniture | pages [15] -->
m

<!-- b001710 | furniture | pages [15] -->
m

<!-- b001711 | furniture | pages [15] -->
m

<!-- b001712 | furniture | pages [15] -->
m

<!-- b001713 | furniture | pages [15] -->
m

<!-- b001714 | furniture | pages [15] -->
m

<!-- b001715 | furniture | pages [15] -->
m

<!-- b001716 | furniture | pages [15] -->
m

<!-- b001717 | furniture | pages [15] -->
m

<!-- b001718 | furniture | pages [15] -->
m

<!-- b001719 | furniture | pages [15] -->
m

<!-- b001720 | furniture | pages [15] -->
m

<!-- b001721 | furniture | pages [15] -->
m

<!-- b001722 | furniture | pages [15] -->
m

<!-- b001723 | furniture | pages [15] -->
m

<!-- b001724 | furniture | pages [15] -->
m

<!-- b001725 | furniture | pages [15] -->
m

<!-- b001726 | furniture | pages [15] -->
m

<!-- b001727 | furniture | pages [15] -->
m

<!-- b001728 | furniture | pages [15] -->
m

<!-- b001729 | furniture | pages [15] -->
m

<!-- b001730 | furniture | pages [15] -->
m

<!-- b001731 | furniture | pages [15] -->
m

<!-- b001732 | furniture | pages [15] -->
m

<!-- b001733 | furniture | pages [15] -->
m

<!-- b001734 | furniture | pages [15] -->
m

<!-- b001735 | furniture | pages [15] -->
m

<!-- b001736 | furniture | pages [15] -->
m

<!-- b001737 | furniture | pages [15] -->
m

<!-- b001738 | furniture | pages [15] -->
m

<!-- b001739 | furniture | pages [15] -->
m

<!-- b001740 | furniture | pages [15] -->
m

<!-- b001741 | furniture | pages [15] -->
m

<!-- b001742 | furniture | pages [15] -->
m

<!-- b001743 | furniture | pages [15] -->
m

<!-- b001744 | furniture | pages [15] -->
m

<!-- b001745 | furniture | pages [15] -->
m

<!-- b001746 | furniture | pages [15] -->
m

<!-- b001747 | furniture | pages [15] -->
m

<!-- b001748 | furniture | pages [15] -->
m

<!-- b001749 | furniture | pages [15] -->
m

<!-- b001750 | furniture | pages [15] -->
m

<!-- b001751 | furniture | pages [15] -->
m

<!-- b001752 | furniture | pages [15] -->
m

<!-- b001753 | furniture | pages [15] -->
m

<!-- b001754 | furniture | pages [15] -->
m

<!-- b001755 | furniture | pages [15] -->
m

<!-- b001756 | furniture | pages [15] -->
m

<!-- b001757 | furniture | pages [15] -->
m

<!-- b001758 | furniture | pages [15] -->
m

<!-- b001759 | furniture | pages [15] -->
m

<!-- b001760 | furniture | pages [15] -->
m

<!-- b001761 | furniture | pages [15] -->
m

<!-- b001762 | furniture | pages [15] -->
m

<!-- b001763 | furniture | pages [15] -->
m

<!-- b001764 | furniture | pages [15] -->
m

<!-- b001765 | furniture | pages [15] -->
m

<!-- b001766 | furniture | pages [15] -->
m

<!-- b001767 | furniture | pages [15] -->
m

<!-- b001768 | furniture | pages [15] -->
m

<!-- b001769 | furniture | pages [15] -->
m

<!-- b001770 | furniture | pages [15] -->
m

<!-- b001771 | furniture | pages [15] -->
m

<!-- b001772 | furniture | pages [15] -->
m

<!-- b001773 | furniture | pages [15] -->
m

<!-- b001774 | furniture | pages [15] -->
m

<!-- b001775 | furniture | pages [15] -->
m

<!-- b001776 | furniture | pages [15] -->
m

<!-- b001777 | furniture | pages [15] -->
m

<!-- b001778 | furniture | pages [15] -->
m

<!-- b001779 | furniture | pages [15] -->
m

<!-- b001780 | furniture | pages [15] -->
m

<!-- b001781 | furniture | pages [15] -->
m

<!-- b001782 | furniture | pages [15] -->
m

<!-- b001783 | furniture | pages [15] -->
m

<!-- b001784 | furniture | pages [15] -->
m

<!-- b001785 | furniture | pages [15] -->
m

<!-- b001786 | furniture | pages [15] -->
m

<!-- b001787 | furniture | pages [15] -->
m

<!-- b001788 | furniture | pages [15] -->
m

<!-- b001789 | furniture | pages [15] -->
m

<!-- b001790 | furniture | pages [15] -->
m

<!-- b001791 | furniture | pages [15] -->
m

<!-- b001792 | furniture | pages [15] -->
m

<!-- b001793 | furniture | pages [15] -->
m

<!-- b001794 | furniture | pages [15] -->
m

<!-- b001795 | furniture | pages [15] -->
m

<!-- b001796 | furniture | pages [15] -->
m

<!-- b001797 | furniture | pages [15] -->
m

<!-- b001798 | furniture | pages [15] -->
m

<!-- b001799 | furniture | pages [15] -->
m

<!-- b001800 | furniture | pages [15] -->
m

<!-- b001801 | furniture | pages [15] -->
m

<!-- b001802 | furniture | pages [15] -->
m

<!-- b001803 | furniture | pages [15] -->
m

<!-- b001804 | furniture | pages [15] -->
m

<!-- b001805 | furniture | pages [15] -->
m

<!-- b001806 | furniture | pages [15] -->
m

<!-- b001807 | furniture | pages [15] -->
m

<!-- b001808 | furniture | pages [15] -->
m

<!-- b001809 | furniture | pages [15] -->
m

<!-- b001810 | furniture | pages [15] -->
m

<!-- b001811 | furniture | pages [15] -->
m

<!-- b001812 | furniture | pages [15] -->
m

<!-- b001813 | furniture | pages [15] -->
m

<!-- b001814 | furniture | pages [15] -->
m

<!-- b001815 | furniture | pages [15] -->
m

<!-- b001816 | furniture | pages [15] -->
m

<!-- b001817 | furniture | pages [15] -->
m

<!-- b001818 | furniture | pages [15] -->
m

<!-- b001819 | furniture | pages [15] -->
m

<!-- b001820 | furniture | pages [15] -->
m

<!-- b001821 | furniture | pages [15] -->
m

<!-- b001822 | furniture | pages [15] -->
m

<!-- b001823 | furniture | pages [15] -->
m

<!-- b001824 | furniture | pages [15] -->
m

<!-- b001825 | furniture | pages [15] -->
m

<!-- b001826 | furniture | pages [15] -->
m

<!-- b001827 | furniture | pages [15] -->
m

<!-- b001828 | furniture | pages [15] -->
m

<!-- b001829 | furniture | pages [15] -->
m

<!-- b001830 | furniture | pages [15] -->
m

<!-- b001831 | furniture | pages [15] -->
m

<!-- b001832 | furniture | pages [15] -->
m

<!-- b001833 | furniture | pages [15] -->
m

<!-- b001834 | furniture | pages [15] -->
m

<!-- b001835 | furniture | pages [15] -->
m

<!-- b001836 | furniture | pages [15] -->
m

<!-- b001837 | furniture | pages [15] -->
m

<!-- b001838 | furniture | pages [15] -->
m

<!-- b001839 | furniture | pages [15] -->
m

<!-- b001840 | furniture | pages [15] -->
m

<!-- b001841 | furniture | pages [15] -->
m

<!-- b001842 | furniture | pages [16] -->
Page 16 of 25

<!-- b001843 | furniture | pages [16] -->
Team # 2510862

<!-- b001845 | prose | pages [16] -->
Σi=1(Xi − X)(Yi − Y) (11) r √Σi=1(Xi − X)2Σi=1(Yi − Y)2

<!-- b001846 | prose | pages [16] -->
If the Pearson correlation coefficient is close to 1, it means that an increase in the num- ber of entries in an event is usually accompanied by an increase in the number of medals in a particular event, and vice versa.

<!-- b001847 | prose | pages [16] -->
The heat map of correlation coefficients upon shows that the linear correlation be- tween athletics,rowing,shooting,swimming and the number of medals is higher and has a higher impact on the growth of the number of medals. The linear correlation between athletics,rowing,shooting,swimming and the number of medals is higher and has a higher impact on the increase of the number of medals.

<!-- b001848 | heading | pages [16] -->
7.2 Most important sports for different countries

<!-- b001849 | prose | pages [16] -->
In order to quantify the impact of each sport on the medal predictions of different countries, SHAP (SHapley Additive exPlanations) provides an efficient solution, where SHAP values take into account the contribution of each feature to the predicted results from different types of models, in particular integrated models. Its value is derived from Shapley Values in game theory. We first calculate the marginal contribution of a feature, suppose we need to calculate the Shapley value of a feature xj, the steps are as follows:

<!-- b001850 | prose | pages [16] -->
Step 1, select a feature subset S : Suppose we first select a feature subset S, e.g.

<!-- b001851 | prose | pages [16] -->
S = {x1, x2}, denoting the historical number of gold medals and the number of participants of the country.

<!-- b001852 | prose | pages [16] -->
Step 2, calculating: Calculate the prediction result under the feature subset S.

<!-- b001853 | prose | pages [16] -->
Assuming that the historical number of gold medals and the number of participants of the country are x1 and x2, we predict the number of gold medals is f(S) = f(x1, x2).

<!-- b001854 | prose | pages [16] -->
Step 3, adding features: Then, we add features xj to the subset S to get a new feature set S U {xj}. Assume that xj represents the number of participants of the country in a particular event.

<!-- b001855 | prose | pages [16] -->
Step 4, calculating f(S ∪ {j}): The prediction result under the feature set S U {xj}, i.e., f(S U {xj}) = f(x1, x2, χj).

<!-- b001856 | prose | pages [16] -->
Step 5, calculating the marginal contribution: The marginal contribution of the feature xj to prediction result is ∆f j = f(S ∪ {xj}) − f(S), i.e., the contribution of the feature xj is the change after it is added under the current feature set S.

<!-- b001857 | caption | pages [16] -->
Figure 12: SHAP Calculation Process

<!-- b001858 | prose | pages [16, 17] -->
关注数学模型 • Averaging over all feature combinations:

<!-- b001859 | furniture | pages [16] -->
获取更多资讯

<!-- b001860 | furniture | pages [17] -->
Team # 2510862

<!-- b001861 | furniture | pages [17] -->
Page 17 of 25

<!-- b001863 | prose | pages [17] -->
To obtain the Shapley value of a feature xj, we need to sum over all possible fea- 微信公众号：数学模型 ture combinations S and calculate their average marginal contribution. The final Shapley value is the weighted average of the marginal contributions of all combina- tions:Equation 12 X |S|! (|N| −|S| −1)! (12) [f(S ∪{j}) −f(S)] ϕj(f) = |N|! S⊆N\{j} Where: ϕj(f) is the Shapley value of the feature xj, i.e. the contribution of the feature to the model prediction; N is the collection of all features xj.

<!-- b001864 | prose | pages [17] -->
Through SHAP, we can quantify the contribution of each sport to national medal fore- casts. Larger SHAP values indicate that the sport has a greater impact on medal forecasts, 微信号：MATHmodels while smaller SHAP values indicate that the sport has a lesser impact on medal forecasts.

<!-- b001865 | caption | pages [17] -->
Figure 13: Top 10 SHAP Values for Different Sports in USA, CHN and AUS

<!-- b001866 | prose | pages [17] -->
The SHAP values of gold, silver and bronze medals of different countries are analysed separately. In the case of the USA, for example, the sports that contribute the most to the number of medals are track and field, which is much higher than the contribution of other sports, while the sports that contribute the most to China’s medal forecasts are shooting, track and field, etc., and those that contribute the most to Australia’s medal forecasts are swimming, cycling and rowing, etc.

<!-- b001867 | furniture | pages [18] -->
Team # 2510862

<!-- b001868 | furniture | pages [18] -->
Page 18 of 25

<!-- b001869 | heading | pages [18] -->
7.3 Impact of Host Country’s Event Selection on medal

<!-- b001870 | prose | pages [18] -->
Through the collection of information, we have learnt that the introduction of new competitive sports at the 2028 Los Angeles Olympics, namely baseball/softball, cricket, flag football, stick tennis and squash, will impact on the host country, the United States, in a number of ways in terms of its overall medal performance and overall Olympic strategy.

<!-- b001871 | prose | pages [18] -->
By analysing the shap values of each US sport to its medal count, it was found that rugby has a high contribution to the US medal count (9th out of all sports to the gold list, 8th to the silver list, and 6th to the bronze list), and that the US has a strong tradition of rugby-related sports, so the addition of flag rugby may bring more medals to the US. Similarly, the United States, as the originator of stick tennis, will likely win more medals in this sport.

<!-- b001872 | prose | pages [18] -->
The IOC mentioned that the selection of the five new sports is in keeping with the American sporting culture, showcasing iconic American sports to the world while bring- ing international sports to the United States. As a host country, choosing sports with tra- ditional strengths along with those that are highly compatible with the country’s sporting culture helps to create a cultural identity, further inspire athletes to perform and increase international competitiveness and influence.

<!-- b001873 | heading | pages [18] -->
8 Task 4: Analysis of the "Great Coach" Effect and Its Im-

<!-- b001874 | prose | pages [18] -->
pact on Medals’ Performance

<!-- b001875 | heading | pages [18] -->
8.1 The effect contributes to medal counts

<!-- b001876 | prose | pages [18] -->
In major international events like the Olympics, coaches play a critical role not only in strategy and technique but also in psychological support and team coordination. The "great coach effect" suggests that the addition of exceptional coaches can significantly enhance a nation’s or team’s medal count.

<!-- b001877 | prose | pages [18] -->
Béla Károlyi, a renowned gymnastics coach, initially led the Romanian team to suc- cess before joining the U.S. team in 2000. His coaching was pivotal in elevating the U.S. women’s gymnastics team, leading to outstanding performances in the 2000-2016 Olympics. To evaluate his impact, we analyzed medal changes across nine Olympic Games from 1984 to 2016.

<!-- b001878 | prose | pages [18] -->
Directly comparing medal counts before and after 2000 might result in bias due to fac- tors like the number of participants or the host nation effect. To address this, we applied the PSM-DID method: PSM reduces selection bias by matching similar samples, while m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m DID controls for time effects by comparing changes before and after the intervention. In m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m this study, the U.S. women’s gymnastics team after 2000 was the treatment group, while m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the team before 2000 served as the control group. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Selection of Explanatory Variables, Explained Variables and Control Variables m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001879 | prose | pages [18] -->
• Dependent variable: The total number of medals won by the U.S. women’s gym- nastics team, focusing on the changes in medal counts after Károlyi joined in 2000.

<!-- b001880 | prose | pages [18, 19] -->
关注数学模型 • Independent variable: The effect of a great coach. The key time point is set at 2000, with Károlyi’s coaching period as the treatment group (great_coach=1) and other periods as the control group (great_coach=0).

<!-- b001881 | furniture | pages [18] -->
2

<!-- b001882 | furniture | pages [18] -->
MATHmodels

<!-- b001883 | furniture | pages [18] -->
获取更多资讯

<!-- b001884 | furniture | pages [19] -->
Team # 2510862

<!-- b001885 | furniture | pages [19] -->
Page 19 of 25

<!-- b001887 | prose | pages [19] -->
• Control variables: The number of athletes and host country status. The number of athletes reflects the team’s size during each Olympic cycle, while the host country status accounts for potential fluctuations in medal counts when the U.S. hosts the 微信公众号：数学模型 Olympics.

<!-- b001888 | prose | pages [19] -->
Model building: Select the explained variables and covariates

<!-- b001889 | prose | pages [19] -->
The propensity score was calculated using the Logist function

<!-- b001890 | prose | pages [19] -->
Propensity score The matching method was selected similarity principle asthe experimental group matching the

<!-- b001891 | prose | pages [19] -->
No 微信号：MATHmodels Whether it satisfes the common support hypothesisand the balance hypothesis test

<!-- b001892 | prose | pages [19] -->
Yes Do a parallel trend test on the matched samples

<!-- b001893 | prose | pages [19] -->
A symptotic double difierence estimationis performed for the matehed samples

<!-- b001894 | prose | pages [19] -->
Deriving "the Great Coach Effect"

<!-- b001895 | caption | pages [19] -->
Figure 14: Implementation steps and formulae derivation of the PSM-DID methodology

<!-- b001896 | prose | pages [19] -->
• Step 1: Propensity Score Matching (PSM) The purpose of PSM is to match units of observation with similar characteristics through propensity scores. First, the propensity score, which is the probability of being in the influence group of a great coach, is estimated for each sample through a logistic regression model. In our data, the PSM model is:Equation 14 (13) P(greatcoach = 1|X) = logistic(Xβ) where X is the control variable and β is the parameter to be estimated.

<!-- b001897 | prose | pages [19] -->
The propensity scores were then used to match the ‘treatment group’ with the ‘con- trol group’. We use the nearest neighbour matching, i.e. we select the control group unit with the closest propensity score to match with each treatment group unit. Af- ter matching, we can obtain a set of similar samples that are similar on the control variables, thus reducing the impact of selection bias.

<!-- b001898 | prose | pages [19, 20] -->
• Step 2: Difference-in-Differences (DID) The DID method is used to estimate the differential impact of a policy change or intervention that occurred at a specific point in time (2000) on the difference between the treated and control groups. We set up the DID model as:Equation 14 X (14) · DID + · Control + β3 · time + ri + ϵit Medal = β0 + β1 β2 Where: Medal is the number of medals in different years, DID is a cross-multiplier term ri ∗time indicating the effect of great coaching by Béla Károli; Control is a con- trol variable containing factors that may affect the change in the number of medals;

<!-- b001899 | furniture | pages [20] -->
Team # 2510862

<!-- b001900 | furniture | pages [20] -->
Page 20 of 25

<!-- b001902 | prose | pages [20] -->
Time is a time dummy variable to control for the effect of annual trends, taking the value of 0 before 2000 and 1 in 2000 and beyond. ri is a policy dummy variable, i.e., whether a great coach was introduced or not, with no introduction taking the value of 0 and introduction taking the value of 1. ϵit is a random error term indicating unobserved other factors; β0, β1, β2, β3 are the coefficients to be estimated.

<!-- b001903 | prose | pages [20] -->
• Step 3: Sample matching results and KDE analysis In an attempt to verify the quality of matching, we compare the distribution of propensity scores in the treatment and control groups before and after matching by using the kernel density distribution of propensity scores (KDE). Ideally, the propensity score distributions after matching should be very similar, indicating that the matching is valid.

<!-- b001904 | caption | pages [20] -->
Figure 15: Distribution of Propensity Scores

<!-- b001905 | prose | pages [20] -->
Through the KDE graph, we can visualise the low overlap between the propensity score distributions of the two groups before matching. After the PSM distribution, the overlap is higher, indicating that the propensity score matching is effective and reduces the selection bias.

<!-- b001906 | prose | pages [20] -->
• Step 4: Analysis of DID results The key coefficient in the DID model is the interaction term, which reflects the esti- mate of the great coaching effect. If significant and positive, it indicates that great coaching has a positive effect on the change in the number of medals won by USA Gymnastics.

<!-- b001907 | prose | pages [20, 21] -->
关注数学模型 (1) Medal Growth (2) Medal Growth (3) Medal Growth Variable (p-value) (p-value) (p-value)

<!-- b001908 | furniture | pages [20] -->
2

<!-- b001909 | furniture | pages [20] -->
MATHmodels

<!-- b001910 | furniture | pages [20] -->
获取更多资讯

<!-- b001911 | furniture | pages [21] -->
Page 21 of 25

<!-- b001912 | furniture | pages [21] -->
Team # 2510862

<!-- b001913 | caption | pages [21] -->
Table 2: DID regression analysis results

<!-- b001915 | heading | pages [21] -->
DID Variable

<!-- b001916 | prose | pages [21] -->
2.921** (0.03) 1.53** (0.05) 3.213** (0.02) (Great Coach effect) 0.034** (0.05) 0.029**(0.04) Athletes Counts 2.41 (0.02) 2.28 (0.02) Home Effect 2.93*** (0.02) 2.66** (0.02) 2.57** (0.01) Constant Term Control Control Time Variable Not Control Control Not Control Policy Variable 0.648 0.534 R-squared

<!-- b001917 | prose | pages [21] -->
• Column (1) shows the results of the test that controls for both time fixed effects and policy fixed effects without considering the control variables. At this point, the effect of the DID variable on MEDAL growth is 2.921 and is significantly positive at the 0.03 significance level.

<!-- b001918 | prose | pages [21] -->
Column (2) Shows the results of the test when control variables are included but not controlling for time and policy fixed effects. In this setting, the regression coefficient for the great coaching effect is 1.53. 1 Column (3) shows the results of the test with the inclusion of control variables and controlling for both time and policy fixed effects. In this case, the regression coeffi- cient of the great coach effect is 3.213 and has a significant positive effect at the 0.02 significance level.

<!-- b001919 | prose | pages [21] -->
According to the regression results of the DID model, the great coaching effect had a significant positive impact on the growth of USA Gymnastics' medal count. Specifically:

<!-- b001920 | heading | pages [21] -->
1. The great coaching effect significantly increased the number of medals without con-

<!-- b001921 | prose | pages [21] -->
sidering the control variables.

<!-- b001922 | heading | pages [21] -->
2. With the inclusion of control variables, the great coaching effect had a diminished,

<!-- b001923 | prose | pages [21] -->
but still significant, effect on medal growth.

<!-- b001924 | heading | pages [21] -->
3. After controlling for all relevant control variables and time and policy fixed effects,

<!-- b001925 | prose | pages [21] -->
the great coaching effect has the largest impact on medal growth and is extremely significant.

<!-- b001926 | prose | pages [21] -->
With the PSM-DID method, we were able to more accurately estimate the contribu- tion of great coaches to changes in medal counts, avoiding errors due to selection bias or temporal effects.The addition of Coach Béla Károlyi did provide a strong impetus to the growth of medal counts in the U.S. Gymnastics team. Therefore, given the importance of coaching in sports teams, future investment in good coaches may be an effective way to boost Olympic medal counts.

<!-- b001927 | furniture | pages [22] -->
Team # 2510862

<!-- b001928 | furniture | pages [22] -->
Page 22 of 25

<!-- b001929 | caption | pages [22] -->
Figure 16: Changes in medal counts before and after Béla Károlyi’s arrival

<!-- b001930 | prose | pages [22] -->
8.2

<!-- b001931 | heading | pages [22] -->
3 Countries should consider investing "Great Coach"

<!-- b001932 | prose | pages [22] -->
To explore how hiring a "great coach" can improve the medal count in gymnastics, we first established criteria for selecting countries. We focused on those countries where gymnastics has potential but whose medal count has declined in recent years.We com- pared data from two time periods: 1960-2000 and 2000-2024. First, we examined the total number of female gymnasts each country sent to the Olympics, which reflects the coun- try’s investment and emphasis on gymnastics. This metric is used to determine the size of the bubbles in the subsequent bubble chart.

<!-- b001933 | prose | pages [22] -->
Next, we compared the changes in medal counts, identifying countries that performed well between 1960-2000 but saw a decline in medals between 2000-2024. These countries may benefit from hiring a "great coach" to restore their gymnastics competitiveness. To this end, we used K-Means clustering analysis to identify countries with potential but poor recent performance. K-Means is an unsupervised learning method that divides data into groups.

<!-- b001934 | caption | pages [22] -->
Figure 17: The steps of our implementation of K-Means

<!-- b001935 | prose | pages [22, 23] -->
关注数学模型 Based on the results of the K-Means cluster analysis, we identified Spain (ESP), Japan (JPN) and Canada (CAN) as potential countries. All of these countries achieved better results between 1960-2000, however, between 2000-2024, the number of medals declined, although their investment in gymnastics remained relatively robust. By analysing these three countries, we believe that hiring ‘great coaches’ has the potential to help these coun- tries regain their level of performance, especially in women’s gymnastics.

<!-- b001936 | furniture | pages [22] -->
2

<!-- b001937 | furniture | pages [22] -->
MATHmodels

<!-- b001938 | furniture | pages [22] -->
获取更多资讯

<!-- b001939 | furniture | pages [23] -->
Team # 2510862

<!-- b001940 | furniture | pages [23] -->
Page 23 of 25

<!-- b001942 | prose | pages [23] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b001943 | caption | pages [23] -->
Figure 18: Women’s Gymnastics Medal Counts and Participation by country

<!-- b001944 | prose | pages [23] -->
By sifting through the data from these countries and inputting it into the PSM-DID model mentioned above, we conclude that hiring ‘great coaches’ has led to significant increases in the number of medals won by women’s gymnastics in Spain, Japan, and Canada of 4.32, 2.89, and 4.75, respectively, and these increases have been statistically significant at the 0.05 level of significance. were within the statistical significance level of 0.05. This suggests that the influence of great coaches has a significant and reliable effect in improving the performance of the gymnastics programmes in these countries.

<!-- b001945 | heading | pages [23] -->
9 Model Testing

<!-- b001946 | heading | pages [23] -->
9.1 Tests of the stacking model

<!-- b001947 | prose | pages [23] -->
In this study, we use 10-fold cross-validation to assess the generalisation ability of the Stacking model.

<!-- b001948 | prose | pages [23] -->
Let the dataset be D = {x1, x2, ..., xN} , where N is the size of the dataset. 1. Divide the dataset: Randomly divide the dataset D into 10 subsets D1, D2, ..., D10, each of which is of approximately equal size.

<!-- b001949 | prose | pages [23] -->
2. Traning and Testing: For the ith iteration, all subsets except Di are used for training and the remaining subset Di is used as the validation set. Training set Ti = D/Di , Test set Vi = Di.

<!-- b001950 | heading | pages [23] -->
3. Calculate the performance metrics For each validation, calculate the evaluation

<!-- b001951 | prose | pages [23, 24] -->
metrics of the model (e.g., accuracy, mean square error, etc.), denoted as: X 1 Ei = (yj −byj)2 |Vi| xj∈Vi 4.Calculate the average performance: The final average performance index is: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m X 10 Eavg = 1 Ei 10 i=1 Where Eavg is the average error or evaluation metric of the 10-fold cross-validation.

<!-- b001952 | furniture | pages [23] -->
m

<!-- b001953 | furniture | pages [23] -->
m

<!-- b001954 | furniture | pages [23] -->
m

<!-- b001955 | furniture | pages [23] -->
m

<!-- b001956 | furniture | pages [23] -->
m

<!-- b001957 | furniture | pages [23] -->
m

<!-- b001958 | furniture | pages [23] -->
m

<!-- b001959 | furniture | pages [23] -->
m

<!-- b001960 | furniture | pages [23] -->
m

<!-- b001961 | furniture | pages [23] -->
m

<!-- b001962 | furniture | pages [23] -->
m

<!-- b001963 | furniture | pages [23] -->
m

<!-- b001964 | furniture | pages [23] -->
m

<!-- b001965 | furniture | pages [23] -->
m

<!-- b001966 | furniture | pages [23] -->
m

<!-- b001967 | furniture | pages [23] -->
m

<!-- b001968 | furniture | pages [23] -->
m

<!-- b001969 | furniture | pages [23] -->
m

<!-- b001970 | furniture | pages [23] -->
m

<!-- b001971 | furniture | pages [23] -->
m

<!-- b001972 | furniture | pages [23] -->
m

<!-- b001973 | furniture | pages [23] -->
m

<!-- b001974 | furniture | pages [23] -->
m

<!-- b001975 | furniture | pages [23] -->
m

<!-- b001976 | furniture | pages [23] -->
m

<!-- b001977 | furniture | pages [23] -->
m

<!-- b001978 | furniture | pages [23] -->
m

<!-- b001979 | furniture | pages [23] -->
m

<!-- b001980 | furniture | pages [23] -->
m

<!-- b001981 | furniture | pages [23] -->
m

<!-- b001982 | furniture | pages [23] -->
m

<!-- b001983 | furniture | pages [23] -->
m

<!-- b001984 | furniture | pages [23] -->
m

<!-- b001985 | furniture | pages [23] -->
m

<!-- b001986 | furniture | pages [23] -->
m

<!-- b001987 | furniture | pages [23] -->
m

<!-- b001988 | furniture | pages [23] -->
m

<!-- b001989 | furniture | pages [23] -->
m

<!-- b001990 | furniture | pages [23] -->
m

<!-- b001991 | furniture | pages [23] -->
m

<!-- b001992 | furniture | pages [23] -->
m

<!-- b001993 | furniture | pages [23] -->
m

<!-- b001994 | furniture | pages [23] -->
m

<!-- b001995 | furniture | pages [23] -->
m

<!-- b001996 | furniture | pages [23] -->
m

<!-- b001997 | furniture | pages [23] -->
m

<!-- b001998 | furniture | pages [23] -->
m

<!-- b001999 | furniture | pages [23] -->
m

<!-- b002000 | furniture | pages [23] -->
m

<!-- b002001 | furniture | pages [23] -->
m

<!-- b002002 | furniture | pages [23] -->
m

<!-- b002003 | furniture | pages [23] -->
m

<!-- b002004 | furniture | pages [23] -->
m

<!-- b002005 | furniture | pages [23] -->
m

<!-- b002006 | furniture | pages [23] -->
m

<!-- b002007 | furniture | pages [23] -->
m

<!-- b002008 | furniture | pages [23] -->
m

<!-- b002009 | furniture | pages [23] -->
m

<!-- b002010 | furniture | pages [23] -->
m

<!-- b002011 | furniture | pages [23] -->
m

<!-- b002012 | furniture | pages [23] -->
m

<!-- b002013 | furniture | pages [23] -->
m

<!-- b002014 | furniture | pages [23] -->
m

<!-- b002015 | furniture | pages [23] -->
m

<!-- b002016 | furniture | pages [23] -->
m

<!-- b002017 | furniture | pages [23] -->
m

<!-- b002018 | furniture | pages [23] -->
m

<!-- b002019 | furniture | pages [23] -->
m

<!-- b002020 | furniture | pages [23] -->
m

<!-- b002021 | furniture | pages [23] -->
m

<!-- b002022 | furniture | pages [23] -->
m

<!-- b002023 | furniture | pages [23] -->
m

<!-- b002024 | furniture | pages [23] -->
m

<!-- b002025 | furniture | pages [23] -->
m

<!-- b002026 | furniture | pages [23] -->
m

<!-- b002027 | furniture | pages [23] -->
m

<!-- b002028 | furniture | pages [23] -->
m

<!-- b002029 | furniture | pages [23] -->
m

<!-- b002030 | furniture | pages [23] -->
m

<!-- b002031 | furniture | pages [23] -->
m

<!-- b002032 | furniture | pages [23] -->
m

<!-- b002033 | furniture | pages [23] -->
m

<!-- b002034 | furniture | pages [23] -->
m

<!-- b002035 | furniture | pages [23] -->
m

<!-- b002036 | furniture | pages [23] -->
m

<!-- b002037 | furniture | pages [23] -->
m

<!-- b002038 | furniture | pages [23] -->
m

<!-- b002039 | furniture | pages [23] -->
m

<!-- b002040 | furniture | pages [23] -->
m

<!-- b002041 | furniture | pages [23] -->
m

<!-- b002042 | furniture | pages [23] -->
m

<!-- b002043 | furniture | pages [23] -->
m

<!-- b002044 | furniture | pages [23] -->
m

<!-- b002045 | furniture | pages [23] -->
m

<!-- b002046 | furniture | pages [23] -->
m

<!-- b002047 | furniture | pages [23] -->
m

<!-- b002048 | furniture | pages [23] -->
m

<!-- b002049 | furniture | pages [23] -->
m

<!-- b002050 | furniture | pages [23] -->
m

<!-- b002051 | furniture | pages [23] -->
m

<!-- b002052 | furniture | pages [23] -->
m

<!-- b002053 | furniture | pages [23] -->
m

<!-- b002054 | furniture | pages [23] -->
m

<!-- b002055 | furniture | pages [23] -->
m

<!-- b002056 | furniture | pages [23] -->
m

<!-- b002057 | furniture | pages [23] -->
m

<!-- b002058 | furniture | pages [23] -->
m

<!-- b002059 | furniture | pages [23] -->
m

<!-- b002060 | furniture | pages [23] -->
m

<!-- b002061 | furniture | pages [23] -->
m

<!-- b002062 | furniture | pages [23] -->
m

<!-- b002063 | furniture | pages [23] -->
m

<!-- b002064 | furniture | pages [23] -->
m

<!-- b002065 | furniture | pages [23] -->
m

<!-- b002066 | furniture | pages [23] -->
m

<!-- b002067 | furniture | pages [23] -->
m

<!-- b002068 | furniture | pages [23] -->
m

<!-- b002069 | furniture | pages [23] -->
m

<!-- b002070 | furniture | pages [23] -->
m

<!-- b002071 | furniture | pages [23] -->
m

<!-- b002072 | furniture | pages [23] -->
m

<!-- b002073 | furniture | pages [23] -->
m

<!-- b002074 | furniture | pages [23] -->
m

<!-- b002075 | furniture | pages [23] -->
m

<!-- b002076 | furniture | pages [23] -->
m

<!-- b002077 | furniture | pages [23] -->
m

<!-- b002078 | furniture | pages [23] -->
m

<!-- b002079 | furniture | pages [23] -->
m

<!-- b002080 | furniture | pages [23] -->
m

<!-- b002081 | furniture | pages [23] -->
m

<!-- b002082 | furniture | pages [23] -->
m

<!-- b002083 | furniture | pages [23] -->
m

<!-- b002084 | furniture | pages [23] -->
m

<!-- b002085 | furniture | pages [23] -->
m

<!-- b002086 | furniture | pages [23] -->
m

<!-- b002087 | furniture | pages [23] -->
m

<!-- b002088 | furniture | pages [23] -->
m

<!-- b002089 | furniture | pages [23] -->
m

<!-- b002090 | furniture | pages [23] -->
m

<!-- b002091 | furniture | pages [23] -->
m

<!-- b002092 | furniture | pages [23] -->
m

<!-- b002093 | furniture | pages [23] -->
m

<!-- b002094 | furniture | pages [23] -->
m

<!-- b002095 | furniture | pages [23] -->
m

<!-- b002096 | furniture | pages [23] -->
m

<!-- b002097 | furniture | pages [23] -->
m

<!-- b002098 | furniture | pages [23] -->
m

<!-- b002099 | furniture | pages [23] -->
m

<!-- b002100 | furniture | pages [23] -->
m

<!-- b002101 | furniture | pages [23] -->
m

<!-- b002102 | furniture | pages [23] -->
m

<!-- b002103 | furniture | pages [23] -->
m

<!-- b002104 | furniture | pages [23] -->
m

<!-- b002105 | furniture | pages [23] -->
m

<!-- b002106 | furniture | pages [23] -->
m

<!-- b002107 | furniture | pages [23] -->
m

<!-- b002108 | furniture | pages [23] -->
m

<!-- b002109 | furniture | pages [23] -->
m

<!-- b002110 | furniture | pages [23] -->
m

<!-- b002111 | furniture | pages [23] -->
m

<!-- b002112 | furniture | pages [23] -->
m

<!-- b002113 | furniture | pages [23] -->
m

<!-- b002114 | furniture | pages [23] -->
m

<!-- b002115 | furniture | pages [23] -->
m

<!-- b002116 | furniture | pages [23] -->
m

<!-- b002117 | furniture | pages [23] -->
m

<!-- b002118 | furniture | pages [23] -->
m

<!-- b002119 | furniture | pages [23] -->
m

<!-- b002120 | furniture | pages [23] -->
m

<!-- b002121 | furniture | pages [23] -->
m

<!-- b002122 | furniture | pages [23] -->
m

<!-- b002123 | furniture | pages [23] -->
m

<!-- b002124 | furniture | pages [23] -->
m

<!-- b002125 | furniture | pages [23] -->
m

<!-- b002126 | furniture | pages [23] -->
m

<!-- b002127 | furniture | pages [23] -->
m

<!-- b002128 | furniture | pages [23] -->
m

<!-- b002129 | furniture | pages [23] -->
m

<!-- b002130 | furniture | pages [23] -->
m

<!-- b002131 | furniture | pages [23] -->
m

<!-- b002132 | furniture | pages [23] -->
m

<!-- b002133 | furniture | pages [23] -->
m

<!-- b002134 | furniture | pages [23] -->
m

<!-- b002135 | furniture | pages [23] -->
m

<!-- b002136 | furniture | pages [23] -->
m

<!-- b002137 | furniture | pages [23] -->
m

<!-- b002138 | furniture | pages [23] -->
m

<!-- b002139 | furniture | pages [23] -->
m

<!-- b002140 | furniture | pages [23] -->
m

<!-- b002141 | furniture | pages [23] -->
m

<!-- b002142 | furniture | pages [23] -->
m

<!-- b002143 | furniture | pages [23] -->
m

<!-- b002144 | furniture | pages [23] -->
m

<!-- b002145 | furniture | pages [23] -->
m

<!-- b002146 | furniture | pages [23] -->
m

<!-- b002147 | furniture | pages [23] -->
m

<!-- b002148 | furniture | pages [23] -->
m

<!-- b002149 | furniture | pages [23] -->
m

<!-- b002150 | furniture | pages [23] -->
m

<!-- b002151 | furniture | pages [23] -->
m

<!-- b002152 | furniture | pages [23] -->
m

<!-- b002153 | furniture | pages [23] -->
m

<!-- b002154 | furniture | pages [23] -->
m

<!-- b002155 | furniture | pages [23] -->
m

<!-- b002156 | furniture | pages [23] -->
m

<!-- b002157 | furniture | pages [23] -->
m

<!-- b002158 | furniture | pages [23] -->
m

<!-- b002159 | furniture | pages [23] -->
m

<!-- b002160 | furniture | pages [23] -->
m

<!-- b002161 | furniture | pages [23] -->
m

<!-- b002162 | furniture | pages [23] -->
m

<!-- b002163 | furniture | pages [23] -->
m

<!-- b002164 | furniture | pages [23] -->
m

<!-- b002165 | furniture | pages [23] -->
m

<!-- b002166 | furniture | pages [23] -->
m

<!-- b002167 | furniture | pages [23] -->
m

<!-- b002168 | furniture | pages [23] -->
m

<!-- b002169 | furniture | pages [23] -->
m

<!-- b002170 | furniture | pages [23] -->
m

<!-- b002171 | furniture | pages [23] -->
m

<!-- b002172 | furniture | pages [23] -->
m

<!-- b002173 | furniture | pages [23] -->
m

<!-- b002174 | furniture | pages [23] -->
m

<!-- b002175 | furniture | pages [23] -->
m

<!-- b002176 | furniture | pages [23] -->
m

<!-- b002177 | furniture | pages [23] -->
m

<!-- b002178 | furniture | pages [23] -->
m

<!-- b002179 | furniture | pages [23] -->
m

<!-- b002180 | furniture | pages [23] -->
m

<!-- b002181 | furniture | pages [23] -->
m

<!-- b002182 | furniture | pages [23] -->
m

<!-- b002183 | furniture | pages [23] -->
m

<!-- b002184 | furniture | pages [23] -->
m

<!-- b002185 | furniture | pages [23] -->
m

<!-- b002186 | furniture | pages [23] -->
m

<!-- b002187 | furniture | pages [23] -->
m

<!-- b002188 | furniture | pages [23] -->
m

<!-- b002189 | furniture | pages [23] -->
m

<!-- b002190 | furniture | pages [23] -->
m

<!-- b002191 | furniture | pages [23] -->
m

<!-- b002192 | furniture | pages [23] -->
m

<!-- b002193 | furniture | pages [23] -->
m

<!-- b002194 | furniture | pages [23] -->
m

<!-- b002195 | furniture | pages [23] -->
m

<!-- b002196 | furniture | pages [23] -->
m

<!-- b002197 | furniture | pages [23] -->
m

<!-- b002198 | furniture | pages [23] -->
m

<!-- b002199 | furniture | pages [23] -->
m

<!-- b002200 | furniture | pages [23] -->
m

<!-- b002201 | furniture | pages [23] -->
m

<!-- b002202 | furniture | pages [23] -->
m

<!-- b002203 | furniture | pages [23] -->
m

<!-- b002204 | furniture | pages [23] -->
m

<!-- b002205 | furniture | pages [23] -->
m

<!-- b002206 | furniture | pages [23] -->
m

<!-- b002207 | furniture | pages [23] -->
m

<!-- b002208 | furniture | pages [23] -->
m

<!-- b002209 | furniture | pages [23] -->
m

<!-- b002210 | furniture | pages [23] -->
m

<!-- b002211 | furniture | pages [23] -->
m

<!-- b002212 | furniture | pages [23] -->
m

<!-- b002213 | furniture | pages [23] -->
m

<!-- b002214 | furniture | pages [23] -->
m

<!-- b002215 | furniture | pages [23] -->
m

<!-- b002216 | furniture | pages [23] -->
m

<!-- b002217 | furniture | pages [23] -->
m

<!-- b002218 | furniture | pages [23] -->
m

<!-- b002219 | furniture | pages [23] -->
m

<!-- b002220 | furniture | pages [23] -->
m

<!-- b002221 | furniture | pages [23] -->
m

<!-- b002222 | furniture | pages [23] -->
m

<!-- b002223 | furniture | pages [23] -->
m

<!-- b002224 | furniture | pages [23] -->
m

<!-- b002225 | furniture | pages [23] -->
m

<!-- b002226 | furniture | pages [23] -->
m

<!-- b002227 | furniture | pages [23] -->
m

<!-- b002228 | furniture | pages [23] -->
m

<!-- b002229 | furniture | pages [23] -->
m

<!-- b002230 | furniture | pages [23] -->
m

<!-- b002231 | furniture | pages [23] -->
m

<!-- b002232 | furniture | pages [23] -->
m

<!-- b002233 | furniture | pages [23] -->
m

<!-- b002234 | furniture | pages [23] -->
m

<!-- b002235 | furniture | pages [23] -->
m

<!-- b002236 | furniture | pages [23] -->
m

<!-- b002237 | furniture | pages [23] -->
m

<!-- b002238 | furniture | pages [23] -->
m

<!-- b002239 | furniture | pages [23] -->
m

<!-- b002240 | furniture | pages [23] -->
m

<!-- b002241 | furniture | pages [23] -->
m

<!-- b002242 | furniture | pages [23] -->
m

<!-- b002243 | furniture | pages [23] -->
m

<!-- b002244 | furniture | pages [23] -->
m

<!-- b002245 | furniture | pages [23] -->
m

<!-- b002246 | furniture | pages [23] -->
m

<!-- b002247 | furniture | pages [23] -->
m

<!-- b002248 | furniture | pages [23] -->
m

<!-- b002249 | furniture | pages [23] -->
m

<!-- b002250 | furniture | pages [23] -->
m

<!-- b002251 | furniture | pages [23] -->
m

<!-- b002252 | furniture | pages [23] -->
m

<!-- b002253 | furniture | pages [23] -->
m

<!-- b002254 | furniture | pages [23] -->
m

<!-- b002255 | furniture | pages [23] -->
m

<!-- b002256 | furniture | pages [23] -->
m

<!-- b002257 | furniture | pages [23] -->
m

<!-- b002258 | furniture | pages [23] -->
m

<!-- b002259 | furniture | pages [23] -->
m

<!-- b002260 | furniture | pages [23] -->
m

<!-- b002261 | furniture | pages [23] -->
m

<!-- b002262 | furniture | pages [23] -->
m

<!-- b002263 | furniture | pages [23] -->
m

<!-- b002264 | furniture | pages [23] -->
m

<!-- b002265 | furniture | pages [23] -->
m

<!-- b002266 | furniture | pages [23] -->
m

<!-- b002267 | furniture | pages [23] -->
m

<!-- b002268 | furniture | pages [23] -->
m

<!-- b002269 | furniture | pages [23] -->
m

<!-- b002270 | furniture | pages [23] -->
m

<!-- b002271 | furniture | pages [23] -->
m

<!-- b002272 | furniture | pages [23] -->
m

<!-- b002273 | furniture | pages [23] -->
m

<!-- b002274 | furniture | pages [23] -->
m

<!-- b002275 | furniture | pages [23] -->
m

<!-- b002276 | furniture | pages [24] -->
Team # 2510862

<!-- b002277 | furniture | pages [24] -->
Page 24 of 25

<!-- b002279 | prose | pages [24] -->
After 10-fold cross-validation, the average R² of the Stacking model is 0.89, the average MSE is 0.31, and the average MAPE is 0.30, and these results do not fluctuate much from the performance without cross-validation, which indicates that the model’s performance on different data subsets stays consistent with good stability and generalisation ability.

<!-- b002280 | heading | pages [24] -->
9.2 Tests of the PSM-DID model

<!-- b002281 | heading | pages [24] -->
1. Balance test

<!-- b002282 | prose | pages [24] -->
Balance testing is an important step in assessing the validity of the propensity score matching (PSM) method. Its central aim is to ensure the differences between the treatment and control groups on the covariates after matching have been effectively controlled for, so the causal effects estimated by the model are reliable. With the KDE plots drawn earlier, we have analysed the proximity of distributions of the treatment and control groups be- fore and after matching. To further verify the balance of matching, we calculated the stan- dardised mean difference (SMD) values.The formula for the SMD values is:Equation 15 XT −XC q (15) SMD = V ar(XT )+V ar(XC) 2 The smaller the SMD value, the smaller the difference between the two groups, indi- cating better matching. Typically, an SMD value less than 0.1 suggests good matching quality. After calculation, we got the SMD value of 0.0013, which is significantly lower than the threshold of 0.1, indicating that the difference between the treatment group and the control group on the covariate has been effectively controlled, and the balance after matching is good. Therefore, the matching effect met the expectation and further verified the validity of our propensity score matching (PSM) method.

<!-- b002283 | heading | pages [24] -->
2. Sensitivity Analysis

<!-- b002284 | prose | pages [24] -->
Sensitivity analysis is used to evaluate the model’s response to changes in input vari- ables, particularly when facing uncertainty and changes in assumptions. It helps us un- derstand how sensitive the model is to different inputs, ensuring the model’s stability and reliability. In this study, the purpose of sensitivity analysis is to examine how changes in key factors affect the Olympic medal prediction model and assess its performance under different assumptions.

<!-- b002285 | prose | pages [24] -->
We selected input variables such as historical medal data, athlete participation, and host countries, and made small adjustments to these variables (±3%, ±5%, ±10%). After each adjustment, we reran the model and recorded the changes in the output, analyzing how the output changed with the input variations. By comparing the prediction results after different adjustments, we assess the model’s stability. If the model remains stable de- spite small changes in input, it indicates that the model is not sensitive to these variables and is robust.The analysis results show that small changes in the input variables have a minimal impact on the prediction results (standard error changes of ±1.174%, ±1.502%, ±3.115%), indicating that the model is stable.

<!-- b002286 | prose | pages [24] -->
关注数学模型

<!-- b002287 | furniture | pages [24] -->
2

<!-- b002288 | furniture | pages [24] -->
MATHmodels

<!-- b002289 | furniture | pages [24] -->
获取更多资讯

<!-- b002290 | furniture | pages [25] -->
Team # 2510862

<!-- b002291 | furniture | pages [25] -->
Page 25 of 25

<!-- b002292 | heading | pages [25] -->
10 Letter

<!-- b002293 | prose | pages [25] -->
Dear Members of National Olympic Committees, As we prepare for the 2028 Los Angeles Olympics, we have analyzed medal distribu- tion patterns using historical data and advanced modeling. Our findings provide valu- able insights to support strategic planning for participating nations.

<!-- b002294 | prose | pages [25] -->
We used the Stacking method to combine multiple models, improving prediction ac- curacy. Based on our model, the top five countries on the 2028 medal table are projected to be: the United States, China, Australia, France, and Germany. The model’s low MSE and MAPE indicate high reliability. Leading countries should focus on optimizing resources, 微信公众号：数学模型 while others can invest in potential events to seek breakthroughs.

<!-- b002295 | prose | pages [25] -->
For non-medal-winning nations, we analyzed participation trends and identified events with higher probabilities of first-time medals. These nations should increase investment in their strongest events to improve medal chances.

<!-- b002296 | prose | pages [25] -->
We also explored the relationship between events and medals. Using SHAP analysis, we found that new sports like rugby-related events could significantly benefit the United States, aligning with its traditional strengths. Countries should strategically prepare for these new events to maximize their opportunities.

<!-- b002297 | prose | pages [25] -->
On the "Great Coach Effect," our analysis of the U.S. gymnastics team shows that ex- ceptional coaching significantly boosts medal counts. The PSM-DID model confirmed 微信号：MATHmodels this effect, and we identified Spain, Japan, and Canada as nations with potential to bene- fit from hiring great coaches to rebuild their competitiveness in gymnastics.

<!-- b002298 | prose | pages [25] -->
In summary, our analysis offers a data-driven approach for Olympic preparation. From medal predictions to identifying first-time winners and event-specific strategies, our findings provide actionable insights to help countries excel at the 2028 Olympics.

<!-- b002299 | prose | pages [25] -->
Sincerely, Team 2510862

<!-- b002300 | heading | pages [25] -->
References

<!-- b002301 | references | pages [25] -->
[1] Sanchez-Fernandez, Patricio; Vaammonde-Liste, Antonio,”Olympic medals : suc-

<!-- b002302 | references | pages [25] -->
cess predictions for Rio-2016”, Sabinet,2016 Publishing Company , 1984-1986.

<!-- b002303 | references | pages [25] -->
[2] H.M.Shi,D.Y.Zhang,Y.H.Zhang, "Can Olympic medals be predicted? — A perspec-

<!-- b002304 | references | pages [25] -->
tive based on interpretable machine learning",Journal,2024

<!-- b002305 | references | pages [25] -->
[3] F.Wang,” Prediction of Olympic Medal Results for the 2020 Games Based on Neural

<!-- b002306 | references | pages [25] -->
Networks”,Journal,2023

<!-- b002307 | references | pages [25] -->
[4] Schlembach Christoph; Schmidt Sascha L.; Schreyer Dominik; Wunderlich Linus,”

<!-- b002308 | references | pages [25] -->
Forecasting the Olympic medal distribution – A socioeconomic machine learning

<!-- b002309 | references | pages [25] -->
model”, Elsevier,2022
