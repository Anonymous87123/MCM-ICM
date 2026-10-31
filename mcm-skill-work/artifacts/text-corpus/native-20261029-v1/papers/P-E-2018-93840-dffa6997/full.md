# P-E-2018-93840-dffa6997

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | furniture | pages [1] -->
Team # 93840

<!-- b000003 | furniture | pages [1] -->
Page 1 of 19

<!-- b000004 | prose | pages [1] -->
Motivated to measure a country's stability quantitatively and more accurately, our team builds a mathematical framework to identify the current status of a country. In the paper, we introduce a composite index processing comprehensive datasets that consist of di erent factors including economy, politics, demographics and climate change.

<!-- b000005 | prose | pages [1] -->
With the composite measure, we build a dynamic system simulating the uctuation of the market as a result of the variations in di erent sectors. This system not only describes the current fragility of a country facing potential alternation in social and environmental factors, but also it predicts the equilibrium states that the country would approach overtime.

<!-- b000006 | prose | pages [1] -->
Moreover, we propose a bifurcation plot that depicts the tipping points between three states of a country in terms of its fragility: stable state, vulnerable state, and fragile state. We then further apply our model and bifurcation plot in real-life case analyses with three selected countries, Syria, Cuba and New Zealand.

<!-- b000007 | prose | pages [1] -->
After calibrating parameters and comparing di erent factors in each country, we nd out that climate conditions play a signi cant role in Syria's fragile state due to factors such as limited water resources and food supply. We also nd that factors of droughts and occurrence of natural disasters in Cuba caused huge market losses and Cuba would reach the tipping point under appropriate human intervention.

<!-- b000008 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000009 | furniture | pages [2] -->
Team # 93840

<!-- b000010 | furniture | pages [2] -->
Page 2 of 19

<!-- b000011 | prose | pages [2] -->
1

<!-- b000012 | heading | pages [2] -->
Introduction

<!-- b000013 | prose | pages [2] -->
Climate change includes increased droughts, shrinking glaciers, temperature rise and sea level rise. Despite a scienti c consensus on global warming, climate change denial and doubts still exist and the impacts of climate change and the extent to which it is caused by humans are suspected. In our paper, we build a mathematical framework to determine a country's fragility with a composite measure considering multiple factors including economic, political and demographic indicators and climate change. In section 6, we select three countries, Syria, Cuba and New Zealand to do case studies and further analyze the idea of tipping points in the speci c contexts. In section 7, we examine the e ects of human intervention and estimate the total cost of intervention based on our model and research. In section 8, we discuss our limitations and strengths, consider the scenarios for smaller \states" and larger \states", and talk about potential future research on this topic and our framework.

<!-- b000014 | prose | pages [2] -->
2

<!-- b000015 | heading | pages [2] -->
Assumptions

<!-- b000016 | prose | pages [2] -->
Our framework measures the market impacts of di erent factors such as climate change, economic status, political stability and demographic pro les in the unit of US dollars because we think it is more e cient to quantify and examine the extent of e ects.

<!-- b000017 | prose | pages [2] -->
We de ne the state as a country for consistency and data collection purpose.

<!-- b000018 | prose | pages [2] -->
We assume all data we obtain are trustworthy since all of sources are reliable. Thus, we are con dent that our metrics can re ect the accurate condition.

<!-- b000019 | prose | pages [2] -->
3 Framework

<!-- b000020 | prose | pages [2] -->
3.1 De ning Fragility

<!-- b000021 | prose | pages [2] -->
Before devising our model, we rst de ne three possible states of a country: stable state, vulnerable state, and fragile state.

<!-- b000022 | prose | pages [2] -->
Stable state A stable country should be less likely to be in uenced by the incidents such as economic downturns, natural disasters, or political instability. Even if there is a crisis, a stable country can quickly recover and return to its equilibrium state.

<!-- b000023 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000024 | furniture | pages [3] -->
Team # 93840

<!-- b000025 | furniture | pages [3] -->
Page 3 of 19

<!-- b000026 | prose | pages [3] -->
Vulnerable state A vulnerable country is more susceptible then a stable country to the changes in the economy, politics, demographics and climate. A damaging event could cause the country leave its current state and gradually become a fragile state; a favorable event could, on the contrary, lead the country approach to the stable state.

<!-- b000027 | prose | pages [3] -->
Fragile state A fragile country is the currently experiencing uctuations in economy and politics. It does not possess a strong economy or a well-regulated society. As a result, any small turbulence could bring large impacts on all factors. Moreover, even if the country manages to recover from these disturbances, it can only resume to its previous fragile state.

<!-- b000028 | prose | pages [3] -->
3.2

<!-- b000029 | heading | pages [3] -->
The Model

<!-- b000030 | prose | pages [3] -->
To quantify a country's fragility, we use a dynamic system, in terms of money (M), to estimate the impacts of changes in di erent factors on a country. However, we believe that money is not the sole predictor of the fragility of a country. Thus, in our model, we incorporate factors including economy, politics, demographics and climate.

<!-- b000031 | prose | pages [3] -->
M = f(E; P; D; C) (1)

<!-- b000032 | prose | pages [3] -->
Here, M is a function of E; P; D; and C, where M represents the market impact of those factors, and E, P , D, C are the economic, political, demographical and climate change metrics respectively. In this way, we could comprehensively analyze a country's capability to combat unexpected events categorized under di erent sectors. We achieve this simulation by studying how the variation in one parameter would in uence the overall fragility of the society.

<!-- b000033 | prose | pages [3] -->
Further developing our model, we realize that the derivative of M is an autonomous function, that is growth rate of the market is not dependent on time. Yet, the growth rate of the market is described as the positive impact minus the negative impact.

<!-- b000034 | prose | pages [3] -->
growth rate = positive($) negative($) (2)

<!-- b000035 | prose | pages [3] -->
The positive impact considers the natural growth of the market itself accompanied with a limited capacity which varies depending on the parameters. The negative impact is composed of human intervention, disturbing climate change and other unfavorable variation in the

