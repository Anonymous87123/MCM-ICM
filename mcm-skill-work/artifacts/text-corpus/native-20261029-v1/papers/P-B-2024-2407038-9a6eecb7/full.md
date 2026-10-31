# P-B-2024-2407038-9a6eecb7

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | furniture | pages [1] -->
2024

<!-- b000003 | prose | pages [1] -->
Problem Chosen

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | furniture | pages [1] -->
2407038

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Unlocking the Abyss: A Dynamical Model for Deep-Sea Adventure

<!-- b000009 | title | pages [1] -->
Safety and Rescue Strategies

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | prose | pages [1] -->
In the ever-growing realm of adventure tourism, the exploration of sunken shipwrecks by riding submersibles has emerged as an exciting experience and popular activity, which allows enthusiasts to witness the silent beauty of maritime history beneath the waves. However, due to the complexity of the ocean current and weak communication underwater, the event that a submersible loses contact with the host ship under the sea continues, and positioning the missing submarine and carrying out rescue will be difficult. Predicting the trajectory of the submarine and developing the best search strategy are problems faced by both marine administrators and mathematicians. In order to handle this challenge, we divide the problem into three key points and establish three models separately.

<!-- b000012 | prose | pages [1] -->
Model I: Based on the knowledge of the underwater environment, the current effect, seawater density, and seafloor topography are three main points influencing submersible movement. We first utilize the

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
Autoregressive Integrated Moving Average (ARIMA) Time Series Model and ridge regression to fit the three-dimensional continuous current and seawater density distribution. According to the dynamics function of the submersible considering complex factors, we build a model to solve these equations and predict the trajectory of the missing submersible.

<!-- b000015 | prose | pages [1] -->
The prediction results are shown in Figure 6. Furthermore, we analyze the uncertainty of the current. After randomly input time series, it has an average uncertainty of 2.39%.

<!-- b000016 | prose | pages [1] -->
Model II: During the preparation stage, necessary search equipment for rescue must be deployed on the host ship and rescue vessel. There are different indicators of various types of search equipment including: equipment cost, maintenance cost, availability, usage, and readiness, which are firstly averagely processed and quantified. Our model uses the objective functions of minimum total cost, availability, and preparation time. Then, a Muti-Objective Optimization is established based on a Genetic Algorithm to obtain the Pareto set of solutions for the host ship and rescue vessel, respectively. Then, we choose three optimal results as different equipment allocations for the host ship and rescue vessel. The final results are shown in Table 8.

<!-- b000017 | prose | pages [1] -->
Model III: To decide the search strategy, we rasterize the region into grids and estimate the dynamic probability distribution based on our prediction results and the Poisson distribution function. Inspired by Bayes’s theorem, we adjust the probability distribution according to the information obtained from the previous search. Ultimately, we divide the search into many time intervals and accumulate the probability of finding the submersible. The results of the accumulated probability are shown in Figure 10.

<!-- b000018 | prose | pages [1] -->
Additionally, we test the scalability and sensitivity of this model. Applying the model to another tourist destination, the Caribbean Sea, the trajectory corresponds to the current trend in that sea area, which means it has a fine scalability. Then, we change the time interval value in our model to test its sensitivity. After calculation, the final probability change rate is less than 5.8% if the time interval change rate is less than 10%. The results show that our model is not sensitive to changes in time intervals. Finally, we formulate a memo to the Greek government to obtain official approval.

<!-- b000019 | heading | pages [1] -->
Keywords: Submersible Trajectory; Dynamical Analysis; Grid Analysis; Bayes Theorem; Sensitivity

<!-- b000020 | prose | pages [1] -->
Analysis

<!-- b000021 | furniture | pages [1] -->
关注数学模型

<!-- b000022 | furniture | pages [1] -->
2

<!-- b000023 | furniture | pages [1] -->
MATHmodels

<!-- b000024 | furniture | pages [1] -->
获取更多资讯

<!-- b000025 | furniture | pages [2] -->
Team #2407038

<!-- b000026 | furniture | pages [2] -->
Page 1

<!-- b000027 | heading | pages [2] -->
Contents

<!-- b000028 | contents | pages [2] -->
1

<!-- b000029 | heading | pages [2] -->
Introduction

<!-- b000030 | prose | pages [2] -->
2 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2

<!-- b000031 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000032 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 2 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000033 | prose | pages [2] -->
2

<!-- b000034 | heading | pages [2] -->
Assumptions

<!-- b000035 | prose | pages [2] -->
3

<!-- b000036 | heading | pages [2] -->
Notations

<!-- b000037 | prose | pages [2] -->
4

<!-- b000038 | heading | pages [2] -->
Model Preparation

<!-- b000039 | prose | pages [2] -->
3

<!-- b000040 | prose | pages [2] -->
4

<!-- b000041 | prose | pages [2] -->
4

<!-- b000042 | prose | pages [2] -->
5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Data Overview 5 Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 Data Preparation 5

<!-- b000043 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000044 | prose | pages [2] -->
Data Extraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.1 5 Conversion from longitude and latitude to distance . . . . . . . . . . . . . . . . . 4.3.2 5

<!-- b000045 | heading | pages [2] -->
Trajectory Prediction Model Based on Dynamics Analysis

<!-- b000046 | prose | pages [2] -->
5 6 Advanced Time Series Analysis: Delving Deep into Ocean Current Speed Data . . . . . . 5.1 6 Continuous Current Speed Distribution Regression Model 5.2 . . . . . . . . . . . . . . . . .

<!-- b000047 | prose | pages [2] -->
8 Dynamical Model based on Newtonian mechanics . . . . . . . . . . . . . . . . . . . . . . 5.3 9 Discussion on Key Equipment and Technologies . . . . . . . . . . . . . . . . . . . . . . . 5.4 10

<!-- b000048 | heading | pages [2] -->
Comprehensive Equipment Allocation Optimization Model

<!-- b000049 | prose | pages [2] -->
6 11 Preliminary Research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 11 Model Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 12 Parameter Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.1 12 Data Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.2 13 Objective Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.3 13 Genetic Algorithm for Multi-objective Optimization . . . . . . . . . . . . . . . . . . . . . 6.3 14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.4 Results and Analysis 14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.5

<!-- b000050 | heading | pages [2] -->
Conclusion

<!-- b000051 | prose | pages [2] -->
15

<!-- b000052 | prose | pages [2] -->
Grid Probability Search Technique based on Poisson Distribution 7 15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 Regional Rasterization 15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Poisson Probability Distribution 16 Probability Calculation Based on Bayesian Theory 7.3 . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | prose | pages [2] -->
17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.4 Results and Analysis

<!-- b000054 | prose | pages [2] -->
8

<!-- b000055 | heading | pages [2] -->
Expansion of the Model

<!-- b000056 | prose | pages [2] -->
19

<!-- b000057 | prose | pages [2] -->
19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 Model Applied in Different Areas 19 Rescue of Multiple Submersibles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000058 | prose | pages [2] -->
9

<!-- b000059 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000060 | prose | pages [2] -->
20

<!-- b000061 | prose | pages [2] -->
21

<!-- b000062 | furniture | pages [2] -->
关注数学模型

<!-- b000063 | furniture | pages [2] -->
2

<!-- b000064 | furniture | pages [2] -->
MATHmodels

<!-- b000065 | furniture | pages [2] -->
获取更多资讯

<!-- b000066 | furniture | pages [3] -->
Team #2407038

<!-- b000067 | prose | pages [3] -->
1

<!-- b000068 | heading | pages [3] -->
Introduction

<!-- b000069 | prose | pages [3] -->
1.1 Problem Background

<!-- b000070 | furniture | pages [3] -->
Page 2

<!-- b000071 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000072 | prose | pages [3] -->
There have been 38 accidents involving submarines and submersibles since 2000, and one of them was the “Titan implosion” last year [1]. Once an incident in deep water happens, an urgent international search and rescue operation is about to begin. Greece-based company Maritime Cruises Mini-Submarines (MCMS) manufactures submersibles for deep-sea explorations and wishes to provide tourists with the chance to adventure the depths of the Ionian Sea and explore sunken shipwrecks. However, it is vital to have safety procedures to cope with the possible risks underwater. Consequently, we are asked by MCMS to design a four-step procedure for them.

<!-- b000073 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000074 | prose | pages [3] -->
To ensure security on board, a four-step safety procedure is modeled, including Locate, Prepare, Search, and Extrapolate. After thorough background reading, each procedure can be formulated into a sub-problem

<!-- b000075 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000076 | prose | pages [3] -->
as follows: • LOCATE:

<!-- b000077 | prose | pages [3] -->
Develop a predictive model for the submersible’s location over time. Identify uncertainties in pre- dictions. Determine data the submersible can transmit to the host ship to reduce uncertainties. Specify required equipment on the submersible for data transmission. • PREPARE:

<!-- b000078 | prose | pages [3] -->
Recommend additional search equipment for the host ship, considering cost, availability, maintenance, Also, outline the additional equipment a rescue vessel might need for readiness, and usage factors. assistance. • SEARCH:

<!-- b000079 | prose | pages [3] -->
Create a model integrating location predictions to suggest optimal deployment points and search patterns for search equipment, minimizing the time to locate a lost submersible. Calculate the probability of finding the submersible based on time and accumulated search results. • EXTRAPOLATE:

<!-- b000080 | prose | pages [3] -->
To adapt the model for other tourist destinations like the Caribbean Sea, integrate region-specific data such as currents, weather patterns, and underwater topography. For multiple submersibles in the same vicinity, incorporate individual identifiers and update the prediction algorithm to manage simultaneous movements.

<!-- b000081 | prose | pages [3] -->
1.3 Literature Review

<!-- b000082 | prose | pages [3] -->
The task consists of two main models to be constructed: the prediction model of the submersible path and the search methodology of the rescue vessel. According to existing studies, predicting the submersible tracks has two main methods: Neural Network Predictions [2] and Computational Dynamics Simulations [3]. The neural Network-based Method uses a neural network (LSTM) to capture the disturbance like effects of currents or geography, which has remarkable accuracy with the proper network. At the same time, the computational and time costs are unavoidable. Computational Dynamics Simulations start from essential physics and kinetics models, and the simulation runs simultaneously with happening situations. Its accuracy relies heavily on the dynamical models and the formal information.

<!-- b000083 | furniture | pages [3] -->
关注数学模型

<!-- b000084 | furniture | pages [3] -->
2

<!-- b000085 | furniture | pages [3] -->
MATHmodels

<!-- b000086 | furniture | pages [3] -->
获取更多资讯

<!-- b000087 | furniture | pages [4] -->
Team #2407038

<!-- b000088 | furniture | pages [4] -->
Page 3

<!-- b000089 | prose | pages [4] -->
The underwater target search methods mainly include random search, geometry search, and heuristic search. This task requires searching by probability based on the existing results and time, a heuristic search method using prior knowledge of the target. Based on our findings, a few studies use mathematical models to tackle this issue: Limited studies have addressed this issue with mathematical models. Yao et

<!-- b000090 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000091 | prose | pages [4] -->
al. applied expectation-maximization (EM) for static target search, but it is unsuitable for moving targets [4]. In [5], Juan, Li et al. use the RRT algorithm and neural network to improve the exploration capability in multiple-target search in a changing environment, but the search efficiency is relatively low.

<!-- b000092 | prose | pages [4] -->
1.4 Our Work

<!-- b000093 | prose | pages [4] -->
The task involves establishing a four-step procedure to ensure the safety of deep-sea exploration, which mainly includes:

<!-- b000094 | prose | pages [4] -->
1. Based on the currents, seawater density, and seafloor geography of the Ionian Sea, a Trajectory Prediction Model based on dynamics analysis is established.

<!-- b000095 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000096 | prose | pages [4] -->
2. Multi-Objective Optimization evaluates the rescue search equipment and then decides whether to be installed on the host ship and rescue vessels.

<!-- b000097 | prose | pages [4] -->
3. Based on the location obtained from the Trajectory Prediction Model, we rasterize the search area and construct the probability model from the search results and time.

<!-- b000098 | prose | pages [4] -->
4. Extrapolation of the model tests the transferability of situations like different oceans and multiple submersibles lost.

<!-- b000099 | prose | pages [4] -->
In order to avoid complex descriptions and intuitively reflect our workflow, the flowchart is shown in

<!-- b000100 | caption | pages [4] -->
Figure 1.

