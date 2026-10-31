# P-C-2025-2510006-a0fb3dfb

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2025

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | title | pages [1] -->
微信公众号：数学模型

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
C

<!-- b000007 | title | pages [1] -->
2510006

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
2028 LA Olympics: Who Will Dominate the Medal

<!-- b000010 | title | pages [1] -->
Count?

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | title | pages [1] -->
微信号：MATHmodels

<!-- b000013 | prose | pages [1] -->
As the Olympic Games’ importance grows, the focus on medal standings across countries has surged, making Olympic medal prediction an exciting area of research. This paper aims to develop a comprehensive model to forecast the medal counts (including predicted values and conﬁdence intervals) for each country at the 2028 Olympics. We integrate linear regression, ARIMA (AutoRegressive Integrated Moving Average), and random forest models to predict both total and gold medal counts, providing a 90% conﬁdence interval. The ARIMA model captures trends and cycles, while the random forest model handles complex nonlinear relationships.

<!-- b000014 | prose | pages [1] -->
In Task 1, we categorized countries into three groups: host country, the U.S., medal- winning countries, and countries without medals. We used historical data from previous Olympics, linear regression, and average values to predict medal outcomes for both returning and new events. For new events, we used Monte Carlo simulations to estimate medal distributions. We forecasted the host country’s medals based on patterns from past hosts, and for countries without medals, we applied random forest and ARIMA (with parameters p=0, q=2, d=0) to estimate gold medals. By combining linear regression with event participation data, we calculated expected medal counts and used a Poisson distribution to derive 90% conﬁdence intervals. Our results showed that the U.S. is likely to see at least a 95% probability of a medal increase, while China, losing some dominant events, is predicted to regress.

<!-- b000015 | prose | pages [1] -->
In Task 2, we used Fisher’s exact test to analyze the impact of "great coaches," exem- pliﬁed by Lang Ping and Béla Károlyi, on medal outcomes. We recommended "great coaches" for Chinas women’s volleyball team, Indias athletics, and Brazils gymnastics, providing the rationale for these suggestions.

<!-- b000016 | prose | pages [1] -->
In Task 3, we examined medal distribution across sports and advised smaller countries on improving their chances, considering factors like GDP. We found a strong positive correlation between a countrys economic strength and its medal count.

<!-- b000017 | prose | pages [1] -->
Overall, our model provides reliable predictions of medal counts and conﬁdence intervals for the 2028 Olympics. While uncertainties remain for countries with fewer medals, the predictions for top medal winners are robust.

<!-- b000018 | keywords | pages [1] -->
Keywords: ARIMA, Random Forest, Linear Regression, Olympic Medal Predic-

<!-- b000019 | prose | pages [1] -->
tion, Great Coach Eﬀect, Poisson Distribution.

<!-- b000020 | furniture | pages [2] -->
Page 1

<!-- b000021 | furniture | pages [2] -->
Team # 2510006

<!-- b000022 | heading | pages [2] -->
Contents

<!-- b000023 | contents | pages [2] -->
模型

<!-- b000024 | heading | pages [2] -->
1 Introduction

<!-- b000025 | prose | pages [2] -->
2

<!-- b000026 | heading | pages [2] -->
Background

<!-- b000027 | prose | pages [2] -->
1.1 2

<!-- b000028 | prose | pages [2] -->
1.2 2 Problem Restatement .

<!-- b000029 | heading | pages [2] -->
Notations & Assumputions

<!-- b000030 | prose | pages [2] -->
2 4

<!-- b000031 | heading | pages [2] -->
Data Processing

<!-- b000032 | prose | pages [2] -->
5 3

<!-- b000033 | prose | pages [2] -->
Clustering Analysis 5 3.1

<!-- b000034 | prose | pages [2] -->
3.2 Country Classification 5

<!-- b000035 | prose | pages [2] -->
Event Addition and Removal 3.3 6

<!-- b000036 | prose | pages [2] -->
Task 1: Olympic Medal Prediction and Analysis 6

<!-- b000037 | prose | pages [2] -->
2028 Medal Table Prediction . 4.1 6

<!-- b000038 | prose | pages [2] -->
Countries with Previous Medals (Non-Host Countries) 4.1.1 6

<!-- b000039 | prose | pages [2] -->
Host Country: United States . 4.1.2 8

<!-- b000040 | prose | pages [2] -->
Prediction for Countries Winning Medals for the First Time 4.1.3 10

<!-- b000041 | heading | pages [2] -->
4.2 Analysis of the Relationship Between Events and Medals

<!-- b000042 | prose | pages [2] -->
16

<!-- b000043 | prose | pages [2] -->
Task 2: Great Coaches 17 5

<!-- b000044 | heading | pages [2] -->
5.1 Evidence of the Great Coach Effect

<!-- b000045 | prose | pages [2] -->
17

<!-- b000046 | prose | pages [2] -->
Selection of Three Countries and Specific Sports 19 5.2

<!-- b000047 | heading | pages [2] -->
Task 3: Recommendations

<!-- b000048 | prose | pages [2] -->
20

<!-- b000049 | heading | pages [2] -->
Model Evaluation

<!-- b000050 | prose | pages [2] -->
21 7

<!-- b000051 | heading | pages [2] -->
7.1 Sensitivity Analysis

<!-- b000052 | prose | pages [2] -->
21

<!-- b000053 | heading | pages [2] -->
Model Evaluation

<!-- b000054 | prose | pages [2] -->
22

<!-- b000055 | heading | pages [2] -->
Reference

<!-- b000056 | references | pages [2] -->
24

<!-- b000057 | references | pages [2] -->
关注数学模型

<!-- b000058 | furniture | pages [2] -->
获取更多资讯

<!-- b000059 | furniture | pages [3] -->
Team # 2510006

<!-- b000060 | furniture | pages [3] -->
Page 2

<!-- b000061 | heading | pages [3] -->
1 Introduction

<!-- b000062 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000063 | heading | pages [3] -->
1.1 Background

<!-- b000064 | prose | pages [3] -->
The Olympic Games are a global spectacle where nations vie for medals. While giants like the USA and China lead the medal table, smaller countries such as Albania and Cape Verde have made history, with both winning their ﬁrst gold medals at the 2024 Paris Olympics. This highlights not just their growing sports prowess, but their rising prominence on the world stage.

<!-- b000065 | prose | pages [3] -->
Predicting future Olympic medal outcomes is complex. Current models often focus solely on athlete performance and past results, missing key factors like national investments, 微信号：MATHmodels event changes, and shifting competition trends. A more comprehensive model could greatly enhance predictions, particularly for the 2028 Olympics.

<!-- b000066 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000067 | prose | pages [3] -->
We are provided with historical data on past Olympics, including host countries, events, and detailed athlete performance, categorized by sport and medal type. The challenge is to build a model that can predict medal outcomes for the 2028 Olympics and provide insights into the underlying factors.

<!-- b000068 | prose | pages [3] -->
Task 1: Build a model to predict the total and gold medal counts for each country in 2028, with 90% conﬁdence intervals.

<!-- b000069 | prose | pages [3] -->
• Compare the predictions with actual data from the 2024 Olympics to identify countries likely to see increases or decreases in their medal counts.

<!-- b000070 | prose | pages [3] -->
• Estimate the probability of each non-medal countries that will win their ﬁrst medals in 2028.

<!-- b000071 | prose | pages [3] -->
• Explore the relationship between sports types, event numbers, and medal distributions across nations.

<!-- b000072 | prose | pages [3] -->
• Analyze the potential impact of new sports introduced by the host country on the overall medal standings.

<!-- b000073 | prose | pages [3] -->
Task 2: "The Great Coach Eﬀect"

<!-- b000074 | prose | pages [3] -->
• Investigate the impact of great coaches on the medal performance of a nation, by examining changes before and after a coachs appointment.

<!-- b000075 | prose | pages [3] -->
• Quantify the eﬀect of a coach’s inﬂuence on medal counts.

<!-- b000076 | prose | pages [3] -->
• Identify three countries where hiring a coach could make a signiﬁcant diﬀerence in their performance.

<!-- b000077 | heading | pages [3] -->
Task 3: Insights from the Model

<!-- b000078 | furniture | pages [4] -->
Team # 2510006

<!-- b000079 | furniture | pages [4] -->
Page 3

<!-- b000080 | prose | pages [4] -->
• Explore the relationships between medal distributions, country-speciﬁc factors (e.g.

<!-- b000081 | prose | pages [4] -->
sports events, economic development), and national strengths.

<!-- b000082 | prose | pages [4] -->
• Help smaller countries optimize their medal chances despite resource limitations.

<!-- b000083 | prose | pages [4] -->
• Explore the correlation between per capita medals and per capita GDP.

<!-- b000084 | prose | pages [4] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b000085 | caption | pages [4] -->
Figure 1: Our work

<!-- b000086 | prose | pages [4] -->
关注数学模型

<!-- b000087 | furniture | pages [4] -->
2

<!-- b000088 | furniture | pages [4] -->
MATHmodels

<!-- b000089 | furniture | pages [4] -->
获取更多资讯

<!-- b000090 | furniture | pages [5] -->
Team # 2510006

<!-- b000091 | furniture | pages [5] -->
Page 4

<!-- b000092 | heading | pages [5] -->
2 Notations & Assumputions

<!-- b000093 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000094 | caption | pages [5] -->
Table 1: Notations

<!-- b000095 | heading | pages [5] -->
Symbols

<!-- b000096 | prose | pages [5] -->
Description

<!-- b000097 | prose | pages [5] -->
Class 1 ~3 1:Aquatic Sports 2:Ball Sports 3:Track & Field Class 4 ~6 4:Gymnastics & Acrobatics 5:Martial Arts 6:Motorsport & Racing ai jk/bi jk/ci for one country, if Class i year 1996 + 4k won gold/silver/bronze, jk number of medals in year 2000 + 4k;j = 1, 2, 3 refers gold,silver and bronze di jk/ei for one country, if Class i year 1996 + 4k won no medal/didn’t participate, jk 微信号：MATHmodels number of medals in year 2000 + 4k;j = 1, 2, 3 refers gold,silver and bronze fi for one country, the expectation of all medals in all new events year 2028 ai j/bi j/ci for one country, Class i year 2024 won gold/silver/bronze, j the predicted value of medals in year 2028;j = 1, 2, 3 refers gold,silver and bronze di j/ei for one country, Class i year 2024 won no medal/didn’t participate, j the predicted value of medals in year 2028;j = 1, 2, 3 refers gold,silver and bronze G/S/B for one country, the expectation of gold/silver/bronze in all events year 2028 T for one country, the expectation of total medals year 2028 ¯G / ¯S / ¯B for one country, the predicted value of gold/silver/bronze in all events year 2028 ¯T for one country, the predicted value of total medals year 2028 [Gmin, Gmax] for one country, the predicted value interval of gold in all events year 2028 [Tmin, Tmax] for one country, the predicted value interval of total medals year 2028 gi the total medals of the ith host in ith Oly.(without new events) mi/ni the total medals of the ith host in (i-1)th/(i+1)th Oly. (consider special cases) Tboost the weighed increment of the host Told/Tnew/T the total medals (old/new/all events) of USA year 2028 u1˜ut−2 ﬁrst medal country(no disintegration) in year 1904 ~2024 v1˜v9 ﬁrst medal country(disintegration) in year 1992 ~2024 aij the number of involved events of ith none-medal country year 1996 + 4j ai the predicted number of involved events of ith none-medal country year 2028 Li the expectation of medals of ith none-medal country year 2028 qi the probability of winning medals of ith none-medal country year 2028 xij/uij the percentage/total number of the jth country Class i medals in year 1896 ~2024 ri the total number of Class i medals in year 1896 ~2024 dij the diﬀerence of Class i and Class j medals ′ d the correlation of Class i and Class j ij ′ ′ x ij/u the percentage/total number of the jth event i medals in year 1896 ~2024 ij ′ r the total number of event i medals in year 1896 ~2024 i t medals after changing great coaches

<!-- b000098 | prose | pages [5, 6] -->
Considering the complexity of factors involved in the upcoming 2028 Los Angeles Olympics, we make reasonable assumptions to simplify the model. Each assumption is followed by its corresponding explanation: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m • Assumption 1: All countries will be unaffected by factors like politics or doping and will participate with complete teams.

<!-- b000099 | furniture | pages [5] -->
m

<!-- b000100 | furniture | pages [5] -->
m

<!-- b000101 | furniture | pages [5] -->
m

<!-- b000102 | furniture | pages [5] -->
m

<!-- b000103 | furniture | pages [5] -->
m

<!-- b000104 | furniture | pages [5] -->
m

<!-- b000105 | furniture | pages [5] -->
m

<!-- b000106 | furniture | pages [5] -->
m

<!-- b000107 | furniture | pages [5] -->
m

<!-- b000108 | furniture | pages [5] -->
m

<!-- b000109 | furniture | pages [5] -->
m

<!-- b000110 | furniture | pages [5] -->
m

<!-- b000111 | furniture | pages [5] -->
m

<!-- b000112 | furniture | pages [5] -->
m

<!-- b000113 | furniture | pages [5] -->
m

<!-- b000114 | furniture | pages [5] -->
m

<!-- b000115 | furniture | pages [5] -->
m

<!-- b000116 | furniture | pages [5] -->
m

<!-- b000117 | furniture | pages [5] -->
m

<!-- b000118 | furniture | pages [5] -->
m

<!-- b000119 | furniture | pages [5] -->
m

<!-- b000120 | furniture | pages [5] -->
m

<!-- b000121 | furniture | pages [5] -->
m

<!-- b000122 | furniture | pages [5] -->
m

<!-- b000123 | furniture | pages [5] -->
m

<!-- b000124 | furniture | pages [5] -->
m

<!-- b000125 | furniture | pages [5] -->
m

<!-- b000126 | furniture | pages [5] -->
m

<!-- b000127 | furniture | pages [5] -->
m

<!-- b000128 | furniture | pages [5] -->
m

<!-- b000129 | furniture | pages [5] -->
m

<!-- b000130 | furniture | pages [5] -->
m

<!-- b000131 | furniture | pages [5] -->
m

<!-- b000132 | furniture | pages [5] -->
m

<!-- b000133 | furniture | pages [5] -->
m

<!-- b000134 | furniture | pages [5] -->
m

<!-- b000135 | furniture | pages [5] -->
m

<!-- b000136 | furniture | pages [5] -->
m

<!-- b000137 | furniture | pages [5] -->
m

<!-- b000138 | furniture | pages [5] -->
m

<!-- b000139 | furniture | pages [5] -->
m

<!-- b000140 | furniture | pages [5] -->
m

<!-- b000141 | furniture | pages [5] -->
m

<!-- b000142 | furniture | pages [5] -->
m

<!-- b000143 | furniture | pages [5] -->
m

<!-- b000144 | furniture | pages [5] -->
m

<!-- b000145 | furniture | pages [5] -->
m

<!-- b000146 | furniture | pages [5] -->
m

<!-- b000147 | furniture | pages [5] -->
m

<!-- b000148 | furniture | pages [5] -->
m

<!-- b000149 | furniture | pages [5] -->
m

<!-- b000150 | furniture | pages [5] -->
m

<!-- b000151 | furniture | pages [5] -->
m

<!-- b000152 | furniture | pages [5] -->
m

<!-- b000153 | furniture | pages [5] -->
m

<!-- b000154 | furniture | pages [5] -->
m

<!-- b000155 | furniture | pages [5] -->
m

<!-- b000156 | furniture | pages [5] -->
m

<!-- b000157 | furniture | pages [5] -->
m

<!-- b000158 | furniture | pages [5] -->
m

<!-- b000159 | furniture | pages [5] -->
m

<!-- b000160 | furniture | pages [5] -->
m

<!-- b000161 | furniture | pages [5] -->
m

<!-- b000162 | furniture | pages [5] -->
m

<!-- b000163 | furniture | pages [5] -->
m

<!-- b000164 | furniture | pages [5] -->
m

<!-- b000165 | furniture | pages [5] -->
m

<!-- b000166 | furniture | pages [5] -->
m

<!-- b000167 | furniture | pages [5] -->
m

<!-- b000168 | furniture | pages [5] -->
m

<!-- b000169 | furniture | pages [5] -->
m

<!-- b000170 | furniture | pages [5] -->
m

<!-- b000171 | furniture | pages [5] -->
m

<!-- b000172 | furniture | pages [5] -->
m

<!-- b000173 | furniture | pages [5] -->
m

<!-- b000174 | furniture | pages [5] -->
m

<!-- b000175 | furniture | pages [5] -->
m

<!-- b000176 | furniture | pages [5] -->
m

<!-- b000177 | furniture | pages [5] -->
m

<!-- b000178 | furniture | pages [5] -->
m

<!-- b000179 | furniture | pages [5] -->
m

<!-- b000180 | furniture | pages [5] -->
m

<!-- b000181 | furniture | pages [5] -->
m

<!-- b000182 | furniture | pages [5] -->
m

<!-- b000183 | furniture | pages [5] -->
m

<!-- b000184 | furniture | pages [5] -->
m

<!-- b000185 | furniture | pages [5] -->
m

<!-- b000186 | furniture | pages [5] -->
m

<!-- b000187 | furniture | pages [5] -->
m

<!-- b000188 | furniture | pages [5] -->
m

<!-- b000189 | furniture | pages [5] -->
m

<!-- b000190 | furniture | pages [5] -->
m

<!-- b000191 | furniture | pages [5] -->
m

<!-- b000192 | furniture | pages [5] -->
m

<!-- b000193 | furniture | pages [5] -->
m

<!-- b000194 | furniture | pages [5] -->
m

<!-- b000195 | furniture | pages [5] -->
m

<!-- b000196 | furniture | pages [5] -->
m

<!-- b000197 | furniture | pages [5] -->
m

<!-- b000198 | furniture | pages [5] -->
m

<!-- b000199 | furniture | pages [5] -->
m

<!-- b000200 | furniture | pages [5] -->
m

<!-- b000201 | furniture | pages [5] -->
m

<!-- b000202 | furniture | pages [5] -->
m

<!-- b000203 | furniture | pages [5] -->
m

<!-- b000204 | furniture | pages [5] -->
m

<!-- b000205 | furniture | pages [5] -->
m

<!-- b000206 | furniture | pages [5] -->
m

<!-- b000207 | furniture | pages [5] -->
m

<!-- b000208 | furniture | pages [5] -->
m

<!-- b000209 | furniture | pages [5] -->
m

<!-- b000210 | furniture | pages [5] -->
m

<!-- b000211 | furniture | pages [5] -->
m

<!-- b000212 | furniture | pages [5] -->
m

<!-- b000213 | furniture | pages [5] -->
m

<!-- b000214 | furniture | pages [5] -->
m

<!-- b000215 | furniture | pages [5] -->
m

<!-- b000216 | furniture | pages [5] -->
m

<!-- b000217 | furniture | pages [5] -->
m

<!-- b000218 | furniture | pages [5] -->
m

<!-- b000219 | furniture | pages [5] -->
m

<!-- b000220 | furniture | pages [5] -->
m

<!-- b000221 | furniture | pages [5] -->
m

<!-- b000222 | furniture | pages [5] -->
m

<!-- b000223 | furniture | pages [5] -->
m

<!-- b000224 | furniture | pages [5] -->
m

<!-- b000225 | furniture | pages [5] -->
m

<!-- b000226 | furniture | pages [5] -->
m

<!-- b000227 | furniture | pages [5] -->
m

<!-- b000228 | furniture | pages [5] -->
m

<!-- b000229 | furniture | pages [5] -->
m

<!-- b000230 | furniture | pages [5] -->
m

<!-- b000231 | furniture | pages [5] -->
m

<!-- b000232 | furniture | pages [5] -->
m

<!-- b000233 | furniture | pages [5] -->
m

<!-- b000234 | furniture | pages [5] -->
m

<!-- b000235 | furniture | pages [5] -->
m

<!-- b000236 | furniture | pages [5] -->
m

<!-- b000237 | furniture | pages [5] -->
m

<!-- b000238 | furniture | pages [5] -->
m

<!-- b000239 | furniture | pages [5] -->
m

<!-- b000240 | furniture | pages [5] -->
m

<!-- b000241 | furniture | pages [5] -->
m

<!-- b000242 | furniture | pages [5] -->
m

<!-- b000243 | furniture | pages [5] -->
m

<!-- b000244 | furniture | pages [5] -->
m

<!-- b000245 | furniture | pages [5] -->
m

<!-- b000246 | furniture | pages [5] -->
m

<!-- b000247 | furniture | pages [5] -->
m

<!-- b000248 | furniture | pages [5] -->
m

<!-- b000249 | furniture | pages [5] -->
m

<!-- b000250 | furniture | pages [5] -->
m

<!-- b000251 | furniture | pages [5] -->
m

<!-- b000252 | furniture | pages [5] -->
m

<!-- b000253 | furniture | pages [5] -->
m

<!-- b000254 | furniture | pages [5] -->
m

<!-- b000255 | furniture | pages [5] -->
m

<!-- b000256 | furniture | pages [5] -->
m

<!-- b000257 | furniture | pages [5] -->
m

<!-- b000258 | furniture | pages [5] -->
m

<!-- b000259 | furniture | pages [5] -->
m

<!-- b000260 | furniture | pages [5] -->
m

<!-- b000261 | furniture | pages [5] -->
m

<!-- b000262 | furniture | pages [5] -->
m

<!-- b000263 | furniture | pages [5] -->
m

<!-- b000264 | furniture | pages [5] -->
m

<!-- b000265 | furniture | pages [5] -->
m

<!-- b000266 | furniture | pages [5] -->
m

<!-- b000267 | furniture | pages [5] -->
m

<!-- b000268 | furniture | pages [5] -->
m

<!-- b000269 | furniture | pages [5] -->
m

<!-- b000270 | furniture | pages [5] -->
m

<!-- b000271 | furniture | pages [5] -->
m

<!-- b000272 | furniture | pages [5] -->
m

<!-- b000273 | furniture | pages [5] -->
m

<!-- b000274 | furniture | pages [5] -->
m

<!-- b000275 | furniture | pages [5] -->
m

<!-- b000276 | furniture | pages [5] -->
m

<!-- b000277 | furniture | pages [5] -->
m

<!-- b000278 | furniture | pages [5] -->
m

<!-- b000279 | furniture | pages [5] -->
m

<!-- b000280 | furniture | pages [5] -->
m

<!-- b000281 | furniture | pages [5] -->
m

<!-- b000282 | furniture | pages [5] -->
m

<!-- b000283 | furniture | pages [5] -->
m

<!-- b000284 | furniture | pages [5] -->
m

<!-- b000285 | furniture | pages [5] -->
m

<!-- b000286 | furniture | pages [5] -->
m

<!-- b000287 | furniture | pages [5] -->
m

<!-- b000288 | furniture | pages [5] -->
m

<!-- b000289 | furniture | pages [5] -->
m

<!-- b000290 | furniture | pages [5] -->
m

<!-- b000291 | furniture | pages [5] -->
m

<!-- b000292 | furniture | pages [5] -->
m

<!-- b000293 | furniture | pages [5] -->
m

<!-- b000294 | furniture | pages [5] -->
m

<!-- b000295 | furniture | pages [5] -->
m

<!-- b000296 | furniture | pages [5] -->
m

<!-- b000297 | furniture | pages [5] -->
m

<!-- b000298 | furniture | pages [5] -->
m

<!-- b000299 | furniture | pages [5] -->
m

<!-- b000300 | furniture | pages [5] -->
m

<!-- b000301 | furniture | pages [5] -->
m

<!-- b000302 | furniture | pages [5] -->
m

<!-- b000303 | furniture | pages [5] -->
m

<!-- b000304 | furniture | pages [5] -->
m

<!-- b000305 | furniture | pages [5] -->
m

<!-- b000306 | furniture | pages [5] -->
m

<!-- b000307 | furniture | pages [5] -->
m

<!-- b000308 | furniture | pages [5] -->
m

<!-- b000309 | furniture | pages [5] -->
m

<!-- b000310 | furniture | pages [5] -->
m

<!-- b000311 | furniture | pages [5] -->
m

<!-- b000312 | furniture | pages [5] -->
m

<!-- b000313 | furniture | pages [5] -->
m

<!-- b000314 | furniture | pages [5] -->
m

<!-- b000315 | furniture | pages [5] -->
m

<!-- b000316 | furniture | pages [5] -->
m

<!-- b000317 | furniture | pages [5] -->
m

<!-- b000318 | furniture | pages [5] -->
m

<!-- b000319 | furniture | pages [5] -->
m

<!-- b000320 | furniture | pages [5] -->
m

<!-- b000321 | furniture | pages [5] -->
m

<!-- b000322 | furniture | pages [5] -->
m

<!-- b000323 | furniture | pages [5] -->
m

<!-- b000324 | furniture | pages [5] -->
m

<!-- b000325 | furniture | pages [5] -->
m

<!-- b000326 | furniture | pages [5] -->
m

<!-- b000327 | furniture | pages [5] -->
m

<!-- b000328 | furniture | pages [5] -->
m

<!-- b000329 | furniture | pages [5] -->
m

<!-- b000330 | furniture | pages [5] -->
m

<!-- b000331 | furniture | pages [5] -->
m

<!-- b000332 | furniture | pages [5] -->
m

<!-- b000333 | furniture | pages [5] -->
m

<!-- b000334 | furniture | pages [5] -->
m

<!-- b000335 | furniture | pages [5] -->
m

<!-- b000336 | furniture | pages [5] -->
m

<!-- b000337 | furniture | pages [5] -->
m

<!-- b000338 | furniture | pages [5] -->
m

<!-- b000339 | furniture | pages [5] -->
m

<!-- b000340 | furniture | pages [5] -->
m

<!-- b000341 | furniture | pages [5] -->
m

<!-- b000342 | furniture | pages [5] -->
m

<!-- b000343 | furniture | pages [5] -->
m

<!-- b000344 | furniture | pages [5] -->
m

<!-- b000345 | furniture | pages [5] -->
m

<!-- b000346 | furniture | pages [5] -->
m

<!-- b000347 | furniture | pages [5] -->
m

<!-- b000348 | furniture | pages [5] -->
m

<!-- b000349 | furniture | pages [5] -->
m

<!-- b000350 | furniture | pages [5] -->
m

<!-- b000351 | furniture | pages [5] -->
m

<!-- b000352 | furniture | pages [5] -->
m

<!-- b000353 | furniture | pages [5] -->
m

<!-- b000354 | furniture | pages [5] -->
m

<!-- b000355 | furniture | pages [5] -->
m

<!-- b000356 | furniture | pages [5] -->
m

<!-- b000357 | furniture | pages [5] -->
m

<!-- b000358 | furniture | pages [5] -->
m

<!-- b000359 | furniture | pages [5] -->
m

<!-- b000360 | furniture | pages [5] -->
m

<!-- b000361 | furniture | pages [5] -->
m

<!-- b000362 | furniture | pages [5] -->
m

<!-- b000363 | furniture | pages [5] -->
m

<!-- b000364 | furniture | pages [5] -->
m

<!-- b000365 | furniture | pages [5] -->
m

<!-- b000366 | furniture | pages [5] -->
m

<!-- b000367 | furniture | pages [5] -->
m

<!-- b000368 | furniture | pages [5] -->
m

<!-- b000369 | furniture | pages [5] -->
m

<!-- b000370 | furniture | pages [5] -->
m

<!-- b000371 | furniture | pages [5] -->
m

<!-- b000372 | furniture | pages [5] -->
m

<!-- b000373 | furniture | pages [5] -->
m

<!-- b000374 | furniture | pages [5] -->
m

<!-- b000375 | furniture | pages [5] -->
m

<!-- b000376 | furniture | pages [5] -->
m

<!-- b000377 | furniture | pages [5] -->
m

<!-- b000378 | furniture | pages [5] -->
m