<!-- b000036 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000037 | furniture | pages [4] -->
Team # 93840

<!-- b000038 | prose | pages [4] -->
parameters that we have de ned.

<!-- b000039 | prose | pages [4] -->
p′(M) = m1M(1 km2

<!-- b000040 | furniture | pages [4] -->
Page 4 of 19

<!-- b000041 | prose | pages [4] -->
BM2 M M

<!-- b000042 | prose | pages [4] -->
A2 + M2 ); g′(M) = (3)

<!-- b000043 | prose | pages [4] -->
Inspired by the outbreak system by Ludwig et al. (1978), we obtain the functions above. p′(M)

<!-- b000044 | prose | pages [4] -->
represents the market growth with limited capacity, where m1 describes the growth rate, m2 represents the maximum of market capacity, and k is a scale factor that measures how economy, politics, demographics and climate change would a ect the actual limit of the market. To come up with the value of k, we use a composite index consisting of metrics in economy, politics,

<!-- b000045 | prose | pages [4] -->
demographics and climate change. g′(M) represents the negative impact that could potentially slow down the market growth. In the early development stage, M is small and the negative market impact would only show signs. However, when the market exceeds a critical level A, the negative impact would turn on quickly. This happens when the harmful events have built up to an extent that they cause a chain of reactions and the impact would nally reach to its limitation B. Therefore, we have the whole model:

<!-- b000046 | prose | pages [4] -->
dM

<!-- b000047 | prose | pages [4] -->
= m1M(1

<!-- b000048 | prose | pages [4] -->
dt

<!-- b000049 | prose | pages [4] -->
BM2

<!-- b000050 | prose | pages [4] -->
M

<!-- b000051 | prose | pages [4] -->
A2 + M2 km2

<!-- b000052 | prose | pages [4] -->
)

<!-- b000053 | prose | pages [4] -->
(4)

<!-- b000054 | prose | pages [4] -->
In order for us to examine the model more easily, we have converted the function into a dimensionless form so that there are only two parameters, r and s.

<!-- b000055 | prose | pages [4] -->
Next step, we de ne all parameters and the techniques of processing relevant data.

<!-- b000056 | prose | pages [4] -->
4 Metrics for Assessing Fragility

<!-- b000057 | prose | pages [4] -->
Our metrics are similar to indicators used in the Fragile States Index. But, instead of rating those factors, we target to collect both quantitative and qualitative data by coun-try and by year. Besides, our metrics will be more concise because we nd that there are some overlapping variables in FSI. For example, both Factionalized Elites of the Cohesion indicators and Uneven Development in Economic indicators have considered the wealth dis-tribution and tries to assess the equality of wealth (Marshall and Cole, 2017). In the end, using RStudio, we process all the datasets and obtain a composite index.

<!-- b000058 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000059 | furniture | pages [5] -->
Team # 93840

<!-- b000060 | furniture | pages [5] -->
Page 5 of 19

<!-- b000061 | prose | pages [5] -->
4.1 Climate Change

<!-- b000062 | prose | pages [5] -->
Climate change is expected to have negative impacts on human societies and economies, which may bring huge economic losses.

<!-- b000063 | prose | pages [5] -->
Occurrence of natural disasters

<!-- b000064 | prose | pages [5] -->
EM-DAT contains data on the occurrence and e ects of di erent types of natural disasters worldwide from 1900 to present. However, the data is not publicly available. So we use probabilistic risk results provided by UNISDR. The probabilistic risk results provide results of an estimate of probable loss levels in a country based on historic events. This data is useful because it considers damages caused by small, moderate and severe events and obtains a robust metric for risking ranking and comparison.

<!-- b000065 | prose | pages [5] -->
Deforestation

<!-- b000066 | prose | pages [5] -->
Food and Agriculture Organization (FAO) contains comprehensive forestry datasets such as forest coverage, reforestation, burned forest and economic value of the country's forestry value. Among them, we select the annual Tree cover loss rate by country with unit of hectare to re ect the deforestation rate as part of climate change.

<!-- b000067 | prose | pages [5] -->
Droughts/ oods

<!-- b000068 | prose | pages [5] -->
We use Precipitation Anomaly from World Bank to re ect occurrence of both droughts and oods. This dataset includes historical monthly precipitation worldwide from 1900 to present.

<!-- b000069 | prose | pages [5] -->
Rising sea levels/shrinking glaciers

<!-- b000070 | prose | pages [5] -->
Although sea level rise is a major component of global climate change, it is not a typical question for all countries. Since rising sea level and green house e ects are tightly related, we only consider temperature rises instead of rising sea level.

<!-- b000071 | prose | pages [5] -->
Rising temperatures

<!-- b000072 | prose | pages [5] -->
We retrieve historical temperature data from World Bank. This data is called Global Historical Climatology Network version 2 station monthly mean temperatures and station metadata created by U.S. National Climatic Data Center. This dataset contains quality- controlled, adjusted monthly mean temperature in unit of degree Celsius.

<!-- b000073 | prose | pages [5] -->
4.2 Economical Metrics

<!-- b000074 | prose | pages [5] -->
The economic meta-metrics considers factors related to economic decline within a country. Except for the economic factors listed below, we have also considered unequal development

<!-- b000075 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000076 | furniture | pages [6] -->
Team # 93840

<!-- b000077 | furniture | pages [6] -->
Page 6 of 19

<!-- b000078 | prose | pages [6] -->
and other relevant factors including government debts/de cits, currency uctuation, con-sumer con dence and foreign investment. More detailed descriptions of those variables are in the appendix.

<!-- b000079 | prose | pages [6] -->
Real Gross National Product (GNP) per capita

<!-- b000080 | prose | pages [6] -->
Real GNP calculates the value of all nal goods and services produced by the means of production owned by all domestic and overseas citizens of a country in a given period of time. It is di erent from the Gross Domestic Products (GDP) because GDP calculates the total values of products and services produced in the country. In other words, GNP measures the income of people within the country while GDP measures the economic productivity in a country (Stiglitz, 2009). Therefore, although GDP is more widely used, We think GNP works better in my model because we want to nd a metric that can better represent the well-being of a country. So we obtain our data of annual GNP by country from Knoema over the period of 1998 to 2012.