<!-- b000101 | caption | pages [4] -->
Figure 1: Work Flow

<!-- b000102 | furniture | pages [4] -->
关注数学模型

<!-- b000103 | furniture | pages [4] -->
2

<!-- b000104 | furniture | pages [4] -->
MATHmodels

<!-- b000105 | furniture | pages [4] -->
获取更多资讯

<!-- b000106 | furniture | pages [5] -->
Team #2407038

<!-- b000107 | prose | pages [5] -->
2

<!-- b000108 | heading | pages [5] -->
Assumptions

<!-- b000109 | furniture | pages [5] -->
Page 4

<!-- b000110 | prose | pages [5] -->
Before establishing a mathematical model for the motion trajectory of a defective submersible under the sea, we make some assumptions to make the model easier to realize.

<!-- b000111 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000112 | prose | pages [5] -->
• Assumption 1: The changes in ocean currents are periodic.

<!-- b000113 | prose | pages [5] -->
Explanation: The periodic changes in ocean currents result from the combined effects of various complex factors, including but not limited to wind, Earth’s rotation, and solar radiation.

<!-- b000114 | prose | pages [5] -->
• Assumption 2: The submersible’s weight and volume do not change after it loses contact with the host ship. The size of the submersible is supposed to be 670 cm × 280 cm × 250 cm

<!-- b000115 | prose | pages [5] -->
Explanation: A submersible’s weight and volume will decide its gravity and buoyancy and further influence the trajectory underwater. To simplify the model, we ignore the changes in these factors for a defective submersible.

<!-- b000116 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000117 | prose | pages [5] -->
• Assumption 3: When a submersible breaks down and loses contact with the host ship, it will lose the ability to provide propulsion and change its volume simultaneously.

<!-- b000118 | prose | pages [5] -->
Explanation: If the submersible still has propulsion, the operation of the driver after contact loss will be unpredictable, which means the later position of the submersible will be unpredictable. Additionally, if the submersible can still reach the water’s surface with its propulsion, discussing how to predict the motion and carry out the rescue underwater is meaningless.

<!-- b000119 | prose | pages [5] -->
• Assumption 4: When a submersible breaks down and loses contact with the host ship, it is always positioned on the sea floor or at some point of neutral buoyancy underwater.

<!-- b000120 | prose | pages [5] -->
Explanation: Since the purpose of a submersible is to allow tourists to visit underwater landscapes and search for underwater boats, it will be suspended at some position under the sea or just stop on the seabed. Then, we can suppose that the submersible is still when accidents happen.

<!-- b000121 | prose | pages [5] -->
• Assumption 5: When a rescue vessel searches for the missing submersible, it can detect submersible as long as they are in the same latitude and longitude coordinates.

<!-- b000122 | prose | pages [5] -->
Explanation: Due to the complex environment and terrain, the rescue vessel may miss the submersible even though they are close enough. The missing probability is low and unpredicted, so we view it as 0, which means the rescue vessel can find the target under the water.

<!-- b000123 | prose | pages [5] -->
3

<!-- b000124 | heading | pages [5] -->
Notations

<!-- b000125 | caption | pages [5] -->
Table 1: Notations Used in this Paper

<!-- b000126 | prose | pages [5] -->
Symbol Definition ˆ𝑌𝑡 Symbol Definition 𝑓𝐶(𝑥) Predicted ocean current velocity vector 𝑅𝑡 Residual sequence 𝐽(𝜃) Ridge regression function 𝑀𝑆𝐸(𝜃) Mean square error 𝐸𝐶 Environmental coefficient Cost objection function 𝐺𝑠 Grid size 𝑣 Velocity 𝑃(𝜒= 𝑘) The Poisson distribution 𝑝(𝐴) Probability of event A

<!-- b000127 | furniture | pages [5] -->
关注数学模型

<!-- b000128 | furniture | pages [5] -->
2

<!-- b000129 | furniture | pages [5] -->
MATHmodels

<!-- b000130 | furniture | pages [5] -->
获取更多资讯

<!-- b000131 | furniture | pages [6] -->
Team #2407038

<!-- b000132 | prose | pages [6] -->
4

<!-- b000133 | heading | pages [6] -->
Model Preparation

<!-- b000134 | prose | pages [6] -->
4.1 Data Overview

<!-- b000135 | furniture | pages [6] -->
Page 5

<!-- b000136 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000137 | prose | pages [6] -->
The material does not provide direct data about the Ionian Sea we will research, so we collect some important data about this region. According to our model, we collect the data about current velocity distribution and seawater density distribution of the Ionian Sea. Owing to the large amount of data, we choose to visualize the data for display instead of listing all of them.

<!-- b000138 | prose | pages [6] -->
4.2

<!-- b000139 | heading | pages [6] -->
Data Collection

<!-- b000140 | caption | pages [6] -->
Table 2: Data and Database Websites

<!-- b000141 | prose | pages [6] -->
Database Names Database Websites

<!-- b000142 | prose | pages [6] -->
https://data.marine.copernicus.eu/product/ Current https://www.ncei.noaa.gov/maps/grid-extract/ Density

<!-- b000143 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000144 | prose | pages [6] -->
Geography of Seafloor

<!-- b000145 | prose | pages [6] -->
4.3

<!-- b000146 | heading | pages [6] -->
Data Preparation

<!-- b000147 | prose | pages [6] -->
4.3.1 Data Extraction

<!-- b000148 | prose | pages [6] -->
https://download.gebco.net/

<!-- b000149 | prose | pages [6] -->
Considering the dataset used is a seven-dimensional dataset [1095 49 52 76 1 1 1 ], with dimensions corresponding to time, depth, longitude, latitude, east-west direction speed, north-south direction speed, and vertical speed, respectively. The initial step involves flattening the data and transforming it into a one-dimensional vector indexed by time. Fixing the parameters of depth, longitude, and latitude allows obtaining a vector of ocean current speeds at a specific depth and location, indexed by time. Typically, example data at 222.4752𝑚deep, 37.083332◦Latitude, 20.166677◦Longitude is shown in Figure 2.

<!-- b000150 | prose | pages [6] -->
Full Data from CMEMS for East-West Current Velocity

<!-- b000151 | prose | pages [6] -->
Full Data from CMEMS for North-South Current Velocity

<!-- b000152 | prose | pages [6] -->
0.4

<!-- b000153 | prose | pages [6] -->
0.4

<!-- b000154 | prose | pages [6] -->
0.3

<!-- b000155 | prose | pages [6] -->
0.3

<!-- b000156 | prose | pages [6] -->
0.2

<!-- b000157 | prose | pages [6] -->
0.2

<!-- b000158 | prose | pages [6] -->
0.1

<!-- b000159 | prose | pages [6] -->
Velocity (m/s)

<!-- b000160 | prose | pages [6] -->
Velocity (m/s)

<!-- b000161 | prose | pages [6] -->
0.1

<!-- b000162 | prose | pages [6] -->
0

<!-- b000163 | prose | pages [6] -->
-0.1

<!-- b000164 | prose | pages [6] -->
0

<!-- b000165 | prose | pages [6] -->
-0.2

<!-- b000166 | prose | pages [6] -->
-0.1

<!-- b000167 | prose | pages [6] -->
-0.3

<!-- b000168 | prose | pages [6] -->
-0.2

<!-- b000169 | prose | pages [6] -->
-0.4

<!-- b000170 | prose | pages [6] -->
-0.3

<!-- b000171 | prose | pages [6] -->
-0.5

<!-- b000172 | prose | pages [6] -->
0 200 400 600 800 1000 1200

<!-- b000173 | prose | pages [6] -->
0 200 400

<!-- b000174 | prose | pages [6] -->
Time (Day)

<!-- b000175 | prose | pages [6] -->
Full Data from CMEMS for Vertical Current Velocity 10-4

<!-- b000176 | prose | pages [6] -->
8

<!-- b000177 | prose | pages [6] -->
6

<!-- b000178 | prose | pages [6] -->
4

<!-- b000179 | prose | pages [6] -->
Velocity (m/s)

<!-- b000180 | prose | pages [6] -->
2

<!-- b000181 | prose | pages [6] -->
0

<!-- b000182 | prose | pages [6] -->
-2

<!-- b000183 | prose | pages [6] -->
-4

<!-- b000184 | prose | pages [6] -->
-6

<!-- b000185 | prose | pages [6] -->
-8

<!-- b000186 | prose | pages [6] -->
600 600 800 1000 1200

<!-- b000187 | prose | pages [6] -->
0 200 400 600 800 1000 1200

<!-- b000188 | prose | pages [6] -->
Time (Day)

<!-- b000189 | prose | pages [6] -->
Time (Day)

<!-- b000190 | prose | pages [6] -->
(b) East-West Current Velocity

<!-- b000191 | prose | pages [6] -->
(a) North-South Current Velocity

<!-- b000192 | prose | pages [6] -->
(c) Vertical Current Velocity

<!-- b000193 | caption | pages [6] -->
Figure 2: Extracted Full Data From CMEMS

<!-- b000194 | prose | pages [6] -->
Conversion from longitude and latitude to distance 4.3.2

<!-- b000195 | prose | pages [6] -->
The data we collect all utilizes longitude and latitude as the coordinates to describe the distribution of the current velocity and seawater density. While we will use the mechanical model to predict the submersible’s motion, the parameters’ dimensions should be converted to the International System of Units for calculation. Due to the slight change in longitude and latitude in the Ionian Sea region, we use the arc distance along longitude and latitude between two points as the coordinate distance. The Spherical Distance Calculation formula is shown in Equation 1.

