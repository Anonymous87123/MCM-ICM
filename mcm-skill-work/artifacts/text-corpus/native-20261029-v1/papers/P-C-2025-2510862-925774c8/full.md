# P-C-2025-2510862-925774c8

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
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

<!-- b000008 | heading | pages [1] -->
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

<!-- b000021 | furniture | pages [3] -->
Team # 2510862

<!-- b000022 | furniture | pages [3] -->
Page 3 of 25

<!-- b000023 | prose | pages [3] -->
1

<!-- b000024 | heading | pages [3] -->
Introduction

<!-- b000025 | prose | pages [3] -->
1.1 Problem background

<!-- b000026 | prose | pages [3] -->
As one of the most influential sporting events in the world, the Olympic Games have always attracted attention and participation from all over the world. Since the first mod-

<!-- b000027 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000028 | prose | pages [3] -->
ern Olympic Games in 1896, the Olympic medal table, especially the gold medal table, has become an important platform for countries to demonstrate their sports strength, national image and culture. In addition to the traditional sports strength, international political and socio-economic factors also affect the distribution of Olympic medals to dif- ferent degrees. The accelerating process of globalisation and inter-country cooperation and competition are shaping the landscape of the Olympic Games.

<!-- b000029 | prose | pages [3] -->
With the development of big data, artificial intelligence and other technologies, data- based analysis and prediction models have become a hot research topic in the field of sports. These technologies are not only capable of handling complex multi-dimensional

<!-- b000030 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000031 | prose | pages [3] -->
data, but also provide countries with a scientific basis for Olympic medal predictions through simulation and prediction. However, medal prediction is more than a simple analysis of data; it also needs to consider cultural, economic and social factors in the context of globalisation, which makes Olympic medal prediction an interdisciplinary and complex challenge.

<!-- b000032 | prose | pages [3] -->
1.2 Restatement of the problem

<!-- b000033 | prose | pages [3] -->
• Creating a model to predict the number of gold medals versus the total number of medals for each country and based on the model predicting the medal standings for the 2028 Summer Olympics in Los Angeles, USA as well as the prediction intervals and analysing whether certain countries are expected to improve or decline in their achievements in 2028 compared to 2024. • To predict which countries that have not won medals are likely to make a break- through at the upcoming 2028 Olympic Games in Los Angeles and evaluate the predicted results. • Analyse the number and type of Olympic events, explore the relationship between events and the number of medals won by each country, identify the events that have a significant impact on each country and analyse the impact of the events chosen by the host country on the outcome of the games. • Analyse the impact of the ’Great Coach Effect’ on the number of medals won based on relevant data. Select three countries to analyse the sports in which they should invest in ’great coaches’ and analyse their potential impact.

<!-- b000034 | prose | pages [3] -->
1.3 Our work

<!-- b000035 | prose | pages [3] -->
The content is summarized in Figure 1 and organized as follows: Section 2 outlines the assumptions and rationale. Section 3 explains the study’s nota- tions. Section 4 details data preprocessing. Section 5 develops the Olympic medal predic- tion model. Section 6 analyzes the likelihood of first-time medalists. Section 7 examines

<!-- b000036 | prose | pages [3] -->
m

<!-- b000037 | prose | pages [3] -->
m

<!-- b000038 | prose | pages [3] -->
m

<!-- b000039 | prose | pages [3] -->
m

<!-- b000040 | prose | pages [3] -->
m

<!-- b000041 | prose | pages [3] -->
m

<!-- b000042 | prose | pages [3] -->
m

<!-- b000043 | prose | pages [3] -->
m

<!-- b000044 | prose | pages [3] -->
m

<!-- b000045 | prose | pages [3] -->
m

<!-- b000046 | prose | pages [3] -->
m

<!-- b000047 | prose | pages [3] -->
m

<!-- b000048 | prose | pages [3] -->
m

<!-- b000049 | prose | pages [3] -->
m

<!-- b000050 | prose | pages [3] -->
m

<!-- b000051 | prose | pages [3] -->
m

<!-- b000052 | prose | pages [3] -->
m

<!-- b000053 | prose | pages [3] -->
m

<!-- b000054 | prose | pages [3] -->
m

<!-- b000055 | prose | pages [3] -->
m

<!-- b000056 | prose | pages [3] -->
m

<!-- b000057 | prose | pages [3] -->
m

<!-- b000058 | prose | pages [3] -->
m

<!-- b000059 | prose | pages [3] -->
m

<!-- b000060 | prose | pages [3] -->
m

<!-- b000061 | prose | pages [3] -->
m

<!-- b000062 | prose | pages [3] -->
m

<!-- b000063 | prose | pages [3] -->
m

<!-- b000064 | prose | pages [3] -->
m

<!-- b000065 | prose | pages [3] -->
m

<!-- b000066 | prose | pages [3] -->
m

<!-- b000067 | prose | pages [3] -->
m

<!-- b000068 | prose | pages [3] -->
m

<!-- b000069 | prose | pages [3] -->
m

<!-- b000070 | prose | pages [3] -->
m

<!-- b000071 | prose | pages [3] -->
m

<!-- b000072 | prose | pages [3] -->
m

<!-- b000073 | prose | pages [3] -->
m

<!-- b000074 | prose | pages [3] -->
m

<!-- b000075 | prose | pages [3] -->
m

<!-- b000076 | prose | pages [3] -->
m

<!-- b000077 | prose | pages [3] -->
m

<!-- b000078 | prose | pages [3] -->
m

<!-- b000079 | prose | pages [3] -->
m

<!-- b000080 | prose | pages [3] -->
m

<!-- b000081 | prose | pages [3] -->
m

<!-- b000082 | prose | pages [3] -->
m

<!-- b000083 | prose | pages [3] -->
m

<!-- b000084 | prose | pages [3] -->
m

<!-- b000085 | prose | pages [3] -->
m

<!-- b000086 | prose | pages [3] -->
m

<!-- b000087 | prose | pages [3] -->
m

<!-- b000088 | prose | pages [3] -->
m

<!-- b000089 | prose | pages [3] -->
m

<!-- b000090 | prose | pages [3] -->
m

<!-- b000091 | prose | pages [3] -->
m

<!-- b000092 | prose | pages [3] -->
m

<!-- b000093 | prose | pages [3] -->
m

<!-- b000094 | prose | pages [3] -->
m

<!-- b000095 | prose | pages [3] -->
m

<!-- b000096 | prose | pages [3] -->
m

<!-- b000097 | prose | pages [3] -->
m

<!-- b000098 | prose | pages [3] -->
m

<!-- b000099 | prose | pages [3] -->
m

<!-- b000100 | prose | pages [3] -->
m

<!-- b000101 | prose | pages [3] -->
m

<!-- b000102 | prose | pages [3] -->
m

<!-- b000103 | prose | pages [3] -->
m

<!-- b000104 | prose | pages [3] -->
m

<!-- b000105 | prose | pages [3] -->
m

<!-- b000106 | prose | pages [3] -->
m

<!-- b000107 | prose | pages [3] -->
m

<!-- b000108 | prose | pages [3] -->
m

<!-- b000109 | prose | pages [3] -->
m

<!-- b000110 | prose | pages [3] -->
m

<!-- b000111 | prose | pages [3] -->
m

<!-- b000112 | prose | pages [3] -->
m

<!-- b000113 | prose | pages [3] -->
m

<!-- b000114 | prose | pages [3] -->
m

<!-- b000115 | prose | pages [3] -->
m

<!-- b000116 | prose | pages [3] -->
m

<!-- b000117 | prose | pages [3] -->
m

<!-- b000118 | prose | pages [3] -->
m

<!-- b000119 | prose | pages [3] -->
m

<!-- b000120 | prose | pages [3] -->
m

<!-- b000121 | prose | pages [3] -->
m

<!-- b000122 | prose | pages [3] -->
m

<!-- b000123 | prose | pages [3] -->
m

<!-- b000124 | prose | pages [3] -->
m

<!-- b000125 | prose | pages [3] -->
m

<!-- b000126 | prose | pages [3] -->
m

<!-- b000127 | prose | pages [3] -->
m

<!-- b000128 | prose | pages [3] -->
m

<!-- b000129 | prose | pages [3] -->
m

<!-- b000130 | prose | pages [3] -->
m

<!-- b000131 | prose | pages [3] -->
m

<!-- b000132 | prose | pages [3] -->
m

<!-- b000133 | prose | pages [3] -->
m

<!-- b000134 | prose | pages [3] -->
m

<!-- b000135 | prose | pages [3] -->
m

<!-- b000136 | prose | pages [3] -->
m

<!-- b000137 | prose | pages [3] -->
m

<!-- b000138 | prose | pages [3] -->
m

<!-- b000139 | prose | pages [3] -->
m

<!-- b000140 | prose | pages [3] -->
m

<!-- b000141 | prose | pages [3] -->
m

<!-- b000142 | prose | pages [3] -->
m

<!-- b000143 | prose | pages [3] -->
m

<!-- b000144 | prose | pages [3] -->
m

<!-- b000145 | prose | pages [3] -->
m

<!-- b000146 | prose | pages [3] -->
m

<!-- b000147 | prose | pages [3] -->
m

<!-- b000148 | prose | pages [3] -->
m

<!-- b000149 | prose | pages [3] -->
m

<!-- b000150 | prose | pages [3] -->
m

<!-- b000151 | prose | pages [3] -->
m

<!-- b000152 | prose | pages [3] -->
m

<!-- b000153 | prose | pages [3] -->
m

<!-- b000154 | prose | pages [3] -->
m

<!-- b000155 | prose | pages [3] -->
m

<!-- b000156 | prose | pages [3] -->
m

<!-- b000157 | prose | pages [3] -->
m

<!-- b000158 | prose | pages [3] -->
m

<!-- b000159 | prose | pages [3] -->
m

<!-- b000160 | prose | pages [3] -->
m

<!-- b000161 | prose | pages [3] -->
m

<!-- b000162 | prose | pages [3] -->
m

<!-- b000163 | prose | pages [3] -->
m

<!-- b000164 | prose | pages [3] -->
m

<!-- b000165 | prose | pages [3] -->
m

<!-- b000166 | prose | pages [3] -->
m

<!-- b000167 | prose | pages [3] -->
m

<!-- b000168 | prose | pages [3] -->
m

<!-- b000169 | prose | pages [3] -->
m

<!-- b000170 | prose | pages [3] -->
m

<!-- b000171 | prose | pages [3] -->
m

<!-- b000172 | prose | pages [3] -->
m

<!-- b000173 | prose | pages [3] -->
m

<!-- b000174 | prose | pages [3] -->
m

<!-- b000175 | prose | pages [3] -->
m

<!-- b000176 | prose | pages [3] -->
m

<!-- b000177 | prose | pages [3] -->
m

<!-- b000178 | prose | pages [3] -->
m

<!-- b000179 | prose | pages [3] -->
m

<!-- b000180 | prose | pages [3] -->
m

<!-- b000181 | prose | pages [3] -->
m

<!-- b000182 | prose | pages [3] -->
m

<!-- b000183 | prose | pages [3] -->
m

<!-- b000184 | prose | pages [3] -->
m

<!-- b000185 | prose | pages [3] -->
m

<!-- b000186 | prose | pages [3] -->
m

<!-- b000187 | prose | pages [3] -->
m

<!-- b000188 | prose | pages [3] -->
m

<!-- b000189 | prose | pages [3] -->
m

<!-- b000190 | prose | pages [3] -->
m

<!-- b000191 | prose | pages [3] -->
m

<!-- b000192 | prose | pages [3] -->
m

<!-- b000193 | prose | pages [3] -->
m

<!-- b000194 | prose | pages [3] -->
m

<!-- b000195 | prose | pages [3] -->
m

<!-- b000196 | prose | pages [3] -->
m

<!-- b000197 | prose | pages [3] -->
m

<!-- b000198 | prose | pages [3] -->
m

<!-- b000199 | prose | pages [3] -->
m

<!-- b000200 | prose | pages [3] -->
m

<!-- b000201 | prose | pages [3] -->
m

<!-- b000202 | prose | pages [3] -->
m

<!-- b000203 | prose | pages [3] -->
m

<!-- b000204 | prose | pages [3] -->
m

<!-- b000205 | prose | pages [3] -->
m

<!-- b000206 | prose | pages [3] -->
m

<!-- b000207 | prose | pages [3] -->
m

<!-- b000208 | prose | pages [3] -->
m

<!-- b000209 | prose | pages [3] -->
m

<!-- b000210 | prose | pages [3] -->
m

<!-- b000211 | prose | pages [3] -->
m

<!-- b000212 | prose | pages [3] -->
m

<!-- b000213 | prose | pages [3] -->
m

<!-- b000214 | prose | pages [3] -->
m

<!-- b000215 | prose | pages [3] -->
m

<!-- b000216 | prose | pages [3] -->
m

<!-- b000217 | prose | pages [3] -->
m

<!-- b000218 | prose | pages [3] -->
m

<!-- b000219 | prose | pages [3] -->
m

<!-- b000220 | prose | pages [3] -->
m

<!-- b000221 | prose | pages [3] -->
m

<!-- b000222 | prose | pages [3] -->
m

<!-- b000223 | prose | pages [3] -->
m

<!-- b000224 | prose | pages [3] -->
m

<!-- b000225 | prose | pages [3] -->
m

<!-- b000226 | prose | pages [3] -->
m

<!-- b000227 | prose | pages [3] -->
m

<!-- b000228 | prose | pages [3] -->
m

<!-- b000229 | prose | pages [3] -->
m

<!-- b000230 | prose | pages [3] -->
m

<!-- b000231 | prose | pages [3] -->
m

<!-- b000232 | prose | pages [3] -->
m

<!-- b000233 | prose | pages [3] -->
m

<!-- b000234 | prose | pages [3] -->
m

<!-- b000235 | prose | pages [3] -->
m

<!-- b000236 | prose | pages [3] -->
m

<!-- b000237 | prose | pages [3] -->
m

<!-- b000238 | prose | pages [3] -->
m

<!-- b000239 | prose | pages [3] -->
m

<!-- b000240 | prose | pages [3] -->
m

<!-- b000241 | prose | pages [3] -->
m

<!-- b000242 | prose | pages [3] -->
m

<!-- b000243 | prose | pages [3] -->
m

<!-- b000244 | prose | pages [3] -->
m

<!-- b000245 | prose | pages [3] -->
m

<!-- b000246 | prose | pages [3] -->
m

<!-- b000247 | prose | pages [3] -->
m

<!-- b000248 | prose | pages [3] -->
m

<!-- b000249 | prose | pages [3] -->
m

<!-- b000250 | prose | pages [3] -->
m

<!-- b000251 | prose | pages [3] -->
m

<!-- b000252 | prose | pages [3] -->
m

<!-- b000253 | prose | pages [3] -->
m

<!-- b000254 | prose | pages [3] -->
m

<!-- b000255 | prose | pages [3] -->
m

<!-- b000256 | prose | pages [3] -->
m

<!-- b000257 | prose | pages [3] -->
m

<!-- b000258 | prose | pages [3] -->
m

<!-- b000259 | prose | pages [3] -->
m

<!-- b000260 | prose | pages [3] -->
m

<!-- b000261 | prose | pages [3] -->
m

<!-- b000262 | prose | pages [3] -->
m

<!-- b000263 | prose | pages [3] -->
m

<!-- b000264 | prose | pages [3] -->
m

<!-- b000265 | prose | pages [3] -->
m

<!-- b000266 | prose | pages [3] -->
m

<!-- b000267 | prose | pages [3] -->
m

<!-- b000268 | prose | pages [3] -->
m

<!-- b000269 | prose | pages [3] -->
m

<!-- b000270 | prose | pages [3] -->
m

<!-- b000271 | prose | pages [3] -->
m

<!-- b000272 | prose | pages [3] -->
m

<!-- b000273 | prose | pages [3] -->
m

<!-- b000274 | prose | pages [3] -->
m

<!-- b000275 | prose | pages [3] -->
m

<!-- b000276 | prose | pages [3] -->
m

<!-- b000277 | prose | pages [3] -->
m

<!-- b000278 | prose | pages [3] -->
m

<!-- b000279 | prose | pages [3] -->
m

<!-- b000280 | prose | pages [3] -->
m

<!-- b000281 | prose | pages [3] -->
m

<!-- b000282 | prose | pages [3] -->
m

<!-- b000283 | prose | pages [3] -->
m

<!-- b000284 | prose | pages [3] -->
m

<!-- b000285 | prose | pages [3] -->
m

<!-- b000286 | prose | pages [3] -->
m

<!-- b000287 | prose | pages [3] -->
m

<!-- b000288 | prose | pages [3] -->
m

<!-- b000289 | prose | pages [3] -->
m

<!-- b000290 | prose | pages [3] -->
m

<!-- b000291 | prose | pages [3] -->
m

<!-- b000292 | prose | pages [3] -->
m

<!-- b000293 | prose | pages [3] -->
m

<!-- b000294 | prose | pages [3] -->
m

<!-- b000295 | prose | pages [3] -->
m

<!-- b000296 | prose | pages [3] -->
m

<!-- b000297 | prose | pages [3] -->
m

<!-- b000298 | prose | pages [3] -->
m

<!-- b000299 | prose | pages [3] -->
m

<!-- b000300 | prose | pages [3] -->
m

<!-- b000301 | prose | pages [3] -->
m

<!-- b000302 | prose | pages [3] -->
m

<!-- b000303 | prose | pages [3] -->
m

<!-- b000304 | prose | pages [3] -->
m

<!-- b000305 | prose | pages [3] -->
m

<!-- b000306 | prose | pages [3] -->
m

<!-- b000307 | prose | pages [3] -->
m

<!-- b000308 | prose | pages [3] -->
m

<!-- b000309 | prose | pages [3] -->
m

<!-- b000310 | prose | pages [3] -->
m

<!-- b000311 | prose | pages [3] -->
m

<!-- b000312 | prose | pages [3] -->
m

<!-- b000313 | prose | pages [3] -->
m

<!-- b000314 | prose | pages [3] -->
m

<!-- b000315 | prose | pages [3] -->
m

<!-- b000316 | prose | pages [3] -->
m

<!-- b000317 | prose | pages [3] -->
m

<!-- b000318 | prose | pages [3] -->
m

<!-- b000319 | prose | pages [3] -->
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

<!-- b000415 | furniture | pages [3] -->
m

<!-- b000416 | furniture | pages [3] -->
m

<!-- b000417 | furniture | pages [3] -->
m

<!-- b000418 | furniture | pages [3] -->
m

<!-- b000419 | furniture | pages [3] -->
m

<!-- b000420 | furniture | pages [3] -->
m

<!-- b000421 | furniture | pages [3] -->
m

<!-- b000422 | furniture | pages [3] -->
m

<!-- b000423 | furniture | pages [3] -->
m

<!-- b000424 | furniture | pages [3] -->
m

<!-- b000425 | furniture | pages [3] -->
m

<!-- b000426 | furniture | pages [3] -->
m

<!-- b000427 | furniture | pages [3] -->
m

<!-- b000428 | furniture | pages [3] -->
m

<!-- b000429 | furniture | pages [3] -->
m

<!-- b000430 | furniture | pages [3] -->
m

<!-- b000431 | furniture | pages [3] -->
m

<!-- b000432 | furniture | pages [3] -->
m

<!-- b000433 | furniture | pages [3] -->
m

<!-- b000434 | furniture | pages [3] -->
m

<!-- b000435 | furniture | pages [3] -->
m

<!-- b000436 | furniture | pages [3] -->
m

<!-- b000437 | furniture | pages [3] -->
m

<!-- b000438 | furniture | pages [3] -->
m

<!-- b000439 | furniture | pages [3] -->
m

<!-- b000440 | furniture | pages [3] -->
m

<!-- b000441 | furniture | pages [3] -->
m

<!-- b000442 | furniture | pages [3] -->
m

<!-- b000443 | furniture | pages [3] -->
m

<!-- b000444 | furniture | pages [3] -->
m

<!-- b000445 | furniture | pages [3] -->
m

<!-- b000446 | furniture | pages [3] -->
m

<!-- b000447 | furniture | pages [3] -->
m

<!-- b000448 | furniture | pages [3] -->
m

<!-- b000449 | furniture | pages [3] -->
m

<!-- b000450 | furniture | pages [3] -->
m

<!-- b000451 | furniture | pages [3] -->
m

<!-- b000452 | furniture | pages [3] -->
m

<!-- b000453 | furniture | pages [3] -->
m

<!-- b000454 | furniture | pages [3] -->
m

<!-- b000455 | furniture | pages [3] -->
m

<!-- b000456 | furniture | pages [3] -->
m

<!-- b000457 | furniture | pages [3] -->
m

<!-- b000458 | furniture | pages [3] -->
m

<!-- b000459 | furniture | pages [3] -->
m

<!-- b000460 | furniture | pages [3] -->
m

<!-- b000461 | furniture | pages [3] -->
m

<!-- b000462 | furniture | pages [3] -->
m

<!-- b000463 | furniture | pages [3] -->
m

<!-- b000464 | furniture | pages [3] -->
m

<!-- b000465 | furniture | pages [3] -->
m

<!-- b000466 | furniture | pages [3] -->
m

<!-- b000467 | furniture | pages [3] -->
m

<!-- b000468 | furniture | pages [3] -->
m

<!-- b000469 | furniture | pages [3] -->
m

<!-- b000470 | furniture | pages [3] -->
m

<!-- b000471 | furniture | pages [3] -->
m

<!-- b000472 | furniture | pages [3] -->
m

<!-- b000473 | furniture | pages [3] -->
m

<!-- b000474 | furniture | pages [3] -->
m

<!-- b000475 | furniture | pages [3] -->
m

<!-- b000476 | furniture | pages [3] -->
m

<!-- b000477 | furniture | pages [3] -->
m

<!-- b000478 | furniture | pages [3] -->
m

<!-- b000479 | furniture | pages [3] -->
m

<!-- b000480 | furniture | pages [3] -->
m

<!-- b000481 | furniture | pages [3] -->
m

<!-- b000482 | furniture | pages [3] -->
m

<!-- b000483 | furniture | pages [3] -->
m

<!-- b000484 | furniture | pages [3] -->
m

<!-- b000485 | furniture | pages [3] -->
m

<!-- b000486 | furniture | pages [3] -->
m

<!-- b000487 | furniture | pages [3] -->
m

<!-- b000488 | furniture | pages [3] -->
m

<!-- b000489 | furniture | pages [3] -->
m

<!-- b000490 | furniture | pages [3] -->
m

<!-- b000491 | furniture | pages [3] -->
m

<!-- b000492 | furniture | pages [3] -->
m

<!-- b000493 | furniture | pages [3] -->
m

<!-- b000494 | furniture | pages [3] -->
m

<!-- b000495 | furniture | pages [3] -->
m

<!-- b000496 | furniture | pages [3] -->
m

<!-- b000497 | furniture | pages [3] -->
m

<!-- b000498 | furniture | pages [3] -->
m

<!-- b000499 | furniture | pages [3] -->
m

<!-- b000500 | furniture | pages [3] -->
m

<!-- b000501 | furniture | pages [3] -->
m

<!-- b000502 | furniture | pages [3] -->
m

<!-- b000503 | furniture | pages [3] -->
m

<!-- b000504 | furniture | pages [3] -->
m

<!-- b000505 | furniture | pages [3] -->
m

<!-- b000506 | furniture | pages [3] -->
m

<!-- b000507 | furniture | pages [3] -->
m

<!-- b000508 | furniture | pages [3] -->
m

<!-- b000509 | furniture | pages [3] -->
m

<!-- b000510 | furniture | pages [3] -->
m

<!-- b000511 | furniture | pages [3] -->
m

<!-- b000512 | furniture | pages [3] -->
m

<!-- b000513 | furniture | pages [3] -->
m

<!-- b000514 | furniture | pages [3] -->
m

<!-- b000515 | furniture | pages [3] -->
m

<!-- b000516 | furniture | pages [3] -->
m

<!-- b000517 | furniture | pages [3] -->
m

<!-- b000518 | furniture | pages [3] -->
m

<!-- b000519 | furniture | pages [3] -->
m

<!-- b000520 | furniture | pages [3] -->
m

<!-- b000521 | furniture | pages [3] -->
m

<!-- b000522 | furniture | pages [3] -->
m

<!-- b000523 | furniture | pages [3] -->
m

<!-- b000524 | furniture | pages [3] -->
m

<!-- b000525 | furniture | pages [3] -->
m

<!-- b000526 | furniture | pages [3] -->
m

<!-- b000527 | furniture | pages [3] -->
m

<!-- b000528 | furniture | pages [3] -->
m

<!-- b000529 | furniture | pages [3] -->
m

<!-- b000530 | furniture | pages [3] -->
m

<!-- b000531 | furniture | pages [3] -->
m

<!-- b000532 | furniture | pages [3] -->
m

<!-- b000533 | furniture | pages [3] -->
m

<!-- b000534 | furniture | pages [3] -->
m

<!-- b000535 | furniture | pages [3] -->
m

<!-- b000536 | furniture | pages [3] -->
m

<!-- b000537 | furniture | pages [3] -->
m

<!-- b000538 | furniture | pages [3] -->
m

<!-- b000539 | furniture | pages [3] -->
m

<!-- b000540 | furniture | pages [3] -->
m

<!-- b000541 | furniture | pages [3] -->
m

<!-- b000542 | furniture | pages [3] -->
m

<!-- b000543 | furniture | pages [3] -->
m

<!-- b000544 | furniture | pages [3] -->
m

<!-- b000545 | furniture | pages [3] -->
m

<!-- b000546 | furniture | pages [3] -->
m

<!-- b000547 | furniture | pages [3] -->
m

<!-- b000548 | furniture | pages [3] -->
m

<!-- b000549 | furniture | pages [3] -->
m

<!-- b000550 | furniture | pages [3] -->
m

<!-- b000551 | furniture | pages [3] -->
m

<!-- b000552 | furniture | pages [3] -->
m

<!-- b000553 | furniture | pages [3] -->
m

<!-- b000554 | furniture | pages [3] -->
m

<!-- b000555 | furniture | pages [3] -->
m

<!-- b000556 | furniture | pages [3] -->
m

<!-- b000557 | furniture | pages [3] -->
m

<!-- b000558 | furniture | pages [3] -->
m

<!-- b000559 | furniture | pages [3] -->
m

<!-- b000560 | furniture | pages [3] -->
m

<!-- b000561 | furniture | pages [3] -->
m

<!-- b000562 | furniture | pages [3] -->
m

<!-- b000563 | furniture | pages [3] -->
m

<!-- b000564 | furniture | pages [3] -->
m

<!-- b000565 | furniture | pages [3] -->
m

<!-- b000566 | furniture | pages [3] -->
m

<!-- b000567 | furniture | pages [3] -->
m

<!-- b000568 | furniture | pages [3] -->
m

<!-- b000569 | furniture | pages [3] -->
m

<!-- b000570 | furniture | pages [3] -->
m

<!-- b000571 | furniture | pages [3] -->
m

<!-- b000572 | furniture | pages [3] -->
m

<!-- b000573 | furniture | pages [3] -->
m

<!-- b000574 | furniture | pages [3] -->
m

<!-- b000575 | furniture | pages [3] -->
m

<!-- b000576 | furniture | pages [3] -->
m

<!-- b000577 | furniture | pages [3] -->
m

<!-- b000578 | furniture | pages [3] -->
m

<!-- b000579 | furniture | pages [3] -->
m

<!-- b000580 | furniture | pages [3] -->
m

<!-- b000581 | furniture | pages [3] -->
m

<!-- b000582 | furniture | pages [3] -->
m

<!-- b000583 | furniture | pages [3] -->
m

<!-- b000584 | furniture | pages [3] -->
m

<!-- b000585 | furniture | pages [3] -->
m

<!-- b000586 | furniture | pages [3] -->
m

<!-- b000587 | furniture | pages [3] -->
m

<!-- b000588 | furniture | pages [3] -->
m

<!-- b000589 | furniture | pages [3] -->
m

<!-- b000590 | furniture | pages [3] -->
m

<!-- b000591 | furniture | pages [3] -->
m

<!-- b000592 | furniture | pages [3] -->
m

<!-- b000593 | furniture | pages [3] -->
m

<!-- b000594 | furniture | pages [3] -->
m

<!-- b000595 | furniture | pages [3] -->
m

<!-- b000596 | furniture | pages [3] -->
m

<!-- b000597 | furniture | pages [3] -->
m

<!-- b000598 | furniture | pages [3] -->
m

<!-- b000599 | furniture | pages [3] -->
m

<!-- b000600 | furniture | pages [3] -->
m

<!-- b000601 | furniture | pages [3] -->
m

<!-- b000602 | furniture | pages [3] -->
m

<!-- b000603 | furniture | pages [3] -->
m

<!-- b000604 | furniture | pages [3] -->
m

<!-- b000605 | furniture | pages [3] -->
m

<!-- b000606 | furniture | pages [3] -->
m

<!-- b000607 | furniture | pages [3] -->
m

<!-- b000608 | furniture | pages [3] -->
m

<!-- b000609 | furniture | pages [3] -->
m

<!-- b000610 | furniture | pages [3] -->
m

<!-- b000611 | furniture | pages [3] -->
m

<!-- b000612 | furniture | pages [3] -->
m

<!-- b000613 | furniture | pages [3] -->
m

<!-- b000614 | furniture | pages [3] -->
m

<!-- b000615 | furniture | pages [3] -->
m

<!-- b000616 | furniture | pages [3] -->
m

<!-- b000617 | furniture | pages [3] -->
m

<!-- b000618 | furniture | pages [3] -->
m

<!-- b000619 | furniture | pages [3] -->
m

<!-- b000620 | furniture | pages [3] -->
m

<!-- b000621 | furniture | pages [3] -->
m

<!-- b000622 | furniture | pages [3] -->
m

<!-- b000623 | furniture | pages [3] -->
m

<!-- b000624 | furniture | pages [3] -->
m

<!-- b000625 | furniture | pages [3] -->
m

<!-- b000626 | furniture | pages [3] -->
m

<!-- b000627 | furniture | pages [3] -->
m

<!-- b000628 | furniture | pages [3] -->
m

<!-- b000629 | furniture | pages [3] -->
m

<!-- b000630 | furniture | pages [3] -->
m

<!-- b000631 | furniture | pages [3] -->
m

<!-- b000632 | furniture | pages [3] -->
m

<!-- b000633 | furniture | pages [3] -->
m

<!-- b000634 | furniture | pages [3] -->
m

<!-- b000635 | furniture | pages [3] -->
m

<!-- b000636 | furniture | pages [3] -->
m

<!-- b000637 | furniture | pages [3] -->
m

<!-- b000638 | furniture | pages [3] -->
m

<!-- b000639 | furniture | pages [3] -->
m

<!-- b000640 | furniture | pages [3] -->
m

<!-- b000641 | furniture | pages [3] -->
m

<!-- b000642 | furniture | pages [3] -->
m

<!-- b000643 | furniture | pages [3] -->
m

<!-- b000644 | furniture | pages [3] -->
m

<!-- b000645 | furniture | pages [3] -->
m

<!-- b000646 | furniture | pages [3] -->
m

<!-- b000647 | furniture | pages [3] -->
m

<!-- b000648 | furniture | pages [3] -->
m

<!-- b000649 | furniture | pages [3] -->
m

<!-- b000650 | furniture | pages [3] -->
m

<!-- b000651 | furniture | pages [3] -->
m

<!-- b000652 | furniture | pages [3] -->
m

<!-- b000653 | furniture | pages [3] -->
m

<!-- b000654 | furniture | pages [3] -->
m

<!-- b000655 | furniture | pages [3] -->
m

<!-- b000656 | furniture | pages [3] -->
m

<!-- b000657 | furniture | pages [3] -->
m

<!-- b000658 | furniture | pages [3] -->
m

<!-- b000659 | furniture | pages [3] -->
m

<!-- b000660 | furniture | pages [3] -->
m

<!-- b000661 | furniture | pages [3] -->
m

<!-- b000662 | furniture | pages [3] -->
m

<!-- b000663 | furniture | pages [3] -->
m

<!-- b000664 | furniture | pages [3] -->
m

<!-- b000665 | furniture | pages [3] -->
m

<!-- b000666 | furniture | pages [3] -->
m

<!-- b000667 | furniture | pages [3] -->
m

<!-- b000668 | furniture | pages [3] -->
m

<!-- b000669 | furniture | pages [3] -->
m

<!-- b000670 | furniture | pages [3] -->
m

<!-- b000671 | furniture | pages [3] -->
m

<!-- b000672 | furniture | pages [3] -->
m

<!-- b000673 | furniture | pages [3] -->
m

<!-- b000674 | furniture | pages [3] -->
m

<!-- b000675 | furniture | pages [3] -->
m

<!-- b000676 | furniture | pages [3] -->
m

<!-- b000677 | furniture | pages [3] -->
m

<!-- b000678 | furniture | pages [3] -->
m

<!-- b000679 | furniture | pages [3] -->
m

<!-- b000680 | furniture | pages [3] -->
m

<!-- b000681 | furniture | pages [3] -->
m

<!-- b000682 | furniture | pages [3] -->
m

<!-- b000683 | furniture | pages [3] -->
m

<!-- b000684 | furniture | pages [3] -->
m

<!-- b000685 | furniture | pages [3] -->
m

<!-- b000686 | furniture | pages [3] -->
m

<!-- b000687 | furniture | pages [3] -->
m

<!-- b000688 | furniture | pages [3] -->
m

<!-- b000689 | furniture | pages [3] -->
m

<!-- b000690 | furniture | pages [3] -->
m

<!-- b000691 | furniture | pages [3] -->
m

<!-- b000692 | furniture | pages [3] -->
m

<!-- b000693 | furniture | pages [3] -->
m

<!-- b000694 | furniture | pages [3] -->
m

<!-- b000695 | furniture | pages [3] -->
m

<!-- b000696 | furniture | pages [3] -->
m

<!-- b000697 | furniture | pages [3] -->
m

<!-- b000698 | furniture | pages [3] -->
m

<!-- b000699 | furniture | pages [3] -->
m

<!-- b000700 | furniture | pages [3] -->
m

<!-- b000701 | furniture | pages [3] -->
m

<!-- b000702 | furniture | pages [3] -->
m

<!-- b000703 | furniture | pages [3] -->
m

<!-- b000704 | furniture | pages [3] -->
m

<!-- b000705 | furniture | pages [3] -->
m

<!-- b000706 | furniture | pages [3] -->
m

<!-- b000707 | furniture | pages [3] -->
m

<!-- b000708 | furniture | pages [3] -->
m

<!-- b000709 | furniture | pages [3] -->
m

<!-- b000710 | furniture | pages [3] -->
m

<!-- b000711 | furniture | pages [3] -->
m

<!-- b000712 | furniture | pages [3] -->
m

<!-- b000713 | furniture | pages [3] -->
m

<!-- b000714 | furniture | pages [3] -->
m

<!-- b000715 | furniture | pages [3] -->
m

<!-- b000716 | furniture | pages [3] -->
m

<!-- b000717 | furniture | pages [3] -->
m

<!-- b000718 | furniture | pages [3] -->
m

<!-- b000719 | furniture | pages [3] -->
m

<!-- b000720 | furniture | pages [3] -->
m

<!-- b000721 | furniture | pages [3] -->
m

<!-- b000722 | furniture | pages [3] -->
m

<!-- b000723 | furniture | pages [4] -->
Team # 2510862

<!-- b000724 | furniture | pages [4] -->
Page 4 of 25

<!-- b000725 | prose | pages [4] -->
the impact of sports on medal counts. Section 8 quantifies the "great coach effect." Section 9 tests the models, and Section 10 evaluates their strengths and weaknesses.

<!-- b000726 | caption | pages [4] -->
Figure 1: Structure of our paper

<!-- b000727 | prose | pages [4] -->
2

<!-- b000728 | heading | pages [4] -->
Assumptions

<!-- b000729 | heading | pages [4] -->
1. Historically, the merging of different teams in a country has no significant effect

<!-- b000730 | prose | pages [4] -->
on exploring a country’s Olympic strength. The Olympic teams of some countries historically may have been divided into sub- teams, such as ’Argentina-1’, ’Argentina-2’, etc., especially in team events where there may have been multiple teams competing. We believe that combining the results of these different teams historically will not have an impact on analysing the overall strength of the country in the Olympic Games.

<!-- b000731 | heading | pages [4] -->
2. There is a correlation between the number of participants from a country in an

<!-- b000732 | prose | pages [4] -->
event and the country’s investment in that event. It is hypothesised that a higher number of participants from a country means that the country has invested more resources (e.g. training facilities, professional coaches, etc.) in the sport. An increase in the number of participants usually reflects the level of interest and importance the country attaches to the sport, and by increasing the participation of athletes, the country is likely to become more competitive in the

<!-- b000733 | prose | pages [4] -->
m

<!-- b000734 | prose | pages [4] -->
m

<!-- b000735 | prose | pages [4] -->
m

<!-- b000736 | prose | pages [4] -->
m

<!-- b000737 | prose | pages [4] -->
m

<!-- b000738 | prose | pages [4] -->
m

<!-- b000739 | prose | pages [4] -->
m

<!-- b000740 | prose | pages [4] -->
m

<!-- b000741 | prose | pages [4] -->
m

<!-- b000742 | prose | pages [4] -->
m

<!-- b000743 | prose | pages [4] -->
m

<!-- b000744 | prose | pages [4] -->
m

<!-- b000745 | prose | pages [4] -->
m

<!-- b000746 | prose | pages [4] -->
m

<!-- b000747 | prose | pages [4] -->
m

<!-- b000748 | prose | pages [4] -->
m

<!-- b000749 | prose | pages [4] -->
m

<!-- b000750 | prose | pages [4] -->
m

<!-- b000751 | prose | pages [4] -->
m

<!-- b000752 | prose | pages [4] -->
m

<!-- b000753 | prose | pages [4] -->
m

<!-- b000754 | prose | pages [4] -->
m

<!-- b000755 | prose | pages [4] -->
m

<!-- b000756 | prose | pages [4] -->
m

<!-- b000757 | prose | pages [4] -->
m

<!-- b000758 | prose | pages [4] -->
m

<!-- b000759 | prose | pages [4] -->
m

<!-- b000760 | prose | pages [4] -->
m

<!-- b000761 | prose | pages [4] -->
m

<!-- b000762 | prose | pages [4] -->
m

<!-- b000763 | prose | pages [4] -->
m

<!-- b000764 | prose | pages [4] -->
m

<!-- b000765 | prose | pages [4] -->
m

<!-- b000766 | prose | pages [4] -->
m

<!-- b000767 | prose | pages [4] -->
m

<!-- b000768 | prose | pages [4] -->
m

<!-- b000769 | prose | pages [4] -->
m

<!-- b000770 | prose | pages [4] -->
m

<!-- b000771 | prose | pages [4] -->
m

<!-- b000772 | prose | pages [4] -->
m

<!-- b000773 | prose | pages [4] -->
m

<!-- b000774 | prose | pages [4] -->
m

<!-- b000775 | prose | pages [4] -->
m

<!-- b000776 | prose | pages [4] -->
m

<!-- b000777 | prose | pages [4] -->
m

<!-- b000778 | prose | pages [4] -->
m

<!-- b000779 | prose | pages [4] -->
m

<!-- b000780 | prose | pages [4] -->
m

<!-- b000781 | prose | pages [4] -->
m

<!-- b000782 | prose | pages [4] -->
m

<!-- b000783 | prose | pages [4] -->
m

<!-- b000784 | prose | pages [4] -->
m

<!-- b000785 | prose | pages [4] -->
m

<!-- b000786 | prose | pages [4] -->
m

<!-- b000787 | prose | pages [4] -->
m

<!-- b000788 | prose | pages [4] -->
m

<!-- b000789 | prose | pages [4] -->
m

<!-- b000790 | prose | pages [4] -->
m

<!-- b000791 | prose | pages [4] -->
m

<!-- b000792 | prose | pages [4] -->
m

<!-- b000793 | prose | pages [4] -->
m

<!-- b000794 | prose | pages [4] -->
m

<!-- b000795 | prose | pages [4] -->
m

<!-- b000796 | prose | pages [4] -->
m

<!-- b000797 | prose | pages [4] -->
m

<!-- b000798 | prose | pages [4] -->
m

<!-- b000799 | prose | pages [4] -->
m

<!-- b000800 | prose | pages [4] -->
m

<!-- b000801 | prose | pages [4] -->
m

<!-- b000802 | prose | pages [4] -->
m

<!-- b000803 | prose | pages [4] -->
m

<!-- b000804 | prose | pages [4] -->
m m

<!-- b000805 | prose | pages [4] -->
m m

<!-- b000806 | prose | pages [4] -->
m m

<!-- b000807 | prose | pages [4] -->
m m

<!-- b000808 | prose | pages [4] -->
m m

<!-- b000809 | prose | pages [4] -->
m

<!-- b000810 | prose | pages [4] -->
m

<!-- b000811 | prose | pages [4] -->
m m

<!-- b000812 | prose | pages [4] -->
m m

<!-- b000813 | prose | pages [4] -->
m m

<!-- b000814 | prose | pages [4] -->
m m

<!-- b000815 | prose | pages [4] -->
m

<!-- b000816 | prose | pages [4] -->
m m

<!-- b000817 | prose | pages [4] -->
m m

<!-- b000818 | prose | pages [4] -->
m m

<!-- b000819 | prose | pages [4] -->
m m

<!-- b000820 | prose | pages [4] -->
m

<!-- b000821 | prose | pages [4] -->
m

<!-- b000822 | prose | pages [4] -->
m m

<!-- b000823 | prose | pages [4] -->
m m

<!-- b000824 | prose | pages [4] -->
m m

<!-- b000825 | prose | pages [4] -->
m

<!-- b000826 | prose | pages [4] -->
m

<!-- b000827 | prose | pages [4] -->
m

<!-- b000828 | prose | pages [4] -->
m m

<!-- b000829 | prose | pages [4] -->
m m

<!-- b000830 | prose | pages [4] -->
m m

<!-- b000831 | prose | pages [4] -->
m m

<!-- b000832 | prose | pages [4] -->
m m

<!-- b000833 | prose | pages [4] -->
m m

<!-- b000834 | prose | pages [4] -->
m

<!-- b000835 | prose | pages [4] -->
m

<!-- b000836 | prose | pages [4] -->
m m

<!-- b000837 | prose | pages [4] -->
m m

<!-- b000838 | prose | pages [4] -->
m m

<!-- b000839 | prose | pages [4] -->
m m

<!-- b000840 | prose | pages [4] -->
m

<!-- b000841 | prose | pages [4] -->
sport and thus improve its chances of winning medals.

<!-- b000842 | prose | pages [4] -->
m

<!-- b000843 | prose | pages [4] -->
m

<!-- b000844 | prose | pages [4] -->
m

<!-- b000845 | prose | pages [4] -->
m

<!-- b000846 | prose | pages [4] -->
m

<!-- b000847 | prose | pages [4] -->
m

<!-- b000848 | prose | pages [4] -->
m

<!-- b000849 | prose | pages [4] -->
m

<!-- b000850 | prose | pages [4] -->
m

<!-- b000851 | prose | pages [4] -->
m

<!-- b000852 | prose | pages [4] -->
m

<!-- b000853 | prose | pages [4] -->
m

<!-- b000854 | prose | pages [4] -->
m

<!-- b000855 | prose | pages [4] -->
m

<!-- b000856 | prose | pages [4] -->
m

<!-- b000857 | prose | pages [4] -->
m

<!-- b000858 | prose | pages [4] -->
m

<!-- b000859 | prose | pages [4] -->
m

<!-- b000860 | prose | pages [4] -->
m

<!-- b000861 | prose | pages [4] -->
m

<!-- b000862 | prose | pages [4] -->
m

<!-- b000863 | prose | pages [4] -->
m

<!-- b000864 | prose | pages [4] -->
m

<!-- b000865 | prose | pages [4] -->
m

<!-- b000866 | prose | pages [4] -->
m

<!-- b000867 | prose | pages [4] -->
m

<!-- b000868 | prose | pages [4] -->
m

<!-- b000869 | prose | pages [4] -->
m

<!-- b000870 | prose | pages [4] -->
m

<!-- b000871 | prose | pages [4] -->
m

<!-- b000872 | prose | pages [4] -->
m

<!-- b000873 | prose | pages [4] -->
m

<!-- b000874 | prose | pages [4] -->
m

<!-- b000875 | prose | pages [4] -->
m

<!-- b000876 | prose | pages [4] -->
m

<!-- b000877 | prose | pages [4] -->
m

<!-- b000878 | prose | pages [4] -->
m

<!-- b000879 | prose | pages [4] -->
m

<!-- b000880 | prose | pages [4] -->
m

<!-- b000881 | prose | pages [4] -->
m

<!-- b000882 | prose | pages [4] -->
m

<!-- b000883 | prose | pages [4] -->
m

<!-- b000884 | prose | pages [4] -->
m

<!-- b000885 | prose | pages [4] -->
m

<!-- b000886 | prose | pages [4] -->
m

<!-- b000887 | prose | pages [4] -->
m

<!-- b000888 | prose | pages [4] -->
m

<!-- b000889 | prose | pages [4] -->
m

<!-- b000890 | prose | pages [4] -->
m

<!-- b000891 | prose | pages [4] -->
m

<!-- b000892 | prose | pages [4] -->
m

<!-- b000893 | prose | pages [4] -->
m

<!-- b000894 | prose | pages [4] -->
m

<!-- b000895 | prose | pages [4] -->
m

<!-- b000896 | prose | pages [4] -->
m

<!-- b000897 | prose | pages [4] -->
m

<!-- b000898 | prose | pages [4] -->
m

<!-- b000899 | prose | pages [4] -->
m

<!-- b000900 | prose | pages [4] -->
m

<!-- b000901 | prose | pages [4] -->
m

<!-- b000902 | prose | pages [4] -->
m

<!-- b000903 | prose | pages [4] -->
m

<!-- b000904 | prose | pages [4] -->
m

<!-- b000905 | prose | pages [4] -->
m

<!-- b000906 | prose | pages [4] -->
m

<!-- b000907 | prose | pages [4] -->
m

<!-- b000908 | prose | pages [4] -->
m

<!-- b000909 | prose | pages [4] -->
m

<!-- b000910 | prose | pages [4] -->
m

<!-- b000911 | prose | pages [4] -->
m

<!-- b000912 | prose | pages [4] -->
m

<!-- b000913 | prose | pages [4] -->
m

<!-- b000914 | prose | pages [4] -->
m

<!-- b000915 | prose | pages [4] -->
m

<!-- b000916 | prose | pages [4] -->
m

<!-- b000917 | prose | pages [4] -->
m

<!-- b000918 | prose | pages [4] -->
m

<!-- b000919 | prose | pages [4] -->
m

<!-- b000920 | prose | pages [4] -->
m

<!-- b000921 | prose | pages [4] -->
m

<!-- b000922 | prose | pages [4] -->
m

<!-- b000923 | prose | pages [4] -->
m

<!-- b000924 | prose | pages [4] -->
m

<!-- b000925 | prose | pages [4] -->
m

<!-- b000926 | prose | pages [4] -->
m

<!-- b000927 | prose | pages [4] -->
m

<!-- b000928 | prose | pages [4] -->
m

<!-- b000929 | prose | pages [4] -->
m

<!-- b000930 | prose | pages [4] -->
m

<!-- b000931 | prose | pages [4] -->
m

<!-- b000932 | prose | pages [4] -->
m

<!-- b000933 | prose | pages [4] -->
m

<!-- b000934 | prose | pages [4] -->
m

<!-- b000935 | prose | pages [4] -->
m

<!-- b000936 | prose | pages [4] -->
m

<!-- b000937 | prose | pages [4] -->
m

<!-- b000938 | prose | pages [4] -->
m

<!-- b000939 | prose | pages [4] -->
m

<!-- b000940 | prose | pages [4] -->
m

<!-- b000941 | prose | pages [4] -->
m

<!-- b000942 | prose | pages [4] -->
m

<!-- b000943 | prose | pages [4] -->
m

<!-- b000944 | prose | pages [4] -->
m

<!-- b000945 | prose | pages [4] -->
m

<!-- b000946 | prose | pages [4] -->
m

<!-- b000947 | prose | pages [4] -->
m

<!-- b000948 | prose | pages [4] -->
m

<!-- b000949 | prose | pages [4] -->
m

<!-- b000950 | prose | pages [4] -->
m

<!-- b000951 | prose | pages [4] -->
m

<!-- b000952 | prose | pages [4] -->
m

<!-- b000953 | prose | pages [4] -->
m

<!-- b000954 | prose | pages [4] -->
m m

<!-- b000955 | prose | pages [4] -->
m m

<!-- b000956 | prose | pages [4] -->
m m

<!-- b000957 | prose | pages [4] -->
m m

<!-- b000958 | prose | pages [4] -->
m

<!-- b000959 | prose | pages [4] -->
m

<!-- b000960 | prose | pages [4] -->
m

<!-- b000961 | prose | pages [4] -->
m m

<!-- b000962 | prose | pages [4] -->
m m

<!-- b000963 | prose | pages [4] -->
m m

<!-- b000964 | prose | pages [4] -->
m m

<!-- b000965 | prose | pages [4] -->
m

<!-- b000966 | prose | pages [4] -->
m

<!-- b000967 | prose | pages [4] -->
m m

<!-- b000968 | prose | pages [4] -->
m m

<!-- b000969 | prose | pages [4] -->
m m

<!-- b000970 | prose | pages [4] -->
m m

<!-- b000971 | prose | pages [4] -->
m m

<!-- b000972 | prose | pages [4] -->
m

<!-- b000973 | prose | pages [4] -->
m

<!-- b000974 | prose | pages [4] -->
m

<!-- b000975 | prose | pages [4] -->
m m

<!-- b000976 | prose | pages [4] -->
m m

<!-- b000977 | prose | pages [4] -->
m m

<!-- b000978 | prose | pages [4] -->
m m

<!-- b000979 | prose | pages [4] -->
m m

<!-- b000980 | prose | pages [4] -->
m m

<!-- b000981 | prose | pages [4] -->
m m

<!-- b000982 | prose | pages [4] -->
m

<!-- b000983 | prose | pages [4] -->
m m

<!-- b000984 | prose | pages [4] -->
m m

<!-- b000985 | prose | pages [4] -->
m m

<!-- b000986 | prose | pages [4] -->
m m

<!-- b000987 | prose | pages [4] -->
m

<!-- b000988 | prose | pages [4] -->
m m

<!-- b000989 | prose | pages [4] -->
m m

<!-- b000990 | prose | pages [4] -->
m m

<!-- b000991 | prose | pages [4] -->
m m

<!-- b000992 | prose | pages [4] -->
m m

<!-- b000993 | prose | pages [4] -->
m

<!-- b000994 | prose | pages [4] -->
m

<!-- b000995 | prose | pages [4] -->
m

<!-- b000996 | prose | pages [4] -->
m m

<!-- b000997 | prose | pages [4] -->
m m

<!-- b000998 | prose | pages [4] -->
m m

<!-- b000999 | prose | pages [4] -->
m m

<!-- b001000 | prose | pages [4] -->
m m

<!-- b001001 | prose | pages [4] -->
m

<!-- b001002 | prose | pages [4] -->
m m

<!-- b001003 | prose | pages [4] -->
m m

<!-- b001004 | prose | pages [4] -->
m m

<!-- b001005 | prose | pages [4] -->
m m

<!-- b001006 | prose | pages [4] -->
m

<!-- b001007 | prose | pages [4] -->
m

<!-- b001008 | prose | pages [4] -->
m

<!-- b001009 | prose | pages [4] -->
m m

<!-- b001010 | prose | pages [4] -->
m m

<!-- b001011 | prose | pages [4] -->
m m

<!-- b001012 | prose | pages [4] -->
m m

<!-- b001013 | prose | pages [4] -->
m m

<!-- b001014 | prose | pages [4] -->
m

<!-- b001015 | prose | pages [4] -->
m

<!-- b001016 | prose | pages [4] -->
m

<!-- b001017 | prose | pages [4] -->
m

<!-- b001018 | heading | pages [4] -->
3. Certain countries are likely to win Olympic medals for the first time in 2028, and

<!-- b001019 | prose | pages [4] -->
m

<!-- b001020 | prose | pages [4] -->
m

<!-- b001021 | prose | pages [4] -->
m

<!-- b001022 | prose | pages [4] -->
m

<!-- b001023 | prose | pages [4] -->
m

<!-- b001024 | prose | pages [4] -->
m

<!-- b001025 | prose | pages [4] -->
m

<!-- b001026 | prose | pages [4] -->
m

<!-- b001027 | prose | pages [4] -->
m

<!-- b001028 | prose | pages [4] -->
m

<!-- b001029 | prose | pages [4] -->
m

<!-- b001030 | prose | pages [4] -->
m

<!-- b001031 | prose | pages [4] -->
m

<!-- b001032 | prose | pages [4] -->
m

<!-- b001033 | prose | pages [4] -->
m

<!-- b001034 | prose | pages [4] -->
m

<!-- b001035 | prose | pages [4] -->
m

<!-- b001036 | prose | pages [4] -->
m

<!-- b001037 | prose | pages [4] -->
m

<!-- b001038 | prose | pages [4] -->
m

<!-- b001039 | prose | pages [4] -->
m

<!-- b001040 | prose | pages [4] -->
m

<!-- b001041 | prose | pages [4] -->
m

<!-- b001042 | prose | pages [4] -->
m

<!-- b001043 | prose | pages [4] -->
m

<!-- b001044 | prose | pages [4] -->
m

<!-- b001045 | prose | pages [4] -->
m

<!-- b001046 | prose | pages [4] -->
m

<!-- b001047 | prose | pages [4] -->
m

<!-- b001048 | prose | pages [4] -->
m

<!-- b001049 | prose | pages [4] -->
m

<!-- b001050 | prose | pages [4] -->
m

<!-- b001051 | prose | pages [4] -->
m

<!-- b001052 | prose | pages [4] -->
m

<!-- b001053 | prose | pages [4] -->
m

<!-- b001054 | prose | pages [4] -->
m

<!-- b001055 | prose | pages [4] -->
m

<!-- b001056 | prose | pages [4] -->
m

<!-- b001057 | prose | pages [4] -->
m

<!-- b001058 | prose | pages [4] -->
m

<!-- b001059 | prose | pages [4] -->
m

<!-- b001060 | prose | pages [4] -->
m

<!-- b001061 | prose | pages [4] -->
m

<!-- b001062 | prose | pages [4] -->
m

<!-- b001063 | prose | pages [4] -->
m

<!-- b001064 | prose | pages [4] -->
m

<!-- b001065 | prose | pages [4] -->
m

<!-- b001066 | prose | pages [4] -->
m

<!-- b001067 | prose | pages [4] -->
m

<!-- b001068 | prose | pages [4] -->
m

<!-- b001069 | prose | pages [4] -->
m

<!-- b001070 | prose | pages [4] -->
m

<!-- b001071 | prose | pages [4] -->
m

<!-- b001072 | prose | pages [4] -->
m

<!-- b001073 | prose | pages [4] -->
m

<!-- b001074 | prose | pages [4] -->
m

<!-- b001075 | prose | pages [4] -->
m

<!-- b001076 | prose | pages [4] -->
m

<!-- b001077 | prose | pages [4] -->
m

<!-- b001078 | prose | pages [4] -->
m

<!-- b001079 | prose | pages [4] -->
m

<!-- b001080 | prose | pages [4] -->
m

<!-- b001081 | prose | pages [4] -->
m

<!-- b001082 | prose | pages [4] -->
m

<!-- b001083 | prose | pages [4] -->
m

<!-- b001084 | prose | pages [4] -->
m

<!-- b001085 | prose | pages [4] -->
m

<!-- b001086 | prose | pages [4] -->
m

<!-- b001087 | prose | pages [4] -->
m

<!-- b001088 | prose | pages [4] -->
m

<!-- b001089 | prose | pages [4] -->
m

<!-- b001090 | prose | pages [4] -->
m

<!-- b001091 | prose | pages [4] -->
m

<!-- b001092 | prose | pages [4] -->
m

<!-- b001093 | prose | pages [4] -->
m

<!-- b001094 | prose | pages [4] -->
m

<!-- b001095 | prose | pages [4] -->
m

<!-- b001096 | prose | pages [4] -->
m

<!-- b001097 | prose | pages [4] -->
m

<!-- b001098 | prose | pages [4] -->
m

<!-- b001099 | prose | pages [4] -->
m

<!-- b001100 | prose | pages [4] -->
m

<!-- b001101 | prose | pages [4] -->
m

<!-- b001102 | prose | pages [4] -->
m

<!-- b001103 | prose | pages [4] -->
m

<!-- b001104 | prose | pages [4] -->
m

<!-- b001105 | prose | pages [4] -->
m

<!-- b001106 | prose | pages [4] -->
m

<!-- b001107 | prose | pages [4] -->
m

<!-- b001108 | prose | pages [4] -->
m

<!-- b001109 | prose | pages [4] -->
m

<!-- b001110 | prose | pages [4] -->
m

<!-- b001111 | prose | pages [4] -->
m

<!-- b001112 | prose | pages [4] -->
m

<!-- b001113 | prose | pages [4] -->
m

<!-- b001114 | prose | pages [4] -->
m m

<!-- b001115 | prose | pages [4] -->
m m

<!-- b001116 | prose | pages [4] -->
m

<!-- b001117 | prose | pages [4] -->
m m

<!-- b001118 | prose | pages [4] -->
m m

<!-- b001119 | prose | pages [4] -->
m m

<!-- b001120 | prose | pages [4] -->
m m

<!-- b001121 | prose | pages [4] -->
m m

<!-- b001122 | prose | pages [4] -->
m m

<!-- b001123 | prose | pages [4] -->
m

<!-- b001124 | prose | pages [4] -->
m m

<!-- b001125 | prose | pages [4] -->
m m

<!-- b001126 | prose | pages [4] -->
m m

<!-- b001127 | prose | pages [4] -->
m m

<!-- b001128 | prose | pages [4] -->
m

<!-- b001129 | prose | pages [4] -->
m

<!-- b001130 | prose | pages [4] -->
m m

<!-- b001131 | prose | pages [4] -->
m m

<!-- b001132 | prose | pages [4] -->
m m

<!-- b001133 | prose | pages [4] -->
m

<!-- b001134 | prose | pages [4] -->
m

<!-- b001135 | prose | pages [4] -->
m

<!-- b001136 | prose | pages [4] -->
m

<!-- b001137 | prose | pages [4] -->
m m

<!-- b001138 | prose | pages [4] -->
m m

<!-- b001139 | prose | pages [4] -->
m m

<!-- b001140 | prose | pages [4] -->
m m

<!-- b001141 | prose | pages [4] -->
m m

<!-- b001142 | prose | pages [4] -->
m

<!-- b001143 | prose | pages [4] -->
m

<!-- b001144 | prose | pages [4] -->
m

<!-- b001145 | prose | pages [4] -->
m m

<!-- b001146 | prose | pages [4] -->
m m

<!-- b001147 | prose | pages [4] -->
m m

<!-- b001148 | prose | pages [4] -->
m

<!-- b001149 | prose | pages [4] -->
m

<!-- b001150 | prose | pages [4] -->
m m

<!-- b001151 | prose | pages [4] -->
m m

<!-- b001152 | prose | pages [4] -->
m m

<!-- b001153 | prose | pages [4] -->
m m

<!-- b001154 | prose | pages [4] -->
m m

<!-- b001155 | prose | pages [4] -->
m m

<!-- b001156 | prose | pages [4] -->
m

<!-- b001157 | prose | pages [4] -->
m m

<!-- b001158 | prose | pages [4] -->
m m

<!-- b001159 | prose | pages [4] -->
m m

<!-- b001160 | prose | pages [4] -->
m m

<!-- b001161 | prose | pages [4] -->
m m

<!-- b001162 | prose | pages [4] -->
m

<!-- b001163 | prose | pages [4] -->
m

<!-- b001164 | prose | pages [4] -->
sports that have historically had a high number of first-time winners from other

<!-- b001165 | prose | pages [4] -->
m

<!-- b001166 | prose | pages [4] -->
m

<!-- b001167 | prose | pages [4] -->
m

<!-- b001168 | prose | pages [4] -->
m

<!-- b001169 | prose | pages [4] -->
m

<!-- b001170 | prose | pages [4] -->
m

<!-- b001171 | prose | pages [4] -->
m

<!-- b001172 | prose | pages [4] -->
m

<!-- b001173 | prose | pages [4] -->
m

<!-- b001174 | prose | pages [4] -->
m

<!-- b001175 | prose | pages [4] -->
m

<!-- b001176 | prose | pages [4] -->
m

<!-- b001177 | prose | pages [4] -->
m

<!-- b001178 | prose | pages [4] -->
m

<!-- b001179 | prose | pages [4] -->
m

<!-- b001180 | prose | pages [4] -->
m

<!-- b001181 | prose | pages [4] -->
m

<!-- b001182 | prose | pages [4] -->
m

<!-- b001183 | prose | pages [4] -->
m

<!-- b001184 | prose | pages [4] -->
m

<!-- b001185 | prose | pages [4] -->
m

<!-- b001186 | prose | pages [4] -->
m

<!-- b001187 | prose | pages [4] -->
m

<!-- b001188 | prose | pages [4] -->
m

<!-- b001189 | prose | pages [4] -->
m

<!-- b001190 | prose | pages [4] -->
m

<!-- b001191 | prose | pages [4] -->
m

<!-- b001192 | prose | pages [4] -->
m

<!-- b001193 | prose | pages [4] -->
m

<!-- b001194 | prose | pages [4] -->
m

<!-- b001195 | prose | pages [4] -->
m

<!-- b001196 | prose | pages [4] -->
m

<!-- b001197 | prose | pages [4] -->
m

<!-- b001198 | prose | pages [4] -->
m

<!-- b001199 | prose | pages [4] -->
m

<!-- b001200 | prose | pages [4] -->
m

<!-- b001201 | prose | pages [4] -->
m

<!-- b001202 | prose | pages [4] -->
m

<!-- b001203 | prose | pages [4] -->
m

<!-- b001204 | prose | pages [4] -->
m

<!-- b001205 | prose | pages [4] -->
m

<!-- b001206 | prose | pages [4] -->
m

<!-- b001207 | prose | pages [4] -->
m

<!-- b001208 | prose | pages [4] -->
m

<!-- b001209 | prose | pages [4] -->
m

<!-- b001210 | prose | pages [4] -->
m

<!-- b001211 | prose | pages [4] -->
m

<!-- b001212 | prose | pages [4] -->
m

<!-- b001213 | prose | pages [4] -->
m

<!-- b001214 | prose | pages [4] -->
m

<!-- b001215 | prose | pages [4] -->
m

<!-- b001216 | prose | pages [4] -->
m

<!-- b001217 | prose | pages [4] -->
m

<!-- b001218 | prose | pages [4] -->
m

<!-- b001219 | prose | pages [4] -->
m

<!-- b001220 | prose | pages [4] -->
m

<!-- b001221 | prose | pages [4] -->
m

<!-- b001222 | prose | pages [4] -->
m

<!-- b001223 | prose | pages [4] -->
m

<!-- b001224 | prose | pages [4] -->
m

<!-- b001225 | prose | pages [4] -->
m

<!-- b001226 | prose | pages [4] -->
m

<!-- b001227 | prose | pages [4] -->
m

<!-- b001228 | prose | pages [4] -->
m

<!-- b001229 | prose | pages [4] -->
m

<!-- b001230 | prose | pages [4] -->
m

<!-- b001231 | prose | pages [4] -->
m

<!-- b001232 | prose | pages [4] -->
m

<!-- b001233 | prose | pages [4] -->
m

<!-- b001234 | prose | pages [4] -->
m

<!-- b001235 | prose | pages [4] -->
m

<!-- b001236 | prose | pages [4] -->
m

<!-- b001237 | prose | pages [4] -->
m

<!-- b001238 | prose | pages [4] -->
m

<!-- b001239 | prose | pages [4] -->
m

<!-- b001240 | prose | pages [4] -->
m

<!-- b001241 | prose | pages [4] -->
m

<!-- b001242 | prose | pages [4] -->
m

<!-- b001243 | prose | pages [4] -->
m

<!-- b001244 | prose | pages [4] -->
m

<!-- b001245 | prose | pages [4] -->
m

<!-- b001246 | prose | pages [4] -->
m

<!-- b001247 | prose | pages [4] -->
m

<!-- b001248 | prose | pages [4] -->
m

<!-- b001249 | prose | pages [4] -->
m

<!-- b001250 | prose | pages [4] -->
m

<!-- b001251 | prose | pages [4] -->
m

<!-- b001252 | prose | pages [4] -->
m

<!-- b001253 | prose | pages [4] -->
m

<!-- b001254 | prose | pages [4] -->
m

<!-- b001255 | prose | pages [4] -->
m

<!-- b001256 | prose | pages [4] -->
m

<!-- b001257 | prose | pages [4] -->
m

<!-- b001258 | prose | pages [4] -->
m

<!-- b001259 | prose | pages [4] -->
m m

<!-- b001260 | prose | pages [4] -->
m m

<!-- b001261 | prose | pages [4] -->
m m

<!-- b001262 | prose | pages [4] -->
m

<!-- b001263 | prose | pages [4] -->
m

<!-- b001264 | prose | pages [4] -->
m

<!-- b001265 | prose | pages [4] -->
m m

<!-- b001266 | prose | pages [4] -->
m m

<!-- b001267 | prose | pages [4] -->
m m

<!-- b001268 | prose | pages [4] -->
m m

<!-- b001269 | prose | pages [4] -->
m

<!-- b001270 | prose | pages [4] -->
m m

<!-- b001271 | prose | pages [4] -->
m m

<!-- b001272 | prose | pages [4] -->
m m

<!-- b001273 | prose | pages [4] -->
m m

<!-- b001274 | prose | pages [4] -->
m

<!-- b001275 | prose | pages [4] -->
m m

<!-- b001276 | prose | pages [4] -->
m m

<!-- b001277 | prose | pages [4] -->
m m

<!-- b001278 | prose | pages [4] -->
m

<!-- b001279 | prose | pages [4] -->
m

<!-- b001280 | prose | pages [4] -->
m m

<!-- b001281 | prose | pages [4] -->
m m

<!-- b001282 | prose | pages [4] -->
m m

<!-- b001283 | prose | pages [4] -->
m

<!-- b001284 | prose | pages [4] -->
m

<!-- b001285 | prose | pages [4] -->
m

<!-- b001286 | prose | pages [4] -->
m m

<!-- b001287 | prose | pages [4] -->
m m

<!-- b001288 | prose | pages [4] -->
m m

<!-- b001289 | prose | pages [4] -->
m m

<!-- b001290 | prose | pages [4] -->
m

<!-- b001291 | prose | pages [4] -->
m

<!-- b001292 | prose | pages [4] -->
m

<!-- b001293 | prose | pages [4] -->
m m

<!-- b001294 | prose | pages [4] -->
m m

<!-- b001295 | prose | pages [4] -->
m m

<!-- b001296 | prose | pages [4] -->
m m

<!-- b001297 | prose | pages [4] -->
m m

<!-- b001298 | prose | pages [4] -->
m

<!-- b001299 | prose | pages [4] -->
m

<!-- b001300 | prose | pages [4] -->
m

<!-- b001301 | prose | pages [4] -->
m

<!-- b001302 | prose | pages [4] -->
countries are also relatively more likely to win for the first time.

<!-- b001303 | prose | pages [4] -->
m

<!-- b001304 | prose | pages [4] -->
m

<!-- b001305 | prose | pages [4] -->
m

<!-- b001306 | prose | pages [4] -->
m

<!-- b001307 | prose | pages [4] -->
m

<!-- b001308 | prose | pages [4] -->
m

<!-- b001309 | prose | pages [4] -->
m

<!-- b001310 | prose | pages [4] -->
m

<!-- b001311 | prose | pages [4] -->
m

<!-- b001312 | prose | pages [4] -->
m

<!-- b001313 | prose | pages [4] -->
m

<!-- b001314 | prose | pages [4] -->
m

<!-- b001315 | prose | pages [4] -->
m

<!-- b001316 | prose | pages [4] -->
m

<!-- b001317 | prose | pages [4] -->
m

<!-- b001318 | prose | pages [4] -->
m

<!-- b001319 | prose | pages [4] -->
m

<!-- b001320 | prose | pages [4] -->
m

<!-- b001321 | prose | pages [4] -->
m

<!-- b001322 | prose | pages [4] -->
m

<!-- b001323 | prose | pages [4] -->
m

<!-- b001324 | prose | pages [4] -->
m

<!-- b001325 | prose | pages [4] -->
m

<!-- b001326 | prose | pages [4] -->
m

<!-- b001327 | prose | pages [4] -->
m

<!-- b001328 | prose | pages [4] -->
m

<!-- b001329 | prose | pages [4] -->
m

<!-- b001330 | prose | pages [4] -->
m

<!-- b001331 | prose | pages [4] -->
m

<!-- b001332 | prose | pages [4] -->
m

<!-- b001333 | prose | pages [4] -->
m

<!-- b001334 | prose | pages [4] -->
m

<!-- b001335 | prose | pages [4] -->
m

<!-- b001336 | prose | pages [4] -->
m

<!-- b001337 | prose | pages [4] -->
m

<!-- b001338 | prose | pages [4] -->
m

<!-- b001339 | prose | pages [4] -->
m

<!-- b001340 | prose | pages [4] -->
m

<!-- b001341 | prose | pages [4] -->
m

<!-- b001342 | prose | pages [4] -->
m

<!-- b001343 | prose | pages [4] -->
m

<!-- b001344 | prose | pages [4] -->
m

<!-- b001345 | prose | pages [4] -->
m

<!-- b001346 | prose | pages [4] -->
m

<!-- b001347 | prose | pages [4] -->
m

<!-- b001348 | prose | pages [4] -->
m

<!-- b001349 | prose | pages [4] -->
m

<!-- b001350 | prose | pages [4] -->
m

<!-- b001351 | prose | pages [4] -->
m

<!-- b001352 | prose | pages [4] -->
m

<!-- b001353 | prose | pages [4] -->
m

<!-- b001354 | prose | pages [4] -->
m

<!-- b001355 | prose | pages [4] -->
m

<!-- b001356 | prose | pages [4] -->
m

<!-- b001357 | prose | pages [4] -->
m

<!-- b001358 | prose | pages [4] -->
m

<!-- b001359 | prose | pages [4] -->
m

<!-- b001360 | prose | pages [4] -->
m

<!-- b001361 | prose | pages [4] -->
m

<!-- b001362 | prose | pages [4] -->
m

<!-- b001363 | prose | pages [4] -->
m

<!-- b001364 | prose | pages [4] -->
m

<!-- b001365 | prose | pages [4] -->
m

<!-- b001366 | prose | pages [4] -->
m

<!-- b001367 | prose | pages [4] -->
m

<!-- b001368 | prose | pages [4] -->
m

<!-- b001369 | prose | pages [4] -->
m

<!-- b001370 | prose | pages [4] -->
m

<!-- b001371 | prose | pages [4] -->
m

<!-- b001372 | prose | pages [4] -->
m

<!-- b001373 | prose | pages [4] -->
m

<!-- b001374 | prose | pages [4] -->
m

<!-- b001375 | prose | pages [4] -->
m

<!-- b001376 | prose | pages [4] -->
m

<!-- b001377 | prose | pages [4] -->
m

<!-- b001378 | prose | pages [4] -->
m

<!-- b001379 | prose | pages [4] -->
m

<!-- b001380 | prose | pages [4] -->
m

<!-- b001381 | prose | pages [4] -->
m m

<!-- b001382 | prose | pages [4] -->
m m

<!-- b001383 | prose | pages [4] -->
m m

<!-- b001384 | prose | pages [4] -->
m m

<!-- b001385 | prose | pages [4] -->
m

<!-- b001386 | prose | pages [4] -->
m m

<!-- b001387 | prose | pages [4] -->
m m

<!-- b001388 | prose | pages [4] -->
m m

<!-- b001389 | prose | pages [4] -->
m m

<!-- b001390 | prose | pages [4] -->
m m

<!-- b001391 | prose | pages [4] -->
m m

<!-- b001392 | prose | pages [4] -->
m

<!-- b001393 | prose | pages [4] -->
m

<!-- b001394 | prose | pages [4] -->
m

<!-- b001395 | prose | pages [4] -->
m m

<!-- b001396 | prose | pages [4] -->
m m

<!-- b001397 | prose | pages [4] -->
m m

<!-- b001398 | prose | pages [4] -->
m m

<!-- b001399 | prose | pages [4] -->
m m

<!-- b001400 | prose | pages [4] -->
m

<!-- b001401 | prose | pages [4] -->
m

<!-- b001402 | prose | pages [4] -->
m

<!-- b001403 | prose | pages [4] -->
m m

<!-- b001404 | prose | pages [4] -->
m m

<!-- b001405 | prose | pages [4] -->
m m

<!-- b001406 | prose | pages [4] -->
m m

<!-- b001407 | prose | pages [4] -->
m

<!-- b001408 | prose | pages [4] -->
m

<!-- b001409 | prose | pages [4] -->
m

<!-- b001410 | prose | pages [4] -->
m m

<!-- b001411 | prose | pages [4] -->
m m

<!-- b001412 | prose | pages [4] -->
m m

<!-- b001413 | prose | pages [4] -->
m m

<!-- b001414 | prose | pages [4] -->
m

<!-- b001415 | prose | pages [4] -->
m m

<!-- b001416 | prose | pages [4] -->
m m

<!-- b001417 | prose | pages [4] -->
m m

<!-- b001418 | prose | pages [4] -->
m m

<!-- b001419 | prose | pages [4] -->
m m

<!-- b001420 | prose | pages [4] -->
m

<!-- b001421 | prose | pages [4] -->
m

<!-- b001422 | prose | pages [4] -->
m

<!-- b001423 | prose | pages [4] -->
m

<!-- b001424 | prose | pages [4] -->
Based on past history, certain sports are typically more likely to be breakthroughs for

<!-- b001425 | prose | pages [4] -->
关注数学模型

<!-- b001426 | furniture | pages [4] -->
2

<!-- b001427 | furniture | pages [4] -->
MATHmodels

<!-- b001428 | furniture | pages [4] -->
获取更多资讯

<!-- b001429 | furniture | pages [5] -->
Team # 2510862

<!-- b001430 | furniture | pages [5] -->
Page 5 of 25

<!-- b001431 | prose | pages [5] -->
微信公众号：数学模型

<!-- b001432 | prose | pages [5] -->
first-time medal-winning countries, particularly among emerging or less competi- tive countries. These sports have lower thresholds, more opportunities to compete, and can offer potential winning opportunities for countries that have not historically won an Olympic medal.

<!-- b001433 | heading | pages [5] -->
4. The effects of coaching do not diminish or enhance over time, but rather are main-

<!-- b001434 | prose | pages [5] -->
tained at a stable level that influences athletes’ performance over time. Specifically, we argue that the effects of coaching in terms of tactical instruction, technical enhancement, and psychological motivation will remain stable through- out an athlete’s career and have a sustained positive effect on his or her Olympic performance. This influence does not diminish as the athlete gains experience or

<!-- b001435 | prose | pages [5] -->
微信号：MATHmodels

<!-- b001436 | prose | pages [5] -->
changes in competitive status. For example, a coach’s training methods and strate- gic philosophy can still have a positive impact on an athlete in the long term, despite changes in age or fitness.

<!-- b001437 | prose | pages [5] -->
3

<!-- b001438 | heading | pages [5] -->
Notations

<!-- b001439 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b001440 | heading | pages [5] -->
Symbol

<!-- b001441 | prose | pages [5] -->
Description

<!-- b001442 | prose | pages [5] -->
Features of the attribute xj

<!-- b001443 | prose | pages [5] -->
The regularization term that penalizes model complexity Ω(f)

<!-- b001444 | prose | pages [5] -->
Slack variables represent the allowed tolerance for each data point ξi

<!-- b001445 | prose | pages [5] -->
The learned weights for each base learner αi

<!-- b001446 | prose | pages [5] -->
Parameters to be estimated β

<!-- b001447 | prose | pages [5] -->
Random error term ϵit

<!-- b001448 | prose | pages [5] -->
Policy dummy variable ri

<!-- b001449 | prose | pages [5] -->
4 Data Pre-processing

<!-- b001450 | prose | pages [5] -->
• Step 1: Special Data Handling Firstly, we deal with data format inconsistencies. In the summerOly_athletes.csv file, there were duplicate event names in the Sports column (Cycling Road, Cycling Track; Cycling Road, Triathlon), which were merged into the larger category, and there were multiple teams from the same country in the Team column, which were correctly grouped together. For example: Argentina-1, Argentina-2, they have been correctly grouped together. In addition, the historical data for Russia (RUS) and Russia 2020 (ROC), even though Russia has already missed the 2024 Olympics for other reasons and may continue to miss the 2028 Olympics, is informative, so we merged them and kept their data, but they are not involved in the subsequent medal predictions.

<!-- b001451 | prose | pages [5] -->
• Step 2: Mapping the ’Team’ column to ’NOC’ We mapped the ’Team’ column (containing the full name of the country) in the sum-

<!-- b001452 | prose | pages [5] -->
m

<!-- b001453 | prose | pages [5] -->
m

<!-- b001454 | prose | pages [5] -->
m

<!-- b001455 | prose | pages [5] -->
m

<!-- b001456 | prose | pages [5] -->
m

<!-- b001457 | prose | pages [5] -->
m

<!-- b001458 | prose | pages [5] -->
m

<!-- b001459 | prose | pages [5] -->
m

<!-- b001460 | prose | pages [5] -->
m

<!-- b001461 | prose | pages [5] -->
m

<!-- b001462 | prose | pages [5] -->
m

<!-- b001463 | prose | pages [5] -->
m

<!-- b001464 | prose | pages [5] -->
m

<!-- b001465 | prose | pages [5] -->
m

<!-- b001466 | prose | pages [5] -->
m

<!-- b001467 | prose | pages [5] -->
m

<!-- b001468 | prose | pages [5] -->
m

<!-- b001469 | prose | pages [5] -->
m

<!-- b001470 | prose | pages [5] -->
m

<!-- b001471 | prose | pages [5] -->
m

<!-- b001472 | prose | pages [5] -->
m

<!-- b001473 | prose | pages [5] -->
m

<!-- b001474 | prose | pages [5] -->
m

<!-- b001475 | prose | pages [5] -->
m

<!-- b001476 | prose | pages [5] -->
m

<!-- b001477 | prose | pages [5] -->
m

<!-- b001478 | prose | pages [5] -->
m

<!-- b001479 | prose | pages [5] -->
m

<!-- b001480 | prose | pages [5] -->
m

<!-- b001481 | prose | pages [5] -->
m

<!-- b001482 | prose | pages [5] -->
m

<!-- b001483 | prose | pages [5] -->
m

<!-- b001484 | prose | pages [5] -->
m

<!-- b001485 | prose | pages [5] -->
m

<!-- b001486 | prose | pages [5] -->
m

<!-- b001487 | prose | pages [5] -->
m

<!-- b001488 | prose | pages [5] -->
m

<!-- b001489 | prose | pages [5] -->
m

<!-- b001490 | prose | pages [5] -->
m

<!-- b001491 | prose | pages [5] -->
m

<!-- b001492 | prose | pages [5] -->
m

<!-- b001493 | prose | pages [5] -->
m

<!-- b001494 | prose | pages [5] -->
m

<!-- b001495 | prose | pages [5] -->
m

<!-- b001496 | prose | pages [5] -->
m

<!-- b001497 | prose | pages [5] -->
m

<!-- b001498 | prose | pages [5] -->
m

<!-- b001499 | prose | pages [5] -->
m

<!-- b001500 | prose | pages [5] -->
m

<!-- b001501 | prose | pages [5] -->
m

<!-- b001502 | prose | pages [5] -->
m

<!-- b001503 | prose | pages [5] -->
m

<!-- b001504 | prose | pages [5] -->
m

<!-- b001505 | prose | pages [5] -->
m

<!-- b001506 | prose | pages [5] -->
m

<!-- b001507 | prose | pages [5] -->
m

<!-- b001508 | prose | pages [5] -->
m

<!-- b001509 | prose | pages [5] -->
m

<!-- b001510 | prose | pages [5] -->
m

<!-- b001511 | prose | pages [5] -->
m

<!-- b001512 | prose | pages [5] -->
m

<!-- b001513 | prose | pages [5] -->
m

<!-- b001514 | prose | pages [5] -->
m

<!-- b001515 | prose | pages [5] -->
m

<!-- b001516 | prose | pages [5] -->
m

<!-- b001517 | prose | pages [5] -->
m

<!-- b001518 | prose | pages [5] -->
m

<!-- b001519 | prose | pages [5] -->
m

<!-- b001520 | prose | pages [5] -->
m

<!-- b001521 | prose | pages [5] -->
m

<!-- b001522 | prose | pages [5] -->
m

<!-- b001523 | prose | pages [5] -->
m

<!-- b001524 | prose | pages [5] -->
m

<!-- b001525 | prose | pages [5] -->
m

<!-- b001526 | prose | pages [5] -->
m

<!-- b001527 | prose | pages [5] -->
m

<!-- b001528 | prose | pages [5] -->
m

<!-- b001529 | prose | pages [5] -->
m

<!-- b001530 | prose | pages [5] -->
m

<!-- b001531 | prose | pages [5] -->
m

<!-- b001532 | prose | pages [5] -->
m

<!-- b001533 | prose | pages [5] -->
m

<!-- b001534 | prose | pages [5] -->
m

<!-- b001535 | prose | pages [5] -->
m

<!-- b001536 | prose | pages [5] -->
m

<!-- b001537 | prose | pages [5] -->
m

<!-- b001538 | prose | pages [5] -->
m

<!-- b001539 | prose | pages [5] -->
m

<!-- b001540 | prose | pages [5] -->
m

<!-- b001541 | prose | pages [5] -->
m

<!-- b001542 | prose | pages [5] -->
m

<!-- b001543 | prose | pages [5] -->
m

<!-- b001544 | prose | pages [5] -->
m

<!-- b001545 | prose | pages [5] -->
m

<!-- b001546 | prose | pages [5] -->
m

<!-- b001547 | prose | pages [5] -->
m

<!-- b001548 | prose | pages [5] -->
m

<!-- b001549 | prose | pages [5] -->
m

<!-- b001550 | prose | pages [5] -->
m

<!-- b001551 | prose | pages [5] -->
m

<!-- b001552 | prose | pages [5] -->
m

<!-- b001553 | prose | pages [5] -->
m

<!-- b001554 | prose | pages [5] -->
m

<!-- b001555 | prose | pages [5] -->
m

<!-- b001556 | prose | pages [5] -->
m

<!-- b001557 | prose | pages [5] -->
m

<!-- b001558 | prose | pages [5] -->
m

<!-- b001559 | prose | pages [5] -->
m

<!-- b001560 | prose | pages [5] -->
m

<!-- b001561 | prose | pages [5] -->
m

<!-- b001562 | prose | pages [5] -->
m

<!-- b001563 | prose | pages [5] -->
m

<!-- b001564 | prose | pages [5] -->
m

<!-- b001565 | prose | pages [5] -->
m

<!-- b001566 | prose | pages [5] -->
m

<!-- b001567 | prose | pages [5] -->
m

<!-- b001568 | prose | pages [5] -->
m

<!-- b001569 | prose | pages [5] -->
m

<!-- b001570 | prose | pages [5] -->
m

<!-- b001571 | prose | pages [5] -->
m

<!-- b001572 | prose | pages [5] -->
m

<!-- b001573 | prose | pages [5] -->
m

<!-- b001574 | prose | pages [5] -->
m

<!-- b001575 | prose | pages [5] -->
m

<!-- b001576 | prose | pages [5] -->
m

<!-- b001577 | prose | pages [5] -->
m

<!-- b001578 | prose | pages [5] -->
m

<!-- b001579 | prose | pages [5] -->
m

<!-- b001580 | prose | pages [5] -->
m

<!-- b001581 | prose | pages [5] -->
m

<!-- b001582 | prose | pages [5] -->
m

<!-- b001583 | prose | pages [5] -->
m

<!-- b001584 | prose | pages [5] -->
m

<!-- b001585 | prose | pages [5] -->
m

<!-- b001586 | prose | pages [5] -->
m

<!-- b001587 | prose | pages [5] -->
m

<!-- b001588 | prose | pages [5] -->
m

<!-- b001589 | prose | pages [5] -->
m

<!-- b001590 | prose | pages [5] -->
m

<!-- b001591 | prose | pages [5] -->
m

<!-- b001592 | prose | pages [5] -->
m

<!-- b001593 | prose | pages [5] -->
m

<!-- b001594 | prose | pages [5] -->
m

<!-- b001595 | prose | pages [5] -->
m

<!-- b001596 | prose | pages [5] -->
m

<!-- b001597 | prose | pages [5] -->
m

<!-- b001598 | prose | pages [5] -->
m

<!-- b001599 | prose | pages [5] -->
m

<!-- b001600 | prose | pages [5] -->
m

<!-- b001601 | prose | pages [5] -->
m

<!-- b001602 | prose | pages [5] -->
m

<!-- b001603 | prose | pages [5] -->
m

<!-- b001604 | prose | pages [5] -->
m

<!-- b001605 | prose | pages [5] -->
m

<!-- b001606 | prose | pages [5] -->
m

<!-- b001607 | prose | pages [5] -->
m

<!-- b001608 | prose | pages [5] -->
m

<!-- b001609 | prose | pages [5] -->
m

<!-- b001610 | prose | pages [5] -->
m

<!-- b001611 | prose | pages [5] -->
m

<!-- b001612 | prose | pages [5] -->
m

<!-- b001613 | prose | pages [5] -->
m

<!-- b001614 | prose | pages [5] -->
m

<!-- b001615 | prose | pages [5] -->
m

<!-- b001616 | prose | pages [5] -->
m

<!-- b001617 | prose | pages [5] -->
m

<!-- b001618 | prose | pages [5] -->
m

<!-- b001619 | prose | pages [5] -->
m

<!-- b001620 | prose | pages [5] -->
m

<!-- b001621 | prose | pages [5] -->
m

<!-- b001622 | prose | pages [5] -->
m

<!-- b001623 | prose | pages [5] -->
m

<!-- b001624 | prose | pages [5] -->
m

<!-- b001625 | prose | pages [5] -->
m

<!-- b001626 | prose | pages [5] -->
m

<!-- b001627 | prose | pages [5] -->
m

<!-- b001628 | prose | pages [5] -->
m

<!-- b001629 | prose | pages [5] -->
m

<!-- b001630 | prose | pages [5] -->
m

<!-- b001631 | prose | pages [5] -->
m

<!-- b001632 | prose | pages [5] -->
m

<!-- b001633 | prose | pages [5] -->
m

<!-- b001634 | prose | pages [5] -->
m

<!-- b001635 | prose | pages [5] -->
m

<!-- b001636 | prose | pages [5] -->
m

<!-- b001637 | prose | pages [5] -->
m

<!-- b001638 | prose | pages [5] -->
m

<!-- b001639 | prose | pages [5] -->
m

<!-- b001640 | prose | pages [5] -->
m

<!-- b001641 | prose | pages [5] -->
m

<!-- b001642 | prose | pages [5] -->
m

<!-- b001643 | prose | pages [5] -->
m

<!-- b001644 | prose | pages [5] -->
m

<!-- b001645 | prose | pages [5] -->
m

<!-- b001646 | prose | pages [5] -->
m

<!-- b001647 | prose | pages [5] -->
m

<!-- b001648 | prose | pages [5] -->
m

<!-- b001649 | prose | pages [5] -->
m

<!-- b001650 | prose | pages [5] -->
m

<!-- b001651 | prose | pages [5] -->
m

<!-- b001652 | prose | pages [5] -->
m

<!-- b001653 | prose | pages [5] -->
m

<!-- b001654 | prose | pages [5] -->
m

<!-- b001655 | prose | pages [5] -->
m

<!-- b001656 | prose | pages [5] -->
m

<!-- b001657 | prose | pages [5] -->
m

<!-- b001658 | prose | pages [5] -->
m

<!-- b001659 | prose | pages [5] -->
m

<!-- b001660 | prose | pages [5] -->
m

<!-- b001661 | prose | pages [5] -->
m

<!-- b001662 | prose | pages [5] -->
m

<!-- b001663 | prose | pages [5] -->
m

<!-- b001664 | prose | pages [5] -->
m

<!-- b001665 | prose | pages [5] -->
m

<!-- b001666 | prose | pages [5] -->
m

<!-- b001667 | prose | pages [5] -->
m

<!-- b001668 | prose | pages [5] -->
m

<!-- b001669 | prose | pages [5] -->
m

<!-- b001670 | prose | pages [5] -->
m

<!-- b001671 | prose | pages [5] -->
m

<!-- b001672 | prose | pages [5] -->
m

<!-- b001673 | prose | pages [5] -->
m

<!-- b001674 | prose | pages [5] -->
m

<!-- b001675 | prose | pages [5] -->
m

<!-- b001676 | prose | pages [5] -->
m

<!-- b001677 | prose | pages [5] -->
m

<!-- b001678 | prose | pages [5] -->
m

<!-- b001679 | prose | pages [5] -->
m

<!-- b001680 | prose | pages [5] -->
m

<!-- b001681 | prose | pages [5] -->
m

<!-- b001682 | prose | pages [5] -->
m

<!-- b001683 | prose | pages [5] -->
m

<!-- b001684 | prose | pages [5] -->
m

<!-- b001685 | prose | pages [5] -->
m

<!-- b001686 | prose | pages [5] -->
m

<!-- b001687 | prose | pages [5] -->
m

<!-- b001688 | prose | pages [5] -->
m

<!-- b001689 | prose | pages [5] -->
m

<!-- b001690 | prose | pages [5] -->
m

<!-- b001691 | prose | pages [5] -->
m

<!-- b001692 | prose | pages [5] -->
m

<!-- b001693 | prose | pages [5] -->
m

<!-- b001694 | prose | pages [5] -->
m

<!-- b001695 | prose | pages [5] -->
m

<!-- b001696 | prose | pages [5] -->
m

<!-- b001697 | prose | pages [5] -->
m

<!-- b001698 | prose | pages [5] -->
m

<!-- b001699 | prose | pages [5] -->
m

<!-- b001700 | prose | pages [5] -->
m

<!-- b001701 | prose | pages [5] -->
m

<!-- b001702 | prose | pages [5] -->
m

<!-- b001703 | prose | pages [5] -->
m

<!-- b001704 | prose | pages [5] -->
m

<!-- b001705 | prose | pages [5] -->
m

<!-- b001706 | prose | pages [5] -->
m

<!-- b001707 | prose | pages [5] -->
m

<!-- b001708 | prose | pages [5] -->
m

<!-- b001709 | prose | pages [5] -->
m

<!-- b001710 | prose | pages [5] -->
m

<!-- b001711 | prose | pages [5] -->
m

<!-- b001712 | prose | pages [5] -->
m

<!-- b001713 | prose | pages [5] -->
m

<!-- b001714 | prose | pages [5] -->
m

<!-- b001715 | prose | pages [5] -->
m

<!-- b001716 | prose | pages [5] -->
m

<!-- b001717 | prose | pages [5] -->
m

<!-- b001718 | prose | pages [5] -->
m

<!-- b001719 | prose | pages [5] -->
m

<!-- b001720 | prose | pages [5] -->
m

<!-- b001721 | prose | pages [5] -->
m

<!-- b001722 | prose | pages [5] -->
m

<!-- b001723 | prose | pages [5] -->
m

<!-- b001724 | prose | pages [5] -->
m

<!-- b001725 | prose | pages [5] -->
m

<!-- b001726 | prose | pages [5] -->
m

<!-- b001727 | prose | pages [5] -->
m

<!-- b001728 | prose | pages [5] -->
m

<!-- b001729 | prose | pages [5] -->
m

<!-- b001730 | prose | pages [5] -->
m

<!-- b001731 | prose | pages [5] -->
m

<!-- b001732 | prose | pages [5] -->
m

<!-- b001733 | prose | pages [5] -->
m

<!-- b001734 | prose | pages [5] -->
m

<!-- b001735 | prose | pages [5] -->
m

<!-- b001736 | furniture | pages [5] -->
m

<!-- b001737 | furniture | pages [5] -->
m

<!-- b001738 | furniture | pages [5] -->
m

<!-- b001739 | furniture | pages [5] -->
m

<!-- b001740 | furniture | pages [5] -->
m

<!-- b001741 | furniture | pages [5] -->
m

<!-- b001742 | furniture | pages [5] -->
m

<!-- b001743 | furniture | pages [5] -->
m

<!-- b001744 | furniture | pages [5] -->
m

<!-- b001745 | furniture | pages [5] -->
m

<!-- b001746 | furniture | pages [5] -->
m

<!-- b001747 | furniture | pages [5] -->
m

<!-- b001748 | furniture | pages [5] -->
m

<!-- b001749 | furniture | pages [5] -->
m

<!-- b001750 | furniture | pages [5] -->
m

<!-- b001751 | furniture | pages [5] -->
m

<!-- b001752 | furniture | pages [5] -->
m

<!-- b001753 | furniture | pages [5] -->
m

<!-- b001754 | furniture | pages [5] -->
m

<!-- b001755 | furniture | pages [5] -->
m

<!-- b001756 | furniture | pages [5] -->
m

<!-- b001757 | furniture | pages [5] -->
m

<!-- b001758 | furniture | pages [5] -->
m

<!-- b001759 | furniture | pages [5] -->
m

<!-- b001760 | furniture | pages [5] -->
m

<!-- b001761 | furniture | pages [5] -->
m

<!-- b001762 | furniture | pages [5] -->
m

<!-- b001763 | furniture | pages [5] -->
m

<!-- b001764 | furniture | pages [5] -->
m

<!-- b001765 | furniture | pages [5] -->
m

<!-- b001766 | furniture | pages [5] -->
m

<!-- b001767 | furniture | pages [5] -->
m

<!-- b001768 | furniture | pages [5] -->
m

<!-- b001769 | furniture | pages [5] -->
m

<!-- b001770 | furniture | pages [5] -->
m

<!-- b001771 | furniture | pages [5] -->
m

<!-- b001772 | furniture | pages [5] -->
m

<!-- b001773 | furniture | pages [5] -->
m

<!-- b001774 | furniture | pages [5] -->
m

<!-- b001775 | furniture | pages [5] -->
m

<!-- b001776 | furniture | pages [5] -->
m

<!-- b001777 | furniture | pages [5] -->
m

<!-- b001778 | furniture | pages [5] -->
m

<!-- b001779 | furniture | pages [5] -->
m

<!-- b001780 | furniture | pages [5] -->
m

<!-- b001781 | furniture | pages [5] -->
m

<!-- b001782 | furniture | pages [5] -->
m

<!-- b001783 | furniture | pages [5] -->
m

<!-- b001784 | furniture | pages [5] -->
m

<!-- b001785 | furniture | pages [5] -->
m

<!-- b001786 | furniture | pages [5] -->
m

<!-- b001787 | furniture | pages [5] -->
m

<!-- b001788 | furniture | pages [5] -->
m

<!-- b001789 | furniture | pages [5] -->
m

<!-- b001790 | furniture | pages [5] -->
m

<!-- b001791 | furniture | pages [5] -->
m

<!-- b001792 | furniture | pages [5] -->
m

<!-- b001793 | furniture | pages [5] -->
m

<!-- b001794 | furniture | pages [5] -->
m

<!-- b001795 | furniture | pages [5] -->
m

<!-- b001796 | furniture | pages [5] -->
m

<!-- b001797 | furniture | pages [5] -->
m

<!-- b001798 | furniture | pages [5] -->
m

<!-- b001799 | furniture | pages [5] -->
m

<!-- b001800 | furniture | pages [5] -->
m

<!-- b001801 | furniture | pages [5] -->
m

<!-- b001802 | furniture | pages [5] -->
m

<!-- b001803 | furniture | pages [5] -->
m

<!-- b001804 | furniture | pages [5] -->
m

<!-- b001805 | furniture | pages [5] -->
m

<!-- b001806 | furniture | pages [5] -->
m

<!-- b001807 | furniture | pages [5] -->
m

<!-- b001808 | furniture | pages [5] -->
m

<!-- b001809 | furniture | pages [5] -->
m

<!-- b001810 | furniture | pages [5] -->
m

<!-- b001811 | furniture | pages [5] -->
m

<!-- b001812 | furniture | pages [5] -->
m

<!-- b001813 | furniture | pages [5] -->
m

<!-- b001814 | furniture | pages [5] -->
m

<!-- b001815 | furniture | pages [5] -->
m

<!-- b001816 | furniture | pages [5] -->
m

<!-- b001817 | furniture | pages [5] -->
m

<!-- b001818 | furniture | pages [5] -->
m

<!-- b001819 | furniture | pages [5] -->
m

<!-- b001820 | furniture | pages [5] -->
m

<!-- b001821 | furniture | pages [5] -->
m

<!-- b001822 | furniture | pages [5] -->
m

<!-- b001823 | furniture | pages [5] -->
m

<!-- b001824 | furniture | pages [5] -->
m

<!-- b001825 | furniture | pages [5] -->
m

<!-- b001826 | furniture | pages [5] -->
m

<!-- b001827 | furniture | pages [5] -->
m

<!-- b001828 | furniture | pages [5] -->
m

<!-- b001829 | furniture | pages [5] -->
m

<!-- b001830 | furniture | pages [5] -->
m

<!-- b001831 | furniture | pages [5] -->
m

<!-- b001832 | furniture | pages [5] -->
m

<!-- b001833 | furniture | pages [5] -->
m

<!-- b001834 | furniture | pages [5] -->
m

<!-- b001835 | furniture | pages [5] -->
m

<!-- b001836 | furniture | pages [5] -->
m

<!-- b001837 | furniture | pages [5] -->
m

<!-- b001838 | furniture | pages [5] -->
m

<!-- b001839 | furniture | pages [5] -->
m

<!-- b001840 | furniture | pages [5] -->
m

<!-- b001841 | furniture | pages [5] -->
m

<!-- b001842 | furniture | pages [5] -->
m

<!-- b001843 | furniture | pages [5] -->
m

<!-- b001844 | furniture | pages [5] -->
m

<!-- b001845 | furniture | pages [5] -->
m

<!-- b001846 | furniture | pages [5] -->
m

<!-- b001847 | furniture | pages [5] -->
m

<!-- b001848 | furniture | pages [5] -->
m

<!-- b001849 | furniture | pages [5] -->
m

<!-- b001850 | furniture | pages [5] -->
m

<!-- b001851 | furniture | pages [5] -->
m

<!-- b001852 | furniture | pages [5] -->
m

<!-- b001853 | furniture | pages [5] -->
m

<!-- b001854 | furniture | pages [5] -->
m

<!-- b001855 | furniture | pages [5] -->
m

<!-- b001856 | furniture | pages [5] -->
m

<!-- b001857 | furniture | pages [5] -->
m

<!-- b001858 | furniture | pages [5] -->
m

<!-- b001859 | furniture | pages [5] -->
m

<!-- b001860 | furniture | pages [5] -->
m

<!-- b001861 | furniture | pages [5] -->
m

<!-- b001862 | furniture | pages [5] -->
m

<!-- b001863 | furniture | pages [5] -->
m

<!-- b001864 | furniture | pages [5] -->
m

<!-- b001865 | furniture | pages [5] -->
m

<!-- b001866 | furniture | pages [5] -->
m

<!-- b001867 | furniture | pages [5] -->
m

<!-- b001868 | furniture | pages [5] -->
m

<!-- b001869 | furniture | pages [5] -->
m

<!-- b001870 | furniture | pages [5] -->
m

<!-- b001871 | furniture | pages [5] -->
m

<!-- b001872 | furniture | pages [5] -->
m

<!-- b001873 | furniture | pages [5] -->
m

<!-- b001874 | furniture | pages [5] -->
m

<!-- b001875 | furniture | pages [5] -->
m

<!-- b001876 | furniture | pages [5] -->
m

<!-- b001877 | furniture | pages [5] -->
m

<!-- b001878 | furniture | pages [5] -->
m

<!-- b001879 | furniture | pages [5] -->
m

<!-- b001880 | furniture | pages [5] -->
m

<!-- b001881 | furniture | pages [5] -->
m

<!-- b001882 | furniture | pages [5] -->
m

<!-- b001883 | furniture | pages [5] -->
m

<!-- b001884 | furniture | pages [5] -->
m

<!-- b001885 | furniture | pages [5] -->
m

<!-- b001886 | furniture | pages [5] -->
m

<!-- b001887 | furniture | pages [5] -->
m

<!-- b001888 | furniture | pages [5] -->
m

<!-- b001889 | furniture | pages [5] -->
m

<!-- b001890 | furniture | pages [5] -->
m

<!-- b001891 | furniture | pages [5] -->
m

<!-- b001892 | furniture | pages [5] -->
m

<!-- b001893 | furniture | pages [5] -->
m

<!-- b001894 | furniture | pages [5] -->
m

<!-- b001895 | furniture | pages [5] -->
m

<!-- b001896 | furniture | pages [5] -->
m

<!-- b001897 | furniture | pages [5] -->
m

<!-- b001898 | furniture | pages [5] -->
m

<!-- b001899 | furniture | pages [5] -->
m

<!-- b001900 | furniture | pages [5] -->
m

<!-- b001901 | furniture | pages [5] -->
m

<!-- b001902 | furniture | pages [5] -->
m

<!-- b001903 | furniture | pages [5] -->
m

<!-- b001904 | furniture | pages [5] -->
m

<!-- b001905 | furniture | pages [5] -->
m

<!-- b001906 | furniture | pages [5] -->
m

<!-- b001907 | furniture | pages [5] -->
m

<!-- b001908 | furniture | pages [5] -->
m

<!-- b001909 | furniture | pages [5] -->
m

<!-- b001910 | furniture | pages [5] -->
m

<!-- b001911 | furniture | pages [5] -->
m

<!-- b001912 | furniture | pages [5] -->
m

<!-- b001913 | furniture | pages [5] -->
m

<!-- b001914 | furniture | pages [5] -->
m

<!-- b001915 | furniture | pages [5] -->
m

<!-- b001916 | furniture | pages [5] -->
m

<!-- b001917 | furniture | pages [5] -->
m

<!-- b001918 | furniture | pages [5] -->
m

<!-- b001919 | furniture | pages [5] -->
m

<!-- b001920 | furniture | pages [5] -->
m

<!-- b001921 | furniture | pages [5] -->
m

<!-- b001922 | furniture | pages [5] -->
m

<!-- b001923 | furniture | pages [5] -->
m

<!-- b001924 | furniture | pages [5] -->
m

<!-- b001925 | furniture | pages [5] -->
m

<!-- b001926 | furniture | pages [5] -->
m

<!-- b001927 | furniture | pages [5] -->
m

<!-- b001928 | furniture | pages [5] -->
m

<!-- b001929 | furniture | pages [5] -->
m

<!-- b001930 | furniture | pages [5] -->
m

<!-- b001931 | furniture | pages [5] -->
m

<!-- b001932 | furniture | pages [5] -->
m

<!-- b001933 | furniture | pages [5] -->
m

<!-- b001934 | furniture | pages [5] -->
m

<!-- b001935 | furniture | pages [5] -->
m

<!-- b001936 | furniture | pages [5] -->
m

<!-- b001937 | furniture | pages [5] -->
m

<!-- b001938 | furniture | pages [5] -->
m

<!-- b001939 | furniture | pages [5] -->
m

<!-- b001940 | furniture | pages [5] -->
m

<!-- b001941 | furniture | pages [5] -->
m

<!-- b001942 | furniture | pages [5] -->
m

<!-- b001943 | furniture | pages [5] -->
m

<!-- b001944 | furniture | pages [5] -->
m

<!-- b001945 | furniture | pages [5] -->
m

<!-- b001946 | furniture | pages [5] -->
m

<!-- b001947 | furniture | pages [5] -->
m

<!-- b001948 | furniture | pages [5] -->
m

<!-- b001949 | furniture | pages [5] -->
m

<!-- b001950 | furniture | pages [5] -->
m

<!-- b001951 | furniture | pages [5] -->
m

<!-- b001952 | furniture | pages [5] -->
m

<!-- b001953 | furniture | pages [5] -->
m

<!-- b001954 | furniture | pages [5] -->
m

<!-- b001955 | furniture | pages [5] -->
m

<!-- b001956 | furniture | pages [5] -->
m

<!-- b001957 | furniture | pages [5] -->
m

<!-- b001958 | furniture | pages [5] -->
m

<!-- b001959 | furniture | pages [5] -->
m

<!-- b001960 | furniture | pages [5] -->
m

<!-- b001961 | furniture | pages [5] -->
m

<!-- b001962 | furniture | pages [5] -->
m

<!-- b001963 | furniture | pages [5] -->
m

<!-- b001964 | furniture | pages [5] -->
m

<!-- b001965 | furniture | pages [5] -->
m

<!-- b001966 | furniture | pages [5] -->
m

<!-- b001967 | furniture | pages [5] -->
m

<!-- b001968 | furniture | pages [5] -->
m

<!-- b001969 | furniture | pages [5] -->
m

<!-- b001970 | furniture | pages [5] -->
m

<!-- b001971 | furniture | pages [5] -->
m

<!-- b001972 | furniture | pages [5] -->
m

<!-- b001973 | furniture | pages [5] -->
m

<!-- b001974 | furniture | pages [5] -->
m

<!-- b001975 | furniture | pages [5] -->
m

<!-- b001976 | furniture | pages [5] -->
m

<!-- b001977 | furniture | pages [5] -->
m

<!-- b001978 | furniture | pages [5] -->
m

<!-- b001979 | furniture | pages [5] -->
m

<!-- b001980 | furniture | pages [5] -->
m

<!-- b001981 | furniture | pages [5] -->
m

<!-- b001982 | furniture | pages [5] -->
m

<!-- b001983 | furniture | pages [5] -->
m

<!-- b001984 | furniture | pages [5] -->
m

<!-- b001985 | furniture | pages [5] -->
m

<!-- b001986 | furniture | pages [5] -->
m

<!-- b001987 | furniture | pages [5] -->
m

<!-- b001988 | furniture | pages [5] -->
m

<!-- b001989 | furniture | pages [5] -->
m

<!-- b001990 | furniture | pages [5] -->
m

<!-- b001991 | furniture | pages [5] -->
m

<!-- b001992 | furniture | pages [5] -->
m

<!-- b001993 | furniture | pages [5] -->
m

<!-- b001994 | furniture | pages [5] -->
m

<!-- b001995 | furniture | pages [5] -->
m

<!-- b001996 | furniture | pages [5] -->
m

<!-- b001997 | furniture | pages [5] -->
m

<!-- b001998 | furniture | pages [5] -->
m

<!-- b001999 | furniture | pages [5] -->
m

<!-- b002000 | furniture | pages [5] -->
m

<!-- b002001 | furniture | pages [5] -->
m

<!-- b002002 | furniture | pages [5] -->
m

<!-- b002003 | furniture | pages [5] -->
m

<!-- b002004 | furniture | pages [5] -->
m

<!-- b002005 | furniture | pages [5] -->
m

<!-- b002006 | furniture | pages [5] -->
m

<!-- b002007 | furniture | pages [5] -->
m

<!-- b002008 | furniture | pages [5] -->
m

<!-- b002009 | furniture | pages [5] -->
m

<!-- b002010 | furniture | pages [5] -->
m

<!-- b002011 | furniture | pages [5] -->
m

<!-- b002012 | furniture | pages [5] -->
m

<!-- b002013 | furniture | pages [5] -->
m

<!-- b002014 | furniture | pages [5] -->
m

<!-- b002015 | furniture | pages [5] -->
m

<!-- b002016 | furniture | pages [5] -->
m

<!-- b002017 | furniture | pages [5] -->
m

<!-- b002018 | furniture | pages [5] -->
m

<!-- b002019 | furniture | pages [5] -->
m

<!-- b002020 | furniture | pages [5] -->
m

<!-- b002021 | furniture | pages [5] -->
m

<!-- b002022 | furniture | pages [5] -->
m

<!-- b002023 | furniture | pages [5] -->
m

<!-- b002024 | furniture | pages [5] -->
m

<!-- b002025 | furniture | pages [5] -->
m

<!-- b002026 | furniture | pages [5] -->
m

<!-- b002027 | furniture | pages [5] -->
m

<!-- b002028 | furniture | pages [5] -->
m

<!-- b002029 | furniture | pages [5] -->
m

<!-- b002030 | furniture | pages [5] -->
m

<!-- b002031 | furniture | pages [5] -->
m

<!-- b002032 | furniture | pages [5] -->
m

<!-- b002033 | furniture | pages [5] -->
m

<!-- b002034 | furniture | pages [5] -->
m

<!-- b002035 | furniture | pages [5] -->
m

<!-- b002036 | furniture | pages [5] -->
m

<!-- b002037 | furniture | pages [5] -->
m

<!-- b002038 | furniture | pages [5] -->
m

<!-- b002039 | furniture | pages [5] -->
m

<!-- b002040 | furniture | pages [5] -->
m

<!-- b002041 | furniture | pages [5] -->
m

<!-- b002042 | furniture | pages [5] -->
m

<!-- b002043 | furniture | pages [5] -->
m

<!-- b002044 | furniture | pages [5] -->
m

<!-- b002045 | furniture | pages [5] -->
m

<!-- b002046 | furniture | pages [5] -->
m

<!-- b002047 | furniture | pages [5] -->
m

<!-- b002048 | furniture | pages [5] -->
m

<!-- b002049 | furniture | pages [5] -->
m

<!-- b002050 | furniture | pages [5] -->
m

<!-- b002051 | furniture | pages [5] -->
m

<!-- b002052 | furniture | pages [5] -->
m

<!-- b002053 | furniture | pages [5] -->
m

<!-- b002054 | furniture | pages [5] -->
m

<!-- b002055 | furniture | pages [5] -->
m

<!-- b002056 | furniture | pages [5] -->
m

<!-- b002057 | furniture | pages [5] -->
m

<!-- b002058 | furniture | pages [5] -->
m

<!-- b002059 | furniture | pages [5] -->
m

<!-- b002060 | furniture | pages [5] -->
m

<!-- b002061 | furniture | pages [5] -->
m

<!-- b002062 | furniture | pages [5] -->
m

<!-- b002063 | furniture | pages [5] -->
m

<!-- b002064 | furniture | pages [5] -->
m

<!-- b002065 | furniture | pages [5] -->
m

<!-- b002066 | furniture | pages [5] -->
m

<!-- b002067 | furniture | pages [5] -->
m

<!-- b002068 | furniture | pages [5] -->
m

<!-- b002069 | furniture | pages [5] -->
m

<!-- b002070 | furniture | pages [5] -->
m

<!-- b002071 | furniture | pages [5] -->
m

<!-- b002072 | furniture | pages [5] -->
m

<!-- b002073 | furniture | pages [5] -->
m

<!-- b002074 | furniture | pages [5] -->
m

<!-- b002075 | furniture | pages [5] -->
m

<!-- b002076 | furniture | pages [5] -->
m

<!-- b002077 | furniture | pages [5] -->
m

<!-- b002078 | furniture | pages [5] -->
m

<!-- b002079 | furniture | pages [5] -->
m

<!-- b002080 | furniture | pages [5] -->
m

<!-- b002081 | furniture | pages [5] -->
m

<!-- b002082 | furniture | pages [5] -->
m

<!-- b002083 | furniture | pages [5] -->
m

<!-- b002084 | furniture | pages [5] -->
m

<!-- b002085 | furniture | pages [5] -->
m

<!-- b002086 | furniture | pages [5] -->
m

<!-- b002087 | furniture | pages [5] -->
m

<!-- b002088 | furniture | pages [5] -->
m

<!-- b002089 | furniture | pages [5] -->
m

<!-- b002090 | furniture | pages [5] -->
m

<!-- b002091 | furniture | pages [5] -->
m

<!-- b002092 | furniture | pages [5] -->
m

<!-- b002093 | furniture | pages [5] -->
m

<!-- b002094 | furniture | pages [5] -->
m

<!-- b002095 | furniture | pages [5] -->
m

<!-- b002096 | furniture | pages [5] -->
m

<!-- b002097 | furniture | pages [5] -->
m

<!-- b002098 | furniture | pages [5] -->
m

<!-- b002099 | furniture | pages [5] -->
m

<!-- b002100 | furniture | pages [5] -->
m

<!-- b002101 | furniture | pages [5] -->
m

<!-- b002102 | furniture | pages [5] -->
m

<!-- b002103 | furniture | pages [5] -->
m

<!-- b002104 | furniture | pages [5] -->
m

<!-- b002105 | furniture | pages [5] -->
m

<!-- b002106 | furniture | pages [5] -->
m

<!-- b002107 | furniture | pages [5] -->
m

<!-- b002108 | furniture | pages [5] -->
m

<!-- b002109 | furniture | pages [5] -->
m

<!-- b002110 | furniture | pages [5] -->
m

<!-- b002111 | furniture | pages [5] -->
m

<!-- b002112 | furniture | pages [5] -->
m

<!-- b002113 | furniture | pages [5] -->
m

<!-- b002114 | furniture | pages [5] -->
m

<!-- b002115 | furniture | pages [5] -->
m

<!-- b002116 | furniture | pages [5] -->
m

<!-- b002117 | furniture | pages [5] -->
m

<!-- b002118 | furniture | pages [5] -->
m

<!-- b002119 | furniture | pages [5] -->
m

<!-- b002120 | furniture | pages [5] -->
m

<!-- b002121 | furniture | pages [5] -->
m

<!-- b002122 | furniture | pages [5] -->
m

<!-- b002123 | furniture | pages [5] -->
m

<!-- b002124 | furniture | pages [5] -->
m

<!-- b002125 | furniture | pages [5] -->
m

<!-- b002126 | furniture | pages [5] -->
m

<!-- b002127 | furniture | pages [5] -->
m

<!-- b002128 | furniture | pages [5] -->
m

<!-- b002129 | furniture | pages [5] -->
m

<!-- b002130 | furniture | pages [5] -->
m

<!-- b002131 | furniture | pages [5] -->
m

<!-- b002132 | furniture | pages [5] -->
m

<!-- b002133 | furniture | pages [5] -->
m

<!-- b002134 | furniture | pages [5] -->
m

<!-- b002135 | furniture | pages [5] -->
m

<!-- b002136 | furniture | pages [5] -->
m

<!-- b002137 | furniture | pages [5] -->
m

<!-- b002138 | furniture | pages [5] -->
m

<!-- b002139 | furniture | pages [6] -->
Team # 2510862

<!-- b002140 | furniture | pages [6] -->
Page 6 of 25

<!-- b002141 | prose | pages [6] -->
merOly_athletes.csv file to the corresponding ’NOC’ (National Olympic Committee 3-letter code) to ensure that all participating teams matched their corresponding NOC codes, thus ensuring data consistency. • Step 3: Feature Engineering In order to enhance the predictive power of the model, several new features were created, as shown below. These new features provide valuable insight into under- standing the impact of Olympic host country effects on medal performance.

<!-- b002142 | prose | pages [6] -->
Data Feature Engineering

<!-- b002143 | prose | pages [6] -->
Features

<!-- b002144 | prose | pages [6] -->
Lagged Features Related

<!-- b002145 | prose | pages [6] -->
Host Country-Related

<!-- b002146 | prose | pages [6] -->
to Medal Performance

<!-- b002147 | prose | pages [6] -->
Features

<!-- b002148 | prose | pages [6] -->
was previous

<!-- b002149 | prose | pages [6] -->
Average Gold

<!-- b002150 | prose | pages [6] -->
Average Total Medals

<!-- b002151 | prose | pages [6] -->
is  host

<!-- b002152 | prose | pages [6] -->
(Last 3 Olympics) (Last 3 Olympics)

<!-- b002153 | prose | pages [6] -->
host

<!-- b002154 | prose | pages [6] -->
Athlete-Related Features

<!-- b002155 | prose | pages [6] -->
Athlete Count

<!-- b002156 | prose | pages [6] -->
will next

<!-- b002157 | prose | pages [6] -->
Male Athlete

<!-- b002158 | prose | pages [6] -->
Female Athlete

<!-- b002159 | prose | pages [6] -->
Athlete

<!-- b002160 | prose | pages [6] -->
in Sports

<!-- b002161 | prose | pages [6] -->
Count

<!-- b002162 | prose | pages [6] -->
Count

<!-- b002163 | prose | pages [6] -->
Count

<!-- b002164 | prose | pages [6] -->
host

<!-- b002165 | caption | pages [6] -->
Figure 2: Fearture Engineering

<!-- b002166 | prose | pages [6] -->
We input the number of entries from each country in different events as features into the model and can predict the number of medals more accurately than each event individually. • Step 4: Data Merging and Final Adjustments In the final step, we merged the summerOly_athletes.csv, summerOly_hosts.csv, and summerOly_medal_counts.csv datasets. NOC and Year were used as key vari- ables to ensure that the data could be accurately linked. In the end, a complete dataset was obtained containing all relevant information about each Olympic event, athlete performance and medal results for each country.

<!-- b002167 | heading | pages [6] -->
Task 1: 2028 Olympics Medal Prediction Model

<!-- b002168 | prose | pages [6] -->
5

<!-- b002169 | heading | pages [6] -->
Develop a model for medal counts for each country

<!-- b002170 | prose | pages [6] -->
5.1

<!-- b002171 | prose | pages [6] -->
In order to predict the number of medals for each country at the 2028 Summer Olympics in Los Angeles, in particular the number of gold medals and the total number of medals, the first step is to construct a machine learning regression prediction model that can make predictions with full consideration of multiple features constructed in the preprocessing portion of the data and use multiple evaluation metrics to measure the accuracy and stability of the predictions. The second step is to obtain prediction intervals for medals through a sampling method, and the third step is to analyse the results to explore which countries are likely to improve or decline.

<!-- b002172 | prose | pages [6] -->
关注数学模型

<!-- b002173 | furniture | pages [6] -->
2

<!-- b002174 | furniture | pages [6] -->
MATHmodels

<!-- b002175 | furniture | pages [6] -->
获取更多资讯

<!-- b002176 | furniture | pages [7] -->
Team # 2510862

<!-- b002177 | furniture | pages [7] -->
Page 7 of 25

<!-- b002178 | prose | pages [7] -->
微信公众号：数学模型

<!-- b002179 | prose | pages [7] -->
⋇Step 1: Principle of Stacking

<!-- b002180 | prose | pages [7] -->
Stacking is an integrated learning approach that combines multiple base learners (LGBM, SVM, XGBoost, and RF) into a final prediction model. Each base learner is trained independently and their predictions are then fed as features into a meta- learner (logistic regression) to generate the final prediction. The core advantage of stacking is the ability to combine the strengths of different models to improve the overall prediction performance. The Olympic medal prediction problem faces mul- tiple challenges, including taking into account the historical performance of coun- tries, the impact of different events and disciplines, home country effects, and pos- sible future changes.

<!-- b002181 | prose | pages [7] -->
微信号：MATHmodels

<!-- b002182 | caption | pages [7] -->
Figure 3: Principle of Stacking

<!-- b002183 | prose | pages [7] -->
In predicting the number of medals at the 2028 Olympics, the stacked approach al- lows us to integrate the unique strengths of each of the underlying models.LGBM, SVM, XGBoost, and RF are able to capture different patterns in the data, such as non-linear relationships, feature interactions, and variance, respectively. By com- bining the outputs of these models, the stacked approach provides more robust and accurate predictions that can effectively predict the total number of medals and gold medals for each country.

<!-- b002184 | heading | pages [7] -->
⋇Step 2: Base Models

<!-- b002185 | heading | pages [7] -->
1. LightGBM (LGBM)

<!-- b002186 | prose | pages [7] -->
LightGBM is a gradient boosting algorithm based on decision trees. It gradually improves the predictive power of the model at each iteration step by constructing a series of decision trees, each one correcting the residuals of the previous one. Light- GBM is extremely efficient when dealing with large datasets and is fast to train. By splitting the tree model, it is able to identify complex interactions between different features (e.g. the relationship between host country and historical performance) and accurately predict the number of medals. The overall objective function is:Equation 1

<!-- b002187 | prose | pages [7] -->
N X

<!-- b002188 | prose | pages [7] -->
(1)

<!-- b002189 | prose | pages [7] -->
L(θ) =

<!-- b002190 | prose | pages [7] -->
l(yi, byi) + Ω(f)

<!-- b002191 | prose | pages [7] -->
i=1

<!-- b002192 | prose | pages [7] -->
Where: l(yi, byi) is the loss function, typically the Mean Squared Error (MSE) for re- gression problems. Ω(f) is the regularization term that penalizes model complexity

<!-- b002193 | prose | pages [7] -->
m

<!-- b002194 | prose | pages [7] -->
m

<!-- b002195 | prose | pages [7] -->
m

<!-- b002196 | prose | pages [7] -->
m

<!-- b002197 | prose | pages [7] -->
m

<!-- b002198 | prose | pages [7] -->
m

<!-- b002199 | prose | pages [7] -->
m

<!-- b002200 | prose | pages [7] -->
m

<!-- b002201 | prose | pages [7] -->
m

<!-- b002202 | prose | pages [7] -->
m

<!-- b002203 | prose | pages [7] -->
m

<!-- b002204 | prose | pages [7] -->
m

<!-- b002205 | prose | pages [7] -->
m

<!-- b002206 | prose | pages [7] -->
m

<!-- b002207 | prose | pages [7] -->
m

<!-- b002208 | prose | pages [7] -->
m

<!-- b002209 | prose | pages [7] -->
m

<!-- b002210 | prose | pages [7] -->
m

<!-- b002211 | prose | pages [7] -->
m

<!-- b002212 | prose | pages [7] -->
m

<!-- b002213 | prose | pages [7] -->
m

<!-- b002214 | prose | pages [7] -->
m

<!-- b002215 | prose | pages [7] -->
m

<!-- b002216 | prose | pages [7] -->
m

<!-- b002217 | prose | pages [7] -->
m

<!-- b002218 | prose | pages [7] -->
m

<!-- b002219 | prose | pages [7] -->
m

<!-- b002220 | prose | pages [7] -->
m

<!-- b002221 | prose | pages [7] -->
m

<!-- b002222 | prose | pages [7] -->
m

<!-- b002223 | prose | pages [7] -->
m

<!-- b002224 | prose | pages [7] -->
m

<!-- b002225 | prose | pages [7] -->
m

<!-- b002226 | prose | pages [7] -->
m

<!-- b002227 | prose | pages [7] -->
m

<!-- b002228 | prose | pages [7] -->
m

<!-- b002229 | prose | pages [7] -->
m

<!-- b002230 | prose | pages [7] -->
m

<!-- b002231 | prose | pages [7] -->
m

<!-- b002232 | prose | pages [7] -->
m

<!-- b002233 | prose | pages [7] -->
m

<!-- b002234 | prose | pages [7] -->
m

<!-- b002235 | prose | pages [7] -->
m

<!-- b002236 | prose | pages [7] -->
m

<!-- b002237 | prose | pages [7] -->
m

<!-- b002238 | prose | pages [7] -->
m

<!-- b002239 | prose | pages [7] -->
m

<!-- b002240 | prose | pages [7] -->
m

<!-- b002241 | prose | pages [7] -->
m

<!-- b002242 | prose | pages [7] -->
m

<!-- b002243 | prose | pages [7] -->
m

<!-- b002244 | prose | pages [7] -->
m

<!-- b002245 | prose | pages [7] -->
m

<!-- b002246 | prose | pages [7] -->
m

<!-- b002247 | prose | pages [7] -->
m

<!-- b002248 | prose | pages [7] -->
m

<!-- b002249 | prose | pages [7] -->
m

<!-- b002250 | prose | pages [7] -->
m

<!-- b002251 | prose | pages [7] -->
m

<!-- b002252 | prose | pages [7] -->
m

<!-- b002253 | prose | pages [7] -->
m

<!-- b002254 | prose | pages [7] -->
m

<!-- b002255 | prose | pages [7] -->
m

<!-- b002256 | prose | pages [7] -->
m

<!-- b002257 | prose | pages [7] -->
m

<!-- b002258 | prose | pages [7] -->
m

<!-- b002259 | prose | pages [7] -->
m

<!-- b002260 | prose | pages [7] -->
m

<!-- b002261 | prose | pages [7] -->
m

<!-- b002262 | prose | pages [7] -->
m

<!-- b002263 | prose | pages [7] -->
m

<!-- b002264 | prose | pages [7] -->
m

<!-- b002265 | prose | pages [7] -->
m

<!-- b002266 | prose | pages [7] -->
m

<!-- b002267 | prose | pages [7] -->
m

<!-- b002268 | prose | pages [7] -->
m

<!-- b002269 | prose | pages [7] -->
m

<!-- b002270 | prose | pages [7] -->
m

<!-- b002271 | prose | pages [7] -->
m

<!-- b002272 | prose | pages [7] -->
m

<!-- b002273 | prose | pages [7] -->
m

<!-- b002274 | prose | pages [7] -->
m

<!-- b002275 | prose | pages [7] -->
m

<!-- b002276 | prose | pages [7] -->
m

<!-- b002277 | prose | pages [7] -->
m

<!-- b002278 | prose | pages [7] -->
m

<!-- b002279 | prose | pages [7] -->
m

<!-- b002280 | prose | pages [7] -->
m

<!-- b002281 | prose | pages [7] -->
m

<!-- b002282 | prose | pages [7] -->
m

<!-- b002283 | prose | pages [7] -->
m

<!-- b002284 | prose | pages [7] -->
m

<!-- b002285 | prose | pages [7] -->
m

<!-- b002286 | prose | pages [7] -->
m

<!-- b002287 | prose | pages [7] -->
m

<!-- b002288 | prose | pages [7] -->
m

<!-- b002289 | prose | pages [7] -->
m

<!-- b002290 | prose | pages [7] -->
m

<!-- b002291 | prose | pages [7] -->
m

<!-- b002292 | prose | pages [7] -->
m

<!-- b002293 | prose | pages [7] -->
m

<!-- b002294 | prose | pages [7] -->
m

<!-- b002295 | prose | pages [7] -->
m

<!-- b002296 | prose | pages [7] -->
m

<!-- b002297 | prose | pages [7] -->
m

<!-- b002298 | prose | pages [7] -->
m

<!-- b002299 | prose | pages [7] -->
m

<!-- b002300 | prose | pages [7] -->
m

<!-- b002301 | prose | pages [7] -->
m

<!-- b002302 | prose | pages [7] -->
m

<!-- b002303 | prose | pages [7] -->
m

<!-- b002304 | prose | pages [7] -->
m

<!-- b002305 | prose | pages [7] -->
m

<!-- b002306 | prose | pages [7] -->
m

<!-- b002307 | prose | pages [7] -->
m

<!-- b002308 | prose | pages [7] -->
m

<!-- b002309 | prose | pages [7] -->
m

<!-- b002310 | prose | pages [7] -->
m

<!-- b002311 | prose | pages [7] -->
m

<!-- b002312 | prose | pages [7] -->
m

<!-- b002313 | prose | pages [7] -->
m

<!-- b002314 | prose | pages [7] -->
m

<!-- b002315 | prose | pages [7] -->
m

<!-- b002316 | prose | pages [7] -->
m

<!-- b002317 | prose | pages [7] -->
m

<!-- b002318 | prose | pages [7] -->
m

<!-- b002319 | prose | pages [7] -->
m

<!-- b002320 | prose | pages [7] -->
m

<!-- b002321 | prose | pages [7] -->
m

<!-- b002322 | prose | pages [7] -->
m

<!-- b002323 | prose | pages [7] -->
m

<!-- b002324 | prose | pages [7] -->
m

<!-- b002325 | prose | pages [7] -->
m

<!-- b002326 | prose | pages [7] -->
m

<!-- b002327 | prose | pages [7] -->
m

<!-- b002328 | prose | pages [7] -->
m

<!-- b002329 | prose | pages [7] -->
m

<!-- b002330 | prose | pages [7] -->
m

<!-- b002331 | prose | pages [7] -->
m

<!-- b002332 | prose | pages [7] -->
m

<!-- b002333 | prose | pages [7] -->
m

<!-- b002334 | prose | pages [7] -->
m

<!-- b002335 | prose | pages [7] -->
m

<!-- b002336 | prose | pages [7] -->
m

<!-- b002337 | prose | pages [7] -->
m

<!-- b002338 | prose | pages [7] -->
m

<!-- b002339 | prose | pages [7] -->
m

<!-- b002340 | prose | pages [7] -->
m

<!-- b002341 | prose | pages [7] -->
m

<!-- b002342 | prose | pages [7] -->
m

<!-- b002343 | prose | pages [7] -->
m

<!-- b002344 | prose | pages [7] -->
m

<!-- b002345 | prose | pages [7] -->
m

<!-- b002346 | prose | pages [7] -->
m

<!-- b002347 | prose | pages [7] -->
m

<!-- b002348 | prose | pages [7] -->
m

<!-- b002349 | prose | pages [7] -->
m

<!-- b002350 | prose | pages [7] -->
m

<!-- b002351 | prose | pages [7] -->
m

<!-- b002352 | prose | pages [7] -->
m

<!-- b002353 | prose | pages [7] -->
m

<!-- b002354 | prose | pages [7] -->
m

<!-- b002355 | prose | pages [7] -->
m

<!-- b002356 | prose | pages [7] -->
m

<!-- b002357 | prose | pages [7] -->
m

<!-- b002358 | prose | pages [7] -->
m

<!-- b002359 | prose | pages [7] -->
m

<!-- b002360 | prose | pages [7] -->
m

<!-- b002361 | prose | pages [7] -->
m

<!-- b002362 | prose | pages [7] -->
m

<!-- b002363 | prose | pages [7] -->
m

<!-- b002364 | prose | pages [7] -->
m

<!-- b002365 | prose | pages [7] -->
m

<!-- b002366 | prose | pages [7] -->
m

<!-- b002367 | prose | pages [7] -->
m

<!-- b002368 | prose | pages [7] -->
m

<!-- b002369 | prose | pages [7] -->
m

<!-- b002370 | prose | pages [7] -->
m

<!-- b002371 | prose | pages [7] -->
m

<!-- b002372 | prose | pages [7] -->
m

<!-- b002373 | prose | pages [7] -->
m

<!-- b002374 | prose | pages [7] -->
m

<!-- b002375 | prose | pages [7] -->
m

<!-- b002376 | prose | pages [7] -->
m

<!-- b002377 | prose | pages [7] -->
m

<!-- b002378 | prose | pages [7] -->
m

<!-- b002379 | prose | pages [7] -->
m

<!-- b002380 | prose | pages [7] -->
m

<!-- b002381 | prose | pages [7] -->
m

<!-- b002382 | prose | pages [7] -->
m

<!-- b002383 | prose | pages [7] -->
m

<!-- b002384 | prose | pages [7] -->
m

<!-- b002385 | prose | pages [7] -->
m

<!-- b002386 | prose | pages [7] -->
m

<!-- b002387 | prose | pages [7] -->
m

<!-- b002388 | prose | pages [7] -->
m

<!-- b002389 | prose | pages [7] -->
m

<!-- b002390 | prose | pages [7] -->
m

<!-- b002391 | prose | pages [7] -->
m

<!-- b002392 | prose | pages [7] -->
m

<!-- b002393 | prose | pages [7] -->
m

<!-- b002394 | prose | pages [7] -->
m

<!-- b002395 | prose | pages [7] -->
m

<!-- b002396 | prose | pages [7] -->
m

<!-- b002397 | prose | pages [7] -->
m

<!-- b002398 | prose | pages [7] -->
m

<!-- b002399 | prose | pages [7] -->
m

<!-- b002400 | prose | pages [7] -->
m

<!-- b002401 | prose | pages [7] -->
m

<!-- b002402 | prose | pages [7] -->
m

<!-- b002403 | prose | pages [7] -->
m

<!-- b002404 | prose | pages [7] -->
m

<!-- b002405 | prose | pages [7] -->
m

<!-- b002406 | prose | pages [7] -->
m

<!-- b002407 | prose | pages [7] -->
m

<!-- b002408 | prose | pages [7] -->
m

<!-- b002409 | prose | pages [7] -->
m

<!-- b002410 | prose | pages [7] -->
m

<!-- b002411 | prose | pages [7] -->
m

<!-- b002412 | prose | pages [7] -->
m

<!-- b002413 | prose | pages [7] -->
m

<!-- b002414 | prose | pages [7] -->
m

<!-- b002415 | prose | pages [7] -->
m

<!-- b002416 | prose | pages [7] -->
m

<!-- b002417 | prose | pages [7] -->
m

<!-- b002418 | prose | pages [7] -->
m

<!-- b002419 | prose | pages [7] -->
m

<!-- b002420 | prose | pages [7] -->
m

<!-- b002421 | prose | pages [7] -->
m

<!-- b002422 | prose | pages [7] -->
m

<!-- b002423 | prose | pages [7] -->
m

<!-- b002424 | prose | pages [7] -->
m

<!-- b002425 | prose | pages [7] -->
m

<!-- b002426 | prose | pages [7] -->
m

<!-- b002427 | prose | pages [7] -->
m

<!-- b002428 | prose | pages [7] -->
m

<!-- b002429 | prose | pages [7] -->
m

<!-- b002430 | prose | pages [7] -->
m

<!-- b002431 | prose | pages [7] -->
m

<!-- b002432 | prose | pages [7] -->
m

<!-- b002433 | prose | pages [7] -->
m

<!-- b002434 | prose | pages [7] -->
m

<!-- b002435 | prose | pages [7] -->
m

<!-- b002436 | prose | pages [7] -->
m

<!-- b002437 | prose | pages [7] -->
m

<!-- b002438 | prose | pages [7] -->
m

<!-- b002439 | prose | pages [7] -->
m

<!-- b002440 | prose | pages [7] -->
m

<!-- b002441 | prose | pages [7] -->
m

<!-- b002442 | prose | pages [7] -->
m

<!-- b002443 | prose | pages [7] -->
m

<!-- b002444 | prose | pages [7] -->
m

<!-- b002445 | prose | pages [7] -->
m

<!-- b002446 | prose | pages [7] -->
m

<!-- b002447 | prose | pages [7] -->
m

<!-- b002448 | prose | pages [7] -->
m

<!-- b002449 | prose | pages [7] -->
m

<!-- b002450 | prose | pages [7] -->
m

<!-- b002451 | prose | pages [7] -->
m

<!-- b002452 | prose | pages [7] -->
m

<!-- b002453 | prose | pages [7] -->
m

<!-- b002454 | prose | pages [7] -->
m

<!-- b002455 | prose | pages [7] -->
m

<!-- b002456 | prose | pages [7] -->
m

<!-- b002457 | prose | pages [7] -->
m

<!-- b002458 | prose | pages [7] -->
m

<!-- b002459 | prose | pages [7] -->
m

<!-- b002460 | prose | pages [7] -->
m

<!-- b002461 | prose | pages [7] -->
m

<!-- b002462 | prose | pages [7] -->
m

<!-- b002463 | prose | pages [7] -->
m

<!-- b002464 | prose | pages [7] -->
m

<!-- b002465 | prose | pages [7] -->
m

<!-- b002466 | prose | pages [7] -->
m

<!-- b002467 | prose | pages [7] -->
m

<!-- b002468 | prose | pages [7] -->
m

<!-- b002469 | prose | pages [7] -->
m

<!-- b002470 | prose | pages [7] -->
m

<!-- b002471 | prose | pages [7] -->
m

<!-- b002472 | prose | pages [7] -->
m

<!-- b002473 | prose | pages [7] -->
m

<!-- b002474 | prose | pages [7] -->
m

<!-- b002475 | prose | pages [7] -->
m

<!-- b002476 | prose | pages [7] -->
m

<!-- b002477 | furniture | pages [7] -->
m

<!-- b002478 | furniture | pages [7] -->
m

<!-- b002479 | furniture | pages [7] -->
m

<!-- b002480 | furniture | pages [7] -->
m

<!-- b002481 | furniture | pages [7] -->
m

<!-- b002482 | furniture | pages [7] -->
m

<!-- b002483 | furniture | pages [7] -->
m

<!-- b002484 | furniture | pages [7] -->
m

<!-- b002485 | furniture | pages [7] -->
m

<!-- b002486 | furniture | pages [7] -->
m

<!-- b002487 | furniture | pages [7] -->
m

<!-- b002488 | furniture | pages [7] -->
m

<!-- b002489 | furniture | pages [7] -->
m

<!-- b002490 | furniture | pages [7] -->
m

<!-- b002491 | furniture | pages [7] -->
m

<!-- b002492 | furniture | pages [7] -->
m

<!-- b002493 | furniture | pages [7] -->
m

<!-- b002494 | furniture | pages [7] -->
m

<!-- b002495 | furniture | pages [7] -->
m

<!-- b002496 | furniture | pages [7] -->
m

<!-- b002497 | furniture | pages [7] -->
m

<!-- b002498 | furniture | pages [7] -->
m

<!-- b002499 | furniture | pages [7] -->
m

<!-- b002500 | furniture | pages [7] -->
m

<!-- b002501 | furniture | pages [7] -->
m

<!-- b002502 | furniture | pages [7] -->
m

<!-- b002503 | furniture | pages [7] -->
m

<!-- b002504 | furniture | pages [7] -->
m

<!-- b002505 | furniture | pages [7] -->
m

<!-- b002506 | furniture | pages [7] -->
m

<!-- b002507 | furniture | pages [7] -->
m

<!-- b002508 | furniture | pages [7] -->
m

<!-- b002509 | furniture | pages [7] -->
m

<!-- b002510 | furniture | pages [7] -->
m

<!-- b002511 | furniture | pages [7] -->
m

<!-- b002512 | furniture | pages [7] -->
m

<!-- b002513 | furniture | pages [7] -->
m

<!-- b002514 | furniture | pages [7] -->
m

<!-- b002515 | furniture | pages [7] -->
m

<!-- b002516 | furniture | pages [7] -->
m

<!-- b002517 | furniture | pages [7] -->
m

<!-- b002518 | furniture | pages [7] -->
m

<!-- b002519 | furniture | pages [7] -->
m

<!-- b002520 | furniture | pages [7] -->
m

<!-- b002521 | furniture | pages [7] -->
m

<!-- b002522 | furniture | pages [7] -->
m

<!-- b002523 | furniture | pages [7] -->
m

<!-- b002524 | furniture | pages [7] -->
m

<!-- b002525 | furniture | pages [7] -->
m

<!-- b002526 | furniture | pages [7] -->
m

<!-- b002527 | furniture | pages [7] -->
m

<!-- b002528 | furniture | pages [7] -->
m

<!-- b002529 | furniture | pages [7] -->
m

<!-- b002530 | furniture | pages [7] -->
m

<!-- b002531 | furniture | pages [7] -->
m

<!-- b002532 | furniture | pages [7] -->
m

<!-- b002533 | furniture | pages [7] -->
m

<!-- b002534 | furniture | pages [7] -->
m

<!-- b002535 | furniture | pages [7] -->
m

<!-- b002536 | furniture | pages [7] -->
m

<!-- b002537 | furniture | pages [7] -->
m

<!-- b002538 | furniture | pages [7] -->
m

<!-- b002539 | furniture | pages [7] -->
m

<!-- b002540 | furniture | pages [7] -->
m

<!-- b002541 | furniture | pages [7] -->
m

<!-- b002542 | furniture | pages [7] -->
m

<!-- b002543 | furniture | pages [7] -->
m

<!-- b002544 | furniture | pages [7] -->
m

<!-- b002545 | furniture | pages [7] -->
m

<!-- b002546 | furniture | pages [7] -->
m

<!-- b002547 | furniture | pages [7] -->
m

<!-- b002548 | furniture | pages [7] -->
m

<!-- b002549 | furniture | pages [7] -->
m

<!-- b002550 | furniture | pages [7] -->
m

<!-- b002551 | furniture | pages [7] -->
m

<!-- b002552 | furniture | pages [7] -->
m

<!-- b002553 | furniture | pages [7] -->
m

<!-- b002554 | furniture | pages [7] -->
m

<!-- b002555 | furniture | pages [7] -->
m

<!-- b002556 | furniture | pages [7] -->
m

<!-- b002557 | furniture | pages [7] -->
m

<!-- b002558 | furniture | pages [7] -->
m

<!-- b002559 | furniture | pages [7] -->
m

<!-- b002560 | furniture | pages [7] -->
m

<!-- b002561 | furniture | pages [7] -->
m

<!-- b002562 | furniture | pages [7] -->
m

<!-- b002563 | furniture | pages [7] -->
m

<!-- b002564 | furniture | pages [7] -->
m

<!-- b002565 | furniture | pages [7] -->
m

<!-- b002566 | furniture | pages [7] -->
m

<!-- b002567 | furniture | pages [7] -->
m

<!-- b002568 | furniture | pages [7] -->
m

<!-- b002569 | furniture | pages [7] -->
m

<!-- b002570 | furniture | pages [7] -->
m

<!-- b002571 | furniture | pages [7] -->
m

<!-- b002572 | furniture | pages [7] -->
m

<!-- b002573 | furniture | pages [7] -->
m

<!-- b002574 | furniture | pages [7] -->
m

<!-- b002575 | furniture | pages [7] -->
m

<!-- b002576 | furniture | pages [7] -->
m

<!-- b002577 | furniture | pages [7] -->
m

<!-- b002578 | furniture | pages [7] -->
m

<!-- b002579 | furniture | pages [7] -->
m

<!-- b002580 | furniture | pages [7] -->
m

<!-- b002581 | furniture | pages [7] -->
m

<!-- b002582 | furniture | pages [7] -->
m

<!-- b002583 | furniture | pages [7] -->
m

<!-- b002584 | furniture | pages [7] -->
m

<!-- b002585 | furniture | pages [7] -->
m

<!-- b002586 | furniture | pages [7] -->
m

<!-- b002587 | furniture | pages [7] -->
m

<!-- b002588 | furniture | pages [7] -->
m

<!-- b002589 | furniture | pages [7] -->
m

<!-- b002590 | furniture | pages [7] -->
m

<!-- b002591 | furniture | pages [7] -->
m

<!-- b002592 | furniture | pages [7] -->
m

<!-- b002593 | furniture | pages [7] -->
m

<!-- b002594 | furniture | pages [7] -->
m

<!-- b002595 | furniture | pages [7] -->
m

<!-- b002596 | furniture | pages [7] -->
m

<!-- b002597 | furniture | pages [7] -->
m

<!-- b002598 | furniture | pages [7] -->
m

<!-- b002599 | furniture | pages [7] -->
m

<!-- b002600 | furniture | pages [7] -->
m

<!-- b002601 | furniture | pages [7] -->
m

<!-- b002602 | furniture | pages [7] -->
m

<!-- b002603 | furniture | pages [7] -->
m

<!-- b002604 | furniture | pages [7] -->
m

<!-- b002605 | furniture | pages [7] -->
m

<!-- b002606 | furniture | pages [7] -->
m

<!-- b002607 | furniture | pages [7] -->
m

<!-- b002608 | furniture | pages [7] -->
m

<!-- b002609 | furniture | pages [7] -->
m

<!-- b002610 | furniture | pages [7] -->
m

<!-- b002611 | furniture | pages [7] -->
m

<!-- b002612 | furniture | pages [7] -->
m

<!-- b002613 | furniture | pages [7] -->
m

<!-- b002614 | furniture | pages [7] -->
m

<!-- b002615 | furniture | pages [7] -->
m

<!-- b002616 | furniture | pages [7] -->
m

<!-- b002617 | furniture | pages [7] -->
m

<!-- b002618 | furniture | pages [7] -->
m

<!-- b002619 | furniture | pages [7] -->
m

<!-- b002620 | furniture | pages [7] -->
m

<!-- b002621 | furniture | pages [7] -->
m

<!-- b002622 | furniture | pages [7] -->
m

<!-- b002623 | furniture | pages [7] -->
m

<!-- b002624 | furniture | pages [7] -->
m

<!-- b002625 | furniture | pages [7] -->
m

<!-- b002626 | furniture | pages [7] -->
m

<!-- b002627 | furniture | pages [7] -->
m

<!-- b002628 | furniture | pages [7] -->
m

<!-- b002629 | furniture | pages [7] -->
m

<!-- b002630 | furniture | pages [7] -->
m

<!-- b002631 | furniture | pages [7] -->
m

<!-- b002632 | furniture | pages [7] -->
m

<!-- b002633 | furniture | pages [7] -->
m

<!-- b002634 | furniture | pages [7] -->
m

<!-- b002635 | furniture | pages [7] -->
m

<!-- b002636 | furniture | pages [7] -->
m

<!-- b002637 | furniture | pages [7] -->
m

<!-- b002638 | furniture | pages [7] -->
m

<!-- b002639 | furniture | pages [7] -->
m

<!-- b002640 | furniture | pages [7] -->
m

<!-- b002641 | furniture | pages [7] -->
m

<!-- b002642 | furniture | pages [7] -->
m

<!-- b002643 | furniture | pages [7] -->
m

<!-- b002644 | furniture | pages [7] -->
m

<!-- b002645 | furniture | pages [7] -->
m

<!-- b002646 | furniture | pages [7] -->
m

<!-- b002647 | furniture | pages [7] -->
m

<!-- b002648 | furniture | pages [7] -->
m

<!-- b002649 | furniture | pages [7] -->
m

<!-- b002650 | furniture | pages [7] -->
m

<!-- b002651 | furniture | pages [7] -->
m

<!-- b002652 | furniture | pages [7] -->
m

<!-- b002653 | furniture | pages [7] -->
m

<!-- b002654 | furniture | pages [7] -->
m

<!-- b002655 | furniture | pages [7] -->
m

<!-- b002656 | furniture | pages [7] -->
m

<!-- b002657 | furniture | pages [7] -->
m

<!-- b002658 | furniture | pages [7] -->
m

<!-- b002659 | furniture | pages [7] -->
m

<!-- b002660 | furniture | pages [7] -->
m

<!-- b002661 | furniture | pages [7] -->
m

<!-- b002662 | furniture | pages [7] -->
m

<!-- b002663 | furniture | pages [7] -->
m

<!-- b002664 | furniture | pages [7] -->
m

<!-- b002665 | furniture | pages [7] -->
m

<!-- b002666 | furniture | pages [7] -->
m

<!-- b002667 | furniture | pages [7] -->
m

<!-- b002668 | furniture | pages [7] -->
m

<!-- b002669 | furniture | pages [7] -->
m

<!-- b002670 | furniture | pages [7] -->
m

<!-- b002671 | furniture | pages [7] -->
m

<!-- b002672 | furniture | pages [7] -->
m

<!-- b002673 | furniture | pages [7] -->
m

<!-- b002674 | furniture | pages [7] -->
m

<!-- b002675 | furniture | pages [7] -->
m

<!-- b002676 | furniture | pages [7] -->
m

<!-- b002677 | furniture | pages [7] -->
m

<!-- b002678 | furniture | pages [7] -->
m

<!-- b002679 | furniture | pages [7] -->
m

<!-- b002680 | furniture | pages [7] -->
m

<!-- b002681 | furniture | pages [7] -->
m

<!-- b002682 | furniture | pages [7] -->
m

<!-- b002683 | furniture | pages [7] -->
m

<!-- b002684 | furniture | pages [7] -->
m

<!-- b002685 | furniture | pages [7] -->
m

<!-- b002686 | furniture | pages [7] -->
m

<!-- b002687 | furniture | pages [7] -->
m

<!-- b002688 | furniture | pages [7] -->
m

<!-- b002689 | furniture | pages [7] -->
m

<!-- b002690 | furniture | pages [7] -->
m

<!-- b002691 | furniture | pages [7] -->
m

<!-- b002692 | furniture | pages [7] -->
m

<!-- b002693 | furniture | pages [7] -->
m

<!-- b002694 | furniture | pages [7] -->
m

<!-- b002695 | furniture | pages [7] -->
m

<!-- b002696 | furniture | pages [7] -->
m

<!-- b002697 | furniture | pages [7] -->
m

<!-- b002698 | furniture | pages [7] -->
m

<!-- b002699 | furniture | pages [7] -->
m

<!-- b002700 | furniture | pages [7] -->
m

<!-- b002701 | furniture | pages [7] -->
m

<!-- b002702 | furniture | pages [7] -->
m

<!-- b002703 | furniture | pages [7] -->
m

<!-- b002704 | furniture | pages [7] -->
m

<!-- b002705 | furniture | pages [7] -->
m

<!-- b002706 | furniture | pages [7] -->
m

<!-- b002707 | furniture | pages [7] -->
m

<!-- b002708 | furniture | pages [7] -->
m

<!-- b002709 | furniture | pages [7] -->
m

<!-- b002710 | furniture | pages [7] -->
m

<!-- b002711 | furniture | pages [7] -->
m

<!-- b002712 | furniture | pages [7] -->
m

<!-- b002713 | furniture | pages [7] -->
m

<!-- b002714 | furniture | pages [7] -->
m

<!-- b002715 | furniture | pages [7] -->
m

<!-- b002716 | furniture | pages [7] -->
m

<!-- b002717 | furniture | pages [7] -->
m

<!-- b002718 | furniture | pages [7] -->
m

<!-- b002719 | furniture | pages [7] -->
m

<!-- b002720 | furniture | pages [7] -->
m

<!-- b002721 | furniture | pages [7] -->
m

<!-- b002722 | furniture | pages [7] -->
m

<!-- b002723 | furniture | pages [7] -->
m

<!-- b002724 | furniture | pages [7] -->
m

<!-- b002725 | furniture | pages [7] -->
m

<!-- b002726 | furniture | pages [7] -->
m

<!-- b002727 | furniture | pages [7] -->
m

<!-- b002728 | furniture | pages [7] -->
m

<!-- b002729 | furniture | pages [7] -->
m

<!-- b002730 | furniture | pages [7] -->
m

<!-- b002731 | furniture | pages [7] -->
m

<!-- b002732 | furniture | pages [7] -->
m

<!-- b002733 | furniture | pages [7] -->
m

<!-- b002734 | furniture | pages [7] -->
m

<!-- b002735 | furniture | pages [7] -->
m

<!-- b002736 | furniture | pages [7] -->
m

<!-- b002737 | furniture | pages [7] -->
m

<!-- b002738 | furniture | pages [7] -->
m

<!-- b002739 | furniture | pages [7] -->
m

<!-- b002740 | furniture | pages [7] -->
m

<!-- b002741 | furniture | pages [7] -->
m

<!-- b002742 | furniture | pages [7] -->
m

<!-- b002743 | furniture | pages [7] -->
m

<!-- b002744 | furniture | pages [7] -->
m

<!-- b002745 | furniture | pages [7] -->
m

<!-- b002746 | furniture | pages [7] -->
m

<!-- b002747 | furniture | pages [7] -->
m

<!-- b002748 | furniture | pages [7] -->
m

<!-- b002749 | furniture | pages [7] -->
m

<!-- b002750 | furniture | pages [7] -->
m

<!-- b002751 | furniture | pages [7] -->
m

<!-- b002752 | furniture | pages [7] -->
m

<!-- b002753 | furniture | pages [7] -->
m

<!-- b002754 | furniture | pages [7] -->
m

<!-- b002755 | furniture | pages [7] -->
m

<!-- b002756 | furniture | pages [7] -->
m

<!-- b002757 | furniture | pages [7] -->
m

<!-- b002758 | furniture | pages [7] -->
m

<!-- b002759 | furniture | pages [7] -->
m

<!-- b002760 | furniture | pages [7] -->
m

<!-- b002761 | furniture | pages [7] -->
m

<!-- b002762 | furniture | pages [7] -->
m

<!-- b002763 | furniture | pages [7] -->
m

<!-- b002764 | furniture | pages [7] -->
m

<!-- b002765 | furniture | pages [7] -->
m

<!-- b002766 | furniture | pages [7] -->
m

<!-- b002767 | furniture | pages [7] -->
m

<!-- b002768 | furniture | pages [7] -->
m

<!-- b002769 | furniture | pages [7] -->
m

<!-- b002770 | furniture | pages [7] -->
m

<!-- b002771 | furniture | pages [7] -->
m

<!-- b002772 | furniture | pages [7] -->
m

<!-- b002773 | furniture | pages [7] -->
m

<!-- b002774 | furniture | pages [7] -->
m

<!-- b002775 | furniture | pages [7] -->
m

<!-- b002776 | furniture | pages [7] -->
m

<!-- b002777 | furniture | pages [7] -->
m

<!-- b002778 | furniture | pages [7] -->
m

<!-- b002779 | furniture | pages [7] -->
m

<!-- b002780 | furniture | pages [7] -->
m

<!-- b002781 | furniture | pages [7] -->
m

<!-- b002782 | furniture | pages [7] -->
m

<!-- b002783 | furniture | pages [7] -->
m

<!-- b002784 | furniture | pages [7] -->
m

<!-- b002785 | furniture | pages [7] -->
m

<!-- b002786 | furniture | pages [7] -->
m

<!-- b002787 | furniture | pages [7] -->
m

<!-- b002788 | furniture | pages [7] -->
m

<!-- b002789 | furniture | pages [7] -->
m

<!-- b002790 | furniture | pages [7] -->
m

<!-- b002791 | furniture | pages [7] -->
m

<!-- b002792 | furniture | pages [7] -->
m

<!-- b002793 | furniture | pages [7] -->
m

<!-- b002794 | furniture | pages [7] -->
m

<!-- b002795 | furniture | pages [7] -->
m

<!-- b002796 | furniture | pages [7] -->
m

<!-- b002797 | furniture | pages [7] -->
m

<!-- b002798 | furniture | pages [7] -->
m

<!-- b002799 | furniture | pages [7] -->
m

<!-- b002800 | furniture | pages [7] -->
m

<!-- b002801 | furniture | pages [7] -->
m

<!-- b002802 | furniture | pages [7] -->
m

<!-- b002803 | furniture | pages [7] -->
m

<!-- b002804 | furniture | pages [7] -->
m

<!-- b002805 | furniture | pages [7] -->
m

<!-- b002806 | furniture | pages [7] -->
m

<!-- b002807 | furniture | pages [7] -->
m

<!-- b002808 | furniture | pages [7] -->
m

<!-- b002809 | furniture | pages [7] -->
m

<!-- b002810 | furniture | pages [7] -->
m

<!-- b002811 | furniture | pages [7] -->
m

<!-- b002812 | furniture | pages [7] -->
m

<!-- b002813 | furniture | pages [7] -->
m

<!-- b002814 | furniture | pages [7] -->
m

<!-- b002815 | furniture | pages [7] -->
m

<!-- b002816 | furniture | pages [7] -->
m

<!-- b002817 | furniture | pages [7] -->
m

<!-- b002818 | furniture | pages [7] -->
m

<!-- b002819 | furniture | pages [7] -->
m

<!-- b002820 | furniture | pages [7] -->
m

<!-- b002821 | furniture | pages [7] -->
m

<!-- b002822 | furniture | pages [7] -->
m

<!-- b002823 | furniture | pages [7] -->
m

<!-- b002824 | furniture | pages [7] -->
m

<!-- b002825 | furniture | pages [7] -->
m

<!-- b002826 | furniture | pages [7] -->
m

<!-- b002827 | furniture | pages [7] -->
m

<!-- b002828 | furniture | pages [7] -->
m

<!-- b002829 | furniture | pages [7] -->
m

<!-- b002830 | furniture | pages [7] -->
m

<!-- b002831 | furniture | pages [7] -->
m

<!-- b002832 | furniture | pages [7] -->
m

<!-- b002833 | furniture | pages [7] -->
m

<!-- b002834 | furniture | pages [7] -->
m

<!-- b002835 | furniture | pages [7] -->
m

<!-- b002836 | furniture | pages [7] -->
m

<!-- b002837 | furniture | pages [7] -->
m

<!-- b002838 | furniture | pages [7] -->
m

<!-- b002839 | furniture | pages [7] -->
m

<!-- b002840 | furniture | pages [7] -->
m

<!-- b002841 | furniture | pages [7] -->
m

<!-- b002842 | furniture | pages [7] -->
m

<!-- b002843 | furniture | pages [7] -->
m

<!-- b002844 | furniture | pages [7] -->
m

<!-- b002845 | furniture | pages [7] -->
m

<!-- b002846 | furniture | pages [7] -->
m

<!-- b002847 | furniture | pages [7] -->
m

<!-- b002848 | furniture | pages [7] -->
m

<!-- b002849 | furniture | pages [7] -->
m

<!-- b002850 | furniture | pages [7] -->
m

<!-- b002851 | furniture | pages [7] -->
m

<!-- b002852 | furniture | pages [7] -->
m

<!-- b002853 | furniture | pages [7] -->
m

<!-- b002854 | furniture | pages [7] -->
m

<!-- b002855 | furniture | pages [7] -->
m

<!-- b002856 | furniture | pages [7] -->
m

<!-- b002857 | furniture | pages [7] -->
m

<!-- b002858 | furniture | pages [7] -->
m

<!-- b002859 | furniture | pages [7] -->
m

<!-- b002860 | furniture | pages [7] -->
m

<!-- b002861 | furniture | pages [7] -->
m

<!-- b002862 | furniture | pages [7] -->
m

<!-- b002863 | furniture | pages [7] -->
m

<!-- b002864 | furniture | pages [7] -->
m

<!-- b002865 | furniture | pages [7] -->
m

<!-- b002866 | furniture | pages [7] -->
m

<!-- b002867 | furniture | pages [7] -->
m

<!-- b002868 | furniture | pages [7] -->
m

<!-- b002869 | furniture | pages [7] -->
m

<!-- b002870 | furniture | pages [7] -->
m

<!-- b002871 | furniture | pages [7] -->
m

<!-- b002872 | furniture | pages [7] -->
m

<!-- b002873 | furniture | pages [7] -->
m

<!-- b002874 | furniture | pages [7] -->
m

<!-- b002875 | furniture | pages [7] -->
m

<!-- b002876 | furniture | pages [7] -->
m

<!-- b002877 | furniture | pages [7] -->
m

<!-- b002878 | furniture | pages [7] -->
m

<!-- b002879 | furniture | pages [7] -->
m

<!-- b002880 | furniture | pages [8] -->
Team # 2510862

<!-- b002881 | prose | pages [8] -->
to avoid overfitting.

<!-- b002882 | furniture | pages [8] -->
Page 8 of 25

<!-- b002883 | prose | pages [8] -->
By minimising this objective function, LightGBM optimises the parameters of the decision tree to improve the accuracy of Olympic medal count predictions.

<!-- b002884 | heading | pages [8] -->
2. Support Vector Machine (SVM)

<!-- b002885 | prose | pages [8] -->
SVM maximises the spacing between different classes of data points by finding an optimal hyperplane.The strength of SVM lies in its ability to model complex pat- terns, especially when the data is highly non-linear and noisy. It is able to find an optimal decision boundary to distinguish between different predictive trends, espe- cially when dealing with features that have complex interactions, and it is effective in identifying which features (e.g., strength of a particular sport) have the greatest impact on medal counts. The objective function of an SVM in regression is: Equation 2

<!-- b002886 | prose | pages [8] -->
N X

<!-- b002887 | prose | pages [8] -->
L(w, b, ϵ) = 1

<!-- b002888 | prose | pages [8] -->
2|w|2 + C

<!-- b002889 | prose | pages [8] -->
(2) ξi

<!-- b002890 | prose | pages [8] -->
i=1

<!-- b002891 | prose | pages [8] -->
Where: w and b are the weights and bias of the hyperplane. ξi are the slack variables that represent the margin of tolerance for each data point. C is the regularization parameter that controls the trade-off between minimizing the error and maximizing the margin.

<!-- b002892 | prose | pages [8] -->
3.Extreme Gradient Boosting(XGBoost) Unlike traditional boosting algorithms, XGBoost introduces Hessian matrices, mak- ing it faster in convergence and improving prediction accuracy. It also introduces regularisation to control model complexity and prevent overfitting.XGBoost is able to model complex interactions between features and is particularly well suited to deal with the combined effects of multiple factors. The objective function of XGBoost is: Equation 3

<!-- b002893 | prose | pages [8] -->
N X

<!-- b002894 | prose | pages [8] -->
L(θ) =

<!-- b002895 | prose | pages [8] -->
i=1

<!-- b002896 | prose | pages [8] -->
T X

<!-- b002897 | prose | pages [8] -->
(3) |wj|2

<!-- b002898 | prose | pages [8] -->
l(yi, byi) + λ

<!-- b002899 | prose | pages [8] -->
j=1

<!-- b002900 | prose | pages [8] -->
Where: λ is a regularization parameter that penalizes large values of the tree param- eters wj.

<!-- b002901 | heading | pages [8] -->
4. Random Forest (RF)

<!-- b002902 | prose | pages [8] -->
Random Forest is an integrated method that combines multiple decision trees trained on random subsets. By using Bagging strategy, it reduces variance, improves stabil- ity and avoids over-fitting. Since each tree is trained independently, Random Forest is able to handle multiple feature combinations, capturing complex patterns and potential feature associations in the data.

<!-- b002903 | heading | pages [8] -->
⋇Step 3: Final Stacking Model Integration

<!-- b002904 | prose | pages [8] -->
Ultimately, the stacked model combines the predictions of LGBM, SVM, XGBoost, and RF into one final prediction. The prediction results of each base model are weighted and combined by a logistic regression model. The integration formula is:Equation 4 Equation 5

<!-- b002905 | prose | pages [8] -->
关注数学模型

<!-- b002906 | furniture | pages [8] -->
2

<!-- b002907 | furniture | pages [8] -->
MATHmodels

<!-- b002908 | furniture | pages [8] -->
获取更多资讯

<!-- b002909 | furniture | pages [10] -->
Team # 2510862

<!-- b002910 | prose | pages [10] -->
Pn

<!-- b002911 | prose | pages [10] -->
R2 = 1 −

<!-- b002912 | prose | pages [10] -->
Pn

<!-- b002913 | furniture | pages [10] -->
Page 10 of 25

<!-- b002914 | prose | pages [10] -->
i=1(yi −byi)2

<!-- b002915 | prose | pages [10] -->
(7) i=1(yi −y)2

<!-- b002916 | prose | pages [10] -->
R² can help us assess the overall fit of the model and understand whether the model explains the variance of the data.Equation 8

<!-- b002917 | prose | pages [10] -->
MSE = 1

<!-- b002918 | prose | pages [10] -->
n

<!-- b002919 | prose | pages [10] -->
n n X

<!-- b002920 | prose | pages [10] -->
(8) (yi −byi)2

<!-- b002921 | prose | pages [10] -->
i=1

<!-- b002922 | prose | pages [10] -->
The MSE provides a quantitative assessment of the prediction error to help us under- stand the absolute magnitude of the prediction error.Equation 9

<!-- b002923 | prose | pages [10] -->
MAPE = 100

<!-- b002924 | prose | pages [10] -->
n

<!-- b002925 | furniture | pages [10] -->


<!-- b002926 | furniture | pages [10] -->


<!-- b002927 | prose | pages [10] -->
n X

<!-- b002928 | prose | pages [10] -->
yi −byi

<!-- b002929 | prose | pages [10] -->
(9)

<!-- b002930 | prose | pages [10] -->
yi

<!-- b002931 | prose | pages [10] -->
i=1

<!-- b002932 | prose | pages [10] -->
MAPE, on the other hand, provides a standardised measure of error that is particu- larly suitable for making comparisons across countries and medal types, making it easy to assess the predictive effectiveness of the model on different countries.

<!-- b002933 | prose | pages [10] -->
These three indicators combine the model fit, error size and error ratio, which help us to comprehensively assess the predictive effectiveness of the model from multiple dimen- sions. The calculation results are shown in Table:

<!-- b002934 | prose | pages [10] -->
XGBOOST LGBM SVM

<!-- b002935 | prose | pages [10] -->
R2 0.78 0.73

<!-- b002936 | prose | pages [10] -->
MSE 0.53 0.62

<!-- b002937 | prose | pages [10] -->
MAPE 0.42 0.48

<!-- b002938 | prose | pages [10] -->
RF Stacking

<!-- b002939 | prose | pages [10] -->
0.86 0.84 0.88

<!-- b002940 | prose | pages [10] -->
0.37 0.39 0.32

<!-- b002941 | prose | pages [10] -->
0.32 0.33 0.30

<!-- b002942 | caption | pages [10] -->
Figure 5: Model evaluation results

<!-- b002943 | prose | pages [10] -->
Overall, the Stacking model has the strongest fitting ability R² and the smallest MSE and MAPE prediction errors due to the integration of multiple base models, obtaining the most stable and accurate prediction results.

<!-- b002944 | prose | pages [10] -->
Include prediction intervals for all results. 5.2.2

<!-- b002945 | prose | pages [10] -->
m

<!-- b002946 | prose | pages [10] -->
m

<!-- b002947 | prose | pages [10] -->
m

<!-- b002948 | prose | pages [10] -->
m

<!-- b002949 | prose | pages [10] -->
m

<!-- b002950 | prose | pages [10] -->
m

<!-- b002951 | prose | pages [10] -->
m

<!-- b002952 | prose | pages [10] -->
m

<!-- b002953 | prose | pages [10] -->
m

<!-- b002954 | prose | pages [10] -->
m

<!-- b002955 | prose | pages [10] -->
m

<!-- b002956 | prose | pages [10] -->
m

<!-- b002957 | prose | pages [10] -->
m

<!-- b002958 | prose | pages [10] -->
m

<!-- b002959 | prose | pages [10] -->
m

<!-- b002960 | prose | pages [10] -->
m

<!-- b002961 | prose | pages [10] -->
m

<!-- b002962 | prose | pages [10] -->
m

<!-- b002963 | prose | pages [10] -->
m

<!-- b002964 | prose | pages [10] -->
m

<!-- b002965 | prose | pages [10] -->
m

<!-- b002966 | prose | pages [10] -->
m

<!-- b002967 | prose | pages [10] -->
m

<!-- b002968 | prose | pages [10] -->
m

<!-- b002969 | prose | pages [10] -->
m

<!-- b002970 | prose | pages [10] -->
m

<!-- b002971 | prose | pages [10] -->
m

<!-- b002972 | prose | pages [10] -->
m

<!-- b002973 | prose | pages [10] -->
m

<!-- b002974 | prose | pages [10] -->
m

<!-- b002975 | prose | pages [10] -->
m

<!-- b002976 | prose | pages [10] -->
m

<!-- b002977 | prose | pages [10] -->
m

<!-- b002978 | prose | pages [10] -->
m

<!-- b002979 | prose | pages [10] -->
m

<!-- b002980 | prose | pages [10] -->
m

<!-- b002981 | prose | pages [10] -->
m

<!-- b002982 | prose | pages [10] -->
m

<!-- b002983 | prose | pages [10] -->
m

<!-- b002984 | prose | pages [10] -->
m

<!-- b002985 | prose | pages [10] -->
m

<!-- b002986 | prose | pages [10] -->
m

<!-- b002987 | prose | pages [10] -->
m

<!-- b002988 | prose | pages [10] -->
m

<!-- b002989 | prose | pages [10] -->
m

<!-- b002990 | prose | pages [10] -->
m

<!-- b002991 | prose | pages [10] -->
m

<!-- b002992 | prose | pages [10] -->
m

<!-- b002993 | prose | pages [10] -->
m

<!-- b002994 | prose | pages [10] -->
m

<!-- b002995 | prose | pages [10] -->
m m

<!-- b002996 | prose | pages [10] -->
m m

<!-- b002997 | prose | pages [10] -->
m m

<!-- b002998 | prose | pages [10] -->
In Olympic medal prediction, the Bootstrap method quantifies the prediction error

<!-- b002999 | prose | pages [10] -->
m

<!-- b003000 | prose | pages [10] -->
m

<!-- b003001 | prose | pages [10] -->
m

<!-- b003002 | prose | pages [10] -->
m

<!-- b003003 | prose | pages [10] -->
m

<!-- b003004 | prose | pages [10] -->
m

<!-- b003005 | prose | pages [10] -->
m

<!-- b003006 | prose | pages [10] -->
m

<!-- b003007 | prose | pages [10] -->
m

<!-- b003008 | prose | pages [10] -->
m

<!-- b003009 | prose | pages [10] -->
m

<!-- b003010 | prose | pages [10] -->
m

<!-- b003011 | prose | pages [10] -->
m

<!-- b003012 | prose | pages [10] -->
m

<!-- b003013 | prose | pages [10] -->
m

<!-- b003014 | prose | pages [10] -->
m

<!-- b003015 | prose | pages [10] -->
m

<!-- b003016 | prose | pages [10] -->
m

<!-- b003017 | prose | pages [10] -->
m

<!-- b003018 | prose | pages [10] -->
m

<!-- b003019 | prose | pages [10] -->
m

<!-- b003020 | prose | pages [10] -->
m

<!-- b003021 | prose | pages [10] -->
m

<!-- b003022 | prose | pages [10] -->
m

<!-- b003023 | prose | pages [10] -->
m

<!-- b003024 | prose | pages [10] -->
m

<!-- b003025 | prose | pages [10] -->
m

<!-- b003026 | prose | pages [10] -->
m

<!-- b003027 | prose | pages [10] -->
m

<!-- b003028 | prose | pages [10] -->
m

<!-- b003029 | prose | pages [10] -->
m

<!-- b003030 | prose | pages [10] -->
m

<!-- b003031 | prose | pages [10] -->
m

<!-- b003032 | prose | pages [10] -->
m

<!-- b003033 | prose | pages [10] -->
m

<!-- b003034 | prose | pages [10] -->
m

<!-- b003035 | prose | pages [10] -->
m

<!-- b003036 | prose | pages [10] -->
m

<!-- b003037 | prose | pages [10] -->
m

<!-- b003038 | prose | pages [10] -->
m

<!-- b003039 | prose | pages [10] -->
m

<!-- b003040 | prose | pages [10] -->
m

<!-- b003041 | prose | pages [10] -->
m

<!-- b003042 | prose | pages [10] -->
m

<!-- b003043 | prose | pages [10] -->
m

<!-- b003044 | prose | pages [10] -->
m

<!-- b003045 | prose | pages [10] -->
m

<!-- b003046 | prose | pages [10] -->
m

<!-- b003047 | prose | pages [10] -->
m

<!-- b003048 | prose | pages [10] -->
m

<!-- b003049 | prose | pages [10] -->
m

<!-- b003050 | prose | pages [10] -->
m

<!-- b003051 | prose | pages [10] -->
m

<!-- b003052 | prose | pages [10] -->
m

<!-- b003053 | prose | pages [10] -->
m

<!-- b003054 | prose | pages [10] -->
m

<!-- b003055 | prose | pages [10] -->
m

<!-- b003056 | prose | pages [10] -->
m

<!-- b003057 | prose | pages [10] -->
m

<!-- b003058 | prose | pages [10] -->
m

<!-- b003059 | prose | pages [10] -->
m

<!-- b003060 | prose | pages [10] -->
m

<!-- b003061 | prose | pages [10] -->
m

<!-- b003062 | prose | pages [10] -->
m

<!-- b003063 | prose | pages [10] -->
m

<!-- b003064 | prose | pages [10] -->
m

<!-- b003065 | prose | pages [10] -->
m

<!-- b003066 | prose | pages [10] -->
m

<!-- b003067 | prose | pages [10] -->
m

<!-- b003068 | prose | pages [10] -->
m

<!-- b003069 | prose | pages [10] -->
m

<!-- b003070 | prose | pages [10] -->
m

<!-- b003071 | prose | pages [10] -->
m

<!-- b003072 | prose | pages [10] -->
m

<!-- b003073 | prose | pages [10] -->
m

<!-- b003074 | prose | pages [10] -->
m

<!-- b003075 | prose | pages [10] -->
m

<!-- b003076 | prose | pages [10] -->
m

<!-- b003077 | prose | pages [10] -->
m

<!-- b003078 | prose | pages [10] -->
m

<!-- b003079 | prose | pages [10] -->
m

<!-- b003080 | prose | pages [10] -->
m

<!-- b003081 | prose | pages [10] -->
m

<!-- b003082 | prose | pages [10] -->
m

<!-- b003083 | prose | pages [10] -->
m

<!-- b003084 | prose | pages [10] -->
m

<!-- b003085 | prose | pages [10] -->
m

<!-- b003086 | prose | pages [10] -->
m

<!-- b003087 | prose | pages [10] -->
m

<!-- b003088 | prose | pages [10] -->
m

<!-- b003089 | prose | pages [10] -->
m

<!-- b003090 | prose | pages [10] -->
m

<!-- b003091 | prose | pages [10] -->
m

<!-- b003092 | prose | pages [10] -->
m

<!-- b003093 | prose | pages [10] -->
m

<!-- b003094 | prose | pages [10] -->
m

<!-- b003095 | prose | pages [10] -->
m

<!-- b003096 | prose | pages [10] -->
m

<!-- b003097 | prose | pages [10] -->
m

<!-- b003098 | prose | pages [10] -->
m

<!-- b003099 | prose | pages [10] -->
m

<!-- b003100 | prose | pages [10] -->
m

<!-- b003101 | prose | pages [10] -->
m

<!-- b003102 | prose | pages [10] -->
m

<!-- b003103 | prose | pages [10] -->
m

<!-- b003104 | prose | pages [10] -->
m

<!-- b003105 | prose | pages [10] -->
m

<!-- b003106 | prose | pages [10] -->
m

<!-- b003107 | prose | pages [10] -->
m

<!-- b003108 | prose | pages [10] -->
m

<!-- b003109 | prose | pages [10] -->
m

<!-- b003110 | prose | pages [10] -->
m

<!-- b003111 | prose | pages [10] -->
m

<!-- b003112 | prose | pages [10] -->
m

<!-- b003113 | prose | pages [10] -->
m

<!-- b003114 | prose | pages [10] -->
m

<!-- b003115 | prose | pages [10] -->
m

<!-- b003116 | prose | pages [10] -->
m

<!-- b003117 | prose | pages [10] -->
m

<!-- b003118 | prose | pages [10] -->
m

<!-- b003119 | prose | pages [10] -->
m

<!-- b003120 | prose | pages [10] -->
m

<!-- b003121 | prose | pages [10] -->
m

<!-- b003122 | prose | pages [10] -->
m

<!-- b003123 | prose | pages [10] -->
m

<!-- b003124 | prose | pages [10] -->
m

<!-- b003125 | prose | pages [10] -->
m

<!-- b003126 | prose | pages [10] -->
m

<!-- b003127 | prose | pages [10] -->
m

<!-- b003128 | prose | pages [10] -->
m

<!-- b003129 | prose | pages [10] -->
m

<!-- b003130 | prose | pages [10] -->
m

<!-- b003131 | prose | pages [10] -->
m

<!-- b003132 | prose | pages [10] -->
m

<!-- b003133 | prose | pages [10] -->
m

<!-- b003134 | prose | pages [10] -->
m

<!-- b003135 | prose | pages [10] -->
m

<!-- b003136 | prose | pages [10] -->
m

<!-- b003137 | prose | pages [10] -->
m

<!-- b003138 | prose | pages [10] -->
m

<!-- b003139 | prose | pages [10] -->
m

<!-- b003140 | prose | pages [10] -->
m

<!-- b003141 | prose | pages [10] -->
m

<!-- b003142 | prose | pages [10] -->
m

<!-- b003143 | prose | pages [10] -->
m

<!-- b003144 | prose | pages [10] -->
m

<!-- b003145 | prose | pages [10] -->
m m

<!-- b003146 | prose | pages [10] -->
m m

<!-- b003147 | prose | pages [10] -->
m m

<!-- b003148 | prose | pages [10] -->
m m

<!-- b003149 | prose | pages [10] -->
m m

<!-- b003150 | prose | pages [10] -->
m m

<!-- b003151 | prose | pages [10] -->
m m

<!-- b003152 | prose | pages [10] -->
m m

<!-- b003153 | prose | pages [10] -->
m m m m

<!-- b003154 | prose | pages [10] -->
through data resampling without the need to make assumptions, and is able to efficiently

<!-- b003155 | prose | pages [10] -->
m

<!-- b003156 | prose | pages [10] -->
m

<!-- b003157 | prose | pages [10] -->
m

<!-- b003158 | prose | pages [10] -->
m

<!-- b003159 | prose | pages [10] -->
m

<!-- b003160 | prose | pages [10] -->
m

<!-- b003161 | prose | pages [10] -->
m

<!-- b003162 | prose | pages [10] -->
m

<!-- b003163 | prose | pages [10] -->
m

<!-- b003164 | prose | pages [10] -->
m

<!-- b003165 | prose | pages [10] -->
m

<!-- b003166 | prose | pages [10] -->
m

<!-- b003167 | prose | pages [10] -->
m

<!-- b003168 | prose | pages [10] -->
m

<!-- b003169 | prose | pages [10] -->
m

<!-- b003170 | prose | pages [10] -->
m

<!-- b003171 | prose | pages [10] -->
m

<!-- b003172 | prose | pages [10] -->
m

<!-- b003173 | prose | pages [10] -->
m

<!-- b003174 | prose | pages [10] -->
m

<!-- b003175 | prose | pages [10] -->
m

<!-- b003176 | prose | pages [10] -->
m

<!-- b003177 | prose | pages [10] -->
m

<!-- b003178 | prose | pages [10] -->
m

<!-- b003179 | prose | pages [10] -->
m

<!-- b003180 | prose | pages [10] -->
m

<!-- b003181 | prose | pages [10] -->
m

<!-- b003182 | prose | pages [10] -->
m

<!-- b003183 | prose | pages [10] -->
m

<!-- b003184 | prose | pages [10] -->
m

<!-- b003185 | prose | pages [10] -->
m

<!-- b003186 | prose | pages [10] -->
m

<!-- b003187 | prose | pages [10] -->
m

<!-- b003188 | prose | pages [10] -->
m

<!-- b003189 | prose | pages [10] -->
m

<!-- b003190 | prose | pages [10] -->
m

<!-- b003191 | prose | pages [10] -->
m

<!-- b003192 | prose | pages [10] -->
m

<!-- b003193 | prose | pages [10] -->
m

<!-- b003194 | prose | pages [10] -->
m

<!-- b003195 | prose | pages [10] -->
m

<!-- b003196 | prose | pages [10] -->
m

<!-- b003197 | prose | pages [10] -->
m

<!-- b003198 | prose | pages [10] -->
m

<!-- b003199 | prose | pages [10] -->
m

<!-- b003200 | prose | pages [10] -->
m

<!-- b003201 | prose | pages [10] -->
m

<!-- b003202 | prose | pages [10] -->
m

<!-- b003203 | prose | pages [10] -->
m

<!-- b003204 | prose | pages [10] -->
m

<!-- b003205 | prose | pages [10] -->
m

<!-- b003206 | prose | pages [10] -->
m

<!-- b003207 | prose | pages [10] -->
m

<!-- b003208 | prose | pages [10] -->
m

<!-- b003209 | prose | pages [10] -->
m

<!-- b003210 | prose | pages [10] -->
m

<!-- b003211 | prose | pages [10] -->
m

<!-- b003212 | prose | pages [10] -->
m

<!-- b003213 | prose | pages [10] -->
m

<!-- b003214 | prose | pages [10] -->
m

<!-- b003215 | prose | pages [10] -->
m

<!-- b003216 | prose | pages [10] -->
m

<!-- b003217 | prose | pages [10] -->
m

<!-- b003218 | prose | pages [10] -->
m

<!-- b003219 | prose | pages [10] -->
m

<!-- b003220 | prose | pages [10] -->
m

<!-- b003221 | prose | pages [10] -->
m

<!-- b003222 | prose | pages [10] -->
m

<!-- b003223 | prose | pages [10] -->
m

<!-- b003224 | prose | pages [10] -->
m

<!-- b003225 | prose | pages [10] -->
m

<!-- b003226 | prose | pages [10] -->
m

<!-- b003227 | prose | pages [10] -->
m

<!-- b003228 | prose | pages [10] -->
m

<!-- b003229 | prose | pages [10] -->
m

<!-- b003230 | prose | pages [10] -->
m

<!-- b003231 | prose | pages [10] -->
m

<!-- b003232 | prose | pages [10] -->
m

<!-- b003233 | prose | pages [10] -->
m

<!-- b003234 | prose | pages [10] -->
m

<!-- b003235 | prose | pages [10] -->
m

<!-- b003236 | prose | pages [10] -->
m

<!-- b003237 | prose | pages [10] -->
m

<!-- b003238 | prose | pages [10] -->
m

<!-- b003239 | prose | pages [10] -->
m

<!-- b003240 | prose | pages [10] -->
m

<!-- b003241 | prose | pages [10] -->
m

<!-- b003242 | prose | pages [10] -->
m

<!-- b003243 | prose | pages [10] -->
m

<!-- b003244 | prose | pages [10] -->
m

<!-- b003245 | prose | pages [10] -->
m

<!-- b003246 | prose | pages [10] -->
m

<!-- b003247 | prose | pages [10] -->
m

<!-- b003248 | prose | pages [10] -->
m

<!-- b003249 | prose | pages [10] -->
m

<!-- b003250 | prose | pages [10] -->
m

<!-- b003251 | prose | pages [10] -->
m

<!-- b003252 | prose | pages [10] -->
m

<!-- b003253 | prose | pages [10] -->
m

<!-- b003254 | prose | pages [10] -->
m

<!-- b003255 | prose | pages [10] -->
m

<!-- b003256 | prose | pages [10] -->
m

<!-- b003257 | prose | pages [10] -->
m

<!-- b003258 | prose | pages [10] -->
m

<!-- b003259 | prose | pages [10] -->
m

<!-- b003260 | prose | pages [10] -->
m

<!-- b003261 | prose | pages [10] -->
m

<!-- b003262 | prose | pages [10] -->
m

<!-- b003263 | prose | pages [10] -->
m

<!-- b003264 | prose | pages [10] -->
m

<!-- b003265 | prose | pages [10] -->
m

<!-- b003266 | prose | pages [10] -->
m

<!-- b003267 | prose | pages [10] -->
m

<!-- b003268 | prose | pages [10] -->
m

<!-- b003269 | prose | pages [10] -->
m

<!-- b003270 | prose | pages [10] -->
m

<!-- b003271 | prose | pages [10] -->
m m

<!-- b003272 | prose | pages [10] -->
m m

<!-- b003273 | prose | pages [10] -->
m m

<!-- b003274 | prose | pages [10] -->
m m

<!-- b003275 | prose | pages [10] -->
m m

<!-- b003276 | prose | pages [10] -->
m m

<!-- b003277 | prose | pages [10] -->
m m

<!-- b003278 | prose | pages [10] -->
estimate the distribution and uncertainty of the prediction results.

<!-- b003279 | prose | pages [10] -->
m

<!-- b003280 | prose | pages [10] -->
m

<!-- b003281 | prose | pages [10] -->
m

<!-- b003282 | prose | pages [10] -->
m

<!-- b003283 | prose | pages [10] -->
m

<!-- b003284 | prose | pages [10] -->
m

<!-- b003285 | prose | pages [10] -->
m

<!-- b003286 | prose | pages [10] -->
m

<!-- b003287 | prose | pages [10] -->
m

<!-- b003288 | prose | pages [10] -->
m

<!-- b003289 | prose | pages [10] -->
m

<!-- b003290 | prose | pages [10] -->
m

<!-- b003291 | prose | pages [10] -->
m

<!-- b003292 | prose | pages [10] -->
m

<!-- b003293 | prose | pages [10] -->
m

<!-- b003294 | prose | pages [10] -->
m

<!-- b003295 | prose | pages [10] -->
m

<!-- b003296 | prose | pages [10] -->
m

<!-- b003297 | prose | pages [10] -->
m

<!-- b003298 | prose | pages [10] -->
m

<!-- b003299 | prose | pages [10] -->
m

<!-- b003300 | prose | pages [10] -->
m

<!-- b003301 | prose | pages [10] -->
m

<!-- b003302 | prose | pages [10] -->
m

<!-- b003303 | prose | pages [10] -->
m

<!-- b003304 | prose | pages [10] -->
m

<!-- b003305 | prose | pages [10] -->
m

<!-- b003306 | prose | pages [10] -->
m

<!-- b003307 | prose | pages [10] -->
m

<!-- b003308 | prose | pages [10] -->
m

<!-- b003309 | prose | pages [10] -->
m

<!-- b003310 | prose | pages [10] -->
m

<!-- b003311 | prose | pages [10] -->
m

<!-- b003312 | prose | pages [10] -->
m

<!-- b003313 | prose | pages [10] -->
m

<!-- b003314 | prose | pages [10] -->
m

<!-- b003315 | prose | pages [10] -->
m

<!-- b003316 | prose | pages [10] -->
m

<!-- b003317 | prose | pages [10] -->
m

<!-- b003318 | prose | pages [10] -->
m

<!-- b003319 | prose | pages [10] -->
m

<!-- b003320 | prose | pages [10] -->
m

<!-- b003321 | prose | pages [10] -->
m

<!-- b003322 | prose | pages [10] -->
m

<!-- b003323 | prose | pages [10] -->
m

<!-- b003324 | prose | pages [10] -->
m

<!-- b003325 | prose | pages [10] -->
m

<!-- b003326 | prose | pages [10] -->
m

<!-- b003327 | prose | pages [10] -->
m

<!-- b003328 | prose | pages [10] -->
m

<!-- b003329 | prose | pages [10] -->
m

<!-- b003330 | prose | pages [10] -->
m

<!-- b003331 | prose | pages [10] -->
m

<!-- b003332 | prose | pages [10] -->
m

<!-- b003333 | prose | pages [10] -->
m

<!-- b003334 | prose | pages [10] -->
m

<!-- b003335 | prose | pages [10] -->
m

<!-- b003336 | prose | pages [10] -->
m

<!-- b003337 | prose | pages [10] -->
m

<!-- b003338 | prose | pages [10] -->
m

<!-- b003339 | prose | pages [10] -->
m

<!-- b003340 | prose | pages [10] -->
m

<!-- b003341 | prose | pages [10] -->
m

<!-- b003342 | prose | pages [10] -->
m

<!-- b003343 | prose | pages [10] -->
m

<!-- b003344 | prose | pages [10] -->
m

<!-- b003345 | prose | pages [10] -->
m

<!-- b003346 | prose | pages [10] -->
m

<!-- b003347 | prose | pages [10] -->
m

<!-- b003348 | prose | pages [10] -->
m

<!-- b003349 | prose | pages [10] -->
m

<!-- b003350 | prose | pages [10] -->
m

<!-- b003351 | prose | pages [10] -->
m

<!-- b003352 | prose | pages [10] -->
m

<!-- b003353 | prose | pages [10] -->
m

<!-- b003354 | prose | pages [10] -->
m

<!-- b003355 | prose | pages [10] -->
m

<!-- b003356 | prose | pages [10] -->
m

<!-- b003357 | prose | pages [10] -->
m

<!-- b003358 | prose | pages [10] -->
m

<!-- b003359 | prose | pages [10] -->
m

<!-- b003360 | prose | pages [10] -->
m

<!-- b003361 | prose | pages [10] -->
m

<!-- b003362 | prose | pages [10] -->
m

<!-- b003363 | prose | pages [10] -->
m

<!-- b003364 | prose | pages [10] -->
m

<!-- b003365 | prose | pages [10] -->
m

<!-- b003366 | prose | pages [10] -->
m

<!-- b003367 | prose | pages [10] -->
m

<!-- b003368 | prose | pages [10] -->
m

<!-- b003369 | prose | pages [10] -->
m

<!-- b003370 | prose | pages [10] -->
m

<!-- b003371 | prose | pages [10] -->
m

<!-- b003372 | prose | pages [10] -->
m

<!-- b003373 | prose | pages [10] -->
m

<!-- b003374 | prose | pages [10] -->
m

<!-- b003375 | prose | pages [10] -->
m

<!-- b003376 | prose | pages [10] -->
m

<!-- b003377 | prose | pages [10] -->
m

<!-- b003378 | prose | pages [10] -->
m

<!-- b003379 | prose | pages [10] -->
m

<!-- b003380 | prose | pages [10] -->
m

<!-- b003381 | prose | pages [10] -->
m

<!-- b003382 | prose | pages [10] -->
m

<!-- b003383 | prose | pages [10] -->
m

<!-- b003384 | prose | pages [10] -->
m

<!-- b003385 | prose | pages [10] -->
m

<!-- b003386 | prose | pages [10] -->
m

<!-- b003387 | prose | pages [10] -->
m

<!-- b003388 | prose | pages [10] -->
m

<!-- b003389 | prose | pages [10] -->
m

<!-- b003390 | prose | pages [10] -->
m

<!-- b003391 | prose | pages [10] -->
m

<!-- b003392 | prose | pages [10] -->
m

<!-- b003393 | prose | pages [10] -->
m

<!-- b003394 | prose | pages [10] -->
m

<!-- b003395 | prose | pages [10] -->
m

<!-- b003396 | prose | pages [10] -->
m

<!-- b003397 | prose | pages [10] -->
m

<!-- b003398 | prose | pages [10] -->
m

<!-- b003399 | prose | pages [10] -->
m

<!-- b003400 | prose | pages [10] -->
m

<!-- b003401 | prose | pages [10] -->
m

<!-- b003402 | prose | pages [10] -->
m

<!-- b003403 | prose | pages [10] -->
m

<!-- b003404 | prose | pages [10] -->
m

<!-- b003405 | prose | pages [10] -->
m

<!-- b003406 | prose | pages [10] -->
m

<!-- b003407 | prose | pages [10] -->
m

<!-- b003408 | prose | pages [10] -->
m

<!-- b003409 | prose | pages [10] -->
m

<!-- b003410 | prose | pages [10] -->
m

<!-- b003411 | prose | pages [10] -->
m

<!-- b003412 | prose | pages [10] -->
m

<!-- b003413 | prose | pages [10] -->
m

<!-- b003414 | prose | pages [10] -->
m

<!-- b003415 | prose | pages [10] -->
m

<!-- b003416 | prose | pages [10] -->
m

<!-- b003417 | prose | pages [10] -->
m

<!-- b003418 | prose | pages [10] -->
m

<!-- b003419 | prose | pages [10] -->
m

<!-- b003420 | prose | pages [10] -->
m

<!-- b003421 | prose | pages [10] -->
m

<!-- b003422 | prose | pages [10] -->
m

<!-- b003423 | prose | pages [10] -->
m

<!-- b003424 | prose | pages [10] -->
m

<!-- b003425 | prose | pages [10] -->
m

<!-- b003426 | prose | pages [10] -->
m

<!-- b003427 | prose | pages [10] -->
m

<!-- b003428 | prose | pages [10] -->
m

<!-- b003429 | prose | pages [10] -->
m

<!-- b003430 | prose | pages [10] -->
m

<!-- b003431 | prose | pages [10] -->
m

<!-- b003432 | prose | pages [10] -->
m

<!-- b003433 | prose | pages [10] -->
m

<!-- b003434 | prose | pages [10] -->
m

<!-- b003435 | prose | pages [10] -->
m

<!-- b003436 | prose | pages [10] -->
m

<!-- b003437 | prose | pages [10] -->
m

<!-- b003438 | prose | pages [10] -->
m m

<!-- b003439 | prose | pages [10] -->
m m m m

<!-- b003440 | prose | pages [10] -->
m m

<!-- b003441 | prose | pages [10] -->
m m

<!-- b003442 | prose | pages [10] -->
m m

<!-- b003443 | prose | pages [10] -->
m m m m m m m m

<!-- b003444 | prose | pages [10] -->
• Step 1: Randomly draw n samples from the original dataset to generate a resampled

<!-- b003445 | prose | pages [10] -->
m

<!-- b003446 | prose | pages [10] -->
m

<!-- b003447 | prose | pages [10] -->
m

<!-- b003448 | prose | pages [10] -->
m

<!-- b003449 | prose | pages [10] -->
m

<!-- b003450 | prose | pages [10] -->
m

<!-- b003451 | prose | pages [10] -->
m

<!-- b003452 | prose | pages [10] -->
m

<!-- b003453 | prose | pages [10] -->
m

<!-- b003454 | prose | pages [10] -->
m

<!-- b003455 | prose | pages [10] -->
m

<!-- b003456 | prose | pages [10] -->
m

<!-- b003457 | prose | pages [10] -->
m

<!-- b003458 | prose | pages [10] -->
m

<!-- b003459 | prose | pages [10] -->
m

<!-- b003460 | prose | pages [10] -->
m

<!-- b003461 | prose | pages [10] -->
m

<!-- b003462 | prose | pages [10] -->
m

<!-- b003463 | prose | pages [10] -->
m

<!-- b003464 | prose | pages [10] -->
m

<!-- b003465 | prose | pages [10] -->
m

<!-- b003466 | prose | pages [10] -->
m

<!-- b003467 | prose | pages [10] -->
m

<!-- b003468 | prose | pages [10] -->
m

<!-- b003469 | prose | pages [10] -->
m

<!-- b003470 | prose | pages [10] -->
m

<!-- b003471 | prose | pages [10] -->
m

<!-- b003472 | prose | pages [10] -->
m

<!-- b003473 | prose | pages [10] -->
m

<!-- b003474 | prose | pages [10] -->
m

<!-- b003475 | prose | pages [10] -->
m

<!-- b003476 | prose | pages [10] -->
m

<!-- b003477 | prose | pages [10] -->
m

<!-- b003478 | prose | pages [10] -->
m

<!-- b003479 | prose | pages [10] -->
m

<!-- b003480 | prose | pages [10] -->
m

<!-- b003481 | prose | pages [10] -->
m

<!-- b003482 | prose | pages [10] -->
m

<!-- b003483 | prose | pages [10] -->
m

<!-- b003484 | prose | pages [10] -->
m

<!-- b003485 | prose | pages [10] -->
m

<!-- b003486 | prose | pages [10] -->
m

<!-- b003487 | prose | pages [10] -->
m

<!-- b003488 | prose | pages [10] -->
m

<!-- b003489 | prose | pages [10] -->
m

<!-- b003490 | prose | pages [10] -->
m

<!-- b003491 | prose | pages [10] -->
m

<!-- b003492 | prose | pages [10] -->
m

<!-- b003493 | prose | pages [10] -->
m

<!-- b003494 | prose | pages [10] -->
m

<!-- b003495 | prose | pages [10] -->
m

<!-- b003496 | prose | pages [10] -->
m

<!-- b003497 | prose | pages [10] -->
m

<!-- b003498 | prose | pages [10] -->
m

<!-- b003499 | prose | pages [10] -->
m

<!-- b003500 | prose | pages [10] -->
m

<!-- b003501 | prose | pages [10] -->
m

<!-- b003502 | prose | pages [10] -->
m

<!-- b003503 | prose | pages [10] -->
m

<!-- b003504 | prose | pages [10] -->
m

<!-- b003505 | prose | pages [10] -->
m

<!-- b003506 | prose | pages [10] -->
m

<!-- b003507 | prose | pages [10] -->
m

<!-- b003508 | prose | pages [10] -->
m

<!-- b003509 | prose | pages [10] -->
m

<!-- b003510 | prose | pages [10] -->
m

<!-- b003511 | prose | pages [10] -->
m

<!-- b003512 | prose | pages [10] -->
m

<!-- b003513 | prose | pages [10] -->
m

<!-- b003514 | prose | pages [10] -->
m

<!-- b003515 | prose | pages [10] -->
m

<!-- b003516 | prose | pages [10] -->
m

<!-- b003517 | prose | pages [10] -->
m

<!-- b003518 | prose | pages [10] -->
m

<!-- b003519 | prose | pages [10] -->
m

<!-- b003520 | prose | pages [10] -->
m

<!-- b003521 | prose | pages [10] -->
m

<!-- b003522 | prose | pages [10] -->
m

<!-- b003523 | prose | pages [10] -->
m

<!-- b003524 | prose | pages [10] -->
m

<!-- b003525 | prose | pages [10] -->
m

<!-- b003526 | prose | pages [10] -->
m

<!-- b003527 | prose | pages [10] -->
m

<!-- b003528 | prose | pages [10] -->
m

<!-- b003529 | prose | pages [10] -->
m

<!-- b003530 | prose | pages [10] -->
m

<!-- b003531 | prose | pages [10] -->
m

<!-- b003532 | prose | pages [10] -->
m

<!-- b003533 | prose | pages [10] -->
m

<!-- b003534 | prose | pages [10] -->
m

<!-- b003535 | prose | pages [10] -->
m

<!-- b003536 | prose | pages [10] -->
m

<!-- b003537 | prose | pages [10] -->
m

<!-- b003538 | prose | pages [10] -->
m

<!-- b003539 | prose | pages [10] -->
m

<!-- b003540 | prose | pages [10] -->
m

<!-- b003541 | prose | pages [10] -->
m

<!-- b003542 | prose | pages [10] -->
m

<!-- b003543 | prose | pages [10] -->
m

<!-- b003544 | prose | pages [10] -->
m

<!-- b003545 | prose | pages [10] -->
m

<!-- b003546 | prose | pages [10] -->
m

<!-- b003547 | prose | pages [10] -->
m

<!-- b003548 | prose | pages [10] -->
m

<!-- b003549 | prose | pages [10] -->
m

<!-- b003550 | prose | pages [10] -->
m

<!-- b003551 | prose | pages [10] -->
m

<!-- b003552 | prose | pages [10] -->
m

<!-- b003553 | prose | pages [10] -->
m

<!-- b003554 | prose | pages [10] -->
m

<!-- b003555 | prose | pages [10] -->
m

<!-- b003556 | prose | pages [10] -->
m

<!-- b003557 | prose | pages [10] -->
m

<!-- b003558 | prose | pages [10] -->
m

<!-- b003559 | prose | pages [10] -->
m

<!-- b003560 | prose | pages [10] -->
m

<!-- b003561 | prose | pages [10] -->
m

<!-- b003562 | prose | pages [10] -->
dataset X∗= {x∗

<!-- b003563 | prose | pages [10] -->
n}.

<!-- b003564 | prose | pages [10] -->
m

<!-- b003565 | prose | pages [10] -->
m

<!-- b003566 | prose | pages [10] -->
m

<!-- b003567 | prose | pages [10] -->
m

<!-- b003568 | prose | pages [10] -->
m

<!-- b003569 | prose | pages [10] -->
m

<!-- b003570 | prose | pages [10] -->
m

<!-- b003571 | prose | pages [10] -->
m

<!-- b003572 | prose | pages [10] -->
m

<!-- b003573 | prose | pages [10] -->
m

<!-- b003574 | prose | pages [10] -->
m

<!-- b003575 | prose | pages [10] -->
m

<!-- b003576 | prose | pages [10] -->
m

<!-- b003577 | prose | pages [10] -->
m

<!-- b003578 | prose | pages [10] -->
m

<!-- b003579 | prose | pages [10] -->
m

<!-- b003580 | prose | pages [10] -->
m

<!-- b003581 | prose | pages [10] -->
1, x∗ 2, ..., x∗

<!-- b003582 | prose | pages [10] -->
m

<!-- b003583 | prose | pages [10] -->
m

<!-- b003584 | prose | pages [10] -->
m

<!-- b003585 | prose | pages [10] -->
m

<!-- b003586 | prose | pages [10] -->
m

<!-- b003587 | prose | pages [10] -->
m

<!-- b003588 | prose | pages [10] -->
m

<!-- b003589 | prose | pages [10] -->
m

<!-- b003590 | prose | pages [10] -->
m

<!-- b003591 | prose | pages [10] -->
m

<!-- b003592 | prose | pages [10] -->
m

<!-- b003593 | prose | pages [10] -->
m

<!-- b003594 | prose | pages [10] -->
m

<!-- b003595 | prose | pages [10] -->
m

<!-- b003596 | prose | pages [10] -->
m

<!-- b003597 | prose | pages [10] -->
m

<!-- b003598 | prose | pages [10] -->
m

<!-- b003599 | prose | pages [10] -->
m

<!-- b003600 | prose | pages [10] -->
m

<!-- b003601 | prose | pages [10] -->
m

<!-- b003602 | prose | pages [10] -->
m

<!-- b003603 | prose | pages [10] -->
m

<!-- b003604 | prose | pages [10] -->
m

<!-- b003605 | prose | pages [10] -->
m

<!-- b003606 | prose | pages [10] -->
m

<!-- b003607 | prose | pages [10] -->
m

<!-- b003608 | prose | pages [10] -->
m

<!-- b003609 | prose | pages [10] -->
m

<!-- b003610 | prose | pages [10] -->
m

<!-- b003611 | prose | pages [10] -->
m

<!-- b003612 | prose | pages [10] -->
m

<!-- b003613 | prose | pages [10] -->
m

<!-- b003614 | prose | pages [10] -->
m

<!-- b003615 | prose | pages [10] -->
m

<!-- b003616 | prose | pages [10] -->
m

<!-- b003617 | prose | pages [10] -->
m

<!-- b003618 | prose | pages [10] -->
m

<!-- b003619 | prose | pages [10] -->
m

<!-- b003620 | prose | pages [10] -->
m

<!-- b003621 | prose | pages [10] -->
m m

<!-- b003622 | prose | pages [10] -->
m m

<!-- b003623 | prose | pages [10] -->
m m

<!-- b003624 | prose | pages [10] -->
m m

<!-- b003625 | prose | pages [10] -->
m m

<!-- b003626 | prose | pages [10] -->
m m m m m m m m m m m m

<!-- b003627 | prose | pages [10] -->
m m

<!-- b003628 | prose | pages [10] -->
m m

<!-- b003629 | prose | pages [10] -->
• Step 2: Compute the statisticon bθ∗the resampled dataset.

<!-- b003630 | prose | pages [10] -->
• Step 3: Repeat the above process B times to obtain B statistics, bθ∗ 1, ..., c

<!-- b003631 | prose | pages [10] -->
B.

<!-- b003632 | prose | pages [10] -->
θ∗

<!-- b003633 | prose | pages [10] -->
• Step 4: Estimate Standard Error and Confidence Interval. Based on the B resampling results, estimate the standard error (SE) and confidence interval for the statistic. As- suming bθ∗has a sample mean [

<!-- b003634 | prose | pages [10] -->
mean , the standard error is calculated as:Equation 10

<!-- b003635 | prose | pages [10] -->
θ∗

<!-- b003636 | prose | pages [10] -->
v u

<!-- b003637 | prose | pages [10] -->


<!-- b003638 | prose | pages [10] -->


<!-- b003639 | prose | pages [10] -->
u t 1

<!-- b003640 | prose | pages [10] -->
bθ

<!-- b003641 | prose | pages [10] -->
SE

<!-- b003642 | prose | pages [10] -->
=

<!-- b003643 | prose | pages [10] -->


<!-- b003644 | prose | pages [10] -->
2

<!-- b003645 | prose | pages [10] -->
B X

<!-- b003646 | prose | pages [10] -->
b −[

<!-- b003647 | prose | pages [10] -->
bθ∗

<!-- b003648 | prose | pages [10] -->
(10)

<!-- b003649 | prose | pages [10] -->
θ∗

<!-- b003650 | prose | pages [10] -->
mean

<!-- b003651 | prose | pages [10] -->
B B

<!-- b003652 | prose | pages [10] -->
b=1

<!-- b003653 | prose | pages [10] -->
关注数学模型

<!-- b003654 | furniture | pages [10] -->
2

<!-- b003655 | furniture | pages [10] -->
MATHmodels

<!-- b003656 | furniture | pages [10] -->
获取更多资讯

<!-- b003657 | furniture | pages [11] -->
Team # 2510862

<!-- b003658 | furniture | pages [11] -->
Page 11 of 25

<!-- b003659 | prose | pages [11] -->
For the confidence interval, if we want to calculate the 95% confidence interval, we can use the percentiles of the B statistics:

<!-- b003660 | prose | pages [11] -->


<!-- b003661 | prose | pages [11] -->


<!-- b003662 | prose | pages [11] -->
2.5%, bθ∗ 1, d

<!-- b003663 | prose | pages [11] -->
2, ..., c

<!-- b003664 | prose | pages [11] -->
θ.0∗

<!-- b003665 | prose | pages [11] -->
θ∗

<!-- b003666 | prose | pages [11] -->
Lower bound = percentile

<!-- b003667 | prose | pages [11] -->
微信公众号：数学模型

<!-- b003668 | prose | pages [11] -->
B

<!-- b003669 | prose | pages [11] -->


<!-- b003670 | prose | pages [11] -->


<!-- b003671 | prose | pages [11] -->
97.5%, bθ∗ 1, bθ∗ 2, ..., c θ∗

<!-- b003672 | prose | pages [11] -->
Upper bound = percentile

<!-- b003673 | prose | pages [11] -->
B

<!-- b003674 | prose | pages [11] -->
微信号：MATHmodels

<!-- b003675 | caption | pages [11] -->
Figure 6: prediction intervals for medal counts

<!-- b003676 | prose | pages [11] -->
Possible Countries to Improve or Decline 5.2.3

<!-- b003677 | prose | pages [11] -->
Possible Countries to Improve:

<!-- b003678 | heading | pages [11] -->
1. United States (2024: 40 Golds, Predicted 2028: 56 Golds): As the host country for

<!-- b003679 | prose | pages [11] -->
the 2028 Los Angeles Olympics, the United States will benefit from the home advantage, which is expected to enhance its performance. Furthermore, the U.S. has consistently ranked among the top countries in terms of gold medals in past Olympics, with a strong pool of athletes. Therefore, it is expected that the U.S. will maintain its lead in 2028 and further increase its gold medal count.

<!-- b003680 | heading | pages [11] -->
2. Australia (2024: 18 Golds, Predicted 2028: 25 Golds): As the host country for the

<!-- b003681 | prose | pages [11] -->
2032 Olympics, Australia has been preparing extensively for future Games. A traditional sports powerhouse, Australia has already demonstrated strong performances across var- ious events. In 2028, Australia is expected to make significant progress, especially in swimming, rowing, and other aquatic sports, resulting in a likely increase in gold medals.

<!-- b003682 | heading | pages [11] -->
3. France (2024: 16 Golds, Predicted 2028: 19 Golds): Having successfully hosted the

<!-- b003683 | prose | pages [11] -->
2024 Paris Olympics, France has made significant improvements in athlete training and infrastructure. With a well-established athlete development system and solid training ex- perience, France’s preparations for 2024 are expected to positively impact its performance in the 2028 Los Angeles Olympics.

<!-- b003684 | prose | pages [11] -->
Possible Countries to Decline:

<!-- b003685 | heading | pages [11] -->
1. China (2024: 40 Golds, Predicted 2028: 33 Golds): Although China has consistently

<!-- b003686 | prose | pages [11] -->
performed strongly in the Olympics, its gold medal count is predicted to decrease slightly

<!-- b003687 | furniture | pages [12] -->
Team # 2510862

<!-- b003688 | furniture | pages [12] -->
Page 12 of 25

<!-- b003689 | prose | pages [12] -->
in 2028. With other countries, such as the U.S. and Australia, becoming more competitive, China may face increased challenges. The U.S. will have the home advantage in 2028, which could make it more difficult for China to dominate in key events.

<!-- b003690 | heading | pages [12] -->
2. Japan (2024: 20 Golds, Predicted 2028: 14 Golds): Despite Japan’s impressive

<!-- b003691 | prose | pages [12] -->
performance in 2024, by 2028, it will have been eight years since the Tokyo Olympics. Over time, many of the athletes who won gold medals in Tokyo may have retired, and there is uncertainty about whether new athletes can quickly fill these gaps. Therefore, Japan is expected to see a decline in its gold medal count in 2028.

<!-- b003692 | heading | pages [12] -->
3. Netherlands (2024: 15 Golds, Predicted 2028: 7 Golds): The Netherlands ranked

<!-- b003693 | prose | pages [12] -->
6th in the gold medal tally in 2024, achieving outstanding results, likely aided by its prox- imity to Paris, which boosted athlete morale and fan support. However, with the 2028 Olympics being held in Los Angeles, far from Europe, several factors could affect the Dutch athletes’ preparation and performance. As a result, despite strong results in 2024, the Netherlands is expected to see a decrease in its gold medal count in 2028.

<!-- b003694 | prose | pages [12] -->
Task 2: Multifaceted analysis for Predicting the Next "First- 6 Medal" Winner

<!-- b003695 | prose | pages [12] -->
Behind the medals at each Olympic Games is not only a representation of the strength of the country’s athletes, but also a reflection of the investment, nurturing and develop- ment of the Olympic Movement in each country. Based on the available historical data of the Olympic Games, there are many countries in the world that have long failed to win

<!-- b003696 | prose | pages [12] -->
m

<!-- b003697 | prose | pages [12] -->
m

<!-- b003698 | prose | pages [12] -->
m

<!-- b003699 | prose | pages [12] -->
m

<!-- b003700 | prose | pages [12] -->
m

<!-- b003701 | prose | pages [12] -->
m

<!-- b003702 | prose | pages [12] -->
m

<!-- b003703 | prose | pages [12] -->
m

<!-- b003704 | prose | pages [12] -->
m

<!-- b003705 | prose | pages [12] -->
m

<!-- b003706 | prose | pages [12] -->
m

<!-- b003707 | prose | pages [12] -->
m

<!-- b003708 | prose | pages [12] -->
m

<!-- b003709 | prose | pages [12] -->
m

<!-- b003710 | prose | pages [12] -->
m

<!-- b003711 | prose | pages [12] -->
m

<!-- b003712 | prose | pages [12] -->
m

<!-- b003713 | prose | pages [12] -->
m

<!-- b003714 | prose | pages [12] -->
m

<!-- b003715 | prose | pages [12] -->
m

<!-- b003716 | prose | pages [12] -->
m

<!-- b003717 | prose | pages [12] -->
m

<!-- b003718 | prose | pages [12] -->
m

<!-- b003719 | prose | pages [12] -->
m

<!-- b003720 | prose | pages [12] -->
m

<!-- b003721 | prose | pages [12] -->
m

<!-- b003722 | prose | pages [12] -->
m

<!-- b003723 | prose | pages [12] -->
m

<!-- b003724 | prose | pages [12] -->
m

<!-- b003725 | prose | pages [12] -->
m

<!-- b003726 | prose | pages [12] -->
m

<!-- b003727 | prose | pages [12] -->
m

<!-- b003728 | prose | pages [12] -->
m

<!-- b003729 | prose | pages [12] -->
m

<!-- b003730 | prose | pages [12] -->
m

<!-- b003731 | prose | pages [12] -->
m

<!-- b003732 | prose | pages [12] -->
m

<!-- b003733 | prose | pages [12] -->
m

<!-- b003734 | prose | pages [12] -->
m

<!-- b003735 | prose | pages [12] -->
m

<!-- b003736 | prose | pages [12] -->
m

<!-- b003737 | prose | pages [12] -->
m

<!-- b003738 | prose | pages [12] -->
m

<!-- b003739 | prose | pages [12] -->
m

<!-- b003740 | prose | pages [12] -->
m

<!-- b003741 | prose | pages [12] -->
m

<!-- b003742 | prose | pages [12] -->
m

<!-- b003743 | prose | pages [12] -->
m

<!-- b003744 | prose | pages [12] -->
m

<!-- b003745 | prose | pages [12] -->
m

<!-- b003746 | prose | pages [12] -->
m

<!-- b003747 | prose | pages [12] -->
m

<!-- b003748 | prose | pages [12] -->
m

<!-- b003749 | prose | pages [12] -->
m

<!-- b003750 | prose | pages [12] -->
m

<!-- b003751 | prose | pages [12] -->
m

<!-- b003752 | prose | pages [12] -->
m

<!-- b003753 | prose | pages [12] -->
m

<!-- b003754 | prose | pages [12] -->
m

<!-- b003755 | prose | pages [12] -->
m

<!-- b003756 | prose | pages [12] -->
m

<!-- b003757 | prose | pages [12] -->
m

<!-- b003758 | prose | pages [12] -->
m

<!-- b003759 | prose | pages [12] -->
m

<!-- b003760 | prose | pages [12] -->
m

<!-- b003761 | prose | pages [12] -->
m

<!-- b003762 | prose | pages [12] -->
m

<!-- b003763 | prose | pages [12] -->
m

<!-- b003764 | prose | pages [12] -->
m

<!-- b003765 | prose | pages [12] -->
m

<!-- b003766 | prose | pages [12] -->
m

<!-- b003767 | prose | pages [12] -->
m

<!-- b003768 | prose | pages [12] -->
m

<!-- b003769 | prose | pages [12] -->
m

<!-- b003770 | prose | pages [12] -->
m

<!-- b003771 | prose | pages [12] -->
m

<!-- b003772 | prose | pages [12] -->
m

<!-- b003773 | prose | pages [12] -->
m

<!-- b003774 | prose | pages [12] -->
m

<!-- b003775 | prose | pages [12] -->
m

<!-- b003776 | prose | pages [12] -->
m

<!-- b003777 | prose | pages [12] -->
m

<!-- b003778 | prose | pages [12] -->
m

<!-- b003779 | prose | pages [12] -->
m

<!-- b003780 | prose | pages [12] -->
m

<!-- b003781 | prose | pages [12] -->
m

<!-- b003782 | prose | pages [12] -->
m

<!-- b003783 | prose | pages [12] -->
m

<!-- b003784 | prose | pages [12] -->
m

<!-- b003785 | prose | pages [12] -->
m

<!-- b003786 | prose | pages [12] -->
m

<!-- b003787 | prose | pages [12] -->
m

<!-- b003788 | prose | pages [12] -->
m

<!-- b003789 | prose | pages [12] -->
m

<!-- b003790 | prose | pages [12] -->
m

<!-- b003791 | prose | pages [12] -->
medals, and their performance in the past few Olympic Games has often fallen short of

<!-- b003792 | prose | pages [12] -->
m

<!-- b003793 | prose | pages [12] -->
m

<!-- b003794 | prose | pages [12] -->
m

<!-- b003795 | prose | pages [12] -->
m

<!-- b003796 | prose | pages [12] -->
m

<!-- b003797 | prose | pages [12] -->
m

<!-- b003798 | prose | pages [12] -->
m

<!-- b003799 | prose | pages [12] -->
m

<!-- b003800 | prose | pages [12] -->
m

<!-- b003801 | prose | pages [12] -->
m

<!-- b003802 | prose | pages [12] -->
m

<!-- b003803 | prose | pages [12] -->
m

<!-- b003804 | prose | pages [12] -->
m

<!-- b003805 | prose | pages [12] -->
m

<!-- b003806 | prose | pages [12] -->
m

<!-- b003807 | prose | pages [12] -->
m

<!-- b003808 | prose | pages [12] -->
m

<!-- b003809 | prose | pages [12] -->
m

<!-- b003810 | prose | pages [12] -->
m

<!-- b003811 | prose | pages [12] -->
m

<!-- b003812 | prose | pages [12] -->
m

<!-- b003813 | prose | pages [12] -->
m

<!-- b003814 | prose | pages [12] -->
m

<!-- b003815 | prose | pages [12] -->
m

<!-- b003816 | prose | pages [12] -->
m

<!-- b003817 | prose | pages [12] -->
m

<!-- b003818 | prose | pages [12] -->
m

<!-- b003819 | prose | pages [12] -->
m

<!-- b003820 | prose | pages [12] -->
m

<!-- b003821 | prose | pages [12] -->
m

<!-- b003822 | prose | pages [12] -->
m

<!-- b003823 | prose | pages [12] -->
m

<!-- b003824 | prose | pages [12] -->
m

<!-- b003825 | prose | pages [12] -->
m

<!-- b003826 | prose | pages [12] -->
m

<!-- b003827 | prose | pages [12] -->
m

<!-- b003828 | prose | pages [12] -->
m

<!-- b003829 | prose | pages [12] -->
m

<!-- b003830 | prose | pages [12] -->
m

<!-- b003831 | prose | pages [12] -->
m

<!-- b003832 | prose | pages [12] -->
m

<!-- b003833 | prose | pages [12] -->
m

<!-- b003834 | prose | pages [12] -->
m

<!-- b003835 | prose | pages [12] -->
m

<!-- b003836 | prose | pages [12] -->
m

<!-- b003837 | prose | pages [12] -->
m

<!-- b003838 | prose | pages [12] -->
m

<!-- b003839 | prose | pages [12] -->
m

<!-- b003840 | prose | pages [12] -->
m

<!-- b003841 | prose | pages [12] -->
m

<!-- b003842 | prose | pages [12] -->
m

<!-- b003843 | prose | pages [12] -->
m

<!-- b003844 | prose | pages [12] -->
m

<!-- b003845 | prose | pages [12] -->
m

<!-- b003846 | prose | pages [12] -->
m

<!-- b003847 | prose | pages [12] -->
m

<!-- b003848 | prose | pages [12] -->
m

<!-- b003849 | prose | pages [12] -->
m

<!-- b003850 | prose | pages [12] -->
m

<!-- b003851 | prose | pages [12] -->
m

<!-- b003852 | prose | pages [12] -->
m

<!-- b003853 | prose | pages [12] -->
m

<!-- b003854 | prose | pages [12] -->
m

<!-- b003855 | prose | pages [12] -->
m

<!-- b003856 | prose | pages [12] -->
m

<!-- b003857 | prose | pages [12] -->
m

<!-- b003858 | prose | pages [12] -->
m

<!-- b003859 | prose | pages [12] -->
m

<!-- b003860 | prose | pages [12] -->
m

<!-- b003861 | prose | pages [12] -->
m

<!-- b003862 | prose | pages [12] -->
m

<!-- b003863 | prose | pages [12] -->
m

<!-- b003864 | prose | pages [12] -->
m

<!-- b003865 | prose | pages [12] -->
m

<!-- b003866 | prose | pages [12] -->
m

<!-- b003867 | prose | pages [12] -->
m

<!-- b003868 | prose | pages [12] -->
m

<!-- b003869 | prose | pages [12] -->
m

<!-- b003870 | prose | pages [12] -->
m

<!-- b003871 | prose | pages [12] -->
m

<!-- b003872 | prose | pages [12] -->
m

<!-- b003873 | prose | pages [12] -->
m

<!-- b003874 | prose | pages [12] -->
m

<!-- b003875 | prose | pages [12] -->
m

<!-- b003876 | prose | pages [12] -->
m

<!-- b003877 | prose | pages [12] -->
m

<!-- b003878 | prose | pages [12] -->
m

<!-- b003879 | prose | pages [12] -->
m

<!-- b003880 | prose | pages [12] -->
m

<!-- b003881 | prose | pages [12] -->
m

<!-- b003882 | prose | pages [12] -->
m

<!-- b003883 | prose | pages [12] -->
m

<!-- b003884 | prose | pages [12] -->
m

<!-- b003885 | prose | pages [12] -->
m

<!-- b003886 | prose | pages [12] -->
m

<!-- b003887 | prose | pages [12] -->
m

<!-- b003888 | prose | pages [12] -->
m

<!-- b003889 | prose | pages [12] -->
m

<!-- b003890 | prose | pages [12] -->
m

<!-- b003891 | prose | pages [12] -->
m

<!-- b003892 | prose | pages [12] -->
m

<!-- b003893 | prose | pages [12] -->
m

<!-- b003894 | prose | pages [12] -->
m

<!-- b003895 | prose | pages [12] -->
m

<!-- b003896 | prose | pages [12] -->
m

<!-- b003897 | prose | pages [12] -->
m

<!-- b003898 | prose | pages [12] -->
m

<!-- b003899 | prose | pages [12] -->
m

<!-- b003900 | prose | pages [12] -->
m

<!-- b003901 | prose | pages [12] -->
m

<!-- b003902 | prose | pages [12] -->
m

<!-- b003903 | prose | pages [12] -->
m

<!-- b003904 | prose | pages [12] -->
m

<!-- b003905 | prose | pages [12] -->
m

<!-- b003906 | prose | pages [12] -->
m

<!-- b003907 | prose | pages [12] -->
m

<!-- b003908 | prose | pages [12] -->
m

<!-- b003909 | prose | pages [12] -->
m

<!-- b003910 | prose | pages [12] -->
m

<!-- b003911 | prose | pages [12] -->
m

<!-- b003912 | prose | pages [12] -->
m

<!-- b003913 | prose | pages [12] -->
m

<!-- b003914 | prose | pages [12] -->
m

<!-- b003915 | prose | pages [12] -->
m

<!-- b003916 | prose | pages [12] -->
m

<!-- b003917 | prose | pages [12] -->
m

<!-- b003918 | prose | pages [12] -->
m

<!-- b003919 | prose | pages [12] -->
m

<!-- b003920 | prose | pages [12] -->
m

<!-- b003921 | prose | pages [12] -->
m

<!-- b003922 | prose | pages [12] -->
m

<!-- b003923 | prose | pages [12] -->
m

<!-- b003924 | prose | pages [12] -->
m

<!-- b003925 | prose | pages [12] -->
m

<!-- b003926 | prose | pages [12] -->
m

<!-- b003927 | prose | pages [12] -->
m

<!-- b003928 | prose | pages [12] -->
significant expectations.

<!-- b003929 | prose | pages [12] -->
m

<!-- b003930 | prose | pages [12] -->
m

<!-- b003931 | prose | pages [12] -->
m

<!-- b003932 | prose | pages [12] -->
m

<!-- b003933 | prose | pages [12] -->
m

<!-- b003934 | prose | pages [12] -->
m

<!-- b003935 | prose | pages [12] -->
m

<!-- b003936 | prose | pages [12] -->
m

<!-- b003937 | prose | pages [12] -->
m

<!-- b003938 | prose | pages [12] -->
m

<!-- b003939 | prose | pages [12] -->
m

<!-- b003940 | prose | pages [12] -->
m

<!-- b003941 | prose | pages [12] -->
m

<!-- b003942 | prose | pages [12] -->
m

<!-- b003943 | prose | pages [12] -->
m

<!-- b003944 | prose | pages [12] -->
m

<!-- b003945 | prose | pages [12] -->
m

<!-- b003946 | prose | pages [12] -->
m

<!-- b003947 | prose | pages [12] -->
m

<!-- b003948 | prose | pages [12] -->
m

<!-- b003949 | prose | pages [12] -->
m

<!-- b003950 | prose | pages [12] -->
m

<!-- b003951 | prose | pages [12] -->
m

<!-- b003952 | prose | pages [12] -->
m

<!-- b003953 | prose | pages [12] -->
m

<!-- b003954 | prose | pages [12] -->
m

<!-- b003955 | prose | pages [12] -->
m

<!-- b003956 | prose | pages [12] -->
m

<!-- b003957 | prose | pages [12] -->
m

<!-- b003958 | prose | pages [12] -->
m

<!-- b003959 | prose | pages [12] -->
m

<!-- b003960 | prose | pages [12] -->
m

<!-- b003961 | prose | pages [12] -->
m

<!-- b003962 | prose | pages [12] -->
m

<!-- b003963 | prose | pages [12] -->
m

<!-- b003964 | prose | pages [12] -->
m

<!-- b003965 | prose | pages [12] -->
m

<!-- b003966 | prose | pages [12] -->
m

<!-- b003967 | prose | pages [12] -->
m

<!-- b003968 | prose | pages [12] -->
m

<!-- b003969 | prose | pages [12] -->
m

<!-- b003970 | prose | pages [12] -->
m

<!-- b003971 | prose | pages [12] -->
m

<!-- b003972 | prose | pages [12] -->
m

<!-- b003973 | prose | pages [12] -->
m

<!-- b003974 | prose | pages [12] -->
m

<!-- b003975 | prose | pages [12] -->
m

<!-- b003976 | prose | pages [12] -->
m

<!-- b003977 | prose | pages [12] -->
m

<!-- b003978 | prose | pages [12] -->
m

<!-- b003979 | prose | pages [12] -->
m

<!-- b003980 | prose | pages [12] -->
m

<!-- b003981 | prose | pages [12] -->
m

<!-- b003982 | prose | pages [12] -->
m

<!-- b003983 | prose | pages [12] -->
m

<!-- b003984 | prose | pages [12] -->
m

<!-- b003985 | prose | pages [12] -->
m

<!-- b003986 | prose | pages [12] -->
m

<!-- b003987 | prose | pages [12] -->
m

<!-- b003988 | prose | pages [12] -->
m

<!-- b003989 | prose | pages [12] -->
m

<!-- b003990 | prose | pages [12] -->
m

<!-- b003991 | prose | pages [12] -->
m

<!-- b003992 | prose | pages [12] -->
m

<!-- b003993 | prose | pages [12] -->
m

<!-- b003994 | prose | pages [12] -->
m

<!-- b003995 | prose | pages [12] -->
m

<!-- b003996 | prose | pages [12] -->
m

<!-- b003997 | prose | pages [12] -->
m

<!-- b003998 | prose | pages [12] -->
m

<!-- b003999 | prose | pages [12] -->
m

<!-- b004000 | prose | pages [12] -->
m

<!-- b004001 | prose | pages [12] -->
m

<!-- b004002 | prose | pages [12] -->
m

<!-- b004003 | prose | pages [12] -->
m

<!-- b004004 | prose | pages [12] -->
m

<!-- b004005 | prose | pages [12] -->
m

<!-- b004006 | prose | pages [12] -->
m

<!-- b004007 | prose | pages [12] -->
m

<!-- b004008 | prose | pages [12] -->
m

<!-- b004009 | prose | pages [12] -->
m

<!-- b004010 | prose | pages [12] -->
m

<!-- b004011 | prose | pages [12] -->
m

<!-- b004012 | prose | pages [12] -->
m

<!-- b004013 | prose | pages [12] -->
m

<!-- b004014 | prose | pages [12] -->
m

<!-- b004015 | prose | pages [12] -->
m

<!-- b004016 | prose | pages [12] -->
m

<!-- b004017 | prose | pages [12] -->
m

<!-- b004018 | prose | pages [12] -->
m

<!-- b004019 | prose | pages [12] -->
m

<!-- b004020 | prose | pages [12] -->
m

<!-- b004021 | prose | pages [12] -->
m

<!-- b004022 | prose | pages [12] -->
m

<!-- b004023 | prose | pages [12] -->
m

<!-- b004024 | prose | pages [12] -->
m

<!-- b004025 | prose | pages [12] -->
m

<!-- b004026 | prose | pages [12] -->
m

<!-- b004027 | prose | pages [12] -->
m

<!-- b004028 | prose | pages [12] -->
m

<!-- b004029 | prose | pages [12] -->
m

<!-- b004030 | prose | pages [12] -->
m

<!-- b004031 | prose | pages [12] -->
m

<!-- b004032 | prose | pages [12] -->
m

<!-- b004033 | prose | pages [12] -->
m

<!-- b004034 | prose | pages [12] -->
m

<!-- b004035 | prose | pages [12] -->
m

<!-- b004036 | prose | pages [12] -->
m

<!-- b004037 | prose | pages [12] -->
m

<!-- b004038 | prose | pages [12] -->
m

<!-- b004039 | prose | pages [12] -->
m

<!-- b004040 | prose | pages [12] -->
m

<!-- b004041 | prose | pages [12] -->
m

<!-- b004042 | prose | pages [12] -->
m

<!-- b004043 | prose | pages [12] -->
m

<!-- b004044 | prose | pages [12] -->
m

<!-- b004045 | prose | pages [12] -->
m

<!-- b004046 | prose | pages [12] -->
m

<!-- b004047 | prose | pages [12] -->
m

<!-- b004048 | prose | pages [12] -->
m

<!-- b004049 | prose | pages [12] -->
m

<!-- b004050 | prose | pages [12] -->
m

<!-- b004051 | prose | pages [12] -->
m

<!-- b004052 | prose | pages [12] -->
m

<!-- b004053 | prose | pages [12] -->
m

<!-- b004054 | prose | pages [12] -->
m

<!-- b004055 | prose | pages [12] -->
m

<!-- b004056 | prose | pages [12] -->
m

<!-- b004057 | prose | pages [12] -->
m

<!-- b004058 | prose | pages [12] -->
m

<!-- b004059 | prose | pages [12] -->
m

<!-- b004060 | prose | pages [12] -->
m

<!-- b004061 | prose | pages [12] -->
m

<!-- b004062 | prose | pages [12] -->
m

<!-- b004063 | prose | pages [12] -->
m

<!-- b004064 | prose | pages [12] -->
m

<!-- b004065 | prose | pages [12] -->
m

<!-- b004066 | prose | pages [12] -->
m

<!-- b004067 | prose | pages [12] -->
m

<!-- b004068 | prose | pages [12] -->
m

<!-- b004069 | prose | pages [12] -->
m

<!-- b004070 | prose | pages [12] -->
m

<!-- b004071 | prose | pages [12] -->
m

<!-- b004072 | prose | pages [12] -->
m

<!-- b004073 | prose | pages [12] -->
m

<!-- b004074 | prose | pages [12] -->
m

<!-- b004075 | prose | pages [12] -->
m

<!-- b004076 | prose | pages [12] -->
m

<!-- b004077 | prose | pages [12] -->
m

<!-- b004078 | prose | pages [12] -->
m

<!-- b004079 | prose | pages [12] -->
m

<!-- b004080 | prose | pages [12] -->
m

<!-- b004081 | prose | pages [12] -->
m

<!-- b004082 | prose | pages [12] -->
m

<!-- b004083 | prose | pages [12] -->
m

<!-- b004084 | prose | pages [12] -->
m

<!-- b004085 | prose | pages [12] -->
m

<!-- b004086 | prose | pages [12] -->
m

<!-- b004087 | prose | pages [12] -->
m

<!-- b004088 | prose | pages [12] -->
m

<!-- b004089 | prose | pages [12] -->
m

<!-- b004090 | prose | pages [12] -->
m

<!-- b004091 | prose | pages [12] -->
m

<!-- b004092 | prose | pages [12] -->
m

<!-- b004093 | prose | pages [12] -->
m

<!-- b004094 | prose | pages [12] -->
m

<!-- b004095 | prose | pages [12] -->
m

<!-- b004096 | prose | pages [12] -->
m

<!-- b004097 | prose | pages [12] -->
m

<!-- b004098 | prose | pages [12] -->
m

<!-- b004099 | prose | pages [12] -->
m

<!-- b004100 | prose | pages [12] -->
m

<!-- b004101 | prose | pages [12] -->
m

<!-- b004102 | prose | pages [12] -->
m

<!-- b004103 | prose | pages [12] -->
m

<!-- b004104 | prose | pages [12] -->
m

<!-- b004105 | prose | pages [12] -->
m

<!-- b004106 | prose | pages [12] -->
m

<!-- b004107 | prose | pages [12] -->
m

<!-- b004108 | prose | pages [12] -->
m

<!-- b004109 | prose | pages [12] -->
m

<!-- b004110 | prose | pages [12] -->
m

<!-- b004111 | prose | pages [12] -->
m

<!-- b004112 | prose | pages [12] -->
m

<!-- b004113 | prose | pages [12] -->
m

<!-- b004114 | prose | pages [12] -->
m

<!-- b004115 | prose | pages [12] -->
m

<!-- b004116 | prose | pages [12] -->
m

<!-- b004117 | prose | pages [12] -->
m

<!-- b004118 | prose | pages [12] -->
m

<!-- b004119 | prose | pages [12] -->
m

<!-- b004120 | prose | pages [12] -->
m

<!-- b004121 | prose | pages [12] -->
m

<!-- b004122 | prose | pages [12] -->
m

<!-- b004123 | prose | pages [12] -->
m

<!-- b004124 | prose | pages [12] -->
m

<!-- b004125 | prose | pages [12] -->
m

<!-- b004126 | prose | pages [12] -->
m

<!-- b004127 | prose | pages [12] -->
m

<!-- b004128 | prose | pages [12] -->
m

<!-- b004129 | prose | pages [12] -->
m

<!-- b004130 | prose | pages [12] -->
m

<!-- b004131 | prose | pages [12] -->
m

<!-- b004132 | prose | pages [12] -->
m

<!-- b004133 | prose | pages [12] -->
m

<!-- b004134 | prose | pages [12] -->
m

<!-- b004135 | prose | pages [12] -->
m

<!-- b004136 | prose | pages [12] -->
m

<!-- b004137 | prose | pages [12] -->
m

<!-- b004138 | prose | pages [12] -->
m

<!-- b004139 | prose | pages [12] -->
m

<!-- b004140 | prose | pages [12] -->
m

<!-- b004141 | prose | pages [12] -->
m

<!-- b004142 | prose | pages [12] -->
m

<!-- b004143 | prose | pages [12] -->
m

<!-- b004144 | prose | pages [12] -->
m

<!-- b004145 | prose | pages [12] -->
m

<!-- b004146 | prose | pages [12] -->
m

<!-- b004147 | prose | pages [12] -->
m

<!-- b004148 | prose | pages [12] -->
m

<!-- b004149 | prose | pages [12] -->
m

<!-- b004150 | prose | pages [12] -->
m

<!-- b004151 | prose | pages [12] -->
m

<!-- b004152 | prose | pages [12] -->
m

<!-- b004153 | prose | pages [12] -->
m

<!-- b004154 | prose | pages [12] -->
m

<!-- b004155 | prose | pages [12] -->
m

<!-- b004156 | prose | pages [12] -->
m

<!-- b004157 | prose | pages [12] -->
m

<!-- b004158 | prose | pages [12] -->
m

<!-- b004159 | prose | pages [12] -->
m

<!-- b004160 | prose | pages [12] -->
m

<!-- b004161 | prose | pages [12] -->
m

<!-- b004162 | prose | pages [12] -->
m

<!-- b004163 | prose | pages [12] -->
m

<!-- b004164 | prose | pages [12] -->
m

<!-- b004165 | prose | pages [12] -->
m

<!-- b004166 | prose | pages [12] -->
m

<!-- b004167 | prose | pages [12] -->
m

<!-- b004168 | prose | pages [12] -->
m

<!-- b004169 | prose | pages [12] -->
m

<!-- b004170 | prose | pages [12] -->
m

<!-- b004171 | prose | pages [12] -->
m

<!-- b004172 | prose | pages [12] -->
m

<!-- b004173 | prose | pages [12] -->
m

<!-- b004174 | prose | pages [12] -->
m

<!-- b004175 | prose | pages [12] -->
m

<!-- b004176 | prose | pages [12] -->
m

<!-- b004177 | prose | pages [12] -->
m

<!-- b004178 | prose | pages [12] -->
m

<!-- b004179 | prose | pages [12] -->
m

<!-- b004180 | prose | pages [12] -->
m

<!-- b004181 | prose | pages [12] -->
m

<!-- b004182 | prose | pages [12] -->
m

<!-- b004183 | prose | pages [12] -->
m

<!-- b004184 | prose | pages [12] -->
m

<!-- b004185 | prose | pages [12] -->
m

<!-- b004186 | prose | pages [12] -->
m

<!-- b004187 | prose | pages [12] -->
m

<!-- b004188 | prose | pages [12] -->
m

<!-- b004189 | prose | pages [12] -->
m

<!-- b004190 | prose | pages [12] -->
m

<!-- b004191 | prose | pages [12] -->
m

<!-- b004192 | prose | pages [12] -->
m

<!-- b004193 | prose | pages [12] -->
m

<!-- b004194 | prose | pages [12] -->
m

<!-- b004195 | prose | pages [12] -->
m

<!-- b004196 | prose | pages [12] -->
m

<!-- b004197 | prose | pages [12] -->
m

<!-- b004198 | prose | pages [12] -->
m

<!-- b004199 | prose | pages [12] -->
m

<!-- b004200 | prose | pages [12] -->
m

<!-- b004201 | prose | pages [12] -->
m

<!-- b004202 | prose | pages [12] -->
m

<!-- b004203 | prose | pages [12] -->
m

<!-- b004204 | prose | pages [12] -->
m

<!-- b004205 | prose | pages [12] -->
m

<!-- b004206 | prose | pages [12] -->
m

<!-- b004207 | prose | pages [12] -->
m

<!-- b004208 | prose | pages [12] -->
m

<!-- b004209 | prose | pages [12] -->
m

<!-- b004210 | prose | pages [12] -->
m

<!-- b004211 | prose | pages [12] -->
m

<!-- b004212 | prose | pages [12] -->
m

<!-- b004213 | prose | pages [12] -->
m

<!-- b004214 | prose | pages [12] -->
m

<!-- b004215 | prose | pages [12] -->
m

<!-- b004216 | prose | pages [12] -->
m

<!-- b004217 | prose | pages [12] -->
m

<!-- b004218 | prose | pages [12] -->
m

<!-- b004219 | prose | pages [12] -->
m

<!-- b004220 | prose | pages [12] -->
m

<!-- b004221 | prose | pages [12] -->
m

<!-- b004222 | prose | pages [12] -->
m

<!-- b004223 | prose | pages [12] -->
m

<!-- b004224 | prose | pages [12] -->
m

<!-- b004225 | prose | pages [12] -->
m

<!-- b004226 | prose | pages [12] -->
m

<!-- b004227 | prose | pages [12] -->
m

<!-- b004228 | prose | pages [12] -->
m

<!-- b004229 | prose | pages [12] -->
m

<!-- b004230 | prose | pages [12] -->
m

<!-- b004231 | prose | pages [12] -->
m

<!-- b004232 | prose | pages [12] -->
m

<!-- b004233 | prose | pages [12] -->
m

<!-- b004234 | prose | pages [12] -->
m

<!-- b004235 | prose | pages [12] -->
m

<!-- b004236 | prose | pages [12] -->
m

<!-- b004237 | prose | pages [12] -->
m

<!-- b004238 | prose | pages [12] -->
m

<!-- b004239 | prose | pages [12] -->
m

<!-- b004240 | prose | pages [12] -->
m

<!-- b004241 | prose | pages [12] -->
m

<!-- b004242 | prose | pages [12] -->
m

<!-- b004243 | prose | pages [12] -->
m

<!-- b004244 | prose | pages [12] -->
m

<!-- b004245 | prose | pages [12] -->
m

<!-- b004246 | prose | pages [12] -->
m

<!-- b004247 | prose | pages [12] -->
m

<!-- b004248 | prose | pages [12] -->
m

<!-- b004249 | prose | pages [12] -->
m

<!-- b004250 | prose | pages [12] -->
m

<!-- b004251 | prose | pages [12] -->
m

<!-- b004252 | prose | pages [12] -->
m

<!-- b004253 | prose | pages [12] -->
m

<!-- b004254 | prose | pages [12] -->
m

<!-- b004255 | prose | pages [12] -->
m

<!-- b004256 | prose | pages [12] -->
m

<!-- b004257 | prose | pages [12] -->
m

<!-- b004258 | prose | pages [12] -->
m

<!-- b004259 | prose | pages [12] -->
m

<!-- b004260 | prose | pages [12] -->
m

<!-- b004261 | prose | pages [12] -->
m

<!-- b004262 | prose | pages [12] -->
m

<!-- b004263 | prose | pages [12] -->
m

<!-- b004264 | prose | pages [12] -->
m

<!-- b004265 | prose | pages [12] -->
m

<!-- b004266 | prose | pages [12] -->
m

<!-- b004267 | prose | pages [12] -->
m

<!-- b004268 | prose | pages [12] -->
m

<!-- b004269 | prose | pages [12] -->
m

<!-- b004270 | prose | pages [12] -->
m

<!-- b004271 | prose | pages [12] -->
m

<!-- b004272 | prose | pages [12] -->
m

<!-- b004273 | prose | pages [12] -->
m

<!-- b004274 | prose | pages [12] -->
m

<!-- b004275 | prose | pages [12] -->
m

<!-- b004276 | prose | pages [12] -->
m

<!-- b004277 | prose | pages [12] -->
m

<!-- b004278 | prose | pages [12] -->
m

<!-- b004279 | prose | pages [12] -->
m

<!-- b004280 | prose | pages [12] -->
m

<!-- b004281 | prose | pages [12] -->
m

<!-- b004282 | prose | pages [12] -->
m

<!-- b004283 | prose | pages [12] -->
m

<!-- b004284 | prose | pages [12] -->
m

<!-- b004285 | prose | pages [12] -->
m

<!-- b004286 | prose | pages [12] -->
m

<!-- b004287 | prose | pages [12] -->
m

<!-- b004288 | prose | pages [12] -->
m

<!-- b004289 | prose | pages [12] -->
m

<!-- b004290 | prose | pages [12] -->
m

<!-- b004291 | prose | pages [12] -->
m

<!-- b004292 | prose | pages [12] -->
m

<!-- b004293 | prose | pages [12] -->
m

<!-- b004294 | prose | pages [12] -->
m

<!-- b004295 | prose | pages [12] -->
m

<!-- b004296 | prose | pages [12] -->
m

<!-- b004297 | prose | pages [12] -->
m

<!-- b004298 | prose | pages [12] -->
m

<!-- b004299 | prose | pages [12] -->
m

<!-- b004300 | prose | pages [12] -->
m

<!-- b004301 | prose | pages [12] -->
m

<!-- b004302 | prose | pages [12] -->
m

<!-- b004303 | prose | pages [12] -->
m

<!-- b004304 | prose | pages [12] -->
m

<!-- b004305 | prose | pages [12] -->
m

<!-- b004306 | prose | pages [12] -->
m

<!-- b004307 | prose | pages [12] -->
m

<!-- b004308 | prose | pages [12] -->
m

<!-- b004309 | prose | pages [12] -->
m

<!-- b004310 | prose | pages [12] -->
m

<!-- b004311 | prose | pages [12] -->
m

<!-- b004312 | prose | pages [12] -->
m

<!-- b004313 | prose | pages [12] -->
m

<!-- b004314 | prose | pages [12] -->
m

<!-- b004315 | prose | pages [12] -->
m

<!-- b004316 | prose | pages [12] -->
m

<!-- b004317 | prose | pages [12] -->
m

<!-- b004318 | prose | pages [12] -->
m

<!-- b004319 | prose | pages [12] -->
m

<!-- b004320 | prose | pages [12] -->
m

<!-- b004321 | prose | pages [12] -->
m

<!-- b004322 | prose | pages [12] -->
m

<!-- b004323 | prose | pages [12] -->
m

<!-- b004324 | prose | pages [12] -->
m

<!-- b004325 | prose | pages [12] -->
m

<!-- b004326 | prose | pages [12] -->
m

<!-- b004327 | prose | pages [12] -->
m

<!-- b004328 | prose | pages [12] -->
m

<!-- b004329 | prose | pages [12] -->
m

<!-- b004330 | prose | pages [12] -->
m

<!-- b004331 | prose | pages [12] -->
m

<!-- b004332 | prose | pages [12] -->
m

<!-- b004333 | prose | pages [12] -->
m

<!-- b004334 | prose | pages [12] -->
m

<!-- b004335 | prose | pages [12] -->
m

<!-- b004336 | prose | pages [12] -->
m

<!-- b004337 | prose | pages [12] -->
m

<!-- b004338 | prose | pages [12] -->
m

<!-- b004339 | prose | pages [12] -->
m

<!-- b004340 | prose | pages [12] -->
m

<!-- b004341 | prose | pages [12] -->
m

<!-- b004342 | prose | pages [12] -->
m

<!-- b004343 | prose | pages [12] -->
m

<!-- b004344 | prose | pages [12] -->
m

<!-- b004345 | prose | pages [12] -->
m

<!-- b004346 | prose | pages [12] -->
m

<!-- b004347 | prose | pages [12] -->
m

<!-- b004348 | prose | pages [12] -->
m

<!-- b004349 | prose | pages [12] -->
m

<!-- b004350 | prose | pages [12] -->
m

<!-- b004351 | prose | pages [12] -->
m

<!-- b004352 | prose | pages [12] -->
m

<!-- b004353 | prose | pages [12] -->
m

<!-- b004354 | prose | pages [12] -->
m

<!-- b004355 | prose | pages [12] -->
m

<!-- b004356 | prose | pages [12] -->
m

<!-- b004357 | prose | pages [12] -->
m

<!-- b004358 | prose | pages [12] -->
m

<!-- b004359 | prose | pages [12] -->
m

<!-- b004360 | prose | pages [12] -->
m

<!-- b004361 | prose | pages [12] -->
m

<!-- b004362 | prose | pages [12] -->
m

<!-- b004363 | prose | pages [12] -->
m

<!-- b004364 | prose | pages [12] -->
m

<!-- b004365 | prose | pages [12] -->
m

<!-- b004366 | prose | pages [12] -->
m

<!-- b004367 | prose | pages [12] -->
m

<!-- b004368 | prose | pages [12] -->
m

<!-- b004369 | prose | pages [12] -->
m

<!-- b004370 | prose | pages [12] -->
m

<!-- b004371 | prose | pages [12] -->
m

<!-- b004372 | prose | pages [12] -->
m

<!-- b004373 | prose | pages [12] -->
m

<!-- b004374 | prose | pages [12] -->
m

<!-- b004375 | prose | pages [12] -->
m

<!-- b004376 | prose | pages [12] -->
m

<!-- b004377 | prose | pages [12] -->
m

<!-- b004378 | prose | pages [12] -->
m

<!-- b004379 | prose | pages [12] -->
m

<!-- b004380 | prose | pages [12] -->
m

<!-- b004381 | prose | pages [12] -->
m

<!-- b004382 | prose | pages [12] -->
m

<!-- b004383 | prose | pages [12] -->
m

<!-- b004384 | prose | pages [12] -->
m

<!-- b004385 | caption | pages [12] -->
Figure 7: Countries that have never won a medal

<!-- b004386 | prose | pages [12] -->
With the continued efforts of the IOC and various national sports organisations, par- ticipation in Olympic sports in these countries is increasing year on year. As the Olympic Games become more popular around the world and resources are distributed more eq- uitably, it is still possible that in the future there will be a few ’dark horse’ countries that could win medals for the first time at future Olympic Games.

<!-- b004387 | prose | pages [12] -->
In order to predict which non-medal-winning countries are likely to make a break-

<!-- b004388 | prose | pages [12] -->
关注数学模型

<!-- b004389 | furniture | pages [12] -->
2

<!-- b004390 | furniture | pages [12] -->
MATHmodels

<!-- b004391 | furniture | pages [12] -->
获取更多资讯

<!-- b004392 | furniture | pages [13] -->
Team # 2510862

<!-- b004393 | furniture | pages [13] -->
Page 13 of 25

<!-- b004394 | prose | pages [13] -->
through at the upcoming 2028 Olympic Games in Los Angeles, we have conducted a multi-dimensional analysis of these countries, using data modelling methods to extract key characteristics to more accurately assess their potential for a first medal.

<!-- b004395 | heading | pages [13] -->
1. Impact of changes in the number of participants

<!-- b004396 | prose | pages [13] -->
Firstly, we analysed the changes in the number of participants of the non-winning countries over the period 1960-2024. By looking at the trends in their participation num- bers over the past few Olympics, we are able to surmise their commitment and involve- ment in the Olympic Games. If a country’s participation numbers are increasing year on year, this tends to imply that the country is increasing its investment in the Olympic Movement, increasing the support it provides to its athletes, and in turn increasing its

<!-- b004397 | prose | pages [13] -->
微信公众号：数学模型

<!-- b004398 | prose | pages [13] -->
potential to win medals.

<!-- b004399 | prose | pages [13] -->
微信号：MATHmodels

<!-- b004400 | caption | pages [13] -->
Figure 8: Participant Trends for Non-Medal-Winning Countries (Top 28)

<!-- b004401 | prose | pages [13] -->
In an effort to quantify the changes in these countries’ inputs, we fitted a trend line to the change in the number of participants for each country. If the slope of the trend line is positive (The red fitted line in Figure 7) indicates an increase in participation, we labelled these countries as ’1’, indicating that their inputs are increasing, and ’0’, vice versa. This characteristic reflects whether countries have the potential to win medals at future Olympic Games.

<!-- b004402 | heading | pages [13] -->
2. Projects more likely to be first-time winners

<!-- b004403 | prose | pages [13] -->
In addition to changes in the number of entries, another key factor is which projects are more likely to be ‘breakthroughs’ for first-time winners. By analysing the countries that have won first-time prizes in the period 2000-2024, as shown in Figures.

<!-- b004404 | prose | pages [13] -->
m

<!-- b004405 | prose | pages [13] -->
m

<!-- b004406 | prose | pages [13] -->
m

<!-- b004407 | prose | pages [13] -->
m

<!-- b004408 | prose | pages [13] -->
m

<!-- b004409 | prose | pages [13] -->
m

<!-- b004410 | prose | pages [13] -->
m

<!-- b004411 | prose | pages [13] -->
m

<!-- b004412 | prose | pages [13] -->
m

<!-- b004413 | prose | pages [13] -->
m

<!-- b004414 | prose | pages [13] -->
m

<!-- b004415 | prose | pages [13] -->
m

<!-- b004416 | prose | pages [13] -->
m

<!-- b004417 | prose | pages [13] -->
m

<!-- b004418 | prose | pages [13] -->
m

<!-- b004419 | prose | pages [13] -->
m

<!-- b004420 | prose | pages [13] -->
m

<!-- b004421 | prose | pages [13] -->
m

<!-- b004422 | prose | pages [13] -->
m

<!-- b004423 | prose | pages [13] -->
m

<!-- b004424 | prose | pages [13] -->
m

<!-- b004425 | prose | pages [13] -->
m

<!-- b004426 | prose | pages [13] -->
m

<!-- b004427 | prose | pages [13] -->
m

<!-- b004428 | prose | pages [13] -->
m

<!-- b004429 | prose | pages [13] -->
m

<!-- b004430 | prose | pages [13] -->
m

<!-- b004431 | prose | pages [13] -->
m

<!-- b004432 | prose | pages [13] -->
m

<!-- b004433 | prose | pages [13] -->
m

<!-- b004434 | prose | pages [13] -->
m

<!-- b004435 | prose | pages [13] -->
m

<!-- b004436 | prose | pages [13] -->
m

<!-- b004437 | prose | pages [13] -->
m

<!-- b004438 | prose | pages [13] -->
m

<!-- b004439 | prose | pages [13] -->
m

<!-- b004440 | prose | pages [13] -->
m

<!-- b004441 | prose | pages [13] -->
m

<!-- b004442 | prose | pages [13] -->
m

<!-- b004443 | prose | pages [13] -->
m

<!-- b004444 | prose | pages [13] -->
m

<!-- b004445 | prose | pages [13] -->
m

<!-- b004446 | prose | pages [13] -->
m

<!-- b004447 | prose | pages [13] -->
m

<!-- b004448 | prose | pages [13] -->
m

<!-- b004449 | prose | pages [13] -->
m

<!-- b004450 | prose | pages [13] -->
m

<!-- b004451 | prose | pages [13] -->
m

<!-- b004452 | prose | pages [13] -->
m

<!-- b004453 | prose | pages [13] -->
m

<!-- b004454 | prose | pages [13] -->
m

<!-- b004455 | prose | pages [13] -->
m

<!-- b004456 | prose | pages [13] -->
m

<!-- b004457 | prose | pages [13] -->
m

<!-- b004458 | prose | pages [13] -->
m

<!-- b004459 | prose | pages [13] -->
m

<!-- b004460 | prose | pages [13] -->
m

<!-- b004461 | prose | pages [13] -->
m

<!-- b004462 | prose | pages [13] -->
m

<!-- b004463 | prose | pages [13] -->
m

<!-- b004464 | prose | pages [13] -->
m

<!-- b004465 | prose | pages [13] -->
m

<!-- b004466 | prose | pages [13] -->
m

<!-- b004467 | prose | pages [13] -->
m

<!-- b004468 | prose | pages [13] -->
m

<!-- b004469 | prose | pages [13] -->
m

<!-- b004470 | prose | pages [13] -->
m

<!-- b004471 | prose | pages [13] -->
m

<!-- b004472 | prose | pages [13] -->
m

<!-- b004473 | prose | pages [13] -->
m

<!-- b004474 | prose | pages [13] -->
m

<!-- b004475 | prose | pages [13] -->
m

<!-- b004476 | prose | pages [13] -->
m

<!-- b004477 | prose | pages [13] -->
m

<!-- b004478 | prose | pages [13] -->
m

<!-- b004479 | prose | pages [13] -->
m

<!-- b004480 | prose | pages [13] -->
m

<!-- b004481 | prose | pages [13] -->
m

<!-- b004482 | prose | pages [13] -->
m

<!-- b004483 | prose | pages [13] -->
m

<!-- b004484 | prose | pages [13] -->
m

<!-- b004485 | prose | pages [13] -->
m

<!-- b004486 | prose | pages [13] -->
m

<!-- b004487 | prose | pages [13] -->
m

<!-- b004488 | prose | pages [13] -->
m

<!-- b004489 | prose | pages [13] -->
m

<!-- b004490 | prose | pages [13] -->
m

<!-- b004491 | prose | pages [13] -->
m

<!-- b004492 | prose | pages [13] -->
m

<!-- b004493 | prose | pages [13] -->
m

<!-- b004494 | prose | pages [13] -->
m

<!-- b004495 | prose | pages [13] -->
m

<!-- b004496 | prose | pages [13] -->
m

<!-- b004497 | prose | pages [13] -->
m

<!-- b004498 | prose | pages [13] -->
m

<!-- b004499 | prose | pages [13] -->
m

<!-- b004500 | prose | pages [13] -->
m

<!-- b004501 | prose | pages [13] -->
m

<!-- b004502 | prose | pages [13] -->
m

<!-- b004503 | prose | pages [13] -->
m

<!-- b004504 | prose | pages [13] -->
m

<!-- b004505 | prose | pages [13] -->
m

<!-- b004506 | prose | pages [13] -->
m

<!-- b004507 | prose | pages [13] -->
m

<!-- b004508 | prose | pages [13] -->
m

<!-- b004509 | prose | pages [13] -->
m

<!-- b004510 | prose | pages [13] -->
m

<!-- b004511 | prose | pages [13] -->
m

<!-- b004512 | prose | pages [13] -->
m

<!-- b004513 | prose | pages [13] -->
m

<!-- b004514 | prose | pages [13] -->
m

<!-- b004515 | prose | pages [13] -->
m

<!-- b004516 | prose | pages [13] -->
m

<!-- b004517 | prose | pages [13] -->
m

<!-- b004518 | prose | pages [13] -->
m

<!-- b004519 | prose | pages [13] -->
m

<!-- b004520 | prose | pages [13] -->
m

<!-- b004521 | prose | pages [13] -->
m

<!-- b004522 | prose | pages [13] -->
m

<!-- b004523 | prose | pages [13] -->
m

<!-- b004524 | prose | pages [13] -->
m

<!-- b004525 | prose | pages [13] -->
m

<!-- b004526 | prose | pages [13] -->
m

<!-- b004527 | prose | pages [13] -->
m

<!-- b004528 | prose | pages [13] -->
m

<!-- b004529 | prose | pages [13] -->
m

<!-- b004530 | prose | pages [13] -->
m

<!-- b004531 | prose | pages [13] -->
m

<!-- b004532 | prose | pages [13] -->
m

<!-- b004533 | prose | pages [13] -->
m

<!-- b004534 | prose | pages [13] -->
m

<!-- b004535 | prose | pages [13] -->
m

<!-- b004536 | prose | pages [13] -->
m

<!-- b004537 | prose | pages [13] -->
m

<!-- b004538 | prose | pages [13] -->
m

<!-- b004539 | prose | pages [13] -->
m

<!-- b004540 | prose | pages [13] -->
m

<!-- b004541 | prose | pages [13] -->
m

<!-- b004542 | prose | pages [13] -->
m

<!-- b004543 | prose | pages [13] -->
m

<!-- b004544 | prose | pages [13] -->
m

<!-- b004545 | prose | pages [13] -->
m

<!-- b004546 | prose | pages [13] -->
m

<!-- b004547 | prose | pages [13] -->
m

<!-- b004548 | prose | pages [13] -->
m

<!-- b004549 | prose | pages [13] -->
m

<!-- b004550 | prose | pages [13] -->
m

<!-- b004551 | prose | pages [13] -->
m

<!-- b004552 | prose | pages [13] -->
m

<!-- b004553 | prose | pages [13] -->
m

<!-- b004554 | prose | pages [13] -->
m

<!-- b004555 | prose | pages [13] -->
m

<!-- b004556 | prose | pages [13] -->
m

<!-- b004557 | prose | pages [13] -->
m

<!-- b004558 | prose | pages [13] -->
m

<!-- b004559 | prose | pages [13] -->
m

<!-- b004560 | prose | pages [13] -->
m

<!-- b004561 | prose | pages [13] -->
m

<!-- b004562 | prose | pages [13] -->
m

<!-- b004563 | prose | pages [13] -->
m

<!-- b004564 | prose | pages [13] -->
m

<!-- b004565 | prose | pages [13] -->
m

<!-- b004566 | prose | pages [13] -->
m

<!-- b004567 | prose | pages [13] -->
m

<!-- b004568 | prose | pages [13] -->
m

<!-- b004569 | prose | pages [13] -->
m

<!-- b004570 | prose | pages [13] -->
m

<!-- b004571 | prose | pages [13] -->
m

<!-- b004572 | prose | pages [13] -->
m

<!-- b004573 | prose | pages [13] -->
m

<!-- b004574 | prose | pages [13] -->
m

<!-- b004575 | prose | pages [13] -->
m

<!-- b004576 | prose | pages [13] -->
m

<!-- b004577 | prose | pages [13] -->
m

<!-- b004578 | prose | pages [13] -->
m

<!-- b004579 | prose | pages [13] -->
m

<!-- b004580 | prose | pages [13] -->
m

<!-- b004581 | prose | pages [13] -->
m

<!-- b004582 | prose | pages [13] -->
m

<!-- b004583 | prose | pages [13] -->
m

<!-- b004584 | prose | pages [13] -->
m

<!-- b004585 | prose | pages [13] -->
m

<!-- b004586 | prose | pages [13] -->
m

<!-- b004587 | prose | pages [13] -->
m

<!-- b004588 | prose | pages [13] -->
m

<!-- b004589 | prose | pages [13] -->
m

<!-- b004590 | prose | pages [13] -->
m

<!-- b004591 | prose | pages [13] -->
m

<!-- b004592 | prose | pages [13] -->
m

<!-- b004593 | prose | pages [13] -->
m

<!-- b004594 | prose | pages [13] -->
m

<!-- b004595 | prose | pages [13] -->
m

<!-- b004596 | prose | pages [13] -->
m

<!-- b004597 | prose | pages [13] -->
m

<!-- b004598 | prose | pages [13] -->
m

<!-- b004599 | prose | pages [13] -->
m

<!-- b004600 | prose | pages [13] -->
m

<!-- b004601 | prose | pages [13] -->
m

<!-- b004602 | prose | pages [13] -->
m

<!-- b004603 | prose | pages [13] -->
m

<!-- b004604 | prose | pages [13] -->
m

<!-- b004605 | prose | pages [13] -->
m

<!-- b004606 | prose | pages [13] -->
m

<!-- b004607 | prose | pages [13] -->
m

<!-- b004608 | prose | pages [13] -->
m

<!-- b004609 | prose | pages [13] -->
m

<!-- b004610 | prose | pages [13] -->
m

<!-- b004611 | prose | pages [13] -->
m

<!-- b004612 | prose | pages [13] -->
m

<!-- b004613 | prose | pages [13] -->
m

<!-- b004614 | prose | pages [13] -->
m

<!-- b004615 | prose | pages [13] -->
m

<!-- b004616 | prose | pages [13] -->
m

<!-- b004617 | prose | pages [13] -->
m

<!-- b004618 | prose | pages [13] -->
m

<!-- b004619 | prose | pages [13] -->
m

<!-- b004620 | prose | pages [13] -->
m

<!-- b004621 | prose | pages [13] -->
m

<!-- b004622 | prose | pages [13] -->
m

<!-- b004623 | prose | pages [13] -->
m

<!-- b004624 | prose | pages [13] -->
m

<!-- b004625 | prose | pages [13] -->
m

<!-- b004626 | prose | pages [13] -->
m

<!-- b004627 | prose | pages [13] -->
m

<!-- b004628 | prose | pages [13] -->
m

<!-- b004629 | prose | pages [13] -->
m

<!-- b004630 | prose | pages [13] -->
m

<!-- b004631 | prose | pages [13] -->
m

<!-- b004632 | prose | pages [13] -->
m

<!-- b004633 | prose | pages [13] -->
m

<!-- b004634 | prose | pages [13] -->
m

<!-- b004635 | prose | pages [13] -->
m

<!-- b004636 | prose | pages [13] -->
m

<!-- b004637 | prose | pages [13] -->
m

<!-- b004638 | prose | pages [13] -->
m

<!-- b004639 | prose | pages [13] -->
m

<!-- b004640 | prose | pages [13] -->
m

<!-- b004641 | prose | pages [13] -->
m

<!-- b004642 | prose | pages [13] -->
m

<!-- b004643 | prose | pages [13] -->
m

<!-- b004644 | prose | pages [13] -->
m

<!-- b004645 | prose | pages [13] -->
m

<!-- b004646 | prose | pages [13] -->
m

<!-- b004647 | prose | pages [13] -->
m

<!-- b004648 | prose | pages [13] -->
m

<!-- b004649 | prose | pages [13] -->
m

<!-- b004650 | prose | pages [13] -->
m

<!-- b004651 | prose | pages [13] -->
m

<!-- b004652 | prose | pages [13] -->
m

<!-- b004653 | prose | pages [13] -->
m

<!-- b004654 | prose | pages [13] -->
m

<!-- b004655 | prose | pages [13] -->
m

<!-- b004656 | prose | pages [13] -->
m

<!-- b004657 | prose | pages [13] -->
m

<!-- b004658 | prose | pages [13] -->
m

<!-- b004659 | prose | pages [13] -->
m

<!-- b004660 | prose | pages [13] -->
m

<!-- b004661 | prose | pages [13] -->
m

<!-- b004662 | prose | pages [13] -->
m

<!-- b004663 | prose | pages [13] -->
m

<!-- b004664 | prose | pages [13] -->
m

<!-- b004665 | prose | pages [13] -->
m

<!-- b004666 | prose | pages [13] -->
m

<!-- b004667 | prose | pages [13] -->
m

<!-- b004668 | prose | pages [13] -->
m

<!-- b004669 | prose | pages [13] -->
m

<!-- b004670 | prose | pages [13] -->
m

<!-- b004671 | prose | pages [13] -->
m

<!-- b004672 | prose | pages [13] -->
m

<!-- b004673 | prose | pages [13] -->
m

<!-- b004674 | prose | pages [13] -->
m

<!-- b004675 | prose | pages [13] -->
m

<!-- b004676 | prose | pages [13] -->
m

<!-- b004677 | prose | pages [13] -->
m

<!-- b004678 | prose | pages [13] -->
m

<!-- b004679 | prose | pages [13] -->
m

<!-- b004680 | prose | pages [13] -->
m

<!-- b004681 | prose | pages [13] -->
m

<!-- b004682 | prose | pages [13] -->
m

<!-- b004683 | prose | pages [13] -->
m

<!-- b004684 | prose | pages [13] -->
m

<!-- b004685 | prose | pages [13] -->
m

<!-- b004686 | prose | pages [13] -->
m

<!-- b004687 | prose | pages [13] -->
m

<!-- b004688 | furniture | pages [13] -->
m

<!-- b004689 | furniture | pages [13] -->
m

<!-- b004690 | furniture | pages [13] -->
m

<!-- b004691 | furniture | pages [13] -->
m

<!-- b004692 | furniture | pages [13] -->
m

<!-- b004693 | furniture | pages [13] -->
m

<!-- b004694 | furniture | pages [13] -->
m

<!-- b004695 | furniture | pages [13] -->
m

<!-- b004696 | furniture | pages [13] -->
m

<!-- b004697 | furniture | pages [13] -->
m

<!-- b004698 | furniture | pages [13] -->
m

<!-- b004699 | furniture | pages [13] -->
m

<!-- b004700 | furniture | pages [13] -->
m

<!-- b004701 | furniture | pages [13] -->
m

<!-- b004702 | furniture | pages [13] -->
m

<!-- b004703 | furniture | pages [13] -->
m

<!-- b004704 | furniture | pages [13] -->
m

<!-- b004705 | furniture | pages [13] -->
m

<!-- b004706 | furniture | pages [13] -->
m

<!-- b004707 | furniture | pages [13] -->
m

<!-- b004708 | furniture | pages [13] -->
m

<!-- b004709 | furniture | pages [13] -->
m

<!-- b004710 | furniture | pages [13] -->
m

<!-- b004711 | furniture | pages [13] -->
m

<!-- b004712 | furniture | pages [13] -->
m

<!-- b004713 | furniture | pages [13] -->
m

<!-- b004714 | furniture | pages [13] -->
m

<!-- b004715 | furniture | pages [13] -->
m

<!-- b004716 | furniture | pages [13] -->
m

<!-- b004717 | furniture | pages [13] -->
m

<!-- b004718 | furniture | pages [13] -->
m

<!-- b004719 | furniture | pages [13] -->
m

<!-- b004720 | furniture | pages [13] -->
m

<!-- b004721 | furniture | pages [13] -->
m

<!-- b004722 | furniture | pages [13] -->
m

<!-- b004723 | furniture | pages [13] -->
m

<!-- b004724 | furniture | pages [13] -->
m

<!-- b004725 | furniture | pages [13] -->
m

<!-- b004726 | furniture | pages [13] -->
m

<!-- b004727 | furniture | pages [13] -->
m

<!-- b004728 | furniture | pages [13] -->
m

<!-- b004729 | furniture | pages [13] -->
m

<!-- b004730 | furniture | pages [13] -->
m

<!-- b004731 | furniture | pages [13] -->
m

<!-- b004732 | furniture | pages [13] -->
m

<!-- b004733 | furniture | pages [13] -->
m

<!-- b004734 | furniture | pages [13] -->
m

<!-- b004735 | furniture | pages [13] -->
m

<!-- b004736 | furniture | pages [13] -->
m

<!-- b004737 | furniture | pages [13] -->
m

<!-- b004738 | furniture | pages [13] -->
m

<!-- b004739 | furniture | pages [13] -->
m

<!-- b004740 | furniture | pages [13] -->
m

<!-- b004741 | furniture | pages [13] -->
m

<!-- b004742 | furniture | pages [13] -->
m

<!-- b004743 | furniture | pages [13] -->
m

<!-- b004744 | furniture | pages [13] -->
m

<!-- b004745 | furniture | pages [13] -->
m

<!-- b004746 | furniture | pages [13] -->
m

<!-- b004747 | furniture | pages [13] -->
m

<!-- b004748 | furniture | pages [13] -->
m

<!-- b004749 | furniture | pages [13] -->
m

<!-- b004750 | furniture | pages [13] -->
m

<!-- b004751 | furniture | pages [13] -->
m

<!-- b004752 | furniture | pages [13] -->
m

<!-- b004753 | furniture | pages [13] -->
m

<!-- b004754 | furniture | pages [13] -->
m

<!-- b004755 | furniture | pages [13] -->
m

<!-- b004756 | furniture | pages [13] -->
m

<!-- b004757 | furniture | pages [13] -->
m

<!-- b004758 | furniture | pages [13] -->
m

<!-- b004759 | furniture | pages [13] -->
m

<!-- b004760 | furniture | pages [13] -->
m

<!-- b004761 | furniture | pages [13] -->
m

<!-- b004762 | furniture | pages [13] -->
m

<!-- b004763 | furniture | pages [13] -->
m

<!-- b004764 | furniture | pages [13] -->
m

<!-- b004765 | furniture | pages [13] -->
m

<!-- b004766 | furniture | pages [13] -->
m

<!-- b004767 | furniture | pages [13] -->
m

<!-- b004768 | furniture | pages [13] -->
m

<!-- b004769 | furniture | pages [13] -->
m

<!-- b004770 | furniture | pages [13] -->
m

<!-- b004771 | furniture | pages [13] -->
m

<!-- b004772 | furniture | pages [13] -->
m

<!-- b004773 | furniture | pages [13] -->
m

<!-- b004774 | furniture | pages [13] -->
m

<!-- b004775 | furniture | pages [13] -->
m

<!-- b004776 | furniture | pages [13] -->
m

<!-- b004777 | furniture | pages [13] -->
m

<!-- b004778 | furniture | pages [13] -->
m

<!-- b004779 | furniture | pages [13] -->
m

<!-- b004780 | furniture | pages [13] -->
m

<!-- b004781 | furniture | pages [13] -->
m

<!-- b004782 | furniture | pages [13] -->
m

<!-- b004783 | furniture | pages [13] -->
m

<!-- b004784 | furniture | pages [13] -->
m

<!-- b004785 | furniture | pages [13] -->
m

<!-- b004786 | furniture | pages [13] -->
m

<!-- b004787 | furniture | pages [13] -->
m

<!-- b004788 | furniture | pages [13] -->
m

<!-- b004789 | furniture | pages [13] -->
m

<!-- b004790 | furniture | pages [13] -->
m

<!-- b004791 | furniture | pages [13] -->
m

<!-- b004792 | furniture | pages [13] -->
m

<!-- b004793 | furniture | pages [13] -->
m

<!-- b004794 | furniture | pages [13] -->
m

<!-- b004795 | furniture | pages [13] -->
m

<!-- b004796 | furniture | pages [13] -->
m

<!-- b004797 | furniture | pages [13] -->
m

<!-- b004798 | furniture | pages [13] -->
m

<!-- b004799 | furniture | pages [13] -->
m

<!-- b004800 | furniture | pages [13] -->
m

<!-- b004801 | furniture | pages [13] -->
m

<!-- b004802 | furniture | pages [13] -->
m

<!-- b004803 | furniture | pages [13] -->
m

<!-- b004804 | furniture | pages [13] -->
m

<!-- b004805 | furniture | pages [13] -->
m

<!-- b004806 | furniture | pages [13] -->
m

<!-- b004807 | furniture | pages [13] -->
m

<!-- b004808 | furniture | pages [13] -->
m

<!-- b004809 | furniture | pages [13] -->
m

<!-- b004810 | furniture | pages [13] -->
m

<!-- b004811 | furniture | pages [13] -->
m

<!-- b004812 | furniture | pages [13] -->
m

<!-- b004813 | furniture | pages [13] -->
m

<!-- b004814 | furniture | pages [13] -->
m

<!-- b004815 | furniture | pages [13] -->
m

<!-- b004816 | furniture | pages [13] -->
m

<!-- b004817 | furniture | pages [13] -->
m

<!-- b004818 | furniture | pages [13] -->
m

<!-- b004819 | furniture | pages [13] -->
m

<!-- b004820 | furniture | pages [13] -->
m

<!-- b004821 | furniture | pages [13] -->
m

<!-- b004822 | furniture | pages [13] -->
m

<!-- b004823 | furniture | pages [13] -->
m

<!-- b004824 | furniture | pages [13] -->
m

<!-- b004825 | furniture | pages [13] -->
m

<!-- b004826 | furniture | pages [13] -->
m

<!-- b004827 | furniture | pages [13] -->
m

<!-- b004828 | furniture | pages [13] -->
m

<!-- b004829 | furniture | pages [13] -->
m

<!-- b004830 | furniture | pages [13] -->
m

<!-- b004831 | furniture | pages [13] -->
m

<!-- b004832 | furniture | pages [13] -->
m

<!-- b004833 | furniture | pages [13] -->
m

<!-- b004834 | furniture | pages [13] -->
m

<!-- b004835 | furniture | pages [13] -->
m

<!-- b004836 | furniture | pages [13] -->
m

<!-- b004837 | furniture | pages [13] -->
m

<!-- b004838 | furniture | pages [13] -->
m

<!-- b004839 | furniture | pages [13] -->
m

<!-- b004840 | furniture | pages [13] -->
m

<!-- b004841 | furniture | pages [13] -->
m

<!-- b004842 | furniture | pages [13] -->
m

<!-- b004843 | furniture | pages [13] -->
m

<!-- b004844 | furniture | pages [13] -->
m

<!-- b004845 | furniture | pages [13] -->
m

<!-- b004846 | furniture | pages [13] -->
m

<!-- b004847 | furniture | pages [13] -->
m

<!-- b004848 | furniture | pages [13] -->
m

<!-- b004849 | furniture | pages [13] -->
m

<!-- b004850 | furniture | pages [13] -->
m

<!-- b004851 | furniture | pages [13] -->
m

<!-- b004852 | furniture | pages [13] -->
m

<!-- b004853 | furniture | pages [13] -->
m

<!-- b004854 | furniture | pages [13] -->
m

<!-- b004855 | furniture | pages [13] -->
m

<!-- b004856 | furniture | pages [13] -->
m

<!-- b004857 | furniture | pages [13] -->
m

<!-- b004858 | furniture | pages [13] -->
m

<!-- b004859 | furniture | pages [13] -->
m

<!-- b004860 | furniture | pages [13] -->
m

<!-- b004861 | furniture | pages [13] -->
m

<!-- b004862 | furniture | pages [13] -->
m

<!-- b004863 | furniture | pages [13] -->
m

<!-- b004864 | furniture | pages [13] -->
m

<!-- b004865 | furniture | pages [13] -->
m

<!-- b004866 | furniture | pages [13] -->
m

<!-- b004867 | furniture | pages [13] -->
m

<!-- b004868 | furniture | pages [13] -->
m

<!-- b004869 | furniture | pages [13] -->
m

<!-- b004870 | furniture | pages [13] -->
m

<!-- b004871 | furniture | pages [13] -->
m

<!-- b004872 | furniture | pages [13] -->
m

<!-- b004873 | furniture | pages [13] -->
m

<!-- b004874 | furniture | pages [13] -->
m

<!-- b004875 | furniture | pages [13] -->
m

<!-- b004876 | furniture | pages [13] -->
m

<!-- b004877 | furniture | pages [13] -->
m

<!-- b004878 | furniture | pages [13] -->
m

<!-- b004879 | furniture | pages [13] -->
m

<!-- b004880 | furniture | pages [13] -->
m

<!-- b004881 | furniture | pages [13] -->
m

<!-- b004882 | furniture | pages [13] -->
m

<!-- b004883 | furniture | pages [13] -->
m

<!-- b004884 | furniture | pages [13] -->
m

<!-- b004885 | furniture | pages [13] -->
m

<!-- b004886 | furniture | pages [13] -->
m

<!-- b004887 | furniture | pages [13] -->
m

<!-- b004888 | furniture | pages [13] -->
m

<!-- b004889 | furniture | pages [13] -->
m

<!-- b004890 | furniture | pages [13] -->
m

<!-- b004891 | furniture | pages [13] -->
m

<!-- b004892 | furniture | pages [13] -->
m

<!-- b004893 | furniture | pages [13] -->
m

<!-- b004894 | furniture | pages [13] -->
m

<!-- b004895 | furniture | pages [13] -->
m

<!-- b004896 | furniture | pages [13] -->
m

<!-- b004897 | furniture | pages [13] -->
m

<!-- b004898 | furniture | pages [13] -->
m

<!-- b004899 | furniture | pages [13] -->
m

<!-- b004900 | furniture | pages [13] -->
m

<!-- b004901 | furniture | pages [13] -->
m

<!-- b004902 | furniture | pages [13] -->
m

<!-- b004903 | furniture | pages [13] -->
m

<!-- b004904 | furniture | pages [13] -->
m

<!-- b004905 | furniture | pages [13] -->
m

<!-- b004906 | furniture | pages [13] -->
m

<!-- b004907 | furniture | pages [13] -->
m

<!-- b004908 | furniture | pages [13] -->
m

<!-- b004909 | furniture | pages [13] -->
m

<!-- b004910 | furniture | pages [13] -->
m

<!-- b004911 | furniture | pages [13] -->
m

<!-- b004912 | furniture | pages [13] -->
m

<!-- b004913 | furniture | pages [13] -->
m

<!-- b004914 | furniture | pages [13] -->
m

<!-- b004915 | furniture | pages [13] -->
m

<!-- b004916 | furniture | pages [13] -->
m

<!-- b004917 | furniture | pages [13] -->
m

<!-- b004918 | furniture | pages [13] -->
m

<!-- b004919 | furniture | pages [13] -->
m

<!-- b004920 | furniture | pages [13] -->
m

<!-- b004921 | furniture | pages [13] -->
m

<!-- b004922 | furniture | pages [13] -->
m

<!-- b004923 | furniture | pages [13] -->
m

<!-- b004924 | furniture | pages [13] -->
m

<!-- b004925 | furniture | pages [13] -->
m

<!-- b004926 | furniture | pages [13] -->
m

<!-- b004927 | furniture | pages [13] -->
m

<!-- b004928 | furniture | pages [13] -->
m

<!-- b004929 | furniture | pages [13] -->
m

<!-- b004930 | furniture | pages [13] -->
m

<!-- b004931 | furniture | pages [13] -->
m

<!-- b004932 | furniture | pages [13] -->
m

<!-- b004933 | furniture | pages [13] -->
m

<!-- b004934 | furniture | pages [13] -->
m

<!-- b004935 | furniture | pages [13] -->
m

<!-- b004936 | furniture | pages [13] -->
m

<!-- b004937 | furniture | pages [13] -->
m

<!-- b004938 | furniture | pages [13] -->
m

<!-- b004939 | furniture | pages [13] -->
m

<!-- b004940 | furniture | pages [13] -->
m

<!-- b004941 | furniture | pages [13] -->
m

<!-- b004942 | furniture | pages [13] -->
m

<!-- b004943 | furniture | pages [13] -->
m

<!-- b004944 | furniture | pages [13] -->
m

<!-- b004945 | furniture | pages [13] -->
m

<!-- b004946 | furniture | pages [13] -->
m

<!-- b004947 | furniture | pages [13] -->
m

<!-- b004948 | furniture | pages [13] -->
m

<!-- b004949 | furniture | pages [13] -->
m

<!-- b004950 | furniture | pages [13] -->
m

<!-- b004951 | furniture | pages [13] -->
m

<!-- b004952 | furniture | pages [13] -->
m

<!-- b004953 | furniture | pages [13] -->
m

<!-- b004954 | furniture | pages [13] -->
m

<!-- b004955 | furniture | pages [13] -->
m

<!-- b004956 | furniture | pages [13] -->
m

<!-- b004957 | furniture | pages [13] -->
m

<!-- b004958 | furniture | pages [13] -->
m

<!-- b004959 | furniture | pages [13] -->
m

<!-- b004960 | furniture | pages [13] -->
m

<!-- b004961 | furniture | pages [13] -->
m

<!-- b004962 | furniture | pages [13] -->
m

<!-- b004963 | furniture | pages [13] -->
m

<!-- b004964 | furniture | pages [13] -->
m

<!-- b004965 | furniture | pages [13] -->
m

<!-- b004966 | furniture | pages [13] -->
m

<!-- b004967 | furniture | pages [13] -->
m

<!-- b004968 | furniture | pages [13] -->
m

<!-- b004969 | furniture | pages [13] -->
m

<!-- b004970 | furniture | pages [13] -->
m

<!-- b004971 | furniture | pages [13] -->
m

<!-- b004972 | furniture | pages [13] -->
m

<!-- b004973 | furniture | pages [13] -->
m

<!-- b004974 | furniture | pages [13] -->
m

<!-- b004975 | furniture | pages [13] -->
m

<!-- b004976 | furniture | pages [13] -->
m

<!-- b004977 | furniture | pages [13] -->
m

<!-- b004978 | furniture | pages [13] -->
m

<!-- b004979 | furniture | pages [13] -->
m

<!-- b004980 | furniture | pages [13] -->
m

<!-- b004981 | furniture | pages [13] -->
m

<!-- b004982 | furniture | pages [13] -->
m

<!-- b004983 | furniture | pages [13] -->
m

<!-- b004984 | furniture | pages [13] -->
m

<!-- b004985 | furniture | pages [13] -->
m

<!-- b004986 | furniture | pages [13] -->
m

<!-- b004987 | furniture | pages [13] -->
m

<!-- b004988 | furniture | pages [13] -->
m

<!-- b004989 | furniture | pages [13] -->
m

<!-- b004990 | furniture | pages [13] -->
m

<!-- b004991 | furniture | pages [13] -->
m

<!-- b004992 | furniture | pages [13] -->
m

<!-- b004993 | furniture | pages [13] -->
m

<!-- b004994 | furniture | pages [13] -->
m

<!-- b004995 | furniture | pages [13] -->
m

<!-- b004996 | furniture | pages [13] -->
m

<!-- b004997 | furniture | pages [13] -->
m

<!-- b004998 | furniture | pages [13] -->
m

<!-- b004999 | furniture | pages [13] -->
m

<!-- b005000 | furniture | pages [13] -->
m

<!-- b005001 | furniture | pages [13] -->
m

<!-- b005002 | furniture | pages [13] -->
m

<!-- b005003 | furniture | pages [13] -->
m

<!-- b005004 | furniture | pages [13] -->
m

<!-- b005005 | furniture | pages [13] -->
m

<!-- b005006 | furniture | pages [13] -->
m

<!-- b005007 | furniture | pages [13] -->
m

<!-- b005008 | furniture | pages [13] -->
m

<!-- b005009 | furniture | pages [13] -->
m

<!-- b005010 | furniture | pages [13] -->
m

<!-- b005011 | furniture | pages [13] -->
m

<!-- b005012 | furniture | pages [13] -->
m

<!-- b005013 | furniture | pages [13] -->
m

<!-- b005014 | furniture | pages [13] -->
m

<!-- b005015 | furniture | pages [13] -->
m

<!-- b005016 | furniture | pages [13] -->
m

<!-- b005017 | furniture | pages [13] -->
m

<!-- b005018 | furniture | pages [13] -->
m

<!-- b005019 | furniture | pages [13] -->
m

<!-- b005020 | furniture | pages [13] -->
m

<!-- b005021 | furniture | pages [13] -->
m

<!-- b005022 | furniture | pages [13] -->
m

<!-- b005023 | furniture | pages [13] -->
m

<!-- b005024 | furniture | pages [13] -->
m

<!-- b005025 | furniture | pages [13] -->
m

<!-- b005026 | furniture | pages [13] -->
m

<!-- b005027 | furniture | pages [13] -->
m

<!-- b005028 | furniture | pages [13] -->
m

<!-- b005029 | furniture | pages [13] -->
m

<!-- b005030 | furniture | pages [13] -->
m

<!-- b005031 | furniture | pages [13] -->
m

<!-- b005032 | furniture | pages [13] -->
m

<!-- b005033 | furniture | pages [13] -->
m

<!-- b005034 | furniture | pages [13] -->
m

<!-- b005035 | furniture | pages [13] -->
m

<!-- b005036 | furniture | pages [13] -->
m

<!-- b005037 | furniture | pages [13] -->
m

<!-- b005038 | furniture | pages [13] -->
m

<!-- b005039 | furniture | pages [13] -->
m

<!-- b005040 | furniture | pages [13] -->
m

<!-- b005041 | furniture | pages [13] -->
m

<!-- b005042 | furniture | pages [13] -->
m

<!-- b005043 | furniture | pages [13] -->
m

<!-- b005044 | furniture | pages [13] -->
m

<!-- b005045 | furniture | pages [13] -->
m

<!-- b005046 | furniture | pages [13] -->
m

<!-- b005047 | furniture | pages [13] -->
m

<!-- b005048 | furniture | pages [13] -->
m

<!-- b005049 | furniture | pages [13] -->
m

<!-- b005050 | furniture | pages [13] -->
m

<!-- b005051 | furniture | pages [13] -->
m

<!-- b005052 | furniture | pages [13] -->
m

<!-- b005053 | furniture | pages [13] -->
m

<!-- b005054 | furniture | pages [13] -->
m

<!-- b005055 | furniture | pages [13] -->
m

<!-- b005056 | furniture | pages [13] -->
m

<!-- b005057 | furniture | pages [13] -->
m

<!-- b005058 | furniture | pages [13] -->
m

<!-- b005059 | furniture | pages [13] -->
m

<!-- b005060 | furniture | pages [13] -->
m

<!-- b005061 | furniture | pages [13] -->
m

<!-- b005062 | furniture | pages [13] -->
m

<!-- b005063 | furniture | pages [13] -->
m

<!-- b005064 | furniture | pages [13] -->
m

<!-- b005065 | furniture | pages [13] -->
m

<!-- b005066 | furniture | pages [13] -->
m

<!-- b005067 | furniture | pages [13] -->
m

<!-- b005068 | furniture | pages [13] -->
m

<!-- b005069 | furniture | pages [13] -->
m

<!-- b005070 | furniture | pages [13] -->
m

<!-- b005071 | furniture | pages [13] -->
m

<!-- b005072 | furniture | pages [13] -->
m

<!-- b005073 | furniture | pages [13] -->
m

<!-- b005074 | furniture | pages [13] -->
m

<!-- b005075 | furniture | pages [13] -->
m

<!-- b005076 | furniture | pages [13] -->
m

<!-- b005077 | furniture | pages [13] -->
m

<!-- b005078 | furniture | pages [13] -->
m

<!-- b005079 | furniture | pages [13] -->
m

<!-- b005080 | furniture | pages [13] -->
m

<!-- b005081 | furniture | pages [13] -->
m

<!-- b005082 | furniture | pages [13] -->
m

<!-- b005083 | furniture | pages [13] -->
m

<!-- b005084 | furniture | pages [13] -->
m

<!-- b005085 | furniture | pages [13] -->
m

<!-- b005086 | furniture | pages [13] -->
m

<!-- b005087 | furniture | pages [13] -->
m

<!-- b005088 | furniture | pages [13] -->
m

<!-- b005089 | furniture | pages [13] -->
m

<!-- b005090 | furniture | pages [13] -->
m

<!-- b005091 | furniture | pages [14] -->
Team # 2510862

<!-- b005092 | prose | pages [14] -->
m

<!-- b005093 | prose | pages [14] -->
m

<!-- b005094 | prose | pages [14] -->
m

<!-- b005095 | prose | pages [14] -->
m

<!-- b005096 | prose | pages [14] -->
m

<!-- b005097 | prose | pages [14] -->
m

<!-- b005098 | prose | pages [14] -->
m

<!-- b005099 | prose | pages [14] -->
m

<!-- b005100 | prose | pages [14] -->
m

<!-- b005101 | prose | pages [14] -->
m

<!-- b005102 | prose | pages [14] -->
m

<!-- b005103 | prose | pages [14] -->
m

<!-- b005104 | prose | pages [14] -->
m

<!-- b005105 | prose | pages [14] -->
m

<!-- b005106 | prose | pages [14] -->
m

<!-- b005107 | prose | pages [14] -->
m

<!-- b005108 | prose | pages [14] -->
m

<!-- b005109 | prose | pages [14] -->
m

<!-- b005110 | prose | pages [14] -->
m

<!-- b005111 | prose | pages [14] -->
m

<!-- b005112 | prose | pages [14] -->
m

<!-- b005113 | prose | pages [14] -->
m

<!-- b005114 | prose | pages [14] -->
m

<!-- b005115 | prose | pages [14] -->
m

<!-- b005116 | prose | pages [14] -->
m

<!-- b005117 | prose | pages [14] -->
m

<!-- b005118 | prose | pages [14] -->
m

<!-- b005119 | prose | pages [14] -->
m

<!-- b005120 | prose | pages [14] -->
m

<!-- b005121 | prose | pages [14] -->
m

<!-- b005122 | prose | pages [14] -->
m

<!-- b005123 | prose | pages [14] -->
m

<!-- b005124 | prose | pages [14] -->
m

<!-- b005125 | prose | pages [14] -->
m

<!-- b005126 | prose | pages [14] -->
m

<!-- b005127 | prose | pages [14] -->
m

<!-- b005128 | prose | pages [14] -->
m

<!-- b005129 | prose | pages [14] -->
m

<!-- b005130 | prose | pages [14] -->
m

<!-- b005131 | prose | pages [14] -->
m

<!-- b005132 | prose | pages [14] -->
m

<!-- b005133 | prose | pages [14] -->
m

<!-- b005134 | prose | pages [14] -->
m

<!-- b005135 | prose | pages [14] -->
m

<!-- b005136 | prose | pages [14] -->
m

<!-- b005137 | prose | pages [14] -->
m

<!-- b005138 | prose | pages [14] -->
m

<!-- b005139 | prose | pages [14] -->
m

<!-- b005140 | prose | pages [14] -->
m

<!-- b005141 | prose | pages [14] -->
m

<!-- b005142 | prose | pages [14] -->
m

<!-- b005143 | prose | pages [14] -->
m

<!-- b005144 | prose | pages [14] -->
m

<!-- b005145 | prose | pages [14] -->
m

<!-- b005146 | prose | pages [14] -->
m

<!-- b005147 | prose | pages [14] -->
m

<!-- b005148 | prose | pages [14] -->
m

<!-- b005149 | prose | pages [14] -->
m

<!-- b005150 | prose | pages [14] -->
m

<!-- b005151 | prose | pages [14] -->
m

<!-- b005152 | prose | pages [14] -->
m

<!-- b005153 | prose | pages [14] -->
m

<!-- b005154 | prose | pages [14] -->
m

<!-- b005155 | prose | pages [14] -->
m

<!-- b005156 | prose | pages [14] -->
m

<!-- b005157 | prose | pages [14] -->
m

<!-- b005158 | prose | pages [14] -->
m

<!-- b005159 | prose | pages [14] -->
m

<!-- b005160 | prose | pages [14] -->
m

<!-- b005161 | prose | pages [14] -->
m

<!-- b005162 | prose | pages [14] -->
m

<!-- b005163 | prose | pages [14] -->
m

<!-- b005164 | prose | pages [14] -->
m

<!-- b005165 | prose | pages [14] -->
m

<!-- b005166 | prose | pages [14] -->
m

<!-- b005167 | prose | pages [14] -->
m

<!-- b005168 | prose | pages [14] -->
m

<!-- b005169 | prose | pages [14] -->
m

<!-- b005170 | prose | pages [14] -->
m

<!-- b005171 | prose | pages [14] -->
m

<!-- b005172 | prose | pages [14] -->
m

<!-- b005173 | prose | pages [14] -->
m

<!-- b005174 | prose | pages [14] -->
m

<!-- b005175 | prose | pages [14] -->
m

<!-- b005176 | prose | pages [14] -->
m

<!-- b005177 | prose | pages [14] -->
m

<!-- b005178 | prose | pages [14] -->
m

<!-- b005179 | prose | pages [14] -->
m

<!-- b005180 | prose | pages [14] -->
m

<!-- b005181 | prose | pages [14] -->
m

<!-- b005182 | prose | pages [14] -->
m

<!-- b005183 | prose | pages [14] -->
m

<!-- b005184 | prose | pages [14] -->
m

<!-- b005185 | prose | pages [14] -->
m

<!-- b005186 | prose | pages [14] -->
m

<!-- b005187 | prose | pages [14] -->
m

<!-- b005188 | prose | pages [14] -->
m

<!-- b005189 | prose | pages [14] -->
m

<!-- b005190 | prose | pages [14] -->
m

<!-- b005191 | prose | pages [14] -->
m

<!-- b005192 | prose | pages [14] -->
m

<!-- b005193 | prose | pages [14] -->
m

<!-- b005194 | prose | pages [14] -->
m

<!-- b005195 | prose | pages [14] -->
m

<!-- b005196 | prose | pages [14] -->
m

<!-- b005197 | prose | pages [14] -->
m

<!-- b005198 | prose | pages [14] -->
m

<!-- b005199 | prose | pages [14] -->
m

<!-- b005200 | prose | pages [14] -->
m

<!-- b005201 | prose | pages [14] -->
m

<!-- b005202 | prose | pages [14] -->
m

<!-- b005203 | prose | pages [14] -->
m

<!-- b005204 | prose | pages [14] -->
m

<!-- b005205 | prose | pages [14] -->
m

<!-- b005206 | prose | pages [14] -->
m

<!-- b005207 | prose | pages [14] -->
m

<!-- b005208 | prose | pages [14] -->
m

<!-- b005209 | prose | pages [14] -->
m

<!-- b005210 | prose | pages [14] -->
m

<!-- b005211 | prose | pages [14] -->
m

<!-- b005212 | prose | pages [14] -->
m

<!-- b005213 | prose | pages [14] -->
m

<!-- b005214 | prose | pages [14] -->
m

<!-- b005215 | prose | pages [14] -->
m

<!-- b005216 | prose | pages [14] -->
m

<!-- b005217 | prose | pages [14] -->
m

<!-- b005218 | prose | pages [14] -->
m

<!-- b005219 | prose | pages [14] -->
m

<!-- b005220 | prose | pages [14] -->
m

<!-- b005221 | prose | pages [14] -->
m

<!-- b005222 | prose | pages [14] -->
m

<!-- b005223 | prose | pages [14] -->
m

<!-- b005224 | prose | pages [14] -->
m

<!-- b005225 | prose | pages [14] -->
m

<!-- b005226 | prose | pages [14] -->
m

<!-- b005227 | prose | pages [14] -->
m

<!-- b005228 | prose | pages [14] -->
m

<!-- b005229 | prose | pages [14] -->
m

<!-- b005230 | prose | pages [14] -->
m

<!-- b005231 | prose | pages [14] -->
m

<!-- b005232 | prose | pages [14] -->
m

<!-- b005233 | prose | pages [14] -->
m

<!-- b005234 | prose | pages [14] -->
m

<!-- b005235 | prose | pages [14] -->
m

<!-- b005236 | prose | pages [14] -->
m

<!-- b005237 | prose | pages [14] -->
m

<!-- b005238 | prose | pages [14] -->
m

<!-- b005239 | prose | pages [14] -->
m

<!-- b005240 | prose | pages [14] -->
m

<!-- b005241 | prose | pages [14] -->
m

<!-- b005242 | prose | pages [14] -->
m

<!-- b005243 | prose | pages [14] -->
m

<!-- b005244 | prose | pages [14] -->
m

<!-- b005245 | prose | pages [14] -->
m

<!-- b005246 | prose | pages [14] -->
m

<!-- b005247 | prose | pages [14] -->
m

<!-- b005248 | prose | pages [14] -->
m

<!-- b005249 | prose | pages [14] -->
m

<!-- b005250 | prose | pages [14] -->
m

<!-- b005251 | prose | pages [14] -->
m

<!-- b005252 | prose | pages [14] -->
m

<!-- b005253 | prose | pages [14] -->
m

<!-- b005254 | prose | pages [14] -->
m

<!-- b005255 | prose | pages [14] -->
m

<!-- b005256 | prose | pages [14] -->
m

<!-- b005257 | prose | pages [14] -->
m

<!-- b005258 | prose | pages [14] -->
m

<!-- b005259 | prose | pages [14] -->
m

<!-- b005260 | prose | pages [14] -->
m

<!-- b005261 | prose | pages [14] -->
m

<!-- b005262 | prose | pages [14] -->
m

<!-- b005263 | prose | pages [14] -->
m

<!-- b005264 | prose | pages [14] -->
m

<!-- b005265 | prose | pages [14] -->
m

<!-- b005266 | prose | pages [14] -->
m

<!-- b005267 | prose | pages [14] -->
m

<!-- b005268 | prose | pages [14] -->
m

<!-- b005269 | prose | pages [14] -->
m

<!-- b005270 | prose | pages [14] -->
m

<!-- b005271 | prose | pages [14] -->
m

<!-- b005272 | prose | pages [14] -->
m

<!-- b005273 | prose | pages [14] -->
m

<!-- b005274 | prose | pages [14] -->
m

<!-- b005275 | prose | pages [14] -->
m

<!-- b005276 | prose | pages [14] -->
m

<!-- b005277 | prose | pages [14] -->
m

<!-- b005278 | prose | pages [14] -->
m

<!-- b005279 | prose | pages [14] -->
m

<!-- b005280 | prose | pages [14] -->
m

<!-- b005281 | prose | pages [14] -->
m

<!-- b005282 | prose | pages [14] -->
m

<!-- b005283 | prose | pages [14] -->
m

<!-- b005284 | prose | pages [14] -->
m

<!-- b005285 | prose | pages [14] -->
m

<!-- b005286 | prose | pages [14] -->
m

<!-- b005287 | prose | pages [14] -->
m

<!-- b005288 | prose | pages [14] -->
m

<!-- b005289 | prose | pages [14] -->
m

<!-- b005290 | prose | pages [14] -->
m

<!-- b005291 | prose | pages [14] -->
m

<!-- b005292 | prose | pages [14] -->
m

<!-- b005293 | prose | pages [14] -->
m

<!-- b005294 | prose | pages [14] -->
m

<!-- b005295 | prose | pages [14] -->
m

<!-- b005296 | prose | pages [14] -->
m

<!-- b005297 | prose | pages [14] -->
m

<!-- b005298 | prose | pages [14] -->
m

<!-- b005299 | prose | pages [14] -->
m

<!-- b005300 | prose | pages [14] -->
m

<!-- b005301 | prose | pages [14] -->
m

<!-- b005302 | prose | pages [14] -->
m

<!-- b005303 | prose | pages [14] -->
m

<!-- b005304 | prose | pages [14] -->
m

<!-- b005305 | prose | pages [14] -->
m

<!-- b005306 | prose | pages [14] -->
m

<!-- b005307 | prose | pages [14] -->
m

<!-- b005308 | prose | pages [14] -->
m

<!-- b005309 | prose | pages [14] -->
m

<!-- b005310 | prose | pages [14] -->
m

<!-- b005311 | prose | pages [14] -->
m

<!-- b005312 | prose | pages [14] -->
m

<!-- b005313 | prose | pages [14] -->
m

<!-- b005314 | prose | pages [14] -->
m

<!-- b005315 | prose | pages [14] -->
m

<!-- b005316 | prose | pages [14] -->
m

<!-- b005317 | prose | pages [14] -->
m

<!-- b005318 | prose | pages [14] -->
m

<!-- b005319 | prose | pages [14] -->
m

<!-- b005320 | prose | pages [14] -->
m

<!-- b005321 | prose | pages [14] -->
m

<!-- b005322 | prose | pages [14] -->
m

<!-- b005323 | prose | pages [14] -->
m

<!-- b005324 | prose | pages [14] -->
m

<!-- b005325 | prose | pages [14] -->
m

<!-- b005326 | prose | pages [14] -->
m

<!-- b005327 | prose | pages [14] -->
m

<!-- b005328 | prose | pages [14] -->
m

<!-- b005329 | prose | pages [14] -->
m

<!-- b005330 | prose | pages [14] -->
m

<!-- b005331 | prose | pages [14] -->
m

<!-- b005332 | prose | pages [14] -->
m

<!-- b005333 | prose | pages [14] -->
m

<!-- b005334 | prose | pages [14] -->
m

<!-- b005335 | prose | pages [14] -->
m

<!-- b005336 | prose | pages [14] -->
m

<!-- b005337 | prose | pages [14] -->
m

<!-- b005338 | prose | pages [14] -->
m

<!-- b005339 | prose | pages [14] -->
m

<!-- b005340 | prose | pages [14] -->
m

<!-- b005341 | prose | pages [14] -->
m

<!-- b005342 | prose | pages [14] -->
m

<!-- b005343 | prose | pages [14] -->
m

<!-- b005344 | prose | pages [14] -->
m

<!-- b005345 | prose | pages [14] -->
m

<!-- b005346 | prose | pages [14] -->
m

<!-- b005347 | prose | pages [14] -->
m

<!-- b005348 | prose | pages [14] -->
m

<!-- b005349 | prose | pages [14] -->
m

<!-- b005350 | prose | pages [14] -->
m

<!-- b005351 | prose | pages [14] -->
m

<!-- b005352 | prose | pages [14] -->
m

<!-- b005353 | prose | pages [14] -->
m

<!-- b005354 | prose | pages [14] -->
m

<!-- b005355 | prose | pages [14] -->
m

<!-- b005356 | prose | pages [14] -->
m

<!-- b005357 | prose | pages [14] -->
m

<!-- b005358 | prose | pages [14] -->
m

<!-- b005359 | prose | pages [14] -->
m

<!-- b005360 | prose | pages [14] -->
m

<!-- b005361 | prose | pages [14] -->
m

<!-- b005362 | prose | pages [14] -->
m

<!-- b005363 | prose | pages [14] -->
m

<!-- b005364 | prose | pages [14] -->
m

<!-- b005365 | prose | pages [14] -->
m

<!-- b005366 | prose | pages [14] -->
m

<!-- b005367 | prose | pages [14] -->
m

<!-- b005368 | prose | pages [14] -->
m

<!-- b005369 | prose | pages [14] -->
m

<!-- b005370 | prose | pages [14] -->
m

<!-- b005371 | prose | pages [14] -->
m

<!-- b005372 | prose | pages [14] -->
m

<!-- b005373 | prose | pages [14] -->
m

<!-- b005374 | prose | pages [14] -->
m

<!-- b005375 | prose | pages [14] -->
m

<!-- b005376 | prose | pages [14] -->
m

<!-- b005377 | prose | pages [14] -->
m

<!-- b005378 | prose | pages [14] -->
m

<!-- b005379 | prose | pages [14] -->
m

<!-- b005380 | prose | pages [14] -->
m

<!-- b005381 | prose | pages [14] -->
m

<!-- b005382 | prose | pages [14] -->
m

<!-- b005383 | prose | pages [14] -->
m

<!-- b005384 | prose | pages [14] -->
m

<!-- b005385 | prose | pages [14] -->
m

<!-- b005386 | prose | pages [14] -->
m

<!-- b005387 | prose | pages [14] -->
m

<!-- b005388 | prose | pages [14] -->
m

<!-- b005389 | prose | pages [14] -->
m

<!-- b005390 | prose | pages [14] -->
m

<!-- b005391 | prose | pages [14] -->
m

<!-- b005392 | prose | pages [14] -->
m

<!-- b005393 | prose | pages [14] -->
m

<!-- b005394 | prose | pages [14] -->
m

<!-- b005395 | prose | pages [14] -->
m

<!-- b005396 | prose | pages [14] -->
m

<!-- b005397 | prose | pages [14] -->
m

<!-- b005398 | prose | pages [14] -->
m

<!-- b005399 | prose | pages [14] -->
m

<!-- b005400 | prose | pages [14] -->
m

<!-- b005401 | prose | pages [14] -->
m

<!-- b005402 | prose | pages [14] -->
m

<!-- b005403 | prose | pages [14] -->
m

<!-- b005404 | prose | pages [14] -->
m

<!-- b005405 | prose | pages [14] -->
m

<!-- b005406 | prose | pages [14] -->
m

<!-- b005407 | prose | pages [14] -->
m

<!-- b005408 | prose | pages [14] -->
m

<!-- b005409 | prose | pages [14] -->
m

<!-- b005410 | prose | pages [14] -->
m

<!-- b005411 | prose | pages [14] -->
m

<!-- b005412 | prose | pages [14] -->
m

<!-- b005413 | prose | pages [14] -->
m

<!-- b005414 | prose | pages [14] -->
m

<!-- b005415 | prose | pages [14] -->
m

<!-- b005416 | prose | pages [14] -->
m

<!-- b005417 | prose | pages [14] -->
m

<!-- b005418 | prose | pages [14] -->
m

<!-- b005419 | prose | pages [14] -->
m

<!-- b005420 | prose | pages [14] -->
m

<!-- b005421 | prose | pages [14] -->
m

<!-- b005422 | prose | pages [14] -->
m

<!-- b005423 | prose | pages [14] -->
m

<!-- b005424 | prose | pages [14] -->
m

<!-- b005425 | prose | pages [14] -->
m

<!-- b005426 | prose | pages [14] -->
m

<!-- b005427 | prose | pages [14] -->
m

<!-- b005428 | prose | pages [14] -->
m

<!-- b005429 | prose | pages [14] -->
m

<!-- b005430 | prose | pages [14] -->
m

<!-- b005431 | prose | pages [14] -->
m

<!-- b005432 | prose | pages [14] -->
m

<!-- b005433 | prose | pages [14] -->
m

<!-- b005434 | prose | pages [14] -->
m

<!-- b005435 | prose | pages [14] -->
m

<!-- b005436 | prose | pages [14] -->
m

<!-- b005437 | prose | pages [14] -->
m

<!-- b005438 | prose | pages [14] -->
m

<!-- b005439 | prose | pages [14] -->
m

<!-- b005440 | prose | pages [14] -->
m

<!-- b005441 | prose | pages [14] -->
m

<!-- b005442 | prose | pages [14] -->
m

<!-- b005443 | prose | pages [14] -->
m

<!-- b005444 | prose | pages [14] -->
m

<!-- b005445 | prose | pages [14] -->
m

<!-- b005446 | prose | pages [14] -->
m

<!-- b005447 | prose | pages [14] -->
m

<!-- b005448 | prose | pages [14] -->
m

<!-- b005449 | prose | pages [14] -->
m

<!-- b005450 | prose | pages [14] -->
m

<!-- b005451 | prose | pages [14] -->
m

<!-- b005452 | prose | pages [14] -->
m

<!-- b005453 | prose | pages [14] -->
m

<!-- b005454 | prose | pages [14] -->
m

<!-- b005455 | prose | pages [14] -->
m

<!-- b005456 | prose | pages [14] -->
m

<!-- b005457 | prose | pages [14] -->
m

<!-- b005458 | prose | pages [14] -->
m

<!-- b005459 | prose | pages [14] -->
m

<!-- b005460 | prose | pages [14] -->
m

<!-- b005461 | prose | pages [14] -->
m

<!-- b005462 | prose | pages [14] -->
m

<!-- b005463 | prose | pages [14] -->
m

<!-- b005464 | prose | pages [14] -->
m

<!-- b005465 | prose | pages [14] -->
m

<!-- b005466 | prose | pages [14] -->
m

<!-- b005467 | prose | pages [14] -->
m

<!-- b005468 | prose | pages [14] -->
m

<!-- b005469 | prose | pages [14] -->
m

<!-- b005470 | prose | pages [14] -->
m

<!-- b005471 | prose | pages [14] -->
m

<!-- b005472 | prose | pages [14] -->
m

<!-- b005473 | prose | pages [14] -->
m

<!-- b005474 | prose | pages [14] -->
m

<!-- b005475 | prose | pages [14] -->
m

<!-- b005476 | prose | pages [14] -->
m

<!-- b005477 | prose | pages [14] -->
m

<!-- b005478 | prose | pages [14] -->
m

<!-- b005479 | prose | pages [14] -->
m

<!-- b005480 | prose | pages [14] -->
m

<!-- b005481 | prose | pages [14] -->
m

<!-- b005482 | prose | pages [14] -->
m

<!-- b005483 | prose | pages [14] -->
m

<!-- b005484 | prose | pages [14] -->
m

<!-- b005485 | prose | pages [14] -->
m

<!-- b005486 | prose | pages [14] -->
m

<!-- b005487 | prose | pages [14] -->
m

<!-- b005488 | prose | pages [14] -->
m

<!-- b005489 | prose | pages [14] -->
m

<!-- b005490 | prose | pages [14] -->
m

<!-- b005491 | prose | pages [14] -->
m

<!-- b005492 | prose | pages [14] -->
m

<!-- b005493 | prose | pages [14] -->
m

<!-- b005494 | prose | pages [14] -->
m

<!-- b005495 | prose | pages [14] -->
m

<!-- b005496 | prose | pages [14] -->
m

<!-- b005497 | prose | pages [14] -->
m

<!-- b005498 | prose | pages [14] -->
m

<!-- b005499 | prose | pages [14] -->
m

<!-- b005500 | prose | pages [14] -->
m

<!-- b005501 | prose | pages [14] -->
m

<!-- b005502 | prose | pages [14] -->
m

<!-- b005503 | prose | pages [14] -->
m

<!-- b005504 | prose | pages [14] -->
m

<!-- b005505 | prose | pages [14] -->
m

<!-- b005506 | prose | pages [14] -->
m

<!-- b005507 | prose | pages [14] -->
m

<!-- b005508 | prose | pages [14] -->
m

<!-- b005509 | prose | pages [14] -->
m

<!-- b005510 | prose | pages [14] -->
m

<!-- b005511 | prose | pages [14] -->
m

<!-- b005512 | prose | pages [14] -->
m

<!-- b005513 | prose | pages [14] -->
m

<!-- b005514 | prose | pages [14] -->
m

<!-- b005515 | prose | pages [14] -->
m

<!-- b005516 | prose | pages [14] -->
m

<!-- b005517 | prose | pages [14] -->
m

<!-- b005518 | prose | pages [14] -->
m

<!-- b005519 | prose | pages [14] -->
m

<!-- b005520 | prose | pages [14] -->
m

<!-- b005521 | prose | pages [14] -->
m

<!-- b005522 | prose | pages [14] -->
m

<!-- b005523 | prose | pages [14] -->
m

<!-- b005524 | prose | pages [14] -->
m

<!-- b005525 | prose | pages [14] -->
m

<!-- b005526 | prose | pages [14] -->
m

<!-- b005527 | prose | pages [14] -->
m

<!-- b005528 | prose | pages [14] -->
m

<!-- b005529 | prose | pages [14] -->
m

<!-- b005530 | prose | pages [14] -->
m

<!-- b005531 | prose | pages [14] -->
m

<!-- b005532 | prose | pages [14] -->
m

<!-- b005533 | prose | pages [14] -->
m

<!-- b005534 | prose | pages [14] -->
m

<!-- b005535 | prose | pages [14] -->
m

<!-- b005536 | prose | pages [14] -->
m

<!-- b005537 | prose | pages [14] -->
m

<!-- b005538 | prose | pages [14] -->
m

<!-- b005539 | prose | pages [14] -->
m

<!-- b005540 | prose | pages [14] -->
m

<!-- b005541 | prose | pages [14] -->
m

<!-- b005542 | prose | pages [14] -->
m

<!-- b005543 | prose | pages [14] -->
m

<!-- b005544 | prose | pages [14] -->
m

<!-- b005545 | prose | pages [14] -->
m

<!-- b005546 | prose | pages [14] -->
m

<!-- b005547 | prose | pages [14] -->
m

<!-- b005548 | prose | pages [14] -->
m

<!-- b005549 | prose | pages [14] -->
m

<!-- b005550 | prose | pages [14] -->
m

<!-- b005551 | prose | pages [14] -->
m

<!-- b005552 | prose | pages [14] -->
m

<!-- b005553 | prose | pages [14] -->
m

<!-- b005554 | prose | pages [14] -->
m

<!-- b005555 | prose | pages [14] -->
m

<!-- b005556 | prose | pages [14] -->
m

<!-- b005557 | prose | pages [14] -->
m

<!-- b005558 | prose | pages [14] -->
m

<!-- b005559 | prose | pages [14] -->
m

<!-- b005560 | prose | pages [14] -->
m

<!-- b005561 | prose | pages [14] -->
m

<!-- b005562 | prose | pages [14] -->
m

<!-- b005563 | prose | pages [14] -->
m

<!-- b005564 | prose | pages [14] -->
m

<!-- b005565 | prose | pages [14] -->
m

<!-- b005566 | prose | pages [14] -->
m

<!-- b005567 | prose | pages [14] -->
m

<!-- b005568 | prose | pages [14] -->
m

<!-- b005569 | prose | pages [14] -->
m

<!-- b005570 | prose | pages [14] -->
m

<!-- b005571 | prose | pages [14] -->
m

<!-- b005572 | prose | pages [14] -->
m

<!-- b005573 | prose | pages [14] -->
m

<!-- b005574 | prose | pages [14] -->
m

<!-- b005575 | prose | pages [14] -->
m

<!-- b005576 | prose | pages [14] -->
m

<!-- b005577 | prose | pages [14] -->
m

<!-- b005578 | prose | pages [14] -->
m

<!-- b005579 | prose | pages [14] -->
m

<!-- b005580 | prose | pages [14] -->
m

<!-- b005581 | prose | pages [14] -->
m

<!-- b005582 | prose | pages [14] -->
m

<!-- b005583 | prose | pages [14] -->
m

<!-- b005584 | prose | pages [14] -->
m

<!-- b005585 | prose | pages [14] -->
m

<!-- b005586 | prose | pages [14] -->
m

<!-- b005587 | prose | pages [14] -->
m

<!-- b005588 | prose | pages [14] -->
m

<!-- b005589 | prose | pages [14] -->
m

<!-- b005590 | prose | pages [14] -->
m

<!-- b005591 | prose | pages [14] -->
m

<!-- b005592 | prose | pages [14] -->
m

<!-- b005593 | prose | pages [14] -->
m

<!-- b005594 | prose | pages [14] -->
m

<!-- b005595 | prose | pages [14] -->
m

<!-- b005596 | prose | pages [14] -->
m

<!-- b005597 | prose | pages [14] -->
m

<!-- b005598 | prose | pages [14] -->
m

<!-- b005599 | prose | pages [14] -->
m

<!-- b005600 | prose | pages [14] -->
m

<!-- b005601 | prose | pages [14] -->
m

<!-- b005602 | prose | pages [14] -->
m

<!-- b005603 | prose | pages [14] -->
m

<!-- b005604 | prose | pages [14] -->
m

<!-- b005605 | prose | pages [14] -->
m

<!-- b005606 | prose | pages [14] -->
m

<!-- b005607 | prose | pages [14] -->
m

<!-- b005608 | prose | pages [14] -->
m

<!-- b005609 | prose | pages [14] -->
m

<!-- b005610 | prose | pages [14] -->
m

<!-- b005611 | prose | pages [14] -->
m

<!-- b005612 | prose | pages [14] -->
m

<!-- b005613 | prose | pages [14] -->
m

<!-- b005614 | prose | pages [14] -->
m

<!-- b005615 | prose | pages [14] -->
m

<!-- b005616 | prose | pages [14] -->
m

<!-- b005617 | prose | pages [14] -->
m

<!-- b005618 | prose | pages [14] -->
m

<!-- b005619 | prose | pages [14] -->
m

<!-- b005620 | prose | pages [14] -->
m

<!-- b005621 | prose | pages [14] -->
m

<!-- b005622 | prose | pages [14] -->
m

<!-- b005623 | prose | pages [14] -->
m

<!-- b005624 | prose | pages [14] -->
m

<!-- b005625 | prose | pages [14] -->
m

<!-- b005626 | prose | pages [14] -->
m

<!-- b005627 | prose | pages [14] -->
m

<!-- b005628 | prose | pages [14] -->
m

<!-- b005629 | prose | pages [14] -->
m

<!-- b005630 | prose | pages [14] -->
m

<!-- b005631 | prose | pages [14] -->
m

<!-- b005632 | prose | pages [14] -->
m

<!-- b005633 | prose | pages [14] -->
m

<!-- b005634 | prose | pages [14] -->
m

<!-- b005635 | prose | pages [14] -->
m

<!-- b005636 | prose | pages [14] -->
m

<!-- b005637 | prose | pages [14] -->
m

<!-- b005638 | prose | pages [14] -->
m

<!-- b005639 | prose | pages [14] -->
m

<!-- b005640 | prose | pages [14] -->
m

<!-- b005641 | prose | pages [14] -->
m

<!-- b005642 | prose | pages [14] -->
m

<!-- b005643 | prose | pages [14] -->
m

<!-- b005644 | prose | pages [14] -->
m

<!-- b005645 | prose | pages [14] -->
m

<!-- b005646 | prose | pages [14] -->
m

<!-- b005647 | prose | pages [14] -->
m

<!-- b005648 | prose | pages [14] -->
m

<!-- b005649 | prose | pages [14] -->
m

<!-- b005650 | prose | pages [14] -->
m

<!-- b005651 | prose | pages [14] -->
m

<!-- b005652 | prose | pages [14] -->
m

<!-- b005653 | prose | pages [14] -->
m

<!-- b005654 | prose | pages [14] -->
m

<!-- b005655 | prose | pages [14] -->
m

<!-- b005656 | prose | pages [14] -->
m

<!-- b005657 | prose | pages [14] -->
m

<!-- b005658 | prose | pages [14] -->
m

<!-- b005659 | prose | pages [14] -->
m

<!-- b005660 | prose | pages [14] -->
m

<!-- b005661 | prose | pages [14] -->
m

<!-- b005662 | prose | pages [14] -->
m

<!-- b005663 | prose | pages [14] -->
m

<!-- b005664 | prose | pages [14] -->
m

<!-- b005665 | prose | pages [14] -->
m

<!-- b005666 | prose | pages [14] -->
m

<!-- b005667 | prose | pages [14] -->
m

<!-- b005668 | prose | pages [14] -->
m

<!-- b005669 | prose | pages [14] -->
m

<!-- b005670 | prose | pages [14] -->
m

<!-- b005671 | prose | pages [14] -->
m

<!-- b005672 | prose | pages [14] -->
m

<!-- b005673 | prose | pages [14] -->
m

<!-- b005674 | prose | pages [14] -->
m

<!-- b005675 | prose | pages [14] -->
m

<!-- b005676 | prose | pages [14] -->
m

<!-- b005677 | prose | pages [14] -->
m

<!-- b005678 | prose | pages [14] -->
m

<!-- b005679 | prose | pages [14] -->
m

<!-- b005680 | prose | pages [14] -->
m

<!-- b005681 | prose | pages [14] -->
m

<!-- b005682 | prose | pages [14] -->
m

<!-- b005683 | prose | pages [14] -->
m

<!-- b005684 | prose | pages [14] -->
m

<!-- b005685 | prose | pages [14] -->
m

<!-- b005686 | prose | pages [14] -->
m

<!-- b005687 | prose | pages [14] -->
m

<!-- b005688 | prose | pages [14] -->
m

<!-- b005689 | prose | pages [14] -->
m

<!-- b005690 | prose | pages [14] -->
m

<!-- b005691 | prose | pages [14] -->
m

<!-- b005692 | prose | pages [14] -->
m

<!-- b005693 | prose | pages [14] -->
m

<!-- b005694 | prose | pages [14] -->
m

<!-- b005695 | prose | pages [14] -->
m

<!-- b005696 | prose | pages [14] -->
m

<!-- b005697 | prose | pages [14] -->
m

<!-- b005698 | prose | pages [14] -->
m

<!-- b005699 | prose | pages [14] -->
m

<!-- b005700 | prose | pages [14] -->
m

<!-- b005701 | prose | pages [14] -->
m

<!-- b005702 | prose | pages [14] -->
m

<!-- b005703 | prose | pages [14] -->
m

<!-- b005704 | prose | pages [14] -->
m

<!-- b005705 | prose | pages [14] -->
m

<!-- b005706 | prose | pages [14] -->
m

<!-- b005707 | prose | pages [14] -->
m

<!-- b005708 | prose | pages [14] -->
m

<!-- b005709 | prose | pages [14] -->
m

<!-- b005710 | prose | pages [14] -->
m

<!-- b005711 | prose | pages [14] -->
m

<!-- b005712 | prose | pages [14] -->
m

<!-- b005713 | prose | pages [14] -->
m

<!-- b005714 | prose | pages [14] -->
m

<!-- b005715 | prose | pages [14] -->
m

<!-- b005716 | prose | pages [14] -->
m

<!-- b005717 | prose | pages [14] -->
m

<!-- b005718 | prose | pages [14] -->
m

<!-- b005719 | prose | pages [14] -->
m

<!-- b005720 | prose | pages [14] -->
m

<!-- b005721 | prose | pages [14] -->
m

<!-- b005722 | prose | pages [14] -->
m

<!-- b005723 | prose | pages [14] -->
m

<!-- b005724 | prose | pages [14] -->
m

<!-- b005725 | prose | pages [14] -->
m

<!-- b005726 | prose | pages [14] -->
m

<!-- b005727 | prose | pages [14] -->
m

<!-- b005728 | prose | pages [14] -->
m

<!-- b005729 | prose | pages [14] -->
m

<!-- b005730 | prose | pages [14] -->
m

<!-- b005731 | prose | pages [14] -->
m

<!-- b005732 | prose | pages [14] -->
m

<!-- b005733 | prose | pages [14] -->
m

<!-- b005734 | prose | pages [14] -->
m

<!-- b005735 | prose | pages [14] -->
m

<!-- b005736 | prose | pages [14] -->
m

<!-- b005737 | prose | pages [14] -->
m

<!-- b005738 | prose | pages [14] -->
m

<!-- b005739 | prose | pages [14] -->
m

<!-- b005740 | prose | pages [14] -->
m

<!-- b005741 | prose | pages [14] -->
m

<!-- b005742 | prose | pages [14] -->
m

<!-- b005743 | prose | pages [14] -->
m

<!-- b005744 | prose | pages [14] -->
m

<!-- b005745 | prose | pages [14] -->
m

<!-- b005746 | prose | pages [14] -->
m

<!-- b005747 | prose | pages [14] -->
m

<!-- b005748 | prose | pages [14] -->
m

<!-- b005749 | prose | pages [14] -->
m

<!-- b005750 | prose | pages [14] -->
m

<!-- b005751 | prose | pages [14] -->
m

<!-- b005752 | prose | pages [14] -->
m

<!-- b005753 | prose | pages [14] -->
m

<!-- b005754 | prose | pages [14] -->
m

<!-- b005755 | prose | pages [14] -->
m

<!-- b005756 | prose | pages [14] -->
m

<!-- b005757 | prose | pages [14] -->
m

<!-- b005758 | prose | pages [14] -->
m

<!-- b005759 | prose | pages [14] -->
m

<!-- b005760 | prose | pages [14] -->
m

<!-- b005761 | prose | pages [14] -->
m

<!-- b005762 | prose | pages [14] -->
m

<!-- b005763 | prose | pages [14] -->
m

<!-- b005764 | prose | pages [14] -->
m

<!-- b005765 | prose | pages [14] -->
m

<!-- b005766 | prose | pages [14] -->
m

<!-- b005767 | prose | pages [14] -->
m

<!-- b005768 | prose | pages [14] -->
m

<!-- b005769 | prose | pages [14] -->
m

<!-- b005770 | prose | pages [14] -->
m

<!-- b005771 | prose | pages [14] -->
m

<!-- b005772 | prose | pages [14] -->
m

<!-- b005773 | prose | pages [14] -->
m

<!-- b005774 | prose | pages [14] -->
m

<!-- b005775 | prose | pages [14] -->
m

<!-- b005776 | prose | pages [14] -->
m

<!-- b005777 | prose | pages [14] -->
m

<!-- b005778 | prose | pages [14] -->
m

<!-- b005779 | furniture | pages [14] -->
Page 14 of 25

<!-- b005780 | caption | pages [14] -->
Figure 9: Relationship Between Sports and Countries Winning First Medals

<!-- b005781 | prose | pages [14] -->
We found that certain sports such as Athletics, Taekwondo and Wrestling are more likely to be breakthrough areas for these countries. These disciplines typically have lower barriers to entry and a wider participation base than other traditional strengths, providing more opportunities for those countries that did not win.

<!-- b005782 | prose | pages [14] -->
Therefore, in our model, we assign higher weights to these projects to better reflect the importance of these projects among first-time award-winning countries. Such weighting assignments help our prediction model to capture the potential of these projects more accurately, thus improving the accuracy of the predictions.

<!-- b005783 | heading | pages [14] -->
3. Integrated prediction in conjunction with the Stacking model

<!-- b005784 | prose | pages [14] -->
Combining the above two features, we introduced them into the Stacking model in the previous section. We have combined the trends in the number of entries from each coun- try, the weighting of the events and the historical medal data in our model to produce the following predictions.

<!-- b005785 | prose | pages [14] -->
Based on the predictions of the Stacking model, the following five countries are con- sidered to be the most likely to win medals for the first time at the 2028 Olympics:

<!-- b005786 | caption | pages [14] -->
Figure 10: Countries Likely to Win Their First Medal in 2028 and Probabilities

<!-- b005787 | prose | pages [14] -->
关注数学模型

<!-- b005788 | furniture | pages [14] -->
2

<!-- b005789 | furniture | pages [14] -->
MATHmodels

<!-- b005790 | furniture | pages [14] -->
获取更多资讯

<!-- b005791 | furniture | pages [15] -->
Team # 2510862

<!-- b005792 | furniture | pages [15] -->
Page 15 of 25

<!-- b005793 | prose | pages [15] -->
7 Task 3:Exploration of the Relationship Between Olympic Events and Medal Wins

<!-- b005794 | prose | pages [15] -->
In the Olympic medal prediction model, the number and type of events is one of the key factors affecting medal allocation. We believe that the number of participants of a country in a particular event can better reflect the predictive power of that event on the number of medals won by that country, and the number of participants of each country in

<!-- b005795 | prose | pages [15] -->
微信公众号：数学模型

<!-- b005796 | prose | pages [15] -->
different events has been input into the model as a substitute for the number of events in the previous section. In order to further explore the relationship between the medals won by the events and the countries, a correlation between the number of entries in different events and the number of medals has been analysed. Finally, using the SHAP method- ology, it was possible to explain the importance of individual features of the model in predicting outcomes and to analyse which events had the greatest impact on the number of medals won by each country.

<!-- b005797 | prose | pages [15] -->
7.1 Explore the relationship between the events and how many medals countries earn

<!-- b005798 | prose | pages [15] -->
微信号：MATHmodels

<!-- b005799 | prose | pages [15] -->
We consider the number of participants from all countries in each event as the char- acteristics and the number of gold, silver, bronze and total medals as the target vari- ables. The Pearson Correlation Coefficient enables us to calculate the linear correlation between the number of participants and the number of medals, and then to determine which events are most closely related to the number of medals, and which events have a lesser impact on the distribution of medals.

<!-- b005800 | caption | pages [15] -->
Figure 11: Correlation Coefficients Between Different Sports and Medal Counts

<!-- b005801 | prose | pages [15] -->
m

<!-- b005802 | prose | pages [15] -->
m

<!-- b005803 | prose | pages [15] -->
m

<!-- b005804 | prose | pages [15] -->
m

<!-- b005805 | prose | pages [15] -->
m

<!-- b005806 | prose | pages [15] -->
m

<!-- b005807 | prose | pages [15] -->
m

<!-- b005808 | prose | pages [15] -->
m

<!-- b005809 | prose | pages [15] -->
m

<!-- b005810 | prose | pages [15] -->
m

<!-- b005811 | prose | pages [15] -->
m

<!-- b005812 | prose | pages [15] -->
m

<!-- b005813 | prose | pages [15] -->
m

<!-- b005814 | prose | pages [15] -->
m

<!-- b005815 | prose | pages [15] -->
m

<!-- b005816 | prose | pages [15] -->
m

<!-- b005817 | prose | pages [15] -->
m

<!-- b005818 | prose | pages [15] -->
m

<!-- b005819 | prose | pages [15] -->
m

<!-- b005820 | prose | pages [15] -->
m

<!-- b005821 | prose | pages [15] -->
m

<!-- b005822 | prose | pages [15] -->
m

<!-- b005823 | prose | pages [15] -->
m

<!-- b005824 | prose | pages [15] -->
m

<!-- b005825 | prose | pages [15] -->
m

<!-- b005826 | prose | pages [15] -->
m

<!-- b005827 | prose | pages [15] -->
m

<!-- b005828 | prose | pages [15] -->
m

<!-- b005829 | prose | pages [15] -->
m

<!-- b005830 | prose | pages [15] -->
m

<!-- b005831 | prose | pages [15] -->
m

<!-- b005832 | prose | pages [15] -->
m

<!-- b005833 | prose | pages [15] -->
m

<!-- b005834 | prose | pages [15] -->
m

<!-- b005835 | prose | pages [15] -->
m

<!-- b005836 | prose | pages [15] -->
m

<!-- b005837 | prose | pages [15] -->
m

<!-- b005838 | prose | pages [15] -->
m

<!-- b005839 | prose | pages [15] -->
m

<!-- b005840 | prose | pages [15] -->
m

<!-- b005841 | prose | pages [15] -->
m

<!-- b005842 | prose | pages [15] -->
m

<!-- b005843 | prose | pages [15] -->
m

<!-- b005844 | prose | pages [15] -->
m

<!-- b005845 | prose | pages [15] -->
m

<!-- b005846 | prose | pages [15] -->
m

<!-- b005847 | prose | pages [15] -->
m

<!-- b005848 | prose | pages [15] -->
m

<!-- b005849 | prose | pages [15] -->
m

<!-- b005850 | prose | pages [15] -->
m

<!-- b005851 | prose | pages [15] -->
m

<!-- b005852 | prose | pages [15] -->
m

<!-- b005853 | prose | pages [15] -->
m

<!-- b005854 | prose | pages [15] -->
m

<!-- b005855 | prose | pages [15] -->
m

<!-- b005856 | prose | pages [15] -->
m

<!-- b005857 | prose | pages [15] -->
m

<!-- b005858 | prose | pages [15] -->
m

<!-- b005859 | prose | pages [15] -->
m

<!-- b005860 | prose | pages [15] -->
m

<!-- b005861 | prose | pages [15] -->
m

<!-- b005862 | prose | pages [15] -->
m

<!-- b005863 | prose | pages [15] -->
m

<!-- b005864 | prose | pages [15] -->
m

<!-- b005865 | prose | pages [15] -->
m

<!-- b005866 | prose | pages [15] -->
m

<!-- b005867 | prose | pages [15] -->
m

<!-- b005868 | prose | pages [15] -->
m

<!-- b005869 | prose | pages [15] -->
m

<!-- b005870 | prose | pages [15] -->
m

<!-- b005871 | prose | pages [15] -->
m

<!-- b005872 | prose | pages [15] -->
m

<!-- b005873 | prose | pages [15] -->
m

<!-- b005874 | prose | pages [15] -->
m

<!-- b005875 | prose | pages [15] -->
m

<!-- b005876 | prose | pages [15] -->
m

<!-- b005877 | prose | pages [15] -->
m

<!-- b005878 | prose | pages [15] -->
m

<!-- b005879 | prose | pages [15] -->
m

<!-- b005880 | prose | pages [15] -->
m

<!-- b005881 | prose | pages [15] -->
m

<!-- b005882 | prose | pages [15] -->
m

<!-- b005883 | prose | pages [15] -->
m

<!-- b005884 | prose | pages [15] -->
m

<!-- b005885 | prose | pages [15] -->
m

<!-- b005886 | prose | pages [15] -->
m

<!-- b005887 | prose | pages [15] -->
m

<!-- b005888 | prose | pages [15] -->
m

<!-- b005889 | prose | pages [15] -->
m

<!-- b005890 | prose | pages [15] -->
m

<!-- b005891 | prose | pages [15] -->
m

<!-- b005892 | prose | pages [15] -->
m

<!-- b005893 | prose | pages [15] -->
m

<!-- b005894 | prose | pages [15] -->
m

<!-- b005895 | prose | pages [15] -->
m

<!-- b005896 | prose | pages [15] -->
m

<!-- b005897 | prose | pages [15] -->
m

<!-- b005898 | prose | pages [15] -->
m

<!-- b005899 | prose | pages [15] -->
m

<!-- b005900 | prose | pages [15] -->
m

<!-- b005901 | prose | pages [15] -->
m

<!-- b005902 | prose | pages [15] -->
m

<!-- b005903 | prose | pages [15] -->
m

<!-- b005904 | prose | pages [15] -->
m

<!-- b005905 | prose | pages [15] -->
m

<!-- b005906 | prose | pages [15] -->
m

<!-- b005907 | prose | pages [15] -->
m

<!-- b005908 | prose | pages [15] -->
m

<!-- b005909 | prose | pages [15] -->
m

<!-- b005910 | prose | pages [15] -->
m

<!-- b005911 | prose | pages [15] -->
m

<!-- b005912 | prose | pages [15] -->
m

<!-- b005913 | prose | pages [15] -->
m

<!-- b005914 | prose | pages [15] -->
m

<!-- b005915 | prose | pages [15] -->
m

<!-- b005916 | prose | pages [15] -->
m

<!-- b005917 | prose | pages [15] -->
m

<!-- b005918 | prose | pages [15] -->
m

<!-- b005919 | prose | pages [15] -->
m

<!-- b005920 | prose | pages [15] -->
m

<!-- b005921 | prose | pages [15] -->
m

<!-- b005922 | prose | pages [15] -->
m

<!-- b005923 | prose | pages [15] -->
m

<!-- b005924 | prose | pages [15] -->
m

<!-- b005925 | prose | pages [15] -->
m

<!-- b005926 | prose | pages [15] -->
m

<!-- b005927 | prose | pages [15] -->
m

<!-- b005928 | prose | pages [15] -->
m

<!-- b005929 | prose | pages [15] -->
m

<!-- b005930 | prose | pages [15] -->
m

<!-- b005931 | prose | pages [15] -->
m

<!-- b005932 | prose | pages [15] -->
m

<!-- b005933 | prose | pages [15] -->
m

<!-- b005934 | prose | pages [15] -->
m

<!-- b005935 | prose | pages [15] -->
m

<!-- b005936 | prose | pages [15] -->
m

<!-- b005937 | prose | pages [15] -->
m

<!-- b005938 | prose | pages [15] -->
m

<!-- b005939 | prose | pages [15] -->
m

<!-- b005940 | prose | pages [15] -->
m

<!-- b005941 | prose | pages [15] -->
m

<!-- b005942 | prose | pages [15] -->
m

<!-- b005943 | prose | pages [15] -->
m

<!-- b005944 | prose | pages [15] -->
m

<!-- b005945 | prose | pages [15] -->
m

<!-- b005946 | prose | pages [15] -->
m

<!-- b005947 | prose | pages [15] -->
m

<!-- b005948 | prose | pages [15] -->
m

<!-- b005949 | prose | pages [15] -->
m

<!-- b005950 | prose | pages [15] -->
m

<!-- b005951 | prose | pages [15] -->
m

<!-- b005952 | prose | pages [15] -->
m

<!-- b005953 | prose | pages [15] -->
m

<!-- b005954 | prose | pages [15] -->
m

<!-- b005955 | prose | pages [15] -->
m

<!-- b005956 | prose | pages [15] -->
m

<!-- b005957 | prose | pages [15] -->
m

<!-- b005958 | prose | pages [15] -->
m

<!-- b005959 | prose | pages [15] -->
m

<!-- b005960 | prose | pages [15] -->
m

<!-- b005961 | prose | pages [15] -->
m

<!-- b005962 | prose | pages [15] -->
m

<!-- b005963 | prose | pages [15] -->
m

<!-- b005964 | prose | pages [15] -->
m

<!-- b005965 | prose | pages [15] -->
m

<!-- b005966 | prose | pages [15] -->
m

<!-- b005967 | prose | pages [15] -->
m

<!-- b005968 | prose | pages [15] -->
m

<!-- b005969 | prose | pages [15] -->
m

<!-- b005970 | prose | pages [15] -->
m

<!-- b005971 | prose | pages [15] -->
m

<!-- b005972 | prose | pages [15] -->
m

<!-- b005973 | prose | pages [15] -->
m

<!-- b005974 | prose | pages [15] -->
m

<!-- b005975 | prose | pages [15] -->
m

<!-- b005976 | prose | pages [15] -->
m

<!-- b005977 | prose | pages [15] -->
m

<!-- b005978 | prose | pages [15] -->
m

<!-- b005979 | prose | pages [15] -->
m

<!-- b005980 | prose | pages [15] -->
m

<!-- b005981 | prose | pages [15] -->
m

<!-- b005982 | prose | pages [15] -->
m

<!-- b005983 | prose | pages [15] -->
m

<!-- b005984 | prose | pages [15] -->
m

<!-- b005985 | prose | pages [15] -->
m

<!-- b005986 | prose | pages [15] -->
m

<!-- b005987 | prose | pages [15] -->
m

<!-- b005988 | prose | pages [15] -->
m

<!-- b005989 | prose | pages [15] -->
m

<!-- b005990 | prose | pages [15] -->
m

<!-- b005991 | prose | pages [15] -->
m

<!-- b005992 | prose | pages [15] -->
m

<!-- b005993 | prose | pages [15] -->
m

<!-- b005994 | prose | pages [15] -->
m

<!-- b005995 | prose | pages [15] -->
m

<!-- b005996 | prose | pages [15] -->
m

<!-- b005997 | prose | pages [15] -->
m

<!-- b005998 | prose | pages [15] -->
m

<!-- b005999 | prose | pages [15] -->
m

<!-- b006000 | prose | pages [15] -->
m

<!-- b006001 | prose | pages [15] -->
m

<!-- b006002 | prose | pages [15] -->
m

<!-- b006003 | prose | pages [15] -->
m

<!-- b006004 | prose | pages [15] -->
m

<!-- b006005 | prose | pages [15] -->
m

<!-- b006006 | prose | pages [15] -->
m

<!-- b006007 | prose | pages [15] -->
m

<!-- b006008 | prose | pages [15] -->
m

<!-- b006009 | prose | pages [15] -->
m

<!-- b006010 | prose | pages [15] -->
m

<!-- b006011 | prose | pages [15] -->
m

<!-- b006012 | prose | pages [15] -->
m

<!-- b006013 | prose | pages [15] -->
m

<!-- b006014 | prose | pages [15] -->
m

<!-- b006015 | prose | pages [15] -->
m

<!-- b006016 | prose | pages [15] -->
m

<!-- b006017 | prose | pages [15] -->
m

<!-- b006018 | prose | pages [15] -->
m

<!-- b006019 | prose | pages [15] -->
m

<!-- b006020 | prose | pages [15] -->
m

<!-- b006021 | prose | pages [15] -->
m

<!-- b006022 | prose | pages [15] -->
m

<!-- b006023 | prose | pages [15] -->
m

<!-- b006024 | prose | pages [15] -->
m

<!-- b006025 | prose | pages [15] -->
m

<!-- b006026 | prose | pages [15] -->
m

<!-- b006027 | prose | pages [15] -->
m

<!-- b006028 | prose | pages [15] -->
m

<!-- b006029 | prose | pages [15] -->
m

<!-- b006030 | prose | pages [15] -->
m

<!-- b006031 | prose | pages [15] -->
m

<!-- b006032 | prose | pages [15] -->
m

<!-- b006033 | prose | pages [15] -->
m

<!-- b006034 | prose | pages [15] -->
m

<!-- b006035 | prose | pages [15] -->
m

<!-- b006036 | prose | pages [15] -->
m

<!-- b006037 | prose | pages [15] -->
m

<!-- b006038 | prose | pages [15] -->
m

<!-- b006039 | prose | pages [15] -->
m

<!-- b006040 | prose | pages [15] -->
m

<!-- b006041 | prose | pages [15] -->
m

<!-- b006042 | prose | pages [15] -->
m

<!-- b006043 | prose | pages [15] -->
m

<!-- b006044 | prose | pages [15] -->
m

<!-- b006045 | prose | pages [15] -->
m

<!-- b006046 | prose | pages [15] -->
m

<!-- b006047 | prose | pages [15] -->
m

<!-- b006048 | prose | pages [15] -->
m

<!-- b006049 | prose | pages [15] -->
m

<!-- b006050 | prose | pages [15] -->
m

<!-- b006051 | prose | pages [15] -->
m

<!-- b006052 | prose | pages [15] -->
m

<!-- b006053 | prose | pages [15] -->
m

<!-- b006054 | prose | pages [15] -->
m

<!-- b006055 | prose | pages [15] -->
m

<!-- b006056 | prose | pages [15] -->
m

<!-- b006057 | prose | pages [15] -->
m

<!-- b006058 | prose | pages [15] -->
m

<!-- b006059 | prose | pages [15] -->
m

<!-- b006060 | prose | pages [15] -->
m

<!-- b006061 | prose | pages [15] -->
m

<!-- b006062 | prose | pages [15] -->
m

<!-- b006063 | prose | pages [15] -->
m

<!-- b006064 | prose | pages [15] -->
m

<!-- b006065 | prose | pages [15] -->
m

<!-- b006066 | prose | pages [15] -->
m

<!-- b006067 | prose | pages [15] -->
m

<!-- b006068 | prose | pages [15] -->
m

<!-- b006069 | prose | pages [15] -->
m

<!-- b006070 | prose | pages [15] -->
m

<!-- b006071 | prose | pages [15] -->
m

<!-- b006072 | prose | pages [15] -->
m

<!-- b006073 | prose | pages [15] -->
m

<!-- b006074 | prose | pages [15] -->
m

<!-- b006075 | prose | pages [15] -->
m

<!-- b006076 | prose | pages [15] -->
m

<!-- b006077 | prose | pages [15] -->
m

<!-- b006078 | prose | pages [15] -->
m

<!-- b006079 | prose | pages [15] -->
m

<!-- b006080 | prose | pages [15] -->
m

<!-- b006081 | prose | pages [15] -->
m

<!-- b006082 | prose | pages [15] -->
m

<!-- b006083 | prose | pages [15] -->
m

<!-- b006084 | prose | pages [15] -->
m

<!-- b006085 | furniture | pages [15] -->
m

<!-- b006086 | furniture | pages [15] -->
m

<!-- b006087 | furniture | pages [15] -->
m

<!-- b006088 | furniture | pages [15] -->
m

<!-- b006089 | furniture | pages [15] -->
m

<!-- b006090 | furniture | pages [15] -->
m

<!-- b006091 | furniture | pages [15] -->
m

<!-- b006092 | furniture | pages [15] -->
m

<!-- b006093 | furniture | pages [15] -->
m

<!-- b006094 | furniture | pages [15] -->
m

<!-- b006095 | furniture | pages [15] -->
m

<!-- b006096 | furniture | pages [15] -->
m

<!-- b006097 | furniture | pages [15] -->
m

<!-- b006098 | furniture | pages [15] -->
m

<!-- b006099 | furniture | pages [15] -->
m

<!-- b006100 | furniture | pages [15] -->
m

<!-- b006101 | furniture | pages [15] -->
m

<!-- b006102 | furniture | pages [15] -->
m

<!-- b006103 | furniture | pages [15] -->
m

<!-- b006104 | furniture | pages [15] -->
m

<!-- b006105 | furniture | pages [15] -->
m

<!-- b006106 | furniture | pages [15] -->
m

<!-- b006107 | furniture | pages [15] -->
m

<!-- b006108 | furniture | pages [15] -->
m

<!-- b006109 | furniture | pages [15] -->
m

<!-- b006110 | furniture | pages [15] -->
m

<!-- b006111 | furniture | pages [15] -->
m

<!-- b006112 | furniture | pages [15] -->
m

<!-- b006113 | furniture | pages [15] -->
m

<!-- b006114 | furniture | pages [15] -->
m

<!-- b006115 | furniture | pages [15] -->
m

<!-- b006116 | furniture | pages [15] -->
m

<!-- b006117 | furniture | pages [15] -->
m

<!-- b006118 | furniture | pages [15] -->
m

<!-- b006119 | furniture | pages [15] -->
m

<!-- b006120 | furniture | pages [15] -->
m

<!-- b006121 | furniture | pages [15] -->
m

<!-- b006122 | furniture | pages [15] -->
m

<!-- b006123 | furniture | pages [15] -->
m

<!-- b006124 | furniture | pages [15] -->
m

<!-- b006125 | furniture | pages [15] -->
m

<!-- b006126 | furniture | pages [15] -->
m

<!-- b006127 | furniture | pages [15] -->
m

<!-- b006128 | furniture | pages [15] -->
m

<!-- b006129 | furniture | pages [15] -->
m

<!-- b006130 | furniture | pages [15] -->
m

<!-- b006131 | furniture | pages [15] -->
m

<!-- b006132 | furniture | pages [15] -->
m

<!-- b006133 | furniture | pages [15] -->
m

<!-- b006134 | furniture | pages [15] -->
m

<!-- b006135 | furniture | pages [15] -->
m

<!-- b006136 | furniture | pages [15] -->
m

<!-- b006137 | furniture | pages [15] -->
m

<!-- b006138 | furniture | pages [15] -->
m

<!-- b006139 | furniture | pages [15] -->
m

<!-- b006140 | furniture | pages [15] -->
m

<!-- b006141 | furniture | pages [15] -->
m

<!-- b006142 | furniture | pages [15] -->
m

<!-- b006143 | furniture | pages [15] -->
m

<!-- b006144 | furniture | pages [15] -->
m

<!-- b006145 | furniture | pages [15] -->
m

<!-- b006146 | furniture | pages [15] -->
m

<!-- b006147 | furniture | pages [15] -->
m

<!-- b006148 | furniture | pages [15] -->
m

<!-- b006149 | furniture | pages [15] -->
m

<!-- b006150 | furniture | pages [15] -->
m

<!-- b006151 | furniture | pages [15] -->
m

<!-- b006152 | furniture | pages [15] -->
m

<!-- b006153 | furniture | pages [15] -->
m

<!-- b006154 | furniture | pages [15] -->
m

<!-- b006155 | furniture | pages [15] -->
m

<!-- b006156 | furniture | pages [15] -->
m

<!-- b006157 | furniture | pages [15] -->
m

<!-- b006158 | furniture | pages [15] -->
m

<!-- b006159 | furniture | pages [15] -->
m

<!-- b006160 | furniture | pages [15] -->
m

<!-- b006161 | furniture | pages [15] -->
m

<!-- b006162 | furniture | pages [15] -->
m

<!-- b006163 | furniture | pages [15] -->
m

<!-- b006164 | furniture | pages [15] -->
m

<!-- b006165 | furniture | pages [15] -->
m

<!-- b006166 | furniture | pages [15] -->
m

<!-- b006167 | furniture | pages [15] -->
m

<!-- b006168 | furniture | pages [15] -->
m

<!-- b006169 | furniture | pages [15] -->
m

<!-- b006170 | furniture | pages [15] -->
m

<!-- b006171 | furniture | pages [15] -->
m

<!-- b006172 | furniture | pages [15] -->
m

<!-- b006173 | furniture | pages [15] -->
m

<!-- b006174 | furniture | pages [15] -->
m

<!-- b006175 | furniture | pages [15] -->
m

<!-- b006176 | furniture | pages [15] -->
m

<!-- b006177 | furniture | pages [15] -->
m

<!-- b006178 | furniture | pages [15] -->
m

<!-- b006179 | furniture | pages [15] -->
m

<!-- b006180 | furniture | pages [15] -->
m

<!-- b006181 | furniture | pages [15] -->
m

<!-- b006182 | furniture | pages [15] -->
m

<!-- b006183 | furniture | pages [15] -->
m

<!-- b006184 | furniture | pages [15] -->
m

<!-- b006185 | furniture | pages [15] -->
m

<!-- b006186 | furniture | pages [15] -->
m

<!-- b006187 | furniture | pages [15] -->
m

<!-- b006188 | furniture | pages [15] -->
m

<!-- b006189 | furniture | pages [15] -->
m

<!-- b006190 | furniture | pages [15] -->
m

<!-- b006191 | furniture | pages [15] -->
m

<!-- b006192 | furniture | pages [15] -->
m

<!-- b006193 | furniture | pages [15] -->
m

<!-- b006194 | furniture | pages [15] -->
m

<!-- b006195 | furniture | pages [15] -->
m

<!-- b006196 | furniture | pages [15] -->
m

<!-- b006197 | furniture | pages [15] -->
m

<!-- b006198 | furniture | pages [15] -->
m

<!-- b006199 | furniture | pages [15] -->
m

<!-- b006200 | furniture | pages [15] -->
m

<!-- b006201 | furniture | pages [15] -->
m

<!-- b006202 | furniture | pages [15] -->
m

<!-- b006203 | furniture | pages [15] -->
m

<!-- b006204 | furniture | pages [15] -->
m

<!-- b006205 | furniture | pages [15] -->
m

<!-- b006206 | furniture | pages [15] -->
m

<!-- b006207 | furniture | pages [15] -->
m

<!-- b006208 | furniture | pages [15] -->
m

<!-- b006209 | furniture | pages [15] -->
m

<!-- b006210 | furniture | pages [15] -->
m

<!-- b006211 | furniture | pages [15] -->
m

<!-- b006212 | furniture | pages [15] -->
m

<!-- b006213 | furniture | pages [15] -->
m

<!-- b006214 | furniture | pages [15] -->
m

<!-- b006215 | furniture | pages [15] -->
m

<!-- b006216 | furniture | pages [15] -->
m

<!-- b006217 | furniture | pages [15] -->
m

<!-- b006218 | furniture | pages [15] -->
m

<!-- b006219 | furniture | pages [15] -->
m

<!-- b006220 | furniture | pages [15] -->
m

<!-- b006221 | furniture | pages [15] -->
m

<!-- b006222 | furniture | pages [15] -->
m

<!-- b006223 | furniture | pages [15] -->
m

<!-- b006224 | furniture | pages [15] -->
m

<!-- b006225 | furniture | pages [15] -->
m

<!-- b006226 | furniture | pages [15] -->
m

<!-- b006227 | furniture | pages [15] -->
m

<!-- b006228 | furniture | pages [15] -->
m

<!-- b006229 | furniture | pages [15] -->
m

<!-- b006230 | furniture | pages [15] -->
m

<!-- b006231 | furniture | pages [15] -->
m

<!-- b006232 | furniture | pages [15] -->
m

<!-- b006233 | furniture | pages [15] -->
m

<!-- b006234 | furniture | pages [15] -->
m

<!-- b006235 | furniture | pages [15] -->
m

<!-- b006236 | furniture | pages [15] -->
m

<!-- b006237 | furniture | pages [15] -->
m

<!-- b006238 | furniture | pages [15] -->
m

<!-- b006239 | furniture | pages [15] -->
m

<!-- b006240 | furniture | pages [15] -->
m

<!-- b006241 | furniture | pages [15] -->
m

<!-- b006242 | furniture | pages [15] -->
m

<!-- b006243 | furniture | pages [15] -->
m

<!-- b006244 | furniture | pages [15] -->
m

<!-- b006245 | furniture | pages [15] -->
m

<!-- b006246 | furniture | pages [15] -->
m

<!-- b006247 | furniture | pages [15] -->
m

<!-- b006248 | furniture | pages [15] -->
m

<!-- b006249 | furniture | pages [15] -->
m

<!-- b006250 | furniture | pages [15] -->
m

<!-- b006251 | furniture | pages [15] -->
m

<!-- b006252 | furniture | pages [15] -->
m

<!-- b006253 | furniture | pages [15] -->
m

<!-- b006254 | furniture | pages [15] -->
m

<!-- b006255 | furniture | pages [15] -->
m

<!-- b006256 | furniture | pages [15] -->
m

<!-- b006257 | furniture | pages [15] -->
m

<!-- b006258 | furniture | pages [15] -->
m

<!-- b006259 | furniture | pages [15] -->
m

<!-- b006260 | furniture | pages [15] -->
m

<!-- b006261 | furniture | pages [15] -->
m

<!-- b006262 | furniture | pages [15] -->
m

<!-- b006263 | furniture | pages [15] -->
m

<!-- b006264 | furniture | pages [15] -->
m

<!-- b006265 | furniture | pages [15] -->
m

<!-- b006266 | furniture | pages [15] -->
m

<!-- b006267 | furniture | pages [15] -->
m

<!-- b006268 | furniture | pages [15] -->
m

<!-- b006269 | furniture | pages [15] -->
m

<!-- b006270 | furniture | pages [15] -->
m

<!-- b006271 | furniture | pages [15] -->
m

<!-- b006272 | furniture | pages [15] -->
m

<!-- b006273 | furniture | pages [15] -->
m

<!-- b006274 | furniture | pages [15] -->
m

<!-- b006275 | furniture | pages [15] -->
m

<!-- b006276 | furniture | pages [15] -->
m

<!-- b006277 | furniture | pages [15] -->
m

<!-- b006278 | furniture | pages [15] -->
m

<!-- b006279 | furniture | pages [15] -->
m

<!-- b006280 | furniture | pages [15] -->
m

<!-- b006281 | furniture | pages [15] -->
m

<!-- b006282 | furniture | pages [15] -->
m

<!-- b006283 | furniture | pages [15] -->
m

<!-- b006284 | furniture | pages [15] -->
m

<!-- b006285 | furniture | pages [15] -->
m

<!-- b006286 | furniture | pages [15] -->
m

<!-- b006287 | furniture | pages [15] -->
m

<!-- b006288 | furniture | pages [15] -->
m

<!-- b006289 | furniture | pages [15] -->
m

<!-- b006290 | furniture | pages [15] -->
m

<!-- b006291 | furniture | pages [15] -->
m

<!-- b006292 | furniture | pages [15] -->
m

<!-- b006293 | furniture | pages [15] -->
m

<!-- b006294 | furniture | pages [15] -->
m

<!-- b006295 | furniture | pages [15] -->
m

<!-- b006296 | furniture | pages [15] -->
m

<!-- b006297 | furniture | pages [15] -->
m

<!-- b006298 | furniture | pages [15] -->
m

<!-- b006299 | furniture | pages [15] -->
m

<!-- b006300 | furniture | pages [15] -->
m

<!-- b006301 | furniture | pages [15] -->
m

<!-- b006302 | furniture | pages [15] -->
m

<!-- b006303 | furniture | pages [15] -->
m

<!-- b006304 | furniture | pages [15] -->
m

<!-- b006305 | furniture | pages [15] -->
m

<!-- b006306 | furniture | pages [15] -->
m

<!-- b006307 | furniture | pages [15] -->
m

<!-- b006308 | furniture | pages [15] -->
m

<!-- b006309 | furniture | pages [15] -->
m

<!-- b006310 | furniture | pages [15] -->
m

<!-- b006311 | furniture | pages [15] -->
m

<!-- b006312 | furniture | pages [15] -->
m

<!-- b006313 | furniture | pages [15] -->
m

<!-- b006314 | furniture | pages [15] -->
m

<!-- b006315 | furniture | pages [15] -->
m

<!-- b006316 | furniture | pages [15] -->
m

<!-- b006317 | furniture | pages [15] -->
m

<!-- b006318 | furniture | pages [15] -->
m

<!-- b006319 | furniture | pages [15] -->
m

<!-- b006320 | furniture | pages [15] -->
m

<!-- b006321 | furniture | pages [15] -->
m

<!-- b006322 | furniture | pages [15] -->
m

<!-- b006323 | furniture | pages [15] -->
m

<!-- b006324 | furniture | pages [15] -->
m

<!-- b006325 | furniture | pages [15] -->
m

<!-- b006326 | furniture | pages [15] -->
m

<!-- b006327 | furniture | pages [15] -->
m

<!-- b006328 | furniture | pages [15] -->
m

<!-- b006329 | furniture | pages [15] -->
m

<!-- b006330 | furniture | pages [15] -->
m

<!-- b006331 | furniture | pages [15] -->
m

<!-- b006332 | furniture | pages [15] -->
m

<!-- b006333 | furniture | pages [15] -->
m

<!-- b006334 | furniture | pages [15] -->
m

<!-- b006335 | furniture | pages [15] -->
m

<!-- b006336 | furniture | pages [15] -->
m

<!-- b006337 | furniture | pages [15] -->
m

<!-- b006338 | furniture | pages [15] -->
m

<!-- b006339 | furniture | pages [15] -->
m

<!-- b006340 | furniture | pages [15] -->
m

<!-- b006341 | furniture | pages [15] -->
m

<!-- b006342 | furniture | pages [15] -->
m

<!-- b006343 | furniture | pages [15] -->
m

<!-- b006344 | furniture | pages [15] -->
m

<!-- b006345 | furniture | pages [15] -->
m

<!-- b006346 | furniture | pages [15] -->
m

<!-- b006347 | furniture | pages [15] -->
m

<!-- b006348 | furniture | pages [15] -->
m

<!-- b006349 | furniture | pages [15] -->
m

<!-- b006350 | furniture | pages [15] -->
m

<!-- b006351 | furniture | pages [15] -->
m

<!-- b006352 | furniture | pages [15] -->
m

<!-- b006353 | furniture | pages [15] -->
m

<!-- b006354 | furniture | pages [15] -->
m

<!-- b006355 | furniture | pages [15] -->
m

<!-- b006356 | furniture | pages [15] -->
m

<!-- b006357 | furniture | pages [15] -->
m

<!-- b006358 | furniture | pages [15] -->
m

<!-- b006359 | furniture | pages [15] -->
m

<!-- b006360 | furniture | pages [15] -->
m

<!-- b006361 | furniture | pages [15] -->
m

<!-- b006362 | furniture | pages [15] -->
m

<!-- b006363 | furniture | pages [15] -->
m

<!-- b006364 | furniture | pages [15] -->
m

<!-- b006365 | furniture | pages [15] -->
m

<!-- b006366 | furniture | pages [15] -->
m

<!-- b006367 | furniture | pages [15] -->
m

<!-- b006368 | furniture | pages [15] -->
m

<!-- b006369 | furniture | pages [15] -->
m

<!-- b006370 | furniture | pages [15] -->
m

<!-- b006371 | furniture | pages [15] -->
m

<!-- b006372 | furniture | pages [15] -->
m

<!-- b006373 | furniture | pages [15] -->
m

<!-- b006374 | furniture | pages [15] -->
m

<!-- b006375 | furniture | pages [15] -->
m

<!-- b006376 | furniture | pages [15] -->
m

<!-- b006377 | furniture | pages [15] -->
m

<!-- b006378 | furniture | pages [15] -->
m

<!-- b006379 | furniture | pages [15] -->
m

<!-- b006380 | furniture | pages [15] -->
m

<!-- b006381 | furniture | pages [15] -->
m

<!-- b006382 | furniture | pages [15] -->
m

<!-- b006383 | furniture | pages [15] -->
m

<!-- b006384 | furniture | pages [15] -->
m

<!-- b006385 | furniture | pages [15] -->
m

<!-- b006386 | furniture | pages [15] -->
m

<!-- b006387 | furniture | pages [15] -->
m

<!-- b006388 | furniture | pages [15] -->
m

<!-- b006389 | furniture | pages [15] -->
m

<!-- b006390 | furniture | pages [15] -->
m

<!-- b006391 | furniture | pages [15] -->
m

<!-- b006392 | furniture | pages [15] -->
m

<!-- b006393 | furniture | pages [15] -->
m

<!-- b006394 | furniture | pages [15] -->
m

<!-- b006395 | furniture | pages [15] -->
m

<!-- b006396 | furniture | pages [15] -->
m

<!-- b006397 | furniture | pages [15] -->
m

<!-- b006398 | furniture | pages [15] -->
m

<!-- b006399 | furniture | pages [15] -->
m

<!-- b006400 | furniture | pages [15] -->
m

<!-- b006401 | furniture | pages [15] -->
m

<!-- b006402 | furniture | pages [15] -->
m

<!-- b006403 | furniture | pages [15] -->
m

<!-- b006404 | furniture | pages [15] -->
m

<!-- b006405 | furniture | pages [15] -->
m

<!-- b006406 | furniture | pages [15] -->
m

<!-- b006407 | furniture | pages [15] -->
m

<!-- b006408 | furniture | pages [15] -->
m

<!-- b006409 | furniture | pages [15] -->
m

<!-- b006410 | furniture | pages [15] -->
m

<!-- b006411 | furniture | pages [15] -->
m

<!-- b006412 | furniture | pages [15] -->
m

<!-- b006413 | furniture | pages [15] -->
m

<!-- b006414 | furniture | pages [15] -->
m

<!-- b006415 | furniture | pages [15] -->
m

<!-- b006416 | furniture | pages [15] -->
m

<!-- b006417 | furniture | pages [15] -->
m

<!-- b006418 | furniture | pages [15] -->
m

<!-- b006419 | furniture | pages [15] -->
m

<!-- b006420 | furniture | pages [15] -->
m

<!-- b006421 | furniture | pages [15] -->
m

<!-- b006422 | furniture | pages [15] -->
m

<!-- b006423 | furniture | pages [15] -->
m

<!-- b006424 | furniture | pages [15] -->
m

<!-- b006425 | furniture | pages [15] -->
m

<!-- b006426 | furniture | pages [15] -->
m

<!-- b006427 | furniture | pages [15] -->
m

<!-- b006428 | furniture | pages [15] -->
m

<!-- b006429 | furniture | pages [15] -->
m

<!-- b006430 | furniture | pages [15] -->
m

<!-- b006431 | furniture | pages [15] -->
m

<!-- b006432 | furniture | pages [15] -->
m

<!-- b006433 | furniture | pages [15] -->
m

<!-- b006434 | furniture | pages [15] -->
m

<!-- b006435 | furniture | pages [15] -->
m

<!-- b006436 | furniture | pages [15] -->
m

<!-- b006437 | furniture | pages [15] -->
m

<!-- b006438 | furniture | pages [15] -->
m

<!-- b006439 | furniture | pages [15] -->
m

<!-- b006440 | furniture | pages [15] -->
m

<!-- b006441 | furniture | pages [15] -->
m

<!-- b006442 | furniture | pages [15] -->
m

<!-- b006443 | furniture | pages [15] -->
m

<!-- b006444 | furniture | pages [15] -->
m

<!-- b006445 | furniture | pages [15] -->
m

<!-- b006446 | furniture | pages [15] -->
m

<!-- b006447 | furniture | pages [15] -->
m

<!-- b006448 | furniture | pages [15] -->
m

<!-- b006449 | furniture | pages [15] -->
m

<!-- b006450 | furniture | pages [15] -->
m

<!-- b006451 | furniture | pages [15] -->
m

<!-- b006452 | furniture | pages [15] -->
m

<!-- b006453 | furniture | pages [15] -->
m

<!-- b006454 | furniture | pages [15] -->
m

<!-- b006455 | furniture | pages [15] -->
m

<!-- b006456 | furniture | pages [15] -->
m

<!-- b006457 | furniture | pages [15] -->
m

<!-- b006458 | furniture | pages [15] -->
m

<!-- b006459 | furniture | pages [15] -->
m

<!-- b006460 | furniture | pages [15] -->
m

<!-- b006461 | furniture | pages [15] -->
m

<!-- b006462 | furniture | pages [15] -->
m

<!-- b006463 | furniture | pages [15] -->
m

<!-- b006464 | furniture | pages [15] -->
m

<!-- b006465 | furniture | pages [15] -->
m

<!-- b006466 | furniture | pages [15] -->
m

<!-- b006467 | furniture | pages [15] -->
m

<!-- b006468 | furniture | pages [15] -->
m

<!-- b006469 | furniture | pages [15] -->
m

<!-- b006470 | furniture | pages [15] -->
m

<!-- b006471 | furniture | pages [15] -->
m

<!-- b006472 | furniture | pages [15] -->
m

<!-- b006473 | furniture | pages [15] -->
m

<!-- b006474 | furniture | pages [15] -->
m

<!-- b006475 | furniture | pages [15] -->
m

<!-- b006476 | furniture | pages [15] -->
m

<!-- b006477 | furniture | pages [15] -->
m

<!-- b006478 | furniture | pages [15] -->
m

<!-- b006479 | furniture | pages [15] -->
m

<!-- b006480 | furniture | pages [15] -->
m

<!-- b006481 | furniture | pages [15] -->
m

<!-- b006482 | furniture | pages [15] -->
m

<!-- b006483 | furniture | pages [15] -->
m

<!-- b006484 | furniture | pages [15] -->
m

<!-- b006485 | furniture | pages [15] -->
m

<!-- b006486 | furniture | pages [15] -->
m

<!-- b006487 | furniture | pages [15] -->
m

<!-- b006488 | furniture | pages [17] -->
Team # 2510862

<!-- b006489 | furniture | pages [17] -->
Page 17 of 25

<!-- b006490 | prose | pages [17] -->
• Averaging over all feature combinations:

<!-- b006491 | prose | pages [17] -->
To obtain the Shapley value of a feature xj, we need to sum over all possible fea-

<!-- b006492 | prose | pages [17] -->
微信公众号：数学模型

<!-- b006493 | prose | pages [17] -->
ture combinations S and calculate their average marginal contribution. The final Shapley value is the weighted average of the marginal contributions of all combina- tions:Equation 12

<!-- b006494 | prose | pages [17] -->
X

<!-- b006495 | prose | pages [17] -->
|S|! (|N| −|S| −1)!

<!-- b006496 | prose | pages [17] -->
(12) [f(S ∪{j}) −f(S)]

<!-- b006497 | prose | pages [17] -->
ϕj(f) =

<!-- b006498 | prose | pages [17] -->
|N|!

<!-- b006499 | prose | pages [17] -->
S⊆N\{j}

<!-- b006500 | prose | pages [17] -->
Where: ϕj(f) is the Shapley value of the feature xj, i.e. the contribution of the feature to the model prediction; N is the collection of all features xj.

<!-- b006501 | prose | pages [17] -->
Through SHAP, we can quantify the contribution of each sport to national medal fore- casts. Larger SHAP values indicate that the sport has a greater impact on medal forecasts,

<!-- b006502 | prose | pages [17] -->
微信号：MATHmodels

<!-- b006503 | prose | pages [17] -->
while smaller SHAP values indicate that the sport has a lesser impact on medal forecasts.

<!-- b006504 | caption | pages [17] -->
Figure 13: Top 10 SHAP Values for Different Sports in USA, CHN and AUS

<!-- b006505 | prose | pages [17] -->
The SHAP values of gold, silver and bronze medals of different countries are analysed separately. In the case of the USA, for example, the sports that contribute the most to the number of medals are track and field, which is much higher than the contribution of other sports, while the sports that contribute the most to China’s medal forecasts are shooting, track and field, etc., and those that contribute the most to Australia’s medal forecasts are swimming, cycling and rowing, etc.

<!-- b006506 | furniture | pages [18] -->
Team # 2510862

<!-- b006507 | furniture | pages [18] -->
Page 18 of 25

<!-- b006508 | prose | pages [18] -->
Impact of Host Country’s Event Selection on medal 7.3

<!-- b006509 | prose | pages [18] -->
Through the collection of information, we have learnt that the introduction of new competitive sports at the 2028 Los Angeles Olympics, namely baseball/softball, cricket, flag football, stick tennis and squash, will impact on the host country, the United States, in a number of ways in terms of its overall medal performance and overall Olympic strategy.

<!-- b006510 | prose | pages [18] -->
By analysing the shap values of each US sport to its medal count, it was found that rugby has a high contribution to the US medal count (9th out of all sports to the gold list, 8th to the silver list, and 6th to the bronze list), and that the US has a strong tradition of rugby-related sports, so the addition of flag rugby may bring more medals to the US. Similarly, the United States, as the originator of stick tennis, will likely win more medals in this sport.

<!-- b006511 | prose | pages [18] -->
The IOC mentioned that the selection of the five new sports is in keeping with the American sporting culture, showcasing iconic American sports to the world while bring- ing international sports to the United States. As a host country, choosing sports with tra- ditional strengths along with those that are highly compatible with the country’s sporting culture helps to create a cultural identity, further inspire athletes to perform and increase international competitiveness and influence.

<!-- b006512 | prose | pages [18] -->
Task 4: Analysis of the "Great Coach" Effect and Its Im- 8 pact on Medals’ Performance

<!-- b006513 | prose | pages [18] -->
The effect contributes to medal counts 8.1

<!-- b006514 | prose | pages [18] -->
In major international events like the Olympics, coaches play a critical role not only in strategy and technique but also in psychological support and team coordination. The "great coach effect" suggests that the addition of exceptional coaches can significantly enhance a nation’s or team’s medal count.

<!-- b006515 | prose | pages [18] -->
Béla Károlyi, a renowned gymnastics coach, initially led the Romanian team to suc- cess before joining the U.S. team in 2000.

<!-- b006516 | prose | pages [18] -->
His coaching was pivotal in elevating the U.S. women’s gymnastics team, leading to outstanding performances in the 2000-2016 To evaluate his impact, we analyzed medal changes across nine Olympic Olympics. Games from 1984 to 2016.

<!-- b006517 | prose | pages [18] -->
Directly comparing medal counts before and after 2000 might result in bias due to fac- tors like the number of participants or the host nation effect. To address this, we applied the PSM-DID method: PSM reduces selection bias by matching similar samples, while

<!-- b006518 | prose | pages [18] -->
m

<!-- b006519 | prose | pages [18] -->
m

<!-- b006520 | prose | pages [18] -->
m

<!-- b006521 | prose | pages [18] -->
m

<!-- b006522 | prose | pages [18] -->
m

<!-- b006523 | prose | pages [18] -->
m

<!-- b006524 | prose | pages [18] -->
m

<!-- b006525 | prose | pages [18] -->
m

<!-- b006526 | prose | pages [18] -->
m

<!-- b006527 | prose | pages [18] -->
m

<!-- b006528 | prose | pages [18] -->
m

<!-- b006529 | prose | pages [18] -->
m

<!-- b006530 | prose | pages [18] -->
m

<!-- b006531 | prose | pages [18] -->
m

<!-- b006532 | prose | pages [18] -->
m

<!-- b006533 | prose | pages [18] -->
m

<!-- b006534 | prose | pages [18] -->
m

<!-- b006535 | prose | pages [18] -->
m

<!-- b006536 | prose | pages [18] -->
m

<!-- b006537 | prose | pages [18] -->
m m

<!-- b006538 | prose | pages [18] -->
m m

<!-- b006539 | prose | pages [18] -->
m m

<!-- b006540 | prose | pages [18] -->
m m

<!-- b006541 | prose | pages [18] -->
m

<!-- b006542 | prose | pages [18] -->
m

<!-- b006543 | prose | pages [18] -->
m

<!-- b006544 | prose | pages [18] -->
m

<!-- b006545 | prose | pages [18] -->
m

<!-- b006546 | prose | pages [18] -->
m

<!-- b006547 | prose | pages [18] -->
m

<!-- b006548 | prose | pages [18] -->
m

<!-- b006549 | prose | pages [18] -->
m

<!-- b006550 | prose | pages [18] -->
m

<!-- b006551 | prose | pages [18] -->
m

<!-- b006552 | prose | pages [18] -->
m m

<!-- b006553 | prose | pages [18] -->
m m

<!-- b006554 | prose | pages [18] -->
m m

<!-- b006555 | prose | pages [18] -->
m m

<!-- b006556 | prose | pages [18] -->
m

<!-- b006557 | prose | pages [18] -->
m

<!-- b006558 | prose | pages [18] -->
m

<!-- b006559 | prose | pages [18] -->
m

<!-- b006560 | prose | pages [18] -->
m

<!-- b006561 | prose | pages [18] -->
m

<!-- b006562 | prose | pages [18] -->
m

<!-- b006563 | prose | pages [18] -->
m

<!-- b006564 | prose | pages [18] -->
m

<!-- b006565 | prose | pages [18] -->
m

<!-- b006566 | prose | pages [18] -->
m m

<!-- b006567 | prose | pages [18] -->
m

<!-- b006568 | prose | pages [18] -->
m

<!-- b006569 | prose | pages [18] -->
m

<!-- b006570 | prose | pages [18] -->
m

<!-- b006571 | prose | pages [18] -->
m

<!-- b006572 | prose | pages [18] -->
m

<!-- b006573 | prose | pages [18] -->
m

<!-- b006574 | prose | pages [18] -->
m

<!-- b006575 | prose | pages [18] -->
m

<!-- b006576 | prose | pages [18] -->
m m

<!-- b006577 | prose | pages [18] -->
m m

<!-- b006578 | prose | pages [18] -->
m m

<!-- b006579 | prose | pages [18] -->
m m

<!-- b006580 | prose | pages [18] -->
m m

<!-- b006581 | prose | pages [18] -->
m

<!-- b006582 | prose | pages [18] -->
m

<!-- b006583 | prose | pages [18] -->
m

<!-- b006584 | prose | pages [18] -->
m

<!-- b006585 | prose | pages [18] -->
m

<!-- b006586 | prose | pages [18] -->
m

<!-- b006587 | prose | pages [18] -->
m

<!-- b006588 | prose | pages [18] -->
m

<!-- b006589 | prose | pages [18] -->
m

<!-- b006590 | prose | pages [18] -->
m

<!-- b006591 | prose | pages [18] -->
DID controls for time effects by comparing changes before and after the intervention. In

<!-- b006592 | prose | pages [18] -->
m

<!-- b006593 | prose | pages [18] -->
m

<!-- b006594 | prose | pages [18] -->
m

<!-- b006595 | prose | pages [18] -->
m

<!-- b006596 | prose | pages [18] -->
m

<!-- b006597 | prose | pages [18] -->
m

<!-- b006598 | prose | pages [18] -->
m

<!-- b006599 | prose | pages [18] -->
m

<!-- b006600 | prose | pages [18] -->
m

<!-- b006601 | prose | pages [18] -->
m

<!-- b006602 | prose | pages [18] -->
m

<!-- b006603 | prose | pages [18] -->
m

<!-- b006604 | prose | pages [18] -->
m

<!-- b006605 | prose | pages [18] -->
m

<!-- b006606 | prose | pages [18] -->
m

<!-- b006607 | prose | pages [18] -->
m

<!-- b006608 | prose | pages [18] -->
m

<!-- b006609 | prose | pages [18] -->
m

<!-- b006610 | prose | pages [18] -->
m

<!-- b006611 | prose | pages [18] -->
m

<!-- b006612 | prose | pages [18] -->
m

<!-- b006613 | prose | pages [18] -->
m

<!-- b006614 | prose | pages [18] -->
m

<!-- b006615 | prose | pages [18] -->
m

<!-- b006616 | prose | pages [18] -->
m m

<!-- b006617 | prose | pages [18] -->
m m

<!-- b006618 | prose | pages [18] -->
m m

<!-- b006619 | prose | pages [18] -->
m

<!-- b006620 | prose | pages [18] -->
m

<!-- b006621 | prose | pages [18] -->
m

<!-- b006622 | prose | pages [18] -->
m

<!-- b006623 | prose | pages [18] -->
m

<!-- b006624 | prose | pages [18] -->
m

<!-- b006625 | prose | pages [18] -->
m

<!-- b006626 | prose | pages [18] -->
m

<!-- b006627 | prose | pages [18] -->
m

<!-- b006628 | prose | pages [18] -->
m

<!-- b006629 | prose | pages [18] -->
m

<!-- b006630 | prose | pages [18] -->
m

<!-- b006631 | prose | pages [18] -->
m

<!-- b006632 | prose | pages [18] -->
m

<!-- b006633 | prose | pages [18] -->
m m

<!-- b006634 | prose | pages [18] -->
m m

<!-- b006635 | prose | pages [18] -->
m

<!-- b006636 | prose | pages [18] -->
m

<!-- b006637 | prose | pages [18] -->
m

<!-- b006638 | prose | pages [18] -->
m

<!-- b006639 | prose | pages [18] -->
m

<!-- b006640 | prose | pages [18] -->
m

<!-- b006641 | prose | pages [18] -->
m

<!-- b006642 | prose | pages [18] -->
m

<!-- b006643 | prose | pages [18] -->
m

<!-- b006644 | prose | pages [18] -->
m m

<!-- b006645 | prose | pages [18] -->
m m

<!-- b006646 | prose | pages [18] -->
m m

<!-- b006647 | prose | pages [18] -->
m

<!-- b006648 | prose | pages [18] -->
m

<!-- b006649 | prose | pages [18] -->
m

<!-- b006650 | prose | pages [18] -->
m

<!-- b006651 | prose | pages [18] -->
m

<!-- b006652 | prose | pages [18] -->
m

<!-- b006653 | prose | pages [18] -->
m

<!-- b006654 | prose | pages [18] -->
m

<!-- b006655 | prose | pages [18] -->
m

<!-- b006656 | prose | pages [18] -->
m

<!-- b006657 | prose | pages [18] -->
m

<!-- b006658 | prose | pages [18] -->
m

<!-- b006659 | prose | pages [18] -->
m m

<!-- b006660 | prose | pages [18] -->
m m

<!-- b006661 | prose | pages [18] -->
m m

<!-- b006662 | prose | pages [18] -->
m m

<!-- b006663 | prose | pages [18] -->
m m

<!-- b006664 | prose | pages [18] -->
m

<!-- b006665 | prose | pages [18] -->
m

<!-- b006666 | prose | pages [18] -->
m

<!-- b006667 | prose | pages [18] -->
m

<!-- b006668 | prose | pages [18] -->
m

<!-- b006669 | prose | pages [18] -->
m

<!-- b006670 | prose | pages [18] -->
m

<!-- b006671 | prose | pages [18] -->
m

<!-- b006672 | prose | pages [18] -->
m

<!-- b006673 | prose | pages [18] -->
m

<!-- b006674 | prose | pages [18] -->
m

<!-- b006675 | prose | pages [18] -->
m m

<!-- b006676 | prose | pages [18] -->
m m

<!-- b006677 | prose | pages [18] -->
m m

<!-- b006678 | prose | pages [18] -->
m m

<!-- b006679 | prose | pages [18] -->
m

<!-- b006680 | prose | pages [18] -->
m

<!-- b006681 | prose | pages [18] -->
m

<!-- b006682 | prose | pages [18] -->
m

<!-- b006683 | prose | pages [18] -->
m

<!-- b006684 | prose | pages [18] -->
m

<!-- b006685 | prose | pages [18] -->
m

<!-- b006686 | prose | pages [18] -->
m

<!-- b006687 | prose | pages [18] -->
m

<!-- b006688 | prose | pages [18] -->
m

<!-- b006689 | prose | pages [18] -->
m

<!-- b006690 | prose | pages [18] -->
m

<!-- b006691 | prose | pages [18] -->
m

<!-- b006692 | prose | pages [18] -->
m

<!-- b006693 | prose | pages [18] -->
m m

<!-- b006694 | prose | pages [18] -->
m m

<!-- b006695 | prose | pages [18] -->
m m

<!-- b006696 | prose | pages [18] -->
m m

<!-- b006697 | prose | pages [18] -->
m m

<!-- b006698 | prose | pages [18] -->
m

<!-- b006699 | prose | pages [18] -->
m

<!-- b006700 | prose | pages [18] -->
m

<!-- b006701 | prose | pages [18] -->
m

<!-- b006702 | prose | pages [18] -->
m

<!-- b006703 | prose | pages [18] -->
m

<!-- b006704 | prose | pages [18] -->
m

<!-- b006705 | prose | pages [18] -->
m

<!-- b006706 | prose | pages [18] -->
m

<!-- b006707 | prose | pages [18] -->
m

<!-- b006708 | prose | pages [18] -->
m

<!-- b006709 | prose | pages [18] -->
m

<!-- b006710 | prose | pages [18] -->
m

<!-- b006711 | prose | pages [18] -->
m m

<!-- b006712 | prose | pages [18] -->
m m

<!-- b006713 | prose | pages [18] -->
m m

<!-- b006714 | prose | pages [18] -->
m m

<!-- b006715 | prose | pages [18] -->
m m

<!-- b006716 | prose | pages [18] -->
m

<!-- b006717 | prose | pages [18] -->
m

<!-- b006718 | prose | pages [18] -->
m

<!-- b006719 | prose | pages [18] -->
m

<!-- b006720 | prose | pages [18] -->
m

<!-- b006721 | prose | pages [18] -->
m

<!-- b006722 | prose | pages [18] -->
m

<!-- b006723 | prose | pages [18] -->
m

<!-- b006724 | prose | pages [18] -->
m

<!-- b006725 | prose | pages [18] -->
m

<!-- b006726 | prose | pages [18] -->
m

<!-- b006727 | prose | pages [18] -->
m

<!-- b006728 | prose | pages [18] -->
this study, the U.S. women’s gymnastics team after 2000 was the treatment group, while

<!-- b006729 | prose | pages [18] -->
m

<!-- b006730 | prose | pages [18] -->
m

<!-- b006731 | prose | pages [18] -->
m

<!-- b006732 | prose | pages [18] -->
m

<!-- b006733 | prose | pages [18] -->
m

<!-- b006734 | prose | pages [18] -->
m

<!-- b006735 | prose | pages [18] -->
m

<!-- b006736 | prose | pages [18] -->
m

<!-- b006737 | prose | pages [18] -->
m

<!-- b006738 | prose | pages [18] -->
m

<!-- b006739 | prose | pages [18] -->
m

<!-- b006740 | prose | pages [18] -->
m

<!-- b006741 | prose | pages [18] -->
m

<!-- b006742 | prose | pages [18] -->
m

<!-- b006743 | prose | pages [18] -->
m

<!-- b006744 | prose | pages [18] -->
m

<!-- b006745 | prose | pages [18] -->
m

<!-- b006746 | prose | pages [18] -->
m

<!-- b006747 | prose | pages [18] -->
m

<!-- b006748 | prose | pages [18] -->
m

<!-- b006749 | prose | pages [18] -->
m

<!-- b006750 | prose | pages [18] -->
m

<!-- b006751 | prose | pages [18] -->
m

<!-- b006752 | prose | pages [18] -->
m m

<!-- b006753 | prose | pages [18] -->
m m

<!-- b006754 | prose | pages [18] -->
m m

<!-- b006755 | prose | pages [18] -->
m m

<!-- b006756 | prose | pages [18] -->
m m

<!-- b006757 | prose | pages [18] -->
m

<!-- b006758 | prose | pages [18] -->
m

<!-- b006759 | prose | pages [18] -->
m

<!-- b006760 | prose | pages [18] -->
m

<!-- b006761 | prose | pages [18] -->
m

<!-- b006762 | prose | pages [18] -->
m

<!-- b006763 | prose | pages [18] -->
m

<!-- b006764 | prose | pages [18] -->
m

<!-- b006765 | prose | pages [18] -->
m

<!-- b006766 | prose | pages [18] -->
m

<!-- b006767 | prose | pages [18] -->
m

<!-- b006768 | prose | pages [18] -->
m

<!-- b006769 | prose | pages [18] -->
m

<!-- b006770 | prose | pages [18] -->
m m

<!-- b006771 | prose | pages [18] -->
m

<!-- b006772 | prose | pages [18] -->
m

<!-- b006773 | prose | pages [18] -->
m

<!-- b006774 | prose | pages [18] -->
m

<!-- b006775 | prose | pages [18] -->
m

<!-- b006776 | prose | pages [18] -->
m

<!-- b006777 | prose | pages [18] -->
m

<!-- b006778 | prose | pages [18] -->
m

<!-- b006779 | prose | pages [18] -->
m

<!-- b006780 | prose | pages [18] -->
m

<!-- b006781 | prose | pages [18] -->
m

<!-- b006782 | prose | pages [18] -->
m m

<!-- b006783 | prose | pages [18] -->
m m

<!-- b006784 | prose | pages [18] -->
m m

<!-- b006785 | prose | pages [18] -->
m

<!-- b006786 | prose | pages [18] -->
m

<!-- b006787 | prose | pages [18] -->
m

<!-- b006788 | prose | pages [18] -->
m

<!-- b006789 | prose | pages [18] -->
m

<!-- b006790 | prose | pages [18] -->
m

<!-- b006791 | prose | pages [18] -->
m

<!-- b006792 | prose | pages [18] -->
m

<!-- b006793 | prose | pages [18] -->
m

<!-- b006794 | prose | pages [18] -->
m

<!-- b006795 | prose | pages [18] -->
m

<!-- b006796 | prose | pages [18] -->
m

<!-- b006797 | prose | pages [18] -->
m m

<!-- b006798 | prose | pages [18] -->
m m

<!-- b006799 | prose | pages [18] -->
m

<!-- b006800 | prose | pages [18] -->
m

<!-- b006801 | prose | pages [18] -->
m

<!-- b006802 | prose | pages [18] -->
m

<!-- b006803 | prose | pages [18] -->
m

<!-- b006804 | prose | pages [18] -->
m

<!-- b006805 | prose | pages [18] -->
m

<!-- b006806 | prose | pages [18] -->
m

<!-- b006807 | prose | pages [18] -->
m

<!-- b006808 | prose | pages [18] -->
m

<!-- b006809 | prose | pages [18] -->
m

<!-- b006810 | prose | pages [18] -->
m

<!-- b006811 | prose | pages [18] -->
m

<!-- b006812 | prose | pages [18] -->
m

<!-- b006813 | prose | pages [18] -->
m

<!-- b006814 | prose | pages [18] -->
m

<!-- b006815 | prose | pages [18] -->
m

<!-- b006816 | prose | pages [18] -->
m m

<!-- b006817 | prose | pages [18] -->
m m

<!-- b006818 | prose | pages [18] -->
m m

<!-- b006819 | prose | pages [18] -->
m m

<!-- b006820 | prose | pages [18] -->
m

<!-- b006821 | prose | pages [18] -->
m

<!-- b006822 | prose | pages [18] -->
m

<!-- b006823 | prose | pages [18] -->
m

<!-- b006824 | prose | pages [18] -->
m

<!-- b006825 | prose | pages [18] -->
m

<!-- b006826 | prose | pages [18] -->
m

<!-- b006827 | prose | pages [18] -->
m m

<!-- b006828 | prose | pages [18] -->
m m

<!-- b006829 | prose | pages [18] -->
m

<!-- b006830 | prose | pages [18] -->
m

<!-- b006831 | prose | pages [18] -->
m

<!-- b006832 | prose | pages [18] -->
m

<!-- b006833 | prose | pages [18] -->
m

<!-- b006834 | prose | pages [18] -->
m

<!-- b006835 | prose | pages [18] -->
m

<!-- b006836 | prose | pages [18] -->
m

<!-- b006837 | prose | pages [18] -->
m

<!-- b006838 | prose | pages [18] -->
m m

<!-- b006839 | prose | pages [18] -->
m m

<!-- b006840 | prose | pages [18] -->
m m

<!-- b006841 | prose | pages [18] -->
m m

<!-- b006842 | prose | pages [18] -->
m m

<!-- b006843 | prose | pages [18] -->
m m

<!-- b006844 | prose | pages [18] -->
m

<!-- b006845 | prose | pages [18] -->
m

<!-- b006846 | prose | pages [18] -->
m

<!-- b006847 | prose | pages [18] -->
m

<!-- b006848 | prose | pages [18] -->
m

<!-- b006849 | prose | pages [18] -->
m

<!-- b006850 | prose | pages [18] -->
m

<!-- b006851 | prose | pages [18] -->
m

<!-- b006852 | prose | pages [18] -->
m

<!-- b006853 | prose | pages [18] -->
m

<!-- b006854 | prose | pages [18] -->
m

<!-- b006855 | prose | pages [18] -->
m

<!-- b006856 | prose | pages [18] -->
m m

<!-- b006857 | prose | pages [18] -->
m m

<!-- b006858 | prose | pages [18] -->
m

<!-- b006859 | prose | pages [18] -->
m

<!-- b006860 | prose | pages [18] -->
m

<!-- b006861 | prose | pages [18] -->
m

<!-- b006862 | prose | pages [18] -->
m

<!-- b006863 | prose | pages [18] -->
m

<!-- b006864 | prose | pages [18] -->
m

<!-- b006865 | prose | pages [18] -->
m

<!-- b006866 | prose | pages [18] -->
m

<!-- b006867 | prose | pages [18] -->
m

<!-- b006868 | prose | pages [18] -->
the team before 2000 served as the control group.

<!-- b006869 | prose | pages [18] -->
m

<!-- b006870 | prose | pages [18] -->
m

<!-- b006871 | prose | pages [18] -->
m

<!-- b006872 | prose | pages [18] -->
m

<!-- b006873 | prose | pages [18] -->
m

<!-- b006874 | prose | pages [18] -->
m

<!-- b006875 | prose | pages [18] -->
m

<!-- b006876 | prose | pages [18] -->
m

<!-- b006877 | prose | pages [18] -->
m

<!-- b006878 | prose | pages [18] -->
m

<!-- b006879 | prose | pages [18] -->
m

<!-- b006880 | prose | pages [18] -->
m

<!-- b006881 | prose | pages [18] -->
m

<!-- b006882 | prose | pages [18] -->
m

<!-- b006883 | prose | pages [18] -->
m

<!-- b006884 | prose | pages [18] -->
m

<!-- b006885 | prose | pages [18] -->
m

<!-- b006886 | prose | pages [18] -->
m

<!-- b006887 | prose | pages [18] -->
m

<!-- b006888 | prose | pages [18] -->
m

<!-- b006889 | prose | pages [18] -->
m

<!-- b006890 | prose | pages [18] -->
m

<!-- b006891 | prose | pages [18] -->
m

<!-- b006892 | prose | pages [18] -->
m

<!-- b006893 | prose | pages [18] -->
m

<!-- b006894 | prose | pages [18] -->
m

<!-- b006895 | prose | pages [18] -->
m

<!-- b006896 | prose | pages [18] -->
m

<!-- b006897 | prose | pages [18] -->
m

<!-- b006898 | prose | pages [18] -->
m

<!-- b006899 | prose | pages [18] -->
m

<!-- b006900 | prose | pages [18] -->
m

<!-- b006901 | prose | pages [18] -->
m

<!-- b006902 | prose | pages [18] -->
m

<!-- b006903 | prose | pages [18] -->
m

<!-- b006904 | prose | pages [18] -->
m

<!-- b006905 | prose | pages [18] -->
m

<!-- b006906 | prose | pages [18] -->
m

<!-- b006907 | prose | pages [18] -->
m

<!-- b006908 | prose | pages [18] -->
m

<!-- b006909 | prose | pages [18] -->
m

<!-- b006910 | prose | pages [18] -->
m m

<!-- b006911 | prose | pages [18] -->
m m

<!-- b006912 | prose | pages [18] -->
m m

<!-- b006913 | prose | pages [18] -->
m m

<!-- b006914 | prose | pages [18] -->
m m

<!-- b006915 | prose | pages [18] -->
m

<!-- b006916 | prose | pages [18] -->
m

<!-- b006917 | prose | pages [18] -->
m

<!-- b006918 | prose | pages [18] -->
m

<!-- b006919 | prose | pages [18] -->
m

<!-- b006920 | prose | pages [18] -->
m

<!-- b006921 | prose | pages [18] -->
m

<!-- b006922 | prose | pages [18] -->
m

<!-- b006923 | prose | pages [18] -->
m

<!-- b006924 | prose | pages [18] -->
m

<!-- b006925 | prose | pages [18] -->
m

<!-- b006926 | prose | pages [18] -->
m

<!-- b006927 | prose | pages [18] -->
m

<!-- b006928 | prose | pages [18] -->
m

<!-- b006929 | prose | pages [18] -->
m m

<!-- b006930 | prose | pages [18] -->
m m

<!-- b006931 | prose | pages [18] -->
m m

<!-- b006932 | prose | pages [18] -->
m

<!-- b006933 | prose | pages [18] -->
m

<!-- b006934 | prose | pages [18] -->
m

<!-- b006935 | prose | pages [18] -->
m

<!-- b006936 | prose | pages [18] -->
m

<!-- b006937 | prose | pages [18] -->
m

<!-- b006938 | prose | pages [18] -->
m

<!-- b006939 | prose | pages [18] -->
m

<!-- b006940 | prose | pages [18] -->
m

<!-- b006941 | prose | pages [18] -->
m

<!-- b006942 | prose | pages [18] -->
m m

<!-- b006943 | prose | pages [18] -->
m m

<!-- b006944 | prose | pages [18] -->
m

<!-- b006945 | prose | pages [18] -->
m

<!-- b006946 | prose | pages [18] -->
m

<!-- b006947 | prose | pages [18] -->
m

<!-- b006948 | prose | pages [18] -->
m

<!-- b006949 | prose | pages [18] -->
m

<!-- b006950 | prose | pages [18] -->
m

<!-- b006951 | prose | pages [18] -->
m

<!-- b006952 | prose | pages [18] -->
m

<!-- b006953 | prose | pages [18] -->
m

<!-- b006954 | prose | pages [18] -->
m

<!-- b006955 | prose | pages [18] -->
m

<!-- b006956 | prose | pages [18] -->
m

<!-- b006957 | prose | pages [18] -->
m

<!-- b006958 | prose | pages [18] -->
m

<!-- b006959 | prose | pages [18] -->
m m

<!-- b006960 | prose | pages [18] -->
m m

<!-- b006961 | prose | pages [18] -->
m m

<!-- b006962 | prose | pages [18] -->
m m

<!-- b006963 | prose | pages [18] -->
m m

<!-- b006964 | prose | pages [18] -->
m

<!-- b006965 | prose | pages [18] -->
m

<!-- b006966 | prose | pages [18] -->
m

<!-- b006967 | prose | pages [18] -->
m

<!-- b006968 | prose | pages [18] -->
m

<!-- b006969 | prose | pages [18] -->
m

<!-- b006970 | prose | pages [18] -->
m

<!-- b006971 | prose | pages [18] -->
m

<!-- b006972 | prose | pages [18] -->
m

<!-- b006973 | prose | pages [18] -->
m

<!-- b006974 | prose | pages [18] -->
m

<!-- b006975 | prose | pages [18] -->
m

<!-- b006976 | prose | pages [18] -->
m

<!-- b006977 | prose | pages [18] -->
m m

<!-- b006978 | prose | pages [18] -->
m m

<!-- b006979 | prose | pages [18] -->
m m

<!-- b006980 | prose | pages [18] -->
m m

<!-- b006981 | prose | pages [18] -->
m

<!-- b006982 | prose | pages [18] -->
m

<!-- b006983 | prose | pages [18] -->
m

<!-- b006984 | prose | pages [18] -->
m

<!-- b006985 | prose | pages [18] -->
m

<!-- b006986 | prose | pages [18] -->
m

<!-- b006987 | prose | pages [18] -->
m

<!-- b006988 | prose | pages [18] -->
m

<!-- b006989 | prose | pages [18] -->
m

<!-- b006990 | prose | pages [18] -->
m m

<!-- b006991 | prose | pages [18] -->
m m

<!-- b006992 | prose | pages [18] -->
m m

<!-- b006993 | prose | pages [18] -->
m m

<!-- b006994 | prose | pages [18] -->
m m

<!-- b006995 | prose | pages [18] -->
m

<!-- b006996 | prose | pages [18] -->
m

<!-- b006997 | prose | pages [18] -->
m

<!-- b006998 | prose | pages [18] -->
m

<!-- b006999 | prose | pages [18] -->
m

<!-- b007000 | prose | pages [18] -->
m

<!-- b007001 | prose | pages [18] -->
m

<!-- b007002 | prose | pages [18] -->
m

<!-- b007003 | prose | pages [18] -->
m

<!-- b007004 | prose | pages [18] -->
m

<!-- b007005 | prose | pages [18] -->
m

<!-- b007006 | prose | pages [18] -->
m

<!-- b007007 | prose | pages [18] -->
m

<!-- b007008 | prose | pages [18] -->
m m

<!-- b007009 | prose | pages [18] -->
m m

<!-- b007010 | prose | pages [18] -->
m m

<!-- b007011 | prose | pages [18] -->
m m

<!-- b007012 | prose | pages [18] -->
m m

<!-- b007013 | prose | pages [18] -->
m

<!-- b007014 | prose | pages [18] -->
m

<!-- b007015 | prose | pages [18] -->
m

<!-- b007016 | prose | pages [18] -->
m

<!-- b007017 | prose | pages [18] -->
m

<!-- b007018 | prose | pages [18] -->
m

<!-- b007019 | prose | pages [18] -->
m

<!-- b007020 | prose | pages [18] -->
m m

<!-- b007021 | prose | pages [18] -->
m m

<!-- b007022 | prose | pages [18] -->
m m

<!-- b007023 | prose | pages [18] -->
m

<!-- b007024 | prose | pages [18] -->
m

<!-- b007025 | prose | pages [18] -->
m

<!-- b007026 | prose | pages [18] -->
m

<!-- b007027 | prose | pages [18] -->
m

<!-- b007028 | prose | pages [18] -->
m

<!-- b007029 | prose | pages [18] -->
m

<!-- b007030 | prose | pages [18] -->
m

<!-- b007031 | prose | pages [18] -->
m

<!-- b007032 | prose | pages [18] -->
m

<!-- b007033 | prose | pages [18] -->
m m

<!-- b007034 | prose | pages [18] -->
m

<!-- b007035 | prose | pages [18] -->
m

<!-- b007036 | prose | pages [18] -->
m

<!-- b007037 | prose | pages [18] -->
m

<!-- b007038 | prose | pages [18] -->
m

<!-- b007039 | prose | pages [18] -->
m

<!-- b007040 | prose | pages [18] -->
m

<!-- b007041 | prose | pages [18] -->
m

<!-- b007042 | prose | pages [18] -->
m

<!-- b007043 | prose | pages [18] -->
m

<!-- b007044 | prose | pages [18] -->
m

<!-- b007045 | prose | pages [18] -->
m

<!-- b007046 | prose | pages [18] -->
m m

<!-- b007047 | prose | pages [18] -->
m m

<!-- b007048 | prose | pages [18] -->
m

<!-- b007049 | prose | pages [18] -->
m

<!-- b007050 | prose | pages [18] -->
m

<!-- b007051 | prose | pages [18] -->
m

<!-- b007052 | prose | pages [18] -->
m

<!-- b007053 | prose | pages [18] -->
m

<!-- b007054 | prose | pages [18] -->
m

<!-- b007055 | prose | pages [18] -->
m

<!-- b007056 | prose | pages [18] -->
m

<!-- b007057 | prose | pages [18] -->
m

<!-- b007058 | prose | pages [18] -->
m

<!-- b007059 | prose | pages [18] -->
m

<!-- b007060 | prose | pages [18] -->
m m

<!-- b007061 | prose | pages [18] -->
m m

<!-- b007062 | prose | pages [18] -->
m

<!-- b007063 | prose | pages [18] -->
m

<!-- b007064 | prose | pages [18] -->
m

<!-- b007065 | prose | pages [18] -->
m

<!-- b007066 | prose | pages [18] -->
m

<!-- b007067 | prose | pages [18] -->
m

<!-- b007068 | prose | pages [18] -->
m

<!-- b007069 | prose | pages [18] -->
m m

<!-- b007070 | prose | pages [18] -->
m m

<!-- b007071 | prose | pages [18] -->
m m

<!-- b007072 | prose | pages [18] -->
m m

<!-- b007073 | prose | pages [18] -->
m

<!-- b007074 | prose | pages [18] -->
m

<!-- b007075 | prose | pages [18] -->
m

<!-- b007076 | prose | pages [18] -->
m

<!-- b007077 | prose | pages [18] -->
m

<!-- b007078 | prose | pages [18] -->
m

<!-- b007079 | prose | pages [18] -->
m

<!-- b007080 | prose | pages [18] -->
m

<!-- b007081 | prose | pages [18] -->
m

<!-- b007082 | prose | pages [18] -->
m

<!-- b007083 | prose | pages [18] -->
m

<!-- b007084 | prose | pages [18] -->
m

<!-- b007085 | prose | pages [18] -->
m

<!-- b007086 | prose | pages [18] -->
m

<!-- b007087 | prose | pages [18] -->
Selection of Explanatory Variables, Explained Variables and Control Variables

<!-- b007088 | prose | pages [18] -->
m

<!-- b007089 | prose | pages [18] -->
m

<!-- b007090 | prose | pages [18] -->
m

<!-- b007091 | prose | pages [18] -->
m

<!-- b007092 | prose | pages [18] -->
m

<!-- b007093 | prose | pages [18] -->
m

<!-- b007094 | prose | pages [18] -->
m

<!-- b007095 | prose | pages [18] -->
m

<!-- b007096 | prose | pages [18] -->
m

<!-- b007097 | prose | pages [18] -->
m

<!-- b007098 | prose | pages [18] -->
m

<!-- b007099 | prose | pages [18] -->
m

<!-- b007100 | prose | pages [18] -->
m

<!-- b007101 | prose | pages [18] -->
m

<!-- b007102 | prose | pages [18] -->
m

<!-- b007103 | prose | pages [18] -->
m

<!-- b007104 | prose | pages [18] -->
m

<!-- b007105 | prose | pages [18] -->
m

<!-- b007106 | prose | pages [18] -->
m

<!-- b007107 | prose | pages [18] -->
m

<!-- b007108 | prose | pages [18] -->
m

<!-- b007109 | prose | pages [18] -->
m

<!-- b007110 | prose | pages [18] -->
m

<!-- b007111 | prose | pages [18] -->
m

<!-- b007112 | prose | pages [18] -->
m

<!-- b007113 | prose | pages [18] -->
m

<!-- b007114 | prose | pages [18] -->
m m

<!-- b007115 | prose | pages [18] -->
m m

<!-- b007116 | prose | pages [18] -->
m m

<!-- b007117 | prose | pages [18] -->
m m

<!-- b007118 | prose | pages [18] -->
m

<!-- b007119 | prose | pages [18] -->
m

<!-- b007120 | prose | pages [18] -->
m

<!-- b007121 | prose | pages [18] -->
m

<!-- b007122 | prose | pages [18] -->
m

<!-- b007123 | prose | pages [18] -->
m

<!-- b007124 | prose | pages [18] -->
m

<!-- b007125 | prose | pages [18] -->
m

<!-- b007126 | prose | pages [18] -->
m

<!-- b007127 | prose | pages [18] -->
m

<!-- b007128 | prose | pages [18] -->
m

<!-- b007129 | prose | pages [18] -->
m

<!-- b007130 | prose | pages [18] -->
m m

<!-- b007131 | prose | pages [18] -->
m m

<!-- b007132 | prose | pages [18] -->
m m

<!-- b007133 | prose | pages [18] -->
m m

<!-- b007134 | prose | pages [18] -->
m m

<!-- b007135 | prose | pages [18] -->
m

<!-- b007136 | prose | pages [18] -->
m

<!-- b007137 | prose | pages [18] -->
m

<!-- b007138 | prose | pages [18] -->
m

<!-- b007139 | prose | pages [18] -->
m

<!-- b007140 | prose | pages [18] -->
m

<!-- b007141 | prose | pages [18] -->
m

<!-- b007142 | prose | pages [18] -->
m

<!-- b007143 | prose | pages [18] -->
m

<!-- b007144 | prose | pages [18] -->
m

<!-- b007145 | prose | pages [18] -->
m

<!-- b007146 | prose | pages [18] -->
m

<!-- b007147 | prose | pages [18] -->
m

<!-- b007148 | prose | pages [18] -->
m

<!-- b007149 | prose | pages [18] -->
m

<!-- b007150 | prose | pages [18] -->
m

<!-- b007151 | prose | pages [18] -->
m m

<!-- b007152 | prose | pages [18] -->
m m

<!-- b007153 | prose | pages [18] -->
m m

<!-- b007154 | prose | pages [18] -->
m

<!-- b007155 | prose | pages [18] -->
m

<!-- b007156 | prose | pages [18] -->
m

<!-- b007157 | prose | pages [18] -->
m

<!-- b007158 | prose | pages [18] -->
m

<!-- b007159 | prose | pages [18] -->
m

<!-- b007160 | prose | pages [18] -->
m

<!-- b007161 | prose | pages [18] -->
m

<!-- b007162 | prose | pages [18] -->
m

<!-- b007163 | prose | pages [18] -->
m m

<!-- b007164 | prose | pages [18] -->
m m

<!-- b007165 | prose | pages [18] -->
m

<!-- b007166 | prose | pages [18] -->
m

<!-- b007167 | prose | pages [18] -->
m

<!-- b007168 | prose | pages [18] -->
m

<!-- b007169 | prose | pages [18] -->
m

<!-- b007170 | prose | pages [18] -->
m

<!-- b007171 | prose | pages [18] -->
m

<!-- b007172 | prose | pages [18] -->
m

<!-- b007173 | prose | pages [18] -->
m

<!-- b007174 | prose | pages [18] -->
m

<!-- b007175 | prose | pages [18] -->
m

<!-- b007176 | prose | pages [18] -->
m m

<!-- b007177 | prose | pages [18] -->
m m

<!-- b007178 | prose | pages [18] -->
m m

<!-- b007179 | prose | pages [18] -->
m m

<!-- b007180 | prose | pages [18] -->
m

<!-- b007181 | prose | pages [18] -->
m

<!-- b007182 | prose | pages [18] -->
m

<!-- b007183 | prose | pages [18] -->
m

<!-- b007184 | prose | pages [18] -->
m

<!-- b007185 | prose | pages [18] -->
m

<!-- b007186 | prose | pages [18] -->
m

<!-- b007187 | prose | pages [18] -->
m

<!-- b007188 | prose | pages [18] -->
m

<!-- b007189 | prose | pages [18] -->
m

<!-- b007190 | prose | pages [18] -->
m

<!-- b007191 | prose | pages [18] -->
m m

<!-- b007192 | prose | pages [18] -->
m m

<!-- b007193 | prose | pages [18] -->
m m

<!-- b007194 | prose | pages [18] -->
m m

<!-- b007195 | prose | pages [18] -->
m m

<!-- b007196 | prose | pages [18] -->
m

<!-- b007197 | prose | pages [18] -->
m

<!-- b007198 | prose | pages [18] -->
m

<!-- b007199 | prose | pages [18] -->
m

<!-- b007200 | prose | pages [18] -->
m

<!-- b007201 | prose | pages [18] -->
m

<!-- b007202 | prose | pages [18] -->
m

<!-- b007203 | prose | pages [18] -->
m

<!-- b007204 | prose | pages [18] -->
m

<!-- b007205 | prose | pages [18] -->
m

<!-- b007206 | prose | pages [18] -->
m

<!-- b007207 | prose | pages [18] -->
m

<!-- b007208 | prose | pages [18] -->
m

<!-- b007209 | prose | pages [18] -->
• Dependent variable: The total number of medals won by the U.S. women’s gym- nastics team, focusing on the changes in medal counts after Károlyi joined in 2000.

<!-- b007210 | prose | pages [18] -->
关注数学模型

<!-- b007211 | furniture | pages [18] -->
2

<!-- b007212 | furniture | pages [18] -->
MATHmodels

<!-- b007213 | furniture | pages [18] -->
获取更多资讯

<!-- b007214 | furniture | pages [19] -->
Team # 2510862

<!-- b007215 | furniture | pages [19] -->
Page 19 of 25

<!-- b007216 | prose | pages [19] -->
• Independent variable: The effect of a great coach. The key time point is set at 2000, with Károlyi’s coaching period as the treatment group (great_coach=1) and other periods as the control group (great_coach=0). • Control variables: The number of athletes and host country status. The number of athletes reflects the team’s size during each Olympic cycle, while the host country status accounts for potential fluctuations in medal counts when the U.S. hosts the

<!-- b007217 | prose | pages [19] -->
微信公众号：数学模型

<!-- b007218 | prose | pages [19] -->
Olympics.

<!-- b007219 | prose | pages [19] -->
Model building: Select the explained

<!-- b007220 | prose | pages [19] -->
variables and covariates

<!-- b007221 | prose | pages [19] -->
The propensity score was calculated

<!-- b007222 | prose | pages [19] -->
using the Logist function

<!-- b007223 | prose | pages [19] -->
Propensity score The matching method was selected similarity principle asthe experimental group matching the

<!-- b007224 | prose | pages [19] -->
No

<!-- b007225 | prose | pages [19] -->
微信号：MATHmodels

<!-- b007226 | prose | pages [19] -->
Whether it satisfes the

<!-- b007227 | prose | pages [19] -->
common support hypothesisand the balance

<!-- b007228 | prose | pages [19] -->
hypothesis test

<!-- b007229 | prose | pages [19] -->
Yes

<!-- b007230 | prose | pages [19] -->
Do a parallel trend test on the

<!-- b007231 | prose | pages [19] -->
matched samples

<!-- b007232 | prose | pages [19] -->
A symptotic double difierence estimationis

<!-- b007233 | prose | pages [19] -->
performed for the matehed samples

<!-- b007234 | prose | pages [19] -->
Deriving "the Great

<!-- b007235 | prose | pages [19] -->
Coach Effect"

<!-- b007236 | caption | pages [19] -->
Figure 14: Implementation steps and formulae derivation of the PSM-DID methodology

<!-- b007237 | prose | pages [19] -->
• Step 1: Propensity Score Matching (PSM) The purpose of PSM is to match units of observation with similar characteristics through propensity scores. First, the propensity score, which is the probability of being in the influence group of a great coach, is estimated for each sample through a logistic regression model. In our data, the PSM model is:Equation 14

<!-- b007238 | prose | pages [19] -->
(13) P(greatcoach = 1|X) = logistic(Xβ)

<!-- b007239 | prose | pages [19] -->
where X is the control variable and β is the parameter to be estimated. The propensity scores were then used to match the ‘treatment group’ with the ‘con- trol group’. We use the nearest neighbour matching, i.e. we select the control group unit with the closest propensity score to match with each treatment group unit. Af- ter matching, we can obtain a set of similar samples that are similar on the control variables, thus reducing the impact of selection bias.

<!-- b007240 | prose | pages [19] -->
• Step 2: Difference-in-Differences (DID) The DID method is used to estimate the differential impact of a policy change or

<!-- b007241 | furniture | pages [20] -->
Team # 2510862

<!-- b007242 | furniture | pages [20] -->
Page 20 of 25

<!-- b007243 | prose | pages [20] -->
intervention that occurred at a specific point in time (2000) on the difference between the treated and control groups. We set up the DID model as:Equation 14

<!-- b007244 | prose | pages [20] -->
X · DID + Medal = β0 + β1

<!-- b007245 | prose | pages [20] -->
(14) · Control + β3 · time + ri + ϵit β2

<!-- b007246 | prose | pages [20] -->
Where: Medal is the number of medals in different years, DID is a cross-multiplier term ri ∗time indicating the effect of great coaching by Béla Károli; Control is a con- trol variable containing factors that may affect the change in the number of medals; Time is a time dummy variable to control for the effect of annual trends, taking the value of 0 before 2000 and 1 in 2000 and beyond. ri is a policy dummy variable, i.e., whether a great coach was introduced or not, with no introduction taking the value of 0 and introduction taking the value of 1. ϵit is a random error term indicating unobserved other factors; β0, β1, β2, β3 are the coefficients to be estimated.

<!-- b007247 | heading | pages [20] -->
• Step 3: Sample matching results and KDE analysis

<!-- b007248 | prose | pages [20] -->
In an attempt to verify the quality of matching, we compare the distribution of propensity scores in the treatment and control groups before and after matching by using the kernel density distribution of propensity scores (KDE). Ideally, the propensity score distributions after matching should be very similar, indicating that the matching is valid.

<!-- b007249 | caption | pages [20] -->
Figure 15: Distribution of Propensity Scores

<!-- b007250 | prose | pages [20] -->
Through the KDE graph, we can visualise the low overlap between the propensity score distributions of the two groups before matching. After the PSM distribution, the overlap is higher, indicating that the propensity score matching is effective and reduces the selection bias.

<!-- b007251 | heading | pages [20] -->
• Step 4: Analysis of DID results

<!-- b007252 | prose | pages [20] -->
The key coefficient in the DID model is the interaction term, which reflects the esti- mate of the great coaching effect. If significant and positive, it indicates that great coaching has a positive effect on the change in the number of medals won by USA Gymnastics.

<!-- b007253 | prose | pages [20] -->
关注数学模型

<!-- b007254 | furniture | pages [20] -->
2

<!-- b007255 | furniture | pages [20] -->
MATHmodels

<!-- b007256 | furniture | pages [20] -->
获取更多资讯

<!-- b007257 | furniture | pages [22] -->
Team # 2510862

<!-- b007258 | furniture | pages [22] -->
Page 22 of 25

<!-- b007259 | caption | pages [22] -->
Figure 16: Changes in medal counts before and after Béla Károlyi’s arrival

<!-- b007260 | prose | pages [22] -->
8.2

<!-- b007261 | heading | pages [22] -->
3 Countries should consider investing "Great Coach"

<!-- b007262 | prose | pages [22] -->
To explore how hiring a "great coach" can improve the medal count in gymnastics, we first established criteria for selecting countries. We focused on those countries where gymnastics has potential but whose medal count has declined in recent years.We com- pared data from two time periods: 1960-2000 and 2000-2024. First, we examined the total number of female gymnasts each country sent to the Olympics, which reflects the coun- try’s investment and emphasis on gymnastics. This metric is used to determine the size of the bubbles in the subsequent bubble chart.

<!-- b007263 | prose | pages [22] -->
Next, we compared the changes in medal counts, identifying countries that performed well between 1960-2000 but saw a decline in medals between 2000-2024. These countries may benefit from hiring a "great coach" to restore their gymnastics competitiveness. To this end, we used K-Means clustering analysis to identify countries with potential but poor recent performance. K-Means is an unsupervised learning method that divides data into groups.

<!-- b007264 | caption | pages [22] -->
Figure 17: The steps of our implementation of K-Means

<!-- b007265 | prose | pages [22] -->
关注数学模型

<!-- b007266 | furniture | pages [22] -->
2

<!-- b007267 | furniture | pages [22] -->
MATHmodels

<!-- b007268 | furniture | pages [22] -->
获取更多资讯

<!-- b007269 | furniture | pages [23] -->
Team # 2510862

<!-- b007270 | furniture | pages [23] -->
Page 23 of 25

<!-- b007271 | prose | pages [23] -->
Based on the results of the K-Means cluster analysis, we identified Spain (ESP), Japan (JPN) and Canada (CAN) as potential countries. All of these countries achieved better results between 1960-2000, however, between 2000-2024, the number of medals declined, although their investment in gymnastics remained relatively robust. By analysing these three countries, we believe that hiring ‘great coaches’ has the potential to help these coun- tries regain their level of performance, especially in women’s gymnastics.

<!-- b007272 | prose | pages [23] -->
微信公众号：数学模型

<!-- b007273 | prose | pages [23] -->
微信号：MATHmodels

<!-- b007274 | caption | pages [23] -->
Figure 18: Women’s Gymnastics Medal Counts and Participation by country

<!-- b007275 | prose | pages [23] -->
By sifting through the data from these countries and inputting it into the PSM-DID model mentioned above, we conclude that hiring ‘great coaches’ has led to significant increases in the number of medals won by women’s gymnastics in Spain, Japan, and Canada of 4.32, 2.89, and 4.75, respectively, and these increases have been statistically significant at the 0.05 level of significance. were within the statistical significance level of 0.05. This suggests that the influence of great coaches has a significant and reliable effect in improving the performance of the gymnastics programmes in these countries.

<!-- b007276 | prose | pages [23] -->
9

<!-- b007277 | heading | pages [23] -->
Model Testing

<!-- b007278 | prose | pages [23] -->
9.1

<!-- b007279 | heading | pages [23] -->
Tests of the stacking model

<!-- b007280 | prose | pages [23] -->
In this study, we use 10-fold cross-validation to assess the generalisation ability of the Stacking model.

<!-- b007281 | prose | pages [23] -->
Let the dataset be D = {x1, x2, ..., xN} , where N is the size of the dataset.

<!-- b007282 | heading | pages [23] -->
1. Divide the dataset: Randomly divide the dataset D into 10 subsets D1, D2, ..., D10,

<!-- b007283 | prose | pages [23] -->
each of which is of approximately equal size.

<!-- b007284 | heading | pages [23] -->
2. Traning and Testing: For the ith iteration, all subsets except Di are used for training

<!-- b007285 | prose | pages [23] -->
and the remaining subset Di is used as the validation set. Training set Ti = D/Di , Test set Vi = Di.

<!-- b007286 | heading | pages [23] -->
3. Calculate the performance metrics For each validation, calculate the evaluation

<!-- b007287 | prose | pages [23] -->
metrics of the model (e.g., accuracy, mean square error, etc.), denoted as:

<!-- b007288 | prose | pages [23] -->
X

<!-- b007289 | prose | pages [23] -->
1

<!-- b007290 | prose | pages [23] -->
(yj −byj)2

<!-- b007291 | prose | pages [23] -->
Ei = |Vi|

<!-- b007292 | prose | pages [23] -->
xj∈Vi

<!-- b007293 | prose | pages [23] -->
4.Calculate the average performance: The final average performance index is:

<!-- b007294 | prose | pages [23] -->
m

<!-- b007295 | prose | pages [23] -->
m

<!-- b007296 | prose | pages [23] -->
m

<!-- b007297 | prose | pages [23] -->
m

<!-- b007298 | prose | pages [23] -->
m

<!-- b007299 | prose | pages [23] -->
m

<!-- b007300 | prose | pages [23] -->
m

<!-- b007301 | prose | pages [23] -->
m

<!-- b007302 | prose | pages [23] -->
m

<!-- b007303 | prose | pages [23] -->
m

<!-- b007304 | prose | pages [23] -->
m

<!-- b007305 | prose | pages [23] -->
m

<!-- b007306 | prose | pages [23] -->
m

<!-- b007307 | prose | pages [23] -->
m

<!-- b007308 | prose | pages [23] -->
m

<!-- b007309 | prose | pages [23] -->
m

<!-- b007310 | prose | pages [23] -->
m

<!-- b007311 | prose | pages [23] -->
m

<!-- b007312 | prose | pages [23] -->
m

<!-- b007313 | prose | pages [23] -->
m

<!-- b007314 | prose | pages [23] -->
m

<!-- b007315 | prose | pages [23] -->
m

<!-- b007316 | prose | pages [23] -->
m

<!-- b007317 | prose | pages [23] -->
m

<!-- b007318 | prose | pages [23] -->
m

<!-- b007319 | prose | pages [23] -->
m

<!-- b007320 | prose | pages [23] -->
m

<!-- b007321 | prose | pages [23] -->
m

<!-- b007322 | prose | pages [23] -->
m

<!-- b007323 | prose | pages [23] -->
m

<!-- b007324 | prose | pages [23] -->
m

<!-- b007325 | prose | pages [23] -->
m

<!-- b007326 | prose | pages [23] -->
m

<!-- b007327 | prose | pages [23] -->
m

<!-- b007328 | prose | pages [23] -->
m

<!-- b007329 | prose | pages [23] -->
m

<!-- b007330 | prose | pages [23] -->
m

<!-- b007331 | prose | pages [23] -->
m

<!-- b007332 | prose | pages [23] -->
m

<!-- b007333 | prose | pages [23] -->
m

<!-- b007334 | prose | pages [23] -->
m

<!-- b007335 | prose | pages [23] -->
m

<!-- b007336 | prose | pages [23] -->
m

<!-- b007337 | prose | pages [23] -->
m

<!-- b007338 | prose | pages [23] -->
m

<!-- b007339 | prose | pages [23] -->
m

<!-- b007340 | prose | pages [23] -->
m

<!-- b007341 | prose | pages [23] -->
m

<!-- b007342 | prose | pages [23] -->
m

<!-- b007343 | prose | pages [23] -->
m

<!-- b007344 | prose | pages [23] -->
m

<!-- b007345 | prose | pages [23] -->
m

<!-- b007346 | prose | pages [23] -->
m

<!-- b007347 | prose | pages [23] -->
m

<!-- b007348 | prose | pages [23] -->
m

<!-- b007349 | prose | pages [23] -->
m

<!-- b007350 | prose | pages [23] -->
m

<!-- b007351 | prose | pages [23] -->
m

<!-- b007352 | prose | pages [23] -->
m

<!-- b007353 | prose | pages [23] -->
m

<!-- b007354 | prose | pages [23] -->
m

<!-- b007355 | prose | pages [23] -->
m

<!-- b007356 | prose | pages [23] -->
m

<!-- b007357 | prose | pages [23] -->
m

<!-- b007358 | prose | pages [23] -->
m

<!-- b007359 | prose | pages [23] -->
m

<!-- b007360 | prose | pages [23] -->
m

<!-- b007361 | prose | pages [23] -->
m

<!-- b007362 | prose | pages [23] -->
m

<!-- b007363 | prose | pages [23] -->
m

<!-- b007364 | prose | pages [23] -->
m

<!-- b007365 | prose | pages [23] -->
m

<!-- b007366 | prose | pages [23] -->
m

<!-- b007367 | prose | pages [23] -->
m

<!-- b007368 | prose | pages [23] -->
m

<!-- b007369 | prose | pages [23] -->
m

<!-- b007370 | prose | pages [23] -->
m

<!-- b007371 | prose | pages [23] -->
m

<!-- b007372 | prose | pages [23] -->
m

<!-- b007373 | prose | pages [23] -->
m

<!-- b007374 | prose | pages [23] -->
m

<!-- b007375 | prose | pages [23] -->
m

<!-- b007376 | prose | pages [23] -->
m

<!-- b007377 | prose | pages [23] -->
m

<!-- b007378 | prose | pages [23] -->
m

<!-- b007379 | prose | pages [23] -->
m

<!-- b007380 | prose | pages [23] -->
m

<!-- b007381 | prose | pages [23] -->
m

<!-- b007382 | prose | pages [23] -->
m

<!-- b007383 | prose | pages [23] -->
m

<!-- b007384 | prose | pages [23] -->
m

<!-- b007385 | prose | pages [23] -->
m

<!-- b007386 | prose | pages [23] -->
m

<!-- b007387 | prose | pages [23] -->
m

<!-- b007388 | prose | pages [23] -->
m

<!-- b007389 | prose | pages [23] -->
m

<!-- b007390 | prose | pages [23] -->
m

<!-- b007391 | prose | pages [23] -->
m

<!-- b007392 | prose | pages [23] -->
m

<!-- b007393 | prose | pages [23] -->
m

<!-- b007394 | prose | pages [23] -->
m

<!-- b007395 | prose | pages [23] -->
m

<!-- b007396 | prose | pages [23] -->
m

<!-- b007397 | prose | pages [23] -->
m

<!-- b007398 | prose | pages [23] -->
m

<!-- b007399 | prose | pages [23] -->
m

<!-- b007400 | prose | pages [23] -->
m

<!-- b007401 | prose | pages [23] -->
m

<!-- b007402 | prose | pages [23] -->
m

<!-- b007403 | prose | pages [23] -->
m

<!-- b007404 | prose | pages [23] -->
m

<!-- b007405 | prose | pages [23] -->
m

<!-- b007406 | prose | pages [23] -->
m

<!-- b007407 | prose | pages [23] -->
m

<!-- b007408 | prose | pages [23] -->
m

<!-- b007409 | prose | pages [23] -->
m

<!-- b007410 | prose | pages [23] -->
m

<!-- b007411 | prose | pages [23] -->
m

<!-- b007412 | prose | pages [23] -->
m

<!-- b007413 | prose | pages [23] -->
m

<!-- b007414 | prose | pages [23] -->
m

<!-- b007415 | prose | pages [23] -->
m

<!-- b007416 | prose | pages [23] -->
m

<!-- b007417 | prose | pages [23] -->
m

<!-- b007418 | prose | pages [23] -->
m

<!-- b007419 | prose | pages [23] -->
m

<!-- b007420 | prose | pages [23] -->
m

<!-- b007421 | prose | pages [23] -->
m

<!-- b007422 | prose | pages [23] -->
m

<!-- b007423 | prose | pages [23] -->
m

<!-- b007424 | prose | pages [23] -->
m

<!-- b007425 | prose | pages [23] -->
m

<!-- b007426 | prose | pages [23] -->
m

<!-- b007427 | prose | pages [23] -->
m

<!-- b007428 | prose | pages [23] -->
m

<!-- b007429 | prose | pages [23] -->
m

<!-- b007430 | prose | pages [23] -->
m

<!-- b007431 | prose | pages [23] -->
m

<!-- b007432 | prose | pages [23] -->
m

<!-- b007433 | prose | pages [23] -->
m

<!-- b007434 | prose | pages [23] -->
m

<!-- b007435 | prose | pages [23] -->
m

<!-- b007436 | prose | pages [23] -->
m

<!-- b007437 | prose | pages [23] -->
m

<!-- b007438 | prose | pages [23] -->
m

<!-- b007439 | prose | pages [23] -->
m

<!-- b007440 | prose | pages [23] -->
m

<!-- b007441 | prose | pages [23] -->
m

<!-- b007442 | prose | pages [23] -->
m

<!-- b007443 | prose | pages [23] -->
m

<!-- b007444 | prose | pages [23] -->
m

<!-- b007445 | prose | pages [23] -->
m

<!-- b007446 | prose | pages [23] -->
m

<!-- b007447 | prose | pages [23] -->
m

<!-- b007448 | prose | pages [23] -->
m

<!-- b007449 | prose | pages [23] -->
m

<!-- b007450 | prose | pages [23] -->
m

<!-- b007451 | prose | pages [23] -->
m

<!-- b007452 | prose | pages [23] -->
m

<!-- b007453 | prose | pages [23] -->
m

<!-- b007454 | prose | pages [23] -->
m

<!-- b007455 | prose | pages [23] -->
m

<!-- b007456 | prose | pages [23] -->
m

<!-- b007457 | prose | pages [23] -->
m

<!-- b007458 | prose | pages [23] -->
m

<!-- b007459 | prose | pages [23] -->
m

<!-- b007460 | prose | pages [23] -->
m

<!-- b007461 | prose | pages [23] -->
m

<!-- b007462 | prose | pages [23] -->
m

<!-- b007463 | prose | pages [23] -->
m

<!-- b007464 | prose | pages [23] -->
m

<!-- b007465 | prose | pages [23] -->
m

<!-- b007466 | prose | pages [23] -->
m

<!-- b007467 | prose | pages [23] -->
m

<!-- b007468 | prose | pages [23] -->
m

<!-- b007469 | prose | pages [23] -->
m

<!-- b007470 | prose | pages [23] -->
m

<!-- b007471 | prose | pages [23] -->
m

<!-- b007472 | prose | pages [23] -->
m

<!-- b007473 | prose | pages [23] -->
m

<!-- b007474 | prose | pages [23] -->
m

<!-- b007475 | prose | pages [23] -->
m

<!-- b007476 | prose | pages [23] -->
m

<!-- b007477 | prose | pages [23] -->
m

<!-- b007478 | prose | pages [23] -->
m

<!-- b007479 | prose | pages [23] -->
m

<!-- b007480 | prose | pages [23] -->
m

<!-- b007481 | prose | pages [23] -->
m

<!-- b007482 | prose | pages [23] -->
m

<!-- b007483 | prose | pages [23] -->
m

<!-- b007484 | prose | pages [23] -->
m

<!-- b007485 | prose | pages [23] -->
m

<!-- b007486 | prose | pages [23] -->
m

<!-- b007487 | prose | pages [23] -->
m

<!-- b007488 | prose | pages [23] -->
m

<!-- b007489 | prose | pages [23] -->
m

<!-- b007490 | prose | pages [23] -->
m

<!-- b007491 | prose | pages [23] -->
m

<!-- b007492 | prose | pages [23] -->
m

<!-- b007493 | prose | pages [23] -->
m

<!-- b007494 | prose | pages [23] -->
m

<!-- b007495 | prose | pages [23] -->
m

<!-- b007496 | prose | pages [23] -->
m

<!-- b007497 | prose | pages [23] -->
m

<!-- b007498 | prose | pages [23] -->
m

<!-- b007499 | prose | pages [23] -->
m

<!-- b007500 | prose | pages [23] -->
m

<!-- b007501 | prose | pages [23] -->
m

<!-- b007502 | prose | pages [23] -->
m

<!-- b007503 | prose | pages [23] -->
m

<!-- b007504 | prose | pages [23] -->
m

<!-- b007505 | prose | pages [23] -->
m

<!-- b007506 | prose | pages [23] -->
m

<!-- b007507 | prose | pages [23] -->
m

<!-- b007508 | prose | pages [23] -->
m

<!-- b007509 | prose | pages [23] -->
m

<!-- b007510 | prose | pages [23] -->
m

<!-- b007511 | prose | pages [23] -->
m

<!-- b007512 | prose | pages [23] -->
m

<!-- b007513 | prose | pages [23] -->
m

<!-- b007514 | prose | pages [23] -->
m

<!-- b007515 | prose | pages [23] -->
m

<!-- b007516 | prose | pages [23] -->
m

<!-- b007517 | prose | pages [23] -->
m

<!-- b007518 | prose | pages [23] -->
m

<!-- b007519 | prose | pages [23] -->
m

<!-- b007520 | prose | pages [23] -->
m

<!-- b007521 | prose | pages [23] -->
m

<!-- b007522 | prose | pages [23] -->
m

<!-- b007523 | prose | pages [23] -->
m

<!-- b007524 | prose | pages [23] -->
m

<!-- b007525 | prose | pages [23] -->
m

<!-- b007526 | prose | pages [23] -->
m

<!-- b007527 | prose | pages [23] -->
m

<!-- b007528 | prose | pages [23] -->
m

<!-- b007529 | prose | pages [23] -->
m

<!-- b007530 | prose | pages [23] -->
m

<!-- b007531 | prose | pages [23] -->
m

<!-- b007532 | prose | pages [23] -->
m

<!-- b007533 | prose | pages [23] -->
m

<!-- b007534 | prose | pages [23] -->
m

<!-- b007535 | prose | pages [23] -->
m

<!-- b007536 | prose | pages [23] -->
m

<!-- b007537 | prose | pages [23] -->
m

<!-- b007538 | prose | pages [23] -->
m

<!-- b007539 | prose | pages [23] -->
m

<!-- b007540 | prose | pages [23] -->
m

<!-- b007541 | prose | pages [23] -->
m

<!-- b007542 | prose | pages [23] -->
m

<!-- b007543 | prose | pages [23] -->
m

<!-- b007544 | prose | pages [23] -->
m

<!-- b007545 | prose | pages [23] -->
m

<!-- b007546 | prose | pages [23] -->
m

<!-- b007547 | prose | pages [23] -->
m

<!-- b007548 | prose | pages [23] -->
m

<!-- b007549 | prose | pages [23] -->
m

<!-- b007550 | prose | pages [23] -->
m

<!-- b007551 | prose | pages [23] -->
m

<!-- b007552 | prose | pages [23] -->
m

<!-- b007553 | prose | pages [23] -->
m

<!-- b007554 | prose | pages [23] -->
m

<!-- b007555 | prose | pages [23] -->
m

<!-- b007556 | prose | pages [23] -->
m

<!-- b007557 | prose | pages [23] -->
m

<!-- b007558 | prose | pages [23] -->
m

<!-- b007559 | prose | pages [23] -->
m

<!-- b007560 | prose | pages [23] -->
m

<!-- b007561 | prose | pages [23] -->
m

<!-- b007562 | prose | pages [23] -->
m

<!-- b007563 | prose | pages [23] -->
m

<!-- b007564 | prose | pages [23] -->
m

<!-- b007565 | prose | pages [23] -->
m

<!-- b007566 | prose | pages [23] -->
m

<!-- b007567 | prose | pages [23] -->
m

<!-- b007568 | prose | pages [23] -->
m

<!-- b007569 | prose | pages [23] -->
m

<!-- b007570 | prose | pages [23] -->
m

<!-- b007571 | prose | pages [23] -->
m

<!-- b007572 | prose | pages [23] -->
m

<!-- b007573 | prose | pages [23] -->
m

<!-- b007574 | prose | pages [23] -->
m

<!-- b007575 | prose | pages [23] -->
m

<!-- b007576 | prose | pages [23] -->
m

<!-- b007577 | prose | pages [23] -->
m

<!-- b007578 | furniture | pages [23] -->
m

<!-- b007579 | furniture | pages [23] -->
m

<!-- b007580 | furniture | pages [23] -->
m

<!-- b007581 | furniture | pages [23] -->
m

<!-- b007582 | furniture | pages [23] -->
m

<!-- b007583 | furniture | pages [23] -->
m

<!-- b007584 | furniture | pages [23] -->
m

<!-- b007585 | furniture | pages [23] -->
m

<!-- b007586 | furniture | pages [23] -->
m

<!-- b007587 | furniture | pages [23] -->
m

<!-- b007588 | furniture | pages [23] -->
m

<!-- b007589 | furniture | pages [23] -->
m

<!-- b007590 | furniture | pages [23] -->
m

<!-- b007591 | furniture | pages [23] -->
m

<!-- b007592 | furniture | pages [23] -->
m

<!-- b007593 | furniture | pages [23] -->
m

<!-- b007594 | furniture | pages [23] -->
m

<!-- b007595 | furniture | pages [23] -->
m

<!-- b007596 | furniture | pages [23] -->
m

<!-- b007597 | furniture | pages [23] -->
m

<!-- b007598 | furniture | pages [23] -->
m

<!-- b007599 | furniture | pages [23] -->
m

<!-- b007600 | furniture | pages [23] -->
m

<!-- b007601 | furniture | pages [23] -->
m

<!-- b007602 | furniture | pages [23] -->
m

<!-- b007603 | furniture | pages [23] -->
m

<!-- b007604 | furniture | pages [23] -->
m

<!-- b007605 | furniture | pages [23] -->
m

<!-- b007606 | furniture | pages [23] -->
m

<!-- b007607 | furniture | pages [23] -->
m

<!-- b007608 | furniture | pages [23] -->
m

<!-- b007609 | furniture | pages [23] -->
m

<!-- b007610 | furniture | pages [23] -->
m

<!-- b007611 | furniture | pages [23] -->
m

<!-- b007612 | furniture | pages [23] -->
m

<!-- b007613 | furniture | pages [23] -->
m

<!-- b007614 | furniture | pages [23] -->
m

<!-- b007615 | furniture | pages [23] -->
m

<!-- b007616 | furniture | pages [23] -->
m

<!-- b007617 | furniture | pages [23] -->
m

<!-- b007618 | furniture | pages [23] -->
m

<!-- b007619 | furniture | pages [23] -->
m

<!-- b007620 | furniture | pages [23] -->
m

<!-- b007621 | furniture | pages [23] -->
m

<!-- b007622 | furniture | pages [23] -->
m

<!-- b007623 | furniture | pages [23] -->
m

<!-- b007624 | furniture | pages [23] -->
m

<!-- b007625 | furniture | pages [23] -->
m

<!-- b007626 | furniture | pages [23] -->
m

<!-- b007627 | furniture | pages [23] -->
m

<!-- b007628 | furniture | pages [23] -->
m

<!-- b007629 | furniture | pages [23] -->
m

<!-- b007630 | furniture | pages [23] -->
m

<!-- b007631 | furniture | pages [23] -->
m

<!-- b007632 | furniture | pages [23] -->
m

<!-- b007633 | furniture | pages [23] -->
m

<!-- b007634 | furniture | pages [23] -->
m

<!-- b007635 | furniture | pages [23] -->
m

<!-- b007636 | furniture | pages [23] -->
m

<!-- b007637 | furniture | pages [23] -->
m

<!-- b007638 | furniture | pages [23] -->
m

<!-- b007639 | furniture | pages [23] -->
m

<!-- b007640 | furniture | pages [23] -->
m

<!-- b007641 | furniture | pages [23] -->
m

<!-- b007642 | furniture | pages [23] -->
m

<!-- b007643 | furniture | pages [23] -->
m

<!-- b007644 | furniture | pages [23] -->
m

<!-- b007645 | furniture | pages [23] -->
m

<!-- b007646 | furniture | pages [23] -->
m

<!-- b007647 | furniture | pages [23] -->
m

<!-- b007648 | furniture | pages [23] -->
m

<!-- b007649 | furniture | pages [23] -->
m

<!-- b007650 | furniture | pages [23] -->
m

<!-- b007651 | furniture | pages [23] -->
m

<!-- b007652 | furniture | pages [23] -->
m

<!-- b007653 | furniture | pages [23] -->
m

<!-- b007654 | furniture | pages [23] -->
m

<!-- b007655 | furniture | pages [23] -->
m

<!-- b007656 | furniture | pages [23] -->
m

<!-- b007657 | furniture | pages [23] -->
m

<!-- b007658 | furniture | pages [23] -->
m

<!-- b007659 | furniture | pages [23] -->
m

<!-- b007660 | furniture | pages [23] -->
m

<!-- b007661 | furniture | pages [23] -->
m

<!-- b007662 | furniture | pages [23] -->
m

<!-- b007663 | furniture | pages [23] -->
m

<!-- b007664 | furniture | pages [23] -->
m

<!-- b007665 | furniture | pages [23] -->
m

<!-- b007666 | furniture | pages [23] -->
m

<!-- b007667 | furniture | pages [23] -->
m

<!-- b007668 | furniture | pages [23] -->
m

<!-- b007669 | furniture | pages [23] -->
m

<!-- b007670 | furniture | pages [23] -->
m

<!-- b007671 | furniture | pages [23] -->
m

<!-- b007672 | furniture | pages [23] -->
m

<!-- b007673 | furniture | pages [23] -->
m

<!-- b007674 | furniture | pages [23] -->
m

<!-- b007675 | furniture | pages [23] -->
m

<!-- b007676 | furniture | pages [23] -->
m

<!-- b007677 | furniture | pages [23] -->
m

<!-- b007678 | furniture | pages [23] -->
m

<!-- b007679 | furniture | pages [23] -->
m

<!-- b007680 | furniture | pages [23] -->
m

<!-- b007681 | furniture | pages [23] -->
m

<!-- b007682 | furniture | pages [23] -->
m

<!-- b007683 | furniture | pages [23] -->
m

<!-- b007684 | furniture | pages [23] -->
m

<!-- b007685 | furniture | pages [23] -->
m

<!-- b007686 | furniture | pages [23] -->
m

<!-- b007687 | furniture | pages [23] -->
m

<!-- b007688 | furniture | pages [23] -->
m

<!-- b007689 | furniture | pages [23] -->
m

<!-- b007690 | furniture | pages [23] -->
m

<!-- b007691 | furniture | pages [23] -->
m

<!-- b007692 | furniture | pages [23] -->
m

<!-- b007693 | furniture | pages [23] -->
m

<!-- b007694 | furniture | pages [23] -->
m

<!-- b007695 | furniture | pages [23] -->
m

<!-- b007696 | furniture | pages [23] -->
m

<!-- b007697 | furniture | pages [23] -->
m

<!-- b007698 | furniture | pages [23] -->
m

<!-- b007699 | furniture | pages [23] -->
m

<!-- b007700 | furniture | pages [23] -->
m

<!-- b007701 | furniture | pages [23] -->
m

<!-- b007702 | furniture | pages [23] -->
m

<!-- b007703 | furniture | pages [23] -->
m

<!-- b007704 | furniture | pages [23] -->
m

<!-- b007705 | furniture | pages [23] -->
m

<!-- b007706 | furniture | pages [23] -->
m

<!-- b007707 | furniture | pages [23] -->
m

<!-- b007708 | furniture | pages [23] -->
m

<!-- b007709 | furniture | pages [23] -->
m

<!-- b007710 | furniture | pages [23] -->
m

<!-- b007711 | furniture | pages [23] -->
m

<!-- b007712 | furniture | pages [23] -->
m

<!-- b007713 | furniture | pages [23] -->
m

<!-- b007714 | furniture | pages [23] -->
m

<!-- b007715 | furniture | pages [23] -->
m

<!-- b007716 | furniture | pages [23] -->
m

<!-- b007717 | furniture | pages [23] -->
m

<!-- b007718 | furniture | pages [23] -->
m

<!-- b007719 | furniture | pages [23] -->
m

<!-- b007720 | furniture | pages [23] -->
m

<!-- b007721 | furniture | pages [23] -->
m

<!-- b007722 | furniture | pages [23] -->
m

<!-- b007723 | furniture | pages [23] -->
m

<!-- b007724 | furniture | pages [23] -->
m

<!-- b007725 | furniture | pages [23] -->
m

<!-- b007726 | furniture | pages [23] -->
m

<!-- b007727 | furniture | pages [23] -->
m

<!-- b007728 | furniture | pages [23] -->
m

<!-- b007729 | furniture | pages [23] -->
m

<!-- b007730 | furniture | pages [23] -->
m

<!-- b007731 | furniture | pages [23] -->
m

<!-- b007732 | furniture | pages [23] -->
m

<!-- b007733 | furniture | pages [23] -->
m

<!-- b007734 | furniture | pages [23] -->
m

<!-- b007735 | furniture | pages [23] -->
m

<!-- b007736 | furniture | pages [23] -->
m

<!-- b007737 | furniture | pages [23] -->
m

<!-- b007738 | furniture | pages [23] -->
m

<!-- b007739 | furniture | pages [23] -->
m

<!-- b007740 | furniture | pages [23] -->
m

<!-- b007741 | furniture | pages [23] -->
m

<!-- b007742 | furniture | pages [23] -->
m

<!-- b007743 | furniture | pages [23] -->
m

<!-- b007744 | furniture | pages [23] -->
m

<!-- b007745 | furniture | pages [23] -->
m

<!-- b007746 | furniture | pages [23] -->
m

<!-- b007747 | furniture | pages [23] -->
m

<!-- b007748 | furniture | pages [23] -->
m

<!-- b007749 | furniture | pages [23] -->
m

<!-- b007750 | furniture | pages [23] -->
m

<!-- b007751 | furniture | pages [23] -->
m

<!-- b007752 | furniture | pages [23] -->
m

<!-- b007753 | furniture | pages [23] -->
m

<!-- b007754 | furniture | pages [23] -->
m

<!-- b007755 | furniture | pages [23] -->
m

<!-- b007756 | furniture | pages [23] -->
m

<!-- b007757 | furniture | pages [23] -->
m

<!-- b007758 | furniture | pages [23] -->
m

<!-- b007759 | furniture | pages [23] -->
m

<!-- b007760 | furniture | pages [23] -->
m

<!-- b007761 | furniture | pages [23] -->
m

<!-- b007762 | furniture | pages [23] -->
m

<!-- b007763 | furniture | pages [23] -->
m

<!-- b007764 | furniture | pages [23] -->
m

<!-- b007765 | furniture | pages [23] -->
m

<!-- b007766 | furniture | pages [23] -->
m

<!-- b007767 | furniture | pages [23] -->
m

<!-- b007768 | furniture | pages [23] -->
m

<!-- b007769 | furniture | pages [23] -->
m

<!-- b007770 | furniture | pages [23] -->
m

<!-- b007771 | furniture | pages [23] -->
m

<!-- b007772 | furniture | pages [23] -->
m

<!-- b007773 | furniture | pages [23] -->
m

<!-- b007774 | furniture | pages [23] -->
m

<!-- b007775 | furniture | pages [23] -->
m

<!-- b007776 | furniture | pages [23] -->
m

<!-- b007777 | furniture | pages [23] -->
m

<!-- b007778 | furniture | pages [23] -->
m

<!-- b007779 | furniture | pages [23] -->
m

<!-- b007780 | furniture | pages [23] -->
m

<!-- b007781 | furniture | pages [23] -->
m

<!-- b007782 | furniture | pages [23] -->
m

<!-- b007783 | furniture | pages [23] -->
m

<!-- b007784 | furniture | pages [23] -->
m

<!-- b007785 | furniture | pages [23] -->
m

<!-- b007786 | furniture | pages [23] -->
m

<!-- b007787 | furniture | pages [23] -->
m

<!-- b007788 | furniture | pages [23] -->
m

<!-- b007789 | furniture | pages [23] -->
m

<!-- b007790 | furniture | pages [23] -->
m

<!-- b007791 | furniture | pages [23] -->
m

<!-- b007792 | furniture | pages [23] -->
m

<!-- b007793 | furniture | pages [23] -->
m

<!-- b007794 | furniture | pages [23] -->
m

<!-- b007795 | furniture | pages [23] -->
m

<!-- b007796 | furniture | pages [23] -->
m

<!-- b007797 | furniture | pages [23] -->
m

<!-- b007798 | furniture | pages [23] -->
m

<!-- b007799 | furniture | pages [23] -->
m

<!-- b007800 | furniture | pages [23] -->
m

<!-- b007801 | furniture | pages [23] -->
m

<!-- b007802 | furniture | pages [23] -->
m

<!-- b007803 | furniture | pages [23] -->
m

<!-- b007804 | furniture | pages [23] -->
m

<!-- b007805 | furniture | pages [23] -->
m

<!-- b007806 | furniture | pages [23] -->
m

<!-- b007807 | furniture | pages [23] -->
m

<!-- b007808 | furniture | pages [23] -->
m

<!-- b007809 | furniture | pages [23] -->
m

<!-- b007810 | furniture | pages [23] -->
m

<!-- b007811 | furniture | pages [23] -->
m

<!-- b007812 | furniture | pages [23] -->
m

<!-- b007813 | furniture | pages [23] -->
m

<!-- b007814 | furniture | pages [23] -->
m

<!-- b007815 | furniture | pages [23] -->
m

<!-- b007816 | furniture | pages [23] -->
m

<!-- b007817 | furniture | pages [23] -->
m

<!-- b007818 | furniture | pages [23] -->
m

<!-- b007819 | furniture | pages [23] -->
m

<!-- b007820 | furniture | pages [23] -->
m

<!-- b007821 | furniture | pages [23] -->
m

<!-- b007822 | furniture | pages [23] -->
m

<!-- b007823 | furniture | pages [23] -->
m

<!-- b007824 | furniture | pages [23] -->
m

<!-- b007825 | furniture | pages [23] -->
m

<!-- b007826 | furniture | pages [23] -->
m

<!-- b007827 | furniture | pages [23] -->
m

<!-- b007828 | furniture | pages [23] -->
m

<!-- b007829 | furniture | pages [23] -->
m

<!-- b007830 | furniture | pages [23] -->
m

<!-- b007831 | furniture | pages [23] -->
m

<!-- b007832 | furniture | pages [23] -->
m

<!-- b007833 | furniture | pages [23] -->
m

<!-- b007834 | furniture | pages [23] -->
m

<!-- b007835 | furniture | pages [23] -->
m

<!-- b007836 | furniture | pages [23] -->
m

<!-- b007837 | furniture | pages [23] -->
m

<!-- b007838 | furniture | pages [23] -->
m

<!-- b007839 | furniture | pages [23] -->
m

<!-- b007840 | furniture | pages [23] -->
m

<!-- b007841 | furniture | pages [23] -->
m

<!-- b007842 | furniture | pages [23] -->
m

<!-- b007843 | furniture | pages [23] -->
m

<!-- b007844 | furniture | pages [23] -->
m

<!-- b007845 | furniture | pages [23] -->
m

<!-- b007846 | furniture | pages [23] -->
m

<!-- b007847 | furniture | pages [23] -->
m

<!-- b007848 | furniture | pages [23] -->
m

<!-- b007849 | furniture | pages [23] -->
m

<!-- b007850 | furniture | pages [23] -->
m

<!-- b007851 | furniture | pages [23] -->
m

<!-- b007852 | furniture | pages [23] -->
m

<!-- b007853 | furniture | pages [23] -->
m

<!-- b007854 | furniture | pages [23] -->
m

<!-- b007855 | furniture | pages [23] -->
m

<!-- b007856 | furniture | pages [23] -->
m

<!-- b007857 | furniture | pages [23] -->
m

<!-- b007858 | furniture | pages [23] -->
m

<!-- b007859 | furniture | pages [23] -->
m

<!-- b007860 | furniture | pages [23] -->
m

<!-- b007861 | furniture | pages [23] -->
m

<!-- b007862 | furniture | pages [23] -->
m

<!-- b007863 | furniture | pages [23] -->
m

<!-- b007864 | furniture | pages [23] -->
m

<!-- b007865 | furniture | pages [23] -->
m

<!-- b007866 | furniture | pages [23] -->
m

<!-- b007867 | furniture | pages [23] -->
m

<!-- b007868 | furniture | pages [23] -->
m

<!-- b007869 | furniture | pages [23] -->
m

<!-- b007870 | furniture | pages [23] -->
m

<!-- b007871 | furniture | pages [23] -->
m

<!-- b007872 | furniture | pages [23] -->
m

<!-- b007873 | furniture | pages [23] -->
m

<!-- b007874 | furniture | pages [23] -->
m

<!-- b007875 | furniture | pages [23] -->
m

<!-- b007876 | furniture | pages [23] -->
m

<!-- b007877 | furniture | pages [23] -->
m

<!-- b007878 | furniture | pages [23] -->
m

<!-- b007879 | furniture | pages [23] -->
m

<!-- b007880 | furniture | pages [23] -->
m

<!-- b007881 | furniture | pages [23] -->
m

<!-- b007882 | furniture | pages [23] -->
m

<!-- b007883 | furniture | pages [23] -->
m

<!-- b007884 | furniture | pages [23] -->
m

<!-- b007885 | furniture | pages [23] -->
m

<!-- b007886 | furniture | pages [23] -->
m

<!-- b007887 | furniture | pages [23] -->
m

<!-- b007888 | furniture | pages [23] -->
m

<!-- b007889 | furniture | pages [23] -->
m

<!-- b007890 | furniture | pages [23] -->
m

<!-- b007891 | furniture | pages [23] -->
m

<!-- b007892 | furniture | pages [23] -->
m

<!-- b007893 | furniture | pages [23] -->
m

<!-- b007894 | furniture | pages [23] -->
m

<!-- b007895 | furniture | pages [23] -->
m

<!-- b007896 | furniture | pages [23] -->
m

<!-- b007897 | furniture | pages [23] -->
m

<!-- b007898 | furniture | pages [23] -->
m

<!-- b007899 | furniture | pages [23] -->
m

<!-- b007900 | furniture | pages [23] -->
m

<!-- b007901 | furniture | pages [23] -->
m

<!-- b007902 | furniture | pages [23] -->
m

<!-- b007903 | furniture | pages [23] -->
m

<!-- b007904 | furniture | pages [23] -->
m

<!-- b007905 | furniture | pages [23] -->
m

<!-- b007906 | furniture | pages [23] -->
m

<!-- b007907 | furniture | pages [23] -->
m

<!-- b007908 | furniture | pages [23] -->
m

<!-- b007909 | furniture | pages [23] -->
m

<!-- b007910 | furniture | pages [23] -->
m

<!-- b007911 | furniture | pages [23] -->
m

<!-- b007912 | furniture | pages [23] -->
m

<!-- b007913 | furniture | pages [23] -->
m

<!-- b007914 | furniture | pages [23] -->
m

<!-- b007915 | furniture | pages [23] -->
m

<!-- b007916 | furniture | pages [23] -->
m

<!-- b007917 | furniture | pages [23] -->
m

<!-- b007918 | furniture | pages [23] -->
m

<!-- b007919 | furniture | pages [23] -->
m

<!-- b007920 | furniture | pages [23] -->
m

<!-- b007921 | furniture | pages [23] -->
m

<!-- b007922 | furniture | pages [23] -->
m

<!-- b007923 | furniture | pages [23] -->
m

<!-- b007924 | furniture | pages [23] -->
m

<!-- b007925 | furniture | pages [23] -->
m

<!-- b007926 | furniture | pages [23] -->
m

<!-- b007927 | furniture | pages [23] -->
m

<!-- b007928 | furniture | pages [23] -->
m

<!-- b007929 | furniture | pages [23] -->
m

<!-- b007930 | furniture | pages [23] -->
m

<!-- b007931 | furniture | pages [23] -->
m

<!-- b007932 | furniture | pages [23] -->
m

<!-- b007933 | furniture | pages [23] -->
m

<!-- b007934 | furniture | pages [23] -->
m

<!-- b007935 | furniture | pages [23] -->
m

<!-- b007936 | furniture | pages [23] -->
m

<!-- b007937 | furniture | pages [23] -->
m

<!-- b007938 | furniture | pages [23] -->
m

<!-- b007939 | furniture | pages [23] -->
m

<!-- b007940 | furniture | pages [23] -->
m

<!-- b007941 | furniture | pages [23] -->
m

<!-- b007942 | furniture | pages [23] -->
m

<!-- b007943 | furniture | pages [23] -->
m

<!-- b007944 | furniture | pages [23] -->
m

<!-- b007945 | furniture | pages [23] -->
m

<!-- b007946 | furniture | pages [23] -->
m

<!-- b007947 | furniture | pages [23] -->
m

<!-- b007948 | furniture | pages [23] -->
m

<!-- b007949 | furniture | pages [23] -->
m

<!-- b007950 | furniture | pages [23] -->
m

<!-- b007951 | furniture | pages [23] -->
m

<!-- b007952 | furniture | pages [23] -->
m

<!-- b007953 | furniture | pages [23] -->
m

<!-- b007954 | furniture | pages [23] -->
m

<!-- b007955 | furniture | pages [23] -->
m

<!-- b007956 | furniture | pages [23] -->
m

<!-- b007957 | furniture | pages [23] -->
m

<!-- b007958 | furniture | pages [23] -->
m

<!-- b007959 | furniture | pages [23] -->
m

<!-- b007960 | furniture | pages [23] -->
m

<!-- b007961 | furniture | pages [23] -->
m

<!-- b007962 | furniture | pages [23] -->
m

<!-- b007963 | furniture | pages [23] -->
m

<!-- b007964 | furniture | pages [23] -->
m

<!-- b007965 | furniture | pages [23] -->
m

<!-- b007966 | furniture | pages [23] -->
m

<!-- b007967 | furniture | pages [23] -->
m

<!-- b007968 | furniture | pages [23] -->
m

<!-- b007969 | furniture | pages [23] -->
m

<!-- b007970 | furniture | pages [23] -->
m

<!-- b007971 | furniture | pages [23] -->
m

<!-- b007972 | furniture | pages [23] -->
m

<!-- b007973 | furniture | pages [23] -->
m

<!-- b007974 | furniture | pages [23] -->
m

<!-- b007975 | furniture | pages [23] -->
m

<!-- b007976 | furniture | pages [23] -->
m

<!-- b007977 | furniture | pages [23] -->
m

<!-- b007978 | furniture | pages [23] -->
m

<!-- b007979 | furniture | pages [23] -->
m

<!-- b007980 | furniture | pages [23] -->
m

<!-- b007981 | furniture | pages [24] -->
Team # 2510862

<!-- b007982 | prose | pages [24] -->
Eavg = 1

<!-- b007983 | furniture | pages [24] -->
Page 24 of 25

<!-- b007984 | prose | pages [24] -->
10 X

<!-- b007985 | prose | pages [24] -->
Ei

<!-- b007986 | prose | pages [24] -->
10

<!-- b007987 | prose | pages [24] -->
i=1

<!-- b007988 | prose | pages [24] -->
Where Eavg is the average error or evaluation metric of the 10-fold cross-validation. After 10-fold cross-validation, the average R² of the Stacking model is 0.89, the average MSE is 0.31, and the average MAPE is 0.30, and these results do not fluctuate much from the performance without cross-validation, which indicates that the model’s performance on different data subsets stays consistent with good stability and generalisation ability.

<!-- b007989 | prose | pages [24] -->
9.2

<!-- b007990 | heading | pages [24] -->
Tests of the PSM-DID model

<!-- b007991 | heading | pages [24] -->
1. Balance test

<!-- b007992 | prose | pages [24] -->
Balance testing is an important step in assessing the validity of the propensity score matching (PSM) method. Its central aim is to ensure the differences between the treatment and control groups on the covariates after matching have been effectively controlled for, so the causal effects estimated by the model are reliable. With the KDE plots drawn earlier, we have analysed the proximity of distributions of the treatment and control groups be- fore and after matching. To further verify the balance of matching, we calculated the stan- dardised mean difference (SMD) values.The formula for the SMD values is:Equation 15

<!-- b007993 | prose | pages [24] -->
q SMD = XT −XC

<!-- b007994 | prose | pages [24] -->
(15)

<!-- b007995 | prose | pages [24] -->
V ar(XT )+V ar(XC)

<!-- b007996 | prose | pages [24] -->
2

<!-- b007997 | prose | pages [24] -->
The smaller the SMD value, the smaller the difference between the two groups, indi- cating better matching. Typically, an SMD value less than 0.1 suggests good matching quality. After calculation, we got the SMD value of 0.0013, which is significantly lower than the threshold of 0.1, indicating that the difference between the treatment group and the control group on the covariate has been effectively controlled, and the balance after matching is good. Therefore, the matching effect met the expectation and further verified the validity of our propensity score matching (PSM) method.

<!-- b007998 | heading | pages [24] -->
2. Sensitivity Analysis

<!-- b007999 | prose | pages [24] -->
Sensitivity analysis is used to evaluate the model’s response to changes in input vari- ables, particularly when facing uncertainty and changes in assumptions. It helps us un- derstand how sensitive the model is to different inputs, ensuring the model’s stability and reliability. In this study, the purpose of sensitivity analysis is to examine how changes in key factors affect the Olympic medal prediction model and assess its performance under different assumptions.

<!-- b008000 | prose | pages [24] -->
We selected input variables such as historical medal data, athlete participation, and host countries, and made small adjustments to these variables (±3%, ±5%, ±10%). After each adjustment, we reran the model and recorded the changes in the output, analyzing how the output changed with the input variations. By comparing the prediction results after different adjustments, we assess the model’s stability. If the model remains stable de- spite small changes in input, it indicates that the model is not sensitive to these variables and is robust.The analysis results show that small changes in the input variables have a minimal impact on the prediction results (standard error changes of ±1.174%, ±1.502%, ±3.115%), indicating that the model is stable.

<!-- b008001 | prose | pages [24] -->
关注数学模型

<!-- b008002 | furniture | pages [24] -->
2

<!-- b008003 | furniture | pages [24] -->
MATHmodels

<!-- b008004 | furniture | pages [24] -->
获取更多资讯

<!-- b008005 | furniture | pages [25] -->
Team # 2510862

<!-- b008006 | furniture | pages [25] -->
Page 25 of 25

<!-- b008007 | prose | pages [25] -->
10

<!-- b008008 | heading | pages [25] -->
Letter

<!-- b008009 | prose | pages [25] -->
Dear Members of National Olympic Committees, As we prepare for the 2028 Los Angeles Olympics, we have analyzed medal distribu- tion patterns using historical data and advanced modeling. Our findings provide valu- able insights to support strategic planning for participating nations.

<!-- b008010 | prose | pages [25] -->
We used the Stacking method to combine multiple models, improving prediction ac- curacy. Based on our model, the top five countries on the 2028 medal table are projected to be: the United States, China, Australia, France, and Germany. The model’s low MSE and MAPE indicate high reliability. Leading countries should focus on optimizing resources,

<!-- b008011 | prose | pages [25] -->
微信公众号：数学模型

<!-- b008012 | prose | pages [25] -->
while others can invest in potential events to seek breakthroughs.

<!-- b008013 | prose | pages [25] -->
For non-medal-winning nations, we analyzed participation trends and identified events with higher probabilities of first-time medals. These nations should increase investment in their strongest events to improve medal chances.

<!-- b008014 | prose | pages [25] -->
We also explored the relationship between events and medals. Using SHAP analysis, we found that new sports like rugby-related events could significantly benefit the United States, aligning with its traditional strengths. Countries should strategically prepare for these new events to maximize their opportunities.

<!-- b008015 | prose | pages [25] -->
On the "Great Coach Effect," our analysis of the U.S. gymnastics team shows that ex- ceptional coaching significantly boosts medal counts. The PSM-DID model confirmed

<!-- b008016 | prose | pages [25] -->
微信号：MATHmodels

<!-- b008017 | prose | pages [25] -->
this effect, and we identified Spain, Japan, and Canada as nations with potential to bene- fit from hiring great coaches to rebuild their competitiveness in gymnastics.

<!-- b008018 | prose | pages [25] -->
In summary, our analysis offers a data-driven approach for Olympic preparation. From medal predictions to identifying first-time winners and event-specific strategies, our findings provide actionable insights to help countries excel at the 2028 Olympics.

<!-- b008019 | prose | pages [25] -->
Sincerely, Team 2510862

<!-- b008020 | heading | pages [25] -->
References

<!-- b008021 | references | pages [25] -->
[1] Sanchez-Fernandez, Patricio; Vaammonde-Liste, Antonio,”Olympic medals : suc-

<!-- b008022 | references | pages [25] -->
cess predictions for Rio-2016”, Sabinet,2016 Publishing Company , 1984-1986.

<!-- b008023 | references | pages [25] -->
[2] H.M.Shi,D.Y.Zhang,Y.H.Zhang, "Can Olympic medals be predicted? — A perspec-

<!-- b008024 | references | pages [25] -->
tive based on interpretable machine learning",Journal,2024

<!-- b008025 | references | pages [25] -->
[3] F.Wang,” Prediction of Olympic Medal Results for the 2020 Games Based on Neural

<!-- b008026 | references | pages [25] -->
Networks”,Journal,2023

<!-- b008027 | references | pages [25] -->
[4] Schlembach Christoph; Schmidt Sascha L.; Schreyer Dominik; Wunderlich Linus,”

<!-- b008028 | references | pages [25] -->
Forecasting the Olympic medal distribution – A socioeconomic machine learning

<!-- b008029 | references | pages [25] -->
model”, Elsevier,2022
