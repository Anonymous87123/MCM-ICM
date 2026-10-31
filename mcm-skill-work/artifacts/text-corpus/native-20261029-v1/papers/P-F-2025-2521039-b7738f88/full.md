# P-F-2025-2521039-b7738f88

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
F

<!-- b000006 | furniture | pages [1] -->
2521039

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
The Global Cybersecurity Chessboard: Decoding Crime

<!-- b000009 | title | pages [1] -->
Distribution and Policy Effectiveness

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
With the acceleration of digital transformation, cybersecurity has become a critical area for national security, economic development, and social stability. This study aims to understand the global distribution of cybercrime, further assess the effectiveness of cybersecurity policies, and explore the key factors inﬂuencing the global distribution of cybercrime. By analyzing open data from the VERIS Community Database (VCDB), we employed correlation analysis, the Hierarchical Interaction Scoring Regression

<!-- b000012 | title | pages [1] -->
微信公众号：数学模型

<!-- b000013 | prose | pages [1] -->
Model (HISR), and the Log-Enhanced Quadratic Regression Model (LEQR) to quan- tify the changes in cybercrime distribution before and after policy implementation, and evaluate the net effect of these policies. The results indicate that improvements in technological measures and organizational measures have a signiﬁcant impact on the effectiveness of cybersecurity policies, while the reporting rate and disruption rate are key indicators for evaluating policy effectiveness.

<!-- b000014 | prose | pages [1] -->
Firstly, we conducted in-depth analysis and data visualization using open data from VCDB. In terms of geographical visualization, the study created a heatmap to display the global distribution of cybercrime events, and further analyzed key cyber- crime indicators, such as the number of targets and success rates. The ﬁndings reveal

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
a signiﬁcant imbalance in the global distribution of cybercrime.

<!-- b000017 | prose | pages [1] -->
Subsequently, we developed a cybersecurity evaluation framework encompassing ﬁve pillars: legal measures, technical measures, organizational measures, capacity building, and international cooperation, to comprehensively assess the effectiveness of cybersecurity policies across countries. The results showed that the United States scored the highest, with its policies performing excellently in improving the reporting rate (0.32). In contrast, China scored the lowest with a composite score of -0.78. We then classiﬁed the policies based on the ﬁve pillars of the Global Cybersecurity Index (GCI) and found that improvements in technical capabilities and efﬁcient organiza- tional coordination are key factors for policy success.

<!-- b000018 | prose | pages [1] -->
Additionally, we explored the correlation between national demographic data, such as GDP, population size, and ICT development level, and cybercrime data, an- alyzing their inﬂuence on the number of cybercrime targets. The results showed that GDP, population size, and ICT development level are positively correlated with the distribution of cybercrime, consistent with the global crime distribution pattern.

<!-- b000019 | heading | pages [1] -->
Finally, we summarize the strengths and weaknesses of the models and methods

<!-- b000020 | prose | pages [1] -->
used, offering appropriate policy recommendations. The study provides new perspec- tives and methodologies for the formulation and evaluation of global cybersecurity policies, emphasizing the importance of technological and organizational measures in enhancing cybersecurity levels.

<!-- b000021 | keywords | pages [1] -->
Keywords: Cybersecurity; Hierarchical Interaction Scoring Regression Model; Log-

<!-- b000022 | prose | pages [1] -->
Enhanced Quadratic Regression Model

<!-- b000023 | furniture | pages [3] -->
Team # 2521039

<!-- b000024 | furniture | pages [3] -->
Page 3 of 25

<!-- b000025 | prose | pages [3] -->
1

<!-- b000026 | heading | pages [3] -->
Introduction

<!-- b000027 | prose | pages [3] -->
1.1 Background of the Issue

<!-- b000028 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000029 | prose | pages [3] -->
With the advancement of the digital wave, cyberspace has become a critical do-

<!-- b000030 | prose | pages [3] -->
[1] Information technology has

<!-- b000031 | prose | pages [3] -->
main for global economy, society, and national security.

<!-- b000032 | prose | pages [3] -->
signiﬁcantly fostered economic development, enabling people to conduct transactions and make purchases online, beyond traditional in-person and face-to-face exchanges. For instance, platforms such as Tmall, Taobao, and JD.com in China, and Amazon in the United States, provide sellers with a marketplace and offer buyers a more diverse

<!-- b000033 | prose | pages [3] -->
[2] However, we are also facing an unprecedented situation in a cen-

<!-- b000034 | prose | pages [3] -->
range of options.

<!-- b000035 | prose | pages [3] -->
tury the severe global security landscape poses serious threats to countries worldwide. Due to conﬂicts over political and jurisdictional issues between different countries and

<!-- b000036 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000037 | prose | pages [3] -->
the protection of corporate reputation by various enterprises, combating cybercrime is challenging. Different countries have adopted distinct national cybersecurity poli- cies and measures aimed at combating cybercrime. The International Telecommunica- tion Union (ITU), an agency of the United Nations, leads global cooperation and sets standards for cybersecurity assessments, aiding in measuring global cyber information security.

<!-- b000038 | caption | pages [3] -->
Figure 1: 2022 INTERPOL Global Crime Trend Summary Report

<!-- b000039 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000040 | prose | pages [3] -->
By summarizing the ﬁndings of existing research, our team aims to address the following problems:

<!-- b000041 | prose | pages [3] -->
• Investigate the global cybercrime distribution and identify which countries are the primary targets of such activities.

<!-- b000042 | prose | pages [3] -->
• Analyze the success rate, thwart rate, reporting rate, and prosecution rate of cy- bercrimes across different countries to uncover potential patterns or trends.

<!-- b000043 | prose | pages [3] -->
• Based on the distribution data of cybercrime, collect and analyze national secu- rity policies and construct models to evaluate the effectiveness of these policies.

<!-- b000044 | prose | pages [3] -->
• Examine the correlation between national demographic data (e.g., GDP, educa- tion levels) and the distribution of cybercrime, thereby further advancing theo- retical research.

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
• Provide recommendations for improving national policy-making and cybersecu-

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
rity development based on the ﬁndings of existing studies.

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

<!-- b000320 | prose | pages [3] -->
m

<!-- b000321 | prose | pages [3] -->
m

<!-- b000322 | prose | pages [3] -->
m

<!-- b000323 | prose | pages [3] -->
m

<!-- b000324 | prose | pages [3] -->
m

<!-- b000325 | prose | pages [3] -->
m

<!-- b000326 | prose | pages [3] -->
m

<!-- b000327 | prose | pages [3] -->
m

<!-- b000328 | prose | pages [3] -->
m

<!-- b000329 | prose | pages [3] -->
m

<!-- b000330 | prose | pages [3] -->
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

<!-- b000723 | furniture | pages [3] -->
m

<!-- b000724 | furniture | pages [3] -->
m

<!-- b000725 | furniture | pages [3] -->
m

<!-- b000726 | furniture | pages [3] -->
m

<!-- b000727 | furniture | pages [3] -->
m

<!-- b000728 | furniture | pages [3] -->
m

<!-- b000729 | furniture | pages [3] -->
m

<!-- b000730 | furniture | pages [3] -->
m

<!-- b000731 | furniture | pages [3] -->
m

<!-- b000732 | furniture | pages [3] -->
m

<!-- b000733 | furniture | pages [3] -->
m

<!-- b000734 | furniture | pages [4] -->
m

<!-- b000735 | furniture | pages [4] -->
m

<!-- b000736 | furniture | pages [4] -->
m

<!-- b000737 | furniture | pages [4] -->
m

<!-- b000738 | furniture | pages [4] -->
m

<!-- b000739 | furniture | pages [4] -->
m

<!-- b000740 | furniture | pages [4] -->
m

<!-- b000741 | furniture | pages [4] -->
m

<!-- b000742 | furniture | pages [4] -->
m

<!-- b000743 | furniture | pages [4] -->
m

<!-- b000744 | furniture | pages [4] -->
m

<!-- b000745 | furniture | pages [4] -->
m

<!-- b000746 | furniture | pages [4] -->
m

<!-- b000747 | furniture | pages [4] -->
m

<!-- b000748 | furniture | pages [4] -->
m

<!-- b000749 | furniture | pages [4] -->
m

<!-- b000750 | furniture | pages [4] -->
m

<!-- b000751 | furniture | pages [4] -->
m

<!-- b000752 | furniture | pages [4] -->
m

<!-- b000753 | furniture | pages [4] -->
m

<!-- b000754 | furniture | pages [4] -->
m

<!-- b000755 | furniture | pages [4] -->
m

<!-- b000756 | furniture | pages [4] -->
m

<!-- b000757 | furniture | pages [4] -->
m

<!-- b000758 | furniture | pages [4] -->
m

<!-- b000759 | furniture | pages [4] -->
m

<!-- b000760 | furniture | pages [4] -->
m

<!-- b000761 | furniture | pages [4] -->
m

<!-- b000762 | furniture | pages [4] -->
m

<!-- b000763 | furniture | pages [4] -->
m

<!-- b000764 | furniture | pages [4] -->
m

<!-- b000765 | furniture | pages [4] -->
m

<!-- b000766 | furniture | pages [4] -->
m

<!-- b000767 | furniture | pages [4] -->
m

<!-- b000768 | furniture | pages [4] -->
m

<!-- b000769 | furniture | pages [4] -->
m

<!-- b000770 | furniture | pages [4] -->
m

<!-- b000771 | furniture | pages [4] -->
m

<!-- b000772 | furniture | pages [4] -->
m

<!-- b000773 | furniture | pages [4] -->
m

<!-- b000774 | furniture | pages [4] -->
m

<!-- b000775 | furniture | pages [4] -->
m

<!-- b000776 | furniture | pages [4] -->
m

<!-- b000777 | furniture | pages [4] -->
m

<!-- b000778 | furniture | pages [4] -->
m

<!-- b000779 | furniture | pages [4] -->
m

<!-- b000780 | furniture | pages [4] -->
m

<!-- b000781 | furniture | pages [4] -->
m

<!-- b000782 | furniture | pages [4] -->
m

<!-- b000783 | furniture | pages [4] -->
m

<!-- b000784 | furniture | pages [4] -->
m

<!-- b000785 | furniture | pages [4] -->
m

<!-- b000786 | furniture | pages [4] -->
m

<!-- b000787 | furniture | pages [4] -->
m

<!-- b000788 | furniture | pages [4] -->
m

<!-- b000789 | furniture | pages [4] -->
m

<!-- b000790 | furniture | pages [4] -->
m

<!-- b000791 | furniture | pages [4] -->
m

<!-- b000792 | furniture | pages [4] -->
m

<!-- b000793 | furniture | pages [4] -->
m

<!-- b000794 | furniture | pages [4] -->
m

<!-- b000795 | furniture | pages [4] -->
m

<!-- b000796 | furniture | pages [4] -->
m

<!-- b000797 | furniture | pages [4] -->
m

<!-- b000798 | furniture | pages [4] -->
m

<!-- b000799 | furniture | pages [4] -->
m

<!-- b000800 | furniture | pages [4] -->
m

<!-- b000801 | furniture | pages [4] -->
m

<!-- b000802 | furniture | pages [4] -->
m

<!-- b000803 | furniture | pages [4] -->
m

<!-- b000804 | furniture | pages [4] -->
m

<!-- b000805 | furniture | pages [4] -->
m

<!-- b000806 | furniture | pages [4] -->
m

<!-- b000807 | furniture | pages [4] -->
m

<!-- b000808 | furniture | pages [4] -->
m

<!-- b000809 | furniture | pages [4] -->
m

<!-- b000810 | furniture | pages [4] -->
m

<!-- b000811 | furniture | pages [4] -->
m

<!-- b000812 | furniture | pages [4] -->
m

<!-- b000813 | furniture | pages [4] -->
m

<!-- b000814 | furniture | pages [4] -->
m

<!-- b000815 | furniture | pages [4] -->
m

<!-- b000816 | furniture | pages [4] -->
m

<!-- b000817 | furniture | pages [4] -->
m

<!-- b000818 | furniture | pages [4] -->
m

<!-- b000819 | furniture | pages [4] -->
m

<!-- b000820 | furniture | pages [4] -->
m

<!-- b000821 | furniture | pages [4] -->
m

<!-- b000822 | furniture | pages [4] -->
m

<!-- b000823 | furniture | pages [4] -->
m

<!-- b000824 | furniture | pages [4] -->
m

<!-- b000825 | furniture | pages [4] -->
m

<!-- b000826 | furniture | pages [4] -->
m

<!-- b000827 | furniture | pages [4] -->
m

<!-- b000828 | furniture | pages [4] -->
m

<!-- b000829 | furniture | pages [4] -->
m

<!-- b000830 | furniture | pages [4] -->
m

<!-- b000831 | furniture | pages [4] -->
m

<!-- b000832 | furniture | pages [4] -->
m

<!-- b000833 | furniture | pages [4] -->
m

<!-- b000834 | furniture | pages [4] -->
m

<!-- b000835 | furniture | pages [4] -->
m

<!-- b000836 | furniture | pages [4] -->
m

<!-- b000837 | furniture | pages [4] -->
m

<!-- b000838 | furniture | pages [4] -->
m

<!-- b000839 | furniture | pages [4] -->
m

<!-- b000840 | furniture | pages [4] -->
m

<!-- b000841 | furniture | pages [4] -->
m

<!-- b000842 | furniture | pages [4] -->
m

<!-- b000843 | furniture | pages [4] -->
m

<!-- b000844 | furniture | pages [4] -->
m

<!-- b000845 | furniture | pages [4] -->
m

<!-- b000846 | furniture | pages [4] -->
m

<!-- b000847 | furniture | pages [4] -->
m

<!-- b000848 | furniture | pages [4] -->
m

<!-- b000849 | furniture | pages [4] -->
m

<!-- b000850 | furniture | pages [4] -->
m

<!-- b000851 | furniture | pages [4] -->
m

<!-- b000852 | furniture | pages [4] -->
m

<!-- b000853 | furniture | pages [4] -->
m

<!-- b000854 | furniture | pages [4] -->
m

<!-- b000855 | furniture | pages [4] -->
m

<!-- b000856 | furniture | pages [4] -->
m

<!-- b000857 | furniture | pages [4] -->
m

<!-- b000858 | furniture | pages [4] -->
m

<!-- b000859 | furniture | pages [4] -->
m

<!-- b000860 | furniture | pages [4] -->
m

<!-- b000861 | furniture | pages [4] -->
m

<!-- b000862 | furniture | pages [4] -->
m

<!-- b000863 | furniture | pages [4] -->
m

<!-- b000864 | furniture | pages [4] -->
m

<!-- b000865 | furniture | pages [4] -->
m

<!-- b000866 | furniture | pages [4] -->
m

<!-- b000867 | furniture | pages [4] -->
m

<!-- b000868 | furniture | pages [4] -->
m

<!-- b000869 | furniture | pages [4] -->
m

<!-- b000870 | furniture | pages [4] -->
m

<!-- b000871 | furniture | pages [4] -->
m

<!-- b000872 | furniture | pages [4] -->
m

<!-- b000873 | furniture | pages [4] -->
m

<!-- b000874 | furniture | pages [4] -->
m

<!-- b000875 | furniture | pages [4] -->
m

<!-- b000876 | furniture | pages [4] -->
m

<!-- b000877 | furniture | pages [4] -->
m

<!-- b000878 | furniture | pages [4] -->
m

<!-- b000879 | furniture | pages [4] -->
m

<!-- b000880 | furniture | pages [4] -->
m

<!-- b000881 | furniture | pages [4] -->
m

<!-- b000882 | furniture | pages [4] -->
m

<!-- b000883 | furniture | pages [4] -->
m

<!-- b000884 | furniture | pages [4] -->
m

<!-- b000885 | furniture | pages [4] -->
m

<!-- b000886 | furniture | pages [4] -->
m

<!-- b000887 | furniture | pages [4] -->
m

<!-- b000888 | furniture | pages [4] -->
m

<!-- b000889 | furniture | pages [4] -->
m

<!-- b000890 | furniture | pages [4] -->
m

<!-- b000891 | furniture | pages [4] -->
m

<!-- b000892 | furniture | pages [4] -->
m

<!-- b000893 | furniture | pages [4] -->
m

<!-- b000894 | furniture | pages [4] -->
m

<!-- b000895 | furniture | pages [4] -->
m

<!-- b000896 | furniture | pages [4] -->
m

<!-- b000897 | furniture | pages [4] -->
m

<!-- b000898 | furniture | pages [4] -->
m

<!-- b000899 | furniture | pages [4] -->
m

<!-- b000900 | furniture | pages [4] -->
m

<!-- b000901 | furniture | pages [4] -->
m

<!-- b000902 | furniture | pages [4] -->
Team # 2521039

<!-- b000903 | furniture | pages [4] -->
m

<!-- b000904 | furniture | pages [4] -->
m

<!-- b000905 | furniture | pages [4] -->
m

<!-- b000906 | furniture | pages [4] -->
m

<!-- b000907 | furniture | pages [4] -->
m

<!-- b000908 | furniture | pages [4] -->
m

<!-- b000909 | furniture | pages [4] -->
m

<!-- b000910 | furniture | pages [4] -->
m

<!-- b000911 | furniture | pages [4] -->
m

<!-- b000912 | furniture | pages [4] -->
m

<!-- b000913 | furniture | pages [4] -->
m

<!-- b000914 | furniture | pages [4] -->
m

<!-- b000915 | furniture | pages [4] -->
m

<!-- b000916 | furniture | pages [4] -->
m

<!-- b000917 | furniture | pages [4] -->
m

<!-- b000918 | furniture | pages [4] -->
m

<!-- b000919 | furniture | pages [4] -->
m

<!-- b000920 | furniture | pages [4] -->
m

<!-- b000921 | furniture | pages [4] -->
m

<!-- b000922 | furniture | pages [4] -->
m

<!-- b000923 | furniture | pages [4] -->
m

<!-- b000924 | furniture | pages [4] -->
m

<!-- b000925 | furniture | pages [4] -->
m

<!-- b000926 | furniture | pages [4] -->
m

<!-- b000927 | furniture | pages [4] -->
m

<!-- b000928 | furniture | pages [4] -->
m

<!-- b000929 | furniture | pages [4] -->
m

<!-- b000930 | furniture | pages [4] -->
m

<!-- b000931 | furniture | pages [4] -->
m

<!-- b000932 | furniture | pages [4] -->
m

<!-- b000933 | furniture | pages [4] -->
m

<!-- b000934 | furniture | pages [4] -->
m

<!-- b000935 | furniture | pages [4] -->
m

<!-- b000936 | furniture | pages [4] -->
m

<!-- b000937 | furniture | pages [4] -->
m

<!-- b000938 | furniture | pages [4] -->
m

<!-- b000939 | furniture | pages [4] -->
m

<!-- b000940 | furniture | pages [4] -->
m

<!-- b000941 | furniture | pages [4] -->
m

<!-- b000942 | furniture | pages [4] -->
m

<!-- b000943 | furniture | pages [4] -->
m

<!-- b000944 | furniture | pages [4] -->
m

<!-- b000945 | furniture | pages [4] -->
m

<!-- b000946 | furniture | pages [4] -->
m

<!-- b000947 | furniture | pages [4] -->
m

<!-- b000948 | furniture | pages [4] -->
m

<!-- b000949 | furniture | pages [4] -->
m

<!-- b000950 | furniture | pages [4] -->
m

<!-- b000951 | furniture | pages [4] -->
m

<!-- b000952 | furniture | pages [4] -->
m

<!-- b000953 | furniture | pages [4] -->
m

<!-- b000954 | furniture | pages [4] -->
m

<!-- b000955 | furniture | pages [4] -->
m

<!-- b000956 | furniture | pages [4] -->
m

<!-- b000957 | furniture | pages [4] -->
m

<!-- b000958 | furniture | pages [4] -->
m

<!-- b000959 | furniture | pages [4] -->
m

<!-- b000960 | furniture | pages [4] -->
m

<!-- b000961 | furniture | pages [4] -->
m

<!-- b000962 | furniture | pages [4] -->
m

<!-- b000963 | furniture | pages [4] -->
m

<!-- b000964 | furniture | pages [4] -->
m

<!-- b000965 | furniture | pages [4] -->
m

<!-- b000966 | furniture | pages [4] -->
m

<!-- b000967 | furniture | pages [4] -->
m

<!-- b000968 | furniture | pages [4] -->
m

<!-- b000969 | furniture | pages [4] -->
m

<!-- b000970 | furniture | pages [4] -->
m

<!-- b000971 | furniture | pages [4] -->
m

<!-- b000972 | furniture | pages [4] -->
m

<!-- b000973 | furniture | pages [4] -->
m

<!-- b000974 | furniture | pages [4] -->
m

<!-- b000975 | furniture | pages [4] -->
m

<!-- b000976 | furniture | pages [4] -->
m

<!-- b000977 | furniture | pages [4] -->
m

<!-- b000978 | furniture | pages [4] -->
m

<!-- b000979 | furniture | pages [4] -->
m

<!-- b000980 | furniture | pages [4] -->
m

<!-- b000981 | furniture | pages [4] -->
m

<!-- b000982 | furniture | pages [4] -->
m

<!-- b000983 | furniture | pages [4] -->
m

<!-- b000984 | furniture | pages [4] -->
m

<!-- b000985 | furniture | pages [4] -->
m

<!-- b000986 | furniture | pages [4] -->
m

<!-- b000987 | furniture | pages [4] -->
m

<!-- b000988 | furniture | pages [4] -->
m

<!-- b000989 | furniture | pages [4] -->
m

<!-- b000990 | furniture | pages [4] -->
m

<!-- b000991 | furniture | pages [4] -->
m

<!-- b000992 | furniture | pages [4] -->
m

<!-- b000993 | furniture | pages [4] -->
m

<!-- b000994 | furniture | pages [4] -->
m

<!-- b000995 | furniture | pages [4] -->
m

<!-- b000996 | furniture | pages [4] -->
m

<!-- b000997 | furniture | pages [4] -->
m

<!-- b000998 | furniture | pages [4] -->
m

<!-- b000999 | furniture | pages [4] -->
m

<!-- b001000 | furniture | pages [4] -->
m

<!-- b001001 | furniture | pages [4] -->
m

<!-- b001002 | furniture | pages [4] -->
m

<!-- b001003 | furniture | pages [4] -->
m

<!-- b001004 | furniture | pages [4] -->
m

<!-- b001005 | furniture | pages [4] -->
m

<!-- b001006 | furniture | pages [4] -->
m

<!-- b001007 | furniture | pages [4] -->
m

<!-- b001008 | furniture | pages [4] -->
m

<!-- b001009 | furniture | pages [4] -->
m

<!-- b001010 | furniture | pages [4] -->
m

<!-- b001011 | furniture | pages [4] -->
m

<!-- b001012 | furniture | pages [4] -->
m

<!-- b001013 | furniture | pages [4] -->
m

<!-- b001014 | furniture | pages [4] -->
m

<!-- b001015 | furniture | pages [4] -->
m

<!-- b001016 | furniture | pages [4] -->
m

<!-- b001017 | furniture | pages [4] -->
m

<!-- b001018 | furniture | pages [4] -->
m

<!-- b001019 | furniture | pages [4] -->
m

<!-- b001020 | furniture | pages [4] -->
m

<!-- b001021 | furniture | pages [4] -->
m

<!-- b001022 | furniture | pages [4] -->
m

<!-- b001023 | furniture | pages [4] -->
m

<!-- b001024 | furniture | pages [4] -->
m

<!-- b001025 | furniture | pages [4] -->
m

<!-- b001026 | furniture | pages [4] -->
m

<!-- b001027 | furniture | pages [4] -->
m

<!-- b001028 | furniture | pages [4] -->
m

<!-- b001029 | furniture | pages [4] -->
m

<!-- b001030 | furniture | pages [4] -->
m

<!-- b001031 | furniture | pages [4] -->
m

<!-- b001032 | furniture | pages [4] -->
m

<!-- b001033 | furniture | pages [4] -->
m

<!-- b001034 | furniture | pages [4] -->
m

<!-- b001035 | furniture | pages [4] -->
m

<!-- b001036 | furniture | pages [4] -->
m

<!-- b001037 | furniture | pages [4] -->
m

<!-- b001038 | furniture | pages [4] -->
m

<!-- b001039 | furniture | pages [4] -->
m

<!-- b001040 | furniture | pages [4] -->
m

<!-- b001041 | furniture | pages [4] -->
m

<!-- b001042 | furniture | pages [4] -->
m

<!-- b001043 | furniture | pages [4] -->
m

<!-- b001044 | furniture | pages [4] -->
m

<!-- b001045 | furniture | pages [4] -->
m

<!-- b001046 | furniture | pages [4] -->
m

<!-- b001047 | furniture | pages [4] -->
m

<!-- b001048 | furniture | pages [4] -->
m

<!-- b001049 | furniture | pages [4] -->
m

<!-- b001050 | furniture | pages [4] -->
m

<!-- b001051 | furniture | pages [4] -->
m

<!-- b001052 | furniture | pages [4] -->
m

<!-- b001053 | furniture | pages [4] -->
m

<!-- b001054 | furniture | pages [4] -->
m

<!-- b001055 | furniture | pages [4] -->
m

<!-- b001056 | furniture | pages [4] -->
m

<!-- b001057 | furniture | pages [4] -->
m

<!-- b001058 | furniture | pages [4] -->
m

<!-- b001059 | furniture | pages [4] -->
m

<!-- b001060 | furniture | pages [4] -->
m

<!-- b001061 | furniture | pages [4] -->
m

<!-- b001062 | furniture | pages [4] -->
m

<!-- b001063 | furniture | pages [4] -->
m

<!-- b001064 | furniture | pages [4] -->
m

<!-- b001065 | furniture | pages [4] -->
m

<!-- b001066 | furniture | pages [4] -->
m

<!-- b001067 | furniture | pages [4] -->
m

<!-- b001068 | furniture | pages [4] -->
m

<!-- b001069 | furniture | pages [4] -->
m

<!-- b001070 | furniture | pages [4] -->
m

<!-- b001071 | furniture | pages [4] -->
m

<!-- b001072 | furniture | pages [4] -->
m

<!-- b001073 | furniture | pages [4] -->
m

<!-- b001074 | furniture | pages [4] -->
m

<!-- b001075 | furniture | pages [4] -->
m

<!-- b001076 | furniture | pages [4] -->
m

<!-- b001077 | furniture | pages [4] -->
m

<!-- b001078 | furniture | pages [4] -->
m

<!-- b001079 | furniture | pages [4] -->
m

<!-- b001080 | furniture | pages [4] -->
m

<!-- b001081 | furniture | pages [4] -->
m

<!-- b001082 | furniture | pages [4] -->
m

<!-- b001083 | furniture | pages [4] -->
m

<!-- b001084 | furniture | pages [4] -->
m

<!-- b001085 | furniture | pages [4] -->
m

<!-- b001086 | furniture | pages [4] -->
m

<!-- b001087 | furniture | pages [4] -->
m

<!-- b001088 | furniture | pages [4] -->
m

<!-- b001089 | furniture | pages [4] -->
m

<!-- b001090 | furniture | pages [4] -->
m

<!-- b001091 | furniture | pages [4] -->
m

<!-- b001092 | furniture | pages [4] -->
m

<!-- b001093 | furniture | pages [4] -->
m

<!-- b001094 | furniture | pages [4] -->
m

<!-- b001095 | furniture | pages [4] -->
m

<!-- b001096 | furniture | pages [4] -->
m

<!-- b001097 | furniture | pages [4] -->
m

<!-- b001098 | furniture | pages [4] -->
m

<!-- b001099 | furniture | pages [4] -->
m

<!-- b001100 | furniture | pages [4] -->
m

<!-- b001101 | furniture | pages [4] -->
m

<!-- b001102 | furniture | pages [4] -->
m

<!-- b001103 | furniture | pages [4] -->
m

<!-- b001104 | furniture | pages [4] -->
m

<!-- b001105 | furniture | pages [4] -->
m

<!-- b001106 | furniture | pages [4] -->
m

<!-- b001107 | furniture | pages [4] -->
m

<!-- b001108 | furniture | pages [4] -->
m

<!-- b001109 | furniture | pages [4] -->
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
m

<!-- b001115 | prose | pages [4] -->
m

<!-- b001116 | prose | pages [4] -->
m

<!-- b001117 | prose | pages [4] -->
m

<!-- b001118 | prose | pages [4] -->
m

<!-- b001119 | prose | pages [4] -->
m

<!-- b001120 | prose | pages [4] -->
m

<!-- b001121 | prose | pages [4] -->
m

<!-- b001122 | prose | pages [4] -->
m

<!-- b001123 | prose | pages [4] -->
m

<!-- b001124 | prose | pages [4] -->
m

<!-- b001125 | prose | pages [4] -->
m

<!-- b001126 | prose | pages [4] -->
m

<!-- b001127 | prose | pages [4] -->
m

<!-- b001128 | prose | pages [4] -->
m

<!-- b001129 | prose | pages [4] -->
m

<!-- b001130 | prose | pages [4] -->
m

<!-- b001131 | prose | pages [4] -->
m

<!-- b001132 | prose | pages [4] -->
m

<!-- b001133 | prose | pages [4] -->
m

<!-- b001134 | prose | pages [4] -->
m

<!-- b001135 | prose | pages [4] -->
m

<!-- b001136 | prose | pages [4] -->
m

<!-- b001137 | prose | pages [4] -->
m

<!-- b001138 | prose | pages [4] -->
m

<!-- b001139 | prose | pages [4] -->
m

<!-- b001140 | prose | pages [4] -->
m

<!-- b001141 | prose | pages [4] -->
m

<!-- b001142 | prose | pages [4] -->
m

<!-- b001143 | prose | pages [4] -->
m

<!-- b001144 | prose | pages [4] -->
m

<!-- b001145 | prose | pages [4] -->
m

<!-- b001146 | prose | pages [4] -->
m

<!-- b001147 | prose | pages [4] -->
m

<!-- b001148 | prose | pages [4] -->
m

<!-- b001149 | prose | pages [4] -->
m

<!-- b001150 | prose | pages [4] -->
m

<!-- b001151 | prose | pages [4] -->
m

<!-- b001152 | prose | pages [4] -->
m

<!-- b001153 | prose | pages [4] -->
m

<!-- b001154 | prose | pages [4] -->
m

<!-- b001155 | prose | pages [4] -->
m

<!-- b001156 | prose | pages [4] -->
m

<!-- b001157 | prose | pages [4] -->
m

<!-- b001158 | prose | pages [4] -->
m

<!-- b001159 | prose | pages [4] -->
m

<!-- b001160 | prose | pages [4] -->
m

<!-- b001161 | prose | pages [4] -->
m

<!-- b001162 | prose | pages [4] -->
1.3 Our Work

<!-- b001163 | prose | pages [4] -->
m

<!-- b001164 | prose | pages [4] -->
m

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

<!-- b001239 | furniture | pages [4] -->
m

<!-- b001240 | furniture | pages [4] -->
m

<!-- b001241 | furniture | pages [4] -->
m

<!-- b001242 | furniture | pages [4] -->
m

<!-- b001243 | furniture | pages [4] -->
m

<!-- b001244 | furniture | pages [4] -->
m

<!-- b001245 | furniture | pages [4] -->
m

<!-- b001246 | furniture | pages [4] -->
m

<!-- b001247 | furniture | pages [4] -->
m

<!-- b001248 | furniture | pages [4] -->
m

<!-- b001249 | furniture | pages [4] -->
m

<!-- b001250 | furniture | pages [4] -->
m

<!-- b001251 | furniture | pages [4] -->
m

<!-- b001252 | furniture | pages [4] -->
m

<!-- b001253 | furniture | pages [4] -->
m

<!-- b001254 | furniture | pages [4] -->
m

<!-- b001255 | furniture | pages [4] -->
m

<!-- b001256 | furniture | pages [4] -->
m

<!-- b001257 | furniture | pages [4] -->
m

<!-- b001258 | furniture | pages [4] -->
m

<!-- b001259 | furniture | pages [4] -->
m

<!-- b001260 | furniture | pages [4] -->
m

<!-- b001261 | furniture | pages [4] -->
m

<!-- b001262 | furniture | pages [4] -->
m

<!-- b001263 | furniture | pages [4] -->
m

<!-- b001264 | furniture | pages [4] -->
m

<!-- b001265 | furniture | pages [4] -->
m

<!-- b001266 | furniture | pages [4] -->
m

<!-- b001267 | furniture | pages [4] -->
m

<!-- b001268 | furniture | pages [4] -->
m

<!-- b001269 | furniture | pages [4] -->
m

<!-- b001270 | furniture | pages [4] -->
m

<!-- b001271 | furniture | pages [4] -->
m

<!-- b001272 | furniture | pages [4] -->
m

<!-- b001273 | furniture | pages [4] -->
m

<!-- b001274 | furniture | pages [4] -->
m

<!-- b001275 | furniture | pages [4] -->
m

<!-- b001276 | furniture | pages [4] -->
m

<!-- b001277 | furniture | pages [4] -->
m

<!-- b001278 | furniture | pages [4] -->
m

<!-- b001279 | furniture | pages [4] -->
m

<!-- b001280 | furniture | pages [4] -->
m

<!-- b001281 | furniture | pages [4] -->
m

<!-- b001282 | furniture | pages [4] -->
m

<!-- b001283 | furniture | pages [4] -->
m

<!-- b001284 | furniture | pages [4] -->
m

<!-- b001285 | furniture | pages [4] -->
m

<!-- b001286 | furniture | pages [4] -->
m

<!-- b001287 | furniture | pages [4] -->
m

<!-- b001288 | furniture | pages [4] -->
m

<!-- b001289 | furniture | pages [4] -->
m

<!-- b001290 | furniture | pages [4] -->
m

<!-- b001291 | furniture | pages [4] -->
m

<!-- b001292 | furniture | pages [4] -->
m

<!-- b001293 | furniture | pages [4] -->
m

<!-- b001294 | furniture | pages [4] -->
m

<!-- b001295 | furniture | pages [4] -->
m

<!-- b001296 | furniture | pages [4] -->
m

<!-- b001297 | furniture | pages [4] -->
m

<!-- b001298 | furniture | pages [4] -->
m

<!-- b001299 | furniture | pages [4] -->
m

<!-- b001300 | furniture | pages [4] -->
m

<!-- b001301 | furniture | pages [4] -->
m

<!-- b001302 | furniture | pages [4] -->
m

<!-- b001303 | furniture | pages [4] -->
m

<!-- b001304 | furniture | pages [4] -->
m

<!-- b001305 | furniture | pages [4] -->
m

<!-- b001306 | furniture | pages [4] -->
m

<!-- b001307 | furniture | pages [4] -->
m

<!-- b001308 | furniture | pages [4] -->
m

<!-- b001309 | furniture | pages [4] -->
m

<!-- b001310 | furniture | pages [4] -->
m

<!-- b001311 | furniture | pages [4] -->
m

<!-- b001312 | furniture | pages [4] -->
m

<!-- b001313 | furniture | pages [4] -->
m

<!-- b001314 | furniture | pages [4] -->
m

<!-- b001315 | furniture | pages [4] -->
m

<!-- b001316 | furniture | pages [4] -->
m

<!-- b001317 | furniture | pages [4] -->
m

<!-- b001318 | furniture | pages [4] -->
m

<!-- b001319 | furniture | pages [4] -->
m

<!-- b001320 | furniture | pages [4] -->
m

<!-- b001321 | furniture | pages [4] -->
m

<!-- b001322 | furniture | pages [4] -->
m

<!-- b001323 | furniture | pages [4] -->
m

<!-- b001324 | furniture | pages [4] -->
m

<!-- b001325 | furniture | pages [4] -->
m

<!-- b001326 | furniture | pages [4] -->
m

<!-- b001327 | furniture | pages [4] -->
m

<!-- b001328 | furniture | pages [4] -->
m

<!-- b001329 | furniture | pages [4] -->
m

<!-- b001330 | furniture | pages [4] -->
m

<!-- b001331 | furniture | pages [4] -->
m

<!-- b001332 | furniture | pages [4] -->
m

<!-- b001333 | furniture | pages [4] -->
m

<!-- b001334 | furniture | pages [4] -->
m

<!-- b001335 | furniture | pages [4] -->
m

<!-- b001336 | furniture | pages [4] -->
m

<!-- b001337 | furniture | pages [4] -->
m

<!-- b001338 | furniture | pages [4] -->
m

<!-- b001339 | furniture | pages [4] -->
m

<!-- b001340 | furniture | pages [4] -->
m

<!-- b001341 | furniture | pages [4] -->
m

<!-- b001342 | furniture | pages [4] -->
m

<!-- b001343 | furniture | pages [4] -->
m

<!-- b001344 | furniture | pages [4] -->
m

<!-- b001345 | furniture | pages [4] -->
m

<!-- b001346 | furniture | pages [4] -->
m

<!-- b001347 | furniture | pages [4] -->
m

<!-- b001348 | furniture | pages [4] -->
m

<!-- b001349 | furniture | pages [4] -->
m

<!-- b001350 | furniture | pages [4] -->
m

<!-- b001351 | furniture | pages [4] -->
m

<!-- b001352 | furniture | pages [4] -->
m

<!-- b001353 | furniture | pages [4] -->
m

<!-- b001354 | furniture | pages [4] -->
m

<!-- b001355 | furniture | pages [4] -->
m

<!-- b001356 | furniture | pages [4] -->
m

<!-- b001357 | furniture | pages [4] -->
Page 4 of 25

<!-- b001358 | furniture | pages [4] -->
m

<!-- b001359 | furniture | pages [4] -->
m

<!-- b001360 | furniture | pages [4] -->
m

<!-- b001361 | furniture | pages [4] -->
m

<!-- b001362 | furniture | pages [4] -->
m

<!-- b001363 | furniture | pages [4] -->
m

<!-- b001364 | furniture | pages [4] -->
m

<!-- b001365 | furniture | pages [4] -->
m

<!-- b001366 | furniture | pages [4] -->
m

<!-- b001367 | furniture | pages [4] -->
m

<!-- b001368 | furniture | pages [4] -->
m

<!-- b001369 | furniture | pages [4] -->
m

<!-- b001370 | furniture | pages [4] -->
m

<!-- b001371 | furniture | pages [4] -->
m

<!-- b001372 | furniture | pages [4] -->
m

<!-- b001373 | furniture | pages [4] -->
m

<!-- b001374 | furniture | pages [4] -->
m

<!-- b001375 | furniture | pages [4] -->
m

<!-- b001376 | furniture | pages [4] -->
m

<!-- b001377 | furniture | pages [4] -->
m

<!-- b001378 | furniture | pages [4] -->
m

<!-- b001379 | furniture | pages [4] -->
m

<!-- b001380 | furniture | pages [4] -->
m

<!-- b001381 | furniture | pages [4] -->
m

<!-- b001382 | furniture | pages [4] -->
m

<!-- b001383 | furniture | pages [4] -->
m

<!-- b001384 | furniture | pages [4] -->
m

<!-- b001385 | furniture | pages [4] -->
m

<!-- b001386 | furniture | pages [4] -->
m

<!-- b001387 | furniture | pages [4] -->
m

<!-- b001388 | furniture | pages [4] -->
m

<!-- b001389 | furniture | pages [4] -->
m

<!-- b001390 | furniture | pages [4] -->
m

<!-- b001391 | furniture | pages [4] -->
m

<!-- b001392 | furniture | pages [4] -->
m

<!-- b001393 | furniture | pages [4] -->
m

<!-- b001394 | furniture | pages [4] -->
m

<!-- b001395 | furniture | pages [4] -->
m

<!-- b001396 | furniture | pages [4] -->
m

<!-- b001397 | furniture | pages [4] -->
m

<!-- b001398 | furniture | pages [4] -->
m

<!-- b001399 | furniture | pages [4] -->
m

<!-- b001400 | furniture | pages [4] -->
m

<!-- b001401 | furniture | pages [4] -->
m

<!-- b001402 | furniture | pages [4] -->
m

<!-- b001403 | furniture | pages [4] -->
m

<!-- b001404 | furniture | pages [4] -->
m

<!-- b001405 | furniture | pages [4] -->
m

<!-- b001406 | furniture | pages [4] -->
m

<!-- b001407 | furniture | pages [4] -->
m

<!-- b001408 | furniture | pages [4] -->
m

<!-- b001409 | furniture | pages [4] -->
m

<!-- b001410 | furniture | pages [4] -->
m

<!-- b001411 | furniture | pages [4] -->
m

<!-- b001412 | furniture | pages [4] -->
m

<!-- b001413 | furniture | pages [4] -->
m

<!-- b001414 | furniture | pages [4] -->
m

<!-- b001415 | furniture | pages [4] -->
m

<!-- b001416 | furniture | pages [4] -->
m

<!-- b001417 | furniture | pages [4] -->
m

<!-- b001418 | furniture | pages [4] -->
m

<!-- b001419 | furniture | pages [4] -->
m

<!-- b001420 | furniture | pages [4] -->
m

<!-- b001421 | furniture | pages [4] -->
m

<!-- b001422 | furniture | pages [4] -->
m

<!-- b001423 | furniture | pages [4] -->
m

<!-- b001424 | furniture | pages [4] -->
m

<!-- b001425 | furniture | pages [4] -->
m

<!-- b001426 | furniture | pages [4] -->
m

<!-- b001427 | furniture | pages [4] -->
m

<!-- b001428 | furniture | pages [4] -->
m

<!-- b001429 | furniture | pages [4] -->
m

<!-- b001430 | furniture | pages [4] -->
m

<!-- b001431 | furniture | pages [4] -->
m

<!-- b001432 | furniture | pages [4] -->
m

<!-- b001433 | furniture | pages [4] -->
m

<!-- b001434 | furniture | pages [4] -->
m

<!-- b001435 | furniture | pages [4] -->
m

<!-- b001436 | furniture | pages [4] -->
m

<!-- b001437 | furniture | pages [4] -->
m

<!-- b001438 | furniture | pages [4] -->
m

<!-- b001439 | furniture | pages [4] -->
m

<!-- b001440 | furniture | pages [4] -->
m

<!-- b001441 | furniture | pages [4] -->
m

<!-- b001442 | furniture | pages [4] -->
m

<!-- b001443 | furniture | pages [4] -->
m

<!-- b001444 | furniture | pages [4] -->
m

<!-- b001445 | furniture | pages [4] -->
m

<!-- b001446 | furniture | pages [4] -->
m

<!-- b001447 | furniture | pages [4] -->
m

<!-- b001448 | furniture | pages [4] -->
m

<!-- b001449 | furniture | pages [4] -->
m

<!-- b001450 | furniture | pages [4] -->
m

<!-- b001451 | furniture | pages [4] -->
m

<!-- b001452 | furniture | pages [4] -->
m

<!-- b001453 | furniture | pages [4] -->
m

<!-- b001454 | furniture | pages [4] -->
m

<!-- b001455 | furniture | pages [4] -->
m

<!-- b001456 | furniture | pages [4] -->
m

<!-- b001457 | furniture | pages [4] -->
m

<!-- b001458 | furniture | pages [4] -->
m

<!-- b001459 | furniture | pages [4] -->
m

<!-- b001460 | furniture | pages [4] -->
m

<!-- b001461 | furniture | pages [4] -->
m

<!-- b001462 | furniture | pages [4] -->
m

<!-- b001463 | furniture | pages [4] -->
m

<!-- b001464 | furniture | pages [4] -->
m

<!-- b001465 | furniture | pages [4] -->
m

<!-- b001466 | furniture | pages [4] -->
m

<!-- b001467 | furniture | pages [4] -->
m

<!-- b001468 | furniture | pages [4] -->
m

<!-- b001469 | furniture | pages [4] -->
m

<!-- b001470 | furniture | pages [4] -->
m

<!-- b001471 | furniture | pages [4] -->
m

<!-- b001472 | furniture | pages [4] -->
m

<!-- b001473 | furniture | pages [4] -->
m

<!-- b001474 | furniture | pages [4] -->
m

<!-- b001475 | furniture | pages [4] -->
m

<!-- b001476 | furniture | pages [4] -->
m

<!-- b001477 | furniture | pages [4] -->
m

<!-- b001478 | furniture | pages [4] -->
m

<!-- b001479 | furniture | pages [4] -->
m

<!-- b001480 | furniture | pages [4] -->
m

<!-- b001481 | furniture | pages [4] -->
m

<!-- b001482 | furniture | pages [4] -->
m

<!-- b001483 | furniture | pages [4] -->
m

<!-- b001484 | furniture | pages [4] -->
m

<!-- b001485 | furniture | pages [4] -->
m

<!-- b001486 | furniture | pages [4] -->
m

<!-- b001487 | furniture | pages [4] -->
m

<!-- b001488 | furniture | pages [4] -->
m

<!-- b001489 | furniture | pages [4] -->
m

<!-- b001490 | furniture | pages [4] -->
m

<!-- b001491 | furniture | pages [4] -->
m

<!-- b001492 | furniture | pages [4] -->
m

<!-- b001493 | furniture | pages [4] -->
m

<!-- b001494 | furniture | pages [4] -->
m

<!-- b001495 | furniture | pages [4] -->
m

<!-- b001496 | furniture | pages [4] -->
m

<!-- b001497 | furniture | pages [4] -->
m

<!-- b001498 | furniture | pages [4] -->
m

<!-- b001499 | furniture | pages [4] -->
m

<!-- b001500 | furniture | pages [4] -->
m

<!-- b001501 | furniture | pages [4] -->
m

<!-- b001502 | furniture | pages [4] -->
m

<!-- b001503 | prose | pages [4] -->
m m

<!-- b001504 | prose | pages [4] -->
m m

<!-- b001505 | prose | pages [4] -->
m m

<!-- b001506 | prose | pages [4] -->
m m

<!-- b001507 | prose | pages [4] -->
m

<!-- b001508 | prose | pages [4] -->
m m

<!-- b001509 | prose | pages [4] -->
m m

<!-- b001510 | prose | pages [4] -->
m m

<!-- b001511 | prose | pages [4] -->
m m

<!-- b001512 | prose | pages [4] -->
m m

<!-- b001513 | prose | pages [4] -->
m m

<!-- b001514 | prose | pages [4] -->
m m

<!-- b001515 | prose | pages [4] -->
m

<!-- b001516 | prose | pages [4] -->
m m

<!-- b001517 | prose | pages [4] -->
m m

<!-- b001518 | prose | pages [4] -->
m

<!-- b001519 | prose | pages [4] -->
m m

<!-- b001520 | prose | pages [4] -->
m m

<!-- b001521 | prose | pages [4] -->
m m

<!-- b001522 | prose | pages [4] -->
m m

<!-- b001523 | prose | pages [4] -->
m m

<!-- b001524 | prose | pages [4] -->
m

<!-- b001525 | prose | pages [4] -->
m m

<!-- b001526 | prose | pages [4] -->
m m

<!-- b001527 | prose | pages [4] -->
m m

<!-- b001528 | prose | pages [4] -->
m m

<!-- b001529 | prose | pages [4] -->
m m

<!-- b001530 | prose | pages [4] -->
m

<!-- b001531 | prose | pages [4] -->
m m

<!-- b001532 | prose | pages [4] -->
m m

<!-- b001533 | prose | pages [4] -->
m m

<!-- b001534 | prose | pages [4] -->
m m

<!-- b001535 | prose | pages [4] -->
m m

<!-- b001536 | prose | pages [4] -->
m

<!-- b001537 | prose | pages [4] -->
m m

<!-- b001538 | prose | pages [4] -->
m

<!-- b001539 | prose | pages [4] -->
m m

<!-- b001540 | prose | pages [4] -->
m m

<!-- b001541 | prose | pages [4] -->
m m

<!-- b001542 | prose | pages [4] -->
m m

<!-- b001543 | prose | pages [4] -->
m m

<!-- b001544 | prose | pages [4] -->
m m

<!-- b001545 | prose | pages [4] -->
m

<!-- b001546 | caption | pages [4] -->
Figure 2: Flow Chart of Our Work

<!-- b001547 | heading | pages [4] -->
Assumptions and Justiﬁcations

<!-- b001548 | prose | pages [4] -->
2

<!-- b001549 | prose | pages [4] -->
Assumption 1: Cybercrime statistics are consistent and comparable.

<!-- b001550 | heading | pages [4] -->
▶Justiﬁcations: The data sources (e.g., GCI, VERIS database) are sufﬁ-

<!-- b001551 | prose | pages [4] -->
ciently representative, and differences in national statistics have a neg- ligible impact on the overall analysis.

<!-- b001552 | heading | pages [4] -->
Assumption 2: The economic motives behind cybercrime are consistent with social

<!-- b001553 | prose | pages [4] -->
and cultural factors

<!-- b001554 | prose | pages [4] -->
▶Justiﬁcations: The fundamental motives of global cybercrime (e.g., economic gain, political objectives) are consistent and can be explained using similar economic and social variables.

<!-- b001555 | prose | pages [4] -->
Assumption 3: The inﬂuence of demographic variables is stable in the short term.

<!-- b001556 | prose | pages [4] -->
▶Justiﬁcations: Variables such as internet penetration rate, education level, and economic conditions remain stable during the study period, with short-term changes having a limited impact on the results.

<!-- b001557 | prose | pages [4] -->
关注数学模型

<!-- b001558 | furniture | pages [4] -->
2

<!-- b001559 | furniture | pages [4] -->
MATHmodels

<!-- b001560 | furniture | pages [4] -->
获取更多资讯

<!-- b001561 | furniture | pages [6] -->
Team # 2521039

<!-- b001562 | furniture | pages [6] -->
Page 6 of 25

<!-- b001563 | prose | pages [6] -->
m

<!-- b001564 | prose | pages [6] -->
m

<!-- b001565 | prose | pages [6] -->
m

<!-- b001566 | prose | pages [6] -->
m

<!-- b001567 | prose | pages [6] -->
m

<!-- b001568 | prose | pages [6] -->
m

<!-- b001569 | prose | pages [6] -->
m

<!-- b001570 | prose | pages [6] -->
m

<!-- b001571 | prose | pages [6] -->
m

<!-- b001572 | prose | pages [6] -->
m

<!-- b001573 | prose | pages [6] -->
m

<!-- b001574 | prose | pages [6] -->
m

<!-- b001575 | prose | pages [6] -->
m

<!-- b001576 | prose | pages [6] -->
m

<!-- b001577 | prose | pages [6] -->
m

<!-- b001578 | prose | pages [6] -->
m

<!-- b001579 | prose | pages [6] -->
m

<!-- b001580 | prose | pages [6] -->
m

<!-- b001581 | prose | pages [6] -->
m

<!-- b001582 | prose | pages [6] -->
m

<!-- b001583 | prose | pages [6] -->
m

<!-- b001584 | prose | pages [6] -->
m

<!-- b001585 | prose | pages [6] -->
m

<!-- b001586 | prose | pages [6] -->
m

<!-- b001587 | prose | pages [6] -->
m

<!-- b001588 | prose | pages [6] -->
m

<!-- b001589 | prose | pages [6] -->
m

<!-- b001590 | prose | pages [6] -->
m

<!-- b001591 | prose | pages [6] -->
m

<!-- b001592 | prose | pages [6] -->
m

<!-- b001593 | prose | pages [6] -->
m

<!-- b001594 | prose | pages [6] -->
m

<!-- b001595 | prose | pages [6] -->
m

<!-- b001596 | prose | pages [6] -->
m

<!-- b001597 | prose | pages [6] -->
m

<!-- b001598 | prose | pages [6] -->
m

<!-- b001599 | prose | pages [6] -->
m

<!-- b001600 | prose | pages [6] -->
m

<!-- b001601 | prose | pages [6] -->
m

<!-- b001602 | prose | pages [6] -->
m

<!-- b001603 | prose | pages [6] -->
m

<!-- b001604 | prose | pages [6] -->
m

<!-- b001605 | prose | pages [6] -->
m

<!-- b001606 | prose | pages [6] -->
m

<!-- b001607 | prose | pages [6] -->
m

<!-- b001608 | prose | pages [6] -->
m

<!-- b001609 | prose | pages [6] -->
m

<!-- b001610 | prose | pages [6] -->
m

<!-- b001611 | prose | pages [6] -->
m

<!-- b001612 | prose | pages [6] -->
m

<!-- b001613 | prose | pages [6] -->
m

<!-- b001614 | prose | pages [6] -->
m

<!-- b001615 | prose | pages [6] -->
m

<!-- b001616 | prose | pages [6] -->
m

<!-- b001617 | prose | pages [6] -->
m

<!-- b001618 | prose | pages [6] -->
m

<!-- b001619 | prose | pages [6] -->
m

<!-- b001620 | prose | pages [6] -->
m

<!-- b001621 | prose | pages [6] -->
m

<!-- b001622 | prose | pages [6] -->
m

<!-- b001623 | prose | pages [6] -->
m

<!-- b001624 | prose | pages [6] -->
m

<!-- b001625 | prose | pages [6] -->
m

<!-- b001626 | prose | pages [6] -->
m

<!-- b001627 | prose | pages [6] -->
m

<!-- b001628 | prose | pages [6] -->
m

<!-- b001629 | prose | pages [6] -->
m

<!-- b001630 | prose | pages [6] -->
m

<!-- b001631 | prose | pages [6] -->
m

<!-- b001632 | prose | pages [6] -->
m

<!-- b001633 | prose | pages [6] -->
m

<!-- b001634 | prose | pages [6] -->
m

<!-- b001635 | prose | pages [6] -->
m

<!-- b001636 | caption | pages [6] -->
Table 2: Major Databases and Their Sources

<!-- b001637 | prose | pages [6] -->
m

<!-- b001638 | prose | pages [6] -->
m

<!-- b001639 | prose | pages [6] -->
m

<!-- b001640 | prose | pages [6] -->
m

<!-- b001641 | prose | pages [6] -->
m

<!-- b001642 | prose | pages [6] -->
m

<!-- b001643 | prose | pages [6] -->
m

<!-- b001644 | prose | pages [6] -->
m

<!-- b001645 | prose | pages [6] -->
m

<!-- b001646 | prose | pages [6] -->
m

<!-- b001647 | prose | pages [6] -->
m

<!-- b001648 | prose | pages [6] -->
m

<!-- b001649 | prose | pages [6] -->
m

<!-- b001650 | prose | pages [6] -->
m

<!-- b001651 | prose | pages [6] -->
m

<!-- b001652 | prose | pages [6] -->
m

<!-- b001653 | prose | pages [6] -->
m

<!-- b001654 | prose | pages [6] -->
m

<!-- b001655 | prose | pages [6] -->
m

<!-- b001656 | prose | pages [6] -->
m

<!-- b001657 | prose | pages [6] -->
m

<!-- b001658 | prose | pages [6] -->
m

<!-- b001659 | prose | pages [6] -->
m

<!-- b001660 | prose | pages [6] -->
m

<!-- b001661 | prose | pages [6] -->
m

<!-- b001662 | prose | pages [6] -->
m

<!-- b001663 | prose | pages [6] -->
m

<!-- b001664 | prose | pages [6] -->
m

<!-- b001665 | prose | pages [6] -->
m

<!-- b001666 | prose | pages [6] -->
m

<!-- b001667 | prose | pages [6] -->
m

<!-- b001668 | prose | pages [6] -->
m

<!-- b001669 | prose | pages [6] -->
m

<!-- b001670 | prose | pages [6] -->
m

<!-- b001671 | prose | pages [6] -->
m

<!-- b001672 | prose | pages [6] -->
m

<!-- b001673 | prose | pages [6] -->
m

<!-- b001674 | prose | pages [6] -->
m

<!-- b001675 | prose | pages [6] -->
m

<!-- b001676 | prose | pages [6] -->
m

<!-- b001677 | prose | pages [6] -->
m

<!-- b001678 | prose | pages [6] -->
m

<!-- b001679 | prose | pages [6] -->
m

<!-- b001680 | prose | pages [6] -->
m

<!-- b001681 | prose | pages [6] -->
m

<!-- b001682 | prose | pages [6] -->
m

<!-- b001683 | prose | pages [6] -->
m

<!-- b001684 | prose | pages [6] -->
m

<!-- b001685 | prose | pages [6] -->
m

<!-- b001686 | prose | pages [6] -->
m

<!-- b001687 | prose | pages [6] -->
m

<!-- b001688 | prose | pages [6] -->
m

<!-- b001689 | prose | pages [6] -->
m

<!-- b001690 | prose | pages [6] -->
m

<!-- b001691 | prose | pages [6] -->
m

<!-- b001692 | prose | pages [6] -->
m

<!-- b001693 | prose | pages [6] -->
m

<!-- b001694 | prose | pages [6] -->
m

<!-- b001695 | prose | pages [6] -->
m

<!-- b001696 | prose | pages [6] -->
m

<!-- b001697 | prose | pages [6] -->
m

<!-- b001698 | prose | pages [6] -->
m

<!-- b001699 | prose | pages [6] -->
m

<!-- b001700 | prose | pages [6] -->
m

<!-- b001701 | prose | pages [6] -->
m

<!-- b001702 | prose | pages [6] -->
m

<!-- b001703 | prose | pages [6] -->
m

<!-- b001704 | prose | pages [6] -->
m

<!-- b001705 | prose | pages [6] -->
m

<!-- b001706 | prose | pages [6] -->
m

<!-- b001707 | prose | pages [6] -->
m

<!-- b001708 | prose | pages [6] -->
m

<!-- b001709 | prose | pages [6] -->
m

<!-- b001710 | prose | pages [6] -->
m

<!-- b001711 | prose | pages [6] -->
m

<!-- b001712 | prose | pages [6] -->
m

<!-- b001713 | prose | pages [6] -->
m

<!-- b001714 | prose | pages [6] -->
m

<!-- b001715 | prose | pages [6] -->
m

<!-- b001716 | prose | pages [6] -->
m

<!-- b001717 | prose | pages [6] -->
m

<!-- b001718 | prose | pages [6] -->
m

<!-- b001719 | prose | pages [6] -->
m

<!-- b001720 | prose | pages [6] -->
m

<!-- b001721 | prose | pages [6] -->
m

<!-- b001722 | prose | pages [6] -->
m

<!-- b001723 | prose | pages [6] -->
m

<!-- b001724 | prose | pages [6] -->
m

<!-- b001725 | prose | pages [6] -->
m

<!-- b001726 | prose | pages [6] -->
m

<!-- b001727 | prose | pages [6] -->
m

<!-- b001728 | prose | pages [6] -->
m

<!-- b001729 | prose | pages [6] -->
m

<!-- b001730 | prose | pages [6] -->
m

<!-- b001731 | prose | pages [6] -->
m

<!-- b001732 | prose | pages [6] -->
m

<!-- b001733 | prose | pages [6] -->
m

<!-- b001734 | prose | pages [6] -->
m

<!-- b001735 | prose | pages [6] -->
m

<!-- b001736 | prose | pages [6] -->
m

<!-- b001737 | prose | pages [6] -->
m

<!-- b001738 | prose | pages [6] -->
m

<!-- b001739 | prose | pages [6] -->
m

<!-- b001740 | prose | pages [6] -->
m

<!-- b001741 | prose | pages [6] -->
m

<!-- b001742 | prose | pages [6] -->
m

<!-- b001743 | prose | pages [6] -->
m

<!-- b001744 | prose | pages [6] -->
m

<!-- b001745 | prose | pages [6] -->
m

<!-- b001746 | prose | pages [6] -->
m

<!-- b001747 | prose | pages [6] -->
m

<!-- b001748 | prose | pages [6] -->
m

<!-- b001749 | prose | pages [6] -->
m

<!-- b001750 | prose | pages [6] -->
m

<!-- b001751 | prose | pages [6] -->
m

<!-- b001752 | prose | pages [6] -->
m

<!-- b001753 | prose | pages [6] -->
m

<!-- b001754 | prose | pages [6] -->
m

<!-- b001755 | prose | pages [6] -->
m

<!-- b001756 | prose | pages [6] -->
m

<!-- b001757 | prose | pages [6] -->
m

<!-- b001758 | prose | pages [6] -->
m

<!-- b001759 | prose | pages [6] -->
m

<!-- b001760 | prose | pages [6] -->
m

<!-- b001761 | prose | pages [6] -->
m

<!-- b001762 | prose | pages [6] -->
m

<!-- b001763 | prose | pages [6] -->
m

<!-- b001764 | prose | pages [6] -->
m

<!-- b001765 | prose | pages [6] -->
m

<!-- b001766 | prose | pages [6] -->
m

<!-- b001767 | prose | pages [6] -->
m

<!-- b001768 | prose | pages [6] -->
m

<!-- b001769 | prose | pages [6] -->
m

<!-- b001770 | prose | pages [6] -->
m

<!-- b001771 | prose | pages [6] -->
m

<!-- b001772 | prose | pages [6] -->
m

<!-- b001773 | prose | pages [6] -->
m

<!-- b001774 | prose | pages [6] -->
m

<!-- b001775 | prose | pages [6] -->
m

<!-- b001776 | prose | pages [6] -->
m

<!-- b001777 | prose | pages [6] -->
m

<!-- b001778 | prose | pages [6] -->
m

<!-- b001779 | prose | pages [6] -->
m

<!-- b001780 | prose | pages [6] -->
m

<!-- b001781 | prose | pages [6] -->
m

<!-- b001782 | prose | pages [6] -->
m

<!-- b001783 | prose | pages [6] -->
m

<!-- b001784 | prose | pages [6] -->
m

<!-- b001785 | prose | pages [6] -->
m

<!-- b001786 | prose | pages [6] -->
m

<!-- b001787 | prose | pages [6] -->
m

<!-- b001788 | prose | pages [6] -->
m

<!-- b001789 | prose | pages [6] -->
m

<!-- b001790 | prose | pages [6] -->
m

<!-- b001791 | prose | pages [6] -->
m

<!-- b001792 | prose | pages [6] -->
m

<!-- b001793 | prose | pages [6] -->
m

<!-- b001794 | prose | pages [6] -->
m

<!-- b001795 | prose | pages [6] -->
m

<!-- b001796 | prose | pages [6] -->
m

<!-- b001797 | prose | pages [6] -->
m

<!-- b001798 | prose | pages [6] -->
m

<!-- b001799 | prose | pages [6] -->
m

<!-- b001800 | prose | pages [6] -->
m

<!-- b001801 | prose | pages [6] -->
m

<!-- b001802 | prose | pages [6] -->
m

<!-- b001803 | prose | pages [6] -->
m

<!-- b001804 | prose | pages [6] -->
m

<!-- b001805 | prose | pages [6] -->
m

<!-- b001806 | prose | pages [6] -->
m

<!-- b001807 | prose | pages [6] -->
m

<!-- b001808 | prose | pages [6] -->
m

<!-- b001809 | prose | pages [6] -->
m

<!-- b001810 | prose | pages [6] -->
m

<!-- b001811 | prose | pages [6] -->
m

<!-- b001812 | prose | pages [6] -->
m

<!-- b001813 | prose | pages [6] -->
m

<!-- b001814 | prose | pages [6] -->
m

<!-- b001815 | prose | pages [6] -->
m

<!-- b001816 | prose | pages [6] -->
m

<!-- b001817 | prose | pages [6] -->
m

<!-- b001818 | prose | pages [6] -->
m

<!-- b001819 | prose | pages [6] -->
m

<!-- b001820 | prose | pages [6] -->
m

<!-- b001821 | prose | pages [6] -->
m

<!-- b001822 | prose | pages [6] -->
m

<!-- b001823 | prose | pages [6] -->
m

<!-- b001824 | prose | pages [6] -->
m

<!-- b001825 | prose | pages [6] -->
m

<!-- b001826 | prose | pages [6] -->
m

<!-- b001827 | prose | pages [6] -->
m

<!-- b001828 | prose | pages [6] -->
m

<!-- b001829 | prose | pages [6] -->
m

<!-- b001830 | prose | pages [6] -->
m

<!-- b001831 | prose | pages [6] -->
m

<!-- b001832 | prose | pages [6] -->
m

<!-- b001833 | prose | pages [6] -->
m

<!-- b001834 | prose | pages [6] -->
m

<!-- b001835 | prose | pages [6] -->
m

<!-- b001836 | prose | pages [6] -->
m

<!-- b001837 | prose | pages [6] -->
m

<!-- b001838 | prose | pages [6] -->
m

<!-- b001839 | prose | pages [6] -->
m

<!-- b001840 | prose | pages [6] -->
m

<!-- b001841 | prose | pages [6] -->
m

<!-- b001842 | prose | pages [6] -->
m

<!-- b001843 | prose | pages [6] -->
m

<!-- b001844 | prose | pages [6] -->
m

<!-- b001845 | prose | pages [6] -->
m

<!-- b001846 | prose | pages [6] -->
m

<!-- b001847 | prose | pages [6] -->
m

<!-- b001848 | prose | pages [6] -->
m

<!-- b001849 | prose | pages [6] -->
m

<!-- b001850 | prose | pages [6] -->
m

<!-- b001851 | prose | pages [6] -->
m

<!-- b001852 | prose | pages [6] -->
m

<!-- b001853 | prose | pages [6] -->
m

<!-- b001854 | prose | pages [6] -->
m

<!-- b001855 | prose | pages [6] -->
m

<!-- b001856 | prose | pages [6] -->
m

<!-- b001857 | prose | pages [6] -->
m

<!-- b001858 | prose | pages [6] -->
m

<!-- b001859 | prose | pages [6] -->
m

<!-- b001860 | heading | pages [6] -->
Website of Data Source

<!-- b001861 | prose | pages [6] -->
Database

<!-- b001862 | prose | pages [6] -->
ITU

<!-- b001863 | prose | pages [6] -->
m

<!-- b001864 | prose | pages [6] -->
m

<!-- b001865 | prose | pages [6] -->
m

<!-- b001866 | prose | pages [6] -->
m

<!-- b001867 | prose | pages [6] -->
m

<!-- b001868 | prose | pages [6] -->
m

<!-- b001869 | prose | pages [6] -->
m

<!-- b001870 | prose | pages [6] -->
m

<!-- b001871 | prose | pages [6] -->
m

<!-- b001872 | prose | pages [6] -->
m

<!-- b001873 | prose | pages [6] -->
m

<!-- b001874 | prose | pages [6] -->
m

<!-- b001875 | prose | pages [6] -->
m

<!-- b001876 | prose | pages [6] -->
m

<!-- b001877 | prose | pages [6] -->
m

<!-- b001878 | prose | pages [6] -->
m

<!-- b001879 | prose | pages [6] -->
m

<!-- b001880 | prose | pages [6] -->
m

<!-- b001881 | prose | pages [6] -->
m

<!-- b001882 | prose | pages [6] -->
m

<!-- b001883 | prose | pages [6] -->
m

<!-- b001884 | prose | pages [6] -->
m

<!-- b001885 | prose | pages [6] -->
m

<!-- b001886 | prose | pages [6] -->
m

<!-- b001887 | prose | pages [6] -->
m

<!-- b001888 | prose | pages [6] -->
m

<!-- b001889 | prose | pages [6] -->
m

<!-- b001890 | prose | pages [6] -->
m

<!-- b001891 | prose | pages [6] -->
m

<!-- b001892 | prose | pages [6] -->
m

<!-- b001893 | prose | pages [6] -->
m

<!-- b001894 | prose | pages [6] -->
m

<!-- b001895 | prose | pages [6] -->
m

<!-- b001896 | prose | pages [6] -->
m

<!-- b001897 | prose | pages [6] -->
m

<!-- b001898 | prose | pages [6] -->
m

<!-- b001899 | prose | pages [6] -->
m

<!-- b001900 | prose | pages [6] -->
m

<!-- b001901 | prose | pages [6] -->
m

<!-- b001902 | prose | pages [6] -->
m

<!-- b001903 | prose | pages [6] -->
m

<!-- b001904 | prose | pages [6] -->
m

<!-- b001905 | prose | pages [6] -->
m

<!-- b001906 | prose | pages [6] -->
m

<!-- b001907 | prose | pages [6] -->
m

<!-- b001908 | prose | pages [6] -->
m

<!-- b001909 | prose | pages [6] -->
m

<!-- b001910 | prose | pages [6] -->
m

<!-- b001911 | prose | pages [6] -->
m

<!-- b001912 | prose | pages [6] -->
m

<!-- b001913 | prose | pages [6] -->
m

<!-- b001914 | prose | pages [6] -->
m

<!-- b001915 | prose | pages [6] -->
m

<!-- b001916 | prose | pages [6] -->
m

<!-- b001917 | prose | pages [6] -->
m

<!-- b001918 | prose | pages [6] -->
m

<!-- b001919 | prose | pages [6] -->
m

<!-- b001920 | prose | pages [6] -->
m

<!-- b001921 | prose | pages [6] -->
m

<!-- b001922 | prose | pages [6] -->
m

<!-- b001923 | prose | pages [6] -->
m

<!-- b001924 | prose | pages [6] -->
m

<!-- b001925 | prose | pages [6] -->
m

<!-- b001926 | prose | pages [6] -->
m

<!-- b001927 | prose | pages [6] -->
m

<!-- b001928 | prose | pages [6] -->
m

<!-- b001929 | prose | pages [6] -->
m

<!-- b001930 | prose | pages [6] -->
m

<!-- b001931 | prose | pages [6] -->
m

<!-- b001932 | prose | pages [6] -->
m

<!-- b001933 | prose | pages [6] -->
m

<!-- b001934 | prose | pages [6] -->
m

<!-- b001935 | prose | pages [6] -->
m

<!-- b001936 | prose | pages [6] -->
m

<!-- b001937 | prose | pages [6] -->
m

<!-- b001938 | prose | pages [6] -->
m

<!-- b001939 | prose | pages [6] -->
m

<!-- b001940 | prose | pages [6] -->
m

<!-- b001941 | prose | pages [6] -->
m

<!-- b001942 | prose | pages [6] -->
m

<!-- b001943 | prose | pages [6] -->
m

<!-- b001944 | prose | pages [6] -->
m

<!-- b001945 | prose | pages [6] -->
m

<!-- b001946 | prose | pages [6] -->
m

<!-- b001947 | prose | pages [6] -->
m

<!-- b001948 | prose | pages [6] -->
m

<!-- b001949 | prose | pages [6] -->
m

<!-- b001950 | prose | pages [6] -->
m

<!-- b001951 | prose | pages [6] -->
m

<!-- b001952 | prose | pages [6] -->
m

<!-- b001953 | prose | pages [6] -->
m

<!-- b001954 | prose | pages [6] -->
m

<!-- b001955 | prose | pages [6] -->
m

<!-- b001956 | prose | pages [6] -->
m

<!-- b001957 | prose | pages [6] -->
m

<!-- b001958 | prose | pages [6] -->
m

<!-- b001959 | prose | pages [6] -->
m

<!-- b001960 | prose | pages [6] -->
m

<!-- b001961 | prose | pages [6] -->
m

<!-- b001962 | prose | pages [6] -->
m

<!-- b001963 | prose | pages [6] -->
m

<!-- b001964 | prose | pages [6] -->
m

<!-- b001965 | prose | pages [6] -->
m

<!-- b001966 | prose | pages [6] -->
m

<!-- b001967 | prose | pages [6] -->
m

<!-- b001968 | prose | pages [6] -->
m

<!-- b001969 | prose | pages [6] -->
m

<!-- b001970 | prose | pages [6] -->
m

<!-- b001971 | prose | pages [6] -->
m

<!-- b001972 | prose | pages [6] -->
m

<!-- b001973 | prose | pages [6] -->
m

<!-- b001974 | prose | pages [6] -->
m

<!-- b001975 | prose | pages [6] -->
m

<!-- b001976 | prose | pages [6] -->
m

<!-- b001977 | prose | pages [6] -->
m

<!-- b001978 | prose | pages [6] -->
m

<!-- b001979 | prose | pages [6] -->
m

<!-- b001980 | prose | pages [6] -->
m

<!-- b001981 | prose | pages [6] -->
m

<!-- b001982 | prose | pages [6] -->
m

<!-- b001983 | prose | pages [6] -->
m

<!-- b001984 | prose | pages [6] -->
m

<!-- b001985 | prose | pages [6] -->
m

<!-- b001986 | prose | pages [6] -->
m

<!-- b001987 | prose | pages [6] -->
m

<!-- b001988 | prose | pages [6] -->
m

<!-- b001989 | prose | pages [6] -->
m

<!-- b001990 | prose | pages [6] -->
m

<!-- b001991 | prose | pages [6] -->
m

<!-- b001992 | prose | pages [6] -->
m

<!-- b001993 | prose | pages [6] -->
m

<!-- b001994 | prose | pages [6] -->
m

<!-- b001995 | prose | pages [6] -->
m

<!-- b001996 | prose | pages [6] -->
m

<!-- b001997 | prose | pages [6] -->
m

<!-- b001998 | prose | pages [6] -->
m

<!-- b001999 | prose | pages [6] -->
m

<!-- b002000 | prose | pages [6] -->
m

<!-- b002001 | prose | pages [6] -->
m

<!-- b002002 | prose | pages [6] -->
m

<!-- b002003 | prose | pages [6] -->
m

<!-- b002004 | prose | pages [6] -->
m

<!-- b002005 | prose | pages [6] -->
m

<!-- b002006 | prose | pages [6] -->
m

<!-- b002007 | prose | pages [6] -->
m

<!-- b002008 | prose | pages [6] -->
m

<!-- b002009 | prose | pages [6] -->
m

<!-- b002010 | prose | pages [6] -->
m

<!-- b002011 | prose | pages [6] -->
m

<!-- b002012 | prose | pages [6] -->
m

<!-- b002013 | prose | pages [6] -->
m

<!-- b002014 | prose | pages [6] -->
m

<!-- b002015 | prose | pages [6] -->
m

<!-- b002016 | prose | pages [6] -->
m

<!-- b002017 | prose | pages [6] -->
m

<!-- b002018 | prose | pages [6] -->
m

<!-- b002019 | prose | pages [6] -->
m

<!-- b002020 | prose | pages [6] -->
m

<!-- b002021 | prose | pages [6] -->
m

<!-- b002022 | prose | pages [6] -->
m

<!-- b002023 | prose | pages [6] -->
m

<!-- b002024 | prose | pages [6] -->
m

<!-- b002025 | prose | pages [6] -->
m

<!-- b002026 | prose | pages [6] -->
m

<!-- b002027 | prose | pages [6] -->
m

<!-- b002028 | prose | pages [6] -->
m

<!-- b002029 | prose | pages [6] -->
m

<!-- b002030 | prose | pages [6] -->
m

<!-- b002031 | prose | pages [6] -->
m

<!-- b002032 | prose | pages [6] -->
m

<!-- b002033 | prose | pages [6] -->
m

<!-- b002034 | prose | pages [6] -->
m

<!-- b002035 | prose | pages [6] -->
m

<!-- b002036 | prose | pages [6] -->
m

<!-- b002037 | prose | pages [6] -->
m

<!-- b002038 | prose | pages [6] -->
m

<!-- b002039 | prose | pages [6] -->
m

<!-- b002040 | prose | pages [6] -->
m

<!-- b002041 | prose | pages [6] -->
m

<!-- b002042 | prose | pages [6] -->
m

<!-- b002043 | prose | pages [6] -->
m

<!-- b002044 | prose | pages [6] -->
m

<!-- b002045 | prose | pages [6] -->
m

<!-- b002046 | prose | pages [6] -->
m

<!-- b002047 | prose | pages [6] -->
m

<!-- b002048 | prose | pages [6] -->
m

<!-- b002049 | prose | pages [6] -->
m

<!-- b002050 | prose | pages [6] -->
m

<!-- b002051 | prose | pages [6] -->
m

<!-- b002052 | prose | pages [6] -->
m

<!-- b002053 | prose | pages [6] -->
m

<!-- b002054 | prose | pages [6] -->
m

<!-- b002055 | prose | pages [6] -->
m

<!-- b002056 | prose | pages [6] -->
m

<!-- b002057 | prose | pages [6] -->
m

<!-- b002058 | prose | pages [6] -->
m

<!-- b002059 | prose | pages [6] -->
m

<!-- b002060 | prose | pages [6] -->
m

<!-- b002061 | prose | pages [6] -->
m

<!-- b002062 | prose | pages [6] -->
m

<!-- b002063 | prose | pages [6] -->
m

<!-- b002064 | prose | pages [6] -->
m

<!-- b002065 | prose | pages [6] -->
m

<!-- b002066 | prose | pages [6] -->
m

<!-- b002067 | prose | pages [6] -->
m

<!-- b002068 | prose | pages [6] -->
m

<!-- b002069 | prose | pages [6] -->
m

<!-- b002070 | prose | pages [6] -->
m

<!-- b002071 | prose | pages [6] -->
m

<!-- b002072 | prose | pages [6] -->
m

<!-- b002073 | prose | pages [6] -->
m

<!-- b002074 | prose | pages [6] -->
m

<!-- b002075 | prose | pages [6] -->
m

<!-- b002076 | prose | pages [6] -->
m

<!-- b002077 | prose | pages [6] -->
m

<!-- b002078 | prose | pages [6] -->
m

<!-- b002079 | prose | pages [6] -->
m

<!-- b002080 | prose | pages [6] -->
m

<!-- b002081 | prose | pages [6] -->
m

<!-- b002082 | prose | pages [6] -->
m

<!-- b002083 | prose | pages [6] -->
m

<!-- b002084 | prose | pages [6] -->
m

<!-- b002085 | prose | pages [6] -->
m

<!-- b002086 | prose | pages [6] -->
m

<!-- b002087 | prose | pages [6] -->
m

<!-- b002088 | prose | pages [6] -->
m

<!-- b002089 | prose | pages [6] -->
m

<!-- b002090 | prose | pages [6] -->
m

<!-- b002091 | prose | pages [6] -->
m

<!-- b002092 | prose | pages [6] -->
m

<!-- b002093 | prose | pages [6] -->
m

<!-- b002094 | prose | pages [6] -->
m

<!-- b002095 | prose | pages [6] -->
m

<!-- b002096 | prose | pages [6] -->
m

<!-- b002097 | prose | pages [6] -->
m

<!-- b002098 | prose | pages [6] -->
m

<!-- b002099 | prose | pages [6] -->
m

<!-- b002100 | prose | pages [6] -->
m

<!-- b002101 | prose | pages [6] -->
m

<!-- b002102 | prose | pages [6] -->
m

<!-- b002103 | prose | pages [6] -->
m

<!-- b002104 | prose | pages [6] -->
m

<!-- b002105 | prose | pages [6] -->
m

<!-- b002106 | prose | pages [6] -->
m

<!-- b002107 | prose | pages [6] -->
m

<!-- b002108 | prose | pages [6] -->
m

<!-- b002109 | prose | pages [6] -->
m

<!-- b002110 | prose | pages [6] -->
m

<!-- b002111 | prose | pages [6] -->
m

<!-- b002112 | prose | pages [6] -->
m

<!-- b002113 | prose | pages [6] -->
m

<!-- b002114 | prose | pages [6] -->
m

<!-- b002115 | prose | pages [6] -->
m

<!-- b002116 | prose | pages [6] -->
m

<!-- b002117 | prose | pages [6] -->
m

<!-- b002118 | prose | pages [6] -->
m

<!-- b002119 | prose | pages [6] -->
m

<!-- b002120 | prose | pages [6] -->
m

<!-- b002121 | prose | pages [6] -->
m

<!-- b002122 | prose | pages [6] -->
m

<!-- b002123 | prose | pages [6] -->
m

<!-- b002124 | prose | pages [6] -->
m

<!-- b002125 | prose | pages [6] -->
m

<!-- b002126 | prose | pages [6] -->
m

<!-- b002127 | prose | pages [6] -->
m

<!-- b002128 | prose | pages [6] -->
m

<!-- b002129 | prose | pages [6] -->
m

<!-- b002130 | prose | pages [6] -->
m

<!-- b002131 | prose | pages [6] -->
m

<!-- b002132 | prose | pages [6] -->
m

<!-- b002133 | prose | pages [6] -->
https://www.itu.int/epublications/publ

<!-- b002134 | prose | pages [6] -->
m

<!-- b002135 | prose | pages [6] -->
m

<!-- b002136 | prose | pages [6] -->
m

<!-- b002137 | prose | pages [6] -->
m

<!-- b002138 | prose | pages [6] -->
m

<!-- b002139 | prose | pages [6] -->
m

<!-- b002140 | prose | pages [6] -->
m

<!-- b002141 | prose | pages [6] -->
m

<!-- b002142 | prose | pages [6] -->
m

<!-- b002143 | prose | pages [6] -->
m

<!-- b002144 | prose | pages [6] -->
m

<!-- b002145 | prose | pages [6] -->
m

<!-- b002146 | prose | pages [6] -->
m

<!-- b002147 | prose | pages [6] -->
m

<!-- b002148 | prose | pages [6] -->
m

<!-- b002149 | prose | pages [6] -->
m

<!-- b002150 | prose | pages [6] -->
m

<!-- b002151 | prose | pages [6] -->
m

<!-- b002152 | prose | pages [6] -->
m

<!-- b002153 | prose | pages [6] -->
m

<!-- b002154 | prose | pages [6] -->
m

<!-- b002155 | prose | pages [6] -->
m

<!-- b002156 | prose | pages [6] -->
m

<!-- b002157 | prose | pages [6] -->
m

<!-- b002158 | prose | pages [6] -->
m

<!-- b002159 | prose | pages [6] -->
m

<!-- b002160 | prose | pages [6] -->
m

<!-- b002161 | prose | pages [6] -->
m

<!-- b002162 | prose | pages [6] -->
m

<!-- b002163 | prose | pages [6] -->
m

<!-- b002164 | prose | pages [6] -->
m

<!-- b002165 | prose | pages [6] -->
m

<!-- b002166 | prose | pages [6] -->
m

<!-- b002167 | prose | pages [6] -->
m

<!-- b002168 | prose | pages [6] -->
m

<!-- b002169 | prose | pages [6] -->
m

<!-- b002170 | prose | pages [6] -->
m

<!-- b002171 | prose | pages [6] -->
m

<!-- b002172 | prose | pages [6] -->
m

<!-- b002173 | prose | pages [6] -->
m

<!-- b002174 | prose | pages [6] -->
m

<!-- b002175 | prose | pages [6] -->
m

<!-- b002176 | prose | pages [6] -->
m

<!-- b002177 | prose | pages [6] -->
m

<!-- b002178 | prose | pages [6] -->
m

<!-- b002179 | prose | pages [6] -->
m

<!-- b002180 | prose | pages [6] -->
m

<!-- b002181 | prose | pages [6] -->
m

<!-- b002182 | prose | pages [6] -->
m

<!-- b002183 | prose | pages [6] -->
m

<!-- b002184 | prose | pages [6] -->
m

<!-- b002185 | prose | pages [6] -->
m

<!-- b002186 | prose | pages [6] -->
m

<!-- b002187 | prose | pages [6] -->
m

<!-- b002188 | prose | pages [6] -->
m

<!-- b002189 | prose | pages [6] -->
m

<!-- b002190 | prose | pages [6] -->
m

<!-- b002191 | prose | pages [6] -->
m

<!-- b002192 | prose | pages [6] -->
m

<!-- b002193 | prose | pages [6] -->
m

<!-- b002194 | prose | pages [6] -->
m

<!-- b002195 | prose | pages [6] -->
m

<!-- b002196 | prose | pages [6] -->
m

<!-- b002197 | prose | pages [6] -->
m

<!-- b002198 | prose | pages [6] -->
m

<!-- b002199 | prose | pages [6] -->
m

<!-- b002200 | prose | pages [6] -->
m

<!-- b002201 | prose | pages [6] -->
m

<!-- b002202 | prose | pages [6] -->
m

<!-- b002203 | prose | pages [6] -->
m

<!-- b002204 | prose | pages [6] -->
m

<!-- b002205 | prose | pages [6] -->
m

<!-- b002206 | prose | pages [6] -->
m

<!-- b002207 | prose | pages [6] -->
m

<!-- b002208 | prose | pages [6] -->
m

<!-- b002209 | prose | pages [6] -->
m

<!-- b002210 | prose | pages [6] -->
m

<!-- b002211 | prose | pages [6] -->
m

<!-- b002212 | prose | pages [6] -->
m

<!-- b002213 | prose | pages [6] -->
m

<!-- b002214 | prose | pages [6] -->
m

<!-- b002215 | prose | pages [6] -->
m

<!-- b002216 | prose | pages [6] -->
m

<!-- b002217 | prose | pages [6] -->
m

<!-- b002218 | prose | pages [6] -->
m

<!-- b002219 | prose | pages [6] -->
m

<!-- b002220 | prose | pages [6] -->
m

<!-- b002221 | prose | pages [6] -->
m

<!-- b002222 | prose | pages [6] -->
m

<!-- b002223 | prose | pages [6] -->
m

<!-- b002224 | prose | pages [6] -->
m

<!-- b002225 | prose | pages [6] -->
m

<!-- b002226 | prose | pages [6] -->
m

<!-- b002227 | prose | pages [6] -->
m

<!-- b002228 | prose | pages [6] -->
m

<!-- b002229 | prose | pages [6] -->
m

<!-- b002230 | prose | pages [6] -->
m

<!-- b002231 | prose | pages [6] -->
m

<!-- b002232 | prose | pages [6] -->
m

<!-- b002233 | prose | pages [6] -->
m

<!-- b002234 | prose | pages [6] -->
m

<!-- b002235 | prose | pages [6] -->
m

<!-- b002236 | prose | pages [6] -->
m

<!-- b002237 | prose | pages [6] -->
m

<!-- b002238 | prose | pages [6] -->
m

<!-- b002239 | prose | pages [6] -->
m

<!-- b002240 | prose | pages [6] -->
m

<!-- b002241 | prose | pages [6] -->
m

<!-- b002242 | prose | pages [6] -->
m

<!-- b002243 | prose | pages [6] -->
m

<!-- b002244 | prose | pages [6] -->
m

<!-- b002245 | prose | pages [6] -->
m

<!-- b002246 | prose | pages [6] -->
m

<!-- b002247 | prose | pages [6] -->
m

<!-- b002248 | prose | pages [6] -->
m

<!-- b002249 | prose | pages [6] -->
m

<!-- b002250 | prose | pages [6] -->
m

<!-- b002251 | prose | pages [6] -->
m

<!-- b002252 | prose | pages [6] -->
m

<!-- b002253 | prose | pages [6] -->
m

<!-- b002254 | prose | pages [6] -->
m

<!-- b002255 | prose | pages [6] -->
ication/global-cybersecurity-index-2024

<!-- b002256 | prose | pages [6] -->
VCDB https://verisframework.org/vcdb.html

<!-- b002257 | prose | pages [6] -->
World Bank https://data.worldbank.org

<!-- b002258 | prose | pages [6] -->
level data on cybercrime incidents and ranked the results in descending order by total incidents, initially identifying countries with high cybercrime rates. Additionally, the countrycode package was used to convert country codes to full names and correct spe- cial cases (e.g., changing "United States" to "USA") to enhance data readability. To opti- mize analysis and visualization, the incident counts were logarithmically transformed.

<!-- b002259 | prose | pages [6] -->
Using tools such as dplyr, countrycode, and ggplot2, we completed the entire process from data cleaning to visualization, ensuring data accuracy and consistency [4] [5]. The ﬁnal results provide valuable data support for the study of global cybercrime distribution and policy development.

<!-- b002260 | heading | pages [6] -->
Data Analysis and Visualization

<!-- b002261 | prose | pages [6] -->
4.3

<!-- b002262 | prose | pages [6] -->
Global Cybercrime Distribution Heatmap 4.3.1

<!-- b002263 | caption | pages [6] -->
Figure 3: Global Cybercrime Distribution

<!-- b002264 | prose | pages [6] -->
During the geographic visualization phase, we loaded global map data and matched it with the processed country data, achieving a one-to-one correspondence by aligning regional ﬁelds with the corrected country names. The visualization employed a color

<!-- b002265 | prose | pages [6] -->
关注数学模型

<!-- b002266 | furniture | pages [6] -->
2

<!-- b002267 | furniture | pages [6] -->
MATHmodels

<!-- b002268 | furniture | pages [6] -->
获取更多资讯

<!-- b002269 | furniture | pages [7] -->
Team # 2521039

<!-- b002270 | furniture | pages [7] -->
Page 7 of 25

<!-- b002271 | prose | pages [7] -->
gradient to represent the number of cybercrime incidents in each country, transition- ing from light blue to deep red to illustrate the distribution trend from low to high. This heatmap visualization effectively reﬂected the global distribution patterns and characteristics of cybercrime.

<!-- b002272 | prose | pages [7] -->
微信公众号：数学模型

<!-- b002273 | prose | pages [7] -->
The resulting global cybercrime distribution heatmap revealed that North America and Europe are high-incidence regions for cybercrime. Countries such as the United States, Canada, the United Kingdom, Germany, and Ireland exhibit a signiﬁcantly higher frequency of cybercrime incidents. In contrast, South America and African countries report relatively fewer cybercrime cases. Among Asian countries, cybercrime activity varies signiﬁcantly, with countries like China, Japan, and South Korea showing high levels of activity, while nations such as Indonesia and the Philippines experience much lower levels.

<!-- b002274 | prose | pages [7] -->
4.3.2 Global Cybercrime Situation Analysis

<!-- b002275 | prose | pages [7] -->
微信号：MATHmodels

<!-- b002276 | caption | pages [7] -->
Figure 4: Hacking word cloud map

<!-- b002277 | prose | pages [7] -->
Based on the data from the VCDB database, we ﬁrst extracted several ﬁelds related to cyberattacks (e.g., attack outcomes, attack methods) and generated a word cloud based on the frequency of these ﬁelds. The font size visually represented the relative frequency of each term, providing an intuitive overview of the primary categories and their occurrence rates in cybercrime, thereby laying the foundation for further research.

<!-- b002278 | caption | pages [7] -->
Figure 5: Classiﬁed statistics on cybercrime

<!-- b002279 | prose | pages [7] -->
The analysis revealed that cyberattack data is categorized into three main groups: Vector, Variety, and Result, all of which exhibit signiﬁcant concentration. In the Vector category, Web application emerged as the most common type, occupying the largest proportion, followed by Backdoor and Unknown. In contrast, Command shell and Desktop sharing software had relatively fewer incidents. Within the Variety category,

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
Use of stolen creds and Unknown accounted for the majority of incidents, while Back-

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

<!-- b002477 | prose | pages [7] -->
m

<!-- b002478 | prose | pages [7] -->
m

<!-- b002479 | prose | pages [7] -->
m

<!-- b002480 | prose | pages [7] -->
m

<!-- b002481 | prose | pages [7] -->
m

<!-- b002482 | prose | pages [7] -->
m

<!-- b002483 | prose | pages [7] -->
m

<!-- b002484 | prose | pages [7] -->
m

<!-- b002485 | prose | pages [7] -->
m

<!-- b002486 | prose | pages [7] -->
m

<!-- b002487 | prose | pages [7] -->
m

<!-- b002488 | prose | pages [7] -->
m

<!-- b002489 | prose | pages [7] -->
m

<!-- b002490 | prose | pages [7] -->
m

<!-- b002491 | prose | pages [7] -->
m

<!-- b002492 | prose | pages [7] -->
m

<!-- b002493 | prose | pages [7] -->
m

<!-- b002494 | prose | pages [7] -->
m

<!-- b002495 | prose | pages [7] -->
m

<!-- b002496 | prose | pages [7] -->
m

<!-- b002497 | prose | pages [7] -->
m

<!-- b002498 | prose | pages [7] -->
m

<!-- b002499 | prose | pages [7] -->
m

<!-- b002500 | prose | pages [7] -->
m

<!-- b002501 | prose | pages [7] -->
m

<!-- b002502 | prose | pages [7] -->
m

<!-- b002503 | prose | pages [7] -->
m

<!-- b002504 | prose | pages [7] -->
m

<!-- b002505 | prose | pages [7] -->
m

<!-- b002506 | prose | pages [7] -->
m

<!-- b002507 | prose | pages [7] -->
m

<!-- b002508 | prose | pages [7] -->
m

<!-- b002509 | prose | pages [7] -->
m

<!-- b002510 | prose | pages [7] -->
m

<!-- b002511 | prose | pages [7] -->
m

<!-- b002512 | prose | pages [7] -->
door, Exploit vuln, and Brute force were also prominent, indicating that attackers tend

<!-- b002513 | prose | pages [7] -->
m

<!-- b002514 | prose | pages [7] -->
m

<!-- b002515 | prose | pages [7] -->
m

<!-- b002516 | prose | pages [7] -->
m

<!-- b002517 | prose | pages [7] -->
m

<!-- b002518 | prose | pages [7] -->
m

<!-- b002519 | prose | pages [7] -->
m

<!-- b002520 | prose | pages [7] -->
m

<!-- b002521 | prose | pages [7] -->
m

<!-- b002522 | prose | pages [7] -->
m

<!-- b002523 | prose | pages [7] -->
m

<!-- b002524 | prose | pages [7] -->
m

<!-- b002525 | prose | pages [7] -->
m

<!-- b002526 | prose | pages [7] -->
m

<!-- b002527 | prose | pages [7] -->
m

<!-- b002528 | prose | pages [7] -->
m

<!-- b002529 | prose | pages [7] -->
m

<!-- b002530 | prose | pages [7] -->
m

<!-- b002531 | prose | pages [7] -->
m

<!-- b002532 | prose | pages [7] -->
m

<!-- b002533 | prose | pages [7] -->
m

<!-- b002534 | prose | pages [7] -->
m

<!-- b002535 | prose | pages [7] -->
m

<!-- b002536 | prose | pages [7] -->
m

<!-- b002537 | prose | pages [7] -->
m

<!-- b002538 | prose | pages [7] -->
m

<!-- b002539 | prose | pages [7] -->
m

<!-- b002540 | prose | pages [7] -->
m

<!-- b002541 | prose | pages [7] -->
m

<!-- b002542 | prose | pages [7] -->
m

<!-- b002543 | prose | pages [7] -->
m

<!-- b002544 | prose | pages [7] -->
m

<!-- b002545 | prose | pages [7] -->
m

<!-- b002546 | prose | pages [7] -->
m

<!-- b002547 | prose | pages [7] -->
m

<!-- b002548 | prose | pages [7] -->
m

<!-- b002549 | prose | pages [7] -->
m

<!-- b002550 | prose | pages [7] -->
m

<!-- b002551 | prose | pages [7] -->
m

<!-- b002552 | prose | pages [7] -->
m

<!-- b002553 | prose | pages [7] -->
m

<!-- b002554 | prose | pages [7] -->
m

<!-- b002555 | prose | pages [7] -->
m

<!-- b002556 | prose | pages [7] -->
m

<!-- b002557 | prose | pages [7] -->
m

<!-- b002558 | prose | pages [7] -->
m

<!-- b002559 | prose | pages [7] -->
m

<!-- b002560 | prose | pages [7] -->
m

<!-- b002561 | prose | pages [7] -->
m

<!-- b002562 | prose | pages [7] -->
m

<!-- b002563 | prose | pages [7] -->
m

<!-- b002564 | prose | pages [7] -->
m

<!-- b002565 | prose | pages [7] -->
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

<!-- b002880 | furniture | pages [7] -->
m

<!-- b002881 | furniture | pages [7] -->
m

<!-- b002882 | furniture | pages [7] -->
m

<!-- b002883 | furniture | pages [7] -->
m

<!-- b002884 | furniture | pages [7] -->
m

<!-- b002885 | furniture | pages [7] -->
m

<!-- b002886 | furniture | pages [7] -->
m

<!-- b002887 | furniture | pages [7] -->
m

<!-- b002888 | furniture | pages [7] -->
m

<!-- b002889 | furniture | pages [7] -->
m

<!-- b002890 | furniture | pages [7] -->
m

<!-- b002891 | furniture | pages [7] -->
m

<!-- b002892 | furniture | pages [7] -->
m

<!-- b002893 | furniture | pages [7] -->
m

<!-- b002894 | furniture | pages [7] -->
m

<!-- b002895 | furniture | pages [7] -->
m

<!-- b002896 | furniture | pages [7] -->
m

<!-- b002897 | furniture | pages [7] -->
m

<!-- b002898 | furniture | pages [7] -->
m

<!-- b002899 | furniture | pages [7] -->
m

<!-- b002900 | furniture | pages [7] -->
m

<!-- b002901 | furniture | pages [7] -->
m

<!-- b002902 | furniture | pages [7] -->
m

<!-- b002903 | furniture | pages [7] -->
m

<!-- b002904 | furniture | pages [7] -->
m

<!-- b002905 | furniture | pages [7] -->
m

<!-- b002906 | furniture | pages [7] -->
m

<!-- b002907 | furniture | pages [7] -->
m

<!-- b002908 | furniture | pages [7] -->
m

<!-- b002909 | furniture | pages [7] -->
m

<!-- b002910 | furniture | pages [7] -->
m

<!-- b002911 | furniture | pages [7] -->
m

<!-- b002912 | furniture | pages [7] -->
m

<!-- b002913 | furniture | pages [7] -->
m

<!-- b002914 | furniture | pages [7] -->
m

<!-- b002915 | furniture | pages [7] -->
m

<!-- b002916 | furniture | pages [7] -->
m

<!-- b002917 | furniture | pages [7] -->
m

<!-- b002918 | furniture | pages [7] -->
m

<!-- b002919 | furniture | pages [7] -->
m

<!-- b002920 | furniture | pages [7] -->
m

<!-- b002921 | furniture | pages [7] -->
m

<!-- b002922 | furniture | pages [7] -->
m

<!-- b002923 | furniture | pages [7] -->
m

<!-- b002924 | furniture | pages [7] -->
m

<!-- b002925 | furniture | pages [7] -->
m

<!-- b002926 | furniture | pages [7] -->
m

<!-- b002927 | furniture | pages [7] -->
m

<!-- b002928 | furniture | pages [7] -->
m

<!-- b002929 | furniture | pages [7] -->
m

<!-- b002930 | furniture | pages [7] -->
m

<!-- b002931 | furniture | pages [7] -->
m

<!-- b002932 | furniture | pages [7] -->
m

<!-- b002933 | furniture | pages [7] -->
m

<!-- b002934 | furniture | pages [7] -->
m

<!-- b002935 | furniture | pages [7] -->
m

<!-- b002936 | furniture | pages [7] -->
m

<!-- b002937 | furniture | pages [7] -->
m

<!-- b002938 | furniture | pages [7] -->
m

<!-- b002939 | furniture | pages [7] -->
m

<!-- b002940 | furniture | pages [7] -->
m

<!-- b002941 | furniture | pages [7] -->
m

<!-- b002942 | furniture | pages [7] -->
m

<!-- b002943 | furniture | pages [7] -->
m

<!-- b002944 | furniture | pages [7] -->
m

<!-- b002945 | furniture | pages [7] -->
m

<!-- b002946 | furniture | pages [7] -->
m

<!-- b002947 | furniture | pages [7] -->
m

<!-- b002948 | furniture | pages [7] -->
m

<!-- b002949 | furniture | pages [7] -->
m

<!-- b002950 | furniture | pages [7] -->
m

<!-- b002951 | furniture | pages [7] -->
m

<!-- b002952 | furniture | pages [7] -->
m

<!-- b002953 | furniture | pages [7] -->
m

<!-- b002954 | furniture | pages [7] -->
m

<!-- b002955 | furniture | pages [7] -->
m

<!-- b002956 | furniture | pages [7] -->
m

<!-- b002957 | furniture | pages [7] -->
m

<!-- b002958 | furniture | pages [7] -->
m

<!-- b002959 | furniture | pages [7] -->
m

<!-- b002960 | furniture | pages [7] -->
m

<!-- b002961 | furniture | pages [7] -->
m

<!-- b002962 | furniture | pages [7] -->
m

<!-- b002963 | furniture | pages [7] -->
m

<!-- b002964 | furniture | pages [7] -->
m

<!-- b002965 | furniture | pages [7] -->
m

<!-- b002966 | furniture | pages [7] -->
m

<!-- b002967 | furniture | pages [7] -->
m

<!-- b002968 | furniture | pages [7] -->
m

<!-- b002969 | furniture | pages [8] -->
Team # 2521039

<!-- b002970 | furniture | pages [8] -->
Page 8 of 25

<!-- b002971 | prose | pages [8] -->
to exploit stolen credentials or system vulnerabilities for intrusions. In the Result cat- egory, Exﬁltrate was identiﬁed as the most frequent goal, followed by Elevate and Deploy payload, while Lateral movement and Inﬁltrate occurred less frequently.

<!-- b002972 | prose | pages [8] -->
This distribution suggests that attackers typically focus resources on efﬁcient attack methods and well-deﬁned targets. Therefore, cybersecurity defenses should prioritize strengthening protections against Web application attacks and Exﬁltrate data theft.

<!-- b002973 | prose | pages [8] -->
Analysis of Target Count, Success Rate, Defeat Rate, Report Rate, and Prose- 4.3.3 cution Rate

<!-- b002974 | prose | pages [8] -->
By analyzing the VERIS database and referencing its glossary deﬁnitions, we ex- tracted key indicators such as target count, success rate, thwart rate, reporting rate, and prosecution rate to assess the distribution characteristics and trends of cybercrime.

<!-- b002975 | prose | pages [8] -->
• Target Count: Reﬂects the number of cybercrime incidents occurring in each country annually, calculated by grouping data based on the timeline.incident. year and victim.country ﬁelds. • Success Rate and Thwart Rate: Represent the proportions of incidents resulting in and not resulting in data breaches, respectively. These are calculated based on the attribute.confidentiality.data_disclosure ﬁeld (True for suc- cess, False for thwart). • Reporting Rate: Evaluates the proportion of incidents that were discovered and recorded, identiﬁed by ﬁltering the discovery_method ﬁeld. • Prosecution Rate: Focuses on whether legal actions were taken, marked by key- words (e.g., “prosecuted” or “charged”) in the summary and reference ﬁelds.

<!-- b002976 | prose | pages [8] -->
Finally, these indicators were aggregated and merged into a uniﬁed dataset, en- abling intuitive visualization and in-depth analysis. This process effectively reveals the temporal and spatial characteristics of cybercrime, providing valuable data sup- port for the development of targeted cybersecurity strategies.

<!-- b002977 | prose | pages [8] -->
m

<!-- b002978 | prose | pages [8] -->
m

<!-- b002979 | prose | pages [8] -->
m

<!-- b002980 | prose | pages [8] -->
m

<!-- b002981 | prose | pages [8] -->
m

<!-- b002982 | prose | pages [8] -->
m

<!-- b002983 | prose | pages [8] -->
m

<!-- b002984 | prose | pages [8] -->
m

<!-- b002985 | prose | pages [8] -->
m

<!-- b002986 | prose | pages [8] -->
m

<!-- b002987 | prose | pages [8] -->
m

<!-- b002988 | prose | pages [8] -->
m

<!-- b002989 | prose | pages [8] -->
m

<!-- b002990 | prose | pages [8] -->
m

<!-- b002991 | prose | pages [8] -->
m

<!-- b002992 | prose | pages [8] -->
m

<!-- b002993 | prose | pages [8] -->
m

<!-- b002994 | prose | pages [8] -->
m

<!-- b002995 | prose | pages [8] -->
m

<!-- b002996 | prose | pages [8] -->
m

<!-- b002997 | prose | pages [8] -->
m

<!-- b002998 | prose | pages [8] -->
m

<!-- b002999 | prose | pages [8] -->
m

<!-- b003000 | prose | pages [8] -->
m

<!-- b003001 | prose | pages [8] -->
m

<!-- b003002 | prose | pages [8] -->
m

<!-- b003003 | prose | pages [8] -->
m

<!-- b003004 | prose | pages [8] -->
m

<!-- b003005 | prose | pages [8] -->
m

<!-- b003006 | prose | pages [8] -->
m

<!-- b003007 | prose | pages [8] -->
m

<!-- b003008 | prose | pages [8] -->
m

<!-- b003009 | prose | pages [8] -->
m

<!-- b003010 | prose | pages [8] -->
m

<!-- b003011 | prose | pages [8] -->
m

<!-- b003012 | prose | pages [8] -->
m

<!-- b003013 | prose | pages [8] -->
m

<!-- b003014 | prose | pages [8] -->
m

<!-- b003015 | prose | pages [8] -->
m

<!-- b003016 | prose | pages [8] -->
m

<!-- b003017 | prose | pages [8] -->
m

<!-- b003018 | prose | pages [8] -->
m

<!-- b003019 | prose | pages [8] -->
m

<!-- b003020 | prose | pages [8] -->
m

<!-- b003021 | prose | pages [8] -->
m

<!-- b003022 | prose | pages [8] -->
m

<!-- b003023 | prose | pages [8] -->
m

<!-- b003024 | prose | pages [8] -->
m

<!-- b003025 | prose | pages [8] -->
m

<!-- b003026 | prose | pages [8] -->
m

<!-- b003027 | prose | pages [8] -->
m

<!-- b003028 | prose | pages [8] -->
m

<!-- b003029 | prose | pages [8] -->
m

<!-- b003030 | prose | pages [8] -->
m

<!-- b003031 | prose | pages [8] -->
m

<!-- b003032 | prose | pages [8] -->
m

<!-- b003033 | prose | pages [8] -->
m

<!-- b003034 | prose | pages [8] -->
m

<!-- b003035 | prose | pages [8] -->
m

<!-- b003036 | prose | pages [8] -->
m

<!-- b003037 | prose | pages [8] -->
m

<!-- b003038 | prose | pages [8] -->
m

<!-- b003039 | prose | pages [8] -->
m

<!-- b003040 | prose | pages [8] -->
m

<!-- b003041 | prose | pages [8] -->
m

<!-- b003042 | prose | pages [8] -->
m

<!-- b003043 | prose | pages [8] -->
m

<!-- b003044 | prose | pages [8] -->
m

<!-- b003045 | prose | pages [8] -->
m

<!-- b003046 | prose | pages [8] -->
m

<!-- b003047 | prose | pages [8] -->
m

<!-- b003048 | prose | pages [8] -->
m

<!-- b003049 | prose | pages [8] -->
m

<!-- b003050 | prose | pages [8] -->
m

<!-- b003051 | prose | pages [8] -->
m

<!-- b003052 | prose | pages [8] -->
m

<!-- b003053 | prose | pages [8] -->
m

<!-- b003054 | prose | pages [8] -->
m

<!-- b003055 | prose | pages [8] -->
m

<!-- b003056 | prose | pages [8] -->
m

<!-- b003057 | prose | pages [8] -->
m

<!-- b003058 | prose | pages [8] -->
m

<!-- b003059 | prose | pages [8] -->
m

<!-- b003060 | prose | pages [8] -->
m

<!-- b003061 | prose | pages [8] -->
m

<!-- b003062 | prose | pages [8] -->
m

<!-- b003063 | prose | pages [8] -->
m

<!-- b003064 | prose | pages [8] -->
m

<!-- b003065 | prose | pages [8] -->
m

<!-- b003066 | prose | pages [8] -->
m

<!-- b003067 | prose | pages [8] -->
m

<!-- b003068 | prose | pages [8] -->
m

<!-- b003069 | prose | pages [8] -->
m

<!-- b003070 | prose | pages [8] -->
m

<!-- b003071 | prose | pages [8] -->
m

<!-- b003072 | prose | pages [8] -->
m

<!-- b003073 | prose | pages [8] -->
m

<!-- b003074 | prose | pages [8] -->
m

<!-- b003075 | prose | pages [8] -->
m

<!-- b003076 | prose | pages [8] -->
m

<!-- b003077 | prose | pages [8] -->
m

<!-- b003078 | prose | pages [8] -->
m

<!-- b003079 | prose | pages [8] -->
m

<!-- b003080 | prose | pages [8] -->
m

<!-- b003081 | prose | pages [8] -->
m

<!-- b003082 | prose | pages [8] -->
m

<!-- b003083 | prose | pages [8] -->
m

<!-- b003084 | prose | pages [8] -->
m

<!-- b003085 | prose | pages [8] -->
m

<!-- b003086 | prose | pages [8] -->
m

<!-- b003087 | prose | pages [8] -->
m

<!-- b003088 | prose | pages [8] -->
m

<!-- b003089 | prose | pages [8] -->
m

<!-- b003090 | prose | pages [8] -->
m

<!-- b003091 | prose | pages [8] -->
m

<!-- b003092 | prose | pages [8] -->
m

<!-- b003093 | prose | pages [8] -->
m

<!-- b003094 | prose | pages [8] -->
m

<!-- b003095 | prose | pages [8] -->
m

<!-- b003096 | prose | pages [8] -->
m

<!-- b003097 | prose | pages [8] -->
m

<!-- b003098 | prose | pages [8] -->
m

<!-- b003099 | prose | pages [8] -->
m

<!-- b003100 | prose | pages [8] -->
m

<!-- b003101 | prose | pages [8] -->
m

<!-- b003102 | prose | pages [8] -->
m

<!-- b003103 | prose | pages [8] -->
m

<!-- b003104 | prose | pages [8] -->
m

<!-- b003105 | prose | pages [8] -->
m

<!-- b003106 | prose | pages [8] -->
m

<!-- b003107 | prose | pages [8] -->
m

<!-- b003108 | prose | pages [8] -->
m

<!-- b003109 | prose | pages [8] -->
m

<!-- b003110 | prose | pages [8] -->
m

<!-- b003111 | prose | pages [8] -->
m

<!-- b003112 | prose | pages [8] -->
m

<!-- b003113 | prose | pages [8] -->
m

<!-- b003114 | prose | pages [8] -->
m

<!-- b003115 | prose | pages [8] -->
m

<!-- b003116 | prose | pages [8] -->
m

<!-- b003117 | prose | pages [8] -->
m

<!-- b003118 | prose | pages [8] -->
m

<!-- b003119 | prose | pages [8] -->
m

<!-- b003120 | prose | pages [8] -->
m

<!-- b003121 | prose | pages [8] -->
m

<!-- b003122 | prose | pages [8] -->
m

<!-- b003123 | prose | pages [8] -->
m

<!-- b003124 | prose | pages [8] -->
m

<!-- b003125 | prose | pages [8] -->
m

<!-- b003126 | prose | pages [8] -->
m

<!-- b003127 | prose | pages [8] -->
m

<!-- b003128 | prose | pages [8] -->
m

<!-- b003129 | prose | pages [8] -->
m

<!-- b003130 | prose | pages [8] -->
m

<!-- b003131 | prose | pages [8] -->
m

<!-- b003132 | prose | pages [8] -->
m

<!-- b003133 | prose | pages [8] -->
m

<!-- b003134 | prose | pages [8] -->
m

<!-- b003135 | prose | pages [8] -->
m

<!-- b003136 | prose | pages [8] -->
m

<!-- b003137 | prose | pages [8] -->
m

<!-- b003138 | prose | pages [8] -->
m

<!-- b003139 | prose | pages [8] -->
m

<!-- b003140 | prose | pages [8] -->
m

<!-- b003141 | prose | pages [8] -->
m

<!-- b003142 | prose | pages [8] -->
m

<!-- b003143 | prose | pages [8] -->
m

<!-- b003144 | prose | pages [8] -->
m

<!-- b003145 | prose | pages [8] -->
m

<!-- b003146 | prose | pages [8] -->
m

<!-- b003147 | prose | pages [8] -->
m

<!-- b003148 | prose | pages [8] -->
m

<!-- b003149 | prose | pages [8] -->
m

<!-- b003150 | prose | pages [8] -->
m

<!-- b003151 | prose | pages [8] -->
m

<!-- b003152 | prose | pages [8] -->
m

<!-- b003153 | prose | pages [8] -->
m

<!-- b003154 | prose | pages [8] -->
m

<!-- b003155 | prose | pages [8] -->
m

<!-- b003156 | prose | pages [8] -->
m

<!-- b003157 | prose | pages [8] -->
m

<!-- b003158 | prose | pages [8] -->
m

<!-- b003159 | prose | pages [8] -->
m

<!-- b003160 | prose | pages [8] -->
m

<!-- b003161 | prose | pages [8] -->
m

<!-- b003162 | prose | pages [8] -->
m

<!-- b003163 | prose | pages [8] -->
m

<!-- b003164 | prose | pages [8] -->
m

<!-- b003165 | prose | pages [8] -->
m

<!-- b003166 | prose | pages [8] -->
m

<!-- b003167 | prose | pages [8] -->
m

<!-- b003168 | prose | pages [8] -->
m

<!-- b003169 | prose | pages [8] -->
m

<!-- b003170 | prose | pages [8] -->
m

<!-- b003171 | prose | pages [8] -->
m

<!-- b003172 | prose | pages [8] -->
m

<!-- b003173 | prose | pages [8] -->
m

<!-- b003174 | prose | pages [8] -->
m

<!-- b003175 | prose | pages [8] -->
m

<!-- b003176 | prose | pages [8] -->
m

<!-- b003177 | prose | pages [8] -->
m

<!-- b003178 | prose | pages [8] -->
m

<!-- b003179 | prose | pages [8] -->
m

<!-- b003180 | prose | pages [8] -->
m

<!-- b003181 | prose | pages [8] -->
m

<!-- b003182 | prose | pages [8] -->
m

<!-- b003183 | prose | pages [8] -->
m

<!-- b003184 | prose | pages [8] -->
m

<!-- b003185 | prose | pages [8] -->
m

<!-- b003186 | prose | pages [8] -->
m

<!-- b003187 | prose | pages [8] -->
m

<!-- b003188 | prose | pages [8] -->
m

<!-- b003189 | prose | pages [8] -->
m

<!-- b003190 | prose | pages [8] -->
m

<!-- b003191 | prose | pages [8] -->
m

<!-- b003192 | prose | pages [8] -->
m

<!-- b003193 | prose | pages [8] -->
m

<!-- b003194 | prose | pages [8] -->
m

<!-- b003195 | prose | pages [8] -->
m

<!-- b003196 | prose | pages [8] -->
m

<!-- b003197 | prose | pages [8] -->
m

<!-- b003198 | prose | pages [8] -->
m

<!-- b003199 | prose | pages [8] -->
m

<!-- b003200 | prose | pages [8] -->
m

<!-- b003201 | prose | pages [8] -->
m

<!-- b003202 | prose | pages [8] -->
m

<!-- b003203 | prose | pages [8] -->
m

<!-- b003204 | prose | pages [8] -->
m

<!-- b003205 | prose | pages [8] -->
m

<!-- b003206 | prose | pages [8] -->
m

<!-- b003207 | prose | pages [8] -->
m

<!-- b003208 | prose | pages [8] -->
m

<!-- b003209 | prose | pages [8] -->
m

<!-- b003210 | prose | pages [8] -->
m

<!-- b003211 | prose | pages [8] -->
m

<!-- b003212 | prose | pages [8] -->
m

<!-- b003213 | prose | pages [8] -->
m

<!-- b003214 | prose | pages [8] -->
m

<!-- b003215 | prose | pages [8] -->
m

<!-- b003216 | prose | pages [8] -->
m

<!-- b003217 | prose | pages [8] -->
m

<!-- b003218 | prose | pages [8] -->
m

<!-- b003219 | prose | pages [8] -->
m

<!-- b003220 | prose | pages [8] -->
m

<!-- b003221 | prose | pages [8] -->
m

<!-- b003222 | prose | pages [8] -->
m

<!-- b003223 | prose | pages [8] -->
m

<!-- b003224 | prose | pages [8] -->
m

<!-- b003225 | prose | pages [8] -->
m

<!-- b003226 | prose | pages [8] -->
m

<!-- b003227 | prose | pages [8] -->
m

<!-- b003228 | prose | pages [8] -->
m

<!-- b003229 | prose | pages [8] -->
m

<!-- b003230 | prose | pages [8] -->
m

<!-- b003231 | prose | pages [8] -->
m

<!-- b003232 | prose | pages [8] -->
m

<!-- b003233 | prose | pages [8] -->
m

<!-- b003234 | prose | pages [8] -->
m

<!-- b003235 | prose | pages [8] -->
m

<!-- b003236 | prose | pages [8] -->
m

<!-- b003237 | prose | pages [8] -->
m

<!-- b003238 | prose | pages [8] -->
m

<!-- b003239 | prose | pages [8] -->
m

<!-- b003240 | prose | pages [8] -->
m

<!-- b003241 | prose | pages [8] -->
m

<!-- b003242 | prose | pages [8] -->
m

<!-- b003243 | prose | pages [8] -->
m

<!-- b003244 | prose | pages [8] -->
m

<!-- b003245 | prose | pages [8] -->
m

<!-- b003246 | prose | pages [8] -->
m

<!-- b003247 | prose | pages [8] -->
m

<!-- b003248 | prose | pages [8] -->
m

<!-- b003249 | prose | pages [8] -->
m

<!-- b003250 | prose | pages [8] -->
m

<!-- b003251 | prose | pages [8] -->
m

<!-- b003252 | prose | pages [8] -->
m

<!-- b003253 | prose | pages [8] -->
m

<!-- b003254 | prose | pages [8] -->
m

<!-- b003255 | prose | pages [8] -->
m

<!-- b003256 | prose | pages [8] -->
m

<!-- b003257 | prose | pages [8] -->
m

<!-- b003258 | prose | pages [8] -->
m

<!-- b003259 | prose | pages [8] -->
m

<!-- b003260 | prose | pages [8] -->
m

<!-- b003261 | prose | pages [8] -->
m

<!-- b003262 | prose | pages [8] -->
m

<!-- b003263 | prose | pages [8] -->
m

<!-- b003264 | prose | pages [8] -->
m

<!-- b003265 | prose | pages [8] -->
m

<!-- b003266 | prose | pages [8] -->
m

<!-- b003267 | prose | pages [8] -->
m

<!-- b003268 | prose | pages [8] -->
m

<!-- b003269 | prose | pages [8] -->
m

<!-- b003270 | prose | pages [8] -->
m

<!-- b003271 | prose | pages [8] -->
m

<!-- b003272 | prose | pages [8] -->
m

<!-- b003273 | prose | pages [8] -->
m

<!-- b003274 | prose | pages [8] -->
m

<!-- b003275 | prose | pages [8] -->
m

<!-- b003276 | prose | pages [8] -->
m

<!-- b003277 | prose | pages [8] -->
m

<!-- b003278 | prose | pages [8] -->
m

<!-- b003279 | prose | pages [8] -->
m

<!-- b003280 | prose | pages [8] -->
m

<!-- b003281 | prose | pages [8] -->
m

<!-- b003282 | prose | pages [8] -->
m

<!-- b003283 | prose | pages [8] -->
m

<!-- b003284 | prose | pages [8] -->
m

<!-- b003285 | prose | pages [8] -->
m

<!-- b003286 | prose | pages [8] -->
m

<!-- b003287 | prose | pages [8] -->
m

<!-- b003288 | prose | pages [8] -->
m

<!-- b003289 | prose | pages [8] -->
m

<!-- b003290 | prose | pages [8] -->
m

<!-- b003291 | prose | pages [8] -->
m

<!-- b003292 | prose | pages [8] -->
m

<!-- b003293 | prose | pages [8] -->
m

<!-- b003294 | prose | pages [8] -->
m

<!-- b003295 | prose | pages [8] -->
m

<!-- b003296 | prose | pages [8] -->
m

<!-- b003297 | prose | pages [8] -->
m

<!-- b003298 | prose | pages [8] -->
m

<!-- b003299 | prose | pages [8] -->
m

<!-- b003300 | prose | pages [8] -->
m

<!-- b003301 | prose | pages [8] -->
m

<!-- b003302 | prose | pages [8] -->
m

<!-- b003303 | prose | pages [8] -->
m

<!-- b003304 | prose | pages [8] -->
m

<!-- b003305 | prose | pages [8] -->
m

<!-- b003306 | prose | pages [8] -->
m

<!-- b003307 | prose | pages [8] -->
m

<!-- b003308 | prose | pages [8] -->
m

<!-- b003309 | prose | pages [8] -->
m

<!-- b003310 | prose | pages [8] -->
m

<!-- b003311 | prose | pages [8] -->
m

<!-- b003312 | prose | pages [8] -->
m

<!-- b003313 | prose | pages [8] -->
m

<!-- b003314 | prose | pages [8] -->
m

<!-- b003315 | prose | pages [8] -->
m

<!-- b003316 | prose | pages [8] -->
m

<!-- b003317 | prose | pages [8] -->
m

<!-- b003318 | prose | pages [8] -->
m

<!-- b003319 | prose | pages [8] -->
m

<!-- b003320 | prose | pages [8] -->
m

<!-- b003321 | prose | pages [8] -->
m

<!-- b003322 | prose | pages [8] -->
m

<!-- b003323 | prose | pages [8] -->
m

<!-- b003324 | prose | pages [8] -->
m

<!-- b003325 | prose | pages [8] -->
m

<!-- b003326 | prose | pages [8] -->
m

<!-- b003327 | prose | pages [8] -->
m

<!-- b003328 | prose | pages [8] -->
m

<!-- b003329 | prose | pages [8] -->
m

<!-- b003330 | prose | pages [8] -->
m

<!-- b003331 | prose | pages [8] -->
m

<!-- b003332 | prose | pages [8] -->
m

<!-- b003333 | prose | pages [8] -->
m

<!-- b003334 | prose | pages [8] -->
m

<!-- b003335 | prose | pages [8] -->
m

<!-- b003336 | prose | pages [8] -->
m

<!-- b003337 | prose | pages [8] -->
m

<!-- b003338 | prose | pages [8] -->
m

<!-- b003339 | prose | pages [8] -->
m

<!-- b003340 | prose | pages [8] -->
m

<!-- b003341 | prose | pages [8] -->
m

<!-- b003342 | prose | pages [8] -->
m

<!-- b003343 | prose | pages [8] -->
m

<!-- b003344 | prose | pages [8] -->
m

<!-- b003345 | prose | pages [8] -->
m

<!-- b003346 | prose | pages [8] -->
m

<!-- b003347 | prose | pages [8] -->
m

<!-- b003348 | prose | pages [8] -->
m

<!-- b003349 | prose | pages [8] -->
m

<!-- b003350 | prose | pages [8] -->
m

<!-- b003351 | prose | pages [8] -->
m

<!-- b003352 | prose | pages [8] -->
m

<!-- b003353 | prose | pages [8] -->
m

<!-- b003354 | prose | pages [8] -->
m

<!-- b003355 | prose | pages [8] -->
m

<!-- b003356 | prose | pages [8] -->
m

<!-- b003357 | prose | pages [8] -->
m

<!-- b003358 | prose | pages [8] -->
m

<!-- b003359 | prose | pages [8] -->
m

<!-- b003360 | prose | pages [8] -->
m

<!-- b003361 | prose | pages [8] -->
m

<!-- b003362 | prose | pages [8] -->
m

<!-- b003363 | prose | pages [8] -->
m

<!-- b003364 | prose | pages [8] -->
m

<!-- b003365 | prose | pages [8] -->
m

<!-- b003366 | prose | pages [8] -->
m

<!-- b003367 | prose | pages [8] -->
m

<!-- b003368 | prose | pages [8] -->
m

<!-- b003369 | prose | pages [8] -->
m

<!-- b003370 | prose | pages [8] -->
m

<!-- b003371 | prose | pages [8] -->
m

<!-- b003372 | prose | pages [8] -->
m

<!-- b003373 | prose | pages [8] -->
m

<!-- b003374 | prose | pages [8] -->
m

<!-- b003375 | prose | pages [8] -->
m

<!-- b003376 | prose | pages [8] -->
m

<!-- b003377 | prose | pages [8] -->
m

<!-- b003378 | prose | pages [8] -->
m

<!-- b003379 | prose | pages [8] -->
m

<!-- b003380 | prose | pages [8] -->
m

<!-- b003381 | prose | pages [8] -->
m

<!-- b003382 | prose | pages [8] -->
m

<!-- b003383 | prose | pages [8] -->
m

<!-- b003384 | prose | pages [8] -->
m

<!-- b003385 | prose | pages [8] -->
m

<!-- b003386 | prose | pages [8] -->
m

<!-- b003387 | prose | pages [8] -->
m

<!-- b003388 | prose | pages [8] -->
m

<!-- b003389 | prose | pages [8] -->
m

<!-- b003390 | prose | pages [8] -->
m

<!-- b003391 | prose | pages [8] -->
m

<!-- b003392 | prose | pages [8] -->
m

<!-- b003393 | prose | pages [8] -->
m

<!-- b003394 | prose | pages [8] -->
m

<!-- b003395 | prose | pages [8] -->
m

<!-- b003396 | prose | pages [8] -->
m

<!-- b003397 | prose | pages [8] -->
m

<!-- b003398 | prose | pages [8] -->
m

<!-- b003399 | prose | pages [8] -->
m

<!-- b003400 | prose | pages [8] -->
m

<!-- b003401 | prose | pages [8] -->
m

<!-- b003402 | prose | pages [8] -->
m

<!-- b003403 | prose | pages [8] -->
m

<!-- b003404 | prose | pages [8] -->
m

<!-- b003405 | prose | pages [8] -->
m

<!-- b003406 | prose | pages [8] -->
m

<!-- b003407 | prose | pages [8] -->
m

<!-- b003408 | prose | pages [8] -->
m

<!-- b003409 | prose | pages [8] -->
m

<!-- b003410 | prose | pages [8] -->
m

<!-- b003411 | prose | pages [8] -->
m

<!-- b003412 | prose | pages [8] -->
m

<!-- b003413 | prose | pages [8] -->
m

<!-- b003414 | prose | pages [8] -->
m

<!-- b003415 | prose | pages [8] -->
m

<!-- b003416 | prose | pages [8] -->
m

<!-- b003417 | prose | pages [8] -->
m

<!-- b003418 | prose | pages [8] -->
m

<!-- b003419 | prose | pages [8] -->
m

<!-- b003420 | prose | pages [8] -->
m

<!-- b003421 | prose | pages [8] -->
m

<!-- b003422 | prose | pages [8] -->
m

<!-- b003423 | prose | pages [8] -->
m

<!-- b003424 | prose | pages [8] -->
m

<!-- b003425 | prose | pages [8] -->
m

<!-- b003426 | prose | pages [8] -->
m

<!-- b003427 | prose | pages [8] -->
m

<!-- b003428 | prose | pages [8] -->
m

<!-- b003429 | prose | pages [8] -->
m

<!-- b003430 | prose | pages [8] -->
m

<!-- b003431 | prose | pages [8] -->
m

<!-- b003432 | prose | pages [8] -->
m

<!-- b003433 | prose | pages [8] -->
m

<!-- b003434 | prose | pages [8] -->
m

<!-- b003435 | prose | pages [8] -->
m

<!-- b003436 | prose | pages [8] -->
m

<!-- b003437 | prose | pages [8] -->
m

<!-- b003438 | prose | pages [8] -->
m

<!-- b003439 | prose | pages [8] -->
m

<!-- b003440 | prose | pages [8] -->
m

<!-- b003441 | prose | pages [8] -->
m

<!-- b003442 | prose | pages [8] -->
m

<!-- b003443 | prose | pages [8] -->
m

<!-- b003444 | prose | pages [8] -->
m

<!-- b003445 | prose | pages [8] -->
m

<!-- b003446 | prose | pages [8] -->
m

<!-- b003447 | prose | pages [8] -->
m

<!-- b003448 | prose | pages [8] -->
m

<!-- b003449 | prose | pages [8] -->
m

<!-- b003450 | prose | pages [8] -->
m

<!-- b003451 | prose | pages [8] -->
m

<!-- b003452 | prose | pages [8] -->
m

<!-- b003453 | prose | pages [8] -->
m

<!-- b003454 | prose | pages [8] -->
m

<!-- b003455 | prose | pages [8] -->
m

<!-- b003456 | prose | pages [8] -->
m

<!-- b003457 | prose | pages [8] -->
m

<!-- b003458 | prose | pages [8] -->
m

<!-- b003459 | prose | pages [8] -->
m

<!-- b003460 | prose | pages [8] -->
m

<!-- b003461 | prose | pages [8] -->
m

<!-- b003462 | prose | pages [8] -->
m

<!-- b003463 | prose | pages [8] -->
m

<!-- b003464 | prose | pages [8] -->
m

<!-- b003465 | prose | pages [8] -->
m

<!-- b003466 | prose | pages [8] -->
m

<!-- b003467 | prose | pages [8] -->
m

<!-- b003468 | prose | pages [8] -->
m

<!-- b003469 | prose | pages [8] -->
m

<!-- b003470 | prose | pages [8] -->
m

<!-- b003471 | prose | pages [8] -->
m

<!-- b003472 | prose | pages [8] -->
m

<!-- b003473 | prose | pages [8] -->
m

<!-- b003474 | prose | pages [8] -->
m

<!-- b003475 | prose | pages [8] -->
m

<!-- b003476 | prose | pages [8] -->
m

<!-- b003477 | prose | pages [8] -->
m

<!-- b003478 | prose | pages [8] -->
m

<!-- b003479 | prose | pages [8] -->
m

<!-- b003480 | prose | pages [8] -->
m

<!-- b003481 | prose | pages [8] -->
m

<!-- b003482 | prose | pages [8] -->
m

<!-- b003483 | prose | pages [8] -->
m

<!-- b003484 | prose | pages [8] -->
m

<!-- b003485 | prose | pages [8] -->
m

<!-- b003486 | prose | pages [8] -->
m

<!-- b003487 | prose | pages [8] -->
m

<!-- b003488 | prose | pages [8] -->
m

<!-- b003489 | prose | pages [8] -->
m

<!-- b003490 | prose | pages [8] -->
m

<!-- b003491 | prose | pages [8] -->
m

<!-- b003492 | prose | pages [8] -->
m

<!-- b003493 | prose | pages [8] -->
m

<!-- b003494 | prose | pages [8] -->
m

<!-- b003495 | prose | pages [8] -->
m

<!-- b003496 | prose | pages [8] -->
m

<!-- b003497 | prose | pages [8] -->
m

<!-- b003498 | prose | pages [8] -->
m

<!-- b003499 | prose | pages [8] -->
m

<!-- b003500 | prose | pages [8] -->
m

<!-- b003501 | prose | pages [8] -->
m

<!-- b003502 | prose | pages [8] -->
m

<!-- b003503 | prose | pages [8] -->
m

<!-- b003504 | prose | pages [8] -->
m

<!-- b003505 | prose | pages [8] -->
m

<!-- b003506 | prose | pages [8] -->
m

<!-- b003507 | prose | pages [8] -->
m

<!-- b003508 | prose | pages [8] -->
m

<!-- b003509 | prose | pages [8] -->
m

<!-- b003510 | prose | pages [8] -->
m

<!-- b003511 | prose | pages [8] -->
m

<!-- b003512 | prose | pages [8] -->
m

<!-- b003513 | prose | pages [8] -->
m

<!-- b003514 | prose | pages [8] -->
m

<!-- b003515 | prose | pages [8] -->
m

<!-- b003516 | prose | pages [8] -->
m

<!-- b003517 | prose | pages [8] -->
m

<!-- b003518 | prose | pages [8] -->
m

<!-- b003519 | prose | pages [8] -->
m

<!-- b003520 | prose | pages [8] -->
m

<!-- b003521 | prose | pages [8] -->
m

<!-- b003522 | prose | pages [8] -->
m

<!-- b003523 | prose | pages [8] -->
m

<!-- b003524 | prose | pages [8] -->
m

<!-- b003525 | prose | pages [8] -->
m

<!-- b003526 | prose | pages [8] -->
m

<!-- b003527 | prose | pages [8] -->
m

<!-- b003528 | prose | pages [8] -->
m

<!-- b003529 | prose | pages [8] -->
m

<!-- b003530 | prose | pages [8] -->
m

<!-- b003531 | prose | pages [8] -->
m

<!-- b003532 | prose | pages [8] -->
m

<!-- b003533 | prose | pages [8] -->
m

<!-- b003534 | prose | pages [8] -->
m

<!-- b003535 | prose | pages [8] -->
m

<!-- b003536 | prose | pages [8] -->
m

<!-- b003537 | prose | pages [8] -->
m

<!-- b003538 | prose | pages [8] -->
m

<!-- b003539 | prose | pages [8] -->
m

<!-- b003540 | prose | pages [8] -->
m

<!-- b003541 | prose | pages [8] -->
m

<!-- b003542 | prose | pages [8] -->
m

<!-- b003543 | prose | pages [8] -->
m

<!-- b003544 | prose | pages [8] -->
m

<!-- b003545 | prose | pages [8] -->
m

<!-- b003546 | prose | pages [8] -->
m

<!-- b003547 | prose | pages [8] -->
m

<!-- b003548 | prose | pages [8] -->
m

<!-- b003549 | prose | pages [8] -->
m

<!-- b003550 | prose | pages [8] -->
m

<!-- b003551 | prose | pages [8] -->
m

<!-- b003552 | prose | pages [8] -->
m

<!-- b003553 | prose | pages [8] -->
m

<!-- b003554 | prose | pages [8] -->
m

<!-- b003555 | prose | pages [8] -->
m

<!-- b003556 | prose | pages [8] -->
m

<!-- b003557 | prose | pages [8] -->
m

<!-- b003558 | prose | pages [8] -->
m

<!-- b003559 | prose | pages [8] -->
m

<!-- b003560 | prose | pages [8] -->
m

<!-- b003561 | prose | pages [8] -->
m

<!-- b003562 | prose | pages [8] -->
m

<!-- b003563 | prose | pages [8] -->
m

<!-- b003564 | prose | pages [8] -->
m

<!-- b003565 | prose | pages [8] -->
m

<!-- b003566 | prose | pages [8] -->
m

<!-- b003567 | prose | pages [8] -->
m

<!-- b003568 | prose | pages [8] -->
m

<!-- b003569 | prose | pages [8] -->
m

<!-- b003570 | prose | pages [8] -->
m

<!-- b003571 | prose | pages [8] -->
m

<!-- b003572 | prose | pages [8] -->
m

<!-- b003573 | prose | pages [8] -->
m

<!-- b003574 | prose | pages [8] -->
m

<!-- b003575 | prose | pages [8] -->
m

<!-- b003576 | prose | pages [8] -->
m

<!-- b003577 | prose | pages [8] -->
m

<!-- b003578 | prose | pages [8] -->
m

<!-- b003579 | prose | pages [8] -->
m

<!-- b003580 | prose | pages [8] -->
m

<!-- b003581 | prose | pages [8] -->
m

<!-- b003582 | prose | pages [8] -->
m

<!-- b003583 | prose | pages [8] -->
m

<!-- b003584 | prose | pages [8] -->
m

<!-- b003585 | prose | pages [8] -->
m

<!-- b003586 | prose | pages [8] -->
m

<!-- b003587 | prose | pages [8] -->
m

<!-- b003588 | prose | pages [8] -->
m

<!-- b003589 | prose | pages [8] -->
m

<!-- b003590 | prose | pages [8] -->
m

<!-- b003591 | prose | pages [8] -->
m

<!-- b003592 | prose | pages [8] -->
m

<!-- b003593 | prose | pages [8] -->
m

<!-- b003594 | prose | pages [8] -->
m

<!-- b003595 | prose | pages [8] -->
m

<!-- b003596 | prose | pages [8] -->
m

<!-- b003597 | prose | pages [8] -->
m

<!-- b003598 | prose | pages [8] -->
m

<!-- b003599 | prose | pages [8] -->
m

<!-- b003600 | prose | pages [8] -->
m

<!-- b003601 | prose | pages [8] -->
m

<!-- b003602 | prose | pages [8] -->
m

<!-- b003603 | prose | pages [8] -->
m

<!-- b003604 | prose | pages [8] -->
m

<!-- b003605 | prose | pages [8] -->
m

<!-- b003606 | prose | pages [8] -->
m

<!-- b003607 | prose | pages [8] -->
m

<!-- b003608 | prose | pages [8] -->
m

<!-- b003609 | prose | pages [8] -->
m

<!-- b003610 | prose | pages [8] -->
m

<!-- b003611 | prose | pages [8] -->
m

<!-- b003612 | prose | pages [8] -->
m

<!-- b003613 | prose | pages [8] -->
m

<!-- b003614 | prose | pages [8] -->
m

<!-- b003615 | prose | pages [8] -->
m

<!-- b003616 | prose | pages [8] -->
m

<!-- b003617 | prose | pages [8] -->
m

<!-- b003618 | prose | pages [8] -->
m

<!-- b003619 | prose | pages [8] -->
m

<!-- b003620 | prose | pages [8] -->
m

<!-- b003621 | prose | pages [8] -->
m

<!-- b003622 | prose | pages [8] -->
m

<!-- b003623 | prose | pages [8] -->
m

<!-- b003624 | prose | pages [8] -->
m

<!-- b003625 | prose | pages [8] -->
m

<!-- b003626 | prose | pages [8] -->
m

<!-- b003627 | prose | pages [8] -->
m

<!-- b003628 | prose | pages [8] -->
m

<!-- b003629 | prose | pages [8] -->
m

<!-- b003630 | prose | pages [8] -->
m

<!-- b003631 | prose | pages [8] -->
m

<!-- b003632 | prose | pages [8] -->
m

<!-- b003633 | prose | pages [8] -->
m

<!-- b003634 | prose | pages [8] -->
m

<!-- b003635 | prose | pages [8] -->
m

<!-- b003636 | prose | pages [8] -->
m

<!-- b003637 | prose | pages [8] -->
m

<!-- b003638 | prose | pages [8] -->
m

<!-- b003639 | prose | pages [8] -->
m

<!-- b003640 | prose | pages [8] -->
m

<!-- b003641 | prose | pages [8] -->
m

<!-- b003642 | prose | pages [8] -->
m

<!-- b003643 | prose | pages [8] -->
m

<!-- b003644 | prose | pages [8] -->
m

<!-- b003645 | prose | pages [8] -->
m

<!-- b003646 | prose | pages [8] -->
m

<!-- b003647 | prose | pages [8] -->
m

<!-- b003648 | prose | pages [8] -->
m

<!-- b003649 | prose | pages [8] -->
m

<!-- b003650 | prose | pages [8] -->
m

<!-- b003651 | prose | pages [8] -->
m

<!-- b003652 | prose | pages [8] -->
m

<!-- b003653 | prose | pages [8] -->
m

<!-- b003654 | prose | pages [8] -->
m

<!-- b003655 | prose | pages [8] -->
m

<!-- b003656 | prose | pages [8] -->
m

<!-- b003657 | prose | pages [8] -->
m

<!-- b003658 | prose | pages [8] -->
m

<!-- b003659 | prose | pages [8] -->
m

<!-- b003660 | prose | pages [8] -->
m

<!-- b003661 | prose | pages [8] -->
m

<!-- b003662 | prose | pages [8] -->
m

<!-- b003663 | prose | pages [8] -->
m

<!-- b003664 | caption | pages [8] -->
Figure 6: Presentation of ﬁve types of cybercrime indicators by country

<!-- b003665 | prose | pages [8] -->
This chart illustrates the performance of different countries across various cybercrime- related indicators, including target count, success rate, thwart rate, reporting rate, and prosecution rate. The data shows that the United States leads signiﬁcantly in the num- ber of cybercrime incidents (7,225 cases), with a high success rate (0.769). However, its reporting rate (0.013) and prosecution rate (0.097) are relatively low, highlighting the issue of cybercrime concealment. The United Kingdom stands out in prosecution rate (0.122), while Canada demonstrates strong performance with a relatively high success

<!-- b003666 | prose | pages [8] -->
关注数学模型

<!-- b003667 | prose | pages [8] -->
rate (0.752). Notably, although South Korea has fewer incidents (49 cases), it exhibits a

<!-- b003668 | furniture | pages [8] -->
2

<!-- b003669 | furniture | pages [8] -->
MATHmodels

<!-- b003670 | furniture | pages [8] -->
获取更多资讯

<!-- b003671 | furniture | pages [9] -->
Team # 2521039

<!-- b003672 | furniture | pages [9] -->
Page 9 of 25

<!-- b003673 | prose | pages [9] -->
higher thwart rate (0.336), which may reﬂect its advantage in cybersecurity defense ca- pabilities. Overall, most countries show extremely low reporting rates (ranging from 0.007 to 0.014), which may be inﬂuenced by national policies or cultural factors, as well as the signiﬁcant impact of organizational behavior. Many institutions, such as investment ﬁrms, tend to conceal hacking incidents and opt to pay ransoms to pre- vent customers or potential clients from becoming aware of their security vulnerabil- ities. This phenomenon further reduces the reporting rate and complicates the issue of cybercrime. Additionally, the differences in prosecution rates reveal disparities in legal frameworks and law enforcement capabilities across countries. For example, the United Kingdom and the United States have relatively high prosecution rates, while France and Germany perform comparatively lower. To effectively address cybercrime, countries should enhance incident disclosure rates and strengthen international col-

<!-- b003674 | prose | pages [9] -->
微信公众号：数学模型

<!-- b003675 | prose | pages [9] -->
laboration. Particular focus should be placed on countries with high incident counts, such as the United States and the United Kingdom, to optimize cybersecurity policies and response strategies.

<!-- b003676 | prose | pages [9] -->
4.3.4 Pattern Analysis

<!-- b003677 | prose | pages [9] -->
微信号：MATHmodels

<!-- b003678 | caption | pages [9] -->
Figure 7: The top ten countries by cybercrime count

<!-- b003679 | prose | pages [9] -->
By statistically analyzing the number of cybercrimes in various countries over the past decade and visualizing the top 10 countries with the highest incident counts in a bar chart, it becomes clear that the United States, United Kingdom, Canada, Aus- tralia, India, New Zealand, China, Japan, Germany, and Ireland are high-priority targets for cybercrime.

<!-- b003680 | prose | pages [9] -->
From the perspective of national development levels, the global cybercrime distri- bution exhibits signiﬁcant disparities. Developed countries report noticeably higher numbers of cybercrime incidents. For instance, countries such as the United States (7,224), United Kingdom (574), and Canada (369) are represented in dark red on the heatmap. These nations have advanced economies, well-developed internet infrastruc- tures, and high coverage rates, providing broader attack surfaces for cybercriminals. Additionally, their heavy reliance on digital technologies further increases their expo- sure, making them prime targets for cybercrime.

<!-- b003681 | prose | pages [9] -->
Additionally, small-to-medium-sized economies such as New Zealand (103) and Ireland (60) report relatively high numbers of cybercrime incidents, likely reﬂecting their reliance on internet-based economies and digital technologies, which increases their vulnerability to cybercrime.

<!-- b003682 | prose | pages [9] -->
In contrast, emerging economies such as China (65) and India (138) report signiﬁ- cantly fewer cybercrime incidents than developed nations, with no clear upward trend

<!-- b003683 | furniture | pages [10] -->
Team # 2521039

<!-- b003684 | furniture | pages [10] -->
Page 10 of 25

<!-- b003685 | prose | pages [10] -->
observed in the data. This indicates that although increasing internet penetration and globalization have created more opportunities for cybercrime, the number of incidents in emerging economies remains below expectations based on their development lev- els. Meanwhile, in poorer regions such as much of Africa, the number of cybercrime incidents is extremely low, with most countries reporting fewer than ﬁve cases, as indi- cated by light blue areas on the heatmap. This is likely due to low internet penetration

<!-- b003686 | prose | pages [10] -->
m

<!-- b003687 | prose | pages [10] -->
m

<!-- b003688 | prose | pages [10] -->
m

<!-- b003689 | prose | pages [10] -->
m

<!-- b003690 | prose | pages [10] -->
m

<!-- b003691 | prose | pages [10] -->
m

<!-- b003692 | prose | pages [10] -->
m

<!-- b003693 | prose | pages [10] -->
m

<!-- b003694 | prose | pages [10] -->
m

<!-- b003695 | prose | pages [10] -->
m

<!-- b003696 | prose | pages [10] -->
m

<!-- b003697 | prose | pages [10] -->
m

<!-- b003698 | prose | pages [10] -->
m

<!-- b003699 | prose | pages [10] -->
m

<!-- b003700 | prose | pages [10] -->
m

<!-- b003701 | prose | pages [10] -->
m

<!-- b003702 | prose | pages [10] -->
m

<!-- b003703 | prose | pages [10] -->
m

<!-- b003704 | prose | pages [10] -->
m

<!-- b003705 | prose | pages [10] -->
m

<!-- b003706 | prose | pages [10] -->
m

<!-- b003707 | prose | pages [10] -->
m

<!-- b003708 | prose | pages [10] -->
m

<!-- b003709 | prose | pages [10] -->
m

<!-- b003710 | prose | pages [10] -->
m

<!-- b003711 | prose | pages [10] -->
m

<!-- b003712 | prose | pages [10] -->
m

<!-- b003713 | prose | pages [10] -->
m

<!-- b003714 | prose | pages [10] -->
m

<!-- b003715 | prose | pages [10] -->
m

<!-- b003716 | prose | pages [10] -->
m

<!-- b003717 | prose | pages [10] -->
m

<!-- b003718 | prose | pages [10] -->
m

<!-- b003719 | prose | pages [10] -->
m

<!-- b003720 | prose | pages [10] -->
m

<!-- b003721 | prose | pages [10] -->
m

<!-- b003722 | prose | pages [10] -->
m

<!-- b003723 | prose | pages [10] -->
m

<!-- b003724 | prose | pages [10] -->
m

<!-- b003725 | prose | pages [10] -->
m

<!-- b003726 | prose | pages [10] -->
m

<!-- b003727 | prose | pages [10] -->
m

<!-- b003728 | prose | pages [10] -->
m

<!-- b003729 | prose | pages [10] -->
m

<!-- b003730 | prose | pages [10] -->
m

<!-- b003731 | prose | pages [10] -->
m

<!-- b003732 | prose | pages [10] -->
m

<!-- b003733 | prose | pages [10] -->
m

<!-- b003734 | prose | pages [10] -->
m

<!-- b003735 | prose | pages [10] -->
m

<!-- b003736 | prose | pages [10] -->
m

<!-- b003737 | prose | pages [10] -->
m

<!-- b003738 | prose | pages [10] -->
m

<!-- b003739 | prose | pages [10] -->
m

<!-- b003740 | prose | pages [10] -->
m

<!-- b003741 | prose | pages [10] -->
m

<!-- b003742 | prose | pages [10] -->
m

<!-- b003743 | prose | pages [10] -->
m

<!-- b003744 | prose | pages [10] -->
m

<!-- b003745 | prose | pages [10] -->
m

<!-- b003746 | prose | pages [10] -->
m

<!-- b003747 | prose | pages [10] -->
m

<!-- b003748 | prose | pages [10] -->
m

<!-- b003749 | prose | pages [10] -->
m

<!-- b003750 | prose | pages [10] -->
m

<!-- b003751 | prose | pages [10] -->
m

<!-- b003752 | prose | pages [10] -->
m

<!-- b003753 | prose | pages [10] -->
m

<!-- b003754 | prose | pages [10] -->
m

<!-- b003755 | prose | pages [10] -->
m

<!-- b003756 | prose | pages [10] -->
m

<!-- b003757 | prose | pages [10] -->
m

<!-- b003758 | prose | pages [10] -->
m

<!-- b003759 | prose | pages [10] -->
m

<!-- b003760 | prose | pages [10] -->
m

<!-- b003761 | prose | pages [10] -->
m

<!-- b003762 | prose | pages [10] -->
m

<!-- b003763 | prose | pages [10] -->
m

<!-- b003764 | prose | pages [10] -->
m

<!-- b003765 | prose | pages [10] -->
m

<!-- b003766 | prose | pages [10] -->
m

<!-- b003767 | prose | pages [10] -->
m

<!-- b003768 | prose | pages [10] -->
m

<!-- b003769 | prose | pages [10] -->
m

<!-- b003770 | prose | pages [10] -->
m

<!-- b003771 | prose | pages [10] -->
m

<!-- b003772 | prose | pages [10] -->
m

<!-- b003773 | prose | pages [10] -->
m

<!-- b003774 | prose | pages [10] -->
m

<!-- b003775 | prose | pages [10] -->
m

<!-- b003776 | prose | pages [10] -->
m

<!-- b003777 | prose | pages [10] -->
m

<!-- b003778 | prose | pages [10] -->
m

<!-- b003779 | prose | pages [10] -->
m

<!-- b003780 | prose | pages [10] -->
m

<!-- b003781 | prose | pages [10] -->
rates, economies largely centered around physical industries, and limited technologi- cal resources.

<!-- b003782 | prose | pages [10] -->
m

<!-- b003783 | prose | pages [10] -->
m

<!-- b003784 | prose | pages [10] -->
m

<!-- b003785 | prose | pages [10] -->
m

<!-- b003786 | prose | pages [10] -->
m

<!-- b003787 | prose | pages [10] -->
m

<!-- b003788 | prose | pages [10] -->
m

<!-- b003789 | prose | pages [10] -->
m

<!-- b003790 | prose | pages [10] -->
m

<!-- b003791 | prose | pages [10] -->
m

<!-- b003792 | prose | pages [10] -->
m

<!-- b003793 | prose | pages [10] -->
m

<!-- b003794 | prose | pages [10] -->
m

<!-- b003795 | prose | pages [10] -->
m

<!-- b003796 | prose | pages [10] -->
m

<!-- b003797 | prose | pages [10] -->
m

<!-- b003798 | prose | pages [10] -->
m

<!-- b003799 | prose | pages [10] -->
m

<!-- b003800 | prose | pages [10] -->
m

<!-- b003801 | prose | pages [10] -->
m

<!-- b003802 | prose | pages [10] -->
m

<!-- b003803 | prose | pages [10] -->
m

<!-- b003804 | prose | pages [10] -->
m

<!-- b003805 | prose | pages [10] -->
m

<!-- b003806 | prose | pages [10] -->
m

<!-- b003807 | prose | pages [10] -->
m

<!-- b003808 | prose | pages [10] -->
m

<!-- b003809 | prose | pages [10] -->
m

<!-- b003810 | prose | pages [10] -->
m

<!-- b003811 | prose | pages [10] -->
m

<!-- b003812 | prose | pages [10] -->
m

<!-- b003813 | prose | pages [10] -->
m

<!-- b003814 | prose | pages [10] -->
m

<!-- b003815 | prose | pages [10] -->
m

<!-- b003816 | prose | pages [10] -->
m

<!-- b003817 | prose | pages [10] -->
m

<!-- b003818 | prose | pages [10] -->
m

<!-- b003819 | prose | pages [10] -->
m

<!-- b003820 | prose | pages [10] -->
m

<!-- b003821 | prose | pages [10] -->
m

<!-- b003822 | prose | pages [10] -->
m

<!-- b003823 | prose | pages [10] -->
m

<!-- b003824 | prose | pages [10] -->
m

<!-- b003825 | prose | pages [10] -->
m

<!-- b003826 | prose | pages [10] -->
m

<!-- b003827 | prose | pages [10] -->
m

<!-- b003828 | prose | pages [10] -->
m

<!-- b003829 | prose | pages [10] -->
m

<!-- b003830 | prose | pages [10] -->
m

<!-- b003831 | prose | pages [10] -->
m

<!-- b003832 | prose | pages [10] -->
m

<!-- b003833 | prose | pages [10] -->
m

<!-- b003834 | prose | pages [10] -->
m

<!-- b003835 | prose | pages [10] -->
m

<!-- b003836 | prose | pages [10] -->
m

<!-- b003837 | prose | pages [10] -->
m

<!-- b003838 | prose | pages [10] -->
m

<!-- b003839 | prose | pages [10] -->
m

<!-- b003840 | prose | pages [10] -->
m

<!-- b003841 | prose | pages [10] -->
m

<!-- b003842 | prose | pages [10] -->
m

<!-- b003843 | prose | pages [10] -->
m

<!-- b003844 | prose | pages [10] -->
m

<!-- b003845 | prose | pages [10] -->
m

<!-- b003846 | prose | pages [10] -->
m

<!-- b003847 | prose | pages [10] -->
m

<!-- b003848 | prose | pages [10] -->
m

<!-- b003849 | prose | pages [10] -->
m

<!-- b003850 | prose | pages [10] -->
m

<!-- b003851 | prose | pages [10] -->
m

<!-- b003852 | prose | pages [10] -->
m

<!-- b003853 | prose | pages [10] -->
m

<!-- b003854 | prose | pages [10] -->
m

<!-- b003855 | prose | pages [10] -->
m

<!-- b003856 | prose | pages [10] -->
m

<!-- b003857 | prose | pages [10] -->
m

<!-- b003858 | prose | pages [10] -->
m

<!-- b003859 | prose | pages [10] -->
m

<!-- b003860 | prose | pages [10] -->
m

<!-- b003861 | prose | pages [10] -->
m

<!-- b003862 | prose | pages [10] -->
m

<!-- b003863 | prose | pages [10] -->
m

<!-- b003864 | prose | pages [10] -->
m

<!-- b003865 | prose | pages [10] -->
m

<!-- b003866 | prose | pages [10] -->
m

<!-- b003867 | prose | pages [10] -->
m

<!-- b003868 | prose | pages [10] -->
m

<!-- b003869 | prose | pages [10] -->
m

<!-- b003870 | prose | pages [10] -->
m

<!-- b003871 | prose | pages [10] -->
m

<!-- b003872 | prose | pages [10] -->
m

<!-- b003873 | prose | pages [10] -->
m

<!-- b003874 | prose | pages [10] -->
m

<!-- b003875 | prose | pages [10] -->
m

<!-- b003876 | prose | pages [10] -->
m

<!-- b003877 | prose | pages [10] -->
m

<!-- b003878 | prose | pages [10] -->
m

<!-- b003879 | prose | pages [10] -->
m

<!-- b003880 | prose | pages [10] -->
m

<!-- b003881 | prose | pages [10] -->
m

<!-- b003882 | prose | pages [10] -->
m

<!-- b003883 | prose | pages [10] -->
m

<!-- b003884 | prose | pages [10] -->
m

<!-- b003885 | prose | pages [10] -->
m

<!-- b003886 | prose | pages [10] -->
m

<!-- b003887 | prose | pages [10] -->
m

<!-- b003888 | prose | pages [10] -->
m

<!-- b003889 | prose | pages [10] -->
m

<!-- b003890 | prose | pages [10] -->
m

<!-- b003891 | prose | pages [10] -->
m

<!-- b003892 | prose | pages [10] -->
m

<!-- b003893 | prose | pages [10] -->
m

<!-- b003894 | prose | pages [10] -->
m

<!-- b003895 | prose | pages [10] -->
m

<!-- b003896 | prose | pages [10] -->
m

<!-- b003897 | prose | pages [10] -->
m

<!-- b003898 | prose | pages [10] -->
m

<!-- b003899 | prose | pages [10] -->
m

<!-- b003900 | prose | pages [10] -->
m

<!-- b003901 | prose | pages [10] -->
m

<!-- b003902 | prose | pages [10] -->
m

<!-- b003903 | prose | pages [10] -->
m

<!-- b003904 | prose | pages [10] -->
m

<!-- b003905 | prose | pages [10] -->
m

<!-- b003906 | prose | pages [10] -->
m

<!-- b003907 | prose | pages [10] -->
m

<!-- b003908 | prose | pages [10] -->
m

<!-- b003909 | prose | pages [10] -->
m

<!-- b003910 | prose | pages [10] -->
m

<!-- b003911 | prose | pages [10] -->
m

<!-- b003912 | prose | pages [10] -->
m

<!-- b003913 | prose | pages [10] -->
m

<!-- b003914 | prose | pages [10] -->
m

<!-- b003915 | prose | pages [10] -->
m

<!-- b003916 | prose | pages [10] -->
m

<!-- b003917 | prose | pages [10] -->
m

<!-- b003918 | prose | pages [10] -->
m

<!-- b003919 | prose | pages [10] -->
m

<!-- b003920 | prose | pages [10] -->
m

<!-- b003921 | prose | pages [10] -->
m

<!-- b003922 | prose | pages [10] -->
m

<!-- b003923 | prose | pages [10] -->
m

<!-- b003924 | prose | pages [10] -->
m

<!-- b003925 | prose | pages [10] -->
m

<!-- b003926 | prose | pages [10] -->
m

<!-- b003927 | prose | pages [10] -->
m

<!-- b003928 | prose | pages [10] -->
m

<!-- b003929 | prose | pages [10] -->
m

<!-- b003930 | prose | pages [10] -->
m

<!-- b003931 | prose | pages [10] -->
m

<!-- b003932 | prose | pages [10] -->
m

<!-- b003933 | prose | pages [10] -->
m

<!-- b003934 | prose | pages [10] -->
m

<!-- b003935 | prose | pages [10] -->
m

<!-- b003936 | prose | pages [10] -->
m

<!-- b003937 | prose | pages [10] -->
m

<!-- b003938 | prose | pages [10] -->
m

<!-- b003939 | prose | pages [10] -->
m

<!-- b003940 | prose | pages [10] -->
m

<!-- b003941 | prose | pages [10] -->
m

<!-- b003942 | prose | pages [10] -->
m

<!-- b003943 | prose | pages [10] -->
m

<!-- b003944 | prose | pages [10] -->
m

<!-- b003945 | prose | pages [10] -->
m

<!-- b003946 | prose | pages [10] -->
m

<!-- b003947 | prose | pages [10] -->
m

<!-- b003948 | prose | pages [10] -->
m

<!-- b003949 | prose | pages [10] -->
m

<!-- b003950 | prose | pages [10] -->
m

<!-- b003951 | prose | pages [10] -->
m

<!-- b003952 | prose | pages [10] -->
m

<!-- b003953 | prose | pages [10] -->
m

<!-- b003954 | prose | pages [10] -->
m

<!-- b003955 | prose | pages [10] -->
m

<!-- b003956 | prose | pages [10] -->
m

<!-- b003957 | prose | pages [10] -->
m

<!-- b003958 | prose | pages [10] -->
m

<!-- b003959 | prose | pages [10] -->
m

<!-- b003960 | prose | pages [10] -->
m

<!-- b003961 | prose | pages [10] -->
m

<!-- b003962 | prose | pages [10] -->
m

<!-- b003963 | prose | pages [10] -->
m

<!-- b003964 | prose | pages [10] -->
m

<!-- b003965 | prose | pages [10] -->
m

<!-- b003966 | prose | pages [10] -->
m

<!-- b003967 | prose | pages [10] -->
m

<!-- b003968 | prose | pages [10] -->
m

<!-- b003969 | prose | pages [10] -->
m

<!-- b003970 | prose | pages [10] -->
m

<!-- b003971 | prose | pages [10] -->
m

<!-- b003972 | prose | pages [10] -->
m

<!-- b003973 | prose | pages [10] -->
m

<!-- b003974 | prose | pages [10] -->
m

<!-- b003975 | prose | pages [10] -->
m

<!-- b003976 | prose | pages [10] -->
m

<!-- b003977 | prose | pages [10] -->
m

<!-- b003978 | prose | pages [10] -->
m

<!-- b003979 | prose | pages [10] -->
m

<!-- b003980 | prose | pages [10] -->
m

<!-- b003981 | prose | pages [10] -->
m

<!-- b003982 | prose | pages [10] -->
m

<!-- b003983 | prose | pages [10] -->
m

<!-- b003984 | prose | pages [10] -->
m

<!-- b003985 | prose | pages [10] -->
m

<!-- b003986 | prose | pages [10] -->
m

<!-- b003987 | prose | pages [10] -->
m

<!-- b003988 | prose | pages [10] -->
m

<!-- b003989 | prose | pages [10] -->
m

<!-- b003990 | prose | pages [10] -->
m

<!-- b003991 | prose | pages [10] -->
m

<!-- b003992 | prose | pages [10] -->
m

<!-- b003993 | prose | pages [10] -->
m

<!-- b003994 | prose | pages [10] -->
m

<!-- b003995 | prose | pages [10] -->
m

<!-- b003996 | prose | pages [10] -->
m

<!-- b003997 | prose | pages [10] -->
m

<!-- b003998 | prose | pages [10] -->
m

<!-- b003999 | prose | pages [10] -->
m

<!-- b004000 | prose | pages [10] -->
m

<!-- b004001 | prose | pages [10] -->
m

<!-- b004002 | prose | pages [10] -->
m

<!-- b004003 | prose | pages [10] -->
m

<!-- b004004 | prose | pages [10] -->
m

<!-- b004005 | prose | pages [10] -->
m

<!-- b004006 | prose | pages [10] -->
m

<!-- b004007 | prose | pages [10] -->
m

<!-- b004008 | prose | pages [10] -->
m

<!-- b004009 | prose | pages [10] -->
m

<!-- b004010 | prose | pages [10] -->
m

<!-- b004011 | prose | pages [10] -->
m

<!-- b004012 | prose | pages [10] -->
m

<!-- b004013 | prose | pages [10] -->
m

<!-- b004014 | prose | pages [10] -->
m

<!-- b004015 | prose | pages [10] -->
m

<!-- b004016 | prose | pages [10] -->
m

<!-- b004017 | prose | pages [10] -->
m

<!-- b004018 | prose | pages [10] -->
m

<!-- b004019 | prose | pages [10] -->
m

<!-- b004020 | prose | pages [10] -->
m

<!-- b004021 | prose | pages [10] -->
m

<!-- b004022 | prose | pages [10] -->
m

<!-- b004023 | prose | pages [10] -->
m

<!-- b004024 | prose | pages [10] -->
m

<!-- b004025 | prose | pages [10] -->
m

<!-- b004026 | prose | pages [10] -->
m

<!-- b004027 | prose | pages [10] -->
m

<!-- b004028 | prose | pages [10] -->
m

<!-- b004029 | prose | pages [10] -->
m

<!-- b004030 | prose | pages [10] -->
m

<!-- b004031 | prose | pages [10] -->
m

<!-- b004032 | prose | pages [10] -->
m

<!-- b004033 | prose | pages [10] -->
m

<!-- b004034 | prose | pages [10] -->
m

<!-- b004035 | prose | pages [10] -->
m

<!-- b004036 | prose | pages [10] -->
m

<!-- b004037 | prose | pages [10] -->
m

<!-- b004038 | prose | pages [10] -->
m

<!-- b004039 | prose | pages [10] -->
m

<!-- b004040 | prose | pages [10] -->
m

<!-- b004041 | prose | pages [10] -->
m

<!-- b004042 | prose | pages [10] -->
m

<!-- b004043 | prose | pages [10] -->
m

<!-- b004044 | prose | pages [10] -->
m

<!-- b004045 | prose | pages [10] -->
m

<!-- b004046 | prose | pages [10] -->
m

<!-- b004047 | prose | pages [10] -->
m

<!-- b004048 | prose | pages [10] -->
m

<!-- b004049 | prose | pages [10] -->
m

<!-- b004050 | prose | pages [10] -->
m

<!-- b004051 | prose | pages [10] -->
m

<!-- b004052 | prose | pages [10] -->
m

<!-- b004053 | prose | pages [10] -->
m

<!-- b004054 | prose | pages [10] -->
m

<!-- b004055 | prose | pages [10] -->
m

<!-- b004056 | prose | pages [10] -->
m

<!-- b004057 | prose | pages [10] -->
m

<!-- b004058 | prose | pages [10] -->
m

<!-- b004059 | prose | pages [10] -->
m

<!-- b004060 | prose | pages [10] -->
m

<!-- b004061 | prose | pages [10] -->
m

<!-- b004062 | prose | pages [10] -->
m

<!-- b004063 | prose | pages [10] -->
m

<!-- b004064 | prose | pages [10] -->
m

<!-- b004065 | prose | pages [10] -->
m

<!-- b004066 | prose | pages [10] -->
m

<!-- b004067 | prose | pages [10] -->
m

<!-- b004068 | prose | pages [10] -->
m

<!-- b004069 | prose | pages [10] -->
m

<!-- b004070 | prose | pages [10] -->
m

<!-- b004071 | prose | pages [10] -->
m

<!-- b004072 | prose | pages [10] -->
m

<!-- b004073 | prose | pages [10] -->
m

<!-- b004074 | prose | pages [10] -->
m

<!-- b004075 | prose | pages [10] -->
m

<!-- b004076 | prose | pages [10] -->
m

<!-- b004077 | prose | pages [10] -->
m

<!-- b004078 | prose | pages [10] -->
m

<!-- b004079 | prose | pages [10] -->
m

<!-- b004080 | prose | pages [10] -->
m

<!-- b004081 | prose | pages [10] -->
m

<!-- b004082 | prose | pages [10] -->
m

<!-- b004083 | prose | pages [10] -->
m

<!-- b004084 | prose | pages [10] -->
m

<!-- b004085 | prose | pages [10] -->
m

<!-- b004086 | prose | pages [10] -->
m

<!-- b004087 | prose | pages [10] -->
m

<!-- b004088 | prose | pages [10] -->
m

<!-- b004089 | prose | pages [10] -->
m

<!-- b004090 | prose | pages [10] -->
m

<!-- b004091 | prose | pages [10] -->
m

<!-- b004092 | prose | pages [10] -->
m

<!-- b004093 | prose | pages [10] -->
m

<!-- b004094 | prose | pages [10] -->
m

<!-- b004095 | prose | pages [10] -->
m

<!-- b004096 | prose | pages [10] -->
m

<!-- b004097 | prose | pages [10] -->
m

<!-- b004098 | prose | pages [10] -->
m

<!-- b004099 | prose | pages [10] -->
m

<!-- b004100 | prose | pages [10] -->
m

<!-- b004101 | prose | pages [10] -->
m

<!-- b004102 | prose | pages [10] -->
m

<!-- b004103 | prose | pages [10] -->
m

<!-- b004104 | prose | pages [10] -->
m

<!-- b004105 | prose | pages [10] -->
m

<!-- b004106 | prose | pages [10] -->
m

<!-- b004107 | prose | pages [10] -->
m

<!-- b004108 | prose | pages [10] -->
m

<!-- b004109 | prose | pages [10] -->
m

<!-- b004110 | prose | pages [10] -->
m

<!-- b004111 | prose | pages [10] -->
m

<!-- b004112 | prose | pages [10] -->
m

<!-- b004113 | prose | pages [10] -->
m

<!-- b004114 | prose | pages [10] -->
m

<!-- b004115 | prose | pages [10] -->
m

<!-- b004116 | prose | pages [10] -->
From a population size perspective, China and India, despite their large popula-

<!-- b004117 | prose | pages [10] -->
m

<!-- b004118 | prose | pages [10] -->
m

<!-- b004119 | prose | pages [10] -->
m

<!-- b004120 | prose | pages [10] -->
m

<!-- b004121 | prose | pages [10] -->
m

<!-- b004122 | prose | pages [10] -->
m

<!-- b004123 | prose | pages [10] -->
m

<!-- b004124 | prose | pages [10] -->
m

<!-- b004125 | prose | pages [10] -->
m

<!-- b004126 | prose | pages [10] -->
m

<!-- b004127 | prose | pages [10] -->
m

<!-- b004128 | prose | pages [10] -->
m

<!-- b004129 | prose | pages [10] -->
m

<!-- b004130 | prose | pages [10] -->
m

<!-- b004131 | prose | pages [10] -->
m

<!-- b004132 | prose | pages [10] -->
m

<!-- b004133 | prose | pages [10] -->
m

<!-- b004134 | prose | pages [10] -->
m

<!-- b004135 | prose | pages [10] -->
m

<!-- b004136 | prose | pages [10] -->
m

<!-- b004137 | prose | pages [10] -->
m

<!-- b004138 | prose | pages [10] -->
m

<!-- b004139 | prose | pages [10] -->
m

<!-- b004140 | prose | pages [10] -->
m

<!-- b004141 | prose | pages [10] -->
m

<!-- b004142 | prose | pages [10] -->
m

<!-- b004143 | prose | pages [10] -->
m

<!-- b004144 | prose | pages [10] -->
m

<!-- b004145 | prose | pages [10] -->
m

<!-- b004146 | prose | pages [10] -->
m

<!-- b004147 | prose | pages [10] -->
m

<!-- b004148 | prose | pages [10] -->
m

<!-- b004149 | prose | pages [10] -->
m

<!-- b004150 | prose | pages [10] -->
m

<!-- b004151 | prose | pages [10] -->
m

<!-- b004152 | prose | pages [10] -->
m

<!-- b004153 | prose | pages [10] -->
m

<!-- b004154 | prose | pages [10] -->
m

<!-- b004155 | prose | pages [10] -->
m

<!-- b004156 | prose | pages [10] -->
m

<!-- b004157 | prose | pages [10] -->
m

<!-- b004158 | prose | pages [10] -->
m

<!-- b004159 | prose | pages [10] -->
m

<!-- b004160 | prose | pages [10] -->
m

<!-- b004161 | prose | pages [10] -->
m

<!-- b004162 | prose | pages [10] -->
m

<!-- b004163 | prose | pages [10] -->
m

<!-- b004164 | prose | pages [10] -->
m

<!-- b004165 | prose | pages [10] -->
m

<!-- b004166 | prose | pages [10] -->
m

<!-- b004167 | prose | pages [10] -->
m

<!-- b004168 | prose | pages [10] -->
m

<!-- b004169 | prose | pages [10] -->
m

<!-- b004170 | prose | pages [10] -->
m

<!-- b004171 | prose | pages [10] -->
m

<!-- b004172 | prose | pages [10] -->
m

<!-- b004173 | prose | pages [10] -->
m

<!-- b004174 | prose | pages [10] -->
m

<!-- b004175 | prose | pages [10] -->
m

<!-- b004176 | prose | pages [10] -->
m

<!-- b004177 | prose | pages [10] -->
m

<!-- b004178 | prose | pages [10] -->
m

<!-- b004179 | prose | pages [10] -->
m

<!-- b004180 | prose | pages [10] -->
m

<!-- b004181 | prose | pages [10] -->
m

<!-- b004182 | prose | pages [10] -->
m

<!-- b004183 | prose | pages [10] -->
m

<!-- b004184 | prose | pages [10] -->
m

<!-- b004185 | prose | pages [10] -->
m

<!-- b004186 | prose | pages [10] -->
m

<!-- b004187 | prose | pages [10] -->
m

<!-- b004188 | prose | pages [10] -->
m

<!-- b004189 | prose | pages [10] -->
m

<!-- b004190 | prose | pages [10] -->
m

<!-- b004191 | prose | pages [10] -->
m

<!-- b004192 | prose | pages [10] -->
m

<!-- b004193 | prose | pages [10] -->
m

<!-- b004194 | prose | pages [10] -->
m

<!-- b004195 | prose | pages [10] -->
m

<!-- b004196 | prose | pages [10] -->
m

<!-- b004197 | prose | pages [10] -->
m

<!-- b004198 | prose | pages [10] -->
m

<!-- b004199 | prose | pages [10] -->
m

<!-- b004200 | prose | pages [10] -->
m

<!-- b004201 | prose | pages [10] -->
m

<!-- b004202 | prose | pages [10] -->
m

<!-- b004203 | prose | pages [10] -->
m

<!-- b004204 | prose | pages [10] -->
m

<!-- b004205 | prose | pages [10] -->
m

<!-- b004206 | prose | pages [10] -->
m

<!-- b004207 | prose | pages [10] -->
m

<!-- b004208 | prose | pages [10] -->
m

<!-- b004209 | prose | pages [10] -->
m

<!-- b004210 | prose | pages [10] -->
m

<!-- b004211 | prose | pages [10] -->
m

<!-- b004212 | prose | pages [10] -->
m

<!-- b004213 | prose | pages [10] -->
m

<!-- b004214 | prose | pages [10] -->
m

<!-- b004215 | prose | pages [10] -->
m

<!-- b004216 | prose | pages [10] -->
m

<!-- b004217 | prose | pages [10] -->
m

<!-- b004218 | prose | pages [10] -->
m

<!-- b004219 | prose | pages [10] -->
m

<!-- b004220 | prose | pages [10] -->
m

<!-- b004221 | prose | pages [10] -->
m

<!-- b004222 | prose | pages [10] -->
m

<!-- b004223 | prose | pages [10] -->
m

<!-- b004224 | prose | pages [10] -->
m

<!-- b004225 | prose | pages [10] -->
m

<!-- b004226 | prose | pages [10] -->
m

<!-- b004227 | prose | pages [10] -->
m

<!-- b004228 | prose | pages [10] -->
m

<!-- b004229 | prose | pages [10] -->
m

<!-- b004230 | prose | pages [10] -->
m

<!-- b004231 | prose | pages [10] -->
m

<!-- b004232 | prose | pages [10] -->
m

<!-- b004233 | prose | pages [10] -->
m

<!-- b004234 | prose | pages [10] -->
m

<!-- b004235 | prose | pages [10] -->
m

<!-- b004236 | prose | pages [10] -->
m

<!-- b004237 | prose | pages [10] -->
m

<!-- b004238 | prose | pages [10] -->
m

<!-- b004239 | prose | pages [10] -->
m

<!-- b004240 | prose | pages [10] -->
m

<!-- b004241 | prose | pages [10] -->
m

<!-- b004242 | prose | pages [10] -->
m

<!-- b004243 | prose | pages [10] -->
m

<!-- b004244 | prose | pages [10] -->
m

<!-- b004245 | prose | pages [10] -->
m

<!-- b004246 | prose | pages [10] -->
m

<!-- b004247 | prose | pages [10] -->
m

<!-- b004248 | prose | pages [10] -->
m

<!-- b004249 | prose | pages [10] -->
m

<!-- b004250 | prose | pages [10] -->
m

<!-- b004251 | prose | pages [10] -->
m

<!-- b004252 | prose | pages [10] -->
m

<!-- b004253 | prose | pages [10] -->
m

<!-- b004254 | prose | pages [10] -->
tions, report far fewer cybercrime incidents compared to the United States. This sug-

<!-- b004255 | prose | pages [10] -->
m

<!-- b004256 | prose | pages [10] -->
m

<!-- b004257 | prose | pages [10] -->
m

<!-- b004258 | prose | pages [10] -->
m

<!-- b004259 | prose | pages [10] -->
m

<!-- b004260 | prose | pages [10] -->
m

<!-- b004261 | prose | pages [10] -->
m

<!-- b004262 | prose | pages [10] -->
m

<!-- b004263 | prose | pages [10] -->
m

<!-- b004264 | prose | pages [10] -->
m

<!-- b004265 | prose | pages [10] -->
m

<!-- b004266 | prose | pages [10] -->
m

<!-- b004267 | prose | pages [10] -->
m

<!-- b004268 | prose | pages [10] -->
m

<!-- b004269 | prose | pages [10] -->
m

<!-- b004270 | prose | pages [10] -->
m

<!-- b004271 | prose | pages [10] -->
m

<!-- b004272 | prose | pages [10] -->
m

<!-- b004273 | prose | pages [10] -->
m

<!-- b004274 | prose | pages [10] -->
m

<!-- b004275 | prose | pages [10] -->
m

<!-- b004276 | prose | pages [10] -->
m

<!-- b004277 | prose | pages [10] -->
m

<!-- b004278 | prose | pages [10] -->
m

<!-- b004279 | prose | pages [10] -->
m

<!-- b004280 | prose | pages [10] -->
m

<!-- b004281 | prose | pages [10] -->
m

<!-- b004282 | prose | pages [10] -->
m

<!-- b004283 | prose | pages [10] -->
m

<!-- b004284 | prose | pages [10] -->
m

<!-- b004285 | prose | pages [10] -->
m

<!-- b004286 | prose | pages [10] -->
m

<!-- b004287 | prose | pages [10] -->
m

<!-- b004288 | prose | pages [10] -->
m

<!-- b004289 | prose | pages [10] -->
m

<!-- b004290 | prose | pages [10] -->
m

<!-- b004291 | prose | pages [10] -->
m

<!-- b004292 | prose | pages [10] -->
m

<!-- b004293 | prose | pages [10] -->
m

<!-- b004294 | prose | pages [10] -->
m

<!-- b004295 | prose | pages [10] -->
m

<!-- b004296 | prose | pages [10] -->
m

<!-- b004297 | prose | pages [10] -->
m

<!-- b004298 | prose | pages [10] -->
m

<!-- b004299 | prose | pages [10] -->
m

<!-- b004300 | prose | pages [10] -->
m

<!-- b004301 | prose | pages [10] -->
m

<!-- b004302 | prose | pages [10] -->
m

<!-- b004303 | prose | pages [10] -->
m

<!-- b004304 | prose | pages [10] -->
m

<!-- b004305 | prose | pages [10] -->
m

<!-- b004306 | prose | pages [10] -->
m

<!-- b004307 | prose | pages [10] -->
m

<!-- b004308 | prose | pages [10] -->
m

<!-- b004309 | prose | pages [10] -->
m

<!-- b004310 | prose | pages [10] -->
m

<!-- b004311 | prose | pages [10] -->
m

<!-- b004312 | prose | pages [10] -->
m

<!-- b004313 | prose | pages [10] -->
m

<!-- b004314 | prose | pages [10] -->
m

<!-- b004315 | prose | pages [10] -->
m

<!-- b004316 | prose | pages [10] -->
m

<!-- b004317 | prose | pages [10] -->
m

<!-- b004318 | prose | pages [10] -->
m

<!-- b004319 | prose | pages [10] -->
m

<!-- b004320 | prose | pages [10] -->
m

<!-- b004321 | prose | pages [10] -->
m

<!-- b004322 | prose | pages [10] -->
m

<!-- b004323 | prose | pages [10] -->
m

<!-- b004324 | prose | pages [10] -->
m

<!-- b004325 | prose | pages [10] -->
m

<!-- b004326 | prose | pages [10] -->
m

<!-- b004327 | prose | pages [10] -->
m

<!-- b004328 | prose | pages [10] -->
m

<!-- b004329 | prose | pages [10] -->
m

<!-- b004330 | prose | pages [10] -->
m

<!-- b004331 | prose | pages [10] -->
m

<!-- b004332 | prose | pages [10] -->
m

<!-- b004333 | prose | pages [10] -->
m

<!-- b004334 | prose | pages [10] -->
m

<!-- b004335 | prose | pages [10] -->
m

<!-- b004336 | prose | pages [10] -->
m

<!-- b004337 | prose | pages [10] -->
m

<!-- b004338 | prose | pages [10] -->
m

<!-- b004339 | prose | pages [10] -->
m

<!-- b004340 | prose | pages [10] -->
m

<!-- b004341 | prose | pages [10] -->
m

<!-- b004342 | prose | pages [10] -->
m

<!-- b004343 | prose | pages [10] -->
m

<!-- b004344 | prose | pages [10] -->
m

<!-- b004345 | prose | pages [10] -->
m

<!-- b004346 | prose | pages [10] -->
m

<!-- b004347 | prose | pages [10] -->
m

<!-- b004348 | prose | pages [10] -->
m

<!-- b004349 | prose | pages [10] -->
m

<!-- b004350 | prose | pages [10] -->
m

<!-- b004351 | prose | pages [10] -->
m

<!-- b004352 | prose | pages [10] -->
m

<!-- b004353 | prose | pages [10] -->
m

<!-- b004354 | prose | pages [10] -->
m

<!-- b004355 | prose | pages [10] -->
m

<!-- b004356 | prose | pages [10] -->
m

<!-- b004357 | prose | pages [10] -->
m

<!-- b004358 | prose | pages [10] -->
m

<!-- b004359 | prose | pages [10] -->
m

<!-- b004360 | prose | pages [10] -->
m

<!-- b004361 | prose | pages [10] -->
m

<!-- b004362 | prose | pages [10] -->
m

<!-- b004363 | prose | pages [10] -->
m

<!-- b004364 | prose | pages [10] -->
m

<!-- b004365 | prose | pages [10] -->
m

<!-- b004366 | prose | pages [10] -->
m

<!-- b004367 | prose | pages [10] -->
m

<!-- b004368 | prose | pages [10] -->
m

<!-- b004369 | prose | pages [10] -->
m

<!-- b004370 | prose | pages [10] -->
m

<!-- b004371 | prose | pages [10] -->
m

<!-- b004372 | prose | pages [10] -->
m

<!-- b004373 | prose | pages [10] -->
m

<!-- b004374 | prose | pages [10] -->
m

<!-- b004375 | prose | pages [10] -->
m

<!-- b004376 | prose | pages [10] -->
gests that the distribution of cybercrime is more closely tied to economic development and digitalization levels rather than sheer population size.

<!-- b004377 | prose | pages [10] -->
Overall, the data reveals a pronounced unevenness in the global distribution of cybercrime incidents. Cybercrime is more concentrated in economically developed re- gions with advanced internet infrastructures. However, this distribution pattern is not solely determined by factors such as national development level or internet penetra- tion rate. Demographic factors, including GDP, internet usage rates, and education levels, likely play a critical role in shaping the distribution of cybercrime.

<!-- b004378 | prose | pages [10] -->
National Security Policies and Global Cybercrime Dis- 5 tribution

<!-- b004379 | prose | pages [10] -->
5.1 Preliminary Analysis

<!-- b004380 | prose | pages [10] -->
5.1.1 Data Visualization

<!-- b004381 | caption | pages [10] -->
Figure 8: Comparison of Target Count Before and After Policy implementation

<!-- b004382 | prose | pages [10] -->
This bar chart, using a logarithmic scale, illustrates the changes in the target count of different countries before and after policy implementation, represented by blue and orange bars, respectively. The use of a logarithmic scale effectively reduces data dis- parities, making the changes across countries more intuitive.

<!-- b004383 | prose | pages [10] -->
From the chart, it is evident that the United States has a signiﬁcantly higher target count compared to other countries. The target count decreased from 706 before the policy implementation to 543 afterward. Although it remains at a high level, a down- ward trend is observed. Similarly, Canada experienced a notable reduction in target

<!-- b004384 | prose | pages [10] -->
关注数学模型

<!-- b004385 | prose | pages [10] -->
count, from 33 to 16, indicating that the policy may have contributed to the decrease

<!-- b004386 | furniture | pages [10] -->
2

<!-- b004387 | furniture | pages [10] -->
MATHmodels

<!-- b004388 | furniture | pages [10] -->
获取更多资讯

<!-- b004389 | furniture | pages [11] -->
Team # 2521039

<!-- b004390 | furniture | pages [11] -->
Page 11 of 25

<!-- b004391 | prose | pages [11] -->
in targets. Australia and China also showed declines in target counts after policy im- plementation, with Australia’s count dropping from 6 to 1 and China’s from 6 to 3, demonstrating a substantial reduction.

<!-- b004392 | prose | pages [11] -->
In contrast, France and Korea displayed different trends. France’s target count in-

<!-- b004393 | prose | pages [11] -->
微信公众号：数学模型

<!-- b004394 | prose | pages [11] -->
creased from 2 before the policy implementation to 7 afterward, suggesting a rise in targets post-policy. Koreas target count similarly grew, from 1 to 4, reﬂecting a com- parable upward trend. These anomalies may be associated with the speciﬁc context of policy implementation or other external factors.

<!-- b004395 | prose | pages [11] -->
Overall, this chart clearly presents the changes in target counts across countries before and after policy implementation, highlighting the varied effects of the policy among different nations. It provides valuable data support for further analysis of the impact and underlying mechanisms of policy implementation.

<!-- b004396 | prose | pages [11] -->
5.1.2 Inﬂuencing Factors Analysis

<!-- b004397 | prose | pages [11] -->
微信号：MATHmodels

<!-- b004398 | caption | pages [11] -->
Figure 9: Incident Count Over Time Map

<!-- b004399 | prose | pages [11] -->
This line chart illustrates the temporal trends in target counts across different coun- tries (CA, AU, FR, JP, CN, KR) from 2014 to 2024. Signiﬁcant variations and ﬂuctuations in target counts are observed among the countries over time.

<!-- b004400 | prose | pages [11] -->
Canada (CA) exhibited the most dramatic changes, peaking in 2016 with a target count exceeding 60, followed by a rapid decline until 2020, after which it stabilized. This pattern may reﬂect the impact of signiﬁcant cybersecurity incidents or policy in- terventions during speciﬁc years. Australia (AU) showed a slow upward trend be- tween 2015 and 2017, followed by a slight decline. However, its overall ﬂuctuations remained relatively small and stable. In contrast, France (FR), Japan (JP), China (CN), and Korea (KR) maintained consistently lower target counts throughout the period, with minimal ﬂuctuations, reﬂecting a relatively steady trend.

<!-- b004401 | prose | pages [11] -->
From a temporal perspective, between 2014 and 2016, target counts in Canada and Australia increased, with Canada’s sharp rise being particularly notable during this period. Between 2017 and 2020, Canada’s target count experienced a steep decline, while the target counts in other countries remained relatively stable. Post-2020, target counts across all countries generally stabilized, with no signiﬁcant peaks or ﬂuctua- tions observed.

<!-- b004402 | prose | pages [11] -->
These trends suggest that changes in target counts across countries may be inﬂu- enced by the implementation of speciﬁc policies. To explore the impact of national cy- bersecurity policies and their timing on the distribution of cybercrime targets, a multi- level linear regression model was implemented using MATLAB. The study’s dataset

<!-- b004403 | furniture | pages [12] -->
Team # 2521039

<!-- b004404 | furniture | pages [12] -->
Page 12 of 25

<!-- b004405 | prose | pages [12] -->
covers multiple countries and includes key variables such as policy implementation status (Policy_i), whether the country was in the post-implementation phase (Post_t), and the interaction term (Policy_i × Post_t).

<!-- b004406 | prose | pages [12] -->
First, datasets for different countries were constructed and cleaned, then gradually merged into a complete analytical sample. In the regression analysis, the model treated countries as a random effect to control for potential heterogeneity across countries. At the same time, the main effects of policy and time, along with their interaction term, were included as ﬁxed effects to quantify the combined impact of these factors on the target count of cybercrime. By ﬁtting a multi-level linear model the coefﬁcients (Coef.), signiﬁcance levels (p-value), and standard errors (SE) were obtained.

<!-- b004407 | prose | pages [12] -->
Yij = β0 + β1Policyi + β2Postt + β3(Policyi × Postt) + uj + ϵij

<!-- b004408 | prose | pages [12] -->
The study revealed the independent effects of policy implementation and time phases on the target count, as well as the reinforcing effects of their interaction. The model results provide data-driven evidence for evaluating policy effectiveness while ensuring robustness by controlling for cross-country differences.

<!-- b004409 | caption | pages [12] -->
Table 3: Regression Results

<!-- b004410 | prose | pages [12] -->
Variable Coef.

<!-- b004411 | prose | pages [12] -->
5.225 Policy_i -3.4 Post_t 4.375 Policy_i × Post_t

<!-- b004412 | prose | pages [12] -->
The results indicate the following:

<!-- b004413 | prose | pages [12] -->
SE pValue

<!-- b004414 | prose | pages [12] -->
0.5 0.036 0.866 0.038 1 0.04

<!-- b004415 | prose | pages [12] -->
• The main effect coefﬁcient for the policy variable (Policy_i) is 5.225, with a stan- dard error of 0.5 and a p-value of 0.036, which is less than the signiﬁcance level of 0.05. This demonstrates that the independent effect of the policy is statisti- cally signiﬁcant. This means that, without considering the time factor, countries that implemented the policy had an average of 5.225 more targets compared to countries that did not implement the policy. Additionally, the low standard error indicates that the model’s estimate of the policy’s main effect is robust.

<!-- b004416 | prose | pages [12] -->
• The main effect coefﬁcient for the time variable (Post_t) is 3.4, with a standard error of 0.866 and a p-value of 0.038, which is also less than the signiﬁcance level of 0.05. This suggests that the independent effect of time is statistically signiﬁcant as well. It indicates that during the post-policy implementation phase, the aver- age target count was 3.4 units lower than during the pre-policy phase. Although the standard error is slightly higher than that of the policy variable, the overall estimate of the time’s main effect remains relatively robust.

<!-- b004417 | prose | pages [12] -->
• The interaction effect (Policy_i × Post_t) coefﬁcient is 4.375, with a standard er- ror of 1.0 and a p-value of 0.02, which is below the 0.05 signiﬁcance level. This indicates that the interaction effect between policy and time is signiﬁcant. The positive coefﬁcient for the interaction effect implies that in countries with policy implementation during the post-policy phase, the average target count increased by 4.375 units. However, the relatively high standard error for the interaction term suggests some uncertainty in its estimate, which may be due to a small sample size or data characteristics.

<!-- b004418 | prose | pages [12] -->
关注数学模型

<!-- b004419 | furniture | pages [12] -->
2

<!-- b004420 | furniture | pages [12] -->
MATHmodels

<!-- b004421 | furniture | pages [12] -->
获取更多资讯

<!-- b004422 | furniture | pages [13] -->
Team # 2521039

<!-- b004423 | furniture | pages [13] -->
Page 13 of 25

<!-- b004424 | prose | pages [13] -->
In summary, the model shows that both the independent effects of policy and time have a signiﬁcant impact on the target count, while the interaction effect between pol- icy and time further ampliﬁes this impact. Particularly during the post-policy phase,

<!-- b004425 | prose | pages [13] -->
微信公众号：数学模型

<!-- b004426 | prose | pages [13] -->
the changes in target counts are more pronounced. The p-values for all variables are below 0.05, indicating that the model’s ﬁt is statistically signiﬁcant, and the relatively low standard errors reﬂect good robustness of the estimates.

<!-- b004427 | prose | pages [13] -->
5.2

<!-- b004428 | heading | pages [13] -->
Model1: Hierarchical Interaction Scoring Regression Model(HISR)

<!-- b004429 | prose | pages [13] -->
5.2.1 Identifying Experimental and Control Group

<!-- b004430 | prose | pages [13] -->
This study employed the difference-in-differences (DID) model to evaluate the effectiveness of cybersecurity policy implementation, quantifying changes in target count, success rate, thwart rate, reporting rate, and prosecution rate over time relative

<!-- b004431 | prose | pages [13] -->
微信号：MATHmodels

<!-- b004432 | heading | pages [13] -->
to policy implementation. The model divided the study subjects into an experiment

<!-- b004433 | prose | pages [13] -->
group and a control group for comparative analysis. The experiment group reﬂects the effects of policy implementation, while the control group provides a baseline for comparison, supporting the assessment of net effects.

<!-- b004434 | prose | pages [13] -->
The experiment group includes countries that have implemented cybersecurity policies, such as:

<!-- b004435 | prose | pages [13] -->
• United States: Known for its long-standing policies with signiﬁcant impacts on target count and success rate. • China: Recently enhanced legal frameworks and technical cooperation. • Korea: Renowned for its rapid response capabilities and robust technical de- fenses.

<!-- b004436 | prose | pages [13] -->
The control group includes countries that have not implemented relevant policies, such as:

<!-- b004437 | prose | pages [13] -->
• New Zealand: Policies focused on traditional security areas. • Ireland: Fragmented measures with no cohesive framework. • Germany: No formal cybersecurity policies introduced.

<!-- b004438 | prose | pages [13] -->
To ensure comparability between the groups, key indicators such as economic level, internet penetration rate, and education level were considered. By comparing metrics like GDP, GDP per capita, and internet access rate, the study balanced the experiment group and control group, reducing the inﬂuence of confounding factors.

<!-- b004439 | prose | pages [13] -->
5.2.2

<!-- b004440 | heading | pages [13] -->
Verifying the Parallel Trend Assumption

<!-- b004441 | heading | pages [13] -->
In the difference-in-differences (DID) model, the parallel trend assumption is a

<!-- b004442 | prose | pages [13] -->
critical prerequisite. This assumption requires that, prior to policy implementation, the trends in the indicators for the experiment group and the control group remain consistent. If the parallel trend assumption holds, it can be inferred that the differences between the experiment group and the control group before policy implementation are primarily due to time trends or other common factors, rather than the policy itself.

<!-- b004443 | prose | pages [13] -->
We ﬁrst extracted the target count, success rate, thwart rate, reporting rate, and prosecution rate for the experiment group and the control group from the data, en- suring consistency in the time range and statistical standards between the two groups. Then, we plotted line charts showing the temporal trends of these indicators for both groups to examine the changes prior to policy implementation.

<!-- b004444 | prose | pages [13] -->
By plotting the temporal changes in cybercrime target counts for the experiment

<!-- b004445 | furniture | pages [14] -->
Team # 2521039

<!-- b004446 | furniture | pages [14] -->
Page 14 of 25

<!-- b004447 | prose | pages [14] -->
group and the control group, the results showed the following:

<!-- b004448 | caption | pages [14] -->
Figure 10: Parallel Trend Veriﬁcation

<!-- b004449 | prose | pages [14] -->
Before policy implementation, the trends in target counts for the experiment group and the control group were largely consistent. For instance, during 2017-2018, the year-over-year decline in target counts for the experiment group was similar in magni- tude to that of the control group, indicating consistent trends between the two groups prior to policy implementation.

<!-- b004450 | prose | pages [14] -->
Therefore, the parallel trend assumption for the experiment group and the control group is satisﬁed, allowing the DID model to be applied to analyze the net effect of the policy.

<!-- b004451 | prose | pages [14] -->
5.2.3

<!-- b004452 | heading | pages [14] -->
Model Process

<!-- b004453 | prose | pages [14] -->
During the data analysis process, it is essential to ensure that the input data in- cludes all necessary dependent variables (e.g., target count, success rate, thwart rate, reporting rate, and prosecution rate) as well as independent variables (Policy_i, Post_t, Policy_i × Post_t). For each indicator (such as target count and success rate), separate

<!-- b004454 | prose | pages [14] -->
m

<!-- b004455 | prose | pages [14] -->
m

<!-- b004456 | prose | pages [14] -->
m

<!-- b004457 | prose | pages [14] -->
m

<!-- b004458 | prose | pages [14] -->
m

<!-- b004459 | prose | pages [14] -->
m

<!-- b004460 | prose | pages [14] -->
m

<!-- b004461 | prose | pages [14] -->
m

<!-- b004462 | prose | pages [14] -->
m

<!-- b004463 | prose | pages [14] -->
m

<!-- b004464 | prose | pages [14] -->
m

<!-- b004465 | prose | pages [14] -->
m

<!-- b004466 | prose | pages [14] -->
m

<!-- b004467 | prose | pages [14] -->
m

<!-- b004468 | prose | pages [14] -->
m

<!-- b004469 | prose | pages [14] -->
m

<!-- b004470 | prose | pages [14] -->
m

<!-- b004471 | prose | pages [14] -->
m

<!-- b004472 | prose | pages [14] -->
m

<!-- b004473 | prose | pages [14] -->
m

<!-- b004474 | prose | pages [14] -->
m

<!-- b004475 | prose | pages [14] -->
m

<!-- b004476 | heading | pages [14] -->
regression models are established:

<!-- b004477 | prose | pages [14] -->
m

<!-- b004478 | prose | pages [14] -->
m

<!-- b004479 | prose | pages [14] -->
m

<!-- b004480 | prose | pages [14] -->
m

<!-- b004481 | prose | pages [14] -->
m

<!-- b004482 | prose | pages [14] -->
m

<!-- b004483 | prose | pages [14] -->
m

<!-- b004484 | prose | pages [14] -->
m

<!-- b004485 | prose | pages [14] -->
m

<!-- b004486 | prose | pages [14] -->
m

<!-- b004487 | prose | pages [14] -->
m

<!-- b004488 | prose | pages [14] -->
m

<!-- b004489 | prose | pages [14] -->
m

<!-- b004490 | prose | pages [14] -->
m

<!-- b004491 | prose | pages [14] -->
m

<!-- b004492 | prose | pages [14] -->
m

<!-- b004493 | prose | pages [14] -->
m

<!-- b004494 | prose | pages [14] -->
m

<!-- b004495 | prose | pages [14] -->
m

<!-- b004496 | prose | pages [14] -->
m

<!-- b004497 | prose | pages [14] -->
m

<!-- b004498 | prose | pages [14] -->
m

<!-- b004499 | prose | pages [14] -->
m

<!-- b004500 | prose | pages [14] -->
m

<!-- b004501 | prose | pages [14] -->
m

<!-- b004502 | prose | pages [14] -->
m

<!-- b004503 | prose | pages [14] -->
m

<!-- b004504 | prose | pages [14] -->
m

<!-- b004505 | prose | pages [14] -->
m

<!-- b004506 | prose | pages [14] -->
m

<!-- b004507 | prose | pages [14] -->
m

<!-- b004508 | prose | pages [14] -->
m

<!-- b004509 | prose | pages [14] -->
m

<!-- b004510 | prose | pages [14] -->
m

<!-- b004511 | prose | pages [14] -->
m

<!-- b004512 | prose | pages [14] -->
m

<!-- b004513 | prose | pages [14] -->
m

<!-- b004514 | prose | pages [14] -->
m

<!-- b004515 | prose | pages [14] -->
m

<!-- b004516 | prose | pages [14] -->
m

<!-- b004517 | prose | pages [14] -->
m

<!-- b004518 | prose | pages [14] -->
m

<!-- b004519 | prose | pages [14] -->
m

<!-- b004520 | prose | pages [14] -->
m

<!-- b004521 | prose | pages [14] -->
m

<!-- b004522 | prose | pages [14] -->
m

<!-- b004523 | prose | pages [14] -->
m

<!-- b004524 | prose | pages [14] -->
m

<!-- b004525 | prose | pages [14] -->
m

<!-- b004526 | prose | pages [14] -->
m

<!-- b004527 | prose | pages [14] -->
m

<!-- b004528 | prose | pages [14] -->
m

<!-- b004529 | prose | pages [14] -->
m

<!-- b004530 | prose | pages [14] -->
m

<!-- b004531 | prose | pages [14] -->
m

<!-- b004532 | prose | pages [14] -->
m

<!-- b004533 | prose | pages [14] -->
m

<!-- b004534 | prose | pages [14] -->
m

<!-- b004535 | prose | pages [14] -->
m

<!-- b004536 | prose | pages [14] -->
m

<!-- b004537 | prose | pages [14] -->
m

<!-- b004538 | prose | pages [14] -->
m

<!-- b004539 | prose | pages [14] -->
m

<!-- b004540 | prose | pages [14] -->
m

<!-- b004541 | prose | pages [14] -->
m

<!-- b004542 | prose | pages [14] -->
m

<!-- b004543 | prose | pages [14] -->
m

<!-- b004544 | prose | pages [14] -->
m

<!-- b004545 | prose | pages [14] -->
m

<!-- b004546 | prose | pages [14] -->
m

<!-- b004547 | prose | pages [14] -->
m

<!-- b004548 | prose | pages [14] -->
m

<!-- b004549 | prose | pages [14] -->
m

<!-- b004550 | prose | pages [14] -->
m

<!-- b004551 | prose | pages [14] -->
m

<!-- b004552 | prose | pages [14] -->
m

<!-- b004553 | prose | pages [14] -->
m

<!-- b004554 | prose | pages [14] -->
m

<!-- b004555 | prose | pages [14] -->
m

<!-- b004556 | prose | pages [14] -->
m

<!-- b004557 | prose | pages [14] -->
m

<!-- b004558 | prose | pages [14] -->
m

<!-- b004559 | prose | pages [14] -->
m

<!-- b004560 | prose | pages [14] -->
m

<!-- b004561 | prose | pages [14] -->
m

<!-- b004562 | prose | pages [14] -->
m

<!-- b004563 | prose | pages [14] -->
m

<!-- b004564 | prose | pages [14] -->
m

<!-- b004565 | prose | pages [14] -->
m

<!-- b004566 | prose | pages [14] -->
m

<!-- b004567 | prose | pages [14] -->
m

<!-- b004568 | prose | pages [14] -->
m

<!-- b004569 | prose | pages [14] -->
m

<!-- b004570 | prose | pages [14] -->
m

<!-- b004571 | prose | pages [14] -->
m

<!-- b004572 | prose | pages [14] -->
m

<!-- b004573 | prose | pages [14] -->
m

<!-- b004574 | prose | pages [14] -->
m

<!-- b004575 | prose | pages [14] -->
m

<!-- b004576 | prose | pages [14] -->
m

<!-- b004577 | prose | pages [14] -->
m

<!-- b004578 | prose | pages [14] -->
m

<!-- b004579 | prose | pages [14] -->
m

<!-- b004580 | prose | pages [14] -->
m

<!-- b004581 | prose | pages [14] -->
m

<!-- b004582 | prose | pages [14] -->
m

<!-- b004583 | prose | pages [14] -->
m

<!-- b004584 | prose | pages [14] -->
m

<!-- b004585 | prose | pages [14] -->
m

<!-- b004586 | prose | pages [14] -->
m

<!-- b004587 | prose | pages [14] -->
m

<!-- b004588 | prose | pages [14] -->
m

<!-- b004589 | prose | pages [14] -->
m

<!-- b004590 | prose | pages [14] -->
m

<!-- b004591 | prose | pages [14] -->
m

<!-- b004592 | prose | pages [14] -->
m

<!-- b004593 | prose | pages [14] -->
m

<!-- b004594 | prose | pages [14] -->
m

<!-- b004595 | prose | pages [14] -->
m

<!-- b004596 | prose | pages [14] -->
m

<!-- b004597 | prose | pages [14] -->
m

<!-- b004598 | prose | pages [14] -->
m

<!-- b004599 | prose | pages [14] -->
m

<!-- b004600 | prose | pages [14] -->
m

<!-- b004601 | prose | pages [14] -->
m

<!-- b004602 | prose | pages [14] -->
m

<!-- b004603 | prose | pages [14] -->
m

<!-- b004604 | prose | pages [14] -->
m

<!-- b004605 | prose | pages [14] -->
m

<!-- b004606 | prose | pages [14] -->
m

<!-- b004607 | prose | pages [14] -->
m

<!-- b004608 | prose | pages [14] -->
m

<!-- b004609 | prose | pages [14] -->
m

<!-- b004610 | prose | pages [14] -->
m

<!-- b004611 | prose | pages [14] -->
m

<!-- b004612 | prose | pages [14] -->
m

<!-- b004613 | prose | pages [14] -->
m

<!-- b004614 | prose | pages [14] -->
m

<!-- b004615 | prose | pages [14] -->
m

<!-- b004616 | prose | pages [14] -->
m

<!-- b004617 | prose | pages [14] -->
m

<!-- b004618 | prose | pages [14] -->
m

<!-- b004619 | prose | pages [14] -->
m

<!-- b004620 | prose | pages [14] -->
m

<!-- b004621 | prose | pages [14] -->
m

<!-- b004622 | prose | pages [14] -->
m

<!-- b004623 | prose | pages [14] -->
m

<!-- b004624 | prose | pages [14] -->
m

<!-- b004625 | prose | pages [14] -->
m

<!-- b004626 | prose | pages [14] -->
m

<!-- b004627 | prose | pages [14] -->
m

<!-- b004628 | prose | pages [14] -->
m

<!-- b004629 | prose | pages [14] -->
m

<!-- b004630 | prose | pages [14] -->
m

<!-- b004631 | prose | pages [14] -->
m

<!-- b004632 | prose | pages [14] -->
m

<!-- b004633 | prose | pages [14] -->
m

<!-- b004634 | prose | pages [14] -->
m

<!-- b004635 | prose | pages [14] -->
m

<!-- b004636 | prose | pages [14] -->
m

<!-- b004637 | prose | pages [14] -->
m

<!-- b004638 | prose | pages [14] -->
m

<!-- b004639 | prose | pages [14] -->
m

<!-- b004640 | prose | pages [14] -->
m

<!-- b004641 | prose | pages [14] -->
m

<!-- b004642 | prose | pages [14] -->
m

<!-- b004643 | prose | pages [14] -->
m

<!-- b004644 | prose | pages [14] -->
m

<!-- b004645 | prose | pages [14] -->
m

<!-- b004646 | prose | pages [14] -->
m

<!-- b004647 | prose | pages [14] -->
m

<!-- b004648 | prose | pages [14] -->
m

<!-- b004649 | prose | pages [14] -->
m

<!-- b004650 | prose | pages [14] -->
m

<!-- b004651 | prose | pages [14] -->
m

<!-- b004652 | prose | pages [14] -->
m

<!-- b004653 | prose | pages [14] -->
m

<!-- b004654 | prose | pages [14] -->
m

<!-- b004655 | prose | pages [14] -->
m

<!-- b004656 | prose | pages [14] -->
m

<!-- b004657 | prose | pages [14] -->
m

<!-- b004658 | prose | pages [14] -->
m

<!-- b004659 | prose | pages [14] -->
m

<!-- b004660 | prose | pages [14] -->
m

<!-- b004661 | prose | pages [14] -->
m

<!-- b004662 | prose | pages [14] -->
m

<!-- b004663 | prose | pages [14] -->
m

<!-- b004664 | prose | pages [14] -->
m

<!-- b004665 | prose | pages [14] -->
m

<!-- b004666 | prose | pages [14] -->
m

<!-- b004667 | prose | pages [14] -->
m

<!-- b004668 | prose | pages [14] -->
m

<!-- b004669 | prose | pages [14] -->
m

<!-- b004670 | prose | pages [14] -->
m

<!-- b004671 | prose | pages [14] -->
m

<!-- b004672 | prose | pages [14] -->
m

<!-- b004673 | prose | pages [14] -->
m

<!-- b004674 | prose | pages [14] -->
m

<!-- b004675 | prose | pages [14] -->
m

<!-- b004676 | prose | pages [14] -->
m

<!-- b004677 | prose | pages [14] -->
m

<!-- b004678 | prose | pages [14] -->
m

<!-- b004679 | prose | pages [14] -->
m

<!-- b004680 | prose | pages [14] -->
m

<!-- b004681 | prose | pages [14] -->
m

<!-- b004682 | prose | pages [14] -->
m

<!-- b004683 | prose | pages [14] -->
m

<!-- b004684 | prose | pages [14] -->
m

<!-- b004685 | prose | pages [14] -->
m

<!-- b004686 | prose | pages [14] -->
m

<!-- b004687 | prose | pages [14] -->
m

<!-- b004688 | prose | pages [14] -->
m

<!-- b004689 | prose | pages [14] -->
m

<!-- b004690 | prose | pages [14] -->
m

<!-- b004691 | prose | pages [14] -->
m

<!-- b004692 | prose | pages [14] -->
m

<!-- b004693 | prose | pages [14] -->
m

<!-- b004694 | prose | pages [14] -->
m

<!-- b004695 | prose | pages [14] -->
m

<!-- b004696 | prose | pages [14] -->
m

<!-- b004697 | prose | pages [14] -->
m

<!-- b004698 | prose | pages [14] -->
m

<!-- b004699 | prose | pages [14] -->
m

<!-- b004700 | prose | pages [14] -->
m

<!-- b004701 | prose | pages [14] -->
m

<!-- b004702 | prose | pages [14] -->
m

<!-- b004703 | prose | pages [14] -->
m

<!-- b004704 | prose | pages [14] -->
m

<!-- b004705 | prose | pages [14] -->
m

<!-- b004706 | prose | pages [14] -->
m

<!-- b004707 | prose | pages [14] -->
m

<!-- b004708 | prose | pages [14] -->
m

<!-- b004709 | prose | pages [14] -->
m

<!-- b004710 | prose | pages [14] -->
m

<!-- b004711 | prose | pages [14] -->
m

<!-- b004712 | prose | pages [14] -->
m

<!-- b004713 | prose | pages [14] -->
m

<!-- b004714 | prose | pages [14] -->
m

<!-- b004715 | prose | pages [14] -->
m

<!-- b004716 | prose | pages [14] -->
m

<!-- b004717 | prose | pages [14] -->
m

<!-- b004718 | prose | pages [14] -->
m

<!-- b004719 | prose | pages [14] -->
m

<!-- b004720 | prose | pages [14] -->
m

<!-- b004721 | prose | pages [14] -->
m

<!-- b004722 | prose | pages [14] -->
m

<!-- b004723 | prose | pages [14] -->
m

<!-- b004724 | prose | pages [14] -->
m

<!-- b004725 | prose | pages [14] -->
m

<!-- b004726 | prose | pages [14] -->
m

<!-- b004727 | prose | pages [14] -->
m

<!-- b004728 | prose | pages [14] -->
m

<!-- b004729 | prose | pages [14] -->
m

<!-- b004730 | prose | pages [14] -->
m

<!-- b004731 | prose | pages [14] -->
m

<!-- b004732 | prose | pages [14] -->
m

<!-- b004733 | prose | pages [14] -->
m

<!-- b004734 | prose | pages [14] -->
m

<!-- b004735 | prose | pages [14] -->
m

<!-- b004736 | prose | pages [14] -->
m

<!-- b004737 | prose | pages [14] -->
m

<!-- b004738 | prose | pages [14] -->
m

<!-- b004739 | prose | pages [14] -->
Yit = β0 + β1Policyi + β2Postt + β3(Policyi × Postt) + ϵit

<!-- b004740 | prose | pages [14] -->
m

<!-- b004741 | prose | pages [14] -->
m

<!-- b004742 | prose | pages [14] -->
m

<!-- b004743 | prose | pages [14] -->
m

<!-- b004744 | prose | pages [14] -->
m

<!-- b004745 | prose | pages [14] -->
m

<!-- b004746 | prose | pages [14] -->
m

<!-- b004747 | prose | pages [14] -->
m

<!-- b004748 | prose | pages [14] -->
m

<!-- b004749 | prose | pages [14] -->
m

<!-- b004750 | prose | pages [14] -->
m

<!-- b004751 | prose | pages [14] -->
m

<!-- b004752 | prose | pages [14] -->
m

<!-- b004753 | prose | pages [14] -->
m

<!-- b004754 | prose | pages [14] -->
m

<!-- b004755 | prose | pages [14] -->
m

<!-- b004756 | prose | pages [14] -->
m

<!-- b004757 | prose | pages [14] -->
m

<!-- b004758 | prose | pages [14] -->
m

<!-- b004759 | prose | pages [14] -->
m

<!-- b004760 | prose | pages [14] -->
m

<!-- b004761 | prose | pages [14] -->
m

<!-- b004762 | prose | pages [14] -->
m

<!-- b004763 | prose | pages [14] -->
m

<!-- b004764 | prose | pages [14] -->
m

<!-- b004765 | prose | pages [14] -->
m

<!-- b004766 | prose | pages [14] -->
m

<!-- b004767 | prose | pages [14] -->
m

<!-- b004768 | prose | pages [14] -->
m

<!-- b004769 | prose | pages [14] -->
m

<!-- b004770 | prose | pages [14] -->
m

<!-- b004771 | prose | pages [14] -->
m

<!-- b004772 | prose | pages [14] -->
m

<!-- b004773 | prose | pages [14] -->
m

<!-- b004774 | prose | pages [14] -->
m

<!-- b004775 | prose | pages [14] -->
m

<!-- b004776 | prose | pages [14] -->
m

<!-- b004777 | prose | pages [14] -->
m

<!-- b004778 | prose | pages [14] -->
m

<!-- b004779 | prose | pages [14] -->
m

<!-- b004780 | prose | pages [14] -->
m

<!-- b004781 | prose | pages [14] -->
m

<!-- b004782 | prose | pages [14] -->
m

<!-- b004783 | prose | pages [14] -->
m

<!-- b004784 | prose | pages [14] -->
m

<!-- b004785 | prose | pages [14] -->
m

<!-- b004786 | prose | pages [14] -->
m

<!-- b004787 | prose | pages [14] -->
m

<!-- b004788 | prose | pages [14] -->
m

<!-- b004789 | prose | pages [14] -->
m

<!-- b004790 | prose | pages [14] -->
m

<!-- b004791 | prose | pages [14] -->
m

<!-- b004792 | prose | pages [14] -->
m

<!-- b004793 | prose | pages [14] -->
m

<!-- b004794 | prose | pages [14] -->
m

<!-- b004795 | prose | pages [14] -->
m

<!-- b004796 | prose | pages [14] -->
m

<!-- b004797 | prose | pages [14] -->
m

<!-- b004798 | prose | pages [14] -->
m

<!-- b004799 | prose | pages [14] -->
m

<!-- b004800 | prose | pages [14] -->
m

<!-- b004801 | prose | pages [14] -->
m

<!-- b004802 | prose | pages [14] -->
m

<!-- b004803 | prose | pages [14] -->
m

<!-- b004804 | prose | pages [14] -->
m

<!-- b004805 | prose | pages [14] -->
m

<!-- b004806 | prose | pages [14] -->
m

<!-- b004807 | prose | pages [14] -->
m

<!-- b004808 | prose | pages [14] -->
m

<!-- b004809 | prose | pages [14] -->
m

<!-- b004810 | prose | pages [14] -->
m

<!-- b004811 | prose | pages [14] -->
m

<!-- b004812 | prose | pages [14] -->
m

<!-- b004813 | prose | pages [14] -->
m

<!-- b004814 | prose | pages [14] -->
m

<!-- b004815 | prose | pages [14] -->
m

<!-- b004816 | prose | pages [14] -->
m

<!-- b004817 | prose | pages [14] -->
m

<!-- b004818 | prose | pages [14] -->
m

<!-- b004819 | prose | pages [14] -->
m

<!-- b004820 | prose | pages [14] -->
m

<!-- b004821 | prose | pages [14] -->
m

<!-- b004822 | prose | pages [14] -->
m

<!-- b004823 | prose | pages [14] -->
m

<!-- b004824 | prose | pages [14] -->
m

<!-- b004825 | prose | pages [14] -->
m

<!-- b004826 | prose | pages [14] -->
m

<!-- b004827 | prose | pages [14] -->
m

<!-- b004828 | prose | pages [14] -->
m

<!-- b004829 | prose | pages [14] -->
m

<!-- b004830 | prose | pages [14] -->
m

<!-- b004831 | prose | pages [14] -->
m

<!-- b004832 | prose | pages [14] -->
m

<!-- b004833 | prose | pages [14] -->
m

<!-- b004834 | prose | pages [14] -->
m

<!-- b004835 | prose | pages [14] -->
m

<!-- b004836 | prose | pages [14] -->
m

<!-- b004837 | prose | pages [14] -->
m

<!-- b004838 | prose | pages [14] -->
m

<!-- b004839 | prose | pages [14] -->
m

<!-- b004840 | prose | pages [14] -->
m

<!-- b004841 | prose | pages [14] -->
m

<!-- b004842 | prose | pages [14] -->
m

<!-- b004843 | prose | pages [14] -->
m

<!-- b004844 | prose | pages [14] -->
m

<!-- b004845 | prose | pages [14] -->
m

<!-- b004846 | prose | pages [14] -->
m

<!-- b004847 | prose | pages [14] -->
m

<!-- b004848 | prose | pages [14] -->
m

<!-- b004849 | prose | pages [14] -->
m

<!-- b004850 | prose | pages [14] -->
m

<!-- b004851 | prose | pages [14] -->
m

<!-- b004852 | prose | pages [14] -->
m

<!-- b004853 | prose | pages [14] -->
m

<!-- b004854 | prose | pages [14] -->
m

<!-- b004855 | prose | pages [14] -->
m

<!-- b004856 | prose | pages [14] -->
m

<!-- b004857 | prose | pages [14] -->
m

<!-- b004858 | prose | pages [14] -->
m

<!-- b004859 | prose | pages [14] -->
m

<!-- b004860 | prose | pages [14] -->
m

<!-- b004861 | prose | pages [14] -->
m

<!-- b004862 | prose | pages [14] -->
m

<!-- b004863 | prose | pages [14] -->
m

<!-- b004864 | prose | pages [14] -->
m

<!-- b004865 | prose | pages [14] -->
m

<!-- b004866 | prose | pages [14] -->
m

<!-- b004867 | prose | pages [14] -->
m

<!-- b004868 | prose | pages [14] -->
m

<!-- b004869 | prose | pages [14] -->
m

<!-- b004870 | prose | pages [14] -->
m

<!-- b004871 | prose | pages [14] -->
m

<!-- b004872 | prose | pages [14] -->
m

<!-- b004873 | prose | pages [14] -->
m

<!-- b004874 | prose | pages [14] -->
m

<!-- b004875 | prose | pages [14] -->
m

<!-- b004876 | prose | pages [14] -->
m

<!-- b004877 | prose | pages [14] -->
m

<!-- b004878 | prose | pages [14] -->
m

<!-- b004879 | prose | pages [14] -->
m

<!-- b004880 | prose | pages [14] -->
m

<!-- b004881 | prose | pages [14] -->
m

<!-- b004882 | prose | pages [14] -->
m

<!-- b004883 | prose | pages [14] -->
m

<!-- b004884 | prose | pages [14] -->
m

<!-- b004885 | prose | pages [14] -->
m

<!-- b004886 | prose | pages [14] -->
m

<!-- b004887 | prose | pages [14] -->
m

<!-- b004888 | prose | pages [14] -->
m

<!-- b004889 | prose | pages [14] -->
m

<!-- b004890 | prose | pages [14] -->
m

<!-- b004891 | prose | pages [14] -->
m

<!-- b004892 | prose | pages [14] -->
m

<!-- b004893 | prose | pages [14] -->
m

<!-- b004894 | prose | pages [14] -->
m

<!-- b004895 | prose | pages [14] -->
m

<!-- b004896 | prose | pages [14] -->
m

<!-- b004897 | prose | pages [14] -->
m

<!-- b004898 | prose | pages [14] -->
m

<!-- b004899 | prose | pages [14] -->
m

<!-- b004900 | prose | pages [14] -->
m

<!-- b004901 | prose | pages [14] -->
m

<!-- b004902 | prose | pages [14] -->
m

<!-- b004903 | prose | pages [14] -->
m

<!-- b004904 | prose | pages [14] -->
m

<!-- b004905 | prose | pages [14] -->
m

<!-- b004906 | prose | pages [14] -->
m

<!-- b004907 | prose | pages [14] -->
m

<!-- b004908 | prose | pages [14] -->
m

<!-- b004909 | prose | pages [14] -->
m

<!-- b004910 | prose | pages [14] -->
m

<!-- b004911 | prose | pages [14] -->
m

<!-- b004912 | prose | pages [14] -->
m

<!-- b004913 | prose | pages [14] -->
m

<!-- b004914 | prose | pages [14] -->
m

<!-- b004915 | prose | pages [14] -->
m

<!-- b004916 | prose | pages [14] -->
m

<!-- b004917 | prose | pages [14] -->
m

<!-- b004918 | prose | pages [14] -->
m

<!-- b004919 | prose | pages [14] -->
m

<!-- b004920 | prose | pages [14] -->
m

<!-- b004921 | prose | pages [14] -->
m

<!-- b004922 | prose | pages [14] -->
m

<!-- b004923 | prose | pages [14] -->
m

<!-- b004924 | prose | pages [14] -->
m

<!-- b004925 | prose | pages [14] -->
m

<!-- b004926 | prose | pages [14] -->
m

<!-- b004927 | prose | pages [14] -->
m

<!-- b004928 | prose | pages [14] -->
m

<!-- b004929 | prose | pages [14] -->
m

<!-- b004930 | prose | pages [14] -->
m

<!-- b004931 | prose | pages [14] -->
m

<!-- b004932 | prose | pages [14] -->
m

<!-- b004933 | prose | pages [14] -->
m

<!-- b004934 | prose | pages [14] -->
m

<!-- b004935 | prose | pages [14] -->
m

<!-- b004936 | prose | pages [14] -->
m

<!-- b004937 | prose | pages [14] -->
m

<!-- b004938 | prose | pages [14] -->
m

<!-- b004939 | prose | pages [14] -->
m

<!-- b004940 | prose | pages [14] -->
m

<!-- b004941 | prose | pages [14] -->
m

<!-- b004942 | prose | pages [14] -->
m

<!-- b004943 | prose | pages [14] -->
m

<!-- b004944 | prose | pages [14] -->
m

<!-- b004945 | prose | pages [14] -->
m

<!-- b004946 | prose | pages [14] -->
m

<!-- b004947 | prose | pages [14] -->
m

<!-- b004948 | prose | pages [14] -->
m

<!-- b004949 | prose | pages [14] -->
m

<!-- b004950 | prose | pages [14] -->
m

<!-- b004951 | prose | pages [14] -->
m

<!-- b004952 | prose | pages [14] -->
m

<!-- b004953 | prose | pages [14] -->
m

<!-- b004954 | prose | pages [14] -->
m

<!-- b004955 | prose | pages [14] -->
m

<!-- b004956 | prose | pages [14] -->
m

<!-- b004957 | prose | pages [14] -->
m

<!-- b004958 | prose | pages [14] -->
m

<!-- b004959 | prose | pages [14] -->
m

<!-- b004960 | prose | pages [14] -->
m

<!-- b004961 | prose | pages [14] -->
m

<!-- b004962 | prose | pages [14] -->
m

<!-- b004963 | prose | pages [14] -->
m

<!-- b004964 | prose | pages [14] -->
m

<!-- b004965 | prose | pages [14] -->
m

<!-- b004966 | prose | pages [14] -->
m

<!-- b004967 | prose | pages [14] -->
m

<!-- b004968 | prose | pages [14] -->
m

<!-- b004969 | prose | pages [14] -->
m

<!-- b004970 | prose | pages [14] -->
m

<!-- b004971 | prose | pages [14] -->
m

<!-- b004972 | prose | pages [14] -->
m

<!-- b004973 | prose | pages [14] -->
m

<!-- b004974 | prose | pages [14] -->
m

<!-- b004975 | prose | pages [14] -->
m

<!-- b004976 | prose | pages [14] -->
m

<!-- b004977 | prose | pages [14] -->
m

<!-- b004978 | prose | pages [14] -->
m

<!-- b004979 | prose | pages [14] -->
m

<!-- b004980 | prose | pages [14] -->
m

<!-- b004981 | prose | pages [14] -->
m

<!-- b004982 | prose | pages [14] -->
m

<!-- b004983 | prose | pages [14] -->
m

<!-- b004984 | prose | pages [14] -->
m

<!-- b004985 | prose | pages [14] -->
m

<!-- b004986 | prose | pages [14] -->
m

<!-- b004987 | prose | pages [14] -->
m

<!-- b004988 | prose | pages [14] -->
m

<!-- b004989 | prose | pages [14] -->
m

<!-- b004990 | prose | pages [14] -->
m

<!-- b004991 | prose | pages [14] -->
m

<!-- b004992 | prose | pages [14] -->
m

<!-- b004993 | prose | pages [14] -->
m

<!-- b004994 | prose | pages [14] -->
m

<!-- b004995 | prose | pages [14] -->
m

<!-- b004996 | prose | pages [14] -->
m

<!-- b004997 | prose | pages [14] -->
m

<!-- b004998 | prose | pages [14] -->
m

<!-- b004999 | prose | pages [14] -->
m

<!-- b005000 | prose | pages [14] -->
m

<!-- b005001 | prose | pages [14] -->
m

<!-- b005002 | prose | pages [14] -->
m

<!-- b005003 | prose | pages [14] -->
m

<!-- b005004 | prose | pages [14] -->
m

<!-- b005005 | prose | pages [14] -->
m

<!-- b005006 | prose | pages [14] -->
m

<!-- b005007 | prose | pages [14] -->
m

<!-- b005008 | prose | pages [14] -->
m

<!-- b005009 | prose | pages [14] -->
m

<!-- b005010 | prose | pages [14] -->
m

<!-- b005011 | prose | pages [14] -->
m

<!-- b005012 | prose | pages [14] -->
m

<!-- b005013 | prose | pages [14] -->
m

<!-- b005014 | prose | pages [14] -->
m

<!-- b005015 | prose | pages [14] -->
m

<!-- b005016 | prose | pages [14] -->
m

<!-- b005017 | prose | pages [14] -->
m

<!-- b005018 | prose | pages [14] -->
m

<!-- b005019 | prose | pages [14] -->
m

<!-- b005020 | prose | pages [14] -->
m

<!-- b005021 | prose | pages [14] -->
m

<!-- b005022 | prose | pages [14] -->
m

<!-- b005023 | prose | pages [14] -->
m

<!-- b005024 | prose | pages [14] -->
m

<!-- b005025 | prose | pages [14] -->
m

<!-- b005026 | prose | pages [14] -->
m

<!-- b005027 | prose | pages [14] -->
m

<!-- b005028 | prose | pages [14] -->
m

<!-- b005029 | prose | pages [14] -->
m

<!-- b005030 | prose | pages [14] -->
m

<!-- b005031 | prose | pages [14] -->
m

<!-- b005032 | prose | pages [14] -->
m

<!-- b005033 | prose | pages [14] -->
m

<!-- b005034 | prose | pages [14] -->
m

<!-- b005035 | prose | pages [14] -->
m

<!-- b005036 | prose | pages [14] -->
m

<!-- b005037 | prose | pages [14] -->
m

<!-- b005038 | prose | pages [14] -->
m

<!-- b005039 | prose | pages [14] -->
m

<!-- b005040 | prose | pages [14] -->
By performing regression calculations in MATLAB, the β3 coefﬁcient values corre-

<!-- b005041 | prose | pages [14] -->
m

<!-- b005042 | prose | pages [14] -->
m

<!-- b005043 | prose | pages [14] -->
m

<!-- b005044 | prose | pages [14] -->
m

<!-- b005045 | prose | pages [14] -->
m

<!-- b005046 | prose | pages [14] -->
m

<!-- b005047 | prose | pages [14] -->
m

<!-- b005048 | prose | pages [14] -->
m

<!-- b005049 | prose | pages [14] -->
m

<!-- b005050 | prose | pages [14] -->
m

<!-- b005051 | prose | pages [14] -->
m

<!-- b005052 | prose | pages [14] -->
m

<!-- b005053 | prose | pages [14] -->
m

<!-- b005054 | prose | pages [14] -->
m

<!-- b005055 | prose | pages [14] -->
m

<!-- b005056 | prose | pages [14] -->
m

<!-- b005057 | prose | pages [14] -->
m

<!-- b005058 | prose | pages [14] -->
m

<!-- b005059 | prose | pages [14] -->
m

<!-- b005060 | prose | pages [14] -->
m

<!-- b005061 | prose | pages [14] -->
m

<!-- b005062 | prose | pages [14] -->
m

<!-- b005063 | prose | pages [14] -->
m

<!-- b005064 | prose | pages [14] -->
m

<!-- b005065 | prose | pages [14] -->
m

<!-- b005066 | prose | pages [14] -->
m

<!-- b005067 | prose | pages [14] -->
m

<!-- b005068 | prose | pages [14] -->
m

<!-- b005069 | prose | pages [14] -->
m

<!-- b005070 | prose | pages [14] -->
m

<!-- b005071 | prose | pages [14] -->
m

<!-- b005072 | prose | pages [14] -->
m

<!-- b005073 | prose | pages [14] -->
m

<!-- b005074 | prose | pages [14] -->
m

<!-- b005075 | prose | pages [14] -->
m

<!-- b005076 | prose | pages [14] -->
m

<!-- b005077 | prose | pages [14] -->
m

<!-- b005078 | prose | pages [14] -->
m

<!-- b005079 | prose | pages [14] -->
m

<!-- b005080 | prose | pages [14] -->
m

<!-- b005081 | prose | pages [14] -->
m

<!-- b005082 | prose | pages [14] -->
m

<!-- b005083 | prose | pages [14] -->
m

<!-- b005084 | prose | pages [14] -->
m

<!-- b005085 | prose | pages [14] -->
m

<!-- b005086 | prose | pages [14] -->
m

<!-- b005087 | prose | pages [14] -->
m

<!-- b005088 | prose | pages [14] -->
m

<!-- b005089 | prose | pages [14] -->
m

<!-- b005090 | prose | pages [14] -->
m

<!-- b005091 | prose | pages [14] -->
m

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
sponding to each indicator for each country can be obtained, providing data support for the detailed analysis of policy effects.

<!-- b005145 | prose | pages [14] -->
In the results analysis, the key coefﬁcient β3 is used to evaluate the effectiveness of national policies on the distribution of cybercrime. If β3 > 0 and is signiﬁcant, it indicates that the policy has a positive effect on reducing the target count of cyber- crime. Conversely, if β3 < 0 or is not signiﬁcant, it suggests that the policy has limited effectiveness or may even have negative impacts.

<!-- b005146 | prose | pages [14] -->
The meaning of β3 varies depending on the indicator and requires logical adjust- ments. For instance, the β3 of target count represents the net effect of the policy in reducing the target count, where a negative value is preferable. Similarly, the β3 of success rate reﬂects the policy’s impact on reducing the success rate, with negative values being more favorable. On the other hand, the β3 of thwart rate, reporting rate, and prosecution rate reﬂects the policy’s effectiveness in improving these rates, where positive values are preferred.

<!-- b005147 | prose | pages [14] -->
关注数学模型

<!-- b005148 | furniture | pages [14] -->
2

<!-- b005149 | furniture | pages [14] -->
MATHmodels

<!-- b005150 | furniture | pages [14] -->
获取更多资讯

<!-- b005151 | furniture | pages [17] -->
Team # 2521039

<!-- b005152 | furniture | pages [17] -->
Page 17 of 25

<!-- b005153 | prose | pages [17] -->
nical Measures likely provide countries with stronger defensive capabilities and threat response mechanisms, while the high scores in Organizational Measures may reﬂect signiﬁcant advantages in policy coordination and management.

<!-- b005154 | prose | pages [17] -->
To present the results more intuitively, we used bar charts to visualize and com- pare the mean scores across different pillar groups, further conﬁrming the important roles of technical and organizational measures in cybersecurity policies. This analy- sis not only highlights the relative importance of different policy dimensions but also provides a foundation for optimizing the design and implementation of future cyber- security policies.

<!-- b005155 | prose | pages [17] -->
微信公众号：数学模型

<!-- b005156 | prose | pages [17] -->
微信号：MATHmodels

<!-- b005157 | caption | pages [17] -->
Figure 12: Averages Scores by GCI Pillars

<!-- b005158 | prose | pages [17] -->
5.3.2 Analysis of National Policy Content

<!-- b005159 | prose | pages [17] -->
In the legal domain, to address the increasingly severe threat of cybercrime, the United States enacted the˘aNational Cybersecurity Strategy˘ain 2021.In addition, the˘aInternet

<!-- b005160 | prose | pages [17] -->
[8]and other related legislation

<!-- b005161 | prose | pages [17] -->
of Things (IoT) Cybersecurity Improvement Act of 2020˘a

<!-- b005162 | prose | pages [17] -->
successfully leveraged market forces to rebalance cybersecurity responsibilities for IoT devices.

<!-- b005163 | prose | pages [17] -->
In the technical domain, the strategy aims to develop software development se- curity standards, named the˘aSecure Harbor Framework, which will draw from best practices such as the˘aNational Institute of Standards and Technology (NIST) Secure Software Development Framework (SSDF).

<!-- b005164 | prose | pages [17] -->
[9]

<!-- b005165 | prose | pages [17] -->
In the organizational domain, the U.S. cybersecurity governance structure includes three main levels: the President, policy enforcement agencies, and the private sector. Policy enforcement bodies consist of coordinating departments, government agencies,

<!-- b005166 | prose | pages [17] -->
[10] This structure enables the United

<!-- b005167 | prose | pages [17] -->
intelligence agencies, and military departments.

<!-- b005168 | prose | pages [17] -->
States to clearly deﬁne roles and responsibilities across departments in maintaining cybersecurity.

<!-- b005169 | prose | pages [17] -->
In the international cooperation domain, the United States has actively engaged in cybersecurity collaboration with the Asia-Paciﬁc region, focusing on areas such as sharing cyber intelligence, strengthening military cooperation in cyberspace, build- ing a secure cybersecurity environment, and coordinating internet policies based on

<!-- b005170 | prose | pages [17] -->
[11] On April 26, 2023, the U.S. and South Ko-

<!-- b005171 | prose | pages [17] -->
the principles of freedom and security.

<!-- b005172 | prose | pages [17] -->
[12], further expanding

<!-- b005173 | prose | pages [17] -->
rea signed the˘aStrategic Cybersecurity Cooperation Framework˘a

<!-- b005174 | prose | pages [17] -->
global cybersecurity cooperation. Canada has also deployed personnel in Washington for bilateral cooperation, and has developed the˘aCanada-U.S. Cybersecurity Action

<!-- b005175 | prose | pages [17] -->
[13]

<!-- b005176 | prose | pages [17] -->
Plan.

<!-- b005177 | furniture | pages [18] -->
Team # 2521039

<!-- b005178 | furniture | pages [18] -->
Page 18 of 25

<!-- b005179 | prose | pages [18] -->
In contrast, regarding technology, China faces signiﬁcant challenges, with its in- vestment in information security representing only 2% of the total IT market invest- ment, far below that of developed nations. Additionally, there are notable gaps in key technological areas.Regarding organization, Chinas State Council Emergency Ofﬁce of- fers only formal coordination between departments, lacking a clear leadership system and efﬁcient division of responsibilities. Furthermore, local cybersecurity emergency departments are disorganized, leading to diminished overall efﬁciency in emergency response.Regarding capability building, China faces three critical issues: a lack of cy- ber sovereignty, nearly total dependence on foreign-controlled network infrastructure,

<!-- b005180 | prose | pages [18] -->
[14] Regarding international cooperation,

<!-- b005181 | prose | pages [18] -->
and insufﬁcient mastery of core technologies.

<!-- b005182 | prose | pages [18] -->
China’s cybersecurity collaboration with ASEAN is constrained.As a result, there is currently no uniﬁed cybersecurity cooperation framework, and tangible cooperation

<!-- b005183 | prose | pages [18] -->
[15]

<!-- b005184 | prose | pages [18] -->
outcomes remain limited.

<!-- b005185 | caption | pages [18] -->
Figure 13: U.S. Policy Measures in Response to Cybersecurity Challenges

<!-- b005186 | prose | pages [18] -->
5.4 Theoretical Summary

<!-- b005187 | prose | pages [18] -->
To analyze the impact of cybersecurity policies and their implementation timing on

<!-- b005188 | heading | pages [18] -->
the distribution of cybercrime targets, multi-level linear regression and HISR models

<!-- b005189 | heading | pages [18] -->
were employed. The multi-level linear regression model demonstrated that policies

<!-- b005190 | prose | pages [18] -->
and time have both independent and interaction effects on target counts. To further

<!-- b005191 | heading | pages [18] -->
evaluate the effectiveness of policy implementation, the DID model was applied. The

<!-- b005192 | prose | pages [18] -->
m

<!-- b005193 | prose | pages [18] -->
m

<!-- b005194 | prose | pages [18] -->
m

<!-- b005195 | prose | pages [18] -->
m

<!-- b005196 | prose | pages [18] -->
m

<!-- b005197 | prose | pages [18] -->
m

<!-- b005198 | prose | pages [18] -->
m

<!-- b005199 | prose | pages [18] -->
m

<!-- b005200 | prose | pages [18] -->
m

<!-- b005201 | prose | pages [18] -->
m

<!-- b005202 | prose | pages [18] -->
m

<!-- b005203 | prose | pages [18] -->
m

<!-- b005204 | prose | pages [18] -->
m

<!-- b005205 | prose | pages [18] -->
m

<!-- b005206 | prose | pages [18] -->
m

<!-- b005207 | prose | pages [18] -->
m

<!-- b005208 | prose | pages [18] -->
m

<!-- b005209 | prose | pages [18] -->
m

<!-- b005210 | prose | pages [18] -->
m

<!-- b005211 | prose | pages [18] -->
m

<!-- b005212 | prose | pages [18] -->
m

<!-- b005213 | prose | pages [18] -->
m

<!-- b005214 | prose | pages [18] -->
m

<!-- b005215 | prose | pages [18] -->
m

<!-- b005216 | prose | pages [18] -->
m

<!-- b005217 | prose | pages [18] -->
m

<!-- b005218 | prose | pages [18] -->
m

<!-- b005219 | prose | pages [18] -->
m

<!-- b005220 | prose | pages [18] -->
m

<!-- b005221 | prose | pages [18] -->
m

<!-- b005222 | prose | pages [18] -->
m

<!-- b005223 | prose | pages [18] -->
m

<!-- b005224 | prose | pages [18] -->
m

<!-- b005225 | prose | pages [18] -->
m

<!-- b005226 | prose | pages [18] -->
m

<!-- b005227 | prose | pages [18] -->
m

<!-- b005228 | prose | pages [18] -->
m

<!-- b005229 | prose | pages [18] -->
m

<!-- b005230 | prose | pages [18] -->
m

<!-- b005231 | prose | pages [18] -->
m

<!-- b005232 | prose | pages [18] -->
m

<!-- b005233 | prose | pages [18] -->
m

<!-- b005234 | prose | pages [18] -->
m

<!-- b005235 | prose | pages [18] -->
m

<!-- b005236 | prose | pages [18] -->
m

<!-- b005237 | prose | pages [18] -->
m

<!-- b005238 | prose | pages [18] -->
m

<!-- b005239 | prose | pages [18] -->
m

<!-- b005240 | prose | pages [18] -->
m

<!-- b005241 | prose | pages [18] -->
m

<!-- b005242 | prose | pages [18] -->
m

<!-- b005243 | prose | pages [18] -->
m

<!-- b005244 | prose | pages [18] -->
m

<!-- b005245 | prose | pages [18] -->
m

<!-- b005246 | prose | pages [18] -->
m

<!-- b005247 | prose | pages [18] -->
m

<!-- b005248 | prose | pages [18] -->
m

<!-- b005249 | prose | pages [18] -->
m

<!-- b005250 | prose | pages [18] -->
m

<!-- b005251 | prose | pages [18] -->
m

<!-- b005252 | prose | pages [18] -->
m

<!-- b005253 | prose | pages [18] -->
m

<!-- b005254 | prose | pages [18] -->
m

<!-- b005255 | prose | pages [18] -->
m

<!-- b005256 | prose | pages [18] -->
m

<!-- b005257 | prose | pages [18] -->
m

<!-- b005258 | prose | pages [18] -->
m

<!-- b005259 | prose | pages [18] -->
m

<!-- b005260 | prose | pages [18] -->
m

<!-- b005261 | prose | pages [18] -->
m

<!-- b005262 | prose | pages [18] -->
m

<!-- b005263 | prose | pages [18] -->
m

<!-- b005264 | prose | pages [18] -->
m

<!-- b005265 | prose | pages [18] -->
m

<!-- b005266 | prose | pages [18] -->
m

<!-- b005267 | prose | pages [18] -->
m

<!-- b005268 | prose | pages [18] -->
m

<!-- b005269 | prose | pages [18] -->
m

<!-- b005270 | prose | pages [18] -->
m

<!-- b005271 | prose | pages [18] -->
m

<!-- b005272 | prose | pages [18] -->
m

<!-- b005273 | prose | pages [18] -->
m

<!-- b005274 | prose | pages [18] -->
m

<!-- b005275 | prose | pages [18] -->
m

<!-- b005276 | prose | pages [18] -->
m

<!-- b005277 | prose | pages [18] -->
m

<!-- b005278 | prose | pages [18] -->
m

<!-- b005279 | prose | pages [18] -->
m

<!-- b005280 | prose | pages [18] -->
m

<!-- b005281 | prose | pages [18] -->
m

<!-- b005282 | prose | pages [18] -->
m

<!-- b005283 | prose | pages [18] -->
m

<!-- b005284 | prose | pages [18] -->
m

<!-- b005285 | prose | pages [18] -->
m

<!-- b005286 | prose | pages [18] -->
m

<!-- b005287 | prose | pages [18] -->
m

<!-- b005288 | prose | pages [18] -->
m

<!-- b005289 | prose | pages [18] -->
m

<!-- b005290 | prose | pages [18] -->
m

<!-- b005291 | prose | pages [18] -->
m

<!-- b005292 | prose | pages [18] -->
m

<!-- b005293 | prose | pages [18] -->
m

<!-- b005294 | prose | pages [18] -->
m

<!-- b005295 | prose | pages [18] -->
m

<!-- b005296 | prose | pages [18] -->
m

<!-- b005297 | prose | pages [18] -->
m

<!-- b005298 | prose | pages [18] -->
m

<!-- b005299 | prose | pages [18] -->
m

<!-- b005300 | prose | pages [18] -->
m

<!-- b005301 | prose | pages [18] -->
m

<!-- b005302 | prose | pages [18] -->
m

<!-- b005303 | prose | pages [18] -->
m

<!-- b005304 | prose | pages [18] -->
m

<!-- b005305 | prose | pages [18] -->
m

<!-- b005306 | prose | pages [18] -->
m

<!-- b005307 | prose | pages [18] -->
m

<!-- b005308 | prose | pages [18] -->
m

<!-- b005309 | prose | pages [18] -->
m

<!-- b005310 | prose | pages [18] -->
m

<!-- b005311 | prose | pages [18] -->
m

<!-- b005312 | prose | pages [18] -->
m

<!-- b005313 | prose | pages [18] -->
m

<!-- b005314 | prose | pages [18] -->
m

<!-- b005315 | prose | pages [18] -->
m

<!-- b005316 | prose | pages [18] -->
m

<!-- b005317 | prose | pages [18] -->
m

<!-- b005318 | prose | pages [18] -->
m

<!-- b005319 | prose | pages [18] -->
m

<!-- b005320 | prose | pages [18] -->
m

<!-- b005321 | prose | pages [18] -->
m

<!-- b005322 | prose | pages [18] -->
regression results revealed that the United States had the most effective policies, while China had the least effective policies.

<!-- b005323 | prose | pages [18] -->
m

<!-- b005324 | prose | pages [18] -->
m

<!-- b005325 | prose | pages [18] -->
m

<!-- b005326 | prose | pages [18] -->
m

<!-- b005327 | prose | pages [18] -->
m

<!-- b005328 | prose | pages [18] -->
m

<!-- b005329 | prose | pages [18] -->
m

<!-- b005330 | prose | pages [18] -->
m

<!-- b005331 | prose | pages [18] -->
m

<!-- b005332 | prose | pages [18] -->
m

<!-- b005333 | prose | pages [18] -->
m

<!-- b005334 | prose | pages [18] -->
m

<!-- b005335 | prose | pages [18] -->
m

<!-- b005336 | prose | pages [18] -->
m

<!-- b005337 | prose | pages [18] -->
m

<!-- b005338 | prose | pages [18] -->
m

<!-- b005339 | prose | pages [18] -->
m

<!-- b005340 | prose | pages [18] -->
m

<!-- b005341 | prose | pages [18] -->
m

<!-- b005342 | prose | pages [18] -->
m

<!-- b005343 | prose | pages [18] -->
m

<!-- b005344 | prose | pages [18] -->
m

<!-- b005345 | prose | pages [18] -->
m

<!-- b005346 | prose | pages [18] -->
m

<!-- b005347 | prose | pages [18] -->
m

<!-- b005348 | prose | pages [18] -->
m

<!-- b005349 | prose | pages [18] -->
m

<!-- b005350 | prose | pages [18] -->
m

<!-- b005351 | prose | pages [18] -->
m

<!-- b005352 | prose | pages [18] -->
m

<!-- b005353 | prose | pages [18] -->
m

<!-- b005354 | prose | pages [18] -->
m

<!-- b005355 | prose | pages [18] -->
m

<!-- b005356 | prose | pages [18] -->
m

<!-- b005357 | prose | pages [18] -->
m

<!-- b005358 | prose | pages [18] -->
m

<!-- b005359 | prose | pages [18] -->
m

<!-- b005360 | prose | pages [18] -->
m

<!-- b005361 | prose | pages [18] -->
m

<!-- b005362 | prose | pages [18] -->
m

<!-- b005363 | prose | pages [18] -->
m

<!-- b005364 | prose | pages [18] -->
m

<!-- b005365 | prose | pages [18] -->
m

<!-- b005366 | prose | pages [18] -->
m

<!-- b005367 | prose | pages [18] -->
m

<!-- b005368 | prose | pages [18] -->
m

<!-- b005369 | prose | pages [18] -->
m

<!-- b005370 | prose | pages [18] -->
m

<!-- b005371 | prose | pages [18] -->
m

<!-- b005372 | prose | pages [18] -->
m

<!-- b005373 | prose | pages [18] -->
m

<!-- b005374 | prose | pages [18] -->
m

<!-- b005375 | prose | pages [18] -->
m

<!-- b005376 | prose | pages [18] -->
m

<!-- b005377 | prose | pages [18] -->
m

<!-- b005378 | prose | pages [18] -->
m

<!-- b005379 | prose | pages [18] -->
m

<!-- b005380 | prose | pages [18] -->
m

<!-- b005381 | prose | pages [18] -->
m

<!-- b005382 | prose | pages [18] -->
m

<!-- b005383 | prose | pages [18] -->
m

<!-- b005384 | prose | pages [18] -->
m

<!-- b005385 | prose | pages [18] -->
m

<!-- b005386 | prose | pages [18] -->
m

<!-- b005387 | prose | pages [18] -->
m

<!-- b005388 | prose | pages [18] -->
m

<!-- b005389 | prose | pages [18] -->
m

<!-- b005390 | prose | pages [18] -->
m

<!-- b005391 | prose | pages [18] -->
m

<!-- b005392 | prose | pages [18] -->
m

<!-- b005393 | prose | pages [18] -->
m

<!-- b005394 | prose | pages [18] -->
m

<!-- b005395 | prose | pages [18] -->
m

<!-- b005396 | prose | pages [18] -->
m

<!-- b005397 | prose | pages [18] -->
m

<!-- b005398 | prose | pages [18] -->
m

<!-- b005399 | prose | pages [18] -->
m

<!-- b005400 | prose | pages [18] -->
m

<!-- b005401 | prose | pages [18] -->
m

<!-- b005402 | prose | pages [18] -->
m

<!-- b005403 | prose | pages [18] -->
m

<!-- b005404 | prose | pages [18] -->
m

<!-- b005405 | prose | pages [18] -->
m

<!-- b005406 | prose | pages [18] -->
m

<!-- b005407 | prose | pages [18] -->
m

<!-- b005408 | prose | pages [18] -->
m

<!-- b005409 | prose | pages [18] -->
m

<!-- b005410 | prose | pages [18] -->
m

<!-- b005411 | prose | pages [18] -->
m

<!-- b005412 | prose | pages [18] -->
m

<!-- b005413 | prose | pages [18] -->
m

<!-- b005414 | prose | pages [18] -->
m

<!-- b005415 | prose | pages [18] -->
m

<!-- b005416 | prose | pages [18] -->
m

<!-- b005417 | prose | pages [18] -->
m

<!-- b005418 | prose | pages [18] -->
m

<!-- b005419 | prose | pages [18] -->
m

<!-- b005420 | prose | pages [18] -->
m

<!-- b005421 | prose | pages [18] -->
m

<!-- b005422 | prose | pages [18] -->
m

<!-- b005423 | prose | pages [18] -->
m

<!-- b005424 | prose | pages [18] -->
m

<!-- b005425 | prose | pages [18] -->
m

<!-- b005426 | prose | pages [18] -->
m

<!-- b005427 | prose | pages [18] -->
m

<!-- b005428 | prose | pages [18] -->
m

<!-- b005429 | prose | pages [18] -->
m

<!-- b005430 | prose | pages [18] -->
m

<!-- b005431 | prose | pages [18] -->
m

<!-- b005432 | prose | pages [18] -->
m

<!-- b005433 | prose | pages [18] -->
m

<!-- b005434 | prose | pages [18] -->
m

<!-- b005435 | prose | pages [18] -->
m

<!-- b005436 | prose | pages [18] -->
m

<!-- b005437 | prose | pages [18] -->
m

<!-- b005438 | prose | pages [18] -->
m

<!-- b005439 | prose | pages [18] -->
m

<!-- b005440 | prose | pages [18] -->
m

<!-- b005441 | prose | pages [18] -->
m

<!-- b005442 | prose | pages [18] -->
m

<!-- b005443 | prose | pages [18] -->
m

<!-- b005444 | prose | pages [18] -->
m

<!-- b005445 | prose | pages [18] -->
m

<!-- b005446 | prose | pages [18] -->
m

<!-- b005447 | prose | pages [18] -->
m

<!-- b005448 | prose | pages [18] -->
m

<!-- b005449 | prose | pages [18] -->
m

<!-- b005450 | prose | pages [18] -->
m

<!-- b005451 | prose | pages [18] -->
m

<!-- b005452 | prose | pages [18] -->
m

<!-- b005453 | prose | pages [18] -->
m

<!-- b005454 | prose | pages [18] -->
m

<!-- b005455 | prose | pages [18] -->
m

<!-- b005456 | prose | pages [18] -->
m

<!-- b005457 | prose | pages [18] -->
m

<!-- b005458 | prose | pages [18] -->
m

<!-- b005459 | prose | pages [18] -->
m

<!-- b005460 | prose | pages [18] -->
m

<!-- b005461 | prose | pages [18] -->
m

<!-- b005462 | prose | pages [18] -->
m

<!-- b005463 | prose | pages [18] -->
m

<!-- b005464 | prose | pages [18] -->
m

<!-- b005465 | prose | pages [18] -->
m

<!-- b005466 | prose | pages [18] -->
m

<!-- b005467 | prose | pages [18] -->
m

<!-- b005468 | prose | pages [18] -->
m

<!-- b005469 | prose | pages [18] -->
m

<!-- b005470 | prose | pages [18] -->
m

<!-- b005471 | prose | pages [18] -->
m

<!-- b005472 | prose | pages [18] -->
m

<!-- b005473 | prose | pages [18] -->
m

<!-- b005474 | prose | pages [18] -->
m

<!-- b005475 | prose | pages [18] -->
m

<!-- b005476 | prose | pages [18] -->
m

<!-- b005477 | prose | pages [18] -->
m

<!-- b005478 | prose | pages [18] -->
m

<!-- b005479 | prose | pages [18] -->
m

<!-- b005480 | prose | pages [18] -->
m

<!-- b005481 | prose | pages [18] -->
m

<!-- b005482 | prose | pages [18] -->
m

<!-- b005483 | prose | pages [18] -->
m

<!-- b005484 | prose | pages [18] -->
m

<!-- b005485 | prose | pages [18] -->
m

<!-- b005486 | prose | pages [18] -->
m

<!-- b005487 | prose | pages [18] -->
m

<!-- b005488 | prose | pages [18] -->
m

<!-- b005489 | prose | pages [18] -->
m

<!-- b005490 | prose | pages [18] -->
m

<!-- b005491 | prose | pages [18] -->
m

<!-- b005492 | prose | pages [18] -->
m

<!-- b005493 | prose | pages [18] -->
m

<!-- b005494 | prose | pages [18] -->
m

<!-- b005495 | prose | pages [18] -->
m

<!-- b005496 | prose | pages [18] -->
m

<!-- b005497 | prose | pages [18] -->
m

<!-- b005498 | prose | pages [18] -->
m

<!-- b005499 | prose | pages [18] -->
m

<!-- b005500 | prose | pages [18] -->
m

<!-- b005501 | prose | pages [18] -->
m

<!-- b005502 | prose | pages [18] -->
m

<!-- b005503 | prose | pages [18] -->
m

<!-- b005504 | prose | pages [18] -->
m

<!-- b005505 | prose | pages [18] -->
m

<!-- b005506 | prose | pages [18] -->
m

<!-- b005507 | prose | pages [18] -->
m

<!-- b005508 | prose | pages [18] -->
m

<!-- b005509 | prose | pages [18] -->
m

<!-- b005510 | prose | pages [18] -->
m

<!-- b005511 | prose | pages [18] -->
m

<!-- b005512 | prose | pages [18] -->
m

<!-- b005513 | prose | pages [18] -->
m

<!-- b005514 | prose | pages [18] -->
m

<!-- b005515 | prose | pages [18] -->
m

<!-- b005516 | prose | pages [18] -->
m

<!-- b005517 | prose | pages [18] -->
m

<!-- b005518 | prose | pages [18] -->
m

<!-- b005519 | prose | pages [18] -->
m

<!-- b005520 | prose | pages [18] -->
m

<!-- b005521 | prose | pages [18] -->
m

<!-- b005522 | prose | pages [18] -->
m

<!-- b005523 | prose | pages [18] -->
m

<!-- b005524 | prose | pages [18] -->
m

<!-- b005525 | prose | pages [18] -->
m

<!-- b005526 | prose | pages [18] -->
m

<!-- b005527 | prose | pages [18] -->
m

<!-- b005528 | prose | pages [18] -->
m

<!-- b005529 | prose | pages [18] -->
m

<!-- b005530 | prose | pages [18] -->
m

<!-- b005531 | prose | pages [18] -->
m

<!-- b005532 | prose | pages [18] -->
m

<!-- b005533 | prose | pages [18] -->
m

<!-- b005534 | prose | pages [18] -->
m

<!-- b005535 | prose | pages [18] -->
m

<!-- b005536 | prose | pages [18] -->
m

<!-- b005537 | prose | pages [18] -->
m

<!-- b005538 | prose | pages [18] -->
m

<!-- b005539 | prose | pages [18] -->
m

<!-- b005540 | prose | pages [18] -->
m

<!-- b005541 | prose | pages [18] -->
m

<!-- b005542 | prose | pages [18] -->
m

<!-- b005543 | prose | pages [18] -->
m

<!-- b005544 | prose | pages [18] -->
m

<!-- b005545 | prose | pages [18] -->
m

<!-- b005546 | prose | pages [18] -->
m

<!-- b005547 | prose | pages [18] -->
m

<!-- b005548 | prose | pages [18] -->
m

<!-- b005549 | prose | pages [18] -->
m

<!-- b005550 | prose | pages [18] -->
m

<!-- b005551 | prose | pages [18] -->
m

<!-- b005552 | prose | pages [18] -->
m

<!-- b005553 | prose | pages [18] -->
m

<!-- b005554 | prose | pages [18] -->
m

<!-- b005555 | prose | pages [18] -->
m

<!-- b005556 | prose | pages [18] -->
m

<!-- b005557 | prose | pages [18] -->
m

<!-- b005558 | prose | pages [18] -->
m

<!-- b005559 | prose | pages [18] -->
m

<!-- b005560 | prose | pages [18] -->
m

<!-- b005561 | prose | pages [18] -->
m

<!-- b005562 | prose | pages [18] -->
m

<!-- b005563 | prose | pages [18] -->
m

<!-- b005564 | prose | pages [18] -->
m

<!-- b005565 | prose | pages [18] -->
m

<!-- b005566 | prose | pages [18] -->
m

<!-- b005567 | prose | pages [18] -->
m

<!-- b005568 | prose | pages [18] -->
m

<!-- b005569 | prose | pages [18] -->
m

<!-- b005570 | prose | pages [18] -->
m

<!-- b005571 | prose | pages [18] -->
m

<!-- b005572 | prose | pages [18] -->
m

<!-- b005573 | prose | pages [18] -->
m

<!-- b005574 | prose | pages [18] -->
m

<!-- b005575 | prose | pages [18] -->
m

<!-- b005576 | prose | pages [18] -->
m

<!-- b005577 | prose | pages [18] -->
m

<!-- b005578 | prose | pages [18] -->
m

<!-- b005579 | prose | pages [18] -->
m

<!-- b005580 | prose | pages [18] -->
m

<!-- b005581 | prose | pages [18] -->
m

<!-- b005582 | prose | pages [18] -->
m

<!-- b005583 | prose | pages [18] -->
m

<!-- b005584 | prose | pages [18] -->
m

<!-- b005585 | prose | pages [18] -->
m

<!-- b005586 | prose | pages [18] -->
m

<!-- b005587 | prose | pages [18] -->
m

<!-- b005588 | prose | pages [18] -->
m

<!-- b005589 | prose | pages [18] -->
m

<!-- b005590 | prose | pages [18] -->
m

<!-- b005591 | prose | pages [18] -->
m

<!-- b005592 | prose | pages [18] -->
m

<!-- b005593 | prose | pages [18] -->
m

<!-- b005594 | prose | pages [18] -->
m

<!-- b005595 | prose | pages [18] -->
m

<!-- b005596 | prose | pages [18] -->
m

<!-- b005597 | prose | pages [18] -->
m

<!-- b005598 | prose | pages [18] -->
m

<!-- b005599 | prose | pages [18] -->
m

<!-- b005600 | prose | pages [18] -->
m

<!-- b005601 | prose | pages [18] -->
m

<!-- b005602 | prose | pages [18] -->
m

<!-- b005603 | prose | pages [18] -->
m

<!-- b005604 | prose | pages [18] -->
m

<!-- b005605 | prose | pages [18] -->
m

<!-- b005606 | prose | pages [18] -->
m

<!-- b005607 | prose | pages [18] -->
m

<!-- b005608 | prose | pages [18] -->
m

<!-- b005609 | prose | pages [18] -->
m

<!-- b005610 | prose | pages [18] -->
m

<!-- b005611 | prose | pages [18] -->
m

<!-- b005612 | prose | pages [18] -->
m

<!-- b005613 | prose | pages [18] -->
m

<!-- b005614 | prose | pages [18] -->
m

<!-- b005615 | prose | pages [18] -->
m

<!-- b005616 | prose | pages [18] -->
m

<!-- b005617 | prose | pages [18] -->
m

<!-- b005618 | prose | pages [18] -->
m

<!-- b005619 | prose | pages [18] -->
m

<!-- b005620 | prose | pages [18] -->
m

<!-- b005621 | prose | pages [18] -->
m

<!-- b005622 | prose | pages [18] -->
m

<!-- b005623 | prose | pages [18] -->
m

<!-- b005624 | prose | pages [18] -->
m

<!-- b005625 | prose | pages [18] -->
m

<!-- b005626 | prose | pages [18] -->
m

<!-- b005627 | prose | pages [18] -->
m

<!-- b005628 | prose | pages [18] -->
m

<!-- b005629 | prose | pages [18] -->
m

<!-- b005630 | prose | pages [18] -->
m

<!-- b005631 | prose | pages [18] -->
m

<!-- b005632 | prose | pages [18] -->
m

<!-- b005633 | prose | pages [18] -->
m

<!-- b005634 | prose | pages [18] -->
m

<!-- b005635 | prose | pages [18] -->
m

<!-- b005636 | prose | pages [18] -->
m

<!-- b005637 | prose | pages [18] -->
m

<!-- b005638 | prose | pages [18] -->
m

<!-- b005639 | prose | pages [18] -->
m

<!-- b005640 | prose | pages [18] -->
m

<!-- b005641 | prose | pages [18] -->
m

<!-- b005642 | prose | pages [18] -->
m

<!-- b005643 | prose | pages [18] -->
m

<!-- b005644 | prose | pages [18] -->
m

<!-- b005645 | prose | pages [18] -->
m

<!-- b005646 | prose | pages [18] -->
m

<!-- b005647 | prose | pages [18] -->
m

<!-- b005648 | prose | pages [18] -->
m

<!-- b005649 | prose | pages [18] -->
m

<!-- b005650 | prose | pages [18] -->
m

<!-- b005651 | prose | pages [18] -->
m

<!-- b005652 | prose | pages [18] -->
m

<!-- b005653 | prose | pages [18] -->
m

<!-- b005654 | prose | pages [18] -->
m

<!-- b005655 | prose | pages [18] -->
m

<!-- b005656 | prose | pages [18] -->
m

<!-- b005657 | prose | pages [18] -->
m

<!-- b005658 | prose | pages [18] -->
m

<!-- b005659 | prose | pages [18] -->
m

<!-- b005660 | prose | pages [18] -->
To identify effective policy models, policies were classiﬁed and analyzed using the

<!-- b005661 | prose | pages [18] -->
m

<!-- b005662 | prose | pages [18] -->
m

<!-- b005663 | prose | pages [18] -->
m

<!-- b005664 | prose | pages [18] -->
m

<!-- b005665 | prose | pages [18] -->
m

<!-- b005666 | prose | pages [18] -->
m

<!-- b005667 | prose | pages [18] -->
m

<!-- b005668 | prose | pages [18] -->
m

<!-- b005669 | prose | pages [18] -->
m

<!-- b005670 | prose | pages [18] -->
m

<!-- b005671 | prose | pages [18] -->
m

<!-- b005672 | prose | pages [18] -->
m

<!-- b005673 | prose | pages [18] -->
m

<!-- b005674 | prose | pages [18] -->
m

<!-- b005675 | prose | pages [18] -->
m

<!-- b005676 | prose | pages [18] -->
m

<!-- b005677 | prose | pages [18] -->
m

<!-- b005678 | prose | pages [18] -->
m

<!-- b005679 | prose | pages [18] -->
m

<!-- b005680 | prose | pages [18] -->
m

<!-- b005681 | prose | pages [18] -->
m

<!-- b005682 | prose | pages [18] -->
m

<!-- b005683 | prose | pages [18] -->
m

<!-- b005684 | prose | pages [18] -->
m

<!-- b005685 | prose | pages [18] -->
m

<!-- b005686 | prose | pages [18] -->
m

<!-- b005687 | prose | pages [18] -->
m

<!-- b005688 | prose | pages [18] -->
m

<!-- b005689 | prose | pages [18] -->
m

<!-- b005690 | prose | pages [18] -->
m

<!-- b005691 | prose | pages [18] -->
m

<!-- b005692 | prose | pages [18] -->
m

<!-- b005693 | prose | pages [18] -->
m

<!-- b005694 | prose | pages [18] -->
m

<!-- b005695 | prose | pages [18] -->
m

<!-- b005696 | prose | pages [18] -->
m

<!-- b005697 | prose | pages [18] -->
m

<!-- b005698 | prose | pages [18] -->
m

<!-- b005699 | prose | pages [18] -->
m

<!-- b005700 | prose | pages [18] -->
m

<!-- b005701 | prose | pages [18] -->
m

<!-- b005702 | prose | pages [18] -->
m

<!-- b005703 | prose | pages [18] -->
m

<!-- b005704 | prose | pages [18] -->
m

<!-- b005705 | prose | pages [18] -->
m

<!-- b005706 | prose | pages [18] -->
m

<!-- b005707 | prose | pages [18] -->
m

<!-- b005708 | prose | pages [18] -->
m

<!-- b005709 | prose | pages [18] -->
m

<!-- b005710 | prose | pages [18] -->
m

<!-- b005711 | prose | pages [18] -->
m

<!-- b005712 | prose | pages [18] -->
m

<!-- b005713 | prose | pages [18] -->
m

<!-- b005714 | prose | pages [18] -->
m

<!-- b005715 | prose | pages [18] -->
m

<!-- b005716 | prose | pages [18] -->
m

<!-- b005717 | prose | pages [18] -->
m

<!-- b005718 | prose | pages [18] -->
m

<!-- b005719 | prose | pages [18] -->
m

<!-- b005720 | prose | pages [18] -->
m

<!-- b005721 | prose | pages [18] -->
m

<!-- b005722 | prose | pages [18] -->
m

<!-- b005723 | prose | pages [18] -->
m

<!-- b005724 | prose | pages [18] -->
m

<!-- b005725 | prose | pages [18] -->
m

<!-- b005726 | prose | pages [18] -->
m

<!-- b005727 | prose | pages [18] -->
m

<!-- b005728 | prose | pages [18] -->
m

<!-- b005729 | prose | pages [18] -->
m

<!-- b005730 | prose | pages [18] -->
m

<!-- b005731 | prose | pages [18] -->
m

<!-- b005732 | prose | pages [18] -->
m

<!-- b005733 | prose | pages [18] -->
m

<!-- b005734 | prose | pages [18] -->
m

<!-- b005735 | prose | pages [18] -->
m

<!-- b005736 | prose | pages [18] -->
m

<!-- b005737 | prose | pages [18] -->
m

<!-- b005738 | prose | pages [18] -->
m

<!-- b005739 | prose | pages [18] -->
m

<!-- b005740 | prose | pages [18] -->
m

<!-- b005741 | prose | pages [18] -->
m

<!-- b005742 | prose | pages [18] -->
m

<!-- b005743 | prose | pages [18] -->
m

<!-- b005744 | prose | pages [18] -->
m

<!-- b005745 | prose | pages [18] -->
m

<!-- b005746 | prose | pages [18] -->
m

<!-- b005747 | prose | pages [18] -->
m

<!-- b005748 | prose | pages [18] -->
m

<!-- b005749 | prose | pages [18] -->
m

<!-- b005750 | prose | pages [18] -->
m

<!-- b005751 | prose | pages [18] -->
m

<!-- b005752 | prose | pages [18] -->
m

<!-- b005753 | prose | pages [18] -->
m

<!-- b005754 | prose | pages [18] -->
m

<!-- b005755 | prose | pages [18] -->
m

<!-- b005756 | prose | pages [18] -->
m

<!-- b005757 | prose | pages [18] -->
m

<!-- b005758 | prose | pages [18] -->
m

<!-- b005759 | prose | pages [18] -->
m

<!-- b005760 | prose | pages [18] -->
m

<!-- b005761 | prose | pages [18] -->
m

<!-- b005762 | prose | pages [18] -->
m

<!-- b005763 | prose | pages [18] -->
m

<!-- b005764 | prose | pages [18] -->
m

<!-- b005765 | prose | pages [18] -->
m

<!-- b005766 | prose | pages [18] -->
m

<!-- b005767 | prose | pages [18] -->
m

<!-- b005768 | prose | pages [18] -->
m

<!-- b005769 | prose | pages [18] -->
m

<!-- b005770 | prose | pages [18] -->
m

<!-- b005771 | prose | pages [18] -->
m

<!-- b005772 | prose | pages [18] -->
m

<!-- b005773 | prose | pages [18] -->
m

<!-- b005774 | prose | pages [18] -->
m

<!-- b005775 | prose | pages [18] -->
m

<!-- b005776 | prose | pages [18] -->
m

<!-- b005777 | prose | pages [18] -->
m

<!-- b005778 | prose | pages [18] -->
m

<!-- b005779 | prose | pages [18] -->
m

<!-- b005780 | prose | pages [18] -->
m

<!-- b005781 | prose | pages [18] -->
m

<!-- b005782 | prose | pages [18] -->
m

<!-- b005783 | prose | pages [18] -->
m

<!-- b005784 | prose | pages [18] -->
m

<!-- b005785 | prose | pages [18] -->
m

<!-- b005786 | prose | pages [18] -->
m

<!-- b005787 | prose | pages [18] -->
m

<!-- b005788 | prose | pages [18] -->
m

<!-- b005789 | prose | pages [18] -->
m

<!-- b005790 | prose | pages [18] -->
m

<!-- b005791 | prose | pages [18] -->
m

<!-- b005792 | prose | pages [18] -->
m

<!-- b005793 | prose | pages [18] -->
m

<!-- b005794 | prose | pages [18] -->
m

<!-- b005795 | prose | pages [18] -->
m

<!-- b005796 | prose | pages [18] -->
m

<!-- b005797 | prose | pages [18] -->
m

<!-- b005798 | prose | pages [18] -->
m

<!-- b005799 | prose | pages [18] -->
m

<!-- b005800 | prose | pages [18] -->
m

<!-- b005801 | prose | pages [18] -->
m

<!-- b005802 | prose | pages [18] -->
m

<!-- b005803 | prose | pages [18] -->
m

<!-- b005804 | prose | pages [18] -->
ﬁve pillars of the Global Cybersecurity Index (GCI). The analysis indicated that ad-

<!-- b005805 | prose | pages [18] -->
m

<!-- b005806 | prose | pages [18] -->
m

<!-- b005807 | prose | pages [18] -->
m

<!-- b005808 | prose | pages [18] -->
m

<!-- b005809 | prose | pages [18] -->
m

<!-- b005810 | prose | pages [18] -->
m

<!-- b005811 | prose | pages [18] -->
m

<!-- b005812 | prose | pages [18] -->
m

<!-- b005813 | prose | pages [18] -->
m

<!-- b005814 | prose | pages [18] -->
m

<!-- b005815 | prose | pages [18] -->
m

<!-- b005816 | prose | pages [18] -->
m

<!-- b005817 | prose | pages [18] -->
m

<!-- b005818 | prose | pages [18] -->
m

<!-- b005819 | prose | pages [18] -->
m

<!-- b005820 | prose | pages [18] -->
m

<!-- b005821 | prose | pages [18] -->
m

<!-- b005822 | prose | pages [18] -->
m

<!-- b005823 | prose | pages [18] -->
m

<!-- b005824 | prose | pages [18] -->
m

<!-- b005825 | prose | pages [18] -->
m

<!-- b005826 | prose | pages [18] -->
m

<!-- b005827 | prose | pages [18] -->
m

<!-- b005828 | prose | pages [18] -->
m

<!-- b005829 | prose | pages [18] -->
m

<!-- b005830 | prose | pages [18] -->
m

<!-- b005831 | prose | pages [18] -->
m

<!-- b005832 | prose | pages [18] -->
m

<!-- b005833 | prose | pages [18] -->
m

<!-- b005834 | prose | pages [18] -->
m

<!-- b005835 | prose | pages [18] -->
m

<!-- b005836 | prose | pages [18] -->
m

<!-- b005837 | prose | pages [18] -->
m

<!-- b005838 | prose | pages [18] -->
m

<!-- b005839 | prose | pages [18] -->
m

<!-- b005840 | prose | pages [18] -->
m

<!-- b005841 | prose | pages [18] -->
m

<!-- b005842 | prose | pages [18] -->
m

<!-- b005843 | prose | pages [18] -->
m

<!-- b005844 | prose | pages [18] -->
m

<!-- b005845 | prose | pages [18] -->
m

<!-- b005846 | prose | pages [18] -->
m

<!-- b005847 | prose | pages [18] -->
m

<!-- b005848 | prose | pages [18] -->
m

<!-- b005849 | prose | pages [18] -->
m

<!-- b005850 | prose | pages [18] -->
m

<!-- b005851 | prose | pages [18] -->
m

<!-- b005852 | prose | pages [18] -->
m

<!-- b005853 | prose | pages [18] -->
m

<!-- b005854 | prose | pages [18] -->
m

<!-- b005855 | prose | pages [18] -->
m

<!-- b005856 | prose | pages [18] -->
m

<!-- b005857 | prose | pages [18] -->
m

<!-- b005858 | prose | pages [18] -->
m

<!-- b005859 | prose | pages [18] -->
m

<!-- b005860 | prose | pages [18] -->
m

<!-- b005861 | prose | pages [18] -->
m

<!-- b005862 | prose | pages [18] -->
m

<!-- b005863 | prose | pages [18] -->
m

<!-- b005864 | prose | pages [18] -->
m

<!-- b005865 | prose | pages [18] -->
m

<!-- b005866 | prose | pages [18] -->
m

<!-- b005867 | prose | pages [18] -->
m

<!-- b005868 | prose | pages [18] -->
m

<!-- b005869 | prose | pages [18] -->
m

<!-- b005870 | prose | pages [18] -->
m

<!-- b005871 | prose | pages [18] -->
m

<!-- b005872 | prose | pages [18] -->
m

<!-- b005873 | prose | pages [18] -->
m

<!-- b005874 | prose | pages [18] -->
m

<!-- b005875 | prose | pages [18] -->
m

<!-- b005876 | prose | pages [18] -->
m

<!-- b005877 | prose | pages [18] -->
m

<!-- b005878 | prose | pages [18] -->
m

<!-- b005879 | prose | pages [18] -->
m

<!-- b005880 | prose | pages [18] -->
m

<!-- b005881 | prose | pages [18] -->
m

<!-- b005882 | prose | pages [18] -->
vancements in technical capabilities and efﬁcient organizational coordination are critical factors for policy success. Additionally, a comparison of policies in the United States and China showed that the United States excels in legal framework, technical infrastructure, organizational coordination, and international cooperation, resulting in signiﬁcant policy outcomes. In contrast, China suffers from insufﬁcient investment in information security, a lack of uniﬁed leadership, weak core technologies, and the absence of a robust cybersecurity cooperation framework.

<!-- b005883 | prose | pages [18] -->
Overall, the United States’ policies are effective and balanced, emphasizing techni- cal capabilities and data transparency. Conversely, Chinas policies are ineffective, re- ﬂecting weak technical capacity, insufﬁcient comprehensiveness in policy design, and

<!-- b005884 | prose | pages [18] -->
关注数学模型

<!-- b005885 | prose | pages [18] -->
inadequate enforcement capabilities. Moving forward, optimizing cybersecurity poli-

<!-- b005886 | furniture | pages [18] -->
2

<!-- b005887 | furniture | pages [18] -->
MATHmodels

<!-- b005888 | furniture | pages [18] -->
获取更多资讯

<!-- b005889 | furniture | pages [19] -->
Team # 2521039

<!-- b005890 | furniture | pages [19] -->
Page 19 of 25

<!-- b005891 | prose | pages [19] -->
cies should focus on enhancing technical capacity, defense mechanisms, and judicial process coordination while strengthening international cooperation and technology sharing to collectively address global cybercrime threats.

<!-- b005892 | prose | pages [19] -->
6 National Demographics and Cybercrime Distribution

<!-- b005893 | prose | pages [19] -->
微信公众号：数学模型

<!-- b005894 | prose | pages [19] -->
6.1 Correlation Analysis

<!-- b005895 | prose | pages [19] -->
Based on the above conclusions, we collected nine national demographic data points from the World Bank Data Platform, including internet usage rate, ICT product export value, total population, Gini index, GDP, GDP growth rate, gross national income, ed- ucation rate, and education level. These datasets were then integrated with cybercrime data (Target Count) from the VCDB database. After cleaning and organizing the data, scatter plots were created to observe and analyze the data distribution, providing an initial assessment of the correlation between national demographic data and cyber-

<!-- b005896 | prose | pages [19] -->
微信号：MATHmodels

<!-- b005897 | prose | pages [19] -->
crime data (Target Count).

<!-- b005898 | caption | pages [19] -->
Figure 14: Scatter plot of national demographic data distribution

<!-- b005899 | prose | pages [19] -->
Next, we applied Spearman’s correlation coefﬁcient to perform pairwise correla- tion analysis on the data, generating a Spearman correlation coefﬁcient matrix. The results were visualized in the form of a heatmap to intuitively present the outcomes of the correlation analysis.

<!-- b005900 | prose | pages [19] -->
From the Spearman correlation heatmap, it is evident that the target variable (Target Count) exhibits signiﬁcant correlations with several key variables. Among them, the correlation with GDP is the highest, with a coefﬁcient of 0.77, indicating that economic scale has a strong inﬂuence on cybercrime targets. The correlation with Population is 0.50, reﬂecting a moderate impact of population size on the distribution of cybercrime. The correlation with ICT Goods Export is 0.41, suggesting that the level of internet access may partially inﬂuence the distribution of cybercrime.

<!-- b005901 | prose | pages [19] -->
In contrast, variables such as the Gini Index, education rate, and others show

<!-- b005902 | prose | pages [19] -->
m

<!-- b005903 | prose | pages [19] -->
m

<!-- b005904 | prose | pages [19] -->
m

<!-- b005905 | prose | pages [19] -->
m

<!-- b005906 | prose | pages [19] -->
m

<!-- b005907 | prose | pages [19] -->
m

<!-- b005908 | prose | pages [19] -->
m

<!-- b005909 | prose | pages [19] -->
m

<!-- b005910 | prose | pages [19] -->
m

<!-- b005911 | prose | pages [19] -->
m

<!-- b005912 | prose | pages [19] -->
m

<!-- b005913 | prose | pages [19] -->
m

<!-- b005914 | prose | pages [19] -->
m

<!-- b005915 | prose | pages [19] -->
m

<!-- b005916 | prose | pages [19] -->
m

<!-- b005917 | prose | pages [19] -->
m

<!-- b005918 | prose | pages [19] -->
m

<!-- b005919 | prose | pages [19] -->
m

<!-- b005920 | prose | pages [19] -->
m

<!-- b005921 | prose | pages [19] -->
m

<!-- b005922 | prose | pages [19] -->
m

<!-- b005923 | prose | pages [19] -->
m

<!-- b005924 | prose | pages [19] -->
m

<!-- b005925 | prose | pages [19] -->
m

<!-- b005926 | prose | pages [19] -->
m

<!-- b005927 | prose | pages [19] -->
m

<!-- b005928 | prose | pages [19] -->
m

<!-- b005929 | prose | pages [19] -->
m

<!-- b005930 | prose | pages [19] -->
m

<!-- b005931 | prose | pages [19] -->
m

<!-- b005932 | prose | pages [19] -->
m

<!-- b005933 | prose | pages [19] -->
m

<!-- b005934 | prose | pages [19] -->
m

<!-- b005935 | prose | pages [19] -->
m

<!-- b005936 | prose | pages [19] -->
m

<!-- b005937 | prose | pages [19] -->
m

<!-- b005938 | prose | pages [19] -->
m

<!-- b005939 | prose | pages [19] -->
m

<!-- b005940 | prose | pages [19] -->
m

<!-- b005941 | prose | pages [19] -->
m

<!-- b005942 | prose | pages [19] -->
m

<!-- b005943 | prose | pages [19] -->
m

<!-- b005944 | prose | pages [19] -->
m

<!-- b005945 | prose | pages [19] -->
m

<!-- b005946 | prose | pages [19] -->
m

<!-- b005947 | prose | pages [19] -->
m

<!-- b005948 | prose | pages [19] -->
m

<!-- b005949 | prose | pages [19] -->
m

<!-- b005950 | prose | pages [19] -->
m

<!-- b005951 | prose | pages [19] -->
m

<!-- b005952 | prose | pages [19] -->
m

<!-- b005953 | prose | pages [19] -->
m

<!-- b005954 | prose | pages [19] -->
m

<!-- b005955 | prose | pages [19] -->
weaker correlations, indicating that income inequality and education levels have a lim-

<!-- b005956 | prose | pages [19] -->
m

<!-- b005957 | prose | pages [19] -->
m

<!-- b005958 | prose | pages [19] -->
m

<!-- b005959 | prose | pages [19] -->
m

<!-- b005960 | prose | pages [19] -->
m

<!-- b005961 | prose | pages [19] -->
m

<!-- b005962 | prose | pages [19] -->
m

<!-- b005963 | prose | pages [19] -->
m

<!-- b005964 | prose | pages [19] -->
m

<!-- b005965 | prose | pages [19] -->
m

<!-- b005966 | prose | pages [19] -->
m

<!-- b005967 | prose | pages [19] -->
m

<!-- b005968 | prose | pages [19] -->
m

<!-- b005969 | prose | pages [19] -->
m

<!-- b005970 | prose | pages [19] -->
m

<!-- b005971 | prose | pages [19] -->
m

<!-- b005972 | prose | pages [19] -->
m

<!-- b005973 | prose | pages [19] -->
m

<!-- b005974 | prose | pages [19] -->
m

<!-- b005975 | prose | pages [19] -->
m

<!-- b005976 | prose | pages [19] -->
m

<!-- b005977 | prose | pages [19] -->
m

<!-- b005978 | prose | pages [19] -->
m

<!-- b005979 | prose | pages [19] -->
m

<!-- b005980 | prose | pages [19] -->
m

<!-- b005981 | prose | pages [19] -->
m

<!-- b005982 | prose | pages [19] -->
m

<!-- b005983 | prose | pages [19] -->
m

<!-- b005984 | prose | pages [19] -->
m

<!-- b005985 | prose | pages [19] -->
m

<!-- b005986 | prose | pages [19] -->
m

<!-- b005987 | prose | pages [19] -->
m

<!-- b005988 | prose | pages [19] -->
m

<!-- b005989 | prose | pages [19] -->
m

<!-- b005990 | prose | pages [19] -->
m

<!-- b005991 | prose | pages [19] -->
m

<!-- b005992 | prose | pages [19] -->
m

<!-- b005993 | prose | pages [19] -->
m

<!-- b005994 | prose | pages [19] -->
m

<!-- b005995 | prose | pages [19] -->
m

<!-- b005996 | prose | pages [19] -->
m

<!-- b005997 | prose | pages [19] -->
m

<!-- b005998 | prose | pages [19] -->
m

<!-- b005999 | prose | pages [19] -->
m

<!-- b006000 | prose | pages [19] -->
m

<!-- b006001 | prose | pages [19] -->
m

<!-- b006002 | prose | pages [19] -->
m

<!-- b006003 | prose | pages [19] -->
m

<!-- b006004 | prose | pages [19] -->
m

<!-- b006005 | prose | pages [19] -->
m

<!-- b006006 | prose | pages [19] -->
m

<!-- b006007 | prose | pages [19] -->
m

<!-- b006008 | prose | pages [19] -->
m

<!-- b006009 | prose | pages [19] -->
m

<!-- b006010 | prose | pages [19] -->
m

<!-- b006011 | prose | pages [19] -->
m

<!-- b006012 | prose | pages [19] -->
m

<!-- b006013 | prose | pages [19] -->
m

<!-- b006014 | prose | pages [19] -->
m

<!-- b006015 | prose | pages [19] -->
m

<!-- b006016 | prose | pages [19] -->
m

<!-- b006017 | prose | pages [19] -->
m

<!-- b006018 | prose | pages [19] -->
m

<!-- b006019 | prose | pages [19] -->
m

<!-- b006020 | prose | pages [19] -->
m

<!-- b006021 | prose | pages [19] -->
m

<!-- b006022 | prose | pages [19] -->
m

<!-- b006023 | prose | pages [19] -->
m

<!-- b006024 | prose | pages [19] -->
m

<!-- b006025 | prose | pages [19] -->
m

<!-- b006026 | prose | pages [19] -->
m

<!-- b006027 | prose | pages [19] -->
m

<!-- b006028 | prose | pages [19] -->
m

<!-- b006029 | prose | pages [19] -->
m

<!-- b006030 | prose | pages [19] -->
m

<!-- b006031 | prose | pages [19] -->
m

<!-- b006032 | prose | pages [19] -->
m

<!-- b006033 | prose | pages [19] -->
m

<!-- b006034 | prose | pages [19] -->
m

<!-- b006035 | prose | pages [19] -->
m

<!-- b006036 | prose | pages [19] -->
m

<!-- b006037 | prose | pages [19] -->
m

<!-- b006038 | prose | pages [19] -->
m

<!-- b006039 | prose | pages [19] -->
m

<!-- b006040 | prose | pages [19] -->
m

<!-- b006041 | prose | pages [19] -->
m

<!-- b006042 | prose | pages [19] -->
m

<!-- b006043 | prose | pages [19] -->
m

<!-- b006044 | prose | pages [19] -->
m

<!-- b006045 | prose | pages [19] -->
m

<!-- b006046 | prose | pages [19] -->
m

<!-- b006047 | prose | pages [19] -->
m

<!-- b006048 | prose | pages [19] -->
m

<!-- b006049 | prose | pages [19] -->
m

<!-- b006050 | prose | pages [19] -->
m

<!-- b006051 | prose | pages [19] -->
m

<!-- b006052 | prose | pages [19] -->
m

<!-- b006053 | prose | pages [19] -->
m

<!-- b006054 | prose | pages [19] -->
m

<!-- b006055 | prose | pages [19] -->
m

<!-- b006056 | prose | pages [19] -->
m

<!-- b006057 | prose | pages [19] -->
m

<!-- b006058 | prose | pages [19] -->
m

<!-- b006059 | prose | pages [19] -->
m

<!-- b006060 | prose | pages [19] -->
m

<!-- b006061 | prose | pages [19] -->
m

<!-- b006062 | prose | pages [19] -->
m

<!-- b006063 | prose | pages [19] -->
m

<!-- b006064 | prose | pages [19] -->
m

<!-- b006065 | prose | pages [19] -->
m

<!-- b006066 | prose | pages [19] -->
m

<!-- b006067 | prose | pages [19] -->
m

<!-- b006068 | prose | pages [19] -->
m

<!-- b006069 | prose | pages [19] -->
m

<!-- b006070 | prose | pages [19] -->
m

<!-- b006071 | prose | pages [19] -->
m

<!-- b006072 | prose | pages [19] -->
m

<!-- b006073 | prose | pages [19] -->
m

<!-- b006074 | prose | pages [19] -->
m

<!-- b006075 | prose | pages [19] -->
m

<!-- b006076 | prose | pages [19] -->
m

<!-- b006077 | prose | pages [19] -->
m

<!-- b006078 | prose | pages [19] -->
m

<!-- b006079 | prose | pages [19] -->
m

<!-- b006080 | prose | pages [19] -->
m

<!-- b006081 | prose | pages [19] -->
m

<!-- b006082 | prose | pages [19] -->
m

<!-- b006083 | prose | pages [19] -->
m

<!-- b006084 | prose | pages [19] -->
m

<!-- b006085 | prose | pages [19] -->
m

<!-- b006086 | prose | pages [19] -->
m

<!-- b006087 | prose | pages [19] -->
m

<!-- b006088 | prose | pages [19] -->
m

<!-- b006089 | prose | pages [19] -->
m

<!-- b006090 | prose | pages [19] -->
m

<!-- b006091 | prose | pages [19] -->
m

<!-- b006092 | prose | pages [19] -->
m

<!-- b006093 | prose | pages [19] -->
m

<!-- b006094 | prose | pages [19] -->
m

<!-- b006095 | prose | pages [19] -->
m

<!-- b006096 | prose | pages [19] -->
m

<!-- b006097 | prose | pages [19] -->
m

<!-- b006098 | prose | pages [19] -->
m

<!-- b006099 | prose | pages [19] -->
m

<!-- b006100 | prose | pages [19] -->
m

<!-- b006101 | prose | pages [19] -->
m

<!-- b006102 | prose | pages [19] -->
m

<!-- b006103 | prose | pages [19] -->
m

<!-- b006104 | prose | pages [19] -->
m

<!-- b006105 | prose | pages [19] -->
m

<!-- b006106 | prose | pages [19] -->
m

<!-- b006107 | prose | pages [19] -->
m

<!-- b006108 | prose | pages [19] -->
m

<!-- b006109 | prose | pages [19] -->
m

<!-- b006110 | prose | pages [19] -->
m

<!-- b006111 | prose | pages [19] -->
m

<!-- b006112 | prose | pages [19] -->
ited impact on the target variable. Overall, economic and population size emerge as

<!-- b006113 | prose | pages [19] -->
m

<!-- b006114 | prose | pages [19] -->
m

<!-- b006115 | prose | pages [19] -->
m

<!-- b006116 | prose | pages [19] -->
m

<!-- b006117 | prose | pages [19] -->
m

<!-- b006118 | prose | pages [19] -->
m

<!-- b006119 | prose | pages [19] -->
m

<!-- b006120 | prose | pages [19] -->
m

<!-- b006121 | prose | pages [19] -->
m

<!-- b006122 | prose | pages [19] -->
m

<!-- b006123 | prose | pages [19] -->
m

<!-- b006124 | prose | pages [19] -->
m

<!-- b006125 | prose | pages [19] -->
m

<!-- b006126 | prose | pages [19] -->
m

<!-- b006127 | prose | pages [19] -->
m

<!-- b006128 | prose | pages [19] -->
m

<!-- b006129 | prose | pages [19] -->
m

<!-- b006130 | prose | pages [19] -->
m

<!-- b006131 | prose | pages [19] -->
m

<!-- b006132 | prose | pages [19] -->
m

<!-- b006133 | prose | pages [19] -->
m

<!-- b006134 | prose | pages [19] -->
m

<!-- b006135 | prose | pages [19] -->
m

<!-- b006136 | prose | pages [19] -->
m

<!-- b006137 | prose | pages [19] -->
m

<!-- b006138 | prose | pages [19] -->
m

<!-- b006139 | prose | pages [19] -->
m

<!-- b006140 | prose | pages [19] -->
m

<!-- b006141 | prose | pages [19] -->
m

<!-- b006142 | prose | pages [19] -->
m

<!-- b006143 | prose | pages [19] -->
m

<!-- b006144 | prose | pages [19] -->
m

<!-- b006145 | prose | pages [19] -->
m

<!-- b006146 | prose | pages [19] -->
m

<!-- b006147 | prose | pages [19] -->
m

<!-- b006148 | prose | pages [19] -->
m

<!-- b006149 | prose | pages [19] -->
m

<!-- b006150 | prose | pages [19] -->
m

<!-- b006151 | prose | pages [19] -->
m

<!-- b006152 | prose | pages [19] -->
m

<!-- b006153 | prose | pages [19] -->
m

<!-- b006154 | prose | pages [19] -->
m

<!-- b006155 | prose | pages [19] -->
m

<!-- b006156 | prose | pages [19] -->
m

<!-- b006157 | prose | pages [19] -->
m

<!-- b006158 | prose | pages [19] -->
m

<!-- b006159 | prose | pages [19] -->
m

<!-- b006160 | prose | pages [19] -->
m

<!-- b006161 | prose | pages [19] -->
m

<!-- b006162 | prose | pages [19] -->
m

<!-- b006163 | prose | pages [19] -->
m

<!-- b006164 | prose | pages [19] -->
m

<!-- b006165 | prose | pages [19] -->
m

<!-- b006166 | prose | pages [19] -->
m

<!-- b006167 | prose | pages [19] -->
m

<!-- b006168 | prose | pages [19] -->
m

<!-- b006169 | prose | pages [19] -->
m

<!-- b006170 | prose | pages [19] -->
m

<!-- b006171 | prose | pages [19] -->
m

<!-- b006172 | prose | pages [19] -->
m

<!-- b006173 | prose | pages [19] -->
m

<!-- b006174 | prose | pages [19] -->
m

<!-- b006175 | prose | pages [19] -->
m

<!-- b006176 | prose | pages [19] -->
m

<!-- b006177 | prose | pages [19] -->
m

<!-- b006178 | prose | pages [19] -->
m

<!-- b006179 | prose | pages [19] -->
m

<!-- b006180 | prose | pages [19] -->
m

<!-- b006181 | prose | pages [19] -->
m

<!-- b006182 | prose | pages [19] -->
m

<!-- b006183 | prose | pages [19] -->
m

<!-- b006184 | prose | pages [19] -->
m

<!-- b006185 | prose | pages [19] -->
m

<!-- b006186 | prose | pages [19] -->
m

<!-- b006187 | prose | pages [19] -->
m

<!-- b006188 | furniture | pages [19] -->
m

<!-- b006189 | furniture | pages [19] -->
m

<!-- b006190 | furniture | pages [19] -->
m

<!-- b006191 | furniture | pages [19] -->
m

<!-- b006192 | furniture | pages [19] -->
m

<!-- b006193 | furniture | pages [19] -->
m

<!-- b006194 | furniture | pages [19] -->
m

<!-- b006195 | furniture | pages [19] -->
m

<!-- b006196 | furniture | pages [19] -->
m

<!-- b006197 | furniture | pages [19] -->
m

<!-- b006198 | furniture | pages [19] -->
m

<!-- b006199 | furniture | pages [19] -->
m

<!-- b006200 | furniture | pages [19] -->
m

<!-- b006201 | furniture | pages [19] -->
m

<!-- b006202 | furniture | pages [19] -->
m

<!-- b006203 | furniture | pages [19] -->
m

<!-- b006204 | furniture | pages [19] -->
m

<!-- b006205 | furniture | pages [19] -->
m

<!-- b006206 | furniture | pages [19] -->
m

<!-- b006207 | furniture | pages [19] -->
m

<!-- b006208 | furniture | pages [19] -->
m

<!-- b006209 | furniture | pages [19] -->
m

<!-- b006210 | furniture | pages [19] -->
m

<!-- b006211 | furniture | pages [19] -->
m

<!-- b006212 | furniture | pages [19] -->
m

<!-- b006213 | furniture | pages [19] -->
m

<!-- b006214 | furniture | pages [19] -->
m

<!-- b006215 | furniture | pages [19] -->
m

<!-- b006216 | furniture | pages [19] -->
m

<!-- b006217 | furniture | pages [19] -->
m

<!-- b006218 | furniture | pages [19] -->
m

<!-- b006219 | furniture | pages [19] -->
m

<!-- b006220 | furniture | pages [19] -->
m

<!-- b006221 | furniture | pages [19] -->
m

<!-- b006222 | furniture | pages [19] -->
m

<!-- b006223 | furniture | pages [19] -->
m

<!-- b006224 | furniture | pages [19] -->
m

<!-- b006225 | furniture | pages [19] -->
m

<!-- b006226 | furniture | pages [19] -->
m

<!-- b006227 | furniture | pages [19] -->
m

<!-- b006228 | furniture | pages [19] -->
m

<!-- b006229 | furniture | pages [19] -->
m

<!-- b006230 | furniture | pages [19] -->
m

<!-- b006231 | furniture | pages [19] -->
m

<!-- b006232 | furniture | pages [19] -->
m

<!-- b006233 | furniture | pages [19] -->
m

<!-- b006234 | furniture | pages [19] -->
m

<!-- b006235 | furniture | pages [19] -->
m

<!-- b006236 | furniture | pages [19] -->
m

<!-- b006237 | furniture | pages [19] -->
m

<!-- b006238 | furniture | pages [19] -->
m

<!-- b006239 | furniture | pages [19] -->
m

<!-- b006240 | furniture | pages [19] -->
m

<!-- b006241 | furniture | pages [19] -->
m

<!-- b006242 | furniture | pages [19] -->
m

<!-- b006243 | furniture | pages [19] -->
m

<!-- b006244 | furniture | pages [19] -->
m

<!-- b006245 | furniture | pages [19] -->
m

<!-- b006246 | furniture | pages [19] -->
m

<!-- b006247 | furniture | pages [19] -->
m

<!-- b006248 | furniture | pages [19] -->
m

<!-- b006249 | furniture | pages [19] -->
m

<!-- b006250 | furniture | pages [19] -->
m

<!-- b006251 | furniture | pages [19] -->
m

<!-- b006252 | furniture | pages [19] -->
m

<!-- b006253 | furniture | pages [19] -->
m

<!-- b006254 | furniture | pages [19] -->
m

<!-- b006255 | furniture | pages [19] -->
m

<!-- b006256 | furniture | pages [19] -->
m

<!-- b006257 | furniture | pages [19] -->
m

<!-- b006258 | furniture | pages [19] -->
m

<!-- b006259 | furniture | pages [19] -->
m

<!-- b006260 | furniture | pages [19] -->
m

<!-- b006261 | furniture | pages [19] -->
m

<!-- b006262 | furniture | pages [19] -->
m

<!-- b006263 | furniture | pages [19] -->
m

<!-- b006264 | furniture | pages [19] -->
m

<!-- b006265 | furniture | pages [19] -->
m

<!-- b006266 | furniture | pages [19] -->
m

<!-- b006267 | furniture | pages [19] -->
m

<!-- b006268 | furniture | pages [19] -->
m

<!-- b006269 | furniture | pages [19] -->
m

<!-- b006270 | furniture | pages [19] -->
m

<!-- b006271 | furniture | pages [19] -->
m

<!-- b006272 | furniture | pages [19] -->
m

<!-- b006273 | furniture | pages [19] -->
m

<!-- b006274 | furniture | pages [19] -->
m

<!-- b006275 | furniture | pages [19] -->
m

<!-- b006276 | furniture | pages [19] -->
m

<!-- b006277 | furniture | pages [19] -->
m

<!-- b006278 | furniture | pages [19] -->
m

<!-- b006279 | furniture | pages [19] -->
m

<!-- b006280 | furniture | pages [19] -->
m

<!-- b006281 | furniture | pages [19] -->
m

<!-- b006282 | furniture | pages [19] -->
m

<!-- b006283 | furniture | pages [19] -->
m

<!-- b006284 | furniture | pages [19] -->
m

<!-- b006285 | furniture | pages [19] -->
m

<!-- b006286 | furniture | pages [19] -->
m

<!-- b006287 | furniture | pages [19] -->
m

<!-- b006288 | furniture | pages [19] -->
m

<!-- b006289 | furniture | pages [19] -->
m

<!-- b006290 | furniture | pages [19] -->
m

<!-- b006291 | furniture | pages [19] -->
m

<!-- b006292 | furniture | pages [19] -->
m

<!-- b006293 | furniture | pages [19] -->
m

<!-- b006294 | furniture | pages [19] -->
m

<!-- b006295 | furniture | pages [19] -->
m

<!-- b006296 | furniture | pages [19] -->
m

<!-- b006297 | furniture | pages [19] -->
m

<!-- b006298 | furniture | pages [19] -->
m

<!-- b006299 | furniture | pages [19] -->
m

<!-- b006300 | furniture | pages [19] -->
m

<!-- b006301 | furniture | pages [19] -->
m

<!-- b006302 | furniture | pages [19] -->
m

<!-- b006303 | furniture | pages [19] -->
m

<!-- b006304 | furniture | pages [19] -->
m

<!-- b006305 | furniture | pages [19] -->
m

<!-- b006306 | furniture | pages [19] -->
m

<!-- b006307 | furniture | pages [19] -->
m

<!-- b006308 | furniture | pages [19] -->
m

<!-- b006309 | furniture | pages [19] -->
m

<!-- b006310 | furniture | pages [19] -->
m

<!-- b006311 | furniture | pages [19] -->
m

<!-- b006312 | furniture | pages [19] -->
m

<!-- b006313 | furniture | pages [19] -->
m

<!-- b006314 | furniture | pages [19] -->
m

<!-- b006315 | furniture | pages [19] -->
m

<!-- b006316 | furniture | pages [19] -->
m

<!-- b006317 | furniture | pages [19] -->
m

<!-- b006318 | furniture | pages [19] -->
m

<!-- b006319 | furniture | pages [19] -->
m

<!-- b006320 | furniture | pages [19] -->
m

<!-- b006321 | furniture | pages [19] -->
m

<!-- b006322 | furniture | pages [19] -->
m

<!-- b006323 | furniture | pages [19] -->
m

<!-- b006324 | furniture | pages [19] -->
m

<!-- b006325 | furniture | pages [19] -->
m

<!-- b006326 | furniture | pages [19] -->
m

<!-- b006327 | furniture | pages [19] -->
m

<!-- b006328 | furniture | pages [19] -->
m

<!-- b006329 | furniture | pages [19] -->
m

<!-- b006330 | furniture | pages [19] -->
m

<!-- b006331 | furniture | pages [19] -->
m

<!-- b006332 | furniture | pages [19] -->
m

<!-- b006333 | furniture | pages [19] -->
m

<!-- b006334 | furniture | pages [19] -->
m

<!-- b006335 | furniture | pages [19] -->
m

<!-- b006336 | furniture | pages [19] -->
m

<!-- b006337 | furniture | pages [19] -->
m

<!-- b006338 | furniture | pages [19] -->
m

<!-- b006339 | furniture | pages [19] -->
m

<!-- b006340 | furniture | pages [19] -->
m

<!-- b006341 | furniture | pages [19] -->
m

<!-- b006342 | furniture | pages [19] -->
m

<!-- b006343 | furniture | pages [19] -->
m

<!-- b006344 | furniture | pages [19] -->
m

<!-- b006345 | furniture | pages [19] -->
m

<!-- b006346 | furniture | pages [19] -->
m

<!-- b006347 | furniture | pages [19] -->
m

<!-- b006348 | furniture | pages [19] -->
m

<!-- b006349 | furniture | pages [19] -->
m

<!-- b006350 | furniture | pages [19] -->
m

<!-- b006351 | furniture | pages [19] -->
m

<!-- b006352 | furniture | pages [19] -->
m

<!-- b006353 | furniture | pages [19] -->
m

<!-- b006354 | furniture | pages [19] -->
m

<!-- b006355 | furniture | pages [19] -->
m

<!-- b006356 | furniture | pages [19] -->
m

<!-- b006357 | furniture | pages [19] -->
m

<!-- b006358 | furniture | pages [19] -->
m

<!-- b006359 | furniture | pages [19] -->
m

<!-- b006360 | furniture | pages [19] -->
m

<!-- b006361 | furniture | pages [19] -->
m

<!-- b006362 | furniture | pages [19] -->
m

<!-- b006363 | furniture | pages [19] -->
m

<!-- b006364 | furniture | pages [19] -->
m

<!-- b006365 | furniture | pages [19] -->
m

<!-- b006366 | furniture | pages [19] -->
m

<!-- b006367 | furniture | pages [19] -->
m

<!-- b006368 | furniture | pages [19] -->
m

<!-- b006369 | furniture | pages [19] -->
m

<!-- b006370 | furniture | pages [19] -->
m

<!-- b006371 | furniture | pages [19] -->
m

<!-- b006372 | furniture | pages [19] -->
m

<!-- b006373 | furniture | pages [19] -->
m

<!-- b006374 | furniture | pages [19] -->
m

<!-- b006375 | furniture | pages [19] -->
m

<!-- b006376 | furniture | pages [19] -->
m

<!-- b006377 | furniture | pages [19] -->
m

<!-- b006378 | furniture | pages [19] -->
m

<!-- b006379 | furniture | pages [19] -->
m

<!-- b006380 | furniture | pages [19] -->
m

<!-- b006381 | furniture | pages [19] -->
m

<!-- b006382 | furniture | pages [19] -->
m

<!-- b006383 | furniture | pages [19] -->
m

<!-- b006384 | furniture | pages [19] -->
m

<!-- b006385 | furniture | pages [19] -->
m

<!-- b006386 | furniture | pages [19] -->
m

<!-- b006387 | furniture | pages [19] -->
m

<!-- b006388 | furniture | pages [19] -->
m

<!-- b006389 | furniture | pages [19] -->
m

<!-- b006390 | furniture | pages [19] -->
m

<!-- b006391 | furniture | pages [19] -->
m

<!-- b006392 | furniture | pages [19] -->
m

<!-- b006393 | furniture | pages [19] -->
m

<!-- b006394 | furniture | pages [19] -->
m

<!-- b006395 | furniture | pages [19] -->
m

<!-- b006396 | furniture | pages [19] -->
m

<!-- b006397 | furniture | pages [19] -->
m

<!-- b006398 | furniture | pages [19] -->
m

<!-- b006399 | furniture | pages [19] -->
m

<!-- b006400 | furniture | pages [19] -->
m

<!-- b006401 | furniture | pages [19] -->
m

<!-- b006402 | furniture | pages [19] -->
m

<!-- b006403 | furniture | pages [19] -->
m

<!-- b006404 | furniture | pages [19] -->
m

<!-- b006405 | furniture | pages [19] -->
m

<!-- b006406 | furniture | pages [19] -->
m

<!-- b006407 | furniture | pages [19] -->
m

<!-- b006408 | furniture | pages [19] -->
m

<!-- b006409 | furniture | pages [19] -->
m

<!-- b006410 | furniture | pages [19] -->
m

<!-- b006411 | furniture | pages [19] -->
m

<!-- b006412 | furniture | pages [19] -->
m

<!-- b006413 | furniture | pages [19] -->
m

<!-- b006414 | furniture | pages [19] -->
m

<!-- b006415 | furniture | pages [19] -->
m

<!-- b006416 | furniture | pages [19] -->
m

<!-- b006417 | furniture | pages [19] -->
m

<!-- b006418 | furniture | pages [19] -->
m

<!-- b006419 | furniture | pages [19] -->
m

<!-- b006420 | furniture | pages [19] -->
m

<!-- b006421 | furniture | pages [19] -->
m

<!-- b006422 | furniture | pages [19] -->
m

<!-- b006423 | furniture | pages [19] -->
m

<!-- b006424 | furniture | pages [19] -->
m

<!-- b006425 | furniture | pages [19] -->
m

<!-- b006426 | furniture | pages [19] -->
m

<!-- b006427 | furniture | pages [19] -->
m

<!-- b006428 | furniture | pages [19] -->
m

<!-- b006429 | furniture | pages [19] -->
m

<!-- b006430 | furniture | pages [19] -->
m

<!-- b006431 | furniture | pages [19] -->
m

<!-- b006432 | furniture | pages [19] -->
m

<!-- b006433 | furniture | pages [19] -->
m

<!-- b006434 | furniture | pages [19] -->
m

<!-- b006435 | furniture | pages [19] -->
m

<!-- b006436 | furniture | pages [19] -->
m

<!-- b006437 | furniture | pages [19] -->
m

<!-- b006438 | furniture | pages [19] -->
m

<!-- b006439 | furniture | pages [19] -->
m

<!-- b006440 | furniture | pages [19] -->
m

<!-- b006441 | furniture | pages [19] -->
m

<!-- b006442 | furniture | pages [19] -->
m

<!-- b006443 | furniture | pages [19] -->
m

<!-- b006444 | furniture | pages [19] -->
m

<!-- b006445 | furniture | pages [19] -->
m

<!-- b006446 | furniture | pages [19] -->
m

<!-- b006447 | furniture | pages [19] -->
m

<!-- b006448 | furniture | pages [19] -->
m

<!-- b006449 | furniture | pages [19] -->
m

<!-- b006450 | furniture | pages [19] -->
m

<!-- b006451 | furniture | pages [19] -->
m

<!-- b006452 | furniture | pages [19] -->
m

<!-- b006453 | furniture | pages [19] -->
m

<!-- b006454 | furniture | pages [19] -->
m

<!-- b006455 | furniture | pages [19] -->
m

<!-- b006456 | furniture | pages [19] -->
m

<!-- b006457 | furniture | pages [19] -->
m

<!-- b006458 | furniture | pages [19] -->
m

<!-- b006459 | furniture | pages [19] -->
m

<!-- b006460 | furniture | pages [19] -->
m

<!-- b006461 | furniture | pages [19] -->
m

<!-- b006462 | furniture | pages [19] -->
m

<!-- b006463 | furniture | pages [19] -->
m

<!-- b006464 | furniture | pages [19] -->
m

<!-- b006465 | furniture | pages [19] -->
m

<!-- b006466 | furniture | pages [19] -->
m

<!-- b006467 | furniture | pages [19] -->
m

<!-- b006468 | furniture | pages [19] -->
m

<!-- b006469 | furniture | pages [19] -->
m

<!-- b006470 | furniture | pages [19] -->
m

<!-- b006471 | furniture | pages [19] -->
m

<!-- b006472 | furniture | pages [19] -->
m

<!-- b006473 | furniture | pages [19] -->
m

<!-- b006474 | furniture | pages [19] -->
m

<!-- b006475 | furniture | pages [19] -->
m

<!-- b006476 | furniture | pages [19] -->
m

<!-- b006477 | furniture | pages [19] -->
m

<!-- b006478 | furniture | pages [19] -->
m

<!-- b006479 | furniture | pages [19] -->
m

<!-- b006480 | furniture | pages [19] -->
m

<!-- b006481 | furniture | pages [19] -->
m

<!-- b006482 | furniture | pages [19] -->
m

<!-- b006483 | furniture | pages [19] -->
m

<!-- b006484 | furniture | pages [19] -->
m

<!-- b006485 | furniture | pages [19] -->
m

<!-- b006486 | furniture | pages [19] -->
m

<!-- b006487 | furniture | pages [19] -->
m

<!-- b006488 | furniture | pages [19] -->
m

<!-- b006489 | furniture | pages [19] -->
m

<!-- b006490 | furniture | pages [19] -->
m

<!-- b006491 | furniture | pages [19] -->
m

<!-- b006492 | furniture | pages [19] -->
m

<!-- b006493 | furniture | pages [19] -->
m

<!-- b006494 | furniture | pages [19] -->
m

<!-- b006495 | furniture | pages [19] -->
m

<!-- b006496 | furniture | pages [19] -->
m

<!-- b006497 | furniture | pages [19] -->
m

<!-- b006498 | furniture | pages [19] -->
m

<!-- b006499 | furniture | pages [19] -->
m

<!-- b006500 | furniture | pages [19] -->
m

<!-- b006501 | furniture | pages [19] -->
m

<!-- b006502 | furniture | pages [19] -->
m

<!-- b006503 | furniture | pages [19] -->
m

<!-- b006504 | furniture | pages [19] -->
m

<!-- b006505 | furniture | pages [19] -->
m

<!-- b006506 | furniture | pages [19] -->
m

<!-- b006507 | furniture | pages [19] -->
m

<!-- b006508 | furniture | pages [19] -->
m

<!-- b006509 | furniture | pages [19] -->
m

<!-- b006510 | furniture | pages [19] -->
m

<!-- b006511 | furniture | pages [19] -->
m

<!-- b006512 | furniture | pages [19] -->
m

<!-- b006513 | furniture | pages [19] -->
m

<!-- b006514 | furniture | pages [19] -->
m

<!-- b006515 | furniture | pages [19] -->
m

<!-- b006516 | furniture | pages [19] -->
m

<!-- b006517 | furniture | pages [19] -->
m

<!-- b006518 | furniture | pages [19] -->
m

<!-- b006519 | furniture | pages [19] -->
m

<!-- b006520 | furniture | pages [19] -->
m

<!-- b006521 | furniture | pages [19] -->
m

<!-- b006522 | furniture | pages [19] -->
m

<!-- b006523 | furniture | pages [19] -->
m

<!-- b006524 | furniture | pages [19] -->
m

<!-- b006525 | furniture | pages [19] -->
m

<!-- b006526 | furniture | pages [19] -->
m

<!-- b006527 | furniture | pages [19] -->
m

<!-- b006528 | furniture | pages [19] -->
m

<!-- b006529 | furniture | pages [19] -->
m

<!-- b006530 | furniture | pages [19] -->
m

<!-- b006531 | furniture | pages [19] -->
m

<!-- b006532 | furniture | pages [19] -->
m

<!-- b006533 | furniture | pages [19] -->
m

<!-- b006534 | furniture | pages [19] -->
m

<!-- b006535 | furniture | pages [19] -->
m

<!-- b006536 | furniture | pages [19] -->
m

<!-- b006537 | furniture | pages [19] -->
m

<!-- b006538 | furniture | pages [19] -->
m

<!-- b006539 | furniture | pages [19] -->
m

<!-- b006540 | furniture | pages [19] -->
m

<!-- b006541 | furniture | pages [19] -->
m

<!-- b006542 | furniture | pages [19] -->
m

<!-- b006543 | furniture | pages [19] -->
m

<!-- b006544 | furniture | pages [19] -->
m

<!-- b006545 | furniture | pages [19] -->
m

<!-- b006546 | furniture | pages [19] -->
m

<!-- b006547 | furniture | pages [19] -->
m

<!-- b006548 | furniture | pages [19] -->
m

<!-- b006549 | furniture | pages [19] -->
m

<!-- b006550 | furniture | pages [19] -->
m

<!-- b006551 | furniture | pages [19] -->
m

<!-- b006552 | furniture | pages [19] -->
m

<!-- b006553 | furniture | pages [19] -->
m

<!-- b006554 | furniture | pages [19] -->
m

<!-- b006555 | furniture | pages [19] -->
m

<!-- b006556 | furniture | pages [19] -->
m

<!-- b006557 | furniture | pages [19] -->
m

<!-- b006558 | furniture | pages [19] -->
m

<!-- b006559 | furniture | pages [19] -->
m

<!-- b006560 | furniture | pages [19] -->
m

<!-- b006561 | furniture | pages [19] -->
m

<!-- b006562 | furniture | pages [19] -->
m

<!-- b006563 | furniture | pages [19] -->
m

<!-- b006564 | furniture | pages [19] -->
m

<!-- b006565 | furniture | pages [19] -->
m

<!-- b006566 | furniture | pages [19] -->
m

<!-- b006567 | furniture | pages [19] -->
m

<!-- b006568 | furniture | pages [19] -->
m

<!-- b006569 | furniture | pages [19] -->
m

<!-- b006570 | furniture | pages [19] -->
m

<!-- b006571 | furniture | pages [19] -->
m

<!-- b006572 | furniture | pages [19] -->
m

<!-- b006573 | furniture | pages [19] -->
m

<!-- b006574 | furniture | pages [19] -->
m

<!-- b006575 | furniture | pages [19] -->
m

<!-- b006576 | furniture | pages [19] -->
m

<!-- b006577 | furniture | pages [19] -->
m

<!-- b006578 | furniture | pages [19] -->
m

<!-- b006579 | furniture | pages [19] -->
m

<!-- b006580 | furniture | pages [19] -->
m

<!-- b006581 | furniture | pages [19] -->
m

<!-- b006582 | furniture | pages [19] -->
m

<!-- b006583 | furniture | pages [19] -->
m

<!-- b006584 | furniture | pages [19] -->
m

<!-- b006585 | furniture | pages [19] -->
m

<!-- b006586 | furniture | pages [19] -->
m

<!-- b006587 | furniture | pages [19] -->
m

<!-- b006588 | furniture | pages [19] -->
m

<!-- b006589 | furniture | pages [19] -->
m

<!-- b006590 | furniture | pages [19] -->
m

<!-- b006591 | furniture | pages [20] -->
Team # 2521039

<!-- b006592 | furniture | pages [20] -->
Page 20 of 25

<!-- b006593 | prose | pages [20] -->
signiﬁcant factors associated with the distribution of cybercrime.

<!-- b006594 | prose | pages [20] -->
m

<!-- b006595 | prose | pages [20] -->
m

<!-- b006596 | prose | pages [20] -->
m

<!-- b006597 | prose | pages [20] -->
m

<!-- b006598 | prose | pages [20] -->
m

<!-- b006599 | prose | pages [20] -->
m

<!-- b006600 | prose | pages [20] -->
m

<!-- b006601 | prose | pages [20] -->
m

<!-- b006602 | prose | pages [20] -->
m

<!-- b006603 | prose | pages [20] -->
m

<!-- b006604 | prose | pages [20] -->
m

<!-- b006605 | prose | pages [20] -->
m

<!-- b006606 | prose | pages [20] -->
m

<!-- b006607 | prose | pages [20] -->
m

<!-- b006608 | prose | pages [20] -->
m

<!-- b006609 | prose | pages [20] -->
m

<!-- b006610 | prose | pages [20] -->
m

<!-- b006611 | prose | pages [20] -->
m

<!-- b006612 | prose | pages [20] -->
m

<!-- b006613 | prose | pages [20] -->
m

<!-- b006614 | prose | pages [20] -->
m

<!-- b006615 | prose | pages [20] -->
m

<!-- b006616 | prose | pages [20] -->
m

<!-- b006617 | prose | pages [20] -->
m

<!-- b006618 | prose | pages [20] -->
m

<!-- b006619 | prose | pages [20] -->
m

<!-- b006620 | prose | pages [20] -->
m

<!-- b006621 | prose | pages [20] -->
m

<!-- b006622 | prose | pages [20] -->
m

<!-- b006623 | prose | pages [20] -->
m

<!-- b006624 | prose | pages [20] -->
m

<!-- b006625 | prose | pages [20] -->
m

<!-- b006626 | prose | pages [20] -->
m

<!-- b006627 | prose | pages [20] -->
m

<!-- b006628 | prose | pages [20] -->
m

<!-- b006629 | prose | pages [20] -->
m

<!-- b006630 | prose | pages [20] -->
m

<!-- b006631 | prose | pages [20] -->
m

<!-- b006632 | prose | pages [20] -->
m

<!-- b006633 | prose | pages [20] -->
m

<!-- b006634 | prose | pages [20] -->
m

<!-- b006635 | prose | pages [20] -->
m

<!-- b006636 | prose | pages [20] -->
m

<!-- b006637 | prose | pages [20] -->
m

<!-- b006638 | prose | pages [20] -->
m

<!-- b006639 | prose | pages [20] -->
m

<!-- b006640 | prose | pages [20] -->
m

<!-- b006641 | prose | pages [20] -->
m

<!-- b006642 | prose | pages [20] -->
m

<!-- b006643 | prose | pages [20] -->
m

<!-- b006644 | prose | pages [20] -->
m

<!-- b006645 | prose | pages [20] -->
m

<!-- b006646 | prose | pages [20] -->
m

<!-- b006647 | prose | pages [20] -->
m

<!-- b006648 | prose | pages [20] -->
m

<!-- b006649 | prose | pages [20] -->
m

<!-- b006650 | prose | pages [20] -->
m

<!-- b006651 | prose | pages [20] -->
m

<!-- b006652 | prose | pages [20] -->
m

<!-- b006653 | prose | pages [20] -->
m

<!-- b006654 | prose | pages [20] -->
m

<!-- b006655 | prose | pages [20] -->
m

<!-- b006656 | prose | pages [20] -->
m

<!-- b006657 | prose | pages [20] -->
m

<!-- b006658 | prose | pages [20] -->
m

<!-- b006659 | prose | pages [20] -->
m

<!-- b006660 | prose | pages [20] -->
m

<!-- b006661 | prose | pages [20] -->
m

<!-- b006662 | prose | pages [20] -->
m

<!-- b006663 | prose | pages [20] -->
m

<!-- b006664 | prose | pages [20] -->
m

<!-- b006665 | prose | pages [20] -->
m

<!-- b006666 | prose | pages [20] -->
m

<!-- b006667 | prose | pages [20] -->
m

<!-- b006668 | prose | pages [20] -->
m

<!-- b006669 | prose | pages [20] -->
m

<!-- b006670 | prose | pages [20] -->
m

<!-- b006671 | prose | pages [20] -->
m

<!-- b006672 | prose | pages [20] -->
m

<!-- b006673 | prose | pages [20] -->
m

<!-- b006674 | prose | pages [20] -->
m

<!-- b006675 | prose | pages [20] -->
m

<!-- b006676 | prose | pages [20] -->
m

<!-- b006677 | prose | pages [20] -->
m

<!-- b006678 | prose | pages [20] -->
m

<!-- b006679 | prose | pages [20] -->
m

<!-- b006680 | prose | pages [20] -->
m

<!-- b006681 | prose | pages [20] -->
m

<!-- b006682 | prose | pages [20] -->
m

<!-- b006683 | prose | pages [20] -->
m

<!-- b006684 | prose | pages [20] -->
m

<!-- b006685 | prose | pages [20] -->
m

<!-- b006686 | prose | pages [20] -->
m

<!-- b006687 | prose | pages [20] -->
m

<!-- b006688 | prose | pages [20] -->
m

<!-- b006689 | prose | pages [20] -->
m

<!-- b006690 | prose | pages [20] -->
m

<!-- b006691 | prose | pages [20] -->
m

<!-- b006692 | prose | pages [20] -->
m

<!-- b006693 | prose | pages [20] -->
m

<!-- b006694 | prose | pages [20] -->
m

<!-- b006695 | prose | pages [20] -->
m

<!-- b006696 | prose | pages [20] -->
m

<!-- b006697 | prose | pages [20] -->
m

<!-- b006698 | prose | pages [20] -->
m

<!-- b006699 | prose | pages [20] -->
m

<!-- b006700 | prose | pages [20] -->
m

<!-- b006701 | prose | pages [20] -->
m

<!-- b006702 | prose | pages [20] -->
m

<!-- b006703 | prose | pages [20] -->
m

<!-- b006704 | prose | pages [20] -->
m

<!-- b006705 | prose | pages [20] -->
m

<!-- b006706 | prose | pages [20] -->
m

<!-- b006707 | prose | pages [20] -->
m

<!-- b006708 | prose | pages [20] -->
m

<!-- b006709 | prose | pages [20] -->
m

<!-- b006710 | prose | pages [20] -->
m

<!-- b006711 | prose | pages [20] -->
m

<!-- b006712 | prose | pages [20] -->
m

<!-- b006713 | prose | pages [20] -->
m

<!-- b006714 | prose | pages [20] -->
m

<!-- b006715 | prose | pages [20] -->
m

<!-- b006716 | prose | pages [20] -->
m

<!-- b006717 | prose | pages [20] -->
m

<!-- b006718 | prose | pages [20] -->
m

<!-- b006719 | prose | pages [20] -->
m

<!-- b006720 | prose | pages [20] -->
m

<!-- b006721 | prose | pages [20] -->
m

<!-- b006722 | prose | pages [20] -->
m

<!-- b006723 | prose | pages [20] -->
m

<!-- b006724 | prose | pages [20] -->
m

<!-- b006725 | prose | pages [20] -->
m

<!-- b006726 | prose | pages [20] -->
m

<!-- b006727 | prose | pages [20] -->
m

<!-- b006728 | prose | pages [20] -->
m

<!-- b006729 | prose | pages [20] -->
m

<!-- b006730 | prose | pages [20] -->
m

<!-- b006731 | prose | pages [20] -->
m

<!-- b006732 | prose | pages [20] -->
m

<!-- b006733 | prose | pages [20] -->
m

<!-- b006734 | prose | pages [20] -->
m

<!-- b006735 | prose | pages [20] -->
m

<!-- b006736 | prose | pages [20] -->
m

<!-- b006737 | prose | pages [20] -->
m

<!-- b006738 | prose | pages [20] -->
m

<!-- b006739 | prose | pages [20] -->
m

<!-- b006740 | prose | pages [20] -->
m

<!-- b006741 | prose | pages [20] -->
m

<!-- b006742 | prose | pages [20] -->
m

<!-- b006743 | prose | pages [20] -->
m

<!-- b006744 | prose | pages [20] -->
m

<!-- b006745 | prose | pages [20] -->
m

<!-- b006746 | prose | pages [20] -->
m

<!-- b006747 | prose | pages [20] -->
m

<!-- b006748 | prose | pages [20] -->
m

<!-- b006749 | prose | pages [20] -->
m

<!-- b006750 | prose | pages [20] -->
m

<!-- b006751 | prose | pages [20] -->
m

<!-- b006752 | prose | pages [20] -->
m

<!-- b006753 | prose | pages [20] -->
m

<!-- b006754 | prose | pages [20] -->
m

<!-- b006755 | prose | pages [20] -->
m

<!-- b006756 | prose | pages [20] -->
m

<!-- b006757 | prose | pages [20] -->
m

<!-- b006758 | prose | pages [20] -->
m

<!-- b006759 | prose | pages [20] -->
m

<!-- b006760 | prose | pages [20] -->
m

<!-- b006761 | prose | pages [20] -->
m

<!-- b006762 | prose | pages [20] -->
m

<!-- b006763 | prose | pages [20] -->
m

<!-- b006764 | prose | pages [20] -->
m

<!-- b006765 | prose | pages [20] -->
m

<!-- b006766 | prose | pages [20] -->
m

<!-- b006767 | prose | pages [20] -->
m

<!-- b006768 | prose | pages [20] -->
m

<!-- b006769 | prose | pages [20] -->
m

<!-- b006770 | prose | pages [20] -->
m

<!-- b006771 | prose | pages [20] -->
m

<!-- b006772 | prose | pages [20] -->
m

<!-- b006773 | prose | pages [20] -->
m

<!-- b006774 | prose | pages [20] -->
m

<!-- b006775 | prose | pages [20] -->
m

<!-- b006776 | prose | pages [20] -->
m

<!-- b006777 | prose | pages [20] -->
m

<!-- b006778 | prose | pages [20] -->
m

<!-- b006779 | prose | pages [20] -->
m

<!-- b006780 | prose | pages [20] -->
m

<!-- b006781 | prose | pages [20] -->
m

<!-- b006782 | prose | pages [20] -->
m

<!-- b006783 | prose | pages [20] -->
m

<!-- b006784 | prose | pages [20] -->
m

<!-- b006785 | prose | pages [20] -->
m

<!-- b006786 | prose | pages [20] -->
m

<!-- b006787 | prose | pages [20] -->
m

<!-- b006788 | prose | pages [20] -->
m

<!-- b006789 | prose | pages [20] -->
m

<!-- b006790 | prose | pages [20] -->
m

<!-- b006791 | prose | pages [20] -->
m

<!-- b006792 | prose | pages [20] -->
m

<!-- b006793 | prose | pages [20] -->
m

<!-- b006794 | prose | pages [20] -->
m

<!-- b006795 | prose | pages [20] -->
m

<!-- b006796 | prose | pages [20] -->
m

<!-- b006797 | prose | pages [20] -->
m

<!-- b006798 | prose | pages [20] -->
m

<!-- b006799 | prose | pages [20] -->
m

<!-- b006800 | prose | pages [20] -->
m

<!-- b006801 | prose | pages [20] -->
m

<!-- b006802 | prose | pages [20] -->
m

<!-- b006803 | prose | pages [20] -->
m

<!-- b006804 | prose | pages [20] -->
m

<!-- b006805 | prose | pages [20] -->
m

<!-- b006806 | prose | pages [20] -->
m

<!-- b006807 | prose | pages [20] -->
m

<!-- b006808 | prose | pages [20] -->
m

<!-- b006809 | prose | pages [20] -->
m

<!-- b006810 | prose | pages [20] -->
m

<!-- b006811 | prose | pages [20] -->
m

<!-- b006812 | prose | pages [20] -->
m

<!-- b006813 | prose | pages [20] -->
m

<!-- b006814 | prose | pages [20] -->
m

<!-- b006815 | prose | pages [20] -->
m

<!-- b006816 | prose | pages [20] -->
m

<!-- b006817 | prose | pages [20] -->
m

<!-- b006818 | prose | pages [20] -->
m

<!-- b006819 | prose | pages [20] -->
m

<!-- b006820 | prose | pages [20] -->
m

<!-- b006821 | prose | pages [20] -->
m

<!-- b006822 | prose | pages [20] -->
m

<!-- b006823 | prose | pages [20] -->
m

<!-- b006824 | prose | pages [20] -->
m

<!-- b006825 | prose | pages [20] -->
m

<!-- b006826 | prose | pages [20] -->
m

<!-- b006827 | prose | pages [20] -->
m

<!-- b006828 | prose | pages [20] -->
m

<!-- b006829 | prose | pages [20] -->
m

<!-- b006830 | prose | pages [20] -->
m

<!-- b006831 | prose | pages [20] -->
m

<!-- b006832 | prose | pages [20] -->
m

<!-- b006833 | prose | pages [20] -->
m

<!-- b006834 | prose | pages [20] -->
m

<!-- b006835 | prose | pages [20] -->
m

<!-- b006836 | prose | pages [20] -->
m

<!-- b006837 | prose | pages [20] -->
m

<!-- b006838 | prose | pages [20] -->
m

<!-- b006839 | prose | pages [20] -->
m

<!-- b006840 | prose | pages [20] -->
m

<!-- b006841 | prose | pages [20] -->
m

<!-- b006842 | prose | pages [20] -->
m

<!-- b006843 | prose | pages [20] -->
m

<!-- b006844 | prose | pages [20] -->
m

<!-- b006845 | prose | pages [20] -->
m

<!-- b006846 | prose | pages [20] -->
m

<!-- b006847 | prose | pages [20] -->
m

<!-- b006848 | prose | pages [20] -->
m

<!-- b006849 | prose | pages [20] -->
m

<!-- b006850 | prose | pages [20] -->
m

<!-- b006851 | prose | pages [20] -->
m

<!-- b006852 | prose | pages [20] -->
m

<!-- b006853 | prose | pages [20] -->
m

<!-- b006854 | prose | pages [20] -->
m

<!-- b006855 | prose | pages [20] -->
m

<!-- b006856 | prose | pages [20] -->
m

<!-- b006857 | prose | pages [20] -->
m

<!-- b006858 | prose | pages [20] -->
m

<!-- b006859 | prose | pages [20] -->
m

<!-- b006860 | prose | pages [20] -->
m

<!-- b006861 | prose | pages [20] -->
m

<!-- b006862 | prose | pages [20] -->
m

<!-- b006863 | prose | pages [20] -->
m

<!-- b006864 | prose | pages [20] -->
m

<!-- b006865 | prose | pages [20] -->
m

<!-- b006866 | prose | pages [20] -->
m

<!-- b006867 | prose | pages [20] -->
m

<!-- b006868 | prose | pages [20] -->
m

<!-- b006869 | prose | pages [20] -->
m

<!-- b006870 | prose | pages [20] -->
m

<!-- b006871 | prose | pages [20] -->
m

<!-- b006872 | prose | pages [20] -->
m

<!-- b006873 | prose | pages [20] -->
m

<!-- b006874 | prose | pages [20] -->
m

<!-- b006875 | prose | pages [20] -->
m

<!-- b006876 | prose | pages [20] -->
m

<!-- b006877 | prose | pages [20] -->
m

<!-- b006878 | prose | pages [20] -->
m

<!-- b006879 | prose | pages [20] -->
m

<!-- b006880 | prose | pages [20] -->
m

<!-- b006881 | prose | pages [20] -->
m

<!-- b006882 | prose | pages [20] -->
m

<!-- b006883 | prose | pages [20] -->
m

<!-- b006884 | prose | pages [20] -->
m

<!-- b006885 | prose | pages [20] -->
m

<!-- b006886 | prose | pages [20] -->
m

<!-- b006887 | prose | pages [20] -->
m

<!-- b006888 | prose | pages [20] -->
m

<!-- b006889 | prose | pages [20] -->
m

<!-- b006890 | prose | pages [20] -->
m

<!-- b006891 | prose | pages [20] -->
m

<!-- b006892 | prose | pages [20] -->
m

<!-- b006893 | prose | pages [20] -->
m

<!-- b006894 | prose | pages [20] -->
m

<!-- b006895 | prose | pages [20] -->
m

<!-- b006896 | prose | pages [20] -->
m

<!-- b006897 | prose | pages [20] -->
m

<!-- b006898 | prose | pages [20] -->
m

<!-- b006899 | prose | pages [20] -->
m

<!-- b006900 | prose | pages [20] -->
m

<!-- b006901 | prose | pages [20] -->
m

<!-- b006902 | prose | pages [20] -->
m

<!-- b006903 | prose | pages [20] -->
m

<!-- b006904 | prose | pages [20] -->
m

<!-- b006905 | prose | pages [20] -->
m

<!-- b006906 | prose | pages [20] -->
m

<!-- b006907 | prose | pages [20] -->
m

<!-- b006908 | prose | pages [20] -->
m

<!-- b006909 | prose | pages [20] -->
m

<!-- b006910 | prose | pages [20] -->
m

<!-- b006911 | prose | pages [20] -->
m

<!-- b006912 | prose | pages [20] -->
m

<!-- b006913 | prose | pages [20] -->
m

<!-- b006914 | prose | pages [20] -->
m

<!-- b006915 | prose | pages [20] -->
m

<!-- b006916 | prose | pages [20] -->
m

<!-- b006917 | prose | pages [20] -->
m

<!-- b006918 | prose | pages [20] -->
m

<!-- b006919 | prose | pages [20] -->
m

<!-- b006920 | prose | pages [20] -->
m

<!-- b006921 | prose | pages [20] -->
m

<!-- b006922 | prose | pages [20] -->
m

<!-- b006923 | prose | pages [20] -->
m

<!-- b006924 | prose | pages [20] -->
m

<!-- b006925 | prose | pages [20] -->
m

<!-- b006926 | prose | pages [20] -->
m

<!-- b006927 | prose | pages [20] -->
m

<!-- b006928 | prose | pages [20] -->
m

<!-- b006929 | prose | pages [20] -->
m

<!-- b006930 | prose | pages [20] -->
m

<!-- b006931 | prose | pages [20] -->
m

<!-- b006932 | prose | pages [20] -->
m

<!-- b006933 | prose | pages [20] -->
m

<!-- b006934 | prose | pages [20] -->
m

<!-- b006935 | prose | pages [20] -->
m

<!-- b006936 | prose | pages [20] -->
m

<!-- b006937 | prose | pages [20] -->
m

<!-- b006938 | prose | pages [20] -->
m

<!-- b006939 | prose | pages [20] -->
m

<!-- b006940 | prose | pages [20] -->
m

<!-- b006941 | prose | pages [20] -->
m

<!-- b006942 | prose | pages [20] -->
m

<!-- b006943 | prose | pages [20] -->
m

<!-- b006944 | prose | pages [20] -->
m

<!-- b006945 | prose | pages [20] -->
m

<!-- b006946 | prose | pages [20] -->
m

<!-- b006947 | prose | pages [20] -->
m

<!-- b006948 | prose | pages [20] -->
m

<!-- b006949 | prose | pages [20] -->
m

<!-- b006950 | prose | pages [20] -->
m

<!-- b006951 | prose | pages [20] -->
m

<!-- b006952 | prose | pages [20] -->
m

<!-- b006953 | prose | pages [20] -->
m

<!-- b006954 | prose | pages [20] -->
m

<!-- b006955 | prose | pages [20] -->
m

<!-- b006956 | prose | pages [20] -->
m

<!-- b006957 | prose | pages [20] -->
m

<!-- b006958 | prose | pages [20] -->
m

<!-- b006959 | prose | pages [20] -->
m

<!-- b006960 | prose | pages [20] -->
m

<!-- b006961 | prose | pages [20] -->
m

<!-- b006962 | prose | pages [20] -->
m

<!-- b006963 | prose | pages [20] -->
m

<!-- b006964 | prose | pages [20] -->
m

<!-- b006965 | prose | pages [20] -->
m

<!-- b006966 | prose | pages [20] -->
m

<!-- b006967 | prose | pages [20] -->
m

<!-- b006968 | prose | pages [20] -->
m

<!-- b006969 | prose | pages [20] -->
m

<!-- b006970 | prose | pages [20] -->
m

<!-- b006971 | prose | pages [20] -->
m

<!-- b006972 | prose | pages [20] -->
m

<!-- b006973 | prose | pages [20] -->
m

<!-- b006974 | prose | pages [20] -->
m

<!-- b006975 | prose | pages [20] -->
m

<!-- b006976 | prose | pages [20] -->
m

<!-- b006977 | prose | pages [20] -->
m

<!-- b006978 | prose | pages [20] -->
m

<!-- b006979 | prose | pages [20] -->
m

<!-- b006980 | prose | pages [20] -->
m

<!-- b006981 | prose | pages [20] -->
m

<!-- b006982 | prose | pages [20] -->
m

<!-- b006983 | prose | pages [20] -->
m

<!-- b006984 | prose | pages [20] -->
m

<!-- b006985 | prose | pages [20] -->
m

<!-- b006986 | prose | pages [20] -->
m

<!-- b006987 | prose | pages [20] -->
m

<!-- b006988 | prose | pages [20] -->
m

<!-- b006989 | prose | pages [20] -->
m

<!-- b006990 | prose | pages [20] -->
m

<!-- b006991 | prose | pages [20] -->
m

<!-- b006992 | prose | pages [20] -->
m

<!-- b006993 | prose | pages [20] -->
m

<!-- b006994 | prose | pages [20] -->
m

<!-- b006995 | prose | pages [20] -->
m

<!-- b006996 | prose | pages [20] -->
m

<!-- b006997 | prose | pages [20] -->
m

<!-- b006998 | prose | pages [20] -->
m

<!-- b006999 | prose | pages [20] -->
m

<!-- b007000 | prose | pages [20] -->
m

<!-- b007001 | prose | pages [20] -->
m

<!-- b007002 | prose | pages [20] -->
m

<!-- b007003 | prose | pages [20] -->
m

<!-- b007004 | prose | pages [20] -->
m

<!-- b007005 | prose | pages [20] -->
m

<!-- b007006 | prose | pages [20] -->
m

<!-- b007007 | prose | pages [20] -->
m

<!-- b007008 | prose | pages [20] -->
m

<!-- b007009 | prose | pages [20] -->
m

<!-- b007010 | prose | pages [20] -->
m

<!-- b007011 | prose | pages [20] -->
m

<!-- b007012 | prose | pages [20] -->
m

<!-- b007013 | prose | pages [20] -->
m

<!-- b007014 | prose | pages [20] -->
m

<!-- b007015 | prose | pages [20] -->
m

<!-- b007016 | prose | pages [20] -->
m

<!-- b007017 | prose | pages [20] -->
m

<!-- b007018 | prose | pages [20] -->
m

<!-- b007019 | prose | pages [20] -->
m

<!-- b007020 | prose | pages [20] -->
m

<!-- b007021 | prose | pages [20] -->
m

<!-- b007022 | prose | pages [20] -->
m

<!-- b007023 | prose | pages [20] -->
m

<!-- b007024 | prose | pages [20] -->
m

<!-- b007025 | prose | pages [20] -->
m

<!-- b007026 | prose | pages [20] -->
m

<!-- b007027 | prose | pages [20] -->
m

<!-- b007028 | prose | pages [20] -->
m

<!-- b007029 | prose | pages [20] -->
m

<!-- b007030 | prose | pages [20] -->
m

<!-- b007031 | prose | pages [20] -->
m

<!-- b007032 | prose | pages [20] -->
m

<!-- b007033 | prose | pages [20] -->
m

<!-- b007034 | prose | pages [20] -->
m

<!-- b007035 | prose | pages [20] -->
m

<!-- b007036 | prose | pages [20] -->
m

<!-- b007037 | prose | pages [20] -->
m

<!-- b007038 | prose | pages [20] -->
m

<!-- b007039 | prose | pages [20] -->
m

<!-- b007040 | prose | pages [20] -->
m

<!-- b007041 | prose | pages [20] -->
m

<!-- b007042 | prose | pages [20] -->
m

<!-- b007043 | prose | pages [20] -->
m

<!-- b007044 | prose | pages [20] -->
m

<!-- b007045 | prose | pages [20] -->
m

<!-- b007046 | prose | pages [20] -->
m

<!-- b007047 | prose | pages [20] -->
m

<!-- b007048 | prose | pages [20] -->
m

<!-- b007049 | prose | pages [20] -->
m

<!-- b007050 | prose | pages [20] -->
m

<!-- b007051 | prose | pages [20] -->
m

<!-- b007052 | prose | pages [20] -->
m

<!-- b007053 | prose | pages [20] -->
m

<!-- b007054 | prose | pages [20] -->
m

<!-- b007055 | prose | pages [20] -->
m

<!-- b007056 | prose | pages [20] -->
m

<!-- b007057 | prose | pages [20] -->
m

<!-- b007058 | prose | pages [20] -->
m

<!-- b007059 | prose | pages [20] -->
m

<!-- b007060 | prose | pages [20] -->
m

<!-- b007061 | prose | pages [20] -->
m

<!-- b007062 | prose | pages [20] -->
m

<!-- b007063 | prose | pages [20] -->
m

<!-- b007064 | prose | pages [20] -->
m

<!-- b007065 | prose | pages [20] -->
m

<!-- b007066 | prose | pages [20] -->
m

<!-- b007067 | prose | pages [20] -->
m

<!-- b007068 | prose | pages [20] -->
m

<!-- b007069 | prose | pages [20] -->
m

<!-- b007070 | prose | pages [20] -->
m

<!-- b007071 | prose | pages [20] -->
m

<!-- b007072 | prose | pages [20] -->
m

<!-- b007073 | prose | pages [20] -->
m

<!-- b007074 | prose | pages [20] -->
m

<!-- b007075 | prose | pages [20] -->
m

<!-- b007076 | prose | pages [20] -->
m

<!-- b007077 | prose | pages [20] -->
m

<!-- b007078 | prose | pages [20] -->
m

<!-- b007079 | prose | pages [20] -->
m

<!-- b007080 | prose | pages [20] -->
m

<!-- b007081 | prose | pages [20] -->
m

<!-- b007082 | prose | pages [20] -->
m

<!-- b007083 | prose | pages [20] -->
m

<!-- b007084 | prose | pages [20] -->
m

<!-- b007085 | prose | pages [20] -->
m

<!-- b007086 | prose | pages [20] -->
m

<!-- b007087 | prose | pages [20] -->
m

<!-- b007088 | prose | pages [20] -->
m

<!-- b007089 | prose | pages [20] -->
m

<!-- b007090 | prose | pages [20] -->
m

<!-- b007091 | prose | pages [20] -->
m

<!-- b007092 | prose | pages [20] -->
m

<!-- b007093 | prose | pages [20] -->
m

<!-- b007094 | prose | pages [20] -->
m

<!-- b007095 | prose | pages [20] -->
m

<!-- b007096 | prose | pages [20] -->
m

<!-- b007097 | prose | pages [20] -->
m

<!-- b007098 | prose | pages [20] -->
m

<!-- b007099 | prose | pages [20] -->
m

<!-- b007100 | prose | pages [20] -->
m

<!-- b007101 | prose | pages [20] -->
m

<!-- b007102 | prose | pages [20] -->
m

<!-- b007103 | prose | pages [20] -->
m

<!-- b007104 | prose | pages [20] -->
m

<!-- b007105 | prose | pages [20] -->
m

<!-- b007106 | prose | pages [20] -->
m

<!-- b007107 | prose | pages [20] -->
m

<!-- b007108 | prose | pages [20] -->
m

<!-- b007109 | prose | pages [20] -->
m

<!-- b007110 | prose | pages [20] -->
m

<!-- b007111 | prose | pages [20] -->
m

<!-- b007112 | prose | pages [20] -->
m

<!-- b007113 | prose | pages [20] -->
m

<!-- b007114 | prose | pages [20] -->
m

<!-- b007115 | prose | pages [20] -->
m

<!-- b007116 | prose | pages [20] -->
m

<!-- b007117 | prose | pages [20] -->
m

<!-- b007118 | prose | pages [20] -->
m

<!-- b007119 | prose | pages [20] -->
m

<!-- b007120 | prose | pages [20] -->
m

<!-- b007121 | prose | pages [20] -->
m

<!-- b007122 | prose | pages [20] -->
m

<!-- b007123 | prose | pages [20] -->
m

<!-- b007124 | prose | pages [20] -->
m

<!-- b007125 | prose | pages [20] -->
m

<!-- b007126 | prose | pages [20] -->
m

<!-- b007127 | prose | pages [20] -->
m

<!-- b007128 | prose | pages [20] -->
m

<!-- b007129 | prose | pages [20] -->
m

<!-- b007130 | prose | pages [20] -->
m

<!-- b007131 | prose | pages [20] -->
m

<!-- b007132 | prose | pages [20] -->
m

<!-- b007133 | prose | pages [20] -->
m

<!-- b007134 | prose | pages [20] -->
m

<!-- b007135 | prose | pages [20] -->
m

<!-- b007136 | prose | pages [20] -->
m

<!-- b007137 | prose | pages [20] -->
m

<!-- b007138 | prose | pages [20] -->
m

<!-- b007139 | prose | pages [20] -->
m

<!-- b007140 | prose | pages [20] -->
m

<!-- b007141 | prose | pages [20] -->
m

<!-- b007142 | prose | pages [20] -->
m

<!-- b007143 | prose | pages [20] -->
m

<!-- b007144 | prose | pages [20] -->
m

<!-- b007145 | prose | pages [20] -->
m

<!-- b007146 | prose | pages [20] -->
m

<!-- b007147 | prose | pages [20] -->
m

<!-- b007148 | prose | pages [20] -->
m

<!-- b007149 | prose | pages [20] -->
m

<!-- b007150 | prose | pages [20] -->
m

<!-- b007151 | prose | pages [20] -->
m

<!-- b007152 | prose | pages [20] -->
m

<!-- b007153 | prose | pages [20] -->
m

<!-- b007154 | prose | pages [20] -->
m

<!-- b007155 | prose | pages [20] -->
m

<!-- b007156 | prose | pages [20] -->
m

<!-- b007157 | prose | pages [20] -->
m

<!-- b007158 | prose | pages [20] -->
m

<!-- b007159 | prose | pages [20] -->
m

<!-- b007160 | prose | pages [20] -->
m

<!-- b007161 | prose | pages [20] -->
m

<!-- b007162 | prose | pages [20] -->
m

<!-- b007163 | prose | pages [20] -->
m

<!-- b007164 | prose | pages [20] -->
m

<!-- b007165 | prose | pages [20] -->
m

<!-- b007166 | prose | pages [20] -->
m

<!-- b007167 | prose | pages [20] -->
m

<!-- b007168 | prose | pages [20] -->
m

<!-- b007169 | prose | pages [20] -->
m

<!-- b007170 | prose | pages [20] -->
m

<!-- b007171 | prose | pages [20] -->
m

<!-- b007172 | prose | pages [20] -->
m

<!-- b007173 | prose | pages [20] -->
m

<!-- b007174 | prose | pages [20] -->
m

<!-- b007175 | prose | pages [20] -->
m

<!-- b007176 | prose | pages [20] -->
m

<!-- b007177 | prose | pages [20] -->
m

<!-- b007178 | prose | pages [20] -->
m

<!-- b007179 | prose | pages [20] -->
m

<!-- b007180 | prose | pages [20] -->
m

<!-- b007181 | prose | pages [20] -->
m

<!-- b007182 | prose | pages [20] -->
m

<!-- b007183 | prose | pages [20] -->
m

<!-- b007184 | prose | pages [20] -->
m

<!-- b007185 | prose | pages [20] -->
m

<!-- b007186 | prose | pages [20] -->
m

<!-- b007187 | prose | pages [20] -->
m

<!-- b007188 | prose | pages [20] -->
m

<!-- b007189 | prose | pages [20] -->
m

<!-- b007190 | prose | pages [20] -->
m

<!-- b007191 | prose | pages [20] -->
m

<!-- b007192 | prose | pages [20] -->
m

<!-- b007193 | prose | pages [20] -->
m

<!-- b007194 | prose | pages [20] -->
m

<!-- b007195 | prose | pages [20] -->
m

<!-- b007196 | prose | pages [20] -->
m

<!-- b007197 | prose | pages [20] -->
m

<!-- b007198 | prose | pages [20] -->
m

<!-- b007199 | prose | pages [20] -->
m

<!-- b007200 | prose | pages [20] -->
m

<!-- b007201 | prose | pages [20] -->
m

<!-- b007202 | prose | pages [20] -->
m

<!-- b007203 | prose | pages [20] -->
m

<!-- b007204 | prose | pages [20] -->
m

<!-- b007205 | prose | pages [20] -->
m

<!-- b007206 | prose | pages [20] -->
m

<!-- b007207 | prose | pages [20] -->
m

<!-- b007208 | prose | pages [20] -->
m

<!-- b007209 | prose | pages [20] -->
m

<!-- b007210 | prose | pages [20] -->
m

<!-- b007211 | prose | pages [20] -->
m

<!-- b007212 | prose | pages [20] -->
m

<!-- b007213 | prose | pages [20] -->
m

<!-- b007214 | prose | pages [20] -->
m

<!-- b007215 | prose | pages [20] -->
m

<!-- b007216 | prose | pages [20] -->
m

<!-- b007217 | prose | pages [20] -->
m

<!-- b007218 | prose | pages [20] -->
m

<!-- b007219 | prose | pages [20] -->
m

<!-- b007220 | prose | pages [20] -->
m

<!-- b007221 | prose | pages [20] -->
m

<!-- b007222 | prose | pages [20] -->
m

<!-- b007223 | prose | pages [20] -->
m

<!-- b007224 | prose | pages [20] -->
m

<!-- b007225 | prose | pages [20] -->
m

<!-- b007226 | prose | pages [20] -->
m

<!-- b007227 | prose | pages [20] -->
m

<!-- b007228 | prose | pages [20] -->
m

<!-- b007229 | prose | pages [20] -->
m

<!-- b007230 | prose | pages [20] -->
m

<!-- b007231 | prose | pages [20] -->
m

<!-- b007232 | prose | pages [20] -->
m

<!-- b007233 | prose | pages [20] -->
m

<!-- b007234 | prose | pages [20] -->
m

<!-- b007235 | prose | pages [20] -->
m

<!-- b007236 | prose | pages [20] -->
m

<!-- b007237 | prose | pages [20] -->
m

<!-- b007238 | prose | pages [20] -->
m

<!-- b007239 | prose | pages [20] -->
m

<!-- b007240 | prose | pages [20] -->
m

<!-- b007241 | prose | pages [20] -->
m

<!-- b007242 | prose | pages [20] -->
m

<!-- b007243 | prose | pages [20] -->
m

<!-- b007244 | prose | pages [20] -->
m

<!-- b007245 | prose | pages [20] -->
m

<!-- b007246 | prose | pages [20] -->
m

<!-- b007247 | prose | pages [20] -->
m

<!-- b007248 | prose | pages [20] -->
m

<!-- b007249 | prose | pages [20] -->
m

<!-- b007250 | prose | pages [20] -->
m

<!-- b007251 | prose | pages [20] -->
m

<!-- b007252 | prose | pages [20] -->
m

<!-- b007253 | prose | pages [20] -->
m

<!-- b007254 | prose | pages [20] -->
m

<!-- b007255 | prose | pages [20] -->
m

<!-- b007256 | prose | pages [20] -->
m

<!-- b007257 | prose | pages [20] -->
m

<!-- b007258 | prose | pages [20] -->
m

<!-- b007259 | prose | pages [20] -->
m

<!-- b007260 | prose | pages [20] -->
m

<!-- b007261 | prose | pages [20] -->
m

<!-- b007262 | prose | pages [20] -->
m

<!-- b007263 | prose | pages [20] -->
m

<!-- b007264 | prose | pages [20] -->
m

<!-- b007265 | prose | pages [20] -->
m

<!-- b007266 | prose | pages [20] -->
m

<!-- b007267 | prose | pages [20] -->
m

<!-- b007268 | prose | pages [20] -->
m

<!-- b007269 | prose | pages [20] -->
m

<!-- b007270 | prose | pages [20] -->
m

<!-- b007271 | prose | pages [20] -->
m

<!-- b007272 | prose | pages [20] -->
m

<!-- b007273 | prose | pages [20] -->
m

<!-- b007274 | prose | pages [20] -->
m

<!-- b007275 | prose | pages [20] -->
m

<!-- b007276 | prose | pages [20] -->
m

<!-- b007277 | prose | pages [20] -->
m

<!-- b007278 | prose | pages [20] -->
m

<!-- b007279 | prose | pages [20] -->
m

<!-- b007280 | prose | pages [20] -->
m

<!-- b007281 | caption | pages [20] -->
Figure 15: Spearman Correlation Heatmap

<!-- b007282 | heading | pages [20] -->
Model2: Log-Enhanced Quadratic Regression Model(LEQR)

<!-- b007283 | prose | pages [20] -->
6.2

<!-- b007284 | prose | pages [20] -->
Based on the above correlation analysis and the distribution characteristics analysis observed in the scatter plots, a multiple linear regression model was constructed to investigate the mechanisms through which GDP, ICT Goods Export, and Population inﬂuence the target variable, Target Count.

<!-- b007285 | prose | pages [20] -->
To reduce data volatility and enhance the linear stability of the model, logarithmic transformations were applied to the three independent variables. Additionally, miss- ing values and outliers in the dataset were removed, and all independent variables were standardized to prevent differences in variable scales from affecting the interpre- tation of regression coefﬁcients.

<!-- b007286 | prose | pages [20] -->
At the basic model stage, the following linear regression model was constructed:

<!-- b007287 | prose | pages [20] -->
Y = α0 + α1 · X1 + α2 · X2 + α3 · X3

<!-- b007288 | prose | pages [20] -->
The model aims to capture the linear relationship between the target variable and the independent variables. Through model evaluation, metrics such as R2, adjusted R2, and the signiﬁcance of regression coefﬁcients (p-values) were analyzed. The low R2

<!-- b007289 | prose | pages [20] -->
value in the basic model may suggest a more complex relationship between the target variable and the independent variables. To further improve the model, a nonlinear

<!-- b007290 | prose | pages [20] -->
3 (the squared term of Log_GDP) was introduced, resulting in the construction

<!-- b007291 | prose | pages [20] -->
term X2

<!-- b007292 | prose | pages [20] -->
of the improved model:

<!-- b007293 | prose | pages [20] -->
Y = α0 + α1 · X1 + α2 · X2 + α3 · X3 + α4 · X2

<!-- b007294 | prose | pages [20] -->
3

<!-- b007295 | prose | pages [20] -->
By comparing the R2, adjusted R2, AIC, and BIC metrics between the basic model and the improved model, it was found that the introduction of the nonlinear term sig- niﬁcantly enhanced the explanatory power of the model. Additionally, the regression coefﬁcient of the nonlinear term was signiﬁcant (p-value < 0.05), conﬁrming its effect on the target variable. This indicates that the improved model is better equipped to

<!-- b007296 | prose | pages [20] -->
关注数学模型

<!-- b007297 | prose | pages [20] -->
capture the complex relationships between variables.

<!-- b007298 | furniture | pages [20] -->
2

<!-- b007299 | furniture | pages [20] -->
MATHmodels

<!-- b007300 | furniture | pages [20] -->
获取更多资讯

<!-- b007301 | furniture | pages [21] -->
Team # 2521039

<!-- b007302 | furniture | pages [21] -->
Page 21 of 25

<!-- b007303 | prose | pages [21] -->
After solving for the coefﬁcients and substituting their values into the model, the

<!-- b007304 | heading | pages [21] -->
Log-Enhanced Quadratic Regression Model was established. By plotting scatter dia-

<!-- b007305 | prose | pages [21] -->
grams and ideal reference lines, the consistency between predicted and actual values, as well as the distribution of deviations, was visually evaluated as shown below:

<!-- b007306 | prose | pages [21] -->
Y = 26.3796 −13.2802 · X1 −15.4265 · X2 −500.2947 · X3 + 551.1509 · X2

<!-- b007307 | prose | pages [21] -->
微信公众号：数学模型

<!-- b007308 | prose | pages [21] -->
3

<!-- b007309 | prose | pages [21] -->
微信号：MATHmodels

<!-- b007310 | caption | pages [21] -->
Figure 16: Actual vs Predicted Target Count

<!-- b007311 | prose | pages [21] -->
In addition, three curve plots were created to illustrate the inﬂuence trends of GDP, ICT Goods Export, and Population on Target Count while holding other variables at their mean values. These plots visualize the nonlinear relationships between these variables and the target variable.

<!-- b007312 | caption | pages [21] -->
Figure 17: Curves predicting crime counts based on factor variations

<!-- b007313 | prose | pages [21] -->
6.3

<!-- b007314 | heading | pages [21] -->
Results Interpretation

<!-- b007315 | prose | pages [21] -->
The nonlinear relationships in the plots indicate that GDP has a signiﬁcant positive impact on the number of cybercrime targets, while ICT Goods Export and Population are negatively correlated with target counts. This relationship arises because the log- arithmic squared term of GDP in the model holds high representational signiﬁcance, causing the coefﬁcients of other variables to take negative values to balance the over- all data. These ﬁndings highlight the complex roles that economic scale, technological exports, and population distribution play in the distribution of cybercrime.

<!-- b007316 | prose | pages [21] -->
The results show that the higher the GDP, the greater the number of cybercrime incidents. This ﬁnding aligns with the global crime distribution patterns analyzed in

<!-- b007317 | furniture | pages [22] -->
Team # 2521039

<!-- b007318 | furniture | pages [22] -->
Page 22 of 25

<!-- b007319 | prose | pages [22] -->
Section 4, where developed countries exhibit signiﬁcantly more cybercrime incidents compared to developing and poor countries. Based on the ﬁve pillars of GCI (Legal Measures, Technical Measures, Organizational Measures, Capacity Building, and Cooperation), GDP inﬂuences a country’s scores in the Technical and Capacity Build-

<!-- b007320 | heading | pages [22] -->
ing pillars. Combined with the conclusions from Section 5, advancements in technical

<!-- b007321 | prose | pages [22] -->
capabilities and efﬁcient organizational coordination are critical to the effectiveness of cybersecurity policies. Changes in GCI scores further impact the ultimate outcomes of cybercrime distribution, which aligns with the inﬂuence of GDP on cybercrime, pro- viding strong theoretical support for Model 1.

<!-- b007322 | prose | pages [22] -->
7

<!-- b007323 | heading | pages [22] -->
Model Evaluation

<!-- b007324 | prose | pages [22] -->
7.1 Merits

<!-- b007325 | heading | pages [22] -->
1. Reliable Data Sources and Robust Data Processing

<!-- b007326 | prose | pages [22] -->
We utilized the VCDB database from the VERIS project and applied logarithmic transformations to the variables. Missing values and outliers were cleaned to enhance data quality. Standardization was performed to avoid inaccuracies in the model caused by differences in variable scales.

<!-- b007327 | heading | pages [22] -->
2. Suitability for Policy Implementation Analysis

<!-- b007328 | prose | pages [22] -->
The HISR model is well-suited for analyzing natural experiments such as policy implementation, where random assignment is not feasible. It effectively evalu- ates the net effects of policies or interventions. By controlling for time variables, the model avoids biases caused by temporal changes.

<!-- b007329 | heading | pages [22] -->
3. Comprehensive Modeling

<!-- b007330 | prose | pages [22] -->
Key indicators such as baseline economic conditions, internet penetration rates, and education levels were referenced to maximize the balance between the ex- periment group and the control group. This approach effectively eliminated the inﬂuence of time trends and other external factors.

<!-- b007331 | heading | pages [22] -->
4. Clear Modeling Logic

<!-- b007332 | prose | pages [22] -->
The model’s core variables intuitively reﬂect the actual effects of policies, offer- ing strong practical guidance for policy-making. The overall construction of the model follows an optimization strategy that progresses from simple to complex, systematically and reasonably improving its performance.

<!-- b007333 | prose | pages [22] -->
7.2 Limitations

<!-- b007334 | heading | pages [22] -->
1. Heterogeneity in Policy Implementation and Context

<!-- b007335 | prose | pages [22] -->
Differences in policy implementation and execution environments across coun- tries may exist, and these heterogeneity factors might not be fully captured by simple interaction terms.

<!-- b007336 | heading | pages [22] -->
2. Limitations of Inﬂuencing Factors

<!-- b007337 | heading | pages [22] -->
Although the model incorporates GDP, ICT Goods Export, and Population as

<!-- b007338 | prose | pages [22] -->
variables, many other potential inﬂuencing factors were not fully included, which may result in the model failing to comprehensively reﬂect the driving forces be- hind the target variable.

<!-- b007339 | prose | pages [22] -->
关注数学模型

<!-- b007340 | furniture | pages [22] -->
2

<!-- b007341 | furniture | pages [22] -->
MATHmodels

<!-- b007342 | furniture | pages [22] -->
获取更多资讯

<!-- b007343 | furniture | pages [23] -->
Team # 2521039

<!-- b007344 | furniture | pages [23] -->
Page 23 of 25

<!-- b007345 | prose | pages [23] -->
8

<!-- b007346 | heading | pages [23] -->
Conclusions

<!-- b007347 | prose | pages [23] -->
In this study, we ﬁrst processed open data from the VCDB database to analyze the

<!-- b007348 | prose | pages [23] -->
微信公众号：数学模型

<!-- b007349 | prose | pages [23] -->
global cybercrime distribution. The results show that cybercrime incidents are more concentrated in economically developed regions with well-established internet infras- tructure.

<!-- b007350 | prose | pages [23] -->
Next, we employed a multi-level linear regression model to explore the effects of policies and their implementation timing on the distribution of cybercrime. We then

<!-- b007351 | heading | pages [23] -->
used the HISR model to evaluate the effectiveness of cybersecurity policy implementa-

<!-- b007352 | prose | pages [23] -->
tion, and ﬁnally validated the study’s theoretical framework through correlation anal- ysis and the LEQR Model.

<!-- b007353 | prose | pages [23] -->
The results indicate that policies and their implementation timing have both inde- pendent and interactive effects on global cybercrime distribution. Moreover, advance-

<!-- b007354 | prose | pages [23] -->
微信号：MATHmodels

<!-- b007355 | prose | pages [23] -->
ments in technical capabilities and efﬁcient organizational coordination are critical to enhancing the effectiveness of cybersecurity policies. Additionally, analysis of coun- tries composite scores and indicators reveals that reporting rate and thwart rate are key metrics for evaluating the effectiveness of cybersecurity policies. The reporting rate reﬂects a country’s capacity to monitor and record cybercrime, as well as public recognition of policy transparency and trust. The thwart rate directly demonstrates a country’s technical skills and operational efﬁciency in defending against and inter- rupting cybercrime attacks.

<!-- b007356 | prose | pages [23] -->
To comprehensively enhance national cybersecurity levels, countries can learn from those with varying composite scores by leveraging strengths and addressing weak- nesses. According to the ﬁve pillars of GCI (Legal Measures, Technical Measures, Organizational Measures, Capacity Building, and Cooperation), policymakers should prioritize improving cybersecurity technology and optimizing organizational struc- tures to ensure effective policy implementation. Examples include emphasizing ad- vancements in cybersecurity technology, strengthening national and sectoral cyberse- curity emergency response agencies, establishing robust national cybersecurity stan- dards frameworks, and implementing child online protection initiatives.

<!-- b007357 | prose | pages [23] -->
Our research also reveals that national demographic data, such as GDP, popula- tion size, and ICT development levels, signiﬁcantly inﬂuence the formulation and implementation of cybersecurity policies. GDP, population size, and ICT develop- ment levels are positively correlated with cybercrime incidence. This suggests that policymakers should fully consider their country’s development context when formu- lating cybersecurity policies tailored to national conditions. For countries with higher GDP, larger populations, and more advanced ICT development, there is a greater like- lihood of experiencing higher levels of cybercrime. These countries should emphasize cybersecurity, allocate more resources to combating cybercrime, and ensure network security.

<!-- b007358 | prose | pages [23] -->
9

<!-- b007359 | heading | pages [23] -->
Memorandum

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

<!-- b007578 | prose | pages [23] -->
m

<!-- b007579 | prose | pages [23] -->
m

<!-- b007580 | prose | pages [23] -->
m

<!-- b007581 | prose | pages [23] -->
m

<!-- b007582 | prose | pages [23] -->
m

<!-- b007583 | prose | pages [23] -->
m

<!-- b007584 | prose | pages [23] -->
m

<!-- b007585 | prose | pages [23] -->
m

<!-- b007586 | prose | pages [23] -->
m

<!-- b007587 | prose | pages [23] -->
m

<!-- b007588 | prose | pages [23] -->
m

<!-- b007589 | prose | pages [23] -->
m

<!-- b007590 | prose | pages [23] -->
m

<!-- b007591 | prose | pages [23] -->
m

<!-- b007592 | prose | pages [23] -->
m

<!-- b007593 | prose | pages [23] -->
m

<!-- b007594 | prose | pages [23] -->
m

<!-- b007595 | prose | pages [23] -->
m

<!-- b007596 | prose | pages [23] -->
m

<!-- b007597 | prose | pages [23] -->
m

<!-- b007598 | prose | pages [23] -->
m

<!-- b007599 | prose | pages [23] -->
m

<!-- b007600 | prose | pages [23] -->
m

<!-- b007601 | prose | pages [23] -->
m

<!-- b007602 | prose | pages [23] -->
m

<!-- b007603 | prose | pages [23] -->
m

<!-- b007604 | prose | pages [23] -->
m

<!-- b007605 | prose | pages [23] -->
m

<!-- b007606 | prose | pages [23] -->
m

<!-- b007607 | prose | pages [23] -->
m

<!-- b007608 | prose | pages [23] -->
m

<!-- b007609 | prose | pages [23] -->
m

<!-- b007610 | prose | pages [23] -->
m

<!-- b007611 | prose | pages [23] -->
m

<!-- b007612 | prose | pages [23] -->
m

<!-- b007613 | prose | pages [23] -->
m

<!-- b007614 | prose | pages [23] -->
m

<!-- b007615 | prose | pages [23] -->
m

<!-- b007616 | prose | pages [23] -->
m

<!-- b007617 | prose | pages [23] -->
m

<!-- b007618 | prose | pages [23] -->
m

<!-- b007619 | prose | pages [23] -->
m

<!-- b007620 | prose | pages [23] -->
m

<!-- b007621 | prose | pages [23] -->
m

<!-- b007622 | prose | pages [23] -->
m

<!-- b007623 | prose | pages [23] -->
m

<!-- b007624 | prose | pages [23] -->
m

<!-- b007625 | prose | pages [23] -->
m

<!-- b007626 | prose | pages [23] -->
m

<!-- b007627 | prose | pages [23] -->
m

<!-- b007628 | prose | pages [23] -->
m

<!-- b007629 | prose | pages [23] -->
m

<!-- b007630 | prose | pages [23] -->
m

<!-- b007631 | prose | pages [23] -->
m

<!-- b007632 | prose | pages [23] -->
m

<!-- b007633 | prose | pages [23] -->
m

<!-- b007634 | prose | pages [23] -->
m

<!-- b007635 | prose | pages [23] -->
m

<!-- b007636 | prose | pages [23] -->
m

<!-- b007637 | prose | pages [23] -->
m

<!-- b007638 | prose | pages [23] -->
m

<!-- b007639 | prose | pages [23] -->
m

<!-- b007640 | prose | pages [23] -->
m

<!-- b007641 | prose | pages [23] -->
m

<!-- b007642 | prose | pages [23] -->
m

<!-- b007643 | prose | pages [23] -->
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

<!-- b007981 | furniture | pages [23] -->
m

<!-- b007982 | furniture | pages [23] -->
m

<!-- b007983 | furniture | pages [23] -->
m

<!-- b007984 | furniture | pages [23] -->
m

<!-- b007985 | furniture | pages [23] -->
m

<!-- b007986 | furniture | pages [23] -->
m

<!-- b007987 | furniture | pages [23] -->
m

<!-- b007988 | furniture | pages [23] -->
m

<!-- b007989 | furniture | pages [23] -->
m

<!-- b007990 | furniture | pages [23] -->
m

<!-- b007991 | furniture | pages [23] -->
m

<!-- b007992 | furniture | pages [23] -->
m

<!-- b007993 | furniture | pages [23] -->
m

<!-- b007994 | furniture | pages [23] -->
m

<!-- b007995 | furniture | pages [23] -->
m

<!-- b007996 | furniture | pages [23] -->
m

<!-- b007997 | furniture | pages [23] -->
m

<!-- b007998 | furniture | pages [23] -->
m

<!-- b007999 | furniture | pages [23] -->
m

<!-- b008000 | furniture | pages [23] -->
m

<!-- b008001 | furniture | pages [23] -->
m

<!-- b008002 | furniture | pages [23] -->
m

<!-- b008003 | furniture | pages [23] -->
m

<!-- b008004 | furniture | pages [23] -->
m

<!-- b008005 | furniture | pages [23] -->
m

<!-- b008006 | furniture | pages [23] -->
m

<!-- b008007 | furniture | pages [23] -->
m

<!-- b008008 | furniture | pages [23] -->
m

<!-- b008009 | furniture | pages [23] -->
m

<!-- b008010 | furniture | pages [23] -->
m

<!-- b008011 | furniture | pages [23] -->
m

<!-- b008012 | furniture | pages [23] -->
m

<!-- b008013 | furniture | pages [23] -->
m

<!-- b008014 | furniture | pages [23] -->
m

<!-- b008015 | furniture | pages [23] -->
m

<!-- b008016 | furniture | pages [23] -->
m

<!-- b008017 | furniture | pages [23] -->
m

<!-- b008018 | furniture | pages [23] -->
m

<!-- b008019 | furniture | pages [23] -->
m

<!-- b008020 | furniture | pages [23] -->
m

<!-- b008021 | furniture | pages [23] -->
m

<!-- b008022 | furniture | pages [23] -->
m

<!-- b008023 | furniture | pages [23] -->
m

<!-- b008024 | furniture | pages [23] -->
m

<!-- b008025 | furniture | pages [23] -->
m

<!-- b008026 | furniture | pages [23] -->
m

<!-- b008027 | furniture | pages [23] -->
m

<!-- b008028 | furniture | pages [23] -->
m

<!-- b008029 | furniture | pages [23] -->
m

<!-- b008030 | furniture | pages [23] -->
m

<!-- b008031 | furniture | pages [23] -->
m

<!-- b008032 | furniture | pages [23] -->
m

<!-- b008033 | furniture | pages [23] -->
m

<!-- b008034 | furniture | pages [23] -->
m

<!-- b008035 | furniture | pages [23] -->
m

<!-- b008036 | furniture | pages [23] -->
m

<!-- b008037 | furniture | pages [23] -->
m

<!-- b008038 | furniture | pages [23] -->
m

<!-- b008039 | furniture | pages [23] -->
m

<!-- b008040 | furniture | pages [23] -->
m

<!-- b008041 | furniture | pages [23] -->
m

<!-- b008042 | furniture | pages [23] -->
m

<!-- b008043 | furniture | pages [23] -->
m

<!-- b008044 | furniture | pages [23] -->
m

<!-- b008045 | furniture | pages [23] -->
m

<!-- b008046 | furniture | pages [23] -->
m

<!-- b008047 | furniture | pages [25] -->
Team # 2521039

<!-- b008048 | heading | pages [25] -->
References

<!-- b008049 | furniture | pages [25] -->
Page 25 of 25

<!-- b008050 | references | pages [25] -->
[1] Li, Y., Wang, H., Li, Y., et al. Research on the Layout and Enlightenment of For-

<!-- b008051 | references | pages [25] -->
eign Industrial Internet Security Industry [J]. China Engineering Science, 2021,

<!-- b008052 | references | pages [25] -->
23(02):112-121.

<!-- b008053 | references | pages [25] -->
[2] Li, X. Research on U.S. Cybersecurity Legislation and Its Implications [D].

<!-- b008054 | references | pages [25] -->
Chongqing University, 2016.

<!-- b008055 | references | pages [25] -->
[3] Moreira, G. B., Calegario, V. M., Duarte, J. C., et al. Extending the VERIS Frame-

<!-- b008056 | references | pages [25] -->
work to an Incident Handling Ontology [C]//2018 IEEE/WIC/ACM Interna-

<!-- b008057 | references | pages [25] -->
微信公众号：数学模型

<!-- b008058 | references | pages [25] -->
tional Conference on Web Intelligence (WI). IEEE, 2018: 440-445.

<!-- b008059 | references | pages [25] -->
[4] Boehmke, B. C. Transforming Your Data with dplyr [J]. Data Wrangling with R,

<!-- b008060 | references | pages [25] -->
2016: 219-232.

<!-- b008061 | references | pages [25] -->
[5] Villanueva, Chen. ggplot2: Elegant Graphics for Data Analysis (2nd ed.) [J]. Mea-

<!-- b008062 | references | pages [25] -->
surement: Interdisciplinary Research and Perspectives, 2019, 17(3):160-167.

<!-- b008063 | references | pages [25] -->
[6] National

<!-- b008064 | references | pages [25] -->
Security

<!-- b008065 | references | pages [25] -->
Memorandum

<!-- b008066 | references | pages [25] -->
cal Infrastructure Control Systems

<!-- b008067 | references | pages [25] -->
on

<!-- b008068 | references | pages [25] -->
Improving

<!-- b008069 | references | pages [25] -->
Cybersecurity

<!-- b008070 | references | pages [25] -->
for

<!-- b008071 | references | pages [25] -->
Criti-

<!-- b008072 | references | pages [25] -->
CyberIR@MIT [EB/OL]. [2025-01-26].

<!-- b008073 | references | pages [25] -->
https://cyberir.mit.edu/site/national-security-memorandum-improving-

<!-- b008074 | references | pages [25] -->
微信号：MATHmodels

<!-- b008075 | references | pages [25] -->
cybersecurity-critical-infrastructure-control-systems/.

<!-- b008076 | references | pages [25] -->
Cybersecurity

<!-- b008077 | references | pages [25] -->
[7] Biden,

<!-- b008078 | references | pages [25] -->
J.

<!-- b008079 | references | pages [25] -->
R.

<!-- b008080 | references | pages [25] -->
Jr.

<!-- b008081 | references | pages [25] -->
National

<!-- b008082 | references | pages [25] -->
Strategy

<!-- b008083 | references | pages [25] -->
[EB/OL].

<!-- b008084 | references | pages [25] -->
[2025-01-26].

<!-- b008085 | references | pages [25] -->
https://www.whitehouse.gov/wp-content/uploads/2023/03/National-

<!-- b008086 | references | pages [25] -->
Cybersecurity-Strategy-2023.pdf.

<!-- b008087 | references | pages [25] -->
[8] The Senate and House of Representatives of the United States of Amer-

<!-- b008088 | references | pages [25] -->
ica. IoT Cybersecurity Improvement Act of 2020 [EB/OL]. [2025-01-26].

<!-- b008089 | references | pages [25] -->
https://www.congress.gov/bill/116th-congress/house-bill/1668.

<!-- b008090 | references | pages [25] -->
[9] National

<!-- b008091 | references | pages [25] -->
Institute

<!-- b008092 | references | pages [25] -->
of

<!-- b008093 | references | pages [25] -->
Standards

<!-- b008094 | references | pages [25] -->
velopment

<!-- b008095 | references | pages [25] -->
Framework

<!-- b008096 | references | pages [25] -->
(SSDF)

<!-- b008097 | references | pages [25] -->
and

<!-- b008098 | references | pages [25] -->
Technology.

<!-- b008099 | references | pages [25] -->
Secure

<!-- b008100 | references | pages [25] -->
Software

<!-- b008101 | references | pages [25] -->
De-

<!-- b008102 | references | pages [25] -->
Version

<!-- b008103 | references | pages [25] -->
1.1

<!-- b008104 | references | pages [25] -->
[EB/OL].

<!-- b008105 | references | pages [25] -->
[2025-01-26].

<!-- b008106 | references | pages [25] -->
https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf.

<!-- b008107 | references | pages [25] -->
[10] Zhang, L., Huang, R. Analysis of the Organizational Structure of Cybersecurity in

<!-- b008108 | references | pages [25] -->
the United States [J]. Journal of Jiangnan Social Institute, 2014, 16(02):18-21.

<!-- b008109 | references | pages [25] -->
[11] Cai, C., Li, J. Cybersecurity Cooperation within the U.S.-Asia-Paciﬁc Alliance Sys-

<!-- b008110 | references | pages [25] -->
tem [J]. World Economics and Politics, 2018, (06):51-77+157.

<!-- b008111 | references | pages [25] -->
[12] Chen, H. U.S.-South Korea Cybersecurity Cooperation: Motivations, Plans, and

<!-- b008112 | references | pages [25] -->
Limitations [J]. Journal of Intelligence, 2024, 43(11):52-60.

<!-- b008113 | references | pages [25] -->
[13] Shen, C. Study on Canada’s Cybersecurity Strategy [J]. Cybersecurity Technology

<!-- b008114 | references | pages [25] -->
and Application, 2023, (04):168-170.

<!-- b008115 | references | pages [25] -->
[14] Liu, D., Yang, G., Zhu, C. Challenges in China’s Cybersecurity Ecosystem [J]. Peo-

<!-- b008116 | references | pages [25] -->
ple’s Forum, 2016, (04):47. DOI:10.16619/j.cnki.rmlt.2016.04.067.

<!-- b008117 | references | pages [25] -->
[15] Wei, H., Hao, X. Differences in ASEAN Cybersecurity Governance Systems and

<!-- b008118 | references | pages [25] -->
China-ASEAN Cooperation [J]. South and Southeast Asian Studies, 2023, (03):22-

<!-- b008119 | references | pages [25] -->
36+153-154. DOI:10.13848/j.cnki.dnynybjb.2023.03.006.

<!-- b008120 | furniture | pages [26] -->
Team # 2521039

<!-- b008121 | heading | pages [26] -->
Report on Use of AI

<!-- b008122 | ai_disclosure | pages [26] -->
OpenAI ChatGPT (Jan 27, 2025 version, ChatGPT-4)

<!-- b008123 | ai_disclosure | pages [26] -->
1.

<!-- b008124 | ai_disclosure | pages [26] -->
m

<!-- b008125 | ai_disclosure | pages [26] -->
m

<!-- b008126 | ai_disclosure | pages [26] -->
m

<!-- b008127 | ai_disclosure | pages [26] -->
m

<!-- b008128 | ai_disclosure | pages [26] -->
m

<!-- b008129 | ai_disclosure | pages [26] -->
m

<!-- b008130 | ai_disclosure | pages [26] -->
m

<!-- b008131 | ai_disclosure | pages [26] -->
m

<!-- b008132 | ai_disclosure | pages [26] -->
m

<!-- b008133 | ai_disclosure | pages [26] -->
m

<!-- b008134 | ai_disclosure | pages [26] -->
m

<!-- b008135 | ai_disclosure | pages [26] -->
m

<!-- b008136 | ai_disclosure | pages [26] -->
m

<!-- b008137 | ai_disclosure | pages [26] -->
m

<!-- b008138 | ai_disclosure | pages [26] -->
m

<!-- b008139 | ai_disclosure | pages [26] -->
m

<!-- b008140 | ai_disclosure | pages [26] -->
m

<!-- b008141 | ai_disclosure | pages [26] -->
m

<!-- b008142 | ai_disclosure | pages [26] -->
m

<!-- b008143 | ai_disclosure | pages [26] -->
m

<!-- b008144 | ai_disclosure | pages [26] -->
m

<!-- b008145 | ai_disclosure | pages [26] -->
m

<!-- b008146 | ai_disclosure | pages [26] -->
m

<!-- b008147 | ai_disclosure | pages [26] -->
m

<!-- b008148 | ai_disclosure | pages [26] -->
m

<!-- b008149 | ai_disclosure | pages [26] -->
m

<!-- b008150 | ai_disclosure | pages [26] -->
m

<!-- b008151 | ai_disclosure | pages [26] -->
m

<!-- b008152 | ai_disclosure | pages [26] -->
m

<!-- b008153 | ai_disclosure | pages [26] -->
m

<!-- b008154 | ai_disclosure | pages [26] -->
m

<!-- b008155 | ai_disclosure | pages [26] -->
m

<!-- b008156 | ai_disclosure | pages [26] -->
m

<!-- b008157 | ai_disclosure | pages [26] -->
m

<!-- b008158 | ai_disclosure | pages [26] -->
m

<!-- b008159 | ai_disclosure | pages [26] -->
m

<!-- b008160 | ai_disclosure | pages [26] -->
m

<!-- b008161 | ai_disclosure | pages [26] -->
m

<!-- b008162 | ai_disclosure | pages [26] -->
m

<!-- b008163 | ai_disclosure | pages [26] -->
m

<!-- b008164 | ai_disclosure | pages [26] -->
m

<!-- b008165 | ai_disclosure | pages [26] -->
m

<!-- b008166 | ai_disclosure | pages [26] -->
m

<!-- b008167 | ai_disclosure | pages [26] -->
m

<!-- b008168 | ai_disclosure | pages [26] -->
m

<!-- b008169 | ai_disclosure | pages [26] -->
m

<!-- b008170 | ai_disclosure | pages [26] -->
m

<!-- b008171 | ai_disclosure | pages [26] -->
m

<!-- b008172 | ai_disclosure | pages [26] -->
m

<!-- b008173 | ai_disclosure | pages [26] -->
m

<!-- b008174 | ai_disclosure | pages [26] -->
m

<!-- b008175 | ai_disclosure | pages [26] -->
m

<!-- b008176 | ai_disclosure | pages [26] -->
m

<!-- b008177 | ai_disclosure | pages [26] -->
m

<!-- b008178 | ai_disclosure | pages [26] -->
m

<!-- b008179 | ai_disclosure | pages [26] -->
m

<!-- b008180 | ai_disclosure | pages [26] -->
m

<!-- b008181 | ai_disclosure | pages [26] -->
m

<!-- b008182 | ai_disclosure | pages [26] -->
m

<!-- b008183 | ai_disclosure | pages [26] -->
m

<!-- b008184 | ai_disclosure | pages [26] -->
m

<!-- b008185 | ai_disclosure | pages [26] -->
m

<!-- b008186 | ai_disclosure | pages [26] -->
m

<!-- b008187 | ai_disclosure | pages [26] -->
m

<!-- b008188 | ai_disclosure | pages [26] -->
m

<!-- b008189 | ai_disclosure | pages [26] -->
m

<!-- b008190 | ai_disclosure | pages [26] -->
m

<!-- b008191 | ai_disclosure | pages [26] -->
m

<!-- b008192 | ai_disclosure | pages [26] -->
m

<!-- b008193 | ai_disclosure | pages [26] -->
m

<!-- b008194 | ai_disclosure | pages [26] -->
m

<!-- b008195 | ai_disclosure | pages [26] -->
m

<!-- b008196 | ai_disclosure | pages [26] -->
m

<!-- b008197 | ai_disclosure | pages [26] -->
m

<!-- b008198 | ai_disclosure | pages [26] -->
m

<!-- b008199 | ai_disclosure | pages [26] -->
m

<!-- b008200 | ai_disclosure | pages [26] -->
m

<!-- b008201 | ai_disclosure | pages [26] -->
m

<!-- b008202 | ai_disclosure | pages [26] -->
m

<!-- b008203 | ai_disclosure | pages [26] -->
m

<!-- b008204 | ai_disclosure | pages [26] -->
m

<!-- b008205 | ai_disclosure | pages [26] -->
m

<!-- b008206 | ai_disclosure | pages [26] -->
m

<!-- b008207 | ai_disclosure | pages [26] -->
m

<!-- b008208 | ai_disclosure | pages [26] -->
m

<!-- b008209 | ai_disclosure | pages [26] -->
m

<!-- b008210 | ai_disclosure | pages [26] -->
m

<!-- b008211 | ai_disclosure | pages [26] -->
m

<!-- b008212 | ai_disclosure | pages [26] -->
m

<!-- b008213 | ai_disclosure | pages [26] -->
m

<!-- b008214 | ai_disclosure | pages [26] -->
m

<!-- b008215 | ai_disclosure | pages [26] -->
m

<!-- b008216 | ai_disclosure | pages [26] -->
m

<!-- b008217 | ai_disclosure | pages [26] -->
m

<!-- b008218 | ai_disclosure | pages [26] -->
m

<!-- b008219 | ai_disclosure | pages [26] -->
m

<!-- b008220 | ai_disclosure | pages [26] -->
m

<!-- b008221 | ai_disclosure | pages [26] -->
m

<!-- b008222 | ai_disclosure | pages [26] -->
m

<!-- b008223 | ai_disclosure | pages [26] -->
m

<!-- b008224 | ai_disclosure | pages [26] -->
m

<!-- b008225 | ai_disclosure | pages [26] -->
m

<!-- b008226 | ai_disclosure | pages [26] -->
m

<!-- b008227 | ai_disclosure | pages [26] -->
m

<!-- b008228 | ai_disclosure | pages [26] -->
m

<!-- b008229 | ai_disclosure | pages [26] -->
m

<!-- b008230 | ai_disclosure | pages [26] -->
m

<!-- b008231 | ai_disclosure | pages [26] -->
m

<!-- b008232 | ai_disclosure | pages [26] -->
m

<!-- b008233 | ai_disclosure | pages [26] -->
m

<!-- b008234 | ai_disclosure | pages [26] -->
m

<!-- b008235 | ai_disclosure | pages [26] -->
m

<!-- b008236 | ai_disclosure | pages [26] -->
m

<!-- b008237 | ai_disclosure | pages [26] -->
m

<!-- b008238 | ai_disclosure | pages [26] -->
m

<!-- b008239 | ai_disclosure | pages [26] -->
m

<!-- b008240 | ai_disclosure | pages [26] -->
m

<!-- b008241 | ai_disclosure | pages [26] -->
m

<!-- b008242 | ai_disclosure | pages [26] -->
m

<!-- b008243 | ai_disclosure | pages [26] -->
m

<!-- b008244 | ai_disclosure | pages [26] -->
m

<!-- b008245 | ai_disclosure | pages [26] -->
m

<!-- b008246 | ai_disclosure | pages [26] -->
m

<!-- b008247 | ai_disclosure | pages [26] -->
m

<!-- b008248 | ai_disclosure | pages [26] -->
m

<!-- b008249 | ai_disclosure | pages [26] -->
m

<!-- b008250 | ai_disclosure | pages [26] -->
m

<!-- b008251 | ai_disclosure | pages [26] -->
m

<!-- b008252 | ai_disclosure | pages [26] -->
m

<!-- b008253 | ai_disclosure | pages [26] -->
m

<!-- b008254 | ai_disclosure | pages [26] -->
m

<!-- b008255 | ai_disclosure | pages [26] -->
m

<!-- b008256 | ai_disclosure | pages [26] -->
m

<!-- b008257 | ai_disclosure | pages [26] -->
m

<!-- b008258 | ai_disclosure | pages [26] -->
m

<!-- b008259 | ai_disclosure | pages [26] -->
m

<!-- b008260 | ai_disclosure | pages [26] -->
m

<!-- b008261 | ai_disclosure | pages [26] -->
m

<!-- b008262 | ai_disclosure | pages [26] -->
m

<!-- b008263 | ai_disclosure | pages [26] -->
m

<!-- b008264 | ai_disclosure | pages [26] -->
m

<!-- b008265 | ai_disclosure | pages [26] -->
m

<!-- b008266 | ai_disclosure | pages [26] -->
m

<!-- b008267 | ai_disclosure | pages [26] -->
m

<!-- b008268 | ai_disclosure | pages [26] -->
m

<!-- b008269 | ai_disclosure | pages [26] -->
m

<!-- b008270 | ai_disclosure | pages [26] -->
m

<!-- b008271 | ai_disclosure | pages [26] -->
m

<!-- b008272 | ai_disclosure | pages [26] -->
m

<!-- b008273 | ai_disclosure | pages [26] -->
m

<!-- b008274 | ai_disclosure | pages [26] -->
m

<!-- b008275 | ai_disclosure | pages [26] -->
m

<!-- b008276 | ai_disclosure | pages [26] -->
m

<!-- b008277 | ai_disclosure | pages [26] -->
m

<!-- b008278 | ai_disclosure | pages [26] -->
m

<!-- b008279 | ai_disclosure | pages [26] -->
m

<!-- b008280 | ai_disclosure | pages [26] -->
m

<!-- b008281 | ai_disclosure | pages [26] -->
m

<!-- b008282 | ai_disclosure | pages [26] -->
m

<!-- b008283 | ai_disclosure | pages [26] -->
m

<!-- b008284 | ai_disclosure | pages [26] -->
m

<!-- b008285 | ai_disclosure | pages [26] -->
m

<!-- b008286 | ai_disclosure | pages [26] -->
m

<!-- b008287 | ai_disclosure | pages [26] -->
m

<!-- b008288 | ai_disclosure | pages [26] -->
m

<!-- b008289 | ai_disclosure | pages [26] -->
m

<!-- b008290 | ai_disclosure | pages [26] -->
m

<!-- b008291 | ai_disclosure | pages [26] -->
m

<!-- b008292 | ai_disclosure | pages [26] -->
m

<!-- b008293 | ai_disclosure | pages [26] -->
m

<!-- b008294 | ai_disclosure | pages [26] -->
m

<!-- b008295 | ai_disclosure | pages [26] -->
m

<!-- b008296 | ai_disclosure | pages [26] -->
m

<!-- b008297 | ai_disclosure | pages [26] -->
m

<!-- b008298 | ai_disclosure | pages [26] -->
m

<!-- b008299 | ai_disclosure | pages [26] -->
m

<!-- b008300 | ai_disclosure | pages [26] -->
m

<!-- b008301 | ai_disclosure | pages [26] -->
m

<!-- b008302 | ai_disclosure | pages [26] -->
m

<!-- b008303 | ai_disclosure | pages [26] -->
m

<!-- b008304 | ai_disclosure | pages [26] -->
m

<!-- b008305 | ai_disclosure | pages [26] -->
m

<!-- b008306 | ai_disclosure | pages [26] -->
m

<!-- b008307 | ai_disclosure | pages [26] -->
m

<!-- b008308 | ai_disclosure | pages [26] -->
m

<!-- b008309 | ai_disclosure | pages [26] -->
m

<!-- b008310 | ai_disclosure | pages [26] -->
m

<!-- b008311 | ai_disclosure | pages [26] -->
m

<!-- b008312 | ai_disclosure | pages [26] -->
m

<!-- b008313 | ai_disclosure | pages [26] -->
m

<!-- b008314 | ai_disclosure | pages [26] -->
m

<!-- b008315 | ai_disclosure | pages [26] -->
m

<!-- b008316 | ai_disclosure | pages [26] -->
m

<!-- b008317 | ai_disclosure | pages [26] -->
m

<!-- b008318 | ai_disclosure | pages [26] -->
m

<!-- b008319 | ai_disclosure | pages [26] -->
m

<!-- b008320 | ai_disclosure | pages [26] -->
m

<!-- b008321 | ai_disclosure | pages [26] -->
m

<!-- b008322 | ai_disclosure | pages [26] -->
m

<!-- b008323 | ai_disclosure | pages [26] -->
m

<!-- b008324 | ai_disclosure | pages [26] -->
m

<!-- b008325 | ai_disclosure | pages [26] -->
m

<!-- b008326 | ai_disclosure | pages [26] -->
m

<!-- b008327 | ai_disclosure | pages [26] -->
m

<!-- b008328 | ai_disclosure | pages [26] -->
m

<!-- b008329 | ai_disclosure | pages [26] -->
m

<!-- b008330 | ai_disclosure | pages [26] -->
m

<!-- b008331 | ai_disclosure | pages [26] -->
m

<!-- b008332 | ai_disclosure | pages [26] -->
m

<!-- b008333 | ai_disclosure | pages [26] -->
m

<!-- b008334 | ai_disclosure | pages [26] -->
m

<!-- b008335 | ai_disclosure | pages [26] -->
m

<!-- b008336 | ai_disclosure | pages [26] -->
m

<!-- b008337 | ai_disclosure | pages [26] -->
m

<!-- b008338 | ai_disclosure | pages [26] -->
m

<!-- b008339 | ai_disclosure | pages [26] -->
m

<!-- b008340 | ai_disclosure | pages [26] -->
m

<!-- b008341 | ai_disclosure | pages [26] -->
m

<!-- b008342 | ai_disclosure | pages [26] -->
m

<!-- b008343 | ai_disclosure | pages [26] -->
m

<!-- b008344 | ai_disclosure | pages [26] -->
m

<!-- b008345 | ai_disclosure | pages [26] -->
m

<!-- b008346 | ai_disclosure | pages [26] -->
m

<!-- b008347 | ai_disclosure | pages [26] -->
m

<!-- b008348 | ai_disclosure | pages [26] -->
m

<!-- b008349 | ai_disclosure | pages [26] -->
m

<!-- b008350 | ai_disclosure | pages [26] -->
m

<!-- b008351 | ai_disclosure | pages [26] -->
m

<!-- b008352 | ai_disclosure | pages [26] -->
m

<!-- b008353 | ai_disclosure | pages [26] -->
m

<!-- b008354 | ai_disclosure | pages [26] -->
m

<!-- b008355 | ai_disclosure | pages [26] -->
m

<!-- b008356 | ai_disclosure | pages [26] -->
m

<!-- b008357 | ai_disclosure | pages [26] -->
m

<!-- b008358 | ai_disclosure | pages [26] -->
m

<!-- b008359 | ai_disclosure | pages [26] -->
m

<!-- b008360 | ai_disclosure | pages [26] -->
m

<!-- b008361 | ai_disclosure | pages [26] -->
m

<!-- b008362 | ai_disclosure | pages [26] -->
m

<!-- b008363 | ai_disclosure | pages [26] -->
m

<!-- b008364 | ai_disclosure | pages [26] -->
m

<!-- b008365 | ai_disclosure | pages [26] -->
m

<!-- b008366 | ai_disclosure | pages [26] -->
m

<!-- b008367 | ai_disclosure | pages [26] -->
m

<!-- b008368 | ai_disclosure | pages [26] -->
m

<!-- b008369 | ai_disclosure | pages [26] -->
m

<!-- b008370 | ai_disclosure | pages [26] -->
m

<!-- b008371 | ai_disclosure | pages [26] -->
m

<!-- b008372 | ai_disclosure | pages [26] -->
m

<!-- b008373 | ai_disclosure | pages [26] -->
m

<!-- b008374 | ai_disclosure | pages [26] -->
m

<!-- b008375 | ai_disclosure | pages [26] -->
m

<!-- b008376 | ai_disclosure | pages [26] -->
m

<!-- b008377 | ai_disclosure | pages [26] -->
m

<!-- b008378 | ai_disclosure | pages [26] -->
m

<!-- b008379 | ai_disclosure | pages [26] -->
m

<!-- b008380 | ai_disclosure | pages [26] -->
m

<!-- b008381 | ai_disclosure | pages [26] -->
m

<!-- b008382 | ai_disclosure | pages [26] -->
m

<!-- b008383 | ai_disclosure | pages [26] -->
m

<!-- b008384 | ai_disclosure | pages [26] -->
m

<!-- b008385 | ai_disclosure | pages [26] -->
m

<!-- b008386 | ai_disclosure | pages [26] -->
Query1: Where can I ﬁnd reliable sources to collect national demographic data, such

<!-- b008387 | ai_disclosure | pages [26] -->
m

<!-- b008388 | ai_disclosure | pages [26] -->
m

<!-- b008389 | ai_disclosure | pages [26] -->
m

<!-- b008390 | ai_disclosure | pages [26] -->
m

<!-- b008391 | ai_disclosure | pages [26] -->
m

<!-- b008392 | ai_disclosure | pages [26] -->
m

<!-- b008393 | ai_disclosure | pages [26] -->
m

<!-- b008394 | ai_disclosure | pages [26] -->
m

<!-- b008395 | ai_disclosure | pages [26] -->
m

<!-- b008396 | ai_disclosure | pages [26] -->
m

<!-- b008397 | ai_disclosure | pages [26] -->
m

<!-- b008398 | ai_disclosure | pages [26] -->
m

<!-- b008399 | ai_disclosure | pages [26] -->
m

<!-- b008400 | ai_disclosure | pages [26] -->
m

<!-- b008401 | ai_disclosure | pages [26] -->
m

<!-- b008402 | ai_disclosure | pages [26] -->
m

<!-- b008403 | ai_disclosure | pages [26] -->
m

<!-- b008404 | ai_disclosure | pages [26] -->
m

<!-- b008405 | ai_disclosure | pages [26] -->
m

<!-- b008406 | ai_disclosure | pages [26] -->
m

<!-- b008407 | ai_disclosure | pages [26] -->
m

<!-- b008408 | ai_disclosure | pages [26] -->
m

<!-- b008409 | ai_disclosure | pages [26] -->
m

<!-- b008410 | ai_disclosure | pages [26] -->
m

<!-- b008411 | ai_disclosure | pages [26] -->
m

<!-- b008412 | ai_disclosure | pages [26] -->
m

<!-- b008413 | ai_disclosure | pages [26] -->
m

<!-- b008414 | ai_disclosure | pages [26] -->
m

<!-- b008415 | ai_disclosure | pages [26] -->
m

<!-- b008416 | ai_disclosure | pages [26] -->
m

<!-- b008417 | ai_disclosure | pages [26] -->
m

<!-- b008418 | ai_disclosure | pages [26] -->
m

<!-- b008419 | ai_disclosure | pages [26] -->
m

<!-- b008420 | ai_disclosure | pages [26] -->
m

<!-- b008421 | ai_disclosure | pages [26] -->
m

<!-- b008422 | ai_disclosure | pages [26] -->
m

<!-- b008423 | ai_disclosure | pages [26] -->
m

<!-- b008424 | ai_disclosure | pages [26] -->
m

<!-- b008425 | ai_disclosure | pages [26] -->
m

<!-- b008426 | ai_disclosure | pages [26] -->
m

<!-- b008427 | ai_disclosure | pages [26] -->
m

<!-- b008428 | ai_disclosure | pages [26] -->
m

<!-- b008429 | ai_disclosure | pages [26] -->
m

<!-- b008430 | ai_disclosure | pages [26] -->
m

<!-- b008431 | ai_disclosure | pages [26] -->
m

<!-- b008432 | ai_disclosure | pages [26] -->
m

<!-- b008433 | ai_disclosure | pages [26] -->
m

<!-- b008434 | ai_disclosure | pages [26] -->
m

<!-- b008435 | ai_disclosure | pages [26] -->
m

<!-- b008436 | ai_disclosure | pages [26] -->
m

<!-- b008437 | ai_disclosure | pages [26] -->
m

<!-- b008438 | ai_disclosure | pages [26] -->
m

<!-- b008439 | ai_disclosure | pages [26] -->
m

<!-- b008440 | ai_disclosure | pages [26] -->
m

<!-- b008441 | ai_disclosure | pages [26] -->
m

<!-- b008442 | ai_disclosure | pages [26] -->
m

<!-- b008443 | ai_disclosure | pages [26] -->
m

<!-- b008444 | ai_disclosure | pages [26] -->
m

<!-- b008445 | ai_disclosure | pages [26] -->
m

<!-- b008446 | ai_disclosure | pages [26] -->
m

<!-- b008447 | ai_disclosure | pages [26] -->
m

<!-- b008448 | ai_disclosure | pages [26] -->
m

<!-- b008449 | ai_disclosure | pages [26] -->
m

<!-- b008450 | ai_disclosure | pages [26] -->
m

<!-- b008451 | ai_disclosure | pages [26] -->
m

<!-- b008452 | ai_disclosure | pages [26] -->
m

<!-- b008453 | ai_disclosure | pages [26] -->
m

<!-- b008454 | ai_disclosure | pages [26] -->
m

<!-- b008455 | ai_disclosure | pages [26] -->
m

<!-- b008456 | ai_disclosure | pages [26] -->
m

<!-- b008457 | ai_disclosure | pages [26] -->
m

<!-- b008458 | ai_disclosure | pages [26] -->
m

<!-- b008459 | ai_disclosure | pages [26] -->
m

<!-- b008460 | ai_disclosure | pages [26] -->
m

<!-- b008461 | ai_disclosure | pages [26] -->
m

<!-- b008462 | ai_disclosure | pages [26] -->
m

<!-- b008463 | ai_disclosure | pages [26] -->
m

<!-- b008464 | ai_disclosure | pages [26] -->
m

<!-- b008465 | ai_disclosure | pages [26] -->
m

<!-- b008466 | ai_disclosure | pages [26] -->
m

<!-- b008467 | ai_disclosure | pages [26] -->
m

<!-- b008468 | ai_disclosure | pages [26] -->
m

<!-- b008469 | ai_disclosure | pages [26] -->
m

<!-- b008470 | ai_disclosure | pages [26] -->
m

<!-- b008471 | ai_disclosure | pages [26] -->
m

<!-- b008472 | ai_disclosure | pages [26] -->
m

<!-- b008473 | ai_disclosure | pages [26] -->
m

<!-- b008474 | ai_disclosure | pages [26] -->
m

<!-- b008475 | ai_disclosure | pages [26] -->
m

<!-- b008476 | ai_disclosure | pages [26] -->
m

<!-- b008477 | ai_disclosure | pages [26] -->
m

<!-- b008478 | ai_disclosure | pages [26] -->
m

<!-- b008479 | ai_disclosure | pages [26] -->
m

<!-- b008480 | ai_disclosure | pages [26] -->
m

<!-- b008481 | ai_disclosure | pages [26] -->
m

<!-- b008482 | ai_disclosure | pages [26] -->
m

<!-- b008483 | ai_disclosure | pages [26] -->
m

<!-- b008484 | ai_disclosure | pages [26] -->
m

<!-- b008485 | ai_disclosure | pages [26] -->
m

<!-- b008486 | ai_disclosure | pages [26] -->
m

<!-- b008487 | ai_disclosure | pages [26] -->
m

<!-- b008488 | ai_disclosure | pages [26] -->
m

<!-- b008489 | ai_disclosure | pages [26] -->
m

<!-- b008490 | ai_disclosure | pages [26] -->
m

<!-- b008491 | ai_disclosure | pages [26] -->
m

<!-- b008492 | ai_disclosure | pages [26] -->
m

<!-- b008493 | ai_disclosure | pages [26] -->
m

<!-- b008494 | ai_disclosure | pages [26] -->
m

<!-- b008495 | ai_disclosure | pages [26] -->
m

<!-- b008496 | ai_disclosure | pages [26] -->
m

<!-- b008497 | ai_disclosure | pages [26] -->
m

<!-- b008498 | ai_disclosure | pages [26] -->
m

<!-- b008499 | ai_disclosure | pages [26] -->
m

<!-- b008500 | ai_disclosure | pages [26] -->
m

<!-- b008501 | ai_disclosure | pages [26] -->
m

<!-- b008502 | ai_disclosure | pages [26] -->
m

<!-- b008503 | ai_disclosure | pages [26] -->
m

<!-- b008504 | ai_disclosure | pages [26] -->
m

<!-- b008505 | ai_disclosure | pages [26] -->
m

<!-- b008506 | ai_disclosure | pages [26] -->
m

<!-- b008507 | ai_disclosure | pages [26] -->
m

<!-- b008508 | ai_disclosure | pages [26] -->
m

<!-- b008509 | ai_disclosure | pages [26] -->
m

<!-- b008510 | ai_disclosure | pages [26] -->
m

<!-- b008511 | ai_disclosure | pages [26] -->
m

<!-- b008512 | ai_disclosure | pages [26] -->
m

<!-- b008513 | ai_disclosure | pages [26] -->
m

<!-- b008514 | ai_disclosure | pages [26] -->
m

<!-- b008515 | ai_disclosure | pages [26] -->
m

<!-- b008516 | ai_disclosure | pages [26] -->
m

<!-- b008517 | ai_disclosure | pages [26] -->
m

<!-- b008518 | ai_disclosure | pages [26] -->
m

<!-- b008519 | ai_disclosure | pages [26] -->
m

<!-- b008520 | ai_disclosure | pages [26] -->
m

<!-- b008521 | ai_disclosure | pages [26] -->
m

<!-- b008522 | ai_disclosure | pages [26] -->
m

<!-- b008523 | ai_disclosure | pages [26] -->
m

<!-- b008524 | ai_disclosure | pages [26] -->
m

<!-- b008525 | ai_disclosure | pages [26] -->
m

<!-- b008526 | ai_disclosure | pages [26] -->
m

<!-- b008527 | ai_disclosure | pages [26] -->
m

<!-- b008528 | ai_disclosure | pages [26] -->
m

<!-- b008529 | ai_disclosure | pages [26] -->
m

<!-- b008530 | ai_disclosure | pages [26] -->
m

<!-- b008531 | ai_disclosure | pages [26] -->
as internet access levels, wealth, and education levels?

<!-- b008532 | ai_disclosure | pages [26] -->
Output:

<!-- b008533 | ai_disclosure | pages [26] -->
m

<!-- b008534 | ai_disclosure | pages [26] -->
m

<!-- b008535 | ai_disclosure | pages [26] -->
m

<!-- b008536 | ai_disclosure | pages [26] -->
m

<!-- b008537 | ai_disclosure | pages [26] -->
m

<!-- b008538 | ai_disclosure | pages [26] -->
m

<!-- b008539 | ai_disclosure | pages [26] -->
m

<!-- b008540 | ai_disclosure | pages [26] -->
m

<!-- b008541 | ai_disclosure | pages [26] -->
m

<!-- b008542 | ai_disclosure | pages [26] -->
m

<!-- b008543 | ai_disclosure | pages [26] -->
m

<!-- b008544 | ai_disclosure | pages [26] -->
m

<!-- b008545 | ai_disclosure | pages [26] -->
m

<!-- b008546 | ai_disclosure | pages [26] -->
m

<!-- b008547 | ai_disclosure | pages [26] -->
m

<!-- b008548 | ai_disclosure | pages [26] -->
m

<!-- b008549 | ai_disclosure | pages [26] -->
m

<!-- b008550 | ai_disclosure | pages [26] -->
m

<!-- b008551 | ai_disclosure | pages [26] -->
m

<!-- b008552 | ai_disclosure | pages [26] -->
m

<!-- b008553 | ai_disclosure | pages [26] -->
m

<!-- b008554 | ai_disclosure | pages [26] -->
m

<!-- b008555 | ai_disclosure | pages [26] -->
m

<!-- b008556 | ai_disclosure | pages [26] -->
m

<!-- b008557 | ai_disclosure | pages [26] -->
m

<!-- b008558 | ai_disclosure | pages [26] -->
m

<!-- b008559 | ai_disclosure | pages [26] -->
m

<!-- b008560 | ai_disclosure | pages [26] -->
m

<!-- b008561 | ai_disclosure | pages [26] -->
m

<!-- b008562 | ai_disclosure | pages [26] -->
m

<!-- b008563 | ai_disclosure | pages [26] -->
m

<!-- b008564 | ai_disclosure | pages [26] -->
m

<!-- b008565 | ai_disclosure | pages [26] -->
m

<!-- b008566 | ai_disclosure | pages [26] -->
m

<!-- b008567 | ai_disclosure | pages [26] -->
m

<!-- b008568 | ai_disclosure | pages [26] -->
m

<!-- b008569 | ai_disclosure | pages [26] -->
m

<!-- b008570 | ai_disclosure | pages [26] -->
m

<!-- b008571 | ai_disclosure | pages [26] -->
m

<!-- b008572 | ai_disclosure | pages [26] -->
m

<!-- b008573 | ai_disclosure | pages [26] -->
m

<!-- b008574 | ai_disclosure | pages [26] -->
m

<!-- b008575 | ai_disclosure | pages [26] -->
m

<!-- b008576 | ai_disclosure | pages [26] -->
m

<!-- b008577 | ai_disclosure | pages [26] -->
m

<!-- b008578 | ai_disclosure | pages [26] -->
m

<!-- b008579 | ai_disclosure | pages [26] -->
m

<!-- b008580 | ai_disclosure | pages [26] -->
m

<!-- b008581 | ai_disclosure | pages [26] -->
m

<!-- b008582 | ai_disclosure | pages [26] -->
m

<!-- b008583 | ai_disclosure | pages [26] -->
m

<!-- b008584 | ai_disclosure | pages [26] -->
m

<!-- b008585 | ai_disclosure | pages [26] -->
m

<!-- b008586 | ai_disclosure | pages [26] -->
m

<!-- b008587 | ai_disclosure | pages [26] -->
m

<!-- b008588 | ai_disclosure | pages [26] -->
m

<!-- b008589 | ai_disclosure | pages [26] -->
m

<!-- b008590 | ai_disclosure | pages [26] -->
m

<!-- b008591 | ai_disclosure | pages [26] -->
m

<!-- b008592 | ai_disclosure | pages [26] -->
m

<!-- b008593 | ai_disclosure | pages [26] -->
m

<!-- b008594 | ai_disclosure | pages [26] -->
m

<!-- b008595 | ai_disclosure | pages [26] -->
m

<!-- b008596 | ai_disclosure | pages [26] -->
m

<!-- b008597 | ai_disclosure | pages [26] -->
m

<!-- b008598 | ai_disclosure | pages [26] -->
m

<!-- b008599 | ai_disclosure | pages [26] -->
m

<!-- b008600 | ai_disclosure | pages [26] -->
m

<!-- b008601 | ai_disclosure | pages [26] -->
m

<!-- b008602 | ai_disclosure | pages [26] -->
m

<!-- b008603 | ai_disclosure | pages [26] -->
m

<!-- b008604 | ai_disclosure | pages [26] -->
m

<!-- b008605 | ai_disclosure | pages [26] -->
m

<!-- b008606 | ai_disclosure | pages [26] -->
m

<!-- b008607 | ai_disclosure | pages [26] -->
m

<!-- b008608 | ai_disclosure | pages [26] -->
m

<!-- b008609 | ai_disclosure | pages [26] -->
m

<!-- b008610 | ai_disclosure | pages [26] -->
m

<!-- b008611 | ai_disclosure | pages [26] -->
m

<!-- b008612 | ai_disclosure | pages [26] -->
m

<!-- b008613 | ai_disclosure | pages [26] -->
m

<!-- b008614 | ai_disclosure | pages [26] -->
m

<!-- b008615 | ai_disclosure | pages [26] -->
m

<!-- b008616 | ai_disclosure | pages [26] -->
m

<!-- b008617 | ai_disclosure | pages [26] -->
m

<!-- b008618 | ai_disclosure | pages [26] -->
m

<!-- b008619 | ai_disclosure | pages [26] -->
m

<!-- b008620 | ai_disclosure | pages [26] -->
m

<!-- b008621 | ai_disclosure | pages [26] -->
m

<!-- b008622 | ai_disclosure | pages [26] -->
m

<!-- b008623 | ai_disclosure | pages [26] -->
m

<!-- b008624 | ai_disclosure | pages [26] -->
m

<!-- b008625 | ai_disclosure | pages [26] -->
m

<!-- b008626 | ai_disclosure | pages [26] -->
m

<!-- b008627 | ai_disclosure | pages [26] -->
m

<!-- b008628 | ai_disclosure | pages [26] -->
m

<!-- b008629 | ai_disclosure | pages [26] -->
m

<!-- b008630 | ai_disclosure | pages [26] -->
m

<!-- b008631 | ai_disclosure | pages [26] -->
m

<!-- b008632 | ai_disclosure | pages [26] -->
m

<!-- b008633 | ai_disclosure | pages [26] -->
m

<!-- b008634 | ai_disclosure | pages [26] -->
m

<!-- b008635 | ai_disclosure | pages [26] -->
m

<!-- b008636 | ai_disclosure | pages [26] -->
m

<!-- b008637 | ai_disclosure | pages [26] -->
m

<!-- b008638 | ai_disclosure | pages [26] -->
m

<!-- b008639 | ai_disclosure | pages [26] -->
m

<!-- b008640 | ai_disclosure | pages [26] -->
m

<!-- b008641 | ai_disclosure | pages [26] -->
m

<!-- b008642 | ai_disclosure | pages [26] -->
m

<!-- b008643 | ai_disclosure | pages [26] -->
m

<!-- b008644 | ai_disclosure | pages [26] -->
m

<!-- b008645 | ai_disclosure | pages [26] -->
m

<!-- b008646 | ai_disclosure | pages [26] -->
m

<!-- b008647 | ai_disclosure | pages [26] -->
m

<!-- b008648 | ai_disclosure | pages [26] -->
m

<!-- b008649 | ai_disclosure | pages [26] -->
m

<!-- b008650 | ai_disclosure | pages [26] -->
m

<!-- b008651 | ai_disclosure | pages [26] -->
m

<!-- b008652 | ai_disclosure | pages [26] -->
m

<!-- b008653 | ai_disclosure | pages [26] -->
m

<!-- b008654 | ai_disclosure | pages [26] -->
m

<!-- b008655 | ai_disclosure | pages [26] -->
m

<!-- b008656 | ai_disclosure | pages [26] -->
m

<!-- b008657 | ai_disclosure | pages [26] -->
m

<!-- b008658 | ai_disclosure | pages [26] -->
m

<!-- b008659 | ai_disclosure | pages [26] -->
m

<!-- b008660 | ai_disclosure | pages [26] -->
m

<!-- b008661 | ai_disclosure | pages [26] -->
m

<!-- b008662 | ai_disclosure | pages [26] -->
m

<!-- b008663 | ai_disclosure | pages [26] -->
m

<!-- b008664 | ai_disclosure | pages [26] -->
m

<!-- b008665 | ai_disclosure | pages [26] -->
m

<!-- b008666 | ai_disclosure | pages [26] -->
m

<!-- b008667 | ai_disclosure | pages [26] -->
m

<!-- b008668 | ai_disclosure | pages [26] -->
m

<!-- b008669 | ai_disclosure | pages [26] -->
m

<!-- b008670 | ai_disclosure | pages [26] -->
m

<!-- b008671 | ai_disclosure | pages [26] -->
m

<!-- b008672 | ai_disclosure | pages [26] -->
m

<!-- b008673 | ai_disclosure | pages [26] -->
m

<!-- b008674 | ai_disclosure | pages [26] -->
m

<!-- b008675 | ai_disclosure | pages [26] -->
m

<!-- b008676 | ai_disclosure | pages [26] -->
m

<!-- b008677 | ai_disclosure | pages [26] -->
m

<!-- b008678 | ai_disclosure | pages [26] -->
m

<!-- b008679 | ai_disclosure | pages [26] -->
m

<!-- b008680 | ai_disclosure | pages [26] -->
m

<!-- b008681 | ai_disclosure | pages [26] -->
m

<!-- b008682 | ai_disclosure | pages [26] -->
m

<!-- b008683 | ai_disclosure | pages [26] -->
m

<!-- b008684 | ai_disclosure | pages [26] -->
m

<!-- b008685 | ai_disclosure | pages [26] -->
m

<!-- b008686 | ai_disclosure | pages [26] -->
m

<!-- b008687 | ai_disclosure | pages [26] -->
m

<!-- b008688 | ai_disclosure | pages [26] -->
m

<!-- b008689 | ai_disclosure | pages [26] -->
m

<!-- b008690 | ai_disclosure | pages [26] -->
m

<!-- b008691 | ai_disclosure | pages [26] -->
m

<!-- b008692 | ai_disclosure | pages [26] -->
m

<!-- b008693 | ai_disclosure | pages [26] -->
m

<!-- b008694 | ai_disclosure | pages [26] -->
m

<!-- b008695 | ai_disclosure | pages [26] -->
m

<!-- b008696 | ai_disclosure | pages [26] -->
m

<!-- b008697 | ai_disclosure | pages [26] -->
m

<!-- b008698 | ai_disclosure | pages [26] -->
m

<!-- b008699 | ai_disclosure | pages [26] -->
m

<!-- b008700 | ai_disclosure | pages [26] -->
m

<!-- b008701 | ai_disclosure | pages [26] -->
m

<!-- b008702 | ai_disclosure | pages [26] -->
m

<!-- b008703 | ai_disclosure | pages [26] -->
m

<!-- b008704 | ai_disclosure | pages [26] -->
m

<!-- b008705 | ai_disclosure | pages [26] -->
m

<!-- b008706 | ai_disclosure | pages [26] -->
m

<!-- b008707 | ai_disclosure | pages [26] -->
m

<!-- b008708 | ai_disclosure | pages [26] -->
m

<!-- b008709 | ai_disclosure | pages [26] -->
m

<!-- b008710 | ai_disclosure | pages [26] -->
m

<!-- b008711 | ai_disclosure | pages [26] -->
m

<!-- b008712 | ai_disclosure | pages [26] -->
m

<!-- b008713 | ai_disclosure | pages [26] -->
m

<!-- b008714 | ai_disclosure | pages [26] -->
m

<!-- b008715 | ai_disclosure | pages [26] -->
m

<!-- b008716 | ai_disclosure | pages [26] -->
m

<!-- b008717 | ai_disclosure | pages [26] -->
m

<!-- b008718 | ai_disclosure | pages [26] -->
m

<!-- b008719 | ai_disclosure | pages [26] -->
m

<!-- b008720 | ai_disclosure | pages [26] -->
m

<!-- b008721 | ai_disclosure | pages [26] -->
m

<!-- b008722 | ai_disclosure | pages [26] -->
m

<!-- b008723 | ai_disclosure | pages [26] -->
m

<!-- b008724 | ai_disclosure | pages [26] -->
m

<!-- b008725 | ai_disclosure | pages [26] -->
m

<!-- b008726 | ai_disclosure | pages [26] -->
m

<!-- b008727 | ai_disclosure | pages [26] -->
m

<!-- b008728 | ai_disclosure | pages [26] -->
m

<!-- b008729 | ai_disclosure | pages [26] -->
m

<!-- b008730 | ai_disclosure | pages [26] -->
m

<!-- b008731 | ai_disclosure | pages [26] -->
m

<!-- b008732 | ai_disclosure | pages [26] -->
m

<!-- b008733 | ai_disclosure | pages [26] -->
m

<!-- b008734 | ai_disclosure | pages [26] -->
m

<!-- b008735 | ai_disclosure | pages [26] -->
m

<!-- b008736 | ai_disclosure | pages [26] -->
m

<!-- b008737 | ai_disclosure | pages [26] -->
m

<!-- b008738 | ai_disclosure | pages [26] -->
m

<!-- b008739 | ai_disclosure | pages [26] -->
m

<!-- b008740 | ai_disclosure | pages [26] -->
m

<!-- b008741 | ai_disclosure | pages [26] -->
m

<!-- b008742 | ai_disclosure | pages [26] -->
m

<!-- b008743 | ai_disclosure | pages [26] -->
m

<!-- b008744 | ai_disclosure | pages [26] -->
m

<!-- b008745 | ai_disclosure | pages [26] -->
m

<!-- b008746 | ai_disclosure | pages [26] -->
m

<!-- b008747 | ai_disclosure | pages [26] -->
m

<!-- b008748 | ai_disclosure | pages [26] -->
m

<!-- b008749 | ai_disclosure | pages [26] -->
m

<!-- b008750 | ai_disclosure | pages [26] -->
m

<!-- b008751 | ai_disclosure | pages [26] -->
m

<!-- b008752 | ai_disclosure | pages [26] -->
m

<!-- b008753 | ai_disclosure | pages [26] -->
m

<!-- b008754 | ai_disclosure | pages [26] -->
m

<!-- b008755 | ai_disclosure | pages [26] -->
m

<!-- b008756 | ai_disclosure | pages [26] -->
m

<!-- b008757 | ai_disclosure | pages [26] -->
m

<!-- b008758 | ai_disclosure | pages [26] -->
m

<!-- b008759 | ai_disclosure | pages [26] -->
m

<!-- b008760 | ai_disclosure | pages [26] -->
m

<!-- b008761 | ai_disclosure | pages [26] -->
m

<!-- b008762 | ai_disclosure | pages [26] -->
m

<!-- b008763 | ai_disclosure | pages [26] -->
m

<!-- b008764 | ai_disclosure | pages [26] -->
m

<!-- b008765 | ai_disclosure | pages [26] -->
m

<!-- b008766 | ai_disclosure | pages [26] -->
m

<!-- b008767 | ai_disclosure | pages [26] -->
m

<!-- b008768 | ai_disclosure | pages [26] -->
m

<!-- b008769 | ai_disclosure | pages [26] -->
m

<!-- b008770 | ai_disclosure | pages [26] -->
m

<!-- b008771 | ai_disclosure | pages [26] -->
m

<!-- b008772 | ai_disclosure | pages [26] -->
m

<!-- b008773 | ai_disclosure | pages [26] -->
m

<!-- b008774 | ai_disclosure | pages [26] -->
m

<!-- b008775 | ai_disclosure | pages [26] -->
m

<!-- b008776 | ai_disclosure | pages [26] -->
m

<!-- b008777 | ai_disclosure | pages [26] -->
m

<!-- b008778 | ai_disclosure | pages [26] -->
m

<!-- b008779 | ai_disclosure | pages [26] -->
m

<!-- b008780 | ai_disclosure | pages [26] -->
m

<!-- b008781 | ai_disclosure | pages [26] -->
m

<!-- b008782 | ai_disclosure | pages [26] -->
m

<!-- b008783 | ai_disclosure | pages [26] -->
m

<!-- b008784 | ai_disclosure | pages [26] -->
m

<!-- b008785 | ai_disclosure | pages [26] -->
m

<!-- b008786 | ai_disclosure | pages [26] -->
m

<!-- b008787 | ai_disclosure | pages [26] -->
m

<!-- b008788 | ai_disclosure | pages [26] -->
m

<!-- b008789 | ai_disclosure | pages [26] -->
m

<!-- b008790 | ai_disclosure | pages [26] -->
m

<!-- b008791 | ai_disclosure | pages [26] -->
m

<!-- b008792 | ai_disclosure | pages [26] -->
m

<!-- b008793 | ai_disclosure | pages [26] -->
m

<!-- b008794 | ai_disclosure | pages [26] -->
m

<!-- b008795 | ai_disclosure | pages [26] -->
m

<!-- b008796 | ai_disclosure | pages [26] -->
m

<!-- b008797 | ai_disclosure | pages [26] -->
m

<!-- b008798 | ai_disclosure | pages [26] -->
m

<!-- b008799 | ai_disclosure | pages [26] -->
m

<!-- b008800 | ai_disclosure | pages [26] -->
m

<!-- b008801 | ai_disclosure | pages [26] -->
m

<!-- b008802 | ai_disclosure | pages [26] -->
m

<!-- b008803 | ai_disclosure | pages [26] -->
m

<!-- b008804 | ai_disclosure | pages [26] -->
m

<!-- b008805 | ai_disclosure | pages [26] -->
m

<!-- b008806 | ai_disclosure | pages [26] -->
m

<!-- b008807 | ai_disclosure | pages [26] -->
m

<!-- b008808 | ai_disclosure | pages [26] -->
m

<!-- b008809 | ai_disclosure | pages [26] -->
m

<!-- b008810 | ai_disclosure | pages [26] -->
m

<!-- b008811 | ai_disclosure | pages [26] -->
m

<!-- b008812 | ai_disclosure | pages [26] -->
m

<!-- b008813 | ai_disclosure | pages [26] -->
m

<!-- b008814 | ai_disclosure | pages [26] -->
Recommended the following reliable data sources:

<!-- b008815 | ai_disclosure | pages [26] -->
World Bank: Comprehensive global data on internet access, GDP, and educa-

<!-- b008816 | ai_disclosure | pages [26] -->
•

<!-- b008817 | ai_disclosure | pages [26] -->
tion.

<!-- b008818 | ai_disclosure | pages [26] -->
ITU: Specialized in ICT statistics, including internet and mobile penetration.

<!-- b008819 | ai_disclosure | pages [26] -->
•

<!-- b008820 | ai_disclosure | pages [26] -->
UNDP: Offers indices related to education and human development.

<!-- b008821 | ai_disclosure | pages [26] -->
•

<!-- b008822 | ai_disclosure | pages [26] -->
OECD: Focused on high-income countries, providing detailed socio-economic

<!-- b008823 | ai_disclosure | pages [26] -->
•

<!-- b008824 | ai_disclosure | pages [26] -->
data.

<!-- b008825 | ai_disclosure | pages [26] -->
UNESCO UIS: Dedicated to education statistics, including literacy and enroll-

<!-- b008826 | ai_disclosure | pages [26] -->
•

<!-- b008827 | ai_disclosure | pages [26] -->
ment rates.

<!-- b008828 | ai_disclosure | pages [26] -->
CIA World Factbook: General demographic data for global countries.

<!-- b008829 | ai_disclosure | pages [26] -->
•

<!-- b008830 | ai_disclosure | pages [26] -->
Kaggle: User-generated datasets suitable for research and analysis.

<!-- b008831 | ai_disclosure | pages [26] -->
•

<!-- b008832 | ai_disclosure | pages [26] -->
IMF: Primarily for economic indicators like GDP and income distribution.

<!-- b008833 | ai_disclosure | pages [26] -->
•

<!-- b008834 | ai_disclosure | pages [26] -->
Government Statistics Ofﬁces: Ofﬁcial national demographic and economic

<!-- b008835 | ai_disclosure | pages [26] -->
•

<!-- b008836 | ai_disclosure | pages [26] -->
statistics.

<!-- b008837 | ai_disclosure | pages [26] -->
Our World in Data: Combines data visualization with downloadable datasets

<!-- b008838 | ai_disclosure | pages [26] -->
•

<!-- b008839 | ai_disclosure | pages [26] -->
on demographics and technology.

<!-- b008840 | ai_disclosure | pages [26] -->
Query2: How should I prioritize these sources for data collection?

<!-- b008841 | ai_disclosure | pages [26] -->
Output:

<!-- b008842 | ai_disclosure | pages [26] -->
Guided to prioritize based on:

<!-- b008843 | ai_disclosure | pages [26] -->
Speciﬁc needs: For ICT, start with ITU; for education, use UNESCO UIS or

<!-- b008844 | ai_disclosure | pages [26] -->
•

<!-- b008845 | ai_disclosure | pages [26] -->
UNDP.

<!-- b008846 | ai_disclosure | pages [26] -->
Comprehensive datasets: World Bank and Our World in Data for multi-indicator

<!-- b008847 | ai_disclosure | pages [26] -->
•

<!-- b008848 | ai_disclosure | pages [26] -->
studies.

<!-- b008849 | heading | pages [26] -->
Cross-validation: Use multiple sources like OECD and national government

<!-- b008850 | prose | pages [26] -->
• sites for accuracy.

<!-- b008851 | prose | pages [26] -->
Query3: How can I set the height of an inserted image in LaTeX?

<!-- b008852 | prose | pages [26] -->
Output: You can set the height of an image by using the includegraphics command with parameters like height=5cm or scale=0.8. The width parameter can also control the image width.

<!-- b008853 | prose | pages [26] -->
Query4: How to adjust the spacing around section headings?

<!-- b008854 | prose | pages [26] -->
Output: Use the titlesec package and the titlespacing command to control spacing for section, subsection, and subsubsection headings. For example:

<!-- b008855 | prose | pages [26] -->
\titlespacing*{\section}{0pt}{10pt}{5pt}

<!-- b008856 | prose | pages [26] -->
Query3: Can you help me format a regression results table?

<!-- b008857 | prose | pages [26] -->
Output: Provided speciﬁc longtable and tabular environment code for clear and professional table formatting.

<!-- b008858 | prose | pages [26] -->
关注数学模型

<!-- b008859 | furniture | pages [26] -->
2

<!-- b008860 | furniture | pages [26] -->
MATHmodels

<!-- b008861 | furniture | pages [26] -->
获取更多资讯

<!-- b008862 | furniture | pages [27] -->
Team # 2521039

<!-- b008863 | prose | pages [27] -->
Overall Experience

<!-- b008864 | prose | pages [27] -->
1. ChatGPT provided highly relevant and authoritative data sources for collecting national demographic information. Its responses were well-structured and included:

<!-- b008865 | prose | pages [27] -->
• Direct access links to reliable datasets. • Speciﬁc use cases for each data source to ensure efﬁcient prioritization. • Practical recommendations for cross-verifying data from multiple sources.

<!-- b008866 | prose | pages [27] -->
By leveraging these recommendations, we gained a clearer understanding of reliable sources for demographic indicators, simplifying the data collection process.

<!-- b008867 | prose | pages [27] -->
2. ChatGPT demonstrated excellent capabilities in generating and supporting for-

<!-- b008868 | prose | pages [27] -->
微信公众号：数学模型

<!-- b008869 | prose | pages [27] -->
matting codes, particularly in:

<!-- b008870 | prose | pages [27] -->
• Providing detailed LaTeX formatting solutions and optimization tips. • Assisting in understanding complex commands (e.g., adjusting heading spac- ing, image dimensions). • Showing ﬂexibility and professionalism in designing and formatting tables.

<!-- b008871 | prose | pages [27] -->
Through multiple interactions, we successfully completed tasks like inserting im- ages, generating formulas, and optimizing documents.

<!-- b008872 | prose | pages [27] -->
Limitations and Suggestions

<!-- b008873 | prose | pages [27] -->
微信号：MATHmodels

<!-- b008874 | prose | pages [27] -->
• ChatGPT cannot validate the availability or format of speciﬁc datasets in real time. Users must manually explore the provided resources to determine if the data supports their research. • ChatGPT cannot directly verify the execution of LaTeX codes and only provides theoretical guidance.