<!-- b000196 | prose | pages [6] -->
(

<!-- b000197 | prose | pages [6] -->
𝐿𝑎𝑡𝑡𝑖𝑡𝑢𝑑𝑒𝐴𝑟𝑐= 𝑅· Δ𝜙 (1) 𝐿𝑜𝑛𝑔𝑡𝑖𝑡𝑢𝑑𝑒𝐴𝑟𝑐= 𝑅· cos 𝜙1 · 𝜆

<!-- b000198 | furniture | pages [6] -->
关注数学模型

<!-- b000199 | furniture | pages [6] -->
2

<!-- b000200 | furniture | pages [6] -->
MATHmodels

<!-- b000201 | furniture | pages [6] -->
获取更多资讯

<!-- b000202 | furniture | pages [7] -->
Team #2407038

<!-- b000203 | furniture | pages [7] -->
Page 6

<!-- b000204 | heading | pages [7] -->
Trajectory Prediction Model Based on Dynamics Analysis

<!-- b000205 | prose | pages [7] -->
5

<!-- b000206 | prose | pages [7] -->
Advanced Time Series Analysis: Delving Deep into Ocean Current Speed Data 5.1

<!-- b000207 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000208 | heading | pages [7] -->
Step 1: ARIMA Time Series Prediction Model Set-up

<!-- b000209 | prose | pages [7] -->
We employed an autoregressive integrated moving average (ARIMA) time series model [6] to predict the conditions of ocean currents. This model provides predictions of changes in ocean currents over a future period through mathematical modeling methods.

<!-- b000210 | prose | pages [7] -->
It is first necessary to check the stationarity of the data since the time series should be stationary. It can be found that the series is not stationary, so the differencing operation, Equation 2, is used to transform it into a stationary series.

<!-- b000211 | prose | pages [7] -->
Δ𝑑𝑌𝑡= Δ(Δ𝑑−1𝑌𝑡) 𝑓𝑜𝑟(𝑑= 1) simple differencing can be represented as Equation 3.

<!-- b000212 | prose | pages [7] -->
(2)

<!-- b000213 | prose | pages [7] -->
Δ𝑌𝑡= 𝑌𝑡−𝑌𝑡−1.

<!-- b000214 | prose | pages [7] -->
(3)

<!-- b000215 | prose | pages [7] -->
The autoregressive part reflects the linear relationship between the current value and its past values.

<!-- b000216 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000217 | prose | pages [7] -->
For the 𝑝𝑡ℎorder autoregressive part, there is Equation 4.

<!-- b000218 | prose | pages [7] -->
𝐴𝑅(𝑝) : 𝜙1𝑌𝑡−1 + 𝜙2𝑌𝑡−2 + . . . + 𝜙𝑝𝑌𝑡−𝑝 (4)

<!-- b000219 | prose | pages [7] -->
The moving average part reflects the linear relationship between the current forecasting error and past observation errors. For the 𝑞𝑡ℎorder moving average part, there is Equation 5.

<!-- b000220 | prose | pages [7] -->
𝑀𝐴(𝑞) : 𝜃1𝜀𝑡−1 + 𝜃2𝜀𝑡−2 + . . . + 𝜃𝑞𝜀𝑡−𝑞 (5)

<!-- b000221 | prose | pages [7] -->
Therefore, for the ARIMA model, let 𝑌𝑡be the observed value of the time series at time 𝑡, and the ARIMA model can be represented as Equation 6.

<!-- b000222 | prose | pages [7] -->
𝑝

<!-- b000223 | prose | pages [7] -->
𝑞

<!-- b000224 | prose | pages [7] -->
𝜙𝑖Δ𝑑𝑌𝑡−𝑖+

<!-- b000225 | prose | pages [7] -->
Δ𝑑𝑌𝑡= 𝜇+

<!-- b000226 | prose | pages [7] -->
∑︁

<!-- b000227 | prose | pages [7] -->
𝑖=1

<!-- b000228 | prose | pages [7] -->
∑︁

<!-- b000229 | prose | pages [7] -->
𝜃𝑗𝜀𝑡−𝑗+ 𝜀𝑡 (6)

<!-- b000230 | prose | pages [7] -->
𝑗=1

<!-- b000231 | prose | pages [7] -->
Where: Δ𝑑𝑌𝑡denotes the series after (𝑑) differencing operations. 𝜇is the constant term of the model. 𝜙𝑖are the coefficients of the autoregressive terms, where 𝑖= 1, . . . , 𝑝. 𝜃𝑗are the coefficients of the moving average terms, where 𝑗= 1, . . . , 𝑞. 𝜀𝑡is the error term at time 𝑡, assumed to be a white noise series.

<!-- b000232 | prose | pages [7] -->
After multiple adjustments and testing, our ARIMA model’s forecasted results were compared with actual data shown in Figure 3, revealing alignment in three comparison charts. Model validation involved calculating and analyzing the residual series, showcasing even scattering around the zero line without discernible trends or patterns. In conclusion, the ARIMA model performs well predicting ocean current changes, supported by a stationary distribution and random residual series.

<!-- b000233 | prose | pages [7] -->
Due to inherent model limitations, continuous monitoring and adjustments based on new data are emphasized.

<!-- b000234 | prose | pages [7] -->
Current Velocity from East to West

<!-- b000235 | prose | pages [7] -->
Current Velocity from North to South

<!-- b000236 | prose | pages [7] -->
0.4

<!-- b000237 | prose | pages [7] -->
0.4

<!-- b000238 | prose | pages [7] -->
Realistic Data

<!-- b000239 | prose | pages [7] -->
0.3

<!-- b000240 | prose | pages [7] -->
0.3

<!-- b000241 | prose | pages [7] -->
Predicted Data

<!-- b000242 | prose | pages [7] -->
0.2

<!-- b000243 | prose | pages [7] -->
0.2

<!-- b000244 | prose | pages [7] -->
0.1

<!-- b000245 | prose | pages [7] -->
0.1

<!-- b000246 | prose | pages [7] -->
Velocity (m/s)

<!-- b000247 | prose | pages [7] -->
Velocity (m/s)

<!-- b000248 | prose | pages [7] -->
0

<!-- b000249 | prose | pages [7] -->
0

<!-- b000250 | prose | pages [7] -->
-0.1

<!-- b000251 | prose | pages [7] -->
-0.1

<!-- b000252 | prose | pages [7] -->
-0.2

<!-- b000253 | prose | pages [7] -->
-0.2

<!-- b000254 | prose | pages [7] -->
-0.3

<!-- b000255 | prose | pages [7] -->
-0.3

<!-- b000256 | prose | pages [7] -->
-0.4

<!-- b000257 | prose | pages [7] -->
-0.4

<!-- b000258 | prose | pages [7] -->
-0.5

<!-- b000259 | prose | pages [7] -->
-0.5

<!-- b000260 | prose | pages [7] -->
-0.6

<!-- b000261 | prose | pages [7] -->
-0.6

<!-- b000262 | prose | pages [7] -->
0 50 100 150 200 250 300 350 400

<!-- b000263 | prose | pages [7] -->
0 50 100 150

<!-- b000264 | prose | pages [7] -->
Time (Day)

<!-- b000265 | prose | pages [7] -->
Current Velocity from Up to Down 10-4

<!-- b000266 | prose | pages [7] -->
8

<!-- b000267 | prose | pages [7] -->
Realistic Data

<!-- b000268 | prose | pages [7] -->
Realistic Data

<!-- b000269 | prose | pages [7] -->
Predicted Data

<!-- b000270 | prose | pages [7] -->
Predicted Data

<!-- b000271 | prose | pages [7] -->
6

<!-- b000272 | prose | pages [7] -->
4

<!-- b000273 | prose | pages [7] -->
Velocity (m/s)

<!-- b000274 | prose | pages [7] -->
2

<!-- b000275 | prose | pages [7] -->
0

<!-- b000276 | prose | pages [7] -->
-2

<!-- b000277 | prose | pages [7] -->
-4

<!-- b000278 | prose | pages [7] -->
-6

<!-- b000279 | prose | pages [7] -->
-8

<!-- b000280 | prose | pages [7] -->
200 200 250 300 350 400

<!-- b000281 | prose | pages [7] -->
0 50 100 150 200 250 300 350

<!-- b000282 | prose | pages [7] -->
Time (Day)

<!-- b000283 | prose | pages [7] -->
Time (Day)

<!-- b000284 | prose | pages [7] -->
(b) East-West Velocity Pred 𝑣𝑠Real

<!-- b000285 | prose | pages [7] -->
(a) North-South Velocity Pred 𝑣𝑠Real

<!-- b000286 | prose | pages [7] -->
(c) Vertical Velocity Pred 𝑣𝑠Real

<!-- b000287 | caption | pages [7] -->
Figure 3: Predicted Current Velocity 𝑣𝑠Real Current Velocity

<!-- b000288 | furniture | pages [7] -->
关注数学模型

<!-- b000289 | furniture | pages [7] -->
2

<!-- b000290 | furniture | pages [7] -->
MATHmodels

<!-- b000291 | furniture | pages [7] -->
获取更多资讯

<!-- b000292 | furniture | pages [8] -->
Team #2407038

<!-- b000293 | furniture | pages [8] -->
Page 7

<!-- b000294 | prose | pages [8] -->
Step 2: Quantifying Uncertainty Using Monte Carlo Method To compute this error, we utilized the Monte Carlo method. The Monte Carlo method is a numerical computation technique based on random sampling.

<!-- b000295 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000296 | prose | pages [8] -->
• Generate Random Input Time Series

<!-- b000297 | prose | pages [8] -->
Random Input Generation: First, generate a series of random input time series, shown in Equation 7, which should reflect the potential fluctuations of natural variables, thereby being used to generate different ocean current velocity prediction scenarios.

<!-- b000298 | prose | pages [8] -->
𝑋𝑡∼𝑁(𝜇, 𝜎2) (7) where, 𝑡= 1, 2, ...,𝑇represents the time points in the time series.

<!-- b000299 | prose | pages [8] -->
• Ocean Current Velocity Vector Sequence Prediction

<!-- b000300 | prose | pages [8] -->
Model Prediction: Input each randomly generated time series into the pre-established and fitted ARIMA model. The model will output a series of predicted ocean current velocity vector sequences for each input series, shown in Equation 8.

<!-- b000301 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000302 | prose | pages [8] -->
ˆ𝑌𝑡= 𝐴𝑅𝐼𝑀𝐴(𝑋𝑡) (8) Here, 𝐴𝑅𝐼𝑀𝐴(𝑋𝑡) represents the ARIMA model’s prediction function given the input 𝑋𝑡.

<!-- b000303 | prose | pages [8] -->
• Evaluation of Uncertainty

<!-- b000304 | prose | pages [8] -->
Uncertainty Measurement: Calculate the ratio of each residual item to each actual velocity item for each set of residual series, which can be obtained by comparing the predicted ocean current velocity vector series with the actual observed ocean current velocity series, shown in Equation 9.

<!-- b000305 | prose | pages [8] -->
|𝐴𝑐𝑡𝑢𝑎𝑙𝑉𝑒𝑙𝑜𝑐𝑖𝑡𝑦| = | ˆ𝑌𝑡−𝑌𝑡| |𝑅𝑒𝑠𝑖𝑑𝑢𝑎𝑙| 𝑅𝑡=

<!-- b000306 | prose | pages [8] -->
(9) |𝑌𝑡|

<!-- b000307 | prose | pages [8] -->
This method emphasizes the maximum relative error, Equation 10, highlighting the degree of deviation between the prediction results and actual conditions in the worst-case scenario. The ratio series is shown in Figure 4.

<!-- b000308 | prose | pages [8] -->
𝑈= max 𝑅𝑡 (10)

<!-- b000309 | prose | pages [8] -->
Uncertainty of Prediction in Test-set

<!-- b000310 | prose | pages [8] -->
4

<!-- b000311 | prose | pages [8] -->
Uncertainty (%)

<!-- b000312 | prose | pages [8] -->
2

<!-- b000313 | prose | pages [8] -->
0

<!-- b000314 | prose | pages [8] -->
-2

<!-- b000315 | prose | pages [8] -->
-4

<!-- b000316 | prose | pages [8] -->
0 50 100 150 200 250 300 350 400 Time (Day)

<!-- b000317 | caption | pages [8] -->
Figure 4: Uncertainty Series in Test-set

<!-- b000318 | prose | pages [8] -->
• Calculation of Average Uncertainty

<!-- b000319 | prose | pages [8] -->
Average Uncertainty: After completing the prediction and uncertainty evaluation of all random se- quences, calculate the average of all uncertainty values. This average provides a quantified indicator of the model’s average level of uncertainty under various random inputs shown in Equation 11.

<!-- b000320 | prose | pages [8] -->
𝑁

<!-- b000321 | prose | pages [8] -->
𝑈𝑎𝑣𝑔= 1

<!-- b000322 | prose | pages [8] -->
∑︁

<!-- b000323 | prose | pages [8] -->
𝑁

<!-- b000324 | prose | pages [8] -->
𝑖=1

<!-- b000325 | prose | pages [8] -->
𝑈(𝑖) = 2.39% (11)

<!-- b000326 | furniture | pages [8] -->
关注数学模型

<!-- b000327 | furniture | pages [8] -->
2

<!-- b000328 | furniture | pages [8] -->
MATHmodels

<!-- b000329 | furniture | pages [8] -->
获取更多资讯

<!-- b000330 | furniture | pages [9] -->
Team #2407038

<!-- b000331 | furniture | pages [9] -->
Page 8

<!-- b000332 | heading | pages [9] -->
Continuous Current Speed Distribution Regression Model

<!-- b000333 | prose | pages [9] -->
5.2

<!-- b000334 | prose | pages [9] -->
We use ridge regression in our model to build a function between a point’s coordinate and current speed value. The objective function for ridge regression to minimize is shown as Equation 12.

<!-- b000335 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000336 | prose | pages [9] -->
𝑛 ∑︁

<!-- b000337 | prose | pages [9] -->
𝜃2

<!-- b000338 | prose | pages [9] -->
𝐽(𝜃) = 𝑀𝑆𝐸(𝜃) +

<!-- b000339 | prose | pages [9] -->
(12) 𝑗

<!-- b000340 | prose | pages [9] -->
𝑗=1

<!-- b000341 | prose | pages [9] -->
Where 𝐽(𝜃) is the objective function to minimize, 𝑀𝑆𝐸(𝜃) is the mean square error, which will be discussed later, 𝛼is the regularization parameter used to control the influence of the regularization, and 𝜃𝑗 is named as 𝐿2 norm, which is a parameter to optimize. To further explain this algorithm, the mean square error function can be written as Equation 13.

<!-- b000342 | prose | pages [9] -->
𝑚

<!-- b000343 | prose | pages [9] -->
𝑀𝑆𝐸(𝜃) = 1

<!-- b000344 | prose | pages [9] -->
∑︁

<!-- b000345 | prose | pages [9] -->
𝑚

<!-- b000346 | prose | pages [9] -->
𝑖=1

<!-- b000347 | prose | pages [9] -->
(ℎ𝜃(𝑥(𝑖)) −𝑦(𝑖))2 (13)

<!-- b000348 | prose | pages [9] -->
Where m is the sampling number, ℎ𝜃(𝑥(𝑖)) represents the predicted value of the model for the 𝑖𝑡ℎsample,

<!-- b000349 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000350 | prose | pages [9] -->
and 𝑦(𝑖) is the actual value of the 𝑖𝑡ℎsample.

<!-- b000351 | prose | pages [9] -->
Though the principle of ridge regression is complex, Matlab provides a complete function to practice ridge regression, which is known as ridge (𝑦, 𝑋, 𝜆), where 𝑦is the target value for model fitting, 𝑋is the input matrix which contains all of the sampling points, and 𝜆is the regularization parameter, which controls the strength of regularization terms. As a three-dimensional vector, the algorithm is operated three times to obtain the current speed at a point in three directions. Since the regression results contain a large range, so we only select some of the points in the range to display, and the result is shown in Table 3.

<!-- b000352 | caption | pages [9] -->
Table 3: Predicted Current Speed at Some Points

<!-- b000353 | prose | pages [9] -->
Latitude Longitude Depth 36.583 21.833 -15.41

<!-- b000354 | prose | pages [9] -->
37.917 19.333 -114.05

<!-- b000355 | prose | pages [9] -->
36.167 22.167 -294.45

<!-- b000356 | prose | pages [9] -->
38.917 20.333 -923.26

<!-- b000357 | prose | pages [9] -->
36.583 17.333 -3181.27

<!-- b000358 | prose | pages [9] -->
...

<!-- b000359 | prose | pages [9] -->
...

<!-- b000360 | prose | pages [9] -->
...

<!-- b000361 | prose | pages [9] -->
x-velocity y-velocity z-velocity -2.767×10−5 -0.2405 0.2687

<!-- b000362 | prose | pages [9] -->
6.088×10−6 0.0344 0.0752

<!-- b000363 | prose | pages [9] -->
2.459×10−5 -0.2307 -0.12

<!-- b000364 | prose | pages [9] -->
1.556×10−4 0.1661 -0.0983

<!-- b000365 | prose | pages [9] -->
-6.264×10−6 0.1162 0.1366

<!-- b000366 | prose | pages [9] -->
...

<!-- b000367 | prose | pages [9] -->
...

<!-- b000368 | prose | pages [9] -->
... Note: The 𝑥coordinate and 𝑦coordinate are all changed back to latitude and longitude values in the table. All quantities in the table use the International

<!-- b000369 | prose | pages [9] -->
System of Units. From the table, it is easy to see that the 𝑥-component and 𝑦-component of the current speed are much higher than the 𝑧-component, which corresponds to the characteristic of the ocean current. The same method can be used to obtain the continuous seawater density distribution. Since the process is generally the same, we only provide the predicted seawater density value at some points in Table 4.

<!-- b000370 | caption | pages [9] -->
Table 4: Predicted Seawater Density at Some Points

<!-- b000371 | prose | pages [9] -->
Latitude Longitude 36.169 19.673 36.573 21.852 37.056 19.223 37.885 20.852 38.381 19.585 ...

<!-- b000372 | prose | pages [9] -->
...

<!-- b000373 | prose | pages [9] -->
Depth Seawater Density -3157 1033.76 -1605 1029.77 -3433 1034.55 -127 1025.41 -2664 1032.26 ...

<!-- b000374 | prose | pages [9] -->
...

<!-- b000375 | furniture | pages [9] -->
关注数学模型

<!-- b000376 | furniture | pages [9] -->
2

<!-- b000377 | furniture | pages [9] -->
MATHmodels

<!-- b000378 | furniture | pages [9] -->
获取更多资讯

<!-- b000379 | furniture | pages [10] -->
Team #2407038

<!-- b000380 | furniture | pages [10] -->
Page 9

<!-- b000381 | heading | pages [10] -->
Dynamical Model based on Newtonian mechanics

<!-- b000382 | prose | pages [10] -->
5.3

<!-- b000383 | prose | pages [10] -->
According to the assumption, the defective submersible will lose propulsion simultaneously when it loses contact with the host ship. So, the submersible will move only under external forces. According

<!-- b000384 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000385 | prose | pages [10] -->
to Oceanography and Physics knowledge, the four main forces that should be considered are gravity, buoyancy, resistance, and ocean current force. The force situation of the submersible is shown in Figure 5.

<!-- b000386 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000387 | caption | pages [10] -->
Figure 5: Force situation of a submersible

<!-- b000388 | prose | pages [10] -->
This graph shows the effects of multiple factors on submersibles. Before the dynamical model is constructed, we first analyze these forces. Equation 14 calculate the Gravity.

<!-- b000389 | prose | pages [10] -->
𝐹𝐺= 𝑚𝑔 (14)

<!-- b000390 | prose | pages [10] -->
Where 𝐹𝐺is the gravity and 𝑚is the mass of the submersible. According to the assumption, the mass of the submersible is a fixed value. So 𝐹𝐺will always be a fixed value.

<!-- b000391 | prose | pages [10] -->
In Equation 15, 𝐹𝐵is the buoyancy, 𝜌is the density of the seawater at the current position of the submersible, and𝑉is the volume of the submersible, which is also a fixed value according to the assumption. So, the buoyancy of the submersible only depends on the local density.

<!-- b000392 | prose | pages [10] -->
𝐹𝐵= 𝜌𝑔𝑉 (15)

<!-- b000393 | prose | pages [10] -->
In Equation 16, 𝐹𝑅is the resistance, 𝜌is still the density of the seawater 𝑣is the current velocity of the submersible, 𝐶𝑑is the resistance coefficient and 𝐴represents the upstream area of the submersible. It is easy to know that 𝐶𝑑and 𝐴can be viewed as constant values and 𝜌and 𝑣will change with the movement of the submersible.

<!-- b000394 | prose | pages [10] -->
𝐹𝑅= 1

<!-- b000395 | prose | pages [10] -->
2 𝜌𝑣2𝐶𝑑𝐴 (16)

<!-- b000396 | prose | pages [10] -->
In Equation 17, ®𝑣𝑠represents the velocity of the submersible related to the current, and ®𝑣𝑐represents the velocity of the current related to Earth. This formula shows that the velocity of the current can be directly added to the submersible’s velocity because the current’s velocity is known when the position of the submersible is known.

<!-- b000397 | prose | pages [10] -->
®𝑣= ®𝑣𝑠+ ®𝑣𝑐 (17) Equations 18 can be constructed according to Newton’s Second Law and the current speed predicted model, where 𝜙represents the angle between the resistance and the horizontal plane and 𝜃represents the angle between the projection of resistance on the horizontal plane and the x-axis. According to the previous

<!-- b000398 | furniture | pages [10] -->
关注数学模型

<!-- b000399 | furniture | pages [10] -->
2

<!-- b000400 | furniture | pages [10] -->
MATHmodels

<!-- b000401 | furniture | pages [10] -->
获取更多资讯

<!-- b000402 | furniture | pages [11] -->
Team #2407038

<!-- b000403 | furniture | pages [11] -->
Page 10

<!-- b000404 | prose | pages [11] -->
discussion, the 𝐹𝐵and 𝑣will change according to the current position, and the exact value of 𝐹𝐵and 𝑣can be predicted from the model established in 5.2.

<!-- b000405 | prose | pages [11] -->
𝑚𝑑𝑣𝑥

<!-- b000406 | prose | pages [11] -->
𝑑𝑡= −𝐹𝑅cos 𝜙cos 𝜃

<!-- b000407 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000408 | prose | pages [11] -->


<!-- b000409 | prose | pages [11] -->
𝑚𝑑𝑣𝑦

<!-- b000410 | prose | pages [11] -->
𝑑𝑡= −𝐹𝑅cos 𝜙cos 𝜃 𝑚𝑑𝑣𝑧

<!-- b000411 | prose | pages [11] -->
(18)

<!-- b000412 | prose | pages [11] -->
𝑑𝑡= 𝐹𝐵−𝐹𝐺+ 𝐹𝑅sin 𝜙

<!-- b000413 | prose | pages [11] -->


<!-- b000414 | prose | pages [11] -->
Then, we consider the seafloor topography of the Ionian Sea and set limits to ensure the submersible will not move down below the seafloor. After the dynamics equations are prepared, we use the Python package to solve the equations. Based on assumptions, the initial state of the defective submersible will be somewhere in the Ionian Sea region with v=0. Figure 6 shows the trajectory obtained from the code.

<!-- b000415 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000416 | caption | pages [11] -->
Figure 6: Trajectory of a Submersible Losing Contact

<!-- b000417 | prose | pages [11] -->
The starting point is random, which in this simulation is (9264, 6207, −3767). After calculation, the position of the submersible we predict after 3 hour is (10342, 5554, −4062). The complete trajectory of the point is shown, which means we can obtain the predicted position of the submersible at any time after calculation. In this simulation, we expect that the submersible will gradually decline along the trajectory curve, and the trajectory is irregular, resulting from periodic current and seawater density. This trajectory model provides us with information for future search and rescue work.

<!-- b000418 | heading | pages [11] -->
Discussion on Key Equipment and Technologies

<!-- b000419 | prose | pages [11] -->
5.4

<!-- b000420 | prose | pages [11] -->
To effectively reduce the uncertainties these factors introduce, the submersible needs to regularly report a series of critical data to the mother ship. This data’s accurate collection and transmission are crucial for optimizing the prediction model. Hence, the submersible needs to be equipped with the following three kinds of advanced monitoring equipment.

<!-- b000421 | prose | pages [11] -->
(i) Ocean current detection and seawater condition monitoring equipment

<!-- b000422 | prose | pages [11] -->
• Acoustic Doppler Current Profiler (ADCP):

<!-- b000423 | prose | pages [11] -->
This instrument measures the echoes from particles in the seawater at different depths from the submersible. • CTD sensors:

<!-- b000424 | prose | pages [11] -->
CTD stands for Conductivity, Temperature, and Depth, the three fundamental oceanography parameters.

<!-- b000425 | prose | pages [11] -->
(ii) Dynamics and External Resistance Monitoring System

<!-- b000426 | prose | pages [11] -->
•Inertial Navigation System (INS):

<!-- b000427 | furniture | pages [11] -->
关注数学模型

<!-- b000428 | furniture | pages [11] -->
2

<!-- b000429 | furniture | pages [11] -->
MATHmodels

<!-- b000430 | furniture | pages [11] -->
获取更多资讯

<!-- b000431 | furniture | pages [12] -->
Team #2407038

<!-- b000432 | furniture | pages [12] -->
Page 11

<!-- b000433 | prose | pages [12] -->
By measuring acceleration and angular velocity, INS provides the submersible with accurate informa- tion on position, velocity, and attitude.

<!-- b000434 | prose | pages [12] -->
(iii) Communication and Data Logging Equipment

<!-- b000435 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000436 | prose | pages [12] -->
• Underwater Acoustic Communication Devices:

<!-- b000437 | prose | pages [12] -->
In the underwater environment, submersibles rely on acoustic communication to exchange data with support ships or other submersibles.

<!-- b000438 | prose | pages [12] -->
•Data Loggers:

<!-- b000439 | prose | pages [12] -->
Used for long-term storage of collected oceanographic data, submersible motion data, and environ- mental monitoring data.

<!-- b000440 | prose | pages [12] -->
•Satellite Communication Systems (used during surface activities):

<!-- b000441 | prose | pages [12] -->
When the surfaces, the satellite communication equipment is enabled to transmit data collected during the dive and receive new instructions from the research team.

<!-- b000442 | prose | pages [12] -->
By equipping these advanced devices, the submersible can regularly obtain and report critical infor- mation to the mother ship, including ocean current data, seawater conditions, dynamics parameters, and

<!-- b000443 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000444 | prose | pages [12] -->
resistance data. This significantly reduces uncertainty and enhances the accuracy of trajectory predictions. Such configuration optimizes the prediction model’s performance, effectively reducing factors that con- tribute to uncertainty in submersible position predictions, thereby ensuring the safe and effective operation of the submersible.

<!-- b000445 | heading | pages [12] -->
Comprehensive Equipment Allocation Optimization Model

<!-- b000446 | prose | pages [12] -->
6

<!-- b000447 | prose | pages [12] -->
In facing the arduous task of marine search and rescue, rapid and effective search and rescue operations are crucial for improving survival rates. The rational allocation of search and rescue equipment carried by the main ship and rescue boats is significant. This necessitates a multi-objective optimization model that comprehensively considers costs, equipment availability, and readiness to aid decision-making. Below, we will introduce CEAOM.

<!-- b000448 | prose | pages [12] -->
6.1 Preliminary Research

<!-- b000449 | prose | pages [12] -->
Detailed investigations were conducted on several types of key equipment, shown in Table 5, including echo sounders, side scan sonars, pinger locators, magnetometers, and optical imaging systems. These devices play an indispensable role in marine search and rescue missions.

<!-- b000450 | caption | pages [12] -->
Table 5: Key Equipment

<!-- b000451 | prose | pages [12] -->
Side Scan Optical Imaging Pinger Locators Echo Sounder Sonar Magnetometer System RJE International Echologger Klein 3000 EU400 PL-600

<!-- b000452 | prose | pages [12] -->
Kongsberg

<!-- b000453 | prose | pages [12] -->
W Fishers

<!-- b000454 | prose | pages [12] -->
SeaViewer

<!-- b000455 | prose | pages [12] -->
Proton 4

<!-- b000456 | prose | pages [12] -->
SVS-650 Teledyne Benthos SonarMite EA 640 UDB-9000

<!-- b000457 | prose | pages [12] -->
Furuno Edgetech 6205 FE800

<!-- b000458 | prose | pages [12] -->
Geometrics

<!-- b000459 | prose | pages [12] -->
Ocean Systems

<!-- b000460 | prose | pages [12] -->
G-882

<!-- b000461 | prose | pages [12] -->
Inc. OASIS Marine Magnetics

<!-- b000462 | prose | pages [12] -->
Kongsberg

<!-- b000463 | prose | pages [12] -->
SeaSPY

<!-- b000464 | prose | pages [12] -->
OE14-502

<!-- b000465 | furniture | pages [12] -->
关注数学模型

<!-- b000466 | furniture | pages [12] -->
2

<!-- b000467 | furniture | pages [12] -->
MATHmodels

<!-- b000468 | furniture | pages [12] -->
获取更多资讯

<!-- b000469 | furniture | pages [13] -->
Team #2407038

<!-- b000470 | prose | pages [13] -->
6.2

<!-- b000471 | heading | pages [13] -->
Model Construction

<!-- b000472 | prose | pages [13] -->
6.2.1

<!-- b000473 | heading | pages [13] -->
Parameter Introduction

<!-- b000474 | furniture | pages [13] -->
Page 12

<!-- b000475 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000476 | prose | pages [13] -->
In this multi-objective optimization model, the focus is on five parameters: equipment cost, annual maintenance cost, availability, usage, and readiness. Below is the definition of each parameter and an introduction to their calculation methods.

<!-- b000477 | prose | pages [13] -->
• Equipment Cost (C):

<!-- b000478 | prose | pages [13] -->
Reflects the initial investment required to purchase various search equipment.

<!-- b000479 | prose | pages [13] -->
• Annual Maintenance Cost (M):

<!-- b000480 | prose | pages [13] -->
Represents the annual expense required to ensure that the equipment maintains optimal working conditions within the specified service life.

<!-- b000481 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000482 | prose | pages [13] -->
• Availability (A):

<!-- b000483 | prose | pages [13] -->
Considers factors such as water temperature, depth, currents, noise, and interference to quantify the equipment’s operational performance under various conditions.

<!-- b000484 | prose | pages [13] -->
Calculation of Availability:

<!-- b000485 | prose | pages [13] -->
The calculation principles for coefficients reflecting the impact of various environmental factors on sound wave propagation can be summarized into a unified equation as Equation 19.

<!-- b000486 | prose | pages [13] -->
Range Environmental Coefficient (𝐸𝐶) = (19) Sensitivity

<!-- b000487 | prose | pages [13] -->
Here, the Environmental Coefficient (𝐸𝐶) could be the Water Temperature Coefficient (𝑊𝑇𝐶), Water Depth Coefficient (𝑊𝐷𝐶), Water Current Coefficient (𝑊𝐶𝐶), Noise Coefficient (𝑁𝐶), or Interference Coefficient (𝐼𝐶), depending on the specific application context and metric being measured.

<!-- b000488 | prose | pages [13] -->
Range denotes the working range of the environmental variable (water temperature, water depth, water current, noise, or interference). This reflects the product’s adaptability or performance variation range under different conditions.

<!-- b000489 | prose | pages [13] -->
Sensitivity refers to the degree to which the product’s performance changes in response to changes in the environmental variable.

<!-- b000490 | prose | pages [13] -->
In summary, the availability index can be calculated as Equation 20.

<!-- b000491 | prose | pages [13] -->
Availability Index = 𝑊𝑇𝐶× 𝑊𝐷𝐶× 𝑊𝐶𝐶× 𝑁𝐶× 𝐼𝐶

<!-- b000492 | prose | pages [13] -->
Usage (U):

<!-- b000493 | prose | pages [13] -->
(20)

<!-- b000494 | prose | pages [13] -->
The equipment’s usage time within a year reflects the actual workload of the equipment.

<!-- b000495 | prose | pages [13] -->
Readiness (R): The preparation time required before each use directly affects the response speed of the mission.

<!-- b000496 | furniture | pages [13] -->
关注数学模型

<!-- b000497 | furniture | pages [13] -->
2

<!-- b000498 | furniture | pages [13] -->
MATHmodels

<!-- b000499 | furniture | pages [13] -->
获取更多资讯

<!-- b000500 | furniture | pages [14] -->
Team #2407038

<!-- b000501 | prose | pages [14] -->
6.2.2

<!-- b000502 | heading | pages [14] -->
Data Processing

<!-- b000503 | furniture | pages [14] -->
Page 13

<!-- b000504 | prose | pages [14] -->
We first define each data set as a collection of a series of observed values, shown in Equation 21. Suppose we have surveyed 𝑘different products for each type of equipment, each with its corresponding

<!-- b000505 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000506 | prose | pages [14] -->
Let 𝑃𝑖represent the average value of the cost, availability, maintenance cost, usage, and readiness. parameter for equipment type 𝑖. 𝑃𝑖𝑗is the observed value of the parameter for the 𝑗𝑡ℎproduct of equipment type 𝑖. 𝑘𝑖is the number of products surveyed for equipment type 𝑖.

<!-- b000507 | prose | pages [14] -->
𝑃𝑖= 1

<!-- b000508 | prose | pages [14] -->
𝑘𝑖

<!-- b000509 | prose | pages [14] -->
𝑘𝑖 ∑︁

<!-- b000510 | prose | pages [14] -->
𝑃𝑖𝑗 (21)

<!-- b000511 | prose | pages [14] -->
𝑗=1

<!-- b000512 | prose | pages [14] -->
The final data processing results are shown in Table 6, where ES stands for Echo Sounder, SSS stands for Side Scan Sonar, PL stands for Pinger Locators, MM stands for Magnetometer, and OI stands for Optical Imaging.

<!-- b000513 | caption | pages [14] -->
Table 6: Equipment Data

<!-- b000514 | prose | pages [14] -->
ES SSS PL MM OI

<!-- b000515 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000516 | prose | pages [14] -->
C 15000 85000 A 4291667 1206667 M 5500 1500 R 8 4 U 480 960

<!-- b000517 | prose | pages [14] -->
6.2.3 Objective Function

<!-- b000518 | prose | pages [14] -->
15000 50000 50000 1580000 633333 1293333 500 2500 5000 1.1 1.2 0.5 108 300 369

<!-- b000519 | prose | pages [14] -->
Set the objective function to minimize total cost, maximize equipment availability, and minimize preparation time.

<!-- b000520 | prose | pages [14] -->
(i) Cost Minimization This includes the equipment’s initial purchase and maintenance costs, which are related to the frequency of use. The specific expression is Equation 22.

<!-- b000521 | prose | pages [14] -->
𝑛

<!-- b000522 | prose | pages [14] -->


<!-- b000523 | prose | pages [14] -->
∑︁

<!-- b000524 | prose | pages [14] -->
𝑓𝐶(𝑥) =

<!-- b000525 | prose | pages [14] -->
𝑖=1

<!-- b000526 | prose | pages [14] -->
𝐶𝑖· 𝑥𝑖+ 𝑀𝑖

<!-- b000527 | prose | pages [14] -->


<!-- b000528 | prose | pages [14] -->
· 𝑥𝑖

<!-- b000529 | prose | pages [14] -->
(22)

<!-- b000530 | prose | pages [14] -->
𝑈𝑖

<!-- b000531 | prose | pages [14] -->
This formula considers the direct cost 𝐶𝑖of purchasing equipment 𝑥𝑖and the annual maintenance cost 𝑀𝑖allocated according to the usage rate 𝑈𝑖. Here, 𝑥𝑖represents the decision variable, whether or not to purchase the 𝑖𝑡ℎtype of equipment.

<!-- b000532 | prose | pages [14] -->
(ii)Availability Maximization Availability indicates the effective working capacity of equipment under specific conditions. mathematical expression is Equation 23.

<!-- b000533 | prose | pages [14] -->
𝑓𝐴(𝑥) = −

<!-- b000534 | prose | pages [14] -->
The

<!-- b000535 | prose | pages [14] -->
𝑛 ∑︁

<!-- b000536 | prose | pages [14] -->
(𝐴𝑖· 𝑥𝑖) (23)

<!-- b000537 | prose | pages [14] -->
𝑖=1

<!-- b000538 | prose | pages [14] -->
The negative sign indicates it is a maximization problem. By maximizing 𝐴𝑖· 𝑥𝑖(i.e., the availability of the chosen equipment), the model ensures that the equipment configuration is efficient and adaptable to various operational environments.

<!-- b000539 | prose | pages [14] -->
(iii)Preparation Time Minimization

<!-- b000540 | furniture | pages [14] -->
关注数学模型

<!-- b000541 | furniture | pages [14] -->
2

<!-- b000542 | furniture | pages [14] -->
MATHmodels

<!-- b000543 | furniture | pages [14] -->
获取更多资讯

<!-- b000544 | furniture | pages [15] -->
Team #2407038

<!-- b000545 | prose | pages [15] -->
The specific expression is Equation 24.

<!-- b000546 | furniture | pages [15] -->
Page 14

<!-- b000547 | prose | pages [15] -->
𝑓𝑅(𝑥) = max(𝑅𝑖· 𝑥𝑖) (24)

<!-- b000548 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000549 | prose | pages [15] -->
Here, 𝑅𝑖represents the preparation time for the equipment from the decision to use it to its readiness for operation. 𝑥𝑖represents the quantity of the 𝑖𝑡ℎtype of equipment, and 𝑛is the number of types of equipment.

<!-- b000550 | heading | pages [15] -->
Genetic Algorithm for Multi-objective Optimization

<!-- b000551 | prose | pages [15] -->
6.3

<!-- b000552 | prose | pages [15] -->
The model employs a genetic algorithm for multi-objective optimization, seeking the optimal balance among cost, availability, and readiness. Ultimately generating a series of solutions that form a Pareto Front shown in Figure 7.

<!-- b000553 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000554 | caption | pages [15] -->
Figure 7: Solutions in Pareto Front

<!-- b000555 | prose | pages [15] -->
Since the quantity of equipment can only be integers, further processing of the results to eliminate duplicate schemes yields in Table 7.

<!-- b000556 | caption | pages [15] -->
Table 7: Optimization Results

<!-- b000557 | prose | pages [15] -->
ES SSS PL MM OI 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 1 0 1 1 0 1 0 1 0 1 1 0 0 1 1 1 0 0 1 0 1 1 1 0 1 1 0 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1

<!-- b000558 | prose | pages [15] -->
6.4

<!-- b000559 | heading | pages [15] -->
Results and Analysis

<!-- b000560 | prose | pages [15] -->
Readiness Availability Cost 1.1 1580000 15000 1.2 633333 50000 0.5 1293333 50000 1.1 2873333 65000 8 7165000 80000 4 2786667 100000 8 7078334 115000 8 7798333 130000 4 4080000 150000 8 8371667 165000 4 3133333 185000 8 9005000 215000

<!-- b000561 | prose | pages [15] -->
Ultimately, we selected four matching schemes, divided into three categories, to achieve the deployment of the main ship and rescue boats. As shown in Table 8 below. Based on the deployment analysis of the

<!-- b000562 | furniture | pages [15] -->
关注数学模型

<!-- b000563 | furniture | pages [15] -->
2

<!-- b000564 | furniture | pages [15] -->
MATHmodels

<!-- b000565 | furniture | pages [15] -->
获取更多资讯

<!-- b000566 | furniture | pages [16] -->
Team #2407038

<!-- b000567 | furniture | pages [16] -->
Page 15

<!-- b000568 | caption | pages [16] -->
Table 8: Four Possible Choices

<!-- b000569 | prose | pages [16] -->
ES SSS PL MM Scheme 1 1 1 1 1 Scheme 2 0 0 0 0 Scheme 3 0 0 1 0 OI Readiness Availability Cost 1 1 8 9005000 215000 1 1 0.5 1293333 50000 1 1 1.1 2873333 65000

<!-- b000570 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000571 | prose | pages [16] -->
Scheme 4 0 1 1 0 1 1 4 4080000 150000

<!-- b000572 | prose | pages [16] -->
results table and a detailed consideration of the characteristics of each scheme, we can derive the following detailed strategies and deployment plans.

<!-- b000573 | prose | pages [16] -->
Main Ship (Optimum Performance Scheme) - Scheme 1:

<!-- b000574 | prose | pages [16] -->
As the option with the best performance and the highest cost, the main ship leverages its large volume and sufficient preparation time to equip the most advanced search and rescue equipment. Its role extends beyond search and rescue to serve as a command and coordination center.

<!-- b000575 | prose | pages [16] -->
Primary Rescue Boats (Rapid Response Scheme) - Schemes 2 and 3:

<!-- b000576 | prose | pages [16] -->
The primary rescue boats emphasize rapid response capability. Their readiness is lower, allowing for quick preparation and dispatch to the accident area for preliminary search and rescue shortly after an

<!-- b000577 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000578 | prose | pages [16] -->
incident occurs.

<!-- b000579 | prose | pages [16] -->
Intermediate Rescue Boat (Balanced Performance Scheme) - Scheme 4:

<!-- b000580 | prose | pages [16] -->
The intermediate rescue boat balances readiness, cost, and performance. The intermediate rescue boat has a slightly longer preparation time than the primary rescue boats. Still, once deployed, it is equipped with more advanced search and rescue equipment and technology, significantly enhancing its search and rescue capabilities.

<!-- b000581 | prose | pages [16] -->
6.5

<!-- b000582 | heading | pages [16] -->
Conclusion

<!-- b000583 | prose | pages [16] -->
This 1 + 𝑛rescue scheme not only improves the response speed and efficiency of rescue operations but also strengthens the adaptability to rescue needs under different maritime conditions and situations. Moreover, this strategy ensures efficient, precise search and rescue actions, providing quicker and more effective rescue services for those trapped in maritime emergencies.

<!-- b000584 | prose | pages [16] -->
Grid Probability Search Technique based on Poisson Distribution 7

<!-- b000585 | prose | pages [16] -->
7.1 Regional Rasterization

<!-- b000586 | prose | pages [16] -->
In a real-world deep water search, rescue vessels conduct operations on the ocean surface using search equipment like sonar to detect aiming objectives. Therefore, the search area can be treated as a surface.

<!-- b000587 | prose | pages [16] -->
Before the accident, the lost submersible will send its last information to the host ship, and the rescue vessels are then dispatched to the mission by analyzing the loss data. Apart from the location, the quality of a search is measured through an effective examination of the search area. Systematic inspection of the search area is achieved by following a predefined pattern tailored to the specific conditions of the search. According to Salvage Manual [7], deep ocean searches have four proven effective and practical search patterns: Parallel Grid Search, Constant Range Search, “Z” search, and ROV Box Search.

<!-- b000588 | prose | pages [16] -->
Parallel Grid Search is the most commonly used and effective search pattern in modern rescue missions, shown in Figure 8(a). Consequently, our model will build upon this search pattern.

<!-- b000589 | furniture | pages [16] -->
关注数学模型

<!-- b000590 | furniture | pages [16] -->
2

<!-- b000591 | furniture | pages [16] -->
MATHmodels

<!-- b000592 | furniture | pages [16] -->
获取更多资讯

<!-- b000593 | furniture | pages [17] -->
Team #2407038

<!-- b000594 | furniture | pages [17] -->
Page 16

<!-- b000595 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000596 | prose | pages [17] -->
(a) Parallel Grid Search (b) Search Grid

<!-- b000597 | prose | pages [17] -->
*The reasonable range of line spacing is generally between 0.5 and 2 times the target size, the reasonable range of Swath Width is generally between 0.5 and 2 times the target size, and the reasonable range of range overlap is generally between 10% and 30%.

<!-- b000598 | caption | pages [17] -->
Figure 8: Searching Pattern of the Rescue Vessel

<!-- b000599 | prose | pages [17] -->
With the help of loss data and Parallel Grid Search, search probability analysis can be determined by applying a grid model that rasterizes the search area into smaller cells shown in Figure 8(b). Each cell

<!-- b000600 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000601 | prose | pages [17] -->
is assigned a probability percentage indicating the likelihood of the target being located within that cell. Therefore, any point’s grid label 𝑁can be expressed as Equation 25.

<!-- b000602 | prose | pages [17] -->
𝑁= 𝐼𝑁𝑇( 𝑥

<!-- b000603 | prose | pages [17] -->
) + 𝑀× 𝐼𝑁𝑇( 𝑦

<!-- b000604 | prose | pages [17] -->
𝐺𝑠

<!-- b000605 | prose | pages [17] -->
) (25)

<!-- b000606 | prose | pages [17] -->
𝐺𝑠

<!-- b000607 | prose | pages [17] -->
Where (𝑥, 𝑦) is the coordinate of a potential place, the abscissa 𝑥represents the longitude and the ordinate 𝑦represents the latitude, 𝐺𝑠is the grid size, 𝑀= 𝑥𝑚𝑎𝑥

<!-- b000608 | prose | pages [17] -->
𝐺𝑠, 𝑥𝑚𝑎𝑥is the maximum length of the horizontal axis. Furthermore, the grid center position coordinates can be obtained by Equation 26.

<!-- b000609 | prose | pages [17] -->
𝑥𝐺= (𝑁%𝑀) · 𝐺𝑠+ 𝐺𝑠

<!-- b000610 | prose | pages [17] -->
(

<!-- b000611 | prose | pages [17] -->
2

<!-- b000612 | prose | pages [17] -->
(26)

<!-- b000613 | prose | pages [17] -->
𝑦𝐺= 𝐼𝑁𝑇(𝑁/𝑀) + 𝐺𝑠

<!-- b000614 | prose | pages [17] -->
2

<!-- b000615 | prose | pages [17] -->
In the area of the Mediterranean, the most prevalent rescue vessel model operating is USNS Grasp (T-ARS 51) [8]. According to its manual, this vessel model has a speed of 25 knots. Known the lost submersible size was 670 cm × 280 cm × 250 cm, other search parameters can be determined below: Swath Width: 2 × 250𝑐𝑚= 5𝑚Overlap: 20% Velocity: 25 × 1.852 = 46𝑘𝑚/ℎ. Assuming a square search area with 30 min search time (t) using Parallel Grid Search, the grid size can be determined using Equation 27.

<!-- b000616 | prose | pages [17] -->
𝐺𝑠= 𝑣× 𝑡

<!-- b000617 | prose | pages [17] -->
𝑇𝑢𝑟𝑛𝑠= (𝑆𝑊) × 𝑇𝑢𝑟𝑛𝑠−(𝑆𝑊× 𝑂𝑉) × (𝑇𝑢𝑟𝑛𝑠−1) (27)

<!-- b000618 | prose | pages [17] -->
Where SW stands for Swath Width, OV stands for Overlap. Therefore, an approximate 300m × 300m grid model is established for regional rasterization.

<!-- b000619 | prose | pages [17] -->
7.2 Poisson Probability Distribution

<!-- b000620 | prose | pages [17] -->
Based on the discussion in 7.1, we have divided the rescue region into several regions. Then, we hope to find the probability distribution of these regions, which means the probability of finding a missing submersible in each region. According to the model built in 5, we can suppose that the submersible is most likely to be in the grid corresponding to the coordinates we predict. The farther the coordinates are from the central grid, the lower the probability of finding the ship. To describe the discrete probability

<!-- b000621 | furniture | pages [17] -->
关注数学模型

<!-- b000622 | furniture | pages [17] -->
2

<!-- b000623 | furniture | pages [17] -->
MATHmodels

<!-- b000624 | furniture | pages [17] -->
获取更多资讯

<!-- b000625 | furniture | pages [18] -->
Team #2407038

<!-- b000626 | furniture | pages [18] -->
Page 17

<!-- b000627 | prose | pages [18] -->
distribution with such a characteristic, we choose to use the Poisson distribution. The Poisson distribution function is shown as Equation 28.

<!-- b000628 | prose | pages [18] -->
𝑃(𝜒= 𝑘) = 𝑒−𝜆· 𝜆𝑘

<!-- b000629 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000630 | prose | pages [18] -->
, 𝑘∈𝑁 (28) 𝑘!

<!-- b000631 | prose | pages [18] -->
Where 𝜆is called the intensity parameter, describing the intensity of the event occurrence, a higher 𝜆 means the Poisson distribution has a larger probability on bigger k values.

<!-- b000632 | prose | pages [18] -->
To compare the finding probability of the grid near the central grid, we use the Manhattan distance as the reference. The Manhattan distance calculates the sum of the separate differences in horizontal and vertical coordinates between two points, which can be described as Equation 29.

<!-- b000633 | prose | pages [18] -->
𝑑= |𝑥2 −𝑥1| + |𝑦2 −𝑦1| (29)

<!-- b000634 | prose | pages [18] -->
The value of the distance will correspond to the 𝑘in the Poisson distribution function. For example, if the distance between a grid and the central grid, the probability that we can find the missing submersible in this grid is as Equation 30.

<!-- b000635 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000636 | prose | pages [18] -->
𝑃𝑓= 𝑃(𝜒= 4) · 1

<!-- b000637 | prose | pages [18] -->
(30)

<!-- b000638 | prose | pages [18] -->
𝑁4

<!-- b000639 | prose | pages [18] -->
Where 𝑁4 represents the total number of grids with a distance to the central grid of 4. As time flows, the position of the submersible becomes more difficult to predict due to the uncertainty of ocean currents and seawater density, so the probability of the submersible in the central grid will gradually decrease. Assume that the ratio of the probability equals the ratio of the time. Then we can derive Equation 31.

<!-- b000640 | prose | pages [18] -->
𝜆= 𝑚+ ln 𝑡

<!-- b000641 | prose | pages [18] -->
(31)

<!-- b000642 | prose | pages [18] -->
𝑡0

<!-- b000643 | prose | pages [18] -->
Where 𝑡0 represents the minimum time for the rescue vessel to prepare and arrive at the searching destination. At the same time, m is a constant that will influence the initial probability of a successful search in the central grid. We suppose 𝑡0 is a constant value, which means the vessels’ preparation time is the same.

<!-- b000644 | prose | pages [18] -->
Probability Calculation Based on Bayesian Theory 7.3

<!-- b000645 | prose | pages [18] -->
Since we have calculated the size of each grid in line with the maximum search competence of a rescue vessel, we can divide time into multiple time intervals as shown in Equation 32.

<!-- b000646 | prose | pages [18] -->
[𝑡0 + 𝑛· 𝑡𝑖𝑛𝑡𝑒𝑟, 𝑡0 + (𝑛+ 1) · 𝑡𝑖𝑛𝑡𝑒𝑟) (32)

<!-- b000647 | prose | pages [18] -->
Where 𝑡0 is still the minimum time for the rescue vessel to prepare and 𝑡𝑖𝑛𝑡𝑒𝑟represents the minimum time for one vessel to effectively search for one place, which is 30 minutes in our example.

<!-- b000648 | prose | pages [18] -->
According to 7.2, we can use the following principle to deploy our rescue vessels. For a single ship, it will search for the grid range with the highest probability at the beginning of a time interval, and it will not change the searching grid until the beginning of the next time interval. Since many vessels can be deployed simultaneously to increase efficiency and strive for more rescue time, they will be deployed in different grids with high probabilities at the beginning of each time interval. Due to the small distances between different regions, the time to move from one grid to another can be ignored compared with the search path length. The process is shown in Figure 9.

<!-- b000649 | furniture | pages [18] -->
关注数学模型

<!-- b000650 | furniture | pages [18] -->
2

<!-- b000651 | furniture | pages [18] -->
MATHmodels

<!-- b000652 | furniture | pages [18] -->
获取更多资讯

<!-- b000653 | furniture | pages [19] -->
Team #2407038

<!-- b000654 | furniture | pages [19] -->
Page 18

<!-- b000655 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000656 | caption | pages [19] -->
Figure 9: Searching Strategy Based on Probability

<!-- b000657 | prose | pages [19] -->
In this figure, the yellow depth represents the size of the probability we predict for this area, and the searching grid is chosen based on the probability of a single rescue vessel. In the next time interval, the

<!-- b000658 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000659 | prose | pages [19] -->
predicted position of the submersible may move to the next central grid, which becomes our next search region.

<!-- b000660 | prose | pages [19] -->
Another important design is that we will not search for the same regions for a second time, which are the red grids in Figure 9. The reason for this strategy is that the average current speed is around 0.12𝑚/𝑠, so for the time interval of 30 minutes, the movement distance of the submersible will be less than 𝑣𝑡= 216𝑚. Considering the direction of the current and resistance effect, the real moving distance in this period will usually be far less than 216 meters, which is smaller than the size of a grid. It means that the submersible only has a small probability of occurring in one grid after it has been searched completely. So, we tend to expand the search range instead of exploring one region repeatedly to ‘wait’ for the submersible to come out. This means we suppose that the probability of finding the submersible in the grid we have searched is

<!-- b000661 | heading | pages [19] -->
0. Then, Bayes’s theorem, Equation 33, should be applied to transform the prior probability distribution

<!-- b000662 | prose | pages [19] -->
to the posterior probability distribution.

<!-- b000663 | prose | pages [19] -->
𝑝(𝐴|𝐵) = 𝑝(𝐵|𝐴) · 𝑝(𝐴)

<!-- b000664 | prose | pages [19] -->
(33) 𝑝(𝐵)

<!-- b000665 | prose | pages [19] -->
Where 𝑝(𝐴) is called the prior probability and 𝑝(𝐴|𝐵) is called the posterior probability. In this problem, the prior probability is the Poisson probability, and the posterior probability is the adjusted probability because some regions do not contain the missing submersible. Based on the Poisson distribution function, 𝑝(𝐴) can be written as the expression as Equation 34.

<!-- b000666 | prose | pages [19] -->
𝑝(𝐴) = 𝑒−𝜆𝑡𝜆𝑡𝑟

<!-- b000667 | prose | pages [19] -->
(34) 𝑟!

<!-- b000668 | prose | pages [19] -->
Where 𝑟is the Manhattan distance between the calculated grid to the current central grid and 𝜆𝑡is the intensity parameter corresponding to the beginning of the current time interval. Furthermore, event A, in which the submersible is in one grid, is the subset of event B, in which the submersible is not in all the searched areas, which means 𝑝(𝐵|𝐴) in this problem equals 1. Then, the final posterior probability can be simplified as Equation 35.

<!-- b000669 | prose | pages [19] -->
𝑝(𝐴|𝐵) = 𝑒−𝜆𝑡𝜆𝑡𝑟

<!-- b000670 | prose | pages [19] -->
(35) 𝑟! · 𝑝(𝐵)

<!-- b000671 | prose | pages [19] -->
Where 𝑝(𝐵) is the total prior probability of all searched grids. It is easy to learn that 𝑝(𝐵) tends to decrease as more and more regions have been sought.

<!-- b000672 | furniture | pages [19] -->
关注数学模型

<!-- b000673 | furniture | pages [19] -->
2

<!-- b000674 | furniture | pages [19] -->
MATHmodels

<!-- b000675 | furniture | pages [19] -->
获取更多资讯

<!-- b000676 | furniture | pages [20] -->
Team #2407038

<!-- b000677 | prose | pages [20] -->
7.4

<!-- b000678 | heading | pages [20] -->
Results and Analysis

<!-- b000679 | furniture | pages [20] -->
Page 19

<!-- b000680 | prose | pages [20] -->
To measure the efficiency of search action, we can draw the accumulated probability of discovering the submersible with respect to time. Since we assume that the probability of a submersible in one region is

<!-- b000681 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000682 | prose | pages [20] -->
uniformly distributed, the plot should be a line chart, and the projection length of each line segment on the t-axis is equal to the time interval length.

<!-- b000683 | prose | pages [20] -->
We randomly select a missing point in the sea and use Python to calculate the probability accumulation results. Table 9 shows some key parameter settings.

<!-- b000684 | caption | pages [20] -->
Table 9: Key Parameters to calculate the probability

<!-- b000685 | prose | pages [20] -->
𝑡0 𝑡𝑖𝑛𝑡𝑒𝑟 20 min 30 min m n 0.2 10

<!-- b000686 | prose | pages [20] -->
Where 𝑡0 is the minimum for the rescue vessel to prepare and arrive at the target position, 𝑡𝑖𝑛𝑡𝑒𝑟is the time interval for a vessel to search for a 𝑚is a coefficient that influences the central grid probability, and 𝑛 is the number of rescue vessels. The accumulation probability in 5 hours or 50 hours is shown in Figure 10(a) and 10(b).

<!-- b000687 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000688 | prose | pages [20] -->
(a) Accumulated Probability in 5 Hours (b) Accumulated Probability in 50 Hours

<!-- b000689 | caption | pages [20] -->
Figure 10: Accumulated Probability of Finding a Submersible in 5 or 50 Hours

<!-- b000690 | prose | pages [20] -->
Comparing the two figures above, the accumulated finding probability is 0.5504 after the official search and rescue operation starts for 5 hours and 0.7160 after the official search and rescue operation starts for 50 hours. This means we should grab the earliest opportunity to search for the submersible because the possible range of the submersible will become larger as time passes. The growth speed of the accumulated successful searching probability will sharply decrease.

<!-- b000691 | prose | pages [20] -->
Additionally, some parameters will influence the overall trend of the accumulated probability. For example, a higher preparation time required will decrease the initial probability because the golden search and rescue time has been wasted. The number of rescue vessels and the time interval to search for one region are also significant. They will influence the total probability accumulated in a fixed period.

<!-- b000692 | prose | pages [20] -->
8

<!-- b000693 | heading | pages [20] -->
Expansion of the Model

<!-- b000694 | prose | pages [20] -->
8.1

<!-- b000695 | heading | pages [20] -->
Model Applied in Different Areas

<!-- b000696 | prose | pages [20] -->
To examine the model’s scalability, we attempt to apply it to the Caribbean Sea. Different seas mean different current distributions and seafloor topographies. So, the trajectory of the missing submersible will differ due to these factors. We utilize the current velocity data and seafloor topography data of the Caribbean Sea to simulate the model in Part 5 again to predict the trajectory of a submersible without propulsion. The trajectory is shown in Figure 11 as follows.

<!-- b000697 | furniture | pages [20] -->
关注数学模型

<!-- b000698 | furniture | pages [20] -->
2

<!-- b000699 | furniture | pages [20] -->
MATHmodels

<!-- b000700 | furniture | pages [20] -->
获取更多资讯

<!-- b000701 | furniture | pages [21] -->
Team #2407038

<!-- b000702 | furniture | pages [21] -->
Page 20

<!-- b000703 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000704 | caption | pages [21] -->
Figure 11: Motion Trajectory of a Submersible in the Caribbean Sea

<!-- b000705 | prose | pages [21] -->
From the figure, it can be seen that the trajectory is mainly along the x-axis. According to [9], the ocean current in the Caribbean Sea mainly flows from east to west, corresponding to our figure’s real situation. This means the model can be applied to other sea areas and predict the movement trend of a submersible.

<!-- b000706 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000707 | prose | pages [21] -->
8.2 Rescue of Multiple Submersibles

<!-- b000708 | prose | pages [21] -->
When preparing for search and rescue operations, a worse case to consider is the simultaneous loss of multiple submersibles. When this situation happens, we should consider how to allocate our limited number of search and rescue vessels. We still base the strategy on the region with a higher probability. It can be assumed that all of the missing submersibles are independent of each other, and The significance of each is the same. Therefore, at the beginning of each time interval, we should calculate the total probability of all the submersibles in each region, representing the expected number of s in this region. The remaining model details do not need to be modified. Part 7 offers more information. If we consider three missing submersibles simultaneously in a close area, the accumulated probability figure is shown in Figure 12.

<!-- b000709 | caption | pages [21] -->
Figure 12: Accumulated Probability of Three Submersibles Separately

<!-- b000710 | prose | pages [21] -->
From the figure, we can see the probability of successful search and rescue for each submersible is lower than that when only one submersible is lost. This is because the total number of rescue vessels is fixed, and they need to consider several submersibles. Theoretically, the farther the missing submersibles are from each other, the lower the probability of each submersible being rescued because the probability distribution overlap will be fewer.

<!-- b000711 | prose | pages [21] -->
Considering the probability of each submersible being rescued, the difference is obvious. This is due to the strategic allocation of rescue prime time, making it difficult to achieve fairness for every submersible. We can only make the model reach the global optimal solution. Detailed adjustment requires more complex algorithms to realize.

<!-- b000712 | furniture | pages [21] -->
关注数学模型

<!-- b000713 | furniture | pages [21] -->
2

<!-- b000714 | furniture | pages [21] -->
MATHmodels

<!-- b000715 | furniture | pages [21] -->
获取更多资讯

<!-- b000716 | furniture | pages [22] -->
Team #2407038

<!-- b000717 | prose | pages [22] -->
9

<!-- b000718 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000719 | furniture | pages [22] -->
Page 21

<!-- b000720 | prose | pages [22] -->
In section 7.3, several parameters can influence the final accumulated probability.

<!-- b000721 | prose | pages [22] -->
Among these parameters, the time interval, the ability of the rescue vessel to search for a region with a certain area, is

<!-- b000722 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000723 | prose | pages [22] -->
significant because it decides how the vessel can take advantage of the golden search and rescue time to explore more areas. Then, we choose this parameter to analyze its sensitivity. The percentage of parameter change is shown in Table 10 below, and the analysis results are shown in the figures following the table.

<!-- b000724 | caption | pages [22] -->
Table 10: Test Time Interval Summary

<!-- b000725 | prose | pages [22] -->
Percentage change Standard -10% -5% 5% 10% 27 min Time interval 30 min 28.5 min 31.5 min 33 min

<!-- b000726 | caption | pages [22] -->
Figure 13 indicates that whether the value of the time interval increases or decreases, the final accu-

<!-- b000727 | prose | pages [22] -->
mulated probability will not have a large difference. In other words, the model is not very sensitive to this parameter.

<!-- b000728 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000729 | caption | pages [22] -->
Figure 13: Accumulated Probability and Deviation under Different Time Intervals

<!-- b000730 | prose | pages [22] -->
Ultimately, if the time interval increases by 10%, there will be a relatively large deviation compared with the standard value. If the rescue vessel spends too much time searching for one grid, it is more likely to waste the prime time and cause a lower probability of a successful rescue.

<!-- b000731 | furniture | pages [22] -->
关注数学模型

<!-- b000732 | furniture | pages [22] -->
2

<!-- b000733 | furniture | pages [22] -->
MATHmodels

<!-- b000734 | furniture | pages [22] -->
获取更多资讯

<!-- b000735 | furniture | pages [23] -->
Team #2407038

<!-- b000736 | heading | pages [23] -->
Memo

<!-- b000737 | furniture | pages [23] -->
Page 22

<!-- b000738 | prose | pages [23] -->
To: Greek Government Regulatory Authorities

<!-- b000739 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000740 | prose | pages [23] -->
From: Team 2407038 Date: 2024.2.5

<!-- b000741 | prose | pages [23] -->
Approval for Maritime Cruises Mini-Submarines (MCMS) - Safety

<!-- b000742 | heading | pages [23] -->
Procedures and Models

<!-- b000743 | heading | pages [23] -->
I. Introduction

<!-- b000744 | prose | pages [23] -->
Maritime Cruises Mini-Submarines (MCMS) wishes to utilize their submersibles for tourist adventures exploring the Ionian Sea’s depths, focusing on sunken shipwrecks. However, the ongoing exploration of the deep sea is marked by frequent underwater accidents. To ensure possible accidents and fast response for

<!-- b000745 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000746 | prose | pages [23] -->
rescue, the objective is to design a model for location prediction, safety procedures, and rescue strategies to address potential safety concerns, specifically loss of communication and mechanical defects.

<!-- b000747 | heading | pages [23] -->
II. Predictive Location Model

<!-- b000748 | heading | pages [23] -->
Locate - Trajectory Prediction Model Based on Dynamics Analysis

<!-- b000749 | prose | pages [23] -->
The submersible must carry essential equipment to collect crucial data during communication failure, ensuring swift and accurate rescue operations to prevent potential tragedies. Considering factors including ocean currents, resistance variations, seawater density, and seafloor geography, we have established a dynamics-based trajectory prediction model. In the trajectory prediction model, they must consistently relay crucial data to the mother ship to enhance precision and reduce model uncertainties. Therefore, they should be equipped with advanced monitoring tools, including:

<!-- b000750 | prose | pages [23] -->
i) Equipment for ocean current detection and seawater condition monitoring (such as Acoustic Doppler

<!-- b000751 | prose | pages [23] -->
Current Profile and Conductivity, Temperature, and Depth (CTD) sensors);

<!-- b000752 | prose | pages [23] -->
ii) A Dynamics and External Resistance Monitoring System (Inertial Navigation System), and