<!-- b000379 | furniture | pages [5] -->
m

<!-- b000380 | furniture | pages [5] -->
m

<!-- b000381 | furniture | pages [5] -->
m

<!-- b000382 | furniture | pages [5] -->
m

<!-- b000383 | furniture | pages [5] -->
m

<!-- b000384 | furniture | pages [5] -->
m

<!-- b000385 | furniture | pages [5] -->
m

<!-- b000386 | furniture | pages [5] -->
m

<!-- b000387 | furniture | pages [5] -->
m

<!-- b000388 | furniture | pages [5] -->
m

<!-- b000389 | furniture | pages [5] -->
m

<!-- b000390 | furniture | pages [5] -->
m

<!-- b000391 | furniture | pages [5] -->
m

<!-- b000392 | furniture | pages [5] -->
m

<!-- b000393 | furniture | pages [5] -->
m

<!-- b000394 | furniture | pages [5] -->
m

<!-- b000395 | furniture | pages [5] -->
m

<!-- b000396 | furniture | pages [5] -->
m

<!-- b000397 | furniture | pages [5] -->
m

<!-- b000398 | furniture | pages [5] -->
m

<!-- b000399 | furniture | pages [5] -->
m

<!-- b000400 | furniture | pages [5] -->
m

<!-- b000401 | furniture | pages [5] -->
m

<!-- b000402 | furniture | pages [5] -->
m

<!-- b000403 | furniture | pages [5] -->
m

<!-- b000404 | furniture | pages [5] -->
m

<!-- b000405 | furniture | pages [5] -->
m

<!-- b000406 | furniture | pages [5] -->
m

<!-- b000407 | furniture | pages [5] -->
m

<!-- b000408 | furniture | pages [5] -->
m

<!-- b000409 | furniture | pages [5] -->
m

<!-- b000410 | furniture | pages [5] -->
m

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

<!-- b000423 | furniture | pages [6] -->
Page 5

<!-- b000424 | furniture | pages [6] -->
Team # 2510006

<!-- b000426 | prose | pages [6] -->
- Explanation: This ensures that external factors do not impact the analysis of sports performance.

<!-- b000427 | prose | pages [6] -->
• Assumption 2: The United States will add five new sports for the 2028 Olympics:

<!-- b000428 | prose | pages [6] -->
Baseball/Softball, Lacrosse, Cricket, Squash, and Flag Football, totaling ten events.(Men and Women) And all are conducted as knockout tournaments.

<!-- b000429 | prose | pages [6] -->
- Explanation: This is based on IOC's preliminary discussions on adding new sports for the upcoming Olympics.

<!-- b000430 | prose | pages [6] -->
• Assumption 3: Four sports (Breakdancing, Boxing, Weightlifting, and Modern Pen- tathlon) will be removed from the Olympics.

<!-- b000431 | prose | pages [6] -->
- Explanation: These sports are likely to be excluded based on IOC's review and changing interests.

<!-- b000432 | prose | pages [6] -->
• Assumption 4: The athletes' nationality will remain unchanged.

<!-- b000433 | prose | pages [6] -->
- Explanation: This assumption maintains a consistent basis for comparing ath- lete performance by country.

<!-- b000434 | prose | pages [6] -->
3Data Processing

<!-- b000435 | heading | pages [6] -->
3.1 Clustering Analysis

<!-- b000436 | prose | pages [6] -->
A country's Olympic performance depends on its proficiency in various sports,but for 70+ events, it's not practical to analyze all. To predict its medal count, we group events into broader categories due to the large number of Olympic events.

<!-- b000437 | prose | pages [6] -->
We assume each country excels in one or more major sports categories. Clustering anal- ysis helps identify these strengths and groups similar events together.

<!-- b000438 | prose | pages [6] -->
We construct a matrix with countries as rows and events as columns, where the values represent medal-winning rates. K-means clustering uses these rates to group similar events. The optimal number of clusters, K = 6, is determined using the elbow method and literature insights. Misclassified points are manually corrected for accuracy.

<!-- b000439 | prose | pages [6] -->
The clustering visualization is shown below:

<!-- b000440 | heading | pages [6] -->
3.2 Country Classification

<!-- b000441 | prose | pages [6] -->
Countries are divided into none-medal and medal-winning. For none-medal countries, we predict the chance of them winning their first medal. Host countries are analyzed sepa- rately to account for their performance boost. We refine the model to handle missing data from countries that skipped certain Games.

<!-- b000442 | prose | pages [6, 7] -->
关注数学模型 Sports Distribution by Category (K-means) Category 3.5 ● Track & Field Gymnastics & Acrobatics ● Aquatic Sports Motorsport & Racing Gymnastics & Acrobatics Ball Sports 3.0 Martial Arts 0

<!-- b000443 | furniture | pages [6] -->
获取更多资讯

<!-- b000444 | furniture | pages [7] -->
Page 6

<!-- b000445 | furniture | pages [7] -->
Team # 2510006

<!-- b000447 | prose | pages [7] -->
2.5 0 ● T Feid Aquatic Sports Motorsport & Racing ● ● 1.5 ● 0 1.0 ● 0 ● Martial Arts 0.5 ● 2 3 5 x O

<!-- b000448 | caption | pages [7] -->
Figure 2: Sports Distribution Classification (K-means)

<!-- b000449 | heading | pages [7] -->
3.3 Event Addition and Removal

<!-- b000450 | prose | pages [7] -->
New Olympic events lack historical data, so we use current country rankings for pre- diction. Discontinued events are excluded from the dataset to prevent them from affecting M future predictions.

<!-- b000451 | prose | pages [7] -->
Task 1: Olympic Medal Prediction and Analysis

<!-- b000452 | prose | pages [7] -->
2028 Medal Table Prediction 4.1

<!-- b000453 | heading | pages [7] -->
4.1.1 Countries with Previous Medals (Non-Host Countries)

<!-- b000454 | prose | pages [7] -->
● Old Events We classify all events into six major categories with K-means method as men- tioned before. Then, we analyze the data of athletes from each country within these cate- gories.

<!-- b000455 | prose | pages [7] -->
Given that athletes often retain their medals in consecutive Olympic Games, our strategy is to use the results from the previous Olympic Games to predict the performances of athletes in the upcoming Games. We define the following variables and indices:

<!-- b000456 | prose | pages [7] -->
Let i represent the above categories of sports: f1 : R → item (where Water Sports, Ball Sports, Track and Field, Technical Events, Combat Sports, and Racing Events correspond to numbers 1 to 6).

<!-- b000457 | prose | pages [7] -->
Let j represent the outcomes in the next Olympic Games: f2 : 1 → gold, 2 → silver, 3 → bronze.

<!-- b000458 | prose | pages [7] -->
Let k represent the previous Olympic year: f3 : R → R, f3(k) = 4k + 1996.

<!-- b000459 | prose | pages [7, 8] -->
Symbols a, b, c, d, and e represent the medal types or absence thereof for the athletes in the previous Games: - a represents gold medals, - b represents silver medals, - c repre- sents bronze medals, - d represents non-medal athletes, - e represents athletes who did not participate in the previous Games.

<!-- b000460 | furniture | pages [8] -->
Team # 2510006

<!-- b000461 | furniture | pages [8] -->
Page 7

<!-- b000463 | prose | pages [8] -->
We deﬁne ai jk as the total number of athletes who won gold in the previous Games in category i and who win medal j (gold, silver, or bronze) in the following Games. Similarly, we deﬁne bi jk, ci jk, and di jk for silver, bronze, and non-medal outcomes, respectively.

<!-- b000464 | prose | pages [8] -->
To explore whether the number of medals in consecutive Olympic Games is related to the year, we propose diﬀerent prediction algorithms. If the medal count shows a strong correlation with the year, we use linear regression to predict. If the correlation is weak, we use the average of the data as the prediction.

