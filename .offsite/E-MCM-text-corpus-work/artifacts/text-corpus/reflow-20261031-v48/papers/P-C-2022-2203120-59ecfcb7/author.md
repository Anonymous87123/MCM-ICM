Problem Chosen 2022

MCM/ICM

Summary Sheet

Summary

It is of great signiﬁcance for traders to buy and sell volatile assets reasonably in market transactions. Traders choose diﬀerent trading strategies and get diﬀerent beneﬁts. This paper studies the best trading strategies for diﬀerent traders based on the daily prices of gold and bitcoin in the past.

For problem 1, the original data is preprocessed ﬁrstly, including ﬁlling the missing value by the daily price of gold in the past, and standardize all the original data. Following the processed data, the ARIMA model is used to establish the price prediction model. Correlation coeﬃceents between the prediction results and the price of gold and bitcoin are 0.8592 and 0.9304 respectively. The eﬀectiveness of our model is denoted. Thirdly, a dynamic programming model with largest total assets and risk as the regular termis is established, with the constraints hit rate and transaction volume limit. Lastly, the optimal daily trading strategy is solved with dynamic programming method. Final proﬁt is $ 132089.1078 on September 10, 2021.

For problem 2, we prove our strategy is the best judged from the generalization ability, robustness and beneﬁt of the model. By adjusting the variable parameters in the model, the strategies suitable for three traders are formed, which are insurance type, common type and radical type. The solution method of problem 1 is used to obtain the changes of each asset and the total earnings of the three trading strategies. Furthermore, the variable parameters in the model are disturbed, and the total assets change within a certain range, indicating that the model has strong anti-interference ability. Finally, the assets obtained by the three types of trading strategies are $14312.6827, $50040.5474 and $132089.1078 respectively. It can be seen that our model yield can resist inﬂation greatly.

For problem 3, ﬁrstly, the sensitivity is deﬁned as the change rate of transaction frequency. By changing the transaction cost of gold and bitcoin, it is calculated that the sensitivity of gold transaction cost is 0.0422 and that of bitcoin transaction cost is 0.0658. It can be seen from the comparison that the transaction strategy is more sensitive to the transaction cost of bitcoin. Secondly, the impact of transaction cost on transaction frequency, asset return and asset risk are analyzed. We ﬁnd that when the transaction cost increases, the transaction frequency, asset return and asset risk are decreases correspondingly.

For problem 4, we summarize the models and strategies established in the ﬁrst three questions, and introduce to traders in the form of memorandum how to simply use the trading strategy to trade and the beneﬁts brought by diﬀerent trading strategies.

1 Introduction

1.1 Problem Background

Market traders buy and sell volatile assets frequently, with a goal to maximize their total return. There is usually a commission for each purchase and sale. Two such assets are gold and bitcoin.The price changes of bitcoin and gold from September 11, 2016 to September 10, 2021 are shown in

bitcoin daily prices is NASDAQ.

(a) Gold daily prices, U.S. dollars per troy ounce (b) Bitcoin daily prices, U.S. dollars per bitcoin

1.2 Restatement of the Problem

In this problem, we are asked by a trader to develop a model that uses only the past stream of daily prices to date to determine each day if the trader should buy, hold, or sell their assets in their portfolio. We will start with $1000 on September 11, 2016 and use the ﬁve-year trading period, from September 11, 2016 to September 10, 2021. On each trading day, the trader will have a portfolio consisting of cash, gold, and bitcoin [C, G, B] in U.S. dollars, troy ounces, and bitcoins, respectively.We should only use these data to solve the following problems:

• Develop a model that gives the best daily trading strategy based only on price data up to that day. Use the model and strategy to predict the value of the initial $1000 investment on September 10, 2021.

• Present evidence that the model provides the best strategy.

• Determine how sensitive the strategy is to transaction costs and how transaction costs aﬀect the strategy and results.

• Communicate the strategy, model, and results to the trader in a memorandum of at most two pages.

1.3 Problem Analysis