<!-- b000081 | prose | pages [6] -->
Unemployment rate

<!-- b000082 | prose | pages [6] -->
Our group has used the unemployment rate, % of total labor force dataset retrieved from Organization for Economic Co-operation and Development (OECD) over the period of 1953-2017. We use unemployment rate as a metric to re ect the economic decline within a country and to estimate the stability of a country.

<!-- b000083 | prose | pages [6] -->
In ation

<!-- b000084 | prose | pages [6] -->
In ation, consumer prices (annul %) dataset is obtained from International Monetary Fund, International Financial Statistics and data les. This in ation rate measures the change in the prices of a basket of selected consumer goods and services. 2010 is the base year for the calculation of in ation rate in our dataset.

<!-- b000085 | prose | pages [6] -->
Poverty level

<!-- b000086 | prose | pages [6] -->
Poverty headcount ratio at $3.20 a day (2011 PPP) (% of population) dataset is ob-tained from The World Bank. This dataset contains data in selected years from 1979 to 2016. An alternative dataset is Poverty headcount ratio at $1.90 a day (2011 PPP) (% of population), but we think $3.30 re ect a normal level of spending better than $1.90. It is di cult for one to live with only $1.90 a day even if one lives in a country with low price level, while $3.30 a day should prevent one from starving in most countries.

<!-- b000087 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000088 | furniture | pages [7] -->
Team # 93840

<!-- b000089 | furniture | pages [7] -->
Page 7 of 19

<!-- b000090 | prose | pages [7] -->
4.3 Political and Demographic Indicators

<!-- b000091 | prose | pages [7] -->
Our team collects data of corruption, health, education, water, energy and freedom of speech to represent the political indicator of the state. We use those variables to not only re-ect the basic level and quality of state functions and services but also indicate the openness of a government and its relationship with citizens. We have also taken account of demograph-ical factors including population density, natural resources abundance, internally displaced persons, and brain drain. We believe that those variables re ect the pressures upon the state deriving from the population itself and those pressures caused by the forced displacement of large communities. Details of variables and data we select are in the appendix.

<!-- b000092 | prose | pages [7] -->
5 Equilibrium and Tipping Points

<!-- b000093 | prose | pages [7] -->
Not only do we want to analyze the impact of each parameters on the overall performance of a country, we are also interested in further studying the pattern of a country's state of fragility as our model exhibit several steady states. Hence, we introduce two terms, equilibrium and tipping points. The equilibrium describes a xed point in the derivative function. In reality, this means a steady state of a country. The tipping point describes the watersheds between di erent stages of equilibrium and, in our model, the occurrence of a tipping point suggests the change in the steady states.

<!-- b000094 | prose | pages [7] -->
Equilibrium

<!-- b000095 | prose | pages [7] -->
Using the dimensionless form of the function, we set dxd

<!-- b000096 | prose | pages [7] -->
= 0 equal to zero to nd the

<!-- b000097 | prose | pages [7] -->
xed points.

<!-- b000098 | prose | pages [7] -->
(6)

<!-- b000099 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000100 | prose | pages [8] -->
We observe equation (6) has a xed point at x = 0. Intuitively, x = 0 is always a unstable xed point because when x is small, the negative impacts is fairly small so that the money supply would grow exponentially for small x near zero. Hence, we can obtain other xed points from the solutions to equation

<!-- b000101 | furniture | pages [8] -->
Team # 93840

<!-- b000102 | furniture | pages [8] -->
Page 8 of 19

<!-- b000103 | prose | pages [8] -->
r

<!-- b000104 | prose | pages [8] -->
1

<!-- b000105 | prose | pages [8] -->
r2

<!-- b000106 | prose | pages [8] -->
r3

<!-- b000107 | prose | pages [8] -->
x

<!-- b000108 | prose | pages [8] -->
r(1 k ) x 1 + x2

<!-- b000109 | prose | pages [8] -->
k

<!-- b000110 | prose | pages [8] -->
It is easier to analyze the equation graphically in that we could simply nd the intersects of the two functions. Since the right-hand side only depend on x, we can alter parameters r; s on the left-hand side to see the changes in the xed points. In Figure 1, we see that for a xed k, shifts in r

<!-- b000111 | prose | pages [8] -->
returns di erent types of solution curves. When r equals r1, the equation returns three roots,

<!-- b000112 | prose | pages [8] -->
which means the function has three xed points. However, when r-value decreases to r2, the latter

<!-- b000113 | prose | pages [8] -->
two xed points collapse into one xed point, where the line r(1 xs ) intersects the curve 1 xx2 tangentially. As r continues decreasing, there remains only one xed point. The similar pattern can be observed as well, as r values increases. To determine the stability of the xed points, we recall that x = 0 is an unstable and the stability of xed points must alternate as x increases.

<!-- b000114 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000115 | prose | pages [9] -->
Tipping Points

<!-- b000116 | prose | pages [9] -->
The phenomenon described above corresponds to two saddle-node bifurcations, where two

<!-- b000117 | prose | pages [9] -->
xed points coalesce into one and then disappears. For easier understanding, we draw dMdt versus M showing di erent solutions corresponding to di erent (r; x) values in Figure 2.

<!-- b000118 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000119 | furniture | pages [10] -->
Team # 93840

<!-- b000120 | furniture | pages [10] -->
Page 9 of 19

<!-- b000121 | prose | pages [10] -->
Stable Status

<!-- b000122 | prose | pages [10] -->
Vulnerable Status

<!-- b000123 | prose | pages [10] -->
Fragile Status

<!-- b000124 | prose | pages [10] -->
dMdt and M . The equilibriums occur when

<!-- b000125 | caption | pages [10] -->
Figure 2: This gure depicts the relationship between dMdt =

<!-- b000126 | prose | pages [10] -->
0, which are the intersects on x-axis.

<!-- b000127 | prose | pages [10] -->
Interestingly, we nd the connection between fragility states and the behaviors of di erent