<!-- b000753 | prose | pages [23] -->
iii) Communication and Data Logging Equipment (Underwater Acoustic Communication Devices, Data

<!-- b000754 | prose | pages [23] -->
Loggers, Satellite Communication Systems).

<!-- b000755 | heading | pages [23] -->
III. Search Equipment Recommendations

<!-- b000756 | heading | pages [23] -->
Prepare - Recommendation Based on Multi-Objective Optimization

<!-- b000757 | prose | pages [23] -->
Consideration is given to the costs associated with the search equipment’s availability, maintenance, readiness, and usage. Five categories of search equipment are considered for both host ship and rescue vessels. A reasonable equipment allocation plan is shown in the following Table .

<!-- b000758 | prose | pages [23] -->
ES ✓ Host Ship × Primary Rescue Boats I × Primary Rescue Boats II × Intermediate Rescue Boats SSS PL MM OI Cost ✓ ✓ ✓ ✓ 215000 ✓ × × × 50000 ✓ ✓ × × 65000 ✓ ✓ ✓ × 150000

<!-- b000759 | prose | pages [23] -->
Note: ES stands for Echo Sounder, SSS stands for Side Scan Sonar, PL stands for

<!-- b000760 | furniture | pages [23] -->
关注数学模型

<!-- b000761 | prose | pages [23] -->
Pinger Locators, MM stands for Magnetometer, and OI stands for Optical Imaging.

