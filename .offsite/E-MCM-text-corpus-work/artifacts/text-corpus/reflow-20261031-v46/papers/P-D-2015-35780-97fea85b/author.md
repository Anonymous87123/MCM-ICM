Sustainability is a comprehensive concept to describe a pattern of development without losing coordination or over consuming resources. Our research is divided into three steps: assessing and forecasting sustainability, formulating development plan, and involving ex- ternal factors.

Firstly, an Entropy-GE Matrix is adopted to create a measurement of sustainability and a state equation constructed from Lanchester’s Equation is employed to forecast trends of sustainability.  We set up a Sustainable Development Indicator system and normalize data of indicators. Aiming at assessing comprehensive performances, we adopt an Entropy-GE Matrix to establish concepts of Development Index (DI), Cooperation Index (CI) and a final score. Based on Lanchester’s Equation, we furthermore construct a state equation to forecast sustainability. In our result of 10 countries’ rankings on sustainability in 2013, America occupies the first place with a score 0.161 while Congo is the last with a score 1.142. As for another result, we obtain a 20-year forecast for three sample countries (America, China, Congo).

Secondly, we study on effectiveness of control elements ci , bi in control matrices and utilize a dynamic programming method to design a 20-year plan for Congo. Using the concept of state space from control engineering, we convert effects of a plan on sustain- able development into effects of control matrices on the state equation. In a case study on Congo, the control variate method is adopted to analyze effectiveness of ci , bi , and dynamic programming is applied to obtain a 20-year optimal plan. With the plan, DI and CI of Congo will dramatically increase in following 20 years. In order to specify our plan, development activities and their effectiveness scores are studied. In the plan for Congo, an economic activity of technical support is strongly recommended.

Thirdly, effects from external factors are considered in our model. By adding an external control matrix consists of Gaussian random numbers to the state equation, we can simulate effects of external factors on sustainable development of Congo. In the result, although external perturbation can cause fluctuation on performances, our plan can still guarantee a rising trend of sustainable development.

Finally, we analyze the stability of our model with a OAT/OFAT method and its result demonstrates that our model can undergo disturbance in a certain extent. Besides, we conclude the strength and weakness of our model.

Introduction

The concept of Sustainable Development (SD) was derived from forest management in early [1]. In recent decades, with the continuous development of modern so- 12th to 16th centuries ciety, the concept of SD evolved and was broadened. It was not until 1987 had this concept been deﬁned by the United Nations World Commission on Environment and Development in its report Our Common Future deﬁnes sustainable development. The report deﬁnes:" Sustain- able development is development that meets the needs of the present without compromising the [2]. While this is the most commonly used ability of future generations to meet their own needs" deﬁnition, it is not the only one. A pragmatic version with economic nuances was formulated by the OECD Environment Committee which considers that sustainable development means "maximizing the net beneﬁt of the economic development, while maintaining the dimensions of [3]. To measure the progress of quality and production at the level of the resources over time" sustainability, sets of Sustainable Development Indicators (SDI) have been created by many [4]. At organizations include World Bank, World Resource Institute, Worldwatch Institute etc present, problems like over increased population, poverty, shortage of energy resources, and environmental pollution remain to be crucial global issues. Without effective ways to solve these problems, they will ﬁnally cause disasters to earth environment and lead to human society collapse. Hence, SD has its unprecedented signiﬁcance in today’s world.

To create a more sustainable world, the International Conglomerate of Money (ICM) is in- terested in investing developing countries. Therefore, following tasks are to be accomplished:

• A measurement to characterize sustainability of a country is needed. By considering various factors like environmental quality and social status, the model should clearly extinguish sustainable countries from unsustainable ones.

• A 20 year sustainable development plan should be created to help a Least Developed Country (LDC) to gain a more sustainable future.

• The effect our 20-year plan has on the sustainability measure of the selected country should be evaluated.

According to existent materials, various sets of SDIs have been created by different countries, organizations, as well as researchers. Among them, the most well-known one is the standard published by Eurostat aims at monitoring the progress towards sustainable development strategy in EU countries. Over 100 Indicators used are divided into three categories: social, environmen- [5], as shown in Figure 1. Other studies also consider wider perspectives, for tal and economic [6]. However, example, cultural diversity and cultural well-being by Jelena Zlatar etc. in 2014 there is still not a global consensus of indicators used to measure SD. In line with various SDIs, studies use models and measurements to comment on sustainability of a country or a region. For instance, Liu Dan constructs an evaluation index system of resource-based city sustainable [7]. Jiali Huang uses eco- development using a BP neural network model and a genetic algorithm [8]. logical network analysis (ENA) to quantify the growth and development of Beijing city

