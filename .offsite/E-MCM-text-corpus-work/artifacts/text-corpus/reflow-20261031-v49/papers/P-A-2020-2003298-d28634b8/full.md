# P-A-2020-2003298-d28634b8

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen A 2020 MCM/ICM Team Control Number 2003298

<!-- b000002 | heading | pages [1] -->
Summary Sheet

<!-- b000003 | title | pages [1] -->
Keeping up with the Migrating Fish

<!-- b000004 | prose | pages [1] -->
Gradual rise of the ocean temperature results in a significant shift in the distribution of herring and mackerel. This situation may cause catastrophe for the small fishing companies in Scotland, for they may not be able to catch sufficient fish in their current location. Our team was asked to identify the most likely distribution of herring and mackerel in the next 50 years, and give practical suggestions to Scotland fishermen based on our study results.

<!-- b000005 | prose | pages [1] -->
For problem 1, we start by analyzing the sea surface temperature data for the past 39 years and use Proper Orthogonal Decomposition to decompose the original dataset into two parts: the spatial term POD modes and the temporal term time coefficients. After retaining the 3 most significant POD modes, we assume that the POD modes are stable over time and achieve our sea surface temperature prediction through the prediction of their corresponding time coefficients. We proceed to estimate the locations of herring and mackerel over the next 50 years based on their habitat temperature. Our conclusion is that in the Atlantic Ocean north-west to Scotland, herring and mackerel will move northward away from the British Isles over the next 50 years. And in the North Sea, herring will gradually move toward east direction.

<!-- b000006 | prose | pages [1] -->
For problem 2, we begin with developing a nutrient loss model to predict the freshness change along with time. Given the maximum acceptable level of nutrient loss and storage temperature, we are able to determine the expected storage time for the catch. Then we calculate the maximum travelling distance for herring and mackerel catch to be 300 km and 500 km, respectively. Based on the movement of fish over the next 50 years, we conclude that the earliest time for mackerel and herring to move away from the fishing range is year 2027 and 2033, and the most likely year is 2045 and 2043. No critical year for the worst case of mackerel moving away from the fishing range and 2066 is the latest time for herring moving out of the fishing range of small vessels.

<!-- b000007 | prose | pages [1] -->
For problem 3, we propose three possible strategies for small fishing companies in order to help them adapt to changing situations. The first strategy is relocating the fishing companies. We estimate that when all the fishing companies in Scotland are relocated, the net benefit would be 65 pound million per year, considering the fishing industry as a whole. The second strategy is changing the fishing mode. In a new fishing mode, some proportion of vessels are used as fishing vessels while the other are used as shipping vessels which equipped with on-board refrigeration system. We also develop a model of required storage temperature on-board in different years, which gives suggestions to small fish companies who need to change their fishing mode in 2045. The third strategy is building a warehouse on high sea islands like Shetland island to preserve fish caught by small vessels, which will also expand the fishing range of small vessels.

<!-- b000008 | prose | pages [1] -->
For problem 4, we modify our proposals considering of fishing restrictions in territorial water. Based on the model in problem 1 and problem 2, all the herring would enter the territory of Danish in 2035. Under the new restrictions, the time of changing into new fishing mode should happen in 2036 rather than 2045, resulting in losing money for small companies.

<!-- b000009 | prose | pages [1] -->
Finally, we analyze the accuracy and sensitivity of our model, proving that our model is accurate and stable for different parameters.

<!-- b000010 | keywords | pages [1] -->
Keywords: Proper orthogonal decomposition, Fish migration, Differential equation, Fishing strategies

<!-- b000011 | furniture | pages [1] -->
关注数学模型 获取更多资讯 2 MATHmodels

<!-- b000012 | furniture | pages [2] -->
Team # 2003298

<!-- b000013 | furniture | pages [2] -->
Page 1 of 23

<!-- b000014 | heading | pages [2] -->
Contents

<!-- b000015 | contents | pages [2] -->
1 Introduction

<!-- b000016 | contents | pages [2] -->
3

<!-- b000017 | contents | pages [2] -->
2 Model Assumptions and Symbols

<!-- b000018 | contents | pages [2] -->
3

<!-- b000019 | contents | pages [2] -->
2.1

<!-- b000020 | contents | pages [2] -->
Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
2.2

<!-- b000023 | contents | pages [2] -->
Symbols

<!-- b000024 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
4

<!-- b000026 | contents | pages [2] -->
3 Solution to Problem 1

<!-- b000027 | contents | pages [2] -->
4

<!-- b000028 | contents | pages [2] -->
3.1

<!-- b000029 | contents | pages [2] -->
Prediction of sea surface temperature

<!-- b000030 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
3.1.1

<!-- b000033 | contents | pages [2] -->
Applying POD to the dataset . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
5

<!-- b000035 | contents | pages [2] -->
3.1.2

<!-- b000036 | contents | pages [2] -->
Predicting future sea surface temperature . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
7

<!-- b000038 | contents | pages [2] -->
3.2

<!-- b000039 | contents | pages [2] -->
Prediction of future locations for herring and mackerel

<!-- b000040 | contents | pages [2] -->
. . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
8

<!-- b000042 | contents | pages [2] -->
4 Solution to problem 2

<!-- b000043 | contents | pages [2] -->
9

<!-- b000044 | contents | pages [2] -->
4.1

<!-- b000045 | contents | pages [2] -->
Prediction of quality deterioration

<!-- b000046 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
10

<!-- b000048 | contents | pages [2] -->
4.1.1

<!-- b000049 | contents | pages [2] -->
Biochemical mechanism . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
10

<!-- b000051 | contents | pages [2] -->
4.1.2

<!-- b000052 | contents | pages [2] -->
Nutrient loss model

<!-- b000053 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
10

<!-- b000055 | contents | pages [2] -->
4.1.3

<!-- b000056 | contents | pages [2] -->
Results and analysis . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
13

<!-- b000058 | contents | pages [2] -->
4.2

<!-- b000059 | contents | pages [2] -->
Estimation of ﬁshing range

<!-- b000060 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
13

<!-- b000062 | contents | pages [2] -->
4.2.1

<!-- b000063 | contents | pages [2] -->
Deﬁnition of useful terms . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
13

<!-- b000065 | contents | pages [2] -->
4.2.2

<!-- b000066 | contents | pages [2] -->
Results for three cases . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
14

<!-- b000068 | contents | pages [2] -->
5 Solution to problem 3

<!-- b000069 | contents | pages [2] -->
16

<!-- b000070 | contents | pages [2] -->
5.1

<!-- b000071 | contents | pages [2] -->
Relocate ﬁshing companies

<!-- b000072 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
16

<!-- b000074 | contents | pages [2] -->
5.2

<!-- b000075 | contents | pages [2] -->
Change ﬁshing mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
17

<!-- b000077 | contents | pages [2] -->
5.3

<!-- b000078 | contents | pages [2] -->
Establish transit stations . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
19

<!-- b000080 | contents | pages [2] -->
6 Solution to problem 4

<!-- b000081 | contents | pages [2] -->
19

<!-- b000082 | contents | pages [2] -->
7 Sensitivity Analysis

<!-- b000083 | contents | pages [2] -->
20

<!-- b000084 | contents | pages [2] -->
8 Strengths and weaknesses

<!-- b000085 | contents | pages [2] -->
21

<!-- b000086 | contents | pages [2] -->
9 Article for Hook Line and Sinker

<!-- b000087 | contents | pages [2] -->
22

<!-- b000088 | contents | pages [2] -->
关注数学模型

<!-- b000089 | furniture | pages [2] -->
2

<!-- b000090 | furniture | pages [2] -->
MATHmodels

<!-- b000091 | furniture | pages [2] -->
获取更多资讯

<!-- b000092 | furniture | pages [3] -->
Team # 2003298

<!-- b000093 | furniture | pages [3] -->
Page 2 of 23

<!-- b000094 | heading | pages [3] -->
1 Introduction