For problem 1, The premise of formulating the strategy is to accurately predict the price trend of gold and bitcoin in the future. Therefore, it is necessary to establish a price prediction model to lay the foundation for formulating the strategy. Common time series prediction models include LSTM, BP neural network, RNN, encoder-decoder model, etc. In view of the simplicity and eﬃciency of ARIMA model, which only needs endogenous variables rather than other exogenous variables, we choose to use ARIMA model.

Next, establish a trading strategy model according to the established indicators, give the trading strategy and calculate the ﬁnal income. Intuitively, the price ﬂuctuation of bitcoin is much greater than that of gold, so we guess the risk is greater than that of gold. Therefore, the risk of investment can be described by the variance of price change. This is essentially a dynamic programming problem. We can quantify the return and risk, take the maximum beneﬁt as the objective function, ﬁnd the constraints and establish the model.

With regard to problem 2, The optimization of the model can be proved from three aspects: generalization ability, robustness and proﬁt. The generalization ability of the model is reﬂected in that changing the parameters in the model can make the model formulate diﬀerent kinds of strategies. Therefore, we divide the strategies into insurance type, common type and radical type. The robustness of the model means that small changes in parameters will not aﬀect the overall strategy, and the anti-interference of the model is strong. It also shows that compared with other investments, our strategy has a better rate of return.

As for problem 3, It is known that the transaction cost is the Commission. Intuitively, the increase of commission should appropriately reduce the transactions. The decrease of commission can increase the number of transactions. The ultimate goal is to maximize the income. Based on the transaction strategy model established by the ﬁrst question, by changing the cost α in the model and observing the corresponding changes of transaction frequency, asset return and asset risk, we can get the sensitivity of three types of strategies to transaction cost.

2 General Assumptions and Notations

2.1 Assumptions

To simplify our problems, we make the following basic assumptions, each of which is adequately justiﬁed.

• All data are authentic.

• The investor is physically and mentally healthy and has no burden such as huge loans.

• Without considering inﬂation and other economic changes in recent years, only tabular data are used.

• All transactions are conducted in US dollars. The commission is deducted from the amount paid instead of being given separately.

• Since it is only US $1000, the minimum transaction unit of US dollar and bitcoin under normal circumstances is not considered for the universality of the model.

2.2 Notations

In this work, we use the nomenclature in Table 1 in the model construction. Other none- frequent-used symbols will be introduced once they are used.

Symbols Descripition

t1 = 3, t2 = 3 gold trading cycle (including holidays), bitcoin trading cycle n number of cycles in ﬁve years DSgi, DSbi hit rate of training prediction model, i=2,3...n Ri = [Ci Gi Bi] asset distribution in the i-th cycle, R0 = [1000 0 0] Ai total assets in the i-th cycle, A0=1000 qi proportion of cash in total assets in the i-th cycle ei, fi threshold of increase or decrease in the i-th cycle Xg(i), Xb(i) forecast average price in the i-th cycle Yg(i), Yb(i) real average price of gold in the i-th cycle αg, αb proportion of commission of each transaction in the transaction amount R2 gi, R2 decision coeﬃcient of the trained model in the i-th cycle bi

3 Problem 1: Prediction and Strategy in the Investment

In this section, based on the existing data, we use ARIMA model to predict the price trend of gold and bitcoin in the future, so as to establish a model and give the best daily trading strategy. Dynamic programming is used to estimate the value of the initial $1000 investment by September 10, 2021.

3.1 Data Preprocessing

Before data analysis, the availability of data must be guaranteed.

• Missing value processing. Unlike bitcoin, which is traded daily, gold is traded only on trading days, so the data is not continuous. For the convenience of subsequent modeling, the missing value is ﬁlled with the mean value before and after the day.

• Data standardization. In regression prediction, standardization gives eigenvalues equal weight. Since we predict by period, we process the data by period. Calculate the mean(¯x) and standard deviation(SD) of data(x), then the processed data x′ = (x−¯x) SD .

3.2 Model Establishment of Problem 1

3.2.1 Price Prediction Model