To give advises for future policies and investments to improve sustainability, researchers have done many qualitative analysis. Anthony Crabbe concludes three strategies: charitable strate- [9]. Vatroslav gy, network strategy and social business strategy to enhance regional sustainability [10]. However, Zovko elaborate impacts GNI index and education have on future development most of the previous work lack quantitative analysis; therefore the advises they provide could not give decision makers strong and clear instructions on policy making and plan designing. On this stage, a better model for development planning is valueable.

Considering the existent research, our research focus on sustainability measurement, sustain- ability forecast, as well as sustainability control and adjustment. Detail work is as follow:

1) We create our own system of Sustainable Development Indicators and provide with a mea- surement of sustainability based on the entropy theory and the GE-Matrix.

2) We also conduct a way to forecast sustainability using Lanchester’s Equation and theory of the state equation.

3) We study the control and adjustment a plan can have on the sustainability by doing further deduction on the state equation and acase study on Congo.

4) Further work in our research focuses on effects from external inﬂuence of the system.

2

Assumption

We assume that effects of external factors on our model obey the Gaussian Distribution. We made this assumption based on reality, because the kinds of external effects considered in our study (e.g. climate change, international aids) seldom have abnormal strong impacts on the original model. Under this assumption, we can easily quantify the external effects in our study.

3

A Model for Sustainability

In this section, we ﬁrst set up a system of Sustainable Development Indicators (SDI). Subse- quently, we provide a complete measurement to score a country’s sustainability. Next, we pro- vide a method to forecast sustainability. Finally, the results of country rankings and a 20-year forecast are demonstrated.

3.1 Sustainable Development Indicators (SDI)

In order to give a well-rounded description of Sustainable development, a series of indicators is used, which are called Sustainable Development Indicators (SDI). Since there is no glob- al consensus of how SDI should be selected, we therefore choose the indicators based on 3 principles:

• The indicators should be as comprehensive as possible to include most parts which are effective to sustainability.

• The indicators had better be easy to be controlled and regulated through government policies and feasible plans.

• The indicators which have already been tested reasonable in existent researches have a priority.

Based on these three principles, we construct a group of indicators in 3 levels, shown in Ta- ble1. The ﬁrst level contains three widely acknowledged aspects, namely environmental, social and economic. The second level contains 9 sub-aspects, three for each layer. On choosing sub-aspects, we considered three most stressed global problems in nowadays under each as- pects(Since the economic aspect only have two levels, the way to choose its sub-aspects is combined with the way of choosing third layer indicators).For example, ... Finally, to choose the third level indicators, we identiﬁed them from following 3 resources:

[11] with a focus on 12 headline indica- (a) More than 100 indicators are identiﬁed by Eurostat tors. These indicators have been used to monitor the EU Sustainable Development Strategy for over 10 years.

(b) 52 international indicators constructed by Liyin Shen to evaluate sustainable urbanization.

[12] The realiability has been tested through the author’s case study of China

(c) 37 indicators concluded by Jelena Zlatar from studies on SDI from 2001 to 2012 in aspects [6]. include environmental social and economic

Among these resources, we pick indicators that appear twice which meanwhile belong to one sub-aspect. Importantly, in order to provide convenience for decision makers, we also consider indicators which do not appear twice but can be easily controlled by policy, for example, edu- cation expense percentage in GDP. After all, we construct a SDI system which will be used as the foundation of our model.

3.2 A Measurement of Sustainability

We provide a complete way to measure sustainability. To start with, data normalization ways are introduced. Then the Entropy Method is adopted to determine weight of indicators and calculate comprehensive performances on environmental, social, and economic aspects . Con- sequently, we deﬁned Development Index and Coordination Index to describe sustainable de- velopment of a country. Finally, a GE-Matrix is used to score sustainability.

Level1 Level2 Level3 Population growth Population Population density The aging rate Environment Forest rents in GDP Resources Energy use per capita Pullotion CO2 emission per capita Life expectancy Health Mortality rate Health expenditure per capita Tertiary school enrollment rate Social Education Education spend in GDP Depth of the food deﬁcit Livelihood Improved water source with access Household expenditure per capita Per Capita GDP Economic Inﬂation Tertiary industry rate