<!-- b000095 | prose | pages [3] -->
Scotland is the largest sea ﬁshing nation within the UK. However, due to the rising ocean temperature, many ocean-dwelling species, including Scottish herring and mack- erel, are migrating to the north for new habitats. The migration of these species has posed a severe threat to small ﬁshing companies, whose livelihood depends heavily on the stability of local ﬁsh species. Thus, it is crucial to assess how this geographic popu- lation shift could impact the local ﬁshery industry.

<!-- b000096 | prose | pages [3] -->
This paper aims to aid the Scottish ﬁshery management consortium in developing favorable ﬁshing strategies. To offer the government a better insight into the migration issue, we construct a series of mathematical models to predict the distribution of the two ﬁsh species over time and quantify its impact on ﬁshing companies.

<!-- b000097 | prose | pages [3] -->
Our speciﬁc tasks include the followings:

<!-- b000098 | prose | pages [3] -->
• Determine the geographic distribution of Scottish herring and mackerel over the next 50 years.

<!-- b000099 | prose | pages [3] -->
• Identify the point of time when the population migrates beyond the current ﬁshing range. That is, the elapsed time until the population is too far away for small ﬁshing vessels to harvest.

<!-- b000100 | prose | pages [3] -->
• Assess two different ﬁshing strategies, including relocating the ﬁshing companies and updating the ﬁshing vessels, in terms of beneﬁts and economic feasibility.

<!-- b000101 | prose | pages [3] -->
• Analyze how the territorial issue may affect ﬁshing strategies.

<!-- b000102 | heading | pages [3] -->
2 Model Assumptions and Symbols

<!-- b000103 | heading | pages [3] -->
2.1 Assumptions and Justiﬁcations

<!-- b000104 | prose | pages [3] -->
• We assume that the temperature of habitats for herring and mackerel is consistent with the surface temperature of the sea. In fact, most herring and mackerels live in the area less than 200 meters below sea level, and the temperature in the shallow water is basically balanced. Thus, we could ignore the vertical difference of ocean temperature.

<!-- b000105 | prose | pages [3] -->
• We assume that the maximum distance a ﬁshing vessel can travel is solely deter- mined by the expected storage time of the catch. Small ﬁshing vessels are not capable of long-distance traveling mainly because they must ensure the freshness of the catch. Thus,we deem that storage time is the primary factor restricting the traveling distance.

<!-- b000106 | prose | pages [3] -->
• We assume that the temperature on the vessel, or the storage temperature for the catch, is constant for each trip.

<!-- b000107 | prose | pages [3] -->
关注数学模型

<!-- b000108 | furniture | pages [3] -->
2

<!-- b000109 | furniture | pages [3] -->
MATHmodels

<!-- b000110 | furniture | pages [3] -->
获取更多资讯

<!-- b000111 | furniture | pages [4] -->
Team # 2003298

<!-- b000112 | furniture | pages [4] -->
Page 3 of 23

<!-- b000113 | heading | pages [4] -->
2.2 Symbols

<!-- b000114 | caption | pages [4] -->
Table 1 shows symbols and notations used in this paper. Note that symbols used

<!-- b000115 | prose | pages [4] -->
only once are not included and will be deﬁned later.

<!-- b000116 | caption | pages [4] -->
Table 1: Symbols and notations

<!-- b000117 | prose | pages [4] -->
symbol deﬁnition

<!-- b000118 | prose | pages [4] -->
D NOAA DOISST dataset Si sea surfacetemperature snapshot A level of TVB-N or K value T absolute temperature (K) t expected storage time

<!-- b000119 | heading | pages [4] -->
3 Solution to Problem 1

<!-- b000120 | heading | pages [4] -->
3.1 Prediction of sea surface temperature

<!-- b000121 | prose | pages [4] -->
We proceed to predict the sea surface temperature changes (SST) over the next 50 years by analyzing the NOAA daily optimum interpolation SST dataset (DOISST) (Esrl.noaa.gov, 2020). In spatial terms, our dataset covers the northeast Atlantic, the southern Norwegian sea, and the entire area of the North Sea. The latitude and longi- tude range from 26.5◦W to 12.5◦E and from 51.5◦N to 67.5◦N respectively. Every two data points are spaced one degree apart. As for the temporal dimension, our dataset includes monthly sea surface temperature data for nearly 40 years, from December 1981 to January 2020.

<!-- b000122 | prose | pages [4] -->
For these spatiotemporal data, the simplest prediction method is to analyze the his- torical changes of each data point and predict the possible values of these points at a certain time in the future, then use these discrete results to represent the temperature changes of the whole sea area. However, there are obvious problems with this attempt. Local temperature changes can be easily disturbed by anomalies (e.g., wars or other hu- man activities that affect the ecological environment of a certain area). The way the data points are predicted separately failed to exclude these outliers, thus leading to inaccu- rate predictions. On the other hand, sea surface temperature changes, as well as global warming, is a holistic process. This can be explained by the fact that human activities are often inherently correlated. Therefore, the temperature changes of a certain area may have intrinsic relationships with its nearby area. All these factors indicate that we should solve this problem by regarding it as a whole.

<!-- b000123 | prose | pages [4] -->
Although we try to avoid predicting the data separately, we still need to account for the outliers mentioned above. To eliminate these outliers, we need to ﬁnd a way to extract the regular patterns from the sea surface temperature changes and discard the impact caused by random events. This introduces our proposed method: Proper Orthogonal Decomposition (POD). (Noori et al., 2017)

<!-- b000124 | prose | pages [4] -->
The POD method is capable of extracting a series of deterministic functions (often called POD modes) from the original dataset, which has the largest ﬂuctuating kinetic

<!-- b000125 | prose | pages [4, 5] -->
关注数学模型 energy in terms of ﬂuid dynamics. It is also able to decompose the original dataset into two parts: one part only related to time and the other only related to space. Through the prediction of the time-dependent part, the overall prediction of sea surface temperature is achieved.

<!-- b000126 | furniture | pages [4] -->
2

<!-- b000127 | furniture | pages [4] -->
MATHmodels

<!-- b000128 | furniture | pages [4] -->
获取更多资讯

<!-- b000129 | furniture | pages [5] -->
Team # 2003298

<!-- b000130 | furniture | pages [5] -->
Page 4 of 23

<!-- b000132 | heading | pages [5] -->
3.1.1 Applying POD to the dataset

<!-- b000133 | prose | pages [5] -->
For all data points corresponding to a certain time record, we call these data points a snapshot. A snapshot contains the longitude and latitude data as well as sea surface temperature of all data points at that time. We can express a snapshot in this way:

<!-- b000134 | prose | pages [5] -->
Si = [d1, d2, d3, ..., dn ] = SST (⃗x, t) [ ]⊤ D = S1,⃗S2, ...,⃗Sm

<!-- b000135 | prose | pages [5] -->
where each vector⃗Si is a snapshot which contains n data points (in this case n=17 × 40=680). It can be expressed as a term related to both location⃗x and timet. The whole dataset is a matrix which composed of m (here m = 468) row vectors (snapshots).

<!-- b000136 | prose | pages [5] -->
The goal of POD is to decompose every snapshot into the following forms:

<!-- b000137 | prose | pages [5] -->
m ∑ Si = SST (⃗x, t) = ak (t) Φk (⃗x) k=1

<!-- b000138 | prose | pages [5] -->
where each Φk (⃗x) is a POD mode that represent a certain kind of sea surface temper- ature distribution. It is only related to the location vector⃗x. The function ak (t) is the corresponding time coefﬁcient which only related to time t.

<!-- b000139 | prose | pages [5] -->
The POD solving ﬂow follows a common Principle Component Analysis (PCA) pro- cess:

<!-- b000140 | heading | pages [5] -->
1. We start by subtracting the average SST from every snapshot to obtain a new

<!-- b000141 | prose | pages [5] -->
snapshot matrix D′:

<!-- b000142 | prose | pages [5] -->
    S1 −¯S⃗ d′ d′ d′ · · ·   11 12 1n S2 −¯S   d′ d′ d′ · · · D′ = 21 22 2n = ... ... ... ... ... ...⃗ d′ d′ d′ · · · Sm −¯S mn m1 m2

<!-- b000143 | prose | pages [5] -->
m−1D′⊤D′ ( C ⊆Rn×n ), and 1