<!-- b000762 | furniture | pages [23] -->
2

<!-- b000763 | furniture | pages [23] -->
MATHmodels

<!-- b000764 | furniture | pages [23] -->
获取更多资讯

<!-- b000765 | furniture | pages [24] -->
Team #2407038

<!-- b000766 | furniture | pages [24] -->
Page 23

<!-- b000767 | prose | pages [24] -->
The implementation of this 1 + 𝑛rescue scheme, through hierarchical organization and task allocation optimization, not only improves the response speed and efficiency of rescue operations but also strengthens the adaptability to rescue needs under different maritime conditions and situations. Ultimately, this strategy ensures more efficient and precise search and rescue actions, providing quicker and more effective rescue

<!-- b000768 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000769 | prose | pages [24] -->
services for those trapped in maritime emergencies.

<!-- b000770 | heading | pages [24] -->
IV. Search Model

<!-- b000771 | prose | pages [24] -->
Search – Grid Probability Search Technique When the submersible went lost, the following search strategy is established to minimize the search time:

<!-- b000772 | prose | pages [24] -->
• Acquire the possible location using the Predictive Location Model

<!-- b000773 | prose | pages [24] -->
• Properly rasterize the search region

<!-- b000774 | prose | pages [24] -->
• Identify the Centre Search Grid and assign a probability to each grid