3.2.1 Data Normalization

Considering that data of SDI measured on different scales, it is necessary to a standardize them into a notionally common scale. Therefore all data in our research need to be adjusted before used in models.

All the 17 indicators we study on can be divided into three categories while normalizing: posi- tive indicators which exert positive effect on sustainability, negative indicators which do nega- tive effect on sustainability, and special indicators. In our model, assume that n (n=17) indica- tors and m samples of countries are considered. In following equations, xij (xij>0) represents the original value of indicator i for sample country j, where (i=1,2,...,n) and (j=1,2,...,m). rij is the proximity of xij towards the relatively best value of indicator i among all samples. For values of positive indicators, bigger is better. Thus, following equation is obtained:

xij rij = maxj(xij) where maxj(xij) is the best value of positive indicator i, which means the maximum value of indicator i among all m sample countries. Oppositely, as for absolute value of negative indicators, smaller is better. Hence, we have:

rij = minj(xij) xij where minj(xij) is the best value of negative indicator i, which means the minimum value of indicator i among all m sample countries. Based on Equation (3.2.1)-(3.2.1), we get the nor- malized value fij of positive or negative indicator i for sample j:

rij Pm fij = j=1 rij However, there are special indicators which can not be categorized into positive or negative indicators. One condition is that the best value of the indicator is a ﬁxed one or original values of the indicator are negative or 0. When the value is 0, we replace it with 0.0001, which has little impact on the ﬁnal result. The other condition is that the normalized value of one indica- tor is effected by other indicators. There are 3 special indicators in our SDI system and their normalization processes are as follows:

1) Inﬂation (annual %) Because the value of inﬂation can be negative (equivalent to deﬂation in a positive value) and the best value of inﬂation is 0, its normalization equation can be expressed as:

|INF| fINF = 1 − |INF|max where fINF is the normalized value of inﬂation; INF is the original value of inﬂation;

|INF|max is the maximum absolute value among all samples. 2) Population Density (per/km2) [13], both overhigh and overlow population densi- According to research by Alberto Martilli ty harm social development, and are negative to environment and energy efﬁciency. The proper population density should be 60-100 per/ km2. Another study from Hao Hu, Kari- [14] also suggests that when population density is under 100 per/ km2, the ma Nigmatulina diseases transmission can be cut into a lower speed. The normalization equation is:

DP −DPAP fDP = 1 − |∆DP|max where fDP characterizes the normalized value of population density; DP is the original value of population density; DPAP is the best value of population density; |∆DP|max rep- resents the maximum absolute difference between DP and DPAP.

3) Population Growth (%) [15], population growth is related to population density On referring to J.V. Ross’s research and its normalized way is:

 1  DP ≤DPAP DP −DPAP PG− +1 DP fPG = 1  DP > DPAP DP −DPAP PG+ +1 DP

where fPG is the normalized value of population growth and PG is its original value.

3.2.2 The Comprehensive Performance

The Entropy Method is derived from thermodynamics and is later introduced to telecommu- [12]. Previous studies have successfully used this nication, energy, ﬁnance and other disciplines [16]. method to determine the weight of a group of indicators which are used for evaluation

The Entropy Method suits for our study because our original data of indicators are trivial there- fore hard to analyze. By adopting a Entropy Method, we can process the data (after normal- ization) into three main variables, representing environmental, social, and economic aspects;

hence the analysis on data can be easier to approach and clearer to understand.

To start with, the entropy value Hi of indicator i is obtained by Equation (3.2.2)

X m Hi = −k fij · ln fij j=1 1 where i = 1, 2, 3, ..., n; k = ln m Accordingly, we determine the weight wi of indicator i by Equation (3.2.2)

1 −Hi Pn wi = i=1(1 −Hi) Hence, the comprehensive performance of sample j by considering indicators 1 to n can be deﬁned as X n wi · fij Fj = i=1 Since our SDI system set up in Section 2.1 has three main aspects, we accordingly get three Fs to describe the comprehensive performance of a country (j omitted in the equation) on environmental (en), social (so), and economic (ec) aspects. Descriptions are shown in Equation (1) X nen wi(en) · fij(en) Fen = i = 1, 2, ..., nen i=1 X nso (1) wi(so) · fij(so) Fso = i = 1, 2, ..., nso i=1 X nec wi(ec) · fij(ec) Fec = i = 1, 2, ..., nec i=1

3.2.3 Development Index and Coordination Index