<!-- b000144 | heading | pages [5] -->
2. We then calculate the data covariance matrix C =

<!-- b000145 | prose | pages [5] -->
compute all its eigenvalues and corresponding eigenvectors. We order all n eigenvalues in a descent order and obtain an n×n matrix Φ which contains n eigenvectors as column vectors.   · · · ϕ11 ϕ21 ϕn1   · · · ϕ12 ϕ22 ϕn2 Φ = [⃗v1,⃗v2, · · · ,⃗vn] = ... ... ... ...

<!-- b000146 | prose | pages [5] -->
· · · ϕ1n ϕ2n ϕnn

<!-- b000147 | prose | pages [5, 6] -->
关注数学模型 The n eigenvectors (the n columns of Φ), which ordered from left two right according to the value of their corresponding eigenvalues, are the POD modes of the dataset. A large eigenvalue indicates that its corresponding POD mode (eigenvector) has a large kinetic energy. In this case, the ﬁrst 5 eigenvalues are listed in table 2:

<!-- b000148 | furniture | pages [5] -->
2

<!-- b000149 | furniture | pages [5] -->
MATHmodels

<!-- b000150 | furniture | pages [5] -->
获取更多资讯

<!-- b000151 | furniture | pages [6] -->
Team # 2003298

<!-- b000152 | furniture | pages [6] -->
Page 5 of 23

<!-- b000154 | caption | pages [6] -->
Table 2: Top 5 largest eigenvalues

<!-- b000155 | prose | pages [6] -->
eigenvalue Proportion of the sum of all eigenvalue

<!-- b000156 | prose | pages [6] -->
4645.04 93.96% 115.16 2.33% 52.76 1.07% 36.62 0.74% 21.79 0.44%

<!-- b000157 | prose | pages [6] -->
We can ﬁnd that the ﬁrst 3 eigenvalues account for 97% of the sum of all eigenvalue. Therefore, in the following mode decomposition process, we can discard other modes with smaller eigenvalues and only retain the ﬁrst three most important modes.

<!-- b000158 | prose | pages [6] -->
3. By projecting the original matrix D′ onto Φ, we obtain a projection matrix A = D′Φ. To decode the original matrix from A, we can compute D′ = A Φ⊤.

<!-- b000159 | prose | pages [6] -->
    a11 a1n  [ϕ11 · · · ϕ1n] + · · · +  [ϕn1 · · · ϕnn] a21 a2n D′ = AΦ⊤= ... ...

<!-- b000160 | prose | pages [6] -->
am1 amn

<!-- b000161 | prose | pages [6] -->
As we only retain the ﬁrst three most import modes, we can use an approximate representation to represent the original matrix D′:

<!-- b000162 | prose | pages [6] -->
      a11 a12 a13  [ϕ11 · · · ϕ1n]+  [ϕ21 · · · ϕ2n]+  [ϕ31 · · · ϕ3n] ≈D′ 3 ∑ a21 a22 a23 ˆD = ak⃗v⊤ k = ... ... ... k=1 am1 am2 am3

<!-- b000163 | prose | pages [6] -->
We can obtain that every eigenvector⃗vk is the spatial POD mode and every time vector⃗ak is its corresponding time coefﬁcient. This indicates that we have ﬁnished the decomposition of our original dataset D′. The three modes and their corresponding time coefﬁcients are illustrated in ﬁgure 1.

<!-- b000164 | prose | pages [6] -->
In order to verify the accuracy of our proposed prediction method, we divide our original dataset in to training set (ﬁrst 446 snapshots) and testing set (last 12 snapshots). We use the training set to retrain a new model, which is used to predict the next 12 snapshots. By comparing the real and predicted values of the last 12 snapshots, we derive the relative error of the model. Parts of the results is shown in table 3.

<!-- b000165 | prose | pages [6, 7] -->
关注数学模型 Snapshot NO. Date Relative error 447 2019.2 7.53% 448 2019.3 16.35% 449 2019.4 18.49% 450 2019.5 14.05%

<!-- b000166 | furniture | pages [6] -->
2

<!-- b000167 | furniture | pages [6] -->
MATHmodels

<!-- b000168 | furniture | pages [6] -->
获取更多资讯

<!-- b000169 | furniture | pages [7] -->
Team # 2003298

<!-- b000170 | furniture | pages [7] -->
Page 6 of 23

<!-- b000171 | caption | pages [7] -->
Figure 1: POD modes and their corresponding coefﬁcients

<!-- b000172 | caption | pages [7] -->
Table 3: Relative error of the model

<!-- b000174 | prose | pages [7] -->
We can ﬁnd that the average relative error of the real and predicted values is 13.69%, which indicates that our model has a relatively good accuracy.

<!-- b000175 | heading | pages [7] -->
3.1.2 Predicting future sea surface temperature

<!-- b000176 | prose | pages [7] -->
Since POD modes are only related to geographical features, we can assume that these features do not change signiﬁcantly over the next ﬁfty years, that is, the eigenvec- tor⃗vk does not change. Therefore, the overall prediction of sea surface temperature can be realized by predicting the subsequent changes of each time vector⃗ak. We proceed our prediction by using linear regression to obtain the overall trend and Fourier transforma- tion to approximate the periodicity characteristic of the time coefﬁcient. The prediction results are illustrated in the ﬁgure 2:

<!-- b000177 | prose | pages [7, 8] -->
关注数学模型 Therefore, by multiplying these time coefﬁcients with their corresponding eigen vector, we obtain the prediction for sea surface temperature over the next 50 years. Ex- ample prediction results are shown in ﬁgure 3.

<!-- b000178 | furniture | pages [7] -->
2

<!-- b000179 | furniture | pages [7] -->
MATHmodels

<!-- b000180 | furniture | pages [7] -->
获取更多资讯

<!-- b000181 | furniture | pages [8] -->
Team # 2003298

<!-- b000182 | furniture | pages [8] -->
Page 7 of 23

<!-- b000183 | caption | pages [8] -->
Figure 2: Predictions of three time coefﬁcients

<!-- b000185 | caption | pages [8] -->
Figure 3: SST changing trend

<!-- b000186 | heading | pages [8] -->
3.2 Prediction of future locations for herring and mackerel

<!-- b000187 | prose | pages [8] -->
We now proceed to estimate the change in locations for herring and mackerel over the next 50 years. Both herring and mackerel are highly migratory ﬁsh, and they are very sensitive to water temperature. One measurement of temperature preference is Mean Temperature of the Catch (MTC), which could be derived from bio-geographic information. According to the MTC data obtained from NOAA report, herring prefer water temperature between 5◦and 7◦, while mackerel prefer 10◦to 14◦.(Reid, 1999)

<!-- b000188 | prose | pages [8] -->
Empirically, the best time of the year to catch herring and mackerel is March and August, respectively. Thus, we simulate the respective migration path for herring and mackerel in March and August each year from 2020 to 2070. (Figure 4 and 5). The contour lines represent the possible locations of these two ﬁsh species.

<!-- b000189 | prose | pages [8, 9] -->
关注数学模型 Generally speaking, the sea surface temperature will increase over the next 50 years, resulting in population shift to cooler areas like far north and east bay area. However, we also observe minor temperature decline in certain periods of time, indicating the change in sea surface temperature is not monotonous. For example, the sea surface temperature of March 2040 is lower than that of March 2030, resulting in an temporary increase in the size of habitable area for herring.

<!-- b000190 | furniture | pages [8] -->
2

<!-- b000191 | furniture | pages [8] -->
MATHmodels

<!-- b000192 | furniture | pages [8] -->
获取更多资讯

<!-- b000193 | furniture | pages [9] -->
Team # 2003298

<!-- b000194 | furniture | pages [9] -->
Page 8 of 23

<!-- b000195 | caption | pages [9] -->
Figure 4: Possible locations for herring in March (2020-2070)

<!-- b000196 | caption | pages [9] -->
Figure 5: Possible locations for mackerel in August (2020-2070)

<!-- b000198 | heading | pages [9] -->
4 Solution to problem 2