<!-- b000128 | prose | pages [10] -->
types of dMdt curves. When a solution only has one smaller stable xed point near zero, M would

<!-- b000129 | prose | pages [10] -->
always approach that xed point overtime. Notice that this xed point is fairly close to zero. This implies that a country, who ts this solution curve, would have a weak economic condition and possibly a unstable political environment. As a result, this country would be defenseless when facing changes in social and environmental factors. So we think this solution curve exhibit similar behavior as a fragile country.

<!-- b000130 | prose | pages [10] -->
Nevertheless, though there is another solution with only one xed point, the second solution has a xed point much away from zero and actually shares similar pattern as a stable country. This can be largely explained by two reasons. First, the solution is always attracted to this equilibrium which is much larger than a fragile state. This results from that a stable country has a strong economy and a suitable management. Changes in society or environment would not prevent the country return to its optimal state. Second, if a country deviates from the equilibrium because of some accidents, its rate of recovering is substantially greater than that of a fragile state. Finally, a solution with three xed points (except x = 0) is considered as a representative of a vulnerable country. We observe that there are two locally attracting xed points in this curve. Thus, the solution curve

<!-- b000131 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000132 | furniture | pages [11] -->
Team # 93840

<!-- b000133 | furniture | pages [11] -->
Page 10 of 19

<!-- b000134 | prose | pages [11] -->
could approach to either xed points, one near zero representing a fragile state and one much larger representing a stable state. This suggests that when an incident happen in a vulnerable country, the country could improve its current condition and become more stable or decline to a more fragile state, depending on the nature of the incident.

<!-- b000135 | prose | pages [11] -->
Recall the previous equation (7), we know the derivatives are the same at intersections for two curves. Thus, we have the following:

<!-- b000136 | prose | pages [11] -->
Then we can rewrite the parameters k; r each as a function of x.

<!-- b000137 | prose | pages [11] -->
2x3

<!-- b000138 | prose | pages [11] -->
(1 + x2)2

<!-- b000139 | prose | pages [11] -->
r =

<!-- b000140 | prose | pages [11] -->
2x3

<!-- b000141 | prose | pages [11] -->
x2 1

<!-- b000142 | prose | pages [11] -->
, k =

<!-- b000143 | prose | pages [11] -->
(10)

<!-- b000144 | prose | pages [11] -->
As a result, we come up with a parametric plot, Figure (3), of (k(x); r(x)), where x 0. As observed, the plane is partitioned into three regions by the s r curve. According to previous analysis on fragility states, we can easily name each region by its corresponding fragility states.

<!-- b000145 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000146 | furniture | pages [12] -->
Team # 93840

<!-- b000147 | furniture | pages [12] -->
Page 11 of 19

<!-- b000148 | caption | pages [12] -->
Figure 3: This gure is a parametric plot of (s; r), where s and r are expressed as a function of t. The s r curve

<!-- b000149 | prose | pages [12] -->
represents the occurrence of a saddle-node bifurcation. In the Stable State, there is only one equilibrium; in Vulnerable State, there are three; in Fragile State, there is one.

<!-- b000150 | prose | pages [12] -->
This graph is crucial to analyze a country's fragility state. As long as we obtain the enough information on each required parameters for a country, we can convert the data to (s; r) using our composite index. Thus, we can immediately tell the current state of that country using this graph. For further application of this graph in the real world, we have conducted three case analyses in the next section.

<!-- b000151 | prose | pages [12] -->
6 Country Analysis

<!-- b000152 | prose | pages [12] -->
6.1 Syria

<!-- b000153 | prose | pages [12] -->
Syria is one of the top 10 most fragile countries in the world. The relatively weak economy system is one reason that makes it weak. Syria's GDP per capita was slightly less than $3000 and ranked at 194 out of 229 countries, according to CIA's record. Besides, the economy system of Syria depends highly on oil production. As IMF points out, oil exportation contributes to more than 25% of national income (International Monetary Fund, 2010). Hence, the declination of oil exploration had a major impact on Syria's economic

<!-- b000154 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000155 | furniture | pages [13] -->
Team # 93840

<!-- b000156 | furniture | pages [13] -->
Page 12 of 19

<!-- b000157 | prose | pages [13] -->
status. After the regulation on oil exploration and the decreasing amount of oil supply, the oil production in Syria has decreased rapidly from 2005 to 2015. It su ers from an annual growth rate of -24.5% during the decade from 2005 to 2015, and does not show any sign of resuming (BP Global, 2017). Furthermore, the increasing consumption of oil turned Syria to an oil importer rather than an exporter in 2013.

<!-- b000158 | prose | pages [13] -->
Another major reason that makes Syria fragile is its political situation. The civil war in Syria caused approximately 100,000 civilian death and more than 400,000 total death (Syrian Observatory for Human Rights, 2017). More than 4 million Syrians became refugees because of the civil war. The climate condition in Syria also restricts its economic development. With a large proportion of desert, Syria su ered heavily from scarce of water supply. More than half of the area in Syria has less than 25 centimeter of annual rainfall, and drought was not uncommon in Syria. Although Syrian could plant olives and cottons, which are the major exportation of agricultural goods in Syria, agriculture was very much restricted in variety and quantity because of the rarity of water. The climate condition in the region around Syria also causes regional tension because of the water supply, and this further causes problem in

<!-- b000159 | prose | pages [13] -->
economic development (Gleick, 2014).

<!-- b000160 | prose | pages [13] -->
This gure shows the fragility assessment of Syria and its current status in

<!-- b000161 | caption | pages [13] -->
Figure 4:

<!-- b000162 | prose | pages [13] -->
M dt

<!-- b000163 | prose | pages [13] -->
plot. The model predicts that Syria would have a negative growth rate and become more fragile.

<!-- b000164 | prose | pages [13] -->
Now, to determine how the climate change increased fragility of Syria, we omitted climate change from our variable, and the resulting graph is as shown below. The graph shows that although Syria is still in a fragile state, its xed point becomes higher, which indicates that in the long term, the economic status of Syria will be better if it does not su er from harsh