Sustainable development is a concept which requires both development and coordination. To be coordinated requires a country to improve itself not only in one aspect but in all aspects at the same time. In our model, we use a Development Index (DI) to depict a overall development status and a Coordination Index (CI) to depict the consistency and coordination of develop- ment among environmental (en), social (so), and economic (ec) aspects. Both index are based on comprehensive performance on aspects (en, so, ec). It is only when DI and CI are both high can we consider a country to be a sustainable one. Here we deﬁne Development Index (DI) to be

DI = CF     T γ1 Fen (2)     γ2 Fso where C = ; F = γ3 Fec The parameters γ1, γ2, and γ3 in C show weight of Fen, Fso, Fec when composing DI.

[17]: The Coodination Index (CI) is deﬁned as

CI = 1 −S ¯F r 1 (3) 3[(Fen −¯F)2 + (Fso −¯F)2 + (Fec −¯F)2] where S =

¯F = 1 3(Fen + Fso + Fec) S is the standard deviation of the three performance values, and ¯F is the arithmetic mean value of the three.

3.2.4 A GE-Matrix to Score Sustainability

The GE-Matrix (McKinsey Matrix) is originally used in evaluating competitiveness and at- tractiveness of a company in a two-dimensional frame. The matrix can provide company with management and development strategies. Here we consider to use GE-Matrix to depict sustain- ability of countries.

Although there are difference between companies and countries in operation, management, and proﬁt perspectives, a fairly reasonable analogy can still be made. On the one hand, company attractiveness describes the strength of a company to make proﬁt; correspondingly, country De- velopment Index describes strength of a country on development. On the other hand, both com- pany competitiveness and country Coordination Index reﬂect a well-rounded capacity. Hence, a [12] shows the matrix we adopt. Both DI and CI can be classiﬁed GE-Matrix is adopted. Figure 2 [18] as shown in Table 2. in to three levels according to research by Li, Zhang, and Song

DI Development level 0-0.5 Weak development 0.5-0.8 Medium development 0.8-1 Strong development

CI Coordination level 0-0.5 Weak coordination 0.5-0.8 Medium coordination 0.8-1 Strong coordination

ment Index and Coordination Index

With DI value y and CI value x of a country in any given year, we can determine a position (x, y) in our GE-Matrix. The distance between (x, y) and the best position (1, 1) is regarded as our sustainability score of a country in one year. The lower the score is, the more sustainable a country is.

3.3 A Forecast on Sustainability

We provide a method to forecast sustainability of a country by using Lanchester’s Equation. Initially, the mechanism of Lanchester’s Equation is introduced. Later, we develop this equation into our own use and provide with a state equation.

3.3.1 Mechanism of Lanchester’s Equation

[19]. Lanchester’s Equation is originally used in combat to assess loss of soldiers from both sides It is a nonlinear ﬁrst order differential equation which can obtain dynamic changes of the system under different war strategies. The equation is described as  dx dt = −ay −αx + u(t) dy dt = −bx −βy + v(t) where a and b are attack strength from one side to the other; α and β are loss of soldiers due to reasons other than attacks; u(t) and v(t) represent supplement of soldiers.

3.3.2 Our State Equation

We know that Lanchester’s Equation provides a model for war, but we "buy" it a new coat of peace in our model. We use it to obtain the dynamic process of sustainability and forecast sustainability changes. This new coat ﬁts well since Lanchester’s Equation can provide an e- quation to characterize not only effect on self aspect,but also effects of interaction among all aspects and effects from outside of the system.

Take the social aspect from our SDI system as an example, it contains 3 second level aspects (health, education, livelihood) and 8 third level indicators (life expectancy, education spend, health expenditure etc.). All the third level indicators reﬂect citizen’s living quality in a country. However, the living quality will also be effected by environment (forest coverage, co2 emission etc.) and country economics (inﬂation, GDP per capita etc.). Lanchester’s Equation embodies the interaction among environmental, social ,and economic aspects clearly.

Moreover, there are effects from outside of a country like ICM provided programs and aids. Therefore, we compare outsider effects on country sustainability ˆUi(t) to soldier supplement in original Lanchester’s Equation. We use ﬁtting method to get coefﬁcient βi. We therefore get our Lanchester’s Equation equation   = α11Fen (t) + α12Fso (t) + α13Fec (t) + β1 ˆU1 (t) dFen(t)  dt = α21Fen (t) + α22Fso (t) + α23Fec (t) + β2 ˆU2 (t) dFso(t)  dt  = α31Fen (t) + α32Fso (t) + α33Fec (t) + β3 ˆU3 (t) dFec(t) dt Using denotation ways from state space theory, we get the state equation