<!-- b000199 | prose | pages [9] -->
For small ﬁshing companies, the freshness of ﬁsh catch has always been a primary concern as the ﬁshing vessels are not equipped with any on-board refrigeration. Small ﬁshing vessels usually weigh 100t or below and measures up to 20m. Given the restric- tion of size, it is difﬁcult to install on-board refrigerators such as compressor-ice makers.

<!-- b000200 | prose | pages [9, 10] -->
关注数学模型 Due to the concern that the catch may go rotten half-way, small ﬁshing vessels are not capable of long-distance traveling.

<!-- b000201 | furniture | pages [9] -->
2

<!-- b000202 | furniture | pages [9] -->
MATHmodels

<!-- b000203 | furniture | pages [9] -->
获取更多资讯

<!-- b000204 | furniture | pages [10] -->
Team # 2003298

<!-- b000205 | furniture | pages [10] -->
Page 9 of 23

<!-- b000207 | heading | pages [10] -->
4.1 Prediction of quality deterioration

<!-- b000208 | prose | pages [10] -->
To determine the expected storage time of catch, we construct a nutrient loss model (LABUZA et.al, 1978) to predict how the quality (i.e., freshness) of the catch would de- teriorate along time. The nutrient loss model is widely used in the literature of food control. The basic idea is to measure "freshness" using nutrient loss indicators, such as protein breakdown, fat spoilage, and so forth.

<!-- b000209 | heading | pages [10] -->
4.1.1 Biochemical mechanism

<!-- b000210 | prose | pages [10] -->
Before introducing the mathematical model, we shall ﬁrst explain the biochemical rationale of how food deterioration occurs. Aquatic food deterioration is mainly caused by chemical and microbiological changes. These biochemical reactions usually involves signiﬁcant nutrient loss, such as protein breakdown and fat spoilage.

<!-- b000211 | prose | pages [10] -->
Scholars have developed a wide range of indicators to measure nutrient loss. In this paper, we select two indicators, total volatile nitrogen (TVB-N) and K-value (index of the degradation of ATP), to reﬂect the freshness of food:

<!-- b000212 | prose | pages [10] -->
TVB-N TVB-N is a product of the biochemical reactions related to protein breakdown. Thus, a high content of TVB-N indicates a substantial loss in protein, which we in turn interpret as quality deterioration.

<!-- b000213 | prose | pages [10] -->
K value K value is the index of the degradation of ATP. ATP is an indispensable sub- stance to maintain life activities. Thus, a high level of ATP degradation indicates low freshness and quality deterioration.

<!-- b000214 | heading | pages [10] -->
4.1.2 Nutrient loss model

<!-- b000215 | prose | pages [10] -->
To start with, we construct a model to predict how the quality (i.e., freshness) of ﬁsh would deteriorate along time. Note that deterioration of quality could be reﬂected by either TVB-N or K value (Zhang et al., 2011). In fact, models based on these two indicators are exactly the same. To avoid redundancy, we do not differentiate the two indicators in our model construction part unless needed. For clariﬁcation, subscript T denotes TVB-N; K denotes K value; subscript A denotes either TVB-N or k value.

<!-- b000216 | prose | pages [10] -->
Following the rule of biochemical reaction gives the equation below:

<!-- b000217 | prose | pages [10] -->
{ dA dt = kA · A (1) A (0) = A0

<!-- b000218 | prose | pages [10] -->
where

<!-- b000219 | prose | pages [10] -->
• A is the level of TVB-N (mg ·100g−1) or K value (%)

<!-- b000220 | prose | pages [10, 11] -->
关注数学模型 dA • dt is accumulation of A (or nutrient loss) per day

<!-- b000221 | furniture | pages [10] -->
2

<!-- b000222 | furniture | pages [10] -->
MATHmodels

<!-- b000223 | furniture | pages [10] -->
获取更多资讯

<!-- b000224 | furniture | pages [11] -->
Team # 2003298

<!-- b000225 | furniture | pages [11] -->
Page 10 of 23

<!-- b000227 | prose | pages [11] -->
• kA is rate constant. (As we will see later, this parameter could be calculated by equation 3 at a given temperature.)

<!-- b000228 | prose | pages [11] -->
• A0 is the initial value of A. (AT0 = 10.01 mg ·100g−1, AK0 = 8.257%)

<!-- b000229 | prose | pages [11] -->
Integrating the above equation gives equation 2, which reﬂects the accumulation of A (or loss of corresponding nutrient) along time.

<!-- b000230 | prose | pages [11] -->
A = A0 · ekA·t (2)

<!-- b000231 | prose | pages [11] -->
Then we consider the rate of biochemical reaction kA. Applying the Arrhenius equa- tion gives:

<!-- b000232 | prose | pages [11] -->
kA = k0 · e−Ea (3) RT

<!-- b000233 | prose | pages [11] -->
where

<!-- b000234 | prose | pages [11] -->
• k0 is frequency factor

<!-- b000235 | prose | pages [11] -->
• Ea is activation energy (J mol−1)

<!-- b000236 | prose | pages [11] -->
• R is gas constant ( 8.3144 J (mol K)−1)

<!-- b000237 | prose | pages [11] -->
• T is the absolute temperature (K)

<!-- b000238 | prose | pages [11] -->
Equation 3 can be derived to:

<!-- b000239 | prose | pages [11] -->
lnkA = lnk0 −Ea (4) RT

<!-- b000240 | prose | pages [11] -->
revealing the linear relationship between lnkA and 1/T. We use linear regression to estimate Ea and k0 based on a set of experimental data.

<!-- b000241 | caption | pages [11] -->
Figure 6: Linear regression results

<!-- b000242 | prose | pages [11] -->
As shown in the ﬁgure, the relationship between kA and T are:

<!-- b000243 | prose | pages [11] -->
lnkT = −7038/T + 23.428

<!-- b000244 | prose | pages [11] -->
lnkK = −13203/T + 45.123

<!-- b000245 | prose | pages [11, 12] -->
关注数学模型 then, we calculate the rate constant k0 and activation energy Ea for TVB-N and K value, respectively. The results are shown in table 4.

<!-- b000246 | furniture | pages [11] -->
2

<!-- b000247 | furniture | pages [11] -->
MATHmodels

<!-- b000248 | furniture | pages [11] -->
获取更多资讯

<!-- b000249 | furniture | pages [12] -->
Team # 2003298

<!-- b000250 | furniture | pages [12] -->
Page 11 of 23

<!-- b000252 | prose | pages [12] -->
TVB-N K-value k0 1.5E+10 3.95E+19 Ea 58501.84 109748.6

<!-- b000253 | caption | pages [12] -->
Table 4: Fitted value of parameters

<!-- b000254 | prose | pages [12] -->
Given the ﬁtted value of parameters, equation 3 can be expressed as:

<!-- b000255 | prose | pages [12] -->
kT = 1.5 × 1010 e−7038 (5) T

<!-- b000256 | prose | pages [12] -->
kK = 3.95 × 1019 e−13203 (6) T

<!-- b000257 | prose | pages [12] -->
So far we have discussed how the freshness indicators change along time (equa- tion 2), and how the rate of nutrient loss is affected by temperature (equation 5 and 6). Combining the two set of equations, we can derive how the level of freshness indicators changes along time under different temperatures. (Figure)

<!-- b000258 | caption | pages [12] -->
Figure 7: Accumulation of TVB-N and K value under different temperatures, Amax is the

<!-- b000259 | prose | pages [12] -->
maximum acceptable level of the freshness indicator

<!-- b000260 | prose | pages [12] -->
This allow us to calculate the expected storage time at a given storage temperature:

<!-- b000261 | prose | pages [12] -->
tT = (ln AT max −ln AT0) (7) −7038 1.5 × 1010 e T

<!-- b000262 | prose | pages [12] -->
tK = (ln AK max −ln AK0) (8) −13203 3.95 × 1019 e T

<!-- b000263 | prose | pages [12] -->
where t is the expected storage time; A0 is initial level of the freshness indicator; Amax is the maximum acceptable level of the freshness indicator, and T is the temperature (K).The subscript T and K represents the TVB-N and K value, respectively.

<!-- b000264 | prose | pages [12] -->
Apparently, the expected storage time trot should be the lower of tT and tK:

<!-- b000265 | prose | pages [12] -->
trot = min {tT , tK}

<!-- b000266 | prose | pages [12] -->
关注数学模型

<!-- b000267 | furniture | pages [12] -->
2

<!-- b000268 | furniture | pages [12] -->
MATHmodels

<!-- b000269 | furniture | pages [12] -->
获取更多资讯

<!-- b000270 | furniture | pages [13] -->
Team # 2003298

<!-- b000271 | furniture | pages [13] -->
Page 12 of 23

<!-- b000272 | heading | pages [13] -->
4.1.3 Results and analysis

<!-- b000273 | prose | pages [13] -->
To determine the point by which the catch go rotten, we have to identify the max- imum acceptable level of the two indicators (AT max and AK max). According to na- tional food safety standards, the level of TVB-N in aquatic food should be no larger than 30mg/100g, while the upper limit of K value is 60%. Thus, we set AT max = 30 mg/100g, and AK max = 60%.

<!-- b000274 | prose | pages [13] -->
Applying equation 7 and 8, we calculate the expected storage time under different temperatures. The results are shown in table 5.

<!-- b000275 | caption | pages [13] -->
Table 5: Expected storage time at different temperatures

<!-- b000276 | prose | pages [13] -->
expected storage time (days) tT tK trot temperature 280K 6.05 15.11 6.05 285K 3.89 6.61 3.89 290K 2.54 2.97 2.54 295K 1.69 1.37 1.37 300K 1.13 0.65 0.65

<!-- b000277 | caption | pages [13] -->
Figure 8: Relation between expected storage time and temperature

<!-- b000278 | prose | pages [13] -->
As shown in ﬁgure8, the expected storage time declines drastically as storage tem- perature rises. The expected storage time under 280k is around 6 days, while the time under 300K is only around 0.65 day.

<!-- b000279 | heading | pages [13] -->
4.2 Estimation of ﬁshing range

<!-- b000280 | heading | pages [13] -->
4.2.1 Deﬁnition of useful terms

<!-- b000281 | prose | pages [13] -->
Maximum traveling distance: As we have mentioned at the beginning of this sec- tion, the maximum traveling distance of a ﬁshing vessel is restricted by its refrigeration

<!-- b000282 | prose | pages [13, 14] -->
关注数学模型 capacity. Small ﬁshing vessels are not capable of long-distance traveling because they must ensure the freshness of the catch. We assume that the maximum traveling distance is solely determined by the expected storage time of the catch.

<!-- b000283 | furniture | pages [13] -->
2

<!-- b000284 | furniture | pages [13] -->
MATHmodels

<!-- b000285 | furniture | pages [13] -->
获取更多资讯

<!-- b000286 | furniture | pages [14] -->
Team # 2003298

<!-- b000287 | furniture | pages [14] -->
Page 13 of 23

<!-- b000289 | prose | pages [14] -->
In fact, the maximum distance a vessel can travel is dependent on the ﬁshing season, as different seasons mean different storage temperatures. Empirically, the best time to catch herring and mackerel is March and August, respectively. Given the difference in storage temperatures of theses two ﬁshing seasons, the expected storage time of herring and mackerel are different as well.

<!-- b000290 | prose | pages [14] -->
Setting the storage temperature at 9◦C (282.15K) in March and 15◦C (288.15K) in August, we can get the expected storage time from equation 7 and 8. Then, we are able to calculate the maximum traveling distance (Dmax), assuming a vessel can travel 100km per day: Dmax = 5 day×100km/day=500km for herring catch and Dmax = 3 day×100km/day= 300km for mackerel catch.

<!-- b000291 | prose | pages [14] -->
Fishing range: We deﬁne ﬁshing range as a circle centered on the ﬁshing port (cur- rent operating location, 57.69◦N, −1.83◦E) with a radius of 300km or 500km (the respec- tive maximum traveling distance to catch mackerel and herring). The ﬁshing range cov- ers all the possible locations to conduct ﬁshing activities. If ﬁshing vessels travel beyond this circle, the catch will go rotten half-way before returning to the port.

<!-- b000292 | prose | pages [14] -->
Critical year: As ocean temperature rises, herring and mackerel population will migrate away from their current habitats. We deﬁne critical year as the point of time when these two populations are too far away for small ﬁshing companies to harvest. That is, the time by which the predicted locations for herring and mackerel are "tangent" to the ﬁshing range circle.

<!-- b000293 | heading | pages [14] -->
4.2.2 Results for three cases

<!-- b000294 | prose | pages [14] -->
In section 3, we predict the possible locations of mackerel and herring based on their temperature preference (MTC). However, MTC is not a deﬁnite value. According to marine scientists, the temperature preference of herring subjects to a normal distribution with mean of 6◦C, while that of mackerel subjects to a normal distribution with mean of 12◦C.

<!-- b000295 | prose | pages [14] -->
Given the uncertainty in temperature preference, the ﬁnal locations of herring and mackerel are indeﬁnite as well. We consider three different cases regarding species mi- gration, namely the best case, the worst case, and the most likely case. For each case, we simulate the migration path of the two species and identify the corresponding critical year. The results are shown in table 6 and ﬁgure 9 , 10.

<!-- b000296 | prose | pages [14] -->
First, we examine the best case regarding mackerel migration. In this case, mack- erel would prefer water temperature of around 7◦C. Thus, they will not migrate too far away as they are not sensitive to rising temperatures. As shown in ﬁgure 9 a, by 2070, the predicted location of mackerel (in red) still falls within the current ﬁshing scope (in green). The feasible ﬁshing area would be the overlapping part. Thus, under the best case, ﬁshers could still harvest mackerel operating in the current location.

<!-- b000297 | prose | pages [14] -->
Then, we consider the most likely case. That is, mackerel would prefer water tem- perature of around 6◦C, which is the mean value of the normal distribution correspond- ing to the highest probability density. In this case, the estimated critical year is around

<!-- b000298 | prose | pages [14, 15] -->
关注数学模型 2045. The distribution of mackerel population by 2045 is shown in ﬁgure 9 b.

<!-- b000299 | furniture | pages [14] -->
2

<!-- b000300 | furniture | pages [14] -->
MATHmodels

<!-- b000301 | furniture | pages [14] -->
获取更多资讯

<!-- b000302 | furniture | pages [15] -->
Team # 2003298

<!-- b000303 | furniture | pages [15] -->
Page 14 of 23

<!-- b000305 | prose | pages [15] -->
However, it is also possible that herring could only survive when the temperature is around 5◦C, corresponding to the worst case. They could be very sensitive to tem- perature change, thus they are more likely to migrate to distant area. For this case, we estimate that the critical year is around 2027. The distribution of mackerel population by 2027 is shown in ﬁgure 9 c.

<!-- b000306 | prose | pages [15] -->
Similarly, we can derive the critical years for herring. The results are shown in table 6 and ﬁgure 9.

<!-- b000307 | caption | pages [15] -->
Table 6: Critical years for mackerel and herring

<!-- b000308 | prose | pages [15] -->
species best case most likely case worst case

<!-- b000309 | prose | pages [15] -->
mackerel no critical year 2045 2027 herring 2066 2043 2033

<!-- b000310 | caption | pages [15] -->
Figure 9: Distribution of mackerel at critical years (in red) and current ﬁshing range (in

<!-- b000311 | prose | pages [15] -->
green)

<!-- b000312 | caption | pages [15] -->
Figure 10: Distribution of herring at critical years (in red) and current ﬁshing range (in

<!-- b000313 | prose | pages [15] -->
green)

<!-- b000314 | prose | pages [15] -->
关注数学模型

<!-- b000315 | furniture | pages [15] -->
2

<!-- b000316 | furniture | pages [15] -->
MATHmodels

<!-- b000317 | furniture | pages [15] -->
获取更多资讯

<!-- b000318 | furniture | pages [16] -->
Team # 2003298

<!-- b000319 | furniture | pages [16] -->
Page 15 of 23

<!-- b000320 | heading | pages [16] -->
5 Solution to problem 3

<!-- b000321 | prose | pages [16] -->
According to the results in section 4.2.2, small ﬁshing companies will not be able to catch mackerel in 2045 and herring in 2043 for most situation if they continue to operate in their current location. Therefore, small companies will need to make some changes in 2043 and 2045 to continue ﬁshing these two species.

<!-- b000322 | prose | pages [16] -->
In this section, we assess possible strategies to combat the economic challenges. Through cost-beneﬁt analysis, we seek to determine the optimal strategy that could im- prove the future business prospects of local ﬁshermen.

<!-- b000323 | heading | pages [16] -->
5.1 Relocate ﬁshing companies

<!-- b000324 | prose | pages [16] -->
One viable strategy to "keep up with" the shifting population is to relocate the ﬁsh- ing ports. At present, we set the ﬁshing port in Southern Scotland (57.69◦N, −1.83◦E). According to table 6, if the ﬁshing companies continue to operate at this location, they will loose all the revenue from mackerel by around 2045. Now we relocate the ﬁshing port to Shetland island (60.34◦N, −1.48◦E), which is closer to the predicted location of mackerel. Using the method in section 4.2.2, we estimate the critical year to be around 2058. (Figure 11 a). This means that the new ports bring an additional beneﬁt of 13 years’ revenue. However, new ports also come with great construction costs, and we need to weigh the beneﬁts against such costs.

<!-- b000325 | caption | pages [16] -->
Figure 11: Locations of relocated and current ports and distribution of mackerel in cor-

<!-- b000326 | prose | pages [16] -->
responding critical years

<!-- b000327 | prose | pages [16] -->
To evaluate the economic feasibility of this strategy, we calculate the Net Present Value (NPV) of the relocation project. NPV is deﬁned as the difference between the present value of cash inﬂow and capital invested. Given the time span of the project (13 years), we deem that NPV is the most effective indicator for evaluation as it considers the time value of moeny. Generally speaking, a project will be rejected if the NPV is negative.

<!-- b000328 | prose | pages [16, 17] -->
关注数学模型 Applying the formula of NPV, we can get the following equation:

<!-- b000329 | furniture | pages [16] -->
2

<!-- b000330 | furniture | pages [16] -->
MATHmodels

<!-- b000331 | furniture | pages [16] -->
获取更多资讯

<!-- b000332 | furniture | pages [17] -->
Team # 2003298

<!-- b000333 | furniture | pages [17] -->
Page 16 of 23

<!-- b000335 | prose | pages [17] -->
13 ∑ CFi (1 + r)i −C0 NPV = i=1

<!-- b000336 | prose | pages [17] -->
where

<!-- b000337 | prose | pages [17] -->
• i is the number of year

<!-- b000338 | prose | pages [17] -->
• CFi is the net cash inﬂow in year i. In this case, CFi is the annual revenue gener- ated from sales of mackerel.

<!-- b000339 | prose | pages [17] -->
• r is the rate of return that can be earned from alternative investments (assume 8%).

<!-- b000340 | prose | pages [17] -->
• C0 is the initial investment of the project. In this case, C0 is the cost to construct new ﬁshing ports in Shetland island.

<!-- b000341 | prose | pages [17] -->
First, we calculate NPV of the project to relocate all the ﬁshing companies. Accord- ing to a report released by Scottish Parliament, the total revenue generated by mackerel in 2018 is £169 million. Assuming this revenue ﬁgure will not change in the future, the present value of cash inﬂows sums up to £1335 million. We also obtained the cost of ﬁsh- ing port construction from World Bank. Here, we take £45 million to be the average cost of construction per ﬁshing port. There are 11 major ﬁshing ports in Scotland in total, so the total cost to relocate all the ﬁshing companies is around £495 million. Therefore, the NPV of this project is around £840 million in total and £64 million per year, indicating that the beneﬁts far outweigh the costs.

<!-- b000342 | prose | pages [17] -->
Similarly, we can analyze the NPV of the project if only a small proportion of the ﬁshing companies are relocated. In this case, the beneﬁts and costs will reduce in pro- portion, thus NPV will still be positive.

<!-- b000343 | prose | pages [17] -->
To conclude, the relocation strategy is feasible in economic terms. However, we should also account for the social impacts. For example, local ﬁshermen may lose their jobs if the companies are relocated. Such effects cannot be quantiﬁed, yet they are very important for policy making.

<!-- b000344 | heading | pages [17] -->
5.2 Change ﬁshing mode

<!-- b000345 | prose | pages [17] -->
In addition to changing the location of the port, small companies can change the current ﬁshing mode to increase the range of ﬁshing. At present, all the ﬁshing vessels ﬁsh and transport their catch back to the land. We would propose a new ﬁshing mode: some proportion of vessels ﬁsh in the ﬁshing area, we call them ﬁshing vessels; other vessels are responsible for transporting the ﬁsh caught by ﬁshing vessels back to land,; we call them shipping vessels. The ﬁshing vessels do not require land-based support, but the shipping vessels will bring supplies to them and take their ﬁsh back to the port. Some refrigerated methods needs to be adopted for the shipping vessels like carrying ice on board. This lower the storage temperature, and the range of ﬁshing can be expanded. The location of the ﬁsh is different in each year and so as the ﬁshing range, which result in different necessary storage temperature in each year.

<!-- b000346 | prose | pages [17] -->
Based on the model of relationship between storage temperature and storage time in problem 2 and the assumption that a ﬁshing boat sails at a distance of 100 km per day,

<!-- b000347 | prose | pages [17, 18] -->
关注数学模型 the relationship between the storage time and the ﬁshing distance can be developed, which could lead to the relationship between the storage temperature and the ﬁshing distance, that is, the necessary storage temperature required for a speciﬁc distance. The formula is given below:

<!-- b000348 | furniture | pages [17] -->
2

<!-- b000349 | furniture | pages [17] -->
MATHmodels

<!-- b000350 | furniture | pages [17] -->
获取更多资讯

<!-- b000351 | furniture | pages [18] -->
Team # 2003298

<!-- b000352 | furniture | pages [18] -->
Page 17 of 23

<!-- b000354 | prose | pages [18] -->
ETa TT = R [ln (ln AT −ln AT0) −ln (kT0S)]

<!-- b000355 | prose | pages [18] -->
EKa TK = R [ln (ln AK −ln AK0) −ln (kK0S)]

<!-- b000356 | prose | pages [18] -->
Tnecessary = min {TT , TK}

<!-- b000357 | prose | pages [18] -->
Since herring will leave the current ﬁshing area in 2043, the new ﬁshing mode needs to be developed from 2044 to increase the ﬁshing range. To maximize economic bene- ﬁts, we discuss the furthest ﬁshing distance, which is the distance between the furthest ﬁsh and the port. According to the model established in question 1, we get the ﬁshing distance for each year after 2043. Part of the results are shown in table below.

<!-- b000358 | prose | pages [18] -->
year Distance 2044 1047.956 2045 969.3691 2046 1027.283 2047 969.3691

<!-- b000359 | caption | pages [18] -->
Table 7: Fishing distance for each year

<!-- b000360 | prose | pages [18] -->
Based on the ﬁshing distance, we get the storage temperature required for each year. It is the same when it comes to mackerel, in which situation new ﬁshing mode should be applied and shipping vessels are needed since 2046. The Necessary storage temperature required by year is shown in ﬁgure 12.

<!-- b000361 | caption | pages [18] -->
Figure 12: Necessary storage temperature required by year

<!-- b000362 | prose | pages [18] -->
关注数学模型

<!-- b000363 | furniture | pages [18] -->
2

<!-- b000364 | furniture | pages [18] -->
MATHmodels

<!-- b000365 | furniture | pages [18] -->
获取更多资讯

<!-- b000366 | furniture | pages [19] -->
Team # 2003298

<!-- b000367 | furniture | pages [19] -->
Page 18 of 23

<!-- b000368 | heading | pages [19] -->
5.3 Establish transit stations

<!-- b000369 | prose | pages [19] -->
In addition to the options mentioned above, another feasible solution is to establish transit stations in order to solve the problem of ﬁsh preservation. Although the existing ﬁshing boats of small companies often cannot meet the preservation conditions for long- distance transportation, we can set up transit warehouses in areas close to the open sea, such as Shetland island, and ﬁrst store the ﬁsh caught in the open sea in the warehouse. Next, by leasing regular freight services, the ﬁsh from the transit station are shipped back to the Scottish islands. This approach can dramatically increase the ﬁshing range of the company without moving its location or doing complete upgrade for ﬁshing vessels.

<!-- b000370 | prose | pages [19] -->
Take the location of the company in question 2 (57.69◦N, −1.83◦3E) as an example. The company was supposed to catch mackerel only before 2045 (most likely case). By applying this solution, the company can not only continue ﬁshing for herring in the North Sea, but also continue ﬁshing mackerel in the far reaches of the north Atlantic until 2068.

<!-- b000371 | heading | pages [19] -->
6 Solution to problem 4

<!-- b000372 | prose | pages [19] -->
In the third question we assume that there is no limit to the extent that ﬁshermen can ﬁsh in the ocean. If we take into account the limits on the ﬁshing scope of the territorial waters of each country, our proposal changed accordingly.

<!-- b000373 | prose | pages [19] -->
For proposals like moving the company location or construct transit warehouses, as the Faroe Islands, which are adjacent to Shetland island, are Danish territory, the pres- ence of Danish territorial water around them will limit the ﬁshing scope of Scottish ﬁsh- ermen. Fishermen are expected to catch fewer ﬁsh each year, and the date the mackerel can no longer be caught will be brought forward. In this case, ﬁshermen are expected to incur great loss.

<!-- b000374 | prose | pages [19] -->
For proposals like changing ﬁshing mode and adding on-board refrigeration meth- ods to shipping vessels, the time of changing into new mode needed to be reconsidered for vessels in Scotland could not ﬁsh in the territory of Danish. Based on our model in problem 1 and problem 2, all the herring would enter the territory of Danish in 2035. Therefore, the time of transforming into new ﬁshing mode needed to happen in 2036 rather than 2045. The ﬁshing area also need to be changed from east of Scotland to north of Scotland, resulting in the change of ﬁshing distance and the required storage temper- ature.

<!-- b000375 | caption | pages [19] -->
Figure 13: Source:https://www.ﬁs.com

<!-- b000376 | prose | pages [19] -->
关注数学模型

<!-- b000377 | furniture | pages [19] -->
2

<!-- b000378 | furniture | pages [19] -->
MATHmodels

<!-- b000379 | furniture | pages [19] -->
获取更多资讯

<!-- b000380 | furniture | pages [20] -->
Team # 2003298

<!-- b000381 | furniture | pages [20] -->
Page 19 of 23

<!-- b000382 | heading | pages [20] -->
7 Sensitivity Analysis

<!-- b000383 | prose | pages [20] -->
Since differential equation is used in problem 2 to build our storage model solving the relationship between storage temperature and storage time, sensitivity analysis is needed to perform on this model. We perturb the initial value of the equation in the extent of 0.2%, 2%, or 10% to observe whether the result will change drastically. By solving 6 sets of differential equations, we compare the model with the original one and observe the effect of the initial value changes on the result.

<!-- b000384 | prose | pages [20] -->
Through analysis, it is found that when the initial value is increased or decreased by 0.2%, and in the range of 250K to 300K, the results are almost identical to the results by the original model, with no obvious difference, and the relative errors are around 0%. The results show that minimal perturbations to the initial value will not affect the model. When the initial value is increased or decreased by 2%, there is a slight difference between 250K and 280K while no signiﬁcant difference between 280K and 300K. The rel- ative error is about 2% between 250K and 292K, which decreases to 1% when storage temperature rise to 292K to 300K. The results show that a small range of perturbations to the initial value have only a small impact on the model, or even no signiﬁcant impact. When the initial value is increased or decreased by 10%, there is a certain difference from the original model when the storage temperature is between 250K and 280K, while there is no signiﬁcant difference from the original model when storage temperature is between 280K and 300K. In former situation, the relative errors between the initial value increase of 10% and the decrease of 10% are 8.7% and 9.5%, respectively. From 290K to 292K, the relative error dropped from 8.7% and 9.5% to 4.8% and 5.3%, respectively, and main- tained the relative error to 300K. The results show that a certain degree of perturbation to the initial value does not cause a large deviation in the model. On the contrary, the relative error can be controlled in a small range, and the relative error decreases with the increase of temperature.

<!-- b000385 | caption | pages [20] -->
Figure 14: Results of sensitivity analysis

<!-- b000386 | prose | pages [20] -->
The analysis shows that our model is quite robust, which will not change greatly due to the perturbation of the initial value. The result of sensitive analysis has practical signiﬁcance. The initial value of the differential equation represents the initial TVB-N content and K-value in the ﬁsh, that is, the natural state of the ﬁsh. Since the initial value selected by the model in problem 2 was obtained from a certain article, where the re- searchers measured a certain ﬁsh. Although the ﬁsh measured in the article can reﬂect

<!-- b000387 | prose | pages [20, 21] -->
关注数学模型 the general values of this species, there are still individual differences between individu- als within the species due to factors such as size, diet, and living environment. However, sensitivity analysis showed that the storage model are basically the same when applied to ﬁsh with different content of TVB-N and K-value, which means that we can ignore the effect of the difference of the content of the two substances in the ﬁsh. The model is universal to all ﬁsh in certain species, and the assumption that the two substances are the same in the natural state of the ﬁsh is reasonable.

<!-- b000388 | furniture | pages [20] -->
2

<!-- b000389 | furniture | pages [20] -->
MATHmodels

<!-- b000390 | furniture | pages [20] -->
获取更多资讯

<!-- b000391 | furniture | pages [21] -->
Team # 2003298

<!-- b000392 | furniture | pages [21] -->
Page 20 of 23

<!-- b000394 | heading | pages [21] -->
8 Strengths and weaknesses

<!-- b000395 | heading | pages [21] -->
Strengths

<!-- b000396 | prose | pages [21] -->
• We predict the ocean surface temperature from a holistic perspective, effectively excluding the inﬂuence of outliers, and reasonably predicted the ocean surface temperature changes.

<!-- b000397 | prose | pages [21] -->
• The original data is conditionality reduced by POD method, which simpliﬁes the complexity of the model while retaining most of the effective information.

<!-- b000398 | prose | pages [21] -->
• We use NPV to evaluate the economic feasibility of different strategies. We deem this is a highly effective indicator as it takes the time value of money into account.

<!-- b000399 | heading | pages [21] -->
Weakness

<!-- b000400 | prose | pages [21] -->
• As our data is not sufﬁcient enough, there may be some errors in long-term forecast of sea surface temperatures.

<!-- b000401 | prose | pages [21] -->
• In evaluating the freshness of ﬁsh catch, we only consider two indicators (level of TVB-N and K value). In fact, there are many indicators to measure nutrient loss.

<!-- b000402 | prose | pages [21] -->
Other indicators may give different storage time.

<!-- b000403 | prose | pages [21] -->
关注数学模型

<!-- b000404 | furniture | pages [21] -->
2

<!-- b000405 | furniture | pages [21] -->
MATHmodels

<!-- b000406 | furniture | pages [21] -->
获取更多资讯

<!-- b000407 | furniture | pages [22] -->
Team # 2003298

<!-- b000408 | furniture | pages [22] -->
Page 21 of 23

<!-- b000409 | heading | pages [22] -->
9 Article for Hook Line and Sinker

<!-- b000410 | prose | pages [22] -->
Global warming could mean fewer ﬁsh for Scottish ﬁshermen

<!-- b000411 | prose | pages [22] -->
The effects of human activity on the earth’s climate are intensifying. The burning of large quantities of fossil fuels produces greenhouse gases that wrap the earth in a thermal mantle, gradually warming the earth’s surface. Over the past few decades, we have seen the environmental impacts of global warming: the redistribution of global rainfall, the melting of glaciers and permafrost, the rising of sea levels, and so on. These changes endanger the balance of natural ecosystems and change the habitats of animals.

<!-- b000412 | prose | pages [22] -->
According to marine scientists, due to the rising ocean temperature, lobsters that originally live in Maine, USA are moving slowly northward to Canada. This phenomenon caught our attention. We are aware that this geographic population shift may have a dramatic impact on ﬁshing companies, especially those small and medium-sized ones. Fishing companies may be forced to go further aﬁeld to keep up with the migrating pop- ulation, which would require greater investment in labor and capital. Thus, the ﬁshing industry will be confronted with severe economic challenges.

<!-- b000413 | prose | pages [22] -->
To gain an in-depth understanding of this problem, we use a reduced order model to predict the changes in sea temperature. According to our prediction, the average temperature of seawater near Scotland will rise by 3 degrees Celsius over the next 50 years. The rise in ocean temperature could result in a signiﬁcant shift of herring and mackerel population. To be speciﬁc, in the Atlantic Ocean north-west to Scotland, the ﬁsh species will move northward away from the British Isles. And in the North Sea, these species will gradually move east into territorial waters of other countries along the east coast of the North Sea, which makes them unavailable for Scotland ﬁshermen. This is no good news for the Scottish ﬁshermen: they will have to go further into the ocean to catch herring and mackerel, which means increasing costs and decreasing revenue.

<!-- b000414 | prose | pages [22] -->
The good news, according to our ﬁndings, is that the distribution of herring and mackerel will not change too much over the next 5 to 10 years. This allows Scottish ﬁshermen to plan ahead and get themselves prepared for future changes. We assessed several ﬁshing strategies that may help to improve the future business prospect. Accord- ing to our results, we would recommend small ﬁshing companies to relocate the ﬁshing ports to somewhere closer to the predicted location of herring and mackerel (e.g., Shet- land island). We also recommend these companies to upgrade their vessels or install on-board refrigeration system, which will allows them to ﬁsh in a broader range. Last but not least, ﬁshing companies could consider building warehouses in high sea areas like Shetland Islands to obtain more catch.

<!-- b000415 | prose | pages [22] -->
关注数学模型

<!-- b000416 | furniture | pages [22] -->
2

<!-- b000417 | furniture | pages [22] -->
MATHmodels

<!-- b000418 | furniture | pages [22] -->
获取更多资讯

<!-- b000419 | furniture | pages [23] -->
Team # 2003298

<!-- b000420 | furniture | pages [23] -->
Page 22 of 23

<!-- b000421 | heading | pages [23] -->
References

<!-- b000422 | references | pages [23] -->
[1] Reid, R. (1999). Essential ﬁsh habitat source document. Woods Hole, Mass.: U.S.

<!-- b000423 | references | pages [23] -->
Dept. of Commerce, National Oceanic and Atmospheric Administration, National

<!-- b000424 | references | pages [23] -->
Marine Fisheries Service, Northeast Region, Northeast Fisheries Science Center.

<!-- b000425 | references | pages [23] -->
[2] Noori, R., Abbasi, M., Adamowski, J. and Dehghani, M. (2017). A simple mathe-

<!-- b000426 | references | pages [23] -->
matical model to predict sea surface temperature over the northwest Indian Ocean.

<!-- b000427 | references | pages [23] -->
Estuarine, Coastal and Shelf Science, 197, pp.236-243.

<!-- b000428 | references | pages [23] -->
[3] LABUZA, T., SHAPERO, M. and KAMMAN, J. (1978). PREDICTION OF NUTRI-

<!-- b000429 | references | pages [23] -->
ENT LOSSES. Journal of Food Processing and Preservation, 2(2), pp.91-99.

<!-- b000430 | references | pages [23] -->
[4] Zhang, L., Li, X., Lu, W., Shen, H. and Luo, Y. (2011). Quality predictive models

<!-- b000431 | references | pages [23] -->
of grass carp (Ctenopharyngodon idellus) at different temperatures during storage.

<!-- b000432 | references | pages [23] -->
Food Control, 22(8), pp.1197-1202.

<!-- b000433 | references | pages [23] -->
[5] World

<!-- b000434 | references | pages [23] -->
Bank.

<!-- b000435 | references | pages [23] -->
(2020).

<!-- b000436 | references | pages [23] -->
Fishing

<!-- b000437 | references | pages [23] -->
Port

<!-- b000438 | references | pages [23] -->
Project.

<!-- b000439 | references | pages [23] -->
[online]

<!-- b000440 | references | pages [23] -->
Available

<!-- b000441 | references | pages [23] -->
at:

<!-- b000442 | references | pages [23] -->
https://projects.worldbank.org/en/projects-operations/project-

<!-- b000443 | references | pages [23] -->
detail/P007801

<!-- b000444 | references | pages [23] -->
[Accessed

<!-- b000445 | references | pages [23] -->
17

<!-- b000446 | references | pages [23] -->
Feb.

<!-- b000447 | references | pages [23] -->
2020].

<!-- b000448 | references | pages [23] -->
https://sp-bpr-en-prod-

<!-- b000449 | references | pages [23] -->
cdnep.azureedge.net/published/2018/4/25/Mackerel/SB%2018-30.pdf

<!-- b000450 | references | pages [23] -->
[6] Esrl.noaa.gov.

<!-- b000451 | references | pages [23] -->
(2020).

<!-- b000452 | references | pages [23] -->
ESRL

<!-- b000453 | references | pages [23] -->
:

<!-- b000454 | references | pages [23] -->
PSD

<!-- b000455 | references | pages [23] -->
:

<!-- b000456 | references | pages [23] -->
NOAA

<!-- b000457 | references | pages [23] -->
Optimum

<!-- b000458 | references | pages [23] -->
Interpola-

<!-- b000459 | references | pages [23] -->
tion

<!-- b000460 | references | pages [23] -->
(OI)

<!-- b000461 | references | pages [23] -->
Sea

<!-- b000462 | references | pages [23] -->
Surface

<!-- b000463 | references | pages [23] -->
Temperature

<!-- b000464 | references | pages [23] -->
(SST)

<!-- b000465 | references | pages [23] -->
V2.

<!-- b000466 | references | pages [23] -->
[online]

<!-- b000467 | references | pages [23] -->
Available

<!-- b000468 | references | pages [23] -->
at:

<!-- b000469 | references | pages [23] -->
https://www.esrl.noaa.gov/psd/data/gridded/data.noaa.oisst.v2.html

<!-- b000470 | references | pages [23] -->
[Ac-

<!-- b000471 | references | pages [23] -->
cessed 17 Feb. 2020].

<!-- b000472 | references | pages [23] -->
[7] Davies,

<!-- b000473 | references | pages [23] -->
D. (2020). Mackerel. [online] Available at:

<!-- b000474 | references | pages [23] -->
https://sp-bpr-en-prod-

<!-- b000475 | references | pages [23] -->
cdnep.azureedge.net/published/2018/4/25/Mackerel/SB%2018-30.pdf [Accessed

<!-- b000476 | references | pages [23] -->
17 Feb. 2020].

<!-- b000477 | references | pages [23] -->
关注数学模型

<!-- b000478 | furniture | pages [23] -->
2

<!-- b000479 | furniture | pages [23] -->
MATHmodels

<!-- b000480 | furniture | pages [23] -->
获取更多资讯

<!-- b000481 | heading | pages [24] -->
Appendix

<!-- b000482 | prose | pages [24] -->
Snapshot NO. Date Relative error 447 2019.2 7.53% 448 2019.3 16.35% 449 2019.4 18.49% 450 2019.5 14.05% 451 2019.6 11.44% 452 2019.7 10.12% 453 2019.8 8.35% 454 2019.9 4.85% 455 2019.10 12.33% 456 2019.11 20.58% 457 2019.12 23.21% 458 2020.1 17.04% Average relative error 13.69% Table: Relative error of 12 testing snapshots

<!-- b000483 | prose | pages [24] -->
关注数学模型

<!-- b000484 | furniture | pages [24] -->
2

<!-- b000485 | furniture | pages [24] -->
MATHmodels

<!-- b000486 | furniture | pages [24] -->
获取更多资讯