<!-- b000165 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000166 | furniture | pages [14] -->
Team # 93840

<!-- b000167 | furniture | pages [14] -->
Page 13 of 19

<!-- b000168 | prose | pages [14] -->
climate. Also, we can see that the curve shifts upward compared to the one accounting for climate condition, and this implies that its rate of decrease will be much slower than it is right now.

<!-- b000169 | prose | pages [14] -->
Looking back at our equation, since we omitted climate conditions, the parameter k and

<!-- b000170 | prose | pages [14] -->
A will change consequently. Since k is positively associated with climate condition, k value will increase after we omitted negative e ect of climate. This is similar for A. Hence, we would expect r to increase because of increase in A, and s will not increase by much because both k and A will increase although k increases slightly more than A. This corresponds to our s r plot as well. As can be seen from the s r plot, the point becomes closer to the vulnerable state than when we considered climate. This also corresponds to our research that harsh climate condition played a signi cant role on making Syria fragile, causing con icts with neighboring countries as well as restricting economic growth. For example, limited water resources could cause a potential shortage of water supply and food supply, which will cause internal displacement and even panic (Gleick, 2014).

<!-- b000171 | prose | pages [14] -->
6.2 Cuba

<!-- b000172 | prose | pages [14] -->
Fragile state index of Cuba ranks 119th out of 178 countries. FSI categorizes Cuba in the list of \warning" countries and describes Cuba as the most improved country of the past 10 years due to its economic and political reforms launched by Cuban President Raul Castro who rstly assumed power in 2006 (Marshall and Cole, 2017).

<!-- b000173 | prose | pages [14] -->
In 2008, restrictions on owning mobile phones were lifted and in 2009, U.S. former Pres- ident Obama removed restrictions on Cuban Americans and allowed money transfer. In 2011, President Raul Castro enacted economic reforms to stimulate small business and en-trepreneurs and to provide opportunities for individuals to increase their incomes. In the same year, he also instituted a two-term limit for running the o ce of president and when he was re-elected in 2013, he announced that he would leave politics at the end of his second term.

<!-- b000174 | prose | pages [14] -->
During President Raul Castro's second term, the political tensions between U.S. and Cuba were eased. Both Castro and Obama announced in 2014 that they were working to normalize diplomatic relations, underlining these e orts by exchanging political prisoners (Peters, 2012). In 2015, Cuba renegotiated a major portion of its o cial debt. After reaching agreement of multiple debtors such as China, Mexico and Russia and a high percentage of debts were forgiven, Cuba's risk rating by Moody increased from stable to positive.

<!-- b000175 | prose | pages [14] -->
In terms of sustainable development, researchers agreed that Cuban government should prioritize the sustainability to provide long-term growth in social, economic and environ-

<!-- b000176 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000177 | furniture | pages [15] -->
Team # 93840

<!-- b000178 | furniture | pages [15] -->
Page 14 of 19

<!-- b000179 | prose | pages [15] -->
mental facets (Davis and Piccone, 2017).

<!-- b000180 | prose | pages [15] -->
Nevertheless, from 2008 to 2015, investment in Cuba has decreased by 17%, exports has fallen by 5% and real GDP has dropped by approximately 1 percent. Moreover, largely due to the nancial crisis in Venezuela, Cuba still has a scal de cit of 10.1% of GDP, while the de cit in U.S. is 3.4% of GDP in 2017 according to Central Intelligence Agency Database. Therefore, despite of the large improvements in the last decade, Cuba's remaining debts, the U.S. embargo, restrictions on eligibility of Foreign Direct Investment and Cuba's dual currency system still pose a huge challenge to the country's economic development and growth in the future.

<!-- b000181 | caption | pages [15] -->
Figure 5: This gure shows the fragility assessment of Cuba and its current status in M dMdt plot. The model

<!-- b000182 | prose | pages [15] -->
predicts that Cuba would maintain a high growth rate.

<!-- b000183 | prose | pages [15] -->
Now, we shall look at the data to see how climate change makes Cuba fragile. Our data shows that the main reasons that drag down Cuba's climate parameter are occurrence of natural disasters and droughts. By replacing these two factors with global average, we can see a increase in climate parameter, which will then increase parameter k and A. With a similar analysis as in the case of Syria, we would expect both r and s to increase slightly, and this will help Cuba to approach the stable state. As can be seen from the graph below, we see a slight upward shift of the curve, which shows that Cuba will become slightly more stable if its amount of rainfall is normal and does not su er from unusual natural disasters. The r s plot further con rms this.

<!-- b000184 | prose | pages [15] -->
As for the tipping point, Cuba will reach a tipping point where it becomes a stable state when r or s increases. Since r = AmB1 , s = kmA2 , to increase r or s we shall increase k, A, or

<!-- b000185 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000186 | furniture | pages [16] -->
Team # 93840

<!-- b000187 | furniture | pages [16] -->
Page 15 of 19

<!-- b000188 | prose | pages [16] -->
decrease B. Since B is relatively robust, we will only consider how we can increase k and

<!-- b000189 | prose | pages [16] -->
A. Since k is positively associated with climate, policy and demographic, we would expect Cuba to reach tipping point if it could implement better political environment. Because of structure and natural resources of Cuba, it is di cult to change the climate and demographic, so we will not further discuss change of these two variables. As for A, since it is positively associated with the economic status, climate, policy and demographic, Cuba will reach tipping point if the economic status and political environment are improved.

<!-- b000190 | caption | pages [16] -->
Figure 6: This bifurcation plot positioned three countries at their current states and shows the potential

<!-- b000191 | prose | pages [16] -->
change of position.

<!-- b000192 | prose | pages [16] -->
6.3 New Zealand

<!-- b000193 | prose | pages [16] -->
New Zealand's fragile state index ranks 169th out of 178 countries. FSI categorizes New Zealand in the list of "sustainable" countries. Sustainable development has been the central focus for Ministry (The Heritage Foundation, 2018). Access to natural resources, water quality, urban issues and climate change are major sustainable development issues for New Zealand in the early years of the 21st century.