<!-- b000465 | prose | pages [8] -->
We use 0.5 as the threshold for determining strong or weak correlation (other thresholds will be considered in subsequent sensitivity analyses). The predicted number of medals is deﬁned as: { ∑6 k=1 ai jk , |r| < 0.5 ai j = 6 max{0, ˆaj} , |r| ≥0.5

<!-- b000466 | prose | pages [8] -->
where ai j is the predicted number of gold medals in category i for the 2024 Games, and r is the correlation coeﬃcient for ai jk, where k = 1, 2, ...6. The linear regression value is:

<!-- b000467 | prose | pages [8] -->
ˆaj = −10ai j1 −4ai j2 + 2ai j3 + 8ai j4 + 14ai j5 + 20ai j6 30 Since this value may be negative, we take the maximum between the linear regression value and 0.

<!-- b000468 | prose | pages [8] -->
Similarly, we apply the same methodology for bi jk, ci jk, and di jk, as well as their total predicted values bi j, ci j, and di j.

<!-- b000469 | prose | pages [8] -->
For athletes who did not participate in the previous Olympic Games but are expected to win medals in the upcoming Games, we deﬁne ei jk as the total number of athletes in category i who did not participate in the previous Games but win medal j (where 0 ≤j ≤3). The prediction for the number of such athletes is deﬁned as:

<!-- b000470 | prose | pages [8] -->
{ ∑6 k=1 ei jk , |r| < 0.5 ei j = 6 max{0, ˆej} , |r| ≥0.5

<!-- b000471 | prose | pages [8] -->
where r is the correlation coeﬃcient for ei jk, and the linear regression value ˆej is:

<!-- b000472 | prose | pages [8] -->
ˆej = −10ei j1 −4ei j2 + 2ei j3 + 8ei j4 + 14ei j5 + 20ei j6 30

<!-- b000473 | prose | pages [8] -->
New Events For new events, we use Monte Carlo simulations. By gathering authoritative data on rankings and points for each country in these events, we compute the winning probability for each country: wA PAB = wA + wB where wA and wB represent the points (weights) of countries A and B, respectively. We simulate the events according to the Olympic competition rules, where the top 16 athletes

<!-- b000474 | prose | pages [8, 9] -->
关注数学模型 are selected and paired for a knockout tournament. After two rounds, the top 4 athletes 微信公众号：数学模型 compete for the gold, silver, and bronze medals, as shown in the ﬁgure below:

<!-- b000475 | furniture | pages [8] -->
2

<!-- b000476 | furniture | pages [8] -->
MATHmodels

<!-- b000477 | furniture | pages [8] -->
获取更多资讯

<!-- b000478 | furniture | pages [9] -->
Team # 2510006

<!-- b000479 | furniture | pages [9] -->
Page 8

<!-- b000481 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000482 | caption | pages [9] -->
Figure 3: Monte Carlo Method for Simulating New Events

<!-- b000483 | prose | pages [9] -->
These 5 new events are split into male and female categories, making a total of 10 events. To obtain more accurate probabilities, we simulate each event 1 million times. The results are then used to estimate each countrys expected medals for these new events, denoted as f1, f2, and f3.

<!-- b000484 | prose | pages [9] -->
For some events, like the Lacrosse tournament, where oﬃcial data is sparse and only world rankings are available, we use logistic regression to assess the performance gaps between athletes: 1 PAB = 1 + exp (α · (RA −RB)) where RA and RB are the rankings of countries A and B. For events like Squash, where top 20 player rankings and points are available, we calculate the probabilities of each athlete winning gold, silver, and bronze, and estimate the probability of each country earning medals.

<!-- b000485 | prose | pages [9] -->
The total medal count for a country is the sum of medals from both traditional and new events: Gold: G = ∑6 1)+f1, Silver: S = ∑6 i=1(ai 1+bi 1+ci 1+di 1+ei i=1(ai 2+bi 2+ci 2+di 2+ei 2)+f2, Bronze: B = ∑6 i=1(ai 3 + bi 3 + ci 3 + di 3 + ei 3) + f3.

<!-- b000486 | prose | pages [9] -->
The ﬁnal predicted values for gold, silver, and bronze medals are rounded to the nearest integer:

<!-- b000487 | prose | pages [9] -->
⌊G + 1 2⌋, ⌊S + 1 2⌋, ⌊B + 1 2⌋ Total medals: T = ⌊G + 1 2⌋+ ⌊S + 1 2⌋+ ⌊B + 1 2⌋ This gives the predicted total and gold medal count for non-host countries that have won medals in the past.

<!-- b000488 | heading | pages [9] -->
4.1.2 Host Country: United States

<!-- b000489 | prose | pages [9] -->
The host country factor in the Olympics cannot be ignored. The table below shows the medal counts for new events by host countries from 1984 onwards.

<!-- b000490 | prose | pages [9, 10] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Year 1984 1988 1992 1996 2000 2004 2008 2012 2016 2021 2024 Gold 4 4 3 5 2 0 2 2 1 7 1 Silver 4 1 1 2 3 0 1 0 0 2 4 Bronze 1 1 0 1 2 0 0 1 0 1 2

<!-- b000491 | furniture | pages [9] -->
m

<!-- b000492 | furniture | pages [9] -->
m

<!-- b000493 | furniture | pages [9] -->
m

<!-- b000494 | furniture | pages [9] -->
m

<!-- b000495 | furniture | pages [9] -->
m

<!-- b000496 | furniture | pages [9] -->
m

<!-- b000497 | furniture | pages [9] -->
m

<!-- b000498 | furniture | pages [9] -->
m

<!-- b000499 | furniture | pages [9] -->
m

<!-- b000500 | furniture | pages [9] -->
m

<!-- b000501 | furniture | pages [9] -->
m

<!-- b000502 | furniture | pages [9] -->
m

<!-- b000503 | furniture | pages [9] -->
m

<!-- b000504 | furniture | pages [9] -->
m

<!-- b000505 | furniture | pages [9] -->
m

<!-- b000506 | furniture | pages [9] -->
m

<!-- b000507 | furniture | pages [9] -->
m

<!-- b000508 | furniture | pages [9] -->
m

<!-- b000509 | furniture | pages [9] -->
m

<!-- b000510 | furniture | pages [9] -->
m

<!-- b000511 | furniture | pages [9] -->
m

<!-- b000512 | furniture | pages [9] -->
m

<!-- b000513 | furniture | pages [9] -->
m

<!-- b000514 | furniture | pages [9] -->
m

<!-- b000515 | furniture | pages [9] -->
m

<!-- b000516 | furniture | pages [9] -->
m

<!-- b000517 | furniture | pages [9] -->
m

<!-- b000518 | furniture | pages [9] -->
m

<!-- b000519 | furniture | pages [9] -->
m

<!-- b000520 | furniture | pages [9] -->
m

<!-- b000521 | furniture | pages [9] -->
m

<!-- b000522 | furniture | pages [9] -->
m

<!-- b000523 | furniture | pages [9] -->
m

<!-- b000524 | furniture | pages [9] -->
m

<!-- b000525 | furniture | pages [9] -->
m

<!-- b000526 | furniture | pages [9] -->
m

<!-- b000527 | furniture | pages [9] -->
m

<!-- b000528 | furniture | pages [9] -->
m

<!-- b000529 | furniture | pages [9] -->
m

<!-- b000530 | furniture | pages [9] -->
m

<!-- b000531 | furniture | pages [9] -->
m

<!-- b000532 | furniture | pages [9] -->
m

<!-- b000533 | furniture | pages [9] -->
m

<!-- b000534 | furniture | pages [9] -->
m

<!-- b000535 | furniture | pages [9] -->
m

<!-- b000536 | furniture | pages [9] -->
m

<!-- b000537 | furniture | pages [9] -->
m

<!-- b000538 | furniture | pages [9] -->
m

<!-- b000539 | furniture | pages [9] -->
m

<!-- b000540 | furniture | pages [9] -->
m

<!-- b000541 | furniture | pages [9] -->
m

<!-- b000542 | furniture | pages [9] -->
m

<!-- b000543 | furniture | pages [9] -->
m

<!-- b000544 | furniture | pages [9] -->
m

<!-- b000545 | furniture | pages [9] -->
m

<!-- b000546 | furniture | pages [9] -->
m

<!-- b000547 | furniture | pages [9] -->
m

<!-- b000548 | furniture | pages [9] -->
m

<!-- b000549 | furniture | pages [9] -->
m

<!-- b000550 | furniture | pages [9] -->
m

<!-- b000551 | furniture | pages [9] -->
m

<!-- b000552 | furniture | pages [9] -->
m

<!-- b000553 | furniture | pages [9] -->
m

<!-- b000554 | furniture | pages [9] -->
m

<!-- b000555 | furniture | pages [9] -->
m

<!-- b000556 | furniture | pages [9] -->
m

<!-- b000557 | furniture | pages [9] -->
m

<!-- b000558 | furniture | pages [9] -->
m

<!-- b000559 | furniture | pages [9] -->
m

<!-- b000560 | furniture | pages [9] -->
m

<!-- b000561 | furniture | pages [9] -->
m

<!-- b000562 | furniture | pages [9] -->
m

<!-- b000563 | furniture | pages [9] -->
m

<!-- b000564 | furniture | pages [9] -->
m

<!-- b000565 | furniture | pages [9] -->
m

<!-- b000566 | furniture | pages [9] -->
m

<!-- b000567 | furniture | pages [9] -->
m

<!-- b000568 | furniture | pages [9] -->
m

<!-- b000569 | furniture | pages [9] -->
m

<!-- b000570 | furniture | pages [9] -->
m

<!-- b000571 | furniture | pages [9] -->
m

<!-- b000572 | furniture | pages [9] -->
m

<!-- b000573 | furniture | pages [9] -->
m

<!-- b000574 | furniture | pages [9] -->
m

<!-- b000575 | furniture | pages [9] -->
m

<!-- b000576 | furniture | pages [9] -->
m

<!-- b000577 | furniture | pages [9] -->
m

<!-- b000578 | furniture | pages [9] -->
m

<!-- b000579 | furniture | pages [9] -->
m

<!-- b000580 | furniture | pages [9] -->
m

<!-- b000581 | furniture | pages [9] -->
m

<!-- b000582 | furniture | pages [9] -->
m

<!-- b000583 | furniture | pages [9] -->
m

<!-- b000584 | furniture | pages [9] -->
m

<!-- b000585 | furniture | pages [9] -->
m

<!-- b000586 | furniture | pages [9] -->
m

<!-- b000587 | furniture | pages [9] -->
m

<!-- b000588 | furniture | pages [9] -->
m

<!-- b000589 | furniture | pages [9] -->
m

<!-- b000590 | furniture | pages [9] -->
m

<!-- b000591 | furniture | pages [9] -->
m

<!-- b000592 | furniture | pages [9] -->
m

<!-- b000593 | furniture | pages [9] -->
m

<!-- b000594 | furniture | pages [9] -->
m

<!-- b000595 | furniture | pages [9] -->
m

<!-- b000596 | furniture | pages [9] -->
m

<!-- b000597 | furniture | pages [9] -->
m

<!-- b000598 | furniture | pages [9] -->
m

<!-- b000599 | furniture | pages [9] -->
m

<!-- b000600 | furniture | pages [9] -->
m

<!-- b000601 | furniture | pages [9] -->
m

<!-- b000602 | furniture | pages [9] -->
m

<!-- b000603 | furniture | pages [9] -->
m

<!-- b000604 | furniture | pages [9] -->
m

<!-- b000605 | furniture | pages [9] -->
m

<!-- b000606 | furniture | pages [9] -->
m

<!-- b000607 | furniture | pages [9] -->
m

<!-- b000608 | furniture | pages [9] -->
m

<!-- b000609 | furniture | pages [9] -->
m

<!-- b000610 | furniture | pages [9] -->
m

<!-- b000611 | furniture | pages [9] -->
m

<!-- b000612 | furniture | pages [9] -->
m

<!-- b000613 | furniture | pages [9] -->
m

<!-- b000614 | furniture | pages [9] -->
m

<!-- b000615 | furniture | pages [9] -->
m

<!-- b000616 | furniture | pages [9] -->
m

<!-- b000617 | furniture | pages [9] -->
m

<!-- b000618 | furniture | pages [9] -->
m

<!-- b000619 | furniture | pages [9] -->
m

<!-- b000620 | furniture | pages [9] -->
m

<!-- b000621 | furniture | pages [9] -->
m

<!-- b000622 | furniture | pages [9] -->
m

<!-- b000623 | furniture | pages [9] -->
m

<!-- b000624 | furniture | pages [9] -->
m

<!-- b000625 | furniture | pages [9] -->
m

<!-- b000626 | furniture | pages [9] -->
m

<!-- b000627 | furniture | pages [9] -->
m

<!-- b000628 | furniture | pages [9] -->
m

<!-- b000629 | furniture | pages [9] -->
m

<!-- b000630 | furniture | pages [9] -->
m

<!-- b000631 | furniture | pages [9] -->
m

<!-- b000632 | furniture | pages [9] -->
m

<!-- b000633 | furniture | pages [9] -->
m

<!-- b000634 | furniture | pages [9] -->
m

<!-- b000635 | furniture | pages [9] -->
m

<!-- b000636 | furniture | pages [9] -->
m

<!-- b000637 | furniture | pages [9] -->
m

<!-- b000638 | furniture | pages [9] -->
m

<!-- b000639 | furniture | pages [9] -->
m

<!-- b000640 | furniture | pages [9] -->
m

<!-- b000641 | furniture | pages [9] -->
m

<!-- b000642 | furniture | pages [9] -->
m

<!-- b000643 | furniture | pages [9] -->
m

<!-- b000644 | furniture | pages [9] -->
m

<!-- b000645 | furniture | pages [9] -->
m

<!-- b000646 | furniture | pages [9] -->
m

<!-- b000647 | furniture | pages [9] -->
m

<!-- b000648 | furniture | pages [9] -->
m

<!-- b000649 | furniture | pages [9] -->
m

<!-- b000650 | furniture | pages [9] -->
m

<!-- b000651 | furniture | pages [9] -->
m

<!-- b000652 | furniture | pages [9] -->
m

<!-- b000653 | furniture | pages [9] -->
m

<!-- b000654 | furniture | pages [9] -->
m

<!-- b000655 | furniture | pages [9] -->
m

<!-- b000656 | furniture | pages [9] -->
m

<!-- b000657 | furniture | pages [9] -->
m

<!-- b000658 | furniture | pages [9] -->
m

<!-- b000659 | furniture | pages [9] -->
m

<!-- b000660 | furniture | pages [9] -->
m

<!-- b000661 | furniture | pages [9] -->
m

<!-- b000662 | furniture | pages [9] -->
m

<!-- b000663 | furniture | pages [9] -->
m

<!-- b000664 | furniture | pages [9] -->
m

<!-- b000665 | furniture | pages [9] -->
m

<!-- b000666 | furniture | pages [9] -->
m

<!-- b000667 | furniture | pages [9] -->
m

<!-- b000668 | furniture | pages [9] -->
m

<!-- b000669 | furniture | pages [9] -->
m

<!-- b000670 | furniture | pages [9] -->
m

<!-- b000671 | furniture | pages [9] -->
m

<!-- b000672 | furniture | pages [9] -->
m

<!-- b000673 | furniture | pages [9] -->
m

<!-- b000674 | furniture | pages [9] -->
m

<!-- b000675 | furniture | pages [9] -->
m

<!-- b000676 | furniture | pages [9] -->
m

<!-- b000677 | furniture | pages [9] -->
m

<!-- b000678 | furniture | pages [9] -->
m

<!-- b000679 | furniture | pages [9] -->
m

<!-- b000680 | furniture | pages [9] -->
m

<!-- b000681 | furniture | pages [9] -->
m

<!-- b000682 | furniture | pages [9] -->
m

<!-- b000683 | furniture | pages [9] -->
m

<!-- b000684 | furniture | pages [9] -->
m

<!-- b000685 | furniture | pages [9] -->
m

<!-- b000686 | furniture | pages [9] -->
m

<!-- b000687 | furniture | pages [9] -->
m

<!-- b000688 | furniture | pages [9] -->
m

<!-- b000689 | furniture | pages [9] -->
m

<!-- b000690 | furniture | pages [9] -->
m

<!-- b000691 | furniture | pages [9] -->
m

<!-- b000692 | furniture | pages [9] -->
m

<!-- b000693 | furniture | pages [9] -->
m

<!-- b000694 | furniture | pages [9] -->
m

<!-- b000695 | furniture | pages [9] -->
m

<!-- b000696 | furniture | pages [9] -->
m

<!-- b000697 | furniture | pages [9] -->
m

<!-- b000698 | furniture | pages [9] -->
m

<!-- b000699 | furniture | pages [9] -->
m

<!-- b000700 | furniture | pages [9] -->
m

<!-- b000701 | furniture | pages [9] -->
m

<!-- b000702 | furniture | pages [9] -->
m

<!-- b000703 | furniture | pages [9] -->
m

<!-- b000704 | furniture | pages [9] -->
m

<!-- b000705 | furniture | pages [9] -->
m

<!-- b000706 | furniture | pages [9] -->
m

<!-- b000707 | furniture | pages [9] -->
m

<!-- b000708 | furniture | pages [9] -->
m

<!-- b000709 | furniture | pages [9] -->
m

<!-- b000710 | furniture | pages [9] -->
m

<!-- b000711 | furniture | pages [9] -->
m

<!-- b000712 | furniture | pages [9] -->
m

<!-- b000713 | furniture | pages [9] -->
m

<!-- b000714 | furniture | pages [9] -->
m

<!-- b000715 | furniture | pages [9] -->
m

<!-- b000716 | furniture | pages [9] -->
m

<!-- b000717 | furniture | pages [9] -->
m

<!-- b000718 | furniture | pages [9] -->
m

<!-- b000719 | furniture | pages [9] -->
m

<!-- b000720 | furniture | pages [9] -->
m

<!-- b000721 | furniture | pages [9] -->
m

<!-- b000722 | furniture | pages [9] -->
m

<!-- b000723 | furniture | pages [9] -->
m

<!-- b000724 | furniture | pages [9] -->
m

<!-- b000725 | furniture | pages [9] -->
m

<!-- b000726 | furniture | pages [9] -->
m

<!-- b000727 | furniture | pages [9] -->
m

<!-- b000728 | furniture | pages [9] -->
m

<!-- b000729 | furniture | pages [9] -->
m

<!-- b000730 | furniture | pages [9] -->
m

<!-- b000731 | furniture | pages [9] -->
m

<!-- b000732 | furniture | pages [9] -->
m

<!-- b000733 | furniture | pages [9] -->
m

<!-- b000734 | furniture | pages [9] -->
m

<!-- b000735 | furniture | pages [9] -->
m

<!-- b000736 | furniture | pages [9] -->
m

<!-- b000737 | furniture | pages [9] -->
m

<!-- b000738 | furniture | pages [9] -->
m

<!-- b000739 | furniture | pages [9] -->
m

<!-- b000740 | furniture | pages [9] -->
m

<!-- b000741 | furniture | pages [9] -->
m

<!-- b000742 | furniture | pages [9] -->
m

<!-- b000743 | furniture | pages [9] -->
m

<!-- b000744 | furniture | pages [9] -->
m

<!-- b000745 | furniture | pages [9] -->
m

<!-- b000746 | furniture | pages [9] -->
m

<!-- b000747 | furniture | pages [9] -->
m

<!-- b000748 | furniture | pages [9] -->
m

<!-- b000749 | furniture | pages [9] -->
m

<!-- b000750 | furniture | pages [9] -->
m

<!-- b000751 | furniture | pages [9] -->
m

<!-- b000752 | furniture | pages [9] -->
m

<!-- b000753 | furniture | pages [9] -->
m

<!-- b000754 | furniture | pages [9] -->
m

<!-- b000755 | furniture | pages [9] -->
m

<!-- b000756 | furniture | pages [9] -->
m

<!-- b000757 | furniture | pages [9] -->
m

<!-- b000758 | furniture | pages [9] -->
m

<!-- b000759 | furniture | pages [9] -->
m

<!-- b000760 | furniture | pages [9] -->
m

<!-- b000761 | furniture | pages [9] -->
m

<!-- b000762 | furniture | pages [9] -->
m

<!-- b000763 | furniture | pages [9] -->
m

<!-- b000764 | furniture | pages [9] -->
m

<!-- b000765 | furniture | pages [9] -->
m

<!-- b000766 | furniture | pages [9] -->
m

<!-- b000767 | furniture | pages [9] -->
m

<!-- b000768 | furniture | pages [9] -->
m

<!-- b000769 | furniture | pages [9] -->
m

<!-- b000770 | furniture | pages [9] -->
m

<!-- b000771 | furniture | pages [9] -->
m

<!-- b000772 | furniture | pages [9] -->
m

<!-- b000773 | furniture | pages [9] -->
m

<!-- b000774 | furniture | pages [9] -->
m

<!-- b000775 | furniture | pages [9] -->
m

<!-- b000776 | furniture | pages [9] -->
m

<!-- b000777 | furniture | pages [9] -->
m

<!-- b000778 | furniture | pages [9] -->
m

<!-- b000779 | furniture | pages [9] -->
m

<!-- b000780 | furniture | pages [9] -->
m

<!-- b000781 | furniture | pages [9] -->
m

<!-- b000782 | furniture | pages [9] -->
m

<!-- b000783 | furniture | pages [9] -->
m

<!-- b000784 | furniture | pages [9] -->
m

<!-- b000785 | furniture | pages [9] -->
m

<!-- b000786 | furniture | pages [9] -->
m

<!-- b000787 | furniture | pages [9] -->
m

<!-- b000788 | furniture | pages [9] -->
m

<!-- b000789 | furniture | pages [9] -->
m

<!-- b000790 | furniture | pages [9] -->
m

<!-- b000791 | furniture | pages [9] -->
m

<!-- b000792 | furniture | pages [9] -->
m

<!-- b000793 | furniture | pages [9] -->
m

<!-- b000794 | furniture | pages [9] -->
m

<!-- b000795 | furniture | pages [9] -->
m

<!-- b000796 | furniture | pages [9] -->
m

<!-- b000797 | furniture | pages [9] -->
m

<!-- b000798 | furniture | pages [9] -->
m

<!-- b000799 | furniture | pages [9] -->
m

<!-- b000800 | furniture | pages [9] -->
m

<!-- b000801 | furniture | pages [9] -->
m

<!-- b000802 | furniture | pages [9] -->
m

<!-- b000803 | furniture | pages [9] -->
m

<!-- b000804 | furniture | pages [9] -->
m

<!-- b000805 | furniture | pages [9] -->
m

<!-- b000806 | furniture | pages [9] -->
m

<!-- b000807 | furniture | pages [9] -->
m

<!-- b000808 | furniture | pages [9] -->
m

<!-- b000809 | furniture | pages [9] -->
m

<!-- b000810 | furniture | pages [9] -->
m

<!-- b000811 | furniture | pages [9] -->
m

<!-- b000812 | furniture | pages [9] -->
m

<!-- b000813 | furniture | pages [9] -->
m

<!-- b000814 | furniture | pages [9] -->
m

<!-- b000815 | furniture | pages [10] -->
Team # 2510006

<!-- b000816 | furniture | pages [10] -->
Page 9

<!-- b000817 | caption | pages [10] -->
Table 2: Host’s New Event Medal

<!-- b000819 | prose | pages [10] -->
By analyzing the data from 1896 to 2024, it is clear that the host country’s medal count, both total and gold, has generally increased. The reasons for this increase can be attributed to two factors:

<!-- b000820 | prose | pages [10] -->
1. The host country may add events that are their strengths.

<!-- b000821 | prose | pages [10] -->
2. The undeniable "home advantage," including familiar venues, food and accommoda- tion, and no time zone adjustment.

<!-- b000822 | prose | pages [10] -->
Therefore, we predict the United States’ medals in the 2028 Los Angeles Olympics sep- arately for old and new events. First, we calculate the increase in medals for traditional events based on the host country’s performance in previous Olympics. This is done by comparing the number of medals won in the host countrys traditional events with the average number of medals won in the two previous Olympics, then calculating the increment and rate of increase.

<!-- b000823 | prose | pages [10] -->
Old Events For countries with missing data from the previous two Olympic Games, we use the two closest Olympic Games in time (e.g., for the 1984 Los Angeles Olympics, since the U.S. did not participate in the 1980 Moscow Olympics, we use the data from 1976 and 1988 for the U.S.).

<!-- b000824 | prose | pages [10] -->
Year Host Medals Previous & Next Average Increase Rate Increment 2g1 m1+n1 g1 −m1+n1 1896 g1 2 m1+n1 2 ... ... ... ... ...

<!-- b000825 | prose | pages [10] -->
2gt mt+nt gt −mt+nt 2024 gt 2 mt+nt 2 2028 to be predicted 115 to be predicted to be predicted

<!-- b000826 | caption | pages [10] -->
Table 3: Calculation of Host Factors

<!-- b000827 | prose | pages [10] -->
Using the data from the table, we calculate the weighted increase rate caused by the host country factors as:

<!-- b000828 | prose | pages [10] -->
( ) g1 + g2 + · · · + gt −1 × 100% Weighted Increase : Tboost = m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m1+m2 + m2+m3 + · · · + mt+nt m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2 2 2 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Next, we take the average of the medals won by the United States in the 2020 Tokyo Olympics m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m and the 2024 Paris Olympics for traditional events, multiply by the increase rate, and obtain m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the ﬁnal prediction for the number of medals in traditional events. The predicted values for m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m the expected gold, silver, bronze, and total medals in the 2028 Los Angeles Olympics are 53.64, 51.43, 31.56, and 136.63, respectively.

<!-- b000829 | prose | pages [10, 11] -->
关注数学模型 New Events Using the Monte Carlo simulation data from earlier for new events, if we use the expected values, the United States is predicted to win 0.937 gold, 0.735 silver, 0.706 微信公众号：数学模型 bronze, and 2.378 total medals in new events at the 2028 Los Angeles Olympics.

<!-- b000830 | furniture | pages [10] -->
2

<!-- b000831 | furniture | pages [10] -->
MATHmodels

<!-- b000832 | furniture | pages [10] -->
获取更多资讯

<!-- b000833 | furniture | pages [11] -->
Team # 2510006

<!-- b000834 | furniture | pages [11] -->
Page 10

<!-- b000836 | prose | pages [11] -->
By adding the expected values from both old and new events, we predict the United States will win 54.57 gold, 52.16 silver, and 32.37 bronze medals, totaling 139 medals in the 2028 Olympics.

<!-- b000837 | heading | pages [11] -->
4.1.3 Prediction for Countries Winning Medals for the First Time

<!-- b000838 | prose | pages [11] -->
We separate the analysis into two parts: the old events before 2024 and the new events added in 2028. For the old events, we fully utilize the data provided in the task, while for the 5 new events added in 2028, we calculate predictions based on authoritative sources.

<!-- b000839 | prose | pages [11] -->
微信号：MATHmodels For countries that have never won medals before, we consider the number of countries that win their ﬁrst medal in each Olympic Games for old events: starting from 1984, the data shows 4, 5, 8, 16, 6, 5, 6, 8, 3, 0, and 4. The average value is 5.91, and the standard deviation is 3.85. It is clear that the number of ﬁrst-time medal winners in 1996 (16) is signiﬁcantly higher than twice the standard deviation, so we need to understand why so many new countries won medals that year.

<!-- b000840 | prose | pages [11] -->
According to historical records, the Disintegration of the Soviet Union, Yugoslavia, and Czechoslovakia in 1991, 1992, and 1993, along with the reuniﬁcation of Germany and Yemen in 1990, led to the emergence of new countries. This explains the unusually high number of ﬁrst-time medal winners. Thus, in the subsequent model, we need to separate countries that emerged from Disintegration from those that were already existing.

<!-- b000841 | prose | pages [11] -->
Old Events First, we need to predict the number of countries without medals participating in the 2028 Los Angeles Olympics. Similarly, based on the number of participated events of each countries from 2000 to 2024, we select whether to use a speciﬁc module which contains the average value or linear regression by examining the correlation, and we obtain the predicted participation numbers for 2028.

<!-- b000842 | prose | pages [11] -->
{ ∑7 k=1 aik , |r| < 0.5 ai 7 j = max{0, ˆaj} , |r| ≥0.5

<!-- b000843 | prose | pages [11] -->
where aij represents the number of events country i participated in at the 1996 + 4j year Olympics. r is the correlation coeﬃcient for aij, with k = 1, 2...7; the linear regression value is calculated as:

<!-- b000844 | prose | pages [11] -->
ˆaj = −8ai1 −5ai2 −2ai3 + ai4 + 4ai5 + 7ai6 + 10ai7 7

<!-- b000845 | prose | pages [11] -->
Next, we calculate the total number of events country i participated in over the years: a = ∑t k=1 aik.

<!-- b000846 | prose | pages [11, 12] -->
Considering the Disintegration of some countries between 1992-1996, which made the 1996 data abnormal, we classify the countries into two categories: countries that emerged from Disintegration and countries that already existed. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m { Non-disintegrated countries winning ﬁrst medal u1, u2, ..., ut−2 Disintegrated countries winning ﬁrst medal v1, v2, ..., v9

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

<!-- b001171 | furniture | pages [12] -->
Team # 2510006

<!-- b001172 | furniture | pages [12] -->
Page 11

<!-- b001174 | prose | pages [12] -->
For Non-disintegrated countries, based on historical data, we apply a combination of the ARIMA model and Random Forest model, using time series data and feature engineering to generate prediction results and their conﬁdence intervals.

<!-- b001175 | prose | pages [12] -->
Reason for the model choice: The number of countries winning their ﬁrst medal in the Olympics is a typical time series data with an underlying trend (the number of participating countries increases, the number of old events increases, etc.), and a four-year cycle. The ARIMA model captures these characteristics well and is used to predict the data for 2028. The Random Forest model, on the other hand, can capture the complex nonlinear relationships between total countries participating, total medals, and the number of countries winning ﬁrst medals. The ensemble of decision trees helps reduce overﬁtting, and when combined with the results from the ARIMA model, we can estimate the conﬁdence interval. The ARIMA model captures linear dependencies in time series data, while the Random Forest model captures non-linear dependencies and additional features.

<!-- b001176 | prose | pages [12] -->
We split the data from 1896-2004 and 2008-2024 into training and testing sets, with each Olympic year as a time point. The target variable is the number of countries winning their ﬁrst medal. After performing ﬁrst and second-order diﬀerencing on the original target variable, we conduct an ADF test to verify the stationarity of the data. The ADF test results indicate that the original series is the most stationary, with an ADF statistic of ADF Statistic = −4.01, and a p-value of 0.0014, as shown in the ﬁgure. After performing ﬁrst and second-order diﬀerencing, there is no noticeable improvement in stationarity, conﬁrming that the original data is optimal.

<!-- b001177 | caption | pages [12] -->
Figure 4: Trend chart of original data,

<!-- b001178 | caption | pages [12] -->
Figure 5: ADF Statistic and p-value.

<!-- b001179 | prose | pages [12] -->
ﬁrst-order diﬀerence, and second-order The ADF statistic is -4.01, and the p- diﬀerence. The original data exhibits value is 0.0014, verifying the stationar- the best stationarity. ity of the original series.

<!-- b001180 | prose | pages [12] -->
Next, we plot the ACF and PACF of the original series. The tailing patterns in the ACF and PACF indicate long-term dependencies, leading us to select the ARIMA model for modeling. To determine the optimal parameters for the ARIMA model, we use the AIC criterion. The AIC is calculated as AIC = 2K −2 ln(L), where K is the number of

<!-- b001181 | prose | pages [12, 13] -->
关注数学模型 model parameters and L is the maximum likelihood value. By plotting the AIC heatmap, we ﬁnd that when p = 0 and q = 2, the AIC value is minimized, so we select ARIMA(0,0,2) as the optimal model.

<!-- b001182 | furniture | pages [12] -->
2

<!-- b001183 | furniture | pages [12] -->
MATHmodels

<!-- b001184 | furniture | pages [12] -->
获取更多资讯

<!-- b001185 | furniture | pages [13] -->
Team # 2510006

<!-- b001186 | furniture | pages [13] -->
Page 12

<!-- b001188 | prose | pages [13] -->
微信公众号：数学模型

<!-- b001189 | caption | pages [13] -->
Figure 6:

<!-- b001190 | prose | pages [13] -->
ACF and PACF plots of second-order diﬀerences. The plots show the long-term dependencies, sup-

<!-- b001191 | caption | pages [13] -->
Figure 7: AIC heatmap.

<!-- b001192 | prose | pages [13] -->
The ﬁgure shows that the AIC criterion selects the 微信号：MATHmodels porting the choice of ARIMA model- ing. ARIMA(0,0,2) model, where p = 0 and q = 2 minimize the AIC value.

<!-- b001193 | prose | pages [13] -->
To validate the ARIMA model’s ﬁtting performance, we perform residual checks. First, we plot the ACF and PACF of the residuals and conduct the Ljung-Box test. The results show no signiﬁcant autocorrelation in the residuals within the selected lag (p > 0.05). Additionally, we plot the histogram and QQ plot of the residuals and con- duct the Shapiro-Wilk test, which conﬁrms that the residuals are approximately normally These results indicate that the ARIMA model ﬁts well, with distributed (p > 0.05). no signiﬁcant autocorrelation in the residuals and a normal distribution, meeting the modeling assumptions.

<!-- b001194 | caption | pages [13] -->
Figure 8:

<!-- b001195 | prose | pages [13] -->
ACF and

<!-- b001196 | caption | pages [13] -->
Figure 9:

<!-- b001197 | prose | pages [13] -->
Ljung-Box PACF of residuals. test results. The The residuals show no Ljung-Box test shows signiﬁcant autocor- no signiﬁcant autocor- relation, indicating a relation in the residu- good ﬁt of the model. als (p > 0.05).

<!-- b001198 | caption | pages [13] -->
Figure 10:

<!-- b001199 | prose | pages [13] -->
Shapiro-

<!-- b001200 | caption | pages [13] -->
Figure 11: QQ plot of

<!-- b001201 | prose | pages [13] -->
Wilk test results. The residuals. The residu- test indicates that the als align with the ﬁtted residuals are normally line, supporting their distributed (p > 0.05). normality.

<!-- b001202 | prose | pages [13, 14] -->
Based on the results from the ARIMA(0,0,2) model, we predict that the number of countries winning their ﬁrst medal in 2028 will be 3.09. By inputting this prediction along with training set features into the Random Forest model, we obtain a 95% conﬁdence interval for the number of countries winning their ﬁrst medal in 2028 of [2.58, 4.87], as shown in the ﬁgure.

<!-- b001203 | furniture | pages [14] -->
Team # 2510006

<!-- b001204 | furniture | pages [14] -->
Page 13

<!-- b001206 | caption | pages [14] -->
Figure 12:

<!-- b001207 | prose | pages [14] -->
Comparison of actual vs predicted number of ﬁrst-time medal-

<!-- b001208 | caption | pages [14] -->
Figure 13: Training, testing, and 2028

<!-- b001209 | prose | pages [14] -->
winning countries (2008-2028). The prediction results for ﬁrst-time medal- prediction aligns well with the actual winning countries. The 95% conﬁdence results, indicating high accuracy of the interval is [2.58, 4.87], indicating stable model. and reliable predictions.

<!-- b001210 | prose | pages [14] -->
For countries emerging from Disintegration after 1996, the number of new countries winning their ﬁrst medal is as follows: 11, 2, 1, 1, 1, 0, 0, 0, forming a monotonically decreasing sequence approaching 0. The original data, ﬁrst-order diﬀerence, and second- order diﬀerence fail to pass the stationarity test. Considering that 18 of the 21 Disintegrated countries have already won medals, we use an exponential regression model to predict a 95% conﬁdence interval of [0, 0.01]. Therefore, we conclude that the number of countries from Disintegrated nations winning their ﬁrst medal in 2028 will be 0, i.e., u = 0.

<!-- b001211 | caption | pages [14] -->
Figure 14: Exponential Regression Model: First Medal Country (Disintegration) 2028 95%

<!-- b001212 | prose | pages [14] -->
Conﬁdence Interval Prediction

<!-- b001213 | prose | pages [14] -->
Thus, we can calculate the probability of country i (which has not won a medal) winning a medal in the 2028 Los Angeles Olympics traditional events as:

<!-- b001214 | prose | pages [14] -->
Li = ai a · (u + v)

<!-- b001215 | prose | pages [14, 15] -->
关注数学模型 Since the number of events is large and the probability of winning in each event is low, the distribution of Li can be approximated by a Poisson distribution: Poisson(Li). From the 微信公众号：数学模型 Poisson distribution formula, the winning probability qi is the complement of the probability of zero medals:

<!-- b001216 | furniture | pages [14] -->
2

<!-- b001217 | furniture | pages [14] -->
MATHmodels

<!-- b001218 | furniture | pages [14] -->
获取更多资讯

<!-- b001219 | furniture | pages [15] -->
Team # 2510006

<!-- b001220 | furniture | pages [15] -->
Page 14

<!-- b001222 | prose | pages [15] -->
qi = 1 −P(x = 0) = 1 −e−Li

<!-- b001223 | prose | pages [15] -->
New Events Among the 5 new events, the countries with a chance of winning their ﬁrst medal are Bangladesh and Nicaragua. Based on the previous Monte Carlo simulation, the following table is derived:

<!-- b001224 | prose | pages [15] -->
Country Item Gold Silver Bronze Total Nicaragua baseball/softball (Men’s) 0.058 0.062 0.062 0.182 微信号：MATHmodels Bangladesh cricket (Men’s) 0.066 0.067 0.068 0.201 Bangladesh cricket (Women’s) 0.075 0.077 0.077 0.229

<!-- b001225 | caption | pages [15] -->
Table 4: Medal Distribution by None-Medal Country and New Event

<!-- b001226 | prose | pages [15] -->
Based on this, we calculate the probability of the two countries winning medals in the new events:

<!-- b001227 | prose | pages [15] -->
{ Bangladesh:PBangladesh = 1 −(1 −qBangladesh)(1 −0.229)(1 −0.201) Nicaragua:PNicaragua = 1 −(1 −qNicaragua)(1 −0.182)

<!-- b001228 | prose | pages [15] -->
For other countries, Pcountry = qcountry.

<!-- b001229 | prose | pages [15] -->
For countries that have never won a medal, we combine the new and old events to derive the top ten countries most likely to win their ﬁrst medal in 2024.

<!-- b001230 | prose | pages [15] -->
Next, we calculate the distribution function of medals based on the expected values of medals. Since for any given country, the distribution of medals in each event is a relatively small probability binomial distribution, by summing these binomial distributions, we

<!-- b001231 | caption | pages [15] -->
Figure 15: Top 10 Countries Most Likely to Win Their First Medal

<!-- b001232 | prose | pages [15, 16] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m approximate the total medal distribution using a Poisson distribution when the number of events is large. Therefore, when calculating the total medal and gold medal counts, we ap- proximate these distributions as Poisson distributions, Poisson(λ), with λ being T (total medals) and G (gold medals). Then, we simulate the Poisson probability distribution using a

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

<!-- b001557 | furniture | pages [16] -->
Team # 2510006

<!-- b001558 | furniture | pages [16] -->
Page 15

<!-- b001560 | heading | pages [16] -->
Random Forest model, calculating the 90% conﬁdence intervals (with 90% conﬁdence

<!-- b001561 | prose | pages [16] -->
assumed for now; sensitivity analysis will consider other conﬁdence levels): [Tmin, Tmax] and [Gmin, Gmax], which are then used as the prediction intervals for the total medals and gold medals for each country in Task 1.

<!-- b001562 | prose | pages [16] -->
Since Russia did not fully participate in the 2024 Olympic Games, the total medal count and gold medal count for Russia are zero. In the ﬁgures below, we can see that among the major Olympic medal-winning countries, the United States is most likely(95%conﬁdence) to improve (in both total medals and gold medals), except for Russia. This is due to the home advantage for the host country, including, but not limited to, familiar venues, cheers from local audiences, accustomed accommodation and food, and no time zone adjustment. There is no signiﬁcant decrease in the total medal count for the United States; however, China is expected to show the most notable decline in gold medals among these ten countries. This is mainly due to the cancellation of weightlifting, China’s most successful event (where it won 5 gold medals at the 2024 Olympic Games).

<!-- b001563 | prose | pages [16] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001564 | caption | pages [16] -->
Figure 16: Top 10 Total Medal Predic-

<!-- b001565 | caption | pages [16] -->
Figure 17: Top 10 Gold Medal Predic-

<!-- b001566 | prose | pages [16] -->
tions tions

<!-- b001567 | prose | pages [16] -->
Analysis of model accuracy and uncertainty: For a given country, the uncertainty of the total medal count is calculated as:

<!-- b001568 | prose | pages [16] -->
Tuncertainty = Tmax −Tmin T

<!-- b001569 | prose | pages [16] -->
We analyze the uncertainty for both countries with many medals and countries with fewer medals.

<!-- b001570 | prose | pages [16, 17] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b001571 | furniture | pages [16] -->
2

<!-- b001572 | furniture | pages [16] -->
MATHmodels

<!-- b001573 | furniture | pages [16] -->
获取更多资讯

<!-- b001574 | furniture | pages [17] -->
Team # 2510006

<!-- b001575 | furniture | pages [17] -->
Page 16

<!-- b001577 | caption | pages [17] -->
Figure 19:

<!-- b001578 | prose | pages [17] -->
Uncertainty in Predicted

<!-- b001579 | caption | pages [17] -->
Figure 18:

<!-- b001580 | prose | pages [17] -->
Uncertainty in Predicted Medal Counts for Countries with Less Medal Counts for Top 10 Countries Than 10 Medals

<!-- b001581 | prose | pages [17] -->
Thus, we conclude that the uncertainty for the countries with more medals is relatively low, while the uncertainty for the countries with less medals is higher. This is because the countries with more medals have smaller ﬂuctuation compared to the number of the medals, while the countries with less medals have greater ﬂuctuation compared to the number of the medals.

<!-- b001582 | heading | pages [17] -->
4.2 Analysis of the Relationship Between Events and Medals

<!-- b001583 | prose | pages [17] -->
Correlation Between Six Major Categories of Events and Medals

<!-- b001584 | prose | pages [17] -->
Categorization Basis: Medal Distribution by Country

<!-- b001585 | prose | pages [17] -->
Let i = 1, 2...6, corresponding to the following major categories of sports: Water Sports, Ball Sports, Athletics, Technical Sports, Combat Sports, and Racing Sports; j corresponds to the countries, which include all countries that have participated in the Olympics since 2000. Deﬁne xij as the proportion of medals for country j in the i-th major category from 1896 to 2024, where xij = uij ri , with uij being the total number of medals won by country j in the i-th category from 1896 to 2024, and ri being the total number of medals won in the i-th category from 1896 to 2024.

<!-- b001586 | prose | pages [17] -->
Next, we calculate the diﬀerence in medal distribution between the i-th category and the j-th category:

<!-- b001587 | prose | pages [17] -->
t ∑ (xik −xjk)2 (1 ≤i, j ≤6) dij = k=1 We then create a 6×6 table. It is evident that in this table, dij = dji and dii = 0. The larger the value of dij, the greater the diﬀerence between {xik −xjk}, meaning that the correlation between these two categories of sports is weaker.

<!-- b001588 | prose | pages [17] -->
To normalize this table, we deﬁne:

<!-- b001589 | prose | pages [17, 18] -->
dij ′ ij = 1 − d max{dij} This gives us a new 6 × 6 table that describes the correlation between every pair of sports categories. We then use this data to generate a heatmap. In the heatmap, the more green the cells are, the stronger the correlation, and the more red they are, the weaker the correlation.

<!-- b001590 | furniture | pages [18] -->
Page 17

<!-- b001591 | furniture | pages [18] -->
Team # 2510006

<!-- b001593 | prose | pages [18] -->
Track & Fleld Aquatic Sperts

<!-- b001594 | prose | pages [18] -->
0.782374433 Bell Sperts 0.519336636 0.732628304 0.612192247 0.360434385

<!-- b001595 | prose | pages [18] -->
0.519336636 0.819731191 0.374237973 Track A Field 0.203151278 0.127263806

<!-- b001596 | prose | pages [18] -->
0.732628304 0.819731191 0.421429111 0.39406066 0.499614724

<!-- b001597 | prose | pages [18] -->
0.421429111 0.710279814 0.612192247 0.203151278 0

<!-- b001598 | prose | pages [18] -->
0.21984997 0.360434385 0.127263806 0.39406066

<!-- b001599 | prose | pages [18] -->
Murtial Arte 0.782374433 0.374237973 0.499614724 0.710279814 0.21984997

<!-- b001600 | caption | pages [18] -->
Figure 20: Heat Map

<!-- b001601 | prose | pages [18] -->
Analysis: The correlation between events is based on medal proportions, normalized to reflect the correlation between each pair. Apart from the self-correlation (which is 1), there is a strong correlation between Ball Sports and Combat Sports, as well as between Water Sports and Athletics. The former is because both Ball Sports and Combat Sports require physical confrontation, and in addition to strength, coordination, flexibility, and reaction time are also indispensable. For the latter, Water Sports and Athletics both fundamentally focus on speed, and some events require explosive power or endurance, which are shared characteristics. In contrast, the lower correlation between Technical Sports and Racing Sports is due to the fact that Technical Sports emphasize flexibility, balance, and coordination in the body to achieve high scores through complex movements, whereas Racing Sports focus on speed, reaction time, and explosiveness, with the goal of completing the race faster than the opponent.

<!-- b001602 | prose | pages [18] -->
5 Task 2: Great Coaches

<!-- b001603 | prose | pages [18] -->
5.1 Evidence of the Great Coach Effect

<!-- b001604 | prose | pages [18] -->
We examine the data for possible evidence of the "great coach" effect: a country has not won a medal in a specific event for several consecutive Olympics, but in the next one or subsequent ones, the number of medals significantly increases! Meanwhile, there was a change in coach in the previous or subsequent Olympics. Thus, we use Fisher's Exact Test to explore whether the medals won are related to the change in coach.

<!-- b001605 | prose | pages [18] -->
Lets assume a country has participated in n consecutive Olympics for a particular event and has not won a medal, but after changing the coach, it won a medal. During the coach's

<!-- b001606 | prose | pages [18, 19] -->
关注数学模型 微信公众号：数学模型 tenure for k Olympics, the country won g gold medals, s silver medals, and b bronze medals, with m Olympics in which the country did not win any medals.

<!-- b001607 | furniture | pages [18] -->
获取更多资讯

<!-- b001608 | furniture | pages [19] -->
Team # 2510006

<!-- b001609 | furniture | pages [19] -->
Page 18

<!-- b001611 | prose | pages [19] -->
First, construct the mapping for gold, silver, and bronze medals:

<!-- b001612 | prose | pages [19] -->
{ gold + silver + bronze = 3 gold : silver : bronze = 3 : 2 : 1 (standard mapping of medals to points)

<!-- b001613 | prose | pages [19] -->
The corresponding "medal points" for gold, silver, and bronze are 1.5, 1, and 0.5, respec- 微信号：MATHmodels tively. Thus, the "medal points" for the medals won are given by:

<!-- b001614 | prose | pages [19] -->
t = 3g + 2s + b 2

<!-- b001615 | prose | pages [19] -->
We use Fisher’s Exact Test to calculate the conﬁdence level of whether winning medals is related to the change in coach:

<!-- b001616 | prose | pages [19] -->
Before Changing Coach After Changing Coach 3g + 2s + b Medal Points 0 2 No Medals (Count) n m

<!-- b001617 | caption | pages [19] -->
Table 5: Table Title

<!-- b001618 | prose | pages [19] -->
From the table, the signiﬁcant level is given by:

<!-- b001619 | prose | pages [19] -->
α = (n + m)!(m + t)!n!t! m!n!t!(m + n + t)! = (n + m)!(m + t)! m!(m + n + t)! ∈(0, 1) Thus, the conﬁdence level is:

<!-- b001620 | prose | pages [19] -->
P = 1 −α

<!-- b001621 | prose | pages [19] -->
We ﬁnd examples of great coaches, satisfying the following conditions:

<!-- b001622 | prose | pages [19] -->
1. In the n Olympics before the coachs tenure, the country did not win any medals in the event.

<!-- b001623 | prose | pages [19] -->
2. After the coach took over, the country won medals, achieving a breakthrough from 0 to 1.

<!-- b001624 | prose | pages [19] -->
Using the examples from the task, we analyze the data for Lang Ping and Béla Károlyi. The following table shows their coaching records for diﬀerent national teams, and the re- sulting P-values indicate how conﬁdent we are in attributing the success to the "Great Coach."

<!-- b001625 | prose | pages [19, 20] -->
To measure the contribution of these "Great Coaches", we calculate the average medal points per Olympics before and after their coaching, and then take the diﬀerence. For example, Lang Ping’s contributions to the Chinese and USA volleyball teams are respectively 0.75 medal points (between silver and bronze medal) and 0.5 medal points (equivalent to one bronze medal). m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Coach Country n m g s b t P 3 Lang Ping China 2 1 1 0 0 0.6190 2 1 Lang Ping USA 3 0 0 0 1 0.5429 2 Béla Károlyi USA 7 1 2 4 2 8 0.9993 9 Béla Károlyi Romania 2 0 1 3 0 0.9441 2

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

<!-- b001633 | furniture | pages [19] -->
m

<!-- b001634 | furniture | pages [19] -->
m

<!-- b001635 | furniture | pages [19] -->
m

<!-- b001636 | furniture | pages [19] -->
m

<!-- b001637 | furniture | pages [19] -->
m

<!-- b001638 | furniture | pages [19] -->
m

<!-- b001639 | furniture | pages [19] -->
m

<!-- b001640 | furniture | pages [19] -->
m

<!-- b001641 | furniture | pages [19] -->
m

<!-- b001642 | furniture | pages [19] -->
m

<!-- b001643 | furniture | pages [19] -->
m

<!-- b001644 | furniture | pages [19] -->
m

<!-- b001645 | furniture | pages [19] -->
m

<!-- b001646 | furniture | pages [19] -->
m

<!-- b001647 | furniture | pages [19] -->
m

<!-- b001648 | furniture | pages [19] -->
m

<!-- b001649 | furniture | pages [19] -->
m

<!-- b001650 | furniture | pages [19] -->
m

<!-- b001651 | furniture | pages [19] -->
m

<!-- b001652 | furniture | pages [19] -->
m

<!-- b001653 | furniture | pages [19] -->
m

<!-- b001654 | furniture | pages [19] -->
m

<!-- b001655 | furniture | pages [19] -->
m

<!-- b001656 | furniture | pages [19] -->
m

<!-- b001657 | furniture | pages [19] -->
m

<!-- b001658 | furniture | pages [19] -->
m

<!-- b001659 | furniture | pages [19] -->
m

<!-- b001660 | furniture | pages [19] -->
m

<!-- b001661 | furniture | pages [19] -->
m

<!-- b001662 | furniture | pages [19] -->
m

<!-- b001663 | furniture | pages [19] -->
m

<!-- b001664 | furniture | pages [19] -->
m

<!-- b001665 | furniture | pages [19] -->
m

<!-- b001666 | furniture | pages [19] -->
m

<!-- b001667 | furniture | pages [19] -->
m

<!-- b001668 | furniture | pages [19] -->
m

<!-- b001669 | furniture | pages [19] -->
m

<!-- b001670 | furniture | pages [19] -->
m

<!-- b001671 | furniture | pages [19] -->
m

<!-- b001672 | furniture | pages [19] -->
m

<!-- b001673 | furniture | pages [19] -->
m

<!-- b001674 | furniture | pages [19] -->
m

<!-- b001675 | furniture | pages [19] -->
m

<!-- b001676 | furniture | pages [19] -->
m

<!-- b001677 | furniture | pages [19] -->
m

<!-- b001678 | furniture | pages [19] -->
m

<!-- b001679 | furniture | pages [19] -->
m

<!-- b001680 | furniture | pages [19] -->
m

<!-- b001681 | furniture | pages [19] -->
m

<!-- b001682 | furniture | pages [19] -->
m

<!-- b001683 | furniture | pages [19] -->
m

<!-- b001684 | furniture | pages [19] -->
m

<!-- b001685 | furniture | pages [19] -->
m

<!-- b001686 | furniture | pages [19] -->
m

<!-- b001687 | furniture | pages [19] -->
m

<!-- b001688 | furniture | pages [19] -->
m

<!-- b001689 | furniture | pages [19] -->
m

<!-- b001690 | furniture | pages [19] -->
m

<!-- b001691 | furniture | pages [19] -->
m

<!-- b001692 | furniture | pages [19] -->
m

<!-- b001693 | furniture | pages [19] -->
m

<!-- b001694 | furniture | pages [19] -->
m

<!-- b001695 | furniture | pages [19] -->
m

<!-- b001696 | furniture | pages [19] -->
m

<!-- b001697 | furniture | pages [19] -->
m

<!-- b001698 | furniture | pages [19] -->
m

<!-- b001699 | furniture | pages [19] -->
m

<!-- b001700 | furniture | pages [19] -->
m

<!-- b001701 | furniture | pages [19] -->
m

<!-- b001702 | furniture | pages [19] -->
m

<!-- b001703 | furniture | pages [19] -->
m

<!-- b001704 | furniture | pages [19] -->
m

<!-- b001705 | furniture | pages [19] -->
m

<!-- b001706 | furniture | pages [19] -->
m

<!-- b001707 | furniture | pages [19] -->
m

<!-- b001708 | furniture | pages [19] -->
m

<!-- b001709 | furniture | pages [19] -->
m

<!-- b001710 | furniture | pages [19] -->
m

<!-- b001711 | furniture | pages [19] -->
m

<!-- b001712 | furniture | pages [19] -->
m

<!-- b001713 | furniture | pages [19] -->
m

<!-- b001714 | furniture | pages [19] -->
m

<!-- b001715 | furniture | pages [19] -->
m

<!-- b001716 | furniture | pages [19] -->
m

<!-- b001717 | furniture | pages [19] -->
m

<!-- b001718 | furniture | pages [19] -->
m

<!-- b001719 | furniture | pages [19] -->
m

<!-- b001720 | furniture | pages [19] -->
m

<!-- b001721 | furniture | pages [19] -->
m

<!-- b001722 | furniture | pages [19] -->
m

<!-- b001723 | furniture | pages [19] -->
m

<!-- b001724 | furniture | pages [19] -->
m

<!-- b001725 | furniture | pages [19] -->
m

<!-- b001726 | furniture | pages [19] -->
m

<!-- b001727 | furniture | pages [19] -->
m

<!-- b001728 | furniture | pages [19] -->
m

<!-- b001729 | furniture | pages [19] -->
m

<!-- b001730 | furniture | pages [19] -->
m

<!-- b001731 | furniture | pages [19] -->
m

<!-- b001732 | furniture | pages [19] -->
m

<!-- b001733 | furniture | pages [19] -->
m

<!-- b001734 | furniture | pages [19] -->
m

<!-- b001735 | furniture | pages [19] -->
m

<!-- b001736 | furniture | pages [19] -->
m

<!-- b001737 | furniture | pages [19] -->
m

<!-- b001738 | furniture | pages [19] -->
m

<!-- b001739 | furniture | pages [19] -->
m

<!-- b001740 | furniture | pages [19] -->
m

<!-- b001741 | furniture | pages [19] -->
m

<!-- b001742 | furniture | pages [19] -->
m

<!-- b001743 | furniture | pages [19] -->
m

<!-- b001744 | furniture | pages [19] -->
m

<!-- b001745 | furniture | pages [19] -->
m

<!-- b001746 | furniture | pages [19] -->
m

<!-- b001747 | furniture | pages [19] -->
m

<!-- b001748 | furniture | pages [19] -->
m

<!-- b001749 | furniture | pages [19] -->
m

<!-- b001750 | furniture | pages [19] -->
m

<!-- b001751 | furniture | pages [19] -->
m

<!-- b001752 | furniture | pages [19] -->
m

<!-- b001753 | furniture | pages [19] -->
m

<!-- b001754 | furniture | pages [19] -->
m

<!-- b001755 | furniture | pages [19] -->
m

<!-- b001756 | furniture | pages [19] -->
m

<!-- b001757 | furniture | pages [19] -->
m

<!-- b001758 | furniture | pages [19] -->
m

<!-- b001759 | furniture | pages [19] -->
m

<!-- b001760 | furniture | pages [19] -->
m

<!-- b001761 | furniture | pages [19] -->
m

<!-- b001762 | furniture | pages [19] -->
m

<!-- b001763 | furniture | pages [19] -->
m

<!-- b001764 | furniture | pages [19] -->
m

<!-- b001765 | furniture | pages [19] -->
m

<!-- b001766 | furniture | pages [19] -->
m

<!-- b001767 | furniture | pages [19] -->
m

<!-- b001768 | furniture | pages [19] -->
m

<!-- b001769 | furniture | pages [19] -->
m

<!-- b001770 | furniture | pages [19] -->
m

<!-- b001771 | furniture | pages [19] -->
m

<!-- b001772 | furniture | pages [19] -->
m

<!-- b001773 | furniture | pages [19] -->
m

<!-- b001774 | furniture | pages [19] -->
m

<!-- b001775 | furniture | pages [19] -->
m

<!-- b001776 | furniture | pages [19] -->
m

<!-- b001777 | furniture | pages [19] -->
m

<!-- b001778 | furniture | pages [19] -->
m

<!-- b001779 | furniture | pages [19] -->
m

<!-- b001780 | furniture | pages [19] -->
m

<!-- b001781 | furniture | pages [19] -->
m

<!-- b001782 | furniture | pages [19] -->
m

<!-- b001783 | furniture | pages [19] -->
m

<!-- b001784 | furniture | pages [19] -->
m

<!-- b001785 | furniture | pages [19] -->
m

<!-- b001786 | furniture | pages [19] -->
m

<!-- b001787 | furniture | pages [19] -->
m

<!-- b001788 | furniture | pages [19] -->
m

<!-- b001789 | furniture | pages [19] -->
m

<!-- b001790 | furniture | pages [19] -->
m

<!-- b001791 | furniture | pages [19] -->
m

<!-- b001792 | furniture | pages [19] -->
m

<!-- b001793 | furniture | pages [19] -->
m

<!-- b001794 | furniture | pages [19] -->
m

<!-- b001795 | furniture | pages [19] -->
m

<!-- b001796 | furniture | pages [19] -->
m

<!-- b001797 | furniture | pages [19] -->
m

<!-- b001798 | furniture | pages [19] -->
m

<!-- b001799 | furniture | pages [19] -->
m

<!-- b001800 | furniture | pages [19] -->
m

<!-- b001801 | furniture | pages [19] -->
m

<!-- b001802 | furniture | pages [19] -->
m

<!-- b001803 | furniture | pages [19] -->
m

<!-- b001804 | furniture | pages [19] -->
m

<!-- b001805 | furniture | pages [19] -->
m

<!-- b001806 | furniture | pages [19] -->
m

<!-- b001807 | furniture | pages [19] -->
m

<!-- b001808 | furniture | pages [19] -->
m

<!-- b001809 | furniture | pages [19] -->
m

<!-- b001810 | furniture | pages [19] -->
m

<!-- b001811 | furniture | pages [19] -->
m

<!-- b001812 | furniture | pages [19] -->
m

<!-- b001813 | furniture | pages [19] -->
m

<!-- b001814 | furniture | pages [19] -->
m

<!-- b001815 | furniture | pages [19] -->
m

<!-- b001816 | furniture | pages [19] -->
m

<!-- b001817 | furniture | pages [19] -->
m

<!-- b001818 | furniture | pages [19] -->
m

<!-- b001819 | furniture | pages [19] -->
m

<!-- b001820 | furniture | pages [19] -->
m

<!-- b001821 | furniture | pages [19] -->
m

<!-- b001822 | furniture | pages [19] -->
m

<!-- b001823 | furniture | pages [19] -->
m

<!-- b001824 | furniture | pages [19] -->
m

<!-- b001825 | furniture | pages [19] -->
m

<!-- b001826 | furniture | pages [19] -->
m

<!-- b001827 | furniture | pages [19] -->
m

<!-- b001828 | furniture | pages [19] -->
m

<!-- b001829 | furniture | pages [19] -->
m

<!-- b001830 | furniture | pages [19] -->
m

<!-- b001831 | furniture | pages [19] -->
m

<!-- b001832 | furniture | pages [19] -->
m

<!-- b001833 | furniture | pages [19] -->
m

<!-- b001834 | furniture | pages [19] -->
m

<!-- b001835 | furniture | pages [19] -->
m

<!-- b001836 | furniture | pages [19] -->
m

<!-- b001837 | furniture | pages [19] -->
m

<!-- b001838 | furniture | pages [19] -->
m

<!-- b001839 | furniture | pages [19] -->
m

<!-- b001840 | furniture | pages [19] -->
m

<!-- b001841 | furniture | pages [19] -->
m

<!-- b001842 | furniture | pages [19] -->
m

<!-- b001843 | furniture | pages [19] -->
m

<!-- b001844 | furniture | pages [19] -->
m

<!-- b001845 | furniture | pages [19] -->
m

<!-- b001846 | furniture | pages [19] -->
m

<!-- b001847 | furniture | pages [19] -->
m

<!-- b001848 | furniture | pages [19] -->
m

<!-- b001849 | furniture | pages [19] -->
m

<!-- b001850 | furniture | pages [19] -->
m

<!-- b001851 | furniture | pages [19] -->
m

<!-- b001852 | furniture | pages [19] -->
m

<!-- b001853 | furniture | pages [19] -->
m

<!-- b001854 | furniture | pages [19] -->
m

<!-- b001855 | furniture | pages [19] -->
m

<!-- b001856 | furniture | pages [19] -->
m

<!-- b001857 | furniture | pages [19] -->
m

<!-- b001858 | furniture | pages [19] -->
m

<!-- b001859 | furniture | pages [19] -->
m

<!-- b001860 | furniture | pages [19] -->
m

<!-- b001861 | furniture | pages [19] -->
m

<!-- b001862 | furniture | pages [19] -->
m

<!-- b001863 | furniture | pages [19] -->
m

<!-- b001864 | furniture | pages [19] -->
m

<!-- b001865 | furniture | pages [19] -->
m

<!-- b001866 | furniture | pages [19] -->
m

<!-- b001867 | furniture | pages [19] -->
m

<!-- b001868 | furniture | pages [19] -->
m

<!-- b001869 | furniture | pages [19] -->
m

<!-- b001870 | furniture | pages [19] -->
m

<!-- b001871 | furniture | pages [19] -->
m

<!-- b001872 | furniture | pages [19] -->
m

<!-- b001873 | furniture | pages [19] -->
m

<!-- b001874 | furniture | pages [19] -->
m

<!-- b001875 | furniture | pages [19] -->
m

<!-- b001876 | furniture | pages [19] -->
m

<!-- b001877 | furniture | pages [19] -->
m

<!-- b001878 | furniture | pages [19] -->
m

<!-- b001879 | furniture | pages [19] -->
m

<!-- b001880 | furniture | pages [19] -->
m

<!-- b001881 | furniture | pages [19] -->
m

<!-- b001882 | furniture | pages [19] -->
m

<!-- b001883 | furniture | pages [19] -->
m

<!-- b001884 | furniture | pages [19] -->
m

<!-- b001885 | furniture | pages [19] -->
m

<!-- b001886 | furniture | pages [19] -->
m

<!-- b001887 | furniture | pages [19] -->
m

<!-- b001888 | furniture | pages [19] -->
m

<!-- b001889 | furniture | pages [19] -->
m

<!-- b001890 | furniture | pages [19] -->
m

<!-- b001891 | furniture | pages [19] -->
m

<!-- b001892 | furniture | pages [19] -->
m

<!-- b001893 | furniture | pages [19] -->
m

<!-- b001894 | furniture | pages [19] -->
m

<!-- b001895 | furniture | pages [19] -->
m

<!-- b001896 | furniture | pages [19] -->
m

<!-- b001897 | furniture | pages [19] -->
m

<!-- b001898 | furniture | pages [19] -->
m

<!-- b001899 | furniture | pages [19] -->
m

<!-- b001900 | furniture | pages [19] -->
m

<!-- b001901 | furniture | pages [19] -->
m

<!-- b001902 | furniture | pages [19] -->
m

<!-- b001903 | furniture | pages [19] -->
m

<!-- b001904 | furniture | pages [19] -->
m

<!-- b001905 | furniture | pages [19] -->
m

<!-- b001906 | furniture | pages [19] -->
m

<!-- b001907 | furniture | pages [19] -->
m

<!-- b001908 | furniture | pages [19] -->
m

<!-- b001909 | furniture | pages [19] -->
m

<!-- b001910 | furniture | pages [19] -->
m

<!-- b001911 | furniture | pages [19] -->
m

<!-- b001912 | furniture | pages [19] -->
m

<!-- b001913 | furniture | pages [19] -->
m

<!-- b001914 | furniture | pages [19] -->
m

<!-- b001915 | furniture | pages [19] -->
m

<!-- b001916 | furniture | pages [19] -->
m

<!-- b001917 | furniture | pages [19] -->
m

<!-- b001918 | furniture | pages [19] -->
m

<!-- b001919 | furniture | pages [19] -->
m

<!-- b001920 | furniture | pages [19] -->
m

<!-- b001921 | furniture | pages [19] -->
m

<!-- b001922 | furniture | pages [19] -->
m

<!-- b001923 | furniture | pages [19] -->
m

<!-- b001924 | furniture | pages [19] -->
m

<!-- b001925 | furniture | pages [19] -->
m

<!-- b001926 | furniture | pages [19] -->
m

<!-- b001927 | furniture | pages [19] -->
m

<!-- b001928 | furniture | pages [19] -->
m

<!-- b001929 | furniture | pages [19] -->
m

<!-- b001930 | furniture | pages [19] -->
m

<!-- b001931 | furniture | pages [19] -->
m

<!-- b001932 | furniture | pages [19] -->
m

<!-- b001933 | furniture | pages [19] -->
m

<!-- b001934 | furniture | pages [19] -->
m

<!-- b001935 | furniture | pages [19] -->
m

<!-- b001936 | furniture | pages [19] -->
m

<!-- b001937 | furniture | pages [19] -->
m

<!-- b001938 | furniture | pages [19] -->
m

<!-- b001939 | furniture | pages [19] -->
m

<!-- b001940 | furniture | pages [19] -->
m

<!-- b001941 | furniture | pages [19] -->
m

<!-- b001942 | furniture | pages [19] -->
m

<!-- b001943 | furniture | pages [19] -->
m

<!-- b001944 | furniture | pages [19] -->
m

<!-- b001945 | furniture | pages [19] -->
m

<!-- b001946 | furniture | pages [19] -->
m

<!-- b001947 | furniture | pages [19] -->
m

<!-- b001948 | furniture | pages [19] -->
m

<!-- b001949 | furniture | pages [19] -->
m

<!-- b001950 | furniture | pages [20] -->
Team # 2510006

<!-- b001951 | furniture | pages [20] -->
Page 19

<!-- b001953 | caption | pages [20] -->
Table 6: Calculation of P-values for Coaches in Diﬀerent Coaching Periods

<!-- b001954 | heading | pages [20] -->
5.2 Selection of Three Countries and Speciﬁc Sports

<!-- b001955 | prose | pages [20] -->
To analyze the impact of great coaches on sports performance, we have selected the following three countries and their respective sports: China (Volleyball), India (Athletics), and Brazil (Gymnastics).

<!-- b001956 | prose | pages [20] -->
These selections are based on the following reasons: China’s volleyball team, under the leadership of Lang Ping, once achieved great success, but in recent years, their performance has declined, and the team urgently needs a great coach to revive its glory. India has great potential in sprinting, but due to a lack of systematic training and scientiﬁc guidance, a great coach could signiﬁcantly improve their performance. Brazil’s gymnastics has made progress in recent years, but still lags behind top countries (such as the United States and China), and a great coach could help them break through this bottleneck. Therefore, bringing in great coaches for these three sports is seen as a key factor in enhancing their international competitiveness.

<!-- b001957 | prose | pages [20] -->
A great coach should address the current challenges faced by these countries. For Chi- nas volleyball, a great coach can introduce advanced tactical systems, help improve the team’s overall competitiveness, especially through tactical innovation, with ﬂexible and var- ied strategies to cope with intense international competition. For Indias sprinting, after the introduction of a great coach, athletes will signiﬁcantly improve their physical ﬁtness and technical level through advanced training methods, particularly through strength training, technical analysis, and other specialized training to enhance explosiveness and speed. For Brazils gymnastics, a great coach can help athletes master higher-diﬃculty routines, im- prove their technical skills, and increase the execution and stability of their routines through technical analysis and specialized training.

<!-- b001958 | prose | pages [20] -->
By introducing great coaches, these three countries are expected to make signiﬁcant improvements in the respective sports. The expected impacts are as follows:

<!-- b001959 | prose | pages [20] -->
Country Sport Current Level Expected Level Main Impact Area China Volleyball Top 8 Top 3 Tactical Innovation India Athletics Top 5(Asia) Top 8 Scientiﬁc Training Brazil Gymnastics Top 20 Top 10 Technical Improvement

<!-- b001960 | caption | pages [20] -->
Table 7: Expected Impact of Hiring Great Coaches

<!-- b001961 | prose | pages [20] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

<!-- b001962 | furniture | pages [20] -->
2

<!-- b001963 | prose | pages [20] -->
m m m m m m m m m m m m m m m m m

<!-- b001964 | furniture | pages [20] -->
m

<!-- b001965 | furniture | pages [20] -->
m

<!-- b001966 | furniture | pages [20] -->
m

<!-- b001967 | furniture | pages [20] -->
m

<!-- b001968 | furniture | pages [20] -->
m

<!-- b001969 | furniture | pages [20] -->
m

<!-- b001970 | furniture | pages [20] -->
m

<!-- b001971 | furniture | pages [20] -->
m

<!-- b001972 | furniture | pages [20] -->
m

<!-- b001973 | furniture | pages [20] -->
m

<!-- b001974 | furniture | pages [20] -->
m

<!-- b001975 | furniture | pages [20] -->
m

<!-- b001976 | furniture | pages [20] -->
m

<!-- b001977 | furniture | pages [20] -->
m

<!-- b001978 | furniture | pages [20] -->
m

<!-- b001979 | furniture | pages [20] -->
m

<!-- b001980 | furniture | pages [20] -->
m

<!-- b001981 | furniture | pages [20] -->
m

<!-- b001982 | furniture | pages [20] -->
m

<!-- b001983 | furniture | pages [20] -->
m

<!-- b001984 | furniture | pages [20] -->
m

<!-- b001985 | furniture | pages [20] -->
m

<!-- b001986 | furniture | pages [20] -->
m

<!-- b001987 | furniture | pages [20] -->
m

<!-- b001988 | furniture | pages [20] -->
m

<!-- b001989 | furniture | pages [20] -->
m

<!-- b001990 | furniture | pages [20] -->
m

<!-- b001991 | furniture | pages [20] -->
m

<!-- b001992 | furniture | pages [20] -->
m

<!-- b001993 | furniture | pages [20] -->
m

<!-- b001994 | furniture | pages [20] -->
m

<!-- b001995 | furniture | pages [20] -->
m

<!-- b001996 | furniture | pages [20] -->
m

<!-- b001997 | furniture | pages [20] -->
m

<!-- b001998 | furniture | pages [20] -->
m

<!-- b001999 | furniture | pages [20] -->
m

<!-- b002000 | furniture | pages [20] -->
m

<!-- b002001 | furniture | pages [20] -->
m

<!-- b002002 | furniture | pages [20] -->
m

<!-- b002003 | furniture | pages [20] -->
m

<!-- b002004 | furniture | pages [20] -->
m

<!-- b002005 | furniture | pages [20] -->
m

<!-- b002006 | furniture | pages [20] -->
m

<!-- b002007 | furniture | pages [20] -->
m

<!-- b002008 | furniture | pages [20] -->
m

<!-- b002009 | furniture | pages [20] -->
m

<!-- b002010 | furniture | pages [20] -->
m

<!-- b002011 | furniture | pages [20] -->
m

<!-- b002012 | furniture | pages [20] -->
m

<!-- b002013 | furniture | pages [20] -->
m

<!-- b002014 | furniture | pages [20] -->
m

<!-- b002015 | furniture | pages [20] -->
m

<!-- b002016 | furniture | pages [20] -->
m

<!-- b002017 | furniture | pages [20] -->
m

<!-- b002018 | furniture | pages [20] -->
m

<!-- b002019 | furniture | pages [20] -->
m

<!-- b002020 | furniture | pages [20] -->
m

<!-- b002021 | furniture | pages [20] -->
m

<!-- b002022 | furniture | pages [20] -->
m

<!-- b002023 | furniture | pages [20] -->
m

<!-- b002024 | furniture | pages [20] -->
MATHmodels

<!-- b002025 | furniture | pages [20] -->
获取更多资讯

<!-- b002026 | furniture | pages [21] -->
Page 20

<!-- b002027 | furniture | pages [21] -->
Team # 2510006

<!-- b002028 | heading | pages [21] -->
Task 3: Recommendations

<!-- b002029 | prose | pages [21] -->
6

<!-- b002030 | prose | pages [21] -->
From an economic perspective, a country's GDP is a reflection of its overall economic strength. A higher GDP typically means that more financial resources can be invested in sports infrastructure, athlete training, and scientific research support. For instance, devel- oped countries like the United States and Japan can provide advanced training facilities, scientific nutrition plans, and professional coaching teams for their athletes. These factors directly enhance their competitiveness in the Olympics. Therefore, there should be a signif- icant positive correlation between GDP and Olympic medal count. In fact, based on the GDP data of the top 20 countries in medal counts for the 2024 Olympics, the log(GDP) has a strong correlation with the total medal count (the correlation coefficient r is ap- proximately 0.83), as shown in the figure below:

<!-- b002031 | prose | pages [21] -->
Linear Relationship between logGDP and Olympic Medal Counts 140 Legend

<!-- b002032 | prose | pages [21] -->
• Data Points 120 0-Linear Regression (y = 35.86x + 32.77) Correlation Coefficient: 0.83 100

<!-- b002033 | prose | pages [21] -->
80 Medal Counts 3 60

<!-- b002034 | prose | pages [21] -->
40

<!-- b002035 | prose | pages [21] -->
20

<!-- b002036 | prose | pages [21] -->
TNIK -20 -0.5 0.5 1.5 1 0 logGDP

<!-- b002037 | caption | pages [21] -->
Figure 21: Relationship between GDP and Medal counts

<!-- b002038 | prose | pages [21] -->
● For the i-th sport, the sum of the squares of the medal distribution across countries,

<!-- b002039 | prose | pages [21] -->
across countries. The smaller this value, the more evenly the medals are distributed, meaning that each country has a chance to win medals in this event. The ten events with the smallest values are: Wrestling, Athletics, Football, Taekwondo, Judo, Shooting, Canoe, Rowing, Gymnastics, and Sailing. As for countries with fewer medals or countries that have never won medals, they could improve their chances by bringing in a "great coach" to earn medals in these areas. Specifically, wrestling and taekwondo are low-cost, high-return medal investment events. Additionally, coastal countries could invest in Sailing.

<!-- b002040 | furniture | pages [22] -->
Team # 2510006

<!-- b002041 | furniture | pages [22] -->
Page 21

<!-- b002042 | heading | pages [22] -->
7 Model Evaluation

<!-- b002043 | heading | pages [22] -->
7.1 Sensitivity Analysis

<!-- b002044 | caption | pages [22] -->
Figure 23: 80% conﬁdence level

<!-- b002045 | caption | pages [22] -->
Figure 22: 60% conﬁdence level

<!-- b002046 | caption | pages [22] -->
Figure 24: 90% conﬁdence level

<!-- b002047 | caption | pages [22] -->
Figure 25: 95% conﬁdence level

<!-- b002048 | caption | pages [22] -->
Figure 26: 99% conﬁdence level

<!-- b002049 | prose | pages [22, 23] -->
关注数学模型 The total number of medals

<!-- b002050 | furniture | pages [22] -->
2

<!-- b002051 | furniture | pages [22] -->
MATHmodels

<!-- b002052 | furniture | pages [22] -->
获取更多资讯

<!-- b002053 | furniture | pages [23] -->
Team # 2510006

<!-- b002054 | furniture | pages [23] -->
Page 22

<!-- b002055 | caption | pages [23] -->
Table 8:

<!-- b002057 | caption | pages [23] -->
Table 9:

<!-- b002058 | prose | pages [23] -->
The number of gold medals varies with the correlation coeﬃcient varies with the correlation coeﬃcient

<!-- b002059 | prose | pages [23] -->
Country 0.3 0.4 0.5 0.6 0.7 Country 0.3 0.4 0.5 0.6 0.7 USA 139 139 139 139 139 USA 55 55 55 55 55 CHN 96 94 87 83 77 CHN 38 38 34 32 31 JPN 59 56 55 54 44 JPN 25 24 24 24 18 GBR 73 73 69 65 57 GBR 22 22 21 19 14 RUS 60 60 60 60 60 RUS 22 22 22 22 22 AUS 53 50 48 48 42 AUS 18 18 16 16 14 微信公众号：数学模型 FRA 63 61 58 55 43 FRA 17 16 15 14 10 NED 44 41 38 36 28 NED 17 15 15 15 11 GER 47 45 44 44 42 GER 14 13 13 13 13 KOR 32 31 29 27 25 KOR 15 15 13 11 10

<!-- b002060 | heading | pages [23] -->
8 Model Evaluation

<!-- b002061 | heading | pages [23] -->
Sensitivity Analysis

<!-- b002062 | prose | pages [23] -->
In the prediction model of each country’s medal counts and it’s interval, we initially assumed a conﬁdence interval of 90% and a value of 0.5 for parameter r, which is the threshold 微信号：MATHmodels for determining strong or weak correlation . Now we will take conﬁdence intervals of 60%, 80%, 95%, and 99% respectively to explore the range of values of medal prediction intervals for diﬀerent countries in diﬀerent conﬁdence intervals. Next, the values of the judgment parameter r will be taken as 0.3, 0.4, 0.6, and 0.7, respectively, to explore the changes in the expected total medal count and gold medal count of each country under diﬀerent judgment parameters.

<!-- b002063 | prose | pages [23] -->
Gradually observe the medal table prediction interval at each conﬁdence interval, and you will ﬁnd that as the conﬁdence value increases, the medal prediction interval for each country will also expand accordingly. Although the increase in conﬁdence level can broaden the prediction interval of medals for each country, the conﬁdence level does not aﬀect the medal prediction value. Let r be the parameter of the threshold for determining strong or weak correlation. The medal predictions for the United States and Russia are very stable: when r varies between 0.3-0.7, the total medal and gold medal predictions for the United States in 2028 remain at 139 and 55 respectively, while the total medal and gold medal predictions for Russia in 2028 remain at 60 and 22 respectively, demonstrating strong stability. The trend of predicted Chinese medals: As r increases from 0.3 to 0.7, the predicted total number of Chinese medals in 2028 decreases from 96 to 77, showing a strong decreasing trend. Situation in other countries: Most countries such as Japan, the United Kingdom, Australia, France, the Netherlands, Germany, South Korea, etc. also show a trend of decreasing total medal predictions as r increases.

<!-- b002064 | prose | pages [23] -->
Advantages and Disadvantages Analysis

<!-- b002065 | prose | pages [23] -->
Advantages:

<!-- b002066 | prose | pages [23, 24] -->
m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The number of gold medals varies with the correlation coeﬃcient varies with the correlation coeﬃcient m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Country 0.3 0.4 0.5 0.6 0.7 Country 0.3 0.4 0.5 0.6 0.7 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m USA 139 139 139 139 139 USA 55 55 55 55 55 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m CHN 96 94 87 83 77 CHN 38 38 34 32 31 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m JPN 59 56 55 54 44 JPN 25 24 24 24 18 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m GBR 73 73 69 65 57 GBR 22 22 21 19 14 RUS 60 60 60 60 60 RUS 22 22 22 22 22 AUS 53 50 48 48 42 AUS 18 18 16 16 14 FRA 63 61 58 55 43 FRA 17 16 15 14 10 NED 44 41 38 36 28 NED 17 15 15 15 11 GER 47 45 44 44 42 GER 14 13 13 13 13 KOR 32 31 29 27 25 KOR 15 15 13 11 10

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

<!-- b002276 | furniture | pages [23] -->
m

<!-- b002277 | furniture | pages [23] -->
m

<!-- b002278 | furniture | pages [23] -->
m

<!-- b002279 | furniture | pages [23] -->
m

<!-- b002280 | furniture | pages [23] -->
m

<!-- b002281 | furniture | pages [23] -->
m

<!-- b002282 | furniture | pages [23] -->
m

<!-- b002283 | furniture | pages [23] -->
m

<!-- b002284 | furniture | pages [23] -->
m

<!-- b002285 | furniture | pages [23] -->
m

<!-- b002286 | furniture | pages [23] -->
m

<!-- b002287 | furniture | pages [23] -->
m

<!-- b002288 | furniture | pages [23] -->
m

<!-- b002289 | furniture | pages [23] -->
m

<!-- b002290 | furniture | pages [23] -->
m

<!-- b002291 | furniture | pages [23] -->
m

<!-- b002292 | furniture | pages [23] -->
m

<!-- b002293 | furniture | pages [23] -->
m

<!-- b002294 | furniture | pages [23] -->
m

<!-- b002295 | furniture | pages [23] -->
m

<!-- b002296 | furniture | pages [23] -->
m

<!-- b002297 | furniture | pages [23] -->
m

<!-- b002298 | furniture | pages [23] -->
m

<!-- b002299 | furniture | pages [23] -->
m

<!-- b002300 | furniture | pages [23] -->
m

<!-- b002301 | furniture | pages [23] -->
m

<!-- b002302 | furniture | pages [23] -->
m

<!-- b002303 | furniture | pages [23] -->
m

<!-- b002304 | furniture | pages [23] -->
m

<!-- b002305 | furniture | pages [23] -->
m

<!-- b002306 | furniture | pages [23] -->
m

<!-- b002307 | furniture | pages [23] -->
m

<!-- b002308 | furniture | pages [23] -->
m

<!-- b002309 | furniture | pages [23] -->
m

<!-- b002310 | furniture | pages [23] -->
m

<!-- b002311 | furniture | pages [23] -->
m

<!-- b002312 | furniture | pages [23] -->
m

<!-- b002313 | furniture | pages [23] -->
m

<!-- b002314 | furniture | pages [23] -->
m

<!-- b002315 | furniture | pages [23] -->
m

<!-- b002316 | furniture | pages [23] -->
m

<!-- b002317 | furniture | pages [23] -->
m

<!-- b002318 | furniture | pages [23] -->
m

<!-- b002319 | furniture | pages [23] -->
m

<!-- b002320 | furniture | pages [23] -->
m

<!-- b002321 | furniture | pages [23] -->
m

<!-- b002322 | furniture | pages [23] -->
m

<!-- b002323 | furniture | pages [23] -->
m

<!-- b002324 | furniture | pages [23] -->
m

<!-- b002325 | furniture | pages [23] -->
m

<!-- b002326 | furniture | pages [23] -->
m

<!-- b002327 | furniture | pages [23] -->
m

<!-- b002328 | furniture | pages [23] -->
m

<!-- b002329 | furniture | pages [23] -->
m

<!-- b002330 | furniture | pages [23] -->
m

<!-- b002331 | furniture | pages [23] -->
m

<!-- b002332 | furniture | pages [23] -->
m

<!-- b002333 | furniture | pages [23] -->
m

<!-- b002334 | furniture | pages [23] -->
m

<!-- b002335 | furniture | pages [23] -->
m

<!-- b002336 | furniture | pages [23] -->
m

<!-- b002337 | furniture | pages [23] -->
m

<!-- b002338 | furniture | pages [23] -->
m

<!-- b002339 | furniture | pages [23] -->
m

<!-- b002340 | furniture | pages [23] -->
m

<!-- b002341 | furniture | pages [23] -->
m

<!-- b002342 | furniture | pages [23] -->
m

<!-- b002343 | furniture | pages [23] -->
m

<!-- b002344 | furniture | pages [23] -->
m

<!-- b002345 | furniture | pages [23] -->
m

<!-- b002346 | furniture | pages [23] -->
m

<!-- b002347 | furniture | pages [23] -->
m

<!-- b002348 | furniture | pages [23] -->
m

<!-- b002349 | furniture | pages [23] -->
m

<!-- b002350 | furniture | pages [23] -->
m

<!-- b002351 | furniture | pages [23] -->
m

<!-- b002352 | furniture | pages [23] -->
m

<!-- b002353 | furniture | pages [23] -->
m

<!-- b002354 | furniture | pages [23] -->
m

<!-- b002355 | furniture | pages [23] -->
m

<!-- b002356 | furniture | pages [23] -->
m

<!-- b002357 | furniture | pages [23] -->
m

<!-- b002358 | furniture | pages [23] -->
m

<!-- b002359 | furniture | pages [23] -->
m

<!-- b002360 | furniture | pages [23] -->
m

<!-- b002361 | furniture | pages [23] -->
m

<!-- b002362 | furniture | pages [23] -->
m

<!-- b002363 | furniture | pages [23] -->
m

<!-- b002364 | furniture | pages [23] -->
m

<!-- b002365 | furniture | pages [23] -->
m

<!-- b002366 | furniture | pages [23] -->
m

<!-- b002367 | furniture | pages [23] -->
m

<!-- b002368 | furniture | pages [23] -->
m

<!-- b002369 | furniture | pages [23] -->
m

<!-- b002370 | furniture | pages [23] -->
m

<!-- b002371 | furniture | pages [23] -->
m

<!-- b002372 | furniture | pages [23] -->
m

<!-- b002373 | furniture | pages [23] -->
m

<!-- b002374 | furniture | pages [23] -->
m

<!-- b002375 | furniture | pages [23] -->
m

<!-- b002376 | furniture | pages [23] -->
m

<!-- b002377 | furniture | pages [23] -->
m

<!-- b002378 | furniture | pages [23] -->
m

<!-- b002379 | furniture | pages [23] -->
m

<!-- b002380 | furniture | pages [23] -->
m

<!-- b002381 | furniture | pages [23] -->
m

<!-- b002382 | furniture | pages [23] -->
m

<!-- b002383 | furniture | pages [23] -->
m

<!-- b002384 | furniture | pages [23] -->
m

<!-- b002385 | furniture | pages [23] -->
m

<!-- b002386 | furniture | pages [23] -->
m

<!-- b002387 | furniture | pages [23] -->
m

<!-- b002388 | furniture | pages [23] -->
m

<!-- b002389 | furniture | pages [23] -->
m

<!-- b002390 | furniture | pages [23] -->
m

<!-- b002391 | furniture | pages [24] -->
Team # 2510006

<!-- b002392 | furniture | pages [24] -->
Page 23

<!-- b002393 | caption | pages [24] -->
Table 10: The total number of medals

<!-- b002394 | caption | pages [24] -->
Table 11:

<!-- b002396 | prose | pages [24] -->
1. Screening of Eﬀective Information: For Task 1, our prediction model is mainly based on the Olympic data from 2000-2024. This is because the data from the 1996 Olympics and earlier are too old, and to avoid potential political factors aﬀecting participation or countries merging/breaking up before 1996.

<!-- b002397 | prose | pages [24] -->
2. Considering the impact of newly established sports events on the host country and countries excelling in these events, we predict the medal performance in new events by gathering league rankings for these events globally and using Monte Carlo simulations to make accurate predictions.

<!-- b002398 | prose | pages [24] -->
3. Considering the diﬀerent peak performance cycles of athletes in various sports cat- egories, we categorize the Olympic events into six major categories: Athletics, Aquatics, Ball Sports, Combat Sports, Gymnastics, and Racing. This categorization allows for more accurate predictions for each country in diﬀerent types of events.

<!-- b002399 | prose | pages [24] -->
4. When calculating the medals for a country in a speciﬁc sport, we consider the trend of increasing or decreasing medals and determine whether to use linear forecasting or average values based on the correlation with time.

<!-- b002400 | prose | pages [24] -->
5. Due to the large number of events, we cleverly use Poisson distribution to calculate the medal distribution function for each country and then simulate the 90% conﬁdence interval for each country’s medal count using Random Forest.

<!-- b002401 | prose | pages [24] -->
Disadvantages:

<!-- b002402 | prose | pages [24] -->
1. Political factors have not been considered, such as whether countries like Russia will participate in the 2028 Los Angeles Olympics.

<!-- b002403 | prose | pages [24] -->
2. For countries with fewer medals, the Poisson distribution’s ﬁtted distribution function may lead to signiﬁcant uncertainty, making the predictions unstable.

<!-- b002404 | prose | pages [24] -->
3. Due to the large volume of data required for the six categories of sports and the per- formances of each category in diﬀerent Olympic editions, the program can be slow, resulting

<!-- b002405 | prose | pages [24, 25] -->
关注数学模型 in high time costs.

<!-- b002406 | furniture | pages [24] -->
2

<!-- b002407 | furniture | pages [24] -->
MATHmodels

<!-- b002408 | furniture | pages [24] -->
获取更多资讯

<!-- b002409 | furniture | pages [25] -->
Team # 2510006

<!-- b002410 | furniture | pages [25] -->
Page 24

<!-- b002412 | prose | pages [25] -->
4. The win-rate model used to calculate the event points for new sports does not accu- rately represent the real win rates.

<!-- b002413 | heading | pages [25] -->
9 Reference

<!-- b002414 | references | pages [25] -->
微信公众号：数学模型

<!-- b002415 | heading | pages [25] -->
References

<!-- b002416 | references | pages [25] -->
[1] Singh, R. K., Rani, M., Bhagavathula, A. S., Sah, R., Rodriguez-Morales, A. J., Kalita,

<!-- b002417 | references | pages [25] -->
H., Nanda, C., Sharma, S., Sharma, Y. D., Rabaan, A. A., Rahmani, J., & Kumar, P.

<!-- b002418 | references | pages [25] -->
(2020). Prediction of the COVID-19 Pandemic for the Top 15 Aﬀected Countries: Ad-

<!-- b002419 | references | pages [25] -->
vanced Autoregressive Integrated Moving Average (ARIMA) Model. JMIR Public Health

<!-- b002420 | references | pages [25] -->
Surveill, 6(2), e19115. DOI: https://doi.org/10.2196/19115

<!-- b002421 | references | pages [25] -->
[2] Unknown Author. (2012). A Clustering Method Based on K-Means Algorithm. Physics

<!-- b002422 | references | pages [25] -->
Procedia, 25, 1104–1109. DOI: https://doi.org/10.1016/j.phpro.2012.03.206

<!-- b002423 | references | pages [25] -->
微信号：MATHmodels

<!-- b002424 | references | pages [25] -->
[3] World Lacrosse. (2023). World Lacrosse Rankings. Retrieved October 1, 2023, from

<!-- b002425 | references | pages [25] -->
https://worldlacrosse.sport/the-game/world-rankings/

<!-- b002426 | references | pages [25] -->
[4] PSA World Tour. (2023). PSA Squash Rankings. Retrieved October 1, 2023, from https:

<!-- b002427 | references | pages [25] -->
//www.psasquashtour.com/rankings/

<!-- b002428 | references | pages [25] -->
[5] International

<!-- b002429 | references | pages [25] -->
Federation

<!-- b002430 | references | pages [25] -->
of

<!-- b002431 | references | pages [25] -->
American

<!-- b002432 | references | pages [25] -->
Football.

<!-- b002433 | references | pages [25] -->
(2023).

<!-- b002434 | references | pages [25] -->
IFAF

<!-- b002435 | references | pages [25] -->
World

<!-- b002436 | references | pages [25] -->
Rank-

<!-- b002437 | references | pages [25] -->
ings.

<!-- b002438 | references | pages [25] -->
Retrieved

<!-- b002439 | references | pages [25] -->
October

<!-- b002440 | references | pages [25] -->
1,

<!-- b002441 | references | pages [25] -->
2023,

<!-- b002442 | references | pages [25] -->
from

<!-- b002443 | references | pages [25] -->
https://www.americanfootball.sport/

<!-- b002444 | references | pages [25] -->
ifaf-world-rankings/

<!-- b002445 | references | pages [25] -->
[6] United Nations. (2023). United Nations Data. Retrieved October 1, 2023, from https:

<!-- b002446 | references | pages [25] -->
//data.un.org/

<!-- b002447 | references | pages [25] -->
[7] International Cricket Council. (2023). ICC Cricket Rankings. Retrieved October 1, 2023,

<!-- b002448 | references | pages [25] -->
from https://www.icc-cricket.com/rankings#mens-team-rankings

<!-- b002449 | references | pages [25] -->
[8] World Baseball Softball Confederation. (2023). WBSC Rankings. Retrieved October 1,

<!-- b002450 | references | pages [25] -->
2023, from https://www.wbsc.org/en/rankings

<!-- b002451 | references | pages [25] -->
m

<!-- b002452 | references | pages [25] -->
m

<!-- b002453 | references | pages [25] -->
m

<!-- b002454 | references | pages [25] -->
m

<!-- b002455 | references | pages [25] -->
m

<!-- b002456 | references | pages [25] -->
m

<!-- b002457 | references | pages [25] -->
m

<!-- b002458 | references | pages [25] -->
m

<!-- b002459 | references | pages [25] -->
m

<!-- b002460 | references | pages [25] -->
m

<!-- b002461 | references | pages [25] -->
m

<!-- b002462 | references | pages [25] -->
m

<!-- b002463 | references | pages [25] -->
m

<!-- b002464 | references | pages [25] -->
m

<!-- b002465 | references | pages [25] -->
m

<!-- b002466 | references | pages [25] -->
m

<!-- b002467 | references | pages [25] -->
m

<!-- b002468 | references | pages [25] -->
m

<!-- b002469 | references | pages [25] -->
m

<!-- b002470 | references | pages [25] -->
m

<!-- b002471 | references | pages [25] -->
m

<!-- b002472 | references | pages [25] -->
m

<!-- b002473 | references | pages [25] -->
m

<!-- b002474 | references | pages [25] -->
m

<!-- b002475 | references | pages [25] -->
m

<!-- b002476 | references | pages [25] -->
m

<!-- b002477 | references | pages [25] -->
m

<!-- b002478 | references | pages [25] -->
m

<!-- b002479 | references | pages [25] -->
m

<!-- b002480 | references | pages [25] -->
m

<!-- b002481 | references | pages [25] -->
m

<!-- b002482 | references | pages [25] -->
m

<!-- b002483 | references | pages [25] -->
m

<!-- b002484 | references | pages [25] -->
m

<!-- b002485 | references | pages [25] -->
m

<!-- b002486 | references | pages [25] -->
m

<!-- b002487 | references | pages [25] -->
m

<!-- b002488 | references | pages [25] -->
m

<!-- b002489 | references | pages [25] -->
m

<!-- b002490 | references | pages [25] -->
m

<!-- b002491 | references | pages [25] -->
m

<!-- b002492 | references | pages [25] -->
m

<!-- b002493 | references | pages [25] -->
m

<!-- b002494 | references | pages [25] -->
m

<!-- b002495 | references | pages [25] -->
m

<!-- b002496 | references | pages [25] -->
m

<!-- b002497 | references | pages [25] -->
m

<!-- b002498 | references | pages [25] -->
m

<!-- b002499 | references | pages [25] -->
m

<!-- b002500 | references | pages [25] -->
m

<!-- b002501 | references | pages [25] -->
m

<!-- b002502 | references | pages [25] -->
m

<!-- b002503 | references | pages [25] -->
m

<!-- b002504 | references | pages [25] -->
m

<!-- b002505 | references | pages [25] -->
m

<!-- b002506 | references | pages [25] -->
m

<!-- b002507 | references | pages [25] -->
m

<!-- b002508 | references | pages [25] -->
m

<!-- b002509 | references | pages [25] -->
m

<!-- b002510 | references | pages [25] -->
m

<!-- b002511 | references | pages [25] -->
m

<!-- b002512 | references | pages [25] -->
m

<!-- b002513 | references | pages [25] -->
m

<!-- b002514 | references | pages [25] -->
m

<!-- b002515 | references | pages [25] -->
m

<!-- b002516 | references | pages [25] -->
m

<!-- b002517 | references | pages [25] -->
m

<!-- b002518 | references | pages [25] -->
m

<!-- b002519 | references | pages [25] -->
m

<!-- b002520 | references | pages [25] -->
m

<!-- b002521 | references | pages [25] -->
m

<!-- b002522 | references | pages [25] -->
m

<!-- b002523 | references | pages [25] -->
m

<!-- b002524 | references | pages [25] -->
m

<!-- b002525 | references | pages [25] -->
m

<!-- b002526 | references | pages [25] -->
m

<!-- b002527 | references | pages [25] -->
m

<!-- b002528 | references | pages [25] -->
m

<!-- b002529 | references | pages [25] -->
m

<!-- b002530 | references | pages [25] -->
m

<!-- b002531 | references | pages [25] -->
m

<!-- b002532 | references | pages [25] -->
m

<!-- b002533 | references | pages [25] -->
m

<!-- b002534 | references | pages [25] -->
m

<!-- b002535 | references | pages [25] -->
m

<!-- b002536 | references | pages [25] -->
m

<!-- b002537 | references | pages [25] -->
m

<!-- b002538 | references | pages [25] -->
m

<!-- b002539 | references | pages [25] -->
m

<!-- b002540 | references | pages [25] -->
m

<!-- b002541 | references | pages [25] -->
m

<!-- b002542 | references | pages [25] -->
m

<!-- b002543 | references | pages [25] -->
m

<!-- b002544 | references | pages [25] -->
m

<!-- b002545 | references | pages [25] -->
m

<!-- b002546 | references | pages [25] -->
m

<!-- b002547 | references | pages [25] -->
m

<!-- b002548 | references | pages [25] -->
m

<!-- b002549 | references | pages [25] -->
m

<!-- b002550 | references | pages [25] -->
m

<!-- b002551 | references | pages [25] -->
m

<!-- b002552 | references | pages [25] -->
m

<!-- b002553 | references | pages [25] -->
m

<!-- b002554 | references | pages [25] -->
m

<!-- b002555 | references | pages [25] -->
m

<!-- b002556 | references | pages [25] -->
m

<!-- b002557 | references | pages [25] -->
m

<!-- b002558 | references | pages [25] -->
m

<!-- b002559 | references | pages [25] -->
m

<!-- b002560 | references | pages [25] -->
m

<!-- b002561 | references | pages [25] -->
m

<!-- b002562 | references | pages [25] -->
m

<!-- b002563 | references | pages [25] -->
m

<!-- b002564 | references | pages [25] -->
m

<!-- b002565 | references | pages [25] -->
m

<!-- b002566 | references | pages [25] -->
m

<!-- b002567 | references | pages [25] -->
m

<!-- b002568 | references | pages [25] -->
m

<!-- b002569 | references | pages [25] -->
m

<!-- b002570 | references | pages [25] -->
m

<!-- b002571 | references | pages [25] -->
m

<!-- b002572 | references | pages [25] -->
m

<!-- b002573 | references | pages [25] -->
m

<!-- b002574 | references | pages [25] -->
m

<!-- b002575 | references | pages [25] -->
m

<!-- b002576 | references | pages [25] -->
m

<!-- b002577 | references | pages [25] -->
m

<!-- b002578 | references | pages [25] -->
m

<!-- b002579 | references | pages [25] -->
m

<!-- b002580 | references | pages [25] -->
m

<!-- b002581 | references | pages [25] -->
m

<!-- b002582 | references | pages [25] -->
m

<!-- b002583 | references | pages [25] -->
m

<!-- b002584 | references | pages [25] -->
m

<!-- b002585 | references | pages [25] -->
m

<!-- b002586 | references | pages [25] -->
m

<!-- b002587 | references | pages [25] -->
m

<!-- b002588 | references | pages [25] -->
m

<!-- b002589 | references | pages [25] -->
m

<!-- b002590 | references | pages [25] -->
m

<!-- b002591 | references | pages [25] -->
m

<!-- b002592 | references | pages [25] -->
m

<!-- b002593 | references | pages [25] -->
m

<!-- b002594 | references | pages [25] -->
m

<!-- b002595 | references | pages [25] -->
m

<!-- b002596 | references | pages [25] -->
m

<!-- b002597 | references | pages [25] -->
m

<!-- b002598 | references | pages [25] -->
m

<!-- b002599 | references | pages [25] -->
m

<!-- b002600 | references | pages [25] -->
m

<!-- b002601 | references | pages [25] -->
m

<!-- b002602 | references | pages [25] -->
m

<!-- b002603 | references | pages [25] -->
m

<!-- b002604 | references | pages [25] -->
m

<!-- b002605 | references | pages [25] -->
m

<!-- b002606 | references | pages [25] -->
m

<!-- b002607 | references | pages [25] -->
m

<!-- b002608 | references | pages [25] -->
m

<!-- b002609 | references | pages [25] -->
m

<!-- b002610 | references | pages [25] -->
m

<!-- b002611 | references | pages [25] -->
m

<!-- b002612 | references | pages [25] -->
m

<!-- b002613 | references | pages [25] -->
m

<!-- b002614 | references | pages [25] -->
m

<!-- b002615 | references | pages [25] -->
m

<!-- b002616 | references | pages [25] -->
m

<!-- b002617 | references | pages [25] -->
m

<!-- b002618 | references | pages [25] -->
m

<!-- b002619 | references | pages [25] -->
m

<!-- b002620 | references | pages [25] -->
m

<!-- b002621 | references | pages [25] -->
m

<!-- b002622 | references | pages [25] -->
m

<!-- b002623 | references | pages [25] -->
m

<!-- b002624 | references | pages [25] -->
m

<!-- b002625 | references | pages [25] -->
m

<!-- b002626 | references | pages [25] -->
m

<!-- b002627 | references | pages [25] -->
m

<!-- b002628 | references | pages [25] -->
m

<!-- b002629 | references | pages [25] -->
m

<!-- b002630 | references | pages [25] -->
m

<!-- b002631 | references | pages [25] -->
m

<!-- b002632 | references | pages [25] -->
m

<!-- b002633 | references | pages [25] -->
m

<!-- b002634 | references | pages [25] -->
m

<!-- b002635 | references | pages [25] -->
m

<!-- b002636 | references | pages [25] -->
m

<!-- b002637 | references | pages [25] -->
m

<!-- b002638 | references | pages [25] -->
m

<!-- b002639 | references | pages [25] -->
m

<!-- b002640 | references | pages [25] -->
m

<!-- b002641 | references | pages [25] -->
m

<!-- b002642 | references | pages [25] -->
m

<!-- b002643 | references | pages [25] -->
m

<!-- b002644 | references | pages [25] -->
m

<!-- b002645 | references | pages [25] -->
m

<!-- b002646 | references | pages [25] -->
m

<!-- b002647 | references | pages [25] -->
m

<!-- b002648 | references | pages [25] -->
m

<!-- b002649 | references | pages [25] -->
m

<!-- b002650 | references | pages [25] -->
m

<!-- b002651 | references | pages [25] -->
m

<!-- b002652 | references | pages [25] -->
m

<!-- b002653 | references | pages [25] -->
m

<!-- b002654 | references | pages [25] -->
m

<!-- b002655 | references | pages [25] -->
m

<!-- b002656 | references | pages [25] -->
m

<!-- b002657 | references | pages [25] -->
m

<!-- b002658 | references | pages [25] -->
m

<!-- b002659 | references | pages [25] -->
m

<!-- b002660 | references | pages [25] -->
m

<!-- b002661 | references | pages [25] -->
m

<!-- b002662 | references | pages [25] -->
m

<!-- b002663 | references | pages [25] -->
m

<!-- b002664 | references | pages [25] -->
m

<!-- b002665 | references | pages [25] -->
m

<!-- b002666 | references | pages [25] -->
m

<!-- b002667 | references | pages [25] -->
m

<!-- b002668 | references | pages [25] -->
m

<!-- b002669 | references | pages [25] -->
m

<!-- b002670 | references | pages [25] -->
m

<!-- b002671 | references | pages [25] -->
m

<!-- b002672 | references | pages [25] -->
m

<!-- b002673 | references | pages [25] -->
m

<!-- b002674 | references | pages [25] -->
m

<!-- b002675 | references | pages [25] -->
m

<!-- b002676 | references | pages [25] -->
m

<!-- b002677 | references | pages [25] -->
m

<!-- b002678 | references | pages [25] -->
m

<!-- b002679 | references | pages [25] -->
m

<!-- b002680 | references | pages [25] -->
m

<!-- b002681 | furniture | pages [25] -->
m

<!-- b002682 | furniture | pages [25] -->
m

<!-- b002683 | furniture | pages [25] -->
m

<!-- b002684 | furniture | pages [25] -->
m

<!-- b002685 | furniture | pages [25] -->
m

<!-- b002686 | furniture | pages [25] -->
m

<!-- b002687 | furniture | pages [25] -->
m

<!-- b002688 | furniture | pages [25] -->
m

<!-- b002689 | furniture | pages [25] -->
m

<!-- b002690 | furniture | pages [25] -->
m

<!-- b002691 | furniture | pages [25] -->
m

<!-- b002692 | furniture | pages [25] -->
m

<!-- b002693 | furniture | pages [25] -->
m

<!-- b002694 | furniture | pages [25] -->
m

<!-- b002695 | furniture | pages [25] -->
m

<!-- b002696 | furniture | pages [25] -->
m

<!-- b002697 | furniture | pages [25] -->
m

<!-- b002698 | furniture | pages [25] -->
m

<!-- b002699 | furniture | pages [25] -->
m

<!-- b002700 | furniture | pages [25] -->
m

<!-- b002701 | furniture | pages [25] -->
m

<!-- b002702 | furniture | pages [25] -->
m

<!-- b002703 | furniture | pages [25] -->
m

<!-- b002704 | furniture | pages [25] -->
m

<!-- b002705 | furniture | pages [25] -->
m

<!-- b002706 | furniture | pages [25] -->
m

<!-- b002707 | furniture | pages [25] -->
m

<!-- b002708 | furniture | pages [25] -->
m

<!-- b002709 | furniture | pages [25] -->
m

<!-- b002710 | furniture | pages [25] -->
m

<!-- b002711 | furniture | pages [25] -->
m

<!-- b002712 | furniture | pages [25] -->
m

<!-- b002713 | furniture | pages [25] -->
m

<!-- b002714 | furniture | pages [25] -->
m

<!-- b002715 | furniture | pages [25] -->
m

<!-- b002716 | furniture | pages [25] -->
m

<!-- b002717 | furniture | pages [25] -->
m

<!-- b002718 | furniture | pages [25] -->
m

<!-- b002719 | furniture | pages [25] -->
m

<!-- b002720 | furniture | pages [25] -->
m

<!-- b002721 | furniture | pages [25] -->
m

<!-- b002722 | furniture | pages [25] -->
m

<!-- b002723 | furniture | pages [25] -->
m

<!-- b002724 | furniture | pages [25] -->
m

<!-- b002725 | furniture | pages [25] -->
m

<!-- b002726 | furniture | pages [25] -->
m

<!-- b002727 | furniture | pages [25] -->
m

<!-- b002728 | furniture | pages [25] -->
m

<!-- b002729 | furniture | pages [25] -->
m

<!-- b002730 | furniture | pages [25] -->
m

<!-- b002731 | furniture | pages [25] -->
m

<!-- b002732 | furniture | pages [25] -->
m

<!-- b002733 | furniture | pages [25] -->
m

<!-- b002734 | furniture | pages [25] -->
m

<!-- b002735 | furniture | pages [25] -->
m

<!-- b002736 | furniture | pages [25] -->
m

<!-- b002737 | furniture | pages [25] -->
m

<!-- b002738 | furniture | pages [25] -->
m

<!-- b002739 | furniture | pages [25] -->
m

<!-- b002740 | furniture | pages [25] -->
m

<!-- b002741 | furniture | pages [25] -->
m

<!-- b002742 | furniture | pages [25] -->
m

<!-- b002743 | furniture | pages [25] -->
m

<!-- b002744 | furniture | pages [25] -->
m

<!-- b002745 | furniture | pages [25] -->
m

<!-- b002746 | furniture | pages [25] -->
m

<!-- b002747 | furniture | pages [25] -->
m

<!-- b002748 | furniture | pages [25] -->
m

<!-- b002749 | furniture | pages [25] -->
m

<!-- b002750 | furniture | pages [25] -->
m

<!-- b002751 | furniture | pages [25] -->
m

<!-- b002752 | furniture | pages [25] -->
m

<!-- b002753 | furniture | pages [25] -->
m

<!-- b002754 | furniture | pages [25] -->
m

<!-- b002755 | furniture | pages [25] -->
m

<!-- b002756 | furniture | pages [25] -->
m

<!-- b002757 | furniture | pages [25] -->
m

<!-- b002758 | furniture | pages [25] -->
m

<!-- b002759 | furniture | pages [25] -->
m

<!-- b002760 | furniture | pages [25] -->
m

<!-- b002761 | furniture | pages [25] -->
m

<!-- b002762 | furniture | pages [25] -->
m

<!-- b002763 | furniture | pages [25] -->
m

<!-- b002764 | furniture | pages [25] -->
m

<!-- b002765 | furniture | pages [25] -->
m

<!-- b002766 | furniture | pages [25] -->
m

<!-- b002767 | furniture | pages [25] -->
m

<!-- b002768 | furniture | pages [25] -->
m

<!-- b002769 | furniture | pages [25] -->
m

<!-- b002770 | furniture | pages [25] -->
m

<!-- b002771 | furniture | pages [25] -->
m

<!-- b002772 | furniture | pages [25] -->
m

<!-- b002773 | furniture | pages [25] -->
m

<!-- b002774 | furniture | pages [25] -->
m

<!-- b002775 | furniture | pages [25] -->
m

<!-- b002776 | furniture | pages [25] -->
m

<!-- b002777 | furniture | pages [25] -->
m

<!-- b002778 | furniture | pages [25] -->
m

<!-- b002779 | furniture | pages [25] -->
m

<!-- b002780 | furniture | pages [25] -->
m

<!-- b002781 | furniture | pages [25] -->
m

<!-- b002782 | furniture | pages [25] -->
m

<!-- b002783 | furniture | pages [25] -->
m

<!-- b002784 | furniture | pages [25] -->
m

<!-- b002785 | furniture | pages [25] -->
m

<!-- b002786 | furniture | pages [25] -->
m

<!-- b002787 | furniture | pages [25] -->
m

<!-- b002788 | furniture | pages [25] -->
m

<!-- b002789 | furniture | pages [25] -->
m

<!-- b002790 | furniture | pages [25] -->
m

<!-- b002791 | furniture | pages [25] -->
m

<!-- b002792 | furniture | pages [25] -->
m

<!-- b002793 | furniture | pages [25] -->
m

<!-- b002794 | furniture | pages [25] -->
m

<!-- b002795 | furniture | pages [25] -->
m

<!-- b002796 | furniture | pages [25] -->
m

<!-- b002797 | furniture | pages [25] -->
m

<!-- b002798 | furniture | pages [25] -->
m

<!-- b002799 | furniture | pages [25] -->
m

<!-- b002800 | furniture | pages [25] -->
m

<!-- b002801 | furniture | pages [25] -->
m

<!-- b002802 | furniture | pages [25] -->
m

<!-- b002803 | furniture | pages [25] -->
m

<!-- b002804 | furniture | pages [25] -->
m

<!-- b002805 | furniture | pages [25] -->
m

<!-- b002806 | furniture | pages [25] -->
m

<!-- b002807 | furniture | pages [25] -->
m

<!-- b002808 | furniture | pages [25] -->
m

<!-- b002809 | furniture | pages [25] -->
m

<!-- b002810 | furniture | pages [25] -->
m

<!-- b002811 | furniture | pages [25] -->
m

<!-- b002812 | furniture | pages [25] -->
m

<!-- b002813 | furniture | pages [25] -->
m

<!-- b002814 | furniture | pages [25] -->
m

<!-- b002815 | furniture | pages [25] -->
m

<!-- b002816 | furniture | pages [25] -->
m

<!-- b002817 | furniture | pages [25] -->
m

<!-- b002818 | furniture | pages [25] -->
m

<!-- b002819 | furniture | pages [25] -->
m

<!-- b002820 | furniture | pages [25] -->
m

<!-- b002821 | furniture | pages [25] -->
m

<!-- b002822 | furniture | pages [25] -->
m

<!-- b002823 | furniture | pages [25] -->
m

<!-- b002824 | furniture | pages [25] -->
m

<!-- b002825 | furniture | pages [25] -->
m

<!-- b002826 | furniture | pages [25] -->
m

<!-- b002827 | furniture | pages [25] -->
m

<!-- b002828 | furniture | pages [25] -->
m

<!-- b002829 | furniture | pages [25] -->
m

<!-- b002830 | furniture | pages [25] -->
m

<!-- b002831 | furniture | pages [25] -->
m

<!-- b002832 | furniture | pages [25] -->
m

<!-- b002833 | furniture | pages [25] -->
m

<!-- b002834 | furniture | pages [25] -->
m

<!-- b002835 | furniture | pages [25] -->
m

<!-- b002836 | furniture | pages [25] -->
m

<!-- b002837 | furniture | pages [25] -->
m

<!-- b002838 | furniture | pages [25] -->
m

<!-- b002839 | furniture | pages [25] -->
m

<!-- b002840 | furniture | pages [25] -->
m

<!-- b002841 | furniture | pages [25] -->
m

<!-- b002842 | furniture | pages [25] -->
m

<!-- b002843 | furniture | pages [25] -->
m

<!-- b002844 | furniture | pages [25] -->
m

<!-- b002845 | furniture | pages [25] -->
m

<!-- b002846 | furniture | pages [25] -->
m

<!-- b002847 | furniture | pages [25] -->
m

<!-- b002848 | furniture | pages [25] -->
m

<!-- b002849 | furniture | pages [25] -->
m

<!-- b002850 | furniture | pages [25] -->
m

<!-- b002851 | furniture | pages [25] -->
m

<!-- b002852 | furniture | pages [25] -->
m

<!-- b002853 | furniture | pages [25] -->
m

<!-- b002854 | furniture | pages [25] -->
m

<!-- b002855 | furniture | pages [25] -->
m

<!-- b002856 | furniture | pages [25] -->
m

<!-- b002857 | furniture | pages [25] -->
m

<!-- b002858 | furniture | pages [25] -->
m

<!-- b002859 | furniture | pages [25] -->
m

<!-- b002860 | furniture | pages [25] -->
m

<!-- b002861 | furniture | pages [25] -->
m

<!-- b002862 | furniture | pages [25] -->
m

<!-- b002863 | furniture | pages [25] -->
m

<!-- b002864 | furniture | pages [25] -->
m

<!-- b002865 | furniture | pages [25] -->
m

<!-- b002866 | furniture | pages [25] -->
m

<!-- b002867 | furniture | pages [25] -->
m

<!-- b002868 | furniture | pages [25] -->
m

<!-- b002869 | furniture | pages [25] -->
m

<!-- b002870 | furniture | pages [25] -->
m

<!-- b002871 | furniture | pages [25] -->
m

<!-- b002872 | furniture | pages [25] -->
m

<!-- b002873 | furniture | pages [25] -->
m

<!-- b002874 | furniture | pages [25] -->
m

<!-- b002875 | furniture | pages [25] -->
m

<!-- b002876 | furniture | pages [25] -->
m

<!-- b002877 | furniture | pages [25] -->
m

<!-- b002878 | furniture | pages [25] -->
m

<!-- b002879 | furniture | pages [25] -->
m

<!-- b002880 | furniture | pages [25] -->
m

<!-- b002881 | furniture | pages [25] -->
m

<!-- b002882 | furniture | pages [25] -->
m

<!-- b002883 | furniture | pages [25] -->
m

<!-- b002884 | furniture | pages [25] -->
m

<!-- b002885 | furniture | pages [25] -->
m

<!-- b002886 | furniture | pages [25] -->
m

<!-- b002887 | furniture | pages [25] -->
m

<!-- b002888 | furniture | pages [25] -->
m

<!-- b002889 | furniture | pages [25] -->
m

<!-- b002890 | furniture | pages [25] -->
m

<!-- b002891 | furniture | pages [25] -->
m

<!-- b002892 | furniture | pages [25] -->
m

<!-- b002893 | furniture | pages [25] -->
m

<!-- b002894 | furniture | pages [25] -->
m

<!-- b002895 | furniture | pages [25] -->
m

<!-- b002896 | furniture | pages [25] -->
m

<!-- b002897 | furniture | pages [25] -->
m

<!-- b002898 | furniture | pages [25] -->
m

<!-- b002899 | furniture | pages [25] -->
m

<!-- b002900 | furniture | pages [25] -->
m

<!-- b002901 | furniture | pages [25] -->
m

<!-- b002902 | furniture | pages [25] -->
m

<!-- b002903 | furniture | pages [25] -->
m

<!-- b002904 | furniture | pages [25] -->
m

<!-- b002905 | furniture | pages [25] -->
m

<!-- b002906 | furniture | pages [25] -->
m

<!-- b002907 | furniture | pages [25] -->
m

<!-- b002908 | furniture | pages [25] -->
m

<!-- b002909 | furniture | pages [25] -->
m

<!-- b002910 | furniture | pages [25] -->
m

<!-- b002911 | furniture | pages [25] -->
m

<!-- b002912 | furniture | pages [25] -->
m

<!-- b002913 | furniture | pages [25] -->
m

<!-- b002914 | furniture | pages [25] -->
m

<!-- b002915 | furniture | pages [25] -->
m

<!-- b002916 | furniture | pages [25] -->
m

<!-- b002917 | furniture | pages [25] -->
m

<!-- b002918 | furniture | pages [25] -->
m

<!-- b002919 | furniture | pages [25] -->
m

<!-- b002920 | furniture | pages [25] -->
m

<!-- b002921 | furniture | pages [25] -->
m

<!-- b002922 | furniture | pages [25] -->
m

<!-- b002923 | furniture | pages [25] -->
m

<!-- b002924 | furniture | pages [25] -->
m

<!-- b002925 | furniture | pages [25] -->
m

<!-- b002926 | furniture | pages [25] -->
m

<!-- b002927 | furniture | pages [25] -->
m

<!-- b002928 | furniture | pages [25] -->
m

<!-- b002929 | furniture | pages [25] -->
m

<!-- b002930 | furniture | pages [25] -->
m

<!-- b002931 | furniture | pages [25] -->
m

<!-- b002932 | furniture | pages [25] -->
m

<!-- b002933 | furniture | pages [25] -->
m

<!-- b002934 | furniture | pages [25] -->
m

<!-- b002935 | furniture | pages [25] -->
m

<!-- b002936 | furniture | pages [25] -->
m

<!-- b002937 | furniture | pages [25] -->
m

<!-- b002938 | furniture | pages [25] -->
m

<!-- b002939 | furniture | pages [25] -->
m

<!-- b002940 | furniture | pages [25] -->
m

<!-- b002941 | furniture | pages [25] -->
m

<!-- b002942 | furniture | pages [25] -->
m

<!-- b002943 | furniture | pages [25] -->
m

<!-- b002944 | furniture | pages [25] -->
m

<!-- b002945 | furniture | pages [25] -->
m

<!-- b002946 | furniture | pages [25] -->
m

<!-- b002947 | furniture | pages [25] -->
m

<!-- b002948 | furniture | pages [25] -->
m

<!-- b002949 | furniture | pages [25] -->
m

<!-- b002950 | furniture | pages [25] -->
m

<!-- b002951 | furniture | pages [25] -->
m

<!-- b002952 | furniture | pages [25] -->
m

<!-- b002953 | furniture | pages [25] -->
m

<!-- b002954 | furniture | pages [25] -->
m

<!-- b002955 | furniture | pages [25] -->
m

<!-- b002956 | furniture | pages [25] -->
m

<!-- b002957 | furniture | pages [25] -->
m

<!-- b002958 | furniture | pages [25] -->
m

<!-- b002959 | furniture | pages [25] -->
m

<!-- b002960 | furniture | pages [25] -->
m

<!-- b002961 | furniture | pages [25] -->
m

<!-- b002962 | furniture | pages [25] -->
m

<!-- b002963 | furniture | pages [25] -->
m

<!-- b002964 | furniture | pages [25] -->
m

<!-- b002965 | furniture | pages [25] -->
m

<!-- b002966 | furniture | pages [25] -->
m

<!-- b002967 | furniture | pages [25] -->
m

<!-- b002968 | furniture | pages [25] -->
m

<!-- b002969 | furniture | pages [25] -->
m

<!-- b002970 | furniture | pages [25] -->
m

<!-- b002971 | furniture | pages [25] -->
m

<!-- b002972 | furniture | pages [25] -->
m

<!-- b002973 | furniture | pages [25] -->
m

<!-- b002974 | furniture | pages [25] -->
m

<!-- b002975 | furniture | pages [25] -->
m

<!-- b002976 | furniture | pages [25] -->
m

<!-- b002977 | furniture | pages [25] -->
m

<!-- b002978 | furniture | pages [25] -->
m

<!-- b002979 | furniture | pages [25] -->
m

<!-- b002980 | furniture | pages [25] -->
m

<!-- b002981 | furniture | pages [25] -->
m

<!-- b002982 | furniture | pages [25] -->
m

<!-- b002983 | furniture | pages [25] -->
m

<!-- b002984 | furniture | pages [25] -->
m

<!-- b002985 | furniture | pages [25] -->
m

<!-- b002986 | furniture | pages [25] -->
m

<!-- b002987 | furniture | pages [25] -->
m

<!-- b002988 | furniture | pages [25] -->
m

<!-- b002989 | furniture | pages [25] -->
m

<!-- b002990 | furniture | pages [25] -->
m

<!-- b002991 | furniture | pages [25] -->
m

<!-- b002992 | furniture | pages [25] -->
m

<!-- b002993 | furniture | pages [25] -->
m

<!-- b002994 | furniture | pages [25] -->
m

<!-- b002995 | furniture | pages [25] -->
m

<!-- b002996 | furniture | pages [25] -->
m

<!-- b002997 | furniture | pages [25] -->
m

<!-- b002998 | furniture | pages [25] -->
m

<!-- b002999 | furniture | pages [25] -->
m

<!-- b003000 | furniture | pages [25] -->
m

<!-- b003001 | furniture | pages [25] -->
m

<!-- b003002 | furniture | pages [25] -->
m

<!-- b003003 | furniture | pages [25] -->
m

<!-- b003004 | furniture | pages [25] -->
m

<!-- b003005 | heading | pages [26] -->
Report on Use of AI

<!-- b003006 | ai_disclosure | pages [26] -->
AI Tools Usage Report

<!-- b003007 | ai_disclosure | pages [26] -->
• OpenAI ChatGPT (Nov 5, 2023 version, ChatGPT-4o):

<!-- b003008 | ai_disclosure | pages [26] -->
– Query1: <Please explain the basic principles of Fisher's

<!-- b003009 | ai_disclosure | pages [26] -->
Exact Test in detail.>

<!-- b003010 | ai_disclosure | pages [26] -->
– Output: <Fisher's Exact Test is a statistical test used to

<!-- b003011 | ai_disclosure | pages [26] -->
determine if there are nonrandom associations between two

<!-- b003012 | ai_disclosure | pages [26] -->
categorical variables. It is especially useful when sample

<!-- b003013 | ai_disclosure | pages [26] -->
sizes are small, and the chi-squared test may not be valid

<!-- b003014 | ai_disclosure | pages [26] -->
due to low expected frequencies in contingency tables. The

<!-- b003015 | ai_disclosure | pages [26] -->
basic principle of Fisher's Exact Test revolves around the

<!-- b003016 | ai_disclosure | pages [26] -->
hypergeometric distribution. It is based on the idea of calculating

<!-- b003017 | ai_disclosure | pages [26] -->
the probability of obtaining the observed data (or something

<!-- b003018 | ai_disclosure | pages [26] -->
more extreme) under the assumption that the two variables

<!-- b003019 | ai_disclosure | pages [26] -->
are independent.>

<!-- b003020 | ai_disclosure | pages [26] -->
– Query2:<Please provide LaTeX code to generate a three-line

<!-- b003021 | ai_disclosure | pages [26] -->
table.>

<!-- b003022 | ai_disclosure | pages [26] -->
– Output:

<!-- b003023 | ai_disclosure | pages [26] -->
\begin{table}[ht]

<!-- b003024 | ai_disclosure | pages [26] -->
\centering

<!-- b003025 | ai_disclosure | pages [26] -->
\begin{tabular}{|c|c|c|}

<!-- b003026 | ai_disclosure | pages [26] -->
\toprule

<!-- b003027 | ai_disclosure | pages [26] -->
Header 1 & Header 2 & Header 3 \\

<!-- b003028 | ai_disclosure | pages [26] -->
\midrule

<!-- b003029 | ai_disclosure | pages [26] -->
Data 1

<!-- b003030 | ai_disclosure | pages [26] -->
& Data 2

<!-- b003031 | ai_disclosure | pages [26] -->
& Data 3

<!-- b003032 | ai_disclosure | pages [26] -->
\\

<!-- b003033 | ai_disclosure | pages [26] -->
Data 4

<!-- b003034 | ai_disclosure | pages [26] -->
& Data 5

<!-- b003035 | ai_disclosure | pages [26] -->
& Data 6

<!-- b003036 | ai_disclosure | pages [26] -->
\\

<!-- b003037 | ai_disclosure | pages [26] -->
Data 7

<!-- b003038 | ai_disclosure | pages [26] -->
& Data 8

<!-- b003039 | ai_disclosure | pages [26] -->
& Data 9

<!-- b003040 | ai_disclosure | pages [26] -->
\\

<!-- b003041 | ai_disclosure | pages [26] -->
\bottomrule

<!-- b003042 | ai_disclosure | pages [26] -->
\end{tabular}

<!-- b003043 | ai_disclosure | pages [26] -->
\caption{Example of a Three-Line Table}

<!-- b003044 | ai_disclosure | pages [26] -->
\end{table}

<!-- b003045 | ai_disclosure | pages [26] -->
– Query3:<How can I determine whether the ACF and PACF plots

<!-- b003046 | ai_disclosure | pages [26] -->
are tail-cut or tail-drag when using an ARIMA model? What

<!-- b003047 | ai_disclosure | pages [26] -->
kind of plots indicate that the ARIMA model can be used?>

<!-- b003048 | ai_disclosure | pages [26] -->
1

<!-- b003049 | ai_disclosure | pages [26] -->
关注数学模型

<!-- b003050 | furniture | pages [26] -->
2

<!-- b003051 | furniture | pages [26] -->
MATHmodels

<!-- b003052 | furniture | pages [26] -->
获取更多资讯

<!-- b003053 | ai_disclosure | pages [27] -->
微信公众号：数学模型

<!-- b003054 | ai_disclosure | pages [27] -->
– Output: When using an ARIMA (AutoRegressive Integrated Mov-

<!-- b003055 | ai_disclosure | pages [27] -->
ing Average) model, the ACF (Autocorrelation Function) and PACF

<!-- b003056 | ai_disclosure | pages [27] -->
(Partial Autocorrelation Function) plots provide useful insights into

<!-- b003057 | ai_disclosure | pages [27] -->
the characteristics of the time series and help determine the appro-

<!-- b003058 | ai_disclosure | pages [27] -->
priate model parameters.

<!-- b003059 | ai_disclosure | pages [27] -->
ACF and PACF Interpretation: Tail-Cutting (or ”Cut-off”):

<!-- b003060 | ai_disclosure | pages [27] -->
ACF: If the ACF plot cuts off after a certain number of lags (i.e., sig-

<!-- b003061 | ai_disclosure | pages [27] -->
nificant autocorrelations at the initial lags, followed by values close to

<!-- b003062 | ai_disclosure | pages [27] -->
zero), it suggests a MA (Moving Average) model component. PACF:

<!-- b003063 | ai_disclosure | pages [27] -->
微信号：MATHmodels

<!-- b003064 | ai_disclosure | pages [27] -->
If the PACF plot cuts off after a certain number of lags (i.e., signif-

<!-- b003065 | ai_disclosure | pages [27] -->
icant partial autocorrelations at the initial lags, followed by values

<!-- b003066 | ai_disclosure | pages [27] -->
close to zero), it suggests an AR (AutoRegressive) model component.

<!-- b003067 | ai_disclosure | pages [27] -->
Tail-Dragging (or ”Long Tail”):

<!-- b003068 | ai_disclosure | pages [27] -->
ACF: If the ACF plot shows a gradual decay (a slow decline in the

<!-- b003069 | ai_disclosure | pages [27] -->
autocorrelation values), it suggests the presence of an AR (AutoRe-

<!-- b003070 | ai_disclosure | pages [27] -->
gressive) model component. PACF: If the PACF plot shows a gradual

<!-- b003071 | ai_disclosure | pages [27] -->
decay (a slow decline in partial autocorrelation values), it suggests

<!-- b003072 | ai_disclosure | pages [27] -->
the presence of an MA (Moving Average) model component. ARIMA

<!-- b003073 | ai_disclosure | pages [27] -->
Model Applicability: ARIMA Model Usage: ARIMA is applicable

<!-- b003074 | ai_disclosure | pages [27] -->
when the time series is stationary or can be made stationary through

<!-- b003075 | ai_disclosure | pages [27] -->
differencing (the ”I” component in ARIMA). The key is to identify

<!-- b003076 | ai_disclosure | pages [27] -->
if the series exhibits characteristics that can be captured by AR and

<!-- b003077 | ai_disclosure | pages [27] -->
MA components. If the ACF cuts off and the PACF shows a gradual

<!-- b003078 | ai_disclosure | pages [27] -->
decay, an AR model might be appropriate. If the PACF cuts off and

<!-- b003079 | ai_disclosure | pages [27] -->
the ACF shows a gradual decay, an MA model might be appropriate.

<!-- b003080 | ai_disclosure | pages [27] -->
A combination of both features (cut-off and gradual decay in ACF

<!-- b003081 | ai_disclosure | pages [27] -->
and PACF) indicates that an ARMA or ARIMA model could be a

<!-- b003082 | ai_disclosure | pages [27] -->
good fit. Summary: AR model: PACF cuts off and ACF tails off. MA

<!-- b003083 | ai_disclosure | pages [27] -->
model: ACF cuts off and PACF tails off. ARMA model: Both ACF

<!-- b003084 | ai_disclosure | pages [27] -->
and PACF tail off gradually.

<!-- b003085 | ai_disclosure | pages [27] -->
ARIMA model: For non-stationary

<!-- b003086 | ai_disclosure | pages [27] -->
data, you first difference the series and then apply ARIMA, checking

<!-- b003087 | ai_disclosure | pages [27] -->
if the differenced series becomes stationary. ACF and PACF Plots

<!-- b003088 | ai_disclosure | pages [27] -->
for ARIMA: When deciding if ARIMA can be used, check the plots

<!-- b003089 | ai_disclosure | pages [27] -->
to see if they exhibit one of the characteristics mentioned above. If

<!-- b003090 | ai_disclosure | pages [27] -->
neither ACF nor PACF cuts off abruptly or tails off gradually, you

<!-- b003091 | ai_disclosure | pages [27] -->
may need to transform or difference the data to make it suitable

<!-- b003092 | ai_disclosure | pages [27] -->
for ARIMA modeling.When using an ARIMA (AutoRegressive Inte-

<!-- b003093 | ai_disclosure | pages [27] -->
grated Moving Average) model, the ACF (Autocorrelation Function)

<!-- b003094 | ai_disclosure | pages [27] -->
and PACF (Partial Autocorrelation Function) plots provide useful

<!-- b003095 | ai_disclosure | pages [27] -->
insights into the characteristics of the time series and help determine

<!-- b003096 | ai_disclosure | pages [27] -->
the appropriate model parameters.

<!-- b003097 | ai_disclosure | pages [27] -->
ACF and PACF Interpretation: Tail-Cutting (or ”Cut-off”):

<!-- b003098 | ai_disclosure | pages [27] -->
ACF: If the ACF plot cuts off after a certain number of lags (i.e., sig-

<!-- b003099 | ai_disclosure | pages [27] -->
nificant autocorrelations at the initial lags, followed by values close to

<!-- b003100 | ai_disclosure | pages [27] -->
zero), it suggests a MA (Moving Average) model component. PACF:

<!-- b003101 | ai_disclosure | pages [27] -->
2

<!-- b003102 | ai_disclosure | pages [28] -->
If the PACF plot cuts off after a certain number of lags (i.e., signif-

<!-- b003103 | ai_disclosure | pages [28] -->
icant partial autocorrelations at the initial lags, followed by values

<!-- b003104 | ai_disclosure | pages [28] -->
close to zero), it suggests an AR (AutoRegressive) model component.

<!-- b003105 | ai_disclosure | pages [28] -->
Tail-Dragging (or ”Long Tail”):

<!-- b003106 | ai_disclosure | pages [28] -->
ACF: If the ACF plot shows a gradual decay (a slow decline in the

<!-- b003107 | ai_disclosure | pages [28] -->
autocorrelation values), it suggests the presence of an AR (AutoRe-

<!-- b003108 | ai_disclosure | pages [28] -->
gressive) model component. PACF: If the PACF plot shows a gradual

<!-- b003109 | ai_disclosure | pages [28] -->
decay (a slow decline in partial autocorrelation values), it suggests

<!-- b003110 | ai_disclosure | pages [28] -->
the presence of an MA (Moving Average) model component. ARIMA

<!-- b003111 | ai_disclosure | pages [28] -->
Model Applicability: ARIMA Model Usage: ARIMA is applicable

<!-- b003112 | ai_disclosure | pages [28] -->
when the time series is stationary or can be made stationary through

<!-- b003113 | ai_disclosure | pages [28] -->
differencing (the ”I” component in ARIMA). The key is to identify

<!-- b003114 | ai_disclosure | pages [28] -->
if the series exhibits characteristics that can be captured by AR and

<!-- b003115 | ai_disclosure | pages [28] -->
MA components. If the ACF cuts off and the PACF shows a gradual

<!-- b003116 | ai_disclosure | pages [28] -->
decay, an AR model might be appropriate. If the PACF cuts off and

<!-- b003117 | ai_disclosure | pages [28] -->
the ACF shows a gradual decay, an MA model might be appropriate.

<!-- b003118 | ai_disclosure | pages [28] -->
A combination of both features (cut-off and gradual decay in ACF

<!-- b003119 | ai_disclosure | pages [28] -->
and PACF) indicates that an ARMA or ARIMA model could be a

<!-- b003120 | ai_disclosure | pages [28] -->
good fit. Summary: AR model: PACF cuts off and ACF tails off. MA

<!-- b003121 | ai_disclosure | pages [28] -->
model: ACF cuts off and PACF tails off. ARMA model: Both ACF

<!-- b003122 | ai_disclosure | pages [28] -->
and PACF tail off gradually.

<!-- b003123 | ai_disclosure | pages [28] -->
ARIMA model: For non-stationary

<!-- b003124 | ai_disclosure | pages [28] -->
data, you first difference the series and then apply ARIMA, checking

<!-- b003125 | ai_disclosure | pages [28] -->
if the differenced series becomes stationary. ACF and PACF Plots

<!-- b003126 | ai_disclosure | pages [28] -->
for ARIMA: When deciding if ARIMA can be used, check the plots

<!-- b003127 | ai_disclosure | pages [28] -->
to see if they exhibit one of the characteristics mentioned above. If

<!-- b003128 | ai_disclosure | pages [28] -->
m

<!-- b003129 | ai_disclosure | pages [28] -->
m

<!-- b003130 | ai_disclosure | pages [28] -->
m

<!-- b003131 | ai_disclosure | pages [28] -->
m

<!-- b003132 | ai_disclosure | pages [28] -->
m

<!-- b003133 | ai_disclosure | pages [28] -->
m

<!-- b003134 | ai_disclosure | pages [28] -->
m

<!-- b003135 | ai_disclosure | pages [28] -->
m

<!-- b003136 | ai_disclosure | pages [28] -->
m

<!-- b003137 | ai_disclosure | pages [28] -->
m

<!-- b003138 | ai_disclosure | pages [28] -->
m

<!-- b003139 | ai_disclosure | pages [28] -->
m

<!-- b003140 | ai_disclosure | pages [28] -->
m

<!-- b003141 | ai_disclosure | pages [28] -->
m

<!-- b003142 | ai_disclosure | pages [28] -->
m

<!-- b003143 | ai_disclosure | pages [28] -->
m

<!-- b003144 | ai_disclosure | pages [28] -->
m

<!-- b003145 | ai_disclosure | pages [28] -->
m

<!-- b003146 | ai_disclosure | pages [28] -->
m

<!-- b003147 | ai_disclosure | pages [28] -->
m

<!-- b003148 | ai_disclosure | pages [28] -->
m

<!-- b003149 | ai_disclosure | pages [28] -->
m

<!-- b003150 | ai_disclosure | pages [28] -->
m

<!-- b003151 | ai_disclosure | pages [28] -->
m

<!-- b003152 | ai_disclosure | pages [28] -->
m

<!-- b003153 | ai_disclosure | pages [28] -->
m

<!-- b003154 | ai_disclosure | pages [28] -->
m

<!-- b003155 | ai_disclosure | pages [28] -->
m

<!-- b003156 | ai_disclosure | pages [28] -->
m

<!-- b003157 | ai_disclosure | pages [28] -->
m

<!-- b003158 | ai_disclosure | pages [28] -->
m

<!-- b003159 | ai_disclosure | pages [28] -->
m

<!-- b003160 | ai_disclosure | pages [28] -->
m

<!-- b003161 | ai_disclosure | pages [28] -->
m

<!-- b003162 | ai_disclosure | pages [28] -->
m

<!-- b003163 | ai_disclosure | pages [28] -->
m

<!-- b003164 | ai_disclosure | pages [28] -->
m

<!-- b003165 | ai_disclosure | pages [28] -->
m

<!-- b003166 | ai_disclosure | pages [28] -->
m

<!-- b003167 | ai_disclosure | pages [28] -->
m

<!-- b003168 | ai_disclosure | pages [28] -->
m

<!-- b003169 | ai_disclosure | pages [28] -->
m

<!-- b003170 | ai_disclosure | pages [28] -->
m

<!-- b003171 | ai_disclosure | pages [28] -->
m

<!-- b003172 | ai_disclosure | pages [28] -->
m

<!-- b003173 | ai_disclosure | pages [28] -->
m

<!-- b003174 | ai_disclosure | pages [28] -->
m

<!-- b003175 | ai_disclosure | pages [28] -->
m

<!-- b003176 | ai_disclosure | pages [28] -->
m

<!-- b003177 | ai_disclosure | pages [28] -->
m

<!-- b003178 | ai_disclosure | pages [28] -->
m

<!-- b003179 | ai_disclosure | pages [28] -->
m

<!-- b003180 | ai_disclosure | pages [28] -->
m

<!-- b003181 | ai_disclosure | pages [28] -->
m

<!-- b003182 | ai_disclosure | pages [28] -->
m

<!-- b003183 | ai_disclosure | pages [28] -->
m

<!-- b003184 | ai_disclosure | pages [28] -->
m

<!-- b003185 | ai_disclosure | pages [28] -->
m

<!-- b003186 | ai_disclosure | pages [28] -->
m

<!-- b003187 | ai_disclosure | pages [28] -->
m

<!-- b003188 | ai_disclosure | pages [28] -->
m

<!-- b003189 | ai_disclosure | pages [28] -->
m

<!-- b003190 | ai_disclosure | pages [28] -->
m

<!-- b003191 | ai_disclosure | pages [28] -->
m

<!-- b003192 | ai_disclosure | pages [28] -->
m

<!-- b003193 | ai_disclosure | pages [28] -->
m

<!-- b003194 | ai_disclosure | pages [28] -->
m

<!-- b003195 | ai_disclosure | pages [28] -->
m

<!-- b003196 | ai_disclosure | pages [28] -->
m

<!-- b003197 | ai_disclosure | pages [28] -->
m

<!-- b003198 | ai_disclosure | pages [28] -->
m

<!-- b003199 | ai_disclosure | pages [28] -->
m

<!-- b003200 | ai_disclosure | pages [28] -->
m

<!-- b003201 | ai_disclosure | pages [28] -->
m

<!-- b003202 | ai_disclosure | pages [28] -->
m

<!-- b003203 | ai_disclosure | pages [28] -->
m

<!-- b003204 | ai_disclosure | pages [28] -->
m

<!-- b003205 | ai_disclosure | pages [28] -->
m

<!-- b003206 | ai_disclosure | pages [28] -->
m

<!-- b003207 | ai_disclosure | pages [28] -->
m

<!-- b003208 | ai_disclosure | pages [28] -->
m

<!-- b003209 | ai_disclosure | pages [28] -->
m

<!-- b003210 | ai_disclosure | pages [28] -->
m

<!-- b003211 | ai_disclosure | pages [28] -->
m

<!-- b003212 | ai_disclosure | pages [28] -->
m

<!-- b003213 | ai_disclosure | pages [28] -->
m

<!-- b003214 | ai_disclosure | pages [28] -->
m

<!-- b003215 | ai_disclosure | pages [28] -->
m

<!-- b003216 | ai_disclosure | pages [28] -->
m

<!-- b003217 | ai_disclosure | pages [28] -->
m

<!-- b003218 | ai_disclosure | pages [28] -->
m

<!-- b003219 | ai_disclosure | pages [28] -->
m

<!-- b003220 | ai_disclosure | pages [28] -->
m

<!-- b003221 | ai_disclosure | pages [28] -->
m

<!-- b003222 | ai_disclosure | pages [28] -->
m

<!-- b003223 | ai_disclosure | pages [28] -->
m

<!-- b003224 | ai_disclosure | pages [28] -->
m

<!-- b003225 | ai_disclosure | pages [28] -->
m

<!-- b003226 | ai_disclosure | pages [28] -->
m

<!-- b003227 | ai_disclosure | pages [28] -->
m

<!-- b003228 | ai_disclosure | pages [28] -->
m

<!-- b003229 | ai_disclosure | pages [28] -->
m

<!-- b003230 | ai_disclosure | pages [28] -->
m

<!-- b003231 | ai_disclosure | pages [28] -->
m

<!-- b003232 | ai_disclosure | pages [28] -->
m

<!-- b003233 | ai_disclosure | pages [28] -->
m

<!-- b003234 | ai_disclosure | pages [28] -->
m

<!-- b003235 | ai_disclosure | pages [28] -->
m

<!-- b003236 | ai_disclosure | pages [28] -->
m

<!-- b003237 | ai_disclosure | pages [28] -->
m

<!-- b003238 | ai_disclosure | pages [28] -->
m

<!-- b003239 | ai_disclosure | pages [28] -->
m

<!-- b003240 | ai_disclosure | pages [28] -->
m

<!-- b003241 | ai_disclosure | pages [28] -->
m

<!-- b003242 | ai_disclosure | pages [28] -->
m

<!-- b003243 | ai_disclosure | pages [28] -->
m

<!-- b003244 | ai_disclosure | pages [28] -->
m

<!-- b003245 | ai_disclosure | pages [28] -->
m

<!-- b003246 | ai_disclosure | pages [28] -->
m

<!-- b003247 | ai_disclosure | pages [28] -->
m

<!-- b003248 | ai_disclosure | pages [28] -->
m

<!-- b003249 | ai_disclosure | pages [28] -->
m

<!-- b003250 | ai_disclosure | pages [28] -->
m

<!-- b003251 | ai_disclosure | pages [28] -->
m

<!-- b003252 | ai_disclosure | pages [28] -->
m

<!-- b003253 | ai_disclosure | pages [28] -->
m

<!-- b003254 | ai_disclosure | pages [28] -->
m

<!-- b003255 | ai_disclosure | pages [28] -->
m

<!-- b003256 | ai_disclosure | pages [28] -->
m

<!-- b003257 | ai_disclosure | pages [28] -->
m

<!-- b003258 | ai_disclosure | pages [28] -->
neither ACF nor PACF cuts off abruptly or tails off gradually, you

<!-- b003259 | ai_disclosure | pages [28] -->
m

<!-- b003260 | ai_disclosure | pages [28] -->
m

<!-- b003261 | ai_disclosure | pages [28] -->
m

<!-- b003262 | ai_disclosure | pages [28] -->
m

<!-- b003263 | ai_disclosure | pages [28] -->
m

<!-- b003264 | ai_disclosure | pages [28] -->
m

<!-- b003265 | ai_disclosure | pages [28] -->
m

<!-- b003266 | ai_disclosure | pages [28] -->
m

<!-- b003267 | ai_disclosure | pages [28] -->
m

<!-- b003268 | ai_disclosure | pages [28] -->
m

<!-- b003269 | ai_disclosure | pages [28] -->
m

<!-- b003270 | ai_disclosure | pages [28] -->
m

<!-- b003271 | ai_disclosure | pages [28] -->
m

<!-- b003272 | ai_disclosure | pages [28] -->
m

<!-- b003273 | ai_disclosure | pages [28] -->
m

<!-- b003274 | ai_disclosure | pages [28] -->
m

<!-- b003275 | ai_disclosure | pages [28] -->
m

<!-- b003276 | ai_disclosure | pages [28] -->
m

<!-- b003277 | ai_disclosure | pages [28] -->
m

<!-- b003278 | ai_disclosure | pages [28] -->
m

<!-- b003279 | ai_disclosure | pages [28] -->
m

<!-- b003280 | ai_disclosure | pages [28] -->
m

<!-- b003281 | ai_disclosure | pages [28] -->
m

<!-- b003282 | ai_disclosure | pages [28] -->
m

<!-- b003283 | ai_disclosure | pages [28] -->
m

<!-- b003284 | ai_disclosure | pages [28] -->
m

<!-- b003285 | ai_disclosure | pages [28] -->
m

<!-- b003286 | ai_disclosure | pages [28] -->
m

<!-- b003287 | ai_disclosure | pages [28] -->
m

<!-- b003288 | ai_disclosure | pages [28] -->
m

<!-- b003289 | ai_disclosure | pages [28] -->
m

<!-- b003290 | ai_disclosure | pages [28] -->
m

<!-- b003291 | ai_disclosure | pages [28] -->
m

<!-- b003292 | ai_disclosure | pages [28] -->
m

<!-- b003293 | ai_disclosure | pages [28] -->
m

<!-- b003294 | ai_disclosure | pages [28] -->
m

<!-- b003295 | ai_disclosure | pages [28] -->
m

<!-- b003296 | ai_disclosure | pages [28] -->
m

<!-- b003297 | ai_disclosure | pages [28] -->
m

<!-- b003298 | ai_disclosure | pages [28] -->
m

<!-- b003299 | ai_disclosure | pages [28] -->
m

<!-- b003300 | ai_disclosure | pages [28] -->
m

<!-- b003301 | ai_disclosure | pages [28] -->
m

<!-- b003302 | ai_disclosure | pages [28] -->
m

<!-- b003303 | ai_disclosure | pages [28] -->
m

<!-- b003304 | ai_disclosure | pages [28] -->
m

<!-- b003305 | ai_disclosure | pages [28] -->
m

<!-- b003306 | ai_disclosure | pages [28] -->
m

<!-- b003307 | ai_disclosure | pages [28] -->
m

<!-- b003308 | ai_disclosure | pages [28] -->
m

<!-- b003309 | ai_disclosure | pages [28] -->
m

<!-- b003310 | ai_disclosure | pages [28] -->
m

<!-- b003311 | ai_disclosure | pages [28] -->
m

<!-- b003312 | ai_disclosure | pages [28] -->
m

<!-- b003313 | ai_disclosure | pages [28] -->
m

<!-- b003314 | ai_disclosure | pages [28] -->
m

<!-- b003315 | ai_disclosure | pages [28] -->
m

<!-- b003316 | ai_disclosure | pages [28] -->
m

<!-- b003317 | ai_disclosure | pages [28] -->
m

<!-- b003318 | ai_disclosure | pages [28] -->
m

<!-- b003319 | ai_disclosure | pages [28] -->
m

<!-- b003320 | ai_disclosure | pages [28] -->
m

<!-- b003321 | ai_disclosure | pages [28] -->
m

<!-- b003322 | ai_disclosure | pages [28] -->
m

<!-- b003323 | ai_disclosure | pages [28] -->
m

<!-- b003324 | ai_disclosure | pages [28] -->
m

<!-- b003325 | ai_disclosure | pages [28] -->
m

<!-- b003326 | ai_disclosure | pages [28] -->
m

<!-- b003327 | ai_disclosure | pages [28] -->
m

<!-- b003328 | ai_disclosure | pages [28] -->
m

<!-- b003329 | ai_disclosure | pages [28] -->
m

<!-- b003330 | ai_disclosure | pages [28] -->
m

<!-- b003331 | ai_disclosure | pages [28] -->
m

<!-- b003332 | ai_disclosure | pages [28] -->
m

<!-- b003333 | ai_disclosure | pages [28] -->
m

<!-- b003334 | ai_disclosure | pages [28] -->
m

<!-- b003335 | ai_disclosure | pages [28] -->
m

<!-- b003336 | ai_disclosure | pages [28] -->
m

<!-- b003337 | ai_disclosure | pages [28] -->
m

<!-- b003338 | ai_disclosure | pages [28] -->
m

<!-- b003339 | ai_disclosure | pages [28] -->
m

<!-- b003340 | ai_disclosure | pages [28] -->
m

<!-- b003341 | ai_disclosure | pages [28] -->
m

<!-- b003342 | ai_disclosure | pages [28] -->
m

<!-- b003343 | ai_disclosure | pages [28] -->
m

<!-- b003344 | ai_disclosure | pages [28] -->
m

<!-- b003345 | ai_disclosure | pages [28] -->
m

<!-- b003346 | ai_disclosure | pages [28] -->
m

<!-- b003347 | ai_disclosure | pages [28] -->
m

<!-- b003348 | ai_disclosure | pages [28] -->
m

<!-- b003349 | ai_disclosure | pages [28] -->
m

<!-- b003350 | ai_disclosure | pages [28] -->
m

<!-- b003351 | ai_disclosure | pages [28] -->
m

<!-- b003352 | ai_disclosure | pages [28] -->
m

<!-- b003353 | ai_disclosure | pages [28] -->
m

<!-- b003354 | ai_disclosure | pages [28] -->
m

<!-- b003355 | ai_disclosure | pages [28] -->
m

<!-- b003356 | ai_disclosure | pages [28] -->
m

<!-- b003357 | ai_disclosure | pages [28] -->
m

<!-- b003358 | ai_disclosure | pages [28] -->
m

<!-- b003359 | ai_disclosure | pages [28] -->
m

<!-- b003360 | ai_disclosure | pages [28] -->
m

<!-- b003361 | ai_disclosure | pages [28] -->
m

<!-- b003362 | ai_disclosure | pages [28] -->
m

<!-- b003363 | ai_disclosure | pages [28] -->
m

<!-- b003364 | ai_disclosure | pages [28] -->
m

<!-- b003365 | ai_disclosure | pages [28] -->
m

<!-- b003366 | ai_disclosure | pages [28] -->
m

<!-- b003367 | ai_disclosure | pages [28] -->
m

<!-- b003368 | ai_disclosure | pages [28] -->
m

<!-- b003369 | ai_disclosure | pages [28] -->
m

<!-- b003370 | ai_disclosure | pages [28] -->
m

<!-- b003371 | ai_disclosure | pages [28] -->
m

<!-- b003372 | ai_disclosure | pages [28] -->
m

<!-- b003373 | ai_disclosure | pages [28] -->
may need to transform or difference the data to make it suitable for

<!-- b003374 | ai_disclosure | pages [28] -->
m

<!-- b003375 | ai_disclosure | pages [28] -->
m

<!-- b003376 | ai_disclosure | pages [28] -->
m

<!-- b003377 | ai_disclosure | pages [28] -->
m

<!-- b003378 | ai_disclosure | pages [28] -->
m

<!-- b003379 | ai_disclosure | pages [28] -->
m

<!-- b003380 | ai_disclosure | pages [28] -->
m

<!-- b003381 | ai_disclosure | pages [28] -->
m

<!-- b003382 | ai_disclosure | pages [28] -->
m

<!-- b003383 | ai_disclosure | pages [28] -->
m

<!-- b003384 | ai_disclosure | pages [28] -->
m

<!-- b003385 | ai_disclosure | pages [28] -->
m

<!-- b003386 | ai_disclosure | pages [28] -->
m

<!-- b003387 | ai_disclosure | pages [28] -->
m

<!-- b003388 | ai_disclosure | pages [28] -->
m

<!-- b003389 | ai_disclosure | pages [28] -->
m

<!-- b003390 | ai_disclosure | pages [28] -->
m

<!-- b003391 | ai_disclosure | pages [28] -->
m

<!-- b003392 | ai_disclosure | pages [28] -->
m

<!-- b003393 | ai_disclosure | pages [28] -->
m

<!-- b003394 | ai_disclosure | pages [28] -->
m

<!-- b003395 | ai_disclosure | pages [28] -->
m

<!-- b003396 | ai_disclosure | pages [28] -->
m

<!-- b003397 | ai_disclosure | pages [28] -->
m

<!-- b003398 | ai_disclosure | pages [28] -->
m

<!-- b003399 | ai_disclosure | pages [28] -->
m

<!-- b003400 | ai_disclosure | pages [28] -->
m

<!-- b003401 | ai_disclosure | pages [28] -->
m

<!-- b003402 | ai_disclosure | pages [28] -->
m

<!-- b003403 | ai_disclosure | pages [28] -->
m

<!-- b003404 | ai_disclosure | pages [28] -->
m

<!-- b003405 | ai_disclosure | pages [28] -->
m

<!-- b003406 | ai_disclosure | pages [28] -->
m

<!-- b003407 | ai_disclosure | pages [28] -->
m

<!-- b003408 | ai_disclosure | pages [28] -->
m

<!-- b003409 | ai_disclosure | pages [28] -->
m

<!-- b003410 | ai_disclosure | pages [28] -->
m

<!-- b003411 | ai_disclosure | pages [28] -->
m

<!-- b003412 | ai_disclosure | pages [28] -->
m

<!-- b003413 | ai_disclosure | pages [28] -->
m

<!-- b003414 | ai_disclosure | pages [28] -->
m

<!-- b003415 | ai_disclosure | pages [28] -->
m

<!-- b003416 | ai_disclosure | pages [28] -->
m

<!-- b003417 | ai_disclosure | pages [28] -->
m

<!-- b003418 | ai_disclosure | pages [28] -->
m

<!-- b003419 | ai_disclosure | pages [28] -->
m

<!-- b003420 | ai_disclosure | pages [28] -->
m

<!-- b003421 | ai_disclosure | pages [28] -->
m

<!-- b003422 | ai_disclosure | pages [28] -->
m

<!-- b003423 | ai_disclosure | pages [28] -->
m

<!-- b003424 | ai_disclosure | pages [28] -->
m

<!-- b003425 | ai_disclosure | pages [28] -->
m

<!-- b003426 | ai_disclosure | pages [28] -->
m

<!-- b003427 | ai_disclosure | pages [28] -->
m

<!-- b003428 | ai_disclosure | pages [28] -->
m

<!-- b003429 | ai_disclosure | pages [28] -->
m

<!-- b003430 | ai_disclosure | pages [28] -->
m

<!-- b003431 | ai_disclosure | pages [28] -->
m

<!-- b003432 | ai_disclosure | pages [28] -->
m

<!-- b003433 | ai_disclosure | pages [28] -->
m

<!-- b003434 | ai_disclosure | pages [28] -->
m

<!-- b003435 | ai_disclosure | pages [28] -->
m

<!-- b003436 | ai_disclosure | pages [28] -->
m

<!-- b003437 | ai_disclosure | pages [28] -->
m

<!-- b003438 | ai_disclosure | pages [28] -->
m

<!-- b003439 | ai_disclosure | pages [28] -->
m

<!-- b003440 | ai_disclosure | pages [28] -->
m

<!-- b003441 | ai_disclosure | pages [28] -->
m

<!-- b003442 | ai_disclosure | pages [28] -->
m

<!-- b003443 | ai_disclosure | pages [28] -->
m

<!-- b003444 | ai_disclosure | pages [28] -->
m

<!-- b003445 | ai_disclosure | pages [28] -->
m

<!-- b003446 | ai_disclosure | pages [28] -->
m

<!-- b003447 | ai_disclosure | pages [28] -->
m

<!-- b003448 | ai_disclosure | pages [28] -->
m

<!-- b003449 | ai_disclosure | pages [28] -->
m

<!-- b003450 | ai_disclosure | pages [28] -->
m

<!-- b003451 | ai_disclosure | pages [28] -->
m

<!-- b003452 | ai_disclosure | pages [28] -->
m

<!-- b003453 | ai_disclosure | pages [28] -->
m

<!-- b003454 | ai_disclosure | pages [28] -->
m

<!-- b003455 | ai_disclosure | pages [28] -->
m

<!-- b003456 | ai_disclosure | pages [28] -->
m

<!-- b003457 | ai_disclosure | pages [28] -->
m

<!-- b003458 | ai_disclosure | pages [28] -->
m

<!-- b003459 | ai_disclosure | pages [28] -->
m

<!-- b003460 | ai_disclosure | pages [28] -->
m

<!-- b003461 | ai_disclosure | pages [28] -->
m

<!-- b003462 | ai_disclosure | pages [28] -->
m

<!-- b003463 | ai_disclosure | pages [28] -->
m

<!-- b003464 | ai_disclosure | pages [28] -->
m

<!-- b003465 | ai_disclosure | pages [28] -->
m

<!-- b003466 | ai_disclosure | pages [28] -->
m

<!-- b003467 | ai_disclosure | pages [28] -->
m

<!-- b003468 | ai_disclosure | pages [28] -->
m

<!-- b003469 | ai_disclosure | pages [28] -->
m

<!-- b003470 | ai_disclosure | pages [28] -->
m

<!-- b003471 | ai_disclosure | pages [28] -->
m

<!-- b003472 | ai_disclosure | pages [28] -->
m

<!-- b003473 | ai_disclosure | pages [28] -->
m

<!-- b003474 | ai_disclosure | pages [28] -->
m

<!-- b003475 | ai_disclosure | pages [28] -->
m

<!-- b003476 | ai_disclosure | pages [28] -->
m

<!-- b003477 | ai_disclosure | pages [28] -->
m

<!-- b003478 | ai_disclosure | pages [28] -->
ARIMA modeling.

<!-- b003479 | ai_disclosure | pages [28] -->
m

<!-- b003480 | ai_disclosure | pages [28] -->
m

<!-- b003481 | ai_disclosure | pages [28] -->
m

<!-- b003482 | ai_disclosure | pages [28] -->
m

<!-- b003483 | ai_disclosure | pages [28] -->
m

<!-- b003484 | ai_disclosure | pages [28] -->
m

<!-- b003485 | ai_disclosure | pages [28] -->
m

<!-- b003486 | ai_disclosure | pages [28] -->
m

<!-- b003487 | ai_disclosure | pages [28] -->
m

<!-- b003488 | ai_disclosure | pages [28] -->
m

<!-- b003489 | ai_disclosure | pages [28] -->
m

<!-- b003490 | ai_disclosure | pages [28] -->
m

<!-- b003491 | ai_disclosure | pages [28] -->
m

<!-- b003492 | ai_disclosure | pages [28] -->
m

<!-- b003493 | ai_disclosure | pages [28] -->
m

<!-- b003494 | ai_disclosure | pages [28] -->
m

<!-- b003495 | ai_disclosure | pages [28] -->
m

<!-- b003496 | ai_disclosure | pages [28] -->
m

<!-- b003497 | ai_disclosure | pages [28] -->
m

<!-- b003498 | ai_disclosure | pages [28] -->
m

<!-- b003499 | ai_disclosure | pages [28] -->
m

<!-- b003500 | ai_disclosure | pages [28] -->
m

<!-- b003501 | ai_disclosure | pages [28] -->
m

<!-- b003502 | ai_disclosure | pages [28] -->
m

<!-- b003503 | ai_disclosure | pages [28] -->
m

<!-- b003504 | ai_disclosure | pages [28] -->
m

<!-- b003505 | ai_disclosure | pages [28] -->
m

<!-- b003506 | ai_disclosure | pages [28] -->
m

<!-- b003507 | ai_disclosure | pages [28] -->
m

<!-- b003508 | ai_disclosure | pages [28] -->
m

<!-- b003509 | ai_disclosure | pages [28] -->
m

<!-- b003510 | ai_disclosure | pages [28] -->
m

<!-- b003511 | ai_disclosure | pages [28] -->
m

<!-- b003512 | ai_disclosure | pages [28] -->
m

<!-- b003513 | ai_disclosure | pages [28] -->
m

<!-- b003514 | ai_disclosure | pages [28] -->
m

<!-- b003515 | ai_disclosure | pages [28] -->
m

<!-- b003516 | ai_disclosure | pages [28] -->
m

<!-- b003517 | ai_disclosure | pages [28] -->
m

<!-- b003518 | ai_disclosure | pages [28] -->
m

<!-- b003519 | ai_disclosure | pages [28] -->
m

<!-- b003520 | ai_disclosure | pages [28] -->
m

<!-- b003521 | ai_disclosure | pages [28] -->
m

<!-- b003522 | ai_disclosure | pages [28] -->
m

<!-- b003523 | ai_disclosure | pages [28] -->
m

<!-- b003524 | ai_disclosure | pages [28] -->
m

<!-- b003525 | ai_disclosure | pages [28] -->
m

<!-- b003526 | ai_disclosure | pages [28] -->
m

<!-- b003527 | ai_disclosure | pages [28] -->
m

<!-- b003528 | ai_disclosure | pages [28] -->
m

<!-- b003529 | ai_disclosure | pages [28] -->
m

<!-- b003530 | ai_disclosure | pages [28] -->
m

<!-- b003531 | ai_disclosure | pages [28] -->
m

<!-- b003532 | ai_disclosure | pages [28] -->
m

<!-- b003533 | ai_disclosure | pages [28] -->
m

<!-- b003534 | ai_disclosure | pages [28] -->
m

<!-- b003535 | ai_disclosure | pages [28] -->
m

<!-- b003536 | ai_disclosure | pages [28] -->
m

<!-- b003537 | ai_disclosure | pages [28] -->
m

<!-- b003538 | ai_disclosure | pages [28] -->
m

<!-- b003539 | ai_disclosure | pages [28] -->
m

<!-- b003540 | ai_disclosure | pages [28] -->
m

<!-- b003541 | ai_disclosure | pages [28] -->
m

<!-- b003542 | ai_disclosure | pages [28] -->
m

<!-- b003543 | ai_disclosure | pages [28] -->
m

<!-- b003544 | ai_disclosure | pages [28] -->
m

<!-- b003545 | ai_disclosure | pages [28] -->
m

<!-- b003546 | ai_disclosure | pages [28] -->
m

<!-- b003547 | ai_disclosure | pages [28] -->
m

<!-- b003548 | ai_disclosure | pages [28] -->
m

<!-- b003549 | ai_disclosure | pages [28] -->
m

<!-- b003550 | ai_disclosure | pages [28] -->
m

<!-- b003551 | ai_disclosure | pages [28] -->
m

<!-- b003552 | ai_disclosure | pages [28] -->
m

<!-- b003553 | ai_disclosure | pages [28] -->
m

<!-- b003554 | ai_disclosure | pages [28] -->
m

<!-- b003555 | ai_disclosure | pages [28] -->
m

<!-- b003556 | ai_disclosure | pages [28] -->
m

<!-- b003557 | ai_disclosure | pages [28] -->
m

<!-- b003558 | ai_disclosure | pages [28] -->
m

<!-- b003559 | ai_disclosure | pages [28] -->
m

<!-- b003560 | ai_disclosure | pages [28] -->
m

<!-- b003561 | ai_disclosure | pages [28] -->
m

<!-- b003562 | ai_disclosure | pages [28] -->
m

<!-- b003563 | ai_disclosure | pages [28] -->
m

<!-- b003564 | ai_disclosure | pages [28] -->
m

<!-- b003565 | ai_disclosure | pages [28] -->
m

<!-- b003566 | ai_disclosure | pages [28] -->
m

<!-- b003567 | ai_disclosure | pages [28] -->
m

<!-- b003568 | ai_disclosure | pages [28] -->
m

<!-- b003569 | ai_disclosure | pages [28] -->
m

<!-- b003570 | ai_disclosure | pages [28] -->
m

<!-- b003571 | ai_disclosure | pages [28] -->
m

<!-- b003572 | ai_disclosure | pages [28] -->
m

<!-- b003573 | ai_disclosure | pages [28] -->
m

<!-- b003574 | ai_disclosure | pages [28] -->
m

<!-- b003575 | ai_disclosure | pages [28] -->
m

<!-- b003576 | ai_disclosure | pages [28] -->
m

<!-- b003577 | ai_disclosure | pages [28] -->
m

<!-- b003578 | ai_disclosure | pages [28] -->
m

<!-- b003579 | ai_disclosure | pages [28] -->
m

<!-- b003580 | ai_disclosure | pages [28] -->
m

<!-- b003581 | ai_disclosure | pages [28] -->
m

<!-- b003582 | ai_disclosure | pages [28] -->
m

<!-- b003583 | ai_disclosure | pages [28] -->
m

<!-- b003584 | ai_disclosure | pages [28] -->
m

<!-- b003585 | ai_disclosure | pages [28] -->
m

<!-- b003586 | ai_disclosure | pages [28] -->
m

<!-- b003587 | ai_disclosure | pages [28] -->
m

<!-- b003588 | ai_disclosure | pages [28] -->
m

<!-- b003589 | ai_disclosure | pages [28] -->
m

<!-- b003590 | ai_disclosure | pages [28] -->
m

<!-- b003591 | ai_disclosure | pages [28] -->
m

<!-- b003592 | ai_disclosure | pages [28] -->
m

<!-- b003593 | ai_disclosure | pages [28] -->
m

<!-- b003594 | ai_disclosure | pages [28] -->
m

<!-- b003595 | ai_disclosure | pages [28] -->
m

<!-- b003596 | ai_disclosure | pages [28] -->
m

<!-- b003597 | ai_disclosure | pages [28] -->
m

<!-- b003598 | ai_disclosure | pages [28] -->
m

<!-- b003599 | ai_disclosure | pages [28] -->
m

<!-- b003600 | ai_disclosure | pages [28] -->
m

<!-- b003601 | ai_disclosure | pages [28] -->
m

<!-- b003602 | ai_disclosure | pages [28] -->
m

<!-- b003603 | ai_disclosure | pages [28] -->
m

<!-- b003604 | ai_disclosure | pages [28] -->
m

<!-- b003605 | ai_disclosure | pages [28] -->
m

<!-- b003606 | ai_disclosure | pages [28] -->
m

<!-- b003607 | ai_disclosure | pages [28] -->
m

<!-- b003608 | ai_disclosure | pages [28] -->
m

<!-- b003609 | ai_disclosure | pages [28] -->
m

<!-- b003610 | ai_disclosure | pages [28] -->
m

<!-- b003611 | ai_disclosure | pages [28] -->
m

<!-- b003612 | ai_disclosure | pages [28] -->
m

<!-- b003613 | ai_disclosure | pages [28] -->
m

<!-- b003614 | ai_disclosure | pages [28] -->
m

<!-- b003615 | ai_disclosure | pages [28] -->
m

<!-- b003616 | ai_disclosure | pages [28] -->
m

<!-- b003617 | ai_disclosure | pages [28] -->
m

<!-- b003618 | ai_disclosure | pages [28] -->
m

<!-- b003619 | ai_disclosure | pages [28] -->
m

<!-- b003620 | ai_disclosure | pages [28] -->
m

<!-- b003621 | ai_disclosure | pages [28] -->
m

<!-- b003622 | ai_disclosure | pages [28] -->
m

<!-- b003623 | ai_disclosure | pages [28] -->
m

<!-- b003624 | ai_disclosure | pages [28] -->
m

<!-- b003625 | ai_disclosure | pages [28] -->
m

<!-- b003626 | ai_disclosure | pages [28] -->
m

<!-- b003627 | ai_disclosure | pages [28] -->
m

<!-- b003628 | ai_disclosure | pages [28] -->
m

<!-- b003629 | ai_disclosure | pages [28] -->
m

<!-- b003630 | ai_disclosure | pages [28] -->
m

<!-- b003631 | ai_disclosure | pages [28] -->
m

<!-- b003632 | ai_disclosure | pages [28] -->
m

<!-- b003633 | ai_disclosure | pages [28] -->
m

<!-- b003634 | ai_disclosure | pages [28] -->
m

<!-- b003635 | ai_disclosure | pages [28] -->
m

<!-- b003636 | ai_disclosure | pages [28] -->
m

<!-- b003637 | ai_disclosure | pages [28] -->
m

<!-- b003638 | ai_disclosure | pages [28] -->
m

<!-- b003639 | ai_disclosure | pages [28] -->
m

<!-- b003640 | ai_disclosure | pages [28] -->
m

<!-- b003641 | ai_disclosure | pages [28] -->
m

<!-- b003642 | ai_disclosure | pages [28] -->
m

<!-- b003643 | ai_disclosure | pages [28] -->
m

<!-- b003644 | ai_disclosure | pages [28] -->
m

<!-- b003645 | ai_disclosure | pages [28] -->
m

<!-- b003646 | ai_disclosure | pages [28] -->
m

<!-- b003647 | ai_disclosure | pages [28] -->
m

<!-- b003648 | ai_disclosure | pages [28] -->
m

<!-- b003649 | ai_disclosure | pages [28] -->
m

<!-- b003650 | ai_disclosure | pages [28] -->
m

<!-- b003651 | ai_disclosure | pages [28] -->
m

<!-- b003652 | ai_disclosure | pages [28] -->
m

<!-- b003653 | ai_disclosure | pages [28] -->
m

<!-- b003654 | ai_disclosure | pages [28] -->
m

<!-- b003655 | ai_disclosure | pages [28] -->
m

<!-- b003656 | ai_disclosure | pages [28] -->
m

<!-- b003657 | ai_disclosure | pages [28] -->
m

<!-- b003658 | ai_disclosure | pages [28] -->
m

<!-- b003659 | ai_disclosure | pages [28] -->
m

<!-- b003660 | ai_disclosure | pages [28] -->
m

<!-- b003661 | ai_disclosure | pages [28] -->
m

<!-- b003662 | ai_disclosure | pages [28] -->
m

<!-- b003663 | ai_disclosure | pages [28] -->
m

<!-- b003664 | ai_disclosure | pages [28] -->
m

<!-- b003665 | ai_disclosure | pages [28] -->
m

<!-- b003666 | ai_disclosure | pages [28] -->
m

<!-- b003667 | ai_disclosure | pages [28] -->
m

<!-- b003668 | ai_disclosure | pages [28] -->
m

<!-- b003669 | ai_disclosure | pages [28] -->
m

<!-- b003670 | ai_disclosure | pages [28] -->
m

<!-- b003671 | ai_disclosure | pages [28] -->
m

<!-- b003672 | ai_disclosure | pages [28] -->
• DeepSeek DeepSeek-V3 (Jul, 2024 version):

<!-- b003673 | ai_disclosure | pages [28] -->
m

<!-- b003674 | ai_disclosure | pages [28] -->
m

<!-- b003675 | ai_disclosure | pages [28] -->
m

<!-- b003676 | ai_disclosure | pages [28] -->
m

<!-- b003677 | ai_disclosure | pages [28] -->
m

<!-- b003678 | ai_disclosure | pages [28] -->
m

<!-- b003679 | ai_disclosure | pages [28] -->
m

<!-- b003680 | ai_disclosure | pages [28] -->
m

<!-- b003681 | ai_disclosure | pages [28] -->
m

<!-- b003682 | ai_disclosure | pages [28] -->
m

<!-- b003683 | ai_disclosure | pages [28] -->
m

<!-- b003684 | ai_disclosure | pages [28] -->
m

<!-- b003685 | ai_disclosure | pages [28] -->
m

<!-- b003686 | ai_disclosure | pages [28] -->
m

<!-- b003687 | ai_disclosure | pages [28] -->
m

<!-- b003688 | ai_disclosure | pages [28] -->
m

<!-- b003689 | ai_disclosure | pages [28] -->
m

<!-- b003690 | ai_disclosure | pages [28] -->
m

<!-- b003691 | ai_disclosure | pages [28] -->
m

<!-- b003692 | ai_disclosure | pages [28] -->
m

<!-- b003693 | ai_disclosure | pages [28] -->
m

<!-- b003694 | ai_disclosure | pages [28] -->
m

<!-- b003695 | ai_disclosure | pages [28] -->
m

<!-- b003696 | ai_disclosure | pages [28] -->
m

<!-- b003697 | ai_disclosure | pages [28] -->
m

<!-- b003698 | ai_disclosure | pages [28] -->
m

<!-- b003699 | ai_disclosure | pages [28] -->
m

<!-- b003700 | ai_disclosure | pages [28] -->
m

<!-- b003701 | ai_disclosure | pages [28] -->
m

<!-- b003702 | ai_disclosure | pages [28] -->
m

<!-- b003703 | ai_disclosure | pages [28] -->
m

<!-- b003704 | ai_disclosure | pages [28] -->
m

<!-- b003705 | ai_disclosure | pages [28] -->
m

<!-- b003706 | ai_disclosure | pages [28] -->
m

<!-- b003707 | ai_disclosure | pages [28] -->
m

<!-- b003708 | ai_disclosure | pages [28] -->
m

<!-- b003709 | ai_disclosure | pages [28] -->
m

<!-- b003710 | ai_disclosure | pages [28] -->
m

<!-- b003711 | ai_disclosure | pages [28] -->
m

<!-- b003712 | ai_disclosure | pages [28] -->
m

<!-- b003713 | ai_disclosure | pages [28] -->
m

<!-- b003714 | ai_disclosure | pages [28] -->
m

<!-- b003715 | ai_disclosure | pages [28] -->
m

<!-- b003716 | ai_disclosure | pages [28] -->
m

<!-- b003717 | ai_disclosure | pages [28] -->
m

<!-- b003718 | ai_disclosure | pages [28] -->
m

<!-- b003719 | ai_disclosure | pages [28] -->
m

<!-- b003720 | ai_disclosure | pages [28] -->
m

<!-- b003721 | ai_disclosure | pages [28] -->
m

<!-- b003722 | ai_disclosure | pages [28] -->
m

<!-- b003723 | ai_disclosure | pages [28] -->
m

<!-- b003724 | ai_disclosure | pages [28] -->
m

<!-- b003725 | ai_disclosure | pages [28] -->
m

<!-- b003726 | ai_disclosure | pages [28] -->
m

<!-- b003727 | ai_disclosure | pages [28] -->
m

<!-- b003728 | ai_disclosure | pages [28] -->
m

<!-- b003729 | ai_disclosure | pages [28] -->
m

<!-- b003730 | ai_disclosure | pages [28] -->
m

<!-- b003731 | ai_disclosure | pages [28] -->
m

<!-- b003732 | ai_disclosure | pages [28] -->
m

<!-- b003733 | ai_disclosure | pages [28] -->
m

<!-- b003734 | ai_disclosure | pages [28] -->
m

<!-- b003735 | ai_disclosure | pages [28] -->
m

<!-- b003736 | ai_disclosure | pages [28] -->
m

<!-- b003737 | ai_disclosure | pages [28] -->
m

<!-- b003738 | ai_disclosure | pages [28] -->
m

<!-- b003739 | ai_disclosure | pages [28] -->
m

<!-- b003740 | ai_disclosure | pages [28] -->
m

<!-- b003741 | ai_disclosure | pages [28] -->
m

<!-- b003742 | ai_disclosure | pages [28] -->
m

<!-- b003743 | ai_disclosure | pages [28] -->
m

<!-- b003744 | ai_disclosure | pages [28] -->
m

<!-- b003745 | ai_disclosure | pages [28] -->
m

<!-- b003746 | ai_disclosure | pages [28] -->
m

<!-- b003747 | ai_disclosure | pages [28] -->
m

<!-- b003748 | ai_disclosure | pages [28] -->
m

<!-- b003749 | ai_disclosure | pages [28] -->
m

<!-- b003750 | ai_disclosure | pages [28] -->
m

<!-- b003751 | ai_disclosure | pages [28] -->
m

<!-- b003752 | ai_disclosure | pages [28] -->
m

<!-- b003753 | ai_disclosure | pages [28] -->
m

<!-- b003754 | ai_disclosure | pages [28] -->
m

<!-- b003755 | ai_disclosure | pages [28] -->
m

<!-- b003756 | ai_disclosure | pages [28] -->
m

<!-- b003757 | ai_disclosure | pages [28] -->
m

<!-- b003758 | ai_disclosure | pages [28] -->
m

<!-- b003759 | ai_disclosure | pages [28] -->
m

<!-- b003760 | ai_disclosure | pages [28] -->
m

<!-- b003761 | ai_disclosure | pages [28] -->
m

<!-- b003762 | ai_disclosure | pages [28] -->
m

<!-- b003763 | ai_disclosure | pages [28] -->
m

<!-- b003764 | ai_disclosure | pages [28] -->
m

<!-- b003765 | ai_disclosure | pages [28] -->
m

<!-- b003766 | ai_disclosure | pages [28] -->
m

<!-- b003767 | ai_disclosure | pages [28] -->
m

<!-- b003768 | ai_disclosure | pages [28] -->
m

<!-- b003769 | ai_disclosure | pages [28] -->
m

<!-- b003770 | ai_disclosure | pages [28] -->
m

<!-- b003771 | ai_disclosure | pages [28] -->
m

<!-- b003772 | ai_disclosure | pages [28] -->
m

<!-- b003773 | ai_disclosure | pages [28] -->
m

<!-- b003774 | ai_disclosure | pages [28] -->
m

<!-- b003775 | ai_disclosure | pages [28] -->
m

<!-- b003776 | ai_disclosure | pages [28] -->
m

<!-- b003777 | ai_disclosure | pages [28] -->
m

<!-- b003778 | ai_disclosure | pages [28] -->
m

<!-- b003779 | ai_disclosure | pages [28] -->
m

<!-- b003780 | ai_disclosure | pages [28] -->
m

<!-- b003781 | ai_disclosure | pages [28] -->
m

<!-- b003782 | ai_disclosure | pages [28] -->
m

<!-- b003783 | ai_disclosure | pages [28] -->
m

<!-- b003784 | ai_disclosure | pages [28] -->
m

<!-- b003785 | ai_disclosure | pages [28] -->
m

<!-- b003786 | ai_disclosure | pages [28] -->
m

<!-- b003787 | ai_disclosure | pages [28] -->
m

<!-- b003788 | ai_disclosure | pages [28] -->
m

<!-- b003789 | ai_disclosure | pages [28] -->
m

<!-- b003790 | ai_disclosure | pages [28] -->
m

<!-- b003791 | ai_disclosure | pages [28] -->
m

<!-- b003792 | ai_disclosure | pages [28] -->
m

<!-- b003793 | ai_disclosure | pages [28] -->
m

<!-- b003794 | ai_disclosure | pages [28] -->
m

<!-- b003795 | ai_disclosure | pages [28] -->
m

<!-- b003796 | ai_disclosure | pages [28] -->
m

<!-- b003797 | ai_disclosure | pages [28] -->
m

<!-- b003798 | ai_disclosure | pages [28] -->
m

<!-- b003799 | ai_disclosure | pages [28] -->
m

<!-- b003800 | ai_disclosure | pages [28] -->
m

<!-- b003801 | ai_disclosure | pages [28] -->
m

<!-- b003802 | ai_disclosure | pages [28] -->
m

<!-- b003803 | ai_disclosure | pages [28] -->
m

<!-- b003804 | ai_disclosure | pages [28] -->
m

<!-- b003805 | ai_disclosure | pages [28] -->
m

<!-- b003806 | ai_disclosure | pages [28] -->
m

<!-- b003807 | ai_disclosure | pages [28] -->
m

<!-- b003808 | ai_disclosure | pages [28] -->
m

<!-- b003809 | ai_disclosure | pages [28] -->
m

<!-- b003810 | ai_disclosure | pages [28] -->
m

<!-- b003811 | ai_disclosure | pages [28] -->
m

<!-- b003812 | ai_disclosure | pages [28] -->
m

<!-- b003813 | ai_disclosure | pages [28] -->
m

<!-- b003814 | ai_disclosure | pages [28] -->
m

<!-- b003815 | ai_disclosure | pages [28] -->
m

<!-- b003816 | ai_disclosure | pages [28] -->
m

<!-- b003817 | ai_disclosure | pages [28] -->
m

<!-- b003818 | ai_disclosure | pages [28] -->
m

<!-- b003819 | ai_disclosure | pages [28] -->
– Query1: <Can you give me some examples of great coaches and

<!-- b003820 | ai_disclosure | pages [28] -->
point out the specific data sources? Please ensure the information

<!-- b003821 | ai_disclosure | pages [28] -->
is authentic and reliable.>

<!-- b003822 | ai_disclosure | pages [28] -->
– Output: <Here are a few examples of great coaches across various

<!-- b003823 | ai_disclosure | pages [28] -->
sports along with reliable data sources to support their achievements:

<!-- b003824 | ai_disclosure | pages [28] -->
Sir Alex Ferguson (Football/Soccer)

<!-- b003825 | ai_disclosure | pages [28] -->
Achievements: Sir Alex Ferguson is widely regarded as one of the

<!-- b003826 | ai_disclosure | pages [28] -->
greatest football managers of all time.

<!-- b003827 | ai_disclosure | pages [28] -->
He managed Manchester

<!-- b003828 | ai_disclosure | pages [28] -->
United from 1986 to 2013, winning 13 Premier League titles, 5 FA

<!-- b003829 | ai_disclosure | pages [28] -->
Cups, and 2 UEFA Champions League titles, among other accolades.

<!-- b003830 | ai_disclosure | pages [28] -->
Source: You can verify this information from reliable sports databases

<!-- b003831 | ai_disclosure | pages [28] -->
such as Transfermarkt and Manchester United Oﬀicial Website. Phil

<!-- b003832 | ai_disclosure | pages [28] -->
Jackson (Basketball)

<!-- b003833 | ai_disclosure | pages [28] -->
Achievements: Phil Jackson is known as one of the greatest NBA

<!-- b003834 | ai_disclosure | pages [28] -->
coaches, having won 11 NBA championships, the most by any coach

<!-- b003835 | ai_disclosure | pages [28] -->
3

<!-- b003836 | ai_disclosure | pages [28] -->
关注数学模型

<!-- b003837 | furniture | pages [28] -->
2

<!-- b003838 | furniture | pages [28] -->
MATHmodels

<!-- b003839 | furniture | pages [28] -->
获取更多资讯

<!-- b003840 | ai_disclosure | pages [29] -->
微信公众号：数学模型

<!-- b003841 | ai_disclosure | pages [29] -->
in NBA history.

<!-- b003842 | ai_disclosure | pages [29] -->
He coached teams like the Chicago Bulls (with

<!-- b003843 | ai_disclosure | pages [29] -->
Michael Jordan) and the Los Angeles Lakers. Source: This informa-

<!-- b003844 | ai_disclosure | pages [29] -->
tion is available on the oﬀicial NBA website and reputable basketball

<!-- b003845 | ai_disclosure | pages [29] -->
databases like Basketball Reference. Bill Belichick (American Foot-

<!-- b003846 | ai_disclosure | pages [29] -->
ball)

<!-- b003847 | ai_disclosure | pages [29] -->
Achievements: Bill Belichick is the head coach of the New England

<!-- b003848 | ai_disclosure | pages [29] -->
Patriots, and he has led the team to 6 Super Bowl titles, the most

<!-- b003849 | ai_disclosure | pages [29] -->
by any coach in NFL history. Source: The details about his coaching

<!-- b003850 | ai_disclosure | pages [29] -->
career are available on NFL Oﬀicial Website and other sources like

<!-- b003851 | ai_disclosure | pages [29] -->
微信号：MATHmodels

<!-- b003852 | ai_disclosure | pages [29] -->
Pro Football Reference. Vince Lombardi (American Football)

<!-- b003853 | ai_disclosure | pages [29] -->
Achievements: Vince Lombardi, after whom the Super Bowl trophy

<!-- b003854 | ai_disclosure | pages [29] -->
is named, won 5 NFL championships as the head coach of the Green

<!-- b003855 | ai_disclosure | pages [29] -->
Bay Packers in the 1960s. Source: His achievements are documented

<!-- b003856 | ai_disclosure | pages [29] -->
in NFL.com and historical sources such as the Pro Football Hall of

<!-- b003857 | ai_disclosure | pages [29] -->
Fame. Pat Summitt (Basketball)

<!-- b003858 | ai_disclosure | pages [29] -->
Achievements: Pat Summitt is regarded as one of the greatest col-

<!-- b003859 | ai_disclosure | pages [29] -->
lege basketball coaches in history. She led the University of Tennessee

<!-- b003860 | ai_disclosure | pages [29] -->
Women’s Basketball team to 8 NCAA championships. Source: Veri-

<!-- b003861 | ai_disclosure | pages [29] -->
fied by ESPN and Tennessee Volunteers Oﬀicial Website.>

<!-- b003862 | ai_disclosure | pages [29] -->
• GitHub CoPilot (Jan 16, 2024 version):

<!-- b003863 | ai_disclosure | pages [29] -->
– Auto-completions for code used in preparing our models.

<!-- b003864 | ai_disclosure | pages [29] -->
4