<!-- b000775 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000776 | prose | pages [24] -->
• Update the Centre Search Grid by time till the objective searched

<!-- b000777 | heading | pages [24] -->
V. Extrapolation for Other Destinations

<!-- b000778 | prose | pages [24] -->
Extrapolate - Expand the model to account for other tourist destinations.

<!-- b000779 | heading | pages [24] -->
1. Adaptation for Other Destinations:

<!-- b000780 | prose | pages [24] -->
The model can be used in various incident areas, incorporating regional variations in sea conditions and topography. We try to transfer the model to the Caribbean Sea in this context. The ocean currents in the Caribbean Sea predominantly move from east to west, aligning with our simulation results, which indicates the model’s applicability to other sea areas and its capability to predict the movement trends of submersibles.

<!-- b000781 | heading | pages [24] -->
2. Multiple Submersibles:

<!-- b000782 | prose | pages [24] -->
The model will update by overlaying each grid probability when the simultaneous loss of multiple s is considered. Therefore, only small changes need to be made to our model to copy with multiple submersible scenarios.

<!-- b000783 | heading | pages [24] -->
VI. Conclusion

<!-- b000784 | prose | pages [24] -->
The proposed safety procedures, predictive models, and equipment recommendations aim to ensure the secure and efficient operation of MCMS submersibles. We request the Greek Government’s support and approval for implementing these measures, emphasizing the importance of responsible and exciting underwater tourism.