<!-- b000194 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000195 | furniture | pages [17] -->
Team # 93840

<!-- b000196 | furniture | pages [17] -->
Page 16 of 19

<!-- b000197 | prose | pages [17] -->
In 1991, the Resource Management Act was enacted to allows public participation com- munities are making decisions on resource consents. This legislation let New Zealand become the rst to adopt sustainability principles. Since the last decade, environmental policies have started to integrate with social, economic and cultural aims, which results a sustainable de- velopment framework.

<!-- b000198 | prose | pages [17] -->
Initiatives such as new air quality standards, improvements in sewage systems, closure of sub-standard land lls, and clean-up of priority contaminated sites are leading to measurable improvements in the quality of air, water and land resources (Bebbington et al., 2009). So government pays considerable e orts to address immediate threats to key natural resources.

<!-- b000199 | prose | pages [17] -->
New Zealand has an open and export-driven economy with exports accounting for 30% of GDP. Its economy has been growing steadily recent years. The OECD (2015) commented that New Zealand has strong scal monetary policy frameworks and a healthy nancial sec-tor, which have yielded macroeconomic stability. Although New Zealand's economy slowed down during the 2008 nancial crisis, the economy quickly recovered in 2010 and increased the growth rate by 3.7 percentage points, unlike most OECD countries.

<!-- b000200 | prose | pages [17] -->
New Zealands political system is based on the British model and is considered to be relatively stable. There is a single house of Parliament and the role of head of state is held by Queen of New Zealand. Democratic engagement is strong and typically between 75-80% of New Zealanders turn out to vote in general elections.

<!-- b000201 | prose | pages [17] -->
The following graph of the fragility assessment of New Zealand shows that New Zealand is currently in the stable state and is slowing approaching to the xed point. This nding con rms our expectation based on our research and suggests the robustness and validity of our framework.

<!-- b000202 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000203 | furniture | pages [18] -->
Team # 93840

<!-- b000204 | furniture | pages [18] -->
Page 17 of 19

<!-- b000205 | caption | pages [18] -->
Figure 7: This gure shows the fragility assessment of New Zealand and its current status in M dMdt plot. The

<!-- b000206 | prose | pages [18] -->
model shows that New Zealand is slowly approaching its equilibrium.

<!-- b000207 | prose | pages [18] -->
7 Human Intervention

<!-- b000208 | prose | pages [18] -->
We think human intervention can be re ected by the political indicators because human can enact policies and enforce legislations to a ect dynamics of a society, in our case, a country. The impacts of human intervention can be both positive and negative. For example, when a country prioritizes its economic growth and manufacturing sector, it is sometimes possible that this country overlooks the environmental policies and the sustainable growth. Therefore, it would take more human e orts than expected on mitigating the risk of climate change, not only including those targeted on unexpected natural disasters but also on long-term sustainable developments.

<!-- b000209 | prose | pages [18] -->
Since Cuba is in the range of vulnerable countries, our team chooses to examine the impacts and costs of human intervention in Cuba and use both of our empirical framework and research to show that interventions alleviate the negative market impacts of climate change and preventing Cuba from becoming a fragile state.

<!-- b000210 | prose | pages [18] -->
Extreme weather conditions has always been the primary concern for Cuba. In 2008, four hurricanes Fay, Gustav, Ike and Paloma damaged 647 thousand dwellings, resulted an estimated amount of 9.76 billion pesos economic losses. The country has also su ered extreme drought which severely a ected croplands and availability of water, and increased danger from res. In 2013, 388 forest re were reported and lost 4279 hectares of forest. Despite those direct economic losses, loss of human life has been fairly low due to government's

<!-- b000211 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000212 | furniture | pages [19] -->
Team # 93840

<!-- b000213 | furniture | pages [19] -->
Page 18 of 19

<!-- b000214 | prose | pages [19] -->
warning and the e ective Civil Defense system.

<!-- b000215 | prose | pages [19] -->
Some research suggests that climate changes in Cuba are associated with ecological and socio-economic changes that promote epidemiological shifts a ecting the health system (El-Sobki et al., 2009). Cuba's First National Communication to the United Nations Framework Convention on Climate Change identi es the sectors of water, forestry and agriculture as the most vulnerable to the e ects of climate change.

<!-- b000216 | prose | pages [19] -->
Cuba has a long history of policy initiatives to address climate change. In 1991, Na-tional Commission on Climate Change was created with a mandate to study the impacts of the phenomenon on its population, food production, water supplies and health. In recent years, Cuba has taken many measures on environmental issues and climate change (Alonso and Clark, 2015). In 2007, Cuba launched the Cuban Society Program to Face Climate Change which analyzes all sectors of the Cuban economy in terms of vulnerability to climate change and required adaptation measures. In addition to those e orts, Cuba has established a sophisticated national disaster risk reduction framework through the creation of a com-prehensive Civil Defense System that protects lives in the case of extreme climatic events and acts as an early warning system. From 1998 to 2008, environmental protection spending increased from 41.9 million pesos about 1.8% of total public spending to 335.6 million pesos about 6.4% of total spending (ElSobki et al., 2009). And based on our model, we project that if the Cuban government is going to alleviate or even eliminate the negative e ects of climate change, the total cost, which is also the magnitude of political indicators in the function, would be more than $12 billion dollars by 2025.

<!-- b000217 | prose | pages [19] -->
There is moderate number of current discrete adaptation projects in Cuba. Those adap-tation projects are addressing needs related to each of its identi ed priority sectors of agri-culture and, to a less extent, freshwater resources and forestry. Our group think that future initiatives could expand upon its current adaptation e orts related to agriculture, disaster risk management, government, coastal zone management and water. They could also close observed gaps related to human health, the di erential impacts of climate change by gender.

<!-- b000218 | prose | pages [19] -->
8

<!-- b000219 | heading | pages [19] -->
Discussion & Conclusion