Improving forecasting especially time series forecasting accuracy is an important yet often diﬃcult task facing decision makers in many areas. Autoregressive integrated moving average (ARIMA) models are one of the most popular linear models in time series forecasting, which have been widely applied in order to construct more accurate hybrid models during the past decade [2].

ARIMA model combines three basic methods:

• Autoregressive(AR). Describe the relationship between the current value and the historical value, and use the historical time data of the variable to predict itself. The order of AR model is recorded as p value.The formula is as follows:

yt = α0 + α1yt−1 + α2yt−2 + · · · + αpyt−p + ϵt (1)

where, and α is the coeﬃcient, ϵt stands for error.

• Integrated(I). When the time series becomes stationary, the diﬀerence needs to be made, and the order of the diﬀerence is recorded as d value. Generally, ﬁrst order is enough.

• Moving average(MA). Moving average model focuses on the accumulation of error terms in autoregressive model. The order of MA model is recorded as q value.The formula is as follows:

yt = c + ϵt + θ1ϵt−1 + θ2ϵt−2 + · · · + θqϵt−q (2)

where, c represents the constant term, ϵt is the white noise process of variance, and θ is the coeﬃcient.

The model is called ARIMA (p, d, q), as shown in the ﬁgure3, where p is the autoregressive term, q is the moving average term, and D is the number of diﬀerences. We will follow the steps listed below to build and solve our model.

step1 Stabilization To use ARIMA model, the time series must be stationary. We use the Augmented Dickey- fuller unit root test to test the stationarity. If the P value obtained from ADF test is less than 0.05, it is a stable time series. If it is unstable, we convert the non-stationary process into a stationary process by diﬀerence method. It can be seen from the table 2 that the time series becomes stable after the ﬁrst-order diﬀerence.

P value before diﬀerence P value after diﬀerence

gold 0.6734 0.0043 bitcoin 0.9921 0.0000

step2 Selection of p and q Use autocorrelation function(ACF) and partial autocorrelation function(PACF) to determine the values of p and q. the conﬁrmation method is shown in the table 3.

Model ACF PACF

AR(P) attenuation tends to 0 truncation after p-order MA(q) truncation after q-order attenuation tends to 0 ARMA(p, q) attenuation tends to 0 after q-order attenuation tends to 0 after p-order

NOTE: Truncation means falling within the conﬁdence interval (95% of the points comply with the rule)

this, we can determine the p value and q value respectively.

(a) ACF chart and PACF chart of gold (b) ACF chart and PACF chart of bitcoin

step3 White noise test If the white noise is obtained, it means that the useful information in the time series has been extracted, and the rest are all random disturbances, which cannot be predicted and used.[9] If the residual sequence passes the white noise test, the modeling can be terminated, because there is no information to continue to extract.

The ARIMA model of gold is ARIMA(2,1,1) and bitcoin is ARIMA(2,1,2). The p value of the white noise test output of this model is very close to 0, indicating that it follows the normal distribution with the mean value of 0, that is, it is a white noise.

step4 Prediction In order to predict the future market timely and accurately, we use the data of 30 consecutive days as the training set and the data of the next 3 days as the test set. The moving step of the training set is 3. The prediction results of one cycle are shown in the ﬁgure 5. The correlation coeﬃcient R2 of gold is 0.8592 and that of bitcoin is 0.9304. The prediction results of the model are relatively successful and can be used.

(a) Forecast chart of gold in one cycle (b) Forecast chart of bitcoin in one cycle

3.2.2 Trading Strategy Model

The best daily trading strategy is given only according to the price data. We need to judge the forecast data and give the strategy according to the forecast. Therefore, we deﬁne variable parameters as shown in the table 4 to quantify the strategy.

Symbols Descripition

β, γ proportion of increase or decrease DS hit rate wH, wL purchase proportion, H/L stands for a higher/lower proportion m selling proportion R2 threshold of Decision coeﬃcient R2 i q cash retention ratio

Decision coeﬃcient(R2): it is used to evaluate the volatility predicted by the model. The closer the index value is to 1, the higher the ﬁtting performance of the model.

  2 Pt xi,j −Y(i) j=1 R2 i = (3)   2 Pt yi,j −Y(i) j=1