<!-- b000785 | prose | pages [24] -->
Thank you for your attention and consideration!

<!-- b000786 | prose | pages [24] -->
Sincerely.

<!-- b000787 | furniture | pages [24] -->
关注数学模型

<!-- b000788 | furniture | pages [24] -->
2

<!-- b000789 | furniture | pages [24] -->
MATHmodels

<!-- b000790 | furniture | pages [24] -->
获取更多资讯

<!-- b000791 | furniture | pages [25] -->
Team #2407038

<!-- b000792 | heading | pages [25] -->
References

<!-- b000793 | furniture | pages [25] -->
Page 24

<!-- b000794 | references | pages [25] -->
[1] “List of submarine and submersible incidents since 2000,” Wikipedia, 10 2023. [Online]. Available:

<!-- b000795 | references | pages [25] -->
https://en.wikipedia.org/wiki/List of submarine and submersible incidents since 2000

<!-- b000796 | references | pages [25] -->
微信公众号：数学模型

<!-- b000797 | references | pages [25] -->
[2] C. Deng, B. Zhao, M. Yang, and Y. Zhao, “Simulation research of full-ocean-depth manned submersible

<!-- b000798 | references | pages [25] -->
based on experimental data,” in 2022 IEEE International Conference on Electrical Engineering, Big