<!-- b000220 | prose | pages [19] -->
One strength of our model is its exibility. All the parameters are relatively independent from each other. Hence, it is easy to change metrics without making major changes to our model. Besides, this helps us to use our model to predict what happens if we change one or some of the parameters, and thereby making predictions for future. Another strength is that it ts the result from Fragile State Index, which shows the accuracy of our model. However,

<!-- b000221 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000222 | furniture | pages [20] -->
Team # 93840

<!-- b000223 | furniture | pages [20] -->
Page 19 of 19

<!-- b000224 | prose | pages [20] -->
there are also limitations. One limitation is that the weight of each parameter may be revised to make this model more accurate. Also, we did not account for the interaction between countries, which may play an important role in evaluating fragility of some countries.

<!-- b000225 | prose | pages [20] -->
Our model can be used to evaluate fragility of small \states", such as cities. To do so, we can nd data for the city and plug into our model to see where the city locates on the graph. However, it may be di cult to use our model to evaluate fragility of larger \states" because we have to change our de nition of some data we are using. For example, we may need to de ne carefully on corruption for a continent. We may use the GDP or population, etc as weights to calculate a mean for the continent. Besides, some data may not be de ned over a continent, like devaluation of currency. After carefully de ne new metrics for assessing fragility of a continent, we may plug in our equation to make it work on larger \states".

<!-- b000226 | prose | pages [20] -->
In our paper, we have developed a framework that measures the fragility of a state, taking account of economic, political, demographical factors and climate change. Our framework accounts for a composite measure of major metrics and uses logistic equations to represent the positive and negative market impacts of those factors with carrying capacities. To check the robustness and validity of our model's results, we selected three representative countries, Syria, Cuba and New Zealand. Our results follow the latest ranking by Fragile State Index, where Syria, Cuba and New Zealand are considered to be fragile, vulnerable and stable respectively. Moreover, we further analyze the impacts of climate change by calibrating our meta-metrics and evaluating the potential level of selected countries.

<!-- b000227 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000228 | furniture | pages [21] -->
Team # 93840

<!-- b000229 | furniture | pages [21] -->
Page 20 of 19

<!-- b000230 | heading | pages [21] -->
Appendix A

<!-- b000231 | prose | pages [21] -->
Data

<!-- b000232 | prose | pages [21] -->
Economic Metrics

<!-- b000233 | prose | pages [21] -->
Collapse/devaluation of currency

<!-- b000234 | prose | pages [21] -->
There is no worldwide index for devaluation of currency, although we have Euro Cur- rency index and US Dollar index. Our approach to tackle this is to use the exchange rate of each country with respect to US dollar and calculate the change of the ex-change rate for each year. We obtain exchange rate data from OECD over the period of 2000-2017.

<!-- b000235 | prose | pages [21] -->
Consumer con dence

<!-- b000236 | prose | pages [21] -->
Our group uses Consumer Con dence index retrieved from OECD to represent the consumer con dence in each country. The data is updated either monthly, and is based on household's decision on major purchasing and their economic status in near future. We can use this to predict the economic development in short term.

<!-- b000237 | prose | pages [21] -->
Foreign investment

<!-- b000238 | prose | pages [21] -->
Foreign direct investment, net in ows (% of GDP) dataset is collected by the World Bank from 1970 to 2016. This shows the con dence of foreign investors for the country.

<!-- b000239 | prose | pages [21] -->
Government debts/de cits

<!-- b000240 | prose | pages [21] -->
General government de cit is available on OECD over the period of 2000-2016. It can be used as an indicator of how stable the government is.

<!-- b000241 | prose | pages [21] -->
Uneven Development

<!-- b000242 | prose | pages [21] -->
The uneven development metrics considers the structural inequality based on group, education, economic status and region. Not only actual inequality but also perceptual in-equality are considered since perceived inequality can also aggravate the tensions within the communities and society. This uneven development also includes opportunities for groups to improve their economic status though access to employment and education.

<!-- b000243 | prose | pages [21] -->
Gini coe cient

<!-- b000244 | prose | pages [21] -->
GINI index from 1979-2015 can be retrieved from World Bank. This is a major metrics measuring the unbalance of distribution of wealth in a country, where 0 represents perfectly equal and 100 represents perfectly unequal.

<!-- b000245 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000246 | furniture | pages [22] -->
Team # 93840

<!-- b000247 | furniture | pages [22] -->
Page 21 of 19

<!-- b000248 | prose | pages [22] -->
Equal rights

<!-- b000249 | prose | pages [22] -->
It is true that equal rights is very important as a factor to show how well people in a country live and can be calculated using the framework provided by United Nations human Rights O ce of High Commissioner, but it conveys similar message as the combination of some other indicators, such as freedom of speech, health, education, corruption, etc. Hence, we will not include this indicator separately in our paper.

<!-- b000250 | prose | pages [22] -->
Political Metrics

<!-- b000251 | prose | pages [22] -->
Corruption

<!-- b000252 | prose | pages [22] -->
This considers representativeness and openness of government and the perception of government by citizens. Corruption Perception Index over the period of 1996 to 2016 can be obtained from The World Bank.

<!-- b000253 | prose | pages [22] -->
Health

<!-- b000254 | prose | pages [22] -->
This considers how well a country's health care system perform and how e cient the health care system is. We will use the ranking and data created by World Health Organization (WHO) to assess the health system of a country.

<!-- b000255 | prose | pages [22] -->
Education

<!-- b000256 | prose | pages [22] -->
This measures whether people in a given country have access to essential education. Education Index is a good indicator of this, and it can be obtained from United Nations Development Programme.

<!-- b000257 | prose | pages [22] -->
Water

<!-- b000258 | prose | pages [22] -->
Basic and safely managed drinking water services from WHO measures the percentage of population that have access to basic drinking-water services. It contains rural, urban and overall data for each country.

<!-- b000259 | prose | pages [22] -->
Energy

<!-- b000260 | prose | pages [22] -->
The World Bank provides data for Access to electricity (% of population) from 1990 to 2014. This data can be important because it helps us understanding how well the overall energy level and this further in uences the economic growth of the country.

<!-- b000261 | prose | pages [22] -->
Freedom of speech