dF dt = AF + B ˆU         T ˆU1 (4) Fen α11 α12 α13 β1         ˆU = ˆU2 Fso α21 α22 α32 β2 where F = A = B = ˆU3 Fec α31 α32 α33 β3 In Equation (3.3.2)-(4), Fx (x = en, so, ec) denotes the comprehensive performance of a coun- try on aspect x. F is comprehensive performance to measure sustainability of a country; A is a system matrix which describes interaction among the three aspects; elements in ˆU describe effects from outside of a country; B is an input matrix to control a country’s capacity on adjust- ing to outside effects. In our ﬁrst stage study, B ˆU is ignored.

On adopting Equation (4), we convert discrete time T to continuous time t.

t = kT k = 1, 2, 3, ...n That is to say, we can obtain continuous data from original inputting discrete data. Hence, the dynamic change of sustainability and possible future value of comprehensive performance F on environmental, social, and economic aspects can be got.

3.4 Results

3.4.1 Country Rankings

[20]. The data cover all 17 indicators in We acquired original data from World Bank Database our SDI system. Ten sample countries are selected from 5 different continents and covers both developed countries and developing countries. Based on our model in Section 2.2, sustainability scores of sample countries in year 2013 are calculated. The rankings are shown in Table 3. The lower the score is, the more sustainable a country is; hence the United States ranks the highest among all the countries, and Congo ranks the lowest.

Rank Country Fen Fso Fec DI CI Score 1 U.S. 0.378 0.343 0.439 0.876 0.897 0.161 2 U.K. 0.164 0.277 0.386 0.625 0.672 0.499 3 Brazil 0.085 0.050 0.056 0.144 0.761 0.889 4 China 0.122 0.213 0.035 0.279 0.408 0.932 5 South Africa 0.147 0.053 0.057 0.195 0.494 0.951 6 Bangladesh 0.015 0.012 0.006 0.025 0.635 1.041 7 Central Africa 0.020 0.015 0.005 0.030 0.521 1.082 8 Cambodia 0.022 0.010 0.007 0.030 0.517 1.084 9 Nepal 0.023 0.016 0.004 0.032 0.478 1.100 10 Congo 0.023 0.014 0.003 0.031 0.396 1.142

3.4.2 A 20-Year Forecast

We use data from 2009-2013 to forecast the comprehensive performances on environmental, social, and economic aspects for different countries based on the model introduced in section 2.3. An analytical-least square method and function ODE45 are used to determine the coef- ﬁcients in our forecast model. We therefore picked three countries (the US, China, Congo) as representatives of countries from three classes: countries already have good performances, countries which have a low performance but is improving, and countries which maintain a low performance now and in future. A 20-year prediction of three sample countries are shown in Figures 3-4.

performances of three countries three countries

In Figure 3, comprehensive performances on environmental, social and economic aspects of the US, China and Congo are embodied. We can discover that the economic performance of China will rise largely in 20 years comparing to others.

A comprehensive view of our 20-year prediction is shown in Figure 4 under the frame of a GE-Matrix. On referring to classiﬁcation ways in Table 2, we notice that the United States has a strong performance in coordination and a medium performance in development at present; in 20 years, its development will be strengthen while its coordination will remain a high standard. Moreover, we noticed that China is developing towards an imbalanced direction. Its coordina- tion remains weak in 2029. As for Congo, situation worse in 2029 since both index will go towards zero.

Therefore, countries like China should adjust its policies towards a better direction rather than focusing on economic development; countries like Congo needs more aids on all aspects.

4 A Sustainable Development Plan

In this section, we create a model to describe a sustainable development plan on a country by adding control elements into the state equation. The optimal result of the model is obtained by using dynamic programming. At last, we do a case study on Congo.

4.1 Adding Control into the State Equation

We add control from the plan to our original state equation by direct and indirect control matri- ces. The mechanism of this control is explained in details by effectiveness of control elements in matrices.

4.1.1 Direct and Indirect Control Matrices

This control measure is developed on the base of our original state equation (Equation (4)). In order to add effects of control from the plan to the system matrix A, we discrete original state equation as below dt = Fk+1 −Fk dF T Therefore the state equation (Equation (4)) is converted into         h i Fen 1 + α11T α12T α13T Fen β1         ˆU1 ˆU2 ˆU3 Fso α21T 1 + α22T α32T Fso β2 = + k Fec α31T α32T 1 + α33T Fec β3 k+1 k