where xi,j represents the predicted value of day j in cycle i and yi,j represents the actual value of day j in cycle iand Y(i) represents the mean of the true value in cycle i.

Hit rate(DS): it is used to evaluate the accuracy of the model in predicting the rise and fall, so as to evaluate the prediction of the long-term trend of the model.

( Xt , (xi,j+1 −xi,j) (yi,j+1 −yi,j) ⩾0 1 DSi = 1 j=1 dj × 100% ; dj = j = 1, 2, 3 (4) t 0 , else

where di represents the predicted rise and fall in cycle i. If the rise and fall of the real value is the same as that of the predicted value, it is 1, on the contrary, it is 0.

In addition, we make the following assumptions:

• The period from September 11, 2016 to November 11, 2016 is the zero cycle, and no transaction is conducted as the experience accumulation period. Since November 12, 2016 is the ﬁrst cycle, the number of cycles is n = 588.

• If the transaction starts from the second cycle, the asset situation in the ﬁrst week is the same as that in the zero cycle.

• Since gold is not traded during holidays, when the predicted value of gold price in a certain period is empty, it means that gold is not traded in that period.

• The Commission is deducted from the amount paid instead of being given separately.

We use i to record the cycle, in which cycle 0 is the experience accumulation period, which only predicts and does not trade. 3 days is a cycle. We use j to record the day. The total number of cycles is 588. Pay attention to the diﬀerence between trading days of gold and bitcoin.

To build a strategy model, we need to ﬁnd the objective function and constraints. To make more proﬁts, we need to make the risk as small as possible and the proﬁt as much as possible. Firstly, we quantify the risk and set the standard deviation of assets owned in the transaction process as the risk index S: v  2 u ∑i−1 u Pi−1 j=i−30 Ai u Ai − t j=i−30 30 Sj = (5) 30

Calculate the amount of cash:

( Ci−1 −Gi × wg , Xg(i) −Yg(i−1) > βg × Ai−1 Ci = (6) Ci−1 + Gi × mg × (1 −αg) × Yg(i+1) , Yg(i−1) −Xg(i) > γg × Ai−1 ( Ci−1 −Bi × wb , Xb(i) −Yb(i−1) > βb × Ai−1 Ci = Ci−1 + Bi × mb × (1 −αb) × Yb(i+1) , Yb(i−1) −Xb(i−1) > γb × Ai−1

Calculate the amount of gold and bitcoin:

( Gi−1 + Ci × wg × (1 −αg) Gi = (7) Gi−1 −Gi−1 × mg ( Gi−1 + Bi × wb × (1 −αb) Bi = Gi−1 −Gi−1 × mb

Then the total asset formula is:

Ai = Ci + Gi × Yg(i) + Bi × Yb(i) (8)

Finally, the objective function and constraints are determined, and the trading strategy model is obtained:

wj,mj Aj −λ × Sj max (9)   Cj, Gj, Bj, Aj ⩾0      DSj ⩾0.5  s.t. Cj ⩾Aj × q    αg = 1%, αb = 2%     A0 = 1000, C0 = C1 = 1000, G0 = G1 = B0 = B1 = 0 where, Wj represents the roportion of gold and bitcoin bought on day j, mj represents the roportion of gold and bitcoin sought on day j, Aj represents the total assets on day j, λ represents the coeﬃcient of regular term, which is used to control risk and return, Sj represents the current day risk. The ﬁrst constraint indicates that all assets are positive, the second constraint indicates that the accuracy of the model is greater than 0.5, the third constraint indicates that the remaining capital of the transaction is greater than q times of the total assets, and α indicates the transaction cost, A0, C0, G0, B0 represents the total assets, cash, gold and bitcoin before the ﬁrst day of trading, C1, G1, B1 represents the amount of cash, gold and bitcoin before trading on day 2.

3.3 Model Solving: Finding Strategies

After the trading strategy model is established, we need to solve the model. The speciﬁc steps are as follows:

step1 Datainitialization. Set i = 1, knowαg = 1%, set parameterβg, γg, ds, R2, wHg, wLg, mg, q, initial asset distributionR1 = R0 = [1000 0 0], total assets r1 = r0 = 1000.

step2 Calculate hit rate (DS). The prediction model hit rate(Formula 4) can evaluate the accuracy of the trained model in predicting the rise and fall. When the accuracy is high enough, you can continue to follow the next steps.

step3 Determine whether to trade. Firstly, due to the cost in the transaction, in order to avoid excessive cost caused by frequent transaction, the transaction is carried out only when the increase and decrease reach a certain threshold. Secondly, in order to avoid too little cash left in the transaction, the transaction can be carried out only when the cash meets the reserved amount. The speciﬁc process is shown in the ﬁgure 6.

where, eg(i+1) = βg × Ai (10) fg(i+1) = γg × Ai (11) Ci qi = (12) Ci + Gi × Yg(i) + Bi × Yb(i) in the formula, βg, γg represents the proportion of increase or decrease.

step4 Determine the number of transactions. Prediction model discrimination coeﬃcient R2 gi can evaluate the volatility predicted by the trained model. The smaller the variable, the more stable the model is, and the proportion of buying gold during trading can be increased. The speciﬁc process is shown in the ﬁgure 7.

Where, the formula for total assets is

Ai+1 = Ci+1 + Gi+1 × Yg(i+1) + Bi+1 × Yb(i+1) (13)

When proportions WHg, WLg and mg are used respectively, the formula for calculating asset distribution is  Ci+1 = Ci −Ci × wLg   Gi+1 = Gi + Ci×wLg×(1−αg) RWHg = (14) Yg(i+1)   Bi+1 = Bi  Ci+1 = Ci −Ci × wHg   Gi+1 = Gi + Ci×wHg×(1−αg) RWLg = (15) Yg(i+1)   Bi+1 = Bi  Ci+1 = Ci −Ci × wLg   Gi+1 = Gi + Ci×wLg×(1−αg) Rmg = (16) Yg(i+1)   Bi+1 = Bi In the formula, Yg(i+1) represents the real average price of gold on (i+1) day.

3.4 Results and Model Evaluation

3.4.1 Model Results

Using Python Programming and our model, set variable parameters: βb = 0, βg = 0.5, γb = 0.3, γg = 0.3, wHg = 0.8, wHb = 0.4, q = 0.01, the initial investment value of $1000 will be $132089.11 by September 10, 2021. The number of transactions is 9, and the ﬁnal asset distribution [C,G,B]=[22.31, 0.16, 2.84]. The changes of assets during the ﬁve-year period are shown in the ﬁgure below.

3.4.2 Model Evaluation

This result is obtained using two models. Firstly, ARIMA model is used for prediction, and we get good results: The correlation coeﬃcient R2 of gold is 0.8592 and that of bitcoin is 0.9304. They are close to 1, indicating that the predicted value is highly correlated with the real value.

Through the trading strategy model, we get speciﬁc beneﬁts. The strategy model has high availability:

• The model is only based on the price changes of gold and bitcoin in recent ﬁve years, so the model has low requirements for data.

• Our model puts forward variable parameters such as β, γ, wH, wL, m, q to form a parameter list. By changing the parameters in the list, we can achieve diﬀerent income results. In the future, we can form an investment prediction software according to the model. We only need to understand the meaning of relevant parameters to realize asset management. Therefore, our model is relatively simple and easy to understand.

• The parameters in the model have a large variable range and are more ﬂexible.

These ensures the reliability of the results.

4 Problem 2: Prove Optimization of the Strategy

Our model proposes multiple variable parameters, which can achieve diﬀerent beneﬁts by changing parameters, so the model has good generalization ability. At the same time, the small change of parameters will not aﬀect the overall strategy, and the model is robust. Compared with other investments, our strategy has a better rate of return. The following will explain the generalization ability, robustness and proﬁt margin of the model to prove the optimization of the strategy.

4.1 Generalization Ability of the Model

Successful investment comes from two factors: one is traders’ correct understanding of the market, and the other is trading rationality. According to the reference materials[7], we divide traders into the following three types:

• Insurance-type. The purpose of such traders’ investment behavior is mainly to obtain long- term capital income, that is, they hope to obtain investment income regularly, and also hope to obtain diﬀerential proﬁts through the change of capital price in a longer term. At the same time, before investing, traders should generally master suﬃcient information and make a rational analysis of the expected proﬁts and risks of the target assets.

• Common-type. The purpose of such traders is mainly to obtain large proﬁts in a short period of time and are willing to bear some risks. Its way mainly depends on the short-term price ﬂuctuation diﬀerence to obtain proﬁts. They take technical analysis as the main means and make speculative decisions based on historical price ﬂuctuation experience. Generally speaking, the probability of success of Common-type investors is not low, but the probability of failure is also high. Its behavior has strong subjective initiative, and the probability of success depends on its accuracy in predicting market ﬂuctuations.

• Radical-type. The characteristics of radical traders’ behavior are based on luck and oppor- tunity, trading in the market with luck and hoping to make huge proﬁts in the short term.

Generally speaking, the risk is very high. Unless they need money urgently, have the psy- chology of gamblers or have the ability to take risks, most people will not use this investment method.

In the model, for three types of traders, the corresponding parameters are adjusted as shown in the

variable parameters Insurance-type Common-type Radical-type

βb 0.35 0.10 0 βg 0.50 0.50 0.50 γg 0.10 0.20 0.30 γb 0.10 0.20 0.30 wHg 0.95 0.80 0.80 wHb 0.15 0.30 0.40 q 0.15 0.05 0.01

Solve the model according to diﬀerent parameters adjustments and get the changes of various types of traders’ assets. The ﬁgure 9 shows the changes of various assets of insurance-type traders in ﬁve years. See the Appendix A for the ﬁgures of the other two types.

(a) Changes of cash (b) Changes of gold (c) Changes of bitcoin

The changes of total assets of three types of traders are shown in the ﬁgure 10:

(a) Insurance-type (b) Common-type (c) Radical-type

Insurance-type Common-type Radical-type

Total assets 14312.68 50040.55 132089.11 [C, G, B] [11474.39, 1.59, 1.07] [421.14, 0.61, 1.05] [22.31, 0.16, 2.84] Number of transactions 85 58 9 SD 3861.73 15501.99 40067.35 R2 0.94 0.27 0.24 g R2 0.41 0.98 0.99 b

NOTE: R2 g/R2 b represent correlation between gold/bitcoin purchase and actual ﬂuctuation, SD represent standard deviation of 5-year assets.

Reading the data in the table 8, although radical investors have more returns, the value of SD is very large, that is, assets change greatly, so they have to bear corresponding risks. It can be seen from the number of transactions that any disturbance in the market may disturb insurance investors. From R2, we can ﬁnd that the more traders tend to venture capital, the more they will buy bitcoin; Gold symbolizes stable and conservative investment. Thus, our model gives a variety of practical and feasible strategies.

4.2 Robustness of the Model

In practical problems, the perturbation of system characteristics or parameters is often inevitable. The good robustness of the model means that the model has strong anti-interference ability, which means that the system has the ability to maintain a certain performance under the disturbance of uncertainty. As shown in the ﬁgure 11, ﬁgure 12, ﬁgure 13, they show the changes of total assets when disturbing the WH, WL and M parameters of gold and bitcoin respectively.

(a) gold (b) bitcoin

(a) gold (b) bitcoin (a) gold (b) bitcoin

As can be seen from the ﬁgure above, if these variables are disturbed, the ﬁnal income of the model is stable within a certain range. In fact, if the other parameters β, γ, q are disturbed, the ﬁnal return and investment risk of the model are stable within a certain range. The model has good robustness, so it is proved that the strategy we give is the best.

4.3 Yield of the Strategy

In the real economic market, because the issue of paper money sometimes exceeds the actual amount needed in circulation, there is often inﬂationso we need to manage money.Under diﬀerent levels of inﬂation, the portfolio is diverse.In reality, money, stocks and bonds are generally used as investment representatives.The portfolio in this question only includes gold ,bitcoin and cash.

Set the bank deposit interest rate as r, inﬂation rate as I,deposit amount as a, Then the actual value of the deposit after ﬁve years is

A = a(1+r−I)5 (17)

Where A represents the actual value of the money after ﬁve years of deposit in the bank.

It can be seen from the data, from 2016 to 2021,the inﬂation rate was 7%, the bank deposit interest rate was 0.5%, so the actual value of $1000 after ﬁve years is $139.2436.In contrast, with our portfolio, our total assets are $14312.6827, $50040.5474 and $132089.1078 respectively when we choose insurance, common and radical investments. The results obtained by our model are several times higher than the more conservative ﬁnancial behavior, so our model has higher income and can resist inﬂation.

5 Problem 3: Sensitivity of Strategy to Transaction Cost

Based on the transaction strategy model established by the ﬁrst question, we can get the sensitivity of the strategy to the transaction cost by changing the cost α in the model and observing the corresponding changes of transaction frequency, asset return and asset risk.

5.1 Sensitivity Diﬁnition

Set initial variable α by α0, the initial transaction frequency h is h0 . After changing K(k = 1, 2, ..., 10) times, the variable α by αk. The corresponding transaction frequency h is hk.Sensitivity is deﬁned as: P10 |hk−hk−1| × 100% k=1 hk−1 (18) 10

This indicator reﬂects the change rate of transaction frequency.

5.2 Impact of Transaction Costs on Strategy

In question 2, we divide the strategy model into insurance type, common type and radical type. When exploring the impact of cost on strategy, we should also consider these three aspects. Let’s take the common type as an example to explore the impact of various changes of α on the strategy. We mainly explore through transaction frequency, asset return and asset risk, in which asset risk is characterized by the variance of return. Speciﬁcally, it is investigated through the changes of the following four costs.

a. αg fell 0.1% each time and αb remained unchanged.

b. αg remained unchanged and αb fell 0.2% each time.

c. αg rise 1% each time and αb remained unchanged.

d. αg remained unchanged and αb rise 2% each time.

change in the cost of gold will not have an impact on traders’ decisions.

(a) Changes of transaction frequency (b) Changes of return (c) Changes of risk

The result of case c is shown in the ﬁgure 15. In this case, we increase the transaction cost of gold by 0.1% each time. After reading the picture, it is found that:

1. If the cost increases to a certain extent, it will reduce the number of transactions and the total income.

2. The cost increases, the transactions become less, and the possible risks are reduced.

3. The changes of the three indicators are synchronous and consistent.

It can be seen that in the face of the continuous rise in the cost of gold, our model has not ignored, keenly felt this signal, and the change direction is in line with the reality. The strategy is relatively sensitive to transaction costs.

(a) Changes of transaction frequency (b) Changes of return (c) Changes of risk

bitcoin respectively.

Insurance-type Common-type Radical-type

αg 0.0267 0.0422 0 αb 0.2308 0.0658 0.0123

Through the data in the table, we can ﬁnd that:

• The sensitivity of trading strategy to the cost of bitcoin is higher than that to the cost of gold.

• The insurance-type strategy is more sensitive to the cost of bitcoin, and the common-type strategy is more sensitive to the cost of gold.

• The sensitivity of radical-tupe strategy to cost is generally low.

6 Conclusion

6.1 Strengths

• Our model puts forward variable parameters to form a parameter list. By changing the parameters in the list, we can achieve diﬀerent income results. In the future, we can form an investment prediction software according to the model. We only need to understand the meaning of relevant parameters to realize asset management. Therefore, our model is relatively simple and easy to understand.

• The parameters in the model have a large variable range and are more ﬂexible.

• The model is only based on the price changes of gold and bitcoin in recent ﬁve years, so the model has low requirements for data.

6.2 Possible Improvements

• In the process of solving the model, the mixed purchase strategy of gold and bitcoin is not well considered, which needs to be improved.

• Due to the lack of ﬁnancial knowledge, the establishment of the model is not necessarily perfect.

7 Memorandum

Memorandum

To: traders

From: Team #2203120

Subject: Investment model, Trading Strategy and Results of Bitcoin and Gold

Date: February 22, 2022

With the development of economy and the popularization of ﬁnancial management concept, more and more people have joined the ranks of investment. In addition to the traditional treasury bonds, funds, stocks, gold and so on, virtual currency has increasingly appeared in people’s vision, setting oﬀa "currency speculation fever". Investment involves both returns and risks. In order to explore the best trading strategy, our team has established a trading strategy model based on the price trend of gold and bitcoin in the past ﬁve years to help you better invest.

STRATEGY

The strategy we designed mainly focuses on three questions: when to trade, what kind of assets to trade and how much to trade.

When to trade. We measured the hit rate of the current model, the rise and fall of gold • and bitcoin, and the proportion of cash after trading. Only when the three indicators meet the trading conditions at the same time can the transaction be carried out, and it is decided whether to buy or sell. On the contrary, if the trading conditions are not met, wait until the next cycle for judgment

• Deal what. By setting the threshold of increase and decrease, compare the rise and fall range of gold and bitcoin, measure the risk and return of trading bitcoin and gold, and decide to trade gold or bitcoin.

• How much is the deal. If we decide to buy, we will use the decision coeﬃcient of the current model to decide how much to buy. When the judgment coeﬃcient is small, it means that the model we currently use is relatively stable and the risk is small. Therefore, when purchasing, we can appropriately increase the purchase proportion, on the contrary, reduce the purchase proportion; If we decide to sell, we will sell according to the preset proportion.

For the above strategies, by changing the variable parameters in the strategy, three strategies can be formed: insurance type, common type and radical type, which are suitable for diﬀerent traders and have good generalization ability. Secondly, when the variable parameters in the strategy are disturbed, the results show that the total assets change within a certain range, indicating that the anti-interference ability of the model is strong. Finally, by comparing the beneﬁts of $1000 deposited in the bank for ﬁve years and the ﬁve-year trading of this strategy, it can be seen that our strategy can resist inﬂation to a certain extent.

MODEL

The strategy is based on the prediction of the future. In view of the simplicity and eﬃciency of ARIMA model, which only needs endogenous variables rather than other exogenous variables, we choose ARIMA model as the price prediction model. In order to predict the future market timely and accurately, we use the data of 30 consecutive days as the training set and the data of the next 3 days as the test set. The correlation coeﬃcient R2 between gold’s prediction result and the real value is 0.8591, and bitcoin’s R2 is 0.9304, which are close to 1, indicating that the correlation between the predicted value and the real value is strong and the prediction accuracy is high. Such prediction lays a solid foundation for follow-up work.

The determination of trading strategy is essentially a dynamic programming problem. We need to maximize the return while taking into account the risk. Therefore, establish the objective function:

wj,mj Aj −λ × Sj max

where, Wj represents the roportion of gold and bitcoin bought on day j, mj represents the roportion of gold and bitcoin sought on day j, Aj represents the total assets on day j, λ represents the coeﬃcient of regular term, which is used to control risk and return, Si represents the current day risk.

By changing the coeﬃcient of the regular term λ, the risk can be adjusted and divided into three investment strategies: steady investment, common investment and radical investment.

RESULTS

Through the training of parameters, we have obtained models for three diﬀerent populations. The best returns and some transaction information of the three models are shown in the table below:

Insurance-type Common-type Radical-type

Total assets 14312.68 50040.55 132089.11 [C, G, B] [11474.39, 1.59, 1.07] [421.14, 0.61, 1.05] [22.31, 0.16, 2.84] Number of transactions 85 58 9 SD 3861.73 15501.99 40067.35

Through the analysis of the results, we can see that:

• The amount of investment is mainly bitcoin.

• Insurance investment tends to trade many times and is vulnerable to market inﬂuence. Ag- gressive investments make fewer transactions.

Appendices

Appendix A

Changes of Various Types of Traders’ Assetes

(a) Changes of cash (b) Changes of gold (c) Changes of bitcoin

(a) Changes of cash (b) Changes of gold (c) Changes of bitcoin