<!-- b000262 | prose | pages [22] -->
This data measures whether people living in a country have freedom of speech. Our team uses World Press Freedom Index from Reporters Without Boarder as an indicator. Although this focuses mainly on press freedom, it can re ect the overall freedom as

<!-- b000263 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000264 | furniture | pages [23] -->
Team # 93840

<!-- b000265 | furniture | pages [23] -->
Page 22 of 19

<!-- b000266 | prose | pages [23] -->
well because in most cases people have the rights to talk privately about their criticism about the government but may not be able to publish on press.

<!-- b000267 | prose | pages [23] -->
Demographic Metrics

<!-- b000268 | prose | pages [23] -->
Population density

<!-- b000269 | prose | pages [23] -->
Population density (people per sq. km of land area) can be found from The World Bank. This measurement helps us to predict the trend of future economic development.

<!-- b000270 | prose | pages [23] -->
Natural Resources abundance

<!-- b000271 | prose | pages [23] -->
Total natural resources rents (% of GDP) from The World Bank can be used to rep-resent natural resources of a country. This also helps us to predict the potential of economic development.

<!-- b000272 | prose | pages [23] -->
Internally displaced persons

<!-- b000273 | prose | pages [23] -->
internal displacement datasets is collected by Internally Displaced Monitoring Centre (IDMC). This dataset contains estimate of number of people displaced because of con icts or disaster in a country.

<!-- b000274 | prose | pages [23] -->
Brain drain

<!-- b000275 | prose | pages [23] -->
Brain Drain data is established by Institute for Employment Research over the period of 1980-2010 (Br•ucker et al., 2013). This data covers the international migration in- formation for 20 OECD destination countries by gender, country of origin and level of education. Its data contains total number of foreign-born individuals aged 25 years or older.

<!-- b000276 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000277 | furniture | pages [24] -->
Team # 93840

<!-- b000278 | heading | pages [24] -->
References

<!-- b000279 | furniture | pages [24] -->
Page 23 of 19

<!-- b000280 | references | pages [24] -->
Alonso, G., and Clark, I. (2015). \Cuba confronts climate change." MEDICC review, 17, 10{13.

<!-- b000281 | references | pages [24] -->
Bebbington, J., Higgins, C., and Frame, B. (2009). \Initiating sustainable development reporting:

<!-- b000282 | references | pages [24] -->
evidence from New Zealand." Accounting, Auditing & Accountability Journal,

<!-- b000283 | references | pages [24] -->
22 (4), 588{625.

<!-- b000284 | references | pages [24] -->
BP Global (2017). \Oil - BP statistical review of world energy 2017." Tech. rep.

<!-- b000285 | references | pages [24] -->
Br•ucker, H., Capuano, S., and Marfouk, A. (2013). \Education, gender and international

<!-- b000286 | references | pages [24] -->
migration: insights from a panel-dataset 1980-2010." Retrieved March, 20, 2014.

<!-- b000287 | references | pages [24] -->
Davis, C., and Piccone, T. (2017). \Sustainable development: The path to economic growth in

<!-- b000288 | references | pages [24] -->
Cuba." The Brookings Institute.

<!-- b000289 | references | pages [24] -->
ElSobki, M., Yasser, P. W. I., Elsobki, M., Wooders, P., and Sherif, Y. (2009). \Clean energy

<!-- b000290 | references | pages [24] -->
investment in developing countries." Wind power in Egypt. Winnipeg, Manitoba, Canada:

<!-- b000291 | references | pages [24] -->
International Institute for Sustainable Development.

<!-- b000292 | references | pages [24] -->
Gleick, P. H. (2014). \Water, drought, climate change, and con ict in Syria." Weather, Climate,

<!-- b000293 | references | pages [24] -->
and Society, 6 (3), 331{340.

<!-- b000294 | references | pages [24] -->
International Monetary Fund (2010). \Syrian Arab Republic: 2009 article IV consultation sta

<!-- b000295 | references | pages [24] -->
report; and public information notice." Tech. rep.

<!-- b000296 | references | pages [24] -->
Ludwig, D., Jones, D. D., and Holling, C. S. (1978). \Qualitative analysis of insect outbreak

<!-- b000297 | references | pages [24] -->
systems: the spruce budworm and forest." The Journal of Animal Ecology, 315{332.

<!-- b000298 | references | pages [24] -->
Marshall, M. G., and Cole, B. R. (2017). \Fragile States Index methodology and CAST

<!-- b000299 | references | pages [24] -->
framework." Global Report.

<!-- b000300 | references | pages [24] -->
OECD (2015). \OECD economic surveys, New Zealand."

<!-- b000301 | references | pages [24] -->
Peters, P. (2012). A viewer's guide to Cuba's economic reform. Lexington Institute Arlington.

<!-- b000302 | references | pages [24] -->
Stiglitz, J. E. (2009). \GDP fetishism." The Economists' Voice, 6 (8).

<!-- b000303 | references | pages [24] -->
Syrian Observatory for Human Rights (2017). \About 500000 persons were killed in Syria

<!-- b000304 | references | pages [24] -->
during 81 months after the Syrian revolution started."

<!-- b000305 | references | pages [24] -->
The Heritage Foundation (2018). \2018 index of economic freedom."

<!-- b000306 | references | pages [24] -->
UNISDR

<!-- b000307 | references | pages [24] -->
(2014).

<!-- b000308 | references | pages [24] -->
\Disaster

<!-- b000309 | references | pages [24] -->
&

<!-- b000310 | references | pages [24] -->
risk

<!-- b000311 | references | pages [24] -->
pro

<!-- b000312 | references | pages [24] -->
le

<!-- b000313 | references | pages [24] -->
by

<!-- b000314 | references | pages [24] -->
country."

<!-- b000315 | references | pages [24] -->
Data

<!-- b000316 | references | pages [24] -->
retrieved

<!-- b000317 | references | pages [24] -->
from

<!-- b000318 | references | pages [24] -->
https://www.preventionweb.net/english/hyogo/gar/2015/en/home/.