<!-- b000799 | references | pages [25] -->
Data and Algorithms (EEBDA), 2022, pp. 468–471.

<!-- b000800 | references | pages [25] -->
[3] D. Li, Q. Zhao, C. He, S. Yang, C. Peng, L. Wang, and W. Zhang, “Motion simulation calculation and

<!-- b000801 | references | pages [25] -->
test verification of deep sea manned submersi,” SHIP SCIENCE AND TECHNOLOG, vol. 43, no. 11,

<!-- b000802 | references | pages [25] -->
pp. 62–65, 6 2021.

<!-- b000803 | references | pages [25] -->
[4] P.

<!-- b000804 | references | pages [25] -->
Yao,

<!-- b000805 | references | pages [25] -->
L.

<!-- b000806 | references | pages [25] -->
Qiu,

<!-- b000807 | references | pages [25] -->
J.

<!-- b000808 | references | pages [25] -->
Qi,

<!-- b000809 | references | pages [25] -->
and

<!-- b000810 | references | pages [25] -->
R.

<!-- b000811 | references | pages [25] -->
Yang,

<!-- b000812 | references | pages [25] -->
of

<!-- b000813 | references | pages [25] -->
static

<!-- b000814 | references | pages [25] -->
target

<!-- b000815 | references | pages [25] -->
in

<!-- b000816 | references | pages [25] -->
ocean

<!-- b000817 | references | pages [25] -->
environment,”

<!-- b000818 | references | pages [25] -->
“Auv

<!-- b000819 | references | pages [25] -->
path

<!-- b000820 | references | pages [25] -->
planning

<!-- b000821 | references | pages [25] -->
for

<!-- b000822 | references | pages [25] -->
coverage

<!-- b000823 | references | pages [25] -->
search

<!-- b000824 | references | pages [25] -->
Ocean

<!-- b000825 | references | pages [25] -->
Engineering,

<!-- b000826 | references | pages [25] -->
2021.

<!-- b000827 | references | pages [25] -->
[Online].

<!-- b000828 | references | pages [25] -->
Available:

<!-- b000829 | references | pages [25] -->
https://api.semanticscholar.org/CorpusID:240130096

<!-- b000830 | references | pages [25] -->
微信号：MATHmodels

<!-- b000831 | references | pages [25] -->
[5] J. Li, C. Li, T. Chen, and Y. Zhang, “Improved rrt algorithm for auv target search in unknown 3d

<!-- b000832 | references | pages [25] -->
environment,” Journal of Marine Science and Engineering, vol. 10, no. 6, 2022. [Online]. Available:

<!-- b000833 | references | pages [25] -->
https://www.mdpi.com/2077-1312/10/6/826

<!-- b000834 | references | pages [25] -->
[6] G. E. P. Box and G. M. Jenkins, “Time series analysis : forecasting and control,” Journal of Time,

<!-- b000835 | references | pages [25] -->
vol. 31, no. 3, 2010.

<!-- b000836 | references | pages [25] -->
[7] U. S. Military, “U.s. navy ship salvage manual volume 4 (deep ocean operations) published by

<!-- b000837 | references | pages [25] -->
direction of commander, naval sea systems command distribution statement a: This document ha

<!-- b000838 | references | pages [25] -->
s been approved for public relea se and sale; its distribution is unlimited,” www.navy.mil, 1993.

<!-- b000839 | references | pages [25] -->
[Online]. Available: https://www.navsea.navy.mil

<!-- b000840 | references | pages [25] -->
t-ars,”

<!-- b000841 | references | pages [25] -->
[8] “Rescue

<!-- b000842 | references | pages [25] -->
and

<!-- b000843 | references | pages [25] -->
salvage

<!-- b000844 | references | pages [25] -->
ships

<!-- b000845 | references | pages [25] -->
www.navy.mil.

<!-- b000846 | references | pages [25] -->
[Online].

<!-- b000847 | references | pages [25] -->
Avail-

<!-- b000848 | references | pages [25] -->
https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2232627/rescue-and-

<!-- b000849 | references | pages [25] -->
able:

<!-- b000850 | references | pages [25] -->
salvage-ships-t-ars/

<!-- b000851 | references | pages [25] -->
[9] P.

<!-- b000852 | references | pages [25] -->
Richardson,

<!-- b000853 | references | pages [25] -->
“Caribbean

<!-- b000854 | references | pages [25] -->
current

<!-- b000855 | references | pages [25] -->
and

<!-- b000856 | references | pages [25] -->
Deep

<!-- b000857 | references | pages [25] -->
eddies

<!-- b000858 | references | pages [25] -->
as

<!-- b000859 | references | pages [25] -->
observed

<!-- b000860 | references | pages [25] -->
by

<!-- b000861 | references | pages [25] -->
surface

<!-- b000862 | references | pages [25] -->
drifters,”

<!-- b000863 | references | pages [25] -->
Sea Research Part II: Topical Studies in Oceanography,

<!-- b000864 | references | pages [25] -->
2005, direct observations of oceanic flow:

<!-- b000865 | references | pages [25] -->
vol. 52,

<!-- b000866 | references | pages [25] -->
no. 3,

<!-- b000867 | references | pages [25] -->
pp. 429–463,

<!-- b000868 | references | pages [25] -->
A tribute to Walter Zenk. [Online]. Available:

<!-- b000869 | references | pages [25] -->
https://www.sciencedirect.com/science/article/pii/S0967064504003029

<!-- b000870 | furniture | pages [25] -->
关注数学模型

<!-- b000871 | furniture | pages [25] -->
2

<!-- b000872 | furniture | pages [25] -->
MATHmodels

<!-- b000873 | furniture | pages [25] -->
获取更多资讯