which equals to Fk+1 = ¯AFk + B ˆUk (5) The discrete equation above clearly indicates that system matrix ¯A and input matrix B both have effects of control on comprehensive performances Fis. In addition, Fi values are bigger than zero; meanwhile, the bigger the values are, the more favorable the result is. Overall, we can control a country’s sustainable development trend by controlling ¯A and control a country’s capacity on adjusting to outside effects by controlling B .

A sustainable development plan is used to change a country’s sustainable development trend, so the mathematical description of state equation after adding the plan is created as

F′ = (GcAAF + UbA) + B ˆU (6) Figures 5-6 are ﬂowcharts of change of F′ before and after executing the plan.

executing the plan executing the plan

GcA is an indirect control matrix, since the plan can indirectly exerts control by using GcA to inﬂuent system matrix A. Here we ignore elements in GcA which have coupled effects on A. Therefore   c1 0 0   (7) 0 c2 0 GcA = 0 0 c3 where cis are indirect control elements from the plan. Properties of ci are shown in Table 4.

ci < 1 ci > 1 Plan reduces original negative effect Plan enhances original negative effect αij < 1 Plan reduces original positive effect Plan enhances original positive effect αij > 1

UbA represents direct control from the plan. With direct control, plans or policies focusing on one aspect only exert inﬂuence on that aspect. Hence, UbA equals to a proportion of the original comprehensive performance F. The proportion is characterized by a direct control ma- trix GbA as follow     b1 0 0 Fen     (8) 0 b2 0 Fso UbA = GbAF = 0 0 b3 Fec Eventually, the state equation after adding a control plan is expressed as F′ = (GcAA + GbA)F + B ˆU = GAF + B ˆU (9)

4.1.2 Effectiveness of Control Elements

The 6 control elements bis and cis are interacted with each other when exerting effects on sus- tainable performance F, and therefore the effect caused by single element is hard to observe. We use the control variate method to discuss effects on comprehensive performances (Fen, Fso, Fec) and Sustainability Score when each control elements change in a certain degree. This discussion provides a foundation for plan-solving.

Under a special condition when ICM do not offer any aids, the indirect control matrix GcA becomes an identity matrix and the direct control matrix UbA becomes a null matrix. There- fore, the two matrices do not effect system matrix A, and the state equation (Equation (6)) becomes identical with the one without plan (Equation (5)).

Under a normal condition with aids, we discuss ci by setting   ci = 1 ± k · p  i̸ = j cj = 1,   bi = 0 where k represents interval quantities; p represents interval length. We discuss bi by setting   bi = k · p · αjj  i̸ = j bj = 0,   ci = 1 where k represents interval quantities and p represents interval length.

4.2 A Dynamic Programming Solution

In order to give the result of an optimal 20-year plan, we have to choose a suitable method to solve our model. Our plan making problem is indeed a multistage decision making problem; therefore, a dynamic programming algorithm is adopted.

1) Stage and stage variables n We divide the 20-year plan into 4 stages; every 5 years is a stage n. k represents the time unit of year

2) State variables S The state variables are Fen, Fso, Fec. Index DI and CI can be calculated via them.

3) Decision variables X Decision variables are expressed as GA = GcAA + GbA, which includes control elements ci and bi (i=1,2,3). Value range of control elements are determined by effectiveness analysis on them.

4) Strategy A strategy is a set of decisions. Expressed as {GA(1), GA(2), GA(3), GA(4), } 5) State transition function The state transition function in stage i is F ′ = GA(i)F + B ˆU. In addition, initial values of state variables in stage n equals to ﬁnal values of state variables in stage n −1. 6) Value function V A value function is a quantitative indicator of how good the process is. Here value function Vn represents a sum of every year sustainability scores in stage n.

X X X 4 4 5 V = Vn = Scorenk(sn, xn) n=1 n=1 k=1

represents the value function of the entire process.

4.3 Development Activities in Practice

Concrete policies and aids are crucial for an effective sustainable development plan, while all of them should consider both development and coordination at the same time. So when creat- ing a 20-year sustainable development plan, the effectiveness of speciﬁc development activities should be evaluated ﬁrst. Only in this way can we clarify how the plan acts in matrix GA and B, and whether it performs well or badly. There are many development activities bringing direct or indirect beneﬁts through programs, policies, and aids which can be provided by ICM.

[22] used the method of Strategic Environmental Assessment (SEA) Sharifzadegan and Gollar to assess a strategic plan and different development activities. With the help of this research we can obtain Table 5 which reveals development activities and their score of effectiveness in detail.

development activities score The reduction of air pollution in the civic and residential areas 0.20 Protecting the agricultural lands and forests 0.23 The reduction of air pollution 0.13 environmental Transferring the obtrusive industries to the industrial towns 0.13 Preventing from contamination of the water resources 0.17 No damaging to the protected areas 0.13 Strengthening the infrastructure 0.04 Improve the sewage disposal 0.12 Create sustainable communities and recognize urban growth 0.18 Renewal of informal settlements 0.26 social Accessibility to public transportation systems 0.12 Control housing and offer residential use 0.07 Improve road infrastructures and built new roads 0.14 Guarantee water supply by new water supply company and pipes 0.07 Transferring the obtrusive industries to the industrial towns 0.19 Using the huge social and accumulated capital for the expansion of the employment 0.13 Investment in local companies 0.16 economic Technical support 0.23 Provide measures to amend by the home occupation and cottage industry regulations 0.10 Finances this organization 0.19

In order to give concrete form of a plan using the development activities in the table, a series of work should be done:

Step 1 We can analyze the effects each one of control elements bi, ci have on the comprehen- sive performance F using method in section 3.1.2.

Step 2 Subsequently we use dynamic programming as indicated in section 3.2 to determine the optimal value of control elements bi, ci

Step 3 The importance rankings of environmental, social and economic aspects and the score of activities under each aspect can collectively determine the activities’ strength in the plan.

4.4 A Case Study on Congo

In this part, we will do a case study on Congo (Democratic Republic of the Congo), one of the Least Developed Countries (LDC). According to our previous result in Figure 4, Congo’sp Development Index and the Coordination Index are nearly going to be zero by 2029. (Congo is in a deep crisis!) Thus, receiving aids from ICM will be like clutching at straws for Congo.

To start with, we give quantitative analysis on effects control elements have in a Congo case. Subsequently we obtain a new 20-year forecast with a plan-controlling for Congo and compare it with the forecast without plan. Finally, some practical development activities are provided within the plan.

4.4.1 Adjusting Control Elements [20] and adopting a control variate method By using data collected from the World Bank Database introduced in section 3.1.2, we can get effects each control element has on comprehensive performances as well as DI and CI of Congo. Partial results are shown in Figures 7-10.

c1 changes b1 changes

ci changes ±5% bi changes ±2%

Figures 7-8 indicates effects c1 and b1 have on the Development Index when c1 changes ±5% and ±10% and when b1 changes ±2% and ±4%. We can observe that b1 has lager impact on DI than c1 has. Moreover, both c1 and b1 do positive effects on DI, that is to say, DI increases when either c1 or b1 increases.

From Figures 9-10, clear comparisons among indirect control elements cis as well as among direct control elements bis are embodied. Among three cis, c2 has the largest impact on DI; among three bis, b1 has the largest impact. While among all 6 elements, only c2 does negative effects on DI.

4.4.2 20-year Forecasts with(out) Plan-controlling

Using the dynamic programming method introduced in Section 3.2 and based on our model added control elements, we therefore get a brand new forecast on Congo’s sustainability in 20 years, comparing to the original forecast made in section 2.4.2. The detailed comparisons of forecasts with and without a plan are shown in Figures 11-12.

In Figure 11, full lines are predictions of performances with a plan; dotted lines are those without a plan. All performances increases impressively after 20 years of plan controlling. Ac- cording to Figure 12, the development direction is a complete changeover after adding a plan. Without a plan, Congo is predicted to have index approximate to zero in 2029; however, with a plan, Congo is expected to reach a medium level on both development and coordination in 2033.

mance with(out) a plan plan shown in the GE-Matrix

4.4.3 The Plan in Practice

On adopting steps mentioned in Section 3.3 on the Congo case, we ﬁnd out that economic has the greatest importance on Congo’s sustainable development, social places a second. Hence following development activities (selected from Table 5)are recommended in our plan (Shown in Table 6):

Recommended level Development activities 1 Technical support (ec) Finances this organization (ec) 2 Renewal of informal settlements (so) Create sustainable communities and urban growth (so) 3 Protecting the agricultural lands and forests (en) Preventing from contamination of the water resources (en) 5 External Effects

5.1 Adding a Perturbation Matrix to State Equation

While a country can accept aid from ICM to improve its sustainability, the country may also be inﬂuenced by external uncertain factors. Some external factors (e.g. foreign investment, glob- alization)exert positive effects on sustainability; others (e.g. climate change, natural disasters) exert negative effects.

In Equation (6), the external effects are described by the external effect matrix B ˆU. B ˆU is commonly respected as a random matrix; its elements obey a normal distribution where µ = 0 and σ is determined by effect degree. Since elements in row i of B ˆU are in proportion to Fi, here we let

B ˆU = ˆAF where ˆA is a perturbation matrix of F; elements ˆαij in ˆA are perturbation increments and ˆαij ∼N(0, σ). Therefore, the ﬁnal expression of the state equation is obtained as F′ = (GcAA + GbA + ˆA)F (10)

5.2 A Revised Forecast on Congo

By setting σ = 0.4, we can obtain a revised forecast on Congo. The revised control elements are shown in Table 7. And a new forecast result of Congo after adding external perturbation inﬂuences are shown in Figure 13.

Control Elements 2014∼2018 2019∼2023 2024∼2028 2029∼2033 0.05 0.05 0.05 0.05 c1 -0.1 0 0.05 0.1 c2 0.5 0.4 0.4 0.35 c3 -0.1 -0.08 -0.04 -0.02 b1 0.05 0.02 0 -0.03 b2 0.5 0.5 0.5 0.45 b3

In Figure 13, performances vary drastically in some years, which indicates that external factors increase the difﬁculty of forecasting. When σ = 0.4, the overall increasing tendency of perfor- mances is still good, which proves that our development plan on Congo is still a favorable one. However, when σ ≥0.5, some performances will decrease to a negative value and have drastic ﬂuctuation. In conclusion, our development plan for Congo can only undergo external effects on a certain extent.

6 Stability Analysis

It is obvious that the development pattern of a country always changes, and the Linear Time- invariant Systems can never completely describe the change of SDI though it is capable of revealing the tendency. Thus, we do stability analysis on our model.

In section 3, sensitivity analysis is used to analyze the effectiveness of control elements bi and ci. With a similar processing mode,we can use sensitivity analysis to assess the stabilityof our model. We add disturbance to system parameter αij, and observe how the outputs deviate from [?] is used. Uncertainty Dij is derived from αij with expectations. Here, a OAT/OFAT method following equation:

X Fm(αij, k) −Fm(α′ ij, k) Dmij = 1 (11) m = en, so, ec k Fm(αij, k) k

Taking α12 as an example, we set αij = (1 + η)α′ ij, (η = −0.3, −0.25, ..., 0.03) and k = 2014, 2015, ..., 2018, and get a sensitivity analysis result shown in Figure 14. Obviously, although variation of α12 causes deviation of outputs, the deviation becomes sta- ble while variation of α12 becomes greater. When change rate of α12 belows 30%, the outputs change less than 11%. This shows that our model has stability to endure disturbance or calcu- lating error to a certain extent.

7

Strength and Weakness

7.1 Strength

7.1.1 Hierarchy

We embody the concept, sustainability of a country, in three speciﬁc indexes. They are environ- mental, social and economic, which can be regarded as the second level. Far more, every index in the second level consist of several indexes with statistical signiﬁcance like life expectancy, inﬂation and forest coverage rate from World Bank Data. These data serves as the third level. More statistical data we collect, more correctly will we estimate a country.

7.1.2 Quantiﬁcation

Our model standardizes statistical data with different dimension. Then, two scientiﬁc index called DI and CI are made to illustrate a country’s development and coordination degree. They can provide information which suggests organizations what they should pay attention to and how to deal with it. Meanwhile, countries can also be ranked by them and countries in crisis will come into notice.

7.1.3 Intersectionality

To describe the process of adjusting a country in poor into good condition is a difﬁcult task. We creatively use the Principle of Control to represent adjustment measures. The input of system can be regarded as a country’s initial situation while the output as situation after adjustment. The changes in controlling matrix are equivalent to assistance and policies. Environmental fac- tors play a role as nonhomogeneous item.

7.2 Weakness

We’d better conduct more sufﬁcient quantitative analysis on how speciﬁc strategies are con- nected with the direct changes on the abstract performance of sustainability. This requires us to collect more research data on a wider range.
